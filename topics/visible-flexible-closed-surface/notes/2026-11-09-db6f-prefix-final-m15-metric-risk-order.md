# 最终 M15 前缀：从采样到连续预算的风险与最小诊断顺序

作者：`/root/coupled_prefix`，2026-11-09。**状态：静态接口与条件式分析，不是新候选计算或证书。** 本轮只读冻结源码、已闭报告和现有计划；没有调用 solver、angular root、RK、导出器或几何／metric 后端，没有修改既有闭件。

结论是：现有 [certification-readiness](2026-11-09-db6f-audit-m15-certification-readiness.md) §§3–6 已给出足够的无改码认证路径，**目前无需新增算法或测试**。本文仅补上风险优先级、共同切口修正的一阶误差机制及实际 CLI 陷阱。最终数值优化者之外的端到端复跑另有计划，不在这里重复。

## 1. 先纠正预算所对应的对象

约 $1.30246\cdot10^{-9}$ 来自冻结的 M15 affine-cut predictor。独立 PP 采样得到 $1.302458505758324\cdot10^{-9}$，5399 个径向点、1024 个角点，与作者同网格数值相符；但该文件明确 `actual_nonlinear_tail=False`、`UNSOLVED`。它的保存非均值五次图、数值角均值高度定义也不同于随后正式共享 Cartesian Hermite／镜像／共同 cut 有限图。这个数字不是未来真正 M15 联解的采样值，更不是它的连续上界。来源：[独立采样与 M12 预算对照](2026-11-09-db6f-audit-m15-prefix-sampling-and-m12-budget.md) §§1–3。

因此第一项风险是**真正原方程联解及其最终有限图的误差尚未知**。不能从辅助结果与 $B=2\cdot10^{-9}$ 之间约 $6.98\cdot10^{-10}$ 的表面余量，推断后续认证一定可过。原 shooting／BVP 的 normalized residual、RMS tolerance、sourceFullD、actualXYZ metric 也都不是可互换的量。已有 M14 真联解的非单调结果仍须保留，不能因 affine 的数值较好删去它。

只有最终 CP、它自己的最后 `tail_seam.tail_record`、完整原 DN／seam audit 和 N512 真校正均按原计划冻结后，下面关于“最终图”的条件才有实际输入。本文不生成未来配置，也不把当前延拓的某个内层 success 提前标为该输入。

## 2. 有证据支持的优先级

| 风险／损失 | 已有依据与能推出的范围 | 触发后的最小动作 |
|---|---|---|
| 真联解或有限图的实际误差超过 B | affine 采样不是最终图；入口精确镜像、有限 Fourier、共享 Hermite、common-cut 均定义具体近似。 | 先识别哪个冻结对象／物理区间超标。严格点 lower 若已超过 B，继续细分验证域不能修复该图。 |
| 角相关性被统一分母和 Fourier 范数拆开 | 同一已审 M12 图的原区间 74：原界 $2.57209\cdot10^{-8}$，径向八分仅降约 $0.0673\%$，固定径向盒的 256 角弧降至约 $9.53674\cdot10^{-9}$。 | 若新图的 baseline 超标，优先在**新 baseline 自己的最坏区间**试现有第一档角弧。旧 0、74 只属旧图，不能硬套。 |
| 首段／尾端精确接缝的高模和径向插值 | 镜像改入口 height 二 jet；common-cut 改末段完整 Cartesian 两 jet。二 jet 的小系数可经一阶插值和角频率进入 metric。 | 先读已有 make stdout、metadata 和新最坏区间位置，区别入口、普通内部、cut 修正区；再决定是否需要新表示。 |
| 径向 Bernstein 或目标包宽形成验证平台 | 当前 angular wrapper 保持原径向盒，角细分不消除径向相关性或 target anchor 区间宽。 | 只有局部角细化留下明确缺口，才诊断原多项式的径向限制或供应包宽度；目前不预写新径向后端。 |
| exact-bridge 转移吃掉预算 | 旧同 g 的 $\eta\simeq3.31932\cdot10^{-13}$，仅占 B 约 $0.0166\%$。 | 重建新图绑定并精确转移一次。没有先收紧 bridge 的数值理由，不能直接借旧文件身份。 |

这里“角相关性优先”是已有**同图受控对照**支持的验证顺序，绝非已经证明 M15 必在 128／256 弧通过。M12 两局部 fixture 在预算 $10^{-8}$ 下达到的是所选域目标界 $<9.849832\cdot10^{-9}$，不是整前缀、不是 $2\cdot10^{-9}$，更不是 M15。对照数字来自上引预算稿 §4；局部／完整继承作用域见 [第一档实际运行补记](2026-11-09-db6f-prefix-angular-fixture-completion.md) §§2–3。旧 eta 与目标包宽来自 readiness §5。

