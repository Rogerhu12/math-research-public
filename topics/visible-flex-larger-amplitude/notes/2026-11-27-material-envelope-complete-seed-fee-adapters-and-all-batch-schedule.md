# run07 完整材料包络入口的固定 seed 费用适配与全实际批次调度

## 1. 本次交付及未执行范围

本次把已刊完整 cached 费用源 a7f186 / 62cb9d 独立适配到当前实际准入的 cc0a073 / b93af98 / 104e014 材料包络入口。物理算子 a62c245、中心化 helper 3e478bb、C1 helper ba3d68f、固定 R711 seed provider 0d09ca4 和 mean kernel f8487df 均不改。旧费用源、旧 request / journal schema 和旧来源守卫原样保留。

另给一个完整 all-recorded-batches 调度源。它在公开 Actions 中读取届时真正存在的完整 cc0a 报告，选择其中**每一条实际完成的 provider mean batch**，保留该批全部 literal phi 的原顺序和原数组摘要；不会预设“第 0 批代表全部角”，不会把任意几个点当作全量费用。

本次只做完整源再生、AST / compile、来源与接口文字核对，没有 scientific import、F、J、normal 求根、积分、区间求值或 fixture。未假设 run07 已返初场、已完成任何 mean batch 或已支付费用。下文保留准备时的完整参数身份；root 已把同一完整费用步骤接在 run07 已准入的科学与纯读取步骤之后，准入不等于返回，不是正在运行求解入口的前置条件。

## 2. 全部完整小源与来源身份

| 文件 | 字节 | SHA256 |
|---|---:|---|
| derive_material_envelope_seed_fee_adapters.py | 15545 | ea455f58cd621be9f65b0b02e5aa0f284bcc3a3af33546ae8ecb69bfbec15835 |
| reference_centred_c1_material_envelope_seed_angular_jet_error_bounds.py | 53269 | 2859943d522cd764b686112acd0acdb065dc6a893625f4a8e237641caf041d36 |
| reference_centred_c1_material_envelope_accurate_mean_residuals.py | 40496 | ce686a593cd81167167adfda966b423e2d95f1c9ce708f5d7252089baed24f1d |
| all_recorded_material_envelope_seed_fees.py | 27573 | 3feff893d09257748d153f0423e75d64eafe75777933ba85ee67611ce61cad6d |
| material-envelope-run07-all-recorded-seed-fees-ready.json | 5949 | 118b05357be5a9cc318cadbbc3108fd107e80a36ebad0dfd24876dfe4daed163 |

再生器实际核对的完整父源为：

- consumer a7f1862362d729f29fba2b41ad040a5961b8cedb5eb729d8d6bbdc5bc36120c9；
- producer 62cb9d143d820b71c2863752b6e29349e996cdcf571bc88b2600f789a43d5702；
- 原完整再生器 05c5d3ee6cd2b4238ebe9cca15a7a0b70a725bb9b8815d11f7dc25fb711f7185。

新报告入口的完整闭包为 cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5 driver 和 104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7 reader；对应 report schema 是 complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1。

物理 field 仍为 a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd，field schema 仍为 complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1。新有限工作政策与物理场身份分开保存，不能用“物理 source 一样”绕过不同 driver / memory / geometry 的完整检查。

新包络 source 逐项固定：

- memory c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152；
- rows 729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7；
- geometry bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f；
- calibration 3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991；
- C1 ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9。

这些身份由完整源字节读取核对，不通过模块别名、旧 schema 改标签或复制旧 metadata 通过。

## 3. 数学主体与完整 journal 的实际保留

完整再生器逐体 AST 检查结果如下：

| 比较范围 | 完全相同 | 允许变化 |
|---|---:|---|
| 原 consumer 顶层函数 | 34 | bind_outer_report_scope 的新政策归属、bind_actual_batch 的准确新 reader 路径 |
| 原 Interval 方法 | 15 | 无 |
| 原 producer 顶层函数 | 15 | 无 |
| ActualMeanBatch 方法 | 14 | 无 |
| CompleteLeafJournal 方法 | 10 | 无 |

