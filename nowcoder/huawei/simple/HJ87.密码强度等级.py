r""" HJ87- 密码强度等级

# 描述

密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。请根据输入的密码字符串，进行安全评定。

一、密码长度:                           二、字母:                               三、数字:
    5分：小于等于4个字符                    0分：没有字母                           0分：没有数字
    10分：5到7字符                         10分：全都是小（大）写字母               10分：1个数字
    25分：大于等于8个字符                   20分：大小写混合字母                    20分：大于1个数字

四、符号:                               五、奖励:
    0分：没有符号                           2分：字母和数字
    10分：1个符号                           3分：字母、数字和符号
    25分：大于1个符号                       5分：大小写字母、数字和符号

最后的评分标准:                         对应输出为：
    >= 90：非常安全                         VERY_SECURE
    >= 80：安全（Secure）                   SECURE
    >= 70：非常强                           VERY_STRONG
    >= 60：强（Strong）                     STRONG
    >= 50：一般（Average）                  AVERAGE
    >= 25：弱（Weak）                       WEAK
    >= 0：非常弱                            VERY_WEAK

注：
    字母：a-z, A-Z
    数字：0-9
    符号包含如下： (ASCII 码表可以在 UltraEdit 的菜单 View -> ASCII Table 查看)
        !"#$%&'()*+,-./     (ASCII 码：0x21 ~ 0x2F)
        :;<=>?@             (ASCII 码：0x3A ~ 0x40)
        [\]^_`              (ASCII 码：0x5B ~ 0x60)
        {|}~                (ASCII 码：0x7B ~ 0x7E)

提示：1 <= len(s) <= 300

# 输入 & 输出

本题含有多组输入样例，每组样例输入一个 string 的密码。
每组样例输出密码等级。

# 示例

输入：
    38$@NoNoNo
    123
输出：
    VERY_SECURE
    WEAK
说明：
    第一组样例的密码长度大于等于8个字符，得25分；大小写字母都有所以得20分；有两个数字，所以得20分；包含大于1符号，所以得25分；
    由于该密码包含大小写字母、数字和符号，所以奖励部分得5分，经统计得该密码的密码强度为 25+20+20+25+5=95 分。
    同理，第二组样例密码强度为 5+0+20+0+0=25 分。

输入：Jl)M:+
输出：AVERAGE
说明：示例2的密码强度为 10+20+0+25+0=55 分。
"""
from sys import stdin

for line in stdin:
    score = 0

    # 规则一
    length = len(line.strip())
    if length <= 4:
        score += 5
    elif 5 <= length <= 7:
        score += 10
    elif length >= 8:
        score += 25

    # 规则二 ～ 规则四
    array = [0, 0, 0, 0]
    for _ in line:
        if _.isdigit():
            array[0] += 1
        elif _.isupper():
            array[1] += 1
        elif _.islower():
            array[2] += 1
        value = ord(_)
        if 0x21 <= value <= 0x2F or 0x3A <= value <= 0x40:
            array[3] += 1
        elif 0x5B <= value <= 0x60 or 0x7B <= value <= 0x7E:
            array[3] += 1

    # 规则二
    if array[1] > 0 and array[2] > 0:
        score += 20
    elif array[1] + array[2] > 0:
        score += 10

    # 规则三
    if array[0] > 1:
        score += 20
    elif array[0] == 1:
        score += 10

    # 规则四
    if array[3] > 1:
        score += 25
    elif array[3] == 1:
        score += 10

    # 规则五
    if array[0] and array[1] and array[2] and array[3]:
        score += 5
    elif array[0] and (array[1] + array[2]) and array[3]:
        score += 3
    elif array[0] and (array[1] + array[2]):
        score += 2

    # 等级判断
    if score >= 90:
        print('VERY_SECURE')
    elif score >= 80:
        print('SECURE')
    elif score >= 70:
        print('VERY_STRONG')
    elif score >= 60:
        print('STRONG')
    elif score >= 50:
        print('AVERAGE')
    elif score >= 25:
        print('WEAK')
    else:
        print('VERY_WEAK')
