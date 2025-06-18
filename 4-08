n = int(input())
my_cards = set(map(int, input().split()))
count = 0

for _ in range(n):
    cards = list(map(int, input().split()))
    for card in cards:
        if card in my_cards:
            count += 1
            my_cards.discard(card)  

print(count)
