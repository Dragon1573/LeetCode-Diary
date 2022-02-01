/* HJ34 - 图片整理
 *
 * https://www.nowcoder.com/practice/2de4127fda5e46858aa85d254af43941
 * https://blog.csdn.net/zhengqijun_/article/details/53038831
 */
#include <stdio.h>
#include <string.h>

void qsort(char *string, int low, int high) {
    // 快速排序
    if (low < high) {
        int i = low, j = high, k = string[low];
        while (i < j) {
            while (i < j && string[j] >= k) j--;
            if (i < j) string[i++] = string[j];
            while (i < j && string[i] < k) i++;
            if (i < j) string[j--] = string[i];
        }
        string[i] = k;
        qsort(string, low, i - 1);
        qsort(string, i + 1, high);
    }
}

int main(int argc, const char *argv[]) {
    char string[1001];
    while (scanf("%s", string) > 0) {
        qsort(string, 0, strlen(string) - 1);
        printf("%s\n", string);
    }
    return 0;
}
