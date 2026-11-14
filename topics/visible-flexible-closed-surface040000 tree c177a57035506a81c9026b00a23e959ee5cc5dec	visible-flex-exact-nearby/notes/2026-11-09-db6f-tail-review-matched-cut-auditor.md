# Matched-cut 首包与完整关闭审计器 v2：全文独立审查

审查者 /root/tail_theory，作者 /root/coupled_prefix，2026-11-09。

**PASS，绑定最终 v2。** 本人全文阅读 v1、v2、方法/勘误、原 client/worker、实际求解器的字段写出位置及原 Python coupled/launcher；找出一处会误拒真实最终结果的尺度维数错误，作者保留 v1 并另存单表达式修正版。本人只执行了同一真实缺观察记录负门及纯静态/哈希检查；没有执行首包或最终正分支，没有读取正在求解的首包、trace、trial 或 iteration，没有制造未来成功 fixture。

## 1. 冻结版本与实际执行

| 对象 | SHA256 |
| --- | --- |
| scripts/db6f-prefix-audit-matched-cut-closed.py（v1 历史） | af5349d6ea2d7f5f3331aee245bd04b605e0cf6d006d2fb25979fd2adf312b31 |
| scripts/db6f-prefix-audit-matched-cut-closed-v2.py（有效入口） | 00c048161cde786c830199d092b76e4a6027e081eab180e2fc449133515050a7 |
| prefix-matched-cut-closed-auditor-method.md | 58b6bb3265fdec134f2aadee204d7de16adb0ee52fef398cb11fa2911c3fbd71 |
| prefix-matched-cut-closed-auditor-v2.md | 994c6864ca88642a0f2159f7883765f985d7f63f15e4da5db7caae70ebf3e988 |
| v2-sources.json | 35efa713b19ae4a24ccec22584a9f2c9b0105fc02bef7e8c6af34a0ae1de6c95 |

笔记简称均使用 `notes/2026-11-09-db6f-` 前缀。实际数值 run 的唯一 stem 为 `prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01`；其冻结 input-bindings SHA 为 5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21。

独立 exact-diff/AST 检查 receipt **71cc97、exit0**，确认仅改 `vector(cp['central_correction_scales'], M)` 为 `M-1`，其它全部字节相同。原 WarpedBVP 确写 `pscale=np.maximum(q**np.arange(2,M+1),1e-9)`；其槽对应 $p_1,\ldots,p_{14}$，而 $p_0$ 另为支撑参数。因此 parameters 长15、scales 长14。冻结 warm 的真实 metadata 也相符。v1 没有产生正面认证；此修正不撤销任何已通过的数学结果，也不改变实际 solver。

本人独立运行：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-audit-matched-cut-closed-v2.py \
  --mode final --check-current-gate
