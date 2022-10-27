"PhoneNumber"
def main():
    "main"
    phone_num = input()
    nation = input()
    if nation == "International":
        phone_num = "+66" + phone_num[1:]
    print(phone_num[:-8], phone_num[-8:-4], phone_num[-4:])
main()
