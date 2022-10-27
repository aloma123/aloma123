"Sequence VIII"
def main():
    "main"
    num = int(input())
    i = 0
    while i < num:
        i += 1
        j = 0
        print(" "*(3*(num-i)), end="")
        while j < i:
            j += 1
            print("%02d" % j, end=" ")
        print()
main()
