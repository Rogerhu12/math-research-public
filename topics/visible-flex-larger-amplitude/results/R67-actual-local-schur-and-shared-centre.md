# R67 — 实际两胞元的有符号 Schur 系数与共同中心重设

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

## 0. 结论与精确范围

本文接 [R65 的真实 Taylor/Wronskian 机制](R65-local-taylor-flow-true-wronskian-and-shared-slope.md)，
已在**同一个固定实度量**上完整支付 outer cells 11、10 的 $m=2,4$
真实背景流。线性坐标始终使用 $mu_*=mu_{11}$，跨这两个胞元不再乘
$2^{11/4}$。切口斜率与 [R61 真头接口](R61-strong-positive-parameter-columns-and-true-cut.md)
使用同一个真实无限尾问题；新流只把其背景线性列包围得更紧，没有换成有限 Robin 尾。

本文还已支付以下具体接口。

1. 四个局部低高度 Schur 标量 $S_{0,m}(R)$ 都严格非零。
2. 把真实头与保存候选的切口动量差换算成 **canonical $Q$ 参数单位**。
   $m=2$ 的旧候选 cut 分量约为当前参数轴的 $3198.48$ 倍；这是实际
   有符号中心差经过真实局部线性传播后的结果，不是旧宽斜率区间的噪声。
3. 对两行输出保留全部46个真头参数导数列。仅头部非线性 DN 导数造成的
   这两行归一扰动的 $ell^1$ 算子范数小于 $4.441\,10^{-8}$。
4. 给出保持 $g$、保存高度 $H$ 和其余模式的明确 $C^2$ 候选重设。
   重设后两模式的 **cut 分量**分别小于 $0.000298351$ 和 $0.004114770$
   个参数轴；完整 mean 仍由同一个根重建。

这不是完整外头闭合。第2、4项尚未加上外候选的连续 forcing；重设产生的
补偿 forcing 必须保留，而且其线性贡献会精确抵消仅靠换中心得到的表面改善。
本文第7节证明这个恒等式。cells 9 至0、其余低模式、全部高模式以及完整
非线性外边值逆仍须另付。

这里的强中心是已经完整求得的新有理深度量、q085 实际 M20 高度向量，
不是另一条 q095/q105 的 stored-$g$ 数值分支。所有46个头部自由参数、
完整 mean 和高频迹继续沿用 R58/R59/R61；本文没有把高切口高度设为零。

## 1. 同一实源与固定物理动量坐标

记真正的 node12 半径为 $b$，真实背景坡度为 $w(r)>0$，固定

$$
\mu_* = \mu_{11},\qquad r_c=\text{原冻结二进制 cuff 半径}.
\tag{67.1}
$$

$r_c$、$b$、$w$ 和全部 source 参数均按 R26 的实积分定义使用；没有把
名义二进制 outer radius $0.3$ 当作其真实积分终点。n10、n11 的原
$R_n,\alpha_n$ 来自完整160项 source 表，原 frozen warp alpha 也保留。
这两层没有 valley 修正、个别 warp 权或个别 cap 覆盖，且 $\chi=j_0=1$。

令 $\delta_n=\delta_0 2^{-n}$、$\rho=2^{11/4}$。原 raw source 的
profile level 在

$$
1,\quad R_n/\delta_n,\quad\delta_n/\alpha_n,
\quad1/\delta_n,\quad\rho
\tag{67.2}
$$

之间按同一 smoothstep 插值。因原 source 半径 $r_o\ge r_c$，整个胞元
都有

$$
w\le\frac{\mu_n}{r_c^7}
\max\{1,R_n/\delta_n,\delta_n/\alpha_n,1/\delta_n,\rho\}
< \mathrm{slopeCap}\,e^{-\mathrm{capTransition}}.
\tag{67.3}
$$

最后一项已用严格 Arb 实数区间逐层通过，故整个 n10/n11 cap 确实不活跃。
这允许复用 R65 的 raw-source Taylor 公式；不是仅凭少数采样点决定分支。
原来的10,793个真实 material 面板也独立满足 raw 分支，作为旧证据的相交核销。

对实 cosine 高度系数 $h_m$ 定义

$$
Q=\frac{h_m}{r^4},\qquad
\Xi_*=\frac{r^4w}{\sqrt{12}\mu_*}
\left(h_{m,r}-\frac{m^2h_m}{r}\right),\qquad u=m^2-4,
\tag{67.4}
$$

