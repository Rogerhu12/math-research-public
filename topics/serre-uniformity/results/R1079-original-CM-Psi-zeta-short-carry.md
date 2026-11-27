# R1079：两种原 CM 曲线的实际 Ψ–ζ 低矩形与完整 p 次 carry

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；o1_theta；
o2 对实际 eigen-$T$、低阶分母及 formal-log carry 范围独立纸核。

**已证明。** 在原 $j=0$ 惰性行及原 $j=1728$ 惰性行，
取 R1021/R1071 的实际整 CM eigenparameter $T$，并将其 tangent
按原 $\omega=dx/(2y)$ 归一为 $1$。原首极 $T^{-p}$ 的全局
Deuring primitive $\Psi$ 满足
$$
\boxed{\qquad
 \Psi(T)\equiv Z_{<p}(T)^p+\delta T\pmod{T^{p^2}},
 \qquad
 Z_{<p}(T)=T^{-1}
 -\sum_{\substack{4\le d\le p-1\\d\ {\rm even}}}
        \overline{G_d}\,T^{d-1}.
 \qquad}
\tag{1079.1}
$$
这是特征 $p$ 中的 Laurent congruence；差属于 $T^{p^2}k[[T]]$。
$G_d$ 保留原 additive-coordinate Hurwitz 归一化，$\delta$ 保留
$d\Psi=\delta\omega$ 的实际单位。$(\cdot)^p$ 是整项 Frobenius，
不能在一般系数域上擅去掉系数的 $p$ 次幂。

本文证明包括双变量 Laurent 加法律、首负 $p$ 极的代换损失、
完整短分母及最后可能的 $T^p$ 加性项。没有把一条含首 $p$ 极的
characteristic-zero $\zeta$ 级数整体约化；没有从 (1079.1) 推出
原 $e$、短 $\eta_k,\nu_k$ 或 Gaussian 共振高 $G$ 的单位。

## 1. 同一个实际模型、微分与参数

取 $p\ge41$，工作于包含所需 CM 单位的不分歧完美剩余域 $k$。
允许的两个原模型是
$$
\begin{array}{c|c|c}
\text{模型}&\text{惰性条件}&\text{实际 CM 单位群}\\ \hline
E_0:y^2=x^3+b,\quad b\ne0&p\equiv5\pmod6&\mu_6\\
E_4:y^2=x^3+a x,\quad a\ne0&p\equiv3\pmod4&\mu_4 .
\end{array}
\tag{1079.2}
$$
$a,b$ 是同一 good CM lift 的参数约化；微分始终是
$\omega=dx/(2y)$。本篇先在同一个 lift 上取实际 CM formal group，
再约化，绝不把不同 first lift 的 formal log 混用。

记 $D=d/\omega$，故
$$
Dx=2y,\qquad Dy=3x^2+a.
$$
原 tangent-one Weierstrass 参数为 $z_O=-x/y$。R1021 的整 CM
eigenparameter $T$ 与原 $z_O$ 有相同 tangent，且受完整
$\mu_{p^2-1}$ framing 以权一作用。R1071 §11 已证明，在同一个
lift 上的形式对数 $L$ 满足
$$
L(z_O(T))=T+O(T^{p^2}).
\tag{1079.3}
$$
这里在 $<p^2$ 范围内的系数全部整；本篇不要求、也不使用
第 $p^2$ 项的系数整性。

以下两个**整形式环**中的估计分别由 framing 齐次性直接得到：
$$
\omega=\bigl(1+O(T^{p^2-1})\bigr)dT,
\qquad
F(T,S):=T(P+Q)=T+S+\text{总次数至少 }p^2.
\tag{1079.4}
$$
因为 $T(-P)=-T(P)$，还准确有
$$
F(T,S)=(T+S)\bigl(1+E(T,S)\bigr),
\qquad \operatorname{ord}_{\rm tot}E\ge p^2-1.
\tag{1079.5}
$$
这是实际 formal group 的整恒等式。后面处理 $\Psi$ 的首极时，
使用 (1079.5)，不将 (1079.3) 直接代入一条未整的高阶 Laurent 级数。

## 2. 原 Ψ 的归一化及两行的单位 δ

### 2.1 j=0：原 R1061 的 Ψ

设 $p=6N+5$。令
$$
\Psi=yx\sum_{j=0}^{N}a_jx^{3j},\qquad a_N=-1,
\qquad
\frac{a_j}{a_{j-1}}
 =-\frac{6j-1}{b(6j+2)}
 \quad(1\le j\le N).
