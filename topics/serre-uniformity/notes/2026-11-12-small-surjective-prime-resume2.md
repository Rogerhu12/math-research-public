# 小满射素数能否给 O3 所需的首个非零惰性迹？

日期：2026-11-12（Asia/Taipei）。会话：serre-uniformity-resume2；并行 Frobenius 分支。

**状态：下述有限群、交域和检测扩张引理已证明；Chebotarev 的 GRH 推论明确为条件性；主目标未解决。** 已读根 README、本题 README、HANDOFF、open、R6、R7、R41。本笔记不自行分配 R 编号，不修改主会话的交接和索引。

主会话预留编号后，完整结论已整理为 [R52](../results/R52-small-surjective-prime-and-detection-fields.md)。六个有理 $j$ 恒等式和全部模四/三/五计数另以有理数运算、穷举矩阵独立复核，均与下述解析证明一致；验证未作为证明替代。

## 0. 结论与真正剩余参数

设 $E/\mathbb Q$ 非 CM，$p>37$ 是实际异常素数，$K$ 是完整非分裂 Cartan 正规化子的商二次域，$\epsilon$ 是其特征。R1、R5 给 $K$ 虚二次，且 $p$ 在 $K$ 中惰性，特别不分歧。

Genao–Mayle–Rouse 的小满射素数定理确实可以给出以下严格加强：

1. 对这种实际异常曲线，$2,3,5$ 中至少一个**完整进表示**满像；不必保留 $7$。
2. 可用 $m\in\{4,3,5\}$ 的射影除法域和 $K$ 构造次数至多 $240$ 的 Galois 扩张，里面有比例至少 $1/4$ 的共轭不变集合，检测 $\epsilon(q)=-1$ 且 $a_q(E)\ne0$。
3. 若模 $5$ 满像，则 $\mathbb Q(E[5])$ 与整个 $p$ 幂除法塔线性不交。这里不需固定 CM 参考曲线。
4. 为保证有效 Chebotarev 真正给出好约化素数，可再并一个二次域；总次数至多 $480$，但判别式仍依赖 $\operatorname{rad}(N_E)$。这没有得到绝对的首个检测素数上界。
5. 对 R41 的两种特殊实际族，次数可以压到 $24$；在 GRH 下得到
   $$p\le184\log\operatorname{rad}(2N_E)+192\log24+130
   <184\log\operatorname{rad}(2N_E)+741.$$
   这是有导子参数的条件性专门家族界，不是无条件统一性。

以下给完整推导，并指出哪些看似加强的条件实际不补足 O3。

## 1. 六个 GMR 例外都带有有理三同源

Genao–Mayle–Rouse [GMR], Theorem 2：每条非 CM 曲线有某个 $\ell\le7$ 的完整 $\ell$ 进满像；除六个 $j$ 外可以取 $\ell\le5$。六个例外恰为下面左列。

定义
$$j_3(t)=\frac{(t+27)(t+3)^3}{t}.$$
直接恒等式给：

| $j$ | $t$，满足 $j=j_3(t)$ |
|---|---:|
| $-2^{-3}5^2\,241^3$ | $-729/2$ |
| $-2^4 3^2\,13^3$ | $-81$ |
| $-2^{-5}5\,29^3$ | $-32$ |
| $-2^{-1}5^2$ | $-2$ |
| $2^4 3^3$ | $-9$ |
| $2^{-15}5\,211^3$ | $-729/32$ |

无需只引用模曲线参数公式：令 $u=t+27$，考虑
$$E_t:\quad y^2+xy+u^{-1}y=x^3.$$
上表中 $u\ne0,27$。该曲线的判别式为 $u^{-3}(1-27/u)\ne0$。点 $(0,0)$ 处的切线是 $y=0$，与三次曲线的交数为三，因此 $(0,0)$ 是有理三阶点。标准 Weierstrass 不变量直接算出
$$j(E_t)=\frac{u(u-24)^3}{u-27}=j_3(t).$$
上表的 $j$ 均不为 $0,1728$；具有同一有理 $j$ 的任意曲线是 $E_t$ 的二次扭曲。虽然扭曲后的三阶点未必有理，子群 $\{O,P,-P\}$ 仍为 Galois 稳定，故仍存在有理三同源。

