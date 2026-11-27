# R1139：原紧致目标的完整 unsmoothing 与裸杯积

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 在 R1136 (F33) 的明确混合 Bernoulli 条件下，
原 smoothing 算子在整个紧致 étale $H^2$ 的指定角色部分生成单位理想。
这个结论下降到实际 Picard/Brauer 商及函数域中的紧致像，
因而消除 R1136 (F53) 留下的 target common-kernel 歧义。
结合 R1138 的整模 $p$ 比较，原裸杯积准确等于原紧致 Manin 来源的值，
保留系数 $m^2/4$。

本篇不将这个紧致来源的值设为零，不将整 $K_2[p]$ 与 $K_2/p$ 混同，
也不把结论扩到未满足混合条件的四阶指定邻对。

## 1. 原输入、明确条件与结论

保持 [R1136](R1136-original-forced-compact-Manin-sources.md) 的原规范：
$$
p>37,\quad K=\mathbb Q(\zeta_p),\quad
\Delta=\operatorname{Gal}(K/\mathbb Q),\quad
X=X_{\rm ns}^+(p),\quad m=(p-1)/2,
$$
$$
\chi=\omega^{p-1-2j},\qquad
\psi=\omega^{p-1-2k},\qquad
1\le j,k\le\lfloor p/4\rfloor-1,
$$
$$
\theta=\chi\psi=\omega^a,\qquad
a=p-1-2(j+k),\qquad r=2j+2k+2.
\tag{1139.1}
$$
$\omega$ 是实际圆分角色。$a$ 为偶数，且
$4\le a\le p-5$；当 $p\equiv3\bmod4$ 时其下界为 $6$。
特别，$a\not\equiv0,1,2\bmod p-1$，而
$r\equiv2-a\bmod p-1$。

本篇始终假定
$$
\boxed{\quad
r=2j+2k+2<m,\qquad
p\nmid B_{\,4j+4k+4}B_{\,p-3-4j-4k}.
\quad}
\tag{1139.2}
$$
这正是 R1136 (F33)，不是只要求两个单独角色 good。
[R1132](R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md)
在这些条件下消去原 $X$ 的整个紧致 $I_r$ 块。
后文只消费这一**整块**结论，不以 R1131 的奇 $K$-rational 扭点消失代替它。

令 $T_n$ 是原 $X$ 上固定 $K$ 的通常 Hecke correspondence。
对每个素数 $n>3$、$n\ne p$，在 $\theta$ 部分记
$$
V_n=n^4-n^{a+2}T_n+n^{2a+1}.
\tag{1139.3}
$$
R1136 (F30) 已付 physical convention
$\widetilde T_n=\sigma_nT_n$，
故 (1139.3) 确是 $n^4-n^2\widetilde T_n+n\widetilde{[n]}$ 的实际角色读数。

用 $\Psi$ 表示 R1136 (F50)–(F52) 的唯一 source unsmoothing：
$$
L=H_1(X,\mathbb F_p)\oplus
 H_1(X_1(p),\mathbb F_p)_{\theta^2},\qquad
c_{\chi,\psi}=
 \bigl(c_{\chi,\psi}^{(2)},C_{\chi,\psi}^{(1)}\bigr)\in L.
\tag{1139.4}
$$
第二个 summand 用 R1136 (F44) 的真实 away-from-$p$ quotient action，
不搬用 $U_p$。两个循环是原独立点对及全部依赖点对的完整来源。

**定理。** 条件 (1139.2) 下，
$$
\boxed{\quad
\frac4{m^2}\{F_\chi,F_\psi\}
       =\Psi(c_{\chi,\psi})
\quad\text{在 }K_2(K(X))/p\text{ 中。}\quad}
\tag{1139.5}
$$
$F_\chi,F_\psi$ 保持原全尖点 leading 规范。
式 (1139.5) 是同一原裸杯积的准确等式；其右侧尚未证明为零。

证明的较强中间结论是：若
$$
\mathcal H_\theta=
 H^2_{\rm et}(X_K,\mu_p^{\otimes2})_\theta,
