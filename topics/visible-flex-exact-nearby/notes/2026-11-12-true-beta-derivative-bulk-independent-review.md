# 真实 β′ bulk 的独立源码审计

2026-11-12，constructive_route。审计两份冻结源全文：

- `fourfold_phase_beta_derivative_bulk.py`，SHA256
  `28f0989aaab52e858bbe10d9e8b004f205e6e60669ec9a7c965b6c9072e97f52`。
- `fourfold_phase_beta_derivative_bulk_refined.py`，SHA256
  `a643f46b5231b79f005c9d714292485e9f03f5318f9061d95d39de59d10f5842`。

同时阅读其 `ParameterDerivativeTarget`、参数 scalar germ、
`BulkTarget.explicit_germ/physical_fields` 及真实 β′ 说明中对应公式。
没有重复运行已完成的 bulk，也未替代 root 对 collar、collector 和全覆盖总和的独审。

## 1. 真正的角导数和参数导数

设圆柱分量 `T=(−sinβ cosγ,cosβ cosγ,sinγ)`。源码的 Tt 包含
普通分量 θ 导数以及旋转基项 `(-T_y,T_x,0)`，因此输出确为
`Fθ=aT`、`Frθ=a' T+aTr`、`Fθθ=a DθT`，不是有限 primitive 的角微分。
角波数使用 `4k`，与规范角 `x=4θ` 一致。

Dual 同时微分 a、a'、β、γ 及它们的径向与角向导数，符合乘积和链式法则。
F、Fr、Frr 的参数列由同一规范原函数的真实 affine 方向取得，并已有各自
无限 primitive 和 E 参数尾。物理 r 导数与局部负向 series 之间的反号
`Kr=−K[1]`、`(Kr)p=−Kd[1]` 正确。两种商实现都是准确商法则的区间表达，
refined 中 `(v_p−(v/w)w_p)/w` 的依赖损失只会扩大包络。

法向取 `Fθ×Fr`，其 r、θ 导数和 area、radius、support、a、b、c 的双数
微分均对应相同对象。`κ=√(−K)` 的倒数参数导数带正号，
所以密度导数 `N_p/κ+N K_p/(2κ³)` 正确。

## 2. 完整连续角盒

真实三角场在每个 `2πj/A+[-π/A,π/A]` 规范角区间直接取原生区间值。
这些闭区间覆盖整圆，未把有限节点最大值当成连续最大值。
F、Fr、Frr 使用的 `physical_fields(...,angular_sigma=0)` 同时支付有限
Fourier 模在实角区间的平移误差，以及对应角宽上的无限 primitive 尾。
局部 scalar polynomial 通过准确正负 binary knots 的共同 span 选定，
参数保留为同一实际 affine 区间。

每个几何分母都在完整 `r×θ×p` 盒上检查严格正性。
所有盒的密度参数导数模上界乘准确径向长度，确实是连续积分上界，
不涉及未付精度的角求积或径向采样。

## 3. 腰部与首 span

高度奇性给出
`Fz/r=∫_0^1 Fr,z(sr) ds` 和
`Fθ,z/r=∫_0^1 Frθ,z(sr) ds`。其 p 导数也在同一积分中取值。
对 `[0,right]` 的各自值与各自 p 导数作区间包络，再用双数商法则，
会包住两个真实平均的比及其参数导数；没有假设两个平均对应相同的中间点。

refined 源保存原局部 scalars/directions，仅为这个高度商重新覆盖 `[0,right]`，
然后恢复局部状态。其它 F、Fr、II、target K 和密度系数仍使用 `[left,right]`。
因此改进既有效，又能随细分收紧其它几何量。其 selector 对首共同 span 的
使用允许延伸到零，因为此前已严格检查 `2^-20` 小于第一正 knot。
原源扩大全部几何的方式也为有效上界，但较松；最终首 span 采用 refined 数据。

## 4. 失败尝试、阈值与本次范围

`base_total_budget/root_total_budget` 仅决定是否继续细分。
接受叶独立保存实际 `density_derivative_absolute_bound` 和
`derivative_absolute_integral_bound`；判断只在真实上界严格小于分配预算时接受。
最后一批的 `100000` 是该算法阈值，不能作为 β′ 结果。

已读的原 `part01` 报告含 27 个失败尝试；它不是整段完成证书。
后续总和必须使用 collector 选择的、完整覆盖对应原 scalar span 的叶，
失败或仅局部完成的旧叶不得混入。此项全覆盖及有向总和由 root 另作独审。

在上述审计范围内未发现数学、符号、连续覆盖或参数微分错误。
本 note 不重复宣称整个有限部 β′ 证书已由本人重算，也不把 β′ 证书
升级为真实返回 KAM、完整 PDE 逆或课题的最终精确族。
