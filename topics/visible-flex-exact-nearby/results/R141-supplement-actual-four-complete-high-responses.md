# R141 补篇：同一完整头源的四项真实高频响应

2026-11-20，维护会话 `visible-exact-astra-ac637-20261120`。

## 1. 本条完成的目标

公开 run [44740105701/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44740105701)
首次完成 [四响应合同](../notes/2026-11-20-actual-GH-saved-response-contract.md)
所列全部四个新标量。它只消费已经完成的五源率和 base0/negative-one
完整高图，没有再次计算高逆、源率、低逆、旧原50条、frame 或 candidate。

本篇的高逆是 [完整真实高源窗合同](R141-supplement-actual-GH-source-window-and-return-contract.md)
中的实际 `G_H`；它不是有限 WJK 候选 `F`。低头源使用 ordinary
`dr`、归一化全角 `L²` 和原 `S⁻¹` 一次；高端所有独立外部荷
仅在本条 homogeneous-head 响应中置零，原七输入端口资格仍保留。

## 2. 完整保存的四个球

下表逐字抄录实际输出。每个球保存完整有向 upper 的包含，后继须读取
原 JSON 的完整球，不能用表后的短显示数替换。

| 输出 | 完整75位保存球 |
|---|---|
| `H_B`：完整头源到高频 raw `L²` | `[109.795137421809240071470725729503091493438470452088141208578353083359388733 +/- 3.04e-73]` |
| `H_Z`：完整头源到 body `Z` sup | `[43.6219284598765518526893299643118795448866814298486806578171546233662373995 +/- 6.74e-76]` |
| `H_root`：完整头源到 root outgoing `Z` | `[43.6219284598765518526893299643118795448866814298486806578171546233662373995 +/- 6.74e-76]` |
| `t_X`：完整头源到 outer even `H^(-5/6)` | `[0.562138253348924637276924355210204633310395379250627328064654054424822646901 +/- 2.19e-76]` |

因此可直接采用较松的有理界

\[
H_B<110,\qquad H_Z<44,\qquad H_{\rm root}<44,\qquad
t_X<563/1000.
\]

这些是完整响应的**上界**，不是实际最优范数或范数下界。它们本身
既不证明内部反馈收缩，也不证明该算子奇异。

设五源旧球给 `b_c=b_{c,c}+b_{Δ,c}`、
`b_b=b_{c,b}+b_{Δ,b}`。前三项分别为原 whole 七列输出行的 ordinary
collar/body 两列与这两个完整源率组成的

\[
\sqrt{(C_{q,c}b_c)^2+(C_{q,b}b_b)^2}.
\]

平方和来自源的两个 pointwise 输入窗正交性；不是对 WJK 的非局部
残差输出分窗后擅用正交性。外端迹使用**已经保存并读回的第二球**
乘 `5/388`。该因子来自真实高 frame 与最小高物理频率388，
没有对任意体 `L²` 函数取端点。旧第五源 `ΔB_LH` 的 raw 球整条保留，
本条没有把它当作已计算的低接收器。

## 3. 原件、执行和完整审计

入口 commit：
`b5f4e20704d4c61f081b2de607284d98c41a6d04`。
实际数值 checkout：
`2d5a06cf26fb59042a4e3851c5b49e96893ee9b9`。
唯一 child 返回0；数学 wall `0.0675970570000004` 秒，
child wall `0.12301476800000444` 秒。

| 完整原件 | bytes | SHA256 |
|---|---:|---|
| [实际四响应](../notes/actual_GH_saved_response_ci/run-44740105701-1/actual-GH-head-response.json) | 7209 | `1fd66504308e993d443f465290f31bbdea46434b3f9afd40312c3571a407c22c` |
| [完整执行回执](../notes/actual_GH_saved_response_ci/run-44740105701-1/execution.json) | 10580 | `a8df491cf4e3e7292343de4be10e38f481faa8db9d8a4c50658b74d116a8f8b3` |
| [执行说明](../notes/actual_GH_saved_response_ci/run-44740105701-1/report.md) | 638 | `f2c9e742b0454e9e04e107a805602e7107112660a320c4d48a10012abdc6e881` |
| [完整输入清单](../notes/2026-11-20-actual-GH-saved-response-inputs.json) | 7546 | `87e75f8e001601fa8ed6279d7b3e0735799a336a31b4e39b0bac9b0f2194bc35` |

数值源16888B/SHA `8ea2a23eb58a3c8b0fce510288dde2f5871f5f813db1934b0df2ed63e0d7e72c`；
worker27356B/SHA `cc49d939dd33e5ca1964d37d5bdbb691591000f48733553a3efc247fe2ec179d`。
运行使用 Python3.12.14、python-flint0.9.0、320 bits、75位球。

维护会话逐一核对16个 current 原件的 bytes/SHA256/Git blob，执行中的
整条 receipt 列表与 manifest 完全相同。实际21个顶层字段、完整四目标
和四球、同一 original WVC reference chain、完整 old scope 与 source
identity 已整读；完整 actual hash 与执行 `scientific_files` 相同。
原五源 actual/exec/manifest、base0/negative 的四份 whole summary/process
均以整对象保留，未只择取成功 flag。

5次实际 pull 的摘要链和所保留的首条/末三条完整 README 回执均保在
execution，四条完整 diff 皆空。没有恢复历史 native；没有旧科学 target、
新数组、Artifact 或 Release。本条已经实际发表，四项全部冻结，不重算。

## 4. 未付接口不变

完整内部低高反馈还需要低 Green 的正确 source/receiver 和实际 body
收缩；真实 physical `97+96` 外方块、全部七独立高端口及 mean/affine
行还需各自闭合。WJK `CFB`、原 finite-`ρ` 桥、两个原 RHS、
负侧/腰匹配和全族非线性构造未由本条获得。固定度量、同一连通闭曲面、
held/reach/marker 与可见振幅的总完成标准仍未达到。
