# R566：actual237 原准备完成、双份必要摘要超限及未返回的科学结论

作者：ChatGPT（AI）；日期：2026-11-16。

**可信度：已证明，限本文列明的真实 Actions 元数据、已返回事件、两份超限描述符及源码控制流事实。原完整科学必要对象未返回；本次实际 owner、重放、模型、FD、fullDN 和最终 audit 的内部结果均未由本文补定。**

actual237 的源码生成、432 件实际源码绑定、原输入准备均真实返回成功。科学外层返回 1，原 rules 和 science 返回码也均为 1；外层记录的 resource_stop 与 external_signal 为 null，owned_processes_quiescent 为 true。源码必要对象实际为 286365 bytes，科学必要对象实际为 164993 bytes，两者分别超过原 90000 bytes 上限并返回 70。compute 和 report 最终只逐字返回 1837 bytes 的源码超限描述符与 1154 bytes 的科学超限描述符。清理步骤走原保留分支，removed=false。

这些事实支持“原准备完成，双必要读回不完整，具体科学终因未返回”。它们不支持把本次归因为旧 run 的 KeyError、某次 root 收敛失败、某个模型失配、内存或时间用尽，也不支持由准备成功、job 标签或累计用时认定 native/fullDN 接受。

## 1. 唯一实际 run、固定来源与读取范围

