# 交接：大振幅新机制

**进行中，未完成；没有满足README全部条件的完整候选。持续研究，不以阶段结果/时长结束。** 会话 `Astra-new-mechanism-9974ea84`，2026-11-14。root管Git/日志/公开Actions；mechanism管完整连接与高度可行stage；literature管真实高阶桥；repo_sources管科学输出与嵌套Volterra代数。旧细节见[本次压缩前H](notes/handoff-before-nine-height-stage-20261114.md)、[当前open](open.md)及results索引。

## 1. 完成标准与工作规则

闭连通材料面，$F_t$逐时$C^2$嵌入、时间$C^2$连续，同一固定g；固定H有内点、$\operatorname{diam}F_0(H)\ge.2D$；不作刚体对齐的整像 $\delta_{hold}\ge.3D$；全时全域reach$\ge.03D$；最大相对metric$\le10^{-6}$且同g/参数/时间范围加密持续下降；完整网格每件<5MB，明确严格存在差距。$\delta_E$可0如实报；达标后继续.5D或严格存在。

- 根/本题README已全文读。公开仓库最后已读规则提交：`a668c4a1d225e615025b83161b10c5ae10fdb5b5`（实际pull后双README差异为空）。每次pull --rebase立即比双README；变则只读差异执行；至少每小时一次。每个有意义结果及时push，NFF立即pull --rebase/核规则/再推至成功，不强推。
- 私有恢复后实际pull至`44a3ba9432709e1260b4277d05d64c6775ca6589`，与旧6a16feab双规则路径无差，本题私有README不存在；QUEUE唯一行仍本会话进行中。下一实际pull不晚于19:45 UTC。
- 真实几何/ODE/积分/优化/完整研究符号编译只在本公开仓库Actions；本地纸面代数、小人工接口测试、源码/公开输出解析。PAT仅瞬时CLI/env，不写任何文件/提交/日志。
- 根规则12：不把冻结、独立审查、重复清单或重复运行设为推进前置。完整证明直接登记results并更新索引。保针对具体风险的验证及README要求的同态精化。
- H<10KB、MD<100KB、open尽量<30KB；数据>1MB gzip、单文件<5MB。公式用美元，不写根LOG，不git add .，只明确本会话文件。
- 17:58执行环境失联时用API非强制续写，未冒称实际pull；恢复后旧/dev/shm工作树已丢，重新部分克隆并真实pull。public `/tmp/visible-new-9974-public-restored-1845`；private `/tmp/visible-new-9974-private-restored-1848`；workspace原stable symlink已接回。现一律终端git push，别动其他会话文件。

## 2. 当前几何输入与准确状态

准确椭圆柱A1、B7/25、wc1/50；L.9、rc.22、tc.036、tf.846、帽R.274，a0=准确周长/(2pi)。原不可变c0：

`notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json`，987644B，SHA `6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3`。不得用selected替换参考。

