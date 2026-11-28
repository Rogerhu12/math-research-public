# 同一部分克隆的稀疏索引与已核远端对象缓存迁移

本轮工作盘受共享使用量影响，仅本会话可逆缓存可处理。已保持两库 blob:none 部分克隆及 sparse cone，将真实 index 改为 sparse index：私库从78,177,966降到899字节，公库从12,438,629降到612,176字节（后续新提交会正常增长）。源文件、refs及提交历史不变。

随后只将公共仓库已经发布的远端 promisor pack 缓存复制到可写 `/tmp/held10-public-promisor-cache-20261128-objects`。先核HEAD完全已发布、远端promisor属性、实际可用内存至少缓存体积加3GiB；每一份副本完整SHA256/长度均核同，manifest先落盘，才安装标准Git alternates路径并移除工作盘重复副本。全部loose objects，包括本地尚未发布对象，留在原处。

真实迁移393,711,125数据字节，释放原盘397,721,600 allocated bytes；原盘free由126,005,248到522,944,512字节。全manifest SHA为 `4c8f8713f66f2902badbe37919a024e22ce5d45191cdf61795e975ef53217240`。随后HEAD对象读取和worktree差异检查真实通过，后继公开pull/rebase/push也已实际正常完成。没有删除数学场、源码、证明或其他会话文件；tmpfs缓存实际占用内存，后续求解继续读取真实MemAvailable。

## 缓存消失时的恢复

这是可再获取的远端缓存，不是科研状态备份。若`/tmp`缓存消失，保留原worktree、refs、index与全部loose objects，只删除`objects/info/alternates`中已经不存在的这一个路径；然后用原远端对记录的已发布HEAD及main作`git -c fetch.negotiationAlgorithm=noop fetch --refetch --filter=blob:none origin <记录的HEAD> main`。没有理由reset工作树、改历史或重新求解数学对象。正常缓存仍在时不运行该恢复或重新迁移。

实际manifest、源码SHA及观察到的index大小见[小记录](2026-11-28-git-promisor-cache-and-sparse-index.json)。完整pack清单不入Git。
