# R135：加性gauge解析芽的全部闭商与图核心

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。完整结果 R135。

状态：完整证明。本文把 R129 的忠实解析演算及全部非零解析芽的单射稠密像结论，与 R23 的强近似单位结合，得到该二元解析芽域的完整闭商演算。关键图逼近是 R66 已证明的机制；这里重新写出固定 $z$ 坐标的解析 gcd、清分母 Bézout、所有图域和伴随步骤，以明确本次覆盖的新的 $X$ 类。

本文不声称闭商有界当且仅当标量分式全纯。R129 的 $w/z$ 例子正好否定这个必要条件。

## 1. 假设与结论

固定本题实际 $A$、$H=L^2(\mathbb Z_2,\mu)$、

$$
\mathcal A=\overline{\mathbb C[I,A]},
\qquad (Cu)(y)=\overline{u(-1-y)}.
$$

取 $X\in\mathcal A$，规范化 $\chi(X)=0$，并假定每个 dyadic 单位根 $\zeta$ 都满足

$$
\gamma_\zeta(X)=X+D_\zeta(A),
\qquad D_\zeta\in\mathbb C\{z\},\quad D_\zeta(0)=0.
\tag{1.1}
$$

再假定 $X$ 不是 $A$ 的一元收敛解析芽。由 R129，记

$$
\mathscr O=\mathbb C\{z,w\},\qquad
\widehat F=F(A,X),
$$

则：

- $F\mapsto\widehat F$ 是忠实的范数收敛解析演算；
- 每个非零 $F\in\mathscr O$ 的 $\widehat F$ 都单射且值域稠密；
- $\widehat F\in\mathcal A$，且 $\widehat F^*=C\widehat FC$；
- 解析单位求值后是有界单位。

一般未规范化的 $X$，先把第二变量从 $(0,\chi(X))$ 平移到原点。全文的芽都在这个指定点附近定义。

对分式 $r=P/Q\in\operatorname{Frac}\mathscr O$，$Q\ne0$，定义最大实现

$$
\operatorname{Dom}T_r
=\{u\in H:\widehat Pu\in\operatorname{Ran}\widehat Q\},
\qquad \widehat Q T_ru=\widehat Pu.
\tag{1.2}
$$

**主定理。** 上述定义单值、闭且稠密定义，只依赖分式 $r$。它满足

$$
\boxed{
\operatorname{Graph}T_r
=\overline{\{(\widehat Qh,\widehat Ph):h\in H\}},
\qquad T_r=CT_r^*C.
}
\tag{1.3}
$$

更小的准确图核心是

$$
\widehat Q\,\mathbb C[A]1,
\tag{1.4}
$$

也可把参数空间 $\mathbb C[A]1$ 换成全部有限柱向量。这里不能擅自删去前面的 $\widehat Q$。

分式赋值是忠实的，并满足以图闭包解释的加法、乘法与实际逆：

$$
\overline{T_r+T_s}=T_{r+s},\qquad
\overline{T_rT_s}=T_{rs},\qquad
(T_r)^{-1}=T_{1/r}\quad(r\ne0).
\tag{1.5}
$$

若 $r$ 非恒定，则每个 $\lambda\in\mathbb C$ 都有

$$
\boxed{\ker(T_r-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(T_r-\lambda I)}=H.}
\tag{1.6}
$$

因此其谱中没有点谱或剩余谱；每点只可能属于预解集或连续谱。本文没有把这改成“谱必为空”或“谱必为整个复平面”。

## 2. 固定 $z$ 坐标的解析 gcd 与 Bézout

本节纯粹讨论收敛解析芽，不改变 $A$ 所对应的变量 $z$。

### 2.1 准备分解及唯一性

每个非零 $F\in\mathscr O$ 可写成

$$
F=z^\nu U P,
\tag{2.1}
$$

其中 $\nu\ge0$，$U$ 是解析单位，$P\in\mathbb C\{z\}[w]$ 为首一 distinguished 多项式：

$$
P(z,w)=w^p+\sum_{j<p}p_j(z)w^j,
\qquad P(0,w)=w^p.
$$

