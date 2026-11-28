# R1190：原实际子簇的一个 $p$ Néron 格界与形式盘运输

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 在原 $X_1$ 的同一个 Jacobian $J$ 上，对全部 $p>37$、$p\equiv5\pmod6$，每个实际有理阿贝尔子簇 $i:B\hookrightarrow J$ 的 Néron Lie 格满足

$$
\boxed{\qquad
p\Lambda_{\rm sat}\subset di(\Lambda_B)\subset\Lambda_{\rm sat},
\qquad
\Lambda_{\rm sat}=\operatorname{Lie}(B)(\mathbf Q_p)\cap\Lambda_J.
\qquad}
\tag{1190.1}
$$

这里通过实际 $di$ 识别 Lie 子空间，$\Lambda_J,\Lambda_B$ 均是各自完整 Néron 模型在 $\mathbf Z_p$ 上的 Lie 格。这个界不依赖 $\dim B$、所选商的同源次数或 R1187 的大高度界。它把 [R1188 §8](R1188-original-torsion-grid-models-and-balanced-Lie-form.md) 在原 level 素数处的 $d\Lambda_{\rm sat}\subset di(\Lambda_B)$ 改进为一个 $p$。

此外，对每个整数 $a\ge1$，有真正形式点的包含

$$
\boxed{\qquad
i\bigl(B(\mathbf Q_p)\bigr)\cap
\mathscr J^{a+1}(\mathbf Z_p)
\subset i\bigl(\mathscr B^a(\mathbf Z_p)\bigr),
\qquad}
\tag{1190.2}
$$

其中 $\mathscr A^a(\mathbf Z_p)=\ker(\mathscr A(\mathbf Z_p)\to\mathscr A(\mathbf Z_p/p^a))$。因而原点差或 Abel 像若在环境 $J$ 中达到深度 $a+1$，并且确实属于原 $B$，则它在 $B$ 的实际形式群中至少达到深度 $a$。

本篇不宣称 $di(\Lambda_B)=\Lambda_{\rm sat}$，也不将本原泛函升级为指定 CM jet 的单位。最终首项比较给的是至多一个 $p$ 的**格损失**，不是首项自身的估值界。无数学程序执行。

## 1. 同一个原对象及同一个 tame 半稳定扩域

沿用 [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)、[R1184](R1184-original-uniform-cubic-CM-disc-and-Neron-integrality.md)、[R1189](R1189-original-CM-formal-multiple-and-ramified-norm-descent.md) 的原对象

$$
X=X_1=\operatorname{Norm}
\bigl(X_{\rm ns}^+(p)\times_j\mathbf P^1_b\bigr),
\quad j=6912b^3(1-b^3),\quad J=J_X,
$$
$$
D_0=(3-N)[c_1-c_0],\qquad N=1+\delta+\delta^2.
\tag{1190.3}
$$

本篇不更换 $c_0,c_1$、$D_0$ 或半秩 Mordell–Weil 方向。所需半稳定扩域是已经在这些原模型上支付的

$$
K_0=\widehat{\mathbf Q_p^{\rm ur}},\quad
R_0=W(\overline{\mathbf F}_p),\quad
e_0=\frac{p^2-1}{2},
$$
$$
L=K_0(\pi_0),\qquad \pi_0^{e_0}=p,
\qquad R=R_0[\pi_0].
\tag{1190.4}
$$

由于 $p\nmid e_0$ 且 $R_0$ 含全部 $e_0$ 次单位根，$L/K_0$ 是实际 tame Galois 扩张，群记为 $G$。

R1018 的 compact-type 行与 R1038 的双中心 Raynaud 行，已经分别给出 $J_L$ 的良好或半稳定约化。这里只消费其共同结论：$J_L$ 半稳定。阿贝尔子簇与商保持半稳定约化，所以任一实际 $B\subset J$ 的 $B_L$ 也半稳定；这一步可直接使用 BLR §7.4 Lemma 2，印刷 p.182。

