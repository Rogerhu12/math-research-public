# R157：首次伴随变形的反循环角色与实际分母支撑三次界

日期：2026-11-12；会话：serre-uniformity-astra-resume2；负责：cm_denominators。

**状态：已证明。** 本文处理 R19 的实际非 CM 曲线及其完整原始整数族，不把局部可解参数或抽象 Selmer 类当作实际曲线。沿用
$$
A:y^2=x^3-x,\qquad E[p]\simeq A[p],\qquad p>37,
$$
$$
g=\gcd_{q\mid Z}v_q(Z),\qquad M=pg,\qquad
n=v_p(M),\qquad K=\mathbb Q(i),\qquad
\eta=\chi_{-4}.
$$
由 R19、R128，
$$
p\equiv3\pmod4,\qquad |Z|>1,\qquad (M,Z)=1,\qquad
E[p^n]\simeq A[p^n],
\tag{157.1}
$$
且 $E,A$ 在 $p$ 好约化，$E$ 在每个 $q\mid Z$ 为乘法约化，并有
$$
v_q(\Delta_{\min}(E))=p\,v_q(Z).
\tag{157.2}
$$
定义实际的最小 $p$ 进 Tate 指数支撑
$$
\mathcal Q_{\min}
=\{q\mid Z:v_p(p\,v_q(Z))=n\},
\qquad
R=\prod_{q\in\mathcal Q_{\min}}q.
\tag{157.3}
$$
这不是任意挑选的素数集合。最大公约数的定义保证它非空。

## 1. 完整结论

**定理 157.1。** 在上述实际情形中：

1. 首次偏离 CM 的伴随变形产生一个非零连续角色
   $$
   \kappa:G_K\longrightarrow\mathbb F_p,
   \qquad
   \kappa(c\sigma c^{-1})=-\kappa(\sigma),
   \tag{157.4}
   $$
   其中 $c$ 为复共轭。其有限导子**准确**为
   $$
   \mathfrak f(\kappa)=R\mathcal O_K.
   \tag{157.5}
   $$
   特别它在 $p$、$2$ 及所有较高 $p$ 进 Tate 指数的分母素数处不分歧，在每个 $q\in\mathcal Q_{\min}$ 的全部 $K$ 上方素理想处均非平凡地、温和地分歧。
2. 对每个非零高斯整数 $\alpha$，若
   $$
   N_{K/\mathbb Q}(\alpha)<p^2/16,
   \tag{157.6}
   $$
   则 $(\alpha,Z)=1$，且其主理想在 $\kappa$ 对应的循环 $p$ 次扩张中 Artin 值为零。
3. 置
   $$
   H=\left\lfloor\frac{p-1}{6}\right\rfloor,\qquad
   C_R=\prod_{q\mid R}(q-\eta(q)).
   $$
   则有明确的必要条件
   $$
   \boxed{C_R\ge
   4p\sum_{j=1}^{H}\varphi(j).}
   \tag{157.7}
   $$
   特别，
   $$
   \boxed{R>\frac{p^3}{50},\qquad
   \operatorname{rad}|Z|>\frac{p^3}{50}.}
   \tag{157.8}
   $$
4. 由 R19 的精确分母，
   $$
   h(j(E))>
   M(3\log p-\log50).
   \tag{157.9}
   $$

这里 $\eta(q)=1$ 表示 $q$ 在 $K$ 分裂，$\eta(q)=-1$ 表示惰性，与 $E$ 在 $q$ 的分裂或非分裂乘法符号不同。定理同时覆盖两种乘法符号，以及 R19 的三个原始整数族。

这是实际分母支撑的必要下界，不是其统一上界。允许 $R$ 随 $p$ 增长时，本文没有产生矛盾，也没有完成 O6。它与 R152 的精确整余核缺陷使用同一个最大同余深度 $n$，但这里额外提取了真实全局类域角色。

## 2. 给定有限层同构与好超奇异整 Tate 模

先完整处理后文排除 $p$ 处分歧所需的局部接口。

### 2.1 两个初等整格事实

设 $T$ 为秩二 $\mathbb Z_p$ 表示，$T/pT$ 绝对不可约。则：
$$
\operatorname{End}_{G}(T/p^rT)=\mathbb Z/p^r
\quad(r\ge1),
\tag{157.10}
$$
并且 $T\otimes\mathbb Q_p$ 中全部 $G$ 稳定格互相位似。