允许 $p=0$，此时 $P=1$。先提取最大的共同 $z$ 次幂，使余芽在 $z=0$ 时不恒零；R129 §3 的残数与 Newton 构造给余下的准备分解。

本稿还用到它的唯一性。固定一个足够小的 $w$ 圆周，使两个候选单位均不为零，且两个首一多项式的全部根都在圆内。对足够小的 $z$，余芽的零点多重集同时等于两个首一多项式的根多重集；二者次数相同，所以多项式相同，随后单位也相同。共同 $z$ 次幂的唯一性来自对 $z$ 的阶。

### 2.2 首一亚纯因子的系数实际收敛

令 $K=\operatorname{Frac}\mathbb C\{z\}$。若 $P$ 是上述首一 distinguished 多项式，而 $D,E\in K[w]$ 首一且 $P=DE$，则 $D,E$ 的系数都属于 $\mathbb C\{z\}$，并且它们在 $z=0$ 时分别为相应次数的 $w$ 次幂。

证明只需可去奇点。有限多个亚纯系数可在一个小的穿孔圆盘上同时定义。对其中每个 $z$，$D(z,\cdot)$、$E(z,\cdot)$ 的根都是 $P(z,\cdot)$ 根的子多重集。由 $P(0,w)=w^p$ 及圆周上的 Rouché 估计，$P$ 的全部根随 $z\to0$ 一致趋于零。各因子的系数是有限根的基本对称函数，所以在穿孔邻域有界且趋于零；亚纯奇点可去。

### 2.3 完整 gcd 与固定 $z$ 的消去恒等式

**引理 2.1。** 对任意非零 $P,Q\in\mathscr O$，存在解析芽 $G,P_1,Q_1,a,b$ 及整数 $m\ge0$，满足

$$
P=GP_1,\qquad Q=GQ_1,\qquad
\boxed{aP_1+bQ_1=z^m.}
\tag{2.2}
$$

其中 $G$ 是 $P,Q$ 的解析最大公因子（相差一个解析单位的意义下），$P_1,Q_1$ 互素。

**证明。** 为避免与原始芽混淆，将准备多项式记为 $P_0,Q_0$：

$$
P=z^\nu U P_0,\qquad
Q=z^\mu V Q_0.
$$

在域 $K$ 上作有限 Euclidean 算法，取首一 gcd $G_0$，并写

$$
P_0=G_0P_0',\qquad Q_0=G_0Q_0'.
$$

§2.2 说明 $G_0,P_0',Q_0'$ 都是收敛系数的首一 distinguished 多项式。置

$$
c=\min(\nu,\mu),\qquad
G=z^cG_0,
$$

$$
P_1=z^{\nu-c}UP_0',\qquad
Q_1=z^{\mu-c}VQ_0'.
\tag{2.3}
$$

这确实是解析 gcd。若 $H$ 同时解析整除 $P,Q$，先写 $H=z^\ell W H_0$ 的准备式。其 $z$ 阶满足 $\ell\le c$。分别准备两个解析商，利用 §2.1 的唯一性，得首一 $H_0$ 在 $K[w]$ 中同时整除 $P_0,Q_0$，所以整除 $G_0$。商 $G_0/H_0$ 再由 §2.2 具有收敛系数。因此

$$
G/H=z^{c-\ell}W^{-1}(G_0/H_0)\in\mathscr O.
$$

所以每个共同解析因子都整除 $G$；同理 $P_1,Q_1$ 无共同非单位解析因子。

因为 $P_0',Q_0'$ 在 $K[w]$ 中互素，有限 Euclidean 算法给 $B,D\in K[w]$，使

$$
BP_0'+DQ_0'=1.
\tag{2.4}
$$

这只涉及有限多个一元亚纯系数。选择足够大的整数 $m$，消去
$z^{-(\nu-c)}B$ 与 $z^{-(\mu-c)}D$ 的全部极点。于是

$$
a=z^{m-(\nu-c)}U^{-1}B,\qquad
b=z^{m-(\mu-c)}V^{-1}D
$$

均属于 $\mathscr O$，且 (2.4) 乘以 $z^m$ 正好给 (2.2)。证毕。

