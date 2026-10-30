---
title: "포트폴리오 사이트 제작 (초급프로젝트 과제 1)"
description: "Hugo PaperMod 테마와 GitHub Actions로 이 사이트를 만들고 GitHub Pages에 자동 배포한 수업 과제"
summary: "2026년 10월 · 완료 · 개인 과제 — Hugo + GitHub Actions로 이 사이트를 만들고 자동 배포"
weight: 2
hidemeta: true
ShowToc: true
TocOpen: true
---

## 활동 개요 {#overview}

| 항목 | 내용 |
| --- | --- |
| 기간 | 2026년 10월 |
| 상태 | 배포 완료 → 점검 후 개선 배포 완료 |
| 형태 | 개인 과제 (초급프로젝트 과제 1) |
| 목적 | 나를 소개하는 사이트를 만들고, `main` 브랜치에 push하면 자동으로 배포되게 구성하기 |

## 수행 과정 {#process}

1. Hugo Themes에서 **PaperMod** 테마를 골라 원본 파일을 내려받았습니다. 별도 설치 없이 빌드되고, 메뉴가 항상 보이며, 화면 크기에 맞게 배치가 바뀌는 테마라서 선택했습니다.
2. 수업에서 제공한 준비 스크립트로 GitHub Pages 배포 파일(`site/`, `.github/workflows/hugo-pages.yml`)을 만들었습니다.
3. 스크립트 기본값은 `pages.json`만 읽어 직접 쓴 설정이 무시되는 문제를 확인하고, `hugo.toml`도 읽도록 연결했습니다.
4. 소개·활동 내용을 마크다운으로 작성하고, 메뉴·목차·한국어(`lang="ko"`) 설정을 적용했습니다.
5. 1차 배포(2026-10-31 02:25 확인) 후 화면 폭·키보드·링크를 점검하고 아래를 개선해 다시 배포했습니다.

| 점검에서 발견한 점 | 개선 내용 |
| --- | --- |
| 한국어 단어가 "것입니/다"처럼 중간에서 줄바꿈됨 | 어절 단위 줄바꿈(`word-break: keep-all`) 적용 |
| 키보드 초점 표시가 1px로 얇아 잘 안 보임 | 3px 파란 초점 테두리 |
| Tab을 누르면 메뉴를 매번 모두 거쳐야 본문에 도착 | "본문 바로가기" 링크 추가 |
| GitHub 아이콘·테마 버튼 이름이 없거나 영어 | 한국어 이름(aria-label) 지정 |
| 모바일 메뉴 링크 폭 32px, 활동 요약이 "…"로 잘림 | 터치 폭 44px 확보, 요약 전체 표시 |
| 404 화면에 숫자만 표시 | 한국어 안내와 홈·소개·활동 링크 |

## 결과물 {#results}

- 사이트 소스: [github.com/won-ji1/portfolio](https://github.com/won-ji1/portfolio)
- 작업 단계별 커밋 이력: [커밋 목록](https://github.com/won-ji1/portfolio/commits/main/)
- 자동 배포 기록: [GitHub Actions](https://github.com/won-ji1/portfolio/actions)

## 배운 점 {#lessons}

- 설정 파일을 여러 개 쓰면 **뒤에 오는 파일이 앞 파일의 값을 덮어쓴다**는 것을 빌드 결과로 확인했습니다.
- 오픈소스 테마를 쓸 때는 **라이선스 고지를 유지**해야 하므로, 저장소의 `LICENSE`와 사이트 하단의 테마 표기를 그대로 두었습니다.
