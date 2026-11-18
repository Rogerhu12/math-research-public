# q060 H_old：资源修正后原候选完成，遇到同一行并列峰

**数值证据与原方程依赖推断；没有原生接受。**

前次自动候选发生明确的 Node heap-limit OOM，未产生候选结果。
本次直接使用已保存的同一个完整 warmup 失败态
（SHA `adf477252c1dc707ce4fe8975aa9c911aca2f9d4c5113ba300d11b82023c4535`），
只显式增加 `--max-old-space-size=3072`，补完同一已声明候选程序。
源仍是 owned 的 `propose_tail_internal_candidate_v3.mjs`，
SHA `b7a8281b12b17c403edc7ba59adf1a7ee72f84a61e8beed0e2562c354dffdcb7`。
没有修改列表、分支条件、16 轮上限、参数、方程或原门。

session93784 真实 exit0，29.844 秒。
原 full-Jacobian replay 与原停止范数逐位相等：
$3.671459625080514\times10^{-9}$。
只有 3 个比例试步实际改变 binary64 状态，其余较小步舍入后不变。
第一轮没有严格改善，程序保留原状态；最终原全 replay 仍是同一个范数。
没有原 worker 重试，因为它的严格改善前提没有成立。

## 新的具体停滞原因

原选择峰是 stage86/component8（mode3 动量）。
最佳已试但未被接受的单节点试步为 $\alpha=1/2,\beta=0$。
它改变的仍只有 node86/component8，结果为：

| 部分 | 总归一化残差 | 具名最大分量 |
|---|---:|---|
| row85 | $6.117678421052487\times10^{-10}$ | component8 |
| row86 | $3.671459625080514\times10^{-9}$ | component11（mode12） |
| 最大未受影响行 | $1.8199376260757712\times10^{-9}$ | 本条不另定位 |

这里不能仅称“一个 ULP 候选失败”。原方程
$R_{86}=\Phi_{86}(X_{87})-X_{86}$ 中，只改 $X_{86,8}$ 不会改变任何
$R_{86,j}$（$j\ne8$）。因此试步后 component11 保持与原总峰逐位相等，
说明它本来就是同一行的并列峰。单分量步骤无法满足严格总范数下降，
便不会进入下一轮。这一推断直接使用已执行试步与原依赖关系，没有
为猜测重复一次全域 locator。

下一项若需要双分量候选，应先只在这一个原局部行核对两个具名残差的
符号和 ULP，再限定一次相应内部变化，并重新做原局部及全 replay。
本条没有执行该后继操作，没有扩大比例搜索，也没有把当前失败当作
不存在或机器精度下界的证明。

紧凑执行记录：
`scripts/resume_transfer/q060_warmup_resource_candidate_failure.json`。
完整候选表与状态只留 scratch；输出仍明确 candidate-only、
solver_success=false、original_solver_invoked=false。
