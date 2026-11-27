# 同一 run10 固定参考输入跨 runner 再生：完整来源与执行合同

## 1. 目的与真实边界

run10 是公开 Actions `45972294636/1`。其真实必要输入于公开分卷记录了完整 warm、参考准备、目标冻结与历史 carrier 重建。本文件提供新 runner 的必要输入生成器。它不复制一次新的随机时间停止参考，也不把当前运行的进度点当作可续 checkpoint。新 runner 的 recipe 仍是完整 `561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4`，`--repo REPO --work WORK --stop-after warm`。它只做原完整 warm 来源链，不重新执行后来的 SO3 优化结论。

新 producer 读取该 runner 真正生成的三个文件：`fullclosed-hold-warm.npz`、完整 node JSON、`pulse-a5-complete-base.json.gz`。不将这些新文件的路径、elapsed、whole SHA 或原始记录改成 run10 旧值。唯一可声明的原数值字相同关系，来自新的真实计算与完整字节校验。

本次仅交付源、原真实完整参数和未执行 ready。没有本机科学 import、F/J/J*、root、标量积分、NumPy运算、fixture、AST或编译；没有改 queue/ref 或正在运行的 job。后续完整 solver 上层另有独立源码，必须消费本桥，不能调用仍硬钉旧 six-file 的旧 binder 假通过。

## 2. 原证据与精确参数

原公开分卷位于 `notes/2026-11-27-public-actions-45972294636-1-part-001.md`，固定 commit `8e32b487661e9ee886f8c4968dcf4d31015e9938`，whole SHA `0b1de8d544053aa5e67f80b144a65274c2f111825845482e68c5c278ef9f7cee`，38,575B。origin 参数保存该卷前三条完整返回对象、全部真实 commands、input/output records、原 public evidence 对象和所有源 identity；是这些紧凑公开对象的新序列化，不冒原卷逐字副本，也不包含科学 raw 数组。

关键固定身份为：

