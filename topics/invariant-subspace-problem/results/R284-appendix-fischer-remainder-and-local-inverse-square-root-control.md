# R284 附录：真实零占据费用的 Fischer 余量与不损失外尾的局部强制性

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：已证明。** 本文接续 [跨出生零占据 Gram](R284-cross-birth-zero-occupation-grams-and-exact-schur-lower-bound.md) 及 [有限正权严格性](R284-appendix-strict-positivity-of-boolean-zero-occupation-compressions.md)。第一部分从真正逐坐标平方零得到二阶零占据费用的一个明确 Fischer 正余量；第二部分证明固定物理位上的整个测试块具有与所有外尾无关的强制性，并给单坐标显式常数。无限维的逆结论只涉及 $X^{-1/2}$ 能量，不擅自宣称 $X^{-1}$ 定义于该测试或完整逆有界。

## 1. 有限位数下的真实 Fischer 正余量

### 1.1 集体模式与 transverse Laplacian

本节取 $M<\infty$、$b_i>0$、$\sum b_i^2=1$。在标准 bosonic Fock 嵌入中，设
$$
a_0=\sum_i b_i a_i,\qquad c_i=a_i-b_i a_0,
\qquad d=M-1.
$$
则 $\sum_i b_i c_i=0$，$[c_i,c_j^*]=\delta_{ij}-b_ib_j$。在 transverse Fock 空间上记
$$
\Delta_\perp=\sum_i c_i^2,\qquad
\mathcal Q_\perp^*=\sum_i(c_i^*)^2.
$$
它们分别是在任一实正交 transverse 基中的 Laplacian 与其伴随，因此
$$
[\Delta_\perp,\mathcal Q_\perp^*]=4\mathcal N_\perp+2dI.
\tag{1.1}
$$
每个实际 Boolean 向量都满足全部 $a_i^2x=0$，从而特别满足
$$
\left(a_0^2+\Delta_\perp\right)x
=\left(\sum_i a_i^2\right)x=0.
\tag{1.2}
$$
这一步用到了真正硬核约束；对一般共同 annihilator 不变空间并不成立。

取合法出生 $s\ge0$，并要求二阶完整最小逆存在，即 $M\ge2s+2$。按主稿记号，
$$
\mathcal J_{j,s}=(D^j/j!)^\dagger|_{K_s},\quad
G_j=\mathcal J_{j,s}^*\mathcal J_{j,s},\quad
U_s=P_0\mathcal J_{1,s},\quad Z_{2,s}=P_0\mathcal J_{2,s}.
$$
源 $f\in K_s$ 位于 occupation 零部分，且 $\Delta_\perp f=0$。将 (1.2) 用到
$$
\mathcal J_{1,s}f=|1\rangle f+|0\rangle U_sf
$$
给
$$
\Delta_\perp U_sf=0.
\tag{1.3}
$$
将其用到真正二阶展开
$$
\mathcal J_{2,s}f
=\sqrt2|2\rangle f+|1\rangle(2U_s-B_s^*G_2)f
+|0\rangle Z_{2,s}f,
$$
其中 $B_s=(\sum b_i^3E_i)|_{K_{s+1}}$，取 occupation 零分量，准确得到
$$
\boxed{\Delta_\perp Z_{2,s}f=-2f.}
\tag{1.4}
$$

### 1.2 完整正交分解和定量下界

