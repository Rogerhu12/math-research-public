# λ=.32 完整有限态到 λ=.64 的唯一真实联立入口

**状态：真实启动与有限初始表示身份；终态另记。**

从完整 λ=.32 物理 checkpoint `4794434a…` 向 λ=.64 作一次显式续接。原完整前缀 metric 为 $5.30874420344815\times10^{-4}$，高于最终 $10^{-6}$ 标准；该短缺如实保留，不把中间状态称最终解。原内解、实际 BC、节点真尾和物理接缝真尾均已完成。

本次继续原 [通用入口](../scripts/resume_m3/run_m3_trace_path_continuation.py)，SHA `4e8e4548536a0f0091910180247c1240ab49d045acbdf08a892f2809993eac57`。没有修改已运行源码、Newton/BC/残差门、八次 outer 总预算、五点域检查、全部原 raw 保存或真实 DN/Jac/audit。后续 metric 观察模块尚未用于本次冻结运行。

定义支撑幅值为 $q_{.64}=0.054696409291371345$，由相同精确二进 $Q_*=\operatorname{binary64}(0.06)$ 与已登记 $P_\lambda$ 确定。数值 gauge、warp reference 和原 parameter scales 仍为既有 `.06` 表示；保持原 base profile 与全部 8 个参数，`p0` 仅对原 base δ 作用一次，全部 7 个真实控制继承。没有按幅值幂放大控制，也没有使用旧失败 λ1 控制。

状态采用上一个物理 quintic 在原 chart(raw.x,p0) 处的全部 25 分量，加入同基上的 reference 差投影，再作原共享 C² 入口修补；不将 raw.y 与 quintic 端点读数混为逐位相同。实际新全 8H 与旧物理 H 逐位相同，精确匹配真接缝响应 `cd1f6d4a…`。该真完整响应仅用于相同 H；任何改变 H 仍提交原实际 worker。新图的 mean-height 留给本次原实际积分，未复制旧值。

metadata 准备 `fe329c`/exit 0 只核 123 个来源并生成计划；实际 observer session **98842**、启动块 `783db1`。完整必要初猜数组已一次形成并保存，未为入口重新运行 RMS 诊断或旧内解。源、输入、完整参数/控制/全 H、有限 guard、初猜 hash、唯一命令与真实启动身份见 [紧凑入口记录](../scripts/resume_m3/trace_path_lam064_coupled_entry.json)。它不预认当前新内解、真实尾或最终 metric 通过；这些依实际终态单独记录。
