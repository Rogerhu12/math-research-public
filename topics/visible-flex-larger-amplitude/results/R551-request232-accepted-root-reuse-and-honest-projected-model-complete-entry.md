# R551 — request232：同根已接受完整 RootEval 复用与诚实 projected64 契约的全链入口

作者：OpenAI ChatGPT（AI 助手）  
日期：2026-11-16

**可信度：已证明（限本文来源组合、逐字控制流和所列条件命题）；request232 的实际编译、owner/replay、完整模型、FD/fullDN 与最终审计尚未执行。** R552 仅为后续 actual232 结论预留号。本稿不把准备成功、统计存在、source pin 相等或某个程序完成解释成数值接受。

本入口以已发表 R548/request231 为完整来源与输入祖先，在一个新实际 job 中重新恢复同一原初猜，执行 R550 的同根下一迭代完整已接受求值复用；同时修复原 system 对实际 current-call 契约键的误读。原 112 模式、576 段、每段完整 226×224 切向与两均值、原完整 338×112 物理响应、所有 FD/fullDN 与最终审计门不变。当前模型仍是原 R534 声明的、在真实 owner128 末状态一次 RN64 投影上形成的完整 projected64 模型；不将其重标成 owner128 程序的全解析导数。

本稿只登记一套可实际调用的新来源。它没有执行祖先 231 的科学 owner，没有继承 229/231 的接受、响应、J 或缓存，没有派发作业，也没有做本地 import、AST、编译、科学算术、fixture、微基准或独立验收。文中字符串重建、JSON 结构比较与 bytes/SHA 只是本次源码形成工作。

## 1. 固定祖先与此次真实差异

### 1.1 完整原 request231

固定公开来源为 `05ae500a2aa98784fe05f6b4b8b3fcf2424f9d59`。其三件是：

| 角色 | 原路径 | bytes | SHA-256 |
| --- | --- | ---: | --- |
| 完整请求 | `computations/public-live128-root-cached-projected-model-original-full112-FD-fullDN-request.json` | 95286 | `f70f24d223f018c0c551a4437455d9491f491334a260d5bce30d93822d6a5b66` |
| 工作流 | `.github/workflows/visible-larger-public-live128-root-cached-projected-model-original-fullDN.yml` | 23014 | `f1d3070182f5ea83c670edf8e1f4aaf3126de2e1f671dbbeaa07e3479025a57f` |
| 原完整接口 | `results/R548-request231-cached-owner-and-same-DN-model-complete-entry.md` | 26027 | `fd1b49f6e3a096a5a171213b664c72b2eb9c0b1228182a00c43920071aa0cad8` |

原 R547 generator 是 `root_20261116_live128_cached_projected_source_views.py`，23546 bytes / `57a28670e2fe167c816f470052923ce130197eb4e182dbf3e959547e07846de3`；原完整 source plan 是 `notes/r547-live128-root-cached-projected-model-complete-source-plan.json`，54357 bytes / `d16616edbadfa2d5bf0c3d4f55b2f3a9b6724dc7a1ae09251898fb945ead1aab`。两者的正文与所有原 387 source words 保留。

本文同时保留原 R534 core plan：72022 bytes / `826aabbd34c2282bdaa4b8298a79bb92b90dc8758134b309f665d863301a4648`，真实字段是祖先请求的 `ancestor_R534_core_source_plan`。新 generator 使用这个实际字段；没有把 231 误当具有原 229 `core_source_plan` 字段的对象。

### 1.2 R550 原执行件

| 角色 | 原真实 basename / metadata path | bytes | SHA-256 |
| --- | --- | ---: | --- |
| 完整 RootEval 复用 header | `root_20261116_accepted_root_evaluation_reuse.hpp` | 7311 | `8610fdd602ca3cea28a0d28af254e1929e954d7762161cc4887af5a097190f26` |
| 原 compiler 接点 adapter | `root_20261116_accepted_root_evaluation_reuse.py` | 16634 | `66c2ff0d0b29c41cef00cc6a77764e4e168d2885c52b3f56c2abd961fad8f97c` |
| 完整 literal source plan | `notes/R550-accepted-root-evaluation-complete-source-plan.json` | 12303 | `14b5c02071359276be2988dc273d6864df3d61e728df10df5b1bddc498134457` |

