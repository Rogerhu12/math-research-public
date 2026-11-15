# 实际98：31-query 四分之一步接受与原 RMS 拒绝位置

/root GPT-6 Astra Pro (AI-assisted)，2026-11-15。**这是原完整方向的一次 warm 进展，不是完成边值问题，也不是闭面或全域 metric 证书。**

## 原运行与读回身份

科学运行：[43677587785](https://github.com/Rogerhu12/math-research-public/actions/runs/43677587785)，job132701028492，source918fdb11dbb7a424b6149b405e2c7fab3cc0c737。原 artifact14147700690（visible-followup-condensedqp-43677587785-1）809042943B，SHA256 `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`。

只读摘要第102轮v3：[43682529851](https://github.com/Rogerhu12/math-research-public/actions/runs/43682529851)，job132716027313，source4bb0bb4a4ff43a4a9df1fabd2629dcddfea37552；reader28252B/SHA256 `e2e8ec32c30bbc9ff0e77709524ff09f100f0ff5f4decd23c43b6445562b7484`。实际完整摘要83396B，包含末尾LF，SHA256 `5fb8012ed36e10864a61bd08ce26563122b8eea170a73f08f9da2cba8cb6a42e`。root通过终端读回日志并核此身份；只复制原标量，无新数学计算。原ZIP和五件均通过原size/SHA核对；不再次保存可重算数据或摘要文件到仓库/Release。

| 原件 | 字节 | SHA256 |
| --- | ---: | --- |
| model-000.json | 736781 | e2957f2d413653ea08c7f893f7cc3584c05450ff2ccb8c761d8109cfef1dfa6a |
| driver-status.json | 3379453 | b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |
| condensed-QP-summary.json | 121691 | a898e81af8f915b55c2db1607a775c28a89eaae1e782735fb133183c8963ec07 |
| response-check.json | 2648609 | b41e3f6d66f7d7a5bb0b4e6a6e0de56a1fc07c7c648044a86e5d012ea8b99385 |
| warm-001.json.gz | 4927052 | b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 |

原warm解压后14864483B/SHA256 `a09ebdf16eae595e16694fe2b3443d0364f5319bb3a5e1a711ed123ace0bff30`。第102轮v1/v2只因摘要分别474627B/216637B超过90000B失败；v3已经在此限内。v3 job最终exit2来自“status embeds exact original model object”检查为false，其余六项身份检查为true；此对象范围差异须如实解释，不能把job说成全部成功，也不改变已核原件中的科学值或增加新的科学接受门。

## 同一实际模型中的三档试探

原31点为20个left-RMS和11个collocation-midpoint；完整B/H局部维8453、C4059、63488角约束行，完整236036自由坐标。完整outside重建，core/control保持原算法约束；λ270、working512、sweeps200和原17档预算未改。原同权目标基值43.42621386634224，实际方向斜率−0.24800196273797923。

| α | 原同权目标 | 原接受 | 完整域检查 |
| ---: | ---: | --- | --- |
| 1 | 未报告有限目标 | 否 | node0坏、midpoint8坏 |
| 1/2 | 43.31301254907233 | 否 | node/midpoint均0坏，但完整left-RMS有2坏 |
| 1/4 | 43.36604610143146 | 是 | node/midpoint及左右RMS均0坏 |

半步实际目标下降0.11320131726990468，实际/预测比0.9762704788037863；拒绝不是“没有下降”，而是原RMS门：

- LEFT464，s=1.1553475805065636，最小β²=−1.8377510686892449，φ=0.13192234775816514。
- LEFT465，s=1.1603320320063233，最小β²=−0.4505572547560164，φ=2.9084275738311756。
- 右RMS的698个检查点没有失域。

这两个left点本来就在31查询内；它们的实际selected-query读数与完整RMS读数一致。线性域可行不保证有限非线性半步域可行。四分之一步中这两点最小β²分别0.5264639822268476和0.15071074960077457；31点全部原β²读数为正，左右各698个RMS检查均0坏。

四分之一步实际下降0.06016776491077991，实际/预测比1.0029891422465396；physical collocation最大0.00710763096028075，完整边界最大7.837078403973583e−9，constant collocation0。最大physical残差仍在interval461、row155819。status明确success=false、new_coupled_finite_acceptance=false、optimization_progress=true、accepted_warm_steps=1。

## 原 QP/FD 的实际范围与下一动作

原完整模型回读有all_original_rows_feasible=true；实际stationarity L2=0.03338554650327883，R267浮点lower bound43.29600689906853、cross-point gap3.8667486990107136e−8。局部working-row预算及dual-sweep预算均实际用到；不宣称全QP最优，不把浮点posterior当严格包络。

原FD最大四阶相对误差8.408533903133078e−10，原阈值5e−5，implementation_check_passed=true；二阶误差9.883441196551308e−6且收缩检查true。它确实在本次warm重新计算完整边界差分；nonlinear_DN_evaluated、nonlinear_native_at_current_H_solved、full_BVP_solved、full_Cartesian_closed_surface均false。

据最近半步的真实失败点，下一第107轮先从原98的真实warm/status对，在相同31查询与原完整B/H/C/outside/预算/验收门下重新线性化。当前没有近邻证据要求增加新query；不按更远整步的失败点猜补点。后续model→FD均在公开Actions临时目录，按根第15条只留脚本、参数、run、输出hash和诚实结论。完整边值问题、固定g闭面、全t reach和整像幅度仍未解决。

## 第102轮整文档比较的源码解释

已直接读取原 `geometry_20261114_thirty_one_query_condensed_warm.py` 的 `_run_engine.write` 和 `geometry_20261114_seven_query_projection_warm.py` 的 `current_row_labels`。后者递归创建新的dict/list，仅替换两条旧通用标签并原样保留resume_producer。前者先复制本次写出对象，再只给本次报告的顶层补充thirty_one_query_projection_entry、selected_angle_row_count与query_specs；独立model文档的顶层来源装饰不会因此成为status内嵌model的同一顶层字段。

因此第102轮v3把“独立写出文档包含的来源身份也逐字段等于status嵌套科学对象”当成契约，范围过宽。它的false与exit2保持原记录；此源码解释不冒称已经逐字段核过两个原JSON的全部差异，也不据此改写原状态。第107轮只报告iteration、before、固定merit、damping、accepted、trials、方向最大系数的对应关系，并明确该读回不是新的科学门。无需重新计算98或重新下载原大件来重复已经完成的科学结论。
