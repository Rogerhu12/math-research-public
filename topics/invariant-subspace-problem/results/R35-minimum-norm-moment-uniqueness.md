# R35：范数不增的完全矩匹配：全 Hilbert 空间中的有限柱目标唯一性

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94，子任务 `centered_literature`。

**状态：已证明的中间结论。** 匹配向量允许属于整个 $L^2(\mathbb Z_2)$，没有有限 chaos 或乘积假设。若比较目标是 $C$-实有限柱函数，全部复双线性平方矩相同且范数不增，则匹配向量只能是目标的整体正负号。本条不是一般目标/一般范数的矩唯一性，也没有解决普通 ISP，不主张文献新颖性。

依赖 R9、R12、R24，以及 R26 §3 已证的超快连续系数循环引理。

## 1. 结论

设

$$
(Cf)(y)=\overline{f(-1-y)},\qquad
B(f,g)=\langle f,Cg\rangle,\qquad Q_n(f)=B(A^nf,f).
\tag{1.1}
$$

$A$ 是 R9 的具体正权 odometer。令 $h\ne0$ 为有限柱函数，满足 $Ch=h$。若任意 $g\in H$ 满足

$$
Q_n(g)=Q_n(h)\quad(n\ge0),\qquad \|g\|\le\|h\|,
\tag{1.2}
$$

则

$$
\boxed{g=h\quad\text{或}\quad g=-h.}
\tag{1.3}
$$

特别地，当 $h=1$ 时，任何不同于 $\pm1$ 的完全平方矩匹配向量（如果存在）必须满足 $\|g\|>1$。

## 2. 零阶矩强迫范数等号和 $C$-实性

记 $H_0=\|h\|>0$。因为 $Ch=h$，有 $Q_0(h)=H_0^2$。由 (1.2)

$$
H_0^2=\langle g,Cg\rangle
\le|\langle g,Cg\rangle|\le\|g\|^2\le H_0^2.
$$

故 $\|g\|=H_0$，且内积 $\langle g,Cg\rangle=\|g\|^2$ 是正实数。直接展开

$$
\|g-Cg\|^2=2\|g\|^2-2\operatorname{Re}\langle g,Cg\rangle=0
$$

得到 $Cg=g$。于是对 $f=h,g$ 均有

$$
B(A^nf,f)=\langle A^nf,f\rangle.
\tag{2.1}
$$

这里的转换依赖范数假设，不能对一般复双线性矩匹配向量无条件使用。

## 3. 精确匹配压低所有高位影响

令 $\chi_j=(-1)^{b_j}$，对有限位集 $S$ 记 $\chi_S=\prod_{j\in S}\chi_j$。这些 Walsh 函数形成 $H$ 的正交单位基。写

$$
g=\sum_{S\text{ 有限}}\widehat g(S)\chi_S.
$$

第 $k$ 位的影响定义为

$$
I_k(g)=\sum_{S\ni k}|\widehat g(S)|^2.
\tag{3.1}
$$

在每位的基 $(1,\chi_k)$ 中，$E_k=e_{10}$ 的矩阵为

$$
E_k=\frac12\begin{pmatrix}1&1\\-1&-1\end{pmatrix},
\qquad \frac{E_k+E_k^*}{2}
=\frac12\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

因此对**任意** $g\in H$，

$$
\operatorname{Re}\langle E_kg,g\rangle
=\frac12\|g\|^2-I_k(g).
\tag{3.2}
$$

选 $d$ 使 $h$ 只依赖低于第 $d$ 位的数字。对 $k\ge d$，其第 $k$ 位是参考向量 $1$，故

$$
\langle E_kh,h\rangle=\frac12H_0^2.
\tag{3.3}
$$

R12 给 $F_k=A^{2^k}/\|A^{2^k}\|$ 满足

$$
\|F_k-E_k\|=\eta_k:=a_{k+1}/a_k.
$$

全部平方矩相等及 (2.1) 意味着 $\langle F_kg,g\rangle=\langle F_kh,h\rangle$。利用 $\|g\|=\|h\|=H_0$，得到

$$
\left|\langle E_kg,g\rangle-\frac12H_0^2\right|
\le2H_0^2\eta_k.
$$

结合 (3.2)，即

$$
\boxed{I_k(g)\le2H_0^2\eta_k\qquad(k\ge d).}
\tag{3.4}
$$

## 4. 从影响尾到一致连续代表：分别处理条件期望与取零尾

