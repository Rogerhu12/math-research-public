# 匹配切口失败之后：每个真实 DN 请求内的线性边值延拓

作者 /root/coupled_prefix，2026-11-09。**状态：只读已关闭失败分析及静态源码差异计划。没有实现新 client/worker、创建新候选或启动 solver。** 原 continuation03 及全部已绑定源均未修改。

## 1. 已关闭事实及所能推出的结论

本次 matched-cut stem 为
`2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01`。

根实际观察 `2026-11-09-db6f-root-matched-cut-observed-execution-01.json` 的 SHA 为 `1f7a7290c5c65a9f73531cd0edddf8f15b0290477be7d0b74eff9a3d5ba57334`：session5817，工具 receipt ff466f，实际 tool exit0。其15件闭文件全部重新核了字节和 SHA。本次 Python 正常结束，但 summary 为 `solver_success=false`，真实 error 是第二次 DN 射击线搜索失败；没有成功 prefix CP。

| 项目 | 首次 DN/J | 第二次 DN/J |
| --- | --- | --- |
| 真包 SHA | `6f4de10c22fc05cedc87994c274c3643b5390add7bfe0ca71001e02a440a7a86` | `44088a6fce132438771fb83267754f32e8d12043379b8f83c1977eccaad0d1de` |
| request | 原实际重启高度，Jac=true/audit=false | 原 affine inner 成功后的候选高度，Jac=true/audit=false |
| 正常 residual | $1.2533744091676813\cdot10^{-9}$ | **没有此字段** |
| 原 response | 正常七字段，converged=true | 仅 failed/lastIteration/checkpoint |
| 最后已保存基点 | iteration0，minA=.10551506989602055 | iteration3，norm2489.354194334243，minA=.05044758616045935 |

第二请求的初始基点已经有 norm2528.657869764615、minA=.0725169878140196。三次仅接受原 Newton 步长 $1/128,1/256,1/256$；norm 依次为2508.914844855985、2499.1154926366553、2489.354194334243，minA 逼近原 .05 保护。最后十档 $1,\ldots,1/512$ 全是 `momentum-root-solver-rejection`，位置标签在 raw0/segment4/stage34–37。没有最后两档可评价但残差不降的情形，不能把另一次 continuation03 的小 Newton 步证据移到这里。

两实际请求记为 $H^0,H^1$。配置与八源逐项相同，15个分量均改变，没有分量变号。只读标量比较为：

- 最大绝对高度差 $1.2709397064221634\cdot10^{-5}$，在模1；其相对变化约1.5872393124%。
- 全向量相对二范数变化约1.5875052710%。
- 最大分量相对变化约23.7702259747%，在模15；该模绝对差仅 $1.6654020638587972\cdot10^{-16}$。
- 首次返回的 jets.height 与该次请求逐值同。原统一 warm 比率为1.0158723931241456，位于原允许区间 $(.25,4)$。
- 两个请求的14个高模都非零，所以当前 worker 不走特殊 harmonic 分支。按原标量公式重算的 normalized linear boundary 修正最大值约 $1.0409765777442666\cdot10^{-6}$，在模2；这只是读保存状态后的标量重算，没有调用 `tail.initial` 或重算 flow。

原 outer 只有在 affine inner 的 `sol.success` 为真后才发送这个第二请求；故其出现支付“该次辅助 inner 成功”的控制流事实。第二 DN 在真正 `o.bc` 评价及 append actual_outer_check 之前抛错，因此没有得到这次候选的真实 outer BC 接受值，更没有完整联解。首次 DN 成功仍有效。

同一失败 state/同一 H 的原样重试没有新增的数值理由。分段改变 H 会改变每段的初猜及线性边界补偿，确有可测试的改进空间；以上数据不证明目标 H 的正分支存在，也不证明它不存在。

## 2. 本方案与旧03路径的区别

