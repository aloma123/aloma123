"Sequence VI"
def main():
    "main"
    num = int(input())
    i = 0
    while i < num:
        i += 1
        j = 0
        while j < i:
            j += 1
            print(j, end=" ")
        print()
main()
