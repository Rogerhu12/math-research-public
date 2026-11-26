# 独立 direct-SO3 warm 输入再生入口

日期：2026-11-26。本条只给完整输入编排，不登记新科学返回。新源不改变原恢复 producer，不把历史标签当本次输出身份；科学计算仍只在该公开仓库 Actions 执行。

## 1. 完整来源与接口

新路径：scripts/resume_20261126/rebuild_axisymmetric_so3_warm.py。

完整源码 22706 bytes，SHA256 561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4；未引用源码 blob e990e26f48fbd43ecbb234850ea5287511dac10a。只存源码，不存任何 raw 或数组。

CLI 为 --repo REPO --work WORK --stop-after warm，另可传 --status STATUS（默认 WORK/status.json，相对路径以 WORK 为根）。stop-after 只接受 warm。全部 raw/status 必须在仓库外的本次 WORK。--print-only 只用标准库读源、核 hash、打印命令，不导入科学模块。

真正执行时，外层唯一科学命令是原已刊来源：

    python -u REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/reproduce_and_solve.py --repo REPO --work WORK/fullclosed_solver

没有 --implementation，原 reproduce 中有条件的 fullclosed_lm 分支不会运行。新计划本身只有 warm 一项，不导入旧 rebuild_a04_chain，也不先生成再切片一个长旧计划。

原 reproduce SHA067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d；prefix recovery SHA4e9ddeaeef2a0ab8b1b38b1412eb066b53578dd649d8f9b4d1a077c7256dee6b；warm recovery SHA63950b72e75e8b6497ad2119ca16076c2c8749f9615166beb6d52adcab86708e。它们的完整函数体、实际 producer 和科学参数均保留。

## 2. 必要恢复范围

从真实历史 accepted .99 blob 开始：commit 60321451c058c6a51da58c37ae5ec6f2d1145f74，路径 notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz，SHA256 b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff。该已登记真实输入由原源码恢复；不用 hash 伪造一个新场。

保留原完整五步 continue0991、continue0992、refine0992m112、continue0993m112、continue0995m112。duration、boundary 输入、fixedmodes3、M112/N2048、原容差/节点预算与默认 separated-QR 均由未改动原 producer 执行。每步须真实 success，最后是本次实际 .995/M112/N2048 prefix。新入口核整个阶段序列和每一步实际输入/输出 SHA。

随后保留原四阶段 pulse_shared_jets、assemble_common_prefix、fullclosed_hold_warm、fullclosed_mode_damped_warm。pulse IVP、公共 jet 桥、完整 Hold/M160/J923 和 mode-damped warm 均保持原定义。mode-damped 仍由完整原 reproduce 生成；新轴对称 T0 准备实际消费 Hold warm，不能混用两个 bundle。

不运行 af89、e8、2038、a04、continue 或之后已登记的旧优化方向；不复跑旧大 readout/连续证书；不生成旧优化 Gauss carrier。新准备入口按原观察规则生成自己的完整 legacy+Gauss 正权 carrier。新 SO3 物理场和求解由后续独立来源执行，本 recipe 不声称已执行它们。

## 3. 新准备入口的实际路径

以下相对 WORK：

| 角色 | 路径 |
|---|---|
| 原 complete Hold warm bundle | fullclosed_solver/data/fullclosed-hold-warm.npz |
| 该 bundle 的真实 producer/节点报告 | fullclosed_solver/data/fullclosed-hold-warm.json |
| 同一真实 assembled pulse/scalar | fullclosed_solver/data/pulse-a5-complete-base.json.gz |
| 原 prefix journal | fullclosed_solver/rebuild-prefix-manifest.json |
| 原完整 warm journal | fullclosed_solver/rebuild-closed-warm-manifest.json |
| 完整原 mode-damped 输出，保留但非新准备主输入 | fullclosed_solver/data/fullclosed-mode-damped-warm.npz |

历史 mode warm 的79c161...仅为历史比较字段；不要求新运行命中它，不把新 Hold warm 身份改成它。所有新文件 SHA 等本次 producer 自然返回后记录。

## 4. 来源、状态、续入和失败

新源绑定21份实际恢复及导入项目依赖：三份编排/恢复驱动、continue/default separated-QR、Frenet/profile、pulse公共jet/helper链、assembly、完整Hold scalar/integer链、两个warm producer。编排层只读文件和hash，不导入这些科学模块。执行前逐份核当前 checkout HEAD:path 字节与实际文件一致，新recipe自身也在此检查内。

原 producer 的完整 source/hash 和显式 identity rebinding 记录保留于原manifest。新入口额外核完整schema/阶段序列、accepted099及五prefix链、warm各producer真实输出hash、Hold M160/J923/922cells和pulse输入、mode-warm的真实父bundle/report/scalar，以及原prefix819/core前三项保持标记。检查只读JSON与文件hash，不加载numpy数组，不重算F/J，不冒科学证书。

外层继续写 recipe-manifest.json、recipe-logs/warm.log、status.json（或显式status）。status的stage/state/completed/failed/identity，以及completed record的name/returncode/seconds/scope/source_commit/source_sha256/command/input_files/outputs/output_bundle_sha256/report_sha256与既有publisher/followup合同兼容；新schema明确为direct-SO3 warm。

自然返回记录包含真实Hold/pulse身份及完整mode-warm身份，全部raw留runner。失败保实际返回码、来源和日志；未通过完整返回检查不加入completed。同一source/input身份下重入只复用逐hash核对的本次warm文件；未登记旧raw不被接管。已有后续followup记录时，核对首个唯一warm记录并保留后续记录，不删改或重放其结果。

recipe_finished只表示这一个输入recipe完成。连续证书继承、SO3 prepare已执行、topic completion标记均为false；job终态不等于课题完成。

## 5. 实际纯元数据验证

失联前已从真实公开工作副本读原完整源码、producer结构及controller合同，并用标准库逐份读取上述21源SHA。环境短暂失联后，完整最终源先存入上述未引用blob；scratch早期稿不作为最终身份。

环境恢复后，已从内存最终字节恢复源码并实际执行Python AST解析与compile，22706 bytes / SHA256 561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4与blob相同，均通过。toplevel imports只有标准库。

原完整repo当时未恢复，因而通过GitHub读取已公开commit 93bbc4dac68b6bfb00b909a8ade1c30e132c3959 中这21份完整来源；逐一SHA256全部与绑定相等。将真实源码文本放入独立元数据检查目录后，实际执行最终recipe的 --stop-after warm --status status.json --print-only，exit0，输出stages=1、pinned_sources=21、scientific_subprocesses_started=0，唯一argv为原reproduce --repo ... --work .../fullclosed_solver，无implementation。该目录只有真实源码，不是科学fixture，也未被当成完整Git checkout或任何科学输入。

正式运行时的HEAD:path字节核、历史blob恢复、五prefix科学续解和四warm阶段尚未执行；这些需要正式公开Actions的真实自然返回。本文只更新已经完成的AST/命令规划事实，没有把它们升级为科学成功。

未安排新科学fixture。本recipe只把必要真实输入交给新的direct R690 scalar/T0/prepare；完整SO3与零闭合差隐式修正继续由各自独立全源处理。