旧 continuation03 把一个固定 affine goal 的第 $j$ 个存储分量变为 $s^{j+1}H^{goal}_j$。此处则在**每个实际外层请求**开始时固定最近的真成功高度 $H^0$ 和当次真正目标 $H^{tar}$，使用
$$
H(\tau)=H^0+\tau(H^{tar}-H^0),\qquad0\le\tau\le1.
\tag{1}
$$
两条参数曲线不同；当次 $H^{tar}$ 还是实际自由切口 outer 产生的高度，未必等于旧 affine goal。因此旧03的成功或失败不能预判新路径必成。

所有 H 都是传给原 DN 的**物理 cut-height**。新的协调层不再除以 $r_{cut}^4$，不乘 $m,r,w$；唯一归一化仍在原 DN 内。$g$、M15/N256、depth12、p8/s32、原36轮、tol $2\cdot10^{-9}$、floor .05、原 RK 和十档 Newton 规则全部保持。

从有限方程角度，设原射击残差为 $F(Y,H)=0$。小步只改变中间边值 H，最终仍要求原 $F(Y,H^{tar})=0$。若某精确有限解处 $D_YF$ 可逆、方程光滑且分支保护有严格余量，隐函数定理才给局部可延续性。当前 minA 和有限浮点 Jacobian 只是数值证据，没有把这些前提逐区间认证，也没有给整条线段的存在定理。原 warm 不是整个非线性解支的精确切向导数，不能声称预测误差必为二阶。

## 3. 最小实现可放在 client 层

建议新建一个独立 adapter，调用冻结的 `db6f-prefix-tail-trial-client.py` 的 `WeightedTailPort.solve` 作为每个实际子请求。原 worker/core/engine、原 `db6f-prefix-coupled.py` 及其 affine inner / true outer 接受逻辑无需改变。

原 base.solve 已有以下所需协议：

1. 每个实际 wire 请求有唯一递增 `self.calls` 和独立 `_tail_NNNN.json.gz`；failed 包也先保存，再抛异常。
2. 只有正常成功返回后才更新 Python `cache_key/cache_value`。
3. 缓存命中使用原 `np.array_equal`，且 audit=true 总是发新请求；Jac=true 要求已有真实 Jacobian 才可命中。

新 adapter 仍把 `.calls` 暴露为**实际物理请求数**，不能改成外层业务请求数。原 outer 的 `tail_calls` 和 `tail_seam.tail_record` 均由它定位最后真实响应。内部每个尝试调用原 base.solve，原 worker 的 `call` 也逐次增加，已有 stage-input 的 call/iteration/trial 文件名自然不冲突。新协调日志另外使用 external-request-id、attempt、$\tau$ 和实际包号。

缓存只允许原有限浮点逐项相等，不能加 `isclose` 或按小范数差接受。这里的“精确”是原 `np.array_equal` 的数值相等规则（它不区分正负零），不是新字节恒等规则。路径原点 H 使用最近真成功**请求标签**的副本；原 worker warm 比率仍按实际 `last.jets.height[0]` 算，不能将标签与实际 jet 高度混为同一个字段。

另有一个原来遇错即退出时不显眼的记录号约束：失败也增加 `.calls`，却不更新 cache。adapter 必须单独记住 cache 对应的成功物理包号；每次正常向外返回时，要求它就是当前 `.calls` 指向的成功包。内部失败后，只能在后续真实成功请求刷新该包号后返回。路径/验证失败一旦上抛，将这个 adapter 标为终止状态，禁止外层捕获后又取旧 cache 冒充最新响应。目标已经与当前最新成功 cache 相同时，原合法 cache 命中不增加 `.calls`，仍指向同一真包。最终 audit=true 必发新包，因此原 seam 文件名继续准确。

## 4. 失败恢复的源码依据及不能重试的错误

