# R52：实际异常像的小满射素数与有界次数检测域

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：有限群、交域、分歧和判别式结论无条件已证；§7 的最小素数对数界明确以 GRH 为条件；主目标未解决。** 本文构造的检测扩张次数有绝对上界，但其判别式依赖实际曲线的导子。正密度与有界次数均没有变成 O3 所需的统一小素数界。

## 1. 适用范围与结论

设 $E/\mathbb Q$ 非 CM，$p>37$，且 $\bar\rho_{E,p}$ 不满射。由 R1，其实际像是完整非分裂 Cartan 正规化子 $N_{\rm ns}(p)$。令
$$
\epsilon:G_{\mathbb Q}\longrightarrow N_{\rm ns}(p)/C_{\rm ns}(p)\simeq\{\pm1\},
\qquad K=\overline{\mathbb Q}^{\ker\epsilon}.
$$
R5 给出 $K$ 为虚二次域，$p$ 在 $K$ 惰性，特别在 $p$ 不分歧。

**定理 R52。** 对每一条这样的实际异常曲线：

1. 存在 $\ell\in\{2,3,5\}$，使完整 $\ell$ 进表示满射到 $\mathrm{GL}_2(\mathbb Z_\ell)$。
2. 取 $m=4$（当 $\ell=2$）或 $m=\ell$（当 $\ell=3,5$），令
   $$
   L_m=\mathbb Q(E[m]),\quad
   P_m=L_m^{(\mathbb Z/m\mathbb Z)^\times I},\quad M_0=P_mK.
   $$
   则 $[M_0:\mathbb Q]\le240$。其中有非空共轭不变子集 $\mathcal C$，比例至少 $1/4$；每个满足
   $$
   q\nmid mN_E,\qquad \operatorname{Frob}_q(M_0/\mathbb Q)\subset\mathcal C
   $$
   的素数都满足 $\epsilon(q)=-1$ 且 $a_q(E)\ne0$。
3. 若 $\bar\rho_{E,5}$ 满射，则对每个 $r\ge1$，
   $$
   \boxed{\mathbb Q(E[5])\cap\mathbb Q(E[p^r])=\mathbb Q.}\tag{52.1}
   $$
   同样与整个 $p$ 幂除法塔不交。
4. 令 $R=\operatorname{rad}(30N_E)$，则
   $$
   M=M_0\mathbb Q(\sqrt R)
   $$
   是次数 $n\le480$ 的 Galois 扩张，其不分歧素数全部为 $E$ 的好素数，且
   $$
   \boxed{\log D_M\le(n-1)\log R+n\log n
   \le479\log R+480\log480.}\tag{52.2}
   $$
   $\mathcal C$ 在 $\operatorname{Gal}(M/\mathbb Q)$ 中的逆像保持相同比例。

以下证明也处理 $K$ 与小除法域发生二次交叠的情形；不假定它们总是线性不交。

## 2. 六个 GMR 例外都被实际异常像排除

Genao–Mayle–Rouse [GMR], Theorem 2 给出完整 $\ell$ 进满射素数 $\ell\le7$；除下表六个 $j$ 外可以取 $\ell\le5$。这六个值全部有有理三同源。

定义 $j_3(t)=(t+27)(t+3)^3/t$。逐项恒等式如下：

| $j$ | 满足 $j=j_3(t)$ 的 $t$ |
|---|---:|
| $-2^{-3}5^2\,241^3$ | $-729/2$ |
| $-2^4 3^2\,13^3$ | $-81$ |
| $-2^{-5}5\,29^3$ | $-32$ |
| $-2^{-1}5^2$ | $-2$ |
| $2^4 3^3$ | $-9$ |
| $2^{-15}5\,211^3$ | $-729/32$ |

