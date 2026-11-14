# 强近似单位消除闭图缺口：实际临界比值及全部解析芽之商

日期：2026-11-12（UTC）。子任务：literature。**状态：已证明。**

本条证明

$$
\boxed{\overline{\{(Ah,Lh):h\in H\}}
=\{(u,v):Lu=Av\}.}
$$

因此 R65 的最小与最大闭比值确实相等。关键工具是 R23 的无常数项收缩多项式强趋恒等；不需要其有界商有统一范数界。进一步，利用局部解析因式分解、亚纯系数上的多项式 gcd 及 Bézout，本条证明所有非零二元收敛解析芽 $F,G$ 的最大比值 $G(A,L)^{-1}F(A,L)$ 都以 $\operatorname{Ran}G(A,L)$ 为图核心，并满足 $T=CT^*C$（含定义域相等）。

依赖：R23 的明确强*近似单位，R24 的复对称性，R60/R62 的非零解析芽算子值单射稠密，R65 的最大/最小图基本框架。本文重新给出全部新的逼近及因式分解步骤。它没有证明每个非零 $H$ 向量循环，也没有解决完整 Hilbert ISP。

## 1. R23 提供的正好是所需的共同图正则化

R23 构造了 $A$ 的多项式 $P_n=p_n(A)$，满足

$$
\|P_n\|\le1,\qquad P_n\longrightarrow I\quad\text{强收敛},
\qquad \operatorname{ord}p_n\longrightarrow\infty. \tag{1.1}
$$

它们还强*收敛，但本条只需要强收敛。因此对任意固定 $m\ge1$，舍去有限项后都能写成

$$
P_n=A^mR_{n,m},\qquad R_{n,m}\in\mathbb C[A]. \tag{1.2}
$$

这里每个 $R_{n,m}$ 都有界，却不要求其范数随 $n$ 一致有界。

### 定理 1.1：任意交换子的最大 $A^m$ 比值有明确图核心

设 $F\in\{A\}'$ 为任意有界算子，$m\ge1$。定义最大闭算子

$$
\operatorname{Dom}T=\{u:Fu\in\operatorname{Ran}A^m\},
\qquad A^mTu=Fu. \tag{1.3}
$$

则

$$
\boxed{\operatorname{Graph}T
=\overline{\{(A^mh,Fh):h\in H\}}.} \tag{1.4}
$$

也就是说，$\operatorname{Ran}A^m$ 是 $T$ 的图核心。

**证明。** $A^m$ 单射保证 (1.3) 是单值算子。其图是有界映射 $(u,v)\mapsto Fu-A^mv$ 的核，所以闭；又它包含 $(A^mh,Fh)$，故定义域稠密。

反向取任意 $(u,v)$ 满足 $Fu=A^mv$。使用 (1.2)，定义实际向量

$$
h_n=R_{n,m}u.
$$

因为 $R_{n,m}$ 是 $A$ 的多项式，和 $F$ 交换，

$$
A^mh_n=P_nu,\qquad
Fh_n=R_{n,m}Fu=R_{n,m}A^mv=P_nv.
$$

由 (1.1)，这两个向量分别趋于 $u,v$，证明最大图包含于右侧闭包。反向包含已由闭性给出。证毕。

特别地，$(P_nu,TP_nu)=(P_nu,P_nTu)$，所以这些正则化在图范数中也是收缩：

$$
\|P_nu\|^2+\|TP_nu\|^2
\le\|u\|^2+\|Tu\|^2,
$$

并按图范数趋于 $u$。分母 $R_{n,m}$ 本身的统一范数界不是这一步的假设。

### 1.1 原临界图的具体逼近

取 $F=L,m=1$。对每个 $Lu=Av$，写 $P_n=AR_{n,1}$，并取

$$
h_n=R_{n,1}u.
$$

于是

$$
(Ah_n,Lh_n)=(P_nu,P_nv)\longrightarrow(u,v). \tag{1.5}
$$

这就是所问实际图的完整逼近，不是条件性等价。交换两个坐标也得到

