# 待解决问题

维护：Astra-held10-06bbeb39-20261126。任务未完成。旧1b6d88ec scratch实际不可取，以下旧进程描述仅保留最后观察，最终状态不推断；本次从已提交源/参数必要再生后继续，见notes/2026-11-26-resume-and-current-sources.md。

前会话最后状态：终端已于11:06 UTC恢复，新g在本地推进，旧λ.02公开Actions已结束，参数/命令/小结果已保存；旧91205/27744及82514/18524/2919终态未知，57647已有八行结果。按已登记断点接续，不原样重做已完成计算。

## 2026-11-26 新接续

R63固定完整g后把未知核放同一函数空间，必须核与全场C² Cauchy及完整残差下降。原M24 λ.002已必要恢复。暖v2同图锚通过，但12次λ推进均原RMS未门、最小步自然终止；不再重跑该链。R68补弧v3在实际同零锚重新通过逐位方程/核心/chart身份和双角metric≤6.48242e−7（未调用solver），[首四档](notes/2026-11-26-warm-v3-intermediate-returns.json)λ.004/.003/.0025/.00225均真status1且RMS未门，[续两档](notes/2026-11-26-warm-v3-next-two-returns.json)λ.002125/.0020625也真实status1、RMS.00783255/.00391697未门，其后[.00203125也status1/RMS.00195866未门](notes/2026-11-26-warm-v3-worker-deadline-actual.json)；worker13:02:07到原期限，末.002015625未返回、无新λ，不重跑旧v3链；独立run45806625263的原Newton方向诊断已真实完成：21档首接受α=2⁻²⁰；中心FD支持本方向局部导数，而有限步二阶余项被同一全局逆强放大，详见[实际诊断](notes/2026-11-26-seam-newton-direction-actual.md)。未施加更新或取得新BVP；R70混合v4的[新真实零锚](notes/2026-11-26-warm-v4-zero-anchor-actual.json)逐位同图及原双角metric通过，未调用solver；[λ.004首真实返回](notes/2026-11-26-v4-first-actual-return.json)为status1、5016点、RMS.0780476/物理BC6.29195e−6未门，22接受步/minα2^-17/域拒142，仍从真.002锚二分到.003，不晋级失败场；δ-design已恢复M32/.004/.008全门输入，新.016及[.032/M32](notes/2026-11-26-original-design-lambda0032-m32-accepted.json)均已原门过（后者2325点/metric6.45736e−7），首[.064返回](notes/2026-11-26-original-design-lambda0064-first-return.json)RMS.00367759未门、无physical/metric；后[.048返回MemoryError](notes/2026-11-26-original-design-lambda0048-memory-return.json)，无raw/physical/RMS，分配位置未获，不称数学失败；仍真.032 raw作锚续attempt007，非固定g精化。material M16冷恢复自然失败，历史λ.004完整H独立尾的factor.25/.5原包/audit已通过， .75在原worker期限处中断、无第三接受包；转新实际设计候选；lowq于12:30:41 UTC到原worker期限，超限诊断仍省略，数学终态未知（[实际记录](notes/2026-11-26-lowq-worker-deadline-actual.json)）。新动态全尾/真核心/完整前缀验证入口已备，但各实际新场数值界仍须重新计算；原factory/checkpoint覆盖语义门已修正；同问题actual-DN精化五源已审，等待真实λ1全尾输入。真正λ1/fullH/公共C²/闭族及固定完整问题精化仍未完成，见最新HANDOFF/notes。

[R71](results/R71-v4-uniform-small-lambda-curvature-bounds.md)已给当前λ=.004的v4连续曲率/同模投影M一致条件数<1.009及小λ的L²全列可逆；不再把此处完整BVP困难归为这组入口曲率基的M近核。仍须核真实径向传播/端口伴随响应，δ改变物理profile的非齐次列不能由入口L²满射直接吸收。

[R72](results/R72-delta-robin-response-and-phase-compatibility.md)进一步给完整δ响应（含桥转移与移动端点责任）、线性共振伴随积分及有限幅βδ/βphase条件；积分非零与实际Schur仍未测。固定d1=0、以原δ替代首phase是新的明确design选择，不能标同g精化；保原source baseδ/raw p0/chart与各自mean（M32为1552），先做真实零控制同图，再交原BVP全部门。

