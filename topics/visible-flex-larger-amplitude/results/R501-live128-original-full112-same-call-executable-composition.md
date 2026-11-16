# R501：原 actual63 全112前缀到逐 H live128、原 FD/fullDN 的可执行组合

> 后续实际运行见[R502](R502-actual219-input-pin-failure-and-unstarted-live128-scope.md)：原219在输入准备阶段失败，科学步骤未起。本文保留发表时的条件实现命题；原版17047B / 04ee80d5…保在f0c78734历史，实际接受或拒绝不得由本条条件命题补出。

作者：ChatGPT / exact_refinement（AI 辅助研究）  
日期：2026-11-16

**可信度：已证明，限于本条明确的表示、来源和条件接口组合；新 request219 尚未执行。** 本文完成 [R493](R493-current-H-live128-response-projection-and-original-fullDN-interface.md) 所列真实调用接点，不把组件存在、编译成功、协议返回或绿色 job 标签称为数值收敛。实际计算结论预留 R502。

## 501.1 原有限问题和本次实际变化

本次入口采用原 `geometry_20261114_live_current576_full_dn.py` 的完整 actual63 路线。原源 SHA 为 `7ba3fd5f183a7772e8f4d5a7b23073610dece4fdd5ba8c1ccbf7d05052597502`。其原工作流已有 350 分钟 job、320 分钟 science 的结构，但没有据此产生本条所需的已完成父请求；本次不虚构旧 fullDN 成功或旧 live request 身份。

真正初始前缀是 actual63 保存的全453坐标 warm，原 gzip SHA 为 `6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a`；对应 status 解压后的**原字节** SHA 为 `8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46`。二者仍是明确未接受的原有限迭代。旧 actual91 的 failed73 尾状态仅作另一部分的初猜，不替代前缀，不成为完成的 native response，也不继承其 J 或域结论。

新入口真实执行如下组合：

1. 从实际 warm 的全部453坐标形成原 profile、物理 boundary 与真实 $H\in\mathbb R^{112}$。
2. 对每个实际未缓存的协议请求，重新执行原完整 withJ、十组实际数组导出和 R273，继而调用当前 H 的持久128 owner。
3. 当前 owner 真正满足原残差门且独立 replay 完成后，在其同一个实际 final state 上形成全 stage、boundary 和混合 endpoint J；请求 audit 时另执行完整原 audit。
4. 明确投影到原 binary64 协议，把正常返回对象送给未改正文的 TailClient.solve。
5. 原当前 H 的仿射 FD 真正执行；同一 Python client、同一 Node worker 和它已计算的当前响应交给原全112/full453 fullDN；最后的 fresh audit 按原控制流另请求。

这条路线使用原有限 Gauss/原 profile，不使用连续 C 十族、R456 mesh、R464 union 或216的18900+2700时钟。334个显式来源 pin 是保守闭包，其中历史实验入口只作来源，不因此执行六控制路径或另一算法。

## 501.2 三种维数不可混写

| 对象 | 完整维数 | 在本实现中的作用 |
|---|---:|---|
| 真实物理高度请求 H | 112 | 每次当前 boundary 的完整非均值偶频输入 |
| shooting 节点状态 | 577 × 224 | 原576段两组112 shooting变量；是 checkpoint/warm 状态 |
| 局部 RK 状态 | 226 | 全224 shooting分量与两条均值状态，供每个真实局部推进 |
| stage 敏感度 | 576段 × 224方向；局部226输出 | 全方向形成，不能把它叫577×224的导数表 |
| 物理 endpoint jets | 338 | height112、meanHeight、slope112、meanSlope、second112 |
| 请求的 endpoint J | 338 × 112 | 原合法混合导数合同；保留全部行与列 |
| 原 augmented prefix | 453 | 338物理行、112 core行和3 scalar controls |
| 原 affine FD | 2组 × 10方向 | 每方向3层、2个 Richardson 结果、2条收缩记录 |

两条均值行既进入返回 jets，也进入原接缝消费。本文没有从 shooting 的224维外形推断均值已经为零，也没有为了方便将完整局部226维降为224维。[S1–S6]

## 501.3 同调用来源不变量