这里 $z$ 因子已经由 $c=\min(\nu,\mu)$ 明确处理。剩余的单位可依赖两个变量，不影响清除有限个一元亚纯极点。故无需作一般线性坐标变换，也无需把一个新的线性坐标算子误当成原来的 $A$。

特别地，若 $P,Q$ 本来互素，则其生成的解析理想含有某个 $z^m$。这是比“共同零点孤立”更直接的、适合本题固定坐标的结论。

## 3. 强近似单位与双生成图逼近

R23 给出多项式 $E_n=e_n(A)$，满足

$$
\|E_n\|\le1,\qquad E_n\to I\text{ 强收敛},
\qquad\operatorname{ord}e_n\to\infty.
\tag{3.1}
$$

因此对任意固定 $m$，舍去有限项后可以写成

$$
E_n=A^m r_{n,m}(A),\qquad r_{n,m}\in\mathbb C[z].
\tag{3.2}
$$

只要求每个 $r_{n,m}(A)$ 有界，不要求其范数一致有界。若 $m=0$，也可以直接使用恒等算子。

**图逼近引理。** 设有界算子 $p,q,a,b$ 两两交换，$q$ 单射稠密，且

$$
ap+bq=A^m.
\tag{3.3}
$$

它们也与 $A$ 交换。则

$$
\boxed{\{(x,y):px=qy\}
=\overline{\{(qh,ph):h\in H\}}.}
\tag{3.4}
$$

**证明。** 右边包含于左边，因为 $pq=qp$，而左边是有界映射 $(x,y)\mapsto px-qy$ 的闭核。反向给定 $px=qy$，取

$$
h_n=r_{n,m}(A)(bx+ay).
\tag{3.5}
$$

则

$$
qh_n=r_{n,m}(A)(bqx+aqy)
=r_{n,m}(A)(bqx+apx)=E_nx,
$$

同样直接计算

$$
ph_n=r_{n,m}(A)(bpx+apy)
=r_{n,m}(A)(bq+ap)y=E_ny.
$$

于是 $(qh_n,ph_n)=(E_nx,E_ny)\to(x,y)$。证毕。

这些两个图坐标同时收敛，而且

$$
\|E_nx\|^2+\|E_ny\|^2\le\|x\|^2+\|y\|^2.
$$

逼近并未取 $r_{n,m}(A)$ 的有界极限，故不会与既有的有界除法障碍冲突。

## 4. 最大图、共同因子与更小图核心

先设 $P,Q$ 都非零。由 $\widehat Q$ 单射，(1.2) 是单值算子，其图为

$$
\{(u,v):\widehat Pu=\widehat Qv\},
\tag{4.1}
$$

因而闭。又 $\widehat P,\widehat Q$ 交换，所以每个 $h$ 给一个图向量
$(\widehat Qh,\widehat Ph)$；其定义域包含稠密的 $\operatorname{Ran}\widehat Q$。

应用引理 2.1。由于 $\widehat G$ 单射，

$$
\widehat Pu=\widehat Qv
\iff\widehat P_1u=\widehat Q_1v.
\tag{4.2}
$$

由于 $\widehat G$ 值域稠密且有界乘子交换，

$$
\begin{aligned}
\overline{\{(\widehat Qh,\widehat Ph):h\in H\}}
&=\overline{\{(\widehat Q_1\widehat Gh,\widehat P_1\widehat Gh):h\in H\}}\\
&=\overline{\{(\widehat Q_1h,\widehat P_1h):h\in H\}}.
\end{aligned}
\tag{4.3}
$$

将 Bézout 恒等式求值得

$$
\widehat a\widehat P_1+\widehat b\widehat Q_1=A^m.
$$

§3 的引理用于这四个有界算子，结合 (4.2)—(4.3)，证明 (1.3) 的图闭包等式。

这也给原始分母的明确逼近。先按 (3.5) 构造 $h_n$，使

$$
(\widehat Q_1h_n,\widehat P_1h_n)\to(u,v).
$$

再用 $\widehat GH$ 稠密，选 $k_n$ 使

$$
\|\widehat Gk_n-h_n\|
\le\frac{1}{n(1+\|\widehat P_1\|+\|\widehat Q_1\|)}.
$$

