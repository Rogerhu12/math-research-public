# 原 LocalNormalSystem 的压缩 tile 存取

本组只改变中间态的磁盘存储，不重新计算任何 F/J、normal、QP、body 或 BVP。它不修改原数学、映射、数值顺序、binding，也不把 gzip 文件伪装成旧 NPZ 传给原 reader。

## 明确的新格式与接口

`scripts/fd2d_gc_compressed_normal_tile.py` 的新 schema 是 `fd2d-compressed-original-local-normal-tile-v1`，强绑定原 `fd2d_gc_normal_checkpoint.py` SHA `330fad074fcfc021279802c9b8f11e0f0f84dc6acb96e48d165360eb82dec66d` 与既有流式 capsule 源 SHA `da1f00e2936472b0a7824ebd6ea4f460eb1f5086a810e8b4c4128c9c14e73d34`。

- `save_compressed_normal_tile(normal, prefix, *, binding)` 返回新的 `prefix/manifest.json`。它先在自身唯一临时目录用原 save 生成一份原 normal，再逐个小于 1 MB 的片流式 gzip、反向解压并核原 SHA。所有片通过后，原 manifest 字节保存在 capsule，外层新 manifest 最后写入，整个目录原子 rename；随后只删除本 helper 自己生成的 raw 临时目录。已有 normal/tile/源目录不删。若打包失败，保留本次私有 raw 目录并在异常中给路径，以免丢掉昂贵进度。
- `load_compressed_normal_tile(problem, capsule, *, expected_binding)` 在一个私有临时目录还原这一份原 normal，调用原 loader 重建并逐字节核映射、源、有限目标 binding、数组 shape/dtype/SHA 和 typed metadata；返回原 `LocalNormalSystem`。读完后清理这份私有恢复目录。
- `read_logical_manifest(capsule)` 返回 capsule 中原 manifest 的完整 JSON 对象，保留它真正的旧 schema。
- `read_logical_piece(capsule, row)` 要求 row 与原 manifest 中某行完全相同，流式核压缩文件和解压字节，返回原 NPZ 的 bytes，严格小于 1 MB。离线逐片 reducer 可用 `np.load(io.BytesIO(data), allow_pickle=False)`；每次只持有一片数据。

外层格式保留原 binding/mapping/metadata 身份；它的 `payload/index.json` 是已有流式 capsule 的原格式。新 schema 的入口是明确的，原 loader 只见到正常还原的原 manifest/NPZ。

## 唯一小型核对

`fd2d-compressed-normal-tile-check.py` 用原 K31/tail16/profile7 列宽、九个抽象节点，人工填少量数值和 signed zero。没有装配物理 normal。真实退出 0：chunk `cb0a2e`，内部约 0.0653 s。

所有 normal 数组、metadata 和重新构造的全部 mapping 均 bitwise 相同；错误 binding、改动的逻辑片 row、一个字节的 gzip 损坏均被拒绝。保存成功后只有 helper 自己的 raw 临时目录被移除。此合成 payload 从 888,972 字节压到 203,674 字节，最大压缩片 176,825 字节。这个压缩比只属于该合成数据；未声称每个真实 tile 的具体压缩比。

## 环境中断后的身份

中断前的源、check、report 已成功落盘。执行器恢复后真实核到 helper SHA `0a893bc33f50c13a4899ec4cff18a3c93b3c5035b2f291400a0b777c1fbdb105`，report SHA `da8736151c156ab3883c2789e948d9bd192eea88f99316f604c6f19e27745f91`。本闭组使用这份原始已实际通过的源码。

仅 GitHub API 可用时另建过 `fd2d-geometry-recovery-20261113` 文本分支；其中 helper 的恢复字节不同，并增加过离线 metadata 检查，未在当时执行。本闭组不使用那份支线文件，不把本报告的真 0 借给它，也不删除该恢复历史。当前主线按实际完整保存边界选择接入；本 helper 不是额外数学门。
