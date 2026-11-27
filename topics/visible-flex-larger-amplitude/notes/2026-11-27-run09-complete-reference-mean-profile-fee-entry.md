# Run09 实际参考的全批均值与剖面费用完整入口

## 1. 本次交付及执行边界

本次交付三个独立完整源码、一份完整源码再生器和一个完整 Actions 参数对象。它们消费 run09 修正后 `ff5444af…` 科学报告及 `aee22caf…` 全体纯读取器所验证的实际输入，继续使用已刊 R709、R713 的准确均值方程、完整径向积分日志、十二段光滑三角剖面矩和实际二角 jet 误差公式。本次没有执行这些科学入口，没有读取或制造尚未产生的均值批次、根包、数值费用或场成功。

原 run09 actual4 的 `e3cb0f5a…` 在几何构造器的 `original`／`selected` 来源字段不匹配处退出；actual5 因其报告未产生而退出。actual6/7 已用真正原日志确认这一来源接口错误。本入口只接受完整修正后的 v2 来源，不把旧 actual4 的 command 文件改作场报告，也不假称 v2 首场已经成功。

全域研究完成标准、原全部变量、当前自由 core/H、三组 SO3 系数、32 个法向阶段、所有原几何与幅度行、固定目标与永久位置责任均由已排科学入口继续承担。这里计算固定参考层的费用，不修改求解器，也不作为它的准入前门。

## 2. 当前参考与历史位置载体必须分开

run09 的实际准备阶段由完整 `4e65577d…` 返回。其完整参数和小卷记录见 `notes/2026-11-27-public-actions-45943410994-1-part-001.md`：

| 对象 | 实际 SHA256／事实 |
|---|---|
| 当前 reference.npz | `2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2` |
| 当前 preparation report | `4cc93d406cc1882771d2ebabb34856e7ed195fb6cdb6b361e1b213e504193ad2` |
| 当前 observations.npz | `792a132357861684ae01b15b2276c0259583ef27c44387288f424e08d6b488bb` |
| 当前完整 reference model | `d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75` |
| 当前固定 chart 完整数组摘要 | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |
| 当前准确标量准备 | 实际 1995 个完整尾部积分叶；`scalar_tolerance_reached=false`；完整无限尾没有删除 |
| 实际公开输入冻结定义 | `7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a` |
| 实际冻结输入完整文件 | `2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d`，430906 B，只留 runner |
| 历史位置载体 | 由已刊 `9e3d0590…` 按真实旧 2397 叶重新构造，要求整份旧 dc5 文件字节命中后才使用其材料地址 |

当前准备报告中的 1995 是实际返回事实，不是新增数值截断参数。新绑定从当前完整准备报告真实读取 `true_scalar.integral_leaves`、其准确宽度及容差状态。它不把叶数当作严格误差，也不把 `tolerance_reached=false` 改成成功。

2397 是旧载体恢复器已经明确绑定的完整历史再生输入。旧载体用于旧材料位置索引与完整历史责任；本费用程序不拿它的旧 $a$、$R$、$H$ 或旧误差表替代当前参考值。准确积分使用当前 `reference_definition.radius_complete_enclosure`、当前全部固定 core 字、当前种子 H 字、当前完整标量 profile、全部准确仿射节点以及当前支持区定义。当前与历史 chart 摘要相等，不自动形成跨目标数值或已支付费用等号；保留实际冻结合同的 `same_mathematical_g_claimed=false`。

## 3. 完整来源与跨对象等号

新 consumer 的 `bind_run09_reference_attribution` 在已有全体纯读取器之后再次闭合实际参考责任：