记本 job 的未缓存协议调用为 $c$。令 $H_c$ 为 Node 真正解析的输入，$X_c^0$ 为本次原初猜策略实际选择的全节点状态。捕获器始终先调用原完整 evaluate(withJ=true)，即使它的初始 norm 已在原阈值下，也不凭早停跳过所需的 J。

每次调用使用独立 `call-0001` 等实际目录。source、request、H 原字节身份、初猜来源、参数、576段顺序、cut/far/scales、原 Jacobian 和 residual 全部在该目录形成。R273 新 system/QR view 只改变真实 capture/source/schema 接点；其数值体沿原3557/d5d，不省去原cut、576stage或far行。

同次 literal packet 与 physical packet 由原61e/824 writer 在同一个 $H_c,X_c^0$ 来源上产生。owner 每次从该 packet/factor 开始，不把旧call1的固定来源检查换名后继续使用。owner、handoff、final state、component input 和 assembler 逐项携带当前 call/run/source 和实际文件身份。路径可以是同一原件的合法别名；实际内容身份按 bytes/SHA 绑定，不能以不同路径名伪造不同科学来源。

**命题501.1。** 若 assembler 正常完成，其响应中 state、物理 jets、请求的 J 和 audit 均来自该实际 call 的已完成组件，不会由旧 actual91、旧 native61 或另一个 H 的完成响应补足。

**证明。** 新 call pipeline 只接收该目录的已完成 snapshot，并检查其 native_call、sequence 和 nonlinear_iteration。factor 返回和两个 packet 由该 snapshot 派生；owner 接收这些实际 descriptor。组件入口继续核原 owner/final-state/packet 绑定。assembler 先核 owner 原 final complete、原 tolerance 与 fresh replay，再核组件的完整维数/完成标志及同 state 绑定，最后才打开其 raw。任一输入缺失、错误或 partial 都不执行成功分支。响应文件在所有必需投影后才标 `response_ready_for_original_client=true`。因此正常分支不存在靠预期尺寸或旧哈希补数据的路径。证毕。

这只是条件来源命题；它不声称 owner 或组件必能在资源内返回，也不替代原有限残差、域、FD或fullDN门。

## 501.4 原128数学体、显式 scalar 出口与一次投影

新的 scalar qualifier 委托原 `geometry_20261115_native128_qualified_json_components_v2.py`，再对实际 a090 physical consumer 的已限定版本作四处唯一、计数明确的导出替换：

- endpoint 的13个协议 scalar 保存原 binary128 words；
- audit 的9个协议 scalar 保存原 binary128 words；
- 每份输出附准确 slot 顺序、bytes/SHA 与 schema；
- 原物理公式、混合 J、原 audit 查询及计算顺序不变。

这些额外写入发生在原值形成后。既有最终组件源不被覆盖；临时生成源记录完整实际身份。新来源不冒原 a090 或 ecf 的 SHA。

投影器只用整数算术选择 binary64 word。设有限 binary128 word 表示准确 dyadic 值 $x$，输出

$$
P_{64}(x)=\operatorname{RN}_{64}(x)
$$

为最近、平局取偶数的 binary64 值。正常数/subnormal 的指数、guard/sticky、进位和溢出分别处理；符号位保留，包括准确负零以及负非零舍入成负零。非有限输入或投影溢出仍触发实际非有限值错误，不钳制成有限值。残差和均值累计值若来自原 %Qa 文本，则先解析成准确有符号 dyadic，再走同一投影，不经十进制近似。[R493 §5–6；S2]

**命题501.2。** 对完整有限输入，assembler 输出的每个 binary64 标量或数组项正好是其指定实际128值的一次 RN-even 投影；Node 的转发不再改变该 JSON 表示。

**证明。** 原13/9 scalar raw、577×224 state、338 jets、请求的338×112 J 分别由固定 descriptor 和尺寸检查选定；投影器逐word完整读取，整数分支唯一选择所述舍入结果。Python JSON 写的是这些已选 binary64 值，其中负零输出为负零浮点记号。Node 直接转发 assembler 的 `response.json` 原文本，不执行 JSON.parse→JSON.stringify 的负零丢失往返。Python 原client随后读取的数值因此具有该选定 binary64表示。完整性或有限性错误在响应成功标志之前返回，不能得到成功的截断矩阵。证毕。

