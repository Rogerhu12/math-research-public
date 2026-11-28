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


## 8. 改变 Frobenius 提升的完整运输与实际同点有限读数

本节支付 §4–7 中一个具体运输，而不是将两个不同 fibre 的
Frobenius 直接等同。设 $p>3$，$L/\mathbb Q_p$ 为任意有限扩张，
$u,1-u\in\mathcal O_L^\times$，并取
$$
z=u^p,\qquad v=z+p\varepsilon,\qquad \varepsilon\in\mathcal O_L.
\tag{1155.20}
$$
故 $z,z-1,v,v-1$ 都是单位。任意这样的 $v$ 都可用于
同一通用 KZ object 的 fibre 间运输；只有在下文 §8.3 的
未分歧算术情形，才将 $v$ 取成 coefficient Frobenius 的实际像。

### 8.1. 精确短运输与全尾整性

在同一 (1155.7) 的通用 de Rham frame 中，置
$$
H(z,v)=G(z)G(v)^{-1},\qquad
D_p\mathcal H(a,b,h)=\mathcal H(p^{-1}a,p^{-1}b,p^{-2}h).
$$
$D_p$ 是 (1155.1) 的群同态。
写 $\delta=v-z=p\varepsilon$，则
$$
\begin{aligned}
a_H&=-\log_p(1+\delta/z),\\
b_H&=-\log_p(1+\delta/(z-1)),\\
h_H&=\operatorname{Li}_2^p(v)-\operatorname{Li}_2^p(z)
       +(\log_pv-\log_pz)\log_p(1-v).
\end{aligned}
\tag{1155.21}
$$
最后一项来自 ordered 群律中的 $ab'$，不能去掉。

在 $|\delta|\le|p|$ 的整个盘内，中央项还有一个不含
任何未定 Coleman 常数的绝对收敛式：
$$
\boxed{\quad
h_H=\sum_{n\ge2}\frac{(-1)^n\delta^n}{n}
       \sum_{r=1}^{n-1}
       \frac{1}{r z^r(z-1)^{n-r}}.
\quad}
\tag{1155.22}
$$
确实，以 $v$ 为变量对 (1155.21) 求导，得
$$
\frac{d h_H}{dv}=\frac{\log_p(v/z)}{v-1},\qquad h_H(z,z)=0.
$$
展开 $\log(1+\delta/z)$ 及 $(z-1+\delta)^{-1}$，
逐项积分正好给 (1155.22) 的 $nr$ 分母及 $(-1)^n$。
这也直接说明没有一次中央项。

全部估值都以 $v_p(p)=1$ 计，不把分歧域的 uniformizer
当成 $p$。对 $n\ge2$，
$n-1-v_p(n)\ge1$，所以两条 logarithm 除 $p$ 后，
$n\ge2$ 的全部尾都在 $p\mathcal O_L$。
对 (1155.22) 的 $n\ge3$，$nr\mid n!$，故
$$
n-2-v_p(nr)\ \ge\ n-2-v_p(n!)\ \ge1.
$$
最后一步由 $v_p(n!)\le(n-1)/(p-1)$ 及整值性成立，
包含 $n=3$ 的端点。因此这是除 $p^2$ 后的完整尾界，
没有只截掉形式上的三次及更高项而不核其分母。
得到
$$
\boxed{\quad
D_pH(z,v)\equiv
\mathcal H\left(
-\frac{\varepsilon}{z},\
-\frac{\varepsilon}{z-1},\
\frac{\varepsilon^2}{2z(z-1)}
\right)\pmod{p\mathcal O_L}.
\quad}
\tag{1155.23}
$$

### 8.2. 换提升后的完整 Frobenius 三槽

把从 $v$ 的 fibre 到 $u$ 的 Frobenius/运输组合记为
$$
R_v(u)=G(u)D_pG(v)^{-1}.
$$
沿 (1155.11) 的同一 class-two quotient，精确因子次序为
$$
\boxed{\quad
R_v(u)=R^\dagger(u)\,D_pH(u^p,v).
\quad}
\tag{1155.24}
$$
这是右侧运输。结合 (1155.16) 与 (1155.23)，由于
$R^\dagger$ 的第一槽准确为零，乘积没有另一个遗漏的中央
cross term。令所有显示量在 $\mathcal O_L/p\mathcal O_L$ 中读取，
则
$$
\boxed{\begin{aligned}
a_v&=-\frac{\varepsilon}{u^p},\\
b_v&=\frac{\varepsilon-\ell_{1,p}(u)}{1-u^p},\\
h_v&=-\frac{\ell_{2,p}(u)}{1-u^p}
      -\frac{\varepsilon^2}{2u^p(1-u^p)}.
\end{aligned}}
\tag{1155.25}
$$
因此改提升的二次修正除 $p^2$ 后一般不消失。
其 BCH 中央坐标则为
$$
\boxed{\quad
h_v-\frac12a_vb_v
=-\frac{\ell_{2,p}(u)}{1-u^p}
 -\frac{\varepsilon\,\ell_{1,p}(u)}
        {2u^p(1-u^p)}.
\quad}
\tag{1155.26}
$$
这里两个 $\varepsilon^2$ 恰相消；
这不是在 ordered 坐标中删除二次项。

(1155.23)–(1155.26) 是强模 $p\mathcal O_L$ 身份，
保留 $u,\varepsilon$ 的全部 nilpotent 部分。
它们也逐点适用于一个实际整函数提升
$v=\psi(u)\equiv u^p\bmod p$。
若原输入只有 $v\equiv u^p\bmod\mathfrak m_L$，
则没有这里的尾界，不能使用本式；
同样，任意挑出的 $v$ 不会因此变成分歧域上的
canonical field Frobenius。

### 8.3. 全部未分歧 fibre 的同一点算术 Frobenius

现设 $L=F/\mathbb Q_p$ 未分歧，并令 $\sigma_F$ 为其
arithmetic Frobenius，即模 $p$ 的 $p$ 次幂提升。取
$$
v=\sigma_F(u),\qquad
\varepsilon_F(u)=\frac{\sigma_F(u)-u^p}{p}\in\mathcal O_F.
\tag{1155.27}
$$
由 §2 的同一 arithmetic comparison 及 universal KZ
object 的 $\mathbb Q_p$ 定义，
$G(\sigma_Fu)=\sigma_F(G(u))$。
所以 (1155.24) 此时准确是
$$
R_F(u)=G(u)\,D_p\sigma_F(G(u))^{-1},
\tag{1155.28}
$$
也就是同一原 arithmetic fibre 相对 Hodge 点的 Frobenius。
所有 coefficient-semilinear 项均保留。
(1155.25) 给其完整有限矩阵，并从右边的两个实际整因子
证明 $R_F(u)\in\mathcal H(\mathcal O_F)$。
没有为分歧 full-level 域声称同样的算术比较，也没有将
这个矩阵的整性直接升级为任意指定 lattice 的 FL 识别。

特别当 $F=\mathbb Q_p$ 时，定义
$$
q_p(w)=\frac{w^{p-1}-1}{p}\in\mathbb Z_p
\qquad(w\in\mathbb Z_p^\times).
$$
这里允许 $p$-adic 单位 $w$，不只整数代表。
因为 $\varepsilon(u)=-u q_p(u)$，有
$$
\boxed{\quad
R_{\mathbb Q_p}(u)\equiv
\mathcal H\left(
 q_p(u),\
 q_p(1-u),\
 -\frac{\ell_{2,p}(\bar u)}{1-\bar u}
 -\frac{\bar u}{2(1-\bar u)}q_p(u)^2
\right)\pmod p .
\quad}
\tag{1155.29}
$$
两条 Fermat quotient 在右边也约模 $p$。
第二槽可直接核准：整数多项式
$$
\frac{1-U^p-(1-U)^p}{p}\equiv\ell_{1,p}(U)\pmod p
$$
给
$\ell_{1,p}(\bar u)\equiv
-uq_p(u)-(1-u)q_p(1-u)$。
因而 (1155.25) 的第二槽确为 $q_p(1-u)$，
未另换 Kummer 符号。

(1155.29) 同时与 §3 的完整
$-(1-p^{-2})\operatorname{Li}_2^p
 +(p^{-2}-p^{-1})\log u\log(1-u)$ 相容；
本节给的是该实际同点读数的有限式。
其对 $u\bmod p^2$ 的依赖也已显式保留，
不是仅用 $\bar u$ 替代原 torsor。

后继指定四线/Manin组合现在可先识别每个实际
$\psi(u)$，再用 (1155.25) 保留其提升误差和二次修正；
尚未给出的原 moment 填充、全部 transfer 与
$F_0$ 的 $z_{12}$ 仍按 §7 继续。
本节为纸面推导；root 固定乘法方向并核全尾估值，
o1_theta 独立核 (1155.21)–(1155.26) 的中央导数、
$n r$ 分母及全部符号。没有数学程序执行。


## 9. 同一有限 Frobenius 的完整六种参数变换

本节在任意 $\mathbf F_p$-代数 $A$ 上工作，允许 $A$ 含 nilpotents；
仍设 $p>3$，并要求 $u,1-u$ 为单位。把 (1155.25) 的有限
矩阵写成 $\mathcal R(u,\varepsilon)$。
以下证明它对两个实际变换 $u\mapsto1-u$、$u\mapsto u^{-1}$
的完整相容性，保留原 ordered 中央坐标。

### 9.1. 所需有限多项式身份

令 $l_r(U)=\ell_{r,p}(U)\bmod p$。整数二项式及指标反转给
$$
l_1(1-U)=l_1(U),\qquad
l_r(U)=(-1)^r U^p l_r(U^{-1})\quad(r=1,2).
\tag{1155.30}
$$
第一式可直接从 §8.3 的
$(1-U^p-(1-U)^p)/p$ 约化得到；第二式将 $j$ 换成 $p-j$，
所以是在 $\mathbf F_p[U,U^{-1}]$ 中的身份。

还需要保留 Frobenius 幂的二次身份：
$$
\boxed{\quad
l_1(U)^2+2U^p l_2(U)
       +2(1-U^p)l_2(1-U)=0
       \quad\text{于 }\mathbf F_p[U].
\quad}
\tag{1155.31}
$$
这里没有把 $U^p$ 换成 $U$。
证明如下。$l_2'=l_1/U$，
$l_1'=(1-U^{p-1})/(1-U)$；
配上 (1155.30)，显示左边的导数为零。
最高的 $U^{2p-1}$ 项相消，故次数至多 $2p-2$，
于是该多项式只可能为 $a+bU^p$。
$U=0,1$ 的值都为零，因为
$\sum_{j=1}^{p-1}j^{-1}=\sum_{j=1}^{p-1}j^{-2}=0$。
因此 $a=b=0$，包括导数检测不到的 $U^p$ 项也已支付。

