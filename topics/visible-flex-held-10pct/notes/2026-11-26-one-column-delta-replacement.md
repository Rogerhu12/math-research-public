# 同一实际基点上，首相位列换成 δ 列的最小诊断

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

本条只给源代码所支持的条件代数与下一次需要诊断时的最小计算。
没有组装新矩阵、求 LU、重跑旧方向或启动新 job；目前没有本条 γ 的实测值。
它不把已完成的 v3 方向当成 v4/v5 的方向，也不据 R72 预判有限幅可逆。

## 1. 必须先成立的共同输入

要比较的两个局部问题是：

* 相位问题：固定当前实际 g，未知 p₀ 为首 phase 坐标，以及共同高 phase 参数；
* 设计问题：首 phase 固定为0，首未知改成原物理 δ 的加性增量，高 phase 参数不变。

比较必须在**同 λ、完整 R53 baseline support 向量与窗口 S/b/k、当前实际 δ/g、
数值 gauge、warp、完整 R70 phase_basis、phase_scale、M、angular、原线性 port、
BC normalization、literal mean 规则、同一 raw t 网格和同一 Y**上进行。
基点须 `d1=0`：在 v4 原坐标中 p₀=0、q_aux=gauge；在 v5 中 p₀=δ_actual−δ_base。
高参数也要有相同物理语义、相同完整向量和 `max(gauge**j,1e-9)` 尺度。

同一个几何核本身不足以推出整个残差或 J 同一。还必须保留字面的
`chart_join/chart_reference_prefix/chart_breaks`、实际 s(t)/ds(t)、原完整参考
lift 系数1与其原入口投影、convection 项及末端 BC。两套计算产生的不同 mesh、
初猜、mean 或刚被更换的 g，不能直接放进一列替换公式。

若后来 v5 已选出不同 δ，旧 v4 接受记录仍绑定旧 g，不能改其标记冒充新 g。
只有在当前实际 δ 上另行明确声明局部比较的固定-g 方程、并核下述共同算子关系后，
才可使用本条。那份局部比较定义不是另一个已接受场，也不绕过现有 loader 的来源检查。

## 2. 源码怎样支持共同算子关系

以下当前课题代码路径以本课题目录为根；未重复写目录的 warm 文件均在
`scripts/resume_20261126/`。旧 source 明列恢复包内的原路径。

1. `scripts/resume_20261126/warm_delta_phase_factory_v5.py` 第53–85行复用同一
   v4 factory，固定 q=gauge，仅将禁止的首 API jet 置零；高 phase 的值和参数链不变。
   SHA `56772568ba9ddbfcf78d65cb0104991b694a4806335914762158a58d2391fc83`。
   R70 的实际公式仍来自 `warm_homotopy_core_factory_v4.py`，
   SHA `f303897c231639b2dd68854d7bf37cc8862eea4e52b468d5be84c856e84fbcb5`。
2. `warm_fixed_m3_model_v4.py::build_model` 用 `fixed=True` 和实际冻结 profile，
   再还原字面的原 radial chart，mean1168/BC=.02；
   SHA `5eb1a30dc861747bde158315b845a62bf666c32ad1b59a033daeafe41da7fabe`。
   v5 entry 用原 `physical_profile`、真实 raw p₀、`fixed=False` 构造；
   SHA `4628b1431b8d09ad661766012b50462dcdbfc1469c23c2b2f9f2f41e26332ba8`。
   这两种构造只有在当前实际 δ 和 literal chart 确实相同时才是共同基点。
3. `scripts/resume_m3/round_raw_lib/exact_core_lift.py::install_core_lift`
   共同使用完整 H/H₁/H₂、入口投影和 aχ、(aχ)'、(aχ)''；SHA
   `28936553078df9d1a2c6486fab1613c20fd7cfdb9b4134d4c95e1d60fa5623f5`。
   `geo` 与 `LiftBVP.initial/fun/terminal` 明确决定这些项如何进入完整方程。
4. `scripts/resume_m3/round_raw_lib/analytic_adaptive_core_jac.py` 第11–24行共同计算状态导数和
   高 phase 导数，包含入口投影扣除以及 `v*d1` convection；两分支的高列都乘
   相同 pscale。第25–26行仅在 `fixed=False` 时把第0列换成对完整 `self.fun`
   的 δ 中心差分；SHA
   `da6690d9f11eac38cec0acee31aa07555a8d1ddd81c1b24997db0421ea19e431`。