## 3. 为什么接缝二 jet 仍须看实际 metric

[common-cut v2 源码](../scripts/db6f-root-common-cut-v2.py) 令 $t=(s-b)/W$，其中 $b$ 是选到的真实旧 mesh 节点，$W=s_{\rm cut}-b$；$W$ 不一定等于 CLI 请求的 0.15。逐 Fourier 系数的修正是

$$
C=H_0(t)\Delta_0+W H_1(t)\Delta_1+W^2H_2(t)\Delta_2,
$$

$$
H_0=10t^3-15t^4+6t^5,\quad
H_1=-4t^3+7t^4-3t^5,\quad
H_2=t^3/2-t^4+t^5/2.
$$

所以

$$
C_s=H'_0(t)\Delta_0/W+H'_1(t)\Delta_1+W H'_2(t)\Delta_2.
$$

角导数还作用于完整 Cartesian Fourier 基；这里必须使用实际模式，包含平面旋转基的频移，不能只把 solver 的 $M=15$ 当作最大 Cartesian 角频。make 的 `cut_jet_coefficient_max_upper` 是三个逐槽最大值，不是 Fourier 加权和或 metric 界。即使 source 非均值 slope 残差很小，也不能据此跳过最终图后端。

更一般地，在同一源目标的正交材料标架中记 $X=dF$、$Z=dC$。若已有 $\|X^T X-I\|\le\varepsilon_0$、$\|Z\|\le d$，则由矩阵恒等式和次乘性

$$
\|(X+Z)^T(X+Z)-I\|
\le\varepsilon_0+2\sqrt{1+\varepsilon_0}\,d+d^2.
$$

这只解释需控制的是**实际一阶修正**，本文没有为新图计算 $d$，也没有新增一份修正证书。现有最短路径直接对 common-cut 后的完整图认证，已经包含所有这些项。基础图与共同图的两个上界之差只能定位可疑区域，不能当成实际 metric 变化量的上下界。

镜像 wrapper 只把入口 height 二 jet 精确置零；在共享 Hermite 中，这项修改只作用于相邻首跨。其 `mirror_second_height_adjustment_max` 同样只作诊断。不得通过撤掉镜像条件或改变 common-cut 宽度来“收紧同一图的证书”：那会定义另一张图，必须重新支付其几何与闭合绑定。

## 4. 真正需要时的最小顺序

1. **完成原对象绑定。** 复用 readiness §3 的固定次序：最终 CP → mirror 基础图 → 新 target → 基础图完整 metric → 新 exact bridge → common-cut make → 最终共同图完整 baseline。基础图报告是现 bridge 接口的输入；它不能冒充最终图报告。无需为这一步另造 preparer。
2. **先查已有最终 baseline。** 用新 bridge 的 `relative_target_metric_difference_upper` 与 baseline 的 binary `metric_operator_upper` 转为精确 Fraction，比较 $\varepsilon(1+\eta)+\eta\le B$。若已通过，停止额外角／径向诊断；必要时 wrapper 只走已审的完整继承路径。
3. **只有 baseline 未过时，运行一个局部 pilot。** 取该新报告自己的 `worst_interval`，128 初始弧、最大深度 4。读取其原区间摘要、`candidate_arc`、分母失败数、proof kind 和达到深度上限的叶。若改善清楚，再做一次完整扫描；若局部仍不过，先分清未过的原因，不盲加全域计算。
4. **完整验收不可用 pilot 代替。** 完整调用省略 `--intervals`；必须核 `finished`、`entire_prefix_covered`、全部叶的分区／正分母及 `entire_prefix_target_met`。完整但 target false 是有效的未达门报告，不应标为求解成功或认证过门。
5. **只处理留下的具体原因。** 角细后仍有大的实际残差，则看同图点值／严格 lower；只有径向依赖或目标包宽主导时，才另审其改进。现第一档既没有径向细分也没有二阶角 Taylor。单纯增密验证不会消除一个已证超过 B 的真实图误差。

不需要先重复旧 M12 fixture，也不需要为了这份静态计划重新采样 affine、导出尾或跑全 Jac。旧对照已经回答了方法层的问题。

## 5. 冻结接口与条件式命令

以下只给**将来真实输入已经存在时**的参数模板，本轮未执行。所有输入／输出变量应填绝对路径；输出用新的、不存在的文件名。`p15_common` 必须是最终 common-cut-v2 metadata，不能填 CP 或基础图。

