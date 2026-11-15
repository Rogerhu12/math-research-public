# Request 153：同次连续 C 取样、真实全112零响应、完整敏感度与有限审计

作者：AI（geometry agent）。日期：2026-11-15。状态：独立源码与明确公开 Actions 配方；本文不预填运行编号、实际输出、收敛或验收结论。

## 1. 本次实际执行对象

本请求定义并执行 **一条**物理高度请求：112个原 binary64 正零，负零 sidecar 为空。请求同时明确 jacobian=true、audit=true。原高度 raw SHA 为 d54f02b97ed5bc2a642756268b41d4b8f7a077e73224e1580d22436834a14db5。本次零向量是新配方自己定义的初始子问题，既不是旧非零场、旧 checkpoint，也不是旧有限尾零响应的别名。

运行链先在同一真实 job 重建 R286 约定 C 的全部原1440片、六 primitive、准确根族和原闭径向查询；独立形成 R312 的全部112深端列；随后选择一个明确 binary64 物理远端，重新从深端传播到它，并对整个新有限原生网格的每个实际取样字词做同 C 闭包围。只有这些输入实际齐全，才启动一条新 live native 请求，求真实零响应、完整全112列无阻尼敏感度、338行端点输出及独立有限审计。

这一步明确支付新有限模型的零响应子问题。它不宣称已经求得新非零高度、699/453完整物理 BVP、任何 accepted 闭场、连续全角误差证书或无限非线性 C 的 DN。下一步必须由新 profile 与真正 BVP 形成新的实际高度，送入同一能力的 live client 重新求解；不能把本次零结果当非零缓存替代物。

依据是 [R331](../results/R331-current-C-zero-seed-general-Robin-and-complete-sensitivity.md)、[R324](../results/R324-continuous-C-finite-head-flux-and-closed-tube.md)、[R312](../results/R312-continuous-C-complete112-zero-tail-and-head-connection.md) 和 [R286](../results/R286-original-stored-continuous-integral-and-metric-bridge.md)。它们分别负责一般边界链结构、有限头严格列传播、深尾列以及已声明的连续模型；结构证明本身不提供本请求的实际运行结果。

## 2. 新源码与保留依赖

八件独立新源位于 computations。旧源不改写。本表长度与 SHA 对应最终完整文本，不以失联旧草稿的 SHA 代替恢复后的实际文本。

| 文件 | 字节 | SHA256 | 责任 |
|---|---:|---|---|
| geometry_20261115_current_C_general_robin_native.mjs | 24004 | fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349 | 每次真实有限非线性评价、方向、端点和有限审计 |
| exact_20261115_current_C_general_robin_chain.py | 28822 | 946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5 | 完整一般 Robin 链、方向和全112敏感度 |
| geometry_20261115_current_C_synchronous_linear_bridge.mjs | 20092 | 67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286 | 现场全数组同步子进程桥 |
| geometry_20261115_current_C_native_worker.mjs | 18173 | 173d82b09f0511346c1deedfd9b6563d1a0555b9a9e12636c0a6d842deebccce | 唯一 live worker、实际几何字词与请求关联 |
| geometry_20261115_current_C_radial_sampling.py | 41983 | 1dec587d72d4c9c9805fd090951df49d751755a4334645d2f410d18c2287e812 | 同次 C 完整闭点包围、真实物理远端列及数值代表 |
| geometry_20261115_current_C_tail_client.py | 23068 | 8c7bd23a2eb3be5d4b739483973912b273ca3f2282fc52b312e1c4bdf53c5616 | 同一进程完整 TailClient 协议 |
| geometry_20261115_current_C_native_launch.py | 14469 | faf11a8fbe3c9c43175be902b27a782cc295d7dba487bb15d0f90670399be13c | 明确请求、全源绑定、资源及进程组生命周期 |
| root_20261115_current_C_native_scalar_readout.py | 29751 | 2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff | 逐原记录读回与无损分段，不做科学算术 |

原已发布源的直接闭包仍逐件保留；与上述八件合为 request 和 native recipe 相同的24项 source_sha256：

