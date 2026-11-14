# R195 补充：实际浮点支撑的四块外带与显式可变带宽

本补充保留原 three-band 源及其 193 维真实报告。新内核 scripts/fd2d_scaled_band_border_lm_v2_R195.cjs 只将半带宽改成明确非负整数参数 halfBandwidthBlocks，默认仍为 3。字段、目标、列尺度、阻尼和实际试步规则没有变化。

## 实际触发原因与保留策略

root 在实际 J27/K7 的 433 维 coupled normal 上调用原内核，得到带外非零拒绝，没有产生方向或试步。随后 root 在同一份已保存 normal 定位到 256 个下三角非零，全部在径向 block distance=4；最大绝对值为 $7.619951433203412\times10^{-31}$。首项 original(28,0)、blocks(4,0) 为 $2.0840753370271356\times10^{-31}$。

连续支撑上的相接端点可以在 binary64 center/h/physical-knot 计算中出现极小非零细尾。它们是实际有限 Jacobian 的一部分。新内核不以量级为由删除，而由该分支明确选择 width=4；所有更远的非零仍必须拒绝。数学 exact active≤4 的论证与浮点实现实际 active 项分开记录。

这些 433 数字来自 root 对其已保存 normal 的真实消费消息，完整实际 checkpoint/report 由 root 闭存。本 agent 没有重组这份 433 normal 或重跑其试步。

## 任意整数带宽的完整等价推论

R195 的证明只用了带外零的条件。对任何明确整数 $w\ge0$，假设实际工作矩阵在径向块上满足
$$
A_{ij}=0\quad (|i-j|>w).
$$
当 $i-j>w$ 时，对每个已消去的 $k<j$，都有 $i-k>w$。Cholesky 归纳给 $L_{ik}=0$，故同一递推给 $L_{ij}=0$。因此因子保持 $w$ 块半带宽。每个 scalar row 的开始、结束和 stride 分别变成
$$
\max(0,(\lfloor i/b\rfloor-w)b),\qquad
\min(m,(\lfloor i/b\rfloor+w+1)b),\qquad (w+1)b.
$$
前代、回代、工作矩阵乘法、未平均原矩阵残差全使用同一个 $w$。单 border 的两 RHS/Schur 公式完全不变。因此这仍是同一个完整 SPD 系统的求解，不是截断或改目标。

存储为 $O(J(w+1)b^2)$，分解为 $O(J(w+1)^2b^3)$。对于固定小 $w$ 仍随径向块数线性增长。原 dense 输入检查仍存在。

## API

~~~javascript
const prepared = v2.prepareBandBorderNormal(normal, definition, {
  halfBandwidthBlocks: 4
});
const result = v2.solvePreparedBandBorder(prepared, lambda);
~~~

便捷 solveDampedNormal 也接同字段。默认 width3，非整数/负数直接拒绝。任何超出已选带宽的实际非零——无论多小——都被拒绝。

scripts/fd2d_band_border_lm_adapter_v2_R195.cjs 提供同原 policy 的
~~~javascript
const lm = createBandBorderLM(kernel, definition, {
  halfBandwidthBlocks: 4,
  kernelSourceSHA256: actualKernelSHA
});
~~~
第三参只传给 prepare 并保 metadata。evaluationNorm/lmStep/runLM 的实际 value、异常处理、全部 trial trace 和阻尼更新保持原文本。它不冒传入 wrapper 就是旧 kernel；未提供实际 SHA 则记 null，旧 SHA 只标 ancestor。R198 packed backend 还可提供自己的 implementationDefinition。

## 已付有限消费

本 agent 复用原 193 normal，只作 width4 与已保存 width3 的方向比较，所有方向分量差准确为 0，无新 F/J/normal。root 随后复用已有 433 normal，在 $\lambda=.001$ 上实际完成：

- 方向最大差 $2.0458894994801469\times10^{-16}$；
- 相对 L2 $2.940387739108767\times10^{-14}$；
- 预测平方范数差 $1.0164395367051604\times10^{-20}$；
- 原缩放方程最大残差 $3.496552006265752\times10^{-18}$；
- 全部 distance4 项保留。

root 的单次 prepare+solve 为175ms、dense1298ms，仅记录这一次真实耗时，不称完整 benchmark。此补充不声明新的连续几何证书，也不修改原 three-band 闭组。
