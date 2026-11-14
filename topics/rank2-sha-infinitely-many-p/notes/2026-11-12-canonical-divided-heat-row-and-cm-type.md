# 实际中心零格上的除 $p$ 热泛函及 CM 类型

日期：2026-11-12。状态：以下整格、除 $p$ 行、CM 比较及类型区分均已证明；
没有证明实际行在无穷多个惰性素数处非零。

本篇的输入是已经认证的实际截面，而不是任意相同次数的 theta 函数。
在 $E_0:y^2=x^3-x$ 上，记

$$
 \theta(z)=\theta_T(z),\quad T=(0,0),\quad
 u(z)=x(z)^{-1/2}=z+O(z^5),\quad V=u^4=x^{-2}.
$$

令

$$
 F_k=\theta^{17}V^k\quad(0\leq k\leq4),\qquad
 \mathcal V=\bigoplus_{k=0}^4\mathbb ZF_k,\qquad
 I=\ker(\operatorname{ev}_0:\mathcal V\to\mathbb Z)
   =\bigoplus_{k=1}^4\mathbb ZF_k.
 \tag{1}
$$

它们在特征零线性无关，例如首项分别是 $z^{4k}$。
实际向量是

$$
 A=F_1+\frac35F_2-\frac15F_3+\frac15F_4.
 \tag{2}
$$

以下均取 $p\geq7$、$p\equiv3\pmod4$，写 $p=4r-1$。
所有分母 $5$ 在这些局部环中可逆。

## 1. 整提升给出的 canonical 除 $p$ 行

[全局 Hurwitz 整数流](2026-11-12-global-hurwitz-integers-and-polynomial-flow.md)
给出

$$
 u'=v,\qquad v'=-2u^3,\qquad L'=u^2,\qquad\theta'=L\theta,
 \quad u(0)=L(0)=0,\ v(0)=\theta(0)=1.
 \tag{3}
$$

因此每个 $F\in\mathcal V$ 的 Hurwitz 系数
$h_n(F)=F^{(n)}(0)$ 都是整数。
取已固定的提升

$$
 \kappa_p=-\frac12(-1)^r\binom{2r}{r}\in\mathbb Z_{(p)}^\times.
 \tag{4}
$$

[准确首坏项](../results/R38-exact-inert-sigma-size-and-jet-budget.md)
及 $\theta^2=x\sigma^2$ 给

$$
 p[z^{p+1}]\theta\equiv\kappa_p\pmod p.
 \tag{5}
$$

在 $p+1$ 次以下，$\theta$ 的系数均 $p$ 整。
对 $k\geq1$，$u^{4k}$ 从 $z^{4k}$ 开始；计算
$[z^{p+1}]\theta^{17}u^{4k}$ 时不使用 $\theta$ 的首坏项。
这里 $u$ 也只需到次数 $p-2$：它只有 $1\bmod4$ 次幂，且其 Hurwitz
系数整。因此

$$
 [z^{p+1}]F_k\in\mathbb Z_{(p)}\quad(k\geq1),\qquad
 p[z^{p+1}]F_0\equiv17\kappa_p\pmod p.
$$

因 $(p+1)!/p\equiv-1\pmod p$，这等价于全格上的准确合同

$$
 h_{p+1}(F)\equiv-17\kappa_p F(0)\pmod p
       \qquad(F\in\mathcal V\otimes\mathbb Z_{(p)}).
 \tag{6}
$$

于是

$$
 \widetilde B_p(F)=
 \frac{h_{p+1}(F)+17\kappa_pF(0)}p\pmod p
 \tag{7}
$$

定义了 $\mathcal V/p\mathcal V$ 上的线性泛函。确实，若将提升 $F$
改成 $F+pG$，(7) 的变化是
$h_{p+1}(G)+17\kappa_pG(0)$，由 (6) 为零模 $p$。
若将 (4) 换成同余的另一提升，(7) 只增加一个常数倍的
$\operatorname{ev}_0$。所以在 $I/pI$ 上得到不依赖这一选择的泛函

$$
 \boxed{\quad
 B_p(\overline F)=\frac{h_{p+1}(F)}p\pmod p,
 \qquad
 [z^{p+1}]F\equiv-B_p(\overline F)\pmod p.
 \quad} \tag{8}
