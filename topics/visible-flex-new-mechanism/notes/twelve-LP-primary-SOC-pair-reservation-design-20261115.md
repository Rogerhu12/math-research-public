# 在原十二次 LP 内预留 SOC 机会：准确 incumbent、局部额度与新 checkpoint 接口

责任：tail_cost。本文与三份源码仅完成原式推导、源码静态接线及未挂 UTF-8 保存；尚未执行新开发或新科学。唯一执行入口由根代理在公开 Actions 发布。已有人工、已有优化阶段和历史 m10 均不重跑。

## 1. 本次改变解决什么

已完成 run **43753280651**、job **132931742484**、source **52a48854e30ddc3d2351ec24274dbe222ef05d9a** 的七个模型用了
\[
1+2+1+1+3+3+1=12
\]
次 primary LP，SOC 为零。第七模型的完整步确实未过细网曲率门，但当时全部十二次已经用完；半步随后由原真实门接受。这是一个真实的调用机会缺口，不是新半径保持策略已经触发或已经改善收敛的证据。

新策略仅改变 primary 的有限内部 LP 分配，让每个允许开始的 primary 留有一次原 SOC LP 的机会。它不强制 SOC，不改变任何真实门、物理模型、原标量 SOC 右端、修正半径、回退或学习记录，也不增加原十二次总额。较少的内部切平面 refinement 可能降低 primary 提案质量；最后一次 LP 还可能主动不用。必须与可能收益一起报告这些代价。

本轮从上述完成阶段的 **future_direct_checkpoint** 继续，不重演第七模型，也不重放历史 m10 来观察旧规则。

## 2. 唯一科学起点与原身份

| 项目 | 已完成真实 checkpoint |
|---|---|
| 两网最大 \(\eta\) | 0.26632415509189855 |
| 细网最大绝对主曲率 | 57.999989993517644 |
| 物理状态 SHA256 | 1275ae1da1bdf0779ff143e90b7177613b8011aa56a1781e3c31363ba1996be7 |
| 终端 body \(B\) / success streak | 0.000125 / 0 |
| coarse / fine 池 ID 数 | 4419 / 4277 |
| coarse / fine 版本 | 2 / 5 |
| 原容量 | 12000 / 6684 |
| 准确有序 bank 数 | 22 |
| bank SHA256 | c952c53a45396f3cdfef89853eb856ffa26f45089703a884e63c1a57956d97f9 |
| 坐标与原 height-reference SHA256 | b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580 |
| source configuration SHA256 | b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6 |

原 future checkpoint 字段完整保留：

- reference_complete163_binary64_exact；
- selected_final159_binary64_exact、selected_final163_physical_exact；
- selected_physical_state_sha256 与 coordinate_definition；
- coarse_pool、fine_pool 的完整有序 ID、容量、版本及历史；
- norm_direction_bank_context、norm_direction_bank_entries 及准确 SHA；
- terminal_trust、terminal_success_streak。

实际转移使用原完整 reference163，不改变 tangent reference tag。二十二条 normal 逐个按原 binary64 值与顺序恢复，不重新归一、不重建事件，也不搬旧数值 cut A/b。第一套新 complete model 仍必须通过原 context、两网坐标 tag 和 bank SHA 的准确绑定门。

普通初值验证及原初始化学习可能按原算法增加新行；那是本轮真实新事件，应照实记录，不能改写原输入池身份。所有科学数据仅 runner 临时保存。源码不内嵌二十二条可重算 payload。

### 原公开输出身份

只消费已完成日志：

- 原日志 3,366,573 B，SHA256 5215dbbd84e122f445ad188168b8a72f7316e0cd31e4b5bfdcfb1f42f1b25b3a；
- COMPLETE JSON 加 LF：895,932 B，SHA256 834cd800038c9d93f5619f17b2c901ee2085633e4393591cd41ebf3e915aef9c；
- 新旧开发复用与 source 绑定由根的新 transfer/audit 明确管理，不因本设计重跑任何旧套件。

## 3. 先核原真实调用顺序

原 source 的主链是：

1. accepted \(x\) 的同一普通两网值、当前池和 J；
2. 原 selected_model；
3. selected affine factory 与 complete original-grid factory；最终 model binding 在两次 factory 之后；
4. solve_remembered_primary：最多三次 LP、每次先给共享 ledger 加一，再实际求解；
5. 每个候选先计算完整 affine-\(e,f\) 的真实模型最大值，向上修复 \(\rho\)，按原单位重核 LP；
6. 最佳 repaired incumbent 保留。最后还对已追加的全部有效切平面重核；
7. 真实普通步、原扩池与学习、完整两网 gate；
8. 条件成立时才调用 same-layout SOC 或 same failed \(y\) 的 expanded-pool rebound SOC；
9. 原半径控制器、旧十七条件、新 covered-expanded-layout 保持规则以及所有 fallback。

