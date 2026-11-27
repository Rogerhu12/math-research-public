# Fejér 固定参考：完整 mean/profile 费用入口

本包为新的、预先规定的 Fejér/R690 数学目标提供三个完整费用程序：准确总均值残差 producer、完整 profile moment 与条件两角 jet consumer、全部实际已记录 batch 的 scheduler。它们独立从已刊 run10 三个完整父源派生；原目标和原文件保持，新的输入归属必须以本分支完整 recipe、实际参考和实际场报告重读。

本包给出完整运行体、完整可逆源再生器、直接来源锁表、一个完整 Actions 参数文件及本文。每件小于 100000 bytes。这里只进行了完整源码文字派生、来源和字段对照、前向与逆向逐字恢复；没有运行 Python AST/compile，没有导入或执行数学、NumPy、区间、profile、F/J/root 或缩小科学算例。费用 step 尚未准入或执行，它不是当前科学求解入口的前置条件。

## 1. 新固定目标与真正已经返回的输入

准确目标使用 R717 规定的七项有理设计的 RN-even binary64 像，随后把这些实际二进有理数当作准确 chart 参数。原理想有理 Fejér 多项式只用于已刊的正性与舍入比较，不能把其理想系数替换实际 chart 而免除误差。完整 160 项、前三固定项与后 157 个当前自由 core 槽的区别继续存在；费用计算固定 reference seed，不覆盖当前任意非零 outer 控制。

