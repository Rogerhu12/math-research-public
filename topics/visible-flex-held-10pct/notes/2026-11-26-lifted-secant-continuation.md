# 独立 lifted-secant 控制器的窄接续

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

新增 `material_design_lifted_secant_continue.py`，直接复制已部署原
`material_design_secant_continue.py`（SHA b7600de7a668288c85e7ce70ffca09748bb7e251075c1320441d1a76d280d081），
仅加入已审跨 M predictor 的独立进程分支。不改在跑文件、CI、旧求解器或
旧 predictor，也不重跑低 q 恢复。

## 唯一的继续路径变化

候选 earlier 仍只来自真正通过原门的 `accepted_runs`，其 λ 必须早于当前
接受锚；M 筛选从等于当前改为不大于当前。实际选到同 M 时继续调用原
`predict`；低 M 时启动独立 Python 子进程运行
`material_design_cross_mode_secant_predictor.py`，避免原 geometry loader
的全局类污染当前控制器或下一预测。

子进程输出必须明确是未接受 cross-mode initializer，绑定两份真实 run 的 SHA、
目标 λ、目标 M 和初猜文件 SHA。initializer 记录区分同 M 与跨 M，保存
left/right run、SHA、M、predictor JSON/SHA、initial SHA；不制造 accepted 源。
原实际 portable command、全部 solver/BC/metric 门、metric-only 升 M、
失败二分、接受锚与历史更新保持原结构。

来源记录额外绑定新 predictor 和被复制旧 controller，并保存复制时的 b760
SHA。参数及默认值不变，没有新增动态 resume 或预算逻辑。仅按根要求移除
原1 MB summary停止条件和原始 last_log 摘录；保留原安全 last_prefix_event。

## 调用

在旧父链自然返回后，用其**实际最高接受场**和真实 earlier run 启动；
不得传 metric-only、预测器输出或源身份不符的其他 VM 场。

~~~bash
python material_design_lifted_secant_continue.py \
  --repo REPOSITORY \
  --work SAME_RUNNER_WORK \
  --source-run ACTUAL_HIGHEST_ACCEPTED_RUN \
  --previous-run ACTUAL_EARLIER_ACCEPTED_RUN \
  --outdir NEW_CONTINUATION_DIRECTORY
~~~

必要的目标列表使用原 `--targets` 参数；未传时保持原默认，不擅自重写。
若最高仍为同 material VM 的 .064/M40，则源是
`secant-design-recovery/secant-material-design/attempt-002/run.json`，
前一真锚是该目录 attempt-000 的 .032/M32。若旧链又实际通过了更高 λ，
须以真实返回为准重新选择，不能照抄这个示例。

所有预测仍是 design 初猜，完整 g 和 mean 的固定问题收敛没有因此获得。
λ=1 的有限前缀也仍欠真实 DN、闭合、时间族与 reach。

## 已做检查

compile 和 `--help` 真实退出0。逐项统一 diff 审阅之外，实际 AST 比较核实：

- 原 finite_nonnegative、original_finite_checks、complete_initializer、
  last_prefix_event 逐项相同；
- parser 参数与默认值、原完整模式 transfer 分支相同；
- 从 target core settings / 实际 command 开始，到原门、历史更新、
  metric-only 和二分整个循环尾部相同；
- 同 M 的旧 predict 调用相同，原 raw last_log 和1 MB停止门确已移除。

这些是源码结构检查；未在本地执行实际继续、BVP 或 DN。
实测记录为 `notes/2026-11-26-lifted-secant-controller-source-checks.json`。

| 文件 | SHA-256 |
|---|---|
| 新 material_design_lifted_secant_continue.py | 519c596e3bbff4c5f61038b78b91e9c996655abba8a6a2b96acf16b6853fb373 |
| 新 controller-source-checks.json | 3af12af9464efcd89d588355e9eb0df8ede23f15630dac9a69a8d05d24b16422 |
| 原 material_design_secant_continue.py | b7600de7a668288c85e7ce70ffca09748bb7e251075c1320441d1a76d280d081 |
| 独立 material_design_cross_mode_secant_predictor.py | 79ebe59d041a4c9f600345890875237f2b222f8301b8c736c586ab0884ecaae9 |