\tag{1139.6}
$$
则在实际 Hecke 算子作用下，全部 $V_n$ 在
$\mathcal H_\theta$ 及其每个 Hecke-stable 商上生成单位理想。
无需假设这些算术 cohomology 群有限维或半单。

## 2. 原 p 倍除子给完整曲线上的实际 Kummer 类

### 2.1 保持原函数与所有尖点

[R1064 §§1–2](R1064-original-cuspidal-cover-descent-and-auxiliary-character-visibility.md)
的原定义为
$$
f_u=u^m/A(u),\qquad
A(u)=\prod_{c\in\Sigma}a_c(u),\qquad
\operatorname{div}u\in p\operatorname{Div}^0_\Sigma(X_K).
$$
因此原规范类及其所有 $\mathbb F_p$ 线性组合均有实际函数代表 $f$ 满足
$$
\operatorname{div}f=pD.
\tag{1139.7}
$$
线性组合先用真实整数指数作乘积，再约模 $p$。
若定义中有 prime-to-$p$ 标量，取其模 $p$ 的整数逆作幂即可；
仍保 (1139.7)。这说明 R1138 的 $F_\chi,F_\psi$ 有这样的原代表，
而不需要更换其常数规范。

在任一闭点的局部环写 $f=t^{pd}u$，$u$ 为单位。
对 $\alpha^p=f$ 作 $\beta=\alpha/t^d$ 后变成
$\beta^p=u$，在特征零中为有限 étale 的 $\mu_p$-torsor。
这些局部规范化来自同一函数域扩张，故在整个 $X_K$ 上拼合。
得到
$$
\kappa(F_\chi),\ \kappa(F_\psi)\in H^1_{\rm et}(X_K,\mu_p).
\tag{1139.8}
$$

泛点限制
$H^1(X_K,\mu_p)\to K(X)^\times/K(X)^{\times p}$
单射：泛点平凡的有限 étale torsor 的截面在正常曲线上延拓。
所以 (1139.8) 的实际 $\Delta$ 角色分别就是 $\chi,\psi$，
不是只在几何 Jacobian 上有相同角色。
于是
$$
\widehat\beta=
 \frac4{m^2}\,
 \kappa(F_\chi)\cup\kappa(F_\psi)
 \in\mathcal H_\theta.
\tag{1139.9}
$$
其泛点像是 (1139.5) 左侧的 norm-residue 类。

### 2.2 直接核全部 tame residues

也可在每个闭点直接核模 $p$ tame。
若 $v(f_\chi)=pu$、$v(f_\psi)=pv$，采用
$\partial\{f,g\}=(-1)^{v(f)v(g)}f^{v(g)}/g^{v(f)}$ 的 convention，则
$$
\partial\{f_\chi,f_\psi\}
 =
 \left[
 \left((-1)^{puv}\frac{f_\chi^v}{f_\psi^u}\right)^p
 \right]_{\rm residue}.
\tag{1139.10}
$$
括号内的比值 valuation 为零，故这确是 residue field 中的 $p$ 次幂。
在非尖点两函数本来都是单位；在每个尖点 (1139.10) 保留了真实
整数阶、符号和全部 residue field。
因此原 cup 在模 $p$ 意义下无遗漏的尖点 residue。

本文用 (1139.9) 的实际紧致 lift，比只核几何 tame 更强。
但不声称 (1139.10) 的整 tame 已等于 $1$；
本篇处理的是 $K_2/p$，不是此前的未分歧整 $K_2[p]$。

## 3. Hochschild–Serre 的实际两层，以及准确 Tate 角色

令 $\overline X=X_{\overline{\mathbb Q}}$。
原 $X$ 在 $\mathbb Q$ 定义，故 Hochschild–Serre 序列
$$
E_2^{s,t}=
 H^s\!\left(K,H^t_{\rm et}
       (\overline X,\mu_p^{\otimes2})\right)
 \ \Longrightarrow\
 H^{s+t}_{\rm et}(X_K,\mu_p^{\otimes2})
\tag{1139.11}
$$
带原 $\Delta$ 作用，且对 proper correspondences 自然。
这里用连续 Galois cohomology；不是在有限 $\Delta$ 上重写算术 $H^1$。
见 [M1, Theorem 14.9、Remark 14.10]。

