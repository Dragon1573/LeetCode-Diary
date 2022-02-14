/* HJ57 - 高精度整数加法
 *
 * https://www.nowcoder.com/practice/49e772ab08994a96980f9618892e55b6
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    while (1) {
        /* 开始：数据输入 */
        char stringA[10001], stringB[10001], result[10002];
        if (scanf("%s", stringA) == EOF) {
            break;
        }
        scanf("%s", stringB);
        /* 结束：数据输入 */

        /* 开始：竖式计算 */
        int n = strlen(stringA), m = strlen(stringB);
        // 操作数从右往左累加，结果从左向右保存（倒序）
        int i = n - 1, j = m - 1, k = 0, flag = 0;
        while (i >= 0 && j >= 0) {
            // 对应位相加，保存进位
            int temp = (stringA[i--] + stringB[j--] - 2 * '0') + flag;
            result[k++] = (temp % 10) + '0';
            flag = temp / 10;
        }
        while (i >= 0) {
            // 前操作数更长，处理剩下多出来的数位
            int temp = stringA[i--] - '0' + flag;
            result[k++] = (temp % 10) + '0';
            flag = temp / 10;
        }
        while (j >= 0) {
            // 后操作数也一样
            int temp = stringB[j--] - '0' + flag;
            result[k++] = (temp % 10) + '0';
            flag = temp / 10;
        }
        if (flag) {
            // 如果仍有进位，则额外添加一位数
            result[k++] = '0' + flag;
        }
        while (k > 0) {
            // 逆序输出结果（将结果字符串翻正）
            printf("%c", result[(k--) - 1]);
        }
        printf("\n");
    }
}