因为 $\Delta_\perp f=0$ 且 $f$ 次数为 $s$，(1.1) 给
$$
\Delta_\perp\mathcal Q_\perp^*f=2(2s+d)f.
$$
所以存在唯一由下式定义的 transverse harmonic 余项 $\mathcal H_sf$，使
$$
\boxed{Z_{2,s}f=-\frac{\mathcal Q_\perp^*f}{2s+d}
+\mathcal H_sf,\qquad \Delta_\perp\mathcal H_sf=0.}
\tag{1.5}
$$
$\operatorname{Ran}\mathcal Q_\perp^*$ 与 $\ker\Delta_\perp$ 正交，而
$$
\|\mathcal Q_\perp^*f\|^2=2(2s+d)\|f\|^2.
$$
故这是实际正交分解，并且
$$
\boxed{X_2:=Z_{2,s}^*Z_{2,s}
=\frac{2}{M-1+2s}I+\mathcal H_s^*\mathcal H_s.}
\tag{1.6}
$$
结合主稿的准确二阶费用身份，
$$
\boxed{
G_2=4G_1-2I+G_2B_sB_s^*G_2
+\frac{2}{M-1+2s}I+\mathcal H_s^*\mathcal H_s.
}
\tag{1.7}
$$
特别
$$
G_2\succeq4G_1-2I+\frac{2}{M-1+2s}I.
\tag{1.8}
$$
若原权平方和是 $S$ 而未归一，则对原 Gram 的 (1.8) 为
$$
\Gamma_2\succeq\frac4S\Gamma_1-\frac2{S^2}I
+\frac{2}{S^2(M-1+2s)}I.
$$
该明确余量依赖 $M,s$，可在增长维数时趋零。本文没有证明它连同桥项和 harmonic 余项支配一般首边所需的二次增长 $G_1^2-4G_1+2I$。

## 2. 固定物理位的局部强制性：外尾完全不进入常数

本节的物理位可以是有限集，也可以是可数无限集。令实正权 $b$ 为非零 $\ell^2$ 向量，整体归一 $\|b\|_2=1$；固定粒子数 $p$，$\mathcal H_p$ 是标准平方自由层。令
$$
W=b^\perp,\qquad P_0=\operatorname{Sym}^p(P_W),\qquad
\mathsf E_p=P_{\mathcal H_p}P_0|_{\mathcal H_p}.
$$
这是 collective mode 的真正零占据压缩；在无限维中仍有 $0\preceq\mathsf E_p\preceq I$。

### 2.1 整个有限局部块的算子不等式

任取有限物理位集 $F$，要求 $b_i>0$（$i\in F$），定义
$$
W_F=\{v:\operatorname{supp}v\subseteq F,\ \langle b_F,v\rangle=0\}.
$$
因为 $W_F\subseteq W$，其 bosonic 第 $p$ 对称幂投影满足
$$
P_{\operatorname{Sym}^p W_F}\preceq P_0.
$$
将其压回整个平方自由层。左边消灭带有 $F$ 外占据的全部坐标；在 $\mathcal H_p(F)$ 上，它恰是使用**局部归一权** $b_F/\|b_F\|_2$ 的零占据压缩，记作 $\mathsf E_p^F$。若 $\iota_F:\mathcal H_p(F)\hookrightarrow\mathcal H_p$ 为实际等距嵌入，则
$$
\boxed{\mathsf E_p\succeq\iota_F\mathsf E_p^F\iota_F^*.}
\tag{2.1}
$$
当 $2\le p\le|F|$，有限正权严格性给 $\mathsf E_p^F>0$。令
$c_F=\lambda_{\min}(\mathsf E_p^F)>0$，得到
$$
\boxed{\mathsf E_p\succeq c_F P_{\mathcal H_p(F)}.}
\tag{2.2}
$$
$c_F$ 只依赖 $F$ 内相对权和固定 $p$；所有外部物理位、它们的权、外尾长度都不进入这个常数。这里没有把 $F$ 内源投影改成某个 primitive 投影。

### 2.2 单一物理坐标的显式常数

