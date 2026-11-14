# 第 28 轮完整 normal 的无损恢复包

原始对象是 `2026-11-12-fd2d-raw-bump-grouped28-work/normal-partitioned/manifest.json`，准确 SHA-256 为 `bb50e4ccc1ba7f98f36303631592738815249785ecc9f45a202d465199be4c31`。它声明 `fd2d-offline-piecewise-ordered-normal-v1`，含 35 个有限 NPZ 片。本文只保存这一份完整且昂贵的中间态，不复制装配所用的约 1 GB tiles。

旧 `fd2d_gc_normal_capsule.py` 有旧 schema 的明确 guard，所以没有将新 manifest 塞入旧入口。另名 `fd2d_gc_piecewise_normal_capsule.py` 保留相同的流式 gzip、逐片压缩/解压 SHA 核对和原子目录发布逻辑，显式接受新 schema，并将数学恢复入口绑定为 `fd2d_gc_piecewise_normal_transport.load_piecewise_normal`。没有修改原 normal loader、原矩阵片、tiles 或主求解源。

## 已实际完成

- `pack` 自然退出 0：session `61823`，初始 chunk `5a14e3`，终结 chunk `07d829`。35 片原始数值文件共 21,624,724 字节；gzip 共 13,692,750 字节；最大单片 554,615 字节。
- 所有压缩片在打包时都流式解压核回原始字节 SHA；原 manifest 的 453,850 个字节逐字节保留。
- 新 `restore` 在独立 `/tmp/fd2d-normal28-capsule-restore-01/normal-partitioned` 实际退出 0，chunk `17d454`，再次核全部片和原 manifest。恢复后的 manifest SHA 与上述原值相同。
- capsule 的 `index.json` SHA 为 `39424afa83fc2082a09fba725e399047a282127077e451809b798a6252458fb7`。每个发布文件小于 1 MB。

两条执行均不载入数值矩阵进行运算，不计算 F/J、QP 或 BVP，也不将压缩/恢复核对冒作数学 binding 核。恢复目录的 basename 必须是 `normal-partitioned`，manifest 最后写入；随后仍由原 `load_piecewise_normal(problem, manifest, expected_binding=...)` 重建和核对映射/有限目标身份。

## 恢复命令

从课题目录执行：

```bash
python scripts/fd2d_gc_piecewise_normal_capsule.py restore \
  --index notes/2026-11-12-fd2d-normal28-capsule-01/index.json \
  --destination /your/recovery/directory/normal-partitioned \
  --expected-manifest-sha256 bb50e4ccc1ba7f98f36303631592738815249785ecc9f45a202d465199be4c31
```

目标必须尚不存在；失败的临时目录不会被发布成完整对象。原第 25 轮已发布 capsule 保留，此次不修改它。
