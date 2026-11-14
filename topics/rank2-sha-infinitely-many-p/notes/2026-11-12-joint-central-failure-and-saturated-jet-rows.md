# 两类中央全失败的有限行与真正饱和 jet 预算

日期：2026-11-12。状态：本文的有限行、局部格指数、共同输出规范不变性、
首带合流比较及尾部素数预算均已证明。没有得到所需的统一 arithmeticity
改进，也没有据此证明无穷多个素数的初级有限性。

本文回到 O8 的具体未付条件。始终区别以下三个对象：

- R44/R47 的固定中央图像 $F(Z)=\sum e_mZ^m$；
- R57 的固定整数流 $h_m=A_{17}^{(m)}(0)$；
- R62 的固定 Euler 图像 $Y(w)=4\mathscr H(z)/f_0(z)$，$w=z^4$。

它们有已证的真实比较，但其普通 Taylor 截面格不是同一个格。
下文不把其中一个的单列整除免费移到另一个的全部多项式列。

## 1. 反设确实给出的完整中央条件

若主目标在固定 $E_{17}$ 上失败，即只有有限个 $p$ 的
$\Sha[p^\infty]$ 有限，则固定有限集合之外有：

$$
J_{A,p}'(0)=0\qquad\text{ordinary 和 inert 两类均成立。}
\tag{1.1}
$$

普通情形使用 R40/R60 的充要判据；惰性情形只需 R50/R54 的充分判据
取逆否命题。没有在惰性处补用未经证明的反向。

(1.1) 是全部精度证书失败，不是仅说首权非单位。特别地，惰性 R77 给

$$
J_{A,p}(u)\in p^2u^2\mathbb Z_p\langle u\rangle,
\tag{1.2}
$$

普通的单位自参考商则满足

$$
\mathscr Q_p(T)=J_{A,p}(T)/J_{A^{(4)},p}(T)
 \in T^2\mathbb Z_p[[T]].
\tag{1.3}
$$

这些是后面采用的真实条件。

## 2. 两种完整 Newton 行

### 2.1 普通素数

令 $d=p-1$，$b=\bar\pi$，$a=\pi/b$，$c=b^{-1}$。用 R63 的完整
Euler 因子定义实际值

$$
V_j=\frac{1-ca^{dj}}{1-ca^{dj+4}}\frac{h_{dj}}{h_{dj+4}}
 =\mathscr Q_p((1+p)^{dj}-1),\qquad V_0=0.
\tag{2.1}
$$

$h_{dj+4}$ 和两个 Euler 因子均为 $p$ 单位。令
$\mathcal F_p(u)=\mathscr Q_p((1+p)^{du}-1)$。有界测度的有限差分给

$$
\mathcal F_p(u)=\sum_{h\ge1}a_h(u)_{\underline h},\qquad
v_p(a_h)\ge h-v_p(h!).
\tag{2.2}
$$

这里 $(u)_{\underline h}=u(u-1)\cdots(u-h+1)$。对 $H\ge1$，定义

$$
L^{\rm o}_{p,H}
 =\sum_{j=1}^H\frac{(-1)^{j+1}}j\binom HjV_j,
\qquad
M^{\rm o}_{p,H}=\min_{r>H}(r-v_p(r)).
\tag{2.3}
$$

准确尾界为

