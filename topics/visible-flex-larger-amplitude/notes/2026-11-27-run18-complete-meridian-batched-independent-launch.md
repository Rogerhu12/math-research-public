# 公开18：完整积分复用与缺失角批处理的新独立求解

## RET85：终态导读与完整历史记录

**已知后继终态：** 本文原始 41b4/d3f1 入口实际失败，完整 frame/_meridian_data 异常和 traceback 原文保留。随后同一 run 46062343475/1 又经过两次不同的真实入口失败，再由 producer-bound 族进入科学，最终官方 cancelled；取消原因及完整最终场仍未知。完整后继记录见[producer 修复与终态](2026-11-27-run18-complete-producer-binding-repair-and-continuation.md)。后继进展不把本文失败源码改称成功。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。5 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 53587 字节；SHA256 `d5377d11be582ceecbdc7b1fa72d0a36f7dd744639346c7d7c1219e241abccd1`；Git blob `2bf31c348caf5808d6d801e41164d9e85c82bc2a`；固定提交 `1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET85 完整交付表](../computations/terminal-run15-18-narrative-retention-85-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

2026-11-27 20:13:34 UTC；Astra-larger-e4e2a2bf-20261126（AI）。**本次提交全启动对象；真实run/job/input/field要在官方触发后另行归属，当前不填结果。**

## 1. 已刊完整科学族

完整源/证明/所有原参数已在6bb07451de8b7476a36c799c4fced3a642aa8bde发布：[完整入口说明](2026-11-27-complete-meridian-batched-solver-entry.md)、[78671B总表](../computations/fixed-fejer-meridian-batched-complete-delivery.json)。39件共1599149B，18完整runtime，137 source roles逐对保原120。

- 完整driver41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2，99313B。
- 完整pure d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52，99382B。
- 完整launcher b54cd45d9fb71fe082f3f4403a595296203883aedc84fb3ac0d0d4c0625d9d12，22136B。
- 当前normal388c/cache7aa/geometry51b7、完整source binder15cd/history ae9e/pure geometry binderf7e1；均是完整独立源，全部父对仍在实际role表。

同一固定g、M160/J923/N2048、全部1,333,370坐标与32stage、原QP/15 rays/恢复/根/积分/域预算和原active J/J*保持。宽seed仍b/S1/4、delta1/32，与17相同参数；只改已详明的plain-detached integration复用、真实缺失角按原8角批处理及观测。每次field仍走原implicit，原每stage/final强制复读与原地点loop保留。没有速度、跨批working字相同、field接受或连续界的预设。

## 2. 完整启动文件及精确原字恢复

这四个完整启动对象随本note同一提交发布；Git blob直接给出原字，之后不改request文件来记运行状态，避免重复push触发。

> **原 JSON 01：完整启动对象身份。** [固定旧版完整记录，第 20–51 行](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md#L20-L51)。


初始queue为63936B，完整三步顺序是：

1. 原6词maker，source89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60。
2. 原26词2218/reference，sourcee7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb；仅step-id run17→run18，不改数学参数、output或summary。
3. 本完整新157词科学步complete-fixed-fejer-meridian-batched-first-20261127，458正式summary、48 live（6normal+42数学）。

[完整科学ready](../computations/fixed-fejer-meridian-batched-science-complete-ready.json)76339B/48be07d523cf6330a23808567a95acd4927aaf1b487cd5c8e5f35176acff1a64以及[完整纯读ready](../computations/fixed-fejer-meridian-batched-pure-complete-ready.json)65979B/000d83d7bb4ecf3f0ef97a266846d52e2dfa79e50a2ad725fa361110ead9459f保全部原157/7 args、原408/395正式selector，新增50各成458/445。完整科学+pure的最小queue是104141B，大于原95000；本次只先排三完整步，完整pure预声明保在原单步文件。科学真正自然回传后，再保完整原active对象/真实输出，退休真返对象并接整个pure与后继；不剪参数、不裁selector、不以平台退出或progress冒complete。

raw报告、checkpoint、packet、mesh、数据及每trial小记录只在本runner，不从17搬运或以旧输入充final。固定参考cache的保留责任和原cleanup_generated_patterns都保。

## 3. 控制器和规则同步

新controller只作两个slot标记、Actions18标签与并行18规则标签共四个单处身份替换；完整19984B控制流及所有限额原字保持。workflow只换身份路径及准确工作描述，完整dependency固定Python3.12.14/numpy2.3.5/scipy1.17.0/torch2.5.1 CPU、原partial checkout、contents-write和350分钟上限保持。GITHUB_TOKEN仅controller环境，科学child清除；未把用户令牌写入文件。

每次真实pull都查根README和课题README差异并照新规；通常五分钟真pull，至少一小时。子进程的detached源码树不受publisher pull改写。root云核不是root真pull；终端失效边界和恢复后pull责任保持。18自己的实际rule-read commit由controller逐次写HANDOFF的独立slot。

controller20000秒是新阶段admission checkpoint，活child不因它被声明完成；平台350分钟上限也不是科学完成。12已实际cancelled但原因未独立核实、没有完整科学返回，新18不把其可能的未知末场或typed history删除。所有原五支持peer的CLI全保，13–17五个未支持来源仍完整unknown/unconsumed/unmigrated，不加source别名。

## 4. 新观察的作用

新observer保每次原完整/partial geometry实际六signed g及所有最大项，并保上一真实已返回trial的point/Phi/Gram/g/accepted/maxfamilies。下一trial开始不会覆盖上一完成trial。标量文件限16KiB、仅runner，失败不改science；它不是继续程序的断点或13-member final。current始终由原接受/原final事件更新，统计读出不冒accepted。

## 5. 全完整request

> **原 JSON 02：原完整启动 request。** [固定旧版完整记录，第 77–371 行](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md#L77-L371)。


## 6. 实际返回位置

本提交时actual_run_id、input whole identities、model/point、report、接受/几何、准确费用和真实mesh精化均尚待返回。后续只在本note和H/log/open记录真实官方事件，request/controller已执行对象保持其原身份。

课题仍未完成。完整有限场回传后继续全准确normal/六jet/全phase帽mixed/R650/hold/reach/R716 δE及固定参数真实mesh/frequency/t精化，直到README全部标准达到。

## 7. 官方真实启动与research已进入

在2026-11-27 20:16:30 UTC官方只读复核中，真实run **46062343475/1** 已存在，created_at及run_started_at均为**2026-11-27T20:15:09Z**，head为本次成功启动提交**1b76cb746b3b6cd5d9b9c5b9d20fc83a0e3e838c**。真实job **140719355272**，依赖安装已成功，research step已in_progress。此观察尚未读取原input/科学的自然返回小卷，故不提前给实际输入hash、初场或解。

首次普通update返回UNKNOWN并伴并发HEAD前移，root立即freshHEAD完整合并重推；第二次普通update成功，未force、不冒终端pull。官方实际head为1b76，不将未挂ref候选a8c925当本次实际执行源。request及初始63936B三步对象此后保持不变，实际controller逐次记录detached scientific source与各步骤whole输出。

完整本次官方投影及jobs包装如下：

> **原 JSON 03：首次官方 run/jobs 观察。** [固定旧版完整记录，第 387–457 行](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md#L387-L457)。


原完整pure7词/445formal已完整预声明，只有真实科学返回才接入其文件；潜在input成功不等于全场完成，任何partial/progress/final待实际读取。README全部指标仍未完成，继续实际求解和完整后继。

## 8. 实际两输入返回与首次科学入口失败（2026-11-27 20:33 UTC读回）

实际公开run46062343475/1仍在同一runner中。本次完整读取index18043B/8a5f6288db9444cfce7e396da6c8bb36e14fa3dcbfddcd1146881214ccef219b/blob555262b02f35a2f61c5bbba62ba35589ed389a78，index记录时间20:24:24 UTC；原阶段1–3完整卷25988B/fa3fb4dc766ccf545b141277ca2183704fe57612838ba04ffc9c48c2e919e04b/blob37a491f9d7515642303c646af71aab6e6e32fe5c，完整原字可在[274011固定卷](https://github.com/Rogerhu12/math-research-public/blob/27401143b962360a11428510018644a2ed68f7c1/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46062343475-1-part-001.md)恢复，含三步每个实际完整命令/输入/输出及所有已读标量。

maker实际0，耗时5.993991221999991秒；reference实际0，469.98148855100004秒。六固定原输入值的SHA与已刊recipe预期一致，但本run的preparation/locations/history/binding各有自身真实身份；完整原卷保所有字段，不以deterministic值替代实际报告。reference完整2218leaf/infinite tail，accuracy_reached=false。只有输入完成，尚无新的场证明。

完整新science实际exit1，8.147090872999911秒；它已经读到自己的launcher命令计划50540B/491c172cebc830da4af9449b669ebd3f6b684dd0887357755c099b71778b07d3，来源commit7936ae753065d6e47c1c02848551020acf5a7b2a/source b54cd45d9fb71fe082f3f4403a595296203883aedc84fb3ac0d0d4c0625d9d12。实际report不存在，完整失败记录如下。不能据8秒、缺report或已写command猜F/J执行数、内部异常、根/几何失败或数学不可能性。

> **原 JSON 04：首次科学入口失败完整返回。** [固定旧版完整记录，第 469–705 行](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md#L469-L705)。


### 原runner实际异常读取

接入现成完整8679B/5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360 reader，不改源码。它绑定实际status的唯一returned failed step、实际launcher源、原log0003-dc8fac08e2e4；原64000尾字节/每traceback7000字符/全部selector与是否截断、是否完整日志的区别全保。父是确已返回的原reference212eb5，不是缺失的场报告。完整参数[resume-20261127-run18-actual-first-and-last-tracebacks-ready.json](../computations/resume-20261127-run18-actual-first-and-last-tracebacks-ready.json)16741B/d10070867e35b597f7759b7aae6ceb22b7fe3e81116b25d15695b3c6d762367f，新队列4720B/9301462176f00adb00808799342e052dca5e47bf52b80f22851d188487f5dc6a。

原63936B三步现在均真实自然返回，才从活队列退休；三个完整原对象固定保1b76cb746b3b6cd5d9b9c5b9d20fc83a0e3e838c下同queue路径，完整science ready与pure ready仍保，所有参数/原预算/outputs/summary无删减。新队列仅只读原异常，finish=false。失败原因还没有回传；必须据实际异常修完整来源族并换独立新输出路径，不冒充成功父，也不重做两已返回必要输入。

## 9. 原异常实际归因：新 meridian 方法的完整绑定不匹配（2026-11-27 20:36 UTC）

同runner实际只读步骤已exit0，source commit b07c0aebbf6125cfa1a7e1b595b84ab3d67be3ca、reader5d25原字；输出11675B/SHA25685cbea9228c60fd15a6c6e7397bd3a3e39e6e33bc349d8305657588abdbe131b。root完整读取阶段1–4卷42893B/ac49f5b0f00b2a7185be88b7a0c0593e74d67978b172e5c2a2e72c062ac463ab/blobb4c479790c2d90184be6f42d77322affca66af5b，全四步原字固定[36fb阶段卷](https://github.com/Rogerhu12/math-research-public/blob/36fb3539d71ac8826645df636359d34769f786e9/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46062343475-1-part-001.md)。

原日志7167B/1baa32787375046913bdb762ff4d57db990e0e8567d75cd8b03f13834d5d190d，从byte0完整读到末尾，两次stat一致；共两个traceback，首异常实际是：

```text
Traceback (most recent call last):
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0003-dc8fac08e2e4-7936ae753065/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py", line 1130, in <module>
    main()
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0003-dc8fac08e2e4-7936ae753065/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py", line 544, in main
    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0003-dc8fac08e2e4-7936ae753065/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py", line 489, in __init__
    self.analytic_normal_frame = analytic_frame_module.AnalyticNormalFrame(self)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0003-dc8fac08e2e4-7936ae753065/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_analytic_normal_frame.py", line 372, in __init__
    raise ValueError('A full original method or the explicit frame wrapper changed: '+name)
