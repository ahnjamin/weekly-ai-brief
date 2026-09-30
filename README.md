# weekly-ai-briefing

지난 1주일간 주목받은 **AI 이슈 · 주요 랩 동향 · GitHub 레포 · Hugging Face 소식 · 논문**을 조사해 공부용 다이제스트로 정리하는 Claude 스킬과, 그 결과물 아카이브.

> 매주 받아서 다른 창에 붙여넣고 공부하는 용도로 만들었습니다. 그래서 출력은 파일이 아니라 **복사하기 좋은 마크다운 채팅 답변**입니다.

## 구성

```
.
├── skills/
│   └── weekly-ai-briefing/
│       └── SKILL.md          # 스킬 본체
└── briefings/
    ├── 2026-W38_0914-0921.md # 아카이브
    └── 2026-W39_0921-0927.md
```

## 설치

### Claude Code / Cowork

```bash
git clone https://github.com/ahnjamin/weekly-ai-brief.git
mkdir -p ~/.claude/skills
cp -r weekly-ai-brief/skills/weekly-ai-briefing ~/.claude/skills/
```

프로젝트 단위로 쓰려면 `~/.claude/skills` 대신 `<프로젝트>/.claude/skills`에 넣으면 됩니다.

### 사용

```
주간 AI 브리핑 해줘
지난 주(10/5~10/12) AI 소식 정리해줘
```

## 스킬이 하는 일

1. 기간 확정 (기본: 오늘부터 지난 7일)
2. 직전 회차 항목을 **중복 제외 목록**으로 정리
3. `general-purpose` 서브에이전트 4개를 **병렬**로 실행
   - **A** 주요 이슈 · 랩 동향 · 모델 릴리스
   - **B** AI Eval
   - **C** Agent (데이터 분석 에이전트 + 평가 에이전트 각 최소 1건)
   - **D** GitHub · Hugging Face · 논문
4. 핵심 arXiv 논문과 주요 주장을 **1차 출처로 교차 검증**
5. 12개 섹션 브리핑 작성 (마지막에 "다른 창에서 공부할 때 추천 순서" + 커버리지 한계)

## 각 항목 포맷

```
### N. 제목
**날짜** · (소속/저자) · URL

3~5줄 요약 — 구체적 수치, 모델명, 방법론의 핵심 메커니즘

> 💡 왜 중요한가 / 학습 포인트 한 줄
```

💡 줄이 핵심입니다. 요약을 되풀이하지 않고 **왜 읽을 가치가 있는지** — 반직관적인 결과, 통념을 깨는 수치, 다른 항목과의 연결 — 를 씁니다.

## 조사 환경 메모

두 회차 돌리면서 실제로 부딪힌 것들. 스킬 안에 전문이 들어 있고, 여기 요약만:

| 경로 | 상태 |
|---|---|
| `export.arxiv.org` API | ❌ 403 차단 |
| `arxiv.org/search/` | ❌ robots.txt 차단 |
| `arxiv.org/abs/<id>` | ✅ **v1 제출일 검증용 정본** |
| `arxiv.org/list/<cat>/pastweek` | ⚠️ 접근되나 ID·날짜 부정확 → abs로 재검증 필수 |
| `huggingface.co/papers?date=` | ✅ 평일만 (주말·당일은 400) |
| `huggingface.co/papers/week/YYYY-Wnn` | ✅ upvote로 화제성 판단 |
| `huggingface.co/changelog` | ✅ 플랫폼 업데이트, 공식 블로그보다 신뢰도 높음 |
| `github.com/trending` | ❌ 수년 전 캐시 반환 |
| GitHub `releases` 목록 페이지 | ⚠️ 캐시가 몇 달 전 |
| GitHub `releases/tag/<ver>` | ✅ 최신 정상 |
| `pypi.org/project/<pkg>/#history` | ✅ 날짜 확정용 |

**2단계 릴리스 확인 루틴**: pypi `#history`로 날짜 확정 → `releases/tag/<ver>`로 내용 확인

**가장 흔한 함정**: **HF Daily Papers 게재일 ≠ arXiv v1 제출일.** arXiv ID가 그 주 번호대여도 v1은 몇 주 전인 경우가 흔합니다. W39 회차에서만 6건이 어긋났습니다.

**부가 버그**: WebFetch가 GitHub 날짜의 연도를 틀리게 렌더링하는 경우가 있습니다 (2026 → 2024).

## 아카이브

| 주차 | 기간 | 하이라이트 |
|---|---|---|
| [W38](briefings/2026-W38_0914-0921.md) | 09.14~09.21 | 메모리 월의 나머지 절반 · ImpossibleRubrics · Emergence World |
| [W39](briefings/2026-W39_0921-0927.md) | 09.21~09.27 | 가격 붕괴 주 · judge 캐스케이드 논쟁 · trace tampering |
