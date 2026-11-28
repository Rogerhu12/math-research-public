# Phi：原二十二列的一阶核 Schur 秩五，权 determinant 次数上界降至 791

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）。

## 1. 同一原对象和结论

继续[原最高矩阵秩十四及 794 次上界](R150-appendix-unit211-Phi-zero-original-highest-rank-fourteen-and-degree-upper-bound-794.md)中同一个
$$
P(u,Q)=\det B_{22}(u,Q)\in\mathbb Q[u,Q].
$$
二十二列的原来源、旧权清分母和固定次数对偶均保持不变。新输入是同一无穷矩阵的一阶系数及其完整八维左右核。

实际一阶核 Schur 矩阵在 $K=\mathbb Q(Q)$ 上的秩为五。因此
$$
\boxed{789\le\deg_uP(u,Q)\le791,}
\qquad
789\le\deg_uP(u,2)\le791.
\tag{1}
$$
下界和模首项 790 来自已支付的同一固定原 determinant；本次没有重算它。仍有两次差额未付，尚不能宣称精确 789 次或相应保度整模型。

## 2. 同源的一阶系数及完整核

沿用已付整数对偶 $a_i,b_j$，其总和为 802，并置
$$
N_{ij}(t)=t^{a_i+b_j}(B_{22})_{ij}(t^{-1},Q),
\qquad
N(t)=H_0+tH_1+O(t^2).
$$
全部条目属于 $K[t]$，且
$$
\det N(t)=t^{802}P(t^{-1},Q).
\tag{2}
$$
$H_0$ 是前稿同一个最高矩阵，规范 SHA256 为
bcbe7bcc2e9a4962af80c1504041aa330edb4903278343f868a46e5d43711b8a。
其 $K$ 秩十四已付。本次真正的一阶系数 $H_1$ 最大 $Q$ 次数为十一，规范 SHA256 为
8c92933a1c8cafa20e3386dfa469aecc48e75ff4b48c591540d01e6e8a46d42a。

固定此前十四个独立原列
$$
J=(0,1,3,4,5,6,7,8,12,13,17,18,19,20).
$$
在 $Q=2,p=1009$ 只选择一个非零十四阶原行 minor，实际得到
$$
I=(0,1,2,3,4,5,9,10,11,16,17,18,19,20).
$$
该点值只选择核基，不测试原解是否存在。随后所有矩阵运算都回到完整 QQ$[Q]$。

按 $(I,I^c)$、$(J,J^c)$ 分块写
$$
H_0=\begin{pmatrix}A&B\\C&D_0\end{pmatrix}.
$$
十四阶 fraction-free Gauss–Jordan 返回非零 $\Delta\in\mathbb Q[Q]$ 及完整 $\operatorname{Adj}$，实际逐坐标验证
$$
A\operatorname{Adj}=\operatorname{Adj}A=\Delta I_{14}.
\tag{3}
$$
$\deg_Q\Delta=72$；其 SHA256 为
906ca700863a5e4d580f1d70a0030779a49f6d01e0f82da2b23d9faf8cfe7398。

按原行列顺序插回
$$
\widetilde U=[-C\operatorname{Adj},\ \Delta I_8],
\qquad
\widetilde V=
\begin{bmatrix}-\operatorname{Adj}B\\ \Delta I_8\end{bmatrix}.
\tag{4}
$$
完整返回
$$
\widetilde U H_0=0,\qquad H_0\widetilde V=0.
\tag{5}
$$
两补坐标块都是 $\Delta I_8$，所以 (4) 的左右秩均为八；它们是已付完整核的非零尺度。式 (3) 返回 392 个坐标，式 (5) 返回 352 个坐标。没有把 $\Delta$ 或任何 $Q$ 主元当成原物理单位。

## 3. 新八阶矩阵的实际 QQ 秩

构造
$$
S_1=\widetilde U H_1\widetilde V\in M_8(\mathbb Q[Q]).
\tag{6}
$$
其最大 $Q$ 次数 151，规范 SHA256 为
5568e61824cb876cc7b91db7d970595f40816dad1c1c44eee7f4f7407c0ab31b。

仅为计算 $K$ 上的秩，对 (6) 的公共行、列多项式内容作精确除法，每项均乘回。约化后的条目最大 $Q$ 次数五。这些非零内容只是函数域坐标尺度，没有加入物理单位表。

对这个新的八阶矩阵作增广 fraction-free 消元，返回全部 64 个变换坐标。实际五个阶梯主元列为
$$
1,2,5,6,7,
$$
主元多项式 $Q$ 次数依次为 $1,2,6,9,9$；其余三行完整为零。每个消元主元非零，因此变换在 $K$ 中可逆，得到
$$
\operatorname{rank}_K S_1=5.
\tag{7}
$$
本次所有阶段合计 5288 次精确多项式除法均完整乘回，其中十四阶双向返回之前为 4914 次。没有执行旧二十二阶增广秩、旧 Hungarian、旧模 determinant 或更高 jet。

## 4. 十一个真实无穷阶因子

在上述分块次序中，$A(0)=A$ 可逆。完整幂级数 Schur 补为
$$
S(t)=D(t)-C(t)A(t)^{-1}B(t).
$$
因为 $\operatorname{rank}H_0=14$，有 $S(0)=0$，而完整一阶公式是
$$
S(t)=t\Delta^{-2}S_1+O(t^2).
\tag{8}
$$
因此
$$
\det N(t)=\det A(t)\,t^8
\det\bigl(\Delta^{-2}S_1+O(t)\bigr).
$$
由 (7)，最后一个八阶常数矩阵有三个零方向；通过与 $t$ 无关的可逆行变换，这三个方向各给一个 $t$ 因子。于是
$$
\operatorname{ord}_{t=0}\det N(t)\ge8+3=11,
\qquad
\deg_uP\le802-11=791.
\tag{9}
$$
这里先在 $K$ 上证明原 $u$ 高次系数为零；这些系数原本属于 QQ$[Q]$，故恒等为零，覆盖全部 $Q$，包括 minor、内容与消元主元的零点。$H_{42}=0$ 也完整保留。

下一尚未计算的对象是这三个剩余核方向上的二阶 Schur 系数。它必须包括 $A(t)^{-1}$ 的修正，不能把 $\widetilde U H_2\widetilde V$ 单独当成完整二阶项。本条只登记 (1)，不提前给二阶秩或整个 Phi 空性。

## 5. 唯一实际执行

源：[原一阶八维核 Schur 输入](../notes/2026-11-28-unit211-Phi-zero-original-twenty-two-first-kernel-Schur-degree-input-8542.py)，10159 字节，blob
65543f5a2319a32031389ab4c3a1b6ca8840dbbb，SHA256
7a8d5bbde603d98e8d3762d535c422f236e61cf5c82330380ca2c6869af13b65。

唯一首次 run 46097560019、job 140832333998；源提交及真实 pull 后提交均为
292beb620132a650f6323e3bebf07c3b22f139f5。
实际 $7.289653619$ 秒、最大 RSS $61024$ KiB、内层退出码 $0$。
stdout 为 3162 字节，SHA256
788f8cc8f774034b1a34392e32b55f02847896791fa8d307bb5d0fefb13b360f。

真实 pull 时间为 2026-11-28 02:20:36.118996 UTC，根与课题 README 均无变化。没有保存可重算矩阵或系数载荷；没有声称整个 Phi 或普通 ISP 已完成。
