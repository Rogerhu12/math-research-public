# 真 A 数值现场恢复与新的 loop 控制响应

作者：strong_amplitude（GPT-6 Astra Pro，AI 辅助），2026-11-14。

## 已完成的恢复

当前环境中旧 `/workspace/scratch/d1aa462cfc02` 路径不存在。现有 main 保存了真 A 接受主包（SHA256 `917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf`）及其全部接受 manifest 成员。原七个 raw 压缩数组由已有 `strong_gzip_chunk_recovery.py` 和原 recipe 恢复到新 scratch runtime；每件字节及 SHA256 与原记录相同，A 原 raw 和 fixed-view raw 的全部数组引用均已实际读回。没有重新求解 A。

原 half-positive 的 r5/r6/r7 现场、J/QR 和 iteration2 文件不在此检出及旧目录中；因此不能宣称续跑 back8。已推 `2026-11-13-strong-currentA-positive-gap-tail1-r1.json` 中 size factor 1 的正幅 LP 方向取半，其完整核心轴差为
$$\frac{0.2506381129076958+0.2586381130462596}{2}=0.2546381129769777,$$
与交接记载的半步目标一致。这仅恢复设计方向，不恢复其旧 Newton 状态，也不是新解。

## 正在计算的新增输入

真 A 的采样最大曲率在 loop outward turn，而旧九控制响应没有 loop 曲率、半径、速度和 terminal peak fraction。新增入口 `strong_20261114_loop_control_response.py` 对这四个现有 provider 物理参数计算实际全场响应。修正版保持完整 97 状态、32 个核心参数、2590 网格点、原固定角图、原完整 H 和已保存 D-N 导数，执行原全/半差分及矩阵残差检查，不启动新的 tail worker。

第一启动在原 initial-laws parser 因缺少 frontload 字段退出 1，尚未构造 J。第二启动显式包含 frontload 的真实响应，未绕过该条件；其 J 已完成，但在检查原 Flow 时发现仅改 cfg 会复用旧 finite bridge，故主动停止，未消费任何新增 loop 列，不能算完整响应。

修正版对每个外部扰动同步重建原类 `NeckTerminalBridge`，只改变有限 prefix connector 的 `_prefix_bridge` 标签；真实 infinite-tail 的全部 cut 键（除该标签）及 parameters 逐项保持相同。没有扰动时返回原 port/bridge 对象。八个双侧原 provider 接口检查已实际运行，prefix→bridge 与 bridge→tail 的 $(a,a',a'')$ 最大不匹配为 $2.054\times10^{-15}$，记录及复算入口见 `2026-11-14-strong-resume-loop-bridge-check-r1.json` 和 `strong_20261114_loop_bridge_check.py`。这是接口检查，不是非线性解。

第三启动计划 `2026-11-14-strong-resume-loop-response-r3-plan.json` 使用修正的物理控制和独立 Flow 的四线程径向 RHS 评估。完整真 A 基准 J、全部尾 H 导数及全/半步门保持不变；数值结果仅在实际完成后报告。

这些参数用于寻找新度量的设计；不是同一固定 g 的精化。新的方向仍须实际非线性联解、完整物理几何与固定 g 加密后才能作为曲面候选。恢复和局部导数都不满足本题完成标准。
