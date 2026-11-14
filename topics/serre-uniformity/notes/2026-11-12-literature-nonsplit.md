# 非分裂 Cartan 文献核查与局部实现

日期：2026-11-12（Asia/Taipei）。会话：serre-uniformity-astra / literature。

状态：文献范围核查；第 5 节是基于标准已发表定理的完整局部计算。没有证明 Serre 一致性，也没有构造全局反例。

## 1. 已发表或已接受的主干结论

以下的 $N_{\mathrm{ns}}(p)=C_{\mathrm{ns}}^+(p)$ 表示**完整正规化子**。

| 来源 | 精确位置和范围 | 对本题的意义 |
| --- | --- | --- |
| Serre, *Quelques applications du théorème de densité de Chebotarev*, Publ. Math. IHÉS **54** (1981), 323–401 | §8.4, Lemme 18：$p>13$ 排除例外投影像；定理编号由下列已接受论文 Introduction 交叉核查 | 不处理非分裂正规化子 |
| Mazur, *Rational isogenies of prime degree*, Invent. Math. **44** (1978), 129–162 | 无 CM 的 $\mathbb Q$ 曲线的有理素数度同源只可能为 $2,3,5,7,11,13,17,37$ | $p>37$ 排除 Borel |
| Bilu–Parent–Rebolledo, *Rational points on $X_0^+(p^r)$*, Ann. Inst. Fourier **63** (2013), 957–984 | Corollary 1.2：$p\ge11$, $p\ne13$ 排除分裂正规化子；$p=13$ 由 Balakrishnan–Dogra–Müller–Tuitman–Vonk (2019) 处理 | $p>37$ 的分裂情形已结束 |
| Le Fourn–Lemos, *Residual Galois representations of elliptic curves with image contained in the normaliser of a nonsplit Cartan*, Algebra Number Theory **15** (2021), no. 3, 747–771, DOI 10.2140/ant.2021.15.747 | Theorem 1.2：无 CM $E/\mathbb Q$，若 $p>1.4\cdot10^7$，或者 $p\notin\{2,3,5,7,11,13,17,37\}$ 且 $j(E)\notin\mathbb Z$，则非满射像必为完整 $N_{\mathrm{ns}}(p)$ | 不能把第二项读成“非整 $j$ 已满射”，也不能推出完整正规化子上的 $j$ 整性 |
| Furio–Lombardo, *Serre's uniformity question and proper subgroups of $C_{ns}^+(p)$* | arXiv:2305.17780v2，2025-11-25，页面标注 final version, to appear in Algebra & Number Theory；Theorem 1.5：$p>37$ 时像为 $\mathrm{GL}_2(\mathbb F_p)$ 或完整 $N_{\mathrm{ns}}(p)$。Theorem 1.6：指数 3 子群 $G(p)$ 在 $p>5$ 均不出现 | 本题真正剩下的是完整 $N_{\mathrm{ns}}(p)$ |

核查页面：

