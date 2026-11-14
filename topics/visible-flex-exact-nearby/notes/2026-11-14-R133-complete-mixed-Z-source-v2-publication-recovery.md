# 完整 Z 源计划的真实成功与摘要发布层恢复

原公开 run 43612904296 的 plan 数学 child 实际退出码为 0，wall time 15.000977661999997 秒。全部 7 门已通过，完整 7721 行源计划已经保存在 native：

`26a488b4347e0e30106e67dcd18b54e211dba6adecd7d2c029a4dc6ba097d95a`。

原 gzip 为 6916980 字节，按 4 个 lossless byte parts 保留。随后 wrapper 将路径表达式写成 `self.evidence/'complete-Z-source-'+phase+...`，Python 先计算路径除法，导致 `PosixPath+str` TypeError。因此原 process.complete 为 false；这不撤销已经实际成功的 child 或完整 native，但也不能把原整个 workflow 写成 success。

原科学源 SHA256 是
`90c90fb1b21806e803e61d5f850b1d8057fcadc577452d3454b05348500a697f`；
本 v2 不修改它、其算术公式、已成功计划、原所有输入或已成功 pilot 行。原 v1 wrapper
`84e0666e30f5d77fff393e7db40529f1c579ffa6bac13fbadd367252883cbb15`
及 manifest
`854261f57cc390f17659ec5ff9cdc83d98d8ef8b32b6b7b241c54fb3359075be`
也原样保存。

v2 的 plan 显式接收原失败 workflow 的实际 artifact。它必须同时核原 run、repository、旧 wrapper/manifest SHA、完整输入 SHA、真实 TypeError、原 child 退出码零、精确 native SHA、完整 7 门和全部 7721 行。不能要求旧 process.complete 为真，也不能由于新 worker/manifest 身份不同就丢掉原成功 native。

新 plan child 使用未改的科学源 `--phase plan --resume` 路径：核对原完整输入与计划身份后，逐字节复制原 native。新的计划 SHA 仍准确等于 26a488…；没有重算原基线或任何原 source 行。新的实际过程独立记录这次恢复，明确区分原数学成功、原发布失败和本次真实退出码。

唯一原有表达式修复是给拼接后的摘要文件名加括号：
`self.evidence/('complete-Z-source-'+phase+'-summary.json')`。
新小摘要仍在写入前验证 UTF-8 字节数不超过 60000。四个新 range 仍只覆盖既定的 1147 个未计算紧支撑行；原 14 个已成 pilot、40 个固定参数子格、全部 7721 真均值与完整 high 输出保持不变。后续消费不修改原失败证据，不重复任何已完成科学行。

本恢复没有新增 inverse 或响应误差结论；完整连续 $Z$ 的同一边界和未知高反馈仍分别接线。
