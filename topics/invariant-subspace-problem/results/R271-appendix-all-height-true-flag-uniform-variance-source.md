# R271 补录：任意高度最低 forcing 的完整真旗、方差一致残余与全部受限逆费用

日期：2026-11-26。作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted GPT-6 Astra Pro。

状态：以下明确范围已证明。本条把三阶真旗的方差无损结论推广到任意有限高度，并给出原 N 头所有奇高度 $r\ge3$ 的实际常数。证明保留完整物理 Galerkin、全部真实幂核旗和环境伴随，不把低 forcing 当作低输出。原物理孔加权 $\mathcal Z_\gamma$、整个最高 carry 费用及普通 ISP 仍未完成。

父结论为[三阶真旗及方差一致界](R271-appendix-lowest-source-true-flag-schur-and-uniform-variance-residual-cost.md)、[最高单位因子不改变完整真核](R271-appendix-highest-unit-invariant-true-kernel-and-graded-physical-energy.md)、[任意奇高度的完整高孔费用](R271-appendix-general-odd-height-hankel-congruence-and-complete-high-hole-cost.md)。本条不重算这些已登记结论。

## 1. 抽象问题与真实幂旗

设 $C$ 是有限维 Hilbert 空间上的算子，$F$ 是其不变子空间，且
$$
C^rF=0,\qquad r\ge2,\qquad f\in F\cap\ker C^2.
\tag{1.1}
$$
对 $0<S\le1$，定义
$$
H_S=\sum_{j=0}^{r-1}\frac{(C^*)^jC^j}{j!S^j},\qquad
a_S\in F,\qquad P_FH_Sa_S=f,
$$
$$
\xi_S=f-H_Sa_S.
\tag{1.2}
$$
这里 $H_S\ge I$，故唯一解满足 $\|a_S\|\le\|f\|$，且 $\xi_S\perp F$。

按原物理内积作完整正交分解
$$
W_i=(F\cap\ker C^{i+1})\ominus(F\cap\ker C^i),
\qquad 0\le i\le r-1,
\tag{1.3}
$$
其中 $\ker C^0=\{0\}$，于是 $F=\bigoplus_iW_i$。所有零维块直接省去。

记
$$
E_{ji}=C^j|_{W_i}\quad(1\le j\le i),\qquad
\beta_j=\|(C^j|_F)^\dagger\|.
\tag{1.4}
$$
若 $W_i\ne0$，则 $E_{ii}$ 单射，而且
$$
E_{ii}^*E_{ii}\succeq\beta_i^{-2}I_{W_i}.
\tag{1.5}
$$
原因是 $W_i\subset F\ominus\ker(C^i|_F)$；没有用较大的环境核替换受限核。

固定 $c\ge\max(1,\|C\|)$，选择
$$
0<\alpha\le1,\qquad
\alpha\le\frac1{i!\beta_i^2}\quad(W_i\ne0),
$$
$$
A_r(c)=1+\sum_{j=1}^{r-1}\frac{c^{2j}}{j!},\qquad
L=4A_r(c)/\alpha+2.
\tag{1.6}
$$
这些量均与 $S$ 无关，且 $L\ge6$。若 $F=W_0$，则 $a_S=f$、$\xi_S=0$，以下不等式仍成立。

## 2. 完整最低来源的全方差定量界

### 定理 2.1

在 (1.1)–(1.6) 下，对全部 $0<S\le1$ 及 $1\le j\le r-1$，
$$
\boxed{\frac{\|C^ja_S\|}{S^j}\le c^jL^{2j}\|f\|.}
\tag{2.1}
$$
因而原环境中的完整残余满足
$$
\boxed{
\|\xi_S\|\le
\left[2+\sum_{j=1}^{r-1}\frac{(c^2L^2)^j}{j!}\right]\|f\|
\le\left[2+(1+c^2L^2)^{r-1}\right]\|f\|.
}
\tag{2.2}
$$

