# leetcode 50
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Time Complexity:
# Space Complexity:

def pow(x,n):
    def calc_power(base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1

        half = calc_power(base, exponent // 2)
        half = half * half

        if exponent % 2 == 1:
            half = half * base

        return half

    result = calc_power(x, abs(n))

    if n >= 0:
        return result

    return 1 / result

print(pow(2.00000,10))
print(pow(2.10000,3))