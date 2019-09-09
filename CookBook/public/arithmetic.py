"""
第一章：数据结构和算法
"""


def drop_first_last(grades):
    """
    去掉最高，最低分，求平均
    :param grades:
    :return:
    """
    if isinstance(grades, (list, tuple)):
        grades.sort()
        first, *middle, last = grades
        return get_average(middle)


def get_average(record):
    """
    求平均
    :param record:
    :return:
    """
    if isinstance(record, (list, tuple)):
        return get_sum(record) / len(record)


def get_sum(items):
    """
    递归求和
    :param items:
    :return:
    """
    head, *tail = items
    return head + get_sum(tail) if tail else head

