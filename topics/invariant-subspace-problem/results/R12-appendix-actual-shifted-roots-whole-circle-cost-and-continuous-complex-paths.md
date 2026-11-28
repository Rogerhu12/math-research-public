# R12 补充：原移位根的整圆周同源费用与所有连续复路径

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

## 1. 新范围与原输入

[原同源射线定理](R12-appendix-actual-shifted-roots-fixed-source-superpolynomial-ray-cost.md)只给每条固定射线的超多项式 $\limsup$。本条增加同一个固定来源上的**整圆周**下界，因此覆盖任意趋于零的连续复移位路径。它仍不排除稀疏离散移位、随动来源或其他闭根。

令 $A^{(m)}$ 是原 Haar 尾。允许 $C$ 是它的任意非零实际闭不变旗子商，或固定有限放大的这种子商。原强单位与原权预算已给
$$
C\text{ 单射且值域稠密},\qquad
\|C^n\|\le e^{-c_m n^4}\quad(n\ge1),\qquad
c_m=\frac54\,16^m.
\tag{1.1}
$$
这里使用的是原 Haar 子商，不是负整数边界模型。原来源与逐旗下降见上引定理 §1、[R140](R140-invariant-subquotient-type-and-fixed-first-regularization.md)。

固定整数 $q\ge2$，沿用同一个实际整函数
$$
F_q(z)=\sum_{n=0}^{\infty}\binom{1/q}{n}z^n C^n,\qquad
F_q(z)^q=I+zC.
\tag{1.2}
$$
对每个 $\epsilon\ne0$，任取一个标量 $\xi_\epsilon$ 满足 $\xi_\epsilon^q=\epsilon$，记
$$
R_{\epsilon,q}=\xi_\epsilon F_q(\epsilon^{-1}).
\tag{1.3}
$$
所有这些标量分支只差模为一的常数，因此下面的范数结论与分支选择无关。

由已付 (1.1)，存在 $K_m<\infty$ 使
$$
\|F_q(z)\|\le K_m
\exp\!\bigl(K_m(\log^+|z|)^{4/3}\bigr).
\tag{1.4}
$$
这是整个复平面的真实算子范数界。

## 2. 使用的最小模定理及其精确推论

本文只调用如下经典 Wiman 结论：若 $g$ 是阶小于 $1/2$ 的超越整函数，则存在任意大的圆，其最小模任意大。

