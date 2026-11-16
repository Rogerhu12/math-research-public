# R609：actual252 来源回执联合检查停止、完整必要正文超限及科学未启动

作者：OpenAI ChatGPT（AI），2026-11-16（UTC）。

**可信度：启发式/数值证据（本条实际运行事实来自两个官方终态 job 的完整日志、其中实际返回的必要描述体，以及冻结源码控制流；本条没有新增科学数值或误差界）。** 对“某一通过位置必先经过哪些源检查”“某一失败位置之后哪些调用尚未进入”的有限程序推论，本文限于实际冻结源码与同一次运行，另明确标为已证明的条件控制流结论。

request252 的来源准备在 R604 桥接回执联合检查处返回外层 exit2。完整来源必要正文的实际尝试大小为487426字节，超过原90000字节上限，因而仅返回1626字节的超限描述体。当前252的十个 caller 视图未进入生成循环；当前科学 reader 文件不存在，原输入恢复和整个 full112/native/FD/fullDN 科学阶段均未开始。程序明确跳过 namespace 清理，未由 job 的结束推断 quiet。

**本次不能确定联合检查内部究竟哪一个条件失败，也不能确定桥接子进程的真实退出码或原 R583 函数的具体异常。** 这些字段属于没有返回的完整来源对象。本文不从外层错误文字、step标签或 SHA 补造其内容。

## 609.1　实际发布、运行及唯一读取

本次实际入口对应 [R605](R605-request252-direct-six-plan-source-and-complete-necessary-entry.md)，组件为 [R604](R604-direct-six-plan-source-bridge-and-exact-ancestry-inverse.md)。两件的条件结论并未宣称已经修复 actual244 未返回的内部错误；本条正记录第一次实际252结果。

| 项目 | 实际值 |
|---|---|
| 仓库 | Rogerhu12/math-research-public |
| 主线与科学实际 head | af8930100294bcf4d52430343e1e33932e2565f0 |
| 科学 run | 43917735686 |
| workflow ID | 420398241 |
| event / attempt | workflow_dispatch / 1 |
| compute job | 133476367763，completed/failure |
| report job | 133476653331，completed/failure |
| 发布行政 run / job | 43917625617 / 133475958236 |
| 发布期间真实 pull 所读 head | 14ae570141e5dd3891c5532b57526cd02c216079 |
| 发布过程 | 非快进后立即真实 pull/rebase；两份 README 不变；17:22:37.927 UTC 普通 push 成功 |
| 实际派发 | 17:22:44.9636716 UTC，单次官方 POST200 |

唯一终态读取者对这两个 job 各读取一次完整官方日志。没有再取运行中日志，也没有为研究本次失败而复跑科学或读取另一个 run 的 raw。

| 已完整读取对象 | UTF-8 字节数 | SHA256 |
|---|---:|---|
| compute job 原日志 | 59804 | 1a2eba1707e6776ca05efe864c18f1ee81cff0244e51d7897c5a07d81a5cec00 |
| report job 原日志 | 13363 | d78534994b270cf5edf333624a7a8f9817c9ebe1dfb860269f3209c14584b401 |
| compute 实际来源必要描述体 | 1626 | 8017fc1b4ee3ac2e9597b4c64111eaf2e719b793a8f0e99e44f369a8d35846b3 |
| report 重述的同一来源描述体 | 1626 | 8017fc1b4ee3ac2e9597b4c64111eaf2e719b793a8f0e99e44f369a8d35846b3 |

两份1626字节正文逐字相同。它们是同一超限描述的 compute/report 运输，不是两份独立科学结果，也不是487426字节正文的分块。此处仅登记必要事实和身份；没有把原日志、必要 raw 或运行输出上传为新的 detached Git 对象或 main 文件。

## 609.2　实际源码身份及所要求的闭包

本次原公开执行件保持冻结身份：

