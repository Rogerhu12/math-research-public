# Request159：真实 current-C / R300-v3 标量的完整453物理 DN 接线

作者：AI  
日期：2026-11-15  
状态：独立源码与明确新实验配方。本文不报告尚未运行的 Request159 科学结果。

## 1. 本次实际要做什么

本入口把当前作业真正重建的 R300-v3 九控制标量与当前作业真正生成的 C 几何采样、112 条非除式远端边界行接到原完整物理 BVP。第一条物理高度由本次完整453初猜的端点、当前 RHS 和原 MaterialTrace 形成；其实际非线性尾响应和全部 J 返回后，执行原 R252 边界 FD，再使用同一个仍存活的 client 执行原 full-DN 的外迭代、完整 BVP 和最终 fresh audit。

这是显式新实验：$\lambda=0.001$，起始九参数使用原 R320 / Request146 字面末值；第4至9个形状系数冻结，第1至3个参数由原方程求解。原699节点准备件只提供338个物理值、112个完整 core 值和三参数槽位的初猜。它既不是新目标的已接受场，也不是当前 C 的非零响应。

[新 driver](../computations/geometry_20261115_current_C_full453_physical_dn.py) 不调用旧 family.setup 或旧 CircleReference，不读取旧零高度 anchor/J，不把旧标量、旧尾 graph/gains 或旧接受标志用于新问题。保留旧 small-core family 模块是为了完整源码闭包及原 accepted96 源身份；旧数值求解器正文和原物理边界函数保持冻结。

本接线建立的是完整有限数值问题。准确 R300 目标、其数值编译器、由区间代表值形成的有限 current-C 尾、精确连续 C 尾及最终闭场仍分别记录。有限求解成功不能自动支付这些对象之间的误差。

## 2. 冻结运行件及来源范围

| 文件 | 原字节数 | SHA-256 |
|---|---:|---|
| geometry_20261115_current_C_full453_physical_dn.py | 62101 | ea68a0036d096fb06785fe8f43c1c3263ef0b3baf110d7af6b2b90767bc2397b |
| geometry_20261115_current_C_full453_launch.py | 19169 | 1feac6d53bf211de2c9bce78929d2f586e02b3a59d4ca037590e3a2a4aa33ea9 |
| root_20261115_current_C_full453_scalar_readout.py | 18307 | c0aa52af6669d3226566280b40a836843645e289220ec2f0f21f535090e5f665 |
| current-C-full453-physical-DN159-recipe.json | 9160 | 950c61771b9af555f0ea60826c6b3c8a91758068f271a321304ce23d6c09915c |
| public-current-C-full453-physical-DN-request.json | 31594 | c75cda0ca309d29a37faa1f8ea3e4f9bc8df128ab01c3b64549cf94013c71d0b |
| visible-larger-public-current-C-full453-physical-DN.yml | 58403 | 8e3349181590b7d3ad0d98cb09b812b11ea63e8fb7a1d0d32a6bb8cdaca341f8 |

前三文件和 recipe/request 位于 computations；工作流位于根 .github/workflows。request 保留57个直接文件的完整 SHA 表；各原模块的完整依赖闭包仍由其原 checked_sources / FROZEN_SOURCES 在实际入口逐文件检查。57是直接派发 pin 数，不冒整个传递依赖闭包的文件总数。

关键现有对象：

