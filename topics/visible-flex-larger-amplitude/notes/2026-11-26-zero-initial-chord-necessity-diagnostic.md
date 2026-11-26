# 零闭合真实初输入的弦长必要条件：完整区间诊断入口

日期：2026-11-26。此入口响应 [公开 run 45820592817/1，part003](2026-11-26-public-actions-45820592817-1-part-003.md) 阶段 11 的实际初根失败。它读取真实初始自由点，而不要求一个尚不存在的零闭合初场，不把失败报告作为场 checkpoint，也不增加求解或最终验收门。

## 1. 从同一准确表示得到的必要条件

保持已刊 `5b4c3921…` 零闭合模型的准确固定 scalar 目标、原材料图及所有原自由变量。若该输入的真实端点方程可以闭合，则

$$
F_s(s,\phi)=T(s,\phi),\qquad |T(s,\phi)|=1,
$$

并且

$$
F(0,\phi)=\Gamma_c(\phi),\qquad
F(S,\phi)=P_{\rm cap}(\phi).
$$

因此微积分基本定理与积分三角不等式给出

$$
|P_{\rm cap}(\phi)-\Gamma_c(\phi)|
=\left|\int_0^S T(s,\phi)\,ds\right|
\le \int_0^S |T(s,\phi)|\,ds=S. \tag{1}
$$

这里的 $S$ 是原准确符号域长度；它不是 mesh carrier 的末项近似。$T$ 的单位长度来自完整准确 $T_0$ 及两层真实 SO(3) 旋转，不依赖某个 Newton 步是否成功。故式 (1) 与 bubble 支撑、三维求根搜索球半径和求根初值无关。

式 (1) 约束的是给定准确目标下**本次特定 core/$H$ 自由输入**。如果严格违反，它排除所有满足同端点和单位径向条件的旋转修正，而不排除改动自由 core、自由 $H$ 或其他新输入。它更不构成本课题、固定目标类或所有闭合等距构造的不存在结论。

## 2. 初始 current core 等于冻结图 core 时的准确公式

此次实际报告无 restart、无 direct-base seed，原自由点来自同一 `q.initial()`。完整源码把全部自由 core 系数取为初始参考 core、所有 omega 设为零，并把自由高度取为参考中的原字面高度。

记 $\nu_m=2m$，完整 $160$ 项都保留：

$$
p(\phi)=1+\sum_{m=1}^{160}c_m\cos(\nu_m\phi),\qquad
p'(\phi)=-\sum_{m=1}^{160}\nu_m c_m\sin(\nu_m\phi),
$$

$$
\delta(\phi)=\Theta_0(\phi)-\phi
=\sum_{m=1}^{160}\frac{1-\nu_m^2}{\nu_m}
 c_m\sin(\nu_m\phi),
\qquad
\rho(\phi)=1+\sum_{m=1}^{160}(1-\nu_m^2)c_m\cos(\nu_m\phi). \tag{2}
$$

当完整圆周的 $\rho$ 有严格正下界时，$\Theta_0$ 是全实唯一 lift；current 与 fixed 系数逐字相同，故 $\Theta_c(\psi)=\Theta_0(\phi)$ 的相应唯一实逆准确为 $\psi=\phi$。这一步不需要先运行数值逆图或端点根。

在普通 normal-angle 正交架 $(e_r(\phi),e_\theta(\phi))$ 中，

$$
\Gamma_c=p\,e_r+p'\,e_\theta,\qquad
P_{\rm cap}=R e_r(\Theta_0)+H e_z,
$$

于是水平弦长平方是

