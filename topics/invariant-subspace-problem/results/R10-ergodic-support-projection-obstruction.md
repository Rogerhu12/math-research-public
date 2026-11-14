# R10：遍历加权复合算子的近不变支集投影只能有标量弱极限

**状态：已证明的中间结论；不声称新颖；没有解决完整 Hilbert ISP。**

日期：2026-11-12。会话：Astra-ISP-b382c564；并行推导：defect-route。

本条适用于 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 的正权加权 odometer。它说明：即使从整个可测支集族中选择近不变投影，而不限于某一组二进制截断，其弱极限也不能给出 [R7](R7-weak-projection-support-and-graph-criterion.md) 所需的非零真支撑。结论只针对支集型子空间，不排除一般闭线性不变子空间。

## 1. 主命题

设 $(X,\mu)$ 是标准概率空间，$\tau:X\to X$ 为可逆、保测、遍历变换，$w\in L^\infty(X)$ 满足 $|w|>0$ 几乎处处。定义

$$
U_\tau f=f\circ\tau^{-1},\qquad A=M_wU_\tau
\quad\text{作用于 }L^2(X,\mu).
$$

给定任意可测集列 $E_n\subset X$，令

$$P_n=M_{\mathbf1_{E_n}},\qquad
\varepsilon_n=\|(I-P_n)AP_n\|.$$

若 $\varepsilon_n\to0$，则：

1. $\mu(\tau E_n\triangle E_n)\to0$。
2. $P_n$ 的每个 WOT 聚点均为 $cI$，其中 $0\le c\le1$。
3. 若 $\mu(E_n)\to c$，则整个序列 $P_n\to cI$ 于 WOT。
4. 不可能同时存在固定 $x,y\in L^2(X)$、$y\ne0$ 和 $\delta>0$，使

   $$\liminf_n\|P_nx\|\ge\delta,\qquad\|P_ny\|\to0.$$

在第 2 项中，$c=0$ 给零支撑，$c>0$ 给全空间支撑；$0<c<1$ 时 $P=cI$ 与 $I-P$ 均无核。因此这些极限均不能直接产生非零真不变子空间。

## 2. 泄漏范数的精确计算

对任意 $f\in L^2$，有

$$
((I-P_n)AP_nf)(x)
=\mathbf1_{E_n^c}(x)w(x)\mathbf1_{E_n}(\tau^{-1}x)f(\tau^{-1}x).
$$

所以

$$
(I-P_n)AP_n
=M_{w\mathbf1_{\tau E_n\setminus E_n}}U_\tau.
\tag{2.1}
$$

$U_\tau$ 酉，而乘法算子的范数等于乘子的本质上确界，故

$$
\varepsilon_n
=\operatorname*{ess\,sup}_{x\in\tau E_n\setminus E_n}|w(x)|.
\tag{2.2}
$$

因此，除去零测集，泄漏集合 $L_n=\tau E_n\setminus E_n$ 包含于 $\{|w|\le\varepsilon_n\}$。由 $|w|>0$ 几乎处处，

$$
\mu(L_n)\le\mu\{|w|\le\varepsilon_n\}\longrightarrow0.
\tag{2.3}
$$

这里不要求 $\varepsilon_n$ 单调：给定 $\eta>0$，最终 $\varepsilon_n\le\eta$，再令 $\eta\downarrow0$，利用 $\mu\{|w|\le\eta\}\downarrow\mu\{w=0\}=0$。

保测性给 $\mu(\tau E_n)=\mu(E_n)$，所以两侧差集测度相等。于是

$$
\mu(\tau E_n\triangle E_n)
=2\mu(\tau E_n\setminus E_n)\longrightarrow0.
\tag{2.4}
$$

这是第 1 项。

## 3. 从 $L^\infty$ 弱星极限到 WOT

记 $h_n=\mathbf1_{E_n}$。由于 $0\le h_n\le1$，可以抽取弱星收敛子列 $h_{n_k}\overset{*}{\rightharpoonup}h$ 于 $L^\infty$，其中 $0\le h\le1$；标准概率空间保证 $L^1$ 可分，所以这里可使用子列。若只讨论一般概率空间，相同论证可改用子网。

先说明乘法算子 WOT 收敛与乘子弱星收敛相同。对 $f,g\in L^2$，

$$\langle M_{h_n}f,g\rangle=\int_X h_nf\overline g\,d\mu,$$

而 $f\overline g\in L^1$。反过来，每个 $k\in L^1$ 都可以写成 $f\overline g$：取 $g=|k|^{1/2}$，在 $k\ne0$ 处取 $f=k/|k|^{1/2}$，其余处令 $f=0$。因此乘子的一切 $L^1$ 配对正好由这些矩阵元覆盖。

特别地，任何收敛的乘子子列给 WOT 极限 $M_h$，而任意 WOT 聚点也必对应这样的弱星极限。后一点亦可由乘法代数的 WOT 闭性直接推出；这里不需要另行假定该闭性。

由 (2.4)，

$$\|h_n\circ\tau^{-1}-h_n\|_1\longrightarrow0.\tag{3.1}$$

这些差函数的 $L^\infty$ 范数至多一。因此它们也弱星收敛于零。为核对这一点，对任意 $k\in L^1$ 先取有界截断 $k_K$，则

$$
\left|\int(h_n\circ\tau^{-1}-h_n)k\,d\mu\right|
\le K\|h_n\circ\tau^{-1}-h_n\|_1+\|k-k_K\|_1;
$$

