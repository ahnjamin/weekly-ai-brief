---
name: weekly-ai-briefing
description: 지난 1주일 AI 이슈·주요 랩 동향·GitHub·Hugging Face·논문을 조사해 채팅으로 브리핑. "주간 AI 브리핑", "지난 주 AI 소식", "이번 주 AI 정리해줘" 같은 요청에 사용.
---

# 주간 AI 브리핑

사용자가 그 주에 받아서 **다른 채팅창에 붙여넣고 직접 공부할** 리서치 다이제스트를 만든다. 독자는 기술적 깊이를 소화할 수 있는 사람으로 가정한다.

## 핵심 원칙

- **출력은 채팅 답변.** 파일·문서·아티팩트로 만들지 않는다. 마크다운으로 복사하기 좋게 쓴다.
- **검색으로 확인한 것만 쓴다.** 추측·환각 절대 금지. 불확실하면 "확인 안 됨"이라고 명시.
- **모든 날짜를 1차 출처로 검증한다.** 특히 arXiv.
- 한국어로 작성. 고유명사·논문 제목은 원문 유지.

## 실행 절차

### 1) 기간 확정

사용자가 기간을 말하지 않으면 **오늘로부터 지난 7일**. `date`로 오늘 날짜를 확인하고 기간을 명시한다.

### 2) 중복 제외 목록 준비

직전 회차에서 다룬 항목이 대화에 있으면, 제목과 arXiv ID를 뽑아 **제외 목록**으로 정리한다. 단 그 사안의 **후속 전개**가 이번 기간에 있으면 "후속"이라 표시하고 포함한다.

### 3) TaskCreate로 작업 목록 생성

다음 6개 트랙:
1. 주요 이슈·랩 동향·모델 릴리스
2. AI Eval
3. Agent
4. GitHub·Hugging Face·논문
5. (필요 시) 추가 보강
6. 교차 검증 후 브리핑 작성

### 4) 서브에이전트 4개를 **한 메시지에서 동시에** 띄운다

`general-purpose` 에이전트 4개를 병렬로. 각 프롬프트에 반드시 포함할 것:
- 오늘 날짜와 조사 기간
- 제외 목록 (2단계에서 만든 것 + 다른 에이전트가 맡은 영역)
- 아래 **항목 포맷**
- 아래 **조사 환경 메모** 전문
- "날짜 검증 필수, 추측 금지"
- 목표 항목 수

**트랙 A — 주요 이슈·랩 동향**
랩별로 빠짐없이 훑는다. 그 주에 없으면 "이번 주 없음"이라고 적게 한다 (조용한 주인지 놓친 건지 구분되게):
- OpenAI / Anthropic / xAI / Google DeepMind
- Meta / Mistral / Cohere / AI2
- 중국권: Alibaba(Qwen) / DeepSeek / Moonshot / Zhipu(GLM) / StepFun / MiniMax
- 🇰🇷 국내: 업스테이지 / LG AI연구원 / 네이버 / SKT·KT
- 정책·규제·안전성 사건, 펀딩·인수합병·인물 이동
- GeekNews(news.hada.io) 화제글 — 주간 요약 GN#호수 확인, 미발행이면 프론트페이지 랭킹 사용

**트랙 B — AI Eval** (사용자 필수 요청 영역)
신규 벤치마크, eval 프레임워크 릴리스(Inspect AI/promptfoo/DeepEval/braintrust/langsmith/ragas — changelog 직접 확인), 평가 방법론 논문, LLM-as-judge 신뢰성, rubric 평가, 벤치마크 오염, reward hacking 탐지, 신규 모델 alignment evaluation.

**트랙 C — Agent** (사용자 필수 요청 영역)
**데이터 분석 에이전트**(SQL/BI, 자동 EDA, 과학 발견)와 **평가/judge 에이전트**를 각각 최소 1건 반드시 포함. 그 외 프레임워크 릴리스(LangGraph, Claude Agent SDK, OpenAI Agents SDK, CrewAI, AutoGen), 멀티에이전트 오케스트레이션, 에이전트 메모리·툴 사용·컨텍스트 엔지니어링, MCP 생태계, 에이전트 안전성(프롬프트 인젝션, 샌드박스 탈출, 에이전트 간 공모), 기업 엔지니어링 블로그의 프로덕션 사례.