局部复用论证参见 [R550](R550-same-root-accepted-complete-evaluation-reuse.md)，26142 bytes / `ca1e24f7ef265fa196b0b93f36b37a1c7e8befdb09313e6e99de6125fe37bf30`。本文不重复更换该 header/adapter 的数学正文，而是给出其到真实 owner、全部后续消费者与必要返回的实际接点。R550 四件随后已正式发表于 main `bb4a03981babcf956e408930538941d54b2c547a`；该发布身份与实际科学运行编号仍分开。当前入口依赖这里列出的完整文件身份，不预填 request232 的未来运行。

R550 继续绑定 R535：原 header 7102 bytes / `6706eae670bf5746eb42d194bd456d290c290d451ddc52d80359d0263f90e7cc`，原 adapter 10892 bytes / `1c99623e2cd63d0a4700011c96e5054645cf7dd8ee5cf3357f0c77d1727026db`，原 plan 10232 bytes / `f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b`。这里保留旧有限词缓存，不把完整 RootEval 的新来源冒成旧 include。

### 1.3 原模型消费者不复制、不换数学

以下三件仍逐字原样：

| 角色 | basename | bytes | SHA-256 |
| --- | --- | ---: | --- |
| boundary | `geometry_20261116_live128_projected_model_boundary128.cpp` | 12844 | `0364ea5cc8173f40dbe7a375fbca798987dcd75b4f67b90470c638352ae8ecb9` |
| components | `geometry_20261116_live128_projected_model_final_components.py` | 38561 | `c4b3a5eb05fc4d4ae6767c2c08f75ea38a5a5538366fcd3264ff59cec17bb04e` |
| assembly | `geometry_20261116_live128_projected_model_response_assembly.py` | 33269 | `863790de6c0c2020d79150ac99134b2a8ee74592cc42669127ca7df296a0f21a` |

完整当前阶段仍由真实加载的同一 DN engine、真实当前状态与原 RK/port/cusp 路径产生；本文不把旧 paired-digit stage 或历史已经完成的响应接作当前 stage。历史相关源继续在完整 ancestry map 中，不等于本入口会调用其所有旧 main。

## 2. 来源集合与唯一实际目录

### 2.1 数量是显式集合的基数

| 集合 | public | generated | complete |
| --- | ---: | ---: | ---: |
| 固定 request231 全部原来源 | 348 | 39 | 387 |
| 新 R550 header 与 adapter | 2 | 0 | 2 |
| 新 R551 generator | 1 | 0 | 1 |
| 新 R550 primal/trace include | 0 | 2 | 2 |
| 新 R551 十 caller views | 0 | 10 | 10 |
| 本请求实际声明并集 | **351** | **51** | **402** |

新 `source_sha256` 完整保留原 387 个 name→SHA；新 `generated_source_sha256` 完整保留原 39 个 generated 条目，再加真实 12 个新输出。名字分别存在，不覆盖旧文件。计数来自字面 map 并集；不宣称它自动证明任意未来动态 import 的递归闭包。

原 39 个 generated 文件不是仓库公共文件：必须由本次 job 的真实祖先 generator 重建。新 12 个输出也只在 Actions 中形成，不把它们写入 Git，不借旧执行结果代替文本生成。本次发布仅一件 generator、一份 complete literal plan、一份请求、一份 workflow 与本文。

### 2.2 源准备顺序

新 generator 的 `context` 固定实际：

```text
HERE = GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations
TOPIC = HERE.parent
new metadata = RUNNER_TEMP/request232-source-preparation
old metadata = RUNNER_TEMP/request231-source-preparation
```

它先核新 plan 与自身完整 bytes/SHA，亲读固定 95286-byte 原请求，再核其中原 generator/plan/core-plan 身份、request231/schema/387/39。祖先请求是独立保存的原件，不用新请求的历史标签代替原文件。

顺序如下。

1. 新 metadata 目录必须 fresh；所有预期新 caller/include 文件必须未占用。
2. 在真实同一 `HERE` 中运行原 R547 generator 的 `prepare`。它按原合同继续真实恢复 R534/R527 等原 source ancestry 与 R535 source-only include。
3. R547 child 真返回后，核其原 schema、complete/error、四个 run/source keys、actual_computations，并逐文件核原 387 个完整 source SHA。
4. 核两件新公共 R550 源及新 generator，按新 plan 的完整 `before/after/count` 顺序形成十个新 caller 文本，核全部新 bytes/SHA；此时尚未执行 caller。
5. 调用原 R550 adapter 的 source-only CLI。它内部真实调用 R535 的 `prepare_sources`；已有 include 只在完整同字节时接受。此动作没有安装 R535 compiler hook，也没有编译或调用数值 owner。
6. 读取真实 R550 binding、两实际输出及其完整 SHA，并核 actual run/HERE、source_preparation_complete、compiler_completed=false、scientific_evaluation_performed_by_preparation=false。其完整祖先 R535 body 保留。
7. 以新 basename 排他写出十 caller，逐件读回 bytes/SHA，并写完整 402 来源 map、51 generated map、roles、counts 与未生成 suffix。

