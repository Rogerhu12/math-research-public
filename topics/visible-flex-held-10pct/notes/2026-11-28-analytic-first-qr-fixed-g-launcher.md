# 首个真实 QR/full-DN 锚到同 g 更严精化：独立直接接线

源码 `analytic/run_qr_anchor_fixed_actual.py` 只接一个已经实际接受的
**内层** `actual-dn/summary.json`。其 schema 必须是
`original-lambda-one-native4-chord3-outer8-prefix-qr-v1`，状态为
`original_finite_true_dn_gates_passed`，且 `result.accepted` 为真。
外层 launcher 的 summary、线性设计 run、未接受检查点均不是该输入。

入口随即调用已冻 `qr_fixed_support_actual_model.accepted_input`，完整
验证真正 QR 原支持核心/full-DN 锚和最终 physical-H，不能靠只查 summary
标签放行。当前没有这种真实 lambda-one 返回，因此本记录没有正向执行、
新 fixed-g 数值接受或闭图结论。

## 同一目标 g 与同一完整端口

首次只保留源实际 $M$（现有 native $M\le64$ 范围），直接复用源的
M-specific port、baseline、native manifest 和完整 native source，
不默认 M24，不导出替代端口，不重生低 lambda 输入。物理 profile、实际
delta、完整核心族、原 gauge/warp reference、原 mean 均由已有模型/锚门
冻结；source 的原角节点不足 `32*M` 时只增加后继求解采样，不改变 mean。

runtime 仅复制三个明确执行字段：`initialCheckpoint` 指向这个真实
**最终 physical-H packet**，`traceFile` 指向独有输出，
`chordMaxCorrections=3`。删去这三键必须与原 baseline 完全相等；
原 port 还必须绑定该 baseline SHA。所有原 source/physical/H/native
引用及 SHA 写入 `source-resolution.json`，不回写源 run。

CLI 的 `--tol` 必须比锚实际 tolerance **严格更小**，且不得越过
原 `1e-6` 上界。BC 与 physical-BC tolerance 也不能放宽；节点上限
须容纳完整原网格。真实新模型仍保原所有残差、域、完整 full-H/J/audit、
chord=3 和 outer=8 门。不是把仿射尾初猜当成 full-DN 返回。

## 执行所有权

`resolve` 只落下真实来源合同、独有 runtime 和可直接执行命令。
`run` 通过 `os.execv` 把本小 resolver 替换为已有
`run_qr_fixed_support_actual_once.py` 显式进程所有者；它不增加一层
`Popen` 监管器或无归属子进程。必须明确选择
`--own-child-session` 或 `--inherit-owned-session`；CI 只允许后者。
真实终态看 owner 的 `actual-process.json` 与新模型 own-KIND run，
准备 summary 不代替真实终态，也不承诺 owner 已启动数值 child。

## 已执行的窄核

源码已真实 compile/help 成功。又使用原 R87 lambda-zero 求解器停止前
保存的真实 `actual-run-before-interruption.json`，作为明确的错误角色
输入执行一次 `resolve`。工具 `84f9d4` 实际返回 exit 1：

```
Require the genuine accepted inner actual-dn/summary.json,
not a launcher or linear-design record
```

输出 `numerical_child_started=false`，没有构造初猜、调用 native、组 J
或启动 BVP。此负向验证只付 schema/角色拒绝，不付缺失正向输入；
没有伪造 lambda-one 或耦合记录。实际路径/SHA/命令见同名 JSON。

后继有真实内层返回时，同一命令可直接使用 `run`，无需再改读取合同。
旧九个 QR fixed-g 模型/reader/mesh 源及其已登记哈希均未改。
