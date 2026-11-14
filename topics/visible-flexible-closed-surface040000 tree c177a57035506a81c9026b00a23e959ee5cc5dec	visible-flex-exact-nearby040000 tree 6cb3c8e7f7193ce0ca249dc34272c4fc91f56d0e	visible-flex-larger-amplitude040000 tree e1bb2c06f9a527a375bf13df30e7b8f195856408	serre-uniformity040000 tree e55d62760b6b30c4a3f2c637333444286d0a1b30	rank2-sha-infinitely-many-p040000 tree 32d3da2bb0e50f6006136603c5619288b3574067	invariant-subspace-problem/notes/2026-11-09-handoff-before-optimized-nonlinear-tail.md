# 交接：可见且有厚度的闭曲面等距弯曲

会话：Astra-visible-flex-4ffd372b；2026-11-09接手，QUEUE提交7acd82077457a23caed9e982cc547c5087da6d2d。**尚无合格闭曲面，状态进行中；中间结果不作收尾。** 原已审结论保留，较早详情归档notes/2026-11-09-handoff-before-deep-curvature-correction.md。

## 完成标准与纪律

已读根README及本题2026-11-09 README（blob099f451b142e184c223d2d0764887d99bd492db5）。同一连通紧无边M、连续C²嵌入族F_t；固定闭握持H有内点且diam F0(H)≥.2D；不配准δ_hold≥.05D，严格/带误差δ_E>0；全时reach≥.03D；同一g相对metric误差≤1e−6。冻结物理metric、参数、时间范围后，加密必须趋机器/求解精度，不能有固定taper误差底。完整成果须未参与者独立重跑后才输出少量<5MB网格。更强目标δ_hold≥.2D、δ_E≥.05D、严格存在仍保留。

只写本题、自己QUEUE行、根LOG追加。HANDOFF<10KB。原HTTPS git无认证，使用已连接GitHub API，最新main父节点、expected_sha租约、force:false；他人并发提交必须保留。不要改旧工作区或邻题源码。

## 最新优先事项（04:00更新）

1. **N80原新尾完整曲率失败。** root_cut_preserving_tail的有限80层采样κ<6不涵盖其后raw无限尾。独审在未经warp的cell80首transition找到κ≈342.8467339（x≈.89571），这一段不含未知校准参数；cell96≈22.735，cell112≈1.495。详audit-cut-tail-deep-curvature.json及独审脚本。N80必须保留为失败物理输入，不能作为全尾低曲率候选。新protectCell=160是不同metric，须重新算真实DN，不可算作旧几何加密。R8现已独审：借已审R28的exact根括号及本题有理常数，默认所有n≥160母线κ<.02且C²接平帽；有限warp/非轴对称扰动另付。
2. **浅层幅度仍太小。** 原N80/cap=.02线性DN m2≈5.676917017；独立优化的Hθθ线性正性门≈4.1077308e−6。真实DN重配后aspect1.02的M4 prefix末height≈3.50682e−4，仍超门约85倍。这个线性门/有限Newton失败不是非线性不可能性定理。全M10=0校准反落压缩支，失败保留；直接m3浅谷优化及非对称首pulse已把线性门升至6.85e−4（K9/cap.4）；在幅度.001形式κ≈13.19且线性A<0，仍不合格。纯删除外valley损失放大也失败。正在保留谷、非对称增强首pulse。closing旧角梯度附加门已纠正：|m f|<r w仅为P的小量条件，真正角投影需|m f|<r；旧wCut=.01幅度障碍撤回，T门与DN不受影响。
3. root开始三重核心并行改进：新φ(θ)=θ+b sin3θ的单位切向角核心严格单位速/闭合，b=.22支持差≥.16400175，M8入口有快速阶乘尾；完整证明已独审为R7，可望免去support核心M48成本。旧三重对称核心：support h(φ)=1+q cos3φ，弧长θ=φ−(8q/3)sin3φ，q<1/8；候选q≈.1给旋转π/3支持差2q。研究mode3能否增强衰减且缩短prefix；m3真实线性端口的非线性prefix已在M4/q=.001,.003,.01收敛，q=.01 metric2.15e−7但完整Darboux1.70e−5，仍须加密；设计时delta改变，非固定metric证据。固定metric M4重布点已去掉近重复节点尖峰，但bc的归一化舍入地板导致solver_success=false，完整Darboux仍1.699e−5，失败保留。首个m3线性根vu=.25/vd=.4/delta=.0725268280，高度1.16799，背景K5.30988，q=.1端口约.001597（当前门39倍）。新N160真实线性m3 DN≈10.5437607641，线性T采样门≈4.060735e−5（cell0），m6/9/12端口已算；仍须独立复核及非线性耦合。它不中心对称，不能直接用R3的直径等式。fixed_metric_bvp负责通用mode3入口/非线性prefix；root负责N160真实线性port及预算。