[v5最小入口](notes/2026-11-26-v5-original-delta-phase-design-entry.md)已冻结；[fresh lowq直接入口](notes/2026-11-26-seam-fresh-v5-recovery.md)必要恢复实际原R53 M24后直接进入零锚及最多3次原BVP，保baseδ/raw p0/chart、固定q/d1=0与R70高phase。新run45822332434已过bootstrap，probe备用v5已撤，保当前v4计算。[真实零锚](notes/2026-11-26-v5-zero-control-actual.json)已过37项原方程/core/完整jets/chart/mean同一核验，run4593371f/raw6fb36ac7/physicalbce9ccd2；solver=false/null，不当新λ求解接受。[首.004/M24实际BVP](notes/2026-11-26-v5-first-actual-solver-return.json)status0/RMS9.94361e−7/BC1.49e−14过，但metric1.71372e−5未门，仅作完整lift至M32的初猜；6步/minα.5为本次观察，不外推全族。其后[.004/M32真实MemoryError](notes/2026-11-26-v5-m32-resource-error.json)无raw/physical/RMS，driver返回0不等于solver成功；原.004/M24完整metric-only场保留，失败M32不作seed。当前三次段已结束，马上同VM读取已存traceback的源位置/hash以定位资源异常；不重求零锚/M24或猜内存分配位置。每个段返回后依据实际接受场继续，不能把预算返回当课题结束。

[v5第三真实返回](notes/2026-11-26-v5-third-actual-solver-return.json)为λ.003/M24 status0/632点、RMS9.95177e−7/物理BC1.62790e−15，但metric8.46899e−6未门；run908a4801/raw53fc02bc/physical5f911599均完整。三次预算已自然结束，接受锚仍真同图zero λ.002，不能晋级该seed；现在从旧summary双身份直接续首pending=.003的M32原完整lift/phase检查，不重复zero/M24。原.004/M32资源栈另读；资源包装仅原执行优化，保全部有限门。

[原R53完整割线入口](notes/2026-11-26-original-design-secant-entry.md)在独立material新作业必要恢复真实同M两锚后，用原计算t cubic PPoly预测完整Y/p；仅初猜，原solver/RMS/BC/metric全门决定接受。通常网格并集；若超过原max_nodes则在右场原网格评价两原PPoly，不重拟合或截状态。当前链不重启，恢复旧λ不重复计作结论。

[首个完整割线真实返回](notes/2026-11-26-original-design-secant-lambda0032-first-return.json)已全原门通过：.008/.016同M真场预测λ=.032（β2，初猜864点），实际M32/866点、RMS9.91172e−7/metric6.71186e−7/物理BC2.62752e−18，3接受Newton步且无域/merit拒。它到达已登记过的同一λ、得到不同raw场，不声称更高λ/同图/固定g精化；原直接.032是2325点/21步，仅比较本次有限求解观察。run97ffa238/raw28a171df/physicalf0c54a25完整来源已核，父链现attempt001继续。

完整割线随后取得新前沿：M32/.064真solver/RMS/BC过但[metric1.04547e−6未门](notes/2026-11-26-original-design-secant-lambda0064-metric-only-return.json)，仅作原完整lift初猜；新[.064/M40](notes/2026-11-26-original-design-secant-lambda0064-m40-accepted.json)已889点/RMS9.95910e−7/metric2.75690e−7/物理BC4.01608e−10全原门过，run4d455f1a/raw97e492d1/physicald1cd2972。实际mean1936（原M32为1552）明确随设计改变，不称同图/C²或固定g精化。当前仅一个真接受M40锚，按原策略继续真实raw初猜，不额外重算旧点或把M32 pair伪作M40 pair。

[单方向的统一两块重标度分析](notes/2026-11-26-existing-direction-uniform-parameter-scaling.md)已用原实际标量精确比较：当前v3方向均衡只使首过k20→19；任何正两块统一权重在已测档都不能早于k16。不能据参数成本占比大就盲改phase_scale；不推至v4、非线性qAPI或任意预条件器。下一步仍是新v5/完整割线的实际返回。

[δ单列替换诊断](notes/2026-11-26-one-column-delta-replacement.md)给同λ/实际g/字面chart/mean/高参数且d1=0的完整Jacobian关系；需先实际核全残差及其余块同一。一次旧LU转置给γ=wᵀbδ，必要时再一正解给完整新方向；当前无γ实测，不为已不存在LU另跑抽象证书，等真实v5返回需要定位时使用。

[原 full-H/native 源码合同](notes/2026-11-26-full-height-native-continuation-source-audit.md)及[v5 actual-DN 接口](notes/2026-11-26-v5-full-dn-source-interface.md)已核：现runner的chord-source/native可复用，generic协调器却尚未装bounded-chord；仅加配置不能启用该实现。实际来源须真SOLVER_RETURN、baseline/runtime配置分开绑定，保全部full-H/J/audit和最多8次真实外迭代。v5的δ内部完整列/高phase入口列不变，当前固定cut的参数直接底块为零有明确范围；旧seam采用另一mean，仍欠源字面mean的Cartesian两jet实测。未运行新尾，不增加抽象缓存或预设速度保证。

