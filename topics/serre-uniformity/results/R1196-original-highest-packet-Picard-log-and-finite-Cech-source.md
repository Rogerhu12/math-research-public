# R1196：原最高型整投影后的 Picard 对数与有限 Čech 源

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 对 R1193 的同一个原最高 primitive packet，先作其真实整投影，再读原 $P=(p-1)D_0$ 的首列，可以完全去掉首层的 $p$-对数分母问题。所需整精度为 $\pi_0^{m^2+1}$，而原 Picard 类只须作至多 $m=(p-1)/2$ 次的 Čech 截断对数，所有分母都是 $p$-单位。其来源仍是原 $G(b_{\rm lift})^2$、三个原 CM 尾的主化函数及同一实际 gluing；并没有另换点差或 ordinary quotient。

本篇同时证明：原 whole-Jacobian 的 degree-$p$ Frobenius 返回项在**这个整 packet 的所需首层**消失。这不是说该 Hasse–Witt 列本身为零，也不是仅凭特殊纤维删除返回项。该结论使下一步只剩有限、无 $p$ 分母的原 Čech 计算。它尚不把所得列或其与 CM Abel 列的楔称为单位。

## 1. 同一个原点、整 packet 与准确精度

保持 R1014、R1018、R1193 的原曲线、点差及所有标记：
$$
X=X_1,\quad J=J_X,\quad
D_0=2[c_1]-[c_\zeta]-[c_{\zeta^2}],\quad P=(p-1)D_0,
$$
$$
p=12g-1>37,\quad m=(p-1)/2,\quad
e_0=m(p+1),\quad R=W(k)[\pi_0],\quad \pi_0^{e_0}=p,
\quad\varepsilon=\pi_0^m.
\tag{1196.1}
$$
这里可先在足够大的有限未分歧底上工作，再作忠实平坦基变到 $k=\overline{\mathbf F}_p$。原 compact-type 模型记为 $\mathcal X/R$，其 Jacobian 好模型为 $\mathcal J/R$。

原点 $P$ 定义于未分歧底，且 R1018 已在整个原形式群证明
$$
P\in F^m\mathcal J(R),\qquad
F^a\mathcal J(R)=\ker\bigl(\mathcal J(R)\to\mathcal J(R/\pi_0^a)\bigr).
\tag{1196.2}
$$
使用 R1193 的真实整幂等元
$$
E_m=(e_{V_m}+e_{P_{m-1}})e_N
\in e_N\mathbf Z_p[\operatorname{PGL}_2(\mathbf F_p)]e_N.
\tag{1196.3}
$$
它经原 full-$p$ pull–push、原 $H_6$ 与 $\kappa_4$ 下降作用在同一个 $J$。所有 Weil 分支同时保留，所以这个作用与原 tame 下降相容。其目标是 $\tau_m+\mathrm{PS}_{m-1}$，不是未经支付的单尖点投影。

置
$$
w_0=m^2-1,\qquad M=m^2+1,\qquad
A_M=R/\pi_0^M,\qquad I=\pi_0^m A_M.
\tag{1196.4}
$$
本篇只有一个固定精度 $M$；它严格小于 $e_0$。因而 $A_M$ 的特征为 $p$，并且
$$
I^{m+1}=0,\qquad m<p,
\qquad (\pi_0^{w_0}A_M)^2=0.
\tag{1196.5}
$$
这些是实际理想幂的消失，不只是每个元素的 $p$ 次方为零。

## 2. 先投影后的真实形式深度

### 引理 1196.1

原连续 $p$-进整作用给出形式点 $E_mP$，且
$$
\boxed{E_mP\in F^{w_0}\mathcal J(R).}
\tag{1196.6}
$$

**证明。** 一个整幂等形式群自同态将原光滑形式群分解为其像与补像。可直接用幂等元在余切空间上的两个自由直和选择参数；形式逆函数定理将乘法映射 $\operatorname{im}E_m\times\operatorname{im}(1-E_m)\to\widehat{\mathcal J}$ 识别为同构。因此其像是光滑形式群，不只是一个有理 Lie 子空间。$\mathbf Z_p$ 系数的作用在形式邻域中由整数近似收敛定义；每个有限精度只需一个整数近似。

