# 当前 M15 首响应在 cut 的高模二 jet：一次局部诊断

状态：**实际浮点数值证据。** 使用当前 M15/W15/N512 的首个真实尾响应，只在其外端点做 raw 几何嵌入及一次局部高模 root/ODE 评价。没有 shooting、prefix BVP、径向积分或新的 DN 求解；没有修改任何保存候选、参数或共同度量。本笔记不把所算的局部 W22 状态称为 W22 真 DN 端点。

作者：Astra-visible-flex-78718bd0，`/root/geometric_closure`，2026-11-10。

## 1. 需要回答的具体问题

R85 已把当前尾部的大 metric 峰定位到内部 $r\simeq0.435$，而公共接缝位于 $r_c=0.6$。前缀 M 与尾部 W 分开的真实接口见 [M/W 接口说明](2026-11-10-78718-geometry-prefix-tail-mode-split-interface.md)，其完整接缝预算为 [R87](../results/R87-common-cut-high-jet-metric-budget.md)。内部高模残差大，并不自动说明外端点的高模二 jet 也大；反过来，外端点局部量小也不控制真实 DN 对内部扰动的非局部响应。

本次只计算一个有用的预测量：将原 cut 的完整高度一 jet 按 R86 的几何方式嵌入 W22 后，新的局部有限 ODE 要求多少高模高度二阶导数。它也比较同一状态的实际周期发展位置及径向一阶导数。

## 2. 精确坐标转换与高度系数公式

输入是 `2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz`，272525 B，SHA256

`a88f0a8eaff38a6fca9576550ef04d538c8b8d1fe55715df6d0439f27801c919`。

它是当前活动主计算的第一个真正 N512 尾响应，尚不是完成 outer 后的最终候选。使用其 `checkpoint.states[0]`，对应第一个 subdivision cell 的最后 profile、局部 $x=1$，即 rawCell0/rawSegment8/part7 的外端点。保存的节点动量须先乘该 cell 的 `portRatio`；本次实际倍率约为 $6.727171322029716$。未把节点动量直接当成局部 profile 动量。

令旧空间的普通余弦高度状态为 $Q_j$，角 root 的正交余弦系数为 $L_j$，角频率 $k_j=3j$。记

$$
\sigma=\frac{r_x}{r},\qquad k=(\log w)_x,
\qquad \dot Q_j=\frac{dQ_j}{dx},\quad
\dot L_j=\frac{dL_j}{dx}.
$$

从同一个 root 和实际有限动量 ODE 得到的普通余弦高度三项系数是

$$
\begin{aligned}
H_j&=r^4Q_j,\\
S_j&=\sqrt2\,w L_j+k_j^2r^3Q_j,\\
B_j&=\frac{\sqrt2\,w}{r_x}(kL_j+\dot L_j)
 +\frac{k_j^2r^3}{r_x}(\dot Q_j+3\sigma Q_j).
\end{aligned}
\tag{1}
$$

这里 $H_j,S_j,B_j$ 分别是 $u,u_r,u_{rr}$ 的非均值系数。均值为

$$
\overline{u_r}=w(1+L_0),\qquad
\overline{u_{rr}}=\frac{w}{r_x}\{k(1+L_0)+\dot L_0\}.
\tag{2}
$$

证明：(1) 第一式来自实际高度变量定义。第二式来自 $u_r=w(1+K)$、$K=L-P_\theta$ 和 $P$ 的系数 $-k_jr^3Q_j/(\sqrt2 w)$。对第二式逐项取 $r$ 导数，使用 $d/dr=r_x^{-1}d/dx$，即得第三式；均值同理。`createMomentumPhysicalJetEvaluator` 通过对同一个非线性角 root 隐式求导计算 $\dot L$，所以这里没有混用另一组诊断演化。

新状态按以下顺序生成：旧 engine `toRaw` 得到 $Q/L$ 坐标；只给新 $Q_j,L_j$ 补零；再调用新 engine `initializeFromRaw`，重新生成所有动量。N 不变时，这由 R86 的数学恒等式保留高度与径向高度一 jet；新的 $\dot L_j$、从而新的 $B_j$ 一般不为零。N 改变时只比较实际重新求均值后的结果，不宣称跨求积网格严格相等。

