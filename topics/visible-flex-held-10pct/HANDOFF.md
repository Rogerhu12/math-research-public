# HANDOFF — Astra-held10-f00f08c9-20261117

维护会话：**Astra-held10-f00f08c9-20261117**（AI）。开始：2026-11-17 19:55（UTC+8）。状态：**进行中，尚无满足全部完成标准的候选**。

## 目标、规则与同步

连通闭曲面连续C²等距嵌入族；固定有内点闭H且diamH≥.2D；整像δhold≥.1D，含反射取商δE>0，全时reach≥.03D。同一固定g/物理参数/时间范围metric≤1e−6且加密下降；材料位移、solver success不能替代。

- 已部分克隆、真实pull main并全文读根README（含授权）及题README；只稀疏检出本题/自己的workflow。
- 已读规则提交：`f2be884234b18c0d5e8cf4090c70ae43f1e51b8f`。2026-11-18 00:52:30（UTC+8），真实 pull/rebase 后双 README 差异为空。下次真实 pull 最迟 01:52:30；每次 pull 后比较这两份 README，只读变化并立即执行。
- 每结论更新本文件并普通push；非快进立刻pull --rebase重推至成功，禁force。每pull比较双README，只读差异；至少每小时一次。令牌只临时命令行。
- 证明进results，数值/条件/缺口分开；可重算数组/mesh/checkpoint/CI artifact不入Git/Release。H<10KB，单Markdown<100KB，不写根LOG。达到完成标准后继续增比例。

## A. 主体几何与高q开放前缀

旧线性DN小cut主参数r=.3,w=.08,w_r=−1.8666666667，vu=.55/vd=.6，ramp .4/eta .05/cycles1，ShortBridge K4/p.2。同g精化q14 M14→16 metric1.16e−7→1.168e−9；q18 M16→20 9.98e−7→2.429e−8；q20 M20→24 9.93e−7→4.172e−9。q22 M28→32 1.133e−6→1.119e−8，actualq=.2200009075、K7.18978；精确有限core ρ>.2449985、Re AC>.5809146。均未闭合。

复现scripts/recover_prefix.py+prefix_recovery_manifest.json，smallcut_prefix_sweep.py建chart，smallcut_secant_launcher.py延拓，fixed_refine_smallcut.py冻结g，smallcut_endpoint.py出完整均值二jet；详见smallcut-high-q-and-fixed-g、q22-fixed-metric-refinement笔记。

R11已用全Cartesian Fourier/共享二jet五次Hermite、s≤.04解析lift精确支付中心C²；843264区间盒覆盖全q20有限prefix，σ>.349674、R<1.508969、witness>.3254827、K<8，P/J>0证明完整上下环带嵌入。开放D<3.018、held比例>.1076；不是闭面/精确等距/reach。源码见cartesian-tensor-prefix笔记。

R13条件窗：若同一prefix接实际尾rXY≤.35、顶高≤1.5265414843、K≤10、σ≥.3且C²闭合，再加R7双帽/短柱，可有held/D>.10338、reach/D>.03191、Hdiam/D>.76。尾假设未付。K10是充分窗口，不是题目硬约束；应检查KD≤33.333及support/D≥.03。

## B. 实际DN联合与当前数值入口

**最新自适应双脉冲尾**：331物理设计后，前三cell保持双脉冲/九段、n≥3不变。q=.002实际联合δ=.1718183369254722，prefix metric1.214e−9、outer1.059e−10、tail fullD5.053e−11/minA.9370。512同材料角全Cartesian二jet最大差1.816e−10；差分半步2.427e−10。新导出器漏momentum×2^a已修，旧错hash保留。有限采样prefix R1.500743/K4.087、tail R1.329006/K9.961，非连续/无限尾证书。

