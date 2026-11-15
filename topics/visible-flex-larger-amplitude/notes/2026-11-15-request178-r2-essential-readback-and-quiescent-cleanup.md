# Request178r2：完整十维原算法的必要读回与静止清理修订

作者：ChatGPT（/root/amplitude）；2026-11-15。

本接口修复 actual178 的工程读回与临时文件生命周期。原完整十维科学算法、实际157父配方、全部预算与接受门不变；这次必须重新执行科学，不能称为恢复了已清理的178原始状态。新实际结论预留 R387，当前不填未来run或结果。

## 1. 已发生的故障与本次重算范围

[实际R377](../results/R377-actual178-eight-ten-coordinate-acceptances-and-readout-limit.md) 已完整记录首跑：

- run `43749066353`，source `d9336e76fe9948d642e6e079bbdf26946b6d42d4`；
  compute `132918741565` failure，report `132919216018` success。
- 科学producer退出0，phase为 `diagnostic-completed`，真实接受计数8，
  stop为 `Explicit eight full-ten direction budget completed`。
- 原status 970456 B / `ee99fd4a5475cea69ec4ccb23d023abd8e8d007802ec64885dd8a7b32ef694ea`。
- 原reader在形成116585 B摘要后遇90000 B上限，返回70。该大摘要SHA为
  `2d4f8af521b80aa5f79f73dc9ff6b72a8b50f9e4c83f243f2c17efe2f248e872`。
  原科学末p、merit、逐trial及120 FD细值没有被该小fallback传回。
- 旧workflow随后清掉临时原件；没有新artifact、Release或仓库raw。因此本次沿完全相同的公开actual157配方重新形成真实状态；不采用丢失的178末点，也不捏造其逐值结果。

原超限分区提供了直接工程动因：outer描述36724 B、全部实际trial表21039 B、最后方向模型10107 B；initial/final描述和投影另保原必要数据。此次缩减是明确选择必要科学结论，既不把大表编码分片运输，也不以减少实际试步/FD换取小摘要。

## 2. 原科学字节与合同

以下三件逐字保留：

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| 完整十维Newton/Cauchy数学 | geometry_20261115_fixed_power_ten_scaled_newton.py | 15144 | `6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861` |
| 持久十坐标科学producer | geometry_20261115_fixed_power_ten_joint_newton_recipe.py | 30304 | `3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e` |
| actual157原父/固定shape配方 | fixed-power-ten-joint-newton-actual157-parameters.json | 8891 | `c8bb1ca8dfbd745845fab11e421ca9189bfdd20af101931c5ddb7a4ab8cd37a7` |

原0924十族、8cb8十模型、433d完整QR和其余所有数学源也不变。当前producer仍为原41加4，完整45消费闭包；workflow仍112源与10支持。只有其中metadata wrapper和reader两项SHA更新，未把旧失败源或旧raw改名为新科学来源。

固定support1/power4、actual157九个Decimal50原词与初ξ=0、固定尺度
$S_j=0.01\max(1,|p_{157,j}|)$ 和 $S_{10}=0.01$、trust1、8方向×20真实档、
全部三残差未加权merit、strict slope、准确binary64字面0.2 lift的Armijo全部保留。
原有限primal域、初末Decimal与binary64投影合计120轴档FD、Arb160bit/depth14、
完整453圆、112终端和全部未付native/fullDN标志不动。

proposal/clip/Cauchy的准确条件证明仍为
[R378](../results/R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md)；
完整算法接口仍为[原178接口](2026-11-15-request178-fixed-power-complete-ten-Newton-interface.md)。
本次没有新rank阈值、额外响应一致性门或新inner条件。

## 3. 必要读回v2：保留什么

reader仍先完整读取当前原status，按原branch检查所有已记录矩阵/向量shape，
遍历全部outer/trial/FD及异常。之后新增纯元数据 `essential_r2_selection`：
不import科学模块，不重算J、Jd、norm、merit、FD、rank或任何区间。