consumer 新增 bind_material_envelope_attribution。它核真实 source roles、完整政策定义、实际 snapshot、完整 pure reader 返回的相同政策和当前 carrier；不会用筛查成功代替费用，也不会要求尚未执行的 scan 被写成 complete。原 pending / partial 状态由 104e 和 c79 原 validator 准确解释。

因此原 R713 中准确 profile 全片段矩、Taylor 余项、角 jet 误差公式，以及原 whole-scalar 区间、完整边界层 / 补集积分、准确 affine 分割和无穷尾、原 journal 原子全叶转换均保留。准确 mean producer 仍包围

$$
L_c\widehat v+B(N\widehat v)-K
$$

及其两阶总角导数。它不是把工作 lambda、d、w 在任意选出的几条径向节点上积分后称为准确 mean 方程。中央 mean 项仍是准确的 Lc v。

新 request 和 journal schema 独立。旧来源的 journal 不会变成新 source 已付过的证据；全部 raw 仍在 runner，公开只保完整小源、参数和实际摘要。

## 4. 如何选择真正的完成 batch 和原工作字

准确位置是原科学报告的：

latest_operator_metadata → base_complete_metadata → fixed_supported_unit_seed → mean_batch_records

每条记录必须来自 provider 的成功完整 mean 调用，并实际带 runner_raw_arrays。完整 104e reader 先绑定报告所有来源、模型、seed、固定标量、中心化、C1 和包络责任；captured 报告字节摘要必须与 reader 读到的摘要及之后磁盘摘要相同。再从对应原 NPZ 读取 seed_model_identity、phi、九个向量 jet 数组和六个标量 / profile-moment 数组。

每个向量的形状是 actual-angle-count × 3，每个标量是 actual-angle-count；全部是有限 binary64。phi 的每个 float.hex 字须逐序等于该批原 literal_angle_hex。读完全部数组后重核原报告与原 NPZ 摘要。显式 array override 若使用，只允许重新定位完全同一摘要的字节，不能替换候选或挑选子数组。

新的全批调度先严格列出报告中所有完成记录，不预填批次数。它还核每个 raw 文件的完整字节数 / 摘要，并核原 provider 只登记此前未缓存的 literal 角，因此记录的完整字集合不重复，和实际 completed_literal_angle_count 一致。原 provider 计算失败时只剩失败记录或尚未成功的角，不会被虚构成已完成批次。

若完整报告没有可消费的完成批次，调度给真实空计划、complete=false，不把 vacuous all 当已付。若只有部分角的 batch 成功，可以支付这些完整实际批次，但输出明确只覆盖所记录集合；不能据此称失败或尚未请求角已付，也不称全连续角覆盖。

完整失败归因直接来自已锁 `104e0140` 纯读取器的真实字段：`last_recorded_seed_failure`、`last_seed_failure_phase` 和 `last_seed_failure_reason`。调度 binding 保存完整已记录失败对象及其 phase/reason；公开 summary 只取存在性及两个标量字段，完整失败记录继续只留 runner。实际无 diagnostics 时三值均为 null；已有 diagnostics 的三个键必须真实存在，不用不存在的 `last_failure` 静默补空。该修正仅闭合失败来源，不改变 mean/profile 数学、批次集合、原 child argv、费用预算或任何完成条件。原数学 adapter 与完整 deriver 字节保持表中原身份；未执行科学计算。

## 5. 全批自然预算与恢复

准备参数把一份真实报告冻结为本次输入；调度绑定包括该报告、五份完整 reference 输入、全部 batch 文件与 metadata、全部角字序列及其摘要、seed / model / target / policy 身份和准确费用参数。任何字段或原文件变化都要求独立新输出，不能把另一实际报告接进旧 journal。

