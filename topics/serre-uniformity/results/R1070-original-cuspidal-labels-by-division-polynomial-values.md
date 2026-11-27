# R1070：原尖点 Kummer 标签的除法多项式评价与全部相位付款

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route，root 复核。
全文为纸面证明，没有数学程序执行。
o2_high_coefficient 已独立回读 R1064 的原指数及 leading 规范，
逐式核准本文的平滑方向、范数、实下降与 $2,3$ 处应用。

**已证明。** 对完整原曲线 $X=X_{\rm ns}^+(p)$、$p>37$，
R1064 固定的每个 forced character 基 $u_\chi$ 的规范 Kummer 标签，
可直接由原椭圆曲线的奇数除法多项式在其实际 $p$-torsion 上的值给出。
公式保留原整数指数提升、实际 necklace、Weil pairing 和 cyclotomic embedding；
不需要计算或猜测一个额外 cusp 常数，也没有取会杀掉原类的 $12p$ 次幂。

这给出了 R1068 有限点输入的实际函数值接口。
它没有证明不同辅助素的共同像为空，也没有排除非 CM 有理点。
§§1–9 先在 forced 范围付款；§10 进一步证明 smoothing 的异常角色
在原 cusp 模块中实际缺席，将同一公式扩到完整实际 $V$，
并给整个家族的精确辅助可见性判据。
R1069 的 good 子模块仍保其无条件 $\Omega(p/\log p)$ 下界。

## 1. 沿用原基，不重新选择一个相似的 modular unit

记
$$
K_0=\mathbf Q(\zeta_p),\qquad
F=K_0^+,\qquad
G=\operatorname{Gal}(F/\mathbf Q)
  =\mathbf F_p^\times/\{\pm1\},\qquad
m=(p-1)/2.
\tag{1070.1}
$$
全部 $m$ 个 cusp 及其原参数、$U_p/pU=V$、
规范函数 $f_u=u^m/A(u)$ 和标签 $\Phi_y(u)$ 均使用 R1064 的定义。
本节的 $F^\times/F^{\times p}$ 等 Kummer 商采用加法记号。

固定
$$
\chi=\chi_j=\omega^{-2j},\qquad
1\le j\le \lfloor p/4\rfloor-1.
\tag{1070.2}
$$
选取 R1064 已固定的原整数
$$
n_h\equiv m^{-1}\chi(h)^{-1}\pmod p,\qquad
\sum_{h\in G}n_h=0.
\tag{1070.3}
$$
令 $\delta\in\mathbf F_p^\times$ 为原非平方，
$z=a+b\sqrt\delta$，$N(z)=a^2-\delta b^2$。
保持 Carlucci 原索引与 R1064 (1064.15)–(1064.18)：
$$
f_\chi=\prod_{z\in\mathbf F_{p^2}^\times/\{\pm1\}}
       g_z^{\,n_{[Nz]}}\in K_0(X)^\times,\qquad
w_\chi=f_\chi\overline{f_\chi}\in F(X)^\times.
\tag{1070.4}
$$
其原 $V$ 类为 $[w_\chi]_V=2u_\chi$。

本文明确消费 R1064 已完整证明的两项来源：

1. 对 augmentation 为零的整数范数指数向量，原 Siegel product
   是实际 modular unit；改变指数一个 $p$ 倍的 augmentation-zero 向量，
   便改变一个实际 modular unit 的 $p$ 次幂，仍保原常数相位。
2. 若指数模 $p$ 是 (1070.3) 的一个标量倍数，则取真实
   $K_0/F$ 范数后的全部 cusp leading classes 之和为零。
   对 (1070.4) 具体为
   $$
   [\operatorname{lc}_{c_h}(w_\chi)]
   =\chi(h)\chi(-\delta)^{-1}e_{\chi^2}[\varpi_1],
   \qquad
   [A(w_\chi)]=0
   \quad\text{in }F^\times/F^{\times p}.
   \tag{1070.5}
   $$
   这里所有原 cusp 都在和中；改变实际参数只乘 $p$ 次幂。

(1070.5) 是本文消去规范常数的依据。
仅知道两个函数有相同 $V$ 类不足以略去这个 leading-coefficient 步骤。

## 2. 选一个可逆的真实平滑整数

取正整数 $c>1$，满足
$$
(c,6p)=1,\qquad c\bmod p\text{ 生成 }\mathbf F_p^\times.
\tag{1070.6}
$$
对一个另给的辅助素 $\ell\ne p$，还可要求 $(c,\ell)=1$；
中国剩余定理保证这些条件可以同时满足。
定义
$$
\kappa_\chi=c^2-\chi(c^2)\in\mathbf F_p.
\tag{1070.7}
$$
在 (1070.2) 的真实范围内，
$$
\kappa_{\chi_j}
=c^{-4j}(c^{4j+2}-1)\ne0,
\tag{1070.8}
$$
因为 $0<4j+2<p-1$，而 $c$ 是原始剩余类。

