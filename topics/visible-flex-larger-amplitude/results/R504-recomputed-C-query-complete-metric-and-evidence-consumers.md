# R504 — 同一 C 的新完整查询进入六个实际 metric / evidence 消费者

- 日期：2026-11-16。
- 作者：ChatGPT（AI，geometry 协作代理）。
- 可信度：**已证明（限完整来源组合与原算法条件命题）；源码/完整字面差异已写，未执行科学或生成实际证书。**
- 本结论接 [R500](R500-same-C-recomputed-head-and-complete-tail-query-enclosures.md) 的真实查询 API，保持 R495 及所有已冻结请求原字节不动。

## 504.1 本次支付的是外层真实调用

R500已经给出真实API：先按原field完整绑定旧C四件，再按R489/R492实际来源读取同语义新C四件，合法合并闭查询；live路径真正使用新source panels和重算累计半径。它没有在发表时自动改六个外层入口。

本次新增一个固定查询薄接口、一个标准库source-view生成器、一份完整before/after/count计划。计划生成六个独立新名的完整程序，实际调用R500，保原准确场与数学核心。展开程序只在Actions实际computations中形成，不把六份约五万字的无改动核心重复放进Git。

真实范围是：

| 角色 | 原有查询能力 | 新实际路径 |
|---|---|---|
| fixed_original112 | 只消费已返回的固定闭查询 | 新固定薄接口：原旧完整query与R489实际query合并；不启动live |
| live_original112 | 一个R426 live oracle | R500唯一原live，源为实际R489完整头部 |
| live_resolution112 | 一个R441族live oracle | 同上，原真实分辨率场loader保持 |
| live_completeM | 一个完整M族live oracle | 同上，原真实M场/全部节点与材料保持 |
| live_incrementalM | 一个R464族live oracle | 同上，原union CP/实际field来源保持 |
| evidence | 原来已有live/refine、全t查询及误差比较 | R500唯一原live，完整norm/coverage/t/compare仍原算法 |

evidence原本就有LiveQueryTarget及实际refine调用；本结论没有把它降成fixed，也没有声称它是新增的oracle。固定metric原本没有11个query工作参数，本结论也不为它假添这组参数或新预算。

## 504.2 每条实际链都先付原场，再付新求值包围

原独立场loader、原R495四族类owner/源码核对、原R492 provider、原完整C/CP/definition/raw节点/材料/十参数绑定都先真实执行。

对原closed metric，之后仍逐段执行：

- R413真实cuff与目标atlas；
- R417同一实际两帽graph/target恒等式；
- R495完整准确prefix/cut求值与R483完整coast表达；
- 原完整active根分区；
- 原四Loewner及闭DFS、所有反射、闭角端点、patch和piece seam。

只有tail query对象的来源改为新独立R500接口。原g的径向项仍E_C(r)，角项仍r²Phi_q²；没有改成几何B导数，没有选择C盒中心，没有改field/nodal words，也没有借用旧accepted结果替当前分支付账。

## 504.3 固定角色没有新增live工作

固定薄接口源码：

[geometry_20261116_same_C_recomputed_fixed_query_consumer.py](../computations/geometry_20261116_same_C_recomputed_fixed_query_consumer.py)。

它复用R500的实际类owner核对、原ActualCompleteCTarget、FixedRefinedQueries和SameCTailQueries.bounds。固定对象中的FixedQueryOnly只提供已读query表的bounds与空cache，不是LiveQueryTarget：

- 不初始化新的C积分runtime；
- 不建立live query journal；
- 不运行QueryCover或新中点积分；
- 不创建query seconds/panels/nodes；
- 不增加任何工作参数。

旧和新两组完整闭query使用同一个R500覆盖/交算法，所以有效性直接由R500条件命题给出。其cuts仅是构造时已返回的两组实际闭区间端点的固定并集。仍须原完整根分区和DFS支付所有cell，不能把更细的query边界当作已经证过的metric叶。

这里保的是原根分区算法及完整闭域责任，不是强制旧rank数量逐字不变。若两组真实query端点改变了初始radial cuts，必须重新按实际cuts生成planned_roots并遍历全部新rank；不沿用旧证书或旧已付前缀。DFS启动后的query仍不能改该次已冻结的root集合。

固定entry从来不会调用refine；若外部明确调用该方法，薄对象只返回attempted=false与固定角色范围，不凭空启动一个oracle。它没有以“没开live”假称原未付query已完成。

## 504.4 五个live角色没有第二个钟

四个metric的实际替换都是：删除原固定target加LiveQueryTarget两行组合，换成一次R500调用。原started、原budget_seconds、原11个c_query参数和R495实际绝对clock clip均保。不存在旧Live仍活着再叠一个新Live的路径。

evidence原程序使用自己的总Budget，并在构造live之前做：

1. 记录原live_started；
2. 检查原Budget；
3. 读取原remaining；
4. 将该真实remaining交给原Live。

新source保这段原正文和调用次序，只把最后构造改为R500。若原测量剩余截止为T，在时刻s记录live_started，随后时刻s'≥s取remaining≤T−s'，则传入的live截止满足

