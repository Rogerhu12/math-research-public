# R749 — 椭圆对数空间的真实点因子投影与有限角色抽取

日期：2026-11-15。**状态：已证明。**

本篇给 R742/R745 后续需要的准确线性操作。
一个数已经完整表示为同一椭圆曲线上代数点对数的代数线性组合后，
可以先唯一返回代数点张量空间，再对点因子施有限 Galois 幂等元。
该操作保持所有代数系数不动，并保持所有已知线性恒等式。

这个操作不来自给定的 $\mathbf C_p$ 上的 Galois 连续作用。
它也不等于同时共轭点和代数系数的自然 Galois trace。
后一差别有 R733 的实际非扭点给出的明确反例。

第5节给原两条 type5 来源的完整有限角色接口。
其中新角色的实际点表示列为明确假设(H)；
本篇不凭 R746 的平方公式或 R745 的代数 theta 来源自动补出(H)。
满足(H)时，结论不仅抽取平凡角色：
不同点特征中的所有非零负一值彼此代数线性独立。

## 1. 固定微分和完整点张量空间

固定
$$
K=\mathbf Q(\omega),\qquad
E=E_1:y^2=x^3+1,\qquad
\varpi=\frac{dx}{2y},\qquad
\iota_p:\overline{\mathbf Q}\hookrightarrow\mathbf C_p .
\tag{1}
$$
所有 CM 自同态都在 K 定义，且
$[a]^*\varpi=a\varpi$。
设
$$
V_E=E(\overline{\mathbf Q})\otimes_{\mathbf Z}\mathbf Q,\qquad
\mathscr V_E=V_E\otimes_{K,\iota_p}\overline{\mathbf Q}.
\tag{2}
$$
(2) 的第二个标量域按 $\iota_p$ 嵌入；下文省去该嵌入的记号。
有扭点的原群先张量 $\mathbf Q$，所以所有扭点在 $V_E$ 中为零。

以 R733 的紧群和小指数域构造定义每个代数点的全椭圆对数。
它与 CM 相容，故
$$
\mathscr L_p:\mathscr V_E\longrightarrow\mathbf C_p,\qquad
\mathscr L_p\left(\sum_i P_i\otimes a_i\right)
=\sum_i a_i\log_{E,\varpi}(P_i)
\tag{3}
$$
是良定义的 $\overline{\mathbf Q}$-线性映射。

**定理 1。** (3) 单射。

**证明。**
一个给定张量只涉及有限多个点。
在它们的 K 线性包中选基 $R_1,\ldots,R_d$，
把该张量唯一写为 $\sum_jR_j\otimes b_j$。
取包含这些点坐标和 K 的有限 p-adic 域，
再取一个正整数 n，使所有 $[n]R_j$ 同时落在实际 exponential 的单射域。

若 $\sum_j c_j\log R_j=0$，其中 $c_j\in K$，
清分母、用 CM 自同态及对数核恰为扭子群，得到
$\sum_j[c_j]R_j=0$ 于 $V_E$。
所以这些对数在 K 上独立。
Fuchs–Pham Theorem 2.2 对简单阿贝尔簇 E 以及
$n\log R_j$ 给它们在 $\overline{\mathbf Q}$ 上也独立；
其指数都是实际代数点 $[n]R_j$，而
$\operatorname{End}_{\overline{\mathbf Q}}(\operatorname{Lie}E)
=\overline{\mathbf Q}$。
由 $\mathscr L_p(\sum_jR_j\otimes b_j)=0$ 得全部 $b_j=0$。证毕。

记
$$
\mathscr U_{E,p}=\operatorname{im}\mathscr L_p .
\tag{4}
$$
因此每个已经属于 (4) 的数都有唯一的点张量原像。
表示所用点的数量、域和代数系数可以变化；
唯一性不依赖某一次表示的选择。
这里的系数条件是代数数，不能改成任意 $\mathbf C_p$ 数。

## 2. 有限 Galois 群只作用点因子

令 F/K 为有限 Galois 扩张，并置
$$
V_E(F)=E(F)\otimes_{\mathbf Z}\mathbf Q,\qquad
\mathscr V_E(F)=V_E(F)\otimes_K\overline{\mathbf Q},\qquad
G=\operatorname{Gal}(F/K).
$$
由于所有 CM 自同态在 K 定义，G 在 $V_E(F)$ 上的作用是 K 线性的。
定义其在张量空间上的作用为
$$
g_{\rm pt}(P\otimes a)=g(P)\otimes a .
\tag{5}
$$
第二因子 a 完全不动。

