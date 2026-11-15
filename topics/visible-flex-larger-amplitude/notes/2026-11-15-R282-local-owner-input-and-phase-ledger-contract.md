# R282 局部 owner 的真实输入与完整相位责任接线

2026-11-15，geometry，AI 辅助研究。**状态：证明与 source-only 接线合同；没有新实现运行、没有实际接受场。** 对应结果为 [R282](../results/R282-local-cross-Gram-cuff-charts-and-complete-phase-responsibility.md)。旧已冻活动解释器、两固定帽和 mixed 入口均保持不变。

## 1. 已查到的最小缺口

旧 R241/v3 的实际循环具有曲率短路径、距离、平帽和中心法向锥责任，保持原静态未标记基面加 R24 的路线。但旧导出是聚合计数与少量 worst/child 展示；它没有给新完整活动—固定 cell 布局的每个空间—相位 product 输出可以直接组合的 local receipt。

新已冻 mixed 入口准确指出 cuff 零弦责任，但没有伪造支付：

- known_cuff_local_responsibility 只判断同侧 collar 闭 cell 触 cuff、帽闭 box 的半径平方范围触该圆。
- 它将原 rank 记为 original_local_chart_responsibility，local_responsibility_paid 为 false。
- 这表示完整相位 product 中可能有正确粘合的同一材料点，不表示整 rank 都是局部近邻。

R282 现在给了可以支付这种近邻的准确充分条件。尚需的最薄后继是一个**独立 local owner 与逐叶组合器**，从同场完整 collar/B 系数计算真实余量，再对每 rank 作空间和相位共同细分。无需重做原求解、改变 $g$ 或创造新的接受门；本合同不把尚未编写的组合器称为已运行。

## 2. 直接复用的源边界

| 已冻源 | 已读的实际边界 | 使用范围 |
|---|---|---|
| geometry_20261115_shared_active_interval_balls.py | ExactFiniteField、tail_coefficients(-1)、material_angle、cell_specs | 同一准确有限场、完整 collar 系数及物理角 cell |
| geometry_20261115_fixed_cap_rational_balls.py | bind_geometry、disk_partition、cap_cells | 同一实际两帽、marker 支撑和 Cartesian 闭域 |
| geometry_20261115_complete_mixed_phase_component.py | bind_inputs、active_rows、rank 规则 | 全部场身份和完整活动—固定 universe |
| geometry_20261115_rational_phase_cover.py | catalog_for、strict_interval、原两图 phase_cover | 非局部叶的原四门，不能只重新测一个中心 |
| root_mixed_phase_normal_balls.py | sqrt_upper 与有理多项式原内核 | 有理平方根上界；非局部相位门原算术 |
| geometry_20261114_continuous_cover_budget_v3.py | 原短路径/法向锥/平帽/距离责任 | 旧路径保留；不把截短展示列表导入为全覆盖 |

前两个球 producer 必须来自同一个真实原 closed/shared loader。原 loader 要求的真实接受、完整 native response/J/audit、H、mean、SE2、配置、来源等都不变。没有这些真实输入时只保本 source-only 合同，不用失败场伪造它们。

原 evaluate_case 和 phase_cover 从两张完整 $[-1,1]$ 根域起步，没有接受任意子区间的现成 CLI 参数。后继组合器应复用 catalog_for 给出的同一四次多项式与 Sturm 链，再调用已有 strict_interval(poly, sequence, a, b, kernel) 核实际叶区间；不能把原整圆未决结果改标签为某个子区间通过。原 R280/R62 整圆分支若已经通过，仍可以直接支付该叶；包含原非严格全圆距离分支的 OR 不删。

## 3. 局部常数的输入

以下数值在实际 Actions 中从已绑定对象形成，当前没有预编数值或未来输出 SHA。

| 项 | 已有实际对象/字段 | 必须保的范围 |
|---|---|---|
| 场身份 | active input_binding.complete_field_binding、shared_background_geometry；同场 cap/cover binding | 与已有 binder 逐项同一，不重新配准或换 B |
| cuff/宽度 | field.cuff、field.inner、field.B.radii 的首两个值 | 精确 stored scalar 的有理解释，$R>0,h>0,h_B>0$ |
| collar 系数 | field.tail_coefficients(-1) | 全部 k、三坐标、实虚部分、六个幂系数；左端 0/1/2 恒为零 |
| 原 native 节点 | field.node(0)、field.node_records[0] | 原第一个 FFT 节点全部 0/1/2、全部均值与 Nyquist，原 readout/原文件 SHA |
| 共享背景 | field.B.coefficients[0]、field.B.nodal[0] | 同一个精确实多项式，$B(R)=H,B'=B''=0$ |
| 材料图 | field.core、field.density、field.rho_lower | 全部 core；$\Phi$ 及原完整密度下界，不能用 $\phi$ 直接作帽角 |
| 帽支撑 | cap input_binding.marker_definitions 及原 plan 的对应 marker | 按同一 side 取完整中心、半径；严格支撑半径上界 |
| 原全局责任 | old cover 的 marker_budget.target_reach、supplied_envelopes 等原字段 | 仅承接原 $\tau,K$ 与范围；不预设新预算 |

完整 collar 系数当前不是活动球输出中的另一个 raw payload；其全节点身份有保存，但 hash 不提供系数。最薄生产方式是复用同一进程内已经构造的 ExactFiniteField 对象。若另进程消费，须通过同一 loader 与真实完整节点输入重建相同准确有限表达式，并绑定实际系数的完整身份；不能从位置/法向球反求，也不能把单点 jets 当作全域导数。

