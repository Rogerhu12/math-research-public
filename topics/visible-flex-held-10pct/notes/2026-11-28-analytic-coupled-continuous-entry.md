# 真 coupled 前缀的连续几何/度量入口：独立适配与真实线性来源拒绝

新入口 `scripts/resume_20261128/analytic/coupled_prefix_continuous.py` 为将来真实 outer 返回的 **最终 physical 高度绑定** 定义独立连续证书入口。当前只有源码、四个原 main 的显式入口替换编译和一次真实错误来源拒绝；**没有正向 coupled 返回，没有新几何/metric/cut 连续证书，也没有本题完成晋级**。

源 SHA-256：`426a8219c67920391463a6ff0c5ab56c8ed02f9f4d7dbd19a6a53dfcc69676ae`。此前已经绑定实际场的原 geometry、tables、metric、cut 和 target 源均不改。新的入口要求它们的已读 SHA 一致，且给新执行记录原 main SHA、执行 main SHA 和逐条唯一替换。

## 实际来源与定义

`geometry` / `tables` 只通过 `actual_cartesian_coupled_prefix.load_coupled_prefix` 取来源；`metric` / `cut` 自己的初始化器通过 `accepted_coupled` 检查真实原全门、原执行绑定、原完整 raw/physical 和最终原尾 packet。没有替换或放宽 `accepted_original`，也没有给原 design run 改标签。

物理文件 SHA 来自当前实际 `physical.npz`，并与最终 endpoint binding 的 physical 引用逐项相等；不假设 coupled run 具有旧 original 的 `physical_sha256` 字段。`FrozenTarget` 使用真正 coupled model/flow、该返回的参数和完整记录构造，包含当前 delta、完整 g 与真实桥端修补。源 mean_N 与 GL6 沿真实 source，不借旧 E 的目标或 mean。

完整高度只认 `endpoint_binding.candidate_H`。cut 入口必须有相同完整 packet、真正 unscaled factor=1，reference/request/checkpoint 的全部 M 个二进制高度逐位一致。raw candidate 即使只差舍入也不被替用。原完整高阶 planar/height 谱、cut 的全部三阶角导数、零模位置抵消以及一二阶零模保留，均由已审原 cut 代数处理。

每份新报告（包括 metric/cut 最终报告）携带 `source_kind=actual_coupled_final_physical_height`、coupling-summary 引用、full-height binding/packet/二进制 H SHA、当前物理文件 SHA、字面 mean 规则和实际 adapter 来源。旧 R73/R74 或其他场的表/证明不满足该合同。cut 的未修补补集只有在新场自己的几何、rational-curvature 和 metric 完整覆盖都绑定同一新定义数组/同一 target 时才能继承。

## 复用的数学代码边界

原区间公式、角 Taylor 与插值余项、原递归径向覆盖和全部证明门保留。四个 main 只在局部新 namespace 中作声明好的入口替换，未改导入模块的门。geometry/tables 的两个替换分别是 honest loader 和当前物理 SHA；metric 仅换 honest constructor；cut 换 honest constructor 及带当前 coupled 合同的两个继承门。四个实际原 main 均完成编译，替换计数为 2 / 2 / 1 / 3，每项恰出现一次。

`CoupledCutMetric` 的方法继承次序为 `CoupledCutMetric → CutMetric → CoupledNewMetric → NewMetric`；原 `super().evaluate` 因而仍进原 `NewMetric.evaluate`，仅初始化及输入绑定走新的真实来源合同。没有新数值或区间算法。

## 已实际执行的负向

当时尚无真实 outer/coupling-summary，故使用现存 original linear lambda=.002/M24 的真 `run.json`（SHA `1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891`）作 source，并**明确故意把同一真 run 放入错误的 coupling-summary 参数角色**。没有生成假 summary，也没有把活 E 尾的 summary 当 outer 记录。

`preflight` 实际 exit=1，原 `accepted_coupled` 明确拒绝：`Only a genuinely accepted, execution-bound actual coupled return is allowed`。门内耗时 0.001080538 秒，整个进程峰 RSS 66236 KiB；没有构造大 prefix、没有 tail/BVP 求解。报告的 `actual_coupled_source_verified`、`full_height_binding_verified`、geometry/metric 全为 false，`source_kind=null`。

这只核验线性来源/错误 summary 角色被拒；它不验证未来真实 coupled 正向路径，不覆盖未实际到达的深层 packet 绑定分支，也不替代真正全 H bundle 或新场自身连续证明。源码编译、该真实拒绝的原 JSON、全部 SHA 和具体执行边界见同名 JSON。

## 调用合同

每一 phase 在新进程运行；旧 phase 的其余参数原样跟随：

```text
python coupled_prefix_continuous.py geometry --coupling-summary ACTUAL_SUMMARY --source-run ACTUAL_RUN --outdir NEW_GEOMETRY [原 geometry 参数]
python coupled_prefix_continuous.py tables --coupling-summary ACTUAL_SUMMARY --source-run ACTUAL_RUN --outdir NEW_TABLES [原 tables 参数]
python coupled_prefix_continuous.py metric --coupling-summary ACTUAL_SUMMARY --tables NEW_TABLES/summary.json --outdir NEW_METRIC [原 metric 参数]
python coupled_prefix_continuous.py cut --coupling-summary ACTUAL_SUMMARY --tables NEW_TABLES/summary.json --geometry-bundle ACTUAL_FULL_H_BUNDLE --base-metric NEW_METRIC/summary.json --base-geometry NEW_GEOMETRY/summary.json --base-curvature NEW_RATIONAL_CURVATURE --outdir NEW_CUT [原 cut 参数]
```

rational-curvature 仍调用原 `cartesian_prefix_curvature_rounding.py`，但输入必须是这次新 geometry 报告。它绑定该报告和其新定义数组；本入口不会把旧场 rational 结果搬过来。所有实际 proof 数组/运行记录放在源仓库外。
