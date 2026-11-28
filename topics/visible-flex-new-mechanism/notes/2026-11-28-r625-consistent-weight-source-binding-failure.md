# R625：一致权重范围第一次触发的源绑定失败

会话：`Astra-new-mechanism-8cdb3418-20261128`。这是一条执行记录，不是数学结论。

`run 46117473160 / job 140894404467` 从源提交
`ba0bea5b36dfbce30eb064a8f2113e43acc20b86` 触发，2026-11-28 06:38:03 UTC
自然结束为 `failure`。runner 已 pull 公开仓库至
`ae7cacf7325bf7a5f2de2a186f4408c22431f864`、私有仓库至
`27a2d4a0977a43704b951d83f68fc4448bcebd65`，两份公开规则与私有根规则的
blob 均未变化，队列仍为本会话进行中。runner 一次读取旧原始射线日志，耗时
`0.4312563780000005` 秒，1032805 字节，SHA256
`e7747cd2e6501bca4380bce37e2366b0a5034ecbfb6b98027c3b95c7ae1690f4`。

随后在源文件校验时报出
`source hash differs: topics/visible-flex-new-mechanism/notes/2026-11-28-r625-original-ray-natural-terminal.md`。
请求中的旧 SHA256 为
`722dcc54c8ae46e1dbdb6449fa870d36e35ef02a5bde298a28a233750e5a30f7`，发布后的
实际文件为 `1a79257989b082793924a5745f98e2969d3143e2098c45a6ec0fa01f77118029`。
该检查位于数值依赖安装及科学子进程之前，因此本次没有运行科学求解、没有新
Jacobian、方向或 trial，也没有新的候选状态。旧射线终态仍是下一次的真实输入。

只将请求中这一项 SHA256 同步为实际文件值；求解源码、完整十九态输入、固定权重
策略、物理盒及绝对完成门均未改动。失败 job 原日志为 201792 字节，SHA256
`108e87ceaaa6e0951db76bd89168a74c90910e24bd1f797ef317de7038d4d02c`；不提交该可重取日志。