$K$ totally imaginary，且
$$
\operatorname{cd}_p(K)=2.
\tag{1139.12}
$$
所需的高阶消失可直接由 [M2, I Theorem 4.10(c)]，
在包含 $p$ 与无穷素的有限 $S$ 上取极限得到；
实素的高阶项在此为空。等号的下界来自数域非零的
$p$-primary Brauer 类；本证明只需上界。

几何完整光滑曲线的 trace 给
$$
H^2_{\rm et}(\overline X,\mu_p)\simeq\mathbb F_p,
\qquad
H^2_{\rm et}(\overline X,\mu_p^{\otimes2})\simeq\mu_p.
\tag{1139.13}
$$
后一同构保 $G_{\mathbb Q}$ 作用，故其 $\Delta$ 角色是
$\omega$，**不是** $\omega^2$。
这是几何 degree trace 的一个 Tate twist，
见 [M1, Proposition 14.2、Example 14.8]。
由于 $\theta$ 偶而 $\omega$ 奇，(1139.11) 的
$E_\infty^{0,2}$ 在 $\theta$ 部分为零。

因此 $\mathcal H_\theta$ 有 Hecke-stable 两层过滤
$$
0\subset\mathcal A_\theta\subset\mathcal H_\theta,
\tag{1139.14}
$$
其中
$$
\mathcal A_\theta
 \text{ 是 }H^2(K,\mu_p^{\otimes2})_\theta\text{ 的商},
$$
$$
\mathcal H_\theta/\mathcal A_\theta
 \text{ 是 }
 H^1\!\left(K,H^1_{\rm et}
       (\overline X,\mu_p^{\otimes2})\right)_\theta
 \text{ 的子商}.
\tag{1139.15}
$$
这里没有假设 spectral sequence 分裂、degenerate，
或存在 Hecke-equivariant 的尖点 section。
子商的表述保留全部可能的 differential。

### 3.1 通常 Hecke 在两层上的真实作用

在 base 项 $H^2(K,\mu_p^{\otimes2})$ 上，
$$
T_n=n+1.
\tag{1139.16}
$$
理由是两 projections 对常数系数作 pullback–trace，
其 trace degree 为 $n+1$。更确切地，这是 (1139.11)
中几何 $H^0(\mu_p^{\otimes2})$ 的作用。
它不因 $p\mid n+1$ 失效，也没有反除该 degree。
普通 $T_n$ 固定 $K$；physical $\sigma_n$ 已在 (1139.3) 的
$n^{a+2}$ 中结算，不能再添一次。

在 $H^1_{\rm et}(\overline X,\mu_p^{\otimes2})$ 上，
原紧致 Hecke 格的全部模 $p$ 关系成立。
选择复嵌入，由同一原 correspondence 的 Betti–étale comparison，
它在 cohomology 上是 compact homology 作用的对偶；
交换的 Hecke 多项式关系在对偶上仍成立。
有限系数 comparison 见 [M1, Theorem 21.1]。
等价地可在原 Jacobian 的整 Tate 格及其对偶上作同一论证。
此处没有另用有理 Chen 同源去替换整格。

这些 Hecke endomorphisms 与 $G_K$ 交换，
所以每条关系继续作用为零于
$H^1(K,H^1_{\rm et}(\overline X,\mu_p^{\otimes2}))$
及其所有子商。
因而 (1139.2) 给出的 source 单位理想确实作用为单位于
(1139.15) 的**上层**。尚不能直接对整个 $\mathcal H_\theta$
这样断言；下一节专门补 base 层和两层之间的扩张。

## 4. 显式两层单位算子，保全部算术常数

让交换多项式代数
$$
\mathscr P=\mathbb F_p[t_\ell:\ell\ne p]
$$
按原 $T_\ell$ 作用于本文各群。
在 source Hecke order 中选择关系，再取 $\mathscr P$ 中的
多项式代表。这样不会把 source 的商关系未经证明强加给 target。

