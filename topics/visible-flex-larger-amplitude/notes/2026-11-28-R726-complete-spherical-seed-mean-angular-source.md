# R726 独立球面端层：完整 seed、三均值及两阶角导数的实际源码

2026-11-28（UTC）。本文件记录一个独立的新端层实现。它从已刊 R725 的完整 seed 和原完整 f848 均值核派生，真正替换端层的值、均值函数、三维 Jacobian、径向导数及两阶角导数。已经形成完整可调用源码，但尚无该新 seed 的公开科学返回。本文不填入未来模型、根、角、场、误差或速度数据，也不改变正在运行的25、26或另行交付的按需计算候选。

正式准确对象及条件定理来自 [R726](../results/R726-spherical-boundary-strong-monotonicity-and-positive-mean-root.md)。[R725](../results/R725-fixed-width-boundary-cutoff-and-curvature-decomposition.md) 的固定宽度三片 cutoff、[R724](../results/R724-paired-halfwave-central-seed-and-complete-source-identity.md) 的相反成对半波和 [R711](../results/R711-smooth-triangle-central-profile-and-geometric-comparison.md) 的十二片辅助幅度积分继续使用原定义。这里没有把 R709 的欧氏闭球势或 R722 针对旧归一化线段的后验公式改名为球面证明。

## 1. 两份完整运行体与实际父源

|角色|完整文件|字节|SHA256|Git blob|
|---|---|---:|---|---|
|新均值/球面导数核|fixed_fejer_R726_spherical_seed_mean_jets.py|48226|2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23|9f7ea1805326a317a281e8c3f6c7cb6ef9709890|
|新完整 seed|fixed_fejer_R726_spherical_halfwave_meridian_reference.py|52457|176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a|231bad2fba5f80ade672703114fe5bd776512baf|
|直接均值父源|supported_smooth_triangle_seed_mean_jets.py|34725|f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917|ee318b8971ce3c3d10715fbcd648c3a3bcfd6712|
|直接 seed 父源|fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py|51540|1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f|b37f930874dd9b874d58120a2d9fe86031146ccb|
|正式 R726 全文|R726-spherical-boundary-strong-monotonicity-and-positive-mean-root.md|27362|faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b|1397c01f1155ebda224441039a3950ce03c2417a|

运行文件位于本题 scripts/resume_20261126。R726 已在 b70f4044ba43bd298d3cb64b40098490bc2e7f06 发表；R725 科学父族的完整22运行体及137角色表在95801769a95b2940b14ad01fe7640581b2c2fb44发表。本交付的两个新 blob 只作独立来源保护，不能把旧族的执行记录写成新族执行。

seed 构造接口不增加参数：仍为 SupportedUnitMeridianJet(problem, prepared, expected_bundle_sha256=..., seed_parameters=..., mean_kernel_module=..., cache_directory=...)。完整 mean_module 改钉新均值全体，构造器同时核验 solve_mean_jets、原 smooth_triangle_value_and_derivative、新 spherical_boundary_jets 和 spherical_boundary_definition 的真实源码文件。原参考 e717 完整来源及 fixed Fejér 标量、全160 core、H 和 reference bundle 身份仍逐项核验。

新的 schema 分别为：

- complete-R726-spherical-boundary-paired-halfwave-seed-working-mean-and-angular-jets-v1；
- complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1。

上层完整来源表必须真正改钉这些新身份并重新生成自身校准、模型和报告；不能只更换 schema 文本后继续声称原均值或场已验证。

## 2. 准确端层及完整三均值方程

固定材料坐标 s、原两个支撑 U、四个端层 E、原中央总长 Lc、原 cutoff chi(s) 和准确原单位切向 u(s,phi)。这些对象沿用完整 R725 端口和全部切点；chi 与 phi 及待解均值方向无关。

对单位 u,d 且 u != -d，theta=acos(u·d)，准确插值为

\[
 {\cal S}_{\chi}(u,d)
 = f_{1-\chi}(q)u+f_\chi(q)d,\qquad
 q=1-u\cdot d,\qquad
 f_a(q)=\frac{\sin(a\arccos(1-q))}
              {\sin(\arccos(1-q))}.
\]

在 u=d 处取解析延拓。固定当前参考角的准确目标仍是完整 P-Gamma-补集积分 K。新方程是

\[
 {\cal R}(v,\phi)=L_c v+B(v,\phi)-K(\phi)=0,\quad
 B(v,\phi)=\int_E {\cal S}_{\chi(s)}(u(s,\phi),N(v))\,ds,
 \quad N(z)=z/|z|.
 \tag{1}
\]

