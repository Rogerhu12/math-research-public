# Serre 一致性交接

## 目标、授权与规则

证明绝对常数C使全部无CM E/Q在p>C时模p满射，或完整给p→∞反例族。**主目标OPEN，未达README完成标准；持续研究，不在阶段报告收尾。** 会话serre-public-astra-20261115；沿远端main，旧未推分支不存在。私有QUEUE已推55eeff4d64c2f54f6b30d8ea5b6dd669f86a4b09。

**已读规则提交：b227ef54ba0062ebc8ef997bbbb85d1b6b835ad2**（2026-11-15T22:21:49.664266+00:00；本地真实git pull --rebase origin main，两README SHA无变化）。root6979d793/topic35f82f3d。工作区/workspace/scratch/09e43497d694/math-research-public，partial/sparse main。完整前态/pins逐字保于[R836前H](handoff-archive-2026-11-15-before-R836.md)及[R836前open](notes/2026-11-15-open-before-R836.md)，内接R835等全部旧归档；旧结论/限制继续生效。

每结论立即推；非快进/引用竞争立即实际pull --rebase再推循环，禁force。每小时及每push前实际pull，两README变化只读diff即遵守并记SHA。PAT只CLI不落文件。root独占main/共享索引，代理只专属稿。新数学只本公开Actions，本地仅纸证/IO/schema/hash/AST。根§15禁raw/机器证书进Git/Release或悬挂blob，一日artifact只保当前必要输入/断点。H<10KB/open<30KB/Markdown<100KB/课题<200MB；日志Asia/Taipei每条≤5行；不添独立测试gate。

## 公开算术当前态（原续算与新消费者并行）

| 任务 | run / job | source commit | 状态 |
|---|---|---|---|
| R787从518位同核继续 | 43766834509 / 132973847087 | 0084d2e067710af828ae071e7850764791e41300 | core93d3d72b / wrapper42157e0d，compute中 |
| R787新518位完整核格 | 43766834526 / 132973884134 | 0084d2e067710af828ae071e7850764791e41300 | core414fef53 / runner889cdf5e，compute中 |
| R815原425-prime续算 | 43748439850 / 132916821952 | a108ce1e72958b296dcca7ff55710c94e8ed16ef | core80516ff9 / wrapperab725da0，原目标/prime/mode不变 |
| R824从365完整位续算 | 43762208712 / 132959291421 | a75fdaa7cd40e81dbf1026767025e58044b3befb | core1ece3cf4 / wrapperc5907739，准确27+244 scope同核继续 |
| R827旧Hermite | 43764014099 / 132964965600 | fd4cbaea820d79e115c300d766042582be14a091 | 已被R835数学替代；取消API403，待自行结束，不再续接 |

**R787真实518**：[双入口](notes/R787-518-digit-checkpoint-and-precision-increment-activation.md)保43737413555/source4092d1cc的BudgetStop/exit1/errornull；current73180954B/4997a05b、history518条/07875f05、manifest7a22beb2/1262项、artifact14181899102/343bee0a。原核只换resume，另启新精度核格，不重14分支。
[核格契约](notes/R787-original-precision-increment-kernel-lattice-and-source-contract.md)bc91a891/core414fef53/runner889cdf5e保全A1234×14/C1214×14相容、56×42残差/unit42逆/KH新全格、一次56LLL和原129×280出口；旧98拒绝默认不用。新格正在运行，尚无准确关系/y。
旧430/42/56 LLL及固定C98全Ω非零已闭，不重跑；同C任意A全拒，不推430不足。新精度同D不代同C，旧拒绝默认不用；全部pins保[R835前H](handoff-archive-2026-11-15-before-R835.md)。

