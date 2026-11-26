# R142：已成 Green 前缀的准确接续与全母格矩积分

2026-11-26，visible-exact-astra-198c63d15049。

**状态：已证明的接续与积分算法；本篇没有新的 defect 数值，也未证明完整精确闭族。**

## 1. 原运行已经结束，实际完成范围不能扩写

公开运行 [44730452579/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44730452579)
的保存输出位于 `notes/low193_verified_green_ci/run-44730452579-1/`。
完整 `actual-scientific-conclusion.json` 为 51911 字节，SHA-256
`870ff37ab18ee7218d74f62a2c9b5f6c9f309322090742699559125e206716e7`；
完整 `execution.json` 为 59281 字节，SHA-256
`80907dfc24a85802f34267ed680303b001fccba729b1eca5e116f428717b66a1`。

两文件一致记录：唯一已成目标是
`complete_exact_low193_comparison_Green`。155 个 comparison panels、
1424 个 refined cells、1425 个完整节点、root97 与 outer96、193 个独立观察
全部属于该已成 Green。原模型链为
`33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79`。

后续 `complete_true_hybrid_low_coefficient_defect` 仅完成 675/1424 个 source
packets，随后触发 16800 秒的固定 wall cap；保存时数学时长
16807.150517695998 秒、进程 return code 1。完整 `defect` 和严格门均为 `null`，
四源为空，完整科学输出 `complete=false, proved=false`。内存峰记录为
3993616384 字节，未触发内存限额。

因此原运行给出了完整 comparison Green，**没有给出完整缺陷上界**。
它既不是已经得到 $\epsilon\ge1$ 的完整充分门失败，也不是对实际算子的
奇异性结论。675 个私有 packets 不构成一个完整范数，不能作为零余项补齐。

## 2. 新计算对象与不变的实际方程

记原 hybrid 低算子为 $A_L^c(r)$，比较方程在 parent $p$ 上为
$x_t=H_p x$，实际长度为 $h_p$，原范数权为 $S_p$。对象与 R141 完全相同：
$A_L^c$ 的主部仍含全族 $\eta_\delta$，低阶项来自同一个 repaired centre，
独立 even mean、ordinary $dr$、root97、outer96 与所有参数窗口保留。
新目标仅换用已证 GM/GI 的完整矩积分包围计算

$$
W_\Delta(r)=(A_L^c(r)-H_p/h_p)S_p^{-1},\qquad
\epsilon=\|S\mathcal G W_\Delta\|_{L^2\to L^2}.
\tag{R142.1}
$$

这里 $h_p$ 是真正长度；若 parent 分成 $n_p$ 个 cell，则
$(H_p/n_p)/(h_p/n_p)=H_p/h_p$。不把 root 区间中点当成真实根。

原完整 parent source ball $\mathbb W_p$ 包围该 parent 上的每一个
$W_\Delta(r)$。依 GM.15 取准确中心 $W_0$ 和 entrywise 非负半径上界 $R$，令

$$
\overline V_p=W_0W_0^T+
\operatorname{diag}\bigl((|W_0|R^T+R|W_0|^T+RR^T)\mathbf1\bigr).
\tag{R142.2}
$$

对于每个 $r$、每个原允许参数及任意实向量 $z$，展开 covariance 差，
逐项用 $2|z_i z_j|\le z_i^2+z_j^2$，得到
$z^TW_\Delta(r)W_\Delta(r)^Tz\le z^T\overline V_pz$。
故这是逐点 PSD majorant；并未把 varying source 冒充为恒定矩阵。

## 3. 共享 parent 矩与完整 signed 两三角

同 parent 的 refined cells 有同一 $H=H_p/n_p$、真实 $S_p$ 和
$\overline V_p$。所以 GM.3 的 $U,Z,Y$ 完全相同，可以只作一次完整有向
Taylor/doubling 求值，再逐 cell 代入各自准确 carrier
$L_i,R_i,\ell_i,\rho_i$。没有把不同节点 carrier 混用。

每个 cell 使用 GM.4 的四个完整 Grams 以及

