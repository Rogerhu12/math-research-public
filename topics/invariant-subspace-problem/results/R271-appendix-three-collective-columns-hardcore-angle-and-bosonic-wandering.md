# R271 附录：三列集体 creation 的硬核正角与真实 bosonic wandering 的最高三头读出

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：下述三列不等式、完整 bosonic wandering 表示与定量硬核正角均已证明。** 结论作用于原 $N/Y$ 真实有限头和全部横向 Fock 源，不限制总孔数。它不把原 $W=M\ominus\overline{BM}$ 向量的 bosonic 核投影当作 bosonic wandering；原 $W$ 到该 wandering 的反向投影费用仍未支付。

所用原空间、头幂和共同 Fock 嵌入见：

- [完整真核的零占据与原头预算](../notes/2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md) §§1--4；
- [移动真实头 bosonic 核投影](../notes/2026-11-14-moving-true-head-bosonic-projections-and-inverse-gram-strong-limit-789f-next.md) §§1--5；
- [原首二进位权与物理 Schur](R271-appendix-first-binary-bit-uniform-physical-schur-and-exact-top-source.md) §1。

下面重给新结论的全部证明。

## 1. 三列硬核不等式

设 $\mathcal F=\Gamma_{\rm s}(\mathfrak h)$，$u\in\mathfrak h$ 为单位向量，$a=a(u)$。令 $e_i$ 为一个物理坐标，置
$$
p=|\langle e_i,u\rangle|^2,\qquad 0<p\le\frac12.
$$
记 $Q_i$ 为该物理坐标占据至多一的正交投影。则对任意 $g\in\ker a$，
$$
\boxed{
\sum_{j=0}^2
\left\|(I-Q_i)\frac{(a^*)^j}{\sqrt{j!}}g\right\|^2
\ge p^2\|g\|^2.
}
\tag{1.1}
$$

这些 creation 列在 $\ker a$ 上处处有定义：
$$
\frac{(a^*)^j}{\sqrt{j!}}g
=|j\rangle_u\otimes g
$$
是等距映射。因此 (1.1) 不需要 $g$ 的总粒子数矩有限。

**证明。** 吸收一个无关相位后，在 $\operatorname{span}(u,e_i)$ 中选择单位向量 $c\perp u$，使
$$
e_i=\sqrt p\,u+\sqrt{1-p}\,c.
$$
把横向源完整分解为
$$
g=\sum_{n\ge0}|0\rangle_u\otimes |n\rangle_c\otimes g_n,
\qquad \|g\|^2=\sum_n\|g_n\|^2.
\tag{1.2}
$$
对每个固定 $j$，$Q_i$ 保持这两个模式的总粒子数 $j+n$，所以不同 $n$ 的输出严格正交。以下可逐 $n$ 估计。

当 $n=0$，取 $j=2$。两个 $u$ 粒子同时落在物理坐标 $i$ 的概率为 $p^2$，故该项的非硬核能量恰为 $p^2\|g_0\|^2$。

当 $n=1$，取 $j=1$。归一态 $|1\rangle_u|1\rangle_c$ 的两个粒子同时落在 $i$ 的概率为 $2p(1-p)\ge p^2$。

当 $n\ge2$，取 $j=0$。$n$ 个 $c$ 粒子的 $i$ 占据服从参数 $1-p$ 的二项分布，其至少二占据的概率不小于 $(1-p)^2\ge p^2$：仅保留指定两个粒子都落在 $i$ 的事件即可。

对所有 $n$ 求和得到 (1.1)。证明只用了有界占据投影；没有通过无界 $a_i^2$ 的范数来反推距离。$\square$

若 $Q_{\rm hc}$ 是全部物理坐标同时硬核的正交投影，则 $\operatorname{Ran}Q_{\rm hc}\subseteq\operatorname{Ran}Q_i$。因此同样有
$$
\sum_{j=0}^2
\left\|(I-Q_{\rm hc})\frac{(a^*)^j}{\sqrt{j!}}g\right\|^2
\ge p^2\|g\|^2.
\tag{1.3}
$$

