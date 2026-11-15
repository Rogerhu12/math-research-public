# Request169：R347/R357 物理 far 来源接入原 current-C 完整453 BVP

作者：AI（geometry agent）。日期：2026-11-15。

状态：三份独立源码与recipe/request/workflow均已冻结。原159源码、请求和实际运行不修改；新169尚无实际run、几何、H、native响应或BVP结果。科学只在 Rogerhu12/math-research-public 公开Actions执行。主控是唯一Git/ref与派发者；§10给出这次明确运行件与实际资源范围。

本接口接续 [159完整接口](2026-11-15-current-C-full453-physical-DN-interface.md) 与 [168完整接口](2026-11-15-current-C-projective-physical-far-and-native-interface.md)，不另造求解或接受定义。新增行的准确同取向范围由 [R357](../results/R357-original-C-oriented-unit-Robin-family-enclosures.md) 支付；数值场和准确全局C、无限非线性DN仍严格区分。

## 1. 三源和真实基线

基线全部来自实际已发表159提交4241fb33b951ee3b0bad9b1579ec7efb7e0de62e。读回器包含主控已经修正的 incomplete→exit2，launcher包含已经发表的外部SIGTERM/SIGINT归属修正。

| 新源，位于computations | Bytes | SHA256 |
|---|---:|---|
| geometry_20261115_current_C_projective_full453_physical_dn.py | 62843 | c35806666d9f0d7912ed6496e51d520421bf0d24db22972fc43d4e6e0b5d1c9b |
| geometry_20261115_current_C_projective_full453_launch.py | 19213 | 9a7602ada770fcdc2bcc1b81456459afb2448eff414453b5529c62d4df80df63 |
| root_20261115_current_C_projective_full453_scalar_readout.py | 18339 | a4b8f1f4a1cc3a0703c94f345b2b90e41525b54a031d3d47ca68fb58a3eeaea2 |

原159三源的逐字身份分别为：

- driver，62101 B / ea68a0036d096fb06785fe8f43c1c3263ef0b3baf110d7af6b2b90767bc2397b；
- 已修signal launcher，19169 B / 1feac6d53bf211de2c9bce78929d2f586e02b3a59d4ca037590e3a2a4aa33ea9；
- 已修incomplete reader，18307 B / c0aa52af6669d3226566280b40a836843645e289220ec2f0f21f535090e5f665。

完整源差异随本次小文本交付供阅读，属于可重算来源差异，不需把重复diff或static receipt入Git。

## 2. 改变的精确范围

driver的21个顶层定义中20个逐文本等于159。唯一不同定义bind_current_native仅将sampler result schema改为168实际schema。其余变化均为文件头的明确范围、SCHEMA/RECIPE_SCHEMA、两个source pin字典。

两个字典分别是PINS共51项、NATIVE_PINS共25项。相对于原159，它们都：

1. 将sampler/worker/client/native-launch/native-reader五个旧文件替换成168五个独立新文件及真实SHA；
2. 另加入R347的geometry_20261115_stored_C_finite_head_projective.py，77731 B / 5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216；
3. 保留原R3244531、C v3 f12f及其原层、R312fe667、native ownerfae2、bridge67e3、general-Robin chain9462、R2739b95、noJ引擎f9b2、R300 factory/numeric/augmented及原全部物理BVP源码。

launcher的owned-group helpers、wait/stop/finally、磁盘/时间处理均逐字保留。main仅改实际deadline schema字符串，顶层改driver basename/SHA及两个输出/recipe schema。

reader的main及所有实际读取/省略/错误逻辑逐字保留；native_readback仅说明文字改变。顶层改为168完整reader的basename/SHA与独立新schema。因此完整unit行、每个闭候选、空间叶/未付和原native trial/trace都由实际新helper读回，未退回原153只读某一count的范围。

本轮没有本地AST或数值执行。实际Actions须做原完整source hash、Python compile/AST、Node语法前置；它们不构成新的数学fixture或接受门。

