# R1–R79 分段证明导航

主目标未完成。返回[结论索引](../results.md)。以下原条目及适用范围完整保留。

- [R1：初级有限性与量词](../results/R1-primary-finiteness-and-quantifiers.md)：证明 Selmer 余秩判据；明确全群有限还需有限支撑，校正解析秩与代数秩的混淆。
- [R2：固定曲线的秩至少为 2](../results/R2-explicit-rank-two-curve.md)：对 $y^2+y=x^3+x^2-2x$，用模 $5,7,11$ 的有限域证书证明两个点独立。
- [R3：二次 cyclotomic 系数判据](../results/R3-cyclotomic-coefficient-criterion.md)：对已知秩至少二的曲线，严格推出 $[T^2]L_p\ne0$ 时初级有限；跨素数非零性尚未证明。
- [R4：固定 CM 曲线精确秩二](../results/R4-cm-rank-two-curve.md)：对 $y^2=x^3-17x$ 展开二次同源下降、核与指数计算，证明秩恰二；模 $41$ 证明两点独立。
- [R5：统一有限抬升的计数障碍](../results/R5-uniform-lifting-obstruction.md)：用 Chebotarev 和扭点计数反驳一个强声称来源的中间引理，不声称否定其最终 BSD 类命题。

- [R6：CM 迹的精确递推](../results/R6-cm-trace-recurrence.md)：采用 CLS 勘误后的特值公式，将分裂素数路线具体化为固定迹序列第 $(p-3)/2$ 项模 $\mathfrak p^4$ 的非消失。
- [R7：同源、基变换与类群公式](../results/R7-isogeny-basechange-primewise.md)：证明逐素数同构、统一非异常性及 $\dim\operatorname{Sel}_p=2\lceil c_p/2\rceil$；$c_p\in\{1,2\}$ 等价于初级部分为零，尚未证明其无穷性。
- [R8：strict Selmer 的实际缺项](../results/R8-strict-selmer-comparison.md)：给出已知两点的 strict 向量及含 Tate–Sha 的精确正合列；明确广义 Kato 类非零比较所需的信息。
- [R9：同步权重的整除与增长](../results/R9-synchronized-weight-divisibility.md)：证明同步素数约束的精确整除与 $o(n\log n)$ 增长；这一乘积公式尝试尚不足以给出大小矛盾。
- [R10：超奇异二次系数判据](../results/R10-supersingular-quadratic-criterion.md)：用 Pollack–Rubin 的已发表定理证明任一 signed 二次系数非零足以给初级有限。
- [R11：统一有限模型的精确界限](../results/R11-uniform-finite-models.md)：统一有限域杀死全部 Sha 等价于全群有限；全部代数点模挠后的不变空间恰为 Mordell–Weil 有理化。
- [R12：两个类群实现的同构](../results/R12-relative-classgroup-comparison.md)：以范数、共轭和整投影证明 R7 的 $c_p$ 等于单个除法域的相对类群维数 $r_\pi(E)$，没有修正项。
- [R13：CM 迹序列没有固定阶线性递推](../results/R13-cm-trace-nonholonomicity.md)：利用椭圆函数的无穷多个极点排除最终多项式系数线性递推；不排除随素数变化的对角项模 $\mathfrak p^4$ 公式。
- [R14：椭圆指数叶的闭合条件](../results/R14-elliptic-exponential-pclosure.md)：直接计算 Bost 型叶在所有普通素数处不满足 $p$-闭合，故这条具体代数化尝试不能直接使用其定理。
- [R15：有限分支同步的整除界](../results/R15-finite-branch-synchronization.md)：有限个固定权重中心和固定多项式移位仍只有 $O_\varepsilon(n^\varepsilon)$ 的对数整除预算；精确区分同一整数的最大值与独立整数的乘积。
- [R16：局部椭圆单位深度判据](../results/R16-local-elliptic-unit-criterion.md)：给出一个具体单位格生成元，证明局部深度 $\nu_p\ge2$ 且 $\nu_p\le3$ 时 $\Sha[p^\infty]=0$；所需无穷次上界尚未证明。
- [R17：素数对角项的四层归约](../results/R17-cm-prime-diagonal-four-layer-reduction.md)：用形式留数把模 $\mathfrak p^4$ 的目标写成四个固定级数的系数；逐项证明截断整性并区分最低层与三个非 D-finite 对数层。
- [R18：最低层有理化与固定 Fermat 商](../results/R18-rational-layer-and-fixed-fermat-quotient.md)：以 $P\mapsto(0,0)-P$ 配对，证明 $R(t)=\operatorname{Tr}_{M/K}(\alpha/(1-\alpha^2t^2))$、$\operatorname{Tr}\alpha=0$，最低项除 $p$ 是固定代数数的 Frobenius–Fermat 商之迹。
- [R19：统一固定函数的对数矩与单位值](../results/R19-fixed-rational-logarithmic-moments.md)：构造 $\Phi=N(1+\alpha t)/N(1-\alpha t)$，证明 CLS 特值的精确对数矩公式，以及 $\Lambda/\Lambda\circ[-1]$ 与 $\Phi$ 的有理函数恒等式；局部字符深度不变。
- [R20：两种判据的截断赋值比较](../results/R20-local-depth-and-critical-value-comparison.md)：证明 $\min(\nu_p,4)=\min(v_p(c_p^+),4)$，所以 $v_p(c_p^+)\le3$ 时整个初级部分为零；尚无无穷次上界。

