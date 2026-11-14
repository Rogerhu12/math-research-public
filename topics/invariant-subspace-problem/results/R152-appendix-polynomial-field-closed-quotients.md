# R152 附录：整个 $K(S)$ 的最大闭分式场与原分母图核心

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。独立附录，不另占结果号。

状态：完整证明。本稿保持已冻结的 R152 主稿不变，把其中 $\mathcal G$ 系数多项式的单射稠密结论，推广为整个分式域的闭算子演算。关键新增步骤是：在 $K[t]$ 中取 gcd 后，用两次有限清分母和 $\mathcal G$ 的二维放大稠密性恢复原始分母的完整图核心。

## 1. 设置与准确范围

沿用 R151/R152 的实际算子代数 $\mathcal A$、快速解析逼近代数 $\mathcal G$、形式嵌入 $\iota$，以及

$$
K=\operatorname{Frac}(\mathcal G)\subseteq\mathbb C((z)).
$$

设 $S\in\mathcal A$ 满足

$$
\gamma_\zeta(S)-S\in\mathcal G
\quad\text{对全部 dyadic }\zeta,
$$

并记

$$
\mathcal R=\mathcal G[S]\subseteq\mathcal A,
\qquad \sigma=\iota(S),
\qquad \mathcal F=\operatorname{Frac}(\mathcal R)=K(\sigma).
\tag{1.1}
$$

为简化记号也把最后的形式分式域写作 $K(S)$。
R152 §7 已证明：$\mathcal R$ 的每个非零实际算子都单射且值域稠密。
同时，$\sigma$ 若代数于 $K$，就已属于 $K$；另一分支是 $\sigma$ 超越于 $K$。

对 $r=p/q\in\mathcal F$，其中 $p,q\in\mathcal R$、$q\ne0$，定义

$$
\operatorname{Dom}T_r=\{x:px\in\operatorname{Ran}q\},
\qquad qT_rx=px.
\tag{1.2}
$$

这里 $p,q$ 已是实际有界算子，不把一般 $K$ 系数单独当作有界算子求值。

**定理。** 最大实现 (1.2) 只依赖分式 $r$，闭、稠密定义，并满足

$$
\boxed{
\operatorname{Graph}T_r
=\overline{\{(qh,ph):h\in H\}},
\qquad T_r=CT_r^*C.
}
\tag{1.3}
$$

参数 $h$ 可限制于 $\mathbb C[A]1$ 或全部有限柱向量。
它给 $\mathcal F$ 的忠实闭分式演算：

$$
\overline{T_r+T_s}=T_{r+s},\qquad
\overline{T_rT_s}=T_{rs},\qquad
(T_r)^{-1}=T_{1/r}\quad(r\ne0).
\tag{1.4}
$$

每个非零 $T_r$ 单射且值域稠密；每个非恒定 $r$ 的全部 $T_r-\lambda I$ 亦然。
此外，对非零 $r$ 和 $x\in\operatorname{Dom}T_r$，

$$
\boxed{x\text{ 对 }A\text{ 循环}
\iff T_rx\text{ 对 }A\text{ 循环}.}
\tag{1.5}
$$

式 (1.5) 是全空间循环性的等价，不是一般的
$\operatorname{cyc}_A(x)=\operatorname{cyc}_A(T_rx)$。
对超越分支的任意 $\mathcal R$ 元素，目前并未证明它在每个不变限制上像稠密。

## 2. 有限放大密度直接给图核心

先记一个有界代数引理。
设 $p_1,q_1,a,b\in\mathcal A$，彼此交换，且 $q_1$ 单射稠密，并有

$$
ap_1+bq_1=D,\qquad 0\ne D\in\mathcal G.
\tag{2.1}
$$

令

$$
\mathcal M=\{(x,y)\in H\oplus H:p_1x=q_1y\}.
$$

这是闭 $A\oplus A$ 不变空间。
R151 的全部有限放大稠密性给