上述命题不是128程序的误差证书，不证明整个IEEE程序的严格导数，也不证明投影误差已小于任意 PDE 误差。实际128残差的原 word/hex 与投影后协议值分别保留。原 stage recorded-factor / mixed endpoint 的有限算术责任不被提高为准确隐式根导数。

## 501.5 零更新、原容差和实际组件

原 persistent owner 的32个方向/10档trial、solveTolerance $2\times10^{-9}$ 保持。新工程 wrapper 只完成当前call来源、真正绝对截止时间、same-call component链接及完整 summary 的语义消费。

原组件的紧凑摘要超限可返回70；如果其同job完整 `summary.json` 已真实形成，新的调用层从该原件读原 scientific_complete，不把“传输70”默认改为数学失败或数学成功。对于 owner 不完整、没有真实final state、未过原残差门或 replay未完成，依赖组件仍不开始，normal response不生成。

零个接受更新的情况仍要完成当前请求所需的实际stage/boundary/J/audit；不能因初始 norm小而借入旧导数。相反，组件全部完成也不独自设置原native/fullDN接受。normal response只表示原client可以按原规则消费这些真实字段。

noJ协议仍支持，但此实现可能为完整物理readout形成全stage与endpoint组件。metadata明确区分“形成了完整J”和“本次请求返回J”；没有把额外形成误报成另一种更便宜的算法。

## 501.6 原 TailClient 与完整 FD/fullDN 消费

新 client 是原1cdf的独立来源view。其 `solve` 正文保持，初始构造改为真实219 policy、明确初猜及新worker；ready/source和close生命周期相应接线。原相同H缓存语义保留。缓存命中不会被计成新未缓存call，也不声称另做一次withJ；不同H的新请求必须走上述整条真实链。

新worker从原36cf协议源构造独立运行view。它沿原warm/缩放/tangent选择，所用tangent map若存在，来自本次已完成128 stage的明确投影；失败只取消原可选预测器，不增加科学接受门。原378 wrapper在solve后覆盖首阶jets的64位路径不再接入新正常响应，否则会破坏同call128来源。

原7ba数学功能中的 profile、全部453坐标、boundary、`response_check` 和 fullDN调用参数保留。新入口第一次在真实actual63的H上取得正常响应，然后执行两组各10方向的原仿射FD，包括原3步长层、两个Richardson结果、$5\times10^{-5}$ 阈值和全部适用收缩判断。这项FD检查原仿射boundary实现；不把它冒成对真实非线性DN映射另做的差分检验。

同一client随后进入原fullDN，其全112非线性outer调用、原17档inner Newton、最多8轮outer、RMS $10^{-6}$、boundary $10^{-11}$、完整域检查和最后fresh audit均保留。最终物理cut audit保原R252 finite projection差额及两均值。原混合338行J合法性沿R491，不另设“全338必须解析”的前门。

**命题501.3。** 若 request219 最终声明原fullDN接受，则这个标志只能来自原fullDN实际返回；前置128组件、normal协议和FD的成功不能独自推出该标志。

**证明。** 新入口把实际返回对象交给原 `original.load_client` 接点，同时核这是同一Pythonclient及worker。原fullDN仍逐轮调用它真实solve，依原inner/actual boundary/RMS/finalaudit分支决定是否写接受结果。新入口仅收取该原return与status；必要reader从实际orchestration/fullDN文件读取，明确不从exit、组件或缺省字段合成success。任一中间失败、中断或未返只保原错误与未付范围。证毕。

有限fullDN接受仍不推出完整闭面、共同g、全t等距、reach/held或严格存在性。这些责任不属于本接口的数值预付款。

## 501.7 一条原时钟与实际进程所有权

本入口选择7ba原350分钟job/320分钟science，即同一个19200秒单调时钟。该钟在初始数据恢复之后、原规则同步及第一次native factory之前创建。每个H、fresh64/R273、packet、C++编译、owner/replay、四组件、协议投影、FD和fullDN共用同一绝对截止时间。不能把204的完整probe预算复制成每次call的新总钟。

factor cap为19200秒，只表示仍受全局剩余时间裁切；原owner6000/replay1200、stage8000、boundary600、endpoint600、audit1800及原开销处理沿实际剩余裁切。最后120秒留必要关闭/读回。所有cap均为上限，不保证18个可能的未缓存调用甚至第一call全部完成。

