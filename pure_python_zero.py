f = open("scores.csv", "r", 
            encoding="utf-8")
lines = f.readlines()
f.close()

#1단계 파일 읽기
#print(len(lines))
#print(lines[0])
#print(lines[1])

'''
#2단계: 헤더 파싱
#header = lines[0].strip().split(",")
#print(header)
#print(first_line)
'''

'''
#3단계: 카테고리별 점수 출력
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

for line in lines[1:4]:
    parts = line.strip().split(",")
    print(parts[cat_idx], 
            parts[score_idx])
'''

'''
#4단계: 점수 계산(빈줄에서 에러)
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

for line in lines[1:]:
    parts = line.strip().split(",")
    score = float(parts[score_idx])
    print(parts[cat_idx], score)
'''

'''
#5단계: 점수 계산(빈칸은 잘 건너갔는데, 미제출이라는 답변이 있어서 에러)
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    score = float(raw)
    print(parts[cat_idx], score)
'''

'''
#6단계: 점수 계산(빈칸은 잘 건너갔는데, 미제출이라는 답변이 있어서 에러)
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    score = float(raw)
    print(parts[cat_idx], score)
'''


   # 1. 에러 발생마다 예외사항 넣어주기인데 이제는 해보고 안되면 뛰어넘는 방식을 할것임
#7단계
'''
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count = 0

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    try:
        score = float(raw)
    except ValueError:
        
        continue
    count += 1

print("사용한 행의 수:", count)
'''
 #8단계
'''
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count = 0
totals = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    try:
        score = float(raw)
    except ValueError:
        continue
    
    category = parts[cat_idx]
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0
    totals[category] += score
    counts[category] += 1

    count += 1

print(totals)
print(counts)
'''
 
#9단계
header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count = 0
totals = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        score = 0.0
    else:
        try:
            score = float(raw)
        except ValueError:
            continue
    
    category = parts[cat_idx]
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0
    totals[category] += score
    counts[category] += 1

    count += 1

print(totals)
print(counts)

for c in sorted(totals.keys()):
    avg = totals[c] / counts[c]
    print(c, round(avg, 2))