# TCF：原 TC 终态后严格补集上的完整 source 续接入口

**状态：源码已实现，尚无科学执行。** 初始检查时，原
[`46117170011/1`](https://github.com/Rogerhu12/math-research-public/actions/runs/46117170011)
尚活跃。生成器在这种状态返回 `ready=false`，不产生 assignment、manifest
或 workflow；不会竞争原 run 已接受或尚持有的 cell。执行者仍是 root，本文
没有启动、取消或重跑任何 Actions。

完整证明见
[TCF 终态缺格与完整聚合](../results/R149-supplement-terminal-missing-cell-fleet-and-complete-source-aggregation.md)。

## 固定对象

初始输入为原完整 manifest
[`2026-11-28-true-root-trial-complete2677-inputs.json`](2026-11-28-true-root-trial-complete2677-inputs.json)，
whole SHA `6b82d09170ed4ec780eccd0910cb69df98615390ef2f73237ed324d1e3f2c692`。
它决定全部原 184 current 文件、32 historical inputs、40 native parts 和
完整 direction recipe。新入口直接复用原完整 public input prefix，而不
进入旧数学目标。

原 7671×193×96 四个全端点数组全部恢复并核 whole SHA。原 7724 个 cell、
真 root、全部 96 列、五个 source 窗口和所有 physical/mean 条件均保留。
已完成 signed matrix/waist 及可能已完成的 negative source 文件均逐字复制。

唯一逐 cell 算术优化是：在同一个 cell 内，对**同一只读完整 Fourier Box**
缓存第一次完整 Legendre 变换；离开 cell 就释放，窗口 norm 及其全部误差
和累加照旧。没有改变 source、trial、投影或有向运算次序。原完整 cell text
SHA 为 `5aee786a11a3fddce44a114e46c5055fb28a15c9c280631fb60e9f1f207623ca`。
尚无速度倍数声明；actual 会记录完整 cell 时间和 memo 命中。

## 全部新文件

| 文件 | 职责 |
| --- | --- |
| [fleet.py](../scripts/fourfold_codazzi_true_root_missing_cell_fleet.py) | 整父终态、完整 accepted union、互斥补集、单格 memo、精确上界聚合 |
| [fleet_owner.py](../scripts/fourfold_codazzi_true_root_missing_cell_fleet_owner.py) | 全输入准入、四全数组恢复、只算缺失 cell；独立最终聚合科学模式 |
| [fleet_public_worker.py](../scripts/fourfold_codazzi_true_root_missing_cell_fleet_public_worker.py) | 原输入恢复/容量/pull/rebase 闭包、共同父锁、assignment 唯一标记及完整 prefix 发布 |
| [fleet_merge_public_worker.py](../scripts/fourfold_codazzi_true_root_missing_cell_fleet_merge_public_worker.py) | 所有固定 jobs 真终态后收集整个并集，逐条新结论 push-ack |
| [make_true_root_missing_cell_fleet_manifest.py](../scripts/make_true_root_missing_cell_fleet_manifest.py) | 纯元数据生成器与两个实际 job 类型的完整 workflow 模板 |
| [TCF proof](../results/R149-supplement-terminal-missing-cell-fleet-and-complete-source-aggregation.md) | 局部 memo、全域 coverage、上界聚合及范围证明 |
| 本页 | 实际入口、状态和后继办法 |

## 初次终态后的使用

先取得原 run 的最终完整公开 state/prefix/execution。生成器须通过终态与
整个 accepted union 检查；它不能以当前任一中途 checkpoint 预先分配。

```bash
python topics/visible-flex-exact-nearby/scripts/make_true_root_missing_cell_fleet_manifest.py \
  --repo . --maximum-cells 256 --maximum-parallel 6 --write
```

仅 `ready=true` 时，此命令写一个小于 100 KB 的完整输入 DAG manifest 和
`.github/workflows/visible-exact-true-root-missing-cell-fleet-<parent-id>.yml`。
命令返回具体路径、全 SHA、完整 assignment 数和缺格总数。它本身没有
科学调用，也不会推送或启动 workflow；root 统一审查和推送。

实际工作流包含以下两类 job：

1. 每个 runner 单进程负责至多 256 个连续缺失原 cell，默认最多六个 runner。
   每个 cell 内仍全 96 列/所有原活动窗口，`fail-fast=false`。共同父标记和
   各 assignment consumed 标记须先成功推送，方可恢复 native 输入及计算。
2. `needs` 全部分片 jobs、`if: always()` 的终态聚合 job。它从真实 GitHub job
   API 核对全部固定 job 已终态，只读取每个完整 actual/execution。聚合时
   不恢复 trial，不调用任何 cell。全部 7724 cell 已覆盖才形成仍缺的原完整
   negative/positive source 结论；已完成旧目标逐字复制。

每个新结论都由公开 worker 推送成功后给科学 child 私有 ack，随后才计算
下一条。完整原 source 结果采用原自然文件模式和原 validator，仍声明
`true_PDE_columns_or_inverse_proved=false`。新 manifest 身份如实保存，不能
把新聚合结果归入旧 manifest 或旧 run。

## 失败分片后的继续

若任何分片在若干完整 cell 后终止，终态聚合保留其整个已接受前缀。最终
`aggregate/actual-accepted-union.json` 含五组全 96 上界、全部 accepted/remaining
整数区间以及所有分片 actual/execution 的 whole SHA。保存完整部分并集不
等于完成原 source 目标。

等该整个 fleet run 真正 completed 后，以真实路径替换下列占位参数：

```bash
python topics/visible-flex-exact-nearby/scripts/make_true_root_missing_cell_fleet_manifest.py \
  --repo . --maximum-cells 256 --maximum-parallel 6 \
  --carry-manifest topics/visible-flex-exact-nearby/notes/ACTUAL-FLEET-INPUTS.json \
  --carry-directory topics/visible-flex-exact-nearby/notes/true_root_missing_cell_fleet_ci/run-ACTUAL-1/aggregate \
  --write
```

生成器沿完整历史小元数据 DAG 准入该 union，新的 worker 另查前一整个 run
确已 completed。新 assignment 恰好覆盖其严格补集；所有此前已接受 cell
和已完成源目标均不会重算。重复同一 consumed assignment 或换 partition
重领同一父并集都会被拒绝。

## 容量及验证范围

每个 cell runner 的完整私有数组预算为 12 GiB；四个 trial arrays 约 4.55 GB。
它们仅留作业私有空间，不存入仓库、artifact 或 Release。公开预算一次覆盖
所有分片的完整小报告与最终整个 source 结论，仍核完整 topic 200 MB。

设 $N$ 为全部互斥 assignment 数。每个完整科学 actual 小于 65,000 B，保留
全部五组 96 维上界；每个 public execution 小于 20,000 B。非空 accepted
prefix 的 actual 必须含原四 whole-array 恢复回执。空 prefix 允许尚未恢复。
整个 transport state 在作业私有目录完整写入并逐字节读回；公开记录绑定其
长度与 whole SHA，并保留科学文件身份、run/attempt、实际退出、已接受游标、
输入身份以及 README 检查链。容量以 $85000N+390000$ B 加 120,000 B
reserve 核算。390,000 B 中聚合占至多 360,000 B；生成器以全部真实分配、
20 位 run id 长度上界和与 worker 相同的序列化函数核算其余标记至多
30,000 B。并发上限只控制同时运行个数。生成器落盘前核对应真实 run API
已终止，worker 在领格前复核。

原 public transport 的全部 README/pull/rebase/容量检查原样复用；每次 pull
核两 README，长计算至多间隔 1800 秒再次 pull，非快进立即 rebase 再推。

初始验证仅包括全部新源码 AST、原 cell body 提取/编译、原 public prefix
编译、实际活跃父记录的拒绝分配，以及完整源码/链接的静态核对。未加载
NumPy、Flint 或 SciPy，未运行旧/新 cell、旧矩阵、旧范数或聚合数值目标。
本页不能作为完整 residual96 已完成的证明；完成以真实整份 actual/execution
为准。
