# R271 附录：原完整左核的 primitive 坐标与末段 Schur 公式

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_rebuild。

状态：**已证明。** 本文在原连续尾、原物理内积及完整源空间中，给出全部左核的有界坐标化，随后把其真实源 Gram 精确压到最后 $d-1$ 个 primitive 孔层。没有得到温和的 Gram 比较，没有证明无权 $N=M$。

## 1. 原空间与顺次最小原像

固定实际 $N$ 或 $Y$ 模型，$m\ge5$、$d=2^m$，以及原合法整数窗
$$
4d\le q\le e^{d^3/4}.
$$
写 $A=A_m$、$D=D_m$、$L=A+D$。头算子 $A$ 是原物理基中的严格上三角矩阵，第一条上对角线处处非零，所以
$$
A^d=0,\qquad \ker A=\mathbb Ce_0.
$$
尾孔层为 $\mathcal H_n$，$D_n=D|_{\mathcal H_n}:\mathcal H_n\to\mathcal H_{n-1}$；令
$$
P_0=P_{\ker D},\qquad K_n=\ker D\cap\mathcal H_n.
$$
$P_0$ 与所有孔投影交换。以下的 $P_0$ 作用于尾，在完整空间上默认张量头单位。
原纯尾的有限孔满射结论（[高孔笔记 §2](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)）保证：每个固定有限 $n\ge1$ 的 $D_n$ 都到整个 $\mathcal H_{n-1}$ 满射，其 Moore--Penrose 逆 $D_n^\dagger$ 在整个 $\mathcal H_{n-1}$ 上有界。这里不要求这个界对 $n$ 一致。

沿用[全尾 primitive 原像正规化](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md) §14，取
$$
T=d-1,\quad P=q+T,\quad
\mathcal L=512\sqrt{q+2T+1}\,(m+q+2T+1)^{3/2}.
$$
它给出同时定义的 $Q_0=I,Q_1,\ldots,Q_T$，在 $K_n$、$n\le P-t$ 上满足
$$
DQ_t=Q_{t-1},\qquad P_0Q_t=0\ (t\ge1),\qquad
D^{t+1}Q_t=0,
\tag{1.1}
$$
$$
Q_tK_n\subset\mathcal H_{n+t},\qquad
\|Q_t|_{K_n}\|\le 2^{t-1}\mathcal L^t\quad(t\ge1).
\tag{1.2}
$$
在每一固定孔层，$Q_t$ 恰为顺次单步 Moore--Penrose 原像：
$$
Q_t|_{K_n}=D_{n+t}^{\dagger}\cdots D_{n+1}^{\dagger}|_{K_n}.
\tag{1.3}
$$
这是 (1.1) 中原像方程及与 $\ker D$ 正交的唯一性；不把它认成 $(D^t)^\dagger$，也不宣称全孔直和上的 $D^\dagger$ 有界。由于本次输入 $n\le q$ 且 $t\le T$，有 $n\le P-t$，所以全部算子确在已付域内。

记原完整左空间和首源映射为
$$
\mathscr V_q=\{v\in P_{\le q}H:P_{<q}Lv=0\},\qquad
E_qv=Av_q.
\tag{1.4}
$$
它的源空间为
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_i\bigl(\ker D^{d-i-1}\cap\mathcal H_q\bigr).
$$
[真实左源构造](../notes/2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)已证明 $E_q:\mathscr V_q\to\mathscr R_q$ 有界满射。写
$$
J_q=E_qE_q^*,\qquad v=E_q^\dagger r=E_q^*J_q^{-1}r.
\tag{1.5}
$$
这些都是完整空间的算子；后面不先限制源为 primitive。

## 2. 全部左核的唯一 primitive 坐标

定义 Hilbert 坐标空间
$$
\mathscr P_q=\mathbb C^d\otimes\bigoplus_{n=0}^q K_n.
$$
对 $p=(p_0,\ldots,p_q)\in\mathscr P_q$，定义
$$
\mathcal Zp=\sum_{t=0}^{d-1}(-A)^tQ_tp,
\qquad
\mathcal E p=P_{\le q}\mathcal Zp.
\tag{2.1}
$$
$Q_t$ 在尾作用，$A$ 在头作用。每个固定 $t$ 增加恰好 $t$ 个孔，因此同一 $t$ 下不同输入孔层正交；(1.2) 给整个直和上的相同范数界。有限求和使 (2.1) 有界。