R1193 在这个实际像的特殊晶体中已证明，全部 tame 权只能属于
$$
\{m^2,m^2-1,e_0-m^2,e_0-(m^2-1)\}.
\tag{1196.7}
$$
特殊 Hodge 是其中的子模。四个数的最小值为 $w_0$。在像形式群上对阶 $e_0$ 的 tame 群平均，取得与特殊余切基相同的真实 eigenparameters。若参数权为 $w$，原未分歧点的该参数值属于 $\pi_0^w W(k)\cap R$。故每个参数值至少含 $\pi_0^{w_0}$，得 (1196.6)。

这里使用的不是“特殊型相同所以整格相同”，而是已成的整 $E_m$ 的实际形式像及其 tame 坐标。证毕。

### 引理 1196.2

在模 $\pi_0^M$ 的平方零核中，原 $p$-进形式对数与规范切空间识别一致：
$$
\boxed{\log_{\mathcal J}(E_mP)
\equiv E_mP\pmod{\pi_0^M\operatorname{Lie}\mathcal J}.}
\tag{1196.8}
$$
右边指 $F^{w_0}/F^M$ 的规范平方零 Lie 类。

**证明。** 整形式群的不变微分使形式对数的总次数 $n$ 系数分母至多为 $p^{v_p(n)}$：若一个多项式系数为 $a_\alpha$，则每个 $\alpha_j a_\alpha$ 整，而 $\min_jv_p(\alpha_j)\le v_p(n)$。因此在深度 $w_0$ 的点上，次数 $n\ge2$ 的项估值至少为
$$
nw_0-e_0v_p(n).
\tag{1196.9}
$$
若 $p\nmid n$，该数至少为 $2w_0\ge M$。若 $v_p(n)=a\ge1$，则它至少为 $p^a w_0-ae_0$。其 $a=1$ 值严格大于 $m^2$，且随后每一步增加 $(p-1)p^a w_0-e_0>0$。所以全部非线性项在所示精度消失。与 (1196.5) 的平方零识别比较即得结论。证毕。

## 3. 原相对 Picard 核的真正有限对数

令 $\mathcal X_M=\mathcal X\times_R A_M$。原 $P$ 对应一个实际的零多度线丛 $\mathscr L_P$；它的泛纤维是 $O_X((p-1)D_0)$，在各分量上的 multidegree 按原树形模型转移。由 (1196.2)，它在 $A_M/I=R/\pi_0^m$ 上平凡。

选择该平凡化及一个实际有限仿射覆盖，提升其局部 frame。Nakayama 引理保证提升仍为 line frame，于是重叠上的真实 transitions 满足
$$
g_{ij}=1+x_{ij},\qquad x_{ij}\in I\mathcal O_{\mathcal X_M},
\qquad g_{ij}g_{jk}=g_{ik}.
\tag{1196.10}
$$
这不是为每个节点另选一个无关函数。它是同一个 $\mathscr L_P$ 的 Čech 代表。

由于 $I^{m+1}=0$，有限级数
$$
\ell_I(1+x)=\sum_{a=1}^{m}\frac{(-1)^{a+1}}a x^a,
\qquad
\exp_I(y)=\sum_{a=0}^{m}\frac{y^a}{a!}
\tag{1196.11}
$$
定义互逆的 sheaf 群同构 $1+I\mathcal O\simeq I\mathcal O$。乘法和互逆恒等式可在 $\mathbf Z_{(p)}$ 上按总次数 $\le m$ 验证；所有更高总次数属于 $I^{m+1}$，故为零。这里完全不使用分母 $p$。

还需确认其确实读取原 Picard 类，而不是一个附带 choice 的较大群。由单位 sheaf 精确列
$$
1\to1+I\mathcal O_{\mathcal X_M}
\to\mathcal O_{\mathcal X_M}^{\times}
\to\mathcal O_{\mathcal X_M/I}^{\times}\to1,
\tag{1196.12}
$$
全局单位映射是满射：原 proper、几何连通族的 $H^0(O)=A_M$，故全局单位为 $A_M^\times$，而任一 nilpotent 商的单位均提升。长正合列因此将 relative Picard 核准确识别为 $H^1(1+I\mathcal O)$。