**R815**：[425 CRT断点](notes/R815-425-prime-checkpoint-and-same-core-continuation.md)保425prime/12707bits/Γ未始，原深续算仍80516/849bca27。
[真实三列结果](notes/R815-three-known-columns-ended-and-denominator-boundary.md)run43762388370/sourceca1fe0d5已成列0/1/271、2886同余、高6/7次零、d012=10238bits；四pair28LLL的49正候选全首(0,0,2)拒。manifest0f2be930/artifact14181118695/afe625bf。仅排中心提升，不推425不足；D=d012·a已实施，不重第三列/Wvg/旧格/拒绝。
[八probe九维](notes/R815-original-eight-probe-common-denominator-lattice-method.md)run43767171070/job132974881457/source278d1920，core49f8952f/runner5f0bc897；固定八probe一次全9DLLL，UH=R/detU±1，三列与旧49只同D/M/known/W引用。保原198小源/两carrier/原七点/cyclic/Γ，false FINAL不覆current；结果未回。

**R824**：[365断点](notes/R824-365-digit-checkpoint-and-same-core-continuation.md)manifestf45e2193/currentc6ddf4fb/lifta7a95048、artifact14179899060/bc2789d4；27+244同核继续，free1186归R787，原129/142/280Q、1521及κ/246一次保留，r28不补143..155，全生成才1778minor/1206。

**R835实际成功**：[原四阶终止与D约化](results/R835-certified-original-order4-termination-and-reduced-D.md)，run43767561191/job132976021283/source3198158a，46.529879231秒；a0/1完整det次数1320/3496，全1341/3517节点+xgcd乘回给真gcd1。分解adjugate右逆接同源σ∞rank272/det695832206及proper，**原I4=C、D约化、K1已成**；q最小/P0∈D/D坐标/eta/height未得。
final3221f24e/manifest2d77e2f0/4901项，artifact14183161538/7eaffd6a至Nov16 22:10:17UTC；新source27499704B/eb908748与原233593489B/1e3fc4db续传。core4f2dc119/runner7715eeb9/证明7e07f78e/17e9c828冻结。全部完整pins见结果；本地18小件仅IO，不重原导数/C/∞。旧Hermite取消403，不再续接，继续原D准确构造。

**R836已证短核入口**：[固定21点铅笔与原D](results/R836-original-reduced-D-fixed-branch-pencil-and-short-RR-kernels.md)保ε=multP0D未知，E2=C+D+εP0，完整整商I_D=(I2:I_(C+P0))。权2两锚在原V5的rank1213认证共同零恰21点；完整T4时830/832×690核=M3(D)，dim295。真不完整短源仅给包含，实际295维或272个权2/3/4候选+V4真962minor/权和793才迫完整；未有实际锚/T′/D/eta。单B模列不能冒名完整char0层，q3只备选未跑。

## 已成源、真实消费者及期限

[R809六C](results/R809-certified-original-six-Hodge-normal-vectors.md)run43712427063/source91fbd81e，84Q/full1380/S5=1234准确已成；A/B不在scope。真R787关系后原R809可resume该包、只append A/B，basis tag排future源；原R792 core7b7a5483/wrappercdac2e93可直接消费真新R787，workflow已删publish、contents只读。

R806/W、R813/g,h、R820/C、R801/803/805/807、R781 R0..142均已认证，不重算；V6/7/8尾界141/175/195，R805[1,144,127]非272项EPS。五个R824入口R792/R809AB/R804/R811/R825全核pending、pins见归档；不冒名R787或将C-only当AB。冻结849bca27/89579f79不改。原R825入口若采用仍须双向Laurent/全长1206、272×816全核秩544全部投影；新R835已给K1，导数向量非乘法算子。原b/s/λ/82^10、共轭/唯一Fb立方根、vκ/有限核边界保；当前无D准确坐标/eta/height。

