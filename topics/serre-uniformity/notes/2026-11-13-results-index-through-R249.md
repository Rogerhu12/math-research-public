# 截至 R249 的结论索引完整记录

原主索引为达到大小限制而精简；以下保留全部原摘要，证明文件不变。

# 结论索引

主要目标尚未解决。以下结论不改变 README 的完成标准。

## 新增结论

- [R210：普通类群、自由单位模与实际二阶剩余量](../results/R210-ordinary-class-units-and-ray-residue.md)：重建Cl(L)χ≅O/43、Γ平凡及E(L)χ≅O[Γ]；45个精确系数等式证明短Robert元为普通单位。射线长度2等价于L=40、v=0、Ω₂=13ε；未计算实际L或射线长度。

- [R212：稀疏单位根与环类周期的纤维阈值](../results/R212-sparse-cyclotomic-fibre-threshold.md)：设q为角色阶的最小素因子，周期消失必有pq²≤4(q−1)M；完整证明少于q项的正单位根和非零，再接同取向嵌入球帽界。仅用于特征零标量Brandt对象。

- [R211：三点纤维对任意原始奇阶环类角色的非消失](../results/R211-odd-character-three-fibre-nonvanishing.md)：p>37、p≡2 mod3、M<3p时每个原始奇阶标量Brandt周期非零；由≤3项单位根消失及唯一三点纤维压回已证三阶情形。角色须在p不分歧，不适用于R166尖点型角色。

- [R208：由真实全局导子恢复两个椭圆粗模盘](../results/R208-elliptic-coarse-frames-from-classical-invariants.md)：从Av和Bv³的真实齐次式恢复20个阶二和1个阶三盘，全部73坐标至粗参数u³；6560个独立靶纤维等式、旧CM3二阶与Frobenius/KS全通过。
- **R214（2026-11-13，已证明）**：[偶阶transfer中心平凡与共同导子](../results/R214-transfer-center-and-common-prime-to-p-conductor.md)：全部实际角色中心平凡；p外各阶的共同导子为c*=bc，gcd(b,c)=1，b=2^eR_b、e≤3、奇部平方自由。最高2-primary阶才看见b；旧c*/c|36不能由现有前提推出。


- [R1：精确剩余像与基本群论](../results/R1-exact-remaining-image.md)：文献把 $p>37$ 的坏像缩至完整非分裂 Cartan 正规化子；给出矩阵证明以及挠点/同源定义域次数。
- [R2：Tate 局部等价判据](../results/R2-exact-tate-local-criterion.md)：负 $j$-赋值处，局部包含于非分裂正规化子等价于 $q\equiv\pm1\pmod p$ 且 Tate 参数为本域 $p$ 次幂；含单位条件和非整 $j$ 的高度下界。
- [R3：相容的局部模型](../results/R3-simultaneous-local-models.md)：显式非 CM 曲线同时满足 $p$ 处及全部潜在乘法处的局部要求；给出全局满射的无穷子族，表明这些要求不足以排除大 $p$。
- [R4：Runge 覆盖计数障碍](../results/R4-runge-cover-obstruction.md)：对完整正规化子像，任意子群覆盖及容许定义域均有尖点轨道数 $\le$ 无穷位数；最小提升域上等号成立。通常 Runge 条件不能靠这种提升恢复。
- [R5：二次自扭曲与惰性](../results/R5-quadratic-self-twist-and-inertness.md)：商特征为虚二次，$p>13$ 时 $p$ 惰性；写出残余自扭曲，并证明统一排除这类扭曲同余等价于本题主要目标。
- [R6：固定特征的 Frobenius 窗口障碍](../results/R6-fixed-character-frobenius-obstruction.md)：构造无 CM 曲线在任意长窗口与 CM 曲线同约化，且最小非零惰性迹素数相对高度的下极限至少为 $1/2$。
- [R7：同时满足局部条件与任意有限检测窗口](../results/R7-simultaneous-local-frobenius-approximation.md)：对每个 $p>37$、$p\equiv3\pmod4$ 和任意 $X\ge p$，构造全局满射的非 CM 曲线，满足 $p$ 处完整局部正规化子、唯一分母处 Tate 幂条件，并在全部奇素数 $q\le X$ 与固定 CM 曲线同约化。
- [R8：有理同源孤立性与 Hecke 邻居次数](../results/R8-rational-isogeny-isolation.md)：假想坏像曲线没有不同的有理几何同源 $j$；对任意非 CM $E/\mathbb Q$ 和 $\ell>37$，循环 $\ell$ 商的 $j$ 定义域次数恰为 $\ell+1$。
- [R9：有理 CM 点的统一约化分离](../results/R9-cm-reduction-separation.md)：$p>163$ 时有理 CM 点恰由十三个类数一判别式中 $p$ 惰性的项给出，并在每个辅助素数 $\ell\ge5$、$\ell\ne p$ 处两两分离；含特殊自同构和同域不同导子的完整处理。
- [R10：辅助素数 5 的残数圆盘计数](../results/R10-many-residue-disks-at-five.md)：$j=0$ 纤维的 $\mathbb F_5$ 点数精确为 $(p-1)/2$ 或 $(p+3)/2$；$p>163$ 时至少 $(p-19)/2$ 个相应圆盘不含有理 CM 点，仍须独立作全局排除。
- [R11：固定 CM 曲线的整 $j$ 同余刚性](../results/R11-integral-j-fixed-cm-congruence.md)：显式阈值以上，$E[p]\simeq A[p]$ 且 $j(E)$ 整强迫 $E$ 与固定 CM 曲线 $A$ 有理同源；对 $A:y^2=x^3-x$ 阈值为 $p>37$。固定 CM 同余问题因而等价于最终整性。
- [R12：无有理基点的 Poincaré 提升](../results/R12-poincare-lift-without-rational-basepoint.md)：以次数 $d>0$ 的有理除子定义 $u$，将次数零对应乘以 $d$ 并作规范有理平移，可使拉回 Poincaré 线丛在 $\mathbb Q$ 上实际平凡；尚不提供积分算法或全层 QC 排除。
- [R13：固定 CM 同余的导子与分母界](../results/R13-denominators-for-fixed-cm-congruence.md)：对 $A:y^2=x^3-x$、$p>37$ 且 $p\equiv3\pmod4$ 的实际同余，精确得到 $N_E=32\prod_{q\in T}q$、分母为 $p$ 次幂、$q\equiv\pm1\pmod{4p}$；分裂分母素数至少 $4p^2+1$。非 CM 时 $T$ 非空，仍缺全局排除。

- [R14：Poincaré 规范平移及好约化积分提升](../results/R14-canonical-poincare-translation.md)：R12 的特殊 Picard 类有显式有理 $d$ 次除根，因此保留原对应 $f$ 即可平移平凡化；好约化模型上可同时作积分平凡化，无需额外将 $f$ 乘以 $d$。仍不提供全部层的 QC 排除。

- [R15：商域分歧与立方分子](../results/R15-ramification-splitting-and-cube-numerator.md)：商虚二次域每个奇分歧素数 $q$ 都满足 $(-p/q)=1$，含 $q=3$ 野惯性；给出 $2$ 的全局互反限制。$p\equiv1\pmod3$ 时 $j=A^3/B^p$ 且 $p\nmid AB$。
- [R16：固定 CM 同余的判别式与广义 Fermat 归约](../results/R16-fixed-cm-discriminant-fermat.md)：极小判别式为 $\pm2^\delta b^p$、$\delta\in\{6,9,12\}$；完整归约到两个原始方程 $X^3-27W^2=Z^p$ 或 $8Z^p$，并给出随 $p$ 增长的 Szpiro 比下界。方程尚未统一排除。
- [R17：新增乘法素数的 Selmer 局部条件](../results/R17-local-selmer-conditions-at-new-primes.md)：固定 CM 同余中，非分裂乘法素数保持 Kummer 条件，每个分裂乘法素数改变一个维度；若全部新增素数为非分裂乘法型，两曲线的 $p$-Selmer 群在同余下相同。

