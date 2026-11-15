# 直接 reference 求值：已闭冷路径、等价性与首次验证设计

日期：2026-11-15。范围：同一固定 g、固定 b0、固定共同原函数、原物理 163 / 独立 159 坐标的求值实现。

本稿冻结一个已经由原源码完整证明的数据流简化，并规定独立新模块的最小验证范围。它不重开已经耗尽 active 时间的原 m7，不给新 optimizer 分配预算，不运行旧开发或旧优化，不保存可重算数组。源码、必要参数、run 和人类结论由根维护者统一发布。

## 1. 已付冷恢复事实与准确边界

原 curvature-guard epoch 的七个模型中，m7 只有已付的第十次 LP；其物理提案向量未序列化。后继原 paid-attainer 方案拟从四个真实全网 attainer 构造合法支持，只新增 LP11 并保留 SOC12。该方案没有重放第十次 LP。

身份修正后的 run 43773136836 / job 132993290386 / source 403a2fcf430f0ed98b5731256befe36bb833eadf 的回执表明：

| 项目 | 已观察值 |
|---|---:|
| 新 coarse ordinary value | 1 |
| 该 value 记录的 geometry 时间增量 | 205.448292651 秒 |
| 新 fine ordinary value | 0 |
| 新 selected-J refresh / batch | 0 / 0 |
| 新 complete model / oracle / LP / 接受点 | 全部 0 |
| 累计 shared values | 15 |
| 累计 LP | 原 10 次 |
| snapshot active | 241.3142038439999 秒 |
| snapshot initialization | 293.5427817930001 秒 |
| 本次 prepare | 14.011384722 秒 |
| 本次 recovery | 205.785849204 秒 |
| 本次 process total | 224.820478542 秒 |

这些数值来自根对本次唯一原日志的消费。本稿没有重新下载或运行科学。

原 active 上限为 120 秒。普通求值先检查时间，执行一个不可抢占的大调用，返回并保存 coarse cache 后再次检查时间。因此本轮是超过上限后退出，不能称在 120 秒内完成。余下两个 LP 槽不构成继续同一 epoch 的时间授权。

本次正确区分了 objective 和普通 field 两个 SHA 域；该身份缺口已修。此次停止不是身份错误，也未检验 LP11 的效果。

本稿不把 205.4483 秒全部归因于下文可删除部分。旧源码只记录整个普通几何时间，未分别记录被丢弃的查询积分、必要 fixed prefix、partial panel、heat 基元和最终场的费用。

## 2. 原调用链及所有关键来源

以下路径均相对 topics/visible-flex-new-mechanism/scripts/。审读基准为上述 source 403a2fcf430f0ed98b5731256befe36bb833eadf。下方单列 SHA-256 的八份直接几何来源与 source 68f92b9cb16677278dfbc7f8e13bdf7189e41d9c 的原绑定逐文本相同；这句话不覆盖整个调用链表，尤其 frame_metric_paid_attainer_resume.py 使用 403a 的已修身份版本。

| 原文件 / 函数 | 本证明使用的内容 |
|---|---|
| frame_metric_paid_attainer_resume.py / PaidAttainerResumeObjective | 同 epoch 的 active 时间与 value 计数恢复，原 Field/坐标/池/学习身份 |
| frame_metric_paid_attainer_recovery.py / _run_paid_attainer_resume_outer | 首先 evaluate(x)，其后才 fine、J、两 factory、LP |
| frame_curvature_epigraph_exchange.py / _wall、physical_geometry | 调用前检查时间；jacobian=False 整几何；返回后计时、计数与 cache |
| frame_metric_budget_recovery.py / MetricRecoveryObjective.evaluate | 完整 coarse decision/rows 后再次 _wall |
| frame_five_height_field.py / FiveHeightField.geometry | 当前159到 reference163，再执行完整 null-height 增量及163到159 Jacobian映射 |
| frame_entry_single_q.py / SingleQProblem.geometry | 四角 reference 的消费点，完整当前角网格和所有最终 jets |
| frame_entry_bounded_height.py / BoundedEntryHeightProblem.geometry、height_jets | 原 metric/height，最终 fixed_primitive center 覆盖 |
| frame_independent_height.py / IndependentHeightProblem.geometry | 后来被覆盖的查询分割 center 积分 |
| frame_fixed_height_primitive.py / FixedHeightPrimitive | 同一固定分割前缀、局部 panel、原零锚及进程内缓存 |
| frame_entry_paired_repair.py / EntryWeightedHeightBasis、PolynomialPanelIntegral | 原九高度列及其同锚分段多项式原函数 |
| frame_collar_natural_body_audit.py / NaturalBodyProblem.grid_for、NaturalCapGrid | 新网格键上的不可变 heat 基元构造 |
| frame_selected_row_radial_jacobian.py / SelectedRadialJacobian | 必须是 FiveHeightField；既有普通 cache 上的径向因子化，不是冷普通求值替代 |