### 9.2. 提升误差的实际变换

若 $\varepsilon$ 来自 §8 的实际
$v=u^p+p\varepsilon$，则补参数与逆参数的原像分别为
$1-v$ 与 $v^{-1}$，而不是另选的两个提升。
约模 $p$，它们的提升误差准确为
$$
\boxed{\quad
S:(u,\varepsilon)\longmapsto
       (1-u,l_1(u)-\varepsilon),\qquad
J:(u,\varepsilon)\longmapsto
       (u^{-1},-\varepsilon/u^{2p}).
\quad}
\tag{1155.32}
$$
第一式消费
$1-u^p-(1-u)^p=p\,C_p(u)$、$C_p\bmod p=l_1$；
第二式使用实际 $v^{-1}-u^{-p}=-p\varepsilon/(u^pv)$。
因此两式保留了全部 Frobenius carry，不是仅在 residue points 上验证。

令 $\mathcal R(u,\varepsilon)=\mathcal H(a,b,h)$，
将 (1155.30)–(1155.32) 代入 (1155.25)，得到
$$
\boxed{\begin{aligned}
\mathcal R(1-u,l_1(u)-\varepsilon)
   &=\mathcal H(b,a,ab-h),\\
\mathcal R(u^{-1},-\varepsilon/u^{2p})
   &=\mathcal H(-a,b-a,-h+a^2/2).
\end{aligned}}
\tag{1155.33}
$$
例如第一行的中央差乘 $u^p(1-u^p)$ 后，恰是
$-(1-u^p)l_2(1-u)-u^p l_2(u)-l_1(u)^2/2$；
(1155.31) 将它完整消去。
第二行只需两条反转式；它的 $a^2/2$ 不能省去。

在 BCH 中央坐标 $k=h-ab/2$ 下，这两个群自同构分别为
$$
S:(a,b,k)\mapsto(b,a,-k),\qquad
J:(a,b,k)\mapsto(-a,b-a,-k).
$$
它们满足 $S^2=J^2=(SJ)^3=1$，
所以 (1155.33) 给全部六种 Möbius 参数变换的同一有限读取。
第一行正是 R1133 (1133.67) 交换两个原 Kummer 槽并反转中心的
群映射；本节在 Frobenius realization 中明确保留其提升误差，
没有从 cup 的反对称性猜一个中央符号。

这些都是任意上述 $A$ 上的有理多项式身份。
特别在分歧 $\mathcal O_L/p\mathcal O_L$ 上仍全成立；
只验证 $\mathbf F_p$-值点会遗漏的 nilpotent 项没有被删除。
本节没有扩大 §8.3 未分歧算术比较的范围，
也没有用参数六重对称性替代原 weighted trace 的跨轨道项。
全部为纸面推导，无数学程序执行。


## 10. 同一五点配置的完整 Frobenius 五项式

本节沿 R1133 (1133.84) 的固定顺序，使用同一个五点配置。
它把原 arithmetic 五项上链接到 §8 的实际
Frobenius/transport 读取，保留五个提升之间的相关性。

### 10.1. 同一个 Coleman 五项式及两配置间的混合项

令
$$
(u_1,u_2,u_3,u_4,u_5)=
\left(\xi,\frac{\xi}{1-\eta},
 \frac{\xi\eta}{(1-\xi)(1-\eta)},
 \frac{\eta}{1-\xi},\eta\right),
\qquad s_i=(-1)^{i-1}.
\tag{1155.34}
$$
保持 $\xi\eta(1-\xi)(1-\eta)(1-\xi-\eta)\ne0$。
取固定的 Coleman branch，并写
$$
a_i=\log_pu_i,\qquad b_i=\log_p(1-u_i),\qquad
k_i=-\operatorname{Li}_2^p(u_i)-\frac12a_ib_i.
$$
用 $A=\log_p\xi,B=\log_p\eta,C=\log_p(1-\xi)$、
$D=\log_p(1-\eta),E=\log_p(1-\xi-\eta)$，
五个 $(a_i,b_i)$ 正是 R1133 (1133.86) 的同一个线性表。
在五维形式向量空间中直接展开，有
$$
\boxed{\quad
\sum_i s_i a_i\wedge b_i=0,\qquad
\sum_i s_i a_ib_i=2CD.
\quad}
\tag{1155.35}
$$
第一式在形式 exterior algebra 中成立，
不只是五个已代入数值的 wedge 为零。

于是
$$
d\sum_i s_i k_i
=-\frac12\sum_i s_i(a_i\,db_i-b_i\,da_i)=0.
$$
固定 $\eta$、令 $\xi\to0$：前三个参数趋零，后两项
分别趋 $\eta,\eta$，所以常数为零。
这里 $\operatorname{Li}_2(t)$ 和
$\log(t)\log(1-t)$ 在这个切向极限均趋零。
先在该局部盘求得身份，再用 Coleman continuation 的唯一性，
得到
$$
\boxed{\qquad \sum_i s_i k_i=0.\qquad}
\tag{1155.36}
$$
所用唯一性是 Furusho Theorem 2.14 证明末段使用的同一原则；
固定 $\eta$ 后只在删去有限点的曲线上作 pullback 和延拓。
因此不从复解析路径偷偷换到任意五个无关的 $p$-adic 常数。

