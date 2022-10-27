"BootSequence"
def main():
    "main"
    num = int(input())
    for i in range(1, num+1):
        if i == num:
            print(num)
            break
        print(i, end="_")
main()
