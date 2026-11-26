# R142 补篇：对称部 coercivity 后的完整 source、193 atoms 与逐盒投影转授

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

**已证明下述 resolvent 转授；未计算新的对称部上界，未声明任何数值门已过。** 完整 signed-loop 和对称部上界由 R149 负责。本篇只给同一实际低193 BVP 在一个已付 resolvent bound 下的完整后继，以及显式纯 adapter。正在运行的 R142 源码、manifest、workflow 和原缺陷目标保持原身份。

配套纯模块：[fourfold_codazzi_low_centre_resolvent_lift_math.py](../scripts/fourfold_codazzi_low_centre_resolvent_lift_math.py)。

## RL1. 唯一的 body 算子与原完整缺陷

沿用 [R141](R141-low193-directed-green-and-complete-observation-certification.md) 的原 mixed boundary、155母格/实际细分、真实根与 ordinary $dr$。原 physical weight $S$、193 moving 坐标、独立 even mean、参数全族及真实 hybrid centre 均不改变。令

$$
 \mathscr H=L^2(I;\mathbb R^{193}),\qquad
 \Delta=A_L^c-\bar A,\qquad
 K=S\bar G\Delta S^{-1}:\mathscr H\longrightarrow\mathscr H .
 \tag{RL.1}
$$

这里 $\mathscr H$ 是经原 $S$ 加权后的 **body 空间**。root97 与 outer96 是另外的实际 trace receivers，不是 $K$ 的输入坐标，不加进本节的 adjoint。$S$ 逐段不连续并无问题：它只定义 body 范数，原 raw 解仍由原 Green 公式恢复，不能在 PDE 中未经付费地微分 $S$。

完整原 R142 给一条包含 $\|K\|$ 的上界 $\varepsilon$，以及原缺陷 atoms、源 covariances 和 body output covariances。下文不能把 $\theta$ 写进旧 $\varepsilon$ 字段，不能把原充分门的 false 改为 true，也不能从一种上界未过推断真实算子有核。

## RL2. 只需要实际 resolvent，不需要 Neumann 展开

设 R149 对同一完整 $K$、同一 Hilbert 内积证明

$$
 H=\frac{K+K^*}{2},\qquad
 \|H\|\le\theta<1.
 \tag{RL.2}
$$

则 $A=I-K$ 满足

$$
 \langle Au,u\rangle
 =\|u\|^2-\langle Hu,u\rangle
 \ge(1-\theta)\|u\|^2 .
 \tag{RL.3}
$$

从 Cauchy--Schwarz 得 $\|Au\|\ge(1-\theta)\|u\|$，故 $A$ 单射且像闭。同一计算对 $A^*=I-K^*$ 成立，故 $\ker A^*=0$；$\operatorname{Ran}(A)^\perp=\ker A^*$ 给像稠密。像同时闭且稠密，因而 $A$ 满射。于是

$$
 R\ge\|(I-K)^{-1}\|,\qquad
 R=\frac1{1-\theta}
 \tag{RL.4}
$$

是有效统一界。可使用更小的、另行严格认证的 $R$；当前配套 binder 只实施 (RL.4)。

这段证明不需要 $\|K\|<1$，也不要求 $K$ 对称、正定或正规。$H$ 的范数上界是充分条件；本篇未宣称当前真实 $K$ 满足它。若 $\theta\ge1$，只得到一条完整未过充分门的结果。

数值上先保存并读回完整 enclosing decimal ball 的 $\theta$，取其 upper endpoint $\theta_+$。binder 以

$$
 \gamma=(1-\theta_+)_{\rm lower}>0,\qquad
 R_+=(1/\gamma)_{\rm upper}
 \tag{RL.5}
$$

计算，且后继同时核 $\gamma\le1-\theta_+$、$R_+\ge1/\gamma$。任何后来保存造成的向外扩大必须保留这个方向，不能在隐藏的更有利数值上通过门。

## RL3. 原四 source 和全部193 atoms

对任一声明原 source $W$，沿用完整比较范数

$$
 g_B\ge\|S\bar GW\|,\qquad
 g_A\ge\|\mathcal O_A\bar GW\|,\qquad
 e_A\ge\|\mathcal O_A\bar G\Delta S^{-1}\|,
 \tag{RL.6}
$$