1. v2 driver／reader、normal／calibration／C1、当前 memory／rows／geometry 使用真实完整源码身份；原 `envelope_memory=c79…` 仍作为历史依赖保留，当前消费者明确使用 `independent_envelope_memory=25181333…`，不把两者换标签。
2. 报告中的完整 target 与实际 `historical_address_binding.actual_path_binding.fixed_target_definition` 逐对象相等，其 canonical 必须是真实 `7c766f…`。实际纯读取器已验证的 target 身份和返回对象也必须相等。
3. target 中完整当前 reference model、报告 `representation.base_complete_model.complete_axisymmetric_reference_model` 和固定 seed 中完整 reference model 逐对象相等，canonical 必须是实际 `d4494b…`。whole reference SHA、base/seed 的 reference SHA、target 和纯读取器的 whole reference SHA 全相等。
4. 全固定 chart 数组摘要在 target、reference、base、seed、纯读取器中相等。160 个字的真实重读由完整原输入／memory／纯读取链承担，不从单个 chart 标签猜出字值。
5. 当前 warm、node report、scalar input、carrier、preparation report、reference bundle 六个完整文件，都与实际公开输入冻结对象中的完整记录相等；真正 `2f8…` 输入冻结文件也保留完整 bytes/SHA。每个子程序调用的五个科学输入继续与本报告原字段逐项绑定，不能指定旧 carrier。
6. 当前 preparation report 捕获一次完整 bytes，核真实 whole SHA／大小后解析；其完整 model、标量定义、完整尾部标志和实际叶数与当前 reference 相符。对全部六输入及冻结文件在绑定前后再核字节。调度器在每次子调用返回后继续重核同一组文件。

这条额外来源链不生成均值根或表格，不能把来源验证结果称为连续场认证。准确 current radius 盒也只是完整公式的一项输入，不是原始 float radius 自动获得的严格界。

## 4. 已刊数学主体完整保留

完整数学依据来自：

- `results/R709-global-convex-mean-closure-without-contraction.md`：准确总均值方程及其必要的正性／全局解责任。
- `results/R713-exact-smooth-triangle-moments-and-actual-fees.md`：全部十二段剖面的精确矩、实际工作字与准确量之差、均值根和两个角 jet 的完整费用。
- `notes/2026-11-26-R713-smooth-triangle-actual-fee-consumer-api.md`：每个实际 batch 的完整输入／缺陷合同。
- `notes/2026-11-27-material-envelope-complete-seed-fee-adapters-and-all-batch-schedule.md`：原完整 mean producer、费用 consumer 及全批调度责任。

新 producer 的 15 个顶层函数、`ActualMeanBatch` 的 14 个方法以及 `CompleteLeafJournal` 的 10 个方法与 `ce686a59…` 逐 AST 完全相等。新 consumer 的 34 个未改顶层函数和 `Interval` 的全部 15 方法与 `2859943d…` 逐 AST 完全相等；变化仅限真实来源／输入绑定的三个旧函数和两个新增只读绑定函数。

准确积分仍按真实 $s=\lambda S+\eta$ 节点和完整支持切点建立全径向分区，中央段按准确 $L_c v$ 支付，补集与所有边界段用完整标量／单位参考／归一化三角 jet 的向外区间计算。初始完整分区没有全部返回前，不发布准确总方程缺陷。细分只以两个完整子片替换整个父片；不以区间减法伪造已支付积分，不丢未分辨的无限尾。

当前候选 $v,v_\phi,v_{\phi\phi}$、$d,d_\phi,d_{\phi\phi}$、$w,w_\phi,w_{\phi\phi}$、$\lambda$ 的三个 jet 以及三个实际 profile moment 工作字，全部来自本报告实际记录的同一个原始 batch NPZ。保留原 shape／dtype／finite／seed identity／所有 literal phi 原序和前后 bytes SHA 检查。实际工作残差不能替代准确总方程的三个缺陷界。

R713 的精确矩和各导数级数逐体保留；误差需支付真实工作矩字与准确矩之间的差，以及准确均值解、单位方向、长度、lambda 和全部角 jet 的参数移动。没有重新求工作均值根，也没有把旧批次的实际值视为当前批次值。

## 5. 全实际批次调度，而非挑选角点

