# 全部原尾强不可约与普通不变空间的无界互补

作者：AI-assisted GPT-6 Astra Pro；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：完整证明的原算子结构结论。** 每个原 Haar 尾算子 $B_m$ 的完整交换子只含 $0,I$ 两个有界幂等元。因此每个原尾强不可约；任意非零真闭 $A$-不变子空间均无闭 $A$-不变补空间。这个结论不假定未知不变空间是有限头图，不使用 Deddens 保持，也不声称不存在非平凡普通不变空间。

本文与[有界根重数和不变投影距离](../results/R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)的用途不同：该文排除一个真有限头坐标到完整尾的同构；本稿直接排除整个原空间的任何有界不变直和分解。R178 §7 已分析某些特殊核对产生的闭无界幂等；这里新增的是对所有普通不变互补对的统一排除依据。

## 1. 已支付的原尾结构

在 $K=L^2(\mathbb Z_2,\mu)$ 上，
$$
(B_mf)(z)=\alpha_{m+v_2(z)}f(z-1),\qquad B_0=A,
$$
其中零点值按原定义取零，$\alpha_j>0$ 是原权序列。令
$$
\mathscr C_m=\{B_m\}'\subset B(K).
$$
[有界根重数正文 §2](../results/R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)已逐尾证明：

1. $B_m$ 拟幂零；
2. $\mathscr C_m$ 是交换的含单位 Banach 代数；
3. 首个物理位的准确分解为
   $$
   B_m=\begin{pmatrix}0&B_{m+1}\\\alpha_mI&0\end{pmatrix},
   \qquad B_m^2=\alpha_m I_2\otimes B_{m+1}.
   \tag{1.1}
   $$

以下只用这些准确身份；不使用渐近有限头截断代替原算子。

## 2. 一步幂等刚性

**引理 2.1。** 若 $E\in\mathscr C_m$ 且 $E^2=E$，则存在 $D\in\mathscr C_{m+1}$，$D^2=D$，使
$$
E=I_2\otimes D.
\tag{2.1}
$$

**证明。** 因为 $E$ 与 $B_m^2$ 交换，首位分块的四个条目均属于 $\mathscr C_{m+1}$。再将 $EB_m=B_mE$ 逐块相等，准确得到
$$
E=\begin{pmatrix}
D&\alpha_m^{-1}B_{m+1}R\\R&D
\end{pmatrix},\qquad D,R\in\mathscr C_{m+1}.
\tag{2.2}
$$
由于这个**完整**尾交换子已证明交换，$D,R,B_{m+1}$ 两两交换。幂等关系的对角与左下条目给
$$
D^2+\alpha_m^{-1}B_{m+1}R^2=D,
\qquad (2D-I)R=0.
\tag{2.3}
$$
第二式使 $DR=R/2$、$D^2R=R/4$。把第一式乘以 $R$，得到
$$
\frac14R+\alpha_m^{-1}B_{m+1}R^3=\frac12R,
$$
从而
$$
\bigl(I-4\alpha_m^{-1}B_{m+1}R^2\bigr)R=0.
\tag{2.4}
$$
括号内的算子可逆。确切地，因为 $B_{m+1}R=RB_{m+1}$，
$$
\limsup_{n\to\infty}
\bigl\|(4\alpha_m^{-1}B_{m+1}R^2)^n\bigr\|^{1/n}
\le4\alpha_m^{-1}\|R\|^2
\lim_{n\to\infty}\|B_{m+1}^n\|^{1/n}=0.
$$
故 $4\alpha_m^{-1}B_{m+1}R^2$ 拟幂零，其与 $I$ 的差有有界逆。由 (2.4)，$R=0$。式 (2.2) 及 (2.3) 随即给 (2.1) 和 $D^2=D$。证毕。

## 3. 全部原尾强不可约

