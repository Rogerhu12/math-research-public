# R603：request248 原钟内接真实 R602 输入支撑乘积、完整当前 DN 与 request250

**可信度：已证明（限本文逐源组合、可重建文字变换及所列条件命题）；request250 的 source-only 准备、实际求解、模型、必要读回与数值接受尚未执行。**

作者：ChatGPT（AI）。日期：2026-11-16 UTC。本条是完整组件与执行入口的来源结论。实际 request250 的唯一终态结论预留 **R607**，此处不预填 run、job、收敛、速度或接受字段。本文不增加数值门、独立 fixture、shadow comparison 或额外科学运行。

## 1. 唯一实际父合同与改动范围

父入口选已刊 **R594 / request248**，固定主线
`b38a46a6d0f34f250cff6d13c64ffafa65931ef8`。其真实 R593 generator 先完整生成原 R589 / R573 链，再产生 owner 12000 秒、总钟 19200 秒的实际派生请求。新 generator 在本 job **调用这条原 R593 prepare 恰一次**，读取它真实返回的 current-request248.json 及完整身份，再派生本 job 的 current-request250.json。旧实际 run 的结果不被读取为新运行结果。

R602 已刊于 `93e41c94d276b57e7f56c140cce2ecc0f5bb50dd`；其 5625 字节 factory 和已刊 R523 的 6246 字节乘积 helper 原字使用。本入口只将 factory 接到实际 worker 原 Fourier-root 选择位置，并为当前 source / snapshot / QR / pipeline / client / fullDN / lifecycle / reader 更新必要身份。原 request244 不是父合同，R583 不在当前选择链中。

**保留的数学对象**是原 Fourier-product local J、原 717ac integrationGrid / RK / cusp 调度、全 576 个 shooting cell、全 226×224 局部方向结果、两 mean、原 R273 完整方向、当前 persistent128 owner / fresh replay、原 R532 完整 projected64 model、准确 lift、原 boundary / mixed338×112 / endpoint / independent audit，以及原 full112 FD / fullDN。R466 的 finite-root-trace 算术没有被借来替换当前 local J。原完成 RootEval、Cholesky、多 RHS 已有共享仍只是祖先事实，不能计作本次新收益。

本次仅把每个真实 field 调用中的完整 A*T 乘积交给 R602 所声明的 R523 actual-input-support 算法。用户输入、参数、原 accepted/failed 历史输入的作用、所有阈值及各原门均不变。统计和文件来源核对不构成新的数值接受条件。

## 2. 正式发布件、生成件和完整源码闭包

本条发布下表四个执行/元数据件与本文。生成源的展开全文只在真实公开 Actions 的 computations 中形成；不再把九份展开源或可再生 raw 保存到主树。

| 角色 | 路径（本题相对；workflow 为仓库相对） | 字节 | SHA256 |
|---|---|---:|---|
| generator | `root_20261116_live128_input_support_source_views.py` | 29284 | `ae2167c351f728089fdd308adbb8acbed6c6318ac28a99a264e9384ae73c7426` |
| plan | `notes/r603-current-DN-input-support-complete-source-plan.json` | 37436 | `a5ec7151e5953989bc486250f2697e5e8920babf51cc4adafb7e3ba539e212ac` |
| outer | `computations/public-live128-current-DN-input-support-composition-request.json` | 12474 | `160492decfaeef22c37e391f8001ed11105b6c988723ab32b056bc6e3283877c` |
| workflow | `.github/workflows/visible-larger-live128-current-DN-input-support-full112.yml` | 25450 | `5536d828c9a7b5a730ce66bf5b275a40f3a5b08be21f96241419a4ad21444bb7` |

两件直接使用的公开数学来源：

- `geometry_20261116_current_DN_input_support_fourier_product_flow.mjs`：5625 字节，SHA256 `f37bee075251957649c9ee5dc25582fac5c17fc3d3b804219cb537abf35f24f0`。
- `geometry_20261116_finite_trace_actual_input_support_linear.mjs`：6246 字节，SHA256 `e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3`。

