"""포트폴리오 사이트 자동 점검 스크립트 (Playwright + Chromium)

점검 항목: 1440/768/390px 가로 넘침, 깨진 요청·이미지, alt 누락, CSS 로딩, 메뉴 표시·터치 폭,
앵커 대상 존재, 내부 링크 200 응답, 폭 변경 후 메뉴 유지, Tab 순서·초점 표시, Enter 이동·뒤로 가기,
200% 확대(720px), 본문 바로가기, 404 페이지.

사용법 (저장소 최상위 폴더):
  pip install playwright && python -m playwright install chromium
  # 공개 사이트 점검
  python docs/tools/check_site.py https://won-ji1.github.io/portfolio/ docs/evidence/auto
  # 배포 전 로컬 빌드 점검: 공개 주소 요청을 public/ 폴더 파일로 응답
  python .github/pages_build.py --build
  python docs/tools/check_site.py https://won-ji1.github.io/portfolio/ docs/evidence/auto public
결과: OUTDIR/report.json 과 화면 캡처 PNG
"""
import json, sys, re, urllib.parse
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = sys.argv[1].rstrip('/') + '/'
OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
PAGES = ['', 'about/', 'activities/', 'activities/law-school/', 'activities/portfolio-site/']
report = {'pages': {}, 'issues': []}

def issue(msg):
    report['issues'].append(msg); print('ISSUE:', msg)

PUBLIC = Path(sys.argv[3]) if len(sys.argv) > 3 else None
import mimetypes
def serve(route):
    u = urllib.parse.urlsplit(route.request.url)
    rel = urllib.parse.unquote(u.path)[len('/portfolio/'):] if u.path.startswith('/portfolio/') else None
    f = None
    if rel is not None:
        f = PUBLIC / rel
        if f.is_dir() or rel == '' : f = f / 'index.html'
    if f is not None and f.is_file():
        route.fulfill(status=200, body=f.read_bytes(), content_type=mimetypes.guess_type(str(f))[0] or 'text/html')
    else:
        route.fulfill(status=404, body=(PUBLIC / '404.html').read_bytes(), content_type='text/html')