[v5窄续入/资源执行](notes/2026-11-26-v5-metric-seed-resume-and-lu-release.md)已保旧summary双身份：接受λ.002、真实未接受.003/M24 seed，直接M32原lift；此前M32 MemoryError的[同VM已存栈](notes/2026-11-26-v5-m32-saved-exception.json)在splu。使用现有block8/旧LU释放包装仅是资源尝试，原矩阵/分辨率/所有门不变，单LU内存是否足够仍待实际返回。终端断开后以连接器部署同VM请求，未将远端读称为真实pull。

## 当前接续顺序（2026-11-20）

- 新多段g原support q=.006→.06已全过；宽窗λ0/τ1完整lift后，λ.002在M24原linearDN前缀已过metric6.48242e−7。原mean1168/GL6和mean512 proxy明确区分；真实尾.25及.5 warm均已完整原门通过；chord3 session54314现接.75/.9，完整fullH与原外迭代仍欠。固定完整g/全部物理参数与均值规则后才进入正式精化。 root下一λ.004/M24真收敛但metric1.53303e−6未门，表示外ψ77/79主导；[M32升谱实际](notes/2026-11-20-m3-newg-lambda0004-m32-accepted.md)已860点过原metric7.604677e−7/BC2.84346e−12，原mean1552；[λ.008/M32](notes/2026-11-20-m3-newg-lambda0008-m32-accepted.md)76535已863点过metric7.844246e−7/BC6.08e−15，现45287续λ.016同原门，旧真尾不动。
- 旧live44720589640的M8 trueDN收敛但metric未门；M12/M16补空间误差下降后，M24原前缀真过l1 2.95091e−7，固定mean512 proxy operator2.53910e−7。新M24真尾请求在求解启动前被诊断键白名单拒，runner12:36 UTC结束；请求已修，当前无旧场副本。固定场实测转本地新g，不重复旧链；旧R55 reach障碍保留。
- 新环境旧scratch缺失：已建立可搬迁70源/port/chart恢复入口和同原native的2CPU installer；不再要求失去的旧launch-plan链。旧91205/27744仍未知。
- R53真实旧核心圆化及整个控制盒正性/C2步长已证明；R54另用横向握持片将柱长降到≤.01，在同一完整D预算下条件比提高至11.14%/13.20%，不改当前数值模型。R52新材料曲率核已证明准确圆弧与条件10.39%/11.72%窗，并显式支付插柱直径/支撑预算。m3首q=.01/M8与n4首q=.01/M12均真实失败，m3转可解余弦同伦，n4收紧曲率数值域的q=.02/M8也在密点真正Frenet失败，转历史端口高度锚定恢复；没有完整BVP/真尾接受。其q/c含义不同于旧支撑核。
- n4原b.16/λ.02/M20全场从公开紧凑参数必要再生，边界目前为原线性DN；原真尾结果已登记，不把再生算新结论。完整命令见2026-11-20两份恢复note。

- R55新g宽盒r∈[1.05,1.1]首cycle的|X|<1.34已严格付清，覆盖实际线性根与已接受幅度场；完整D0≤2.68/K≤12.3/support≥.087仍须给实际新图。R58已对当前4.625独立付h<.025835/w≤.41/K≤8，原tail扰动条件可用于此真实背景；有限JS求值误差、实际非旋转V及完整接缝仍欠。
- R59新M24共享Hermite/解析桥真primitive/mean1168的C²桥已付(V0,η1,η2)<(.035,.179,1.639)；同一新prefix的绝对z0已严格落在[.44631325197234495,.47839691621379593]，故桥半径<1.245/support>.39867/K<8.367444。R60已以1830盒付旧数学jet oracle全桥metric≤8.986281e−7，合Gram转换<3e−8得该真实C²桥metric<9.3e−7。含lift prefix的真核心区间、全角Γ3/Γ4与mean1168严格节点已付；root直接用真核心，2336角盒因插值余项过宽，4672必要细化已实际完成；[R62](results/R62-actual-m24-complete-prefix-and-bridge-certificate.md)完整prefix连续metric/K session2559已真过1065区间，全metric≤9.695184e−7/K≤9.649812、未决0；同图尺寸/support已395盒真过|F|<1.14/support>.504，中央精确二jet已由R61同g局部修补付清（metric≤8.19863e−7/K≤2.18421），prefix—bridge字面二jet／mean1168／同真高度锚已付，不需patch；桥—真尾reference g已由末.001显式target Hermite统一，原F/mean不动、转移后桥metric<9.301e−7；这是新目标定义，实际尾Cartesian接缝仍欠。尾局部G16真实积分层已付半径差<3.310e−10/合α矩阵分项<1.374e−8；n4真背景部分积分／R图oracle及实际x二阶跳已付，原x图不全C²，现接.25真实场的共享R二jet；IEEE/libm与实际尾图不自动通过。不能搬桥常数。

