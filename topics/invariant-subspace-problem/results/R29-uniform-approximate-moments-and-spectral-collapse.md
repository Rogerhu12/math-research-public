# R29：全部归一化矩的一致逼近与非退化双弱极限反例

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94，子任务 `centered_literature`。

**状态：已证明的中间结论。** 本条在 R9 的具体算子上构造单位柱函数：它们与常函数 $1$ 正交且弱趋零，但其全部归一化复双线性平方矩在 $\ell^\infty$ 中一致逼近 $1$ 的矩。进而构造两个非零弱极限、所有归一化交叉矩一致趋零的单位向量对，并得到有界秩一幂零扰动的统一谱收缩。这排除从此种矩误差及双弱极限直接获得真正矩消失对的升级；没有产生普通不变子空间，不主张文献新颖性。

## 1. 设定与主结论

沿用 R9 的 $A$，并取

$$
(Cf)(y)=\overline{f(-1-y)},\qquad
B(f,g)=\langle f,Cg\rangle,
\qquad Q_n(f)=B(A^nf,f).
\tag{1.1}
$$

内积第一变量线性。R24 已自含证明 $A=CA^*C$，因此 $B(A^n\cdot,\cdot)$ 对称。记

$$
W_n=\|A^n\|=\prod_{j=1}^n a_{v_2(j)},\quad W_0=1,
\qquad F_n=A^n/W_n.
\tag{1.2}
$$

以下 $n=0$ 时 $F_0=I$。令 $b_j(y)$ 是第 $j$ 个二进位，位编号从零开始，记实 Rademacher 函数

$$
\chi_j(y)=(-1)^{b_j(y)}.
\tag{1.3}
$$

对 $k,m\ge1$ 定义

$$
g_{k,m}=\frac{i}{\sqrt m}\sum_{j=k}^{k+m-1}\chi_j.
\tag{1.4}
$$

再令

$$
C_k=\prod_{j=1}^{2^k-1}a_{v_2(j)},\quad
\tau_k=\frac{2^ka_k}{C_k},\quad
\varepsilon_k=\sum_{j=k}^{\infty}\frac{a_{j+1}}{a_j}.
\tag{1.5}
$$

下面证明 $\tau_k\to0$；$\varepsilon_k\to0$ 已由 R13 的精确权比公式证明。

**定理 1.1。** 有 $\|g_{k,m}\|=1$、$g_{k,m}\perp1$、$Cg_{k,m}=g_{k,m}$，且

$$
\boxed{
\sup_{n\ge0}
\frac{|Q_n(g_{k,m})-Q_n(1)|}{\|A^n\|}
\le\frac{3}{2m}+2(\tau_k+\varepsilon_k).
}
\tag{1.6}
$$

尤其取 $g_l=g_{l,l}$，则

$$
g_l\rightharpoonup0,\quad \|g_l\|=1,\quad
\min\{\|g_l-1\|,\|g_l+1\|\}=\sqrt2,
\tag{1.7}
$$

同时全部归一化平方矩一致逼近常函数 $1$ 的矩。

## 2. 共轭关系：为何复双线性平方矩可在本构造上改写为内积

Haar 测度下 $\chi_j$ 构成正交单位系，每个均值为零，故 (1.4) 范数为一并与 $1$ 正交。变换 $y\mapsto-1-y$ 翻转每个二进位，因此

$$
\chi_j(-1-y)=-\chi_j(y).
$$

由于 $C$ 还取复共轭，

$$
C(i\chi_j)(y)=\overline{i\chi_j(-1-y)}=i\chi_j(y).
$$

所以 $Cg_{k,m}=g_{k,m}$，且 $C1=1$。这一步中的因子 $i$ 是必需的；若只取实的 Rademacher 和，则 $Cg=-g$，平方矩会变号。由本构造的 $C$-实性，

$$
B(F_ng_{k,m},g_{k,m})=\langle F_ng_{k,m},g_{k,m}\rangle,
\quad B(F_n1,1)=\langle F_n1,1\rangle.
\tag{2.1}
$$