R547 child 在当前准备记录中保真实 `actual_source_receipt`、command/exit/log identities，原385KB级完整source record仍在其实际原路径。本层不再重复嵌入一个无人消费的副本；全部原必要选择另由真正的原R547 readback及其保留full文件支付。R550 child完整 `source_result` 仍保留，真实当前owner会亲核并消费它。

准备记录包含每个 child 的 command/started/returned/exit、stdout/stderr 身份、真实 source receipt，以及完整 error/traceback 与实际 `generated/not_generated`。异常不补成功；准备阶段没有启动第二个科学钟，也没有用一个成功的文本转换冒实际 compiler 返回。

### 2.3 两个新实际 include

| 角色 | 真实输出 basename | bytes | SHA-256 |
| --- | --- | ---: | --- |
| primal | `root_20261116_accepted_root_evaluation_reuse_primal128.cpp` | 25794 | `40e89e28adc36848cf0d28b466e219065e10bdf8b37145d5e18326a6cd5eb6e1` |
| trace | `root_20261116_accepted_root_evaluation_reuse_trace128.cpp` | 35565 | `822488bd3ca682478939baa7df047aa614218b6724e448f01705e10c9225eb71` |

两旧 R535 include 仍在 source map 中。R550 binding 的 `actual_R535_source_binding`、`actual_headers`、`actual_original_sources`、`actual_generated_sources` 分别保留原 adapter/header/owner/CPP、旧 include 与真实新 include；不让其中一个短 provenance 标签代替实际文件。

## 3. 十个实际 caller 与字段修复

### 3.1 输出完整身份

| 角色 | 新 basename | bytes | SHA-256 |
| --- | --- | ---: | --- |
| owner | `geometry_20261116_live128_reused_projected_same_call_owner.py` | 25821 | `ea354ba982e6904fc43e552f1d75e2171130e0d4c04e4a1a2c2aaf67d392923c` |
| system | `exact_20261116_live128_reused_projected_current576_system.py` | 29055 | `8cc721f1f8b555176c9b815c266e695c8d59de8b36e136e094ae0b29d223262d` |
| qr | `exact_20261116_live128_reused_projected_current576_chain_qr.py` | 21847 | `ca4673949b9e30ff44761271f67dc927c2b8e916b8e73f6f2ff556aa780832f3` |
| pipeline | `geometry_20261116_live128_reused_projected_call_pipeline.py` | 43209 | `9bcfa99f38399a2fe7c21f5d15bfe728a6ebbf6c03c51c70d8d25f4415928313` |
| call | `geometry_20261116_live128_reused_projected_current_call.mjs` | 45399 | `995334613f7916d5988984fb691275c067280d1b98be1e7ac8f106b34a7d35a8` |
| worker | `geometry_20261116_live128_reused_projected_worker.mjs` | 8305 | `57079b19350f4e17e1f694242f6b37cb0a60362699f6616788af99a733ef1f1c` |
| client | `geometry_20261116_live128_reused_projected_tail_client.py` | 36243 | `4f4865a5f99a7342965b669e8aea82de252caa05bf47d75c8722ad8f1628fc8c` |
| fulldn | `geometry_20261116_live128_reused_projected_original_full_dn.py` | 41830 | `b95937dded2084453509c4b5ecaaca36767ae8314076b42cf49f77ea6d92db2a` |
| runner | `geometry_20261116_live128_reused_projected_owned_run.py` | 39356 | `39712ee8fde3f75299dfced1a699e65a8ae790a472f406761fc03fd68e619079` |
| reader | `root_20261116_live128_reused_projected_necessary.py` | 60620 | `25c2f0937b430ec71c9734296ff79c051e8cc705c1040a31f6211acac16b0318` |

完整 source plan 保存每件旧 basename/bytes/SHA、新完整输出身份和每条 literal 替换的实际次数。所有原科学函数正文除已明确 R550 compiler 接点外，只发生当前来源名、SHA、schema、request/namespace 的必要级联。新 reader 添加实际 R550 统计声明与原完整 RootStats 消费，不新增任何数值阈值。

原 client 的 52 项 source map 逐值保留，新 map 增为 62 项；旧 client 当前动态名字所指旧 SHA 在新 fullDN 的 map 中改为明确历史 basename 后，才增加新当前 client 的真实 SHA。新 role 与旧角色分别存在，不能仅改名字却留下旧执行身份。

