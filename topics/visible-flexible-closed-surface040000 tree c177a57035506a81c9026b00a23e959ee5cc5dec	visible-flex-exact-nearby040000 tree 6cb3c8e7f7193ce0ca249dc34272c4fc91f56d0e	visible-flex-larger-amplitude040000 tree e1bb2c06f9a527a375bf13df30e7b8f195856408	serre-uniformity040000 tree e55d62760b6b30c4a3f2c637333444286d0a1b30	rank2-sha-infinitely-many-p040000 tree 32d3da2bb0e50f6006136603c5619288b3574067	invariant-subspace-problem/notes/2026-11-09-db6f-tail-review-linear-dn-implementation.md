# 每请求线性 DN 延拓实现 v2：完整独立审查

审查者：`tail_theory`。状态：**有效 v2 的源码、闭输入身份及隔离协议审查 PASS**。本审查没有构造真实 port，没有运行 Node、moment root、RK、flow、DN、BVP 或优化，没有生成新的数学候选。本结论允许 root 按既有授权评估唯一已准备的 $H_0\to H_1$ pilot；它不预言该请求成功，也不支付 prefix 联解、无限尾或 README 的任何完成门。

作者是 `coupled_prefix`。审查者未参与这套实现的编写；审查中发现 v1 的完整 trial 分组缺口，作者另存 v2，旧文件与旧执行记录保持原字节。实现依据及先前方案独审见 `2026-11-09-db6f-prefix-matched-cut-linear-dn-continuation-plan-v2.md`、`2026-11-09-db6f-tail-review-linear-dn-plan.md`。本次重新逐段检查实际实现及原 client/worker/core 控制流，未将方案 PASS 代替实现审查。

## 1. 冻结身份和审查材料

有效入口为下列四个新文件。

| 文件 | SHA-256 |
|---|---|
| `scripts/db6f-prefix-tail-linear-continuation-client-v2.py` | `6d278d78e275df2e0e66db3eb0edb592321fecc22c1c229eacd53f5869166d15` |
| `scripts/db6f-prefix-flat-linear-continuation-coupled-v2.py` | `c7598d48d695570b9fb8fbd0959ca382ed16e246125e05ddba7f757b9198ae43` |
| `scripts/db6f-prefix-prepare-linear-dn-pilot-v2.py` | `91e3d9689daf9863ab575a9985c217f61f601b84ddd45cceaf1248d24f391062` |
| `scripts/db6f-prefix-test-linear-dn-protocol-v2.py` | `bf3d9aef7cde67bb86e5ff0e0291cf51030810f24d8c47f2b516747c00e31317` |

完整读过作者原实现稿、v2 勘误、四个实现文件、协议测试、纯准备器，以及原 trial-client、trial-worker、trial-core 和 coupled/flat-coupled 的相关完整控制路径。作者两份闭清单共 14+11 件在本轮重新逐文件核 hash；另核旧输入绑定和新 launch/policy 的全部 144/143 项。上述数字是各清单的条目数，不主张这些清单互不重复。

审查源账本为 `2026-11-09-db6f-tail-review-linear-dn-implementation-sources.json`，SHA-256 `d603e73b7a888c6b2315e5f77eddde08e3eeda7f37f23cc6e627fe81186dc56a`。有效 v2 作者闭清单的 SHA-256 为 `80dc8e419eee37a8b9e496b89a17682a951c164ee964494baac2f6990207c975`。原 v1 的 14 件仍与其 `f855b94c…` 清单相符，不能用 v2 的通过结论反向认可 v1 的缺口。

## 2. 原数学问题与新增控制层的边界

`Coordinator` 只决定原 port 的调用目标和调用次序；真正的 `WeightedTailPort` 仍通过原 client/worker/core 求解。同一外部请求的路径固定为

$$
H(\tau)=H_{\rm origin}+\operatorname{float}(\tau)
(H_{\rm goal}-H_{\rm origin}),\qquad 0\leq\tau\leq1.
$$

这里的 $H$ 已是物理 cut height，适配器没有再乘或除 $c^4$。$\tau$ 的控制网格以 `Fraction` 保存。到 $\tau=1$ 时显式使用 `goal.copy()`；中间浮点向量若已经等于目标，也必须进入原精确目标与 flags 的验收路径。不能以近似相等、`isclose` 或某一中间成功代替目标完成。

