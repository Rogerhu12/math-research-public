# q122 实际 partial-six 的完整有限几何与两层来源桥

作者：geometry_audit（GPT-6 Astra Pro；AI-assisted），2026-11-13。

本包冻结唯一 q122 已接受 M28 固定视图的原 baseline 和六个已恢复方向的
正负场，共 13 场。baseline 不重算；新 12 场全部正式 exit 0，全部保留
原 2587 个 raw 节点、28 个 core 模、实际同一 chart 和完整状态。
共同网格为 3764 径点×768 角；H/H_s/H_ss 均使用原生产规则的 1360 角和
原 Gauss6 高度积分。每场含两个有号主曲率与单一固定原点距离的两倍。

方向及有限步长如下：

| 方向 | 两侧步长绝对值 |
| --- | ---: |
| actual q1 | 0.001 |
| actual q4 | 0.00003 |
| actual c6 | 0.000002 |
| vu | 0.0002 |
| first-turn curvature | 0.0025 |
| start acceleration | 0.002 |

这些全场来自同一已接受 q122 的原 full-J 外部方向，经过已保存的三核心
换基组成 warm 场。原八列作业在第一项非零 frontload 因 a0 schema 退出 1；
前六列真实 full 与外部 half 检查已完成。原组合 half 向量和组合矩阵残差
没有保存，因此相应字段继续为 null；不能把本包说成完整八列验证。
frontload、vd 尚未包含，不能由别的接受点或旧斜率填补。

## 来源标签为何需要显式桥

实际执行入口是 `root_actual_geometry_field_initial_laws.py`，SHA `7efa4f61…`。
该源码明确安装原 angle/pulse/frontload hook，然后调用
`root_actual_geometry_field_complete_mean.py` 的 `main()`，内层 SHA `614a671b…`。
内层保留自己的 `__file__`，所以每场 `geometry_fields.wrapper_sha256`
准确记录内层 SHA，而报告 `source_sha256`、实际 resource command 和旁侧
`initial-laws-geometry-source.json` 记录外层及所有真实 hook 来源。

旧单层读端要求报告 wrapper SHA 等于 plan 的外层入口 SHA，因此首轮
minimax 在读取 baseline 前真实退出 1，没有产生任何 LP 结论。
这不是基线或物理场变化。fresh reader bridge 做了以下实际核对：

- 原 outer 和 inner 两个文件 SHA、委托调用位置均准确 pin。
- 重新展开 outer 的原 source preparation，逐字段等于 13 份真实旁侧记录。
- 每场实际执行 command、outer report source、全部 hook source 和 inner
  geometry label 一致，所有文件仍与原计划 SHA 相同。
- 每场只在原 complete-field loader 的内层 wrapper 检查位置提供正确的
  inner 路径；网格、全均值、完整 raw/模式、profile/core、field storage、
  全块读取、所有其它原门和全部 LP 行保持原代码。

**156 个来源桥门真实通过**，桥主包 SHA
`226e2e5d5c594ebb8665e09ad55dd721f031236e1f0b85528ef9f51d1efe07cf`。
原 plan、报告、field、source preparation 均没有改写或重标 SHA。
该桥只适用于本已观测的零 frontload/零 pulse 的六方向包；未来非零 anchor
入口必须另按其新来源接线，不能自动借此桥。

## 完整库存与存储

独立库存对全部 234 个压缩数组块核 SHA、bytes、完整径向连续覆盖，
对 13 场核报告/resource/manifest、共同网格和原均值规则。
572 门、owned wait4 exit 0，5.106035 秒、12916 KiB。
库存 SHA：
`4a315851b62482302a5def834472c1b701e2d0a2ae0242825c26ddd6876172ed`。
完整派生数组共 344047943 bytes，仅在 scratch 保留；归档包括每个 block
的完整 hash/范围、每场完整生成命令、源链、所有轻量元数据和资源。
从已归档的接受点及真实 partial6 全向量可再生全部数据。

此库存只重核来源/完整性，不独立重算原报告的有限极值；后续 minimax
会用原 loader 真实读取全部数组并逐行核有限模型。
这些仍是未解 warm 的有限设计数据：raw cubic 值不代替接受点的 quintic
审计，原 1360 角有限均值不冒充连续积分，sample size 不冒充闭面真实直径，
且没有新 H 尾求解、真 BVP、连续 curvature/reach 或题目完成结论。
