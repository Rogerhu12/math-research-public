# R593 — 同一全局时钟内的 native owner 资源窗口与既有跨 H 初猜复用

作者：OpenAI ChatGPT（AI 协作者）  
日期：2026-11-16（UTC）

**可信度：已证明（限本文列出的完整源码、整数资源参数、同 job 绝对时钟和原有限程序合同）。** 本文证明一个明确资源分配变化的实际作用范围，并交付可执行的来源组件；不报告新科学运行结果。actual225 的已完成与未返范围属于 **启发式/数值证据**，仅依已经发表的 R528 引述，不在本条重新运行、恢复旧 raw 或作未返残差推断。

## 593.1 具体问题与本次唯一科学资源变化

actual225 原 R528 已明确区分局部 owner 超时与整个 job 时钟耗尽：原 owner 上限 6000 秒，整个科学钟 19200 秒；只形成一个当前真实 H 的 call，接受了一次完整试步，下一试步只完成 534/576 stages、119840/129248 行，未返回完整 norm。外层原 elapsed=6982.009654177 秒，外层 resource_stop=null。原 R528 正文 28538 B，SHA256 为 8ab4897ac61d96388db618b4639036d3088883848ec33339f10251504ef14921。该实际证据支持检查局部资源政策；它不证明下一试步会下降，也不证明提高上限后整链会完成。

本次独立后继沿已刊 R589 的完整原 63 prefix、原 78 数学源与原 91 初始尾状态来源，维持 R573 的当前 owner 算术、同对象 projected64 线性模型和原 full112/FD/fullDN 调用。唯一被改动的原资源值是：

| 完整原 JSON 地址 | 原值 | 本次值 |
|---|---:|---:|
| /live_call_resources/owner/owner_seconds_cap | 6000 | 12000 |

以下值及其类型全部保持原样：全局 science19200 秒，workflow science step320 分钟、job350 分钟，最终读回/清理 reserve120 秒，replay reserve1200 秒，stage science cap8000 秒，boundary与endpoint各600 秒，独立 audit1800 秒，factor cap19200 秒，threads4、原 R273 workers2、原 factor bytes、原磁盘门、全部原 numerical tolerances、32 个方向/10 档试步、完整 112/224/226/576/577 责任。

本条不采用 request242 的 actual98 prefix 或三个新参数初猜，不修改已经运行的 225、242、246 或任何历史源码。原 6000 上限不是数学容差；它在真正执行入口的资源参数中被显式改为 12000，不能写成“所有预算不变”。

## 593.2 原初猜路径已经跨 H 复用

### 593.2.1 实际原 worker

当前 R573 worker 为 geometry_20261116_live128_synthesis_product_projected_worker.mjs，8327 B，SHA256 ecad08d60e9bcf668e2c5c82771627cae2c7160f806b8f2573e90dacb898f021。它逐字绑定并透明组合原 78718-prefix-tail-tangent-fourier-worker.mjs，12294 B，SHA256 36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a。

原 worker 在单次启动时设置 last=live128.initialSeed()。旧 actual91 的完整状态仅进入这一初猜槽，并明确 converged=false、initial_guess_only=true，不导入旧响应缓存、旧 predictor、旧 J 或已接受标记。

对每个新的真实 H，原选择顺序是：

1. 若当前 tangentPredictor 存在，先调用它的 predict(H)；失败只进入原 fallback。
2. 若尚未得到预测且 last 存在，检查首 height 分量的实际幅值比。仅有限且严格在 (0.25,4) 内才调用原 geometricAmplitudeWarm。
3. 对该非 tangent 初猜，若原 correctInitialBoundary 没有关闭，则形成当前 Dirichlet 差，再加原完整 finite linear initial(delta)。
4. 若仍没有 initial，current_call 使用原 dn.tail.initial(target)。
5. 新响应真正 converged 后，last=sol；原可选完整 tangentPredictor 从这次 sol 的所有 stage maps 重新形成。

因此“每个 H 都重新使用旧91状态”不是这条实际源码的行为。把已经存在的 last/predictor 复用重新命名成修复不成立，本条也没有这样做。

原 tangent helper 4250 B，SHA256 8d39830939a52fc40f7de06cf5a2a9de9959f94058594051a7989b8b40744459；原幅值 warm helper 3416 B，SHA256 61c401abf66ca792f1c085f6a4b5b5911a62c3f966adb2dc11bd911b196148af。它们都只形成初猜，不代替当前 residual、root、positivity 或 acceptance。新的资源入口不修改任何一个初猜分支。

### 593.2.2 当前 128 状态、RN64 协议与新 H

