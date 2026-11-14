# R239 附录：真实外出生源的受限因子与 Vandermonde 方向排除

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；主会话全文核查 R271 原三块源、两带域及实际头容量。
状态：已证明真实外桥有效源的因子分解与对显式二阶坏方向的正交；未将该正交传过 Schur 逆，未得到无权能量上界。

本稿承接 [R271 真实 Schur 消元](R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md) §7、
[出生层二带公式](../notes/2026-11-13-low-kernel-birth-layer-double-schur-bridge-1cf.md)
以及 [原权 Vandermonde 短旗反例](R239-appendix-vandermonde-coprimitive-short-kernel-counterexamples.md)。固定同一原合法 $m\ge5$、$d=2^m$、$4d\le q\le e^{d^3/4}$，
$D=D_m$、$D_3=D_{3,m}$，采用原 Hilbert 度量。

## 1. 短旗最高删除坐标与第三次尾

记
$$
E_{h,p}=\ker D^h\cap\mathcal H_p^{(m)},\qquad
U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
$$
固定层的相容尾塔已经证明
$$
D^{h-1}:U_{h,p}\longrightarrow \ker D\cap\mathcal H_{p-h+1}^{(m)}
$$
是有界双射。其逆记为 $\mathfrak J_{h,p}$。
所有关于 $\mathfrak J$ 的断言只在固定有限层使用；本稿不补上任何全孔层统一范数界。

令
$$
C_D=[D,D^*]=S_mI-2\sum_{j\ge m}a_j^2n_j.
$$
有 $[D,C_D]=-2D_3$、$[D,D_3]=0$，因而准确有
$$
[D^3,D^*]=3C_DD^2-6D_3D.
$$
特别，
$$
\boxed{D^3D^*f=-6D_3Df\quad(f\in\ker D^2).}
\tag{1.1}
$$
这仍是原顺序算子式。

设 $X$ 是一个有限块上的 Vandermonde 向量：
$$
D_I^*X=0,\qquad D_I^2X=0.
$$
在这个有限块上用 (1.1)，立即得到
$$
D_{3,I}D_IX=0.
$$
归一化并张量补集真空后，前缀之外的删除全部为零，因此对原无限尾的同一个 $x$，
$$
\boxed{D^2x=0,\qquad D_3Dx=0.}
\tag{1.2}
$$
这里没有把原无限尾 $D^*x$ 写成零；它仍恰有远尾创建项。

因此
$$
Dx\in\ker D\cap\ker D_3.
\tag{1.3}
$$
若 $x_2=P_{U_{2,p}}x$，则 $x-x_2\in\ker D$，所以
$$
Dx_2=Dx,\qquad D_3Dx_2=0.
\tag{1.4}
$$
这是随后进入真实出生桥的那一部分。

## 2. 正确消元的外桥没有跨过 Q1 的交换

保留 R271 的三块分解，三块分别为相对出生层
$s-q\le0$、$s-q=1$、$s-q\ge2$：
$$
\mathcal G=SS^*
=\begin{pmatrix}
B_0&V_1^*&0\\
V_1&B_1&V_2^*\\
0&V_2&B_2
\end{pmatrix}.
$$
真正的右端为 $g=(g_0,0,0)$。令
$$
Q_1=B_1-V_1B_0^{-1}V_1^*,\qquad
\zeta=V_1B_0^{-1}g_0,
$$
$$
\sigma=V_2Q_1^{-1}\zeta,\qquad
\mathcal H_2=B_2-V_2Q_1^{-1}V_2^*,\qquad
z_2=\mathcal H_2^{-1}\sigma.
\tag{2.1}
$$
这些都是原稿的真实算子。

按出生层分解 $S=S_0+S_1$，其中 $S_0$ 保持出生层，$S_1$ 增加出生层一。
增加出生层的项只来自 $D$ 从正交高度 $h$ 降到 $h-2$ 的那一块；
头矩阵 $A$ 保持尾高度和出生层。
因此外桥准确为
$$
V_2=S_1S_0^*
$$
在出生层 $q+1$ 到 $q+2$ 的相应限制。特别，
$$
\boxed{\sigma\in\operatorname{Ran}S_1,\qquad
\sigma\text{ 只在出生层 }q+2.}
\tag{2.2}
$$
高块虽包含所有出生层 $\ge q+2$，但这个有效源本身只在其第一层。

置
$$
\rho=S_0^*Q_1^{-1}\zeta
$$
（取出生层 $q+1$ 的链限制），则 $\sigma=S_1\rho$。
这里完整保留 $Q_1^{-1}$；没有要求它与 $D_3$、任何尾塔或任何投影交换。

## 3. 外桥的每段准确因子与共同基层

在第 $t$ 个输出段，$2\le t\le d-1$，出生层 $q+2$ 对应
$$
p=q+t,\qquad h=t-1,
$$
所以 $\sigma_t$ 的尾高度准确为 $U_{t-1,q+t}$。
其允许头为 $e_i$、$0\le i\le d-t-1$。