实际集合是 **466 = 366 public + 100 generated**：原 248 的 454 = 363 + 91 全部逐名逐 SHA 保留，新增两个公开组件与本 generator，共三个 public；另增九个独立新名视图。不是删旧 pin 后改标签，也不是把原 91 个生成源误认成 Git 已存文件。原 R593 prepare 真生成全部祖先，再由本 generator 在同一真实目录写九个新文件。

| 新角色 | 实际生成 basename | 字节 | SHA256 | 顺序 literal 数 |
|---|---|---:|---|---:|
| system | `exact_20261116_live128_input_support_current576_system.py` | 29109 | `d16c37c7732ab9b2b9b7ba2eb5f1203bc9d95617e35171ceacce4d6ec36ea338` | 3 |
| qr | `exact_20261116_live128_input_support_current576_chain_qr.py` | 21844 | `1d880f96a979dd9d60e17c8c4e3001f7dd143a8393324fe34e3596a4cb967d67` | 2 |
| pipeline | `geometry_20261116_live128_input_support_call_pipeline.py` | 43258 | `de7cb5aae4e80694a899ca36eaa6e067d14f8af60dfd7da074805316a8ff3303` | 4 |
| call | `geometry_20261116_live128_input_support_current_call.mjs` | 48864 | `678a216ea7c030ca2b66129befb6a4f9f8f53845c46daa4bfc32b668b8c830cb` | 14 |
| worker | `geometry_20261116_live128_input_support_worker.mjs` | 8878 | `18a6da3f8a9133128e048686fd78c11b05d7cbecbac9e459e652cd6c30520370` | 4 |
| client | `geometry_20261116_live128_input_support_tail_client.py` | 41346 | `c4aaf9f1da54f6cf843cc138b79bce4a9d94a07a990118ae3bf494ff864c4e39` | 8 |
| fulldn | `geometry_20261116_live128_input_support_original_full_dn.py` | 47523 | `b2bae392a4746db7e9741fa6b26c893f124cb48c4c2448f2c9a277fe2934e542` | 4 |
| runner | `geometry_20261116_live128_input_support_owned_run.py` | 39323 | `4ad124b99196e6574a3f2cecc9e731dd8a32858e1f9fd9e03dc3312b9e9a3489` | 11 |
| reader | `root_20261116_live128_input_support_necessary.py` | 68099 | `e08f0e5f4077e337e95c1fbb3f9bb74c37eab44dbebf72093169d5b2bd2ef8e5` | 15 |

plan 的每个 view 保全部 baseline 三身份键、每个 before / after / 精确 count、最终 output 三身份键。生成时逐 anchor 核 count，形成全文后核字节数与 SHA；已存在输出不覆盖。任何旧源同名但不同 SHA 都被拒绝为来源不符。generator 自身、outer、plan、实际 checkout HEAD / GITHUB_SHA 也直接绑定。所有旧、生成、额外来源在当前完整 map 中均真核，而非只看 cardinality。

只在 metadata 文字层按原基线应用上述全部 literal，已逐件恢复相同完整输出字节。没有执行任一 Python / Node 科学模块、import、AST、编译、数值算术、fixture 或科学测试。原工作流保有的 Python compile / Node --check 在未来实际公开 Actions 中执行，不在作者环境执行；它们仍是原 source preparation 的责任，不是新增科学验收。

## 3. 真实 factory 调用点，非悬空 adapter

R573 worker 原来读取真实恢复的
`scripts/78718-prefix-tail-tangent-fourier-worker.mjs`，核原 12294 字节源 SHA256
`36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a`，
再作其明确 source composition。当前新 worker 保这个入口及原反向恢复检查，额外只在原 source 的下式独一 occurrence 替换 import 的真实 URL：

```javascript
 (await import('./78718-tail-fourier-root-split-engine.mjs')).createFourierRootSplitFluxEngine:null;
```

替换后它导入当前 computations 内实际 R602 factory 的绝对 file URL。替换发生在原 worker 通用相对 import 解释之前，因此新文件不会被误送到原恢复 scripts 目录。原 field / geometry / stored-engine 的导入位置和全部原 source pin 保留。

