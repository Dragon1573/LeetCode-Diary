""" HJ66 - 配置文件恢复

时间限制：C/C++ 1秒，其他 2秒
空间限制 C/C++ 32MB ，其他 64MB

## 描述

有6条配置命令，它们执行的结果分别是：

|       命令       |      执行       |
| :--------------: | :-------------: |
|      reset       |   reset what    |
|   reset board    |   board fault   |
|    board add     |  where to add   |
|   board delete   | no board at all |
| reboot backplane |   impossible    |
| backplane abort  |  install first  |
|      he he       | unknown command |

为了简化输入，方便用户，以 "最短唯一匹配原则" 匹配：

1. 若只输入一字串，则只匹配一个关键字的命令行。

    例如输入： "r" ，根据该规则，匹配命令 "reset" ，执行结果为： "reset what" ；
    输入： "res" ，根据该规则，匹配命令 "reset" ，执行结果为： "reset what" ；

2. 若只输入一字串，但匹配命令有两个关键字，则匹配失败。

    例如输入： "reb" ，可以找到命令 "reboot backpalne" ，但是该命令有两个关键词，所有匹配失败。

3. 若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果仍不唯一，匹配失败。

    例如输入： "r b" ，找到匹配命令 "reset board" 和 "reboot backplane" 。
    例如输入： "b a" ，无法确定是命令 "board add" 还是 "backplane abort" ，匹配失败。

4. 若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果唯一，匹配成功。

    例如输入： "bo a" ，确定是命令 "board add" ，匹配成功。

5. 若输入两字串，第一关键字匹配成功，则匹配第二关键字，若无匹配，失败。

    例如输入： "b addr" ，无法匹配到相应的命令。

6. 若匹配失败，打印 "unknown command" 。

注意：有多组输入。

数据范围：
    数据组数：1 <= t <= 800
    字符串长度： 1 <= s <= 20

## 进阶

时间复杂度：O(n)
空间复杂度：O(n)

## 输入 & 输出

输入多行字符串，每行字符串一条命令；输出执行结果，每条命令输出一行

## 示例

输入：
    reset
    reset board
    board add
    board delet
    reboot backplane
    backplane abort
输出：
    reset what
    board fault
    where to add
    no board at all
    impossible
    install first
"""
from sys import stdin

COMMANDS = [
    'reset', 'reset board', 'board add', 'board delete', 'reboot backplane',
    'backplane abort'
]
EXEC = [
    'reset what', 'board fault', 'where to add', 'no board at all',
    'impossible', 'install first'
]
DEFAULT = 'unknown command'

for line in stdin:
    command = line.strip().split(' ')
    if len(command) < 1 or len(command) > 2:
        print(DEFAULT)
    elif len(command) == 1:
        if 'reset'.startswith(command[0]):
            print(EXEC[0])
        else:
            print(DEFAULT)
    else:
        matched = []
        for _ in range(1, len(COMMANDS)):
            a, b = COMMANDS[_].split(' ')
            if a.startswith(command[0]) and b.startswith(command[1]):
                matched.append(_)
        print(EXEC[matched[0]] if len(matched) == 1 else DEFAULT)