令 $P_m$ 是对最低 $m$ 位 sigma 代数取条件期望的正交投影。它保留恰好那些 $S\subseteq\{0,\dots,m-1\}$ 的 Walsh 系数。因此由每个未保留的 $S$ 至少含一个 $k\ge m$，对 $m\ge d$ 有

$$
\|g-P_mg\|_2^2
\le\sum_{k\ge m}I_k(g)
\le2H_0^2\varepsilon_m,
\qquad \varepsilon_m=\sum_{k\ge m}\eta_k.
\tag{4.1}
$$

这个求和允许一个 Walsh 集合被计数多次，只用于上界；没有要求有限 chaos。

记 martingale 增量 $D_m=P_{m+1}g-P_mg$。它是深度 $m+1$ 的柱函数，故由均匀有限空间的直接范数比较

$$
\|D_m\|_\infty\le2^{(m+1)/2}\|D_m\|_2
\le H_0\,2^{(m+2)/2}\sqrt{\varepsilon_m}.
\tag{4.2}
$$

这里的有限维系数 $2^{(m+1)/2}$ 必须保留，不能从 $L^2$ 尾小直接声称 $L^\infty$ 尾小。

具体权满足

$$
\eta_j\le e^{-770\,16^j},\qquad
\varepsilon_m\le2e^{-770\,16^m}.
\tag{4.3}
$$

第二式由相邻上界的比至多 $e^{-11550\,16^m}<1/2$ 的几何级数控制得到。因此

$$
\|D_m\|_\infty
\le H_0\,2^{(m+3)/2}e^{-385\,16^m}
\le H_0e^{-380\,16^m}\quad(m\ge2).
\tag{4.4}
$$

最后一步只用 $\frac{m+3}{2}\log2\le5\,16^m$。于是增量级数一致收敛，给出连续函数

$$
G=P_dg+\sum_{m=d}^{\infty}D_m,
$$

有限多个初始项不影响结论。由于 $P_mg\to g$ 于 $L^2$，这个连续函数 $G$ 与原 $L^2$ 向量 $g$ 几乎处处相同。并且由 (4.4)

$$
\|G-P_mg\|_\infty
\le2H_0e^{-380\,16^m}\quad(m\text{ 充分大}).
\tag{4.5}
$$

为与 R26 的阈值比较，记 $L_m=-\log a_m$。R9 的闭式给 $L_m\le100\,16^m$ 对 $m\ge2$ 成立：舍去负项后，$L_m/16^m\le280/3+300/8^m<100$。故 $a_m\ge e^{-100\,16^m}$，(4.5) 特别给

$$
\|G-P_mg\|_\infty=O(a_m).
\tag{4.6}
$$

最后才转到 R26 所使用的截断 $T_m(y)=y\bmod2^m$（把高位设为零）。它不同于条件期望 $P_m$。因为 $P_mg$ 在每个低位柱上恒定，

$$
P_mg(T_m(y))=P_mg(y).
$$

现在 $G$ 已有连续代表，可以逐点计算并得到

$$
\boxed{
\|G-G\circ T_m\|_\infty
\le2\|G-P_mg\|_\infty=O(a_m).
}
\tag{4.7}
$$

这完成从影响估计到真正连续截断估计的全部步骤。

## 5. 用循环性完成唯一性

$h$ 是固定有限柱函数，所以 $h\pm G$ 都连续且满足 R26 §3 的尾条件 $O(a_m)$。如果 $g\ne h$ 且 $g\ne-h$，则二者都是非零向量，特别地 $h+G$ 对 $A$ 循环。

但复对称性给交叉项相等，从全部平方矩匹配得到

$$
B(A^n(h+G),h-G)=Q_n(h)-Q_n(g)=0\qquad(n\ge0).
$$

这使非零向量 $C(h-G)$ 与循环向量 $h+G$ 的整个轨道正交，矛盾。因此 $g=\pm h$，定理得证。

## 6. 与单位近似反例的对照

R29 构造 $C$-实单位向量 $g_l\perp1$，满足

$$
\sup_{n\ge0}\frac{|Q_n(g_l)-Q_n(1)|}{\|A^n\|}\to0,
\qquad g_l\rightharpoonup0.
$$

这与本条不矛盾：有非零误差时，(3.4) 只能变成 $I_k(g_l)\le2\eta_k+\delta_l$。对全部高位求和时，误差 $\delta_l$ 不可无限累加，因而不能得到 (4.1) 的超快尾。R29 的向量把影响均摊在越来越长的高位块上，正好实现这个缺口。本条只处理**精确匹配**，并未给有界误差的统一稳定性结论。