- [R21：tame 参数的三个对角项](../results/R21-tame-coordinate-three-term-formula.md)：证明局部字符对数模 $p^4$ 只需三个对角项，完整处理系数分母与无限尾项；首项准确等于 CLS 特值的单位倍数。
- [R22：固定有理函数不能除去中心因子](../results/R22-fixed-rational-division-obstruction.md)：证明有限 étale 自映射的除子支撑障碍，排除用一个固定有理函数解 $F([69]P)/F(P)^{69}=C\Phi(P)^N$；不排除局部 Iwasawa 模中的除法。
- [R23：乘法坐标下的函数超越性](../results/R23-multiplicative-coordinate-transcendence.md)：在任意特征证明非零形式群同态 $\widehat{\mathbb G}_m\to\widehat E$ 拉回每个非恒定椭圆有理函数都超越；直接套用有理函数 Mellin 输入不成立，已知椭圆 $\mu=0$ 不受影响。
- [R24：显式局部基与双权有限判据](../results/R24-multiple-weight-finiteness-criterion.md)：以严格 LT 坐标构造局部单位塔基，证明全部相关权的精确对数矩赋值比较；$\min(v_{\mathfrak p}a_{(p-3)/2},v_{\mathfrak p}a_{p-2})\le3$ 足以给初级有限，同时失败恰为 $g_0\in p^2,\ g_1\in p$。
- [R25：$\lambda$ 控制有限 Selmer](../results/R25-lambda-controls-finite-selmer.md)：以 $\mu=0$、原始 Galois 模无有限子模和准确注入证明 $\dim\operatorname{Sel}_p\le\lambda(H_p)$；$\lambda\le3$ 及双权判据均加强为整个初级部分为零。
- [R26：极大理想阶的统一界](../results/R26-maximal-ideal-order-and-finite-selmer.md)：给实际矩阵表示及 Schur 补证明 $\dim\operatorname{Sel}_p\le\operatorname{ord}_{(p,T)}H_p$；Vandermonde 公式以有限个权准确检测 $G_p\in(p,T)^n$。
- [R27：准确 Selmer 控制与 Smith 公式](../results/R27-exact-selmer-matrix-control.md)：证明非异常处 usual 与 extended 群相同；有限维数为 $T$ 作用矩阵模 $p$ 的余核维数，无穷余秩为其中心特征空间维数，Smith 分解确定 Sha 的有限商。
- [R28：中心差分逆像不代数](../results/R28-algebraic-difference-inverse-obstruction.md)：将 R22 加强到任意代数形式函数，通过稳定有限覆盖、Riemann–Hurwitz 和除子下降证明；尚未得到所需代数化定理的算术输入。
- [R29：两个固定级数给四层 Frobenius](../results/R29-two-fixed-series-frobenius-truncation.md)：以固定 $\mathscr L=\int_0^X(1+u^4/68)^{-1/2}du$ 及 $\mathscr L^5$ 给整个仿射部分模 $p^5$ 的有限截断，证明 $C_pY_p\equiv\bar\pi\pmod{p^2}$；不在单位点代入无限形式对数。
- [R30：中心类群与高阶 Fitting 判据](../results/R30-central-classgroup-and-higher-elliptic-ideals.md)：证明无穷 Selmer 余秩为 $2\lceil q_p/2\rceil$，初级有限恰当且仅当 $\operatorname{Fitt}_{\Lambda,2}(\mathcal A_p)\not\subset(T-p)$；允许任意大的非零中心赋值，且给有限 Sha 商的准确 $p$-秩。
- [R31：固定单位的分母值公式](../results/R31-fixed-unit-pade-denominator.md)：用固定辅助理想 $(67)$ 及完整 Theta 常数证明 $D_p(\alpha)^{53856}=\sigma_{\mathfrak p}(w)/w^p$，其中 $w\in M^\times$ 不依赖 $p$；这控制指定值的全部层，尚不替代目标高阶矩。
- [R32：Rubin–Stark 有限层证书](../results/R32-rubin-stark-finite-layer-certificate.md)：仅用已出版 Bley–BKS 定理，以固定修正素理想 $(67)$ 给完整类群模的高阶 Fitting 理想；初级有限恰为某层秩三外积值在 $T=p$、模 $p^n$ 非零。

