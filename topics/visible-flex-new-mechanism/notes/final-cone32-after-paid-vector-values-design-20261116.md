# 第 32 次有限锥调用：新细网行后的同任务恢复、完整返回记录与实际验收合同

日期：2026-11-16。本文是新增入口的静态设计，未执行新求解器、人工检查、几何、J 或 JVP。沿用已批准的有限锥方法与原总资源；只承接第 32 个尚未启动的锥调用槽。

## 1. 唯一来源与已付结论

唯一恢复来源是 run 43798128882 / job 133071559203 / source `b8577eaaa8d8327495db13bd1f684348ede6cb06` 的完整原 stdout。其人类结论为 [paid-MaxTime-vector-first-actual-and-new-soft-row-20261116.md](paid-MaxTime-vector-first-actual-and-new-soft-row-20261116.md)，已发布 commit `c99a38e230759d407c5eb2b1afb9ed62cf9d5a06`，16823B / SHA256 `4280b80ca63bd55d4476a0082ae43321b4ea5139ce6aef94c25929da29cbbe31`。

原日志 3765299B / SHA256 `9170360919ba81f563ef5a441069c6d65863c55591a9ab218193bf2833a42f51`；COMPLETE JSON+LF 3505269B / SHA256 `df20419f4e3051848d1b6dbb63ff3f0b2b31ea1f4de528108176f951b0f76731`。读取只发生一次，早期 finite-cone、末 LP 槽、geometry 的证据由这份已核完整报告传递，不再次下载旧大日志、不再次执行任何旧检查。

已付 MaxTime31 的三个尺度均未下降。第三次实际值学习了 fine ID159001，行池从4448/4543、版本13/12变为4448/4544、版本13/13。原点52、完整bank512、8补充法向、学习62events/61commits/pending0、$B=0.00025$、两个streak0均保持。该失败方向不在新入口中重试，缺失的旧$\rho$/norm不恢复或猜造。

## 2. 预算不重新开始

唯一新solver start必须记为原有限锥任务 ordinal32。旧64个HiGHS仍封存，new LP/SOC为0；方法仍Clarabel0.11.1，原设置max_iter200、max_threads1、gap_abs/gap_rel/feas均$10^{-9}$，允许进入原候选路径的后端状态仍只有Solved/AlmostSolved。

本次科学钟在读取来源日志和必要24输入之前启动，继承的最终终值是：

| 账目 | 来源终值 | 上限 | 当前可用 |
|---|---:|---:|---:|
| 同一锥任务科学秒 | 773.3401341169999 | 1200 | 426.65986588300007 |
| 原累计科学秒 | 1129.469954378 | 1800 | 670.530045622 |
| 锥任务真实值 | 60 | 96 | 36 |
| 原累计真实值 | 122 | 160 | 38 |
| 已启动锥调用 | 31 | 32 | 1 |
| 原HiGHS | 64 | 64 | 0 |

因此新入口最多使用1次锥调用、36个真实值和两科学钟的交集。它实际上只建一个模型；原最多六次二分真实验收保留，初始必要恢复两网也收费。每个solver time_limit取原10秒与两剩余科学钟的最小值。后端与冷调用非抢占，真实返回时间即使越限也完整收费，再按原后置检查退出；不能称总调用严格在10秒内。

用新启动时刻$t_0$定义锥起点$t_0-773.3401341169999$与原起点$t_0-1129.469954378$。原NewTaskConeLedger初始化后显式恢复total=cone=31、legacy=0，当前event表空并带来源收据。只有原charge函数能够把第32次启动记账，且必须在后端constructor前进行；第二次charge不可能被新入口接受。新输入/恢复失败也保留本次科学增量与全部已启动工作。

原cfg64/160/1800/10及其他数学参数逐字保持，不归一化原10.0，也不将新的记录标签或恢复时钟写入cfg改变factorizer身份。

## 3. 两种objective身份的正确衔接

最新checkpoint的objective是纯值入口：

```text
d6008a66f2939258d1b5b3f752e4f3f5235f242ca83b52bcd2b44479b376e336
```

它同时完整保存此前真实仿射objective定义及其SHA：

```text
e101bd909dbdb5fb2c7f839b2d416b66e473bf7326dfb80e7af396f3f97a26b6
```

新constructor直接初始化原RememberingCompleteObjective的数据接口，逐字段验证其真实基类definition包含于该仿射定义，验证原finite_cone_primary_method完整等于冻结方法，然后恢复这份原仿射方法定义。它不把纯值definition重命名成仿射证明，也不从旧pool绑定推新pool可用。当前field/factorizer/cfg/coordinate均与checkpoint完全核同；field仍为8e77c498…ab1，factorizer仍为b6cc198…1963。

这里继续的是同一有限锥算法，不改变数学方法身份。恢复途径、前一值-only身份和费用继承写在独立continuation metadata。新完整模型必须重新在真实点52、版本13/13和全部当前IDs上由两factory生成。其签名是当前binding，而不是来源模型27的旧row mapping或J证书。

保持原参考163/159→163映射、全部g/b0/锚/积分规则/幅宽与参数尺度。重建时仍调用已付fresh_adapter_gate接口，把同一direct场身份接至原精确null-height gate；物理门不替换。

