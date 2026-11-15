# R288：不交紧微包的跨包三阶局域性与 canonical 一次端层自动消去

日期：2026-11-15。**完整原式的纸面证明；没有执行新的求积、profile 评价、符号程序、秩计算或开发检查。**

[R283](R283-canonical-end-layer-three-history-moments-and-pure-symmetry-cancellation.md) 把当前 pure 已付几何上的两个 mixed 周期端目标，准确归约为原 W_{fc} 三阶尾的三个加权历史矩。本稿证明：对 R277—R281 所用的真正不交紧 profile 微包，这三个矩在每个内部零平台上已经自动为零。

关键是一个比“外尾仿射”更强的原式事实：当第三场 C(u_i;u_j,u_j) 的两个微包不同，其整个场局域于外槽 u_i 的包，而不仅是在外部具有仿射分子。真实 second 尾仍在包内参与 forcing，但它的常 x 导数与紧初阶分子的端差准确正交。

剩余的 diagonal C(u_i;u_i,u_i) 一般仍有非零三阶左尾。它们的三个加权矩，由已安装几何的 **whole-period universal pure 身份**分别消去；不是把原尾点态置零。

本稿只支付一次指数端层。原平台多项式、零端通量、内部退化、完整第四 ruling 和同一 gauge 的 joint 条件继续保留。

## 1. 固定对象与严格范围

固定 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) §7.3(17)、[R213](R213-two-mixed-sources-and-gauge-invariant-platform-obstructions-after-pure-closure.md)(1) 所给的实际闭几何，或其后用完整有限观测 IFT 保持同一身份的版本：

$$
M_X=0,\qquad T_X=\kappa\mathfrak H,\quad\kappa\ne0,
\qquad \pi V_X=0
\quad\text{对全部共同右 collar profiles 成立}.
\tag{1}
$$

这是实际完整 canonical period 的 pure 零身份，不是只引用 pure 响应像、闭锥或可达空间的等号。全局 characteristic 初值、右锚和真实几何 history 均保持不变。

在已经固定的合法物理区间 I 内，取有限个两两有正间隙的紧区间 J_i，并取

$$
u_i\in C_c^\infty(J_i;\mathbb R),\qquad
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i.
\tag{2}
$$

这里 a_i\ne0，因而在第 i 包上 g=\ell_i f，\ell_i=b_i/a_i。每个 u_i 在其零端具有 R281 的非零解析 prefactor 乘指数平端；无需各包同形。R287 的两个振荡因子和各自有限频率校正都在这个范围内。

重要区别：**(2) 要求 profile 本人紧支撑且不交，不只是正阶导数分包。** 原 R183 那种带非零常值平台的重叠 step 圆不能未经新证明套用本稿。

实际圆已经用原三矩、hook 和完整八复制支付二、三阶 range。十二复制、最后五块正幅混合以及 Gaussian 条件按各自既有证明保留；本稿不重新评价这些数据，也不需要它们来证明下述局域引理。

## 2. 原二阶场的真实外尾分子

沿用 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 与 [R248](R248-complete-fourth-harmonics-and-complementary-block-reduction.md) 的规范：

$$
Z(a,b)=\operatorname{Range}H(Y_a,Y_b),\qquad
C(a;b,c)=\operatorname{Range}H(Y_a,Z(b,c)).
\tag{3}
$$

H 为对称双线性 forcing，H(U,U)=(dU)^2；Range 始终是同一 canonical 右锚恢复。未单独付左 collar 的分解项仍按其原形式字段理解，不冒称为独立合法输入。

记 Z_j=Z(u_j,u_j)。因为该 forcing 的四个分子配对均支撑于 J_j，在其右侧 Z_j 为零。在其左侧，R56 原式给

$$
P_j=p_j(s),\qquad B_j=0,\qquad
\eta_{0,j}=-\frac12(p_j)_s,
$$

$$
\mathcal W_j=\alpha_j(s)x^2+\beta_j(s)x+\gamma_j(s).
\tag{4}
$$

这三个系数包含全部真实 s-history。由

$$
V_{Z_j}=(A_j,\ zP_j+B_j,\ eA_j-h\mathcal W_j),
\qquad
A_j=\frac12(\mathcal W_j)_x+\frac{\eta_{0,j}}h,
$$

第三分量的 x^2 项准确相消，所以

$$
\boxed{
V_{Z_j}\text{ 在整个左外区间上对 x 仿射，}
\quad \partial_xV_{Z_j}\text{ 与 x 无关。}
}
\tag{5}
$$