| 保留源 | SHA256 |
|---|---|
| geometry_20261115_stored_continuous_E_cover_v3.py | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df |
| geometry_20261115_stored_continuous_E_cover_v2.py | 004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea |
| geometry_20261115_stored_continuous_E_cover.py | 9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed |
| tail_frozen_geometry.mjs | db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3 |
| strong_frozen_calibration_factory.mjs | 77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247 |
| closure_bounded_point_cache.mjs | 35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043 |
| exact_20261114_closed_background.mjs | be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b |
| exact_20261114_public_resume.py | 11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5 |
| source-dependencies.json | 7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941 |
| root_20261114_current576_rules_runner.py | 3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde |
| geometry_20261115_stored_C_v3_cut_twojet_readout.py | 1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed |
| geometry_20261115_stored_continuous_C_far_graph.py | fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a |
| geometry_20261115_stored_C_finite_head_flux.py | 4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d |
| exact_20261114_tail_capacity_loader.mjs | 07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395 |
| geometry_20261114_noj_matched_variational_engine.mjs | f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9 |
| exact_20261114_native_damped_chain_qr.py | 9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33 |

另外，public78原源恢复器按原 source-dependencies.json 和其内实际 revision 恢复原公式模块。recipe 明确锁原 split engine、product-J、momentum root、cusp、physical-jet、metric 模块和 noJ-matched 引擎。它们不是新 C 系数来源；其有限方程与完整返回结构被复用，实际 profile 只由本次采样器供应。

原 engine a47df10f…、product205b28db…、rootcbf75389…、cusp b12f3626…、physicalJet2b96df25…、metric36e4e642…与 noJf9b292c4…的完整 SHA 在 native recipe 的 original_runtime_sha256 中。每个实际模块导入先按当前字节检查。mode-capacity07d45b95…只以当前112容量装载原代码，不替代数学原件。

下面六件证明原文也按完整字节绑定：

| 证明 | 字节 | SHA256 |
|---|---:|---|
| R286-original-stored-continuous-integral-and-metric-bridge.md | 37491 | 81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb |
| R297-continuous-E-unit-panel-and-piecewise-enclosure.md | 15793 | 3505389d22bc63f6d7b5c7cde62e36e856d94993841fc7eb3cdd034ff92a10e0 |
| R306-complete-cap-endpoint-primitives-and-budget-preserving-integration.md | 13875 | 6f3593306fa66098c73f2aaa12ca21788263c24eac6f31c881bb52308b601ea1 |
| R312-continuous-C-complete112-zero-tail-and-head-connection.md | 26907 | 036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73 |
| R324-continuous-C-finite-head-flux-and-closed-tube.md | 14346 | f99acd8b025b38f5f2cdacbc8e129debbb48467587e72f92f74df5065fcad796 |
| R331-current-C-zero-seed-general-Robin-and-complete-sensitivity.md | 24156 | 044ae2a9d9d3cb31450cf8487b31a0577b5a7742e8776d66fef8a0453d1649e8 |

本环境恢复源码后没有进行新的本地 Python import、数值计算、Node构造器或科学调用。当前完整文本可重现；真正 Python AST/compile 与所有 mjs 的 Node --check 安排在本次 Actions、科学开始之前。没有把先前失联版本的 AST 记录冒称当前文本已经执行过。

## 3. 原输入、模型身份及实际来源

三原始数学输入只恢复一次，逐字取自原历史公开提交8bd267107cc8710d371f3b62c02986655ac965b0：

| 角色 | 临时 basename | 字节 | SHA256 |
|---|---|---:|---|
| config | tail-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| calibration_ledger | ledger-ready.json | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| stored_reference | stored-ready.json | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

其确切仓库路径、Git blob（适用时）、历史提交和角色保存在 public-current-C-full112-native-request.json，恢复后文件只在本请求自有 RUNNER_TEMP 目录。没有把旧ready包中的原逐点表、48步 selector 或旧 graph 当作新模型 C 的连续几何。

模型 schema 固定为 R286-original-stored-continuous-model-convention-C-v1。C 生产器仍是 f12f7470… v3，全部160×9原片及六个 A、B、sqrtE_A、sqrtE_B、w_A、w_B primitive 保留。深端 n≥160 原准确根族及其包围保留；没有选择并认证一个可计算单根族，也没有引入 R26 的另一个数值对象。