- 已接受.25 warm 的 stage127 现以字面R结点/共同Cartesian二jet定义实际C²图，17完整径向块×全角连续metric≤1.127693e−9、K≤8.000976，真R58背景未换；15606端点等式精确。相邻全stage的唯一节点共用、fullH和切口接缝继续，详见 [stage127证书](notes/2026-11-20-warm025-stage127-shared-r-c2-certificate.md)。

- [.25深圆领与平盘](notes/2026-11-20-warm025-deep-collar-certified.md)已用实际stage1151内端459个字面两jet参数构造并认证：918精确端点等式，metric<3.772e−30/K<8.001；z_b∈[.1,1.28]时盘组件嵌入、radius<1.34/support>.09。全尾须共用此唯一外端数据；[同桥高度合同](notes/2026-11-20-m24-cut-height-and-tail-mean-contract.md)已付Zc≥.4981646，保原μc、zb=Zc+μc严格在(.49,1.27)，本盘和stage0的高度窗已满足。只常数槽对齐，fullH与Cartesian两jet仍欠。

- [.25 cut stage0](notes/2026-11-20-warm025-stage0-continuous-r-map.md)已付16完整R块/全角metric≤6.587613e−9、K<8.04；14688精确端点等式，真实cut半径逐字相等，z_b窗下radius<1.34/support>.08889。linear全模与低模二次项精确同频合并，其余二次项严格余项支付，未截掉图模式。全1152段batch79634正在共用唯一接点，保stage0/127和deep锚；fullH尚欠。

- [.25相邻共享R段](notes/2026-11-20-warm025-shared-r-adjacent-stages.md)128/143/144已付48完整片×全角，metric≤8.716666e−12、K<8.000106；44064精确端点等式，127/128与143/144实际接口共一份R/Cartesian二jet，stage127原整图不动。全batch固定0/127两端优先、deep唯一锚；fullH与全域继续。

- [实际桥cut完整两jet](notes/2026-11-20-m24-true-bridge-cut-r-two-jet.md)已真导出，固定R=ahat(s)而不偷换实际a*；219个精确qYjet、真M/M′、同符号Zc及49/25 Fourier迹供两侧共用。高度零模R导约−.08005981069、RR导约1.86392648427，均值导数债仍在；尚未拼warm/fullH Cartesian seam。

- [.25整cell7](notes/2026-11-20-warm025-shared-r-cell7.md)stage1008..1151共144段/2308片已全角全R连续通过，metric≤4.885242e−25/K<8.001，2118744精确端点等式、143内缝和圆领唯一锚逐字共用；已接深盘组件。其它cell及fullH继续，不重已付部分。

## 继承的接续断点（2026-11-18）

- m3 已完成λ.02/.04/.08/.16/.32/.64有限锚但metric未门；最新完整CPf55b4f…/metric8.726888546e−4。直接λ1的38274真实maxnodes/RMS1.06820865，随后Frenet正根margin−2.533498598e−7，无新实际尾/完整metric，失败raw保留。175e同native provider从完整λ64启动λ.82（91205/439498、qseed.05336960976112643）；环境中断后状态未知。恢复环境后先读原进程/输出，不重inner或重复启动；1a5a同provider strict partial恢复源已精确保存、尚未执行。R47/R48/R49已备真实高M接口和均值条件，R50另证固定窗口弧外全正时端点控制空间C4稠密并逐层保迹/两矩（无统一率或BVP收敛），R51再给固定真实主矩与保护弧半径下的有符号圆心必要界，须区分法向角与材料坐标，不能作10%存在或排除。partial升M必须另声明标准入口的(1−λ)修正及真实新维尾。最终幅度、固定全部g/物理参数/时间范围的精化、闭合和连续几何仍未付。
- n4 新b=.16/λ=.02/M20：96568完整原联立已真成功，4次实际尾均过原门，末c782c31…/1240Jac+audit；完整CPdb78f248…2282点/RMS9.97643e−9，prefix metric8.91023257e−7、BC1.37309e−9。实际q=.012488348123231355及19c仍为未知，fixed=True只冻物理轮廓，不能算README#5全参数固定精化。mean2/nonmean2 seam−4.39895e−9/3.18959e−7如实保留。27744同g/J16升M24后tail1/2已原门接受1.973505059e−9，inner0真过2282点/RMS9.976202498e−9、raw56594/sidec4725已存；q漂移至.012488289412475258，call3新24H已发。失联后状态未知，恢复后接原返回点；λ1/完整闭合/10%未付，辅助halfH和旧失败不重，不新增fullD门。
- 固定M16 checkpoint的尾32→64步使真实R metric下降12.66倍，但全尾二阶差仍.00629485。R27真背景积分已严格区分工厂值；R29/R31补全同一低幅实际闭图全角/全径向/全相位metric<1e−6，桥真积分/舍入/共用固定atlas全部支付。转入有实质幅值提升的实际圆弧与真尾，不重复低幅几何铺盒。R36给真积分/反函数oracle及固定atlas转移，R37已补同实际raw核的全角余项；R39进一步付全径向系数/中心差/真实atlas，ε<5.940838571e−9，仅若同图有限主部metric≤9.88118311e−7才推出真图<1e−6。R39完整有限主部到R31卷积的exact Fraction接口已执行，见integral-principal-polynomial-interface；只核代数接口，不用形式半径1作物理metric。该主部门未算、当前M8不合格；下一项是新合格实际候选的完整metric/尾闭合，不搬旧数值界。
- R28新M16/64步图自身几何和非零帽已给全O(3)非全等、reach/D>.04345、held/D>.00546266；不能移用M8矩，不能把低幅闭图称10%完成。连续几何不再重复铺盒。

