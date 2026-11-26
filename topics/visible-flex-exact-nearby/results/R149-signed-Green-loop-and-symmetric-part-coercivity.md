# R149：同一低193缺陷的有符号闭环迹与对称部逆门

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

**已证明：** 原完整 defect Green 的一个不同充分门、其全区间有符号闭环
迹公式和线性格数递推。配套纯算法不导入数值库、不读写文件、无执行入口。
它不修改正在运行的 R142，不重算已经完整保存的 Hilbert–Schmidt 上界，
也不在新有符号量尚未实际完成时宣称逆已成立。

本篇对象仍为 [R141](R141-low193-directed-green-and-complete-observation-certification.md)
的完整 WVC hybrid 低193算子。原实际参数域、真根长度、全部 mean、
root97/outer96、ordinary dr、实际 S 和边界(G.2)保持。
它不是整个真实 DF(Qrepair)，也没有支付完整 CFB、物理外块或其余端口。

## 1. 在完全同一个 Hilbert 空间取伴随

取原实 Hilbert 空间
$\mathscr H=L^2([r_*,R],dr;\mathbb R^{193})$，使用原归一正弦、独立 even
mean 和归一余弦的正交坐标。设

$$
\Delta(r)=A_L^c(r)-\bar A(r),\qquad
\mathcal K=S\bar G\Delta S^{-1}:\mathscr H\to\mathscr H .
\tag{HL.1}
$$

$S_i=\operatorname{diag}(I_{96},q_i,q_iI_{96})$ 是原正权。
这里 $\mathcal K$ 仅以 body 为输入和输出；原193个 atoms 已通过 $\bar G$
的真实 mixed boundary 进入核，后文还分别保留它们的输出估计。

有限区间上原完整 Green 和 $\Delta$ 分片有界，故 $\mathcal K$ 是
Hilbert–Schmidt。其伴随取于上述同一 dr、同一193坐标，而非 raw x
空间、不同权空间或 body-plus-atoms 空间。令

$$
\mathcal H_{\mathcal K}=(\mathcal K+\mathcal K^*)/2.
$$

则准确有

$$
\boxed{\quad
\|\mathcal H_{\mathcal K}\|_{\mathrm{HS}}^2
=\frac{\|\mathcal K\|_{\mathrm{HS}}^2+
              \operatorname{Re}\operatorname{tr}(\mathcal K^2)}2.
\quad}
\tag{HL.2}
$$

本题实实现的 trace 为实数；若将来使用复 Fourier，实现中仍必须取 Re。

**证明。** Hilbert–Schmidt 算子的两个乘积为 trace class。
展开 $(\mathcal K+\mathcal K^*)^2/4$，使用
$\operatorname{tr}(\mathcal K\mathcal K^*)
=\operatorname{tr}(\mathcal K^*\mathcal K)=\|\mathcal K\|_{\mathrm{HS}}^2$，
以及 $\operatorname{tr}((\mathcal K^*)^2)
=\overline{\operatorname{tr}(\mathcal K^2)}$，即得。
也可对有限秩核先证，再以 Hilbert–Schmidt 极限通过。证毕。

## 2. 新充分门及已有完整 HS 上界的使用方向

设已经完成的原记录给
$E_+\ge\|\mathcal K\|_{\mathrm{HS}}^2$，新完整有符号记录给
$T_+\ge\operatorname{Re}\operatorname{tr}(\mathcal K^2)$。则

$$
c_+=\operatorname{upper}\bigl((E_++T_+)/2\bigr),\qquad
\kappa_+=\operatorname{upper}\sqrt{c_+}
\tag{HL.3}
$$

给 $\|\mathcal H_{\mathcal K}\|\le\kappa_+$。
合法完整输入必有 $c_+\ge0$；负的 upper 是输入/包围错误，不能用于宣告成功。
原 R142 的完整 body_HS2_upper 可直接作为 $E_+$。仅有一般算子范数 upper
时，不能把其平方冒充 HS 上界；R142 的 body_norm_upper 之所以可平方，
只因其已证明是该完整 HS 平方上界的平方根。