| 责任 | 原冻结文件 / SHA |
|---|---|
| C 的准确连续约定 | geometry_20261115_stored_continuous_E_cover_v3.py / f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df |
| 深端全112图 | geometry_20261115_stored_continuous_C_far_graph.py / fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a |
| 受证双坐标传播核 | geometry_20261115_stored_C_finite_head_flux.py / 4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d |
| 原147明确 R323 构造 | geometry_20261115_continuous_nine_v3_actual_construction.py / 738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0 |
| 准确九控制 factory v3 | geometry_20261115_continuous_nine_scalar_factory_v3.py / 0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e |
| 九控制数值 profile v3 | geometry_20261115_continuous_nine_scalar_numeric_v3.py / 7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60 |
| 当前完整物理 RHS 适配 | geometry_20261115_continuous_nine_augmented_v3.py / d86f6fdf3cf59df3d45c907c655fe54ab830180facd27b7402e649b2e14d151b |
| 当前 profile/BVP 同源 binder | geometry_20261115_continuous_C_full112_binding.py / c0bda3350b30b9659c326112eaf8f411d0bb6f825a7a3f81fcc6c7502ed3f952 |
| 实际物理半径与远端行 sampler | geometry_20261115_current_C_radial_sampling.py / 1dec587d72d4c9c9805fd090951df49d751755a4334645d2f410d18c2287e812 |
| 完整非线性 owner | geometry_20261115_current_C_general_robin_native.mjs / fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349 |
| 同步线性桥 | geometry_20261115_current_C_synchronous_linear_bridge.mjs / 67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286 |
| general-Robin QR / 全112 RHS | exact_20261115_current_C_general_robin_chain.py / 946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5 |
| 当前 live client | geometry_20261115_current_C_tail_client.py / 8c7bd23a2eb3be5d4b739483973912b273ca3f2282fc52b312e1c4bdf53c5616 |
| 冻结完整原生 scalar reader | root_20261115_current_C_native_scalar_readout.py / 2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff |
| 原 complete full-DN main | geometry_20261114_full_dn_solve.py / c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 |
| 原 complete band 后端 | geometry_20261114_lifted_modes_banded_full_dn.py / 390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4 |
| 原物理角边界 | geometry_20261114_physical_test_boundary.py / 3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681 |

完整 prior implementation 来源还包括独立九控制 full112 的 00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8。其实际 target 及 tail 被本入口明确替换；它原接口中仅属于旧 finite 标量/旧 anchor 的标签不继承。

## 3. 五个历史原件与具体初猜证据

所有历史数据只在本次 Actions 临时目录恢复一次，原字节从普通历史提交 8bd267107cc8710d371f3b62c02986655ac965b0 读取。当前 main 不重新存这些可重算数据，不创建 artifact 或 Release。

| 角色 | 原路径（topic 内） | 字节数 | SHA-256 |
|---|---|---:|---|
| 原完整物理配置 | notes/public-actions-43588155190-1-prepare112/T112-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| 原 calibration ready | notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| 原 stored ready | notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |
| accepted96 core 来源 | notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| 全453初猜 | notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |

最后一件的 Git blob 是 d3aadef529d767c8facc26c399f458e903014512。源侧只读已付的小 driver-status.json 和 publication.json，并未通过 connector 读取其4.2MB payload。该原小状态 77991 B / 6ddba15ee29868bf8ed26bde840aec7eb9ab210869163092b7733d5257d072c6，明确写入：

- run43588155190、source5870c8dd4bfbd12009df1328cc1a63812f183c1d；
- producer geometry_20261114_lifted_modes_prepare.py / 9a1ae018d71e38ff901c4b9156b23502a4efde44f812c1ff4e03323878b659db；
- nodes699、state_dimension453、left_rows341、right_rows112；
- prepared SHA 为上表原值；
- new_coupled_finite_acceptance=false。

原 producer 的 prepared 构造直接写入 /mesh、/states、/rhs。其布局是 $3M+2=338$ 个物理行、$M=112$ 个 core 常数行、3个标量常数行。因此 recipe 的 /mesh 与 /states 来自原代码和原 metadata，不是猜测字段。实际 Actions 恢复后再核原 SHA、M112/N2048、699行及每行453列。

binder 读取全部原字面值，只把原网格按公共 $u=s/L$ 映到本次 profile 的实际数值长度；保留物理338及 core112 初猜，三参数槽明确替为 recipe 的前3值。原 /rhs、原 g、原 port 和原成功标签不传给当前求解。当前 RHS 在整个初猜上重新计算，随后原 preflight、节点/中点及 RMS 域责任照旧执行。由旧 JSON 序列化没有保存的负零不冒充已经恢复；本次实际 H 和 native 状态的有符号零另由真实 raw 字词及 sidecar 保留。