原 worker 对同一 cell.engine 用 Set 识别，给每个实际 engine 构造一次 updated factory，随后沿原 Object.assign 方式安装。新 R602 factory 内 **仍调用原 a47df factory 一次**，保其 root / split / rhsWithJacobian / tables / existing statistics 等原引用，只替换 flowStateWithJacobian。每个实际 engine 有独立 R523 statistics；同一个 engine 原来被多个 cell 使用的共享关系不改。

manifest 增加实际 factory URL / SHA、R602 范围和原 local-J / schedule 保留声明。它依然返回全部 original-worker replacements、importRedirects、完整原 worker 逆恢复身份、实际新 worker / call 身份。普通 stdout 协议仍转发原 assembler 的 responseText，没有 Node 重新序列化改变返回数字。

R602 的约定本身见 R602 完整证明与接口。它真读取并绑定：

| 原对象 | 字节 | SHA256 |
|---|---:|---|
| 原 factory a47df | 2045 | `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372` |
| 原 flow 717ac | 2400 | `717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f` |
| 原 local J 205b | 3948 | `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25` |
| 原 integrationGrid b12f | 1805 | `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f` |

这些是实际被消费的祖先身份，不把新 factory 冒充 a47df 或新 flow 冒充 717ac 的全源 SHA。

## 4. 两条实际 with-J 路径都经过同一 engine

### 4.1 原当前 H 初始完整 evaluate

current_call 保完整原 `dn.tail.evaluate(states,target,true,scales)`，没有省略它、代入零 H 解、删方向或缓存旧 H 的 J。其 original-core 全源仍为
`ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`，
actual evaluate.toString 的 SHA 仍严格核
`9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9`。

原 evaluate 由原 cellFlow 调用已装好的当前 engine.flowStateWithJacobian。故 R602 是这次实际完整 J 的乘积实现。new core-instrumentation 记录 actual_input_support_source_bindings、完整 stage-to-engine 映射、actual_flow_factory_is_R602=true、original_flow_source_claimed_identical=false。旧“evaluate 和 flow 都未 instrument”合并措辞拆为准确的 evaluate 原 body、声明的 R602 flow 与原 schedule，不伪称整个 flow 旧字节。

之后原 snapshot 形成、全部 raw arrays / negative-zero sidecars / scales / cut / far / request words、全 R273 矩阵与方向仍走原程序。新 system 改两个 producer basename，并把“原 evaluate 原字”的错误信息收窄到它实际核验的对象。QR 只改 system 的实际名与 SHA；pipeline 只改 system / QR 的实际名与 SHA。三者数学体原样。原 reciprocal producer 检查仍真实读取实际新 client / call 文件，不丢掉来源要求。

### 4.2 原 owner 状态的 R532 projected64 全模型

本条不派生 R532，也不派生 c4 components 或 assembly。保持：

- R573 owner：26666 字节，`2af373696034e49f61e6dcc49707e668ed60d600b5a4f9dbf0d71d85cd24ad17`。
- R532 same-DN projected stages：32316 字节，`2279a605df5ee41c5400c658018722fd52e6add40ee35ff38dbca1a31b2bb76a`。
- R534 final components：38561 字节，`c4b3a5eb05fc4d4ae6767c2c08f75ea38a5a5538366fcd3264ff59cec17bb04e`。
- R534 response assembly：33269 字节，`863790de6c0c2020d79150ac99134b2a8ee74592cc42669127ca7df296a0f21a`。

R532 的当前来源 tuple 接受 caller 明确提供的实际 owner / client / current_call / worker 完整身份；本文的新 currentModelSourceTuple 真读取四件，再与 spec.frozen_sources 核 SHA。owner 保旧原字，另外三件是上表新实际源。七项原语义 schema 继续指相同数学合同；实际 source receipt 直接区分新旧实现。

R532 对已加载 DN、engine、flow 引用作真实 capture / before-after 同一性检查，并记录实际 flow 函数 SHA；它不靠 a47df 的文件名推当前 flow 就是旧字节。其每个 n 的原调用仍是：

```javascript
const f=c.engine.flowStateWithJacobian(initial,c.profiles,
 {stepsPerSegment:dn.tail.parameters.steps});
```

