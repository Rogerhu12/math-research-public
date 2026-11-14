# R143：任意二阶的正则化gauge跨核与首位核图

日期：2026-11-12（UTC）。独占作者：critical_kernel。完整结果 R143。
状态：以下定义域与跨核定理、固定参数图核心及首位横截性已完整证明。
本稿不假设二阶系数逐行可和，也不假设 gauge 保持原闭乘子的定义域。
它没有证明一般复一阶限制的值域稠密。

## 1. 已建立的实际闭乘子接口

设

$$
f=a_*+\sum_{j\ge0}a_j\chi_j+
\sum_{0\le i<j}b_{ij}\chi_i\chi_j,\qquad
a\in\ell^2,\quad \sum_{i<j}|b_{ij}|^2<\infty.
\tag{1.1}
$$

使用真实算子

$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad V_j1=\chi_j.
$$

R130/R131 给其闭乘子 $X=X_f$，满足：

- $X^*=CXC$，其中 $Cf(y)=\overline{f(-1-y)}$；
- 有限柱空间 $\mathcal P$ 是图核心，有限 chaos 空间也在域内；
- 每个有界 $T\in\{A\}'$ 保持 $\operatorname{Dom}X$，且
  $XT=T X$ 在该域上成立；
- $X1=f$，闭值域就是 $f$ 的闭多项式轨道。

固定 dyadic 根 $\zeta$，其阶为 $N=2^m$，记

$$
U=U_\zeta,\qquad (Uu)(y)=\zeta^{\,y\bmod N}u(y),\qquad
G=\gamma_\zeta(X)=UXU^*.
$$

$U\mathcal P=\mathcal P$，所以 $\mathcal P$ 也是 $G$ 的图核心。
以下始终区分 $\operatorname{Dom}X$ 与
$\operatorname{Dom}G=U\operatorname{Dom}X$。

### 1.1 $G$ 的真实 $C$ 自伴性及全交换子域交换

反射 $y\mapsto-1-y$ 给

$$
CUC=\zeta U,\qquad CU^*C=\zeta^{-1}U^*.
$$

因此

$$
G^*=UX^*U^*=CGC.
\tag{1.2}
$$

这是闭算子及定义域的等式。

若 $T\in\{A\}'$，则 $U^*TU\in\{A\}'$，因为
$U^*AU=\zeta^{-1}A$。利用 $X$ 的域交换后再共轭，得到

$$
T\operatorname{Dom}G\subseteq\operatorname{Dom}G,\qquad
GTu=TG u\quad(u\in\operatorname{Dom}G).
\tag{1.3}
$$

本稿后续正则化算子同时保持这两个闭域，使用的是 (1.3)；
没有先假定 $U\operatorname{Dom}X=\operatorname{Dom}X$。

## 2. 核心上的差只含有限个一阶行算子

对每个 $i<m$，定义尾一阶符号与其 R125 闭乘子

$$
g_i=\sum_{j\ge m}b_{ij}\chi_j,\qquad Z_i=X_{g_i}.
\tag{2.1}
$$

每个固定行属于 $\ell^2$，因此 $Z_i$ 已有完整闭实现；
它可能无界，不要求 $\sum_j|b_{ij}|<\infty$。

记

$$
F_i=\gamma_\zeta(V_i)-V_i \quad(0\le i<m),
$$

以及有限解析头

$$
\begin{aligned}
F_*={}&\sum_{i<m}a_i(\gamma_\zeta(V_i)-V_i)\\
&+\sum_{i<j<m}b_{ij}
\bigl(\gamma_\zeta(V_i)\gamma_\zeta(V_j)-V_iV_j\bigr).
\end{aligned}
\tag{2.2}
$$

所有 $F_i,F_*$ 都是某个在零点邻域解析的标量函数在 $A$ 上的
通常全纯演算。没有把一般 $\mathcal A$ 元素称为解析芽。