第一条在 $r=1$ 是绝对不可约的 Schur 引理。若矩阵 $B$ 模 $p^r$ 交换所有作用矩阵，先减去其模 $p$ 的标量，写成 $pB_1$；$B_1$ 模 $p^{r-1}$ 仍交换全部作用矩阵，逐级归纳即可。自同构恰为其中的标量单位。

对第二条，将另一格缩放到 $T'\subseteq T$ 且 $T'\nsubseteq pT$。其模 $p$ 像是非零不变子空间，故为全部 $T/pT$。于是 $T'+pT=T$；对有限生成的 $T/T'$ 用 Nakayama 引理即得 $T'=T$。

### 2.2 好超奇异曲线在 $\mathbb Q_p$ 上的有理局部唯一性

$A$ 在 $p\equiv3\pmod4$ 好超奇异。$E$ 在 $p$ 好约化；若它普通，其模 $p$ 惯性半单化有第一层字符，而 $A[p]$ 有互异的第二层基本字符，不能满足 (157.1)。故 $E$ 也好超奇异。因 $p\ge5$，两者的 $a_p$ 都等于零。

以下使用反变晶体函子
$$
D^*_{\mathrm{cris}}(V)
=\operatorname{Hom}_{\mathbb Q_p[G_{\mathbb Q_p}]}
(V,B_{\mathrm{cris}}),
$$
即先把协变 Tate 空间取对偶，再使用通常晶体函子的规范。这与 Volkov [V] §1.2 的规范一致，避免把协变 $D_{\mathrm{cris}}(V_pE)$ 的倒数 Frobenius 多项式误写成 $X^2+p$。

对好超奇异椭圆曲线，该二维对象满足
$$
\phi^2=-p,\qquad
\dim_{\mathbb Q_p}\operatorname{Fil}^1D=1,
\qquad N=0.
\tag{157.11}
$$
$X^2+p$ 在 $\mathbb Q_p$ 不可约。任取 $\operatorname{Fil}^1D$ 中非零的 $v$，向量 $v,\phi v$ 就构成基。对两个这样的对象，分别选 $v,w$，映射
$$
v\longmapsto w,\qquad
\phi v\longmapsto\phi w
$$
交换 $\phi$，并保持全部过滤。晶体函子的全忠实性给出
$$
V_p(E)|_{G_{\mathbb Q_p}}
\simeq V_p(A)|_{G_{\mathbb Q_p}}.
\tag{157.12}
$$
这正是 [V] §2.2.1 的唯一对象 $D_c^*(1;0)$；Prop. 2.7 给出相应分类。上面的基计算也直接解释了这里为何没有另一个过滤参数。

模 $p$ 的好超奇异表示在 $\overline{\mathbb F}_p$ 上，惯性有 $\omega_2,\omega_2^p$ 两条不同本征线，而算术 Frobenius 交换这两条线。因此局部表示绝对不可约。应用 §2.1 的稳定格事实，将 (157.12) 缩放，得到整同构
$$
T_p(E)|_{G_{\mathbb Q_p}}
\simeq T_p(A)|_{G_{\mathbb Q_p}}.
\tag{157.13}
$$

### 2.3 精确对齐已给的模 $p^n$ 同构

固定 (157.1) 中一个**全局**同构 $f_n$。任取 (157.13) 的整局部同构 $h$，则
$$
(h\bmod p^n)\circ f_n^{-1}
$$
是 $A[p^n]$ 的局部自同构。由 (157.10)，它是某个标量单位。将该单位提升至 $\mathbb Z_p^\times$ 并缩放 $h$，可使
$$h\bmod p^n=f_n|_{G_{\mathbb Q_p}}.\tag{157.14}$$

这一步不只证明两个局部有理表示同构。它保证该同构可以与已固定的全局有限层标架准确一致，是首次差异类在 $p$ 处成为 coboundary 的必要接口。

## 3. 首次伴随差异及其一维投影

通过提升 $f_n$ 选择两边整基，使
$$\rho_E\equiv\rho_A\pmod{p^n}.$$
定义
$$
c_E(\sigma)=
\frac{\rho_E(\sigma)\rho_A(\sigma)^{-1}-I}{p^n}\pmod p.
\tag{157.15}
$$
由于 $n\ge1$，有 $2n\ge n+1$；相乘后的一阶公式证明 $c_E$ 是
$$c_E\in Z^1(G_{\mathbb Q},\operatorname{ad}^0 A[p]).$$
两边行列式都是 $p$ 进分圆角色，因此 (157.15) 的迹为零。