原查询文件 original-stored-continuous-E144-queries.json 仍先处理 config 的原 binary64 cut=0.3闭点，再处理整个自然径向域。没有把 cut 重归一到名义值或用某个 Rout 中点。真实 natural Rout、源片、闭点覆盖、全部未付叶与未访后缀由本次实际结果决定。

f12f 的预算仍显式3600秒，区别于首次148上游1800秒；该公开资源变更沿156已声明版本。precision256、全部积分/工作宽度/细分/面板约束及原目标表达不改。查询达到工作宽度与闭覆盖有效性是不同字段；粗而有效的包含不因工作宽度不足变成几何失败。

## 4. 精确包围、数值代表与不能合并的责任

本链有三层对象，报告分别保存：

1. 约定 C 的实对象与原准确根族：primitive、完整半径逆像、w及其导数和同物理远端的两坐标列使用 Arb 包围，并保原源片和所有分支。
2. 本次独立选择的 binary64 采样代表、坐标μ、端口与一般远端矩阵：每个选择值及与原实包围的差另记。没有把区间任意中点拼接后宣称它们共同来自某一唯一全局 C 成员。
3. 原 Node 有限方程：现场原 engine 使用实际 logw 字词再计算 exp(logw)、exp(2logw) 及 E。worker记录这些真实字词；本链没有认证 JS transcendental 的舍入误差。因此原生残差只控制该明确有限数值模型，不能自行支付与准确 C 的总误差。

两个原表达 exp(2logw) 与 exp(logw) 的平方不被擅自互换。几何包围与有限代表之间的误差记录也不被当作无穷尾非线性误差证书。所有中间 result 中对应的 exact_global_C_realization… 与 infinite…certified 字段保持真实范围，不能因 workflow success 自动置真。

## 5. 真实物理远端与完整列

旧 deep far 原归一节点是准确 C 的不确定半径盒。新采样器不将它的中点冒充该原节点。本次取原 cell8/segment8 外端的完整半径上界，再选严格大于该上界的第一个可表示 binary64；还要求这个实际字词严格小于原 cut，并处于实际已包围的 C 域中。若这些条件无法成立，原输出明确未付，所有 native 请求未启动。

采样器对该明确物理半径的**全部**闭逆像逐片处理，保真正 r_x、w_x、全部边界和原深端列，从 R312 的深端重新传播到这里。R324 的真实误差、Taylor余项、完整初始盒、二幂归一恢复、所有可能逆像片、已完成与未开始 mode 都保留。没有对高度列 U 做除法，因此不需要任何内部 Dirichlet 图。

每个物理频率 m=2,4,…,224，在原归一 Q_F=1 的同一完整两坐标列 (U,K=H_r) 上形成一般边界行：

$$
(-K r^4 + U m^2 r^3)\,Q
+\frac{U\sqrt{12}\,\mu}{r^4 w}\,\Pi=0.
$$

每行只允许同一个准确二幂整体缩放；随后两系数的完整包围、实际选取字词和代表误差全部保存。不能由浮点行非零或末 cut 可除倒推所有内部图可除。数值行同时来自一个共同准确 C 成员的断言仍未支付。

原 complete112 general far rows 的全部原 JSON 行会逐行进入读回日志，包含 (U,K) 区间、μ/r字词、两系数及误差、整体二幂和原归一说明。即使后来 field sampling 资源中断，已写出的原远端行也单独读回，不把它们冒成完整 geometry_ready。

原4531的 main 不在153中执行，不生成或宣称原148/156所求的 cut DN图。153复用的是该冻结源实际函数，用于上述深端到**新物理远端**传播；它的实际输出独立归入 sampler schema。深端完整和当前有限远端完整也仍不等于 cut DN或无限非线性DN完成。

## 6. 新576阶段与实际字词取样

新网格有577节点、576阶段、每阶段12个RK4步、每次2048角节点、完整112模式。节点从原 cut 到新 rFar 严格递减；原公式为 binary64 exp(log(cut)+(log(far)-log(cut))*n/576)，两端固定为实际原字词。每阶段在相邻物理半径间向外仿射推进。

