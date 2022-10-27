"Books"
import math
def main():
    "main"
    book = int(input())
    page = int(input())
    ups = int(input())
    down = int(input())
    day = 0
    read = 0
    while book != 0:
        read += math.ceil(page*((ups + day)/(down + day)))
        if read > page:
            read = 0
            book -= 1
        elif read == page:
            day = day + book
            break
        day += 1
    print(day)
main()
