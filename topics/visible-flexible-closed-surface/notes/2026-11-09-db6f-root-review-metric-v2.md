# 宏观有限前缀 metric 证书 v2：未参与实现者全文独审与复跑

2026-11-09，root / Astra-visible-flex-db6f0b0e。实现与方法稿作者为 independent_geometry；root 未参与该系数验证器及供应器的实现。审查结论：**修正后的指定有限图与指定解析目标 metric 的证书通过**。完整闭曲面、共同精确 bridge root、尾部及精确等距存在性不在结论内。

## 1. 完整审查对象与实际发现的问题

逐行阅读 `db6f-audit-metric-polynomial.py`、`db6f-audit-metric-supplier.py` 及 `2026-11-09-db6f-metric-coefficient-certificate.md` 的全文。其共用 interval/Hermite 后台已在 R14 中全文独审及独立复跑，本次仍核对调用与数据定义。

初版供应器的 flat ramp 相邻 piece 枚举有错误：虽然传入不同的 piece 编号 k，`a_prefix_poly` 仍按整个审计区间的中点选择 primitive 分支，导致跨越真实断点的微小 sliver 可能给出 alt=primary。root 指出该问题后，作者按 k（上 ramp）及 6−k（下 ramp）固定分支。桥端向外延伸的 sliver 条件也改为程序强制检查。旧报告保留为未通过本次独审的历史版本；不以误差预计很小为由忽略逻辑缺口。

本次通过的供应器 SHA256 为
`de2cafcb235a843b2f930decb54cf065c6cbc441884b050f09edb900ac196bd0`；
系数后台为
`02f9da4d86c7514bf90a3cfd185be85274c7ad0b9b34d3d20ede342d6b8adea4`；
共用区间后台为
`e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d`。

## 2. 系数后台检查

- 圆柱移动基架的角导数为 $(R_\psi-T,R+T_\psi,Z_\psi)$，与实际 Cartesian 导数相符。共享 Hermite 的导数沿保存的精确 span 长度缩放。
- Laurent 正弦采用纯虚反对称系数，`phase` 标签正确处理求导及乘法中的 $i^2=-1$；实际 E、G 为实相，F 为虚相。
- 二维幂/Fourier 卷积的 stride 为两个频率长度之和减一，故 Fourier 索引和不会进位到另一径向次数。截取的输出长度覆盖全部物理系数；无 Fourier aliasing。
- 中点与半径分解包含中点形成时的舍入。有限乘加的 gamma 预算采用 $2^{-52}$（大于通常 unit roundoff）及额外 subnormal 预算；正卷积和正矩阵乘积用 $(observed+underflow)/(1-\gamma)$ 作上界。后续半径合并和每次关键代数操作均向外舍入。
- Bernstein 权重为精确二项式有理数的向外包围，凸包范围后再作 Fourier l1；不存在把角采样最大值提升成全圆上界的步骤。
- 供应器 uniform remainder 进入常数系数区间是合法的点值包围：每个位置可有不同 remainder 值，Bernstein 包围对所有允许系数同时成立。
- 从坐标误差 $(b_E,b_F,b_G)$ 到材料正交框架的三项界及对称矩阵行和范数界均正确；$a_*,\rho_*$ 的正性在使用前检查。

这些算术声明采用普通 IEEE754 binary64、正确舍入 sqrt 和有限标准乘加模型；没有宣称证明助理形式化或任意硬件编译器语义。

## 3. 供应器检查

主参数解释成精确二进有理数，周期长度由同一 Fraction 表达式重新计算。flat primitive 三段公式与原 profile 一致，且邻段的实际交叠通过精确有理多项式差控制。修复后分支由真实 piece 编号指定。

角图的 clamped spline 通过 Fraction 三对角系统求解，而非把分别舍入的 PPoly 当成精确 C² spline。其截止函数与导函数来自同一个局部多项式；首端导数为零、末端两阶平坦由公式给出。邻断点包围同样不靠数值近似等同。

桥的相位是冻结参数的精确三次式，sin/cos 的零点 Taylor 余项、局部相位的五阶展开余项及积分后的高次截断预算均有效。节点半径 interval 按同一个真积分连续累加。第一桥节点若在真实 prefix 端点两侧，锚值用速度不超过一包围；必要的 prefix 外延范围 guard 已加入。

重要边界保持：此证书的桥 $L,p_t,p_s$ 是冻结 binary 常数，尚未证明满足最终共同精确 cut 的匹配根。输出明确记录端点半径、速度及长度偏差并置 `exact_bridge_matching_root_certified=false`。本审查不将这些偏差改写成零。

## 4. 独立全量复跑

root 使用本题 `repro/source-root` 快照，以真实宏观 `db6f-root-flat17-coupled-m8f16.json` 为输入，分别执行供应器与验证器，输出：

- `2026-11-09-db6f-root-metric-coupled-replay-target-v2.json` 及配套压缩数据；
- `2026-11-09-db6f-root-metric-coupled-replay-v2.json`。

生成的目标数据 SHA256 与作者 v2 逐字节相同：
`4674eef190bb613fc3953e37fc6f643636c15ecbf45bf97ac2d4f3d1cadf62d2`。
覆盖全部 846 解析审计段、完整圆周，材料相对 metric 算子范数上界为
$$
\boxed{3.622549868552692\times10^{-7}}.
$$
该界和最坏区间与作者复跑一致。此处整个 t 的传递只适用于另外明确构造的正确材料角相位族；它不补付完整公共 metric、尾与帽的接口和固定 g 收敛。