Lemos [L], Theorem 1.1 排除了所有带非平凡有理循环同源的实际 $p>37$ 异常曲线。因此 GMR 的六个例外不可能出现，证明：
$$\boxed{\exists\ell\in\{2,3,5\}:\rho_{E,\ell^\infty}(G_{\mathbb Q})=\mathrm{GL}_2(\mathbb Z_\ell).}\tag{1.1}$$
这里保留了完整进满像。尤其不能仅凭模 $2$ 满像就假设模 $4$ 满像。

## 2. 二次域交叠可以严格处理

按 (1.1)，若 $\ell=2$，取 $m=4$；若 $\ell=3,5$，取 $m=\ell$。置
$$L_m=\mathbb Q(E[m]),\qquad G_m=\mathrm{GL}_2(\mathbb Z/m\mathbb Z).$$
这些实际像均为整个 $G_m$。定义其射影固定域
$$P_m=L_m^{Z_m},\qquad Z_m=\{aI:a\in(\mathbb Z/m\mathbb Z)^\times\}.$$
相应次数为
$$[P_4:\mathbb Q]=48,\qquad[P_3:\mathbb Q]=24,\qquad[P_5:\mathbb Q]=120.\tag{2.1}$$
“迹模 $m$ 是否为零”在乘任意可逆标量后不变，因此在射影群上是良定义的共轭不变条件。

### 2.1 奇辅助素数

对 $\ell=3,5$，任何二次特征 $G_\ell\to\{\pm1\}$ 都在 $\mathrm{SL}_2(\mathbb F_\ell)$ 上平凡：后者由初等幺幂元生成，每个非平凡生成元的阶为奇数 $\ell$。所以唯一非平凡二次特征是行列式的二次特征。Weil 配对说明其二次域为 $\mathbb Q(\sqrt{\ell^*})$，其中 $\ell^*=(-1)^{(\ell-1)/2}\ell$。

因此：

- $\ell=3$ 时，$K\cap L_3$ 或为 $\mathbb Q$，或 $K=\mathbb Q(\sqrt{-3})$。
- $\ell=5$ 时，唯一候选二次域 $\mathbb Q(\sqrt5)$ 是实域，而 $K$ 虚，故
  $$\boxed{K\cap L_5=\mathbb Q.}\tag{2.2}$$

这些二次特征都在标量上平凡，所以若 $K\subset L_m$，已经有 $K\subset P_m$。

### 2.2 模四情形

记 $s:G_4\to\{\pm1\}$ 为模二约化 $\mathrm{GL}_2(\mathbb F_2)\simeq S_3$ 的符号特征，$d(g)=\det(g)\in\{1,3\}\simeq\{\pm1\}$。

**引理。** $G_4$ 的非平凡二次特征恰为 $s,d,sd$。

**证明。** 对任意二次特征 $\psi$，两个初等矩阵 $e_{12}(1),e_{21}(1)$ 共轭，因此 $\psi$ 在二者上的值相同。选 $e\in\{0,1\}$ 使 $\psi s^e$ 在二者上都平凡。$\mathbb Z/4\mathbb Z$ 是局部环，其 $\mathrm{SL}_2$ 由初等矩阵生成：利用某个单位矩阵项做消元，归约为对角矩阵 $\operatorname{diag}(v,v^{-1})$，后者亦为初等矩阵之积。因此 $\psi s^e$ 经行列式分解；单位群只有阶二，得所述列表。反之三个特征明显不同且非平凡。证毕。

它们全部在 $\pm I$ 上平凡。故二次域即使交叠，仍下降到 $P_4$，没有必要使用模八层。若 $K\not\subset L_4$，则 $P_4$ 与 $K$ 线性不交，联合像为直积；若 $K\subset L_4$，联合像是上述三个特征之一的图。

注意为什么不能一律只用模二：若 $K$ 恰是 $L_2$ 的判别式二次域，那么 $K$ 惰性 Frobenius 是 $S_3$ 的换位，在模二迹为零。模四层允许迹为 $2$，正好修复此处。

