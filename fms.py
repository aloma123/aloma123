"""Future Message"""
def main():
    """Future Message"""
    var = input()
    if var.islower():
        print("Lowercase")
    elif var.isupper():
        print("Uppercase")
    elif var.istitle():
        print("Title")
    elif var.isspace():
        print("Space")
    elif var.isnumeric():
        print("Number")
    else:
        print("Other")
main()