R775/R786至Nov16 05:52/05:41UTC，R786 index已在后载体；R790的146CM行07:22、R791 tangent06:37到期，R794 carrier不含它们。真关系发布即消费，临近到期只IO保必要旧输入。R809六C15:52、R78743016:25、R815425 18:33UTC到期；续算保最小bundle/完整current。详见[期限记录](notes/2026-11-15-R815-endpoint-and-input-retention.md)。全部源pins在各certified结果、[旧结果索引](results-archive-2026-11-15-before-R833.md)及上述归档。

## 真正全p缺口与已封闭边界

本节只保当前接口；全部旧源、完整公式、已闭支路和不可省边界逐字在[R836前H](handoff-archive-2026-11-15-before-R836.md)、[R836前open](notes/2026-11-15-open-before-R836.md)及其递归归档，不重做。

R317仍余p2/5mod9完整非分裂正规化子，a³+db³1/p|b，D/bc无统一上界。R707固定p41完整129盘八CM已闭，不外推全p。R575真CM根号负，逆twist秩零撤回；R616/726给原β非挠/rank/log，非高度。R832显式jet界只给有限窗口，未给(724.33)。

[原Poincaré/period审计](notes/2026-11-15-original-height-Poincare-linearization-and-period-determinant-audit.md)9a54e844保原Q点β/非p项/刚性化/零阶纤维，U_i=c(a_iV_i−A_iL_i)，共同第二类项整函数相消。指定degree dY+2 period多项式仍缺；End⁰G=F、非零torus商维≥g+1，线性AST/η^-或E0^g幂等元不补高度。九覆盖混合Hermitian/端点逆序/中心曲率审计已闭。

sigma必须同一primitive/Legendre h三个原单位。R739/R741/R737不同标签不拼，R808/810有限Gram/Howe链已闭且保[K,P_T]；R826/828原八源/两G零、R830真conductor-p、R831old6交换代数、R833/834真Γ/Serre-dual全复用。指定uP0,e配对仍缺，不以全局源非零代值。
[unitary交叉heat](notes/2026-11-15-sigma-unitary-cross-heat-and-primitive-source.md)173077d4保原36theta/full72和same-h差权；指定p+1源未知，μell仅共同jet，FG一次横向零，中央h辅助j2048/3非原j0。
[KS](notes/2026-11-15-sigma-Kronecker-weight-one-square-and-critical-convolution.md)/[XF](notes/2026-11-15-sigma-original-X6-weight-one-and-logarithmic-square.md)/[PL](notes/2026-11-15-sigma-original-Schwarz-frame-and-critical-Lagrange-source.md)/[PC](notes/2026-11-15-sigma-original-PF-cusp-Cartier-and-period-correction.md)保十八项/原Fermat/Ωη相位、C^-5和Wronskian1−κU^pJ，C非第二水平周期。
[CR](notes/2026-11-15-sigma-critical-Cartier-residues-on-original-X6.md)b85ab474给Carβ=xΣresν^(1/p)dy/(y−a)，原P0值=3αR_p、S=αR_p/1458；原三挠character排正则余项。[HC](notes/2026-11-15-sigma-critical-P1-descent-and-C-root-residues.md)38d7d105给P1_x下降、∞零留数与全部4/9/11阶局部式；[CN](notes/2026-11-15-sigma-critical-cusp-residue-nonzero.md)78f5d9e5纸证固定K∈Z[1/30]且mod13=11，故固定有限例外外全局Carβ非零。指定P0加权留数及same-h三单位仍未知，不再重证全局非零。

ordinary原p43/776bitq已Gaussian5排；[Shapiro](notes/2026-11-15-original-Robert-Shapiro-second-class.md)337a9892/[θ-lift](notes/2026-11-15-original-exact-dual-theta-lift-and-shifted-cup.md)7388c4be保唯一Kglob/Θ=i a_q和同Σ θ3，C4/T²杯积仅复R779；无独立Θ、禁巨大q枚举。R729及R816/818/819/821/823共同c1不分歧已成，不给高度单位。原p41b/s/ζ²一次/CRT6逆/246/c0c1保持。主目标OPEN，继续open.md。