## 3. 检测集合的确切比例

在 $M_0=P_mK$ 中取
$$\mathcal C=\{g:\epsilon(g)=-1,\ \operatorname{tr}(g)\not\equiv0\pmod m\}.$$
此条件按上一节是良定义的共轭不变条件。下面直接计数，避免仅凭“线性不交”含糊断言有可用类。

对奇素数 $\ell$，$G_\ell$ 中迹零可逆矩阵数为 $\ell^2(\ell-1)$：迹零矩阵共 $\ell^3$ 个，其中行列式零者恰为幂零矩阵，数量 $\ell^2$。后者可按秩一幂零矩阵的共同像与核直线计数，得 $(\ell+1)(\ell-1)$ 个非零矩阵，再加零矩阵。

所以 $K$ 不交时
$$\frac{|\mathcal C|}{|\operatorname{Gal}(M_0/\mathbb Q)|}
=\frac12\left(1-\frac{\ell}{\ell^2-1}\right),$$
分别为 $5/16$（$\ell=3$）、$19/48$（$\ell=5$）。若 $\ell=3$ 且 $K=\mathbb Q(\sqrt{-3})$，需数行列式非平方且迹非零：阶为 $48$ 的群中，非平方行列式陪集有 $24$ 个元素，迹零者有 $12$ 个，故比例为 $1/4$。例如矩阵 $\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)$ 已给非零迹的实际类。

对 $G_4$，总阶为 $96$，迹非零元素有 $64$ 个。以下是完整计数：

| $K$ 的交叠情形 | $\epsilon=-1$ 且迹非零元素数／联合群阶 |
|---|---:|
| 与 $L_4$ 不交 | $64/(2\cdot96)=1/3$ |
| $\epsilon=s$ | $24/96=1/4$ |
| $\epsilon=d$ | $28/96=7/24$ |
| $\epsilon=sd$ | $28/96=7/24$ |

证明该表可不依赖程序。模二的每个可逆矩阵有 $16$ 个模四提升。两个三循环的迹为奇数，全部提升迹非零；三个换位各有八个迹为 $2$ 的提升，其中行列式 $1,3$ 各四个。恒等矩阵的提升写成 $I+2H$，其迹为 $2+2\operatorname{tr}H$，行列式为 $1+2\operatorname{tr}H$；因此迹非零的八个提升全部行列式为 $1$。逐项相加就是上表。

上述条件均不受标量影响，移到射影群不改变比例。因此
$$\boxed{[M_0:\mathbb Q]\le240,\qquad
\frac{|\mathcal C|}{|\operatorname{Gal}(M_0/\mathbb Q)|}\ge\frac14.}\tag{3.1}$$
Chebotarev 仅由此给出正密度。对好素数，非零模 $m$ 迹才进一步说明整数 $a_q(E)\ne0$；下一节会专门确保所选素数真的好。

## 4. 模五满像与整个异常 p 幂塔不交

这里给比只和商二次域不交更强的实际结论。设 $\bar\rho_{E,5}$ 满像，仍令 $p>37$ 实际异常，置 $L_{p^r}=\mathbb Q(E[p^r])$。

**命题。** 对每个 $r\ge1$，
$$\boxed{\mathbb Q(E[5])\cap L_{p^r}=\mathbb Q.}\tag{4.1}$$

**证明。** 一级群 $N=C\rtimes C_2$ 是可解群，且由 R41 §2 的直接交换子计算有
$$N^{\rm ab}\simeq\mathbb F_p^\times\times C_2.$$
所以 $L_p$ 的最大阿贝尔子域是 $\mathbb Q(\zeta_p)K$。

另一方面 $\mathrm{SL}_2(\mathbb F_5)$ 完美。可直接核实：令 $h=\operatorname{diag}(2,2^{-1})\in\mathrm{SL}_2(\mathbb F_5)$，则
$$[h,e_{12}(x)]=e_{12}((2^2-1)x).$$
因 $2^2-1=3$ 可逆，全部上初等元都在交换子群；下初等元同理，它们生成整个 $\mathrm{SL}_2$。故任何从 $\mathrm{GL}_2(\mathbb F_5)$ 到可解群的商都杀掉 $\mathrm{SL}_2$，从而经行列式分解。

