# 每请求线性 DN 延拓 v2：独立全文与原接口审查

审查者：`/root/tail_theory`，2026-11-09。

**结论：冻结 v2 的数学范围、原源码控制流及所规定状态机通过静态独审。** 本结论允许把它作为新 adapter 的待实施规范，不是对尚未出现的实现、实际目标可解性或新联解结果的批准。没有调用 DN、角向 root、RK、flow、BVP 或优化；没有读取活动 continuation03 的输出。仅重放了明确关闭的 matched-cut 两请求的标量诊断。

## 1. 绑定对象与实际复核

最终稿为 `2026-11-09-db6f-prefix-matched-cut-linear-dn-continuation-plan-v2.md`，SHA256：

`a65890daff2c55ff8e0593445c0f7689e06d445024e87988444160762da04fe6`。

v2 来源账本 SHA 为 `b0af556d2cc5aae09bbe4a0eb43be7d20ae75bbc987de759f43741eb77a5f983`。原 v1 的 `62e59c6b…` 正文、五件出版清单及所有源均保持原字节。独立检查按账本的四个唯一字符串替换重建 v2，结果逐字节一致，没有未声明的第五处修改。

本次重新核对原来源账本的 32 件直接源码和已关闭材料；从实际原命令的 `--source-root` 定位 `repro/source-root`，另核原 121 件输入账本中的五个有关引擎源：`general_root_tail_momentum.mjs`、`f6tail_fast_momentum.mjs`、`f6tail_fast_split_flux_engine.mjs`、`f6tail_cusp_grid.mjs`、`f6tail_momentum_split_flux.mjs`。121 件账本本身已核哈希，**没有把只选读五件说成重新读取全部 121 件**。逐文件路径、字节数和完整 SHA 均在独立 `tail-review-linear-dn-plan-check.json`。

已全文读计划、原 trial-client/worker/core/split、warm-remesh、coupled 与两个选择 wrapper，并核实际 source-root 的 root、split-flux 和 cusp 路径。未通过模块 import 执行这些源码。源码身份核查、Python AST 解析和四处差分的独立工具 receipt 为 `89e8bc`，实际 exit0。

作者已关闭诊断脚本 `db6f-prefix-matched-cut-dn-request-compare.py` 以新的独立输出路径重放，receipt `7bd517`，实际 exit0。输出为 11,433 字节，SHA：

`c15fe8ad4b26adea9638acca728bcf170d7cae744b10e1b66b2e923cbacdd702`。

该输出与作者原诊断逐字节相同。它只读取已关闭的 15 件运行文件及八源、重算标量；不是新求解，也不是原 JS 初猜数组的逐位重放。

## 2. 关闭失败的证据范围

本稿所用 matched-cut 运行是根实际观察关闭的 session5817，receipt `ff466f`、tool exit0；Python 正常结束与数学接受不同。其 summary 明确 `solver_success=false`，没有成功 prefix CP。第一 DN/J 是实际成功，残差约 $1.2533744092\cdot10^{-9}$；第二个响应只有 `failed/lastIteration/checkpoint`，不得为它补写正常 residual、converged 或 audit 字段。

第二请求的保存基点及其最后十档失败标签在关闭诊断内得到复算。所有 15 个请求高度都改变；最大绝对差在首模，最大相对分量变化在极小的第 15 模。这些标量不证明高模相对变化就是失败原因。最后十档全是原 momentum-root-solver 拒绝，不可挪用另一次 continuation03 的“小 Newton 步可下降”结论。

原 `db6f-prefix-coupled.py` 在 auxiliary inner `sol.success` 后才发第二个实际 DN。该 DN 抛错发生于真正 `o.bc` 及 actual-outer-check 追加之前，因此只支付 inner 成功的控制流事实，不支付真实 outer BC。根的实际工具关闭记录与数学失败内容已分开；本次审查不读取或评价仍活动的 03。

## 3. 原方程、物理高度及局部延拓

每次外请求固定物理高度原点及目标，使用

$$
H(\tau)=H^0+\tau(H^{\rm tar}-H^0),\qquad 0\leq\tau\leq1.
$$

这里 H 的 15 个分量正是原 port 的物理 cut height。原 DN 入口负责除以 $r_{cut}^4$；新协调层重复归一化会改变边值，v2 已明确禁止。它与旧 $s^{j+1}H_j$ 的曲线路径不同。

有限方程 $F(Y,H)=0$ 在一个真解附近的可延拓性需要联合光滑、$D_YF$ 可逆以及分支保护的严格余量。隐函数定理在这些条件下给局部结论，不给当前整条线段的存在性或唯一性。保存的 minA 和浮点 Jacobian 没有证明这些全域假设。原线性 warm 也不是解支的精确切向预测，不支付二阶预测误差。本节的条件量词准确。