以及去掉对角项的坐标

$$
q=(r_c/r)^uQ,\qquad v=(r/r_c)^u\Xi_*.
\tag{67.5}
$$

原 source 的 $w$ 仍使用各胞元本来的 $\mu_n$。只有线性坐标中的动量
尺度固定为 $\mu_*$。于是完整背景方程为

$$
\frac{d}{dr}\binom{q}{v}=
\begin{pmatrix}0&a_m(r)\\-b_m(r)&0\end{pmatrix}
\binom{q}{v},
\quad
a_m=\frac{\sqrt{12}\mu_*r_c^{2u}}{r^{8+2u}w},\quad
b_m=\frac{\nu_m\sqrt{12}\,r^{6+2u}w}{\mu_*r_c^{2u}},
\quad\nu_m=\frac{m^2(m^2-1)}{12}.
\tag{67.6}
$$

这里 $(q,v)_r$ 表示整个二分量向量的径向导数。矩阵迹为0，因此真实
基本矩阵行列式恰为1。式 (67.4)–(67.6) 在两个胞元的公共端点完全相同，
所以不再有胞元动量重标因子。

## 2. 已完成的真实流及 $S_0$ 图

令 $\Phi_m(R,b)$ 为 (67.6) 从 $b$ 向外到 node11 或 node10 的基本矩阵。
按 (67.5) 还原，外端 canonical 高度满足

$$
Q(R)=A_m(R)Q(b)+B_m(R)\Xi_*(b),
\tag{67.7}
$$

其中

$$
A_m=(R/b)^u\Phi_{00},\qquad
B_m=(Rb/r_c^2)^u\Phi_{01}.
\tag{67.8}
$$

R65 的真实内头线性列在切口为 $(Q,\Xi_*)=(1,s_m)$。它不是一个外头
新增自由参数；同一个实数 $s_m$ 已由真实无限深尾定义。故

$$
\boxed{S_{0,m}(R)=A_m(R)+B_m(R)s_m.}
\tag{67.9}
$$

实际计算同时推进共享中心列 $(1,\widehat s_m)$ 和两个独立基列；
在每个外端交集包围

$$
S_0\in
\bigl[Q_{\widehat s}(R)+B_m(s_m-\widehat s_m)\bigr]
\cap[A_m+B_ms_m]
\cap[\text{原真实 PB 流区间}].
\tag{67.10}
$$

所以共同振幅和共同斜率的关系没有被拆成互不相关的背景问题。
括号中的旧 PB 区间是冗余相交条件，不是新流误差的替代品。

R65 已证明的 Taylor 递推、全基点导数余项与根括号处理在这里仅将
线性坐标 $\mu_n$ 改为同一个正数 $\mu_*$。source 本身不变。
本次使用256-bit Arb、24阶 Taylor、$2^{-100}$ 局部平衡余项门和
$2^{-160}$ 临界根括号。完整18段共3,478个 Taylor 面板、8个临界根括号，
所有余项、实半径端口相交、旧真实流相交和非零高度图都通过。

实际系数的方便阅读值如下；严格证据是包内向外 dyadic 端点。

| 外端 | 模式 | $S_0=Q(R)/Q(b)$ | $R^4S_0=h_m(R)/Q(b)$ |
|---|---:|---:|---:|
| node11 | 2 | $-5.510180359119779\,10^5$ | $-3.460419758509642$ |
| node11 | 4 | $-1.1033707432237582\,10^7$ | $-69.2922131758113$ |
| node10 | 2 | $2.1335644066843054\,10^{11}$ | $1.346877058754216\,10^6$ |
| node10 | 4 | $8.56245985454624\,10^{13}$ | $5.405311744263046\,10^8$ |

这四个局部标量均严格非零。它们没有证明46模外头矩阵或无限维外头
边值算子的可逆性。

## 3. 共同斜率下的实际 cut 分量

记 $q_m$ 为保存实际中心的 canonical $Q_m(b)$，$L_m$ 为其 orthonormal
cosine 动量。真实切口转换系数为

$$
c_b=\frac{\sqrt{12}\mu_*}{b^4w_b^2}>0.
\tag{67.11}
$$

由于真实头与候选的低 $Q$ 完全相同，它们的 $m^2b^3Q/w_b$ 项准确消去。
由 R63 的选定非线性功能界和 R61 完整头反馈，真实差值满足

