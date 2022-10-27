"RockPaperScissor"
def main():
    "main"
    key = input()
    awin = 0
    bwin = 0
    for i in range(0, len(key), 2):
        if key[i] == key[i + 1]:
            pass
        elif key[i] == "P" and key[i + 1] == "R":
            awin += 1
        elif key[i] == "R" and key[i + 1] == "S":
            awin += 1
        elif key[i] == "S" and key[i + 1] == "P":
            awin += 1
        else:
            bwin += 1
    if awin > bwin:
        print("A win " + str(awin) + "-" + str(bwin))
    elif awin < bwin:
        print("B win " + str(bwin) + "-" + str(awin))
    else:
        print("DRAW %s" % awin)
main()