$$
\overline{(D\oplus D)\mathcal M}=\mathcal M.
\tag{2.2}
$$

给定 $(x,y)\in\mathcal M$，置 $h=bx+ay$。由 (2.1) 及 $p_1x=q_1y$，直接算得

$$
q_1h=Dx,\qquad p_1h=Dy.
\tag{2.3}
$$

所以

$$
(D\oplus D)\mathcal M
\subseteq\{(q_1h,p_1h):h\in H\}
\subseteq\mathcal M.
$$

以 (2.2) 取闭包，得到

$$
\boxed{
\mathcal M=\overline{\{(q_1h,p_1h):h\in H\}}.
}
\tag{2.4}
$$

这一证明使用的是 $D\oplus D$ 在整个闭图上的密度。
只知道 $D$ 在 $H$ 上稠密不足以代替 (2.2)。
也不需要构造任何未经证明一致有界的 $D$ 近似逆。

## 3. 超越分支：gcd、两次清分母与原始图

假设 $\sigma$ 超越于 $K$。此时 $\mathcal G[t]\to\mathcal R$ 的求值是单射。
取非零 $p=P(S)$、$q=Q(S)$，其中 $P,Q\in\mathcal G[t]$。

在域 $K$ 上取首一 gcd

$$
g=\gcd_{K[t]}(P,Q),\qquad
P=gP_0,\quad Q=gQ_0,
\quad\gcd(P_0,Q_0)=1.
$$

$g,P_0,Q_0$ 的系数可能都只属于 $K$，因此此处还不能直接求值。
选择两个非零 $\mathcal G$ 元素 $a_0,c_0$，分别清除有限组系数的分母，使

$$
g_1=a_0g\in\mathcal G[t],\qquad
P_1=c_0P_0\in\mathcal G[t],\qquad
Q_1=c_0Q_0\in\mathcal G[t].
\tag{3.1}
$$

令 $d=a_0c_0\in\mathcal G\setminus\{0\}$，则有真实多项式恒等式

$$
dP=g_1P_1,\qquad dQ=g_1Q_1.
\tag{3.2}
$$

$P_1,Q_1$ 在 $K[t]$ 中仍互素，因为 $c_0$ 在该域中为单位。
Euclidean 算法给 $u,v\in K[t]$，满足 $uP_1+vQ_1=1$。
再清除它们的有限多个分母，得到

$$
aP_1+bQ_1=D,
\qquad a,b\in\mathcal G[t],\quad
0\ne D\in\mathcal G.
\tag{3.3}
$$

现在且只现在，对 (3.1)—(3.3) 的 $\mathcal G[t]$ 元素在 $S$ 上求值。
为减少下标，把求值后的 $g_1,P_1,Q_1,a,b$ 分别记为 $g,p_1,q_1,a,b$。
它们全是 $\mathcal R$ 中的真实有界算子；$d,g,p_1,q_1,D$ 均非零，故单射稠密。

由 (3.2) 和单射的 $d,g$，对任意 $x,y$ 有

$$
px=qy
\iff dpx=dqy
\iff gp_1x=gq_1y
\iff p_1x=q_1y.
\tag{3.4}
$$

由 (3.3)，§2 给最后一个最大图的参数核心。
还需恢复**原始**分母 $q$，不能停在 $q_1$ 上。
因为 $dH$ 和 $gH$ 都在 $H$ 中稠密，而所有因子有界、交换，

$$
\begin{aligned}
\overline{\{(qh,ph):h\in H\}}
&=\overline{\{(qdh,pdh):h\in H\}}\\
&=\overline{\{(gq_1h,gp_1h):h\in H\}}\\
&=\overline{\{(q_1h,p_1h):h\in H\}}.
\end{aligned}
\tag{3.5}
$$

(3.4)、(3.5) 及 (2.4) 证明 (1.3) 的图核心断言。
共同因子 $g$ 在这里仅使用全空间单射稠密性；没有假设 $g$ 在未知限制上也像稠密。

