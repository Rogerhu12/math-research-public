# 第 36 轮恢复源码、真实中断点与执行顺序

## 状态与身份

这份说明保存于执行环境不可用期间。小文本通过根 README 第 8 条允许的 GitHub 路径保存；没有通过 API 传二进制，没有伪造新的退出码、残差、场或 accepted。

当前最后真正接受的主态仍是：

- `notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz`；
- SHA256 `b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f`；
- 原真实目标范数 `3.3585306931843513`。第 35 轮没有新的接受态。

第 36 轮是明确的新实际场和新有限方程。三个原始 baseline 都真正自然退出 0：中正／晚负范数 `463.81319733444`；中正／晚正 `744.04303764165`；只保中正窗 `18.069248304419975`。它们都是初始场评价，均不是接受步。当前选中最后一支考察实际方向；不能把 18.069 与旧 b075 的 3.358 当作同一实际场或已经改善。

全部已知原 SHA、会话与退出见 [恢复历史清单](2026-11-12-fd2d-signed36-recovery-source-and-history-manifest.json)。原闭组 `57ec62a835b6c31033a35dd8a938b5198e09367d3ce53a72cbd7c499cb56fe43` 有 68 件，失联前尚未发布第 23 批。恢复清单没有声称这些二进制现在已经重建。

## 原盘返回时：直接救首块，不重装

只选中窗的 51 块 normal 计划已经真实完成。控制器 92477 最后工具块 `4ac5c4` 真实退出 1。第一块 `0000-nodes` 的完整原 normal 已装配并由原无损 transport 保存。失败发生在其后的旧 gzip 包装：缩进 JSON manifest 有 1,059,811 字节，超过该包装的 1 MB guard。已观察到相同 JSON 对象的紧凑形式为 302,069 字节。

原始完成块路径：

```text
notes/2026-11-12-fd2d-raw-bump-signed36mid-work/normal-tiles/.0000-nodes.raw-wc5p23sy/normal-tile/manifest.json
```

这个数值结果不应重算。恢复后先核原 36 数学源码、原请求、原 baseline 与该完成块确实存在且原 binding 一致。保留旧退出凭据和 raw 目录。若原数学文件已经回来，不运行下面的新源码重建器来覆盖它们。

在 topic 根目录生成两个另名 compact v2 transport 文件：

```bash
python scripts/fd2d-build-compressed-normal-v2-recovery.py --scripts scripts
```

生成器及 v2 调用器当前都没有成功 Python 执行记录。若目标文件已经存在，应先按其真实来源核字节，不盲目重复生成。原 v1 helper 和 reducer 不改。

原 36 上下文可用时，救首块的实际命令为：

```bash
python scripts/fd2d-gc-signed-stage-normal-rescue.py \
  --request notes/2026-11-12-fd2d-raw-bump-signed36mid-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36mid-rescue-a01 \
  --tile-id 0000-nodes \
  --raw-manifest notes/2026-11-12-fd2d-raw-bump-signed36mid-work/normal-tiles/.0000-nodes.raw-wc5p23sy/normal-tile/manifest.json
```

rescue 只核并重包 JSON 与原 NPZ，不调用 F、J 或 normal 装配；它要求原 binding 完全一致，不放宽或改写旧身份。成功后 v2 controller 只补缺失的 50 块：

```bash
python scripts/fd2d-gc-signed-run-normal-tile-batches-v2.py \
  --request notes/2026-11-12-fd2d-raw-bump-signed36mid-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36mid-controller-v2-a01 \
  --batch-size 4
```

完整归并仍按原顺序逐片相加、核覆盖账本与真实 baseline 的平方范数；不能用一个不完整 normal 产生方向。新 v2 reducer 只更换无损读取形式，不更换数值求和、mapping、列尺度或阻尼。

## 只剩 main 时：明确的新恢复轨迹

失联上下文未保留原 22 件新增源码的全部原字节，不能杜撰原 SHA。为使后续实际计算可继续，`scripts/fd2d-build-signed36-source-recovery.py` 保存了一个确定性的、明确另立身份的恢复实现。它核对每份 main35 模板的 Git blob，做有限、计数固定的替换，再核生成结果的 SHA256。它生成 14 个接线源、一个 fresh signed StageIO、三个新的请求。每份 Python 在真正执行生成器时才做 AST 解析；现在不能把这种未来检查写成已通过。

原四份 root kernel 的源和数学保持不动：

- `fd2d_gc_signed_trace_problem.py`；
- `fd2d_gc_signed_trace_windows.py`；
- `fd2d_gc_signed_trace_cells.py`；
- `fd2d_gc_signed_trace_fine_cells.py`。

完整 coast 消费仍调用冻结 R165 的同点实际场公式；新 signed 支持相交格仍调用 root 的完整 split G8 公式。其余旧 R152/R153/R155 算式和准确 n/m 端点保留。保留 Gauss 行由新实际 `retained_gauss_mask()` 决定；平台真零行不重新补入。曲率、格内 Gauss、所有值与参数链式必须消费同一新实际场。

