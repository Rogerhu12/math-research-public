# 新首块 dense reference 正权与 H 初值的实现核读

2026-11-12，constructive-route。已全文核读重建源
`scripts/fourfold_dense_reference_weights.py`，SHA256
`5be66a7907bf826f600440e674158e9c7ac9d007d26dd4000202916ad79924ee`。
下面仅核对有限参考函数的证书，不给真实 ODE 或 Jacobian 背书。

源先以 Fraction 展开 DOP853 nested formula，再作准确的
$z=z_0+\lambda u$ 仿射代换，将实际时间段映到 $u\in[0,1]$。
它保留保存 h 与准确时间差之间可能存在的差别；不依赖 h 的浮点
减法恰好准确。幂系数到 Bernstein 系数的转换
$$
b_k=\sum_{j=0}^k a_j\binom{k}{j}/\binom{n}{j}
$$
及非负基分割统一性给出全段范围。对 $L_\tau$ 再除准确有符号
时间差，所以逆向积分段也得到正确导数范围。

程序用 Arb 有向指数把准确有理端点送到 $q=\exp L>0$ 的区间，
再向外转换成 binary64。它只利用定义上的 $q_\tau/q=L_\tau$，
没有将 q 认成真实 Jacobian。准确网格 $2\pi j/258$ 与整数除
$2^{80}$ 的 H 系数也在 Arb 中重算，随后减保存 dyadic 初始角。

当前实际报告
`data/phase_ring_continuation/exact_affine_step2_dense258/block_0000_forward_reference_weights.json.gz`
SHA256 `77f7610c2eb0982a0ff35ae74add7404dfc9afe5b3bb49d0059c6c99b8c5b7aa`，
已核对其 trace SHA 为新 `60b0cc65...`，共 141 段、43 条射线，
H SHA 为 `58375d24a99ba0f43b29143fe22f950a6e74e4fec2b94123d68b078fcf088260`。
这份新输出给参考正权范围
$[.5486437202169419,3.700265227131817]$，最大 H 初值误差上界
$3.897834852526276\times10^{-17}$。

本块没有拆成中途开始的 trace chunk。未来若
`first_accepted_segment>0`，其保存初值一般是中途射线值，不能仍称
H 网格初值；应跳过该初值比较或从上一个段末端误差继续传播。
目前全段正权、真实 ODE 残差、角复管和参数二阶传播仍是不同的
输入，不能只凭正权证书宣布 R60 或共轭方程已经闭合。
