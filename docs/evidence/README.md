# 검증 근거 자료

| 파일 | 내용 | URL | 캡처 시각 (KST) | 화면 폭 | 캡처 |
| --- | --- | --- | --- | --- | --- |
| `fig01_live_home_first_deploy.png` | 1차 배포 직후 공개 홈 화면 (어두운 테마). 첫 문단 끝 "것입니/다"처럼 한국어 단어가 중간에서 줄바꿈되는 문제 확인. 오른쪽 위 Chrome 프로필 표시는 '프로필 가림'으로 덮음(그 밖의 부분은 원본 그대로). 현재 파일만 가린 것이며, 가리기 전 원본은 Git 이력(커밋 e2e59ad)에 남아 있음 | https://won-ji1.github.io/portfolio/ | 2026-10-31 02:25 | 브라우저 창 약 1896px | 본인 (Chrome) |
| `fig02_live_1440.png` | 2차 배포(커밋 70320f1, [Actions 실행](https://github.com/won-ji1/portfolio/actions/runs/41099966347)) 후 공개 홈 화면. 어절 단위 줄바꿈, 하단 "사이트 소스 코드" 링크 반영 확인 | https://won-ji1.github.io/portfolio/ | 2026-10-31 03:10 | 1440px (Chrome 기기 모드, 2배율 저장 2880px) | 본인 (Chrome) |
| `fig03_live_390.png` | 같은 화면 모바일 폭. 단어 중간 줄바꿈 없음("있습니다.", "것입니다."), 메뉴 3개 표시, 가로 넘침 없음 | https://won-ji1.github.io/portfolio/ | 2026-10-31 03:11 | 390px (Chrome 기기 모드, 2배율 저장 780px) | 본인 (Chrome) |

## 자동 점검 결과 (`docs/evidence/auto/`)

`docs/tools/check_site.py`로 커밋 `6c08c2b`(사이트 최종본)의 배포용 빌드(`python .github/pages_build.py --build`)를 점검한 결과입니다.
공개 주소 `https://won-ji1.github.io/portfolio/` 요청을 같은 커밋의 `public/` 파일로 응답하게 해 배포 경로(/portfolio/)를 그대로 재현했습니다.
환경: Chromium 153.0.8010.12 (Playwright, Linux) · 점검 시각 2026-10-31 18:24 KST (처음 02:37 c38640f → 재점검 03:49·04:02·04:14·04:42 → 초점 테두리 수정과 점검 항목 추가 후 최종 점검)

| 파일 | 내용 | 화면 폭 |
| --- | --- | --- |
| `report.json` | 6개 페이지(404 포함) × 4개 폭 점검 결과, 내부 링크·앵커 38개, 잘린 내용 0건, 초점 테두리 잘림 0건, localhost·file·http 참조 0건, 파비콘 5개 확인(로컬 재현에서는 파일 존재로 확인), Tab 순서, '맨 위로' 버튼 겹침 스캔(toplink_overlaps: 0건), 테마 버튼 Enter 전환, 앵커 새로고침, 결함 목록(issues: 0건) | 1440·768·390·360px (겹침 스캔은 1440·900·768·390·360px × 창 높이 900·420px) |
| `skip_link_390.png` | 대표 활동 페이지에서 첫 Tab 시 "본문 바로가기"와 3px 초점 테두리 표시 | 390px |
| `keyboard_focus.png` | 소개 페이지에서 Tab 14회 후 초점 위치 표시(머리글 초점 테두리는 9ad8a20부터 요소 안쪽에 표시) | 1440px |
| `404_390.png` | 없는 주소(/portfolio/no-such-page/deep/) 접속 시 한국어 404 안내와 홈·소개·활동 링크 3개가 잘리지 않고 표시(26e71c6 수정 후) | 390px |
| `zoom200_home.png` | 200% 확대와 같은 조건(1440px 창 = CSS 720px)에서 홈 화면, 가로 넘침 없음(넘침 측정은 6개 페이지 모두) | 720px |

## 개선 전 자동 점검 결과 (`docs/evidence/auto_before/`)

1차 배포 커밋 `d53123c`의 배포용 빌드를 점검 스크립트의 초기 버전(이후 기능을 더해 `docs/tools/check_site.py`로 저장소에 추가, 초기 버전에는 본문 바로가기·404·겹침 항목이 없음)로 2026-10-31 01:52 KST에 점검한 결과입니다. 환경: Chromium 153.0.8010.12 (Playwright, Linux).

| 파일 | 내용 | 화면 폭 |
| --- | --- | --- |
| `390_home_before.png` | 개선 전 홈 화면. 제목 "한지원입니/다", 소개 "있습니/다"처럼 단어 중간 줄바꿈, 활동 요약이 "1차 결과 대…"로 잘림 | 390px |
| `report_before.json` | 개선 전 점검 기록. 결함 0건이지만 Tab 초점이 `outline auto 1px`(브라우저 기본값), 메뉴 링크 폭 32px로 측정됨 → 2차 개선의 근거 | 1440·768·390px |

참고: `docs/evidence/auto/`의 결과는 사이트의 마지막 변경 커밋 `6c08c2b` 빌드로 점검한 것입니다. 그 뒤 커밋은 `docs/`·`README.md`만 바꿉니다. 이 점검은 작업 환경에서 공개 서버에 직접 접속할 수 없어 공개 주소 요청을 같은 빌드 파일로 응답하게 한 재현 점검이며, 없는 주소에 404.html을 돌려주는 것은 GitHub Pages의 동작이라 이 점검으로는 404.html의 내용만 확인합니다.
