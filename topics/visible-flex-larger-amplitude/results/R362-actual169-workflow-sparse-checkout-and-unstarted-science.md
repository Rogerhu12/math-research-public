# R362：实际 Request 169 在工作流自检前因稀疏检出缺件停止

作者：AI（ChatGPT）
日期：2026-11-15
分类：实际公开 Actions 工程结论；原日志完整读回；无新科学运算

## 362.1 本次结论与边界

实际 Request 169 的计算 job 和只读 report job 均返回 failure。第一处错误是科学开始前的工作流源码自检试图读取自己的 YAML，但 checkout 的非 cone 稀疏路径未包含该文件。原 58 个直接源、recipe 与规则检查所在步骤因此未能整体完成；原五输入恢复、原公共源恢复和连续 C 生产步骤均被跳过。后续 always 步骤中的缺件错误沿同一缺失的临时 dispatch-request.json 传播。

本次没有启动连续 C 积分、新 profile 构造、112 模态深端/有限头传播、原生 noJ/withJ、FD、453 维 BVP 或最终 audit。没有新的数值拒绝、域反例、有限头分母证书或接受场。本条“未启动”由完整实际控制流与原 traceback 证明，不把未输出的科学调用计数伪填成实际 producer 的零计数。

最小修复是在 checkout 的 sparse-checkout 中加入本工作流路径。原数学源、58/51/25 来源闭包、当前参数 recipe、全部原验收条件和资源预算不需要改变。由于 push 触发器只监听 request 路径，真实重发还应在 request 中加入本次失败来源与重试理由，并同步工作流的 request SHA；单独提交 YAML 不会自动触发本请求。

## 362.2 实际来源及完整读回身份

