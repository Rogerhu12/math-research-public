# R563：actual236 的真实 dyadic 来源与双必要正文未返回

作者：ChatGPT（AI，amplitude 协作代理）。日期：2026-11-16。

**可信度：已证明（限下述独立官方终态、实际返回字段及固定源码的读回/生命周期解释）。本次完整科学必要正文没有返回；当前 H、owner/replay、R561 路径统计、全模型、FD/fullDN 的数值状态和具体内部错误均不能据本文补齐。**

actual236 真正完成了来源生成、417项完整源绑定和原输入准备，随后原 science/rules/外层均返回1。来源必要对象225803B、科学必要对象177614B分别超过原单90000B上限，两者都真实返回70；compute与report实际传输的只是1813B和1130B的两个不完整对象。原runner选出的owned静止字段true，外层resource_stop=null、external_signal=null；cleanup实际removed=false。本文来自本次两原终态日志各一次，不用actual232或任何其它run代判。

## 1　实际run、源码和唯一读取

| 项目 | 本次实际值 |
|---|---|
| 仓库 | Rogerhu12/math-research-public |
| workflow | .github/workflows/visible-larger-public-live128-root-dyadic-projected-model-original-fullDN.yml |
| workflow ID | 420141317 |
| run / attempt | 43873389241 / 1 |
| event / branch | workflow_dispatch / main |
| 实际head/source | e6d389dfe1f79669f5b616497dc91bf92a70637d |
| created_at | 2026-11-16T13:11:18Z |
| updated_at | 2026-11-16T14:55:14Z |
| run终态 | completed / failure |
| compute job | 133320084785，completed / failure |
| report job | 133381236270，completed / success |