- [Furio–Lombardo v2 原文](https://arxiv.org/html/2305.17780v2)，Introduction, Theorems 1.2、1.3、1.5、1.6；其 Theorem 1.2 回顾 Zywina 的分类，并说明完整证明已在 Le Fourn–Lemos Proposition 1.4 和 Appendix B 发表。
- [Le Fourn–Lemos 原文](https://arxiv.org/pdf/2002.02714)，Theorem 1.2、Proposition 1.4、Appendix B。
- [2026 年已发表 Furio–Lombardo 7-adic 论文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.70193)，Introduction 同样陈述问题尚未解决。

在 $p\equiv2\pmod3$ 时，指数 3 群可写成
$$
G(p)=C_{\mathrm{ns}}(p)^3\rtimes\langle s\rangle,
\qquad s(x)=x^p\quad(x\in\mathbb F_{p^2}).
$$
已知的 $G(p)$ 排除不能重命名为对 $N_{\mathrm{ns}}(p)$ 的排除。二者所对应曲线、尖点轨道和 Jacobian 商都不同。

## 2. 2026 年的新进展不改变剩余主目标

### 2.1 $p$-进像分类

Bisatt–Furio–Lombardo, *Explicit $p$-adic Hodge theory for elliptic curves and non-split Cartan images*, [arXiv:2603.04021v2](https://arxiv.org/html/2603.04021v2)，2026-06-08，预印本。

Theorem 1.1 (=9.1) 给出：无 CM $E/\mathbb Q$、$p>7$、$\operatorname{Im}\bar\rho_{E,p}\subseteq N_{\mathrm{ns}}(p)$ 时，存在 $n\ge1$ 满足
$$
\operatorname{Im}\rho_{E,p^\infty}
=\pi_n^{-1}\bigl(N_{\mathrm{ns}}(p^n)\bigr).
$$
Theorem 1.2 的 adelic 指数上界为
$$
[\mathrm{GL}_2(\widehat{\mathbb Z}):\operatorname{Im}\rho_E]
\ll_\varepsilon\max\{1,h(j(E))\}^{2+\varepsilon}.
$$
Remark 9.2 明确指出：全局的 $n$ 不能由纯 $p$-进论证给出界。这些结论分类并限制仍可能出现的像，未排除它们；上界仍依赖 $E$ 的高度。此处只记录预印本内容，不把其中新结果作为仓库已证明结论的无条件前提。

### 2.2 无方程二次 Chabauty

Hashimoto–Lido–Lombardo–Mascot–Parent, *Equationless quadratic Chabauty for non-split Cartan modular curves*, [arXiv:2608.10919](https://arxiv.org/abs/2608.10919)，2026-08-11，预印本。

Theorem 1.0.1 重得 $X_{\mathrm{ns}}^+(13)(\mathbb Q)$ 为七个已知 CM 点。一般方法直接使用模解释和除子运算，而不先求射影方程；Theorem 4.4.6 含 $\operatorname{rank}J(\mathbb Q)=g$ 等假设，Remark 3.0.7 讨论秩条件。它提供逐曲线求有理点的工具，未证明存在对所有素数统一适用的排除界；Introduction 仍把统一界列为问题。

### 2.3 最小满射素数与最大例外素数不同

Genao–Mayle–Rouse, *A uniform bound on the smallest surjective prime of an elliptic curve*, Ramanujan J. **70**, article 22 (2026)，[正式论文](https://link.springer.com/article/10.1007/s11139-026-01376-8)，2026-05-12。

Theorem 2：无 CM 的 $E/\mathbb Q$ 至少有一个 $\ell\le7$ 使 $\ell$-进表示满射；除列出的六个 $j$ 外可取 $\ell\le5$。该结果的量词是“存在一个小满射素数”，并不控制“大素数是否例外”。Introduction 明确将最大例外素数的一致有界性留为开放问题。

## 3. 一处必须避免继承的文献缺口

Furio–Lombardo v2 在 Introduction 的 Claim 1.4 后说明：Bajolet–Bilu–Matschke 关于 $p\le100$ 非分裂 Cartan 曲线整 $j$ 有理点的计算性论证似有缺口，具体指向 Furio 博士论文 Remark 5.3.10。因此不能沿用旧论文综述把这段全范围计算视作已核证。这里记录的是后续作者对该论证的明确异议，不声称我们已逐行重审原计算。

## 4. 真正剩余的两种障碍

**整性不是现有的普遍前提。** Le Fourn–Lemos 的整性论证针对严格子群对应的曲线。其 Remark 1.6 说明完整 $N_{\mathrm{ns}}(p)$ 对应的 Jacobian 面临不同障碍：在 BSD 下不存在非零有限 Mordell–Weil 群商，因此不能直接照搬 Mazur 的秩零商形式浸入论证。

**局部条件只给限制。** Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Trans. AMS **371** (2019), 137–146，[原文](https://arxiv.org/pdf/1702.01985)，Proposition 2.2：$p\ge5$ 且全局像包含于 $N_{\mathrm{ns}}(p)$，则所有 $\ell\not\equiv\pm1\pmod p$ 都是潜在好约化处；特别 $p$ 本身是潜在好约化处。证明使用 Tate 表示及每个正规化子元素的平方落入 Cartan。该定理不声称 $\ell\equiv\pm1$ 的分母素数不存在。

以下计算说明：即使是 $p$ 处的完整局部正规化子像，也可以由无 CM 的有理曲线在任意大 $p$ 上实现。

## 5. 一个完整局部实现计算

### 命题 L1

对任意素数 $p>37$ 且 $p\equiv2\pmod3$，曲线
$$
E_p:\quad y^2=x^3+p x+1
$$
无复乘，并且
$$
\bar\rho_{E_p,p}\bigl(G_{\mathbb Q_p}\bigr)
\text{ 共轭于 }N_{\mathrm{ns}}(p).
$$
这里结论只关于局部 Galois 群 $G_{\mathbb Q_p}$，没有断言 $\bar\rho_{E_p,p}(G_{\mathbb Q})$ 也是此群。

### 证明

1. 判别式和 $j$ 为
$$
\Delta(E_p)=-16(4p^3+27),\qquad
j(E_p)=\frac{6912p^3}{4p^3+27}.
$$
因 $p>3$，$p\nmid\Delta(E_p)$，所以给出的整数模型在 $p$ 处有好约化。

2. $4p^3+27$ 与 $p$ 互素，且 $4p^3+27>6912$。若 $j(E_p)$ 是整数，分母必须整除 $6912p^3$，于是必须整除 $6912$，矛盾。因此 $j(E_p)\notin\mathbb Z$。CM 曲线的 $j$ 是代数整数，故有理非整 $j$ 排除 CM。（这是经典奇异模整性；可见 Cox, *Primes of the Form $x^2+ny^2$*, Theorem 11.1 及 Proposition 13.2。）

3. 在 $p$ 处的约化为 $\widetilde E_p:y^2=x^3+1$。由于 $p\equiv2\pmod3$，$x\mapsto x^3$ 是 $\mathbb F_p$ 的双射。记 $\chi$ 为二次特征并令 $\chi(0)=0$，则
$$
\#\widetilde E_p(\mathbb F_p)
=p+1+\sum_{x\in\mathbb F_p}\chi(x^3+1)
=p+1+\sum_{u\in\mathbb F_p}\chi(u+1)
=p+1.
$$
故 $a_p=0$，约化超奇异。也可直接用 Hasse 不变量判据：$(x^3+1)^{(p-1)/2}$ 只含次数为 $3$ 倍数的项，而 $p-1\not\equiv0\pmod3$，故其 $x^{p-1}$ 系数为零。

4. 应用 Serre 的标准惯性定理：*Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. **15** (1972), §1.11, Proposition 12，印刷页 275。[作者机构提供的原文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)。其假设是局部基域绝对分歧指数 $e=1$ 且好超奇异约化；对 $\mathbb Q_p$ 成立。结论 (b),(c) 给出
$$
E_p[p]\simeq\mathbb F_{p^2},\qquad
\bar\rho_{E_p,p}(I_p)=\mathbb F_{p^2}^{\times}=C_{\mathrm{ns}}(p),
$$
惯性通过满射的二级基本特征作用。Serre 的结论 (d) 直接给出：因残域 $\mathbb F_p$ 不含 $\mathbb F_{p^2}$，局部总像为完整正规化子。

这最后一步亦可展开：惯性正规，故局部总像正规化完整 $C_{\mathrm{ns}}(p)$；算术 Frobenius 对 tame inertia 的共轭为 $p$ 次幂，因而它对 $\mathbb F_{p^2}^{\times}$ 的共轭非平凡。于是局部总像包含 $C_{\mathrm{ns}}(p)$ 和一个外陪集元素，等于 $N_{\mathrm{ns}}(p)$。$\square$

### 推论和逻辑边界

$p\equiv2\pmod3$ 的素数无穷多：若只有有限个，取它们乘积 $P$，则 $3P-1\equiv2\pmod3$ 有一个不在原集合中的 $2\pmod3$ 素因子。因此命题给出任意大的局部实现。

所以，“对足够大的 $p$，无 CM 的有理曲线不能在 $p$ 处出现完整非分裂正规化子像”是一个错误的中间命题。要证明主目标，必须使用超出这项局部条件的全局信息。这个反例只针对错误的中间命题，不是 Serre 一致性的反例。

### 命题 L2：上述简单族实际上全局满射

在命题 L1 的同样假设下，
$$
\bar\rho_{E_p,p}(G_{\mathbb Q})=\mathrm{GL}_2(\mathbb F_p).
$$
此证明不使用 Furio–Lombardo 的分类。

**证明。** 令 $D=4p^3+27$。它是大于 $1$、与 $6p$ 互素的整数，并且 $D<2^p$。最后的不等式可从整数 $n=17$ 的情形起归纳：
$$
\frac{4(n+1)^3+27}{4n^3+27}
<\left(\frac{n+1}{n}\right)^3
\le\left(\frac{18}{17}\right)^3<2.
$$
取任意素因子 $\ell\mid D$，则 $\ell\ge5$、$\ell\ne p$，且
$$
0<m:=v_\ell(D)<p.
$$
在 $\ell$ 处，给定模型的 $c_4=-48p$ 为单位，而 $v_\ell(\Delta)=m>0$；所以它已极小并有乘法约化。经过至多二次**非分歧**扩张后成为 Tate 曲线，参数 $t$ 满足 $v_\ell(t)=m$。该非分歧扭曲不改变惯性作用。

Tate 描述 $E[p]$ 由 $\mu_p$ 和 $t^{1/p}$ 给出。在最大非分歧扩张中，$\mu_p$ 已存在，单位的 $p$ 次根也存在（$p\ne\ell$，用 Hensel 引理）。因 $p\nmid m$，添加 $t^{1/p}$ 得到分歧次数 $p$ 的扩张。因此全局像 $H$ 包含非平凡 transvection $u$，即某一基下的
$$
u=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad a\ne0.
$$
命题 L1 给出 $H\supseteq C_{\mathrm{ns}}(p)$。记 $L$ 为 $u$ 的固定直线。完整非分裂 Cartan 在二维空间上不可约，所以有 $c\in C_{\mathrm{ns}}(p)$ 使 $cL\ne L$。于是 $v=cuc^{-1}\in H$ 为固定另一条直线的 transvection。在分别来自 $L,cL$ 的基下，
$$
u=\begin{pmatrix}1&a'\\0&1\end{pmatrix},\qquad
v=\begin{pmatrix}1&0\\b'&1\end{pmatrix},\qquad a'b'\ne0.
$$
因基域是素域 $\mathbb F_p$，对 $u,v$ 取整数幂便得到全部上、下初等幺幂矩阵。它们通过二维 Gaussian 消元生成 $\mathrm{SL}_2(\mathbb F_p)$，所以 $H\supseteq\mathrm{SL}_2(\mathbb F_p)$。而 $C_{\mathrm{ns}}(p)\simeq\mathbb F_{p^2}^{\times}$ 的行列式是满射的范数 $\mathbb F_{p^2}^{\times}\to\mathbb F_p^{\times}$，故 $\det H=\mathbb F_p^{\times}$。从而 $H=\mathrm{GL}_2(\mathbb F_p)$。$\square$

这说明在同一条显式无 CM 有理曲线上，$p$ 处的局部像可以是完整非分裂正规化子，而全局像是完整一般线性群。真正排除全局正规化子，须把不同处的约束放在**同一个全局基**下相容地使用。

### 命题 L3：同时满足分母处局部条件的全局满射子族

此处沿用根代理构造并给出一个额外 Frobenius 证据。设 $p$ 是满足 $p\equiv41\pmod{60}$ 的素数，$q$ 是任意满足 $q\equiv1\pmod{5p}$ 的素数。令
$$
D=1728q^p-p^{3p},\qquad
E_{p,q}:\quad y^2=x^3+\frac{3p^p}{D}x+\frac2D.
$$
则 $E_{p,q}$ 无 CM、$p$ 处局部模 $p$ 像为完整 $N_{\mathrm{ns}}(p)$、唯一潜在乘法素数 $q$ 处局部模 $p$ 像包含于标量群 $\{\pm I\}$，但全局模 $p$ 像为 $\mathrm{GL}_2(\mathbb F_p)$。

**证明。** $D\ne0$，且直接计算得
$$
j(E_{p,q})=\frac{p^{3p}}{q^p},\qquad
\Delta(E_{p,q})=-\frac{2^{12}3^6q^p}{D^3}.
$$
$j$ 非整数，故无 CM；其唯一负赋值处为 $q$。$p\nmid D$，并且模型在 $p$ 处的 $A$ 系数赋值为 $p>0$、$B$ 系数为单位、判别式为单位，所以有好约化，约化具有 $j=0$。因 $p\equiv2\pmod3$，与 L1 同样的立方双射计数给出超奇异性，Serre Proposition 12 给出局部满正规化子。

在 $q$ 处有潜在乘法约化。记其对应的 Tate 参数为 $t$；$j$ 级数的形式反演给出
$$
t=j^{-1}(1+O(j^{-1}))
=\left(\frac q{p^3}\right)^p u,
\qquad u\in1+q^p\mathbb Z_q.
$$
由于 $p\ne q$，$p$ 次幂在 $1+q\mathbb Z_q$ 上是双射，故 $t\in\mathbb Q_q^{\times p}$。同时 $q\equiv1\pmod p$ 使 $\mu_p\subset\mathbb Q_q$。因此对应 Tate 曲线的 $p$ 扭点在 $\mathbb Q_q$ 上全有理；原曲线相差至多一个二次扭曲，局部像为标量 $\{\pm I\}$ 的子群。

关键的额外全局证据来自 $5$：$p\equiv q\equiv1\pmod5$，且 $p\equiv1\pmod4$，所以
$$
D\equiv2\pmod5,\quad
\widetilde E_{p,q}:y^2=x^3+4x+1\quad\text{over }\mathbb F_5.
$$
判别式模 $5$ 为 $2$，故这里好约化。把 $x=0,1,2,3,4$ 代入右端，分别得到 $1,1,2,0,1$；点数为 $8$，因此 $a_5=-2$。故 $\operatorname{Frob}_5$ 的模 $p$ 特征多项式是
$$
T^2+2T+5,
$$
判别式 $-16$。因 $p\equiv1\pmod4$，它有两个不同的 $\mathbb F_p$ 根，迹又非零。这与属于任何非分裂 Cartan 正规化子不相容：Cartan 内非标量元素的特征多项式不可约，外陪集元素的迹全为零。

最后说明全局像必满，而不仅是不在此正规化子中。设全局像为 $H$，它包含 $p$ 处的完整非分裂 Cartan，故不可约、行列式满，并且投影像含阶 $p+1$ 的元素。Dickson 的 $\mathrm{GL}_2(\mathbb F_p)$ 子群分类排除所有其它真子群：Borel 因不可约性排除；分裂 Cartan 正规化子因投影元素阶只有 $2$ 或 $p-1$ 的因子而排除；例外投影群 $A_4,S_4,A_5$ 的元素阶至多 $5$，也被排除；非分裂正规化子由 $\operatorname{Frob}_5$ 排除。若 $H$ 包含 $\mathrm{SL}_2$，满行列式立即给 $H=\mathrm{GL}_2$。因此结论成立。这里仅用了经典有限群分类，没有使用新的 uniformity 结论。$\square$

**参数可取得。** 对每个这样的 $p$，可以不借助素数等差数列定理来选择 $q$：取任意素因子
$$
q\mid\Phi_{5p}(5p).
$$
该整数大于 $1$，且因圆分多项式常数项为 $1$，它与 $5p$ 互素。在特征不整除 $5p$ 的有限域里，$X^{5p}-1$ 可分；其各圆分因子分割不同精确阶的根。因此 $5p\bmod q$ 的乘法阶恰为 $5p$，所以 $5p\mid q-1$。对 $p$ 而言，标准 Dirichlet 定理保证 $p\equiv41\pmod{60}$ 的素数无穷多，因 $\gcd(41,60)=1$。

例如 $p=41,q=821$ 满足全部同余条件；无需展开大整数 $D$ 就能完成上述证明。

因此，单独结合“$p$ 处满正规化子”和“所有潜在乘法处的像都已是正规化子允许的标量”，仍远不足以确定全局像。小好约化处的 Frobenius 可以排除它。

## 6. 检索结论

本次检索覆盖作者主页、原文、2026 年新预印本和正式论文；未找到公认的 Serre 一致性完整证明。这个表述是本次检索范围内的结论，不以搜索无结果替代数学证明。上述已发表/已接受分类足以把本题研究目标精确固定为：排除任意大 $p$ 下无 CM 曲线的**全局完整** $N_{\mathrm{ns}}(p)$ 像，等价地对非分裂 Cartan 模曲线的非 CM 有理点给出统一水平限制。
