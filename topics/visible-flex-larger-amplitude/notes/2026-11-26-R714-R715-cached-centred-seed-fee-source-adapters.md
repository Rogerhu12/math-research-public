# R714 / R715 缓存中心化表示的独立完整 seed 费用消费者

## 1. 来源适配的范围

本次为 R714 同一计算图内 frame 复用与 R715 完整参考中心化组合后的新表示，独立生成两份完整科学源：R713 准确中央 profile 矩和参考角 jet / node 费用消费者，以及完整准确 mean 方程积分 producer。它们从原 `82e6f1a7…`、`581fbcc3…` 完整体派生；原消费者、plain-centered 两源及其 schema 和硬来源检查均保持不变。

缓存版源有自己的 report / request / journal schema。只有它自己的完整 driver、pure reader、normal 算子、calibration helper、C1 helper 和实际返回的 seed batch 才能组成合法输入。本次未选定 batch、未产生 fee request、未运行科学计算，也没有假设未来求解已经返回初场或完整 mean batch。

该适配不是新求解方向的前置条件。未执行的 plain R711 / plain-centered 分支不产生必须先跑的报告或位置责任。真正已发生的历史仍由各完整求解入口按实际报告保留；本消费者不会删减、补造或转移历史地点。

## 2. 精确完整来源合同

| 角色 | 完整 SHA256 |
|---|---|
| cached driver | `f075257aaea0930f60d905c9b02ac5cfcff61bc42d7daf337912c8a287d0f347` |
| cached pure reader | `3803a72570aed98eb797f03aca6696055b299ad43e1b06673c482c1a6b25a907` |
| cached normal field | `a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd` |
| cached calibration helper | `3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991` |
| `frame_C1` helper | `ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9` |
| 原完整 R711 provider | `0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b` |
| 原完整 R711 mean kernel | `f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917` |
| 原完整 R711 base | `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865` |

报告 schema 固定为 `complete-R711-reference-centred-C1-reuse-fixed-normal-plane-SO3-QP-v1`，场模型 schema 固定为 `complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1`。大小写准确的 source role 是 `frame_C1`，模型键是 `normal_frame_C1_reuse`。

新完整执行体如下，每份均小于 100000 字节：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `reference_centred_c1_smooth_triangle_seed_angular_jet_error_bounds.py` | 49032 | `a7f1862362d729f29fba2b41ad040a5961b8cedb5eb729d8d6bbdc5bc36120c9` |
| `reference_centred_c1_smooth_triangle_accurate_mean_residuals.py` | 40325 | `62cb9d143d820b71c2863752b6e29349e996cdcf571bc88b2600f789a43d5702` |

完整再生器 `derive_reference_centred_seed_fee_adapters.py` 的本次版本为 `05c5d3ee6cd2b4238ebe9cca15a7a0b70a725bb9b8815d11f7dc25fb711f7185`。它先核原两份完整数学源，逐份核新 driver / reader / field / calibration 完整字节，再核 driver registry、三层 schema 和 field 的 C1 helper pin，并读取核对同一 C1 helper 全文摘要。它不会 import 任一科学模块。

同一再生器仍支持原 `reference-centred` 变体。实际纯文本重新生成后，两份 plain 执行源分别仍为 `ded2f37b2cccd98fff1b812e79013301cc04cc5bc34c3629e068cfc859727b11` 和 `7596defae9f81580c9db4e7ff593b98825843dcb9d16d73bc798d2be279ffd74`，字节未改。旧 plain 消费者仍拒绝 cached 模型。

## 3. 同一个实际报告、冻结参考与 C1 定义

新消费者首先运行其完整 byte-bound cached pure reader。该 reader 逐角色核真实文件摘要和报告来源，核完整 canonical 模型，并读取 C1 helper 中明确选定的 stdlib policy 定义与计数键；这一步不执行 F、J、normal 根、积分或区间科学运算。