由 (1.1)、$Dp=0$ 和 $A^d=0$，全部相邻项及两端准确相消，故
$$
L\mathcal Zp=0,\qquad
P_0\mathcal Zp=p,\qquad
\mathcal E p\in\mathscr V_q.
\tag{2.2}
$$
反之，取任意 $v\in\mathscr V_q$，令 $p_n=P_0v_n$。输出第 $n-1$ 层的方程是
$$
D_nv_n=-Av_{n-1}\qquad(1\le n\le q).
$$
固定层最小逆的正交分解给
$$
v_n=p_n-A D_n^\dagger v_{n-1}.
\tag{2.3}
$$
$v_0=p_0$，因为第零孔层全属 $\ker D$。逐次代入 (2.3)，并用 (1.3) 及 $A^d=0$，得到
$$
v_n=\sum_{t=0}^{\min(n,d-1)}(-A)^tQ_tp_{n-t}.
\tag{2.4}
$$
因此
$$
\boxed{\mathcal E:\mathscr P_q\longrightarrow\mathscr V_q
\text{ 为有界双射，且 }\mathcal E^{-1}v=P_0v.}
\tag{2.5}
$$
这里覆盖所有非primitive 的左质量；它们由 (2.4) 生成，未被删除。

令
$$
\mathcal C_L=P_{\le q}(\mathcal Z-I),\qquad
\mathcal C_R=P_{>q}\mathcal Z.
\tag{2.6}
$$
于是 $\mathcal E=I+\mathcal C_L$，且
$$
P_0\mathcal C_L=P_0\mathcal C_R=0.
$$
原 primitive 嵌入与 $\mathcal C_L$ 的整个像正交，故真实坐标度量为
$$
\boxed{\mathcal D=\mathcal E^*\mathcal E
=I+\mathcal C_L^*\mathcal C_L\succeq I.}
\tag{2.7}
$$
特别，$\mathcal D^{-1}$ 是有界的，$\|\mathcal D^{-1}\|\le1$；但未由此给出 $\mathcal E$ 的小范数。

## 3. 全右旗与真正源的同一性

$\mathcal Zp$ 只支持到 $q+d-1$。对输入第 $n$ 孔层和第 $t$ 项，右段号是 $k=n+t-q\ge1$。其头指标至多 $d-1-t$，尾部分属 $\ker D^{t+1}$。因此
$$
i\le d-1-t\le d-k,\qquad d-i\ge t+1,
$$
正是原宽度 $d$ 右输入旗。最右一段允许为零。$L\mathcal Zp=0$ 给全部内部方程，所以
$$
\mathcal C_Rp\in\ker S,
\qquad
E_q\mathcal E p+F_{\rm flag}\mathcal C_Rp=0.
\tag{3.1}
$$
这里 $F_{\rm flag}=F|_{\ker S}$ 是原完整右旗的首源算子。
准确采用[同返回源两侧规范](R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)的宽度 $d$ 空间：第 $k$ 段在孔层 $q+k$、头指标 $i\le d-k$，各尾分量属于 $\ker D^{d-i}$；$F(c)=Dc_1$，$S(c)$ 收集 $Ac_k+Dc_{k+1}$（$1\le k<d$）及最右输出 $Ac_d$。以上全在原物理直和及其诱导内积中定义。

记
$$
\mathcal B=E_q\mathcal E.
$$
由 (2.4)，其准确式为
$$
\boxed{\mathcal Bp
=\sum_{t=0}^{d-2}(-1)^t A^{t+1}Q_tp_{q-t}.}
\tag{3.2}
$$
于是 (3.1) 等价于
$$
\boxed{F_{\rm flag}\mathcal C_R=-\mathcal B.}
\tag{3.3}
$$
全部源均为同一个完整 $\mathscr R_q$；没有把 $r$ 换成某个投影源。

对任意原源 $r$，置
$$
y=J_q^{-1}r,\quad v=E_q^*y,\quad
c^\flat=F_{\rm flag}^*y,\quad p=P_0v.
$$
则 $v=\mathcal E p$。由 (3.3)，
$$
\mathcal Z^*(v+c^\flat)
=\mathcal E^*v+\mathcal C_R^*c^\flat
=\mathcal B^*y-\mathcal B^*y=0.
$$
因此
$$
\boxed{\mathcal Dp=\mathcal B^*y=-\mathcal C_R^*c^\flat.}
\tag{3.4}
$$
这包括一般非primitive源和全部左孔层。其能量式为
$$
\boxed{\mu_q(r)^2=\|v\|^2
=\|p\|^2+\|\mathcal C_Lp\|^2
=\langle\mathcal Dp,p\rangle.}
\tag{3.5}
$$

## 4. 完整源 Gram 的坐标公式

