# HANDOFF — Astra-held10-f00f08c9-20261117

维护会话：**Astra-held10-f00f08c9-20261117**（AI）。开始：2026-11-17 19:55（UTC+8）。状态：**进行中，尚无满足全部完成标准的候选**。

## 目标、规则与同步

连通闭曲面连续C²等距嵌入族；固定有内点闭H且diamH≥.2D；整像δhold≥.1D，含反射取商δE>0，全时reach≥.03D。同一固定g/物理参数/时间范围metric≤1e−6且加密下降；材料位移、solver success不能替代。

- 已部分克隆、真实pull main并全文读根README（含授权）及题README；只稀疏检出本题/自己的workflow。
- 已读规则提交：`4569355a30d8b9efd3dd1b4269cf8c57f4cbc19b`。2026-11-18 01:17:20（UTC+8），真实 pull/rebase 后双 README 差异为空。下次真实 pull 最迟 02:17:20；每次 pull 后比较这两份 README，只读变化并立即执行。
- 每结论更新本文件并普通push；非快进立刻pull --rebase重推至成功，禁force。每pull比较双README，只读差异；至少每小时一次。令牌只临时命令行。
- 证明进results，数值/条件/缺口分开；可重算数组/mesh/checkpoint/CI artifact不入Git/Release。H<10KB，单Markdown<100KB，不写根LOG。达到完成标准后继续增比例。

## A. 主体几何与高q开放前缀

旧线性DN smallcut高q前缀：同g q20 M20→24 metric9.93e−7→4.172e−9；q22 M28→32 1.133e−6→1.119e−8，actualq=.2200009075/K7.18978、精确coreρ>.2449985。均开放。源码恢复及各profile/chart/二jet见smallcut-high-q-and-fixed-g、q22-fixed-metric-refinement笔记和recover_prefix.py。

R11已用全Cartesian Fourier/共享二jet五次Hermite、s≤.04解析lift精确支付中心C²；843264区间盒覆盖全q20有限prefix，σ>.349674、R<1.508969、witness>.3254827、K<8，P/J>0证明完整上下环带嵌入。开放D<3.018、held比例>.1076；不是闭面/精确等距/reach。源码见cartesian-tensor-prefix笔记。

R13条件窗：若同一prefix接实际尾rXY≤.35、顶高≤1.5265414843、K≤10、σ≥.3且C²闭合，再加R7双帽/短柱，可有held/D>.10338、reach/D>.03191、Hdiam/D>.76。尾假设未付。K10是充分窗口，不是题目硬约束；应检查KD≤33.333及support/D≥.03。

## B. 实际DN联合与当前数值入口

历史实际非线性尾见adaptive-actual-coupling-and-fixed-g、widecut、ports、actual-prefix-tail-coupling和nonlinear-tail-stage1笔记。保双脉冲q002联合及q004同整g M8→M12已通过，q008二阶缺陷/K恶化；小幅成功不补高q接口。旧端口恢复、错误规范修复、所有失败与取消均保留。

**m3真联合固定g**：δ=.06105607686781097，完整g SHA11a9…b125。M8→M16八段均用原2e−9门通过：实际q=.0200012257089，tail res1.161e−9、metric1.587e−11、全D2.735e−7/minA.440917/K8.040692；M8全D2.345e−6。完整512角单刚体Cartesian缝最大Xss差3.315e−9，高度两jet≤6.17e−12。真正同g径向BVP已到2462节点：metric4.971e−9→5.845e−11，完整tensor9.015e−6→1.947e−6；尾同层误差不变。旧节点全部保留、峰的桥段区间宽减半，未替换ODE jets。实际q=.02000154623、tail res1.161e−9/mean缝3.49e−13。见m3-true-radial-refinement及同名包；新q025初始化在cell0/segment4局部momentum root触原A floor.05，尚无全局res，非容量界；q021与直接旧accepted states原shoot起步对照继续，见m3-q025-initializer-local-root。全节点稀疏Newton等价及split原映射一致已核；八段降低stage放大而不改原门。旧M12与两段稀疏M16明确取消exit130（末res2.083e−9/6.970e−7），非数学失败。详见m3-fixed-m16-parts8-and-radial-floor及对应两包；旧入口m3-smallcut-true-coupling-and-secant-prefix。q04/q06只线性DN prefix，非真联合；幅度不足/全闭验收未付。

n4精确圆弧+中央柱：R19/19A证明整像中心位移下界、固定两fold帽排除O(3)、公共H及两个有理10%条件窗；全闭前提未付。宽弧旧M4 λ1 metric.00407、窄弧旧M6 λ.7 metric.01258、λ1maxnodes，完整55源/70源恢复见n4-first-batch-and-consumed-window、narrow-old-basis-terminal-results。新C4补弧矩基已冻/实恢复；q005 M6 λ.3maxnodes，λ.1 metric1.224e−4；λ0设计链至q045/M16：metric5.499e−8、tensor.0014915/K13.2628，未圆化且仅线性DN。新material-angle回拉+q04/q045双态secant使q05/M16一次迭代接受：1220节点、metric2.322e−8/tensor.000245/K14.0966；旧q05M16/M20取消exit130非数学失败。q055/M16也一次接受：1283节点、metric1.003e−7/tensor.002246/K14.9898，δ=.03011246227；非同g精化，见n4-q055-material-secant。q06λ0一次接受但metric7.660e−7/tensor.04005/K15.9544；由采样K和两对称点给reach/D必要上限约.02949，尚非区间证书，见n4-q060-and-local-reach-budget。q05圆化λ.005初猜实rho−.271被拒，λ.0001投影接受却metric2.60e−4/tensor2.53失败，见n4-q050-first-circularization-failures。入口complementary-controls-and-first-prefixes、n4-q045-prefix、n4-material-angle-warm-start及对应包。

