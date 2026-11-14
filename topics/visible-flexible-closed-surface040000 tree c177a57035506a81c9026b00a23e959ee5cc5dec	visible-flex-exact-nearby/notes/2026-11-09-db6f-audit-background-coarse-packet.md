# 全域粗背景包独立复核

2026-11-09，`/root/independent_geometry`。独立审读并复跑 `scripts/db6f-tail-background-coarse-packet.py`，冻结 SHA256 `0f89d4da2462062903ddf6b282418bf02cd82fc8c8bde311a1962383dcf3385d`。结论为绑定当前正式 source 与 int2 manifest 的粗包 **PASS**。

输入包 `2026-11-09-db6f-tail-background-coarse-int2.json` 的数据 SHA256 为 `3043cf21f9d1e49ae18ae7ea7a08a60f77f59793809c104a8d7942c21abe0cba`。独立复跑另存 `2026-11-09-db6f-audit-tail-background-coarse-rerun.json/.npz`，全部数组逐元素一致，JSON 除输出数据文件名外一致。机器记录见 `2026-11-09-db6f-audit-background-coarse-packet.json`。

包共 4638 行，对应完整 collar 和 4637 个有限扰动 span。物理半径由 manifest 的精确二进节点或归一化增量定义重建。原始 source 与积分证书的 checkpoint、参数以及 manifest 绑定按实际正式输入核对；这不是从数组单点取样建立的范围。

对同一 source 的 cell 0，独立以 Fraction 计算

$$
r_{0,\mathrm{inner}}
\ge c-\sum_j A_{0j}^{upper}
-\alpha^{upper}\sum_j B_{0j}^{upper}.
$$

所得下界确实包含脚本使用的保守阈值 0.30112385996418195。脚本仅将**整个物理 span 的上端点**位于该阈值之内的 4057 行分类为内段；含糊或越界的盒归入更宽的全域界。因此不会因边界归属误差把 raw 0 当作恒定 cap 内段。

内段的有限 cap 不超过 1/49；深于有限保护端的无限 source 由已审 R15 raw 界覆盖。结合已交叉审查的完整背景主曲率界 6，有

$$
|w_r|\le6(1+w^2)^{3/2}
\le6(1+1/49^2)^{3/2}<6.01.
$$

最后不等式另在 Fraction 上平方比较，且对实现实际使用的二进 6.01 仍严格成立。内盒采用 $w\in[0,1/49]$ 向外端点和 $w_r\in[-6.01,6.01]$；其余 581 行采用已审全域界 $w\in[0,16/15]$、$w_r\in[-24,24]$。

计算 source 端点的 `strong_profile_anchors` 模块冻结 SHA256 `9eb20eb44bb202e1dec3df55493ff2ba149b5dc96b340ddf5c5781b46bd65d23`，已由 root 另外审读和复跑；本次独立 Fraction 计算直接复核了粗包所需的单个阈值，未借用该模块的数值结果作为唯一依据。

这些界很宽，但它们包围同一个精确背景，不改变目标 g。只有把它们与有限扰动的连续系数计算结合，才能判断哪些段已经满足所需 metric 或实际曲率预算。本次审查不声称完整尾 metric 或实际曲率阈值已通过。