这个范围不能随意扩大。当 $p\equiv3\pmod4$ 时，
偶角色 $\chi=\omega^{(p+1)/2}$ 满足
$\chi(c^2)=c^2$，对每个 $c$ 都有 $\kappa_\chi=0$。
它位于本 forced 范围之外。
到本节为止不据此扩大角色范围；R1069 的 good∩forced 全满足 (1070.8)。
后继 §10 从原 Stickelberger 格证明该异常角色的实际 $V_\chi$ 为零，
据此才将可逆性扩至完整实际 $V$。

## 3. 除法多项式乘积在原模型上的定义

设 $E$ 是特征不整除 $c$ 的域上的椭圆曲线，采用任意广义 Weierstrass 方程。
奇数 $c$ 的标准除法多项式 $\psi_c$ 满足
$$
\operatorname{div}(\psi_c)=E[c]-c^2[O],
\qquad \psi_c(-P)=\psi_c(P).
\tag{1070.9}
$$
这里可以完全代数地检查：在代数闭包上，取
$$
\psi_c=c\prod_{T\in(E[c]\setminus\{O\})/\{\pm1\}}
                  (x-x(T)).
\tag{1070.10}
$$
每一因子的 divisor 是 $[T]+[-T]-2[O]$，
故得到 (1070.9)；整个集合 Galois-stable，乘积定义在基域。
它与通常的奇数除法多项式有相同 leading normalization。
后文实际上允许将 $\psi_c$ 乘任何只依赖 $E$ 的非零常数。

在原 full-level cover 上，令 $(P,Q)$ 为与
$g_{(a/p,b/p)}$ 对应的同一有序 $p$-torsion 基，
并记
$$
P_z=aP+bQ,\qquad
M_{c,\chi}(E;P,Q)=
 \prod_{z\in\mathbf F_{p^2}^\times/\{\pm1\}}
          \psi_c(P_z)^{-n_{[Nz]}}.
\tag{1070.11}
$$
$c$ 与 $p$ 互素，所以所有非零 $P_z$ 都不在 $E[c]$，
每个因子均有限且非零。
$c$ 为奇数使 $\pm z$ 的选择完全无影响。

每个范数类 $h\in G$ 恰有 $p+1$ 个 $\pm$-类，因此
$$
\sum_{z/\pm}n_{[Nz]}=(p+1)\sum_h n_h=0.
\tag{1070.12}
$$
于是将 $\psi_c$ 乘一个只依赖 $E$ 的常数不改变 (1070.11)。
改变 Weierstrass 方程时，除法多项式的共同 differential scaling
也是这种常数，因而严格抵消。
所以 (1070.11) 是椭圆曲线及原 level 数据的内在函数，
对几何同构和基变换相容。
这同时支付特征 $2,3$ 中的广义 Weierstrass 模型：
此时 $c$ 与 $6$ 互素，(1070.9)–(1070.12) 全部成立。

## 4. 原 normalizer 与实域下降，没有未跟踪的相位

先在固定 Weil pairing 的 full-level 分支上讨论。
原非分裂 normalizer 的元素是
$$
z\longmapsto az\quad\text{或}\quad z\longmapsto a\bar z.
\tag{1070.13}
$$
第一种的 determinant 为 $N(a)$，第二种为 $-N(a)$。
在 determinant 为一的几何子群中，
$N(z)$ 因而只可能乘 $1$ 或 $-1$。
原 $[N(z)]\in G$ 不变，(1070.11) 的全部指数被严格置换。
所以 $M_{c,\chi}$ 下降为 $K_0(X)$ 中的函数。

再取 determinant 为 $-1$ 的原共轭元素
$$
(a,b)\longmapsto(a,-b),\quad z\longmapsto\bar z.
\tag{1070.14}
$$
它在 full-level 常数域上诱导
$\zeta_p\mapsto\zeta_p^{-1}$，且逐项保持原范数指数。
(1070.11) 采用代数除法多项式，没有 Siegel 指标换代表时的根单位因子。
故有严格等式
$$
\overline{M_{c,\chi}}=M_{c,\chi},
\qquad M_{c,\chi}\in F(X)^\times.
\tag{1070.15}
$$
这里没有把任意 $\mathrm{GL}_2$ 换基都当成固定 cyclotomic embedding：
改变 determinant 时必须同时运输 Weil pairing 的指定根。
固定该根后，几何 normalizer 的不变性恰给所需的基无关性。

