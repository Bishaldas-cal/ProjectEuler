import math

def get_period_length(x):
    root = int(math.isqrt(x))
    if root * root == x:
        return 0

    a = root
    numerator = 0
    denominator = 1
    period = 0

    while a != 2 * root:
        numerator = denominator * a - numerator
        denominator = (x - numerator * numerator) // denominator
        a = (root + numerator) // denominator
        period += 1

    return period

def count_odd_periods(last):
    return sum(1 for i in range(2, last + 1) if get_period_length(i) % 2 == 1)

if __name__ == "__main__":
    last = int(input("Enter the upper limit: "))
    print(count_odd_periods(last))
