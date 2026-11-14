# 旧 R225 两端计算的源码身份补记

作者：geometry_design，AI 辅助，2026-11-14。

状态：历史数值运行与复现材料的身份记录，不新增数学结论。

`R225-free-core-BVP.md`、`-summary.json`、`-execution.json` 与 `R225-BVP-extension-profile.json` 保留为先前 M48 失败、原生 M128 部分轨道及远端仿射试验的历史记录。它们不表示当前 `free_core_bvp.py` 就是所有旧试验使用的逐字源码。

- M48 的实际执行源完整留存为 `computations/geometry_20261114_r225_free_core_bvp_m48_historical.py`，SHA256 `32b38b24f81f718e979242edc41fd9756e8001d23d8a5c011aeb3a09abaa978b`，与实际失败输出记录相符。原样压缩输出是 `notes/2026-11-14-geometry-resume-R225-M48-historical-failed-BVP.json.gz`，SHA256 `5eff1886e9bda2f18297dda7a714a20b52964fd3117a9e342eaa5d0417263090`。该输出没有接受的 BVP 解。
- 原生 M128 冷轨道使用的 `geometry_20261114_r225_fixed_profile.py` SHA256 为 `478d0bf603ea05a9f20228ff2fd591e2f767e6ab0686a6129b1114aa831b0c6c`，该源仍原样保留。它只到达 $.9945$，没有到达 $.9955$。
- 旧 summary 的 `current_source_sha256` 以及 execution 中的 `510b5eef5d829eef162099490963994c34eb5ffea12579ec4fa533645164a3bd` 指向当时已经加入内存优化的准备版本。不能用它断言之前被外部 $-9$ 终止的 M128 仿射试验启动时就是该逐字源码。
- 该 M128 资源退出保留了真实日志、194.17 秒/2,603,436 KiB 的回收记录和完整 169 节点未收敛 checkpoint；但启动版本未另存逐字副本或单独启动 hash，之后又在同一路径加入 warm、memory 和 block-CSC 功能。这个源码归档缺口明确保留。当前源码与新短端计划可复算所定义的有限方程，但不能冒充原资源试验的原样二进制重放。
- 四线程 Jacobian 对照记录的执行源 hash 为 `b4eb44af9559dbe5e675ff5410baaec9c9138527ef24e43c484031dfcd65ffcc`；该版本的逐字副本同样没有单独保存。数值对照记录保留了三站完整矩阵逐位一致这一事实，现行相同计算形式可以重新验证。

下一次旧 R225 分支的明确入口是 `2026-11-14-geometry-resume-R225-short-end-actual-actions-plan-r2.json`，其源码与输入身份另列；新的球约束放大核心分支也使用独立源、输入、运行目录与记录。
