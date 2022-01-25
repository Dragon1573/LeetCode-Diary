""" HJ18 - 识别有效的IP地址和掩码并进行分类统计

# 字符串分段判别法
"""
from sys import stdin


def check_ip(ip: str) -> bool:
    """ 检查 IP 地址 """
    # 私有地址与五大类别不冲突，需要同时累计
    ip_bit = ip.split('.')
    # 四段值，且每一段不为空
    if len(ip_bit) != 4 or '' in ip_bit:
        return False
    for i in ip_bit:
        if int(i) < 0 or int(i) > 255:
            # 每一段必须在 0 ～ 255 中
            return False
    return True


def check_mask(mask: str) -> bool:
    """ 检查掩码 """
    if not check_ip(mask):
        # 掩码不符合 IP 地址要求
        return False
    if mask == '255.255.255.255' or mask == '0.0.0.0':
        # 掩码不能全0或全1
        return False
    # 将掩码转换为 32 位二进制数
    whole_mask = ''.join([bin(int(_))[2:].zfill(8) for _ in mask.split('.')])
    # 最后一个 1 应与最早一个 0 相邻
    return whole_mask.rfind("1") + 1 == whole_mask.find("0")


def check_private_ip(ip: str) -> bool:
    """ 检查私网地址 """
    a, b, _, _ = ip.split('.')
    is_private = False or a == '10'
    is_private = is_private or (a == '192' and b == '168')
    valid_part_2 = a == '172' and 16 <= int(b) <= 31
    return is_private or valid_part_2


if __name__ == "__main__":
    counter = [0] * 7
    for line in stdin:
        # 拆分地址与掩码
        ip, mask = line.strip().split('~')
        # 检查地址
        if check_ip(ip):
            first = int(ip.split('.')[0])
            if first == 127 or first == 0:
                # 特殊地址不计数
                continue
            if check_mask(mask):
                # 检查掩码，根据地址范围判断类别
                if check_private_ip(ip):
                    counter[6] += 1
                if 0 < first < 127:
                    counter[0] += 1
                elif 127 < first <= 191:
                    counter[1] += 1
                elif 192 <= first <= 223:
                    counter[2] += 1
                elif 224 <= first <= 239:
                    counter[3] += 1
                elif 240 <= first <= 255:
                    counter[4] += 1
                continue
        counter[5] += 1
    print(*counter)
