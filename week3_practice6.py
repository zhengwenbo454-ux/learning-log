def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    n = int(input("请输入一个整数: "))
    result = fib(n)
    print(f"斐波那契数列的第 {n} 项为: {result}")
    