外层实际记录原rules session、science session与Node session的pid/pgid/sid、/proc start ticks、uid、run和namespace。原3b8 rules runner不改：显式从当前已读21bd/bff8 README字节形成BASELINES，保原每2700秒真实pull/rebase、变更停止及错误记录。其science子session与Node的独立session都需独立quiet；停止一个父group不被冒成所有后代已结束。

always reader先停止/观察已确认own的group，再扫描同namespace仍存进程；无法读清、身份不符或未知写者都会使quiet未证。它不会向只同名而身份不符的任意进程发信号，也不会在未证静止时并发读删科学目录。

## 501.8 必要读回、失败与清理

reader只生成一份不超过90000B的ASCII JSON。保实际call、原owner全部返回trial必要量和失败地址、完成/未访方向与组件范围、原FD全部层、fullDN/RMS/两mean、真实错误文字、source/input/raw文件身份。

原 Newton domain observer只输出每次残差评价及失败地址，没有alpha和接受boolean；reader保所有实际评价，但明确这些未导出的字段不能反推。RMS preflight原producer只保存每fraction前24个invalid point时，这个原地址范围也明确标记，不能说其余地址已经读到。

必要摘要超限时，完整被选对象只留Actions临时目录，返回实际bytes/SHA和transport70；不拆包、不字典编码大科学树、不截断后称成功。读回不完整或quiet未证即跳过清理。完整必要scope可以记录科学失败；此时若已quiet允许删除该own namespace，但不删除其他任务目录。

所有577×224、338×112、stage table、完整prefix field与factor只在同job临时供科学消费，不能从哈希恢复。实际清理结局必须由本次日志确认，本文不预填“已清”。

## 501.9 可复现范围与尚未付项

16个新source、完整request与workflow分别给出明确SHA；总接口列出所有文件。旧334 pin保守闭包中的原204/208祖先和actual63 producer链逐值保留，不混称全部实际执行。actual63 warm/status、原config、两ready和original78来源在Actions真正恢复原字节；actual91全artifact完整校验后仅提取合法初猜。

本地没有import科学源、AST/编译/执行新科学或运行fixture。Actions只做通常源码语法解析和原科学本身。新的workflow包括workflow_dispatch，正式发表后由主控官方dispatch并核实际head/run；本条没有自动派发或改Git ref。

未付范围是本条实际H的owner是否收敛、全组件是否返回、normal协议是否被原client接受、FD/fullDN是否通过、完整必要摘要能否装入90KB及实际清理结局。它们均留R502如实报告，不由本条源组合推定。

## 来源

- [R493](R493-current-H-live128-response-projection-and-original-fullDN-interface.md)：逐H来源、准确投影、原接口条件证明。
- [R491](R491-original-native-fullDN-gates-and-complete128-response-consumption.md)：原native/fullDN门与合法混合338行责任。
- [本次完整接口](../notes/2026-11-16-request219-live128-original-full112-interface.md)：16新source、334原/新pin、历史输入及CLI。
- [原完整消费者](../computations/geometry_20261114_full_dn_solve.py)，SHA c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162。
- [原client](../computations/exact_20261114_true_tail_client.py)，SHA 1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09。
- [原live入口](../computations/geometry_20261114_live_current576_full_dn.py)，SHA 7ba3fd5f183a7772e8f4d5a7b23073610dece4fdd5ba8c1ccbf7d05052597502。
- [S1：新真实call捕获](../computations/geometry_20261116_live128_current_call.mjs)，SHA c20af799243d35a045c9c5be7900fbd19bb8b391acb9efb26fe9c5265566cd21。
- [S2：准确投影](../computations/exact_20261116_binary128_live_response_projection.py)，SHA b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e。
- [S3：同call owner](../computations/geometry_20261116_live128_same_call_owner.py)，SHA 5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5。
- [S4：响应组装](../computations/geometry_20261116_live128_response_assembly.py)，SHA 08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb。
- [S5：真实原fullDN入口](../computations/geometry_20261116_live128_original_full_dn.py)，SHA 63bbbefcfda8ae5761be314da743afc5291ad1a83749cf6d554003d429f5508e。
- [S6：生命周期](../computations/geometry_20261116_live128_original_fullDN_owned_run.py)，SHA 64126513260ad2790b9a5561a6536f43a1eadfde3313b0f20e19236bcb8c13a7。
