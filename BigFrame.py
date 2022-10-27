"BigFrame"
def main():
    "main"
    line2 = input().strip()
    line3 = input().strip()
    line4 = input().strip()
    line5 = input().strip()
    line6 = input().strip()
    most = max(len(line2), len(line3), len(line4), len(line5), len(line6))
    print("*" * (most + 4))
    box = (line2, line3, line4, line5, line6)
    for i in box:
        print("* " + i + (" " * (most - len(i))) + " *")
    print("*" * (most + 4))
main()