accepted96 的 /fixed_scalar_profile/geometry 是当前 R323 core 的真实来源，core_end 沿原 actual accepted.mesh[-1]。入口同时比较 factory 的原 core 文件 SHA 和选中 geometry canonical SHA。accepted96 原有限接受只作为原输入合法身份；它不能推出 current-C 或新 R300 目标的接受。

## 4. 明确新实验：九参数、低 core 目标和状态维数

参数顺序固定为

$$
(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3).
$$

本次原 recipe 字面九值为：

~~~json
[0.3055213835477326,0.21645013203050154,0.34270051957744246,-0.06322334619266512,-0.01747451701873286,0.9376115689625685,1.0751306255033548,0.6886900390922872,0.9385431607625546]
~~~

其来源是 Request146 / R320，run43716274591、source69765fcd81ca84819cdeb09c4fe14c55fdb5fb80；原 status SHA252a9ceabf63305cdab40312b104e397acb7a8deb52ea513d4ecc038104d80e5，原 primary SHA befc5446223c3f45bc96f4d53aeae6e0115f2fe3214051bc4219f2465fefe1e9。只使用这九个字面参数，不使用该旧候选的场、W、J、残差或 radius。Request151 已固定原相同 R323 构造，本工作流消费其原147 atomic request 全字节 17398 B / 4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707，不重写其数学 policy。

令 $c^{96}_{1:3}$ 为上表 accepted96 实际 core 的前三项。本次物理 inlet 目标明确取

$$
c^{\rm target}_{1:3}=0.001\,c^{96}_{1:3}.
$$

其余109个 core 未冻结为旧值；它们仍是原完整 BVP 的自由常数未知量。$\lambda$ 是这次新实验的明确选择，不是声称在已接受的同一 $g$ 上精化。第4至9标量系数在本次453系统冻结，前三标量参数仍由原方程求解；输出需要记录全部9个最终参数。全部9个都冻结的450维同 $g$ 精化没有由本入口提供。

状态布局、各原有限角规则和门：

| 内容 | 原值 |
|---|---:|
| field modes / native modes | 112 / 112 |
| 物理行 / core 行 / active scalar 行 | 338 / 112 / 3 |
| 总维数 / 左右边界行 | 453 / 341+112 |
| 物理 RHS 角求积 | 2048 |
| MaterialTrace / physical boundary 角数 | 4096 / 4096 |
| inner 原试步 / outer 原上限 | 17 / 8 |
| 原最大 mesh 节点 | 1200 |
| collocation 与最终 frozen physical RMS | $10^{-6}$ |
| 原边界容差 | $10^{-11}$ |
| 原 FD 阈值 | $5\cdot10^{-5}$ |
| 原 height / radial 取向 | $-1$ / $-1$ |

没有补充 interval-domain、线性残差、rank、K/D、metric、jet 或新的阈值来替代这些原有限接受规则。实际 binder 的源/维数/同对象检查仍是必要输入合同，不被解释为新的几何定理。

## 5. 同一个 C 对象、数值代表以及有限远端

同作业先执行原 f12f v3：160×9=1440有限片、全部六 primitive、原两个闭 query、精度256、integral_abs96 / relative80、max_panels200000、max_query_nodes200000，实际 C wall budget3600。相对原147的1800，只是明确上游资源扩大；目标 C、原精度、全部分支和全部未付范围不变。第一 query 是配置原 binary64 rCut 的点；第二仍是整个原自然闭域，不重归一切口。

R323 构造完整保留原两遍300秒 domain pass 和初始九值。初始九域未通过或未付不被本入口改成新 BVP 接受门。factory 必须确实产生其完整当前定义、数值编译和对应身份，绝不能由过去已打印的147数值构造假 result。R323 有限严格 cut 盒的选窗条件保持原源。

