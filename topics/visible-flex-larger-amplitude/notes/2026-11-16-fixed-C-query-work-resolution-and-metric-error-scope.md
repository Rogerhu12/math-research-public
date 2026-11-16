# 固定准确 C 与闭目标下的区间精化、真实误差测量和原求解容差

日期：2026-11-16。作者：geometry agent（AI）。

本说明仅整理已发表源码和已有证明的可执行接点，不另设结果编号，不增加科学接受门，不改变正在执行的 209、212 或已冻结的 214。没有执行区间、积分、BVP、编译、AST 或科学测试；没有实际 accepted450、误差序列或误差平台的新结论。

## 1. 应先区分的两个操作

在同一准确 C、全部许可根族、十个准确参数、完整 construction、首材料图和 $t\in[0,1]$ 不变时，可以分别做：

1. **同一已生成场的测量精化。** 不重求 BVP，只增加完整空间包围、同 C 查询和准确相位逆的工作。它可能缩小 R459 的误差区间 $[L_j,U_j]$，但不产生一个新场，不能重标为一次 mesh/M/native 精化。
2. **同一目标上的新场精化。** 沿真实 accepted 父重新求解新的径向节点、N、steps、M 等，重付全部 H/J/FD/fullDN/final/audit，再重新生成径向 Hermite、shared 场和几何证据。真实误差可能改善，也可能不改善；需由同一目标的 R459 量比较。

两种操作可以在原绝对钟内交错。固定 $\eta$ 多次通过、增加节点数或增加 query 预算，都不单独证明实际误差下降。[R459 §459.7–9]

## 2. 已有可收紧的工作接口

| 对象与真实入口 | 可以明确增加的工作 | 保持的数学对象与限制 |
|---|---|---|
| R459 `Measurement.base_measure`、原 a601 `root_plan/roots/split_cell` | `interval_bits`、`sqrt_bits`、`initial_angular_depth`、`max_depth`、`max_cells`、测量预算；减小 `measurement_width_goal` | 完整两反射片、全部 prefix/native/collar/patch、全角与两帽不变。细分减少单元内位置变化和部分天然区间依赖；不自动改变 C 叶盒、固定场数据或真实场误差。 |
| R426 `LiveQueryTarget.refine` → 原 f12f `QueryCover.run/split` | `c_queries.precision_bits`；积分 absolute/relative bits、guard、evaluation limit、integral depth；inverse depth、value width bits、累计 panels/nodes/活动预算 | 对同一准确闭径向区间重算原六 primitive 的子积分，保所有可能逆像和完整深尾；新合法 E 包围与旧完整界求交。资源停保完整粗父，不以 `work_resolution_complete=false` 拒绝有效界。 |
| R400 `AccurateTenTarget`、R416 `AccurateCutModel` | 实际 `sqrt_bits` 与场的 interval precision；完整空间分格 | 对同一 DAG、同一固定 E0/E1/E2 盒重新作向外开方和完整表达式传播。只能改善算术表示误差；没有 cut 叶更新参数。 |
| R457 准确共同材料 API，经 R459 `evaluate_active_cell` | `max_inverse_steps`、`max_phase_query_cells`、interval bits、实际时间网格 subdivisions | 同一首材料定义与当前完整场。准确逆是同一 $\Theta_j^{-1}$，有限逆迭代只是包围工作，不能取中点定义另一张材料图。 |
| R352 共享校准正规形式、完整多项式 Bernstein；R481 的 coast 责任及 R483 独立实现 | 在相同叶盒和全分支上先准确合并，再包围；对子域作完整 Bernstein/de Casteljau 细化 | 消除重复 DAG 变量、完整 bump 求值和同变量差的部分依赖，不改变准确目标或原全部控制。R483 当前只改同一固定盒的 coast 三 jet 传播；不重 C 叶、不替代初始 factory 的完整域责任。其 source-only 状态不得写成已执行。 |

R426 的十一参数不是只改一个 `precision_bits`：源码同时保存绝对/相对积分目标、每种计数和预算。更高位数不代表原已保存端点被重新计算；更高 depth 也不保证可分辨的界更窄。实际返回旧界与新界的交保包含关系，但没有成功、终止或每次严格收紧的承诺。[R426 §426.4–10]

214 当前仍按原冻结 choices 使用相同的 C 查询参数；其中 query precision256、积分 absolute/relative128、inverse depth40、value width80、query 活动预算900 是既有声明。三次 R459 测量仍使用 interval256、sqrt128、max depth20、100000 cells、width goal $10^{-8}$、每次最多300秒并裁原钟；真正时间细化为4/8/16。它们是当前计划，不是观测到的实际耗时、宽度或误差。没有在本说明中修改这些值。

## 3. R426 真正重算了什么，明确没重算什么

原 f12f `ContinuousHead` 固定完整160条 shallow 字面表、原正 global lambda、cap/flat/weight/cut 公式和物理参数，形成 n159..0、每层9片，共1440片。`build_head` 按完整六 primitive 构造累计径向端点与全头积分。