[官方run](https://github.com/Rogerhu12/math-research-public/actions/runs/43873389241)；[固定来源](https://github.com/Rogerhu12/math-research-public/commit/e6d389dfe1f79669f5b616497dc91bf92a70637d)。

15:03:59 UTC自然jobs轮询看到两job已终态，作者随后唯一获取两原日志各一次。此前只取元数据、没有running logs；没有重复读取actual232或祖先231的原日志，也没有追加科学运行、AST、编译、fixture或测试。

下表只是connector已解码返回文本的UTF-8重编码identity，**不是HTTP原字节、压缩ZIP或服务端raw日志identity**：

| 返回文本 | bytes | SHA256 |
|---|---:|---|
| compute 133320084785 | 75362 | 1d1757a0fbc8f8e9b615e90b4b45b11d6b14156141539e7f0ff00324aa696574 |
| report 133381236270 | 17546 | 22aa531873a387a49a10f45af5b4f625fafc857bed33d1ef83ab509a810d9e84 |

实际日志/necessary/raw只在当前读取上下文缓存，没有为交接创建Git blob或仓库raw文件。本文是作者逐项归责说明，不复制未返回大正文。

## 2　冻结入口与本次数学合同

完整来源和条件接口见 [R562](R562-request236-exact-dyadic-average-and-complete-projected-model-entry.md)。本次五件中四个执行入口身份：

| 文件 | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_live128_dyadic_projected_source_views.py | 37603 | 0f984347d801b3b8132b7814494b3f883f72ef1bd73d00aa15d01b767c2de85c |
| notes/r562-live128-dyadic-projected-model-complete-source-plan.json | 64999 | a72e2d5a225a977c6eec7d3f7d65066b102a405b1362af5b855d38495b8c4780 |
| computations/public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request.json | 97937 | 299cf5532e510c3629354347d1ba03aa57135077a1530b605867b0f71e08cb45 |
| workflow（第1节完整路径） | 23459 | b683e42765e1ca758ddf8d189fbb501057f733e5dcc920594a9e9878ea082b66 |

原232的351公开/51生成共402项完整保留。本次增R561两公开源、两个完整include、一个当前generator、十个caller，实际并集 **354公开+63生成=417项**。JSON计划与八个原数学/资源对象、lanes照原完整绑定；源数是实际闭包数量，不是原科学调用数。

| 当前生成角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| owner | geometry_20261116_live128_dyadic_projected_same_call_owner.py | 25904 | 2b2070afb87813910f6422600a63c80d16c0f551897b2e23ab4b2b3497a80dbd |
| runner | geometry_20261116_live128_dyadic_projected_owned_run.py | 39356 | 97e639c3f98f212fb78e3b8f3420063b17412bc3df39035b6b4e63f161e22764 |
| reader | root_20261116_live128_dyadic_projected_necessary.py | 61330 | 3bda6213246c10163519c9067b85c570fe947f96411b97a459c406fabb95cee1 |
| primal include | root_20261116_exact_dyadic_average_primal128.cpp | 26420 | 0e01b54b3b456711efd23ba94961eb669aef5394ab848e720fcf4a4ac64c854f |
| trace include | root_20261116_exact_dyadic_average_trace128.cpp | 35787 | 07b8fd4dd7d31b2728e0f74a3ed9c9e6653593376529c12d26cdb57d617b8dc5 |

[R561](R561-exact-normal-dyadic-average-and-original-first-products.md)的唯一算术增量是原primal residual/root_gram/primal_flux三个角向末乘法：**原首乘积仍真实计算**；当实际N=2^k、inverse词准确，且product及缩放后均为normal或product为±0时，按原字准确调整指数或保±0，其余调用原product*inverse。原累加顺序、所有方向算术、原试步、主solve/replay、当前模型及末门不变。trace只传真实stats到新primal root_matrix，不把direction正文替成另一算法。

实际原owner scope应直接安装R561一次，R550/R535只source-only，不能先安装旧hook再装新hook。这个编译/安装合同不能从本次来源生成0推成实际编译已完成。三个path各10项计数及full last、R550 primal/trace完整复用统计、整RootStats未知字典与实际compilation本来由reader完整选择；本次科学正文未回，因此这些具体值全部未知。

诚实模型guard沿232新字段 same_call_complete128_value_components_and_explicit64_linear_model_required，不补旧全128导数声明。128当前state/value/fresh replay仍是权威；once-RN64真实state上同DN engine形成完整576单元226×224、224×224及两mean模型，再精确lift存储；338×112物理消费者仍按原混合导数合同。没有新增全解析J或数值shadow门。

原112/112、576/577、全部224方向、226局部状态/双mean、338输出、32×10及2e-9、完整FD方向/三层/原Richardson和5e-5门、原prefix/fullDN全部门不改。总科学19200秒、120秒读回reserve、350分钟job/320分钟科学step、4线程、每call factor19200/owner6000/replay1200/stage8000/boundary600/endpoint600/audit1800均原样；各cap只限制当前剩余原钟，不预付完成或重启时钟。

## 3　实际步骤表

| 步骤 | 官方结果 | 已支付范围 |
|---|---|---|
| 1–6实际环境/运行时 | success | 原准备步骤返回 |
| 7完整232祖先+R561当前来源 | success | complete=true、actual_exit=0及真实source record identity |
| 8全source/request绑定 | success | 417项当前源、request/head；原Python编译检查、Node syntax-only |
| 9启动容量 | success | 本步骤实际free大于原64GiB门 |
| 10输入准备 | success | preparation返回complete/phase/error |
| 11原科学 | failure | 三个实际退出码均1；内部error未返 |
| 12source必要 | failure / 70 | 225803完整对象超限，1813不完整返回 |
| 13science必要 | failure / 70 | 177614完整对象超限，1130不完整返回 |
| 14清理 | success | 真实保留分支removed=false |
| report两必要步骤 | success | 原样转运两个不完整小对象 |

第8步事件明确Python_compiled_not_imported=true、Node_syntax_checked_not_executed=true、no_CXX_scientific_compilation_or_scientific_evaluation_yet=true。该步骤通过不能证明owner C++ compiler、当前call或R561分支已经实际执行。

## 4　实际来源生成、原输入及容量

令以下缩写仅表示本job原日志中的真实路径：

- C=/home/runner/work/math-research-public/math-research-public/topics/visible-flex-larger-amplitude；
- T=/home/runner/work/_temp；
- B=T/visible-live128-root-dyadic-projected-model236；
- S=T/request236-source-preparation；
- A=T/request232-source-preparation。

A是本job真正重生的232子合同临时目录，不是旧actual232磁盘或科学状态。

13:11:44.5843463Z，R562_source_preparation_return：

| 字段 | 原值 |
|---|---|
| complete / actual_exit | true / 0 |
| actual_source_receipt.file | S/source-views.json |
| bytes | 137494 |
| SHA256 | 3ed55d5aa507a4cb1fb17e59c1eb6fd5fafb55d28ea425cb4bd35d62994d854c |
| science_success_inferred | false |

request236_source_binding随后原样返回sources=417、当前request完整SHA及e6d389df完整head。137494字节原record没有整体回到作者；只使用这一真事件和identity，不把原生成后缀/所有安装字段从SHA复原。

13:12:08.8624878Z，request236_preparation_return：

| 字段 | 原值 |
|---|---|
| complete / phase / error | true / "complete" / null |
| actual.file | B/preparation.json |
| bytes | 79042 |
| SHA256 | b4baa3dc9105866f094a26cca673f92110f46685b0e20207b5036d67b5bdc4ea |

原actual63 prefix、actual91 tail仍只作重新构造当前问题的初猜，不继承其J、接受或owner缓存。

启动容量before与after相同：total154993672192、used62959800320、free92017094656字节；原minimum_free_bytes_at_start=68719476736。原事件还保unused_ephemeral_runner_SDKs_removed=[]、scientific_payload_deleted=false、maximum_uncached_protocol_calls=18、all_possible_calls_fit_not_proved=true及original320_minute_clock_not_started_yet=true。没有据此承诺18次调用都容纳、科学末尾剩余磁盘或完整预算可完成。

## 5　原科学return已知，内部stop原因未知

14:55:02.7208892Z，request236_actual_science_return：

| 字段 | 实际值 |
|---|---|
| actual_exit_code | 1 |
| rules_returncode | 1 |
| science_returncode | 1 |
| resource_stop | null |
| external_signal | null |
| owned_processes_quiescent | true |
| execution.file | B/execution.json |
| execution.bytes | 2584 |
| execution.sha256 | c26cc4a0b94f17001fac2ef6879f00f819cf8ec5c9399f7d5bbf1eaeec65ae55 |

原runner在finally作owned静止、wait原rules child并读取真实rules result，然后写execution.json和上述事件。该事件并不携带全部error/traceback、call目录、原stderr、owner/replay状态或门结果。

因而这里的resource_stop=null不能排除子层的独立cap或错误；science1也不是数学拒绝标志。本文不把两时间戳之差当owner6000计时，不借actual232/229/231/225的已知错误解释本次。owned_processes_quiescent=true只按事件所记录的实际范围承认，不替科学必要读回或最终删除。

本次未返回：当前H/高度、实际call数量、owner是否启动/接受、完整root统计、R561三path资格/hit/fallback、g++/compiler安装、final/replay、全stage模型、boundary/endpoint/audit、FD每方向/层、fullDN实际迭代/最终接受及所有partial/未访地址。缺字段不等于false或0，也不能用已生成源的条件正确性补实际结果。

## 6　来源225803B超限，完整祖先重选事实与未返范围

source frame：

~~~text
BEGIN_R562_DYADIC_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
END_R562_DYADIC_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
~~~

compute/report两frame body逐字相同，包括末LF为 **1813B / c9028eadeeeef4873fe62edbcae0c6153e34ce72905b398bba0ac6f61b91b9bf**。独立event返回actual_reader_exit=70、necessary_readback_complete=false、scientific_success_not_inferred=true。

完整小对象schema为R562-root-dyadic-current-owner-projected-model-source-preparation-v1-necessary-v1、request_number=236；run四字段是本仓库/run43873389241/attempt字符串"1"/实际e6d389df完整SHA；source及plan分别为第2节37603/0f984347、64999/a72e2d5a。

| 已返回字段 | 原值 |
|---|---|
| attempted_bytes | 225803 |
| attempted_sha256 | 74e483d2859105c17e8cbcd56d59cdc877c32153793ed3d7fcebb11a9531dc3a |
| complete_local_necessary_object.file | S/necessary-source-overflow.json |
| 该文件bytes/SHA | 同上225803/74e483d2完整值 |
| necessary_readback_complete | false |
| source_preparation_complete | false |
| transport_exit_code | 70 |
| cleanup_permitted | false |
| no_segments_or_encoded_raw | true |
| numerical_success_not_inferred | true |

source_preparation_complete=false仍是R562超限分支固定新建小对象的字值；它不抹掉第4节实际complete=true/exit0，也不能被第4节的true回填为必要完整。不得把本次来源准备阶段错归为failure。

旧R551同job子读回返回的完整identity：

| 原字段/实际路径 | bytes或退出码 | SHA256 |
|---|---:|---|
| original_R551_readback_exit | 70 | — |
| original_R551_transport：T/request232-source-preparation-necessary.json | 1818 | bcc94b2fcaed1ad40d02ff79ff7026a11650f12a7721b5e99deb4c800c363035 |
| original_R551_complete_necessary：A/necessary-source-overflow.json | 169036 | 2c713a96906a2c7eef02737e96f542703da3c473afc46e8ba71b2cb08a34bfaa |

沿固定R562.readback：实际调用原R551 reader；对子70分支保其false，严格核固定A/necessary-source-overflow.json真实file/bytes/SHA、attempted bytes/SHA，再完整读JSON并核同run/source/plan，才填这份complete identity。接着新层用具名完整逆来源表选择原完整范围和当前R561 source binding。这里付的是**同job原大对象确被真实绑定后再选**，不是作者已收到该169036正文，也不是新225803已回。

这个169036与actual232/R552的对象长度恰好相同，SHA不同；它是本次新run里的来源子合同，不可以贴旧body或当旧run的输出复用。225803实际全文没有返回，其分字段占用未返回；不能据该总数猜具体递归binding、inventory或stderr贡献，也不能把overflow descriptor当旧完整body。

## 7　科学177614B超限，全部selected责任仍未返回

science frame：

~~~text
BEGIN_REQUEST236_DYADIC_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
END_REQUEST236_DYADIC_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
~~~

compute/report中的小body同字，包括末LF **1130B / 16e0a053c20a2d4347ee3859be96745b48fee13a391c321c89df0ed64736ae1e**。actual_reader_exit=70，necessary_readback_complete=false，scientific_success_not_inferred=true。

| 字段 | 实际值 |
|---|---|
| schema | R562-live128-root-dyadic-projected-model-original-full112-necessary-v1 |
| request_number | 236 |
| request.file | C/computations/public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request.json |
| request.sha256 | 299cf5532e510c3629354347d1ba03aa57135077a1530b605867b0f71e08cb45 |
| run | 同第6节实际四字段 |
| actual_original_necessary_summary.file | B/necessary-summary-overflow.json |
| actual_original_necessary_summary.bytes | 177614 |
| actual_original_necessary_summary.sha256 | 725222a6828b7fa694183115ae61510817ee26b4a03ef80e1f5a1af44000e0ee |
| necessary_readback_complete / transport_exit_code | false / 70 |
| cleanup_permitted | false |
| scientific_success_not_inferred | true |
| no_segments_or_encoded_scientific_tree_returned | true |
| unreturned_scope | 完整selected necessary对象超90000，科学与错误内容没有改为成功view |

固定reader仍先绑真正request/caller/source/namespace并调用原quiet，再选完整preparation/execution/deadline、orchestration、同clienthandoff、所有真实call目录、原affine FD/fullDN、rules、原stderr、file receipts和metadata errors。原八类具名共享保完整RootStats/compilation/安装记录，未知新增dict并不删除。R561三条path的各10计数与full last本来在整RootStats范围内。

但原main在完整canonical对象超过90000时，先写上述B/necessary-summary-overflow.json，再真实用这份不完整小对象返回70。因此**选择合同完整，不代表本次传输完整**。本次只回177614的identity，没有回它的necessary_readback_complete、metadata errors、fullDN_accepted或任一stage内容。也不能把源码里初始化的false当实际原门拒收。

所有原失败地址、已做/未做component范围应由未返正文提供；本文不猜一个全未起列表，也不凭文件总长度猜内部已运行到哪。没有截断成功摘要、额外分段、通用数值编码或新读回路径绕过90K。

## 8　report与清理

两个report步骤重新核小对象的真实schema/run/source/request或plan/bytes/SHA后打印相同body。最后request236_report_identity保compute_result="failure"与scientific_success_not_inferred_from_job_label=true。报告success只指实际小body转运成功，科学和来源两个不完整都保留。

source与science必要步骤原本各自always，因此第12步70没有跳过第13步。清理则要求两个necessary完整标志同时true；本次二者false，14:55:03.9329838Z原request236_cleanup实际给：

~~~text
removed=false
namespace=/home/runner/work/_temp/visible-live128-root-dyadic-projected-model236
reason="source or original-science necessary scope incomplete; raw retained until runner destruction"
no_scientific_completion_or_quiet_inferred=true
~~~

故第14步success意味着保留分支正常完成，不是删除发生。没有调用基于完整必要正文的删除分支，没有从quiet推readback完整；临时raw保留到runner销毁不等于今后仍能按SHA取回。本文没有下载/入Git这些可再生raw，也没有声称未来可以从摘要重建owner状态。

## 9　独立实际结论及后继边界

本次实际付款是：R562源准备0、417当前绑定、原prepare完整、科学/rules/outer1、source225803→1813/70、science177614→1130/70、runner所选quiet=true、外层两个stop字段null、cleanup明确false。每项都来自actual236自己的原返回，不是与actual232相似就代入。

本次仍不支付R561优化分支的实际资格/执行数量、性能效果、原128接受/重放、同DN模型完成或任一FD/fullDN末门。不能说优化被数值拒绝，也不能说所有数值计算成功后仅报告失败；两种推断都超出返回范围。原有限词条件证明继续按其明确前提成立，不由source事件替代真实compiler或数值证据。

后继必要表示应从新的真实同job全部selected文件保留原值、缺失/null、数值类型和位、完整失败/partial/未访责任，在同90000/70约束内作明示具名可逆共享；不能把本次未返正文当手头fixture、伪恢复祖先或删字段以保证适配。已在跑237/240的结果也必须等待其自身终态，本文不预判其容量、错误或接受。

本文不修改actual236，不追加原门、不派重复实验、不以额外审查/数值测试延后结论登记。本次两原日志均已由唯一读者各取一次，之后只引用本结论及已返回identity。