细节与真实执行索引见HANDOFF及最新日期笔记。下列O1—O系列保留原问题与历史更新；已登记的结论不重新计算。

## O1. 建立可用的几何与复现起点

从 R114/flat17 和 true A 族提取实际位置公式、度量、闭合帽、固定握持区、全时变化的定义。先定点读结果及最小脚本，不重新运行旧课题已经登记的计算。查明 5%–6.3% 的限制来自核心形状、帽的直径、曲率还是非局部 reach。

## O2. 达到 10% 的候选

R1已给温和椭圆的精确尺寸/支撑/曲率预算，但未构造满足预算的连接器。直接位置法目前出现过尺度逃逸和高曲率边界层；改用固定E规范、真实曲率及支撑约束继续。另已恢复旧13.2%开放前缀的原两jet，尝试更厚的新尾（允许额外高度，不沿用旧20%目标的过窄尾预算）。

同时探索形状/谱/闭合帽参数设计和不同构造。必须计算整像 Hausdorff 距离，不以材料点位移代替；所有比例用完整 $D=\operatorname{diam}F_0(M)$。握持区允许不连通但必须有内点和直径至少 $0.2D$。正的整像变化不自动给出 $\delta_{\rm E}>0$。

小cut q20现已定义严格C²的有限表示并精确修复中心接口；R11已连续认证开放prefix嵌入、曲率<8、D<3.018及witness>.325，开放集合比例>.1076。外端尚未闭合；要把前缀优势转为闭族，应实现rXY≤.35、增高≤.25的实际非线性尾，尾本身仍需κ/support/尺寸的连续区间证书。见smallcut-c2-center-and-geometry笔记。

R57已排新profile的准确k=.45 reach合格节点。数值设计可经过未合格中间模型，但不可搬最终k=.2的保护窗结论；当前从λ0设τ1进入。R8正K入口退化延拓仍未知。

## O3. 固定候选的全部条件

固定完整g时须同时保持原尾背景校准/warp定义：H请求本身不重调背景，跨calibrationSteps/背景积分设置则可能换g。独立完整ready/checkpoint绑定已备，未执行新的固定参数场解；不能只冻结短port的cut。

R56现已给出只用C²二jet范围和真实目标g一阶范围的连续矩阵证书，并证严格余量下有限细分终止。下一步是对实际合格候选支付全部连续范围输入；当前浮点DFT/样点不能代替它，不需再求同一个抽象充分定理。

只有达到幅度与厚度的真实候选才进入固定 $g$/参数/$t$ 的空间、角频率和时间加密；完整检查两帽、拼接 $C^2$、全域相对度量误差、全时嵌入/局部曲率/非局部 reach，以及含反射的非刚体性。有限样本与严格连续区间结论分开报告。

## O4. 交付与继续加强

提供若干时间网格的可复现生成命令和哈希，单个网格 <5MB；按根 README 第15条不把可再生网格放入 Git/Release。解释数值解与严格存在之间的具体缺口。完成后继续提高 $\delta_{\rm hold}/D$、$\delta_{\rm E}/D$ 并报告 reach$/D$。

## 尚未获证的事项

目前没有本题完整候选，没有本题的 10% 存在性证明，也没有可用于替代全部检查的条件定理。障碍结论、文献综述和参数筛查只算中间进展。

## O5. Gauss–Codazzi 的完整边值路径

使用R2的三场系统（末端不除N）和a(s)设计，联立椭圆入口与平面圆领条件。已有短局部圆整，但正曲率段的单向谱射击不稳定；不能把局部成功当闭合。三场BVP与周期位置重建现已实际实现，但数值未通过（notes/2026-11-17-gc-complete-bvp-attempts.md）。低阶有限端段未解决退化边界；继续改变端部表示并接合已有振荡尾。


