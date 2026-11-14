# 深尾可定量接入所需的最小量（待证接口，不是续接定理）

会话 Astra-visible-flex-950f9f73 / nonlinear_tail，2026-11-09。
本条只整理实际有限状态与已审 R46 之间的接口，并给出一个直接的周期引理。
未宣称当前有限远端 Robin 条件已等于非线性无限尾的边界图。

## 已有可用的实际输入

`2026-11-09-950f-audit-root-k6-m12-a0003.json` 独立重放了同一固定 metric
的 M12 / a=.0003 / rawDepth10 状态。其有限角多项式系数三角上界为

| raw cell | P | K | L |
|---|---:|---:|---:|
|6|4.4494e-6|6.0385e-4|6.0361e-4|
|7|6.8258e-11|1.7753e-8|1.7750e-8|
|8|8.6614e-16|4.4309e-13|4.4305e-13|
|9|8.7753e-21|8.9107e-18|8.9102e-18|

这里 P=z_theta/(r w)，K=(z_r-w)/w，L=K+P_theta，均包含已求出的平均根。
这些数仍只在径向采样点成立，浮点 Fourier 系数也未作区间包络。
它们支持从 raw cell 7/8 开始做有效估计；不能把 `minD=1` 的舍入显示当恒等式。

同一 M12 状态从 raw depth10 改到12后，cut 非均值一阶 jet 最大变化
1.734723475976807e-18，均值一阶 correction不变，physical fullD仍
1.6834720479e-9。此项只支持有限边界影响很小，不补全以下缺口。

## R46 不能直接充当现成 DN 定理

源：`../large-amplitude-twist-flex/results/R46-actual-r64-47-parameter-deep-tail.md`
第8至11节。它在 sufficiently deep 的固定 N 后使用

    X_(m,n) = (epsilon_bar delta_n^5)^(-1) exp(m tau_n) sign_(m,n) U_(m,n),
    tau_n = 1 + (n-N) log(2)/4,
    U=(Q,xi), Q=r^(-4) v_perp,
    xi_m=(C'_m/r^3-m^2 Q_m)/sqrt(12).

本数值 worker 的第二半状态是非线性 connection momentum Pi，不能直接当 xi；
须用真实 full-mean root 的 `toRaw` 或同等精确公式转换。

R46 给的是固定有限个不稳定谱坐标的解析族。稳定坐标与全部高频 trace 都由
无限 fixed point 决定，不是任意 full Fourier Dirichlet trace 的满射。故即使
一个有限节点的 P,K,L 很小，也没有自动证明它恰在该无限图上。
此外原结果的 spacing=2、rCuff约.9、wCut=.05 与本题 spacing=3、rCuff=.15、
wCut=.5 不同；本题6个控制谷和有限径向warp也必须计入有限头部。
原定理的巨大常数与非有效 N 不能仅换入本题幅度便宣称已经构造。

## 必须产出的五组可检查量

1. **连续径向、全角解析小球。** 在实际 raw N0=7或8的端口及后续全部cell，
   用精确几何和区间积分给出 Q、xi 的加权 Fourier l1 界（至少某个正宽度tau）。
   有限系数的三角界只是低频部分；须另有未表示频率的尾估计。
   单独的 P,K,L 小量可控制 D,S,A 的正性，但不替代带角导数的解析范数。

2. **真实线性 Green 界。** 对本题3Z模式与真实 finite head/profile 构造
   inward稳定图或 dichotomy 的有效逆界 B，包括谱投影的条件数；低频可作
   validated transfer，剩余无限高频须有统一解析衰减界。不能只记录标量
   m3 DN，不能用非正规矩阵的特征值模代替逆算子范数。
   R46 在2Z权重下有47个不稳定方向；3Z的方向数必须重算后采用。

3. **精确非线性余项常数。** 在上述小球半径rho上，验证完整含mean根的
   recurrence余项导数L(rho)，以及实际D,S,A的正下界。目标是有效
   B L(rho)<1，而不是只说“deep enough”。这里root cell7已显示约1e-8的
   相对扰动，可能允许远小于R46粗通用常数的实际局部界。

4. **候选到无限图的残差与修正界。** 对有限远端线性Robin条件产生的候选，
   计算完整全频边界缺陷 eta；证明 B eta + B L(rho) rho <= rho。
   这会得到真正无限尾及其端口非线性图/导数。有限头部和prefix必须随后对
   该图重新匹配，或用整个耦合系统的 a-posteriori 逆界一次修正。不能只把
   已经很小的 finite far trace 改成零、taper掉，或认作任意Dirichlet可续接。

5. **全cell的Cartesian C2趋零。** 给出非均值到二阶及均值一二阶的统一
   包络，使其随n趋零，并验证背景E''→0。R46第11节的有用模板是
   O(epsilon_bar (1+|log delta_n|)^15 delta_n^(3/2))，但常数要覆盖本几何。
   端点的超小height或P,K,L不足以排除极薄transition中的二阶峰。
   完整period与参数族上的同一收敛界也必须保留。

可先把2–4改写成对实际段射击残差的 Newton–Kantorovich / radii-polynomial
证书，从有限 head 的数值Jacobian和深尾解析bound拼装。它允许先用现有真实
候选而不要求原R46的任意Dirichlet满射；最终仍须给出完整无限维逆界。
这只是施工方案，五组量目前均未全部完成。

## 三重对称下的平移period引理

这一步不依赖半转对称。设平面development的一形式alpha满足
alpha(theta+2pi/3)=R_(2pi/3) alpha(theta)，且连接角在每个2pi/3扇区
增加2pi/3（例如连接系数2pi/3周期、完整平均holonomy=2pi）。
记一个扇区的平移向量为v；三个扇区的总平移就是

    v + R_(2pi/3)v + R_(4pi/3)v = 0.

因此对真实解，只要保持3Z对称与精确平均holonomy，完整水平平移period自动
闭合。数值有限mean root仅给舍入级近似，不能据此跳过精确mean方程。
此引理可替换R46中π周期用于平移闭合的那一步；不会自动转移其余谱/小量常数。
