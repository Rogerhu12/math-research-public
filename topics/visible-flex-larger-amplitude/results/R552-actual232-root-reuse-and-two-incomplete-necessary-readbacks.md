# R552：actual232 的真实来源生成、双必要读回超限与科学结论未返回

作者：ChatGPT（AI，amplitude 协作代理）。日期：2026-11-16。

**可信度：已证明（限本文逐项记录的官方终态、已返回必要对象及固定源码控制流解释）；actual232 的完整科学必要正文未返回，不能据本文判定当前 H、owner/replay、模型或原 FD/fullDN 的数值结果。**

本次 actual232 确实完成了来源生成、402 项真实源绑定和原输入准备，并调用了原科学入口。随后实际 science/rules/外层退出码均为 1。来源必要正文 169036 字节、科学必要正文 144265 字节各自超过原单份 90000 字节限制，分别真实返回 70；公开日志收到的是 1818 字节和 1130 字节的两个明确不完整对象。报告 job 只是原样转运这些小对象而成功，没有把 compute 的 failure 或必要读回的不完整改成数学成功。

原 runner 返回 owned_processes_quiescent=true，resource_stop 与 external_signal 均为 null；这只限定它实际选出的生命周期字段。具体内部错误、调用数、RootStats、接受状态及原末门结果均没有随科学必要正文返回。清理步骤实际选择 removed=false，保留临时 raw 到 runner 销毁；没有删除成功，也没有额外读取、重算或借其它 run 补结果。

## 1　唯一实际运行和终态来源

| 项目 | 实际身份 |
|---|---|
| 公开仓库 | Rogerhu12/math-research-public |
| workflow | .github/workflows/visible-larger-public-live128-root-reused-projected-model-original-fullDN.yml |
| workflow ID | 420125932 |
| run / attempt | 43870893094 / 1 |
| event / branch | workflow_dispatch / main |
| 实际 head/source | 42492b0c728e260b3b1de8be79b4ab962259ad3e |
| 官方 created_at / run_started_at | 2026-11-16T12:55:05Z |
| 官方 updated_at | 2026-11-16T14:47:44Z |
| run 终态 | completed / failure |
| compute | 133311483693，completed / failure |
| report | 133376482266，completed / success |

