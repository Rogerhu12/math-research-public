# λ=.64：原内解接受，新 H 原尾停止门失败

**状态：数值证据与完整终态身份；未得到完整物理审计或最终解。**

[λ=.64 的唯一入口](2026-11-18-m3-trace-path-lam064-coupled-entry.md) 已完整终止。原 `solve_bvp` 经过 2 次网格迭代，在 518 个节点返回 `success=True`，最大 RMS 为 $9.88664786974291\times10^{-7}$。实际 Newton 共接受 11 步，均为全步；域拒和 merit 拒均为 0。其完整原始 $x,y,p$、全部 RMS、$4\times517\times25$ cubic 与真正的旧 DN 锚均已保存。

原内解返回后，coupler 对新的完整 8H 请求实际尾部，保持原 `jacobian=True`、`audit=True` 和严格 $2\times10^{-9}$ 门。原尾在 iteration 4 以

$$
\mathrm{norm}=3.667517320458417\times10^{-9}
$$

线搜索失败。该迭代记录的 `minA=0.5217377678289357`、`minD=0.9991188300565388`；这些只是实际有限读数，不据此声称连续域认证或把失败原因归为域退化。原失败 checkpoint 完整保存，有限尾 audit 未成功返回。

## 参数与状态范围

本次仍是同一显式有限物理同伦：$\lambda=.64$，定义支撑幅值 $q=0.054696409291371345$，数值 gauge/warp 为 `.06`，M8 的七列及原 parameter scales 不变。`fixed=False` 的首参数仅控制基底 profile 的 δ 位移；实际返回 `p0=-1.3940640122370465e-5`。全部八个参数、七个真实控制与新 8H 均列入紧凑记录，不能把大数值参数与其有尺度的物理控制混为同一量。

原内解返回文件是 `m3_work/trace-path-lam064-coupled-v1/inner-00-returned.json.gz`，SHA-256 为 `8cf33fae278e949488af8f09ebbc178dd910ac07306ca306e1080fa2815f73df`；DN 锚 sidecar 为 `f8bc77ca3b381c509be7b05775fbb9670a462a765ada554b4003032f8b245ff5`。本次共保存 19 个真实 raw 快照及各自 sidecar，没有把其中的中间状态标成最终物理 checkpoint。

实际新 H 尾失败记录是 `seed_tail_0001.json.gz`，SHA-256 为 `753aa9ec4584f0bafa216acbfaffe98fab44a0369e914ca06c7c739d81b365c4`。原 outer 的实际 BC 检查因该尾失败尚未完成，未创建物理 quintic，未取得完整前缀 metric、mean-height 或 seam 审计。不能以原内解成功代替这些后续门。

## 真实终态与接续

observer session **98842**，启动块 `783db1`、终态块 `5e1ac0`；于 **2026-11-18 05:00:33 UTC** 记录 child=0，原 worker=0，历时约 272.41 秒。进程退出 0 只表示原异常收集流程正常结束，原数学 `solver_success=False` 已单列。

[紧凑终态记录](../scripts/resume_m3/trace_path_lam064_coupled_terminal.json) 由已冻结纯只读 collector 生成：`7c9c27`/exit 0，核 123 个执行来源、全部 raw/sidecar 和真实尾记录，未构造模型或重新计算任何方程。

接下来只对这个新保存的实际失败尾作一次完整行定位，再按真实超门集合决定最小初值；若新 H 原尾接受，恢复本次已接受 raw inner 的原 post-tail 流程。不会重跑该内解、旧初猜或旧审计，也不会从此次尾门失败推断一个普遍机器精度下界。后续定位与修复作为独立结论登记。
