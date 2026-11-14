# R133 恢复链第 5 步：恢复原 tol 2e-9 的 5814 节点候选

2026-11-14 实际重新执行完成，正常返回码为 **0**。本条只登记恢复的有限候选与其完整输入身份；没有把有限 BVP 成功改称连续 PDE 或完整高频逆。

## 实际执行和原数学门

沿用 [原六步重放链](2026-11-13-R133-final-moving-replay-chain.md) 第 5 步的原生产器、全部数学参数、全 Fourier 与 mean/ν 行。只替换猜测、输出、完整 accepted 检查点和 QR 临时目录，并明确设置 4096 MiB 地址空间上限、单线程 BLAS。原生产器 SHA 是 `5b019896c9b5cb50b24da0f349bc2266e6d4585795b8b2c8fdd1150496f4015c`。本次完整命令与实际进程结果见 [2026-11-14-R133-final-replay-stage05-process.json](2026-11-14-R133-final-replay-stage05-process.json)。

- 输入完整候选 SHA：`6c3bab3e53e6e0eecc960f692d005054360e8a749255e46ac26ccdbbab08b7d1`。
- 实际节点数：5814；完整有限门 `finite_BVP_success=true`。
- 原径向 RMS 门实际值：`1.9999073421885831e-09`。
- 精确二进制有理参数 ν：`-80394554034525/2251799813685248`。
- 进程实际用时：374.987641 秒；最大子进程 RSS：391984 KiB。
- 完整浮点报告 SHA：`5654861efa753d3dc316d4d0da4de3380b68167cc2b52a9db95af77119b64374`。

所有实际 accepted 状态及其径向导数均留在该步 `checkpoints/`；最终 PPoly 是原程序由完整节点值及导数生成的同一 Hermite 对象。完整内部与物理边界诊断正常执行，没有为缩短重放删掉诊断或放松原门。

## 恢复对象与范围

完整索引 SHA 为 `5a3fec4ebe832d59347bbf79e5675e88db76846aad87fdd045c5bcf9763c8243`，与原链该步索引**逐字相同**；索引中的全部分片、区间覆盖及 SHA 见进程记录。恢复位置：

`/workspace/scratch/ac0d699811ad/replay-final-20261114/stage05/moving-m32-alpha0765-tol2e9-candidate.json`

## 可重放方式与存储

可用 [逐步原程序运行器](../scripts/fourfold_codazzi_final_replay_stage.py) 复跑；其 SHA 是 `43ed8f5de77118103fe60e250e348e853b6cce2353550d5e1a5e4b9a2591bf7f`。`--stage 5`、`--guess` 和全部实际命令已在进程记录保存。原生产器与输入由现有六步链严格绑定，下一步只消费本步完整输出。

遵根 README 第 11 条，可由原输入和脚本确定重建的大数组、完整日志及重复浮点报告保存在上述独立工作目录，不重复提交。Git 保存本小记录、实际过程清单和必要的最终科学身份对照。旧失败、暂停与未知退出的记录保持原状；本次正常返回不能改写旧进程结果。