原 scalar 有限 Gauss $a$ 与返回 ap 的导数兼容不在此获得假定。局部常数仅来自完整有限 Hermite collar 和实际共享 B，所有导数由多项式求出。原 $g$ 完整表只保原身份，不替换为 $B'$。

## 4. 材料坐标与实际 membership

活动流已经具有以下真实键：

- ordinal、cell_id、sheet、piece_index、piece_kind；
- closed_radial_interval；
- closed_normalized_physical_angle_interval，其中 $\phi=2\pi q$；
- phase_motion=active_R248_image_rotation。

固定帽流保 cap、cell_id、parameter_box_xy，以及该闭 box 与原闭 cuff disk 相交的准确域。帽侧的 Cartesian 参数就是材料平面坐标，不是活动点的变形后 XY。

后继局部门只在同侧 cuff 环带使用共同参数

$$u=r-R,\qquad v=R(\theta-\theta_c),\qquad
\theta_{\rm active}=\Phi(2\pi q)+\alpha,\quad
e_{\theta_{\rm cap}}=(x,y)/\sqrt{x^2+y^2}.$$

相位为 R281 的 t/u 两图，各自起始闭区间都是 $[-1,1]$。必须对当前 phase 子区间的所有值同时支付 membership。活动的方向是材料圆上的 $R_\alpha e_{\Phi(2\pi q)}$，不能误用实际变形位置的单位 XY 方向。局部图在 $r>0$、角提升宽小于 $2\pi$ 的原抽象粘合面上单射，不接触帽极点。

图内所有不同材料点由 R282 的积分不等式支付。恰为同一 cuff 材料点时两份表示送到同一 $(u,v)$；仅在这一原商关系下不要求正弦长，不能凭位置相同或接近判断商等价。

## 5. 常数与逐叶记录

一个后继实现至少保以下数学输入/输出：

| 类别 | 最小内容 |
|---|---|
| 局部表达式 | 原场/bundle、全 collar 系数身份、原 B descriptor、完整 core、原 marker 支撑身份 |
| 图参数 | 同侧 cuff、$R,\delta,\omega$，有理单位中心 $e$ 与严格扇区参数 $\eta$ |
| 系数界 | 全部 $\nu_{jk}$ 的形成规则及完整系数身份，$L_j,T_j,b_j,h,h_B$ |
| 实际余量 | $M_r,M_\theta,E_u,E_v,\varepsilon$ 的准确有理上界，$m=1-2\varepsilon-\varepsilon^2>0$ |
| 图域归属 | 两侧全域半径下界/上界，材料方向的三个扇区严格下界，所用精度 |
| 原 rank | active ordinal、cap index、rank=$iN_C+j$、两个原 cell 的完整身份 |
| 叶域 | 原 r/q/帽 XY 的闭子域、相位图和闭子区间、完整父子细分路径 |
| owner | local-cross-Gram，或原 R241/R281 owner 的真实完整 receipt；不同点与商关系范围 |
| 未决 | 具体未付的表达式/membership/余量/资源原因，不写成几何反例 |

local 分支本身不需要先有单位法向球：真实全域导数满足 R282 的正 Gram 下界已给该图正则性和非零切向分量。若原活动法向球尚未支付，只能在独立 local 证明确实覆盖该叶时使用此分支；不能把旧 normal_ball_certified flag 改成 true。进入 R281 的其它叶仍必须有各自正确连续球。

上述记录是实际责任的可重算证据格式，不是给原非线性求解增加一个 L2/jet/曲率接受门。当前没有实际这些数值。

## 6. 完整组合器的最小控制流

这是后继实现边界，未运行：

1. 沿现有 bind_inputs 的真实场身份接三个来源；保原完整 active_rows 与帽 cells。
2. 按原全部 rank 顺序逐个处理。每 rank 建两张 RP1 图上的完整空间 product 根节点。
3. 对当前节点，先尝试任何可复用且明确覆盖此叶的旧 owner；局部 cuff 分支可使用 R282 常数和真实 material membership。
4. 若 local 不适用，原 R281 四门仍保 OR；正确连续球只覆盖当前完整空间子域，同一相位区间不另换基面。
5. 未决时二分一个空间或相位区间。保父域等于闭子域之并；禁止丢公共端点或根据像很近删除 leaf。
6. 每个 rank 只有当两图全部叶都已支付才记完整 component paid。部分支付时保存剩余叶，不把一个 local leaf 提升为整 rank。
7. 全局记录全部 rank 的已付/未决状态及准确未访问后缀。预算退出只影响资源结果，不改变旧科学门。

R282 保证：在真实完整有限系数、严格 marker 支撑和共同 cuff 图输入下，正确粘合的对角三元组有一个带严格余量的局部邻域；足够细分可支付这些局部责任。它不保证远处剩余几何责任都能通过，不承诺任意场的完整 reach。

## 7. 当前 source-only 证据与范围

本次逐源读取了旧 path/cone/flat-cap 机制、实际 full field 的 tail/material-angle/Hermite 形成、共享 B 首端点、固定帽全支撑及已冻 mixed rank 规则。没有 import 科学模块、没有调用现有 field/loader、没有本地系数/范数/区间计算，没有新 fixture，也没有 Git mutation 或下载。

本次对应 frozen source 身份由随附小型静态回执逐字 hash；该回执只证明引用的文件身份、语法文本范围和未改旧源，不证明实际场余量。证明文件可直接登记。后继 actual producer/ledger 的实现和使用仍保持独立身份，源不变的历史结果不被重标。

完整 temporary cell、系数和 leaf 数据按 README 第 15 条不入 Git/Release。只保源码、运行参数、真实 run、完整输出 SHA 和紧凑结论；没有为了清单而重下载旧大型数据，也没有为本证明安排等待 fixture 的人工门。
