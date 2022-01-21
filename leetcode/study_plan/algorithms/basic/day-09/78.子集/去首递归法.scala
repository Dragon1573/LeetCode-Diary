/*
 * @lc app=leetcode.cn id=78 lang=scala
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (80.27%)
 * Likes:    1451
 * Dislikes: 0
 * Total Accepted:    358.1K
 * Total Submissions: 446.1K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 *
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0]
 * 输出：[[],[0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10
 * -10 <= nums[i] <= 10
 * nums 中的所有元素 互不相同
 *
 *
 */

// @lc code=start
object Solution {
  def subsets(nums: Array[Int]): List[List[Int]] = {
    nums match {
      case Array() => List(List())
      case _ =>
        val temp = subsets(nums.tail)
        temp ::: temp.map(List(nums.head) ::: _)
    }
  }
}
// @lc code=end