- [R33：中心类群的增长证书](../results/R33-central-classgroup-growth-certificate.md)：中心有限商准确为 $D_p/p^nD_p$；阶数增长单调下降，某层满阶循环因子至多两个即给初级有限，并比较增长证书与 Rubin–Stark 值理想所需精度。
- [R34：严格 Selmer 与中心类群的奇秩](../results/R34-strict-selmer-and-odd-central-classgroup-rank.md)：严格群准确由处处无分歧中心商对偶给出；固定非挠点使局部 Kummer 像满射，故 $s_{\infty,p}=q_p+1$、$q_p$ 为正奇数，有限性恰为 $q_p=1$，只需一个辅助素数的 rank $2$ 证书。

- [R35：已知严格 MW 线选择单辅助类](../results/R35-single-auxiliary-prime-and-strict-mordell-weil-line.md)：固定两点给饱和满射 $\lambda_p:D_p\to\mathbb Z_p$；检测其模 $p$ 的任一分裂辅助素数已实现完整第一 Fitting 中心理想，剩余核与 Sha 的有限 MW 误差有准确正合列。
- [R36：两条整 Bockstein 泛函与一个确切非零值](../results/R36-two-bockstein-functionals-and-a-nonzero-value.md)：以局部 LT 坐标和辅助赋值各除一次中心，实际 rank2 值为 $p^{b_p}u_nG_{p,n}$；在 $p=13$、辅助素位 $(109,i-76)$ 得到 $3\bmod13$，附纯有理数及有限域复算脚本。尚缺跨素数非零性。

- [R37：CM 互易式与反对称高度非零](../results/R37-cm-period-reciprocity-nonvanishing.md)：将特定 universal-extension 行列式化为广义 Jacobian 的线性对数，证明全部目标素数处非零；反 cyclotomic MW 配对行列式为非零的 $j_p^4$，尚不控制额外 Tate–Sha 方向。
- [R38：sigma 的准确惰性大小](../results/R38-exact-inert-sigma-size-and-jet-budget.md)：证明 $S_p=p^{-p/(p^2-1)}$、无限分母列的准确赋值及全部二次正规化的最优大小；固定坐标 jet 总量恰为 $\tfrac12\log k+O(1)$。
- [R39：四个 CM 高度的线性 period 表示](../results/R39-cm-height-linear-period-matrix.md)：同一五维广义 Jacobian 和两列代数点给三个 cyclotomic 高度及反对称值的全部代数线性独立；剩余 regulator 为明确二次式，strict 自高度为三次式。