| 角色 | 文件 | 字节数 | SHA256 |
|---|---|---:|---|
| 来源生成器 | computations/root_20261116_live128_direct_loop_source_views.py | 39322 | e528780ecc5556c4181d1cbe137f6e02140d978525702de8f99d71bb25bc4d58 |
| 来源计划 | notes/r605-live128-direct-loop-source-complete-plan.json | 58151 | c64422f86312cb0784ea6235b22fe2c139eb60847c0fe4c08ddd5970cfb42d9b |
| 外层请求 | computations/public-live128-direct-loop-source-composition-request.json | 23556 | fdafd91e34f874ae97e298d8fbb3c715a5044de5195b3f4fe6e14f825e85eb1c |
| workflow | .github/workflows/visible-larger-live128-direct-loop-source-full112.yml | 25758 | e6bb0ce06f73dfff755b3acc08a837362f40caa9baf824848c0a020fed4e8771 |

该 workflow 身份与冻结发布字节相符。来源生成器、计划与请求的身份同时由本次实际返回的描述体给出；workflow 身份由发布冻结件给出。

计划中的471个最终来源包含原248的454个实际来源、五个新增公开来源、两个真实 R583 C++ 输出以及十个新的 caller 视图。这个计划总数不是本次完成数。下面的实际停止先于新十视图循环，因此不能将471的计划闭包写成已经完整生成、导入或执行。

本次沿已刊248的原63输入、owner上限12000和总科学钟19200秒。原 replay1200、stage8000、boundary/endpoint600、audit1800、必要读回120及全部原数值门仍在冻结请求中。这些是未启动科学链的合同，不能写成本次已经消耗、通过或拒绝的科学预算。当前252的实际科学钟尚未由该科学入口建立。

## 609.3　实际首个来源停止

compute 日志在17:23:10.2927676 UTC返回事件 request252_source_preparation_return：

- complete=false；
- actual_exit=2；
- phase=R583-source-generation；
- error.type=ValueError；
- error.message 为 “Actual direct original R583 source bridge receipt, not a small success substitute”。

原 traceback 定位到生成器 prepare 第429行的联合 require，并在第40行 raise ValueError。外层 workflow 用 check=True 等待这个来源子程序，随后得到 CalledProcessError：来源程序 exit2，来源准备 step 的 shell exit1。二者是不同层级的实际返回码。

实际来源准备文件只返回身份：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| /home/runner/work/_temp/request252-source-preparation/source-views.json | 9038 | 1286ec0f5a1052660b997820f10c9f2fdb2ce7249246592f7d55e4dcd9a6613a |

9038字节文件的完整正文未返回。因此不能从此身份还原其 generated、not_generated、R583_child、原 stderr、桥接回执或完整 binding。

冻结源码中，第429行联合检查要求以下条件同时成立：

1. 已读取的 complete_R604_bridge_receipt 是 dict；
2. schema 等于 R604-direct-original-R583-six-argument-source-bridge-v1；
3. run 等于当前外层实际 run 身份；
4. source 等于当前真实桥接源码身份；
5. actual_original_adapter 等于当前真实 R583 adapter 身份；
6. actual_binding 等于当前真实 binding 文件身份；
7. 回执 actual_exit 等于实际子程序返回码；
8. original_callable 等于 prepare_sources。

实际错误证明这个合取没有全部成立。日志没有给出失败子项。特别地，不能由这个错误断言回执不存在、schema错、路径错、实际子进程退出2或70、原 prepare_sources 抛出某个异常，或 R583 的某个内层计划形成失败。

紧接这一检查之后才是原完整 R583 binding 检查：子程序exit0、完整schema/run、source_preparation_complete、没有编译/科学执行、同一真实 HERE、两个完整生成输出以及实际 loop-mode 合同。该后续检查本次没有进入，不能把它的任何子项记录为已通过或已失败。

## 609.4　由实际停止位置得到的有限控制流范围

以下结论是对冻结生成器 prepare 的有限控制流推论，限于这次日志确认到达的第429行，不用未返回文件的内容作前提。

在到达桥接回执检查以前，程序已经完成：

- 核真实 Git head 与 GITHUB_SHA 一致；
- 核新增公开源码的实际字节身份以及输出路径不覆盖祖先文件；
- 以真实同 job 子程序调用冻结248来源生成器一次；
- 读取248实际来源准备回执，核其 schema、run、generator、outer request 和 plan；
- 核248来源子程序exit0、complete=true、error=None；
- 取得完整实际248请求，逐个检查原454来源在同一 HERE 中确实存在、不是 symlink、SHA逐值相同；
- 再次核新增公开来源、当前生成器、R583 adapter、六个实际计划参数路径及 R604桥接源；
- 真实同步调用 R604桥接 CLI；该调用已经返回，才能进入后续观察和回执检查。

