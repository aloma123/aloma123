"Squid Game 3"
def main():
    "main"
    scorea = 0
    scoreb = 0
    for _ in range(10):
        teama = int(input())
        scorea += teama
    for _ in range(10):
        teamb = int(input())
        scoreb += teamb
    if scorea > scoreb:
        print("B")
    elif scoreb > scorea:
        print("A")
    else:
        print("AB")
main()
