"Key"
def main():
    "main"
    num_id = input()
    sum_id = 0
    for i in num_id:
        sum_id += int(i)
    last3 = int(num_id[-3:])*10
    key = sum_id + last3
    if key > 9999:
        key = int(str(key)[-4:])
    elif key < 1000:
        key = key + 1000
    print("%04d" % key)
main()