所有 576 stage、226 输出、224 方向、before-port / after-port、两 mean、shooting residuals 和原最终统计均照原形成。原字段 original_flowStateWithJacobian_invocations 在本组合中继续数**原调用位置的 API 调用**，不等于声明当前函数文本与 717ac 逐字相同；实际新 flow hash / factory binding 与本文共同给出范围。

当前 owner 的 binary128 状态仍只作原一次 RN64 投影；projected64 点不因此被当作 accepted native 解。完整 finite64 模型按原 bit-level 精确 lift 到 binary128，非有限模型字仍按原责任失败。owner / replay 的128值和原 residual 仍权威。新乘积计数不替代模型准确性、fresh replay、原 FD 或最终 audit。

## 5. 本地乘积的条件结论及不得扩大之处

本节调用 R523 / R602 的已证条件，不重复制造新的执行结果。每次实际 RHS/local J 已按原算法形成 A 后，helper 独立检查当前 A 的全部 size×K 项和实际会被读取的 T 前 K² 项；此处 K=224、size=226。T 的后两行不在原 j<K 的右操作数范围，不能为了统计多读它们为新资格。

合格时只为**本次当前 T**的每行记录非零列地址；保每个输出的原 j 顺序、每个保留 product 再 add 的括号、原 +0 输出初始化、所有输出列和两 mean。对 A 的 z===0 项不形成乘积；对非零 A 的当前 T 行仅访问真实非零支撑。没有输入模式分块假设、零 H 假设、旧 T 支撑复用或跨 H 缓存。所有原非零乘积下溢、有限累加、overflow / NaN 的边界仍由 R523 原完整命题负责。

不满足有限输入资格时立即走原完整 i / j / k 循环；不是拒收。有限 A、T 不意味着中间乘积/累加有限。有限结果的逐词结论和非有限分类结论必须分开；不声称任意 NaN payload、floating flags、总程序资源前沿或执行时间相同。helper 不捕获资源异常再重跑，不新增 output-finite throw 或数学门。

R602 保原初始 tangent、RK 四 field 的次序、increment、所有 state / tangent 最终 += 位置、原 integrationGrid / ordinaryH、cusp profile 调用和 root statistics。它未把原 finite-trace 库接入当前 Fourier-product local J。减少的是满足原资格时可以严格省略的标量乘积/加法，实际减少多少、是否更快、是否在原钟内走得更远都须由真实返回区分。

原 noJ/rhs/rk4 等已有函数引用保持；不过当前原 fullDN 的实际请求仍以其原 jacobian / audit flags 决定责任，不因外层称 noJ 就可以省初始完整内部 J 或 predictor。新入口没有改变这些 flags。

## 6. 实际统计、共享 engine 和中断范围

新 current_call 在真实 session 建立时遍历原 dn.tail.cells，按 engine 的 JavaScript 对象身份建立完整 `actual_stage_to_engine`。每个 distinct engine 检查 R602 linearEvaluation、实际 factory/helper SHA 与本 spec frozen sources，然后保存它的真实 flow toString SHA 与 source binding。相同 source binding 仅在完整 encode 相等时具名共享；engine 本身、statistics 本身不被合并。

快照文件是每个真实 call 目录下的 `input-support-progress.json`。每次先写独占 `.writing`，完成后 rename；旧完整快照不因部分新写被假称当前完整。body 保存：

- 完整 576 个 stage 到 engine 的地址映射；每个 engine 的索引和 source_binding_index。
- 该 engine 的 actual_flow_source_sha256。
- **整个实际** linearInputSupportStatistics 对象，包括 schema、14 个计数、fallback_reason_counts、full last_observation、所有 scope 与未知后续字段。
- 原 source / hook / call / job deadline、真实保存序号、阶段和原 model-clock callback 的完整上下文。
- “累计真实 engine 对象”“末快照不等于强杀位置”“快照之后同步工作未返回”“统计不替全 J / 两 mean / 接受”的明确范围。

14 项计数不作白名单删节；下表只是已有对象的说明：