因为 $j\ge m$ 时 $\gamma_\zeta(V_j)=V_j$，有限截断恒等式
在有限 chaos 上取真实极限后给

$$
(G-X)u=F_*u+\sum_{i<m}F_i Z_i u
\qquad(u\in\mathcal P).
\tag{2.3}
$$

令右边为 $D_{\zeta,\mathrm{core}}u$。
本稿不预先宣称这个有限和闭，也不把其自然域等同于
$\operatorname{Dom}G\cap\operatorname{Dom}X$。

## 3. 同时正则化所有相关行

对一个复 $\ell^2$ 行，将系数按实、虚部正负部分写成四个
非负 $\ell^2$ 序列。R128 给相应的正一阶闭乘子 $Z_{i,\nu}$
及有界预解式

$$
R_{i,\nu}(t)=(I+tZ_{i,\nu})^{-1}\in\{A\}',\qquad t>0.
$$

零行或零分量取相应因子为 $I$。所有这些因子交换、单射、
范数不超过1，且 $t\downarrow0$ 时强趋 $I$。
令

$$
R_i(t)=\prod_{\nu=1}^4R_{i,\nu}(t),\qquad
R(t)=\prod_{i<m}R_i(t).
\tag{3.1}
$$

若 $m=0$，即 $\zeta=1$，可直接取 $R(t)=I,D=0$；
下文有内容的情形为 $m\ge1$。

R128 的含域恒等式及全交换子域保持给

$$
\operatorname{Ran}R(t)\subseteq\bigcap_{i<m}\operatorname{Dom}Z_i,
\qquad
Z_iR(t)\in\{A\}'\ \text{有界}.
\tag{3.2}
$$

例如 $Z_iR_i(t)$ 是四个预解式的有限有界组合，再乘其他
$R_\ell(t)$ 即得 $Z_iR(t)$。故定义

$$
\boxed{
Q_\zeta(t)=F_*R(t)+\sum_{i<m}F_iZ_iR(t)\in\{A\}'.
}
\tag{3.3}
$$

这是实际有界算子。每个因子均为有界交换子，故
$Q_\zeta(t)$ 对 $B(u,v)=\langle u,Cv\rangle$ 对称，
并保持每个闭 $A$ 不变空间。

对 $u\in\mathcal P$，一阶行的全交换子域交换给

$$
R(t)D_{\zeta,\mathrm{core}}u=Q_\zeta(t)u.
\tag{3.4}
$$

式 (3.4) 是先在行算子的真实定义域上验证的；
不依赖把无界形式差任意搬过 $R(t)$。

### 3.1 参数改变只差一个实际有界单位

对 $s,t>0$，单个正预解式满足

$$
R_{i,\nu}(s)
=R_{i,\nu}(t)
\left[\frac tsI+\left(1-\frac ts\right)R_{i,\nu}(s)\right].
$$

方括号的逆是交换 $s,t$ 后的相应因子，故为有界交换单位。
将有限多个因子相乘得

$$
R(s)=R(t)W(s,t),\qquad W(s,t)\in\{A\}'^\times.
\tag{3.5}
$$

因此对任意闭 $A$ 不变 $L$，

$$
R(s)L=R(t)L.
\tag{3.6}
$$

这里单位及其逆保持 $L$，使用的是 R88 的强多项式闭包。
相同一阶域恒等式还给 $Q_\zeta(s)=Q_\zeta(t)W(s,t)$。

## 4. 正则化后的闭域恒等式

**定理4.1。** 对每个固定 $t>0$，

$$
\boxed{
R(t)\operatorname{Dom}X\subseteq
\operatorname{Dom}X\cap\operatorname{Dom}G,\qquad
G R(t)v=R(t)Xv+Q_\zeta(t)v
\quad(v\in\operatorname{Dom}X).
}
\tag{4.1}
$$

也有反向版本