### 3.2 真实缺项与最小语义修复

原 R547 system 中 `request_height_bytes` 索取：

```python
B.same(current['same_call_complete128_final_components_required'],True,
       'All224/226 and mixed338-by112 are supplied by the same actual128 state')
```

实际 R534/R547 current-call 已声明的字段是：

```python
same_call_complete128_value_components_and_explicit64_linear_model_required=True
```

新 system 只将该 guard 改为：

```python
B.same(current['same_call_complete128_value_components_and_explicit64_linear_model_required'],True,
       'Current128 values/replay and the explicit complete projected64 linear model are required')
```

该变更与已报告 actual229 的缺键一致，但证明本身只用两个真实源码的字面字段关系，不借它给未读的 231 终态归因。本文不重取 229 日志；其实际 scope 由 R543 负责。本入口没有填入旧字段 true，没有删除 guard，没有把 projected64 模型提升成全部 128 导数。

**命题 551.1（实际字段接续）。** 若本次真实 current-call 完成并返回其原声明，新 system 读取的是它实际写出的同一字段。由于 guard 后面的原 current128 值、模型、边界响应及原 fullDN 消费算法未变，修复消除的是不存在的键，不是一个数值接受条件。若实际字段缺失或不为 true，原控制流仍停止；本文不伪造返回值来跨过它。

## 4. 一次直接 compiler 安装

### 4.1 安装发生在原 scope，准备不安装

新 owner 的 `install_root_evaluation_reuse(owner_scope, record, runner)` 亲读：

```text
RUNNER_TEMP/request232-source-preparation/source-views.json
RUNNER_TEMP/request232-source-preparation/R550/source-binding.json
```

它要求当前 R551 schema/request232/四 run keys/HERE/complete，以及 generated 中实际 owner 的完整文件身份。随后要求实际 `R550_child` 已返回 exit0，binding 路径和完整正文与 child receipt 一致。新 adapter 由固定16634-byte/66c2 源加载，直接对原 `source_scope("owner")` 返回的真实 globals 调用一次 `install_owner_compiler`。

R550 adapter 本身要求 `_R550_SOURCE_BINDING` 与 `_R535_SOURCE_BINDING` 均尚不存在；它亲核原 persistent owner、原 CPP、两个 headers、旧/新 include 和完整 compiler-function source plan。它只在同一 globals 中定义已声明的新 `compile_owner`，使原 `main` 后来真正调用编译。不能先安装 R535 再用 R550 覆盖它。

原 persistent main/solve/replay source 的完整 identity 保留。新 `ORIGINAL_CPP` 与 `TRACE_CPP` 指向两份真实 R550 include，原 persistent CPP 仍为 `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd`。PINS 同时保祖先与新 adapter/header/include，没有把新 include 宣称成旧源码。

### 4.2 原 defer 与后继模型顺序

compiler hook 安装后，新 owner 仍按原 R534 接点核对 `_precleanup_final_components`，再把该钩子设为原 `deferred_current_model_handoff`。实际原 owner main、原返回码、owner_final、原 tolerance、独立 fresh replay 与同一次 call identity 先行；后面的新完整模型继续使用同次 owner 状态。

因此两类动作分开：

- R550 安装记录只证明实际 source 准备和 compiler 接点；其 `actual_compile_not_yet_called` 不可作为编译成功。
- 原 owner summary 的 `compilation.root_finite_word_cache_compilation_source_binding` 才是实际 compiler 调用所写的完整 R550/R535 来源。旧 key 名保留只是 metadata 接口，不表示使用旧 R535 hook。
- 原 R534 defer 说明旧同步 post 组件没有在 owner 内抢先执行；不说明 stage/model/endpoint/audit 已完成。
- 原 boundary/endpoint/独立 audit 的真实字段和原 fullDN 门仍必须由本次实际执行支付。

**命题 551.2（一次安装与来源完整）。** 在固定源与当前 bindings 满足上述实际检查时，唯一运行的 owner compiler hook 来自原 R550 adapter；原 R547 owner 只是保留的历史生成源。源准备两次亲核同一 R535 include 不等于安装两次钩子，不会使原 `main` 脱离其真实 globals。结论不包括编译是否成功、owner 是否收敛或同一预算是否足够。

## 5. 复用的数学范围与不变的原门

R550 的持久对象仅为当前一次 root 调用中的一个完整已接受 `RootEval`。原主迭代仍至多30次，原每次试步至多20档；原 trial 的实际求值和原接受不等式都照常执行。

