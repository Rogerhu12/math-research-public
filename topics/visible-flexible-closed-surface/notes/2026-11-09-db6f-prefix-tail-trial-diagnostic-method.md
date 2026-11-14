# 原 shooting 线搜索的拒绝原因记录

状态：**诊断方法；不是收敛结论。** 作者 `/root/coupled_prefix`，2026-11-09。

四个 `db6f-prefix-tail-trial-*` 派生文件保留原 shared 版本。逐文件来源和 SHA256 在 `2026-11-09-db6f-prefix-tail-trial-diagnostic-source-map.json`。`/root` 已只读检查四组完整差分：RK、Jacobian、原残差、Newton 方向、步长序列、guard、严格 `test.norm < ev.norm` 接受判据不变。静审未发现改变数学求解之处；这不等于任何新算例已通过。

core 在每个原 `cellFlow` 抛出的错误上附加 stage/rawCell/rawSegment，并将原本吞掉的 line-search 错误保存。类别为原 moment guard 拒绝、moment Newton 拒绝、其他 evaluate 拒绝、残差不降和接受。完整原错误字符串始终保留，分类未命中不丢失证据。被拒 evaluate 的 stage 输入仅保存该有限状态小向量，便于后续精确重放单 stage，不复制整套大数组。

worker 把这些元数据写入独立 JSONL，把有 stage 坐标的被拒输入写入独立 gzip。写盘回调放在原数值 try/catch 外，I/O 错误不被冒充为数值分支拒绝。没有改 root 初猜、降低 projectionFloor、改物理度量或修改 PDE。恢复状态的原目标 `cutHeight` 原样送入。

`scripts/db6f-prefix-tail-trial-run.py` 只执行一次真正 DN 请求（`jacobian=True,audit=False`），不解 prefix BVP。首次诊断设 `maxIterations=2`，原配置只替换恢复输入、步数预算和独立记录路径。有限预算后仍未达到原 tol 的状态必须保留为未收敛。方法预期先复现 M15 失败点范数约 $6.60078222010092$，是否逐位一致及 trial 原因须由实际输出判断。

所有输出均有独立 stem，不改旧 FAILED/UNCONVERGED 输入。重跑命令和实际 source-map/config/input hash 由 runner 在启动前写入 `-reproduction.json`。原完整求解结果与后续诊断的可发布清单分开保存。

首次启动 `m15-trial-replay-01` 在初始化前因 shell 已建立同 stem 的 stdout log，被过宽的“不覆盖旧输出”检查拒绝，实际 exit 1，未调用 DN。该 log 保留。runner 随后只豁免精确的 `-run.log` 文件名，数学代码未改，实际诊断使用全新 `m15-trial-replay-02`。