| 类型 | 原完整成员 |
|---|---|
| 调用和资格 | calls_started、calls_completed、finite_input_calls、original_complete_loop_calls |
| 实际扫描 | actual_A_entries_checked、actual_used_T_entries_checked |
| A 行省略/保留 | zero_j_terms_skipped、scalar_products_skipped、retained_j_terms_completed |
| 当前 T 支撑 | actual_nonzero_T_words_indexed、actual_zero_T_words_seen、T_rows_indexed |
| 非零 A 后 | zero_T_products_skipped_after_nonzero_A、retained_scalar_products_completed |

快照发生在原初始 evaluate 前/返回后，原 R532 model-clock callback 成功返回后、完整模型返回后、实际 response 返回前以及可捕获的 call failure 路径。R532 原 callback 的 stage / complete_stages 是实际原库给出的，不由计数倒推。callback 调用数和位置不变；新 metadata 写入发生在原 clock 检查之后。它有实际 wall-time / I/O / allocation 成本，计入同一个原钟，未获额外时间。

计数在 engine 生命周期内累计，多个 cell、初始 evaluate、projected model、后续 H 若实际复用同一 engine，会共享该原对象计数。reader 不把累计数伪造成本 call 独立数，也不自行相减填出未返工作。

若 worker 在同步 evaluate 或某个同步 cellFlow 内被强杀，JavaScript 不能保证再执行保存回调。必要 reader 仅返回最后实际完整快照及已有 `.writing` 的完整文件身份；没有最后文件则返回 present=false。它不补当前 engine 内部 k、原未保存操作数、最后 stage 或 all_completed。原 model result 自身的 current_stage / unvisited 与原全部 error scope 仍由原 reader 另外完整选择。普通 exception 可保存当时对象，但不会改变原 exception 或重跑科学；保存失败的 error 如实保留。

## 7. source-only 一次父链和真实目录

新 generator 的 CLI 不改变本题真实 computations 目录。它要求
GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations 与实际 HERE 相等；新 views 就在这里以新名写入。既不把视图放到另一目录却保旧 computations 标签，也不篡改 GITHUB_WORKSPACE 来绕过原 loader。

prepare 顺序：

1. 核公开250 outer、generator自身、完整plan、原248 outer/plan/generator、真实 checkout HEAD，以及 fresh request250-source-preparation。
2. 以原248 outer 参数调用原 R593 prepare 一次。它继续真实 R589→R573 等所有祖先步骤，不作为重复科学运行。
3. 真读取 request248-source-preparation/source-views.json，核同 run 四字段、complete、child exit0；读取其 actual current_request，路径必须是同目录 current-request248.json，字节/SHA真核。由该完整实际对象取得 454 源/91生成，不能拿原246 map 假补当前248。
4. 核全部原454实际文件、额外两个已刊组件；按plan顺序在新名生成九件，各核全文 SHA，再追加generator自身和新源。所有旧pin保原值。
5. 写真实 current-request250.json、complete-source-map.json 与 source-views.json。source receipt 保实际父current request完整身份和全部新生成记录/未生成suffix。
6. 只在完整成功时向 GITHUB_ENV 写本job当前请求路径和真SHA。若中断/失败，partial源记录、错误、未生成suffix保留；后续独立always读回按实际范围归责，不填成功。

原 R573 owner 的安装函数仍消费其真实同job request240-source-preparation 祖先记录，直接安装 R572 一次；原 R535/R550/R561/R564 source-only 祖先关系不改。它的“240”是来源 schema/临时子合同号，不冒旧实际 run，run/source 四字段均是当前公开 job。new current tuple 的 owner 是同一个原字源，与该实际生成 receipt 一致。

current_request 的数值合同从实际248完整 deep copy。只更新当前 request_number/schema/namespace、三个实际入口名、完整源码 map、source计划/来源记录和本条 provenance。所有祖先对象保持；尤其原 R593_resource_strategy 中关于其当时 R573 源不变的描述保为祖先记录，并在新 R603_current_DN_input_support 中明确它不是“当前所有 flow 字节未变”的声明。

## 8. 原输入、参数、门和预算全部保留

完整来源仍由固定248 outer → 完整246祖先 → 同job实际248明确读取，而非把下表当作新的省略输入。下列压缩件是原已存输入，作者没有新建或借其推本次接受。