- [R40：完整 Selmer 的反圆分二阶判据](../results/R40-anticyclotomic-second-coefficient-and-full-selmer.md)：把已证反对称 MW 非退化放入已发表完整 Selmer 主项公式，得到初级有限当且仅当实际 Katz 分支二次系数非零；剩余 Sha 块为交替形式，中央临界值的某层赋值小于 $4(n+1)$ 是准确有限证书。
- [R41：两个独立乘子的共同深度可求和](../results/R41-two-multiplier-common-depth-summability.md)：以统一短关系乘积同时覆盖全部提升深度，再用惰性 norm/angle 阶数分解，证明共同质量 $O(k^{3/4})$、全部共同大小损失可求和；尚须实现接受这套估计的固定非代数 germ。
- [R42：互素 CM 差分的有理共同原函数](../results/R42-coprime-cm-difference-primitives.md)：以有限极点数据、精确深度分层和升层左逆证明，两个无 twist 的有理差分幂迫使任意复 Laurent germ 属于原椭圆函数域；无需实系数或有限覆盖。
- [R43：常数 twist 的共同原函数分类](../results/R43-twisted-cm-primitive-classification.md)：完整分类两互素 CM 标量差分幂；除椭圆有理函数外，只保留整数权 $z^k$ 或反 CM 字符的 $\zeta$，高次幂不增加广义特征项。
- [R44：中央对角的完整系数预算](../results/R44-central-diagonal-global-coefficient-budget.md)：全权 Gauss 界与两类真实分母列给出准确 $\mathcal B(k)=2\log k+O(1)$，普通和惰性各贡献一半；只排除以该截断系数预算直接达到代数化门槛，不替代真正评价映射的估计。

- [R45：最低中央迹及统一首层分母](../results/R45-lowest-central-trace-and-uniform-first-denominators.md)：严格分母与复界加模$3^{24}$证书给 $d_1=64(-1+i)$、$e_1=4/17^3$；所有好普通处的 $m\equiv1$ 列有准确阶乘赋值，所有惰性$p\ge7$的 $e_{p+2}$ 赋值均为$-2$。
- [R46：固定 sigma 截面与中央 Mellin 因子](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)：由 Yang 一般 theta 范数公式构造固定 $S=P(x^2)\sigma^{L^2}$，证明中央系数的范数公式和实际整条 Katz 分支的两个 Mellin 因子；有限性等价两个中心零阶之和为二，尚未证明无穷性。

- [R47：中央Borel模形式及准确复增长](../results/R47-central-borel-modular-form-and-exact-growth.md)：全权Borel变换来自固定权一模形式，边界圆无亚纯延拓；原中央整函数的阶与型均准确确定。
- [R48：实theta结构与中心斜率判据](../results/R48-real-theta-structure-and-central-slope-criterion.md)：明确17处Gauss积分及全局CM伸缩，使整条分支成为一个实际Mellin因子的平方；中心均零，初级有限准确等价一阶导数非零。
- [R49：次数十七的有理theta截面](../results/R49-degree-seventeen-rational-theta-section.md)：直接核2处向量，保留奇半特征后下降到四参数截面；十维精确行列式证明归一参数全有理，完整分支的伸缩指数为log〈136〉。
- [R50：惰性中央值的整周期比较](../results/R50-inert-central-integral-comparison.md)：用秩零参考曲线的实际signed原始基消去共同周期；所有惰性p≥7有中央整性，且 $v_pd_{p+1}\le1$ 足以初级有限。混合权二变量图、阶乘及非单位Euler抵消均已核。
- [R51：实际theta截面与准确平方常数](../results/R51-explicit-theta-section-and-central-square-constant.md)：全局中央迹唯一重构和严格Gaussian区间两证书确定三个参数为 $(51/5,-289/5,4913/5)$、常数57800；得到低阶挠点sigma乘积、全部目标素数的准确平方赋值及普通整测度尾界。
- [R52：惰性prime diagonal与真实连接](../results/R52-inert-prime-diagonal-and-theta-connection.md)：同一固定有理级数 $\Xi=(\Theta^{17}P)'/F$ 的指定模p系数给充分判据；证明整条Xi非D-finite及自然连接的常数矩阵维数障碍，不排除该对角另有Frobenius公式。