先保存新 trace 的整个 signed decimal ball 并读回 upper，后形成(HL.3)；
再保存 $\kappa_+$ 整球、读回 upper，最后检验

$$
\boxed{\quad \kappa_+<1,\qquad g=1-\kappa_+>0.\quad}
\tag{HL.4}
$$

没有从旧 HS upper 倒推出新 trace，未将 abs(trace) 用作有利符号。

**命题。** (HL.4)成立时，$I-\mathcal K$ 在 $\mathscr H$ 上可逆，且
$\|(I-\mathcal K)^{-1}\|\le g^{-1}$；无需另有
$\|\mathcal K\|<1$。

**证明。** 对任意 $u$，

$$
\langle(I-\mathcal K)u,u\rangle
=\|u\|^2-\langle\mathcal H_{\mathcal K}u,u\rangle
\ge g\|u\|^2.
$$

有界实双线性型因此满足 Lax–Milgram 的完整 coercivity，给每个右侧的唯一解
及上述范数界。等价地，可先由该不等式得到闭值域和单射，再对伴随使用同一
对称部排余核，得满射。证毕。

这是不同于旧 Neumann 门的充分条件。若旧 $\epsilon<1$ 已完整成功，不为
“优化”重跑旧目标；若旧门完整失败，新的 trace 是一个真正不同的目标。
新门失败也只表示该证书没有闭合，不能推断实际 BVP 奇异。

一个纯解析符号校验表明这不是旧门改名：在两分量、零比较生成元、
$x_2(0)=x_1(L)=0$ 的例子取
$\Delta=\left(\begin{smallmatrix}0&d\\d&0\end{smallmatrix}\right)$。
令 $Vf(r)=\int_0^r f(s)\,ds$，则
$\mathcal K=\left(\begin{smallmatrix}0&-dV^*\\dV&0\end{smallmatrix}\right)$
严格反自伴，所以对称部为零，而 $\|\mathcal K\|$ 可任意大。
直接全矩形积分给 $\|\mathcal K\|_{\rm HS}^2=d^2L^2$、
$\operatorname{tr}(\mathcal K^2)=-d^2L^2$，恰合(HL.2)、(HL.8)的负号和因子2。
这只是公式校验，不是本题193维实际数值或删 mean 的依据。

## 3. 同输入闭环中的 S 准确相消

沿 R141 G.12–G.15，$L,\ell$ 的维数为193乘97、97乘193，
$R,\rho$ 为193乘96、96乘193，$C_i=U_i^{-1}$、$D_i=V_i^{-1}$。
对 source $s\in I_i$、output $r\in I_j$、$i<j$，准确有

$$
\begin{split}
K(r,s)&=S_j R_j(r)(D_{j-1}\cdots D_i)
       \rho_i(s)\Delta(s)S_i^{-1},\\
K(s,r)&=-S_i L_i(s)(C_i\cdots C_{j-1})
       \ell_j(r)\Delta(r)S_j^{-1}.
\end{split}
\tag{HL.5}
$$

乘积中先有相邻的 $S_i^{-1}S_i=I$；取193维循环迹再消去
$S_j^{-1}S_j$。定义两个**同点、有符号**矩阵

$$
A_i(s)=\rho_i(s)\Delta(s)L_i(s)\in\mathbb R^{96\times97},
\qquad
B_i(r)=\ell_i(r)\Delta(r)R_i(r)\in\mathbb R^{97\times96}.
\tag{HL.6}
$$

得到

$$
\operatorname{tr}(K(r,s)K(s,r))
=-\operatorname{tr}\!\left[
 (D_{j-1}\cdots D_i)A_i(s)
 (C_i\cdots C_{j-1})B_j(r)\right].
\tag{HL.7}
$$

既没有交换非交换因子，也没有把两个不同源的输出假设成正交。
同 cell 时两个 transfer 空乘积为 identity，公式保留。
与 r,s 互换后的 trace 由循环性相同；对角集合 dr ds 测度为零。因此