**证明。** 写 $f=f_0+f_{(1)}$，其中 $f_0\in W_0$、$f_{(1)}\in W_1$。$W_0$ 在完整压缩 $P_FH_S|_F$ 中与其余块正交，因为 $C^jW_0=0$ 对 $j\ge1$ 成立。因此 $P_{W_0}a_S=f_0$。以下只在 $F_+=\bigoplus_{i=1}^{r-1}W_i$ 工作。

令 $u=\sqrt S$，$D_u|_{W_i}=u^iI$。完整压缩能量的合同
$$
K_u=D_u(P_FH_S|_{F_+})D_u
\tag{2.3}
$$
具有块
$$
(K_u)_{ik}=\delta_{ik}u^{2i}I+
\sum_{j=1}^{\min(i,k)}
\frac{u^{i+k-2j}}{j!}E_{ji}^*E_{jk}.
\tag{2.4}
$$
所有原跨旗项都在这条公式内。其对角块 $B_i=(K_u)_{ii}$ 满足 $B_i\succeq\alpha I$；对 $i\ne k$，
$$
\|(K_u)_{ik}\|\le A_r(c)u^{|i-k|}.
\tag{2.5}
$$
这是由于 $0<u\le1$ 且 $i+k-2j\ge|i-k|$。

先考虑 $S\le L^{-2}$。用块标量权
$$
Z_u|_{W_i}=(uL)^{-(i-1)}I
\tag{2.6}
$$
共轭 (2.3)。设 $B=\operatorname{diag}(B_i)$，$O=K_u-B$。当 $i>k$ 时，$Z_uB^{-1}OZ_u^{-1}$ 的 $(i,k)$ 块范数至多
$\alpha^{-1}A_r(c)L^{-(i-k)}$；当 $i<k$ 时，至多
$\alpha^{-1}A_r(c)(SL)^{k-i}$。因此每个块行与块列的范数和都不超过
$$
\frac{A_r(c)}\alpha
\left(\frac1{L-1}+\frac{SL}{1-SL}\right)
\le\frac{2A_r(c)}{\alpha(L-1)}<\frac12.
\tag{2.7}
$$
块 Schur 范数估计可直接由 Cauchy–Schwarz 证明：若块范数矩阵的行和、列和分别至多 $a,b$，则整个算子范数至多 $\sqrt{ab}$。故 (2.7) 使完整共轭方程的 Neumann 逆范数至多 $2/\alpha$。这里的 Neumann 展开作用于有界的完整真旗矩阵，未替换任何核或来源。

写 $a_S-f_0=D_ub$。完整方程成为
$$
K_ub=D_uf_{(1)}=u f_{(1)}.
$$
右端只在 $W_1$，而 $Z_u$ 在该块等于恒等。于是
$$
\|P_{W_i}a_S\|
\le\frac2\alpha S^iL^{i-1}\|f\|,
\qquad i\ge1,\quad S\le L^{-2}.
\tag{2.8}
$$
由 $C^jW_i=0$ 对 $i<j$，
$$
\begin{aligned}
\frac{\|C^ja_S\|}{S^j}
&\le\frac{2c^j}{\alpha}L^{j-1}
\sum_{i=j}^{r-1}(SL)^{i-j}\|f\|\\
&\le\frac{3c^j}{\alpha}L^{j-1}\|f\|
\le c^jL^{2j}\|f\|.
\end{aligned}
\tag{2.9}
$$
第二步使用 $L\ge6$，最后一步使用 $L\ge4/\alpha+2$。

若 $S\ge L^{-2}$，直接用 $\|a_S\|\le\|f\|$ 得
$S^{-j}\|C^ja_S\|\le c^jL^{2j}\|f\|$。这证明 (2.1) 对整个实区间成立。最后在 (1.2) 中使用完整环境伴随 $C^*$，得到 (2.2)。证毕。

本定理没有把 $S\to0$ 的固定参数渐近当成实际 $S$ 处的费用；大、小 $S$ 两段都已支付。

## 3. 原残余在零方差的完整真旗 Green 递推