由 (1139.2)、R1136 (F33)、(F44)，可选有限多个
$n_i>3$、$n_i\ne p$ 与多项式 $A_i$，使
$$
E=\sum_i A_i(T)V_{n_i}(T)=1
\quad\text{在原 compact }H_1(X,\mathbb F_p)
 \text{ 及 }L\text{ 上}.
\tag{1139.17}
$$
R1136 §13.1 已证明删去 $2,3$ 不产生新的公共极大理想。
由 §3.1，$E=1$ 在 (1139.15) 上层；
在下层它暂时只是把各 $T_\ell$ 代为 $\ell+1$ 得到的某个 scalar。

在 base 层，(1139.3) 的 scalar 准确为
$$
\begin{aligned}
v_n&=n^4-n^{a+2}(n+1)+n^{2a+1}\\
   &=n(n^a-n)(n^a-n^2).
\end{aligned}
\tag{1139.18}
$$
因为 $a\not\equiv1,2\bmod p-1$，
取一个 primitive residue $g\in\mathbb F_p^\times$，
则 $g^a\ne g,g^2$。
Dirichlet 定理给一个素数 $n_0>3$、$n_0\ne p$、$n_0\equiv g\bmod p$。
因此 $v=v_{n_0}\in\mathbb F_p^\times$。
这里仅用存在性，不附加小辅助素或有效筛选范围。

现在取实际 target 算子
$$
\boxed{\quad
F=E+(1-E)v^{-1}V_{n_0}.
\quad}
\tag{1139.19}
$$
$F$ 属于全部 $V_n$ 生成的 $\mathscr P$-理想。
在上层 $E=1$，所以 $F=1$。
在下层 $V_{n_0}=v$，故无论 $E$ 是哪个 scalar，
仍有 $F=E+(1-E)=1$。

因此 $F-1$ 把整个 $\mathcal H_\theta$ 送入 $\mathcal A_\theta$，
并杀掉 $\mathcal A_\theta$，从而
$$
(F-1)^2=0,\qquad
\boxed{\quad(2-F)F=1\quad\text{在 }\mathcal H_\theta\text{ 上}.}
\tag{1139.20}
$$
右式是完整算子恒等式，不只说明 associated graded 没有公共核。
特别，$1$ 在全部 $V_n$ 的实际算子理想中。

这个证明也说明为何不能直接把 (1139.17) 的 source 关系
用在整个算术 target：base 层一般有非零的
$H^2(K,\mu_p^{\otimes2})$。式 (1139.19) 在保留该层的同时补齐它。
没有以“常数规范”或某个未知 splitting 删除这项。

## 5. Picard 核、Brauer 商与函数域中的紧致像

因为 $\mu_p\subset K$，Kummer exact sequence 给实际
$\Delta$-等变正合列
$$
0\longrightarrow
 (\operatorname{Pic}(X_K)/p)\otimes_{\mathbb F_p}\mu_p
 \longrightarrow H^2_{\rm et}(X_K,\mu_p^{\otimes2})
 \longrightarrow
 \operatorname{Br}(X_K)[p]\otimes_{\mathbb F_p}\mu_p
 \longrightarrow0.
\tag{1139.21}
$$
这里 $\operatorname{Br}$ 为 cohomological Brauer group。
在 $K$ 上 $\mu_p$ 是常系数 rank-one 空间，但其
$\Delta$ 作用仍保留；(1139.21) 没有把第二个 Tate twist 忘掉。
该列是通常 Kummer 列张量 $\mu_p$，见 [M1, Example 7.9(a)]。

proper finite curve correspondences 的 pullback、trace/Gysin
保持 (1139.21)，且与泛点的 restriction/corestriction 相容。
Hecke 的中间曲线取其光滑紧致规范化，
尖点与椭圆点的 ramification multiplicities 全部保留。
这里不要求 degree 是 $p$ 单位。

故 Picard 项是 Hecke-stable 核。
(1139.20) 因而下降到整个 Brauer 商，
以及泛点限制的像
$$
\mathcal U_\theta=
 \operatorname{im}\left(
 H^2_{\rm et}(X_K,\mu_p^{\otimes2})_\theta
 \longrightarrow
 H^2(K(X),\mu_p^{\otimes2})_\theta
 \right).
