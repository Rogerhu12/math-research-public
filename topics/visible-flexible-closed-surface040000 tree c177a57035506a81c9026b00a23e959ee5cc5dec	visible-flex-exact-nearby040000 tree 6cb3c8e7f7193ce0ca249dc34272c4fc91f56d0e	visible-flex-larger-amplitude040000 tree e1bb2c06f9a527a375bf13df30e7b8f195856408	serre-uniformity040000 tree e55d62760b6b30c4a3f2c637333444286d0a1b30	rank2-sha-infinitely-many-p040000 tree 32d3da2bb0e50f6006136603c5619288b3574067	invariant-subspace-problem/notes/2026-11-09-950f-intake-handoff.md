# 交接：可见且有厚度的闭曲面等距弯曲

会话：Astra-visible-flex-4ffd372b；2026-11-09接手，QUEUE提交7acd82077457a23caed9e982cc547c5087da6d2d。**尚无合格闭曲面，状态进行中；中间结果不作收尾。** 原已审结论保留，较早详情归档notes/2026-11-09-handoff-before-deep-curvature-correction.md。

## 完成标准与纪律

已读根README及本题2026-11-09 README（blob099f451b142e184c223d2d0764887d99bd492db5）。同一连通紧无边M、连续C²嵌入族F_t；固定闭握持H有内点且diam F0(H)≥.2D；不配准δ_hold≥.05D，严格/带误差δ_E>0；全时reach≥.03D；同一g相对metric误差≤1e−6。冻结物理metric、参数、时间范围后，加密必须趋机器/求解精度，不能有固定taper误差底。完整成果须未参与者独立重跑后才输出少量<5MB网格。更强目标δ_hold≥.2D、δ_E≥.05D、严格存在仍保留。

只写本题、自己QUEUE行、根LOG追加。HANDOFF<10KB。原HTTPS git无认证，使用已连接GitHub API，最新main父节点、expected_sha租约、force:false；他人并发提交必须保留。不要改旧工作区或邻题源码。

## 当前优先事项

- 原N80全尾在raw cell80有κ≈342.8467，已失格；保留失败。N160为新metric，R8支付默认未改深源，浅warp与非轴对称误差另付。
- 主线改用三重切向角核心（R7）+Frenet prefix+真实物理尾。b=.22严格支持差≥.16400175；先求实际大幅度prefix，再冻结metric加密。纯入口的快谱尾不能替代被匹配条件修正后的实际核心/前缀谱尾。
- closing优化浅谷和非对称pulse，提高真实m3端口可用幅度；当前最优仍未付正性/曲率。root做真实非线性tail延拓，fixed_metric_bvp做prefix，independent_audit继续独立核查。不是闭族完成。
- old角梯度诊断已纠正：|mf|<rw仅为归一化P小量条件，角投影条件是|mf|<r；旧wCut=.01幅度障碍撤回，线性T门/DN不变。

## 已审几何工具（均不代替完整构造）

- R1：旧wide-m2整个带的像仅整体转动，配准后窄帽给δ_E/D<2.7325581396e−5；同模板(δ_E/D)(reach/D)≤1/3200。只限δ_E强目标，不否定新版δ_hold基础目标。
- R2：双模块条件直径、内部滚动球必要条件；排除旧.98组合，.96/.97未排除，无真实模块。
- R3：S=−S时D=2max|x|；反射半转prefix可用球包络。隔离中央柱给δ_hold≥min(R−r,ell)；两不连通固定帽可组成H。独审PASS。
- R4：reach(S)≥ρ，环境位移||Du||≤η<1、||D²u||≤L，给reach≥(1−η)²ρ/(1+η+Lρ)。轴对称未标记帽+转动带使基准整像全等；四个不同C² Hölder正则性且仿射独立的固定标记排除全部E(3)，紧性给δ_E>0。需先有完整基准reach。独审PASS。
- **R5新增**：平面切向锥宽<π/2、|κ|≤K时，所有点对|q−p|²≥2|(q−p)·n_p|/K；同号有界斜率旋转图得内部点对界min(1/K,inf r√(1+w²)/|w|)。完整证明及独审PASS；K6且适当r,w时尾块可达1/6。只控制块内点对，不给有边块reach或整个闭面的跨块reach。见results/R5-sharp-monotone-normal-chord.md。

## 核心与尾部的已知数值状态

旧ellipse/synthetic-Robin结果全部保留，只是中间数值：M4→8→12曾降低metric到3.59e−8，但delta改变，非固定metric加密；旧端口没有真实tail。M8/aspect1.3球包络采样4.46855，实际末rho=.6008466>.6；支持差采样不是严格下界。详centred-diameter-correction、root_phase_envelope及前版H归档。

默认cut-preserving raw源rCut=.6,wCut=.5,width=.35,δ0=.006,a2.75,R64，浅prefixR2。修改cell0倒数第二transition恢复cut，末port raw，w_r=−5.83333333。旧N80有限背景height.0216288、warpα71.928617；完整背景已因raw80失格，保留失败。N160是新metric。R8只支付默认未改深源n≥160，有限warp仍需连续界。

