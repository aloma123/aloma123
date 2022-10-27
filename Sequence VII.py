"Sequence VII"
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
    k = 0
    while k < num-1:
        k += 1
        numl = 0
        numo = num
        while numo > k:
            numl += 1
            numo -= 1
            print(numl, end=" ")
        print()
main()
