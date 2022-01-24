""" HJ85 - 最长回文子串（Manacher 算法） """


def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return (right - left - 2) // 2


def longestPalindrome(s: str) -> str:
    end, start = -1, 0
    s = '#' + '#'.join(list(s)) + '#'
    arm_len = []
    right = -1
    j = -1
    for i in range(len(s)):
        if right >= i:
            i_sym = 2 * j - i
            min_arm_len = min(arm_len[i_sym], right - i)
            cur_arm_len = expand(s, i - min_arm_len, i + min_arm_len)
        else:
            cur_arm_len = expand(s, i, i)
        arm_len.append(cur_arm_len)
        if i + cur_arm_len > right:
            j = i
            right = i + cur_arm_len
        if 2 * cur_arm_len + 1 > end - start:
            start = i - cur_arm_len
            end = i + cur_arm_len
    return s[start + 1:end + 1:2]


if __name__ == "__main__":
    print(len(longestPalindrome(input())))
