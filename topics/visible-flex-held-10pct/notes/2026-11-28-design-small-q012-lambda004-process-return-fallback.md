# q=.012 / λ=.004 / M24：断线后转录的真实 −9 返回

**可信度：实际工程终态；没有数学失败或 OOM 结论。** 本记录从已经返回的工具结果转录，不是假装恢复原本地 JSON 字节。原 JSON SHA `307d0f084bf2d25d2a69460e93956989745cd8663ec3658310828edd41c82f6f` 的全文现不可读。相邻 fallback JSON 单独绑定已知真实路径、命令、SHA 和缺失字段。

从真全门 q=.012、λ=.002/M24 场续入原 λ=.004。实际 controller 为 `run_design_qr_dispatch_v5.py --controller bootstrap`，原 QRv3 + CSR budget v2 数学子入口保持全部原方程、列和验收门，RHS32。已实际打印的 command-record SHA 为 `b1a2ddbfe8af4183742d5442bc053f87e9b93ecd64e2d9e92f61b01ad5cd2614`。

原 pre-J guard 等 45 秒后才放行，实际 MemAvailable=1945116672 B ≥ 原需求1883198500 B；预算未降低。随后完整 QR factor 1 的第 **6** 次 solve 已返回。数值 child 最终 −9，controller 返回3，session 22231 于 2026-11-28 14:21:24 UTC 真结束；observer 已 join 全部 owned 子树，无残余。尚无 raw return、最终 RMS 或 metric，也没有返回可据以统计的 accepted Newton 步数。

kernel RUSAGE_CHILDREN 真最终峰 **524404 KiB**，CPU user83.555034秒、system1.319382秒。它接近512 MiB，而上一成功同 M24 恢复的峰为518732 KiB；这只是要求以后观察实际进程 cgroup/rlimit 的线索，没有证明一个512 MiB上限或此次OOM。主机 MemAvailable 本身不能证明容器配额。

完整615×73节点、24参数、23scale仍保存在 full-J前的 ordinal1，SHA为 `0fdf914d92a9dc84b45cb8ab3e3f7d92ec66c4b0faa908fbad88b161fc5add37`。没有更后的全节点保存，不能把第6次 solve 或未返回的 chord 步当成已保存场。未作 λ 二分，真 accepted 仍为 λ=.002。

后继 RHS16、完整 accepted-Newton-step 持久化和 actual-limit observer 已作为独立源准备；在环境变为 unavailable 前**从未 spawn**。不会把准备记录当成新算例。新的 b=.5 物理设计另有独立条件预算，也尚未求解；旧 b=.2 的这次工程中断不构成它的数学排除。