给任意群代数元
$$
A=\sum_{g\in G}c_g g\in\overline{\mathbf Q}[G],
$$
定义
$$
A_{\rm pt}(P\otimes a)
=\sum_g g(P)\otimes c_ga .
\tag{6}
$$
由定理1，准确的对数空间操作为
$$
\boxed{
A_p^{\log}
=\mathscr L_p\,A_{\rm pt}\,
  (\mathscr L_p|_{\mathscr V_E(F)})^{-1}.
}
\tag{7}
$$
它只在 $\mathscr L_p(\mathscr V_E(F))$ 上定义。
(7) 不要求任何 g 延拓成固定 $\mathbf C_p$ 的连续自同构。

**推论 2。**
若 $u_i\in\mathscr L_p(\mathscr V_E(F))$、$a_i\in\overline{\mathbf Q}$，
且 $\sum_i a_i u_i=0$，则
$$
\sum_i a_i A_p^{\log}(u_i)=0.
\tag{8}
$$
同样，等式两边都有完整点表示时，可以对整个等式施 (7)。

证明：先用定理1提升原关系为点张量关系，再施 $\overline{\mathbf Q}$-线性的(6)。
这不允许对仍未识别为 (4) 中元素的原中央量、条件积分或任意 p-adic 单位施(7)。

若 G 为阿贝尔群，字符 $\rho:G\to\overline{\mathbf Q}^{\times}$ 的幂等元为
$$
e_\rho^{\rm pt}
=\frac1{|G|}\sum_{g\in G}\rho(g)^{-1}g_{\rm pt}.
\tag{9}
$$
不同字符的像直和，且所有点张量唯一分解为这些像的和。
由 (3) 的单射性，对数空间也具有同一直接和分解。

特别，
$$
e_{\rm triv}^{\rm pt}(P\otimes a)
=\left(\frac1{|G|}\sum_{g\in G}g(P)\right)\otimes a .
\tag{10}
$$
括号内是实际 K 点的有理倍数。
故其像准确等于
$$
\mathscr V_E(K)=
(E(K)\otimes_{\mathbf Z}\mathbf Q)\otimes_K\overline{\mathbf Q}.
\tag{11}
$$
在更大有限 Galois 域中重复(10)，对原 $F$ 点给相同结果：
每个原共轭被重复相同次数，归一因子准确抵消。
所以可对一个指定有限 p-ray 域的有向并一致使用这个投影。

## 3. 固定坏处扩张与只在 p 分歧的角色

令 $t^3=17$、$L=K(t)$，仍用 R733 的
$$
Q_2=(-4/t^2,15/17),\qquad
Q_4=(42/t^4,397/17^2).
\tag{12}
$$
取 $p\nmid6\cdot17$。
设 H/K 为有限阿贝尔扩张，只可能在 p 之上分歧。
则
$$
\boxed{H\cap L=K.}
\tag{13}
$$
事实上 L/K 在 p 处不分歧，而 H/K 在17及所有非p有限处不分歧。
二者交域因而在 K 的全部有限素处不分歧。
它是阿贝尔扩张，K 类数一，所以交域为 K。
K 的复无限处不产生额外实分歧条件。

因此
$$
\operatorname{Gal}(LH/K)
=\operatorname{Gal}(L/K)\times\operatorname{Gal}(H/K).
\tag{14}
$$
令 $\sigma(t)=\omega t$ 并令 $\sigma$ 固定 H；
p-ray 因子 G 则固定 L。
二者都按 (5) 只作用点，故其所有幂等元交换。

对 $k=2,4$，设
$$
E_k:y^2=x^3+17^k,\qquad
\phi_2(x,y)=(x/t^2,y/17),\qquad
\phi_4(x,y)=(x/t^4,y/17^2).
$$
若 $P\in E_k(H)$，直接作用坐标给
$$
\sigma_{\rm pt}\phi_k(P)=[\omega^{k/2}]\phi_k(P).
\tag{15}
$$
这个身份对所有 H 点成立，不仅对 (12) 的两个基点成立。
(15) 与原微分运输
$\phi_2^*\varpi=t\,dx/(2y)$、
$\phi_4^*\varpi=t^2\,dx/(2y)$ 同时保留。