对任意 $u=\mathcal E a\in\mathscr V_q$ 和 $y\in\mathscr R_q$，
$$
\langle E_qu,y\rangle
=\langle\mathcal Ba,y\rangle
=\langle\mathcal E a,\mathcal E\mathcal D^{-1}\mathcal B^*y\rangle.
$$
故
$$
E_q^*=\mathcal E\mathcal D^{-1}\mathcal B^*,
\qquad
\boxed{J_q=\mathcal B\mathcal D^{-1}\mathcal B^*.}
\tag{4.1}
$$
该式保留完整的逆后压缩，未将其替换成 $\mathcal B\mathcal B^*$。
同时，$p$ 是约束 $\mathcal Bp=r$ 下 $\langle\mathcal Dp,p\rangle$ 的唯一最小者，因而
$$
\mathcal Dp\perp\ker\mathcal B.
\tag{4.2}
$$

若 $a=e_0g$、$g\in\bigoplus_{n\le q}K_n$，则 $Aa=0$，所以
$$
\mathcal Za=\mathcal Ea=a,\qquad
\mathcal C_La=\mathcal C_Ra=\mathcal Ba=0.
$$
由 $v\perp\ker E_q$，得到
$$
\boxed{(e_0^*\otimes P_0)v=(e_0^*\otimes I)p=0.}
\tag{4.3}
$$
这里仅排去第零头的 primitive 坐标；没有令整个第零头尾向量为零。

## 5. 最后 $d-1$ 个 primitive 孔层的准确 Schur 补

按输入孔数把坐标空间正交分为
$$
\mathscr P_q=\mathscr P_{\rm lo}\oplus\mathscr P_{\rm bd},
$$
$$
\mathscr P_{\rm lo}=\mathbb C^d\otimes\bigoplus_{n=0}^{q-d+1}K_n,
\qquad
\mathscr P_{\rm bd}=\mathbb C^d\otimes\bigoplus_{n=q-d+2}^{q}K_n.
\tag{5.1}
$$
对低坐标，$\mathcal Z$ 的最高孔数至多 $(q-d+1)+(d-1)=q$，故
$$
\mathcal C_R|_{\mathscr P_{\rm lo}}=0,
\qquad
\mathcal B|_{\mathscr P_{\rm lo}}=0.
\tag{5.2}
$$
写
$$
\mathcal D=
\begin{pmatrix}D_{00}&D_{01}\\D_{10}&D_{11}\end{pmatrix},
\qquad p=(p_0,p_1),\qquad
B_1=\mathcal B|_{\mathscr P_{\rm bd}},\quad
C_1=\mathcal C_R|_{\mathscr P_{\rm bd}}.
$$
因为 $\mathcal D\succeq I$，$D_{00}\succeq I$ 可逆。定义真正的 Schur 补
$$
\boxed{D_{\rm eff}=D_{11}-D_{10}D_{00}^{-1}D_{01}.}
\tag{5.3}
$$
对于任意 $b\in\mathscr P_{\rm bd}$，
$$
\langle D_{\rm eff}b,b\rangle
=\inf_a\langle\mathcal D(a,b),(a,b)\rangle
\ge\|b\|^2,
$$
故 $D_{\rm eff}\succeq I$，在这完整 Hilbert 空间上有有界逆。

对真实左最小者，(3.4) 的低行及边界行分别给
$$
\boxed{p_0=-D_{00}^{-1}D_{01}p_1,\qquad
D_{\rm eff}p_1=-C_1^*c^\flat=B_1^*y.}
\tag{5.4}
$$
此外
$$
\boxed{
J_q=B_1D_{\rm eff}^{-1}B_1^*,\qquad
r=B_1p_1,\qquad
\mu_q(r)^2=\langle D_{\rm eff}p_1,p_1\rangle.
}
\tag{5.5}
$$
这精确编码全部低孔非primitive质量；不是把低坐标置零。
虽然右耦合只读取最后 $d-1$ 个 primitive 孔层，低坐标通常由 (5.4) 非零重建。

## 6. 成本范围与尚未支付之处

对本节全部 $q$，(1.2) 直接给
$$
\|\mathcal E\|,\ \|\mathcal Z\|
\le1+\sum_{t=1}^{d-1}\|A^t\|(2\mathcal L)^t.
\tag{6.1}
$$
它足以保证所有映射、伴随及逆度量操作合法，但不保证原所需的温和三 Gram 常数。
尤其，$\mathcal D\succeq I$ 仅控制下界；从 $p=P_0v$ 不能反推 $\|v\|\le C\|p\|$ 而省去 (6.1) 的实际费用。

(5.5) 保留的 $D_{\rm eff}$ 恰是仍须分析的完整低孔消元代价。
本文没有控制原窄源的裸费、$\lambda(r^\flat)$ 或该 Schur 补之间的温和比较，也没有在原 $W$ 上完成全头或非primitive质量重建。
因此无权 $N=M$ 及普通复 Hilbert 不变子空间问题仍开放。
