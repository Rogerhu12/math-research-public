# 三份已完成角表的无损外层归档及一份真实恢复

这是可逆本地存储维护，不是新的数学结果。经父任务确认没有活读取后，三份完整 `continuous-angular-three-jets.npz` 原文件逐份使用 gzip 外层封装；NPZ 内所有压缩字节及科学数据均保持原样。每份归档都先落盘、fsync、逐字节解压核完整原 SHA/长度，再核原文件完整 SHA，将持久清单写好后才移除原路径。

本次实际归档进程 exit0：原始三份共 160172910 字节，gzip 共 96495304 字节，初次实际释放文件分配块 63668224 字节。源采用 zlib 1.3.2、level6、wbits31、1MiB 源块；完整清单逐项保留原路径、SHA、长度、权限、mtime、归档 SHA 与恢复验证。每次写前保留原 128MiB 磁盘门。

随后父任务要用 λ=.002 原表计算此前未付的同场 .12 cut 活动矩。我已实际恢复该原路径，32968314 字节、SHA `fae2e2143371b8bdca681bb75f06a94f1a425716561c5fac30d3e46dc57a00b8`，完整核同；对应 gzip 保留。两份 λ=.064 原表仍处于归档状态。因此恢复后当前净 payload 分配块节省是 **30699520 字节**，不是初次节省的 63668224 字节。原 archive manifest 保留历史终态，另一个 restoration-observation 记录新的实际状态。

所有 summary、exact-defining-jets、.12 cut 表、F 真 full-H 的 native 输入输出以及活 tail metric 输入均未改。不得将角表原路径不存在误判为原证书输入永久丢失。

恢复入口（只选择确实需要的一个原路径）：

```text
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/lossless_cold_angular_gzip.py restore \
  --manifest /workspace/scratch/7c4e33ee17de/held10-maintenance/cold-prefix-angular-gzip-20261128/manifest.json \
  --original-path <清单中的准确原绝对路径>
```

加 `--verify-only` 可只逐字节解压复核而不写回原路径。三份 gzip 为独立完整归档，不依赖 XOR base。完整科学表和归档只留 scratch；本条入 Git 的仅源码、恢复规则、小标量与 SHA。