另一方面，原 compact-type 族的 $H^1(O)$ 是自由 $R$-模，且与任意此处的基变相容。也可由 $R\Gamma(O)$ 的自由两项模型与 $H^0(O)=R$ 直接核准。因此
$$
H^1(\mathcal X_M,I\mathcal O)
=I\otimes_{A_M}H^1(\mathcal X_M,O)
=I\operatorname{Lie}(\mathcal J_{A_M}).
\tag{1196.13}
$$
得到规范的同构
$$
\boxed{\quad
\operatorname{Pic}(\mathcal X_M,I)
\xrightarrow{\ \ell_I\ }
I\operatorname{Lie}(\mathcal J_{A_M}),\qquad
[\mathscr L_P]\longmapsto
\left[\sum_{a=1}^{m}\frac{(-1)^{a+1}}a(g_{ij}-1)^a\right].
\quad}
\tag{1196.14}
$$
换 frame 只加有限对数的 Čech coboundary。改变所选模 $I$ 平凡化的全局单位可以提升，所以也不改变右边的类。

## 4. 实际 pull–push、整角及首列公式

有限对数与 pullback 显然相容。对真正有限平坦态射及其 norm，有精确恒等式
$$
\ell_I\bigl(\operatorname{Nm}(1+x)\bigr)
=\operatorname{Tr}\bigl(\ell_I(1+x)\bigr).
\tag{1196.15}
$$
这是 $\log\det=\operatorname{Tr}\log$ 在次数 $\le m$ 的普遍多项式恒等式；仍只除 $1,\ldots,m$。所以该式在 degree 被 $p$ 整除时也成立，不需要反除 norm 的次数。

不必假设原 full-level correspondence 经每一次正则化后都仍逐箭头有限平坦。它已在原好 Jacobian 上给出实际整自同态。对任一这样的形式群同态，(1196.14) 下的作用等于其 Lie 作用。严格地，在通用测试环 $A_M[T_1,\ldots,T_d]/(T_1,\ldots,T_d)^{m+1}$ 上应用同一个 Picard 有限对数；共轭后的自同态是次数至多 $m<p$ 的 additive polynomial。次数 $2,\ldots,m$ 的 additive polynomial 全为零，故它恰为其 Lie 一次部。再将测试变量代入实际理想 $I$ 即得所需自然性。这里也可在真实有限平坦细化上先用 (1196.15)，再以实际 Picard 延拓的唯一性比较。

因此 $E_m$ 必须作用于 Picard 类，或作用于右边的 $H^1$ 类；**不是逐个 transition 的普通函数算子**。结合 (1196.6)、(1196.8) 及平方零理想到 $I$ 的自然性，得到本篇主公式：
$$
\boxed{\quad
E_m\log P
\equiv
 dE_m\left[
\sum_{a=1}^{m}\frac{(-1)^{a+1}}a(g_{ij}-1)^a
\right]
\pmod{\pi_0^{m^2+1}\operatorname{Lie}\mathcal J}.
\quad}
\tag{1196.16}
$$
它同时保留该 packet 可能的第 $m^2-1$ 层和所求第 $m^2$ 层。投影后的右侧自动属于 $\pi_0^{m^2-1}\operatorname{Lie}$；不要求投影前的 Čech 类已经这么深。

### 4.1 与原主化函数的同一性

R1014 给原特殊纤维的完整主化：中心用
$$
G(b)^2,\qquad G(b)=\frac{(b-1)^2}{b^2+b+1},
$$
三个原 CM 尾用 $x_\xi^{m a_\xi}$，其中 $a_1=2$、$a_\zeta=a_{\zeta^2}=-1$，其余分量用一。R1018 的真正 ordinary quotient 将中心函数提升为 $G(b_{\rm lift})^2$，而不是 $G(b)^p$ 或另一个 target 参数。

从这组数据细化并提升到 (1196.10) 即给本篇指定输入。模 $\pi_0^m$ 的延长存在性是原 $P\in F^m$；任何两次延长只改变上面的 coboundary。因此 (1196.16) 没有隐藏一个可任选的 Picard 常数。另一方面，式中仍必须保留三个 CM 尾、各节点和中心的全部实际 transitions；不能只保某一条 generic 尾上的 $G$-Taylor 项。

