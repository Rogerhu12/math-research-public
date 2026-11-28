# R73 同一最终新图：连续 metric 实际通过

2026-11-28，Astra-held10-7c4e33ee-20261128。

[R74 完整证明](../results/R74-same-new-cartesian-prefix-continuous-metric.md)记录本次真实运行给出的范围。对象仍是本会话真 λ=.002/M24/879节点源的945节点最终 Cartesian 图，未附尾/cut。不是旧631点 R62 图，也不是原 physical 函数/mean primitive。

| 已执行步骤 | 实际返回 |
|---|---|
| 完整真核/中心0至3阶角表 | 1536个闭盒/准确三重扇区；237.048885478秒 |
| 原径向分段 | 964片，含全部共同节点、真profile/bridge/target joins |
| 实际自动二分 | 503次 |
| 全部接受径向叶 | 1467，无未决片 |
| 扇区覆盖 | 2,253,312盒；全圆等价6,759,936盒 |
| 连续相对metric算子上界 | 9.899331346061255e−7 |
| 准确有理预算 | 99/100000000，严格通过 |
| 主验证 wall | 789.251783560秒 |
| 同一 R73 图的定义绑定 | 全部十组原定义数组逐位一致 |
| 原非线性BVP/尾重算 | 无 |

独立源审查见 [analytic-cartesian-metric-formula-review](2026-11-28-analytic-cartesian-metric-formula-review.md)。它核公式、同图合同和覆盖推理，没有重复运行区间证书。当前目标 provider 的 entry 单点第四槽是前缀侧三阶值；本次 metric 仅读取半径前三槽，未用它声称桥右侧三阶值。

## 原始小记录与哈希

以下 JSON 是实际输出的逐字副本，没有把摘要改写成 solver 返回。

| 文件 | SHA256 |
|---|---|
| [连续度量完整返回](2026-11-28-new-prefix-continuous-metric.json) | `b762fae9126112612ad2078f1222f4616f0607deec06a4f87d5bb9c5aa143646` |
| [角区间表生成记录](2026-11-28-new-prefix-metric-angular-tables.json) | `5872e2cb713de30d30778043114b4b2ebc8fdb0d3ae08f428d5f8040f139b995` |
| [准确覆盖和R73同图绑定](2026-11-28-new-prefix-metric-exact-cover.json) | `bad816814dde16da33edf0cd75132b800e7a489e6fa3e74b096006af070f198f` |

原真实 source run SHA为 `1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891`；raw为 `4f5033800dab66e46125d8e88fc4d0eb4dbacfc5dd6d1bd8f7808a74f9193616`，physical为 `b9a61ae87a80f550daf98417e0cf2c39d12e3150a974fb8c904aa3d21cc7d1b0`。该输入的必要再生已在本会话恢复记录中登记，不把其恢复当作新数学结果。

本次角表和最终共同定义数组的哈希分别保存在角表生成记录中。完整角表、全部叶及可再生定义数组仅在仓外工作目录，不进 Git/Release。新定义数组比 R73 文件多保存 phase-chart 两jet；其余十组数组一一逐位相同。

## 实际复现入口

在仓库根，使用已有完整真实源，给每次执行一个不存在的新仓外目录：

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/geometry/cartesian_prefix_metric_tables.py \
  --source-run /workspace/scratch/7c4e33ee17de/held10-design-work/design-material-recovery-20261128/lambda002_m24/run.json \
  --outdir /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-metric-tables-20261128-v1 \
  --angular 1536

python topics/visible-flex-held-10pct/scripts/resume_20261128/geometry/cartesian_prefix_metric.py \
  --tables /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-metric-tables-20261128-v1/summary.json \
  --outdir /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-continuous-metric-20261128-v1 \
  --target 9.9e-7

python topics/visible-flex-held-10pct/scripts/resume_20261128/geometry/cartesian_prefix_metric_cover.py \
  --metric-report /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-continuous-metric-20261128-v1/summary.json \
  --geometry-report /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-interval-20261128-v2/summary.json \
  --out /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-continuous-metric-20261128-v1/exact-cover-and-R73-binding.json
```

上列是本次实际路径，重跑时改为新的输出目录并相应传给后继。主扫描前仅做过9个完整区间 probe 来检查执行接口，没有把 probe 结果当连续覆盖；随后全部964片从头完整扫描一次。准确覆盖后处理没有重新求区间/原BVP，只核所有有理叶端点、原上界与同图数组身份。

## 持续任务

本次付清了 **R73那张图** 尚欠的连续metric。它没有full-H/outer，不是λ1，没有准确H，更没有完成整个README。当前真实full-H、λ推进与同g精化继续；对它们形成的新场、外端修补和完整闭图继续支付自己的连续界。
