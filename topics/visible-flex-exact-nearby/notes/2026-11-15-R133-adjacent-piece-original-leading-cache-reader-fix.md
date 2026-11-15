# R133：两相邻物理分片消费器的原缓存字段名修复

2026-11-15。实际公开 Actions [43675153388/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43675153388) 的首次科学子进程退出1。四个对象身份门已通过；244个仓库输入与6个原始整件案例均通过身份校验。失败发生于读取既有 Taylor 新增阶数，**完整新自然阶段为0，新完整源行为0**，没有可宣称的新数学缩界。

## 实际失败与不可混淆的记录

- 原科学源 SHA256：dd0cd5511e88d589ebbb8d6084cf80ccaa2488d034e9f31f24eb52d5d2b91b1f。
- 原244输入 manifest：09c89e02b98915040f183560ed9d0ea31c5eeb683ad4bb3d056a74d4407aa10d。
- 原失败 native：22719 B，SHA256 96eca2c7465a9491dfce6102c95a50ec3315c5e2b99c1f9af47f484b1bda5c26。
- [原 process](correlated_adjacent_piece_first_Airy_sources_ci/run-43675153388-1/consumers/process.json)：4367 B，SHA256 b4e0091c5c20e888733a77ae2bf549471ba449cca73b5966ba11bc2640fc0cdc。
- [原 worker process](correlated_adjacent_piece_first_Airy_sources_ci/run-43675153388-1/worker-process.json)：4430 B，SHA256 f9f43ad0632b70e5cf89176d6f800b2da3ceab207565d90a7175f68c8ac6fcbd。
- 实际启动了1个新科学子进程；它在1.2168383070000033秒后以 ValueError 结束。worker 所记2.920538289999996秒包含消费器开销，不能写成完成数学的用时。
- 准确错误为 a saved appended leading degree changed。没有重新计算任何旧 target、FFT、intrinsic、原根 cubic、有限系数、既存范数、矩阵字、phase profile 或原外源行。

上述原失败文件保留，不改写为成功。只有修复后公开 Actions 的新 process 才能说明后续结果。

## 与原生产器逐字对照的一行修复

既有生产器的 append_series(name, previous, degree_count, build) 在阶段 payload 中保存 name=name。其调用为 append_series("leading-"+key, ...)，所以9至14阶保存的 payload.name 是 leading-G、leading-T 等。0至8阶的完整旧 leading prefix 则继续使用裸 key；两种原格式都必须准确保留。

新读取器在9至14阶的校验从 v["name"]!=key 改为 v["name"]!="leading-"+key。阶数、文件名、完整 coefficient payload、source/manifest/algebra/runtime 身份门均不变。0至8阶的读取没有改动。该修复不改变数学表达式或任何已有数值。

修复后的三件为：

- 科学源51519 B，SHA256 f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739；
- 原路径244输入 manifest 仍83150 B，仅上述科学源的 bytes/hash 更新，SHA256 76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a；
- 原 workflow 仍6597 B，仅 manifest SHA 更新，SHA256 de81591847d94e9bc8fbcd68d5ee7d5457425918d382b0e59de0108f439cc09b。

其他243个仓库输入、6个外部原始完整案例、CI、worker、algebra 全部逐字不变。原失败没有完成阶段，所以没有跨源身份迁移的阶段，也没有放松 resume 检查。修复推送后由本公开仓库的 Actions 重新消费同一原数据。

本条仅解决 reader schema，不支付尚缺的修正 seam 算子、正权端口、强返回、截断充分性或整个无限维闭逆。
