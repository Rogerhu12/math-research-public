# R5：虚二次自扭曲、p 惰性及一个等价的统一性目标

日期：2026-11-12。状态：**已证明的结构归约**；不是一致性证明。自扭曲解释本身是经典事实。

采用 R1 的 $C,N,J,s$ 记号。设 $p$ 为奇素数，$E/\mathbb Q$，且 $\bar\rho_{E,p}(G_{\mathbb Q})\subseteq N$，令
$$\varepsilon:G_{\mathbb Q}\longrightarrow N/C\cong\{\pm1\}.$$

## 1. 二次域一定虚，而非任意二次域

取复共轭 $c$。由 Weil 配对，$\det\bar\rho(c)=-1$，且 $\bar\rho(c)^2=I$。$C\cong\mathbb F_{p^2}^\times$ 中平方为 $I$ 的元素只有 $\pm I$，二者行列式都为 $1$。因此 $\bar\rho(c)\notin C$，
$$\varepsilon(c)=-1.$$
所以 $\varepsilon$ 非平凡，核固定一个虚二次域 $K$。此结论不需要无 CM 假设。

## 2. 残余自扭曲与有理同源的严格区别

由矩阵计算，$J$ 与 $C$ 交换，且 $JsJ^{-1}=-s$。故
$$J\bar\rho(g)J^{-1}=\varepsilon(g)\bar\rho(g)\qquad(g\in G_{\mathbb Q}).$$
若 $E^\varepsilon$ 为相应二次扭曲，其表示为 $\varepsilon\bar\rho$，因此
$$E[p]\cong E^\varepsilon[p]\quad\text{作为 }\mathbb F_p[G_{\mathbb Q}]\text{-模}.$$

然而若 $E$ 无 CM，则 $E$ 与 $E^\varepsilon$ **不在 $\mathbb Q$ 上同源**。证明不需任何同源界。取扭曲同构 $\phi:E\to E^\varepsilon$，满足 $g(\phi)=\varepsilon(g)\phi$。因 $\operatorname{End}_{\overline{\mathbb Q}}(E)=\mathbb Z$，
$$\operatorname{Hom}_{\overline{\mathbb Q}}(E,E^\varepsilon)=\mathbb Z\phi.$$
若非零 $n\phi$ 在 $\mathbb Q$ 上定义，取 $\varepsilon(g)=-1$，则 $n\phi=g(n\phi)=-n\phi$，矛盾。

因此，把有限挠点的这个同构提升为有理同源，是一个实质性且尚未统一解决的步骤。不能从 Tate/Faltings 同源定理得到这一步：那些定理需要完整的 $\ell$-进信息，而这里仅有单层 $p$-挠点。

## 3. p 在 K 中惰性

本节假设 $p>13$。使用已发表输入：Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, Lemma 2.3(i)，说明 $\varepsilon$ 在 $p$ 不分歧。该输入来自椭圆曲线局部惯性分类，不是单凭 $N$ 的群论可得。

**命题。** $\varepsilon(\operatorname{Frob}_p)=-1$，即 $p$ 在 $K$ 中惰性。

**证明。** 因 $p\nmid|N|$，野惯性像平凡；温和惯性像为循环群。因 $\varepsilon$ 在 $p$ 不分歧，惯性像在 $C$ 中。行列式是圆分特征，而 $\chi_p(I_p)=\mathbb F_p^\times$，所以惯性像不能全是标量：标量的行列式都是平方。

取其非标量元素 $t\in C$，以及算术 Frobenius 的一个提升 $F$。温和惯性关系给出
$$\bar\rho(F)t\bar\rho(F)^{-1}=t^p.$$
若 $t$ 对应 $\lambda\in\mathbb F_{p^2}^\times\setminus\mathbb F_p^\times$，则 $t^p\ne t$。所以 $\bar\rho(F)$ 不能属于交换群 $C$，必属于外陪集，得到结论。

结合 R2：对每个负 $j$-赋值处 $q$，$\varepsilon$ 非分歧，且 $q\equiv1\pmod p$ 对应 $q$ 在 $K$ 中分裂，$q\equiv-1\pmod p$ 对应惰性。

## 4. 可用的 Frobenius 筛与真正缺口

对 $q\ne p$ 的好约化素数，外陪集迹为零给出
$$\varepsilon(q)=-1\Longrightarrow p\mid a_q(E).$$
再由 Hasse 界，如果 $q<p^2/4$，必有整数等式 $a_q(E)=0$。因此，如能对**实际异常子族**证明存在
$$q<p^2/4,\qquad \varepsilon(q)=-1,\qquad a_q(E)\ne0,$$
即可排除该异常像。

这里的三个条件必须同时满足。Chebotarev 仅给定性存在，或给依赖扩张判别式的有效界；它本身不给统一的小素数。R6 证明即便固定 $\varepsilon=\chi_{-4}$，仅凭无 CM 性也无法取得绝对有限的检测窗口。

## 5. 与主目标等价的二次自扭曲一致性

以下两条等价：

(U) 存在绝对 $C$，使所有无 CM $E/\mathbb Q$ 在 $p>C$ 模 $p$ 满射。

(T) 存在绝对 $B$，使所有无 CM $E/\mathbb Q$ 在 $p>B$，都不与任何非平凡二次扭曲具有同构的 $p$-挠点 Galois 模。

**证明。** 先证明满射表示 $\rho:G_{\mathbb Q}\to\mathrm{GL}_2(\mathbb F_p)$ 无非平凡二次自扭曲。若
$$A\rho(g)A^{-1}=\chi(g)\rho(g),$$
分别选 $g$ 使其像为 $I+e_{12}$ 与 $I+e_{21}$。取迹得 $2=2\chi(g)$，所以 $\chi(g)=1$。故 $A$ 与这两个矩阵都交换；直接比较矩阵元可知 $A$ 为标量。原等式随后迫使所有 $\chi(g)=1$。因此 (U) 推出 (T)。

反之，取 $p>\max\{B,37\}$。若 $\bar\rho_{E,p}$ 不满，R1 的已证分类使其像为 $N$。第 1、2 节构造非平凡 $\varepsilon$ 及 $E[p]\cong E^\varepsilon[p]$，与 (T) 矛盾。故 (T) 推出 (U)。证毕。

所以，将目标改写为“统一排除二次自扭曲”并未自动降低难度；它就是主要目标的一个等价形式。一般 Frey–Mazur 猜想会蕴含它，但引用该猜想不符合本课题的无条件完成标准。

## 6. 文献与适用边界

- Zywina，[作者原文](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)，Lemmas 2.3、2.5、2.6；§5 将自扭曲比较与依赖导子的 Sturm 界相接。
- Frengley, *Congruences of elliptic curves arising from non-surjective mod $N$ Galois representations*，[arXiv:2111.05813v2](https://arxiv.org/pdf/2111.05813)，Proposition 3.4 与 Lemma 4.1 讨论同样结构及素数幂推广；本文在需要的素数层已独立写出证明，不依赖该预印本的新结论。

注意：改到 $K$ 只让像落在非分裂 Cartan，未给出定义在 $K$ 上的循环 $p$-同源。非分裂 Cartan 在 $\mathbb F_p^2$ 上仍不可约，不能把系数域 $\mathbb F_{p^2}$ 与数域二次扩张混为一谈。