自适应q004同g M8→M12的prefix metric2.437e−9→2.615e−10、tail fullD1.94e−8→2.58e−11，K10.359；两层非极限定理。q006原tol失败后显式3e−6通过，q008 fullD4.687e−6/K12.319。入口adaptive-actual-coupling-and-fixed-g及adaptive_coupled_seed_deliverable，65源恢复已验。

历史实际尾：widecut r.35/w.3两次真联合q.001013/.002通过，后者fullD2.214e−6；72源恢复已核。beta8 q.0002/.0004通过，q.0006失败不是容量；旧高谷仅q2e−6，删脉冲恶化。beta8 p05线性q10通过/q12一次失败，32列原端口再生逐值同一；旧39源漏.cjs，需完整71源/PadTo展开160。入口widecut、ports、actual-prefix-tail-coupling各笔记。旧q18 forcingλ.07同g M8/12/16 metric下降但fullD1.96e−5/1.15e−5/8.23e−6、Xrr差.00382/.00130，非无限尾或C²误差收敛。

**m3真联合固定g**：δ=.06105607686781097，完整g SHA11a9…b125。M8→M16八段均用原2e−9门通过：实际q=.0200012257089，tail res1.161e−9、metric1.587e−11、全D2.735e−7/minA.440917/K8.040692；M8全D2.345e−6。完整512角单刚体Cartesian缝最大Xss差3.315e−9，高度两jet≤6.17e−12。真正同g径向BVP已到2462节点：metric4.971e−9→5.845e−11，完整tensor9.015e−6→1.947e−6；尾同层误差不变。旧节点全部保留、峰的桥段区间宽减半，未替换ODE jets。实际q=.02000154623、tail res1.161e−9/mean缝3.49e−13。见m3-true-radial-refinement及同名包；新q真联合继续。全节点稀疏Newton等价及split原映射一致已核；八段降低stage放大而不改原门。旧M12与两段稀疏M16明确取消exit130（末res2.083e−9/6.970e−7），非数学失败。详见m3-fixed-m16-parts8-and-radial-floor及对应两包；旧入口m3-smallcut-true-coupling-and-secant-prefix。q04/q06只线性DN prefix，非真联合；幅度不足/全闭验收未付。

主会话新n4精确圆弧+中央直柱：R19已证明偶数中心对称整像dH≥中心位移、固定二fold帽简单谱排除全部全等；有理核心R=.325/c>.72061，α=39/250、ℓ=.7给shift>.34258。若完整D≤3.4、σ≥.11、K≤9.5，则held/D>.10075、reach/D≥10/323、Hdiam/D≥7/34，全部闭族前提未付。普通n4宽弧M4 λ1 metric.00407/全D3.801，固定M8触maxnodes；新负K head虽耗窗，但旧compact基高频放大使λ.15 rho失败。R19A已用Fraction给窄窗q=.06/R=.1/a=.145、α=.0285/ℓ=.51：若闭D≤2.5,K≤13.2,σ≥.08，则held>.10676,reach≥1/33,H/D≥.204。第一批55源/参数文件与70原源实际恢复见n4-first-batch-and-consumed-window笔记、scripts/even_circle/first_batch。两个新head有Fraction耗窗下界>.28，仍只有线性根。vu=vd.4/ramp.45窄弧旧M6小步至λ.7虽投影接受，metric.01258/tensor14.874；λ1maxnodes失败。详见narrow-old-basis-terminal-results/对应包。新C4补弧矩基17文件已冻结/实恢复；q.005/M6 λ.3maxnodes且λ.1 metric1.224e−4。λ0设计支到q.04/M16，未圆化且只有线性DN；见complementary-controls-and-first-prefixes及两同名包。λ0续至q.045/M16，1157节点、metric5.499e−8/全tensor.0014915/K13.2628，见n4-q045-prefix；q.05/M16与M20正运行。双模共振BVP另启；全闭前提未付。