原 M15/N256、depth12、p8/s32、36 轮、solveTolerance $2\cdot10^{-9}$、projectionFloor .05、原十档 Newton 线搜索和物理 g 不变。内部 32 次物理调用预算及 dyadic 路径步长是新的搜索工作预算，不能冒充原误差容差。原 true outer、inner、physical BC 和最终 seam 门均另保留。

## 4. last 与 cache 的复制、更新及失败边界

### 4.1 原 warm 并非总是复制 last

worker 只在首高度比值有限且严格位于 $(.25,4)$ 时对 `last.states` 作两层 `map`，得到独立数组。保护区外 `initial` 保持未定义，core 按原规则选择线性 initial。v2 正确修复了 v1 的无条件复制表述；该回退仍解同一个目标方程，但不保证小步预测质量。

当前所有高模非零，不满足原特殊 harmonic 分支的“请求高模全零”前提。保存请求标签 H 与 `last.jets.height` 必须保留为不同字段；原首模 ratio 的分母来自后者。线性边界修正只改初猜，仍由原 `correctInitialBoundary` 及原 `tail.initial` 执行。

core 对传入 initial 再逐行复制。Newton、trial 和 progress 的局部数组不会通过别名改写先前成功 `last.states`。worker 仅在整个 `dn.solve` 正常返回且 `sol.converged` 时执行 `last=sol`；正常非收敛返回和赋值之前的原数值异常均不更新 last。写 recovery checkpoint、保存 progressStates 或 FAILED stage 不等于更新 last-good。

### 4.2 Python cache 与真实包号

原 base client 在实际 wire 前递增 `.calls`；保存每个响应之后，只有 `converged` 为真且无 failed 才更新 cache。失败会增加 `.calls` 而保留旧 cache。v2 因此要求 adapter 另存成功包号，并在每个正常向外返回时核对它等于当前 `.calls`。这个条件是原 seam 使用 `_tail_{calls}.json.gz` 的必要接口保护。

缓存命中沿用 `np.array_equal`，无 `isclose`。它是不区分正负零的数值相等规则，不是字节身份。Jac=true 只有已有实际 Jacobian 时才可命中；audit=true 总是绕过 cache。失败之后若旧 cache 已落后物理包号，跨过同 H 逻辑节点不会消除差异：必须先有后续实际成功刷新，或以终止失败结束实例。

base client 保存响应使用独占创建，但不是原子临时文件替换。完整 closed 包、尺寸与 JSON 身份校验不可省；部分写入、ENOSPC、EOF 和 JSON 错误不能视为普通数值失败。base 对成功 schema 本身的验证较窄，adapter 还须检查残差、状态和身份；若发现伪成功或非有限值，worker/cache 可能已经更新，所以必须终止，不能回滚假定 last 未变。

## 5. 三类自动步半的封闭依据

v2 的允许分类经过全文核对；它们是将来实现必须逐项落实的门，不是从任意 exception 推出的恢复能力。

| 类别 | 必要的关闭证据 | 为什么可保留 last-good |
| --- | --- | --- |
| 完整正常非收敛 | 明确 converged=false，原请求、参数、完整 schema 和有限性均有效 | 整个 DN 返回但 worker 不赋值 last，client 不更新 cache |
| 原 shooting 线搜索汇总失败 | 本 call 所有已闭 trial 行无未知/other/I/O；最终失败基点的原十档齐全，只有已核 momentum 拒绝或有限残差不降 | 失败发生在 `tail.solve` 的 Newton 线搜索，尚未返回完整 DN |
| 首次 progress 以前的已知 root 失败 | 中间 flags=false/false；failed 包恰有三键，lastIteration/checkpoint 均显式 null；同源、同参数、36>0；精确 known-momentum 白名单 | 同一 request 首次 evaluate 在 progress 之前；末后的 cutRaw/cutJets 必须在至少一次 progress 之后 |

第三行的证明需要固定原源码，而不只是 error 文本。worker 每次请求先把两个 progress 槽置 null；正常 warm 数组复制、原线性 initial 不调用该 momentum root。core 每轮先 evaluate，随后生成 history 并回调 progress；progress 在写 trace/iteration 文件之前设置两个槽。36 为正，所以到达 solve 末端的 `toRaw` 及 DN 的 `cutJets` 必已经过一次 progress。因此在规定的精确三键/null 证据下，已核 root 错误只能归入首次 evaluate。缺键的 `.get()` 返回 None 不足以支付这条推理。

原 trial evaluator 能捕获任意异常并最终汇总为 `multiple-shooting line search failed`。只查这个字符串，或只看最后十行，均不足以排除本 call 早期未知错误。v2 要求检查本 call 的所有关闭 trial 行，正确保留了这一限制。原 momentum 白名单须绑定精确源码字符串，不能使用任意宽松前缀把其它错误纳入。

