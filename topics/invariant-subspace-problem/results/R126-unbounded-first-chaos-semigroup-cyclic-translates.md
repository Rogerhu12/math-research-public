# R126：不可和正第一chaos加任意有界交换子像循环

**当前范围更新：** 任意相位的ℓ²第一 chaos 循环性已由 R125 另证；本文额外允许任意有界交换子像 C1 扰动。

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：完整证明，暂未分配结果号。使用已证 R20/R39 的实际半群及 R88 的交换子强闭包；不使用纯模型核向实际模型的移植。

## 1. 主定理

设
$$
t_j\ge0,\qquad \sum_jt_j^2<\infty,\qquad \sum_jt_j=\infty,
$$
并令
$$
u=\sum_{j\ge0}t_j\chi_j\in H_{\le1}.
\tag{1.1}
$$
这是一个真正不具有有界乘子的第一 chaos 向量，因为其第一阶系数不在 $\ell^1$（R88）。

**定理 1.1。** 对任意有界交换子 $C\in\{A\}'$，
$$
\boxed{h=u+C1\text{ 对实际 }A\text{ 循环。}}
\tag{1.2}
$$
更具体地，存在有界交换子 $R$，使
$$
Rh=1.
\tag{1.3}
$$
所以 $h$ 自动非零。

特别地，对任意复常数 $a_*$、任意 $(b_j)\in\ell^1$，
$$
a_*+\sum_j(t_j+b_j)\chi_j
\tag{1.4}
$$
都循环。乘以任意非零复数后仍循环，因此允许 $t_j$ 具有一个共同复相位，再加任意 $\ell^1$ 第一阶扰动。

本定理还允许 $C1$ 具有无限 Walsh 次数；只要求 $C$ 是有界交换子。

## 2. 已证真实半群的精确接口

沿用
$$
N_j=A^{2^j}/d_j,\qquad
Y_j=N_j(I+N_j)^{-1},\qquad
V_j=I-2Y_j.
$$
有 $V_j1=\chi_j$。

R20 构造实际半群
$$
S_m(s)=\prod_{j<m}\exp[-st_j(I-2N_j)],
\qquad
S(s)=\operatorname*{s-lim}_{m\to\infty}S_m(s).
\tag{2.1}
$$
它满足：

- $S(s)$ 强连续，与 $A$ 交换；
- $S_m(s)\to S(s)$ 在每个有限 $s$ 区间上对每个固定向量一致强收敛；
- 对每个有限 $L$，
  $$
  \sup_{m,\ 0\le s\le L}\|S_m(s)\|<\infty;
  \tag{2.2}
  $$
- 因 $\sum t_j=\infty$，R39 给 $S(1)$ 拟幂零，因此对于每个实数 $\omega$，存在有限 $M_\omega$，使
  $$
  \boxed{\|S(s)\|\le M_\omega e^{\omega s}\qquad(s\ge0).}
  \tag{2.3}
  $$

最后一项可直接由半群性质复核：整数 $n$ 上
$\|S(1)^n\|^{1/n}\to0$，再把 $s=n+r$、$0\le r<1$，用强连续半群在 $[0,1]$ 上的一致有界性即可。这里不是从一个形式无界和猜测空谱或增长界。

## 3. 把归一化幂生成元改成精确 Walsh 乘子

有限和之间的差为
$$
E_m=\sum_{j<m}t_j\bigl[V_j-(I-2N_j)\bigr]
=2\sum_{j<m}t_jN_j^2(I+N_j)^{-1}.
\tag{3.1}
$$
实际关系 $N_j^2=\eta_jN_{j+1}$ 以及
$$
\|(I+N_j)^{-1}\|\le \frac2{1-\eta_j}
$$
给
$$
\|t_jN_j^2(I+N_j)^{-1}\|
\le C t_j\eta_j.
$$
由于 $t\in\ell^2$、$\eta\in\ell^2$，
$$
\sum_jt_j\eta_j<\infty.
$$
故
$$
\boxed{E_m\longrightarrow E\in\mathcal A\quad\text{于算子范数}.}
\tag{3.2}
$$
所有 $E_m,E,N_j,V_j$ 彼此交换，也与任意 $C\in\{A\}'$ 交换。

给定定理中的 $C$，定义有限有界算子
$$
H_m=C+\sum_{j<m}t_jV_j
$$
及其指数
$$
T_m(s)=e^{-sH_m}.
$$
因为全部因子交换，精确有
$$
\boxed{
T_m(s)=e^{-s(C+E_m)}S_m(s).
}
\tag{3.3}
$$
由 (2.1)—(2.2)、(3.2)，
$$
T_m(s)\longrightarrow T(s):=e^{-s(C+E)}S(s)
\tag{3.4}
$$
在有限时间区间上对每个固定向量一致强收敛，而且有限 $T_m$ 在这些区间上一致有界。

