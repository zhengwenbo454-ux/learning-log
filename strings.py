"""
strings.py
字符串工具：词频统计、字符串回文判断
"""

def is_palindrome_str(s: str) -> bool:
    """
    字符串版本回文判断，直接切片比较
    :param s: 输入字符串
    :return: True是回文，False不是
    """
    return s == s[::-1]


def word_frequency(text: str) -> list[tuple[str, int]]:
    """
    文本词频统计：转小写、去除标点、按出现次数降序排序
    :param text: 原始长文本
    :return: 列表 [(单词,次数), ...]，按次数从高到低
    """
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text = text.lower()
    # 清除标点
    for p in punctuation:
        text = text.replace(p, "")
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # 降序排序
    sorted_items = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_items
