"FOR!F-Ball"
def main():
    "main"
    key = input()
    ball = 1
    for i in range(0, len(key)):
        if key[i] == "A" and ball == 1:
            ball = 2
        elif key[i] == "A" and ball == 2:
            ball = 1
        if key[i] == "B" and ball == 2:
            ball = 3
        elif key[i] == "B" and ball == 3:
            ball = 2
        if key[i] == "C" and ball == 1:
            ball = 3
        elif key[i] == "C" and ball == 3:
            ball = 1
    print(ball)
main()
