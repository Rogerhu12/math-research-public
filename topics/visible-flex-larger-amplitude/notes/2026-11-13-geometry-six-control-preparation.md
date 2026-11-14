# 第六个实际控制的完整几何流程准备与五控真实回归

作者：geometry_audit（GPT-6 Astra Pro，AI-assisted），2026-11-13。

**六控几何尚未执行。** 新接受点必须先具备真正的 accepted/raw/tail 三件身份和同一点 full-J 的 core-held `start_acceleration` 列。这里不把正在求解的 q098 当成已接受，也不把 q096 的五列拼到将来新点。

## Fresh 源

- `root_actual_geometry_fullmean_six_plan.py` 生成 baseline+六控正负共13场。前三个 prescribed core 与 vu、第一转弯曲率保留；第六列是当前点实际 `start_acceleration`。六个差分尺度必须显式指定，无隐含增大。它沿用全部原节点、全模式、生产均值1360规则、原域门和逐场资源记录。
- 新 plan 可消费同接受点 `strong_interior_jet_audit.py` 的最大曲率见证：必须有准确 input SHA、模式数及角网格对齐。该见证的物理 s 转成同实际 chart 的 t 并保留在共同网格中，cubic 重新评价不会替代原 quintic 审计。若384角不能包含实际见证，plan 明确报错要求用户显式提高角数，不悄悄就近取点。
- `root_geometry_minimax_variable_controls.py` 只把原全行 epigraph 算法的控制维数一般化。每点仍有四条带符号主曲率约束和一条固定原点尺寸约束，全部原有限行重新检查。
- `root_geometry_minimax_current_controls.py` 严格消费同点全11或13场，保全每模响应和逐点完整中央差分。`root_geometry_minimax_current_combined_plan.py` 按显式选项将五/六个控制完整送回原 warm 构造器。

没有修改旧五控源、冻结数学源或既有数据。所有新场都仍是浮点几何设计，需独立真实 BVP 和连续认证。

## 已实际核对的范围

用已经真实完成的 q096 新 M28 **完整11场**执行一次恒 S、Δq=.0005 的五控回归，正式 exit0，23.6075434685 s、123852 KiB。原 6,495,360 条不等式全部重查。除新增 `control_count=5` 外，整个预测字典（包括活动行历史、所有 28 core 增量、物理参数增量和极值证据）与原专用五控结果 **完全相等**，不是只比较几个小数。

新组合 plan 的完整 target core、完整 profile、每个实际控制步长及均值规则也与已经实际执行过的恒 S 组合相等。没有为此重复计算组合场。

新六控 plan 的 baseline-only 身份/witness 路径已在实际 q096 完成准备：3383×384 网格、原全部节点及其真实 quintic 最大曲率见证被保留。该例仅验证准备和数据身份；没有执行新的几何场，更没有伪造缺失的第六列。

[精确字典比较记录](2026-11-13-geometry-six-control-preparation-regression-gates.json)、[实际回归输出](2026-11-13-geometry-six-control-preparation-five-regression-r1.json)和[正式资源](2026-11-13-geometry-six-control-preparation-five-regression-r1-resource.json)保留结果。其余可再现计划、网格、四个源的 SHA 见[清单](2026-11-13-geometry-six-control-preparation-manifest.json)。

待实际新点接受后重新计算全部几何方向。`start_acceleration` 的差分尺度先考虑 .002，但必须根据新实际响应和原 finite-domain 检查决定；不能从自由背景高度的符号推断 core-held 几何符号。
