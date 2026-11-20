# PCG + SOC 的实际返回报告：分离原射线、QP 迭代点与修正步

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

## 1. 状态与范围

新增 [full_phi_pcg_soc_report.py](../scripts/resume_20261120/full_phi_pcg_soc_report.py)，源码 SHA256 见文末。仅准备源码；本地只做 AST 和编译语法检查，没有导入或执行消费器，没有读取实际报告作数值归因，没有读取 NPZ、场、方向数组或调用 $J/J^T$，没有新 fixture。

这是已返回 JSON 的独立消费者。冻结的 `full_phi_qp_bottleneck_report.py`（`930d832f92cf61021f394b835fb9ab0e14ae0d1ce3ca4a72f597a65e09bab0b0`）和 `full_phi_qp_scalar_diagnostics.py`（`9124229786200659f1c9dc73620eecd75dda6493990f684149471d7003263b9d`）均不改字节。新源仅复用前者 `linear_history` 和后者的原 QP 方向标量公式、非有限数序列化；旧的 trial 配对及 accepted-parent 更新不再复用。

执行入口限制为本仓库公开 Actions。输出 raw JSON 留在 runner work；公开记录只逐项选择确有意义的标量，不将原报告或本归因输出整包提交。

## 2. 三个对象不能合并

设主 QP 返回原 augmented 步 $d$。原射线为 $x+\alpha T d$。SOC 如有可用修正，则另读 $x+T(d+e)$。

| 对象 | 模型来源 | 实际读出来源 | 不可继承的量 |
| --- | --- | --- | --- |
| 原主 QP 点 $d$ | 原 QP 的 $A,v,C,b,\mu$ | `record.qp` | 不把这些 Pg、乘子、活动面或 status 搬到 $d+e$ |
| 原射线 $\alpha d$ | SOC 已接受时用 `uncorrected_direction_model`；否则用 record 原字段 | `record.trials` | 不使用已被 SOC 替换的 slope、norm 或 prediction |
| SOC 修正步 $d+e$ | `record.soc.trial` 中已实际重付的 $A(d+e)$、slope、energy、prediction | `record.soc.trial.statistics` 和完整 geometry/filter | 未执行 corrected QP，故 corrected Pg/status 明确为空 |

SOC 接受后的下一方向，父统计取自其真实 `soc.trial.statistics`。原射线接受才从对应 alpha 的原 trial 取统计。消费者只在内存里构造明确标注的“原射线分析视图”来调用冻结标量公式；不重写原报告，不伪造 saved ray 或新方向文件。

原射线逐个实际 alpha 的预测为

$$
\Phi_{\mathrm{model}}(\alpha)
=\Phi_0+2\alpha\,v^TAd+\alpha^2\|Ad\|^2.
$$

SOC 使用相同公式的 $d+e$ 版本，并直接读取其已付 energy；两者都将 $\mu^2\|z\|^2$ 单列，不把 QP regularizer 混入真实 Phi 预测，不把 virtual RHS 的平方范数当 Phi。仅原 $d$ 的能量与原 QP objectives 交叉读出；SOC 不使用这些旧 QP objectives。

## 3. 源与模型解释边界

支持以下两组实际 schema，分别显式区分 `original` 与 `R671`：

- `fullclosed-gauss-{original|R671}-parent-row-SOC-v1`：冻结 805/5bc 的纯 SOC 链。
- `fullclosed-gauss-{original|R671}-coarse-PCG-parent-row-SOC-v1`：`40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e` 完整复合派生器声明的链。

核对报告中 805/5bc、f96、324/da083/dd595/fb4 的角色 SHA 与对应 schema。R671 保留实际 canonical definition、model identity、原/末 context、carrier 及 bundle 身份；不把非零新尾读成原 lift。未知 schema/角色语义直接报错，不猜测。

本消费者只有 JSON，没有执行完整源体 binder，所以报告中明确 `entire_actual_source_body_authenticated_by_this_consumer=False`。它不以 schema 或来源字符串代替 launcher 已付的全 AST 源体绑定。

## 4. 主 QP 与固定预条件的归因字段

每方向 `main_QP` 汇总原 $d$ 上的欧氏 Pg、停止容差、二者比值、最终线性可行性、互补量、规范化释放方向及实际阈值。保留原 history/transition 的活动面加入与释放计数、固定面段、32 次显式刷新的实际记录、误差是否迫使重启、不同重启原因、最后一条实际 history、相邻共轭缺陷记录与已付算子次数。

`preconditioner` 分清：

- 构造成功、构造不可用而显式回到 fb4、未启用三种状态。
- 构造总秒数与 frame/moments/small-SPD 分项；分项已含在总数内，不重复相加。
- 实际方向 $\mu$、$\beta=1/\mu^2$、构造额外 $J/J^T$ 次数、literal 小 Gram 诊断。
- v4 真实 apply 次数、秒数、失败记录、最后成功 apply、完成的 Euclidean release starter 次数。
- 应用期失败保留 `fixed_preconditioner_application_failed` 和实际截断 $d$，不将它改称收敛，也不伪造 identity fallback。

