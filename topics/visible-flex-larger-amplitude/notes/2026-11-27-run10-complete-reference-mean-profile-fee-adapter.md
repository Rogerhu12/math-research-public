# run10：实际固定参考的完整 mean/profile 费用入口

本包把已刊 run09 的三个完整固定参考费用程序，独立接到 run10 的实际输入及 detached-closure 科学族。原 R709/R713 算术、完整径向积分日志与全已记录批次调度保持。新入口必须消费 run10 真正存在的一份完整报告及其全部完成均值批次；本文没有把尚未取得的首场、批次数、normal 根、误差费用或最终证书写成已完成。

本次只进行了完整源码文本派生、正逆字节核对和接口对照。执行器实测不可用，未运行 Python AST/compile、未导入科学模块、未运行任何本地 F/J/root、积分或缩小算例。独立再生器实现了全体 AST/compile、75 个完整来源与精确正逆派生的源检查，供有执行器时直接使用；这不是科学主线的额外准入条件。

## 1. 实际输入与数学归属

实际 run 为 `45972294636/1`。本包亲读的公开小卷是
[`2026-11-27-public-actions-45972294636-1-part-001.md`](2026-11-27-public-actions-45972294636-1-part-001.md)，固定 commit
`8e32b487661e9ee886f8c4968dcf4d31015e9938`，38575 bytes，SHA256
`0b1de8d544053aa5e67f80b144a65274c2f111825845482e68c5c278ef9f7cee`，
Git blob `e914a571f6fe2c228e6662ad2b144363c8486881`。
其中 warm、reference、完整固定输入 producer 与 source-only 检查均有真实返回；这份小卷不代表随后完整场已经返回。

当前 reference 的真实身份如下：

| 对象 | 完整 SHA256 | bytes |
|---|---|---:|
| current_warm_bundle | `3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c` | 8767118 |
| current_node_report | `1fed8f9b49202ae67c2d317c3a30d855d7a5d9f486fe034591a23fada2b08268` | 554141 |
| current_scalar_input | `aa7af21dc95861841c2d6cbbe4d5034cce671e796fe8a4346aeb8aa887d8b2c4` | 14227847 |
| current_reference_bundle | `512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b` | 866207 |
| current_carrier | `71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d` | 227202 |
| current_preparation_report | `35fdae489de9a7ee205b4f03f805b30107cec382abbdd242ece43f87d857d286` | 29809 |

模型身份为
`081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5`；
完整 scalar profile 为
`c46f875f96a41a09ccad4bcfb75ed6efd33e239b28dbcdb538ce9d2daa47bc65`；
固定 chart 为
`90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e`。
当前固定目标 canonical identity 为
`e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049`。

它与目标 JSON 的 whole-file SHA
`b24080447828d8ffb49ae146dd5672d34bf6f5cec512054633b6f849c2bdabfb`
（97335 bytes）分别记录，不能互换。实际完整输入 binding 的 whole-file SHA 为
`4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf`
（430908 bytes）；该大输入只由 runner 完整读取，未通过 connector 整读或另包装转存。

当前 preparation 真实记录 **2218** 个 scalar 积分叶，`scalar_complete_tail=true`，
`scalar_tolerance_reached=false`。完整覆盖与达到请求精度是两个字段。其准确宽度仍保在实际 preparation 与新费用 attribution 中，没有把未达到的精度补成零。当前 reference 的 R/H、精确 scalar law、chart 和 frozen seed 都来自上表完整当前输入。

另一个 **2397** 是固定旧 run05 carrier 恢复程序使用的原积分表叶数。该 producer 返回的
`actual_scalar_live_leaves=2397` 属于它的旧表恢复过程；不能把它解释成当前 reference preparation 的叶数。
恢复出的旧 carrier whole SHA
`dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`
（227202 bytes）继续承担历史地址责任，而不会替换当前 R、H、误差包围或 seed 工作值。

虽然 warm whole bytes 与旧某次记录相同、原固定 chart 也相同，本包仍保留
`same_original_fixed_chart=true`、
`same_mathematical_g_claimed=false` 和
`old_values_or_certificates_inherited=false` 的真实合同。
不声称相同 g 也不是声称数学上不同；它要求真正重读当前完整目标，不能用少数相同摘要推出已继承场或费用。

## 2. 完整新源码及父源

三个运行体都完整保存在新 basename；没有覆盖原 run09 文件，也没有依赖一个只改标签的执行代理。

| 完整运行体 | bytes | SHA256 |
|---|---:|---|
| [run10_reference_seed_angular_profile_error_bounds.py](../scripts/resume_20261126/run10_reference_seed_angular_profile_error_bounds.py) | 64800 | `91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1` |
| [run10_reference_accurate_mean_residuals.py](../scripts/resume_20261126/run10_reference_accurate_mean_residuals.py) | 40898 | `19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38` |
| [run10_all_recorded_reference_seed_fees.py](../scripts/resume_20261126/run10_all_recorded_reference_seed_fees.py) | 29234 | `42624b7f7fb4be694ff1253baf456b8526269a0f20099a40af737b5ffc096cb5` |

