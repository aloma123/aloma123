"Blackjack"
def main():
    "main"
    number = int(input())
    total = 0
    ace = 0
    if number == 2:
        first = input()
        second = input()
        hand = [first, second]
    elif number == 3:
        first = input()
        second = input()
        third = input()
        hand = [first, second, third]
    for i in range(0, len(hand)):
        if hand[i].isnumeric():
            hand[i] = int(hand[i])
        elif hand[i] == 'J':
            hand[i] = 10
        elif hand[i] == 'Q':
            hand[i] = 10
        elif hand[i] == 'K':
            hand[i] = 10
        elif hand[i] == 'A':
            hand[i] = 11
            ace = ace + 1
        total += hand[i]
    if ace == 3:
        total -= 20
    elif ace == 2 and total == 32:
        total -= 20
    elif ace == 2 and total > 21:
        total -= 10
    elif ace == 1 and total > 21:
        total -= 10
    print(total)
main()