除了定量界，还可给出精确极限。对 $i\ge1$ 写
$$
P_{W_i}a_S=S^iz_i(S).
$$
原完整方程中乘入这条尺度后，各 $(i,k)$ 块都是 $S$ 的非负整数次多项式。在 $S=0$ 处它是下三角块矩阵，对角块为 $E_{ii}^*E_{ii}/i!$，均可逆。因此所有 $z_i(S)$ 在 $S=0$ 附近解析。

定义 $v_i=E_{ii}z_i(0)/i!$。下三角方程等价于
$$
\boxed{
v_1=(E_{11}^\dagger)^*f_{(1)},\qquad
v_i=-(E_{ii}^\dagger)^*
\sum_{k=1}^{i-1}E_{ki}^*v_k\quad(2\le i\le r-1).
}
\tag{3.1}
$$
$(E_{ii}^\dagger)^*$ 是从 $W_i$ 到 $\operatorname{Ran}E_{ii}$ 的真正最小逆；右端没有环境逆的替换。

由于 $C^j$ 杀掉 $W_i$ 中 $i<j$ 的分量，有
$$
\frac{C^ja_S}{j!S^j}\longrightarrow v_j,
\qquad
\boxed{\xi_S\longrightarrow
\xi_{\mathrm{lim}}=f_{(1)}-\sum_{j=1}^{r-1}(C^*)^jv_j.}
\tag{3.2}
$$
仍使用完整环境 $C^*$，因此这条极限保留所有核外输出。

例如 $r=3$ 时，$v_1=u$、$v_2=-(BD)^{\dagger *}E^*u$，恰恢复父稿的两条 Green 列及其符号。

从 (3.1) 还得到更锐的零方差极限界
$$
\boxed{
\|\xi_{\mathrm{lim}}\|
\le\left[1+c\beta_1\prod_{i=2}^{r-1}(1+c^i\beta_i)\right]\|f\|.
}
\tag{3.3}
$$
证明是令 $M_i=\sum_{k=1}^i c^k\|v_k\|$，则
$M_1\le c\beta_1\|f\|$，
$M_i\le(1+c^i\beta_i)M_{i-1}$。
式 (3.3) 只估精确极限，不能替代 (2.2) 的全区间界。

## 4. 原 N 头的全部受限真旗逆

现在取原参数
$$
m\ge5,\quad n=2^{m-1},\quad d=2n,\quad a=16^{m-2},
$$
$$
R\ge d\text{ 为偶数},\quad r\ge3\text{ 为奇数},\quad y=m+R/2.
\tag{4.1}
$$
令 $C_0$ 为原最高 carry $t=0$ 的完整头加全部强位，
$F_0=\lim_{t\downarrow0}\ker C_t^r$。由原最低 forcing 的准确恒等式 $C_t^2f_1=0$，有
$$
f_1\in F_0\cap\ker C_0^2,\qquad C_0F_0\subset F_0,
\qquad C_0^rF_0=0.
\tag{4.2}
$$
这里的 $f_1=e_1\otimes\Omega$ 是最低整数坐标，不是任意一孔列。

最高单位不变定理允许在只作旧头相似后计算同一个 $F_0$。在单位奇尾链 $J_l$ 上使用
$$
C_\circ=J_n+bE_{\rm high}+J_l,\quad b=m^{-2},\qquad
N_\circ=E_{\rm high}\otimes E_{n-1,0},
$$
$$
X_0=C_\circ^r,\qquad
X_1=\left.\partial_t(C_\circ+tN_\circ)^r\right|_{t=0}.
\tag{4.3}
$$
完整奇高度简单极点保证
$$
F_\circ=\{x:X_0x=0,\quad X_1x\in\operatorname{Ran}X_0\}.
\tag{4.4}
$$
对 $1\le j\le r-1$，完整整数约束矩阵为
$$
\mathcal J_j=
\begin{pmatrix}X_0&0\\X_1&X_0\\C_\circ^j&0\end{pmatrix}.
\tag{4.5}
$$
对任意 $x\in F_\circ$ 选兼容 $z$，有
$\mathcal J_j(x,z)=(0,0,C_\circ^jx)$。
将 $(x,z)$ 投到 $\ker\mathcal J_j$，其第一分量必在 $F_\circ\cap\ker C_\circ^j$，所以
$$
\boxed{\|(C_\circ^j|_{F_\circ})^\dagger\|\le\|\mathcal J_j^\dagger\|.}
\tag{4.6}
$$
不需要预先给辅助 $z$ 的范数收费。

