# R721 — 同一固定度量下支持种子的端层宽度与平滑三角 profile 敏感性

2026-11-27（UTC）。**已证明：对 R711 的全部准确 profile 根域 $0<r<1$、$0<\delta<1/8$，固定准确均值与中央长度时，增大 $\delta$ 严格增加中央 $\max|F_{ss}|$，虽然幅度 $\lambda$ 本身严格下降；相位二阶量 $\max|\alpha_{ss}|$ 则严格下降。** 对端层总宽度另给完整移动边界导数、准确均值敏感性与中央主项下降判据，并分离端层转向、Gram 与真正曲率的责任。

本结果只作符号证明与实际源码合同映射，没有科学执行，没有新求解器或参数准入门。它使用已登记的 R708–R711，不重新认领其中的单位闭合、均值存在、角导数或曲率比较定理。新内容是同一 R711 profile 内部的严格参数单调性，以及改变物理端层宽度时不可遗漏的完整敏感性公式。

**所得结论不能直接排序两个完整实际场的 principal curvature、Gram 误差、reach 或可行性。** 它能区分端层加宽的收益、中央段与均值变化的代价，给下一次完整初始场探索一个明确的数学理由。当前第 17 次入口没有被本说明预判为成功或失败。

## 1. 准确对象、当前源与适用范围

准确目标仍为
$$
g=ds^2+a_{\rm deep}(s)^2\rho_0(\phi)^2d\phi^2,\qquad 0\le s\le S.
$$
固定参考由完整 Fejér recipe、准确 R690 scalar 和其冻结材料图定义。两个参数不会重新定义这个 $g$。

本说明对应以下已经完整公开的来源：

| 角色 | 完整来源 SHA256 |
|---|---|
| 参考 [fixed_fejer_axisymmetric_reference.py](../scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py) | e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb |
| seed [fixed_fejer_supported_meridian_reference.py](../scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py) | ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a |
| base [fixed_fejer_supported_so3_meridian_operator.py](../scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py) | 552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3 |
| normal [fixed_fejer_stage_point_normal_lift.py](../scripts/resume_20261126/fixed_fejer_stage_point_normal_lift.py) | 42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10 |
| observed driver [fullclosed_fixed_fejer_stage_point_observed_so3_qp.py](../scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_observed_so3_qp.py) | 8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d |
| pure [read_fixed_fejer_stage_point_observed_so3_report.py](../scripts/resume_20261126/read_fixed_fejer_stage_point_observed_so3_report.py) | c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f |

所有源码位于本题 scripts/resume_20261126。实际 CLI 为
$$
\beta=b/S=\texttt{seed-boundary-total-length},\qquad
\delta=\texttt{seed-profile-delta}.
$$
其中 $b$ 是四端层的物理总长度；$\delta$ 是归一化中央 profile 的参数，二者不能混用。

支撑保持
$$
U/S=[1/32,15/32]\cup[17/32,31/32],\qquad L=|U|=7S/8.
$$
每个端层宽度为 $\Delta=b/4$，两个中央段有相同长度
$$
\ell=7S/16-b/2=(L-b)/2,\qquad L_c=2\ell=L-b.
$$
在固定的参考 core/H 上，准确均值方程是
$$
\mathcal F(v,b,\phi)=(L-b)v+B(b,Nv,\phi)-K(\phi)=0,\qquad N(v)=v/|v|.
$$
参数几何域为 $0<b<L=7S/8$，使每端层和每中央段都保持正长度。因为支撑端点未动，
$$
K=P-\Gamma-\int_{U^c}T_0\,ds
$$
不依赖 $b,\delta$。$B$ 依赖 $b,d=Nv,\phi$，不依赖中央 profile 参数 $\delta$。

以下种子几何公式适用于：准确均值根和所用同一分支已经存在、全部需要的正分母与正则性已付，完整准确 seed 已闭合，外旋转为零。此时
$$
F_{\rm seed}(s,\phi)=P(\phi)-\int_s^S T(u,\phi)\,du,\qquad
(F_{\rm seed})_s=T,\quad |T|=1.
$$
它们不把工作 seed 的舍入或求积误差置零，也不证明实际 32-stage normal 程序选择了某个准确根，更不能迁移给已有非零外旋转的优化末场。实际 whole-field 仍要消费其真实同点完整 packet 和原全部费用。

## 2. 不重复的已有结论接口