这是三个真正耦合的均值未知量。令 r=|v|、d=N(v)、alpha=Lc r，便得到 R726 的 alpha*d+B(d,phi)=K。新源实际重算 B，而不是沿用旧 B 后添加一个球面标签。

全部原 boundary Gauss 节点、正权、节点顺序、径向精确分片和标量尾责任保留。工作方程只是把完整积分替换为这些原有正权求和。原权重不重新归一化，不筛掉难角；不采用旧均值缓存或旧校准值。原 mean cache 在每个新 seed 对象中从空的内存字典开始，按真实 fixed-chart 角的 binary64 hex 保存完整新根及两阶角导数。它不从旧 raw NPZ 载入旧均值。

新代码不把急角条件作为额外数值准入门。工作算术仅在非零输入且非对跖的可用插值域内计算；实际对跖、非有限、零范数或不可用导数仍保留真实失败。即使一次工作 Newton 完成，也没有证明全角急角域、R726 球冠存在条件或全域分支关联。

## 3. 零角解析系数、实际递推和截断责任

直接在 theta=0 计算 acos 的导数或 sin(a*theta)/sin(theta) 会制造工作奇点。因此实现使用 q 作为光滑系数变量。对准确单位输入，

\[
 q=\tfrac12|u-d|^2=1-u\cdot d.
\]

工作代码也从两次真实归一化后的完整差向量求 q；它没有夹断 dot product，没有把负范数、对跖角或非有限值替换成一个可用场。

由二类 Chebyshev 的对应微分方程，或者直接对 f 的三角表达式求导，

\[
 (2q-q^2) f_a''+3(1-q)f_a'+(a^2-1)f_a=0.
\]

设 f_a(q)=sum c_n(a)q^n，则逐次系数比较给出

\[
 c_0(a)=a,\qquad
 c_{n+1}(a)=
 \frac{(n+1)^2-a^2}{(n+1)(2n+3)}c_n(a).
 \tag{2}
\]

例如 c1=a(1-a²)/3；a=1 时所有高阶系数为零。a=1/2 时对应 f=.5(1-q/2)^(-1/2)，也是同一递推的解析校核。这些是符号恒等式，没有执行数值 fixture。

工作小角分支为 0<=q<=1/4，完整保留 n=0,...,32。三个 Horner 变量在每一步同时更新：

\[
 (p_2,p_1,p)\leftarrow
 (q p_2+2p_1,\ q p_1+p,\ q p+c_n).
 \tag{3}
\]

因此一阶、二阶 q 导数是同一个实际系数数组的多项式导数。源码没有借另一张独立舍入的导数系数表冒充原多项式导数。

径向导数还需要 a 导数。设 g_n=dc_n/da，则从同一次递推得到

\[
 g_0=1,\quad
 g_{n+1}=r_n g_n-\frac{2a}{(n+1)(2n+3)}c_n,\quad
 r_n=\frac{(n+1)^2-a^2}{(n+1)(2n+3)}.
 \tag{4}
\]

每步用原 c_n/g_n 同时产生下一项，之后对 g 表用同样的 Horner 求值。这里区分了“同一浮点程序的形式导数”与“对离散舍入映射本身求微分”：后一种不是原求解器或自动微分的数学语义。q 导数严格针对已实际生成的多项式；a 导数沿生成该系数的同一计算图传播。

对 0<=a<=1，有 0<=r_n<1/2，因此

\[
 0\le c_n\le 2^{-n}.
\]

又有 2^{n+1}|g_{n+1}| <= 2^n|g_n|+4/[(n+1)(2n+3)]。用 sum_{k>=1}1/k²<2 得 |g_n|<5*2^{-n}。令 rho=q/2<=1/8、m=33，精确无限级数的截断尾满足

\[
 |E_0|\le\frac{\rho^m}{1-\rho},
\quad
 |E_1|\le
 \frac12\rho^{m-1}\frac{m-(m-1)\rho}{(1-\rho)^2},
\]

\[
 |E_2|\le\frac14\rho^{m-2}\left[
 \frac{m(m-1)}{1-\rho}
 +\frac{2m\rho}{(1-\rho)^2}
 +\frac{2\rho^2}{(1-\rho)^3}\right],
\quad
 |E_a|\le\frac{5\rho^m}{1-\rho}.
 \tag{5}
\]

