"""
main.py
程序入口：调用模块里的函数，处理输入、打印结果
"""
import time
from numbers import dec2bin, digit_sum, hailstone_sequence, is_palindrome, countdown
from strings import is_palindrome_str, word_frequency


def main():
    print("===== 数字工具测试 =====")
    num = 10
    print(f"{num} 二进制：{dec2bin(num)}")
    print(f"{num} 各位和：{digit_sum(num)}")
    print(f"冰雹步数(10): {len(hailstone_sequence(10)) - 1}")
    print(f"121 是否回文数：{is_palindrome(121)}")

    print("\n===== 倒计时演示 =====")
    cd_list = countdown(5)
    for v in cd_list:
        print(v)
        time.sleep(1)
    print("倒计时结束！")

    print("\n===== 字符串工具测试 =====")
    test_str = "racecar"
    print(f"{test_str} 是否回文：{is_palindrome_str(test_str)}")

    sample_text = "Hello, World! This is a sample text for testing purposes."
    freq_result = word_frequency(sample_text)
    print("词频统计：")
    for w, c in freq_result:
        print(f"{w}: {c}")


if __name__ == "__main__":
    main()