直接沿用：

- [R708](R708-supported-unit-meridian-seed-contraction.md)：准确端层归一化、平端口、单位积分构造及薄端层导数成本。
- [R709](R709-global-convex-mean-closure-without-contraction.md)：完整三均值方程、凸梯度单调性、无收缩逆界和完整角导数。其粗充分条件依旧是 $b<k_-$、$b<k_z$、$k_++2b<L$，不是物理必要条件。
- [R710](R710-supported-unit-seed-complete-angular-jet-error-bounds.md)：候选到准确根及完整两角 jets 的误差账。
- [R711](R711-smooth-triangle-central-profile-and-geometric-comparison.md)：十二片 profile、全部 $0<r<1$ 的幅度根、准确中央 $F_{ss}$ 以及真正曲率矩阵的比较。
- [R713](R713-exact-smooth-triangle-moments-and-actual-fees.md)：完整 profile 矩和实际参数的有理算术接口。
- [R715](R715-reference-centred-normal-sixjets-and-error-ledger.md)：准确与工作完整物理 lift 的区分。

本说明不会把候选 $\widehat D=K-B(N\widehat v)$ 当成准确根上的 $D_*=L_cv_*$。若 R709 的粗条件没有付清，必须另有真实根存在/包含及共同分支证明后，才能用更紧的根界消费其后续公式。本说明不提供这个缺失证书。

## 3. 固定均值时，增大 profile 参数会提高中央径向二阶主项

令 $a=1/4$，$0<\delta<a/2$，沿用 R711 的 quarter 速度与原函数
$$
g_\delta(t)=
\begin{cases}
S_5(t/\delta),&0\le t\le\delta,\\
1,&\delta\le t\le a-\delta,\\
S_5((a-t)/\delta),&a-\delta\le t\le a,
\end{cases}
\quad
Q_\delta(t)=\int_0^t g_\delta(u)\,du,\quad
c_\delta=a-\delta.
$$
完整 $h_\delta$ 是 $Q_\delta/c_\delta$ 的原四 quarter 对称拼接。对固定准确 $r\in(0,1)$，记唯一幅度根为
$$
A_\delta(\lambda_\delta)=r,\qquad
A_\delta(\lambda)=\int_0^1\cos(\lambda h_\delta(t))\,dt,\quad
0<\lambda_\delta<\pi,
$$
并定义
$$
p_\delta=\lambda_\delta/c_\delta.
$$
在一个准确中央段 $I=[s_-,s_-+\ell]$ 上，令 $t=(s-s_-)/\ell$，
$
\alpha=\lambda_\delta h_\delta(t),\qquad
T=\cos\alpha\,d+\sin\alpha\,w,\qquad
V=-\sin\alpha\,d+\cos\alpha\,w.
$
这里 $d,w$ 为同一对对径向坐标固定的正交单位向量，所以 $T,V$ 也是正交单位向量，$F_{ss}=T_s=\alpha_sV$。R711 已给的准确极值因而是
$
\max_{s\in I}|F_{ss}|=\max|\alpha_s|=p_\delta/\ell.
$

### 3.0 合法根域及共同范围

下面的比较只使用两参数都合法的准确幅度根，不把有限工作求根或候选均值当作它们的存在证明。所需域并不随 $\delta$ 收缩：它恰为
$$
\mathcal D=\{(r,\delta):0<r<1,\ 0<\delta<1/8\}.
$$
理由是 R711 §4 的完整对称性在每个合法 $\delta$ 都给
$$
A_\delta(0)=1,\qquad A_\delta(\pi)=0,\qquad
-A_\delta'(\lambda)=
\int_0^1h_\delta(t)\sin(\lambda h_\delta(t))\,dt>0
\quad(0<\lambda<\pi).
$$
第一、第二个恒等式分别来自零幅度与 quarter 配对；最后一个严格号来自正测度的 $0<|h_\delta|<1$ 集合。连续性和严格单调性因而在每个 $(r,\delta)\in\mathcal D$ 给唯一 $0<\lambda_\delta(r)<\pi$。这里仅把 R711 已证结论实例化为本次参数比较的共同域，没有把 $A_\delta(\pi)=0$ 冒成工作浮点求积的恒等式。