$$
\beta_{K,m}=c_bq_ms_m-\sqrt2L_m+\epsilon_m,
\qquad |\epsilon_m|\le E_m.
\tag{67.12}
$$

$E_m$ 同时包含真实46模辅助解的非线性 correction 和 R58 全频头反馈；
没有把这两个解当成完全相同。mean 和其余高模式仍按 R61 单独保留。

如果只把 (67.12) 的 cut 项送入当前局部背景外端低高度约束，它给出的
canonical 参数分量为

$$
\delta q_m^{\rm cut}
=-\frac{B_m}{c_bS_{0,m}}\beta_{K,m}.
\tag{67.13}
$$

**定义 (67.13) 时暂未加入外源。** 因此外源可能与它相消，不能用这个
分量超过参数轴直接证明完整外匹配失败。

对 (67.12) 的已知线性部分，实际使用共同斜率的 Möbius 式

$$
f_m(s)
=-\frac{B_m(c_bq_ms-\sqrt2L_m)}{c_b(A_m+B_ms)}
=-q_m+\frac{q_mA_m+B_m\sqrt2L_m/c_b}{A_m+B_ms}.
\tag{67.14}
$$

因为分母在完整真斜率区间上严格不为0，对于任何固定的合法
$A_m,B_m,c_b$，$f_m(s)$ 对 $s$ 单调或恒定。两端点的区间像取凸包，
再加

$$
\left[-\left|\frac{B_m}{c_bS_0}\right|E_m,
       \left|\frac{B_m}{c_bS_0}\right|E_m\right]
\tag{67.15}
$$

就包围整个真实 cut 分量。此推理不需要在不知道导数符号时假选一个符号；
每个固定背景实例的两个端点已经包含该实例的整个单调像。

R61 的实际轴为 $a_2=2^{-193}$、$a_4=2^{-196}$。node11 和 node10 都有

$$
3198.4771<|\delta q_2^{\rm cut}|/a_2<3198.4778,
\qquad |\delta q_4^{\rm cut}|/a_4<0.004140540.
\tag{67.16}
$$

$m=2$ 的 canonical cut 分量约为 $-2.5477343\,10^{-55}$。这解释了
为什么仅再压缩原线性斜率区间不能消掉当前中心差；它本身严格非零。
式 (67.16) 只比较量纲完全相同的参数，未把裸物理 $K$ 误差与 $Q$ 轴比较。

## 4. 已付真头非线性导数的两行局部传播

令 $a_j$ 为 R61 全部46个轴，输入参数以
$\sum_j|\delta Q_j|/a_j\le1$ 归一。R61 保留

$$
D(\text{真头 trace})=B_0+\Delta B,
\qquad \Delta Q_j=\Delta P_j=0,
\tag{67.17}
$$

并逐输出模式、逐输入参数给真实 $\Delta K_{m,j}$ 的正界。
本文对 $m=2,4$ 的两输出行使用

$$
C_{m j}=
\frac1{a_m}\left|\frac{B_m}{c_bS_{0,m}}\right|
\,\operatorname{cap}(\Delta K_{m,j}).
\tag{67.18}
$$

这是对归一输入轴的列，不再多乘一次 $a_j$。实际包完整保存
$2\times46$ 项，且两个外端分别满足

$$
\max_j\sum_{m\in\{2,4\}}C_{mj}<4.441\,10^{-8}.
\tag{67.19}
$$

因此这里没有因只看 $m=2$ 的一个对角项而漏掉另外45个输入。
式 (67.19) 只涉及真头 DN correction 经背景外流的两行；完整外候选
线性化的源导数、其余低行以及无限高块尚未包括，不能将它称作完整
Schur Neumann 门。

## 5. 明确保持 $g,H$ 的候选 cut jet 重设

取同一个严格记录的 dyadic 中心 $\widehat s_m$，定义新的**确切 dyadic**
候选动量

$$
\widehat L_m
=\operatorname{mid}_{\rm dyadic}
\left(\frac{c_b\widehat s_m q_m}{\sqrt2}\right),
\qquad m=2,4.
\tag{67.20}
$$

这里 midpoint 的具体 dyadic 值是定义的一部分；不是“真实 $c_b$”的
未计算取值。其残余区间 $c_b\widehat s_mq_m-\sqrt2\widehat L_m$ 在
账本中完整保留。实际值为