## 已审几何工具（均不代替完整构造）

- R1：旧wide-m2整个带的像仅整体转动，配准后窄帽给δ_E/D<2.7325581396e−5；同模板(δ_E/D)(reach/D)≤1/3200。只限δ_E强目标，不否定新版δ_hold基础目标。
- R2：双模块条件直径、内部滚动球必要条件；排除旧.98组合，.96/.97未排除，无真实模块。
- R3：S=−S时D=2max|x|；反射半转prefix可用球包络。隔离中央柱给δ_hold≥min(R−r,ell)；两不连通固定帽可组成H。独审PASS。
- R4：reach(S)≥ρ，环境位移||Du||≤η<1、||D²u||≤L，给reach≥(1−η)²ρ/(1+η+Lρ)。轴对称未标记帽+转动带使基准整像全等；四个不同C² Hölder正则性且仿射独立的固定标记排除全部E(3)，紧性给δ_E>0。需先有完整基准reach。独审PASS。
- **R5新增**：平面切向锥宽<π/2、|κ|≤K时，所有点对|q−p|²≥2|(q−p)·n_p|/K；同号有界斜率旋转图得内部点对界min(1/K,inf r√(1+w²)/|w|)。完整证明及独审PASS；K6且适当r,w时尾块可达1/6。只控制块内点对，不给有边块reach或整个闭面的跨块reach。见results/R5-sharp-monotone-normal-chord.md。

## 核心与尾部的已知数值状态

旧椭圆路线：同周长planar ellipse柱+上下反射Frenet prefix+真实衰减尾+两固定平帽。相位F_phi=R_phi F(s,θ−phi)保旋转材料metric，实际开圆领内逐点固定。非线性流F_s=αN+√(1−α²)B、α=−a'/(aκ)给精确ds²+a²dθ²机制。

旧profile vu=.35,vd=.5,ramp=.4,cycles1,rCut=.6,wCut=.5。原DN是错误尺度迁移的合成Robin，不能当真实封尾。aspect1.2的M4→8→12完整metric约2.25e−4→2.88e−6→3.59e−8，但每次delta改变，**不是固定metric加密**。固定a(s)wrapper改extrinsic aspect为未知，低阶restart曾maxnodes失败，非不存在证明。

旧M8/aspect1.3/ell=.26的球包络采样D≈4.46855（粗圆柱4.95283），prefix最高z≈2.14170。末实际半径.6008466>.6，已纠正rho=.6封尾假设：须至少rho≤.601，若目标D≤5.2，则尾顶z≤√(2.6²−.601²)。支持差采样.260991只是差值的上估计，未证≥.26。root_phase_envelope.py与独立rerun保留，全部为条件预算。m3首短根的一阶球包络：q=.08/ell=.16时D≈3.0282，提示可试K8–9和较大浅cap，但非真实非线性界。

