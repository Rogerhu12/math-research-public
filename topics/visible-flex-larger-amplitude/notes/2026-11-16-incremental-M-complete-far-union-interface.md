# R462 独立旧112／新增M远端族联合：完整来源与调用接口

作者：geometry agent（AI）。日期：2026-11-16。

## 1. 已交付范围

本包交付三个独立可执行源码与完整条件证明。它从同一 job 中真实完成的原112采样结果保留全部旧远端行族、数值行、误差与实际物理 far／μ 字；另读同一准确 C 的完整新 M deep 结果，仅对新增物理频率执行真实有限头传播。之后形成完整新 M 矩阵和新网格样本，可由独立新 client／worker 调用原完整 M native 数学。

**未执行，没有实际新 M、父点、行、时间收益、native 返回或 BVP 接受。** 本包不修改已刊 R450、R456、R442、R457，也不替 request207 首版改方法。当前原 M driver／owned launcher 尚未注册本包 tuple；`configure` 明记这一缺口。完整 driver、checkpoint、外层进程生命周期与几何来源注册须由后继独立版本完成，不能将本包存在写成全链已跑。

数学证明为 [R462](../results/R462-same-C-old-mode-far-families-and-new-mode-propagation.md)。同准确 C、同物理频率、同 far 字、同 μ 字下，单模态方程和取向行不依赖系统保留的其它模态数，因此旧全族包含／误差可原样保留。旧 Π 列必须移到新 M 偏移；新增模态必须真算。本结论不把数值行族中的任意向量认作同一个准确 C 成员，也不认证无限非线性 DN。

## 2. 本包文件与冻结身份

| 发布路径（题目录下） | bytes | SHA-256 |
|---|---:|---|
| `computations/geometry_20261116_current_C_incremental_M_far_union.py` | 52848 | `5da13c5f94c59be9f002f906a373d5320ed64d0ac0254af1746a1e5c8ce13c46` |
| `computations/geometry_20261116_current_C_incremental_M_native_worker.mjs` | 18663 | `b536850a32fb8c26f7bc7a06483a4d3823662ea2fd2a9235e77dbdca069b6b08` |
| `computations/geometry_20261116_current_C_incremental_M_tail_client.py` | 23746 | `d9db5098b8dbf8ebabb83fb25c060faaa0acf28dd9075654b550bdf07ac5a710` |
| `results/R462-same-C-old-mode-far-families-and-new-mode-propagation.md` | 19065 | `6d6e0875600c14440aaac1c081704d30e6fa39d4e92d285ed788bff43dd94079` |

本接口自身身份在交付 manifest 中。`publication-files.json` 和两个来源薄层的完整 `.diff` 是暂存交付文件，不加入题目录重复保存无改动依赖。联合 sampler 是新独立文件；worker/client 的差异仅来源名、schema、说明，不改原完整 M native、响应、QR、两 mean 或原接受算法。

本地仅进行了源码文本读写、原 callee 对照与 bytes/SHA/diff；没有 import、AST、compile、fixture、科学算术或程序测试。不能把未执行写成运行已验证。

## 3. 实际依赖，不复制旧数学核

### 3.1 两个主要复用入口

| 文件 | SHA-256 | 使用范围 |
|---|---|---|
| `geometry_20261116_current_C_same_far_registered_resampling.py` | `5f14be90b0e5ae36ee624ece930d46fa1205eee0efcc6e2a97decca15e7011d5` | R456 的旧112来源、完整字节流、old binding、原绝对钟、临时路径与元数据函数 |
| `geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py` | `9a85d7d17796ea567cdcfdac567ee531fcf5c225bfe9f57699bbb403aead41c1` | 原完整 M runtime、单模式 `point_column`、`finite_point_required`、`InverseSampler`、真实 `radial_grid`、raw arrays |
| `geometry_20261116_stored_C_finite_M_head_pruefer_positive.py` | `82a3f3e28e506320f474c64fd50d9ceadf3b39e9de9dc07f70c3df3c5c66bde6` | 由原 M sampler 实际加载；完整全 M／C／cut／deep binding、准确比较推进 |
| `geometry_20261116_stored_continuous_C_M_far_graph.py` | `5f16872e6e2e71914a73345b2f9b9142dbb0a7438e68805033a3277d3eb3d528` | 新全 M deep 结果的真实 producer；不由 union sampler 重新实现 |
| `geometry_20261115_pruefer_joint_row_representative.py` | `24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97` | 仅为真实新频率调用原 `form`；不重选旧行 |