$$

这是实际整提升的第一层除 $p$ 映射。它可用
$0\to p\mathbb Z/p^2\mathbb Z\to\mathbb Z/p^2\mathbb Z
\to\mathbb F_p\to0$ 及 (6) 表述；不需要先给一个未证明的
crystalline 比较，便能严格定义。
但定义良好不等于它的某个指定值非零。

特别地，改变实际输入的 $p^2$ 系数不是自由的：在同一个
$I$ 整格中改一个 $p$ 倍输入不会改变 (8)。因此，以任意相同权的
模形式加 $p$ 倍修正所构造的反例，若不保持这个实际输入整格，
不能作为 (8) 的反例。

## 2. 四个规范基上的完整行

令两个固定有理级数 $\mathcal F,\Theta$ 由

$$
 z=u\mathcal F(u^4),\qquad \theta(z(u))=\Theta(u^4),
 \qquad
 \mathcal F(v)=\sum_{n\geq0}
       \frac{\binom{2n}{n}}{4^n(4n+1)}v^n
 \tag{9}
$$

定义。设

$$
 \Xi_k(v)=\frac{(\Theta(v)^{17}v^k)'}{\mathcal F(v)}
       \qquad(1\leq k\leq4).
$$

[实际素数对角归约](2026-11-12-inert-theta-diagonal-and-curvature.md)
的 Lagrange 反演逐个基给出

$$
 \boxed{\qquad
 (B_p(F_1),\ldots,B_p(F_4))
   =-4\bigl([v^{r-1}]\Xi_1,\ldots,[v^{r-1}]\Xi_4\bigr)
                   \pmod p.
 \qquad} \tag{10}
$$

为核对精度，反演的特征零原式是

$$
 [z^{p+1}]F_k
 =\frac4{p+1}[v^{r-1}]
       (\Theta^{17}v^k)'\mathcal F^{-p-1}.
$$

所需截断范围内各级数均 $p$ 整，且 $r-1<p$；
$\mathcal F^{-p}\equiv1$ 到该次数，因此得到 (10)。
它只使用四个固定级数，并且保留了真实除 $p$ 后的信息。
它没有把这四个级数称为固定有限阶线性微分系统。

两个小素数的精确校准如下。表中第二列是特征零的
$[z^{p+1}](F_1,F_2,F_3,F_4)$；第三列是 (8) 的行。

| $p$ | 精确系数行 | $B_p$ 的模 $p$ 行 | $[z^{p+1}]A\pmod p$ |
|---|---|---|---|
| $7$ | $(61/60,1,0,0)$ | $(4,6,0,0)$ | $5$ |
| $11$ | $(23659/50400,37/60,1,0)$ | $(10,8,10,0)$ | $7$ |

这些数可由 $x''=6x^2-2$、$\theta^2=x\sigma^2$ 算到次数 $12$
独立重算；它们只校准规范，不是无穷性证据。

## 3. 同一次数 $17$ 的 CM 比较方向

记 $\alpha=4-i$。已经准确核过的固定除法多项式是

$$
 \frac{\theta(\alpha z)}{\theta(z)^{17}}
 =1+(12-20i)V+(-10+28i)V^2+(-20-12i)V^3+(1+4i)V^4.
 \tag{11}
$$

取共轭并相减，得到同一个 $I$ 中的截面

$$
 C_{17}(z):=
 \frac{\theta(\alpha z)-\theta(\bar\alpha z)}{-40i}
 =F_1-\frac75F_2+\frac35F_3-\frac15F_4.
 \tag{12}
$$

所以这次比较与实际 $A$ 的次数、首项和参考指数均相同。
若 $t_n=[z^n]\theta$，并定义整数 Lucas 序列

$$
 U_n=\frac{\alpha^n-\bar\alpha^n}{-2i},\qquad
 U_0=0,\quad U_1=1,\quad U_n=8U_{n-1}-17U_{n-2},
$$

则

$$
 [z^{p+1}]C_{17}=\frac{U_{p+1}}{20}t_{p+1},
 \qquad
 [z^{p+1}]C_{17}\equiv
       \frac{\kappa_p}{20}\frac{U_{p+1}}p\pmod p.
 \tag{13}
$$

$p\mid U_{p+1}$ 来自 $\alpha^p\equiv\bar\alpha$，
而 (5) 给最后的合同。
所以 (10) 的这个指定线性组合准确等于一个固定底数的
Lucas 除 $p$ 商，并非由有限维性自动保证是单位。

完整惯性 Mahler 斜率却有更强的准确结论。
采用[实际半因子的规范](2026-11-12-inert-central-mahler-half-factor.md)，
准确沿用其中正式参数 $t=-x/y$ 的定义
$c_p=[t^{p+1}]\log(\sigma(\log_Et)/t)$，$v_p(c_p)=-1$，
并令 $J_{\theta,p}(0)=1$ 为次数一参考半因子。
写

$$
 a_p=\frac{\alpha^{p+1}}{17},\qquad
 b_p=\frac{\bar\alpha^{p+1}}{17}
                  \quad\in1+p\mathcal O_{\mathbb Q_p(i)}.
$$

在与 $A$ 同样的指数 $17c_p$ 下，整数权的准确系数恒等及解析性给

$$
 J_{C_{17},p}(s)=\frac{a_p^s-b_p^s}{-40i}J_{\theta,p}(s),
 \qquad
 J_{C_{17},p}'(0)=\frac{p+1}{-40i}
                   \log_p\frac{4-i}{4+i}\ne0.
 \tag{14}
$$

最后一个非零性是无条件的：$(4-i)/(4+i)\in\mathbb Q(i)$
不是根单位，而局部单位的 $p$ 进对数核是根单位群。
其赋值准确等于 $v_p(U_{p+1})$。
因此同一个真实解析提取确实能给固定对数；但下面的类型区分
说明不能用 (14) 代替实际 $A$ 的未知导数。

## 4. 已知对数方向与实际 quartic 方向

在十七处的自然 Schrödinger 模型中，考察
$W=\operatorname{Fun}(\mathbb F_{17})$ 及
$D_af(y)=f(ay)$。$i$ 对应 $4\in\mathbb F_{17}^\times$，
其阶是 $4$。所以

$$
 W^{D_4=1}
 =\langle\delta_0,1_{\mathbb F_{17}^\times}\rangle
  \oplus\bigoplus_{j=1}^3
     \langle\lambda^{-j}(y)1_{\mathbb F_{17}^\times}\rangle,
 \qquad \lambda(3)=-i.
 \tag{15}
$$

这只是有限群的精确分解：零点给一个平凡表示，非零点的四个
$\langle4\rangle$ 轨道给四个字符。平凡类型有维数 $2$，
其余三个类型各有维数 $1$。

[已经证明的 CM 类型接口](2026-11-12-theta-rational-cm-scaling-type.md)
说明，$\theta(\alpha z)$ 与 $\theta(\bar\alpha z)$ 来自秩零参考的
CM 环面平移，二者在十七处仍属平凡紧类型。
实际 $A$ 则来自
$\lambda^{-1}(y)1_{\mathbb F_{17}^\times}$；它属于非平凡 quartic 类型。
这两个已证接口足够区分 (12) 和 (2)，不需要凭维数为其他类型
认定一条新的秩二曲线。

还有一个直接的实际检验，排除了把除 $p$ 行误当字符等变标量。
在 $p=7$，上表给

$$
 B_7(A)=2,\qquad B_7(C_{17})=4\qquad\text{在 }\mathbb F_7.
 \tag{16}
$$

扩域到 $\mathbb F_{49}$ 后，$A$ 与 $C_{17}$ 属于不同的紧字符，
且两条线均保留在中心零空间内。
一个到任意固定一维字符的等变线性泛函，必杀掉其中至少一条线。
(16) 说明实际除 $p$ 行不是这样的泛函。
所以不能以 quartic 类型的一维性套 Schur 引理，宣称其实际值自动非零。
若将来构造更大的 Frobenius 矩阵，必须保留求值行和这些不交换的
热修正，不能只保留一个字符块的维数。

## 5. 纯对数条件是另一条真实限制

固定同次数参考 $f_0=\theta(\alpha z)$，令 $R_k=F_k/f_0$。
这些有理函数在 $O$ 为零，且至多在
$[\alpha]^{-1}(T)\setminus\{T\}$ 有简单极点。
[实际纯对数分解](2026-11-12-actual-rational-reference-pure-logarithmic-form.md)
给任意这样的 $R$ 一条准确等式

$$
 R\omega=c(R)\omega+\frac1{17}\sum_P\rho_Pd\log g_P,
 \qquad
 c(R)=\frac1{17}\sum_{Q\in E_0[\alpha]}R(Q),
 \quad\operatorname{div}g_P=17(P)-17(T),\quad g_P(O)=1.
 \tag{17}
$$

在整个四参数格上，这个 holomorphic 系数的行可完全算出：

$$
 \boxed{\qquad
 (c(R_1),c(R_2),c(R_3),c(R_4))
 =\frac1{1088}(3+12i,-9-2i,-17,-5-54i).
 \qquad} \tag{18}
$$

下面给出只需乘法与 Newton 幂迹的证书。
取 $X=x^2$，并记

$$
 \begin{aligned}
 K(X)&=(4-i)X^4+(-12+20i)X^3+(28+10i)X^2+(-20-12i)X-i,\\
 U(X)&=X^4+(12-20i)X^3+(-10+28i)X^2+(-20-12i)X+1+4i.
 \end{aligned}
$$

四次商代数 $\mathbb Q(i)[X]/(K)$ 中，
$R_k=X^{4-k}/U$ 的余式是 $H_k/16384$；下表按
$(1,X,X^2,X^3)$ 列出 $H_k$ 的系数。

| $k$ | $1$ | $X$ | $X^2$ | $X^3$ |
|---|---|---|---|---|
| $1$ | $-11-10i$ | $-345+82i$ | $-265-142i$ | $5+54i$ |
| $2$ | $-13-18i$ | $-655+66i$ | $-95-278i$ | $-29+54i$ |
| $3$ | $-139+22i$ | $-729-94i$ | $-73-462i$ | $-59+70i$ |
| $4$ | $499-3138i$ | $-847+3650i$ | $-3103-1158i$ | $227+534i$ |

直接检查 $K\mid(UH_k-16384X^{4-k})$，再用

$$
 \operatorname{Tr}(1,X,X^2,X^3)
  =(4,4-4i,-12-40i,-236-92i)
$$

及 $c=4\operatorname{Tr}(R)/17$，即得到 (18)。
可复核脚本是
[check-canonical-divided-heat-row.py](../scripts/check-canonical-divided-heat-row.py)。

实际 $A$ 的 (18) 值准确为零；相反，同次数已知对数方向 (12) 满足

$$
 c(C_{17}/f_0)=\frac{1+4i}{170}\ne0.
 \tag{19}
$$

所以 (14) 不能作为已经进入实际纯对数子空间的非零校准。
特别地，当四个系数 $a_k$ 都是有理数时，$c=0$ 是两个独立的
有理线性条件，准确等价于

$$
 a_2=6a_1-27a_4,\qquad a_3=-3a_1+14a_4.
 \tag{20}
$$

因此该有理纯对数子空间是二维的，可以取基
$(1,6,-3,0)$ 与 $(0,-27,14,1)$。
实际向量是第一条加第二条的 $1/5$ 倍。
这保留了原参考、全部简单极点和准确 holomorphic 修正；
它与仅保留一个抽象 de Rham 类的比较不同。

## 6. 仍须证明的准确断言

本题的惰性单位证书现在就是

$$
 \boxed{\qquad
 B_p\!\left(F_1+\frac35F_2-\frac15F_3+\frac15F_4\right)\ne0
 \quad\text{对无穷多个 }p\equiv3\pmod4.
 \qquad} \tag{21}
$$

已知的是 canonical 四参数输入、(10) 的固定级数行、
(13)–(14) 的同次数 CM 校准，以及实际 quartic 类型。
尚未证明的是跨 $p$ 限制这个指定加权行的非零定理。
另一种足够的完成方式是直接证明实际完整半因子的
$J_{A,p}'(0)\ne0$ 对无穷 $p$；它比 (21) 弱，不能被首层失效排除。