## 5. 为什么原 degree-$p$ 返回在本 packet 首层消失

本节给与 R1023 的原 whole-Jacobian 对数公式直接相容的检验，防止把 (1196.16) 误读成删除真实 Frobenius。

使用 R1023 的 strict integral formal coordinates：它们保持真实 tame 平均，且形式对数的次数 $2,\ldots,p-1$ 已消去。写 $Z=Z(P)$、$E=dE_m$，以 $H$ 表示整个非约化 $R/(p)$ 上的实际 $H^1(O)$ Frobenius 矩阵。原次数 $p$ 部分满足
$$
pB_p(Z)\equiv HZ^{(p)}\pmod p.
\tag{1196.17}
$$
实际 Picard 自同态与 Frobenius 交换，所以
$$
EH\equiv HE^{(p)}\pmod p.
\tag{1196.18}
$$
这里 $(p)$ 对矩阵系数及变量作真正特征 $p$ Frobenius，包含非约化底的 $\pi_0\mapsto\pi_0^p$；不只对剩余域系数取 $p$ 次方。

$EZ$ 是实际 packet Lie 格中的 tame 固定向量，因此同引理 1196.1 的坐标论证给 $v_{\pi_0}(EZ)\ge w_0$。取整矩阵提升，(1196.17)–(1196.18) 于是给
$$
E B_p(Z)
=\frac1p H(EZ)^{(p)}
 +\text{估值至少为 }pm\text{ 的整项}.
\tag{1196.19}
$$
第一项估值至少为 $pw_0-e_0>m^2$，而 $pm>m^2$。故该整个 projected degree-$p$ 项在本篇精度消失。

次数 $n>p$ 的项，原 $Z(P)$ 深度为 $m$，故估值至少为 $nm-e_0v_p(n)$。若 $p\nmid n$，它至少为 $e_0>m^2$；若 $v_p(n)=1$，用 $n\ge2p$ 得至少 $2m^2>m^2$；若 $v_p(n)\ge2$，最小值从 $p^2m-2e_0>m^2$ 起严格增加。这也排除了所有更高对数项。

所以这里的消去依赖**同一个真实整投影与 Frobenius 的相容式**。原矩阵 $H_{\rm bottom\to hi}$ 可非零，其与未投影坐标的配对也可非零；本篇不把它独立设为零。最低型的 $w_0=m$ 不满足 (1196.19) 的估值，故 R1023 的最低型返回项没有被撤回。

## 6. 与原最高 CM 列及同一 $\beta$ 的准确接口

R1193 已给实际负 Hodge 向量 $L=\sum_sL_s\omega_s^{\rm hi}$ 的整提升 $\Omega_L\in E_mH^0(\mathcal X,\omega)$，其原 tame 权为 $m^2$、deck 角色为 $\zeta^2$。定义同一个原点的线性读数
$$
\mathcal V_m(L)
=\overline{\pi_0^{-m^2}
\langle\log P,\Omega_L\rangle}\in k.
\tag{1196.20}
$$
配对的整性由 (1196.16) 给出；其精确 tame character 迫估值至少为 $m^2$。有限角对 Rosati 的 $g\mapsto g^{-1}$ 稳定，故它在该配对上自伴，因而可以将 $E_m$ 放在任一槽。

这一读数只依赖 $L$。确实，同一个底向量的两个整 eigenlifts 若不同，在本篇精度内唯一可能的较低 Hodge 权是 $m^2-1$，需乘一次 $\pi_0$。但原中心该权的全纯空间是 $k\,db/u$，其 deck 角色为 $\zeta$；它不能进入所定的 $\zeta^2$ 提升。其余 (1196.7) 的权与 $m^2$ 之差的最小正代表均大于 $m^2$，而同权差至少含 $\pi_0^{e_0}$。因此任何 lift 差对 (1196.20) 的贡献为零。

