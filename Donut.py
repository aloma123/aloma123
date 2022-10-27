"""HW"""
def main():
    """donut"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    box = numb+numc
    pricebox = numa*numb
    numbox = numd//box
    remain = numd - (numbox*box)
    if remain >= numb:
        numbox = numbox + 1
        remain = 0
    price = numbox*pricebox + remain*numa
    piece = numbox*box +remain
    print(price, piece)
main()
