# 한지원 포트폴리오 사이트

- 공개 사이트: <https://won-ji1.github.io/portfolio/>
- 저장소: <https://github.com/won-ji1/portfolio>
- 배포 기록(GitHub Actions): <https://github.com/won-ji1/portfolio/actions>

Hugo 정적 사이트 생성기와 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 테마로 만든 개인 소개 사이트입니다.
`main` 브랜치에 push하면 GitHub Actions가 자동으로 빌드해 GitHub Pages에 배포합니다.

## 1. 사용 도구와 버전

| 도구 | 버전 | 용도 |
| --- | --- | --- |
| Hugo (extended) | **0.167.0** | 사이트 빌드 (워크플로 `.github/workflows/hugo-pages.yml`의 `HUGO_VERSION`) |
| Python | 3.9 이상 (작성 환경 3.13) | 배포 빌드 스크립트 `.github/pages_build.py` 실행 |
| Git | 2.x | 버전 관리 |
| 테마 | PaperMod, 원본 커밋 `118119693d8b5ac211b939775678310973bcb232` | `site/themes/template/` |
| 준비 스크립트 | `prepare_github_pages.py` 3.1 (수업 제공) | 배포 파일 생성 |

GitHub Actions에서는 워크플로가 Hugo 0.167.0, Dart Sass, Node, Go를 직접 설치하므로 별도 설정이 필요 없습니다.

## 2. 설치

1. Git 설치: <https://git-scm.com/downloads>
2. Python 3.9 이상 설치: <https://www.python.org/downloads/>
3. Hugo **extended 0.167.0** 설치: <https://github.com/gohugoio/hugo/releases/tag/v0.167.0>
   에서 운영체제에 맞는 `hugo_extended_0.167.0_...` 파일을 받아 압축을 풀고, `hugo` 실행 파일이 있는 폴더를 PATH에 추가합니다.
   설치 확인: `hugo version` → `hugo v0.167.0-...+extended`
4. 저장소 받기:

   ```bash
   git clone https://github.com/won-ji1/portfolio.git
   cd portfolio
   ```

## 3. 실행·빌드 명령

**로컬 미리보기** (수정 내용을 바로 확인):

```bash
cd site
hugo server --config "hugo.toml,pages.json"
```

`hugo.toml,pages.json`은 반드시 **따옴표로 감싸 한 덩어리**로 입력합니다. Git Bash·macOS 터미널·명령 프롬프트(cmd)·PowerShell에서 모두 같은 명령으로 동작합니다. (PowerShell에서는 따옴표 없이 쓰면 쉼표에서 인수가 나뉘어 `unknown command "pages.json"` 오류가 납니다.)

브라우저에서 <http://localhost:1313/portfolio/> 를 엽니다. 종료는 `Ctrl + C`.

**배포와 같은 방식으로 빌드** (저장소 최상위 폴더에서):

```bash
python .github/pages_build.py --build
```

macOS·Linux에서 `python` 명령이 없으면 `python3`으로 바꿔 입력합니다.

결과는 `public/` 폴더에 생성되며 `public/index.html`이 홈 페이지입니다. (`public/`은 Git에 올리지 않습니다.)

## 4. 수정할 파일 위치

| 바꾸고 싶은 것 | 파일 |
| --- | --- |
| 사이트 제목, 언어, 메뉴, 홈 첫 화면 소개, GitHub 링크 | `site/hugo.toml` |
| 소개 페이지 (관심 분야·학습 목표·역량) | `site/content/about.md` |
| 활동 목록 문구 | `site/content/activities/_index.md` |
| 대표 활동 (로스쿨 진학 준비) | `site/content/activities/law-school/index.md` |
| 대표 활동 흐름도 이미지 | `site/content/activities/law-school/timeline.svg` |
| 보조 활동 (포트폴리오 사이트 제작) | `site/content/activities/portfolio-site.md` |
| 파비콘 | `site/static/` |
| 한국어 줄바꿈·요약 표시 CSS | `site/assets/css/extended/korean.css` |
| 키보드 초점·터치 영역·본문 바로가기 CSS | `site/assets/css/extended/a11y.css` |
| 본문 바로가기 링크, 테마 버튼 이름 | `site/layouts/_partials/header.html` (테마 원본 복사 후 수정) |
| 하단 소스 링크, '맨 위로' 버튼 이름 | `site/layouts/_partials/footer.html` (〃) |
| GitHub 아이콘 링크 이름 | `site/layouts/_partials/social_icons.html` (〃) |
| 활동 카드 링크 이름 / 이동 경로 이름 | `site/layouts/list.html`, `site/layouts/_partials/breadcrumbs.html` (〃) |
| 본문 영역 id (`main-content`) | `site/layouts/baseof.html` (〃) |
| 404 페이지 | `site/layouts/404.html` |
| 검증 캡처·기록 | `docs/evidence/` |
| 배포용 설정 (baseURL, 테마 지정) — 직접 수정하지 않음 | `site/pages.json`, `.github-pages.json` |
| 배포 워크플로 | `.github/workflows/hugo-pages.yml` |

