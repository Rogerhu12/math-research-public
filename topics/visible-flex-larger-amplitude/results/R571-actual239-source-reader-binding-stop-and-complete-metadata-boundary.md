# R571　actual239：当前 reader 名未同步导致初始化停止，科学未启动

**可信度：已证明（限官方终态、唯一两 job 日志直接返回的事实及所列固定源码控制流；没有本次科学数值结果）。**

作者：OpenAI / ChatGPT geometry agent（AI）。日期：2026-11-16。

actual239 在 step3 的 metadata initialize 中停止。R570 的 `form_current_inner` 已把首级必要 reader 改成真正捕获 cubic 的新来源，但同一 composer 的 `TWO_PHASE_READER` 常量仍是旧 `bound230` 名；`compose` 对四个 metadata source 名的严格集合绑定因此拒绝。真实错误为 ValueError，未到十一层源码 materialize，也未产生实际 job deadline、环境脚本或科学输入。

本次完整返回一份 **8894 B** 的 immutable source-preparation necessary，含该真实异常及全部相应来源元数据；它是该固定 metadata scope 的完整读回，不是全科学读回。原五primary、完整generation/refinement、same-C测量等均不可用。自有cleanup与原upstream cleanup均未调用，`raw_deleted=false`。

本次不更改冻结239或重派同一入口。独立后继只需修真实当前 reader 名及其真实来源级联，继续保原严格来源绑定；不删guard，不改原数学/资源/接受门，也不把本次未启动的capture或field作为父。

## 571.1　官方运行与读取身份

| 项 | 官方实际值 |
|---|---|
| repository | Rogerhu12/math-research-public |
| request | 239 |
| run | 43891863925 |
| attempt | 1 |
| event | workflow_dispatch |
| actual head | `e396395de8ed0c124cd481d85a32e795aa795812` |
| workflow ID | 420255317 |
| workflow path | `.github/workflows/visible-current-C-same-call-cubic-refinement239.yml` |
| created/run_started | 2026-11-16T15:00:58Z |
| updated | 2026-11-16T15:01:23Z |
| status / conclusion | completed / failure |
| compute | 133384932094 |
| report | 133385092157 |