为直接证明三同源，令 $u=t+27$，考虑
$$E_t:\quad y^2+xy+u^{-1}y=x^3.$$
表中 $u\ne0,27$，故判别式 $u^{-3}(1-27/u)$ 非零。点 $(0,0)$ 处的切线为 $y=0$，与三次曲线的交数为三，因此该点是有理三阶点。Weierstrass 不变量给
$$j(E_t)=\frac{u(u-24)^3}{u-27}=j_3(t).$$
这些 $j$ 均不为 $0,1728$；同一 $j$ 的任意 $\mathbb Q$ 曲线是 $E_t$ 的二次扭曲，其三阶点生成的循环子群仍为 Galois 稳定。所以全都具有有理三同源。

Lemos [L], Theorem 1.1 排除所有带非平凡有理循环同源的非 CM 曲线在 $p>37$ 异常。因此上述六个例外均不出现，证明定理第 1 项。特别地，选到 $\ell=2$ 时确有模四满像，不能以仅有模二满像替代这一步。

## 3. 所有二次交叠与射影下降

按上述选取，$L_m$ 的实际 Galois 群为完整
$$G_m=\mathrm{GL}_2(\mathbb Z/m\mathbb Z).$$
其标量子群阶分别为 $2,2,4$，故
$$
[P_4:\mathbb Q]=48,\qquad
[P_3:\mathbb Q]=24,\qquad
[P_5:\mathbb Q]=120. \tag{52.3}
$$
乘一个可逆标量不改变“迹模 $m$ 是否为零”，所以这个条件可以下降到射影群。

### 3.1 模三和模五

任何二次特征 $G_\ell\to\{\pm1\}$ 在 $\mathrm{SL}_2(\mathbb F_\ell)$ 上平凡：后者由阶为奇数 $\ell$ 的初等幺幂元生成。因此唯一非平凡二次特征是行列式的二次特征。Weil 配对识别其域为
$$\mathbb Q(\sqrt{\ell^*}),\qquad \ell^*=(-1)^{(\ell-1)/2}\ell.$$
于是模三只可能交叠于 $K=\mathbb Q(\sqrt{-3})$；模五的唯一二次子域 $\mathbb Q(\sqrt5)$ 是实域，与虚二次 $K$ 不同，故
$$K\cap L_5=\mathbb Q.\tag{52.4}$$
上述特征在标量上都平凡；若 $K\subset L_m$，则已在 $P_m$ 内。

### 3.2 模四

记 $s:G_4\to\{\pm1\}$ 为模二约化 $G_2\simeq S_3$ 的符号，$d$ 为行列式 modulo $4$ 的特征。$G_4$ 的非平凡二次特征恰为 $s,d,sd$。

证明如下。两个初等矩阵 $e_{12}(1),e_{21}(1)$ 共轭，故任意二次特征 $\psi$ 在二者上取相同值。乘上适当的 $s^e$，$e\in\{0,1\}$，可使 $\psi s^e$ 杀掉二者。局部环 $\mathbb Z/4\mathbb Z$ 上的 $\mathrm{SL}_2$ 由这些初等矩阵生成：利用一个单位矩阵项消元，归约为 $\operatorname{diag}(v,v^{-1})$，而后者也是初等矩阵之积。因此 $\psi s^e$ 经行列式分解，得到所述列表；三个特征确实两两不同。

它们都杀掉 $\pm I$。所以若 $K\subset L_4$，已经 $K\subset P_4$，联合像为 $s,d,sd$ 之一的图；若不交，联合像为直积。这里使用模四是必要的：若 $K$ 是模二 $S_3$ 域的判别式二次域，所有惰性 Frobenius 在模二都是换位，迹为零；模四迹为 $2$ 仍可检测非零整数迹。

## 4. 共轭不变检测集合与精确密度

在 $M_0=P_mK$ 上定义
$$\mathcal C=\{g:\epsilon(g)=-1,\ \operatorname{tr}(g)\not\equiv0\pmod m\}.$$
迹的零与非零已按 §3 下降到射影群；故此定义良定且共轭不变。

