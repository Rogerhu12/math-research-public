# R500 — 同一准确 C 的重算完整头部进入 tail 闭查询

- 日期：2026-11-16。
- 作者：ChatGPT（AI，geometry 协作代理）。
- 可信度：**已证明（限以下完整来源与闭包围的条件命题）；独立 API 已写，未执行科学或新实验。**
- 本文不改变任何已冻结请求，不预填 accepted450，不把新查询作为原 BVP 前门。

## 500.1 已经存在的范围与实际断口

R489 用同一组原输入、原浅层160行、原 lambda、相同 cut/cuff、相同深端全部准确根族，实际重新调用原 f12f 的完整1440片与六 primitive 积分器。允许改变的仅是原已明示的工作精度和资源参数。其新 result、input-binding、query-plan、query-results 以及真实 source panels 都是新对象，旧对象保持不动。

R492 对原 E0、E1、E2 三个语义 cut 叶取两次合法包围的交，构造同一准确十参数 DAG 和 R416 准确 cut patch 的独立求值视图。原 CP、definition、节点、B、材料图和参数字均保留。R495 已把该求值视图接到完整 metric 和相对误差算法，以及 R483 的完整 coast 表达。

实际剩余断口是：这些原外层仍构造 ActualCompleteCTarget，再构造 R426 LiveQueryTarget。前者要求 result/input/query 四件与原 definition.continuous_tail 的实际来源逐一相同；后者由这个旧 result 的 source-piece-index 和 source_radial_panels 建 QueryCover。它实际保留旧累计半径盒，并未自动读取 R489 新的完整头部。

因此，仅 R492 三叶变窄不表示 tail 的 E(r) 查询已使用新累计积分。本结论正面补这个接口，不把旧 source 字样改成“refined”就算完成。

## 500.2 本次独立组件和边界

新增：

[geometry_20261116_same_C_refined_head_tail_queries.py](../computations/geometry_20261116_same_C_refined_head_tail_queries.py)。

它接收真正已经加载的 R492 RefinedCutBundle，包含 R495 已明确注册的 original112、resolution112、completeM、incrementalM 四族。实际 bundle 的类 owner、源码、provider 和 target 实例须相同。旧场先经原完整 loader；本组件不会从 receipt 或 SHA 构造一个未来场。

本次实际 API：

~~~python
tail = bind_loaded_same_C_tail_queries(
    current,
    args=args,
    output=actual_metric_output,
    metric_started=original_metric_started,
    budget_check=original_budget_check,
)
~~~

该调用替换原“一次 LiveQueryTarget 构造”，不能先造原 oracle 再并开一个新 oracle。它保留 bounds、refine、close、describe、necessary、live_status，以及原 root plan 所用的 domain/cuts 等接口。旧源码和模块全局都不修改。

这只是一项完整可调用的来源桥；本组件不声称已修改 R495 的六个外层 source views、R459 的正式 measurement 入口、某个 workflow、某份实际结果或已接受场。具体后继必须用独立来源登记真实调用，不能假称已运行旧已刊入口却获得新来源。

## 500.3 同语义前提必须由完整原件给出

设准确 C 的许可根序列集合为 Omega。对 omega 属于 Omega，原准确函数记为 E_omega(r)。本结论的“同一 C”不是两个 result 使用相似 schema，也不是两个名义值接近。

组件先调用原 ActualCompleteCTarget，在原 current 上完整绑定旧四件、原物理区间、原 C 公式和 source 闭包。随后真实读取 R489 的 refined-C/result.json 及三个实际成员，并重新调用 R489.semantic_bindings：

1. 两个 input-binding 的完整 key 集相同；
2. 除 runtime 与明确工作参数外，全部原字段按原 canonical 字节逐一相同；
3. 所有未识别的新数学字段都不能被忽略；
4. 深端仍为 original-exact-root-family，不计算或选择某个根；
5. 原所有输入、原完整请求 query 列表及其 closed endpoints 保留；
6. 新 result 与 R489/R492 实际记录的 bytes/SHA一致，属于同一真实 job、commit 和原绝对钟。

新四件使用自身真实身份，不写回旧 definition.continuous_tail，不伪造一次新的 factory result，也不把实际工作盒变成准确系数。它们给出的只是对所有同一个 Omega 中函数的另一组合法求值包围。

原 cut 半径和 cuff 半径、原完整 field domain D=[r_cuff,r_cut] 不变。新自然外半径包围可以改变，但不能拿其上端点擅自扩大共同合法域；每个新完整 query 仍须支付原 domain_containment_proved。

## 500.4 固定闭查询的交与覆盖

对任意闭区间 I 包含于 D，设两次真实求值分别给闭实区间 B0(I)、B1(I)，且已经证明：

$$
\forall\omega\in\Omega,\quad
\forall r\in I,\quad
E_\omega(r)\in B_0(I),\qquad E_\omega(r)\in B_1(I).
$$

则逐点有

$$
E_\omega(r)\in B_0(I)\cap B_1(I).
$$