p_j、\mathcal W_j 及该常导数通常并不为零。后面的证明完整使用 (5)，没有先删 second 左尾。

## 3. 跨包第三场的整个外部为零

令

$$
C_{ij}=C(u_i;u_j,u_j),\qquad i\ne j.
$$

其 forcing H(Y_{u_i},Z_j) 的每个分子配对都含 Y_{u_i} 或其真实导数。因此 forcing 支撑于外槽包 J_i。固定 u 的 s 微分也不破坏这一事实：换到特征坐标后只增加同一紧 profile 的 x 导数。

如果 J_i 位于 J_j 右侧，则 Z_j 在 J_i 上为零，整个 forcing 与 C_{ij} 均为零。

如果 J_i 位于 J_j 左侧，则在整个 J_i 上，\partial_xV_{Z_j} 是同一个依赖 s 的常向量。于是 C_{ij} 的真实左 P 尾为

$$
\begin{aligned}
p_{ij}(s)
&=\frac1{2h(s)}
\int_{J_i}\partial_xV_{Y_{u_i}}\cdot\partial_xV_{Z_j}\,dx\\
&=\frac1{2h(s)}
\partial_xV_{Z_j}\cdot
\left[V_{Y_{u_i}}\right]_{\partial J_i}=0.
\end{aligned}
\tag{6}
$$

初阶分子为

$$
V_{Y_{u_i}}=(-u_i'/2,\,0,\,hu_i-eu_i'/2),
$$

所以它在 J_i 两端确为零。式 (6) 不使用 u_j 的三矩为零，也不把 Z_j 假设为局域。

在 J_i 外部，原局部 J、T_s、T_{sx} 为零，故 B_{ij}=0。式 (6) 使左 P_{ij}=0，右锚使右 P_{ij}=0，且这些等式对全部 s 成立。R56 随即给

$$
(\eta_0)_{ij}=0,\qquad
(\mathcal W_{ij})_s
=K_0P_{ij}-\lambda(P_{ij})_s=0
\quad\text{在 }I\setminus J_i.
$$

同一个全路径 canonical 初值为零，所以 \mathcal W_{ij} 在该外部始终为零。最后原恢复式给

$$
\boxed{
C_{ij}=0\quad\text{于 }I\setminus J_i,\qquad i\ne j.
}
\tag{7}
$$

这已经包括真实 normal/mixed 分量、全部 s-history 和所有所需导数。没有在微包间重新设置 s 初值。

式 (7) 不宣称 C_{ij} 在 J_i 内为零。它在包内可能含关于 u_i 的一次局部项；在第四 forcing 中与 Y_{u_i} 相乘后，这些项属于二次指数层，不能把它们当作未付的三阶平台一次尾。

## 4. 单包 diagonal 左尾的三个加权矩为零

现在固定任意一个 i，令

$$
C_i=C(u_i;u_i,u_i).
$$

C_i 的 forcing 支撑于 J_i，但其左尾一般不为零。R56 给它与 R283 §2 相同的真实二次 characteristic 尾和仿射分子。

它在 s 上周期：M_X=0 使 Z(u_i,u_i) 的原端数据相接，而
T_X=\kappa\mathfrak H、
\mathfrak H(u_i;u_i,u_i)=0
使 C_i 的 characteristic period 为零。这里无需单个 u_i 满足任何不可能的实零三矩；只使用同一几何的完整算子身份。

用 R283 的记号，将左平台分子写为

$$
(V_{C_i})_T=a z+t_0,\qquad
(V_{C_i})_B=\eta z+q_0,
$$

令

$$
v_i=t_0/h,\qquad w_i=q_0/h,\qquad
\rho_i=(v_i)_{ss}+v_i-kw_i.
$$

其真实二次历史多项式为

$$
\mathcal P_i(x)=
\int h\rho_i\left\{
\left(x+\omega-\frac{k}{h}\right)^2+h^{-2}
\right\}\,ds.
\tag{8}
$$

在整个左外区间使用的都是同一 a,t_0,\eta,q_0，不在不同观察点另积原函数。

由 (1)，原完整 pure period 对这个真实允许的单输入 u_i 恒零：

$$
0=\mathcal V_{\rm p}(u_i)
=-\mathscr P\{H(Z_i,Z_i)\}
-4\mathscr P\{H(Y_{u_i},C_i)\}.
\tag{9}
$$

式 (9) 是 universal 身份的纸面应用，不是替换当前实际圆的种子，也不是新的 profile 科学评价。

在 u_i 自己的左解析零端，第二场平方只含平台和二次以上指数层。由 R283 的完整 cross 公式，(9) 的唯一一次层为