调度从一个完整不可变的 v2 报告获取 `latest_operator_metadata.base_complete_metadata.fixed_supported_unit_seed.mean_batch_records`，与全纯读取器返回的完整批次表逐值相等后，按原记录次序消费每个实际完成批次。所有字面角、包括任意永久点首次触发的角，都保留；不指定 batch0，不抽样，不跳过昂贵角。

每个 batch 的 runner raw NPZ 必须真实存在且 whole SHA／大小与实际记录相符。所有已录角的顺序、唯一性、完整完成计数保持原 provider 合同。没有 batch 时明确返回没有已录完成批次、`complete=false`；有失败 batch 或未记录角时，保留实际最后 seed failure、phase、reason，不把缺失当作零误差或成功。

每批原完整径向 journal 可续算；不同报告字节、source、current target、批次、全部 angle words、精度或参数不能借用该 journal。调度器每次从未完成批次继续轮转。完成初始全径向覆盖后才把真实 fee request 交给 R713 consumer；达到自然时间预算后，返回真实完整／未完整状态。600 秒不是全费用必定完成的承诺。

新调度器的 16 个既有函数逐 AST 相等；四个变化函数只增加完整09来源绑定、完整输入重核、producer／consumer输出与同完整来源对象的严格等号。原主循环、参数解析、子调用命令生成、自然预算、轮转、失败记录与完整状态逻辑均保留。

## 6. 明确尚未支付的责任

本次单步只计划支付所有实际已记录均值批次的准确总均值缺陷及固定光滑三角剖面费用。它没有提供 requested nodes，因此每角 `requested_nodes=[]`，节点费用仍明确为 false。保留原 `bound_reference_node` 完整数学函数，不调用它来假称已有实际节点工作字。

这个 finite literal-angle 结论不等于 whole-angle cell：未提供角区间覆盖；也未支付当前 raw reference calibration 缺陷、32 个 normal stage 根盒、原 endpoint 复读误差、完整隐式 3／6／9 系统、物理六jet、metric、reach 或全域嵌入费用。新的 analytic frame／J3／C1／packet 来源被完整归属，但“已经使用解析公式”不是浮点误差已付的证明。后继 normal/root/sixjet producer 必须消费同场的真实包、实际工作字、准确积分和全角／全径向责任。

不能将 `mean_covers>0`、单批 consumer `complete=true` 或 `all_recorded_batch_mean_and_profile_fees_complete=true` 改写成研究完成。后一个标志也只指这份不可变报告中真实记录的全部已完成批次；未记录或失败的批次继续明示。

## 7. 完整源码与实际静态检查

| 独立完整源码 | bytes | SHA256 |
|---|---:|---|
| `run09_reference_seed_angular_profile_error_bounds.py` | 64824 | `7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1` |
| `run09_reference_accurate_mean_residuals.py` | 40771 | `17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820` |
| `run09_all_recorded_reference_seed_fees.py` | 29133 | `0c7efa0726aa27dbde769a8cce7615efc75e1676b49cf3c2602767b8543d915f` |

完整再生器 `derive_run09_reference_seed_fee_sources.py`：28758 B，SHA256 `f9d1098c6c508a1476d854fa3288629e675daccf37eaf93be914f9e55a9910c9`。它读取完整已刊三个父源，核 v2 全部 58 个实际依赖角色，严格再生三个完整体；源码纯 AST／compile、重复键和尾空白检查已实际完成。没有导入科学模块，没有执行浮点／区间算例或构造替代 fixture。

完整源码派生记录在 `run09-reference-seed-fee-source-lock.json`；保留全部 source contract、原父 SHA、每个完整输出字节数与摘要、逐类逐函数 AST 对比和无科学执行字段。原三个完整源不修改、不覆盖，不称原源码已支持这些新 target／memory schema。

## 8. 完整 Actions 参数

参数文件 `run09-v2-all-recorded-reference-seed-fees-ready.json`：9190 B，SHA256 `41ac4eb37bd4b5dc6c66505940e629155408769f20eb3d1db0544d771074e859`。一个完整步骤，32 个参数元素，48 个标量 summary；完整对象紧凑序列化为 5707 B。所有实际数组、逐角费用、完整科学日志和 journal 只留 runner；公共 summary 只取来源、计数、状态、准确宽度字符串和 scope，不把数组转字符串发布。

