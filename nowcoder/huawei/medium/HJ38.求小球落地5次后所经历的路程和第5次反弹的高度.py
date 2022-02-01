""" HJ38 - 求小球落地5次后所经历的路程和第5次反弹的高度

https://www.nowcoder.com/practice/2f6f9339d151410583459847ecc98446
"""
if __name__ == '__main__':
    height = int(input())
    print(height * (3 - 1 / 8), height * 1 / 32, sep='\n')