新 policy 不作为额外 factory 参数展开进原方程。有效配置保留 M15、N256、depth12、parts8、steps32、原每次 36 轮、尾容差 $2\times10^{-9}$、projection floor $0.05$、原十档 Newton 线搜以及固定背景 $g$。只改变五个 I/O 字段：`initialCheckpoint`、`traceFile`、`iterationCheckpointFile`、`trialDiagnosticFile`、`trialStatePrefix`。逐值带 JSON 类型的比较确认其它配置、source root 与运行堆参数没有暗改。

外部控制预算是最大步 $1/8$、最小步 $1/1024$、最多 32 次真实物理请求、最多 1024 次逻辑推进；失败、bootstrap 和最后验证都占真实请求预算。TRACK 预留最终验证的一个槽。这些是有界搜索规则，不是存在性或收敛定理。临时目标的改变只用于 warm 路径；最终返回的目标仍必须是调用者原先给定的 $H_{\rm goal}$。

## 3. 原 warm、last 与 postprocess 的真实语义

原 worker 对历史 states 的采用仍受自身 ratio 门保护。只有有限 ratio 严格处在 $(0.25,4)$ 时才走相应旧态缩放；否则仍可回到原 linear 初值。原 harmonic 条件和 `correctInitialBoundary` 机制都未改。因此本实现不承诺每个临时请求一定从上一成功 states 原样出发。

原 core 在进入 shooting 时又复制初值。worker 的 `last` 只在完整 DN 调用正常完成且 `converged=true` 后更新；正在写出的 progress/迭代 checkpoint 不等同于新的 last good。原 DN 即使请求 `jacobian=false,audit=false`，仍会在正常求解后的流程计算 cutRaw/cutJets；而 shooting 内部本来就使用每轮所需的 Jacobian。不能把 TRACK 两个 false 解释为只做一次便宜的流，或认为任何 root 错误必定来自初始评估。

这也是失败分类必须保守的原因：带有 history 的同名 momentum 异常可能发生于后处理。它不能因为字串看似熟悉而自动折半。最后 VALIDATE 阶段的任何失败均终止当前适配器实例，不继续搜索。

原 base client 在每个真实 wire 请求之前增加 `.calls`，包括失败请求；它只有在正常成功记录落盘后才更新其成功缓存。适配器维护 request 的复制、响应规范化摘要、实际 packet 身份和成功 call 号。自动重试之前检查 base 的旧成功 cache 没有被失败调用改写；正常返回又要求 GOOD 的 call 等于当前 `.calls`。因此失败后不能拿一个旧缓存冒充最新目标闭包。

## 4. v1 的实际缺口与 v2 的修复

审查者构造了两个仅在内存中的抽象反例，工具 `bcfc0a` 实际 exit 0：aggregate 失败的 `lastIteration=1`，但只保留 iteration1 的十行；以及正常 `converged=false` 而 trial 行为空。v1 都可能把它们分类成可缩小临时步长。问题是它验证了所有“读到的行”，却未验证较早组确实存在。这违反了已审方案中不完整诊断应停止的要求。

作者保留 v1，新增 `complete_trial_groups`，在分类器中要求完整顺序结构。AST 核对确认 client 除该 helper、失败分类器和两个 schema 名外与 v1 相同；selector 只改为 v2 adapter 文件名。原 Coordinator、数学调用、缓存/返回规则未因这个修复改变。

### 4.1 Aggregate 失败

先对每条行记录检查类型、索引、原 $2^{-k}$ 步长、有限 norm、接受/拒绝与实际下降关系，以及原错误白名单。再要求从 iteration0 到失败 iteration $i$ 的全部组按原追加顺序出现：每组 trial 索引从 0 连续起步，组内 baseNorm 相同；此前组唯一 accepted 是末行；最后一组恰为十行全部拒绝，并与失败包最后 norm 相符。游标必须消耗完全部记录。缺整组、缺单行、重复、乱序、额外行或未知错误都不能自动折半。

### 4.2 正常 nonconverged 返回为何需要 36 个完整接受组

原 core 的每轮顺序是：保存 full-Jacobian 基点及 progress；若该 norm 已过原容差则立即 break；否则计算方向并逐档试步；首个真正下降的试步被接受、写 `history[i].step` 并进入下一轮；十档均失败则抛 aggregate 异常。循环后若最后基点仍未过容差，会对最后接受的状态另做一次最终完整评估。

