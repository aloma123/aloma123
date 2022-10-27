"""HW"""
def number(value_1, value_2):
    """number"""
    if value_1 > value_2:
        return value_1
    return value_2
def main():
    """main"""
    numx = input()
    numy = input()
    numz = input()
    lastest = numx + numy + numz
    lastest = number((numx + numz + numy), lastest)
    lastest = number((numy + numx + numz), lastest)
    lastest = number((numy + numz + numx), lastest)
    lastest = number((numz + numy + numx), lastest)
    lastest = number((numz + numx + numy), lastest)
    print(int(lastest))
main()
