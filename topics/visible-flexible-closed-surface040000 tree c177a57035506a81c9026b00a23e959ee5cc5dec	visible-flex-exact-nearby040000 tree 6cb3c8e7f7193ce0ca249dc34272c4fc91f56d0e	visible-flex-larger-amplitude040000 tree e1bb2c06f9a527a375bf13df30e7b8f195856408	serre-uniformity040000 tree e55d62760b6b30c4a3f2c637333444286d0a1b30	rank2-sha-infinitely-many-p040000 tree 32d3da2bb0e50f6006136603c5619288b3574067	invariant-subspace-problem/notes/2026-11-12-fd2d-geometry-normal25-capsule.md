# staged25 唯一完整 normal 的可恢复压缩包

2026-11-12。该包只持久化已完成装配的字节，不计算 F/J、不求解线性系统、不读取数组语义，也不改变原 normal、48 个 tile 或原 loader。

原文件为 `2026-11-12-fd2d-raw-bump-staged25-work/normal-partitioned/manifest.json`，435510 字节，SHA256：

`e022f588dd0731aca74896ea8ef7fcbf649bd89c4a8d336e50b57a55c730a732`。

胶囊目录为 [normal25-capsule-01](2026-11-12-fd2d-normal25-capsule-01/index.json)，完整 index SHA256：

`6c0135760056dcc714e048b42ea748b4901548cf5ce468df258b62465c6e697b`。

## 精确保存范围

35 个原 NPZ 逐件使用固定 `mtime=0`、空 gzip 文件名压缩。创建过程中既核原文件的完整 SHA/字节数，又完整流式解压核回原 SHA；不是只核 gzip 头或 CRC。原 manifest 以 `original-manifest.json` 原字节保存，没有重新序列化。最后才写完整 `index.json` 并原子重命名整个新目录。

| 量 | 实际字节数 |
| --- | ---: |
| 原 NPZ 数值数据 | 21436600 |
| 压缩后的 35 个数值片 | 13617435 |
| 原 manifest | 435510 |
| capsule index | 16703 |
| 完整 capsule 目录合计 | 14069648 |
| 最大压缩片 | 554372 |

目录内每一件均小于 1000000 字节。只需发布这一个最新完整 normal 的 capsule；48 个约 1 GB 的可再生 tile 不在包内。

## 恢复

源为 [fd2d_gc_normal_capsule.py](../scripts/fd2d_gc_normal_capsule.py)，只使用 Python 标准库。可调用：

```python
create_normal_capsule(normal_manifest, destination,
    expected_manifest_sha256=...)
restore_normal_capsule(index_path, destination,
    expected_manifest_sha256=...)
```

恢复目标必须是一个尚不存在、basename 为原 `normal-partitioned` 的目录。例如从课题目录执行：

```bash
python scripts/fd2d_gc_normal_capsule.py restore \
  --index notes/2026-11-12-fd2d-normal25-capsule-01/index.json \
  --destination /tmp/normal25-recovery/normal-partitioned \
  --expected-manifest-sha256 e022f588dd0731aca74896ea8ef7fcbf649bd89c4a8d336e50b57a55c730a732
```

restore 核完整压缩片 SHA、原 manifest 的逐片身份、完整覆盖及解压后 SHA/字节数；有界流式解压，未全部成功不会产生可用的最终目录。它在临时目录中最后写原字节 `manifest.json`，再原子重命名为指定目标。不使用 pickle，不重建 NPZ，不改变任何浮点值。

恢复后仍用原 `fd2d_gc_normal_checkpoint.py::load_normal_checkpoint(problem, manifest, expected_binding=...)`。原 loader 继续核真实 state/source/objective binding、原 LocalNormalSystem 映射及全部数组身份。capsule 不能替代或绕过这一数学输入核对；例如把同一矩阵用于另一个接受态，仍应由原 loader 拒绝。

## 真实运行

pack：session `55273`，初块 `76e3f7`，结束块 `d684a2`，自然退出 `0`；内部耗时 `13.169704429998092` 秒。

独立 restore：session `41805`，初块 `e9653e`，结束块 `a2e4d1`，自然退出 `0`。真实恢复目录为 `/tmp/fd2d-normal25-capsule-restore-01/normal-partitioned`。全部 35 片流式身份通过，恢复的 manifest 字节数和 SHA 与上列原文件完全相同。

这是传输与持久化结果，不是新 normal 装配、QP/Schur 求解或几何验收。原 normal 及 tile 均保持不动。
