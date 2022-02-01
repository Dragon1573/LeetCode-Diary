""" HJ48 - 从单向链表中删除指定值的节点

https://www.nowcoder.com/practice/f96cd47e812842269058d483a11ced4f
"""
if __name__ == '__main__':
    array = [int(_) for _ in input().split()]
    n, head, array, drop = array[0], array[1], array[2:-1], array[-1]
    link_list = [head]
    for _ in range(0, len(array), 2):
        index = link_list.index(array[_ + 1])
        link_list.insert(index + 1, array[_])
    link_list.remove(drop)
    print(*link_list)
