# R150 continuation：参数 -6 的完整局部谱与原九目标无额外因子成员性

作者：Astra-ISP-789f / root 与 literature_audit；AI-assisted，GPT-6 Astra Pro。2026-11-15 UTC。

状态：对同一原 17 式、全部次数不超过 3 的 6188 列来源，参数 $s=-6$ 处的完整局部正 Smith 指数准确为

$$
1,1,1,1,1,1,1,2,3.
$$

局部挠长度为 $12$，自由余维为 $13$。整个横向平方直和项已包含于原局部来源像，故原九目标在此处无需任何额外 $s+6$ 因子。这是实际 $224\times155$ 原投影计算与完整长度上界的严格夹逼，没有重新计算完整 Macaulay 矩阵，也不把该局部结论当作全局多项式证书。

## 1. 同一原来源与自然局部参数

取

$$
R=\mathbb Q[s]_{(s+6)},\qquad t=s+6,\qquad
A(s):R^{6188}\longrightarrow R^{4367}.
$$

$A$ 保留原全部 17 方程，各乘所有总次数不超过 3 的单项式；目标保留总次数 1 至 5 的全部 4367 坐标。

原可逆二项式矩坐标变换给出

$$
m_i=\sum_{j=0}^i\binom ij s^{i-j}z_j,\qquad
c=z_0,\quad d=z_1,\quad I=(z_2,\ldots,z_{10}).
$$

记

$$
V=R^{4367},\qquad W=(I^2)_{\le5},\qquad L=A(s)R^{6188}.
$$

$W$ 的秩为 $4212$，商 $V/W$ 保留 20 个纯坐标及 135 个一次横向坐标。由[原泛参数完整分类](R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)，

$$
W_{\mathbb Q(s)}\subset L_{\mathbb Q(s)},\qquad
\operatorname{rank}_{\mathbb Q(s)}L=4354,\qquad
\operatorname{rank}_{\mathbb Q(s)}\pi L=142.
$$

[原负六参数点完整分类](R150-appendix-rank-one-physical-mean-at-minus-six-full-critical-emptiness.md)已经证明原完整常数秩为 $4345$，且投影常数秩为 $133$。因此完整和投影局部模块都有九个正 Smith 指数；下面确定其所有阶数。

## 2. 实际投影确为全部 6188 来源的像

原纯平面方程严格为

$$
F_{\mathrm{pure}}=g(s)d^2\eta(s),\qquad
g(s)=-2s^2(s-2)(s+6).
$$

前 11 个 $\eta$ 坐标是原 $4p(s)p(s)^{\mathsf T}$ 的极化系数，后六个 $\Gamma$ 坐标为零。此次实际原模型给出

$$
g(-6+t)=576t-264t^2+40t^3-2t^4.
$$

在本次常数平移后的原十一条 $N$ 方程中，选取零基编号 6 的坐标，实际

$$
\eta_6(-6)=82944\ne0.
$$

所以可除该局部单位，但绝不除 $g$。原投影模块准确由以下行生成：

- 170 个纯 $c,d$ 乘子乘原 17 式，保留全部纯及一次横向输出；
- 54 个真实 $g(s)c^ad^{b+2}z_j$ 行，其中 $a+b\le2$、$2\le j\le10$。

全部 918 个原一次横向来源已逐行核为相应 $g$ 行乘 $\eta_i$。反方向由上述 $\eta_6$ 单位从真实来源恢复每个 $g$ 行。其余 5100 个原来源的投影由横向次数恒为零。故这个 $224\times155$ 矩阵呈现的正是 $\pi L$，并非在接触点擅自添加 54 个裸单位行后的扩大模块。

本轮先作常数平移 $s=-6+t$，核对 $B_6,B_{11},B_{16}$ 的可逆性与原 $J_2,J_3$ 的完整合同，再从原方程重建 Taylor 系数到四阶。所有 17 行、全部 6188 投影来源、原 $g$ 倍及双向局部生成均实际通过。

## 3. 投影的完整 Taylor–Smith 计算

每一阶段选实际常数单位子块，只求其真正右端；完整核对

$$
U(t)Y(t)=V(t)
$$

的每个 Taylor 卷积。保留全部剩余行和列，确认完整 Schur 常数项为零后才除一个共同 $t$。没有构造完整原大矩阵的逆。

实际结果如下。

| 退出阶数 | 该阶段矩阵形状 | 实际常数秩 | 累计秩 | 已确定挠长度 |
|---:|---:|---:|---:|---:|
| 0 | $224\times155$ | 133 | 133 | 0 |
| 1 | $91\times22$ | 7 | 140 | 7 |
| 2 | $84\times15$ | 1 | 141 | 9 |
| 3 | $83\times14$ | 1 | 142 | 12 |

三阶时已经达到已证明的 generic projection rank $142$，剩余 Taylor Schur 全零。因此这不是有限截断的下界猜测，而是准确的投影正谱

$$
1^7,\ 2,\ 3,\qquad\delta_P=12.
$$

投影余模的自由秩为 $155-142=13$。每个阶段的单位行列、实际非零行列式身份、右端解和完整 Schur 哈希均保存在小回执中。

## 4. 长度夹逼给出完整模块同构和目标成员性

[完整模 31 仿射最大子式因子](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)中，原 $s+6$ 因子的准确指数为 $12$。原整数模型的常数分母和行内容为 31 单位，且特征零与模 31 generic rank 均为 4354。因此原完整特征零局部长度满足

$$
\delta_A\le12.
$$

[原局部投影长度差准则](R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)给出