直接决定等价性的旧源码 SHA-256：

| 文件 | SHA-256 |
|---|---|
| frame_collar_bvp.py | 64dffdbfc6456fe022105d264442d307c8f88022cdf755ec0a41ea97fff93d00 |
| frame_entry_single_q.py | b0744e42b00854b85ac6828afc4520c0505b5d4800c47ab4d8bb96c84d04e286 |
| frame_entry_bounded_height.py | deac1dbb3410fc426bd1cbb84c126062a5ff61e2aa19c6fcdf1bbd9d0727b612 |
| frame_independent_height.py | d7c52dd824a9302d8877092c551cc567ed1477a0dc6192799d8ad42969121de6 |
| frame_fixed_height_primitive.py | 16d7200ed2fe3c4f433d5f3ae787696311499264cb21172d9915efea9ae7b780 |
| frame_entry_paired_repair.py | 8f09d96a4377175e0242a37f1450960f0914e28a787699565d437058e7625ac1 |
| frame_five_height_field.py | 549e61db392f318260d636d41a090bd56e8c96b2eab580075707b5e25a24f656 |
| frame_height_null_coordinates.py | 5ebfde0a3322bd119704fda517b2f15db48964fad7a3a344b1e863ec4c2f2f22 |

这里只保存源绑定，不保存计算数据。

## 3. 只读三字段引理

设原 SingleQProblem 为 S，其 base 为 BoundedEntryHeightProblem B。当前独立状态为 q，原 FiveHeightCoordinates 给出 reference163 状态 r(q)：保当前全部 u/v/Q 系数，九高度暂取原固定参考 c*。令 old=S.to_old(r(q))，即只删除新增 Q 槽，保原旧布局。

原 SingleQ.geometry 首先计算：

~~~python
reference = S.base.geometry(old, t, np.arange(4)*np.pi/2, quadrature_order)
~~~

随后，对这个 reference 字典的全部实际读取只有：

~~~python
metric = reference["metric"]
height = reference["height"]
center = reference["center"]
~~~

原函数没有读取 reference 的 X、T、primitive、frame、四角位置 jets 或其 Jacobian。其最终当前场另外用：

~~~python
grid = S.source.grid_for(t, theta)
fields = grid.fields(r(q))
fields["_theta"] = theta[None, :]
frame = target_frame(fields)
~~~

因此，只要上面三个 reference 字段相同，保留原最终组装代码就得到相同完整函数。这是对原函数实际读取集合的穷尽陈述，不是用部分测试推全函数。

### 3.1 metric

原 IndependentHeightProblem.geometry 调用 B.metric(old,t,jacobian=False)。SingleQ 创建 reference 时从未请求 parameter Jacobian，即使外层 SingleQ 自己随后请求 Jacobian 也如此。因此直接调用该原 metric 方法给出原 reference 的完整 metric 字典。

固定 g 的数学定义、完整 frozen coefficients、原 a/a_s/a_ss 等计算不变。

### 3.2 height

原 reference 的 height 正是 B.height_jets(old,t)，其定义为：

$$
b=b_0+C\,c_*,\qquad b_s=b_{0,s}+C'\,c_*,
\qquad b_{ss}=b_{0,ss}+C''\,c_*.
$$