原112只接两种真实来源，必须由 `--original-family` 明确选择：

| family | 原 sampler | SHA-256 |
|---|---|---|
| `positive` | `geometry_20261115_current_C_pruefer_positive_radial_sampling.py` | `965c277c5aad5a3b5c8c817600d4c435186d9ce1b267b0b59f6e7a8fa69de390` |
| `joint` | `geometry_20261115_current_C_pruefer_joint_radial_sampling.py` | `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4` |

两者的原112传播核为 `geometry_20261115_stored_C_finite_head_pruefer_positive.py`／`c2f515aa276890da63871fe0e9e1440775950d4985465457e9d6025976d914c8`，原112 deep 为 `geometry_20261115_stored_continuous_C_far_graph.py`／`fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a`。`bind_old` 按其真实旧 data 调原 R456 `bind_original_far`；不能拿新 M binding 替入原等式。

### 3.2 原准确 C、传播与证明依赖

原 loaders 逐一核下列完整文件；本包不绕开它们：

| 文件 | SHA-256 |
|---|---|
| `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_stored_continuous_E_cover_v2.py` | `004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea` |
| `geometry_20261115_stored_continuous_E_cover.py` | `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed` |
| `geometry_20261115_stored_C_finite_head_flux.py` | `4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d` |
| `geometry_20261115_stored_C_finite_head_projective.py` | `5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216` |
| `geometry_20261115_stored_C_finite_head_riccati.py` | `34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124` |
| `geometry_20261115_stored_C_finite_head_pruefer.py` | `250474d748842d9b5423be2123460308ab16419d4b5dac1d8c9967fc208c0122` |
| `geometry_20261115_pruefer_positive_endpoints.py` | `91dd207bc20a87a36e2d4bc13e1b88a14333b67cf47ec048f85e8d46500822ff` |

三个实际 CLI proof 文件的内容 pin 分别为：

- `--proof`：原 R380／`8a51036fd130c80365284c2e4678c3aa765d177471b4d16df0f4c85add016fa9`。
- `--mode-extension-proof`：原完整 R442／`535118e0403bdf10af73f7b47d35e607121c298c12a077b76e20337a3a6c2013`。
- `--unit-row-proof`：原 R357／`286f17eeab74b44716985fd199d5085cde667fb2626a9eb508ef72d35bc29140`。

原 deep 数据仍分别保 R312 proof／`036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73`。R462 没有将旧深端证书改成更大 M 的证书；新全 M 原适用条件全部由真实新 deep 结果绑定。

### 3.3 完整 M native 依赖

新 worker/client 的原数值数学本体完全保留。新配置逐字核以下完整源码：

| 文件 | SHA-256 |
|---|---|
| `geometry_20261116_current_C_M_general_robin_native.mjs` | `fb951f3688673a01b698bb7c606d6a854c061816e139bae55e51a176b4439f8c` |
| `geometry_20261116_current_C_M_synchronous_linear_bridge.mjs` | `8f189c095ec5bfbc3c323e2421cd98f931931334603ec902a94a75a60a3854de` |
| `exact_20261116_current_C_M_general_robin_chain.py` | `d4f6d4ffa7f54c38fb251ed72ef7d5bcdd8c5371c99506b0b8d98095506c3737` |
| `exact_20261114_tail_capacity_loader.mjs` | `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395` |

此外，原 `original-config.source_sha256` 中每个实际源码完整核读，原 `original_runtime_sha256` 全映射原样保留并由原 native runtime 实际核；不把一份摘要当旧完整运行源闭包。Node/Python/flint 的实际运行版本由原 runtime receipt 记录，本包没有本地 import 验证它们。

