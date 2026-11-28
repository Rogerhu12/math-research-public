# 待解决问题

维护：Astra-held10-7c4e33ee-20261128。**进行中，未完成。** 本题README全部标准保持不变。原完整open已保留于 [继承open](notes/2026-11-28-inherited-open.md)，不删除旧结论、失败或未知终态。当前实际输入以HANDOFF和原solver记录为准。

[17:09 UTC后执行恢复](notes/2026-11-28-workspace-view-reset-and-recovery.md)：旧数值scratch当前不可读，两库已重新partial clone/pull并核双README无变。原generic80294/design89083均真exit1，分别有明确ENOSPC与未知原因，不能当活算或数学失败。只再生新R87必要输入，不重算旧q=.06/1152段已登记原型。

## 1. 实际圆弧设计推进到λ1

原R53 δ-design晚返已到λ=.128/M48全原门通过（metric1.59049982984e−7、1219点）；原.256域失败、.192 MemoryError，截止attempt011未知。完整标量及来源见 [旧执行末态](notes/2026-11-28-design-previous-frontier.json)。继续时使用最高真实锚，必要再生丢失raw不计新进展。现有跨M完整lift割线只改变未接受初猜，所有原solver/RMS/BC/metric门不变。若高M稀疏LU耗尽内存，改善执行/矩阵组织或用本仓库Actions，不以资源失败排除数学支。

原v2/v3/v4失败链不原样重跑；v5以δ替首phase的metric-only输入不能晋级。R72兼容标量及实际δ/Robin响应仍可改变设计，入口基Gram可逆不替完整边值问题。λ<1没有准确圆弧保护H，δ/mean变化是设计而非固定g精化。

新合法设计输入：[三重b=.5宽过渡](notes/2026-11-28-design-wide-transition-b050-curvature-and-held-window.md)，S=.5/k=.2与原R54握持窗不变；条件完整support盒A≤2/3给全λ核心κ<11.4，真实小q锚A<.1。只有小标量BigInt已运行，新核心/BVP未启动。由真21d676/3bc1c05 raw作新宽窗λ.002初猜，同b下取.004第二锚后续原全λ/谱门；新g若最终全标准通过可选为终态，不强制回旧q/b。[高k旧profile实筛](notes/2026-11-28-design-higher-k-old-profile-screen.md)已排除k=.4/.5所选经典支，k=.45用R57；只属R5/C³类。后续改物理profile，不再跑这几条已排旧支。 [R87](results/R87-single-gentle-ramp-half-curvature-held-window.md)已给六段单缓坡新profile，k=.5/S=.675/b=.3/α=.8，原r≤1.1盒的连续核心/首圆片/全首周期尺寸与条件held/reach预算已付。[新r≤1.15盒](notes/2026-11-28-design-single-gentle-r115-extension.md)与[原Python线性根](notes/2026-11-28-design-single-gentle-linear-root-actual.md)已实付，δ=.06809451565377872；现在接同新profile的原λ0全BVP及λ1，线性校准与条件几何本身不作完成。[R91](results/R91-period-mean-compensation-and-wider-core-box.md)又以准确总曲率把核心充分盒扩为A≤8/9、全λ κ<3723/314；实际新场仍须自行付其余门。

[新R87 λ=.256/M40实返](notes/2026-11-28-design-single-gentle-lambda256-m40-recovered-observation.md)仅metric1.24844e−6未门，M48未知。M32→40平台支持从同一新profile收紧径向tol2e−7，保原全部门；最高原真接受仍λ=.128/M24。

[R94真实窗舍入后果](results/R94-binary64-core-window-period-budget.md)已付实际binary64 S/b下原R91核心预算；最终完整支持A≤8/9、Gauss与材料角求值误差仍须单独核，不用理论真实积分替代有限实现。

## 2. 完整非线性尾及共同接缝

[原低模真实末态](notes/2026-11-28-tail-low-modes-actual-terminal.md)已达λ.002来源的M8 full-H；sample metric2.9133693236e−8、residual1.8949786217e−9，不含来源剩余16模。M8full→M16首请求收到失败包，具体字符串未知。新路线在较低幅度逐步升模或更细模式阶梯；最终必须原M24或最终λ1源的全部H，保原audit/完整J/native4/chord3及8outer。失败包checkpoint不作接受场。

本次新879点源的[完整M24/N512/f=1原响应已返](notes/2026-11-28-tail-actual-complete-fullH.md)：1152段/55344未知、freshJ及1776项heightJ/audit齐，residual3.65238e−10。原audit normalizedFullDefect1.96429e−5如实保留，不能替代连续证书。[完整1152段有限定义](notes/2026-11-28-tail-actual-complete-geometry-bundle.md)已实际返回，18460 quintic spans和共享两jet/原global mean全核；原全尾实际终态已遍全部18460 spans和深collar：[R90](results/R90-complete-closed-all-phase-metric.md)已将原17644通过 spans 与816同场Taylor补证合成完整连续metric，全部相位严格<1e−6；Kmax10.017503096，deep/完整投影单射/共享两jet已付。原内部K<10的stage82 false保留。原8outer及整闭图仍欠，不把有限定义当完成。