root cut-preserving构造在cell0倒数第二transition恢复raw，最后port不改；保真实cut slope/second且重算warp。rCut=.6,wCut=.5,width=.35,K6,cap=.02，N80有限部分高度.0216288，warpα71.9286170；cap=.05高.0291259；cap=.1宽度不足。上述N80全尾曲率已失败。独审实际积分/324点吻合，cut w_r=−5.83333333；独审momentum已确认m2及P160的m3切口DN/正性门；far32/48/64一致。但m3 far48物理RK logGain634.97而动量655.91，不能引用前者为准确深部放大或无限衰减。

实际非线性tail接口（N80仅局部诊断）：depth8延续到height1e−6，3e−6 Newton失败；M8/64与128步完整Darboux误差均约2.96944e−8，shooting残差约1e−10，minA≈.74431，基频斜率径向加倍差4.489e−14。M4完整方程误差5.50e−5，不能用小shooting残差替代。实际cut恢复transition引入x=.95982478947临界点，worker已加actualCuspGrid；M4→M8同时修网格，不能纯归因角向加密。raw状态及参数保存，28项清单fixed_metric_artifact_manifest.json。

非线性接口必须含均值：旧M12平均z_s比圆对称值多1.5983e−4；反向段须DN(sigma*H)，方向放在非线性函数内部。fixed_metric_actual_tail_bvp记录mean/nonmean一二阶jet。R6已独审PASS：非退化连通切口相同metric+完整高度二阶jet决定Cartesian二阶jet。近似应用还需C1 metric缺陷或直接Cartesian二阶检查，C0 metric≤1e−6不够。

root的wCut=.05/.1/.2/.3与cap=.02/.05七组m3扫描均不如wCut=.5基线；δ0六点扫描以.02最好（线性门7.17e−5、q=.1端口/门22.34），仍不足；更大δ0非单调变差，无全参数排除。root_trueport_prefix_scan：20种vu/vd、cycles1/2/3/4/6的真实m2线性DN筛选完成。更短prefix的根曲率陡增；强衰减根过高，未见满足当前幅度门与几何预算组合者。不是全参数排除。closing几何的其他实际尾背景、条件buffer二次不等式及deep coarse bound见2026-11-09-closing-real-tail-progress.md与closing-radial-reach.md；buffer代数独审PASS，参数包围和深alpha_n统一界仍缺。

## 分工、来源和接手动作

fixed_metric_bvp：真实非线性DN、固定metric、mode3 prefix。closing_geometry：N160浅cell真实校准、幅度门、封口与全局reach。independent_audit：未参与构造，独审证明与独立数值复算。root：全题推进、H/open/results索引、推送。当前均继续研究。root新增 optimized-tail worker，正对K9/cap.4做真实m3非线性幅度延拓；不会把线性门当非线性不存在性。

可只读依赖：/workspace/scratch/effcccee615b/math-research内旧ellipse文件；/workspace/scratch/f6f33987b45e/math-research内large-amplitude脚本。closing_tail_sources.mjs核9项Git blob；root原构造来源SHA256 c2a282deb622141cb05554a4a0910dd0a9a57cd7948ecab02917ae5c13d40bf5。本题脚本支持source-root环境/参数，不修改邻题。

文献范围：Ghomi2019 Problem1.1、Payne2023 cylinder摘要未给本题定量闭嵌入族；2025 compact Bonnet pair是两个浸入而非连续闭嵌入族。不能由检索无结果宣称全球不存在。出处见resumption-and-literature。邻题R520非定量存在不能付本题数值比例；旧wide-m2尾κ约95，仍不合格。旧direct-coordinate/sphere失败输入与独审均保留，不重复盲加阶。

下一步必须实际得到冻结metric的完整prefix+非线性无限tail+圆领+两帽；核C²缝/全时嵌入、握持尺寸与距离、δ_E>0、全局reach所有跨块点对；固定几何加密经独立重跑后才可满足README。不以环带、失败证明、小振幅存在或局部加密收尾。