公开运行：[run 43739904996](https://github.com/Rogerhu12/math-research-public/actions/runs/43739904996)。

| 对象 | 实际身份 |
|---|---|
| Repository | Rogerhu12/math-research-public |
| Dispatch source | 82fe6b4bcf593a103d3af63d68f7277c77c0eda8 |
| Workflow | .github/workflows/visible-larger-public-current-C-projective-full453-physical-DN.yml |
| Compute job | 132890537050，completed / failure |
| Report job | 132891095792，completed / failure |
| 原 request | 35286 B；2db89139012a1bdb7fdc6b07ea7f46f11eb3409531de81b34f897d4f1e08561b |
| 原 recipe | 9940 B；f8f6b353458f04052940a05bbe28d28c48b0050f631f76f813267924a31d4765 |
| 原 workflow | 86237 B；e62e93d60f87c48c8005aba2b1bb2c0b900e2594832a32f6981d516a7b46559c |

本次通过官方 job-log 接口分别完整取得两个已完成 job 的解码日志，各仅一次。读回没有下载科学大包，没有重跑任何数学函数。

| 已完整读回对象 | 返回 UTF-8 字节数 | SHA256 |
|---|---:|---|
| Compute 解码日志 | 168013 | 46c237a7387f291dfbce72e9225214755ce69cd99d47260ec13d4441404c0dee |
| Report 解码日志 | 9594 | c35b80f44a25b66497dd7ce348401d0189a6cad7a15f4f86fedaf70208daaea2 |

这些 SHA 描述接口实际返回的解码 UTF-8 文本，保留返回文本中的 BOM、换行和日志前缀，不是 ZIP、原临时科学数组或独立下载 artifact 的 SHA。全部原错误栈、always 读回、规则同步和清理输出均已读；没有以日志摘要代替未产生的科学数组。

## 362.3 第一处失败的准确路径

原 compute 日志在 17:15:24.4499294 UTC 开始第一处 traceback。Python heredoc 的第 95 行读取：

.github/workflows/visible-larger-public-current-C-projective-full453-physical-DN.yml

随后在 17:15:24.4512515 UTC 报 FileNotFoundError。实际绝对路径为：

/home/runner/work/math-research-public/math-research-public/.github/workflows/visible-larger-public-current-C-projective-full453-physical-DN.yml

该文件存在于 dispatch Git 提交中，也由 Actions 服务成功作为当前工作流解释；缺失的是 runner 的稀疏工作树副本。当前 non-cone sparse 列出了根 README、topic 文档、computations 和证明文件，却没有列出这份工作流。原源码检查需要从磁盘读取 YAML，逐段核其 shell 与内联 Python，因此服务端能启动 YAML 并不支付磁盘上可读这一条件。

本步骤的原顺序是先逐源哈希与 Python/Node 语法检查，再核 recipe、证明、规则及 owner helper，随后读取工作流，最后才写临时 dispatch-request.json 和其他运行输入副本。本次到达读取 YAML 的原行，说明此前顺序语句未抛出错误；不能据此把整个 preflight 标为成功，更不能称后面的全部工作流 heredoc 语法扫描已经执行。

临时副本尚未写出，故后续多个 always 步骤读取：

/home/runner/work/_temp/visible-current-C-projective-full453169/dispatch-request.json

均得到 FileNotFoundError。这些是同一工程首因的后继缺件，不是相互独立的 C、profile、模态、native 或 FD 失败。

## 362.4 原步骤逐项结局

| 实际步骤 | 原结局 | 已付范围 |
|---|---|---|
| 1–7 setup、checkout、namespace、Python、Node、依赖、容量 | success | 工程环境及容量原读数 |
| 8 58 源、recipe、规则与工作流源码自检 | failure | 在自身 YAML 读取处停止；整体 preflight 未完成 |
| 9 五个原数学输入及完整 453 seed 恢复 | skipped | 没有本次恢复证据 |
| 10 原公开 source subset 恢复 | skipped | 没有本次恢复证据 |
| 11 原连续 C 完整 cover | skipped | 没有 C 结果、query 或 primitive |
| 12 原 point-query 全 leaf / cut 两 jet 读回 | failure | 缺临时 dispatch-request |
| 13 R323 窗口、准确目标及数值 profile 构造 | failure | owner 执行入口缺 request，构造器未 exec |
| 14 已存在构造 metadata 读回 | success | 明确 primary unavailable、没有现存构造 metadata |
| 15 全深端行 | failure | 缺临时 dispatch-request |
| 16 物理半径采样与 projective far 行 | failure | 缺临时 dispatch-request |
| 17 当前 H、FD、完整 BVP、fresh audit | failure | 缺临时 dispatch-request，BVP launcher 未进入 |
| 18 C 原 metadata / pending 读回 | success | 明确 compute skipped、全部 producer 输出 null |
| 19 原深端行读回 | failure | 缺临时 dispatch-request |
| 20 全 BVP/native/FD/trial/failure 读回 | failure | 缺临时 dispatch-request，无科学输出可读 |
| 21 规则、资源、owner 与原失败文本读回 | success | 11 份实际原文件；read errors 为空 |
| 22 有条件清理 | success | 成功记录 cleanup skipped；没有主动删未读目录 |
| Report 的五 primary 复述 | failure | 成功复述两个 unavailable primary，传播 compute failure 后 exit 2 |

在第 13 步，原规则 runner 确实建立了 owner 进程并同步规则。其被标为 science 的独占子组运行的是执行适配入口；该入口在自己的第 68 行读取 request_raw 时就失败，尚未 exec 任何数学 producer。因此不能把这个进程标签解释成科学已经开始。

实际 traceback 顺序为：17:15:24.4512515 自身 YAML；17:15:24.6385994 cut；17:15:27.6297271 construction owner；17:15:28.0672272 deep；17:15:28.3200866 sampler；17:15:28.5766429 BVP；17:15:28.8641967 far reader；17:15:29.0475067 BVP reader。除第一项外，均指向同一未生成的 dispatch-request.json。没有被隐藏的后续科学异常。

## 362.5 原容量与规则同步

容量步骤原样输出：

| 项目 | 字节 |
|---|---:|
| 磁盘总量 | 154993672192 |
| 整理前 used / free | 62972731392 / 92004163584 |
| 整理后 used / free | 44371611648 / 110605283328 |
| startup minimum | 34359738368 |
| live free reserve | 2147483648 |

原记录明确 full_multi_call_capacity_not_guaranteed=true，原迭代和容差不变。本次第一错误发生在读取一个源码文件，与该容量检查无关；这些余量也不构成完整后续多调用必完成的保证。

规则 runner 原实际记录：

- 17:15:26 UTC 完成真实 pull --rebase，读取 main 66d8e9d100ccac2e50a893557dae645d189d726e。
- 无 force 普通发布同步提交 bba70ac253a45f20881c1b581a9ac257cdec4b00。
- 根 README blob 为 21bd547f56590b7f2dd279d0297efb289a9b2783，题 README 为 bff8aea253a9e6a7a4fac28d810ac454c5499fec。
- runner-result 原 science_returncode=1、wrapper_returncode=1、README_change=null、periodic_sync_failures=[]，science_terminated_for_actual_rule_change=false。
- scientific_checkout_modified=false、partial_scientific_files_not_removed=true。

因此本次停止不是新规则变更强制终止，也不是同步失败。以上 runner 的真实 pull 与研究环境本身是否具有终端能力是两件事，不冒称读回侧另做过 pull。

## 362.6 两个实际 primary 与报告传播

Report 原样复述并核对两个已生成的小摘要：

| primary | 字节数 | SHA256 |
|---|---:|---|
| scalar_summary | 485 | 4f70ad453a4dc917a5fa18a75ec95db5a50d212e91a5feb855d8d71fbe18acac |
| construction_summary | 438 | b9484116aab0ae7587872046a8c9e3b129a36f2147b63ff31d2136fb97bdcefa |

C 摘要的 schema 为 request169-original-continuous-E-actual-scalar-summary-v1，compute_step_outcome 为 skipped；source_result、query_results、complete_unpaid_scope 均为 null。这里 null 表示 producer 未产生结果，不表示覆盖为空、域反证或误差为零。

构造摘要保留原 request147-actual-v3-continuous-nine-construction-v1 schema；primary_output_unavailable=true、actual_existing_metadata=[]、summary_complete=false、actual_BVP_or_fullDN_success=false。后一个 false 只是没有实际成功结果，不是一次完整 BVP 求解后的失败判定。

cut_twojet_summary、far_summary、bvp_summary 均由 report 明确记为 primary unavailable。Report 的传输 errors=[]，compute_result=failure、BVP_outcome=failure，最后 exit 2 传播原计算 job 失败；不能因 report step 本身非零就再构造一种科学失败。

## 362.7 进程与条件清理的实际范围

规则读回记录实际 parent PID 2740/start_ticks 24554，公共 PGID 2161；独占执行子组 PID/PGID 2868/start_ticks 24838。最后观察中两个原 PID 身份均已不存在，独占组 live members 为空。父所继承的 runner 公共组没有被要求整体为空，没有向其他进程发信号。原 quiescent=true，unknown_owner_scopes=[]。

但 quiescence 单独不足以触发清理。原实际 readback outcomes 为：

- C、construction、rules：success；
- cut、far、BVP：failure。

17:15:29.4340156 UTC 原清理步骤打印 request169_owned_cleanup_skipped，明确 raw_left_only_until_runner_destruction=true、no_missing_readback_or_scientific_completion_inferred=true、no_other_repository_or_input_or_process_touched=true。它没有越过失败的完整读回条件删除自有目录；其 step success 只表示这段保留决定被正常记录。原工作流不上传 raw，临时目录最终由 runner 生命周期清除；本结论不声称这些未产生/未读内容已永久归档。

## 362.8 唯一必要的工程重发

在原 sparse-checkout 中增一行自身 YAML 路径即可支付首因。修改不移除源码自检，不放宽输入身份，不更换数学模块，不增加或改变接受门。原 58 直接源、driver 51 与 native 25 闭包，以及原 recipe 的 453 初猜、九参数、正 lambda、FD、32/10、严格下降、最终 audit 与所有原预算保持。

初次一行补丁（尚未加入 request 重试 metadata 时）的工作流为 86335 B / 4eb9254d3aaa5807a8656d5e953a1117e79be8bbe5ae21f77361ecb13f1f5c0f，diff 为 556 B / fe7b0afe854e3a16f59f7bac4e273ab937dbdcda8f0259bf398d7f18494fe509。这是工程修复草稿身份，不冒后续 dispatch 的最终 workflow SHA。真实重发另由 root 将本次 run/source/job/日志身份写入 request，更新工作流内相应 request SHA 后公开提交，以实际新 run 为后续证据。

本条完整支付的是实际 169 的工程停止位置、原失败传播和清理边界。完整新 C、当前 H、112 敏感度、453 BVP 及闭面责任仍须后续真实运行，不能由本次环境安装、语法前缀或 unavailable 摘要替代。

## 来源

- [原 dispatch 工作流](https://github.com/Rogerhu12/math-research-public/blob/82fe6b4bcf593a103d3af63d68f7277c77c0eda8/.github/workflows/visible-larger-public-current-C-projective-full453-physical-DN.yml)。
- [原 dispatch request](https://github.com/Rogerhu12/math-research-public/blob/82fe6b4bcf593a103d3af63d68f7277c77c0eda8/topics/visible-flex-larger-amplitude/computations/public-current-C-projective-full453-physical-DN-request.json)；实际文件身份以本文 SHA 与原工作流读取路径共同定位。
- [R348：原 159 的实际完整 C 与未起 BVP 范围](R348-actual159-complete-C-far-work-limit-and-unstarted-full453-BVP.md)。
- 原 job logs：GitHub Actions run 43739904996 的 jobs 132890537050、132891095792；完整解码文本身份见 §362.2。
