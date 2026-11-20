# R139 实际结果：均值atom必要门完成，未排除固定配方

2026-11-20，visible-exact-astra-ac637-20261120。

**实际新目标已完整完成；判定为未证明排除。** 公共
[44721682192/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44721682192)
成功完成 [mean atom必要门](R139-supplement-mean-atom-lower-budget-for-fixed-comparison.md)
的三个独立下界记录。保存的乘积下界没有达到准确阈值
$1/16384$，所以本次不能排除原W2C比较配方；这不是原充分门
已经通过，也不是实际算子可逆的结论。

## 1. 原始记录与准确含义

令 $h_k,a_k$ 是原配方实际取用的完整有向上端数，
$S=\sum_kh_ka_k$、$M=\max_ka_k$。原完整193观测中的mean行给
$L^2\ge SM$。此次只保存 $S_\ell\le S$、$M_\ell\le M$ 及
$P_\ell\le S_\ell M_\ell\le SM$。以下是完整原记录球；使用时取下端。

```text
S_lower = [1.01807173933890169193496019283180503648800692933785419733657430270880747467e-5 +/- 3.21e-80]
M_lower = [5.17657379645405748404304329761182308283076458945679772999744139034416956634e-5 +/- 1.49e-80]
P_lower = [5.27012348877216395443012616094611082334696919121038149058446273957135493070e-10 +/- 3.34e-85]
```

原结果的 `saved_product_lower_at_least_threshold` 与
`fixed_recipe_rejection_proved` 均为 `false`，
`outcome=necessary_atom_rejection_not_proved`。
此处没有从下界未达阈值反推真实 $SM$ 的上界。

三个记录依次原子保存并读回；第三条使用前两条读回下端。
源代码及根/独立代理均核过该方向，未把上界越阈值当作必要门的证明。

## 2. 同对象、完整范围与公开回执

完整科学页为
[actual-scientific-conclusion.json](../notes/low_family_atom_floor_ci/run-44721682192-1/actual-scientific-conclusion.json)，
87510 bytes，SHA256
`c51d21c18ebad81b7966590a38aa00b04b9602a9687f3dddb45bb15f495871da`。
执行页为
[execution.json](../notes/low_family_atom_floor_ci/run-44721682192-1/execution.json)，
54394 bytes，SHA256
`0270e1f67c700372dfbb1d29ef6c5974ad335a15093ba3ee3c3e266e1da3aa70`。
[report.md](../notes/low_family_atom_floor_ci/run-44721682192-1/report.md)
527 bytes，SHA256
`1de92d44616ae171ee0360a7d7d879d9bf1e242226619fea2095e3afefa3fa81`。

输入清单 SHA256 为
`d2ba289f34561793a6315cf643d30b2f27f2e04a00445d8cec6d33583227552e`。
根已将全部70份完整当前receipt及7份科学模块身份与该清单逐项比较，
全部源文件的bytes/SHA再次相符；完整输出schema、27个有序通过门、
原 `retained_scope` 也逐项吻合。执行页记录25份AST、21原件恢复、
4次README检查及单一科学child成功，所有pull均符合已读规则。

本次完整材料化同一153个reference/centre parent、155个比较panel，
保全部4650原row/4801闭交、完整mean、29原同算子记录和两个原optical
记录。新数学墙钟为60.901720220000016秒。
原producer调用、旧目标重算、新数组、artifact、Release均为0。

## 3. 完成项与仍未完成的项

此次完成的唯一新目标为
`complete_low_family_mean_atom_necessary_floor`，新记录数准确为3。
这些记录现冻结并只读复用。

原五图50个新scalar的完成数仍为0；原完整低族比较的row/column/norm
三量也仍为0。两次失败 `44716804300/1`、`44719196440/1` 及其
0scalar回执保持原样。下一步接续已证明正pivot修复后的原三量，
不重新计算本篇的三个mean-atom记录。

同参数、同真实根的高反馈、完整signed centre、原finite/rho/端点
费用、两RHS、7ports、负侧及最终非线性闭合均未因此支付。
本篇只关闭这个独立必要性检验，课题总验收仍未完成。
