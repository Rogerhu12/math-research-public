# 每请求线性 DN 延拓实现 v2：完整 trial 分组门

状态：原方程控制协议的修补与隔离测试；**没有新的 DN、BVP、实际候选或数学收敛结论**。作者为 `coupled_prefix`。本文与 v2 四个新脚本均另存，v1 源、原 15 类测试报告及其闭清单保留原字节。最终完整源码独审另行记录。

## 1. v1 的具体缺口与修补范围

`tail_theory` 的完整实现审查发现：v1 会检查读到的每行是否属于已知数值拒绝，再检查 aggregate 失败最后一组的十次拒绝，但没有要求更早的 iteration 组完整存在。因此，若末状态是 iteration 1，只有 iteration 1 的十行、整个 iteration 0 被截去，v1 仍可能允许缩小临时边值步长。v1 对正常 `converged=false` 包也没有要求其对应的全部 trial 组存在。

该缺口不更改原物理方程，但违反已审方案中“未知或不完整诊断应终止”的限制。**v1 不进入实际 pilot**。旧隔离报告仍只证明其中实际执行的那些协议例，不被追认为完整性证明。

v2 新增 `complete_trial_groups`，并只在原失败分类函数中使用。原 Coordinator、真正客户端构造、物理调用计数、缓存规则、原始包验证、最后精确目标和请求 flags、原 worker/core/RK/root 均不修改。选择器和纯准备器只改为选取 v2 路径、两处版本化 schema，并把本勘误纳入输入绑定。

## 2. 原源码决定的完整组语义

依据冻结 `db6f-prefix-tail-trial-core.mjs` 的 `solve`：每个 iteration 先保存一次完整 Jacobian 基点，再依次尝试 $2^{-k}$，其中 $k=0,\ldots,9$。每次 trial 的诊断在原串行回调中追加。第一次真实残差严格下降即记 `accepted` 并退出该组。

因此，一个已完成并继续到下一 iteration 的组必须满足：

1. 从 `trial=0` 起连续出现，索引为 $0,\ldots,k$；
2. 组内 `iteration` 和 `baseNorm` 相同；
3. 唯一 `accepted` 是末行；此前每行只能是已知数值拒绝或真实残差不下降。

若 aggregate line-search 失败发生在 iteration $i$，则完整已闭记录必须依次包含组 $0,\ldots,i$。前 $i$ 组满足上述接受规则；最后一组必须恰有十行、全部拒绝，且各行 `baseNorm` 等于原失败包 `lastIteration.norm`。原错误字符串中的数值也仍须与该 norm 相符。乱序、重复、缺组、缺 trial、未知错误均不允许自动折半。

正常 `converged=false` 的控制流更强。原固定预算为 36 轮。如果任一基点满足原容差，循环会立即退出，随后不会再评估接受后的其他状态，正常返回必为 `converged=true`。因此正常 false 返回只能用满 36 轮，而且每一轮都已经接受一步，否则早已抛 aggregate 错误。v2 要求：

- `history` 恰有 iteration $0,\ldots,35$；
- 36 个 trial 组全部按顺序完整接受；
- 每组 `baseNorm` 等于对应 `history[i].norm`，末行 `step` 等于对应 `history[i].step`。

**不增加两条错误的逐位等式。** 接受后原源码会额外做最终完整评估，所以最终 `residual` 不必等于最后保存的基点 norm；state-only trial 评估与下一次 full-Jacobian 评估也不要求逐位同值。v2 均不添加这些门。

第一次 progress 之前的已知 momentum 异常仍保留原窄分类：请求两 flags 均 false、准确三键失败包、`lastIteration` 与 `checkpoint` 明确为 JSON null、当前 call 无 trial 行、原 36 轮及完整来源绑定。其它后处理或未知异常仍终止。

## 3. 新文件与执行范围

新文件为：

- `scripts/db6f-prefix-tail-linear-continuation-client-v2.py`；
- `scripts/db6f-prefix-flat-linear-continuation-coupled-v2.py`；
- `scripts/db6f-prefix-prepare-linear-dn-pilot-v2.py`；
- `scripts/db6f-prefix-test-linear-dn-protocol-v2.py`。

新 policy schema 为 `db6f-physical-height-continuation-v2`，新 pilot launch schema 为 `db6f-linear-dn-closed-request-pilot-v2`。原每轮 36、尾容差 $2\times10^{-9}$、floor $0.05$、同一固定 metric、临时线性边值路径、最大物理请求 32、最大逻辑推进 1024、步长区间 $[1/1024,1/8]$ 完全不变。

首次未来实际运行仍限定为已闭 matched 请求 $H_0\to H_1$ 的单个外部请求；初始成功包只作 warm。新 stem 使用 `2026-11-09-db6f-prefix-linear-dn-matched-h0-h1-pilot-v2-01`。本次纯准备不生成或启动完整 prefix outer，也不修改仍运行的 amplitude03。

## 4. 已执行的隔离验证

新协议测试实际工具 receipt `c47cdd`，exit code 0，共 21 类。前述所有缺口都有定向反例：缺早期整组、缺中间 trial、把含 unknown 的早期组或前缀整体截去、乱序与重复、接受后仍有行，以及正常 false 的空行/缺轮/缺步长/基点不一致。全部被拒绝。

原抽象状态机仍只使用一个虚构标量和内存 stub，故这些测试不是未来正向物理响应。另只读已闭首个真实 DN 包检查原 schema 兼容性；非法数值副本仅存在内存中。真实 port、Node/root/flow/RK/DN/BVP、新候选包均为 0。

源码哈希、实际命令、纯准备输出和真实工具退出在同批 execution 与 publication 文件中完整绑定。实际求解若由 root 后续启动，必须另有真实运行观察；本报告不提供任何真实求解退出或数学成功。