$$
\overline{\{(Lh,Ah):h\in H\}}
=\{(u,v):Au=Lv\}.
$$

因此 R65 的 $X_{\min}=X_{\max}=A^{-1}L$，以及 $Y_{\min}=Y_{\max}=L^{-1}A$。

### 1.2 为什么 R49 的有界除法障碍不阻止这件事

R49 排除的是一个固定有界算子 $B$ 满足 $LB=A^m$；它没有排除上述逐个有限多项式 $R_{n,m}$。这里并未取 $R_{n,m}$ 的有界极限，也未把强收敛 $A^mR_{n,m}\to I$ 改成范数收敛。

事实上，(1.2) 的分母范数必趋于无穷。若存在一个范数有界子列，则在可分 Hilbert 空间上逐个矩阵元取对角子列，得到某个有界算子 $R$ 及弱算子收敛；从 $A^mR_{n,m}\to I$ 强收敛得 $A^mR=I$。$A^m$ 单射且满射，于是有界可逆，这与其拟幂零性矛盾。因此

$$
\|R_{n,m}\|\longrightarrow\infty.
$$

这与 (1.5) 的两个图坐标同时收敛完全相容。

## 2. 共轭自伴性以及两种不同的中间上同调

令 $C$ 为 R24 的共轭。R24 证明每个有界 $F\in\{A\}'$ 都满足 $F=CF^*C$，且 $A^m=C(A^m)^*C$。

### 推论 2.1

定理 1.1 的最大闭比值满足

$$
\boxed{T=CT^*C.} \tag{2.1}
$$

**证明。** 先在 $\operatorname{Ran}A^m$ 上定义 $T_0(A^mh)=Fh$。由伴随定义，

$$
v\in\operatorname{Dom}T_0^*,\quad T_0^*v=w
\iff F^*v=(A^m)^*w.
$$

共轭后正好为 $F(Cv)=A^m(Cw)$，所以 $CT_0^*C$ 是最大图实现 $T$。而定理 1.1 给 $\overline{T_0}=T$，于是 $T_0^*=T^*$，得到 (2.1)。证毕。

这是关于指定共轭 $C$ 的自伴性，不能换成通常的 $T=T^*$，也不提供通常自伴算子的实谱结论。R65 的 $A^{-1}L$ 和 $L^{-1}A$ 仍具有全平面连续谱。

### 2.1 约化中间上同调为零，但未约化商不为零

对 $(A,L)$ 考虑有界复形

$$
H\xrightarrow{\,D\,}H\oplus H\xrightarrow{\,R\,}H,
\qquad
Dh=(Ah,Lh),\quad R(u,v)=Lu-Av.
$$

$RD=0$，而定理 1.1 已证明

$$
\ker R=\overline{\operatorname{Ran}D}. \tag{2.2}
$$

所以用值域闭包定义的约化中间上同调为零。

但 $\operatorname{Ran}D$ 本身不闭。否则 $D$ 单射（因为 $A$ 单射），闭值域定理给某个 $c>0$，使

$$
\|Ah\|^2+\|Lh\|^2\ge c\|h\|^2.
$$

迭代此不等式，并用 $A,L$ 交换，得到

$$
c^n\|h\|^2
\le\sum_{j=0}^n\binom nj\|A^jL^{n-j}h\|^2.
$$

由两个算子的拟幂零性，对任意 $\epsilon>0$，有固定常数 $C_A,C_L$ 使
$\|A^j\|\le C_A\epsilon^j$、$\|L^j\|\le C_L\epsilon^j$。因此

$$
c^n\le 2^nC_A^2C_L^2\epsilon^{2n},
$$

选择 $2\epsilon^2<c$ 再令 $n\to\infty$ 即矛盾。

于是 $\operatorname{Ran}D\subsetneq\ker R$；未取闭包的代数商 $\ker R/\operatorname{Ran}D$ 非零，其自然商拓扑并不分离点。不能把这个非零代数商误记为 (2.2) 的非零闭图缺陷。

另外得到严格定义域包含