## 4. 输入对象与同一准确 C 的绑定

`sample` 必须得到真实同一 job／repository／source 的以下独立原件：

1. f12f 完整 C cover 的 `result.json` 及其实际全部 input binding、source_radial_panels、query_inverse_cover、query plan/results、自然 Rout 和真实 binary cut point 查询。
2. 原112 deep 目录及完整 `result.json`／row stream。
3. 原112 positive 或 joint sampler 的真正 **completed/native_geometry_ready** result、geometry、完整112行文档、原 far matrix、node μ、required prefix，以及原 complete mode／tube／coverage／commit／prepared／coefficient／inverse ledgers；joint 还包括原 numerical selection ledger。
4. 本次独立 R442 全 M deep 目录／result／全部物理频率行与真实适用条件。即使旧112不重复传播，也不以旧 R312 常数冒新增频率 deep 已付。
5. 真原193、joint203 或 actual202205 launcher 的 result 及它实际消费的 absolute deadline 文件。

旧112必须是上述原 sampler 的完整结果。当前窄入口不消费“原 far 完成但原 grid/result 尚未完成”的部分结果，也不把 R456 重新采样输出改标签当原 positive/joint；调用者必须继续保最初旧源 raw。这是已复用原完整 binding 的输入范围，不是给 BVP 增加接受门。

旧、新 data 的完整 C core 准确相同；共同子合同还逐项比较 `actual_cover_result`、`actual_cover_input_binding`、`actual_complete_source_stream`、`actual_complete_inverse_stream`、`actual_query_plan`、`actual_query_results`、`actual_point_query`、`original_binary_cut_exact_rational`。两个 deep binding 仍分别保留，没有强行要求旧、新 deep source 或不同合法盒相等。

旧 far 点保真正原 binary64 半径、四量点包围、所有 inverse leaves、原数值字与误差；μ 来自原 node-mu 最后一字并与全部原 row 的 μ 字核同。所有新增模式都用这两个准确有限坐标字。不能重取一个新的 far midpoint/μ 后继承旧 Q/Π 行。

同一个准确 C／根选择族在每个模式被包含，但联合数值代表仍不必来自一个共同准确 C realization。该限制保在 result、geometry、row document、config 和 worker scope；没有把 C 盒中心或旧 finite selector 变成目标。

## 5. `sample` 的完整 CLI

入口：

```text
python geometry_20261116_current_C_incremental_M_far_union.py sample
  --cover-directory PATH --cover-result-sha256 SHA
  --far-directory NEW_FULL_M_DEEP --far-result-sha256 SHA
  --original-far-directory ORIGINAL112_DEEP --original-far-result-sha256 SHA
  --original-sampling-directory ORIGINAL112_SAMPLER --original-sampling-result-sha256 SHA
  --original-family positive|joint
  --code-directory COMPUTATIONS
  --proof R380_FILE --mode-extension-proof R442_FILE --unit-row-proof R357_FILE
  --origin-launch-directory ORIGINAL_LAUNCH --origin-launch-result-sha256 SHA
  --job-deadline ACTUAL_DEADLINE --job-deadline-sha256 SHA
  --out FRESH_DIRECTORY
  --field-modes M --steps STEPS
  --precision-bits BITS --representative-max-precision-bits BITS
  --max-panels COUNT --max-depth DEPTH --local-defect-bits BITS
  --panel-norm-limit RATIONAL --taylor-terms TERMS
  --max-geometry-cache-records COUNT
  --sample-max-nodes COUNT --sample-inverse-depth DEPTH --sample-value-bits BITS
  --free-bytes-reserve BYTES
  --budget-seconds SECONDS --linear-budget-seconds SECONDS --sampling-budget-seconds SECONDS
```

所有参数都显式 required，没有预填未来 run、M、steps、预算或接受常数。此包范围是整数 M>112；steps、panel/cache/sample count 必须正。沿原有限工作范围，precision 为64..4096，representative precision 不低于它且不高于8192；两个 subdivision depth 为0..60，work bits 为0..1024，Taylor项1..256，panel norm limit 为(0,1/4]，磁盘 reserve 非负。三时间 allowance 为有限正数。