**定理 3.1。** 对每个 $m\ge0$，
$$
\boxed{E\in\{B_m\}',\ E^2=E\quad\Longrightarrow\quad E=0\ \text{或}\ E=I.}
\tag{3.1}
$$
幂等不要求自伴。

**证明。** 反复应用引理 2.1，对每个 $\ell\ge1$ 得
$$
E=I_{2^\ell}\otimes D_\ell,
\qquad D_\ell\in\mathscr C_{m+\ell},\quad D_\ell^2=D_\ell.
\tag{3.2}
$$
因此 $E$ 与每个有限物理头的整个矩阵代数交换。

为明确这一步在原纯 Haar 表示中的结论，设 $\Omega=1$，将有限头中投影到其头真空的秩一投影提升为尾恒等，记为 $p_\ell$。由 $Ep_\ell=p_\ell E$ 及 $p_\ell\Omega=\Omega$，有
$$
E\Omega\in\bigcap_{\ell\ge1}\operatorname{Ran}p_\ell=\mathbb C\Omega.
$$
最后的交等式是原无限张量真空表示的直接事实：对每个有限柱 $g$，若 $f\in\operatorname{Ran}p_\ell$ 且 $\ell$ 超过 $g$ 的支持，则
$\langle f,g\rangle=\langle f,\Omega\rangle\langle\Omega,g\rangle$；柱函数稠密使 $f$ 为常向量。

写 $E\Omega=c\Omega$。每个有限柱都是某个有限头矩阵 $F$ 作用于 $\Omega$，因而
$$
EF\Omega=FE\Omega=cF\Omega.
$$
由稠密性 $E=cI$；再由 $E^2=E$ 得 $c\in\{0,1\}$。证毕。

因此每个 $B_m$ 在通常意义下均为**强不可约**：不存在非平凡有界交换幂等；等价地，它的任何有界相似变换均无非平凡约化直和。

## 4. 对全部普通不变空间及核像的直接后果

### 4.1 任意闭不变补空间均不可能

若 $M,N$ 是闭 $A$-不变子空间且
$$
H=M\dotplus N,
\tag{4.1}
$$
沿 $N$ 投影到 $M$ 的算子 $E$ 由闭图定理有界。两空间的 $A$-不变性给 $EA=AE$，且 $E^2=E$。定理 3.1 迫 $M=0$ 或 $N=0$。

所以每个非零真闭普通 $A$-不变空间都没有闭 $A$-不变补空间。这里没有预设这个空间由慢乘子核、图、有限头坐标或者 Deddens 轨道产生。

更一般，若非零闭不变空间 $M,N$ 满足
$$
M\cap N=0,\qquad\overline{M+N}=H,
\tag{4.2}
$$
则 $M+N$ 必不闭，因而
$$
\inf\{\|x+y\|:x\in M,y\in N,\ \|x\|^2+\|y\|^2=1\}=0.
\tag{4.3}
$$
否则加法映射从 Hilbert 空间 $M\oplus N$ 到 $H$ 有下界，其像闭，与 (4.2) 及 (4.1) 的排除矛盾。相应沿 $N$ 投影到 $M$ 是稠密定义的闭无界幂等。这把 R178 §7 的无界互补机制推广到任意满足 (4.2) 的普通不变对，而不从中断言这样的对已经存在。

### 4.2 完整交换子每个元素的谱均连通

若 $X\in\mathscr C_m$ 的谱分裂成两个不交非空紧集，围绕其中一块的 Riesz 积分给非平凡有界幂等 $E$。因为 $X$ 的每个预解式均与 $B_m$ 交换，$E\in\mathscr C_m$，与 (3.1) 矛盾。因此
$$
\boxed{X\in\mathscr C_m\quad\Longrightarrow\quad\sigma(X)\text{ 连通}.}
\tag{4.4}
$$
这不声称谱必须是单点。尤其不能据此把完整交换子等同于原范数闭多项式代数，或排除非零拟幂零交换子。

### 4.3 互补核像必须有真正的退化

若 $X\in\mathscr C_m$ 有非零核和非零闭像，且另外满足
$$
\ker X\cap\operatorname{Ran}X=0,\qquad
\overline{\ker X+\operatorname{Ran}X}=K,
$$
则两空间的和不能闭。这是 (4.2) 的直接应用，因为两者都被 $B_m$ 保持。若另加上和为全空间的代数等式，则这样的 $X$ 不存在。

这保留了未知核和未知像的真实拓扑，未把“闭像”或“有限余维”自动替换成有界直和，也没有消去可能的非零核与像交。

## 5. 仍未支付的接口

强不可约性排除有界不变互补，不排除没有不变补空间的普通不变子空间。对有限头闭图所得的实际真底空间，之前的小稿还用根重数排除了有限放大的尾模补空间；本稿不能省去那个有限重数分析，因为 $M_k(\mathscr C_m)$ 在 $k>1$ 时不交换。

若要构造真正的非零真 $A$-不变空间，仍须给出实际闭核、实际非稠密闭像，或一个保留真实域的闭图。不能把 (4.3) 的必需退化当成其中任何一个对象已经存在。
