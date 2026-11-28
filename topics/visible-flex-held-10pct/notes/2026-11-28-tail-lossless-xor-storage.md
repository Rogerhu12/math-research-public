# 冷存旧 E 输入的无损 XOR 归档已实际完成

## 实际空间结果

旧 E 已终止，当前 full-H、全谱 geometry 和后继 outer 只读取新 F 的 native 输入/输出；旧 E 的 source、manifest、config、JSON 和 checkpoint 仍原位。对已经完成原始 gzip 归档的 29 个完整顶层 `input.bin`，本次进一步使用同一真实 static-template 字节作 XOR 字典。

- 原科学输入总字节：356,709,164 B。
- 先前 29 个 gzip 总量：210,929,851 B。
- 29 个新 XOR gzip 总量：13,681,701 B。
- 实际释放的已分配空间：**197,226,496 B**。

每份新档都已经从落盘后的 delta 独立解压、与完整 template 逐字节 XOR 恢复，并与该份原始完整输入逐位比较、核对原 SHA-256。新恢复程序和该行 ready manifest 先持久化，随后再次核旧 gzip/base 哈希，才移除那份冗余旧 gzip。原历史 journal 没有改写；所有旧 output.bin 和不符合相同长度的子输入仍走原 journal 的 gzip。新 F 的 native 文件完全未归档。

## 格式与恢复

新 manifest 是 `held10-maintenance/lossless-old-E-native-xor-20261128/manifest.json`，schema 为 `held10-lossless-native-input-xor-v1`。base 仍是原 `static-template.bin.lossless.gz`，它保存完整独立 raw template，**不依赖任何 delta，必须长期保留**。

恢复规则只有字节操作：`original = gunzip(delta) XOR gunzip(base)`，然后核原完整长度与 SHA-256。它没有浮点近似、重算方程、改原字段或删未知量。恢复 CLI 对已存在且不同的文件拒绝覆盖；实际恢复会保留原 mode 和 mtime。

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/lossless_native_xor_archive.py restore \
  --manifest /workspace/scratch/7c4e33ee17de/held10-maintenance/lossless-old-E-native-xor-20261128/manifest.json \
  --relative-path 0027-state-input.bin
```

加 `--verify-only` 只解码并核原字节、不创建完整文件；该独立 CLI 已对 `0027-state-input.bin` 实际运行成功。移除 `--verify-only` 时恢复到原 native-runs 路径，恢复一个输入约需 12.3 MB 空间。

所有原字节、gzip 与 delta 均只保存在仓库外的 scratch；Git 中只有源程序、格式说明和小哈希记录。这是保留科学证据的本地无损存储处理，不是新的数学接受或课题完成。
