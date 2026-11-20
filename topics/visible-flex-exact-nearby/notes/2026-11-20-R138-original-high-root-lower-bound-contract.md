# R138 原 high97 根压缩：新单侧标量消费者合同

科学入口拟公开为 `scripts/fourfold_codazzi_original_high_root_lower_bound.py`。本合同是已发表 HP.12 的后继收紧及其完整科学执行范围，不修改旧 HP、W、X、axis、mean 或 signed 96/97 结果。

## 1. 唯一新对象与已成目标的边界

新对象是同一 `Qrepair`、固定 `eta0/nu`、真实根 `r_*`、真实 periodic frame、`p=(0,0,1/2)` 上，原全部 `j>=97` 根型的单侧下界。几何与标量均用同一 moving `phi`、完整 `2*pi` 圈、归一角内积。原 low `1..96` / high `97..infinity` 不变；没有有限截断 high，也没有将人工轴矩形顶点冒作真实几何。

读取并核完整 axis `44730968113/1`、mean `44733403315/1`、X `44737045152/1`、signed 96/97 `44745192261/1` 及各 execution。signed 原件含前三者的完整对象，本输出保留这一整份 nested 原件；独立输入又逐一与其中对象比对。旧轴坐标、实际 mean 分母及四个根 `Z/Z_theta/P/P_theta` 都只读。旧 signed 三矩阵项、旧两响应 primitive、旧 Z/P 径向传播、旧轴目标和旧 mean 目标调用均为零。

原五个 cubic shard 加一个 root germ 仅用于私有候选定义恢复。全修补及同一 root 区间通过已成 definition helper 输入，完整 mean、32 sine 与32 cosine 背景都保留；不重新拟合旧候选。不发表候选、frame、Fourier 或 Gram 数组。

## 2. 新全角标量目标及 actual 导数

新科学只走 `32768` 个闭角格，Arb `320` bits。每格包含真实完整角区间和完整旧轴误差球，使用原 W 的实际 frame/position 误差 `11/10^7`、`1/25000`。角平行运输只给私有比较量，不被当作真实全圈周期 frame；实际 frame 与位置及其导数仍带下述完整 X 缺陷。

记

\[
 s=v/m,\quad \rho=a/m,\quad
 w_1=b_{\rm geom}s,\quad w_2=\rho u,\quad w_3=\rho,
\]
\[
 \Omega=\begin{pmatrix}0&-w_1&-w_2\\w_1&0&-w_3\\w_2&w_3&0\end{pmatrix}.
 \tag{HC.1}
\]

这是原 W/HP 的连接顺序；不能改成把 `(w1,w2,w3)` 当普通叉乘向量的另一种 skew 约定。完整 actual 根公式为

\[
 O'=O\Omega+sZ,\qquad
 O''=O'\Omega+O\Omega'+s'Z+s^2Z_\theta,
\]
\[
 G'=\rho vY+sP,\qquad
 G''=\rho v'Y+\rho vY'+s'P+s^2P_\theta.
 \tag{HC.2}
\]

`Z_theta/P_theta` 是已成 X 的 physical 角导数，故 `(HC.2)` 中必须有 `s^2`。旧 `Z/P` 传播不再执行。完整 actual 根仍正交，`X cross Y=-n`。

真实 principal 为 `a_pr=-2 rho^2 sigma/v`、`sigma=G dot n`。从 `(HC.2)` 求