## 3. 168依赖的准确身份

| 职责 | 文件 | SHA256 |
|---|---|---|
| 全C采样与有向单位far行 | geometry_20261115_current_C_projective_radial_sampling.py | b290dd6030224efc36bfeb30a53e00d76c43c924ae67a0c068e0d23d4d82d8c4 |
| 同一完整native worker | geometry_20261115_current_C_projective_native_worker.mjs | c3d5c745f34621fc4817d77377895d3534ad37967da89b2c17ee3faabd6862ed |
| 同一个live TailClient | geometry_20261115_current_C_projective_tail_client.py | 23824ecbe00d997a0268d0a1438d460f45fa4c4a9de2f05ff6467f0e6f6b5654 |
| 显式112-H入口来源 | geometry_20261115_current_C_projective_native_launch.py | ae54abbb383269cbd2fd111c08a103b7eb8a14b15db01d09c2fcc8227488bf9d |
| 完整sampler/native语义读取 | root_20261115_current_C_projective_native_scalar_readout.py | 8a3ddc5d59244b245292bd5a0e3fb33768527017148cc4e697d2f2cf771989e7 |

R347proof29f79e1f与R357proof286f17ee由实际168sampler分别核全文。R357已发布提交ca4194951a04879d154f3eee47e4b45fa6e42d55；它不依赖本次输出先通过。

实际tail-config.source_sha256必须含上述新的NATIVE_PINS全部25项，不能只替一个client文件名而仍给旧sampler/worker/schema。额外真实来源允许按原配置保留，但任何同名重复身份不得冲突。

geometry bundle仍是current-C-native-radial-geometry-bundle-v1。这个layout保持不表示producer相同。实际sampler result必须为current-C-projective-physical-radial-samples-and-general-far-v1，并且source SHA、同run/source、completed/native_geometry_ready及完整C输入全部逐原合同绑定。

## 4. 正式schema和启动参数

新driver result schema：

    current-C-projective-R300-v3-three-active-complete453-physical-DN-v1

新recipe：

    explicit-current-C-projective-R300-v3-three-active-complete453-recipe-v1

新launcher result：

    current-C-projective-R300-full453-owned-process-launch-v1

新deadline：

    request169-owned-job-science-deadline-v1

新reader：

    current-C-projective-R300-full453-complete-scalar-readback-v1

其余原current-C client config、geometry、linear snapshot/response与wire protocol保持原完整layout。没有静默接受旧sampler result schema。

launcher参数完整沿159：

    python geometry_20261115_current_C_projective_full453_launch.py
      --recipe ACTUAL_169_RECIPE
      --recipe-sha256 ACTUAL_RECIPE_SHA
      --accepted ACTUAL_ORIGINAL_ACCEPTED_FILE
      --accepted-sha256 ORIGINAL_ACCEPTED_SHA
      --complete-seed ACTUAL_COMPLETE453_FILE
      --factory-directory SAME_JOB_CURRENT_FACTORY
      --factory-result-sha256 ACTUAL_FACTORY_RESULT_SHA
      --tail-config SAME_JOB_NEW_PROJECTIVE_CLIENT_CONFIG
      --tail-config-sha256 ACTUAL_CONFIG_SHA
      --tail-source-root ACTUAL_RESTORED_SOURCE_TOPIC
      --computations ACTUAL_COMPUTATIONS
      --job-deadline ACTUAL_SAME_JOB_169_DEADLINE
      --out FRESH_EXCLUSIVE_LAUNCH_DIRECTORY

complete-seed的字节SHA、明确mesh/states JSON pointer及来源仍在recipe.complete_initial_guess内核验。它只作初猜；原全部状态/RHS、当前target、MaterialTrace和H都会实际重求。

