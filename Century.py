"Century"
import math

def main():
    "mian"
    num = int(input())
    for _ in range(num):
        txt = input()
        numt = txt[:4]
        years = int(txt[5:])
        if numt == "B.E." and years <= 543:
            print("ERROR")
        elif numt == "B.E.":
            century = math.ceil((years - 543)/100)
            print(century)
        else:
            century = math.ceil(years/100)
            print(century)
main()