若整个角圈已有同一准确均值分支
$$
0<r_-\le r(\phi)\le r_+<1,
$$
则对所比较的全部 $\delta$，R711(8)(9) 给共同界
$$
\arccos r_+\le\lambda_\delta(r(\phi))
\le2\arccos r_-<\pi,\qquad
-A_\delta'(\lambda_\delta)\ge
\frac13\min_{\lambda\in[\arccos r_+,\,2\arccos r_-]}\sin\lambda>0.
$$
在任何闭的 $\delta$ 子区间 $[\delta_1,\delta_2]\Subset(0,1/8)$，显式 piece 公式及其交界匹配允许积分内微分；上述非零导数使 $\lambda_\delta(r)$ 为同一个 $C^1$ 参数分支。均值 $r$ 不随 profile-only 的 $\delta$ 改变，因为完整三均值方程不含 $\delta$。

这不能反过来支付三均值方程的真实根：若仅有工作候选 $\widehat v$ 或 $\widehat D$，尚不能声称实际 $r\in(0,1)$ 已证。R709 或另一完整准确根存在/包含证明仍是同一 seed 的前提。$r=0,1$、$\delta=0,1/8$ 的端点不属于本严格比较；若改变 $b$，还必须对每个所用 $b$ 支付准确均值根域，不能借 profile 根域代替它。

### 3.1 严格单调性

**定理 1（profile-only 单调性）。** 固定 $r\in(0,1)$、$\ell>0$ 和同一准确正交架。若 $0<\delta_1<\delta_2<a/2$，则 $p_{\delta_2}>p_{\delta_1}$、$\lambda_{\delta_2}<\lambda_{\delta_1}$，且下文的两条径向主项变化严格成立。

**第一部分证明。** 在固定 quarter 点上
$$
g_{\delta_2}(t)\le g_{\delta_1}(t).
$$
这是因为
$$
g_\delta(t)=S_5\!\left(\min\{1,\min(t,a-t)/\delta\}\right)
$$
而 $S_5$ 在 $[0,1]$ 单调。该不等式在正测度的区间严格，故 $Q_{\delta_2}\le Q_{\delta_1}$，并在正测度集严格。

固定旧值 $p_1=p_{\delta_1}$。由于
$$
0\le p_1Q_{\delta_2}(t)\le p_1Q_{\delta_1}(t)\le\lambda_{\delta_1}<\pi,
$$
cos 的严格单调性与四 quarter 对称性给
$$
A_{\delta_2}(p_1c_{\delta_2})
=4\int_0^a\cos(p_1Q_{\delta_2})\,dt
>
4\int_0^a\cos(p_1Q_{\delta_1})\,dt=r.
$$
在第二个 profile 中，完整余弦矩对正幅度严格下降，所以必须 $p_{\delta_2}>p_1$。

因此
$$
\boxed{\quad
\delta_2>\delta_1
\Longrightarrow
\max|F_{ss}|_{\delta_2}>
\max|F_{ss}|_{\delta_1}
\quad}
$$
在同一准确均值、同一中央长度的比较中严格成立。

这是同一 profile 家族的参数结论，不是 R711 对旧五段输入的比较重述。它也只排序径向二阶向量范数；真实法向曲率还含 $N_{\rm surf}\cdot F_{ss}$ 和完整角向几何，不能据此直接断言 principal curvature 变大。

### 3.2 幅度本身反而下降

**定理 1 的第二部分证明。** 这个细节解释为什么不能只看幅度 $\lambda$。

在 $0<t<a/2$ 上，归一化 $H_\delta=Q_\delta/c_\delta$ 对 $\delta$ 严格下降。plateau 区的导数是
$$
\partial_\delta H_\delta(t)=
\frac{t-a/2}{(a-\delta)^2}<0.
$$
ramp 区令 $x=t/\delta$。由
$$
I_5(x)=\tfrac52x^4-3x^5+x^6,\qquad
2I_5(x)-xS_5(x)=-x^4(1-x)(5-4x)\le0
$$
有
$$
\partial_\delta H_\delta
=\frac{aI_5(x)-(a-\delta)xS_5(x)}{(a-\delta)^2}
\le\frac{(\delta-a/2)xS_5(x)}{(a-\delta)^2}<0.
$$
piece 交界连续，故整体顺序成立。用 R711 的 quarter 配对
$$
A_\delta(\lambda)=8\cos(\lambda/2)
\int_0^{a/2}\cos\!\left(\lambda(1/2-H_\delta(t))\right)dt
$$
可得固定 $0<\lambda<\pi$ 时 $A_\delta(\lambda)$ 随 $\delta$ 严格下降。因此同 $r$ 时
$$
\lambda_{\delta_2}<\lambda_{\delta_1},
\qquad
1<\frac{p_{\delta_2}}{p_{\delta_1}}
<\frac{a-\delta_1}{a-\delta_2}.
$$
幅度降低与最大相位斜率增加同时发生，并不矛盾。

