# HANDOFF — visible-flex-held-10pct

维护会话：**Astra-held10-f00f08c9-20261117**（AI）。开始：2026-11-17 19:55（UTC+8）。状态：**进行中，尚无满足全部完成标准的候选**。

## 目标、规则与同步

连通闭曲面连续C²等距嵌入族；固定有内点闭H且diamH≥.2D；整像δhold≥.1D，含反射取商δE>0，全时reach≥.03D。同一固定g/物理参数/时间范围metric≤1e−6且加密下降；材料位移、solver success不能替代。

- 已部分克隆、真实pull main并全文读根README（含授权）及题README；只稀疏检出本题/自己的workflow。
- 已读规则提交：`238e8c265b46877efa8f3c476909cc95a87024d9`。2026-11-17 23:56:27（UTC+8），真实 pull/rebase 后双 README 差异为空。下次真实 pull 最迟 00:56:27；每次 pull 后比较这两份 README，只读变化并立即执行。
- 每结论更新本文件并普通push；非快进立刻pull --rebase重推至成功，禁force。每pull比较双README，只读差异；至少每小时一次。令牌只临时命令行。
- 证明进results，数值/条件/缺口分开；可重算数组/mesh/checkpoint/CI artifact不入Git/Release。H<10KB，单Markdown<100KB，不写根LOG。达到完成标准后继续增比例。

## A. 主体几何与高q开放前缀

旧线性DN小cut主参数r=.3,w=.08,w_r=−1.8666666667，vu=.55/vd=.6，ramp .4/eta .05/cycles1，ShortBridge K4/p.2。同g精化q14 M14→16 metric1.16e−7→1.168e−9；q18 M16→20 9.98e−7→2.429e−8；q20 M20→24 9.93e−7→4.172e−9。q22 M28→32 1.133e−6→1.119e−8，actualq=.2200009075、K7.18978；精确有限core ρ>.2449985、Re AC>.5809146。均未闭合。

复现scripts/recover_prefix.py+prefix_recovery_manifest.json，smallcut_prefix_sweep.py建chart，smallcut_secant_launcher.py延拓，fixed_refine_smallcut.py冻结g，smallcut_endpoint.py出完整均值二jet；详见smallcut-high-q-and-fixed-g、q22-fixed-metric-refinement笔记。

R11已用全Cartesian Fourier/共享二jet五次Hermite、s≤.04解析lift精确支付中心C²；843264区间盒覆盖全q20有限prefix，σ>.349674、R<1.508969、witness>.3254827、K<8，P/J>0证明完整上下环带嵌入。开放D<3.018、held比例>.1076；不是闭面/精确等距/reach。源码见cartesian-tensor-prefix笔记。

R13条件窗：若同一prefix接实际尾rXY≤.35、顶高≤1.5265414843、K≤10、σ≥.3且C²闭合，再加R7双帽/短柱，可有held/D>.10338、reach/D>.03191、Hdiam/D>.76。尾假设未付。K10是充分窗口，不是题目硬约束；应检查KD≤33.333及support/D≥.03。

## B. 实际DN联合与当前数值入口

**最新自适应双脉冲尾**：331物理设计后，前三cell保持双脉冲/九段、n≥3不变。q=.002实际联合δ=.1718183369254722，prefix metric1.214e−9、outer1.059e−10、tail fullD5.053e−11/minA.9370。512同材料角全Cartesian二jet最大差1.816e−10；差分半步2.427e−10。新导出器漏momentum×2^a已修，旧错hash保留。有限采样prefix R1.500743/K4.087、tail R1.329006/K9.961，非连续/无限尾证书。

q004 M8与冻结同整g的M12/N256/steps64：prefix metric2.437e−9→2.615e−10，tail fullD1.940e−8→2.584e−11，δ严格.17181827062051344，实际q .004→.0040116065091，K≈10.3594。两层不是收敛证明。q006原tol1e−6触4000节点失败，显式tol3e−6重试及q008通过；q008 fullD4.687e−6/K12.319，几何预算恶化。其余design δ会变，不混同g。入口adaptive-actual-coupling-and-fixed-g笔记及scripts/nonlinear_tail/adaptive_coupled_seed_deliverable、adaptive_continuation_addendum，65源空目录真实启动已验。

widecut r=.35/w=.3：438物理优化后canonicalD1=9.86804231267902；真实联合actualq=.001013386及新designq=.002通过，prefix metric1.055e−10/2.390e−9，尾minA.6757/.3280。q002 fullD2.214e−6，不能凭小metric称C²。72源恢复器逐字再生canonical8；冷启动/弱gain/另一402设计失败都在widecut笔记。

beta8实际联合q=.0002/.0004通过，q=.0006内层maxnodes失败不是容量界。前三cell旧高谷块仅q2e−6通过；删内脉冲恶化，已转保双脉冲设计。beta8 p05旧线性DN到q10 metric4.37e−8，q12一次Frenet拒绝非上界；32列端口空目录再生全部逐值一致。旧39源缺.cjs，恢复需完整71源；原PadTo配置需展开160才能得canonical hash。见ports与实际联合笔记。