## 3. 对全部指数统一有效的低位截断和高位矩阵单位

令 $A_k$ 为把所有 $v_2(y)\ge k$ 的权删去所得的幂零截断。R9 的直接公式给

$$
\|A-A_k\|=a_k,
\tag{3.1}
$$

且 $A_k$ 只作用于低于第 $k$ 位的有限链，其余高位上为恒等算子。$\|A_k\|,\|A\|\le a_0<1$。

对 $0\le r<2^k$，定义

$$
G_{r,k}=A_k^r/W_r.
\tag{3.2}
$$

由于截断后的逐点段乘积不超过原段乘积，$\|G_{r,k}\|\le1$。幂差伸缩展开给

$$
\|A^r-A_k^r\|\le r a_k a_0^{r-1}\le r a_k
\quad(r\ge1).
$$

又 $W_r\ge W_{2^k-1}=C_k$，因为所有权都小于一。于是

$$
\|F_r-G_{r,k}\|\le\tau_k
\qquad(0\le r<2^k).
\tag{3.3}
$$

$r=0$ 时两者均为 $I$，也满足该界。

令 $E_j$ 为第 $j$ 位上的矩阵单位 $e_{10}$，其余位取恒等。对有限位集 $S$ 记 $E_S=\prod_{j\in S}E_j$。R13 的精确无进位乘法及 R12 的 $\|F_{2^j}-E_j\|=a_{j+1}/a_j$ 给

$$
\left\|F_s-E_{S(s)}\right\|\le\varepsilon_k
\quad\text{若 }2^k\mid s,
\tag{3.4}
$$

其中 $S(s)$ 是 $s$ 的二进位支集；误差界与支集大小无关。

现在对**任意** $n\ge0$ 写

$$
n=r+s,\qquad0\le r<2^k,\quad2^k\mid s.
$$

这没有进位，故 $F_n=F_rF_s$。结合 (3.3)—(3.4)，得到

$$
\boxed{
\|F_n-G_{r,k}E_{S(s)}\|\le\tau_k+\varepsilon_k
\qquad\text{对全部 }n\ge0.
}
\tag{3.5}
$$

$G_{r,k}$ 只作用低 $k$ 位，$E_{S(s)}$ 只作用第 $k$ 位及以上，因而在 (3.5) 的近似算子中可以精确分离张量因子。这里没有把原来的 $F_r$ 擅自当成低位算子。

最后核实 $\tau_k\to0$。记 $L_k=-\log a_k$。从 R9 的权闭式，对 (1.5) 的有限几何和求和得到

$$
-\log C_k
=\frac{20}{3}16^k-15\,8^k+(150k-275)2^k+\frac{850}{3}.
\tag{3.6}
$$

因此

$$
-\log a_k+\log C_k
=L_k-(-\log C_k)
=\frac{260}{3}16^k-75\,8^k+(575-150k)2^k-\frac{1700}{3}.
\tag{3.7}
$$

该量减去 $k\log2$ 仍趋于正无穷，故 $\tau_k=2^ka_k/C_k\to0$。

## 4. 高位和向量上的精确矩阵单位矩

置位块 $J=\{k,\dots,k+m-1\}$。对任意有限 $S\subseteq\{k,k+1,\dots\}$，记

$$
q=|S\cap J|,\qquad p=|S\setminus J|.
$$

**引理 4.1。** 有

$$
\boxed{
\langle E_Sg_{k,m},g_{k,m}\rangle
=2^{-|S|}\left(1-\frac{q(q+1)}m\right).
}
\tag{4.1}
$$

**证明。** 单位因子 $i$ 在内积的两端抵消。采用每位的正交基 $|+\rangle=1$、$|-\rangle=\chi$；在这个基中

$$
e_{10}=\frac12\begin{pmatrix}1&1\\-1&-1\end{pmatrix}.
\tag{4.2}
$$

