# R682：真实 CM 归一 Abel 积分的共同首阶与消元方程的去因子展开

日期：2026-11-14。状态：**在 R616/R634 明列的实际非消失前提下，本文各引理已证明；真实高度的首项赋值和全部候选排除仍开放。**

本文不添加一个未经证明的 $m=1$ 假设。新结论是：R634 外积的第二因子不仅作为一个向量在第 $m$ 阶非零，而且它的每一个坐标都恰在第 $m$ 阶非零。证明只需要原有理 CM 点、$\mathbb Q$-单性、实际实乘和 $p$ 进解析子群定理，不依赖丢失的 R571/R578 文件。随后给出任意 $m$ 下真实外积的准确首项、去除共同 CM 因子的方法，以及一个把有限 jet 与完整尾界连接起来的严格判据。

## 1. 保持同一实际曲线、商和 CM 点

保留 R634 的全部对象和前提：

$$
X=X_1=Z_p,\quad f=j_A=q[x-c_0]:X\longrightarrow A,
\quad \beta=f(c_1)\in A(\mathbb Q),\quad z=a-1.
$$

$A$ 在 $\mathbb Q$ 上单，$\beta$ 非挠，

$$
F=\operatorname{End}_{\mathbb Q}^0(A),\qquad
[F:\mathbb Q]=g=\dim A\ge3,
\qquad F\otimes\mathbb Q_p\simeq\mathbb Q_p^g.
\tag{682.1}
$$

这些结论采用 R616 的同一实际前提
$L'(g_{-1,+},1)L(g_{-1,-},1)\ne0$；本文不证明该前提对全部 $p$ 成立。
局部参数 $z$ 及 $f-\beta$ 均在 $\mathbb Q$ 上定义。

写 $G=g(X)$。在一个充分小的 $p$ 进盘中，特征零形式群对数给

$$
\log_p f(c_1+z)=L+U(z),\qquad L=\log_p\beta,
\qquad U(z)=u_mz^m+u_{m+1}z^{m+1}+\cdots,
\tag{682.2}
$$

其中所有 $u_n\in\operatorname{Lie}(A)(\mathbb Q)$，$u_m\ne0$。
这里对数恒等式来自群同态性，$U$ 是 $f-\beta$ 的形式对数，不是声称 $\log_p f$ 的常数项在 $\mathbb Q$ 中。

$m$ 有限：$f$ 非常值，因为 $q$ 非零且 Abel 像生成 Jacobian；特征零形式群对数是形式同构，故 $U$ 不恒为零。

## 2. 有理非挠点的对数不落在真代数超平面

**引理 682.1。** 设 $B/\mathbb Q$ 为 $\mathbb Q$-单阿贝尔簇，$P\in B(\mathbb Q)$ 非挠。固定嵌入 $\overline{\mathbb Q}\hookrightarrow\mathbb C_p$。对每个非零代数不变微分

$$
\omega\in H^0(B_{\overline{\mathbb Q}},\Omega^1),
$$

都有 $\omega(\log_pP)\ne0$。

**证明。** 首先 $\log_pP$ 有定义且非零。由于 $B$ proper，$B(\mathbb Q_p)$ 是紧 $p$ 进 Lie 群。取一个充分小的开子群 $B_1$，使形式对数在其上单射；紧性给 $B(\mathbb Q_p)/B_1$ 有限。如果 $\log_pP=0$，某个正整数 $n$ 满足 $nP\in B_1$，进而 $\log_p(nP)=0$ 强制 $nP=0$，与非挠性矛盾。

假设 $\omega(\log_pP)=0$。则

$$
V=\ker\omega\subsetneq\operatorname{Lie}(B_{\overline{\mathbb Q}})
$$

是一个真 $\overline{\mathbb Q}$-线性子空间。若 $\dim B=1$，$V=0$ 已与 $\log_pP\ne0$ 矛盾。其余情形对 $P$ 和 $V$ 应用 Fuchs–Pham 的 Theorem 2.2，得到正维代数子群 $H\subset B_{\overline{\mathbb Q}}$，满足

$$
P\in H(\overline{\mathbb Q}),\qquad\operatorname{Lie}(H)\subset V.
$$

特别 $H$ 是真子群。这里绝不把 $\mathbb Q$-单性误换成几何单性；$H$ 可能仅在数域上定义。

取一个有限 Galois 扩张 $L_0/\mathbb Q$，使 $H$ 在 $L_0$ 上定义，令