## O6. R3换握持机制的实际圆弧闭族

圆弧核心保留精确γ、ρ=h+h''平段，PDE只对未知场作谱离散；不能把有限投影误当精确圆弧。先检查局域控制基的真实terminal Jacobian与支线是否可解，R5已在精确C3旋转度量/Cauchy前提下证明二维片的保持及其相位条带；仍需先得到满足该前提的实际完整前缀。R6已给3fold固定帽的非全等性条件证明及显式几何预算，仍须在真实候选上选定参数并认证活动矩。继续支付全域metric/收敛和全时reach。窄圆弧的病态控制是实际风险，不把有限矩阵方阵计数当存在性。若成功，整体逆刚体对齐可直接把圆弧片作为H，不需新增杠杆。

## O7. 正曲率带的局部刚性与新负曲率段

R8已证明完整正K环带内的圆弧片必须k=1才可能嵌入；从退化边界到内部的唯一延拓仍未支付。保持H的原度量，增加负K加速使R5保护窗在正K带之前耗尽，只是避免已知保护域触及该带的设计条件；仍须全局非线性BVP和同g加密，不能把角窗耗尽当实际圆弧消失。

## O8. 实际非线性尾与二阶缺陷

首批实际尾只到完整q18端口的λ=.0781；原g在λ=.07的M8→M12 metric下降，但A谷的Gauss相容仍有缺陷。需把M16及更多表示的共同Cartesian二jet与Gauss误差一并核查；新首cell/平谷的DN必须与前缀重匹配，最终λ=1且全部端口模数/均值/两jet同时一致。有限Gram图扩张不替代谱极限。复现与已失败路径见nonlinear-tail-stage1笔记。

## O9. 实际前缀—尾联立的后续验收

已用原接受门通过beta8新物理g的q=.0002和q=.0004有限联合求解；须继续增幅并冻结候选，再核完整Cartesian公共两jet、同g模式/深度收敛与实际C²圆领/平盘闭合。记录见actual-prefix-tail-coupling笔记。小幅度联合成功不补足高q旧线性前缀的接口。

R12已支付精确接缝的结构定理：h正定时高度二jet和度量一jet决定整圈Cartesian二jet。数值剩余工作是共同正下界、连续误差传播及明确C²拼接，不再把精确问题当额外独立边界方程。


## O10. A图与真正几何障碍的区分

R15证明保反射、D>0、从背景相连的同g幅度分支在非零K轴上不能穿A=0，但现有λ.0781点所需精确轴曲率仅.3906，未超预算。优先降低真实Gauss/二jet缺陷；若进入平谷负A，必须完整匹配锥或其他平谷解。破坏反射、换投影图或独立非背景分支各有不同未知量与边界条件，不得因局部代数允许而称已构造。

## O11. 双脉冲联合支与新的偶数对称圆弧核心

自适应尾已实际联立至q008，q004同整g两层的metric/fullD明显下降，q002全Cartesian两jet仅采样差约2e−10；仍需可见幅度和全闭合。q008二阶缺陷与曲率预算恶化，原tol失败/放宽重试分别保留。并行推进m3较小cut的真DN联合，以及n4精确圆弧中央柱的换握持机制；两者都须实际解出完整prefix—tail，条件比例窗不能顶替。详见adaptive-actual-coupling-and-fixed-g笔记。

## O12. 真实混合首cell的几何验收

R18在真实非恒定cell的混合根已求出；physical h=rwv,p=w²t显著减小节点状态误差，但直接插值仍产生严重二阶缺陷。保留全部v/H坏插值和line-search失败，转精确旋转背景+全Cartesian扰动共享二jet五次表示，继而同g径向加密。节点残差、形式rr或有限Jac都不能替代实际图的C²、metric及Gauss检查。

## O13. R19四重核心的实际闭合

R19已严格给中心对称Hausdorff下界、中央柱公共H、四重基准加二重固定帽的全O(3)非全等与有理10.075%条件窗。H已留.001材料角余量。仍须解出精确圆弧核心到真实非线性尾的全前缀、中央C²接口、实际尾圆领/平盘闭合、同g加密和全时连续几何；普通n4短循环λ1/M4的metric.00407未通过，低线性端口也不证明圆弧可解。新的负K轮廓须实际通过，而不是仅耗尽特征窗。

O12更新：精确背景+共享Cartesian二jet已严格定义有限C²图；uniform16→32的metric下降但完整tensor增大，critical入网已有解的tensor仍约节点floor15倍。新表示不等于等距极限。后续如升角模，须先声明完整内端动量边界lift，不能凭8列补零当继承真实高模。

