# SC/JF：完整实际真列与两个完整 signed96 矩阵的后继入口

日期：2026-11-27；会话：`visible-exact-astra-fb31ed6-20261127`。

**已完成：执行定义、完整 metadata 准入与保存/回读路径。尚未执行：三个新 SC
数学目标。** 当前 TC 与真实正逆链尚未完整，故没有生成本目标的实际 manifest、
workflow 或假设成功的数组。数学依据是已证
[JF联合矩阵界](../results/R149-supplement-joint-signed-finite-matrix-error.md)及
[JC联合composition界](../results/R149-supplement-joint-compound-waist-row-error.md)。

## 1. 必须完整消费的实际前件

入口需要同一 selected $Q_0+\delta Z$、同一 true root 的完整原始 low→58→224→32
物理正逆链、TC三个完整自然对象及其最终全 cell prefix、原 RW96、实际 JC7，
以及原 SP/PW/WTA/WX 左右接收器。两 physical density means 始终存在。

`fourfold_codazzi_signed_finite_actual_inputs.py` 抽出原
`positive_inverse_negative_receivers_owner.physical_pair` 的完整准入：
58/224/32 全 fields、target order、全部 scalar records、原 source hash、manifest、
run、execution receipts、同一 reference identity、两完整已通过正逆门、low/D/high
来源一致性全部保留。224项的14个输入端口、16个输出单位及 qualifications 全核，
32项 WPN 的 finite/tail 两整行及 exact lifting 条件全核。虽然当前 TC误差公式
只乘其中六项，这不允许以六个孤立球代替整个 P224 表及其已证前置逆。

TC准入消费 `actual-trial-state.json`、两96来源对象、完整signed trial矩阵对象、
全径向prefix、实际execution及原manifest；由原 TC owner 验每件原数学对象。
每个来源96列、全部五类源、原 root/outer/jump 零恒等、both means、全部原rows
及每个原 full hash 均保留。若存在合法原TC续接，已继承自然对象保持最初 producer
manifest，只通过完整原 manifest 链接消费；不能把成功对象漏掉后重算。

JC独立实际 run `45887337009/1` 已完成7球。完整实际文件
`notes/joint_compound_row_ci/run-45887337009-1/actual-joint-compound-waist-row-error.json`
为17976 B，SHA256
`fec83298af0f0bacfe907f9c445cc42f0ed165129cbea18a38cb5d0214ef336e`；
manifest SHA256
`516554f609356ddc801632b88605367df03edeaf0c32830d446bb1090a2a5cf5`。
本后继使用整个JC actual、execution和manifest，逐项验七个原ball、三个lower与
四个upper方向、全部附带结论、完整旧W记录、RW/family与source绑定。
最后联合row误差球由原actual直接消费，绝不再次执行JC目标，也不从旧scalar row
误差反推 $E_H$。本地已经对这份真实全JC和原WX20-gate执行metadata准入，
两者通过；没有导入NumPy/Flint/SciPy，没有做科学算术。

## 2. 三个新自然目标

1. `complete_true_PDE_waist_column_errors96`：全部96个真PDE腰列误差 $D_j$。
2. `complete_true_physical_primitive96_matrix_gate`：完整96×96 physical primitive
   矩阵的有符号真条目包围和充分逆门实际结果。
3. `complete_true_declared_incoming_cosine96_matrix_gate`：完整96×96 declared
   incoming cosine矩阵的有符号真条目包围和充分逆门实际结果。

每个目标独立保存完整小结论、原输入身份和私有完整载体的whole hash；保存后立即
读回，公开worker在目标出现后立即推送。一次实际结论包含true或false门结果，
不以足够门未通过推断真算子奇异。

令 $P_{k,o}$ 为完整P224中端口 $k$ 到输出 $o$ 的原上界。TC只在
$k=1,2,7$ 非零，分别对应完整 high collar、high body、raw low源。按JF：

$$
d_j=\sum_{k\in\{1,2,7\}}P_{k,\mathrm{low\ root97}}F_{k,j},\qquad
z_j=\sum_{k\in\{1,2,7\}}P_{k,\mathrm{high\ root\ mixed}}F_{k,j},
$$
$$
D_j=C_R\sqrt{d_j^2+z_j^2}+C_O F_{\mathrm{negative\ root},j}
                           +C_2 F_{\mathrm{negative\ strict},j}.
$$

完整原receiver已付其单位转换，不额外重复输出因子。真实目标行是归一目标Hilbert
空间中的 $g_i$；先应用完整左receiver，再用Bessel。不把旧角度中的compound行
或RW有限近似行当作正交行。

本首入口在原 TC 归一physical root-even96输入及真 $g_1,\ldots,g_{96}$ 输出
坐标上取 $D_s=D_t=I$。source与target各自保存一整份96个严格正权重，含义分开。
一般的 $D_s,D_t$ 公式仍由JF pure支持；本次不把原96方阵改称未齐的全Schur。

记 $v_j$ 为同一个TC trial腰列的全primitive+means范数。列误差项与row误差项为

$$
\Xi_A=\Gamma_A\Bigl(\sum_jD_j^2\Bigr)^{1/2}
       +\kappa_A E\Bigl(\sum_jv_j^2\Bigr)^{1/2},
$$

