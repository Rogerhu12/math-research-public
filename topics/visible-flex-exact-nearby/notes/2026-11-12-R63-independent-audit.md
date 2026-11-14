# R63 独立审计：固定 H 的局部逆与端点转换

2026-11-12，constructive_route。完整阅读 R63 正文及
`scripts/fourfold_circle_local_inverse_budget.py`，并以独立源码重算其有限整数输入。

## 数学核查

在 Wiener 闭球中，有限 H 的 Fourier 复合给
`||N(u)|| ≤ B_H ||u||²/2` 与 Lipschitz 常数 `B_H r`。
因此原文的球自映射半径、收缩率、`1−κ/2` 解界和偏移后逆导数的
Neumann 界都成立。这里无须额外预设全复带单叶性；实圆上 H 的全局保向性
及 F 的保向性选出准确的预共轭分支。参数变化时固定 H 的要求不可省略。

对两条复边界作 Parseval，权重确为 `cosh(2kS)`。常数模贡献 1，
正负每对非零模至多贡献 `4 exp(−2(S−s)k)`，所以
`sqrt(2 coth(S−s)−1)` 保留了常数、负模及全部无限尾。
物理角到归一化角的端点误差系数确为 4。
有限弧只有在两条完整边界被无缺口覆盖后才可以按弧长作平方平均。

## 有限预算独立重算

新源 `scripts/fourfold_circle_local_inverse_independent_audit.py` 不导入原预算源。
它从两个 dyadic H/q 文件重新形成有正负频率的整数数组，独立作完整卷积
`H' q−1`，记录准确整数结果的 SHA256，并以 256-bit Arb 重新求模和。
它将重算值与原报告的准确 dyadic 端点比较，而非比较十进制显示值：

- 两个 `||H'q−1||`、q 范数、逆导数、扩大复带上的二阶导数、κ 及偏移逆界，
  均严格小于原报告各自的有向上界。
- 原报告可容许 E 的数值严格小于独立重算的 `r/(2R)`，方向正确。
- H'(0) 的准确 Fraction 与原报告完全一致且为正。
- 3 个新 Hardy 因子与原逐系数因子，都落在原报告保存的准确 dyadic 区间内。

运行入口（课题目录）：

    PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_circle_local_inverse_independent_audit.py --budget notes/2026-11-12-R63-finite-local-inverse-budget.json --out notes/2026-11-12-R63-finite-local-inverse-independent-audit.json

完整报告保存每个检查布尔值、输入哈希、独立整数卷积哈希和显示值。
两个 H 的 κ 约为 0.05756948325225034、0.057574402646343815；
允许的实际 E 门约为 0.00014204041677143495、0.00014204503804858876。
这些是有限 H 的门，没有将尚未认证的真实返回残差填入门中。

本次审计未发现数学或有向计算错误。实际全时间复残差、完整参数导数、KAM
横截与迭代条件，以及原课题的精确等距族，仍须分别完成。