原出生层公式给
$$
\boxed{
(S_1^*f)_{t+1}
=-t(t-1)\,
\mathfrak J_{t+1,q+t+1}\,
D_3D^{t-2}f_t.
}
\tag{3.1}
$$
这里 $f_t\in U_{t-1,q+t}$，头坐标保留恒等。
没有遗漏链旗投影：目标段 $t+1$ 允许同样的 $i\le d-t-1$，
而其纯核阶容量 $d-i\ge t+1$ 正好容纳 (3.1) 的高度 $t+1$。

所有段的最高删除坐标都在同一个基层：
$$
D^{t-2}f_t\in\ker D\cap\mathcal H_{q+2}^{(m)}.
$$
令
$$
\mathcal K_j=\ker D\cap\mathcal H_j^{(m)},\qquad
C_q=D_3|_{\mathcal K_{q+2}}:\mathcal K_{q+2}\to\mathcal K_{q+1},
$$
$$
J_t=\mathfrak J_{t-1,q+t},\qquad
K_t=\mathfrak J_{t+1,q+t+1}.
$$
于是 (3.1) 为
$$
(S_1^*f)_{t+1}=-t(t-1)K_t C_q J_t^{-1}f_t.
$$
对真实 $\sigma=S_1\rho$ 取伴随，得到
$$
\boxed{
J_t^*\sigma_t
=-t(t-1)C_q^*K_t^*\rho_{t+1}.
}
\tag{3.2}
$$
(3.2) 中
$$
C_q^*=P_{\mathcal K_{q+2}}D_3^*|_{\mathcal K_{q+1}}
$$
是真实受限伴随，不能省掉该投影。

所以每一段的源都准确满足
$$
\boxed{
J_t^*\sigma_t\perp\ker C_q.
}
\tag{3.3}
$$
等价地，对任何允许头分量的 $f_t$，
$$
f_t\in U_{t-1,q+t},\quad D_3D^{t-2}f_t=0
\quad\Longrightarrow\quad
\langle\sigma_t,f_t\rangle=0.
\tag{3.4}
$$
这是实际外桥后的源正交；不是对任意环境源的断言。
也可以直接由 (3.1) 与 $\sigma=S_1\rho$ 看出，不必支付各个因子的范数。

## 4. 原 Vandermonde 坏族确被源排除的一段

取第 $t=3$ 段，令 $p=q+3$。
用原纯尾前 $2p$ 位的互异权构造单位 Vandermonde 向量 $x_{m,p}$。
它满足
$$
x_{m,p}\in E_{2,p},\qquad
\|D^*x_{m,p}\|^2=S_{m+2p}\longrightarrow0,
\qquad D_3Dx_{m,p}=0.
$$
令 $x_2=P_{U_{2,p}}x_{m,p}$，由 (1.4)，
$D_3Dx_2=0$。第 3 段的 $\sigma_3$ 在 $U_{2,p}$ 上，
故 (3.4) 给
$$
\boxed{
\langle\sigma_3,e_i x_{m,p}\rangle
=\langle\sigma_3,e_i x_2\rangle=0
\quad(0\le i\le d-4).
}
\tag{4.1}
$$
原坏向量的 $U_1$ 部分属于更高出生层，已与 $\sigma$ 的出生层 $q+2$ 正交；
其 $U_2$ 部分则由真正外桥消去。
这一结论对所有原准确源旗中的输入 $r$ 成立，特别适用于真正 $w\in W$ 的残量。

因此，短旗的统一环境 $D^*$ 下界虽被该族彻底否定，
该族并不会自动成为真实外桥有效源 $\sigma$ 的坏方向。
这是具体源上的准确取消，不是从有限层满射或一般环境 gap 推出的预算。

## 5. 为什么仍不能把源正交传给最优链

令 $\mathscr B\subset\mathscr Y_2$ 为任意满足 $V_2^*b=0$ 的闭子空间。
上面的坏方向（包括其高出生层分量）就在这个外桥核中。
由 (2.1)，对 $b\in\mathscr B$，
$$
\mathcal H_2b=B_2b,\qquad
\langle\sigma,b\rangle=0.
$$
真实方程 $\mathcal H_2z_2=\sigma$ 因而只给
$$
\boxed{\langle z_2,B_2b\rangle=0\quad(b\in\mathscr B).}
\tag{5.1}
$$
它没有给 $\langle z_2,b\rangle=0$。
普通高块 $B_2$ 可以把这个外桥核与其他高出生方向混合；
没有证明它保持 $\mathscr B$，也没有证明它在该部分有统一条件数。

同样，(3.2) 是经过固定层尾塔伴随后的 $C_q^*$ 像，
不能据此套用只对降低孔数的 $C_q$ 已付的 Schur 逆能量收缩。
各 $\mathfrak J$、$Q_1^{-1}$ 与真实 $\mathcal H_2$ 的成本仍须留在原位置。

后续准确问题是：这种源排除在真实 Schur 度量中能否转成
$\langle\mathcal H_2^{-1}\sigma,\sigma\rangle$ 或
$\|\widetilde C_{\rm tot}(h(z))\|$ 的可用上界。
本稿没有给出该上界，没有宣称坏方向从 $z_2$ 中消失，也没有改变原 $N=M$ 与普通 ISP 的开放状态。