5. 恢复 source 的原目录为 `topics/visible-flexible-closed-surface/`。
   其中 `scripts/950f-prefix-warped-bvp.py::initial` 第116–127行在 fixed=False
   时不把 p₀送入 core；`notes/fixed_metric_mode3_bvp.py::SupportBVP.flow/chart`
   第55–62、85–92行则通过 baseδ+p₀ 改完整物理 profile 与径向坐标。
   warped 与 `scripts/950f-prefix-adaptive-chart-bvp-v2.py` 两层重新建立正确 Flow/fixed_flow，
   `frame/adapt_fun/adapt_fun_jac` 由共同 g、lift、Y 和 angular 决定。
   原三件文件属于既有恢复 manifest；其中 SupportBVP 源 SHA 为
   `e2e5cf08339c82fac24ef296dc721cec4e43852d2a6d963721ce69a1d8d7a11c`。

因此，在这些实现所定义的共同允许域内，若两支构造确实满足第1节的条件，则
沿 `d1=0` 且固定 δ=δ_actual 的共同切片，**整个**计算 RHS、入口、末端 BC
作为 (Y,p_high) 的函数相同；不仅是 core.evaluate 相同。于是数学状态列和
高参数列相同。有限程序还须在实际使用点核：完整残差、节点/中点 RHS、s/ds、
入口及 BC，以及状态/高参数 Jacobian 块同一；不能把这一待核身份先记为实测通过。
若只有近似相同，则 J_new=J+单列更新不是严格身份，须保留其余块差，不能漏掉。

## 3. 完整 collocation 参数列，包括中点链

设每个状态有 n=3M+1 个分量，raw 网格有 m 个点。以原计算 t 为自变量，
相邻间隔 h_i=t_(i+1)−t_i，节点 RHS 为 f_i=f(t_i,Y_i,p)。SciPy 的中点状态为

\[
Y_{i+1/2}=(Y_i+Y_{i+1})/2-\frac{h_i}{8}(f_{i+1}-f_i),
\]

collocation 行为

\[
C_i=Y_{i+1}-Y_i-\frac{h_i}{6}(f_i+f_{i+1}+4f_{i+1/2}).
\]

对任一参数 τ，在节点 Y 固定时令 b_i=∂_τf_i、
b_mid=∂_τf(t_mid,Y_mid,p)、A_mid=∂_Yf(t_mid,Y_mid,p)，则

\[
\partial_\tau Y_{mid}=\frac{h_i}{8}(b_i-b_{i+1}),\qquad
\widetilde b_{mid}=b_{mid}+\frac{h_i}{8}A_{mid}(b_i-b_{i+1}),
\]

\[
\boxed{\partial_\tau C_i=-\frac{h_i}{6}
  (b_i+b_{i+1}+4\widetilde b_{mid}).}
\]

这正是 SciPy `construct_global_jac` 的
`T=stacked_matmul(df_dy_middle,df_dp[:-1]-df_dp[1:])`、
`df_dp_middle += .125*h*T` 和后续 `-h/6` 行。
本地实际读到的 SciPy1.17.0 `_bvp.py` SHA 为
`59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2`，
`construct_global_jac` 从159行、`collocation_fun` 从277行起。
这不是声称 runner 必为该版本；实际诊断应继续像已部署
`seam_probe_original_newton_direction.py` 第243–251行一样绑定其真实
`_bvp.__file__`/SHA 与实际 private signature，再使用该源码的原装配。

δ 的节点和中点 b 均须取**完整**计算 RHS 的原 δ 列。现原步长为
`2e-6*max(.1,actual_delta)`；它包含 profile、s/ds、lift 和 convection。
不能用物理 s 固定的偏导替代计算 t 固定的偏导，也不能只填入口的 δ 响应。

完整底部 BC 为
\(B(Y_0,Y_1,p)=(Y_0-I(p),\,T(Y_1,p))\)，所以参数列还必须接
\((-I_\tau,T_\tau)\)，使用原归一化后的 terminal 行。
原 `SupportBVP.bc_jac`/`WarpedBVP.bc_jac` 的 actual `P[:,0]` 是本次 δ 列来源，
不可因一个抽象端口论证直接删掉 BC 行。该多段模型的 cut/bridge 数据固定、
lift 在 cut 平掉、入口 δ 无关，解释了原代码的第0个 BC 列为零；参见 R72。
若实际比较的 BC 或均值规则改变，这个零列结论须重新核对。