$$
H_0=\bigcap_{\sigma\in\operatorname{Gal}(L_0/\mathbb Q)}\sigma(H).
$$

这是有限个闭代数子群的交，且由 Galois 下降在 $\mathbb Q$ 上定义。因为 $P$ 是有理点，每个 $\sigma(H)$ 都包含 $P$，所以 $P\in H_0$。
代数群 $H_0$ 只有有限多个几何连通分支。故某个正整数 $r$ 使 $rP\in H_0^0$；$rP$ 仍非挠，从而 $H_0^0$ 正维。特征零中的恒等连通分支在 $\mathbb Q$ 上定义，且它是 $B$ 的阿贝尔子簇。
另一方面 $H_0^0\subset H\subsetneq B$，所以它是真阿贝尔子簇，与 $B$ 的 $\mathbb Q$-单性矛盾。证毕。

这里需要的是**交**：取 Galois 共轭的和可能等于整个 $B$，不能提供矛盾。
本引理也证明本篇所有对数特征分量非零；不需要预先假定 $p$ 进调节子为单位。

## 3. 每个实乘坐标的共同首阶

$\operatorname{Lie}(A)(\mathbb Q)$ 通过实乘成为一个 $F$-向量空间。
该作用忠实：非零 $a\in F$ 在同源范畴可逆，其切映射也可逆。
由 $\dim_{\mathbb Q}\operatorname{Lie}(A)=g=[F:\mathbb Q]$，它在 $F$ 上的维数为一。
选取一个 $F$-基 $e\in\operatorname{Lie}(A)(\mathbb Q)$，写

$$
u_n=b_ne,\qquad b_n\in F,\qquad b_m\ne0.
\tag{682.3}
$$

令 $\sigma_1,\ldots,\sigma_g:F\hookrightarrow\mathbb Q_p$ 为各嵌入。相应坐标泛函 $\omega_i$ 由
$\omega_i(be)=\sigma_i(b)$ 唯一确定；它们的系数为代数数，是 $g$ 个线性独立的代数不变微分。
记

$$
L_i=\omega_i(L),\qquad a_i=\sigma_i(b_m),\qquad
T_i=\frac{a_i}{L_i}.
\tag{682.4}
$$

由引理 682.1，$L_i\ne0$；由 $b_m\ne0$，所有 $a_i\ne0$。

R634 的归一函数因此准确为

$$
t_i(z)=1+\frac{\sum_{n\ge m}\sigma_i(b_n)z^n}{L_i}
       =1+T_i z^m+O(z^{m+1}).
\tag{682.5}
$$

**定理 682.2（共同首阶）。** 所有 $T_i$ 非零且两两不同。特别，对任何 $i\ne j$，

$$
\operatorname{ord}_{z=0}(t_i-1)=m,
\qquad
\operatorname{ord}_{z=0}(t_i-t_j)=m,
$$
$$
\boxed{\quad
\operatorname{ord}_{z=0}(t_i^2-t_j^2)=m,
\qquad [z^m](t_i^2-t_j^2)=2(T_i-T_j)\ne0.
\quad}
\tag{682.6}
$$

**证明。** 只需排除 $T_i=T_j$。该等式给

$$
a_iL_j-a_jL_i=0.
$$

因为 $\omega_i,\omega_j$ 独立而 $a_i,a_j\ne0$，
$a_i\omega_j-a_j\omega_i$ 是非零代数不变微分。上式说它杀掉 $\log_p\beta$，与引理 682.1 矛盾。
式 (682.5) 随即给前两项；最后一项也可由
$(t_i^2-t_j^2)=(t_i-t_j)(t_i+t_j)$ 和 $(t_i+t_j)(0)=2$ 得到。证毕。

这个结论加强 R634 Lemma 634.4 的向量结论。它仍未给
$v_p(T_i-T_j)$ 的上界或下界，也未证明 $m=1$。

**附带的代数上界。**

$$
1\le m\le2(G-g)+1.
\tag{682.7}
$$

证明：$f^*H^0(A,\Omega^1)$ 是 $g$ 维；$f^*$ 单射因为 $q$ 满射且 Abel 拉回在一阶微分上是同构。由 (682.2)，这些微分全在 $c_1$ 至少消失 $m-1$ 阶。因此

$$
h^0\bigl(X,K_X-(m-1)c_1\bigr)\ge g.
$$

该线丛有效，且由 Serre 对偶其 $h^1=h^0((m-1)c_1)\ge1$，所以是 special。Clifford 不等式给