这不要求两次区间细分相同，不要求两次浮点中心相同，也不要求所有独立盒的每个笛卡尔积点都对应一个共同 C realization。所用量词是：每一真实允许函数的每个值均在两次包围中。交运算不会挑选某个 C 成员。

若两包围都是给定条件下的合法包围，交必非空；实际数据出现空交时，本组件抛明确来源/包围错误并保原记录，不能据空交给出新值、声称 C 不存在或继续使用一个“修复后”的中点。

如果只有一组查询完整覆盖 I，则它单独仍是合法值界。新工作精度不足、未访、参数预算停止或 source panels 尚未读全，不撤销已有完整粗界。

### 多个闭子区间

假设有限组实际完整查询 I_j 的并覆盖 I，且每个查询均有 B_j 包含同一全根族在 I_j 上的全部值。则

$$
E_\omega(I)\subseteq
\operatorname{hull}\{B_j:I_j\cap I\ne\varnothing\}.
$$

组件按闭区间顺序检查没有缺口；相邻共享端点被保留，单点查询也不能被外推。只有实际闭并集覆盖所问的整个 I，才返回 hull。所选盒可因跨越 I 端点而更宽，这只使外包更保守，不削弱覆盖。

当旧 query 和新 query 单独都未覆盖 I、但它们的实际完整子区间联合覆盖时，也可用上述命题。新 source 保存各区间的实际 query 索引与来源，不能把这种混合覆盖写成某一条原 query 的结果。

### 不是自动严格收紧

如果 B0、B1 均完整，交后的宽度不超过任一原宽度。但可能等宽；若只有新界或混合覆盖，也不推出比某个未付旧界更窄。source 只对实际返回的一次 I 记录是否观察到严格 width reduction。

这个计数不是全域 metric 误差下降，不是 accepted450，也不是精化完成。R459 原上下界比较与真实 solver 容差分责仍保留，不以“已用了新 C”替代实际误差证据。

## 500.5 新固定 query 的原条件不减

新 FixedRefinedQueries 独立读取和保留全部 requested/returned query、完整实际未访后缀、source 未访范围、原 error、账本 descriptor 和原 work flags。

只有原各项真实条件均成立，某个结果才成为可用闭值界：

- 原 f12f 同一模型、全部许可根族、浅层 source 和 proof；
- 全1440片/160有限 cell、原 finite joins/protected join 和原深根存在条件；
- 当前 query 的 complete_closed_domain_bound、domain_containment_proved、continuous_model_family_conditions_proved；
- 真实自然外半径的共同域条件及原两个闭端点。

work_resolution_complete 不在上述数学条件中。原准许保留的完整 coarse 包围仍可用；query-depth、value-width、预算计数不被偷偷提升成新接受门。

对 whole-natural-domain，只在其实际共同自然域下界以内消费包围；对 closed-rational-radius-interval，只在真实请求的闭区间及不超过该下界的范围内使用。原分析恒等式 E=1+w² 给 E≥1，可继续作这个已存在的解析相交；不会用几何 B 的导数替换 C 的 E。

即使新 producer 的整个请求列表没有全部成功，已经真实返回且完整的某个闭 query 仍保有自己的证明。未返的 query 和源片责任单列，不能通过某个总 completed 字样抹掉。

## 500.6 真实使用新累计半径的 live 路径

新组件只创建一个原 R426 LiveQueryTarget。它的 baseline 是上述明确的新 query 对象；continuous_e_result 路径明确指向 R489 的 refined-C/result.json。

因此，原 LiveQueryTarget.prepare 实际执行：

1. 读取新的完整 input-binding，仍用原160行和原 lambda 建原 ContinuousHead；
2. 读取新 source-piece-index，并逐片核 n159..0/j0..8、全部原piece参数及闭[0,1]定义；
3. 顺序读新 source_radial_panels 的全部原行、bytes/SHA，核1440片的完整闭参数分区；
4. 核相邻真实累计半径端点逐记录接齐；
5. 用这些新的 radius_left/right 和实际 E/E_r/E_rr fragment 盒建立原 QueryCover；
6. 原 deep_cover 再给同一全部准确根族的解析外包；
7. 原 SixPrimitiveIntegrator 仅用于该次新子查询的真实中点子积分。

这里新累计半径的来源是先前 R489 已真实重做的完整六积分头部，不是本组件给旧盒删宽，也不是从新 cut 三盒反推整条半径函数。prepare 仍按原函数完整读实际source；旧 deleted payload 不能由 SHA 恢复。

本组件不再次重算全1440头部，也不要求复制或上传这些 raw。若新 source 账不可读、身份不符或预算在中途耗尽，新 query 未付；旧完整合法界保留，原 current source 地址和未访后缀仍记录。

## 500.7 所有值与导数阶责任

这一点必须单列，避免把 query schema 的含义扩大。