$m^{-1/2}\sum_{j\in J}\chi_j$ 是恰有一位处于 $|-\rangle$ 的 $m$ 个正交张量向量之和。对角项中，若该位不在 $S$，矩阵系数为 $2^{-|S|}$；若该位在 $S$，系数为 $-2^{-|S|}$。因此全部对角项贡献

$$
\frac{m-2q}{m}\,2^{-|S|}.
$$

非对角项只有在两个不同的激发位都属于 $S\cap J$ 时非零；由 (4.2)，每个这样的有序对贡献 $-2^{-|S|}/m$。共有 $q(q-1)$ 个，故总和为

$$
2^{-|S|}\left(1-\frac{2q+q(q-1)}m\right),
$$

即 (4.1)。证毕。

常函数 $1$ 的对应系数为 $\langle E_S1,1\rangle=2^{-|S|}$，所以

$$
\left|\langle E_Sg_{k,m},g_{k,m}\rangle
-\langle E_S1,1\rangle\right|
=\frac{q(q+1)}{m2^{p+q}}\le\frac{3}{2m}.
\tag{4.3}
$$

最后一个界对所有 $q$ 都成立：$q=0$ 时为零，$q=1$ 时 $q(q+1)2^{-q}=1$，$q=2,3$ 时为 $3/2$，以后相邻项比为 $(q+2)/(2q)\le1$。

## 5. 统一矩误差与弱零结论

对任意 $n$ 使用 §3 的 $n=r+s$。$g_{k,m}$ 在低 $k$ 位上的因子为 $1$，故张量分离给

$$
\langle G_{r,k}E_{S(s)}g_{k,m},g_{k,m}\rangle
=\langle G_{r,k}1,1\rangle\,
\langle E_{S(s)}g_{k,m},g_{k,m}\rangle.
$$

常函数 $1$ 有相同的低位因子，且 $|\langle G_{r,k}1,1\rangle|\le1$。于是 (4.3) 给近似算子的两矩之差至多 $3/(2m)$。再把两个单位向量分别代入算子范数误差 (3.5)，总误差增加至多 $2(\tau_k+\varepsilon_k)$。最后使用 (2.1) 与 $F_n=A^n/W_n$，得到 (1.6)。所有估计均不依赖 $n$，所以确实控制整个 $n\ge0$ 上确界。

取 $g_l=g_{l,l}$。对任意固定 $h\in H$，Bessel 不等式给

$$
|\langle g_l,h\rangle|
\le\left(\sum_{j=l}^{2l-1}|\langle\chi_j,h\rangle|^2\right)^{1/2}
\longrightarrow0.
$$

正交性和单位范数给 (1.7)，完成定理 1.1 的证明。

这也表明：在单位球上，不能仅由 $\sup_n|Q_n(g)-Q_n(1)|/\|A^n\|$ 小，就推导 $g$ 接近 $\pm1$ 或获得所需强紧性。它与 R27 的**精确**有限柱匹配范数逃逸不矛盾；本条的误差不为零。

## 6. 两个非零弱极限，而全部归一化交叉矩一致趋零

定义

$$
f_l=\frac{1+g_l}{\sqrt2},\qquad
v_l=\frac{1-g_l}{\sqrt2}.
\tag{6.1}
$$

两者均为 $C$-实单位向量，且 $\langle f_l,v_l\rangle=0$。由于 $B(F_n\cdot,\cdot)$ 对称，交叉项精确抵消：

$$
\langle F_nf_l,v_l\rangle
=B(F_nf_l,v_l)
=\frac12\bigl[B(F_n1,1)-B(F_ng_l,g_l)\bigr].
\tag{6.2}
$$

因此

$$
\boxed{
\sup_{n\ge0}\frac{|\langle A^nf_l,v_l\rangle|}{\|A^n\|}
\le d_l:=\frac{3}{4l}+\tau_l+\varepsilon_l\longrightarrow0.
}
\tag{6.3}
$$

同时