即使中间 flags=false/false，`dn.solve` 仍会计算 cutRaw/cutJets；不能把它叫作没有后处理的纯射击返回。已有 history 的同名 root 错误，在原 schema 不足以定位时必须停止。worker 在 `last=sol` 后仍有 trace/输出 I/O，所以后赋值的 I/O 异常也不得采用“last 未更新”的证明。journal 写入失败同样终止。终止后若需恢复，只能另建进程/stem，明确从完整关闭的成功 CP 重新验证。

## 6. 原点、相同浮点 H 与有界工作量

新 base client 的 cache 初始为空。输入历史 CP，即便确曾成功，也只是当前进程的 warm；不得预填旧响应/Jacobian 为本次 last-good。计划要求首请求同高度时按原 flags 真算一次，或先对明确绑定的种子标签真 bootstrap。这一 gate 保留了真实响应身份。

每个外请求的 origin 和 goal 均复制固定；中间 H 用固定二者计算，不累积舍入后的新原点。$\tau=1$ 显式 `goal.copy()`，故不会把最后的插值舍入结果当作原目标。

非终点若得到与当前真成功标签数值相同的浮点 H，v2 允许逻辑推进，且明确不产生新实际请求、新成功包或新的数学成功。逻辑 tau 位于最低间隔 $1/1024$ 的 dyadic 格，最多 1024 次推进；若已等于 goal，直接进入原 goal 的终点处理。这比 v1 一律停止更适合原 seam 的极小高度重请求，并未降低目标精度。

所有真实 bootstrap、失败尝试和最后验证都计入每个外请求最多 32 次物理调用。至少预留必要的最终验证位；预算耗尽、最小步限制和停滞均以“目标未完成/未验证”终止，不能把最后一个中间解返回外层。缓存相等逻辑不能绕过第 4 节的成功包号不变量。

## 7. 最后目标、Jac/audit 与原 outer

到达目标的中间真响应后，原 requested flags 决定最后验证。Jac=true 必须返回原目标的 705 项 heightJetJacobian；它是原物理 H 的导数，不是沿 tau 的割线、插值 Jacobian 或路径导数。audit=true 必须真正触发原 auditSteps=32 的实际请求。两 flags 均 false 时可用原合法同目标 cache，但它仍须对应最新成功物理包。

最后 VALIDATE 的任何失败都代表该外请求未完成，不再将其作为较小 tau 的可替代成功。即使同 H 的中间射击已收敛，也不能伪补 requested Jac/audit。正常返回以后，原 `o.bc`、原 outer 检查和最终 seam 继续决定是否接受整个 prefix；延拓不增加 H 的额外外边界条件，也不把固定目标求解替代自由切口 outer。

原 shooting 每轮 `evaluate(...,true)` 的全变分仍执行。中间 Jac=false 省掉的是响应层 heightJetJacobian 等后处理，不能据此声称每个中间步骤没有变分成本。32 次物理请求是实际可能昂贵的上限，并非廉价保证。

## 8. 来源身份、日志与实施审查的剩余范围

每个新包应真实保存旧八源加新 adapter 共九源，不能以 adapter 哈希替换原 trial-client 的哈希。原 base 的 `sources` 字典确被每个响应 record 采用，因此首 wire 之前追加新源能够实现该身份要求。新 wrapper、策略 sidecar 及 transitive source-root 仍须另由 launch/journal 绑定；九个直接源并不等于全部依赖。

原 source 文件、原 121 件输入身份和旧审计器保持历史冻结；新运行必须使用新的记录前缀、真实九源门与对应输入绑定，不能修改旧记录让旧门接受新方案。策略不能作为未知字段展开进物理 factory 的参数。日志至少关联 external request、固定 origin/goal、tau、尝试号、实际包号、已关闭失败分类、最后 GOOD 与最终 requested flags。活动 trial 文件不能整件临时哈希后冒充关闭身份，只能提取本次已闭 call 的完整片段并核其边界。

以上是静态规范的 PASS。将来 adapter、选择 wrapper、策略/schema、实际 journal 原子性及输入准备器出现后，仍需另作完整源码独审，核实这里的分类和包号不变量确实实现。后续实际数值运行还须由真实工具退出与原响应/outer/final seam 同时判读。本文没有为未来 M15/N512、完整图 metric、曲率、reach、G5 或 README 完成作任何代证。

## 9. 可复核材料

- 独立只读身份检查器：`scripts/db6f-tail-review-linear-dn-plan.py`。
- 独立机器检查：`notes/2026-11-09-db6f-tail-review-linear-dn-plan-check.json`，SHA `18290d3701a95d674afda0c11e4ee9bd46a76ea4003a5dc75b91c0b5416b3fd5`。
- 原关闭标量诊断的独立重放：`notes/2026-11-09-db6f-tail-review-linear-dn-closed-diagnosis-replay.json`，与作者 `c15fe8ad…` 逐字节相同。
- 本次实际执行记录与闭文件总清单另列，均不包含新的 solver 运行。