\tag{1139.22}
$$
使用这个像的定义即可，不需要另选一个 Picard 商的 splitting。
一个 field class 只有某个 lift 被 $V_n$ 杀，
和它在商中被 $V_n$ 杀，是不同陈述；
(1139.20) 在商上是恒等式，处理的是后一种真实需求。

Merkurjev–Suslin [MS, Theorem 11.5] 给函数域上的实际同构
$$
K_2(K(X))/p
 \xrightarrow{\ \sim\ }
H^2(K(X),\mu_p^{\otimes2}),
\tag{1139.23}
$$
将 $\{f,g\}$ 送到两 Kummer 类之 cup。
该 norm-residue map 保 pullback 与有限 corestriction，
所以保原 Hecke correspondence。
本式是 field 的 Milnor/Quillen $K_2$ 模 $p$ 同构。

通过 (1139.23)，也把 $\mathcal U_\theta$ 记作
$K_2(K(X))/p$ 中的实际紧致像。由 (1139.20) 得到
$$
\boxed{\quad
\mathcal U_\theta\cap
 \bigcap_{\substack{n>3\ {\rm prime}\\n\ne p}}\ker V_n
 =0.
\quad}
\tag{1139.24}
$$
更强地，整个 $V_n$-理想在 $\mathcal U_\theta$ 上含恒等算子。
因此本结论没有遗漏 Picard quotient 导致的 lift 歧义。

## 6. 同一原 cup 与同一原 compact cycle 的准确等式

令
$$
\beta=\frac4{m^2}\{F_\chi,F_\psi\}.
\tag{1139.25}
$$
由 §2，$\beta\in\mathcal U_\theta$，其实际 lift 是 (1139.9)。
R1138 (1138.17)–(1138.18) 给
$$
\Psi_n(c_{\chi,\psi})=V_n\beta
\quad(n>3,\ n\ne p).
\tag{1139.26}
$$
左侧同时包含独立与依赖点对，右侧包含完整
$n^4-n^{a+2}T_n+n^{2a+1}$，没有删 cyclic norm 的 crossed terms。

取 (1139.17) 的同一 $A_i,n_i$。
R1136 (F52) 以及每个 smoothed map 的真实 Hecke 相容性给
$$
\begin{aligned}
\Psi(c_{\chi,\psi})
 &=\sum_i\Psi_{n_i}(A_i c_{\chi,\psi})\\
 &=\sum_i A_i\,\Psi_{n_i}(c_{\chi,\psi})\\
 &=\sum_i A_i V_{n_i}\beta
 =E\beta.
\end{aligned}
\tag{1139.27}
$$
第二行的 $A_i$ 是同一多项式在实际 target 上的作用。
它不宣称 target 中所有 source relations 都成立。

式 (1139.27) 还有一个必要作用：
$$
\Psi(c_{\chi,\psi})\in\mathcal U_\theta,
\tag{1139.28}
$$
因为其 lift 可直接取 $E\widehat\beta$。
所以不必先对任意一个 $\mathfrak z_{n,X}$ 或 $\Phi_n$
的任意代表声称其全部尖点 tame 已为零。
对本次指定 cycle，(1139.26)–(1139.27) 已给准确的紧致 lift。

设 $\delta=\beta-\Psi(c_{\chi,\psi})$。
由 (1139.28)，$\delta\in\mathcal U_\theta$。
R1136 (F51)–(F52) 给 $\Psi V_n=\Psi_n$；
结合 Hecke equivariance 与 (1139.26)，有
$$
V_n\delta
 =V_n\beta-\Psi(V_n c_{\chi,\psi})
 =V_n\beta-\Psi_n(c_{\chi,\psi})=0
\tag{1139.29}
$$
对全部辅助素数成立。
现在才能使用 (1139.24)，得到 $\delta=0$。
这证明 (1139.5)。

