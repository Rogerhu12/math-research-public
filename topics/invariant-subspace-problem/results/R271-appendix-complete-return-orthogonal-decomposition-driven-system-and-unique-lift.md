# R271 附录：完整返回的物理正交分解、有限驱动系统与唯一提升

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文把真正的返回差 $G^{-1}-B$ 识别为同一完整／裸最小右链之差的 Gram。这个差落在一个准确物理商中，满足带裸链强迫项的有限 nilpotent 系统；其完整未压缩残量方程在该商的最小代表上是单射的。所有源、尾旗、零源核和高返回均保留。

这不是返回费用的统一上界。仅压缩后的 Sylvester 方程与行收缩不足以估计返回；本文同时保留唯一性所需的完整残量，包括其在完整零源核方向的输出分量。

依赖：

- [强尾联块的真实源、自然域与同一顶部](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。
- [首段观测损耗、精确源收缩与圆盘演算](R271-appendix-first-row-observability-loss-exact-source-contraction-and-disk-calculus.md)。

## 1. 一个固定右环境

固定前稿的 $m,R,n$，写
$$
C=A_m+D_<,\qquad C^h=0,\qquad D=D_>,\qquad \delta=\|D\|.
$$
令 $E_{a,j}=\ker D^a\cap\mathcal H_j^>$、$E_{0,j}=0$。取完整物理右环境
$$
\mathscr W=\bigoplus_{j=1}^{h}\mathscr W_j,\qquad
\mathscr W_j=\ker C^{h-j+1}\otimes E_{h,n+j}.
\tag{1.1}
$$
所有内积均为原物理内积。逐段头作用记为 $\mathcal C$：
$(\mathcal Cx)_j=Cx_j$。定义真正的尾行移位
$$
\mathcal T(x_1,\ldots,x_h)=(Dx_2,\ldots,Dx_h,0).
\tag{1.2}
$$
它保持 (1.1)：头旗因 $h-j$ 次核包含于 $h-j+1$ 次核而保持，尾部由 $D E_{h,n+j+1}\subseteq E_{h,n+j}$ 保持。并且
$$
\|\mathcal T\|\le\delta,\qquad
\mathcal T^h=0,\qquad
\mathcal C\mathcal T=\mathcal T\mathcal C.
\tag{1.3}
$$

记 $P=P^{\rm lo}$ 为逐段正交裸投影：
$$
(Px)_j=(I-P_{E_{j-1,n+j}})x_j,\qquad P^{\rm hi}=I-P.
\tag{1.4}
$$
$P$ 与 $\mathcal C$ 交换。高空间 $P^{\rm hi}\mathscr W$ 被 $\mathcal T$ 保持，因为第 $j+1$ 段的 $E_{j,n+j+1}$ 经 $D$ 落到第 $j$ 段的 $E_{j-1,n+j}$。

完整右域 $\mathcal Y_f$ 满足
$(\mathcal C+\mathcal T)c=0$ 和原源条件 $Dc_1\in\mathscr R$；裸右域 $\mathcal Y_b\subseteq P\mathscr W$ 满足
$(\mathcal C+P\mathcal T)b=0$ 和同一源条件。它们正是前稿的域，末段 $Cx_h=0$ 已由 (1.1) 保留。其源映射及最小列为
$$
F:\mathcal Y_f\to\mathscr R,\quad Fc=Dc_1,\qquad
F_b:\mathcal Y_b\to\mathscr R,\quad F_bb=Db_1,
$$
$$
J_f=F^\dagger,\quad J_b=F_b^\dagger,\qquad
H=J_f^*J_f=G^{-1},\quad B=J_b^*J_b.
\tag{1.5}
$$
前稿已证明 $P\mathcal Y_f=\mathcal Y_b$，且 $FP$ 在该关系中保持源。准确地说，对 $c\in\mathcal Y_f$ 有 $F_bPc=Fc$。

## 2. 全部零源和返回空间

令
$$
Z_f=\ker F\subseteq\mathcal Y_f,\qquad
Z_b=\ker F_b\subseteq\mathcal Y_b,
$$
$$
\mathscr E=P^{\rm hi}\mathscr W\ \mathbin{\oplus^\perp}\ Z_b,
\qquad
\mathscr E_0=\mathscr E\ominus Z_f.
\tag{2.1}
$$
$Z_f\subseteq\mathscr E$：完整零源经 $P$ 是裸零源，故其低部分在 $Z_b$。所有这些空间都是闭的；$\mathscr E_0$ 使用完整物理正交补。

$\mathscr E$ 被 $\mathcal T$ 保持。高部分的不变性已证；若 $z\in Z_b$，则
$$
P\mathcal Tz=-\mathcal Cz\in Z_b,
$$
因为 $\mathcal C$ 保持裸右域并与源交换。因此 $\mathcal Tz$ 的低部分在 $Z_b$，高部分在 $P^{\rm hi}\mathscr W$。同理 $Z_f$ 被 $\mathcal T$ 保持，因为
$\mathcal Tz=-\mathcal Cz$ 对 $z\in Z_f$ 成立。

$\mathcal C$ 也保持 $\mathscr E$ 和 $Z_f$。因此在实际商
$\mathscr E/Z_f$ 的正交代表 $\mathscr E_0$ 上定义
$$
T_0=P_{\mathscr E_0}\mathcal T|_{\mathscr E_0},
\qquad
C_0=P_{\mathscr E_0}\mathcal C|_{\mathscr E_0}.
\tag{2.2}
$$
这些是由不变子空间的商诱导的压缩，故
$$
\|T_0\|\le\delta,\qquad T_0^h=0,\qquad
C_0^h=0,\qquad T_0C_0=C_0T_0.
\tag{2.3}
$$
本文没有给 $C_0$ 一个 $\delta$ 范数界。

定义同一源的返回列
$$
\mathcal R=J_f-J_b:\mathscr R\to\mathscr W.
\tag{2.4}
$$
对任意 $r$，$PJ_fr-J_br\in Z_b$，故 $\mathcal Rr\in\mathscr E$。又 $J_fr\perp Z_f$，而 $J_br\perp\mathscr E$，所以
$$
\mathcal Rr\in\mathscr E_0,\qquad
J_b^*\mathcal R=0.
\tag{2.5}
$$
这里 $J_br\perp\mathscr E$ 同时使用其裸低支撑和对全部裸零源的最小正交性。于是
$$
\boxed{
J_f=J_b+\mathcal R,\qquad
H=B+\mathcal R^*\mathcal R.
}
\tag{2.6}
$$
因此 $H-B$ 是完整返回列的真实 Gram，不是独立原像范数的拼合。

## 3. 带同一裸输入的有限驱动方程

令 $C_{\rm s}=C|_{\mathscr R}$。完整与裸最小化分别给
$$
J_fC_{\rm s}=(I-P_{Z_f})\mathcal CJ_f
=-(I-P_{Z_f})\mathcal TJ_f,
$$
$$
J_bC_{\rm s}
=(I-P_{Z_b})\mathcal CJ_b
=-(I-P_{Z_b})P\mathcal TJ_b.
\tag{3.1}
$$
因为 $\mathscr E^\perp=(P\mathscr W)\ominus Z_b$，第二式右端恰为
$-P_{\mathscr E^\perp}\mathcal TJ_b$。把 $J_f=J_b+\mathcal R$ 代入第一式，使用 $\mathcal T\mathscr E\subseteq\mathscr E$，便得到
$$
\boxed{
\mathcal RC_{\rm s}=-T_0\mathcal R-KJ_b,
\qquad
K=P_{\mathscr E_0}\mathcal T|_{\operatorname{Ran}J_b}.
}
\tag{3.2}
$$
$\operatorname{Ran}J_b$ 是闭空间，并且与 $\mathscr E_0$ 物理正交。故这个完整行有真正预算
$$
\boxed{
\|[\,T_0,\ K\,]\|_{\mathscr E_0\oplus\operatorname{Ran}J_b
   \,\to\,\mathscr E_0}\le\delta.
}
\tag{3.3}
$$
这来自同一个 $\mathcal T$ 的正交输入分解，不是把两项分别粗估后相加。

也可保留两种强迫的区别。置
$$
A_{\rm hi}=P_{\mathscr E_0}P^{\rm hi}\mathcal TJ_b,\qquad
A_{\rm null}=P_{\mathscr E_0}P_{Z_b}P\mathcal TJ_b.
$$
则
$$
KJ_b=A_{\rm hi}+A_{\rm null},\qquad
\mathcal RC_{\rm s}=C_0\mathcal R-A_{\rm null},
$$
$$
\boxed{(C_0+T_0)\mathcal R=-A_{\rm hi}.}
\tag{3.4}
$$
高返回和裸零源反馈没有被合并成一个无条件小的输入。

## 4. 首源核上的准确消失

若 $r\in\ker C_{\rm s}$，则 $Cr=0$。还需核实单段尾逆确在原域内，而不能只使用这一个头等式。

原完整源的 Jordan 描述是
$$
\mathscr R
=\bigoplus_\gamma\ \bigoplus_{i=0}^{\ell_\gamma-2}
 v_{\gamma,i}\,E_{\ell_\gamma-i-1,n},
\qquad Cv_{\gamma,i}=v_{\gamma,i-1},
\quad\ell_\gamma\le h.
\tag{4.1}
$$
因此 $\ker C_{\rm s}$ 只含各块的 $i=0$ 项，且
$D^{h-1}r=0$。固定孔层的真最小逆 $D^\dagger$ 满足 $DD^\dagger r=r$；它在头上为单位，故
$$
CD^\dagger r=0,\qquad
D^hD^\dagger r=D^{h-1}r=0.
$$
所以
$$
c(r)=(D^\dagger r,0,\ldots,0)
\tag{4.2}
$$
同时属于完整和裸右域：第一段裸高空间为 $E_{0,n+1}=0$，其余所有头／尾旗及末端均满足。任何同源右链的第一段都满足 $Dx_1=r$，因而其总范数不小于 $\|D^\dagger r\|$。故 (4.2) 同时是真正最小者：
$$
\boxed{
J_fr=J_br=c(r),\qquad
\mathcal Rr=0\quad(r\in\ker C_{\rm s}).
}
\tag{4.3}
$$

源本身由定义满足 $\mathscr R\subseteq\operatorname{Ran}C\otimes\mathcal H_n^>$，但这不等于每个源都在 $\operatorname{Ran}C_{\rm s}$。例如 $n=0$ 时源为 $\operatorname{Ran}C$，而 $\operatorname{Ran}C_{\rm s}=\operatorname{Ran}C^2$，两者通常不同。

(4.1) 还证明 $\operatorname{Ran}C_{\rm s}$ 闭：它仍是同一有限可逆头变换下有限个闭尾旗的直和。若 $C_{\rm s}^{\sharp_b}=S_b^{-1}C_{\rm s}^*S_b$ 为 $S_b=L+B$ 伴随，则真实负图准确为
$$
\boxed{
\mathscr N=(\ker C_{\rm s})^{\perp_{S_b}}
=\operatorname{Ran}C_{\rm s}^{\sharp_b}.
}
\tag{4.4}
$$
(4.4) 不提供该表示的逆范数，也不把 $S_b$ 伴随换成物理伴随或源本身的像。

## 5. 必须保留的完整残量与唯一性

压缩系统 (3.2) 不是全部物理条件。由完整链和裸链的原方程，未压缩身份是
$$
\boxed{
(\mathcal C+\mathcal T)\mathcal R
=-P^{\rm hi}\mathcal TJ_b.
}
\tag{5.1}
$$
左边保在整个 $\mathscr E$ 中，包括其 $Z_f$ 输出分量。只有再投影到 $\mathscr E_0$ 才得到 (3.4)；不能反过来由 (3.4) 省掉该分量。

事实上，
$$
\mathcal L=(\mathcal C+\mathcal T)|_{\mathscr E_0}
:\mathscr E_0\longrightarrow\mathscr E
\tag{5.2}
$$
是单射。若 $x\in\mathscr E_0$ 且 $\mathcal Lx=0$，则 $x$ 满足完整内部及末端方程。它的第一段源为零：高部分的第一段为零，低部分在 $Z_b$。因此 $x\in Z_f$；与 $x\perp Z_f$ 合并给 $x=0$。

所以 (5.1) 在 $\mathscr E_0$ 中有且仅有已经构造出的解 $\mathcal Rr$。这排除了对真正未压缩问题任意添加齐次返回列。本文只对这些实际输入确认可解和唯一；没有宣布 $\mathcal L^{-1}$ 在整个环境中有统一界、在未证明的闭像上有界，或将某个 Moore–Penrose 逆免费移过商投影。

仅保 (3.2)、(3.3)、(4.3) 的抽象数据仍会留下无法估计的幅度。例如取一个小的二阶源 shift、$T_0=K=0$，可把源最高向量任意大地送入 $\ker T_0$ 而仍满足这些压缩式。物理条件 $\mathscr R\subseteq\operatorname{Ran}C$ 本身并不排这种抽象形式；真正补充是 (5.1) 的完整残量及 (5.2) 的单射。这个说明不是原 Boolean 模型的反例。

## 6. 对同源两费的准确意义

对任意同源 $r$，
$$
\lambda(r)^2=\alpha(r)^2+\|\mathcal Rr\|^2.
\tag{6.1}
$$
对前稿原 $w,u_Q$ 产生的源 $r_n^C$，裸链候选和完整 flat 配对已经给
$\Xi(r_n^C)^2\le2\|Y_n\|^2$。若 $c=J_fr_n^C$、$b=J_br_n^C$，同一真实未来满足
$$
\langle Y_n,c\rangle=\mu(r_n^C)^2,\qquad
\langle Y_n,b\rangle=-\alpha(r_n^C)^2.
$$
因而有保全部返回的配对
$$
\boxed{
\langle Y_n,\mathcal Rr_n^C\rangle
=\mu(r_n^C)^2+\alpha(r_n^C)^2.
}
\tag{6.2}
$$
这里的负号来自实际裸候选 $-P^{\rm lo}Y_n$；没有重新选择来源。

(6.2) 说明仅把真实未来范数变小会迫使返回列变大，不能据此直接得到普通右费上界。下一步要控制的是 (5.1) 对同一实际源的真实提升，或直接控制 (6.2) 的共同配对。所需 $\mu^2\le\kappa_m\Xi^2$ 及 $\kappa_mh/Q=O(1)$ 尚未证明；不能从有限 nilpotence、行收缩或两端 Stein 相减代替这个缺口。
