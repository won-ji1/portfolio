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
hugo server --config hugo.toml,pages.json
```

브라우저에서 <http://localhost:1313/portfolio/> 를 엽니다. 종료는 `Ctrl + C`.

**배포와 같은 방식으로 빌드** (저장소 최상위 폴더에서):

```bash
python .github/pages_build.py --build
```

결과는 `public/` 폴더에 생성되며 `public/index.html`이 홈 페이지입니다. (`public/`은 Git에 올리지 않습니다.)
