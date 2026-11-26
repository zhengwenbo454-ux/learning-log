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
calc(4, 0)

def AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("年龄不能为负数")
    assert age >= 18, "年龄必须满18岁"

try:
    check_age(-5)

except AgeError as e:
    raise ValueError ("年龄非法") from e


 
