# 已授权的旧 M16 验证矩阵缓存释放

2026-11-28，工具 session `93300` 真实 exit `0`。
清理范围只有旧 q=.06、λ=.002/M16 完整矩阵验证的可再生 J 缓存：
`/workspace/scratch/7c4e33ee17de/held10-linear-work/actual-m16-check/actual_jacobian.npz`。
它不是新的 q=.012/R87 输入，也不是当前 M24 响应基所需的 CSR。
协作方已确认没有活进程依赖这份旧 M16 测试矩阵。

原完整归档 SHA 为
`a9d655651b6170f1eb8097fe61606dc7a89b40fd181b042ef8e1af305fad4bef`，
字节数 `37127402`，单独 inode 的 allocated bytes 为 `37130240`。
先实际作一次 gzip level-6、mtime-0 编码体积检查，得到 `36080727` 字节，
仅省 `1046675` 字节，未保存近等长副本。该探测只比较编码体积，
不是一份保存并经过恢复核验的压缩档案。

按本轮明确授权，在删除前已逐项核对并保留：原完整节点输入
`e75f89f7...`、来源 run `2b9e2fe6...`、原构造命令、全部输入和来源文件、
原 `check_block_qr.py`（`3dcac440...`）、原因子代码（`ad93895f...`）、
原 residual 与全部标量结果。manifest 先 fsync，再核原缓存 SHA/inode/nlink，
然后只删除这个冷缓存。未重算旧 J 或任何数学验证；若以后需要该矩阵，
manifest 给出从保留的原完整输入重新生成的命令。

这与此前 CSC 的实际逐字节编码证明不同：本次属于有完整科学状态、
源码、命令和结果哈希的可再生矩阵缓存释放；没有预先声称重新运行一定
生成相同归档字节，后续若重建仍必须实际核 SHA。

manifest 位于
`/workspace/scratch/7c4e33ee17de/held10-maintenance/cold-m16-verification-J-cache-release-20261128-a/manifest.json`，
SHA `cdd3fdf37b2e4606191906d05c74f072d5fb3fe3ac07ac268a33f774ecff0827`。
同名 JSON 保留实际小记录。当前 M24 CSR `1814497d...`、全部 V、
q 列、接受 raw、完整 full-H/native 输入及所有活求解输入均未动。
