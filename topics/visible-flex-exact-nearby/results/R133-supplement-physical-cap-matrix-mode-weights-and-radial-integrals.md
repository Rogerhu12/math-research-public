# R133 补篇：全物理帽矩阵的逐模源权与连续径向积分

2026-11-14。**已证明：完整96列帽图的有向连续残差算法，以及不丢
mean、不限制耦合输出频率的逐模 Green 计费。** 原完整660块有限
提案已经实际完成；首两个真实闭片的旧粗界也已经执行。本篇的
全域数值图误差须由完整公共闭覆盖实际算出，不由有限 QR 成功授予。

## 1. 对象和原范数

本篇使用原 ac1 的准确连续修复定义
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`，
固定原 $\alpha,\nu$，并保仿射参数

$$
 \eta=\eta_0+\delta\eta,\qquad
 \eta_0=-\frac{7789843107295549}{4611686018427387904},
 \qquad |\delta\eta|\le10^{-9}.
 \tag{W.1}
$$

帽区 $I=[L,R]=[9/10,25/8]$，所有角均为真实物理角 $\theta$。
记 $\mathfrak M=\ell^2_{k\in4\mathbb Z}(C(I))$，即每个 Fourier
系数先取径向 supremum，再平方求和；双状态使用两个
$\mathfrak M$ 范数之和。输入 $a\in\mathbb R^{96}$ 使用普通
$\ell^2$ 范数，左迹为

$$
 Ja=\sum_{j=1}^{96}a_j\cos(4j\theta),\qquad
 \|Ja\|_{L^2_\theta}=\|a\|_2/\sqrt2.
 \tag{W.2}
$$

因此如果把输入重新按物理 $L^2$ 单位归一，本篇所有矩阵误差界
另乘 $\sqrt2$。输出的非零 sine/cosine Gram 为 $1/2$，mean 的
Gram 为 $1$，没有把均值当成 $M=0$ 的非零模公式极限。

完整源、边界与图误差的基础合同见
[物理帽矩阵图与连续残差](R133-supplement-physical-cap-matrix-graph-and-continuous-residual-contract.md)。
修复后的实际全模 Green 与完整非线性 exterior 导数见
[连续中心物理帽](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)。

## 2. 逐模权只作用于参考源列

旋转参考的两条严格正速率记为 $s_D,s_C$，完整径向图上
$q_M\le q_+$，三角核常数为 $T$。已执行的整帽报告给

$$
 q_+<1.389936764,\quad T<3.625263015,\quad
 s_D>2.9252958741,\quad s_C>.8601652212.
 \tag{W.3}
$$

置 $H_D=1+(1+q_+)T$、$H_C=1+q_+$。对每个真实物理
$M=|k|\ge4$，参考普通径向源的核满足

$$
 G_B(M)\le\frac{H_D}{\sqrt{2Ms_D}},\qquad
 G_C(M)\le\frac{H_Dq_+}{\sqrt{2Ms_D}}
             +\frac{H_C}{\sqrt{2Ms_C}}.
 \tag{W.4}
$$

证明是在实际逐模正指数核中应用 Cauchy–Schwarz：
$\int_0^\infty e^{-2Ms t}dt=(2Ms)^{-1}$。真实变系数核的
指数不大于此核，已经支付的三角列分别乘 $H_D,H_C$。两侧
积分方向及 $q_M$ 的真实 regular 右迹沿用同一参考，未重定义帽。

令 $\mathcal R<5.571744$ 为修复后**完整无权双状态**反馈逆。
于是 finite nonmean 源可以先按

$$
\begin{aligned}
 g_B&=\mathcal R H_D/\sqrt{2s_D},\\
 g_C&=\mathcal R\big[H_Dq_+/\sqrt{2s_D}
                         +H_C/\sqrt{2s_C}\big]
\end{aligned}
\tag{W.5}
$$

乘 $\||D_\theta|^{-1/2}f_{\ne0}\|_{L^2_rL^2_\theta}$。
所有 mean 源仍以原独立 mean 核计费。unknown coefficient
remainder 若没有逐模分布，仍使用原无权 ordinary 或 divergence
源列。

这里没有声称完整反馈保持 high 模。准确的顺序是：参考 Green
把带权的已知源送到原 $\mathfrak M^2$，再用同一个完整
$(1-\mathcal K)^{-1}$。$\mathcal K$ 的全部乘法、mean、低高互馈
和真实外端图均未截去。由此即使初始源仅在高频，后续产生的低频
与 mean 也已经在 $\mathcal R$ 中支付。

## 3. 提案与连续闭覆盖

有限提案保存所有节点的同一组 dyadic 状态 $Y_i$ 和两侧导数
$D_i^+,D_{i+1}^-$。每片使用准确有理 Hermite 公式

$$
 \widehat Y=Y_i+hD_i^+t+
 [3(Y_{i+1}-Y_i)-h(2D_i^++D_{i+1}^-)]t^2+
 [2(Y_i-Y_{i+1})+h(D_i^++D_{i+1}^-)]t^3.
 \tag{W.6}
$$

$h$ 是两个真实 dyadic 节点的准确有理差。相邻片共享相同 $Y_i$，
所以提案和全部角导在径向接口准确连续；导数可有已知单侧变化，
一阶算子不因此新增点源。真实 $9/10$ 与 double `.9` 的微小差
作为第一段首片延拓保留，并在准确 $L$ 重新计算左边界误差。

计算网格为提案所有节点、原连续中心所有 cubic 接口及完整 scalar
target 的所有 germ 接口的并。每个闭片只使用一个实际 Hermite
多项式、一个原中心片和一个真实 target germ。whole-$\eta$、所有
primitive 尾与精确 continuous repair offsets 一起保留。增加有限
提案节点只改变提案；不能把加密本身当作连续门通过。

## 4. 真实物理系数及无限余项

闭片以 $z\in[-1,1]$ 参数化。已经证明并实际运行的
[物理逆角径向 Fourier jets](R133-supplement-physical-cap-inverse-angle-radial-Fourier-jets.md)
给出

$$
 q_B=\widehat q_B+E_B,\qquad q_C=\widehat q_C+E_C,
 \quad\|E_B\|_{\mathcal A^0(C_r)}\le\epsilon_B,
 \quad\|E_C\|_{\mathcal A^0(C_r)}\le\epsilon_C.
 \tag{W.7}
$$

$\widehat q$ 是径向二次、物理 Fourier 支集 $|j|\le128$ 的准确
dyadic 模型；所有逆角、定向 FFT、alias、$|j|>128$ 真尾、三阶
径向 Taylor 余项和 whole-$\eta$ 宽度均包含在 $E$ 中。
这不是把有限 moving Fourier 称作有限 physical Fourier。

真实 scalar $\gamma,\beta,K,s$ 也以有限 dyadic 多项式加完整
uniform error 表示。若相乘产生次数高于3的 scalar 模型，新的
consumer 把每个被省略系数的绝对值之和完整加入误差，保留次数
至3。这只是准确的预算恒等式，不删除其数学效应。

记 $a=\gamma Ks^2$、$e=\beta(Ks^2+1)$，模型范数与误差分别为
$N_a,\epsilon_a$ 等。有限提案两分量在本片的列平方 module 界为
$B_*,C_*$。置

$$
 Q_* =N_{q_B}B_*+N_{q_C}C_*,\qquad
 E_* =\epsilon_B B_*+\epsilon_C C_*.
 \tag{W.8}
$$

这些都是先对每个 Fourier 槽取径向 supremum，再对槽与全部96
输入列平方求和的上界。乘法使用完整
$\ell^1(C_r)*\ell^2(C_r)\to\ell^2(C_r)$；没有交换
$\sup_r$ 与求和的顺序。

## 5. 完整有限残差和 ordinary/divergence 分裂

定义模型 $\widehat Q=\widehat q_B\widehat b+
\widehat q_C\widehat c$。有限 ordinary 多项式为

$$
\begin{aligned}
 F_B&=\widehat b_r+2\widehat\beta\widehat b
       +\partial_\theta(\widehat a\widehat c
                              -\widehat\gamma\widehat Q),\\
 F_C&=\widehat c_r+\widehat e\widehat c
       -\widehat\beta\widehat Q
       -\partial_\theta(\widehat\gamma\widehat b).
\end{aligned}
\tag{W.9}
$$

提案支集 $|j|\le96$，系数支集 $|j|\le128$，因此所有这些
有限乘积有 $|j|\le224$。$N=512>448$ 的 directed FFT 完整计算
它们；频率97至224必须保留。准确反射奇偶性分别给 $F_B$ 的零
mean/纯虚 Fourier 和 $F_C$ 的纯实 Fourier；删除某槽之前程序
先确认其计算区间包含准确零。它没有把任意非零尾置零。

剩余 ordinary 列的无权 module 界为

$$
\begin{aligned}
 r_{B,\mathrm{err}}&\le2\epsilon_\beta B_*,\\
 r_{C,\mathrm{err}}&\le\epsilon_e C_*+
             \epsilon_\beta Q_*+(N_\beta+\epsilon_\beta)E_*.
\end{aligned}
\tag{W.10}
$$

剩余 divergence 原函数列的界为

$$
 d_B\le\epsilon_a C_*+\epsilon_\gamma Q_*+
                   (N_\gamma+\epsilon_\gamma)E_*,\qquad
 d_C\le\epsilon_\gamma B_*.
 \tag{W.11}
$$

证明直接展开真实系数减模型的乘积；例如
$\gamma Q-\widehat\gamma\widehat Q
=(\gamma-\widehat\gamma)\widehat Q+\gamma(Q-\widehat Q)$。
未知 Fourier 余项在第一行留在 $\partial_\theta$ 之内，用已经
支付的 divergence Green，绝不对没有另付角导数的 $E$ 求导。

## 6. 准确径向积分，完整 Fourier Gram

设某有限残差为 $F(z)=\sum_{n=0}^d F_nz^n$。使用准确转换

$$
 z^n=\sum_{\substack{0\le k\le n\\n-k\text{ even}}}
 \frac{(2k+1)n!}{(n-k)!!(n+k+1)!!}P_k(z).
 \tag{W.12}
$$

令相应 Legendre 系数为 $L_k$。正交性给

$$
 \frac12\int_{-1}^1\|F(z)\|^2dz
      =\sum_{k=0}^d\frac{\|L_k\|^2}{2k+1}.
 \tag{W.13}
$$

式中范数可为完整 Fourier/输入列平方和，也可先乘准确非零模
权 $|M|^{-1/2}$，或只取完整 even mean。每个转换系数通过有理数
进入 Arb 外舍区间，随后正项平方和给上界。没有把径向采样点的
残差当成连续积分，也没有把 $z-z^3$ 两项分别绝对值后遗失其真实
抵消。原 source 的粗逐次数绝对值界仍是正确上界；本式给出更紧
的同一个真实多项式积分。

完整普通源空间是 Hilbert 空间，所以全部96列平方和给标准
Hilbert–Schmidt 上界。$\mathfrak M$ 本身不是 Hilbert 空间；
对它所用的是列平方预算
$\|Ta\|\le\sum_j|a_j|\|Te_j\|\le
\|a\|_2(\sum_j\|Te_j\|^2)^{1/2}$。两者都保留非零模
$1/2$ 与 mean $1$ 的 Gram。

## 7. 全域汇总与全部真实外行

每个有限普通源的 (W.13) 乘真实片长后在闭覆盖上相加；同理累计
ordinary coefficient error 的片长乘平方。各片 divergence module
上界 $d_i$ 则可用 $\sqrt{\sum_i d_i^2}$：对每个模及输入列，
全域的径向最大值平方不超过各片最大值平方和，再交换非负求和。
这通常偏粗，但确实是所需 $\ell^2(C_r)$ 上界，不是
$L^2_r\ell^2$ 的替代。

左迹在准确 $L$ 评估 (W.6)，减去全部96列的单位 cosine 输入。
右迹保全部96条物理 Robin、真实 $q_M-q_M^{\rm proposal}$ 费和
完整 nonlinear regular 导数的无限输出。现已付的 uniform 真费为

$$
 \|D\mathcal N\|_{L^2\to L^2}<5.898255\cdot10^{-6},\qquad
 \|D\mathcal N_0\|_{L^2\to\mathbb R}<7.372818\cdot10^{-7}.
 \tag{W.14}
$$

另外保 actual $q_*$ 的 native 区间与每个浮点 proposal 的准确
dyadic 差，并加已付 $2^{-512}$ 真径向线费。外 even mean 的
提案值不清零。反射给 $b_0=0$；本篇不授任意非反射数据。

将 (W.5) 乘两个 finite weighted ordinary 累积量，将原独立
mean Green 乘有限 mean 累积量，再将 (W.10)–(W.11) 与全部
左右边界费代入原全模 Green，得到

$$
 \|S-\widehat S\|_{\ell^2_{96}\to\mathfrak M^2}
 \le\varepsilon_{\rm cap}.
 \tag{W.15}
$$

左迹同样给完整无限输出帽图误差。即使提案只有96输出模，
$j>96$ 的真输出仍在 (W.15) 内。完整均值/高低耦合已在原无权
resolvent中支付，因此 (W.15) 没有遗留重新返回原单位的步骤。

## 8. 实际执行范围和下一数值门

原完整660块/96列提案的实际 FFT 相对残差为
$5.7051555493294925\cdot10^{-15}$。首两个原连续片已实际正常
退出：第一片仅是准确 $9/10$ 到 double `.9` 的微片，第二片宽
约 $1/1200$。旧粗 ordinary 累积界在第二片后为
$6.450629174$、$5.073453522$；未知系数 divergence 余项仅为
$4.142471\cdot10^{-7}$、$2.949120\cdot10^{-9}$。

已保存的真实最高输入导数显示入口衰减率约1508，原片长使
$\lambda h\approx1.26$。这解释有限节点门很小而三次 Hermite
连续残差仍大的原因；该粗报告原样保留。新的有限提案只在入口
邻域分片加密，保原96列、193状态、全部接口、true mean/第四
Robin 和同一个原后向门。任何新图误差仍须实际执行完整闭覆盖。

算法的实际独立核包括非恒定径向多项式 $z-z^3$、96完整列及
物理模28；(W.13) 的准确无权平方为 $128/35$，带权平方为
$32/245$，directed 结果均从外侧包含。该核只验证新径向积分与
Gram/频率权的实现，不替代本候选全域运算。

source 为 `fourfold_codazzi_physical_cap_matrix_residual.py`（原粗界）
和新 `fourfold_codazzi_physical_cap_matrix_residual_v2.py`。新的
`fourfold_codazzi_physical_cap_DN_refined_proposal.py` 只是明确局部
径向网格的有限提案。所有报告将各自保存真实 kind/source/参数/
范围；未完成全域时 `complete` 保持 false。moving–physical
残差敏感接线与帽之外的完整主体逆仍是独立消费，不在本篇偷授。
