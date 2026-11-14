# R271 附录：primitive 孔带宽、源 Gram 的顶层分裂与远端 Schur 小量

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_rebuild。

状态：**已证明。** 本文继续[完整左核 primitive 坐标与末段 Schur 公式](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)，保留原实际头、完整连续尾、原源及物理内积。定量结论使用真实头高幂的四次衰减，不用粗的整个坐标映射范数代替长距离耦合。

## 1. 沿用的完整坐标

取原 $m\ge5$、$d=2^m$、$4d\le q\le e^{d^3/4}$，令 $T=d-1$，
$$
\mathcal L=512\sqrt{q+2T+1}\,(m+q+2T+1)^{3/2}.
$$
前稿在
$$
\mathscr P_q=\mathbb C^d\otimes\bigoplus_{n=0}^qK_n,
\qquad K_n=\ker D\cap\mathcal H_n
$$
上给
$$
\mathcal Z=\sum_{t=0}^{d-1}(-A)^tQ_t,
\quad \mathcal E=P_{\le q}\mathcal Z=I+\mathcal C_L,
\quad \mathcal C_R=P_{>q}\mathcal Z,
$$
$$
\mathcal D=\mathcal E^*\mathcal E=I+\mathcal C_L^*\mathcal C_L\succeq I,
\quad \mathcal B=E_q\mathcal E,
\quad J_q=\mathcal B\mathcal D^{-1}\mathcal B^*.
\tag{1.1}
$$
这里 $Q_tK_n\subset\mathcal H_{n+t}$、$P_{\ker D}Q_t=0$ 对 $t\ge1$，而
$$
\|Q_t|_{K_n}\|\le(2\mathcal L)^t.
\tag{1.2}
$$
所有 $n\le q,t\le d-1$ 均在原定义域内。

## 2. 真实度量的孔带宽与顶层单位块

