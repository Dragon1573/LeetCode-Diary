from typing import List


d = {
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 1,
    '2': 2
}


def hack_24(nums: List[str], target: int) -> bool:
    if len(nums) == 1:
        if d[nums[0]] == target:
            res.append(nums[0])
            return True
        else:
            return False
    for i in range(len(nums)):
        a = nums[i]
        b = nums[:i] + nums[i + 1:]
        if hack_24(b, target + d[a]):
            res.append('-' + a)
            return True
        elif hack_24(b, target - d[a]):
            res.append('+' + a)
            return True
        elif hack_24(b, target * d[a]):
            res.append('/' + a)
            return True
        elif target % d[a] == 0 and hack_24(b, target // d[a]):
            res.append('*' + a)
            return True
    return False


while True:
    try:
        nums = input().strip().split()
        if 'joker' in nums or 'JOKER' in nums:
            print('ERROR')
        else:
            res = []
            if hack_24(nums, 24):
                print(''.join(res))
            else:
                print('NONE')
    except Exception:
        break
