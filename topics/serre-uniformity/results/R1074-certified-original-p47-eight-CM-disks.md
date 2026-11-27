# R1074：原 p47 的完整辅助筛选只保留八个有理 CM 圆盘

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；global_route，root 独立核读。

**已证明的固定素数结论。** 对完整原曲线
$X=X_{\rm ns}^+(47)$，任意有理点在 R1065 的原 $47$-adic regular model
上，必约化到八个有理 CM 点所占的八个 smooth 点之一。
这八个圆盘确实全部含有原有理 CM 点；其余 $227$ 个原圆盘不含有理点。
结论不附加整 $j$、小惯性、固定二次域或辅助六水平假设。

完整原 cuspidal $47$-Kummer 标签也必与相应 CM 点的全局标签相同。
另外，独立的 coarse Burnside 计数与真实标签 image 大小相合，
证明原标签图在全部 $X(\mathbf F_{283})$ 上单射；
每个有理点在 $283$ 处也必约化到同一个 CM 点。
这是同一个全局候选在原 $47$ 处和 $\ell=283$ 处的真实同点比较；
没有逐角色另选辅助点。
**圆盘内部的非 CM 有理点排除仍未完成。**
本结果不是 $X(\mathbf Q)$ 的完整点分类，也不外推全 $p$ 的 Serre 一致性。

## 1. 原数学输入与定理的准确形式

使用
[R1065](R1065-original-p-local-cusp-label-compression.md) 的原 proper regular
model $\mathcal M/\mathbf Z_{47}$。
其可由 $\mathbf Q_{47}$ 点约化到的 smooth 点为
$$
\mathcal M^{\rm sm}(\mathbf F_{47})
 =\coprod_{s\in\{0,9,10,36,44\}}\mathbf A^1_s(\mathbf F_{47}),
\qquad \#\mathcal M^{\rm sm}(\mathbf F_{47})=235.
\tag{1074.1}
$$
这里 $36=1728\bmod47$。这不是只在 $j=0$ 附近的局部输入。
原有理点的 $j$ 在 $47$ 整，且其 section 落在 (1074.1)；
所有这些模型和 extra-automorphism descent 分支已经在 R1065–R1066 付款。

令 $V=C_\Sigma[47]$ 为 R1062 的**实际** cusp 模块。
[R1072](R1072-certified-original-p47-cuspidal-disk-labels.md) 的已认证输入给：
$$
V=\bigoplus_{R\in\mathcal R}V_{\omega^R},
\qquad
\mathcal R=(26,28,30,32,34,36,38,40,42,44),
\tag{1074.2}
$$
每个实际角色均为 Bernoulli-good。
因此 R1069 的 $p$-only global localization 在全部实际 $V$ 上都是同构，
不只是对某个更小子模块成立。
在原 circular-unit 基
$\beta_\chi=e_\chi[\eta_5]$ 中，每个原圆盘有唯一全局候选
$$
\mathbf c(y)\in\mathbf F_{47}^{10}.
$$
R1072 已证明全部 $235$ 个完整向量互异；本次只消费该已成输入。

记下表中实际有理 CM 点为 $c_J$，其 $j$ 值为 $J$。
本次得到
$$
\boxed{\quad
\operatorname{red}_{47}X(\mathbf Q)
 =\{\operatorname{red}_{47}(c_J):J\in\mathcal J\},
\quad}
\tag{1074.3}
$$
其中
$$
\mathcal J=\{0,1728,-3375,8000,54000,287496,-12288000,16581375\}.
$$
这八个 reduction 彼此不同。
对任意 $x\in X(\mathbf Q)$，若其原 reduction 对应 $c_J$，则
$$
\Phi_x=\Phi_{c_J}
\quad\text{on the full actual }V,
\tag{1074.4}
$$
作为 R1067 的 $p$-only 全局 Kummer 标签。
$X$ 的 cusps 形成次数 $23$ 的原 Galois 轨道，故没有有理 cusp；
(1074.3) 因而覆盖全部有理点。

## 2. 本次新执行的来源和终态

本次执行的是新的辅助比较。
旧 R1072 输入以原 consumer 重建并核对完整 SHA-256；
不是重新打开旧结论、旧 scalar 窗口、原最低泛函或已完成的 $p=41$。

| 项目 | 本次真实回执 |
|---|---|
| execution ID | p47-ell283-original-same-point-v1 |
| 固定输入 | $p=47,\ \ell=283,\ c=5,\ \delta=5$ |
| source commit | e5d0d9d4101ca12f960db709bfe34acf17663791 |
| run / attempt | 45928658257 / 1 |
| job | 140275928914，original_same_point_sieve |
| job 及全部 steps | completed / success |
| 数学预算 / reserve | 600 秒 / 30 秒 |
| SUMMARY 时间 | 3.122853439 秒 |
| 最终预算回执 | 3.122898203000002 秒，within_budget=true |
| 算术依赖 | python-flint 0.9.0 |
| 输出状态 | complete；无 FAILED_RECEIPT |