$$
g\le\frac{2G-2-(m-1)}2+1=G-\frac{m-1}2,
$$

即 (682.7)。此界随 $X$ 改变，不构成绝对 Serre 界。

## 4. 任意共同首阶下的真实外积展开

完全保留 R634 的同一 $\Lambda_i$、$\Omega$、$d_i$：

$$
d_i=\Lambda_i(0)+(\omega_0)_i,\qquad
\delta_i=(\omega_0)_i-\omega_i,
$$
$$
V_i=t_i^2-t_g^2,\qquad
W_i=d_i t_i^2-\Lambda_i-\omega_i,
\qquad\mathcal E_{ij}=W_iV_j-W_jV_i.
\tag{682.8}
$$

令

$$
v_i=2(T_i-T_g)\ne0,
\quad V_i=z^m\widehat V_i,
\quad\widehat V_i(0)=v_i.
\tag{682.9}
$$

写 $\Lambda_i(z)=\Lambda_i(0)+\sum_{n\ge1}\lambda_{i,n}z^n$，则准确有

$$
W_i(z)=\delta_i-\sum_{1\le n<m}\lambda_{i,n}z^n
      +(2d_iT_i-\lambda_{i,m})z^m+O(z^{m+1}).
\tag{682.10}
$$

特别所有 $\mathcal E_{ij}$ 都含人为的共同因子 $z^m$，并且

$$
\boxed{\quad[z^m]\mathcal E_{ij}=\delta_iv_j-\delta_jv_i.\quad}
\tag{682.11}
$$

对相同目标 $\omega=\omega_0$，$\delta=0$，所以全部外积至少含 $z^{m+1}$。
若 $n\ge1$ 是向量 $W(z)$ 的首非零阶，写
$W(z)=w_nz^n+O(z^{n+1})$，则

$$
[z^{m+n}]\mathcal E_{ij}=(w_n)_iv_j-(w_n)_jv_i,
\qquad \operatorname{ord}\mathcal E_{ij}\ge m+n.
\tag{682.12}
$$

当右侧非零时恰等于 $m+n$。如果 $m>1$，$\Lambda$ 的低阶项仍可能使 $n<m$；不能把同目标首阶无条件写成 $2m$。$m=1$ 时 (682.10)–(682.12) 恰恢复 R634 (634.31)–(634.33) 的二次候选首项。

因为每个 $\widehat V_i(0)\ne0$，可在足够小的盘中逐个取倒数，定义

$$
\mathcal H_{ij}(z)=
\frac{W_i(z)}{\widehat V_i(z)}-
\frac{W_j(z)}{\widehat V_j(z)}.
\tag{682.13}
$$

这给准确恒等式

$$
\mathcal E_{ij}(z)=z^m\widehat V_i(z)\widehat V_j(z)
                       \mathcal H_{ij}(z).
\tag{682.14}
$$

因此在这个盘的 $z\ne0$ 部分，用 $\mathcal H_{ij}=0$ 替换原方程不会增加或删除根；它只去掉外积构造强加的 CM 因子，并用真正非零的单位级数作除法。这里“单位级数”指常数项在系数域非零，绝不等同于常数项是 $p$-整单位；有限精度损失仍须计入 $v_p(v_i)$。

跨目标时

$$
\mathcal H_{ij}(0)=\delta_i/v_i-\delta_j/v_j.
\tag{682.15}
$$

若这个数非零，就可以尝试按下面的严格尾判据排除该目标在深盘中的所有根；本文不声称它已对所有 $\Omega^2$ 非零。同目标的 $\mathcal H_{ij}(0)$ 必为零，须继续求真实下一阶。

## 5. 从完整尾界得到可执行的深盘排除

以下只是一个严格接口，必须代入同一个真实高度函数的系数，不能用 Abel 系数替代。

**引理 682.3（有限 jet 加完整线性尾界）。** 设

$$
F(z)=\sum_{n\ge\nu}c_nz^n,\qquad c_\nu\ne0,
$$

在 $v_p(z)\ge s$ 收敛。设存在 $N>\nu$ 及实数 $A,B$，使对所有 $n\ge N$

$$v_p(c_n)\ge A-Bn.$$

若 $s>B$ 且

$$
v_p(c_n)+(n-\nu)s>v_p(c_\nu)
\quad(\nu<n<N),
$$
$$
A-BN+(N-\nu)s>v_p(c_\nu),
\tag{682.16}
$$