对奇 $\ell$，$G_\ell$ 中迹零可逆矩阵数为 $\ell^2(\ell-1)$。理由是全部迹零矩阵有 $\ell^3$ 个，其中行列式零者为幂零矩阵，有 $\ell^2$ 个：每条直线作为共同像和核，给 $\ell-1$ 个非零秩一幂零矩阵，另加零矩阵，合计 $(\ell+1)(\ell-1)+1=\ell^2$。

故与 $K$ 不交时检测比例为
$$
\frac12\left(1-\frac{\ell}{\ell^2-1}\right)
=\begin{cases}5/16,&\ell=3,\\19/48,&\ell=5.\end{cases}
$$
模三交叠时，惰性条件要求行列式为非平方。该陪集有 $24$ 个元素，其中迹零者的特征多项式为 $X^2-1$，构成一个大小为 $48/4=12$ 的共轭类；其余 $12$ 个迹非零，比例为 $12/48=1/4$。

对 $G_4$，总阶为 $96$。模二每个元素有 $16$ 个提升。两个三循环全部提升迹为奇数；三个换位各有八个迹为 $2$ 的提升，其中行列式 $1,3$ 各四个；恒等元素的提升 $I+2H$ 满足
$$
\operatorname{tr}(I+2H)=2+2\operatorname{tr}H,\qquad
\det(I+2H)=1+2\operatorname{tr}H,
$$
所以其八个非零迹提升全部行列式为 $1$。由此得到：

| $K$ 的交叠方式 | 联合群中的检测比例 |
|---|---:|
| 与 $L_4$ 不交 | $64/192=1/3$ |
| 特征 $s$ | $24/96=1/4$ |
| 特征 $d$ | $28/96=7/24$ |
| 特征 $sd$ | $28/96=7/24$ |

移到射影群时标量陪集整齐合并，比例不变。结合 (52.3)，得到
$$
[M_0:\mathbb Q]\le240,\qquad
\frac{|\mathcal C|}{|\operatorname{Gal}(M_0/\mathbb Q)|}\ge\frac14.
\tag{52.5}
$$
若 $q\nmid mN_E$，则好约化挠点表示的 Frobenius 迹为 $a_q(E)\bmod m$，检测条件确实给 $a_q(E)\ne0$。Chebotarev 因而给这样一个正密度素数集；它尚不给首个素数大小。

## 5. 模五满像与完整异常 p 幂塔不交

本节只需模五满像，不需 R41 的固定或变量 CM 参考族。令
$$L_{p^r}=\mathbb Q(E[p^r]),\qquad J=\mathbb Q(E[5])\cap L_p.$$
实际一级群 $N=C\rtimes C_2$ 可解；R41 §2 的交换子计算给
$$N^{\rm ab}\simeq\mathbb F_p^\times\times C_2.$$
对应的最大阿贝尔子域为 $\mathbb Q(\zeta_p)K$。

另一方面 $\mathrm{SL}_2(\mathbb F_5)$ 完美。令 $h=\operatorname{diag}(2,2^{-1})$；因
$$[h,e_{12}(x)]=e_{12}(3x),$$
全部上初等元都是交换子，下初等元同理，它们生成整个 $\mathrm{SL}_2$。所以任何从 $\mathrm{GL}_2(\mathbb F_5)$ 到可解群的商都杀掉 $\mathrm{SL}_2$，因而经行列式分解。

$J$ 同时是两侧的 Galois 商；由可解性和 Weil 配对，
$$J\subseteq\mathbb Q(\zeta_5)\cap\bigl(\mathbb Q(\zeta_p)K\bigr).$$
$K$ 在 $p$ 不分歧，而 $\mathbb Q(\zeta_p)$ 在 $p$ 全分歧，所以 $\mathbb Q(\zeta_p)K$ 的 $p$ 惯性固定域恰为 $K$。$\mathbb Q(\zeta_5)$ 在 $p$ 不分歧，故 $J\subset K$；但 $\mathbb Q(\zeta_5)$ 的唯一二次域 $\mathbb Q(\sqrt5)$ 为实域。因此 $J=\mathbb Q$。

