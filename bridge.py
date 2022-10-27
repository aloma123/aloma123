"""HW"""
def main():
    """bridge"""
    puta = int(input())
    putb = int(input())
    goal = int(input())
    bneed = goal//5
    bused = min(bneed, putb)
    aused = goal - bused*5
    if aused > puta:
        print(-1)
    else:
        print(aused)
main()