$$
v_p\left(L^{\rm o}_{p,H}
 -(p-1)\log_p(1+p)\mathscr Q_p'(0)\right)
 \ge M^{\rm o}_{p,H}.
\tag{2.4}
$$

证明是 R60 的 Newton 导数公式；其中有限双和可以准确收成 (2.3)，
因为
$\sum_{r=j}^H\binom rj/r=\binom Hj/j$。因此 (1.1) 强迫
$L^{\rm o}_{p,H}\in p^{M^{\rm o}_{p,H}}\mathbb Z_p$。

若 $H\le p-2$，则 $M^{\rm o}_{p,H}=H+1$，且可以删掉 (2.1) 的
Euler 比值，仍得到

$$
\boxed{\quad
\sum_{j=1}^H\frac{(-1)^{j+1}}j\binom Hj
 \frac{h_{(p-1)j}}{h_{(p-1)j+4}}
 \in p^{H+1}\mathbb Z_p.
\quad}
\tag{2.5}
$$

确实，Euler 比值减一的赋值至少为 $dj$，而原比值至少有一层 $p$；
当前 $j$ 和 $H$ 的分母均为单位。一般 $H$ 仍应保留 (2.1)，或按
R60 选择足够大的固定步长，不能无条件删除高精度 Euler 误差。

### 2.2 惰性素数

现在 $d=p+1$，$\alpha=17c$，$v_p(\alpha)=-1$。在 R54 的 $E_1$
规范中，$A_1(z)=\sum\beta_mz^m=e^{\alpha z^d}G(z)$，置

$$
\lambda_p(h)=\left\lceil\frac{h(p-1)+4}{2p}\right\rceil,
\qquad
a_h=\alpha^{-h}[z^{dh}]G,
\qquad v_p(a_h)\ge\lambda_p(h).
\tag{2.6}
$$

实际整数点值为

$$
V_j=J_{A,p}(j)=j!\alpha^{-j}\beta_{dj}.
\tag{2.7}
$$

定义同一个有限 Newton 行

$$
L^{\rm i}_{p,H}
 =\sum_{j=1}^H\frac{(-1)^{j+1}}j\binom HjV_j,
\qquad
M^{\rm i}_{p,H}=\lambda_p(H+1)+v_p(H!).
\tag{2.8}
$$

由于 $\lambda_p(h)+v_p((h-1)!)$ 不减，R54 的完整尾界准确给

$$
v_p(L^{\rm i}_{p,H}-J_{A,p}'(0))\ge M^{\rm i}_{p,H}.
\tag{2.9}
$$

因此惰性全失败同样给一个实际有限行的整除。其系数只使用固定
$\beta_{dj}$、准确有理数 $c$ 及显示出的阶乘，没有未知周期。

为核对这真是原 jet 的行，而非另选测度，直接展开可得

$$
a_h=\sum_{j=1}^h
 \frac{(-1)^{h-j}\alpha^{-j}}{(h-j)!}\beta_{dj}
 =\frac1{h!}\sum_{j=0}^h(-1)^{h-j}\binom hjV_j.
\tag{2.10}
$$

所以 (2.8) 是固定 theta 系数前缀上的明确线性泛函。

## 3. 一个中央线性条件所增加的准确格指数

这里精确量化“额外整性”，并标清采用的格。
取前 $H$ 个下降阶乘系数的 Gauss 包络

$$
\Lambda_{p,H}^{\rm o}
 =\bigoplus_{h=1}^H p^{h-v_p(h!)}\mathbb Z_p,
\qquad
\Lambda_{p,H}^{\rm i}
 =\bigoplus_{h=1}^H p^{\lambda_p(h)}\mathbb Z_p.
\tag{3.1}
$$

在两种格上都使用
$L_H(a)=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_h$。两者的像都是
$p\mathbb Z_p$，因为首坐标的权恰为一，其他坐标不会有更小赋值。
允许尾部只受相应 Gauss 界约束时，它能提供的导数值理想准确为
$p^{M_{p,H}}\mathbb Z_p$：最小赋值在相应最小项达到，且单独取该项
即可实现这个理想。因此前缀可以延成导数零的 Gauss 级数，当且仅当

$$
L_H(a)\in p^{M_{p,H}}\mathbb Z_p.
$$

于是有准确指数

$$
\boxed{\quad
[\Lambda_{p,H}:\Lambda_{p,H}\cap
 L_H^{-1}(p^{M_{p,H}}\mathbb Z_p)]
 =p^{M_{p,H}-1}.
\quad}
\tag{3.2}
$$

本式对实际系数给必要的局部条件。反向的“可延成”只针对所显示的
Gauss 包络，不宣称任意延拓仍来自原固定整数 ODE、原 Iwasawa 测度
或另一条允许的全局 theta 截面。

还可求出两类联合的累计量。令
$H_p(K)=\lfloor(K-4)/(p-\chi_{-4}(p))\rfloor$，只计 $H_p(K)\ge1$
及固定有限坏集之外的素数。这里 $K$ 是 $h_m=A_{17}^{(m)}(0)$ 的
**自然 $z$ 阶上限**；预留的四阶用于相邻参考 $h_{m+4}$，不是
$w=z^4$ 中的阶。则

$$
\boxed{\quad
\sum_p(M_{p,H_p(K)}-1)\log p
 =\frac34 K\log K+O(K).
\quad}
\tag{3.3}
$$

证明只用 R44 已使用的固定模四 Mertens 估计。普通处

$$
H-\log_p(H+1)\le M^{\rm o}_{p,H}-1\le H,
$$

而惰性处

$$
M^{\rm i}_{p,H}-1=\tfrac12H+O(1+H/p).
$$

普通误差的加权和为 $O(K)$：把 $p\le\sqrt K$ 与其余素数分开，
前者至多 $O(\sqrt K\log K)$，后者用
$\log(1+K/p)\le K/p$ 及该半区间素数倒数和有界。
惰性误差由 $\sum_{p\le K}\log p=O(K)$ 及
$\sum_p\log p/p^2<\infty$ 控制。主项分别为
$\tfrac12K\log K$ 和 $\tfrac14K\log K$。

若改以 $w=z^4$ 的 jet 阶 $k_w$ 计数，必须代入 $K=4k_w$；
(3.3) 的主项随即变为 $3k_w\log k_w$，而不是
$\tfrac34k_w\log k_w$。第4–6节的 $k$ 则专指中央图像的
$Z$ 阶，其索引是原中央权 $m$；第7节重新使用 $w$ 时记阶为 $k_w$。
这些重标度不改变精确格指数，但会改变写出的渐近常数。

**(3.3) 不是 jet 的 arithmeticity 常数。** 它是一个线性中央条件
在两个明确系数包络中增加的总指数。还没有把这些包络识别为
$\mathcal O(D)$ 的饱和截面格，也没有把半因子的线性行当作平方中央
系数 $e_m$、更没有当作 $F^b$ 的同一行。

### 3.1 只看逐项整除的全球增益很小

对 $m>0$，普通情形 $p-1\mid m$ 时，(1.3) 给
$v_p(h_m)\ge2+2v_p(m)$，而仅已知中心零给 $1+v_p(m)$。
惰性写 $m=(p+1)k$，(1.2) 则给

$$
v_p(h_m)\ge B_p(k)+2+2v_p(k),\qquad
B_p(k)=v_p(m!)-k-v_p(k!)
 =v_p(k!)+v_p\binom{(p+1)k}{k}\ge0.
\tag{3.4}
$$

相对于已证的一阶中心下界，两类新增的逐项因子都是
$p^{1+v_p(m)}$。令这些因子的乘积为 $C_m$，则

$$
\log C_m\le2\tau(m)\log(m+1)+\log m=m^{o(1)}.
\tag{3.5}
$$

因为 $p-\chi_{-4}(p)$ 必为 $m$ 的约数，每个约数至多对应其两侧的
两个素数，而第二部分只涉及 $p\mid m$。
所以只把全失败降成单个 $h_m$ 的附加整除，不会给出降低
$m\log m$ 量级 Gevrey 系数的估计。完整 Newton 行之间的关系比这个
逐项影子更强，不能因 (3.5) 就丢弃它们。

## 4. R44/R47 真正需要的饱和矩阵

固定 $F(Z)=\sum e_mZ^m$，令
$N_D=\binom{D+2}{2}$，列为 $Z^aY^b$，$a+b\le D$。记

$$
r_j=([Z^j]Z^aF^b)_{a+b\le D},\quad
V_{D,k}=\ker_{\mathbb Q}(r_0,\ldots,r_{k-1}),\quad
L_{D,k,p}=V_{D,k}\otimes\mathbb Q_p\cap\mathbb Z_p^{N_D}.
\tag{4.1}
$$

若第 $k$ 行增加秩，取独立前缀行矩阵 $B$，则已证

$$
\log\|\varphi_D^k\|_p
 =\{\delta_p(B)-\delta_p([B;r_k])\}\log p.
\tag{4.2}
$$

这里 $\delta_p$ 是非零最大子式的最小赋值；冗余前缀行不参加其定义。
等价而便于与 Newton 行比较的形式是

$$
\boxed{\quad
\varphi_D^k(L_{D,k,p})\subset p^q\mathbb Z_p
\iff
r_k\in\operatorname{row}_{\mathbb Q_p}(B)+p^q\mathbb Z_p^{N_D}.
\quad}
\tag{4.3}
$$

证明是把 $B$ 的饱和行空间用一个整可逆列变换化为前若干坐标，
其余坐标正是饱和核的对偶。这个变换也证明 (4.2)。

因此一个候选 Newton 关系若要给 $q$ 层改善，实际必须找到同一组
$c_0,\ldots,c_{k-1}\in\mathbb Q_p$，使得

$$
[Z^{k-a}]F^b-\sum_{j<k}c_j[Z^{j-a}]F^b\in p^q\mathbb Z_p
\quad\text{对全部 }a+b\le D.
\tag{4.4}
$$

负指标的系数约定为零。前缀行的系数不必整；这是饱和核的真实对偶
条件，不是另加限制。第2节目前只支付固定半因子某一组权的线性行，
没有支付 (4.4) 的所有混合列。

所需的全球目标仍准确为

$$
\sum_{p\notin S}
 \{\delta_p(B)-\delta_p([B;r_k])\}\log p
 \le\alpha'k\log k+C(k+D),
\tag{4.5}
$$

对所需的 $D\asymp\sqrt k$ 范围统一成立，再处理固定 places。
负的局部项必须保留；(3.3) 不能从 (4.5) 的左边直接相减。

## 5. 两类首坏带的统一合流比较

本节直接针对 (4.1) 的中央图像，不改成 Euler 商。
固定有限集合之外，置

$$
r=\begin{cases}p-1,&p\equiv1\pmod4,\\p+1,&p\equiv3\pmod4.\end{cases}
$$

R45/R46 保证 $e_0,\ldots,e_r$ 整。取
$1\le q\le p-1$（普通），或 $1\le q\le p-3$（惰性）。
将普通评价矩阵的 $0,\ldots,r$ 行保持原样，后 $q$ 行各乘 $p^2$。
它们全部整。已有实际首带公式分别为

$$
p^2P(Z,F)\equiv Z^r\Xi_p(Z)P_Y(Z,F_{\le r})
 \pmod{p,Z^{r+q+1}},
\tag{5.1}
$$

其中普通 $\Xi_p=A_p^2\theta^2F_{\le r}$，惰性
$\Xi_p=\kappa_p^2(Nf)^{-2}F_{\le r}$。
两者的 $Z$ 一次项都是单位，因为 $e_1=4/17^3$ 为单位。

于是上述缩放矩阵的约化，经一个对角为单位的三角行变换，准确成为

$$
\mathcal C_{D,r,q}=
\begin{pmatrix}
[Z^j]P(Z,F_{\le r})\ (0\le j\le r)\\
[Z^j]P_Y(Z,F_{\le r})\ (0\le j<q)
\end{pmatrix}.
\tag{5.2}
$$

若它满行秩，则原评价矩阵的非零 Smith 指数恰为

$$
\underbrace{-2,\ldots,-2}_{q},
\quad\underbrace{0,\ldots,0}_{r+1}.
\tag{5.3}
$$

特别地，每个新坏行在此前真正饱和核上的范数均为 $p^2$。

现在令 $F_{\le r}\mapsto F_{\le r}+\eta Z^r$，$\eta\in\mathbb Z_p$。
全部导数行不变，value 行仅末行增加 $\eta P_Y(0,0)$。
这是 (5.2) 中已存在的一行。因此其整行格、所有最大子式理想、
秩及方阵行列式均不变。普通情形 $q=r$ 的带尾仍成立；
$\Xi_p$ 的变化只在原三角变换的非对角部分。

所以两类的首带主格都看不见单独的中央系数 $e_r$。
实际全失败在普通处把 $v_p(e_{p-1})\ge2$ 加强到 $\ge4$，
在惰性处把 $e_{p+1}$ 加强为 $p^2$ 整除；这些单项加强不能改变
(5.2)。这没有说原固定 ODE 的全部高低系数可以独立变化，也没有
排除更深余行受到 (1.1) 的限制。

## 6. 任意固定数目的坏带只有线性总预算

这是关于 (4.5) 量级的一条有用界。R44 的逐系数估计给

$$
v_p(e_m)\ge-\frac{2m-1}{p-1}.
$$

因此不论 $D$ 多大，任意第 $k$ 行的单项式列都满足

$$
v_p([Z^k]Z^aF^b)\ge-\frac{2k}{p-1}.
$$

限制到饱和核只能缩小范数，故
$\log\|\varphi_D^k\|_p\le2k\log p/(p-1)$。
固定坏集外，$p>k+2$ 时全部输入系数整，局部对数范数不为正。
于是对 $2\le R\le k/2$ 有统一上界

$$
\boxed{\quad
\sum_{\substack{p>k/R\\p\notin S}}\log\|\varphi_D^k\|_p
 \le 2k\log R+O(k).
\quad}
\tag{6.1}
$$

使用的是 $\sum_{x<p\le y}\log p/(p-1)=\log(y/x)+O(1)$；
允许局部项为负并不影响这个上界。常数与 $D$ 无关，固定坏位另列。

特别地，任何固定数目的坏带只贡献 $O_R(k)$，不能单独改变
$k\log k$ 的 arithmeticity 系数。若 $R=\log k$，右边为
$O(k\log\log k)=o(k\log k)$。真正尚需统一控制的是
$p\le k/\log k$ 的越来越深前缀，而不只是继续增加一两个首带实例。

## 7. R62 中央假设可合法进入的实际矩阵

对 Euler 图像 $Y=4\mathscr H/f_0$，写
$f_0=e^{\alpha z^d}G_0$、$\mathscr H=e^{\alpha z^d}K$。
原列 $w^aY^b$ 可以在所有行同时乘 $G_0^D$，变成

$$
\boxed{\quad w^a(4K)^bG_0^{D-b},\qquad a+b\le D.\quad}
\tag{7.1}
$$

这个操作**准确保持每阶饱和核及评价范数**。一般地，若所有输出同乘
$U(w)$，$U(0)\in\mathcal O^\times$，则消失至 $k_w-1$ 阶的条件不变，
第 $k_w$ 项只乘 $U(0)$。即使 $U$ 的高系数不整，结论仍成立；
不能将它与改变源截面基混为一谈。

R62 的全失败现在准确表示：$K$ 的中央余类投影在更大 $\rho$ 盘为
Tate 函数，Stokes 展开中 $E_0$ 的系数为零。它确实改变了 (7.1)
的输入。然而仍保留所有非中央 $E_j$，特别 $\mathcal S_4\equiv1$。

这里存在一个须实际支付的乘法问题。若
$K(z)=\sum_{0\le j<d}z^jK_j(z^d)$，则

$$
\mathsf P_0(K^2)=K_0(z^d)^2
 +z^d\sum_{j=1}^{d-1}K_j(z^d)K_{d-j}(z^d).
\tag{7.2}
$$

不出现的四倍数余类视为零。即使 $K_0$ 已在更大盘解析，(7.2) 的
混合项并未由此消失；它们是 (7.1) 的真实非线性列的一部分。
不能把中央投影当作乘法同态。

普通侧也有同样明确的区别：函数乘积对应 Amice 测度的**加法**卷积，
其 principal Mellin 导数涉及
$\log\langle x_1+\cdots+x_b\rangle$ 及和为单位的边界，
并不是单个 $\log\langle x\rangle$ 矩的乘积。
第2节的单列关系尚未控制这些实际卷积列。

因此本轮已把联合反设落实为 (2.3)/(2.8)，把需要得到的整格结论落实为
(4.3)/(4.4)，并用 (6.1) 指明必须进入无界坏带的范围。
下一步应在真实固定 ODE 上研究这些混合列的同一饱和关系；
本篇没有把 (3.3) 的输入格指数当作已经得到的 (4.5)。

### 直接依赖

- R44/R45/R46/R47：同一中央对角的系数界、首分母与复增长。
- [实际 vanishing jets/minors](2026-11-12-central-vanishing-jets-and-minors.md)：
  标准整模型及准确 Plücker 范数。
- R54/R60/R62/R63/R77：完整半因子、两类 Newton 尾界、实际自参考及
  中央 Stokes 条件；本文没有新增插值规范。
- [首坏带合流格](2026-11-12-inert-first-bad-band-and-confluent-jets.md)
  与[第二带余行](2026-11-12-second-band-bockstein-and-central-variation.md)：
  本篇第5节采用同一整行论证，但明确改回 R44 的中央图像。