若 $P_\rho\in(E_k(H)\otimes\mathbf Q)\otimes_K\overline{\mathbf Q}$
满足
$$
g_{\rm pt}P_\rho=\rho(g)P_\rho,
\tag{16}
$$
则 $\phi_k(P_\rho)$ 位于联合特征
$(\omega^{k/2},\rho)$ 中。
不同的 $(k,\rho)$ 给不同直接和分量。
特别非平凡 $\rho$ 的(10)严格为零；
平凡分量则准确是 $\phi_k(E_k(K))\otimes_K\overline{\mathbf Q}$。

以上等式对形式点张量使用线性延拓。
不把一个一般代数倍点张量冒作可由椭圆曲线加法实际实现的单个点。

## 4. 自然 Galois trace 不等于点因子 trace

在系数也位于一个 Galois 扩张时，自然作用会同时共轭系数：
$$
g_{\rm diag}(P\otimes a)=g(P)\otimes g(a).
\tag{17}
$$
(17) 是 semilinear 操作，和(5)不同。

原 (12) 给直接的实际反例。
在 $\mathscr V_E(L)$ 中取
$$
X=Q_2\otimes t^2 .
\tag{18}
$$
由 R733，$Q_2$ 非扭，故 $X\ne0$。
另一方面，
$$
\sigma Q_2=[\omega]Q_2,\qquad \sigma(t^2)=\omega^2t^2,
$$
所以
$$
\sigma_{\rm diag}X=X.
\tag{19}
$$
但只作用点时，
$$
e_{\rm triv}^{\rm pt}X
=\frac13(Q_2+[\omega]Q_2+[\omega^2]Q_2)\otimes t^2=0.
\tag{20}
$$
因此自然 trace 的不变对象完全可能具有零的平凡点分量。

这个差别直接适用于原有限门。
即便完整 Mumford 平移、全部配对相位和伙伴微分合起来给 K 定义的 theta 算子，
也不能由此推它的点表示仅含平凡 p-ray 特征。
需要在实际点公式中保留每个代数系数和对应的点特征，再按(9)提取。
一个 Gauss 和或 root-of-unity 系数的逆角色可以与非平凡点角色共同下降；
把该系数先固定后使用自然 trace 是另一项操作。

(18)–(20) 不宣称原完整门必出现这种抵消；
它证明两种 trace 的相等需要另行支付，不能由“在 K 定义”推出。

## 5. 原有限角色负一值的准确接口