完整数学依据见 [R717](../results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 和 [R709、R710、R713 等既有结果索引](../results.md)。本次是实际来源适配，不重复登记这些证明，也没有重新声称完整场已满足它们的全部条件。

本包亲读的实际记录是
[run12 阶段 1–2 的完整公开小卷](2026-11-27-public-actions-46011377225-1-part-001.md)，
16600 bytes，SHA256 `5c093747e64ca227983e72590db4f5fc9bcc6fc950889504ee85edc8df30472a`，
Git blob `2daddb631388db54dd4309857297294c332faf1a`。
两项必要输入真实 returncode 均为 0。maker 用时 5.893721085999999 秒，reference 用时 430.2165345 秒；这些是实际过程记录，不是本费用程序的性能数字。

实际数学目标 canonical identity 为
`957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`。
完整返回 reference definition identity 为
`50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319`，
reference model identity 为
`ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac`。
它们与文件 whole SHA 分开记录。

| 真正返回的输入文件 | bytes | 完整 SHA256 |
|---|---:|---|
| fixed-reference-input.npz | 4334 | `b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98` |
| fixed-affine-nodes.json | 144306 | `1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5` |
| fixed-scalar-input.json | 40488 | `2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189` |
| reference.npz | 894879 | `212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb` |
| observations.npz | 205842 | `84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e` |
| report.json | 84966 | `a35e7ed22d3453d69cc746ff6b706735717bb74131d43ece0b7ddda440403900` |

对应实际完整六文件 binding 为 35712 bytes，
SHA256 `a6992516e83b53e153bf5d2b9ef8985f7542bff615e2b3edd6e467a2d105f52b`。
固定 chart 全数组摘要为 `af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103`，
完整 mesh 数组摘要为 `ca4b5c626e0e5cf1687c40c25a68a76c4e8fbde391bd8c853399400c784dddfc`。
本包只从上列小卷读取这些输出身份；没有通过 connector 读取大型 NPZ、144306-byte 节点全文或地点/逐点数组。

reference 的固定工作规则是完整 2218 叶；实际返回也是 2218 叶。完整尾域保留，`requested_integral_accuracy_reached=false`。
consumer 严格接受这项真实布尔值，不把它改为 true，也不把未付宽度写成零。
2218 不是准确积分证书；本 producer 会用原完整区间公式及径向 cover 重新支付实际 seed 的均值方程费用。
旧 run05 的 2397 叶和 dc5 carrier 不作为当前参考数值输入，本新族没有把它们重新标成 Fejér 对象。

真正存在的输入不等于已经存在的场或均值 batch。本 ready 对科学报告 whole SHA、实际完成 batch 数和费用结果仍保留 null；完整 source identity 已知，实际数据 identity 只从相应完整返回文件核得。输入身份在 ready 中作为已观测事实保存，运行时仍必须全部重读，不以本文或 summary 替代完整实际输入。

## 2. 三个完整运行体及直接父体

| 完整运行体 | bytes | 完整 SHA256 |
|---|---:|---|
| [fixed_fejer_reference_seed_angular_profile_error_bounds.py](../scripts/resume_20261126/fixed_fejer_reference_seed_angular_profile_error_bounds.py) | 72182 | `0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b` |
| [fixed_fejer_reference_accurate_mean_residuals.py](../scripts/resume_20261126/fixed_fejer_reference_accurate_mean_residuals.py) | 41476 | `ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0` |
| [fixed_fejer_all_recorded_reference_seed_fees.py](../scripts/resume_20261126/fixed_fejer_all_recorded_reference_seed_fees.py) | 29348 | `ff21999e226953efd095f403f413c08fc244e36c05122485f97b128d699b5bba` |

直接父体分别是：

- `run10_reference_seed_angular_profile_error_bounds.py`，64800 bytes，`91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1`；
- `run10_reference_accurate_mean_residuals.py`，40898 bytes，`19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38`；
- `run10_all_recorded_reference_seed_fees.py`，29234 bytes，`42624b7f7fb4be694ff1253baf456b8526269a0f20099a40af737b5ffc096cb5`。

三者的完整 SHA 和更早 R713/C1/material-envelope/run09 来源仍写在独立完整程序中。没有修改旧三体或旧 journal schema，没有把旧输出重新解释为新 source 的费用。

新 source schema 为：

| 对象 | 精确 schema |
|---|---|
| profile/角 jet consumer | `complete-fixed-fejer-reference-actual-seed-angular-profile-node-fees-v1` |
| accurate mean producer | `complete-fixed-fejer-reference-accurate-total-mean-residuals-v1` |
| 径向 journal | `same-fixed-fejer-reference-actual-batch-complete-integral-journal-v1` |
| accurate request | `actual-fixed-fejer-reference-seed-accurate-fee-request-v1` |
| all-batch schedule | `complete-fixed-fejer-all-recorded-reference-seed-fee-schedule-v1` |

源闭包不是只检查 schema。所有源仍按 whole SHA 检查，实际函数的 code filename 归属继续由完整 reader 和原加载函数验证。

## 3. 实际来源与六文件的绑定

本入口只接受完整新科学 driver
`fullclosed_fixed_fejer_immutable_point_so3_qp.py`，
SHA `477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd`，
及其完整 pure reader
`read_fixed_fejer_immutable_point_so3_report.py`，
SHA `274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b`。
该 reader 保有已刊完整 110-role source registry 以及每个 source/model/snapshot/packet/typed-memory/scan/row 原合同。费用源不再复制另一份大 registry，也不缩减 reader 的真实逐项重核。

关键直接来源如下：

| 角色 | 实际完整源 SHA256 |
|---|---|
| deterministic maker 89cc | `89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60` |
| complete reference e717 | `e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb` |
| pure six-input binder 3da | `3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f` |
| full source/report binding 3b3 | `3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88` |
| fixed supported provider ad52 | `ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a` |
| complete mean kernel f848 | `f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917` |
| complete current base 552f | `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3` |
| complete whole-scalar interval source a846 | `a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6` |

`bind_fixed_fejer_reference_attribution(raw,pure)` 对整目标、其 canonical identity、全部 reference model、fixed seed 内同模型、完整 reference NPZ、chart 摘要及 maker 数学 recipe 逐项核等。真实 pure role 名为 `actual_public_input_binding`，继续使用这个已存在角色；没有虚构新的 source role。

六文件的准确键为
`current_fixed_input_bundle`、`current_node_report`、`current_scalar_input`、
`current_carrier`、`current_preparation_report`、`current_reference_bundle`。
new fixed-input NPZ 是七成员输入，不能用旧 warm/qjets 替代。固定原有五个 CLI 输入参数保持；第六个 fixed-input NPZ、maker report 与其全部原输入/源码来自真实六文件 binding 的完整出处，全部重读。

完整核对包括：

1. report 的 target、material-envelope actual-path binding 的 target、纯读 target、reference model、base model 与 seed model 整对象相等；
2. 实际 maker 输出三记录与六文件的三个对应角色整记录相等，maker 的完整 `definition`、数学目标 recipe、e640 参数身份和实际 whole-source 均相等；
3. 准确 scalar profile、全尾包含、实际固定叶数及真实精度布尔值，从准备报告的完整 `true_scalar` 读取；
4. maker 所有 source/input records、完整 preparation source paths、target file、locations 和 supplied-location-provenance 文件，加入不可变字节快照；
5. input reference 执行的真实 run/attempt 与实际 binding 相等，但不把 reference 的一次执行误作 field 或 fee 的执行身份；
6. 旧值、旧 roots/certificates、same-original-chart 或 same-mathematical-g 声明均不得迁入；旧 literal 的 reinterpretation 明确保持，未知旧报告/typed 顺序不回填。

源路径可能属于仍保存的旧 followup checkout；记录指定的实际文件仍须存在且 whole SHA/bytes 匹配。当前加载副本的 whole source 被另行核定，不能拿 basename 相同替代真实路径记录。缺文件或身份差异是费用输入不可用，不能因此宣布数学场不存在。

## 4. 实际 batch 与当前 outer 场的范围

读取流程捕获科学 report 全字节和 SHA，再运行完整 274d reader，并复核返回的 SHA 与前后文件。raw 的
`latest_operator_metadata.base_complete_metadata.fixed_supported_unit_seed.mean_batch_records`
必须与完整 pure `seed_diagnostics.mean_batch_records` 逐值相等。

每个实际完成 batch 保留 seed identity、原顺序全部 literal φ hex、原 raw NPZ 的全 15 个向量/标量数组、shape、binary64 类型、finite 条件及文件 whole SHA。向量是 v/d/w 的 0/1/2 角 jet，标量是 λ 的 0/1/2 角 jet 与三个实际 profile moment 工作值。读取数组后的 report/NPZ 摘要再次比较。显式 raw-array path override 仅改变存放位置，不能改变身份。

scheduler 取每一个真正记录的完成 batch，包含任意历史/几何地址触发的批次，依原顺序调度，不固定 batch 0、不抽角、不删最后失败信息。真实 `last_recorded_seed_failure`、phase、reason 原样保留。provider 每个新 literal angle 只登记一次的合同继续核对，完成角总数与整个列表逐项一致。零个真实 batch 不产生 vacuous complete，也不由另一个 run 的 batch 替补。

这些 fixed-seed 费用同时完整绑定当前 outer model、frozen initial reference point、R715 calibration、C1/full-stage contract 和真实 material-envelope policy，但归属不等于费用已付。解析 frame、解析 J3、不可写点和同链缓存仍是 outer 数值模型的来源；它们不免除准确根、全 32 stages、两角隐式导数或物理六 jet 的误差责任。固定 seed 的 v/H/chart 不从当前 outer 参数重新选取。

## 5. 原完整数学、径向 cover 与 profile moment

producer 的 `ActualMeanBatch` 从完整 e717 context 初始化，所有原数学字段和 API 保持。chart 使用 context 中实际生成的 160 个 binary64 字作为准确有理参数，保全部模式及 0/1/2 角导；不直接换成 R717 的理想有理值。H 是该 fixed seed 的实际 frozen H，R 采用同 context 的完整准确 enclosure。五个参数输入和六文件/maker 原出处在初始化和每次输出前重核。

准确仿射位置仍写作 $s=\alpha S+\beta$，存放为 $(\alpha,\beta)$。完整 plan 包含全部 923 原准确节点、两个 support、两个 central 和四个 boundary 的所有端点。central 的 $L_c v$、boundary 的完整归一化向量以及 outside 的完整 b/c 积分共同形成三个准确均值方程；原两角 jet 中的所有交叉项与当前候选字费用保持。全尾、scalar branch 的结构正性来源、严格归一化分母与准确径向整叶盒均未削减。

`CompleteLeafJournal` 整类逐字不变。全初始 cover 完成前不发 fee-request；split 需要两个完整 child 先完成，先写/fsync 日志，再用精确端点和替换父贡献。恢复保每一条顺序、前序 hash、全部角/jet/坐标、完整 binding 与精确 partition，partial 最后一行仍拒绝。原自然预算允许报告部分真实 cover；缺块不补零，不把整数叶数当准确覆盖证明。

consumer 的 Interval 整类、所有准确 profile 片段、精确矩、完整 Taylor 余项、归一化两角 jet、mean 三方程误差和四 reference jet 公式保持。唯一 profile 内的来源变化，是把旧 provider schema 守卫换为完整 ad52 实际 schema，公式未换。三 profile moment 的费用仍由所有片段精确积分和原级数余项实际计算；producer 的 `profile_moments_computed_here=False` 和 `profile_moments_require_independent_R713_consumer=True` 保持，不把职责写成已完成。

打印出的 working residual 或 working Newton tolerance 不能替代准确均值残差。一个完整 mean cover 可以有宽盒；是否达到 `1/100000000` width-goal、条件 mean/profile 算术是否完成、全部已记录 batch 是否完成分别报告。宽盒使某个正性/逆矩阵前提未付时，原异常和部分结果保留，不改为几何不可行结论。

## 6. 前后重核与不会晋升的结论

新源在原快照责任上加入 maker 与六文件完整出处的末次重核。mean 的初始化及 `recheck_actual_bytes` 重新核这些实际 source/input/output records。consumer 只有在全部结果生成后再次核完整输入快照、report、raw batch 与 fee-request whole SHA，才写 `complete=True` 及 `all_actual_input_and_fee_request_records_rechecked=True`。scheduler 保持每个 child 后和总返回前的整快照重核。

consumer 的 complete 仍表示：对这一真实 batch、所给准确 mean 输入和所请求节点，完整条件算术已处理。external accurate fees 的来源责任保留。scheduler 只有全部实际已记录 batch 的 complete producer/consumer 记录齐全才报告其 complete；它不会把空 batch 集、working 精度、first field 成功或某一个 geometry scan 当作费用完成。

本 ready 没有实际节点工作四 jet 输入，因此保持 `requested_nodes=[]`，`actual_node_jet_fees_paid=False`。本组件不支付 whole-φ cover、外层 normal/IFT、基线 raw calibration、物理六 jet、Gram/曲率、A-support、闭浸入/嵌入/reach、固定握持、全 phase 或 R716 矩责任。geometry 的完整 whole-φ adapter 可以复用本数学方法，但必须仍自行构造每个准确角盒和根/径向费用；不能把 literal batch 的 complete 标志当作它的 cover。

## 7. 完整参数与输出

完整参数位于
[fixed-fejer-all-recorded-reference-seed-fees-ready.json](../computations/fixed-fejer-all-recorded-reference-seed-fees-ready.json)。
其唯一完整 step 为 `all-actual-fixed-fejer-reference-seed-batches-mean-profile-fees-first-20261127`，
script 为 `fixed_fejer_all_recorded_reference_seed_fees.py`，
parent 是真正新输入 `fixed-fejer-reference/reference.npz`。科学 report 为
`{work}/fixed-fejer-immutable-point-first/report.json`，
输出为 `{work}/fixed-fejer-all-recorded-reference-seed-fees/report.json`。

全部 32 个 argv 元素如下：

```text
--repo {repo}
--report {work}/fixed-fejer-immutable-point-first/report.json
--reference-bundle {work}/fixed-fejer-reference/reference.npz
--carrier {work}/fixed-fejer-reference/observations.npz
--node-report {work}/fixed-fejer-r690-inputs/fixed-affine-nodes.json
--scalar-input {work}/fixed-fejer-r690-inputs/fixed-scalar-input.json
--preparation-report {work}/fixed-fejer-reference/report.json
--outdir {work}/fixed-fejer-all-recorded-reference-seed-fees
--execution-mode complete-recorded-batches
--seconds 600
--per-batch-seconds 60
--panels 128
--precision-bits 160
--width-goal 1/100000000
--taylor-order 48
--profile-series-order 48
```

与已刊 run10 完整 ready 比较，只有七个实际输入/输出路径改为本分支路径；所有参数名、数值、execution-mode 和预算逐字保持。48 个原 scalar summary selector 的名称全部保留，仅 actual attribution 的路径改为新实际字段；另增加六个新 recipe/输入/重解释状态 selector，总计 54。没有输出对象代替 scalar selector，没有删除原失败信息。所有 runner 原始 journal、raw batch、consumer 结果和子进程日志保留；ready 未加入清理规则。

scheduler 子进程完整调用由原 `producer_args` 和 `consumer_args` 函数生成。mean 对每个实际 index 传全五个输入、实际 batch 原顺序、原精度与剩余自然预算；consumer 传该实际 request、同一 report/index 和全部 profile/算术参数。consumer 不受额外人工短时中断，预算语义与原实现相同，600 秒不声称硬实时上界。

source report 未返回或 raw arrays 不存在时，相应费用自然不能运行；这是真实输入依赖，不是增加独立科学准入门。当前 solver 在独立执行，费用源完成不要求先出另一份 fixture。

## 8. 可逆完整源复现及实际核查范围

完整标准库再生器
[derive_fixed_fejer_reference_seed_fee_sources.py](../scripts/resume_20261126/derive_fixed_fejer_reference_seed_fee_sources.py)
保存三个父体的 whole SHA/bytes、每处完整 old/new 文本、出现次数和准确字符位置，以及三个完整目标 SHA/bytes。前向逐处替换；逆向用准确位置消去新片段，并完整恢复所有原字节。不能用全局模糊替换把新函数名与旧调用混为一谈。

源码级完整前向/逆向已在 V8 文本环境逐体核相等。这不是 Python AST/compile 或数学执行。再生器本身只读源、做标准库文字/摘要并写完整源，未来 root 可在现有工作流直接使用；它不是另设求解前门。调用为：

```text
python derive_fixed_fejer_reference_seed_fee_sources.py --repo REPO --outdir SCRATCH
python derive_fixed_fejer_reference_seed_fee_sources.py --repo REPO --outdir SCRATCH --verify-existing
```

实际逐字比较的细分范围是：consumer 33 个同名 top-level 函数全文保持、Interval 整类保持；profile moment 函数只改一项 provider schema literal。mean 的 ActualMeanBatch 12 个数学方法保持，constructor 只补来源重核，recheck 方法补完整 input snapshot；CompleteLeafJournal 整类保持。scheduler 的整个 main 至 EOF、子进程命令构造、费用校验/状态/自然预算机制保持，来源 attribution 路径按新族变化。所有例外都在完整可逆操作表里，未用这张范围表代替 whole-file 复现。

solver 独立全文读取 consumer 72182-byte 候选并定点核新 attribution、batch、recheck 与 e717/3da/3b3/477 的实际字段交界，未见所读接口阻断；其范围不是 R713 数学重审或新 scheduler 全审。geometry 已收到本两个数学消费者的最终 source pins。本文不把任何源码审读称为运行成功或准确费用已付。

## 9. 发布与后继责任

当前三个新运行体 whole SHA 已锁；source-lock 与本说明列明所有必要直接依赖，完整 110-role 科学祖先闭包由 whole pinned 274d reader 真读。没有为了仓库容量复制该已刊大表或裁剪科学源。旧三体、旧原参数、历史来源和结论全部保持。

root 是唯一 refs/queue 写者；本次仅提交未引用的完整 Git blobs 供普通发布。费用结果、实际 batch 数、当前场误差和研究目标完成状态均未预填。下一实际返回若表明输入或程序有具体问题，保原源与真实失败，再做明确独立修订；不改已刊旧目标，不宽松来源守卫，也不把失效输入误当数学不可能。