### 4.1 全部坏链

坏链满足 $l\le d+r-2$。有
$$
\|C_\circ\|<3,\quad \|X_0\|\le3^r,
\quad \|X_1\|\le r3^{r-1},\quad
\|\mathcal J_j\|\le(r+3)3^r.
$$
$m^{2r}\mathcal J_j$ 是整数矩阵，其秩至多 $2dl\le2d(d+r-2)$。令
$$
M_{m,r}=m^{2r}(r+3)3^r.
$$
对任意非零秩整数矩阵，非零奇值平方的乘积是最高阶余子式的平方和，因而至少为一。结合范数上界，并在缩回 $m^{2r}$ 时再支付该因子，得
$$
\boxed{
\|(C_\circ^j|_{F_\circ})^\dagger\|
\le M_{m,r}^{\,2d(d+r-2)}=:K_{\rm bad}(m,r).
}
\tag{4.7}
$$
零映射的 Moore–Penrose 逆取零，亦受此界控制。

### 4.2 全部好链

若 $l\ge d+r-1$，最高退化不掉秩，故 $F_\circ=\ker C_\circ^r$。记 $H_0=J_n+bE_{\rm high}$，有 $H_0^{n+1}=0$、$\|H_0\|<2$。完整参数化为
$$
\Phi_p(u)=\sum_{k=0}^{n}(-1)^k\binom{p+k-1}{k}
H_0^ku\otimes e_{p-1+k},\qquad1\le p\le r.
\tag{4.8}
$$
全部 $rd$ 列独立，且参数空间中 $C_\circ$ 恰为 $I_d\otimes J_r$，因为 $C_\circ\Phi_p=\Phi_{p-1}$。

可取
$$
\|\Phi\|\le r(n+1)\binom{n+r-1}{n}2^n.
\tag{4.9}
$$
这里分别对 $r(n+1)$ 个块使用三角不等式，故未遗漏维数因子。
若 $v_q$ 是输出的第 $q$ 个尾坐标，前 $r$ 级的准确左逆是
$$
u_{h+1}=\sum_{k=0}^{h}\binom hk H_0^k v_{h-k},
\qquad0\le h\le r-1.
\tag{4.10}
$$
该 binomial 反演可逐项相乘验证，其块行和及块列和都至多 $r3^{r-1}$。所以左逆范数不超过这一数。对 $J_r^j$ 取范数一的右逆并搬回完整物理列，得到
$$
\boxed{
\|(C_\circ^j|_{F_\circ})^\dagger\|
\le r^2(n+1)3^{r-1}\binom{n+r-1}{n}2^n
=:K_{\rm good}(n,r).
}
\tag{4.11}
$$
此处使用真正的最小解不超过这个可行解，而非声称非正交参数化保最小性。

## 5. 还原全部真实强权和旧头费用

原强尾中位尺度 $c_*=y^{-2}$ 的相似费用至多 $4^R$。每条标准尾链为 $c_*L_l$。
从单位链还原到它的正对角参数可写成
$$
q_k=c_*^k\sqrt{\frac{k!(l-1)!}{(l-1-k)!}},\qquad q_0=1.
$$
因为 $l\le R+1$，
$$
q_k/q_{k-1}=c_*\sqrt{k(l-k)}
\le\frac{R+1}{2y^2}<1,
$$
所以 $q_k\le1$，且 $q_k^{-1}\le y^{2k}$。