深端程序依 [R312](../results/R312-continuous-C-complete112-zero-tail-and-head-connection.md) 保全部112模态；sampler 使用 [R324](../results/R324-continuous-C-finite-head-flux-and-closed-tube.md) 原核，把完整双坐标端列传到其明示选择的实际物理 rFar。该点严格越过整个 node8 半径盒，且严格小于原 cut。所有可能反像片、端点、closed tubes 和误差均由原 sampler 保留。原148/156把列继续传到 rCut 的状态和预算不能代替这一有限 rFar 责任。

新 binder 核 current factory 的 complete_C_binding 与 sampler 的 original_C_input_binding，比较时只按原 original_C_core 排除 query/runtime/work 参数。实际 work 参数本身仍完整记录。进一步要求二者同一个实际 cover result SHA、同一个原 binary cut、有同一 run/source 的实际新结果。这消除错接历史结果，但不把一组数值区间中点自动证明为同一个精确全局 C 根族成员。

sampler 的 general Robin 行使用完整112×224矩阵，cut 端不先除某个 height column。所有 core 内点也不调用旧 node graph/gains。固定原153的 native coordinate/positive scale rule照旧，reference_floor=1；不声称等价于旧有限模型的 sigma 量纲或范数。R324 全 cut column 中 height 盒包含0不是本入口的 gate，也不是共振结论。

## 6. 从当前场产生 H，并保持同一 live owner

第一条 H 在当前453初猜完成原 full preflight 后才计算：

$$
H=\varepsilon_h\,P(c)\,z_{\ne0},\qquad \varepsilon_h=-1.
$$

这里 $P(c)$ 是原 MaterialTrace 的完整物理到材料角变换，输入包含实际端点和其当前 RHS，保留所有112模态及 mean 责任。没有从配置、旧 anchor 或 recipe 填入 H 值。

第一条 actual solve 请求完整 H、jacobian=true、audit=false。它执行当前 C 本身的有限 root/RK 全576 stage；原非线性32次/10个 noJ 试步/严格原norm/2e−9保持，R331 的 $\eta=1$ 只用于非线性 correction。响应的全112 RHS敏感度用 $\eta=0$ 完整方阵和原112个入口方向形成，返回完整338×112的 endpoint jet derivative；两 mean 行没有被丢弃。

[原 R331 证明](../results/R331-current-C-zero-seed-general-Robin-and-complete-sensitivity.md) 中阶段 $-I$ 消元和整个边界方阵可逆性是不同问题。浮点 QR pivots、数值小残差或该调用的有限接受不构成严格无限非共振证书。rank/求值/域异常保原现场，不替换为旧 J。

SharedNativeClient 只在真实成功响应后把五个 actual cut 字段写入自己的 wrapper metadata：radius、E、Ep、backgroundSlope、backgroundSecond。READY原本只有前三项，不补造另两项。完整 checkpoint H 加实际负零 sidecar 恢复后逐字核到本次 H；source、call 和完整响应 canonical SHA 另记。后继响应必须保持相同 native 背景字词。

随后保原五项 profile/native 比较：rtol2e−11、atol2e−13。profile 使用其自身已编译值，backgroundSlope/Second 仅由自身 E0/E1 的原式形成；绝不拿 native 结果覆盖 profile。即使两侧来自同一准确 C 数据，不同数值代表的这些比较也仍可能失败。失败如实记录，不能通过改目标字段消失。

同 worker 保持到最后 audit；没有先关闭再用 checkpoint 或历史缓存冒同一 owner。native client 自身允许的同 H、非 audit 当前缓存只来自该 live 进程真正完成的响应；audit=true 强制真实 fresh call。

## 7. 原 FD 与原 complete physical-DN main 的保留

第一条真实 H/J 形成后，才构造该点的明确 affine map，用于原边界实现 FD。原三个扰动保持逐式：

- yb[iz+1] 加 $10^{-5}$；
- yb[iz+32] 加 $10^{-9}$；
- yb[iz+M] 加 $10^{-10}$。

