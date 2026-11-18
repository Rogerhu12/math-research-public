# q060 新圆弧 M8 真联立：首次 RMS 额外取点越过原 Frenet 域

状态：**本次真实联立未得到返回的 BVP 解；没有新实际尾响应、最终 cubic、完整参数或 metric。**
原 `solve_bvp` 在第一轮 Newton 返回后、第一次 RMS 估计完成前抛出了域错误。
保存下来的只有该 inner 的完整入口状态和原实际 DN 锚，以及执行/异常日志。
不能把日志里的两个末参数标量当成已恢复的最终状态。

## 1. 原入口实际执行与身份

本次严格执行
`2026-11-18-q060-circle-trace-coupled-entry.md` 的冻结计划：

- 新 $q=0.05210565550627671$，M8/25 状态，控制空间
  $\operatorname{span}(B_2,\ldots,B_6,T,U)$；
- $\lambda=1$、$a=.21$、主过渡 $.32$、控制过渡 $.4$，原所有数值域门保持；
- 基础 profile 使用旧 q060 最终冻结值，`fixed=False`、新 `p0=0`，warp reference $.06$；
- 原 271 节点初猜、max_nodes 6000、原 RMS/BC/merit/尾阈值，以及原八轮实际尾外循环。

运行源 SHA-256 为
`1204d93ce144efec9d61d34de7af189e4c597d3c1bf85090a1f7bcbae7c020f3`，
启动计划为
`8b9de60b551deccd8ceb4bb2f88ee6f406b3b24e6abc35158f54ebeae0c54da4`。
2026-11-18 01:57:08 UTC 开始；独立 observer 的工具 session 为 `12897`，
启动 chunk `0d336f`，终态 chunk `5e626c`。
01:58:12 UTC 观察到 child exit 0，原 worker exit 0，总观察时长约 64.06 秒。
这些退出码表示异常被原控制流记录后正常结束，**不是数学接受标志**。

必要重建在 01:57:10 UTC 完成；原 $y,p,H$ 的三个完整 binary64 哈希、
七项物理控制及尺度均与已登记唯一初猜一致。
没有重跑那份初猜的 RMS 诊断，也没有调用旧余弦 restart。
01:57:22 UTC 原 worker 完成初始化，首个相同八项 $H$ 复用了已接受原响应的已有缓存。
本次新 native 请求计数为 **0**；worker 日志只有一条 `warm_initial_state`，
不存在本次新接受的尾记录。

## 2. 确切的失败阶段

原首轮 Newton 的已记录统计为：

| 项目 | 实际记录 |
|---|---:|
| 网格节点 | 271 |
| 接受的 Newton 步 | 9 |
| 原域拒绝试步 | 60 |
| 原 merit 拒绝试步 | 4 |
| 最小接受 alpha | $1/2048$ |
| singular 标志 | false |
| 日志所存末 `p0` | $0.0012654705997656407$ |
| 日志所存末 `p1` | $-14.69994229085809$ |

这不是 max-nodes 终态，也不是最后的 prefix/seam 审计失败。
实际 traceback 明确经过：

1. SciPy `solve_bvp` 接收原 `solve_newton` 返回值；
2. 重新计算原节点/中点 collocation 数据，构造原 cubic；
3. `estimate_rms_residuals` 计算额外 Lobatto 点的 `f2 = fun(x2,y2,p)`；
4. 原 adaptive `frame` 抛出
   `Adaptive Frenet domain failure: -1.717530786436109e-06`。

因此本次 RMS 本身没有完整返回，后续加点/停止判定尚未完成，
外层也尚未拿到 `sol.success` 或新的完整 cut $H$。
此前的 60 次域拒绝只是独立试步记录，不能将所有拒绝都归为这一个末错误。

原 SciPy RMS 使用每段的节点、中点及

$$
x_\pm=x_{\rm left}+\frac h2\pm\frac h2\sqrt{\frac37}
$$

两点。原 Newton 的 `col_fun` 只直接取节点与中点；额外两点在 Newton 返回之后
才由 RMS 函数检查。本次错误发生在 $x_-$ 那次 RHS 调用中。
这定位出一个具体的取点域缺口；没有据此改变残差、放宽 Frenet 门或声称存在性失败。

## 3. 已保存内容与不可恢复部分

`inner-00-entry.json.gz` 的 SHA-256 为
`a2fced8cb9864fb9c3190d999d5a5a0e09ed08779c1efa867808bb088a6231f4`；
它保存原 271 个 $x$、$25\times271$ 个入口 $y$、八项入口 $p$ 和新空间身份。
对应 `inner-00-entry-dn-anchor.json` 为
`0c6062a321509f30a9a9f0a25b7aabe1d54e26614e5f76ed0614290fd30def7a`，
绑定原实际尾 `ae01f13a...` 的相同完整八项 $H$ 和完整响应哈希。

原 `solve_bvp` **没有返回**，所以外层“返回后保存 cubic”的钩子没有得到返回对象。
日志虽证明 SciPy 当时在进程内部已构造 cubic，却没有保存其字节。
当前不能恢复该 cubic、末网格状态或其余六项参数，也不能从 `p0/p1` 两项日志
计算一个声称属于本次末态的完整核心。
没有 `inner-00-returned` 文件、物理 CP、新尾文件或 metric。
不重跑这次已完成的内层来补造缺失状态。

后续若采用新的、明确记录的域检查方法，需要在每个原 Newton 接受赋值和
Newton 返回时就保存原数组及节点 RHS；本条只记录缺口和已完成失败，未执行该后续方法。

## 4. 只读终态收集

紧凑记录由
`scripts/resume_m3/collect_q060_circle_trace_coupled_terminal.py`
读取完整已结束输出生成。它核 66 项冻结来源、派生函数、原入口数组哈希、
实际 DN 锚、观察器终态及“无返回态/无新尾/无 CP”的文件范围，
没有重算核心、RMS、Newton 或尾。

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/collect_q060_circle_trace_coupled_terminal.py \
  --run-dir /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-coupled-v1 \
  --out /tmp/q060-circle-trace-terminal-new.json
```

实际只读收集工具 chunk `189e89`，真实 exit 0。
入库紧凑记录 `q060_circle_trace_coupled_terminal.json` 的 SHA-256 为
`427f091f8c9c10d1bc4069c79b914a8bd6f7fcaf93ca06c4dfef0057fbb89c07`。
原数组、完整日志和资源输出留在 scratch。
