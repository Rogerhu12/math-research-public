# λ=.64：保留 λ=.32 尾内部的新节点 H 初值失败

**状态：真实原求解失败的数值记录；没有取得本次 H 的接受响应。**

λ=.64 原前缀 inner 已返回成功，完整 raw cubic、全部参数和 DN 锚保存在原目录。其真实节点 H 的原尾求解停在 $3.667517320458417\times10^{-9}$；随后唯一已具名反向局部候选也未改善完整受影响行。本条使用另外一个有明确身份的初值：复制 λ=.32 已真实接受的尾内部、深端及切口动量，仅把 node 0 的八个 Dirichlet 分量按原 JavaScript `H/rCut**4` 公式改为这次 λ=.64 **节点 H**，并把 `cutHeight` 同步为新 H。

入口复用已登记的 [保内部原尾脚本](../scripts/resume_m3/solve_preserved_interior_original_tail.py)，源 SHA `af65f13ceb394589e9578c535ca337ca80b86bcb3bf4291b509af966b785b614`。历史 CLI 参数名 `--seam-failure` 和候选通用说明含有 seam 字样；本次实际输入明确为已返回 raw-inner 的 nodal H，尚未形成后续物理 quintic 接缝请求。它绑定 λ=.32 真接受 `cd1f6d4a…`、λ=.64 原近解失败 `753aa9ec…` 和实际运行计划 `498fcf21…`，不把两个不同 H 混作同 H 缓存。

完整 $1153\times16$ 状态只改变 node 0 的分量 0 至 7。所有内部和深端状态、切口动量逐位保持；`rawStates` 按原 `rawNode` 一致重取。原重加载确认 ratio=1、边界补差为零。初值不是接受响应；配置只改 `initialCheckpoint` 和输出 trace 路径，原方程、步长、分片、尺度、域条件与 $2\times10^{-9}$ 停止门均不改。

唯一原 worker 的初始归一残差为 $8.722347033396337\times10^{-5}$。它在 iteration 6 发生原线搜索失败，完整失败态给出

$$
\mathrm{norm}=8.321001905444967\times10^{-5},\qquad
\min A=0.5218773593450274,\qquad
\min D=0.9991191395649076.
$$

因此，这个保旧内部的初值没有替代原近解状态的价值。本条不继续该远残差状态、不追加比例或坐标扫描。原近解 `753aa9ec…` 和已接受 inner `8cf33fae…` 均保持。原完整最终 Jacobian 与 audit 虽在请求中要求，但失败响应没有返回它们，不能把请求写成通过。

实际 session **63447**，启动块 `47cc95`，终态块 `3586c2`；observer 于 **2026-11-18 05:19:21 UTC** 观察 child=2，历时约 642.77 秒，worker 按协议退出码为 0。worker 的正常关闭不等于数学接受。完整失败文件为 `m3_work/trace-path-lam064-nodal-preserved-v1/seed_tail_0001.json.gz`，SHA-256：

`46a7b4cf5efeac76b6e7b616486b895133656d882fe6099054fee7b9e2d6662c`。

全部实际命令、123 个执行来源的清单引用、两组 H、边界差集、资源终态和 trace 哈希见 [紧凑执行记录](../scripts/resume_m3/trace_path_lam064_nodal_preserved_failure.json)。本条没有重跑前缀 BVP、旧 inner、mean-height 积分、prefix metric 或 seam 审计，也没有给出连续几何或最终持握比例结论。