原 make_directions、direct 与 separated 两组、两级 fourth-order Richardson、second-order contraction 和 $5\cdot10^{-5}$ 门不改。FD 测试的是当前真实 H/J 附近的原物理边界实现，不声称每个 FD 扰动都重解非线性尾，也不把旧零高度 J 当本点 J。

边界本身仍是原 R252 physical-angle test：

$$
R_\phi=Z_{\ne0}f-\gamma\,S(c)\,D_{\rm num}(H),\qquad
\gamma=\varepsilon_h\varepsilon_r/\sqrt{E_{\rm profile}(r_{\rm cut})}.
$$

完整 $P,S$、core 列、scalar 列、mean 与 physical RHS 都保留；没有逆矩阵截断或 principal block 替代。原 material-test 与 finite physical-test 不等价的责任仍由原报告表示。

原 complete band/main 正文保持冻结。独立 wrapper 只注入本次实际 profile、实际完整 flow、明确 lambda 目标、完整初猜、同一个 load_client owner 和诚实来源记录。原17个 inner 试步、原8个 outer、原全 BVP/RMS/BC、真实 tail 重新线性化、最终 frozen physical RMS 以及 audit=true 的新鲜实际响应均保留。全局替换在 finally 中还原。

原 core 构造接口需要 config 中 modes=112、spacing=2。原153 config 没有这两个 metadata；本入口创建独立副本，仅加这两项及来源说明，不修改原153 config或数学源。原 current-profile port 也用当前身份生成，不引用旧非零响应。最终 accepted 文档明确写新 target 和数值 shadow；旧 metric identity 仅保为原来源，不能冒同 $g$。

源路径最多有第一条 FD anchor、每8个 outer 各最多两个 solve 入口、最后一次 fresh audit，故入口数的路径上界是18。这是说明资源可能的数量级，没有在代码里加18-call截断。实际 native 调用数和可能的同 H cache 必须从真实返回记录读取。

## 8. 可直接调用的 CLI

所有实际科学调用必须在本公开仓库 Actions 中。source guard 同时检查 GITHUB_ACTIONS 与 GITHUB_REPOSITORY。

完整 BVP driver：

~~~text
python -u geometry_20261115_current_C_full453_physical_dn.py
  --recipe ACTUAL_RECIPE
  --recipe-sha256 ACTUAL_RECIPE_SHA
  --accepted ORIGINAL_ACCEPTED
  --accepted-sha256 b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff
  --complete-seed ORIGINAL_PREPARED453
  --factory-directory ACTUAL_SAME_JOB_FACTORY
  --factory-result-sha256 ACTUAL_FACTORY_RESULT_SHA
  --tail-config ACTUAL_SAME_JOB_CURRENT_CONFIG
  --tail-config-sha256 ACTUAL_CONFIG_SHA
  --tail-source-root RESTORED_ORIGINAL_SOURCE_TOPIC
  --tail-client geometry_20261115_current_C_tail_client.py
  --jac-workers 2 --node-heap 6144
  --out FRESH_DRIVER_OUT --work FRESH_BAND_WORK
~~~

实际工作流从全局资源 launcher 调用上面入口。launcher 还需要 --computations、--job-deadline、--out，外部 --out 是独占 BVP-launch 根；内部 driver 输出为 full-BVP，band factor 在 banded-work。其余实际原输入/结果 SHA 与上面相同。job-deadline 是 namespace 建立时产生的小 metadata，绑定本 recipe SHA、run/source、真实起时和315分钟 science 窗口；它不是未来 scientific result。

读回器：

~~~text
python -u root_20261115_current_C_full453_scalar_readout.py
  --launch-directory ACTUAL_BVP_LAUNCH
  --sampler-directory ACTUAL_CURRENT_GEOMETRY
  --sampler-result-sha256 ACTUAL_GEOMETRY_RESULT_SHA
  --computations ACTUAL_COMPUTATIONS
  --out FRESH_SCALAR_READBACK_SIBLING
~~~

所有实际结果 SHA 在同作业原文件存在之后现算。没有预填 sampler、factory、H、J、BVP或future run的 SHA。