取一个含 $p\ge2$ 个物理位的集合 $I=\{i_0,\ldots,i_{p-1}\}$。令 $\omega=e^{2\pi i/p}$，取
$$
v_{i_r}=\frac{\omega^r}{b_{i_r}},\qquad v_i=0\quad(i\notin I).
$$
因为 $\sum_{r=0}^{p-1}\omega^r=0$，有 $v\in W$。标准单位 bosonic 向量
$$
k_v=\frac{(a^*(v))^p\Omega}{\sqrt{p!}\,\|v\|^p}
$$
属于 $\operatorname{Sym}^pW$。它在平方自由层上的投影只有一个物理坐标：
$$
P_{\mathcal H_p}k_v
=\frac{\sqrt{p!}\prod_{i\in I}v_i}{\|v\|^p}\,e_I.
$$
因此将 $|k_v\rangle\langle k_v|\preceq P_0$ 压回平方自由层，得到
$$
\boxed{
\mathsf E_p\succeq c_I|e_I\rangle\langle e_I|,
\qquad
c_I=\frac{p!\prod_{i\in I}b_i^{-2}}
{\left(\sum_{i\in I}b_i^{-2}\right)^p}>0.
}
\tag{2.3}
$$
这是可直接复算的常数，同样只依赖 $I$ 内的相对权。对任意平方自由 $x\in\mathcal H_p$，其等价二次型表述为
$$
|\langle x,e_I\rangle|^2\le c_I^{-1}\|P_0x\|^2.
\tag{2.4}
$$
固定 $I,p$ 的结论不应改写成所有增长出生的统一常数；例如 $I$ 内等权时该明确常数为 $p!/p^p$。

### 2.3 对完整最小逆拉回测试的准确逆能量结论

令 $J:\mathcal K\to\mathcal H_p$ 为任意有界线性映射，定义
$$
X=J^*\mathsf E_pJ,\qquad z_I=J^*e_I.
$$
由 (2.3)，
$$
X\succeq c_I|z_I\rangle\langle z_I|.
\tag{2.5}
$$
此式直接给
$$
\boxed{z_I\in\operatorname{Ran}X^{1/2},\qquad
\|X^{-1/2}z_I\|^2\le c_I^{-1}.}
\tag{2.6}
$$
这里 $X^{-1/2}$ 取在 $(\ker X)^\perp$ 上的标准逆平方根。为完整说明无限维范围：由 (2.5)，
$$
|\langle z_I,f\rangle|\le c_I^{-1/2}\|X^{1/2}f\|.
$$
所以 $X^{1/2}f\mapsto\langle z_I,f\rangle$ 在 $\operatorname{Ran}X^{1/2}$ 上定义一个有界泛函；延拓到其闭包并使用 Riesz 表示，得到范数至多 $c_I^{-1/2}$ 的 $g\in(\ker X)^\perp$，满足 $z_I=X^{1/2}g$。这证明真实的 range 结论及 (2.6)，不只是在闭包中的结论。

等价地，
$$
\sup_{\varepsilon>0}\langle(X+\varepsilon I)^{-1}z_I,z_I\rangle
\le c_I^{-1}.
\tag{2.7}
$$
有限维且 $X>0$ 时可写为 $\langle X^{-1}z_I,z_I\rangle\le c_I^{-1}$。在一般无限维中，(2.6) **不**自动给 $z_I\in\operatorname{Dom}X^{-1}$，也不给完整 $X^{-1}$ 有界。

整个局部块也不损失维数：由 (2.2)，对每个 $w\in\mathcal H_p(F)$，
$$
J^*\iota_Fw\in\operatorname{Ran}X^{1/2},\qquad
\|X^{-1/2}J^*\iota_Fw\|^2\le c_F^{-1}\|w\|^2.
\tag{2.8}
$$
该估计直接针对同一个固定物理测试块，不经过完整条件数。

对实际 $J=\mathcal J_{1,s}$ 或 $\mathcal J_{2,s}$，$X$ 分别是主稿的 $G_1-I$ 或 $X_2$；此时 (2.6)、(2.8) 控制的是**这些真正完整最小逆的伴随拉回物理测试**。尚未证明原 graph $\Gamma=T^*T=I+S^*S$ 的相关测试可以不付额外费用地识别成这里的 $J^*e_I$。因此本文不把这条局部逆平方根估计直接代入原负前缀 graph 正规方程，也不据此宣布原边界 $N=M$。