被接受的 trial 已按原表达形成完整 value，随后原状态改为该 trial。若尚有下一迭代，R550 检查完整 residual 长度 J、角 rows 长度 N、五个 summary words、全部 J residual words 与每个角行的十个词。通过时移动整个对象，下一迭代消费一次；不只缓存误差或几个 summary。形状/非有限资格不符时清除 ready 并保留原下一次重新求值路径；不把这些资格检查变成求解拒收门。第29次迭代接受只记录 no-next，原 iteration-limit 责任不变。

在相同已存有限输入、相同 root 上下文与原表达的确定性条件下，下一次原主求值的输入恰是已接受 trial 的输入；复用的是已经由原路径完整生成的所有有限值，包括符号零。R550 不跨 root、stage、H、geometry 保存它，不把相邻但不等的状态合并，不用三角恒等式或精度变化重算 value。

上述条件只支持已完成有限返回值的同一性与相应原数值判断，不把“输入有限”扩大成所有中间量必有限。资格失败仍走原表达；资源异常不被捕获为重跑。原入口处及完整扫描中的 `time_check` 继续真实执行，新增资格扫描和少执行的求值会改变墙钟、分配行为与资源截断位置；不声称 fenv sticky flags、NaN payload、运行轨迹或耗时逐字相同。

原 RootStats 与 R535 word counters 只计实际执行的工作。新计数不补旧的被省略求值数，也不由 `reused_complete_evaluations>0` 推出整个 root、stage、J 或 fullDN 完成。

本入口保以下原范围：

| 对象 | 保留内容 |
| --- | --- |
| 模式、网格和状态 | field_modes=tail_modes=112，spacing=2，depth=576，577个节点，每节点224状态 |
| 局部切向 | 每段完整226×224，全部224方向，两均值行与原 port/cusp/求和次序 |
| 当前 owner | 原32×10 outer solve/trials，solve_tolerance=2e−9；完整128值与独立fresh replay仍为接受依据 |
| 完整物理输出 | 原顺序 slope112、second112、meanSlopeCorrection1、meanSecondCorrection1、height112；全338×112 |
| FD | direct/separated 两组，各10方向，原3步长层、2 Richardson层、相对门5e−5及全部适用收缩检查 |
| 原前缀与末门 | 原17 inner trials、RMS1e−6、boundary1e−11、完整物理/domain门与同当前H fresh final audit |
| 原模型边界 | 一次RN64完整状态的同DN projected64模型，准确lift到128存储；不称投影点已接受，不称全338解析J |

这些参数是固定原 request231 的值，本文没有替换新的阈值、符号、初点或维数。原 finite-prefix 任务仍不等于完整闭面证明。

## 6. 输入、原钟和资源

### 6.1 初猜来源完整不变

新请求的 `original_inputs`、`actual63`、`actual91_artifact`、`runtime`、`live_call_resources`、`resources`、`original_scientific_contract`、`reviewed_README_blobs`、`lanes` 均与固定231逐值相同。此比较只检查已有 metadata，没有计算科学新值。