实际后续 step 的环境中保留了上一层的真实请求路径：

/home/runner/work/_temp/request248-source-preparation/current-request248.json

其 SHA256 为9f1c17a63be41be54cae3e451e91669f7a4159120d39c501e988a3a5aac2ae4f。这个对象是本 job 实际形成的248祖先请求，不是当前252完整请求，也不是旧248 run 的科学状态。

桥接返回后、联合检查前，程序有一个两个 R583 输出文件的观察循环，并可读取存在的完整 binding 与 bridge receipt。由于这部分实际字段未返回，本文不能把“执行到观察循环”升级为两个输出已生成、某一个输出缺失、其字节正确或桥接来源完整成立。

第429行之后的十 caller 视图生成循环位于第452行起。该循环尚未进入，因而当前252的完整请求、正常 science reader 和当前调用链没有完成形成。本次不能把祖先454的通过范围延伸成当前471的通过范围，也不能用祖先有效来源替代当前独立源码身份。

## 609.5　来源必要读回的实际超限

17:23:11.7646610 UTC起，compute 打印来源帧：

BEGIN_REQUEST252_DIRECT_LOOP_SOURCE_SOURCE_NECESSARY

至对应 END_REQUEST252_DIRECT_LOOP_SOURCE_SOURCE_NECESSARY。SOURCE重复两次是实际帧拼写，不作更名。

这一帧含完整1626字节描述体，schema为：

R604-direct-R583-original248-complete-source-preparation-v1-necessary-v1。

实际关键字段为：

| 字段 | 实际值 |
|---|---|
| attempted_bytes | 487426 |
| attempted_sha256 | f41a10949d0634fc350f4882106ab93db9894a626fce2b2a499ec4df311b2dd6 |
| necessary_readback_complete | false |
| source_preparation_complete | false |
| transport_exit_code | 70 |
| cleanup_permitted | false |
| whole_body_not_split_or_truncated | true |
| scientific_success_not_inferred | true |

complete_local_necessary_object 指向：

/home/runner/work/_temp/request252-source-preparation/necessary-source-overflow.json，

实际登记487426字节和同一 SHA256。17:23:11.8428247 UTC的 request252_one_source_necessary_transport 事件另确认 actual_reader_exit=70、实际对外描述体1626字节及上述8017fc1b完整SHA。

由此可确认本次完整来源必要正文未通过单90000字节运输合同。保留其完整本地对象身份和超限描述，不等于已经返回那487426字节。正文没有分包、裁切、用计数替换成功正文或把上限提升。

本次未返回的正文可能含来源桥、祖先回执、原表示关系报告、错误及局部来源观察。本文没有这些实际字段值，故不宣称 R604旧逆或 R600六代关系本次具体采用了哪一条、缩小了多少、哪个源结构占主要字节，或其内部关系失败。仅由487426这一总数不能推断未经关系处理的原尺寸，也不能把旧run的必要正文当本次输入进行重放。

report job 的来源 step 又完整打印同一个1626字节描述，event=request252_source_report_identity，SHA逐字相同。这证明描述运输成功；并不证明来源必要scope完整，且不改变原70。

## 609.6　科学必要scope实际不存在

因为前述十caller循环未开始，科学必要 reader 路径没有形成。compute 运行必要读回命令时，Python 实际错误为：

python: can't open file '/home/runner/work/math-research-public/math-research-public/topics/visible-flex-larger-amplitude/computations/root_20261116_live128_direct_loop_source_necessary.py': [Errno 2] No such file or directory

随后17:23:11.9423926 UTC事件 request252_necessary_not_returned 给出：

- actual_reader_exit=2；
- actual_scientific_summary_not_invented=true；
- cleanup_permitted=false。

这是真实必要reader缺失错误，不是 native 求解失败、FD拒绝或 fullDN数学门失败。report job 在17:23:18.1940549 UTC也返回 request252_no_necessary_summary，compute_result=failure，scientific_or_transport_success_not_inferred=true，并exit2。