所以，在冻结的 36 轮预算下，正常 `converged=false` 不可能来自提前达到容差的 break，也不可能来自未接受步长的中间轮。它必定用满 36 轮且每轮都接受了一步。v2 据此要求 history 为 iteration0 到 35，以及全部 36 个完整接受组；每组 baseNorm 对应 history norm，末 accepted 的 step 对应 history step。

这里没有追加两条不正确的逐位等式：最终 residual 属于最后接受状态的完整复评，不必等于末 history 基点 norm；上一 state-only trialNorm 也不必逐位等于下一次 full-Jacobian baseNorm。实现未添加这些等式，抽象测试还特意使用不相等数值验证这个边界。

### 4.3 首次 progress 之前的窄异常类

只有请求 flags 均 false、准确三键失败包、`lastIteration` 和 `checkpoint` 均显式为 JSON null、当前 call 无 trial 行，并且错误是冻结原 momentum 白名单，才适用这条窄重试路径。配合原 36 轮控制流和来源绑定，这表明尚未到首个 progress；它不涵盖带 history 的同名后处理错误。所有其它协议异常、来源异常、未知错误及 VALIDATE 错误均终止。

## 5. 数据协议、真实源码身份与返回门

正常 response 要求原七键结构。`converged` 必须是 bool，residual 必须为有限非负数，flag 与原 residual/tol 判定相符。cutJets 要求原准确 17 键：14 个有限非 bool scalar 加三个长度 M 的数组；Jacobian 若请求则必须提供原 $(3M+2)M=705$ 个有限槽；audit 若请求则必须提供原八键有限报告。

checkpoint 是原六键结构。运行参数按带类型 canonical JSON 与实际 ready 参数核对；865×30 states、13 个严格递增 rawNode 索引、13×30 rawStates 以及从 states 精确抽取的对应关系均检查。history 的已有可选字段按原 schema 处理，没有要求未计算的 chartCondition 必须出现，也没有强迫 residual 等于最后 history norm。

`cutHeight` 的精确相等是**请求标签身份**。它不宣称数值求解后的 jets.height 已逐位等于目标，更不将一个数值残差小包当作严格精确解。原 matched 接口中的 binary64 roundtrip 间隙没有因此被抹除。

新 production adapter 把自己的真实文件/hash 作为第九个来源加入原八源列表；旧八源逐值保留。实际响应必须记录这一九源身份，不能仍冒用旧八源审计器。selector/preparer/policy 及全部传递输入另由 launch 清单绑定。运行中不读取旧 active amplitude03 的 trace 或覆写其 I/O。

### 5.1 缓存、日志与原子 last-good 引用

响应包必须实际存在并可完整读取；缺失、截断、过大、来源不符、flags/target 不符均是终止事件。原 base 保存 gzip 并非由本适配器变成事务性写入，所以包写入异常不能伪装成数值失败继续。

事件 journal 逐条 flush/fsync；last-good 引用以独立临时文件、fsync、`os.replace` 发布。引用指向已闭实际 packet，不是新图或解证书。任何验证、journal 或引用写入异常都锁住实例并阻止正常返回。当前 call 的串行 trial 记录从原诊断流抽取，v2 完整分组门检查其结构；不能把仍可能追加的整个日志文件当作一份永久不变的数学证书。

原 base.close 的 timeout/terminate 语义没有被伪装成已观察到 worker exit0。pilot 的实际 poll 可为 null，必须如实保留。未来真实工具退出、原 worker 退出和数学返回三个事实仍需分别观察；本源码审查不能替代 root 的实际执行记录。

## 6. Bootstrap、最终 flags 与 outer 接口

初始已成功 packet 只提供 warm，不预填成新的数学成功。若 bootstrap 目标不同，先按原 false/false 请求建立本实例真实 good；若相同则按调用需要处理 flags。中间 TRACK 使用 false/false；最终必须对 `goal.copy()` 满足调用者原要求。请求的 target Jacobian 必须来自目标上的原真 tangent，不是路径 secant 或对 $\tau$ 的导数；请求 audit 时同样执行原 audit 路径。

只有在同目标、同 flags 条件已由当前最新真实包满足时才允许缓存返回。若非终点目标和上一 good 在浮点中完全相同，允许有界逻辑推进，但不增加真实成功次数、不掩盖 `.calls`，也不跳过最终 flags 门。