原 actual63 warm 仍为4799943-byte压缩输入，SHA `6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a`；其原 decoded status 为1810333 bytes / `8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46`。原 actual91 artifact 仍只取 failed73 全尾状态作初猜，artifact14145200674/10267458 bytes / `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。它不提供当前 prefix、完成响应、接受状态或 J。

原78公开 source、两个完整 ready 与完整 accepted/warm/status/tail config 按原固定Git身份真实恢复。新来源 map 不授权删除有消费者的输入或缩小 source-root；历史实际接受不转移给新当前H。

### 6.2 唯一科学钟与各上限

| 项 | 原值 |
| --- | ---: |
| compute job timeout | 350分钟 |
| science step / 唯一 total scientific time | 320分钟 / 19200秒 |
| readback/cleanup reserve | 120秒 |
| 每call owner cap | 6000秒 |
| fresh replay reserve cap | 1200秒 |
| 完整stage cap | 8000秒 |
| boundary cap | 600秒 |
| endpoint cap | 600秒 |
| 独立audit cap | 1800秒 |
| owner threads | 4 |
| startup minimum free | 68719476736 bytes |
| running free-byte resource stop | 2147483648 bytes |
| 原 outer loop 最大未缓存protocol calls | 18 |

各 cap 是同一个真实绝对截止下的上限，不相加生成新科学钟。新H也不重启19200秒。原 source/input恢复仍在原科学起点之前；原 runner 在 rule sync 与第一个 native factory 前建立 `R493-original-full112-live128-job-deadline-v1`。本文保持该既有时钟合同，不把 source-only child 称科学执行，不通过重复prepare给后面的owner续时。

runtime 仍 node_heap=6144、jac_workers=2、max_nodes=1200、material_angles=physical_angles=4096、outer_iterations=8、extension_step=0.005、taper_fraction=0.4、native_eta词"1"、native_exact_workers=2、native_max_factor_bytes=2147483648。上述真实参数只规定实验，不保证所有可能的18次call、各组件或必要正文都能在现有资源内完成。

## 7. 新统计进入真实必要读回

### 7.1 完整 RootStats，而非只挑计数

新 reader 继续沿原实际 evaluation/owner/replay summary 选择整个 `root_statistics` 对象。R550 新成员 `root_accepted_evaluation_reuse` 无需被截成另一个手写摘要：它作为完整原对象成员保留，内部两个 path 为 `primal` 与 `trace_variation`，每个 path 均保以下13个实际值：

```text
iteration_sites
original_main_evaluations_started
original_main_evaluations_returned
reused_complete_evaluations
accepted_results_offered
qualified_results
shape_declined_results
nonfinite_declined_results
no_next_iteration_results
summary_words_visited
residual_words_visited
angular_rows_visited
angular_words_visited
```

同时完整保 `last_present` 和 `last`；last 包含原 phase、iteration_zero_based、row_zero_based、component_zero_based。无last的null不补成某个地址。原 R53518个计数、其它 RootStats 的原未知键和所有已选必要 scalar 仍保留。

原 `root_statistics` 缺失、字面null、未完成或含部分计数分别保原结构。reader声明13个字段的名字不是验证它们存在的额外门；存在的完整原对象才是实际数据。

### 7.2 八个具名表与精确逆

保留的八类是 `root_statistics`、`root_finite_word_cache`、`owner_compilation`、`root_cache_compile_binding`、三个原 `root_finite_word_cache_source_*` 记录，以及 `physical_source_input_binding`。只有整对象原键集、JSON类型、全部值严格相等时，才在其已声明字段位置共享同一具名正文。

原字典缺键不等于present null；bool/int/float类型分开，−0与+0分开，含NaN的对象不合并。原数组顺序、分组原record index与完整列名保留。逆向先按group columns、constant或original_values、original_record_indices重建每个原字典，再只在显式八类引用位置展开。R550完整成员保留在RootStats中，没有新增任意树编码或数值数组压缩协议。

原 `safe_selected` 对非有限JSON显示的边界仍在；它不是原IEEE NaN payload字节同一性的声明。本方案不把“少传一个重复对象”改成“没选它的内容”。

### 7.3 source/install/compile 分责

原 owner-call-procedure 记录中三字段真实初值为null：

```text
root_finite_word_cache_source_preparation
root_finite_word_cache_source_binding
root_finite_word_cache_compiler_installation
```

source准备后第一项是真source-views descriptor，第二项含actual_file和完整实际R550 binding，第三项是原R550 install返回。reader完整保这些实际记录；另保 `root_primal_uses_declared_R550_accepted_evaluation_reuse_source` 与一次直接安装说明。真实编译来源仍从原summary.compilation选择，不从source或安装推编译。原每call物理source-input manifest与完整实际复制身份保留，未把5件同字节source视图冒新科学。

### 7.4 90KB 与失败责任

源准备scope与科学scope分别独立一份ASCII JSON、各≤90000 bytes；不把同一完整科学正文拆包。科学reader在原owned quiet后保原所有trial/replay/model/FD/fullDN/final/error/unvisited字段与新完整RootStats。

收口时，原231唯一终态读者的 [R549](R549-actual231-declared-model-contract-and-source-readback-overflow.md)（30740 bytes / `5e798549809ba73e9cb1d47c0aa0dc19976ad2cf4f9926022155e55f57078213`）已确认：R547源准备完整返回，但源必要正文 attempted102413 bytes / `df6e42e834390f8dc7b606b945cf683944c609554d96ec25b3b392d0ffdcd2e4`，按原90KB规则返回70，仅返回fallback。这个102413-byte正文没有在旧日志中完整返回，本文也未取旧日志或把它当fixture。

因此新source readback继续真调用原R547 readback，但原child70时不把fallback当完整原body。它在本次job亲读原descriptor指向的 `RUNNER_TEMP/request231-source-preparation/necessary-source-overflow.json`，先核实际路径、bytes/SHA、完整原schema/run与scope；保原child70、原fallback的false及完整原对象身份。新层再独立给出完整原对象的具名可逆表示与本层R550绑定、全部错误和未生成suffix。这里没有改变旧返回码，也不把旧false改为true；当前新层必要scope的完整性按本次完整读取另判。

为去除固定来源语义重复，新层只对已绑定source inventory与literal-change记录使用两张显式具名列表示。它保每条原字段、原键顺序、原行顺序、实际bytes、完整SHA、缺失与null；未知shape保持全文。只有整个有序JSON与另已实际读取的完整source record相等时，才允许在已声明context引用它。逆向须能恢复所有原所选记录，不用任意对象编码或数值近似。原R547全文必要对象先真实读取后才组织，不能拿其overflow descriptor补写缺失正文。

两张表的纯metadata文字来源是 `root_20261116_live128_declared_model_request_source_views.py`，32840 bytes / `543b1d271a7e98cb72babb8a83ebe805ac2f98f72162703283ea3fa3fed56c70`（detached blob `64ffe184486181a1aea3e986aceb0cf48cd04274`）。R551将 `ordered_metadata/NamedSourceTables/selected_source_record/readback` 的相应正文放入自己的generator，只改实际context/schema、402catalogue增量与本层R550日志枚举，并对每个实际stderr（含空文件）保完整identity和text；没有runtime import这个donor，也没有增加第403个source。此为源文字出处，不冒一个额外已经执行的reader。

若新层真实必要正文仍超限，照旧返回70与实际bytes/SHA/未完整返回/不许cleanup；不预删未来字段保证容量。两个readback步骤独立always执行；report独立显示真实source与science scope，不用job success标签替代数值结论。

## 8. 生命周期、完整来源失败与清理

原 R508/R547 的 PID/pgid/sid/start_ticks、实际namespace与已登记或可疑owned进程规则未改。只有真实归属才可发信号；unreadable/unknown不凭同uid推成已静止。原动态worker registry、独立stage guard会话及closed过程保留。新source child不启动科学会话，返回记录真实；其失败不假造未来owner状态。

新 workflow 只有显式 `workflow_dispatch`，不加push科学触发；root是唯一发布/正式dispatch者。新独占namespace为：

```text
RUNNER_TEMP/visible-live128-root-reused-projected-model232
```

只有source必要scope和science必要scope都真实完整，才调用原runner.cleanup；cleanup仍亲核本run/source/request、namespace所有权与原实际quiet。数学失败本身不禁止在完整必要读回和quiet后按原规则清理；读回不全或quiet未证则不清。source metadata与临时展开文件仅保到本job需要结束，不刊科学raw、不上传大artifact、不向Git重复提交展开caller。

当前 R550 eligibility是局部执行选择，不是新lifecycle或科学门。原各接受布尔字段仅按原返回解释；本文既不把程序complete提升native/fullDN接受，也不把一个历史默认false自动解释成真实数值拒绝。

## 9. 完整实际 CLI 与输出位置

以下为新 workflow 已写入的真实argv合同。路径中的shell变量由原checkout与namespace步骤设置；命令展示不代表在本文形成时执行。

### 9.1 source准备与source必要读回

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_reused_projected_source_views.py" prepare \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r551-live128-root-reused-projected-model-complete-source-plan.json" \
  --plan-sha256 06acd58ff29dd4dee359341711174ae10897843984347833511be8faac82d124 \
  --computations "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/request232-source-preparation"

python -u "$VISIBLE_COMPUTATIONS/root_20261116_live128_reused_projected_source_views.py" readback \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r551-live128-root-reused-projected-model-complete-source-plan.json" \
  --plan-sha256 06acd58ff29dd4dee359341711174ae10897843984347833511be8faac82d124 \
  --computations "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/request232-source-preparation"
```