原 worker 从 `last.states.map` 新建初猜；core.solve 又对 `opts.initial` 逐数组复制。Newton 修改的是这些局部新数组。worker 仅在整个 `dn.solve` 正常返回且 `sol.converged` 时执行 `last=sol`。所以当前已知的射击/角向 root 数值异常在该赋值之前发生；非收敛正常返回也不更新 last。保存 `progressStates` 或 FAILED checkpoint 不改变这个事实。

结合 base client 的成功后 cache 更新规则，**有完整保存包的、可定位为原数值求解阶段的失败**之后，worker 的 last 和 client 的 cache 都仍是最近真成功点。adapter 必须保存并恢复自己同一份 last-good 请求标签/响应/包号引用，并核其仍指向这个真成功包；下一步必须从该点重新建立原 warm，绝不能用失败 checkpoint 续算并称其为 last-good。

这里不能把任意 error 都作为可二分的数学失败：

- 原已识别的射击/角向 root 数值失败，以及已完整返回且字段有效的 `converged=false` 可以进入细分；实现须从关闭的实际包分类，不靠 catch 任意 Exception。特别是 core 会把 trial 内捕获的任意异常汇总为 `multiple-shooting line search failed`，所以这个最终字符串本身不足以证明纯数值失败。若是此汇总错误，还须核本 call 已完成的 trial 行：只有已知 momentum guard/root 拒绝或正常有限残差不降时才自动二分；出现 `other-evaluation-rejection`、缺失/不完整行、I/O/协议错误或未知原始字符串就停止。原 trial 文件仍可继续写其它 call，只使用当前响应已经关闭的 call 行或冻结其小片段，不把整个活动文件的暂时哈希当闭身份。
- ENOSPC、记录失败、EOF、worker 消失、协议/schema/配置变化及未知异常停止本请求，不继续假定 worker 内态未改变。恢复必须在新进程、新 stem 中，明确用最近已关闭真成功 CP 作 initialCheckpoint，再真实验证。
- 尤其要注意 worker 在 `last=sol` 之后还有 trace/输出 I/O。该阶段的 I/O 错误不能套用“原数值异常发生在更新之前”的证明。

原 `dn.solve` 的 cut jets、Jacobian 或 audit 后处理若抛错，也不能把先前已收敛的射击态补成完整成功响应。下节把最后请求的原 Jac/audit 验证单独列为阶段，避免错误地把验证失败当成又一个更小 H 的成功。

已知 momentum 错误前缀仍须结合绑定源检查产生位置；不能从文本相似便认定任何任意外部错误都来自原 root。所有 `converged=true` 但 residual 非有限/未过原 tol、参数/请求不符、或成功 schema 不完整的响应属于协议/验收异常，停止而不二分。保存失败并不等于允许拿该失败作连续分支证据。

## 5. 有界状态机和精确目标门

下述是待实现的状态机，未生成任何新配置或可执行协调器。

### 5.1 首次尚无 last-good

新进程的 Python cache 为空。即使 config.initialCheckpoint 引用了真历史成功，也只是启动 warm，不等于当前引擎已返回一个新的真响应。

本例最小入口可继续使用已冻结 matched prefix warm，另将新 config 的 initialCheckpoint 指向本次真实 `_tail_0001`。首个实际 prefix 请求正是其 H；必须先按原 flags 真正求解一次，成功后才建立 last-good。不得把旧705 Jacobian 或旧 converged 字段预塞入 cache。

若将来首个请求不同于已绑定种子的高度，则只能先在种子标签高度做一次真实 bootstrap DN，再由其实际成功建立 last-good。种子须有明确来源、同 g/原数值配置及有限状态检查；bootstrap 失败则停止，不能以输入文件名代付成功。

### 5.2 子目标追踪

固定一次外请求的 `origin=last_good_request.copy()` 与 `goal=request.height.copy()`。不累计修改 goal，也不逐次把已舍入中间 H 再当新的线段原点。使用可精确表示的 dyadic $\tau$；每次目标为 (1)，但在 $\tau=1$ **显式使用原 goal.copy()**，避免最后一次插值算术改变原目标。