用 $\mathscr J_R,\mathscr B_R$ 表示 $L$ 上的 Néron 模型，用 $\mathscr J_0,\mathscr B_0$ 表示 $K_0$ 上的 Néron 模型。分歧基变映射不被当成同构。唯一使用的函子性是：$i$ 延拓为两端相应 Néron 模型的同态，并保持单位截面。

## 2. 半稳定形式群的有限平坦核及其真实余切模

先固定一个在 $R$ 上半稳定的阿贝尔簇 $A/L$，令 $\mathscr A/R$ 为其 Néron 模型、$\widehat{\mathscr A}$ 为单位处形式群。记

$$
\omega_A=e^*\Omega^1_{\mathscr A/R},\qquad
\Lambda_{A,R}=\operatorname{Hom}_R(\omega_A,R).
\tag{1190.5}
$$

这两个模均为秩 $\dim A$ 的自由 $R$-模。

### 引理 1190.1（真正有限层）

对每个 $n\ge1$，单位形式群的 $p^n$ 核由一个有限平坦、交换、$p$ 幂阶的 $R$-群方案 $A_n$ 表示；它与 $n$ 的自然包含及乘 $p$ 映射相容。并且有函子性的等式

$$
\boxed{\qquad
\omega_{A_n}=\omega_A/p^n\omega_A.
\qquad}
\tag{1190.6}
$$

**证明。** 在单位分量 $\mathscr A^0$ 上，半稳定性使每个 $[p^n]$ 为 quasi-finite flat 态射，见 BLR §7.3 Lemma 2(a)。所以其核 $H_n$ 为 separated、quasi-finite、flat 群方案。因为 $R$ henselian，$H_n$ 的 finite part 是有限、开且闭的子群，包含整个特殊纤维；这是 BLR 印刷 p.179 紧接该引理后的 finite-part 构造。

再取这个有限群方案中，其特殊纤维为单位连通分量的开闭部分。有限 $R$-代数的幂等元在 henselian 底上唯一提升，故该部分存在。它是子群：乘法与逆在特殊纤维保持单位连通分量，而有限源中一个非空开闭部分不能有空特殊纤维。它又是有限平坦群方案的开闭部分，因而有限平坦，记为 $A_n$。其通向 $\mathscr A$ 的像在特殊纤维上支撑于单位点，故它恰是 $\widehat{\mathscr A}$ 的 $p^n$ 核。自然包含和乘 $p$ 映射都由原形式群给出，故相容。

在单位形式参数 $T_1,\ldots,T_d$ 中，$[p^n]$ 的线性项为 $p^n(T_1,\ldots,T_d)$。计算单位处增广理想模平方，只留下这些线性关系，得到

$$
\omega_{A_n}
=\frac{(T_1,\ldots,T_d)}
{(T_1,\ldots,T_d)^2+([p^n]_1(T),\ldots,[p^n]_d(T))}
\simeq (R/p^nR)^d.
\tag{1190.7}
$$

该同构正是 $\omega_A\to\omega_{A_n}$ 的规范商映射，因而不依赖参数选择，并与群同态相容。这里没有把有限层的 $\omega_{A_n}$ 当成自由 Lie 格。证毕。

此处的有限平坦性使用了**原半稳定性**。它不是任意光滑形式群的 $p^n$ 核均有限平坦的断言；例如加法形式群不能如此处理。

## 3. Vasiu–Zink 在原分歧指数上只损失一个 $p$

采用 Adrian Vasiu、Thomas Zink，*Boundedness results for finite flat group schemes over discrete valuation rings of mixed characteristic*，J. Number Theory 132 (2012), 2003–2019，Theorem 1。

其所需形式是：对有限平坦交换 $p$ 幂阶群方案之间的同态 $f:G_1\to G_2$，若泛纤维是同构，则存在 $g:G_2\to G_1$，使 $gf=[p^s]$、$fg=[p^s]$；$s$ 仅依赖底 DVR。对 $p\nmid e$、$e\ge p-1$，同文 Example 2 给出可取