ValueError: A full original method or the explicit frame wrapper changed: _meridian_data

```

第二异常是launcher对已失败driver的CalledProcessError；首末traceback正文均未裁剪，只有单独的末异常行摘要超过2048字符而显式裁剪。两个异常不能合成一个虚构原因，也不把外层CalledProcessError当最内层原因。完整各标量、准确status与日志identity、所有scope和原完整命令均保上述固定阶段卷。

这次实际拒绝来自 analytic frame 的完整方法文本绑定，点名`_meridian_data`。修复将以真正当前完整新方法的精确identity更新相关来源绑定，并贯通所需完整lower/upper/reader/参数来源链；不删除guard、不允许旧hash冒新方法、不改数学公式或原科学预算。原失败版本的完整137来源、所有120父pairs、原命令和原输出路径保持固定Git可恢复；将使用独立新输出路径继续，不能重用原已存在command。修复后的数值表现仍须新的实际运行给出，不能从本次文本错误推出场、根、收敛或几何结果。

完整诊断标量对象保如下；其中field_or_J_evaluations=0只说明本只读诊断没有科学求值，不能据此反填旧失败driver的执行计数。

> **原 JSON 05：首次真实异常完整诊断。** [固定旧版完整记录，第 741–789 行](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-meridian-batched-independent-launch.md#L741-L789)。

