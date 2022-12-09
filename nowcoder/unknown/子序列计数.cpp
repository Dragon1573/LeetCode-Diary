/**
 * 题目描述：
 *
 * 读入一个正整数 n ，代表将字符串 "abc" 重复 n 次，形成一个长度为 3n 的字符串、
 * 例如 n = 3 时，形成的字符串为 "abcabcabc" 。
 * 请你计算该字符串中有多少个 "acb" 子序列，答案对 (10^9 + 7) 取模。
 *
 * 输入描述：
 *
 * 一个正整数 n ，其中 1 <= n <= 10^9
 *
 * 输出描述：
 *
 * "acb" 子序列的数量，答案对 (10^9 + 7) 取模。
 *
 * 示例：
 * 
 * 输入：3
 * 输出：4
 * 说明：
 *    abcabcabc
 *    ^ ^ ^
 *    ^ ^    ^
 *    ^    ^ ^
 *       ^ ^ ^
 *    如上以标出4个结果对应的字母位置。
 */
#include <iostream>
using BIGINT = long long;
using namespace std;
const BIGINT modulo = 1000000007;

int main(int argc, char const *argv[]) {
    // 此处 n 不能为 int ，(n * n) > INT_MAX 影响后续计算结果
    BIGINT n;
    cin >> n;

    // 1）a 和 c 可以位于相同循环节；
    // 2）a 和 c 都不能位于最后一个循环节；
    // 3）b 至少位于下一个循环节，可以位于最后一个循环节。
    // 
    // 综上，我们可以获得求和公式：
    //  sum(sum(sum(1, j + 1, n), i, n - 1), 1, n - 1)
    //  = n * (n * n - 1) / 6

    // n <= 10^9 ，因此 (n * n) <= 10^18 < LONG_LONG_MAX ，可以保证不溢出
    BIGINT result = (n * n - 1) % modulo;
    result = (result * n) % modulo;
    // 值在变小，可以不进行取模操作
    result /= 6;

    cout << result << endl;
    return 0;
}