[fresh新QR完整尾小块入口](notes/2026-11-28-tail-fresh-qr-complete-chunk-geometry-entry.md)从真实final physical-H直接开始，保原stage0/全谱/共享mean/全部公共两jet/完整merge及连续门；不需要旧−9或旧部分尾。实际只有源码与递归写门检查，无新λ1几何。

两侧须同一完整g、真实primitive、字面源mean、完整高度非零模与零模。R12/R14已证明精确高度二jet+度量一jet的Cartesian接缝机制；实际仍须同一两jet，不能用小残差、单侧formalRR或不同mean代替。R58–R62旧λ.002场连续界、旧.25尾cell7/deep及若干stage不重铺；新场单独付连续界。本次R73已付新879点源的最终Cartesian前缀/短桥连续几何（support>.6445、norm<1.1901、K≤12.3）；R74又付同图全连续metric<99/1e8，准确三重协变覆盖全角/全相位；更高真设计λ=.064/M40的R76几何与[R77同图完整连续metric](results/R77-lambda064-same-cartesian-prefix-continuous-metric.md)也已付，后者1433叶×3072扇区角格、全角/全phase严格<99/1e8；全部定义身份已核。[R79](results/R79-actual-width012-cut-prefix-continuous-metric-geometry.md)现已付同λ=.002原raw-H场width=.12完整cut前缀：82叶与未改补集全metric<99/1e8、K≤123/10；.04/.01已有真实点反例。[R80](results/R80-actual-complete-tail-absolute-geometry.md)已付同cut原点的实际完整尾/deep/平盘绝对几何（ell=marker=0）：radius≤.92043712、support≥.77104143、K≤10.017504；[R82](results/R82-actual-marked-closed-family-all-time-geometry.md)又付同字面正柱/规范帽整闭图全时C²嵌入与reach/D>.03408815。[R83](results/R83-actual-closed-third-activity-and-euclidean-separation.md)又付同图完整第三活动矩实部>.1392755与含反射δE>0；[R84](results/R84-actual-endpoint-third-tensor-separation.md)进一步付指定0与9/20端点的张量差>7e−19（当时仅张量不变量）；[R86](results/R86-full-disk-marker-with-unchanged-geometry-budget.md)在完整真平盘选择半径2r0和准确幅度1600ε0，保持原全几何预算，指定端点I3差>3.59e−14；这是新固定盘度量设计，非旧g精化。 [R88](results/R88-quantitative-euclidean-hausdorff-from-third-moment.md)现已把两端点张量差转成包含任意平移/反射的严格表面距离，canonical>4e−23、新完整盘>2e−18；它们是保守下界，不是实际或最大距离。 [R89](results/R89-sharp-marker-bernstein-and-unchanged-geometry.md)已进一步准确证明更紧帽导数界并真实构造新35倍幅度固定帽，保持原全几何、dE>7e−17；仍只属原λ.002/raw-H新盘设计。[R90](results/R90-complete-closed-all-phase-metric.md)现已完成同一raw-H整闭图全相位metric门；最终physical-H、准确λ1和固定完整g精化继续。

[R85](results/R85-complete-robin-to-actual-dn-and-fixed-metric-update.md)已给完整系统真实末端行的rank≤M更新和fixed-g的25维联合块，保所有原未知/域门/8outer。[完整24列](notes/2026-11-28-analytic-complete-terminal-response-basis-actual.md)及[端口初猜](notes/2026-11-28-analytic-boundary-dn-initializer-actual.md)现已真返：全64191行port-forcing残差5.4210e−18，literal小S有Fraction逆证书；完整mesh/pscale同但y/p不同，仍旧点chord。[完整q列/25联合块实算](notes/2026-11-28-analytic-complete-fixed-q-dn-chord-actual.md)现给混合点χN=2.47108106147e−5、保全F_L的固定δ全仿射残差1.362e−18；当前J差/非线性域与原BVP/8outer仍继续。优先利用这些全量列响应减少重复大J，不冒称旧Robin χL已支付fullDN固定g可逆。

[真实λ1完整QR-DN入口](notes/2026-11-28-tail-lambda-one-complete-qr-resource-entry.md)已准备并按原源码核同；真正accepted λ1 summary到来后，原native4/chord3/8outer及最终physical-H完整门直接接入。新source_kind/真实mean/4/5相位明确，不冒旧streamed或旧M24来源；当前只有入口检查，尚无正向耦合结果。

[R92](results/R92-complete-refined-chord-space-and-residual.md)已证完整旧弦向任意径向细网格的准确可逆运输，保所有新未知/子行/原BC；完整左右残差界与单右端不增明确。真实旧λ.002固定g仿射前缀只二分867号cell到880节点，RMS/BC/metric全原门已过，但真新native从未启动；旧raw当前不可读，不迁移其旧J/V到新λ1。