取第二个真实配置 $(\xi',\eta')$，用撇号记其对应的五个参数、
logs 及 $G_i'=G(u_i')$。由 (1155.35) 的形式 wedge 身份，
$$
\sum_i s_i(a_i b_i'-b_i a_i')=0.
\tag{1155.37}
$$
令
$$
R_i=G(u_i)D_pG(u_i')^{-1}
   =\mathcal H(\alpha_i,\beta_i,\zeta_i),\qquad
\kappa_i=\zeta_i-\alpha_i\beta_i/2.
$$
同一 class-two BCH 公式准确给
$$
\kappa_i=k_i-p^{-2}k_i'
              -\frac{a_ib_i'-b_ia_i'}{2p}.
\tag{1155.38}
$$
故两份 (1155.36) 和 (1155.37) 消去完整混合项，得到
$$
\boxed{\quad
\sum_i s_i\kappa_i=0,\qquad
\sum_i s_i\zeta_i=C_R D_R,
\quad
C_R=C-p^{-1}C',\quad D_R=D-p^{-1}D'.
\quad}
\tag{1155.39}
$$
第二式再用 $\alpha_i=a_i-p^{-1}a_i'$、
$\beta_i=b_i-p^{-1}b_i'$ 的同一线性表和 (1155.35)。
因此它保留原 ordered 五项式的乘积项，
与 R1133 (1133.88) 的坐标一致；
并没有先把各个中央槽当成普通可加 cocycle。

### 10.2. 同一两变量提升的五个真实 carry

现设 $L/\mathbb Q_p$ 有限，且
$\xi,\eta,1-\xi,1-\eta,1-\xi-\eta$ 全为 $\mathcal O_L$ 的单位。
取
$$
\xi'=\xi^p+p\varepsilon_\xi,\qquad
\eta'=\eta^p+p\varepsilon_\eta,
\qquad \varepsilon_\xi,\varepsilon_\eta\in\mathcal O_L.
\tag{1155.40}
$$
五个 $u_i'$ 必须由这两个数按 (1155.34) 实际计算。
于是 $u_i',1-u_i'$ 全为单位，且
$$
\varepsilon_i=\frac{u_i'-u_i^p}{p}\in\mathcal O_L.
$$
以下表中全部量在 $\mathcal O_L/p\mathcal O_L$ 中读取，置
$$
X=\xi^p,\quad Y=\eta^p,\quad
\mathsf C=1-X,\quad\mathsf D=1-Y,\qquad
c_\xi=l_1(\xi),\quad c_\eta=l_1(\eta),
$$
$$
e_{\mathsf C}=c_\xi-\varepsilon_\xi,\qquad
e_{\mathsf D}=c_\eta-\varepsilon_\eta.
$$
原五个 carry 的完整表为
$$
\begin{array}{c|l}
i&\varepsilon_i\\ \hline
1&\varepsilon_\xi\\[2pt]
2&\displaystyle
 \frac{\varepsilon_\xi}{\mathsf D}
 -\frac{X e_{\mathsf D}}{\mathsf D^2}\\[7pt]
3&\displaystyle
 \frac{Y\varepsilon_\xi+X\varepsilon_\eta}{\mathsf C\mathsf D}
 -\frac{XY e_{\mathsf C}}{\mathsf C^2\mathsf D}
 -\frac{XY e_{\mathsf D}}{\mathsf C\mathsf D^2}\\[7pt]
4&\displaystyle
 \frac{\varepsilon_\eta}{\mathsf C}
 -\frac{Y e_{\mathsf C}}{\mathsf C^2}\\[7pt]
5&\varepsilon_\eta .
\end{array}
\tag{1155.41}
$$
例如 $e_{\mathsf D}$ 正是
$\big((1-\eta')-(1-\eta)^p\big)/p\bmod p$，
而不是 $-\varepsilon_\eta$。
对乘积的 carry，模 $p$ 的乘法律为
$\varepsilon(fg)=f^p\varepsilon(g)+g^p\varepsilon(f)$；
逆元的 carry 是 $-\varepsilon(f)/f^{2p}$。
这两条与 §9 的补参数公式逐项给出整张表。
没有因 $u_i$ 是有理函数便跳过其分母的 carry。

### 10.3. 保留 nilpotents 的实际有限五项 identity

每个 $R_i$ 现满足 §8 的实际 $u_i^p\to u_i'$ 运输条件。
将 (1155.25) 代入 (1155.39)，得到
$$
\boxed{\quad
\sum_{i=1}^5 s_i\left(
 -\frac{l_2(u_i)}{1-u_i^p}
 -\frac{\varepsilon_i^2}{2u_i^p(1-u_i^p)}
\right)
 =\frac{e_{\mathsf C}e_{\mathsf D}}{\mathsf C\mathsf D}.
\quad}
\tag{1155.42}
$$
因为 $C_R\equiv-e_{\mathsf C}/\mathsf C$、
$D_R\equiv-e_{\mathsf D}/\mathsf D$，右边的符号为正。
等价的 BCH 五项式为
$$
\boxed{\quad
\sum_{i=1}^5 s_i\left(
 \frac{l_2(u_i)}{1-u_i^p}
 +\frac{\varepsilon_i l_1(u_i)}
        {2u_i^p(1-u_i^p)}
\right)=0.
\quad}
\tag{1155.43}
$$
五个 $\varepsilon_i$ 是 (1155.41) 相关的实际值，
不能逐项指定为零后继续使用这两个恒等式。
即使 $\varepsilon_\xi=\varepsilon_\eta=0$，
三个中间参数的 carry 一般也不为零。

这些是强模 $p\mathcal O_L$ 等式，故包含分歧输入的全部
nilpotent 部分。还可将其读成
$\mathbf F_p[\xi,\eta,\varepsilon_\xi,\varepsilon_\eta,
(\xi\eta(1-\xi)(1-\eta)(1-\xi-\eta))^{-1}]$
中的有理多项式身份：
对每个有限未分歧扩张及任意两误差参数取整提升，上述证明成立；
所有 $\overline{\mathbf F}_p$ 点构成该开集的稠密集合，
因而清分母后的多项式恒为零。
所以任意含 nilpotents 的 $\mathbf F_p$-代数代入亦成立。
此论证使用全部有限扩张的点，而不是由有限的
$\mathbf F_p$-值检验猜测多项式身份。

(1155.42)–(1155.43) 已付原换弦/五项组合所需的
局部 Frobenius 相容式；右侧乘积与 R1133 的
$\operatorname{Cor}(CD)$ 一样不能拆成两个 Norm 的乘积。
实际 finite transfer 仍须按同一 coset/路径执行；
本节不把此逐项身份称为指定 theta moment 的全组合已经构造，
也不将任意 $\xi',\eta'$ 解释为分歧域上的 field Frobenius。
原 $F_0$ 的 $z_{12}$ 仍待同一 filling 完成后读取。
全部为纸面证明，无数学程序执行。


## 11. 原 Gaussian 单个单位方程的中央第十二 jet 与单位组合

本节给 §6 的同一个 $U_a(P)$ 一个可直接用于后继 filling 的有限
中央读取。这里的变量是椭圆曲线原点处的**有限阶整坐标**，
不是 R1149 的模曲线变形参数，也不是把实际非零 $p$-torsion
点的完整 formal logarithm 当成非零坐标。
结论是原单个 primitive 的 relative Frobenius jet；
加权矩、全部 Cor 及目标 $F_0$ 的比较仍须继续。

### 11.1. 原 formal-group 坐标的安全范围

设 $p>37$，原 Gaussian 模型为
$$
E:\ y^2=x^3+A x,\qquad A\in\mathcal O_F^\times,\qquad
\omega=\frac{dx}{2y}.
$$
取原整参数 $t=-x/y$，仅在有限阶取
$$
z(t)=\int_0^t\omega\pmod{t^{21}},\qquad z=t+O(t^5).
\tag{1155.51}
$$
此处积分只除以 $1,\ldots,20$，均为 $p$ 单位。
因此 $z$ 是整的可逆坐标 jet，且
$z([a]t)=a z(t)\pmod{t^{21}}$。
它来自特征零 formal-logarithm 身份的这个安全有限前缀；
没有在实际 torsion 点上将完整 logarithm 截断为 (1155.51)。

由 $x'^2=4x^3+4Ax$、$x''=6x^2+2A$ 以及原 leading $x=z^{-2}+\cdots$，
逐项得到
$$
x(z)=z^{-2}-\frac A5z^2+\frac{A^2}{75}z^6
                  -\frac{2A^3}{4875}z^{10}+O(z^{14}).
\tag{1155.52}
$$
Gaussian 自动同构使指数皆为 $2\bmod4$；
三个系数分别由
$2c_1=12c_1+2A$、
$30c_2=12c_2+6c_1^2$、
$90c_3=12c_3+12c_1c_2$
给出。有限坐标的 $O(z^{21})$ 误差作用于 $x$ 后至少为
$O(z^{18})$，故不影响以下模 $z^{16}$ 的单位比值。

保持 §6 的同一整数 $3\le a\le(p-1)/2$，置
$$
s=a^2,\qquad u_0=\frac{s-4}{4(s-1)}\in\mathbf F_p\setminus\{0,1\}.
$$
在本节所有有限式中 $A$ 也约模 $p$，并定义
$$
U(z)=\frac{x([a]P)-x([2]P)}{x([a]P)-x(P)}
     \in(\mathcal O_F/p)[[z]]/(z^{16}).
\tag{1155.53}
$$
这是原 $U_a$ 的实际函数 jet；分子、分母乘 $z^2$ 后
leading 均为单位。因而 $U$、$1-U$ 都是所需的单位。

为保全部系数，对 $b=1,2$ 记 $t_b=b^2$。原差值准确为
$$
\begin{aligned}
x([a]P)-x([b]P)
={}&z^{-2}(a^{-2}-b^{-2})
\left(1+\frac{A s t_b}{5}z^4
-\frac{A^2s t_b(s^2+s t_b+t_b^2)}{75}z^8\right.\\
&\left.\hspace{22mm}
+\frac{2A^3s t_b
 (s^4+s^3t_b+s^2t_b^2+s t_b^3+t_b^4)}{4875}z^{12}
+O(z^{16})\right).
\end{aligned}
\tag{1155.54}
$$
令 $\mathcal L(z)=\log(U(z)/u_0)$，log 只按幂零元作有限展开。
由 (1155.54) 的 $t_b=4$ 与 $t_b=1$ 两项相减，
$$
\mathcal L=L_1z^4+L_2z^8+L_3z^{12}\pmod{z^{16}},
\tag{1155.55}
$$
其中
$$
\boxed{\begin{aligned}
L_1&=\frac{3As}{5},\\
L_2&=-\frac{A^2s(2s^2+25s+42)}{50},\\
L_3&=\frac{A^3s(2s^4+75s^3+588s^2+1275s+682)}{1625}.
\end{aligned}}
\tag{1155.56}
$$
例如对一般 $t_b$，log 的 $z^{12}$ 系数为
$$
A^3\left(
\frac{2s t_b(s^4+s^3t_b+s^2t_b^2+s t_b^3+t_b^4)}{4875}
+\frac{s^2t_b^2(s+t_b)^2}{375}\right);
$$
因此 (1155.56) 保留了 log 的全部乘积修正。

### 11.2. 同一有限 polylogarithm 的完整三阶展开

现在只在上述幂零商中工作。因 $p>37$，
$$
U(z)^p=u_0,\qquad 1-U(z)^p=1-u_0.
$$
设 $\ell_r=\ell_{r,p}$，$U=u_0e^{\mathcal L}$。
有限多项式的导数恒等式给
$$
\frac{d}{d\mathcal L}\ell_2(U)=\ell_1(U),\qquad
\frac{d}{d\mathcal L}\ell_1(U)
=\frac{U-U^p}{1-U}=\frac{U-u_0}{1-U}.
\tag{1155.57}
$$
所读阶数小于 $p$，积分常数由 $\mathcal L=0$ 固定，故
$$
\begin{aligned}
\ell_1(U)
 &=\ell_1(u_0)+
   \frac{u_0}{2(1-u_0)}\mathcal L^2+
   \frac{u_0(1+u_0)}{6(1-u_0)^2}\mathcal L^3
   \pmod{\mathcal L^4},\\
\ell_2(U)
 &=\ell_2(u_0)+\ell_1(u_0)\mathcal L+
   \frac{u_0}{6(1-u_0)}\mathcal L^3
   \pmod{\mathcal L^4}.
\end{aligned}
\tag{1155.58}
$$
特别第二式没有 $\mathcal L^2$ 项，但必须保留显示的三次项。
同样可以先用准确有限 log 身份
$$
\ell_1(U)-\ell_1(u_0)
=-u_0\log(U/u_0)
 -(1-u_0)\log\bigl((1-U)/(1-u_0)\bigr)
$$
在此低阶商中核对第一式。
这解释了为何下面的第二 Frobenius 槽不是 raw $\log(1-U)$。

将 §5 的同一 relative Frobenius 记为
$$
R^\dagger(U(z))=(0,b(z),h(z)).
$$
其完整低阶值为
$$
\boxed{\begin{aligned}
b(z)&=-\frac{\ell_1(u_0)}{1-u_0}
-\frac{u_0}{2(1-u_0)^2}\mathcal L^2
-\frac{u_0(1+u_0)}{6(1-u_0)^3}\mathcal L^3,\\
h(z)&=-\frac{\ell_2(u_0)}{1-u_0}
-\frac{\ell_1(u_0)}{1-u_0}\mathcal L
-\frac{u_0}{6(1-u_0)^2}\mathcal L^3
\qquad\bmod z^{16}.
\end{aligned}}
\tag{1155.59}
$$
第一槽准确为零，所以这里 ordered 与 BCH 中央相同。
本节没有把任意 $v$ 的运输误差 $\varepsilon$ 设为零；
所读的正是已指定的 $v=U(z)^p$ relative Frobenius。

### 11.3. 一个不依赖有限 logarithm 值的单位组合

记 $h_j=[z^j]h(z)$、$b_j=[z^j]b(z)$。由 (1155.59)，
$$
h_4=-\frac{\ell_1(u_0)}{1-u_0}L_1,\qquad
h_8=-\frac{\ell_1(u_0)}{1-u_0}L_2,\qquad
h_{12}=-\frac{\ell_1(u_0)}{1-u_0}L_3
       -\frac{u_0L_1^3}{6(1-u_0)^2}.
\tag{1155.60}
$$
$L_1$ 是单位，而直接代入 $u_0,L_1$ 得
$$
\boxed{\quad
h_{12}-\frac{L_3}{L_1}h_4
=-\frac{2A^3s(s-1)(s-4)}{125}\ \in(\mathcal O_F/p)^\times.
\quad}
\tag{1155.61}
$$
这里
$$
\frac{L_3}{L_1}
=\frac{A^2(2s^4+75s^3+588s^2+1275s+682)}{975}
$$
也只含已付单位分母。
所以原单个 primitive 的两个指定中央 jet 不可能同时为零：
若 $\ell_1(u_0)=0$，则 $h_{12}$ 本身为所示单位；
否则 $h_4$ 已为单位。

作为同一 finite Frobenius 的完整第二槽读取，
$$
\boxed{\quad
b_4=0,\qquad
b_8=-\frac{2A^2(s-1)(s-4)}{25},\qquad
b_{12}=\frac{4A^3(s-1)(s-4)(s+5)^2}{375}.
\quad}
\tag{1155.62}
$$
$b_8$ 恒为单位，$b_{12}$ 不宣恒为单位。
这两个值使用 (1155.59) 的实际第二槽，未删除一个 raw-log 线性项后
再称其为原 Kummer 槽。

(1155.61) 是一个已经付清的原 primitive 局部输入。
原 R1156–1157 filling 的加权和、同陪集 Cor、运输误差及
moment contraction 仍可能产生真实抵消；本式没有排除那些抵消，
没有把 $z$ 换成模曲线的 $t$，也没有宣称已付 $F_0$ 的 $z_{12}$。
实际 torsion 点的 $\mathcal O_L/p$ 中，高于 $z^{12}$ 的幂零项
也不能仅凭本节的 jet 计算删除。

root 纸推；o2_high_coefficient 独立核准 (1155.54)–(1155.56)
全部系数、中央单位组合和第二槽两个系数。
全部为原函数的有限代数推导，无数学程序执行。


## 12. 同一有限椭圆坐标上的实际 Frobenius 提升与第八 jet

本节保持 §11 的原函数 $U_a$、有限整坐标 $z$ 和 $L_1,L_2,L_3$，
明确指定形式盘的 Frobenius 提升。这样得到的是同一 KZ pullback 的
实际 relative Frobenius；不把它解释为分歧 torsion 点上的 field Frobenius。
它补全 §11 中 $v=U^p$ 与一个真正底参数提升之间的差别。

### 12.1. 实际形式底及不可删除的 carry

设 $F/\mathbb Q_p$ 未分歧，$\sigma_F$ 为其整 Frobenius。
将 (1155.51) 的有限整坐标任意延长成
$\mathcal O_F[[t]]$ 的整可逆坐标 $z$，并固定
$$
\psi|_{\mathcal O_F}=\sigma_F,\qquad \psi(z)=z^p.
$$
这里可直接将显示的有限 $z(t)$ 多项式用作完整坐标；
不需要在首个 $p$ 分母之后延长椭圆 formal logarithm。
$U=U_a\in\mathcal O_F[[z]]^\times$、$1-U$ 也为单位。
其准确常数是
$$
\widetilde u_0=\frac{a^2-4}{4(a^2-1)}\in\mathbb Z_p^\times,
$$
约化为 §11 的 $u_0$。置
$$
v=\psi U,\qquad
\varepsilon=\frac{\psi U-U^p}{p}\in\mathcal O_F[[z]],\qquad
\varepsilon_0=\frac{\sigma_F(\widetilde u_0)
                         -\widetilde u_0^p}{p}\in\mathcal O_F.
\tag{1155.63}
$$
分子整除 $p$ 来自真正的 Frobenius-lift 性质，
不是由函数值在 residue field 中相等便对任意提升相减。

以下在 $(\mathcal O_F/p)[[z]]/(z^{16})$ 中读取，
并沿用 $\mathcal L=L_1z^4+L_2z^8+L_3z^{12}$。
因为 $U-\widetilde u_0\in z^4\mathcal O_F[[z]]$，
$v-\sigma_F(\widetilde u_0)\in z^{4p}\mathcal O_F[[z]]$。
在这一个安全有限商中，原特征零 log
$\widetilde{\mathcal L}=\log(U/\widetilde u_0)\bmod z^{16}$
只除 $1,2,3$，且 $\widetilde{\mathcal L}^4=0$。
故
$$
\frac{U^p-\widetilde u_0^p}{p}
=\widetilde u_0^p
 \left(\widetilde{\mathcal L}
       +\frac p2\widetilde{\mathcal L}^2
       +\frac{p^2}{6}\widetilde{\mathcal L}^3\right)
       \pmod{z^{16}}.
$$
约模 $p$，准确得到
$$
\boxed{\qquad
U^p=u_0,\qquad
\varepsilon=\varepsilon_0-u_0\mathcal L
\qquad\bmod(p,z^{16}).
\qquad}
\tag{1155.64}
$$
特别 $\varepsilon$ 不是常数，也不能在实际 $\psi$ 下置零。
由于 $\widetilde u_0\in\mathbb Q_p$，这里还可写
$\varepsilon_0=-u_0q_p(\widetilde u_0)$；本节不假设该数为零。

### 12.2. 三槽及完整中央运输

令同一 ordered Heisenberg Frobenius 为
$$
R_\psi(z)=G(U(z))D_pG(\psi U(z))^{-1}
          =\mathcal H(a_\psi,b_\psi,h_\psi).
$$
§8 的右运输证明是单位分母上的 $p$-整幂级数身份；
在 $p$-完备有限 jet 商中仍逐项成立。
因此可将 (1155.64) 直接代入 (1155.25)，保留其完整
$\varepsilon^2$ 中央项。定义常数
$$
a_0=-\frac{\varepsilon_0}{u_0},\qquad
b_0=\frac{\varepsilon_0-\ell_1(u_0)}{1-u_0},\qquad
h_0=-\frac{\ell_2(u_0)}{1-u_0}
      -\frac{\varepsilon_0^2}{2u_0(1-u_0)} .
$$
由 (1155.58) 的原有限 polylog 展开，
$$
\boxed{\begin{aligned}
a_\psi&=a_0+\mathcal L,\\
b_\psi&=b_0
 -\frac{u_0}{1-u_0}\mathcal L
 -\frac{u_0}{2(1-u_0)^2}\mathcal L^2
 -\frac{u_0(1+u_0)}{6(1-u_0)^3}\mathcal L^3,\\
h_\psi&=h_0+b_0\mathcal L
 -\frac{u_0}{2(1-u_0)}\mathcal L^2
 -\frac{u_0}{6(1-u_0)^2}\mathcal L^3
 \qquad\bmod z^{16}.
\end{aligned}}
\tag{1155.65}
$$
第二槽也准确等于
$b_0+\log((1-U)/(1-u_0))$ 的有限展开。
这与 (1155.59) 不矛盾：那一节的第二输入是 $U^p$，
本节的第二输入是同一形式底的 $\psi U$，
两者之间的 carry 已由 (1155.64) 实际计算。

尤其中央线性项是 $b_0\mathcal L$：
$\varepsilon^2$ 的交叉项把原 $-\ell_1(u_0)\mathcal L/(1-u_0)$
准确改成这个系数；其平方项还产生新的
$-u_0\mathcal L^2/(2(1-u_0))$。
这两项都不能在改变 Frobenius 提升时省去。

### 12.3. 原第八 jet 的显式单位组合

记 $h_{\psi,j}=[z^j]h_\psi$。由 (1155.65)，
$$
\begin{aligned}
h_{\psi,4}&=b_0L_1,\\
h_{\psi,8}&=b_0L_2-\frac{u_0L_1^2}{2(1-u_0)},\\
h_{\psi,12}&=b_0L_3
 -\frac{u_0L_1L_2}{1-u_0}
 -\frac{u_0L_1^3}{6(1-u_0)^2}.
\end{aligned}
\tag{1155.66}
$$
$L_1=3As/5$ 是单位。因 $u_0/(1-u_0)=(s-4)/(3s)$，
有
$$
\boxed{\quad
h_{\psi,8}-\frac{L_2}{L_1}h_{\psi,4}
=-\frac{u_0L_1^2}{2(1-u_0)}
=-\frac{3A^2s(s-4)}{50}\in(\mathcal O_F/p)^\times.
\quad}
\tag{1155.67}
$$
全部因子在原 $3\le a\le(p-1)/2$、$p>37$ 范围内确为单位。
同一提升的两个线性槽还有
$$
[z^4]a_\psi=\frac{3As}{5},\qquad
[z^4]b_\psi=-\frac{A(s-4)}5,
$$
二者也都是单位。

本节没有选取或删掉 $\varepsilon_0$，所以 (1155.67)
不依赖该 Fermat quotient 或 $\ell_1(u_0)$ 的未知值。
它是同一原单个 primitive、选定形式 Frobenius 的准确输入。
后继仍需原 filling 的加权、同陪集 corestriction、全部根相位及
moment contraction；单块单位不排总和抵消。
$z$ 仍是椭圆点坐标而非模曲线参数，
也不将 $\psi$ 的专化擅作任意分歧域上的 $\sigma_F$；
实际 torsion 的较高幂零项没有被删除。

root 纸推；o2_high_coefficient 独核实际 carry、三槽中央修正及
(1155.67) 的完整常数。无数学程序执行。


## 13. 原坏参数的浅退化读取与 log-preserving 深分支

本节保留 §8 的同一个原 KZ frame、右运输次序和实际参数。
它扩大有限读取的适用域，但不在分歧域上另造 field Frobenius。
特别，下面的浅退化式允许个别坐标具有负赋值；
“模 $p\mathcal O_L$”始终指显示数与真实数之差属于该理想。

### 13.1. 浅近零或近一的准确 Eulerian 尾

设 $p>37$，$L/\mathbb Q_p$ 为任意有限扩张，赋值规范为
$v_p(p)=1$。取
$$
u\in\mathcal O_L\setminus\{0\},\qquad
w=u^p,\qquad d=1-w\ne0,\qquad
\kappa=\max\{v_p(w),v_p(d)\}\le\frac13.
\tag{1155.68}
$$
因 $w+d=1$，两者中至少一个是单位。
沿 (1155.13) 定义 $\ell_{r,p}$，此处也使用 $r=3$；
这些是 $\mathbb Z_p[U]$ 中的原多项式，不先将 $u$ 换成
其 residue-field 常数。

(1155.15) 的完整 Eulerian 展开在
$|u|\le1,\ v_p(1-u^p)\le1/3$ 的 rational affinoid 上仍一致收敛。
确实，第 $m$ 项的赋值至少为
$$
m-(m+1)v_p(d)\ \ge\ m-(m+1)\kappa.
$$
该下界趋于无穷。此 affinoid 是闭单位盘去掉包含全部
$p$ 次单位根的一个开盘，因而几何连通；其上构造的函数与
原 Coleman 函数在 $|u|<1$ 的子域相等。
同 §5 的解析延拓遂识别为同一
$\operatorname{Li}_r^\dagger$，没有改变 Coleman 常数。
也可在任意较小 rational affinoid 上逐次作此论证。

因为 $P_0=1,\ P_1(w)=w$，保留 $m=0,1$ 得
$$
\boxed{\quad
\operatorname{Li}_r^\dagger(u)
 \equiv \frac{\ell_{r,p}(u)}d
       -\frac{r p w\,\ell_{r+1,p}(u)}{d^2}
       \pmod{p\mathcal O_L},
\qquad r=1,2.
\quad}
\tag{1155.69}
$$
被删去的 $m\ge2$ 项有赋值
$m-(m+1)\kappa\ge1$，包括
$m=2,\ \kappa=1/3$ 的端点。
原单位域中的 $m=1$ 项可以略去；近一时本式显示它不一定可略。

这里使用的解析输入仍是上列 Furusho Theorem 2.14、
Example 2.16(1) 的同一个函数。
新域、收敛界及有限截断由上述整数 Eulerian 递推直接证明。

### 13.2. 浅退化短运输必须保留三次中央项

取一个实际第二输入
$$
v=w+p\varepsilon,\qquad \varepsilon\in\mathcal O_L.
\tag{1155.70}
$$
不要求它是分歧域的自同态像。
(1155.68) 保证
$v_p(p\varepsilon/w)>0$、
$v_p(p\varepsilon/d)>0$，所以 (1155.21)–(1155.22)
的实际短路径级数仍绝对收敛。

将 $D_pH(w,v)$ 的三个坐标记为 $A_T,B_T,H_T$。
逐项保留两个 logarithm 的一次、二次项，以及中央的二次、三次项，
得到
$$
\boxed{\begin{aligned}
A_T&\equiv-\frac{\varepsilon}{w}
               +\frac{p\varepsilon^2}{2w^2},\\
B_T&\equiv \frac{\varepsilon}{d}
               +\frac{p\varepsilon^2}{2d^2},\\
H_T&\equiv-\frac{\varepsilon^2}{2wd}
        +\frac{p\varepsilon^3(1-3w)}{6w^2d^2}
          \qquad \pmod{p\mathcal O_L}.
\end{aligned}}
\tag{1155.71}
$$
中央三次项的号可不借形式矩阵记忆，直接从
$$
p^{-2}h_H
 =-p^{-2}\int_0^{p\varepsilon}
       \frac{\log(1+t/w)}{d-t}\,dt
$$
读取：二次系数为 $-1/(2wd)$，三次系数为
$(d-2w)/(6w^2d^2)=(1-3w)/(6w^2d^2)$。

完整尾界如下。两个 log 的第 $n\ge3$ 项，在除 $p$ 后的
赋值至少为
$$
n-1-n\kappa-v_p(n).
$$
中央的第 $n\ge4$ 项在除 $p^2$ 后，按 (1155.22) 的
$1\le r<n$ 逐项估计，赋值至少为
$$
n-2-(n-1)\kappa-v_p(nr).
\tag{1155.72}
$$
这里只出现 $(n-1)\kappa$，因为 $w,d$ 至多一者不是单位。
当 $n<p$ 时两式的最小端点分别是
$n=3$ 和 $n=4$，在 $\kappa=1/3$ 时恰为 $1$。
当 $n\ge p$ 时，用
$v_p(nr)\le v_p(n!)\le(n-1)/(p-1)$
及 $p>37$，两条线性余量均严格大于 $1$ 并趋于无穷。
所以本式控制全部尾，不是只把三次之后形式截掉。

### 13.3. 同一个 relative Frobenius 的浅退化三槽

沿 (1155.24) 的同一精确顺序
$$
R_v(u)=R^\dagger(u)\,D_pH(w,v)
       =\mathcal H(a_v,b_v,h_v),
$$
结合 (1155.69)–(1155.71)，得到
$$
\boxed{\begin{aligned}
a_v&\equiv-\frac{\varepsilon}{w}
              +\frac{p\varepsilon^2}{2w^2},\\
b_v&\equiv\frac{\varepsilon-\ell_{1,p}(u)}d
       +\frac{p\bigl(w\ell_{2,p}(u)+\varepsilon^2/2\bigr)}{d^2},\\
h_v&\equiv-\frac{\ell_{2,p}(u)}d
       +\frac{2pw\ell_{3,p}(u)}{d^2}
       -\frac{\varepsilon^2}{2wd}
       +\frac{p\varepsilon^3(1-3w)}{6w^2d^2}
       \qquad\pmod{p\mathcal O_L}.
\end{aligned}}
\tag{1155.73}
$$
原 $R^\dagger$ 的第一槽严格为零；
故这次乘积没有把某个仅知属于 $p\mathcal O_L$ 的误差
再乘上负赋值的第一槽。这是本式保持所声明精度的原因。

(1155.73) 是三条在 $L$ 中的坐标同余，
不宣称右边组成 $\mathcal H(\mathcal O_L/p)$ 的点。
当 $w$ 或 $d$ 不是单位时，
任意另一个群乘法、BCH 变换或 tensor contraction
可能放大被删去的误差；不能仅凭本式已经写了“mod $p$”
就任意连续做这些操作。

实际组合可以先提高精度再相乘。
例如，要把单项误差控制到 $p^h\mathcal O_L$，
Eulerian 和保留 $m<M$，使
$M-(M+1)\kappa\ge h$；
log 与中央级数保留足够多的项，使 (1155.72)
及其 log 版本在全部尾指标上至少为 $h$。
取
$$
(N-1)\left(1-\kappa-\frac1{p-1}\right)-1\ge h
$$
即为两种运输尾从 $n=N$ 起的一个共同充分条件。
斜率为正，因此这是有限明确的精度选择。
随后按原矩阵乘法、固定陪集 Cor 及实际权逐步累计误差；
未约化的 (1155.15)、(1155.21)–(1155.22)
保留了全部同源数据。

### 13.4. 原共同提升保留边界时，任意深的近零分支

另设 $0\ne u\in\mathfrak m_L$，不再施加 (1155.68) 的深度上界。
此时 $d=1-u^p$ 是单位。
如果**同一个已经给出的实际提升**满足
$$
v=u^p(1+p\alpha),\qquad \alpha\in\mathcal O_L,
\tag{1155.74}
$$
则在原坐标中直接有
$$
\boxed{\quad
R_v(u)\equiv\mathcal H\left(
-\alpha,\
 \frac{u^p\alpha-\ell_{1,p}(u)}{1-u^p},\
-\frac{\ell_{2,p}(u)}{1-u^p}
-\frac{u^p\alpha^2}{2(1-u^p)}
\right)\pmod{p\mathcal O_L}.
\quad}
\tag{1155.75}
$$
本式的三个坐标全为整的。

证明可直接在 $|u|<1$ 用
$\sum_{p\nmid n}u^n/n^r$，或用 $d$ 为单位的
(1155.15)，得到
$\operatorname{Li}_r^\dagger\equiv\ell_r/d$。
运输中置 $\varepsilon=w\alpha$：
两个相对增量分别为 $p\alpha$、$pw\alpha/d$。
两个 log 除 $p$ 后的高次项都在 $p\mathcal O_L$；
中央第 $n\ge3$ 项还带 $w^{n-r}$，其中 $n-r\ge1$，
故全部除 $p^2$ 后的尾同样在 $p\mathcal O_L$。
仅保中央二次项即得 (1155.75)。
在与浅退化域重叠的范围内，
(1155.73) 的额外 $p$ 项代入 $\varepsilon=w\alpha$
也确实全部落入 $p\mathcal O_L$；
这与直接的任意深证明一致。

一个可核的共同 log-preserving 来源是：
在某个已给出的形式底上，
$u=z^m a$，$a$ 为整单位，
$\psi(z)=z^p b$、$b\in1+p\mathcal O$，
且 $\psi(a)/a^p\in1+p\mathcal O$。
于是
$\psi(u)/u^p=b^m\psi(a)/a^p\in1+p\mathcal O$，
保留真实 $a$ 后就得到同一 $\alpha$。
这是一条充分条件，不是为每个 primitive 自由选择一个新 $\psi$。

近 $1$ 或 $\infty$ 时，可先在同一配置中使用
$t=1-u$ 或 $t=u^{-1}$。
必须将第二输入同时换成 $1-v$ 或 $v^{-1}$，
核该实际 $t$ 满足 (1155.74)，再沿原参数 isomorphism 运输：
分别保 (1155.33) 的
$\mathcal H(b,a,ab-h)$ 或
$\mathcal H(-a,b-a,-h+a^2/2)$，以及原根规范。
这里使用的是同一 class-two path object 的参数变换；
不把近一时 $1-v$ 擅自换成 $(1-u)^p$。
由于 (1155.75) 已给整的三槽，这一分支的这些 polynomial
群变换不会放大其 $p\mathcal O_L$ 误差。


上述坏域的参数运输还可在约化前直接核准，避免把 §9 的单位域
有限身份越界使用。Furusho，
[*p-adic multiple zeta values I — p-adic multiple polylogarithms and the p-adic KZ equation*](https://arxiv.org/pdf/math/0304085)，
Invent. Math. **155** (2004), 253–286，
Example 2.19(a) 给原规范的 $\operatorname{Li}_2(1)=\zeta_p(2)=0$。
在同一 Coleman branch 中，分别求导并取 $u\to0$、$u\to1$
的切向常数，即得到两个完整身份
$
\operatorname{Li}_2(1-u)+\operatorname{Li}_2(u)
=-\log u\,\log(1-u),\qquad
\operatorname{Li}_2(u^{-1})+\operatorname{Li}_2(u)
=-\frac12\log^2u.
\tag{1155.76}
$
第二式使用 $\log(-1)=0$；
两式的导数为零后，Coleman 唯一性把已核的常数带到整个定义域。
于是对原 $G(u)=\mathcal H(\log u,\log(1-u),-\operatorname{Li}_2(u))$，
严格有 $G(1-u)=S(G(u))$、$G(u^{-1})=J(G(u))$，
其中 $S,J$ 就是显示的两个多项式群自同构。
它们与 $D_p$ 交换，所以对任意同一实际两输入
$R_v(u)=G(u)D_pG(v)^{-1}$，也严格有
$R_{1-v}(1-u)=S(R_v(u))$、
$R_{v^{-1}}(u^{-1})=J(R_v(u))$。
因此近 $1,\infty$ 的使用先是完整特征零身份，
随后才在已证明整性的坐标上约化。

### 13.5. 对原二同源分解的具体接口和仍须读取的输入

[R1157 §11](R1157-original-integral-SV-Manin-triangle-filling.md)
已保原所有切线尺度、
$R_i(T_0-B_j)$、$\Delta/K_i$、
闭点以及实际有限 transfer。
其 characteristic-zero 四线参数约化到 $0,1,\infty$
时，不能再逐项套用旧单位域的 (1155.25)。

本节给出两个实际可检验的替代入口：
满足 (1155.68)–(1155.70) 时用 (1155.73)；
满足同一提升的 (1155.74) 时用 (1155.75)。
例如若已经证明某实际参数或其补参数为
$c t^e(1+O(t))$，其中 $c$ 为单位、
$v_p(t)=1/(p^2-1)$、$1\le e\le12$，
则其相应浅退化量是
$pe/(p^2-1)<1/3$，对 $p>37$ 落入第一入口。
这里条件中的实际阶及 leading 单位需要原函数逐项证明，
并未宣称全部四线参数自动满足它们。

在完整 SS full-level 来源上构造共同 log-smooth 模型及
共同 $\psi$，仍是另一件具体工作。
尤其不能在分歧 $\mathcal O_L$ 上令 uniformizer 取 $p$ 次幂，
又同时要求固定底层的 $p$，便称得到所需场 Frobenius。
本节只消费已经给出的实际两 fibre；没有创造该算术映射，
没有删掉相同配置的五项 carry 或 ordered 修正，
也没有据单个有限公式宣布目标 $F_0$ 的 $z_{12}$ 已读。

本节为纸面证明，无数学程序执行。
o2_high_coefficient 独立核准浅退化 Eulerian 修正、
中央三次项的符号和全部尾估值。


## 14. 原全部 CM 形式参数的共同提升与整有限 jet

本节使用 [R1157 §12](R1157-original-integral-SV-Manin-triangle-filling.md)
已经支付的原三次辅助点和全部参数阶。
在原 Gaussian/cubic CM 参考曲线上，固定一个非零 $p$-点作
$\mathcal O_{CM}/p=\mathbb F_{p^2}$ 模的生成元，
并为每个标记 $\alpha$ 固定一个 CM 整数提升。
实际形式端点为
$P(z),[\alpha]P(z),[1+\alpha]P(z)$。
这包括 $\mathbb F_p$-rank two 的点对。

取一个有限未分歧域 $F/\mathbb Q_p$，包含 CM、二扭点、
三次辅助点及参考线交点的全部系数，令
$$
\mathcal R=\mathcal O_F[[z]],\qquad
\psi|_{\mathcal O_F}=\sigma,\qquad \psi(z)=z^p,
\tag{1155.77}
$$
其中 $\sigma$ 是原未分歧的 $p$-power Frobenius。
$z$ 是原 elliptic formal-group 的整参数，不在此改成完整形式 logarithm。
所有标记、直线和归一常数均先固定，
然后在同一个环上应用这一 $\psi$。

**已证明：** 原四线来源的所有参数在这个共同提升下
同时给整的 Frobenius 三槽；
它们在任意 $N<p$ 的次数范围内都有下面的明确有限公式。
所支付的是这个实际形式来源的矩阵，
并非已经识别到原有限 $E[p]$ moment 或其 Fontaine–Laffaille 读数。

### 14.1. 全部边界由同一个提升同时保留

R1157 (1157.47)–(1157.53) 的 divisor 因子先给精确的整 $z$ 幂，
不只是一个点处的赋值；非零首项再使剩余因子为整单位。
所以每个原四线参数都满足
$$
u=z^m a(z),\qquad 1-u=z^n b(z),\qquad
a,b\in\mathcal R^\times,\qquad m,n\in\{-1,0,1\}.
\tag{1155.78}
$$
线归一中的有正阶的 $\alpha_i$ 也保留其整幂和单位因子。
特别，没有一个更低 $z$ 次项仅因含因子 $p$ 被悄悄删除。

在 $\mathcal R[1/z]$ 中直接计算
$$
\frac{\psi(u)}{u^p}
 =\frac{\psi(a)}{a^p}\in1+p\mathcal R,\qquad
\frac{1-\psi(u)}{(1-u)^p}
 =\frac{\psi(b)}{b^p}\in1+p\mathcal R.
\tag{1155.79}
$$
这里 $\sigma(c)\equiv c^p\bmod p$，
所以 $\psi(a)\equiv a^p\bmod p$，
且 $a^p,b^p$ 在 $\mathcal R$ 中可逆。
两个商的整性同时成立，包括 $m$ 或 $n$ 为负的情形；
负的 $z$ 幂在商中准确相消。
这使用一个共同的 $\psi$，没有对每个 primitive 重新指定误差。

定义原同一 KZ frame 中的矩阵
$$
R_\psi(u)=G(u)D_pG(\psi(u))^{-1}.
\tag{1155.80}
$$
若 $u$ 近零，则 $u\in z\mathcal R$，
$1-u^p$ 为整单位。
原 $\operatorname{Li}_r^\dagger(u)=
\sum_{p\nmid j}u^j/j^r$ 是 $\mathcal R$ 中的级数。
置 $\alpha=(\psi(u)/u^p-1)/p\in\mathcal R$，
原短运输中的两个增量是 $p\alpha$、
$pu^p\alpha/(1-u^p)$。
两个 log 除 $p$ 后的系数均整；
中央第 $j$ 项除 $p^2$ 后的系数为
$p^{j-2}/(jr)$ 乘一个整项，$1\le r<j$，
且 $j-2-v_p(jr)\ge0$。
所以整个矩阵的三个坐标都属于 $\mathcal R$。

若 $u,1-u$ 都为 $\mathcal R$ 单位，
同一个结论由 §5 的完整 Eulerian 展开和 §8 的完整短运输得到：
Eulerian 尾逐项至少含 $p^j$，两分母都是整单位，
故在 $p$-完备的 $\mathcal R$ 中收敛。
若 $1-u$ 近零或 $u$ 有极，
分别对 $1-u$、$u^{-1}$ 使用前一段，
再用 (1155.76) 的**完整** $S,J$ 群映射。
由 (1155.79)，变换后的第二输入仍是同一 $\psi$ 的像。
因此在全部四类参数上都有
$$
\boxed{\qquad R_\psi(u)\in\mathcal H(\mathcal R).\qquad}
\tag{1155.81}
$$
这一整性是在取 jet 之前证明的。
所以不能误把含 $z^{-1}$ 的原参数先代进
$\mathcal R/(p,z^{N+1})$；先构造 (1155.80)，再约化其整坐标。

### 14.2. 单位参数的任意安全阶 jet

以下所有等式在
$$
\mathcal R_N=\mathcal R/(p,z^{N+1}),\qquad 0\le N<p
$$
中读取。每次积分只除 $1,\ldots,N$，均为单位。

先取 $u,1-u\in\mathcal R^\times$，
$c=u(0)$，于是 $c,1-c\in\mathcal O_F^\times$。
用这个**实际**常数计算
$$
w_c=c^p,\qquad \varepsilon_c=\frac{\sigma(c)-c^p}{p}.
$$
原常数矩阵的约化是
$$
\begin{aligned}
a_c&=-\frac{\varepsilon_c}{w_c},\\
b_c&=\frac{\varepsilon_c-\ell_{1,p}(c)}{1-w_c},\\
h_c&=-\frac{\ell_{2,p}(c)}{1-w_c}
     -\frac{\varepsilon_c^2}{2w_c(1-w_c)}.
\end{aligned}
\tag{1155.82}
$$
这里 $w_c\bmod p=\bar c^{\,p}$，不擅自把它改为 $\bar c$，
也不假定 $c$ 是 Teichmüller lift。

令
$$
L(z)=\log\frac{u(z)}c,\qquad
M(z)=\log\frac{1-u(z)}{1-c},
$$
并只保次数至 $N$。
两个 log 的参数均在 $1+z\mathcal R$ 中，
故这些有限截断是整的。
完整 jet 恰为
$$
\boxed{
R_\psi(u)\equiv\mathcal H\left(
a_c+L,\ b_c+M,\
h_c+b_cL+\int_0^z M(t)\,dL(t)
\right)\quad\bmod(p,z^{N+1}).}
\tag{1155.83}
$$

证明可在特征零先计算，随后使用 (1155.81) 约化。
因 $N<p$，有
$\psi(u(z))=\sigma(c)+O(z^p)$；
故正次数至 $N$ 的第二输入没有变化。
两个 abelian 槽分别增加 $L,M$。
中央坐标的导数则准确为
$(b_c^{\rm exact}+M)\,dL$，
其中 $b_c^{\rm exact}$ 是原常数矩阵的未约化第二槽。
积分的常数由 $z=0$ 的同一矩阵固定。
这给 (1155.83)，其常数约化由 (1155.82) 给出。
特别，$b_cL$ 和所有二次有序项仍保留。

### 14.3. 三种坏参数的明确 jet 和边界常数

令
$$
t=z^m a(z),\qquad m\ge1,\qquad a\in\mathcal R^\times,\qquad a_0=a(0).
$$
定义这个单位首项的实际 carry 和有限 log
$$
\kappa(a_0)=\frac{\sigma(a_0)/a_0^p-1}{p}\bmod p,\qquad
A_a(z)=-\kappa(a_0)+\log\frac{a(z)}{a_0}.
$$
并置
$$
L_r(t)=\sum_{j=1}^{N}\frac{t^j}{j^r}
 \quad\bmod(p,z^{N+1}),\qquad r=1,2.
$$
当 $m>1$ 时，超出所需次数的项自然为零。

三个坏域的全部 jet 是
$$
\boxed{\begin{array}{c|c}
\text{原参数}&R_\psi\text{ 的三槽}\\ \hline
u=t&
\mathcal H(A_a,-L_1(t),-L_2(t))\\[2pt]
u=1-t&
\mathcal H(-L_1(t),A_a,L_2(t)-A_aL_1(t))\\[2pt]
u=t^{-1}&
\mathcal H(-A_a,-L_1(t)-A_a,L_2(t)+A_a^2/2).
\end{array}}
\tag{1155.84}
$$
所有等式都是同一第二输入 $\psi(u)$ 的结果。

对第一行，$\log z$ 项在
$\log t-p^{-1}\log\psi(t)$ 中严格相消。
正次数小于 $p$ 时，
$\log\psi(a)=\log\sigma(a_0)+O(z^p)$，
故第一槽就是 $A_a$。
而 $\psi(t)$ 的阶至少为 $p$，
其 $\operatorname{Li}_2$ 与 $\log(1-\psi(t))$ 的正次数
都至少为 $p$。
原中央坐标可准确写成
$$
-\operatorname{Li}_2(t)
+p^{-2}\operatorname{Li}_2(\psi(t))
-p^{-1}a_\psi(t)\log(1-\psi(t)).
$$
所以至次数 $N$ 只留下 $-L_2(t)$；
第二槽同样只留下 $-L_1(t)$。
没有对高次数项的系数整性作猜测：
整性已由 §14.1 的完整矩阵另行支付。
后两行再分别使用实际 $S,J$，给显示的全部乘积和半平方。

尤其在边界 $z=0$，
$$
\boxed{\begin{array}{c|c}
u\to0&(-\kappa(a_0),0,0)\\
u\to1&(0,-\kappa(a_0),0)\\
u\to\infty&(\kappa(a_0),\kappa(a_0),\kappa(a_0)^2/2).
\end{array}}
\tag{1155.85}
$$
所以即使某 Bloch specialization 把 $[0],[1],[\infty]$ 记作零，
也不能逐项删掉这些实际有序 Frobenius 边界。
它们的 BCH 中央常数为零，与有序中央常数可能非零并不冲突。

### 14.4. 同一配置的关系与原有限读取范围

$\psi$ 是固定环同态，故原所有乘法关系、线关系、
分母和五点配置都同时被它保持。
若一份真实五点配置的五个参数及补参数都具有
(1155.78) 的形式，那么 §10 的完整 Coleman 身份与
(1155.81) 允许直接在 $\mathcal R_N$ 中约化：
$$
\sum_i s_i\left(h_i-\frac12a_i b_i\right)=0,\qquad
\sum_i s_i h_i=C_\psi D_\psi,
\tag{1155.86}
$$
其中
$C_\psi=\log(1-\xi)-p^{-1}\log\psi(1-\xi)$，
$D_\psi=\log(1-\eta)-p^{-1}\log\psi(1-\eta)$。
这些量也是整的，且是同一配置的实际数值。
没有将五个 carry 各自改为零。

对已给定的有限有序矩阵乘法、逆元及整系数群态射，
现在约化到 $\mathcal R_N$ 确实与运算交换；
不会再出现 §13 浅退化坐标误差被负赋值放大的问题。
本陈述只消费**已经给出的整系数**运算，
不由此猜测 moment 的 de Rham 标架或 FL 尺度也没有损失。
全部原根相位、四线/五项 gauge、真实 finite Cor 仍按原程序保留。

由 (1155.82)–(1155.84)，每个原参数的这个形式 $N$-jet
只需其单位部分至次数 $N$ 的模 $p$ 系数，
以及实际常数/单位首项的模 $p^2$ carry。
例如 §11–12 的单 primitive 比较所用形式次数十二满足 $12<p$，
无须为了这些形式 jet 引入完整形式 logarithm 的首个 $p$ 分母。
这没有删除真实 $p$-torsion 上更高次数的 nilpotents：
从形式 jet 到该真实值的箭头仍须单独证明，不能据此把完整 moment 读数截在次数十二。

### 14.5. 与真实 $E[p]$ 塔之间保留的准确比较

(1155.77) 一般不保持原 $E[p]$ 的定义理想。
因此 (1155.83)–(1155.84) 不能单靠代入一个 $p$-点，
就被称作该有限标记塔上的 field Frobenius 或原 $F_0$。
固定 CM 整数提升的选择也不能在尚未完成这一步时被随意更换；
不同提升在 $E[p]$ 上相同，不代表其整个形式来源相同。

“理想的误差含一个 $p$”本身不足以省去比较。
仅在具有同一 tame 指数 $e=p^2-1$ 的简单整模型中取
$g=z^e-p$，仍以 $\psi(z)=z^p,\psi(p)=p$，就有
$$
\psi(g)\big|_{g=0}=p^p-p.
$$
对 $1\le r<p$，在允许的 divided-power 归一中准确得到
$$
\left.\frac{\psi(g^r/r!)}{p^r}\right|_{g=0}
 =\frac{(p^{p-1}-1)^r}{r!}
 \equiv\frac{(-1)^r}{r!}\not\equiv0\pmod p.
\tag{1155.87}
$$
这是一个完整的误差计算，说明未经支付的整格归一可以看见
该 normal 方向；它没有声称原四十三格必然采用此项。
真正后继是原根塔/共同 log 或 crystalline realization 的比较，
包括所有 moment 权和可能的除 $p$，
而不是把这一差称为一个已经消失的余链。

本节由原完整 KZ 矩阵、R1157 的精确 divisor 因子、
形式环同态及安全次数的积分逐式证明。
没有数学程序执行。

独立纸核：o2_high_coefficient 核准 (1155.83)–(1155.85) 的全部常数、积分号、$S/J$ 中央补项与 $N<p$ 的范围；原 $E[p]$ 比较没有作为本节输入。


## 15. 原含分歧坏点的半稳定比较与同一路径规范

本节解除 §2 对**原 rational primitive 的指定 Hodge 读数**
所保留的未分歧点限制。这里仍取 $p>37$，
$L/\mathbb Q_p$ 为任意有限扩张，$L_0$ 为其最大未分歧子域，
并令 $u\in L\setminus\{0,1\}$。
不要求 $u$ 或 $1-u$ 为整数单位。

**已证明：** §1 的同一原整根塔 $\mathscr D_u$ 张量到
$\mathbb Q_p$ 后为半稳定 torsor。它与三穿孔直线上的原
logarithmic KZ object 具有保持 $\varphi,N$、连接和滤过的
实际 period 比较；采用原 $\log_p p=0$ 与原切向根规范时，
其 semistable Hodge 坐标仍为
$$
G_{\rm st}(u)=
 \mathcal H\bigl(\log_pu,\log_p(1-u),-\operatorname{Li}_2^p(u)\bigr).
\tag{1155.88}
$$
若两个一次 Kummer classes 都是单位类，这也将 (1155.7)
扩到含分歧的良好单位点。
在坏点，(1155.88) 称为半稳定 Hodge 坐标；
不把它称作 crystalline Bloch–Kato logarithm。

这个结论是对原路径对象的比较，不只说存在某个与它同维的
半稳定表示。它也没有把下面的 rational 比较自动提升为
原有限 $E[p]$ moment 到四十三维 Fontaine–Laffaille 格的比较。

### 15.1. 全部局部三维 Heisenberg torsor 的分类

先固定同一 Tate generator 与 ordered 群律 (1155.1)。
在这个规范下，
$$
H^1_{\rm st}(L,\mathcal H_{\mathbb Q_p})
 =H^1(L,\mathcal H_{\mathbb Q_p}),
\qquad
H^1(L,\mathcal H_{\mathbb Q_p})
 \simeq\mathbb Q_p^2\times L^3
\tag{1155.89}
$$
是 pointed sets 的分类。最后的坐标依赖以下明确的
Frobenius/Hodge 规约；它本身不是某个函数的 dilogarithm 公式。

在忠实的三维表示中，graded Tate pieces 按
$\mathbb Q_p(2),\mathbb Q_p(1),\mathbb Q_p$ 排列。
逐中心解 Lang 方程可唯一消去 Frobenius 的三个上三角项，
因为 $1-p^{-j}\sigma$ 在 $L_0$ 上可逆，$j=1,2$。
于是可以且只可以取
$$
\Phi=\operatorname{diag}(p^{-2},p^{-1},1)\sigma,\qquad
N=n_aE_{12}+n_bE_{23},\qquad n_a,n_b\in\mathbb Q_p .
\tag{1155.90}
$$
确实，$N\Phi=p\Phi N$ 使两个一次系数为 $\sigma$-不变量；
中央 Lie 系数满足 $\sigma(n_h)=pn_h$，
迭代 $[L_0:\mathbb Q_p]$ 次后迫 $n_h=0$。

这里消失的只是 **Lie 的中央 $N$ 分量**。在同一表示中仍有
$$
N^2=n_an_bE_{13},\qquad
\exp(tN)=
\mathcal H(tn_a,tn_b,t^2n_an_b/2).
\tag{1155.91}
$$
所以不能把中央 monodromy 的全部矩阵贡献删掉。
例如在 $u$ 的极点盘，两个 Kummer valuation 都可能非零。

在 (1155.90) 的固定 Frobenius frame 中，任何
$\mathcal H(L)$ 点都给一个与原 weight filtration 严格相容、
graded 为上述三个 Tate filtration 的 Hodge filtration。
这是两个**严格 filtered extensions**，两端为弱可容许
Tate objects。Colmez–Fontaine Proposition 3.4 说明弱可容许
对象对这种扩张封闭，Theorem A 再给实际半稳定表示。
不能只核总空间的 $t_H=t_N$ 而省去子对象的不等式。
由于 $F^0\mathcal H=1$，这份 Hodge filtration 恰有三个
$L$ 坐标；Lang 规约后没有尚可任意移动的 Frobenius gauge。

这构造出了每个 Kummer pair 的半稳定 lift：
两个一次槽由 valuation 与 logarithm 分别分类。
另一方面，
$$
H^2(L,\mathbb Q_p(2))=0,\qquad
H^1(L,\mathbb Q_p(2))
 =H_f^1(L,\mathbb Q_p(2))\simeq L .
$$
前式由 local duality 与
$H^0(L,\mathbb Q_p(-1))=0$；
后式由同一 duality、Euler characteristic 和
Bloch–Kato exponential 得到。
又 $H^0(L,\mathbb Q_p(1)^2)=0$，
所以同一 abelian quotient 的 lifts 是该中央 $H^1$ 的
自由齐性空间。任何 lift 与上面构造的半稳定 lift 的差
因此都是 crystalline。中央 twisting 保持半稳定性，
给 (1155.89) 的全称结论。

在 Fontaine 的
$N(\log[\widetilde p])=-1$ 规范下，
一次 Kummer class $\kappa(v)$ 的 $N$ 系数为 $v_p(v)$。
可直接在它的二阶扩张中取
$e_0-\log[\widetilde v]\,e_1/t_{\rm cyc}$ 核出这个正号。
因此对 $\mathscr D_u$，
$(n_a,n_b)=(v_p(u),v_p(1-u))$。
采用以 uniformizer 为基的 log-crystal 记号时，
必须同时作 ramification-index 的 $N$ 归一；
不把 $v_L(\pi)=1$ 与 $v_p(p)=1$ 混用。

分类证明只保证半稳定性及规范参数的数目。
(1155.88) 的**实际中央值**由以下同一 variation 的比较支付，
不从 (1155.89) 的维数推出来。

### 15.2. 已刊比较定理确实允许点所在域分歧

令
$$
\overline Y=\mathbb P^1_{\mathbb Z_p},\qquad
D=\{0,1,\infty\},\qquad Y=\overline Y-D .
$$
这是在未分歧底上的 smooth proper pair，且 $D$ 是相对
normal-crossing divisor。
本节所有分歧发生在取点 $u\in Y(L)$ 时；
不要求 $\mathcal O_L$ 本身成为未分歧底。

使用 Vologodsky 已刊论文的以下实际构造。
精确编号按其作者全文给出：

- §§10–11、Theorem 42 给这个 pair 上 Faltings 的
  filtered log $F$-crystal 到原 étale sheaf 的 exact、
  tensor-compatible fully faithful functor。
- Theorems 46–47、50 将 level $r$ 的 fundamental variation
  认成同一 étale path variation，范围
  $r\le(p-1)/2$。
- **Theorem 43 的点是任意有限扩张上的**
  $x:\operatorname{Spec}L\to Y_{\mathbb Q_p}$。
  它没有要求 $x$ 约化到 $Y$ 的内部，也没有要求 $L$ 未分歧。
- 该证明所用的 Theorem 44 先把 log-crystalline sections
  放进
  $\Psi^{\rm un}(x^*\mathcal E)\otimes B_{\rm st}$，
  并保持 Frobenius 及总 monodromy；随后才进入 $B_{\rm dR}$。

此处的标准 class-two path object 是 level three。
它的三维表示具有 Hodge 幅二；其对偶及所需的 tensor/evaluation
幅至多四。所有上述限制在 $p>37$ 时同时满足。
不需要在有坏约化的 full $p$-level 模型上直接套这个定理：
所用的 universal pair 始终是上面的三穿孔直线。

为明确这里不只得到一个 $B_{\rm dR}$ 同构，
记 Theorem 43 证明中的实际中间箭头为
$$
\alpha_{\mathcal E}:
 V_x\otimes_{\mathbb Q_p}B_{\rm st}
 \longrightarrow
 \Psi^{\rm un}(x^*\mathcal E)\otimes_{L_0}B_{\rm st}.
\tag{1155.92}
$$
对 $\mathcal E^\vee$ 同样有一个已经在 $B_{\rm st}$ 中定义的箭头。
两者与 evaluation/coevaluation 相容。
它们在 $B_{\rm dR}$ 中给同一定理的对偶同构，
故
$$
\alpha_{\mathcal E^\vee}^{\,\vee}\alpha_{\mathcal E}=1,
\qquad
\alpha_{\mathcal E}\alpha_{\mathcal E^\vee}^{\,\vee}=1
\tag{1155.93}
$$
先在 $B_{\rm dR}$ 中成立。
由 $B_{\rm st}\hookrightarrow B_{\rm dR}$ 单射，
(1155.93) 已在 $B_{\rm st}$ 中成立。
有限自由两端遂得实际的 $B_{\rm st}$ 同构。
这没有使用错误的命题
“一个矩阵在 $B_{\rm dR}$ 可逆，所以它的 $B_{\rm st}$ 行列式是单位”。

(1155.92) 的来源是同一个 log-crystalline pullback，
故保持 $\varphi$、总 $N$ 与 Galois 作用。
它的 $B_{\rm dR}$ 扩张保持滤过：
原 functor 按 $F^0\cap\varphi=1$ 构造，
Tate twists 给各个 filtration degree；
同一对偶 construction 给逆映射的过滤相容性，
因而比较严格保持原滤过。
对 families，连接由 crystal 的 pullback/Taylor
同构保持，不从一个孤立 fibre 的弱比较猜出连接。

### 15.3. 原根塔与 whole path variation 的同一性

本篇 §1 消费的是 R1133 §11 的**整个** pointed class-two
path/root 认同，不是仅在一个数值点上选同构：
原 $\alpha,\beta,\Gamma$ 的函数根及其全部相容 $p^r$ 层，
将两个一次路径生成元送到原 $\sigma,\tau$，
将交换子送到同一个 $\nu$；
(1155.3)–(1155.5) 又固定了算术作用和 ordered 中央的号。
因此这个认同同时 intertwines 实际几何 monodromy、
Galois 作用和同一 Tate generator。

可以用 $2\in Y(\mathbb Z_p)$ 作内部基点应用上节的
fundamental-variation 定理。
原切向点到 $2$ 的比较已由 §1–2 固定；
随后与同一 path variation 的 $2\to u$ 比较复合。
这里在 $2$ 处的刚化只固定**已经存在的 whole-variation
认同**的常数，不声称任意一个 fibre 的同构都会延伸。

Vologodsky 的 good-pair 构造在 Frobenius-fixed path 上
与 Coleman 的原平行运输一致；
其 §§1.19–1.21、§4 的唯一 Frobenius-fixed path
及 §12 的比较使用同一个 log crystal。
采用原 $\log_p p=0$ 分支后，令 $p_{\rm Hdg}$ 为唯一 Hodge
点、$p_\varphi$ 为唯一 Frobenius-fixed 点，便有
$$
p_\varphi=p_{\rm Hdg}\,G_{\rm st}(u).
\tag{1155.94}
$$
按 §1 已固定的方向，同一 KZ 方程给
$$
da=\frac{du}{u},\qquad
db=\frac{du}{u-1},\qquad
dh=b\,da .
$$
由原切向 leading 和在 $2$ 处的同一常数，
三个解正是
$\log_pu,\log_p(1-u),-\operatorname{Li}_2^p(u)$。
它们作为 Coleman functions 沿同一 Frobenius continuation
到达所有 $u\in Y(L)$。
这证明 (1155.88)，没有在每个坏盘重新添加一个中央常数。

在坏点，$p_\varphi$ 一般不被 $N$ 固定。
(1155.91) 的有序二次项因此仍在同一对象内。
当 $v_p(u)=v_p(1-u)=0$ 时，(1155.90) 给 $N=0$，
(1155.94) 就是原 crystalline 情形，
所以得到含分歧良好单位的准确 rational Bloch–Kato 读数。
本节不是把 Sakugawa Proposition 5.6 的未分歧前提直接删除，
而是用上述另外的已刊 log comparison 支付新增范围。

### 15.4. 实际 log pullback 保留法向的 divided-power 贡献

因为 $\overline Y$ proper，任何 $u\in Y(L)$ 都延伸为
$\operatorname{Spec}\mathcal O_L\to\overline Y$。
给 $\operatorname{Spec}\mathcal O_L$ 取由其闭点定义的 log
结构后，这是原 pair 的 log morphism。
即使 $u$ 约化到 $0,1,\infty$，原 log crystal 仍可实际拉回。

这一步怎样携带 Frobenius 也有显式来源。
取 $\pi\in\mathcal O_L$ 及其在 $\mathcal O_{L_0}$ 上的
Eisenstein polynomial $f(T)$。
Vologodsky §3.9 在
$$
\mathcal O_{L_0}[T]\bigl[f(T)^r/r!:r\ge1\bigr]^{\wedge}_p,
\qquad T\longmapsto T^p
\tag{1155.95}
$$
的 logarithmic PD realization 上构造
$\Psi^{\rm un}$，再取 $T=\pi$ 的 de Rham fibre。
Lemma 14 与 Theorem 15 保证该 rational tensor construction
不依赖临时 uniformizer。
其 log-period 中的 $N$ 要按 §15.1 的同一 Fontaine
规范换算；本节不改原 Tate generator。

所以 (1155.92) 是实际
$(\varphi,N)$ object 与原 étale fibre 的比较，
不是在 $\mathcal O_L$ 上制造一个不存在的 canonical
field Frobenius。
尤其，先取 $T=\pi$ 再天真地令 $\pi\mapsto\pi^p$，
不是 (1155.95) 的替代做法。

(1155.95) 恰保留
$f(T)^r/r!$ 及其 Frobenius 像。
因此本节并不删除 (1155.87) 的法向 carry：
含一个 $p$ 的定义理想误差，仍可能在强可除归一后留下单位。
原 $R_\psi(u)$ 的 formal formula 与本节比较属于同一个
rational path object；要将它变为特定算术 fibre 上的
Frobenius 矩阵，仍须实施这个 log pullback/period 运输。
不得把 $u^p\to u$ 的矩阵直接改名为同点 Frobenius。

### 15.5. 对原全部四线 primitive 的后果和剩余整接口

R1157 §12 的全参数表保证所有实际 primitive 都满足
$u\ne0,1,\infty$，并给出坏盘的精确阶和 leading 单位。
它们可能所在的分歧域、坏参数和 rank-one 点对
都在本节的范围内。因此每个**原函数根塔**
已有同源的 rational semistable KZ realization；
§13 的实际两输入运输、§14 的共同形式 $\psi$
可以在这一原对象中使用。

还须分开以下下一步：

1. R1158 的模 $p$ moment pushout 使用有限
   $E[p]$ 标记及其原权。把这些权随意提升到 $\mathbb Z_p$，
   并不自动给 $T_pE$ 上的 Galois-equivariant
   rational group morphism。
2. 若做原 finite transfer、root gauge 或改变四线 filling，
   必须继续保同一根、实际陪集和有序中央修正。
   (1155.92) 的张量自然性允许消费已经给出的这些态射，
   不能替代尚未构造的态射。
3. 已知 rational associatedness 不决定某个指定
   Galois-stable $\mathbb Z_p$ 格。
   从这些 raw Tate objects 到 R1147–50 的四十三格，
   仍须原相容 moment/整比较或等价的实际 lattice 识别。
   本节没有对分歧域使用 Fontaine–Laffaille，
   没有约掉 (1155.95) 的 PD 方向。
4. 原目标在真正比较后满足 $N=0$，
   不意味着每个 raw primitive 的 $N$ 或
   (1155.91) 的有序项分别为零。
   必须在完整群态射及所有加权项中完成相消。

因而本节闭合的是“实际坏含分歧 primitive 的 rational
associatedness 和中央 Hodge 常数”这一门。
原 $F_0$ 的 $z_{12}$ 及 global subtraction 的非零性
没有作为结论写入。

### 本节 primary 定位

- V. Vologodsky，*Hodge structure on the fundamental group and its
  application to $p$-adic integration*，Mosc. Math. J. **3** (2003),
  205–247，
  [期刊记录及 DOI](https://www.mathnet.ru/eng/mmj83)，
  [作者全文](https://arxiv.org/pdf/math/0108109)。
  本节亲读并使用作者全文 §3.9 / Lemma 14 / Theorem 15
  （PDF 第 13–14 页），§§10–12 / Theorems 42–44
  （PDF 第 32–35 页），§§13–16 / Theorems 46–47、50
  及 Corollary 51（PDF 第 36–40 页），
  以及 §§1.19–1.21、§4 的 good-pair path。
  作者全文的 theorem 编号在这里明确标注；
  期刊 DOI 为 10.17323/1609-4514-2003-3-1-205-247。
  未使用其 §1.10 所述、但该文没有证明的
  “任意 generic-fibre morphism”扩张版自然性；
  本节 universal pair、basepoint、crystal pullback 与
  tensor operations 都是上述构造本身的态射。
- P. Colmez–J.-M. Fontaine，*Construction des représentations
  $p$-adiques semi-stables*，Invent. Math. **140** (2000), 1–43，
  DOI 10.1007/s002220000042，
  [作者全文](https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf)。
  使用 Theorem A、§3.4 Proposition 3.4 的严格扩张，
  及 §4.1 的 admissible comparison。
- 原切向路径、KZ 号和全部根尺度仍逐字消费本篇 §1–4
  的 Nakamura–Wojtkowiak、Furusho、Sakugawa 来源；
  本节不改那些规范。

本节全部为纸面证明，无数学程序执行。

root 亲读 Vologodsky 作者全文 §3.9、Theorems 15/42–44/50、Corollary 51 及已刊记录，并亲读 Colmez–Fontaine Proposition 3.4 / Theorem A。逐项核 Lang 规约、严格扩张、N²/有序半平方、Bst 中的两个实际对偶箭头与原 whole path 刚化；原 finite moment/四十三格与 PD carries 仍保持所列边界。无数学程序执行。