$$
-\{\mathcal P_i u_i'-\mathcal P_i'u_i\}.
\tag{10}
$$

R276/R281 的首指数分离迫 (10) 为零。非零指数平端不可能满足
Q u_i'-Q'u_i=0
而 Q 是非零二次多项式，故

$$
\boxed{\mathcal P_i\equiv0.}
\tag{11}
$$

(11) 是三个加权 s 积分为零；它不声称 \rho_i=0、C_i 为 rigid 场、p_i=0 或其原第三左尾为零。

同一第三尾多项式在 J_i 的**整个左外区间**延续，因此 (11) 同时适用于该区间中任一零平台。在 J_i 右侧，C_i 本身由右锚为零。

## 5. 任一内部零平台的有序源自动为零

原初阶包支撑不交，故二阶交叉 forcing 准确为零：

$$
Z(f,g)=\sum_j a_jb_j Z_j.
$$

三阶线性恢复随即给

$$
C(f;f,g)=
\sum_{i,j}a_i a_jb_j C_{ij}.
\tag{12}
$$

取任一零平台 J，位于全部活动包之外。由 (7)，每个 i\ne j 的项在 J 上整个场为零；只剩

$$
C(f;f,g)|_J
=\sum_{i:\,J\text{ 位于 }J_i\text{ 左侧}}
a_i^2b_i\,C_i|_J.
\tag{13}
$$

式 (13) 保留这些 diagonal 场的所有原尾。现在仅对它们应用 R283 的线性历史多项式提取，并使用 (11)，得到

$$
\boxed{
\mathcal P_J[C(f;f,g)]=
\sum_{i:\,J<J_i}a_i^2b_i\,\mathcal P_i=0.
}
\tag{14}
$$

R213/R283 的实际有序源是

$$
W_{fc}=-4C(f;f,g),\qquad
Q_J=\mathcal P_J[W_{fc}].
$$

所以

$$
\boxed{Q_J=0\quad\text{在每一个内部或外部零平台上。}}
\tag{15}
$$

这不是不同平台之间的正负抵消，也不需要调节最后五块的正幅。每个 diagonal 项的三个真实加权矩已经分别为零。由 (7)，其余跨包项不能把一个新的三阶平台尾带入 (15)。

所有已固定的微包位置、完整副本权重、实际母包及右锚均原样保留。它们可以来自 R279、R281、R284 或 R287 的不同有限频率根；(6)—(15) 不要求各包同形、同 cutoff 或相同未付历史值。

## 6. 对当前 mixed 周期端条件的准确提升

在第 i 个活动包，g=\ell_i f。R283 的两个实际 gauge 目标是

$$
G_c=-\frac{V_d}{4\kappa},\qquad
G_s=-\frac{V_e}{2\kappa}.
$$

它们的一次端层分别为

$$
G_c^{[1]}=-\frac{\ell_i}{8\kappa}
(Q_Jf'-Q_J'f),\qquad
G_s^{[1]}=-\frac1{8\kappa}
(Q_Jf'-Q_J'f).
$$

由 (15)，**所有这些一次端层同时为零**。因此在每个当前解析零端都有准确分解

$$
\boxed{
G_c=P_{e,c}+(f')^2t^{-4}B_{e,c},\qquad
G_s=P_{e,s}+(f')^2t^{-4}B_{e,s},
\quad B_{e,c},B_{e,s}\in C^\infty.
}
\tag{16}
$$

P_{e,c},P_{e,s} 仍是原 canonical 的实际平台多项式。若相应平台门 P_e''=0 和 R225/R276 的零端通量分支已支付，则

$$
G_c'',G_s''\in (f')^2t^{-8}C^\infty,
$$

R276 的原 Green 公式给两个端逆解都真实光滑；不再有非零一次指数引起的 e^{+c/t} 爆长项。这一结论仍不能省去平台和通量前提，也不支付活动包内部 p/A 的退化匹配。

本稿由实际 whole pure 身份和原跨包恢复得到 (15)，**没有从全部72 Gaussian 面积或六条能量推断它**。这些此前已付条件继续保持；其余对称 Gaussian 乘积、零/一层 ruling、完整 period 的内部与平台条件，以及同一个二阶 gauge 的全 joint 方程仍需分别处理。

对只要求导数分包、具有非零常平台的旧 step 圆，或另加任意非 canonical 第三初值，本稿的齐次外尾和首指数论证不能未经检验套用。当前新的紧微包解析圆则已准确支付全部零端一次历史门。

