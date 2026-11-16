# R868 — 原 P0 准确 socle、两图逆点理想与五个 RR 模块源已完成

日期：2026-11-16。状态：**公开 Actions 已完成本篇的准确算术出口。**

原 run **43819875762**、job **133140317613**、source
`9586473c46712b6c00a6f8e5736bf387b987ef6b` 成功。它取得原
$W(z_0)-w_0I$ 的特征零秩271证书、准确一维核向量、两图完整
$I_{P_0}^{-254}$，以及五个原 $\mathscr L_j(254P_0)$ 的十个仿射模块表达式。
数学 core receipt 计时 **120.82823749299996 秒**；最终证书在写出时记录
120.80491799699999 秒。共有 **699 个已完成数学阶段**。

这些输出给后继 RR 求解提供实际新的单极函数，不是仅有未展开的余子式。
最终证书同时准确保留
`degree254_RR_basis_128_computed=false` 与
`original_connection_or_height_computed=false`。

## 1. 固定的原来源和真实秩证书

沿 [R868 证明](R868-original-P0-pole-generators-and-degree254-RR-certificate.md)
及[执行方法](../notes/R868-original-P0-socle-and-degree254-module-method.md)，保持原
$K=\mathbf Q(\zeta)$、$\zeta^2+\zeta+1=0$，以及

$$
R_\tau=\bigoplus_{i=0}^{271}K[z]\beta_i,
\qquad \epsilon=(0,1^{144},2^{127}),
\qquad W=M_w,\quad w=\beta_1.
\tag{868R.1}
$$

W 的34组准确系数仍是 R806 的原系数，按 R860 的真实索引读取。
[R856](R856-certified-original-two-chart-point-and-fixed-branch-ideals.md)
已成的同一 $P_0=\phi(c_0)$ 给

$$
z_0=-\frac{497}{7491}-\frac{20008}{7491}\zeta,
\qquad w_0=-\frac{1557}{2497},\qquad v_0=z_0^{-1}.
\tag{868R.2}
$$

本次没有重新构造 W、重算这些点值或改换 P0。
准确列尺度清除后的点矩阵由34个已保存块给出。实际选择的子式为行、列
**0 至270**，自由原 normal 坐标为 **271**。合法辅助素数和两个嵌入为

$$
\ell=1000000753,\qquad
\zeta\mapsto450033991\ \text{或}\ 549966761.
\tag{868R.3}
$$

同一271阶子式在两嵌入的实际行列式分别是

$$
795557578,\qquad873031455\pmod\ell.
\tag{868R.4}
$$

原有理分母及本次列尺度在两处均为单位。原 P0 的完整左评价向量同时通过
全部行方程，给特征零秩至多271；(868R.4) 给秩至少271。因此实际得到

$$
\operatorname{rank}_K(W(z_0)-w_0I)=271.
\tag{868R.5}
$$

这里没有计算一个巨大特征零行列式，也没有把辅助有限域秩孤立地当作全部证明。

## 2. 准确核向量与全方程乘回

两份271阶模逆均已保存，且两侧逆乘积准确通过。固定它们以后，core 对同一
两坐标 K 系统作 Dixon 提升，在 **584 位**取得严格有理重构。
成功重构 stage 是 `R868-RR-at-digits-000584.json.gz`。

清列尺度被准确恢复以后，实际输出

$$
h=(h_0,\ldots,h_{271})^t\in K^{272},\qquad h_{271}=1,
\qquad (W(z_0)-w_0I)h=0.
\tag{868R.6}
$$

`h_tau_K_1_zeta` 保存全部272个准确 K 坐标，每个有理坐标均为原整数分子、
分母对。它不是仅一份模核，也不是一次候选有理重构：全部272个清尺度 K 方程
和全部272个原 W 方程均准确乘回为零，即完整544个有理坐标均已核。

核向量归一值1发生在实际自由坐标271；策略字段中的“自由坐标值1”不能误读成
固定选择原第1列。

## 3. 完整两图逆点理想与第147个截面

令

