"""기간 안 HF Daily Papers 후보를 한 번에 모은다.

usage: python3 scripts/fetch_papers.py 2026-09-28 2026-10-05 > /tmp/papers.md
- 평일 daily 페이지 + 해당 ISO 주간 페이지를 합치고 publishedAt이 기간 안인 것만 남긴다
- briefings/*.md 에 이미 나온 arXiv ID는 뺀다 (지난 회차 중복 제외)
- upvote 순, 초록은 앞 500자만 (전문과 v1 날짜는 abs 페이지에서 확인할 것)
"""
import datetime as dt, glob, json, re, sys, urllib.request

start, end = (dt.date.fromisoformat(a) for a in sys.argv[1:3])
seen_before = {m for f in glob.glob('briefings/*.md') for m in re.findall(r'arxiv\.org/abs/(\d{4}\.\d{4,5})', open(f).read())}

def get(q):
    with urllib.request.urlopen(f'https://huggingface.co/api/daily_papers?{q}&limit=100', timeout=30) as r:
        return json.load(r)

urls, day = set(), start
while day <= end:
    if day.weekday() < 5:  # 주말 페이지는 없음
        urls.add(f'date={day}')
    y, w, _ = day.isocalendar()
    urls.add(f'week={y}-W{w:02d}')
    day += dt.timedelta(days=1)

papers = {}
for q in sorted(urls):
    try:
        rows = get(q)
    except Exception as e:  # 당일·미공개 페이지는 400
        print(f'<!-- skip {q}: {e} -->')
        continue
    for x in rows:
        p = x['paper']
        pub = p.get('publishedAt', '')[:10]
        if p['id'] in seen_before or not (str(start) <= pub <= str(end)):
            continue
        papers[p['id']] = (p.get('upvotes', 0), pub, p['title'], ' '.join(p.get('summary', '').split())[:500])

print(f'# 후보 {len(papers)}편 ({start} ~ {end}, 지난 회차 {len(seen_before)}개 ID 제외)\n')
for pid, (up, pub, title, summ) in sorted(papers.items(), key=lambda kv: -kv[1][0]):
    print(f'- **{pid}** · ▲{up} · {pub} · {title}\n  {summ}\n')
