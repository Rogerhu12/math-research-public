# 从实际完整 QP 终态绑定固定 g 径向精化

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**状态：完整的报告代数恢复规则与小入口；无本条新的科学计算。** 本文把 R676 的转移和完整 fine QP 接到一个真实、自然结束的 full-QP 父报告。默认只作 stdlib 报告／身份／预算诊断；实际数组读取、精化、场复读和求解只在本仓库公开 Actions 的 `--execute` 模式中进行。没有在本地运行科学程序，也没有增加数值 fixture。

## 1. 父身份与末阻尼的准确恢复

入口要求父报告 `complete == true`，并核

$$
\operatorname{SHA256}(\text{实际父 bundle})
=\texttt{final\_bundle\_sha256},
\tag{1}
$$

以及实际观察 carrier 的 SHA 等于父报告 `observation_carrier_sha256`。这里用父的**终态**字段，不把输入 bundle SHA、旧 run 的候选或只存在的中途 checkpoint 冒作自然终态。

绑定的原完整 driver 为

`fullclosed_gauss_inequality_qp.py`

SHA `5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a`；R671 driver 为

`fullclosed_gauss_exact_tail_inequality_qp.py`

SHA `b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8`。

两者没有 `final_damping` 字段。令报告初值为 $\mu_0$，第 j 个完整方向中记录的实际阻尼为 $d_j$。源码的唯一更新规则是

$$
\mu_{j+1}=\begin{cases}
\max(10^{-8},d_j/2),&\texttt{accepted=true},\ \alpha_j=1,\ r_j\ne\mathrm{null},\ r_j>.75,\\
d_j,&\texttt{accepted=true}\text{ 且不满足上一行},\\
4d_j,&\texttt{accepted=false},
\end{cases}
\tag{2}
$$

其中 $\alpha_j$ 是 `accepted_alpha`，$r_j$ 是 `actual_to_full_step_predicted_decrease`。最后这个比是**实际下降与完整步预测下降**之比，不能按接受的半步另造一个比。接受半步不自动减小阻尼，阈值严格为 $>.75$。

入口逐条从实际 `directions[j].damping` 读取，并核 $d_0=\mu_0$、后续 $d_j=\mu_j$，再作 (2)。若 `directions` 为空，最终值就是 `initial_damping`。两份冻结源码的 initial-filter／target 提前退出都发生在当轮改变阻尼之前；所有实际阻尼更新之后才 append 该完整方向。因此归纳即可证明上述恢复是其正常终态下一步将使用的阻尼。

计算使用同一 binary64 字面规则，包括源码的 binary64 `1e-8` 下限；同时记录 float 十进制、hex 和准确 binary Fraction。这里是对既有报告控制状态的准确恢复，不是新的表面计算。不会复制其他 run 的阻尼，也不假定缺失的 `final_damping`。

将来若父来自 R676 派生的 fine driver，可显式提供该实际 `--parent-source`。入口先核实际文件 SHA 与报告一致，再核 provenance 中的冻结 base 与已刊 `100e57…` 派生器身份，但**不会把注释头作为正文相同的证明**：它读取相应冻结 base，用该派生器的 `ExactLocationDriver` 在内存中重建完整 AST，核其一处 size、六处位置键、一处 schema 修改，按已刊 writer 的 `ast.unparse`／重新解析方式得到预期正文 AST，再与实际派生文件的整个正文 AST 比较（仅忽略源码行列位置）。不一致就不能按 (2) 重放。

此步骤只 import 已绑定的 stdlib 派生器、处理源码 AST，不 import／执行父 driver 或任何场模块。报告同时保存完整 AST 相同标志、AST 摘要 SHA、真实 base 与派生器 SHA。主入口先完成 `bound_parent_source`，再调用 `terminal_damping`；共享 helper 的其他消费者也须保持这个顺序。未知更新规则的其他 driver 不猜测末阻尼。

## 2. 全部可恢复永久位置的并集