```sh
p15_repo='/workspace/scratch/db6f0b0e7462/math-research'
p15_scripts="$p15_repo/topics/visible-flexible-closed-surface/scripts"
cd "$p15_repo"

# 已有完整 baseline 时不重复此调用。
python "$p15_scripts/db6f-root-common-cut-v2.py" metric \
  --geometry "$p15_common" --target "$p15_target" \
  --out "$p15_baseline"

# 仅在 baseline 的精确转移值未达 B 时选择其真实 worst_interval。
# p15_worst 是该报告的整数索引；不得预填旧 M12 的 0 或 74。
python "$p15_scripts/db6f-audit-prefix-angular-metric.py" \
  --geometry "$p15_common" --target "$p15_target" \
  --baseline "$p15_baseline" --bridge "$p15_bridge" \
  --budget 2e-9 --initial-arcs 128 --max-depth 4 \
  --intervals "$p15_worst" --out "$p15_local_report"

# 局部因果结果支持继续时，正式完整扫描省略 --intervals。
python "$p15_scripts/db6f-audit-prefix-angular-metric.py" \
  --geometry "$p15_common" --target "$p15_target" \
  --baseline "$p15_baseline" --bridge "$p15_bridge" \
  --budget 2e-9 --initial-arcs 128 --max-depth 4 \
  --out "$p15_full_report"
```

**两个具体 CLI／字段陷阱：**

- common-cut 脚本共用 parser 中虽有 `--angular`、`--radial`，但 `metric` 分支仅安装 common-cut adapter 后调用 `metric.run(..., limit=None)`，完全不读取这两个值。调大它们只会改变 geometry／moment 分支的设置，**不能收紧 metric**。也不能直接用未安装 adapter 的原 polynomial CLI 认证共同图。
- `--budget 2e-9` 是精确原目标上的总门。wrapper 的 `metric_operator_upper` 仍是源目标界；`exact_target_metric_operator_upper` 才已转移。closed-budget 再取前者转移一次，不能先扣 eta 再把已转移字段重转。partial 输出故意不提供可误认成完整前缀的兼容字段。

除完整报告外，定位时的现有接口如下；无需新增 solver 接口。字段与命令已逐项核对 [angular wrapper](../scripts/db6f-audit-prefix-angular-metric.py)、[原 polynomial 后端](../scripts/db6f-audit-metric-polynomial.py) 及上述 common-cut 源码，准确版本见同名 JSON 的 hash：

| 已有产物／接口 | 可读出的信息与边界 |
|---|---|
| 最终 baseline | `worst_interval`、`coordinate_residual_upper`、正的 `minimum_a_lower`／`minimum_chart_rho_lower`、完整区间计数。它没有逐区间 ledger，三个坐标最大值也未必发生在同一区间。 |
| target 的 data packet | `left/right` 是实际物理盒；`a/e/ep` 的系数上下端点和 remainder 用于判断目标包宽。供应包宽不是 metric，可用于定位，不能再直接加减到已算误差。 |
| angular 的 interval shards | `original_interval`、`initial_uniform_arc_upper`、`local_denominator_failures`、计算次数。 |
| angular 的 row shards | 精确角端点、`proof_kind`、`candidate_arc`、正分母、source／exact-target 上界、`target_met`。最深叶失败只表示当前上界未达门，不是实际图 lower。 |
| common-cut make 的已保存 stdout | 实际 `width`、`corrected_spans`、三个 cut 二 jet 系数最大值；metadata 给 `correction_start_index`。物理起点由基础图真实 mesh 读取。 |
| common-cut adapter 的对象属性 | 若以后必须精确定位且另获执行授权，`cut_delta`、`correction_width`、`cut_correction` 提供源码定义的包围；构造对象会读完整图，本轮未调用。 |

## 6. 证据范围与无需新增的门

本轮只重读源码／小报告并计算文件 hash。全部来源绑定列于同名 `.json`；没有新 metric 数字、没有新候选、没有测试运行，也没有修改任何已冻结源。

现有 readiness §§3–6 已覆盖本次所需算法、预算和完整覆盖门，本文没有提出新的强制计算。最终同一图只要真正获得原目标连续界至原求解容差，就不应另造“C² 差也必须到 $10^{-11}$”之类 README 未要求的完成门；固定 g 的加密序列、独立实际重跑及精确存在性差距仍按既有计划如实汇总。

本稿是带来源的静态条件分析，尚未作为新的数学结果提交。它不支付未来 M15 的 prefix／tail 证书或 README G5。