$$
s=\left\lfloor\log_p\frac{pe}{p-1}\right\rfloor.
\tag{1190.8}
$$

在 (1190.4) 中，

$$
\frac{pe_0}{p-1}=\frac{p(p+1)}2,
\qquad p\le\frac{p(p+1)}2<p^2.
$$

因此这一个已经固定的原底环 $R$ 可取

$$
\boxed{s=1.}
\tag{1190.9}
$$

以下始终只用这个有限平坦群方案定理；不从某个有限层的 $g$ 推出全形式群的准逆。

## 4. 从 finite schematic image 到整余切格

对实际包含 $i:B\hookrightarrow J$，取引理 1190.1 的 $B_n,J_n$。其限制 $i_n:B_n\to J_n$ 定义良好。令

$$
I_n=\operatorname{Im}_{\rm sch}(B_n\to J_n),
\qquad B_n\xrightarrow{f_n}I_n\hookrightarrow J_n.
\tag{1190.10}
$$

$I_n$ 是有限平坦交换群方案。具体地，其坐标环是有限自由 $R$-代数 $\mathcal O(B_n)$ 中的像子代数，故是有限且无 $R$-挠的模；DVR 上有限无挠即平坦。原群态射的 schematic image 保持群结构。

由于泛纤维 $i$ 是一个真正闭嵌入，$f_{n,L}$ 为同构。$I_n$ 的阶为 $p$ 幂，因此 Vasiu–Zink 给出

$$
g_n:I_n\longrightarrow B_n,
\qquad g_nf_n=[p]_{B_n},\quad f_ng_n=[p]_{I_n}.
\tag{1190.11}
$$

对余切模取逆像，第一式给

$$
f_n^*g_n^*=p\,\operatorname{id}_{\omega_{B_n}},
\qquad
p\omega_{B_n}\subset\operatorname{im}(f_n^*).
\tag{1190.12}
$$

另一方面，$I_n\hookrightarrow J_n$ 是闭嵌入，所以单位处余切模映射 $\omega_{J_n}\twoheadrightarrow\omega_{I_n}$ 满射。结合 (1190.6)，得到

$$
p\omega_{B,R}
\subset i^*\omega_{J,R}+p^n\omega_{B,R}
\qquad(n\ge1).
\tag{1190.13}
$$

注意：这里无需 $\omega_{I_n}$ 自由，也不要求各个 $g_n$ 彼此相容。

令 $M=\omega_{B,R}/i^*\omega_{J,R}$。它是有限生成 $R$-模，而 (1190.13) 给 $pM\subset p^nM$ 对所有 $n$ 成立。由 $p$ 进分离性 $\bigcap_n p^nM=0$，可得

$$
\boxed{\qquad p\omega_{B,R}\subset i^*\omega_{J,R}.\qquad}
\tag{1190.14}
$$

这是从全部有限层得到的实际自由余切格结论，未使用未经构造的形式准逆。

## 5. Smith 对偶与 tame 固定点下降

### 5.1 在 $R$ 上取整 Lie 对偶

泛纤维上 $i^*$ 满射。对自由 $R$-模之间的映射 $i^*: \omega_{J,R}\to\omega_{B,R}$ 取 Smith 基，可写为

$$
\operatorname{diag}(\pi_0^{a_1},\ldots,\pi_0^{a_d})
\quad\text{及额外零列},\qquad a_j\ge0.
$$

由 (1190.14) 和 $p=\pi_0^{e_0}$，有 $a_j\le e_0$。对偶的 $di$ 在对应坐标中也是这组对角元，故

$$
p\bigl(\operatorname{Lie}(B)(L)\cap\Lambda_{J,R}\bigr)
\subset di(\Lambda_{B,R})
\subset\operatorname{Lie}(B)(L)\cap\Lambda_{J,R}.
\tag{1190.15}
$$