先令 $n\to\infty$，再令 $K\to\infty$。

保测变换的复合在弱星拓扑下连续：

$$\int(h_n\circ\tau^{-1})k\,d\mu
=\int h_n(k\circ\tau)\,d\mu,$$

且 $k\circ\tau\in L^1$。因此沿收敛子列，(3.1) 给出

$$h\circ\tau^{-1}=h\quad\text{几乎处处}.$$

由遍历性，$h$ 必为常数 $c\in[0,1]$。例如，每个有理数 $t$ 对应的水平集 $\{h>t\}$ 都不变，故测度只能是零或一；这迫使 $h$ 几乎处处常值。由上一段的乘法算子对应，WOT 聚点就是 $cI$，第 2 项得证。

又因为 $\int h_n\,d\mu=\mu(E_n)$，若后者收敛于 $c$，每个弱星聚点都只能是该常数 $c$。单位球弱星紧且可度量，所以极限唯一便给整个序列弱星收敛于 $c$，也即第 3 项的 WOT 收敛。等价地，可以反证：若某个固定 $L^1$ 配对不趋于所需值，取坏子列，再取弱星收敛子子列，就与唯一的常数聚点矛盾。

## 4. 固定锚点不可能同时成立

若第 4 项中的两个条件同时成立，抽取任一 WOT 收敛子列，其极限按第 2 项为 $cI$。正交投影性质给

$$
c\|x\|^2=\lim_k\langle P_{n_k}x,x\rangle
=\lim_k\|P_{n_k}x\|^2\ge\delta^2,
$$

故 $c>0$。但同理

$$c\|y\|^2=\lim_k\|P_{n_k}y\|^2=0,$$

与 $y\ne0$ 矛盾。

如果某个聚点为零或恒等，则沿该子列投影实际强收敛于零或恒等。例如，$P_n\to0$ 于 WOT 时，$\|P_nx\|^2=\langle P_nx,x\rangle\to0$；$I$ 的情形应用于 $I-P_n$。这些强极限同样是平凡的。

## 5. 二进制 odometer 上的精确例子

现在取 $X=\mathbb Z_2$ 配 Haar 概率，$\tau(x)=x+1$。令实数列 $a_r>0$ 单调下降至零，并定义

$$w(y)=a_{v_2(y)}\quad(y\ne0),\qquad Af(y)=w(y)f(y-1).$$

$y=0$ 处可以任意定义，不改变 $L^2$ 算子。$\tau$ 保测且遍历：若函数对加一不变，则对所有整数平移不变；整数在 $\mathbb Z_2$ 中稠密，平移表示在 $L^2$ 上强连续，故该函数对所有平移不变，从而为常数。也可用有限商上的循环平移证明。

对每个 $N\ge1$，令

$$
E_N=\{x:x\bmod2^N\in\{2^{N-1},\ldots,2^N-1\}\},
\qquad P_N=M_{\mathbf1_{E_N}}.
$$

$E_N$ 恰是第 $N$ 个二进制位为一的集合（最低位计作第一位），故 $\mu(E_N)=1/2$。两侧集合均为正测度的无原子集，所以 $P_N$ 的秩和余秩都无限。

加一后的唯一出口为模 $2^N$ 的回绕：

$$\tau E_N\setminus E_N=\{y:y\equiv0\pmod{2^N}\}.$$

该集合上 $v_2(y)\ge N$；其中 $v_2(y)=N$ 的部分测度为 $2^{-N-1}>0$。由单调性和 (2.2)，

$$\|(I-P_N)AP_N\|=a_N\longrightarrow0.\tag{5.1}$$

这个泄漏算子的秩是无限的：在输出集合 $\{y:v_2(y)=N\}$ 上，权恒为 $a_N>0$；对应输入集合经 $\tau$ 与它保测同构，所以泄漏在一整个无限维 $L^2$ 子空间上是 $a_N$ 倍的酉映射。不能将这里的近不变性冒称为秩一缺陷。

另一方面，若 $g$ 只依赖固定的前 $m$ 个二进制位，则 $N>m$ 时独立性给

$$\int\mathbf1_{E_N}g\,d\mu=\frac12\int g\,d\mu.$$

有限位柱函数在 $L^1(\mathbb Z_2)$ 中稠密，且 $\|\mathbf1_{E_N}\|_\infty\le1$，所以

$$\mathbf1_{E_N}\overset{*}{\rightharpoonup}\frac12,
\qquad P_N\longrightarrow\frac12I\quad\text{于 WOT}.\tag{5.2}$$

对于常数单位向量 $1$，有 $\|P_N1-\tfrac121\|_2=1/2$，故此收敛不是 SOT 收敛。这精确展示了当前模型最自然的二进制近不变半空间如何退化：缺陷趋零，但弱极限在零和一均无核。

## 6. 对 R9 的应用及范围

[R9](R9-radial-odometer-and-nilpotent-approximants.md) 的标量模型满足 $w(y)=a_{v_2(y)}>0$ 几乎处处，且 $a_r\downarrow0$，因此本条全部结论适用。任何可测支集型近不变投影序列，都不能通过 WOT 支撑方法给出该 $A$ 的非零真闭不变子空间；第 5 节给出缺陷恰为 $a_N$ 的具体序列。

这是对**一类构造方法**的完整障碍定理。一般闭线性子空间不必由可测支集描述。证明这些更一般子空间存在或不存在，仍是本课题尚未解决的数学部分。