\[
 \sigma'=G'\cdot n+G\cdot n',\qquad
 \sigma''=G''\cdot n+2G'\cdot n'+G\cdot n'',
\]
\[
 a_{\rm pr}''=-2\rho^2
 \left(\frac{\sigma''}{v}-\frac{2\sigma'v'}{v^2}
       -\frac{\sigma v''}{v^2}+\frac{2\sigma(v')^2}{v^3}\right).
 \tag{HC.3}
\]

此 actual `C2` 费用没有由 W 的 `C0` 单独提升。每格 principal 下界可取完整 `sigma` 包围的下端与已付 actual `2/5` 的较大者；`G0` 可取全格位置范数上界与已付 `222/125` 的较小者。两者都针对同一个 actual 对象，因此合法；没有据此授予整个假想轴矩形的支撑正性。

## 3. 精确消掉 c 中的 v/m 商费

令 `V=Y+uX`、`M=1+u^2`。从 `(HC.1)` 的三列得

\[
 X'=w_1Y+w_2n+sZ_X,\quad
 Y'=-w_1X+w_3n+sZ_Y,\quad
 n'=-w_2X-w_3Y+sZ_n,
\]
\[
 V'=(u'-w_1)X+uw_1Y+\rho M n+s(Z_Y+uZ_X).
 \tag{HC.4}
\]

HP.6 的向量 `c` 于是准确为

\[
 \boxed{\quad
 \mathbf c=-\frac\rho m
       [b_{\rm geom}(Y+uX)+(Z_X-uZ_Y)],
 \quad}
\]
\[
 \boxed{\quad
 \mathbf c'=-\frac\rho m
       [b_{\rm geom}V'+s((Z_\theta)_X-u(Z_\theta)_Y)-u'Z_Y].
 \quad}
 \tag{HC.5}
\]

系数 `rho,m,b_geom` 在这个固定根圈上为常量。这里用的是真实 physical 缺陷的 moving pullback；`Z_phi=s Z_theta`，没有省角 Jacobian。

对完整矩阵范数上界 `z0,z1`，正交 frame 给

\[
 V_0\le\sqrt{1+|u|^2},\quad
 V_1\le\sqrt{|u'-w_1|^2+|uw_1|^2+|\rho M|^2}
                         +|s|\sqrt{1+|u|^2}\,z_0,
\]
\[
 c_0\le|\rho/m|\sqrt{1+|u|^2}(|b_{\rm geom}|+z_0),
\]
\[
 c_1\le|\rho/m|
     (|b_{\rm geom}|V_1+|s|\sqrt{1+|u|^2}z_1+|u'|z_0).
 \tag{HC.6}
\]

这些是整向量范数，非逐坐标最大值。科学入口对 signed triple 使用 `(HC.5)` 的完整向量误差球；对算子费使用 `(HC.6)` 的整向量界。

另记 `b=rho Y`。除直接 `(HC.2)` 的实际 `b''` 上界外，允许以下等价更紧界。完整展开

\[
 Y''=(-w_1'-w_2w_3)X-(w_1^2+w_3^2)Y-w_1w_2n
    +s(-w_1Z_X+w_3Z_n)+s'Z_Y+s^2(Z_\theta)_Y
\]

给

\[
 b_2\le|\rho|\left[
  \sqrt{|w_1'+w_2w_3|^2+|w_1^2+w_3^2|^2+|w_1w_2|^2}
 +|s|\sqrt{|w_1|^2+|w_3|^2}z_0+|s'|z_0+|s|^2z_1\right].
 \tag{HC.7}
\]

两个已包含 actual 导数的上界取较小者合法。不需要 `c''`、frame 三阶导数或 X 未保存的高阶缺陷。

## 4. 完整 signed 局部型

使用已发表 HP.8--HP.9 的全部六个剩余局部系数、完整 mean rank 和两个非局部 primitive。三项平方系数只取 signed 负部 `max(0,-A)`，其余三个 cross 取绝对值；这是单侧下界，不是 compact 的两侧算子范数。

最大的 `Aqq` 首先使用已发表 HP.13：

\[
 A_{qq}=\frac{\rho^2}{v^2}
 \{[s b_{\rm geom}(1+u^2)+u']\sigma
          -sG\cdot[(X-uY)\times(Z_X-uZ_Y)]\}.
 \tag{HC.8}
\]

最后一项的整球半径至多
`abs(rho^2/v^2)*abs(s)*G0*(1+abs(u)^2)*z0`。保留 signed 前项和完整 actual 缺陷后才取负部。其余系数直接用完整向量 triple 求包围；没有复算旧 `(96,96),(96,97),(97,97)` 任一矩阵项。

原 high principal 误差严格使用 HP.2 的

\[
 \varepsilon_{\rm pr}=
       (2^{1/6}/32)\,388^{-4/3}\|a_{\rm pr}''\|_\infty.
 \tag{HC.9}
\]

## 5. mean 读出的完整一次分部积分

对原 high 输入 `z`，沿 HP.7 令

\[
 q=N^{-1/3}z,\quad R=JN^{-2/3}z,\quad T_s=JN^{-4/3}z,
\]
\[
 \mathbf e=\mathbf b'R+\mathbf c'T_s,\quad
 \ell_z=\mathcal D^{-1}\langle\mathbf e\rangle\cdot\ell,
 \quad\mathbf v=\mathbf e-g_m\ell_z.
\]

固定原 `nH=388`，记 `qH=nH^(-1/3),rH=nH^(-2/3),tH=nH^(-4/3)`。全部 high 背景乘法之前不移动投影。

对每个固定环境输出方向，周期分部积分和 `IR=N^(-5/3)z` 给

\[
 |\langle\mathbf b'R\rangle|
 \le\min(b_1r_H,b_2n_H^{-5/3})\|z\|_2.
 \tag{HC.10}
\]

这是对完整平均向量的算子范数估计：先与任一单位环境向量配对，再积分分部、取其上确界。没有将三个环境分量错误地视为独立行；同一个实际 `b2` 整向量范数控制所有方向。

因而可取

\[
 Y_H=k_0q_H+b_0r_H+c_0t_H,\quad
 E_H=b_1r_H+c_1t_H,
\]
\[
 L_H=\frac{20}{17}\{\min(b_1r_H,b_2n_H^{-5/3})+c_1t_H\},
 \qquad V_H=E_H+g_0L_H.
 \tag{HC.11}
\]

它们分别控制 `y,e,ell_z,v`。实际 `D>17/20` 来自完整旧 mean 证书；`g_m` 和独立 `mu` 仍完整，不把 `g_m` 当成零均值。`c'` 的平均项保守使用原完整范数，没有免费引入第三导。

## 6. 环境 primitive 的 near/far 收紧

本节的 `I` 始终是完整环境圆周的零均值 primitive，环境最低非零频率是 `1`。不能使用 scalar 四重的 `1/4`。

令 `M=388,L=194`，考察 `I M_(b') J N^(-2/3) P_H`。按环境输出频率分为 `abs(k)>=L` 与 `abs(k)<L`。近块的 `I` 范数至多 `1/L`。远块的乘子满足

\[
 \|P_{|k|<L}M_{\mathbf b'}P_{|l|\ge M}\|
 \le\min\{b_1,\sqrt2\,b_2/(M-L)\}.
 \tag{HC.12}
\]

为证明第二项，将高输入分成 `l>=M` 和 `l<=-M` 两个正交块。对每块，`D=-i partial_phi` 的输出、输入谱相距至少 `M-L`；相应压缩乘子 `B` 满足
`D_out B-B D_in=-i P_out M_(b'') P_in`。用两谱分离的半群积分解该 Sylvester 方程，得到每块范数至多 `b2/(M-L)`。两个输入的直和合成为至多 `sqrt(2)` 倍。第一项 `b1` 则是完整乘法算子范数。该证明允许三维环境输出，只用其整向量乘子范数，不额外乘环境维数。

近远输出正交，所以两费平方和。远块的 `I` 在非零输出上至多 `1`，其零输出由 `I` 定义准确去掉。因此

\[
 I_{b,H}=r_H\left[(b_1/194)^2+
     \min\{b_1,\sqrt2b_2/194\}^2\right]^{1/2}
\]
\[
 \boxed{\quad I_H=\min\{V_H,
           I_{b,H}+c_1t_H+g_0L_H\}\quad}
 \tag{HC.13}
\]

控制完整 `I v`。后两项各用环境 `I` 的范数 `1`，完整 `g_m ell_z` 没有删除。整个分解只对已知系数求导，不对未知高输入求导。`V_H` 是原完整界，因此取两上界的较小者仍严格。

## 7. 单侧高压缩下界与必要的源系数

由 HP.8 全部项和 `(HC.11)--(HC.13)`，新完整误差为

\[
 \varepsilon_{\rm loc}=
 A_{qq}^-q_H^2+A_{RR}^-r_H^2+A_{TT}^-t_H^2
 +|A_{Rq}|r_Hq_H+|A_{qT}|q_Ht_H+|A_{RT}|r_Ht_H,
\]
\[
 \varepsilon_m=2G_0g_0L_HY_H,\qquad
 \varepsilon_I=G_0I_HV_H+G_1I_HY_H.
 \tag{HC.14}
\]

系数都表示新全圈 sup 包围。于是

\[
 \boxed{\quad
 D_H\succeq\lambda_H I,\qquad
 \lambda_H=a_{\min}-\varepsilon_{\rm pr}
                  -\varepsilon_{\rm loc}-\varepsilon_m-\varepsilon_I.
 \quad}
 \tag{HC.15}
\]

报告的 `complete_actual_high_lower_bound` 是该明确算子下界的完整保存球，必须使用其下端；它不是声称实际最小特征值落在一个小区间内。若其下端未大于零，完整包围仍完成，而正性门为 false；不能因此声称 `D_H` 或实际 BVP 奇异。

同一新背景还支付 relative R.7--R.9 必要的 `chi0,chi1,||chi q0||L2,V0,V1,X1,|m|,1/|rho|`；`chi=u'/v`、`chi'=u''/v-u'v'/v^2`。`||chi q0||L2` 用全部闭格的完整平方上界之和后开根。新 `kappa=388^(-2/3) chi0` 的严格小于 `1` 门，仅给 relative 篇明确的 odd/even 两种 restriction 的 `L2` Neumann 逆；不表示已计算具体接收器 `W_L`。

为后继完整根源消元，另保存 F.2 的两列源系数。低列 `R=Jz_L`，故

\[
 L_L=(20/17)\min(b_1,b_2/4),\qquad
 C_{\omega,L}=b_0+b_1+g_0L_L,
 \qquad C_{\omega,H}=Y_H+I_H.
\]

低列的 `1/4` 只出现在 scalar `I R=N^(-1)z_L` 的系数平均分部积分中；不是环境 primitive 常数。再以已发表 F.4--F.7 的完整 `CV0,CV13,MG13` 定义

\[
 L_h=G_1C_{V,0}+2(20/17)G_0g_0,
\]
\[
 C_L=L_hC_{\omega,L},\quad C_H^{\times}=L_hC_{\omega,H},\quad
 C_q=M_{G,1/3}C_{V,1/3}+(20/17)G_0g_0C_{V,0}.
 \tag{HC.16}
\]

这五个源/列系数全部为新组合，使用完整新保存标量的回读端点。它们不授予所有根数据上的 `C_* ||H||^2` 费用；该全数据路线已被旧 signed negative result 排除。后继仍须完整 `W_L`、原 Y 的 `rE/rB` 及 relative 三门。

## 8. 保存、字段与运行范围

科学流程先保存 `complete_new_scalar_bounds` 和全部 receiver 背景球并读回。新 `a_min` 用下端，其余费用用上端；随后保存/读回所有 `YH/EH/LH/VH/IH` 和四项误差，再构成并保存 `lambda_H`。`kappa` 也先保存再严格比较。F.2 新系数只读前面已保存的 complete 上界，不用临时较小 midpoint。最终两个 gate 都使用完整保存球回读，不靠布尔标签、打印值或中心值。

完整输出恰为以下 `26` 个顶层字段；unfinished prefix 可只有其已完成子集：

`identity, complete, proved, failure, stage, completed_cells, old_axis_targets_called, old_mean_targets_called, old_X_targets_called, old_two_mode_matrix_entries_recomputed, old_ZP_propagations_called, old_geometry_targets_called, published_arrays, whole_original_references, scope, seconds, complete_new_scalar_bounds, complete_receiver_coefficients, complete_high_lower_bound_terms, complete_actual_high_lower_bound, high_lower_bound_positive, receiver_neumann_gate, complete_nonhomogeneous_source_coefficients, strict_gates_use_complete_saved_decimal_balls, private_geometry_only_for_new_scalar_targets, old_signed_two_mode_scope_preserved`。

最终 stage 为 `complete-new-original-high-root-lower-bound`。`complete/proved` 表示该完整新包围完成；高正性和 Neumann 资格分别用自己的严格 gate。`actual_positive_boundary_problem_singular/positive_inverse_proved/final_topic_complete` 保持 false；旧 signed negative scope 整份保留。

CLI 输入为 `--definition-source --candidate --germ --axis --axis-execution --mean --mean-execution --physical-budget --physical-execution --two-mode --two-mode-execution --output`。运行仅在原仓库公共 Actions，固定同原 Python/package 版本、四个数值线程变量为 `1`，不在本机执行科学。worker 恢复同六个原 blob，逐 current pin、历史原字节、参数/root interval/repair/原作用域核验；先 push consumed marker 后单 child，无科学自动重试，全部结果一次完整保存。失败保完整已成 prefix 与原失败原因。真实 pull、README 差异检查、topic `200000000` bytes 上限、非快进立即 rebase 重推均沿原已审核公共 worker。