其中 $\mathcal O_Ax=(R_ax(a),\Theta R_bx(R))$ 保留全部97+96真实原子。

置 $u=Sx$。真实方程仍准确等价于

$$
 (I-K)u=S\bar GWf.
 \tag{RL.7}
$$

由 (RL.4) 得

$$
 b_W=R_+g_B,\qquad
 a_W=g_A+e_Ab_W,\qquad
 \|\mathcal OG_LW\|\le\sqrt{b_W^2+a_W^2}.
 \tag{RL.8}
$$

第二式来自 raw 解恒等式 $x=\bar GWf+\bar G\Delta S^{-1}u$。右侧由 ordinary $L^2$ 源经 $\bar G$ 得到，因此 $x$ 是原 $H^1$ 解，真实 traces 有定义，全部原 transmissions 与 mixed boundary 保留。没有从任意 $L^2$ 输入读取端点。

这同时适用于：

| 原 source role | 保留的准确 raw source |
|---|---|
| ordinary_raw_low_source | $I_{193}$ |
| transformed_low_source | $S^{-1}$ |
| low_second_kind_correction | $(A_L^c-D_f)S^{-1}$ |
| centre_high0_return_source | 原 $A^c_{LH}$ 的97..160完整128输入列 |

这些仍各自需要其全部真实 source packets、body Gram 和193 atoms；仅有 $R_+$ 不会补出它们的数值。若保留 root 与 outer 两个 receiver 分开求界，同理分别使用原 $e_a,e_R$：

$$
 a_{W,a}=g_{W,a}+e_ab_W,\qquad
 a_{W,R}=g_{W,R}+e_Rb_W .
 \tag{RL.9}
$$

因此后继 physical58 的分端点公式不依赖 Neumann 展开，原缺陷两个完整 HS平方仍须如实消费。

## RL4. 完整增广第二类逆仍是同一恒等式

R141 的增广空间为 $\mathscr Z=\mathscr H\oplus\mathbb R^{193}$，原 $H_L$ 只读 body 输入。其严格代数恒等式

$$
 (I-H_L)^{-1}h
 =h+\mathcal OG_L(A_L^c-D_f)S^{-1}h_B
 \tag{RL.10}
$$

只要求真实 $G_L$ 已存在。推导不展开 $\sum K^n$，不对 $h_B$ 求导，也不删除任一独立 atom 输入。

所以当该 correction source 的 (RL.8) 为 $b,a$ 时，仍有

$$
 \|(I-H_L)^{-1}\|
 \le\frac{\sqrt{(2+b)^2+a^2}+\sqrt{b^2+a^2}}2 .
 \tag{RL.11}
$$

这只是原 $2\times2$ 块上界 $\bigl\|\begin{smallmatrix}1+b&0\\a&1\end{smallmatrix}\bigr\|_2$ 的显式值；唯一改变是 $b,a$ 由 (RL.8) 支付。不能把 $R_+$ 本身直接当成含193 atoms 的这个二类逆。

## RL5. 全盒投影保留原 point receiver 与 point column

沿用 R141 (G.34)--(G.38) 的完整 whole-box 数据：

$$
 a_J\ge\sup_{r\in J}\|u\mapsto(Ku)(r)\|,\quad
 b_J\ge\sup_{s\in J}
 \|v\mapsto S(\cdot)\bar G(\cdot,s)S(s)^{-1}v\|,\quad
 p_J\ge\sup_{r\in J}\max_\alpha\|\bar P_\alpha^S(r)\|.
 \tag{RL.12}
$$

$a_J$ 使用原 true-coefficient-defect 的完整源 covariances，$b_J$ 使用原比较 Green 的 body-only output covariances。它们由全格 PSD 外包控制实际部分积分，所以对整个闭盒成立。

不论逆是怎样严格支付的，都有准确 resolvent identity

$$
 SG_LS^{-1}
 =S\bar GS^{-1}
 +K(I-K)^{-1}S\bar GS^{-1}.
 \tag{RL.13}
$$

固定一个 point source，其比较列属于 $L^2$；固定输出点，$K$ 的该行是 (RL.12) 的有界 receiver。因此对 correction kernel，

$$
 \sup_{r,s\in J}\|\mathrm{correction}(r,s)\|
 \le a_JR_+b_J.
$$

沿对角两侧取极限，得到

