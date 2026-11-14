# 交接：可见振幅数值解附近的精确等距解

会话 visible-exact-astra-f6a2，2026-11-12接手；**进行中，主目标未完成**。

## 完成标准与已读规矩

连通闭C²精确同度量嵌入族；固定有内点H、diam(H)≥.2D；held位移≥.05D；
含反射δ_E>0；全时reach≥.03D。有限模、线性、条件式、浮点或障碍均不算完成。
最近已读规矩提交：aec966622b5050b7dfb7c8fdaf7e6b56f8db734b（根README、本题README）。
每次pull只读两README差异并立即应用，至少每小时pull。根授权/规矩1–13、本题README、
原HANDOFF/open/log及8篇旧Markdown notes已完整读过。用户明确授权读其它文件夹；
只读外题，未改外题。提交前pull，保留并发更新，不强推。并行者不执行git。
上一批已推17bb9986cb67026e23e5b972d56ada923feeb239；本批R48–51及严格root/参数包已登记。

## 当前立即续做

1. **主输入type_fixed_step02，不是旧canonical**。32角插值rotation差2.55e−4，
   补16最差中点后48角约.551349/.551342，差6.74e−6，仍为普通浮点。
   同图mean列和有限probe η=(.002soft,.0002middle,0hard)返回差样本全正。
   D5目标(15121+√5)/27422、D8目标(4852+√8)/8804正接入实际几何及R31/R51共轭。
   二进制knots有微小反射缺陷，既有±同根返回未支付；显式对称对象须另定义。
2. R45–47已付完整正cap source/contact、strict负区Cauchy/WKB、有限Ai物理源。
   全反馈β=(2π)^−1 FP∫F/µ，物理距离减项及PT校准已证；实际候选β区间仍欠。
   必须固定R37同一个ℓ/χ/零阶项。R34算术、R40正常形不能免费供应网络输入。
3. 显式sym step02的无限角target已认证根t∈[.2383698,.2383701]，C'>300.5184、
   K0'>60.1022；共同span(.2375,.23969803864366687)内，|x−t|≤1/4096的实collar
   有45<K0/(x−t)<75。根部局部解析可供有限jet，不能当复strip；Gaussian为备选。
4. constructive做新D5错位射线/连续N门；numerical付原step02的Fz/r、area、ζ连续门；
   audit做β稳定root Taylor。R48–51均完成，当前没有实际β区间或全频强逆。
   后续付全频逆、有限低块/核规范、普通源、真平帽、相对Killing匹配及R37残差因子
   Newton/loss，再付同一精确族固定H、可见性、δ_E、reach。不得停在上述中间结果。

## 永久候选、恢复及失败

下列均是有限体普通浮点样本，无闭帽/连续几何证书。当前主输入
`data/phase_ring_continuation/type_fixed_step02.npz`，96601B，SHA256
`05d3e59cf338c5d2a2bde13aad7bf1d4e5247c326efb46b3148793e75a7ea883`。
M24/n201 graded/Gauss3/Q256quarter；必须保留保存的radius_shift。
β4(0)=.20747484022400084，实际U4(0)=.059612958013，不可混规范；
alpha=(.7396093769906578,−.005100267374734773,−.049352132159964625)。
metric最大7.84528322e−5、core N最大−.411846、外区[.3,3]K最小+.0293380、
环区[.3,.6]K最小+.0635238；D代理2.55249442、腰差.131455962、比.0515009792，
主曲率最大7.58466、支撑最小.901671。粗扫描root.238475与后续.238369915731
是同一根的不同精度诊断。当前不能叫连续单核心证书。

原类型约束predictor `data/fourfold_phase_m24n201_type_constrained_predictor.npz` SHA
`bf8430db367ae5d328c953dc2ba631288f75f778ea720756811a72f01c1f2449`。
固定mean0/2，仅mean1及非均值两步Newton，metric .000590342→.000131532→.0000784528。
step00/01/02、逐步JSON与type_fixed_run.json均已推。完整重做/续算命令、依赖SHA和
消元核查见 `notes/2026-11-12-constrained-mean-continuation.md`；入口
`scripts/fourfold_phase_constrained_multi.py`，固定0/2、regularization1e−5、core-N-upper0、
outer-floor0。当前先付返回兼容，不盲目重复或升M。多固定源60ad13a4、单固定3956b88e。

同图Schur `data/phase_ring_continuation/type_fixed_step02_schur_directions.npz`，306760B，SHA
`941c19642b4e74cbe5d68c311629bbe66f05df16fca26692c541ed61d6f29629`。
此诊断主动放开mean0/2，β/radius_shift仍固定。Gram谱(7.58e−12,1.53486e−6,.01805565)，
主兼容row(−.05738,−.84564,−.53067)。软列核心去径向重参余量.8593，再去缩放λ≈−.09532
后.03336；δE/E最大.38017、δa/a最大.09903，不是固定g核。R37速度必须用
−M/N±√(−K0 G_actual)/|N|，不是G0；参数搜索同步g0(p)，选定p后才冻结目标metric。
Schur源d4fbd8be48679dcb6ab972b1d8ec9bb4d89f21314961d92dd03c7ef133228462；
历史数据源hash不改写，唯一识别修补是radius_shift_knots判断phase格式。

旧对象保留：
- canonical `data/fourfold_phase_m24n201_q256_checkpoint.npz` SHA
  63b5513befcf44ce907b047dbeb41a7e143431211d20e3cbb103a081cbef0a0e：metric3.65699e−5，
  三正根.235457/.427727/.456718及外负环K(.445)≈−.504，不是本批单核心。
