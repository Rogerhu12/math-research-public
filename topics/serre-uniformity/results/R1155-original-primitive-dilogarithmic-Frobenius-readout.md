# R1155：原单位方程的 dilogarithm 坐标与整 Frobenius 读数

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇沿 R1133 的同一原根代数，固定路径方向后计算它的局部 de Rham / Frobenius 中央槽。结果分别注明：未分歧算术 fibre 的 Bloch–Kato 坐标、通用三穿孔直线的 Frobenius 矩阵、以及原 supersingular torsion 单位的实际代入。通用 Frobenius 从 $u^p$ 的 fibre 到 $u$ 的 fibre；将它改成同一算术 fibre 的 Frobenius，必须保留运输项。

## 1. 原根代数到标准 Heisenberg 的方向

令
$$
\mathcal H(a,b,h)=
\begin{pmatrix}1&a&h\\0&1&b\\0&0&1\end{pmatrix},\qquad
(a,b,h)(a',b',h')=(a+a',b+b',h+h'+ab').
\tag{1155.1}
$$
权为 $1,1,2$，同一个 Tate generator 依次运输这三个坐标。

R1133 §11 已付原
$$
\alpha^p=u,\quad \beta^p=1-u,\quad
\Gamma^p=\prod_{i=0}^{p-1}(1-\zeta_p^i\alpha)^i
$$
以及切向 leading 为一的根规范。其函数域自同构写
$g=\tau^b\sigma^a\nu^h$，真实 ordered 坐标满足
$$
h-\frac12ab=-\ell i_2^{\rm NW}(u),\qquad
a=\rho_u,\quad b=\rho_{1-u}.
\tag{1155.2}
$$
这里不能直接将 NW 的 complex $li_2$ 字面换成 Coleman $\operatorname{Li}_2$，因为两套路径的复合次序相反。

具体令 $\mathrm{rev}$ 为将 NW 左至右的路径复合改成 Furusho 右至左复合的反同态。它保持两个一次生成元，但
$$
\mathrm{rev}(X)=A,\qquad
\mathrm{rev}(Y)=B,\qquad
\mathrm{rev}([X,Y])=-[A,B].
\tag{1155.3}
$$
若 NW 的路径为 $\gamma$，同一路径在 Furusho 记号中为 $b_u$，则
$$
f_\sigma^{\rm NW}=\gamma\,\sigma(\gamma)^{-1},
\qquad
\mathrm{rev}(f_\sigma^{\rm NW})
 =\sigma(b_u)^{-1}b_u
 =(b_u^{-1}\sigma(b_u))^{-1}.
\tag{1155.4}
$$
因此
$$
\log(f_\sigma^{\rm NW})^{-1}
 =aX+bY+\ell i_2^{\rm NW}[X,Y]
$$
准确变成
$$
\log(b_u^{-1}\sigma(b_u))
 =aA+bB-\ell i_2^{\rm NW}[A,B]
 \pmod{\Gamma^3}.
\tag{1155.5}
$$
其标准 Heisenberg ordered 中央槽正是 (1155.2) 的 $h$。首层没有交换；中央也没有任意改号。

这同时说明原有限根代数是同一 pointed class-two path torsor 的模 $p$ 商。NW 的整 Kummer characters 在所有 $p^n$ 层的相容性给其原 $p$-adic class-two 提升；这里只用 class two 的 $1/2$，不引入 $p$ 分母。

## 2. 原良好单位 fibre 的晶体性和 Bloch–Kato 坐标

令 $F/\mathbb Q_p$ 为有限扩张，$p>3$，且
$u,1-u\in\mathcal O_F^\times$。把上一节的原整 torsor 张量到
$\mathbb Q_p$，其系数组为
$$
1\longrightarrow\mathbb Q_p(2)\longrightarrow
\mathcal H_{\mathbb Q_p}\longrightarrow
\mathbb Q_p(1)^2\longrightarrow1.
\tag{1155.6}
$$

这个实际 rational torsor 是 crystalline，理由可不借分歧域上的 Fontaine–Laffaille：

- 两个一次 quotient 都是单位的 Kummer classes，故在
  $H_f^1(F,\mathbb Q_p(1))$。
- $H^0(F,\mathbb Q_p(2))=H^0(F,\mathbb Q_p(-1))=0$；
  local Euler characteristic 与 Bloch–Kato 维数式给
  $H^1(F,\mathbb Q_p(2))=H_f^1(F,\mathbb Q_p(2))$。
- Sakugawa 的 non-abelian exponential 适用于这个 split unipotent group。
  它的 Lie filtration weights 为 $-1,-1,-2$，coordinate algebra 非负，
  $F^0\mathcal H=1$；$\varphi^f-1$ 在两次一次槽及中心均可逆，
  所以 Lang map 为逐中心解出的 polynomial isomorphism。
  其 Theorems 3.9–3.10 因而给每个 crystalline abelian pair 一个
  crystalline lift，并保持中心作用。
- 原 lift 与该 lift 相差一个 $H^1(F,\mathbb Q_p(2))$ 类，
  该类亦 crystalline，所以原 lift 本身 crystalline。

这是同一原 rational torsor 的结论，不把分歧底的 integral lattice 识别一并偷渡。

现在另设 $F/\mathbb Q_p$ **未分歧**。Sakugawa Theorem 5.4 与
Proposition 5.6，以及 Furusho Theorem 2.3，在 (1155.3)–(1155.5)
固定的同一 frame 中给
$$
\boxed{\quad
G(u)=\log_{\mathcal H}^{\rm BK}(\mathscr D_u)
 =\mathcal H\bigl(\log_pu,\ \log_p(1-u),\
                         -\operatorname{Li}_2^p(u)\bigr).
\quad}
\tag{1155.7}
$$
这里的 $\log_{\mathcal H}^{\rm BK}$ 取值于群，而不是普通 Lie logarithm；
故其 Lie 中央槽为
$-\operatorname{Li}_2^p(u)-\log_pu\log_p(1-u)/2$。

也能直接从 KZ 方程核出第三槽：
$$
dG=\left(A\,\frac{du}{u}+B\,\frac{du}{u-1}\right)G.
$$
若 $a=\log_pu,\ b=\log_p(1-u)$，则
$dh=b\,da$，而
$d(-\operatorname{Li}_2^p(u))=\log_p(1-u)\,du/u$。
切向常数为零，因而得到 (1155.7) 的负号及完整 ordered 槽。
这与 (1155.5) 相容。

## 3. 同一 $\mathbb Q_p$ fibre 的实际 Frobenius

本节设 $u\in\mathbb Z_p$，且 $u(1-u)$ 为单位。
以原 Hodge 点 $p_d$ 和唯一 Frobenius 固定点 $p_c$ 记
$$
p_c=p_dG(u).
$$
这是 Sakugawa Proposition 3.2 的方向。令 $\Phi(p_d)=p_dR$；
在三个 Tate 系数上 $\Phi$ 分别乘 $p^{-1},p^{-1},p^{-2}$。
于是
$$
R=G(u)\,\Phi(G(u))^{-1}.
\tag{1155.8}
$$
写 $a=\log_pu,\ b=\log_p(1-u),\ L=\operatorname{Li}_2^p(u)$，
直接按 (1155.1) 相乘得
$$
\boxed{
R=\mathcal H\left(
 (1-p^{-1})a,\ (1-p^{-1})b,\
 -(1-p^{-2})L+(p^{-2}-p^{-1})ab
\right).
}
\tag{1155.9}
$$
所以原中央 Frobenius 槽不是单独的
$-(1-p^{-2})L$。即使两个一次槽都已知，仍必须保留显示的
$(p^{-2}-p^{-1})ab$。

该公式目前按 $\mathbb Q_p$ 的 coefficient Frobenius 写出。
对一般未分歧 $F$ 要保留其 coefficient Frobenius；
对分歧 $F$ 更不能把不存在的 canonical $F$-Frobenius 填入此式。

## 4. 从 $u^p$ 到 $u$ 的通用 Frobenius 矩阵

记
$$
\operatorname{Li}_r^\dagger(u)
 =\operatorname{Li}_r^p(u)-p^{-r}\operatorname{Li}_r^p(u^p)
 \quad(r=1,2).
\tag{1155.10}
$$
它们是 Coleman 的 overconvergent polylogarithms。
Furusho 的 Theorem 2.14、Lemma 2.15 及 Example 2.16 给原 KZ
path object 的 Frobenius：
$$
R^\dagger(u)=
G(u)\,
G\left(p^{-1}A,\
 (\Phi_{\rm De}^p)^{-1}p^{-1}B\Phi_{\rm De}^p;\ u^p\right)^{-1}.
\tag{1155.11}
$$
在 class two 中 $\Phi_{\rm De}^p$ 没有一次项，所以对 $B$ 的
共轭只在 class three 才贡献。记 $a'=\log_p(u^p)=pa$、
$b'=\log_p(1-u^p)$。乘积的中央交叉项准确为
$p^{-2}a'b'-p^{-1}ab'=0$。故
$$
\boxed{\quad
R^\dagger(u)=
\mathcal H\left(0,\
 -\operatorname{Li}_1^\dagger(u),\
 -\operatorname{Li}_2^\dagger(u)\right).
\quad}
\tag{1155.12}
$$
这是真正从 $u^p$ fibre 到 $u$ fibre 的 relative Frobenius，
与 (1155.9) 的同点算术 Frobenius 区别明确。前者第一槽恒零，
后者第一槽一般非零，已足以看出不能互代。

(1155.11) 是整条 rigid analytic 域上的函数恒等式，
所以 (1155.12) 可以在任意有限 $F/\mathbb Q_p$ 的良好单位点
代入；这一步是对通用 crystalline path object 的求值，不声称
对分歧原格使用了 Fontaine–Laffaille。

## 5. 保留分歧 nilpotents 的准确有限 polylogarithm

定义
$$
\ell_{r,p}(U)=\sum_{j=1}^{p-1}\frac{U^j}{j^r}
 \in\mathbb Z_p[U]\qquad(r=1,2).
\tag{1155.13}
$$
对于任意有限 $F/\mathbb Q_p$ 及
$u,1-u\in\mathcal O_F^\times$，有强整同余
$$
\boxed{\quad
\operatorname{Li}_r^\dagger(u)
 \equiv\frac{\ell_{r,p}(u)}{1-u^p}
 \pmod{p\mathcal O_F}.
\quad}
\tag{1155.14}
$$
这里模的是 $p\mathcal O_F$，不是只模 $\mathfrak m_F$。
当 $F$ 分歧时，$u$ 在 $\mathcal O_F/p$ 中的 nilpotent
部分全部保留。

给出全尾证明，避免在 $|u|=1$ 处非法求和。
令整数多项式 $P_m(T)$ 由
$$
\sum_{k\ge0}k^mT^k=\frac{P_m(T)}{(1-T)^{m+1}}
$$
定义；$P_0=1$，递推
$
P_{m+1}=T\bigl((1-T)P_m'+(m+1)P_m\bigr)
$
证明全部 $P_m\in\mathbb Z[T]$。
在 $|u|<1$ 按 $n=j+pk$ 展开，得到
$$
\operatorname{Li}_r^\dagger(u)=
\sum_{j=1}^{p-1}\frac{u^j}{j^r}
 \sum_{m\ge0}(-1)^m\binom{r+m-1}{m}
 \left(\frac pj\right)^m
 \frac{P_m(u^p)}{(1-u^p)^{m+1}}.
\tag{1155.15}
$$
在 $|u|\le1,\ |1-u|=1$ 的 affinoid 上，
$|1-u^p|=1$，每个 $m$ 项的 norm 至多 $p^{-m}$；
二项式系数及 $P_m$ 都是整数。
所以内和一致收敛，并给有界 rigid analytic 函数。
它与原 $\operatorname{Li}_r^\dagger$ 在 $|u|<1$ 相等，
由解析延拓在该 affinoid 上相等。删去 $m\ge1$ 的完整
$p$-整尾即得 (1155.14)。

特别，原 relative Frobenius 的三个有限槽准确为
$$
\boxed{\quad
R^\dagger(u)\equiv
\mathcal H\left(
0,-\frac{\ell_{1,p}(u)}{1-u^p},
  -\frac{\ell_{2,p}(u)}{1-u^p}
\right)\pmod{p\mathcal O_F}.
\quad}
\tag{1155.16}
$$

若 $u_0\in\mathbb Z_p^\times$ 是非一的 Teichmüller 点，
则 $u_0^p=u_0$、$\log_pu_0=0$，两种 Frobenius 在此点一致。
(1155.10)、(1155.14) 因而还给
$$
\operatorname{Li}_2^p(u_0)\in p^2\mathbb Z_p,\qquad
\frac{\operatorname{Li}_2^p(u_0)}{p^2}
 \equiv-\frac{\ell_{2,p}(\bar u_0)}{1-\bar u_0}
 \pmod p .
\tag{1155.17}
$$
一般 $u\in u_0+p\mathbb Z_p$ 有
$\log_pu,\log_p(1-u)\in p\mathbb Z_p$；
沿该盘积分
$d\operatorname{Li}_2^p=-\log_p(1-u)\,du/u$
可见 $\operatorname{Li}_2^p(u)\in p^2\mathbb Z_p$：一次项含
$\log_p(1-u_0)(u-u_0)$，其赋值至少二；其余 $n$ 次项的分母
至多引入 $v_p(n(n-1))$，而 $n-v_p(n(n-1))\ge2$（$n\ge2,p>3$）。
所以 (1155.9) 的三个槽都整，不能因形式含 $p^{-2}$ 就
丢弃乘积修正，也不能据整性改换指定格。

## 6. 原 supersingular torsion 单位真的落在上述域

回到 R1133 的实际 Weierstrass 曲线 $E/F$，假设良好 supersingular
约化，$p>5$。令 $P\ne0$ 为原 $p$-torsion 点，
$3\le a\le(p-1)/2$，并取其原单位方程
$$
U_a(P)=\frac{x(aP)-x(2P)}{x(aP)-x(P)},\qquad
W_a(P)=\frac{x(2P)-x(P)}{x(aP)-x(P)}=1-U_a(P).
\tag{1155.18}
$$
可在含 $P$ 的有限分歧扩张 $L/F$ 中计算，但不把 $L$
误称未分歧。

Supersingular 特殊纤维的 $E[p]$ 只有一个几何点，
故所有这些 $P$ 都约化到原点。对整 formal parameter $t$，
$$
x(t)=t^{-2}+\text{较高阶整项},\qquad
[a]t=at+\text{较高阶整项}.
$$
因此
$$
t(P)^2\bigl(x(aP)-x(bP)\bigr)
 \equiv a^{-2}-b^{-2}\pmod{\mathfrak m_L}
$$
对这里的 $a,b=1,2$ 成立。范围排除了
$a^2=1,4\pmod p$，所以
$$
\boxed{\quad
U_a(P),W_a(P)\in\mathcal O_L^\times,\quad
\overline U_a(P)=\frac{a^2-4}{4(a^2-1)},\quad
\overline W_a(P)=\frac{3a^2}{4(a^2-1)}.
\quad}
\tag{1155.19}
$$
这是真实原输入的良好单位检验；没有把 torsion 点替成另一条
不相干的 ordinary 曲线或只在 $\mathbb F_{p^2}$ 上的点。

所以对原每个 primitive $D(U_a(P))$，(1155.16) 可按原
$U_a(P)\in\mathcal O_L/p$ 逐项代入，读出其通用 Frobenius
中央函数。只有进一步约模 $\mathfrak m_L$ 时才可将
$U_a(P)$ 换成 (1155.19) 的常数。
先这样换常数再做原 weighted trace 会丢掉 nilpotent 项，
不能恢复原 $F_0$ 的 $z_{12}$。

## 7. 与原全局中央槽的接口

本篇已付：

1. 原 $D(\alpha)$ 与标准 Heisenberg path torsor 的准确方向；
2. 良好单位的 actual rational fibre 晶体性；
3. 未分歧 fibre 的指定 Bloch–Kato 坐标和 $\mathbb Q_p$
   同点 Frobenius 的全部乘积修正；
4. 原通用 Frobenius 中央函数的完整 mod $p\mathcal O_L$
   finite-polylogarithm 读数，以及 supersingular 原输入的单位性。

下一项实际计算仍在原对象内进行：把 R1133 的指定四线/Manin
组合与所有 finite transfer 做完，再运输到 R1147–50 的规范
moment frame，读取 $F_0$ 的 $\mu^{12}\tau_1^2$ 槽。
R1133 §11 的逐陪集乘积、不同 Norm 之间的交叉项以及上述
$u^p\to u$ 的运输都必须保留。
(1155.16) 本身不等于已经完成这个 $z_{12}$ 计算。

## 已刊 primary 与精确使用范围

- H. Nakamura–Z. Wojtkowiak，*Tensor and homotopy criteria for functional
  equations of $\ell$-adic and classical iterated integrals*，
  LMS Lecture Note Series 393 (2012), 258–310，
  [作者全文](https://math.univ-cotedazur.fr/~wojtkow/11NakamuraWojtkowiak.pdf)，
  §4.2 (4.9)、§5.1–5.2、(5.2)–(5.3) 与 (6.12)。
  原同根比较由 R1133 §11 支付；本篇另写路径反同态。
- H. Furusho，*p-adic multiple zeta values II: Tannakian interpretations*，
  Amer. J. Math. 129 (2007), 1105–1144，
  DOI 10.1353/ajm.2007.0024，
  [作者稿](https://arxiv.org/pdf/math/0506117)，
  Theorem 2.3、Theorem 2.14、Lemma 2.15、Example 2.16 及 §2.3。
  本篇只取 class two，并显示其完整矩阵乘法。
- K. Sakugawa，*On a non-abelian generalization of the Bloch–Kato exponential
  map*，Math. J. Okayama Univ. 59 (2017), 41–70，
  [全文](https://www.math.okayama-u.ac.jp/mjou/mjou59/_04_Sakugawa.pdf)，
  Proposition 3.2、Theorems 3.9–3.10、Theorem 5.4、
  Proposition 5.6。最后一个命题的未分歧前提明确保留。
- Bloch–Kato 的单位 Kummer 子空间、维数式及 local duality
  沿 R1147 §15 已定位来源。分歧底仅用 rational comparison，
  未使用未分歧的 integral Fontaine–Laffaille 等价。

本篇全部为纸面推导；没有数学程序执行。
