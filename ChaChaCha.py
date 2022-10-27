"ChaChaCha"
import math
def main():
    "main"
    days = int(input())
    income = 0
    for _ in range(days):
        num_hr = math.ceil(float(input()))
        income += num_hr*8720
    print(income)
main()