## 3. 同一完整问题的精化

冻结最终δ、全部轮廓/warp校准、核心或声明的同一未知函数空间、源Cartesian mean/primitive、尾背景和完整时间域。[新QR首锚固定g入口](notes/2026-11-28-analytic-qr-anchor-fixed-actual-source-entry.md)已保原支持族和完整数值门，独立KIND/完整祖先链绑定；mesh使用真实R87显式4/5扫窗。只有源码检查，须待真正λ1/full-DN首锚后执行。R53原支持族与完整baseline+零phase是不同的合法未知空间，须选定并如实说明。旧actual-refine KIND/1168分支不覆盖新高M/新mean；只改标签不合格。

本次真879点λ.002/M24已算完整原J的δ↔logq Schur=2.469619216e−5（两h相对差4.055e−7），据此原支持族fixed=True同λ/同g/mean1168的M24实际径向精化已全原门过（1032点、RMS1.99629e−7、metric6.53252e−7），现继续M32谱精化；这不是fullDN闭图精化或严格逆证书。

[新QR fixed完整尾C²入口](notes/2026-11-28-tail-qr-fixed-complete-c2-source-entry.md)已保完整同g及各自physical-H/真实均值、全部共同半径细分和原严格比较；须用真锚/真fixed pair实际支付，尚无新比较上界。

至少给固定问题的频率、径向和时间精化，完整度量误差持续下降到机器或求解容差，不能用设计λ/δ变化冒充。R63/R69及actual-tail-C²比较器只给结构/有限差，不自动给C² Cauchy或精确解存在。对严格存在还有完整可求和/逆界责任；数值完成须按README说明此差距。

## 4. 完整闭面与全时比例

真实未标记图须支付D0≤2.68、|κ|≤12.3、X·n≥.087等所用预算（或直接给更好实际界）。R54/R67在这些前提下的短中央柱/横向准确圆弧H/固定全谐波帽已给held>.1D、H径>.2D、reach>.03D和δE>0的结构，不重证它们，重点构造实际输入。

[R78](results/R78-lambda064-complete-prefix-third-activity-moment.md)已付同一 λ=.064/M40/mean1936 前缀1035格的三阶活动矩，严格 `1571879/10^7 < A3p < 1572603/10^7`；两种短柱系数已给。该场尾/cut、最终柱长及整闭图 Euclidean 下界仍欠，不能混入 λ=.002 尾数值。

中央柱与上下半面的公共Cartesian两jet、桥—尾、深圆领和平盘均须一致；全部F_t为C²嵌入且t在C²连续。reach覆盖全t而非端点，整像Hausdorff不能替换成材料点位移，D用完整曲面直径。新λ/mean/核心不继承旧低幅数值常数。

[R95实际beta区间](results/R95-actual-core-normalization-from-positive-inverse-average.md)已给真实系数的轻量完整标量误差证书；历史λ.128/M24实例真过，但新λ1仍须实际A门及同输入的全部核心位置/导数/全图证书。

[R93有限高阶相位及E(3)界](results/R93-finite-high-order-phase-witness-and-euclidean-bound.md)已将R67某个非零高阶矩接口变成有限明确相位及可代入距离系数。新λ1须真实认证其mN/AN/帽与完整R、σ；不要求预先假设m3非零，不搬旧λ.002活动矩。柱长/帽一经选定即冻结为同一g再精化。

[新QR final-H完整几何/活动矩入口](notes/2026-11-28-tail-qr-finalH-geometry-and-activity-entry.md)已经修复旧raw-H/旧width/source/phase硬锁：仍须新场同完整bundle、真实共同cut、全谱/mean/两jet和原连续证明。活动矩区间两种符号均可排零，未计算新阳性。

[R96完整二维帽界](results/R96-complete-marker-hessian-two-variable-psd.md)将同完整有理帽Hessian上界从17/2改为23/10；只提高未来幅度的曲率充分预算，尚未选择新帽。若采用，必须在最终fixed-g之前冻结真实r/eps，并在所有图/metric/几何/活动矩/mesh/time入口绑定同一合同，另付高度/support与全图门。

## 5. 交付及强目标

达到全部门后给多个t的完整网格生成命令、参数和SHA；按根§15可再生网格不入Git/Release，单个生成网格<5MB。说明数值与严格存在的具体差距。基础完成后继续提高held/D、δE/D并报告reach/D，不能为了结束降低标准。

## 6. 备用数学方向（保留原O1–O13）

原Gauss–Codazzi完整BVP、四重核心/双模共振、真实混合首cell、短cut、旧m3联合支等全部成功/失败见继承open对应O1–O13与results索引。只有新输入、方向或表示有实质理由时再做；不重新计算已登记低幅闭图/障碍。R8退化入口唯一延拓、完整核支和真全局边值可解性仍独立，不能靠有限方阵计数或单个近核推存在/不存在。当前优先原R53的实际λ1和真正全尾。
