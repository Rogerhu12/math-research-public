# q060 同请求 parts8→16：无终态观测

**工程记录，非数学失败或接受结果。**

在三次局部候选均未改善后，使用
`probe_original_tail_nested_parts.py`，直接调用原
`950f-tail-client-v3.py` 与原 worker。输入为已登记的原 call3 完整失败态
（SHA `6059334f…`）；完整八维物理高度保持不变。
配置只改 shootingParts 从 8 到 16，以及 initializer/trace 路径。
保持 $M=8$、quadrature $128$、depth $8$、RK steps $16$、
maxIterations $36$ 和原严格 $2\times10^{-9}$ 门；
请求 Jacobian 与 audit 均为 true。heap3072 只属于资源设置。

原 warm-remesh 处理嵌套分段；原 worker 已开始实际求解。
session68353 的有限进展如下：

| 原迭代 | 原归一化残差 | minA | minD |
|---|---:|---:|---:|
| 0 | 50.7982911336314 | .5220201874037915 | .9991195608486535 |
| 1 | .11564303278765951 | .5219178056676257 | .9991195608601366 |

最后 worker 记录为 2026-11-17 23:35:47 UTC 的 iteration1 correction；
最后观察器记录为 23:36:04 UTC、状态 observed_running、returncode=null。
23:40 UTC 查询原句柄返回 `Unknown process id 68353`。
目录没有 observer 终态、probe summary 或原 native response/checkpoint。
当前工具进程清单只覆盖当前 sandbox namespace，不能据此断定旧宿主进程
已死亡，更不能推测 OOM。没有从这两步推出收敛、发散或不存在结论。

完整配置、原输入、命令和 8 个原 client/worker 源、31 个 runtime 源、
当前 sparse helper 与 probe 的哈希，均已在 scratch 的 `seed-entry.json`
中固定；本仓库保留入口脚本及
`scripts/resume_transfer/q060_nested_parts_observation_gap.json` 的紧凑来源。
旧目录和原源未改。后续同源新输出前缀重试若产生真实终态，须另列新
运行记录，不能回填本次缺失的返回码。