分歧底上各 $a_j$ 可以位于 $0$ 与 $e_0$ 之间；本篇不将它们提前称为 $0$ 或 $1$。

### 5.2 固定同一个有理切向量，下降不再损失 $p$

Edixhoven，*Néron models and tame ramification*，Theorem 4.2，给出实际 Néron 模型等同

$$
\mathscr A_0
\simeq
\bigl(\operatorname{Res}_{R/R_0}\mathscr A_R\bigr)^G
\qquad(A=B,J).
\tag{1190.16}
$$

在单位处取双数点即得到

$$
\Lambda_{A,0}=(\Lambda_{A,R})^G,
\tag{1190.17}
$$

其中右端先将 $R$-模视为 $R_0$-模，并保原 semilinear Galois 作用。这个等式不是 $\Lambda_{A,0}\otimes R=\Lambda_{A,R}$ 的断言。

现在取

$$
x\in\operatorname{Lie}(B)(K_0)\cap\Lambda_{J,0}.
$$

实际 Néron 基变映射把 $x$ 送入 (1190.15) 的中间环境。于是存在 $y\in\Lambda_{B,R}$ 满足 $di(y)=px$。因为泛纤维 $di$ 单射，这个 $y$ 唯一；$x$ 与 $i$ 均在 $K_0$ 上定义，故 $gy=y$ 对所有 $g\in G$ 成立。由 (1190.17)，$y\in\Lambda_{B,0}$。因此

$$
p\bigl(\operatorname{Lie}(B)(K_0)\cap\Lambda_{J,0}\bigr)
\subset di(\Lambda_{B,0}).
\tag{1190.18}
$$

整个下降没有取一个再乘以扩张度的 trace；使用的是同一切向量的唯一原像及 tame 固定模型。

最后，Néron 模型与未分歧扩张及其完备化相容，见 BLR §7.2 Theorem 1(ii)、Corollary 2。$R_0/\mathbf Z_p$ 忠实平坦。对原 $x\in\Lambda_{\rm sat}$，(1190.18) 的唯一泛纤维原像本来就在 $\operatorname{Lie}(B)(\mathbf Q_p)$；它属于 $\Lambda_B\otimes R_0$ 当且仅当它属于 $\Lambda_B$。所以 (1190.18) 精确下降为 (1190.1)。证毕。

作为直接推论，$\Lambda_{\rm sat}/di(\Lambda_B)$ 是一个至多 $\dim B$ 维的 $\mathbf F_p$-空间；特别

$$
[\Lambda_{\rm sat}:di(\Lambda_B)]\le p^{\dim B}.
\tag{1190.19}
$$

这也精确给出：在 $\mathbf Z_p$ 上所有 Smith 指数只能为 $0$ 或 $1$。

## 6. 真正形式点的统一一个深度运输

为支付 (1190.2)，先记录一个纯整形式群事实。对 $p>2$ 的任意光滑交换 $\mathbf Z_p$-群，在单位形式参数中，其整不变微分给形式对数

$$
\log(T)=T+\sum_{r\ge2}\frac{P_r(T)}r,
\qquad P_r\in\mathbf Z_p[T_1,\ldots,T_d]^d
\text{ 为 }r\text{ 次齐次式}.
\tag{1190.20}
$$

它可由沿径向积分闭不变微分直接得到。对 $T\in p^a\mathbf Z_p^d$、$a\ge1$，第 $r$ 项估值至少 $ar-v_p(r)$，且对两输入之差，非线性部分的 Lipschitz 增益至少

$$
(r-1)a-v_p(r)\ge1\qquad(r\ge2).
$$

因此 $\log-\operatorname{id}$ 为严格压缩，逐次求逆在相同球内收敛。这证明实际双射