rawNode=[0,72,144,216,288,360,432,504,576] 在这条新网格中是明确分组标签，**不声称**复用旧 C 的8×9原几何块分段。各 actual RK 参数字词包括 k/steps、x+h/2、x+h 及有限审计的 k/steps、1，全部在采样计划中显式枚举。浮点加法形成的某个场点若略超名义阶段端点，代码不裁剪或替换它；实际物理半径另外按完整 C 域检查与包围。

worker只按真实 x raw字词查该阶段已绑定 field map；没有临时插值、旧 profile fallback、重新按标签生成半径，或将两个不同 x 字词合为一个名义值。μ按实际节点 r、实际数值 logw 的声明表达计算为有限正值；端口使用当前两个μ的原binary比值。无旧每节点 gains 或 G 被借入。

只有当前 source/result/全部数组身份与完整 field map 齐全，才返回 native_geometry_ready。点值工作分辨率 false 不被当新数值验收门；但缺源片、缺域、不能得到有限正坐标或缺完整行时，保持真实未付，不能填补代表。

owner采用容量2的确定性局部 engine缓存，避免同时保留576份同维角表。重新创建使用同冻结公式；统计counter不进入原科学表达。mean两分量保留完整226推进与两行切向贡献，只有224 shape反馈到每次局部矩阵，不把均值投回形状。

## 7. 一般边界链、阻尼方向与无阻尼响应

原状态坐标是每节点 z_n=(Q_n,Pi_n)，224维。切口 target 为实际 H/rCut^4，rCut^4就是 owner现场计算并保存的真实binary64字词。初始shape577节点全部正零；不会通过把首节点强制改成 target 来偷偷投影 cut残差。对本次 H=0该初始子问题明确成立，但仍真实调用当前 evaluate/roots/flow并读其实际结果。

新σ选择公开为每节点相同的 max(reference_floor,max_abs_current_Q_target)，reference_floor=1。本次没有沿用旧σ，也不宣称与旧范数数值等价。后续新H仍按声明同一规则形成各次实际尺度。

完整线性链保 cut112行、576×224 stage行和far112行，总129248行/变量。中间stage是 −I 与本次完整J的真实配对；far是本次全112×224一般矩阵，不强迫写成旧[-G,I]。全局边界方阵秩与每个内部−I可消元是两项不同责任，按R331明确区分。

非线性方向使用 eta=1 的完整平方根链，所有节点罚行和常数能量保留；它只供应原线搜索的候选方向。原链原32轮、10个 alpha=2^(-k)、原 guards、原noJ试探、严格 norm下降和原2e−9收敛界保持。完整stage J由本次现场原withJ生成，noJ-matched引擎维持同一primal顺序。没有exact残差、L2、梯度或浮点rank新门。

端点敏感度必须用**同次最终 freshwithJ**与 eta=0 的完整112 RHS。cut RHS 是 −I/(原cut_height_denominator字词×sigma0)，stage/far RHS为零，罚行为零但行结构和全部常数仍保。每个节点都恢复 delta=sigma*z，不把cut顶半强制改写成预期答案；所有577×224×112原敏感度与节点0的224×112别名逐字关联。

只借用冻结9b951…的完整 Householder qr_prefix；新far块、factorize/formed/readback、绑定与输出都是独立明确源码。因子下三角pivot为有限非零的浮点观察不是严格非共振证书。零pivot、非有限、资源不足或原域失败按实际原因保存，不预付全局可逆。方向的原dyadic全行账及敏感度全部112 RHS最大残差仅为读回，不作为新的非线性门。

## 8. 338端点与独立有限审计

实际返回的338行顺序是 slope[112]、second[112]、meanSlopeCorrection、meanSecondCorrection、height[112]；每行对全部112实际物理H列。第一斜率和meanSlope由当前局部导数乘完整当前cut敏感度形成；其余second、meanSecond与height保原来源的1e−4对称差分方法。全部字段如实记录此混合生成方式，不把整个338×112矩阵说成严格区间导数或binary64有限算法的精确导数。

该方法在零输入也实际执行；不能用旧零J或旧有限尾表补输出。所有端点原physical jet和真正当前cut port保持。完整数组在临时包中；读回记录完整实际JSON/原数组身份、行数和原生产者字段，不在本地重算导数。