本次不存在当前科学必要正文。没有当前H、warm/predictor、root迭代、primal状态、J、audit、FD、fullDN、接受步、最终参数、solver merit或统计值可以从本次日志报告。原19200秒总钟和12000秒owner上限没有被本次科学程序消耗；不能据来源准备短时退出推断原预算足够或不够。

## 609.7　实际 step 与责任表

| 责任或阶段 | 本次实际范围 |
|---|---|
| compute steps1–6 | 常规准备成功；不等于当前数学源码调用成功 |
| step7 来源准备 | 实际运行，在第429行联合桥接回执检查失败 |
| 原248祖先来源形成 | 同job完整前缀控制流已通过，原454个来源逐值核回 |
| R604同步桥接调用 | 实际调用并返回；内部完整回执及退出码未返 |
| 两个 R583生成输出 | 观察代码已到达；具体存在/身份状态未返 |
| 十个当前252 caller视图 | 尚未进入生成循环 |
| step8 当前471来源与语法检查 | skipped |
| step9 当前科学容量门 | skipped；不能写作通过或拒绝 |
| step10 原63/78/91输入恢复 | skipped |
| step11 当前H/fullJ/R273/live128/原FD/fullDN | skipped，科学未启动 |
| step12 来源必要读回 | 全body487426超限，真实70；只返完整超限描述体 |
| step13 科学必要读回 | 当前reader不存在，真实exit2，未返回科学正文 |
| step14 cleanup | step本身完成，但明确removed=false |
| report来源step | 同一1626字节描述体运输成功 |
| report科学step | 真实absence/error，exit2 |

“祖先来源前缀已付”“当前来源闭包未完成”“来源完整必要正文未返回”和“科学尚未启动”是四个不同层次。本次没有把来源失败回填为数学传播失败，也没有用 report 的来源step success冒充完整必要成功。

## 609.8　清理、quiet及实际保留边界

17:23:12.0069013 UTC，cleanup 事件明确：

- event=request252_cleanup；
- removed=false；
- namespace=/home/runner/work/_temp/visible-live128-direct-loop-source252；
- reason 为 “source or original-science necessary scope incomplete; raw retained until runner destruction”；
- no_scientific_completion_or_quiet_inferred=true。

原source和science必要完成标记均未成立，workflow走的是跳过清理分支。没有调用原科学namespace清理去删除这批暂存对象。cleanup step 的 success 仅表示这个分支正常记录并退出，不能解释成 raw 已清。

该事件也没有给出完整当前science owned-process quiet证明。来源子程序已同步返回、workflow完成、hosted runner最终结束，都不能代替原namespace的PID/startticks/PGID/未知进程责任。因此本文只报告程序明确留下对象直至runner销毁的政策，不承诺具体raw占用、销毁时刻或不存在残余进程。

## 609.9　本次结论及仍需真实支付的责任

actual252确认了一条具体工程停止：来源桥调用已经返回，但独立外层的完整回执联合合同未成立。它没有提供内层错误的完整正文。该差别决定后继不能把某个猜测的字段不一致写作本次实际根因，不能声称只改一个可能字段就已修复。

第二条独立实际责任是487426字节来源必要正文未返。当前描述体本身完整、两job一致，且明确不允许清理；但是原来源图、桥接错误、完整关系报告与未生成列表的实际值仍缺。后继若改变表示，只能沿实际producer的具名语义、完整原对象与可逆同体关系处理；不能按本次未返body猜重复量，不能分包、减少必要责任或提高90000上限。

第三，科学入口、输入恢复及所有原末门本次未进入。R583的循环模式观察、原完整产品累加、原128值/模型、J/FD/fullDN、owner12000的资源策略，均没有得到本次新的实际科学证据。原条件证明和旧来源结果保持其原范围，不以本次失败回写成无效数学，也不以祖先来源准备成功升级为当前科学通过。

本条交付的是完整实际停止与证据边界。当前252执行源码、请求、workflow及原阈值均保持冻结；本次不追加科学重跑、不恢复已结束run的raw、不引入新接受门。所有未支付责任继续以本次真实字段、原单body限制和后继实际来源闭包为准。
