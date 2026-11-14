# HANDOFF：大振幅新机制

**进行中，未完成；没有满足README全部标准的完整候选。不以阶段结果、运行预算或时长结束。** 会话 `Astra-new-mechanism-9974ea84`（2026-11-14）。root管Git/公开Actions/日志；mechanism管真实几何与联合driver；literature管完整高阶/外槽编译；repo_sources管C1闭路控制和科学输出。完整历史见[此前H](notes/handoff-before-full-phase-P1-20261114.md)、[open](open.md)、[结果索引](results.md)。

## 1. 授权、规则与环境

根/本题README已全文读。公开仓库最后已读规则提交：`1f4fd588dc7b58151424339779c8f6d99ed7d26e`。每次实际pull --rebase后立刻比两README；有变只读差异执行并记SHA。至少每小时pull。每个有意义结论即时commit/push；NFF立刻pull/rebase、核README、重推至成功，绝不force。私有19:20:16 UTC实际pull至`7943e238737119df3b4a564b854335f4b226debc`，双规则路径无差，本题私有README不存在；QUEUE唯一行本会话进行中；下一私有pull不晚于20:19 UTC。

真实几何、ODE/积分、优化与完整研究符号编译只用本公开仓库GitHub Actions。本地仅纸面代数、小人工开发、源码/公开输出解析；不伪造Actions环境。PAT仅瞬时CLI/env，绝不文件/提交/日志。根规则12：不把冻结、独立复核、逐字归档或重复清单设为推进前置；完整证明直接登记results并同步索引。

H<10KB，MD<100KB，open尽量<30KB；数据>1MB gzip、单件<5MB。只明确stage本会话文件，不git add .，不写根LOG。public `/tmp/visible-new-9974-public-restored-1845`，private `/tmp/visible-new-9974-private-restored-1848`；workspace同名稳定symlink接回。只终端git推送，不碰其他会话文件。操作helper为workspace `research_sync.py`，只amend自己尚未发布提交；--pull-only会留下H更新待下次commit。

## 2. 完成标准和不可变输入

闭连通材料面，每时刻C²嵌入且t∈[0,1]在C²拓扑连续，**同一固定g**；固定材料H有内点、diam F0(H)≥.2D；不作刚体对齐整像δhold≥.3D；全时全域reach≥.03D；最大相对metric≤1e−6，且同g/参数/时间范围精化继续下降。完整网格每件<5MB，报告严格存在差距；δE可0如实报。基本达标后继续.5D或严格存在。

当前核心A1、B7/25、半宽1/50；L.9、握持rc.22、入口tc.036、尾tf.846、六帽R.274。准确a0来自椭圆周长。固定g的5个body系数在原selected完整保存，不能替换成seed g。

- 永久原c0：`notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json`，987644B，SHA `6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3`。不得用当前selected重定义参考。
- 原167维selected：`notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json`，425422B，SHA `c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46`。167=81u+72v+9height+5body；冻结g后162。
- 完整g SHA `fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`；原selected canonical924e7de4…（完整报告有全值）。原唯一250步η.7136/κ106/负z失败，不盲加预算。

R57使用真实e=|Xs|²−1、q=Xs·T，η=(|e|+sqrt(e²+4q²))/2；G=a²准确。R60高度只改共同z原函数。原函数查询依赖已修：旧四点h.00738是假，新h.0522307355873稀/密差2.78e−17；不能用求积末位解释O(1)误差。

## 3. 当前真实几何状态

长入口ell=.162 actual43622984979失败η79.34/κ226.8，入口外只共同平移，不重跑。短入口actual43627111925/source8c53fba0，ell=.081，两新场paired/boundedη1.45982/1.34092；原162值和g未变。单B7步骤均因更早负z迫Δc≥2.95/3.42>盒容量2而为空。详notes/frame-entry-short-bounded-actual-audit-20261114.md。

short完整第三输入：`notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz`，decoded2618547B SHA `9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c`。初始bounded物理SHA5e8cf334…。

**最新九高度actual43630874689/source6cbe68bc complete127.4s。** 固定T/a/g，原[-1,1]^9内一LP松弛0、一QP2iter，实际只应用一次高度步。新物理SHA `f198ba74dcf3644569bf1ed78eecbc48a0f21ec421205d46a6b159cb00ff0f56`。帽高.1427042008431，minz.01425708，ballnorm².98754057，采样高度门通过；η1.388247、metriccost.03158755、κ149.42、镜像法弦.01425979<.061，仍失败。bodyη.61414、patch.286919；strip最大y.393509仍>.38。g/uv/T原样，六jet独立有限差≤1.25e−14；同态384→768 η1.388247397、镜像.0142597873，非连续包围。

当前输入：`notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz`，decoded1815965B SHA `f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3`。完整新九系数、门与精化见notes/fixed-nine-height-actual-result-20261114.md。旧loader失败43629844644已按paired共享grid/bounded参考差严格修；未LP/QP的失败仍保，dev43630530984已过。

## 4. 几何正在实施的下一步

