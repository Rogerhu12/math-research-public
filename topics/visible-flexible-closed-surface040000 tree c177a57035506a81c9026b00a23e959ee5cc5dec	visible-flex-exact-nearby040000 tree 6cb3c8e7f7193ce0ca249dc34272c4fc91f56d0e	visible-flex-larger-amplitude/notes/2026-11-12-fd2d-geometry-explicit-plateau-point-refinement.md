# R163 的指定物理点细分：23b3 两个已保存平台端点

## 结论与范围

本组给 R163 的原 schema 增加一个薄入口：在实际保存网格中插入明确给出的 binary64 物理点，也可以选择原 cell 的中点。它保留全部旧节点、物理参数、中央和尾参数布局、完整 atlas/lifting/windows 及其原始源；只按实际新网格重算整帽支撑、冗余列、trace gauge 和有限目标的物理区间映射。没有新 R 号，也没有新 BVP。

本次唯一注入的输入是 `2026-11-12-fd2d-raw-bump-reuse23-b0003-accepted-0001.npz`，SHA256 为 `a485ca86233a196223f16fc2f9c01b7cf3592ae5499d9a04fd94bd7f2511e81e`，129 个节点、K31、16 个尾参数、7 个物理 profile 参数。只复制其 `gauss_l_definition.gauss_plateau` 的两个端点，没有选额外中点。随后主线的 23b4、24 或其接受态不能借用本次有限对照的结论；同一入口可直接消费它们各自保存的实体。

保存输出为 `2026-11-12-fd2d-physical-point-refinement23-01-field.npz`，119880 bytes，SHA256 为 `2e45aeedbee3c9bdb068c1101195a2ff09f57712c4d6e28ebb2a7ea6bded1772`。它仍使用原 independent-tail positive-trace schema，没有新增函数表示。

## 两个请求点、原窗口和支撑

| 保存点 | binary64 十六进制 | 原 cell | 新 cell |
| --- | --- | --- | --- |
| 0.6250652134122892 | `0x1.40088c32f232ap-1` | 64 | 64、65 |
| 0.8344782316901254 | `0x1.ab40bb14aa7eep-1` | 73 | 74、75 |

新增子区间的宽度为约 0.013383538762117397 和 0.0062981358880551674，另一侧次序反转。没有极小子 cell，也没有把请求点吸附到旧节点。

实际窗口使用原保存 `entry`、`exit` 和原乘法产生的 binary64 `rim`。把这些标量视为其精确有理值，数学平台为

$$
[s_{\rm entry}+r,s_{\rm exit}-r].
$$

两个已保存的 `gauss_plateau` 端点各向此平台内部缩进

$$
\frac{5}{144115188075855872}=5\,2^{-57}.
$$

因此，本组没有声称保存端点与上述解析分段点是相同实数，更没有修改窗口来消除这个差别。已保存平台是数学平台的内侧子区间；只在支撑全部落在该子区间内的完整 P1 帽上删除 R153 的 raw-l 冗余。这足以证明删除不改完整场。新 inactive-l 节点是 66 到 74；trace 整帽节点变为 126 到 129，其实际物理支撑保持原样。

原有限内部目标 cell 列表

$$
[63,64,73,74,121,122]
$$

按原物理区间的全部子 cell 映为

$$
[63,64,65,74,75,76,123,124].
$$

端点、每个原 cell 的完整 children 范围、原有限目标定义均保存；后续消费者不能沿用旧整数 cell ID 选择新的物理区间。新节点和子 cell 上的有限求积、节点目标、内部目标是新的离散，并不声称旧有限残差不变。

## 实数恒等与保存误差

R163 的证明对任意细分点适用。若在 $[s_i,s_{i+1}]$ 插入 $t$，则每个 raw Fourier 系数取

$$
y(t)=\frac{s_{i+1}-t}{s_{i+1}-s_i}y_i+
\frac{t-s_i}{s_{i+1}-s_i}y_{i+1}.
$$

精确实数运算下，新旧 P1 函数在整段恒等；同一个固定 lifting、atlas、R153 和 R155 点态映射仍给同一个完整函数。傅里叶阶和尾 Bernstein 阶均不改变。数学证明不依赖本次 48 个有限点。