选取 $T_p(A)$ 的整基，使实际 CM 自同态 $[i]$ 的矩阵为
$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$
这样的基存在：任一模 $p$ 非零的 $v$ 与 $iv$ 模 $p$ 线性独立，因为 $T^2+1$ 不可约，故在整层构成基。对任意 $\sigma\in G_{\mathbb Q}$，
$$
\rho_A(\sigma)J\rho_A(\sigma)^{-1}=\eta(\sigma)J.
\tag{157.16}
$$
因此
$$
\operatorname{ad}^0 A[p]
=\mathbb F_pJ\oplus
\{D:\operatorname{tr}D=\operatorname{tr}(JD)=0\},
$$
第一项为 $\mathbb F_p(\eta)$。其明确的等变投影为
$$
\operatorname{pr}_{J}(D)
=-\tfrac12\operatorname{tr}(JD).
\tag{157.17}
$$
置
$$x_E=\operatorname{pr}_{J}(c_E)\in Z^1(G_{\mathbb Q},\mathbb F_p(\eta)).$$
在 $G_K$ 上系数作用平凡，故
$$\kappa=x_E|_{G_K}:G_K\longrightarrow(\mathbb F_p,+)$$
为群同态。对复共轭应用 cocycle 公式立即得到 (157.4)。

改变提升的整基只使 $c_E$ 加一个伴随 coboundary；其投影限制到 $G_K$ 后为零。不同全局有限层同构也只差标量单位：全局绝对不可约已由 R128 §1 的二进 $Q_8$ 惯性证明，再应用 (157.10)。因此固定 $[i]$ 后，上述 $\kappa$ 不依赖这些标架提升。改用 $[-i]$ 会把它反号，不改变导子、核或下界。

## 4. 导子准确等于最小 Tate 指数支撑

### 4.1 $p$ 处

使用 §2.3 与全局标架对齐的局部整同构。其矩阵为 $I+p^nB$。交织等式给出
$$
c_E(\sigma)=
\overline\rho_A(\sigma)\,\overline B\,
\overline\rho_A(\sigma)^{-1}-\overline B,
\qquad \sigma\in G_{\mathbb Q_p}.
\tag{157.18}
$$
所以它在 $p$ 处是 coboundary。在 $G_{K_p}$ 上，(157.17) 的一维系数作用平凡，故
$$\kappa|_{G_{K_p}}=0.\tag{157.19}$$
这里 $p$ 在 $K$ 惰性；$K_p/\mathbb Q_p$ 是未分歧二次扩张。

### 4.2 $2$ 处及其余好素数

R128 §1 已证明 $E,A$ 在二处具有同一个有限惯性商 $Q_8$ 和同一个惯性核。因 $p>37$，该群阶可逆，有限群平均给
$$H^1(Q_8,\operatorname{ad}^0 A[p])=0.$$
因而 $c_E|_{I_2}$ 为 coboundary；投影并限制到 $I_2\cap G_K$ 后为零。故 $\kappa$ 在 $K$ 的二进素理想处不分歧。

在 $q\nmid2pZ$ 处，两个 $p$ 进表示都不分歧，故 $c_E$、$\kappa$ 也不分歧。

### 4.3 分母素数

设 $q\mid Z$。由 $(p,Z)=1$，$q\ne p$；$A$ 在 $q$ 好约化。对 $E$ 的分裂 Tate 表示，惯性作用为
$$
\begin{pmatrix}
1&p\,v_q(Z)t_p\\0&1
\end{pmatrix}.
\tag{157.20}
$$
非分裂乘法只多一个未分歧二次角色，故在惯性上仍是 (157.20)。温和参数 $t_p:I_q\to\mathbb Z_p$ 可取值一。

若 $v_p(p\,v_q(Z))>n$，则 (157.15) 在 $I_q$ 上为零。

若 $v_p(p\,v_q(Z))=n$，取 $t_p(\tau)=1$。此时
$$
D=c_E(\tau)\in\operatorname{ad}^0 A[p]
$$
是非零秩一 nilpotent 矩阵：它是 (157.20) 的首个非零项，经一个整可逆基变换所得。写
$$
D=\begin{pmatrix}a&b\\c&-a\end{pmatrix}.
$$
若其一维投影为零，则由 (157.17) 有 $c=b$。而 $\det D=0$ 给
$$a^2+b^2=0.$$
$-1$ 在 $\mathbb F_p$ 非平方，所以 $a=b=c=0$，与 $D\ne0$ 矛盾。因此
$$\kappa(\tau)\ne0.\tag{157.21}$$