式(5)的一阶、二阶界分别来自 (1/2) sum_{n>=m} n rho^{n-1} 与 (1/4) sum_{n>=m} n(n-1)rho^{n-2}，保留 rho=q/2 的链导数。q=0 用连续值；对剩余 q，以上尾项逐项单调，所以可代 rho=1/8。只有在这一端点，前因子才可分别写为 4rho^m 与16rho^m；它们不作为较小 q 的逐点公式。具体得到严格上界 2^-98、2^-91、2^-84、2^-96。它们分别只描述准确系数的函数、q 一阶、q 二阶、a 一阶截断误差。它们**不包含**系数生成的浮点误差、Horner 舍入、输入归一化、真实 q 载体误差、输出归一化、三角函数、积分、根或全场误差。源码将这个边界直接写入 spherical_boundary_definition 的 scope，没有把这些小尾数当成准确场已支付的误差。

在 q>1/4 且 q<2 的工作分支，源码实际使用 theta=acos(1-q)、sin(theta) 和 sin(a*theta)，完整求值相应的链导数。设 z=1-q，则

\[
 \theta_q=(1-z^2)^{-1/2},\qquad
 \theta_{qq}=-z(1-z^2)^{-3/2}.
\]

令 s=sin(theta), c=cos(theta), n=sin(a theta), h=cos(a theta)，有

\[
 f_\theta=ah/s-nc/s^2,\qquad
 f_{\theta\theta}=(1-a^2)n/s-2ahc/s^2+2nc^2/s^3.
\]

源码用 f_q=f_theta theta_q、
f_qq=f_thetatheta theta_q²+f_theta theta_qq，
以及 f_a=theta*cos(a theta)/sin(theta)。大角分支不被调用于零角。a=0/1 的系数值和 q 导数使用其准确常数恒等式；a 导数仍保留完整表达式。

两个工作分支在 q=1/4 处只在准确无限表达式下相同，有限多项式与三角工作式不是一个逐字相同、数学上精确 C² 的函数。本源码和元数据明确不作这样的声明。其切换/截断/舍入属于后续工作到准确场的误差责任；不能把本说明转换为未经支付的连续几何证书。

系数只依径向 cutoff，不依角度。实现保存33份 P 维系数和33份 a 导数，而不是33份完整 P×A 网格；全角网格仍逐点原样计算。这个存储布局没有丢掉任一角或径向点，也不产生速度宣称。

## 4. 实际工作映射及完整三维 Jacobian

为在有限算术中保留单位输出的明确计算语义，实际工作图是

\[
 u=N(x),\quad d=N(y),\quad e=u-d,\quad q=e\cdot e/2,
\]
\[
 A=f_{1-\chi}(q),\quad B=f_\chi(q),\quad
 R=A u+B d,\quad T=N(R).
 \tag{6}
\]

准确 Slerp 的 |R|=1，所以最后一个 N 在准确域上是恒等变换。工作代码实际执行它，因而它的一阶、二阶导数全部保留。没有把这一额外的浮点归一化当作误差零。

记 D_x=DN(x)、D_y=DN(y)、D_R=DN(R)，C=A_q u+B_q d。对于均值原坐标 y 的任意完整三维扰动，

\[
 dq=(d-u)\cdot D_y\,dy,
\]

\[
 D_yT=D_R\{B I+C\otimes(d-u)\}D_y.
 \tag{7}
\]

函数 _spherical_y_jacobian 返回完整 P×A×3×3 数组。所有原正权求和后，Newton 真正使用

\[
 J_v=L_c I+\sum_p w_p\,D_yT_p.
 \tag{8}
\]

它不是原 integral chi*DN(Y) 的简单换名。新代码删掉旧矩阵 M 的欧氏 PSD 注释和旧表达式，不声称完整三维 J_v 对称。原 _checked_solve 仍用完整3×3矩阵求解，不将它替成标量/对角近似，不缩减任何一个均值方向。

在准确急角域，R726 证明的方向 Jacobian 与(8)一致。对 v!=0，将 dv 分解为 dr*d+r*dd，其中 d·dd=0。于是 Lc*dv=d*dalpha+alpha*dd，且 B 仅依 N(v)。alpha=Lc*r 的径向导数与两个切向方向共同组成完整三维坐标。这解释了保留原三维 Newton API 的数学合法性，而不将球面方向变量误降成一个径向变量。

## 5. 两阶角导数：同一个完整图

原参考角 phi 是实际求导变量。外层当前自由参数不是这些固定 seed 均值的输入。原 seed 已冻结 fixed target core/H、完整标量与 reference；新源保留这个作用域。它没有 detach 一个本来活动的外层参数，也没有把 Newton 迭代过程的自动微分当作隐式根导数。