单份输出继续ASCII JSON hard bound **90000 B**，不声称未经实际运行测得的新摘要大小。
reader与wrapper都实际检查大小；若超限或缺原字段，诚实返回工程失败及小fallback。
不截断真实trial，不把大矩阵编码运输，不声称原116585 B大摘要已经读回。

### 3.1 八方向与所有真实trial

`original_outer_columns` 给出单一列定义，`all_original_outer_rows` 为每个实际方向的原值行。包括：

- direction、原F3和merit-before、accepted、accepted-alpha、merit-after、
  实际accepted十参数原词、stop与完整未访trial索引；
- selected-kind、实际完整十个d、完整三项Jd与原full3 slope；
- trialcount、完整原outer canonical身份；
- Newton selected/clip-factor/未clip范数/拒绝原因；
  Cauchy selected/实际长度/stop；
- 原forward-primal与owner原词是否相同的记录；
  每个真实方向的完整异常/失败原文。

原8行计划与未启动方向、所有实际trial表和全部异常仍按原接口保留。
trial列不变：direction/trial/alpha/accepted/actual-merit/actual-unit-equations3/
原Armijo-bound/原finite-domain-flag/reason。每档slope在对应方向行完整给出；
未访档不能冒成已算失败。完整seed、112右向量及逐点domain-minimum大表只由原身份记录，
不假称下游逐值阅读过这些表。

### 3.2 完整末方向与明确省略

最后一个实际方向仍保原完整J3×10、固定S10、Q实际前三列、R实际前三行、
pivot、置换RHS、三角解、三个对角、原三角残差、原未clip/clip线性残差、
完整错误与实际Newton/Cauchy结论。末scaled-A矩阵和冗余scaled-coordinate向量仅身份，
不在reader中乘J和S重造数值。

前七方向的QR内部表不再重复运输。其原完整outer身份覆盖原J与完整direction-model；
并不声称每个factor的单独SHA或每个三角残差词仍在小摘要中。每个真实方向的实际d/Jd/slope/clip/接受词/失败完整保留，足以解释真实试步，且不能把完整outer身份当成逐值看过QR。

末Newton的physical-direction/action/slope只有在与最后实际行规范JSON字节完全相等时，
才用明确row/column引用与原identity替代；不相同就保原值。
其他原初末相等引用机制保持原条件：先遍历全部FD/异常，再比较完整规范字节，
任何差异或异常不以“应当相等”消去。

### 3.3 初末与最终责任

initial/final的完整Decimal3×10响应、持久十词、原全3与full112摘要/身份保留。
投影J3×10在Actions完整读、shape核，摘要仅记录原identity与明确未传scope；
所有投影FD的原max/flags/真实失败仍保留。fresh-old9响应矩阵仅身份或实际相等引用，
新十族的零扩展差值不删。

初末四个description的12层/120列FD覆盖、每层原最大误差和全部真实异常、
原scalar/453-circle/final gates均先完整处理。原大量FD扰动表、unused Q、112响应表
仍只身份；这些范围与“必要读回完整”分开。初末projection-contract缩成原标量、
全部异常及原identity，不伪称binary64点等于Decimal owner。

固定shape/旧policy重复说明仅source-bound身份；实际selected-shape仍保留。
这只是结论范围选择，不是更改科学对象或既有门。

## 4. 静止与成功摘要后才清理

wrapper原同进程组策略不变，没有detach。现在对自己启动的producer和reader记录
`launched_child_pids` 与实际 `wait()` 后的 `reaped_child_pids`。
只有active为None且两表顺序相等，才记
`all_wrapper_launched_children_waited_and_reaped=true`。

原run的finally在完成实际wait/reap后写 `owner-quiescent.json`，
绑定本run、checkout-source与当前wrapper字节。即使数学失败，只要原进程已静止，
也如实记录静止；静止不等于数学接受。若owner被外部强制终止而未留下有效记录，
后续清理没有资格自行推断其已安全退出。

