# R149 补充 IR：原 inverse density 的 96 行与两种全频残差

**状态：已证明（完整残差认证公式及实际目标定义）。** 本文不预报
尚未得到的 actual 数值。会话 `visible-exact-astra-fb31ed6-20261127`，
2026-11-27。

## IR.1 原算子和有限 trial

全部对象与
[DC](R149-supplement-same-sign-density-compression-and-finite-Theta-rows.md)、
[IL](R149-supplement-complete-inverse-density-lift-derivative-bounds.md) 相同。
在物理周期 $\pi/2$ 的归一 Lebesgue 测度下，$N=|D_x|$ 的频率是
$4|n|$，$G=N^{-1}$，$\mathscr H=\dot H^{-1/2}_0$。
原 root-even 基为 $e_j=\sqrt2\cos4jx$，固定相位
$D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_-$ 保留。因此

$$
 b_j=ND_+e_j,\qquad (b_j)_j=2j(1-i),\quad
 (b_j)_{-j}=2j(1+i).                                         \tag{IR.1}
$$

IL 的同一 selected 真 lift 为 $p=\psi^{-1}$；其有限模型
$\widehat p=K_{48}\circ A_-$ 和完整 strip 误差 $E_p$ 直接消费 IL
的完整 actual，绝不重新执行该目标。DC 的精确恒等式为

$$
 C^\dagger=\Pi_+U_p\Pi_++\Pi_-U_p\Pi_-,\qquad
 U_pf=p'f\circ p,\qquad \|(C^\dagger)^{-1}\|_{\mathscr H}\le1.
 \tag{IR.2}
$$

为全部 $j=1,\ldots,96$ 同次选取有限实 trial

$$
 \widehat z_j(x)=\sum_{n=1}^{192}
    \{c_{nj}e^{4inx}+\overline {c_{nj}}e^{-4inx}\},\qquad
 F_j(z)=\sum_{n=1}^{192}\frac{c_{nj}}{4in}e^{4inz}.            \tag{IR.3}
$$

所有 $c_{nj}$ 是保存后读回的精确 binary64 dyadic 数。浮点线性解
仅选择该有限 trial，不提供逆证书，也不作任何反射/正交假设。
全部 96 列必须存在；旧 TC/RW 的 trial 或残差不参与新选择。

由 $U_p\Pi_+\widehat z_j=\partial_x(F_j\circ p)$，正频输出系数
是 $4ik\,(F_j\circ p)_k$。负频输出按共轭补齐，而不是把
$U_p\widehat z_j$ 的正频直接当作 $C^\dagger\widehat z_j$；后一种
做法会错误混入 opposite-sign 项。密度输出的 mean 精确为零。

## IR.2 完整 analytic 像与 alias/tail

固定 $\sigma=1/256$、$L=4096$ 个 exact equispaced 样本、输出
head $K=1024$。令 $H_1$ 为完整旧 W 的
`selected.physical_true_conjugacy_derivative_Astrip_upper`。原单腿
$L_\delta<1/16$ 给出 $|\operatorname {Im}X_-^{-1}(z)|\le16\sigma/15$；
真 $H$ 在实轴取实值，其导数在完整像 strip 上由 $H_1$ 控制，故

$$
 |\operatorname {Im}p(z)|\le {16\over15}H_1\sigma,
 \quad |\operatorname {Im}\widehat p(z)|\le t,
 \qquad t={16\over15}H_1\sigma+E_p.                          \tag{IR.4}
$$

两幅像之间的每条线段也位于 $|\operatorname {Im}w|\le t$。对每列

$$
 M_j=\sum_{n=1}^{192}{|c_{nj}|\over4n}e^{4nt},\qquad
 Z_j=\sum_{n=1}^{192}|c_{nj}|e^{4nt}                         \tag{IR.5}
$$

分别控制完整 $F_j\circ\widehat p$ 和所需 $F'_j$。实际样本用完整
有理 terminal64 与 K48 的 Horner evaluation 求出；每个样本以
Arb ball 保存并读回，再作有向 FFT。有限网格上的最大值从不替代
(IR.5) 的整个 strip 上界。

令 $q=e^{-8\sigma}$、$u=e^{-4\sigma}$。每个 $1\le k\le K$ 的
精确 DFT coefficient 与真 Fourier coefficient 之差至多

$$
 \mathcal A_{jk}=M_j\frac{u^{L-k}+u^{L+k}}{1-u^L}.            \tag{IR.6}
$$

这包含所有整数 alias images；实部、虚部都外向膨胀该界，然后
乘 $4ik$ 并减去 (IR.1) 的完整右端。不是只对 finite Galerkin
matrix 的误差作评估。

两个 complementary tails 为 DC.16 与 DB.27：

$$
 T_{H,j}^2=8M_j^2q^{K+1}
 {K+1-Kq\over(1-q)^2},                                     \tag{IR.7}
$$

$$
 T_{0,j}^2=32M_j^2q^{K+1}\left\{
 {(K+1)^2\over1-q}+{2(K+1)q\over(1-q)^2}
 +{q(1+q)\over(1-q)^3}\right\}.                             \tag{IR.8}
$$

这些系数已包括正、负两 sign 和物理频率4。虽然 $F_j$ 只写正频，
输出正频受同一 analytic bound 控制，而完整实输出的负频是其
共轭，故两倍能量准确如上。原右端全部支于 $1\le|k|\le96$，因此
$K$ 之外无遗漏的 $b_j$ 项。

## IR.3 真 lift 差的两种完整控制