于是 $(\widehat Qk_n,\widehat Pk_n)\to(u,v)$。这一步只用稠密像，不要求 $\widehat G^{-1}$ 有界。

若 $P=0$，则 (4.1) 为所有 $(u,0)$，所以 $T_0$ 是全域零算子；因 $\widehat Q$ 稠密，图核心结论同样成立。若 $P=cQ$，由 $\widehat Q$ 单射直接得 $T_{P/Q}=cI$。

### 4.1 多项式轨道及有限柱参数图核心

$1$ 对 $A$ 循环，故 $\mathbb C[A]1$ 在 $H$ 中稠密。映射

$$
h\longmapsto(\widehat Qh,\widehat Ph)
$$

是从 $H$ 到 $H\oplus H$ 的有界映射。因此

$$
\boxed{
\operatorname{Graph}T_r
=\overline{\{(\widehat Qp(A)1,\widehat Pp(A)1):p\in\mathbb C[z]\}}.
}
\tag{4.4}
$$

这说明 $\mathbb C[A]\widehat Q1$ 是图核心。其生成向量 $\widehat Q1$ 本身循环，因为 $\widehat Q$ 稠密像并与 $A$ 交换。

全部有限柱向量也在 $H$ 中稠密，故以它们代替 (4.4) 的参数 $p(A)1$ 得到另一图核心。准确域子空间是“$\widehat Q$ 作用于有限柱”，而非未经证明地把所有有限柱都放进 $\operatorname{Dom}T_r$。

这个区别真实存在：$r=1/z$ 给 $T_r=A^{-1}$、$\operatorname{Dom}T_r=\operatorname{Ran}A$。若 $Au=1$，则 $u(y-1)=1/w(y)$；本题权重满足

$$
\int w(y)^{-2}\,d\mu(y)
=\sum_{j\ge0}2^{-j-1}\alpha_j^{-2}=\infty,
$$

所以常向量 $1$ 并不属于这个定义域。

## 5. 共轭自伴性：含完整定义域的伴随计算

在 $\operatorname{Ran}\widehat Q$ 上先定义核心算子

$$
T^{(0)}(\widehat Qh)=\widehat Ph.
$$

因 $\widehat Q$ 单射，这是良定义的；因其像稠密，$T^{(0)}$ 稠密定义。通常伴随的定义给

$$
v\in\operatorname{Dom}(T^{(0)})^*,\quad
(T^{(0)})^*v=w
\iff\widehat P^*v=\widehat Q^*w.
\tag{5.1}
$$

所有等式采用内积对第一变量线性的约定。用
$\widehat P^*=C\widehat PC$、$\widehat Q^*=C\widehat QC$ 共轭 (5.1)，右边成为

$$
\widehat P(Cv)=\widehat Q(Cw).
$$

所以

$$
C(T^{(0)})^*C=T_r
\tag{5.2}
$$

是最大图及其定义域的相等。§4 已证明 $\overline{T^{(0)}}=T_r$，因此
$(T^{(0)})^*=T_r^*$，最终得到

$$
\boxed{T_r=CT_r^*C.}
\tag{5.3}
$$

它是相对于反线性共轭 $C$ 的自伴性，不等同于通常自伴，也不导出实谱。

### 5.1 与全部有界交换子的域交换

若 $B\in\{A\}'$，则 $B$ 与 $\widehat P,\widehat Q$ 交换，因为二者属于 $\mathcal A$。对 $u\in\operatorname{Dom}T_r$，

$$
\widehat PBu=B\widehat Pu=B\widehat Q T_ru
=\widehat Q BT_ru.
$$

所以

$$
B\operatorname{Dom}T_r\subseteq\operatorname{Dom}T_r,
\qquad T_rBu=BT_ru.
\tag{5.4}
$$

本式只陈述全空间闭算子的域交换，没有由此声称它在每个闭 $A$-不变空间上的定义域或值域都稠密。

## 6. 忠实的分式演算与闭包代数运算

### 6.1 与表示无关且忠实

若 $PQ'=P'Q$，给定 $\widehat Pu=\widehat Qv$，有