O9更新：m3 q02真联合及同g M8径向对照通过，实际Cartesian接缝和完整均值已数值核；prefix内部二阶插值缺陷、M8 tail fullD仍待加密。M16原shoot的Riccati校正病态失败不等于物理Gram/A失败；转M12或完整稀疏shooting Newton校正，门不改。q06 secant成功仍是开放线性DN。

O13更新：R19A给更窄保护弧的严格10.676%条件窗（q=.06,R=.1,a=.145,α=.0285,ℓ=.51），允许完整D≤2.5/K≤13.2。窄H宽.0004但有内点，直径由柱长支付。普通fast背景仅采样/线性诊断，不能当实际闭族；新窄弧BVP正在进行。

O13新结果：旧窄弧M6小步至λ.7的投影接受仍伴metric.01258，λ1触节点上限。新补集矩控制可改善有限条件数，仍须审查未表示高频和同g极限。完整无限非线性尾不是有限C²闭图的唯一途径；可采用原共享二jet圆领使有限扰动消零，再接已证平坦的旋转背景/圆盘，但该圆领和全图误差都须计入验收。

O13/R20：无条件圆弧—主频距离下界已证，条件切空间障碍明确要求完整核与可微支。补弧Gram证明有限矩兼容，因此不能把数个高模乘子或控制条件数解释成完整不存在。正在先提高q再作圆化设计，所有设计链与同g验收分开。

O9进一步更新：M16八段全节点真联合已通过原门，tail完整D降至2.735e−7；prefix仍9.015e−6径向平台，1965节点/tol1e−8实际BVP继续。旧M12与M16两段稀疏版本已取消且没有数学终态。见m3-fixed-m16-parts8-and-radial-floor笔记。

O9/R21更新：实际固定M8有限尾的深端已以字面共享Cartesian两jet圆领接平盘，并完成背景区间归一化/曲率及圆领盘连续几何；root独立Fraction复算全同。对象仍有外边界，外有限尾仅采样，完整prefix共缝和全闭/全时证书继续。不得把这一组件证书冒称整个闭面。

O13双模更新：实际原n4端口下root03同时使mode4/8有限线性条件近零，原BackwardLine与物理双参数Jac独立核验；新a.147/D2.65/K12.5条件比例窗有Fraction证书。非线性双模场及真实尾/闭合仍未付，不能由线性满秩升级为存在。

O9径向层已实解：同整g M16从983到2462节点，实际C²图metric降85倍至5.845e−11，tensor降4.63倍至1.947e−6；真正尾仍原门接受。见m3-true-radial-refinement。全闭表示的同g误差仍待合并，增幅另行设计。

O13双模首解：λ0 q005/M6设计已求出，冻结完整δ/vd后M8 metric4.262e−6→5.733e−7，tensor .002042→.0003271；核心幅度和c8为未知，非固定core。角谱诊断定位遗漏28/32模。仍需圆化、真实非线性尾、完整闭合与更多同g层，见double-prefix-first-and-fixed-g。

O9增幅初始化：q025首个momentum坏状态已原式复现，局部同伦触原A floor .05，未到完整shoot/prefix，非真实容量结论。小步q021和直接旧accepted全部states作原shoot初值的对照继续；新cut残差必须由原Newton/线搜索支付。

O13/R22：双谐波精确极小极大距离及固定中心半径的最优eta已证明并独立有理核验；近圆弧误差为四阶仍不为零。条件支障碍仍缺完整核与可微性证明；新eta>.333的全圆rho预算已更新，不可沿用旧正性界。

O13实际圆化：q05/M16 λ.005初猜实rho<0未入BVP；λ.0001原BVP接受却完整metric2.60e−4、tensor2.53，不能通过。完整高频与内部角表示仍须处理，低矩或入口lift准确不补这项缺口。

O9/R23：真实fixed-M8已成为完整显式C²闭面，连续全曲面K≤10/support>.7/reach/D>.0434，全部相位同界；公共mean和相位角图的严格C²已支付。零marker时δE=0、q02幅度不足，完整同g metric与M16全闭加密仍须审计。这个结果解决闭合几何，不解决10%。

O13双模更新：λ.05 M8完整metric失败，λ.1maxnodes；旧M12同g对照趋近q=0且metric仍未过门，不能当保幅精化。固定J8的真正嵌套已完整初值/rho/Jac审计，新的同gM12正在实解；具体限制见double-prefix-nested-refinement。

O13厚度预算：n4同轮廓q06虽投影接受，完整二阶缺陷.04005；偶数对称给D≥2Rxy，数值K与R给reach/D必要上限0.0294865780848<.03，尚未区间认证。应改变物理形状/轮廓，不将该有限图更高q当合格候选。

O9初猜对照：原旧态可健康起步，但q025线性放大H的完整Newton预测仍在原线搜索iter3失败；不代表实际q025 coupled幅度上限。旧态直接法明确取消。下一关键证据仍是第二个真联立幅值态，M16与M8设计对照正在运行。

