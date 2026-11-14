# 2026-11-14 — 原乘子与低角首像尾带

**状态：下列同预算像包含已证明；主目标未完成。**
本条继续 general-double-contact 笔记的实际第三块尾带。
它覆盖一些不能逐系数除以三个 $t$ 因子的来源，但仍未判定全部
低角首核。没有占用 R561，也没有增加任何中央零。

## 1. 同一有限自由来源上的两个真乘子

沿用 R491、R555 的原格
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n\,\mathcal O[t]_{\le e_n},
\qquad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
\quad h_7=7+4t+16t^2,\quad d=1+8t.
\tag{1}
$$
本条只为简化下标，将 R555 的 $e_{n+1}$ 写成 $e_n$；准确值为
$$
e_n=\lfloor9n/2\rfloor+4-3A_n-B_n+C_n.
\tag{2}
$$
取 $\mathcal O=\mathbf Z_p$，$p=6s-1>83$。所有来源和公共 carrier
均与原题相同。

原 $S=S_{34}$ 以及一个十二权计算来源为
$$
S=\frac{Yt(t-1)h_7}{7},\qquad
H=Y^{12}q_{12}
=\frac{Y^{12}t^3h_7^3(t-1)^4}{d^6}.
\tag{3}
$$
因此
$$
S\mathcal W_D\subset\mathcal W_{D+1},\qquad
H\mathcal W_{D-12}\subset\mathcal W_D \quad(D\ge12).
\tag{4}
$$

第一项不是只按形式阶数判断。对每个 $n$，令
$\Delta A=A_{n+1}-A_n$，其余同理，则准确的基列乘法为
$$
S\,Y^nq_n B
=Y^{n+1}q_{n+1}
\frac{t^{1-\Delta A}h_7^{1-\Delta A}
(t-1)^{1-\Delta B}d^{\Delta C}}7\,B.
\tag{5}
$$
全部指数非负。乘子的次数为
$4-3\Delta A-\Delta B+\Delta C$，而由 (2)，目标次数帽的准确余量是
$$
e_{n+1}-e_n-
(4-3\Delta A-\Delta B+\Delta C)
=
\begin{cases}
0,&n\text{ 偶},\\
1,&n\text{ 奇}.
\end{cases}
\tag{6}
$$
这支付了所有余类，而不是只支付大 $n$。

第二项使用准确周期
$$
q_{n+12}=q_{12}q_n,\qquad e_{n+12}=e_n+47.
\tag{7}
$$
这里的自由系数帽增量是 **47**；它不是
$A_n+e_n$ 的十二权增量 50。
两项乘法在显示来源格中的像均 $p$-饱和：
(5) 的多项式首系数是单位，逐块作整多项式除法即可；
(7) 只是每个高权分量中保留一个低次自由子格。
这不声称物理评价像 $p$-饱和。

置 $N_D=\sum_{n=0}^D(e_n+1)$。特别
$$
N_{11}=317,\qquad
\operatorname{rank}_{\mathcal O}
(\mathcal W_D/H\mathcal W_{D-12})
=N_D-N_{D-12}=47D-200.
\tag{8}
$$
其显示自由补格是全部 $n<12$ 分量，加上每个 $12\le n\le D$
分量的最高 47 个自由 $t$ 单项式。
这是来源商的准确描述，不是首像或余核的秩公式。

## 2. 保全部低行与原 $U_0$ 的实际三尾

设 $\bar P\in\ker\bar J$，保原共同 carrier 和
$\mathcal E_{\rm tot}=Y\partial_Y+40$。记
$$
W_i(P)=\left.\mathcal E_{\rm tot}^{\,i}P\right|_{Y=\bar g(w),\,t=t(w)}.
$$
所以 $W_0(P),W_1(P)\in w^s k[[w]]$，且
$W_2(P)\in w^\ell k[[w]]$。设
$$
\nu=\operatorname{ord}_wW_2(P)<\infty,\qquad
\delta=\nu-\ell\ge0.
\tag{9}
$$
仍取原 $1\le\ell<s-13$ 及
$M=c_*U_0m_{13}J$，没有把 $m_{13}$ 可逆化。

