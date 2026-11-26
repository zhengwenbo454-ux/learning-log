def calc(a, b):
    try:
        res = a / b
    except ZeroDivisionError as e:
        print(f"捕获异常：{e}")
    else:
        print(f"计算结果：{res}")
    finally:
        print("函数执行结束")
calc(10, 2)
calc(10, 0)