中间尝试全部调用原 `base.solve(H(\tau),jacobian=False,audit=False)`。只有完整真响应、converged=true、原 residual 小于 $2\cdot10^{-9}$、请求身份及有限状态均有效时，才推进 $\tau_{good}$ 并原子保存新的 last-good 包引用。失败时保持 $\tau_{good}$ 和该真成功态，从它出发将增量二分；失败态独立保留诊断，永不覆盖 last-good。

这个分支不得直接采用外层 affine slope、旧 Jacobian 插值或前一次 FAILED state 代替真实响应。若非终点的浮点插值 H 与 last-good H 逐值相同，明确停止并记录路径分辨率不足，不借 cache 命中推进虚假子步。若 origin 已与 goal 逐值相同，则无需插值，直接走最后原 flags 门。

一个明确、保守且有界的初轮策略可绑定为：初始增量 $1/8$，最大增量 $1/8$，最低增量 $1/1024$；成功保持当前增量，已识别的数值失败二分；每个外请求最多32个**实际物理请求**，包括 bootstrap、失败尝试以及最后验证。源和策略文件都须在运行前冻结。这些数字是工作预算，不是替换原数值容差或存在性条件。

至少预留一个实际请求位置给必要的最后 Jac/audit。若增量低于最低值、浮点 $\tau+\Delta\tau=\tau$、或物理请求预算耗尽，明确报告“该目标未完成/未验证”，保留最后真成功包与全部实际失败。不能返回最后的中间 jets 给外层。

状态转移可压缩为下表；`GOOD` 保存的是实际已关闭成功响应，不是仅输入 CP：

| 状态 | 允许操作 | 唯一成功出口/失败处理 |
| --- | --- | --- |
| `UNSEEDED` | 原真实 bootstrap 或首个同 H 请求 | 真成功建立 `GOOD`；否则终止 |
| `TRACK` | 从最近 `GOOD` 向固定线段下一 H 发原请求 | 真成功推进；合格数值失败回 `GOOD` 并步半 |
| `VALIDATE` | 对 goal.copy 发原 requested flags | 完整目标/flags 成功才 `RETURN`；失败终止 |
| `TERMINAL_FAILURE` | 保存闭包、错误分类和最后 `GOOD` 引用 | 禁止从旧 cache 正常返回或继续使用此实例 |

执行中的任何 journal/来源记录失败也属于终止错误。若真实 worker 已更新而 Python 记录未完整保存，不能从内存猜它对应哪个可复现成功点。

### 5.3 最后原 requested flags

到达 $\tau=1$ 的真 DN 解后，再对 **同一个原 goal** 调用原 `base.solve`，flags 精确等于外请求的 `jacobian` 与 `audit`。

- 外请求需要 Jac=true 时，只有原引擎对目标解给出的完整705项 Jacobian 才可返回；路径割线、Jacobian插值或 $d/d\tau$ 都不能替代它。
- audit=true 必须经过原绕缓存实际请求和原 auditSteps=32；不能把中间 audit=false 包改标签。
- 两 flags 都 false 时，原 cache 可合法返回刚完成的同目标真实包；这仍有可追溯实际请求身份。
- 最后 Jac/audit 阶段失败就是原外请求未成功。即使已有同 H 的纯射击成功，也不能把它标为已完成 requested validation，更不能用退回某个 $\tau<1$ 的成功响应替代。

只有最后原目标和 flags 都完成，adapter 才向原 outer 返回正常响应。此后 `o.bc` 仍按原 $10^{-8}$ 门检查，原 physical BC $2\cdot10^{-11}$、原 inner tol $2\cdot10^{-9}$、最多8次 outer 和最终 seam 请求全保持。不存在借内部延拓绕过原 outer 接受条件的路径。

## 6. 开销、来源及实际源码差异清单