[官方run](https://github.com/Rogerhu12/math-research-public/actions/runs/43891863925)；
[compute](https://github.com/Rogerhu12/math-research-public/actions/runs/43891863925/job/133384932094)；
[report](https://github.com/Rogerhu12/math-research-public/actions/runs/43891863925/job/133385092157)。

本负责人在官方jobs已显示两job终态后，各取一次日志；没有读取running日志，没有重复下载，没有读取另一run的scientific raw补本次。API实际返回的解码文本身份：

| 文本 | bytes | SHA256 |
|---|---:|---|
| compute | 120971 | `fb39b4754d8670716e7a754e9cf8c0e85c8ea676ce6e5a203430ec0342f9a85c` |
| report | 23460 | `2b6e55d5a7fc836c7b8dc4f922fb6194855f591a597afae657c72a95b38f4df2` |

这是本次实际解码UTF-8文本含BOM的身份，不是原压缩日志包。原日志、必要正文和runtime源副本仅作会话证据，不作为Git blob或artifact存储。本文件是作者结论。

## 571.2　实际冻结入口

本次R570/239五个直接运行入口身份：

| 对象 | bytes | SHA256 |
|---|---:|---|
| 当前request | 54783 | `6eb0b2572b8ef204b80e1c5d6172e902c0b37254d305f641cb11bef4f818812f` |
| actual source entry | 38204 | `27ef948f256d32994192e8fffb550add9697e69e92d7186c3eeb90f385db4a16` |
| 当前sampling/refinement composer | 76607 | `ebd89315edd17a1e9da8b49c73ec770e108213ef4f4c58d59ddaf0da92224d41` |
| 完整56输出plan | 71198 | `05513054b03e64c1d82c16db2458ec270e5364198dfa382c39fb81fed3128504` |
| 实际workflow | 91712 | `f49152d9f22af88a35be61056117e07de7cd2d0e54ac985599a42a900b3a8c4d` |

准确路径为：

- `topics/visible-flex-larger-amplitude/notes/current-C-same-call-cubic-refinement239-request.json`；
- `topics/visible-flex-larger-amplitude/computations/root_20261116_request239_actual_source_entry.py`；
- `topics/visible-flex-larger-amplitude/computations/root_20261116_request239_sampling_refinement_composition.py`；
- `topics/visible-flex-larger-amplitude/notes/r570-same-call-cubic-complete-source-plan.json`；
- §571.1所列workflow。

R570真实源闭包原计划为307 public+311 generated=618，十一层数量为15/5/13/49/51/46/57/6/6/7/56。本次该数字仅存在于完整冻结合同及已形成的metadata；十一层materialize未执行，不能写成“618实际生成及语法已过”。

新增bridge 24718 B/861a7d7b…、原R569修正后6d27库及当前same-C evidence都在冻结源合同中，本次没有进入其数值调用。

## 571.3　首个真实停止位置

compute step3调用：

`root_20261116_request239_actual_source_entry.py initialize`，

在原checkout明确绑定当前54783 B request，再创建原namespace及runtime metadata view。实际traceback指出：

1. entry 的 `initialize` 第405行调用当前 `C.compose(actual_request, base, comp, ...)`；
2. 工作视图中的当前composer第497行检查：
   `require(set(declared) == set(ADDITIONAL), ...)`；
3. 同源 `require` 第115行抛出 ValueError；
4. 实际message为：
   `Use the current composer and actual generated metadata readers`。

15:01:09.9316307Z 的 `request239_actual_source_metadata_view` 返回：

| 原字段 | 实际值 |
|---|---|
| actual_exit | 2 |
| completed | false |
| scientific_computation_started | false |
| actual_job_deadline | null |
| namespace_created_unix_seconds | 1794841267.4340913 |
| original_checkout_files_modified | false |
| raw_deleted | false |
| result.bytes | 7421 |
| result.sha256 | `ab7f79889e45c33008b1aedecf5879dc9900876fadbb100a7ec6401ebb9bfc44` |

result实际路径：

`/home/runner/work/_temp/visible-current-C-actual202-ten450-closed-geometry205/source-binding239/result.json`。

已写出的当前derived请求真实身份为106171 B、SHA

`a8f7df593bc527e06fd8bb9c217f282e5a0335786c94129e5087f57bd39fa901`，

路径为工作视图中的原220固定metadata路径：

`/home/runner/work/_temp/request239-runtime-metadata-workspace/topics/visible-flex-larger-amplitude/notes/current-C-coast-base-zero-linear-gzip-incremental-M-refinement220-request.json`。

它是本job形成的临时合同，不是原f6ca frozen220，也不是新科学结果。当前错误发生在它写出之后、实际derived205/composition/deadline形成之前。

## 571.4　确定的源码原因：两处实际 reader 名不一致

该首因可由本次已冻结源码和真实失败位置精确闭合，不需新试跑。

当前composer顶部仍写：

`TWO_PHASE_READER = "root_20261116_actual202_bound230_coast_base_zero_linear_gzip_two_phase_necessary_readout.py"`，

并定义 `ADDITIONAL=(ENTRY, BASE_READER, TWO_PHASE_READER, RULE_READER)`。这是四个真实metadata成员的完整名字集合，并非任意包含关系。

而同源 `form_current_inner` 先对 `roles`、`native_registration`、`current_BVP_readout` 做真实来源rebind；它随后遍历原222 metadata_sources，把每个descriptor按实际输出映射更新，并以更新后的 `row["file"]` 作新字典键。R570的first_reader真实新输出为：

| 来源 | basename | bytes | SHA256 |
|---|---|---:|---|
| 旧基线reader | `root_20261116_actual202_bound230_coast_base_zero_linear_gzip_two_phase_necessary_readout.py` | 31492 | `fecdc98d02fb420fa3146c1af197304cab199d798a119a1b15bce37dbefbfbbc` |
| 当前capture reader | `root_20261116_actual202_captured239_coast_base_zero_linear_gzip_two_phase_necessary_readout.py` | 32662 | `508885ca68dc0500a8bd5923b2cfb90746ebb118bc4fd25a83cb5160d153a7e9` |

因此，实际形成者把该键改为新 `captured239`，消费集合仍要求旧 `bound230`，两集合必不等。ENTRY、BASE_READER和RULE_READER另三个名字不提供把此差异消除的别名；不能在新dictionary偷偷加旧名指向新source，因为那会损坏真实basename/identity合同。

上表及其映射是固定源码推出的来源事实，不冒称原log额外打印了106171 B derived请求全文。实际error、调用点及新derived身份则直接来自本次日志和完整必要metadata。两类证据在此一致。

这不是requested_parameter_domain、原C族、coast点、浅逆采样、cubic多项式、tube正域、relative metric或native接受的拒绝。也不是234那条两worker sampler schema问题；当前239仍用原单worker来源。正确后继应令composer严格绑定它自己实际产生的新reader，而不是把guard删除或将任何未知source算作允许。

## 571.5　工作视图、唯一时间起点与祖先来源

step35返回的完整metadata明确：

- primary_checkout：`/home/runner/work/math-research-public/math-research-public`；
- actual_working_view：`/home/runner/work/_temp/request239-runtime-metadata-workspace`；
- original_namespace：`/home/runner/work/_temp/visible-current-C-actual202-ten450-closed-geometry205`；
- original_clock_restarted=false；
- original_python_javascript_bytes_modified=false；
- original_checkout_files_modified=false；
- original46_generated_output_bytes_modified=false；
- raw_deleted=false。

这里original46未改是来源副本合同，不能据此说46新generated已在本job生成。实际materialization步骤仍skipped。

namespace-start文件身份为702 B、SHA

`ea9a7325671b2c42f3c0d8775d36d593b206ddc900f38e8159661d7c40b56ce8`，

file为 `source-binding239/namespace-start.json`。它保存初始化的唯一原起点；本次job-science-deadline仍null，不能从起点存在推出原science clock已经启动并用尽。

当前source-copy记录为：

| 字段 | 实际值 |
|---|---|
| files | 2868 |
| bytes | 56042811 |
| copied_source_files_are_not_scientific_results | true |
| complete_copy_index.bytes | 568115 |
| complete_copy_index.sha256 | `d12122a37ccd27c83b4276f67019ea28eee3c71bd3f20bfa6853ae30bdc094dd` |

其范围是checkout普通文件（不含.git）；完整index仅临时身份，未在必要正文展开。复制的源码不是科学raw，不构成accepted父或数值重生。

完整metadata保原祖先身份：

| 对象 | bytes | SHA256 |
|---|---:|---|
| 原frozen220 request | 99218 | `f6ca63871733d3f5e48ef3eb8d540fc137806ceb1ae74cef01af6b21e25f3aba` |
| 原frozen220 workflow | 94508 | `c1cb332dc9bd9b9b2c0b94b94477152c55d4448323dbd32f6b727142ae39524f` |
| 原220 plan | 66325 | `14970cc2fea0f5245218ae0752e5659747a69d6d5a22d25252fe166a48c7a786` |
| 实际222请求 | 9442 | `37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672` |
| 原222修复plan | 66182 | `7a74a8e65b7283bfe9acb36a27a38dbef01e8ee0507eff0ac4c3548015288ddf` |
| 已形成repaired222合同 | 99330 | `2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2` |
| R503 explicit政策JSON | 18919 | `2f6113ce7b1928d2954d8768d2117db4452abf89cbb7f2f8b1a57719228e9dd3` |

原220四outer副本也保原身份：composer47343/f3e8ce8e…、owner25670/4afc0135…、runner48824/7dbc1dc3…、reader42493/e887a1ce…。它们是实际源复制中的祖先，不能与当前239 caller混同。

## 571.6　唯一完整返回的 necessary scope

15:01:11.1963170Z 至15:01:11.1998417Z，compute实际打印：

`BEGIN/END_REQUEST239_ACTUAL_SOURCE_BINDING_NECESSARY`。

其schema：

`request239-current-C-source-binding-entry-v1-necessary-v1`。

正文准确 **8894 B**，SHA256：

`03f334935a1f3b4795aa6b955123981c4d990eca89f69ad11eda0f5af28a7d1c`。

实际顶层字段全部责任如下：

| 字段 | 返回内容/语义 |
|---|---|
| actual_entry_request | 当前54783 B request的真实路径/完整SHA |
| actual_source_preparation | 当前7421 B result文件真实路径/完整SHA |
| complete_necessary_readback | true |
| complete_original_source_preparation_metadata | 完整原metadata对象 |
| immutable_source_metadata_only_no_process_quiet_claim | true |
| mathematical_success_not_inferred | true |
| namespace_start | 702 B原起点文件完整身份 |
| raw_deleted | false |
| repository/run_id/source_commit | 本次准确repo/run/head |
| source | 当前38204 B entry真实路径/完整SHA |
| source_copy_index_full_payload_not_exported | true |

完整内层对象中，`completed=false`、`scientific_computation_started=false` 和首ValueError/完整traceback均保。下列项是实际null：

- actual_composition；
- actual_derived205；
- actual_job_deadline。

其余当前derivedrequest、original/repaired合同、policy、工作视图、namespace/sourcecopy、四outer来源、当前source计数合同均按原返回对象保。它没有把null写成空成功对象；没有声称当前56caller文件已生成。

`complete_necessary_readback=true` 仅说明这个immutable初始化metadata的完整选择范围已读回。step35成功不包含科学summary、全generation ledger、同C四场、process quiet或最终cleanup。不得把这个true拿去替其他失败scope的marker。

## 571.7　后续失败是未形成环境的级联，非科学反例

step3错误后，setup Python/Node、runtime安装、容量、十一层materialize、完整源绑定/同C登记、原输入与公共源恢复、完整C cover等原前置步骤均为skipped。

后续部分原 `always()` step仍按既有策略尝试错误/必要读回。实际runtime-env脚本未形成，因此出现：

- `KeyError: 'VISIBLE_COMPUTATIONS'`；
- `KeyError: 'VISIBLE_BASE'`；
- `ModuleNotFoundError: No module named 'root_20261114_current576_rules_runner'`；
- source `request239-runtime-env.sh` 的“No such file or directory”。

这些报错发生在读取当前环境或导入原wrapper之前；不是full far、native、FD、453、450或geometry的数学调用返回。不能把step16–28的failure标签解读成这些科学对象都计算过并被原门拒绝。

同C first/successors与refinement science步骤29–31均skipped；没有头部重算、mesh重求、M128 union、metric、held、display或cubic capture的实际结果。R569、R553、R575的任何新常数也未形成。

## 571.8　各必要scope的实际缺失

compute返回 `request239_generation_scope_unstarted`，reason为：

`actual_source_entry_did_not_form_runtime_environment`，

并明确complete_necessary_readback=false、raw_deleted=false。这里不是原readback deadline耗尽；日志中同名脚本的另一个候选reason只是回显的源文字，未实际触发，不能混入结论。

report五个primary都逐一返回 `request205_primary_unavailable`：

| original_kind | 实际状态 |
|---|---|
| scalar_summary | unavailable |
| cut_twojet_summary | unavailable |
| far_summary | unavailable |
| construction_summary | unavailable |
| bvp_summary | unavailable |

这五行都保compute_result=failure、BVP_outcome=failure、no_native_BVP_or_upstream_success_inferred=true。其 `request205_report_transport_scope.errors=[]` 仅意味着report自身逐项解析没有额外异常，不意味着五个原primary存在。

report还返回：

- generation scope unavailable，actual_outcome=failure；
- refinement primary unavailable，science_outcome=skipped、readback_outcome=failure；
- closed_postsolve scope的science_outcome/readback_outcome均failure、necessary_summary_identity=null；
- same-C必要身份为null。

same-C report的完整outcomes为prepare=skipped、first=skipped、successors=skipped、readback=failure、composition=failure；repair_scope_outcome=success仅对应§571.6的immutable entry readback。

原report代码中“完整新正文在compute日志”是固定scope说明；本次真正科学body没有打印，不能凭这一静态布尔补出不存在的body。所有缺失原对象都保持未返/未启动，不能用source SHA或seed构造科学checkpoint。

本次没有90000 B超限事件。8894 B metadata确适配，但它的范围很小；不能据此证明未来十一层完整source或全部capture/evidence必要会适配。

## 571.9　真实清理路径

step38调用当前entry的 `guard-cleanup`。由于runtime-env未形成，调用仍在原checkout scope；guard拒绝将其冒作实际239 computations/view。实际事件为：

`request239_cleanup_skipped_before_generated_entry`。

返回：

| 字段 | 实际值 |
|---|---|
| error.type | ValueError |
| error.message | Use the actual239 computations for guarded cleanup |
| actual_generated_cleanup_not_called | true |
| original_upstream_cleanup_not_called | true |
| raw_deleted | false |
| process_quiet_not_inferred_from_metadata | true |

完整traceback保entry第560行实际comp/view的严格绑定失败。该错误是初始化未完成后的清理scope分责，不是新科学失败。原自有删除函数没有调用，不能写“cleanup成功”。平台post-job清理也不替代这个明确的自有结果。

本次没有科学owned进程启动记录，也没有用metadata猜quiet；保持原未知scope不准cleanup的合同。已复制的metadata/source临时视图按runner生命周期处理，本结论不保证该runner后续可恢复。

## 571.10　最小独立修复的边界

真实断点已足以提出可行动的下一源修复：

1. 在独立新composer中，将完整四成员集合的首级reader绑定为真实 `captured239` 输出；
2. 保严格set相等、basename/descriptor、完整bytes/SHA和actualHERE检查；
3. 保旧239源码与请求为完整祖先，不覆写已经运行的文件；
4. 对新的public composer/entry和真实外层调用者做必要source/manifest/请求身份级联；
5. 仍真正执行原56view及全部旧557来源，不跳过任何数学前置；
6. 原C/root/十词、单worker浅逆采样、完整far、原453→450、五factor/M128、所有J/FD/final、同g/全t/geometry责任与原18900+2700钟全部保留。

这是metadata consumer与producer名字一致性的修复，不应假造旧名字作为新source的别名，也不应把set断言改成宽松包含或删掉。新源只能宣称源码接通；是否还有后续来源或资源问题，须由其实际运行说明。

原239未启动capture，因此没有可复用的当前cubic、准确quintic、accepted450或measure对象；后继必须从完整既定子合同重新进行实际科学。本次不重启冻结239，不加入fixture/审计或更严数学门。R575实际projection估计的独立后继责任仍保，不能借本次初始化修复宣称它已调用。

## 571.11　最终事实边界

本次已确认的进展是：原source元数据可被完整复制、原222修复合同可形成、当前239 inner合同已写出、初始化的完整失败scope可以在8894 B中返回。实际失败是composer对首级reader名的旧常量遗漏，定位于真实producer/consumer的明确集合差。

本次没有生成完整十一层新源，没有科学runtime初始化/输入恢复，没有C、far、453/450、native、FD、cubic capture或几何测量结果。完整初始化necessary的成功与其他所有scope的缺失、cleanup未调用分别记录；不混为数学否定或实验完成。

作者只做终态官方元数据/两日志唯一读取及已冻结源的文字定位；不运行本地科学、AST、编译、fixture或独立验证门。此完整作者结论可立即登记，随后用独立新来源支付已定位的工程断点。
