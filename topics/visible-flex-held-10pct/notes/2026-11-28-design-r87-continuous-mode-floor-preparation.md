# R87 连续后继：明确 M 下限与完整两源升模割线

**性质：执行入口准备，不是新数值解或证明。** 独立 `scripts/resume_20261128/design/run_design_stage_control_v2.py` 已真实 compile/help 通过；本条写入时尚未用它启动 BVP。旧正式 controller、全部原数学源和当前活 λ0 求解均不改。

为使新严格 `tol=2e-7` 路线连续推进而不重跑已知的 $\lambda=.256/M24$ metric 失败，新增明确参数 `--mode-floor 0.256:32`。它只在原下一阶段边界把 M 提高到声明阶梯中相应下限；更高的当前 M 保留，原 metric 判定与按真实失败升模的规则保持。

在 lifted-secant 模式下显式加 `--two-source-mode-lifts`，当目标 M 严格高于当前真接受场，且存在更早真接受锚时，调用已冻结的 `both_source_lifted_secant.py`：两份完整原 PPoly 各自提升到目标 M，再对全状态和全部参数作割线。返回状态、真实双源绑定、完整 raw 与目标 port SHA 全核；预测仍是未接受初猜，必须再经过全部原 BVP/域/BC/metric 门。若起点只是上一阶 metric 失败的收敛场，则仍走原单源完整提升，不将它冒充接受锚。

正式停止请求、已完成阶段限制和 exit 4 合同原样保留。已实际遇到过的 `MemoryError`、`[Errno 28]`、`No space left on device` 按真实 error 或失败日志识别为工程事件，与负码/信号退出一样不会送进数学 λ 二分；没有据此断言 OOM，也没有修改系统限额。完整源 SHA 和准备状态见[小记录](2026-11-28-design-r87-continuous-mode-floor-preparation.json)。后继将先由真 λ0 bootstrap 到正 λ，再在同一 R87 家族继续 $\lambda=1$，不以阶段回执等待另行授权。