- [R53：有限挠点与模形式的除p jet](../results/R53-finite-torsion-and-modular-divided-jets.md)：固定17点 Fourier 基准确恢复惰性首权；构造实际整 holomorphic $V_p$，其 CM 值给 $((p+1)!/p)b_{p+1}$。modp² 提升信息不可由固定挠点置换丢弃。
- [R54：惰性解析半因子与中心斜率](../results/R54-inert-analytic-half-factor-and-central-slope.md)：构造实际过收敛 $\mathcal J_p$，证明 $\operatorname{ord}A_p=2\operatorname{ord}\mathcal J_p$；首导数非零足以初级有限，首层与 $b_{p+1}$ 单位准确等价，导数有明确有限尾界。
- [R55：普通固定对数级数与有限权证书](../results/R55-ordinary-fixed-log-series-and-weight-certificate.md)：同一固定 $G_{\rm ord}$ 恢复 $b_{p-1}/p$；完整 Newton 差分及尾界用有限个正权准确检测真正 $J_p'(0)$。
- [R56：普通斜率的无周期有理极限](../results/R56-ordinary-period-free-hurwitz-limit.md)：证明实际 $J_p'(0)\in\mathbb Z_p$，并由 $(m_n-1)!b_{m_n}$ 以明确 $p^{n+2}$ 误差恢复；单权赋值低于 $n+2$ 是完备有限证书，仍未证明跨素数非零。

- [R57：全局Hurwitz整数与固定多项式流](../results/R57-global-hurwitz-integers-and-fixed-polynomial-flow.md)：实际 $h_m=m!b_m$ 全为整数；无分母多项式ODE和真实sigma乘积给完整证明，普通有限性准确成为某层 $v_p(h_{(p-1)p^n})<2n+2$。整数性尚不给跨p上界。

- [R58：统一整数对角与准确固定除子](../results/R58-unified-integer-diagonal-and-exact-fixed-divisor.md)：同一 $a_r$ 在 $r=(p-\epsilon_p)/4$、$\epsilon_p=(-1/p)$ 总被p除，恰一次整除足以两类初级有限；证明 $\gcd a_r=24$，并准确识别整个Euler原函数在普通非目标权的分母p。

- [R59：固定同源参考与惰性归一行](../results/R59-fixed-isogeny-normalized-inert-rows.md)：实际商在原椭圆曲线上有理，构造完整十七行与严格尾界；纯对数分解的整体常数由零迹消去。同开集恰当微分检查保留实际参考连接，尚无所需周期比较。
- [R60：秩零参考与纯有理Newton证书](../results/R60-reference-normalized-rational-newton-certificate.md)：用实际参考单位消去普通周期，线性最高权给完备证书；再以二次权增长消去Euler数据；同一实际A的四阶导数参考使输入缩成一个整数序列的相邻项。p13归一核查根端通过，跨p非零仍开。

- [R61：canonical 热行与固定 Miller 范数](../results/R61-canonical-heat-row-and-fixed-miller-norm.md)：实际中心零整格上的除p行良定；类型与纯dlog二维子空间已算出，短周期固定单位和完整theta切向范数保留全部规范，但没有传入已知非零log。
- [R62：实际 Euler 原函数的 Stokes 常数](../results/R62-actual-euler-primitive-stokes-constants.md)：全部余类、严格尾界及精确半径已证；目标导数恰为中央常数，实际非中央j4块恒为单位，所以完整固定原函数的半径不随中央消失改善。
- [R63：full Euler、Cartier 与固定连接](../results/R63-full-euler-cartier-and-fixed-primitive-connection.md)：全tame测度的单Euler关系给准确自参考值、真实Cartier与首坏5p系数；实际原函数商满足固定代数微分方程，尚缺附加中心条件的整格含义。