R426 `LiveQueryTarget.prepare` 实际读取并绑定同 job 的：

- `large-arrays/source-piece-index.json` 的完整1440分片身份；
- `large-arrays/complete-source-radial-panels.jsonl` 的全闭参数分区、共享累计径向端点、原 E/E_r/E_rr 行；
- 原 result/input/query 的完整身份与自然外端，原全部许可深根前提。

它从这些已保存端点建立原 `QueryCover`。细分中点使用

$$R_m\supset R_0+\int_{x_0}^{m}(f_0+\lambda f_1)\,dx,$$

并与原单调端点范围求交。**原1440全头总和与已保存累计端点没有在此 API 中重积分。** 新子积分即使很窄，也继续带着 $R_0$ 的原宽度。这是当前程序的确切界限，不是对真实半径不确定性的下界。[f12f `build_head`；R426 `prepare`；R426 §426.4/10]

`QueryCover.run` 的公开数值查询结果只聚合 E。完整叶账同时保 E_r/E_rr；原 `geometry_20261115_stored_C_v3_cut_twojet_readout.py` 才按原点 query 的完整叶 span 重读全部三量并求 hull。它是准确完整读取，不执行新的导数求积。不能把 R426 的一个新 E 区间直接塞成新的 E1/E2。

## 4. 哪些宽度不能靠当前下游细分消掉

### 4.1 固定上游包围

R400 `AccurateTenTarget.__init__` 从真实 definition 的 `actual_enclosure_leaves` 读取 E0/E1/E2，再一次 `tree.evaluate(leaves,sqrt_bits)` 得到长度、支撑和校准系数。`closed_range` 枚举全部可能片，但不会重新取得这些叶。R416 对同一叶建立准确 cut patch 的实系数表达；高 precision 只重新包围该表达。

因此：

- 更细的公共 u 不能自动收窄既定 $[L_*]$；径向目标 $(L_*/L_{\rm num})^2$ 在当前数值图中的输入宽度仍保留。
- 更细的 cut patch cell 不能自动改变其 E0/E1/E2 所带的共同系数不确定性。
- 更细的径向 inverse cell 不能自动消去原累计半径盒宽。

R352 §352.9 已证明并说明这些边界；无需另写一套重复定理。其正规形式能消去**表达式重复依赖**，不能任意缩进给定叶盒的端点。

### 4.2 全深根族与解析 majorant

f12f `ContinuousHead.deep_cover` 对 n≥160 使用固定的全许可原根族正级数 majorant。提高 Arb 精度可以减少该公式的算术误差；原公式的全族范围和估计余量不会仅因精度增大而消失。原 `QueryCover` 对深尾不做数值根选择，保完整深尾为 coarse 叶。

必须区分：真实同族成员之间的差异、现有解析估计的松弛、盒内未实现组合和数值外包误差。当前源码并未分离出它们的最优大小；不能把某个宽盒称为不可突破的真实 metric floor，也不能把中点或另选深根当作同一准确目标。

### 4.3 准确 dyadic 输入与当前有限场

原 shallow alpha/R、lambda、十参数、construction 和已保存 nodal 字词是此模型的准确 dyadic 输入。重新校准其中某个字不是“增加工作精度”。同理，R409 的新 nodal012、FD 二阶和共享 Hermite 是当前准确有限场的定义数据；增加测量精度不会把它们变成准确连续 ODE 解的数据。

R352 §352.7 已要求保数值 literal anchor/width/系数和真实校准缺陷。R409 明示原数值 RK 轨迹到新准确 Hermite 场的误差未因定义而自动付清；其 B 也不被认定满足 $1+B'^2=E_C$。这些量必须由真实新求解/重放改变，或者在原场上直接测量；不能靠重标新 source 抹掉。[R409 §409.1–3/7/10]

## 5. 原 solver/native 容差没有现成全域 metric 单位换算

R459 `Measurement.bind` 实际保存原 collocation RMS $10^{-6}$、BC $10^{-11}$、physical RMS $10^{-6}$ 的原适用范围和 native policy/residual 等原记录；同时明确输出：

```
ODE_RMS_BC_FD_and_native_residual_are_not_this_global_relative_metric_norm = true
tolerance_to_metric_error_transfer_bound_produced = false
reaching_original_solver_tolerance_not_relabelled_as_metric_precision_floor = true
```

所核当前链中没有一个已实现常数把 native 的 $2\times10^{-9}$、上述 RMS 或 BC 直接换算成全闭域相对 Gram 算子范数。原 FD 证明的是所测响应的一致性范围，也不是该缺失的全域稳定性常数。[R459 §459.8]

若以后需要这样一条传递，具体责任是：

1. 保原残差的归一尺度，取得实际线性/非线性问题的稳定性或逆界，而非用“浮点 QR 成功”代替；
2. 控制有限网格 residual 到连续径向/完整角域缺陷的差、RK/求积/模态截断和原边界响应误差；
3. 控制从解系数经新 nodal012、Hermite、R249 投影、shared/cut 构造到完整一阶场导数的传递，保两 mean、所有片/缝、两反射和固定帽；
4. 在同一正定目标及公共材料图上将导数误差换成相对 Gram 误差。

