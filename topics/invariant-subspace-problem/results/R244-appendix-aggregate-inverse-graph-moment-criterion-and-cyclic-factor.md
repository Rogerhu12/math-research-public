# R244 附录：正常矩的聚合逆图范数判据与循环第一因子

日期：2026-11-13（UTC）。作者：normal_states；Astra-ISP-1cf 复核。

状态：以下等价判据、实际最小闭图识别及有限维检验均已证明，属于中间结论。它将 R244 的逐个输入配对域条件替换为一个聚合矩连续性条件，未为任意假想正正常湮灭者构造满足条件的正则器。

## 1. 实际设置及所需强单位

仍记
$$
H=L^2(\mathbb Z_2),\quad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\quad
\mathfrak C=\{A\}',\quad
B(f,g)=\langle f,Cg\rangle.
$$
内积对第一变量线性，$B$ 为连续对称双线性。$\mathfrak C$ 交换，所有元素均为 $C$ 对称。$1$ 对 $A$ 循环。

令 $\mathscr D$ 为全部有限 Walsh 柱的线性空间。对 $u\in\mathscr D$，实际有界乘子 $X_u\in\mathcal A$ 满足 $X_u1=u$。R88 给
$$
\Psi_n(F)=X_{\Pi_nF1}\in\mathcal A,\qquad
\Psi_n(F)\longrightarrow F\quad\mathrm{SOT},\qquad
\sup_n\|\Psi_n(F)\|<\infty
\tag{1.1}
$$
对每个固定 $F\in\mathfrak C$ 成立。

本稿允许任何 $P\in\mathfrak C$，只要求：

1. $1\in\operatorname{Ran}P$；
2. 存在 $U_n\in\mathfrak C$，使
   $$
   K_n=PU_n\longrightarrow I\quad\mathrm{SOT},\qquad
   \sup_n\|K_n\|<\infty.
   \tag{1.2}
   $$

不要求 $U_n$ 自身一致有界，也不要求 $P\in\mathcal A$。

R230 的全部非零规范正一阶无穷预解式乘积均满足这些假设。累计非负系数行属于 $\ell^2$ 时，它给实际收缩 $P$ 和满足 $\|PU_n\|\le1$ 的强单位；同一 R230 的逆测试证明 $1\in\operatorname{Ran}P$。R261 再给其平方根次数零型估计，但本稿的等价关系不需要任何定量指数域成本。

## 2. 逆、循环向量和全部有限柱的图核心

由 (1.2) 及交换性，$P$ 单射：若 $Px=0$，则
$$
K_nx=U_nPx=0,\qquad x=\lim_nK_nx=0.
$$
又 $K_nH\subseteq\operatorname{Ran}P$，故 $P$ 稠密像。定义闭稠密算子
$$
G=P^{-1},\qquad \operatorname{Dom}G=\operatorname{Ran}P,
\qquad g=G1.
\tag{2.1}
$$
闭性直接来自 $P$ 有界：若 $u_j\to u$、$Gu_j\to v$，则 $u_j=PGu_j\to Pv$，所以 $u=Pv$、$Gu=v$。

### 2.1 $g$ 的循环性

置 $M=\overline{\mathcal A g}$。它闭且 $A$ 不变。由 R88 的一致有界强多项式逼近，$M$ 被每个 $\mathfrak C$ 元素保持，特别被 $P$ 保持。因此
$$
1=Pg\in M.
$$
由于 $1$ 对 $A$ 循环，$M=H$。所以
$$
\boxed{g=P^{-1}1\text{ 是实际 }A\text{ 的循环向量。}}
\tag{2.2}
$$
这里使用的是 $P$ 保持闭轨道，不是仅从 $P$ 稠密像推循环性。

### 2.2 精确列关系

对任意 $F\in\mathfrak C$，
$$
F1=FPg=PFg,
$$
故
$$
\boxed{F1\in\operatorname{Dom}G,\qquad G(F1)=Fg.}
\tag{2.3}
$$
特别，全部有限柱都在 $\operatorname{Dom}G$，并且
$$
Gu=X_ug\qquad(u\in\mathscr D).
\tag{2.4}
$$

集合 $\{X_ug:u\in\mathscr D\}$ 在 $H$ 稠密。确切地，$g$ 循环给 $\mathcal A g$ 稠密，而 (1.1) 对每个固定 $F\in\mathcal A$ 给 $\Psi_n(F)g\to Fg$，其左侧属于上述集合。

