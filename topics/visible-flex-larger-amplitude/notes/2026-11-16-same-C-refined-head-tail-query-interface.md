# R500：同语义完整 C 重算结果的 tail query API

日期：2026-11-16。作者：ChatGPT（AI，geometry 协作代理）。

本组件把 R489 真实重算的完整头部、查询和 source panels 交给原闭查询算法，保原准确场与原来源。条件证明见 [R500](../results/R500-same-C-recomputed-head-and-complete-tail-query-enclosures.md)。

本次是独立可调用组件；没有 request、workflow、运行、accepted450 或已测误差。R495已刊源不修改，当前214/216和后继218均不会因组件发表自动切换。

## 1. 唯一新科学 API 源

| 路径 | bytes | SHA-256 |
|---|---:|---|
| computations/geometry_20261116_same_C_refined_head_tail_queries.py | 29687 | 2ab6b97fc77c520ed8b888d31a766d9e4e744fb40dc8af46dfd4d287f015b580 |

schema：

~~~text
R500-same-semantic-C-refined-head-complete-tail-queries-v1
~~~

该 Python 文件没有独立 main/科学CLI、没有 subprocess、没有第二个 namespace 或时钟、没有删除动作。其唯一入口用于真正已执行原 loader 的 caller。所有源码导入和数值求值仍限指定公开Actions；本文没有本地导入、AST、compile或执行。

直接依赖为以下完整原件；它们的原传递闭包也必须保留，不能只下载本表就省原loader责任。

| 名称 | SHA-256 |
|---|---|
| geometry_20261116_same_C_refined_leaf_target_and_cut.py | a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7 |
| geometry_20261116_same_C_full_head_refinement.py | 0ce2f7ab8d1cfc95097ac8089c41ecc1f888343c8432255bd91b1d6cc5d3f8f8 |
| geometry_20261115_current_C_ten_live_query_complete_metric.py | 77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892 |
| geometry_20261115_same_job_C_live_query_provider.py | 07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9 |
| geometry_20261115_stored_continuous_E_cover_v3.py | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df |

R495四族已实际注册所用桥仍为 geometry_20261116_same_C_refined_metric_family_bridge.py /06656a5ed8bd020d7ab476ed9790f8fc9e4e75d3e7f61ef9c9cc1fb765ddfc74。本组件不复制它，也不扩它的family集合。

## 2. 输入对象必须已经真实存在

精确调用：

~~~python
tail = Tail.bind_loaded_same_C_tail_queries(
    current,
    args=actual_args,
    output=actual_output,
    metric_started=actual_original_metric_start,
    budget_check=actual_existing_budget.check,
)
~~~

current必须是已加载的 R492.RefinedCutBundle。R495四个明确family也返回这个真实类，所以可直接接。该对象必须保：

- 同一真实 provider/target 实例；
- 原 current.original 的完整 source_bundle；
- 原 definition 对象及其身份；
- 同一原 CP、十参数、节点、材料、B、cut chart/field 来源；
- R489真实result/input/new C/cut及原deadline；
- R492原完整三叶交和准确求值合同。

helper从 type(current).__module__ 取实际类owner，再核路径、SHA及确切类身份；不会从sys.modules里选第一个同basename模块，也不会把别的对象仅按schema文字重标成R492。

computations必须是helper自身实际HERE。全部原源和新helper在该真实目录，source-view生成如果将来使用，也须在真实HERE生成新名后再核最终身份。

output必须属于R489已绑定的同一namespace和RUNNER_TEMP；large-arrays真实目录须已存在、无symlink。live-C-queries和same-C-refined-tail-binding.json尚不能存在。它只负责这个caller新的query流，不接管别的已有oracle，也不覆盖旧文件。

## 3. args、资源和不变的原CLI字段

必需args：