**实际像包含。** 若同预算首核向量满足下列任一条件：
$$
\bar P\in S^3\overline{\mathcal W}_{D-3},
\qquad\text{或}\qquad
\bar P\in H\overline{\mathcal W}_{D-12},
\tag{10}
$$
则
$$
\operatorname{span}_k
\{\epsilon^2w^{\ell+10+\delta},\ldots,
  \epsilon^2w^{\ell+12}\}
\subset\operatorname{im}\bar M
\quad(0\le\delta<3).
\tag{11}
$$
当 $\delta\ge3$，没有新的尾带断言，而且 R468 在该向量上的三轴
首次变化本来就超过第三块末端。

**证明。** 写 $P=AQ$，其中 $A=S^3$ 或 $H$。
它们在原物理 germ 上都准确为
$$
A_0(w)=w^3u_A(w),\qquad u_A(0)\ne0.
$$
原 $S_0(w)=w\,u_S(w)$，$u_S(0)\ne0$。
$A$ 的相对 charge 分别为 $c_A=3,12$。
由同一个 Euler 算子的乘积公式，
$$
\begin{aligned}
W_0(Q)&=A_0^{-1}W_0(P),\\
W_1(Q)&=A_0^{-1}\{W_1(P)-c_AW_0(P)\},\\
W_2(Q)&=A_0^{-1}
 \{W_2(P)-2c_AW_1(P)+c_A^2W_0(P)\}.
\end{aligned}
\tag{12}
$$
这些是有意义的幂级数等式，因为 $Q$ 是 (10) 中的真来源，
不是从物理形式级数任意除出来的列。

由 (4)，$Q,SQ,S^2Q$ 全部属于原 $\overline{\mathcal W}_D$。
它们的前两块阶数至少为 $s-3+j$，$j=0,1,2$；
乘原 $w^{13}$ 后均超过第一、第二块的长度 $s$。
因此它们在整个原 $\bar M$ 中的前两块确实为零。

第三块在目标截断内准确等于
$$
\frac{a_0^2}{2}\epsilon^2w^{13}
S_0(w)^j A_0(w)^{-1} W_2(P),
\qquad j=0,1,2.
\tag{13}
$$
(12) 中其他项以及乘 $S^j$ 产生的低 Euler 项的阶数至少为
$s-3+j$，再乘 $w^{13}$ 后严格超过 $\ell+12$，所以是在
**原第三块内** 消失，未删去可见 carry。
保留 $j=0,\ldots,2-\delta$，(13) 的首阶依次为
$\ell+10+\delta,\ldots,\ell+12$，首系数全为单位。
这些实际列是同一末端带的可逆三角基。

最后完整 $c_*U_0$ 乘法在每条第三块末端带上是可逆三角变换；
它保持该带且不会制造较低块，所以 (11) 属于原物理首像。
证毕。

## 3. 对低角边界的准确用途

对于 general-double-contact 笔记中
$r=\ell$、局部 $F_{YY}(0,1)\ne0$ 的二重候选，
有 $\nu=\ell$。若该候选满足 (10)，(11) 吸收 R468 的全部
三条实际高轴首次变化，即使
$$
\tau(P)=\min_{B_n\ne0}\operatorname{ord}_tB_n\le2.
$$
因此逐系数 $t$ 除法不是唯一已付的尾带来源。

一旦有任意一个首核向量满足 (10) 且 $\nu=\ell$，
所得是整个固定原目标的三条末端行都在首像中的结论；
于是这三行对其他 $\ker\bar J$ 向量也不再产生首余核类。
这仍不处理一般 $K_1(M)$ 的另外三条第一 carry 尾行，
也不替同一整提升上的 $d_2$ 作结论。

(8) 可以显示十二权内部以外只剩 $O(D)$ 个来源方向，
但不能据此推出物理核或 forcing 的边界容量。
尤其没有证明
$$
\ker\bar J\cap
(S^3\overline{\mathcal W}_{D-3}+H\overline{\mathcal W}_{D-12})
=
(\ker\bar J\cap S^3\overline{\mathcal W}_{D-3})
+
(\ker\bar J\cap H\overline{\mathcal W}_{D-12}).
$$
两个来源片段的低行可以互相抵消，故不能把 (11) 免费推广到该和。

本条也没有发现一个此前未核过的实际低预算候选。
下一接口仍是这些内部子核之外的真实低角边界、
一般 $K_1(M)$ 的完整六尾和同一修正的第二障碍；
原完整中央零只约束已付的固定来源。