$$
\operatorname{Ran}A\subsetneq\operatorname{Dom}(A^{-1}L)\subsetneq H,
$$

$$
\operatorname{Ran}L\subsetneq\operatorname{Dom}(L^{-1}A)\subsetneq H. \tag{2.3}
$$

左边严格性来自 $D$ 的像不闭及已证图闭包；右边严格性分别由 R36、R49 的真实值域不包含给出。

## 3. 一个双生成理想的图核心引理

设有界 $F,G$ 交换，$G$ 单射且值域稠密；允许 $F$ 暂时不单射。若存在同时与 $F,G$ 交换的有界算子 $U_n,V_n$，使

$$
P_n=FU_n+GV_n\longrightarrow I\quad\text{强收敛},
$$

则

$$
\boxed{
\overline{\{(Gh,Fh):h\in H\}}=\{(u,v):Fu=Gv\}.
} \tag{3.1}
$$

**证明。** 给定 $Fu=Gv$，取 $h_n=U_nv+V_nu$。交换关系直接给

$$
Gh_n=U_nGv+V_nGu=P_nu,
$$

$$
Fh_n=U_nFv+V_nFu=P_nv.
$$

两坐标同时收敛，得到反向包含；正向包含由最大图闭性给出。证毕。

特别地，若某个固定 $N\ge0$ 满足

$$
FU+GV=A^N,\qquad U,V\in\mathcal A,
$$

则用 R23 写 $P_n=A^NR_{n,N}$（$N=0$ 时可直接取 $P_n=I$），在 (3.1) 中取 $U_n=UR_{n,N}$、$V_n=VR_{n,N}$ 即可。

## 4. 二元解析芽的共同因子与清分母 Bézout

记 $\mathscr O=\mathbb C\{z,w\}$，以及一元亚纯芽域 $K=\operatorname{Frac}\mathbb C\{z\}$。

### 引理 4.1

对任意非零 $F,G\in\mathscr O$，存在非零解析芽 $D,F_1,G_1$ 及解析芽 $U_1,V_1$、整数 $N\ge0$，使

$$
F=DF_1,\qquad G=DG_1,\qquad
U_1F_1+V_1G_1=z^N. \tag{4.1}
$$

**证明。** 使用 R62 已自含证明的局部准备分解，写

$$
F=z^\nu U P,\qquad G=z^\mu V Q,
$$

其中 $U,V$ 是解析单位，$P,Q$ 是关于 $w$ 的首一多项式、系数属于 $\mathbb C\{z\}$，且

$$
P(0,w)=w^p,\qquad Q(0,w)=w^q.
$$

次数 $p$ 或 $q$ 可以为零，此时对应多项式为 $1$。

在域 $K$ 上对 $P,Q$ 作通常有限次 Euclidean 算法，取其首一 gcd $D_0\in K[w]$，并写

$$
P=D_0P_1,\qquad Q=D_0Q_1,
$$

$P_1,Q_1$ 也首一且在 $K[w]$ 中互素。

这些多项式实际上全部具有在 $z=0$ 可去的亚纯系数。确实，有限多个系数可在一个穿孔圆盘内同时定义；对每个这样的 $z$，$D_0(z,\cdot)$ 及 $P_1(z,\cdot)$ 的根都是 $P(z,\cdot)$ 的根的子多重集，$Q_1$ 同理。由于 $P(0,w)=w^p$，其全部根随 $z\to0$ 趋于零：对任意充分小固定圆周 $|w|=\rho$，在小 $z$ 下 $P(z,w)$ 与 $w^p$ 的边界差小于 $|w|^p$，辐角原理给全部 $p$ 个根在圆内。$Q$ 同理。

因此 $D_0,P_1,Q_1$ 的首一系数都是一致有界的有限根对称函数；其在 $z=0$ 的亚纯奇点可去。于是这些多项式属于 $\mathbb C\{z\}[w]$，原来的乘法恒等式也延伸到 $z=0$。

令 $b=\min(\nu,\mu)$，取