奇素数处 $K/\mathbb Q$ 不分歧，故所用 $I_q$ 包含于相应 $G_K$。若 $q$ 在 $K$ 分裂，反循环性使两个上方素理想的惯性角色互为负，均非零；若惰性，则只有一个上方素理想。所有这些非零角色的阶为 $p\ne q$，所以温和且导子指数准确为一。

这证明 (157.5)，同时证明 $\kappa$ 非零、像准确为整个加法群 $\mathbb F_p$。

## 5. 小高斯整数全部落在角色核中

R132 给出对全部实际 $q\mid Z$ 的条件
$$
\begin{cases}
q\ge4M-1,&q\equiv3\pmod4,\\
q\ge4M^2+1,&q\equiv1\pmod4.
\end{cases}
\tag{157.22}
$$
现在设 $0<N(\alpha)<p^2/16$。

若分裂的 $q\mid Z$ 除 $(\alpha)$，则 $q\le N(\alpha)$，与第二条矛盾。若惰性的 $q\mid Z$ 除 $(\alpha)$，写 $\alpha=a+bi$，则 $q\mid a,b$，从而 $N(\alpha)\ge q^2\ge(4p-1)^2$，同样矛盾。因此
$$(\alpha,Z)=1.\tag{157.23}$$

将 $(\alpha)$ 分解为高斯素理想。对二进素理想及惰性有理素数给出的素理想，它们被复共轭固定；$\kappa$ 不分歧于这些因子，反循环性及 $p$ 为奇数迫其 Artin 值等于零。

只需处理分裂有理素数 $t\equiv1\pmod4$ 上的素理想 $\mathfrak t$。它满足
$$t\le N(\alpha)<p^2/16,$$
并且 $t\nmid2pZ$。在 $G_K$ 中取其算术 Frobenius。$A$ 的实际 Frobenius 是
$$
\pi_{\mathfrak t}=a+bi\in\mathbb Z[i],
\qquad a^2+b^2=t,\qquad b\ne0.
\tag{157.24}
$$
两个 Frobenius 迹模 $p$ 同余，而 Hasse 界给
$$
|a_t(E)-a_t(A)|\le4\sqrt t<p.
$$
故它们作为整数准确相等。

利用完整模 $p^{n+1}$ 的首次差异公式，(157.15) 给
$$
0\equiv
\operatorname{tr}\bigl(c_E(\operatorname{Frob}_{\mathfrak t})
(aI+bJ)\bigr)
=-2b\,\kappa(\operatorname{Frob}_{\mathfrak t})
\pmod p.
\tag{157.25}
$$
更明确地，这来自
$$
\rho_E(\sigma)\equiv
(I+p^n c_E(\sigma))\rho_A(\sigma)\pmod{p^{n+1}},
$$
先对两边取迹、减去相等的整数迹、再除 $p^n$。
由 $0<|b|\le\sqrt t<p/4$，$b$ 模 $p$ 非零。因此 $\kappa(\operatorname{Frob}_{\mathfrak t})=0$。共轭素理想也为零。

对 $(\alpha)$ 的全部素理想因子相加即得定理第 2 项。这里对一个随 $p$ 明确增长的范围证明了全称命题，没有根据有限次点数实验外推。

## 6. 真实射线类商及单位因子

高斯整环为 Euclidean 整环，故类数一。由 (157.5) 及类域论，$\kappa$ 给出模 $R\mathcal O_K$ 的射线角色
$$
\theta:(\mathcal O_K/R\mathcal O_K)^\times
\longrightarrow\mathbb F_p.
$$
它杀掉全局单位 $\{\pm1,\pm i\}$。反循环性还使它杀掉
$(\mathbb Z/R)^\times$：每个有理单位剩余类可由与 $R$ 互素的有理整数表示，其共轭不变，而角色在共轭下反号。

首先除去有理单位剩余类，得到
$$
T_R=
\frac{(\mathcal O_K/R\mathcal O_K)^\times}
{(\mathbb Z/R)^\times},
\qquad
|T_R|=\prod_{q\mid R}(q-\eta(q))=C_R.
\tag{157.26}
$$
局部计算如下：

- $q$ 惰性时，商为 $\mathbb F_{q^2}^\times/\mathbb F_q^\times$，阶 $q+1$。
- $q$ 分裂时，商为 $(\mathbb F_q^\times\times\mathbb F_q^\times)/\operatorname{diag}\mathbb F_q^\times$，阶 $q-1$。