- 只消外环predictor SHA0491c4a735e59e2631e8bc8646d4b6590ec699b74c4c4885dc981be6b7aedbaf：
  core N最大+.7493，明确失败。quarter1_step00/01/02末metric5.13954e−5但外环仍负−.365588。
  数据和重做入口都在constrained-mean笔记；不得与type_fixed两步混同。
- M32三步后exit137，SHA20081f6a7118ee8d5c266e20adf8bd75e1ede37c1ad65644eeb735439a8ed315，
  metric2.41417e−5，与canonical核心Fxx/Fxθ/Fθθ差.623/.461/.862；复试仍exit137。
- 旧位置M24/151、M16/151、M16/101及入口/hash均保留在既有笔记。旧weighted M16
  degree1已含振幅，加载make_candidate(series,1.,order=1)，不能再乘.06；腰型别失败。

## 新冻结包与尚未推的恢复入口

32map、axisym校验、取消记录和旧canonical比较的全部SHA在
`notes/2026-11-12-principal-map32-frozen-manifest.json`、
`notes/2026-11-12-principal-comparison-frozen-manifest.json`，root逐项核对通过。
反射限制见 `notes/2026-11-12-principal-map-reflection-caveat.md`。
48角/参数/旧新H共轭与重做入口见 `notes/2026-11-12-step02-parameter-and-conjugacy-checkpoint.md`。
冻结manifest同日期前缀：R48-and-parameter（40项）、Hnode-correction（19项）、new-D5-Hnodes（2项）。
初D5 a042a48...真实64点误差.00683174推翻48插值；112实际节点局部校正后的
`type_fixed_step02_d5_jet_corrected_probe.npz`（同data目录）SHA
0dcfb37f84a1b3d6197b375aa8700628a00398c0b509ce5da6c92f1ecf489199，p=.4413514918092046，
metric样本7.9227e−5、腰比.05150175。新dyadic H在1/64带M0<3.222593,R0<4.698363；
新64真实节点误差3.40664e−6、导数误差.00343982、twist均值.00230682034，仍非Wiener界。
新错位网格是live，不得混入冻结manifest。

全[0,3]角尾/alias覆盖1396共同径向单元，六jet最大1.130e−10，实际三角/FFT舍入另付。
`data/phase_ring_continuation/type_fixed_step02_uniform_tail_inputs.npz` SHA
41d305d88844ff1548e1b1e45aebe423c134c366c7950de7c36eb8a05973fba9；
`notes/2026-11-12-uniform-phase-primitive-tail.md`有snapshot-only重做命令。
备选解析平滑输入`type_fixed_step02_analytic_smoothing_inputs.npz`（同data目录）SHA
bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532；
`notes/2026-11-12-analytic-radial-smoothing.md`付exact Z=∫slope、1944单元、反射/knots误差、
(4G_h−G_2h)/3定义。h=1e−5对称后最大C²差4.262e−6；未重解metric也未转移原返回数据。

strict root证书见 `notes/2026-11-12-symmetric-root-interval.md`，JSON SHA
 a40084d57e07db9c2b9162c76a094d7a7b087abddc740ed146f79f708342aa2f；完整snapshot重做，无ODE。
β旧探针已保全 `notes/2026-11-12-first-phase-probe-and-endpoint-failure.md`，原源
fourfold_phase_beta_probe.py不得混成新Taylor源。约36.8只是浮点，端点外推不稳，无区间。

## 已证结果和外题阅读

完整正文results/，索引results.md；均不是主目标完成。R1–24旧几何不能迁给当前图。
R25–29付有理背景径向谱/普通源、几何、Liouville及非径向GC/mean；径向逆不能
吸收二阶非径向主项，共轭共振不是PDE核。R30–34付真实参数circle Newton、完整
星形Darboux/全散射、单位T回缩、全β/j二次无理危险格；实际全网输入仍欠。
R35–38付真实正组件DN/source/Robin、移动root/shear、固定target型别及应变/握持泄漏、
twofold线性平尾。R39–44付有限光滑Airy/全源、scalar unitary有限正常形、直接log变角、
Dyson及首相位4/3强余项、有限W连续二型预算。角带与变角loss必须逐项计入。
R45付内部2/3增益、K=−H*、正负窗口/root和regular全部接触、真Airy Cayley。
R46付strict双曲Cauchy、精确frame/polar、WKB两阶强余项、完整β有限部及PT校准。
R48付准确整数多项式正导/逆导数及近邻D5/D8；R49付直接log权双向完整Cauchy/source；
R50付完整β分部降阶和真实root减项；R51付同宽Wiener复合及全部KAM迭代域门。
R47付有限Taylor/cutoff Ai全部lag/mean/物理源增益2/3和真实边界B∂/伴随，不假定正侧
椭圆Cauchy。实际有限jet、坐标下界、cap realization及全频强逆仍须逐项供应。

源continuous-flexibility-swarm/R520全文已读，仅充分小q，无本题可见下界。R492局部
核并独立改成R37；R499按使用读B0–9部分，root完整核B3–5，R47独立lag证明。
R513/517–519确切阅读范围、SHA及邻题visible-flexible-closed-surface README/HANDOFF
在source-transfer笔记；邻题仍未完成，其近似metric/几何界不授予本候选。
只取实际用的单文件，不递归取大库。其它数值入口：type-fixed-parameter-diagnostics、
phase24-core-type-predictor-and-c2-gates、phase24-type-network-and-compatible-removal笔记。
