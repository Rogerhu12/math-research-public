# 只读空间诊断：同分区 pack 覆盖与 publication 稀疏范围前提

审查者：`/root/tail_theory`，2026-11-09。**只读诊断已完成；未执行任何删除、重打包、sparse-checkout、配置、index 或 refs 修改。** 本报告不授权清理，也不降低发布器的可用空间门槛。原主求解仍由 root 持有。

## 1. 已读方法与边界

先全文读取 `scripts/db6f-audit-git-maintenance17-preflight.py`、`scripts/db6f-audit-git-maintenance18-preflight.py` 及 maintenance18 预检审稿。旧协议要求在原 promisor 分区内保全对象，ordinary 对象不能冒充同分区覆盖；旧 MIDX 没列出一个包，也不等于包含该包的新 MIDX 已证明其 selected owner 为零。

本次另写 `scripts/db6f-tail-readonly-pack-coverage.py`，独立解析 v2 idx 的 fanout、排序 OID、32/64 位偏移、idx SHA1 校验和及包名内的 pack checksum。没有读取 pack 或 loose payload，没有 Git 子进程或网络调用。只读 HEAD/refs 时仅保存身份哈希，不读取认证配置或环境。

初始允许的 workspace 元数据扫描限 `/workspace/scratch/db6f0b0e7462`，跳过所有隐藏目录、隐藏文件和符号链接，不进入 `/home/oai/.cache` 或其他受限目录。root 随后缩窄任务后，不再扫描额外目录；后续字节核验只针对 publication 的本题 tracked notes/repro。

## 2. 当前 pack 不存在足够的大冗余目标

实际运行收据 `2bc3da` 启动、`ca9709` 完成，exit 0。冻结报告：`notes/2026-11-09-db6f-tail-readonly-pack-coverage.json`，SHA-256 `3e4fbf47dcad70ef3bd8a80e9350fe002f013b8bd7bd00379f742c21e353474d`。

共有 36 个 pack，总大小 5,315,821,312 B，已索引不同 OID 为 124,327；promisor/ordinary 集合交集为零。两个大包的结果为：

| 包名前缀 | 大小 B | 同分区独有 OID | 独有条目压缩跨度估计 B |
|---|---:|---:|---:|
| `2bb64ed7669d57870b10e387d4548e2513f95bfd` | 4,061,484,070 | 90,281 | 4,061,483,964 |
| `3eb380dfcaea0a6293aa56f6489c90a1db7a93de` | 1,108,181,319 | 16,850 | 1,108,137,347 |

“压缩跨度”由相邻物理 offset 之差精确计算，最后一项到 pack 尾部 checksum 之前；它衡量当前 stored entry 占用，可能包含 delta 表示，**不是**可重构救援包的大小上界。少量 OID 也可能重构为很大数据，不能以独有数量绕过实际救援及验证。

脚本同时区分“每个单包分别冗余”与“多个包联合删除仍覆盖”。按大小依次尝试移除、每次重新要求同分区剩余联合覆盖的纯集合计算，仅找到五个小包，总大小 **163,827 B**。最终逐分区联合与原联合精确相同。这是索引层候选，不是已付 MIDX owner/实际 payload 的删除证书；它更远不足以回收 500 MB。

因此当前没有可由本预检支持的、达到 500 MB 的真正完整冗余 pack 目标。两个大 canonical 包均不能直接移除。没有执行 rescue、MIDX 重建或 expire。

## 3. Publication 的限定字节和 index 核验

root 确认 `math-publication` 为专用发布 worktree，并把下一方案限定为缩小它的 checkout 范围。另写的 `scripts/db6f-tail-readonly-worktree-duplicates.py` 只处理以下 Git pathspec：

```text
topics/visible-flexible-closed-surface/notes
topics/visible-flexible-closed-surface/repro
```

只读 Git 调用使用 `GIT_OPTIONAL_LOCKS=0`、`GIT_NO_LAZY_FETCH=1`，禁用 fsmonitor 和 untracked-cache，且不读 system/global config。查询配置仅限六个明确非敏感键；不查询 remote、credential 或认证值。对 publication 的 index/HEAD 记录读前读后 stat 和 SHA，比较前后 status/config，并检查全部通过文件在区间末尾仍未变化。

真实执行：`8b63ed` 启动、`5e0be6` 完成，exit 0。报告 `notes/2026-11-09-db6f-tail-readonly-publication-sparse-preflight.json`，SHA-256 `df9aecaa0a19fcb3fdfb61d389d99b75fdaa7254eb26d8039e7d9621ef712abd`。

| 项目 | 结果 |
|---|---:|
| tracked notes/repro 文件 | 2,598 |
| 同路径 SHA256 相同，且两份 raw blob 均匹配 publication index | 2,597 |
| 这批同字节副本逻辑大小 | 703,350,709 B |
| publication 块计占用 | 709,005,312 B |
| 不同于 primary inode、且 publication nlink=1 的块计占用 | 709,005,312 B |
| 与 primary 相同 inode 的逻辑大小 | 0 B |
| dirty / untracked / ignored status 项 | 0 / 0 / 0 |
| 读区间发生变化的已核文件 | 0 |