$$
\operatorname{tr}(\mathcal K^2)
=-2\int_{s<r}\operatorname{tr}\{\text{(HL.7)中不带负号的乘积}\}\,ds\,dr.
\tag{HL.8}
$$

Hilbert–Schmidt 的 Cauchy–Schwarz 使这个双积分绝对可积。
它是一个 signed ordinary source 目标，不添加或删除任何接口 atom。

已有完整 local_factors 可以准确消费同一 raw 源
$W_\Delta=\Delta S^{-1}$，此时

$$
A_i(s)=I_{R,i}(s)O_{L,i}(s),\qquad
B_i(s)=I_{L,i}(s)O_{R,i}(s).
\tag{HL.9}
$$

这里的两个 S 都在**同一实际点**，是(HL.6)的同一个对象。
whole-box interval products 可保守包围它，不能用各自旧范数重建 signed
矩阵。对 ordinary_raw、second-kind 或 high0-return 角色，不可套用本 trace
作为(HL.1)的证据。

## 4. 全域只携带一个96乘97矩阵

定义完整 signed 单格积分及同格三角

$$
a_i=\int_{I_i}A_i(s)\,ds,\qquad
b_i=\int_{I_i}B_i(r)\,dr,\qquad
t_i=\int_{I_i}\int_{I_i\cap\{s<r\}}
                  \operatorname{tr}(A_i(s)B_i(r))\,ds\,dr.
\tag{HL.10}
$$

从 $X_0=0_{96\times97}$ 递推

$$
\boxed{\quad
X_{i+1}=D_i(X_i+a_i)C_i.
\quad}
\tag{HL.11}
$$

则完整闭环积分与平方迹为

$$
\boxed{\quad
\mathcal L=\sum_i\{\operatorname{tr}(X_i b_i)+t_i\},
\qquad \operatorname{tr}(\mathcal K^2)=-2\mathcal L.
\quad}
\tag{HL.12}
$$

**证明。** 归纳展开得到
$X_j=\sum_{i<j}(D_{j-1}\cdots D_i)a_i(C_i\cdots C_{j-1})$。
不同 cells 天然满足 s<r，积分可分离成各自完整 signed 矩阵积分，得离格项；
同格部分正是 $t_i$。再用(HL.8)。证毕。

每次先加 $\operatorname{tr}(X_i b_i)+t_i$，再更新 X。
trace 直接作96乘97个 entry 乘积之和，无须为一个 trace 作完整 dense 乘法。
只持有当前 cell 的 subboxes、a、b及一个 X；不建立平方格数 kernel 表。
Uinv/Vinv 和当前独立节点均来自同一完整 comparison Green。

## 5. varying Δ 的合法 whole-box signed 积分

每格取准确归一 cuts $0=\tau_0<\cdots<\tau_v=1$。
在每个**整个闭子格**上形成(HL.9)的矩阵球
$\mathbb A_\alpha,\mathbb B_\alpha$，包含所有原允许参数和每个真实半径。
真实 mass 为 $\mu_\alpha=h_i(\tau_{\alpha+1}-\tau_\alpha)>0$。

完整 a、b 由 $\sum_\alpha\mu_\alpha\mathbb A_\alpha$、
$\sum_\alpha\mu_\alpha\mathbb B_\alpha$ 包围。三角由

$$
\sum_{\alpha<\beta}\mu_\alpha\mu_\beta
  \operatorname{tr}(\mathbb A_\alpha\mathbb B_\beta)
+\sum_\alpha\frac{\mu_\alpha^2}{2}
  \operatorname{tr}(\mathbb A_\alpha\mathbb B_\alpha)
\tag{HL.13}
$$

作完整 interval enclosure。每一个不同子格矩形完整保留；
同子格只用其真实三角面积1/2，但 integrand 在整个闭矩形上包围两独立变量。

这里没有把整个 varying $\Delta(s)$ 的 ball 视为一个恒定未知矩阵。
矩阵球每次出现可以保守地失去相关性，但必须包含真正同一个参数下的函数值。
不得先对 signed integrand 取 abs、positive part 或丢负号。

