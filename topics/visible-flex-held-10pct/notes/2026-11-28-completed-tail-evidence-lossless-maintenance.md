# 已完成尾部证据的无损存储与准确恢复

本轮只处理已经终止、当前无 reader 的冷文件，并保留完整原科学字节。所有新 gzip 都在 unlink 原副本之前，从实际磁盘文件流式解压/恢复、逐字节比对原件并核全部长度及 SHA256；原数学源、数值结论和 native 运算均未重算。

## 实际释放

| 操作 | 真实数据 block 净减少（bytes） | 清单 / journal SHA256 |
|---|---:|---|
| 3 份冷 E 完整 J output 的永久 output-base XOR+gzip | 7,016,448 | `7cb34e18d7c54efd47acab5e9a12caaad777b1f8e651ec4b3942b9740616e9a4` |
| 5 份准确相同的完整 node-index 原位硬链接 | 6,062,080 | `cf62ba1fc713812b8465d8ba5e2c8d6620855b7c0d9617bb3c47f832c91146d2` |
| R83 已完成后，将临时恢复的 λ.002 angular 表返回原永久 gzip 存储状态 | 32,968,704 | `ef313b761ae77ae1a3d8773d0eed8a824dcb595a8184899d876d721935c71ca5` |
| 1151 份已完成原逐 stage metric 证书 JSON | 52,690,944 | `54d5d879844356ede8638c6f2596be6b456c29020a7c3c48856b0111bdd3b42d` |
| 1465 份已完成 v4 receipt / Taylor / progress JSON | 16,560,128 | `747b1b0f35bb001393074b6ac96cc498128582b3604d8ac56a91f4685f701e54` |
| **数据 block 合计** | **115,298,304** | |

上述按实际原件与新压缩文件的 `st_blocks*512` 计算；五份新 manifest/journal 另占 **2,420,736 bytes**，未计入数据节省。共享磁盘上的其他用户/进程变化不能算成这里的释放量。root 的 Git promisor cache 迁移、稀疏 index 清理，以及 analytic 自己记录的可再生旧 J 缓存删除也不计入本表。

output XOR 的真实节省不是每份一律 3.7 MB：三份分别为 1,622,016、1,716,224、3,678,208 bytes。独立完整 `0024-jac-output.bin.lossless.gz` 是永久 base，**保留原位，不是另一个 delta**。输入模板的既有 base 与其他旧 input-XOR 清单均未改变。output 协议保全原 native state/J 的头、全部状态、矩阵和诊断，不冒称为 input 格式。

完整 summary、contract、map 的 `.gz` 数据、全部 mean、fullbundle 内的原 node index、当前 F 和 memo 输入保持原位。五份硬链接处理的是其他已经冻结、完整 SHA 同为 `e9cb47ae…` 的 node-index 副本；它们所有原路径和全部字节仍然存在。冻结硬链接文件不得原地重写；后续重新生成请使用新的 node-check 路径。

## 准确恢复命令

下面都是纯字节恢复，不进行 BVP、native 或证明重算。清单记录完整原路径、字节数、SHA、mode 和 mtime；已存在但字节不同的目标会被拒绝，不能覆写它。

~~~bash
held_repo=/workspace/scratch/7c4e33ee17de/math-research-public
held_maintenance=/workspace/scratch/7c4e33ee17de/held10-maintenance
held_tail="$held_repo/topics/visible-flex-held-10pct/scripts/resume_20261128/tail"

# 恢复一份冷 E 的完整原 wire output；另外两份为 0014 / 0020。
python "$held_tail/lossless_native_output_xor_archive.py" restore \
  --manifest "$held_maintenance/old-E-complete-output-xor-20261128-a/manifest.json" \
  --relative-path 0001-jac-output.bin

# 重新执行 R90 全 collector 前，先恢复下面两份清单中的全部原 proof JSON。
python "$held_tail/lossless_completed_metric_proofs.py" restore \
  --manifest "$held_maintenance/completed-original-metric-proofs-gzip-20261128-a/manifest.json" \
  --all
python "$held_tail/lossless_completed_metric_proofs.py" restore \
  --manifest "$held_maintenance/completed-v4-metric-proofs-gzip-20261128-a/manifest.json" \
  --all

# 如以后确实需要重读完整 angular 表，再恢复此前已完成的原字节。
python "$held_tail/lossless_cold_angular_gzip.py" restore \
  --manifest "$held_maintenance/cold-prefix-angular-gzip-20261128/manifest.json" \
  --original-path /workspace/scratch/7c4e33ee17de/held10-geometry-work/new-prefix-metric-tables-20261128-v1/continuous-angular-three-jets.npz
~~~

三个 restore 入口均支持 `--verify-only`，只解码核全 SHA、不写原件。proof 恢复也可用 `--relative-path` 单独恢复一份原 JSON。运行完整 collector 时，两组 proof 清单必须先完整恢复；直接读取现有 R90 最终标量报告不需要恢复它们。既有 A/B 已付的其他证据仍在原位，完整索引硬链接无需恢复。

归档实际 session 53960、64592、27400 均已返回 exit 0；每份独立 gzip 都已在归档时完成真正流式原字节核验。原 `.json` 路径目前可能为空缺是明确的存储状态，不能把它说成数据仍以未压缩形式存在，也不能把缺文件当数学失败。

额外真实执行了 output `restore --verify-only` 和单份原 stage 94 证书的写回恢复，两条 CLI 均 exit 0。该原路径的全部字节和 SHA 与归档一致；在第二次核 permanent gzip 后，再移除这份自检临时恢复副本，未增加长期占盘。其他原文件没有重算。

所有清单、恢复源和实际执行状态的完整引用见同名小 JSON。大型数据、delta 和完整证明叶均未入 Git。