官方 run 为 [43884807627](https://github.com/Rogerhu12/math-research-public/actions/runs/43884807627)，仓库 Rogerhu12/math-research-public；workflow ID 420212367，attempt 1，事件 workflow_dispatch，分支 main。实际 head、checkout 输出及所有返回帧的 GITHUB_SHA 均为：

99347c619e66946b758f6f731ce0a4f76d41fa9e。

官方 created_at 与 run_started_at 均为 2026-11-16T14:21:08Z，终态 updated_at 为 16:19:49Z，conclusion=failure。发布前的作者 source commit 与行政 publisher job 不作为科学 run。

| 实际 job | 官方名称 | 终态 |
|---|---|---|
| 133359953110 | Actual237 lifted-product-owner same-DN model and original FD fullDN | completed/failure |
| 133435732711 | Actual source scope and one necessary237 original scientific conclusion | completed/success |

两原 job 日志均由本结论作者在终态后各读取一次；运行中只读 jobs 元数据。终态官方元数据在 16:24:37 UTC 轮询确认。本文没有再次下载任何一个 job 日志，没有读取未来 run 的日志，也未提取或上传临时科学数组。

连接器提供的是**解码文本**。以下是该返回文本重新 UTF-8 编码后的身份，包含该文本中的时间戳、命令回显、换行和初始 BOM；不能称为 HTTP 原始日志字节的身份：

| 连接器完整返回文本 | UTF-8 bytes | SHA-256 |
|---|---:|---|
| compute job 133359953110 | 76211 | cd62e6f2d454b354fd6d19644ca70c5866f95d35fce4ca69e89f945df256bd85 |
| report job 133435732711 | 17767 | 226ac0f2d2708039609181495dfd1a45d50718e81a9be493dd8ebda7f3ddfcad |

两份实际帧均按原 BEGIN/END 边界提取，去掉日志时间戳，并保留原 JSON body 的末尾 LF。compute 与 report 的源码帧逐字相等，科学帧也逐字相等；§5、§6 中的 bytes/SHA 同时匹配两处原 identity 事件。没有把 report 的完整成功打印升级为所指 286365/164993 bytes 正文已经传回。

原日志和可再生必要 body 仅在本次临时会话中阅读，未作为 Git blob、主树文件或 artifact 保存。本文为作者结论，保留可核验的来源、实际值、范围与未付责任。

## 2. 冻结请求及原科学合同

实际 workflow 为 .github/workflows/visible-larger-public-live128-root-lifted-product-projected-model-original-fullDN.yml，完整 23955 bytes，SHA-256 0059a6c510d453b63f05fe9fe49ea574a0ad14cc5d1d2842949c82e4a28003fb。

实际请求为 computations/public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json，完整 96574 bytes，SHA-256 fff570a800581ed22887734b467ad1b368cdd8d17d9df04ba49ad1e05c6bf605；schema 为 public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request-v1。

实际 R565 生成器为 root_20261116_live128_lifted_product_projected_source_views.py，38098 bytes，SHA-256 ee6bad1b586c77e94e54714ecff05a980ce9ad11bc50658a55583fd372ddc6f2。其完整来源计划 notes/r565-live128-lifted-product-projected-model-complete-source-plan.json 为 71039 bytes，SHA-256 6d6ff7d6f95f83e809fc0e260765a47185011ca86e2cc62c0a4dcf544f9789f1。这些身份在本 job 的 prepare、source binding、必要读回和 report 中分别实际绑定。

| 角色 | 实际 basename | bytes / SHA-256 |
|---|---|---|
| owned runner | geometry_20261116_live128_lifted_product_projected_owned_run.py | 39404 / d61c81c14532bd5be2dc5a5f718196be1be922082a419e06dcc2c5463574b1ff |
| 原科学入口 | geometry_20261116_live128_lifted_product_projected_original_full_dn.py | 由冻结请求的 source_sha256 与完整 R565 计划绑定 |
| 科学必要 reader | root_20261116_live128_lifted_product_projected_necessary.py | 62562 / 9d3b25b88f31b7d1ddc383d566b13a10d845759ab7887aa2946b0b7d578d1d68 |

本次来源保持原236的全部417 pins，再实际加入 R564 两公共源、两生成 include、新生成器及十个独立 caller，合计432=357 public+75 generated。它是一个明确的实际源码集合；不把该数量称为任意动态导入的普遍闭包证明。R562 及更早 caller 作为祖先保留，实际科学入口由本次新身份指定。

R564 对指定首乘积在实际资格成立时计算完整 113×53 整数乘积并 RN-even 到原 binary128 字；否则执行原乘法。它保留 R561 第二乘法选择、R550 同根接受后完整 RootEval 复用及 R535 有限词机制。实际 hook 规定在原 owner_scope 中只直接安装 R564 一次。R534 完整 projected64 same-DN 模型、权威的128值与独立重放、原边界和 endpoint/audit 责任保持。**源码准备得到 include 不等于本次实际 g++ 编译、hook 安装或某一优化分支使用已经被读回证实。**

原请求中重要的科学与资源值未改：

| 合同 | 冻结原值 |
|---|---|
| field / tail modes；spacing | 112 / 112；2 |
| 完整 depth、节点数、每节点 shooting state | 576；577；224 |
| 含两 mean 的局部 RK 状态；全 stage 方向 | 226；224 |
| 实际物理输出顺序 | slope112, second112, meanSlopeCorrection1, meanSecondCorrection1, height112 |
| 物理 J | 338×112，保原混合导数合同，不宣称全解析 |
| 原 nonlinear 最大迭代 / trial / tolerance | 32 / 10 / 2e-9 |
| 原 FD | direct_boundary 与 separated_boundary 各10方向；3步长层；2 Richardson 层；relative threshold 0.00005；全部适用 contraction |
| 原 prefix inner trial / RMS / boundary tolerance | 17 / 1e-6 / 1e-11 |
| runtime | node_heap6144；jac_workers2；max_nodes1200；material_angles4096；physical_angles4096；outer_iterations8；extension_step0.005；taper_fraction0.4 |
| native 参数 | eta="1"；exact workers2；max_factor_bytes2147483648 |
| 整体时钟 | 19200 scientific seconds；不因新 H 重开；readback/cleanup reserve120 |
| 工作流 caps | job350分钟；science step320分钟 |
| 每 call caps | owner6000；replay reserve1200；stage8000；boundary600；endpoint600；audit1800；threads4；均按实际剩余钟裁切 |
| 启动磁盘 / 运行资源停界 | 68719476736 / 2147483648 bytes |
| 预计最大未缓存 protocol calls | 18；不是全部都可完成的容量证明 |

原实际63 prefix 和 actual91 failed73 tail 只作为初猜及来源；本次不继承旧接受或旧完整响应。准备事件虽成功，所引用 preparation.json 的完整输入账未通过本次科学必要正文传回，故本文不把上述请求参数表写成所有运行阶段都已访问的清单。

## 3. 本次真实准备与实际容量

compute 使用 blob:none、固定 head 的 partial/sparse checkout。实际 Python3.12.14、Node24.22.1，安装原 numpy2.3.5、scipy1.17.0；日志报告 g++15.2.0。安装输出不构成本次科学 C++ 编译成功证据。

14:21:38.5059160Z，R565_source_preparation_return 返回 complete=true、actual_exit=0、science_success_inferred=false。实际 receipt 为 /home/runner/work/_temp/request237-source-preparation/source-views.json，144876 bytes，SHA-256 c47e8563da7d5f220908c081fadb1d03df0dc8ebda2277f3d615fef2f1b069bc。

14:21:41.5490608Z，request237_source_binding 返回432 sources、实际 request SHA 和同一 head；事件明确 Python_compiled_not_imported=true、Node_syntax_checked_not_executed=true、no_CXX_scientific_compilation_or_scientific_evaluation_yet=true。原绑定块逐件核 source_sha256，核完整实际 source map 与 generated map，并保持 README blob 核验。这个事件证明这些前置绑定实际走到返回点；不替代后来 owner 的实际编译/数值记录。

14:21:41.7509322Z，容量事件的 before 与 after 完全相同：

| 项 | bytes / 原值 |
|---|---:|
| total | 154993672192 |
| used | 62966304768 |
| free | 92010590208 |
| minimum_free_bytes_at_start | 68719476736 |
| unused_ephemeral_runner_SDKs_removed | [] |

scientific_payload_deleted=false，all_possible_calls_fit_not_proved=true，original320_minute_clock_not_started_yet=true。这里确实通过了原启动容量要求；不能拿别的 run 的磁盘不足替本次归因，也不能由这一时刻的 free 推运行全程资源充足。

14:21:55.4056493Z，request237_preparation_return 返回 complete=true、phase="complete"、error=null。其实际 preparation.json 为 /home/runner/work/_temp/visible-live128-root-lifted-product-projected-model237/preparation.json，81722 bytes，SHA-256 408397a2ead94375efa0ca2a98f87f84c89fe8cd5088fe870550ca777447d5aa。

以上 source receipt 与 preparation receipt 的正文均没有由本文另行下载；记录的是原事件实际返回的身份和明确字段。尤其不能把后面源码超限 fallback 中的 source_preparation_complete=false 反向覆盖这里真实 complete=true 的准备事件，原因见§5。

## 4. 科学外层的真实返回及不可扩张的含义

14:21:55.4320571Z 出现原 runner run 命令回显。它仍传真实237请求、其 SHA 和本 job 独占 namespace。16:19:35.5823781Z 返回 request237_actual_science_return：

| 实际字段 | 原值 |
|---|---|
| actual_exit_code | 1 |
| rules_returncode | 1 |
| science_returncode | 1 |
| resource_stop | null |
| external_signal | null |
| owned_processes_quiescent | true |
| execution.file | /home/runner/work/_temp/visible-live128-root-lifted-product-projected-model237/execution.json |
| execution.bytes | 2657 |
| execution.sha256 | f0fd340392d8119ef39637516c9a87965e9d957bb672434b77e9a05e02286d96 |

随后 shell 原样报 exit code1。该实际事件是已返回的运行事实。它没有携带内层异常、native阶段位置、接受步、owner最后残差或最后 H。

resource_stop=null 和 external_signal=null 只是该**外层实际记录**的值；不能推“所有内层组件没有资源停”。owned_processes_quiescent=true 是这次外层关闭算法实际返回的总状态；它也不赋予未返回的逐 PID/startticks 清单或未读 marker 任何推测值。本文没有根据这个 null/true 组合推造数学拒收、timeout、OOM 或原门通过。

这段 wall-time 不能视为完整 root、全 J、某个 stage 或某个优化的独立计时：原科学调用包含其完整流程，日志没有返回分项进展。本文不把“约两小时后退出”换算为某个确定进度或预填当前 native owner 已完成。实际后继源若修读回，仍应按其自己新的 run/source 和原门报告，不能迁移本次未知内部状态。

## 5. 源码必要读回：已返原70和两层正文身份，未返286365正文

16:19:36.8686325Z 至16:19:36.8709048Z，compute 打印唯一源码帧 BEGIN_R565_LIFTED_PRODUCT_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY 至同名 END。body 含末尾 LF 为1837 bytes，SHA-256 910e97088826a2d50bfd34f559776c794e91825720137eaeef09db43b0c64b82。

16:19:36.9958837Z 的实际 transport 事件确认 actual_reader_exit=70、上述 bytes/SHA、necessary_readback_complete=false。shell 随后按原码退出70。report 于16:19:45.7971729Z 再次逐字打印同一 body，16:19:45.7983366Z 的 source_report_identity 再核相同1837/SHA。

这个已返对象的完整语义字段如下；路径中的目录均属于同一个 actual237 job：

| 字段 | 实际值 |
|---|---|
| schema | R565-root-lifted-product-current-owner-projected-model-source-preparation-v1-necessary-v1 |
| request_number | 237 |
| run | §1仓库、run43884807627、attempt"1"、head99347c… |
| necessary_readback_complete | false |
| source_preparation_complete | false |
| transport_exit_code | 70 |
| attempted_bytes | 286365 |
| attempted_sha256 | f5c4a3a60bccc7686cd144477cfb68b30e0bbf7977c97d7f2737bcd2ba8e03e3 |
| complete_local_necessary_object.file | /home/runner/work/_temp/request237-source-preparation/necessary-source-overflow.json |
| complete_local_necessary_object.bytes / sha256 | 同上286365 / f5c4a3a6…完整 SHA |
| original_R562_readback_exit | 70 |
| original_R562_transport.file | /home/runner/work/_temp/request236-source-preparation-necessary.json |
| original_R562_transport.bytes | 1813 |
| original_R562_transport.sha256 | 8f2a0f7af766665969e1aabfacfb36add2d7e5c39c6d12c8ac11a73dde34147f |
| original_R562_complete_necessary.file | /home/runner/work/_temp/request236-source-preparation/necessary-source-overflow.json |
| original_R562_complete_necessary.bytes | 225803 |
| original_R562_complete_necessary.sha256 | 97594d3385b865bb06cc8fa565c68d4f63e534e08978fbc6bd167439eda99ca2 |
| source | §2实际38098字节生成器的完整路径与 SHA |
| plan | §2实际71039字节计划的完整路径与 SHA |
| cleanup_permitted | false |
| no_segments_or_encoded_raw | true |
| numerical_success_not_inferred | true |

上述 source.file 的实际前缀为 /home/runner/work/math-research-public/math-research-public/topics/visible-flex-larger-amplitude/computations/，其后为§2生成器 basename；plan.file 同一 topic 下接§2 notes 路径。它们的 bytes/SHA 没有省略其他版本或混入 preview。

request236-source-preparation 是 actual237 内真实调用冻结 R562 祖先源的临时目录，不是另一次 actual236 run 的日志或文件。其225803 bytes 与1813 bytes 均为本 job 返回的身份。本文没有把该祖先 body 当已返回，也没有借其它 run 的同名文件补其内容。

### 5.1 source_preparation_complete=false 的实际来源

R565 生成器 readback 先读取本 job source-views.json，核 schema/run/source/plan，然后把当前完整对象纳入具名来源表示。它真实调用冻结 R562 readback。原 child 返回70时，保留原 exit70 与 fallback.false，再读取原 descriptor 所指同 job 固定 overflow 路径，逐 bytes/SHA 核完整对象。它没有把旧70改成0，也没有只嵌一个假完整 descriptor。

最后 canonical(result) 若超过 LIMIT=90000，原源码写本层 necessary-source-overflow.json，并建立一个**新的 transport fallback**。该分支字面设置 necessary_readback_complete=false、source_preparation_complete=false、transport_exit_code=70，再保当前和祖先的完整文件身份。此时 body 不再携带完整 current_source_record、实际错误树、未生成 suffix、具名表或全部 compiler binding。

因此，1837字节对象的 source_preparation_complete=false 是超限 transport 的保守表示，不是源生成失败的独立事件。§3 的 source prepare complete=true/exit0 与本节 fallback.false 同时成立、分别保留。由 fallback.false 断言“R564没生成”“源码准备没完成”不符合真实控制流；由 prepare.true 断言“完整源码必要体已读”同样不符合事实。

本结论只将286365、225803及其 hashes作为实际声明的完整身份；没有以这些身份、原临时路径或源码意图恢复未返回的任何正文值。

## 6. 科学必要读回：原164993完整选择没有传回

16:19:37.4202502Z 至16:19:37.4219906Z，compute 返回 BEGIN_REQUEST237_LIFTED_PRODUCT_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY 至同名 END。body 含末尾 LF 为1154 bytes，SHA-256 d8f1897e9a5f93bd42f8b04963be73140ec4fdfe59d2831bbdb08d67b17fe90c。

16:19:37.5504813Z 的 transport 事件为 actual_reader_exit=70，necessary_readback_complete=false，scientific_success_not_inferred=true；随后 shell 退出70。report 于16:19:45.8292184Z 至16:19:45.8299517Z 打印逐字相同的1154字节，16:19:45.8300639Z 的 identity 还明确 compute_result="failure"、scientific_success_not_inferred_from_job_label=true。

| 已返字段 | 原值 |
|---|---|
| schema | R565-live128-root-lifted-product-projected-model-original-full112-necessary-v1 |
| request_number / run | 237 / 同本次真实run/source/attempt |
| request.file | /home/runner/work/math-research-public/math-research-public/topics/visible-flex-larger-amplitude/computations/public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json |
| request.sha256 | fff570a800581ed22887734b467ad1b368cdd8d17d9df04ba49ad1e05c6bf605 |
| actual_original_necessary_summary.file | /home/runner/work/_temp/visible-live128-root-lifted-product-projected-model237/necessary-summary-overflow.json |
| actual_original_necessary_summary.bytes | 164993 |
| actual_original_necessary_summary.sha256 | 63f1f5ba5b19676a046599cbc5443f198bc84e9a43fddeafbc30f414074a1422 |
| transport_exit_code | 70 |
| necessary_readback_complete | false |
| cleanup_permitted | false |
| no_segments_or_encoded_scientific_tree_returned | true |
| scientific_success_not_inferred | true |
| unreturned_scope | The complete selected necessary object exceeds90000 bytes; scientific and error contents not replaced by a success view |

最后一行保留原范围声明。1154字节完整返回，并不等于它指向的164993字节也返回。未返回的对象不是“空对象”“全部字段false”或“只有错误”；其科学、资源、错误、原地址、统计和来源内容都不得由目前读到的长度推断。

具体仍未读出的责任包括：

1. 首个/后继真实 H 的调用次数、实际输入状态、初猜路径、当前 call 身份及 last=tangentPredictor 是否实际用于本 run。
2. owner 实际编译、R564 direct hook 安装、祖先 include 使用、primal/trace RootStats，尤其 exact_lifted_factor_product 三路径17计数和 full last。
3. 原32×10试步、root branch、最后 residual、接受/拒绝、重放状态及字节吻合、同次当前64完整模型是否产生。
4. 完整576 stage、每个226×224及两 mean、338×112物理响应、endpoint/boundary/audit 的当前进展与未访地址。
5. 原FD两组各10方向、全部层和 contraction、fullDN、最终同 H fresh audit 的实际结果。
6. 具体内层 exception/traceback、未完组件资源状态、逐 owned process 证据和完整原错误必要选择。

这些项目列出的是原应付责任，不是新 gate。尤其不能从“338×112不是全解析”另设一个原合同没有的全解析前门；也不能用旧 run 的成功或失败填补本次缺项。本文没有判定这些对象实际存在还是尚未生成；两者在未返回范围内都保持未知。

## 7. Quiet、清理和 report 的实际层级

§4 的科学返回事件明确 owned_processes_quiescent=true；这是本次已返回的 quiet 总状态。本次 cleanup workflow 仍先要求 NECESSARY_COMPLETE 和 SOURCE_READBACK_COMPLETE 同为true，才调用原 owned runner cleanup。

实际环境中两项均为false。16:19:37.6639479Z，request237_cleanup 返回：

- removed=false；
- namespace=/home/runner/work/_temp/visible-live128-root-lifted-product-projected-model237；
- reason 为 source or original-science necessary scope incomplete; raw retained until runner destruction；
- no_scientific_completion_or_quiet_inferred=true。

所以官方 cleanup step=success 只表明这个**保留分支**正常返回；不是完整科学数据已删除，也不是必要正文已收齐。原 runner 的删除分支没有因此被执行。runner destruction 后原临时目录是否仍可访问没有另作调查，本文不许诺恢复该目录；固定 SHA 只能标识曾报告的文件，不能代替文件字节。

report job=success 也只是按原 schema/run/request/plan及bytes/SHA核验并再打印这两份实际 transport body。report 没有把 compute_result=failure改掉，没有生成新的完整科学对象。由它的 job 名称中“scientific conclusion”或成功标签推出 native/fullDN通过，均超出实证。

## 8. 可用结论及后续责任

本次已付的独立事实是：实际237固定来源建立了原准备和432源码绑定；科学外层真实返回1且已关闭所管进程；两个完整必要选择分别超出原90000bytes限制，原70及失败范围均真实保留；两个 report 帧与 compute 帧逐字相同；清理实际没有删除原 namespace。

本次未付的是完整科学内部结论及完整来源读回，不是一个可以凭标签补写的数值失败理由。R564 的条件同词命题仍由其源/证明承担，actual237 未返回其具体执行计数、full last、最终门或速度证据。本文不据本次的双超限宣称这些数学命题已反驳，也不据其源码存在宣称数值任务已完成。

后续完整读回若采用具名的固定语义共享，应保持本次暴露的两类 scope：完整 source preparation/祖先子调用及错误范围，和原科学必要选择/完整统计/最后未访地址。不得提高90000上限、把descriptor升格为完整正文、删除失败或未知值，或新增数学 gate 来替代原责任。本结论本身不发起重跑、不修改已冻237，不把后继 run 的实际状态接在这次旧状态后。

## 9. 可核验来源

- [actual237官方run和两job](https://github.com/Rogerhu12/math-research-public/actions/runs/43884807627)，唯一终态日志读者与字节范围见§1。
- [冻结237请求](https://github.com/Rogerhu12/math-research-public/blob/99347c619e66946b758f6f731ce0a4f76d41fa9e/topics/visible-flex-larger-amplitude/computations/public-live128-root-lifted-product-projected-model-original-full112-FD-fullDN-request.json)。
- [冻结R565 source plan](https://github.com/Rogerhu12/math-research-public/blob/99347c619e66946b758f6f731ce0a4f76d41fa9e/topics/visible-flex-larger-amplitude/notes/r565-live128-lifted-product-projected-model-complete-source-plan.json)。
- [实际source生成与读回](https://github.com/Rogerhu12/math-research-public/blob/99347c619e66946b758f6f731ce0a4f76d41fa9e/topics/visible-flex-larger-amplitude/computations/root_20261116_live128_lifted_product_projected_source_views.py)，特别是readback的真实祖先70/完整overflow绑定与本层90000限制。
- [冻结237workflow](https://github.com/Rogerhu12/math-research-public/blob/99347c619e66946b758f6f731ce0a4f76d41fa9e/.github/workflows/visible-larger-public-live128-root-lifted-product-projected-model-original-fullDN.yml)，原source/science两份独立必要读回、report与cleanup条件。
- [R564完整条件证明](R564-exact-binary64-factor-products-and-complete-integer-rounding.md)，只作为本次算术来源和明确责任，不作为未返回的运行结论。