$$
D=z^bD_0,\qquad
F_1=z^{\nu-b}UP_1,\qquad
G_1=z^{\mu-b}VQ_1.
$$

因为 $P_1,Q_1$ 在 $K[w]$ 中互素，有限 Euclidean 算法还给 $B,C\in K[w]$，使

$$
BP_1+CQ_1=1.
$$

取足够大的整数 $N$，消去 $z^{-(\nu-b)}B$ 与 $z^{-(\mu-b)}C$ 所有系数的极点。由于 $U,V$ 是单位，

$$
U_1=z^{N-(\nu-b)}U^{-1}B,\qquad
V_1=z^{N-(\mu-b)}V^{-1}C
$$

都是二元解析芽。于是 $U_1F_1+V_1G_1=z^N$，证明 (4.1)。证毕。

这段论证只使用单变量域上的有限多项式 Euclidean 算法、根的有界性及可去奇点；没有把形式 gcd 未经证明当作收敛解析芽。

### 4.1 一个后续可用的形式可除性推论

若 $F,G\in\mathscr O$、$G\ne0$，且存在 $Q\in\mathbb C[[z,w]]$ 满足 $F=GQ$，那么 $F/G$ 实际属于 $\mathscr O$。

**证明。** 非零 $F$ 的情形使用 (4.1)；公共非零因子 $D$ 可在形式幂级数整环中取消，所以 $F_1=G_1Q$。从 Bézout 关系得

$$
z^N=G_1(U_1Q+V_1)
\quad\text{于 }\mathbb C[[z,w]].
$$

形式环中 $z^N$ 的任意因子都是 $z^a$ 乘单位。为见这一点，分别从两个因子提取最大的共同 $z$ 幂，剩余因子在 $z=0$ 都不为零；若剩余乘积仍含正的 $z$ 幂，代入 $z=0$ 会与 $\mathbb C[[w]]$ 为整环矛盾。因此两个提出的指数之和正是 $N$，剩余乘积为 $1$。

所以 $G_1=z^aE$，其中 $E$ 在形式环中是单位。$G_1$ 原来收敛，除去有限次 $z$ 后得到的 $E$ 仍收敛，且其常数项非零，故为解析单位。形式等式 $F_1=z^aEQ$ 又说明 $F_1$ 的前 $a$ 个 $z$ 系数恒为零，所以 $F_1/z^a$ 是解析芽。因此

$$
Q=(F_1/z^a)E^{-1}\in\mathscr O.
$$

$F=0$ 时直接取 $Q=0$。证毕。

## 5. 全部解析芽之商的最大图等于最小图

在本节，用 $\widehat F=F(A,L)$ 表示 R62 的范数解析演算。每个非零芽的算子值都单射且值域稠密。

**定理 5.1。** 对任意非零 $F,G\in\mathscr O$，最大闭比值

$$
T_{F/G}=\widehat G^{-1}\widehat F
$$

满足

$$
\boxed{
\operatorname{Graph}T_{F/G}
=\overline{\{(\widehat Gh,\widehat Fh):h\in H\}},
\qquad T_{F/G}=CT_{F/G}^*C.
} \tag{5.1}
$$

**证明。** 先作引理 4.1 的分解。R62 使 $\widehat D$ 单射，所以

$$
\widehat Fu=\widehat Gv
\iff
\widehat F_1u=\widehat G_1v. \tag{5.2}
$$

另一方面 $\widehat D$ 值域稠密，且所有算子交换，因此

$$
\begin{aligned}
\overline{\{(\widehat Gh,\widehat Fh):h\in H\}}
&=\overline{\{(\widehat G_1\widehat Dh,\widehat F_1\widehat Dh):h\in H\}}\\
&=\overline{\{(\widehat G_1h,\widehat F_1h):h\in H\}}.
\end{aligned} \tag{5.3}
$$

解析演算将 (4.1) 变为真实有界恒等式

$$
\widehat U_1\widehat F_1+\widehat V_1\widehat G_1=A^N.
$$

