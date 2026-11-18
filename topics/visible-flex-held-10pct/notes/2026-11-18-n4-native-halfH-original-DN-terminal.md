# n4 同一半幅目标的原 DN：真实线搜索失败终态

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 实际结果

原 DN 会话 `35038` 已在 2026-11-18 04:26:11 UTC 真实结束。最后完整残差为

$$
2.0636915055985155\times10^{-9}>2\times10^{-9},
$$

Newton 迭代编号 4 的十档线搜索均未被接受，程序返回 `multiple-shooting line search failed`。这不是一个被接受的实际尾；所请求的完整 cut、height-jet Jacobian 和审计响应未返回。

这次真正运行包括 5 次全 Jacobian 批求值和 19 次标量候选批求值，合计 24 个完整批次。全部原生进程均以 0 正常退出，没有工程失败。Node worker 在关闭时正常退出 0，外层 driver 因原 DN 数学求解未过门而退出 1。observer 实际墙钟为 3761.74039772 秒；不能用外层退出 1 把这些完整批次改称资源中断。

原完整 Newton 残差依次为 `1.5211857880e-8`、`5.7068517983e-9`、`3.2097725023e-9`、`2.4266321055e-9` 和上面的终态值。最后 `minA=0.980752332821046`、`minD=0.9999448760732821`。这些有限进展没有替代原严格接受门。

## 完整目标与保存状态

本次请求是原先保存的完整 **0.5H 向量**，共 20 个物理高度分量；没有换成完整 100% H。其 binary64 哈希始终为 `411ec0ff8775c34ce1106b1afa72ded610646a54384bb05dbb71afbbfd0ff70a`。原物理尾、M20、spacing4、N512、depth8、parts32、RK16、生产 `projectionFloor=.05`、36 次最大迭代、原 `2e-9` 门及 audit32 均保持不变。配置只改变已经声明的 `initialCheckpoint` 与 `traceFile` 路径。

完整失败响应和 checkpoint 位于 `n4_work/native-dn-halfH-v1/tail_0001.json.gz`，SHA-256 为 `ebae719050d7122fb15b64795cc9c2480aa0afc6b42df9a8c7863d51c6f88306`。保存状态已经经过本轮原 Newton 更新，不再具有先前某个具名邻数候选的“仅改一个坐标”身份。

只读 collector 核对最终 checkpoint 的 2305 个节点，并把 nodes1–2304 的每个原状态输入与最后一次完成的全 Jacobian 批次输入逐字节对应：共 96768 个输入标量，包括每段追加的两个零均值分量。最后被拒绝的标量候选没有冒充保存的 Newton 状态。这个输入身份检查不单独覆盖 node0 的左端边界或远端 Robin 条件；那些条件仍由原完整 DN 残差计算负责。

## 已保存内部行的有限定位

对该最后完整 Jacobian 批次的只读解析显示，内部行中仅一行达到或超过原门：stage43、component38，即 mode76 的动量行。保存的 flow 为 `-1702.1893878738542`，节点值为 `-1702.189387873853`，差为 `-1.1368683772161603e-12`，原归一尺度为 `0.0005508906608046747`。其归一残差恰等于上述原完整残差。

这个差在当前数值附近为 5 个 binary64 间距，不是单邻点差，也不是机器精度下界或数学不可解证明。这里没有重新计算流，没有构造新的局部候选，也没有重建未保存的 trial node0。完整定位输出仍在 `n4_work/native-dn-halfH-v1/iteration4-internal.json`，SHA-256 为 `382e886e5361654927dbef7d2a0279c501b59ad4916c21865a40c038359b7491`；其源码为 `scripts/resume_n4_tail/diagnose_native_saved_internal_rows.py`，SHA-256 为 `2b34b5c33206aafde272fd511e05ea88fc66418ff52af20928371922556e6410`，实际只读终态为 `e32132`、退出 0。

## 来源、资源与后续目标

实际 DN 源仍为 `native_extended/continue_native_tail_checkpoint.py` 的 `117b0a6d…` 版本，执行计划仍为 `7aadf151…`；运行中没有更换源码或安装并行包装器。紧凑终态记录为 `scripts/resume_n4_tail/native_original_DN_halfH_terminal.json`。collector `record_native_DN_terminal.py` 的 SHA-256 为 `71e6aa510615ad3e41f17d4f6e3f4ceb051c057c7278f965671598f5b7096b06`，实际只读执行 `73129 / 992265` 退出 0。各批次输入、输出、日志和完整来源列表以 scratch manifest `terminal-native-records.json` 绑定，未将节点或逐段表写入 Git。

observer 的 namespace 采样树 RSS 最大值为 24228 KiB，`RUSAGE_CHILDREN` 的 `maxrss` 为 946612 KiB；这是两种不同观察，均不称全主机所有子进程的同时峰值。

半幅 H 是辅助初始化目标。下一条实际工作将这个完整失败 checkpoint 明确作为**未接受初值**，用已核对数值字节相同的四进程入口，调用原 raw coupler 的 `--scales 1`，直接求所需的完整 H，再接原前缀联立。完整 H 必须自行通过原 DN、Jacobian 和审计门。本条未完成 full H、实际 raw 前缀联立、精确圆弧、连续闭族或 10% 指标。