audit=true触发独立现场有限重放：全部576阶段、每阶段12步、2048角节点及完整原几何/物理jet检查。原fullD、normalizedFullDefect、leading/D、formalCurvature、physicalPV、actualMetric和holonomy字段由该真实审计返回。它没有等同于连续全角/闭面metric或原target atlas证明；没有通过字段标签直接支付seam、reach或无限尾误差。

只在真实native收敛时计算端点敏感度；若原求解不收敛或敏感度失败，完整现场和该失败保留，没有将selected中间态当最终响应。本次只有一个协议请求，因此不存在第二个“默认为最终audit”的新native solve。独立audit是这个请求内真实有限审计；后续 fullDN 的外层fresh audit请求将是另外真实call。

## 9. live client、缓存与后续新 BVP

TailClient保原四参数接口(config,sources,prefix,node_heap)。唯一owner进程跨请求存活；只缓存这个进程实际完成的同H、非audit响应。audit强制真实新call；新H送同一worker实际求解，不用anchor旧J换标签。

同一live进程可将刚完成的全577节点状态和全节点敏感度用于下一H的初猜；预测仅初猜。每次root/RK/J/完整非线性环仍真实执行。请求输入完整112词、负零sidecar、source/geometry身份、call/iteration/sequence与结果关联都明确保存。

startup ready只真实评价零cut root；linearSlope=null，零DN未预先假定。第一条recipe请求才求完整零响应与112列。以后新profile/BVP必须重新形成实际H；本工作流没有预填该H，也没有声称同worker fullDN8outer全部成本已获预算。全DN接线不能用跨进程零结果冒同live状态。

## 10. 精确 CLI 和临时布局

sampler入口（实际SHA都在运行时从同job原文件计算）：

~~~
python geometry_20261115_current_C_radial_sampling.py
  --code-directory COMPUTATIONS
  --cover-directory BASE/continuous-E
  --cover-result-sha256 ACTUAL_C_RESULT_SHA
  --far-directory BASE/deep-far
  --far-result-sha256 ACTUAL_DEEP_RESULT_SHA
  --proof R324_PROOF_PATH
  --out BASE/current-geometry
  --precision-bits 256
  --linear-budget-seconds 1800 --sampling-budget-seconds 1800
  --max-panels 200000 --max-depth 32 --local-defect-bits 12
  --panel-norm-limit 1/2 --taylor-terms 24
  --max-geometry-cache-records 65536
  --sample-max-nodes 1000000 --sample-inverse-depth 24
  --sample-value-bits 32 --steps 12
~~~

实际启动器：

~~~
python geometry_20261115_current_C_native_launch.py
  --geometry-directory BASE/current-geometry
  --geometry-result-sha256 ACTUAL_SAMPLER_RESULT_SHA
  --recipe COMPUTATIONS/current-C-native-zero112-recipe.json
  --recipe-sha256 5ace7ca3782e2a1578516c7e502a4ebf5d2c39cace1e7626dafd7f0518363ea8
  --computations COMPUTATIONS
  --source-topic RESTORED_SOURCE_TOPIC
  --out BASE/native-launch
~~~

读回：

~~~
python root_20261115_current_C_native_scalar_readout.py
  --sampler-directory BASE/current-geometry
  --sampler-result-sha256 ACTUAL_SAMPLER_RESULT_SHA
  --launch-directory BASE/native-launch
  --out BASE/native-scalar-readout
~~~

没有sampler result时读回可省可选SHA，明确 unavailable，不制造native结果。launcher还检查sampler run_id/source_commit/source/model，不能把历史相同schema包当本次输入。

内部QR CLI仅由同步桥调用，要求 --snapshot-directory、--snapshot-result-sha256、--native-owner-source、--computations、--eta、--budget-seconds 1800、--max-factor-bytes 2147483648、--out。调用shell=false，完整stdout/stderr各有独立文件，不能污染worker行协议。

所有原始文件位于 BASE=$RUNNER_TEMP/visible-current-C-native153：