배포 빌드는 `.github-pages.json`의 `"config": "hugo.toml,pages.json"` 순서로 설정을 읽습니다. 뒤에 오는 `pages.json`이 baseURL·테마 같은 배포 값을 덮어씁니다.

`site/layouts/`의 파일은 같은 경로의 테마 원본(`site/themes/template/layouts/`)보다 우선 적용됩니다. 테마 원본 파일은 수정하지 않았습니다.

저장소 최상위의 `assets/`, `layouts/`, `i18n/`, `images/`, `theme.toml`, `go.mod`는 내려받은 테마 원본입니다. 실제 빌드에는 `site/themes/template/`에 복사된 테마가 쓰입니다.

## 5. 수정 후 재배포와 확인 방법

1. 위 파일을 수정하고 로컬 미리보기로 확인합니다.
2. 커밋하고 `main`에 push합니다.

   ```bash
   git add .
   git commit -m "수정 내용을 설명하는 메시지"
   git push origin main
   ```

3. **Actions 확인:** <https://github.com/won-ji1/portfolio/actions> 에서 방금 커밋 메시지로 시작된 `Deploy Hugo to GitHub Pages` 실행을 엽니다. `build`와 `deploy` 두 작업이 모두 초록색 체크(✓)면 성공입니다.
4. **공개 화면 확인:** <https://won-ji1.github.io/portfolio/> 를 새로고침해 변경 내용이 보이는지 확인합니다. 캐시 때문에 이전 화면이 보이면 `Ctrl + Shift + R`(Mac: `Cmd + Shift + R`)로 강력 새로고침합니다.

처음 한 번은 GitHub 저장소의 **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 설정해야 합니다. 설정 전 첫 실행이 실패했다면 설정 후 Actions 화면에서 **Re-run jobs**를 누릅니다.

## 6. 동작 점검 방법

브라우저 자동 점검 스크립트로 화면 폭(1440·768·390px), 링크·앵커, 이미지·CSS 로딩, 키보드(Tab·Enter), 200% 확대, 404 페이지를 한 번에 확인할 수 있습니다.

```bash
pip install playwright
python -m playwright install chromium
python docs/tools/check_site.py https://won-ji1.github.io/portfolio/ check-output
```

결과는 `check-output/` 폴더(Git에서 제외)에 저장되며, `check-output/report.json`의 `issues`가 빈 목록이면 결함이 없는 것입니다. 제출용으로 남긴 점검 결과는 `docs/evidence/auto/`에 있습니다. 점검 기록과 화면 캡처는 [`docs/evidence/`](docs/evidence/README.md)에 있습니다.

## 7. 출처와 이용 조건

| 자료 | 사용 위치 | 구분 | 출처·이용 조건 |
| --- | --- | --- | --- |
| PaperMod 테마 | `site/themes/template/` (원본: 저장소 최상위) | 외부 자료 | <https://github.com/adityatelange/hugo-PaperMod> · MIT License, 고지 파일 `LICENSE`·`site/themes/template/LICENSE` 유지, 사이트 하단 "Powered by Hugo & PaperMod" 표기 유지 |
| PaperMod 원본 README | `site/themes/template/README.md` | 외부 자료 | 위와 같음 |
| Hugo | 빌드 도구 | 외부 도구 | <https://gohugo.io/> · Apache License 2.0 |
| 배포 준비 스크립트 | `prepare_github_pages.py`, `.github/pages_build.py`, `.github/workflows/hugo-pages.yml`, `site/pages.json`, `.github-pages.json` | 수업 제공 자료 | 2026학년도 초급프로젝트 과제 1 제공 스크립트 3.1이 생성 |
| 소개·활동 글의 내용 | `site/content/` | 직접 작성 | 본인 경험·계획. 문장 다듬기와 페이지 구성에 AI(Claude) 도움을 받음 |
| 대표 활동 흐름도 `timeline.svg` | `site/content/activities/law-school/` | AI 생성 | 본인이 제공한 활동 내용을 바탕으로 AI(Claude)가 SVG 코드로 작성 |
| 파비콘 (`favicon.ico` 등 5개) | `site/static/` | AI 생성 | AI(Claude)가 Python Pillow로 생성. 글꼴: Noto Sans CJK (SIL Open Font License) |
| 자동 점검 스크립트 `check_site.py` | `docs/tools/` | AI 생성 + 본인 확인 | AI(Claude)가 Playwright로 작성, 실행 결과를 `docs/evidence/auto/`에 저장 |
| 검증 화면 캡처 `fig01`~ | `docs/evidence/` | 직접 제작 | 본인이 Chrome에서 공개 사이트를 캡처 |
| 사이트 설정·화면 수정 | `site/hugo.toml`, `site/layouts/`, `site/assets/css/extended/` | AI 도움 + 본인 확인 | AI(Claude)가 작성하고 본인이 사이트에서 동작을 확인 |

AI 도움을 받은 커밋에는 커밋 메시지 끝에 `Co-Authored-By: Claude` 표시를 남겼습니다.