独审momentum确认N160 mode3 DN=10.5437607712063，m6/9/12=25.5495153497543/40.1256324437583/54.3144838634213，线性T门4.06073396104e−5，far32/48/64一致。物理(f,f_r)的far48 logGain634.97对比动量655.91有严重深部相消，禁止引用前者为准确放大因子。

旧N80真实非线性tail局部诊断：depth8、height1e−6，M8径向64→128完整Darboux约2.96944e−8不降；不能用shooting约1e−10代替完整残差。M4→M8同时修复实际cusp点x=.95982478947，不能纯归因角向加密。28项输入/原始states已推送，fixed_metric_artifact_manifest.json。

非线性接口必须保mean：旧M12平均z_s修正1.5983e−4；反向段输入DN(sigma*H)，sign在非线性函数内部。R6已审：相同metric与完整高度二阶jet决定非退化连通切口Cartesian二阶jet；近似时须C1 metric缺陷或直接Cartesian二阶检查，C0 metric≤1e−6不够。

新m3 support核心prefix在真实线性port下M4/q=.001,.003,.01收敛。q=.01时metric2.15e−7、完整Darboux1.699e−5、cutheight1.597e−4；delta各改，非固定metric加密。冻结delta后重布点消除近重复mesh二阶尖峰，但归一化bc的舍入地板导致solver_success=false；保留physical残差约1e−17的诊断。旧support核心q=.08仍需约M48入口，现改用已审R7的tangent-angle核心；q_eff=.08时M8入口metric约1.2e−14，κ∈[.36,1.64]，正在解新族prefix。

当前首短prefix vu=.25,vd=.4,ramp=.4,cycles1，线性delta=.0725268280，H1.16799，K5.30988，gain.01597046。q_eff=.08/ell=.16的一阶球包络D≈3.0282，只是预算；提示可试tail K8–9。R7推荐b=.22、ell=.164，严格支持差≥.16400175，最终需实际D≤3.28。

closing的六谷+非对称首pulse：K9/pulseCap0=.4、β0…5=[3.125,2.8125,4.0625,5,5.25,4.0625]，T门6.85e−4、DN11.5413、tail高.04036；指定height.001时形式κ≈13.19、线性A<0，失败。K8/cap.2门5.49e−4，形式κ≈12.16，也失败。首cap .6/.8/1/1.2分别重优化，未见合格实例。root已适配真实split-flux非线性worker，K9/cap.4的初始线性网格1024触Node384MB内存上限，属资源失败；在同物理metric下改线性预处理256/far32、heap512MB重试，保留两套输入，尚待结果。

已失败的线性筛选：m2二十速度/周期组合、m3九外向和六内向组合均未提供当前tail门+几何预算的可用组合。m3七种wCut/cap全局扫描不如wCut.5基线；δ0六点扫描以.02门7.17e−5最好，仍不足。全M10=0校准落压缩支；纯删除外valley损失放大。这些都是有限探索，不是一般不存在性。

无限tail适用性：独审确认3fold全Darboux/holonomy=1可作三个扇区严格平移消去，phase封帽机制不限偶频。但现有R20正式定理是偶频/literalδ0=.08，不能直接覆盖3Z/默认.006。其充分深条件在n160明确不满足（M160约1.08e8 vsδ160^−1/16<1536）；即使推广也须另外支付深起点到cut的有限传播。背景R8≠非线性tail存在定理。数值仍需同metric全频/深度/径向加密和实际Cartesian审计。

## 分工、来源和接手动作

fixed_metric_bvp：真实非线性DN、固定metric、mode3 prefix。closing_geometry：N160浅cell真实校准、幅度门、封口与全局reach。independent_audit：未参与构造，独审证明与独立数值复算。root：全题推进、H/open/results索引、推送。当前均继续研究。root新增 optimized-tail worker，正对K9/cap.4做真实m3非线性幅度延拓；不会把线性门当非线性不存在性。

可只读依赖：/workspace/scratch/effcccee615b/math-research内旧ellipse文件；/workspace/scratch/f6f33987b45e/math-research内large-amplitude脚本。closing_tail_sources.mjs核9项Git blob；root原构造来源SHA256 c2a282deb622141cb05554a4a0910dd0a9a57cd7948ecab02917ae5c13d40bf5。本题脚本支持source-root环境/参数，不修改邻题。

文献范围：Ghomi2019 Problem1.1、Payne2023 cylinder摘要未给本题定量闭嵌入族；2025 compact Bonnet pair是两个浸入而非连续闭嵌入族。不能由检索无结果宣称全球不存在。出处见resumption-and-literature。邻题R520非定量存在不能付本题数值比例；旧wide-m2尾κ约95，仍不合格。旧direct-coordinate/sphere失败输入与独审均保留，不重复盲加阶。

下一步必须实际得到冻结metric的完整prefix+非线性无限tail+圆领+两帽；核C²缝/全时嵌入、握持尺寸与距离、δ_E>0、全局reach所有跨块点对；固定几何加密经独立重跑后才可满足README。不以环带、失败证明、小振幅存在或局部加密收尾。
