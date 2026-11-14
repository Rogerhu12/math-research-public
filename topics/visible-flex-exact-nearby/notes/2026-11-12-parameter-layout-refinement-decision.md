# 已付预算下的进一步布局比较

以冻结第18段 R6/Q384 center 与 η=10⁻9 uniform 两真实报告为输入，`fourfold_parameter_saved_layout_refinement.py` 保持 Nt/m、外域和目标不变，对 K 与 N 重新计算全部解析补集，并逐项要求原 target/4 门。此处只计算布局，不采新节点。

中心 field 的 K 可由639降至569，但 N仍1280；density由(N1792,K895)降至(N1664,K761)。均匀 field K511→500，density K511→473，两个 N都仍1024。两源实际主费用为真场采样，因此未据这个小收益改变已冻结v5或重算完成叶。记录的成本判断不赋予任何新连续密度证书；所有提出的新节点仍欠真实node/RMS费用。

真实输入、完整试验不等式及每一步通过/失败均在 `2026-11-12-actual-parameter18-central-degree-layout.json` 和 `2026-11-12-actual-parameter18-uniform-degree-layout.json`。未来若复用此研究脚本，当前 study 的原函数最低网格口径是Q384，其他Q须显式调整该输入，不能直接转授。
