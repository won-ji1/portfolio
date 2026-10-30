# 검증 근거 자료

| 파일 | 내용 | URL | 캡처 시각 (KST) | 화면 폭 | 캡처 |
| --- | --- | --- | --- | --- | --- |
| `fig01_live_home_first_deploy.png` | 1차 배포 직후 공개 홈 화면 (어두운 테마). 첫 문단 끝 "것입니/다"처럼 한국어 단어가 중간에서 줄바꿈되는 문제 확인 | https://won-ji1.github.io/portfolio/ | 2026-10-31 02:25 | 브라우저 창 약 1896px | 본인 (Chrome) |

## 자동 점검 결과 (`docs/evidence/auto/`)

`docs/tools/check_site.py`로 커밋 `c38640f`의 배포용 빌드(`python .github/pages_build.py --build`)를 점검한 결과입니다.
공개 주소 `https://won-ji1.github.io/portfolio/` 요청을 같은 커밋의 `public/` 파일로 응답하게 해 배포 경로(/portfolio/)를 그대로 재현했습니다.
환경: Chromium 153.0.8010.12 (Playwright, Linux) · 점검 시각 2026-10-31 02:37 KST

| 파일 | 내용 | 화면 폭 |
| --- | --- | --- |
| `report.json` | 5개 페이지 × 3개 폭 점검 결과, 내부 링크 34개, Tab 순서, 결함 목록(issues: 0건) | 1440·768·390px |
| `skip_link_390.png` | 대표 활동 페이지에서 첫 Tab 시 "본문 바로가기"와 3px 초점 테두리 표시 | 390px |
| `keyboard_focus.png` | 소개 페이지에서 Tab 14회 후 초점 위치 표시 | 1440px |
| `404_390.png` | 없는 주소(/portfolio/no-such-page/deep/) 접속 시 한국어 404 안내와 홈·소개·활동 링크 | 390px |
| `zoom200_home.png` | 200% 확대와 같은 조건(1440px 창 = CSS 720px)에서 홈 화면, 가로 넘침 없음 | 720px |