$C+E$ 与 $S(s)$ 交换：它与每个有限 $S_m(s)$ 交换，强极限保留等式。因此 $T$ 本身也是与 $A$ 交换的强连续半群。

由 (2.3)，乘上至多指数增长的 $e^{-s(C+E)}$ 不影响任意指数快衰减：
$$
\boxed{
\text{每个 }\omega\in\mathbb R\text{ 都有 }M'_\omega<\infty,\quad
\|T(s)\|\le M'_\omega e^{\omega s}.
}
\tag{3.5}
$$
不需要 $C$ 正、正规或自伴。

## 4. 在常向量上取有限积分恒等式的极限

由于 $V_j1=\chi_j$，
$$
h_m:=H_m1=C1+\sum_{j<m}t_j\chi_j
\longrightarrow h
\quad\text{于 }H.
\tag{4.1}
$$
每个有限有界生成元满足
$$
T_m(s)1-1=-\int_0^sT_m(v)h_m\,dv.
\tag{4.2}
$$

固定有限时间 $s$。局部一致范数界及 (4.1) 给
$$
\sup_{0\le v\le s}\|T_m(v)(h_m-h)\|\to0.
$$
又 (3.4) 对固定 $h$ 在该时间区间上一致强收敛，所以
$T_m(v)h_m\to T(v)h$ 一致于 $v\in[0,s]$。故可在 Hilbert 空间值积分中取极限：
$$
\boxed{
T(s)1-1=-\int_0^sT(v)h\,dv.
}
\tag{4.3}
$$

这同时严证常向量属于新半群生成元的定义域，且负生成元把 $1$ 送到 $h$。本稿不把整个生成元定义域等同于未经证明的逐项收敛域；证明循环性其实只需要 (4.3)。

## 5. 强积分给有界反向算子

由 (3.5)，可选一个指数负界，故
$$
\int_0^\infty\|T(v)\|\,dv<\infty.
$$
对每个 $x\in H$，定义
$$
Rx=\int_0^\infty T(v)x\,dv
\tag{5.1}
$$
为 Hilbert 空间值强积分。于是 $R$ 有界，且
$$
\|R\|\le\int_0^\infty\|T(v)\|\,dv.
$$
无穷上限截断在算子范数下收敛。不需要假设半群在 $B(H)$ 范数下连续。

每个 $T(v)$ 都与 $A$ 交换，故强积分也满足 $RA=AR$。让
$s\to\infty$ 于 (4.3)，(3.5) 使 $T(s)1\to0$，得到
$$
\boxed{Rh=1.}
\tag{5.2}
$$

令 $M_h=\overline{\mathbb C[A]h}$。R88 的
$$
\{A\}'=\overline{\mathbb C[A]}^{\mathrm{SOT}}
$$
保证每个有界交换子保持 $M_h$：对固定 $x\in M_h$ 用强逼近与闭性即可。因此 $Rh\in M_h$，即 $1\in M_h$。常向量 $1$ 循环，故 $M_h=H$，证明定理。

这里使用的是明确的有界反向算子，而不是由一个形式空谱或稠密近似直接宣称循环性。

## 6. 第一 chaos 推论与范围

对 (1.4)，取
$$
C=a_*I+\sum_jb_jV_j\in\mathcal A.
$$
因为 $(b_j)\in\ell^1$ 且 $\sup_j\|V_j\|<\infty$，算子级数范数收敛，$C1=a_*+\sum_jb_j\chi_j$，故定理适用。

例如任意复常数及任意 $\ell^1$ 扰动后的
$$
\sum_{j\ge0}(j+1)^{-p}\chi_j,\qquad \frac12<p\le1,
$$
均循环。这些系数不在 $\ell^1$，所以并未被全部有界第一 chaos 的结论自动涵盖。

也可把 $t_j$ 放在任意稀疏位集，只需保持非负、平方可和但不可和。所有对 $\eta_j$ 的误差仍由 $\sum t_j\eta_j<\infty$ 支付。

本稿没有涵盖任意相位的不可和 $\ell^2$ 系数，例如无法化为共同相位非负序列加 $\ell^1$ 扰动的排列。没有宣称所有第一 chaos 已循环，更没有宣称一般 $L^2$ 循环性或完整 ISP 已解决。
