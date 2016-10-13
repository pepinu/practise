suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
result = []
loops = int(raw_input())
cards = raw_input().split()
cards = map(int, cards)
for i in cards:
    suit_value = i / 13
    rank_value = i % 13
    result.append(ranks[rank_value] + "-of-" + suits[suit_value]) 
print ' '.join(map(str, result))