位置与径向导数比较使用 R85 的实际周期发展公式，而不把理想标架指定成一个曲面的导数。没有计算完整 XYZ 的二阶导数，亦没有使用未导出的高模状态代替最终 common-cut 自己的 `cut_delta`。

## 3. 实际结果

输入 profile 的浮点值为 $r=0.6$、$w=0.5000000000000018$；它们来自保存物理源的评价。本表是普通双精度诊断，数值不是区间证书。

| 同一 cut 的几何嵌入 | W22/N512 | W22/N1024 |
|---|---:|---:|
| 新 $48,51,\ldots,66$ 高度系数绝对和 | 0 | 0 |
| 新高模 $u_r$ 系数绝对和 | $6.66\cdot10^{-21}$ | $4.53\cdot10^{-21}$ |
| 新高模 $u_{rr}$ 系数绝对和 | $1.0003341\cdot10^{-12}$ | $1.0003061\cdot10^{-12}$ |
| 全部 $u_{rr}$ 系数变化绝对和 | $1.0007899\cdot10^{-12}$ | $1.0013197\cdot10^{-12}$ |
| 共同角点的 $u_r$ 最大差 | $5.55\cdot10^{-17}$ | $5.55\cdot10^{-17}$ |
| 共同角点的周期发展径向导数最大差 | $3.48\cdot10^{-16}$ | $1.14\cdot10^{-15}$ |
| 局部实际 metric 算子误差 | $1.04\cdot10^{-15}$ | $1.46\cdot10^{-15}$ |

原 W15/N512 cut 的局部 metric 为约 $1.23\cdot10^{-15}$。其非均值 $H,S,B$ 的系数绝对和分别约 $8.09259\cdot10^{-4}$、$8.70840\cdot10^{-3}$、$4.36140\cdot10^{-2}$。所以表中的高模二阶变化远小于原来的全二阶大小。

由 (1) 重构逐角 $u_{rr}$ 与原物理 jet evaluator 的差约 $3.6$ 至 $4.4\cdot10^{-15}$。这只是本次公式与源的实际浮点一致性量，不用于把 $10^{-12}$ 的表值升级为严格上界。

## 4. 对当前计算的意义与未支付部分

此处支持一个有限而具体的判断：当前首响应的内部遗漏频率峰，没有伴随 cut 处很大的**局部**新增高度二阶强迫。保留 M15 prefix、真正求 W22 tail 的方案仍值得实际尝试；无需仅由内部峰就预先判定接缝修正必然过大。

不过新的 DN 必须满足整个径向边值问题。内部高模响应可能改变 cut 的低、高模坡度、均值和位置；本次保持一 jet 的 warm 嵌入没有计算这种响应，也没有给其上界。真实 W22 输出后仍应直接使用全部 XYZ 位置/一阶/二阶 jet 生成 common-cut，并按 R87 或原连续 metric 算法评价。不能将本表的高模坡度近零复制到新的 DN 响应。

## 5. 可复现来源与实际回执

脚本：[78718-geometry-tail-cut-high-jet-diagnostic-v1.mjs](../scripts/78718-geometry-tail-cut-high-jet-diagnostic-v1.mjs)，SHA256
`5329ebb9abf1bfc2940657deb081f12d4ac097a508de8b880ba48c72a06d993a`。

报告：[2026-11-10-78718-geometry-m15-cut-high-jet-diagnostic-v1.json](2026-11-10-78718-geometry-m15-cut-high-jet-diagnostic-v1.json)，6039 B，SHA256
`07f4bdbe81f21ba09c7fe6479a94c86183c99ab337291b9efcb32c882c533541`。

实际工具 **7152ff 自然 exit0**，墙时约 6.48 秒。输入参数数组只在终端内存读取；报告保存有限诊断量，不包含 shooting 状态数组。重做这次局部计算只需给脚本 `--packet`、一个新的 `--out`，并将 `VISIBLE_FLEX_SOURCE_ROOT` 指向本题 `repro/source-root`、`CLOSING_TAIL_CACHE` 指向其中相邻题的 `scripts` 目录。它不会调用 DN worker。
