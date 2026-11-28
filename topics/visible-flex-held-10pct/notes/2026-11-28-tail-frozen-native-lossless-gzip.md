# 已终止旧 E 的完整 native 字节无损归档

旧 E 的实际退出记录已核，当前 F、完整 geometry 与后继 memo 的实际依赖不在这个旧根。原目录 `tail-adaptive-fullheight-20261128-a/attempt-001/native-runs` 中60个不小于256KiB的完整二进制文件已实际逐份 gzip：原字节485,211,696 B，gzip总字节324,179,721 B，实释放已分配空间160,993,280 B。

每份归档先完整解压并核对原长度/SHA，再重读原文件与stat身份，持久写journal后才解除原路径；全部科学字节都保留。源、config、JSON、checkpoint和新F数据均未选择。这是已停止进程证据的可逆存储处理，不是数学重算或验收。

原journal位于 `held10-maintenance/lossless-old-E-native-20261128.json`。普通文件的恢复命令为：

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/archive_frozen_native.py restore \
  --journal /workspace/scratch/7c4e33ee17de/held10-maintenance/lossless-old-E-native-20261128.json \
  0027-state-output.bin
```

**后续29份完整input已另外做XOR无损编码。** 这些条目不能再用原gzip路径恢复，必须使用其独立XOR manifest与恢复入口；原journal保持历史原字节，未伪改成新归档。新旧恢复方法均保原长度与SHA，拒绝覆盖不同的已有文件。恢复时需为所选原文件留真实空间。

Git只保存入口、格式/命令与这条小结果。完整原字节和压缩档均留仓库外，没有上传可再生数组。完整范围与实测数值见相邻JSON。