直接核过的原限额引用：

- solve_remembered_primary 的两处限额判断均读传入 cfg["max_linear_models"]；
- 每个 LP 的 local cfg 只继承该副本并以剩余原 active 时间压低原 time limit；
- frozen solve_primary 不再另查或改变共享上限，使用原 LP arrays、HiGHS options、原 residual/floor 条件；
- outer 与原 charged SOC wrapper 各自仍读未改的原 cfg，其总额仍为 12；
- ledger 保存已启动调用数，没有一个需要临时更换的共享 limit 字段。

所以本次不用 monkeypatch solver、全局配置或 ledger。新的 primary wrapper 仅构造一个独立 cfg 副本，finally 明确记录 scope 关闭、实际收费及原配置 hash 不变。不存在异常时遗漏“恢复共享上限”的路径，因为原上限从未被赋写。

## 4. 确定的额度规则

记
\[
r=12-n_{\rm started},
\]
其中 \(n_{\rm started}\) 是原 ledger 中所有已经启动的 primary 与 SOC LP，不是成功返回数、accepted 数或虚拟预留数。

| primary 开始前真实剩余 \(r\) | 本次最多 primary LP | 花满后最少剩余 |
|---:|---:|---:|
| \(r\ge5\) | 3 | \(r-3\ge2\) |
| 4 | 2 | 2 |
| 3 | 1 | 2 |
| 2 | 1 | 1 |
| 1 | 不开始新 primary | 1 未用 |
| 0 | 原总额结束 | 0 |

写为
\[
c(r)=
\begin{cases}
3&r\ge5,\\
2&r=4,\\
1&r=2,3,\\
0&r=0,1.
\end{cases}
\]

在原计数 \(n\) 下，本次传给 frozen inner driver 的**局部绝对上限**是 \(n+c(r)\)，而不是把其已用数清零或给它额外 \(c(r)\) 次。实际 outer 和 SOC 一直保留 12。

### 4.1 机会保证

当 \(r\ge2\) 时，\(c(r)\le r-1\)。若本次 primary 用到允许的最大调用数，仍有至少一次原 SOC 的 LP 机会。若它提前结束，剩余只会更多。

当 \(r\ge3\) 时，\(c(r)\le r-2\)。因此 primary 若被真实门接受而未调用 SOC，至少还剩两次，足以允许下一 primary 与一次可能的 SOC。

当 \(r=2\) 时，允许一次 primary。若之后需要并符合原条件，可用最后一次 SOC。若 primary 已直接接受，剩下一次不能启动另一个没有配套 SOC 机会的 primary：明确退出并报告 unused=1。这里没有“必须把十二次用满”的承诺。

这个规则只保证 LP 可用槽。原时间、普通值、行容量、regularity、正 gain、同 \(x/y\) 绑定、residual 以及原实际 acceptance 条件依然可能阻止或拒绝 SOC。

### 4.2 为什么不只预留最后一次

仅把每轮 primary 限到剩余减一，会出现：本轮 primary 成功、留下一次，下一轮 primary 又消耗这一次，仍在真实失败时没有 SOC。新规则同时规定 \(r=1\) 不开始新 primary，并在 \(r\ge3\) 时留下两个，解决该调用顺序问题。

这不是对历史七模型进行反事实重放。新普通步会改变后续模型、cuts、bank、学习与曲率；没有任何结论声称历史第七模型将在新阶段以相同状态再次出现。

## 5. 修复 \(\rho\) 与 incumbent 的完整合同

本次继续调用已经冻结的 solve_remembered_primary，不复制或近似其数学。

设其冻结 complete model 最大值为 \(\rho_{\rm full}(p)\)，LP 返回辅助量为 \(\rho_{\rm LP}\)。原函数使用
\[
\rho_{\rm aux}=\max\{\rho_{\rm full}(p),\rho_{\rm LP}\}
\]
替换候选辅助量，保留真实 step 与 norm auxiliary，再对全部原 LP rows/bounds 计算原单位 residual。

每一后来有效支持平面都不超过同一 complete model 的凸函数值。因而已经按完整 \(\rho_{\rm full}\) 修复的早期 incumbent 仍可能满足后来的 cuts；源码仍执行最后一次全 residual 核，不能仅借这句话跳过。

新局部额度结束时，只能返回该原函数已经保存并重核的 incumbent：

- 返回的 predicted slack 是完整 affine 模型值，不是最后一个 cut LP 的松弛最优值；
- epigraph gap 不达标则保 returned_inexact_cut_model=true；
- strict objective tie 保留较早 incumbent，最后一次候选的 gap=true 不能重标较早返回值；
- 无合格 incumbent 则保原 None/fallback；
- solver、wall 或 residual 抛错仍抛给显式 outer，保最后真实 accepted，不伪造 incumbent；
- 每次 solver 启动前已计数，抛异常不会免费。