原直接design的[.04/M32实际返回](notes/2026-11-26-original-design-lambda0040-memory-return.json)也为MemoryError、无raw/physical/RMS；returncode0不作成功，栈未投影，不借独立v5栈归因。真.032仍接受锚，当前attempt008的目标尚未实露。独立完整割线已另到.064/M40；不把两条链的状态混合。

[v4第二.003/M24实际返回](notes/2026-11-26-v4-second-actual-return.json)为status1/3130点/RMS.0439794，虽scaledBC3.89058e−8和physicalBC4.65616e−12已过，仍未接受。5接受步/minα2^-20/域拒16/merit拒101，未曝光细分域原因；从真实zero锚.002二分.0025进入第三次，不晋级该失败场。

完整割线链的[λ.128/M40实际尝试](notes/2026-11-26-original-design-secant-lambda0128-domain-return.json)使用真.064/M40完整raw（此时仅一个真M40锚），报Adaptive Frenet domain failure: -9.69571782897475e−9；无raw/physical/RMS，栈未投影，不断言是初始域、δ差分或增网造成。保持原域门、真接受.064，父链自然attempt004，不clip或晋级异常场。

原直接分支[新λ字面0.036000000000000004/M32行](notes/2026-11-26-original-design-lambda0036-accepted.json)已全原门通过：2325点/RMS8.13144e−7/metric6.58945e−7/物理BC1.31858e−12；run8ef7fd02。保留summary result仍写.032的滞后原值，实际accepted row与它分别记录，不静默改写。当前attempt009下一目标未露；全局已知前沿仍是独立secant的.064/M40。

[λ1来源接原完整DN的窄协调入口](notes/2026-11-26-original-lambda-one-chord-native4-entry.md)已实际通过compile/help；仅支持真实原R53或v5 solver来源，保原full-H/J/audit/8outer，复用同VM chord3/native4及已验streamed执行身份。当前λ1输入仍缺，未启动新尾；配置/Cartesian mean/全闭同g缺口均不因此支付。

已核[v5 actual设计→固定g](notes/2026-11-26-v5-design-to-fixed-actual-dn-interface.md)和[原R53 λ1实际场的两种固定未知空间](notes/2026-11-26-r53-actual-to-fixed-metric-interface.md)。须冻结最终actual δ、完整字面径向/角图、源Cartesian mean/primitive和尾背景；首步明示未接受初猜真求解，不能伪造线性锚。现有五件actual-refinement入口的KIND/1168/端点频率分支需窄适配，R53几何factory本身无.002锁。当前均无λ1/full-DN输入，不构成精化结果。

[跨M完整lift割线入口](notes/2026-11-26-cross-mode-secant-entry.md)79ebe59d已通过语法/CLI及非平凡径向图独立代数核。分别核真锚，以左自己的λ/δ/图作原系数1完整lift，再按共同t与右原cubic外推；不造M40接受锚、cubic或physical，不把不同mean解释成同g。计划消费material VM自己的.032/M32和.064/M40，尚未真实生成预测或BVP；实际续入须独立CLI并重过全部原门。

[独立lifted-secant续入](notes/2026-11-26-lifted-secant-continuation.md)519c已真实compile/help与原控制流AST核，旧在跑源不改。只有低M真锚预测改走独立CLI，同M原预测及实际solver/验收/metric-only升M/失败二分不变；自然返回后从实测最高真锚接续。三个活跃通道只热加inner-00的status/nodes/rms投影；内层返回即使status0也不冒完整metric/physical接受，未投影参数向量。

原直接链[新.04/M32真实接受](notes/2026-11-26-original-design-lambda0040-accepted-after0036.json)来自真.036/attempt008：2325点/RMS8.17719e−7/metric6.79248e−7/物理BC5.72873e−16，run4f89af1d/raw52a7d250/physicald8799e16。13原接受步/minα2^-17/域拒1/merit拒22；此新输入通过不抹掉旧.032→.04 MemoryError。summary滞后.036但实际source证明确实续真.036；当前attempt010，最近同M真锚为.036/.04，全局前沿仍独立.064/M40。

[v4第三.0025/M24真实返回](notes/2026-11-26-v4-third-actual-return.md)仍status1/RMS.0174015失败，虽scaled/physical BC已过；父三次段已结束，真接受锚仍.002，不执行字面下一.00225或重复失败链。新[低模→完整M24原DN](notes/2026-11-26-seam-low-mode-tail-route.md)从同一完整来源H先求M8的五档再M16/M24，保原背景/门/audit/J/native4/chord3；fresh恢复6801字节逐字同，改变表示和未接受初猜，无联立/λ1/同g宣称。fresh warm请求已准备，待实际run；probe余时不足一小时，不重复同实验。
