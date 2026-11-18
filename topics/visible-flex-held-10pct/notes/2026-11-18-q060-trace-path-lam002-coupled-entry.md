# q060 有限迹路径 λ=.02：唯一真实联立入口

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。

紧接[已完成的模型入口](2026-11-18-q060-finite-trace-path-entry-terminal.md)，启动唯一同 λ=.02 的实际联立。observer 会话 `94553`，启动工具块 `67ca61`；实际入口事件为 2026-11-18 03:17:09 UTC，03:17:10 UTC 完整初始数组已读入。此条只登记启动和源，不预认终态。

## 输入与原门

直接读取已有 `entry-arrays.npz` 的 $25\times271$ 状态、完整八参数与径向网格。仅为真实求解构造一次同模型，验证原 $y/p/H$ 哈希；没有重复旧投影、共享 $C^2$ 修补或 RMS 诊断。表示 gauge、warp、七个参数尺度保留原 `.06`；独立支撑 seed 为 `.059818741459951905`。固定 λ=.02、原主／控制窗口和完整七个物理系数，不扫描幅度或 λ。

新 owned runner 继承原实际尾外循环与 main，两个派生片段逐字节等于已审查五点版本。保持原八次 outer 预算、Newton/Jacobian/merit、节点上限及全部 BC/RMS/域门。已审查的五点 guard 仍仅补原 RMS 两额外取点的同域检查，不新增残差阈值。原 mean-height、完整 metric 与接缝审计留在原后处理调用链内。

初始八个 $H$ 与旧实际响应逐位同，首查询只将已接受的完整 208 项 Jacobian／audit 响应置入原 cache，不伪造新尾计算。任何改变后的 $H$ 仍调用原实际尾并要求 Jacobian／audit；原停止门仍为 $2\times10^{-9}$。

## 保存与读取边界

保留每个真实 Newton 接受状态、返回／异常观察，以及每个内层入口／返回的完整 $x,y,p$、已有 RHS／raw cubic 与原实际 DN 锚。旧 guard 内的端点专用 kind/path 字样，仅在新保存入口更正为当前 partial-lift 路径；数值数组和算法不变。

新 CP kind 为 `exact_m3_finite_circle_trace_path_partial_lift`，control path 为 `finite-cosine-trace-synchronous-lift-v1`。另保存独立 `q_gauge`、`seed_support_amplitude`、完整七个 `physical_controls`、λ、径向 lift 窗 `[.5,.9]`、源绑定、原余弦参考及完整 `path_definition`。`actual_primary_amplitude` 仍是原 serializer 的支撑 seed，不能解释为表示 gauge 或真主矩。

`path_base_profile` 与原完整参数共同确定同一个模型；原 `frozen_profile` 已吸收终态 $p_0$。未来若重基为 $p_0=0$，须显式转接实际材料坐标，不能再次施加历史 $p_0$。旧 `ratio**j` restart、旧 raw/full-lift loader 不适用于此新路径。

closed_geometry 只读独审新 runner 及原后处理：`adaptive.audit` 使用本次 `o.flow`，原 `height_integral` 的 frame 动态读取实际 partial `geo`，确实重新积分本图竖直均值；没有复用旧均值轨迹。没有为此审查重复任何数值计算。

## 冻结来源

- [最小 owned runner](../scripts/resume_m3/run_q060_trace_path_coupled.py)，SHA-256 `4d2684114f17e770d8d08b909d4c2bac5c2482c0d63f57394e4644f71b66291d`。
- [紧凑入口记录](../scripts/resume_m3/q060_trace_path_coupled_entry.json)，保存全部必要参数、103 项源绑定、原同 $H$ 响应身份及真实启动观测。
- scratch 计划 `m3_work/q060-circle-trace-path-coupled-lam002-v1/launch-plan.json`，SHA-256 `99b888b421ecaea72dbbafffca9811121ed8d663c62049c3ce03e54edc6b52be`；observer 命令文件 SHA-256 `bebd0b25ff654773908ede1225704a701496b6d6c209331a844b58c9ada175a3`。

这是改变物理空间／参考表示的新设计求解，不是同一 $g$ 的精化。全部数学接受和失败边界以实际终态另行登记。
