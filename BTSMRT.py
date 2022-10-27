"BTSMRT"
def main():
    "main"
    day = input()
    age = float(input())
    tall = float(input())
    if age < 14 and tall < 90:
        print("FREE")
    elif age < 14 and tall <= 140 and day == "Children Day":
        print("FREE")
    elif age >= 60 and day == "Senior Day":
        print("FREE")
    else:
        print("PAY")
main()