这里仍用同一个 B.height_baseline、同一个 reference anchor、同一个角向均值规则和原 EntryWeightedHeightBasis。没有把当前精确九高度舍入成新的参考状态。

### 3.3 center

BoundedEntryHeightProblem.geometry 最终覆盖 center 为：

~~~python
center = (
    B.port.initial_center_z
    + B.fixed_primitive(t)
    + B.height_basis.integral(t) @ old[B.slices["height"]]
)
~~~

该式只依赖原 fixed primitive、原高度控制原函数及原 c*，与当前切向系数无关。直接使用这一式保留原物理零锚、固定 partition、完整 panel 的 Gauss order、各查询点局部 panel 规则和同一高度原函数。

原 IndependentHeightProblem.geometry 中根据查询数组进行的 radial_quadrature、height_baseline(nodes) 与累积 center，随后被上述式整体替换。它们没有进入最终 reference 三字段中的任何一项。

由此，可以不调用 B.geometry 或 IndependentHeightProblem.geometry，直接取得三字段。删除四角整场和被覆盖 center 的证明至此闭合；必要的原固定原函数仍须真实求值。

## 4. 原最终组装与全部坐标保留

令原周期算子给出 $P=\Pi T$、$P_s=\Pi T_s$、$P_{ss}=\Pi T_{ss}$。新模块照用原式：

$$
\begin{aligned}
X &= aP+z_c e_z,\\
X_s &= a_sP+aP_s+b e_z,\\
X_{ss} &= a_{ss}P+2a_sP_s+aP_{ss}+b_s e_z,\\
X_\theta &= aT,\\
X_{s\theta} &= a_sT+aT_s,\\
X_{\theta\theta} &= aT_\theta.
\end{aligned}
$$

保留同一完整 theta 网格、原零模/Nyquist 处理及其浮点周期算子。没有用 $D_\theta\Pi=1$ 改写离散公式。

随后完全沿用 FiveHeightField.geometry：

- Z、C、C_s、C_ss 均由原 exact-null basis 的同一个 values 方法产生；
- 仅在原真实内支撑行更新 center、X、Xs、Xss 及 height 字典；
- null 坐标全零和真实外域保原数组与原 signed-zero 写入方式；
- reference163 保固定 c*，最终物理九高度仍由原精确仿射 map 定义，不使用九个新 rounded doubles 代替；
- jacobian=True 时先沿原 complete_tangent_parameter_jets 组装全部163列，再保前154列并拼原5个 null-height 列；
- 基本 Jacobian 和 full_two_jet_jacobian 两个返回分支均保原列序与键集合。

因此简路不是 selected-values 或 reduced-grid 近似。最终 ordinary 数据和原门所需的全部位置 jets 仍完整。

数学上的全函数等价由第3–4节给出。新公共人工和实际值将记录 binary64 差异；在这些输出尚未读取前，不预报逐位相等或速度比。

## 5. 新模块和显式 adapter

新增源码为：

topics/visible-flex-new-mechanism/scripts/frame_direct_reference_geometry159.py

当前静态源码快照：23148 字节，SHA-256 ac6bb23c625429452d8216018b996cdbc9fc3fc8d9cfe5c04cc6a46a7b99ab0b。未执行。

导出：

~~~python
POLICY = "same159-direct-immutable-reference-geometry-v1"
DirectReferenceFiveHeightField(existing_field)
adapter.geometry(state, radial, theta, quadrature_order=4,
                 jacobian=False, full_two_jet_jacobian=False)
adapter.implementation_definition()
adapter.timing_snapshot()
~~~

该类是真实 FiveHeightField 子类，保已有 SelectedRadialJacobian 的 isinstance 合同。构造时不再运行 FiveHeightField、SingleQ 或 Bounded 构造器；复制原 field 的属性引用，原 coordinates、null_basis、SingleQ、Bounded、source 和它们的所有缓存仍是同一个对象。

adapter 不 monkeypatch 原对象，不改任何原146源码，不提供 optimizer 或研究CLI。frozen_metric_copy 返回同一个 adapter 及状态副本，不重建 g/H/reference。原 evaluation_variant 的既有行为没有在本任务中扩展；若未来显式建立不同求值 variant，应对那个新 Field 另行安装 adapter。

