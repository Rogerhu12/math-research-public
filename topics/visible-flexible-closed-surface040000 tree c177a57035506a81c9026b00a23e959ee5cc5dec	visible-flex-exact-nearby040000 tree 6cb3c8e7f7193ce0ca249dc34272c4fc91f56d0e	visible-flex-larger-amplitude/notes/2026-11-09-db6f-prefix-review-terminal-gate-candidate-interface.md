# terminal error gate：正常候选接口定向独审

审稿人：`/root/coupled_prefix`，2026-11-09。审查对象为 `scripts/db6f-audit-terminal-error-gate.py`，SHA256 `1be7add52ec2c06653a2a64baa8653e675559a55551cf22603d14a80f9cfb234`。

**结论：在稿件明定的“已经独立审过的完整证书之条件式组合”范围内，正常候选分支的本次定向静审 PASS；没有发现必须修改的 same-g、实际图身份、一次目标转移或完整覆盖 schema 错误。** 未运行正常 candidate 分支，未重复 tail_theory 的真实 M12 负测，没有构造未来 packet/报告或新求解。本审不等于未来候选的正向放行，更不付 G5 或最终独立全流程。

## 1. 同一物理定义允许不同 bridge 支持网格

`candidate` 分别加载 common-cut 的实际 tail manifest 和 exact bridge。新 bridge 必须绑定新 base geometry、同 target；其 pt/ps/L、root box、导数下界、唯一性、arclength rescale 与 phase 等定义字段逐项等于已审 M12 参照。新 prefix 的 frozen_profile、chart、warp_reference、ell 和两个 profile 源哈希也逐项相同。

实际 manifest 的 rCut/wCut 以原 binary 值转 Fraction，与 bridge 的 exact radius/slope/second 相等，最后一个恒等式为 $w_r=-7w/r$。这避免把 `.6` 偷换成另一份十进有理半径定义。

bridge 若引用另一数值 manifest，代码强制显式提供 `--bridge-tail-manifest`，按 bridge 保存的 SHA 读取它与其真实 input checkpoint，再对支持 grid、实际 grid 和参照三者核参数。`parameters` 比较键的存在性及带 JSON 类型的 canonical 值；只有已审政策列明的数值/I/O键允许不同，未知物理键不能以 null 或缺失混过去。

本次只读实际文件确认，这不是未触及的假设接口：M12 的 bridge 支持 manifest 是 uniform `b202b471…`，实际图是 critical `cc23977e…`，两者 parameters 完全相同，三个物理 cut 的 Fraction 恒等式均通过。没有把这份旧支持 manifest 的 metric、曲率、背景 packet 或 nodes 数量用作新实际图的证书。支持 manifest 不必重做其图的连续证书；这里消耗的是其已绑定物理定义和 cut，实际图仍另有完整链。

尾部 six-background mapping、calibration 表、tight alpha、cell-zero/inner-A/outer-B、共同高度与 positive-alpha 记录均固定到真实哈希；完成的 transfer 必须指向新实际 manifest，不允许以 parameter-only preflight 代替。其政策与 source 哈希也固定。允许数值参数改变并不放松这六个 exact-background 定义。

## 2. prefix 的 exact-target 预算恰转一次

原 polynomial 报告和新 angular 报告的 `metric_operator_upper` 均约定为相对 source target 的误差 $\epsilon$。代码取当前 bridge 的 $\eta$，独立用 Fraction 计算
$$
\epsilon_* = \epsilon(1+\eta)+\eta.
$$

原分支要求显式目标路径并按 metric 的 target SHA 读取；angular 分支按其 inputs.target 读取，且 source float 必须精确等于 `selected_source_metric_upper.exact`。angular 已有的两个 exact-target 字段仅用于检查上式相等，**没有作为输入再转一次**。最终还与 closed-budget 和 whole 的 prefix exact 上界核同值。