$$
\boxed{
R(t)\operatorname{Dom}G\subseteq
\operatorname{Dom}X\cap\operatorname{Dom}G,\qquad
X R(t)v=R(t)Gv-Q_\zeta(t)v
\quad(v\in\operatorname{Dom}G).
}
\tag{4.2}
$$

**证明。** 固定 $v\in\operatorname{Dom}X$，取有限柱
$v_n\to v,\ Xv_n\to Xv$。由 (1.3)，
$R(t)v_n\in\operatorname{Dom}G$，且

$$
\begin{aligned}
G R(t)v_n
&=R(t)Gv_n\\
&=R(t)Xv_n+R(t)D_{\zeta,\mathrm{core}}v_n\\
&=R(t)Xv_n+Q_\zeta(t)v_n.
\end{aligned}
\tag{4.3}
$$

第一步使用 $G$ 的真实域交换；第二步使用共同有限柱上的
(2.3)；第三步使用 (3.4)。
由于 $R(t),Q_\zeta(t)$ 有界，右端收敛到
$R(t)Xv+Q_\zeta(t)v$，而 $R(t)v_n\to R(t)v$。
$G$ 闭，故得到 $\operatorname{Dom}G$ 的包含及 (4.1)。
$R(t)v\in\operatorname{Dom}X$ 由 $X$ 自身的域交换得到。

对 $v\in\operatorname{Dom}G$，使用 $G$ 的有限柱图逼近，
在共同核心上将 (4.3) 反向改写为
$XR(t)v_n=R(t)Gv_n-Q_\zeta(t)v_n$，
再用 $X$ 闭性，即得 (4.2)。证毕。

这个定理只把正则化后的向量放入共同域；它没有声称两个原闭域相同。

## 5. 任意核上的合法跨核配对和固定图核心

固定任意 $\lambda\in\mathbb C$，令

$$
M=\ker(X-\lambda I),\qquad
M_\zeta=U_\zeta M=\ker(G-\lambda I).
$$

两者闭且 $A$ 不变。
所有有界交换子保持 $M,M_\zeta$，也由原乘子的域交换直接可见。

由 (4.1)，对 $v\in M$，

$$
R(t)v\in M\cap\operatorname{Dom}G,\qquad
(G-\lambda I)R(t)v=Q_\zeta(t)v.
\tag{5.1}
$$

取 $w_\zeta\in M_\zeta$。式 (5.1) 两侧配对所需的向量都在
$G$ 的真实域内；由 (1.2)，

$$
\boxed{
B(Q_\zeta(t)v,w_\zeta)
=B((G-\lambda I)R(t)v,w_\zeta)
=B(R(t)v,(G-\lambda I)w_\zeta)=0.
}
\tag{5.2}
$$

故

$$
\boxed{B(Q_\zeta(t)M,U_\zeta M)=0.}
\tag{5.3}
$$

这无需 $U_\zeta\operatorname{Dom}X=\operatorname{Dom}X$。

### 5.1 变换后算子在未知核 $M$ 上确为稠密定义的限制

由于 $R(t)\to I$ 强收敛，(5.1) 给
$M\cap\operatorname{Dom}G$ 在 $M$ 中稠密。
而 $G-\lambda I$ 在这个域上的像属于 $M$：
若 $x\in M\cap\operatorname{Dom}G$，则

$$
R(s)x\to x,\qquad
(G-\lambda I)R(s)x=R(s)(G-\lambda I)x
\to(G-\lambda I)x.
$$

左边又由 (5.1) 等于 $Q_\zeta(s)x\in M$；
$M$ 闭即得结论。因此

$$
G_{\zeta,M}:=(G-\lambda I)|_{\operatorname{Dom}G\cap M}
:\operatorname{Dom}G\cap M\longrightarrow M
$$

是闭、稠密定义的限制算子。

更强地，对**任意固定 $t>0$**，