| 目录 | 原件责任 |
|---|---|
| original-inputs | 三件原数学输入，只恢复一次 |
| source-topic | public78原公式源，源闭包身份固定 |
| continuous-E | 当前f12f原完整结果/primitive/query/未付账 |
| cut-twojet-readout | 原point全部leaf的独立读出 |
| deep-far | 本次全112深端原列与输入绑定 |
| current-geometry | 全部采样包围/逆像/字段计划/数值代表/远端列/原数组 |
| native-launch/live-client/native/call-* | 每次实际请求、trace/trials、原state、成功或失败响应 |
| native-launch/live-client/native/linear-children/call-* | 每次现场snapshot、child输入/日志/完整factor和所有RHS |
| native-scalar-readout | 原读回索引，必要时完整语义分段索引 |
| rule-sync、rule-sync-far、rule-sync-sampling、rule-sync-native | 各实际规则runner同步与真实child退出记录 |

实际source-topic目录以原恢复器返回的 VISIBLE_SOURCE_TOPIC 为准；表中只是其在自有BASE中的职责，不以名字替代真实路径与SHA。

## 11. 全预算与实际时序

| 阶段 | 明确源码预算 | Actions step cap | 范围 |
|---|---|---:|---|
| C六primitive/全1440/闭query | 3600秒；原200000panel等不变 | 75分钟 | 实际partial与完整域分开 |
| point全leaf两jet读出 | 原读回程序 | 10分钟 | 真闭点/真源条件 |
| R312全112deep | 原代码参数 | 5分钟 | 不冒cutDN |
| 物理取样与新far列 | 独立linear1800秒、sampling1800秒 | 70分钟 | 同一sampler中分别计时 |
| 当前完整native请求列表 | 全部列表合计3600秒；本次仅1条 | 75分钟 | 原32/10不变，资源中断诚实partial |
| 每次QR子程 | 1800秒；2GiB原factor预算 | 包在native总预算内 | 不是额外无限延长整call |
| 原native完整读回 | 无科学算术 | 20分钟 | 先读后清理 |
| compute job | — | 300分钟 | 包括环境、恢复、所有阶段和读回 |
| compact report | — | 5分钟 | 只重复实际已读小块身份 |

sampler的linear预算在绑定/建geometry之后、实际列传播开始时建立。sampling预算保留先取得far点已耗的时间，只从其墙钟中扣除独立linear阶段的实际时长，不重置原已计采样工作。sampler总elapsed还包含输入绑定/setup。QR子程自己的deadline以其main开始计时，包括其runtime/binding阶段；桥还有原预算加120秒的进程等待界。外层native资源总3600秒统管owner与所有同步children。

启动前检查至少32GiB空闲，并只移除runner明确未使用的Android/dotnet/ghc目录；这是可用资源检查。它既不保证一条最坏32轮一定完成，也不声称够19call或整个fullDN。全部原快照、因子与临时数组保留到本次读回；本请求不采用未部署的后台归档或伪缓存。内存/磁盘/时间不足是实际工程未完成，不能冒数学拒绝。

launcher用独占新进程组启动client，worker和同步QR子程继承它。正常返回、异常或3600秒超时后，launcher确认该组无活动进程，必要时TERM等待30秒再KILL等待10秒；只忽略Linux已无执行代码的zombie。确认前不允许把仍在写的现场宣布闭合。若仍未观察到组结束，结果明确partial，清理步骤保留该目录直到runner销毁，不删除并发写入现场。

## 12. 完整读回、90KB分段与坏文件责任

原C标量、独立cut两jet、全部deep112原行三块沿已有156接线保留。原156独立cut-DN第四步在153中换成sampler/native这条新第四族，不能把它们的schema混用。原C生产器、cut读出及deep source都未因本请求改数学。

新reader只用标准库读取实际文件、JSON、原行与字节SHA；不重新算norm、积分、J、原BVP或线性作用。每个实际非线性iteration输出完整原baseline和全部原trial记录，保接受/拒绝/guard/真实norm及所有原字段。若终止时最终native JSON不存在或未解析，已有trace/trials JSONL逐原行仍读出；未完尾行或坏文件保完整原字节和明确unparsed记录，不猜其未返回科学值。

