# 完整168：实际坐标非线性metric预测与已付选点二jets出口

日期2026-11-16。本文记录已实现但尚未执行的两个独立源码接口，分别支撑后继不同的非线性模型和跨接受点的必要输入保存。它们不插入正在结算的small168原会话；没有本地科学执行，没有开发试跑，也没有新的几何接受。

## 1. 实际候选坐标的完整非线性metric预测

原式见[R504](../results/R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders.md)。新源码 `frame_complete_body_extension168_nonlinear_metric_line.py`，33071 B / SHA256 9ab2222f217b06142fb9906fdba22ac1538691cbeae338003c0deb226ef8b931。其 POLICY 为 `complete168-actual-candidate-nonlinear-metric-only-predictor-v1`。

`ActualCandidateMetricPredictor168(field,current168,radial,thetas,first_jet_bounds,source_receipt,wall=...)` 固定原已付两网U/T/e/f与a/a_s。`predict(actual_candidate168,candidate_receipt=...,capture=...)` 直接使用真正应用后的binary64坐标，不以名义alpha重新构造候选。全部旧154＋新8切向系数进入原scalar_frame；原角相位与完整Π保持。

数学差式是
$$
U_1=U_0+a_s\Pi(T_1-T_0)+a\Pi(T_{s,1}-T_{s,0})+(b_1-b_0)e_3.
$$
源码明确把重新计算的基点frame与已付T之差另报，并给这条新浮点组装独立身份；不称其与ordinary逐bit相同。六高度系数差取两个实际binary64数的准确有理差，再与原binary64密度样本作有理点积后转float。该步骤不把母函数/超越采样宣称为准确实值。若全部162切向坐标逐byte相同，直接复用已付T，仅加高度差，无新frame/Π。

每个结果给完整U/T/e/f/eta及其数组身份、最大值位置、当前field/metric/grid/candidate来源。模块不取X或中心原函数，不求J、曲率、硬行、14门或标量最优。原affine-observable的凸性不能转移到这个真实参数图；未来调用者须另定义有限查询规则与统一预算。候选仍须通过原两网14门和准确172盒才可接受。

所有started/completed/failed preparation及实际调用入口分别记；首次基点frame和高度密度在同一进程缓存。capture保中途已完成数组和输入，wall检查在工作完成后失败不会把同一工作再算一遍费用。此模块不授予预算；imports、解析、准备、候选查询、失败、输出全归未来原任务账。

## 2. 原ordinary已付内存的selected-only出口

新源码 `frame_complete_body_extension168_selected_cache.py`，34389 B / SHA256 3047e5e43d03a6f17aafb48f43e9d899e75e0a8fb46aae0d9161b7556487dc3b。POLICY `complete168-paid-selected-ordinary-cache-and-current-J-v1`。它补的是以后当前点J所需的原二jets保存，不补已经丢失的56数据。

三接口如下：

- `export_selected_current168_geometry(...)` 从同一实际点的原 `field.bind_ordinary` 取当前pool字面次序、其unique物理点的七数组X/Xs/Xt/Xss/Xst/Xtt/T，另保存query径向并原首末点的a/a_s/a_ss；若原paid height完整存在，仅选其b/b_s/b_ss作来源，不重新评价。
- `bind_selected_current168_geometry(...)` 以原stdout的expected binding认证当前168/物理172、固定g/b0/reference、cfg/side、grid、pool版本和原顺序、每数组dtype/shape/bytes/SHA，得到独立selected-only binding。
- `current_168_selected_rows_from_selected_geometry(...)` 新求完整168导数；沿原三family全角kernels、virtual jets、原metric/curvature contraction、全部旧154＋新8径向展开和六高度列，仅把原ordinary gather改成已付选点读取。新J须单独收费；不复用旧点最终J。

选点binding不伪装成fullgrid ordinary，不为未保存点补零。只有原pool里已保存的原row ID可由该入口请求，即使另group恰共享一个物理点也不能越过声明范围。新增metric attainer走已发表metric-only导数入口和完整U/T缓存；未保存的新hard行没有免费输入。

未来实际接受时必须先完成原value-only学习追加池，再在ordinary数据仍在内存时导出两网选点数据；实际14门的原收据保独立。原full U/T缓存仍负责完整方向分离，该出口不替换它。当前点以后的selected J仍是新科学工作，导出/序列化也计原实际时钟。源与参数可入Git，机器payload只能留原stdout/临时runner。

## 3. 当前边界与继续

本次仅源码推导和文本读取。两个源import不主动运行科学；未执行其预测、导出、重绑、J或任何测试。small168同账原结论须读它自己的FINAL_CLOCK与全部门，不能被这些新接口补写。后继真实非线性模型继续支付曲率所需B0或b_s、全实际门、同g精化和主课题完整C²/厚度/幅度义务。