$$
\log_A:\mathscr A^a(\mathbf Z_p)
\xrightarrow{\ \sim\ }p^a\Lambda_A
\qquad(a\ge1).
\tag{1190.21}
$$

此双射只涉及 Néron 单位形式 chart，不省略 Fuchs–Pham 的特定射影指数 chart 成本。

若 $b\in B(\mathbf Q_p)$ 且 $i(b)\in\mathscr J^{a+1}(\mathbf Z_p)$，则

$$
x=\log_J(i(b))\in
p^{a+1}\Lambda_J\cap\operatorname{Lie}(B)(\mathbf Q_p)
=p^{a+1}\Lambda_{\rm sat}.
\tag{1190.22}
$$

这里 $x$ 属于 $\operatorname{Lie}(B)$ 也可不预用全局对数：取商 $J\to J/B$，其形式对数与群映射相容，而 $i(b)$ 的商为零，所以 $x$ 在该 Lie 映射的核中。

由 (1190.1)，$x\in di(p^a\Lambda_B)$。令 $b_0$ 为 (1190.21) 给出的唯一 $\mathscr B^a$ 点，其对数送到 $x$。$i(b_0)$ 与 $i(b)$ 均属于 $\mathscr J^1$，且对数相等；(1190.21) 的单射性迫使两者相等。实际 $i$ 是闭嵌入，故 $b=b_0$，证明 (1190.2)。

特别，在原 ambient Jacobian 中的形式深度 $2$ 已足以进入原 $B$ 的形式深度 $1$；不需要按 $\deg\iota$ 或 $\deg\rho$ 再乘一个巨大整数。该结论只适用于已经属于 $B$ 的点，不能将任意 $J$ 点未经投影当作 $B$ 点。

## 7. 对同一原 $\beta$、交错型和首项的精确影响

应用到 R1187–R1188 的实际 $B\subset J$，沿用同一 $\beta_B$、同一 Abel 映射以及按 $t=b-1=p^3w$ 取得的实际 jet。令

$$
U(w)=\sum_{r\ge1}U_rw^r\in\operatorname{Lie}(B)(\mathbf Q_p)[[w]],
\qquad rU_r\in\Lambda_B,
\tag{1190.23}
$$

后式由原 $p^3$ chart 的 Néron 延拓支付。取 R1182、R1188 的同一非零泛函

$$
\lambda(v)=\Omega(\log_p(M\beta_B),v),
$$

并令 $a_m=\lambda(U_m)\ne0$ 为其原第一非零项。通过 $di$ 识别后，分别定义

$$
h_B=\min_{v\in\Lambda_B}v_p(\lambda(v)),
\qquad
h_{\rm sat}=\min_{v\in\Lambda_{\rm sat}}v_p(\lambda(v)).
\tag{1190.24}
$$

对格的任一整基取最小值即得这些整数；$\lambda\ne0$ 保它们有限。由 (1190.1) 两端包含，准确有

$$
\boxed{\quad h_{\rm sat}\le h_B\le h_{\rm sat}+1.\quad}
\tag{1190.25}
$$

对 R1182 的 scalar-invariant 首项余量

$$
e_B=v_p(a_m)-h_B,\qquad
e_{\rm sat}=v_p(a_m)-h_{\rm sat},
$$

因此

$$
\boxed{\quad e_{\rm sat}-1\le e_B\le e_{\rm sat}.\quad}
\tag{1190.26}
$$

这里比较的是**同一个** $\lambda$ 和 $a_m$，没有重标 $\Omega$、更换 $\beta$ 或把不同商的首项混在一起。即使 $h_{\rm sat}$ 为负，上述关系仍成立；统一缩放 $\lambda$ 不改变两个 $e$。

例如设 $\ell_p(m)=\lceil\log_p(m+1)\rceil$。R1182 §9 的真实 Néron 本原化深度为

$$
H_B=\ell_p(m)+\max\{0,e_B\}+1.
$$

用环境饱和格计算的