| 原输入键 | stored 字节 | SHA256 |
|---|---:|---|
| accepted | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| warm | 4799943 | `6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a` |
| warm_status | 231286 | `6443fce5e818ff20fd36075f6038ee60630d0b77e8ed2304d41e4d072ea6a005` |
| tail_config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| frozen_ledger_ready | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| frozen_stored_ready | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

原输入固定 commit 是 `8bd267107cc8710d371f3b62c02986655ac965b0`；各原路径、Git blob、runtime basename、解压后身份及 source ledger 按父合同全保。actual63 源 run43646179305 / source db6d728f30ee2d0c9ea62c96c622d8d85d2354b2，decoded status1810333 / 8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46，仅完整 prefix 初猜。actual91 artifact14145200674 / run43672150224 的原 expected_size10267458、SHA78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6、source b78f0dd1471a118d2ed21467602509d188c2ab67 全保，仅 failed73 whole-state tail 初猜。原78完整恢复source职责照原执行。

| 合同 | 明确原值 / 范围 |
|---|---|
| 维数 | M=112、tail112、spacing2、depth576、577节点、每节点224态、局部226态、224方向、338返回行、physical J 338×112 |
| 原 tail 数值 | quadrature2048、32 iterations、10 trials、solve tolerance2e−9、原 cuspAwareFlow |
| Runtime | node_heap6144、jac_workers2、max_nodes1200、material_angles4096、physical_angles4096、outer_iterations8、extension_step0.005、taper_fraction0.4 |
| 原 R273 | eta字面“1”、native_exact_workers2、native_max_factor_bytes2147483648 |
| FD | direct / separated 各10方向、3 step layers、2 Richardson layers、相对阈值0.00005、原 applicable contractions |
| Prefix/fullDN | 原17试步、RMS tolerance1e−6、boundary tolerance1e−11、全部原 physical RMS/domain gates、最终同H fresh audit |
| 总科学钟 | 19200秒；原规则同步/首次factory之前起一次；不同 H 不重开 |
| 当前 owner | 12000秒上限，replay reserve1200在该 allowance 内，threads4 |
| 其它调用上限 | factor19200、stage8000、boundary600、endpoint600、audit1800；原overheads345/720/345/345保留 |
| 外层/清理 | job350分钟、science step320分钟、readback/cleanup reserve120秒 |
| 存储 | startup minimum68719476736字节、科学stop reserve2147483648字节；不放宽原实际门 |
| 调用范围 | 原outerloop最多18 uncached protocol calls；上限不代表所有调用均能完成 |

两组 mean 与338行顺序按原实际 consumer合同，不以历史metadata名称替换。原 mixed338×112 不是全部解析J；新增全解析门没有授权，也没有加入。原原始响应、affine FD选择、fullDN验收和fresh audit决定接受。统计、source preparation complete、job success、elapsed时间或程序完成flag不能替它们。

原 H 初猜选择 last / tangentPredictor / fallback / geometricAmplitudeWarm / currentDirichlet correction 在祖先已有，当前仍原字；不把它们宣称为新优化，也不导入历史成功 J/response cache。原 noJ / jacobian flags与optional predictor是否能合法返回按原路径保。

## 9. 原 clock、owner、quiet 与 cleanup

runner由真实248 runner17dd19a1派生，仅新tuple/namespace/schema和明确source描述改变；原 prepare / science / rules / run / quiet / cleanup 的控制流不改。原科学钟在source与输入恢复之后，由本job原 run 一次建立，包含原规则同步与真正factory；source-only生成不伪称science耗时或重开预算。各owner/guard/组件使用原同一绝对deadline及剩余时间clip。

实际PID、start_ticks、session/group、descendant、suspected namespace和不可读scope规则保持。原 quiet 若不能证实，必要reader仍不读取科学文件为成功scope，cleanup跳过。源必要与科学必要分别 always 执行；某份70不阻止另一份真实尝试。只有两份 necessary_complete 真值与再次 quiet / 当前 source/run/request ownership全符时，原cleanup才能删除本次namespace。

