# HANDOFF — visible-flex-held-10pct

维护会话：**Astra-held10-f00f08c9-20261117**（AI）。开始：2026-11-17 19:55（UTC+8）。状态：**进行中，尚无满足全部完成标准的候选**。

## 目标、规则与同步

连通闭曲面的连续C²等距嵌入族，固定有内点闭H，diam F₀(H)≥.2D；整像δ_hold≥.1D，含反射取商δ_E>0，全时reach≥.03D。同一固定g/物理参数/时间范围下最大相对度量误差≤1e−6且加密下降。材料位移不是整像变化，solver success不是完成。

- 已部分克隆、真实pull main并全文读根README（含授权）及题README；仅本题及自己的workflow稀疏检出。
- 已读规则提交：`36c306c3a5ced5b86eed41c88532ad522e15ac5c`。2026-11-17 23:18:51（UTC+8），真实 pull/rebase 后双 README 差异为空。下次真实 pull 最迟 00:18:51；每次 pull 后比较这两份 README，只读变化并立即执行。
- 每条结论同步本文件并普通push；非快进立即pull --rebase再推，禁止force。每次pull比较双README，只读差异；至少每小时一次。令牌只在命令行临时使用。
- 完整证明进results；数值/条件/缺口分开。可重算数组、网格、CI artifact不入Git/Release，只存源码、参数、hash。本文件<10KB、单Markdown<100KB；不写根LOG。

## A. 高振幅小cut前缀和连续几何

主参数r=.30、w=.08、w_r=−1.8666666667，vu=.55、vd=.60、flat ramp=.4、eta=.05、cycles1、ShortBridge κ4/p=.2。割线仅改初值，原方程不改。

旧尾线性DN的固定g加密：q14 M14→16 metric1.16e−7→1.16822e−9；q18 M16→20 9.98e−7→2.42874e−8；q20 M20→24 9.92e−7→4.17253e−9，actualq=.20000109659082244、κ采样6.62074、高1.27654148、Frenet根≥.0005641758。q22同g M28→M32已完成：metric1.13275e−6→1.11885e−8、actualq=.2200009075、κ采样7.18978、根.000422747，1675节点。直接有理Fourier卷积证明该有限core ρ>.2449985、Re A_C>.5809146，不误用R7的q≤.21统一界（q22-fixed-metric-refinement笔记）。它们均未闭合。

复现：scripts/recover_prefix.py与prefix_recovery_manifest.json恢复源；smallcut_prefix_sweep.py建chart，smallcut_secant_launcher.py延拓，fixed_refine_smallcut.py冻结g加密，smallcut_endpoint.py导出完整均值/非均值两jet。命令/hash在smallcut_delivery_manifest.json；全部数组仅scratch。详见smallcut-high-q-and-fixed-g笔记。

全Cartesian有限Fourier/共享二jet五次Hermite表示和s≤.04的解析core lift，已精确支付中心上下接缝C²。同一物理g M20→M24 metric9.9307654e−7→4.1719950e−9（238倍）。新全域区间检查含中心已覆盖843264盒、无失败：σ>.349674、半径<1.508969、witness>.3254827、8I±II严格正，另有XY径向投影及角Jac正。R11完整证明及两份独立审读已发表，并由P/J正与支撑正证明上下全prefix为嵌入环带；这仍是开放前缀的有限表示，未证明精确等距或闭族。源码/定义及旧四次审计见cartesian-tensor-prefix笔记。

先前浮点mesh-cover给D≤3.030641、witness≥.318244；R11已用连续证书替代该前缀几何估计（D<3.018、witness>.325）。若实际尾rXY≤.35、顶高≤1.526542，尚容许增高.25。R7的二重固定帽/短柱给含反射δ_E>0；R13已将R11的W>.325与尾窗口合并：若真实尾全域κ≤10、σ≥.3、rXY≤.35、顶高≤1.5265414843并全接合，则可得held/D>.10338、reach/D>.03191、Hdiam/D>.76。明确条件定理，尾尚未构造。

## B. 实际非线性DN与闭合缺口

原尾真实延拓仅到完整q18端口λ=.0781。相同原g在λ=.07、M8/12/16的metric8.03e−9/2.24e−9/9.29e−10，但Darboux1.96e−5/1.15e−5/8.23e−6，Xrr层差.00382/.00130，差分噪声仅4e−12。不能由小metric宣称C²/无限尾完成。详见nonlinear-tail-stage1及common-twojets笔记和scripts/nonlinear_tail。

**实际非线性DN联立已接通**：scripts/coupling保留原TailMixin/真实outer及全部门；upper输入−H并反射整个尾z/mean。beta8 q=.0002/.0004已过原门，metric2.37e−11/2.42e−10；q=.0006内层rms1.99e−6触maxnodes，尾仍接受，非容量界。源hash/恢复见actual-prefix-tail-coupling笔记。

