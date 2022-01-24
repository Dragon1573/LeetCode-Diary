""" HJ74 - 参数解析

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

在命令行输入如下命令：

    xcopy /s c:\\ d:\\e，

各个参数如下：

    参数1：命令字 'xcopy'
    参数2：字符串 '/s'
    参数3：字符串 'c:\\'
    参数4: 字符串 'd:\\e'

请编写一个参数解析程序，实现将命令行各个参数解析出来。

解析规则：

1. 参数分隔符为空格；
2. 对于用 "" 包含起来的参数，如果中间有空格，不能解析为多个参数；

    比如在命令行输入 xcopy /s "C:\\program files" "d:\" 时，参数仍然是4个，
    第3个参数应该是字符串 C:\\program files ，而不是 C:\\program，
    注意输出参数时，需要将 "" 去掉，引号不存在嵌套情况。

3. 参数不定长；
4. 输入由用例保证，不会出现不符合要求的输入。

数据范围：字符串长度 1 <= s <= 1000
进阶：线性时间 & 空间复杂度

## 示例

输入：xcopy /s c:\\ d:\\e
输出：
    4
    xcopy
    /s
    c:\\
    d:\\e
"""
if __name__ == '__main__':
    commands = input().split(' ')
    array = []
    inBrackets = False
    for _ in commands:
        if _.startswith('"') and _.endswith('"'):
            array.append(_[1:-1])
        elif _.startswith('"'):
            inBrackets = True
            array.append(_[1:])
        elif _.endswith('"'):
            inBrackets = False
            array[-1] += ' ' + _[:-1]
        elif inBrackets:
            array[-1] += ' ' + _
        else:
            array.append(_)
    print(len(array), *array, sep='\n')