其中 $\Gamma_{\rm physical}=B_H/\sqrt2$、
$\Gamma_{\rm incoming}=B_HK_W$，而
$\kappa_{\rm physical}=1/\sqrt2$、$\kappa_{\rm incoming}=1$。
后一个等式只来自原 TC trial 支集严格低于原固定 $J_s$ 的合法恒等，不能删除
真列误差中的 $K_W$。先形成两个完整合法candidate：旧96 scalar-row误差的
Hilbert–Schmidt组合，及新actual JC的whole operator误差。两份整candidate分别
保存回读后取较小完整上界。没有逐entry拼接两个互不兼容的原逆证明。

## 3. 必要载体恢复与全signed门

`fourfold_codazzi_signed_finite_trial_carrier_restore.py` 只在全部前件已实际完整
后、公开Actions中调用。它重物化同一原TC `trial_value`：使用原proposal完整源码
中的value-producing AST前缀，所有CF4/QR/root identity/向腰传播语句原样保留，
仅略去值完成后不再修改value的三份derivative数组。完整原value SHA、shape、
字节数与原TC proposal receipt必须一致。必要TC QR重物化记为1；原R133 nodal
QR记为0，旧96 residual、waist-norm、matrix-norm及JC目标调用均为0。

随后同原TC方式恢复原RW整grid、96整rows、两个全部9216 signed条目载体，全部
按原完整bytes/SHA匹配；旧row误差、旧trial范数不重算。原nodal→Hermite→14Z
输入恢复继续使用原不可变Docker、原完整cubic及14分片SHA；该必要输入子进程
单独计数，保持原Hermite的 `OPENBLAS_CORETYPE` 未设置语义。TC值proposal恢复
仍为其原Haswell、单线程runtime。

所有true signed entry的区间也完整生成、保存、读回并记whole hash。各条目半径
可用 $\Gamma_A D_j+\kappa_A\min(\epsilon_i,E_{\rm JC})v_j$；operator norm界
只使用上一节完整 $\Xi_A$。entry carrier中的原pairing舍入误差与operator扰动
区分清楚，不重复付费，也不删掉前者。

完整trial midpoint方阵的Arb逆只用于选择一个exact dyadic矩阵 $B$。其全部9216
mantissa/exponent保存并精确读回后，才计算完整signed

$$
E_0=I-BD_t\widetilde M D_s^{-1},\qquad
\rho=\|E_0\|_2+\|BD_t\|_2\Xi_A.
$$

先完成signed矩阵乘法，再取全部行列绝对和得到2-norm上界。完整原范数list保存
回读后才计算扰动项；扰动项保存回读后才计算 $\rho$；以保存球的upper判
$\rho<1$。仅该严格门实际通过时，用保存的 $\|B\|_2$ 和保存的 $\rho$ 得

$$\| (D_t M D_s^{-1})^{-1}\|_2\le\frac{\|B\|_2}{1-\rho}.$$

该最后上界也保存回读。如果完整trial midpoint没有可得逆proposal，仍保存全部
真条目包围与明确 `inverse_proposal_unavailable`；不伪造逆或把没有proposal称
真算子奇异。若原完整sufficient gate未过，公开全部实际gate球并保false。

## 4. 具体使用与公开执行约束

五个源文件：

- `fourfold_codazzi_signed_finite_actual_inputs.py`：完整已完成前件metadata；
- `fourfold_codazzi_signed_finite_actual_owner.py`：三个新数学目标；
- `fourfold_codazzi_signed_finite_trial_carrier_restore.py`：原载体必要精确恢复；
- `make_signed_finite_actual_manifest.py`：只有完整前件时才生成实际入口；
- `fourfold_codazzi_signed_finite_actual_public_worker.py`：公开执行及即时保存推送。

当真实TC、WPN和JC结果全齐后，metadata-only命令形式为：

```bash
python topics/visible-flex-exact-nearby/scripts/make_signed_finite_actual_manifest.py \
  --repo . \
  --tc-result-dir topics/visible-flex-exact-nearby/notes/true_root_trial_residual_ci/run-ACTUAL-1 \
  --tc-manifest topics/visible-flex-exact-nearby/notes/ACTUAL-TC-inputs.json \
  --wpn-result-dir topics/visible-flex-exact-nearby/notes/ACTUAL-WPN/run-ACTUAL-1 \
  --wpn-manifest topics/visible-flex-exact-nearby/notes/ACTUAL-WPN-inputs.json
```

上面的ACTUAL只是文档中的待替换路径，不是已生成manifest中的占位内容。
JC默认取真实run45887337009/1及其完整manifest；gate/ports全部真实路径由whole
WPN actual内部原specs直接导出，不能任选不同链。缺失/不完整/failed/未过正逆门
都只返回readiness，不生成科学manifest或workflow。

worker先metadata全验，再恢复原TC manifest的全小输入闭包（首launch137件）及全部原native；原TC闭包
从其真实完成checkout恢复，避免较新的源码覆盖旧carrier定义。全原TC preflight
继续验7721rows/40parts以及完整RW/NW，之后才发布consumed并启动一次new science。
每30分钟pull并读两README差异；非快进拒绝立即rebase再推，直到真正成功。
容量核算采用已经公开的origin tree加完整本地Git delta，绝不查询尚未推送的
local tree的REST对象。新数组仅在runner临时目录，不入仓库、Artifact或Release。

所有private source都保原完整topic相对路径及 `fourfold_...py` basename，而非把
role名写成 `math.py`、`json.py` 等裸文件。owner在该原script目录运行；没有
role snapshot遮蔽标准库的入口。文件路径与原全hash共同核定。

该96方阵即使通过，也没有包含两physical mean独立matching行、完整nu/phase列、
high消元后的全cross块。它只完成所声明真96方阵；完整incoming Schur及最终
闭曲面精确族仍须另行完成，所有result始终保相应false scope。