对任意 x(phi)、y(phi)，有

\[
 u_1=DN(x)x_1,\quad
 u_2=DN(x)x_2+D^2N(x)[x_1,x_1],
\]
\[
 d_1=DN(y)y_1,\quad
 d_2=DN(y)y_2+D^2N(y)[y_1,y_1].
\]

原完整 _normalization、_D2N_same 和 _apply 函数在新均值源中逐字保留。记 e1=u1-d1，则

\[
 q_1=e\cdot e_1,\qquad
 q_2=e_1\cdot e_1+e\cdot(u_2-d_2).
 \tag{9}
\]

cutoff 对 phi 固定，所以

\[
 R_1=A u_1+B d_1+q_1(A_q u+B_q d),
\]

\[
 \begin{split}
 R_2={}&A u_2+B d_2+
 2q_1(A_q u_1+B_q d_1)\\
 &+q_2(A_q u+B_q d)
 +q_1^2(A_{qq}u+B_{qq}d).
 \end{split}
 \tag{10}
\]

最终

\[
 T_1=DN(R)R_1,\qquad
 T_2=DN(R)R_2+D^2N(R)[R_1,R_1].
 \tag{11}
\]

_spherical_angle_jets 实际逐项实现(9)–(11)，保留两个输入归一化的法向加速度、参考与均值的所有混合项，以及最后输出归一化的二阶项。零角时 q=0、C 和所有系数导数有限，因此没有 acos'(1) 或 0/0 进入该分支。

对完整工作均值方程，先固定 y1=y2=0，由同一图算部分 B_phi：

\[
 J_v v_1=K_1-\partial_\phi B.
 \tag{12}
\]

得到 v1 后，再令 y2=0，x1=T1、x2=T2、y1=v1，完整求出 B2_known。这包含所有已知二阶项，而不是只保 reference acceleration：

\[
 J_v v_2=K_2-B_{2,\mathrm{known}}.
 \tag{13}
\]

将真实 v2 放回同一图求完整 B2，保留三分量工作残差
Lc*v1+B1-K1 和 Lc*v2+B2-K2。它们是实际计算读数，不是统一角域误差界。

R726 用 d''=w-|d'|²d 表达的球面法向加速度在这里来自 D²N(v)[v1,v1]。它没有因为改用 v 坐标而消失。全部完整 J_v、根及残差仍在原数组结果和 raw batch 中返回。

## 6. 径向导数与原端口

同一个边界点沿 s 变化时，均值 y=v(phi) 对 s 固定；参考 x=T0(s,phi) 和 chi(s) 变化。因此

\[
 u_s=DN(x)x_s,\quad q_s=(u-d)\cdot u_s,
\]

\[
 A_s=A_q q_s-f_{a,\,a}|_{a=1-\chi}\chi_s,\qquad
 B_s=B_q q_s+f_{a,\,a}|_{a=\chi}\chi_s,
\]

\[
 R_s=A u_s+A_su+B_sd,\qquad T_s=DN(R)R_s.
 \tag{14}
\]

_spherical_radial_jet 实际保留参考转向和 cutoff 转向两项，不能只返回 theta*chi_s 的速度估计。原完整 R725 chi/chi_s 载体和实际 B,C,Bs,Cs 四标量全保留。准确 theta*chi_s 是 R726 对 cutoff 分量的几何解释，不是完整 T_s 的替代物。

R725 chi 在外端为0、内端为1，前3阶端口导数为零。准确 Slerp 因而在外端给 u 与全部参考端口，在内端给 d、径向导数0；角导数也按同一解析延拓接合。R724 中央半波在两端一二导数为零。新实现保全部原支持、8个 boundary 内切点、每中央6个 physical profile 片及补集原 field。它没有把“精确端口接合”冒成已量化的浮点逐字端口误差。

原 raw h*Delta lift、所有当前 core/omega/H 自由量、bubble 和32段法向链不在这两个最小文件中被改写。本交付不删去原 raw closure defect，也不把 T 冒充完整上层 F_s。上层继续须调用完整原 lift 和全部校准。

## 7. 工作求根与预算逐项保留

solve_mean_jets 的完整签名及参数语义保留：

- K0/K1/K2、e0/e1/e2 为完整(A,3)；
- T0/T1/T2 为完整(Pb,A,3)，chi/weights 为完整(Pb,)；
- profile_delta、profile_quadrature_order、maxiter、tolerance、
  scalar_iterations、mean_backtracks、mean_armijo 继续完整传入；