只传最初 coarse manifest 会漏掉完整 QP 后续找到的位置。本入口从本次完整父报告递归提取：

- `final_curvature_memory`、`final_radius_memory` 及 protected 标志。
- 每方向、每 trial 的 `new_permanent_curvature_locations`、`new_permanent_radius_locations`。
- 所有实际 geometry 中的 `cell/u/phi` 字典以及 `stage/phi` 或 `stage/angle` 字典，包括观测最坏点、半径最远点和任意点读数。
- `arbitrary_*_sources.locations` 中保存的原输入位置。这些位于旧 `round13` 去重之前，可以恢复其中仍有记载的不同 binary 实数位置。
- 工作不等式中的 `('grid',stage,angle,branch)`、`('arbitrary',cell,u,phi,branch)`、`('grid_radius',stage,angle)`、`('arbitrary_radius',cell,u,phi)`。
- protected 代表中的 `seed=[cell,u,phi]` 与 `current_location=[cell,u,phi]`。

常规数值向量或任意三元素 list **不会**被当成位置。仅解释以上有明确字段／标签的编码。`fixed_core`、`cap_height` 是原 solver 本来保留的直径下界分支，不伪造成一个几何观察地址。完整 geometry 的 `arbitrary_witnesses` 合并了两类位置且没有逐项类型；这些记录保守地进入曲率与半径两个位置集合。

位置键为准确数值 tuple，保留 binary $u,\phi$，不取 13 位小数，不按距离或“同一个 basin”删点。相同 tuple 合并时 protected 用逻辑或。只能恢复原报告或调用者 manifest 实际保存过的位置；对从未保存的信息不作可恢复承诺。

只有 `stage` 的位置要读取原 carrier 的 `observation_cells` 和 `observation_u`。此数组读取仅在 Actions 中发生，使用 stdlib 对实际 NPZ 内这两个向量读取；不 import 场模块、不求值任何几何。角索引是当前 quarter 列号，使用绑定算子的字面公式

$$
\phi=\pi\,\mathrm{angle}/(N/2)
\tag{3}
$$

恢复数值角；已直接保存的 `phi` 则原值保留。先核 carrier SHA，再按其实际 stage 映射，不能把旧 stage 编号硬套到新 mesh。

Actions 写出一个只含位置与来源的补充 manifest，绑定当前父 bundle SHA、carrier SHA、完整父 report SHA 和本入口 SHA。**调用者提供的全部旧 manifest 仍作为独立参数原样传给 R676**；补充 manifest 不替换它们。R676 再做准确二分坐标迁移、完整并集与真实 fine 几何复读。没有任何旧曲率、半径或通过标志被当成新值继承。

## 3. 单因素的首批预算

默认链只做一次径向二分。M 和完整角数 N 都取实际父报告的值，不增加频率；当前 M160 父便仍为 M160。保留固定解析模型、$\lambda/\eta$、同一 scalar 输入及全部原行。六 Gauss／胞及全部旧观察的正权由 R676 处理。

fine solver 固定首批为：

| 参数 | 值／来源 |
|---|---|
| 径向二分次数 | 1 |
| M、完整角数 N | 与实际父相同 |
| 新 Gauss 阶数 | 6 |
| fine 方向数 | 1 |
| 最大 QP Hessian advances | 256 |
| `qp_atol` | 0 |
| `qp_rtol` | 默认 $10^{-6}$，完整 argv 记录 |
| 初始阻尼 | 本次父报告按 (2) 恢复的真实末值 |
| 正谱目标 | 原 $p=8,\epsilon=.001,c=.05$ |
| 原径向混合参数 | .5；跨层权变化按 R676 另读共同父泛函 |
| 数值几何 policy | 原 .992；仍不是连续 reach 结论 |
| 完整工作行上限 | 默认192，明确参数记录 |
| stage block | 默认64 |

