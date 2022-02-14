""" HJ64 - MP3光标位置

# 描述

MP3 Player 因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，用户要通过上下
键才能浏览所有的歌曲。为了简化处理，假设每屏只能显示4首歌曲，光标初始的位置为第
1首歌。

现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：

- 歌曲总数 n <= 4 的时候，不需要翻页，只是挪动光标位置。
- 光标在第一首歌曲上时，按 Up 键光标挪到最后一首歌曲；光标在最后一首歌曲时，按
  Down 键光标挪到第一首歌曲。其他情况下用户按Up键，光标挪到上一首歌曲；用户按
  Down 键，光标挪到下一首歌曲。

特殊翻页：屏幕显示的是第一页（即显示第 1–4 首）时，光标在第一首歌曲上，用户按
Up
键后，屏幕要显示最后一页（即显示第7-10首歌），同时光标放到最后一首歌上。同样的，
屏幕显示最后一页时，光标在最后一首歌曲上，用户按 Down 键，屏幕要显示第一页，光标
挪到第一首歌上。

一般翻页：屏幕显示的不是第一页时，光标在当前屏幕显示的第一首歌曲时，用户按 Up 键
后，屏幕从当前歌曲的上一首开始显示，光标也挪到上一首歌曲。光标当前屏幕的最后一首
歌时的 Down 键处理也类似。

其他情况，不用翻页，只是挪动光标就行。

# 数据范围

本题含有多组输入数据，数据组数 1 <= t <= 5 ，命令长度 1 <= s <= 100 ，歌曲数量 1
<= n <= 150

# 进阶

线性的时间复杂度和空间复杂度。

# 输入描述

每组输入占2行，首行为歌曲数量，其次是操作命令 U/D 。

# 输出描述

每组输出占2行，首行输出当前列表，其次输出当前选中歌曲

# 示例

输入：10
      UUUU
输出：7 8 9 10
      7
"""
from collections import deque

try:
    while True:
        n = int(input())
        commands = input().strip()
        
        if n <= 4:
            move = (commands.count('D') - commands.count('U')) % n
            print(*range(1, n + 1))
            print((n - move) % n + 1)
        else:
            array = deque([1, 2, 3, 4])
            index = 0
            for _ in commands:
                if _ == 'U':
                    if array[0] == 1 and index == 0:
                        array.clear()
                        array.extend(range(n - 3, n + 1))
                        index = 3
                    elif index == 0:
                        array.pop()
                        array.appendleft(array[0] - 1)
                    else:
                        index -= 1
                elif _ == 'D':
                    if array[-1] == n and index == 3:
                        array.clear()
                        array.extend(range(1, 5))
                        index = 0
                    elif index == 3:
                        array.popleft()
                        array.append(array[-1] + 1)
                    else:
                        index += 1
            print(*array)
            print(array[index])
except Exception as e:
    pass      