### 5.1 新求值身份必须如实变化

原 SingleQ.evaluation_definition 的 common_center_evaluation 字段逐字写着：

~~~text
unchanged base geometry with fixed 4-angle grid, center only
~~~

新实现已经不再进行该调用，故不能原样复用这个实现描述或冒充旧 field SHA。adapter 的 evaluation_definition 保留全部原物理、参考、坐标和 quadrature 字段，仅将上述路线描述改为直接三字段，并增加独立 source_original_ordinary_evaluation_sha256 引用。

因此：

- 原 physical identity、固定 g/b0、reference map 与 canonical159→163 不变；
- 新 evaluation SHA 诚实反映新求值接口；
- 不把它接回已耗尽的原 epoch；
- 旧 norm-bank / learning 的数学迁移、任何新模型与 cache 的重绑定，属于后继另外证明的接口。本稿不豁免任何原 context hash。

## 6. 计时、冷/命中与对象生命周期

模块对必要原调用分项计时：

1. reference_metric；
2. reference_height_jets；
3. reference_fixed_height_primitive；
4. reference_height_control_primitive；
5. current_complete_scalar_grid；
6. current_fields_and_frame；
7. current_complete_periodic_primitives；
8. original_position_jet_assembly；
9. 原163 Jacobian组装（仅明确请求时）；
10. 原五 null-height 更新。

有原缓存的调用，记录该调用前后的真实缓存存在性：

- B._height_cache 的完整径向查询键；
- fixed_primitive.prefix 和所请求点的 partial_cache；
- weighted-height correction primitive 的原 prefix / per-point cache；
- SingleQSource 的完整径向与角向网格键。

这些标签只说明所指那一级缓存。SingleQ 网格 miss 不等于所有下层 heat 基元都是冷的；高度 baseline hit 也不表示控制多项式评估免去。没有缓存的原接口直接标 not-cached-by-this-interface。

所有已经开始的 component，包括抛异常的 component，都在 finally 累计实际经过时间；geometry 总时间另外记录，保 validation、元数据与未单列的组装开销。只保累积量及最后一调用的小型记录，不保新的数组轨迹。

本模块继承的 evaluation_variant 仍会建立原 FiveHeightField。若后继明确需要一个精化 variant，调用者须将该 variant 显式装入新的 DirectReferenceFiveHeightField 并重新绑定新求值身份；不能把原 variant 静默当作本适配器。当前两原网只是同一 field 的不同查询网格，不要求改变求值 variant。

本模块没有另加 reference 三字段数组 memo。它保留原对象的既有内存缓存，避免在不同 theta 网格和同进程后继计算间重建这些对象。也没有对 NaturalCapGrid 的径向批处理基元做新切片优化；该优化需要独立逐字段证明，不在本次源码中提前加入。

### 6.1 预算和持久化

调用方仍拥有全部时钟、ordinary value、J、LP 和验收计数。模块不设置、暂停、恢复或修改任何 ledger；分项 timer 也不触发额外几何比较。

根规则15没有 Actions cache 的数据保存豁免。新数组只在当前 runner 内临时持有，不写 Git、Release、artifact 或跨run缓存。报告只保存人类结论、源/参数/run及输出hash。

已经耗尽的原 epoch 无合法的 LP11 继续空间。后继任务预算由根另行给出；不得将冷费挪到免费 initialization，也不得再次继承耗尽前的 active 数。

## 7. 最小首次人工验证设计

所有项目只在公开 Actions 首次执行。本稿及新模块交付时均未执行 Python、compile、人工、真实几何或优化。

只借已有 frame_five_height_field.artificial_problem 的小输入工厂，不调用它或任何旧模块的 developer_check。该工厂给真实163/159布局与小8角/低阶固定积分；不以真实研究样本作开发输入。

建议三组新检查，限定于新实现的三个剩余风险：

### A. 三字段与返回分支