$$
\widehat L_2=
952613911650926180903376877471692341\,2^{-221},
\qquad
\widehat L_4=
424252065143616126687275593170840713\,2^{-243}.
\tag{67.21}
$$

其余18个保存模式的 $L$ 完全不动，所有20个保存高度 $H$ 不动。
这只是重新定义一个待校正外候选，不声称原 worker 精确求出了这些新动量。

令 $c$ 为真实 node11 半径，$\ell=c-b>0$，$x=(r-b)/\ell$，并设

$$
B(x)=x-6x^3+8x^4-3x^5=x(1-x)^3(1+3x),
\tag{67.22}
$$

$$
\delta h_m(r)=\ell w_b\sqrt2(\widehat L_m-L_m)B(x)
\quad (b\le r\le c),\qquad
\delta h_m(r)=0\quad (r\ge c).
\tag{67.23}
$$

在 $b$，$\delta h_m=\delta h_{m,rr}=0$，且
$\delta h_{m,r}=w_b\sqrt2(\widehat L_m-L_m)$；在 $c$，函数及其前两阶
导数均为0。因此保持原低 cut 高度和整个 node11 外侧候选不变，并
准确实现所需的两项 cut 动量变化。背景度量完全不改。

由

$$
B'(x)=(1-x)^2(1+5x)(1-3x),\qquad
B''(x)=-12x(1-x)(3-5x),
\tag{67.24}
$$

可得

$$
0\le B\le16/81,\quad |B'|\le1,\quad |B''|\le9.
\tag{67.25}
$$

第一项最大值在 $x=1/3$；$B'$ 的最小值是 $-64/125$，在 $x=3/5$。
最后一项由 $x(1-x)\le1/4$、$|3-5x|\le3$ 直接得到。
这些是整个连续区间的界，不是有限点检查。

记 $d_m=w_b\sqrt2(\widehat L_m-L_m)$。于是

$$
\|\delta h_m\|_\infty\le\frac{16\ell}{81}|d_m|,
\quad \|\delta h_{m,r}\|_\infty\le|d_m|,
\quad \|\delta h_{m,rr}\|_\infty\le\frac9\ell|d_m|.
\tag{67.26}
$$

实际 $m=2$ 的 $|d_2|<3.490420\,10^{-55}$，对应三项上界依次为
$2.143442\,10^{-60}$、$3.490420\,10^{-55}$、$1.010465\,10^{-49}$。
$m=4$ 的这三项更小。

## 6. 完整 mean 与重设后的 cut 余量

仍使用实际 R33/R44 变量

$$
\mathsf P=\frac{h_\theta}{rw},\qquad
K_\perp=\frac{h_{\perp,r}}w,
\qquad\sigma=1/64.
\tag{67.27}
$$

原候选整个 cell11 的 $\mathcal A_{\sigma,1}$ 相对范数为
$R_{\rm old}<3.429795\,10^{-18}$。由实际 raw source 的 level 最小值和
原 unwarped 半径最大值直接得到 $w_{\min}>2.713198\,10^{-17}$。
于是 (67.23) 的完整强改变量满足

$$
\Delta R\le
\sum_{m=2,4}(1+m)e^{\sigma m}
\frac{|d_m|}{w_{\min}}
\left(1+\frac{16m\ell}{81b}\right)
<3.982867\,10^{-38}.
\tag{67.28}
$$

$R_{\rm new}=R_{\rm old}+\Delta R<1/64$，所以 R33 完整 mean 小根
保持存在，并使用同一个所有频率的根，而不是截断角度平均。
沿新旧候选之间的线段，R33 的 $\|DM\|\le16R_{\rm new}$ 给

$$
|\Delta M|\le16R_{\rm new}\Delta R<2.185667\,10^{-54}.
\tag{67.29}
$$

将 mean 高度的唯一常数锚定在 node11，使

$$
\delta h_0(r)=-\int_r^c w(s)\,[M_{\rm new}(s)-M_{\rm old}(s)]\,ds.
\tag{67.30}
$$

那么 $r\ge c$ 的完整高度保持不变，且

$$
|\delta h_0|\le\ell w_{\max}\,16R_{\rm new}\Delta R
<2.643039\,10^{-63}.
\tag{67.31}
$$

由于非均值场及所需的前阶径向导数在 $c$ 一致，mean 根及其径向导数
也一致，故完整高度在 $c$ 是 $C^2$ 的。没有逐胞元重新指定 mean 高度。
在当前单 cut、自由 cuff 高度的规范里，最终接合时可对内尾整体选择一个
加性常数；固定形状的纯相位族使用同一个常数。本文未据此删除任何
非均值边界方程。