target supplier 必须绑定新 base geometry、原 frozen_profile 与旧 bridge_constants，数据 SHA 与 metric 同，原 extension guard 为真。common-cut 形成新图之后仍不能拿旧 base 的 metric 报告来过门，因为 metric.geometry_sha256 必须是新 common-cut SHA。

本次另用真实已闭 M12 angular 完整继承记录作 metadata/Fraction 交叉核：source float、source exact、单次转换的两个 exact 字段、whole prefix exact 上界均严格相等。这里只核保存数值及接口，不导入原 angular 后端，不将该旧图当成新 terminal 候选。

## 3. metric、曲率和实际图的身份链

- common-cut 的 geometry、metric、moment 三份报告都必须指向同一个最终 geometry SHA；几何/矩报告的 data SHA 与 base 原数组同。mirror/common-cut/reader/profile/exact-bridge 实现都限定为已审版本。
- 每份 full tail 或可选 metric-only 报告的 manifest SHA 都必须等于实际图 SHA；其 packet、data、row 文件全部按哈希读取，packet 的 finite manifest 和六背景定义也逐项吻合。
- 可选 metric-only 只贡献同图、同背景的另一个完整 metric 上界，并要求其 curvature_evaluated/curvature_certified 都为 false。最终 tail metric 取两个合法上界的 min；曲率仍唯一来自 full metric-curvature 报告。
- prefix 曲率来自这个候选自己的 geometry certificate，tail 曲率来自这个候选自己的 full tail certificate，再与已审固定帽的 $10/3$ 取 max。终门重算 whole metric 的 component max、曲率 max、reach 和 reach/D，并核其 exact 记录；没有搬入旧 M12 数值曲率。

本审对照了相应 producer 的真实字段和生成源码，未见“报告字段名称正确但实际上来自另一层”的正向接口冲突。特别是 angular 完整报告保留兼容的 source `metric_operator_upper`，所以原 closed-budget-v3 的单次转移接口可用。

## 4. 完整覆盖的检查范围

正常分支要求 prefix 几何、metric 均声明完整覆盖；angular 分支还要求 finished、requested_intervals=None、processed=target_intervals、exact_partition_reread_verified=True，并绑定完整 baseline。局部 angular fixture 不具有这些 complete 条件，不能冒充全 prefix。

实际 tail manifest 的 shard rows 按共享端点关系满足 $1+\sum(\mathrm{rows}-1)=\mathrm{totalUniqueNodes}$，且所有 shard 哈希/字节数匹配。tail 报告必须包含 collar、entire_finite_tail_and_collar_covered=True、checked=packet_intervals、total_finite_spans=n 和 selected_span_interval=[-1,n]。此处 -1 是原后端的 collar 索引，n 是末端排他界；与原完整后端的 schema 一致。metric-only 还要求 complete_packet_partition_validated=True。

这些是**对已审证书身份、完整声明和计数的核查**。终门只重哈希绑定的 rows/packet，自己不解码全部行来重证角弧/径向 partition 或重算逐行最大值；也不重证 producer 的解析估计。这不是隐藏的额外证书能力，源码顶层说明、正常输出 scope 与 `independent_complete_input_certificates_remain_proof_dependencies=True` 都保留了这一限制。未来正向结果仍须有每份完整输入证书本身的独立验证，不能凭一个可编辑 JSON 中的来源哈希宣称已重跑后台。

## 5. 实际审查与未实施事项

全文读取目标脚本，重点复核 parameters/definitions/transfer、prefix_metric、tail_certificate 和 candidate；对照了 original/ angular prefix producer、exact bridge、closed-budget-v3 和 whole-v2 生成字段。另只读真实 M12 的两份不同 manifest、bridge、angular 完整记录与 whole，执行十项 metadata/Fraction 恒等检查，全部通过。

本轮 root/flow/solver/interval-backend 调用均为0；没有执行 candidate、负向 CLI、生成 packet/manifest 或伪造未来成功记录，作者源码未改。尾端阈值和严格改善的全文/真实负测由 tail_theory 的互补审稿覆盖；本审不替代该工作。