在非 cusp 部分，$M_{c,\chi}$ 是一个单位。
可由 (1070.11) 的因子直接看出，也可由下一节的
Kato–Siegel 函数与基变换看出。
因此它能在 R1068 的每个实际非 cusp 有限域点上取值，
包括有额外 automorphism 的 $j=0,1728$ 点。

## 5. 精确 Kato 平滑，以及为什么原 $p$-相位没有被丢掉

使用已发表的 Kato–Siegel 函数 $\vartheta_c(E)$。
其原定理给出一个随基变换相容的函数，满足
$$
\operatorname{div}\vartheta_c=c^2[O]-E[c].
\tag{1070.16}
$$
因此在每个椭圆曲线上存在只依赖 $E$ 的非零常数 $\lambda(E)$，
使
$$
\vartheta_c(E)=\lambda(E)/\psi_c.
\tag{1070.17}
$$
由 (1070.12)，这个常数在完整乘积中严格消去：
$$
M_{c,\chi}
=\prod_{z/\pm}\vartheta_c(E)(P_z)^{n_{[Nz]}}.
\tag{1070.18}
$$

为保住根单位，不能只引用
$\mathcal O(Y(p))^\times\otimes\mathbf Q$ 中的平滑恒等式。
以下直接核准其精确解析版本。

在 $\mathbf C/(\mathbf Z\tau+\mathbf Z)$ 上置
$$
\Theta(u,\tau)=q^{1/12}(t^{1/2}-t^{-1/2})
 \prod_{n>0}(1-q^nt)(1-q^nt^{-1}),
\quad q=e^{2\pi i\tau},\ t=e^{2\pi iu}.
\tag{1070.19}
$$
Scholl Theorem 1.2.1(v) 给
$$
\vartheta_c(u)
=(-1)^{(c-1)/2}
 \frac{\Theta(u,\tau)^{c^2}}{\Theta(cu,\tau)}.
\tag{1070.20}
$$
若 $u=r\tau+s$，采用 R1064 原 Siegel product 规范，有
$$
g_{r,s}=e^{\pi ir(r\tau+s)}\Theta(r\tau+s,\tau).
\tag{1070.21}
$$
把 (1070.19) 展开即得到原
$-q^{B_2(r)/2}e^{\pi is(r-1)}$ 和两列无限乘积。
在 $g_{r,s}^{c^2}/g_{cr,cs}$ 中，
(1070.21) 的两个二次指数严格相消。

将 $(cr,cs)$ 改回原固定代表时，只引入根单位。
这也可从
$$
\Theta(u+a\tau+b)
=(-1)^{a+b}e^{-\pi ia^2\tau-2\pi iau}\Theta(u)
\tag{1070.22}
$$
直接看出：与 (1070.21) 的指数合并后，
只剩 $e^{\pi i(-as+rb+ab)}(-1)^{a+b}$。
同样，改 $\pm$ 代表也只乘一个符号。
完整乘积中的 (1070.20) 全局符号由 (1070.12) 消去。
故得到实际函数恒等式
$$
M_{c,\chi}=\varepsilon\,
 \frac{f_\chi^{c^2}}{f_\chi^{[c]}},
\qquad
f_\chi^{[c]}=\prod_{z/\pm}g_{cz}^{n_{[Nz]}},
\tag{1070.23}
$$
其中 $\varepsilon$ 是根单位。

两侧函数定义在 $K_0(X)$；它的常数域为 $K_0$，
故 (1070.23) 中的 $\varepsilon$ 也在 $K_0$。
取真实 $K_0/F$ norm 后，
$\varepsilon\bar\varepsilon=1$，不是仅仅在有理化群中忽略它。
由 (1070.15)，准确得到
$$
M_{c,\chi}^{\,2}
=\frac{w_\chi^{c^2}}{w_\chi^{[c]}},
\qquad
w_\chi^{[c]}=f_\chi^{[c]}\overline{f_\chi^{[c]}}.
\tag{1070.24}
$$
这一步只取次数二的范数，$p$ 为奇数；
没有使用会杀掉待求 Kummer 类的 $p$ 次幂。

## 6. 整数指数提升、$V$ 类与全部 cusp leading 的结算

