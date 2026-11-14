# 显式全态 Hermite 初猜与提前真审计的组合准备

## 可执行结论

新增 `strong_eager_audit_explicit_hermite_actual_bvp.py` 将已经冻结的提前真 H 审计入口与一个只改首次 live 输入路径的 Python 子类组合。源变换反向可精确恢复此前完整生产入口；原 `root_actual_neck_bvp.py` 的内存编译 SHA 仍为 `1947ef4a62aa73f6dff8b4abe5fc1de53e824107785df976a923728eece7635e`。全部 MJS 和旧 Python 源保持原字节。

需要这样组合，是因为原 recorded port 在启动 live 时会用最近完整响应覆盖配置中的 initialCheckpoint。只同时传两个旧选项会忽略另外提供的 Hermite 初猜。新子类保留原初始 audited packet、ready 与 exact-H cache；它只在首次非 saved-H 请求、live 尚未创建且全部 H 字节精确相同时，将 `_last_checkpoint` 设为显式未接受 warm。其它高度走原输入路径，并明确记录未选中。任何后续请求都不能再次回退到旧 Hermite 初猜。

“选中初猜”和“真正交给原构造器”分开登记。实际原 `_ensure_live` 成功返回后，子类读取它刚写出的真实配置及 I/O provenance，核 initialCheckpoint 路径和 SHA，再登记构造器回执。该回执不表示 Newton 收敛，也不表示新 H 已审计。后面调用完全沿原 solve/缓存/标准包/全 J/残差/正性/最终审计门。

## 身份范围

输入必须来自已冻结的 `strong_full_flow_hermite_warm_v3.py`，报告必须保留原全部检查及适用性结论。预检查逐 SHA 读取所有源和输入，包括两个已接受基点、全 flow-J 侧车和真正完整 warm 场；另核当前接受主包与初始 audited packet 的绑定。新的 warm 明确标 `new_target_accepted=false`，没有响应或新 flow-J 快照。

完整状态为 577×56；原 rawNode 为 `[0,72,144,216,288,360,432,504,576]`，其 rawStates 是全部 9×56 对应子数组。两层数组、全部 rawNode 顺序、全 28 项 H 和全部非 I/O 参数都核验。开发期一次只读草稿误将 rawStates 当成全部 shooting states，校验立即拒绝；随后按冻结的原 exactRawWarm 索引语义修正，未改变任何原输入、原求解或已保存结果。

新前缀控制或不共线方向不能自动沿用 q098→q106→q122 的共线误差诊断。仍由原生成器决定适用性；显式投影启发式保持其独立标签和界限。新入口只检查已经给出的真实报告，不扩大适用域。

## 实际执行记录

| 检查 | owned exit | 墙时（秒） | 峰 RSS（KiB） |
|---|---:|---:|---:|
| 首次 live 输入协议回放，15 门及 55 输入身份门 | 0 | 2.014963580 | 34308 |
| 真实 q106 生产 prepare-only，完整来源/参数装配 | 0 | 1.017925431 | 34104 |

回放使用真实已审计 q106 作为旧基点，真实 q122 初始尾的已完成 full-J 响应作为唯一允许返回的目标数值包。该 q122 包本身 audit=false，回放没有把它标成最终 audit，也不对任何新的审计请求捏造响应。整个回放没有 Node、ODE 或新 BVP。

检查覆盖：saved-H 缓存不会提前消费 warm；首个 matching-H 的实际构造器配置收到正确 warm SHA；原 audited cache 身份保持；完成响应随后取代 warm 成为最近 checkpoint；回到相同 H 不重新安装旧 warm；1 ULP 不同 H 保留原审计包初猜并进入原 live；后续 audit 请求不能用未经审计的包冒充。

生产 prepare-only 仍取真实 q106 原目标，不启动场或 worker，只核原 31 参数/116 BC 及组合源。真正新目标消费还需下一生产运行；本批没有 Newton 次数或运行时间改善主张。当前 q122 原实际求解保持不变。

本批完整文件、SHA、资源和命令见 `2026-11-13-strong-eager-hermite-input-preparation-manifest.json`。此前 Hermite 输入、真实旧包、原生成器与提前审计源按原哈希引用，不重复保存大数组。
