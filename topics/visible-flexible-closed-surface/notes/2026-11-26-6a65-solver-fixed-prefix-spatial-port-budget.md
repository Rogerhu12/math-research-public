# 固定 prefix 后的非正交空间端口长度预算

2026-11-26，Astra-visible-flex-6a65 / resume_solver。

本文把既有 [R212](../results/R212-spatial-meridian-length-bound-without-reflection.md) 的正交端切向必要式用于当前更晚固定的 prefix 端口。新端切向不再准确正交，所以使用 [R238](../results/R238-nonorthogonal-spatial-port-length-bound.md) 已证明的任意夹角投影积分式，再代入 geometry agent 已有的四轴端口；不重新计算源、value、normal 或 LM。完整解析证明见 R238；以下浮点代入只是有限诊断，不称作源的区间证书。

**当前结论：** gap 1.05 的新 source 从固定点 $b=.1815625$ 到真实 cut $S=.9772364498716914$，自由区间自身长 $L=S-b=.7956739498716915$。长轴的曲率半径 .097 必要长度约为 .755356，仍有 .040318 余量；更紧的 9.5 曲率 guide 给 .757579，余量 .038095。本次检查没有排除该输入。不能再把 .795674 当作 $S-c$ 后额外扣除 $b-c=.08$：它本来就是 $S-b$。

## 1. 本次真实端口与有限代入

输入来自已封存 source cache，不是新数学接受态。其
sourceDefinitionSHA256 为
1b3b539ace7a1fdb5b7af3fd4a62100a376e64ec9462b4c501fed64efa600fbd；
端口 JSON SHA-256 为
7755e0a252dc1159b0fd0897b1dded7baf382db0107bc93c32b975af93522116。

长轴 $u=0$ 的实际输入为

$$
\begin{aligned}
P_0&\simeq(1.453478927449583,\,-3.25527\cdot10^{-15},\,.18156193558245665),\\
T_0^{\rm raw}&\simeq(.005017514313456809,\,-8.06243\cdot10^{-16},\,.9999874121958306),\\
P_1&\simeq(.8000000000000004,\,-4.63171\cdot10^{-17},\,.5100000000000001),\\
T_1^{\rm raw}&\simeq(-1.0000000000000004,\,8.88676\cdot10^{-17},\,-4.44089\cdot10^{-16}).
\end{aligned}
$$

脚本使用 JSON 的全部实际浮点位，将端切向正规化；两端原速度平方误差分别为
$-1.1102230246251565\cdot10^{-16}$ 和
$8.881784197001252\cdot10^{-16}$。长轴弦长
.7313728671334473，$w$ 离端切向平面的剩余量约 $3.42\cdot10^{-15}$；
没有把该浮点小量声明为严格零。

| 材料轴 | 假设曲率上界 | 本次必要下界的最大值 | $S-b$ 减该值 |
| --- | ---: | ---: | ---: |
| $u=0,\pi$ | $1/.097$ | .7553559685907328 | .04031798128095865 |
| $u=0,\pi$ | 9.5 | .7575790869256123 | .03809486294607922 |
| $u=\pi/2,3\pi/2$ | $1/.097$ | .4438231074398133 | .3518508424318782 |
| $u=\pi/2,3\pi/2$ | 9.5 | .4519426196056965 | .34373133026599495 |

长轴采用 R238 式 (2)；侧轴表中较强的是用弦方向作 $v$ 的 R238 式 (1)，其非重叠条件在报告中逐项实际核实。不是对整个单位球面优化后的全局最强预算。结果只是这些条件未排除所给端口；不能反向推得完整 $g$ 的兼容、$C^2$ BVP、全域嵌入或 reach。

## 2. 可复算文件与实际退出

脚本 scripts/6a65-fixed-prefix-spatial-port-budget.py：
4850 bytes，SHA-256
7d67243fc3c20408570b5e74dd41d4071224dd0691508f4afb829ec220d0d4dc。

本次命令：

    python /tmp/visible-flex-6a65e705/solver-work/recovered-sources/6a65-fixed-prefix-spatial-port-budget.py \
      --ports /tmp/visible-flex-6a65e705/geometry-work/gap105-window-fixed-ports-budget01.json \
      --out /tmp/visible-flex-6a65e705/solver-work/gap105-prefix-port-budget01.json

真实 OS exit 0。输出报告 SHA-256：
2934f9c5f175448552411b705a3cfa828142552737ddecbd48e61b99fb0a509c。
报告保留四个端口的数值预算、两种条件性曲率数值、投影选择、两种等价公式的一致性检查和所有适用范围标记。输入只有几个端口标量，不读取或发布 source 的大数组。

无新 source 重建、完整 value、normal、trial 或接受；没有重复 R212 的旧排除区间。这个核查支持继续当前固定 prefix 的新分支，并明确应使用的真实自由长度。