.source-preparation及新源码是本runner临时件，不提交Git或artifact。未完成科学/transport/quiet时，原raw保到runner销毁；不为了新统计fit删旧错误、未访地址或原数组输入。

## 10. 全部实际 CLI 和工作流顺序

以下命令是**未来公开 Actions**的实际接口说明，不是本条已执行记录。comp 为真实 GITHUB_WORKSPACE 下本题 computations；namespace、source metadata 都必须为 RUNNER_TEMP 的下列精确子目录。工作流已包含原checkout sparse/blob:none、原Python/Node/NumPy/SciPy/编译器版本与全部旧source plan路径，并新增本plan；所有版号原样。

source prepare 的完整新增CLI：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_input_support_source_views.py" prepare \
  --request "$VISIBLE_COMPUTATIONS/public-live128-current-DN-input-support-composition-request.json" \
  --request-sha256 160492decfaeef22c37e391f8001ed11105b6c988723ab32b056bc6e3283877c \
  --computations "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/request250-source-preparation"
```

内部真实原父调用是：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_extended_owner_budget_source_views.py" prepare \
  --request "$VISIBLE_COMPUTATIONS/public-live128-extended-owner-budget-composition-request.json" \
  --request-sha256 002265d96fc7dedaa4500708b8a028f3ccb660eef55c21528325555e3b9e2cc8 \
  --computations "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/request248-source-preparation"
```

后续step的环境由真source receipt设：

- VISIBLE_BASE = RUNNER_TEMP/visible-live128-input-support250；
- VISIBLE_SOURCE_PREPARATION = RUNNER_TEMP/request250-source-preparation；
- VISIBLE_CURRENT_REQUEST = 其真实 current-request250.json；
- VISIBLE_CURRENT_REQUEST_SHA256 = 该真实全文SHA，不预计算动态路径字节为旧248SHA；
- VISIBLE_NECESSARY = RUNNER_TEMP/visible-live128-input-support250-necessary.json。

原owned入口两个实行动作：

```bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_input_support_owned_run.py" prepare \
  --request "$VISIBLE_CURRENT_REQUEST" --request-sha256 "$VISIBLE_CURRENT_REQUEST_SHA256" \
  --namespace "$VISIBLE_BASE"

PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_input_support_owned_run.py" run \
  --request "$VISIBLE_CURRENT_REQUEST" --request-sha256 "$VISIBLE_CURRENT_REQUEST_SHA256" \
  --namespace "$VISIBLE_BASE"
```

prepare仍恢复全部原63/78/91；run仍派原 rules及science，内部原 flags/parameters由完整当前请求按原CLI逐字段取值。本条无另加fixture/短跑/benchmark。

两份各自完整必要接口：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_input_support_source_views.py" readback \
  --request "$VISIBLE_COMPUTATIONS/public-live128-current-DN-input-support-composition-request.json" \
  --request-sha256 160492decfaeef22c37e391f8001ed11105b6c988723ab32b056bc6e3283877c \
  --computations "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/request250-source-preparation"

PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_input_support_necessary.py" \
  --request "$VISIBLE_CURRENT_REQUEST" --request-sha256 "$VISIBLE_CURRENT_REQUEST_SHA256" \
  --namespace "$VISIBLE_BASE" --out "$VISIBLE_NECESSARY"
```

原cleanup接口只是当前basename/绑定变化：

```bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_input_support_owned_run.py" cleanup \
  --request "$VISIBLE_CURRENT_REQUEST" --request-sha256 "$VISIBLE_CURRENT_REQUEST_SHA256" \
  --namespace "$VISIBLE_BASE" --summary "$VISIBLE_NECESSARY"