父报告中的 coarse centers 若有明确列表，也原值传入 fine launcher。此入口绑定当前固定 p8、.5 混合、.992 policy 的父；不会在“只做径向精化”时悄悄换一个 objective 或几何 policy。频率增加应另起一批并明确比较范围。

设父有 J 个节点、P 个径向观察，则 $J'=2J-1$。新原生 node/mid 加六 Gauss 的行数是

$$
P_{\mathrm{standard}}=(2J'-1)+6(J'-1)=16J-15.
\tag{4}
$$

旧 node/mid 均已成为新节点，其余原行最多还需 $P-(2J-1)$ 个，所以

$$
P'\le16J-15+P-(2J-1).
\tag{5}
$$

实际准确重复点只会减少这个上界。M 不变时每个插入节点带来 $3(3M+2)$ 个完整内部 jet 自由度，故原变量及完整 integrated 坐标的增加量均为

$$
3(J-1)(3M+2).
\tag{6}
$$

默认 report-only 读 J/M/N/原行数和变量数，输出 (4)—(6) 及一个完整 quarter residual、两个第一 jet cache 的组件字节预算。它没有运行场、没有给 solver 性能预测，也不把这些组件之和冒称整个进程峰值内存。

## 4. 入口、实际身份与执行顺序

目标源：`scripts/resume_20261120/launch_refinement_from_full_report.py`。

当前源为 31438 B，SHA-256：

`4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60`。

绑定的 R676 转移源 SHA：

`2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a`；

绑定的完整 fine bridge SHA：

`100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622`。

R676 转移源含当前新 node/mid 的 `true_a_stage_boxes`：直接保存本次已查询的整数 oracle 盒，供冻结 R657/R674/R675 消费，不复制旧盒、没有额外 query。

默认只作报告／预算诊断：

```bash
python "$TOPIC/scripts/resume_20261120/launch_refinement_from_full_report.py" \
  --repo "$REPO" --work "$WORK" \
  --parent-report "$ACTUAL_FULL_REPORT" --bundle "$ACTUAL_FULL_FINAL" \
  --carrier "$ACTUAL_PARENT_CARRIER" --node-report "$ACTUAL_PARENT_NODES" \
  --scalar-input "$ORIGINAL_SCALAR_INPUT" \
  --manifest "$COMPLETE_OLD_LOCATIONS" \
  --outdir "$WORK/current-full-r2-01"
```

`--manifest` 可重复。默认只读报告、来源／输入 SHA 与纯位置 JSON，生成 `plan.json`；stage 数组待解析的位置数单独登记。不会打开科学数组内容、不会生成场、不会启动 solver。

在公开 Actions 中加 `--execute`，可在身份／argv 完全相同且尚未启动科学步骤的同一个诊断目录继续，依次：

1. 按当前真实 carrier 解出全部剩余 grid 位置，写 `parent-report-permanent-locations.json`。
2. 调用 frozen R676，写 `refinement/` 中实际转移、同 oracle 新观察、binary 差界和初次有限读数。
3. 调用 frozen fine bridge，写 `fine-full-phi/` 的一方向真实求解。
4. fine bridge 自动读取实际终态的共同父 grid；链入口再绑定 fine `complete` 与 `final_bundle_sha256`，记录真实输出 SHA。

完整 argv、全部输入 SHA、父 driver／依赖 SHA、R676 两个源 SHA、阻尼逐条 trace、位置来源、执行 run/attempt/commit、派生 fine driver 的命令清单与实际终态均记录。fine driver 的工作目录由这次父报告 SHA 与本次目录名区分，避免不同批次覆盖同名命令清单。曾经开始执行的预算不能被这个入口静默覆盖。

新的 raw bundle、carrier、manifest 和 reports 都只在 runner；公开登记源码、参数、run 和输出 SHA。本条未实际运行上述链，因此没有新的数值终态、下降量或收敛标志。返回一次正常求解也不自动支付 README 的持续精化收敛：只在实际同一父有限泛函上报告可比改变，并继续分别处理新层的完整／连续误差与几何范围。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