- 每角仍从 v=K0/Lc 开始原三维 Newton；
- 只更新尚未达到同一原三分量 Euclidean tolerance 的角；
- 每次 backtrack 仍对同一完整边界规则、同一新方程评价；
- 原 alpha=1 起、逐次乘1/2、原严格下降及原 Armijo 双不等式全保；
- 每批原所有活动角都必须接受，失败角不被丢弃；
- 原128、24、64、16等默认值不减少；实际运行仍由完整原参数对象传入；
- 原三均值、一个幅度和全部两角导数保留，没有改成逐角单变量近似。

代码中从完整 Newton step 求解到 backtrack/接受/更新计数的3293字节与 f848 原文完全相同，SHA256为30ebaa0986370945ac0f95f2bc9964ef85ba4aa6a2491241393dcb030d6dab6a。变的是它实际收到的新均值值和完整 Jacobian，不是预算或接受规则。

_trial_mean_residual 对每个实际提出的完整角求新球面值。实际输入范数、q、对跖与输出范数不可用的对保留 NaN/false availability，不用有限假值通过接受比较。仍把完整 trial、残差、alpha、可用与接受状态放在原失败记录中。工作 root 的 domain rejection 不是 R726 急角存在定理已经被检验。

新 kernel 的 complete=True 只沿原工作求解成功语义：实际新均值、幅度、完整三分量闭合达到原 tolerance，且全部返回数组有限。R726_acute_existence_uniqueness_verified、quadrature_and_floating_errors_enclosed、accurate_global_branch_association_verified 等仍明确 false。actual_sampled_acute_pairs 只报告这一次有限工作样本，不能升级成全域结论。

## 8. 原中央、幅度、投影 frame 与全残差保持

原 _twelve_piece_profile 保留全部12个准确 R711 polynomial 片、每片原 positive Gauss、未归一化权重、原数组顺序。没有将其缩为一季度、一个正半波或物理6片。

完整中央幅度流程仍逐角实际求 a_delta(0)、a_delta(pi)，要求真实工作 bracket a_pi<|v|<a_0。它不把工作 a_pi 强制设为准确值0。原64次 bisection、同一 scalar tolerance、与完整新 B 合成的三分量 physical closure tolerance 都保留。新 B 改变 |v|，所以 lambda 必须真实重算；不得借旧 lambda。

随后原公式

