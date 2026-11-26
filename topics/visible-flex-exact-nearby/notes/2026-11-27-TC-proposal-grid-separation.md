# TC：浮点 proposal 节点与精确积分分割分离

日期：2026-11-27；会话：`visible-exact-astra-fb31ed6-20261127`。

**实际失败已定位；实现修复已证明保持全部积分分割。新 TC 数学目标仍待实际执行。**

## 1. 原完整失败，不改写旧结果

公开 run `45884668422/1`、job `140132276212` 使用原 immutable Python 容器，
已经恢复 137 当前输入、18 原历史文件、40 全 native rows，原完整 cubic
`3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402`
与全部14个原方向分片 SHA 均通过。必要 Hermite 输入恢复用时
24.26656646299999 s；旧 nodal QR、旧 residual/norm 目标均为零。

首次真正 TC child 于 `2026-11-26T19:36:21.374601+00:00` 启动，
`19:37:16.579043+00:00` 返回1。完整科学状态仍为 `proposal=null`，
`completed_targets=[]`，matrix/negative/positive/prefix receipts 全为 null。
断言在 `choose_all_columns` 入口、任何 QR 数组分配之前：

```
ValueError: complete declared proposal grid with one internal root node
```

原失败状态：
`notes/true_root_trial_residual_ci/run-45884668422-1/actual-trial-state.json`，
7347 B，SHA256
`cacd588e662508693e36b9ffa45fe3afd33cecbb355642d66e3014e93a1541d1`。
同目录整个 `execution.json` 和 `report.md` 保留，原 manifest
`2026-11-27-true-root-trial-original-runtime-mounted-inputs.json` 不改。

## 2. 原断言为何失败

旧 `complete_plan` 对原 common-row 有理端点、原 binary64 cubic knots 及固定
窗口/控制端点取 **精确有理并集**，之后逐点转 binary64 给 proposal。
精确有理数严格递增不能推出其 binary64 图像严格递增：不同有理数可能有相同图像。
前面的完整输入与端点断言已经给出首端0、末端25/8及唯一内部真根节点；因此本次
复合断言中缺失的性质就是浮点相邻长度严格正。把精确端点无区别地当成浮点步进
节点是实现错误，不是原 PDE 或原已证输入的失败。

## 3. 两个分割各司其职

修复只对 **proposal 节点** 按相同 binary64 图像分组。每组保一个精确有理代表：
优先保0、25/8、3、1/20、9/50和正负源窗口边界等必须节点；没有必须节点时取
该组最小的精确有理数。不同必须节点不得有相同 binary64 图像。真根仍是唯一符号
节点 `true_root`，数值 proposal 仍只使用原隔离区间内明确 dyadic 点。
选择后直接核每个 proposal 浮点步长严格正。

**certificate 积分分割保全部原精确切点。** 对每个 trial 段与每个原 common row
的交集，再按原全体精确有理切点细分，包括从 proposal 删除的那些切点。
因此任意原 row、背景 cubic piece、metric seam、源窗口边界仍是积分分割边界。
没有把窄区间的径向质量改成零，没有删行、合并输入球或跨不同原 coefficient
piece 使用一个多项式。每个非空精确区间仍以原 `dr` 质量进入全部96列及对应全部源。

证明如下。设原切点集为 $C$，新 trial 节点集为 $T\subset C\cup\{r_*\}$。
任取一个新 trial 段 $I$ 和一个原 common row $J$。实现保存
$(I\cap J)$ 内全部 $C$ 的切点，并逐个相邻端点生成子区间；它们的内部互不相交，
并集恰为 $I\cap J$。再对全部 $I,J$ 求和，得到与原完整径向域相同的覆盖。
原 root 隔离带仍按 TC 原上下界作两侧保守覆盖，不以浮点根替换。对 trial 节点的
coalescing 只改变尚未完成的有限 dyadic trial 选择，不改变 PDE、窗口、均值、
角支集、原输入球、旧已完成目标或 TC 完整 residual 公式。

计数门仍为 `maximum_certificate_cells=9000`，理由不依赖新科学计算。原
`fourfold_codazzi_mean_completed_head_body_residual_v3.py` 的 `prepare` 对
`tn + nodes + response.nodes + adjoint.nodes` 及两个 CONTROL 端点先作精确并集
再细分；`identity` 还逐行要求整段位于同一个原 background/response/adjoint piece。
因此原7721 common rows 的端点集已经包含全部 base binary64 knots。新增加给
certificate 的 `cuts` 在根隔离带内部只能是原 row 端点；它们本来已经由
逐 row 交集切开，根内不会增加新子格。其余额外切点0、25/8、3、CONTROL、正负
窗口边界均在根隔离带外，原 `exact_fixed` 已全部包含。故新旧 certificate 的
精确积分小区间相同，只改变各小区间归属的 trial-piece 编号，计数不增加。
旧 run 在 `choose_all_columns` 之前已经通过 `len(plan)<=9000` 的门；这个实际事实
和上述原 source partition 恒等足够保留9000上限。新 owner 仍在任何 proposal
算术前重新执行相同门，并记录实际小区间/节点/合并数。

每个新 trial 段仍由 TC.7 的同一七次 Hermite 定义，左右引用同一保存的节点值；
真根 even96 为精确恒等，两侧 full193 根值相同。TC.10 cutoff 及所有 ordinary、
mean、high、outer、jump 条件照旧。完整 residual 后续必须实际包围新 trial；
proposal 品质和其收敛性不预先假定。

## 4. 本次具体入口

源码仅改变 `fourfold_codazzi_true_root_trial_inputs.py` 的 grid/plan 选择；owner
更新该完整源 SHA，加入明确 policy 与小型 mesh audit。原
`fourfold_codazzi_true_root_trial_proposal.py` 的 CF4、QR、193维算子、三阶 derivative
选择、原 directed residual math 均保持原字节。

metadata-only generator 已生成：

- manifest：`notes/2026-11-27-true-root-trial-separated-grid-inputs.json`，
  81747 B，SHA256 `c5fd0a7a8cd7c6a1a2207e7b640a213ea8dd2ed8bb967107cff969501ed5d447`；
- workflow：`.github/workflows/fourfold-codazzi-true-root-trials-separated-grid-public.yml`，
  2418 B，SHA256 `2b9e63f40067744792f672983e4a6a17c2e7706fc81d71d79bd9df63e966ba44`。

本地只做源码 AST、完整 bytes/SHA、manifest 与原规则 metadata 检查；没有执行
科学计算。上一 run 没有完整新科学对象可继承，故本次仍需首次完成三原自然目标。
原 nodal 输入只作已获准必要重物化并继续核原全 SHA；不重跑旧 QR 或旧 scalar/norm。
后继 SC/JF 仍必须等 TC三目标、完整 P224 链、RW96及 actual JC7 全部到齐。