原 f12f QueryCover.run 的正式成功 query 返回的是 E 值盒、原闭域条件及原叶账地址。它没有在该 query 摘要中返回 E_r/E_rr 的完整全区间 hull。source fragment 和 inverse leaf 本身含原相应导数范围，但不能不读不组合就把摘要升级成三阶量。

因此本 API 的 bounds 仍只返回：

~~~text
(E_lower, E_upper, actual_complete_closed_query_sources)
~~~

这个0阶 E 值界正是原 R418/R426 四 Loewner及 R459 广义谱相对误差中径向目标系数所需的量。角系数仍来自同一原 r² Phi_q²；patch 的坐标变换和完整 field Gram 仍由原 accurate-cut/六jet代码给出。

R492 已完成的责任继续单独成立：

- cut 点 E/E_r/E_rr 语义叶来自旧/新完整 cut reader 交；
- 同一 accurate target DAG 的全部 prefix 值/导数；
- R416 真实准确 cut chart 的系数及完整 active 六jet。

R500 不给出新的全tail E_r/E_rr 查询 API，不声称只由0阶值盒已经验证 target 的 C² regularity，不声称 query 误差有高阶导数估计。原 C 的准确光滑性和 R413/R416 atlas条件依赖原已证明的公式与 gluing；它们没有因一种新的数值包围而被删除或重新命名。

全t相位、两反射片和两帽的原论证也不重做。若原外层在全闭域支付了相同目标的 metric 上界，既有 R443/R459 的共同材料同余转移范围不变。它不是“固定 g 自己旋转对称”的替代断言。

## 500.8 一个原预算和一个原钟

API 需要原 metric_started、原 budget_seconds及原11个 c_query 参数；它不提供新的 seconds 默认值，不新建一个额外可用阶段。

构造唯一原 R426 budget 后，ExistingBudgetWithNamespace 只代理这个同一对象：

- panel/query/integral_calls 等计数仍写回原对象；
- 原 active seconds、原 metric 起始的绝对终点和原 max-panels/max-nodes 均保；
- 再检查 R492 已绑定的同一个实际 job 截止时间；
- 不改变异常类型，不把资源 RuntimeError 包装成数学 ArithmeticError；
- 不设新 signal handler、线程、进程或异步计时器。

这仍是原 cooperative 检查；外层 OwnedChild/TERM→KILL/quiet 的硬生命周期责任保持原caller所有，不把这里的 check 宣称为新硬杀钟。

收尾 close/必要状态在资源停止后仍可调用，不能因截止时间已到而丢掉原错误、最后query、当前source row或完整未付范围。所有新query ledger仍由原 R426管理；本组件只新增小的来源binding文件，不删除旧payload。

## 500.9 完整必要范围与当前未注册处

describe/necessary 保留：

- 旧 actual factory query 四件和完整原状态；
- 新 actual R489 query 四件及每个实际query的原完成/工作/错误状态；
- 两个完整未访 query/source 后缀；
- 原 R492 provider和实际同一absolute deadline；
- 新 live-query原全部状态、current query/source地址及 ledger身份；
- 实际闭覆盖、合法交使用数和已观察到的单区间 width reduction；
- 原 CP/definition/十词/节点/材料/field未改以及本 API 仅0阶E的范围。

这些都是必要来源对象或地址，不输出科学大账正文。它没有承诺无论多少未决都必能塞入90KB；实际outer仍按原90KB/70/unknownscope和quiet/cleanup规则处理。

本次没有新request、workflow或接受父。R495外层源若将来接入，必须用新source/schema真实登记此API，并在自己的必要selector中保这些新来源与完整未付；不能只替输出标签。现有当前214/216和拟218不会因本文自动改变数学路径或来源。

## 500.10 原件定位

| 实际源 | 本文使用的函数/类 | SHA-256 |
|---|---|---|
| geometry_20261116_same_C_full_head_refinement.py | checked_C、semantic_bindings、Recompute.compute | 0ce2f7ab8d1cfc95097ac8089c41ecc1f888343c8432255bd91b1d6cc5d3f8f8 |
| geometry_20261116_same_C_refined_leaf_target_and_cut.py | RefinedLeafProvider、RefinedCutBundle | a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7 |
| geometry_20261115_current_C_ten_live_query_complete_metric.py | ActualCompleteCTarget、bounds、原query metadata合同 | 77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892 |
| geometry_20261115_same_job_C_live_query_provider.py | LiveQueryTarget、prepare、refine、ActiveBudget | 07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9 |
| geometry_20261115_stored_continuous_E_cover_v3.py | ContinuousHead、SixPrimitiveIntegrator、QueryCover.run | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df |
| geometry_20261116_same_C_refined_metric_family_bridge.py | R495实际四族注册与原tail未切换范围 | 06656a5ed8bd020d7ab476ed9790f8fc9e4e75d3e7f61ef9c9cc1fb765ddfc74 |

本文只使用原源码的完整条件与闭区间覆盖推理。所有新算术调用仍只能在公开Actions，未本地import/AST/compile/执行、未fixture、未新门、未推断实际精化或接受结果。