新n4双模线性root03：vu.4/vd.2644695137/δ.02840070836/ramp.45，原port24未改；τ4≈5e−14、τ8≈−3.6e−11，原BackwardLine复核非零向量/正尺度，双参数Jac σ约408/.675。背景K<8、耗窗>.147721；R19新a.147/α.029/ℓ.54在全闭D≤2.65,K≤12.5,σ≥.08前提下held>.10261、reach>.03018、H>.20377，root Fraction逐字复核。见n4-double-linear-resonance及double_resonance_linear；实际双模λ0 q005/M6→同g M8，δ=.02840699270/vd=.26450353591冻结，metric4.262e−6→5.733e−7、tensor.002042→.0003271；固定g释放c8、实际q=.004959299，非固定核心。旧core换坐标两jet差<2e−15，首遗漏ψ模28/32定位角截断；见double-prefix-first-and-fixed-g及double_prefix_first。双模λ.05 M8 metric2.118e−5/tensor.05164失败，λ.1maxnodes；旧同g M12虽solver接受却q塌到7.198e−6且metric4.232e−6未过门。现固定投影J8使M8→M12完整core/初值嵌套，原rho门保留、λ0显式拒绝；独立新BVP继续。见double-prefix-nested-refinement。

## C. 接缝、A图与混合边值

R12：h=g−dz²正定时同g一jet和完整z二jet经一次固定平面刚体确定整圈Cartesian二jet；给误差链，采样不当连续证书。R14：同turning number/同严格Q符号支内，闭合总转角已决定mean zr，Darboux再定zrr；Q过零不适用。

R15：轴向精确界|A|≥|w_r|√D/(E^1.5 Kmax)；反射/D>0且从背景连通的振幅支在非平谷轴上不能A变号，非用户相位族普遍限制。旧λ.0781轴若精确仅需κr≈.3906，尚未超预算，Gauss缺陷1.388e−5才是问题。R10有低K精确锥环带A变号，但匹配需Hr=H/r、Hrr0、均值/共顶点，不可免费贴入。

R16有限不定Gram可用但无过零权L²一致逆；R18完整cos/sin/mean混合DAE原引擎核验已过。实际首cell physical h/p坏插值与K达8e4、共享Cartesian二jet后tensor未下降的失败均保留。见actual-cell-mixed-coordinates-and-bad-interpolation、actual-cell-shared-cartesian-c2及mixed_dae/actual_cell包；有限根与C²表示均不代替误差收敛。

R17给无轴反射二fold核h=1+qcos2φ+εsin4φ；q.2/ε.005时ρ≥.325、Re AC>.5456625，精确卷积已核。但需要全cos/sin+均值BVP，非免费自由度，旧象限证书不移用。

R20：精确圆弧与任意主频的ρ一致距离≥(n²−1)q tan²(na/2)；n4/a.145的系数严格>1.3357528678，Fraction独立同字节核验。仅在完整线性核+可微支假设下排除固定宽圆弧小q支；有限高矩可用补弧Gram任意修正，不得由有限τ推不存在。

R22：双主频到圆弧的精确距离为(n²−1)q(1−c)²/[(1+c)(5+c)]，c=cos(na)；n4/a.147系数>.0395989054489351，Fraction独立逐字同一。中心半径固定的最优eta=1/[3−4(√2−1)(1−c)]≈.367413，须用更新全圆rho界；尚未进入BVP。切空间推论仍要求完整核/可微性，不由有限共振推出。

R21：实际固定M8 finite tail已定义4638节点/73系数C²图，共2jet圆领接半径.05平盘；组件仍有外边界。背景完整区间给λ>101.60、增高[.01722689,.02886511]、K≤8，深根范围仅引用旧背景定理。圆领/盘连续σ>.8、norm<.817、metric<1.36e−29、K<8.002；root独立Fraction结果全同。外尾仍仅采样metric3.597e−8。完整共缝、全闭几何/收敛继续；包finite_closure/m3_m8_collar_disk。

R23：实际m3 fixed-M8已完整C²闭合为S²：共享中心/全cut二jet、同一mean、有限尾圆领平盘。504320全prefix盒+4637段全尾连续界给全曲面σ>.7、K≤10、D<2.30242、reach/D>.0434。相位角亦共享二jet，Fraction证明角Jac>.8399，故全相位C²连续；root独立cut/组合输出逐字一致、角界完全一致。零marker时δE=0，幅度不足，整域同g metric未证；不能当10%。见R23及finite_closure/m3_m8_closed_map。M16径向细层全闭审计继续。

## D. 其他结果和来源

历史证明R1–R10见results：椭圆/圆弧条件窗、平领二jet、条件特征保护、固定帽排除O(3)。R8只证正K完整带内圆弧必须k1，K0退化入口唯一延拓未付；R9负K耗窗>.92只是设计；R10锥支必须补齐均值/共顶点/完整二jet。旧GC/短领失败全部保留于notes/scripts；来源R114/flat17仅held>.0527832、reach>.0312033，R115及旧.063未解决本题。

## 当前接手分工

literature_mechanisms：真实有限尾圆领/平盘闭合；new_construction：m3固定g径向精化；true_a_analysis：双模共振n4真实非线性BVP。主会话：n4圆弧新构造、证明/连续几何、规则同步与逐结论push。open.md列全部缺口；完成前持续研究，不停在阶段报告。
