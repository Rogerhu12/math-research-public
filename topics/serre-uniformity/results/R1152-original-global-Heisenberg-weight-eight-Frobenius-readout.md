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