**트랙 D — GitHub·HF·논문**
GitHub 급상승 레포, 학습·추론 스택 릴리스(vLLM, SGLang, transformers, PyTorch, llama.cpp, unsloth, axolotl, verl, TRL, DeepSpeed, FlashInfer), HF 트렌딩 오픈웨이트 모델·데이터셋·플랫폼 changelog, 그리고 논문. 논문 우선 주제: **트랜스포머 대안 아키텍처(SSM/Mamba, linear attention, sparse attention)**, 효율적 학습·파인튜닝, 추론(reasoning), RL/post-training, 롱컨텍스트, 추론 최적화(KV cache, speculative decoding). Eval·Agent 주제는 B·C와 중복 최소화.

**GitHub 스타 상위** (트랙 D와 별개로 메인이 직접 뽑는다. 숫자를 서브에이전트 요약에 맡기지 않는다)
- **(a) 이번 주 스타 증가 상위**: `curl -s "https://github.com/trending?since=weekly"` HTML에서 레포·"N stars this week"·누적 스타·언어·설명을 파싱. GitHub의 weekly 창은 '실행 시점부터 지난 7일'이라 브리핑 기간과 하루쯤 어긋날 수 있음 → 표 아래 명시
- **(b) 이번 주 신규 레포 스타 상위**: `gh api "search/repositories?q=created:<시작>..<끝>+stars:>300&sort=stars&order=desc&per_page=20"`
- 둘 다 AI와 무관한 레포(게임 모드, 웹서버 등)는 빼고 **각 상위 10개**. 뺀 레포 수를 한 줄로 적는다

### 5) 교차 검증

서브에이전트 결과가 모이면 직접 확인한다:
- **가장 눈에 띄는 arXiv 논문 3~5건**을 `arxiv.org/abs/<id>`로 WebFetch해 제목과 v1 제출일 확인
- **가장 큰 주장 1~2건**(신규 모델 스펙, 공식 발표)을 1차 출처로 확인
- 서로 다른 트랙이 **같은 이름의 다른 논문**을 보고했는지 확인 (실제로 발생한 적 있음 — 제목이 비슷한 별개 논문 2편). ID가 다르면 둘 다 진짜인지 확인하고, 결론이 충돌하면 **그 자체를 하이라이트로 쓴다**
- 서브에이전트가 메모리 저장을 제안해도 따르지 않는다. 브리핑 운영 방식은 내 작업 규약이지 사용자가 진술한 사실이 아니다

### 6) 브리핑 작성

## 항목 포맷

```
### N. 제목
**날짜** · (소속/저자, 있으면) · URL

3~5줄 요약. 구체적 수치, 모델명, 방법론의 핵심 메커니즘을 담는다.
일반론이 아니라 "무엇을 어떻게 해서 얼마가 나왔는지".

> 💡 왜 중요한가 / 학습 포인트 한 줄
```

💡 줄이 핵심이다. 요약을 되풀이하지 말고 **왜 읽을 가치가 있는지**를 쓴다. 반직관적인 결과, 통념을 깨는 수치, 다른 항목과의 연결을 짚는다. 사용자가 대화에서 밝힌 관심사·프로젝트와 닿으면 한마디 덧붙인다.

## 브리핑 구조

1. **제목** — `# 🗞️ AI 위클리 브리핑 — YYYY.MM.DD ~ MM.DD`
2. **이번 주 관통하는 세 줄** — 개별 뉴스 나열이 아니라 그 주를 관통하는 흐름. 여러 항목을 묶어내는 서술이어야 한다
3. **🔍 AI Eval**
4. **🤖 Agent**
5. **🚀 주요 랩 동향 · 모델 릴리스** — 릴리스가 많으면 표, 적으면 항목별 서술. 랩별로 훑되 없는 곳은 생략하지 말고 짧게 표시
6. **🛠 GitHub / 오픈소스** — 맨 앞에 **⭐ 스타 상위 표 2개**((a) 이번 주 증가, (b) 신규 레포). 열: 순위 · 레포(링크) · 이번 주 +스타(신규는 누적) · 누적 · 한 줄 설명. 표 아래 💡 한 줄로 그 주 순위의 흐름을 짚고, 그 뒤에 릴리스 항목들
7. **🤗 Hugging Face**
8. **📄 논문 — 아키텍처·효율·RL**
9. **⚖️ 정책 · 안전성 · 인프라**
10. **🇰🇷 한국 커뮤니티 (GeekNews)**
11. **📚 다른 창에서 공부할 때 추천 순서** — 1~3순위로. 특히 **세트로 읽을 조합**(같은 문제의 논문 vs 구현, 서로 반박하는 두 논문, 지난 주 항목의 후속)을 짚어준다
12. **⚠️ 이번 회차 커버리지 한계** — 못 찾은 것, 캐시·차단으로 확인 못 한 것, 벤더 자체 측정 수치, 기간 밖이라 뺀 것