新停止标签另记 new-pair-allocation-primary-ceiling-reached，并原样保存 inherited_primary_solver_stop_status。即使 frozen inner 原文把它叫 original-shared-LP-budget，也不据此报告实际十二次总额耗尽。

## 6. SOC 与控制器

### 6.1 same-layout 分支

旧 outer 的 same-layout SOC 在 solver 返回后才增加计数。为了使本策略的“已启动数”在抛错时仍准确，新 outer 对该分支使用已经通过的 solve_rebound_correction 通用 charged wrapper。

该函数输入是原 primary、同一个 \(y\) 的原 full views、原真实 step、原 cfg、共享 ledger；它不要求一个 rebound context。因此 same-layout 也可直接使用：

- 原 build_correction；
- 原 actual \(y\) residual 与 accepted \(x\) 的 J；
- 原 scalar predicted slack 与 SOC RHS；
- 原 reversible scaling、HiGHS tolerances；
- 原 original-unit primal/dual/residual 核。

新 outer 在调用前先把 correction progress 放入 model，再交该 wrapper 启动前记账，删除旧 after-call 再加一的两行。不会双计数。若 build_correction 本身判无提案，没有启动 LP 就不收费。

这项改变仅把原 same-layout 数学接到已付的准确计费入口。其 schema 保留，并另记 actual_scope，不冒作 expanded context。

### 6.2 expanded-pool 分支与半径

same failed \(y\) 的 paid restore_failed_y_layout、capture/rebuild、两次 factory 的最终 binding、scalar RHS 与完整预测分账、一次 correction 与原全 gate 都原样继承。

直接调用原 next_expanded_layout_hold_trust，包括：

- 旧十七 guard 和 learning 事实；
- 原成功 SOC 的保持条件；
- covered expanded-pool soft-ID / same-\(x\) / complete actual-total-step 条件；
- 原 shrink、grow、minimum、streak 以及所有 fallback。

预留 LP 不使任何 hold guard 自动为真，也不把一次 SOC 接受等同保 \(B\)。报告分别记录 LP 机会、实际 solver、actual acceptance、是否 qualified 和下一模型是否真正使用保留半径。

## 7. 配置与成本范围

生产 source cfg 完整保持原 hash。新 policy 通过显式 constructor kw 和 evaluation_definition 声明，不加入 cfg，避免改变 SelectedRadialJacobian / memory_context 的准确绑定。

不增加：

- 原全阶段 LP 总额 12；
- 原每次 LP time limit；
- 原 active 120 秒；
- 原共享普通值额度 40；
- 原行池容量；
- 原变量、原 \(g,b_0,H\)、exact159/physical163；
- 原门容差、strip/curvature proposal floors 或 SOC RHS。

末尾原两网验收仍由既有 audit 按原边界独立记账，不把它混入或隐藏在“预留”次数中。

新策略可能更早要求一次原 full-fine 失败点评价，以判断原 SOC 分支是否适用；这种 ordinary/J/JVP/LP 耗时与值次数全部仍用原账。原 time/value/pool 限制可能先触发，因此不保证实际使用 reserved LP。

新阶段不是旧完成阶段的重复，也不是为了看到 hold 而延长预算。任何后继要由本轮真实输出提出新的、可归因问题，不能重跑同阶段直到策略出现。

## 8. 三份新增源码与准确接线

| 文件 | 未挂 UTF-8 blob | 字节 | SHA256 |
|---|---|---:|---|
| scripts/frame_metric_soc_pair_reservation.py | 99145e5bbe517d936574f9c84ac67156a5c2d49f | 11361 | 1b89f9a36a2ca9ec6cc3b85d907b6cf899300d9629c53eb3fe880fa10562c27b |
| scripts/frame_metric_soc_pair_reservation_recovery.py | 6e2172ad3842cbeb19912778a2ccb5a24296c6ba | 43551 | 25e64f68c506829b19a37f44a0581a06f16b4886cd0acfee433fcadbe460e6aa |
| scripts/frame_metric_soc_pair_reservation_development.py | 4d2edebb69b069a3cf0080f6e1b7b06e2dcfb476 | 17615 | 17b3021ece71250e95e272f6e2264a1a1d16b1436ea6425b4d44294c50a4080c |

### 8.1 Constructor

新类 SOCPairReservedObjective 继承原 ExpandedLayoutHoldObjective 的 factory、geometry、snapshot、rebound 等合同，但 constructor 不谎报原硬编码十一条数量，而从 RememberingCompleteObjective 初始化同一实际对象，再调用已付的准确 checkpoint bank helper。

