"""
# HJ54 - 表达式求值

时间限制：C/C++ 1秒，其他 2秒
空间限制：C/C++ 32MB ，其他 64MB

## 描述

给定一个字符串描述的表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 '+-*/()' 和 '0-9' 。

数据范围：运算过程中和最终结果均满足 |val| <= 2^{31} - 1 ，
即只进行整型运算，确保输入的表达式合法。

## 示例

输入：400+5
输出：405
"""
from typing import List

MP = '+-*/)'


def compare(x: str, y: str) -> bool:
    """ 比较运算符 """
    if x == '(':
        # 栈顶是开括号，后续运算提升优先级，直接压栈
        return False
    elif x in ['+', '-'] and y in ['*', '/']:
        # 当前优先级高于栈顶，直接压栈
        return False
    # 否则触发一次计算
    return True


def calculate(nums: List[int], ops: List[str]) -> None:
    """ 逆波兰表达式的计算 """
    b = nums.pop()
    a = nums.pop()
    o = ops.pop()
    if o == '+':
        a += b
    elif o == '-':
        a -= b
    elif o == '*':
        a *= b
    elif o == '/':
        a //= b
    nums.append(a)
    pass


if __name__ == "__main__":
    # 输入表达式
    expression = input()
    num_stack, op_stack = [], []
    # 在符号栈底层补开括号
    op_stack.append('(')
    # 在表达式末尾补闭括号，触发一次最终计算
    expression += ')'
    # 用来记录下一个符号是一元运算符（负号）还是二元运算符
    isBinary = False
    """ 遍历表达式 """
    _ = 0
    while _ < len(expression):
        if expression[_] == '(':
            # 遇到开括号直接压栈
            op_stack.append('(')
        elif expression[_] == ')':
            # 遇到闭括号
            while op_stack[-1] != '(':
                # 持续处理计算，直到括号内的表达式计算完毕
                calculate(num_stack, op_stack)
            # 移除开括号
            op_stack.pop()
        elif isBinary:
            # 当前是二元运算符
            while compare(op_stack[-1], expression[_]):
                # 比较当前与栈顶运算符的优先级，确定是否执行计算
                calculate(num_stack, op_stack)
            # 当前运算符压栈，等待后续计算
            op_stack.append(expression[_])
            # 表达式片段结束，后续可能会出现一元运算符
            isBinary = False
        else:
            j = _
            if expression[j] in ['+', '-']:
                # 当前是一元运算符，跳过此位置
                _ += 1
            while expression[_] not in list(MP):
                # 持续寻找下一个运算符的位置
                _ += 1
            # 将中间这部分转换为数值进行压栈
            t = expression[j:_]
            num_stack.append(int(t))
            # 回退到运算符前的数字位，防止后面重复移位
            _ -= 1
            # 后续运算符是一个二元运算符
            isBinary = True
        # 处理下一个字符
        _ += 1
    # 表达式扫描完毕，最终数值栈顶元素为表达式的计算结果
    print(num_stack[-1])
    pass