则在 $0\ne z$、$v_p(z)\ge s$ 上，$F(z)\ne0$，并且

$$v_p(F(z))=v_p(c_\nu)+\nu v_p(z).$$

**证明。** 对 $n>\nu$ 比较第 $n$ 项与首项，额外赋值是
$v_p(c_n)-v_p(c_\nu)+(n-\nu)v_p(z)$。
对有限段由 (682.16) 为正。对 $n\ge N$，它至少为
$A-Bn-v_p(c_\nu)+(n-\nu)s$；因为 $s>B$，这个表达式关于 $n$ 递增，其在 $N$ 已严格为正。
故首项的赋值严格小于所有其余项；收敛的非阿基米德和不能抵消这个唯一最小项。证毕。

可直接应用于 $F=\mathcal E_{ij}$，这样不必执行 (682.13) 的除法。
例如若已对所有 $n\ge0$ 严格得到

$$
v_p([z^n]t_i)\ge A_t-Bn,\quad A_t\le0,
$$
$$
v_p([z^n](\Lambda_i+\omega_i))\ge A_\Lambda-Bn,
\quad v_p(d_i)\ge A_d,
\tag{682.17}
$$

则有限卷积及超度量不等式给

$$
v_p([z^n]\mathcal E_{ij})\ge
\min\{A_d+4A_t,\ A_\Lambda+2A_t\}-Bn.
\tag{682.18}
$$

证明只需把 (682.8) 写成 $d\,t^2(t^2-t^2)$ 与
$(\Lambda+\omega)(t^2-t^2)$ 的和；每个总次数 $n$ 的乘积具有 (682.18) 的下界。无需丢弃任何高阶项，也不把长尾当成“数值很小”。

原候选的 $v_p(a-1)\ge4$ 可在已有真实 (682.17) 时取 $s=4$。
目前未知的 $L_i$ 赋值、$\Lambda$ 的真实系数、$\Omega$ 的目标值均会进入这些常数。
没有这些输入，(682.16) 不能自动成立。

## 6. 适用范围和仍未解决的步骤

本文完成了每个归一坐标的共同首阶、$\mathbb Q$-单情形所必需的 AST 下降、一个几何阶数上界，以及任意 $m$ 的真实外积首项与严格尾判据。它没有计算固定 $Y$-线性高度 $\ell_h$、同一规范下的 $\Omega$，或 $\lambda_{p,h}^F$ 的实际 jet。

特别：

* 引理 682.1 只排除**代数系数的线性关系**。跨目标的 (682.15) 一般含 CM 点对数的商与 $\log_p2,\log_p3$；不能直接据 AST 断言它非零。
* R588 的 $M_2\overline M_2$ 公式涉及两个真正的高权**中心** $L$ 值，不能以收敛半平面中的 Euler 乘积非零代替其中心非消失。
* 本文不证明 $m=1$、$v_p(v_i)=0$ 或 (682.12) 非零，不从 BMS 的逐盘非恒零推出一个统一排除半径。

下一项实际工作应在这些同一坐标中求 $\Lambda$ 的真 jet 与有限目标，或另证足够强的统一赋值界；不能把去因子处理本身登记为候选排除。

## 来源

1. Clemens Fuchs and Duc Hiep Pham, *The p-adic analytic subgroup theorem revisited*, 2015, Theorem 2.2, printed p.2, <https://arxiv.org/pdf/1502.00768>。本文已另给从 $\overline{\mathbb Q}$ 子群到有理非挠点和 $\mathbb Q$-单性的完整交下降论证。
2. Robin Hartshorne, *Algebraic Geometry*, 1977, Theorem IV.5.4（Clifford）；亦见 Xinyi Yuan–Tong Zhang, *Effective bound of linear series on arithmetic surfaces*, Theorem 5.1, <https://faculty.bicmr.pku.edu.cn/~yxy/preprints/effective_bound.pdf>。
3. Amnon Besser, J. Steffen Müller, Padmavathi Srinivasan, *p-adic adelic metrics and Quadratic Chabauty I*, arXiv:2112.03873v4, 2026, Lemma 7.1 and Theorem 7.9, <https://arxiv.org/pdf/2112.03873>。本文只承接 R634 使用它们得到的真实有限目标及逐盘非恒零；这些定性结论不替代 (682.16)。
4. 本仓库 R593、R596、R616、R634：同一实际线丛、固定线性高度、CM 点、实乘、原高度规范及外积。没有沿用未恢复的旧数值。