## 2. 原完整 bosonic 核和其真实 $B_m$ wandering

取原 $m\ge5$、$d=2^m$，
$$
A=A_m,\quad B=B_m,\quad
S=S_m=\sum_{i\ge m}(i+1)^{-4},\quad
u=\frac{(b_i)_{i\ge m}}{\sqrt S},\quad b_i=(i+1)^{-2}.
$$
所有头算子保持原物理内积。原 $A_m$ 为 $B_m$ 的多项式，严格降低物理头指标且 $A_m^d=0$，所以 $A_mB_m=B_mA_m$。

在原前 $m$ 位硬核头与完整 bosonic 尾的共同空间上，令
$$
\mathcal K_m^{\rm B}=\ker(A+\sqrt S\,a(u)).
$$
按已证零占据重构，定义
$$
\mathcal R h
=\sum_{j=0}^{d-1}
\frac{(-A)^j(a^*)^j h}{S^{j/2}j!},
\qquad h\in\mathbb C^d\otimes\ker a.
\tag{2.1}
$$
这是从零集体占据空间到 $\mathcal K_m^{\rm B}$ 的有界同构，且
$$
\mathcal R^*\mathcal R=H\otimes I,\qquad
H=\sum_{j<d}\frac{(A^j)^*A^j}{S^j j!},\qquad
I\le H\le C_m I,
\tag{2.2}
$$
其中
$$
C_m=\sum_{j<d}\frac{\|A_m^j\|^2}{S_m^j j!}.
$$
由于 $B$ 与 $A$ 对易，
$$
B\mathcal R=\mathcal R B.
\tag{2.3}
$$
有限头 $B$ 的所有次对角权非零，故
$$
\operatorname{Ran}B=\operatorname{span}(e_0,\ldots,e_{d-2}),
\qquad \ker B^*=\mathbb C e_{d-1}.
$$
这些像在张量全部横向源后仍闭，再经 $\mathcal R$ 的有界同构仍闭。因此
$$
\mathcal W_m^{\rm B}
:=\mathcal K_m^{\rm B}\ominus B_m\mathcal K_m^{\rm B}
$$
的完整表达为
$$
\boxed{
\mathcal W_m^{\rm B}
=\{\mathcal R(h\otimes g):g\in\ker a\},
\qquad h=H^{-1}e_{d-1}.
}
\tag{2.4}
$$
确实，$\mathcal Rk$ 与所有 $\mathcal RB\ell$ 正交当且仅当
$B^*Hk=0$。这里先保完整 $H$，再取其真实逆；没有压缩与取逆的交换。

置
$$
\lambda=\langle H^{-1}e_{d-1},e_{d-1}\rangle.
$$
由于 $H$ 严格正且 $I\le H\le C_mI$，
$$
\boxed{
C_m^{-1}\le\lambda\le1,\qquad
h_{d-1}=\lambda,\qquad
\|h\|^2\le\lambda.
}
\tag{2.5}
$$
最后一个不等式来自 $H^{-2}\le H^{-1}$。对
$z=\mathcal R(h\otimes g)$，准确有
$$
\boxed{\|z\|^2=\lambda\|g\|^2.}
\tag{2.6}
$$

式 (2.4) 是局部完整 bosonic 核上的 $B_m$ wandering，不是原全局 $B$ 理想的 $W$。

## 3. 最高三头行的完整三角提取

原两模型的 $A_m$ 一次项均为 $B_m/d_0$，其中 $d_0=e^{-20}$。因为 $d-1$ 为奇数，最高两个连续物理头下降权准确为
$$
(A_m)_{d-2,d-1}=1,\qquad
(A_m)_{d-3,d-2}=\kappa_0,
\qquad
\kappa_0=\frac{d_1}{d_0^2}=e^{-1070}.
\tag{3.1}
$$
所有非一次项至少下降两个物理头指标；它们不改变 (3.1)。特别，
$$
(A_m^2)_{d-3,d-1}=\kappa_0.
\tag{3.2}
$$
这同时适用于原 N/Y 头，未作 Jordan 相似。