`--far-directory` 是**新全 M deep**，`--original-far-directory` 是**旧112 deep**。它们不是同一项别名。`--original-sampling-directory` 不是 accepted checkpoint 目录，也不要求存在 accepted BVP。所有原数据和 out 必须在真实 RUNNER_TEMP；out 必须不存在且不包含／被包含于任何旧 data 目录。源码／proof 由所给真实 computations/路径完整核。

`--sample-max-nodes` 沿原 sampler 的实际 inverse-range work-unit 计数，不冒唯一物理点数上限。`max-panels` 只计本次新增模式实际推进 attempt。报告保实际唯一点数、fresh point数、inverse range数及各 phase 计数，不把旧112传播工作重新加到本次。

### 5.1 原时钟，不重新开始 namespace

原 R456 `bind_clock` 的三真实来源全部保留：

| origin | launcher SHA-256 | deadline schema |
|---|---|---|
| 原193 | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` | `request193-owned-job-science-deadline-v1` |
| joint203 | `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7` | `request203-owned-job-science-deadline-v1` |
| actual202205 | `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7` | `request205-owned-job-science-deadline-v1` |

必须核实际 launcher 的 `actual_job_deadline` bytes/SHA、相同 recipe SHA、原18900 science 秒／2700 readback reserve及原 namespace 起点。whole-call elapsed 从本次入口前段开始，包含来源加载与绑定实际耗时；原重型 binder 内部不是每次字节都检查，下一边界仍会观察过期。新增传播 phase、numeric＋grid phase 分别有明确 allowance，同时受 whole allowance 和原绝对 deadline 约束，不能按 phase 重新给 namespace。

协作检查处理 SIGTERM/SIGINT flag、实际 out 盘 reserve、原绝对时钟与各工作上限；它不是独立异步 kill。后继 caller 仍须真实使用 OwnedChild／TERM→KILL／join／PID+start-ticks 或独占 PGID quiet 和原 job/step 硬限。本包没有自带已接好的外层 workflow、hard owner 或 cleanup marker。

## 6. 执行数据与完整未付范围

### 6.1 旧来源读入

`bind_old` 先真实加载旧112 runtime，原 `bind_inputs` 必须完整 ready，再按旧 `data['binding']` 调原 R456 `bind_original_far`。它逐原字节读完整旧账并核 SHA／bytes／行数；实际 mode／row／anchor对象完整解析。成功大 coefficient／prepared／tube 等 streams 沿原函数只进行完整身份读取，不声称再次逐值计算证明。

旧完整 binding 和 reuse progress 保存在 `original112_binding`。原库 helper 保持自己的 `M_changed=false`，这里只指被复用的原对象；新 result 和 union binding 明确 `M_changed=true`，不偷偷改写旧 receipts。

完成旧 binding 后只保原 JSON／bytes／有理地址，再加载原 M runtime，避免同一临时模块 tag 覆盖造成旧 class 身份混用。没有 monkeypatch 已刊源的数学全局常量。

### 6.2 新模式

`bind_union` 从所有旧 far inverse leaves 重建新 required/by_panel，并写 `required-source-panels.json` 与 `union-input-binding.json`。后者同时保两个完整 binding、同 C 子字段、全旧／新物理 mode集合、far／μ字、旧行原件身份和 inverse ledger 命名空间。

只为 `data['far_rows'][112:]` 调原 `point_column`，每条要求真实 `physical_frequency=2*(global_index+1)`。原 Taylor／正端点／angle lift／全部候选／prepared→commit／leaf coverage 与完整 pending 原样保留。新频率不会从 m=2 重新编号，也不拿旧模式初列代替新增模式。

仅当全部新增模式完成原 propagation 与 unit-row family 条件后，`new_numeric_rows` 才对它们调用原 `N.form`；旧两个数值字不重选。完整新增候选仍参与误差包围，nominal seed不等于挑中准确全局 C 成员。

### 6.3 全矩阵与新 grid

`complete-M-far-union-rows.json` 保每条原旧／新 row body 与身份、来源、全候选误差、坐标和 ledger spans。新 M×2M矩阵将零基 i 的 Q 放 i、Π 放 M+i；原112两系数按 little-endian bytes保持，包括负零。新增零列是准确零，不能把旧112×224阵整体塞到新阵左上角。

`fresh_grid` 调原 `radial_grid(r_far,r_cut,steps,M)`，保576 stage 的原实际 schedule。只在 sampler cache 预置旧 far 点，其他真实点重新走完整 inverse sampler。所有577 node 半径／μ、实际各stage field参数字与数值误差、port、M×2M far matrix重新形成。原 geometry layout为：

- node_radii、node_mu：各[577]；
- field_geometry：[576, actual_field_count_per_stage, 5]，列为x、r、drdx、logw、dlogwdx；
- far_matrix：[M,2M]；
- stage_packets保全部实际field word与point_index，field plan保完整原schedule。

far处 μ 严格保旧末字，其他 μ 由新原样本形成。native 的实际 exp(logw)、exp(2logw) 与 E 运算仍由原 worker 真实记录；区间 sampler不把它们重标成准确代数恒等式，也不以小native残差支付其有限求值误差。

### 6.4 原件与停止

输出根目录包括 `result.json`、`union-input-binding.json`、`required-source-panels.json`、`complete-M-far-union-rows.json`、`actual-radial-field-plan.json`、完成时的 `geometry.json` 和 `large-arrays/`。部分步骤未到达就不存在相应文件，不造空成功对象。

新账名字为 coefficient-boxes、sample-inverse-leaves、complete-unpaid-scope、new-mode-accepted-panels、new-mode-complete-tubes、new-mode-all-rows、new-mode-panel-commits、new-mode-inverse-leaf-coverage、numeric-point-values-and-errors、new-mode-numeric-row-selection。prepared只属于准备记录；commit才付实际传播前缀。

旧绑定中止保正在读取的ledger与真实已读字节／行数及原未读后缀。新模式停止保 actual attempted／completed／not-started频率，以及原 callee写出的 stack、last-paid、当前factorized state、last-unaccepted、未提交transaction／span与源片后缀。若在模式调用前失败，当前频率仍包含在 not-started完整后缀。新grid停止保实际node／stage／field cursor和完整plan身份，当前inverse stack由原 sampler写入同一unpaid账。

资源停止返回75；原包含／来源／算术未能完成返回2；只有本次新完整geometry产生才返回0。任一失败不称新native拒绝，因为本次sampler并未调用native。发生连 result 都未能写出的外部硬终止／I/O故障时，后继caller必须按实缺失记录，不凭旧hash补result。

## 7. 独立 native 配置与 client／worker

```text
python geometry_20261116_current_C_incremental_M_far_union.py configure
  --directory ACTUAL_UNION --result-sha256 SHA
  --original-config ORIGINAL112_CONFIG --original-config-sha256 SHA
  --computations COMPUTATIONS --out FRESH_CONFIG_FILE
  --quadrature N