该参数使用原全批入口相同五个科学输入和全部数值参数，仅新的报告／输出目录与新来源不同。实际来源报告预计位置是 `{work}/run09-public-reference-analytic-frame-v2-first/report.json`；其未来 whole SHA 与批次数没有预填。依赖缺失时入口应真实失败，不默默替换为原无报告的 e3cb 或别的 run。

```json
[
  "--repo",
  "{repo}",
  "--report",
  "{work}/run09-public-reference-analytic-frame-v2-first/report.json",
  "--reference-bundle",
  "{work}/axisymmetric-R690-reference-v2-first/reference.npz",
  "--carrier",
  "{work}/axisymmetric-R690-reference-v2-first/observations.npz",
  "--node-report",
  "{work}/fullclosed_solver/data/fullclosed-hold-warm.json",
  "--scalar-input",
  "{work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
  "--preparation-report",
  "{work}/axisymmetric-R690-reference-v2-first/report.json",
  "--outdir",
  "{work}/run09-v2-all-recorded-reference-seed-fees",
  "--execution-mode",
  "complete-recorded-batches",
  "--seconds",
  "600",
  "--per-batch-seconds",
  "60",
  "--panels",
  "128",
  "--precision-bits",
  "160",
  "--width-goal",
  "1/100000000",
  "--taylor-order",
  "48",
  "--profile-series-order",
  "48"
]
```

允许同一真实报告／全部参数／全部 source 再次调用同一 outdir，接续其完整 journal。若后继求解产生了不同报告或新 batch 表，必须作为新的明确输入绑定，不重用原报告身份。

本次交付未改任何 ref 或运行队列。源码发布及是否实际准入由根控制；实际准入不等于已执行，科学结果以真实返回记录为准。

## 9. Root完整独立复核、实际排队与原状态

2026-11-27 07:40:52 UTC，root实际取回全部7个完整交付blob并核整SHA/字节数；完整阅读本note、28758字节再生器、完整来源锁及9190字节全部参数对象。另重新读取三个已刊完整父源53269/40496/27573字节并核SHA，直接逐函数文本比较：consumer原34个、producer全部15个、scheduler原16个函数原字不变；只明列consumer的三个绑定函数与scheduler四个绑定/再核函数改变，新增完整来源函数。Interval、ActualMeanBatch、CompleteLeafJournal的完整类体也原字相同。原数学公式、径向cover及全部实际batch调度没有被换成测试或小实例。

完整v2来源58角色已在root的N09全75-role核查中按实际全文覆盖；新全三体/source-lock/ready与原父身份对应。solver失联前已实际完成stdlib完整再生/AST/compile；root当前环境不可用，**没有再执行本机replay或科学算例**。整SHA、完整函数/类体文本和全参数复核不改称科学执行。

活动09队列现在把这一个完整5707字节步骤放在现有科学、pure两步之后；32个参数元素、48个标量selector全保。原两个pending对象逐对象相等，全部原header/归档证据保留，未把正在运行但未返的步骤归档为完成。完整ready中的executed/admitted=false描述原准备对象，其实际准入以活动队列和本节为准，不回填科学输出。

root已读取真实07:39:44 UTC小索引：v2科学步骤 `complete-run09-public-reference-analytic-frame-v2-first-20261127` 为running、子进程未退出；仅1–7有返回。它确认实际步骤正在运行，不确定首F、求根、几何或性能阶段，也不能据此预填报告SHA、均值批次数或费用。

本次云端head `cbbb7eb83a946762c7e537d6c425e606467edc81` 双README整SHA581402/3c1c无变；最后真实pull仍为eda95d51e82b126439d51d42185a880e6ddad3e9，环境恢复即真实拉取，不把云端源码/参数操作冒pull。原4/5失败、6/7诊断、08/07未知和固定目标责任均保。继续实际完整场、费用和同g精化。
