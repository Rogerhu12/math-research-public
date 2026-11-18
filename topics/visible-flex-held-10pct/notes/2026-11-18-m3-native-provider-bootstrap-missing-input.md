# λ=.64 native 尾入口：缺失依赖导致 ready 前终止

**状态：工程打包失败；没有执行新的 DN、全尾 flow 或前缀内解。**

本次准备从原 λ=.64 近解失败态 `753aa9ec…` 启动一次完整原 DN，并显式切换到独立 native shooting 算术来源。实际入口为 [solve_bound_native_tail.py](../scripts/resume_m3/solve_bound_native_tail.py)，SHA `e02ea1d52af44b7a9fe1ccf8dd741b7e153b93f030433ca5672ba9bce1d24fb6`；原 checkpoint 的全部状态、边界和参数原样复制为未接受初值，配置仅改 `initialCheckpoint` 与 trace 输出路径。它要求原实际 projection floor `.05`、原 $2\times10^{-9}$ 停止门、完整 Jacobian 和 audit，不安排单独的预先全态计算。

独立 bundle `m3_work/native-literal-source-v1` 在 Node 模块初始化时读取 `notes/closing_tail_dependency_blobs.json`，该资源没有被打包。stderr 明确给出 `ENOENT`，来源为 `closing_tail_sources.mjs` 的第 6 行。Python client 因没有收到 ready 而返回 `Weighted stage-tail initialization failed`。

实际 session **47630**，启动块 `9ecfc3`，终态块 `006d2e`；observer 于 **2026-11-18 05:31:08 UTC** 观察 child=2，历时约 2.00 秒。构造函数尚未返回，没有 worker ready、DN 请求或任何 tail response 文件。原 client 在这一异常路径没有把 worker 对象交还给入口，所以没有取得单独的 worker returncode；不根据 Node stderr 补造该值。此终止不属于原尾数值不收敛，也不说明 native 算术能否使原状态过门。

完整命令、200 个来源的清单引用、未改动候选、manifest `0793f8b6…`、异常 stdout 和真实资源终态见 [紧凑记录](../scripts/resume_m3/trace_path_lam064_native_bootstrap_failure.json)。v1 源和输出保留，补充真实依赖应使用独立后继 bundle/manifest。新的 provider 还会显式增加两项来源标记；后继入口将仅按固定字面值处理这些标记，再继续逐项核原物理参数，不放宽方程或门。

## 第二次启动：manifest 文件齐全，但 CJS 依赖未复制

独立 bundle v2 已加入上述 notes JSON；复制清单仍只覆盖 `.mjs`，没有把 JSON 指向的 `general_root_smooth_tail_cells.cjs` 放入新 source-root。实际 session **88879** 在 **2026-11-18 05:34:18 UTC** 再次于 ready 前终止，启动块 `2f23f3`、终态块 `86b247`、observer/child=2，历时约 2.00 秒。stderr 给出该 `.cjs` 文件的 `ENOENT`，来源为 `closing_tail_sources.mjs` 第 13 行；同样没有 DN 请求、全尾计算或响应文件，worker returncode 仍未取得。

此次求解入口 [solve_bound_native_tail_v2.py](../scripts/resume_m3/solve_bound_native_tail_v2.py) 的 SHA 为 `2629f3d9b25e1342c410156154bc8c0a8ae8d0ba4f26fe6efdc575b8879366f8`。相对首入口，其独立 helper 仅逐值核 `shootingEvaluation` 和 `nativeBatchManifestSHA256` 两个明确的 provider 来源标记，记录其出现/消失，再对所有其余键调用原参数与 I/O 比较；配置不增加新物理选项，原 `.05` 门仍明确锁定。这些检查尚未因为此次缺失依赖而进入 ready 后路径。

第二次输入、来源、异常和真实终态见 [第二次紧凑记录](../scripts/resume_m3/trace_path_lam064_native_bootstrap_failure_v2.json)。后继 v3 包从 dependency manifest 枚举并复制全部九个实际资源，再逐个核新副本的 Git blob 内容。求解源码 `2629f3d9…`、原近解状态和物理配置均保持；前两次只是加载失败，没有为此重复任何已完成的数学求解。
