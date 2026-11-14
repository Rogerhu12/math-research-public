# 有界正则化传递循环性与任意复第一 chaos 的独立乘积

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。

状态：完整证明，供 R132 登记。主引理由根代理指出，本文独立核验其定义域交换、稠密值域与闭不变空间保持的每一步。它把旧稿中“除至多一个因子外同射线或绝对可和”的限制全部删除。

## 1. 实际交换子代数提供的两个接口

沿用本题实际算子 $A$、Hilbert 空间 $H=L^2(\mathbb Z_2,\mu)$ 以及共轭

$$
(Cu)(y)=\overline{u(-1-y)}.
$$

R88 给出以下两条性质：

1. 每个 $T\in\{A\}'$ 满足 $T^*=CTC$；因此有界交换子的单射性与稠密值域等价。
2. $\{A\}'$ 是 $A$ 的多项式的强算子闭包；因此每个闭 $A$-不变子空间被全部有界交换子保持。

第一条的直接理由是

$$
(\overline{\operatorname{Ran}T})^\perp
=\ker T^*=C\ker T.
\tag{1.1}
$$

第二条在下面使用时只针对一个已给定的闭不变空间：多项式保持该空间，强极限仍保持它。

若 $v\in H$，记其闭循环空间为

$$
\mathcal M(v)=\overline{\operatorname{span}\{A^nv:n\ge0\}}.
$$

## 2. 有界正则化传递循环性

**引理 2.1。** 设 $T$ 是稠密定义的闭单射算子。若存在单射的有界交换子 $R\in\{A\}'$，满足

$$
\operatorname{Ran}R\subseteq\operatorname{Dom}T,
\qquad S:=TR\in\{A\}'\subseteq B(H),
\tag{2.1}
$$

并且

$$
R\operatorname{Dom}T\subseteq\operatorname{Dom}T,
\qquad TRu=RTu\quad(u\in\operatorname{Dom}T),
\tag{2.2}
$$

那么对每个循环向量 $v\in\operatorname{Dom}T$，向量 $Tv$ 也循环。

**证明。** 若 $Sx=0$，则 $T(Rx)=0$。由 $T$ 单射先得 $Rx=0$，再由 $R$ 单射得 $x=0$。所以 $S$ 是单射有界交换子；由 (1.1)，它的值域稠密。

$v$ 循环及 $SA=AS$ 给

$$
\mathcal M(Sv)
=\overline{S\operatorname{span}\{A^nv:n\ge0\}}
=\overline{\operatorname{Ran}S}=H.
\tag{2.3}
$$

令 $M=\mathcal M(Tv)$。它是闭 $A$-不变子空间，故由 §1，$RM\subseteq M$。又由 (2.2)，

$$
Sv=TRv=RTv\in M.
$$

包含循环向量 $Sv$ 的闭 $A$-不变空间只能是 $H$，所以 $M=H$。证毕。

这个证明不把无界 $T$ 作用于稠密轨道后所得的像直接视为稠密；真正作用于轨道的是有界且稠密值域的 $S=TR$。也不要求 $T$ 在任意闭不变子空间上的限制值域稠密。

## 3. 任意复第一 chaos 乘子都满足引理

取

$$
0\ne h=c+\sum_{j\ge0}a_j\chi_j,
\qquad a\in\ell^2.
\tag{3.1}
$$

令 $X_h$ 为 R125 构造的实际闭乘子。我们使用已证明的准确接口：

$$
X_h1=h,\qquad \ker X_h=\{0\},
\qquad H_{\le p}\subseteq\operatorname{Dom}X_h\quad(p<\infty),
\tag{3.2}
$$

以及 R128 的全部有界交换子域交换：