用同一个明确小径向数组，包含零锚、entry端口、内部点及高度支撑右外点；角网格只用8和16。以原 field 和新 adapter 在人工数据上对照以下三个必要分支：

- null0、普通值；
- 非零Q与非零null、基本 Jacobian；
- 非零Q与非零null、完整二阶 Jacobian。

检查三字段、全部 ordinary 返回 jets、原J列序和新159拼接；分别报告最大差及逐位是否相等，不把数值差裁零。原 physical/canonical identity 及坐标 map 必须严格同一。此处的小型原 geometry 是新简路的人工 comparator，不调用旧开发套件，不运行真实旧几何作比较。

### B. 删除路径与真实缓存

在独立小人工对象上临时将旧 Bounded.geometry / IndependentHeight.geometry 设为禁止调用的哨兵，确认新 adapter 仍用三字段完成；仅测试期间设置并恢复，不修改生产对象或旧源码。

以同一对象再求一个必要的非零null状态，核原 prefix / partial / scalar-grid 的真实 hit 记录和实际 null 更新。检查 frozen_metric_copy 保对象身份、没有新 metric/reference 构造。一次人工受控 component 异常只用于核已开始时间进入 failed 统计，避免失败开销在新报告丢失。

### C. 新求值身份与既有 selected-J 入口

用这个小人工 adapter 实例化原 SelectedRadialJacobian 并 bind_ordinary：

- 必须通过真实 FiveHeightField / SingleQ / 163→159合同；
- 新 ordinary evaluation SHA 与旧不同，原source SHA引用准确；
- 原 g/b0、coordinate、height-reference 数学身份仍同；
- 小普通 cache 的原坐标/状态/网格绑定确实传入。

这里不重跑原 factorized-J 套件、所有11组旧导数或旧 finite-difference检查。原J自身数学没有改变；本次只检查新field入口及返回数据的兼容性。

首次开发实现现为 scripts/frame_direct_reference_geometry159_development.py：20642B，SHA256 af63965826364efee0e96e12663a77d520d28f246b957ce1cb3e7b4e8fb9cc12。准确为3组×3项=9项；全部成功时人工原geometry对照3次、新adapter6次（5成功、1预定失败），两种Jacobian分支每方各1次，最大12径向×16角。人工输入工厂2次，factorizer构造/普通bind各1次，其evaluate为0；旧developer/研究几何/LP/JVP/optimizer均0。当前只发布源码，尚无passed结果。本设计不请求为已由第3–4节闭合的纸证增加机械复核门。

## 8. 首次真实求值的最小范围

根另行制定任务预算后，优先只验证该新求值接口：

- 从已经付费的当前best checkpoint恢复原参考、状态、固定g/b0、原两网、精确高度映射；不重放旧optimizer或开发；
- 同一runner只建一个 adapter，同一原对象取得 coarse 和 fine 的两份必要完整 ordinary 数据；
- 使用原 authoritative scalar forms / gate函数读取全部原门，并与对应已付同状态收据的 eta、curvature、位置/高度标量及物理身份比较；
- 记录两次必要调用每项的冷/命中时间、source构造/prepare及总体墙钟，不能只给 warm-trial 时间；
- 不再调用旧真实 geometry 作对照，不跑真实 full163 Jacobian，不调用原第十次LP、不调用已耗尽epoch的LP11；
- 原收据没有完整数组时，不能声称核过其逐数组hash。全函数来源仍由第3–4节和新人工对照说明。

如果后继需要 selected J 或优化，必须先明确其独立接口与预算，并预先在同一执行进程接好，使已经产生的普通 cache、参考基元和后续 J 可继续复用。不得在完成本求值任务后为了同一数组另开一个恢复run，再把重算费用隐去。

## 9. 已闭与未付结论

已闭的是三字段数据流等价性、两个无贡献计算的准确删除范围、完整最终jets/列序/null映射、真实缓存所有权和新metadata边界。

尚未实际知道新冷求值的时间、分项占比、binary64差异及后续优化增益。即使人工与普通求值成功，也不自动给出 norm-bank / learning 的新身份迁移、同m7继续权限或新的几何目标已达结论。