\[
 r'=d\cdot v',\quad
 r''=d\cdot v''+(|v'|^2-r'^2)/r,\quad
 \lambda'=r'/a',\quad
 \lambda''=(r''-a''\lambda'^2)/a'
\]

及投影 w=N(e0-(e0·d)d) 的全部两阶角导数逐字保留。原所有 combined closure、一阶与二阶三分量残差和真实数组身份仍完整返回。

从 central_amplitude_bracket 到最终边界诊断字段前的6613字节完整原文一致，SHA256=951e6382ab47a4cba7a531b387bebb3a98d463d7bf204d5c73998264b5d95443。这包含原幅度二分、lambda 两角、投影 frame、全 physical 三分量 residual 和有限性读回，不只是一个函数摘要。

seed.evaluate 中原 physical_paired_central_field 的772字节也逐字同父，SHA256=49188a593ea55dfec7d33202f4f899d2e4ba46ba2ab6ff29b312a986410a79cd。两 equal central interval 的 transverse mean 仅在完整相反两半波合起来才为零；本实现没有把任一单独 interval 误写成自身平均横向为零。

## 9. 均值与场实际消费同一原坐标

原 seed 已经在完整 mean cache 和 raw batch 中保存 v、v_phi、v_phiphi。旧 evaluate 仅取 d/w/lambda。新 _means 现在把已保存的完整 v jets 也返回给 evaluate，没有增加求根、径向采样或额外角。

新边界 evaluate 调用：

    spherical_boundary_jets(
        T, T_phi, T_phiphi,
        mean["v"], mean["v_phi"], mean["v_phiphi"],
        chi, Ts=T_s, chi_s=chi_s)

这样均值 B 和实际场查询都从同一 raw v 开始同一个 N(v) 图。它不会在一个地方使用 raw v、另一个地方把已归一化 d 再当 raw 坐标求不同的浮点链。

输出仍为完整原 T0、T0_s、T0_phi、T0_phiphi 数组，shape、literal material angles、原 current-free-variable scope、readonly finite结果合同不变。新 helper 的科学函数仍只允许该公开 repository 的 Actions 环境。本文生成源码时没有执行这些函数。

## 10. 精确径向划分和现有 hotspot 的严格解释边界

原 _prepare_plan 完整9379字节中，只有报告 schema 换为 new R726，数值、排序、精确 affine 运算、分片和全部实际输入保持原字。新体对应9391字节。原 _chart 1349字节和 _radial 1196字节也完全原样。源码没有因 Slerp 增删一个原 Gauss 节点、tail 或 support boundary。

对已公开的25有限 hotspot：
cell=885，u=.8306046932331322，显示 s=2.1573631007205925。
maker89cc 的原完整 exact node construction 有819个前缀节点，然后4、8、64、12、16段；索引830到894是
[A,S-width] 的64个等分，其中

\[
 A=cut+f+hold+rise.
\]

cell885 对应此块 j=55 的区间。若 u 按该真实 binary64 字解释为准确有理数，置 t=(55+u)/64，则该 literal point 的准确 affine 定义为

\[
 s=tS+(1-t)A-t\,width.
 \tag{15}
\]

这里 A 和 width 使用 maker 的原 binary64 常数所代表的准确分数，不用显示小数代换实际 carrier。这个结论只识别原 working mesh 的 exact-affine64格块。没有当前实际 S 及其完整绑定，本文不把显示 s 反推为准确 S，不宣称该点一定是 seed 的 boundary、central 或 cutoff 子片，不依据 cell 编号猜曲率主因。该已有观察不会成为新 seed 的输入或验证门。

## 11. 全来源、完整再生与本地工作范围

完整再生器 reproduce_fixed_fejer_R726_spherical_seed_sources.mjs 从两份上述完整父文件读取每一字节，核验各自 size/SHA，按公开全部原文/替换文本生成两份独立新文件；每个 patch 有唯一原文锚及逆向文本。全部11个 mean 替换、13个 seed 替换可逆回原 f848/1533 完整体。新工作源不是对旧文件的就地覆盖。

本次已经做的验证仅是源码文字构造、完整字节数、whole hash、逐处文字逆变换回完整父源以及明确不变数学段的文字相等。没有 Python 导入、AST、compile、fixture、局部科学、benchmark、真实场或 root 计算；也没有新增独立机器审核门。科学求值只应在实际完整新运行中发生。

执行再生器的完整接口是：

    node reproduce_fixed_fejer_R726_spherical_seed_sources.mjs \
      --source-directory <包含两份完整父源码的目录> \
      --generated-directory <独立完整新源码目录>

它只读写源码文本，不输入或输出科学数组。两父的 exact Git blob 可直接恢复每一字节；不把仅有摘要当完整来源。新 mean 的 source SHA 再由完整 seed 的 MEAN_KERNEL_SHA 真正硬绑定。

## 12. 后续完整上层与准确费用责任

本最小交付没有声明整套 solver/geometry/pure/fee 已适配。后续独立上族应以真实 R725完整22运行体为机制父，递归传播新 mean/seed/base/Q/normal/calibration/packet/source/policy身份；原全部自由量、32stage、当前137完整来源、数值预算、历史和未知 peer 必须保留。不得把25/26或按需候选的实际结果当作新 Slerp 模型结果。

新 target metric 仍由原 fixed Fejér 完整 scalar/chart定义；改变的是固定 seed 及其参考参数化和校准。相同原点词并不自动代表同一个物理 seed 场，更不允许迁移旧 root、closure、已接受步或连续证书。旧 typed/provenance 全保留其原来源和未知责任。

准确费用尤其不能直接调用旧 R722 posterior_mean_root_domain，因为其 B、Jacobian、势、条件及误差传播对象不同。需要完整新的 R726 同场准确端层/均值域/角2责任：全准确 reference 及 cutoff 片、complete quadrature/tail、整角胞急角或适用范围、真实 alpha/r 的正性、R726 球冠存在/唯一性、root enclosure、完整角导数界与当前 normal roots 的同支关联。缺项保未付，不以 working complete 或有限 sampled acute=true 顶替。

物理闭面、上下反射、帽、固定Cartesian markers、全时间相位、完整 reach/Gram、握持和 R716 十二矩仍由各自完整实际后继承担。本交付既不继承这些旧证书，也不缩减它们。没有数据支持速度、收敛、可行性或目标改善的实测结论。

完整实际返回状态：new scientific run=null；actual mean/root/model/field/point identity=null；准确域/误差/全场证书未付。这些 null 是未知，绝不是已完成或空历史。