\tag{1079.6}
$$
直接用 $D$ 计算得
$$
D\Psi=\delta,\qquad \delta=2b a_0\ne0.
$$
全部分子、分母均为单位：$6j-1$、$6j+2$ 严格位于 $1,\ldots,p-1$，
且 $b\ne0$。最高次项的导数系数是 $6N+5=p$，约化为零。

在 R1061 的实际模型 $b=-108$ 上，这正是该文 §6 的
$\Psi=VU S(U^3)$ 和 $\delta=-216a_0$，没有另选 scalar。
因为 $x\sim T^{-2}$、$y\sim-T^{-3}$ 及 $a_N=-1$，
$\Psi$ 的首极准确为 $T^{-p}$。

### 2.2 j=1728：同一首极归一的 Ψ

写 $p=4r-1$。令
$$
\Psi=y\sum_{j=0}^{r-1}c_jx^{2j},\qquad c_{r-1}=-1,
\qquad
\frac{c_j}{c_{j-1}}
 =-\frac{4j-1}{a(4j+1)}
 \quad(1\le j\le r-1).
\tag{1079.7}
$$
由于
$$
D(yx^{2j})=(4j+3)x^{2j+2}+a(4j+1)x^{2j},
$$
递推准确给
$$
D\Psi=\delta,\qquad \delta=a c_0\ne0.
$$
分子最高 $p-4$，分母中整数最高 $p-2$，全部为单位。
最高项导数系数 $4(r-1)+3=p$ 消失；首极仍是 $T^{-p}$。
此处没有把 $j=0$ 的三次递推直接套到四次 CM 行。

### 2.3 唯一性、实际角色与完整加法律

上述 $\Psi$ 是奇函数，仅在 $O$ 有 pole，阶恰为 $p$。
由 $d\Psi=\delta\omega$，其 Laurent expansion 的负幂只能是
$p$ 的倍数；因此在任意同 tangent 的原局部参数中，负主部
只有所规定的 $T^{-p}$。

取 $\xi\in\mu_6$ 或 $\mu_4$。原 CM automorphism 满足
$T\mapsto\xi T$、$\omega\mapsto\xi\omega$。
因为 $p\equiv-1$ 模相应 CM 单位群的阶，
$\Psi(\xi P)-\xi\Psi(P)$ 的导数为零、首负主部抵消，
并且它没有其它 pole；故为常数。奇性将该常数杀掉。因此
$$
\Psi(\xi P)=\xi\Psi(P).
\tag{1079.8}
$$

始终用下列原 slope 归一：
$$
m(P,Q)=\frac{y(P)-y(Q)}{x(P)-x(Q)}.
$$
两行都准确满足
$$
\boxed{\quad
\Psi(P+Q)-\Psi(P)-\Psi(Q)=m(P,Q)^p.
\quad}
\tag{1079.9}
$$
$j=0$ 时这就是 R1061 §6 已付的原加法律。为同时支付 Gaussian
范围，可直接固定一般 $Q$ 作主部证明：两边之差对 $P$ 的微分为零；
可能的 pole 仅为 $P=O,-Q$。在 $O$，$m(P,Q)=-T^{-1}+O(T)$，
其 $p$ 次幂准确抵消 $-\Psi(P)$ 的负主部；在 $-Q$，
以 $T(P+Q)$ 为参数，slope 的首项为其逆，故抵消
$\Psi(P+Q)$ 的负主部。差因而为常数。
在 $P\to O$ 时，slope 的常数项为零，所得常数也是零。
一般 $Q$ 的恒等式延拓到整个 $E\times E$ 的函数域。

这里 coefficient 是 $+1$，不是 $1/2$。标准
$\zeta$ 加法中的 $1/2$ 与 $x' = 2y$ 正好抵消，见下一节。

## 3. 只约化安全的 ζ jet

原 characteristic-zero Hurwitz 常数的定义为
$$
x(z_{\rm add})=z_{\rm add}^{-2}
 +\sum_{\substack{d\ge4\\d\ {\rm even}}}
      (d-1)G_d z_{\rm add}^{d-2},
$$
$$
\zeta(z_{\rm add})=z_{\rm add}^{-1}
 -\sum_{\substack{d\ge4\\d\ {\rm even}}}
       G_d z_{\rm add}^{d-1},\qquad \zeta'=-x.
\tag{1079.10}
$$
$z_{\rm add}$ 的 differential 就是原 $\omega$。

