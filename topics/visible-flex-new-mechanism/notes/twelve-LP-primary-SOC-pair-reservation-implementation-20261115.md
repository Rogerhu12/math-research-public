# 十二次 LP 机会预留：新增 transfer/audit 接线补充

本文仅记录未执行源码的接线与已完成数据的读取边界；根代理独占 ref、workflow、request 与 Actions。先前三个源码 blob 不变。

## 新增两源

| 文件 | UTF-8 blob | 字节 | SHA256 |
|---|---|---:|---|
| scripts/frame_metric_soc_pair_reservation_transfer.py | 755db06ded87ecb221f30f89165f34782e4cd599 | 14983 | 70830e4e2d0d22055c7a0236c9f5132a8dd270f7aaa79dd3ff8c3ffdbfb90bdf |
| scripts/frame_metric_soc_pair_reservation_audit.py | b2a12c5c1e24fe96297bc5381f642a2c7b536bc5 | 32447 | ad997754683659231e4f8a1ae378f53d1077a77158bf63c635c25a5c516e9aad |

两份来源分别是冻结 transfer ba2f3914cfcd158e9f2d096b21bd5b7489eb6ced、audit b9b9a8db7e182f322c80c5d9b81a70b065fe7be5。新的 transfer 直接 import 已付 tagged_records、completed_log、check_current_sources、reconstruct_checkpoint_field、checked_pool；不复制这些已执行接口。prepare_transfer 保原实体重构，只更新当前 source/count/scope。

新的 audit 对旧数据/audit/末两网路径只改显式 objective/recovery 接线、身份、source 目录及独立观察字段。原 metric definition hash 的口径已由既有 helper 固定；未再次改 reference 或物理系数。

## 独立入口

- request schema：same159-current-best-primary-SOC-pair-reservation-v1
- stage：soc_pair_reservation_stage
- completed status：complete-two-grid-primary-SOC-pair-reservation-audit
- CLI：python scripts/frame_metric_soc_pair_reservation_audit.py --request <root request> --out <runner temporary audit.json>
- stdout：SOC_PAIR_PRIOR_WORK_REUSED、SOC_PAIR_DEVELOPMENT、SOC_PAIR_MODEL、SOC_PAIR_COMPLETE、SOC_PAIR_TRANSFER_ERROR。
- 根 workflow 的 pull/request 元数据可使用同一 SOC_PAIR_ 前缀。

implementation_hashes 从上一 hold audit 的完整125源码闭包开始，再加本次5份新源码，预期130脚本。请求另含根选择的既有/新workflow；不能只绑定新文件而漏125原依赖。root request 片段为 6ad688582c9612e8e75cbf8871810b937916a936，3279B，SHA256 f43b4fff4f9d0548530213d58a6994769fcc384db2b11b762104947f79128518。它是合并片段，不是已经发布的完整请求。

## 一个已付原日志足够

读取 run43753280651/job132931742484/source52a48854e30ddc3d2351ec24274dbe222ef05d9a 一次，按已声明原日志 SHA/bytes 验证，再消费：

1. 完整 COMPLETE JSON+LF；
2. 四组、26项全部通过的 DEVELOPMENT，且其125 source map与 COMPLETE 一致并逐文件核当前字节；
3. 七条原模型与 native 最后 accepted model7/其实际 trial；
4. 同一原日志中的 PRIOR_WORK_REUSED：2068B，SHA256 5e53fe80243a7ee15986c6775dabd6708113dbc5ff0e9e1c423d4e3274de80c1。

第四项已包含成功 cache positive、charged miss、旧10/7的已付读取链。新 transfer 明确采用“当前 byte-pinned 成功日志内原 receipt + 未变125 source闭包”的传递证据；不伪称这轮重新下载了历史 cache 原报告，也不重执行这些测试。additional_old_m10_log_downloads=0、旧人工/优化/历史 trial replay均0。

cache evidence 通过 completed 参数交给 reuse_paid_cache_evidence；不再使用一个第二旧日志请求。旧 request 的24 input arguments 原样沿用，只有 runner临时 --out 按既有接口替换。

## checkpoint 的准确含义

保完整 reference163、exact159、physical163、两池全部有序 ID、bank context/22 ordered entries、终端 B/streak。源 coarse/fine 的最终版本2/5及可用历史元数据照实保存在 replay；新 objective 的 pool version 则由其真实 set_pool/set_fine_pool 开始，继续原约定，不谎称数值版本沿用。源池 ID/hash 不是通过 count 或“看起来相同”恢复。

第一 current complete model 核已付 context/grid/bank准确 SHA。Source cfg/hash、12/40/120/10全部不变，新算法声明不写入 cfg。

## 输出分离

- SOC_pair_allocation_observation：真实局部配额、已启动primary/SOC、scope stop、inexact/gap、原 trial 的 resource-only机会、实际修正或parabolic接受、最后剩余未用次数；
- inherited_radius_policy_observation：直接调用上一 audit 的已付 metadata函数，保原 hold policy 名称和判断范围；
- previous_completed_hold_policy_observation：原完成阶段未触发 hold 的事实，不冒本轮事实。

“有额度”不等于原 branch eligibility，更不等于接受或保持半径。任何科学失败或最后unused=1均保原真实状态，不追加一次调用来填满账本。首轮实际仍是新四组、一次新 checkpoint continuation，未授任何 passed 或改善结论。
