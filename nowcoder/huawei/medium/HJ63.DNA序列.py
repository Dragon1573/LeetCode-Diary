""" HJ63 DNA序列

# 描述

一个 DNA 序列由 A/G/C/T 四个字母的排列组合组成。 G 和 C 的比例（定义为
GC-Ratio）是序列中 G 和 C 两个字母的总的出现次数除以总的字母数目（也就
是序列长度）。在基因工程中，这个比例非常重要。因为高的 GC-Ratio 可能是
基因的起始点。

给定一个很长的 DNA 序列，以及限定的子串长度 N ，请帮助研究人员在给出的
DNA 序列中从左往右找出 GC-Ratio 最高且长度为 N 的第一个子串。DNA 序列
为 ACGT 的子串有: ACG, CG, CGT 等等，但是没有 AGT, CT 等等。

# 数据范围

数据范围：字符串长度满足 1 <= n <= 1000 ，输入的字符串只包含 A/C/G/T 字
母。

# 输入描述

输入一个 string 型基因序列，和 int 型子串的长度。

# 输出描述

找出 GC 比例最高的子串，如果有多个则输出第一个的子串。

# 示例

输入：ACGT
      2
输出：CG
说明：ACGT 长度为2的子串有 AC, CG, GT 3个，其中 AC 和 GT 2个的
      GC-Ratio 都为 0.5，CG 为 1，故输出 CG 。

输入：AACTGTGCACGACCTGA
      5
输出：GCACG
说明：虽然 CGACC 的 GC-Ratio 也是最高，但它是从左往右找到的 GC-Ratio
      最高的第2个子串，所以只能输出 GCACG 。
"""
if __name__ == '__main__':
    DNA_series = input().strip()
    N = int(input())

    size = len(DNA_series)
    begin, ratio = 0, 0
    for _ in range(size - N + 1):
        r = DNA_series.count('G', _, _ + N) + DNA_series.count('C', _, _ + N)
        if r > ratio:
          ratio = r
          begin = _
    print(DNA_series[begin:begin + N)
        