在 (67.12) 中将 $L$ 换为 (67.20)，但仍保留相同 $s-\widehat s$ 和
相同真实非线性 $E_m$，重复第3节的 Möbius 端点包围，两个外端均得到

$$
\frac{|\delta q_2^{\rm cut,new}|}{a_2}<0.000298351,
\qquad
\frac{|\delta q_4^{\rm cut,new}|}{a_4}<0.004114770.
\tag{67.32}
$$

这一步为共享真线性中心提供了精确、可计算的外候选 cut jet。
它没有令真实头的非线性 DN correction 为0。

## 7. 必须同时保留的补偿 forcing

对任何背景二阶高度算子写成一阶系统

$$
Y_r=C(r)Y+e_v F(r),\qquad
\mathcal L Y=Y_r-CY.
\tag{67.33}
$$

令 $Y_c$ 是实际候选，$\beta=Y_*(b)-Y_c(b)$，其中 $Y_*$ 的内端来自
真实头。外端误差的精确变参数恒等式是

$$
Y_*(R)-Y_c(R)
=\Phi(R,b)\beta
+\int_b^R\Phi(R,r)
\bigl[e_vN(Y_*(r))-\mathcal L Y_c(r)\bigr],dr.
\tag{67.34}
$$

这里 $N$ 是完整 mean 和点态分母下的真实非线性项；没有用候选的有限
Galerkin 方程代替它。对任意候选变化 $\delta Y$，恒等式

$$
\int_b^R\Phi(R,r)\mathcal L\delta Y(r)\,dr
=\delta Y(R)-\Phi(R,b)\delta Y(b)
\tag{67.35}
$$

来自对 $\Phi(R,r)\delta Y(r)$ 求导。对 (67.23) 的紧支撑变化，
node11 和 node10 都有 $\delta Y(R)=0$，且
$\beta_{\rm new}=\beta-\delta Y(b)$。故

$$
\boxed{
\Phi\beta_{\rm new}-\int\Phi\mathcal L(Y_c+\delta Y)
=\Phi\beta-\int\Phi\mathcal L Y_c.}
\tag{67.36}
$$

这是为什么不能把 (67.32) 单独称作完整外残差改善。
重设的价值是让切口迹、背景列和候选线性项使用相同符号中心，并将
误差预算放在真实非线性和实际候选残差上。若把非线性拆为
$N(Y_c+\delta Y)$ 与未知校正，其差仍要完整计入。

在当前固定 gauge 中，物理高度源 $f_H$ 满足

$$
h_{m,rr}+\frac{w_r}{w}h_{m,r}
-\frac{m^2w_r}{rw}h_m=f_H.
\tag{67.37}
$$

它只进入 $v_r$，系数为

$$
\left(\frac r{r_c}\right)^u\frac{r^4w}{\sqrt{12}\mu_*}.
\tag{67.38}
$$

若 tail 的原 source 坐标 $x$ 使用第二行源 $N_x$，且
$f_H=(w/r_x)N_x$，则进入 $v_x$ 的准确系数是

$$
\boxed{\left(\frac r{r_c}\right)^u
\frac{r^4w^2}{\sqrt{12}\mu_*}N_x.}
\tag{67.39}
$$

没有遗漏 $w$、$r_x$ 或重复一个 $\rho$。后续真实有序源核必须保留
$N_x(r)$ 与 $w(r)^2$ 的位置关联，不能把谷底源峰值和脉冲处最大 $w^2$
在整个胞元上同时取极值。

### 7.1 整段候选线性项已经准确合并

保存候选在任一原物理节点满足 $h_{c,m}(R)=R^4Q^{\rm saved}_{R,m}$，
其中 $Q^{\rm saved}_{R,m}$ 是原文件中明确的 binary64 常数。由 (67.35)，
将整个候选线性 forcing 与 cut 项准确合并，除以外端高度图后得到

$$
\boxed{e^{\rm lin}_m(R)=q_m-\frac{Q^{\rm saved}_{R,m}}{S_{0,m}(R)}.}
\tag{67.40}
$$

候选 cut 动量 $L_m$ 在这个式子里准确消失，故不能仅通过 (67.20)
改变它。按本文严格 dyadic $S_0$ 区间作有理数区间除法，得到下面的
实际方便阅读值；完整有理端点另有执行包。