R550 child实际argv：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261116_accepted_root_evaluation_reuse.py" \
  --source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R550-accepted-root-evaluation-complete-source-plan.json" \
  --ancestor-source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$RUNNER_TEMP/request232-source-preparation/R550/source-binding.json"
```

此CLI只由source generator调用；真实owner使用已返回binding安装compiler，不能对R550 CLI成功结果补写compiler_completed=true。

source必要文件为 `RUNNER_TEMP/request232-source-preparation-necessary.json`；frame：

```text
BEGIN_R551_REUSED_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
END_R551_REUSED_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
```

### 9.2 原初猜恢复与唯一科学run

```bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_reused_projected_owned_run.py" prepare \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 1e1b37ac0184eea4111989cb080214fa734cabd7f8f16b1cf859bd9cec494fd5 \
  --namespace "$VISIBLE_BASE"

PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_reused_projected_owned_run.py" run \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 1e1b37ac0184eea4111989cb080214fa734cabd7f8f16b1cf859bd9cec494fd5 \
  --namespace "$VISIBLE_BASE"
```

`VISIBLE_BASE`是§8的232namespace，`VISIBLE_NECESSARY`是其旁边的`visible-live128-root-reused-projected-model232-necessary.json`。真正每call的owner/model/compilation/body路径沿原runner/同call合同产生，没有提前创建accepted现场。

### 9.3 原science必要与条件cleanup

```bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/root_20261116_live128_reused_projected_necessary.py" \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 1e1b37ac0184eea4111989cb080214fa734cabd7f8f16b1cf859bd9cec494fd5 \
  --namespace "$VISIBLE_BASE" --out "$VISIBLE_NECESSARY"