第 3 节的共同图逼近因此证明约去公共因子后的最小图等于最大图。结合 (5.2)–(5.3) 即得 (5.1) 的第一式。

所有这些有界解析算子都满足 R24 的 $C$ 对称性；依第 2 节同一伴随计算，最大图是最小图的共轭伴随。既然二者相等，得到第二式，含定义域相等。证毕。

该证明也给出了具体的逼近程序。对约去公共因子后的图向量 $\widehat F_1u=\widehat G_1v$，取 $P_n=A^NR_{n,N}$，并令

$$
h_n=R_{n,N}(\widehat U_1v+\widehat V_1u).
$$

则 $(\widehat G_1h_n,\widehat F_1h_n)=(P_nu,P_nv)\to(u,v)$。要回到原始未约去因子的核心，对每个 $n$ 利用 $\widehat DH$ 稠密，选择 $x_n$ 使 $\widehat Dx_n$ 足够接近 $h_n$；有界的 $\widehat F_1,\widehat G_1$ 使这一步同时保持两个坐标的误差趋零。没有要求 $\widehat D$ 有有界逆。

## 6. 分式表示的独立性与闭包代数运算

最大比值只依赖于分式 $F/G\in\operatorname{Frac}\mathscr O$，不依赖其表示。若 $FG'=F'G$，且 $\widehat Fu=\widehat Gv$，则

$$
\widehat G(\widehat F'u-\widehat G'v)
=\widehat G'\widehat Fu-\widehat G\widehat G'v=0.
$$

$\widehat G$ 单射给 $\widehat F'u=\widehat G'v$；反向相同。因此两个最大图相等。

这一分式赋值也是单射的。若两个闭比值相等，在共同核心 $\operatorname{Ran}(\widehat G\widehat G')$ 上比较，得到

$$
\widehat F\widehat G'=\widehat F'\widehat G.
$$

R62 的解析芽演算单射性给 $FG'=F'G$。

此外，令 $R_1,R_2$ 为非零分式，使用自然交定义域和乘积定义域，有

$$
\overline{T_{R_1}+T_{R_2}}=T_{R_1+R_2},
\qquad
\overline{T_{R_1}T_{R_2}}=T_{R_1R_2},
\qquad
(T_R)^{-1}=T_{1/R}. \tag{6.1}
$$

若和为零，右边理解为全域零算子。

**证明。** 写 $R_i=F_i/G_i$。在 $\operatorname{Ran}(\widehat G_1\widehat G_2)$ 上，两个原始运算都良定义，并分别等于公共分母 $\widehat G_1\widehat G_2$、分子
$\widehat F_1\widehat G_2+\widehat F_2\widehat G_1$ 和 $\widehat F_1\widehat F_2$ 的核心算子。定理 5.1 说明这些核心的图闭包是右侧最大实现。

反向检查，在自然和或乘积的定义域上，左乘共同有界分母即得到对应分子恒等式，所以原始运算包含在右侧闭算子中。这给前两式的两个包含方向。逆等式由交换图的两个坐标直接得到。证毕。

这里明确使用**取闭包后的**运算，未把两个无界算子的原始和或乘积未经证明称作闭算子，也未省去自然定义域条件。

## 7. 已解决和仍未解决的范围

本条无条件解决了实际 $A,L$ 的最小/最大图缺口，并推广到全部 R62 解析芽之商。它也解释了 R23 强近似单位与 R49 值域不包含之间没有矛盾：前者允许分母范数发散，却给出两个图坐标的同步收敛。

对非恒定分式 $R=F/G$，R62 还说明 $T_R$ 没有特征值，而且每个 $T_R-\lambda$ 的值域都稠密：核对应非零芽 $F-\lambda G$ 的核；值域已经包含其稠密值域，见 R65 的一般框架。

但判定哪些分式的最大实现有界、哪些参数具有有界预解逆，还需要真实系数的新增分析。不能由图核心存在或 $C$-自伴性直接推出这些有界性判断。尤其 $C$-自伴性并不把无界算子谱限制在实轴；R65 已给出全平面连续谱的实际例子。