随后 `bind_outer_report_scope` 独立核 cached source / schema / model identity、calibration 定义和原冻结参考点。原初点摘要必须同时等于该报告的实际原 reference 初点与 centering 定义中的初点；base 和固定 seed identity 必须一致。当前 outer 自由点不会被重新选作新的参考点。

cached 附加检查要求：

- source registry 的 `frame_C1` 与完整 helper 字节摘要一致；
- 模型中的完整 `normal_frame_C1_reuse` 与 pure reader 的完整 definition 相同，且 canonical identity 相同；
- 一次完整外参数导数、所有原 normal 阶段及隐式矩阵保持；
- 没有 root、stage 或 control 自由量被删除；
- pure reader 不声称实际加速或舍入证书。

这里只记录 C1 定义归属。C1 scope 的命中次数、同图缓存、局部零模板和计时不会降低准确 seed 费用，也不会成为更强精度断言。缓存只支持完整一次外参数 J / J*；本适配没有把它解释成外参数二阶 Hessian 接口。

新增完整 outer attribution 保留报告 schema、完整场模型摘要、operator / calibration / C1 来源、centering 定义摘要和原冻结初点摘要。fee request 还须逐项匹配原 report 摘要、seed、raw batch、fixed scalar / chart、实际 batch index 和全部 literal angle 顺序。来自另一报告、另一表示、另一 batch 或另一已选参考点的请求均不能改标签消费。

## 4. 实际 batch 与完整准确积分

原 `bind_actual_batch` 的全部 raw 责任保留。只有 provider 真正记录为完成的 batch 可被选择；captured 原报告中的 batch 列表须与完整 pure reader 输出一致。raw NPZ 在 runner 上按完整摘要核对，读取后再次核报告和 NPZ 摘要。九个向量 jet 数组、六个标量 / moment 数组、dtype、shape、有限性、seed identity 和原 angle 顺序不省略。显式新文件路径只能定位原字节，不能换候选。

实际静态 AST 比较保留了 R713 原 33 个数学 / 工具顶层函数与 Interval 的全部 15 方法；变动仅在报告 binding、main 的请求 / 输出归因以及新增来源核。准确 mean producer 的 ActualMeanBatch 全部 14 方法、CompleteLeafJournal 全部 10 方法，以及原 14 个非 main 顶层函数 AST 相同。

因此准确 mean producer 仍采用完整四段标量 law、准确 affine 节点和所有支持 / 端层边界；补集和准确尾全部保留。实际 candidate 是该 batch 的 $v,v_\phi,v_{\phi\phi}$ 原字。中央项仍是准确 mean 方程定义的 $L_cv$，并不冒充用工作 $\widehat\lambda,\widehat d,\widehat w$ 逐节点求得的中央积分。

新 journal schema 和实际 binding 固定该新 producer / consumer 的完整来源及原 batch。原哈希链、完整 leaf 覆盖、自然预算返回和后继续接语义不改；精度目标未到不能误报已到，完整外包也不会因为目标未到被称无效。旧 journal 不会被当作新来源计算的证据。

## 5. 费用支付的分层

R713 消费者继续准确计算中央 profile 全部片段的绝对矩、Taylor 余项和 $A,A',A''$ 区间，再结合完整外部输入支付参考角 jet / node 的条件误差。准确 mean producer 明确保留 `profile_moments_computed_here=false`，由独立 R713 消费者支付这些中央矩费用。

以下量仍分开记录：准确 mean 方程 residual、provider 实际参考场及其 profile 费用、outer normal 原胞 Gauss / cumsum、冻结的工作参考差额 $\delta_{\rm ref}$、当前全部 normal 根及跨段隐式角 jet，以及当前 raw closure lift 的完整六个物理 jet。

新输出明确保留：

- `fixed_seed_reference_fees_only=true`；
- `numerical_raw_reference_calibration_paid=false`；
- `complete_outer_normal_root_and_implicit_error_paid=false`；
- `complete_R715_physical_lift_and_sixjet_error_paid=false`；
- `outer_history_or_field_certificates_transferred=false`。