用 Čech–Serre 配对，(1196.16) 将该完整列写成
$$
\boxed{\quad
\mathcal V_m(L)=
\overline{\pi_0^{-m^2}
\left\langle
 dE_m\left[\sum_{a=1}^{m}
\frac{(-1)^{a+1}}a(g_{ij}-1)^a\right],\Omega_L
\right\rangle}.
\quad}
\tag{1196.21}
$$
这里全部数据在同一个 $\mathcal X_M$ 上，包含完整节点与分量 gluing。它是一个有限整 Čech 读数，不调用未知的高阶 Hasse–Witt 列，也不把一个形式存在的 derived 同伦当作显示数值。

与其比较的原 CM Abel 列已经由 R1193 给出
$$
\mathcal T_m(L)=T_L(1)
=\frac{2A_p(1)}m
\sum_s\frac{\lambda_s\rho_sL_s}{1-s},
\tag{1196.22}
$$
并带该文全部 $\kappa_{\rm hi}$、marked parameter 及 $p^3$ 盘尺度。本篇没有改变这些单位。

对 R1191 的同一个实际 $q_C:J\twoheadrightarrow C$、$\beta=q_C(D_0)$，仍有 $q_CE_m=e_mq_C$，但不要求任意 $q_C$ 预先 Hecke-equivariant。证明如下：将 $E_m$ 的有限 character 值与 $e_m$ 的 cyclotomic CRT 系数放在同一个嵌入 $\mathbf Q_p$ 的有限代数数域，再取该域到 $\overline{\mathbf Q}_\ell$ 的嵌入，$\ell\ne p$。原 local–global compatibility 将 $E_m$ 在 $V_\ell J$ 上的作用识别为 $\tau_m+\mathrm{PS}_{m-1}$ 的惯性 isotypic 投影。R1191 证明 $C$ 只含其全部 primitive 尖点型，而 $e_m$ 恰选 $\tau_m$。实际 $q_C$ 与 $G_{\mathbf Q_p}$ 交换，故保持这些惯性 isotypic 部分；在 Tate 模上便有 $q_CE_m=e_mq_C$。有理 Hom 的 Tate 作用单射以及系数基变的忠实性将等式送回原 $\operatorname{Hom}\otimes\mathbf Q_p$。右边 $e_m$ 已由 R1191 保持任意既定 $C$ 的原整格。

因此
$$
dq_C(E_m\log P)=(p-1)e_m\log\beta.
\tag{1196.23}
$$
$p-1$ 是单位，没有另加同源尺度。实际 $dq_C$ 仍须作用在 (1196.21) 的完整类上；不能因整个 packet 中 (1196.22) 有单位向量，就认定指定 $C$ 的楔为单位。R1190 只控制真实子簇运输的至多一个 $p$ 格损失，不能替代这项数值比较。

## 7. 原 generic 尾的全部局部次数及最高 gap 单位

为了使 (1196.21) 的局部输入可直接继续计算，这里给原特殊尾上所有所需次数的准确投影，保持其使用范围。

写
$$
D_s:Y^2=X(X^{m+1}+A_s),\qquad
X=z^{-2},\quad
Y=z^{-(m+2)}\sqrt{1+A_sz^{p+1}},
$$
$$
\psi_s=z^{-m}(1+A_sz^{p+1})^{-1/2}.
\tag{1196.24}
$$
$\psi_s$ 是同一个 ordinary-node 局部函数，仍不称为整个 quotient 尾的全局 regular 函数。对 $1\le a\le m$，其特殊纤维 Čech 类为
$$
[\psi_s^a]=0\quad(a\text{ 偶}),
$$
$$
\boxed{\quad
[\psi_s^a]=
(-1)^{(a-1)/2}
\binom{a-1}{(a-1)/2}A_s^{(a-1)/2}
[z^{-(m+1-a)}]\quad(a\text{ 奇}).
\quad}
\tag{1196.25}
$$

**证明。** 完整 Hodge 基为
$$
\omega_j=-2z^{m-2j-1}(1+A_sz^{p+1})^{-1/2}dz,
\qquad0\le j\le(m-1)/2.
$$
若 $a=2b+1$，$\psi_s^a\omega_j$ 的 residue 只有在 $j=b$、二项展开取第 $b$ 项时出现，其系数是
$-2(-1)^b\binom{2b}{b}A_s^b$。该 residue 与 gap $z^{-(m-2b)}$ 的配对 $-2$ 比较，正给 (1196.25)。若 $a$ 偶，所需 residue 指数的奇偶性矛盾；所有配对为零。Serre 对偶的非退化性完成证明。