[官方 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43870893094) 和 [固定入口提交](https://github.com/Rogerhu12/math-research-public/commit/42492b0c728e260b3b1de8be79b4ab962259ad3e) 是本次实际来源。不得用 R550 的组件发布头、R551 的作者草稿、231 或后继236/237/240的运行头替代它。

作者此前只作低频 jobs 元数据观察。2026-11-16 14:50 UTC 官方两 job 已终态后，作者分别获取了这两个 job 的原日志一次；没有取运行中日志，没有重取本次或祖先科学日志。正文依据已经缓存的这一次返回作文本/JSON/字节核对，没有本地科学执行、AST、编译、fixture 或额外数值检查。

两份 connector 返回的是已解码文本。以下 identity 是该返回文本的 UTF-8 重编码身份，**不是 HTTP 原始字节、GitHub 压缩包或服务端 raw log 的身份**：

| 唯一日志 | UTF-8 bytes | SHA256 |
|---|---:|---|
| compute 133311483693 | 75167 | 624afb6fb1295704e0a986fbd57d34d59ee3a16f283674d37d823e72bfbcd9a6 |
| report 133376482266 | 17560 | 12211e48c41d9de1022526e9b5d529a59463fa37257e81a09186870576951ebc |

日志和实际 necessary/raw 只保在本次临时读取上下文，不作为 Git blob 或仓库交付物保存。本文是独立作者结论，不是原日志或未返回大正文的复制品。

## 2　冻结的实际合同与本次来源增量

本次入口完整条件来源为 [R551](R551-request232-accepted-root-reuse-and-honest-projected-model-complete-entry.md)。实际执行件：

| 文件 | bytes | SHA256 |
|---|---:|---|
| computations/root_20261116_live128_reused_projected_source_views.py | 37196 | c501c85b7ec9fe44b7d5642c49025dea57862b9bb482e656425a282c8eb86f10 |
| notes/r551-live128-root-reused-projected-model-complete-source-plan.json | 77676 | 06acd58ff29dd4dee359341711174ae10897843984347833511be8faac82d124 |
| computations/public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json | 91119 | 1e1b37ac0184eea4111989cb080214fa734cabd7f8f16b1cf859bd9cec494fd5 |
| workflow（第1节完整路径） | 23242 | 1ab7875944747f7d8a25415c102c65e715b22c19c9838a2ef0fa1d464c71c7c2 |

完整并集是 351 个公开源加 51 个实际生成源，共 402 项。原231的348公开、39生成共387项全部保；新增 R550 两公开/两 include、一个新 generator 和十个当前 caller。生成全文没有另入 Git，原计划逐 literal/count/完整输出 SHA 绑定。

三条本次最直接的实际生成入口为：

| 角色 | 实际 basename | bytes | SHA256 |
|---|---|---:|---|
| runner | geometry_20261116_live128_reused_projected_owned_run.py | 39356 | 39712ee8fde3f75299dfced1a699e65a8ae790a472f406761fc03fd68e619079 |
| owner | geometry_20261116_live128_reused_projected_same_call_owner.py | 25821 | ea354ba982e6904fc43e552f1d75e2171130e0d4c04e4a1a2c2aaf67d392923c |
| necessary reader | root_20261116_live128_reused_projected_necessary.py | 60620 | 25c2f0937b430ec71c9734296ff79c051e8cc705c1040a31f6211acac16b0318 |

R550 组件保原同根、同次已接受完整 RootEval 到下一迭代的条件复用，祖先 R535 仅 source-only，实际 owner scope 由新 hook 直接安装一次。完整所有试步、原接受式、32×10、容差和原 final/replay 权威不变。源已生成不等于该 hook 实际安装或 g++ 成功；编译/安装正文恰是本次未返回科学范围之一。

R551 还把 system 的 guard 改为真实 current_call 字段：

~~~text
same_call_complete128_value_components_and_explicit64_linear_model_required
~~~

它没有填旧 same_call_complete128_final_components_required=true 来冒完整128导数。实际原128状态、residual、replay仍是权威；完整576个单元的226×224/224×224及两2×224 mean模型在实际owner状态一次 RN64 后、同一已加载 DN engine 上重算，再按精确 IEEE64→128 lift 存储。原112 boundary、mixed338×112 endpoint、独立audit及原FD/fullDN门保持。**本节是固定源码合同，不是本次这些科学阶段完成的声明。**

原19200秒科学绝对钟、120秒读回清理保留、350分钟job、320分钟科学step均保。每call上限仍为 factor19200、owner6000、replay reserve1200、stage8000、boundary600、endpoint600、audit1800，4线程；上限并非求和增加总钟或每call可完成承诺。原runtime的112/112、576单元/577节点、226局部状态/224方向、两个均值、338输出/338×112物理J、完整FD方向/层数/原阈值全部未变。

## 3　实际步骤范围

| 步骤 | 官方结果 | 从本次返回能得到的事实 |
|---|---|---|
| 1–6 runner/checkout/目录/运行时 | success | 完成实际环境与声明运行时准备 |
| 7 来源准备 | success | 新来源准备返回 complete=true/exit0及真实文件identity |
| 8 全源绑定 | success | 实际402项、request/source身份已核；Python compiled-not-imported、Node syntax-only |
| 9 临时容量 | success | 启动free超过原64GiB门；未因此证明所有调用可同时容纳 |
| 10 原输入准备 | success | preparation.json返回complete/phase/error实际字段 |
| 11 原完整科学 | failure | runner/rules/science实际退出1，内部错误正文未返 |
| 12 来源必要读回 | failure / 70 | attempted169036，返回1818字节不完整对象 |
| 13 科学必要读回 | failure / 70 | selected144265，返回1130字节不完整对象 |
| 14 条件清理 | success | 实际执行“保留raw”分支，removed=false |
| report 两个必要转运步骤 | success | 各自精确复印对应小对象，未得到完整原正文 |

“源绑定 success”只包含本步骤声明的完整来源和语法责任：其实际事件明确 no_CXX_scientific_compilation_or_scientific_evaluation_yet=true。本次不是第7步生成器启动失败，也不能从第8步推 C++ 编译、owner、数值正确或最终接受。

## 4　已实际返回的来源和原输入准备

为使临时路径精确而不重复长前缀，本文定义：

- C=/home/runner/work/math-research-public/math-research-public/topics/visible-flex-larger-amplitude；
- T=/home/runner/work/_temp；
- B=T/visible-live128-root-reused-projected-model232；
- S=T/request232-source-preparation；
- A=T/request231-source-preparation。

这些是本次原事件的实际路径缩写，A只是本job重生的冻结231子合同目录，不是旧run231磁盘。

12:55:37.2939620Z 的 R551_source_preparation_return 明确：

| 字段 | 原值 |
|---|---|
| complete | true |
| actual_exit | 0 |
| actual_source_receipt.file | S/source-views.json |
| bytes | 130483 |
| SHA256 | 2db1a631f1736b5e3a723d6e29e4329ab4aec1335aa9cf6bfba87f96b0911ba7 |
| science_success_inferred | false |

随后 request232_source_binding 返回 sources=402、当前完整request SHA和实际head；Python_compiled_not_imported=true、Node_syntax_checked_not_executed=true。这个130483字节源准备正文没有从日志整篇返回，本文只使用实际事件及其identity，不能由其identity补每个生成步骤的原错误/后缀内容。

12:55:54.3317046Z 的 request232_preparation_return：

| 字段 | 原值 |
|---|---|
| complete / phase / error | true / "complete" / null |
| actual.file | B/preparation.json |
| actual.bytes | 76711 |
| actual.sha256 | 4588adea427da97876758fae27e9ef5239af9f272be147e4e4ac99e613e3c884 |

冻结请求只把actual63当原prefix初猜、actual91当tail初猜，重新构造当前原问题；这份prepare事件没有把旧接受/J/owner状态变成本次接受。

容量事件 before与after逐值相同：total154993672192、used62958665728、free92018229248字节；minimum_free_bytes_at_start=68719476736。unused_ephemeral_runner_SDKs_removed=[]、scientific_payload_deleted=false，maximum_uncached_protocol_calls=18、all_possible_calls_fit_not_proved=true、original320_minute_clock_not_started_yet=true。这些是该准备步骤自己的原字段，不代表科学阶段末尾磁盘状态或所有18次调用成功。

## 5　科学入口真实返回与不可推断范围

14:47:34.1957339Z 的 request232_actual_science_return 逐字段返回：

| 字段 | 原值 |
|---|---|
| actual_exit_code | 1 |
| rules_returncode | 1 |
| science_returncode | 1 |
| resource_stop | null |
| external_signal | null |
| owned_processes_quiescent | true |
| execution.file | B/execution.json |
| execution.bytes | 2585 |
| execution.sha256 | 5bb71124df5383d6acbc3cb2dc5b30828bf3f0366d9604464b2f821da25c755e |

原 runner 的 finally 先尝试 quiet，保实际静止结果，再 wait 原rules child并读取真实 rules/runner-result.json，最终写 execution.json并打印上述选定字段。源码这条打印路径不打印内部原stderr、完整error/traceback、actual owner结果或数值gate。本文据已返回 true承认该事件所记录的owned静止，不把它提升为全部必要正文、后续清理时又一次quiet或数值结果。

resource_stop=null只说该外层选定资源字段未设置；不能否定子call自己的原cap、退出或内部错误。science_returncode=1是实际returncode，不是数学拒收标签。原请求设有owner6000等cap，也不能据壁钟接近某数就猜本次在哪个cap停止。日志没有返回该科学原错误正文，本文不归因缺字段、原229/231 KeyError、编译错误、收敛失败或磁盘。

因此下列值既不补true，也不补false或0：当前H/高度、call数、owner是否已起/接受、final/replay、R550缓存次数、原RootStats、完整model/stage、boundary/endpoint/audit、FD各方向、原fullDN迭代/最终接收。源码注册已付与实际科学执行已付必须分开。

## 6　来源必要读回：原完整R547对象实际重选，新单体仍超限

本次 source frame 为：

~~~text
BEGIN_R551_REUSED_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
END_R551_REUSED_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY
~~~

compute和report中的完整frame body逐字相同。包括末LF后为 **1818B / b19ba250221936174348f436b335190cc75cc5b68ca604b014ccc0dca29d76f1**；独立原transport event返回actual_reader_exit=70、necessary_readback_complete=false、scientific_success_not_inferred=true。

实际小对象 schema 为 R551-root-reused-current-owner-projected-model-source-preparation-v1-necessary-v1，request_number=232。四个run字段保GITHUB_REPOSITORY、RUN_ID=43870893094、RUN_ATTEMPT="1"、SHA=本次42492b0c完整值，source=第2节37196/c501、plan=77676/06acd。

其全部超限核心字段：

| 原字段 | 实际返回 |
|---|---|
| attempted_bytes | 169036 |
| attempted_sha256 | 26b6cc357cc1f6163f5325e5e1af24ffcfdad92521a9c640c0e3104632f3f02a |
| complete_local_necessary_object.file | S/necessary-source-overflow.json |
| complete_local_necessary_object.bytes / SHA | 同上169036 / 26b6cc35完整值 |
| necessary_readback_complete | false |
| source_preparation_complete | false |
| transport_exit_code | 70 |
| cleanup_permitted | false |
| no_segments_or_encoded_raw | true |
| numerical_success_not_inferred | true |

source_preparation_complete=false是**原R551超限分支固定重建小对象的值**。第4节实际生成complete=true/exit0与此并不冲突。不能把这个fallback的false改写成生成阶段failure，也不能反过来用生成true改动原必要false。

本次返回还完整保留原R547子读回的三项：

| 原字段/文件 | bytes | SHA256 |
|---|---:|---|
| original_R547_readback_exit | 70（退出码，非字节数） | — |
| original_R547_transport，T/request231-source-preparation-necessary.json | 1368 | 9d80da76516242814d44624778fc13766a93a8c8fbe35b5cea823a1c66a32d16 |
| original_R547_complete_necessary，A/necessary-source-overflow.json | 102413 | 93a2a31f073dfdd3f093f2fa2e53a79653f722c3014b1390b0ab2d1a07050dd9 |

这三个值属于actual232同job的祖先readback，不是actual231/R549的旧raw；相同102413长度不等于同一正文或SHA。

沿固定generator的readback实际控制流：它真正调用原R547 reader；收到70及原false transport后，只允许固定同job A/necessary-source-overflow.json，核实际file/bytes/SHA与attempted bytes/SHA，再读取JSON正文并核run/source/plan。之后才把original_R547_complete_necessary的actual identity放进结果。故本次返回的该identity支持“旧完整对象在同job被真实读取绑定”，但**不支持作者已收到或全文阅读该102413正文**。

新层随后以具名inventory/literal表重选，并保新R550完整来源及未访/错误。实际169036说明这一完整表示依旧超限；本次没有返回按field大小诊断，不能从它猜是哪一张表、递归binding或stderr造成多少占用。没有把原child70改成0，也没有把任何false伪改true。完整169036只是原临时文件身份，不能作为本结论的已读科学或来源正文。

## 7　科学必要读回：完整选定对象未返

原science frame：

~~~text
BEGIN_REQUEST232_REUSED_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
END_REQUEST232_REUSED_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY
~~~

compute和report中的完整body同字。包括末LF为 **1130B / e278932eaecae73194630a39d72d47cdbcd06433561290e660625ff29e06d67c**。其独立transport事件返回actual_reader_exit=70、necessary_readback_complete=false、scientific_success_not_inferred=true。

全部实际小对象字段责任：

| 字段 | 实际值或完整指向 |
|---|---|
| schema | R551-live128-root-reused-projected-model-original-full112-necessary-v1 |
| request_number | 232 |
| request | C/computations/public-live128-root-reused-projected-model-original-full112-FD-fullDN-request.json；SHA=第2节1e1b37ac完整值 |
| run | 与第6节同四个实际run/source字段 |
| actual_original_necessary_summary.file | B/necessary-summary-overflow.json |
| actual_original_necessary_summary.bytes | 144265 |
| actual_original_necessary_summary.sha256 | df60ae0726d0642737d5961c9f1d8d33d5425e605528fd2e675f6e0122bef720 |
| necessary_readback_complete | false |
| transport_exit_code | 70 |
| cleanup_permitted | false |
| scientific_success_not_inferred | true |
| no_segments_or_encoded_scientific_tree_returned | true |
| unreturned_scope | 原完整selected necessary对象超过90000字节，科学/错误内容没有替换成成功view |

原reader按真正当前caller/source/request和namespace绑定，调用原quiet后才选择当前实际文件；正常选择范围含preparation、execution、actual job deadline、orchestration、same-live-client、所有实际call目录、原FD/fullDN、rules、所有原stderr和完整文件identity/读取错误。R551保整RootStats未知字典及编译/安装来源，原13项reuse计数分别属primal/trace并保full last；没有把统计等于数值接受门。

main形成完整canonical对象后，若len(raw)>90000，先把完整原字写B/necessary-summary-overflow.json，然后用上表小对象返回70。**144265只证明这份被选对象的真实长度/identity，不揭示其原necessary_readback_complete、error或fullDN_accepted值。** 即使原build曾设置fullDN_accepted默认false，也不能把未返对象中一个默认值宣称实际数学拒绝。本次小对象没有这些字段。

同时，不能把“编译/RootStats已经由selector保留”写成“这些值本次已经回传”。源合同是完整选择，实际transport结果是不完整；两者必须同时记录。原boundaries、全部partial/未访实际地址只能由未返正文给出，本文没有人为构造一个更小成功摘要、另一段frame或分片取回。

## 8　report、quiet和清理的实际边界

report的两个步骤各自重新核本次schema、run/source/request或plan、byte长度与SHA，随后打印原source及science小body。两个正文与compute完全一致，未选择新数据。report最后的request232_report_identity明确compute_result="failure"，scientific_success_not_inferred_from_job_label=true。

原workflow两项必要步骤都是always，source的70没有跳过science必要读回。清理条件则要求两者necessary_readback_complete同时true；本次两项false，因此没有调用真实删除分支。14:47:35.4063775Z 实际request232_cleanup给：

| 字段 | 原值 |
|---|---|
| removed | false |
| namespace | B |
| reason | source or original-science necessary scope incomplete; raw retained until runner destruction |
| no_scientific_completion_or_quiet_inferred | true |

这解释第14步success：该保留分支的程序成功打印了事实。它不代表rmtree执行、全部raw已读或后继有可用父。runner结束后的平台销毁不是由本文的SHA恢复路径；没有把这些临时文件保存为Git/artifact，也不能让未来run只凭其摘要重建完整科学状态。

此前科学event已给owned_processes_quiescent=true；这里的清理分支不重复断言quiet，保其no_scientific_completion_or_quiet_inferred原语义。本文没有追加kill、cancel、重试或重跑。

## 9　已付、未返与后继责任

本次新增可用事实是：真实来源生成和原输入准备成功；诚实的新模型guard/source已经在完整402项绑定中；原科学入口实际返回1；两个完整selected necessary正文分别超限；原runner静止字段true；原cleanup明确保留raw；两job转运的是相同不完整小对象。

本次**没有**新增以下实际结论：

- R550 accepted RootEval复用的实际命中次数、值相等观测或耗时效果；
- 128 owner/fresh replay接受、当前height或非零continuation进展；
- once-RN64全576模型完成、四组件或原独立audit完成/通过；
- 任一FD方向/层、original fullDN最终接受或新原始父状态；
- 当前内部错误与旧229/231错误相同，或新模型guard修复已被实际走到；
- 原scientific object的完整partial/未访范围已经回传；
- 后继236/237/240同样超限或同一科学原因。

[R550](R550-same-root-accepted-complete-evaluation-reuse.md) 与R551的有限词条件论证不会因本次transport70被改成数值反例；它们也不会因为来源生成0而变成实际数值成功。已有原338×112混合导数合同和原fullDN门保持，不能补“全解析J”或一个新检查作为接受前门。

后继若修必要表示，须在新独立入口从真实同次文件保留原selected全部值/类型/符号/缺失/null、实际错误与地址，并保单90000及超限70；不能把本次未返回144265或169036对象当成手头fixture或可恢复输入。本结论不修改在跑来源、不派发重复实验，也不以额外独立审查/科学测试延期登记。

## 10　终态结论

actual232是一次真实完成到原科学返回和两项必要读取尝试的公开运行。科学内部接受状态与具体停止原因未由返回正文支付；已返回的严格终态是：science/rules/outer exit1，来源169036→1818/70、科学144265→1130/70，runner选定quiet=true，实际cleanup removed=false。下一步必须沿完整真实来源修读回或消费仍能合法重生的同次新运行数据，不能把报告job成功、source生成complete或局部身份当作原数学门通过。

本次两原日志已经由唯一读者各取一次。此后只引用本文和已返回身份，不重新取得这两日志，不保存可再生Actions raw，不猜未返回科学量。