$$
s+\operatorname{remaining}\le T-(s'-s)\le T.
$$

这说明沿用这对原起点和剩余额度不会延长测量期限。namespace绝对时钟另由同一原Budget与R492 provider真实检查；这里没有把新记录的monotonic值配上旧完整budget重新开钟。

R500只代理同一个原query budget的读写计数，所有积分调用、panel/query计数及active秒数都仍记在原对象。资源异常原类穿透，close/必要收尾在预算停止后仍可执行。外层进程组/TERM→KILL/quiet硬生命周期仍由实际caller负责，本组件不冒独立硬杀钟。

## 504.5 包围改变不改变准确目标或原接受公式

六条路径的新E值盒，来自同一个全根族在同一个真实物理闭r区间上的合法包围。原算法对这些盒作向外区间运算。

因此：

- 任意原真实C成员的E(r)都在新使用的合法盒中；
- 原Gram仍来自同一个完整准确场；
- 四Loewner充分条件的含义不变；
- R459的广义谱norm公式、实际lower witness和全域upper责任不变；
- 未决cell仍未决，旧合法祖先界和未访frontier保留；
- 新盒没有实际收紧、未返或预算停止时，不发生“默认通过”。

新source完全没有改native/current-H/root/J/两mean/FD/fullDN/final/audit的任何接受门。它在实际field已经加载之后评估几何；没有反过来把几何证书作为原BVP的新增前置要求。

只改了合法包围，不证明误差已经下降。固定eta多次pass仍不能冒README的精化证据。evidence仍真正计算可比较的relative operator upper/lower；U_new<L_old只是严格下降的充分判据，重叠仍原undetermined，不成为下一精化拒收门。

## 504.6 evidence的固定g签名继续绑定旧准确定义

R500对外expected_binding/explicit_target/expected_result仍保原准确field绑定的对象。新C工作参数和新查询result另有真实身份，不取代它们。

所以evidence生成fixed_closed_target_signature时，仍包含原first material、同一个准确target、完整construction、十参数、原cuff及全t范围。它不把新precision、query-depth或新C result SHA塞进去而制造一个不同g，也不因为只来源名相同就声称不同材料图已相同。

R495原材料查询保持对正确注册的original current进行真实精确相位逆运输；base metric仍使用R495准确求值视图。二者在原R495证明范围是同一个准确函数，盒可以宽度不同。R504不自动收紧全部材料t-witness的场六jet，只把这些实际径向目标query接到R500。

全t结论仍来自原R443/R459的全角双射和同时拉回的同余，帽固定、两反射及全piece覆盖都须真付。不会由有限t网格或两个端点推出全t，也不强加跨级C²误差作为新完成门。

## 504.7 必要范围完整，比较不重复大对象

五个metric的same_actual_C_target直接保新tail.necessary，包含旧/新四件、原完整query状态/未访/错误、实际R489 source/clock和live当前地址。

evidence的result和necessary新增same_semantic_tail_queries，保存同样完整必要对象。原所有field/CP/coverage/global norm/t-grid/FD与末容差证据原样保留。

比较阶段真实读取每个完整measurement result，用原公式比较。它不把每一level的完整tail对象再次复制到series。series保存：

- 实际measurement result的完整身份；
- 是否有该tail对象；
- 该完整必要对象的canonical bytes/SHA；
- 明示完整query必要正文属于对应measurement，未在series重复传输。

这是真实来源引用，不声称摘要中的hash代替已经缺失的query正文。如果某个measurement必要输出超过90KB或未返回，series引用不会使那份缺失正文变成已读。原raw仍同job保留，原70/quiet/cleanup边界保持。

原Bridge.compact含“R495阶段未切tail”的scope字段，本次仍完整保留该原回执，并明确标成前一leaf-only阶段；新完整tail对象另列。不能把旧局部scope误读为本次全consumer没有接线，亦不能覆盖原回执后冒旧source输出。

## 504.8 完整文字计划和生成顺序

标准库生成器：

[root_20261116_same_C_recomputed_tail_metric_source_views.py](../computations/root_20261116_same_C_recomputed_tail_metric_source_views.py)。

完整计划：

[r504-same-C-recomputed-tail-metric-source-plan.json](../computations/r504-same-C-recomputed-tail-metric-source-plan.json)。

顺序为原所有真实依赖及需要的既有views → 原R495相应实际新名 → R504新名。计划逐view保存完整baseline file/bytes/SHA、每条完整before/after/count及完整output身份。

生成器先核全部选中baseline、helper、replacement次数和最终byte/SHA，全部在内存形成以后才独占xb写新basename；不覆盖任何原文件。若中途失败，保当前role、已经写出的实际输出身份和完整unconfirmed角色后缀。生成不导入这些科学程序、不运行AST/compile，也不替代其真正数学source closure。

六个角色可以显式选择生成；未选择角色单列，不能据一个role成功声称所有六个已经支付。实际生成的view仍须由未来caller按其真实文件名和SHA调用。

## 504.9 条件、未返和运行边界

本次没有接受父、没有实际查询值、没有测量上界、没有新run、没有新的W/H/eta/K/tau或精化因子。已有R489/R492对象不存在时，本API不能从SHA补造它们。

原90KB限制保持，未保证任意数量错误都必能装入。必要输出超限继续70；没有分块编码大raw、上传可再生payload或降低清理条件。

新来源范围仍是R495明确注册的四场族与R489实际actual202205时钟来源。未来更换launcher/field source的来源必须独立真实登记，不能因R504名字而冒泛化。新科学只Actions，当前214/216及218冻结/拟定入口不被本文修改。

## 504.10 已付和下一实际责任

源码上，六个完整外层现在都有明确的新名、schema/frame、真实tail调用、原source closure和必要选取；固定与live两种原工作范围均保。R500“尚未注册外层”这项责任由本独立计划明确支付，R500原文件本身仍原字节不改。

实际后继仍须同job产生真正accepted场、运行R489完整重算、生成并调用所选R504view，再按真实输出判断metric/evidence。217/R490尚未建立；本结论不预填其recipe、预算、父或结果，也不要求先跑一个额外fixture/审计才允许实际主链工作。

原条件证明、真实SOURCE_PINS及本次完整literal差异共同界定可调用范围；没有任何本地科学执行或额外接受门。
