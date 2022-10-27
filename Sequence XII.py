"Sequence XII"
def main():
    "print"
    num = int(input())
    def front(num):
        "front"
        for i in range(1, num, 1):
            for front in range(num+1-i, num, 1):
                print("%02d" % front, end=" ")
            for middle1 in range(num, i-1, -1):
                print("%02d" % middle1, end=" ")
            for middle2 in range(i+1, num+1, 1):
                print("%02d" % middle2, end=" ")
            for back in range(num-1, num-i, -1):
                print("%02d" % back, end=" ")
            print()
    front(num)
    for j in range(1, num*2, 1):
        if j < num:
            print("%02d" % j, end=" ")
        else:
            print("%02d" % ((num*2)-j), end=" ")
    print()
    def back(num):
        "back"
        for i in range(1, num, 1):
            for front in range(i+1, num, 1):
                print("%02d" % front, end=" ")
            for middle1 in range(num, num-1-i, -1):
                print("%02d" % middle1, end=" ")
            for middle2 in range(num+1-i, num+1, 1):
                print("%02d" % middle2, end=" ")
            for back in range(num-1, i, -1):
                print("%02d" % back, end=" ")
            print()
    back(num)
main()