readback参数：

    python root_20261115_current_C_projective_full453_scalar_readout.py
      --launch-directory ACTUAL_LAUNCH_DIRECTORY
      --sampler-directory SAME_JOB_PROJECTIVE_SAMPLER
      --sampler-result-sha256 ACTUAL_SAMPLER_RESULT_SHA
      --computations ACTUAL_COMPUTATIONS
      --out FRESH_SIBLING_READBACK_DIRECTORY

sampler-result-sha256在原reader中为可选参数，以便原结果缺失时仍读未启动/失败原件；已产出的实际结果应由workflow传完整SHA。读回绝不借另一个运行的几何或补造缺失文件。

## 5. 原真实H和完整求解顺序保留

最终169 recipe逐字保留159的R320九参数、lambda=.001、height_sign=-1及原完整453初猜来源。这是新的明示实验，不能称从159已接受状态续解；本文没有填任何尚未返回的159状态。六个额外标量控制固定，三个原参数仍由原完整BVP求解，初猜的旧RHS/J/metric/尾部响应不复用。

原prepare_problem完整保留：

- 同job准确factory与当前数值profile；
- 原accepted/core来源及geometry canonical SHA；
- 全部9参数，active仅0/1/2、其余6冻结；
- 原complete453初猜公共u重参数化；
- 原完整当前RHS与mesh点状态、物理边界；
- 当前material/physical angles以及原fullheight形成。

随后保持一个真实live owner：

1. 从当前profile和完整初猜端点生成原全部112物理H；
2. 对该实际H调用新client进行真native solve/J；
3. 用返回的真实cut字词做原五项比较；
4. 执行原同定义R252 FD；
5. 把同一owner一次交给原full-DN入口；
6. 每轮当前H、原inner与outer、最终audit=True均为原真实调用；
7. 最后只关闭该自有owner，失败也走原完整finally。

没有把新单位far矩阵替换进旧零响应缓存。READY也不是已算anchor。只有真实返回后SharedNativeClient才填自己的cut与响应；profile字词不覆盖它。

## 6. 全部原数学范围保持

read_recipe中的原契约逐字保留：field112、angular2048、physical338、state453、material/physical4096、maxnodes1200、outer8、原inner17、collocation1e-6、BC1e-11、FD5e-5。

bind_current_native中的原策略也逐字保留：native32、trial10、tol2e-9、eta1 correction、eta0完整112 RHS、reference_floor1、projection_floor.05、quadrature2048、steps12、每linear child1800s、factor2147483648 B。

同一原target/current C/source关系、实际cut、完整field plan/all rounding descriptors与nondividing far必要性均保留。没有由R347/R357增加新的非线性norm门或改原FD/最终物理审计。

R357改变的是数值far行表示。准确齐次边界在正比例下相同，但数值残差权重、原有限least-squares方向和浮点轨迹可能不同。本文只称原算法代码和接受条件不变，不声称与旧159每一步相同。

## 7. 准确对象与有限数值责任仍分开

新sampler先对所有准确C逆像候选给出有向单位行包围，再明确选择实际binary64代表与误差描述。单位行hull中的任意一个点未必由同一个准确全局C根族实现；这项责任保持未付。

原native实际得到的是该明确数值几何、完整root/RK/mean/Robin矩阵的有限响应/J和审计。即使原full453返回成功，也不自动支付准确C共同实现、无限DN、连续相对metric、C²接缝、全曲面embedding/reach或闭场结论。

特别地，old_R324绑定来源继续是4531，actual_R347 source另记5440；目标仍原声明C，不把单位行归一化改成另一个g或一个已证明的无限尾解。

## 8. 资源、外部中断与完整清理

§10的最终workflow已明确选择资源；源码没有为169新增call cap或改变原最大迭代。原launcher记录的18个算法入口上界是说明，不是第19次阻止科学的门。

实际sampler声明完整112射影传播14400s/25M计划，但同job还有C重建、cut、factory、deep、全部采样、完整BVP与读回。各预算之和不能冒充在一个GitHub job内一定完成。namespace的18900秒对BVP前各段是启动资源计划，不是通用绝对kill钟；sampler绑定/runtime setup仍排除在其两个内部phase时钟之外。原BVP launcher开始后，才按原代码实际执行其同namespace截止和7200秒过程上限的较早者。平台step/job硬限、实际剩余裁剪及读回预留在§10明确。

