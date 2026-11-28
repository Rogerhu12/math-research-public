# 五个已终止 mild-tail 冷输入根的无损本地归档

## 实际终态

独立维护器 TTY 89041 已实际 exit 0：33 份完整 native input 与 5 份 static template，共 310392616 字节，改存为 32192490 字节的独立 gzip base 与逐完整字节 XOR+gzip。按原、归档各自实际 `st_blocks`，净释放 **278179840 字节**；结束时共享盘实际可用 529186816 字节。共享卷还有其他写入，故最后可用量不被当成净释放量。

所有原数据均在每份归档落盘后，经独立恢复函数恢复完整字节、逐字节比对并复核完整 SHA256；持久 manifest 已先写出，随后才删除可精确恢复的原副本。所有原 output、JSON、packet 及活 full-H F/geometry 源和数据均未修改。D 的 `0004-jac-input.bin` 实际是目录屏障，明确排除，并非一个被悄悄丢掉的半成品数据文件。

## 明确的原根与恢复清单

| 归档子目录 | 原冷根 | 完整 inputs | 含 base 原字节 | 归档字节 | 实际释放字节 |
|---|---|---:|---:|---:|---:|
| root-00 | `tail-mild-modes-20261128-a/m08/native-runs` | 18 | 132028948 | 6688194 | 125308928 |
| root-01 | `tail-mild-modes-20261128-a/m12/native-runs` | 4 | 41181580 | 5425401 | 35753984 |
| root-02 | `tail-mild-modes-20261128-b/m12/native-runs` | 5 | 49648296 | 5678680 | 43982848 |
| root-03 | `tail-mild-modes-20261128-c/m16/native-runs` | 3 | 38332528 | 6180185 | 32149504 |
| root-04 | `tail-mild-modes-20261128-d/m24/native-runs` | 3 | 49201264 | 8220030 | 40984576 |

每个 manifest 绑定对应原控制器真实终态 SHA、完整原文件路径/长度/SHA/权限/mtime、永久独立 base 与每份 delta 的完整 SHA，以及逐份恢复检查。5 个 base 全是完整原 template 的 gzip，不依赖其他 delta，必须长期保留；没有循环恢复依赖。总汇总位于：

`/workspace/scratch/7c4e33ee17de/held10-maintenance/five-cold-native-inputs-xor64-20261128/summary.json`

SHA256：`fe3f00eb72833a545d689a5cfc3c409d5a10fb939b87e5fb101db34af18950a4`。完整来源、小标量和各 manifest SHA 见同名 JSON。

## 维护预留变更及实际等待

第一版维护器使用 128 MiB 预留，实际只等待、未写任何科学归档；在共享盘跌至该门以下后，按 root 明确授权终止等待器（TTY 32555，真实 exit 130）。终止后再次实核全部 38 个原文件仍与清单 SHA 一致，归档科学文件数为零。旧源码、旧计划与独立停止记录保留不改。

新的独立 v2 只把主动腾盘维护预留改为 64 MiB。每次写前仍要求实际 free 足够：`libz.compressBound(完整原文件长度) + 32 字节封装余量 + 64 MiB + 2 MiB 元数据余量`，而且实际 gzip 长度不得超过所预算的上界；即使 XOR 后极易压缩，也按完整原长预算。**活 geometry 的 128 MiB 逐写门未改变；全部数值与数学验收门未改变。** 对其他进程在检查后同时占盘的竞争不宣称已消除。

## 完整字节恢复命令

从仓库根运行；省略 `--verify-only` 会在原路径恢复完整 `.bin`，保原权限和 mtime。若原路径已有不同内容则拒绝覆盖。实际已在原文件删除后，分别用这个独立 CLI 复核 D 的完整 base 与最终 `0003-jac-input.bin`，两次均 exit 0、SHA 全同。

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/lossless_frozen_raw_inputs_v2.py restore \
  --manifest /workspace/scratch/7c4e33ee17de/held10-maintenance/five-cold-native-inputs-xor64-20261128/root-04/manifest.json \
  --relative-path 0003-jac-input.bin --verify-only

python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/lossless_frozen_raw_inputs_v2.py restore \
  --manifest /workspace/scratch/7c4e33ee17de/held10-maintenance/five-cold-native-inputs-xor64-20261128/root-04/manifest.json \
  --relative-path static-template.bin --verify-only
```

其他根按上表替换 `root-04`；原文件名以该 manifest 的完整清单为准。这是可逆本地字节存储结论，不是新的 PDE、连续几何或 README 完成结论；科学数组、gzip 与 delta 均未进入 Git。