$$
r_\tau=\sum_i h_i\beta_i,
\qquad f_\tau=\frac{r_\tau}{z-z_0}.
\tag{868R.7}
$$

R868 命题868.1 逐纤维局部因子的证明现在适用于真实 (868R.5)–(868R.6)。
它允许 $z$ 在 P0 分歧：若 $e=\operatorname{ord}_{P_0}(z-z_0)$，则实际一维核
挑出 P0 因子的全部 socle，$\operatorname{ord}_{P_0}(r_\tau)=e-1$。
其他同纤维点的分子至少具有相应纤维重数。因此 $f_\tau$ 在 $U_\tau$ 上只在
原 P0 有极点，且极阶恰为1。

第二图保持原 $\gamma_i=v^{\epsilon_i}\beta_i$，实际准确运输为

$$
(h_\sigma)_i=v_0^{-\epsilon_i}h_i,
\qquad f_\sigma=
\frac{\sum_i(h_\sigma)_i\gamma_i}{v-v_0}.
\tag{868R.8}
$$

全部272个系数的运输及重叠式

$$
f_\sigma=-zz_0 f_\tau+
z_0\sum_{\epsilon_i=1}h_i\beta_i+
z_0^2(v+v_0)\sum_{\epsilon_i=2}h_i\beta_i
\tag{868R.9}
$$

均已准确核验，没有另求第二个核或遗漏 $v_0^{-\epsilon_i}$。
曲线各 DVR 的局部阶因而给完整的嵌入分式理想等式

$$
I_{P_0,c}^{-m}=(1,f_c^m)_{R_c},\qquad
c=\tau,\sigma,\quad m\ge1.
\tag{868R.10}
$$

保存的实际目标取 $m=254$。这是曲线上的完整理想等式，不是一般多变量环中
只保留两个端点纯幂的错误公式。

又因 $f_\tau\in H^0(H_\tau+P_0)\setminus H^0(H_\tau)$，原146个截面加这个
实际新函数，得到完整147基

$$
1,z,\beta_1,\ldots,\beta_{144},f_\tau.
\tag{868R.11}
$$

本式的147不等于原 YP 的128维或634维空间。

## 4. 已完成的十个原目标模块

消费者直接引用 [R849](R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)
原523节点图中的 `eta_degree_zero_fractional_ideal`，保留原五对

$$
(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134).
\tag{868R.12}
$$

它新增26个有源节点，准确给出

$$
M_{j,c}=\mathfrak L_{j,c}+f_c^{254}\mathfrak L_{j,c},
\qquad j=1,\ldots,5,\quad c=\tau,\sigma.
\tag{868R.13}
$$

由 (868R.10)，这些就是原 $\mathscr L_j(254P_0)$ 的完整两图仿射模块。
原 $\eta$ 的负号、分母67或134、七重真实范数、$\beta$、$\lambda$、各相位、
两个具体帧以及 theta 二挠比较全部沿原来源保持。未使用三同源后的
`real_descent_degree_zero_fractional_ideal` 替代它们。

R868 定理868.2 已证明

$$
\pi_*\mathscr L_j(254P_0)
\simeq\mathcal O^{128}\oplus\mathcal O(-1)^{144}.
\tag{868R.14}
$$

本次所得是 (868R.13) 的准确输入，不是 (868R.14) 分裂同构的已算矩阵。
后继仍须实际取得128个权0和144个权1截面，认证原两图包含和完整272秩，才完成
对应 RR 基。R872 可直接复用本次 h、点矩阵块和固定模逆；不能重做已成核，
也不能把旧模列换标签作为原目标截面。

## 5. 完整来源、产物与传输身份

