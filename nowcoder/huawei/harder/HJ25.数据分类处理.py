""" HJ25 - 数据分类处理

# 描述

信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、QQ用户、手机号码、银行帐号等信息及活动记录。
采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。

请注意本题有多组输入用例。

数据范围：
    1 <= i, r <= 100
    0 <= val <= (2**31 - 1)

# 输入描述

一组输入整数序列 I 和一组规则整数序列 R
I 和 R 序列的第一个整数为序列的个数（个数不包含第一个整数）

# 输出描述

1. 从 R 依次中取出 R<i> ，对 I 进行处理，找到满足条件的 I ；
2. I 整数对应的数字需要连续包含 R<i> 对应的数字，比如 R<i> 为 23 ， I 为 231 ，那么 I 包含了 R<i> ，条件满足；

按 R<i> 从小到大的顺序：

1. 先输出 R<i> ；
2. 再输出满足条件的 I 的个数；
3. 然后输出满足条件的 I 在 I 序列中的位置索引（从0开始）；
4. 最后再输出 I 。

附加条件：

1. R<i> 需要从小到大排序。相同的 R<i> 只需要输出索引小的以及满足条件的 I ，索引大的需要过滤掉
2. 如果没有满足条件的 I ，对应的 R<i> 不用输出
3. 最后需要在输出序列的第一个整数位置记录后续整数序列的个数（不包含『个数』本身）

# 示例

输入：
    15 123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123
    5 6 3 6 3 0
输出：30 3 6 0 123 3 453 7 3 9 453456 13 453 14 123 6 7 1 456 2 786 4 46 8 665 9 453456 11 456 12 786
说明：
    开头的 30 表示后续有 30 个数
    随后的 3 表示从大到小排列，首个 R<i> 是 0 但没有满足条件的 I （不输出），第二个 R<i> 满足条件为 3
    其次的 6 表示存在 6 个包含 3 的 I
    紧接的 0 表示 123 所在的原序号是 0
    最后的 123 表示字符串 "123" 包含 "3" ，满足条件

    将序列 R: 5,6,3,6,3,0（第一个 5 表明后续有 5 个整数）排序去重后，可得 [0,3,6] 。
    序列 I 没有包含 0 的元素。
    序列 I 中包含 3 的元素：
        I[0] 的值为 123 、I[3] 的值为 453 、I[7] 的值为 3
        I[9] 的值为 453456 、I[13] 的值为 453 、I[14] 的值为 123
    序列 I 中包含 6 的元素：
        I[1] 的值为 456 、I[2] 的值为 786 、I[4] 的值为 46 、I[8] 的值为 665
        I[9] 的值为 453456 、I[11] 的值为 456 、I[12] 的值为 786
    最后按题目要求的格式进行输出即可。
"""
try:
    while True:
        # 输入数据
        n_i, *array_i = input().strip().split()
        n_r, *array_r = map(int, input().strip().split())
        result = []

        # 序列 R 排序
        array_r = [str(_) for _ in sorted(list(set(array_r)))]
        for r in array_r:
            temp = [None, 0]
            # 输出 R<i>
            temp[0] = r
            for index, i in enumerate(array_i):
                if r in i:
                    # 累计出现频次
                    temp[1] += 1
                    # 记录索引
                    temp.append(index)
                    # 记录值
                    temp.append(i)
            # 仅输出有满足条件的 R<i>
            if temp[1] > 0:
                result.extend(temp)
        print(len(result), *result)
except Exception:
    pass