| 项目 | 原实际 identity |
|---|---|
| 固定 target canonical | `e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049` |
| target whole 文件 | `b24080447828d8ffb49ae146dd5672d34bf6f5cec512054633b6f849c2bdabfb` /97,335B |
| 原 public evidence canonical | `47a8fa781713388379a6de4c259f4ddf7f810e1b3d69c63f8630565031b761ef` |
| reference model canonical | `081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5` |
| scalar profile canonical | `c46f875f96a41a09ccad4bcfb75ed6efd33e239b28dbcdb538ce9d2daa47bc65` |
| 全部 scalar 定义参数 | `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` |
| 160 chart 字数组 | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |
| 完整 mesh 字数组 | `eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262` |
| 923准确 affine 节点 | `ba5a3188e048f69b6602b4b784640c70932fbc1f53cfbf13b0857ba25e6b4b02` |
| 完整 reference NPZ | `512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b` /866,207B |
| 全7377观测 carrier | `71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d` /227,202B |
| 旧05完整地址 carrier | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` /227,202B |

当前 scalar live leaves 必须为 **2218**；完整 infinite tail 保留；原 requested accuracy 返回 false。历史地址来源单独为 **2397**，不能用后者代替当前2218。当前 exact integral width 原值完整留在参数与源里。panels128、tail cutoff1/8、requested tolerance1e-18、完整 seed integration8、observation Gauss6、1845 legacy+5532Gauss、M160/J923/P7377/N2048全保。

e711含旧公开 execution evidence 与完整原文件来源，不是仅数学公式的hash。其原 `same_mathematical_g_claimed=False` 是当时对更早历史目标的声明，原词保持。新桥另有 `same_mathematical_g_as_origin_run10_verified`，其含义只指新输入与此完整冻结 run10 定义的关系。

## 3. 确定重建当前2218全表

原 `4e65577d…` 在300秒预算后停止 `e091f675…` 的积分表细分，执行速度可改变 live-leaf count。新入口不重用该时间停止来挑另一张表。它调用完整已刊 `fcd20177…` 中 `counted_tail_class`，继承原 e091 所有 exact scalar kernel。该类只将停止条件替换为已实际返回的2218 live leaves；每片 integer/Fraction interval 运算、max-width heap priority、递增 sequence 破平局、split 次序和所有尾项原样。

固定全参数、初始 leaf 和每次确定 split 后，live-leaf数每次净增1。因此给定实际2218数，逐步归纳恢复同一张原 finite table；如果原 accuracy 条件先到，原类诚实拒绝而不越过该条件。新报告还核原 profile canonical、完整 exact width、原 false accuracy状态。生成的全部 leaves/values/total_integrals exact words 落 runner-only `complete-current-2218-integer-table.json`；只其来源、SHA、bytes、计数进入公开 compact。旧 actual 表未曾单独存档，不能称直接比较了一个不存在的旧表 raw；同表性由完整确定算法和真实 count 解释，全部后续参考输出还需原 whole SHA 真实命中。

## 4. 全参考场工作词再生与 whole 校验

新 warm 的全部10 NPZ成员真实读取。完整qjets布局仍923×3×482；只原准许的 frozen-core projection参与参考构造。完整mesh/chart及前三字和width严核；全部923准确节点由原 bee5 recipe 公式独立构造并与实际node逐项相等。实际node必须指向实际新warm/scalar whole SHA。

准确 scalar 只从原 `FullHold` 确切读取的完整 `analytic_extension_origin` 与 `fixed_scalar_profile.geometry` 投影取值，完整 canonical 必须 e640。原 FullHold/整数/hold/deep/observed/history 源逐whole SHA加载。新raw中的其它metadata不被当成旧raw文件identity。

`generate_carrier` 保留4e原遍历顺序及dtype：7377完整 observation，原 midpoint/error 向上包围、time error、radius，所有正权重/legacy和六Gauss成员。新文件必须 whole71f且227202B。

`generate_reference` 保留4e原完整8点×922 integration 与7377 observation union、原逐地址去重规则、全部4scalar值及4error、原 normalized-c/np.sum 高度公式和完整NPZ keyword顺序。原reference model由真实重生数据和冻结原来源定义构成，明确这是 **origin model**；其canonical必须081。新reference必须whole512f且866207B。故完整原四jet缓存、全部地址、mesh、core、initialH、radius、width、误差和嵌套原model都由原whole包匹配，而非根据若干点或宽容差声称相同。容器/平台字节不一致也会如实拒输入等同性，不能归作数学场不存在。

冻结target由完整原public evidence、实际重生model、scalar参数、160chart字与923节点再组成；原 e711 canonical 与 b240 whole两者都必须命中。新文件明确叫 `origin-run10-fixed-target-definition.json`，原path与run号仍是历史来源，不是本次执行身份。

## 5. 新当前preparation与完整context

新 `preparation.json` schema是 `complete-reconstructed-run10-reference-preparation-v1`，source是本新producer；其全部实际 input_for_solver、warm、node、locations/provenance、execution和seconds来自新运行。它不伪装旧4e prepare执行，也不声称whole35f/whole4ace。

`same_run10_frozen_reference_input_binding.py` 是纯stdlib入口。它核整个e711目标、六当前文件、原primitive NPY类型/shape/所有member payload、完整新raw参数/节点与真实warm关系、完整2218 metadata、两个carrier、当前source/exec与origin分层；最后重hash。返回每个reference member实际payload摘要、实际六file、完整origin/current身份以及未读历史责任。

`reconstruct_same_run10_fixed_reference.from_files` 是显式新constructor。其kwargs为repo/reference_bundle/carrier/node_report/scalar_input/preparation_report/**material_envelope_binding**/panels=128，返回原 `4e.AxisymmetricReferenceContext` 实例。它首先真读上桥，再按原完整from_files所有字段/数组/缓存/FullHold初始化；只有已被全桥替代证明的“当前raw必须等旧origin raw SHA”交界改成明确 origin 对象等号。实际 `input_records` 全是新文件，`model` 是已再生whole包中的冻结origin081。原 `reference_at/create_problem/metadata`、`AxisymmetricMeridianJet` 和所有physics函数保留原4e实际代码文件，旧from_files完全未改。额外实例属性记录完整bridge与新constructor source，solver顶层必须继续保这些源。

这不是将旧guard删掉后调用旧入口：新constructor有独立完整source、schema、bridge、全部数组检查。旧9f69/4e公开源原字不动；solver须用独立完整上层，不可把新的报告冒旧 six-file 的真实返回。

## 6. 历史与13成员续接边界

原完整十一payload package逐原 `add_supplied_locations` 消费、indexed位置用真正重生的carrier解析、protected/roles全留。旧2397/dc5另实算并whole验证，原P0来源不能由计数替代集合。

新桥必保run10未读后续责任，明确 `unknown_history_is_empty=False`、不从状态猜final/typed/terminal。现有完整E策略仍须覆盖同字old/current格与P0；未知typed发现顺序、旧值、旧接受和保护晋升不被伪造。未来真正full report/13成员final与typed只能由严格完整父迁移输入消费。不能从SHA重造final数组；参考重生只是恢复同一固定问题，不是恢复未保存的优化轨迹末点。

本参数尚未填任何新输出SHA、future parent point、future13-member checkpoint、future report或typed列表。后继可在同冻结问题原初点另启明示独立branch，或在真正完整父可用时接严格完整迁移；两者不可混称。

## 7. 交付和执行

完整origin参数：`computations/run10_frozen_reference_continuation_origin.json`，45929B，SHA `d7c6fd9d571542f9c17f3ddc4e7ace589025ca74b69246c45b0c2e4239b8c088`。
纯bridge：`scripts/resume_20261126/same_run10_frozen_reference_input_binding.py`，20775B，SHA `5aee3276dc2c70a3adc52dda618494a8ef458f4b1496c34a5c2640c00a5735b0`。
完整producer：`scripts/resume_20261126/reconstruct_same_run10_fixed_reference.py`，44484B，SHA `5989b2b299d9b6a9bbc2c6bd2ee87f04eb5288ead69bcc4ec6bbb9497b9e40f6`。
完整单步ready：`computations/same-run10-reference-2218-run11-complete-ready.json`，5714B，SHA `1154925fb6b4c8fff8455903d450eb2bd7894e1e57405c6702fe39721e9751d3`。

ready含全部16个argv token、全部10输出记录和36个标量selectors。输出 `{work}/same-run10-fixed-reference`；`preparation.json`是独立immutable输入，最终 `report.json`另存桥文件hash，因此没有报告自引用hash环。参数只有生成规则、已公开真实记录和全部source identity；原数据和新生成数组全部留runner。此步是完整求解必需的固定输入生成，不是额外审查或fixture门。

实际运行未开始，成功与否、耗时、whole输出和同词结论都由公开Actions自然返回记录。任何失败保完整真实error/已产部分报告，不填通过标志。