| 外端 | 模式 | $e^{\rm lin}_m$，canonical $Q$ 单位 | 连同真头非线性 cut 余项后的轴倍数 |
|---|---:|---:|---:|
| node11 | 2 | $9.653018414733358\,10^{-48}$ | 约 $1.21185957285685\,10^{11}$ |
| node10 | 2 | $1.9102867077921163\,10^{-47}$ | 约 $2.39821280171360\,10^{11}$ |
| node11 | 4 | $5.112387223663689\,10^{-56}$ | 小于 $5134.561$ |
| node10 | 4 | $1.0104145830664972\,10^{-55}$ | 小于 $10147.965$ |

这里已经完整包括**全部候选线性 forcing**，不再是第3节的 cut-only
数字。仍须加实际非线性外源

$$
\mathcal I_m(N)=\frac1{S_{0,m}(R)}
\int_b^R (R/r_c)^u\Phi_{01,m}(R,r)
(r/r_c)^u\frac{r^4w}{\sqrt{12}\mu_*}N_H(r)\,dr,
\tag{67.41}
$$

或等价地用 (67.39) 的 source-$x$ 形式。真实候选残差的中心项应是
(67.40)、完整真头 cut correction 和 $\mathcal I_m(N(Y_c))$ 的有符号和，
再为未知外校正保留 $N(Y_*)-N(Y_c)$。

node11/node10 是当前可重设的**内部候选节点**，不是课题额外指定的
外端高度边界。表中数字不证明真正外边值问题不相容。它们准确指出：
只改 cut 动量不足以更新整个外候选中心；应结合实际有符号源和真实
背景传播，一并更新这些内部高度/导数节点，或者在完整外边值方程中
将它们作为待校正变量。

## 8. 执行证据与下一实际入口

主真实流：

- [执行源码](../computations/closure_outer_taylor_shared_flow.py)。
- [完整流包](../notes/2026-11-12-closure-outer-taylor-m2m4-12to10-r1.json)。
- [wait4 资源与真实退出](../notes/2026-11-12-closure-outer-taylor-m2m4-12to10-r1-resource.json)。
- [24件稳定文件清单](../notes/2026-11-12-closure-outer-taylor-flow-stable-manifest.json)。

该子进程 wait4 退出码0、signal 为 null，110.074442 s、峰30,824 KiB。
18个完整 source 段都单独保存可恢复列；旧终端会话句柄过期后，退出
事实由已经写入的 wait4 记录核实，没有把句柄失效猜成成功或失败。

实际 cut/参数/重心化账本：

- [短账本源码](../computations/closure_outer_shared_schur_cut.py)。
- [全部结果与两行46列](../notes/2026-11-12-closure-outer-shared-schur-cut-r1.json)。
- [短账本 wait4 记录](../notes/2026-11-12-closure-outer-shared-schur-cut-r1-resource.json)。

退出码0、0.530611 s、峰29,896 KiB；12个明确门全部通过。
全部输入文件和数学源码都记录 SHA256。整个短账本没有新 source 求积、
新 ODE、Node 或矩阵求逆。

正文21个严格小数上界/下界以及10个 bump 多项式恒等式，另由
[纯 Fraction 源码](../computations/closure_r67_fraction_bounds.py) 对照
[严格有理账本](../notes/2026-11-12-closure-r67-fraction-bounds-r1.json)
正式通过；退出码0、峰11,520 KiB。

(67.40) 的
[独立有理源码](../computations/closure_outer_linear_cancellation.py) 和
[四行完整区间](../notes/2026-11-12-closure-outer-linear-cancellation-r1.json)
也已正式退出0，0.405787 s、峰14,884 KiB，9门全真。该计算直接使用
原完整 M20/13-port response，未改其保存 $Q$。外源积分未付的标志仍是
`false`，没有把有理区间计算当作非线性外求解。

当前直接可执行的下一接口，是原 tail 候选逐 material 面板的完整
$N_x$ 记录器，加上 (67.39) 的有序背景 Green 功能。原候选的线性部分
按 (67.35) 与端点使用同一 $s_m$ 作代数合并；不能先对三项各自取绝对值。
这将支付真实外残差在参数范数中的预算。本文尚未执行该源核，不把
只有 (67.16)/(67.32) 的 cut 数字代替它。
