# R998 — 新 beta27 的完整混合 Selmer 消失与最高投影的真实作用

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

**已证明。** 对 R991/R994 的三个原定向角色
$\beta_j=\psi_{27}\eta_j$，两条 weight-one CM 实现的中央
Bloch–Kato Selmer 空间

$$
H_f^1(K,\widehat\beta_j(1))
=H_f^1(K,\widehat\beta_j^{,c}(1))=0
\qquad(j=4,10,16)
$$

在每个系数素数都为零；任一固定兼容整模型的离散 Selmer 群在
每个素数有限，并在排除一个固定有限集合后为零。
这里控制的是完整 Bloch–Kato 条件，不是某个 strict 或 projected
局部核。该结论消去新实际 Rankin 两维表示中的混合槽；它没有
给出最高槽本身的非零，也没有由复解析秩一推出跨素数 AJ 非零。

## 1. 固定完整形式与正确的 CM 定向

保持 $K=\mathbf Q(\omega)$、原 $H/K$、三个 $\eta_j$ 及
$E_{27}:y^2+y=x^3$。R991 给完整 primitive theta newform

$$
h_j=\theta(\beta_j),\qquad \beta_j=\psi_{27}\eta_j,
\qquad k(h_j)=2,
\qquad N(h_j)=31212,
\tag{1}
$$

其 nebentypus 平凡。R994 已使用全部原有限角色及全部无限尾严格证明
$L(h_j,1)>0$；因此(1)的中央值非零是一个已付的固定复数结论，
没有依赖本篇所研究的素数 $p$。

在固定包含所有角色值与 $K$ 的系数域 $L$ 中，记
$W_j$ 为(1)的 **cohomological** 二维 $p$-adic realization。
它在好位的几何 Frobenius 多项式为
$X^2-a_{\ell,j}X+\ell$；原 CM 约定给

$$
W_j=\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}\widehat\beta_j,
\qquad
W_j|_{G_K}=\widehat\beta_j\oplus\widehat\beta_j^{,c}.
\tag{2}
$$

符号 $(1)$ 始终是同调意义的 Tate twist；(2)不是把 Tate module
与其对偶不加 twist 混用。由原 $\eta_j^c=\eta_j^{-1}$，

$$
\beta_j\beta_j^c=\mathrm N,
\qquad \widehat{\mathrm N}=\mathbf Q_p(-1).
\tag{3}
$$

因而 $W_j(1)$ 是通常 abelian-variety 中央 Selmer 的规范。

## 2. Kato 原定理同时包含中央与 CM 情形

这里实际使用 Kato, *p-adic Hodge theory and values of zeta
functions of modular forms*, Astérisque 295 (2004)，
**Theorem14.2(2)，印刷页235；CM 的完成见 §15.23**。
§14.1 定义的离散 Selmer 群使用每个有限位的完整 $H_f^1$ 条件。
该定理在偶权中央复值非零时，给每个系数位的离散 Selmer 有限，
并给几乎所有系数位的群为零；§15 并未排除 CM。

在该定理中取基域 $\mathbf Q$、平凡有限角色、权2及中央 twist1。
由 R994，假设 $L(h_j,1)\ne0$ 对三个实际形式全部成立。
故对于每个系数位 $\mathfrak p$ 和相应稳定格 $T_j$，

$$
\operatorname{Sel}_f(\mathbf Q,T_j)\text{ 有限},
\qquad H_f^1(\mathbf Q,W_j(1))=0.
\tag{4}
$$

第二式也可从第一式的 Tate module 直接读出：有限离散群的
$p$-adic Tate module 为零，而 rational Bloch–Kato 群是相应
整 Selmer 的有理化。这里未把某个非中央 twist 的结果移到中央。
对固定兼容格，定理还给

$$
\operatorname{Sel}_f(\mathbf Q,T_j)=0
\quad\text{在一个固定有限集合之外。}
\tag{5}
$$

扩张固定系数域保持(4)；对整格只须清除固定系数扩张及比较的
分母。因此(5)仍可在稍大的固定有限集合之外使用。

## 3. 原 CM 单线的全局和所有局部 Shapiro

对(2)应用 Shapiro 得

$$
H^1(\mathbf Q,W_j(1))
\simeq H^1(K,\widehat\beta_j(1)).
\tag{6}
$$

此同构保持完整 Bloch–Kato 条件，理由需逐类局部给出。

- 在 $v\nmid p\infty$，restriction 到 inertia 与局部 Shapiro
  的各 $w\mid v$ 分量交换，故保持定义 $H_f^1$ 的 unramified 核。
- 在 $v\mid p$，投影公式
  $B_{\rm cris}\otimes\operatorname{Ind}V
  \simeq\operatorname{Ind}(B_{\rm cris}\otimes V)$
  和局部 Shapiro 使通往 crystalline cohomology 的图交换；
  取核即保持完整 $H_f^1$，未改成某一个 ordinary 子空间。
- 无穷位使用同一零局部条件。取所有局部 restriction 的核，
  得到全局有限条件同构。

因此由(4)、(6)，