```

它只由工作流原完整条件分支调用。report保compute结果，不把report success作为science success。当前workflow只有明示workflow_dispatch；root正式刊出后才能作一次真实dispatch，作者没有自行启动。

## 11. 单份完整必要读回，旧70与原地址不丢

### 11.1 Source necessary

schema为 `R603-live128-input-support-complete-source-preparation-v1-necessary-v1`；
frame为
`BEGIN_REQUEST250_CURRENT_INPUT_SUPPORT_SOURCE_NECESSARY` /
`END_REQUEST250_CURRENT_INPUT_SUPPORT_SOURCE_NECESSARY`。
实际body文件为 RUNNER_TEMP/request250-source-preparation-necessary.json。

本 reader 真调用原 R593 readback 一次。原child返回70时，按其descriptor和固定samejob路径读取完整 necessary-source-overflow.json，核全bytes/SHA及attempted identity，保原child70、原false transport、完整原必要body。普通0/2也按原schema/run/source/plan/outer真绑定。旧fallback不被改成完整body；新的完整必要状态独立判断实际当前记录与原fullbody的necessary范围。

新current source record中的完整生成/未生成/error/stderr/stdout identity全部保。可选R588具名关系只作用于这一**已完整读取的 current_source_record**；原parent完整body/其原具名关系保持原对象不动。绑定原R58819120/6f7cb804后，只有连同新表/header/inverse的整个candidate严格更短才选。关系给出原selected canonical bytes/SHA和明确字段，逆为只对current_source_record调用原restore_relation；未知形状完整保留。关系失败保原literal对象及真实error，不能借编码删scope。

最后整个新body超过90000就返回70，保local full object identity/attempted bytes/SHA、cleanup=false、unreturned全范围。本文不保证R603一定fit；source结构比原新增并不等于未来任何错误体都能压到90K。

### 11.2 Science necessary

schema为 `R603-live128-input-support-original-full112-necessary-v1`；
frame为
`BEGIN_REQUEST250_CURRENT_INPUT_SUPPORT_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY` /
相应END。原248 reader65727字节的所有原选择、八 RootWordMetadata族、全部root统计/last/source/compilation、owner trials/replay、model/lift/guard、FD/fullDN、original stderr、actual partial/unvisited、错误和quiet范围逐项保留。

新增方法仅从每个实际 call 的固定 input-support-progress.json 读取上述整个快照；actual_file保present / bytes / SHA，missing与实际JSON null分开。存在文件时核当前call与当前call/client source；所有14计数、全部fallback/last/unknown都已在original_value中原样，没有只传计数总和。实际 `.writing` 身份独立列出，不能冒完整快照。call-result已有的 actual_input_support_progress及snapshot_error也保。

current source及statistics可能比旧摘要更大，完整90K限制不升。超过时保原single overflow70和明确未返，不切片，不把全科学tree/数组重新编码，不为容量删旧失败地址。原R588对RootStats的具名相等共享依然原样；new R523统计不被冒成R572 RootStats。

## 12. 条件来源命题与实际未付责任

**命题。** 假定本次公开Actions按本文精确固定源/输入执行、原来源/尺寸/工作目录核对返回、相应field实际完成，且R523的普通无并发mutation typed-array调用前提成立，则其newwithJ的A*T由当前实际A/T构成；所有非零输出算术顺序按R602条件命题保留，fallback按原完整循环，原全维模型/两mean/边界/FD/fullDN门没有因本接线缩减。所有已保存的输入支撑统计是同一engine的真实对象快照，完整必要消费者确实选取，而非仅在源内声明后漏读。

证明由§3真实worker import、§4两个实际调用者的引用与source绑定、§5已证局部乘积、§6真实快照及§7–11实际完整消费者组成。source中的ordinary error/资源退出可以使某阶段或整个job未完成；命题没有把成功条件由metadata推成事实。原原始根/J构造已共享，不由新counter再计为收益。

当前尚未付的仍包括：新公开job真实sourcepreflight；实际原输入恢复、容量和原钟；完整初始evaluate、R273方向；persistent128 solve/fresh replay；全R532当前模型和所有组件/FD/fullDN；两份真实必要是否fit；实际quiet及cleanup；实际时间与任何数值接受结果。后继R607必须按原返回逐项归责，不能由已刊R602/R603或任何历史正高run接受代判。

当前已成完整执行来源不等于实现额外连续闭面/全t几何证书。这个入口继承原finite-prefix/native/fullDN问题及其既定门。其 source-only 对照仅是源码/参数身份和条件控制流，不新建数学门、额外审计或确认流程。
