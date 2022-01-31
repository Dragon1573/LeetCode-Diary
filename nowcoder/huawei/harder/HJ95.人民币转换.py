""" HJ95 - 人民币转换

# 描述

1. 中文大写金额数字前应标明『人民币』字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、
捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。

2. 中文大写金额数字到『元』为止的，在『元』之后，应写『整』字，如 532.00 应写成
『人民币伍佰叁拾贰元整』，在『角』和『分』后面不写『整』字。

3. 阿拉伯数字中间有『0』时，中文大写要写『零』字，阿拉伯数字中间连续有几个『0』时，
中文大写金额中间只写一个『零』字，如 6007.14 ，应写成『人民币陆仟零柒元壹角肆分』。

4. 10 应写作『拾』，100 应写作『壹佰』。例如，1010.00 应写作『人民币壹仟零拾元整』，
110.00 应写作『人民币壹佰拾元整』。

5. 十万以上的数字接千不用加『零』，例如， 30105000.00 应写作『人民币叁仟零拾万伍仟元整』

本题含有多组样例输入。

# 示例

输入：
    151121.15
    10012.02
    13.64
    0.85
输出：
    人民币拾伍万壹仟壹佰贰拾壹元壹角伍分
    人民币壹万零拾贰元贰分
    人民币拾叁元陆角肆分
    人民币捌角伍分

输入：
    1010.00
    110.00
输出：
    人民币壹仟零拾元整
    人民币壹佰拾元整
"""
ch = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']

while True:
    try:
        s = input()
        before, after = s.split('.')
        head, body, tail = '人民币', '', ''

        # 处理小数
        if after == '00':
            tail = '元整'
        else:
            if before == '0':
                tail = ''
            else:
                tail = '元'
            if after[0] != '0':
                tail += ch[int(after[0])] + '角'
            if after[1] != '0':
                tail += ch[int(after[1])] + '分'

        # 四位一组进行分组
        array, i = [], len(before)
        while i - 4 >= 0:
            array.insert(0, before[i - 4:i])
            i -= 4
        if i > 0:
            array.insert(0, before[:i])

        # 遍历分组，依次处理
        for i, num in enumerate(array):  # 如：['15', '1121']
            flag = True
            for j, c in enumerate(num):
                if c == '0':
                    if num == '0000':
                        if array[-1] != '0000' and flag:
                            body += '零'
                            flag = False
                            continue
                    else:
                        if j != len(num) - 1 and num[j + 1] != '0' and flag:
                            body += '零'
                            flag = False
                            continue
                else:
                    if len(num[j:]) == 4:
                        body += ch[int(c)] + '仟'
                    elif len(num[j:]) == 3:
                        body += ch[int(c)] + '佰'
                    elif len(num[j:]) == 2:
                        if c != '1':
                            body += ch[int(c)] + '拾'
                        else:
                            body += '拾'
                    else:
                        body += ch[int(c)]
            if len(array[i:]) == 3:
                body += '亿'
            elif len(array[i:]) == 2 and num != '0000':
                body += '万'
        print(head + body + tail)

    except Exception:
        break