$$
\boxed{H_f^1(K,\widehat\beta_j(1))=0.}
\tag{7}
$$

共轭 $c$ 在完整全局及局部复形上互换两个 CM 方向，所以同样有

$$
\boxed{H_f^1(K,\widehat\beta_j^{,c}(1))=0.}
\tag{8}
$$

整格版本用同一 induced 格作 Shapiro；换到任一固定几何兼容格
只相差固定分母。由(4)/(5)，两条单线的离散完整 Selmer 均在
每个 $p$ 有限，且在固定有限集合之外为零。有限集合不依赖
所取 CM 层、某一循环的高度或一个待证的最高非零类。

## 4. 新 Rankin 的混合槽准确就是已经消失的那条线

令 $S$ 为 R991 的实际 $I_9/I_3$ 曲面，$M=t_2(S)$。
R995 的 $g=[\delta]^*$ 在 $h_1(E_{27})$ 上给严格 CM 幂等元
$e_E^+=(1+g/\delta)/2$，它选原 $\widehat\psi_{27}$ 方向。
在 $M\otimes e_E^+h_1(E_{27})$ 中保原 $\eta_j$ trace 并作
codimension2 的 twist $(2)$，完整两维表示是

$$
V_{j,\mathrm{new}}
=\left(\widehat\psi_{27}^{,3}\widehat\eta_j^{-1}\right)(2)
\ \oplus\
\left(\widehat{\bar\psi}_{27}^{,2}
       \widehat\psi_{27}\widehat\eta_j^{-1}\right)(2).
\tag{9}
$$

第一项准确为原 $\widehat\lambda_j(2)$，因为
$\psi_{27}^3=\psi_0^3$。第二项用(3)完整化简为

$$
\begin{aligned}
\left(\widehat{\bar\psi}_{27}^{,2}
       \widehat\psi_{27}\widehat\eta_j^{-1}\right)(2)
&=\left(\widehat{\bar\psi}_{27}
       \widehat\eta_j^{-1}\widehat{\mathrm N}\right)(2)\\
&=\widehat\beta_j^{,c}(1).
\end{aligned}
\tag{10}
$$

这正是 R991 unitary 分解中的 $(\nu_{27}\eta_j)^{-1}$ 的
代数中央实现。没有用旧 R826 的 $\eta_j^{-2}\psi_0$，
没有把 inverse/conjugate 在 CM 单线上省略。

由(8)及有限条件对直和的相容性，

$$
\boxed{
H_f^1(K,V_{j,\mathrm{new}})
\xrightarrow[\ \sim\ ]{\ P_{\rm high}\ }
H_f^1(K,\widehat\lambda_j(2)).}
\tag{11}
$$

这里的箭头是 R995 已构造的真实 Chow projector 在 étale 实现上的
作用，不是仅凭两个纯表示有相同 Hodge 型所选的抽象投影。

## 5. 对实际图循环的准确结论及对偶方向

对 R995 的完整2/17带权图族，先保完整内外 projector、全部分支与
原 finite-character trace，再取 $e_E^+$。若它的 AJ 类属于原
全 Bloch–Kato 条件，则(11)给严格等式

$$
\operatorname{AJ}_p(e_E^+Z_j)
=\operatorname{AJ}_p(P_{\rm high}e_E^+Z_j)
\quad\text{于 }H_f^1(K,V_{j,\mathrm{new}}).
\tag{12}
$$

有限条件是原循环论证中已经保留的条件；本篇不把一个任意
$H^1$ 类都宣布在 $H_f^1$ 中。对当前指定的条件类，混合部分
不能再补偿最高部分。因此只要同一完整新类的 AJ 非零，
最高类的 AJ 就非零，反向也成立。

但是(12)并不制造那个非零类。R994 只给复 Rankin 导数非零，
尚需针对实际图的 reciprocity 或真正的 $p$-adic 非零输入。
即使固定一个 $p$ 得非零，也不从本篇推出无限多个 $p$。

R995 的最高双线投影自伴，而单 CM 投影满足
$P_+^{\mathrm t}=P_-$；转置不共轭系数。
故把 AJ 当作 de Rham 微分上的泛函时，必须把 projector 转到
**对偶的**微分上。不能对 $P_+Z$ 直接配对同属 $P_+$ 的
$\Omega_S\otimes\omega_E$ 并称其为最高值。
式(11)/(12)是 Galois cohomology 中的等式，不犯这个对偶混淆；
局部显式公式须照 R997 的实际正反角色/微分方向继续。

## 文献与已有完整证明

- K. Kato (2004), Theorem14.2(2)、§14.1、§15.23：
  [Numdam 原文](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。
  已直接读取印刷页234–236与 §15.23；不能用非 CM 的大像假设
  排除其已在 §15 完成的 CM 部分。
- R991：原三个角色、实际新模曲面及完整 Rankin 分解。
- R994：三个固定 $L(\psi_{27}\eta_j,1)>0$ 的严格全尾证明和真实公开回执。
- R995：严格 Chow projector、真实 fiber-product 及所有 finite trace/AJ 自然性。

本篇是上述已证固定非零复值的理论消费，没有新增数学执行或素数扫描。