$$
T\operatorname{Dom}X_h\subseteq\operatorname{Dom}X_h,
\qquad X_hTu=TX_hu\quad(T\in\{A\}').
\tag{3.3}
$$

把系数写成四个非负部分

$$
a=b_1-b_2+i b_3-i b_4,
\qquad b_\nu\ge0,\quad b_\nu\in\ell^2,
\qquad(\lambda_1,\lambda_2,\lambda_3,\lambda_4)=(1,-1,i,-i).
$$

固定任意 $t>0$，R128 给非负闭乘子的收缩预解式

$$
R_\nu=(I+tX_{b_\nu})^{-1}\in\{A\}',
\qquad\|R_\nu\|\le1.
\tag{3.4}
$$

零分量取 $X_{b_\nu}=0$、$R_\nu=I$。每个 $R_\nu$ 都单射；它们两两交换，并保持各个 $X_{b_\mu}$ 的定义域。于是

$$
R=\prod_{\nu=1}^4R_\nu
\tag{3.5}
$$

是单射的有界交换子，而且

$$
\operatorname{Ran}R
\subseteq\bigcap_{\nu=1}^4\operatorname{Dom}X_{b_\nu}
\subseteq\operatorname{Dom}X_h.
\tag{3.6}
$$

第一包含可把任意指定的 $R_\nu$ 放在乘积最左边；第二包含及共同定义域上的等式

$$
X_h=cI+\sum_{\nu=1}^4\lambda_\nu X_{b_\nu}
$$

是 R128 通过伴随图核心配对证明的结果，不需要未经证明地交换闭包与求和。

由 $tX_{b_\nu}R_\nu=I-R_\nu$，有有界恒等式

$$
\boxed{
S:=X_hR
=cR+\frac1t\sum_{\nu=1}^4
\lambda_\nu(I-R_\nu)\prod_{\mu\ne\nu}R_\mu
\in\{A\}'.
}
\tag{3.7}
$$

(3.3) 又给 $X_hRu=RX_hu$ 于整个 $\operatorname{Dom}X_h$。所以引理 2.1 的全部条件成立。

**定理 3.1。** 任意非零第一 chaos 闭乘子 $X_h$，都把其定义域内的每个循环向量送到循环向量：

$$
\boxed{
v\in\operatorname{Dom}X_h,\quad\mathcal M(v)=H
\quad\Longrightarrow\quad\mathcal M(X_hv)=H.
}
\tag{3.8}
$$

这里 $a$ 是任意复 $\ell^2$ 序列，没有相位或绝对可和条件。若 $a=0$ 而 $c\ne0$，则 $X_h=cI$，同一结论当然成立，上面的正则化取 $R=I$ 即可。非零条件不可删除。

更一般地，可连续施加有限个这类闭乘子：只要各步所得向量确实属于下一步的定义域，从一个循环向量出发所得每一步仍循环。下一节给出不需要额外检验定义域的一类具体向量。

## 4. 两两独立位集合上的任意复第一 chaos 乘积

**定理 4.1。** 设 $J_1,\ldots,J_p\subseteq\mathbb N_0$ 两两不交，且

$$
h_\nu=c_\nu+\sum_{j\in J_\nu}a_{\nu,j}\chi_j\ne0,
\qquad a_\nu\in\ell^2(J_\nu).
\tag{4.1}
$$

所有系数和常数都允许任意复数。则点态乘积

$$
\boxed{f=\prod_{\nu=1}^p h_\nu}
\tag{4.2}
$$

属于 $H_{\le p}$，非零，并且对实际 $A$ 循环。

**证明。** 各因子依赖的位集合不交，故在乘积 Haar 空间上独立。于是

$$
\|f\|_2=\prod_{\nu=1}^p\|h_\nu\|_2>0.
\tag{4.3}
$$

分别截断每个第一阶 Walsh 展开，有限乘积在 $L^2$ 中趋于 $f$；这可由逐因子的望远镜展开与独立性直接得到。每个有限乘积的 Walsh 次数至多 $p$，故 $f\in H_{\le p}$。

下面核验实际闭乘子与这些点态乘积之间的等式。若 $u$ 不依赖第 $j$ 位，则真实一位公式给

$$
V_ju=\chi_ju,
\qquad V_j=(I-N_j)(I+N_j)^{-1}.
\tag{4.4}
$$

事实上，按该位写 $u=(v,v)$，而

$$
N_j=\begin{pmatrix}0&\eta_jN_{j+1}\\I&0\end{pmatrix}.
$$

所以 $(I+N_j)(v,0)=(v,v)$，再作用 $I-N_j$ 得 $(v,-v)$。这个等式保留了实际进位，并没有以纯模型替换 $N_j$。

设 $u\in H_{\le q}$ 只依赖与 $J_\nu$ 不交的位。R125 的实际有限系数部分在每个固定有限次数层上收敛到 $X_{h_\nu}$。由 (4.4)，

$$
\begin{aligned}
X_{h_\nu}u
&=\lim_{n\to\infty}
\left(c_\nu u+\sum_{j\in J_\nu,\ j<n}a_{\nu,j}V_ju\right)\\
&=\left(c_\nu+\sum_{j\in J_\nu}a_{\nu,j}\chi_j\right)u
=h_\nu u.
\end{aligned}
\tag{4.5}
$$

最后一步还可直接以独立性核验：数值系数尾对应的 $L^2$ 范数恰为

$$
\|u\|_2\left(\sum_{j\in J_\nu,\ j\ge n}|a_{\nu,j}|^2\right)^{1/2}\longrightarrow0.
$$

从循环向量 $u_0=1$ 开始，依次置 $u_\nu=\prod_{\mu\le\nu}h_\mu$。已经证明 $u_{\nu-1}\in H_{\le\nu-1}\subseteq\operatorname{Dom}X_{h_\nu}$，且

$$
u_\nu=X_{h_\nu}u_{\nu-1}.
$$

用定理 3.1 归纳，每个 $u_\nu$ 均循环，特别是 $f$ 循环。证毕。

## 5. 结论的范围

定理 3.1 是对真实闭乘子及其真实定义域的结论。独立乘积定理不要求任何一个因子的系数在 $\ell^1$，也不要求同射线；全部因子都可为任意复 $\ell^2$ 系数。

这里的独立性用于 (4.5)，即让真实乘子作用精确成为所写的点态乘积。若不同因子依赖重叠位，不能未经核验就把它们的点态乘积当作真实乘子复合；有限个此类循环乘积的任意非零线性组合也没有由本文自动得到循环性。

本稿仍未证明一般复第一 chaos 乘子在任意闭 $A$-不变子空间上的限制值域稠密。引理 2.1 只在给定的输入向量已经循环时传递循环性，未越过该剩余问题。

依赖：R88 的全交换子结构；
[R125：全部第一 chaos 闭乘子与循环性](2026-11-12-all-l2-first-chaos-closed-multiplier-cyclicity-0c.md)；
[R128：共同正则化与不变部分](2026-11-12-unbounded-first-chaos-domains-and-invariant-parts-0c-agent.md)。