记
$$
g_j=\frac{(a^*)^j g}{\sqrt{j!}},\qquad
h_1=h_{d-2},\quad h_2=h_{d-3},\quad
\beta=(Ah)_{d-3}.
$$
由 (2.1)，$z$ 的最高三头行准确为
$$
z_{d-1}=\lambda g_0,
\tag{3.3}
$$
$$
z_{d-2}=h_1g_0-\frac{\lambda}{\sqrt S}g_1,
\tag{3.4}
$$
$$
z_{d-3}=h_2g_0-\frac{\beta}{\sqrt S}g_1
+\frac{\kappa_0\lambda}{\sqrt2\,S}g_2.
\tag{3.5}
$$
$j\ge3$ 的项不能到达这三行，因每个 $A$ 因子至少下降一头。原全部非齐次高次项均已包含在 $h$ 与 $\beta$ 中，未被删掉。

令 $Q_{\rm hc}$ 作用于全部尾物理坐标。它与提取头行及所有头标量系数对易。定义
$$
F_j=(I-Q_{\rm hc})g_j,\qquad
E_r=(I-Q_{\rm hc})z_{d-1-r}\quad(r=0,1,2),
$$
并令
$$
\mathcal E^2=\sum_{r=0}^2\|E_r\|^2
\le\|(I-Q_{\rm hc})z\|^2.
$$
式 (3.3)--(3.5) 给真正的逆三角关系
$$
F_0=\lambda^{-1}E_0,
$$
$$
F_1=\frac{\sqrt S}{\lambda}(h_1F_0-E_1),
$$
$$
F_2=\frac{\sqrt2\,S}{\kappa_0\lambda}
\left(E_2-h_2F_0+\frac{\beta}{\sqrt S}F_1\right).
\tag{3.6}
$$

原头已有 $\|A_m\|\le6$，而 $m\ge5$ 时 $S_m<1$。由 (2.5)，
$$
|h_1|,|h_2|\le\sqrt\lambda,\qquad
|\beta|\le6\sqrt\lambda.
$$
于是 (3.6) 逐项给
$$
\|F_0\|\le\lambda^{-1}\mathcal E,
$$
$$
\|F_1\|\le2\sqrt S\,\lambda^{-3/2}\mathcal E,
$$
$$
\|F_2\|\le\frac{14\sqrt2\,S}{\kappa_0\lambda^2}\mathcal E.
\tag{3.7}
$$
在最后一式中，括号的三项分别不超过
$1,\lambda^{-1/2},12\lambda^{-1}$ 倍 $\mathcal E$，其和不超过
$14\lambda^{-1}\mathcal E$。因为 $\kappa_0,\lambda,S\le1$，相加得
$$
\boxed{
\sum_{j=0}^2\|F_j\|^2
\le\frac{400}{\kappa_0^2\lambda^4}
\|(I-Q_{\rm hc})z\|^2.
}
\tag{3.8}
$$
常数 $400$ 可直接由 $1+4+392=397<400$ 得到。这是同一个 $z$ 的完整头行提取，未分别选择三个源。

## 4. 真实 bosonic wandering 与全部硬核的定量正角

选第一尾物理位 $i=m$，令
$$
p_m=\frac{b_m^2}{S_m}.
$$
积分比较给
$$
\frac1{3(m+1)^3}\le S_m
\le\frac1{(m+1)^4}+\frac1{3(m+1)^3},
$$
所以
$$
\boxed{\frac3{m+4}\le p_m\le\frac3{m+1}\le\frac12\qquad(m\ge5).}
\tag{4.1}
$$
对 (2.4) 的同一个 $g$ 应用 (1.3)，再用 (3.8) 和 (2.6)，得到
$$
\|(I-Q_{\rm hc})z\|^2
\ge\frac{\kappa_0^2\lambda^4p_m^2}{400}\|g\|^2
=\frac{\kappa_0^2\lambda^3p_m^2}{400}\|z\|^2.
$$
因此
$$
\boxed{
\|(I-Q_{\rm hc})z\|^2
\ge
\frac{\kappa_0^2p_m^2}{400C_m^3}\|z\|^2
\ge
\frac{9e^{-2140}}{400(m+4)^2C_m^3}\|z\|^2
\quad(z\in\mathcal W_m^{\rm B}).
}
\tag{4.2}
$$