$$
\boxed{
R(t)M\ \text{是 }G_{\zeta,M}\text{ 的图核心},\qquad
\overline{\operatorname{Ran}G_{\zeta,M}}
=\overline{Q_\zeta(t)M}.
}
\tag{5.4}
$$

证明：上面的 $R(s)x$ 是图逼近，而 (3.6) 说明其全部属于同一个
集合 $R(t)M$。取图核心的像并闭包即得第二式。
它同时说明 (5.3) 右侧的闭像不依赖正则化参数。

### 5.2 与现有 Fourier 排核机制的准确接口

若某个具体二阶类另外证明，对有限 dyadic 子群之外所有 $\zeta$，

$$
\overline{Q_\zeta(t)M}=M,
\tag{5.5}
$$

则 (5.3) 推出 $B(M,U_\zeta M)=0$，R122 的有限 Fourier 支撑、
全本质支撑和逐柱秩论证即可排除非零 $M$。

本稿没有证明一般 (5.5)。
即便 $Q_\zeta(t)$ 在整个 $H$ 上单射稠密，也不能把其全空间
稠密值域直接搬到任意指定的 $M$。

## 6. 首位 gauge 给任意二阶核的严格横截性

现在取 $\zeta=-1$。只改变第0位 $V_0$，所有 $V_j,j>0$
都被固定。令

$$
g=a_0+\sum_{j>0}b_{0j}\chi_j,\qquad Z=X_g.
\tag{6.1}
$$

这是一个实际闭一阶乘子。直接算 Cayley 因子得

$$
\gamma_{-1}(V_0)-V_0
=\frac{4N_0}{I-N_0^2}
=:F(A).
\tag{6.2}
$$

$F(A)=A\,U_0(A)$，其中 $U_0$ 是真解析单位。
核心差精确为

$$
D_{-1,\mathrm{core}}=F(A)Z.
\tag{6.3}
$$

为 $Z$ 取 R128 的四正分量共同正则化 $R(t)$。
则

$$
Q_{-1}(t)=F(A)Z R(t).
\tag{6.4}
$$

若 $g\ne0$，R125 给 $Z$ 单射；$R(t)$ 单射且
其值域在 $\operatorname{Dom}Z$ 内；$F(A)$ 单射。
因此 $Q_{-1}(t)$ 是实际有界单射交换子，且由 $C$ 对称性值域稠密。

**推论6.1。** 若 $g\ne0$，则对任意 $\lambda\in\mathbb C$，

$$
\boxed{
\ker(X-\lambda I)\cap U_{-1}\ker(X-\lambda I)=\{0\}.
}
\tag{6.5}
$$

**证明。** 若 $v$ 同时属于两核，$R(t)$ 保持两核。
由 (5.1) 得 $Q_{-1}(t)v=0$；其单射性给 $v=0$。证毕。

同理，若符号不依赖低于 $k$ 的全部位，而第 $k$ 行

$$
a_k+\sum_{j>k}b_{kj}\chi_j
$$

非零，令 $h=2^k$，取 $\zeta$ 阶为 $2h$、$\zeta^h=-1$，
即可把 $N_0$ 换成 $N_k$，得到相同的横截结论。
这使用该结构性独立假设，不由较低行和消失推出。

(6.5) 比一般“尚未控制核”多给了一个严格约束，
但两个闭无限维子空间交为零并不意味着其中之一为零。

## 7. 横截性迫使假想核成为一个真实闭图

仍假设 (6.1) 的 $g\ne0$，且暂设
$M=\ker(X-\lambda I)\ne0$。

按最低物理位分解

$$
H=\mathbb C^2\otimes\widehat H
=\widehat H\oplus\widehat H,\qquad
U_{-1}=\begin{pmatrix}I&0\\0&-I\end{pmatrix}.
$$

若 $(x,0)\in M$ 或 $(0,y)\in M$，它也属于 $U_{-1}M$，
所以 (6.5) 迫该向量为零。
因此两个坐标投影在 $M$ 上都单射。