```

必须消费本源实际 completed/native_geometry_ready result。`original-config` 是与所复用原112 sampler result对应的 `current-C-complete112-client-config-v1`，不是任意后继 M 或 R456 parent native config。它的原 geometry result 与已绑定旧112 source必须同bytes/SHA；全部原 `source_sha256` 映射真实文件核同。

新 config保原 source_topic、original_runtime_sha256、32迭代／10试探／2e−9／eta0完整策略、线性预算与原所有正量条件，只实际更新独立schema／source tuple／新geometry／M／quadrature／真实steps。quadrature为明确偶数且N>8M，沿原完整角积分输入合同；不是新的rank／验收阈值。

schema如下：

| 对象 | schema |
|---|---|
| union result | `R462-current-C-old112-and-new-M-far-union-fresh-sampling-v1` |
| geometry | `R462-current-C-incremental-M-native-radial-geometry-bundle-v1` |
| config | `R462-current-C-incremental-M-client-config-v1` |
| client | `R462-current-C-incremental-M-live-tail-client-v1` |
| worker | `R462-current-C-incremental-M-live-native-worker-v1` |
| 原 native runtime spec | `current-C-complete-M-native-runtime-spec-v1`（原样） |

`TailClient(config,sources,prefix,node_heap=6144)` 保原四参数API、loadGeometry全维/原clock外层要求、每次完整M请求、完整η0敏感度与原raw word边界。worker对新result/geometry只接受真实独立source与同run/source；native/bridge/QR/原source_topic数学没有复制或缩减。

`configure` **不调用 native**，配置中的 `every_new_native_response_J_mean_and_factor_must_be_fresh` 是后继义务。现 R442/R457 driver 的 source校验还不接受本tuple；必须独立注册后才可继续完整M endpoint与BVP，不能靠改metadata或删来源校验执行。

## 8. 必要读回、quiet与清理

```text
python geometry_20261116_current_C_incremental_M_far_union.py readback
  --directory ACTUAL_UNION --result-sha256 SHA
  --computations COMPUTATIONS --out FRESH_READBACK_DIRECTORY