本launcher保留159实际修正的SIGTERM/SIGINT语义：子进程新session由本源实际拥有，外部信号不能令其成为失控的孤立科学组。原stdout/stderr留完整，退出/关闭/资源/外部信号分别记；未确认自有group静止时不冒完整读回或主动清理。

新reader的complete_scalar_readback依旧要求quiescence以及所有实际read errors为空。失败exit2；成功exit0。完整原trial/FD/参数/final字段和每个sampler candidate由bounded语义块输出；原大状态、RHS、J与factor只做完整身份/明确省略，不重算。

主控workflow只能在读回实际成功与原组静止后删除此次独占临时树。不得用job success、hash一个失败摘要或日志尾段代替完整读取。没有本169科学raw被预存到Git、Release或共享artifact。

## 9. 交付边界

本组三源不需要先等168零响应成功才能被审读或发表；真正运行时必须由同job实际完成的完整sampler提供输入。这个依赖是原真实来源合同，不是额外审批门。

三份科学/reader薄适配的改动范围仍为来源/schema/完整reader接线；最终workflow另含标准库资源/进程身份记录。实际发布commit与运行号在发生后另行记录，所有数学结果以该次完整原读回为准。

## 10. 最终三运行件与完整临时生命周期

| 路径 | Bytes | SHA256 |
|---|---:|---|
| computations/current-C-projective-full453-physical-DN169-recipe.json | 9940 | f8f6b353458f04052940a05bbe28d28c48b0050f631f76f813267924a31d4765 |
| computations/public-current-C-projective-full453-physical-DN-request.json | 35286 | 2db89139012a1bdb7fdc6b07ea7f46f11eb3409531de81b34f897d4f1e08561b |
| .github/workflows/visible-larger-public-current-C-projective-full453-physical-DN.yml | 86237 | e62e93d60f87c48c8005aba2b1bb2c0b900e2594832a32f6981d516a7b46559c |

源闭包为58个直接pins。相对已发表159，只替换168五源和本169三源的basename/完整SHA，再加入原R347射影源；51个driver PINS和25个NATIVE_PINS均与实际冻结源码逐键相符。原科学参数、原三C输入、两闭query、R312深端、两份构造/453初猜来源、原147 atomic construction字典和R300/R323公式均逐JSON值保持。完整unified diffs是临时可重算审读材料，不作为新增raw入库。

原九参数是

    [0.3055213835477326, 0.21645013203050154, 0.34270051957744246,
     -0.06322334619266512, -0.01747451701873286, 0.9376115689625685,
     1.0751306255033548, 0.6886900390922872, 0.9385431607625546]

其来源是recipe中原146 run43716274591/source69765fcd81ca84819cdeb09c4fe14c55fdb5fb80的literal final九系数；不是从159结果取值。完整初猜依旧是原历史prepare112的699个node、每node453状态，文件SHA0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714，mesh/states指针分别为/mesh与/states。它们被重参数化到当前public u；没有从旧文件借任何fresh科学读数。

### 10.1 启动与资源

独占临时根为 RUNNER_TEMP/visible-current-C-projective-full453169。嵌入标准库helper request169_owned_process.py 是12476B/SHA a2af90fceba09ed8d061b781151afab9bcb156cad3c4c23fb0b91b2d6d035e34。它不import数学；只绑定同job/request/recipe、保存原与实际argv、按实际启动时点分配资源、记录PID/start_ticks及科学独占session。

原规则runner3b8b6dd5保持2700秒周期和真实pull/README变更停止。GitHub token只给规则父进程；科学子进程移除GH_TOKEN/GITHUB_TOKEN/MR_TOKEN。每个原C、construction、deep、sampling、BVP步骤均只通过原runner实际建立的独占科学session启动，不在--command后插入多余裸--。

