"iPhone 13 Again"
def main():
    "main"
    model = input()
    rom = input()
    def mingb():
        "rom"
        if model == "iPhone 13 mini":
            print(25900)
        elif model == "iPhone 13":
            print(29900)
        elif model == "iPhone 13 Pro":
            print(38900)
        elif model == "iPhone 13 Pro Max":
            print(42900)
        else:
            print("Not Available")
    def normalgb():
        "rom"
        if model == "iPhone 13 mini":
            print(259900)
        elif model == "iPhone 13":
            print(33900)
        elif model == "iPhone 13 Pro":
            print(42900)
        elif model == "iPhone 13 Pro Max":
            print(46900)
        else:
            print("Not Available")
    def maxgb():
        "rom"
        if model == "iPhone 13 mini":
            print(37900)
        elif model == "iPhone 13":
            print(31900)
        elif model == "iPhone 13 Pro":
            print(50900)
        elif model == "iPhone 13 Pro Max":
            print(44900)
        else:
            print("Not Available")
    def romtb():
        "rom"
        if model == "iPhone 13 Pro":
            print(58900)
        elif model == "iPhone 13 Pro Max":
            print(62900)
        else:
            print("Not Available")
    if rom == "128 GB":
        mingb()
    elif rom == "256 GB":
        normalgb()
    elif rom == "512 GB":
        maxgb()
    elif rom == "1 TB":
        romtb()
    else:
        print("Not Available")
main()
