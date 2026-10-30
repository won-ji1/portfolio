# 검증 근거 자료

| 파일 | 내용 | URL | 캡처 시각 (KST) | 화면 폭 | 캡처 |
| --- | --- | --- | --- | --- | --- |
| `fig01_live_home_first_deploy.png` | 1차 배포 직후 공개 홈 화면 (어두운 테마). 첫 문단 끝 "것입니/다"처럼 한국어 단어가 중간에서 줄바꿈되는 문제 확인 | https://won-ji1.github.io/portfolio/ | 2026-10-31 02:25 | 브라우저 창 약 1896px | 본인 (Chrome) |
| `fig02_live_1440.png` | 2차 배포(커밋 70320f1, [Actions 실행](https://github.com/won-ji1/portfolio/actions/runs/41099966347)) 후 공개 홈 화면. 어절 단위 줄바꿈, 하단 "사이트 소스 코드" 링크 반영 확인 | https://won-ji1.github.io/portfolio/ | 2026-10-31 03:10 | 1440px (Chrome 기기 모드, 2배율 저장 2880px) | 본인 (Chrome) |
| `fig03_live_390.png` | 같은 화면 모바일 폭. 단어 중간 줄바꿈 없음("있습니다.", "것입니다."), 메뉴 3개 표시, 가로 넘침 없음 | https://won-ji1.github.io/portfolio/ | 2026-10-31 03:11 | 390px (Chrome 기기 모드, 2배율 저장 780px) | 본인 (Chrome) |

## 자동 점검 결과 (`docs/evidence/auto/`)

`docs/tools/check_site.py`로 커밋 `a6447c6`(사이트 내용 최종본)의 배포용 빌드(`python .github/pages_build.py --build`)를 점검한 결과입니다.
공개 주소 `https://won-ji1.github.io/portfolio/` 요청을 같은 커밋의 `public/` 파일로 응답하게 해 배포 경로(/portfolio/)를 그대로 재현했습니다.
환경: Chromium 153.0.8010.12 (Playwright, Linux) · 점검 시각 2026-10-31 03:49 KST (처음 점검 02:37, 커밋 c38640f 기준 → 최종 사이트 변경 후 재점검)

| 파일 | 내용 | 화면 폭 |
| --- | --- | --- |
| `report.json` | 5개 페이지 × 3개 폭 점검 결과, 내부 링크 34개, Tab 순서, 결함 목록(issues: 0건) | 1440·768·390px |
| `skip_link_390.png` | 대표 활동 페이지에서 첫 Tab 시 "본문 바로가기"와 3px 초점 테두리 표시 | 390px |
| `keyboard_focus.png` | 소개 페이지에서 Tab 14회 후 초점 위치 표시 | 1440px |
| `404_390.png` | 없는 주소(/portfolio/no-such-page/deep/) 접속 시 한국어 404 안내와 홈·소개·활동 링크 | 390px |
| `zoom200_home.png` | 200% 확대와 같은 조건(1440px 창 = CSS 720px)에서 홈 화면, 가로 넘침 없음 | 720px |

## 개선 전 자동 점검 결과 (`docs/evidence/auto_before/`)

1차 배포 커밋 `d53123c`의 배포용 빌드를 같은 점검 스크립트(이후 `docs/tools/check_site.py`로 저장소에 추가)로 2026-10-31 01:52 KST에 점검한 결과입니다. 환경: Chromium 153.0.8010.12 (Playwright, Linux).

| 파일 | 내용 | 화면 폭 |
| --- | --- | --- |
| `390_home_before.png` | 개선 전 홈 화면. 제목 "한지원입니/다", 소개 "있습니/다"처럼 단어 중간 줄바꿈, 활동 요약이 "1차 결과 대…"로 잘림 | 390px |
| `report_before.json` | 개선 전 점검 기록. 결함 0건이지만 Tab 초점이 `outline auto 1px`(브라우저 기본값), 메뉴 링크 폭 32px로 측정됨 → 2차 개선의 근거 | 1440·768·390px |

참고: `docs/evidence/auto/`의 결과는 사이트 내용의 마지막 변경 커밋 `a6447c6` 빌드로 다시 점검한 것입니다. 그 뒤 커밋은 `docs/` 폴더만 바꿉니다.