namespace建立时声明18900秒科学计划和2700秒读回余量，job硬上限360分钟。原C3600秒/75分钟step、两次construction domain300秒/20分钟step、deep5分钟step、cut10分钟读回均不改。

sampling声明linear14400秒、point1800秒、25M工作尝试、原depth32/.5norm/12defect/24Taylor、2GiB动态reserve。实际规则startup结束后观察remaining，先预留原BVP7200秒，给两sampling phase共同乘上

    min(1, max(0, remaining - 7200) / (14400 + 1800))

这个比例仅是资源裁剪，不改变方程、完整112范围、误差门、逆像覆盖、原native验收或任意数值阈值。实际原argv、比例和两个有效预算全部存receipt；若无正余量则未启动并记partial。sampling的285分钟step和job360分钟仍是实际外层硬限；setup不纳入内部clock的事实不会被这个计划掩盖。

BVP不修改原recipe。它进入原launcher后，以7200秒和实际namespace剩余时间的较小值作为自有完整过程预算；原SIGTERM/SIGINT转发、TERM/KILL/join与外部中断记录保持。即使已过deadline，仍允许原launcher写出其原始未启动/资源scope；不是由新helper伪造一个数学拒绝。BVP step135分钟。原每linear child1800秒继续与采样linear14400秒明确分开。

初始32GiB可用盘和动态2GiB reserve只是资源要求，没有全流程必完成承诺。18个原算法入口是源级上界说明，不是第19次阻止调用的新增门。全部32/10/17/8和原容差保留。

### 10.2 原读取与marker

C、cut、construction、deep、BVP/native、rules六个实际读回步骤全部保留。最后阶段C/deep/rules各5分钟、BVP完整语义30分钟合计45分钟仅为资源预留；前段cut/construction已有各自原读回。单job若遇平台中断，不宣称这个预留必然兑现。

BVP读回前先观察全部已登记规则父PID/start_ticks及科学独占PGID。父可能继承runner公共group，因此只核父PID原start_ticks，不要求公共组为空。独立BVP子组还必须有同run/source的原launcher quiescence结果。活流或未知身份会输出未付范围、阻止主动清理，不能以hash可变流冒完整读回。

原新169 reader exit0且scalar-summary明确complete_scalar_readback_without_recorded_read_error=true、owned_group_quiescent_before_readback=true后，workflow才写同run/source的readback-complete.json，绑定实际reader和原summary字节SHA。这是读取完成marker，不是BVP接受。原summary超过单块界时走既有-index-split协议，完整成员仍在stdout；不拼大对象或截trial。

规则读回保全部rule-sync、owned-rule-sync-processes、实际deadline、原recipe、当前native config和dispatch元数据。原mirror在out树之外，不递归打印clone或凭据。规则helper解析失败返回非零，成功才写同job rule-readback-complete.json。

cleanup同时要求六个读回步骤success、两个marker同run/source、原owner再次确认为静止、独立BVP组的原quiescence结果。否则明确保raw直到runner销毁，不主动删除未读输出。只删除自有namespace，包含本次恢复的自有输入副本；不触原repo、外部input或别人的进程。

### 10.3 已完成的源级核与未发生的结果

本次实际完成了完整文本构造/差异、字节SHA、58/51/25来源字典逐项比较，以及19个run块、18个Python heredoc的文本闭合核。终端仍不可用，没有本地AST、bash-n、Node或科学运行。工作流在任何science前对58源执行实际Python compile/AST及Node --check，对本工作流的所有Bash块和Python heredoc做真实syntax前置，并核嵌入helper。它们不是额外数值fixture。

截至冻结时，没有169实际source commit/run/result/J/H/BVP接受；不得从168/159的job状态或源可执行性代填。准确C全局代表实现、无限DN、同g450、完整闭场metric/C²/embedding/reach仍沿原责任，不由本次有限BVP结果自动支付。