记 $Q_t^{(n)}=Q_t|_{K_n}$，并把 $\mathcal D_{nn'}$ 看作从头张量 $K_{n'}$ 到头张量 $K_n$ 的块。由 (1.1)，准确有
$$
\begin{aligned}
\mathcal D_{nn'}={}&\delta_{nn'}I\\
&+\sum_{\substack{1\le t,s\le d-1\\n+t=n'+s\le q}}
(-1)^{t+s}(A^t)^*A^s
\otimes (Q_t^{(n)})^*Q_s^{(n')}.
\end{aligned}
\tag{2.1}
$$
没有假设不同阶 $Q_t$ 的像互相正交；仅使用相同输出孔层才可能配对。因为 $1\le t,s\le d-1$，
$$
\boxed{\mathcal D_{nn'}=0\quad\text{若 }|n-n'|>d-2.}
\tag{2.2}
$$
而 $n=q$ 时不存在 $t\ge1$ 满足 $n+t\le q$，所以
$$
\boxed{\mathcal D_{qq}=I,\qquad \mathcal D_{qn}=\mathcal D_{nq}=0\quad(n<q).}
\tag{2.3}
$$
这是原整个 $\mathbb C^d\otimes K_q$ 的单位直和块，不只是某个标量方向。

## 3. 完整左源 Gram 的 primitive 顶层分裂

令
$$
U_q=\mathbb C^d\otimes K_q\subset\mathscr V_q,
\qquad
\mathscr R_q^{\rm prim}=\operatorname{Ran}A\otimes K_q.
$$
若 $v\in\mathscr V_q$，它的纯顶层 primitive 部分 $P_{U_q}v$ 仍属于 $\mathscr V_q$。由于 $A$ 只作用于头，
$$
E_qP_{U_q}=P_{\ker D}E_q.
\tag{3.1}
$$
$P_{\ker D}$ 保持整个原源空间 $\mathscr R_q$。对 (3.1) 取伴随，再相乘，得到
$$
\boxed{J_qP_{\ker D}=P_{\ker D}J_q.}
\tag{3.2}
$$
在该 primitive 源直和块上，
$$
\boxed{J_q|_{\mathscr R_q^{\rm prim}}
=(AA^*|_{\operatorname{Ran}A})\otimes I_{K_q}.}
\tag{3.3}
$$

对任意完整原源 $r$，令 $r_0=P_{\ker D}r$、$r_\perp=(I-P_{\ker D})r$。因为 $\ker A=\mathbb Ce_0$，
$$
A_0=A|_{e_0^\perp}:e_0^\perp\longrightarrow\operatorname{Ran}A
$$
是原物理内积中的有限维同构。真实左最小者准确分裂为
$$
\boxed{
E_q^\dagger r
=(A_0^{-1}\otimes I)r_0+E_q^\dagger r_\perp,
}
\tag{3.4}
$$
两项正交，第一项只在第 $q$ 孔层，第二项的顶层 primitive 投影为零。因此
$$
\boxed{
\mu_q(r)^2
=\|(A_0^{-1}\otimes I)r_0\|^2+\mu_q(r_\perp)^2.
}
\tag{3.5}
$$
这个结论仅分裂真实左源 Gram。没有声称原完整右旗 Gram $G_q$ 或裸最小源费用也与 $P_{\ker D}$ 交换，因而不能据此对一般来源分别套用已经证明的三 Gram 特例。

## 4. 原真实头高幂及统一系数界

[原全整数窗逐步证明](../notes/2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md) §5 式 (5.3) 已由真实进位计数证明，两种原头都满足
$$
\boxed{\|A_m^t\|\le6^t
\exp\!\left[-\gamma(t-m)_+^4\right],\qquad
\gamma=\frac{770}{256}.}
\tag{4.1}
$$
这里只使用这条原头界，不用任意同维幂零头替换 $A_m$。

由 $q\ge4d$、$m+1\le d$ 及 $T=d-1$，
$$
q+2T+1\le\frac32q,\qquad
m+q+2T+1\le\frac74q.
$$
于是
$$
\mathcal L\le
512\sqrt{\frac32}\left(\frac74\right)^{3/2}q^2
<2048q^2.
$$
令
$$
\Theta=\log(12\mathcal L).
$$
则对全部原合法 $q$，
$$
\boxed{\Theta<\frac12d^3+11.}
\tag{4.2}
$$
每一个提升阶的整个孔直和范数因此至多
$$
w_t:=\exp\!\left[t\Theta-\gamma(t-m)_+^4\right].
\tag{4.3}
$$
同一 $t$ 不同输入层的输出正交，所以 (4.3) 没有输入孔层数 $q$ 的额外因子。

## 5. 最后 $d/8$ 层与远低部之间的交叉小量

沿前稿按
$$
\mathscr P_{\rm lo}=\mathbb C^d\otimes\bigoplus_{n\le q-d+1}K_n,
\quad
\mathscr P_{\rm bd}=\mathbb C^d\otimes\bigoplus_{q-d+2\le n\le q}K_n
$$
分块。令 $r=d/8$（$m\ge5$ 时为整数），并在边界坐标内再取
$$
\mathscr P_{\rm top}
=\mathbb C^d\otimes\bigoplus_{q-r+1\le n\le q}K_n.
\tag{5.1}
$$
其正交投影分别记为 $P_{\rm lo},P_{\rm bd},P_{\rm top}$。

若输入属于 $\mathscr P_{\rm top}$，$\mathcal C_L$ 的非零输出必在孔层
$$
[q-r+2,q].
$$
而从输入 $n\le q-d+1$ 到这个输出带，必须提升至少
$$
t\ge(q-r+2)-(q-d+1)=d-r+1.
\tag{5.2}
$$
因此，令 $P_J$ 为物理孔带 $J=[q-r+2,q]$ 的投影，有
$$
P_{\rm lo}\mathcal D P_{\rm top}
=(P_J\mathcal C_LP_{\rm lo})^*
 (\mathcal C_LP_{\rm top}).
\tag{5.3}
$$
由 (4.3) 和 (5.2)，
$$
\|P_J\mathcal C_LP_{\rm lo}\|
\le\sum_{t=d-r+1}^{d-1}w_t,
\qquad
\|\mathcal C_LP_{\rm top}\|
\le\sum_{t=1}^{r-1}w_t.
\tag{5.4}
$$
两个和分别不超过 $d$ 项，且没有对不同源孔层再次求和。

当 $m\ge5$ 时，$m/d\le5/32$。第一和中的每个 $t$ 都有
$$
t-m\ge\left(\frac78-\frac5{32}\right)d=\frac{23}{32}d,
\qquad t\Theta\le d\Theta.
$$
第二和只用 $t\Theta\le r\Theta$ 并舍去负四次项。故
$$
\begin{aligned}
\|P_{\rm lo}\mathcal D P_{\rm top}\|
&\le d^2\exp\!\left[(d+r)\Theta
-\gamma\left(\frac{23}{32}\right)^4d^4\right]\\
&\le d^2\exp\!\left[-\frac{32241313}{134217728}d^4
+\frac{99}{8}d\right].
\end{aligned}
\tag{5.5}
$$
这里准确的有理数恒等式为
$$
\gamma\left(\frac{23}{32}\right)^4-\frac9{16}
=\frac{32241313}{134217728}>\frac6{25}.
$$
对 $d\ge32$，$2\log d+(99/8)d\le d^4/25$，所以
$$
\boxed{\|P_{\rm lo}\mathcal D P_{\rm top}\|
\le e^{-d^4/5}.}
\tag{5.6}
$$
这是实际整个 Hilbert 块之间的算子范数估计，包括任意远位置支撑和该条带内任意非正交的 $Q_t$ 组合。

## 6. 真正 Schur 修正和极小补全的费用

写
$$
\mathcal D=
\begin{pmatrix}D_{00}&D_{01}\\D_{10}&D_{11}\end{pmatrix}
\quad\text{于 }\mathscr P_{\rm lo}\oplus\mathscr P_{\rm bd},
$$
并保留真实 Schur 补
$$
D_{\rm eff}=D_{11}-D_{10}D_{00}^{-1}D_{01}.
$$
由 $D_{00}\succeq I$ 及 (5.6)，
$$
\boxed{
0\preceq P_{\rm top}(D_{11}-D_{\rm eff})P_{\rm top}
\preceq e^{-2d^4/5}I_{\mathscr P_{\rm top}}.
}
\tag{6.1}
$$
对任意边界坐标 $b\in\mathscr P_{\rm top}$，在保持完整边界坐标 $b$ 不变时，使真实左能量最小的低坐标是
$$
a_{\min}=-D_{00}^{-1}D_{01}b,
$$
且准确满足
$$
\boxed{\|a_{\min}\|\le e^{-d^4/5}\|b\|.}
\tag{6.2}
$$
对应的完整左能量与只嵌入 $b$ 的左能量之差，是 (6.1) 的二次型，因而至多 $e^{-2d^4/5}\|b\|^2$。

对一般原来源，边界坐标还可能含有
$$
\mathscr P_{\rm bd}\ominus\mathscr P_{\rm top}.
$$
这些中间坐标不能置零。本文没有控制它们与 $B_1$ 的真实约束、裸费用或 $C_1^*c^\flat$ 的比较。因此 (6.1)--(6.2) 不是全源左费上界，也没有给出原所需的 $C_m=O(e^{d^3/4}/d)$ 子序列。