**长度必须保整个正 ball。** 对有符号积分，只把 mass 换成 upper 后相乘
一般不合法；负 integrand 会把所需方向翻转。配套纯算法以完整
$h_i$、$\mu_\alpha$、$\mu_\alpha\mu_\beta$、$\mu_\alpha^2/2$ 运算，
最后才对整个 trace 的完成球取 upper。首格仍是真根长度，
不是 padding 区间宽度或 root midpoint 长度。

原 raw transmissions 是 identity；旧有限接口的普通积分测度为零。
若处理新的独立 affine jump input，仍按原单独 port/lift，它不属于本次
$\Delta(r)dr$ 的 kernel trace。

## 6. 新 gap 接回真实低逆，全部 atoms 和 source 保持

原方程仍为 R141 G.29：
$u=S\bar G Wf+\mathcal K u$。用(HL.4)得

$$
\|SG_LW\|\le g_B/g,\qquad
\|(R_a\operatorname{ev}_{r_*},\Theta R_b\operatorname{ev}_R)G_LW\|
 \le g_A+e_Ag_B/g.
\tag{HL.14}
$$

其真实 H1 资格仍由
$x=\bar G Wf+\bar G\Delta S^{-1}u$ 得到，因而 atoms 是真实 trace。
原 root97（包括 mean）与 outer96 全部留在 e_A、g_A；没有 mean-output
等于零的假设。特别，HIGH0 local source 的 mean 行为零，不允许推出
完整 Green 输出或低 defect 的 mean 行为零。

R141 G.31–G.32 的增广二类逆、G.39 的 whole-point 投影界及 G.43 的独立
边界 lift 只使用 $(I-\mathcal K)^{-1}$ 的范数界，故其分母可统一换为 g。
例如 whole-point 修正仍为 $a_Jb_J/g$；a_J、b_J、p_J 必须各自完整已付。
source 四列、193 atoms、全部 boxes 未完成时，单独(HL.4)不授其数值。

实现应登记 strict_symmetric_part_gate_passed，而不是把旧
strict_low_coefficient_residual_passed 改成 true。旧 $\epsilon\ge1$ 的实际
记录保持原样。原高反馈 CFB、实际 physical 外块、finite rho桥、七端口、
两 RHS、负侧/mean/ν 和非线性完成标准继续按原真实对象支付。

## 7. 配套纯算法及实际执行边界

fourfold_codazzi_low_centre_signed_loop_math.py 提供：

- panel_loop_packet：完整 source role 与闭子格的(HL.9–HL.13)；
- complete_loop_trace：所有实际 cells 连续齐全后才给(HL.12)；
- coercivity_quantities：只读旧 HS upper 与新完整 trace，形成(HL.3)；
- admit_saved_symmetric_part：核 owner 保存、读回的新完整 norm ball 包含整个已算 upper。

该最后输出 kind=R149_complete_weighted_body_symmetric_part_v1，含同一
source_role、private_model_token、symmetric_part_norm_upper、
symmetric_part_HS2_upper、complete_signed_trace_of_square=true、
complete_cells 及 whole_saved_norm_readback_used=true。完整 signed trace
另存 complete_trace_square_ball；它不是上面那个 boolean。
独立 [R142 同模型 resolvent adapter](R142-supplement-coercive-resolvent-complete-source-and-point-lifts.md)
及其 [纯模块](../scripts/fourfold_codazzi_low_centre_resolvent_lift_math.py)
由此检查严格门、形成 gap 与 resolvent，
再按(HL.14)转授四源、193 atoms 和全 point 窗；本模块不重复这些旧算式。

owner 可显式提供同一定义的 child coefficient provider 和缓存的 directed
local factors；不得猴补 active run、偷换实际源、把真实参数当径向任意控制，
或从旧标量重构未保存的 signed carriers。必要的同模型内部物化按 R142
第4节如实记录，不登记第二个旧 Green/HS 结论。

本篇没有生成新的 trace 数值，没有运行新 public science。
只有实际全区间新 scalar 完成后，才有该新充分门的通过或失败结论。