## 4. bank、学习与新行

完整512 bank记录按原顺序与原context/state SHA恢复；8条独立补充法向全部保留。每条原ID/网格坐标与精确有理unit-ball约束继续由原恢复/重建接口核验。第一次current complete model重新绑定bank，旧512条支持及8补充支持不删除、不以同ID异法向覆盖旧约束。

学习恢复完整62events、61commits、pending空，核每个事件原committed/pending状态、gamma及maximizer、checkpoint与state SHA完全相等。constructor不调用commit或replay。新模型的原guarded_primary可记录真实的空pending模型commit；若新实际首步发生，原学习函数可以加入由这个新base/J/实际步诊断产生的新样本。不能重放旧MaxTime值验证的三步作为有J的训练样本。

输入池严格真整数、唯一、合法范围、原顺序；粗池4448/version13，细池4544/version13，包含fine159001。恢复只set原池和完整history，禁止initialize或自动expand改变入口。最初两网ordinary读取不学习新行；它们复用同过程cache供selected J、完整factory与新步。对原点52的paid scalar仅按原容差比较，不冒原数组逐位证书。

## 5. 原数学和实际资格保持

新模型沿原完整selected/J、经验curvature guard、原仿射$e/f$及有限Lorentz锥组装。新fine159001位于selected软行，因而在当前有限锥集合中明确出现。保留所有512+8原支持，以及原真实box、硬行和目标。只读旧direction的来源不作为新增solver方向；本入口不尝试复原未知原辅助坐标。

唯一新cone的完整全网oracle、$\rho$上调、原线性/盒及原单位half-cone残差门均保持。若原状态不是Solved/AlmostSolved，或修复/残差/下降门失败，候选不进入几何；即使记录了完整返回向量，也不提升其资格。若可返回，依原真实ordinary/两网门与严格下降接受，最多六次原二分。失败产生新行时按原逻辑返回最后接受点，没有SOC、rebound J或第二次solver补救。

旧covered资格字段对锥报告未全部适配的限制仍如实保留；本入口不同时修控制器或给普通fallback变化新covered功劳。真实$B$/streak、行学习、原收缩/增长fallback仍沿冻结outer执行。

## 6. 新返回的完整161捕获

此前第31次调用只保存p159。本次对真正新的第32次solution.x记录补全，必须在任何资格筛选前：

1. 如实际返回shape161且全有限，保存全部161个二进制有理数和数组SHA；
2. 保存原step_scale159、按原乘法得到的独立p159、其数组SHA；
3. 直接保存x[159]的原rho与x[160]的原norm辅助量，浮点值和二进制有理表达均保；
4. 保存当前真实snapshot_binding，包括当前A/b/c、bounds、step_scale、guard及两factory/完整oracle签名；
5. 保存可得的后端status/实际耗时及原linear/bound、finite-cone原单位残差；若后续读取或修复异常，已经捕获的完整向量仍留在event。

只有新求解器真实返回产生这些字段。不能给旧MaxTime31补造rho/norm，不能因finite161存在就宣模型合格。最终“全部保存”的布尔字段必须从原event中实际列表长度161/159与两个辅助项对应关系推导；没有有限返回时为null而非冒true。

新完整event、实际trial159/163和最终checkpoint只在runner临时文件与原stdout保留。重复原cone tags可用count/hash及完整当前pool/版本追溯，不全局压缩步向量、不上传artifact或cache、不进Git。

## 7. 费用字段的一个真实缺口

最新value-only COMPLETE保存的source_snapshot_scalar_counters仍是先前锥运行末116值的组件计时，不是六次纯值之后的mutable component totals。六条value_call_events是包装器elapsed，与原value_geometry_seconds并非同一口径，不能相加后冒作精确原组件累计。

因此本入口保留那份原组件计时、最近六条实际调用以及adapter内部99.716150581秒为独立来源收据。新value_geometry_seconds与fine_value_seconds从0记录并明确“本attempt组件”；真实值ordinal仍61+61，真正两科学钟仍完整累计，没有任何预算重置或费用消失。总费用应看两最终科学终值，不对不同口径组件重复求和。

## 8. 最小新增源码和验证范围

新增三个Python文件：

- `frame_metric_final_cone32.py`：显式恢复constructor、继续ledger/双钟、原solver路径的完整161记录补全；
- `frame_metric_final_cone32_recovery.py`：以原有限锥outer为来源，只接当前52/池13,13/模型28/剩1槽，并保原assess/学习/验收；
- `frame_metric_final_cone32_audit.py`：一次最新原log的固定指纹核验、24输入恢复、只读已付6/12/11/9收据、完整实际报告与下一checkpoint。

另有独立workflow和request。所有旧源保持冻结；不运行旧6/12/11/9，也不做新的tiny cone、镜像单位测试或旧API套件。新glue的真假在首次公开实际入口的真实身份/shape/source/预算断言与输出中暴露；源只静态审读，不称已通过运行。

若入口未能建成或剩余时间耗尽，输出所有真实准备费用、已开始ordinary/J/solver的账与最后真实点52，不能把未开始项写成通过。若cone32使用后不改善，也不增加33或重开旧64。届时依据新的完整161、残差与当前真实行数据进入下一尚未做方法，而不是原样延期同阶段。
