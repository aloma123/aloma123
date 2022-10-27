"seqXI"

def main():
    "main"
    num = int(input())
    for i in range(1, num, 1):
        for front in range(1, i+1, 1):
            print("%02d" % front, end=" ")
        for middle in range(1, (num*2)-(i*2)):
            print("%02d" % i, end=" ")
            middle = middle + 1
        for back in range(i, 0, -1):
            print("%02d" % back, end=" ")
        print()
    for j in range(1, num*2, 1):
        if j < num:
            print("%02d" % j, end=" ")
        else:
            print("%02d" % ((num*2)-j), end=" ")
    print()
    for i in range(1, num, 1):
        for front in range(1, num+1-i, 1):
            print("%02d" % front, end=" ")
        for middle in range(1, i*2):
            print("%02d" % (num - i), end=" ")
            middle = middle + 1
        for back in range(num-i, 0, -1):
            print("%02d" % back, end=" ")
        print()
main()