原公开
[run](https://github.com/Rogerhu12/math-research-public/actions/runs/45928658257)
及
[job](https://github.com/Rogerhu12/math-research-public/actions/runs/45928658257/job/140275928914)
包含完整 stdout receipts。
global_route 本次独立读取 job steps、完整日志、原 request 和 source；
实际 source 与执行前逐行纸审的 candidate 内容完全一致。
没有在会话 V8、私有执行器或其它未批准环境重跑数学。

完整固定来源：

- [consumer](../scripts/original_p47_ell283_cuspidal_sieve.py)，SHA-256
  b197913a1f03750b9b2837dbfa42116faec7e45fc8bcd414faf6fbf84825c5ee；
- [method](../notes/2026-11-27-original-p47-ell283-cuspidal-sieve-method.md)，SHA-256
  cd406f755768779a484e3aa965de685d49cf6056af6be7a90e20443b5dd3572c；
- [request](../notes/original-p47-ell283-cuspidal-sieve-request.json)，SHA-256
  1871b12acdbc020ef9d6a3f15e875893f855cf9f30b1dc3116accfcc135d414a；
- 旧输入 consumer SHA-256
  35a0035d4f238670309d19c9acec35b5f9610cf13f5676f96503c59048148f98；
- 旧实际角色表 SHA-256
  880799848773da716df2dd4b5db76c07fcc0027e281baff963aff0eeeaf82014；
- 旧全部 coarse points SHA-256
  12025eb9c76692312c856360add6a4702cbe02ccaf51def477bafeaf5e06d1ee。

SOURCE_RECEIPT 还逐项核对 R9、R1062、R1064、R1069–R1073
和两 README 的完整 SHA；准确值全部保存在上述 immutable source 的 request。
规则读至 commit 051258bd5bde1fa0cc675150c325180d79cfa05e；
本次根 README SHA 为
581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102，
课题 README SHA 为
6ce1403bd2d2587bb9cca70bd0095a1264b1167fe2c4b62f0652ae671e6277a5。

## 3. 辅助端的完整覆盖及真正同点方程

[R1073](R1073-original-split-auxiliary-cuspidal-sieve.md) 已支付所有原函数、
全部 phase、fixed-root 运输和 cusp 来源。本次按其 exact 方法执行。

### 3.1 全部模型与全部 fixed necklaces

枚举所有 $j\in\mathbf F_{283}$。
一般 $j$ 保一个 quadratic representative；
$j=0$ 保六个 sextic twists；
$j=1728$ 保两个 quartic twists。
这是 $289$ 个模型表示，不能将此数直接叫原曲线点数。
对每个模型实际点计数求 Frobenius trace $a_\ell$。

$\ell<p^2/4$ 排除原 Frobenius 模 $p$ 为 scalar：
若 $\pi\equiv[a]\bmod p$，取 $|a|\le p/2$ 的整数代表。
$\pi-[a]\ne0$，因为其 degree $\ell$ 不是平方；
而
$$
0<\deg(\pi-[a])\le(\sqrt\ell+|a|)^2<p^2,
$$
与 $p$ 整除该 endomorphism 所迫 degree 至少 $p^2$ 矛盾。
这里 $\det(\pi)\equiv283\equiv1\bmod47$，且 $-1$ 在 $\mathbf F_{47}$ 非平方，所以不存在 split projective involution。其余非标量 split 元素无 fixed nonsplit necklace；
非标量 unipotent 也不能落在阶素于 $p$ 的 normalizer。
所以只有 characteristic polynomial 在 $\mathbf F_{47}$ 不可约的模型有贡献。

对这些模型，取实际非零 $P\in E[47]$ 和 $Q_0=\pi P$。
先把完整群阶中的全部 $47$ 因子从 cofactor 删去，
再从非零 Sylow 点逐次乘 $47$ 取得 $P$。
不可约性给 $(P,Q_0)$ 真为 basis，实际 Frobenius matrix 是
$$
A=\begin{pmatrix}0&-1\\1&a_\ell\end{pmatrix},
\qquad \det A=1.
$$
其 order $f$ 整除 $48$，故在实际 $\mathbf F_{283^f}$ 上求点即足够。
代码核真实 characteristic equation、$47P=47Q_0=0$、
normalized Miller pairing 非退化及其倍点相容性。

遍历全部
$$
J=\begin{pmatrix}a&b\\d&-a\end{pmatrix},\qquad
a^2+bd=5,\qquad J\sim-J,\qquad AJA^{-1}=\pm J.
$$
非零 trace 给一条，trace zero 给 $25$ 条。
实际 Cartan basis 是 $(P,JP)$，Weil root 是
$\zeta_J=\zeta_{\rm nat}^{\,d}$，不是独立另选的根。

### 3.2 原半点乘积与 fixed-root 标签

全部 $1104$ 个 native 半点都保留。
每个 Frobenius half-orbit 只真评价一次 $\psi_5$，然后使用其**实际半轨道长度**
乘所有 Frobenius 共轭得到 $W_O\in\mathbf F_{283}^{\times}$。
不把 ambient field norm 中的额外 $f/|O|$ 次幂混进来。
特别 trace zero 的 full order 为四、half-orbit 长度为二。

用原坐标
$$
v_1=w/d,\qquad v_0=u-aw/d
$$
按 $[v_0^2-5v_1^2]\in\mathbf F_{47}^{\times}/\{\pm1\}$ 分组。
每组严格核为 $48$ 个半点，所有原 orbit multiplicities 均保留。
得到 $23$ 个真正 base-field 产品 $S_h$。

在真实 $\zeta_J$ 下，R1073 给
$$
D_\chi(J)=-\kappa_\chi^{-1}
 \sum_{h\in\mathbf F_{47}^{\times}/\pm}
 h^{-R}\operatorname{KLog}_{\zeta_J}(S_h),
\quad
\kappa_\chi=5^2-5^{2R},
$$
其中 $\operatorname{KLog}_{\zeta}(z)$ 由 $z^6=\zeta^k$ 定义。
指数六来自 $(283-1)/47$，没有改用大域的 Kummer 指数。

固定最小 primitive root $\zeta_0=4$，写 $\zeta_J=\zeta_0^\alpha$。
逐点真实计算
$$
D_\chi^0=\alpha^{1-R}D_\chi(J),\qquad
\alpha^{1-R}B_\chi(\zeta_J)=B_\chi(\zeta_0).
$$
因此每个**同一个**原辅助点给一个完整十维标签 $\mathbf D^0$。
每个原 global 候选 $\mathbf C$ 仅在
$$
\bigl(C_\chi B_\chi(\zeta_0)\bigr)_{\chi\in\mathcal R}
       =\mathbf D^0
\tag{1074.5}
$$
整行成立时保留。不存在逐角色换点、换 necklace 或换相位的步骤。

### 3.3 全部 cusps 与实际零坐标 mask

原全部 $23$ 个 rational cusps 也逐一加入。
同一个 cusp $h$ 的所有角色使用 R1073 的同一行：
$$
D_{\chi,h}^{\rm cusp}
 =\frac{23\,\chi(h)\chi(-5)^{-1}}{\chi(5)^2-1}
   B_{\chi^2}(\zeta_0).
$$
即使 $\chi^2$ 不属于实际 $V$，仍实际计算这里的 circle projection，
不能直接删去。每个 $B_\chi=0$ 的坐标仍须要求 $D_\chi=0$；
算法本身没有除掉可能为零的局部单位读数。

本次真实 AUX_CIRCLE 给
$$
\bigl(B_{\omega^R}(\zeta_0)\bigr)_{R\in\mathcal R}
  =(14,25,19,38,4,35,34,39,32,14),\qquad
{\rm zero\_roles}=\varnothing.
\tag{1074.6}
$$
所以在这个固定辅助素处，十个原 global 坐标全可见且比较矩阵可逆。

## 4. 完整结果、CM 定位和 compact receipts

本次 SUMMARY 的全部覆盖计数是：

| 完成项 | 数量 |
|---|---:|
| 原输入圆盘 / 互异完整 global 候选 | 235 / 235 |
| auxiliary 模型表示 | 289 |
| 有贡献 / 无贡献模型表示 | 118 / 171 |
| affine necklace 表示 | 286 |
| cusp 表示 | 23 |
| 互异 fixed-root 完整辅助标签 | 279 |
| 保留的原 global 候选 | 8 |

这些表示数本身不是原曲线点数。
每个有贡献模型的全部 fixed necklaces 都完成；
所有 cusps 都完成；没有预算截断或未处理尾项。

准确 survivor 表如下。ID 和 $t_*$ 使用 R1072 被 SHA 钉住的原顺序；
所有存活项的 twist 标号均为零。
这不表示可以在枚举时删掉另一种 $j=1728$ twist。

| 原 ID | $s=j\bmod47$ | 原 $t_*$ | 有理 CM $j=J$ | CM 阶判别式 |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | $-3$ |
| 76 | 9 | 29 | $-3375$ | $-7$ |
| 77 | 9 | 30 | $-12288000$ | $-27$ |
| 100 | 10 | 6 | $16581375$ | $-28$ |
| 108 | 10 | 14 | $8000$ | $-8$ |
| 141 | 36 | 0 | $1728$ | $-4$ |
| 196 | 44 | 8 | $287496$ | $-16$ |
| 220 | 44 | 32 | $54000$ | $-12$ |

八项并非依数值相似性命名。
R1071 §17 已从经典 CM 表、原 CM Cartan 与 first-lift Hasse 梯度给出来源。
其余六个非特殊 $J$ 使用实际
$$
A_J=\frac{3J}{1728-J},\qquad B_J=\frac{2J}{1728-J}\pmod {47^2}
$$
，并读取
$$
t_{*,J}=\mathscr H_{47,A}\frac{A_J-A_s}{47}
       +\mathscr H_{47,B}\frac{B_J-B_s}{47}\pmod {47}.
$$
随后以 $(A_J,B_J)\bmod47^2$ 自身为新 marked first lift，
独立重建原完整 profile 的 constant vector；
所有六项都与旧参考下的 $\mathbf c_s(t_{*,J})$ 同时在十个角色相符。

真实 CERTIFIED_INPUT 的梯度及 first-lift 核验为：

| $J$ | $(A_J,B_J)\bmod47^2$ | $(\mathscr H_A,\mathscr H_B)\bmod47$ |
|---:|---:|---:|
| $-3375$ | $(1646,361)$ | $(43,4)$ |
| $8000$ | $(1281,854)$ | $(12,35)$ |
| $54000$ | $(289,929)$ | $(12,35)$ |
| $287496$ | $(7,741)$ | $(12,35)$ |
| $-12288000$ | $(2163,1442)$ | $(43,4)$ |
| $16581375$ | $(1187,55)$ | $(12,35)$ |

两个特殊中心使用原已认证的 $t_*=0$。
六个 auxiliary $j=0$ sextic twists 全给同一个 fixed-root 标签并保留 ID 0。
两个 $j=1728$ twists 各保完整 $25$ 条 necklace 表示；
各自有 $14$ 个不同标签，均只匹配 ID 141。
这些是来源和相位控制，不替代其它模型及 cusps 的枚举。

最终记录：

| 数据 | SHA-256 |
|---|---|
| 排序后的八项 compact survivors | 6a1c2261bd27b3c69d3bf1438ce6e41dd2877bcc41f1c724b656fd4adc701382 |
| 排序后的完整 canonical auxiliary tag 集合 | 2b643e58e8ae9e7127655363db56388b367208ef67bb0b24ceef113567ea519c |
| runner scratch 完整 payload（97227 bytes） | b260a30677f0a303821a71b48d40953fc2ce971a75b59313b89ca9c8b06b5105 |

原始 torsion/orbit 明细和全数组只留 runner scratch；
没有上传 artifact、Release 或提交可重算 raw arrays。
本文核读完整公开日志与 pinned source，没有声称下载过不存在的 artifact。
SUMMARY 明确
all_known_cm_labels_survive=true、
all_survivors_are_identified_known_cm_labels=true、
rational_point_classification_claimed=false。

## 5. 为什么这给原有理点的圆盘排除

取任意 $x\in X(\mathbf Q)$。
R1065 给唯一的原 smooth reduction $y_{47}$；
R1072 的完整 profile 给其唯一 global 候选 $\mathbf c(y_{47})$。
R1067 保证这个全局标签只支撑 $47$；
R1069 在本次全部实际角色上保证 global-to-local 同构，
所以没有未付的类群自由度。

$X$ 在 $283$ 好约化，故 $x$ 有一个实际 reduction
$y_{283}\in X(\mathbf F_{283})$，允许它原先落在 cusp 上。
R1073 的完整规范函数和良好模型保证其标签准确满足 (1074.5)。
§3 覆盖了所有 affine 与 cusp 可能，§4 的真实 complete 执行只留下八个候选。
因此 $y_{47}$ 只能是表中八项之一。

R1072 的 $235$ 个完整向量互异，故此处不是仅把标签缩到八项，
而是把实际原 smooth 圆盘缩到八个。
R1071 §17 的独立 CM first-lift 比较说明这八项正是相应 $c_J$ 的原圆盘。
每个 $c_J$ 本来就是有理点，所以 (1074.3) 是等式。
global localization 的单射性进一步给完整 (1074.4)。

## 6. CM 范围和准确 j 同余

### 6.1 八项穷尽有理 CM locus 的逐项证明

经典十三项有理 CM 表已在 R9 §1 保存；
其已发表来源为 Silverman, *Advanced Topics* (1994), Appendix A §3，
同表也见
[Zywina 作者全文 §1.9 Table 1](https://pi.math.cornell.edu/~zywina/papers/PossibleImages/PossibleImages.pdf)。
这里只使用其明示转引的经典表。

不能把 R9 的 $p>163$ 总定理未经检查套到 $47$。
但该表全部模型的坏素都不含 $47$，其 CM orders 的判别式也都与 $47$ 互素，
所以 R9 §§2–3 的证明可逐项在 $47$ 实施：
惰性时惯性是完整 nonsplit Cartan，结合 coarse 自同构轨道长度至多三，
迫唯一的有理 CM Cartan 点；分裂时普通惯性含 projective order
大于二的 split 元素，不能稳定这样的原 coarse Cartan 轨道。

表中八项的 underlying fields 是 $-3,-4,-7,-8$，均在 $47$ 惰性。
其余五项的 fields 是 $-11,-19,-43,-67,-163$，均在 $47$ 分裂：
$$
\left(\frac{47}{11}\right)=\left(\frac3{11}\right)=1,\quad
\left(\frac{47}{19}\right)=\left(\frac9{19}\right)=1,\quad
\left(\frac{47}{43}\right)=\left(\frac4{43}\right)=1,
$$
$$
\left(\frac{47}{67}\right)=-\left(\frac{20}{47}\right)=1,\qquad
\left(\frac{47}{163}\right)=-\left(\frac{22}{47}\right)=1.
$$
后两式用 $(2/47)=1$、$(5/47)=-1$、$(11/47)=-1$。
所以本表确实穷尽 $X(\mathbf Q)_{\rm CM}$。
这句话只分类 CM locus，绝不把 (1074.3) 升格为全部有理点分类。

### 6.2 由同一个原圆盘得到的 47-adic 同余

对 $J\ne0,1728$，在该实际 CM 点附近采用其 marked reference，
原 $j-J$ 是 good deformation 参数 $u_{\rm base}$ 乘单位。
R1066 的实际 blowup 参数是 $t=u_{\rm base}/47$，
与原 $t_*$ 只差保留的整可逆 affine 运输。
因此同一原 smooth 圆盘迫
$$
j(x)\equiv J\pmod {47^2}.
\tag{1074.7}
$$

在两个特殊 CM 点，R1066 §4.3 给
$$
j-J=u_{\rm base}^{e_s}\cdot{\rm unit},\qquad
T=(u_{\rm base}/47)^{e_s},\qquad e_s=3\text{ 或 }2.
$$
同一**coarse**中心圆盘意味着 $T\in47\mathbf Z_{47}$，故
$$
J=0:\quad v_{47}(j(x))\ge4,\qquad
J=1728:\quad v_{47}(j(x)-1728)\ge3.
\tag{1074.8}
$$
不能从 coarse 条件擅自写 $u_{\rm base}/47\in47\mathbf Z_{47}$：
这些圆盘内部可能需要 ramified fine lift。
所以本文不把 (1074.8) 夸大成六阶或四阶同余。
采用 $v_{47}(0)=+\infty$，原 CM 点本身也满足这些式子。

综上，全部原有理 $j$ 在 $47$ 整，并且
$$
j(x)\in47^4\mathbf Z_{47}\ \cup\
 (1728+47^3\mathbf Z_{47})\ \cup\
 \bigcup_{J\in\mathcal J\setminus\{0,1728\}}
       (J+47^2\mathbf Z_{47}).
\tag{1074.9}
$$

## 7. 独立 Burnside 点数付款与整个辅助标签图的单射

本节不将 §4 的表示数直接叫点数。
先对原 coarse fibers 作独立的 twisted Burnside 计算，
然后才与已经认证的标签 image 大小比较。

对固定 $j$，设
$$
A_E=\operatorname{Aut}_{\overline{\mathbf F}_{283}}(E)/\{\pm1\},
\qquad \mathscr N=\{\text{原 nonsplit necklaces}\}.
$$
Frobenius 归一化 $A_E$，且原 coarse fiber 是 $A_E\backslash\mathscr N$。
有限集合的 twisted Burnside 恒等式是
$$
\#(A_E\backslash\mathscr N)^{\rm Frob}
 =\frac1{|A_E|}\sum_{a\in A_E}\#\operatorname{Fix}(a\,{\rm Frob}).
\tag{1074.10}
$$
其证明可逐 stable orbit 核定：
对任意该 orbit，所有点与所有满足 $a\,{\rm Frob}(s)=s$ 的 $a$
的配对总数恰为 $|A_E|$；非 stable orbit 贡献零。
所以不要求每个 rational coarse 点已经有某个预选模型上的 fixed necklace。

一般 $j$ 有 $A_E=1$。
quadratic twist 只将 $\pi$ 换成 $-\pi$，不改变 necklace，
故选定一个 representative 的每行都恰给一个原点。
本次这些行数为 $286-6-50=230$。

对 $j=0$，$A_E=C_3$，且 $283\equiv1\bmod3$。
三个 $a\pi$ 在实际 ordinary CM 二次域中，范数均为 $283$。
该 CM 域在 $47$ 惰性，所以它们模 $47$ 位于 nonsplit Cartan。
§3.1 排除 scalar。
它们的实际 trace 也不为零：否则其二次域将为
$\mathbf Q(\sqrt{-283})$，不可能等于 $\mathbf Q(\sqrt{-3})$。
Hasse 界 $|a_{283}|\le33<47$ 排除 trace 非零却模 $47$ 为零。
因此三个项各有唯一 fixed necklace。
(1074.10) 给原 $j=0$ fiber 恰为一个点；
代码中的六个 sextic-twist 行是它的重复表示。

对 $j=1728$，$A_E=C_2$。
因 $283\equiv3\bmod4$，原 supersingular Frobenius 满足
$\pi^2=[-283]$、$\pi i=-i\pi$。
故 $\pi$ 和 $i\pi$ 都是 trace zero、norm $283$；
其模 $47$ 行列式为一，且为 nonsplit projective involution。
R1073 的原 fixed-count 给每项 $25$ 条 necklace，
所以 (1074.10) 给这个 coarse fiber 恰为 $25$ 个点。
两种 quartic-twist 模型中的 $50$ 行覆盖它们，不能叫 $50$ 个点。

最后全部 $23$ 个 cusps 在 $\mathbf F_{283}$ 上有理，且与 affine fibers 不交。
由此严格得到
$$
\boxed{\quad
\#X(\mathbf F_{283})=230+1+25+23=279.
\quad}
\tag{1074.11}
$$
这个点数来自原 coarse 轨道证明及真实枚举，不是从 tag 数反推。

R1073 §9 的 fixed-root 运输使完整辅助标签
$$
\Psi_{283}:X(\mathbf F_{283})\longrightarrow\mathbf F_{47}^{10}
$$
对原 coarse 点良定义，包含 cusps 的 regularized 值，
并且本次枚举覆盖了其全部 image。
§4 的 complete receipt 独立给 $\#\operatorname{im}\Psi_{283}=279$。
结合 (1074.11)，得到
$$
\boxed{\quad \Psi_{283}\text{ 在全部 }X(\mathbf F_{283})\text{ 上单射。}\quad}
\tag{1074.12}
$$

若 $x\in X(\mathbf Q)$ 在 (1074.3) 中对应 $c_J$，
则 (1074.4) 与原标签的良好约化相容性给
$\Psi_{283}(\operatorname{red}_{283}x)
 =\Psi_{283}(\operatorname{red}_{283}c_J)$。
所以 (1074.12) 迫两个原辅助点相同。
CM 点的 $j$ 整，其约化不是 cusp，故 $x$ 也不约化到 cusp；
从原 $j$ morphism 得
$$
\boxed{\quad
j(x)\in\mathbf Z_{283},\qquad j(x)\equiv J\pmod {283}.
\quad}
\tag{1074.13}
$$
(1074.7)–(1074.9) 和 (1074.13) 使用同一个 $J$，
不能分别选择两个不同 CM 点。
这是两个指定素处的真实原点识别及同余，
仍不是无限深圆盘上的解析消去方程。

## 8. 已排除的范围与真正剩余问题

本次新计算完整排除了 $227$ 个原 smooth $47$-adic 圆盘，
并将完整全局 cusp 标签限为八个实际 CM 标签。
不依赖旧有 gap 的全 $p\le97$ 分类，也不把有限域 ordinary/CM 名称
替换成有理点结论。

尚未证明任一剩余圆盘只含它的 CM 有理点。
同一个 cuspidal Kummer 标签在一整个原 $p$-adic 圆盘上恒定，
所以继续重复同一层标签，不能自动取得盘内精度。
R1057 的指定原 $X_1,c_1$ 深盘唯一性也不能未经实际 source 运输
推广为本篇全部 $X_{\rm ns}^+(47)$ 的八个圆盘。

全 $p$ 的共同辅助像排除同样仍开放；
本文固定 $p=47,\ell=283$，没有把本次 finite-field 成功外推成统一定理。


## 9. 整个原 CM 圆盘上的 j 单射与坏 47 高度

本节是纸面后继，不执行新的数学程序。
它使用 §5 已经认证的八个**原**圆盘，而不将 Kummer 标签的局部恒定性
误当成盘内解析消去。先支付实际 $j$ morphism 的全圆盘精度，
再给原非对角 Cartan 对应的支撑和 Néron 配对；
最后说明与既成 R43 的准确关系。

### 9.1 全部 Cp 点上的实际解析同构

令 $\mathcal U_J\subset X(\mathbf C_{47})$ 为原正则模型中
$\overline{c_J}$ 的 tube。这里包括需要 ramified fine lift 的点。
若 $J\ne0,1728$，令 $e_J=1$；若 $J=0$ 或 $1728$，
分别令 $e_J=3$ 或 $2$。

存在该 **coarse** tube 的整参数 $z$，$z(c_J)=0$，以及
$a_J\in\mathbf Z_{47}^{\rm ur,\times}$、整收敛函数 $R_J$，满足
$$
\frac{j-J}{47^{e_J}}=a_Jz+47R_J(z),
\qquad R_J(0)=0.
\tag{1074.14}
$$
参数及等式可在原点的实际下降环中读取；
写不分歧扩张只是为了统一证明，不增加点或删掉 twist。

关键是 (1074.14) 在整个完成局部环中成立，
不是只在 $\mathbf F_{47}$ 值上成立。
对六个非特殊 $J$，R1066 §4.2 的真实 invariant blowup chart 给
$$
u/47=ct+47R(t),\qquad c\text{ 为单位},\quad R\text{ 整}.
$$
这里的正 $47$-赋值来自精确 Kummer invariance：
原 $\tau^{48}=47$ chart 中的正 $\tau$-赋值误差已经下降到
不分歧 invariant 环，因而确实被 $47$ 整除。
R1066 的 full-level source 次数控制已支付所有高项。
在实际 CM lift $t=t_J$ 处平移，得
$(u-u(t_J))/47=(t-t_J)(c+47R_1)$。
这六个 $J$ 的约化都不是 $0$ 或 $1728$，所以 good fine deformation 上
$j-J$ 是 $u-u(t_J)$ 的整单位倍；再复合其整展开便给 (1074.14)。

对两个特殊中心，使用 R1066 §4.3 的真实 $\mu_{e_J}$ eigenparameter。
写
$$
T=t^{e_J},\qquad u/47=tV(T),\qquad
V(T)\equiv c\pmod {47},
$$
其中 $V$ 是整单位。原 coarse morphism 满足
$$
j-J=u^{e_J}W(u^{e_J}),\qquad W(0)\text{ 为单位}.
$$
因此
$$
\frac{j-J}{47^{e_J}}
 =T\,V(T)^{e_J}
    W\!\left(47^{e_J}T\,V(T)^{e_J}\right)
 =a_JT+47R_J(T).
\tag{1074.15}
$$
这里 $T$ 才是原 coarse 参数；没有要求 $t\in\mathbf Q_{47}$，
也没有从 $T\in47\mathbf Z_{47}$ 错推 $t\in47\mathbf Z_{47}$。

对任意 $z_1,z_2$ 满足 $|z_i|_{47}<1$，
整幂级数的差商
$(R_J(z_1)-R_J(z_2))/(z_1-z_2)$ 仍整，故
$$
\left|
 \frac{j(z_1)-j(z_2)}{47^{e_J}}
\right|_{47}
=|z_1-z_2|_{47}.
\tag{1074.16}
$$
导数同样是单位。整形式逆函数定理于是给
$$
\boxed{\quad
j:\mathcal U_J\xrightarrow{\ \sim\ }
 \{\,J+47^{e_J}w:\ |w|_{47}<1\,\}.
\quad}
\tag{1074.17}
$$
这是整个 $\mathbf C_{47}$ tube 上的解析同构，且处处 étale。
它加强了 §6 的同余，但本身不限制圆盘中有理点的数量。

### 9.2 原 j-preserving 非对角对应的所有支撑避让

令 $Z$ 是原 $X$ 上若干非恒等 Cartan double-coset correspondences 的
整数组合；每个几何支都改变 Cartan，而保持 underlying elliptic curve，
所以保持原 $j$。要求这些支不含 diagonal component。
这从实际 moduli 描述也可直接核：一般 elliptic curve 的
$\operatorname{Aut}/\{\pm1\}$ 平凡，非恒等 double coset 给不同的 Cartan。

在任意 $x\in\mathcal U_J$ 处，§9.1 已证明 $j$ étale。
因此 $X\times_{\mathbf P^1_j}X$ 在 $(x,x)$ 附近的 diagonal 是开闭支；
一个全局非对角几何不可约支若经过 $(x,x)$，
就在该邻域包含 diagonal 的非空开，从而本身是 diagonal，矛盾。
所以没有这样的支固定 tube 中的点。

这也支付两个特殊点的原 moduli 接口：
在 tube 内若 $j=0$ 或 $1728$，(1074.17) 迫该点就是 $c_J$。
其 Cartan 是 **canonical CM Cartan**，全部 CM units 都正规化它，
故其实际 Cartan 的 automorphism orbit 是 singleton。
非恒等 double-coset 支不能借 coarse 自同构把另一个 Cartan 重新认成该点。

现在取任意 $x,y\in\mathcal U_J$。
若一个支将 $x$ 连到 tube 内的点 $x'$，则 $j(x')=j(x)$，
由单射性得 $x'=x$，又与上述无 fixed point 矛盾。
因此，连同所有几何共轭支，
$$
\operatorname{Supp}(\operatorname{Fix}Z)\cap\mathcal U_J
=\operatorname{Supp}(Z(x))\cap\mathcal U_J
=\operatorname{Supp}(Z(y))\cap\mathcal U_J
=\varnothing.
\tag{1074.18}
$$
虚系数只可能消去支撑，不影响此结论。
$\operatorname{Fix}Z$ 是真正的有限交点 cycle；
这里没有把含 diagonal 的 Hecke 算子硬当成有限 fixed divisor。

### 9.3 真实 raw divisor 的坏 47 Néron 配对

进一步假设 $Z$ 对称且在 $H^0(X,\Omega^1)$ 上 trace 为零。
设 $d=\deg Z(x)$。对称性及 Lefschetz 交数公式给
$$
\deg\operatorname{Fix}Z=2d-2\operatorname{Tr}
       (Z\mid H^0(X,\Omega^1))=2d.
$$
以下取共同有限扩张 $L/\mathbf Q_{47}$ 上的 $x,y\in\mathcal U_J\cap X(L)$；
实际应用中两点均在 $\mathbf Q_{47}$ 上。于是
$
P=x-y,\qquad D=\operatorname{Fix}Z-Z(x)-Z(y)
\tag{1074.19}
$$
都是次数零的真实 divisors，且由 (1074.18) 支撑互不相交。

在原正则模型上，$x$ 与 $y$ 的 sections 通过同一个 smooth 特殊点。
它们与每个垂直不可约分量的交数相同，故 $P$ 的 admissible vertical
correction 可以取零；其仅差一个全纤维的歧义不改变与次数零 $D$ 的配对。
另一方面，(1074.18) 说明 $D$ 的全部几何支撑都不在这个 tube，
所以其闭包避开该特殊点，水平交数也为零。

若先作有限扩张使各支撑有理，smooth chart 的基变换仍光滑，
同一论证保持成立；再用交数的 projection formula 降回去。
由此对任意 coefficient prime $\ell\ne47$ 及相应非 $\ell$ 处的
Néron 高度规范，
$$
\boxed{\quad
h_{47}\bigl(x-y,\operatorname{Fix}Z-Z(x)-Z(y)\bigr)=0.
\quad}
\tag{1074.20}
$$
这一步不需要整个 Jacobian 潜在好约化，也不需要特殊纤维的图是一棵树。
所用非 coefficient-prime 高度等于垂直修正后的交数，
是 R43 §§1、4 已核的已发表 Néron/Poincaré 比较。

### 9.4 旧 R43 对八个实际圆盘的应用及余下输入

[R43](R43-neron-height-from-integral-correction.md) §4 Theorem 4
已经对其实际对称 trace-zero 对应 $F$、规范双扩张截面及基点 $b$ 证明
$$
h^{\rm Nek}_{F,47,b}(x)
 =\frac{k_i(F)-k_{i_b}(F)}{2d^2}\log_\ell47.
$$
因此 §5 的实际圆盘结论立即给
$$
h^{\rm Nek}_{F,47,b}(x)
 =h^{\rm Nek}_{F,47,b}(c_J),
\qquad
h^{\rm Nek}_{F,47,c_J}(x)=0.
\tag{1074.21}
$$
这里保留同一个 $J$。若使用一个固定全局基点 $b$，
应说两个值相等，不能把所有圆盘的值都擅自设为零。
这个应用不需要小 Hecke 次数条件，也不需要 $\operatorname{rank}J=g$；
它没有重新声称一个新的通用局部高度定理。

(1074.18)–(1074.20) 另外支付了原 off-diagonal Cartan cycle 的
**raw 支撑**和直接交数，用于需要此精确 divisor 而不只是
规范 QC 局部函数的后继论证。
仍须另外取得原完整 level-$2209$ Fricke-plus Jacobian 的实际秩、
辅助素处整 Hecke / Mordell–Weil 格、全局高度及盘内首项。
R45 的非零 Heegner 商并不等于整个 Jacobian；
旧 $X_1,c_1$ 的结果也没有在这里被换成全 $X$。
所以 (1074.17)、(1074.20) 和 (1074.21) 均未把八个圆盘内的有理点唯一性
当成已经完成。

本节由 global_route 逐式纸证；o1_theta 独核全整 chart、特殊 coarse
参数与 canonical-Cartan 支撑，o2_high_coefficient 独核垂直及水平交数、
有限扩张和 degree-zero 范围。没有运行新的数学计算。
