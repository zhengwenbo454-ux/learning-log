def add_item(item, lst=None):
    """
    添加元素，避开可变默认参数陷阱
    :param item: 待添加元素
    :param lst: 列表，默认None
    :return: 新列表
    """
    if lst is None:
        lst = []
    lst.append(item)
    return lst

if __name__ == "__main__":
    print(add_item(1))
    print(add_item(2))
    print(add_item(3))