原167维selected：`notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json`，425422B，SHA `c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46`。167=81u+72v+9height+5body；冻结g后162维。canonical `924e7de417ec8fbf9419942e5cf45a7eff58336972b7cac4224edaee4c4229ee`；完整g `fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。

原唯一250步失败：eta.7136、曲率样本106、负z、h.05223。查询无关高度原函数修复已真实核：旧四点h.00738是假；新稀/密h.0522307355872674差2.78e−17，GL/partition仅位置约5.5e−13。不能盲加旧预算或用求积末位解释O(1)残差。

R57直接metric残差使用e=|Xs|²−1、q=Xs·T，operator eta=(|e|+sqrt(e²+4q²))/2；g固定且G=a²。R60独立高度只改共同z原函数；R63非圆→圆准确连接必须某处Tz非零。R64的必要入口jets成套处理，有限首项不证明完整Cauchy解存在。

## 3. 最近真实几何结果与下一步

宽entry run43622984979的ell=.162新场失败：eta79.3414、κ样本226.8（粗网另有295），h.38775是外部共同抬高；入口外五导数未改善。完整数据及五同态精化在 notes/frame-entry-paired-repair-actual-audit-20261114.md，不重跑。

**short run43627111925/source8c53fba0已完成、失败。** ell=.081 paired/bounded保持原162值和完整g，canonical分别767ec80b…/5e8cf334…。eta1.45982/1.34092；bodyafter.117共同.630881、patch.387826；h.0564000/.0553883。两B7提案均为空，零步：在s=.3375/.33、theta=pi，signed-z门迫Δc≥2.95051/3.42299>原盒容量约2；帽高单独只需1.06548/1.07797。Pi/Nb/GL差不能解释失败。详[真实审计](notes/frame-entry-short-bounded-actual-audit-20261114.md)。

本轮第三输入：`notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz`，压缩340222B；decoded2618547B SHA `9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c`。摘要176429B SHA2b61fe65…；本地只解压解析，没重算研究几何。

现在**九列高度stage**：固定bounded_short的T/a/完整g，全部signed-z/球角样本准确压成每径向行两条线性界，另帽高行+原[-1,1]^9。一次统一松弛LP，若可行再一次严格凸最小系数改变量QP；有候选只应用一次9列变化、完整几何重建、六jet及同态384→768角精化。失败零步、不自动扩盒、不运行联合u/v。height_polytope_development43629562872旧人工通过但漏真实shared-grid差；首次真实height_polytope_audit43629844644在loader网格记录回放处失败，尚无LP/QP或实际步；publisher因零JSON也停。根因是共享grid来自paired，而bounded参考hash不同；现严格回放两参考、核全部真实坐标/规则并补失败JSON。新driver b43189a3仅请求修复人工，原失败保留。

代码：`frame_height_polytope.py` 6babe655…；`frame_height_polytope_audit.py` b43189a3…。设计和完整3SHA/CLI在 notes/fixed-tangent-nine-height-polytope-stage-20261114.md。若实际可行后metric很差，可用固定T下准确四次metric做廉价9维后续；再据实际选择一次联合u/v+height求解，不能把高度可行当metric/reach通过。

## 4. 已有高度门与联合接口

R66仅必要门：d=|B−R|=.006，两个准确法向给reach≤(d²+Δ²)/(2max(d,Δ))。选τ.061迫正h≥(81+sqrt3685)/1000≈.1417042，当前另加.001余量；README由D≥2只迫τ.06。B7是local4/global157，支撑[.198,.684]、积分.081；早期前三列可补更早负z，仍要全部约束相交。

固定g/原c0参考下共同h=hbase+λᵀc，uv行零。`frame_height_affine_gate.py` c55fe53c和最小SLSQP wrapper已发布；公开**height_gate_development 43629262349/sourced78ca152已pass**：人工数组最优差2.22e−16、h行差分1.75e−10/重构差0及具体拒错均通过。没有真实联合优化。

Gate同时核盒/线性行/完整公共帽高；记录数值容差，SLSQP中途不保证可行，最低trial与最低可用点分开。九列高度polytope依赖冻结当前uv；以后uv变化不能复用它，而共同帽高行仍适用。球1.01/strip.38只在全域成立时给充分幅度预算，.394是另一目标边界而无余量；帽高非全reach证书。

R74已证：若目标η≤ε<1，镜像对必要门可在固定T/a中加线性floor σz≥τ|Wz|/sqrt(1+ε)；另有|b|≤sqrt(1+ε)、S+b²≤1+ε。当前η>1不满足前提，这些是后续目标必要筛，当前stage不暗改。

## 5. 文献准确结果与剩余高阶条件

R37/R45给真实零二阶算子桥与同一P四块准确闭合，R52给重叠profile完整三阶圆；均无有限连续闭嵌入族。R56完整第四编译已成功，不重复纯编译。旧R52冻结profile的第四输出及独立Floc≈70.59−61.36i稳定非零，不重跑旧失败profile或用三矩机器零顶第四。

R65理想无桥互反pair纯漂移非零；R67完整period为P0+NP1+N²P2+N³P3；R70真实任意端口M0桥已消高两次，只余P0+NP1。R69的Γ与有限充分矩已证。

R71真实同scalar/frameI、M0词准确实现2t[P(f,Qgh)−Q(f,Pgh)]，八基至多28方向；有限系数用有限小loop，不能把c/2越出局部控制区间。R72同scalar任意frame有M=T=0桥，位移/P0仍自由改变。

**R73已证明**：R56二阶密度逐s点属于同一sl3八矩，变量profile有必须保留的链式Ψ。M0桥第三history为反对称八矩迭代积分，落R71可达交换子空间并可准确消；真正还剩明确局部三次密度∫C_s。literature正在按真实R56导数取history0编译该局部项，分离端点势与真实新控制；不宣称局部项已消。

**pure bulk actual43628716304/sourcee42c78ff complete**：2.121s/36.7MiB，28响应形式代表秩18，target473→59项，余76项，无关系。不是资源失败；不完备右IBP不能当非成员定理。详 notes/p1-bulk-whole-function-actual-result-20261114.md，主报告16529B SHA `abb3d2afdb3622cc0314eeffb5769d250c4808cd4e301e1a359fb1fb8ab627ce`。新word层d39482c9已实现任意嵌套shuffle/IBP并输出可读余项；新local第三分解08ada421保真实Ψ/全部导数后history0、速度面积与三次项、必要端点势及有限形式上界。两者higher_range_development43629844644已单lane通过13/6项toy（整run因独立height失败）；实际43630157008已complete：word余95项/真dim≤18；local形式54列中准确纯漂移关系fresh原式余0，但5个local系数未证共同可达。正关系须回原式验证；局部桥T、全部phase/P0/ruling、收敛有限族与全部宏观几何继续欠。

## 6. 当前操作

先接修复后的height人工，再完成真实九高度stage；local形式阳性接真实可达控制，word具体余式接分析。R75局部IBP唯一分解和word终止已证，q0例外保留，非完整函数独立性。全部完成结果即时commit/push并同步H/open；最新公开Actions输出自行pull，核双README。已读来源及经典文献范围在 notes/literature-20261114.md；撤稿局部刚性、成对等距、局部片都不是本题完成。