实际保存使用 binary64。以所有原标量的精确有理值为基准，两个新节点上 raw 系数的最大逐系数误差上界是

$$
\frac{551155087639}{693041296771888296778268672}
\approx7.952701955947229\times10^{-16}.
$$

完整细分 raw P1 函数的逐系数一致范数误差受同一数界控制。每个子区间的斜率误差用左右端点误差之和除以真实子区间宽度，本次上界约 $1.262707267245544\times10^{-13}$。此处理也适用于同一原 cell 中多个新点；没有错误套用仅一个中点时的公式。

整帽 gauge 的 raw 系数最大变化约 15.1361，属于恰好被完整 R153 映射消掉的冗余系数，不能拿它当完整场误差。本次 trace 的 $d=n-l$ gauge 舍入上界是精确零。

原生 reader 的 6 个共同径向点乘 8 个共同角共 48 点，对比完整 $n,m,l$ 及其角一、二阶导数。最大绝对差在 $l_{\xi\xi}$ 为 $4.547473508864641\times10^{-13}$；以 $1+|\mathrm{old}|$ 缩放后的最大差为 $3.5378054133016178\times10^{-15}$。物理 $a,a_s,a_{ss}$ 和实际 chart 的 $U,U_s,U_\xi,U_{\xi\xi}$ 全部差零。这里没有查询径向 jet、没有计算整个有限 F/J、没有 body，也没有连续几何证书。

## API 与近点处理

入口在 `scripts/fd2d_gc_physical_point_refinement.py`：

```python
problem = create_physical_point_refined_problem(
    candidate,
    saved_field=actual_saved_field,
    include_saved_gauss_plateau=True,
    physical_points=(),
    midpoint_cells=(),
    **original_constructor_arguments,
)
vector, definition = problem.inject_saved_field(canonicalize_redundant=True)
arrays = checkpoint_arrays(
    problem, vector, candidate_sha256,
    refinement_definition=definition,
)
```

此入口内部分配一个新问题对象，复用未修改的 `fd2d_gc_midpoint_refined_positive_trace_v3.py`。全部原函数定义匹配后重算实际 mesh 的 N/h/size/coords、中央固定节点、R153 全帽列、R155 gauge pairs、保留的 Gauss 行和缓存。后续短批 restart 仍使用 R163 v3 的 `split_cells=()`；原已保存网格和系数直接恢复，不再次插值或 gauge。

通用入口还支持 `physical_points=(...)` 和明确原网格的 `midpoint_cells=(...)`。已逐字存在的坐标只记录“已存在”；重复请求同一新坐标只记录一次。为避免用 1 ulp 的近零 cell 伪装对齐，默认用精确有理比较，拒绝与现有或本次已插入坐标间距不大于

$$
\max\{16\,\mathrm{ulp}_{\rm local},10^{-12}(s_{i+1}-s_i)\}
$$

的新增请求。这个数值分区策略明确记录在 definition 中，可由调用者明示配置。拒绝时 `UnsafePointInsertion.definition` 给出原请求、精确距离和原因；不会悄悄吸附坐标、移动窗口或接受部分对齐。一个中点若舍入到原端点也明确报告。此策略不是几何不存在条件，也不是新的求解审批门。

## 真实退出记录

第一次运行 session44529 的注入实体已保存；在最后写 JSON 报告时，检查中的 `numpy.bool_` 没有转换为 Python bool，实际 exit1。原检查源、初始报告、已保存实体和失败回执全部保留，未把它标为成功。

随后 `fd2d-physical-point-refinement-recovery-check.py` 回读同一个已保存实体，以原 R163 空 split 精确恢复。没有进行第二次 P1 注入。它核实原全部物理参数/函数 packet 字节、实际支撑和 children 映射，并重做上述小范围原生对照。session53999，初始 chunk4d7ee1、末 chunk69b826，实际自然 exit0；报告计时 11.306426572999044 秒、峰值 RSS 93568 KiB。

以上原始实体和报告的身份以本组 closed manifest 为准。本次改变的是可用于后续真求解的有限分区；强目标仍需实际同 g 完整核、连续误差和几何条件，不能由此组推出。