这个方案只改善如何得到每个目标 DN 的初猜，不减少原 Newton 每轮所需的真实残差或全 flow Jacobian。中间 flags Jac=false 只省掉响应的 heightJetJacobian 等工作，不能声称取消 shooting 内的全变分计算。首个实际 DN 的已记录耗时约125秒；第二个失败 DN 的 iteration3 已约838秒，整轮原 prefix 约1195秒。多子步有成本，不能把32请求预算叫作廉价试验。

单个响应仍受原小于5MB上限约束；32个物理请求的响应包保守总量小于160MB，trace、stage diagnostics 和输入另计。当前两个闭包约0.27MB，不把这个样本大小当通用上界。运行仍需 root 原空间 guard，所有调用串行，只使用一套原 worker；计划本身没有启动它。

最小源码差异建议为：

| 新增项 | 作用 | 保持冻结的部分 |
| --- | --- | --- |
| 新 client adapter | 上述状态机、策略/journal、调用原 base.solve | 原 trial-client 的 wire/保存/缓存实现；原 worker/core/engine |
| 新 flat-coupled 选择 wrapper | 只把现有 active-client import 选择到 adapter | 原 coupled 方程、BC、outer 和 seam 实现 |
| 独立小策略与输入绑定 | 固定步长预算、bootstrap真包、策略SHA及新 I/O | 原物理 tail config 除五 I/O 路径；原 restart/自由参数/所有数值 flags |

新 adapter 使用原八源代码，但自身也影响运行。因此每个新实际包应明确保存**原八源加新 adapter 共九个真实源**（原 base client 不可从来源中删掉），新 wrapper 和策略文件再由新 launch/协调日志绑定。不能继续声称“原八源完全相同”的运行身份。旧 matched-cut 的121输入、旧审计器强绑定及旧结果保持历史身份；未来新运行必须有自己的严格输入与九源审查，不改旧记录绕门。

在现有 API 中可由 adapter 于构造完成、发送首个求解请求前，向原 base 实例的 `sources` 字典追加自身 SHA；原 base.solve 自动把该字典写入每个包。这个来源字典变更不修改原八个源文件，也不改变真实 wire 请求。新 wrapper/策略/全部传递依赖另外绑定，不能因为主包列九源就遗漏原 source-root 依赖。具体实现仍须审查，本文尚未创建它。

策略可以作为 record-prefix 对应的独立 sidecar，由新 adapter 读取并在每条外请求日志中绑定其 SHA；不把协调策略键 spread 到原物理 factory 参数中。每个内部包仍保持真实的 physical request/config/response，journal 单独关联外目标、$\tau$、原点成功包、实际包号和状态。最终原 `.calls`/record_prefix 仍定位最后目标包，所以原 seam 文件名规则继续有效。

## 7. 下一步范围

当前建议先让未参与本设计者完整审查这个状态机、原数组复制/last 更新证明和来源方案。若获准实施，可直接在新 stem 的原自由切口 coupled 调用中使用该 adapter；也可先对已关闭的真实 $H^0\to H^1$ 做一个有界单外请求核验。两者均必须真实达到目标和原 flags，不能以中间成功作完成。

本稿没有执行上述任一路径，没有修改36轮、原容差、.05保护或物理 g，也没有延长 Newton 的十档线搜索。若线段中某处正支路消失、保护限制住路径，或者工作预算不足，延拓仍可能停止；它不证明目标不可解。继续原自由切口 BVP、同 g N512 校正与完整几何/G5 认证的门均未改。

## 8. 可复核的已关闭来源

同 stem 的 `-diagnosis.json` 只保存本次两请求的标量差、闭包/trace/trials 身份及原响应字段集合；没有复制 height/state 大数组。同 stem 的 `-sources.json` 逐项绑定本稿、该诊断、原观察/输入绑定、所有直接核过的源码和已关闭运行材料。原 matched stem 的文件名及八源身份保持不变。`-observed-execution.json` 只记录这次只读元数据检查的真实工具结果，不冒充新 solver 运行。