这些不是新增完成门，而是当前两源实际职责的边界。要把参考误差接成整个当前场的准确界，仍须支付真实 outer 节点 / 归约误差、完整 core inverse、当前 normal-chain 根 / 隐式误差，以及 R715 的 $h,h',h''$ 传播。C1 模型保持工作径向 Gram 真实读取；不会由缓存、参考中心化或小工作 residual 得出恒等径向度量。

实际 batch 中的有限角费用也不是整角覆盖。要得到全域结论仍须有相同场的完整连续覆盖和其他几何责任。本次没有运行此类昂贵证书，也没有把来源一致性冒充数值余量。

## 6. 可复现完整来源与后续 Actions 接口

源再生只需完整已刊原数学源和本合同指定的 cached 完整源目录：

```text
python derive_reference_centred_seed_fee_adapters.py
  --repo <complete-source-checkout>
  --variant reference-centred-c1
  --entry-source-directory <complete-cached-entry-sources>
  --outdir <scratch-new-complete-source-directory>
```

这是纯源码再生，允许本地静态执行；实际费用计算必须在公开 Actions。科学输入要等真正完整 batch 返回后才指定 `--report`、`--batch-index`，必要时 `--batch-arrays` 只重定位相同 raw 字节。未返回的 source / report / batch 摘要不预填。

准确 mean producer 的完整 CLI 保持原五份 reference 输入、`--repo`、`--report`、`--batch-index`、独立 `--outdir`，以及显式预算 / panels / precision / width-goal / maximum-transitions。全覆盖完成后才提供该新 schema 的 fee request；未完成时只保诚实完整 journal 与状态。

随后同报告和同 batch 的新 R713 消费者接 `--fees`、独立 `--output`，保原 `--precision-bits`、`--taylor-order`、`--profile-series-order`。完整原始数组、逐叶结果和费用报告留在 runner；公开紧凑身份、实际覆盖、必要标量与恢复参数，不复制可重算 raw。

## 7. 静态核查记录

两份完整源已经实际执行 stdlib AST / compile、重复 literal key / keyword、尾空白及 100000 字节限制检查。再生器核对了完整来源闭包，并记录上述逐函数 AST 保留。没有 scientific import、真实 batch 消费、积分、区间求值、F/J、normal 求根或新 fixture。

可重算的 2730 字节 source-lock 输出摘要为 `1dd51300e812578e540945fb6cdccc840dcdab7e9d82548dc188c3a588447570`。该生成表不需要另存公开副本；完整来源和参数已在本说明及再生器中保留。

本说明不把未来 cached 运行结果预先填写为成功；也不以等待本消费者付费为理由延迟完整新求解入口。

## 8. 发布前 reader 来源纠正

construction 在完整 `read_report` 自审发现初稿8b5的一处模型 schema 比较仍写旧plain literal。最终3803版只把该比较改为本文件准确的 `OPERATOR_SCHEMA`；其余六份科学执行源字节不改。该错误未被归因为实际科学失败，也没有通过放宽 schema 接受未知来源。

本费用适配同步只更新 cached reader 的完整 pin，以及由此导出的两份完整文件来源；原数学、积分和journal方法全不变。此前 cb713 / 6e25 是未引用备份，最终应使用本说明表列的 a7f186 / 62cb9d。完整新 `read_report` 的来源闭包与模型检查已逐段复核，旧plain schema literal 不再残留于该新reader。

## 9. 根代理的独立纯源码再生

root完整读05c5再生器与本说明，使用实际公开68bf修正后的3803 reader及其他完整源分别重生plain和cached两个变体。plain仍逐字ded2/7596；cached逐字a7f186/62cb9d，完整source-lock摘要1dd51300与本说明一致。原Interval15方法、ActualMeanBatch14方法、CompleteLeafJournal10方法和其余数学函数AST全保；这只是stdlib文本/AST核查，没有import科学模块或生成任何科学费用。可重算的source-lock留scratch，未复制入Git。新独立envelope若改变driver/reader，仍须绑定自己的实际完整来源，不能沿用本合同冒名消费。