当前 call 文件 geometry_20261116_live128_synthesis_product_projected_current_call.mjs，45476 B，SHA256 cf59d20d7fbd315b5a4250f2e691c10292030805c79430a4fa71e1755a98f0c8，在其 solve 中实际使用 opts.initial 或原 cold initial，并要求全 577×224 状态。随后为本 H 重新进行原完整 withJ、R273、literal/physical packets、128 owner 与完整必要后置消费者。

返回的 sol.states 取本次 response.checkpoint.states。这里是明确 RN64 协议中的完整投影状态，不声称跨 H 原封传递 binary128 内部 raw 文件。原 policy 的 retain_optional_tangent_predictor=True；可选 maps 必须为全 576 份 224×224 finite 数组才能传回，缺项不能以成功子集建立预测器。失败/奇异保持原 warm fallback。

当前 Python client geometry_20261116_live128_synthesis_product_projected_tail_client.py，40476 B，SHA256 3c35e7a802abdfe4857b59f6335e515207b67b312a1a08c07ff7e39ddd98e83f，保留同一 H、未要求 audit 且所需 J 已实际返回时的原缓存规则；audit=True 绕过这一缓存。新 H 从不因来源身份相同而拿旧 response 代替真实调用。

## 593.3 必须区分的四个时钟层

令 $T$ 是外层原 job-deadline.json 的 absolute_monotonic_deadline_ns，$t$ 是当前 monotonic 时刻；最终读回/清理 reserve 为 $r=120$ 秒。各角色登记并检查的科学截止均受同一固定时刻 $T-r$ 约束，它不会因 H、方向、trial、replay 或后置组件改变。这里没有声称进程在一个指定纳秒同步静止：原 drive_owner 的10秒退出等待、子进程终止/回收等待与外层 quiet 均保留并实际记录；它们不是新求解预算，未证 quiet 时仍不得读取活动科学对象或删除 raw。

### 593.3.1 外层全局时钟

R589 runner geometry_20261116_live128_named_necessary_owned_run.py，39330 B，SHA256 457a1ca8f575f2192664b0e5583b0bb3672d3b4dce4c6d56ec0e17844dc6b3a6，在 run() 只允许不存在的 deadline 文件，写入 started+19200s。原输入恢复在该科学钟开始前；规则 runner、当前 native、FD、fullDN 及所有后继实际科学均计入这一个时钟。

外层每0.25秒检查原截止时间、原磁盘 reserve 与实际信号。达到截止后沿原已登记 pid/startticks/pgid/sid 的作用域停止和 quiet；它没有因某个 inner cap 提高而失效。workflow 的320分钟 step 与350分钟 job 是另两层原上界，不被本条延长。

### 593.3.2 owner 的局部请求、全局裁剪与独立 replay

实际当前 owner 为 geometry_20261116_live128_synthesis_product_projected_same_call_owner.py，26666 B，SHA256 2af373696034e49f61e6dcc49707e668ed60d600b5a4f9dbf0d71d85cd24ad17。它完整保留原 persistent owner 程序 geometry_20261115_native_persistent128.py，43371 B，SHA256 767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322；原工程组合底本为 geometry_20261116_native_simd_stats_qualified_final128_same_job.py，38408 B，SHA256 8855ef79037bf552f44bd926e92ff5b2874fa17e8e35e1773c6344b71fd2c37c。

在实际 owner 分配时，源码计算

$R=\max(0,\lfloor(T-t)/10^9\rfloor-r)$。

若本 call 真正请求 audit，$a=1800+345=2145$；否则 $a=0$。当前请求上限记为 $c$，则

$B(c)=\min(c,\max(0,R-a-330))$，

$P(c)=\min(1200,\max(0,B(c)-301))$。

B 是实际 owner 秒数，P 是实际 replay reserve。原资源起步条件 B≥600、P≥60 保留；它只是原有限程序能启动的资源边界，未改为数学接受条件。当前 owner guard 本来允许 600≤c≤20000，所以 12000 在既有完整参数域中。

随后形成真实 owner 绝对截止 D，取原全局截止减原 reserve/audit 与当前 B 秒窗口的较小者；原 owner main 的 until 又取其自身 started+B 与该 D 的较小者。因此源码预处理、编译以及原 owner 的所有工作都受真实 D 限制，不因进入 inner main 重开另一完整 B 秒。

原 persistent owner 的顺序是：

- 编译本次实际完整 owner；
- solve_until=until−P；
- 当前 128 nonlinear 求解/完整 QR/所有实际 trial 共用 solve_until；
- 若真实 final state/residual 可用，独立 fresh replay 只取得 until−当前时刻的实际剩余；
- 后续 completeness、原容差与独立 replay 责任照原消费者判断。