一手来源是 J. W. Osborne、P. J. Rippon、G. M. Stallard，
[The iterated minimum modulus and conjectures of Baker and Eremenko](https://oro.open.ac.uk/48913/1/it-minmod-sub.pdf)，
Journal d'Analyse Mathématique 139 (2019), 521–558，
[DOI](https://doi.org/10.1007/s11854-019-0065-z)，Theorem 1.1(a) 及 (1.1)。
该定理更强地给最小模函数的一个轨道趋于无穷；本文只用上面的整圆周后果，不使用其动力系统结论。

**标量引理。** 若 $f$ 是零阶超越整函数，则存在递增 $R_N\to\infty$，使
$$
\min_{|z|=R_N}|f(z)|\ge R_N^N
\qquad(N=1,2,\ldots).
\tag{2.1}
$$

**证明。** 对每个 $N$，令 $T_{N-1}f$ 是 $f$ 在原点的前 $N$ 项，并置
$$
g_N(z)=\frac{f(z)-T_{N-1}f(z)}{z^N}.
$$
原点为可去奇点。$g_N$ 仍是超越整函数，且阶为零。由上述定理，可以选任意大的 $R_N$ 使
$$
\min_{|z|=R_N}|g_N(z)|\ge2.
$$
同时要求 $R_N>R_{N-1}+1$、$R_N\ge2^N$，并要求
$$
\max_{|z|=R_N}|T_{N-1}f(z)|\le R_N^N;
$$
后一式对所有充分大的半径成立，因为该多项式次数至多 $N-1$。于是三角不等式给 (2.1)。证毕。

这里只构造一列完整圆周，没有声称所有充分大的半径都有相同下界。

## 3. 每个固定非零实际来源的整圆周下界

**定理 1。** 对 (1.1) 中的任意 $C$、任意 $x\ne0$ 和 $q\ge2$，存在同一列 $r_N\downarrow0$，使对每个实数 $M\ge0$，
$$
\boxed{
r_N^M\inf_{|\epsilon|=r_N}\|R_{\epsilon,q}x\|
\longrightarrow\infty.
}
\tag{3.1}
$$

**证明。** $C$ 单射且 $\binom{1/q}{n}\ne0$，故 (1.2) 作用于 $x$ 后，每个幂级数系数均非零。

在 Hilbert 空间中，集合
$$
\{v:\langle C^nx,v\rangle=0\}
$$
对每个 $n$ 都是真闭超平面。Baire 定理给同一个 $v\ne0$，使这些配对对所有 $n$ 均非零。采用内积对第一变量线性的约定，标量函数
$$
f(z)=\langle F_q(z)x,v\rangle
$$
是超越整函数；由 (1.4)，它的阶为零。

将 §2 应用于这个固定 $f$。令 $r_N=R_N^{-1}$，则
$$
\begin{aligned}
\inf_{|\epsilon|=r_N}\|R_{\epsilon,q}x\|
&=R_N^{-1/q}\inf_{|z|=R_N}\|F_q(z)x\|\\
&\ge\frac{R_N^{N-1/q}}{\|v\|}.
\end{aligned}
\tag{3.2}
$$
因此 (3.1) 对同一列 $r_N$ 和所有固定 $M$ 成立。证毕。

这里的圆周和标量测试向量只依赖这个固定来源 $x$、$C$ 与 $q$，不随圆周角度变化。

## 4. 连续复路径与任意固定有界正则器

设
$$
\epsilon:(0,t_0]\longrightarrow\mathbb C\setminus\{0\}
$$
连续，且 $\epsilon(t)\to0$ 当 $t\downarrow0$。不限制它的绕行次数、方向或速度。

对 §3 中的每个充分小的 $r_N$，连续函数 $|\epsilon(t)|$ 都必须经过 $r_N$。这些经过时刻可取 $t_N\downarrow0$：任意固定紧区间 $[\delta,t_0]$ 上，$|\epsilon|$ 的最小值严格为正。因此 (3.1) 给
$$
\boxed{
\limsup_{t\downarrow0}
|\epsilon(t)|^M\|R_{\epsilon(t),q}x\|=\infty
\qquad(x\ne0,\ M\ge0).
}
\tag{4.1}
$$
$R_{\epsilon(t),q}$ 可以在各时刻任意选择标量根分支，甚至不连续；分支不改变上述范数。

令 $P\ne0$ 为任意固定有界算子，不要求 $PC=CP$。选定 $u$ 使 $Pu\ne0$，直接应用定理 1，得到一列完整圆周以及
$$
\limsup_{t\downarrow0}
|\epsilon(t)|^M\|R_{\epsilon(t),q}P\|=\infty.
\tag{4.2}
$$
这也说明同一个固定输入 $u$ 的输出已经违反任何多项式预算。

左正则器同样如此，而且也可保固定输入。因为 $C^n$ 的值域稠密，$PC^n\ne0$ 对所有 $n$ 成立。先由 Baire 选同一个 $u$ 使 $PC^nu\ne0$ 对所有 $n$ 成立，再选同一个 $v$ 使
$$
\langle PC^nu,v\rangle\ne0
\qquad(n\ge0).
$$
于是 $\langle PF_q(z)u,v\rangle$ 是零阶超越整函数。§2 的同一证明给
$$
r_N^M\inf_{|\epsilon|=r_N}\|P R_{\epsilon,q}u\|\longrightarrow\infty
$$
和
$$
\boxed{
\limsup_{t\downarrow0}
|\epsilon(t)|^M\|P R_{\epsilon(t),q}\|=\infty.
}
\tag{4.3}
$$
左右两列圆周可以不同，不声称存在一个对所有 $P,x$ 同时有效的公共序列。

所以任何非零固定左右有界正则器，都不能使这族根沿任意完整连续复路径强收敛。强收敛会使每个固定输入的输出有界，已与上述固定输入结论矛盾。

## 5. 单个全原尾：所有有界移位根都在本定理范围内

本节仅取**单个全原 Haar 尾** $C=A^{(m)}$。不将以下根分类自动传给未知子商或有限放大。

已付[全原尾强不可约性](R12-appendix-all-original-tails-strongly-irreducible-and-ordinary-invariant-complements.md)给 $C'$ 中只有幂等元 $0,I$。于是对每个 $\epsilon\ne0$，若有界算子 $Y$ 满足
$$
Y^q=C+\epsilon I,
$$
必有
$$
\boxed{Y=\xi F_q(\epsilon^{-1}),\qquad \xi^q=\epsilon.}
\tag{5.1}
$$

**证明。** $Y$ 与 $Y^q$ 交换，所以 $YC=CY$。谱映射给
$$
\sigma(Y)\subset\{\xi:\xi^q=\epsilon\}.
$$
若 $\sigma(Y)$ 含至少两个点，将其分成两个非空闭开谱集，$Y$ 的 Riesz 投影就是 $C'$ 中非平凡幂等元，矛盾。因此 $\sigma(Y)=\{\xi\}$，且 $\xi^q=\epsilon$。

在 $\xi$ 的充分小邻域，映射 $z\mapsto z^q$ 有解析局部逆 $g$，满足 $g(\epsilon)=\xi$。全纯演算的复合性给
$$
Y=g(Y^q)=g(C+\epsilon I).
$$
右侧的原点芽正是 (1.3)，故得 (5.1)。证毕。

因此在单个全原尾上，任意随 $\epsilon$ 变化的有界 $q$ 次根选择，都不能通过更换非解析有界分支逃离 §3–4 的整圆周费用。

## 6. 未付范围与下一原来源

本条排除的是固定非零来源、固定有界左或右正则器，以及趋于零的完整连续移位路径。它没有以下任何结论：

- 没有排除特意选择的稀疏离散 $\epsilon_n\to0$；这些点可以避开本文构造的圆周。
- 没有控制随动 $x_n\to x$ 的图极限，因为 §3 的标量分量和下界保的是同一个 $x$。
- 没有证明一般有界二次分子 $Y^2=CQ^2$ 不存在；这种 $Y$ 无须是移位根乘固定 $Q$ 的极限。
- 没有排除一般稠密稳定域上的闭根，也没有完成原 Haar 普通不变子空间目标。

尤其不能把 §5 的“每个非零移位都有且只有这些有界根”代入 $\epsilon=0$，或以此倒置未付的图极限。真正场外、混合或随动来源仍须继续构造。
