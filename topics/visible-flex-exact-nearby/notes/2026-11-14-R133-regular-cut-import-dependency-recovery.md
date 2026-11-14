# cut-to-waist 原提案导入依赖恢复

公开 run `43587619788`，job `132425396173` 的真实数学子进程退出码为 1。
原日志显示失败发生在导入链
`final_regular_head_model → final_head_trial_model → candidate_shards →
fourfold_phase_codazzi_two_end_probe → fourfold_phase_symmetric_geometry →
fourfold_phase_geometry → fourfold_phase_newton → fourfold_newton_refined`
的最后一次导入：`ModuleNotFoundError: poschl_teller_fourfold_series`。
模型尚未建立，实际已完成径向格为 0，没有可重用的数值 frame 前缀。

这次失败的原 artifact `14110908090` 为 2623 字节，ZIP SHA256
`d220009c278702a9618ab1981c546387bc849b6766fc8aeca7e054eed2a1942b`。
原 `process.json` 与 `producer.stdout.log` 均由该 run 保存；不改写此失败。

原输入 manifest 的递归选择只匹配以 `fourfold_` 开头的本地 module，
遗漏了现有 `poschl_teller_fourfold_series.py`。现按所有实际本地 module
文件名重核完整静态导入闭包，恰为 66 个 source；原 65 个 source 外
只缺这一个文件，其已经公开、且原主体 manifest 固定的 SHA256 为
`173634e9e305dfe12946b4bc792014f2e443f689fc3dd2f5e1dfd834210992c9`。

新增 `2026-11-14-R133-regular-cut-CI-pinned-inputs-v2.json` 保留原 manifest
的全部 80 个文件 SHA、参数、数学源、背景、连续修补定义、全 193×96
维度和权重定义，仅将上述未改原件加入实际隔离执行副本，总共 81 个文件。
旧 manifest SHA256
`da5049f248e070aef21ed03d62ca92495e60a6f976b86698d903b5aad67aa4d7`
及其对应原失败过程继续保留。

新的 workflow 只更新 manifest 路径及其准确 SHA，科学 producer 和
worker 字节保持不变。66 个固定 source 的隔离副本已经完成纯导入轻门；
这个轻门没有构建模型、计算径向格或冒称连续证明。后续真实提案计算继续
由本公开仓库 Actions 执行，成功格和任何失败前缀都按原规则保存。

这项修复不触发已经成功的完整 cap-cut 14 门，也不重算任何完成的主体行。