## 9. 资源、进程和失败语义

工作流原 namespace 名为 visible-current-C-full453159；compute 使用360分钟 job 上限。namespace 起时建立18900秒 science deadline，给最后读回/清理保留2700秒。BVP进程另有7200秒 wall预算，实际预算为它与 science deadline 剩余时间的最小值。这个 budget 覆盖第一 H/FD/fullDN/fresh audit 整条活进程，不是每次 call 的重复预算。

主要分阶段资源：

| 阶段 | 资源 |
|---|---|
| f12f C 重建 | 3600秒 source budget；step75分钟 |
| cut 两jet原读回 | step10分钟 |
| 原 R323 / factory / 两域 pass | step20分钟；原每pass300秒 |
| 原完整112 deep | step5分钟 |
| sampler | linear1800秒、sampling1800秒；step70分钟 |
| full BVP live过程 | 实际不超过7200秒及job science剩余；step135分钟 |
| 全 BVP/native/linear读回 | step30分钟 |
| 原 C/far/construction/rules 读回 | always，随后独占清理 |

这些是资源限制，不修改原迭代次数、每次 trial 列表或原数学容差。没有承诺任何18-call路径一定能在360分钟内完成。

预检32GiB可用空间，live过程每5秒检查2GiB reserve。32GiB不被声称覆盖18个请求、每请求32个完整 snapshot/factor/ledger；耗尽 reserve 记录独立 storage resource stop。没有流式丢弃未读因子来制造完成。

科学 child shell=false、独立 process group；其 Node worker 和同步 Python QR 默认继承该组。父进程剥除 GH_TOKEN/GITHUB_TOKEN/MR_TOKEN。规则同步 token 只在外层 runner，原2700秒实际 pull/README 变更处理保留。

正常退出或资源中断后，launcher 检查该独占 Linux process group 的活进程；先 TERM、必要时 KILL，忽略已不能写出的 zombie。只有实际观察 quiescent 才可声明完整读回/允许删除。main退出0而还有未确认退出的后代，不被记录为完整 finite BVP 接受。race 的 ProcessLookupError只表示同一组已消失；不会扩大发信号到其它组。

外部 SIGTERM/SIGINT 由 launcher 明确捕获并转发给自己创建的独立 BVP 进程组。信号处理仅记录而不在 Popen/赋值窗口抛异常；循环和 finally 完成自有组停止、确认及现场写回。原规则父进程15秒后可升级终止，因此外部中断路径用2秒TERM、2秒KILL及1秒wait，原正常30/10/5秒清理保持。外部中断单列 external_interruption，退出128+signal，不说成数学或墙钟拒绝；大日志完整SHA由原reader读出，不延误停止。

BVP source自身的失败、node/guard/line-search失败、语法或 I/O 失败、原域未付、wall deadline、disk reserve 与 reader错误分别记录。缺少某个 actual result 不用零、旧值或声称收敛来补齐。缺 owned根按本launcher“先建根再Popen”的实际源码合同说明本次BVP未启动；存在却缺解析完整 result 的根不推 quiescence。

## 10. 完整原读回、90KB分段与清理

独立 reader 只导入冻结153的标准库 reader。无科学库、求值器、RHS、积分、FD、QR 或 Arb 计算。它完成：

- 全部实际 BVP status、FD各方向/层级、preflight/inner trial/outer/audit原值；
- 全部原 native-trace / native-trials JSONL，逐原行输出，不受最终JSON是否完整影响；
- 全部原 Python/Node/linear stdout及stderr，不只末尾或首异常 hash；
- 坏JSON/坏行的完整原字节，以及即便语法有效但没有LF的最后一行原字节；
- 所有真实 current native calls、各 correction/sensitivity 子进程的原范围、各 RHS 最大残差、完整 manifest/descriptors、所有存在的原数组/factor/ledger文件流式 SHA；
- sampler 真正112条 general far rows 的原区间、代表值及误差小行，仍逐行输出；
- 全部自有文件身份与明确被省略的大可重算成员的 canonical SHA/长度索引。