```

实际 receipt **2b9873、exit_code=2**，返回 `NOT_READY`，原因是缺 root 的实际工具退出观察。auditor 写文件数0、solver数0、active_trace_read=false。这个负门先核冻结输入，再在 root_observation 的空路径处退出；未读任何本次活动求解产物。它不是一次数值求解失败。

## 2. 只读实现与输入身份

Ledger 消费真实文件字节，检查文件大小、读前后 stat、SHA 和已有的长度记录，并在输出前重哈希全部已消费文件。JSON 拒绝重复键和非有限常数；关键身份用 typed canonical JSON 比较，故布尔值不能冒充数字，缺键不能悄作相同参数。

只接受已固定的 stem / input-bindings SHA；`--prefix` 不是任意候选的入口。121 条绑定全部重哈希，实际配置、warm、准备报告和旧真成功 warm 都由这些固定输入追溯。未来 first/final 的数值产物则必须属于同一实际 run。

本审另写 `scripts/db6f-tail-review-matched-cut-auditor.py`，只读源码/AST、已关闭来源和旧 warm 小 metadata，不导入作者程序或 engine。它实际 receipt **936276、exit0**，重核121输入及13/7项两版本来源账本，去重 **131 个闭文件**全部通过。它同时核 source 关键写出语句与独立路径身份，不读取任何首正包或 future final 数据。

作者程序只在 final_coefficients 内导入 NumPy / scipy.interpolate.PPoly 以读取和评价已保存多项式；无原 flow/solver 模块导入。它不修改任何已有文件。正常输出使用新报告 `open('xb')`，不允许覆盖；`--check-current-gate` 只写标准输出。这里的“0写”专指该负门，独立审稿/检查报告当然由审查者另行新建。

## 3. 八源及 parameters 的实际继承链

root 特别要求本审从原源确认以下细节，而非只看某个包碰巧能通过；现全部核实。

**八个 HERE/name 正是 client 记录的实际文件。** client 先以自身 sibling 路径找到 `db6f-prefix-tail-trial-worker.mjs`，再用 `worker.with_name(name)` 逐文件记录八源 SHA。审计器的 HERE 是同一 scripts 目录，八个绝对路径都恰在121绑定中，真实字节哈希相同。不能将其它目录同名文件混作此身份。

**五个 I/O 是原 parameters 的真实字段。** `closing_recalibrated_tail.mjs` 先构造 `p={defaults,...input}`，assemble 的 parameters 从 `...p` 展开；weighted 包装再展开 `...tail.parameters`；shooting core 返回 parameters 又从 `...physical.parameters` 展开。显式覆写只涉及 modes/spacing/depth/physicalDepth/parts/steps/quadrature/linearMethod 等原有限离散字段，没有抹去五个 I/O。trial split 增加同一 rhsEvaluation 标识。worker 正常 checkpoint 使用 `sol.parameters`，失败恢复 checkpoint 使用同一实际 dn.tail.parameters。故审计器排除五 I/O 后比较全部解析参数，再将每个 I/O 与当前 cfg 核对，是实际数据链，不是它自己拼造的参数子集。

固定121输入又核 modes15、spacing3、depth12、p8、steps/auditSteps32、tail quadrature256、36轮、原 $2\cdot10^{-9}$ tolerance、guard .05 和 boundary correction。已有成功中间尾只提供初猜；它的未审计 flags 没有变成本次成功的证明。

## 4. first 模式只审首个实际 DN/J

唯一首包路径是本 run 的 `_tail_0001.json.gz`。期望请求由冻结 preparation 的 **actual_restart_request_height** 给出，精确 typed 比较完整 height/Jacobian/audit，不能用历史63/64请求标签代替那约 $10^{-19}$ 的实际重启差。请求必须 jacobian=true、audit=false。

正常响应按原七字段 schema 检查，converged 是 bool 且为真，实际 residual 有限并严格小于原 tolerance。严格不等号来自 core 的 `converged:last.norm<tolerance`，不是新加容差。705 项 heightJetJacobian 对应 $(3M+2)M$，17项 jets 包含14个标量和3个15向量；非有限值和 bool 不作数值接受。

checkpoint 全六字段核对实际参数、请求高度、865×30有限 states、rawNode 与13×30 rawStates。原 subdivision 对每个9段 raw cell 分8份，12 raw cells 共864 stage，故节点865，rawNode 为 $0,72,\ldots,864$。这与 frozen native 定义一致，不混用 physicalDepth 和 stage depth。

历史每行的 iteration/norm/minA/minD 来源于 core 的真实带 Jacobian 基点评价。其收敛判断发生在 correction 之前，所以已收敛末行合法地没有 chartCondition，也没有 step。只有算过 correction 才写 chartCondition、只有线搜接受才写 step；审计器对缺席字段不索取伪造值。原轮数耗尽后还可进行额外最终评价，所以历史末 norm 不必等于最终 residual；程序正确没有强加此等式。

原失败响应保留 failed / lastIteration / checkpoint 的真实身份，null 不会补成不存在的 residual 或 Jacobian。该状态被分类为原数值成功尚未建立，不会被错误归为正面首包。

first 成功只报告 `PASS_FIRST_ACTUAL_DN_J_ONLY`，prefix_coupled_success=false，不需要工具退出，也不推断外层过程成功。它既不读取 trace，也不把已关闭首包等同整个 run 已关闭。

## 5. final 模式的真实退出链

final 首先要求显式 root 观察记录：observer=/root、status=observed-process-completed、真实 session_id=5817、非空 tool_receipt、非 bool 整数 actual_exit_code 及同一 stem。guard 的 child 记录不能代替这层证据；原 Node worker 没有独立保存的退出字段，程序没有发明一个新门。

root 观察的 files 必须绑定实际 reproduction、summary、最终 CP、最终 seam 包和全部系数块。所有路径限制在 repo 内；`/dev/shm` 的备用观察不作为输入。root 可另外绑定 repo 内 primary guard 观察，但它不改变 root 实际工具观察的必要性。

随后再核 original reproduction 的静态内容逐字段等于原121输入绑定、原 bound launcher SHA 和不变的 command；其实际 Python child exit 也须为0。root tool 非零与原 child 非零分别报告执行未成功，不推断数学无解。

原 coupled main 可捕获异常并 exit0；因此程序另外要求 summary 的 solver_success/error、reproduction 的 mathematical_success/error 自洽。原源会在最终 seam 前先写 CP，所以单有 CP 或 solver_success=true 也不够。完整成功必须实际 summary、最后真实 BC、最后真实 seam 同时齐全。对于失败/缺文件，程序不会为了满足成功 schema 生成替代数据。

根观察的真实性仍来自 root 的实际 tool receipt，而非这个只读程序自行发现进程状态；本审也没有执行未来正分支或补写任何 root 观察。

## 6. 原 outer BVP 门及最终 PPoly 身份

最终 CP/summary 除其保存协议中已知的 mesh/chunks/array_format 和分别记录的 seconds 外逐字段相同。原 collocation success 与 max RMS residual、固定 prefix options、同一 frozen profile/chart/cut/gauge/warp/meridian 均核对。自由 $p$、support 振幅和 adaptive mesh 不要求等于初猜；scales 维数现按原 $M-1$ 修正。

actual_outer_checks 的所有 inner_success=true 是成功路径的原控制流结果：`solve_with_actual_tail` 一旦 inner 失败，立即 `return sol,history`，之后不可能又产生 sol.success=true 的完整 run。最后 actual_boundary_residual≤原 $10^{-8}$、尾 residual<原 $2\cdot10^{-9}$，均来自原已审源。审计器不重算 BVP，也没有用自己另造的 residual 替换原接受门。

最后 outer 行的 tail_calls 指向原实际 DN/J 包，该包的请求与自己的 checkpoint.cutHeight 相同，residual 与该行同值。原保存没有另存该历史 inner endpoint 全节点，所以这里只能依靠原已审调用顺序和绑定数据证明其来源；没有冒称从最终 PPoly 重新构造历史 BC。

随后读取本 run 的全部最终 gzip NumPy float64 系数块，核 SHA/长度、6×(nodes−1)×state-block、连续覆盖0..45、全有限及完整递增物理 mesh。仅用保存 PPoly 在 L 求值，按原规范化 $H=-q_gY_Z(L)$ 得实际 final seam 请求；这个请求可能与 earlier inner-node H 有舍入差，程序没有强求两者相同。

final seam 包必须晚于最后 outer call，jacobian=true、audit=true，八项实际源 audit 有限，jets/converged/residual 与 CP 的 seam 字段逐值同。原 audit 请求绕过 cache。原 seam 角样本是 $\max(512,64M)=960$，prefix audit1024，tail auditSteps32，三者不混称一个分辨率。

mean/nonmean 一二 jet mismatch、cut metric/C1 metric、prefix sampled metric、tail source actualMetric 等均只记录，不新设 $2\cdot10^{-9}$ 的 second-jet 或 sampled-metric接受门。程序也不把这些采样字段称为连续 whole 证书。

## 7. 结论与实际范围

有效 v2 可以用于 root 对已关闭首包的实际正分支检查，并在真正完成及 root 实际观察齐备之后用于 final 模式。**本审结论是实现和原接受条件的审查通过，不是两个正分支已运行通过。** 两个实际正分支由 root 在对应真实数据齐备后另行执行并记录退出。

本人的静态检查 JSON 为 `notes/2026-11-09-db6f-tail-review-matched-cut-auditor-check.json`，SHA256 **668039b7c1ead7a246fdf401f33b098042ed33ca2e6a0911bb0f92c3ccae5001**；实际负门 receipt 和单表达式修订历史另存观察记录。完整关闭 PASS 的含义仍仅是这份同 g 有限 M15/N256 原联解完成；它不支付 N512 真校正、实际 XYZ/公共 C²表示、连续误差/曲率/reach、独立端到端复算或 README 总完成。