对高层，$L_{p^r}/L_p$ 的次数为 $p$ 幂。置 $J_r=\mathbb Q(E[5])\cap L_{p^r}$；因 $J_r\cap L_p=\mathbb Q$，其次数同时整除 $480$ 和某个 $p$ 幂。$p>37$ 与 $480$ 互素，故 $J_r=\mathbb Q$。整个塔的任何有限交域均已在某个有限层，证明 (52.1) 及无限塔结论。

这个不交结论只控制联合 Galois 像。它没有提升任何 CM 挠点同构，也没有把惰性迹的模 $p$ 整除提升到模 $p^r$。

## 6. 必须排除坏约化素数并保留判别式

有限挠点域在某些坏素数也可能不分歧：乘法约化时，Tate 参数赋值被 $m$ 整除即可使模 $m$ 的幺幂惯性消失。因此不能把“在 $M_0$ 不分歧”直接当作好约化。

令 $R=\operatorname{rad}(30N_E)$。它是偶平方自由整数，$T=\mathbb Q(\sqrt R)$ 的判别式为 $4R$；每个除 $R$ 的素数都在 $T$ 分歧。置 $M=M_0T$，则其所有不分歧素数都不除 $30N_E$。

除法域在 $mN_E$ 支集外不分歧，商二次域在 $N_E$ 支集外不分歧（[MW], Lemma 15，或 R5），故 $M$ 只在 $R$ 的支集分歧。又 $[M:\mathbb Q]\le2[M_0:\mathbb Q]\le480$。限制映射到 $\operatorname{Gal}(M_0/\mathbb Q)$ 满射，故 $\mathcal C$ 的逆像非空、共轭不变、比例不变。

有限 Galois 数域的局部 different 估计为
$$v_q(D_M)\le n-1+n\,v_q(n).$$
具体说，局部分歧指数为 $e$ 时，在最大不分歧子扩张上取 uniformizer 的 Eisenstein 多项式；其导数各项的赋值模 $e$ 互不相同，故 different 指数至多 $e-1+e\,v_q(e)$。乘残数次数并对 $q$ 上方素点求和，利用 $e\mid n$ 即得该式。将所有分歧素数相加，
$$
\log D_M
\le(n-1)\sum_{q\mid D_M}\log q
+n\sum_{q\mid D_M}v_q(n)\log q
\le(n-1)\log R+n\log n.
$$
这也是 [MW], Lemma 7 的证明。于是得到 (52.2)，完成定理全部无条件结论。

## 7. 有效素数界及其参数限制

Ahn–Kwon [AK], Theorem 1.1，无条件给每个非空共轭类一个不分歧素数 $q\le D_M^{12577}$。所以本文构造确有好素数满足
$$
\epsilon(q)=-1,\quad a_q(E)\ne0,\quad
q\le\bigl(480^{480}R^{479}\bigr)^{12577}.
\tag{52.6}
$$
这是有导子参数的极弱界，不是统一界，也不声称为最佳有效常数。

**GRH 条件性推论。** 假设所用 Galois 扩张的 Dedekind zeta 函数满足 GRH。Bach–Sorenson 的形式（[MW], Theorem 5）给
$$q\le(4\log D_M+2.5n+5)^2.$$
检测素数不可能为 $p$：坏约化时已排除；好约化时，普通惯性含两个不同且和非零的 $\mathbb F_p$ 特征值，与非分裂正规化子不相容，故 $E$ 在 $p$ 超奇异，且 $a_p(E)=0$。所以 $q\ne p$，实际异常像使 $p\mid a_q(E)$，Hasse 界给 $p\le2\sqrt q$。代入 (52.2) 得
$$
p\le3832\log\operatorname{rad}(30N_E)+3840\log480+2410.
\tag{52.7}
$$
这比 [MW], Theorem 1 已有的一般 GRH 界
$$c(E)\le964\log\operatorname{rad}(2N_E)+5760$$
更弱，不能包装为新的最佳导子界。