直接父体依次为：

- `run09_reference_seed_angular_profile_error_bounds.py`：
  `7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1`；
- `run09_reference_accurate_mean_residuals.py`：
  `17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820`；
- `run09_all_recorded_reference_seed_fees.py`：
  `0c7efa0726aa27dbde769a8cce7615efc75e1676b49cf3c2602767b8543d915f`。

每个新体另有明确 `DERIVED_FROM_COMPLETE_RUN09_*_SHA256`。其更早 R713、C1、material-envelope 父来源仍按原记录保留。没有把新输入的来源链改写成旧 run09 真输入。

完整再生器
[`derive_run10_reference_seed_fee_sources.py`](../scripts/resume_20261126/derive_run10_reference_seed_fee_sources.py)，
32018 bytes，SHA256 `06908b376ab4d9da84dfc7b39068c7fb2c64faf689f4e0f083aa3829f1416640`，
只导入标准库，记录每一项前向替换、出现次数、完整输出 SHA 及逆替换。
逆序替换在文本阶段已经逐体还原整个已刊父源，而非只比较少数选中函数。
它还实现以下源级检查，但本文不冒称在失联执行器上已经运行：

1. 验证三个已刊父文件的完整 bytes/SHA；
2. 全部新体解析与 compile、重复字典键/关键字检查；
3. 原数学和控制主体完整 AST 与源片段等号；
4. 读取真实 c3dc driver 的全部 `SOURCE_PINS`，逐项重核 **75** 个完整源，不删历史父族；
5. 新科学/纯读/normal/calibration/memory 的 schema 与实际 source roles 等号；
6. 当前 dc3b input binding 的 whole binding、canonical target、model、chart 和两 input producer 源；
7. 新 consumer → producer → scheduler 的精确依赖链；
8. 可选 `--verify-existing` 检查现存完整派生体逐字一致。

## 3. 明确改变了什么、保留了什么

科学 outer source 是完整
`fullclosed_run10_detached_closure_so3_qp.py`，
SHA `c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1`；
纯读器是完整
`read_run10_detached_closure_so3_report.py`，
SHA `2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e`。
字段 schema 是
`complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1`，
normal whole source 为
`6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4`。

新的 attribution 绑定当前 calibration b597、C1 1f80、memory f1c、geometry 6c67、
input/完整源 binding dc3b，以及实际 public input 9f69 与 freeze producer fcd2。
完整值在 source-lock 中逐项保存。C1、解析 frame/J3 和 detached closure 的实际来源仅用于识别 outer field；
这些优化本身没有支付准确 seed、normal 或全场费用。

已有均值 provider
`0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b`
及其均值 kernel
`f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917`
保持。完整准确参考 kernel 4e655 和 whole-scalar 积分核 a846 保持。

本次文本核对的完整主体范围是：

| 程序 | 逐字保持的完整 top-level 主体 | 范围 |
|---|---:|---|
| consumer | 36 | 包含 Interval 整类、所有 profile/mean/node 区间公式、输入解析和 main；仅四个实际来源绑定主体有名称/路径合同变化 |
| producer | 17 | 15 个函数及 ActualMeanBatch、CompleteLeafJournal 两个整类全部逐字相同 |
| scheduler | 18 | 完整子进程、校验、状态、budget/resume、main 等保持；只有 attribution/bind/recheck 三个主体的 run10 key 名称变化 |

这张表是实际文本比较，不能写成未进行的 AST 或数学数值比较。
完整再生器保存了同一范围的 AST 检查实现。

## 4. 一份真实报告、全部真实批次

scheduler 先捕获当前 whole report 字节，再调用完整 2efa 纯读器；
捕获的 SHA、纯读器返回的 SHA 与读取后的文件 SHA 必须相同。
该纯读器仍核完整 source/model/current-point、全部原 snapshot、
detached closure 实际计数、全 material-envelope scan/row 与其来源。
费用程序不会用 latest metadata 回填旧 snapshot。

`bind_run10_reference_attribution` 进一步把以下对象交叉核为同一输入：

- 顶层 fixed target、material-envelope actual-path binding 内整 target 和各 canonical identity；
- target 内完整 current reference model、outer base 内完整 reference model、fixed seed 内完整 reference model；
- 顶层 whole reference bundle、base/seed 的原始 reference bundle 和实际六文件；
- 全 chart 字身份、完整当前输入 evidence、actual input producer/source 和真实 run/attempt；
- preparation whole bytes、完整 reference_definition、准确 scalar definition、全尾覆盖和实际积分叶数。

六原文件及 binding 在读取前后重核，不以本地路径相同代替完整字节身份。
当前 scalar 输入 SHA 以真实 `aa7af21d...` 开头；完整值在上表和 runner 记录中保留。

实际均值数组只来自：
`latest_operator_metadata.base_complete_metadata.fixed_supported_unit_seed.mean_batch_records[index].runner_raw_arrays`。
完整纯读后的批次列表必须与捕获原 report 的列表逐值相等。每个完成记录的 fixed seed identity、
全 literal φ 顺序、shape/dtype/finite 值和 raw whole SHA 必须吻合。
路径 override 只能换存放路径，不能换数组身份。