原 R18202 导出模块和数值包未在 main，metric 另立了明确新 schema 的准确有理 producer/installer。它由已经上库的证明数据生成新的 domain 与 QP 包，不冒旧 02 字节。

从 topic 根目录按下面顺序准备：

```bash
python scripts/fd2d-build-compressed-normal-v2-recovery.py --scripts scripts
python scripts/fd2d_gc_signed_search_domain_recovery.py \
  --out-prefix notes/2026-11-12-fd2d-signed-domain-recovery-01
python scripts/fd2d-build-signed36-source-recovery.py
```

新 Context 对当前实际 profile box 核 `box <= handle.delta_absolute_bounds`，每次实际域判断取原 search-domain 判断与 `handle.verify_delta(actual_delta)['passed']` 的交。QP 用安全浮点行给方向，准确证书由有理检查独立支付。每个 checkpoint 都刷新其真实 tail16 和当前 δ 的准确证书，避免沿用结构 origin 中的旧 certificate。

三个新的 request 只是静态入口：

- `notes/2026-11-12-fd2d-signed36-negative-source-recovery01-request.json`；
- `notes/2026-11-12-fd2d-signed36-positive-source-recovery01-request.json`；
- `notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json`。

当前优先只选中窗，不自动重做已经明确很差的两晚窗支线。新请求仍从已在 main 的原 b075 输入开始；新输出、缓存与 request 身份均另名。它不能认领原 36 数值包或第一块 old-binding normal。

实际新 baseline 与 plan：

```bash
python scripts/fd2d-gc-signed-stage-baseline-checkpointed.py \
  --request notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36-mid-source-recovery01-baseline-a01

python scripts/fd2d-gc-signed-stage-normal-plan.py \
  --request notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36-mid-source-recovery01-plan-a01

python scripts/fd2d-gc-signed-run-normal-tile-batches-v2.py \
  --request notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36-mid-source-recovery01-controller-a01 \
  --batch-size 4

python scripts/fd2d-gc-compressed-piecewise-normal-reduce-v2.py \
  --request notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36-mid-source-recovery01-reduce-a01
```

每个进程应由现有 `fd2d-run-monitored-command-v2.py` 包装并另名保存真实 receipt；上面展示内部 argv，不能把未调用命令写成执行记录。每块原子保存，缺块恢复，不因传输断开猜退出码。

完整 normal 后：

```bash
python scripts/fd2d-gc-signed-stage-schur-selected.py \
  --request notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36-mid-source-recovery01-schur-a01 \
  --factor-id lambda1e5 --damping 1e-5 \
  --field-solver-module fd2d_gc_block_normal_solve

python scripts/fd2d-gc-signed-stage-qp-v2.py \
  --request notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36-mid-source-recovery01-qp-a01 \
  --factor-id lambda1e5 --direction-id original-domain

python scripts/fd2d-gc-signed-stage-trial.py \
  --request notes/2026-11-12-fd2d-signed36-mid-source-recovery01-request.json \
  --out-prefix notes/2026-11-12-fd2d-signed36-mid-source-recovery01-trial-full-a01 \
  --direction-id original-domain --backtracking-index 0
```

若完整实际全步未接受，再使用同一已存方向与 `--backtracking-index 1`，另名真实半步输出。只按完整实际 F 的 Armijo 结果接受。范数下降、有限 success、连续后验与 README 强目标分别报告；这个恢复实现没有改变最终目标。

## 主线数学含义与备用设计

[R184](../results/R184-signed-trace-preimages-and-transition-Codazzi-cost.md) 已严格区分：把一个不满足 Gauss 的旧场移入全 trace 平台，不能通过更大的 raw P1 或角空间保持同一实际场。加宽 transition 能降低给定端值变化的部分导数成本，但会改变实际新场／其投影，不能自动称等值重表达；原 Codazzi 也可能抵消增量。因此 18.069 需要真实方向评估，而不是继续以恒等重采样名义修改窗口。

R186 的备用路径改变最后一个真实 profile 参数，使孤立晚段成为负 K；这不是同 g 加密。根据其自由前六推论，可保留前六个 δ 在原 box 内自由，末 δ 进入准确 binary `[.027,.08]`。当前只选中窗的 K 域不对 δ7 添加晚窗行。可在同一已保存 normal／Schur 上另做端点提案约束 `delta7 >= .027`，让全部 raw 场与其余参数一起调整。这样仍须真实 Armijo；半步若没有进入该区间，就不能说已经消除晚段岛。若正式将它提升为新的实际搜索域，则需明确新域身份，并在每次域检查准确核该 binary 下界。

先完成当前选中窗的首个真实方向与实际全／半步，再根据实测结果选择这条设计自由度；本说明没有生成任何备用 NPZ 或 accepted。
