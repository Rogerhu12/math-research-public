# 原顺序 normal 逐片规约对接压缩 tile

另名入口 `scripts/fd2d-gc-compressed-piecewise-normal-reduce.py` 以冻结 `fd2d-gc-piecewise-normal-reduce.py`（SHA `870447554f40d4c4ea0a45fd3d9ad2cd4002c8a27de0cea291e0d16f559237d2`）为模板。原文件和活动第 31 轮未改。

新入口接受原 `fd2d-lossless-local-normal-checkpoint-v1` 或明确的新 `fd2d-compressed-original-local-normal-tile-v1`。外部 tile 路径中的 id 与 capsule 内的原 `directory_name=normal-tile` 分开验证；实际 descriptor、ordinal、plan、mapping、源、typed metadata 和完整覆盖仍沿原检查。各数组仍按原 tile 顺序逐个相加，不改变浮点规约顺序。

唯一存取变化是先取得原 logical manifest，再取得经 gzip/原 SHA 核过的原 NPZ bytes，交相同的 `np.load(BytesIO(...), allow_pickle=False)`。输出仍为原 `fd2d-offline-piecewise-ordered-normal-v1`，仍交原 `fd2d_gc_piecewise_normal_transport.py` 重建真实映射；`actual_reducer_source` 如实记录新入口。已有 input-index 只允许相同 source/request 恢复，不跨源沿用旧索引。

为保持纯离线进程的依赖和内存范围，三个读函数从冻结 compressed helper 精确抽取，只有 `transport.SCHEMA` 换成显式相同字符串常量；源身份校验直接读文件，不 import LocalNormalSystem 或 SciPy。这三个函数的 AST 在该常量归一后与原 helper 相同。实际源码导入、冻结源绑定和 AST 核于 chunk `9bac4c` 真实退出 0；未装配或规约任何完整 normal。

原小合成 capsule 位于 `/tmp`，环境恢复后已不可访问；第 31 轮 raw tiles 也已由其 owner 归档。因此两次试读报告为明确 FileNotFound 的真 1，没有把它们写成压缩分支通过。最终本组只闭源码/公式身份与轻量导入核，首次真实完整压缩 tile 消费属于后续第 32 轮的自然执行。不再为此另跑一份 whole normal。

接口保持原 CLI：`--request`、`--out-prefix`，可选 `--piece`。numeric 侧另名 worker/plan/controller 负责实际生成压缩片和调用本入口，本组不改它们。