$$
0\longrightarrow W/(L\cap W)\longrightarrow V/L
\longrightarrow (V/W)/\pi L\longrightarrow0,
$$

以及

$$
\operatorname{length}_R W/(L\cap W)=\delta_A-\delta_P.
$$

结合实际 $\delta_P=12$ 和完整上界 $\delta_A\le12$，得到

$$
\delta_A=\delta_P=12,\qquad W/(L\cap W)=0.
$$

因此

$$
W\subset L,\qquad V/L\simeq(V/W)/\pi L.
$$

最后这个同构同时保留全部挠模及自由部分，故完整原模块的正 Smith 指数也准确为 $1^7,2,3$。特别地，最大正指数为 $3$，删去一个最大正指数后的 determinantal length 为 $9$。原常数秩仍为 $4345$；本条没有把特殊点误说成满 generic rank。

原九个目标准确为

$$
t_j(s,m)=
\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2=z_j^2,
\qquad 2\le j\le10.
$$

所以全部 $t_j\in W\subset L$。等价地，对每个 $j$，存在原次数不超过 3 的有理局部来源，满足分母在 $s=-6$ 不为零，并完整产生 $t_j$。这不是仅在剩余点取值后的成员性。

原

$$
h_0=s^3(s-2)F_+^2F_-^2E_8
$$

在本点的实际因子取值为

$$
F_+(-6)=-2180,\qquad F_-(-6)=-540,\qquad E_8(-6)=1673280,
$$

从而

$$
h_0(-6)=4006940238043545600000\ne0.
$$

因此 $h_0$ 是本局部环的单位；原九个 $h_0t_j$ 同样全部属于 $L$，且无需追加任何 $s+6$ 因子。

## 5. 实际运行、源码与小证据

原始运行是 run **43702348535**、job **132776011109**，步骤 **minus-six-original-projected-local-smith**。执行来源 commit：

31811ae0e3a61ff3b193d094059703b44a67ba17。

[完整小回执](../notes/r150-infinity-remote-session-789f/43702348535-minus-six-original-projected-local-smith.json)记录 exit code 0、数学时间 7.521673932998965 秒、墙钟时间 7.63741521999691 秒。原临时回执 8191 字节，SHA-256：

0039c5bdb8b1e720ac324e7f40ce3c3295248ed05776580c96fbaf7d35232619。

[原来源投影源码](../notes/2026-11-15-r150-minus-six-original-projected-local-smith-789f.py)的 SHA-256：

73c11b1d957962fdb8c9b17143aaf8d894845b1b4c8382f200eeaf2422178119。

其原 generator 与单项式 actions 分别固定为：

- 2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186；
- 2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332。

原投影 $P_0,\ldots,P_4$ 的逻辑 SHA-256：

- f31a69a3836e62989ca9a8a7ad67f8c535a1f496dc00b2c7196b9aef9590b99f；
- bf1e99d5fe502b59564e8635185ba39d1e5c1ebc39481d7a2f29fc36ef376068；
- 617bb1c63f38f9ee60462265b55dbe095f396b120422877f7c1f47596a56785e；
- 8816f45a3a59d38cebf9f80484238039737375c88f31a0491fdd5784061b2d6f；
- 2b73defd99a1fc95f831eeb1bdd5da9958e524aca5596e6baea1db59c7d75fd2。

本轮没有重算原正常形、没有新有限域 rank 计算、没有上传大矩阵或可重算数组。完整证明使用原全部来源的局部生成与长度同构；没有制造一套与原目标不同的局部方程。

## 6. 剩余范围

本条关闭的是参数 $-6$ 处原九目标的局部多项式来源条件，并且更强地关闭整个 $W$ 的局部来源条件。$s=0$ 已由另一完整局部谱与泛型像桥支付；$s=2$、$F_\pm$、$E_8$ 等其它有限点及未知异常支持仍按各自实际证据推进。

本条不由单点局部成员性宣布原 $h_0t_j$ 的全局 $\mathbb Q[s]$ 来源成员性，不补造未计算的显式全局来源，也不改变原 Hilbert 空间问题的完成范围。

## 7. 公共因子 $K_{115}$ 与条件来源费用 $8574$

已付零点最大子式阶为 $66$，本稿把负六点的原最大子式阶从已用下界 $9$ 精确提高至 $12$。因此原全部最大子式的公共因子可取
$$
K_{115}=s^{66}(s-2)^9(s+6)^{12}F_+^2F_-^2E_8^2,
\qquad \deg K_{115}=115.
$$
其首项系数仍为 $5^6$，是 $31$ 单位。这里除的是整个原最大子式族；未把次大阶 $9$ 当作最大阶。

沿[同一选定子式及其无穷远阶](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)保原 $H=8770$、无穷远界 $130/125/125$，有
$$
8527\le\deg D\le8640,\qquad
8412\le q:=\deg(D/K_{115})\le8525.
$$
原三支加权余式费用相应为
$$
\begin{aligned}
\text{非基来源}&\le8525-1+45=8569,\\
\text{原来源转移}&\le8770+55-125-115-11=8574,\\
\text{目标伴随支路}&\le8770+64-125-115-10-8412=172.
\end{aligned}
$$
所以原九个 $h_0t_j$ **若已具有全局 $\mathbb Q[s]$ 原来源**，可取统一加权费用至多 $8574$。本稿的负六局部成员性没有支付这个全局前提。固定 $D$ 的首项 $31$ 单位条件仍未证明，也没有用 $K_{115}$ 的首项单位替代它。