### 3.3 更高径向变化的相反代价

**定理 1 的径向结论。** 由 $S_5'(x)=30x^2(1-x)^2$ 在 $[0,1]$ 的最大值为 $15/8$，原五次速度给
$$
\max|\alpha_{ss}|=
\frac{15\lambda_\delta}
 {8\,\delta(a-\delta)\ell^2}.
$$
在 $0<\delta<a/2$ 内，$\delta(a-\delta)$ 随 $\delta$ 增加；上节又给 $\lambda_\delta$ 下降，故同 $r,\ell$ 时这个相位二阶量严格下降。

这不表示 $|F_{sss}|$ 也必下降，因为
$$
T_{ss}=\alpha_{ss}V-\alpha_s^2T,\qquad
|T_{ss}|^2=\alpha_{ss}^2+\alpha_s^4.
$$
两个贡献各自的全段最大值变化方向相反；上述极值结论不足以排序完整的 $\max|T_{ss}|$。更宽 ramp 可改善某些高阶变化或工作求积的尺度，但不能把这一目的写成中央 $|F_{ss}|$ 改进。原 actual normal 的完整 Gauss 求积、准确标量、根误差与费用预算仍须真实支付。

## 4. 端层加宽的直接收益：归一化转向项

在一个端层上
$$
Y=(1-\chi)T_0+\chi d,\qquad T_b=N(Y),
$$
其中 $d$ 对径向坐标固定，$P_{T_b}=I-T_bT_b^T$，且 $DN(Y)=P_{T_b}/|Y|$。完整径向导数为
$$
(T_b)_s=
\frac{P_{T_b}}{|Y|}
\bigl((1-\chi)T_{0,s}+\chi_s(d-T_0)\bigr).
$$
令 $c=T_0\cdot d=\cos\theta$，$\theta<\pi$。单位端点给
$$
|Y|^2=1-2\chi(1-\chi)(1-c).
$$
同时
$$
Y\times(d-T_0)=T_0\times d,
$$
所以 cutoff 转向项的准确范数是
$$
\left|
\frac{\chi_sP_{T_b}(d-T_0)}{|Y|}
\right|
=
\frac{|\chi_s|\sin\theta}{|Y|^2}.
$$
这保留了端层方向夹角，较只用 $|d-T_0|\le2$ 更能说明实际机制。

若整端层已有 $\theta\le\theta_{\max}<\pi$、$|Y|\ge\nu>0$、$|T_{0,s}|\le U_s$，则
$$
\frac{\sin\theta}{|Y|^2}
\le2\tan(\theta/2),\qquad
\max|\chi_s|=\frac{15}{8\Delta}=\frac{15}{2b},
$$
从而
$$
\boxed{\quad
|(T_b)_s|\le
\frac{U_s}{\nu}+
\frac{15}{b}\tan(\theta_{\max}/2).
\quad}
$$
在共同已付的 $U_s,\nu,\theta_{\max}$ 下，第二项呈明确 $1/b$ 改善。实际 $\theta_{\max}$ 和 $\nu$ 会随均值方向以及加宽后覆盖的 $T_0$ 区域变化；不允许只缩放 $1/b$ 而保未经比较的旧角度或旧分母。

该界是上界，不是实际最大曲率的下界。径向参考项、方向抵消、法向投影以及全 Gram 的条件数均继续存在。

## 5. 端层宽度对均值根：不能遗漏移动边界

**定理 2（物理端层宽度敏感性）。** 在所比较的 $b$ 邻域内，假设准确参考 $T_0$ 在全部扫过的端层上有连续径向一阶导数，准确均值根分支及其端层正分母已经存在。本文不要求在当前科学入口前另运行参数扫描；这些是导数公式的数学适用条件。