因此 $\mathscr D$ 是 $G$ 的图核心：给定 $u=Pv\in\operatorname{Dom}G$，取 $u_j\in\mathscr D$ 使 $Gu_j=X_{u_j}g\to v$；则
$$
u_j=PGu_j\longrightarrow Pv=u.
$$
沿用 R244 的最小闭乘子定义，得到准确识别
$$
\boxed{G=X_g.}
\tag{2.5}
$$
这仅对本节产生的循环 $g$ 断言，不把任意最小闭乘子都认作最大图。

顺便，$P$ 的 $C$ 对称性给 $G$ 的最大 $C$ 对称性。事实上
$\operatorname{Dom}G^*=\operatorname{Ran}P^*$、$G^*=(P^*)^{-1}$；
而 $CP^*=PC$，故
$$
CG^*C=G.
\tag{2.6}
$$
(2.6) 不参与下面的正常极限步骤。

### 2.3 同一强单位自动逼近逆

在整个 $\operatorname{Ran}P$ 上，原来的 (1.2) 已给
$$
\boxed{U_nu=U_nPGu=K_nGu\longrightarrow Gu.}
\tag{2.7}
$$
所以不必另外要求某组指数尺度逆截断同时具有全空间产品范数界。这里始终使用同一组 $U_n$；一致有界的是 $PU_n$，不是 $U_n$。

## 3. 聚合判据

令 $\phi$ 是 $B(H)$ 上任意正常泛函，其限制仍记为 $\phi:\mathfrak C\to\mathbb C$。无需先假设正性或有限秩。

**定理。** 在第1节假设下，以下三条等价：

**(A) 正则后的固定真空表示。** 存在 $h\in H$，使
$$
\phi(PF)=B(Fh,1)\qquad(F\in\mathfrak C).
\tag{3.1}
$$

**(B) 有限柱聚合矩的逆图范数界。** 存在 $C_\phi<\infty$，使
$$
\boxed{
|\phi(X_u)|\le C_\phi\|Gu\|
\qquad(u\in\mathscr D).
}
\tag{3.2}
$$

**(C) 未正则泛函的循环第一因子表示。** 存在 $h\in H$，使
$$
\boxed{
\phi(F)=B(Fg,h)\qquad(F\in\mathfrak C).
}
\tag{3.3}
$$

三条中的 $h$ 相同且唯一，并且
$$
\|h\|=\sup_{0\ne u\in\mathscr D}
\frac{|\phi(X_u)|}{\|Gu\|}.
\tag{3.4}
$$

### 证明：(B) 推出 (C)

在稠密线性空间 $G\mathscr D$ 上定义
$$
\ell(Gu)=\phi(X_u).
$$
由于 $G$ 单射，定义无歧义；由于 $u\mapsto X_u$ 线性，它是线性的。(3.2) 使 $\ell$ 有界。由 Hilbert 空间 Riesz 表示及 $B$ 非退化，存在唯一 $h\in H$，满足
$$
\phi(X_u)=B(Gu,h)=B(X_ug,h)\qquad(u\in\mathscr D).
\tag{3.5}
$$
其范数正是 (3.4)。

给定固定 $F\in\mathfrak C$，把 (3.5) 用于 $u_n=\Pi_nF1$。由 (1.1)，$\Psi_n(F)$ 一致有界且强趋于 $F$。正常泛函对此连续，因此
$$
\phi(\Psi_n(F))\longrightarrow\phi(F).
$$
另一方面，$\Psi_n(F)g\to Fg$，故右侧趋于 $B(Fg,h)$。得到 (3.3)。

正常连续性可直接由迹类密度的有限秩逼近证明：有限秩部分对强收敛连续，迹范数尾由统一算子范数界控制。没有把正常泛函当作对任意无界强逼近都连续。

### 证明：(C) 推出 (A) 和 (B)

由 $Pg=1$、交换性及 $C$ 对称，
$$
\phi(PF)=B(PFg,h)=B(F1,h)=B(Fh,1),
$$
即 (A)。令 $F=X_u$，由 (2.4) 立刻得到 (B)，常数为 $\|h\|$。

### 证明：(A) 推出 (C)

对 $U_nF$ 使用 (3.1)：
$$
\phi(PU_nF)=B(U_nFh,1)=B(h,U_nF1).
\tag{3.6}
$$
左侧的 $PU_nF=K_nF$ 强趋于 $F$，且范数一致有界；正常性给左侧趋于 $\phi(F)$。

右侧由 $F1=PFg$ 及交换性，准确等于
$$
B(h,PU_nFg)=B(h,K_nFg)\longrightarrow B(h,Fg).
$$
于是 (C) 成立。此处没有要求 $U_nF$ 一致有界，也没有将两组不同的逆测试截断拼在一起。

最后，若两个 $h$ 满足 (C)，则它们之差对稠密轨道 $\mathfrak Cg$ 的 $B$ 配对全为零，故相等。证毕。

## 4. 有限维 Gram 检验及精确极限

