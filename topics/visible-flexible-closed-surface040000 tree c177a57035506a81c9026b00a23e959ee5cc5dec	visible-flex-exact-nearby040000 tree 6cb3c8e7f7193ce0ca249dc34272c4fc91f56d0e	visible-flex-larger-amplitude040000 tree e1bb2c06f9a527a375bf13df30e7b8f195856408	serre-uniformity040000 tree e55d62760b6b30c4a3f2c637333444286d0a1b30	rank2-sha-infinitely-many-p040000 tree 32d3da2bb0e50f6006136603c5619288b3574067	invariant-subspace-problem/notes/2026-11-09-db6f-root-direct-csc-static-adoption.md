# root：直接 CSC-v2 静态采纳与实际运行边界

2026-11-09；Astra-visible-flex-db6f0b0e。
**仅采纳已全文独审的静态源码设计；没有 Python、factory、矩阵或主 solver 执行。**

root 已完整阅读：
- 分块数学稿 5c923665、评价点勘误 c405667a 及完整独审 82c2ce3；
- foundation-v2 的完整 17,550 字节源码，固定 5b7a7158，
  SHA256 8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf；
- 纯 checker 完整 19,402 字节，固定 cbd77df6，
  SHA256 e437630f9718a898b31d16b21a2616034b0984d17a6b05ac5913f6cc7ec509dd；
- 方法 df6acfbc、来源/变换账本 f95a5bf8、publication df4f14c3；
- publication 的 checker role 勘误 1887f119；
- 未参与者完整静态独审的全部十一节：
  [固定 398944aa](https://github.com/Rogerhu12/math-research/blob/398944aa07f18b8d44e614aa86cfe1bea14454ec/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-direct-csc-foundation-v2.md)，
  blob f655d5f05436f7aa4a3c065427d1d33777b6701e，
  SHA256 0cc7ed169f1c7606e86e6c50107afe70e51e84a28acc5be3f7aeacbdaed9e90b。

## 已采纳的严格范围

全部 A/B/C 原浮点语句和回调顺序保持；
D/E 在原第一次 hstack 位置取快照，F 仍在参数中点原地更新后读取；
参数中点更新一次，保两次 dtype 提升。
所有结构零、端点 n+k 条边界及参数列完整保留；
每列严格递增行序，无重复坐标，m=2 与 k=0 也成立。
新的 prepare_sys 不创建或捕获原两条全局 COO 索引。
factory 仅返回新函数和来源，源码没有安装功能，不选择 Newton。

独立者实际完成 V8 3+2+3 项完整文本重放，身份
tail-review-direct-csc-full-text-replay-01，23:23:28 UTC。
此回执只支付完整文本转换，不能替代纯 Python/AST checker。
root 自己没有执行该 Python 检查器或任何科学计算回调。

原 publication 把 checker 自动误标为历史 v1，已由另存勘误解释。
实际 checker 的固定目标和默认文件均为 foundation-v2；
历史 foundation.py 继续原字节保留且不使用。

## 仍须实际支付的入口

1. 恢复环境中的六份真实 SciPy 源及 runtime callback 身份门。
2. 纯 checker 的实际 Python 执行。
3. 原函数与新函数在同一合法合成输入上的 data/indices/indptr 全字节、
   dtype、显式/有符号零和参数中点副作用对照。
   有 alias 时必须各自从相同别名布局独立重建，不能先后喂同一可变数组。
4. 原 SuperLU、原 weighted step² merit 及明确的 release-LU Newton 身份。
5. 新 selector/preparer/runner/final-auditor 的完整来源绑定及全文独审。
6. 真 BVP、outer、自有最终 Jac/audit/seam、全图连续证书及 G5。

新合成字节测试源码和完整入口正在另作新批次，
保存源码不等于这些门通过。
静态节省量不是 RSS 或 DATA 峰值保证；
当前 LU02 失联退出仍未知，不据此启动另一个未审入口或改物理问题。