widecut r=.35/w=.30保留原拓扑，438次真实物理优化后canonical D1=9.86804231267902。实际联立固定δ点q=.001013386和新design q=.002通过，prefix metric1.055e−10/2.390e−9、尾minA .6757/.3280；q002尾Gauss/fullD增至2.214e−6，不能凭小metric称C²收敛。72文件恢复器独立再生端口逐字同hash；冷启动失败、弱增益校准及另一402次峰谷设计均完整登记在widecut笔记。不同prefix δ不混为同g。

R12已严格证明：接口水平Gram h=g−dz⊗dz正定时，相同g一jet与z二jet经一次固定平面刚体配准决定整圈Cartesian二jet；含反射/同向约定及显式有限误差链。数值应用仍需连续误差界、共同C²表示，不新增独立Cartesian方程。

R14进一步证明：同g接口、同turning number和同一严格Q符号支内，完整z迹与非均值zr已由闭合总转角唯一确定mean zr，再由非特征Darboux确定zrr；给连续误差条件数。仅局部精确定理，接口Q过零时不适用，所有数值均值/holonomy仍须记录。

新DN必须重配完整H向量，不能复用旧线性根；beta8与widecut的线性prefix结果另记，不能替代实际尾。前三cell高谷块（峰.85、谷.04、n≥3不变）背景高.060955、κ采样9.88977，真联立仅q=2e−6通过；旧H forcing到λ1e−5，删除内侧脉冲使minA转移深cell3且容量恶化。冻结源及结果见three-cell-block笔记；现恢复各圈双脉冲，同时控制Q=0与gain。各为不同物理g，严禁混称同g。

R10严格构造同g C∞低曲率锥环带：0<w≤.01、a≤.01、r≥.2时κ<.77且D/S>0，指定幅度A变号；所以点wise A>0只是现有图限制。它仍需Hr=H/r、共顶点及全两jet，未连接prefix/深尾。有限Gram扩张也不证明无限谱通过A零点。

R15给精确轴向必要界 |A|≥|w_r|√D/(E^(3/2)κmax)：保反射、D>0、从旋转背景相连的同g振幅支在非平谷轴上不能A变号。不是用户相位族的普遍限制。旧λ.0781点若精确同g仅需|κr|≈.3906<10，实际缺的是Gauss相容（缺陷1.388e−5）；该点未被曲率预算排除。常w锥匹配必须完整Hr=H/r、Hrr=0与同顶点；不能直接贴入旧DN。

R16已证明有限detG≠0即有完整动量图（不需SPD），但固定过零权的精确Galerkin最小奇异值趋0，无L²一致逆界。独立LU实验用R10精确锥15组均通过，a=.0088时A≈−4.204、G负特征3/6/12；固定M径向64→128误差约16倍下降。明确不是振幅穿奇点或模式收敛，原正A源不动。R18已给不逐点除G的完整µ-free混合DAE等价式与全cos/sin边值源码；12组原方程对照逐项误差≤3.34e−15（主会话独立重复），6锥通过原严格根/ODE门，但M32未缩放全局Jac条件数可达1.5e14，无模式收敛。现转真实非恒定cell与全二jet。

R17严格给h=1+q cos2φ+ε sin4φ的无反射二重核心，3|q|+15|ε|<1保证凸；q=.2、ε=.005有ρ≥.325、Re A_C>.5456625，四次复Fourier卷积独立核验。R7非全等矩仍适用。但无反射core不是免费BVP自由度；需完整cos/sin+零模及额外相容条件，旧单象限几何证书也需重算。

## C. 其他支线和来源

R3/R4给精确圆弧刚体换握持及四组局部10.8%条件窗；R5只对精确C³前缀证明退化入口圆弧保持。R6/R7为3fold/2fold标记非全等定理。R8依据Ghomi–Spruck原文证明完整正K带内的圆弧必k=1，但K=0入口仍缺；R9保留s≤.42的C³新g严格损耗窗>.92、背景κ≤55/8，未解实际非圆BVP。

新loop λ0同g M4→6 metric1.776e−9→6.393e−10；λ.3仍3.93e−4，λ.5控制饱和。旧圆弧λ1/M4 metric≈.00805，有限Schur病态不能证明无限解。半帽/Gauss–Codazzi/有界E短领均未达metric；正确G-floor的小cut nc31/M12最好4.32458e−4、κ10.0221。完整失败与源码在对应notes/scripts；无终态的执行中断不作数学失败。

来源R114/flat17 held/D>.0527832、reach/D>.0312033、metric≤1.2567e−9只作来源；R115只是椭圆core条件构造，不含已解尾；旧.063也是未解暖场。自己的workflow `.github/workflows/held10-smallcut-research.yml`（题外文件）8组Actions已逐日志核验，不保存可再生artifact。

## 当前接手入口

三个代理分别推进高q/新DN前缀、前三cell实际非线性尾、原接受门的真DN联立。主会话负责规则同步、证明审读、连续Cartesian几何和逐结论push。全部缺口见open.md；现在优先增大真实联立幅度、支付全Cartesian接缝与无限深尾，达到10%完成标准后继续提高比例。