scheduler 把所有真实完成记录依原顺序纳入计划，包括任意永久几何地址触发的 batch。
不固定 batch 0，不抽少数角，不把缺失或失败 batch 替换成别的 report。
原 provider 的每个新 literal angle 只记录一次的合同仍严格核；
完成角数必须等于完整记录的实际总数。
`last_recorded_seed_failure`、`last_seed_failure_phase`、
`last_seed_failure_reason` 按当前完整纯读器的真实字段保存，不重新引入旧 `last_failure` 错键。

零个真实完成 batch 时，不把空集合标记成费用完成。
未取得 source report 或其 whole raw arrays 时，入口不能支付对应费用；
没有造一份成功 report、数值零残差或非存在结论替代它。

## 5. 准确费用的范围

producer 保留完整准确径向域和所有初始切片，包含无限尾。
精确仿射位置仍按原约定
$s=\lambda S+\eta$，存放顺序为 $(\lambda,\eta)$。
当前 scalar/chart/core/H 与实际均值候选字都属于同一被验证的 fixed seed。
完整初覆盖、每一 split、叶身份和 journal 恢复规则保持。
只在整个所需 cover 完成后生成原格式 fee-request。

consumer 保留全部分段精确 profile moments、完整均值方程及其两角导误差，
并把实际候选字与准确闭包比较。打印出的工作残差不当作准确残差费用；
达到工作 Newton tolerance 也不免除任何包围项。

自然预算返回的字段区分：

- 径向完整 cover；
- 请求的 width-goal 是否达到；
- 每一个完整 actual batch 的 mean/profile 费用是否完成；
- 整份报告所有已记录 batch 是否完成。

这些字段互不代替。未供 actual node words 时，原 `requested_nodes=[]` 保持。
本 step 不重算当前 F/J/normal roots，也不声称支付当前 raw calibration、
全部 32 个 normal stage、隐式导数、物理六 jet、whole-φ 连续 cover、
Gram/curvature、闭面外向或 R716 体积矩责任。
normal/sixjet 与闭面消费者必须使用各自完整新合同，不能仅凭此 seed attribution 升格。

## 6. 完整可准入参数

完整参数文件
[`run10-all-recorded-reference-seed-fees-ready.json`](../computations/run10-all-recorded-reference-seed-fees-ready.json)，
9788 bytes，SHA256 `5e39c84e9c0ec48458acbded09d1d50ba377735c7f9d009d4e7e752c9b81e09d`。
其中只有一个完整科学 step，32 个 argv 元素、48 个标量 summary selector；
原五个输入参数、all-recorded-batches 机制及原 budget 未缩减。

入口读取
`{work}/run10-detached-closure-values-first/report.json`；
输出
`{work}/run10-all-recorded-reference-seed-fees/report.json`。
source report whole SHA 只在实际执行时取得；本文件不预填它。
完整 current reference NPZ 是 controller 的 parent。
输出命名空间与 source report、六输入及全部实际 batch arrays 先检查分离，
不会先覆盖输入再靠末次摘要发现。

所有原参数完整保留：

```text
--repo {repo}
--report {work}/run10-detached-closure-values-first/report.json
--reference-bundle {work}/axisymmetric-R690-reference-v2-first/reference.npz
--carrier {work}/axisymmetric-R690-reference-v2-first/observations.npz
--node-report {work}/fullclosed_solver/data/fullclosed-hold-warm.json
--scalar-input {work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz
--preparation-report {work}/axisymmetric-R690-reference-v2-first/report.json
--outdir {work}/run10-all-recorded-reference-seed-fees
--execution-mode complete-recorded-batches
--seconds 600
--per-batch-seconds 60
--panels 128
--precision-bits 160
--width-goal 1/100000000
--taylor-order 48
--profile-series-order 48
```

600 秒是原调度自然预算；子进程真实 setup、完整初覆盖与消费者执行仍有实际成本，
不能据此承诺 wall time 上限或全部费用成功。每批次 60 秒轮转、完整保留 journal 和
同 immutable report/参数的恢复规则都没有改。

## 7. 交付与复核边界

完整锁表
[`run10-reference-seed-fee-source-lock.json`](../computations/run10-reference-seed-fee-source-lock.json)，
27321 bytes，SHA256 `acbd01ef756733b0e21e2a5b5b258ff84426b0a647e180d2bfd5b670b29e48fd`，
保留三个父与三个新体、全再生器、75 原始 source roles、
真实公开小卷、六实际输入与目标 whole/canonical 两类身份、完整准备参数及所有未付范围。

本次已经完成的工作是完整源文本派生和全字节正逆核对；
新费用 step 尚未执行，实际 mean/profile 完成率、精确残差、profile 误差和速度均未知。
原 run09 三体、run10 科学/纯读程序及已排科学参数保持原字节。
费用独立追加在实际科学与纯读之后，不成为求解器的新前置门。