最后一项的标准恒等式说明所缺量是什么：若真有相同目标的准确等距参考 $F_*$，并已证明 $\|(DF-DF_*)G^{-1/2}\|\le\delta$，则展开 Gram 并用 $\|DF_*G^{-1/2}\|=1$ 得相对误差不超过 $2\delta+\delta^2$。当前链没有给出这一准确参考、该全域 $\delta$ 或从原残差到它的常数；此处只是责任分解，不增加一个必须先找参考才能继续原 BVP/测量的门。

## 6. 现在就有的继续路径

**先用已有实际量，而不预言哪项主导。** 214 按原链若真正返回 accepted 场，R459 已能给全域 opnorm 上/下界、完整覆盖/pending、取得下界的实际地址、live C 查询记录、原容差和实际时间点。根据这些真实字段区分缺域、逆像宽、prefix 固定叶宽、场 jet 区间宽或单纯资源未访。

**无需改科学核的第一步是同场更紧测量。** 在原钟允许且另有明确参数来源时，现有 R459/R426 CLI 已支持增加空间/积分/逆像/位数工作；它使用同一准确场和同一 C 族。上界改善只报上界改善；区间重叠保“未分辨”，不阻止继续原精化。[R459 §459.7]

**已有表达式改进优先复用。** R352 的共享变量正规形式及 R483 当前 coast 完整 Bernstein 是可直接继续的同对象传播改进。它们能绕开一部分天然区间过估计，不需要先重选 C 根或改十词。当前 214 冻结件未接 R483，本说明不把未来接线冒现成执行。

**若真实记录指向累计 C 或 cut 叶宽，再回到已有生产器。** f12f `main/build_head/SixPrimitiveIntegrator` 已能在同样三原输入、1440片和六 primitive 下，以新明确工作参数重新生成全头与原点/whole 查询；原完整 cut-twojet reader 可消费其真实新叶。这样是新的科学计算和新 provenance，不是对旧 receipt 改窄端点。R383 的同定义命题已区分数学 C/DAG 身份与运行/外包围身份，但 R400/R416 当前加载器没有开放“替换固定叶”的参数：若在同一既有场上使用新上游界，须另接真实同语义 leaf provider，保原 CP/definition，记录旧新完整来源并重新求值同一 DAG；不能直接覆写旧 definition 后仍声称原 SHA。

**实际场精化仍由原完整路径负责。** mesh/M/N/steps 的 fresh450 与原全部终门不因区间宽而略去；实际 $t$ 网格4/8/16须真查询。全 $t$ 上界来自 R443/R447/R459 对 $(E,G)$ 同时拉回的广义谱不变性和完整角圈，不是由这些有限时间点插值，也不要求把固定帽目标误说成旋转对称。

## 7. 准确来源索引

- `results/R352-shared-calibration-normal-forms-and-complete-Bernstein-target-enclosures.md`：全文已读，特别§352.2–9。
- `results/R383-accurate-R323-target-identity-and-coast-control-necessary-band.md`：同数学 C/DAG 与运行包围来源分责。
- `results/R426-same-job-continuous-C-live-query-refinement-and-complete-metric-interface.md` 与 `computations/geometry_20261115_same_job_C_live_query_provider.py`（31603 B，07fc4e41…）：`prepare/bounds/refine`。
- `computations/geometry_20261115_stored_continuous_E_cover_v3.py`（89307 B，f12f7470…）：`bind_inputs/ContinuousHead.deep_cover/SixPrimitiveIntegrator/build_head/QueryCover`。
- `computations/geometry_20261115_stored_C_v3_cut_twojet_readout.py`（1c39b242…）：原完整点查询叶 span、E/E_r/E_rr hull，无新求积。
- `computations/geometry_20261115_continuous_ten_frozen450_prefix_metric.py`（32761 B，011ca7db…）：`AccurateTenTarget.__init__/closed_range`；`geometry_20261115_current_C_accurate_cut_patch.py`（28417b93…）：`AccurateCutModel`。
- `results/R409-current-continuous-ten450-full-radial-shared-background-and-seam-construction.md`：新准确有限场与数值 ODE 轨迹的边界。
- `results/R459-fixed-closed-target-relative-error-and-refinement-evidence.md` 与 `computations/geometry_20261116_fixed_target_complete_metric_evidence.py`（62091 B，494fea70…）：`Measurement.bind/target/base_measure`、全域上下界、全时间转移及比较。
- `closed-experiment-R437/current-ten450-first-closed-work-choices.json` 与 `request214/current-C-actual202-shallow-inverse-incremental-M-refinement214-request.json`：本说明逐字段引用的工作参数；这里只读，没有改动。

这份说明不宣告观察到了误差平台，不给任意 metric epsilon 作为新的求解停止门，也不把目前缺少传递界当作停止现有直接误差测量和原精化的理由。