默认执行模式 complete-recorded-batches，准备参数为总自然预算 600 秒、每批自然量子 60 秒、panels=128、precision_bits=160、width_goal=1/100000000、taylor_order=48、profile_series_order=48。这不是有限小样本：所有实际批次在完整计划内，轮转读取，同一 outdir 中各批的完整径向 journal 可以继续。

每次 producer 返回后，调度只在完整初始径向覆盖已经实际完成时读取它产生的 fee-request；随后独立运行 R713 consumer，支付同批所有实际角的完整 profile / mean-jet 费用。请求缺项、不一致或当前准确界不足会实际失败，保独立原 stdout/stderr 和失败状态，不填零，不改阈值，不冒物理不存在。达到当前 width_goal 而同一准确请求不能消费时，本次不盲目重复相同失败请求，仍保其他批次与未解决责任。

全调度 complete 仅表示每一个已记录实际批次都有一份真正完成的准确 mean / profile 费用结果。它与 all_width_goals_reached 分开；达到或未达到请求宽度都不是当前场的完整证明。已有同批完整有效费用结果不会因后一次更窄 refinement 尚未完成而被虚构消失，全部输出及其各自请求摘要保留。

时间预算为自然返回边界。单个完整叶、source setup 或 consumer 不因超时被掐断；故总壁钟可以超过所给预算，不称硬上限。调度异常或进程中断若留下尚未写入 state 的完整 child / journal，默认 fail closed，不把 orphan raw 自动认领成已付。正常自然返回后同目录恢复必须逐字保同 binding、已记录 producer / consumer 文件摘要。

输出命名空间在初次 binding 后对原报告、五输入和所有实际 raw batch 一次检查：任何输入位于新 outdir 本身或其子树都拒绝。各 child 日志与 conditional output 使用新序号，不覆写原输入或已有原科学输出。全部控制仍公开 Actions，科学 source、完整 child argv 和每次返回文件摘要保存在 runner 的总 report。

## 6. 目前真正缺少的实际 node 工作字与误差输入

a7f1 / 62cb 的原准确 mean producer 对每角生成 nodes=[]；本次保留这一真实责任边界。单凭 mean NPZ 的 v、d、w、lambda 及其角 jet，不含任意 actual radial query 的 T、Tphi、Tphiphi、Ts 全部工作字。

原 6a803 base 的 _parent 对 integration / grid 标签可以在 runner 写完整四 jet 的 replaceable NPZ cache，但原 metadata 不把这些缓存逐一提交成带全部 query 地址和文件摘要的不可变证据；任意 point 标签的四 jet 也不保证逐次落盘。文件名仅由 label 和 literal phi 形成，不能独立代替完整 query / producer / 当前实际输入绑定。因此本次没有把“可能有缓存”写成已经获得全部节点工作值。

要支付某个完整请求节点，仍需明确：

- 同一冻结 seed、原完整 report / batch 和 literal phi；
- 实际 cell / u 或准确 affine s 地址、相应完整 query 来源；
- 原实际 provider 的 T、Tphi、Tphiphi、Ts 四个工作向量；
- 准确 scalar、固定 chart、cutoff / cutoff_s、中央 profile 坐标及 region 分支输入；
- 对真实 working 节点和准确符号节点的全部 carrier / 运算差额。

bound_reference_node 会逐项消费这些完整输入，而不是默认缺费为零；现在没有供入，所以所有 requested_nodes 仍明确为空。取得这些节点责任需要独立受检的完整 producer / 缓存绑定，或在公开 Actions 按完整声明重新计算真实工作值。不能在本地偷算，也不能把新重读值冒成先前未记录的字节。

## 7. 当前 normal / calibration / 物理六 jet 并未由本层支付

即使全部记录的 mean batch 都实际完成准确费用，仍不包括：