PYTHONPATH="$VISIBLE_COMPUTATIONS" python -u \
  "$VISIBLE_COMPUTATIONS/geometry_20261116_live128_reused_projected_owned_run.py" cleanup \
  --request "$VISIBLE_COMPUTATIONS/public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json" \
  --request-sha256 1e1b37ac0184eea4111989cb080214fa734cabd7f8f16b1cf859bd9cec494fd5 \
  --namespace "$VISIBLE_BASE" --summary "$VISIBLE_NECESSARY"
```

第二条只在§8已说明的两scope及quiet条件成立时运行。科学frame：

```text
BEGIN_REQUEST232_REUSED_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
END_REQUEST232_REUSED_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
```

原Actions的Python语法编译、Node `--check`继续在真实source生成后的402文件集执行。本文不在本地做这些检查，也不把它们升级成独立fixture或新的科学接受标准。

## 10. 发布件、历史metadata与结果边界

### 10.1 本次四执行/配置件

| 路径 | bytes | SHA-256 |
| --- | ---: | --- |
| `computations/root_20261116_live128_reused_projected_source_views.py` | 37196 | `c501c85b7ec9fe44b7d5642c49025dea57862b9bb482e656425a282c8eb86f10` |
| `notes/r551-live128-root-reused-projected-model-complete-source-plan.json` | 77676 | `06acd58ff29dd4dee359341711174ae10897843984347833511be8faac82d124` |
| `computations/public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json` | 91119 | `1e1b37ac0184eea4111989cb080214fa734cabd7f8f16b1cf859bd9cec494fd5` |
| `.github/workflows/visible-larger-public-live128-root-reused-projected-model-original-fullDN.yml` | 23242 | `1ab7875944747f7d8a25415c102c65e715b22c19c9838a2ef0fa1d464c71c7c2` |

十展开caller、两R550 includes及完整diff均是可由已绑定literal源重建的文本，不额外入Git。交接manifest只用于publisher准确路径→blob→bytes/SHA，不是科学输入，不另刊一份庞大展开目录。

新request中的历史 `source_contract` 和 R527/R534/R547 composition 重复说明，以完整原231请求身份及准确JSON pointer引用。实际source准备亲读该95286-byte原文件；新request保完整原387source值及全部原输入/参数。此做法只去除当前metadata重复文字，不删任何科学数值、失败地址或返回记录。当前 R551 composition 独立明确新request/source/roles/402集合，不能拿旧231 namespace当实际232现场。

### 10.2 可用条件结论

在固定源、真实准备与当前进程绑定均符合本文合同的公开Actions执行中：

1. 原387来源及全部原初猜/政策保持，实际只新增本文明确的15个source身份。
2. 原R547source-only准备不会运行旧科学owner；当前owner直接安装一次R550，实际g++和return由原main支付。
3. 正确的current-call键把真实128值与原声明projected64模型接到原消费者，不制造全128导数标志。
4. R550只在原接受之后复用同根下一主迭代的完整有限求值；所有原trial、最终数值门与后继消费者范围保持。
5. 完整旧/新RootStats、原failure/pending与实际source/install/compile各自进入原必要范围；source生成、返回计数、完成flag与数学接受继续分责。
6. 所有上限仍受原19200绝对钟与quiet/cleanup合同约束；本结论没有给出速度、内存、正文容量或任何数值完成保证。

尚未支付的事实是实际新compiler、复用次数、owner收敛/fresh replay、完整576stage/全338响应、FD/fullDN/末审计与实际必要容量。这些只能由未来actual232的真实返回形成R552。本文不把另一在跑入口的状态、某个原结果或source层条件结论代填给它。
