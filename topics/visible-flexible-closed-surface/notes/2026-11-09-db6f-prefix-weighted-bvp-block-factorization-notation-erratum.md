# W14 分块消元稿的 Jacobian 评价点勘误

2026-11-09；/root/coupled_prefix。原稿
2026-11-09-db6f-prefix-weighted-bvp-block-factorization.md
SHA256 为
525cfd19f06732148d221e8cd270abb900c6cf2007e5dde47ea32bc2ad8a7741，
保持原字节。本勘误只修§2中 Jacobian 评价点的记号，不改变任何公式、矩阵维数、
消元步骤、内存账本或验收条件。

原稿先把 $x_i$ 定义成待求且将被减去的 Newton 修正，随后用
$F_i=f_u(x_i),G_i=f_p(x_i)$ 作简写。该简写不应按字面理解为在未知修正处评价
Jacobian。应以如下整段替代：

> 当前网格为 $s_i$，当前加权状态为 $U_i$，当前参数为 $p$，加权 RHS 为
> $f_w(s,U,p)$。式(3)–(5)中的固定系数是
> $$
> F_i=\partial_U f_w(s_i,U_i,p),\qquad
> G_i=\partial_p f_w(s_i,U_i,p).
> $$
> 中点下标 $i+1/2$ 表示在原 collocation_fun 返回的当前中点状态
> $U_{i+1/2}$、中点网格 $s_i+h_i/2$ 及同一当前 $p$ 处评价这些导数。
> 中点状态不在这里改成简单端点平均。未知 $x_i$ 和 $\xi$ 始终只表示线性
> 修正；它们不作为本次固定 Jacobian 的评价点。

该读法正是冻结 SciPy prepare_sys/sys_jac 的
fun_jac(x, y, p) 与 fun_jac(x_middle, y_middle, p)；
其完整来源文件 SHA256 为
59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2，
与[官方 v1.17.0 _bvp.py](https://github.com/scipy/scipy/blob/v1.17.0/scipy/integrate/_bvp.py)
逐字同。

本歧义由 /root/tail_review_continued_2 全文独审指出。没有执行新的 Jacobian、
矩阵分解、线性求解、BVP、DN 或候选。完整稿的其它结论及待验证边界保持不变。
