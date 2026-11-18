# λ=.04 原内解接受，随后新 H 原尾未过停止门

**分类：启发式／数值证据。** 本条登记 `run_m3_trace_path_continuation.py` 的一次真实终态。固定 $M=8$、$\lambda=.04$、支撑种子 $q=0.05963857477670898$，数值 gauge、尺度和 warp 均仍为原 `.06`。完整来源和必要初值见前一条 `2026-11-18-m3-trace-path-lam004-coupled-entry.md`。

## 原前缀内解已接受

真实 observer 会话 `20514`，启动工具块 `3aa85e`、结束工具块 `56334c`；**2026-11-18 04:01:11 UTC** 观察到子进程退出码 $0$，原 worker 也为 $0$。原主流程正常捕获了后述数学求解失败，因此进程退出 $0$ 不代表整体成功。

原 `solve_bvp` 在 **493 节点、1 次 mesh 迭代**后返回 `success=true` / status $0$，最大原 RMS 为

$$
9.873653007345489\times10^{-7}<10^{-6}.
$$

该次 Newton 有三次接受步，均为全步；域拒绝、merit 拒绝、无步返回均为零。原 normalized $x/y/p$、完整 cubic、RMS、消息与实际 DN 锚已在新 H 请求前保存，毋须重跑此内解。

真实返回态 `inner-00-returned.json.gz` 的 SHA-256：

`7ca5ea61dcabd581bb9541167b2b7c9086d184b5d336465f1e9b3f2479c9fe4e`。

其原 cubic 为 $4\times492\times25$；完整八参数及七个物理控制在紧凑终态记录中。参数 $p_0=-3.596950323757216\times10^{-10}$ 仍仅相对原 `path_base_profile` 改变 $\delta$，不是支撑种子的又一次缩放。

## 新 H 原实际尾失败

从上述真实返回态读出完整八项 $H$ 后，原 worker 真正执行了新请求，要求完整 Jacobian 与审计。两次原 Newton 修正后，第三次停止检查（迭代编号 $2$）为

$$
\|R\|_{\rm original}=3.6678628847049105\times10^{-9},
\qquad \text{原门}=2\times10^{-9}.
$$

原线搜索没有取得严格改善，返回真实失败；没有放宽门。最后检查的 $\min A=0.5218915639820443$、$\min D=0.9991195358652001$。这两个有限域读数不代替残差门。

完整失败记录为运行目录 `seed_tail_0001.json.gz`，SHA-256：

`a94402ea667b60d454ffe364a3e3b65a8f2b3572f6c1b86c01baf478de924510`。

本次共一个原内层调用和一个实际 native 尾请求。失败发生在该已接受内解之后、物理 quintic 导出之前；因此 **本次还没有 λ=.04 的物理 CP、均值高度、完整前缀 metric 或接缝审计**。不能把 $\lambda=.02$ 的完整后处理数值套过来。

## 保存与复现

运行目录为 `m3_work/trace-path-lam004-coupled-v2/`。`launch-command.json` 保留真实 observer 命令；prepared 与 runtime plan 均已在入口记录绑定。原方程、五点有限域检查、merit、节点与停止门和八次 outer 预算未改。

只读收集源 `scripts/resume_m3/collect_trace_path_coupled_terminal.py` 不导入数值模型，不计算新的 flow、Jacobian、RMS、均值或 metric。实际收集 `216b0e` 退出 $0$，核 114 项执行源、8 个完整 raw 快照及其锚、唯一返回内解和唯一失败尾；全快照清单只保存在 scratch，Git 中的 `scripts/resume_m3/trace_path_lam004_coupled_terminal.json` 记录其 SHA 与必要参数。

这一失败仍允许从真实已接受内解接续原 post-tail 流程。下一条针对这个具体新尾状态定位残差并决定初值；它与本条原失败分开登记，不重做已接受内解，也不把后续修正倒写成此次成功。
