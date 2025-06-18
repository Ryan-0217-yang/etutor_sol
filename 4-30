n = int(input())
segments = []

for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments.sort()

total = 0
cur_start, cur_end = segments[0]

for i in range(1, n):
    start, end = segments[i]
    if start <= cur_end:
        cur_end = max(cur_end, end)
    else:
        total += cur_end - cur_start
        cur_start, cur_end = start, end

total += cur_end - cur_start

print(total)
