""" HJ36 - 字符串加密

https://www.nowcoder.com/practice/e4af1fe682b54459b2a211df91a91cf3
"""
try:
    while True:
        key = input().strip()
        raw = input().strip()

        # 生成映射表
        trans = []
        for _ in key:
            if _ not in trans:
                trans.append(_)
        for _ in range(97, 97 + 26):
            if chr(_) not in trans:
                trans.append(chr(_))

        passwd = [trans[ord(_) - 97] for _ in raw]
        print(''.join(passwd))
except Exception:
    pass