在 $f_\chi^{[c]}$ 中令 $v=cz$，其整数范数指数变为
$$
n'_h=n_{hc^{-2}}.
\tag{1070.25}
$$
原角色方向是
$$
n'_h\equiv\chi(c^2)n_h\pmod p.
\tag{1070.26}
$$
取任一整数 $t$ 提升 $\chi(c^2)$。
则 $n'_h-tn_h$ 是 $p$ 倍，且
$\sum_h(n'_h-tn_h)=0$。
原 Carlucci 乘积条件适用于除以 $p$ 后的整数向量，
所以其差确给一个实际 modular unit 的 $p$ 次幂。
取 norm 后也仍是一个实际 $F$-unit 的 $p$ 次幂；
指标代表的根单位已经在 (1070.24) 中严格消去。
由此
$$
[w_\chi^{[c]}]_V=2\chi(c^2)u_\chi.
\tag{1070.27}
$$
(1070.24) 与 $p\ne2$ 于是给
$$
[M_{c,\chi}]_V=\kappa_\chi u_\chi.
\tag{1070.28}
$$
特别地，$M_{c,\chi}$ 的 cusp divisor 是 $p$ 的倍数。

还须结算规范 $A$，不能只停在 (1070.28)。
(1070.5) 对原指数 $n$ 和重指标向量 $n'$ 都适用；
后者只是原模 $p$ 角色向量的标量倍数。
因此
$$
[A(w_\chi)]=[A(w_\chi^{[c]})]=0.
\tag{1070.29}
$$
在同一组实际 cusp 参数上取 (1070.24) 的全部 leading coefficient，
其乘法相容性给
$$
2[A(M_{c,\chi})]
=c^2[A(w_\chi)]-[A(w_\chi^{[c]})]=0.
$$
$p$ 为奇数，所以
$$
[A(M_{c,\chi})]=0
\quad\text{in }F^\times/F^{\times p}.
\tag{1070.30}
$$
这是规范常数消失的完整证明；它包含所有 cusp，
并保留原参数改变只乘 $p$ 次幂的事实。

## 7. 原标签的实际代数评价定理

令 $L/F$ 为任一域扩张，$\operatorname{char}L=0$；
或在 $\ell\ne p$ 的好整模型上约化到剩余域，
并取 $(c,\ell)=1$。
对任一原非 cusp 点 $y$，
由 (1070.28)–(1070.30) 和原规范定义，
$$
\boxed{\displaystyle
\Phi_y(u_\chi)
=\frac{m}{\kappa_\chi}
 \left[
 \prod_{z\in\mathbf F_{p^2}^\times/\{\pm1\}}
 \psi_c(P_z)^{-n_{[Nz]}}
 \right]
\quad\text{in }L^\times/L^{\times p}.
}
\tag{1070.31}
$$
这里 $\kappa_\chi^{-1}$ 在 $\mathbf F_p$ 中取值，
任意整数提升给相同 Kummer 类。

原覆盖及其规范标签在所有 $\ell\ne p$ 好约化已由 R1067 付款；
(1070.18) 是原非 cusp 整模空间上的单位恒等式，
故特征零证明的 (1070.31) 与这些约化相容。
在 cusp 也可对 $M$ 去掉其 $p$ 倍参数阶后取 leading coefficient；
所得值仍是 R1064 的原切向纤维。
$2,3$ 处因 $p>37$ 没有原有理 cusp，故实际有限点输入完全使用 (1070.11)。

公式对以下选择均保持不变：

- 改变原 $n_h$ 一个 $p$ 倍、augmentation-zero 的整数向量，
  只改变实际乘积的 $p$ 次幂；
- 改变 Weierstrass 方程、$\psi_c$ 的共同常数或 $\pm z$ 代表，
  由 (1070.9)、(1070.12) 严格抵消；
- 在同一 necklace 内改变保持指定 Weil pairing 的基，
  由原几何 normalizer 不变性严格抵消；
- 换一个满足 (1070.6) 的平滑整数，仍计算同一个
  $\Phi_y(u_\chi)$，不能把不同 $c$ 所得值当成独立约束。

## 8. 用于同一全局标签的有限域条件

设 $\mathfrak q\mid\ell$ 为 $F$ 的素点，
$k_\mathfrak q=\mathbf F_q$。
若 $p\nmid q-1$，则 $k_\mathfrak q^\times/k_\mathfrak q^{\times p}=0$，
该原 Kummer 分量不可见。
这是 R1064 的实际不可见情形，本文不增加虚构读数。

若 $p\mid q-1$，选与 $\mathfrak q$ 相容的
$\zeta_p$ 的约化及原 Weil pairing，定义
$$
\mathcal K_{\ell,\chi}(y)
=M_{c,\chi}(y)^{\,m\kappa_\chi^{-1}(q-1)/p}
\in\mu_p(k_\mathfrak q).
\tag{1070.32}
$$
$M$ 的各因子可以在完整 $E[p]$ 的分裂域中计算；
(1070.15) 和 $y\in X(\mathbf F_\ell)$ 保证整个乘积在
$k_\mathfrak q$ 中。不是把任意一条 torsion line 的值当成标签。

采用 R1067/R1069 的原圆单位基
$\beta_\chi=e_\chi[\eta_a]$，
若同一个实际 $p$-disk 给出唯一全局候选
$\phi(u_\chi)=c_\chi\beta_\chi$，则它在辅助素的必要条件是：
存在同一个
$$
y\in X(\mathbf F_\ell)
$$
使全部可见 $\chi$ 同时满足
$$
\mathcal K_{\ell,\chi}(y)
=\overline{\beta_\chi}^{\,c_\chi(q-1)/p}.
\tag{1070.33}
$$
右侧以 R1067 给出的真实圆单位乘积代表计算。
它没有选择一个新的单位线替代原基。

在 $\ell=2,3$ 时，
(1070.33) 的完整点输入正是 R1068 的全部模型、全部 stable necklaces
再取几何 isomorphism 商。
不能只保 Frobenius 的特征多项式、任意 conjugacy class 或一个 twist：
那些数据只付点数，不付 (1070.11) 的原 torsion 值。
一旦取一个实际 $y$，所有 $\chi$、所有相容 cyclotomic embeddings
和所有辅助素都必须使用同一个全局候选 $\phi$。

由 R1069，取
$W=W_{\rm good}\cap W_{\rm for}$，
上述唯一全局候选和实际辅助评价对每个 $p>37$ 成立，
并保其已证 $\Omega(p/\log p)$ 的角色数。
本文没有宣称 (1070.33) 在任何范围已经无解。
真正尚欠的是这个同标签有限点条件的统一排除。

## 来源与准确消费范围

- R1064 §§3–4：原 $n_h$、Carlucci 指数条件、
  $w_\chi$ 与 $u_\chi$ 的尺度、全部 cusp 的平方角色 leading 公式；
  §§1–2、6：规范 torsor 标签及有限域意义。
- R1067：所有 $\ell\ne p$ 的好整模型和原 p-only 标签，
  原圆单位基的实际辅助约化；R1069：逐 good 角色的唯一全局候选，
  以及 forced good 角色的无条件定量下界。
- R1068：$2,3$ 处完整实际点输入、twisted Burnside、
  stable necklace 和 Weil pairing 的范围。
- A. J. Scholl, *An introduction to Kato's Euler systems*,
  in *Galois Representations in Arithmetic Algebraic Geometry*,
  Cambridge University Press (1998), 379–460,
  DOI 10.1017/CBO9780511662010.011。
  作者全文 https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf ，
  §1.2 Theorem 1.2.1，印刷第384页，尤其 (i)、(ii)、(v)；
  其证明从印刷第385页开始。
  本文使用实际函数、基变换与精确 $\Theta$ 式，
  没有仅在 units $\otimes\mathbf Q$ 中抹掉 torsion。
- K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*,
  Astérisque 295 (2004), 117–290。
  https://www.numdam.org/article/AST_2004__295__117_0.pdf ，
  §1 Proposition 1.3、§1.4 与 Lemma 1.7，印刷第121–123页。
  这些原文给实际 torsion section、base change、
  full-level $\mathrm{GL}_2$ 行为及 determinant 对 cyclotomic 常数域的作用。
  精确解析符号以已亲读的 Scholl (v) 为准，
  不采用 PDF OCR 中损坏的 Kato (1.3)(3) 指数。

root 已亲读 Scholl Theorem 1.2.1 及证明、Kato §§1.3–1.10 的相应原文，独核实际除法多项式、全部相位、实下降及 cusp 规范；没有消费损坏的 OCR 指数。


## 9. 任意整数平滑与2、3处的低次数原评价

### 9.1 全部向量乘积支付偶数平滑

取任意整数 $c>1$、$(c,p)=1$；
在辅助特征 $\ell$ 还要求 $(c,\ell)=1$。
不再要求 $(c,6)=1$，但改用全部非零 level 向量：
$$
M_c^{\mathrm{all}}=
\prod_{z\in\mathbf F_{p^2}^{\times}}
\psi_c(P_z)^{-n_{[Nz]}}.
\tag{1070.34}
$$
偶数 $c$ 时 $\psi_c(-P)=-\psi_c(P)$；
全部向量乘积使 $\pm$ 代表无歧义。
模型的共同常数仍因 $\sum_z n_{[Nz]}=0$ 严格消去。
原 normalizer 及 $\sigma_{-1}$ 只置换全部向量，故
$M_c^{\mathrm{all}}\in F(X)^\times$。

本扩展不引用任意 $c$ 的 canonical Kato normalization。
直接使用 (1070.19) 的 $\Theta$，置
$$
R_c(u)=\Theta(u)^{c^2}/\Theta(cu).
$$
(1070.22) 表明它对 $u\mapsto u+1,u+\tau$ 均不变：
quasiperiod 的二次及线性指数全相消，
剩余符号为 $(-1)^{c^2-c}=1$。
它的 divisor 是 $c^2[O]-E[c]$，因此
$R_c=\lambda(E)/\psi_c$。
全部指数之和为零消去 $\lambda(E)$。
(1070.21) 的二次相位消去、指标取代表的根单位、
以及实际 $K_0/F$ 范数步骤照用。

全部 $z$ 的 raw Siegel product 是 $f_\chi^2$ 乘根单位，
所以准确得到
$$
(M_c^{\mathrm{all}})^2=
\left(w_\chi^{c^2}/w_\chi^{[c]}\right)^2.
\tag{1070.35}
$$
这里仍是实际函数等式，未先有理化单位群。
沿用同一个整数换标 $n'_h=n_{hc^{-2}}$，
以及全部 cusp leading 计算，得到
$$
[M_c^{\mathrm{all}}]_V=2\kappa_\chi(c)u_\chi,\qquad
[A(M_c^{\mathrm{all}})]=0,\qquad
\kappa_\chi(c)=c^2-\chi(c^2).
\tag{1070.36}
$$
因此，只在 $\kappa_\chi(c)\ne0$ 时，
$$
\boxed{\Phi_y(u_\chi)=
\frac{m}{2\kappa_\chi(c)}[M_c^{\mathrm{all}}(y)].}
\tag{1070.37}
$$
奇数 $c$ 时 $M_c^{\mathrm{all}}=M_{c,\chi}^2$，
恰恢复 (1070.31)。

若 $\kappa_\chi(c)=0$，实际 $M_c^{\mathrm{all}}$
本身是 $F(X)$ 中的 $p$ 次幂：
其 $V$ 类为零给 $M_c^{\mathrm{all}}=a v^p$，
其中 $a\in F^\times$、$v$ 为实际 modular unit；
而 $[A(M_c^{\mathrm{all}})]=m[a]=0$，
$m$ 是模 $p$ 单位，迫 $a\in F^{\times p}$。
故该退化平滑不给原标签，
不能除以零后从特殊函数的值推出原标签为零。

### 9.2 特征2的实际三除法多项式

在 $\ell=2$ 取 $c=3$。标准广义 Weierstrass 式
$$
\psi_3=3x^4+b_2x^3+3b_4x^2+3b_6x+b_8
$$
在 R1068 的全部原模型上直接成为：

| 原模型 | $\psi_3$ |
| --- | --- |
| $y^2+xy=x^3+A x^2+1$ | $x^4+x^3+1$ |
| $y^2+y=x^3+A x+B$ | $x^4+x+A$ |

这些式由原 $b_i$ 逐项代入，不使用一个猜测的 Siegel 常数。
特别唯一 trace-zero 模型 $E_0:y^2+y=x^3$ 的原读数为
$$
\boxed{\Phi_y(u_\chi)=\frac m{9-\chi(9)}
\left[\prod_{z/\pm}
(x(P_z)^4+x(P_z))^{-n_{[Nz]}}\right],}
\tag{1070.38}
$$
只在 $9-\chi(9)\ne0$ 时使用。
该多项式的零点为非零三挠点的 $x$ 坐标；
原非零 $p$-torsion 不碰零，没有遗漏需要剔除的因子。

### 9.3 特征3的实际二除法多项式

在 $\ell=3$ 取 $c=2$。
R1068 的全部模型都已写成 $y^2=f_E(x)$，且 $\psi_2=2y$。
成对相乘给
$$
\psi_2(P)\psi_2(-P)=-4f_E(x(P)).
$$
共同常数 $-4$ 由原 augmentation-zero 指数严格消去。
故
$$
\boxed{\Phi_y(u_\chi)=\frac m{2(4-\chi(4))}
\left[\prod_{z/\pm}f_E(x(P_z))^{-n_{[Nz]}}\right],}
\tag{1070.39}
$$
只在 $4-\chi(4)\ne0$ 时成立。
两种 trace-zero 模型的 $f_E$ 分别是 $x^3+x$ 和 $x^3-x$；
其余模型仍保各自完整 cubic。
这些二挠零点同样不遇原非零 $p$-torsion。
这里的因子二来自全部向量乘积，不能沿用奇数平滑的尺度而删去。

上述式保 R1068 全部 stable necklaces、几何同构商、
同一 Weil pairing 和 cyclotomic embedding。
trace-zero 输入因而成为原 $p$-torsion 上
$x^4+x$ 或 $x^3\pm x$ 的实际乘积；
尚未证明这些乘积的共同像排除。

还有一个必须保留的边界：
若同一 $\chi$ 在2与3都可见，
原可见性条件给 $\chi(2)=2,\chi(3)=3$，
于是两个低次平滑的 $\kappa$ 都恰好为零。
此时必须回到 §2 的可逆 $c$，
不能声称 (1070.38) 与 (1070.39) 同时读取这个角色。

本节消费原 §§1–8 的完整函数和相位，
任意 $c$ 的 ellipticity 及低次除法多项式在本节自证。
global_route 推导，root 与 o2_high_coefficient 独立核准
偶数平滑的因子二、全部 $b_i$、退化时的实际 $p$ 次幂
及可见性边界。无数学程序执行。


## 10. 全部实际角色的可逆平滑与精确辅助可见性

本节回到 R1062 的完整 $V=C_\Sigma[p]$，
不限于 forced 子空间。先用原 Stickelberger 格的
准确 eigenvalue 排除两个边界角色。

### 10.1 两个角色在实际 cusp 模块中缺席

若 $p\equiv3\pmod4$，置 $m=(p-1)/2$，
$\chi_*=\omega^{m+1}$，$\psi=\chi_*^{-1}=\omega^{m-1}$。
取 $2j=m-1<m$，R1062 的原 Jacobi 展开仍给
$J(\psi,\eta)\equiv0\pmod p$；
反向和的唯一 $p-1$ 次系数为
$-\binom m{m-1}=-m$，是单位。
原 Gauss 乘积恒等式遂给 $v_pJ(\psi,\eta)=1$。

另一方面 $\psi^2=\omega^{-2}$，所以
$$
\sum_{a=1}^{p-1}a^2\psi(a)^2\equiv-1\pmod p.
$$
在原
$$
B_{2,\psi^2}
=\frac1p\sum a^2\psi(a)^2-\sum a\psi(a)^2
 +\frac p6\sum\psi(a)^2
$$
中，后两项整，第一项的 valuation 准确为 $-1$。
故 $S_\psi=-J(\psi,\eta)B_{2,\psi^2}/4$ 是 $p$-unit，
准确得到
$$
\boxed{
(C_\Sigma\otimes\mathbf Z_p)_{\chi_*}=0,\qquad V_{\chi_*}=0.
}
\tag{1070.40}
$$
这里 $\psi,\eta,\psi\eta,\psi^2$ 全非平凡，
$p>37$ 不出现 Jacobi 退化。
不能把 forced 范围之外首和的极点略掉：
正是这个极点抵消了 Jacobi 和的一次 $p$ 因子。

若 $p\equiv1\pmod4$，quadratic $\eta=\omega^m$ 是偶角色。
直接按原范数纤维求和：
$a\ne0$ 时 $\sum_b\eta(a^2-\delta b^2)=1$，
$a=0$ 时该和为 $-(p-1)$。
又 $\sum_{a=1}^{p-1}B_2(a/p)=(1-p)/(6p)$，所以
$$
\boxed{
S_\eta=\frac p4
 \left(\frac{1-p}{6p}-\frac{p-1}{6}\right)
=\frac{1-p^2}{24}\in\mathbf Z_p^\times,\qquad V_\eta=0.
}
\tag{1070.41}
$$
trivial 分量本来为零；当 $p\equiv3\pmod4$ 时
quadratic 不是偶角色。
因此整个实际 $V$ 的非零分量都满足 $\chi^2\ne1$。

### 10.2 原除法多项式公式扩到完整实际 $V$

取一个 $c\bmod p$ 为 primitive 的正整数，
仍可同时要求 $(c,6p\ell)=1$。
对偶角色 $\chi=\omega^r$，
$$
\kappa_\chi(c)=0
\quad\Longleftrightarrow\quad
2(r-1)\equiv0\pmod{p-1}.
$$
$p\equiv1\pmod4$ 时两解 $r=1,1+m$ 都为奇数；
$p\equiv3\pmod4$ 时唯一偶解恰为已排除的 $\chi_*$。
所以这同一个 $c$ 对整个实际 $V$ 的每个非零分量均可逆。

还须支付原基，而不只证明某个 smoothing scalar 非零。
对任意 $V_\chi\ne0$，照 (1070.3) 选原 augmentation-zero 整数指数。
R1062 的 $\theta$ 在 $\mathbf Z_p[G]$ 中整，
且 $S_{\chi^{-1}}\in p\mathbf Z_p$，
故原 raw product 的 divisor 确为 $p$ 倍。
Carlucci 实际 unit 格张量 $\mathbf Z_p$ 后，
在每个非 trivial 角色由这个指数生成：
$p\nmid d$ 使原 $R_d$ 变成 $\mathbf Z_p[G]$，
trivial 方向以外的 $\theta$ eigenvalue 均非零，
所以指数到实际 unit 格的映射在各非 trivial 方向为同构。
$n\bmod p=e_\chi\ne0$ 因而保证该 unit 不在 $pU$；
所得 $u_\chi$ 准确生成一维 $V_\chi$。
即使 $v_pS_{\chi^{-1}}>1$，这个单位格结论仍成立。

实际 $\chi^2\ne1$，故原平方角色 leading 计算全部适用，
特别全部 cusp leading 类总和仍为零。
因此 (1070.31) 及 §§3–8 的相位、整数提升、实下降和同一点条件，
准确扩为
$$
\boxed{
\Phi_y(u_\chi)=\frac{m}{c^2-\chi(c^2)}
 \left[\prod_{z/\pm}\psi_c(P_z)^{-n_{[Nz]}}\right]
\quad\text{对所有实际 }V_\chi\ne0.
}
\tag{1070.42}
$$
先前 forced 限定由 (1070.40)–(1070.41) 的真实缺席解除；
没有在一个实际非零分量上除掉零 $\kappa$。

这不把 R1069 其它角色尚存的 class-group 自由度
自动称为唯一全局候选。
唯一性仍只在其 good 子模块使用；本节扩展的是原函数评价。

### 10.3 整个原家族的精确可见素判据

令 $\ell\ne p$ 为辅助素，$d_\ell=\operatorname{ord}_p(\ell)$。
由 R1064 的真实角色，
$\chi$ 可见恰当且仅当 $\chi(\ell)=\ell$。
若 $d_\ell$ 为偶数，此式对偶角色无解。

若 $p\equiv3\pmod4$ 且 $d_\ell=m$，
full even characters 中唯一解为 $\chi_*$，
而 (1070.40) 已证明它不属于实际 $V$。
故 $H^1(\mathbf F_\ell,H_V)=0$，且 $H_V(\mathbf F_\ell)=0$。
只要原 $X(\mathbf F_\ell)$ 非空，
每个允许的原 cuspidal twist 在该素都自动有点，
每个原点的纤维恰有一个 $\mathbf F_\ell$ 点；
若基础点集为空，该基础障碍仍保留。

反过来，若 $d_\ell=1$，forced $\chi_1$ 可见。
若 $d_\ell>1$ 为奇数，且排除上述 $d_\ell=m$ 情形，
取 $j=(d_\ell-1)/2$。
当 $p\equiv1\pmod4$ 时，
$d_\ell\le(p-1)/4$；
当 $p\equiv3\pmod4$ 且 $d_\ell<m$ 时，
$d_\ell\le m/3$。
两种情况下 $1\le j\le\lfloor p/4\rfloor-1$，
所以真实 forced $V_{\chi_j}$ 已无条件一维，
且 $\ell^{2j+1}=1$。
于是完整判据为
$$
\boxed{
H^1(\mathbf F_\ell,H_V)\ne0
\iff
d_\ell\text{ 为奇数且 }
\neg\bigl(p\equiv3\pmod4,\ d_\ell=(p-1)/2\bigr).
}
\tag{1070.43}
$$
特别若 $p=2q+1$、$q$ 为奇素数，整个原 cuspidal 家族
**只在 $\ell\equiv1\pmod p$ 时可见**。
这只是精确删除无效辅助素，未声称其余素已排除候选，
也未把基础曲线点集为空的障碍丢掉。

本节消费 R1062 的原完整 Stickelberger/unit 格和已证明 forced 分量，
以及 R1064 的原 finite-field 角色。
global_route 与 root 分别付款边界角色及精确判据；
o2_high_coefficient 独核 exceptional 角色的 Jacobi/Bernoulli valuations。
全部为纸面证明，无数学程序执行。


[R1071](R1071-original-p-local-cuspidal-label-polynomials.md)
从本篇原 $\psi_c$ 函数在全部 supersingular reference 的有限 Taylor 数据，
给每个实际 $p$-local disk 的全角色多项式。
原 $\beta_0,\lambda$、Weil root 和 circular-unit 尺度均保留，
高 log 分母全部排除；仍须比较同一全局候选与本篇有效辅助点像。