整个推导中的 $F_\chi,F_\psi$、$c^{(2)}_{\chi,\psi}$、
$C^{(1)}_{\chi,\psi}$、$\sigma_n$ 与所有 normalization
均是 R1064/R1070/R1136/R1138 的原对象。
没有通过换一个有利的 cup、丢掉 rank-one orbit，
或对常数项另取未知 scalar 来完成等式。

## 7. 本篇关闭的门与仍开放的指定值

R1136 (F53) 的 target common-kernel 门，
现已在 **(1139.2)** 的准确范围内关闭。
这来自两层算子恒等式 (1139.20)，
不是把 source 单位理想未经证明移到整个 $K_2/p$。

下列问题仍分别保留：

- 尚未证明 $\Psi(c_{\chi,\psi})=0$；
  一个真实紧致循环的 motivic 读数可以非零。
  因而 (1139.5) 本身不是原不同角色杯积的消失定理。
- 未满足 (1139.2) 时，不能使用这里的 source 或 target 单位理想。
  R1136 (F34) 的四阶指定非重复邻对不在该低混合范围。
- 本篇不将 $\mathcal U_\theta$ 换成整个 field $K_2/p$，
  不援用整 $K_2[p]$ 的 Suslin 残余消失来代替 (1139.23)。
- 真正的高阶覆盖仍须指定低 cochains、
  完整跨轨道关系和原 cusp inertia moments；
  没有由本等式直接得到有理点排除。

## 8. 原始来源与复核

- [M1] J. S. Milne，*Lectures on Étale Cohomology*，version 2.21 (2013)，
  [作者全文](https://www.jmilne.org/math/CourseNotes/LEC.pdf)。
  实读 Example 7.9(a)（Kummer sequence）、
  Proposition 14.2 / Example 14.8（完整曲线的 trace 与 Tate twist）、
  Theorem 14.9 / Remark 14.10（连续 Hochschild–Serre）、
  Theorem 21.1（有限系数 comparison）。
  对应印刷页为 53、90/93、96–97、130。
  本文的两层算子 (1139.19)–(1139.20) 在这些实际过滤上直接证明。
- [M2] J. S. Milne，*Arithmetic Duality Theorems*，second edition (2006)，
  [作者全文](https://www.jmilne.org/math/Books/ADTnot.pdf)，
  I Theorem 4.10(c)，印刷第 57 页（PDF 第 65 页）。
  本文取 totally imaginary $K$，再沿有限 $S$ 取极限；
  没有使用可能需要其他假设的 strict cohomological dimension 断言。
- [MS] A. S. Merkur'ev、A. A. Suslin，
  *Cohomology of Severi–Brauer varieties and the norm residue homomorphism*，
  Math. USSR-Izvestiya 21 (1983), 307–340，
  [DOI](https://doi.org/10.1070/IM1983v021n02ABEH001793)；
  [原文入口](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=1657&wshow=paper)。
  实读 Theorem (11.5)，印刷第 328 页（34 页 PDF 的第 22 页）：
  $n$ 与 field characteristic 互素时的 degree-two norm-residue 同构。
- R1064 (1064.2)–(1064.8)：原函数的 $p$ 倍 divisor、真实全尖点规范，
  以及完整 proper curve 上的 étale Kummer lift。
- R1132 (1132.2)–(1132.4)：当前明确两 Bernoulli 门下的原正商整块消失。
- R1136 §§11–13：实际 full-level/Cartan Hecke、
  rank-one exact twist、away-from-$p$ 整 Hecke quotient、
  完整 source unsmoothing 与其 common-kernel 范围。
- R1138：整模 $p$ 的原 bare-cup 比较，全部 cyclic correlation 已逐项计算。

global_route 与 root 独立得到两层 target 论证；
o2_high_coefficient 已纸核准确 Tate 角色、base degree、
(1139.19)–(1139.20)、Picard 稳定核及 (1139.27) 的紧致 lift。
本篇没有数学程序执行。

root 已逐节回读 exact candidate 6fcfcbe6aeeaa1ce01fc093ed056c8892185a591，并另核实际 p 倍 divisor、全部 tame、两层 nilpotent 恒等式及泛点商；Milne 与 Merkurjev–Suslin 原文入口已复取。该结论仅在 (1139.2) 的原低混合范围内消费。