特别地，$a=m$ 的局部最高 gap 系数
$$
c_{m,s}=(-1)^{(m-1)/2}
\binom{m-1}{(m-1)/2}A_s^{(m-1)/2}
\in k^\times
\tag{1196.26}
$$
是单位。所有阶乘指标都小于 $p$。

原 target eigenparameter 及六标记的实际变换仍为
$$
t_s=c_s\varepsilon\psi_s\pmod p,\qquad
b_{\rm lift}=B_s(t_s),\quad B_s'(0)\in W(k)^\times.
$$
在该重叠上的 Igusa 主化部分，定义真实有限 Taylor 系数
$$
\log\frac{G(B_s(T))^2}{G(B_s(0))^2}
\equiv\sum_{a=1}^{m}\ell_{a,s}T^a\pmod{T^{m+1}}.
\tag{1196.27}
$$
其线性项是 $B_s'(0)\lambda(s)$，与 R1018/R1023 的原底输入一致。这个部分对最高 gap 的直接项是
$$
\varepsilon^m c_s^m\ell_{m,s}c_{m,s}[z^{-1}].
\tag{1196.28}
$$
不把 $B_s(0)$ 强制改成 Teichmüller 提升，也不删其高阶参数系数。更不从 (1196.26) 推出 $\ell_{m,s}$ 为单位。

(1196.25) 只是原特殊尾上的精确局部消元。将其代入完整 (1196.21) 时，低次数的 regular 消去函数与正次节点尾仍必须随同原 Čech coboundary 运输。先投影已经删除的是首层 $p$-分母返回，而不是这些无 $p$ 分母的实际 gluing 数据。

## 8. 已关闭与仍未关闭的门

已关闭的是：同一个原 $P$ 的高型首列无需另求 $H_{\rm bottom\to hi}$ 的高 normal 系数；它由 (1196.16)/(1196.21) 的有限整源决定，且所有 frame、norm 与 actual quotient 比较都保持原 Picard 类。原 generic 尾的全部 $a\le m$ 局部幂也已有 (1196.25) 的完整公式。

仍需计算的是：这个有限源经过实际全图消元后的列，在同一个 $C$ 槽上与 (1196.22) 的楔及其估值。没有把有理非零、packet 上的一个单位、某条尾的局部单位或第一次 residue 条件当成整个 $p^3$ 盘的排点结论。Serre 主目标仍 OPEN。

## 9. 来源

- [R1014](R1014-original-CM-divisor-reduction-and-Igusa-Frobenius-principalization.md) §§2–4：原 compact-type 模型、完整树形 Picard、中心 $G^2$ 与三个原 CM 尾 $x_\xi^{ma_\xi}$ 的同一主化。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)：同一个 $P\in F^m$、真实 ordinary quotient、完整 tame 参数及原 $\psi_s$。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)、[R1023](R1023-original-CM-divisor-complete-first-log-vector.md) §§2–3：真实非约化模 $p$ 图、原 target 参数、形式对数分母及实际 Frobenius 矩阵。本文 §5 解释为何这里只在先整投影之后删除其首层贡献。
- [R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md) §§2–7：实际 $E_m$、完整型权、负 Hodge 中心的唯一性、同一 marked CM 列与整个原 $p^3$ 盘尾界。
- [R1191](R1191-original-half-rank-factor-all-primitive-inertia-slots.md)、[R1190](R1190-original-one-p-Neron-Lie-lattice-bound.md)：同一指定 $C,\beta$ 的整槽及实际格界；只按各自已成范围消费。

全部证明为纸面 sheaf、形式群、有限截断和原坐标计算；没有执行数学程序。root逐节核对，o2独立核对 §§3–4 的相对 Picard 核、全局单位提升、自由上同调与有限对数自然性；§6 另补 Tate 惯性交织证明，未假设任意商映射为 Hecke-equivariant。