首先，复积分中值式给

$$
 \|F_j\circ p-F_j\circ\widehat p\|_\sigma\le E_p Z_j.
 \tag{IR.9}
$$

在 (IR.7–8) 中取 $K=0$、$M_j=E_pZ_j$ 即分别支付**全频**的
true-map $\mathscr H$ 和 $L^2$ 误差。这里不先截尾再假设模型差
也有限维。

还可合法使用更小的 real-axis 同伦界。因旧 W 的完整 Wiener
derivative norm 包含 degree-one 常数1，$H'\ge2-H_1$。原反向
单腿导数至少 $15/16$，于是

$$
 m_p={15\over16}(2-H_1)\le p',\quad
 \|p'-\widehat p'\|_\infty\le E_p/\sigma,
 \quad m=m_p-E_p/\sigma.                                   \tag{IR.10}
$$

当实际 directed gate $m>0$ 成立，每个
$p_s=(1-s)p+s\widehat p$ 是同周期 degree-one 实 lift，
$p_s'\ge m$。故对任意 complex 周期函数 $f$，换元给
$\|f\circ p_s\|_2\le m^{-1/2}\|f\|_2$。设 $P_1$ 为 IL 已存
$\|\widehat p'\|_\infty$ 上界，写

$$
 U_p\Pi_+\widehat z_j-U_{\widehat p}\Pi_+\widehat z_j
 =(p'-\widehat p')(\Pi_+\widehat z_j)\circ p
 +\widehat p'\{(\Pi_+\widehat z_j)\circ p
                 -(\Pi_+\widehat z_j)\circ\widehat p\}.
$$

沿同伦积分、Minkowski、(IR.10) 以及正频正交投影的 norm1 给

$$
 E_{0,j}^{\rm real}
 ={E_p\over\sqrt m}\left\{
 {\|\widehat z_j\|_2\over\sigma}
       +P_1\|\widehat z_j'\|_2\right\}                    \tag{IR.11}
$$

作为**完整实同号压缩**的 $L^2$ 模型误差。注意此式使用
$\|\widehat z_j\|_2^2=2\sum_n|c_{nj}|^2$，已经包括补负共轭的
$\sqrt2$，不可再删去该因子。完整 $\mathscr H$ 模型误差可取
$E_{0,j}^{\rm real}/2$。若 $m\le0$，该 real bound 不可用，但
(IR.9) 的 analytic bound 仍完整有效；实际入口不得因此改变真对象。
最终每个范数独立取两种已证明上界的较小者。

## IR.4 同一 signed head 得到两种真正全空间残差

令 $r_{kj}$ 是带完整算术和 (IR.6) alias 的正频 coefficient ball。
其负频共轭也完整保留。令 $E_{H,j},E_{0,j}$ 为上一节的最终模型
上界。正交分解给

$$
 \epsilon_{H,j}=\left(
       \sum_{k=1}^K{|r_{kj}|^2\over2k}+T_{H,j}^2\right)^{1/2}
       +E_{H,j},                                            \tag{IR.12}
$$

$$
 \epsilon_{0,j}=\left(
       2\sum_{k=1}^K|r_{kj}|^2+T_{0,j}^2\right)^{1/2}
       +E_{0,j}.                                            \tag{IR.13}
$$

绝对值仅在形成完整有符号 residual coefficient 后使用。两式针对
完全同一个全空间残差 $R e_j=C^\dagger\widehat z_j-b_j$。
于是完整联合算子界为

$$
 \epsilon_H=\left(\sum_{j=1}^{96}\epsilon_{H,j}^2\right)^{1/2},
 \qquad \epsilon_0=\left(\sum_{j=1}^{96}\epsilon_{0,j}^2\right)^{1/2}.
 \tag{IR.14}
$$

这些是 Hilbert–Schmidt 上界，适用于联合 $\ell^2_{96}$ 输入；
后继使用不再额外乘 $\sqrt{96}$。所有96列的完整结果球必须保存、
读回后，才计算 (IR.14)。若只完成 prefix，不授予联合96结论。

## IR.5 实际得到的行及保留的接口

实际输出的目标是
$L=E_{96}^*D_+^{-1}C^{-1}:L^2_0\to\mathbb R^{96}$。
其 trial rows 是 $G\widehat z_j$；DC.13 在 $A=Id$ 时给

$$
 \|L-\widehat L\|_{L^2\to\ell^2}\le\epsilon_H/2,
 \qquad \|L\|_{L^2\to\ell^2}\le\sqrt{96}.                 \tag{IR.15}
$$

它还不是 $V_Q=LA$。只有消费同一个完整 $A=Id-\mathcal T_\alpha I$
后才得到真正 $V_Q$；若 $\alpha$ 用 trial，必须支付 DB.25 的完整
作用差。完整 $\epsilon_H,\epsilon_0$ 可直接进入
[DB.24–27](R149-supplement-complete-Theta-row-regularity-and-negative-window-density-inverse.md)
以支付 $\Theta=V_Q\overline G$ 的一阶损失。原 $\overline G$ 的
normalizers、phase 和 two means 均不因本次计算而消失。

该入口不重跑 IL 四标量，旧169个transport germs、旧KAM、RW96、
TC96、任一旧norm均不执行。新 private grid、全部 trial 系数和每列
完整 Fourier head 都整对象保存读回，只公布小结论与完整 SHA。
结果保留全部原输入 receipt 与同一 selected member 身份，明确
full physical mean/$\nu$/phase Schur、正侧逆链、以及课题完成均未宣称。