对 R41 的两种限定实际族，还可使用更小的扩张。该结果给 $H=\mathbb Q(E[2])$ 的群为 $S_3$，且 $H\cap\mathbb Q(i)=\mathbb Q$。取 $M_0=H\mathbb Q(i)$，次数为 $12$；三循环且在 $\mathbb Q(i)$ 惰性的子集比例为 $1/6$，检测 $a_q(E)$ 为奇数。令
$$R_0=\operatorname{rad}(2N_E),\qquad M=M_0\mathbb Q(\sqrt{R_0}).$$
则次数至多 $24$，$\log D_M\le23\log R_0+24\log24$。完全相同的 GRH 推导给
$$
\boxed{p\le184\log\operatorname{rad}(2N_E)+192\log24+130
<184\log\operatorname{rad}(2N_E)+741.}\tag{52.8}
$$
这是限定族的条件性导子界；没有去掉 GRH 或导子参数。

## 8. O3 尚未解决的部分

有界次数不能控制判别式。R13、R24 允许坏约化支集及其素数大小增长，未给 $\log\operatorname{rad}(N_E)$ 的统一上界；因此 (52.6)–(52.8) 与任意大的异常 $p$ 仍相容。

R7 的无限反例族从另一个角度说明此限制：删除 GMR 的六个 $j$ 后，它们也有完整 $2/3/5$ 进满像之一，且能同时满足任意长的零惰性迹窗口、$p$ 处完整局部非分裂像和分母处 Tate 幂条件；但其全局模 $p$ 像为整个 $\mathrm{GL}_2$。因此这不是实际异常族的反例，却证明小辅助满像加这些局部条件不足以给统一检测界。继续 O3 必须利用实际全局异常像，获得本文尚无的额外算术限制。

## 9. 来源

- T. Genao, J. Mayle, J. Rouse, *A uniform bound on the smallest surjective prime of an elliptic curve*, Ramanujan J. **70** (2026), article 22，Theorem 2：[期刊全文](https://link.springer.com/article/10.1007/s11139-026-01376-8)。只使用已证小满射素数定理及其六个 $j$ 例外，三同源排除在 §2 自含证明。
- P. Lemos, *Serre's Uniformity Conjecture for Elliptic Curves with Rational Cyclic Isogenies*, Trans. AMS **371** (2019)，Theorem 1.1：[作者稿](https://arxiv.org/html/1702.01985v2)。
- J. Mayle, T. Wang, *On the effective version of Serre's open image theorem*, Bull. LMS **56** (2024), 1399–1416，Theorems 1、5，Lemmas 7、15：[期刊全文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.13002)。有效 Chebotarev 的常数为 $4,2.5,5$；未优化其表格常数。
- J.-H. Ahn, S.-H. Kwon, *An explicit upper bound for the least prime ideal in the Chebotarev density theorem*, Ann. Inst. Fourier **69** (2019), 1411–1458，Theorem 1.1：[期刊原文](https://www.numdam.org/item/10.5802/aif.3274.pdf)。
- 仓库 [R1](R1-exact-remaining-image.md)、[R5](R5-quadratic-self-twist-and-inertness.md)、[R41](R41-two-and-p-power-division-field-independence.md)、[R7](R7-simultaneous-local-frobenius-approximation.md)。
- 完整分支及失败路线：[研究笔记](../notes/2026-11-12-small-surjective-prime-resume2.md)；截至本次会话的文献边界：[文献核验](../notes/2026-11-12-literature-resume2.md)。