$$
H_{\rm sat}=\ell_p(m)+\max\{0,e_{\rm sat}\}+1
$$

满足

$$
\boxed{\quad H_{\rm sat}-1\le H_B\le H_{\rm sat}.\quad}
\tag{1190.27}
$$

所以在已知同一环境格读数后，转到实际子簇 Néron 格只产生至多一个深度的不确定性；原 $t$ 坐标的相应阈值是 $3+H_B$，其中 $3$ 正是已成 R1184 的真实尺度。若另有 $m\le p-2$，则可直接使用 R1182 的更短 $H_B=e_B+1$，相同一个深度比较仍成立。

这没有给出 $e_{\rm sat}=0$，也没有宣称原候选已到达上述阈值。原环境 $\Lambda_J$ 与有理射影模型、平衡 $F$-基之间的成本，以及指定 $a_m$ 相对本原泛函的位置，仍须分别支付。R1036–R1037 的整 MW 泛函本原性也不能替代该指定首项。

## 8. 来源、范围与后继

1. Adrian Vasiu and Thomas Zink，*Boundedness results for finite flat group schemes over discrete valuation rings of mixed characteristic*，**J. Number Theory 132 (2012), 2003–2019**，DOI [10.1016/j.jnt.2012.03.010](https://doi.org/10.1016/j.jnt.2012.03.010)。已亲读 [2012-04-13 作者 PDF](https://people.math.binghamton.edu/adrian/VZ3.pdf)：Theorem 1 为 PDF 第 2 页；Example 2 为 PDF 第 16 页，明确 $p\nmid e$ 时的 (1190.8)。本篇直接算出原 $e_0$ 给 $s=1$，只调用有限平坦群方案结论。
2. Bas Edixhoven，*Néron models and tame ramification*，**Compositio Math. 81 (1992), 291–306**。[正式 PDF](https://www.numdam.org/item/CM_1992__81_3_291_0.pdf)：Theorem 4.2 在印刷 p.296（含封面 PDF 第 7 页）。本篇从其固定模型等同逐式取双数点，保持原 semilinear 作用，而不是把 ramified base change 冒称无损。
3. Siegfried Bosch, Werner Lütkebohmert, Michel Raynaud，*Néron Models*，Springer，1990。[原书 PDF](https://www.math.stonybrook.edu/~kamenova/homepage_files/Bosch_Raynaud_Neron_Model_tc.pdf)：§7.2 Theorem 1(ii)、Corollary 2，pp.176–177；§7.3 Lemma 2(a) 及其后 finite-part 段，p.179；§7.4 Lemma 2，p.182。本篇不使用 §7.5 Theorem 4 的小分歧闭嵌入结论，因为原 $e_0$ 超过该小分歧范围。
4. R1018、R1038、R1189 只提供同一原 $J$ 在 (1190.4) 上的真实半稳定模型。R1187–R1188 只提供原实际 $B$、$\beta_B$ 和 Lie 运输；本篇对每个实际 $B\subset J$ 都成立，不依赖该选择的高度最优性。
5. [R1182 §9](R1182-original-effective-Abel-jet-valuation-and-CM-disc-radius.md)、[R1184](R1184-original-uniform-cubic-CM-disc-and-Neron-integrality.md) 提供完整尾比较与原 $p^3$ chart。本篇只替换实际子簇格运输的一项损失，不提前关闭 O4 的指定首项与 whole-disc 门。

o2_high_coefficient 已独立纸核有限余切包含、全 $n$ 闭性、Smith 对偶以及 tame 唯一原像下降；其审读不替代本文对 Vasiu–Zink 原文及 $e_0$ 的直接核对。root 亦亲读2012作者版 Theorem 1/Example 2、Edixhoven 4.2 及 BLR 两个有限部分/半稳定段。完整证明直接登记，Serre 主目标仍 OPEN，继续原指定 CM 首项与环境 Néron 格读取。
