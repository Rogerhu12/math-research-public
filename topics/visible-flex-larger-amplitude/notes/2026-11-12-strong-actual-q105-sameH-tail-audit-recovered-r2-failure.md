# recovered-r2：较小资源的正式失败记录

session25392实际poll到exit1；worker before/after close均−9。heap256MiB、point cache2，
其余原M24/N512/depth8/steps12/parts8/fullJac+audit/tol2e−9及全H保持。
wall180.289569s、wait4 peak383756KiB、user29.126849s/system1.902015s。
这些数字没有确证终止原因；不称OOM、限时或数学失败。

174.276s ready，五/七点历史指纹与全部stored物理参数通过。trace保存了完整原H
request，但没有geometric_amplitude_warm完成事件、第一Jac返回、接受试步或新恢复包。
因此本次没有新数值状态可接收，latest实际恢复仍为recovered-r1保存的iteration0。

较小资源方案未给出成功响应。后续将准备显式严格同离散的原样raw暖启动入口，
全参数、全部577×48状态、rawNode/rawStates和完整H逐项核对后，避免不必要的Q/L
重映射和ratio1转换；仍执行原Newton/fullJac/full audit。该新入口尚未运行。
旧已推r1的5.560497e−11试步只是可用暖点，须重新经过完整验收，不冒充已丢失29674包。