根 audit 继续传原 runtime/Field/H/reference/subspace/bounds/gate/cfg 参数，新增或替换显式 kw：

    initial_bank_context=<future 原 context>
    initial_bank_entries=<future 原 22 ordered entries>
    expected_initial_bank_state_sha256="c952c53a45396f3cdfef89853eb856ffa26f45089703a884e63c1a57956d97f9"
    expected_initial_bank_entries=22
    soc_pair_reservation_policy="same159-twelve-LP-primary-SOC-pair-reservation-v1"
    initial_direction_records=()

不要再传 expanded_layout_hold_policy 或 expanded_pool_policy；类内固定两项原 policy，拒绝通过 kwargs 覆盖。不改 cfg。

### 8.2 Recovery

    run_soc_pair_reserved_recovery(
        objective, initial,
        known_metric_locations=(),
        restored_controller=<future 原 B/streak>,
        artificial_inputs_only=False,
        evaluate_only=False)

参数名和原 result/solver/checkpoint 布局保持。旧 controller 的数学和 callback 直接 import；paid cache helper 也直接 import。没有 monkeypatch 旧 outer 或冻结 module。

### 8.3 Metadata 与 source

新增：

- primary_SOC_pair_allocation_definition；
- 每次 primary_allocation_before_factory；
- linear_program.primary_SOC_pair_allocation；
- 每个真实 trial 的 SOC_LP_opportunity_allocation；
- solver.primary_allocation_decisions；
- solver.unpaired_primary_stop；
- solver.final_shared_LP_allocation。

最后一个字段逐项保存真实 started_primary、started_SOC、started_total、remaining_unspent，以及其中因“不启动单独 primary”规则未用的额度。不是把全部剩余额度统称 reserved。

原 attach_complete_model_reports 的复合旧标签 original_primary_inner_cap_and_shared_LP_budget_not_changed 先保留到 inherited_frozen_scope_labels，再改成 false，并新增两个准确事实：

1. 原每模型三次上界和全局十二次仍保；
2. 新动态 primary ceiling 可能更严格。

complete model 与 primary/rebound registry 的顺序及最终 binding 不变，不因资源元数据另建一个科学模型。

实现 hash helper 继承全部旧 hash，再列新增三源；根 transfer/audit/request/workflow 完成递归 source 绑定。这里不猜根尚未写完的新总 binding 数。

## 9. 仅新增开发检查

developer_check() 自带原 require_public_research_environment，返回 passed 与 all_passed；它没有在本地执行。

四个新组：

1. **额度表。** 检查全部十三个整数剩余额度及两个机会不等式，原 cfg 不变。
2. **真实 frozen repair 调用。** 使用原 artificial_arrays DATA、原 mapped ArrayLP、原 residual、原 _candidate 与 _cut_lp。solver 只用明确标记的数组 callback；一个凸二次 protocol 提供支持平面。核两次/一次额度、honest inexact 返回、较早同 objective incumbent 与最后 gap=true 不混淆。不是 HiGHS 通过，也不是实际曲面。
3. **收费与 scope。** 两次总余额中 primary 先用一次，再由原 charged_solver_call 在 callback 前用最后一次；核 no-unpaired-stop、primary 抛错和 None 原路径。无科学 optimizer。
4. **准确 22 输入。** 新 constructor 真调用已付 restore helper，再真走 inherited first-model bank gate。仅父数据初始化和 model fixture 为 stub；不重原十一条 negative suite。不执行旧 recovery loop。

fixture 中独立 step 只取原最小 physical weight 的八分之一，因此原 tail/body 盒确实允许；这只是 tiny array 接口，不是科学阶段缩 J 或缩半径。

旧十组、七组、cache 组、原二十六项 hold 开发及旧科学执行数均为零。根 audit 可以只读复用已付报告与准确源闭包，但本次四组首次真实执行仍须公开 Actions。

## 10. 首次实际必须读出的结果

完成、partial 或 error 都要保真实边界：

- 四个新开发组的完整结果，未执行者不能算 passed；
- checkpoint 的 exact159、physical163、reference、source cfg、两池和 22bank 准确匹配；
- 各 primary 的 start ordinal、局部 ceiling、实际 inner calls、停止原因、repaired \(\rho\)、gap 与 final residual；
- 每个失败普通步当时真实剩余额度、原分支 eligibility、是否实际启动 SOC；
- 每个 SOC 的开始前收费、原 scalar RHS、实际原单位 residual、same-\(x/y\) final binding；
- 原 learning、旧十七报告、新 hold 决策，以及下一模型真正使用的 \(B\)；
- 原 14 门、exact physical boxes、两网 \(\eta/\kappa\)、终端 pools/bank/B；
- 普通值、末验、J/JVP、primary/SOC LP、active/preparation/total 时间分别记录；
- 未用 LP 数量与停止代价。

如果没有 SOC 触发，只报告没有触发。若有触发仍不得仅凭接受次数或单轮耗时断言因果改善。全部结论以本轮新真实输出为准。