- [R18：无基点范数刚性化接口](../results/R18-norm-rigidification-interface.md)：对角纤维的 $d$ 次幂除以沿有理除子 $D$ 的范数，规范等于 Poincaré 拉回；给出实际对应的次数零线丛族与好约化有限精度范数计算，无需有理基点或开 $d$ 次根。
- [R19：三个显式 Fermat 族与固定 CM 同余等价](../results/R19-converse-fermat-fixed-cm.md)：补全 R16 的反向降层证明，并将 $2$ 处极小导子 $32$ 条件化为准确的模 $4$ 表；$p>37$、$p\equiv1\pmod4$ 时三族无解，剩余指数仍待统一排除。
- [R20：精确商域与小素数单位判据](../results/R20-exact-quotient-field-and-small-unit-tests.md)：$p\equiv1\pmod4$ 时由 $j-1728$ 的既约分子与 $v_2(j)$ 精确恢复商虚二次域；任意异常 $p>37$ 下给出 $2,3$ 处单位 $j$ 的分裂与二次剩余限制。
- [R21：十二次幂惯性型及类数一 CM 扭曲归约](../results/R21-twelfth-power-signature-and-cm-twists.md)：完整证明 $\lambda^{12}|_{I_p}=\omega_2^{12}$ 或 $\omega_2^{12p}$；类数一时与 CM 特征之差的阶整除 $\gcd(12,p+1)$。$K=\mathbb Q(i)$、$p\equiv7\pmod{12}$ 得到某个有理四次 CM 扭曲，但导子仍可无界。
- [R22：好超奇异处的辛类型](../results/R22-good-supersingular-symplectic-type.md)：独立证明 $p\equiv7\pmod8$ 时局部同构只能辛，$p\equiv3\pmod8$ 时符号由约化判别式平方类决定；对固定 $A$ 的整数族，结合 R13、R25 后这些符号条件冗余。
- [R23：固定分母方程处处局部可解](../results/R23-fixed-denominator-everywhere-local-fermat.md)：每个 $p>37$ 都有无穷多素数 $q$，使 $X^3-27W^2=q^p$ 在全部完成域有原始解及与 $A[p]$ 的严格辛同构。$p\equiv1\pmod4$ 时相应光滑射影覆盖是 Hasse 原理反例；这不是 Serre 一致性反例。
- [R24：四次参数与极小判别式刚性](../results/R24-quartic-parameter-and-discriminant-rigidity.md)：$K=\mathbb Q(i)$、$p\equiv7\pmod{12}$ 的实际同余可取平方自由四次参数 $d$，得到参数方程、准确导子及分母限制；独立证明小分歧下同余保持 $p$ 处极小判别式赋值，含 $p\mid d$。
- [R25：二进惯性域筛](../results/R25-dyadic-inertia-field-filters.md)：用已发表惯性域分类把 R19 三族加强为族 I、III 奇分支的 $4\mid W$，族 II 的 $Z\equiv1\pmod4$，族 III 偶分支的 $X\equiv6\pmod8$；没有据此排除所有指数。
- [R26：固定 CM 同余的局部辛条件边界](../results/R26-local-symplectic-saturation.md)：固定 $A$ 时，除 $2,p$ 外可选择两种局部辛类型；$2,p$ 的唯一类型在现有整数条件下相容，替换为 $2$ 幂同源参考曲线不增加独立条件。
- [R27：一模十二指数下的固定商域归约](../results/R27-fixed-quotient-field-at-one-mod-twelve.md)：$p\equiv1\pmod{12}$ 时全局二次扭曲可将半稳定例外限制到 $\{2,3\}\cup\operatorname{Ram}(K)$；由 Anni–Siksek 得到有效的固定域有限 CM 归约，类数大于一的固定 $K$ 最终排除。界仍依赖 $K$。
- [R28：坏约化范数接口与显式分量群](../results/R28-bad-reduction-norm-interface.md)：在约化正则模型上完成有限平坦范数、多度数修正及单分量积分截面；推导非分裂曲线全部剩余类的交矩阵和分量类精确阶。全光滑开集粘合仍有明确的垂直系数条件。
- [R29：四次 CM 参数的辛符号相容性](../results/R29-quartic-cm-symplectic-consistency.md)：奇惰性加性素数的局部符号必须一致；$p\equiv7\pmod{24}$ 时全局只能辛，并排除指定素数的 III$^*$ 型；独立计算 $p\mid d$ 的单位符号，尚未产生统一矛盾。
- [R30：尖点平衡交数与统一乘二](../results/R30-cusp-balanced-component-correction.md)：全部尖点闭包与超奇异分量的交数为 $6/e_i$；实际规范平移族的分量障碍被 $2$ 消去，R28 的通用倍数 $p-1$ 可降为 $2$，并给精确的剩余粘合系数。
- [R31：判别式比特征与辛条件化简](../results/R31-discriminant-character-and-two-prime-obstruction.md)：四次同余的判别式比平方类是 $M=\epsilon2^\alpha B$；奇素数单位符号及全部 $p$ 处辛类型可由它统一表达。结合 R36 后，当前 $2$–$p$ 辛比较冗余。
- [R32：秩一单素数分母的统一指数窗口](../results/R32-prime-denominator-rank-one-window.md)：固定 $q,r,c$ 的 Mordell 曲线秩一时，指数 $6k+r$ 落在长度绝对有界的区间，起点取决于生成元分母深度；任意秩下均限制有理倍乘指标，未限制原始点的绝对深度。
- [R33：真实 Hecke 范数与积分障碍](../results/R33-hecke-norm-and-component-data.md)：对称对应的泛纤维范数显式抵消；小次数 Hecke 的实际多度数等于 Brandt 数且尖点范数缺陷为零。全 trace-zero Hecke 格有秩至少 $g-n$ 的子格消去垂直障碍；最终 QC 排除仍未得到。
- [R34：原始点深度与有效支撑界](../results/R34-primitive-depth-and-effective-support-bounds.md)：构造高秩曲线上任意深的原始有理点及具体例子；保留全部分母支撑后有显式高度界，并得到 R19 的有效判别式—导子不等式，常数仍随支撑增长。
- [R35：素数幂层的精确 Tate 判据](../results/R35-prime-power-tate-criterion.md)：对每个 $p^n$ 层，负 $j$ 处的正规化子条件等价于 $q\equiv\pm1\pmod{p^n}$ 和整个 Tate 参数为 $p^n$ 次幂；固定 $A[p^n]$ 同余时分裂分母素数至少 $4p^{2n}+1$。
- [R36：可变四次参数的二进惯性域](../results/R36-variable-quartic-dyadic-inertia.md)：完整惯性核加强 $v_2(A)$ 三分支的模 $4$、模 $8$ 和赋值条件，含 $c_6=0$ 端点的独立 Hensel 证明；纳入后 $2$–$p$ 辛比较自动相容，扭曲参数仍无界。
- [R37：三次下降与精确类群障碍](../results/R37-cubic-descent-and-class-group-obstruction.md)：固定参考的二除法域给普通或模 $2$ 射线三次类域，指定坏素数全部分裂；普通分支的基本判别式至少按 $p^4$ 增长，特殊分支有单位和明确素数见证。并证明相应 Mordell 点不在自然三同源的有理像中。
- [R38：三进参数与辛条件](../results/R38-three-adic-parameter-and-symplectic-filters.md)：完整使用温和四阶的三行分类，按 $B\bmod9$ 精确限制 $v_3(A),v_3(n),3\mid d$；最浅好约化分支有额外迹筛，$3$ 处辛符号明确选择归一化的 III/III$^*$ 型。
- [R39：小 Hecke 实际修正的有限支撑](../results/R39-hecke-vertical-support-control.md)：真实对角拉回的非恒定部分只支撑于有限自同源集合；$T_2$ 的修正至多四值，$p\equiv1,9,25\pmod{56}$ 时全光滑开集平凡。另用 gonality 无条件证明其 trace-zero 方向对全部 $p>37$ 非零。
- [R40：变量四次参考的三次类域](../results/R40-variable-quartic-cubic-class-fields.md)：将三次类域论证推广到全部 R24 参数，逐一处理 $3,p$ 和六种二进类型；普通分支给 $|d|\operatorname{sf}(B)\gg p^4$，射线分支给二次增长，含 $B=1$，仍没有统一上界。
- [R41：二与所有 p 幂除法域不交](../results/R41-two-and-p-power-division-field-independence.md)：R37、R40 的增长界排除全部二次交域，实际联合像为 $S_3\times G_{p^s}$，无需高次 CM 同余；好素数中惰性且迹为奇数者密度恰为 $1/6$，但均在 $p^2/4$ 之后，未给首个检测素数上界。
- [R42：三次整环与原始指标计数](../results/R42-cubic-index-forms-and-fixed-root-count.md)：三次最大整环的判别式精确为 $D_F$ 或 $4D_F$，Fermat 根的指标为 $J$ 或 $2J$；证明指标坐标互素，并由已发表 Thue–Mahler 定理给固定带符号 $Z$、跨全部 $p$ 的显式解数界。解数界不控制最大指数。
- [R43：实际坏素数处的 Néron 高度](../results/R43-neron-height-from-integral-correction.md)：以双扩张及规范截面证明无基点高度差为 $-(k_i-k_j)\log_\ell(p)/2$，并给基点 Nekovář 项的准确符号和 $d^2$ 比较；$T_2$ 的坏高度至多四值，仍须另行满足实际 QC 商的条件。
- [R44：奇惰性加性素数的参数排除](../results/R44-inert-prime-parameter-obstruction.md)：$p\equiv19\pmod{24}$ 时，$(q/p)=1$ 的惰性加性素数强迫 $(q/B)=(-2/q)^\alpha$，这是不依赖 III/III$^*$ 的纯 $j$ 筛；给通过既有二进、三进和分母显式条件而被此筛删除的整数见证。
- [R45：实际 Heegner 商的积分 QC 方向](../results/R45-heegner-quotient-integral-directions.md)：已发表一阶矩及范数界给 $a=\dim A\gg_\varepsilon p^{3/2-\varepsilon}$；$p\ge151$ 时 $T_2|_A$ 非标量。满足实际商与 Chow–Heegner 条件的整数格中，秩至少 $a-n$ 的子格使全部坏 $p$ 局部高度恒定；未控制辅助处完整函数或共同根。
- [R46：三次 Selmer 嵌入与精确全局筛](../results/R46-cubic-selmer-and-mordell-weil-sieve.md)：R37 的指定类群字符空间 $V$ 全部属于自然三同源 Selmer 群；若 $W_e$ 为其与 Mordell–Weil 像之交，则 $V/W_e\hookrightarrow\Sha[\phi]$。指标三次覆盖处处局部可解，有有理点恰当字符属于 $W_e$，给精确候选域计数，仍须满足原始整数与完整分母条件。
- [R47：对数同构与实际全局高度方程](../results/R47-heegner-logarithms-global-height.md)：将 DLF 的已知解析子群论证无条件用于实际 Heegner 商，证明每个辅助处的有理点对数满秩及闭包有限指数；对 R45 核中方向统一归一化有理截面，消去所有非辅助局部高度，得到含准确迹二次型、平移线性项及完整辅助高度的必要方程。积分指数和统一共同根排除仍未知。

- [R48：真实解析方程的饱和格与共同根证书](../results/R48-analytic-saturation-and-root-certificates.md)：有限维真实 QC 函数空间有规范饱和整格，保持共同零点及全部特征零方向；统一整数指数不是根排除的逻辑前提。饱和约化的最大次数至少为维数减一，固定函数组无根等价于某个有限精度的无解证书，但没有随层统一精度。
- [R49：真实 QC 函数独立性与次数增长](../results/R49-independent-qc-functions-and-saturated-degree.md)：把已发表 BMS 定理逐项用于实际无基点 Poincaré 高度，证明每盘的完整缺陷函数连同全纯积分在 $\mathbb Q_\ell$ 上代数独立；饱和后次数至少按 $a-n-1$ 增长。相容 Hodge splitting 的全局与局部变化精确相消，不能当作新增方程；根的算术识别仍未完成。
- [R50：实际 Selmer 群的交替矩阵](../results/R50-actual-selmer-alternating-matrix.md)：由准确中心值和已发表 supersingular CM 定理，对全部 $p>37$、$p\equiv3\pmod4$ 得 $\mathrm{Sel}_p(y^2=x^3-x)=0$。实际同余曲线的 $p$-Selmer 群是来自 Poitou–Tate 对偶的 $s\times s$ 交替矩阵的核，$s$ 是分裂乘法新增素数个数，故维数至多 $s$ 且模二等于 $s$；未计算非对角算术条目。
- [R51：原始指标点的准确充分条件](../results/R51-primitive-index-sufficiency.md)：在候选三次最大整环上，原始坐标与精确高次幂指标自动恢复全部奇素数原始性；只须保留模 $3$ 的迹线性条件及至多一个二进条件，即与 R19 实际异常同余等价。仍须统一排除随 $L,Z,p$ 变化的精确原始幂值。

- [R52：小满射素数与有界次数检测域](../results/R52-small-surjective-prime-and-detection-fields.md)：实际异常曲线有完整 $2/3/5$ 进满像之一；处理全部二次交叠后，惰性非零迹检测域次数至多 $240$、检测比例至少 $1/4$，加入坏约化排除后次数至多 $480$。模五满像时与整个异常 $p$ 幂塔不交。判别式和有效素数界仍依赖导子，限定族的对数界明确以 GRH 为条件。

- [R53：通过现有筛后存活的全局覆盖](../results/R53-nonzero-mw-after-frobenius-filters.md)：构造 $p=43$、$W_1\ne0$ 的完整普通类群候选，通过分母素数和全部小 Frobenius 分裂筛；387 位素数有自含 Lucas 证书。最大整环及指标式显式，实际高次指标方程在每个完成域都有原始解，但未得全局原始高指标点，因此不是异常同余曲线或反例族。
- [R54：Hecke 谱缺陷与有限坏纤维靶集](../results/R54-hecke-spectral-defect-and-finite-target.md)：将全部真实高度方程归一化为一个完整谱缺陷向量；积分核只要求该向量落在坏纤维数据的线性包，而有理点须落在对应联合有限靶集。准确恢复被取核丢掉的离散信息及所需补充方向数，保留完整局部高度与线性平移项。
- [R55：真正可达坏分量与扩大 QC 核](../results/R55-rational-bad-components-and-larger-qc-kernel.md)：在确切未分歧最小正则模型上证明可达分量恰由 $\mathbb F_p$ 超奇异 $j$ 标记，各光滑开集为 $\mathbb A^1/\mathbb F_p$。其个数 $s_p$ 有准确类数公式和有效 $O(\sqrt p\log p)$ 上界，真实零坏高度方向格秩至少 $a-s_p$；有限靶逆像的 CM 识别仍未知。

- [R56：单素数指标的射线类群与单位递推](../results/R56-single-prime-index-ray-class-and-unit-recurrence.md)：R53 的原始高指标元在 $q$ 上只能支撑于指定的不分歧素理想，且在 $2$ 上恰有三种模式；在模 $(3)$ 射线类群给三个明确必要关系。通过关系后的全部解由三个单位轨道及三阶递推零点精确参数化，两侧指数均有效；本例的射线类群、基本单位和生成元尚未实算，未判定实际高指标点。
- [R57：真实新 Hecke 谱的坏高度非消失](../results/R57-new-hecke-spectrum-does-not-kill-bad-height.md)：构造全局有理潜在全环面幂等元，给 $p\equiv5\pmod{12}$ 时完整 Jacobian 上的闭式分量高度差。$p=41$ 的已发表非消失输入使 $A=J$，真正可达的 $j=0,28$ 之间有 $k_{28}-k_0=240/7$，否定新旧谱不同便使实际坏高度全消失的推论；另给任意实际方向的分量部分迹与图作用公式。
- [R58：平方惯性型、环类分裂及理想阶界](../results/R58-ring-class-splitting-and-small-split-primes.md)：$p\equiv1\pmod{12}$ 时 $\lambda^2$ 在 $p$ 外不分歧，项目除法域分裂导子 $p$ 环类群正合列。对任何非主分裂素理想、阶 $r$，包括 $q=2,3$，实际整数 Frobenius 迹给 $p<4q^{r/2}$；排除十七个明确商域并给有效判别式增长下界，仍未控制变化商域。

- [R59：局部类型、环面二次扭曲与真实高度核](../results/R59-local-types-toric-twist-and-height-kernel.md)：完整 Jacobian 的环面因子恰为 level-$p$ Jacobian 的二次扭曲；principal-series 与 supercuspidal 因子分别对应 Igusa 与 Drinfeld 中间上同调。实际 Heegner 商的 principal-series trace-zero 方向全部消去几何坏高度，给所有 $p$ 的部分迹公式及精确核分解，仍缺辅助处共同根识别。
- [R60：Selmer 矩阵的 Kummer 剩余符号](../results/R60-selmer-matrix-kummer-residue-symbols.md)：CM 惰性新增素数的单点松弛类唯一归一化，实际交替矩阵子块由固定 CM 除法域中的两个 $p$ 次剩余符号及准确因子 $2$ 给出。联合控制域线性不交；固定旧素数后，新增条目零／非零模式有精确密度。尚未算出具体根式，修改 Selmer 条件的可实现性不等于存在实际异常曲线。
- [R61：双素数短关系与判别式增长](../results/R61-two-prime-relations-and-discriminant-growth.md)：$p\equiv1\pmod{12}$ 时两个非主分裂素理想给 $p<16(q_1q_2)^{\lfloor\sqrt{h_K}\rfloor}$；多个实际 Frobenius 根的实迹范数引理保留交域条件。CRT 避素构造给无条件 $|D_K|\gg(\log p)^4/(\log\log p)^6$，仍是必要下界。
- [R62：多素数选择与显式变化商域界](../results/R62-many-prime-relations-and-effective-quotient-bound.md)：用平方类超平面从两倍 Frobenius 域中选出一半，保证合成不含 $K$；结合反复 CRT 和短类群关系，对平方分支得 $\log p<(5/2)\log(8D^{5/2})\exp(2\sqrt{\log18\,\log h_K})$，特别 $D>\exp((\log\log p)^2/36)$。没有判别式上界。
- [R63：全部素数同余类的变化商域界](../results/R63-all-prime-classes-and-quotient-discriminant-growth.md)：用 $\lambda^{12}$ 和真实循环总分歧好约化扩张，把 R62 推广到全部 $p>37$、$h_K>1$；明确界为 $\log p<28\log(8D^{5/2})\exp(2\sqrt{\log18\,\log h_K})$，故 $D>\exp((\log\log p)^2/64)$。十二次幂迹差的非零性直接由有向理想支撑证明；变化 $D$ 与类数一仍未排除。