$$
 p_J^{\rm true}\le p_J+a_JR_+b_J.
 \tag{RL.14}
$$

原 $S$ 到 raw 的系数和 matching 下界照旧：

$$
 p_{J,\rm raw}^{\rm true}
 =\max(1,q_i)\max(1,q_i^{-1})(p_J+a_JR_+b_J),\qquad
 \sigma_{\min}(\widehat L,\widehat R)
 \ge\frac1{\sqrt2\,p_{J,\rm raw}^{\rm true}}>0.
 \tag{RL.15}
$$

**$\theta$ 不是 point norm。** 它不替换 $a_J$、$e_A$、$b_J$ 或任何真实 covariance。$\varepsilon$ 和 $\theta$ 同样不提供 $L^2\to C^0$ 免费估计。实际 owner 必须仍完成全部原5696盒或其明确更新后的全覆盖。

## RL6. 与正在运行 owner 的精确对应

已经定点核读如下当前源码（R142 owner blob83dcab56、Green core1346cfb0、local adapter78afd2f9）：

- R142 owner 在完整 defect 后单独测试保存的 $\varepsilon<1$；未过即结束其一目标完整 false 分支。这一原行为和结论不变。
- Green core 的 actual_low_source_bound 除严格 gate 外，只将 $1/(1-\varepsilon)$ 用于 body；atoms 加原缺陷 receiver 乘该 body。
- 其 correction source 的第二类逆只使用完整 body/atoms，公式为 (RL.11)。
- whole_box_projection_bound 除原 gate 和同一 $\varepsilon$ 的身份检查外，只在 (RL.14) 的位置使用 $1/(1-\varepsilon)$。全部源 covariance、output covariance、actual $S$ 和点因素均独立保留。
- physical58 的 complete_new_scalar_closure 不再使用 $\varepsilon$。它消费实际四源 body/atoms 及原 defect root/outer HS平方；这些改由 (RL.8)--(RL.9) 合法供给后，其58个 scalar 公式不需改变。

纯 adapter 新增三个明确入口：bind_symmetric_part_resolvent、actual_low_source_bound_from_resolvent、whole_box_projection_bound_from_resolvent。没有 monkeypatch 或修改旧函数。

与 R149 统一的输入 schema 为 kind=R149_complete_weighted_body_symmetric_part_v1、source_role=true_coefficient_defect、同一个 private_model_token、symmetric_part_norm_upper、symmetric_part_HS2_upper、complete_signed_trace_of_square=True、complete_cells、whole_saved_norm_readback_used=True。完整 trace ball 和原 body_HS2_upper 另保留以证明数值来源。

binder 独占生成 kind=R142_same_model_symmetric_part_resolvent_v1、basis=symmetric_part_coercivity、coercivity_gap_lower 和 resolvent_norm_upper。它保留 comparison_defect_body_upper=$\varepsilon$ 与 strict_low_coefficient_residual_passed 的原真假，并另给 strict_symmetric_part_gate_passed。任何后继 new-kind 都不得把这两门混成一门。

## RL7. 最小必要的后继身份变更，不扩大已付范围

若实际 R142 得到完整 $\varepsilon$ 但原门未过，且新的完整 R149 另行证明 $\theta<1$，最小后继仍必须：

1. 消费原 R142 完整实际 scientific/execution/manifest 与原 Green prefix；原已完成目标不重新登记。缺失私有载体若必须物化，如实作为新目标依赖，不宣称恢复了从未保存的载体。
2. 以新 kind 登记独立的对称部成功目标；原 $\varepsilon$ 及 false 门保持原身份。随后只有四源和全部193 atoms、完整 whole-box transversality 实际完成，才可给新的完整低逆结果。
3. 在 physical consumer、physical owner 和 physical manifest generator 各增加显式新 kind 分支。旧两种低证书的 strict-low 检查原样保留；新分支核完整独立对称部证书和 (RL.8)--(RL.15)，不得伪装为旧 R142 六个成功目标。
4. physical58、ports224、WPN32 继续只消费真正完整前驱。全高反馈、实际族差、真实物理外行、原七独立输入、负侧返回和非线性完成标准仍分别支付。

本篇仅证明这一数学转授并提供纯定义。未启动新的科学，未声称 R149 已有完整实际输出；$\theta\ge1$、输入缺失或 source/point 未完均不得获得 actual-low 完成状态。
