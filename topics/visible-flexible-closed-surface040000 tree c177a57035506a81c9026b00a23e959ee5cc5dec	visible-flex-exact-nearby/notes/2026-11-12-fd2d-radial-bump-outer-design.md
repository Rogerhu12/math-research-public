# 固定物理径向域上的紧支度量设计及原三场方程

**解析部分已证明；附真实有限实现检查。** 这是新的度量外设计族，不是同 g 加密，
也不声称已经求得新的非线性前缀。当前基准是
`2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json`，SHA256
`7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
其基准 T=.02 固定；物理子午长 L=1.4889731783581288，中央准确柱长 .32。

## 1. 显式的 C4 参数族

固定物理坐标 s∈[0,L]，选 J 个支撑区间 [α_j,β_j]，它们严格位于
中央圆柱末端与切口之间；实际默认再保护两边 .02 的开放邻域。
令 h_j=β_j−α_j，q_j=(s−α_j)/h_j，定义

$$
\psi_j(s)=
\begin{cases}
1024q_j^5(1-q_j)^5,&0<q_j<1,\\
0,&\text{其他}.
\end{cases}
\qquad
a_\delta(s)=a_*(s)+\sum_{j=1}^J\delta_j\psi_j(s).
$$

每个端点有五阶零点，所以零延拓属于 C4，0 至 4 阶导在支撑端点都为零。
因此原 a_* 的 C2 接合完全保留；中央圆柱和切口整个保护邻域上，a 及原有所有导数均未改变。
这保护的是度量两 jet，**不是已经证明实际位置、法向和第二基本形式自动接好**。
实际前缀的切口仍由原 BVP 全角 l,m,n 与尾匹配，再使用 R133 的真实刚体对齐。

源码用因式形式的 Leibniz 公式求导，不靠端点处大系数相消：

$$
\psi_j^{(k)}=\frac{1024}{h_j^k}
\sum_{i=0}^k {k\choose i}(5)_i(-1)^{k-i}(5)_{k-i}
q_j^{5-i}(1-q_j)^{5-k+i},\qquad 0\le k\le4.
$$

其中 (5)_i 是下降阶乘。默认 J=7，把设计区间等分为 J+3=10 格，
第 j 个支撑覆盖连续四格。这给七个重叠局部径向自由度。
实际支持端点完整保存于 profile.definition() 和检查报告；参数本身是准确解释的所存二进制实数。

以下全域界准确成立：

$$
0\le\psi_j\le1,\qquad
|\psi'_j|\le\frac{81920}{19683h_j},\qquad
|\psi''_j|\le\frac{40}{h_j^2}.
$$

证明：q(1−q)≤1/4 给第一式。令 v=1−2q，则无量纲一导为
20v(1−v²)^4，正半轴最大值在 v=1/3，等于 81920/19683。
令 t=q(1−q)∈[0,1/4]，无量纲二导为 10240t³(2−9t)。
其正最大值在 t=1/6，为 640/27；负最小值在 t=1/4，为 −40。
这也给可用的参数尺度 h_j²/40：单位这种尺度最多改变一单位 a''，但不是参数域限制。

## 2. 正度量域与全部标量导数

目标度量准确为

$$g_\delta=ds^2+a_\delta(s)^2du^2.$$

只需 a_δ>0 就是正 Riemannian 度量。这里不要求 |a'_δ|≤1；那个条件是旋转背景的
额外表征条件，原三场 GC 方程不需要它，也不除 n 或旋转背景的参考 n。
径向坐标仍是物理 s：s_x=1，s_δ=(s_x)_δ=0。固定 U(s,ξ) 图册也与 δ 无关。

非零 Christoffel 项为 Γ^s_uu=−aa'、Γ^u_su=a'/a，直接计算得到

$$c=\frac{a'}a,\qquad K=-\frac{a''}a.$$

对任意参数 j，有完整的准确公式

$$
a_j=\psi_j,\quad a'_j=\psi'_j,\quad a''_j=\psi''_j,\quad
c_j=\frac{\psi'_j-c\psi_j}{a},\quad
K_j=\frac{-\psi''_j-K\psi_j}{a},\quad
(1/a)_j=-\frac{\psi_j}{a^2}.
$$

`jet(s)` 返回这些数组，参数维在最后一维；JVP 就是与方向作线性收缩。

### 连续正值的可用充分条件

若已知基准 a_*≥B>0，则

$$a_\delta(s)\ge B+\sum_{j\text{ 在该支撑区间活动}}\min(\delta_j,0).$$

证明只用 0≤ψ_j≤1。正参数项取零下界，负参数项取 δ_j 下界；相加即可。
因此 B+Σmin(δ_j,0)>0 是全域充分条件；按支撑端点分区、每区只求活动项可更紧。
`check_positive` 明确分开有限采样 screen 和这个依赖已证 B 的解析充分界。
不会把节点正值误称连续正值。

本候选已有完整连续证明包
`2026-11-12-fd2d-peak-spacer34-radius-certificate-02.json`，SHA256
`3c9fa775b8cb94b93c1a39fc7ab68814c0efa271812271d3e5183d030b7d3695`，
给 B=4/5；包准确绑定上述候选。该包由 geometry 支线负责，未重新跑 ODE。

为了直接放进参数 QP，取搜索下界 ε<B。每个活动集合 A 上的条件
B+Σ_A min(δ_j,0)≥ε，等价于所有子集 S⊂A 满足

$$\sum_{j\in S}\delta_j\ge\epsilon-B.$$

因为左侧 min 和就是所有子集和的最小值。`positive_profile_linear_domain` 枚举这些小集合，
返回显式线性矩阵和下界；该域只是构造性搜索域，不能用它排除域外正度量。
还可以另加 δ 盒作为搜索选择。对于上述严格基准包，这些不等式支付真正全径向的正值。

## 3. 准确尾 lifting 的外设计导数

三场顺序一直是 V=(n,m,l)。令材料角 U=U(s,ξ)，

$$v(U)=(\cos^2U,-\sin U\cos U,\sin^2U),\qquad y=a(s)\sin U.$$

准确平坦尾场为 κ(y;b)v(U)。径向权重 ω(s) 固定，与 δ 无关；
中央 seed lifting 的 δ 导数为零。记 y_j=ψ_j sin U，则

$$L_j=\omega\,\kappa_y y_jv.$$

所需空间导数为

$$
y_s=a'\sin U+a\cos U\,U_s,\quad y_\xi=a\cos U\,U_\xi,
$$

$$
(y_j)_s=\psi'_j\sin U+\psi_j\cos U\,U_s,\quad
(y_j)_\xi=\psi_j\cos U\,U_\xi.
$$

再用乘积法则准确得到

$$
\begin{aligned}
(L_j)_s={}&\omega'\kappa_y y_jv+
\omega[(\kappa_{yy}y_sy_j+\kappa_y(y_j)_s)v+
\kappa_y y_jv_UU_s],\\
(L_j)_\xi={}&\omega[(\kappa_{yy}y_\xi y_j+\kappa_y(y_j)_\xi)v+
\kappa_y y_jv_UU_\xi].
\end{aligned}
$$

正 Bernstein 尾中 α_q=630q⁴(1−q)⁴ Σ b_i B_i^K(q)，所以 κ_yy 是这个已知多项式的
二阶 q 导除以宽度三次方。源码 `positive_tail_kappa_yy` 显式实现这一公式；
|y|≤.34 和 |y|≥.8 的零延拓与已有 κ 的平滑阶数相容，没有在 n=0 处除法。
`tail_lifting_profile_jacobian` 返回完整值、s 和 ξ 列，不做 Fourier 投影。

## 4. 接入原三场残差，不补虚假方程

设 d=2K+1、e=K+1、q=3K+2，N 个径向节点。新的参数顺序明确为

```
[central c: K, tail Bernstein b: K+1, physical delta: J]
```

基准 T 不在未知量中。代码暴露 `tail_parameter_slice`、`profile_parameter_slice`、
`parameter_count`、`fixed_base_T`，不再使用旧 `K:-1` 或最后一项是 T 的假设。
未知数 Nq+2K+1+J；原残差数量 Nq+2K+2，故 J=7 时多六个设计自由度。
Jacobian 是矩形，直接使用带正则方向的约束最小二乘/Schur，不为凑方阵加六个任意方程。

固定图册下，令 D=(aU_ξ)^{-1}、w=U_s/U_ξ。原完整场的有限系数 RHS 对应

$$f_n=Dm_\xi+c(l-n)+wn_\xi-L_{n,s},\qquad
f_m=Dl_\xi-2cm+wm_\xi-L_{m,s}.$$

这里减去 lifting 的 s 导，因为未知量是 correction 的 Fourier 系数。
原节点系数固定时，V_j=L_j。用 D_j=−ψ_j/(a²U_ξ)，得到

$$
\begin{aligned}
(f_n)_j={}&D_jm_\xi+D(L_m)_{\xi j}+c_j(l-n)+c(L_{l,j}-L_{n,j})
+w(L_n)_{\xi j}-(L_n)_{sj},\\
(f_m)_j={}&D_jl_\xi+D(L_l)_{\xi j}-2c_jm-2cL_{m,j}
+w(L_m)_{\xi j}-(L_m)_{sj}.
\end{aligned}
$$

Gauss 的完整导数为

$$G_j=lL_{n,j}+nL_{l,j}-2mL_{m,j}-K_j.$$

代码随后按原 PE/PO 投影和原梯形径向差分装配；状态、尾参数、中央参数列保持原意义。
支撑离开两端，所以准确中央和 cut 的 δ 列为零，gap 行也不依赖 δ。
全部真实 cut 均值照旧保留。

`data.fields_parameters` 保存 [angle,node,3,all_parameters] 的完整原字段参数列；
中央列在独立节点系数约定下为零，调用方执行准确中央边界消元时再组合该线性映射。
lifting 的 `profile_parameters`、`profile_x_parameters`、`profile_xi_parameters`
给外设计列；`parameters`、`x_parameters`、`xi_parameters` 给尾控制列。
因此全角 Gauss/Codazzi complement 可以直接消费，不必偷偷把高模丢掉。

## 5. 实际实现范围和可用入口

源 `fd2d_gc_radial_bump_profile.py` 已实际在 7 个非零 δ 上检查：
session 67454/2a3344，真 exit0，2.946 秒；a/a'/a''/c/K 与 tail lifting 三种 jet 的
最大方向相对 L2 差 5.13e−10，保护邻域三项误差逐位为零。

`RawBumpDAE` 的全 Jacobian 也已实际检查：session 52457/2b5b7b，真 exit0，29.802 秒。
δ=0 同格与旧完整 F、fields、全 Gauss 差均逐位零；非零 7δ 的最大原 F 方向相对 L2 差
2.30e−9。实际 J 为 4732×4738，字段保持独立 n,m,l。
该版字节完整保留为 `fd2d_gc_raw_bump_dae_check01_snapshot.py`；随后仅暴露附加尾导数字段，
新字段的独立小检查与原 F/J 不变比较另存，不把旧检查 SHA 转借新源。

可用初值 `2026-11-12-fd2d-raw-bump-jvp01-warm.npz`，SHA256
`70371620059412d29b2bf51bd76b7617eefc3e0b5af99c127dea74fe66fda9a2`。
它从新 34 候选自身的真实前段和 K15 桥生成，只在原节点和支撑端点的并集上评价原 P1 correction，
新增 δ=0；**没有重新求解，也不是误差加密结果**。

后续主代理对 raw 场、中央、尾控制和这些径向参数真正联解。选定最终 δ 后，
必须把该物理 g 定义完整保存，再在同一 g 下做角频/径向/时间加密。
本接口和检查没有支付实际位置全域 metric、曲率、reach、held 或闭帽接合。