坏链只使用 $k\le l-1\le d+r-3$，故单位化成本至多 $y^{2(d+r-3)}$。好链 (4.8) 只使用 $k\le n+r-1\le d+r-3$；左逆 (4.10) 则只乘 $q_k\le1$。因此同一上界覆盖所有好链，不支付整个长链的巨大单位化费用。

最后原旧头相似费用为 $e^{221a}$。各 primitive 块的可行逆平方相加只取最大块费用，再用同一个实际相似还原。因此定义
$$
\boxed{
K_{\rm flag}(m,R,r)=e^{221a}4^R y^{2(d+r-3)}
\big[K_{\rm bad}(m,r)+K_{\rm good}(n,r)\big].
}
\tag{5.1}
$$
对全部 $1\le j\le r-1$，原完整物理受限逆满足
$$
\boxed{\|(C_0^j|_{F_0})^\dagger\|\le K_{\rm flag}(m,R,r).}
\tag{5.2}
$$
上述同一相似只作为构造可行代表的工具，不把原完整 Galerkin 变成 primitive 正交直和。

式 (5.1) 不含最高单位 $U^{-1}$、最高 carry $t^{-1}$ 或远方差 $S^{-1}$。它针对同一个真实 $F_0,C_0$ 的来源费用。

## 6. 原整段奇高度的实际方差可直接代入

原 $\|C_0\|<8$。在 (1.6) 中明确取
$$
\alpha_{m,R,r}=\frac1{(r-1)!K_{\rm flag}(m,R,r)^2},\qquad
L_{m,R,r}=4A_r(8)(r-1)!K_{\rm flag}(m,R,r)^2+2.
\tag{6.1}
$$
则对每个奇数 $r\ge3$ 和全部 $0<S\le1$，原完整残余有
$$
\boxed{
\|\xi_0(S)\|\le
2+\sum_{j=1}^{r-1}\frac{(64L_{m,R,r}^2)^j}{j!}.
}
\tag{6.2}
$$
因此可以直接代原连续尾方差 $S=S_x$，不需要证明其进入未知邻域。

实际使用还应保留原能量界。由完整正规方程，
$\langle H_Sa_S,a_S\rangle=\langle f,a_S\rangle\le\|f\|^2$，所以每一项都有
$\|C^ja_S\|\le\sqrt{j!}S^{j/2}\|f\|$。与 (2.1) 逐项取小得到
$$
\boxed{
\|\xi_0(S)\|\le
2+\sum_{j=1}^{r-1}
\min\left\{\frac{64^jL_{m,R,r}^{2j}}{j!},
\frac{8^j}{\sqrt{j!}S^{j/2}}\right\}.
}
\tag{6.2a}
$$
故不把方差一致的通用界宣称为实际 $S_x$ 处总比能量界更小。

只读出对数大小时，(6.2) 至多为
$$
4(r-1)\log K_{\rm flag}
+2(r-1)\log((r-1)!)+O(r),
\tag{6.3}
$$
其中绝对 $O(r)$ 可直接由 $A_r(8)\le e^{64}$ 及 (6.1)–(6.2) 展开；完整使用时以明确式为准。

这补上了 $r\ge5$ 的方差一致界。$r=3$ 优先使用父稿更锐的 $1600K_{\rm flag}^3$，本条不把较粗通用常数称为三阶改进。$r=1$ 不满足本条的 forcing 前提，也未被包含。

## 7. 后继仍需支付什么

(6.2) 是同一真实源的无权费用，(3.1)–(3.2) 给它准确的零方差极限。二者都保留了高真旗的源专属 Green 列。

但是 (5.1) 仍含 $4^R$，且 (6.2) 的指数随 $r$ 增长；这里没有得到所需 $\gamma<1/16$ 的物理孔加权 $\mathcal Z_\gamma$。最高 carry 的完整正则项、一般 $t>0$ 的真实费用、原母窗与全部 same-$w$ 配对仍需按原开放接口处理。不能把本条的全高度方差控制登记为 $N=M$ 或普通 ISP 的完成。