selector 对未来完整 coupled 外层只替换客户端选择；原 nonlinear BC、free prefix parameter、原 outer 接受条件和最终 seam 行为不改。不过**本次准备的 launch 仅为一个 H1 外部请求，Jacobian=true、audit=false**；它没有启动完整 prefix outer，也不产生 final seam audit。即使该 pilot 以后成功，也仍然不能称完整 prefix 联解。

## 7. 真实闭输入、配置和输出隔离

独立检查器重新核了有效 launch 的 144 项和 policy 的 143 项文件绑定。有效 launch SHA-256 为 `5d4224ea9138bd6fc6f017c6aade288e003532fb45e77252d4d45c4fdc988cb5`；policy 为 `1feff0e39f7b9cb5030163c5d62f5c8becf714f23fa0cf46515aea54f3b874ea`。

bootstrap 来自原已闭 matched 第一个成功真实包；H1 逐值取自同一已闭 run 的第二个失败请求，而不是从其失败 states 猜测目标。原失败结论没有被改写：第二个请求在原局部搜索中失败，不证明 H1 没有正分支解，也没有被本适配器的准备工作变成成功。

新 stem 为 `2026-11-09-db6f-prefix-linear-dn-matched-h0-h1-pilot-v2-01`。五个配置 I/O 差异正是预定五键；其余 typed config、原 source root、Node heap 参数和目标 flags 相同。九个新运行路径或前缀均在该新 stem，未挪用原 matched 或 active03 的写入位置。纯准备器没有构造真正 port，也没有把成功的输入 packet 复制为新求解结果。

## 8. 独立实际执行与结果

以下均由本审查者实际观察工具结束；精确命令、输出身份和作用域保存在同名 observed JSON。作者的执行另列于作者闭清单，未混作本审查者执行。

| 工具 receipt | 实际 exit | 检查内容 | 结论 |
|---|---:|---|---|
| `dbcf83` | 0 | 原 v1 的 15 类纯协议测试 | 与原 3271B 报告逐字相同；未覆盖后来发现的缺组反例 |
| `bcfc0a` | 0 | 两个 v1 内存反例 | 确认缺完整组时可被错误分类，不产生候选包 |
| `bad5fb` | 0 | 原 v1 闭输入 metadata | 143/142 绑定及新路径通过；当时明确未批准 v1 pilot |
| `464ce0` | 0 | v2 的 21 类原协议独立重放 | 输出 4198B，SHA `5b4a683c…`，与作者逐字相同 |
| `20133a` | 0 | 新独立 checker | 352 个 malformed 抽象例全拒、三种完整抽象结构通过；144/143 绑定通过 |
| `befef2` | 0 | 两作者 publication 及附加来源重新核 hash | 14+11 件原文件和审查依赖保持同一身份 |

独立 checker 为 `scripts/db6f-tail-review-linear-dn-v2.py`，SHA-256 `870b8953753a179163752cde91f166812b56b1964fb91ba9d04566b73848e9a3`。结果 `2026-11-09-db6f-tail-review-linear-dn-v2-check.json` 的 SHA-256 为 `0ae529a9f8cdf5e43fa0fce64e0afcab25348f8b67282aad65534d81aa9c4d0c`。

352 例逐位置删除、重复、邻位交换、未知错误替换、整组删除及 history 对应破坏；它们全是内存中的抽象协议记录，不是虚构的未来正向 DN packet。三种通过的抽象结构只检验分类器控制语义。原测试还只读已闭第一真实包的 schema 兼容性。所有这些执行合计真实 port、Node、root、RK、flow、DN、BVP、新候选包均为 0。

## 9. 最终范围

有效 v2 已满足本次委托的完整源码审查、原数学门保持、失败回退的封闭分类、真实来源和新 I/O 隔离要求。未发现仍需修改的实现阻断项。v1 的缺口及其历史测试保留，不能再用于启动实际 pilot。

本结论不证明临时边值路径有解、不证明有限次数跟踪能到达 H1、不证明数值成功等于严格等距解，也不支付完整闭图、G5、曲率、reach 或强目标。以后实际运行若失败、日志不完整或基础设施中断，应按真实观测另立闭记录；若成功，也只先取得该明确目标与 flags 的原数值 DN 响应。完整 prefix/闭图仍需要其各自的新真实求解和独立证书。