交域 $J=\mathbb Q(E[5])\cap L_p$ 是两侧的 Galois 商，因此可解，且
$$J\subseteq\mathbb Q(\zeta_5)\cap\bigl(\mathbb Q(\zeta_p)K\bigr).$$
$K$ 在 $p$ 不分歧，而 $\mathbb Q(\zeta_p)$ 在 $p$ 全分歧。故后一个合成域在 $p$ 的惯性固定域恰为 $K$。$\mathbb Q(\zeta_5)$ 在 $p$ 不分歧，所以 $J\subseteq K$。唯一可能的非平凡二次子域是 $\mathbb Q(\sqrt5)$，与 $K$ 虚二次矛盾；故 $J=\mathbb Q$。

高层 $L_{p^r}/L_p$ 是 $p$ 幂次扩张。若 $J_r=\mathbb Q(E[5])\cap L_{p^r}$，由 $J_r\cap L_p=\mathbb Q$ 得 $[J_r:\mathbb Q]$ 同时整除 $480$ 与某个 $p$ 幂。因 $p>37$，二者互素，故 $J_r=\mathbb Q$。每个有限交域都出现在有限层，整个塔也不交。证毕。

本命题与 R41 的证明结构相似，但适用范围不同：它适用于任意实际异常曲线，只需模五满像；不使用 R37/R40 的二除法域判别式增长。它仍只是不交，不能变成高次 CM 同余或小 Frobenius 上界。

## 5. 有效 Chebotarev：好约化与判别式不能省略

### 5.1 排除“未分歧但坏约化”的误用

有限挠点表示在某个坏约化素数也可能不分歧。例如乘法约化处，Tate 参数的赋值被 $m$ 整除可能消掉模 $m$ 惯性像。因此“在 $M_0$ 不分歧”不足以保证是 O3 所需好素数。

令
$$R=\operatorname{rad}(30N_E),\qquad T=\mathbb Q(\sqrt R),\qquad M=M_0T.$$
$R$ 是偶平方自由整数，所以 $\operatorname{disc}(T)=4R$；每个除 $R$ 的素数都在 $T$ 分歧。故 $M$ 的每个不分歧素数均不除 $30N_E$，特别是 $E$ 的好约化素数。另一方面 R5 或 [MW] Lemma 15 给商域 $K$ 不分歧于 $N_E$ 支集外，而除法域在 $mN_E$ 支集外不分歧。因此 $M$ 只在 $R$ 的支集分歧，且
$$n=[M:\mathbb Q]\le480.\tag{5.1}$$
在 $\operatorname{Gal}(M/\mathbb Q)$ 中取 $\mathcal C$ 的逆像；它非空，共轭不变，比例仍至少 $1/4$。

### 5.2 判别式的完整参数

有限 Galois 数域 $M$ 的局部 different 估计给
$$v_q(D_M)\le n-1+n\,v_q(n).$$
可由 $q$ 处最大不分歧子扩张上一个 uniformizer 的 Eisenstein 最小多项式得到：若分歧指数为 $e$，其导数的不同次幂项的赋值模 $e$ 互不相同，故 different 指数至多 $e-1+e\,v_q(e)$；乘残数次数并汇总所有 $q$ 上方素点即得上式。参见 [MW] Lemma 7 的同一估计。

因分歧支集包含于 $R$，
$$\log D_M\le(n-1)\log R+n\log n
\le479\log R+480\log480.\tag{5.2}$$
这一步只利用支集，不依赖 Weierstrass 方程选取或其非最小判别式。它也显示：固定扩张次数没有消掉 $R$。

### 5.3 无条件和 GRH 结论

Ahn–Kwon [AK], Theorem 1.1，无条件给每个非空共轭类一个不分歧素数
$$q\le D_M^{12577}.$$
因此本构造有一个好素数满足
$$\epsilon(q)=-1,\quad a_q(E)\ne0,\quad
q\le\bigl(480^{480}R^{479}\bigr)^{12577}.\tag{5.3}$$
这只是极弱的导子依赖界，不是绝对界；也不声称是文献中最佳有效常数。