一个语义块大于90000B时，冻结 reader 的 emit 按原 JSON 容器/成员递归分段；单个很长标量按其完整 canonical JSON 的12000B字节片段输出。不截 trial 列表，不把超限原块只替为一个 hash。日志使用 UTF-8 surrogateescape，原 byte offset、bytes、SHA 和恢复编码规则都记录。

有效大 states/RHS/mesh/J/factor 数组及重复完整 compiler/input 树不进入stdout；完整原文件/成员被读取并哈希，其省略 scope逐项列出。它们不是丢失的失败说明，也不被用来在读回器里重新推 norm、H 或接受。所有原 scalar 和完整 trial list 保留。

主 summary 超90KB时，其完整 index 也按同一语义协议进入compute日志，GITHUB_OUTPUT只保短索引；report不会拼回一个超大8-call或18-call块。主索引明确只涵盖此前各原输出块，避免不可能的自引用SHA。读错、owner未退出或原JSON不完整时，对应“完整 scalar已保存”标志保持 false，不冒完整证据。

五个主 report分别保 C、cut、far、construction、BVP原摘要；全部详细段在本次原compute日志。report只校原bytes/SHA并重印，不运行数学；其success不是BVP接受结论。

清理在全部always读回之后，只删这个159 namespace及其内部原source/input副本。检查确切basename、RUNNER_TEMP归属、无symlink以及实际 quiescence。任何完整读回步骤失败或进程未确认退出，则不主动删自有现场，保持到runner销毁；不上传raw，也不删除仓库或其它任务文件。 完整BVP reader以自己的 complete_scalar_readback 标志决定0或2退出，规则receipt reader遇原读错亦非零；因此读取错误不会被步骤绿色掩盖而误触清理。这是原数据生命周期责任，不重判科学接受。原Git历史输入仍可按固定ref/SHA恢复。

## 11. 与既有结果的边界

R339 的全cut双坐标传播尚未付完整112非零分母；159没有把它改成已付，也没有把包含0说成共振。159的非除式远端行只需付原sampler到明确rFar的完整当前责任。R331只证明阶段/线性结构，真正 finite QR与实际 nonlinear domain仍需这次运行。

原147和151的准确新标量/公共u目标结果不自动证明对应数值profile全C²、相对metric达到$10^{-6}$或生成了closed field。原 sampled cut 是当前数值provider的真实数据，严格同准确 C 的一体误差仍未付。完整物理有限接受后仍需原同新 $g$ 精化、准确field误差、两jet/atlas、metric、闭场、held、reach与全phase责任。

本次既没有用旧zeroJ包装newC，也没有用一个完整338×112有限敏感度宣称无限DN。外层 actual full-DN 不能由只有第一条native响应、FD通过、worker退出0或report成功替代。

## 12. 发布及源码检查范围

唯一触发为 computations/public-current-C-full453-physical-DN-request.json 的main push，工作流名 visible-larger-public-current-C-full453-physical-DN.yml，独立concurrency且不取消已运行任务。原147/151/153工作流、原科学源码和已有请求均不改。

当前根README blob21bd547f56590b7f2dd279d0297efb289a9b2783、题README bff8aea253a9e6a7a4fac28d810ac454c5499fec；每个有规则父进程的实际阶段绑定该版并保原实时同步。正文未把API读当前source称作本地git pull。

本轮仅源码文本、已存在小metadata和SHA核对；终端探测返回无可用环境，故不填写新本地 AST、Node、bash-n 或科学执行结果。实际 Actions 的57源码 pin/AST/Node检查明确列在科学步骤之前。仅小文本blob用于交付，root独占Git refs和派发；临时完整diff仅便于主控读修改，非额外验收门，也不提交可重算static receipt。

实现已完整给出。它的下一有意义证据就是本次实际同job C/factory/sampler/current-H/FD/full-BVP/fresh-audit的原返回及完整partial scope，而不是再添加一套合成fixture或先把未来数值写进文档。
