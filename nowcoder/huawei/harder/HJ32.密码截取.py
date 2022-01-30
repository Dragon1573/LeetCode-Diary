""" HJ32 - 密码截取（最长回文子串）

# 描述

Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
比如进行下列变化 ABBA -> 12ABBA, ABA -> ABAKK, 123321 -> 51233214。
因为截获的串太长了，而且存在多种可能的情况（abaaab 可看作是 aba，或 baaab 的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

数据范围：字符串长度满足 1 <= n <= 2500

# 示例

输入：ABBA
输出：4

输入：ABBBA
输出：5

输入：12HHHHA
输出：4

# 题解

中心对称扩展法

时间复杂度：O(n^2)
空间复杂度：O(1)
"""
if __name__ == '__main__':
    # 输入文字
    string = input()

    # 中心为一个元素时，每个字符自身必然是一个回文串
    single_center_list = [1] * len(string)
    # 遍历字符串中间的每一个位置
    for i in range(1, len(string) - 1):
        # 从中间向两侧进行扩展
        j = 0
        # 避免索引越界
        while j < min(i, len(string) - i - 1):
            j += 1
            # 如果回文对应位置字符相同，累计相同的数量
            if string[i - j] == string[i + j]:
                single_center_list[i] += 2
            else:
                break
    # 单个中心最长回文串长度
    single_center_max = max(single_center_list)

    # 中心为两个元素时，两个字符可能不相同，此时长度为0
    double_center_list = [0] * len(string)
    for i in range(1, len(string) - 1):
        j = 0
        # 标记寻找对称轴左侧的首个字符
        first_flag = True
        while j < min(i, len(string) - i - 2):
            j += 1
            if string[i] == string[i + 1]:
                # 对称轴两侧字符相同
                if first_flag:
                    # 回文串长度最少为2
                    double_center_list[i] = 2
                    # 移除标记
                    first_flag = False
                if string[i - j] == string[i + 1 + j]:
                    # 从中心向两侧扩展
                    double_center_list[i] += 2
                else:
                    break
            else:
                # 如果对称轴两侧字符直接不同，则这部分不是回文串
                break
    double_center_max = max(double_center_list)

    # 最长回文串是两种扫描方式中更长的
    print(max(single_center_max, double_center_max))