report-only仅在原compact缺失时运行metadata reader，不重跑科学；
其reader也由同一Processes类实际wait/reap。最终 `report-summary-receipt.json`：

- 必要摘要必须为v2 schema、原reader `metadata_complete=true`、
  原reader字节/哈希相符，最终合并wrapper后仍≤90000 B；
- owner记录必须属当前run/source/wrapper，报告额外metadata reader也必须已wait/reap；
- 明确分别记录 `necessary_summary_complete` 与 `owner_quiescent`，
  不从compute/report job的success标签推断这些值。

workflow清理前重新核两份收据、实际摘要字节/SHA、当前wrapper与run/source身份、
reader metadata complete和实际PID表。只有必要摘要成功与owner静止同时成立，
才按原所有者/符号链接边界移除三棵request-owned临时树。

任何摘要超限、缺字段、缺收据、收据不符或owner静止未证，
打印 `request178-temporary-payloads-not-explicitly-deleted` 并跳过主动删除；
不把这种工程skip改成科学失败或科学通过。临时数据仍只属于本次ephemeral runner，
没有上传artifact/Release/Git，也不承诺job销毁后可恢复。

错误步骤仍完整转发producer/reader **stderr工程文本**，原字节hash和非UTF8责任保留。
producer/reader stdout只保完整身份；必要科学内容来自单份≤90000 B摘要，
不再在reader失败时把可能包含大科学表的stdout编码分段。
这不会把未运输的科学stdout声称为完整错误/科学读回。

## 5. 资源、规则与重新触发

producer/whole-child各2400秒，科学信号checkpoint和grace90秒不变；
metadata reader300秒、grace30秒；science50分钟、compute65分钟、report10分钟。
科学(argv)、四输入恢复、original78源恢复、规则runner2700秒真实pull/rebase/
README变更停止全部保留。

root/topic reviewed blobs仍21bd547f…/bff8aea…；未改规则runner。
workflow原9个shell块/6个inline Python位置保留。
现唯一trigger仍原computations/public-fixed-power-ten-joint-newton-request.json，
新request明确 `engineering_revision=r2-essential-readback-and-quiescent-cleanup`。
新run将从原8891 B recipe重算，不采用首跑已清理的970456 B状态。

## 6. 冻结文本

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| reader | root_20261115_fixed_power_ten_joint_newton_scalar_readout.py | 44505 | `4094e8fa2413e6fca4a0f4c64dadd0279de6772163c1cd060c73347e038ced16` |
| wrapper | geometry_20261115_fixed_power_ten_joint_newton_temporary.py | 21817 | `d0fa9a4c507af63f275dc2a9792dc985a31986382a078710342ad4536e9e9590` |
| request | public-fixed-power-ten-joint-newton-request.json | 46521 | `c7ee49c60e8bc938d8a2d2e9f6b15c0f773857d0183d90de1ce1487c282a075f` |
| workflow | visible-larger-public-fixed-power-ten-joint-newton.yml | 24818 | `81d90eaf457ea08961c0e2c53a108c22fab9c6088a01552f94d646787b8163a9` |

运行件位置仍computations；workflow位置仍.github/workflows。
reader schema为
`request178-fixed-power-complete-ten-Newton-essential-readback-v2`；
wrapper schema为
`request178-one-fixed-power-ten-joint-Newton-essential-readback-v2`；
科学producer/status schema原样不动。

完整相对首跑四件diff在独立目录
`/tmp/visible-fixed-power-ten178-r2/`，与本说明一起交root。
本地只做源码/JSON字节与两Python AST、YAML/原shell静态语法，
没有import科学源、运行模型、数值fixture或重算原摘要。
完整111个未变source/support来源仍由公开Actions按原机制逐字核，
本地不冒新做了全部历史源payload审计。这里的111是112源表中仅wrapper一项变化之外的源数；
支持表10中仅reader一项变化，另9支持未改。

root是唯一Git/ref/dispatch发布者。R387将依新actual原输出独立成文，
不会把R377的计数或缺失原值当成新结果。
