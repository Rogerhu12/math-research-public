# 两个冷 CSC hardlink 的实际逐字节可逆存储关系

2026-11-28，按已授权的单次方案，工具 session `60771` 真实 exit `0`。
独立入口 `scripts/resume_20261128/analytic/reconstruct_cold_m24_csc_archive.py`
只读取完整原 CSR，执行一次 `tocsc(copy=True)`，再用原 SciPy
`save_npz(..., compressed=True)` 编码到 seekable `BytesIO`。
它没有重新计算 J、方程、任何数值解或旧矩阵比较。

生成的完整归档为 `82251436` 字节，SHA256 实际严格等于旧 CSC：
`28abf787e7f94ea3424ee1e0d2a9fc5839589698920c5872d3459674d382fe53`。
全部 ZIP 成员顺序、压缩方式、大小、CRC、时间戳、额外字段、属性以及
归档注释也逐项相同。整个生成过程没有写第二份大归档到磁盘。

原两个冷路径均绑定相同 dev/inode、`nlink=2`，原字节与编码来源在
实际删除前再次核完整 SHA。可逆恢复 manifest 已先 fsync 到盘，随后
才删除这两个我方冷名字：

- `held10-linear-work/actual-m24-check/actual_jacobian.npz`
- `held10-design-work/check-direct-csc-m24-20261128/actual_direct_csc.npz`

实际释放该 inode 的 allocated bytes 为 `82251776`。共享磁盘有并行写入，
故不把前后 `disk_free` 变化当作精确释放量。完整原 CSR
`held10-design-work/check-direct-csr-m24-20261128/actual_direct_csr.npz`
原封保留，操作后完整 SHA 仍为
`1814497d5cb4d5159b3f90eb52be4ff276cf281cb4a05cc29547b2b4a179265c`。

恢复 manifest 为
`/workspace/scratch/7c4e33ee17de/held10-maintenance/cold-m24-csc-lossless-reconstruction-20261128-a/manifest.json`，
SHA256 `a24db070d55d89988960c77ecea5b91a1c2f1da3edd59c4bfd55fc32cad0b51d`。
同名 JSON 记录本次完整小 manifest、版本、编码参数、代码 SHA 和两个原路径。
恢复命令是同一入口的 `restore --manifest <该路径>`；恢复入口必须再次
核代码、Python/NumPy/SciPy/zlib 版本、完整保留 CSR 和重建出的完整 CSC
字节，全部匹配后才写回原路径及 hardlink。

本次已经证明并使用字节重建关系；没有为演示再恢复大文件到盘。
当前 CSR、唯一 raw、完整 native/full-H 输入以及 angular 数据均未删除。
所有科学数组继续只留 scratch；仓库仅保存入口和小恢复记录。