Apply 秒数是 QP 秒数的子项；构造/线性准备/SOC/整方向也明确是嵌套成本。输出没有将所有时钟无区别相加。

R673 中固定面误差界仍属于原 $d$ 的当前仿射面，不能当整个不等式问题或非线性 Phi 的剩余误差。原普通 CG 的 kernel 不变子空间文字不直接套到任意固定 $B$；新输出明确本 JSON 消费器没有核实际 $B$ 的 kernel 保持性。

## 5. SOC 与完整真筛的归因字段

`SOC` 记录是否真正尝试、是否得到 proposal、精确 skip/failure reason、selected 父行及其原物理位置/固定半径伙伴/归一化，$\|d\|,\|e\|,\|d+e\|$，修正范数比，显式 tau，QR 实际秩与数值诊断。

保留全部原行的 bounds、$Cd$、$Ce$、$C(d+e)$、原/修正 slack、物理线性 product 与浮点可行性容差对应的量。完整父行非线性读出也分别保留 full-trial 与 corrected-trial 版本。未读完或未到选择阶段的计数保持空值，不冒充零违反行。

每个已记录原 ray trial 和实际 SOC trial 分别列出：真实 Phi/下降量、对应方向在同 alpha 的预测及实际/预测比、domain/descent 标志、是否真正执行 geometry、完整几何读出是否成功、product、算法 margin、曲率和直径点下界、worst 与 radius 位置，以及新永久点。

拒绝原因分清非有限/domain/真实 Phi 或 Armijo/不完整几何读出/已知点 product 超内部 margin/额外绝对曲率 cap。`curvature_feasible=True` 而未执行几何不会被读作几何通过。点 product 小于 1 只作点值事实，不推连续曲率或 reach。固定父行没有正残差，也不自行归因为新峰；源中保留“不足以判因”的限定。

## 6. 实际末阻尼与主线程选取

逐方向按已刊冻结规则重放：未接受乘 4；接受满步且该实际方向的下降比大于 .75 才减半；其余保持。SOC 接受的比值来自 corrected prediction。输出与 `damping_after_direction`、下一方向实际 damping 或 `final_damping` 逐项比较；不改更新规则。

`reports[0].scalar_summary.d000` 等字典只含标量，方便 worker 逐项公开。完整细节在同一报告的 `reports[0].directions[0]`。特别适合直接选择：

- `QP_status`、`main_QP_Pg`、`main_QP_Pg_over_tolerance`、`release_count`、`longest_same_face`。
- `preconditioner_status`、构造/apply 秒数及失败次数。
- 原射线几何拒步数、原 data energy 与正则化/data energy 比。
- `SOC_reason`、selected 行数、QR 秩、修正范数比、全部旧 slack 的最小值、实际 SOC product/Phi。
- 实际 accepted kind/alpha/Phi/product/maxGram、同 alpha 模型比、真实 next mu。

这些是区别线性截断、活动面、构造/应用故障及非线性几何拒绝的事实字段，没有自动选定“唯一瓶颈”，没有从 raw 负乘子或 Pg/容差比单独推出因果，也不自动排新预算。

## 7. Actions CLI

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/full_phi_pcg_soc_report.py" \
  --report "$WORK/actual-pcg-soc/report.json" \
  --out "$WORK/actual-pcg-soc-attribution.json"
```

可重复 `--report` 并列读取多个已返回结果，不比较不相同模型为同父试验。两个冻结依赖默认从脚本同目录取，也可显式给 `--scalar-source` 和 `--history-source`（这里 history 指 930d 报告消费者，不是 4d9 末 mu/位置 helper）。不覆盖已有输出。

源码 SHA256：`adc90f41cb7cb1dd4b5842e547d2381432094e8e0565c63c5859e5bcfc1d06dd`。

本次状态：仅源码与说明准备；AST/compile 通过，实际报告消费尚未执行。

## 8. 本次执行队列

该纯JSON消费者已排在同run的实际PCG+SOC方向之后，step为 `actual-R671-PCG-SOC-returned-attribution-02`，读取 `exact-tail-full-phi-PCG-SOC-first/report.json`，写 `postprocess/reference-tail-PCG-SOC-attribution.json`。本条发布时尚未消费实际新结果。队列同时修正两个位置计数选择器为4d9真实字段 `curvature_numeric_tuples` / `radius_numeric_tuples`；这只影响公开摘要，不改变输入或科学命令。队列采用紧凑JSON留出后续容量，解析后的全部步骤、次序、命令与参数保持此次明确版本，没有删除旧步骤或重置已执行id。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
