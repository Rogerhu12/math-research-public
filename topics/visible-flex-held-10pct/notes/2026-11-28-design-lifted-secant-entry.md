# 从晚返 λ=.128 前沿继续原 R53 设计

日期：2026-11-28。维护：Astra-held10-7c4e33ee-20261128 / design_continuation。

## 实际断点

交接摘要中的 `.064/M40` 不是旧作业的最终接受值。当前
`ci/live-material-result.json`（worker deadline，原 run45821850836）保留了
晚返 `.08/M40`、`.096/M40` 和 `.128/M48` 的完整有限验收标量。
最后一项为 1219 点、RMS `9.195974420760265e-7`、metric
`1.590499829842865e-7`、物理 BC `4.142436380220934e-13`，
δ `0.06412830439644338`、mean2320。来源及原 raw/physical/run SHA
见 `2026-11-28-design-previous-frontier.json`；这些是对已记录实际返回的
补登记，不是本次重新计算，也不是闭曲面完成。

随后 `.256/M48` 原 raw 初猜发生 Frenet 域异常，`.192/M48` 为
`MemoryError()`；`.16` 所在的 attempt011 在 worker 截止时尚无实际
终态，不能推断其数学失败。原单 M secant 在升 M 后没有第二个同 M
接受锚，只能使用原 raw；新入口使用已经保存但未实际执行的跨 M 完整
lift secant，避免再次照抄这些无预测的大步尝试。

本工作区未找到旧 runner 数值场。依据现有源/参数恢复旧前沿是为取得
继续计算所必需的输入；`λ≤.128` 的再生结果不再登记成新的数学进展。

## 唯一的新继续方式

`scripts/resume_20261128/design/run_design_recovery.py` 执行原
`lowq_prefix_recovery_secant_design.py` 的 q=.006→.06、λ0、
λ.002/M8→M16→M24 恢复以及原 `.004/.008/.016` 设计 bootstrap。
恢复中的物理 profile、chart 规则、原 R48 完整 lift 和全部验收门不变。

从两个真实接受的 `.008/.016` 锚起，调用已有的
`material_design_lifted_secant_continue.py`。同 M 时使用原完整 t-PPoly
secant；升 M 后若已有低 M 的前一接受锚，调用原
`material_design_cross_mode_secant_predictor.py`，保左图自己的 δ、
计算坐标和完整入口修正。所有预测仅为未接受初猜。目标仍是原
`.032 .064 .128 .256 .512 .75 1`，原失败二分和 metric-only 升 M
逻辑保持，M 列表仍 `24 32 40 48 64 80 96 128`。

每次真实子命令及替换另写在工作目录的 `*-execution.jsonl` 中；原
portable 求解器仍自行生成真实源/输入、raw、physical、RMS、BC 和
完整 finite metric 验收记录，不把 predictor 或日志包装当作接受场。

## 有界径向执行

现有 `streamed_release_prefix_driver.py` 只给 `solve_bvp` 内的 RHS/Jac
分块。原 portable 在求解前仍调用整批 `rhs=o.fun(x,y,par)` 作初始域
检查。新 `prefix_resource_driver.py` 复用原分块函数和旧 LU 释放方法，
并将这一次初始检查也按8个径向点分组，完整访问原节点/状态/参数。
域错照常抛出，不截断模式、不裁剪 Frenet 根、不缩小真实检查范围。

wrapper 记录原函数和实际执行函数 SHA、分组大小、旧 LU 释放以及
实际命令。数学方程和原验收门不变；浮点逐位身份不作声明。它不能
减少单个最终 sparse LU 的固有内存，也没有将旧 `.192` 的未知异常栈
归因于这一次未分组的初始 RHS。

## 复现

先在仓库外准备静态源和原输入：

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261126/tail_recovery_setup.py \
  --repo REPOSITORY --work OUTSIDE_WORK
python -u topics/visible-flex-held-10pct/scripts/resume_20261128/design/run_design_recovery.py \
  --repo REPOSITORY --work OUTSIDE_WORK --outdir OUTSIDE_WORK/design-recovery-20261128
```

数组、完整求解日志、raw checkpoint 和生成源留在工作目录，不入 Git。
本入口已实际 compile，恢复入口 CLI help 通过；本文创建时实际70源
恢复尚在执行，未宣称新的 BVP 接受。真实返回随后独立登记。

设计中的 δ、控制和 mean 节点规则可变化，仍不是固定完整 g 精化。
即便 λ1 前缀通过，也仍欠真正 full-H 非线性 DN、共同 Cartesian 两jet、
全时闭族、reach/幅度和固定完整问题的加密收敛。