在 GRH 下，Bach–Sorenson 的有效 Chebotarev（[MW] Theorem 5；[AK] 引言亦明确重述）给
$$q\le(4\log D_M+2.5n+5)^2.$$
结合 (5.2)，
$$q\le\bigl(1916\log R+1920\log480+1205\bigr)^2.\tag{5.4}$$

这些检测素数不可能等于异常素数 $p$：若 $p\mid N_E$，已被 $T$ 排除；若 $E$ 在 $p$ 好约化，普通约化的惯性特征为 $\chi_p,1$，包含两个不同且和非零的 $\mathbb F_p$ 特征值，这与非分裂正规化子不相容。因此是好超奇异约化；对 $p>3$，$a_p(E)=0$，不属于检测集合。

故实际异常像给 $p\mid a_q(E)$，Hasse 界给 $p\le2\sqrt q$。在 GRH 下得到
$$p\le3832\log\operatorname{rad}(30N_E)+3840\log480+2410.\tag{5.5}$$

**不能将 (5.5) 记为新的最佳结果。** Mayle–Wang [MW], Theorem 1，已经在 GRH 下对所有非 CM 曲线证明更强的
$$c(E)\le964\log\operatorname{rad}(2N_E)+5760.$$
该文 Theorem 2 的非同源曲线首个不同迹素数界，应用于 $E$ 与 $E^\epsilon$，也已处理同一个检测问题。GMR 在这里提供较直接的小群证明，但本节通用数值界弱于已发表界。

## 6. R41 两种实际族中的更小扩张

现在限于 R41 的固定 CM 参考族或变量四次参考族。令 $H=\mathbb Q(E[2])$；R41 给
$$\operatorname{Gal}(H/\mathbb Q)=S_3,\qquad H\cap\mathbb Q(i)=\mathbb Q.$$
因此可以直接取
$$M_0=H\mathbb Q(i),\qquad[M_0:\mathbb Q]=12.$$
三循环且在 $\mathbb Q(i)$ 惰性的元素占 $1/6$，好 Frobenius 对应 $a_q(E)$ 奇而非零。无需 GMR，也不需整条 $p$ 除法域。

取 $R_0=\operatorname{rad}(2N_E)$、$M=M_0\mathbb Q(\sqrt{R_0})$，同样解决所有坏约化素数的排除问题。这时
$$n\le24,\qquad\log D_M\le23\log R_0+24\log24.$$
在 GRH 下，完全相同的 Chebotarev–Hasse 推导给
$$\begin{aligned}
p&\le2(4\log D_M+2.5n+5)\\
&\le184\log R_0+192\log24+130\\
&<184\log R_0+741.
\end{aligned}\tag{6.1}$$
这是一个精确的条件性专门家族推论；没有优化 Bach–Sorenson 的表格常数。它比 [MW] 对一般曲线的通用常数小，但不能据此去掉 GRH 或导子参数。

即使某些坏素数已在 $H$ 分歧，也不能未经证明删去辅助二次域：例如最小判别式赋值为偶数的乘法约化素数，二除法域可能不分歧；有限二除法 Frobenius 不能替代好约化迹。

## 7. 为什么还不能统一排除

### 7.1 既有条件允许导子继续增长

固定参考的 R13 给
$$N_E=32\prod_{r\in T}r,$$
而每个分母素数 $r$ 满足相应模 $4p$ 条件。它们给的是 $r$ 的下界和同余，并没有控制 $\sum_{r\in T}\log r$ 的上界。R24 变量参考还允许四次参数 $d$ 的素因子进入导子，未得到其统一上界。

因此 (6.1) 最多迫使
$$\log\operatorname{rad}(2N_E)\ge\frac{p-741}{184}$$
（在所声明 GRH 下）。这个指数规模的导子下界与现有约束相容。没有理由把 $\operatorname{rad}(N_E)$ 换成一个有绝对上界的量，也不能把已有高度下界反向使用。