- 完整连续 phi 胞覆盖；
- 当前自由点的 normal-chain 根和所有隐式参数 / 角导误差；
- 冻结工作参考差额 delta_ref 的完整 outer 节点 / Gauss / cumsum 费用；
- 当前 raw closure lift、core inverse 和 F 的全部六个物理 jet；
- 全域 metric、reach、D/L、嵌入或所有 t 的几何证书。

本次保持下列输出为 false：actual_node_jet_fees_paid、continuous_phi_cover_paid、raw_calibration_and_current_normal_chain_paid、complete_physical_sixjet_metric_geometry_paid。consumer 也保 numerical_raw_reference_calibration_paid、complete_outer_normal_root_and_implicit_error_paid、complete_R715_physical_lift_and_sixjet_error_paid 为 false。

R715 小 centered residual 与 raw Delta 的差别仍按完整已刊公式处理；物理 Fs 的 hprime Delta 和 Fss 的 hsecond Delta 不会因为参考中心化或 C1 缓存而消失。本次既没有从工作 residual 猜严格误差，也没有宣称原求解误差停滞的原因已经确定。

## 8. 准备的 run07 全量参数与实际执行条件

完整 JSON 从已经准入的包络 entry ready 逐项复制五份真实输入路径：

- axisymmetric-R690-reference-v2-first/reference.npz；
- 同目录 observations.npz 和 report.json；
- fullclosed_solver/data/fullclosed-hold-warm.json；
- fullclosed_solver/data/pulse-a5-complete-base.json.gz。

目标实际报告路径为 reference-centred-c1-material-envelope-normal-lift-first/report.json。它必须在 runner 真正存在并被完整 reader 接受；参数没有假填未来报告摘要或完成批数。controller 的 parent_bundle 使用实存 reference，故不以“有 final.npz”掩盖初场失败报告的可读性。

总入口只有一个完整 step，所有批次及每个 child 的完整参数由严格绑定的 source 真实生成。所列完整 ready 文件保存准备时字节，不回填未来结果；实际活动队列已追加同一完整 step，并把 scope 明确记为已准入、尚未取得返回。原四个完整队列对象逐值保留，不挡主场求解。

公开 summary 只列真实 source / model / seed / policy / report 摘要、实际批数角数、全角序列摘要、覆盖数、实际 children / 时间、complete 与明确未付标志，不输出逐角 jet、矩阵、逐叶区间或可重算数组字符串。

本交付是一条来源与实现适配记录，不新增重复数学编号，不把完成 source 或预算退出当作课题完成。


## 9. root 独立复核与实际准入记录

root 逐字读过完整再生器、调度器、全部来源适配与本说明；对原 104e 纯读取器真实失败字段的交叉检查发现旧 scheduler 的 `last_failure` 错键，正式交付使用上表已修正的完整 revision2。完整失败对象、phase 和 reason 均从实际字段取得，不静默抹去已有失败。

root 实际在 scratch 仅运行已全文审核的 stdlib 源码再生器：新 consumer 53269B / 2859943d 与 producer 40496B / ce686a59 均与交付完整字节相同。34个 consumer 函数、15个 Interval 方法、15个 producer 函数、14个 ActualMeanBatch 方法及10个 CompleteLeafJournal 方法的原数学 AST 保留；两处 source binding 与新增 attribution 明确另核。这里没有导入或求值科学数组、区间、积分、根或 fixture。

活动 run07 `45909290354/1` 的完整参数队列在原科学 step 与纯读取 step 之后追加 `all-actual-material-envelope-seed-batches-complete-mean-profile-fees-first-20261127-07`。全部原五输入、每一实际记录批、全 literal 角、原费用参数与600/60秒自然预算均按完整源执行；没有预填尚未返回的 report SHA、批数、角数或费用成功。若完整输入不可读或数学消费失败，按真实失败继续处理；若只是完整径向覆盖尚未完成，则据实际 journal 接续，不将预算退出冒称完成。