把四个固定支撑端点记为 $s_j^0$，进入支持的方向记为 $\varepsilon_j=+1$ 或 $-1$。使用完整局部坐标
$$
s_j(b,t)=s_j^0+\varepsilon_jbt/4,\qquad 0\le t\le1,
\quad \chi(t)=S_5(t).
$$
在固定方向 $d$ 下，
$$
B(b,d,\phi)=\frac b4\sum_{j=1}^4
\int_0^1N\bigl((1-\chi)T_0(s_j(b,t),\phi)+\chi d\bigr)\,dt.
$$
固定局部坐标 $t$ 后，所有移动的积分端点已经进入 $s_j(b,t)$ 及前因子 $b/4$。在该准确正则域内作乘积/链式微分，因此固定 $d,\phi$ 的真实偏导是
$$
\boxed{\quad
B_b=
\frac14\sum_j\int_0^1T_{b,j}\,dt
+
\frac b{16}\sum_j\varepsilon_j
\int_0^1t(1-\chi)DN(Y_j)T_{0,s}(s_j)\,dt.
\quad}
$$
第一项是物理长度的变化；第二项是真实径向参考随移动端层采样位置变化。二者都不可删去。这正对应 R709 对移动端点和 $L_c$ 乘积项的提醒，未把宽度变化错误当作固定支持的角导数。

若上述共同界成立，则由
$$
\int_0^1t(1-S_5(t))\,dt=1/7
$$
得到一个可用但保守的完整上界
$$
|B_b|\le1+\frac{bU_s}{28\nu}.
$$

在一个真实准确根分支上，$J=\mathcal F_v$ 为 R709 的完整通常非对称 Jacobian。因为 $L_c'= -1$、$K_b=0$，
$$
\boxed{\quad Jv_b=v-B_b.\quad}
$$
R709 的完整径向/正切块分解给该正则根处 $J$ 可逆。只要已有合法全矩阵逆界 $\|J^{-1}\|\le\eta$，便有
$$
|v_b|\le\eta\left(r+1+\frac{bU_s}{28\nu}\right).
$$
这不是 $r_b$ 的符号结论。

更清楚地，令 $v=rd$、$P=I-dd^T$、$M=B_d\succeq0$。投影后
$$
(L_crI_{d^\perp}+PMP)d_b=-PB_b,
$$
$$
L_cr_b=r-d\cdot B_b-d\cdot Md_b.
$$
因此 $d_b$ 与 $r_b$ 取决于完整向量 $B_b$ 和径向/切向耦合，不能从“端层更宽”推其方向或符号。这些公式的右端均是准确的完整三分量量，不能用候选残差替代。当前工作 mean 的 Newton 最大迭代数、初值或容差也不是可自由选择准确均值方向的几何参数：当相应唯一性已付时，它们求的是同一根。

## 6. 端层加宽对中央主项的明确代价

**推论 3（局部下降的充要判据）。** 在定理 2 的同一准确根分支、$0<r<1$、$0<b<L$ 及固定 $0<\delta<1/8$ 上，中央 $U_c$ 对 $b$ 的导数严格为负，当且仅当下面列出的正向均值变化不等式成立。

