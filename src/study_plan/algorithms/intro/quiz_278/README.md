# 第278题 - 第一个错误的版本

![难度：简单](https://img.shields.io/badge/%E9%9A%BE%E5%BA%A6-%E7%AE%80%E5%8D%95-blue)
[![来源：LeetCode](https://img.shields.io/badge/来源-LeetCode_No.704-blue)](https://leetcode-cn.com/problems/first-bad-version)

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 `n` 个版本 `[1, 2, ..., n]` ，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 `isBadVersion(version: int) -> bool` 接口来判断版本号 `version` 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 `API` 的次数。

## 提示

- $1 \le \text{bad} \le n \le 2^{31} - 1$