旧q18完整H forcing仅λ=.0781：λ=.07同g M8/12/16 metric8.03e−9/2.24e−9/9.29e−10，但fullD1.96e−5/1.15e−5/8.23e−6、Xrr层差.00382/.00130；差分噪声仅4e−12。不是C²/无限尾收敛。旧高q前缀不能借小q新尾宣称接合。

**m3真实联合最新**：q02已原950f成功，δ=.06105607686781097。固定同g M8径向/角图分段点入网后prefix metric2.747e−8→4.971e−9、全tensor2.975e−4→9.015e−6，tail仍M8 fullD2.345e−6/minA.442/K8.04；完整高度二jet缝≤6.17e−12，设计态512角Cartesian二jet≤8.61e−9。原prefix最大缺陷跨角样条断点，后仍有bridge插值缺口。采样D约2.291仅数值包围，幅度不足。M16原shoot校正Riccati条件1.28e11，line search失败res6.87e−7未过2e−9门；转M12/独立全shooting校正。q04/q06仅线性DN prefix（q06 secant成功metric1.144e−7/K9.411），不可冒称真联合。入口m3-smallcut-true-coupling-and-secant-prefix笔记及m3_coupled_seed_deliverable/m3_secant_deliverable，70源空目录/实际导出链已验。

主会话新n4精确圆弧+中央直柱：R19已证明偶数中心对称整像dH≥中心位移、固定二fold帽简单谱排除全部全等；有理核心R=.325/c>.72061，α=39/250、ℓ=.7给shift>.34258。若完整D≤3.4、σ≥.11、K≤9.5，则held/D>.10075、reach/D≥10/323、Hdiam/D≥7/34，全部闭族前提未付。普通n4 M4圆弧同伦λ1虽有限求解通过，但metric.00407/全D3.801；不作可行候选，正设计更充分的负K区。

## C. 接缝、A图与混合边值

R12：h=g−dz²正定时同g一jet和完整z二jet经一次固定平面刚体确定整圈Cartesian二jet；给误差链，采样不当连续证书。R14：同turning number/同严格Q符号支内，闭合总转角已决定mean zr，Darboux再定zrr；Q过零不适用。

R15：轴向精确界|A|≥|w_r|√D/(E^1.5 Kmax)；反射/D>0且从背景连通的振幅支在非平谷轴上不能A变号，非用户相位族普遍限制。旧λ.0781轴若精确仅需κr≈.3906，尚未超预算，Gauss缺陷1.388e−5才是问题。R10有低K精确锥环带A变号，但匹配需Hr=H/r、Hrr0、均值/共顶点，不可免费贴入。

R16有限detG≠0可用不定Gram图；过零权的精确Galerkin无L²一致逆。15个精确锥LU测试通过，径向四阶，不证明跨奇点/模式收敛。R18完整µ-free混合DAE不逐点求G逆，含cos/sin/均值/原alias；12原engine对照≤3.34e−15，6精确锥通过，但M32全局Jac可1.5e14。真实首cell h=rwv/p=w²t连续变量变换与六行终态已发表：uniform16状态差从v坐标.006717降至5e−5，但物理H插值metric3.68e−4/张量.922/rr跳18.8，未C²。v插值K甚至4.24e4/8.01e4；全部失败保留。40源空目录真实组装18stage已验，入口actual-cell-mixed-coordinates-and-bad-interpolation笔记及mixed_dae/actual_cell；精确背景+全Cartesian共享二jet五次图已定义C²，uniform16→32 metric3.019e−7→1.078e−7、K≈8.040，但tensor .004547→.008295反增；critical入网的已有cusp16得.002737，仍有径向缺口。完整记录见actual-cell-shared-cartesian-c2笔记及actual_cell/cartesian_c2；不称C²误差收敛。

R17给无轴反射二fold核h=1+qcos2φ+εsin4φ；q.2/ε.005时ρ≥.325、Re AC>.5456625，精确卷积已核。但需要全cos/sin+均值BVP，非免费自由度，旧象限证书不移用。

## D. 其他结果和来源

R1椭圆10.3%局部条件窗；R2全Gauss–Codazzi/平领2jet；R3/R4精确圆弧换握持/10.8%局部窗；R5条件于精确C³前缀的退化入口圆弧保持；R6/R7三fold/二fold固定帽排除全部O(3)全等；R8正K完整带内圆弧必k1但K0入口缺；R9新C³负K轮廓保护窗损耗>.92、背景K55/8，未解全非圆BVP。

圆弧旧profile/新loop有限BVP未获所需metric；小cut nc31/M12短领最佳4.3246e−4/K10.022，半帽/Gauss–Codazzi亦未过。完整失败和源见notes/scripts；无终态中断不记数学失败。来源R114/flat17仅held/D>.0527832、reach/D>.0312033；R115椭圆core条件、旧.063均未解决本题。自己的workflow held10-smallcut-research.yml（题外）8组已逐日志核查，不保存可重算artifact。

## 当前接手分工

literature_mechanisms：m3前缀设计/真实幅度；new_construction：m3真实尾与DN联合；true_a_analysis：实际cell混合DAE/Cartesian C²表示。主会话：n4圆弧新构造、证明/连续几何、规则同步与逐结论push。open.md列全部缺口；完成前持续研究，不停在阶段报告。