$$
Q(\phi)=\bigl(R\cos\delta-p\bigr)^2
       +\bigl(R\sin\delta-p'\bigr)^2, \tag{3}
$$

完整弦长平方是 $Q(\phi)+H^2$。源独立包围两个实分量后平方，遇零交叉时把平方下界置为准确零；没有在二次式中使用可能错误的区间单调方向。

两条轴向见证还能免除三角函数的近似：$\phi=0$ 时所有 sine 准确为零、cosine 为一；$\phi=\pi/2$ 时 sine 准确为零、cosine 为 $(-1)^m$。从而

$$
Q(0)=\left(R-1-\sum_m c_m\right)^2,\qquad
Q(\pi/2)=\left(R-1-\sum_m(-1)^m c_m\right)^2. \tag{4}
$$

数值 root 失败报告的残差与修正最大值均不进入这些公式。

## 3. 完整外包与全角覆盖

`diagnose_zero_initial_chord.py` 使用原 `e091f675…` integer interval 的精确有理包围和三角函数实现；$R$ 使用真实完整参考模型内的 `radius_complete_enclosure`，保留 R690 全尾费用。$S$ 使用经原 scalar 输入重建的 `FullHold.S` 及其自身整数比例尺；$H$ 和每个 core 系数取实际 binary64 字面的准确分数。所有乘加、三角函数、平方和除法均向外包围。显示用近似小数只在公开 Actions 中由实际区间生成，任何严格判断都用有理端点。

源同时读两条准确轴向见证，以及本次完整 `q.phi` 中最前面的八个实际 binary64 角。每个后者的角取其准确字面值，记录对应 hex；它们不是把失败残差转作几何值。

完整连续范围从一个闭区间 $\phi/\pi\in[0,1/2]$ 开始。每次先算出两个子区间的完整盒，再替换父区间。无论自然时间或叶数预算何时用尽，已返回的叶集仍覆盖整个闭四分之一圆，不丢任何开缝或端点。

$p,\rho,Q$ 均为 $\pi$ 周期偶函数；$\delta,p'$ 为 $\pi$ 周期奇函数，式 (3) 因此也对 $\phi\mapsto\pi-\phi$ 不变。四分之一圆的完整覆盖经过这两种反射覆盖全部实角。

$\rho$ 的全局界由完整逐项 $L^1$ 界与完整角覆盖界相交。尚未证明严格正性时，只返回完整范围，源不启用“唯一 inverse branch 下的初输入障碍”旗标，也不把数值正采样当作全圆正性。

设返回的 $Q$ 全角最大值满足

$$
Q_-\le \max_\phi Q(\phi)\le Q_+.
$$

$Q_+$ 取全部完整角叶上界的最大值。$Q_-$ 取全部叶下界和实际点见证下界的最大值：每一个这样的下界都不大于全角最大值，故此最大值仍合法。源还检查独立点与覆盖外包不矛盾。所请求的 $Q_+-Q_-$ 精度如果未达到，已有盒仍然有效，报告明确保留 `requested_accuracy_reached=false`。

## 4. 严格判断与可用高度区间的方向

设 $S\in[S_-,S_+]$。原初始高度是准确字面 $H$。有

$$
Q_-+H^2-S_+^2
\le \max_\phi\bigl(Q(\phi)+H^2-S^2\bigr)
\le Q_++H^2-S_-^2. \tag{5}
$$

如果一条真实点的完整差值盒下界大于零，或式 (5) 左端大于零，并且全圆 current/fixed chart 正性已证，就严格排除本次固定 core/$H$ 输入下的单位径向闭合。报告使用限定名称 `no_unit_meridian_closure_for_this_fixed_initial_core_H_certified`；它不命名为等距课题不可解。

若式 (5) 右端不大于零，则只证明全部角满足式 (1)。它不能推出端点旋转方程可解、局部 Jacobian 满秩、嵌入、reach 或完整等距。

保持本次 core 和准确目标、只改自由高度时，还可得到：

$$
H_{\rm new}^2\le S_+^2-Q_-
\quad\text{是闭合所必需的上界}, \tag{6}
$$

而当 $S_-^2-Q_+\ge0$ 时，

$$
0\le H_{\rm new}\le\sqrt{S_-^2-Q_+}
\quad\Longrightarrow\quad
Q(\phi)+H_{\rm new}^2\le S^2\ \text{对所有角成立}. \tag{7}
$$

式 (7) 仅是通过弦长必要条件的充分高度界。代码以 integer `isqrt` 对有理数求向外平方根；使用其下端选择高度才保证式 (7)，使用式 (6) 平方根的上端表达必要上界。两者不能互换。

报告从这次完整实际幅度预算中读取 `effective_height_floor` 的字面准确值，另外说明式 (7) 给出的高度范围是否仍包含高于该 floor 的区间。不降低已有幅度 floor，也不写入任何新高度。后继若改变自由 $H$，必须是新的明确初值选择，随后保留全部变量、真残差、原行及全几何/幅度筛；当前入口不替这些步骤预判成功。

## 5. 独立初输入来源与可执行参数

该源不调用接受场专用的 `ActualZeroInput`，不删除它的 checkpoint 要求。这里有单独的 `ActualInitialInput`，职责严格限定为本次实际未种子重启的初输入：

1. 核实际失败报告 schema、真实完整 `b4d71ade…` driver 和全部 source role 字节；要求真正 `actual_initial_zero_closure_field_read_failed`，且没有初/末场、restart 或 direct-base seed。
2. 核四个实际参考文件、完整 preparation 及其 `4e65577d…` 来源；经原构造器重新得到完整准确目标、mesh、chart 与 scalar 模型。
3. 用实际参数建立原 `7f26ff35…` base 和 `5b4c3921…` zero 模型；与失败报告的完整模型、固定 scalar、policy 逐项相等。
4. 读取原 `q.initial()`，核完整自由向量 SHA 与真实异常记录及最新 operator metadata 同为 `cd530c07…`；核 current=fixed 全 core、所有 omega 为零、原 $H$ 字面一致。
5. 全过程不调用端点求根、残差、$F$、$J$ 或 $J^*$，并在输出前核这些实际调用计数仍为零。

实际绑定的失败报告为：

`4341323c805a3e4f38c20c6e5264e9875b8b717082793ece982c029f488ed744`。

参考 bundle 与 scalar 身份分别为：

- `0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1`；
- `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb`。

完整源 `diagnose_zero_initial_chord.py` 为 `25311` 字节，SHA256：

`65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0`。

完整单阶段 [ready参数](../computations/resume-20261126-zero-initial-chord-diagnostic-steps.json) 为 `7360` 字节，SHA256：

`0016f57860ac7174546c520d36a552866d89862480e1ba059c5a773922202d58`。

它保留已有真实参考 parent，读取新 `.75` 失败报告，使用 `60` 秒自然 admission、至多 `256` 个完整角叶、原 `128` scalar panels、八个实际首角，另请求 $10^{-10}$ 的水平最大值平方外包宽度。精度、时间或叶数用尽不截尾，不把条件未证写成严格障碍或成功。

源码经过 AST/compile、重复 dict key/keyword、CLI 名称及来源静态核对；construction 已独立复核式 (2)–(7) 和完整覆盖的上下界方向。当前未在本地执行科学计算，也尚无本诊断的真实 Actions 返回。此说明提供完整推导和可执行入口，不预填诊断结果。

## 6. 阶段14的实际返回：当前输入通过全部弦长必要条件

类型：公开 Actions 的完整向外区间数值证据；不是端点求根成功或闭等距存在结论。

[03b阶段14实际记录](2026-11-26-public-actions-45820592817-1-part-004.md)已返回，实际外层秒数 26.01711728400005、exit 0，内部秒数 21.55870132600012；source commit `b0ce03b92b21b08dafeab40218a72e12e1e6bdbf`。完整源仍为上述65787b3e，真实报告 SHA256 `49538e228b7cc5fa0f6617c0847cfe6cf73bb58781283611f0319ce2d67b5eb0`，299582字节，仅留runner；输入完整失败4341323c、模型29f540c6、自由初点cd530c07、准确固定scalar6ffc均再次实际绑定。

原高度为 `0x1.f27228dabd944p+0`，即精确有理数 `2192188409312849/1125899906842624`，显示工作值1.9470544370684175。所有160个core模式、两条准确轴和原首8个literal角均读入；256个闭角叶覆盖完整四分之一并经对称覆盖全圆。全圆rho严格为正，报告 `rho_positive=true`。请求的水平最大值平方宽度未达到（`precision_reached=false`，停止于完整叶预算），已有完整外包仍有效，不丢未精化的叶。

完整最大弦长平方减去真实S平方的严格上界为

$$
\frac{-552100725590121109140894695655279009490692367551695160412357945602997397}
{500000000000000000000000000000000000000000000000000000000000000000000000}<0.
$$

因此本次实际 `all_chords_necessary_condition=true`、`point_chord_obstruction=false`、`no_closure_for_this_core_H=false`。这排除了“当前H造成普遍弦长超限，所以任何单位母线闭合都不可能”的解释；它不证明有限bubble端点映射可达、Jacobian可逆或完整E/B可解。不能据此声称必须降低当前H，亦不能因必要条件通过而制造初场。

保持同core和准确目标时，通过全部弦长条件的高度充分下界端点（式7使用平方根下端）实际为

`2212514956353528124420170437536814118275649940681685866920143616697546937/1000000000000000000000000000000000000000000000000000000000000000000000000`。

必要高度上界的向外上端为

`442791470453033368164202054454989042887167932010934168733112557245956737/200000000000000000000000000000000000000000000000000000000000000000000000`。

报告也确认该充分区间包含高于原完整幅度floor的区间；floor字面为 `4548635623644201/4503599627370496`。这是可选择输入的范围说明，不是修改高度、放宽幅度或验收。此次 `height_written=false`、`initial_field_manufactured=false`，zero-root、full residual、J和Jtranspose调用全部为0；metric、连续几何及isometry旗标全false。

下一实际输入检查同一wide/.75端点Newton的真实失败角、矩阵与回溯，同时读取完整wide控制矩；原失败报告未保存这些逐角中间量，不能由纯reader凭空恢复。保原方程、全部变量、真正root容差和几何筛，再按实际归因选择控制方向或明确的新初输入。