| 字段 | 来源/含义 |
|---|---|
| computations | 实际原完整计算源目录，也是本helper HERE |
| continuous_e_result | **旧**准确场definition所绑的真实原 C result |
| continuous_e_result_sha256 | 上一字段真实SHA |
| budget_seconds | 原完整metric/measurement阶段allowance |
| c_query_precision_bits | 原R426 query算术精度 |
| c_query_integral_absolute_bits | 原子积分绝对工作目标 |
| c_query_integral_relative_bits | 原子积分相对工作目标 |
| c_query_analytic_guard_bits | 原解析分支工作guard |
| c_query_integral_evaluation_limit | 原积分evaluation工作预算 |
| c_query_value_width_bits | 原值宽工作目标 |
| c_query_integral_max_depth | 原积分最大细分深度 |
| c_query_inverse_max_depth | 原逆像最大细分深度 |
| c_query_max_panels | 原实际panel预算 |
| c_query_max_nodes | 原实际query node预算 |
| c_query_budget_seconds | 原累计active query秒数 |

这11个c_query字段直接由原R426.parameter_record读取和原范围检查，不创建新的取值、容差或科学门。value-width等仍是工作目标，不能改变原完整粗界合法性。

metric_started必须是caller在本阶段开始时记录的原monotonic值，不能在helper调用前重新取一个更晚时刻。budget_check若提供必须是caller的原实际budget。新LiveQueryTarget只有一个，它内部持有一个原ActiveBudget；wrapper只转发其读写计数并附上已有R492绝对job截止检查。

调用原外层CLI时，所有旧CLI参数保留；本组件没有额外seconds参数。原R489工作参数是先前重算的真实记录，不能用当前c_query参数倒填为其历史值。

## 4. 旧四件先绑定，新四件另有真实身份

输入continuous_e_result始终指旧field的实际原result，而不是让调用者偷偷把路径换成R489 result。helper先真实调用：

~~~python
Metric.ActualCompleteCTarget(
    C, current, args.continuous_e_result,
    args.continuous_e_result_sha256)
~~~

原source/factory/input/query/物理域/完整根族核对原样执行。然后helper从已经绑定的provider.directory读取refined-C/result.json，按实际receipt读取input-binding、query-plan、query-results，并再次比较R489.semantic_bindings。

新查询视图的名字是FixedRefinedQueries。它是独立对象，不是伪造的新factory结果。它保存：

- 旧实际factory C result；
- 新真实四成员及各bytes/SHA；
- 完整原非工作语义比较；
- 全query计划、实际返回序列和完整未访；
- 原natural radius、full head/root/join条件；
- 每条query原flags、原E盒、实际工作目标是否达到。

新query不需要whole-request全部成功才使用某条已经合法完整的粗界；每条可用范围仍须支付自己的原complete/domain/root条件。旧源/新源都不支付的域保持None。

## 5. 唯一live oracle真正从新source建模

helper只复制args容器用于指向真实refined-C/result.json；不改调用者args或任何模块全局。原R426.LiveQueryTarget以新FixedRefinedQueries为baseline，仍在原output下建立同名live-C-queries目录和四条原journal。

其prepare实读的是新result描述的：

- source_piece_index；
- source_radial_panels全流；
- 新真实累计radius_left/right；
- 原同C全部160浅层行和lambda；
- 原全部1440片闭参数分区；
- 同一个全根族deep_cover。

原R426逐行bytes/rows/SHA和分区连续性检查仍实际执行。不会因为query摘要存在就省这一步。新source raw缺失时，只能记录该live责任未付；不能用旧source-index或SHA伪补新累计半径。

原SixPrimitiveIntegrator仍只在live query里计算其真实新子积分。本组件本身不重跑1440完整头部；那部分由实际R489先前result负责。它也不从cut叶推导非平凡tail闭区间。

## 6. 可调用方法和返回范围

### bounds(a,b)

a、b是原物理r坐标的准确有理端点，满足原field的cuff≤a≤b≤cut。返回None表示完整闭覆盖未付；否则返回：

~~~python
(E_lower, E_upper, actual_complete_closed_query_sources)
~~~

E_lower/E_upper为Q，sources为明确原query/新query/live或混合闭覆盖索引。顺序与原metric消费者三元合同相同。

旧完整界与新完整界同覆盖I时作交；仅一方完整则保它；两方各不完整但真实完整子区间并覆盖I时，用全部相关合法盒的hull。没有删闭端点、没有点值外推、没有把未访片当作空集。