因此在全局余量充分且 P=1200 时，6000 对应的 nonlinear+编译局部上界为4800秒；12000对应10800秒。这里是可用窗口的条件上界，不是预测实际耗时、迭代次数或残差。若原全局余量更小，B 会被相同 $R-a-330$ 裁剪，甚至新旧 B 完全相同；本条不把 requested12000 当 actual12000。

### 593.3.3 8000 秒 stage 模型是后继阶段

当前 pipeline 为 geometry_20261116_live128_synthesis_product_projected_call_pipeline.py，43286 B，SHA256 1ad21f183fb98e859086d96048063a25aaa749803d68bfa67801a4df665ab666。它先实际运行 owner 与 replay，验证原 final.complete、below_original_tolerance、independent_fresh_replay_complete，再读取同 call 的完整 final-state.f128。

R573/R534 已将旧128 post-stage如实标为 deferred；然后当前 pipeline 才开始当前同 DN 的 projected64 stage library。该阶段不是 owner 的共同更早 min(6000,8000)：

$S=\min(8000,\max(0,\lfloor R_{\rm after\ owner}\rfloor-a-345))$。

它独立写入同 job 的真实 phase window，projection、全576 stage×224方向的原 flowStateWithJacobian、exact model lift 共用这一阶段 cap。独立 owned guard 和每阶段原 resource callback 继续检查真实 window/全局钟。

stage library geometry_20261116_live128_same_dn_projected_stages.mjs，32316 B，SHA256 2279a605df5ee41c5400c658018722fd52e6add40ee35ff38dbca1a31b2bb76a；binding geometry_20261116_live128_projected_stage_binding.py，25000 B，SHA256 fab3790936e6516bd39f445a2fc8384196cb1479405a10588f9007d821751cbf。本条不修改它们的求值、回调、输出维度或错误处理。

### 593.3.4 边界、端点、audit、FD 与 fullDN

后置原 science caps 是 boundary600、endpoint600、audit1800；各自编译/关闭 overhead 依原代码为720、345、345。非audit组件在实际请求audit时仍预留2145秒；每次启动都用实际 remaining 做 min，实际余量小于1秒就记录该真实未启动责任。audit=False 的普通 call 不被新增 audit 门；最终 fresh audit 的原请求/同 H 门保持原样。

stage 的失败不被伪装成可用边界输入。当前 pipeline 保留“实际 model failure 不压掉仍可负担的原独立 audit”分支；各组件的 requested、attempted、scientific_complete、原错误、真实 input identity 继续分开。

当前 fullDN 接点 geometry_20261116_live128_synthesis_product_projected_original_full_dn.py，46439 B，SHA256 721aaa94d4bd70fed644aed0ee62e0d19ba526aadd1e6793645636a90f445b63，保持完整原 warm-H anchor→原 affine boundary FD→原完整 fullDN→最终同 H fresh audit。最多18个 uncached protocol calls 是原 outer-iterations8 给出的控制流上界，不是每 call 保证独享12000秒。原 same-H cache可减少实际次数，但不重开全局钟。

## 593.4 资源变化的有限程序结论

**命题1（局部预算单调，原全局硬上界不变）。** 在相同实际分配时刻、相同 T、原 r/a/330 与请求标志下，令 c从6000改为12000，则 B不减；当 B足以保持P=1200时，原 solve_until 获得相应较长局部上界。无论B/P如何裁剪，所有 owner/replay/后继的已登记科学deadline仍受同一 T−r；原检查粒度、终止/回收语义与外层 watchdog也不变。

证明直接来自 min/max 的单调性与上述真实源码绝对截止取较小值。工程调用、源准备、编译的实际耗时仍会消耗余量；它们不是额外无时限区间。命题不声称“新任务包含旧任务每一时刻的轨迹”，因为资源停止位置、真实机器调度和后续可用时间会变化。

**命题2（原数值接受责任不减）。** 本条不替换任何 R573 scientific source，不改变当前 H 输入、初猜分支、finite root 分支、32×10 试步、原严格 norm下降规则、两mean、全576×224与338×112责任、原2e−9 native容差、完整原FD门、prefix1e−6 RMS与1e−11 boundary、最终audit。于是任何在新入口中声明完整 native/fullDN 的结果仍须经过这些同一原消费者；较长预算只使更多原程序工作有机会完成。

本命题不把 R573 projected64 model 变成 binary128准确导数，也不新增模型精度对拍门。原 owner128值与独立 replay仍是原权威数值对象，原混合338响应合同保持。