块计和 inode 结果排除了“只删一个硬链接但仍保留同一 inode”的直接误判；overlay/reflink/分配策略仍可能使实际 df 增量不同，因此没有把 709,005,312 B 当作保证的可回收值。

首次真实调用 `e40fcf` exit 1，发生在枚举 index 元数据阶段：初稿对所有隐藏路径一律拒绝，碰到 tracked 零字节占位文件。该次无报告，尚未进入本程序的逐文件字节比较，没有 Git 写入。修订为只接受精确名称与空 blob OID `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，再核两处 stat=0；零字节路径无需打开内容。其他隐藏路径仍拒绝。之后才执行上述成功核验；没有掩去首次入口拒绝。

## 4. 唯一不同版本的小文档与配置隔离

唯一不同的是 `notes/2026-11-09-db6f-prefix-tail-quadrature-cost.md`：publication 3,867 B，primary 4,454 B。它未被计入同字节副本。

另一次只读检查 `54f3b2` 实际 exit 0：publication 旧文本的 raw Git blob SHA1 精确等于其 index OID `efd69834bc999c988bb427f9fd8b277be4769847`，且当前一个通过校验的 pack idx 包含该 OID。报告 `notes/2026-11-09-db6f-tail-readonly-publication-exception.json`，SHA-256 `c744af3cc8101eed54ff93677d1158cfab728db2a8d6c08be33dbaaea2c8956c`。没有实际解码 pack payload；对象身份和 publication 现存字节已有独立吻合，Git 对象本身未被建议删除。

当前 `extensions.worktreeConfig=true` 已存在；两个 worktree 的 `core.sparseCheckout=true`、`core.sparseCheckoutCone=true`。只查询该安全字段的 origin 确认：

- publication 来自 `.git/worktrees/math-publication/config.worktree`；
- primary 来自 `.git/config.worktree`。

二者目前 sparse pattern 文本相同，SHA-256 为 `518d77a5cad0c177b44d5329b5fd3f27fdf0dafda434e8ed99b3aa6350732a55`，均包含整个本题目录。不能因为字段值相同就说它们共用一个 worktree-local 文件；本次已核路径分别独立。

## 5. Root 可考虑的可逆范围变更及前提

下述仅记录 parent 提议，**本代理没有执行**：

```text
git -C /workspace/scratch/db6f0b0e7462/math-publication sparse-checkout set --cone topics/visible-flexible-closed-surface/scripts topics/visible-flexible-closed-surface/results
```

cone 选取这两个子目录时，应保留根文件及祖先目录的直接文件，包括本题直接的 README/HANDOFF/LOG 等，而不 checkout notes/repro 子树。必须以实际生成的 pattern、status 和文件范围核验为准。该操作修改 publication 的 worktree-local sparse 状态、它自己的 index/checkout；正常情况下不改变对象库、refs 或 primary 工作文件。实际执行者仍应核对 primary 的 sparse 文件/config/refs及全部活跃输入未变，不能把本次只读预检当作事后证明。

额外前提和后续风险：

1. 由 publication 的持有者确认没有正在使用该 worktree 的发布/merge 进程。本报告的 clean status 与稳定读区间不能证明无人持有 open fd，也不能排除未来写者；未扫描进程命令行，避免误读凭据。
2. 不改变 primary 的稀疏范围或现存求解工作状态。原 03 与 matched-cut 等长任务保持在 primary。
3. future publication 将新的 notes/repro 从 primary 明确复制并按原发布协议验证时，目标在 sparse 范围外。不能忽略 `git add` 的 sparse 拒绝；需采用明确支持范围外 staging 的操作或暂时扩回所需路径，并核 staged blob SHA。此处不修改原协议。
4. publication 内脚本若在运行时依赖 notes/repro 输入，缩小 checkout 后可能找不到文件。数学运行继续在 primary；发布验证若需要这些输入，应按具体闭清单恢复必要路径，不将缺失误作不存在。
5. merge/rebase 的 LOG 冲突仍须按原协议手工合并。LOG 属祖先目录的直接文件而应保留，但冲突时 Git 可以临时显现稀疏外文件；处理完应核未合并项、stage 和最终范围，而不是批量丢弃 primary 的研究更新。
6. 稀疏状态可通过扩回整个本题目录恢复，前提是对象仍保全且空间充足。该可逆性不等于可忽视操作中的 dirty/untracked 文件；本次实际状态为零，但执行前仍应保持同一前提。

这些条件支持 parent 评估一个“省去重复 checkout、保留全部 Git 对象与 primary 数据”的方案；不支持删除两个含大量独有对象的 canonical 包，也不支持绕过 1 GB 发布门。
