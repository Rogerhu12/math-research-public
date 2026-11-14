# R133：旧α=.765作业的最后完整已接受状态

旧v15的会话28392后来在 `write_stdin` 中返回
`Unknown process id 28392`。当时原过程记录仍是 `complete=false`、
`status=started`，没有最终floating报告。原记录未改写成成功、数学失败、
资源失败或某个退出码；实际退出码和原因均未知。

此前已有三个实际接受的完整步骤。最后一个 `accepted-002.npz` 的SHA为
`41a9f0655efdfaffa6affed308015e33b4f13a4514cfdc709527c262f3f50915`，
原文件5479118B，1379节点、257状态，含每个状态及实际径向导数。
最后一步的步长为1/256，参数约为 (-0.03130143137036608\)；
其仿射不变成本由约230.6811减到230.2638。
这些数据不是原作业未观察到的最终结果。

为完整保存这个可恢复检查点，使用
`scripts/fourfold_codazzi_preserve_accepted_checkpoint.py`，按原SciPy
相同的 cubic Hermite 构造从全部 nodal 状态和导数生成完整
(4\times1378\times257\) 分片系数。
此转换不求解任何方程，不改变检查点，不推断原进程结局。

新完整索引为
`2026-11-13-R133-alpha0765-v15-last-accepted-candidate.json`，
SHA `c1a8df23d05e6934fc7ba82fe2d2be501d97ef198205b12b2ecb705eb34bb69c`，
与五个 `candidate-part000..004.npz.gz` 一并保存，每片小于5MB。
保留报告记录原输入、过程、日志、检查点、转换源码和新索引全部SHA。
完整原stdout保存为 `2026-11-13-R133-alpha0765-v15-original-partial.log.gz`，
原未完成process JSON也原样提交。

本项只恢复明确已经产生的完整数据，不宣称α=.765的有限边值已收敛，
也不将缺少终局记录归因为OOM或Jacobian奇异。
后续主体工作已接到保全部物理边界/均值的互逆变量256模实际求解；
任何新的成功或失败都须由其自己的完整报告判断。
