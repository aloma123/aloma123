"iPhone 13 Again"
def main():
    "main"
    phone = input()
    rom = input()
    total = 0
    if rom == "128 GB":
        pass
    elif rom == "256 GB":
        total += 4000
    elif rom == "512 GB":
        total += 12000
    elif rom == "1 TB":
        total += 20000
    else:
        print("Not Available")
    if phone == "iPhone 13 mini":
        total += 25900
        if rom != "128 GB" or "256 GB" or"512 GB":
            print("Not Available")
        else:
            print(total)
    elif phone == "iPhone 13":
        total += 29900
        if rom != "128 GB" or "256 GB" or"512 GB":
            print("Not Available")
        else:
            print(total)
    elif phone == "iPhone 13 Pro":
        total += 38900
        print(total)
    elif phone == "iPhone 13 Pro Max":
        total += 42900
        print(total)
    else:
        print("Not Available")
main()