固定 profile 参数 $\delta$，令 $c_\delta=1/4-\delta$。本题两中央段等长，
$$
U_c(b,\phi)=\max_{s\in I}|F_{ss}|
=\frac{\lambda(b,\phi)}{c_\delta\,\ell(b)},\qquad
\ell(b)=(L-b)/2.
$$
幅度方程给
$$
\lambda_b=\frac{r_b}{A_\delta'(\lambda)},\qquad A_\delta'(\lambda)<0.
$$
所以
$$
\boxed{\quad
\partial_b\log U_c
=\frac1{L-b}+
\frac{r_b}{\lambda A_\delta'(\lambda)}.
\quad}
$$
结论是：

- 若 $r_b\le0$，增大 $b$ 必使这个准确中央径向二阶主项增加。
- 要使它严格下降，充要条件是准确的正向变化 $r_b>\lambda|A_\delta'(\lambda)|/(L-b)$。
- 若同时增大 $\delta$，还要计入第3节的 profile-only 主项增加，不能把两项当作同一种改善。

这些是对一个已存在正则根分支的局部敏感性结论。要比较两个有限相隔的 $b$，必须在整个连接参数区间保持所用准确分支和界，或直接给两个场完整向外比较；不能把一个点上的导数符号冒成整段比较。

在暂时冻结方向/均值常数的尺度分析中，端层的主要项像 $A/b$，中央的项像 $C/(L-b)$。两者竞争解释了为什么“越宽越好”与“越薄越好”都不正确。若 $A,C$ 没有共同准确来源，这个尺度比较不是新的实际最优宽度或证书。

## 7. Gram 和真正曲率的主项与 profile 斜率不是同一件事

对本说明的准确单位 seed，记
$$
W=F_\phi=P_\phi-\int_s^ST_\phi\,du,\qquad
q_g=a(s)\rho_0(\phi)>0.
$$
相对目标 Gram 误差准确为
$$
G_{\rm rel}-I=
\begin{pmatrix}
0&f\\ f&h
\end{pmatrix},\qquad
f=\frac{T\cdot W}{q_g},\quad h=\frac{|W|^2}{q_g^2}-1.
$$
其算子范数为
$$
\frac{|h|+\sqrt{h^2+4f^2}}2.
$$
这里的零仅是准确单位 seed 的径向恒等式，不能从该公式删除原工作场的径向 Gram 行。

端层的角导数是
$$
(T_b)_\phi=
\frac{P_{T_b}}{|Y|}
\bigl((1-\chi)T_{0,\phi}+\chi d_\phi\bigr).
$$
它没有直接的 $\chi_s$ 项。中央 $T_\phi,T_{\phi\phi}$ 由 R711(18) 的完整架连接和
$\alpha_\phi=h_\delta\lambda_\phi$、$\alpha_{\phi\phi}=h_\delta\lambda_{\phi\phi}$ 给出；它们也没有直接的 $h_s$ 项。

因此，减小径向 cutoff 斜率不能直接推出混合或角向 Gram 改善。均值的角向变化、投影架变化、完整径向积分和 $q_g$ 才是这里的主项。实际 mean 的 $v_\phi,v_{\phi\phi}$ 又通过 R709 的完整 Jacobian 与 $B$ 的交叉偏导决定，不能沿用另一个 $b$ 的角 jet 数值。

真正 principal curvature 则须继续使用 R711(19) 或现有完整 Gram/K 消费者。记
$$
b_g=T\cdot W,\qquad \sigma=|T\times W|>0.
$$
完整正交切基中的二阶项含
$$
N_{\rm surf}\cdot T_s,\qquad
\frac{N_{\rm surf}\cdot T_\phi-b_gN_{\rm surf}\cdot T_s}{\sigma},
$$
$$
\frac{N_{\rm surf}\cdot F_{\phi\phi}
-2b_gN_{\rm surf}\cdot T_\phi
+b_g^2N_{\rm surf}\cdot T_s}{\sigma^2}.
$$
单独改变 $|T_s|$ 不控制这三个量，也不控制 $\sigma$。若没有完整 $\sigma$ 正下界和全二阶包围，不能把种子的径向主项比较改写成 reach 改善。

## 8. 两种参数变化的空间影响也不同

只改 $\delta$ 而保持 $b$ 时，准确 mean 方程完全不变，所以 $v,d,w$ 及其两角 jets 不变；$\lambda$ 随 profile 改变。R711(16) 保每个中央段的完整积分及两角导数。因此准确 $F,F_\phi,F_{\phi\phi}$ 在中央段之外逐点相同，原 core/cap 与端层场保持。这是已有的 profile-only 局部化结论。

改 $b$ 时，四端层及 $v,d,w$ 都改变。虽然 $T=T_0$ 仍在固定 $U^c$，位置是从帽端的完整积分；两个支持之间的补集可能继承上方整个支持积分的变化而移动。只有完整端点闭合和原端口被保留，不能将 profile-only 的局部化结论迁给 width 变化。

这也说明原完整域、全部径向 pieces、上下片、平帽和 p4、混合点对与 all-phase 支撑都必须保留。参数选择不允许缩小后续几何费用范围。

## 9. 对当前 1/16→1/4、1/128→1/32 的严格解释

旧、新相对长度分别为：

| 对象 | 原参数 | 新参数 |
|---|---|---|
| 四端层物理总长 | $S/16$ | $S/4$ |
| 每端物理长度 | $S/64$ | $S/16$ |
| 每中央段物理长度 | $13S/32$ | $5S/16$ |
| profile 参数 | $1/128$ | $1/32$ |
| 每中央 ramp 物理长度 $\ell\delta$ | $13S/4096$ | $5S/512$ |

这张表只是精确参数代数，不是实际根或数值执行结果。

若暂固定 $r,\ell$，第3节给 profile-only 的中央主项严格增加，且比值小于
$$
\frac{1/4-1/128}{1/4-1/32}=\frac{31}{28}.
$$
但第17参数同时改变了 $b$，准确 $r$ 未知且 $\ell$ 也变，因此不能将该比值直接用于两个实际场。

对外端层，物理宽度扩大四倍，只有在共同方向与分母界下才能把 cutoff 项的 $1/b$ 成分相应缩小。其余项不能据参数名置为不变。

当前源码允许这两项精确有理值；它没有声称 R709 粗余量已经成立。新 $b=S/4$、$L_c=5S/8$ 会使这些充分余量更紧。其真实性以及实际 Newton、profile、32-stage normal 的成功仍要由本次自然执行与完整准确费用分别支付。

## 10. 哪个下一方向有已知数学理由

本说明不要求执行新的试验，只把下一次选择的理由分开：

1. **若真实完整数据指向端层转向为主要径向成本**，加宽 $b$ 有第4节的明确收益；必须同时读均值变化和中央长度代价。把 $\delta$ 暂保原值可以隔离 width 效果，并避免第3节已证明的 profile-only 中央主项惩罚。
2. **若准确中央径向二阶量主导**，增大 $\delta$ 不是降低该量的方向。减小 $\delta$ 会改善这个主项，但更窄 ramp 的工作求积、完整根误差与全域费用不会因此自动变好。
3. **若混合/角向 Gram 或小 $\sigma$ 主导**，仅按径向斜率选参数不足。需要真实 $v_\phi,v_{\phi\phi},\lambda_\phi,\lambda_{\phi\phi}$ 与完整 $F_\phi,F_{\phi\phi}$ 的来源来识别机制；现有全部外层自由变量保留。
4. **均值方向不是当前额外可调旋钮。** 在同一 $K,b$ 和已付唯一性下，$d=Nv$ 被方程固定。现 provider 的 $w$ 也固定为 $e_r$ 在 $d^\perp$ 上的单位投影。另换 $w$、角相位或方向规则会是新场定义，需要明确完整来源和对称/端口合同；不能伪装成现有 CLI 的某个 root 参数。

以上建议不把有限观察的最大约束值归因于某一项。原初值的工作 Gram、完整几何最大约束、接受计数和后来 trial 结果是不同记录；没有逐项真实证据时，不称其坏项来自 seed 曲率。

## 11. 与现有准确消费者的接线边界

完整当前路径是：

- fixed_fejer_stage_observed_normal_packet_accurate_field_input.py，720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3：绑定实际8dc9/c9ce、120源、完整同点packet与动态seed。
- 当前 whole radial，03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd：从实际seed读取全部参数，重建完整准确域，通过 reference_mean_adapter 的 WholeMean 子类复用完整积分数学。
- fixed_fejer_reference_accurate_mean_residuals.py，ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0：完整边层/补集积分数学。
- fixed_fejer_reference_seed_angular_profile_error_bounds.py，0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b：完整 R709/R710/R711/R713 算术。

原 ae67/0471 独立 literal-batch CLI 仍绑定477499/274d；当前 whole-field adapter 复用其数学，不调用旧 CLI 绑定器，也没有放宽旧来源。

ae67 已保完整 $B$ 三分量总角 jets、$K$ 三 jets、$L_c$ 和全部总方程残差；这不等于未知方向域上的 $B_d,B_{dd},B_{d\phi}$ 锐利全矩阵包围。当前0471仍以完整粗R709条件生成 $r_\pm,\zeta$，再用R710的完整保守导数界。若条件未证，whole费用返回未付状态，不是工作物理根失败或非存在。

本说明第5节的 width 导数公式没有被冒称为现已运行的费用输出。要将其用于严格实际参数敏感性证书，需要同一真实场的准确根与上述新增导数输入；本说明没有在现科学入口前增加这种要求。

## 12. 完整未付责任

本稿的 theorem 只依赖明确条件，没有消费第 17 次运行的未来报告。它没有产生新的实际 point、接受步、mean/normal root、full-angle packet、Gram/K/support、闭面、reach、幅度或非全等证书。它没有改变原预算、全部变量、32 stages、1024角胞、完整径向/尾、历史地址、typed保护、帽或all-phase范围。

profile-only 单调性与 width 敏感性是符号结论。任何实际有效性结论必须继续绑定本次完整自然返回的报告/同点不可变快照，保工作误差和准确几何分账；未知输入和未来费用仍为未付。