- [R64：惯性阶部分迹与 CM 类型靶集](../results/R64-inertial-order-traces-and-cm-type-targets.md)：完整全局惯性阶幂等元的 Drinfeld 迹逐字符求出，类型标量坏秩按 $p\bmod12$ 精确为 $0,1,1,2$；后三类靶由明确的两到三个有理 CM 点实现。真实 Heegner 商必须使用完整块交集，相应完整 QC 函数的共同 CM 值纤维仍未排除其他根。
- [R65：椭圆单位及一、二阶导数构造实际 Selmer 类](../results/R65-elliptic-unit-first-second-derivatives.md)：零 Selmer、类群等型消失及已发表有限 Gras 等式证明一个固定 Robert 单位的正确 $V(-1)$ 分量模 $p$ 原始。真实 $p$ 处校正后，一阶导数生成非退化单点类；退化者用可搜索辅助素数及原始二阶导数构造。二次下降和唯一归一化准确恢复 R60 的实际类，尚未据此构造异常曲线。

- [R66：小惯性三次商导子、非消失与 Tate 分母](../results/R66-cubic-conductor-nonvanishing-and-tate-primes.md)：独立证明三次环类导子 $M=D(3^aR)^2$ 的精确局部指数与类数一单位限制，已发表 Feigon–Whitehouse 公式给 $p>M$ 的中心值非消失。三次商与二除法域的三次部分不交，Tate 分母与 $M$ 互素并在三次扩张完全分裂；未用 submitted 的有限商/整性结论。
- [R67：全部小范数类代表与更强判别式增长](../results/R67-small-class-representatives-and-sharper-growth.md)：对每个类同时构造范数 $<8D^{5/2}$ 且与 $2D$ 互素的代表，类群盒子计数迫使固定界内已有许多非主分裂素数。两分支优化给全部 $p$ 的明确界，并将渐近 $\liminf\log D/(\log\log p)^2$ 下界提高到 $1/(2\log2)$；仍无判别式上界。
- [R68：Gross–Zagier 系数与实际极化传输](../results/R68-gross-zagier-height-coefficients-and-polarization.md)：将两个已发表 $\ell$ 进 Gross–Zagier 公式接到实际 Heegner 商，保留 Rosati 倍率、微分尺度和有理高度的 $1/2$。经典 Heegner 投影非挠后，每个特征对数及 BDP 分母均非零，无需高度非退化猜想；实际平移及完整辅助高度仍待计算。
- [R69：忘线映射与无条件秩零商](../results/R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)：直接求出 $p+1$ 个忘线映射的配对矩阵，并通过 Galois 下降及三次 Cartan 轨道构造实际扭曲 Jacobian 商。已发表 BD1997 Theorem B 与 Gross 周期的 Galois 相容性，使小惯性且 $p>M$ 时得到有理点群有限的非零商；不以 Studnia 的未发表 B 为输入，仍缺尖点整性及变化导子排除。

- [R70：Robert 单位的有限域证书](../results/R70-robert-unit-finite-field-certificates.md)：确定 $K(A[p])=K((1+i)^3p)$ 及算术 Artin 取向，将基单位局部投影化成 $p^2-1$ 个 $\psi_{11}$ 值的准确加权和。$p=43$ 时 $q=859,1031$ 非退化，$q=49019$ 严格退化；三个完整证书经根会话复算一致。尚未求实际导数或 Selmer 非对角条目。

- [R71：真实项链同源与层41的极化谱](../results/R71-necklace-isogeny-polarization-and-level41-spectrum.md)：以实际对应证明 $q=\phi r$、$qq^\dagger=2\phi\lambda$。求层41完整54维真实谱及行列式 $2^{108}3^8 5^8 113^8 461^6$，其外辅助处有整右逆；有限组合证书已从零复核。