这条界同时保留全部横向 Fock 源、全部总孔层和全部出生。特别，
$$
\mathcal W_m^{\rm B}\cap\mathcal H_{\rm hc}=\{0\}.
\tag{4.3}
$$
对于原前 $m$ 位已经硬核的头，(4.2) 中的 $Q_{\rm hc}$ 就是整个共同 Fock 空间到原全硬核物理空间的限制。

定义角度下界
$$
\vartheta_m=\frac{3e^{-1070}}{20(m+4)C_m^{3/2}}.
\tag{4.4}
$$
原头已付
$$
C_m\le(k_m+e)\exp(k_mT_m+3T_m^{4/3}),
$$
$$
k_m=\max(2m,16),\qquad T_m=\log108+3\log(m+1).
$$
故
$$
\log\vartheta_m^{-1}=O(m\log(m+1)).
\tag{4.5}
$$
也可用原明确放宽 $C_m\le e^{40m^2}$ 得
$$
\vartheta_m\ge
\frac{3e^{-1070-60m^2}}{20(m+4)}.
\tag{4.6}
$$
这里没有整个原头链条件数的 $e^{c\,2^{4m}}$ 代价。

## 5. 原 $W$ 的正向近核与尚未支付的反向量

为防止把 (4.2) 用错空间，本节明确原接口。令
$$
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N
$$
为原全局 N/Y 模型的空间。令 $P_m^{\rm B}$ 为上述局部 bosonic 核的投影。

已证移动头定理给
$$
\|(I-P_m^{\rm B})w\|
\le26\,R_m\eta_{m-1}\|w\|
\quad(w\in M),
\tag{5.1}
$$
$$
R_m\le e^{22m^2},\qquad \eta_{m-1}\le e^{-80\,16^m},
$$
并有 $P_m^{\rm B}\to P_M$ 强收敛。式 (5.1) 是原核向量到 bosonic 核的单侧小误差。

但 $v_m=P_m^{\rm B}w$ 不因此属于 $\mathcal W_m^{\rm B}$。因为 $B_m$ 保持 $\mathcal K_m^{\rm B}$，
$$
\left(B_m|_{\mathcal K_m^{\rm B}}\right)^*v_m
=P_m^{\rm B}B_m^*v_m
=P_m^{\rm B}B_m^*w.
\tag{5.2}
$$
最后的等式严格来自
$P_m^{\rm B}B_m^*(I-P_m^{\rm B})=0$。

把 $B_m$ 以尾恒等扩到共同物理空间。原 carry 给 $\|B-B_m\|\to0$。对 $w\in W$，$B^*w\perp M$，故仅有
$$
P_m^{\rm B}B_m^*w
=P_m^{\rm B}B^*w+P_m^{\rm B}(B_m^*-B^*)w
\longrightarrow0.
\tag{5.3}
$$
其中第二项的真实 carry 费已付；第一项只由强收敛得到趋零，没有 (5.1) 那样的统一速率。它作用于 $B^*w\in M^\perp$，不是作用于 $M$。

尤其不能从 (5.1) 推出 $v_m$ 到
$\ker(B_m|_{\mathcal K_m^{\rm B}})^*=\mathcal W_m^{\rm B}$
的相同误差，也不能先除以这个随 $m$ 退化的非零奇值，再用 (4.2) 得出原 $w=0$。此外，$v_m$ 中的
$B_m\mathcal K_m^{\rm B}$ 分量可能与其 bosonic wandering 分量的非硬核部分相消；正交分解不使尾硬核投影同时约化这两项。

因此本文真正支付的是 (1.1) 和 (4.2) 的原始物理正角。把该角度与原同一个 $W$ 来源、完整 source Schur 或两费返回联合，仍须保留 (5.2) 的反向量；普通 ISP 与原 $N=M$ 未由本文完成。