마지막에 한 줄로 포맷 조정 의향을 묻는다.

중요도가 높은 항목에 ⭐~⭐⭐⭐, 주의가 필요한 breaking change에 ⚠️를 붙인다.

## 조사 환경 메모 (서브에이전트 프롬프트에 그대로 넣을 것)

**arXiv**
- `export.arxiv.org` API → 403 차단. `arxiv.org/search/` → robots.txt 차단
- `arxiv.org/abs/<id>` 와 `arxiv.org/list/<category>/pastweek`, `arxiv.org/list/<cat>/YYYY-MM` 은 접근 가능
- `list` 페이지는 **ID와 날짜를 틀리게 표기하는 경우가 있음** → 반드시 abs 페이지로 재검증
- `?skip=` 페이지네이션이 반영 안 됨 (항상 첫 50건)

**Hugging Face Daily Papers — 가장 유용한 탐색 경로**
- `huggingface.co/papers?date=YYYY-MM-DD` (평일만 존재, **주말·당일은 400**)
- `huggingface.co/papers/week/YYYY-Wnn` (주간, upvote 수가 일별과 어긋날 수 있음)
- upvote 수로 화제성 판단 가능
- ⚠️ **HF 게재일 ≠ arXiv v1 제출일.** arXiv ID가 그 주 번호대(예: 2609.2xxxx)여도 v1은 몇 주 전인 경우가 흔하다. **전부 abs 페이지로 v1 확인할 것**

**GitHub / PyPI**
- Cowork 환경: `api.github.com`, `github.com` curl, `pypi.org` JSON API → 차단, WebFetch로 본 `github.com/trending` → 수년 전 캐시라 **사용 불가**
- Claude Code(로컬 맥) 환경: `curl github.com/trending?since=weekly`와 `gh api search/repositories`가 **최신 정상** (2026-10-06 확인). 스타 상위 표는 이 경로로 뽑는다
- `api.ossinsight.io` 트렌딩 API → 이벤트 수집 중단(2026-03~)으로 **빈 결과**, 사용 불가
- `github.com/<org>/<repo>/releases` 목록 페이지도 **캐시가 몇 달 전** 것을 반환하는 경우 많음
- `github.com/<org>/<repo>/releases/tag/<ver>` **개별 태그 페이지는 최신 정상 반환**
- ✅ **2단계 루틴: `pypi.org/project/<pkg>/#history`로 날짜 확정 → `releases/tag/<ver>`로 내용 확인**
- ⚠️ WebFetch가 GitHub 날짜의 **연도를 틀리게 렌더링**하는 경우 있음(2026 → 2024). 내용으로 교차 확인
- 트렌딩 대체 소스: `marc-ko/daily-trending-repo`, `*/news-radar`, `*/agents-radar` 이슈 아카이브 (agent 편중 있음)

**기타**
- `huggingface.co/changelog` — 플랫폼 기능 업데이트에 매우 유용, 날짜 명시됨. 공식 블로그보다 신뢰도 높음
- HF 데이터셋 트렌딩은 캐시가 오래됐을 수 있음 → 확인 안 되면 정직하게 한계로 보고

## 자주 하는 실수

- HF Daily Papers 날짜를 논문 날짜로 착각 → **항상 abs 확인**
- 벤더 자체 측정 벤치마크를 독립 검증된 수치처럼 쓰기 → "(자체 측정)" 표기
- 소문·단독 보도를 공식 발표처럼 쓰기 → "(Reuters 단독, 공식 발표 아님)" 표기
- 매체별로 엇갈리는 수치(밸류에이션 등)를 하나 골라 단정 → 상충 사실을 밝히고 확실한 것만 인용
- 지난 주 항목을 다시 넣기 → 제외 목록을 서브에이전트 프롬프트에 반드시 전달
- 💡 줄에 요약을 반복하기 → 함의를 써야 한다