### refine(a,b,cell)

实际调用唯一原R426.refine，查询当前闭r盒。cell是原真实metric cell地址，原样进原query ledger。新增返回字段只指明实际R489 source和原coarse仍可用。

budget停止和源码/包围错误分别按原异常路径保。完整query在状态提交之后才可用于bounds；未返回调用不补数。

### close()

调用原R426.close，返回其真实requests/six_primitives/inverse_cover/unpaid四流descriptor或原真实close错误。不另建clock，也不因为原deadline已过而阻止收尾。

### describe() / necessary()

返回本R500 schema的完整来源与范围对象。原old/new完整query状态和未访不能丢；原live_status完整嵌套。当前没有固定输出frame；是后继实际caller自己的summary/必要reader职责。

### live_status()

明确原R426实际状态、它所用R489 baseline、源读到的当前行/后缀、query缓存计数/当前未返query、实际budget/错误和journal receipts。里面原R426的“本adapter没有重做全1440”说的是live层；R500外层另记R489已经重算的真实来源，二者不能混淆。

### 与原root plan兼容的数据

domain保持原物理区间。cuts是构造时旧/新已返回完整query分区端点的固定并集；后续live查询不更改root universe。conditions_proved来自任一实际同语义完整C条件证明，但每一条使用的query仍要通过自身条件。旧factory expected_binding/expected_result/explicit_target继续保原identity，不重标为新。

## 7. 值阶、field阶和目标不替换

当前API只消费原query正式返回的0阶E值。这已足够原tail/collar四Loewner和R459广义谱量中的g_rr。原角系数仍r²Phi_q²；准确patch的坐标拉回、Gram和完整六jet仍原R416/R492代码。

没有新的whole-tail E_r/E_rr hull方法。R492原cut E/E_r/E_rr及准确cut六jet独立保持，原source fragments本身的导数盒也不被本接口擅自总结为新全域导数结论。

准确target绝不是1+Bprime²。R500不写B，不换材料图，不调十参数，不改原natural-radius定义、原C root选择、midpoint或原finite profile。相同准确函数的新有效包围不意味着选出了新的准确C realization。

## 8. 实际caller要改的最少位置与尚未完成处

已经加载R495 refined current以后，将原两行：

~~~python
fixed_tail = ActualCompleteCTarget(...)
tail = Live.LiveQueryTarget(...)
~~~

换为一次已核新source的bind_loaded_same_C_tail_queries调用。**不要保原Live再并行造R500**，否则会重复oracle/工作预算并冲突输出目录。

原R426完整metric的inspect_cell_once/inspect_cell仍使用tail.bounds/refine；完整root plan、闭DFS、原四Loewner、两反射、caps和全部pending地址不需改变。

若未来接R459/evidence，还须真实注册这个新query对象及其necessary字段、原source closure、实际frame/schema。本文没有声称该入口已经登记。具体source-view计划必须给完整旧/新文字身份，不在runtime猴补旧全局后冒旧source。

后继必要selector至少保：

- old/new各四件身份；
- 原完整query状态/未访/错误与新source ledger地址；
- R489实际deadline/source；
- 原live当前query/source读前缀和未访；
- 全域covered是否真实；
- observed interval-width reduction的窄范围。

原90KB/70/quiet/cleanup条件保持。大量未决仍可诚实超限，不压成只有SHA后宣称必要已读。

## 9. 来源与未付

R489原origin仍是explicit actual202205和原deadline205；该来源即使被212/214等外层字节组合沿用，也须遵守其实际input/run/namespace绑定。R500不自动注册未来改过launcher的来源。

本组件可用于R492本体及R495已经正确登记的四族，均须真正有相应current对象；缺raw或没有accepted450时不能从摘要创建对象。它不重求BVP，不改任何native/J/FD/fullDN/final/accepted门。

工作变更可能使新包围更紧，也可能相同或更宽；组件合法取交不保证严格改进，不承诺某预算内终止，更不把query-width计数称作README要求的真实全域误差下降。

独立源/证明完成后可登记；实际外层来源注册和运行仍是明确下一责任。没有新的fixture、独审、短跑或科学前门。