### 7.2 R6/R7 直接阻止只靠小满像和有限窗口

R7 对任意固定 $p>37$、$p\equiv3\pmod4$ 和任意长 $X$ 构造无穷不同 $j$ 的非 CM 曲线：它们同时满足小窗口内的 CM Frobenius 数据、$p$ 处完整局部非分裂像以及唯一分母处的完整 Tate 幂条件，却全局模 $p$ 满像。

从这无穷族删去 GMR 的六个 $j$ 后，每一条仍自动具有某个 $\ell\le5$ 的完整进满像，但首个非零 $\chi_{-4}$ 惰性迹素数仍大于 $X$。所以“有小辅助满像”本身不能提供对首个检测素数的绝对界，甚至与 R7 的全部局部条件合用也不能；固定次数的检测扩张同样可以有无界判别式。

这不是实际异常族的反例。要解决 O3，仍须使用这些 R7 实例不具备的**全局模 $p$ 异常像**，证明它对变化的导子/检测域施加足够强的额外限制。目前没有得到这样的上界。

### 7.3 与 p 除法塔不交也不产生小素数

第 4 节的不交给联合有限层的直积像和独立的 Frobenius 分布；它没有将某个共轭类强迫到小于 $p^2/4$ 的区间。若把 $L_p$ 也并入检测域，域次数至少含 $2(p^2-1)$，判别式估计会变差；不能把直积的正密度当作无需判别式的 Linnik 界。

## 8. 本分支得到和未得到什么

**得到：** 六个 GMR 例外的自含三同源排除；模四/三/五中的完整二次交叠分析；次数 $240$、检测比例至少 $1/4$ 的实际射影扩张；模五满像与全部异常 $p$ 幂除法域不交；包含好约化排除的 Chebotarev 参数追踪；R41 限定族的 GRH 常数 (6.1)。

**未得到：** 对实际异常族的导子或检测域判别式统一上界；无条件 $q<p^2/4$ 的非零惰性迹素数；绝对异常素数界。通用有效导子界已有更强文献结果，本笔记不重复包装成统一性进展。

## 9. 外部已证输入与原始出处

- [GMR] T. Genao, J. Mayle, J. Rouse, *A uniform bound on the smallest surjective prime of an elliptic curve*, Ramanujan J. 70 (2026), article 22，Theorem 2：[期刊全文](https://link.springer.com/article/10.1007/s11139-026-01376-8)。只使用已发表的小满射素数定理和六个明确 $j$；三同源逐项证明在 §1。
- [L] P. Lemos, *Serre's Uniformity Conjecture for Elliptic Curves with Rational Cyclic Isogenies*, Trans. AMS 371 (2019)，Theorem 1.1：[作者稿](https://arxiv.org/html/1702.01985v2)。
- [MW] J. Mayle, T. Wang, *On the effective version of Serre's open image theorem*, Bull. LMS 56 (2024), 1399–1416，Theorems 1、2、5，Lemmas 7、15：[期刊全文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.13002)。其中 Theorem 5 引用 Bach–Sorenson 的 GRH 有效 Chebotarev；Lemma 7 是本文展开的判别式估计；Lemma 15 是商二次特征分歧支集。
- [AK] J.-H. Ahn, S.-H. Kwon, *An explicit upper bound for the least prime ideal in the Chebotarev density theorem*, Ann. Inst. Fourier 69 (2019), 1411–1458，Theorem 1.1，p. 1413：[期刊原文](https://www.numdam.org/item/10.5802/aif.3274.pdf)。使用无条件指数 $12577$；本文未下载或提交 PDF，也未渲染图片。
- E. Bach, J. Sorenson, *Explicit bounds for primes in residue classes*, Math. Comp. 65 (1996), 1717–1735，Theorems 3.1、3.2、5.1 与 Corollary 3.3。本文所用形式已在 [MW] Theorem 5 和 [AK] p. 1412 完整重述；未声称优化其数值常数。
- 仓库内部：R1（实际完整像）、R5（商域虚二次且 $p$ 惰性）、R6/R7（有限窗口障碍）、R13/R24（实际导子参数）、R41（两种限定族的二除法域不交）。
