# R141 补充：同选定成员的完整正侧 Newton ordinary source 七量实际完成

2026-11-20，维护会话 `visible-exact-astra-ac637-20261120`。

## NA.1 完整原结果与确切范围

[公开 Actions 44765046846/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44765046846)
已完成唯一新科学 child，返回码 0，18/18 门为 true，7 个完整 scalar
均已按合同保存、从磁盘读回并核 contains。完整原文件为：

| 文件 | bytes | SHA256 |
|---|---:|---|
| [positive-Newton-ordinary-source.json](../notes/positive_Newton_ordinary_source_ci/run-44765046846-1/positive-Newton-ordinary-source.json) | 35749 | `223461e2bf67ee35054b15a713928c5fa90bbf315f442c9f394a8e3403a20166` |
| [execution.json](../notes/positive_Newton_ordinary_source_ci/run-44765046846-1/execution.json) | 18244 | `fb7782433762b9e1d4e69c78f319b7b5b15cfae827311cf600654e655bf89198` |

两者的 `complete=true`、科学 `proved=true`、`failure=null`，没有 timeout。
实际科学 checkout 为 `e2f8d963ac3df8fae61ec3f2b1d4399a55fc1ab0`；
触发提交 `f2a3dc66ca60ed4641c34cbc5dbc40885f0c3b9a`。
Python 3.12.14、python-flint 0.9.0、320 bits；数学时间约 0.176657348 秒，
完整 child 约 1.396090608 秒。时间仅说明本次执行，不作速度或复杂度定理。

原对象仍是 candidate `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`、
连续中心 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`、
完整方向 `6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。
固定内禀 $\eta_0$、$\nu_0$、振幅、真实根和独立 even mean 与
[N.1–21 同成员和新补尾证明](R141-supplement-selected-member-and-complete-positive-Newton-source.md)
完全相同。

原 implicit pair 给出的 $\delta_*$ 满足
$|\delta_*|<9.368259853002\cdot10^{-11}<10^{-10}$。
本次只将原 uniform 区间限制到包含该同一成员的半径 $10^{-10}$；
没有把 $\delta_*$ 设为半径端点，也没有创建新的共轭族或延长 WOBSA 的适用范围。
Newton ordinary source 为 $-f_{\delta_*}$，下列是它的范数 upper。

## NA.2 七个完整新上界

径向范数使用真实 $dr$，角范数使用原 moving 圆周的归一化测度；pair 为
Euclidean $L^2$，完整独立 even mean 保留。`low193` 为原 96 对非零模加 mean；
下表 high 是已知源的 97–288 部分，绝不对未知解施加有限角支撑假设。

| 顺序与原字段 | 完整结果的方便严格 upper |
|---|---:|
| 1 `new_outer_tail_raw_physical_residual_L2_upper` | $5.110321\cdot10^{-8}$ |
| 2 `new_outer_tail_continuous_centre_repair_L2_upper` | $4.737093\cdot10^{-15}$ |
| 3 `new_outer_tail_selected_nonlinear_remainder_L2_upper` | $8.799654\cdot10^{-16}$ |
| 4 `complete_outer_tail_selected_Newton_full_L2_upper` | $5.110321\cdot10^{-8}$ |
| 5 `complete_positive_selected_Newton_full_L2_upper` | $7.044651\cdot10^{-8}$ |
| 6 `complete_positive_selected_Newton_low193_L2_upper` | $7.044651\cdot10^{-8}$ |
| 7 `complete_positive_selected_Newton_high97_through288_L2_upper` | $1.102257\cdot10^{-15}$ |

表内只是对已保存完整球作向外简写；后继消费者必须读原完整记录。
第 5、6 条原球中心分别约 $7.0446502653441925\cdot10^{-8}$、
$7.0446502653026983\cdot10^{-8}$；其差不能用来反推或代替 high 范数。
第 7 条独立完整 upper 约 $1.1022563095834347\cdot10^{-15}$，不是零。

设 $C_{full},C_{low},C_{quad}$ 为只读旧 CRA 核区记录，
$S_{full},S_{low},S_{high}$ 为只读旧完整方向源记录，$d=10^{-10}$；
本次新外尾量记作 $R,T_{rep},N$。N.16–18 的实际消费者准确实现

$$
T=R+T_{rep}+dS_{full}+N,
\qquad F_{full}=\sqrt{C_{full}^2+T^2},
$$
$$
F_{low}=\sqrt{C_{low}^2+(R+T_{rep}+dS_{low}+N)^2},
\qquad F_{high}=dS_{high}+\sqrt{C_{quad}^2+N^2}.
\tag{NA.1}
$$

每个下游使用之前均先保存、读回同一完整 ball，再取其有向 upper。
真根至 $9/10$ 与 $[9/10,25/8]$ 径向不交（端点零测），故所用平方和合法。
旧 $C_{quad}$ 已含核区选定参数二次费用，不能再按另一半径任意缩放。

## NA.3 原字节复用与新补尾的完整性

[首次 manifest](../notes/2026-11-20-R141-positive-Newton-ordinary-source-inputs.json)
为 17776 bytes，SHA256
`8866c54756973ef453f18eaa9e1aae22f8a7ac248fb2a823c7a7ed8207200315`。
29 个当前小输入与原 manifest 的 bytes/SHA/blob 完全相同；
7 件历史原件按 raw3、positive4 的原序恢复整个容器：

| 原完整容器 | bytes | SHA256 |
|---|---:|---|
| raw7296 | 4592623 | `6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1` |
| positive4650 | 6223338 | `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d` |

原 6143/3594 接口与完整原行准入后，新 raw 外尾有 1341 个交段，
positive 外尾有 1346 个交段，准确终点 $25/8$，完整长度 $89/40$。
没有重算原 whole7296、原核区、true-root germ 或 whole7721 目标。
原 CRA 在整个 $[0,9/10]$ 的成功结果直接限制到 $[r_*,9/10]$，
没有从 whole upper 减去另一 upper，也没有按长度比缩放。

中心修补 pair $A^0/A^1$ 费用保持 $3.861\cdot10^{-18}$、
$1.970\cdot10^{-17}$；它们没有乘以参数缩放。
只有原 full-delta 方向包络因真实参数方向线性而缩 $1/100$；
完整 mean、方向连续修补和原源 mean 费用按 N.1–21 各付一次。
原物理振幅也只乘一次。全部 old producer、old target、old scientific import、
新数组、artifact、Release 计数均为 0。

执行原件记录 5 次 pull 后 README 检查，完整保留首条及末三条 receipt；
留存项实际 diff 和相对已读 `96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1`
的 diff 都为空。其余 receipt 按原执行合同在公开 job log 打印并参加链 hash；
此结论不声称独立恢复了不在小 execution 中留存的第二条。

## NA.4 已关闭与继续义务

本结论关闭同一 selected member 的正侧 ordinary Newton source 数值槽，
并同时给出完整 full、low193、known high97–288 三种兼容上界。
与 [真实物理源对](R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md)
结合时，仍须按其原单位和完整 18 输入接线，不能用普通源范数代替边界值。

真实外端 Robin、独立 physical mean 和 height RHS 的实际值仍未由本次计算证明。
N.21 的 mean 是准确倒数 $m_\delta(R)^{-1}$；不能改成 $m_\delta(R)-1$。
选定成员的角共轭 $H_*$ 也不是外高度 $f_B$。
low193 完整逆、真正物理 97+96 外行、future224/future32、两条 WPN 完整 RHS、
负侧/根/接口数据、全频非线性迭代及最终精确闭曲面族仍独立未付。
原 JSON 对这些结论的 false 状态全部保持。