本节固定 R746 的原测度及符号：
$$
I_{k,\chi}
=\int_{\mathbf Z_p^\times}x^{-1}\chi(x)\,d\nu_{k,17}(x),
\qquad k=2,4.
\tag{21}
$$
非法 $\chi|_{\mu_6}\ne1$ 的值已由 R746 证明为零。
对合法有限 $\chi$，R746 的真实
$$
\rho_{k,\chi}=\chi\circ(\widehat\psi_k/\widehat{\bar\psi}_k)
$$
只在 p 分歧，而且在所选 p-local units 上为 $\chi^{-1}$。
所以对同一个 k，
$$
\rho_{k,\chi}=\rho_{k,\chi'}
\quad\Longrightarrow\quad\chi=\chi'.
\tag{22}
$$

以下是本节使用的完整输入：

**(H)** 对所考虑的每个 $(k,\chi)$，已经证明存在
$$
\mathbf P_{k,\chi}\in
(E_k(H_{k,\chi})\otimes_{\mathbf Z}\mathbf Q)
              \otimes_K\overline{\mathbf Q},
\quad
A_{k,\chi}\in\overline{\mathbf Q}^{\times},
$$
其中 $H_{k,\chi}/K$ 只在 p 分歧，
使
$$
g_{\rm pt}\mathbf P_{k,\chi}
=\rho_{k,\chi}(g)\mathbf P_{k,\chi},\qquad
\Omega_p I_{k,\chi}
=A_{k,\chi}\mathscr L_p(\phi_k\mathbf P_{k,\chi}).
\tag{23}
$$
这里 $\Omega_p$ 是与 R735/R746 相同的共同非零周期。
零值允许 $\mathbf P_{k,\chi}=0$。
非零值的 A 仍必须是代数数，不能只知它为 p-adic 单位。
从两个不同特征点的对数乘积到(23)的平方根，不属于本篇证明。

**定理 3。**
在(H)成立的任意有限指标族中，所有非零的
$\Omega_p I_{k,\chi}$ 在 $\overline{\mathbf Q}$ 上线性独立。

**证明。**
将全部 $H_{k,\chi}$ 放进同一个有限阿贝尔只p分歧域 H。
由(13)–(16)，$\phi_k\mathbf P_{k,\chi}$ 分别位于
$(\omega^{k/2},\rho_{k,\chi})$ 的联合特征空间。
由(22)及 $k=2,4$，这些联合特征两两不同。
任何(21)的代数线性关系，先用(23)、定理1提升为点张量关系，
再逐个使用联合幂等元。
每个非零分量的系数必须为零；$A_{k,\chi}\ne0$。
证毕。

该定理没有要求这些点空间的维数预先为一。
只用每个实际数属于所写特征空间且非零。
也不需要所有角色值非零；零值直接不进入独立族。

### 5.1 一变量有限门的平凡角色系数

设 $\Phi$ 是 $(\mathbf Z/p^m\mathbf Z)^\times$ 上的代数值函数，
完整 Fourier 展开为
$$
\Phi(x)=\sum_\chi\widehat\Phi(\chi)\chi(x),\qquad
\widehat\Phi(\chi)
=\frac1{\varphi(p^m)}
 \sum_{a\in(\mathbf Z/p^m\mathbf Z)^\times}
       \Phi(a)\chi(a)^{-1}.
\tag{24}
$$
定义真实有限门值
$$
J_k(\Phi)
=\Omega_p\int_{\mathbf Z_p^\times}x^{-1}\Phi(x)\,d\nu_{k,17}(x).
$$
在全部出现的合法角色均满足(H)时，它属于(4)，且准确有
$$
\boxed{
(e_{\rm triv}^{\rm pt})_p^\log J_k(\Phi)
=\widehat\Phi(1)\,\Omega_p I_{k,1}.
}
\tag{25}
$$
这只是把(24)代入、用(9)、(22)、(23)，非法角色本来就是零。

R735 已无条件给 $I_{k,1}\ne0$。
所以在(H)的明确范围内，
$$
\widehat\Phi(1)\ne0\quad\Longrightarrow\quad J_k(\Phi)\ne0.
\tag{26}
$$
若 $\widehat\Phi(1)=0$，(25)只说明其平凡点分量为零，不说明整个值为零。
准确的零判据由定理3给出：
$J_k(\Phi)=0$ 当且仅当每个满足 $I_{k,\chi}\ne0$ 的合法角色都有
$\widehat\Phi(\chi)=0$。

同样，两个 k 的有限门之和为零，须分别在每个联合特征中为零；
两种17 Kummer角色不能彼此抵消。

## 6. 对完整原门的使用范围

R745 已付原有限门和所有有限正阶伙伴矩的代数 theta 来源；
R742 已付固定 $r=1$ 时的有限深度及完整17投影。
这两项保证后续可以保有限代数系数进行实际点公式比较，
但没有单独证明每条来源具有(23)。

特别，完整六变量斜门不是自动等于单条
$D_{k,17}$ 乘一个一变量函数 $\Phi$。
要把(25)用于 R742 的全部 G4、W/V 返回及完整外部，
仍须支付该来源的全 p-Schwartz 谱分解和(H)，
并保所有伴随、坏处、周期以及有限点角色。

同理，原 $J'_S,J'_T,J'_U$ 尚不能仅因它们是 p-adic 数就被施(7)。
只有把整个待用关系的每项都放入同一个(4)后，
推论2才允许施点因子投影。
本篇没有从投影后的负一行非零推出原中央非零。

本篇不使用新的数学运行或生成数据；
唯一非扭点输入是 R733 已证明的实际 $Q_2$。

## 文献与依赖

- C. Fuchs and D. H. Pham,
  [Some applications of the p-adic analytic subgroup theorem](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf),
  *Glasnik Matematički* 51(71) (2016), 335–343，
  Theorem 2.2，p.338；全椭圆对数/有限指数域的使用同 R733。
- [R733](R733-two-cubic-points-and-algebraic-independence-of-p-adic-logarithms.md)：
  原两点、微分、真实 Kummer 角色及全p对数核。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)：
  平凡有限角色的已付共同周期及非零点公式。
- [R742](R742-fixed-seventeen-operators-and-same-gate-primitive-limit.md)、
  [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)：
  原完整有限门、相位及正阶伙伴代数化。
- [R746](R746-original-type-five-all-finite-p-character-squares.md)：
  完整有限角色的真实导子、只p分歧域及平方；
  (23)所需线性点公式仍是独立输入。