$$
\widehat Q(\widehat P'u-\widehat Q'v)
=\widehat Q'\widehat Pu-\widehat Q\widehat Q'v=0.
$$

$\widehat Q$ 单射给 $\widehat P'u=\widehat Q'v$。反向同理，所以最大图只依赖分式。

反之，若两个最大算子相同，在共同域向量 $\widehat Q\widehat Q'h$ 上比较其像，得到

$$
\widehat P\widehat Q'h=\widehat P'\widehat Qh\quad(h\in H).
$$

R129 的解析演算忠实性遂给 $PQ'=P'Q$。因此分式赋值也是忠实的。

### 6.2 和、积和逆的所有域包含

写 $r=P/Q$、$s=F/G$。自然和的定义域是两域之交，乘积的定义域是

$$
\{u\in\operatorname{Dom}T_s:T_su\in\operatorname{Dom}T_r\}.
$$

它们都包含稠密的 $\operatorname{Ran}(\widehat Q\widehat G)$。在该共同核心上分别有

$$
(T_r+T_s)(\widehat Q\widehat Gh)
=(\widehat P\widehat G+\widehat F\widehat Q)h,
$$

$$
T_rT_s(\widehat Q\widehat Gh)=\widehat P\widehat Fh.
\tag{6.1}
$$

§4 说明这些核心图的闭包分别是 $T_{r+s}$、$T_{rs}$。

另一方面，在自然和的域上，写 $y=T_ru$、$v=T_su$；乘以共同有界分母得到

$$
\widehat Q\widehat G(y+v)
=(\widehat P\widehat G+\widehat F\widehat Q)u.
$$

在自然乘积域上，写 $v=T_su$、$y=T_rv$，则

$$
\widehat Q\widehat Gy
=\widehat P\widehat Gv=\widehat P\widehat Fu.
$$

所以两个原始运算分别包含在对应的最大闭图中。结合共同核心的反向包含，证明

$$
\boxed{\overline{T_r+T_s}=T_{r+s},\qquad
\overline{T_rT_s}=T_{rs}.}
\tag{6.2}
$$

若结果分式为零，右边是全域零算子，前述稠密核心仍给相同结论。式 (6.2) 没有声称未经闭包的两个乘积域相同。

若 $r\ne0$，$\widehat P$ 也单射稠密。直接由图交换两坐标，得到

$$
\boxed{(T_r)^{-1}=T_{1/r}.}
\tag{6.3}
$$

逆的定义域是 $\operatorname{Ran}T_r$，下节说明它稠密；闭性也由图坐标交换保留。

## 7. 点谱、稠密值域与精确有界除法判据

若 $r\ne0$，由 $\widehat P$ 单射可知 $T_r$ 单射。又

$$
T_r(\widehat Qh)=\widehat Ph,
$$

故其值域包含稠密的 $\operatorname{Ran}\widehat P$。

对任意 $\lambda$，有准确的闭算子等式

$$
T_r-\lambda I=T_{(P-\lambda Q)/Q}.
\tag{7.1}
$$

因为 $\widehat Pu\in\operatorname{Ran}\widehat Q$ 当且仅当
$(\widehat P-\lambda\widehat Q)u\in\operatorname{Ran}\widehat Q$，两者域完全相同。

若 $r$ 非恒定，$P-\lambda Q$ 对每个 $\lambda$ 都是非零解析芽，故 R129 保证它的求值单射稠密。上段用于 (7.1) 即给 (1.6)。因此 $T_r-\lambda$ 若不满射，就是单射稠密像而非满射的连续谱情形；若满射，其逆因闭图定理有界，故 $\lambda$ 在预解集。

**准确判据。** 对任意非恒定 $r=P/Q$，

$$
\boxed{
\lambda\in\rho(T_r)
\iff\exists B\in B(H):
(\widehat P-\lambda\widehat Q)B=\widehat Q.
}
\tag{7.2}
$$

成立时 $B=(T_r-\lambda I)^{-1}$，且自动属于 $\{A\}'$。