- [R72：最优商尖点形式浸入及分母必要条件](../results/R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：已发表 Raynaud 正合性给最优商微分饱和；实际 Tate 首项、秩零和形式群无挠性独立重证分母必须 exceptional。前提为三次中心扭曲值非零；不依赖未发表 Studnia B/D，未排除 exceptional 或变化导子。

- [R73：退化素数的实际辅助导数及非零矩阵项](../results/R73-explicit-auxiliary-derivative-residue.md)：对 $p=43,q=49019,r=859$，860条核线的实际 Vélu–Robert 加权和为 $31+12i$，原始导数为 $17+26i\ne0$。退化性使p校正不改变该值，859确为二阶补救的有效辅助素数；两个实际非对角项均非零，规范条目另核。完整C++证书已复算。

- [R74：两个共同Heegner域与普通素数47](../results/R74-level41-two-heegner-fields-and-common-ordinary-prime.md)：实际模符号 Krylov 行列式模1009为161、415，严格证明 $D=-43,-163$ 各使层41全部54个中心扭曲值非零。真实 $T_{47}$ 行列式模47为28，给全嵌入普通性；完整PARI和独立小证书均已复算。

- [R75：一般系数域的47进高度与周期校准](../results/R75-general-coefficient-heights-at47-and-period-calibration.md)：已发表2015年期刊版 Gross–Zagier 在47处无需系数域完全分裂。Hodge基点、$h_K=2h_{\mathbb Q}$、实际极化及圆分 Rankin 导数的非零代数周期因子均明确；不能省略具体周期倍率。

- [R76：三点纤维与扩大三次非消失范围](../results/R76-three-point-fibres-and-cubic-nonvanishing.md)：三个同取向最优嵌入由整单位共轭和外接半径排除，得 $M<16p/7$ 时纤维至多2；若 $(-7/p)=1$ 可到 $M<8p/3$。实际 $p\equiv2\bmod3$ 时再用整格平方指标，把 $(-7/p)=1$ 或 $M\equiv1\bmod3$ 子类扩大到 $M<3p$。已发表 Waldspurger 公式接入 R69/R72，仍无变化 $M$ 上界。

- [R77：层41全部圆分导数与实际高度非退化](../results/R77-level41-cyclotomic-derivatives-at47.md)：整普通测度和2162条路径给 $L_{47}'/47$ 的严格首位，Hecke Krylov 行列式模47为21。全部54个圆分导数非零，经R75得真实 $J_{\rm ns}^+(41)(\mathbb Q)$ 的47进高度非退化；规范数值、平移及共同根仍待计算。

- [R78：规范 Selmer 矩阵与原始二阶坐标](../results/R78-normalized-selmer-entry-and-second-order-coordinate.md)：实际 Miller 配对、正权导数的 Hilbert90 符号、二次下降和局部 Tate 配对给 $p=43$、$(859,49019)$ 子块 $\left(\begin{smallmatrix}0&6\\37&0\end{smallmatrix}\right)$，行列式36；保留真实 $p$ 处三个校正量，二阶类的唯一规范表达已定。证书从头复算一致，不构造实际异常曲线。

- [R79：真实 T₂ 平移与 CM 点精确比例](../results/R79-actual-T2-CM-translation-and-height-ratios.md)：粗模重数和 Riemann–Hurwitz 给层41方向 $F=27T_2+4$ 的 $3\eta_F=162U_{-7}+1620B_{-8}+120B_{-4}+8U_{-3}$。两个真实 CM 除子在全部54因子非零，其比例平方为 $(1/4)v_{-8}/v_{-4}$，八个系数域均有精确平方根证书；实际正负、其余CM比例及完整局部高度仍待定。

- [R80：三色全塌缩与类数一非消失](../results/R80-three-colour-collapse-and-class-number-one-nonvanishing.md)：$M<3p$、$p\equiv2\bmod3$ 时每纤维至多三点；周期零迫全部左序含 $\mathcal O_{-7}$，纯理想论证及 Frobenius 主化给唯一 Brandt 类、$h(\mathcal O)=3$。类数一分支由环类数公式和 $H_{-108}$ 的精确迹排尽，主源及小证书已复核。

- [R81：全部虚二次域的三倍水平非消失](../results/R81-cubic-period-nonvanishing-below-three-times-level.md)：在 R80 后，类数三分支的原始性迫导子一；范数27与几何界只余 $(D,p)=(107,41)$，再由平方指标排除。故所有虚二次域的原始三次角色在 $M<3p$ 均给非零周期及实际中心值；R69/R72 可用此范围，非 exceptional 分母强迫 $M>3p$，仍非导子上界。

- [R82：真实 Schur 补与可除 Selmer 直线](../results/R82-actual-schur-complement-and-divisible-selmer-line.md)：含 R78 二阶块的真实候选曲线，其剩余 Selmer 群由准确交替 Schur 补决定；恰三处分裂乘法素数时维数一，并有 $\operatorname{Sel}_{43^n}\simeq\mathbb Z/43^n$。保留秩零及可除 Sha 的可能；已发表 p-converse 的半稳定假设不覆盖实际导子 $32\operatorname{rad}Z$，不能转移至辅助曲线或提升整塔同余。


- [R83：小辅助 CM 序与统一周期界](../results/R83-small-auxiliary-cm-orders-and-uniform-period-bound.md)：三个同取向嵌入构造判别式不超过 $3\lfloor M/p\rfloor^2$ 的真实辅助序；逐处理想拼接和约化型计数给周期消失时 $h(\mathcal O_c)<16r\lfloor r\rfloor^3$，$r=M/p$。因此 $p\ge2M/h^{1/4}$ 保证非消失；常数明确，未控制变化导子的上界。

- [R84：固定底域的变化导子非消失](../results/R84-fixed-field-variable-conductor-nonvanishing.md)：由已发表谱端及正主项、R87 独立 regular 计数，得固定 $K$ 下有效的 $p\ge C_{K,\epsilon}c^{1+\epsilon}$ 非消失。九个类数一底域可取同一有效常数，非 exceptional 分母迫 $M\gg_\delta p^{2-\delta}$；未处理 exceptional 或给导子上界。

- [R85：非分裂 Cartan 高度与层41全部 CM 坐标平方](../results/R85-nonsplit-cartan-heights-and-level41-CM-coordinates.md)：直接验证 CST admissible order、test line 和次数二商的 $2d^2$ 高度倍率；实际400条项链路径确定各 Hecke 域中的 $\kappa$。求 $U_{-3},U_{-7}$ 的全部坐标平方并验证精确平方根，全部64个符号组合均使规范平移非零，故实际平移生成秩一 Hecke 模。GP 从头及独立有理证书复验一致；实际符号已由 R89 确定；完整高度与共同根仍待计算。

- [R86：最近 CM 点对与三次类数界](../results/R86-nearest-cm-pairs-and-cubic-class-number-bound.md)：最近点对使辅助判别式随纤维大小下降，层次积分给周期消失时 $h(\mathcal O_c)<64r\lfloor r\rfloor^2\le64r^3$。有效判据改善为 $p\ge4M/h^{1/3}$；Siegel 推论的统一指数为 $5/6+\epsilon$，常数一般无效。

- [R87：统一三次轨道界与平方根非消失](../results/R87-uniform-cubic-orbital-bound-and-square-root-nonvanishing.md)：三阶角色在分歧交集的导子部分整除9；直接紧环面体积和通过零点的整数倍计数给全域统一、有效的 $p\ge C_\epsilon M^{1+\epsilon}/h(\mathcal O_c)$ 非消失，另给完全明示的有限算术判据。Siegel 推至 $p\gg_\nu M^{1/2+\nu}$，此常数一般无效；独立修补 FW 一般计数的单元素边界，不否定其最终非消失结论。

- [R88：R53 原始指标方程的真实 Frobenius 排除](../results/R88-r53-primitive-index-frobenius-obstruction.md)：证明四次判别式与不可约二挠三次式的准确迹模四关系；在521处与同一曲线的模43迹比较，完整排除387位 R53 原域全部原始高指标元。保留其处处局部可解及非零有理覆盖点事实，不扩大为同 Z 的全部三次域或统一排除。

- [R89：全部带符号 CM 坐标与实际 T2 平移](../results/R89-signed-CM-coordinates-and-actual-T2-translation.md)：以已发表 Heegner–Jacobi 模性、正确紧化与单位重数、实际新/Fricke+模符号投影确定层41八个 Hecke 域的 CM 坐标及 ξG；精确平方与旧独立高度证书全一致。二次域 ξG=(405h+2685)/2，h²−2h−31=0；未计算完整局部高度或证明共同根排除。

- [R90：类数三周期完整消失表及实际排除](../results/R90-class-number-three-periods-and-actual-frobenius-exclusions.md)：23个原始类数三序的严格类多项式证书给全部四个周期零例；实际整数迹和保留三次角色将四例全部排除。故实际小惯性且环类数三时无条件非消失，不限M/p；非exceptional分母强迫环类数至少六。

- [R91：不分歧三次角色、类数三商域的绝对素数界](../results/R91-unramified-cubic-class-number-three-prime-bound.md)：非零整数整除式覆盖全部素数，三次角色及同一个全局四次幂角色的耦合Frobenius测试，使实际小惯性、hK=3、c=1只余(D,p)=(643,47),(907,47)。全部整数和有限域证书可用标准库重验；未证明两对来自椭圆曲线。

- [R92：四个小层的三色单位理想与实际整性](../results/R92-small-level-fourier-units-and-actual-integrality.md)：对 p=41,47,59,83 给整系数 Bézout 证书，证明真实三色 Fourier 理想为单位理想；因此这些层没有 exceptional 素数，非零周期的实际小惯性分支 j 整。完全独立于存在证明异议的 BBM 整点分类，未宣称整点已全排除。

- [R93：真实三除法域完全排除不分歧类数三分支](../results/R93-class-three-exclusion-by-the-actual-three-division-field.md)：一般小惯性、c=1、整 j 时，Δ立方类只含 p，真实 E[3] 的 S3 商为 Q(ζ3,∛p)。将同一好约化整数迹的模3/模9限制与 R91 的模47角色耦合，排除两个最后候选，故所有 p>37 的 hK=3、c=1 分支不存在；h(O_c)=3 只余七个类数一底域/导子组合。证明与标准库证书独立复核通过，不依赖 BBM。

- [R94：中央对合与完整Chow–Heegner平移算子](../results/R94-central-involution-and-complete-Chow-Heegner-operator.md)：真实对应满足(S−1)²=p−κ/2，平方自由合数固定除子保留单位和交长；层41全部53方向平移有理秩50，三维零平移核。115组CM系数、161功能、54个Hecke算子及无固定点对应的几何反算皆有精确证书；环境重置后完整重算字节一致，辅助局部高度和共同根仍开。

- [R95：统一剩余类障碍与R53同Z的全部排除](../results/R95-uniform-residue-obstruction-and-all-r53-branches.md)：1033处模2/模3/模p的同一实际整数迹，迫全部p>37的R19三族Z为平方或立方模1033，排除344类。R53的±q违反，故同Z全部三族、三次域、素数指数均无原始解；不需MW秩上界，原非零覆盖与局部解仍成立。

- [R96：实际判别式三次支撑及3处精确分支](../results/R96-actual-cubic-discriminant-support-and-local-three-branches.md)：整j下η在q≠3,p处分歧恰当且仅当3∤v_qΔ，包括q2。K3,c6/9时实际二除法域与三次商在3局部相同；完整整基计算给c6的v3Δ模3为0/2、c9为1/2，并给精确j赋值和七对环类序的Δ三次支撑。

- [R97：认证Thue方程完全排除层41的环类数三分支](../results/R97-level41-class-three-exclusion-by-certified-thue-equations.md)：一般类数一的φ=λ4η^{-v}给精确主理想角色，排除四小层全部非K3组合；层41的K3两导子完整归为192个无GRH认证Thue式，14个j只留CM0，其余13个由5/11处实际迹排尽。环境重置后完整重算恢复；37<p≤97该分支只余p47/59/83、K3、c6/9。

- [R98：剩余三层必须有新的四阶惯性素数](../results/R98-small-levels-require-new-quartic-inertia.md)：对p47/59/83、K3、小惯性、三次导子6/9，若2/3/p外无四阶惯性，Δ平方类只有−3/6；完整396个认证Thue式给49解，各层仅留CM0。因此任意剩余无CM实际曲线必有q≡1或11模12、q≠p的四阶惯性且v_q(j−1728)奇；没有排除该变化分歧分支。

- [R99：立方分母偶分支的多Frey与四条固定非CM曲线](../results/R99-cube-even-branch-multifrey-and-four-fixed-curves.md)：Q√3上的显式二次角色和二同源下降给精确层768、nebχ12；全p不可约及11个实际同迹测试排六轨道，余四轨道精确为B0的±1/±2扭曲。每个Dq乘q覆盖q=p；实际B[p]同构于其中之一，尚非统一排除。

- [R100：四次差的二次商及二处四阶惯性排除](../results/R100-quartic-shadow-and-dyadic-inertia-exclusion.md)：对p11模12、K−3、小惯性、c6/9、整j，实际β6精确等于χΔ|GK；D4在3的反射和二处完整字符比较排e2=4。c6仅e2=3/6，c9仅e2=1/2且v2j≥12；新奇四阶素数仍须控制。

- [R101：四小层全部尖点的严格阿基米德约化](../results/R101-certified-all-cusp-archimedean-reduction.md)：独立Arb入口及328个整数正余量见证覆盖113尖点，p41/47/59/83的全部整点满足log|q|^-1≤896/1100/1419/2127。§9以全部整数坐标严格包围再降到246/282/354/508，§10逐个排完1≤j≤1727。正确矩阵方向、零坐标及安全误差因子均明示；实q完整覆盖及最终候选识别现已由R109完成，不调用BBM整点分类。

- [R102：层41在47处的实际Makdisi模型](../results/R102-actual-level41-makdisi-model-at47.md)：实际41挠点、820项链及带ζ41的迹给73维L=K+D的积分评价基；子式43+17i模47为单位，模47⁴的Frobenius下降和完整108次局部因子皆有独立证书。模型仍须接实际除子、完整Poincaré高度及共同根。

- [R103：完整二进好约化模型唯一确定辅助扭曲](../results/R103-unique-twist-from-complete-dyadic-models.md)：两条参考的实际3挠点域及H加8的全参数稳定模型，给III偶X分支唯一必要d=(a/3)(−2)^e，(−1)^e=(2/ab)。3处同一整数迹固定符号；2/3两处允许两种辛类型，不能再制造辛冲突，整体排除仍开。

- [R104：变化判别式域上的实际三次导子](../results/R104-variable-discriminant-field-and-actual-cubic-conductor.md)：真实二除法S3域在F=Q√Δ上的原始环类导子精确为3p/6p/18p，三次最大整环判别式DF f²，且|DF|=3Q、p在F惰性。给完整局部非零的Pic/3Pic判据和精确扭曲导子；D4嵌入等价旧范数条件，抽象类域存在尚非曲线共同实现。

- [R105：实际CM点的粗模二阶展开](../results/R105-actual-cm-coarse-jets-in-makdisi-model-at47.md)：41挠点的真实形式形变与同Weil根校准，给R102全部73坐标至47⁴的点值、切线、二阶项；先除A²再用t=A³，实际粗模坐标导数范数35为单位。尚非QC高度函数单根性。

- [R106：立方族II的层1536与二进排除](../results/R106-cube-family-II-level1536-and-dyadic-exclusion.md)：全部十三新形式轨道中九个被同迹范数排除，余四B1扭曲；完整两点域和H加16稳定性排Y5模8，实际Y必须1模8，参考只余按a模3指定的两条非CM曲线。仍未排剩余全局同余。

- [R107：实际四次迹奇偶与变化判别式增长](../results/R107-actual-quartic-trace-parity-and-discriminant-growth.md)：K分裂/F惰性素数的同一好扭曲迹须偶且a²≡3m²模p，迫q>p/4并排抽象F−111例。两个普通Dirichlet Burgess界及完整互素理想计数给有效Q≫εp^(2−ε)、规范导子≫εp^(6−ε)；仍无支撑上界。

- [R108：立方异奇偶分支与唯一固定参考](../results/R108-cube-opposite-parity-and-unique-reference.md)：族I及III奇X的半整数h给整辅助模型、精确层768；全部十轨道及16局部模型迫a奇b偶，并分别Y1/−1模8。Hensel全参数稳定性和3处同迹唯一确定d=(a/3)(−2)^(b/2模2)，剩余同余尚开。

- [R109：四个剩余小层的完整整点分类](../results/R109-four-small-level-integral-points-by-complete-real-covers.md)：113尖点、7128实分支、130937严格叶完整覆盖，独立384位逐叶通过；169候选全部准确判定，只余41/47/59/83各8/8/9/8个惰性CM值。中间整数段、CM端点及全部相位均保留；不调用BBM分类。四层实际环类数三分支由此前整性接口全部关闭，非整j和一般层仍开。

- [R110：实际尖点与典范除子理想](../results/R110-actual-cusps-and-canonical-divisor-ideals-at47.md)：同Weil规范的20尖点首两项给54维真实典范空间，实际K_f与D在199维平方空间中的理想、零Jacobian类和CM限制均准确构造；106阶单位子式证明辅助典范除子互不交。全部矩阵独立复核，完整高度仍开。

- [R111：族II由五阶点域唯一确定参考](../results/R111-cube-family-II-unique-reference-from-five-division.md)：实际48次五阶点域的剩余次数一分支给所有H−1模8的好约化迹−2，H加16稳定；同一非零整数迹迫唯一d=(a/3)(−2)^e、(−1)^e=(6/a)。全部立方分母剩余分支现在各有唯一非CM参考，尚未排全局同余。

- [R112：真正B−4类的实际局部实现](../results/R112-actual-cm-minus4-class-in-local-makdisi-model.md)：同Weil根的真实四次CM自同构和41挠点形变识别20个椭圆点，除B取粗参数B²，实际核给73维H0(L²(−K_f−Z−4))及完整Frob下降。直接表示整数类Z−4−D，保留挠点；不等同于已算高度。

- [R113：全素数的环类数六周期非消失](../results/R113-class-number-six-cubic-period-nonvanishing.md)：完整83个原始序及严格类多项式，把所有可能周期零压到(707,53)、(1432,43)、(2443,43)，均违反实际p2/5模9。全部实际h(O_c)=6中心值非同时零；四小层该分支也由R109排尽，尚存共同零须h≥9。

- [R114：最小变形与固定CM同余的精确深度](../results/R114-exact-cm-congruence-depth-from-minimal-deformations.md)：对R19全部实际三族及每个n，E[3^n]≅A[3^n]当且仅当Z为3^n次幂；E[p^n]≅A[p^n]当且仅当Z为p^(n−1)次幂。完整Tate类给必要性，Q8局部刚性、强不可约及最小有限平坦R=T给充分性；未把一次同余自动提升整塔；R128已推广到全部奇数层；九次幂支的显式全点分类及全部p>37排除现由R129完成。

- [R115：环类数九的实际周期非消失](../results/R115-class-number-nine-periods-and-actual-trace-exclusion.md)：全部55个序及完整非零整数gcd覆盖所有p，四个实际必要候选中三对因C9类群而导子不原始，最后(5443,83)由q23同一整数迹排除。独立GP及有限域枚举通过；四小层h9分支排尽，共同零须h≥12。

- [R116：类数一商域的有效导子幂次下界](../results/R116-fixed-class-one-cubic-conductor-prime-bound.md)：hK1且K≠Q√−3时，同一真实迹给p<256q²；Chang短箱与正权理想计数先给固定(K,c)的有效p界。§7展开全部变化常数，进一步在八域统一证明有效c>p^(1/1000)，含exceptional且无需整j；仍是导子下界，未给主问题绝对常数。

- [R117：实际CM群运算与主除子Poincaré范数](../results/R117-actual-cm-group-operations-and-principal-poincare-norm-at47.md)：真实325维三次空间及单位秩判据给−B−4、−2B−4和2B−4，保留挠点和完整Frob下降；实际主除子范数4666447、47进对数4643130模47⁴。所有核/子式/范数由标准库独立复核；非主局部高度及共同根仍开。

- [R118：环类数十二的实际周期非消失](../results/R118-class-number-twelve-periods-and-ramified-frobenius.md)：286个原始序的严格类多项式与完整整数gcd覆盖全部p，六对实际必要候选四个被同一split迹/η排除，两个被ramified惯性/迹排除。独立GP286式全一致；全部实际h12周期非零，四小层该分支排尽，共同零须h≥15。

- [R119：分歧素数的高斯Frobenius平方界](../results/R119-ramified-prime-gaussian-frobenius-square-bound.md)：实际商域在q≥5、q≠p、q1模4处分歧时，好约化j1728纤维的真实Frobenius=a+bi，且p|b，故q≥p²+4。q3模4给明确非CM局部实现，说明该平方界不能直接延伸；没有声称局部例子的全局像异常。

- [R120：九级固定Cartan扭曲与显式三次覆盖](../results/R120-nine-cartan-twist-and-explicit-cubic-cover.md)：R19的九次幂分母映入固定亏格二曲线y²=7x⁶+12x⁵−36x⁴−10x³+84x²−72x+19；精确Qi商特征、三次椭圆覆盖、秩至少二及全部整j纤维均已验证。R126先给九幂支绝对p界，R129现给全部四个有理点且均CM，关闭该分支；弱Cartan条件不等同完整9挠点同构。

- [R123：实际Weierstrass微分与形式对数尺度](../results/R123-actual-weierstrass-differentials-and-formal-logarithm-scale.md)：完整Gauss–Manin恒等式给KS尺度β=(9B dA−6A dB)/(2(4A³+27B²))，Tate规范中准确为dq/q。实际47处β0模47为38，二阶积分保留β1交叉项；居中坐标的三点组合严格提取模47⁴的形式对数线性项。

- [R124：九级扭曲的准确秩二与实际五进对数](../results/R124-nine-twist-exact-rank-two-and-five-adic-logarithms.md)：全部3888个群元素的角色恒等式、eta/Sturm和两嵌入L′>7/25的严格有理界，给Jacobian准确秩2及NS秩至少2。两条明确除子生成有限指数格，5进对数除5的矩阵为[[64,46],[2,76]]模125且模5非奇异；R125给实际全局高度；全部有理点现由R127/R129的另一条路线完整分类。

- [R125：实际实乘法与五进全局高度](../results/R125-explicit-real-multiplication-and-five-adic-heights.md)：双三次覆盖及显式3同源给Rosati自伴随有理RM T²=3和实际除子作用；以同源兼容的(U−2)ω补空间、完整域迹及极化规范，精确算HJ=[[425,1710],[1710,10]]模5⁵。m66/132交叉检查、标准库完整证书及已发表Coleman–Gross公式均核完；该高度计算本身不是QC根分类；全部有理点后由R129另法完成。

- [R126：唯一三次域椭圆覆盖与九幂分母的定性界](../results/R126-unique-cubic-elliptic-cover-and-ninth-power-finiteness.md)：L=Q(r),r³−3r−4=0的完整整环/类数及2、3赋值计算，将全部C(Q)压到唯一ε=r²+r−7椭圆扭曲覆盖。另由Faltings与实际den(j)=|Y|^(9p)直接得到九次幂Z分支的绝对有限p界B9；所有更高3次幂同样不能产生无界p。此处B9为定性界；R129现已将该分支加强为p≤37，非九次幂分支及主目标仍开。


- [R127：唯一三次域覆盖的完整二下降与准确秩一](../results/R127-cubic-cover-complete-two-descent-rank-one.md)：确定全S-unit模平方基及每个实际局部Kummer像，1024候选完整剩8；真实非挠点和准确(2,2)挠群给rank=1、Sha[2]=0。覆盖映射为四次且拉回微分dx/y，不声称已得MW饱和基。完整标准库证书和独立局部/多项式验证通过。

- [R128：全奇数层准确同余深度与全部分裂素数幂排除](../results/R128-all-odd-congruence-depth-and-split-prime-power-exclusion.md)：对实际R19曲线令g=gcd_q vqZ，则每个奇m都有E[m]≅A[m]当且仅当m|pg；g为奇数、只含3模4素因子且(g,Z)=1。实际有限平坦Tate模型、最优级/权、Q8惯性和最小R=T封闭各层；Lemos定理排全部1模4素数幂（含第五幂）。R129另给9∤g，仍不控制g1及变化3模4因子。

- [R129：九级扭曲的完整有理点分类与九次幂分支排除](../results/R129-nine-twist-complete-rational-points-by-elliptic-chabauty.md)：在R127准确秩一上，用5惰性三次扩张的实际对数和完整尾界覆盖全部六个剩余盘，得C(Q)={(-1,±12),(1,±2)}。四点仅给CM的j=1728或287496，因而全部p>37的实际九次幂Z及更高3幂分支均不存在；把R126定性B9加强为此分支的明确37界。全射影整数证书与独立精度/全盘核查通过；不声称整个统一性已解决。

- [R121：实际CM对数、47饱和Hecke格与粗模展开](../results/R121-actual-cm-logarithms-and-saturated-hecke-orbit-at47.md)：304位454步真实Makdisi长乘和零类测试完成，严格PicChart/Čech/KS及居中三点式给全部54个真实47进对数；实际Hecke循环行列式为单位，得到47饱和秩54格。实际CM坐标的CRT作用和j0粗盘三阶Abel展开均有独立证书，仍未计算非主局部高度或全部QC根。

- [R130：固定奇数层有限性及七级、四十九级限制](../results/R130-fixed-odd-level-finiteness-and-seven-adic-denominator-restrictions.md)：对每个固定奇m≥7，全部Weil乘子平方类的扭曲模曲线及Faltings给m|g分支有限p界B_m；不统一于m。七级反辛扭曲在Q2无点，正辛商含非挠点，不能用秩零排除。已发表X_ns+(49)全CM分类给49∤g；任何p→∞序列除至多一次3因子外，g的最小素因子须趋无穷。

- [R131：层41模型上的实际Hecke作用](../results/R131-actual-hecke-actions-on-the-level41-model-at47.md)：真实7条规范Vélu同源、全部41挠点及Weil根重标给T2/T3作用，KS规范准确产生1/ℓ因子；820行、Frobenius、典范核和完整54次Hecke谱由独立代码重建核验。保存紧凑算子证书及可重建目标矩阵哈希，避免提交大中间数据；不等同非主高度。

- [R132：最大同余层与分裂乘法支撑平方界](../results/R132-maximal-congruence-level-and-split-multiplicative-prime-bound.md)：以M=pg代替一次p，在全部素数幂上证明分母q3模4须q≥4M−1，q1模4须q≥4M²+1；若又为分裂乘法，真实Gaussian Frobenius及8整除进一步给q≥8M²−4M+1。得到相应高度下界，未给统一上界，也不能把最后一界用于非分裂乘法。

- [R133：两个CM点校准全部54个高度系数](../results/R133-two-cm-points-calibrate-all-54-height-coefficients.md)：53个P−3方向和P−7的F=27T2+4方向给54×54真实高度校准矩阵；其trace-Gram乘积行列式45模47，逆矩阵双侧验证通过。若给出对应完整局部高度即可无精度损失恢复全部系数；这些非主高度值尚待计算；b28(27T2+4)后由R134证明为零，不把校准矩阵误当高度结果。

- [R134：实际T2路径作用与层41坏高度完全抵消](../results/R134-actual-t2-bad-height-cancellation-at41.md)：直接以环带Kummer拉回/范数推前识别实际带权路径矩阵，并从真实Vélu微分及EP坐标计算两条自回路的Drinfeld迹；F=27T2+4的四个Xi均为117/2，故全部b_j(F)=0。清除R133唯一剩余坏处常数，54个辅助非主高度值仍待计算；不改变R57其他方向的非零坏高度。

- [R135：层41完整实际坏谱与四个有限靶](../results/R135-complete-actual-bad-height-spectrum-at41.md)：全部真实二、三同源的统一相位及额外自同构权重确定三种Drinfeld惯性块；接R94后得到全部53方向、四个精确β和50维零坏核。F3/F11/F13子式−839808000在47为单位；Ξ核与坏核交恰一维。四CM点实现全部有限靶，完整辅助高度及靶逆像仍开。

- [R136：真实形式指数与两个不相交Abel局部族](../results/R136-actual-formal-exponential-and-disjoint-abel-charts-at47.md)：构造两个Frob稳定54点族、实际不交126次基除子及72次残余理想；全三阶KS jets给整形式Abel逆。两族恢复R121长乘点后各在全部820×73 PicChart坐标逐项相同。保存5源码与4139字节最终证书，可重建大中间量；任意纤维坐标尚非选定高度。

- [R137：实际秩零商的分母深度与有效范数界](../results/R137-cyclotomic-denominator-depth-and-effective-bound.md)：严格以R69/R72非零三次中心值、实际秩零商为前提，形式积分全尾界给den(j)的p次根D整除明确实圆分理想范数Np。Parseval给Np≤(2p/9−4/[9(p−1)])^((p−1)/4)，各正深度−vℓj/p<(p−1)/4；全部负赋值若被p²整除则j整。无需先排exceptional，但未控制分子或M，也不覆盖共同中心零分支。

- [R139：全部奇数CM层的满像与准确尖点轨道](../results/R139-all-odd-cm-images-and-exact-cusp-orbits.md)：由实际八挠点、primary Frobenius和CRT证明A[m]在Q(i)上的全Cartan像；完整原始向量、对偶Tate商和一次全局共轭给轨道数(1+∏分裂ℓ(2vℓm+1))/2。R128剩余m|pg全为单轨道，因此并入固定3层不增加标准Runge所需轨道；不宣称全部模单位方法无效。

- **R138（已证明）**：[真实形式 Poincaré 双逆范数与三阶局部坐标](../results/R138-actual-formal-poincare-double-inverse-at47.md)：两套实际 Abel 族上完整主函数、四个126维限制代数及独立整数范数给 δ=1+41·47³、半对数44·47³；三阶框架坐标已定，Hecke 相容高度仍保留二次双线性项。

- **R140（已证明）**：[实际 Hecke 双扩张的整相容化与三阶高度接口](../results/R140-integral-hecke-balancing-and-cubic-height-interface-at47.md)：真实T3判别式23mod47，完整可分投影e及补空间逆s无47分母；规范标量混合二阶项给B=−sD，相容化后仅余54迹系数。Hurwitz分母界严格给三阶全尾截断，明确保留实际几何标量和非形式纤维搬运。

- **R141（已证明）**：[真正T3规范标量的混合Hessian及整高度修正](../results/R141-actual-canonical-t3-hessian-and-integral-height-correction-at47.md)：两组54点、270×54主部和完整函数空间给真实C=(logc)₁₁；eC=0、B=sC及MB−BMᵀ=C全部成立。保存完整54²矩阵和可重建来源，不能用任意双线性矩阵替代此几何标量。

- **R142（已证明）**：[尖点第二项消去与更强的实际分母理想](../results/R142-second-cusp-jet-and-refined-cyclotomic-denominator.md)：保留非零中心值/秩零商前提，以整组合消去z项而不除a₂；同一实际λ上vλW≥2vℓD，给D|Norm(J^[2])|Np。共同根处W一阶消失自动，二阶深度才是新条件，未证全p exceptional为空。

- **R143（已证明）**：[平方自由惰性CM扭曲的全部商中心值消失](../results/R143-squarefree-cm-twists-all-analytic-quotients-vanish.md)：A:y²=x³−x、m平方自由且各素因子3模4时，每个实际Weil乘子分支的每个正维Q阿贝尔商均L(B,1)=0。完整GL2下降、逐地根数和不可约块已证明；不宣称MW秩正或有理点排除。

- **R144（已证明）**：[真实CM高度差校准及全局截面常数消去](../results/R144-cm-height-difference-calibration-without-section-constants.md)：T2P−3=3P−12给第三实际CM坐标，53个P−12/P−3差值和一个P−7/P−3差值的矩阵det43mod47。全局截面常数相消；双扩张全证给以b的G_b=2d²F、η_b=dη−4dFU_b，实际截面和54个高度差仍待计算。

- **R145（已证明）**：[同一新框架的实际Hecke相容Poincaré局部值](../results/R145-actual-hecke-compatible-formal-poincare-value-at47.md)：真实三阶jets、双逆主函数及四个独立范数给δ=1+20·47³；加R141真实B修正后ΛH(σ(Y,Y))=4263370模47⁴，赋值2。指定纤维值已经完成，非形式搬运、全局截面及QC共同根继续。

- **R146（已证明）**：[全部新增乘法素数非分裂时的单位中心值](../results/R146-nonsplit-multiplicative-support-and-a-unit-central-value.md)：实际E[p]≅(y²=x³−x)[p]、p>37且s=0时v_p(L(E,1)/ΩE)=0。整旧/新周期比较保留全部假设，推出解析秩0、E(Q)及Sha有限；没有排除实际E。

- **R147（已证明）**：[真实CM12点及二阶Hecke碰撞单位](../results/R147-actual-cm12-hecke-branch-and-collision-units-at47.md)：真实Vélu/41挠点/项链给全部73坐标和三阶jets；粗模分支重数3/1、c=6549518250000及同一ω的dj系数比1525119准确计算，供全局截面纤维搬运。

- **R148（已证明）**：[含对角分量的真实全局对应截面](../results/R148-global-correspondence-section-with-diagonal-and-basepoint.md)：实际线丛的轴/对角刚性化给唯一σ，η=dκ+2FU_b及原高度差800λσ。F2在P−12指定范数框架坐标3987767，log坐标3840276；仍须加入该框架的Poincaré高度，不能设零。

- **R149（已证明）**：[最大奇同余深度上的整中心值同余](../results/R149-full-odd-depth-central-values-and-the-euler-zero-boundary.md)：每个ℓ^n||M=pg上全部稳定根、Ihara及Γ1整周期给s=0时Lalg为ℓ单位，s>0时vℓLalg≥n。全系数同余深度准确n，旧Euler≥sn不自动传成新L≥sn；非零时M整除约分分子。

- **R150（已证明）**：[实际共轭尖点微分与分母平方、立方整除](../results/R150-galois-conjugate-cusp-jets-and-cubic-denominator-divisibility.md)：同一实际非零中心值谱含≥2个归一化形式时D²|Np；a₂值非恒定时D³|Np。小house与第一不同系数零点界保留全部整性、同一尖点及系数域分歧；共同中心零和唯一有理谱仍开。

- **R151（已证明）**：[完整Miller主函数、局部联络及CM范数](../results/R151-complete-miller-local-connection-and-cm-norms.md)：完成304位454步全部真实325维主截面，终点换框、54个Lie导数及26个CM盘/完整106次典范范数均验证。指定局部值1730352mod47⁴；实际F(Du)/F(Dc7)和更换典范后的全局截面坐标已算。两CM混合形式值亦完成，仍需两条CM主函数及R148全局纤维搬运，未称已得最终高度。

- **R152（已证明）**：[最大CM同余深度与精确幺幂余核缺陷](../results/R152-maximal-cm-depth-and-the-exact-unipotent-defect.md)：ℓ^n||pg时cyclotomic核内特征零秩一余核的最小整挠长度恰n，真实Tate惯性达到；有限r≤n层的非零余核总为两份同长循环模。换格、扩系数、二次扭曲均不修复自由秩一条件，不推非挠点。

- **R153（已证明）**：[唯一有理三次谱的有效环类判别式下界](../results/R153-one-rational-cubic-spectrum-and-class-number-growth.md)：M<p时非零谱至少含两个形式；唯一非零有理谱迫Mh(O)>p(p+1)/1296，故M有效大于常数倍p^(4/3)/(logp)^(2/3)。真实整周期、Mestre范数及自含F25次数界完成；明确保留共同中心零分支。

- **R154（已证明）**：[双变量Miller搬运及同一主函数链的Hecke复用](../results/R154-double-miller-transport-and-hecke-reuse.md)：完整范数符号给m²λ=形式终点+m logf(D)+logg(AY)，Hecke第二变量可取g=N_T(fh^m/k)，无需再跑一次大整数群乘。保留实际换框、含Δ零极相消和非单位求值精度，未声称最终高度已算。

- **R155（已证明）**：[实际二阶固定除子的全部支撑及整理想](../results/R155-actual-t2-fixed-divisor-support-and-integral-ideal-at47.md)：在同一模型完整实现Q2=2P−7+Z−8，真实CM自同源/项链/Frobenius和全部截面已核；二重支点保留一阶条件，H0(2L−Q2)维177及22阶单位子式给准确整体理想。R148同步补P−7规范截面坐标4622835，仍保留范数框架高度。

- **R156（已证明）**：[CM 二同源对应与第二 Hecke 谱变化](../results/R156-cm-two-isogenies-and-nonconstant-second-hecke-spectrum.md)：完整处理导子 c/2c 及二处单位权；实际 p≡2mod3、M<p 时，以 j0 的准确带权邻域排除三次单位根坐标特征向量，自动给 a₂ 非恒定及 D³|Np。大 M/共同中心零仍开。

- **R157（已证明）**：[首次伴随反循环角色与三次分母支撑下界](../results/R157-first-adjoint-character-and-cubic-denominator-support.md)：实际 E[p]≅(y²=x³−x)[p] 的首次 p 进差异给准确导子 R 的满反循环角色；p 处整同构、2 处 Q8 与最小 Tate 惯性均处理。小 Gaussian 主理想全在核，扇区注入给 R>p³/50，不给上界。

- **R158（已证明）**：[小高斯乘积放大与超多项式分母支撑](../results/R158-small-gaussian-products-and-superpolynomial-support.md)：R157 角色核容纳互异原始小素元乘积，精确容量不等式推出每固定 B 终有 R>p^B，且 liminf logR·loglogp/(logp)²≥1。增长参数、全局单位及 CRT 碰撞完整控制，仍为下界。

- **R159（已证明）**：[整 Weierstrass 消去与准确 jet 精度](../results/R159-integral-weierstrass-cancellation-and-exact-jet-precision.md)：residual 交数 e 的单位常数模π^N由0..eN阶jet无损确定，有限代数与Neumann算法只取单位逆；重根及分歧锐例已核。给实际SLP单位递推及整盘端点因子，实际CM落实由R160继续。

- **R160（已证明）**：[实际典范代数、30个整盘及Miller公共因子消去](../results/R160-actual-canonical-algebras-cm-discs-and-integral-miller-cancellation.md)：两套106维真实典范限制代数及独立整数范数、26个CM与4个典范支点0..16阶展开全部核验；固定110位165步首一因子递推与真实端点一致。保存三个同段范数证书及两CM基点类，完整链和全局高度仍开。

- **R161（已证明）**：[严格伴随Selmer直线与实际Tate支撑正交](../results/R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md)：真实最小R=T和flat切线给严格W群零、p处全放松的对偶线维数一；实际首次差异须与该线在最小Tate支撑上正交。原Robert单位的有限域局部公式、p43真实非零与零值证书完成；多个非零项仍可相消。

- **R162（已证明）**：[小Hecke整基、CM关系清挠与完整双变量搬运](../results/R162-small-hecke-cm-relations-and-torsion-free-transport.md)：54个指标≤91的真实Hecke算子构成47整基，两个好约化群阶gcd16消去有理挠点；109个CM点/平移坐标以明确47单位整数清分母。给保留全部主函数、实际对应范数及终点换框的搬运公式，不将主函数存在当作已计算。

- **R163（已证明）**：[全部惰性p的原始伴随Robert生成元](../results/R163-all-prime-primitive-adjoint-robert-generator.md)：严格Selmer零群杀所需类群分量；在准确导子(1+i)²p上用有限Gras与辅助11的单位系数120，证明同一原始ψ11单位对每个p>37、p3mod4生成R161的真实对偶线。完整处理回到(1+i)³p的范数，未加入零Euler因子；局部零和多项抵消仍保留。

- **R164（已证明）**：[小惰性迹与联合S-unit阻碍](../results/R164-small-inert-traces-and-joint-sunit-obstructions.md)：小惰性好素数的Hasse迹迫实际首差局部零；新增真实S-unit对偶行与Gaussian行必须作用于同一惯性权重。给准确r+1维及主化算法，证明任何固定有限组行仍有无限候选零列；不误作实际曲线存在。

- **R165（已证明）**：[真实T2的CM4/CM16除子及主函数搬运](../results/R165-actual-t2-on-cm4-cm16-divisor-and-principal-transport.md)：完整Vélu、41挠点和项链给20个CM16点及Frobenius，独立负核路径逐项核验。准确粗模重数给T2Z−4=Z−4+2Z−16；两次实际AddFlip构造T2B及完整换框主函数hT，已补两Abel族八个CM形式端点的hT范数及54×3 jets，尚非完整高度。

- **R166（已证明）**：[小惯性的真实超尖商与正根数](../results/R166-small-inertia-cuspidal-positive-sign-quotients.md)：在实际Ip=C³、p2/5mod9分支构造每个连通扭曲上的非零cuspidal Q商；两个环面角色给不可约四维系统，完整局部Mackey及Saito判据给全局根数+1。R169补尖点交格，R172补非零中心值到实际秩零；非零值本身仍待证明。

- **R167（已证明）**：[整Hecke收缩与真实CM形式终点](../results/R167-integral-hecke-contraction-and-actual-cm-formal-endpoints.md)：实际N=48−T47杀J(F47)且在形式群可逆；54维整矩阵及108维整数行列式独验。由两套准确CM坐标构造mC12、mC7、NC12、NC7的八个完整Abel理想；N²非标量，不能用单纤维除N替代对应范数。

- **R168（已证明）**：[Tate Frobenius非齐次约束与Weil平方类](../results/R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md)：真实支撑单位给有限矩阵C和γ，实际首差满足γDεx=0、CDεx=Dε(q+1)/(2p^n)。单支撑内在斜率λq确定xq；判别式pvqZ及全局Weil乘数给非零平方条件。R171已给真实主化实例及λq=16，变化支撑的统一不相容性仍未证明。

- **R169（已证明）**：[尖点型商的饱和微分格与指定Whittaker行](../results/R169-cuspidal-whittaker-lattices-and-the-specified-cusp-row.md)：真实X(p)→X0(p²)拉回首系数1，单f有限类型的完整交格饱和；给同一实际尖点的完整有限特征标行公式。指定行在特征零非零，单位行充分给完整最优商形式浸入；保留跨f同余及实际商有理点有限的独立前提。

- **R170（已证明并实算）**：[真实T2的形式除子主函数](../results/R170-actual-t2-formal-divisor-transport-at47.md)：三个真实二同源的全部三阶展开、Frobenius及Hecke等式通过；另选216支撑不交的54点Abel族，构造Y=mB、T2Y两个完整理想。秩433单位核给实际kT，全部820乘法等式及有理下降核验；保留新族v/f0，尚未完成旧框架比较或非形式高度。

- **R171（已证明并实算）**：[主化轨道与自局部Tate斜率](../results/R171-principal-norm-selflocal-tate-slope.md)：p43上α=89460y+1的范数为负776位素数，ECPP/Pratt、44个带标记CM根及1848个原始Robert符号全由标准库复验。轨道公式无需除44，未分歧二次限制给准确1/2，实际λq=16并迫xq=−1；此q已被Gaussian5排除，不能冒作存活曲线或统一排除。

- **R172（已证明，保留非零值前提）**：[尖点型中心值与实际秩零商](../results/R172-cuspidal-central-values-and-actual-rank-zero-quotients.md)：真实反射与已刊大像直积给KLZ完整整余核条件；惰性非零迹和代数整数范数选出普通系数素数，准确处理共同坏处Euler因子。一般新形式的一阶Selmer消失经真实Hecke/有限中心数域的Kummer拼接推出整个有理投影像Q点有限；所用角色线须属于这个实际像，R173进一步核定其完整共轭范围。

- **R173（已证明，保留非零值前提）**：[完整有理轨道及三次子群指定行理想](../results/R173-rational-cuspidal-orbits-and-cube-subgroup-row-ideals.md)：固定μp的系数共轭使一个已有限的实际Q商提供全部原始θ共轭及两个三次方向，允许f变为fσ而保持实际尖点和剩余嵌入。两方向的整行理想之和恰为C³秩二投影的指定行理想；仍须排除与旧三色行的共同零，不由秩或迹推单位性。

- **R174（已证明）**：[指定尖点行的范数核与三色Fourier函数](../results/R174-cuspidal-norm-kernel-and-cubic-fourier-functions.md)：从同一Kirillov基及特征标表推导逐列Weyl/Bruhat范数核；固定范数上的原始字符准确落到U1/μ6，二次twist只乘列单位。m=(p+1)/6素数时，新旧共同零给完整六点函数式；一般证明不依赖有限归一化核验，合数m仍缺低阶字符。

- **R175（已证明）**：[实际CM生成元的碰撞修正Miller搬运](../results/R175-collision-corrected-miller-transport-at-cm-points.md)：以完整tame symbol证明[m]e_t=(−1)^{m(dP−db)}f[D]_t e(AY,D)，不需另算移动函数；准确接R148的j参数、两个截面坐标和初始h/终点换框。两个CM链的完整值及非形式第二变量高度仍待实算。

- **R176（已证明，固定全部支撑）**：[非线性Tate整塔与准确后阶阻碍](../results/R176-fixed-support-nonlinear-tate-lifting-tower.md)：完整Tate局部模型及所有模p^m中心化子给每级普通提升存在；恢复固定局部型的核维h、余核维h+1。单q的γ0且λ单位时每层至多唯一，实际曲线至多一个Q同源类，仍须逐层消去对偶线阻碍；不作存在性或变化支撑统一排除。

- **R177（已证明，实际应用保留中心值前提）**：[有限Weil奇偶障碍与完整尖点型行理想](../results/R177-weil-parity-obstruction-and-complete-cuspidal-row-ideals.md)：整Heisenberg代数中构造H投影，特征零秩二经整直和保持到每个好剩余域，行空间全奇；完整六点支撑式会把它送入六项算子的奇左核，而二阶递推给该核至多一维。因此全部相关有限类型与旧三色行的共同理想为单位。m=(p+1)/6素数时一个原始有理轨道已足够；实际旧商有限及一个尖点型中心值非零即迫j整。合数m仍缺proper-divisor类型与实际有限商。

- **R178（已证明并实算）**：[共同3Db整数除子及完整初始运输](../results/R178-actual-common-translation-divisor-and-initial-transport.md)：由实际KS规范证明Rω=Δ/Wω⁶，保留g1/f0换框；两个完整新理想、24步短组合及全部主截面完成。hD=Rg1²h³²⁴/Fbuild在两CM形式第一变量的实际范数均已算，给完整3m²双变量公式；共同长链与最终高度仍待完成。

- **R179（已证明并实算）**：[相离CM Hecke框架与共同形式端点](../results/R179-disjoint-cm-hecke-frames-and-common-formal-endpoints.md)：另选S使216支撑互异并避开第一变量及其T2像；实际Frobenius基变换完整保留。两CM的真实T2主函数全部820乘法式核验；3mDb、3mDu、3mDc的六个正负完整family1理想已构造，仍保留v/f0和后续非单位消去。

- **R180（已证明，非椭圆实现定理）**：[唯一flat整塔与规范晶体迹](../results/R180-flat-tate-lifting-and-canonical-crystalline-trace.md)：用flat切线规范q-unit得C̃=C−βγ；C̃可逆且首层全部惯性非零时，同一全部支撑上存在唯一完整flat+Tate表示。一般Artin系数采用协变Cartier实现，晶体迹t是完整通用参数，固定A型阻碍为其逐位检测。R171实例得到真实Z43表示但Gaussian5证明无椭圆实现；t零性与变化支撑仍开。

- **R181（已证明，中心值前提独立）**：[全部尖点参数的整行及阶四CM边界](../results/R181-all-cuspidal-orders-integral-rows-and-the-order-four-cm-boundary.md)：完整层真实整拉回及同一Whittaker泛函给全部正则参数的单位行充分判据，阶四无需全交格等式。所有r>4的实际非CM类型存在；阶四两半型的非CM重数各为(Mp−h(−p))/2，p≥2¹⁶时均正。可用实际商仍须相应中心值非零；CM张量的半单辛性排除直接套R172秩一余核条件。

- **R182（已证明，真实好特征核）**：[精确Mellin阶的Möbius算子与真实十二阶核](../results/R182-primitive-mellin-mobius-operators-and-real-order-twelve-kernels.md)：全部精确阶由同频率算子提取，m=2^a时原始列等价指定H两行消去十二点旋转差。p47、真实Tate特征ℓ1409有cubic方块核，但实际P_HR仍秩二；纯标准库证书排除自动可逆捷径，未排除原始共同非零。

- **R183（已证明并实算）**：[实际CM Hecke范数与短除子主函数](../results/R183-actual-cm-hecke-norms-and-short-divisor-transport.md)：两个实际ρT范数、两条13次真实短组合及完整73维末尾理想同构通过；FΣ=Fbuild/(g_full·(vS/f0)^93)，准确保留框架并给两范数。平移单位值由0..4e+3阶jet整精度求得；两类完整454步在各162个Hecke目标的整盘消去及真实范数4551951/945641均已完成，全部初末因子保留。

- **R184（已证明并实算）**：[完整CM主函数与实际F2高度输入](../results/R184-complete-cm-miller-functions-and-f2-height-inputs.md)：两类304位454步主函数、原框架/新S两个真实端点及全部26CM/106典范碰撞范数完成；fC0[D]_j为3560142/4417075，指定形式值4082232/207646。共同369链、真实Db端点和全范数亦完成；[最终总装](../notes/2026-11-13-r184-complete-common-chain-and-two-f2-heights.md)给F2高度差2015736/4073772，仍仅两条校准行。

- **R185（已证明并实算）**：[同一主化元及原始Robert单位的43进坐标](../results/R185-p-local-robert-and-principal-unit-coordinates.md)：固定R171同一q、α和Artin方向，规范AH基中d_q=(20,29)、d_Rob=(24,20)，行列式5。完整标记范数、无限尾及有限平坦分歧界给高单位正交线，β_q=8，校正后(0,41)且λ_q仍16；不把这些一阶局部数值称作Ω₂或晶体迹第二位。

- **R186（已证明并实算）**：[无辅助处对应的真实Hecke高度整基](../results/R186-prime-to47-hecke-basis-for-global-height-calibration.md)：有效六次循环四对应C4=T2²−3id替换旧T47行，换基系数模47为29；实际基矩阵/迹高度矩阵行列式29/18及双侧逆完整。54个全局h(B,S_iB)即可校准同一s，不除logB²，可复用已成B链；真实对应范数、切向单位和非47 Néron项仍须实算。

- **R188（已证明并实算）**：[真实Cartan标记的CM–Hecke正常水平交数](../results/R188-marked-cm-hecke-proper-intersections.md)：全部54个对应在ℓ∤2·41·n处完整枚举68256个四元数端态，有限20项链权重与实际矩阵逐项一致，得到538个非零项（512项非47）。粗模因子1/2、典范提升长度及3处整个返回核类均保留；共有分量切向自交、ℓ|2n及41分量仍待算。

- **R189（已证明并实算）**：[全p原始primal Robert生成元与精确局部配对](../results/R189-primal-robert-generator-and-exact-local-pairings.md)：在正确W(−1)型及准确导子(1+i)²p上，固定β=−1+2i的Euler因子8−4i全p为单位，明确函数4/(βx²+1)生成p全放松线；原aux11的primal投影反为零。同q全部1848值给有限坐标10、同一AH基配对(6,10)，完整flat/Tate调整与Ω₂继续。

- **R190（已证明并实算）**：[全部奇素数高度修正与3处切向自交](../results/R190-all-odd-local-height-corrections.md)：固定Z4的j−1728及尖点q41，准确生成元给3处自交总项−76；70个奇同源度项由真实准典范提升补齐。保存54行全部ℓ≠2,41,47的完整系数及四位对数和，剩真实λ47与2/41项。

- **R192（已证明并实算）**：[真实T3的CM36支撑及主函数运输](../results/R192-actual-t3-cm36-divisors-and-principal-transport.md)：四个真实三同源、同Weil根/Frobenius及40×73值给T3Z4=2Z36。删20个真实碰行后在800点图完成两AddFlip、T3B和hT3=s2f0³/s1²；最终紧凑证书保留全部函数，实际高度与93维第三类微分继续。

- **R193（已证明并实算）**：[全部54个Hecke高度的2处局部项](../results/R193-two-adic-local-heights.md)：Gross细长度、C2粗范数、四单位标记及完整quasi格分类给I2=ΣLw/4+20ρv2(n)−120ρ；56,616个Hurwitz元逐一矩阵匹配，T1/T2/T3/C4为−80/−40/0/80。偶层推前重数已独核，不用有限枚举代替几何证明。

- **R195（已证明并实算）**：[41处项与完整非47修正向量](../results/R195-level41-and-complete-non47-local-heights.md)：正确半稳定模型中ΦB=0，qST=w41及粗C2商给j切向导数41²，故I41=−40ρ；与R190/R193合并全54行，首三K为4226475/1840520/3638646模47⁴。其余实际λ47与全部QC根仍开。

- **R191（已证明并实算）**：[42次实域主化与反循环射线扩张](../results/R191-cyclotomic-principalization-and-eta-ray-field.md)：整数Norm g=−q、42个同标记根及模43⁴的完整Hensel证书给导子恰q的循环43扩张，在2/43完全分裂；直接Norm原始子保正杯积号。源与数学证书已恢复，不冒认实际Norm见证已算。

- **R196（已证明并实算）**：[实际参考Bockstein与真正Norm域](../results/R196-cm-reference-bockstein-and-the-actual-norm-field.md)：同Weil/Artin规范给差−i(κp+2κq)、精确导子p²q及实际Kummer平方化；5个Frob值保剩余次数42除数。primal圆分项与非对角块保留，完整Ω₂仍待实际Norm斜率。

- **R194（已证明并实算）**：[实际第三类微分与Poincaré校准](../results/R194-actual-third-kind-differential-and-poincare-calibration.md)：完整199/219乘积空间交为93维，RR排除共同有效部分；20CM留数、两个完整尖点域及54Lie校准共154条件全通过。低内存恢复N325/q199与旧数学对象精确同SHA，得到实际η_B，未宣称unit-root识别。

- **R197（已证明并实算）**：[前三个真实全局Hecke高度](../results/R197-first-three-actual-global-hecke-heights.md)：实际T2/T3分支迹、tiny及四类完整454步B范数同框架总装，h(B,B)/h(B,T2B)/h(B,T3B)=3623418/2463646/4692386模47⁴。非47全项、j/q41切向及终点运输保留，根独立装配同证书；余51高度及QC根仍开。

- **R198（已证明并实算）**：[p² Robert Norm及纯p secondary贡献](../results/R198-p-squared-robert-norm-and-a-secondary-contribution.md)：实际44条p²轨道、79,464值与奇度同源分布给精确Norm；同β/Weil/Artin规范得ep,q=28K和13b=−13ε。它是指定纯p primitive，不是完整Ω₂或未知L。

- **R199（已证明并实算）**：[Gaussian CM Hecke周期与未分歧支撑](../results/R199-gaussian-cm-hecke-cycles-and-unramified-support.md)：有标记局部格及单位指数2给TnZ1=ρ(n)Z1+2Σρ(n/f)Zf，C4Z1=2Z2+2Z4；全54行55导子25960去重CM点，976个n递推/次数核验。核下降不等于个体挠坐标下降。

- **R200（已证明）**：[二阶阻碍参考抵消及唯一Norm斜率](../results/R200-second-obstruction-reference-cancellation-and-one-supported-norm-slope.md)：全S/完整Kummer-zero规范下，正确Sha对偶和secondary互反给Ω₂=<wq,ep,q+eq,q>=ε(13+11v)；圆分项精确抵消，纯p贡献保留。未求v，普通Norm外支撑另有正Artin修正。

- **R201（已证明并实算）**：[S-class消失与规范Norm剩余量](../results/R201-s-class-vanishing-and-the-canonical-norm-residue.md)：相应W型S-class为零使精确S-unit Norm见证存在；完整44权及Teichmüller根修正给v=2t−12、L=21t、Ω₂=ε(10−L)。本层零恰L10；实际L仍待求，不用存在性冒认求值。

- **R203（已证明）**：[真实Hecke规范项与直接局部迹接口](../results/R203-actual-hecke-normalization-and-local-trace-interface.md)：证明g_T=M_Tg_B+dlog h_T，循环向量消除抽象非唯一性；给准确RR极点界及直接分支迹方案，保真实1/ℓ和含极点盘整性。新的分支jets及剩余51高度尚未完成。

- **R204（已证明并实算）**：[primal二阶Frobenius与完整Euler逆](../results/R204-primal-secondary-frobenius-and-full-euler-inverse.md)：完整T角色投影及DE⁻¹=e⁻¹D−kbe⁻²N给固定{2,p}标记参考的Frob_q=24F0；两辅助各79,464值一致，正Artin/τ下降独立核准。保持参考的L互反桥仍缺，24不冒认实际L。


- **R205（已证明并实算）**：[清极点Serre导数与真实Hecke目标ODE](../results/R205-cleared-serre-derivative-and-actual-hecke-target-odes.md)：52个覆盖非椭圆点的清极点截面及73列三次式全部3112720等式通过；源盘和实际T2第三支0..3阶478880值独立吻合。准确保留KS的1/2及实际权二尺度；椭圆粗盘与其他新分支仍须处理。

- **R206（已证明并实算）**：[五个超奇异参考模型及实际41水平传输](../results/R206-supersingular-reference-atlas-and-actual-level41-transport.md)：完整Hasse多项式分解给全部j=0/9/10/36/44；R80上真实41基、Weil根及项链共轭保留，三个完整纤维和60个CM点共183960值独立吻合。现执行器覆盖9/10/44，椭圆盘由R208继续，不把项目坐标冒认实际权二值。

- **R207（已证明并实算）**：[实际射线扩张的Gaussian迹43次整模型](../results/R207-gaussian-trace-model-of-the-actual-ray-extension.md)：同一标记Kummer数据的正指数迹给q-Eisenstein整元；1325素数CRT、严格27435bit系数界及三个未用素数确定完整43次多项式。根独立C++两行和完整Node核验相同；Norm为q单位时剩余值恰常数项，实际Norm见证及L仍未求。

- **R216（已证明并实算）**：[五个超奇异参考纤维的真实标量原函数](../results/R216-scalar-primitives-on-all-five-supersingular-reference-fibres.md)：4079普通层标号、21椭圆coarse盘、16可去分母全部恢复；5×5单位方程不损失47进位，二十CM4真实留数一及log u保留。实际同源端点独立复现首三tiny，完整216KB证书落盘；余51高度及全部QC根仍开。

- **R214补强（已证明）**：共同导子在域判别式支撑上的部分 $(bc)_D\mid36$；分歧二进域上中心平凡二阶单位角色杀死 $U_4$，故 $b_D\mid4$，结合 $c_D\mid9$。不把这一结论误写为整个 $b\mid36$。

- **R213（已证明）**：[实际深度零角色的变判别式统一非消失](../results/R213-actual-depth-zero-uniform-central-nonvanishing.md)：逐处匹配Pi已发表相对迹公式，在p处分歧的真实Ω上得到准确正谱与p|y支集；重新作变化域整数倍计数，给有效统一p≥Cε(Da²)^(1+ε)/h(Oa)。准确保留共同导子a=c或bc及D支撑界36；r>4自动非CM，阶四谱仍需过滤。

- **R215（已证明）**：[正Hecke卷积剔除CM及辅助素数平方代价](../results/R215-positive-hecke-filter-and-quadratic-prime-cost.md)：实际阶四谱插入h2+(q+1)h0，谱权为a_q²，惰性q杀全部CM；分裂双环面的完整赋值计数给q²几何代价和显式变化导子误差。无需额外指定q在K的分裂型；稳定范围p≥q²M或有效类数范围均给真实非CM中心非消失。

- **R217（已证明）**：[多个小非剩余避开变化导子及实际非CM范围](../results/R217-many-small-nonresidues-avoid-changing-conductor.md)：Pollack多素数定理与ω(B)≤log B/log2避开任意多项式坏集；接R215真实q²正Hecke估计，得到p≥CνM^(1/(2−1/√e)+ν)的阶四非CM中心非消失，q>M时直接稳定范围。共同导子bc和Siegel无效性均保留，纠正旧γ/β混用。

- **R209（已证明并实算）**：[全部54索引的实际互素核DAG](../results/R209-complete-coprime-kernel-dags.md)：在次数≤44的有限étale商环运输完整互素核，不构造个体挠点大域；两源各3282目标、升降序全部2422对应复合核模型一致。C4严格删去对偶核；完整核、路径、源目标模型及哈希已落盘，实际水平和高度继续。

- **R218（已证明并实算）**：[deRham拉回初值及三变量四阶同源方程](../results/R218-isogeny-de-rham-pullback-and-quartic-odes.md)：完整微分恒等式给φ*η=nη−uω与u复合律；函子性导出三变量ODE，1至4皆47进单位，故实际变形四阶唯一。两源各3326模型已落盘，各27条含43/89的独立ψ隐式提升全同；避免逐大核重复提升，真实高度仍继续。

- **R219（已证明并实算）**：[一个精确普通实单位Norm目标及真实Galois标号](../results/R219-single-real-norm-target-and-galois-labels.md)：识别σ33的Möbius变换并证明普通z不是Norm；完成σ(z)与44个共轭的有理商环核验，生成单个Q(z)普通实单位U的全部44系数。普通实X、NX=U存在，21个准确剩余符号给L；原像X与L仍待求，未以存在性冒认完成。

- **R220（已证明）**：[共同导子的伴随表示与全局二次扭曲导子](../results/R220-common-conductor-adjoint-and-quadratic-twist-level.md)：有限伴随Artin导子恰p²D M*；单个全局扭曲给p²R²T及显式二三因子。实际j分子直接决定三/四阶惯性支撑；将全部非整j的共同导子下界转为Ntw≳D p^(5−1/√e−δ)，不冒认导子上界或整j排除。

- **R221（已证明并实算）**：[完整实际水平运输与端点极点消项](../results/R221-full-level-transport-and-actual-endpoint-cancellation.md)：两源各3326节点raw φP/φQ及det=n全核；54索引177228行积分已求，538真CM4极点的四阶单位余项保留。静态1076个D0碰撞逐标签/物理参数恰为两倍极点，七个无极点tiny完整；静态单位范数及51高度继续。

- **R223（已证明并实算）**：[近CM4点的选择性六位核提升与四位单位对数](../results/R223-selected-CM4-kernel-lifts-and-unit-logarithms.md)：200具体目标仅需167源核、313祖先目标，ψ Newton与完整特征多项式逐核核验，并全部回投原DAG。log u及log(j−1728)四位已保存，54索引Frobenius封闭；关闭R221的补位缺口，完整单位范数仍继续。

- **R224（已证明）**：[光滑理想检测及实际整j四阶支撑增长](../results/R224-smooth-ideal-detection-and-integral-j-conductor-growth.md)：固定K的指定二次Frobenius小素数界q≪|D_F|^(1/(2√e)+ε)有效且避多项式坏集；完整Euler填补和光滑理想证明不给变化K偷用固定常数。K=−3,c6/9整j非空四阶支撑增强为Q0≳p^(2√e−ε)、N≳p^(2+4√e−ε)，主问题仍开。

- **R225（已证明）**：[三次光滑理想与变化导子的统一有效增长](../results/R225-smooth-cubic-characters-and-uniform-conductor-growth.md)：八个hK1且K≠−3域的实际导子c≳εp^(κ3−ε)，κ3=(e^(2/3)−1)/4；类数同指数、Dc²双指数。完整保留模c分班边界、小自变量及Euler坏集误差，包含全部exceptional与整/非整j；仍是下界。

- **R222（已证明并完整实算）**：[完整Miller范数、54个全局高度与实际迹系数](../results/R222-complete-miller-norms-and-all54-global-heights.md)：4100点单位atlas和3282实际CM目标保完整454步因子、终点运输、D0换参及近CM4对数；全部54高度及s=H⁻¹h已算，det18、无精度损失。前三准确复现R197，独立CM矩阵复现R184全局差4073772；全部QC局部函数和共同根继续。

- **R226（已证明）**：[二部分类型与分离的共同导子整性门槛](../results/R226-two-primary-types-and-separated-conductor-thresholds.md)：准确按v₂(p+1)分配c或bc；p≡1mod4全部所需类型自动非CM，p≡7mod8唯一阶四仅看c，M*只支付平方根指数。非整分支的近平方M*或M的γ次替代条件保留逻辑“或”，仍无上界。

- **R227（已证明）**：[坏二进位的正Hecke滤波与完整3mod8分支](../results/R227-dyadic-positive-filter-with-ramified-toric-character.md)：在相同Gross–Prasad共轭极大序插入正T₂²，允许2|D或2|a；直接壳积分主项至少1、完整regular计数和4M支集给有效统一M^(1+ε)/h。整个p≡3mod8分支整性改善为M*平方根范围，非整M*近平方及Ntw近p⁵下界仍不代替上界。

- **R219忠实Norm补充（已证明并实算）**：[实际Norm见证的全域必要性及六个线性试解排除](../notes/2026-11-13-o6-faithful-norm-witness-and-linear-probe.md)：eχ[U]=29eχ[z]非零迫任何NX=U见证生成完整L，真K子域元素乘积及43次幂均不足。6343处精确赋值及859²处六个幂剩余排除z−aθ的底域43次修正；不排一般Norm解，不冒认已求L。

- **R228（已证明并实算）**：[全部QC全局多项式与110有理超奇异粗盘](../results/R228-global-QC-polynomials-and-rational-SS-disks.md)：53方向完整800二次/线性平移及四个联合坏靶已算；R184两条独立CM高度差2015736/4073772全同。3154几何粗点精确去重给110有理盘，真正Q47中心及三阶73/199/325坐标保存；尚未补的大Abel常数、局部高度及共同根保持开放。

- **R229（已证明）**：[Hecke Burgess、三次小素理想与更强实际导子增长](../results/R229-cubic-hecke-burgess-and-stronger-conductor-growth.md)：使用Yang已发表固定数域3/16界，完整变化Euler坏集和指数平滑给指定三次非剩余Np≪Q^(3/(8e^(2/3))+ε)。八个实际类数一域的c、h有效下界指数升至(2/3)e^(2/3)−1=0.2984893607，保留固定域范围和同一实际差角色。

- **R230（已证明并实算）**：[循环Lie坐标、110盘真实全纯积分与三个CM常数](../results/R230-cyclic-Lie-coordinates-and-all-SS-tiny-integrals.md)：54维单位Lie/八域双向矩阵、全部110盘54微分和tiny积分已求；CM3独立KS三阶匹配。三个CM盘完整Abel常数及53全局四次多项式精确复现，余107常数及真正局部QC高度仍须另求。

- **R231（已证明并实算）**：[全部十九普通点及完整129盘真实坐标](../results/R231-all-ordinary-reference-points-and-complete-residue-atlas.md)：次数120/280/840半域中的实际41水平、准确20/k迹与Gauss朝向给全部19四位普通中心及三阶jets；独立73物理值和51319二次恒等式全过。合R228关闭全部129盘坐标，普通大Abel常数、局部QC高度与共同根仍须继续。

- **R234（已证明并实算）**：[全部超奇异真实Hecke图、右端及129盘tiny](../results/R234-actual-SS-Hecke-graph-and-Abel-right-hand-sides.md)：3154几何粗点、49真实核及22078完整73坐标目标检查全过，两个实际Hecke右端及完整相容式已求；全部129盘54维tiny完整。尚未以线性系统代替常数或局部高度，求解见后续R235。

- **R235（已证明并实算）**：[联合Hecke方程及全部超奇异大Abel常数](../results/R235-complete-SS-Abel-constants-from-joint-Hecke-equations.md)：P(A2+2A3)真实秩3153的一维核由联合约束唯一消去，无精度损失求全部3154几何中心及110有理中心54维常数。两个原方程、三独立CM及全部有理虚部核验通过，CM锚未参与求解；真正局部QC高度及根继续。

- **R237（已证明并实算）**：[三个普通CM常数与113盘全局高度函数](../results/R237-three-ordinary-CM-anchors-and-113-global-functions.md)：判别式−11/−19/−67的全部289项有理路径关系、实际物理CM点和全73坐标已核，给ORD_j38/39/40的54维中心常数；合R235完成113×53个全局四次函数，三旧CM盘独立复现。其余16普通常数和真正局部QC高度/共同根继续。

- **R232（已证明）**：[实际二次迹域及线性小素数障碍](../results/R232-quadratic-trace-field-and-linear-prime-obstruction.md)：p≡1mod4或Gaussian域的同一真实迹范数给p<9q，扩大三次角色恒一窗口至p/10；Hecke Burgess得到有效c、环类数增长指数1.5969787214及扭曲导子指数5.1939574428。整/非整j均覆盖，仍为必要下界。

- **R233（已证明）**：[实际二次差角色与统一共同导子增长](../results/R233-quadratic-difference-character-and-common-conductor-growth.md)：同一σ=ν⁶把实二次判别式与b比较，测试素数可进入c，七域σ非平凡得b指数√e；合三次界给八个非−3类数一域bc统一指数1.5969787214。K−3非平凡σ得b指数2√e，取消旧c6/9及整j限制，未关闭全局上界。

- **R219-H90（构造已证明，演示实算）**：[实际Norm-one单位到普通实原像的Hilbert–90接口](../notes/2026-11-13-o6-constructive-hilbert90-checkpoint.md)：固定χ/τ投影及q处1保证求和Z非零且实，若NZ=U^cB43且c非零则显式X为普通单位；同一L读数只需底域B。底域43次根提取器已由全局精确等式验证演示，实际混合单位与Norm原像仍缺。

- **R239（已证明并实算）**：[同一Artin标号中的短实单位Norm目标](../results/R239-short-real-unit-target-and-exact-gauge.md)：精确双向域映射给z=ξ⁴，全部44正σ共轭和τ兼容；U=V15⁸=V7¹¹B7⁴³=V42⁹B42⁴³。全部42等价目标已算，最短固定幂基分子543bit，V7的完整L读数因子为1并保留−3修正；未取得上域原像。

- **R240（已证明并实算）**：[实际第二类联络微分与108维整deRham基](../results/R240-actual-second-kind-connection-and-integral-de-Rham-basis.md)：同一R141/R145框架内，以161维实际RR空间解54单点双极/零留数微分，Ω1 B Ω2ᵀ准确校准，8748原方程及Frobenius全部通过。与全纯基的杯积−Ω2为单位，给完整108基；其大积分及真正QC高度继续。

- **R236（已证明）**：[校正二次扭曲投影与剩余阶四非CM非消失](../results/R236-corrected-quadratic-twist-projector-and-order-four-noncm-nonvanishing.md)：逐处固定点符号、Deuring准确计数及混合相对迹给无辅助素数的非CM正谱；两个奇异轨道均零，误差仍E，阈值只倍增。全部小惯性分支统一为M*平方根整性范围，非整共同导子近平方下界，仍非绝对一致性。

- **R241（已证明并实算）**：[精确原生消元与全部19普通基点差](../results/R241-exact-native-elimination-and-ordinary-based-points.md)：F47²整数消元保持原主元、Newton逆及完整核检查；真正AddFlip的新旧点/下降/witness/PRNG完全一致，root复现。共同74维colon给19个实际P−b，保留f_b/f0；16盘长链逐位checkpoint继续，未提前记对数完成。

- **R242（已证明并实算）**：[全部第二类微分的实际Hecke运输](../results/R242-actual-second-kind-Hecke-transport.md)：由真实deRham初值恢复四条目标一阶值，两套54主函数分子与R141旧SHA完全相同；T3ν=νMᵀ+df的39852等式在738点成立，超过646次数界，给模47⁴全局验证。保留图方程恰当微分与极点有限部，实际大积分继续。

- **R238（已证明）**：[二进最优嵌入符号与统一非CM门槛](../results/R238-dyadic-optimal-embedding-sign-and-unified-noncm-threshold.md)：两个二进交序的准确固定类数(h−1)/2、(3h−1)/2及1728半数修正给共同CM负号；同一正投影覆盖p≡3mod8，不扩张二进Hecke支集。全部实际类型统一有效系数5184及准确类数阈值，整j和共同导子上方控制仍开。

- **R248（已证明并实算）**：[实际终点运输与普通第二类大积分](../results/R248-actual-terminal-transports-and-ordinary-second-kind-integrals.md)：820×73完整理想恒等式核对真实终点，保留v1/f0、454步函数和规范导数；首盘ORD_j05全部108积分模47⁴完整，457实际函数及协变检查入库。其余普通/SS大积分、真实局部高度和共同根继续。

- **R243（已证明并实算）**：[完整单位Norm核与无条件43饱和](../results/R243-complete-unit-norm-kernel-and-43-saturation.md)：22个首一整单位证书及实际有限符号行列式12给全单位43饱和，q符号秩19、核恰由ε/V42/新χ±8单位W生成。H与F的元素Norm指数准确43^19/43^38，root标准库重算全过；普通上域原像和L仍未取得。

- **R246（已证明并实算）**：[全部超奇异盘上的第二类移极点](../results/R246-second-kind-pole-removal-on-the-complete-SS-atlas.md)：实际127维colon及54主部构造完整移动函数，41364评价和两个完整尖点域给μ=(ν+dF)C的有理正则表示；w在3154SS全单位。真实T3矩阵与270点简单分母完整保存，大积分和局部QC继续。

- **R245（已证明）**：[分裂加性导子素数的惯性归一化](../results/R245-split-additive-conductor-primes-and-inertia-normalized-traces.md)：同一实际局部Frobenius先消相位，再比较真实普通CM约化域；指定三阶/四阶支撑给q>p²/16，其余分支给p/4或p/9。七个非额外单位域的新分裂共同导子素数统一大于p/9，整/非整j均覆盖，仍无上界。

- **R249（已证明）**：[经实二次诱导闭合CM中心值秩零](../results/R249-cm-rank-zero-through-real-quadratic-induction.md)：实际四维系统诱导自平行权二、平凡中心角色Hilbert CM形式；完全分裂辅助ℓ的惯性明确实现Nekovář B(c)，准确Shapiro/Kummer给非零中心值实际有限商。全部共同导子整性有效系数回到2592，保留中心值前提和主目标缺口。