对 $4\le d\le p-3$ 的偶数，$G_d$ 是 $p$-整的：
在 R1075 的 coefficient-one Eisenstein 规范中，
$G_d=2\mathcal E_d/(d-1)!$；阶乘是单位，而
von Staudt 的可能 $p$ 分母要求 $p-1\mid d$，这里不发生。
剩下的 $d=p-1$ 在 (1079.2) 两行中都**严格为零**：
$j=0$ 的 $G_d$ 只在 $6\mid d$ 时可能非零；
$j=1728$ 的 $G_d$ 只在 $4\mid d$ 时可能非零；
相应惰性条件排除了 $d=p-1$。

因此
$$
Z_{<p}(T)=T^{-1}
 -\sum_{\substack{4\le d\le p-1\\d\ {\rm even}}}
       \overline{G_d}T^{d-1}
\tag{1079.11}
$$
确实是在原系数域上的有限 Laurent polynomial。
第一个没有纳入的可能项是 $d=p+1$，指数是 $p$；
其系数可能含 $1/p$，本篇从来不约化它。

NIST DLMF [23.10.2](https://dlmf.nist.gov/23.10.E2) 的标准式为
$$
\zeta(u+v)-\zeta(u)-\zeta(v)
 =\frac12\frac{\zeta''(u)-\zeta''(v)}
                   {\zeta'(u)-\zeta'(v)}
 =\frac{y(u)-y(v)}{x(u)-x(v)}.
\tag{1079.12}
$$
最后一步用 $\zeta'=-x$、$\zeta''=-2y$，完整保住符号与 $2$。

在同一个 actual $T$ 中，(1079.3) 使 (1079.12) 的
**总次数小于 $p$** 部分与 additive variable 中完全相同。
这些有限 homogeneous pieces 的系数全整，所以可先逐片约化。
得到
$$
Z_{<p}(T+S)-Z_{<p}(T)-Z_{<p}(S)
 =\bar m(T,S)+O_{\rm tot}(\ge p).
\tag{1079.13}
$$
这只是合法短 jet 的断言，不是对完整 $\zeta$ 级数的约化断言。

## 4. 双变量 Laurent 截断与首极精度

为使 $O_{\rm tot}$ 含义准确，可在按总次数完备的 graded
Laurent 环中工作，其每个 homogeneous piece 位于
$$
k[T,S,T^{-1},S^{-1},(T+S)^{-1}],
\qquad \deg T=\deg S=1.
\tag{1079.14}
$$
slope 的 $T-S$ 分母因子由 numerator 消去；
剩余极沿 $T=0,S=0,T+S=0$。
实际 $F(T,S)$ 与 $T+S$ 的关系由 (1079.5) 保证，
因此所有下面的代换都在同一个过滤环中合法。

从 (1079.4) 和 $d\Psi=\delta\omega$，先逐个 Laurent 系数得
$$
\Psi(T)=T^{-p}+\delta T+
 \sum_{j=1}^{p-1}a_jT^{jp}+O(T^{p^2}).
\tag{1079.15}
$$
在这个范围内，除线性项外，非 $p$ 倍指数的导数系数均是单位，
故必须为零；常数由奇性为零。

现在比较 $\Psi(F(T,S))$ 与 $\Psi(T+S)$。

- 首负 $p$ 极由 (1079.5) 给
  $$
  F(T,S)^{-p}-(T+S)^{-p}
   =(T+S)^{-p}\bigl((1+E)^{-p}-1\bigr).
  $$
  特征 $p$ 中 $(1+E)^{-p}=(1+E^p)^{-1}$，
  所以最早总次数至少
  $$
  -p+p(p^2-1)=p^3-2p>p^2.
  $$
- 线性项的差为 $\delta(F-T-S)$，总次数至少 $p^2$。
- 对 $T^{jp}$，代换差还含 $E^p$，
  其总次数至少 $jp+p(p^2-1)>p^2$。
- $O(T^{p^2})$ 的代换仍从总次数 $p^2$ 起。

因而真实 (1079.9) 在总次数 $<p^2$ 内准确给
$$
\Psi(T+S)-\Psi(T)-\Psi(S)
 =\bar m(T,S)^p+O_{\rm tot}(\ge p^2).
\tag{1079.16}
$$
另一方面，(1079.13) 在特征 $p$ 中升 $p$ 次，得到
$$
Z_{<p}(T+S)^p-Z_{<p}(T)^p-Z_{<p}(S)^p
 =\bar m(T,S)^p+O_{\rm tot}(\ge p^2).
\tag{1079.17}
$$
所有跨项因 Frobenius 消失；不存在先除一个未知 $p$ 再约化的步骤。

## 5. 排尽最后的加性不定项

将 (1079.16) 减 (1079.17)，再减去 $\delta T$。
首负 $p$ 极相消，所得短 polynomial
$$
A(T):=\bigl(\Psi(T)-Z_{<p}(T)^p-\delta T\bigr)_{<p^2}
$$
只有 $T^{jp}$ 项、没有常数和线性项，并满足
$$
A(T+S)=A(T)+A(S)
\quad\text{在总次数 }<p^2.
$$
若 $2\le j\le p-1$，$T^{jp}$ 的二项式展开中
$T^pS^{(j-1)p}$ 的系数是
$\binom{jp}{p}\equiv j\ne0$。
不同 $j$ 的总次数不同，不能互相抵消。因此
$$
A(T)=c\,T^p.
\tag{1079.18}
$$

由 (1079.8)，$\Psi$ 的 CM 权是 $1$；
由 (1079.11)，$Z_{<p}$ 的 CM 权是 $-1$，
故 $Z_{<p}^p$ 的权是 $-p\equiv1$。
$\delta T$ 也有权 $1$。所以 $A(\xi T)=\xi A(T)$。
然而 $T^p$ 的权是 $p\equiv-1$。
取原 $\mu_6$ 或 $\mu_4$ 中 $\xi^2\ne1$ 的元素，便得
$c(\xi^{-1}-\xi)=0$，故 $c=0$。
这证明 (1079.1)，包括原单位及完整 short carry。

## 6. 可直接消费的系数与准确边界

对所有上述安全偶数 $d$，(1079.1) 给
$$
[T^{p(d-1)}]\Psi(T)=-\overline{G_d}^{\,p},
\qquad
[T]\Psi=\delta.
\tag{1079.19}
$$
在 $j=0$ 行，R1075 的新单位因此也读作
$$
[T^{p(p-6)}]\Psi(T)
 =-\overline{G_{p-5}}^{\,p}\ne0.
\tag{1079.20}
$$
这只是同一个原 $\Psi$ 的已指定高系数；它不等于
R1076 的短 $\eta_k$ 或 $\nu_k$。R1077 的加权 primitive
系数也仍保其原权，不被 (1079.20) 自动改成短端点。

Gaussian 行的 (1079.19) 同样可消费，但它只读取低
$G_d$ 的 $p$ 次系数。若要从中反解近 $p^2$ 的其它
Hurwitz 系数，必须保实际下位卷积、共振项及 first-lift
尺度，本文没有支付这种新反解或单位性。

最后，(1079.1) 不能写成
“把完整 characteristic-zero $\zeta(z_{\rm add})^p$
约化到 $p^2$”。formal log 在第 $p^2$ 项可能有 $p$ 分母；
将它直接代入一条具有负 $p$ 极的级数，会使 carry 提前进入。
本文避开这一步：全部高精度推导在**实际整 eigen-$T$**
和其整 formal group 中完成，只使用安全的有限
$Z_{<p}$。所证明的范围正是差属于 $T^{p^2}k[[T]]$，
不声称更高阶或任意 supersingular 点的同一归一式。

## 7. 来源与验证范围

- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：
  同一整 CM framing、原 $T$ 与 actual level 作用。
- [R1071](R1071-original-p-local-cuspidal-label-polynomials.md) §11：
  同 first lift 的原 formal log、$<p^2$ 整性及 actual eigen-$T$。
- [R1061](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)
  §6：原 $j=0$ 的 $\Psi$、$\delta$ 与 slope 的 $+1$ 加法律；
  本篇 §2.2–2.3 独立补齐 Gaussian 同规范。
- [R1075](R1075-original-Hurwitz-unit-and-first-cuspidal-slope.md)：
  原 coefficient-one / Hurwitz 尺度以及 $G_{p-5}$ 单位；
  全部实际标架在本篇保持。
- NIST DLMF [23.10.2](https://dlmf.nist.gov/23.10.E2)：
  已亲读标准 $\zeta$ 加法；本篇明确代入 $\zeta'=-x$、
  $\zeta''=-2y$，不省略 $1/2$ 的来源。

全部证明为纸面推导；没有执行数学程序、没有新数值窗口，
也没有重跑既有回执。原 $e/f_N$、原筛选同标签及主目标仍开放。