$[i]$ 在 $T_R$ 中准确有阶二。它的平方是已除去的 $-1$，而在任何奇素数分量中，$i$ 均不是有理对角标量。因此实际反循环射线商是
$$
U_R=T_R/\langle[i]\rangle,\qquad
|U_R|=C_R/2.
\tag{157.27}
$$
诱导的 $\theta:U_R\to\mathbb F_p$ 非零，故
$$|\ker\theta|=\frac{C_R}{2p}.\tag{157.28}$$

下一节始终在这个已除去 $\pm i$ 的群中计数，保留式 (157.27) 的因子二。

## 7. 半开扇区中的原始向量注入

对正整数 $L$ 定义
$$
\mathcal S_L=
\{a+bi:1\le a\le L,\ -a<b\le a,\ \gcd(a,b)=1\}.
\tag{157.29}
$$
它是一个半开 $90^\circ$ 扇区。$a=1$ 时准确保留 $1$、$1+i$；负对角端点 $1-i$ 被排除。对 $a\ge2$，正、负的合法 $b$ 各有 $\varphi(a)$ 个。因此
$$|\mathcal S_L|=2\sum_{j=1}^{L}\varphi(j).\tag{157.30}$$

若 $L\le H$，则全部 $\alpha\in\mathcal S_L$ 满足
$$N(\alpha)\le2L^2\le2H^2<p^2/16.$$
由第 5 节，它们都定义了 $\ker\theta$ 中的元素。

**引理 157.2。** 若 $L\le H$ 且 $R>2L^2$，则 $\mathcal S_L\to U_R$ 单射。

**证明。** 写 $\alpha=a+bi$、$\beta=c+di$。若两者在 $U_R$ 中同类，则有两种可能：模 $R$，$\alpha$ 是 $\beta$ 的有理标量倍，或是 $i\beta$ 的有理标量倍。中国剩余定理允许该标量在各素数分量取不同单位值，但乘 $i$ 的选择是同一个全局选择。

第一种情形给
$$R\mid ad-bc.$$
因 $|ad-bc|\le2L^2<R$，有 $ad-bc=0$。两个向量原始，且实部为正，因此 $\alpha=\beta$。

第二种情形给
$$R\mid ac+bd.$$
同样有 $ac+bd=0$。但 $a,c>0$、$|b|\le a$、$|d|\le c$；若点积为零，必须 $|b|=a$、$|d|=c$ 且 $b,d$ 异号。其中一个必在被排除的负对角端点，矛盾。故第二种情形不发生。证毕。

这里同时检查了 determinant 与 dot product 的碰撞，没有把只除 $\pm1$ 的计数误用于已除 $\pm i$ 的射线类群。

## 8. 无渐近输入的 totient 下界及注入阈值

### 8.1 一个自含的统一计数界

对每个正整数 $L$，
$$\sum_{j=1}^{L}\varphi(j)>\frac{L^2}{4}.\tag{157.31}$$
证明如下。$[1,L]^2$ 中不互素的正整数对被某个共同素因子 $r$ 覆盖，故其数量至多
$$L^2\sum_{r\ {\rm prime}}r^{-2}.$$
而
$$
\sum_{r\ {\rm prime}}\frac1{r^2}
\le\frac14+\sum_{\substack{m\ge3\\m\ {\rm odd}}}\frac1{m^2}
<\frac14+
\sum_{\substack{m\ge3\\m\ {\rm odd}}}\frac1{m^2-1}
=\frac12.
$$
最后一项是望远镜和。因而互素对多于 $L^2/2$。互素对的准确数目是 $2\sum_{j\le L}\varphi(j)-1$，即得 (157.31)。

### 8.2 先证明 $R>2H^2$

不能预先假定注入所需的模数阈值。若 $R\le2H^2$，由 (157.22) 可知：

- $R$ 不可能有两个或以上素因子，因为那样 $R\ge(4p-1)^2>2H^2$。
- 单个素因子也不可能在 $K$ 分裂，因为那样 $R\ge4p^2+1>2H^2$。

