# 完整 β 与复角图表的独立复核

2026-11-12，root 审核。此记录把源码证明审核和独立数值加总分开；
没有把固定原图的结论转给 δ₂、δ₃ 或未确定的参数 KAM 小盒。

## 原始对称图完整 β

完整通读 `fourfold_phase_beta_bulk_interval.py`、
`fourfold_phase_beta_bulk_box.py`、`fourfold_phase_beta_combine.py`，
结合已审核的 native collar 源，确认以下实际步骤。

- 原始 binary knots 转准确 Fraction；用准确中点选择同一多项式 germ，
  不舍弃仅相差极小二进制距离的非空区间。三阶 jet 从完整标量多项式
  得到；Horner 更新分别为 δJ₀+c、δJ₁+J₀、δJ₂+2J₁、δJ₃+3J₂。
- Box 的复四则及所有 FFT 蝶形向外计算。有限原函数和径向三 jet
  的误差先分别支付，再进入 Parseval 的 E、E′、E″ 乘积。
  E″ 的费用包含两个 Fᵣᵣ² 项及 FᵣFᵣᵣᵣ 的全部交叉尾。
- Fθ=aT、Fᵣθ=a′T+aTᵣ、Fθθ=aTθ 使用真实有限相位恒等式；
  复点乘是双线性的。正、负频率相乘计算 E，不在复 r 处取共轭。
- 对每个实径向区间，角覆盖同时支付相邻节点实间隙和复 strip；
  梯形余项统一乘准确径向长度。半角节点权重由真实反射偶性恢复全角。
- Arb 的复积分 callback 在完整输入复盒上检查实际分母及平方根支；
  被拒绝的盒返回非有限值并由积分器细分，没有作为通过证据使用。
- 腰部 Q=Fz/r 与 Fθz/r 各用径向导数积分表示。整个小段上各导数
  的区间包含其积分平均值，故平均值之商被所用正分母商界包含；
  并未把这一平均恒等式错误地写成某一点的导数商恒等式。
- 密度与 R50 的完整 ground-state 口径一致；展开根附近的
  fᵣ=−1/(2ρ)−Lρ 后得到已审核 collar 的 A/B/C 符号。

另用不导入合并器的独立 flat-cover 检查：直接合并三个完成分片的
259 个被接受子区间，按准确 Fraction 排序；用 bisect 对照原输入
重新生成的 167 个 knot span，检查每个子段所属 span、首尾、正长度、
相邻端点准确相等和最终切口。所有失败叶片列表为空。

采用 Arb 224 bits，将每行保存的 lower、upper 端点球分别求和，
而非读取缩短后的显示中心或再次构造较宽 union。结果保存于
[独立覆盖与端点求和](2026-11-12-beta-independent-cover-sum-audit.json)。
这一独立求和给更紧的安全端点，因而确认原先公布的严格界

\[
36.79967508215<\beta<36.80349990665.
\]

同一计算给 52<S=2√5β/π<53，所以 Q=53 为最近的奇整数；
所有 Q≤51 距离大于 1，Q≥55 距离大于 2。这独立确认
dist(S,2Z+1)>.60929435491 和 β 危险格距离>.42801799599。
原始输入仍为 bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532。

完整证明、输入和运行命令见
[原始对称图完整有向 β](2026-11-12-symmetric-complete-directed-beta.md)。
没有因求和核验而重复耗时的完整 bulk 积分；解析性、连续范围和尾界
由上述源码审核及其冻结域门承担。

## 准确仿射族整核心复角图表

完整通读 `fourfold_phase_affine_complex_chart.py` 及其证明。
独立检查 Qθ、Qθθ 的腰部延拓，双线性 Sθθ 的恒等式，以及

\[
J_{\theta\theta}=-n+aF\cdot
(T_{\theta\theta}\times X+a'T_\theta\times T
 +2aT_\theta\times T_r+aT\times T_{r\theta}).
\]

其中 −n 的符号来自 T·(Tθ×X)=−Tθ·(T×X)。复向量叉积的
Hermitian 范数估计可由二阶外积恒等式证明，不需要假设向量为实。
对实轴取实值的解析标量，一阶竖直项纯虚，二阶竖直 Taylor
费用确为 σ²M₂/2。实域 support² 是 S 的有效下界。

源码明确要求三份输入的 origin/direction/参数范围一致，检查
准确径向闭覆盖，重新计算逐模式 phase hull 并与 scalar 证书匹配。
Gθθ 从较大的 R59 独立控制盒导入，只加强覆盖，不把更大的盒
错误当作已证明准确仿射 support 的对象。

因此同意该证书对实 |r|≤binary64(.24)、实 |δ|≤binary64(.01)、
物理 |Imθ|≤1/64 的四个右半平面结论及周期 Log/平方根分支。
该证书 source SHA 为
0f0f27282edc5ef4baf29c3abfb3d67264216495d6e0821872a8da26e9f3cfde，
输出 SHA 为
a1bfb82ee751e31a51a9997804ca2da68aaa4eb76b63081f1e4c0f9806e68a8f。
它没有径向复化、ODE 流或参数 KAM 成功的含义。