若分子 $p=0$，最大图直接为 $\{(x,0):x\in H\}$，由 $qH$ 稠密立即得到原分母图核心，不需要 gcd。

## 4. 有理分支与 R153 的衔接

若 $\sigma$ 代数于 $K$，R152 已证明 $\sigma\in K$，故 $K(S)=K$。
R153 对 $\operatorname{Frac}(\mathcal G)$ 给出了更强的全部不变子商版本，本稿不重复其子商下沉、限制图核心和精确循环子空间等式。

本稿所需的全空间图核心也可直接说明。给 $p,q\in\mathcal R$，写 $bS=a$，其中 $a,b\in\mathcal G$、$b\ne0$。
取大于两多项式次数的 $n$，则

$$
p_0=b^np\in\mathcal G,\qquad
q_0=b^nq\in\mathcal G.
$$

最大图由单射的 $b^n$ 消去后不变；参数图闭包由 $b^nH$ 稠密也不变。
对 $\mathcal M=\{(x,y):p_0x=q_0y\}$，有

$$
(q_0\oplus q_0)(x,y)=(q_0x,p_0x),
$$

直接属于原参数图。
$q_0\in\mathcal G\setminus\{0\}$ 的二维放大在 $\mathcal M$ 上稠密，故仍得到 (1.3)。
这也使本附录的全空间论证不依赖 R153 尚未完成的任何新步骤。

## 5. 闭性、伴随域与更小图核心

因为 $q$ 单射，(1.2) 是单值算子；其图是有界映射 $(x,y)\mapsto px-qy$ 的闭核，故算子闭。
交换性使所有 $(qh,ph)$ 都在图中，因此定义域包含稠密的 $qH$。

以 $T^{(0)}(qh)=ph$ 定义稠密核心算子。
通常伴随的完整图条件为

$$
(v,w)\in\operatorname{Graph}(T^{(0)})^*
\iff p^*v=q^*w.
\tag{5.1}
$$

$p,q\in\mathcal A$，故 $p^*=CpC$、$q^*=CqC$。
共轭 (5.1) 得 $p(Cv)=q(Cw)$，正是最大图。
又 §§3–4 已给 $\overline{T^{(0)}}=T_r$，所以

$$
T_r=CT_r^*C.
$$

映射 $h\mapsto(qh,ph)$ 有界，而 $\mathbb C[A]1$ 和有限柱向量各自在 $H$ 中稠密，故它们都可作为参数空间。
准确图域核心为 $q\mathbb C[A]1$，或 $q$ 作用于有限柱向量。
例如 $r=1/A$ 时原始常向量 $1$ 并不在最大域内，故不能省去前面的 $q$。

对任意 $B\in\{A\}'$，$B$ 与 $p,q$ 交换。
若 $px=qy$，则 $pBx=qBy$，从而

$$
B\operatorname{Dom}T_r\subseteq\operatorname{Dom}T_r,
\qquad T_rBx=BT_rx.
\tag{5.2}
$$

## 6. 分式无关性与全部自然运算的闭包

若 $p/q=p'/q'$，即 $pq'=p'q$，对任意 $px=qy$，有

$$
q(p'x-q'y)=0.
$$

$q$ 单射给 $p'x=q'y$；反向同理。
所以最大图只依赖分式。
反之，若两个最大算子相同，在 $qq'h$ 上比较像就有 $pq'h=p'qh$ 对全部 $h$ 成立，故两个实际分式相同。
演算因此忠实。

写 $r=p/q$、$s=f/g$。自然和的域是两域之交，自然乘积的域是

$$
\{x\in\operatorname{Dom}T_s:T_sx\in\operatorname{Dom}T_r\}.
$$

它们都包含稠密的 $qgH$，且在该集合上

$$
(T_r+T_s)(qgh)=(pg+fq)h,\qquad T_rT_s(qgh)=pfh.
\tag{6.1}
$$