- [R64：实际临界Gauss–Manin与Legendre提升](../results/R64-critical-gauss-manin-and-legendre-bockstein.md)：固定代数模函数及两条PF周期给准确素数对角；显式Legendre模p²提升保留除p行，非首项Arb尺度根端独核。完整周期分母与目标对数组合已区分。
- [R65：惰性Hurwitz整性与饱和Stokes jets](../results/R65-hurwitz-integrality-and-saturated-stokes-jets.md)：全部惰性处Euler原函数Hurwitz整；首个Newton滤子的真实全局p分母被Taylor格吸收，显式非零核与逐minor阶乘换算均已证明。
- [R66：全权一临界行与固定除法单位](../results/R66-full-weight-one-and-fixed-division-unit-model.md)：实际Borel偶部给整数周期指数，普通保留modp³、惰性modp²；原256标签的68阶除法函数给明确M1整模型，坏位准确{2,3,5,17}。
- [R67：实际合流jet格及临界不可见性](../results/R67-actual-confluent-jets-and-central-coefficient-invisibility.md)：全首坏带与真实导数行准确比较，p103 D6/D7的饱和Smith证书通过；任意允许坏行数的首带行列式都不检测beta_(p+1)。
- [R68：真实整crystalline Frobenius](../results/R68-integral-crystalline-frobenius-and-exact-critical-comparison.md)：整基、全盘Hodge除p和正确行矩阵给U/V全整；对两种实际critical系数为特征零完全相等，新代表首坏统一推迟至2p+4，尚未给跨p非零。

- [R69：第二坏带真实Bockstein及中央变形](../results/R69-second-band-bockstein-and-central-deformation.md)：先消重复leading行再取饱和商；p103 D9完整证书和中央变形精确复算，局部矩阵仍不能检测完整中央Stokes消失。
- [R70：固定GM向量jet与真实Hodge指数](../results/R70-gm-vector-jets-and-actual-hodge-index.md)：完整向量前缀的整等价、真实稀疏源Smith指数与固定首坏p+4均证明；标量p到2p改善尚不能免费计作固定格净收益。
- [R71：实际Kummer Frobenius及补偿临界jet](../results/R71-actual-kummer-frobenius-and-compensated-critical-jet.md)：真实奇偶单位半线、整exact修正和GM因子精确接合，保留lift依赖的补偿；完整行仍是移动jet。
- [R72：对称幂缺陷与实际挠点投影](../results/R72-symmetric-power-defect-and-actual-torsion-projection.md)：一般混合商及原256项后的三角秩已证明，实际有限和末项恒2/3；剩余和能否无穷次不抵消仍开。

- [R73：实际除幂商格与最后vanishing范数](../results/R73-actual-divided-power-quotient-and-vanishing-jet-norms.md)：指定Sym/Γ商、原Frobenius偶像的全部Smith指数和三种最后行范数1、1、p^-3均证明；不替代所选元素的末系数。
- [R74：一阶模数与真实Witt临界投影](../results/R74-first-modulus-and-divided-witt-critical-projection.md)：实际J_(2O)等于普遍向量扩张，2pO余项保留除p；原GM投影给准确−p项，剩余第二Witt行未证不抵消。
- [R75：固定周期空间上的两类原函数](../results/R75-fixed-critical-primitives-on-the-period-torsor.md)：两类首层同为固定原函数的prime coefficient；真实torsor、明确非恒定留数及monodromy给闭形式边界和整条非Dfinite，指定对角仍开。

- [R76：固定原函数的Bockstein与完整深度](../results/R76-fixed-primitives-bockstein-and-complete-central-depth.md)：同一固定H含两类首层与全部深层；准确Euler余核、Frobenius坐标比较和单个H的非Dfinite均已证明。
- [R77：迭代Frobenius与短输入完整证书](../results/R77-iterated-frobenius-and-short-input-complete-inert-certificate.md)：真实有理p²-Frobenius恢复高权，锐Hodge整除界及模p^(4n+4)完备测试只需O(p(n+1))长度、O(n+1)精度的输入。
- [R78：Wronskian与真实Kummer临界相消](../results/R78-exact-wronskian-and-kummer-critical-cancellation.md)：特征零投影及modp²导数行全部保留，原显式单位代入第二Witt关系后自动抵消，不能作为独立非零输入。
- [R79：标准p曲率与惰性全盘Hasse行](../results/R79-normalized-legendre-p-curvature-and-full-inert-row.md)：规范常数恰一，完整Cartier与有理原函数证明实际V=H/(h s^p)在全形式盘成立，仍须保留模平方信息。

