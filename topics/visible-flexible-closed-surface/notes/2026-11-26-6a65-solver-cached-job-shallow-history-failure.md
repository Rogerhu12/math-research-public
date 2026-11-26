# Cached Cartesian job：浅历史首次发布失败与最小修正

日期：2026-11-26；会话：Astra-visible-flex-6a65。此条是实际基础设施失败及其局部修复验证，没有数学新接受或目标完成声明。

## 实际失败

[run 45823011528](https://github.com/Rogerhu12/math-research-public/actions/runs/45823011528) 的 job 139919847958（actual-fixed-g-continuation）由 Actions API 返回 completed/failure。实际日志显示 Node 与 Python 依赖安装成功，运行的是公开 trigger commit `c0661016195ec9864a1ed27aee1760e0b6c2c354` 的 batch bootstrap。

12:48:09 UTC，它先在 detached HEAD 写出一个本地 pre-process scalar commit（日志短 SHA `0ec293d`，没有成功推送）；12:48:11 的第一次 `git pull --rebase origin main` 随后错误地把已公开 trigger commit `c066101` 本身作为待重放提交。冲突涉及 invariant-subspace-problem 的 H/log/open/results，以及本课题 H 和原 long-run 报告，均是整树 add/add 症状。controller 如实拒绝越过自身 H 标记去解决这些冲突；失败回执的再次提交也因现存 unmerged entries 失败。进程实际 exit 1。

在此之前没有 `new-batch-source-stage-start`，因此本 job 没有执行新 Cauchy value、原 observer、Cartesian baseline/LM 或缓存生成。未推送的 scalar 文件没有可核公开字节 SHA；不能补造。不要通过取一侧覆盖跨课题冲突来恢复这次发布。

## 原因与修正

workflow 先以 depth 1 克隆当时较新的 main，再以 depth 1 fetch 较旧的精确 trigger commit 并 detached checkout。两处浅边界使本地缺少连接这两个提交的祖先图。后续 remote main 前进时，rebase 将 trigger 误识为待重放根提交，而不是它已在远端历史中的祖先。

在精确 checkout 之后、任何本地 commit/pull 之前，补齐提交图即可。仍保留 blob 部分克隆：

```sh
if [ "$(git rev-parse --is-shallow-repository)" = true ]; then
  git fetch --filter=blob:none --unshallow origin main
fi
git merge-base --is-ancestor "$GITHUB_SHA" origin/main
test "$(git rev-parse HEAD)" = "$GITHUB_SHA"
```

这不改变 frozen trigger、数值源码、目标、缓存数据或任何数学结果；新 job 必须重新实际生成自己的源输入。原 long run/source003 的已加载程序和 frozen 数值 epoch 不因此改变。本条不声称修正后公有 job 已完成；其新实际回执须另记。

## 与真实失败对应的本地 Git 回放

可执行文件为 `scripts/6a65-shallow-trigger-rebase-fixture.py`，全部操作只触及 disposable local bare/working repositories，无网络、凭据或公有 main 变化。

该源码 SHA-256 为 `bbb26b29321e8434d88acd6ad10d064b27b1a866a62d1345dbb5efe291b34ce2`。

```sh
python /tmp/visible-flex-6a65e705/solver-work/recovered-sources/6a65-shallow-trigger-rebase-fixture.py \
  --directory /tmp/visible-flex-6a65e705/solver-work/shallow-trigger-rebase-fixture01
```

实际外部 OS exit 0；fixture 内部用时 0.37808295599825215 秒。它先真实复现 depth-one 最新 main + depth-one 旧 trigger + 后续 remote advance 的 rebase 失败（exit 1，trigger 整树冲突），再用 fresh clone 执行 unshallow，验证 exact trigger HEAD 不变、共同祖先存在。修正分支的真实 rebase exit 0，只重放一条自己的 scalar commit，保留远端文本，随后普通 push 真正成功。

报告 `shallow-trigger-rebase-fixture01/report.json` SHA-256：
`4fba72e459f6f0baae47f3b83366e71f8ca45d416d110ed051f0f7cb7dc02ff1`。
本地 synthetic commit hashes、失败/成功日志 SHA 均在该小报告中，不能冒作公有提交。没有重复任何数学 fixture、完整 value、normal 或试步。