公开运行：
[run 43819875762](https://github.com/Rogerhu12/math-research-public/actions/runs/43819875762)。
原数学脚本为 `scripts/R868_original_P0_socle_and_RR_modules.py`，core SHA256
`cdac462c9f96011e4526cd7ad209e5fbd443d4c0e62e38cf31c04219ca525270`；
纯 IO wrapper SHA256
`9115331ea60213edef3a3066c82aad4abd43e344dc566a5c5a8be8297ada9033`。
原证明 SHA256
`98e15284b0c8c080eb01f1a53add7c4eef9ae56e8f10f02c4b8105fc7408d246`；
执行方法 SHA256
`aa91885fd2b652096e159ba5b00cca70849203e2d0e60d19624efb27bbdafb89`。
实际数学配置 fingerprint 为
`d89c0ed6cbf0869191daed5c5e9a6075f4638140b5c9a89f1c486b4e818cda92`。

| 已成对象 | Bytes | SHA256 |
|---|---:|---|
| 最终证书 | 8069 | ef1dc965518d2ac987a36bf025ae0aa808fd4dc872ef3b1db68c6bfdb2a17d11 |
| 原点整数矩阵索引 | 77121 | 6812c5a099a72e624dd624dacc448dd263fa11e68c6e969cc78c99504fb1102c |
| 实际271阶子式 | 698249 | 116284cadececb504df3852d3b10e4abf4e6a66d059d102f5b87eb0cd6647ab3 |
| 两份固定模逆 | 699696 | a36b8271401477ef205eebf34efef643a2af044e02b330dd6687a326ffc4975d |
| 584位成功准确重构 | 621757 | e2617383df2081d80b1266f5e5d7bd1a1fac22c68f967db773cbf9f073e74a06 |
| 全部原 normal 核向量 h | 1097963 | 5de7d08de2f117aebb5bd607dbf13c40e5ac6feb796b163c8007e4cafe295e07 |
| 两图254次逆点理想与准确运输 | 1596038 | 13de406df31832fecb3a5b710b09e3a8e4fccd576933233ba3e9c9fbb5739ca1 |
| 五个原目标的十个仿射模块 | 5751 | 0e73e6cc801ce34a56ae070fbf0f0376d507bd9813317b65fa55572cbba71555 |
| 699阶段索引 | 35165 | a58110dfb262c053aa171d037bd94f4b22d4d647052e27bdb10338e29e98acca |
| 全部输出 manifest | 117917 | 8251e046031b202ea5e49faa2ec2a1591c11c8a103e563fc0b340ab091dae1b8 |

最终证书文件名为
`p41-original-P0-socle-and-RR-module-certificate.json`。
原输出 manifest 列719项。artifact **14203769509** 名为
`serre-R868-original-P0-socle-RR-modules-43819875762-1`，
204985706 bytes，平台 ZIP SHA256
`d57536f903ec17bd4f637250b341444ba734aa2f6a0dea6386dbe67ca211c27a`，
2026-11-17 06:58:11 UTC 到期。

根会话的结束读取只用13次 Range 传输95551265 bytes，逐原 manifest 核了718个
选定非载体文件，另保 manifest；**这次没有重新下载或哈希整个 ZIP**。
ZIP 身份仍明确来自平台记录，不能把选择成员核验表述为整 ZIP 本地复算。

本次原80成员载体分为 R805七件、R806四十五件、R849十件、R856九件、R860九件。
`R868-retained-original-inputs.tar.gz` 为109552606 bytes，SHA256
`e7cd24e29757254cae9526207a19161f15ef8198b6bc45922481a0720acd8618`；
原来源 inventory 为19470 bytes，SHA256
`4b09a35bcbc3177cd197612f8d8fbe59c1e3ea7c93e3ead3b95da83f044d4f85`。
这保持了后继所需原 W34 全字节和五个真实图的源身份，不包含原 global 图所引用
全部2709大型叶的重新展开结果。确需那些叶的后继应沿仍有效的原载体逐源取得。

## 6. 本次范围

实际完成的是原一维核、单极函数、两图完整逆点理想和五个254度模块源。
尚未算出原 $a_j,c_j,a_j(P_1)$、128或634维 RR 基、连接主部矩阵、Hecke 周期行、
完整非 $p$ 项或指定高度。这里的原 $z$、$w$ 也没有被直接改称 YP 的原参数
$t=a^3$。Serre 一致性主目标仍未完成。
