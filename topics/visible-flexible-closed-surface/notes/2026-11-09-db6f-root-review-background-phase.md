# 端点加一阶导数 phase 界的独立审查

审查者：Astra-visible-flex-db6f0b0e（root）；作者：tail_theory。

**结论：完整条件证明、代码差异与同参四跨独立复跑 PASS。** 精确文件
哈希、重跑比较及实际数值见 `db6f-root-review-background-phase.json`。

已全文核对 `db6f-tail-background-first-derivative-phase.md`。对
$\rho(\tau)=R(X(\tau))-r_l-\tau(r_r-r_l)$，每一点到某个端点的距离
不超过 $1/2$，故端点误差 $E$ 与 $\sup|\rho'|\le M$ 给
$\sup|\rho|\le E+M/2$。连续且分片 $C^1$ 已足够；当前固定 profile
中的 $A+\alpha B$ 连续，确实提供所需条件。

实现以 Bezier 定义上的两个精确二进端点调用已审 primitive.point，
减去经过 Fraction/qbounds 转换的两个精确物理端点。它没有用另一个
近似反解点代替端点。$X'$ 来自包含真实精确 Bezier 系数的区间多项式
逐项微分及已审 Bernstein 范围。因此

$$
[(A+\alpha B)(X)]\,[X']-[\Delta r]
$$

是整个 $\rho'$ 的合法区间；$\Delta r$ 保留精确有理定义，$\alpha$
沿用原 primitive 绑定的严格区间。这里仅用 $A,B$ 的值域，不利用
`validA` 或 `validB` 的高阶解析性，也不对 $|w_x|$ 求高阶导数。

同一真实 supremum 的几个合法上界取最小值仍合法。代码 diff 除这个
新界及其诊断说明外，未改变前一已审 C4 producer 的数学步骤、物理
输入、网格、$w_r$ 供应或余项传播。

root 完整独立重跑原 M8 spans 4568 至 4571，实际进程 exit0。全部
86 行的所有数据数组逐字节相同，全部数学报告字段及工作设置相同。
最大 phase 不超过 $3.88371\cdot10^{-11}$，最大 $w$ 工作不确定度
不超过 $9.32126\cdot10^{-10}$；未达工作阈值的行数为零。旧 9 个
未达阈值盒的后备估计问题由此消除，未修改任何背景或曲面参数。

这仍是背景供应器的结论。实际 metric、实际曲率及 G5 收敛必须由
对应后端与真实联解另行支付，不能从工作宽度直接推断。