按原存储序：前 n(m−1) 行是按 F-order 展开的 collocation，之后 n 行入口，
最后 M 行 terminal；前 nm 个未知为节点 Y，最后 M 个为参数。
全矩阵维数是 N=nm+M，首参数列的零基索引是 i=nm。

## 4. 一次转置解得到精确兼容泛函

本节的矩阵恒等式适用于上述原程序实际装配的有限矩阵及δ差分列。第3节链式公式在精确偏导下为解析身份；以原中心差分列代入，并不认证连续问题的精确Fréchet导数或该差分的截断/舍入误差。

令 J 是共同基点上相位问题的完整可逆矩阵，b₁=Je_i 为首 phase 参数列，
b_δ 为上一节正确装配的 δ 列。若其余块身份已付，则

\[
J_\delta=J+(b_\delta-b_1)e_i^T.
\]

用已有同一个 LU 解

\[
J^Tw=e_i,\qquad \gamma=w^Tb_\delta.
\]

由 wᵀJ=e_iᵀ，w 消掉所有状态列及高 phase 列，而 wᵀb₁=1。这就是当前
离散问题中可直接测量的独立兼容泛函，不是维数计数。矩阵行列式引理给出

\[
\det J_\delta=\gamma\det J.
\]

故在这些精确代数前提下，列替换后可逆当且仅当 γ≠0。
若原 r=F(z)、d=J⁻¹r，则设计方向首参数满足
\((d_\delta)_i=(w^Tr)/\gamma=d_i/\gamma\)。原 Newton 更新符号仍为减号。

需要整个新方向时，只再解一次 t=J⁻¹b_δ，不另分解矩阵：

\[
\boxed{d_\delta=d-(t-e_i)\frac{d_i}{\gamma}.}
\]

可直接核 \(Jd_\delta+(b_\delta-b_1)(d_\delta)_i-r\)。这是
Sherman–Morrison 的本题一列形式；若 γ 太接近数值误差，不能凭一个非零
binary64 数断言连续或有限精确矩阵已可逆。

若再假定状态块 A 可逆，将 J 分为
\(\left[\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right]\)，则
\(S=D-CA^{-1}B\)、
\(s_\delta=(b_\delta)_{\rm terminal}-CA^{-1}(b_\delta)_{\rm interior}\)，且
\(\gamma=e_1^TS^{-1}s_\delta\)。这是 R72 所述端口响应的有限 Schur 解释。
本诊断**不需要**额外假设或求解 A，也不需要生成整个 Schur 矩阵/SVD；
上面的全 J 转置式已经足够。

## 5. 单位、误差与下一次最少输出

γ 是“首 phase 坐标变化/物理 δ 变化”的响应系数。若把 δ 的坐标尺度改成
δ=δ_actual+a·ξ，则替换列和 γ 都乘 a；|γ| 本身不能跨任意单位比较。
相同 phase_scale=σ 时，物理首相位为 d1=σp₀；若明确用本 profile 的
δ_ref=3/50 归一化，物理 phase 对相对 δ 的对应系数为 σδ_refγ。
报告原 γ 时须一并报告这两个尺度，而不能自行挑一个让数字好看。

下一次确有真实共同基点、且已有 LU 时，最少只增加：

1. 实际身份检查的标量/hash，完整 bδ 的来源/步长与BC列来源；
2. 一次 `factor.solve(e_i,trans='T')`，记录 γ、wᵀr、δ 校正预测和转置方程
   的规范化 backward error；需要完整方向才做另一次正解；
3. 若据新方向尝试更新，继续用新设计的真实完整 F、原域、原 Armijo、原 RMS、
   BC 与 metric 门。γ 不是接受标记，未通过的试点不能晋锚。

小 transpose backward error 只说明实际解满足一个附近线性方程，**不保证**
w 的 forward error 或 γ 的正确位数，尤其这里已有大逆放大证据。
使用同一 LU 的代数更新也不能自动修复其误差；原线性残差和后续真实非线性
测试仍须保留。所有向量留在 runner，仅必要标量和 SHA 留公开记录。

当前不为一个已经销毁/不存在的 LU 重新求解。等待真正 v5 零锚/实际返回后，
如需要区分 δ 兼容方向与高 phase 病态，再把这个最小诊断接到该实际基点。