已证的原分母图核心说明，(6.1) 两个核心图的闭包分别为 $T_{r+s}$、$T_{rs}$。
反向，在自然和的任意域向量上乘共同分母 $qg$，直接得

$$
qg(T_r+T_s)x=(pg+fq)x.
$$

在自然乘积域上先令 $y=T_sx$、$z=T_ry$，则

$$
qgz=pf x.
$$

所以两自然图分别包含在对应的最大闭图中，结合核心反向包含得到 (1.4) 的和、积结论。
若分子结果为零，最大实现为全域零算子，仍同样成立。
若 $r\ne0$，交换图的两个坐标直接得到 $(T_r)^{-1}=T_{1/r}$。

这并不宣称自然乘积未经闭包已经闭，也不宣称两个相反顺序的原始乘积域相等。

## 7. 核、范围、实际除法与循环性反射

若 $r=p/q\ne0$，$p$ 单射给 $\ker T_r=0$。
又 $T_r(qh)=ph$，所以值域包含稠密的 $pH$。
当 $r$ 非恒定，$p-\lambda q\ne0$ 对每个 $\lambda$ 成立，且

$$
T_r-\lambda I=T_{(p-\lambda q)/q}
$$

为同定义域的算子等式。
故所有这些差均单射稠密，谱没有点谱或剩余谱。

预解及有界性的精确判据是

$$
\boxed{
\lambda\in\rho(T_r)
\iff\exists B\in B(H):(p-\lambda q)B=q,
}
\tag{7.1}
$$

$$
\boxed{
T_r\text{ 有界}
\iff\exists B\in B(H):qB=p.
}
\tag{7.2}
$$

例如 (7.1) 右边使 $(T_r-\lambda)Bx=x$；对最大域向量再用 $p-\lambda q$ 的单射性得左逆。
这给通常有界预解式。
同理 (7.2) 右边使最大图恰为全域有界算子 $B$ 的图。
反向均立即成立。满足这些等式的 $B$ 自动与 $A$ 交换：把等式分别左乘、右乘 $A$，再取消单射的对应因子即可。

最后令 $r\ne0$、$x\in\operatorname{Dom}T_r$。
若 $x$ 循环，$p$ 是有界稠密像的交换子，故 $px$ 循环。
又

$$
px=qT_rx\in\operatorname{cyc}_A(T_rx),
$$

因为 $q\in\mathcal A$ 保持该闭循环空间。于是 $T_rx$ 循环。
反向对 $1/r$ 和向量 $T_rx$ 应用同一论证，得到 (1.5)。

## 8. 与 R153 的边界及新增内容

当 $K(S)=K$，R153 还有每个不变子商上的单射稠密、原分母图核心、商下沉，以及精确循环子空间保持等更强结论。
本稿的新增部分是 $\sigma$ 超越于 $K$ 时的整个 $K(S)$：所有非零 $\mathcal G[S]$ 元素只已知全空间单射稠密，但 gcd 后产生的一个 $D\in\mathcal G$ 足以通过二维不变图密度完成最大图与最小图相等。

此证明没有把 $\mathcal G[S]$ 的一般元素提升为普遍限制稠密，也没有把 $C$ 自动下传到未知不变子商。
更没有给所有有界分式作标量全纯分类；(7.1)—(7.2) 保留的是实际有界算子除法条件。

依赖：

- [R152 主稿：快速 gauge 增量的混合芽与 $\mathcal G$ 系数多项式](../notes/2026-11-12-fast-gauge-increments-analytic-germs-and-closed-quotients-0c-agent.md)。
- [R151：$\mathcal G$ 在所有有限放大中的限制密度](../notes/2026-11-12-quartic-analytic-approximation-gauge-stability-0c-agent.md)。
- [R153：所有不变子商上的快速分式场](../notes/2026-11-12-fast-fraction-field-on-all-invariant-subquotients-0c-agent.md)。
