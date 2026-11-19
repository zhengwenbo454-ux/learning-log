count = 100
def modify_count():
    global count
    count += 10
    print(f"函数内部修改后的count值: {count}")

if __name__ == "__main__":
    print(f"初始count值: {count}")
    modify_count()
    print(f"函数调用后count值: {count}")

def modify_count_local():
    count = 50  # 局部变量
    count += 10
    print(f"函数内部局部count值: {count}")

if __name__ == "__main__":
    print(f"初始count值: {count}")
    modify_count()
    print(f"函数调用后count值: {count}")
    modify_count_local()
    print(f"函数调用后count值: {count}")

def modify_count_nonlocal():
    count = 30  # 外层函数的局部变量
    def inner_function():
        nonlocal count
        count += 10
        print(f"内层函数修改后的count值: {count}")
    inner_function()
    print(f"外层函数调用后count值: {count}")