证明可直接由 (6.3) 及 (7.1) 读出，也可检查：右侧使每个 $Bx$ 满足
$\widehat P Bx=\widehat Q(x+\lambda Bx)$，所以 $(T_r-\lambda)Bx=x$；对 $u\in\operatorname{Dom}T_r$，左乘单射 $\widehat P-\lambda\widehat Q$ 得
$B(T_r-\lambda)u=u$。此外，将右侧恒等式分别右乘及左乘 $A$，单射性给 $BA=AB$。

同理，不论 $r$ 是否恒定，

$$
\boxed{
T_r\text{ 有界}
\iff\exists B\in B(H):\widehat QB=\widehat P.
}
\tag{7.3}
$$

若一个稠密定义闭算子在其定义域上有统一通常范数界，则它的定义域由闭性成为闭集，因而为全 $H$；因此 (7.3) 的“有界”没有遗漏一个仅在真稠密域上有界的闭实现。右侧成立时最大图显然就是 $B$ 的全域图，且 $B\in\{A\}'$。

这些是实际有界算子除法判据，没有把右侧替换成标量芽的全纯可除性。

### 7.1 非零闭商在其定义域内保持并反映循环性

若 $r\ne0$ 且 $u\in\operatorname{Dom}T_r$，则

$$
\boxed{u\text{ 循环}\iff T_ru\text{ 循环}.}
\tag{7.4}
$$

先设 $u$ 循环。$\widehat P$ 是有界、稠密像的交换子，所以
$\widehat Pu$ 也循环。令 $M=\operatorname{cyc}_A(T_ru)$。因
$\widehat Q\in\mathcal A$ 保持 $M$，

$$
\widehat Pu=\widehat Q T_ru\in M.
$$

故 $M=H$。反向对非零分式 $1/r$ 和向量 $T_ru\in\operatorname{Dom}T_{1/r}$ 使用同一论证即可。本步是 R132 的有界正则化机制在分子、分母均已知单射稠密时的直接形式，不要求任何闭商本身有界。

## 8. 已知边界与两个不同的谱现象

若分式 $r$ 本身属于 $\mathscr O$，则 $T_r=r(A,X)$ 有界，这是充分条件。

必要性不成立。R129 §9 的具体元素

$$
X=\sum_{j\ge0}a_jY_j,
\qquad a_j=2^{-j}\alpha_j^2,
$$

满足本文假设，且有

$$
Z=\sum_{j\ge0}a_j\frac{A^{2^j-1}}{d_j}(I+N_j)^{-1}\in\mathcal A,
\qquad AZ=X.
\tag{8.1}
$$

范数收敛由
$\|A^{2^j-1}(I+N_j)^{-1}/d_j\|\le3/\alpha_j$
和 $\sum_j2^{-j}\alpha_j<\infty$ 给出。$X$ 的非一元解析性由有限 gauge 差在半径趋零处的不可去极点证明。因此二元解析及本文分式演算都忠实，但非全纯分式 $w/z$ 的最大实现是有界的 $Z$。

与此相反，$r=1/z$ 的实现是无界 $A^{-1}$。它的预解集却是全平面，因为

$$
(A^{-1}-\lambda I)^{-1}=A(I-\lambda A)^{-1}
\quad(\lambda\in\mathbb C),
$$

而 $A$ 拟幂零使 $I-\lambda A$ 始终有界可逆。因此非恒定分式的结论 (1.6) 不能加强成“必有连续谱”，更不能强加之前某个特定临界比值的全平面谱结论。

本文的完整结论是：这一新的忠实解析芽域有规范的闭商、明确的最小与最大图相等、$C$ 自伴性、忠实闭包运算，以及所有非恒定商的零点谱和稠密像。全部有界商的标量分类与实际 $A$ 的一般不变子空间问题仍未由这些事实解决。

依赖文件：

- [R129：加性 gauge 混合解析芽](../notes/2026-11-12-additive-gauge-mixed-analytic-germs-0c-agent.md)。
- [R66：强近似单位与解析商图核心](../notes/2026-11-12-closed-graph-cores-and-analytic-ratios-0c-agent.md)。
- R23 的无常数项收缩多项式强近似单位、R88 的交换子与 $C$ 对称结构。
