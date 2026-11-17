# q060 同一新高度的原生 parts16 终态

**数值证据：原门未通过。**

此前 parts16 run 只有[观测缺口](2026-11-18-q060-nested-parts-observation-gap.md)，
没有返回码。本次使用同一源、同一完整输入和同一 parts16 配置，仅换新
输出路径，观察器实际取得了终态。没有回填旧 run 的返回码。

输入仍是 `beta4625-q060-local-tail-retry/seed_tail_0003.json.gz`
（SHA `6059334fa00c9fe6ce4bca788dff852f4da0988b920c5ad7e7f22b7fad65e35b`）。
完整八维物理 $H$、全部物理参数、$M=8$、spacing3、N128、depth8、RK16、
maxIterations36 和原严格 $2\times10^{-9}$ 门保持不变。
与原 parts8 请求相比只改 shootingParts 为 16 和 initializer/trace 路径。
原 worker 自行进行 nested remesh，然后真正调用原 nonlinear DN。

session19362 于 2026-11-17 23:44:34 UTC 得到 observer 真实 exit2，
观察时间 202.294 秒；probe 时间 201.195 秒。
原范数经过四个记录迭代，从 $50.7982911336314$ 降到
$3.6679653980984485\times10^{-9}$，随后原 line search 在 iteration3 失败。
最后 minA 为 $.5219178057511858$、minD 为 $.9991195608601376$。
失败不是根域 A 已负的证据，也不证明根不存在。

原始完整 native record
`closed_work/q060-call3-parts16-v2/seed_tail_0001.json.gz`
的 SHA 为
`c2c80ef0372cf5cccec24ab8e8c33b11bcd1b87c989d2a4e6f8e60d0986ae64a`。
它保存了 $1153\times16$ 失败状态及 9 个 raw node 边界。
原请求的 Jacobian/audit 标志均为 true；由于原 solve 失败，**没有返回
完整 Jacobian 或 audit 结果**，不能将请求标志写成完成了审计。
没有调用 prefix solver，没有接受新尾，也没有分段加密收敛结论。

入口为
`scripts/resume_transfer/probe_original_tail_nested_parts.py`，
源 SHA
`9e1c91f92beb12bd0d85da789ab5d7e10a487a4f599bcc005761de6334f29cfc`；
调用的原 client/worker、runtime 和 sparse helper 均未改。
完整命令、参数、输入/输出/源哈希与实际终态见
`scripts/resume_transfer/q060_native_parts16_terminal.json`。
完整状态、trace 和运行输出只留 scratch。

接下来只对这个新的 parts16 失败态做一次原 full-Jacobian 残差定位，
区分具体主峰、ULP 与局部传递尺度，再选择有依据的精度或初值方案。
不从 $3.67\times10^{-9}$ 这个单标量盲目再升 parts32，也不重启已经停止的
局部候选家族；前缀联立仍须等一个实际通过原门的尾结果。
