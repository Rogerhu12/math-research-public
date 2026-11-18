# q060：同旧高度原生接受尾部的前缀接续入口

本条冻结新的实际联立入口，接续
`2026-11-18-q060-warmup-two-neighbors-original-acceptance.md`。
它不是新的前缀求解结论。当前拥有的新增可用状态，是原 worker 在
相同完整 `H_old` 上真实接受的 parts16 尾部；原前缀和以后每个新高度
仍须分别完成原有验收。

## 已接受的 initializer 身份

使用
`closed_work/q060-warmup-two-neighbors-native-v2/seed_tail_0001.json.gz`，
SHA-256 `c57fe4ea23e90de71502666a40d5b0ccaa12c18f788e62e003ba5e2393e5f249`。
此响应的完整 H 与会话 33116 第一个实际 warmup 请求逐项相同；
响应具有 `converged=true`、原残差 `1.835729812540257e-9`、
208 个有限 Jacobian 标量和原 audit。没有把此前不同 `H_new`
的响应搬给当前请求。

完整原 H、原生请求、所有物理配置和来源 hash 载于
`scripts/resume_transfer/q060_coupled_same_height_parts16_entry.json`。
入口保留原 profile、原 q040 prefix restart、原 linear/restart ports
以及同字节 bridge/chart。`q=.06`、warp `.06`、M8、angular256、
audit512、初始 nodes801、maxnodes6000、原三项 prefix/boundary 容差、
warmup scale1 和 lagged-tail 选项均不变。

## 相对会话 33116 的完整变化

命令仅改 `--source-topic`、`--tail-config`、`--out-prefix` 三个路径。
配置仅改 `initialCheckpoint` 和 `traceFile` 路径；parts 仍为 16，
N128、depth8、RK16、原 `2e-9` 尾门均不变。
配置去除经逐项核对的 IO 字段后，与已接受原生 initializer 的配置
严格相同。

新 owned source 为
`closed_work/q060-recovery-resource-v3-source`。它由已冻结的
`prepare_recovering_tail_source_v3.py` 生成，原数学源保持只读。
与此前 owned source 比较，coupler 文件逐字节相同；
resource-v3 adapter 的唯一变化，是给已有候选子进程显式传入与
原 worker 相同的 `--max-old-space-size=3072`。候选集合、最多一次
候选和一次原 worker 重试的预算、全部物理方程及验收测试没有改变。

## 内解保存与后续请求

保留已审的两个保存 hook：内解返回后，在向原 worker 提交新的
candidate H **之前**，先保存原始 cubic/mesh/参数，再保存它使用的
真实 accepted affine-DN 响应、请求、配置和来源的 sidecar。
原始内解始终标记 `solver_success=false, actual_tail_accepted=false`；
只有后续实际请求通过原 worker，才能升级其尾部验收状态。

入口目录为 `closed_work/q060-coupled-parts16-hold-v2`，其中
`entry-plan.json` 保存完整命令、旧/新参数差异与全部输入 hash。
使用原 observer 记录进程、心跳与真实 wait 返回码。该准备记录在
启动前冻结；它不会把旧的缺失 cubic 重构成逐位原状态，也不会把
退出码 0 本身解释为前缀或整个课题已经通过。