记 $D_0=P_0M,D_1=P_1M$，令 $K_i=\overline{D_i}\subseteq\widehat H$。
存在唯一闭、单射的图算子

$$
T:D_0\subseteq K_0\longrightarrow K_1,\qquad
M=\{(x,Tx):x\in D_0\},\quad \operatorname{Ran}T=D_1.
\tag{7.1}
$$

闭性直接来自 $M$ 在 $H$ 中闭。

真实最低位矩阵为

$$
A=\begin{pmatrix}0&B\\ \alpha_0 I&0\end{pmatrix},
\qquad
(Bu)(z)=\alpha_{1+v_2(z)}u(z-1).
\tag{7.2}
$$

其中 $B$ 是尾权移；特别 $A^2=\alpha_0 I_2\otimes B$。
所以 $K_0,K_1$ 都为 $B$ 不变空间。
由 $AM\subseteq M$ 得

$$
\alpha_0D_0\subseteq D_1,\qquad BD_1\subseteq D_0.
\tag{7.3}
$$

每个 $B$ 不变闭空间上的 $B$ 值域稠密：
归一化的高阶 $B^{2^\ell}$ 正是尾上的高位 $N_j$，
弱趋 $I/2$，且每个都属于 $B$ 乘一个保持该空间的多项式；
闭线性值域闭包的弱闭性给结论。
故 (7.3) 闭包后有

$$
K_0\subseteq K_1,\qquad
K_1=\overline{BK_1}\subseteq K_0.
$$

于是 $K_0=K_1=:K$，(7.1) 实际上是

$$
\boxed{
T:\operatorname{Dom}T\subseteq K\longrightarrow K
\text{ 闭、单射、稠密定义且值域稠密}.
}
\tag{7.4}
$$

同一个 $A$ 不变性还给真正的域条件和图方程

$$
\boxed{
BTx\in\operatorname{Dom}T,\qquad
TBTx=\alpha_0x\qquad(x\in\operatorname{Dom}T).
}
\tag{7.5}
$$

$A^2M\subseteq M$ 给

$$
B\operatorname{Dom}T\subseteq\operatorname{Dom}T,\qquad
TBx=BTx\quad(x\in\operatorname{Dom}T).
\tag{7.6}
$$

特别 $\operatorname{Dom}T\subseteq\operatorname{Ran}T$，且

$$
T^{-1}x=\alpha_0^{-1}BTx
\qquad(x\in\operatorname{Dom}T).
\tag{7.7}
$$

(7.5) 不能直接写成 $T^2=\alpha_0B^{-1}$ 的全域等式：
$Tx$ 不一定属于 $\operatorname{Dom}T$，而 $B^{-1}$ 也未必全域。
本稿保留所有域条件，没有用形式半阶根制造矛盾。

## 8. 当前缺口

本稿完成两件实际工作：

1. 对全部平方可和二阶符号，给无同域假设的共同正则化跨核公式
   (5.3)，并精确识别变换后算子在原核上的固定图核心 (5.4)；
2. 只要最低位一阶行非零，给两个 gauge 核的零交 (6.5)，
   以及任何假想非零核必须满足的闭图与真实尾根条件 (7.4)—(7.7)。

剩余关键仍是一般 $\overline{Q_\zeta(t)M}=M$。
对于首位差，这就是相关复一阶限制的稠密像问题，经 R140 的固定
正则化得到同一准确接口。全空间第一阶循环性、全空间的谱分类或
两个核的横截性都不自动给该稠密结论。

尤其，本稿没有证明一般纯 Boolean 二次
$\sum_{i<j}b_{ij}Y_iY_j$ 单射；
也没有把 R139 的有限解析头子类扩大成任意无限临界行。

## 后续完整附录

[有界二阶Schur核等价、最大闭商及抽象平方障碍](R143-appendix-bounded-quadratic-head-determinant.md)。该附录保留所有实际定义域条件，不将未排除的核写成零。