因此只能是 $R=q$，其中 $q$ 惰性且 $q\ge4p-1\ge171$。置
$$L=\left\lfloor\sqrt{\frac{q-1}{2}}\right\rfloor.$$
此时 $1\le L\le H$、$q>2L^2$，故引理 157.2 已适用于这个较小扇区。结合 (157.28)、(157.30)、(157.31)，得到
$$
\frac{q+1}{2p}\ge2\sum_{j\le L}\varphi(j)>\frac{L^2}{2}.
$$
另一方面，对实数 $x\ge1$ 有 $\lfloor x\rfloor\ge x/2$，所以
$$L^2\ge\frac{q-1}{8}.$$
于是
$$
p<8\frac{q+1}{q-1}
\le8\frac{172}{170}<9,
$$
与 $p\ge43$ 矛盾。这证明
$$R>2H^2.\tag{157.32}$$

现在可把引理 157.2 应用于完整 $\mathcal S_H$。由
$$
\frac{C_R}{2p}=|\ker\theta|
\ge|\mathcal S_H|
=2\sum_{j\le H}\varphi(j)
$$
准确得到 (157.7)。

## 9. 三次支撑界与精确适用范围

由于 $p\ge43$，
$$
H=\left\lfloor\frac{p-1}{6}\right\rfloor
\ge\frac{p-6}{6}\ge\frac p7.
$$
所以 (157.7)、(157.31) 给
$$C_R>pH^2\ge\frac{p^3}{49}.\tag{157.33}$$

若 $\omega(R)\ge3$，则 (157.22) 直接给
$$R\ge(4p-1)^3>p^3/50.$$
若 $\omega(R)\le2$，则
$$
\frac{C_R}{R}
=\prod_{q\mid R}\left(1-\frac{\eta(q)}q\right)
\le\left(1+\frac1{4p-1}\right)^2
\le\left(\frac{172}{171}\right)^2.
$$
因此
$$
R>\frac{p^3}{49}\left(\frac{171}{172}\right)^2
>\frac{p^3}{50}.
$$
这证明 (157.8)。最后，
$$
h(j(E))\ge p\log|Z|
\ge pg\log\operatorname{rad}|Z|
\ge M\log R
>M(3\log p-\log50),
$$
即 (157.9)。

例如 $p=43$ 时，$H=7$、$\sum_{j\le7}\varphi(j)=18$，准确界是 $C_R\ge3096$。若最小 Tate 指数支撑只有一个在 $K$ 惰性的素数 $q$，则须 $q+1\ge3096$。此前用于构造抽象 Kummer 类或辅助导数的素数 $859,1031$ 并未被宣称是这样的单一实际分母支撑，故两类结论没有冲突。

本文真正新增的是：一个由实际曲线首次整变形规范地产生、导子精确可控的反循环 $p$ 角色，以及它强制的大量小主理想完全分裂。对多个素数，这个角色不是可逐素数任意指定的局部数据；它必须同时满足整个射线类核条件。

本文未推出 $R$、$Z$、$p$ 的绝对上界，未将一次伴随角色换成实际 Mordell–Weil 点，也未断言它自动提供完整 Euler 系统或比 R149 更高的中心值整除。

## 来源与可追踪接口

- [R19：固定 CM 同余的反向 Fermat 判据](R19-converse-fermat-fixed-cm.md)：实际曲线、三族完整覆盖、精确分母及乘法 Tate 指数。
- [R128：全部奇数同余深度](R128-all-odd-congruence-depth-and-split-prime-power-exclusion.md)，§§1、4、5：二处同一个 $Q_8$ 惯性、$(M,Z)=1$、实际 $E[p^n]\simeq A[p^n]$。
- [R132：完整最大同余层的支持素数界](R132-maximal-congruence-level-and-split-multiplicative-prime-bound.md)：(157.22) 与真实高斯 Frobenius。
- [R152：最大 CM 深度与精确 unipotent 缺陷](R152-maximal-cm-depth-and-the-exact-unipotent-defect.md)：同一个最小 Tate 指数在真实惯性上达到；本篇一维投影的非零性另在 §4.3 完整证明。
- **[V]** Maja Volkov, *Les représentations $\ell$-adiques associées aux courbes elliptiques sur $\mathbb Q_p$*, J. reine angew. Math. **535** (2001), 65–101, DOI [10.1515/crll.2001.046](https://doi.org/10.1515/crll.2001.046)。[作者原稿](https://arxiv.org/pdf/math/0007208)，§1.2（原稿 pp.6–7）的反变晶体函子；§2.2.1（p.13）的 $D_c^*(1;0)$；§2.2.4 Proposition 2.7（p.14）的分类。这里只调用已发表的局部晶体接口；整格、有限层精确对齐及全部后续类域与计数步骤均已展开。