每块上限90000B是传输分段界。若一个完整JSON超过界，reader按原成员路径递归分段：对象/数组保类型、全部成员数、原canonical字节/SHA、每个完整成员；超大单标量按其完整canonical JSON字节分段。**没有用hash替换超限记录后丢弃原内容**。原完整索引本身超界也同法输出；GITHUB_OUTPUT只放一个短primary，指向原完整索引的分段范围和SHA，不把大段拼回小primary。

Python launcher/client、Node worker和每个linear子程的stdout/stderr全部按12000原字节分段。段内容以UTF-8 surrogateescape编码到JSON，记录原offset、bytes、SHA及完整原文件身份；按顺序重编码并拼接可恢复每个原字节，不只保尾部。分段跨UTF-8字符也由surrogateescape保字节。坏JSON与坏JSONL行沿同协议保全。实际stdout中BEGIN/END/bytes/SHA都由对应reader产生，root以后读取所有段，不能只看最后primary。

大factor、snapshot/J和科学数组不序列化到日志；读回逐原descriptor完整hash核到实际文件。全部输出manifest、原输入数组、方向全行账、每RHS数值最大残差、完整factor metadata身份与已付/未付节点保留。338×112响应JSON、全577checkpoint/state及负零关联按实际文件完整读并给身份，不宣称未导出的字段被审过。

sampler的112 general_far_row原小行另逐完整行打印，包含实际物理两坐标和误差，便于后续使用真实边界读数。保原geometry是否ready，不能因行数112就假定field采样完成。

如果读取失败，reader保原错误、能读的所有原包和不可解析字节；这种读回错误不转成native科学接受/拒绝。Actions report允许正常primary或完整索引已分段的schema，依原bytes/SHA重印，不重科学。

## 13. 规则、发布、清理与失败语义

唯一触发文件是 computations/public-current-C-full112-native-request.json；工作流是 .github/workflows/visible-larger-public-current-C-full112-native.yml，独立concurrency不取消已运行计算。没有手工伪造未来run/artifact/result SHA。

根README基线21bd547f56590b7f2dd279d0297efb289a9b2783，题README基线bff8aea253a9e6a7a4fac28d810ac454c5499fec。冻结rules runner3b8b6dd5…包裹C、deep、sampling和native，2700秒规则同步范围保持。GitHub token只交规则父进程/原恢复阶段，bootstrap进入科学child前移除GH_TOKEN/GITHUB_TOKEN/MR_TOKEN，launcher与同步QR再移除一次；worker协议不携带凭证。

所有readout使用always()。清理最后运行，只删本请求BASE并确认其严格位于RUNNER_TEMP、非symlink、非父目录，且实际native组已停止。成功与失败均读回后清理；无upload-artifact、Release或raw Git发布。科学输出可由已提交源/全部参数/run/输出SHA重算，按规则15保留这份来源与紧凑结论。

C不完整、deep不完整、sampler未付、native原guard/line-search失败、QR实际失败、敏感度失败、audit失败、资源停止、reader失败和规则同步失败各用原阶段字段表达，不能互相换标签。原source resultSHA只在运行时计算后向下传递；过去139/143/144/148/156等结果仅说明动机，不作为本次缺失包的替补。

## 14. 发布件与本次后续

公开保留八件新源、完整零请求recipe、request、workflow及本接口；完整差异和可重算source-only检查只供主控阅读，不把它们当新科学fixture。当前工作流接线已把终端失联事实写明，实际语法检查是Actions前置步骤；没有本地科学结果。

本次recipe 6534B /5ace7ca3782e2a1578516c7e502a4ebf5d2c39cace1e7626dafd7f0518363ea8，request21082B /230c47b8cba5213c73eb64737e24a8923b2323360901867aa327413a993de1b1，workflow50286B /8dd7acc7f1dcc55229e333178715ebfd5c0e4c768f620eb52c33412400ae5296。实际root发布与运行以后，结论另依原job全读回登记。

下一实质步骤仍是新g/profile形成自己的真实非零H、当前C非线性provider真正求该H与全导数、完整BVP的原FD/fullmain/fresh audit及后续同g连续证明。本次零响应的完成不能结束这些原责任，也不能为未来非零调用预造成功锚。