新n4双模线性root03：vu.4/vd.2644695137/δ.02840070836/ramp.45，原port24未改；τ4≈5e−14、τ8≈−3.6e−11，原BackwardLine复核非零向量/正尺度，双参数Jac σ约408/.675。背景K<8、耗窗>.147721；R19新a.147/α.029/ℓ.54在全闭D≤2.65,K≤12.5,σ≥.08前提下held>.10261、reach>.03018、H>.20377，root Fraction逐字复核。见n4-double-linear-resonance及double_resonance_linear；实际双模BVP继续，线性根非完成。

## C. 接缝、A图与混合边值

R12：h=g−dz²正定时同g一jet和完整z二jet经一次固定平面刚体确定整圈Cartesian二jet；给误差链，采样不当连续证书。R14：同turning number/同严格Q符号支内，闭合总转角已决定mean zr，Darboux再定zrr；Q过零不适用。

R15：轴向精确界|A|≥|w_r|√D/(E^1.5 Kmax)；反射/D>0且从背景连通的振幅支在非平谷轴上不能A变号，非用户相位族普遍限制。旧λ.0781轴若精确仅需κr≈.3906，尚未超预算，Gauss缺陷1.388e−5才是问题。R10有低K精确锥环带A变号，但匹配需Hr=H/r、Hrr0、均值/共顶点，不可免费贴入。

R16有限不定Gram图detG≠0可用，但过零权无L²一致逆；15精确锥测试非谱收敛。R18完整cos/sin/均值µ-free混合DAE原引擎12组差≤3.34e−15，M32 Jac可1.5e14。实际首cell physical h/p节点改善但直接H插值metric3.68e−4、tensor.922、rr跳18.8，v插值K可8.01e4；40源已恢复。后改精确背景+全Cartesian共享二jetC²，uniform16→32 metric3.019e−7→1.078e−7但tensor .004547→.008295反增；cusp16 .002737仍有径向缺口。见actual-cell-mixed-coordinates-and-bad-interpolation、actual-cell-shared-cartesian-c2及mixed_dae/actual_cell各包；不称C²误差收敛。

R17给无轴反射二fold核h=1+qcos2φ+εsin4φ；q.2/ε.005时ρ≥.325、Re AC>.5456625，精确卷积已核。但需要全cos/sin+均值BVP，非免费自由度，旧象限证书不移用。

R20：精确圆弧与任意主频的ρ一致距离≥(n²−1)q tan²(na/2)；n4/a.145的系数严格>1.3357528678，Fraction独立同字节核验。仅在完整线性核+可微支假设下排除固定宽圆弧小q支；有限高矩可用补弧Gram任意修正，不得由有限τ推不存在。

R21：实际固定M8 finite tail已定义4638节点/73系数C²图，共2jet圆领接半径.05平盘；组件仍有外边界。背景完整区间给λ>101.60、增高[.01722689,.02886511]、K≤8，深根范围仅引用旧背景定理。圆领/盘连续σ>.8、norm<.817、metric<1.36e−29、K<8.002；root独立Fraction结果全同。外尾仍仅采样metric3.597e−8。完整共缝、全闭几何/收敛继续；包finite_closure/m3_m8_collar_disk。

## D. 其他结果和来源

历史证明R1–R10见results：椭圆/圆弧条件窗、平领二jet、条件特征保护、固定帽排除O(3)。R8只证正K完整带内圆弧必须k1，K0退化入口唯一延拓未付；R9负K耗窗>.92只是设计；R10锥支必须补齐均值/共顶点/完整二jet。旧GC/短领失败全部保留于notes/scripts；来源R114/flat17仅held>.0527832、reach>.0312033，R115及旧.063未解决本题。

## 当前接手分工

literature_mechanisms：真实有限尾圆领/平盘闭合；new_construction：m3固定g径向精化；true_a_analysis：双模共振n4真实非线性BVP。主会话：n4圆弧新构造、证明/连续几何、规则同步与逐结论push。open.md列全部缺口；完成前持续研究，不停在阶段报告。