with sync_playwright() as p:
    _br = p.chromium.launch()
    class B:
        version = _br.version
        def new_context(self, **kw):
            c = _br.new_context(**kw)
            if PUBLIC: c.route('https://won-ji1.github.io/**', serve)
            return c
        def close(self): _br.close()
    br = B()
    report['browser'] = f'Chromium {br.version}'
    for width in (1440, 768, 390):
        ctx = br.new_context(viewport={'width': width, 'height': 900})
        page = ctx.new_page()
        failed = []
        page.on('response', lambda r: failed.append(f'{r.status} {r.url}') if r.status >= 400 else None)
        page.on('requestfailed', lambda r: failed.append(f'FAILED {r.url}'))
        errors = []
        page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        for path in PAGES:
            url = BASE + path
            page.goto(url, wait_until='networkidle')
            info = page.evaluate('''() => {
              const de = document.documentElement;
              const over = [];
              for (const el of document.querySelectorAll('body *')) {
                const r = el.getBoundingClientRect();
                if (r.width && (r.right > innerWidth + 1) && getComputedStyle(el).position !== 'fixed') {
                  // ignore elements inside a horizontally scrollable container
                  let p = el.parentElement, inScroll = false;
                  while (p) { const s = getComputedStyle(p).overflowX; if (s === 'auto' || s === 'scroll') { inScroll = true; break; } p = p.parentElement; }
                  if (!inScroll) over.push(el.tagName + '.' + el.className);
                }
              }
              const imgs = [...document.images].map(i => ({src: i.currentSrc, ok: i.complete && i.naturalWidth > 0, alt: i.getAttribute('alt'), w: i.getBoundingClientRect().width, ratio: i.naturalWidth ? (i.getBoundingClientRect().width / i.getBoundingClientRect().height) / (i.naturalWidth / i.naturalHeight) : null}));
              const css = [...document.styleSheets].map(s => { try { return s.cssRules.length } catch (e) { return -1 } });
              const menu = [...document.querySelectorAll('#menu a')].map(a => { const r = a.getBoundingClientRect(); return {t: a.textContent.trim(), h: Math.round(r.height), w: Math.round(r.width), vis: r.width > 0 && r.height > 0, x: Math.round(r.x), y: Math.round(r.y)} });
              const anchors = [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href'));
              const hs = [...document.querySelectorAll('h1,h2,h3')].map(h => h.tagName + ':' + h.textContent.trim().slice(0, 30));
              return {scrollW: de.scrollWidth, innerW: innerWidth, over: over.slice(0, 5), imgs, css, menu, anchors, hs, lang: de.lang, title: document.title};
            }''')
            key = f'{width}:{path or "home"}'
            report['pages'][key] = info
            if info['scrollW'] > info['innerW'] + 1:
                issue(f'{key} horizontal overflow {info["scrollW"]}>{info["innerW"]} {info["over"]}')
            elif info['over']:
                issue(f'{key} elements past right edge {info["over"]}')
            for im in info['imgs']:
                if not im['ok']: issue(f'{key} broken image {im["src"]}')
                if im['alt'] is None: issue(f'{key} image without alt {im["src"]}')
                if im['ratio'] and abs(im['ratio'] - 1) > 0.02: issue(f'{key} image distorted {im}')
            if any(c == 0 for c in info['css']) or not info['css']:
                issue(f'{key} stylesheet missing {info["css"]}')
            for m in info['menu']:
                if not m['vis']: issue(f'{key} menu item hidden {m}')
                if width == 390 and m['h'] < 24: issue(f'{key} small touch target {m}')
            # fragment targets
            for h in info['anchors']:
                full = urllib.parse.urljoin(url, h)
                u = urllib.parse.urlsplit(full)
                if u.fragment and full.split('#')[0] == url:
                    if not page.evaluate('id => !!document.getElementById(decodeURIComponent(id))', u.fragment):
                        issue(f'{key} missing anchor target #{u.fragment}')
                if h in ('', '#') or h.startswith('javascript:'):
                    issue(f'{key} empty link {h!r}')
            page.screenshot(path=str(OUT / f'{width}_{(path or "home").strip("/").replace("/", "_")}.png'), full_page=(width != 1440 or True))
        if failed: issue(f'{width} failed requests: {sorted(set(failed))}')
        if errors: issue(f'{width} console errors: {errors}')
        ctx.close()

    # Internal link crawl: every same-site link must return 200 and fragments must exist
    ctx = br.new_context(viewport={'width': 1440, 'height': 900}); page = ctx.new_page()
    seen = set()
    for key, info in list(report['pages'].items()):
        if not key.startswith('1440'): continue
        src = BASE + key.split(':', 1)[1].replace('home', '')
        for h in info['anchors']:
            full = urllib.parse.urljoin(src, h)
            if not full.startswith(BASE.replace('localhost', 'localhost')) and 'won-ji1.github.io/portfolio' not in full:
                continue
            full = full.replace('https://won-ji1.github.io/portfolio/', BASE)
            base_url, _, frag = full.partition('#')
            if (base_url, frag) in seen: continue
            seen.add((base_url, frag))
            r = page.goto(base_url, wait_until='domcontentloaded')
            if not r or r.status != 200:
                issue(f'link {h} from {src} -> {r.status if r else None}'); continue
            if frag and not page.evaluate('id => !!document.getElementById(decodeURIComponent(id))', frag):
                issue(f'link {h} from {src}: missing #{frag}')
    report['internal_links_checked'] = len(seen)

    # Resize 1440 -> 390 -> 1440 without reload (P35)
    page.goto(BASE, wait_until='networkidle')
    for w in (390, 1440):
        page.set_viewport_size({'width': w, 'height': 900}); page.wait_for_timeout(300)
    vis = page.evaluate('() => [...document.querySelectorAll("#menu a, main")].every(e => e.getBoundingClientRect().width > 0)')
    if not vis: issue('resize: menu/main hidden after 1440->390->1440')
    report['resize_ok'] = vis

    # Keyboard: Tab order and focus visibility (P41, P43)
    page.goto(BASE + 'about/', wait_until='networkidle')
    tabs = []
    for i in range(14):
        page.keyboard.press('Tab')
        tabs.append(page.evaluate('''() => { const e = document.activeElement; const s = getComputedStyle(e);
           return {tag: e.tagName, text: (e.getAttribute('aria-label') || e.textContent || '').trim().slice(0, 25), href: e.getAttribute('href'),
                   outline: s.outlineStyle + ' ' + s.outlineWidth, shadow: s.boxShadow, visible: e.getBoundingClientRect().width > 0} }'''))
    report['tab_order'] = tabs
    for t in tabs:
        if t['outline'].startswith('none') and t['shadow'] == 'none':
            issue(f'focus not visible on {t}'); break
    page.screenshot(path=str(OUT / 'keyboard_focus.png'))
    # Enter on focused menu link navigates (P42)
    page.goto(BASE, wait_until='networkidle')
    page.focus('#menu a >> nth=0')
    with page.expect_navigation():
        page.keyboard.press('Enter')
    page.wait_for_load_state('networkidle')
    report['enter_nav'] = page.url
    page.wait_for_timeout(300)
    with page.expect_navigation():
        page.go_back(wait_until='commit')
    page.wait_for_load_state('networkidle')
    report['back_nav'] = page.url
    # 200% zoom equivalent: 720 CSS px wide at 1440 window
    z = br.new_context(viewport={'width': 720, 'height': 450}, device_scale_factor=2).new_page()
    for path in PAGES:
        z.goto(BASE + path, wait_until='networkidle')
        sw = z.evaluate('() => document.documentElement.scrollWidth')
        if sw > 721: issue(f'zoom200 {path} overflow {sw}')
    z.screenshot(path=str(OUT / 'zoom200_home.png'))
    # Skip link and 404
    q = br.new_context(viewport={'width': 390, 'height': 844}).new_page()
    q.goto(BASE + 'activities/law-school/', wait_until='networkidle')
    q.keyboard.press('Tab')
    report['first_tab'] = q.evaluate('() => [document.activeElement.textContent.trim(), document.activeElement.getBoundingClientRect().top]')
    q.screenshot(path=str(OUT / 'skip_link_390.png'))
    q.keyboard.press('Enter'); q.wait_for_timeout(400)
    report['after_skip'] = q.evaluate('() => [document.activeElement.id, location.hash]')
    r = q.goto(BASE + 'no-such-page/deep/', wait_until='networkidle')
    report['404'] = [r.status, q.evaluate('() => document.querySelector("h1") && document.querySelector("h1").textContent'), q.evaluate('() => [...document.styleSheets].length')]
    q.screenshot(path=str(OUT / '404_390.png'))
    br.close()

(OUT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=1))
print('browser:', report['browser'], '| links checked:', report['internal_links_checked'], '| issues:', len(report['issues']))
print('first_tab:', report['first_tab'], 'after_skip:', report['after_skip'], '404:', report['404'])
print('enter_nav:', report['enter_nav'], 'back:', report['back_nav'])
for t in report['tab_order']: print('TAB', t)
