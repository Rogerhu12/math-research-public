# Phi：同一二十二列的一阶八维左右核 Schur 输入

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。

## 1. 已付同一矩阵和剩余五阶

沿用[QQ 最高秩十四及次数上界 794](../results/R150-appendix-unit211-Phi-zero-original-highest-rank-fourteen-and-degree-upper-bound-794.md)的同一 $B_{22}$、固定对偶以及
$$
N(t)=H_0+tH_1+O(t^2),\qquad
\det N(t)=t^{802}P(t^{-1},Q).
$$
已付 $\operatorname{rank}_{\mathbb Q(Q)}H_0=14$，故已有八个无穷因子；此前固定原模多项式在 $Q=2,p=1009$ 的真实次数为 789、首项 790。目前正确范围是 $789\le\deg_uP\le794$。

本次新目标只用真正一阶系数 $H_1$ 和完整八维左右核；不重跑旧二十二阶增广秩、Hungarian 或模 determinant。

## 2. 实际十四阶 minor 只用于定义核基

固定前次真实主元列
$$
J=(0,1,3,4,5,6,7,8,12,13,17,18,19,20).
$$
旧日志没有保存原行置换索引，因此只在 $H_0[:,J]$ 上选择十四个原行。优先用 $Q=2,p=1009$ 的小矩阵；若其列秩不足，再依次用预定 $Q=3,5,7$。这只是找一个非零十四阶 minor，不测试原理想、不挑一个能使 Phi 空的参数点。

得到原行 $I$ 后，在完整 QQ$[Q]$ 中构造
$$
A=H_0[I,J],\quad B=H_0[I,J^c],\quad
C=H_0[I^c,J],\quad D_0=H_0[I^c,J^c].
$$
程序以十四阶 fraction-free Gauss–Jordan 得到非零多项式 $\Delta$ 和完整矩阵 $\operatorname{Adj}$，并实际返回
$$
A\operatorname{Adj}=\operatorname{Adj}A=\Delta I_{14}.
\tag{1}
$$
不要求任何 $\Delta(Q)$ 是原物理单位。它仅在系数域 $\mathbb Q(Q)$ 中非零。

## 3. 全部左右核和新八阶矩阵

按原行、列顺序插回以下多项式矩阵：
$$
\widetilde U=[-C\operatorname{Adj},\ \Delta I_8],
\qquad
\widetilde V=
\begin{bmatrix}-\operatorname{Adj}B\\ \Delta I_8\end{bmatrix}.
\tag{2}
$$
源完整返回
$$
\widetilde U H_0=0,\qquad H_0\widetilde V=0.
\tag{3}
$$
两个补坐标块均为 $\Delta I_8$，所以它们在 $\mathbb Q(Q)$ 上有完整的八维秩；结合已付 $\operatorname{rank}H_0=14$，(2) 是完整左右核基的非零尺度。

真正的新矩阵为
$$
S_1=\widetilde U H_1\widetilde V.
\tag{4}
$$
每个共同多项式行、列内容仅为了计算函数域秩而精确除去，全部乘回；没有将它们加入原物理单位。最后对新八阶矩阵做完整增广多项式消元并返回 64 个变换身份，得到真实秩 $s$。

## 4. 对原 determinant 的严格后果

在行列顺序 $(I,I^c)$、$(J,J^c)$ 中，常数主块 $A$ 在 $\mathbb Q(Q)$ 上可逆。对 $N(t)$ 作常数可逆行列变换，再取其 Schur 补，得到
$$
\det N(t)
=\text{一个 }t=0\text{ 处非零的单位}\;
 t^8\det\bigl(\Delta^{-2}S_1+O(t)\bigr).
$$
这是完整左右核的一阶 Schur 公式；非零尺度 $\Delta^{-2}$ 不改变秩。因此
$$
\operatorname{ord}_{t=0}\det N(t)\ge8+(8-s),
\qquad
\deg_uP\le802-8-(8-s)=786+s.
\tag{5}
$$
若实际 $s=3$，(5) 恰给 $\deg_uP\le789$；合并同一固定原模多项式已付的 789 次下界，才得到真正精确 789 次及 $Q=2,p=1009$ 保度。

若 $s>3$，只给新的准确上界与尚未付差额。所有函数域操作仅证明原多项式高系数恒等消失，其结论延拓到全部 $Q$；任何 minor、内容或消元主元的零纤维都不因此从原图移除。没有提前宣称整个 Phi 空。

## 5. 冻结源和依赖

建议文件：
2026-11-28-unit211-Phi-zero-original-twenty-two-first-kernel-Schur-degree-input-8542.py。

源 blob 65543f5a2319a32031389ab4c3a1b6ca8840dbbb，10159 字节，SHA256
7a8d5bbde603d98e8d3762d535c422f236e61cf5c82330380ca2c6869af13b65。

使用与前次最高秩源相同的六件小源码依赖。直接环境变量 ISP_PHI_RAW_TWENTYTWO_SOURCE 指向二十二列原源，只取其 4080 字节必要原列定义前缀；其余五个递归源码环境不变。无历史 JSON。旧最高矩阵 SHA 用来确认一阶系数属于同一个原估值矩阵，没有重跑旧 rank 作为前置门。

所有计时器受同一个绝对 120 秒截止约束。只输出小 minor 索引、核/矩阵 SHA、秩、原返回数与回执，不保存可重算矩阵、系数、编码或分片。