```

该命令仅Actions内标准库元数据读取，不启动科学算术，不消耗已过期的科学budget来阻止错误读回。外层必须先确认sampler已退出／join，保原complete quiet并给予读回时间；本包没有把仅读者成功冒成全部外部进程已止。

它完整读取实际 result、全部生成ledger的每个byte／行数／SHA。complete-unpaid-scope及new-mode-all-rows解析全部原行，必要正文保全部错误／当前stack／未访地址与每个新模式的完整scope状态。完整 union row文件全解析并核身份，正文保全M逐模式来源／全局列／原两word／原row identity；巨大成功候选、系数和array正文留Actions原件。完成geometry的全部实际arrays完整hash核，不重新科学计算。

`summary.json` schema为 `R462-complete-old-new-mode-union-one-necessary-readback-v1`，包括 producer_result、原字段存在性保留、必要original、完整旧ledger身份、新generated ledger身份、union/geometry完整身份与明确未运输scope。缺键不补null冒原字段。

标准输出是一个独立小frame：

```text
BEGIN_R462_INCREMENTAL_M_FAR_UNION_NECESSARY
<one complete JSON object>
END_R462_INCREMENTAL_M_FAR_UNION_NECESSARY
```

若存在GITHUB_OUTPUT，键为 `incremental_M_far_summary`（实际路径）、`incremental_M_far_summary_bytes`、`incremental_M_far_summary_sha256`。单体上限90000 bytes；极端M或完整未付范围超限时诚实返回70并留下完整临时summary/raw，不能静默删错误、升限、分段或编码大raw。没有承诺任意M/失败都适配90KB。

**无命令删除raw。** 后继统一workflow只能在所有必要读回成功、实际summary身份成立和所有自有科学组quiet之后清理其自身namespace；这里只提供元数据，不替未来外层生成虚构cleanup marker。

## 9. 后继最小注册与未付责任

本包不读取accepted checkpoint，不把旧112接受转给新M，也不改变完整BVP的真parent与十词/准确target绑定。下一独立driver/writer须同时保存：

- 真accepted parent的原profile/十词/完整状态、原FD/final/audit来源；
- 本次完整新M deep结果与旧112原完整far的两个来源；
- 新union geometry、完整native config/client/worker/原M数学闭包；
- 新全部native响应／J／双mean／$(3M+2)\times M$端响应、fresh全部RHS与$(4M+2)$冻结BVP；
- 实际绝对clock／owned child、所有partial与必要readback／quiet；
- 真新checkpoint后重新radial／atlas／shared／metric／reach／held及公共材料同g比较的来源。

其中任何未做都继续未付，不由本次旧模态复用定理填补。M扩展只复用单模态远端完整族及其坐标表示，不复用响应、J、QR、warm接受、exact-C共同实现或几何证书。没有新fixture、额外科学前门、实际request或派发；原全M路径仍合法可继续。
