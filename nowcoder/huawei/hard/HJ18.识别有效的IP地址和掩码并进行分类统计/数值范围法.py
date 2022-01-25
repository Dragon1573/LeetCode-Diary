""" HJ18 - 识别有效的IP地址和掩码并进行分类统计

# 数值范围法

1. 使用正则表达式判断地址和掩码是否符合格式规范
2. 将地址和掩码转换为32位无符号整数；
3. 根据题干给出的地址范围，转换为十六进制形式的上下界
4. 判断掩码与地址数值所在的数值范围
"""
from sys import stdin
from re import match


def ip2int(ip_addr: str) -> int:
    """ 将 IP 转换为数值表示 """
    if not match(r'\d{1,3}(.\d{1,3}){3}', ip_addr):
        return -1
    result = 0
    for i, v in enumerate(ip_addr.split('.')):
        result += int(v) << 8 * (3 - i)
    return result


counter = [0] * 7

for line in stdin:
    ip, mask = map(ip2int, line.strip().split('~'))

    if 0 <= ip <= 0x00FFFFFF or 0x7F000000 <= ip <= 0x7FFFFFFF:
        # 本地回环不属于任何一类
        continue

    if mask == 0 or mask == 0xFFFFFFFF:
        # 掩码不能全 0 或全 1
        invalid_mask = True

    i, invalid_mask = 0, False
    while i < 32:
        # 寻找最后一个 1
        if mask & (1 << i) == (1 << i):
            break
        i += 1
    while i < 32:
        # 寻找前面的 0
        if mask & (1 << i) == 0:
            invalid_mask = True
            break
        i += 1
    if invalid_mask:
        # 非法掩码
        counter[5] += 1
        continue

    if 0x0A000000 <= ip <= 0x0AFFFFFF or 0xAC100000 <= ip <= 0xAC1FFFFF:
        # 私有地址
        counter[6] += 1
    elif 0xC0A80000 <= ip <= 0xC0A8FFFF:
        counter[6] += 1
    if 0x01000000 <= ip <= 0x7EFFFFFF:
        # A 类地址
        counter[0] += 1
    elif 0x80000000 <= ip <= 0xBFFFFFFF:
        # B 类地址
        counter[1] += 1
    elif 0xC0000000 <= ip <= 0xDFFFFFFF:
        # C 类地址
        counter[2] += 1
    elif 0xE0000000 <= ip <= 0xEFFFFFFF:
        # D 类地址
        counter[3] += 1
    elif 0xF0000000 <= ip <= 0xFFFFFFFF:
        # E 类地址
        counter[4] += 1
    else:
        # 非法 IP
        counter[5] += 1

print(*counter)