$$
f_l\rightharpoonup\frac1{\sqrt2}1,
\qquad v_l\rightharpoonup\frac1{\sqrt2}1,
\tag{6.4}
$$

两个弱极限的零阶配对等于 $1/2$，而每一步的零阶配对都恰为零。并且

$$
\left\|f_l-\frac1{\sqrt2}1\right\|
=\left\|v_l-\frac1{\sqrt2}1\right\|=\frac1{\sqrt2}.
\tag{6.5}
$$

故即使把“对每个固定 $n$ 的矩趋零”强化为**全部归一化矩一致趋零**，仍不能只凭两个非零弱极限传递真正的矩消失。

## 7. 有界秩一幂零扰动的统一谱收缩

本节是上述构造的直接推论，不使用任何未验证的谱收缩定理。按 $K_lx=\langle x,v_l\rangle f_l$ 定义秩一算子，则

$$
\|K_l\|=1,\qquad K_l^2=0,\qquad
K_l\xrightarrow{\rm WOT}K:=\tfrac12(1\otimes1).
\tag{7.1}
$$

**命题 7.1。** 对任意固定 $M<\infty$，

$$
\sup_{|\alpha|\le M}r(A+\alpha K_l)\longrightarrow0.
\tag{7.2}
$$

但每个实数 $\alpha>0$ 都满足

$$
r(A+\alpha K)>\alpha/2.
\tag{7.3}
$$

**证明 (7.2)。** 因 $A$ 拟幂零，对每个 $\epsilon>0$，

$$
S_\epsilon=\sum_{n=0}^{\infty}\frac{\|A^n\|}{\epsilon^{n+1}}<\infty.
$$

对 $|\lambda|\ge\epsilon$，范数收敛的预解式级数和 (6.3) 给

$$
|\langle(\lambda I-A)^{-1}f_l,v_l\rangle|
\le d_lS_\epsilon.
\tag{7.4}
$$

有界秩一因子分解说明：$\lambda\ne0$ 属于 $\sigma(A+\alpha K_l)$ 当且仅当

$$
1=\alpha\langle(\lambda I-A)^{-1}f_l,v_l\rangle.
\tag{7.5}
$$

这里可直接核验：$\lambda I-A-\alpha f_l\otimes v_l$ 等于 $\lambda I-A$ 乘以 $I-\alpha(\lambda I-A)^{-1}f_l\otimes v_l$，后一秩一扰动可逆恰当且仅当右端标量不等于 $1$。当 $Md_lS_\epsilon<1$ 时，(7.5) 对全部 $|\alpha|\le M$、$|\lambda|\ge\epsilon$ 都不可能成立。于是所有这些谱都在 $\epsilon$ 圆盘内。$\epsilon$ 任意，证明 (7.2)。

**证明 (7.3)。** $A$ 是正权算子，故 $c_n=\langle A^n1,1\rangle>0$ 对所有 $n\ge0$ 成立，且 $c_0=1$。对实 $\lambda>0$，

$$
q(\lambda)=\langle(\lambda I-A)^{-1}1,1\rangle
=\sum_{n=0}^{\infty}c_n\lambda^{-n-1}
$$

连续且严格递减，在 $\lambda\to\infty$ 时趋零，在 $\lambda\downarrow0$ 时趋无穷。并且 $q(\alpha/2)>2/\alpha$，因为零阶项恰为 $2/\alpha$，后面的正项非零。故存在唯一 $\lambda_\alpha>\alpha/2$ 使 $(\alpha/2)q(\lambda_\alpha)=1$。同一秩一因子式表明 $\lambda_\alpha\in\sigma(A+\alpha K)$（实际是特征值），证明 (7.3)。证毕。

该构造具有统一有界的秩一范数、每步幂零、全部归一化矩一致小、所有有界扰动参数上的谱半径一致趋零，以及非零 WOT 秩一极限；极限扰动却不拟幂零。因而把这些条件拼在一起仍不足以替代 R15 所需的强弱配对或无范数损失条件。