$$
T_{L,i}+T_{R,i}
=h_i^2\left\{\operatorname{tr}(P_i^TU P_iZ)
+\operatorname{tr}Y-2\operatorname{tr}(P_i^TY)\right\},\qquad P_i=L_i\ell_i.
\tag{R142.3}
$$

GM.2 的准确核平方在源 covariance 上是正线性的。先用 (R142.2)
支配准确核平方，再用 (R142.3) 展开，保留所有 signed 抵消；不能把式中
三个有符号项各自作不成立的 Loewner 比较。
两个真实三角、identity jump、mean 和所有 $h_i,h_i^2$ 都保留。

原离格递推的 $A,B,K$ 仅依赖 comparison Green、输出权与完整原 atoms，
与 source role 无关。按 GM.16 将它们计算并定向保存一次，缺陷 batch 和
成功后四源 batch 复用；$J$ 与右协方差保原高精度流，各 batch 一次。
这是真正相同数学对象的复用，不是删去一条误差费用。

完整平方上界由 GM.17 给出。逐 cell 的包围都覆盖原准确对象，有向相加和
开方给出 (R142.1) 的全域 upper。算法在每个保存的 matrix entry 上沿用
原 Arb 外包保证；不把 binary64 midpoint 当成准确 Gram。
最后将完整 defect scalar 保存、读回其整个 decimal ball，使用读回 upper
判定 $\epsilon<1$。

若严格门不成立，本次有一个完整新目标，保留完整 upper 而不授逆。
若严格门成立，原 R141 Neumann 恒等式给同一真实 hybrid 低逆，再计算
ordinary raw、transformed、second-kind correction、high0 return 四个完整源，
每个含 root97、outer96、完整径向域。最后才作原全部 whole-point boxes 的
transversality 估计。该六目标顺序不改变 full CFB、真实 physical 外块、
原 finite-$\rho$ 桥、七端口、两 RHS 和最终非线性 matching 的独立义务。

## 4. 必要内部物化与完成计数

原 Green 的 2525206400 字节私有载体未写文件、未公开；不能声称恢复了
这些字节。新 moment target 需要其内部表示，故从同一准入数据必要地
重新物化准确模型及其 carriers，核模型链、1424 counts 与已成前缀一致。
该内部工作如实记录，不登记第二个 Green 结论，不重做旧 endpoint QR/SVD
或 centre-floor、WVC/W2C 已成 norm targets。

新 `completed_targets` 从缺陷开始，只允许一目标完整 false 分支或六目标
完整通过分支。原完整 Green 及原 wall-cap 失败的两份 whole 文件作为
`completed_prior_directed_prefix` 引用；既不改旧文件，也不升级旧 flags。
任何新异常仍只保实际完成的 scalar prefix。

## 5. 可执行接续及运行成本的精确范围

新 owner 是
`fourfold_codazzi_low_centre_moment_continuation_owner.py`，显式导入已有
`fourfold_codazzi_low_centre_exact_cell_moments.py` 与
`fourfold_codazzi_low_centre_parent_moment_provider.py`。
原三个 Green/refinement/point modules 不改。模板 degree24，原精度768bits，
同一153 coefficient parents、155 comparison panels、1424 refined cells。

缺陷 pass 的非恒定 covariance moments 现在每 parent 一次，即155次；
原失败方法为每 refined cell 的4个 whole boxes。所有1424个独立节点仍逐个
支付，四源和 point 仍完整。A/B/K 从五次改为一次，J/right 从五次改为
缺陷与四源共两次。这些是代码结构的计数，**不是运行时或收缩通过的保证**。

这个后继没有缩窄 parent 系数球。若完整 parent-moment 门仍不成立，下一
明确的新对象是已证 CC 的 genuine-child 系数包围及 child moment cache；
不能反复重跑同一个完整 parent upper 来寻找有利结果。

引用：本题 R141 原定理、GM.1–17、GI 全篇及 CC.1–16，均为已登记本仓库
证明。此处只接续原未完成的低逆目标；精确闭曲面族的总完成标准保持不变。