**命题3（没有承诺全链时间）。** 增大某个 owner局部上限可能减少后续stage、FD或其他call的实际余量。原19200总钟没有变大；不能据 B_new≥B_old 推出最终残差下降、更多完整call、完整FD或fullDN必成。所有未开始、未完成和截止错误按原地址/范围回传。

## 593.5 实际可执行来源组件

本条的 source-only generator 实际调用原 R589 prepare 一次，在同一真实 computations/HERE 中形成原451来源；然后生成仅两个独立元数据视图：当前248 owned runtime 与 necessary reader。旧451所有pin逐值保留，增加一个公开generator与两个生成view，得到

$454=363\ {\rm public}+91\ {\rm generated}$。

原R573 fullDN entry、client、worker、current-call、pipeline、owner、compiler adapters、全部数学库没有新视图，全部保持原字节。源码生成不创建科学钟、不导入科学模块、不执行数值函数。

当前正式外层小request显式绑定原R589完整98952B request；它不是删掉大request字段的替代摘要。Actions在临时source-preparation目录深复制完整原JSON对象，加入真实新来源/当前namespace/request号，并只更改上述一个完整资源地址。所有原输入、lanes、runtime、resources、arithmetic、retention、科学合同和scientific_entry的完整对象保持类型和值。把该cap还原为6000后，整个live_call_resources必须与原对象相同；这属于真实来源/参数绑定，不是新增科学评价或接受门。

真实当前request的完整 bytes/SHA写入来源receipt和 GITHUB_ENV；后续prepare/run/necessary/cleanup都消费这一实际临时request及其SHA。原checkout中的246request不改，旧R589/R573 request号只作来源祖先，不冒本次248实际run。

两个新view：
- owned runtime只改本次request/schema/namespace/来源标识；原source/input恢复、rules、clock、science command、quiet与cleanup实现完整保留。
- necessary reader在原选择范围之外，加回原owner已经实际写出的完整actual_resource_allocation，并返回本次完整resource strategy/请求caps。原actual stage window、post组件分配、错误、未返和独立audit责任已由原selector返回，本条不删改这些成员。

## 593.6 读回、生命周期与仍未付边界

原 R589 完整 source-only necessary 与 R588具名RootStats/来源共享关系保留。当前 source scope与science scope各为一份语义独立的完整body，上限仍90000B。任何一个body超限仍明确70/不完整，既不拆包、不截断、不提高门，也不由预估宣称一定能运输。

本次新增字段存在于真实原owner-call-procedure时才返回；owner尚未启动时不捏造分配或默认actual12000。完整实际argv、requested cap、实际裁剪、剩余全局钟和原stage/post window有各自来源对象。原scope未返、源准备失败或读回失败都维持原明确失败/未付状态。

所有科学raw只留本job临时namespace。只有当前source必要scope完成、当前science必要scope完成、同源ownership和原真实pid/startticks/pgid/sid作用域quiet都成立，才沿原cleanup删除唯一namespace。真实own或suspected-own不可读仍阻止读/删；无权将外部同uid进程泛当本任务或普遍忽略PermissionError。source准备/数值成功都不能单独授权清理。

本条完成的是：既有跨H初猜复用的真实源码结论、局部owner/replay与全部后继时钟的完整分责、一个有实际caller的明确资源策略和必要读回范围。它不支付任何新数值native/FD/fullDN成功，不从已删除225 raw恢复状态，不把242/246未返结果当作新父。完整request248入口在R594登记；只有未来实际248官方终态才属于预留R595。

## 593.7 完整来源与发表范围

R589正式来源为 f70acbf1886f0f363c3c1d6b60760438f59e545c。原完整request98952B/SHA256 5c48bf2add2def97a6f1d86dc85d6159822e035ce50d61ca42e2179dc3a924b0，原generator26794B/80e74595d24b0aa8d1de2a95ec77cfe0d37e25288d36f277718c66149edbed0a，原plan20112B/e615b290d30f00867cb106906548491b84b7a02e7ba3f260a96cc261b9e352a9。

本条新generator26239B/9f852d3576372d25712f5276771dc9ac51fe1a97c4b8fdc700fd470d5a2ee5ee；完整双view plan10168B/4d7cee7c4d51c5415a5e22a10f3e21b6f00ab045a84260a484299b7426417229。两view的全部literal patch与baseline/output身份在plan正文，整份作者源与完整差异供交接；可再生展开源和diff不入主树。

本文仅执行源文本阅读、确定字面组合、元数据哈希与纸面证明；没有本地科学求值、导入、AST、编译、测试、fixture或新增独立审计。未来Actions的原source语法和数值消费者照原流程真正运行。