`frame_height_quartic.py` e4105426…准确压缩固定T高度目标，保九高度poly全部A/b/原盒，解析grad/Hess。公开dev43631537869通过：grad8.62e−12、Hess2.67e−11；逐圈无约束四次极小/S仅数值必要诊断，不是严格下界。准备一次120iter/300eval/30s四次阶段，再完整重构。

`frame_entry_single_q.py` b0744e42…加一个W5 B3·归一(kθ/k³) v列，162→163；q=0数学上准确含父场，g/b0不变。公开dev43630999193通过，zero-Q六jet全0，Jac≤1.02e−8。新Q盒明确[-8,8]。联合全链dev43632772378已pass（动态z Jac1.86e−11、零Q六jet全0、四输入/数值poly/失败保best均过）；首actual43633105146在poly回放b差3.89e−16停止（A差0、尚无优化）；正修为保原A/b与明确末位对照，继续原80iter/120eval/300s：原u/v盒[-8,8]、height[-1,1]，硬帽高和**当前**signed-z非线性行；同一cached X/Jac供目标和约束。工作网格变更单列objective身份；初态同网评价，最后160×384/768同参数审计。uv变化时不得复用冻结T高度多面体。返回/best必须同时核cap、z、盒；ball/strip仍原目标和末门，不暗改阈值。

帽高Gate c55fe53c公开dev43629262349已过；h=hbase+λᵀc、uv行0。R66当前τ.061只为较强设计必要门，h≥(81+sqrt3685)/1000+.001；README由D≥2仅迫τ.06。R74近等距必要镜像floor/|b|/S筛还须守ε<1前提；当前η>1不能冒满足。帽高不是全reach。新B=.36/.37须全core/端口/c0/g/参考重建，已有transport设计与R66分支表，非旧g精化。

## 5. 理论状态、最新准确实算及下一算子

R37/R45真实零二阶桥/四块闭合，R52完整三阶重叠圆；都没有有限连续闭嵌入族。R56完整变系数有限编译已成功；旧R52 frozen profile full-fourth失败，不重复。R70把真实M0桥的全部第四period降到P0+NP1，仍保P0/ruling。R71真实第三交换子、R72任意frame的M=T0同scalar桥；有限系数用有限小loop，不越出局部控制区间。

R73逐s八矩与链式Ψ给T=−history+∫C；M0 history可由R71消。R76准确隔离真实闭scalar路径2∫C，真实长度变化重积frame给2t C3[path]，保Φ_M²和frame校正局部成本。R77有限维对偶+真实状态右逆证明面积/三次速度整个系数空间真实有限可达，含形式阳性的两C3列。

pure old43628716304余76项；新word43630157008/sourcef3381b75余95项，10原式依赖给响应真dim≤18。最高jet2/右尾深2，科学压缩见notes/literature-word-normal-form-actual-audit-20261114.md，不再盲扩normalizer。同期local形式54列rank46给fresh原式余0关系：5R71+5local；不是共同路径已付。

旧C1 actual43631537869完整95行两商81zero/14余，只余h^-1/h^0低次k/ω，三profile不成；L+=−τ(p1,p2)/12真关系。R79已证闭C1真实有限可达与固定端点势。

**新endpoint actual43632772378/source31a276f6 complete6.840s**：101行端点势商全fresh核，151cols代表rank18；真实端点势加入后，18个明确有理R71系数使pure P1原式余0！已登记R82及完整关系，摘要SHA622cd662…、关系fa33f51a…。旧pure阴性遗漏仿射端点项，不重复；本次只付−4，非全相位/完整第四。

R78已证全P1=L(F,D)+Q(D,D)，四实函数或两复模式等价。R81已证真实H=[r0,s0]−3[r0,r1]保全部pure而对三矩光滑圆给非零−2；不冒mixed满射。pure仅核Q(q²,q²)，另需L(F,q²)+Q(d,q²)；同一真实参数共同匹配，不能独立调两mode。colored actual43632772378/source31a276f6于300s列响应阶段资源退出，152原模板，完整local/种子已核；新d7513321已精确预消完整T及基准可达项，原式核删列/吸收/最终两mode，300s不变已再请求，旧partial保留；diagonal τ不确定全T。全phase/P0/逐s ruling、更高阶收敛与宏观几何继续欠。R80已证完整真第三仿射类Tend+W及两mode实际函数商必要充分门；同类控制不再盲添。新core工厂ea799032已落地，人工43633105146双侧234列及全部身份/拒错已pass，新单态driver fbe810c9已写，本次仅完整IO人工；真实B=.37尚未请求，不混旧g。

## 6. 连续推进

当前请求fullphase预消修订actual与新B单态IO人工；旧Bjoint修已发表poly末位回放，不改原约束/盒/预算。子问题结束即接open下一项，不等待用户阶段批准。真实输出自动发布后实际pull并核两README，再同步H/log/open/results。原始文献及撤稿/成对等距/局部片的适用边界见notes/literature-20261114.md，不再以来源清单代替研究。
