def dec2bin(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def hailstone_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def is_palindrome(s):
    return s == s[::-1]

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("倒计时结束！")
