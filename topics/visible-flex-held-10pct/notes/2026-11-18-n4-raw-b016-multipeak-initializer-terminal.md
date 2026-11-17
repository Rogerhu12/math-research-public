# n4：多峰初值规则的有限终态与原门保留

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

## 本次结论

对[新失败态](2026-11-18-n4-raw-b016-relaxed-tail-location.md)实施预先声明的
顺序多峰初值规则，第一 pass 实际评估 8 个候选，均没有严格降低完整局部分数。
规则按其声明条件停止，最终原 full-Jacobian 重放仍为
$8.024431255867547\times10^{-9}$，与输入逐位相同。
因为没有严格完整残差改善，本次没有重复调用原 DN 求解器。

所以本条既不是新的 DN 失败迭代，也没有接受的真尾。
输出 envelope 的 `response` 为 `null`；其 hash 记录这次有限策略终态，
不能被当成含有一份新数学状态的 checkpoint。
后继初猜仍须明确引用原 `relaxed-tail.json.gz` 失败态。

## 实际候选为何未被选中

当前完整最大行是 stage 19、component 38（mode 76 动量）。
第一 pass 使用源码声明的
$\alpha\in\{1/8,1/4,5/16,1/3,3/8,1/2,3/4,1\}$。
改变 node 19 后，rows 18 和 19 都用原 full-Jacobian flow 重算，
其余行缓存与两端边界一同计入完整分数。

最小步 $\alpha=1/8$ 已把 row 19 降到约
$7.02138\times10^{-9}$，但将 row 18 提升到
$2.4268896856267033\times10^{-8}$；其余所列单点候选也没有改善完整分数。
较大步长下，row 19 内的 mode 80 分量成为约
$7.02138\times10^{-9}$ 的主导分量。
源码的第二节点分支要求所调下游行已低于原门；本批该条件均未成立，
所以没有实际评估 $\beta$ 候选。

这是这个有限候选规则的负结果，不是对任意内部初值、完整真尾、
或闭合构造不存在的证明。尤其不能把预设的最多 16 pass 写成本次已经执行 16 pass。

## 接受逻辑与来源

执行源码
[`probe_tail_multipeak_initializers.mjs`](../scripts/resume_n4_tail/probe_tail_multipeak_initializers.mjs)
SHA-256：
`9d3c5984b9de051c4c567a566f1386dcb45e2831b761fefe692ccf06cc211cb5`。
该源在运行前经过独立只读审查，本次运行中保持冻结。

每次改动的 node 集合对应精确的受影响行并集
$\bigcup_i\{i-1,i\}$；左右原边界残差均计入分数。
局部根域失败只丢弃候选，不改变物理根域门。
只有最后原完整重放严格改善才允许调用原
`dn.solve(jacobian=true,audit=true)`；最终接受仍唯一来自原求解器。
本次没有进入这一步，因此没有新的解析 DN Jacobian 或终态 audit。

紧凑记录：
[`raw_primaryb016_lam002_m20_multipeak_terminal.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_multipeak_terminal.json)。

- 输入完整失败态 SHA-256：
  `886a67f6cc8932873fefb350ed533bbff1a75a4bc282adcd1481eef48515d31d`。
- 无新状态的输出 envelope SHA-256：
  `caf5ac54a0dba716a33221124b115a378027ee112eafa63311644813071e8b4a`。
- 全部 config 与 20 个实际 height 分量经 binary64 身份比较，保持相同。
- owner session 35900 于 2026-11-17 23:24:40 UTC 真实 exit 0。
  脚本约 134.48 秒，外层观测约 148.32 秒。
- 完整状态、所有 trial 和全表保留在 scratch，Git 只保留源码、标量和 hash。

$0.2H$ 只是原初始化路径上的一个请求，不是目标构造必须支付的物理终点。
本条不把该失败态升级为接受态；后继可以声明它只作初猜，按原 worker 的已有
高度 predictor 请求更接近完整目标的 $0.5H$ 和 $H$，各自仍须过全部原门。
