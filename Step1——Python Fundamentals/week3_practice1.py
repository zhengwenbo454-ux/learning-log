def min_max_avg(numbers):
    """
    计算数字列表的最小值、最大值和平均值
    """
    if not numbers:
        return None, None, None  # 如果列表为空，返回None

    min_value = min(numbers)
    max_value = max(numbers)
    avg_value = sum(numbers) / len(numbers)

    return min_value, max_value, avg_value

if __name__ == "__main__":
    # 测试 min_max_avg 函数
    test_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    min_val, max_val, avg_val = min_max_avg(test_numbers)
    print(f"最小值: {min_val}, 最大值: {max_val}, 平均值: {avg_val}")

    