令
$$
\mathscr D_m=\operatorname{span}\{\chi_F:F\subseteq[0,m)\},
\qquad E_m=G\mathscr D_m,
$$
并定义
$$
c_m=\sup_{0\ne u\in\mathscr D_m}
\frac{|\phi(X_u)|}{\|Gu\|}.
\tag{4.1}
$$
每个 $E_m$ 有限维，$E_m\subset E_{m+1}$，其并在 $H$ 稠密。因此每个 $c_m$ 有限，而且 $c_m$ 单调不减。

存在唯一 $h_m\in CE_m$，使
$$
B(Gu,h_m)=\phi(X_u)\qquad(u\in\mathscr D_m),
\qquad \|h_m\|=c_m.
\tag{4.2}
$$
这是一个真正的有限维正 Gram 系统：分母来自向量
$\{G\chi_F:F\subseteq[0,m)\}$ 的 Hilbert Gram 矩阵。它不使用 R250 的双线性正常矩矩阵作为正 Gram 矩阵。

限制关系给
$$
h_m=P_{CE_m}h_{m+1},
$$
从而对 $n\ge m$，
$$
\|h_n-h_m\|^2=c_n^2-c_m^2.
\tag{4.3}
$$
故以下条件准确等价：
$$
\sup_mc_m<\infty
\quad\Longleftrightarrow\quad
h_m\text{ 在 }H\text{ 中收敛}
\quad\Longleftrightarrow\quad
\text{第3节的三种表示存在}.
\tag{4.4}
$$
在有限维层面无须预先选择 $\phi$ 的向量配对分解；正有限秩密度可以直接产生右端的矩。

(4.4) 给实际计算接口，不提供 $c_m$ 的统一界，也不把有限维每层都可解误作整个无限系统有有界解。

## 5. 慢主理想湮灭者的必要发散

现在固定在全 $H$ 单射的 $S\in\mathfrak C$，并假设
$$
\phi(SF)=0\qquad(F\in\mathcal A).
\tag{5.1}
$$
由 (1.1) 和正常性，(5.1) 延伸到所有 $F\in\mathfrak C$。

若第3节等价条件成立，则对任意 $F\in\mathfrak C$，
$$
0=\phi(PSF)=B(FSh,1).
$$
取 $F=A^n$，用 $C$ 对称、$1$ 的循环性和 $B$ 非退化，得到 $Sh=0$；$S$ 单射迫 $h=0$。再由 (3.3)，
$$
\boxed{\phi|_{\mathfrak C}=0.}
\tag{5.2}
$$

特别，若 $\rho\ne0$ 是正正常密度、$\phi(T)=\operatorname{Tr}(\rho T)$，则 $\phi(I)=\operatorname{Tr}\rho>0$，与 (5.2) 矛盾。故任何非零正正常慢主理想湮灭者都必须满足：
$$
\boxed{
c_m(P,\phi)\longrightarrow\infty
\quad\text{对每个满足第1节假设的 }P.
}
\tag{5.3}
$$
其中包括每个非零规范正一阶无穷预解式乘积。

这里不必先证明某个单独的 $\phi(P)\ne0$：若 (A) 存在，收缩强单位已使其零表示推出整个 $\phi|_{\mathfrak C}=0$。也不必把 $S$ 的全空间稠密像搬到未知不变限制。

## 6. 与 R244 逐列条件及现有障碍的关系

若 $\rho=\sum_{i=1}^d f_i\otimes f_i$，且 R244 的
$$
Pf_i\in\operatorname{Dom}X_{Cf_i}\qquad(1\le i\le d)
$$
成立，则 R244 已直接产生 (A)，因而本稿 (B) 必成立。

反过来，本稿 (B) 只约束一个聚合正常泛函，不要求分别证明上述 $d$ 个最小图域包含，也不要求为迹类无限分解支付逐项乘子像的绝对和。存在 (B) 就足够排慢湮灭者。没有断言 (B) 自动推出每个单独的配对域条件。

R240 的固定正循环向量及 R230 的无穷逆测试附录仍证明：一般正正常性不保证任何规范 $P$ 满足 (B)。例如其指定高次数块矩以指数规模增长，而 R261 给该次数上的逆范数只有 $e^{o(\sqrt q)}$；于是 (4.1) 无界。这个反例本身不满足 (5.1)，故不能否定见证专属构造。

新的实际待证点可以准确写成：利用正性与全部慢矩方程 (5.1)，为该密度选择一个满足第1节假设的 $P$，使 (4.1) 一致有界；或者直接证明其聚合矩在某个这样的逆图范数中连续。当前证明尚未提供这一界，不将本等价式或有限维检验登记为普通 ISP 的完成。
