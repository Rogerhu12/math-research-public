# 执行器更换后的强分支恢复

07:46 UTC 左右，session94301 的轮询返回
`executor key changed during session recovery`；新 shell 也暂时不能启动。
随后 root 找到新执行器的入口（`shell="bash", login=false`），确认旧工作树
未推文件已不在新环境。本次恢复目录是 `math-research-recovered`，从 main
的 `7f2191d504f55128229357b5dea992c1176f931a` 接续。两 README 的核读与
Git/HANDOFF 更新由 root 管理。

## 恢复了什么

以下源代码由会话中保留的完整原文恢复，并实际比对了原先记录的 SHA256：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| strong_checkpointed_tangent_bvp.py | 16183 | f75bbcd1b67c05335761966973acb7407ad0bf4f5422f5708639467c1a2afb05 |
| strong_small_batch 的首次严格检查版本 | 8866 | ac121bbdc82a7e153ff8225282bd43f58ce3ee077540f25bca856654ee342c0a |
| strong_frozen_calibration_factory.mjs | 14557 | 77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247 |
| strong_frozen_calibration_check.mjs | 4874 | 711bd993db037c5b4f58020b31b021c89a93a8ded9bcee0595aeb7ccb5cc1780 |

small_batch 的首次版本保存在 `strong-small-batch-before-fd-check.py.gz`。
现行源码是在精确恢复的该版本上重放原会话 FD 操作数诊断补丁，SHA 为
`2b1d3edc9b9a645bea98d191b2d74dbae0c4506f128259cdb263e304f995612e`。
生产 BVP 路径、方程和验收没有变化。Python 源均已重新编译检查。
冻结工厂由 tail_refinement 协助逐字恢复，未运行 Node。

旧 toy 观察等价验证时使用的 writer 也通过逆向删除后来新增的真实零步
检查分支恢复，得到原 SHA
`52e27282b4e0fbcb70b87f854060685e195c6525fe9fca159b0d4d3ef2701612`，
已存 `strong-checkpointed-before-real-check.py.gz`。这证明文本重建一致，
不等于重新运行数值验证。

## 三个状态必须分清

1. 旧 session72974 已实际 poll 到 exit0。真实 q090/M20/N512 的首次保存和
   恢复均为零 Jacobian，891点，x/y/p逐位相等；两包约2.09MB，峰值分别
   143044和149660KiB。其原 NPZ 目前不可访问，不能把保留的摘要当恢复包。
2. 旧 session29445 已实际 exit1，属于**实现比较未过**。RHS、状态Jac、
   collocation、midpoint、A/B及BC逐位相同；中心差分参数PJ最大差
   3.025309158743994e−8，超过事先的逐元2e−10比较门槛，P块最大差
   5.7771073435295464e−11。不是非线性 BVP 失败，未产生新曲面。
3. session94301 是针对上述 PJ 的 F+/F− 操作数复核。执行器更换前没有
   观察到它的退出码或结果，终态仍为未知；不得写成 signal9、OOM、成功
   或数学失败。原 checkpointed c6eighth-r1 从未启动。

全部可保留的实际数字、原包哈希与缺失状态集中在
`2026-11-12-strong-executor-recovery-observations.json`。该 JSON 明确只是
从工具观测重建的恢复记录，不冒充丢失的数值原包。

## 后续精确命令

`2026-11-12-strong-recovered-continuation-plan.json` 使用新的
`small-batch-fd-recovered-r1` 与 `c6eighth-checkpointed-recovered-r1` 前缀。
先重做实际 FD 操作数检查，再求同图 c6=−.00037189361930905265 的小步：
M20/N512、tol1e−6、max2000、direct-block QR、cache8、radial16/interval12。
每个入口及接受的 Newton 状态以唯一 NPZ 保存，读回验证后原子改名，
保留最近两包；它们始终标为未验收。最终完整 RMS 与物理审计仍然必做。

冻结校准接口是异步导出 `createFrozenCalibrationFactory(config, options)`，
返回 `{factory, manifest, reference, verify, physicalModeColumn, idealModeGraph}`。
`factory.assemble()` 明确使用保存的全局 warp alpha；原160层与far170的
辅助计算、物理积分顺序保留，仅n<160的校准调用读保存的二进制alpha。
原 cal 除alpha外的六项诊断缺失时抛错。该接口的五/七点历史指纹对照
仍需独占运行，当前不能称运行验证通过。研究 task 未完成，继续实际延拓。
