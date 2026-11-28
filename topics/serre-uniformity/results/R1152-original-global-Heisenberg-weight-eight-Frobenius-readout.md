# R1152：原全局 Heisenberg 中心常数的权八 Frobenius 词读数

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇在 R1148 的 $p>C_{\rm cyc}$ 范围，保持 R1151 的同一个原 $\Theta=\eta(\gamma_3,\gamma_5)$、群律和 finite Fontaine–Laffaille 坐标。比值公式始终限定在原 $rs\ne0$ 分支，将其实际中央比值接到一个明确的 crystalline Frobenius 词系数：
$$
\boxed{\quad
\frac{z_\infty}{r_\infty s_\infty}
 =
 1+\frac{\zeta_{p,1}(3,5)}
          {5\zeta_{p,1}(3)\zeta_{p,1}(5)}.
\quad}
\tag{1152.1}
$$
左边是原 compatible integral lift 的实际 Frobenius 坐标；右边的方向及指标在 §3 固定。当 R1151 的 $rs\ne0$ 时，整个右边在 $\mathbb Z_p$，其约化就是 $z/(rs)$。不先约化分母中的单个 period，也不把 (1152.1) 当作其非零性或某个固定有理数值。

## 1. 从原有限类到同一整 lift

记 $L_{r,n}=\mathbb Z/p^n(r)$，$S_0=\operatorname{Spec}\mathbb Z[1/p]$。原群仍为
$$
\mathcal H_n=L_{3,n}\oplus L_{5,n}\oplus L_{8,n},\qquad
(a,b,h)(a',b',h')=(a+a',b+b',h+h'+ab').
\tag{1152.2}
$$
原 $\gamma_{3,n},\gamma_{5,n}$ 取 R1148 §10 的标准 cyclotomic elements 的 compatible coefficient reductions；权五也就是 R1147 (1147.26) 的同一 tower。第一层为原 $\gamma_3,\gamma_5$。这里的箭头是 $\mathbb Q$ 上的系数约化，不把有限 cyclotomic extension 中的 field norm 错当成该箭头。

R1146 已付 $H^1(S_0,L_{8,1})=H^2(S_0,L_{8,1})=0$。逐次使用
$$
0\longrightarrow L_{8,1}\longrightarrow L_{8,n}
 \longrightarrow L_{8,n-1}\longrightarrow0
$$
的长正合列，直接归纳得
$$
H^1(S_0,L_{8,n})=H^2(S_0,L_{8,n})=0\qquad(n\ge1).
\tag{1152.3}
$$
因此每个固定 pair $(\gamma_{3,n},\gamma_{5,n})$ 都有唯一 Heisenberg lift $\Theta_n$，且 $\Theta_n\bmod p^{n-1}=\Theta_{n-1}$。Tate characters $3,5,8$ 的 $H^0$ 为零，所以固定 quotients 的兼容同构也唯一。取极限得到 $\Theta_\infty$，并且
$$
H^1(S_0,\mathbb Z_p(8))=H^2(S_0,\mathbb Z_p(8))=0.
\tag{1152.4}
$$
此处连续上同调的 $\varprojlim^1$ 项为零：相关有限 $H^1$ 全零，$H^0$ 也全零。张量 $\mathbb Q_p$ 后相同消失成立。

局部 R1151 §1 的坐标构造逐字在 $\mathbb Z/p^n$ 上成立：
$$
\Phi=R(A,B,H)\operatorname{diag}(1,p^{-3},p^{-5},p^{-8}),\qquad
R(A,B,H)=
\begin{pmatrix}
1&0&0&0\\
A&1&0&0\\
B&0&1&0\\
H&0&A&1
\end{pmatrix}.
\tag{1152.5}
$$
任意三个整 lifts 给同一 split filtration 的 strongly divisible module；finite full faithfulness 与唯一 Hodge lift 使不同三元组给不同 torsors。

这里也补全 $p^n$ 层的满性，而不是仅由第一层外推。对 $r=3,5,8$，非平凡 tame character 给
$H^0(\mathbb Q_p,L_{r,n})=0$；local duality 同时给 $H^2=0$。Euler characteristic 或逐层长正合列给 $\#H^1=p^n$。每个 abelian pair 的中心 lifting fibre 有 $p^n$ 个元素，故一共 $p^{3n}$ 个 local classes，与 (1152.5) 的互异三元组数相等。tensor width 仍是原 $16<p-2$。

坐标对系数约化相容。于是同一 $\Theta_\infty$ 有规范坐标
$$
(r_\infty,s_\infty,z_\infty)\in\mathbb Z_p^3,\qquad
(r_\infty,s_\infty,z_\infty)\bmod p=(r,s,z).
\tag{1152.6}
$$
它们不是另选 Galois cocycle 的三个取值。当 $rs\ne0$ 时，前两整坐标是单位，故左边 (1152.1) 已经是一个整的、可约模 $p$ 的数。

## 2. 原类在 mixed Tate 权八商中的识别

使用已发表的 mixed Tate 结构与 crystalline comparison，准确来源列在 §7。对 $\mathrm{MT}(\mathbb Z)$，规范 de Rham fibre functor 的 Galois 群为 $\mathbb G_m\ltimes U$，其分次 Lie 代数自由，生成权为 $3,5,7,\ldots$，每个权一维。这里“权”是 Tate exponent，实际 motivic weight 为其 $-2$ 倍。

因此权至八仅有
$$
\sigma_3,\quad \sigma_5,\quad \sigma_7,\quad [\sigma_3,\sigma_5].
\tag{1152.7}
$$
没有权一、偶权 indecomposable 或额外权八方向。把 $\sigma_7$ 及更高生成元杀掉，并令
$$
\sigma_3\mapsto X_3,\qquad
\sigma_5\mapsto Y_5,\qquad
[\sigma_3,\sigma_5]\mapsto Z_8,\qquad
[X_3,Y_5]=Z_8
\tag{1152.8}
$$
给出一个真实的 mixed Tate Heisenberg quotient，群律取 (1152.2)。

还须识别其 abelian classes 与原 circular-unit source。Nakamura–Sakugawa–Wojtkowiak（2017）的 Proposition 2.2、Lemma 2.4 和 (2.11) 在 $z=1$ 给：在 $\ker\chi_{\rm cyc}$ 上，depth-one polylogarithmic character 是原 Soulé character 的非零倍数，倍数的绝对代数表达为
$$
\frac1{(r-1)!\,(1-p^{r-1})}\qquad(r=3,5);
\tag{1152.9}
$$
path/action 取逆会给相应符号，但不改变该线非零。该 Soulé character 的 Kummer 元恰为
$$
\prod_{\substack{1\le a<p^n\\p\nmid a}}
 (1-\zeta_{p^n}^{a})^{a^{r-1}},
$$
所以这是原 cyclotomic element 的同一输入。$\mathbb Q$ 到 $\ker\chi_{\rm cyc}$ 的 $H^1$ restriction 在这些非零权上为单射：cyclotomic quotient 的 $H^1$ 被一个使 $\chi^r-1$ 可逆的 tame 元素消去。

由 R1148 §10 的原生成性，两个 rational global $H^1$ 均为一维，原 $\gamma_{3,\infty},\gamma_{5,\infty}$ 非零。故 (1152.8) 的两个 realised quotients 与它们只差两个非零 $\mathbb Q_p$ 标量 $c_3,c_5$。按
$$
(a,b,h)\longmapsto(c_3a,c_5b,c_3c_5h)
\tag{1152.10}
$$
运输后，quotients 完全相同；(1152.4) 使整个 realised global lift 与原 $\Theta_\infty\otimes\mathbb Q_p$ 唯一同构。

本篇无需猜 $c_3,c_5$ 的符号或整估值：对 (1152.10)，
$$
\frac{c_3c_5h}{(c_3a)(c_5b)}=\frac h{ab}.
\tag{1152.11}
$$
因此本篇读数在原指定来源上的识别完全不受这两次独立缩放影响。该论证使用的是原 global central $H^1$ 消失；不是仅因两对象有相同 graded pieces 就宣布它们相同。

## 3. 固定 Frobenius、Ihara 群律和指标

令 $X=e_0,Y=e_1$，以 $Y$ 的个数定义 depth。取已刊 Jarossay（2020）§1.1.2–1.1.3 作者版的惯例：
$$
g\circ f=g(X,Y)\,
 f\bigl(X,g^{-1}Yg\bigr),\qquad
\tau(q)f(X,Y)=f(qX,qY).
\tag{1152.12}
$$
$\varphi$ 是 crystalline Frobenius，Tate 线 $\mathbb Q_p(r)$ 上为 $p^{-r}$。固定
$$
\Phi_{p,1}=\tau(p)\varphi(1),\qquad
\tau(p)\varphi(f)=\Phi_{p,1}\circ f.
\tag{1152.13}
$$
这里 base field 是 $\mathbb Q_p$，coefficient Frobenius 为恒等。于是
$$
\varphi(f)=\tau(p^{-1})(\Phi_{p,1})\circ\tau(p^{-1})(f).
\tag{1152.14}
$$
它明确选取与 (1152.5) 相同的 Frobenius 方向。若改成 inverse Frobenius 或 Frobenius-fixed KZ path，必须另作变换；不能原样代入下式。

令 $\Phi=\Phi_{p,1}$，并准确定义
$$
\begin{aligned}
a&=\Phi[X^2Y]=-\zeta_{p,1}(3),\\
b&=\Phi[X^4Y]=-\zeta_{p,1}(5),\\
q&=\Phi[X^4YX^2Y]=\zeta_{p,1}(3,5).
\end{aligned}
\tag{1152.15}
$$
最后一个指标按 Jarossay 的从右向左 convention 固定；本篇始终同时给出词 $X^4YX^2Y$，避免与相反的双指标顺序混用。

由已刊 mixed Tate crystalline/de Rham comparison，原 Galois 同构在 §2 的运输后给同一 filtered Frobenius 对象。规范 mixed Tate de Rham splitting 在本四维表示中的权零向量，正是原 $\operatorname{Fil}^0$ 中映到一的唯一 Hodge lift；其余三方向由同一 Tate lines 及 right action 锁定。因此没有另加一个中心 Hodge gauge。

写 $\Phi$ 在 (1152.8) 商中的实际群坐标为 $(a,b,h)$。(1152.14) 与 (1152.5) 给其 Frobenius coordinates 为
$$
(p^{-3}a,\ p^{-5}b,\ p^{-8}h).
\tag{1152.16}
$$
乘以 §2 的两个 scalars 后就是原 $(r_\infty,s_\infty,z_\infty)$。权缩放及 (1152.10) 都在比值中抵消，故
$$
\boxed{\quad
\frac{z_\infty}{r_\infty s_\infty}=\frac h{ab}.
\quad}
\tag{1152.17}
$$

## 4. 指定权八词的全部系数

将 $\sigma_3,\sigma_5$ 按其非零 depth-one image 规范化，使
$$
f_3=\operatorname{ad}_X^2Y=X^2Y-2XYX+YX^2,
$$
$$
f_5=\operatorname{ad}_X^4Y
=X^4Y-4X^3YX+6X^2YX^2-4XYX^3+YX^4
\tag{1152.18}
$$
分别是其 depth-one 部分。高 depth 部分保留在实际生成元内；下面说明它们为何不贡献指定读数。

由 (1152.12)，Ihara Lie bracket 来自
$$
f\star g=fg+D_f(g),\qquad
D_f(X)=0,\quad D_f(Y)=[Y,f],\qquad
\{f,g\}=f\star g-g\star f.
\tag{1152.19}
$$
令 $W=X^4YX^2Y$，$W'=X^2YX^4Y$。直接展开 (1152.18) 给完整表：

| 项 | $[W]$ | $[W']$ |
|---|---:|---:|
| $f_3f_5$ | $0$ | $1$ |
| $D_{f_3}(f_5)$ | $0$ | $0$ |
| $f_5f_3$ | $1$ | $6$ |
| $D_{f_5}(f_3)$ | $-6$ | $0$ |
| $f_3\star f_5$ | $0$ | $1$ |
| $f_5\star f_3$ | $-5$ | $6$ |
| $\{f_3,f_5\}$ | $5$ | $-5$ |

例如 $D_{f_3}(f_5)$ 在 $W$ 的两个可能项来自
$X^4Yf_3-X^4f_3Y$，系数 $1-1=0$；而
$D_{f_5}(f_3)$ 的唯一贡献是 $-X^2f_5Y$ 中的 $-6$。任何右端附有 $X$ 的其它项都不可能是 $W$。这付清了 derivative 项，不能只取普通 concatenation。

取实际 Ihara logarithm，记至权八为
$$
\log_\circ\Phi
=a\sigma_3+b\sigma_5+c\sigma_7
+w[\sigma_3,\sigma_5].
\tag{1152.20}
$$
权八、depth 二的项只可能来自显示的 bracket 与二次项。三次及以上乘积权至少九；任一生成元的 depth $\ge2$ 部分与另一个生成元作 $\star$ 后 depth 至少三，所以不能贡献 $W,W'$。没有遗漏一个未知权八 indecomposable。

Ihara exponential 的二阶项为 $\frac12L\star L$。故表给
$$
\Phi[W]=5w-\frac52ab,\qquad
\Phi[W']=-5w+\frac72ab.
\tag{1152.21}
$$
同一 Heisenberg 群的普通 exponential 则给
$$
h=w+\frac12ab.
\tag{1152.22}
$$
代入得准确的两个词身份
$$
\boxed{\quad
\Phi[X^4YX^2Y]=5h-5ab,\qquad
\Phi[X^2YX^4Y]=-5h+6ab.
\quad}
\tag{1152.23}
$$
特别两者之和为 $ab$。此处的 $5$ 与常数项 $1$ 都来自原群律及 Ihara derivative，非任选正规化。

## 5. 同一整比值、原 finite subtraction 和边界

由 (1152.23) 得 $h=ab+q/5$，结合 (1152.15)/(1152.17) 即证 (1152.1)。

在 R1151 的 $rs\ne0$ 分支，定义
$$
\kappa_p=
\overline{\left(
1+\frac{\zeta_{p,1}(3,5)}
 {5\zeta_{p,1}(3)\zeta_{p,1}(5)}
\right)}
\in\mathbb F_p.
\tag{1152.24}
$$
横线约的是整个已经由 (1152.6) 证明在 $\mathbb Z_p$ 的量。于是
$$
\kappa_p=\frac z{rs},\qquad
\mathcal D/(rs)=\mathsf h-\kappa_p\mathsf a\mathsf b.
\tag{1152.25}
$$
Gaussian 和 cubic 两个原实际最高项因而分别是
$$
16\delta^3c_g^6rs\,
 (z_{12}-\kappa_p x_4y_8),
\tag{1152.26}
$$
$$
16\delta^3c_g^6rs\,
 \left(z_{12}-\kappa_p\frac{\lambda A_*}{6}y_7\right).
\tag{1152.27}
$$
这里 $z_{12},x_4,y_8,y_7,\lambda$ 全部仍是 R1149–R1151 的原 $F_0$ 条目。global constant 已由一个指定 weight-eight Frobenius 读数锁定；不能再把它当自由平移、置零，或用单独 $z_{12}$ 的值代替 (1152.26)/(1152.27)。

当 $r=0$ 或 $s=0$ 时，本篇不定义 (1152.24) 作为有限比值；继续使用 R1151 的七分支表。即使 rational depth-one period 非零，模 $p$ 为零时也不能除去该支。

本篇没有证明 $\kappa_p$ 为某个固定数，没有证明上述中央组合非零，也没有把有限第一数字条件升成 whole $p$-disk 排点。继续目标是该指定双 period 的准确有限读数、原 $F_0$ 组合及深盘/其它原范围。

## 6. 为什么这不需要一个未付的 period 猜想

证明只用 mixed Tate 类别的已刊结构、已刊 crystalline comparison 与原上同调唯一性。没有使用 $p$-adic period map 的单射、不同 multiple zeta values 的线性独立、$\zeta_p(3)$ 或 $\zeta_p(5)$ 的普遍非消失猜想。

在使用分母的分支，$r_\infty,s_\infty$ 的单位性来自明确假设 $rs\ne0$ 和 (1152.6)；(1152.16) 与非零 rescaling 才推出相应 rational period 非零。其它分支原样保留。

标准 polylogarithmic 输入在 §2 只用于支付两个 abelian directions 与原 circular units 的非零同源；中央识别由 (1152.4) 与实际群商完成，而不是从一个 depth-one 公式猜出 length-two 值。

## 7. 精确来源

- [R1146](R1146-original-proper-arithmetic-Heisenberg-cover.md) 的原中心 $H^1/H^2$ 消失；[R1147](R1147-original-canonical-moment-Heisenberg-lift.md) 的原 compatible cyclotomic/Heisenberg tower、finite Fontaine–Laffaille 与短 tensor；[R1148 §10](R1148-original-canonical-cusp-Heisenberg-and-minus-one-Frobenius.md) 的原 $\gamma_3,\gamma_5$ 全局生成性；[R1151](R1151-original-finite-Frobenius-global-subtraction.md) 的原群律、Hodge frame、实际 finite coordinates 和全部零局部化分支。上述 $p^n$ 坐标满性、整比值及权八词计算在本文自证。
- P. Deligne、A. B. Goncharov，*Groupes fondamentaux motiviques de Tate mixte*，Ann. Sci. Éc. Norm. Sup. **38 (2005), 1–56**，[期刊入口](https://www.numdam.org/item/ASENS_2005_4_38_1_1_0/)，Propositions 2.3、2.10 及 §5。所用 free-Lie/weight/fibre-functor 陈述也在下面 Yamashita §3.1 完整列出并已亲读。
- G. Yamashita，*Bounds for the Dimensions of p-Adic Multiple L-Value Spaces*，Documenta Math. Extra Volume Suslin **(2010), 687–723**，[已刊全文](https://ems.press/content/book-chapter-files/27510?nt=1)。§3.1（印刷696–699页）给 free graded Lie、$N=1$ 生成函数与 canonical de Rham functor；Theorem 4.2、Definition 4.4、Theorem 4.6（708–712页）给 crystalline realisation 和 functorial de Rham comparison。这里只消费已刊 theorem，不消费该文的 period 单射猜想。Frobenius 的取向使用本文 (1152.13)，不把其它记号的 inverse Frobenius 无变换移入。
- H. Nakamura、K. Sakugawa、Z. Wojtkowiak，*Polylogarithmic analogue of the Coleman–Ihara formula, I*，Osaka J. Math. **54 (2017), 55–74**，[期刊全文](https://ir.library.osaka-u.ac.jp/repo/ouka/all/61898/ojm54_01_055.pdf)。Proposition 2.2、Lemma 2.4、(2.10)–(2.11)（59–60页）付同一 depth-one character 与原 Soulé Kummer moment；本文不使用其单变量公式代替 length-two 值。
- D. Jarossay，*Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values*，Algebra & Number Theory **14 (2020), 1711–1746**，DOI [10.2140/ant.2020.14.1711](https://doi.org/10.2140/ant.2020.14.1711)，[作者已刊对应版](https://arxiv.org/pdf/1610.09107)。作者版 §1.1.2–1.1.3，(1.1)–(1.4) 与 Notation 1.1.1 固定本文的 Ihara law、正向 $\Phi_{p,1}$、Tate scaling 和双指标顺序。本文没有把其另外未刊系列的计算公式当作黑箱。

无数学程序执行；无已有窗口重算。主目标仍继续。


## 8. 去掉无穷 period 表示：同一正向 Frobenius 的有限 harmonic 读数

下面继续同一 $\Phi=\Phi_{p,1}$，置
$$
g=\tau(p^{-1})\Phi,\qquad
(a_0,b_0,h_0)=(p^{-3}a,p^{-5}b,p^{-8}h)
\tag{1152.28}
$$
为其在原权八商中的坐标。定义有限和，指标严格按递增求和变量排列：
$$
\operatorname{Har}_p(n_1,\ldots,n_d)
=\sum_{0<m_1<\cdots<m_d<p}
 \frac1{m_1^{n_1}\cdots m_d^{n_d}}.
\tag{1152.29}
$$
它与 Gaussian 路线的首标签 $\mathcal H_p$ 不是同一记号。

### 8.1 完整尾项的整估值

令 $I_n\subset\mathbb Z_p$ 为所有 $p^j/j!$、$j\ge n$ 生成的理想。
有
$$
I_uI_v\subset I_{u+v},\qquad
I_n=p^n\mathbb Z_p\quad(n<p),\qquad
I_n\longrightarrow0.
\tag{1152.30}
$$
第一式来自二项式系数；后两式直接由 $j-v_p(j!)$ 得到。

Chatzistamatiou（2017）Theorem 5.3、§5.4 给 Frobenius-fixed KZ path $K$ 的所有长度 $n$ 词系数属于 $I_n$。这包括 regularized words：两条到共同 good point 的整路径相乘，使用 $I_uI_v\subset I_{u+v}$ 即得两个 tangential ends 的同一界。

由 (1152.13) 和 $\varphi(K)=K$，
$$
\Phi=\tau(p)K\circ K^{\circ-1}.
\tag{1152.31}
$$
Ihara substitution 与 inverse 的每个固定权系数是更低或相同权系数的整系数多项式，不引入分母；因此 $\Phi$ 的长度 $n$ 系数仍在 $I_n$。进而
$$
(\Phi^{-1}Y\Phi)[W]\in I_{|W|-1}.
\tag{1152.32}
$$
故 $g$ 的长度 $\le8$ 系数在 $\mathbb Z_p$；
$h_0=a_0b_0+g[X^4YX^2Y]/5$ 也在 $\mathbb Z_p$。

### 8.2 正确符号的有限公式

已刊 Jarossay（2015）§2.1 定理及 §3 的系数证明，
在 Jarossay（2020）(1.19) 的正向 convention 中，准确给
$$
p^w\operatorname{Har}_p(n_1,\ldots,n_d)
=(-1)^d\sum_{\ell\ge0}
(\Phi^{-1}Y\Phi)
 [X^\ell YX^{n_d-1}Y\cdots X^{n_1-1}Y],
\quad w=\sum n_i.
\tag{1152.33}
$$
这里消费的是已刊定理，不把另外未刊系列的计算当作黑箱。

为固定本篇方向与符号，重述该 $N=1$ 系数论证。
标准 KZ 解在一个额外首块 $X^\ell Y$ 上的 $z^p$ 系数是
$(-1)^{d+1}p^{-\ell-1}\operatorname{Har}_p(n_1,\ldots,n_d)$。
Frobenius 水平身份将它乘 $p^{w+\ell+1}$，并与
$z\mapsto z^p$ 的 KZ 解及 overconvergent Frobenius 解相乘。
在 $z^p$ 系数中，没有正的中间 $p$ 倍指数，所以交叉项全空。
后一个 KZ 解的 $z^p$ 项是其 $z$ 项；去掉末端 $X$ 的对数后，该项为
$-\sum_{j\ge0}\operatorname{ad}_X^j(\Phi^{-1}Y\Phi)$。
在以 $Y$ 结尾的指定词中，右端附 $X$ 的项不贡献，留下
$-\sum_{j=0}^{\ell}(\Phi^{-1}Y\Phi)[X^jY\cdots Y]$。
令 $\ell\to\infty$，已刊 §3 的 overconvergent 系数估值使剩余 Frobenius 解项趋零，正得 (1152.33)。这也说明为什么符号是 $(-1)^d$，以及为什么使用正向 $\Phi$。

现在 $p>w+1$。将 (1152.33) 除以 $p^w$；
每个 $\ell\ge1$ 项由 (1152.32) 落在
$$
p^{-w}I_{w+\ell}\subset p^{-w}I_{w+1}=p\mathbb Z_p.
$$
这些理想随 $\ell$ 趋零，所以整条尾部可约为零，而非仅截掉前几个可见项。
$\ell=0$ 项则由
$\Phi^{-1}Y\Phi=p^{-1}\tau(p)(g^{-1}Yg)$ 给
$$
\boxed{\quad
\operatorname{Har}_p(n_1,\ldots,n_d)
\equiv(-1)^d(g^{-1}Yg)
 [YX^{n_d-1}Y\cdots X^{n_1-1}Y]
 \pmod p.
\quad}
\tag{1152.34}
$$
本篇只用 $w=3,5,8$，故 $p>37$ 足够覆盖全部尾项与分母。

## 9. 必需的 depth-two 生成元及两个实际 Bernoulli 读数

用 $f_r=\operatorname{ad}_X^{r-1}Y$。原 $\sigma_3,\sigma_5$ 的所需部分为
$$
\begin{aligned}
\sigma_3&=f_3+q_3,\qquad q_3=[Y,[X,Y]],\\
\sigma_5&=f_5+q_5+(\text{depth}\ge3),\\
q_5&=2[Y,f_4]+\frac12[f_2,f_3].
\end{aligned}
\tag{1152.35}
$$
这里不是把全部高 depth 当零；后文严格说明指定词只消费这些部分。

第一式由原生成元的 antisymmetry 直接得到。第二式可由同一 motivic Ihara image 的 infinitesimal double-shuffle 付清。其五边形来自同一 motivic fundamental groupoids；Furusho（2011）Theorem 0.2、Corollary 0.3 将此 image 送入 double-shuffle Lie algebra。

具体地，对 $1+\varepsilon\sigma_5$，记单项 zeta 读数为 $Z=-1$，并按降序词 $X^{r-1}YX^{s-1}Y$ 记
$A=Z_{4,1},B=Z_{3,2},C=Z_{2,3},D=Z_{1,4}$。
四条 shuffle/stuffle 等式的线性部分正是
$$
B+C+Z=0,\quad A+D+Z=0,\quad
2A+B+C+D=0,\quad 6A+3B+C=0.
$$
涉及一个 leading $1$ 的 regularization 是一次项，两种 regularization 在此一致。
解得
$$
A=-2,\quad B=\frac{11}{2},\quad
C=-\frac92,\quad D=3.
\tag{1152.36}
$$
Jacobi 将 weight five/depth two 的自由 Lie 部分化为
$[Y,f_4]$ 与 $[f_2,f_3]$ 两个基元；在
$X^2YXY,XYX^2Y$ 上的系数分别为 $(3,-3)$ 与 $(-1,3)$。
故 (1152.36) 准确给 (1152.35)，没有除一个未知 period。

(1152.35) 直接读出
$$
\begin{aligned}
(g^{-1}Yg)[YX Y^2]&=-3a_0,\\
(g^{-1}Yg)[YX^3Y^2]&=-5b_0.
\end{aligned}
$$
例如第二式使用 $q_5[X^3Y^2]=-2$、$q_5[YX^3Y]=3$，
两项相减为 $-5$。结合 (1152.34)，
$$
\operatorname{Har}_p(1,2)\equiv-3a_0,\qquad
\operatorname{Har}_p(1,4)\equiv-5b_0.
\tag{1152.37}
$$

这里的 Bernoulli 读数也可直接支付。对 $m=2,4$，
在 $\mathbb F_p$ 中用 $i^{-1}=i^{p-2}$、$j^{-m}=j^{p-1-m}$，
再用 Faulhaber，得到
$$
\operatorname{Har}_p(1,m)
=\frac1{p-1}\sum_{k=0}^{p-2}
 \binom{p-1}{k}B_k
 \sum_{j=1}^{p-1}j^{2p-2-m-k}.
$$
本范围的 $B_k$ 都 $p$-整。内和唯一非零指数对应
$k=p-1-m$，值为 $-1$；
$\binom{p-1}{k}\equiv(-1)^k=1$、$p-1=-1$，
故该有限和准确为 $B_{p-1-m}$。记
$$
\beta_3=\overline{B_{p-3}},\qquad
\beta_5=\overline{B_{p-5}},\qquad
a_p=\overline{a_0},\quad b_p=\overline{b_0},\quad h_p=\overline{h_0}.
$$
得到
$$
\boxed{\quad
a_p=-\frac{\beta_3}{3},\qquad
b_p=-\frac{\beta_5}{5},\qquad
a_pb_p=\frac{\beta_3\beta_5}{15}.
\quad}
\tag{1152.38}
$$

## 10. 两个 weight-eight 词的完整共轭读数

至权八，(1152.20)–(1152.22) 等价于
$$
[g]_8=h_0\{\sigma_3,\sigma_5\}
       +a_0b_0(\sigma_5\star\sigma_3).
\tag{1152.39}
$$
设
$$
\begin{aligned}
V_{134}&=YX^3YX^2Y^2,\\
V_{125}&=YX^4YXY^2,
\end{aligned}
$$
并分别写 $V=YW_L=W_RY$。这两个词的 depth 都为四。
计算 (1152.39) 的 depth-three 部分时，
只用 $f_3q_5,q_3f_5$ 及其相同 depth 的导数项；
更高 depth 输入至少给 depth 四，再与 $Y$ 共轭后 depth 至少五，
不能贡献指定 $V$。

以下表格列出所有乘法与导数项；每个括号依次为 $[W_L],[W_R]$：

| 项 | $V_{134}$ | $V_{125}$ |
|---|---:|---:|
| $f_3q_5+q_3f_5$ | $(0,-9/2)$ | $(0,11/2)$ |
| $D_{f_3}q_5$ | $(2,0)$ | $(-4,6)$ |
| $D_{q_3}f_5$ | $(0,0)$ | $(-3,0)$ |
| $\sigma_3\star\sigma_5$ | $(2,-9/2)$ | $(-7,23/2)$ |
| $f_5q_3+q_5f_3$ | $(4,3)$ | $(-1,2)$ |
| $D_{f_5}q_3$ | $(6,-20)$ | $(-4,8)$ |
| $D_{q_5}f_3$ | $(9/2,0)$ | $(-11/2,0)$ |
| $\sigma_5\star\sigma_3$ | $(29/2,-17)$ | $(-21/2,10)$ |

这些数直接展开 (1152.35) 与
$D_fY=Yf-fY$ 得到。例如
$[Y,f_3]=Y^2X^2-2YXYX+2XYXY-X^2Y^2$；
对 $V_{125}$ 的 $W_L=X^4YXY^2$，其唯一可插入的
$XYXY$ 给 $2q_5[X^3Y^2]=-4$，
而 $D_{q_3}f_5$ 给 $-3$。
表保留了所有原导数，不只取 concatenation。

还必须包括普通 inverse 的交叉项：
$$
\begin{aligned}
[g^{-1}Yg]_9={}&[Y,[g]_8]\\
&+a_0b_0\bigl(
(\sigma_3\sigma_5+\sigma_5\sigma_3)Y
-\sigma_3Y\sigma_5-\sigma_5Y\sigma_3\bigr).
\end{aligned}
\tag{1152.40}
$$
后面括号在 $V_{134}$ 的值为 $-3/2$；
在 $V_{125}$ 的值为 $15/2+1=17/2$。
代入完整表，得到
$$
\boxed{\begin{aligned}
(g^{-1}Yg)[V_{134}]&=-25h_0+30a_0b_0,\\
(g^{-1}Yg)[V_{125}]&=2h_0-12a_0b_0.
\end{aligned}}
\tag{1152.41}
$$
三层 harmonic 的符号是负号。定义
$$
J_p=\overline{\operatorname{Har}_p(1,3,4)},\qquad
K_p=\overline{\operatorname{Har}_p(1,2,5)}.
$$
由 (1152.34)/(1152.38) 得到真实有限值
$$
\boxed{\quad
h_p=\frac{J_p+2\beta_3\beta_5}{25},\qquad
25K_p+2J_p=16\beta_3\beta_5.
\quad}
\tag{1152.42}
$$
这是从同一 Frobenius 来源读出的两个指定三重和，不是以任意多元矩阵代替原中央项。

## 11. 原整缩放是单位，故完整退化分支也可检测

§2 为 rational 比值只需 $c_3,c_5\ne0$。
现在进一步支付其单位性。固定相同的 compatible $\zeta_{p^n}$：
NSW (2.11) 的 Soulé Kummer character 第一层，
逐项就是 R1148 §10 的原
$\sum b^{r-1}\kappa(1-\zeta_p^b)\otimes\zeta_p^{\otimes(r-1)}$。
若用 primitive projector/corestriction 写法，只多一个 degree $p-1$ 的单位。
限制到 $\ker\chi_{\rm cyc}$ 在有限系数上也单射：
tame 元素的 $\omega^r-1$ 为单位，故 cyclotomic quotient 的 $H^1$ 为零。

NSW Proposition 2.2 / Lemma 2.4 的比例分母为
$(r-1)!(1-p^{r-1})$，对 $r=3,5$ 和 $p>37$ 都是单位。
因此标准 depth-one integral lattice 与原 $\gamma_r$ lattice
在模 $p$ 上互为非零倍数。R1148 的全局 rank-one 生成性及
$H^0(S_0,\mathbb Q_p/\mathbb Z_p(r))=0$ 排除了 integral $H^1$ 的 torsion，
所以两整个 lattices 的比例确为 $\mathbb Z_p^\times$，不是只在 $\mathbb Q_p$ 中非零。

由此 §2 的同一缩放满足
$$
c_3,c_5\in\mathbb Z_p^\times,\qquad
(r,s,z)=(\bar c_3a_p,\bar c_5b_p,\bar c_3\bar c_5h_p).
\tag{1152.43}
$$
不用猜它们的具体符号，也不借 Bernoulli-good 假设证明这条 lattice 身份。
因此
$$
r=0\Longleftrightarrow\beta_3=0,\quad
s=0\Longleftrightarrow\beta_5=0,\quad
z=0\Longleftrightarrow J_p+2\beta_3\beta_5=0.
\tag{1152.44}
$$

特别在 $\beta_3\beta_5\ne0$ 的原分支，(1152.24) 现在有完全有限的准确读数：
$$
\boxed{\quad
\kappa_p=\frac z{rs}
=\frac65+\frac{3J_p}{5\beta_3\beta_5}.
\quad}
\tag{1152.45}
$$
这支付了 §5 所欠的 arithmetic finite input，不再仅给一个无穷 period 表示。

将 (1152.44)/(1152.45) 代入 R1151 的全部表，给出同一原 local 三槽
$(A,B,H)$ 的完整 global compatibility：

| 有限输入 | 准确充要条件 |
|---|---|
| $\beta_3\beta_5\ne0$ | $5\beta_3\beta_5H=(6\beta_3\beta_5+3J_p)AB$ |
| $\beta_3=0,\ \beta_5\ne0,\ J_p=0$ | $A=H=0$ |
| $\beta_3=0,\ \beta_5\ne0,\ J_p\ne0$ | $A=0$，且 $B\ne0$ 或 $H=0$ |
| $\beta_3\ne0,\ \beta_5=0,\ J_p=0$ | $B=H=0$ |
| $\beta_3\ne0,\ \beta_5=0,\ J_p\ne0$ | $B=0$，且 $A\ne0$ 或 $H=0$ |
| $\beta_3=\beta_5=0,\ J_p=0$ | $A=B=H=0$ |
| $\beta_3=\beta_5=0,\ J_p\ne0$ | $A=B=0$，$H$ 任意 |

表中不再含一个未指定的 global central constant；$J_p$ 是 (1152.29) 的明确有限和。它仍不是某个固定有理数或已证非零量。

原通用八次项中还得到
$$
\frac38-\kappa_p
=-\frac{3(11\beta_3\beta_5+8J_p)}
        {40\beta_3\beta_5}.
\tag{1152.46}
$$
Gaussian/cubic 两个真正最高组合仍须把 (1152.45) 与原 $F_0$ 的
$z_{12},x_4,y_8,y_7$ 一起计算。
本篇没有证明这些组合非零或 whole $p$-disk 只剩 CM；
完整原问题继续。

## 12. 新增已刊来源与执行边界

- A. Chatzistamatiou，*On integrality of p-adic iterated integrals*，J. Algebra **474 (2017), 240–270**，DOI [10.1016/j.jalgebra.2016.11.016](https://doi.org/10.1016/j.jalgebra.2016.11.016)，[作者版](https://arxiv.org/pdf/1501.05760)。亲读 Theorem 5.3、§5.4、Corollary 5.5；本篇由其 $I_n$ 界自证正向 Frobenius 与完整 harmonic 尾项的安全约化。
- D. Jarossay，*Une notion de multizêtas finis associée au Frobenius du groupe fondamental de $\mathbb P^1\setminus\{0,1,\infty\}$*，C. R. Math. **353 (2015), 877–882**，[已刊全文](https://www.numdam.org/item/CRMATH_2015__353_10_877_0.pdf)，§2.1 定理及 §3 的 horizontal/coefficient 证明。现代正向标号按其已刊 2020 文 (1.19)；本文 §8.2 显式重述 $N=1$ 的系数、空交叉项与符号，未消费未刊一般计算公式。
- H. Furusho，*Double shuffle relation for associators*，Ann. of Math. **174 (2011), 341–360**，[期刊全文](https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n1-p09-p.pdf)，Theorem 0.2、Corollary 0.3 及 (1.4)–(1.5)。本篇只用其 infinitesimal weight-five relations；四个线性方程及全部词/导数读数在 §§9–10 自证。该文的群乘法 convention 与本文顺序相反不影响所用 infinitesimal coefficient identities；实际 bracket 与 exponential 始终由 (1152.12)/(1152.19) 自行计算。

root 与 o1 分别纸读两个 weight-eight 词，并交叉核完整表。
全部新结论均为纸面推导；没有执行数学程序或重扫旧 prime 窗口。


## 13. 同一原 Soulé 规范的绝对中央坐标

现在固定 §3 的 Ihara 群律及原 compatible Tate generators，
进一步消去 §2 暂留的两个缩放。这里需要比较实际 Galois action，
不能只在 $r,s$ 已知非零时倒除两个局部数。

### 13.1 路径、逆共轭与两个准确阶乘

采用 NSW（2017）§2.1、(2.4) 的定义：
对标准路径 $\gamma$，令
$$
\gamma=f_\sigma\cdot\sigma(\gamma),\qquad
\log f_\sigma\equiv
-\sum_{r\ge1}\ell i_r(1)(\sigma)\operatorname{ad}_X^{r-1}Y
\quad\bmod(\operatorname{depth}\ge2).
\tag{1152.47}
$$
在基本群中由此有
$$
\sigma(x)=x^{\chi(\sigma)},\qquad
\sigma(y)=f_\sigma^{-1}y^{\chi(\sigma)}f_\sigma.
$$
也就是说，同一标准 $X=\log x,Y=\log y$ 下的作用是
**逆共轭**，与 (1152.12) 完全相同。其乘法次序也可直接核准：
$f_{\sigma\tau}=f_\sigma\sigma(f_\tau)$；
在 $\ker\chi$ 上代入上式，正是
$$
f_{\sigma\tau}
=f_\sigma(X,Y)\,
 f_\tau(X,f_\sigma^{-1}Yf_\sigma)
=f_\sigma\circ f_\tau .
\tag{1152.48}
$$
因此这里用的是 $f_\sigma$，不是它的普通 inverse 或 Ihara inverse。
群胚的路径书写顺序若换约定，必须连同上述逆共轭身份一起运输；
不能只将 (1152.47) 的负号删掉。
两切向点在 $1$ 处若用相反的单位切向量，其差为 $-1$ 的
$p$-primary Kummer 类，因 $p$ 为奇数而为零。
原 Tate generators 没有另作 rescaling。

NSW Proposition 2.2 / Lemma 2.4 对奇数 $r=3,5$ 给
$$
\ell i_r(1)|_{\ker\chi}
=\frac{\gamma_{r,\infty}|_{\ker\chi}}
       {(r-1)!\,(1-p^{r-1})}.
\tag{1152.49}
$$
其 (2.11) 是原加权 Kummer product 本身，
没有再除 $p-1$：§11 中 projector/corestriction 的单位说明，
在这里由所固定的未平均加权和取代。
原 $\gamma_r$ 的第一层正是 R1148 (1148.27) 及其权五版本。

$\sigma_r$ 的 depth-one 系数规范为一，所以 (1152.47)–(1152.49)
直接读取该 mixed Tate quotient 的两个 abelian Galois classes：
$$
-\frac{\gamma_{3,\infty}}{2!(1-p^2)},\qquad
-\frac{\gamma_{5,\infty}}{4!(1-p^4)}.
$$
restriction 的单射已在 §11 支付；因而这些是整个 $S_0$ 上的
同一类，非只在 cyclotomic kernel 上的数值身份。
反除 $p$ 后的 Betti/de Rham fibre-functor comparison 保同一
Tate generators，且任何 unipotent path 变换在 abelianization 上
只是 coboundary，不改变上述两个系数。

因此 (1152.10) 的实际缩放准确为
$$
\boxed{\quad
c_3=-2(1-p^2),\qquad
c_5=-24(1-p^4).
\quad}
\tag{1152.50}
$$
先在 global classes 上确定它们，才作 localization；
没有用一个可能为零的局部值测定线性映射。
原 global central $H^1$ 为零，所以这两个准确 abelian
identifications 同样锁定整个 Heisenberg lift，
第三槽仍乘 $c_3c_5$，不能另加一个中央常数。

### 13.2 三个绝对有限读数及真实中央差

将 (1152.50) 约化，并用 (1152.38)/(1152.42)，得到
$$
\boxed{\quad
r=\frac23\beta_3,\qquad
s=\frac{24}{5}\beta_5,\qquad
z=\frac{48}{25}(J_p+2\beta_3\beta_5).
\quad}
\tag{1152.51}
$$
这些公式不要求 $\beta_3\beta_5\ne0$。
它们是在 R1151 原 Tate frame 内的实际坐标；
(1152.45) 的比值和 §11 全部七分支表均保持不变。

令 $\mathcal B=\beta_3\beta_5$。则对任意实际 local 三槽，
原 subtraction polynomial 有准确尺度
$$
\mathcal D=rs\,\mathsf h-z\,\mathsf a\mathsf b
=\frac{16}{25}
 \left(5\mathcal B\mathsf h-3(J_p+2\mathcal B)\mathsf a\mathsf b\right).
\tag{1152.52}
$$
当 $\mathcal B=0$ 时，这一多项式等式仍然成立，
但其零集不能替代 §11 完整分支表。

具体地，原 Gaussian/cubic 最高项现在分别为
$$
\boxed{\quad
[T^3]\mathcal D
=\frac{256}{25}\delta^3c_g^6
 \left(5\mathcal Bz_{12}-3(J_p+2\mathcal B)x_4y_8\right),
\quad}
\tag{1152.53}
$$
$$
\boxed{\quad
[T^2]\mathcal D
=\frac{256}{25}\delta^3c_g^6
 \left(5\mathcal Bz_{12}
       -\frac12(J_p+2\mathcal B)\lambda A_*y_7\right).
\quad}
\tag{1152.54}
$$
通用八次项的同一因子则为
$$
\frac{3rs}{8}-z
=-\frac6{25}(11\mathcal B+8J_p).
\tag{1152.55}
$$
这些均仅为原已经存在的 subtraction 的准确有限读数，
不是其非零性。

### 13.3 对真实 Miller 校准单位的严格后果

为与 R1153 直接对接，记其实际单位
$$
\eta_\star=U_\star\gamma_\star^{-2}\in\mathbb F_p^\times.
$$
将 (1152.51) 与 R1153 (1153.24) 比较，只能无条件得到
$$
\boxed{\quad
(\eta_\star-1)\beta_3=0,\qquad
(\eta_\star^2-1)\beta_5=0.
\quad}
\tag{1152.56}
$$
特别：

- $\beta_3\ne0$ 时，$\eta_\star=1$，
  故所有原 reference 的 $U_E=\gamma_E^2$。
- $\beta_3=0,\ \beta_5\ne0$ 时，先只有 $\eta_\star=\pm1$。
  若再有 $p\equiv3\pmod4$，则仍有 $\eta_\star=1$：
  R1153 给 $U_\star=4\delta c_{g,\star}^2\beta_\star^2$，
  $\delta$ 为非平方；而
  $(\gamma_\star^2)^{(p-1)/2}
   =\gamma_\star^{p-1}=-1$，
  所以 $\eta_\star$ 是平方。
  此时 $-1$ 为非平方，便排掉负号。
- 两个 $\beta$ 同零时，(1152.56) 不检测该单位；
  原 R1153 的实际 Miller 公式继续完整使用。

这最后一项边界是必需的：即使局部 $H^1$ 是一维，
一个已经消失的局部 global class 也不能用来标定这条整线。
本节没有宣称在全部 bad 分支已付普遍 principal-polarization
标量比较。中央 $z_{12}$、较低中央项及 whole $p$-disk 的
排除继续；无数学程序执行。
