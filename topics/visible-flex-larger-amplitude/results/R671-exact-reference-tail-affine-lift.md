# R671. 准确旋转参考尾的解析 lift 扩充，保留全部原自由坐标

日期：2026-11-20。会话：Astra-resume-public-20261120 / geometry_path。

**状态：解析表示与微分公式已证明；没有执行新的数值求解。** 本条接 [R669](R669-same-g-axisymmetric-tail-linear-uniqueness-and-endpoint-defect.md)，给出消除其末胞五次高度障碍的具体表示扩充。材料度量、core 条件、帽接口、原自由坐标都不改。它不证明非圆 core 可以准确接上此尾，也不把 R669 的无穷小唯一性提升为非线性不可能性。

## 1. 原空间和新的固定标量函数

沿用 R669 的准确 FullHold 端点 $T=S$、同一 $a(s)$、$R=a(S)$、帽高 $H$、材料角 $\theta=\Theta(\phi)$ 和 $\rho=\Theta'>0$。记

$$
b=a'=\sin\alpha,\qquad c=\cos\alpha,\qquad
a''=-\kappa c,\qquad c'=\kappa b,
$$

$$
I(s)=\int_s^S c(u)\,du,\qquad I'=-c,\qquad I''=-\kappa b.
\tag{1}
$$

这里的 $I$ 是由原准确 scalar 定义的积分函数，不是两个普通浮点积分结果相减后的新定义。它只须在下面 cutoff 的支撑所处的 Hold 内部使用；支撑以外直接采用零修正。[FullHold 的高度增量 oracle](../notes/2026-11-17-parallel-model-full-hold-oracle.py) 可以给出同一函数的向外包围。在末点使用字面 $I(S)=0$。

原表示是

$$
F_0=q+f e_r(\Theta)+\chi H e_z,
\qquad f=\chi\,[R+(S-s)],
\tag{2}
$$

其中 $q$ 仍是原完整角基的共享五次 Hermite 场，端点 residual 三 jet 为零；$\chi$ 是宽度 $w=.05$ 的旧 smoothstep。$e_r(\Theta)$ 与全部 $\rho$ 链保持未截断的解析角依赖。这些端口与自由坐标约定直接来自[原完整 Gram 算子](../notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py)。

取两个固定的 Hold 内部位置 $s_a<s_b<S$，并令

$$
\eta(s)=
\begin{cases}
0,&s\le s_a,\\
10u^3-15u^4+6u^5,&s_a<s<s_b,
\quad u=(s-s_a)/(s_b-s_a),\\
1,&s\ge s_b.
\end{cases}
\tag{3}
$$

所以 $\eta$ 为 $C^2$，且必须在一个严格内点后已经恒为1。可以令 $s_b\le S-h_o$，使整个最后 out ramp 都在恒1区间。更便于原代码的一种选择见第5节。

对固定外部参数 $0\le\lambda\le1$，定义

$$
\boxed{\quad
f_\lambda=f+\lambda\eta(a-f),\qquad
h_\lambda=\chi+\lambda\eta(1-\chi),\qquad
k_\lambda=-\lambda\eta I.
\quad}
\tag{4}
$$

新的场为

$$
\boxed{\quad
F_\lambda=q+f_\lambda e_r(\Theta)
 +(h_\lambda H+k_\lambda)e_z.
\quad}
\tag{5}
$$

当 core 参数固定时，(5) 对原 $q,H$ 是仿射表示；core 可变时保留原来的 $\Theta,\rho$ 非线性链。$\lambda$ 在本条中是写入模型身份的固定同伦参数，不增加未知量，也不假装整个 core 参数化是线性的。

## 2. 表示、端口与自由度的准确性质

**旧空间包含。** $\lambda=0$ 时，(5) 逐字等于 (2)，而不是旧场的拟合、重采样或投影。

**所有原自由坐标保留。** 原 $q$ 没有乘 $1-\eta$ 或 $1-\lambda\eta$。全部自由 core 高模、core 的允许二阶 jet、所有内部节点的 $Y,U,A$、以及 $H$ 均保留，原 `pack/unpack` 和 free-coordinate 维数不变。固定 core、固定 $\lambda$ 后，任意旧 $\delta q$ 对物理场的作用仍准确是 $\delta q$。若一个组合变化使物理场处处不变，则终端高度先给 $\delta H=0$，随后 $\delta q=0$，所以没有以新 lift 暗中消去旧自由方向。

**core 邻域不变。** $\eta$ 的支撑严格在 Hold 内部，旧 $\chi$ 也在 core 邻域为零。因此新修正的三 jet 在 core 邻域全零，原 core 曲线、$F_s=e_z$、允许的二阶端口及上下镜像拼接条件原样保留。

**帽的完整三 jet 不变。** 原准确 scalar 在 $S$ 满足

$$
a=R,\quad a'=-1,\quad a''=0,\qquad
I=I'=I''=0.
$$

因 $\eta=1$ 于 $S$ 的左邻域，且 $\chi(S)=1,\chi'(S)=\chi''(S)=0$，(4) 给

$$
(f_\lambda,f_\lambda',f_\lambda'')(S)=(R,-1,0),
$$

$$
(h_\lambda,h_\lambda',h_\lambda'')(S)=(1,0,0),
\qquad
(k_\lambda,k_\lambda',k_\lambda'')(S)=(0,0,0).
\tag{6}
$$

故对相同 $q$ 终端零三 jet、相同 $H,\Theta$，新旧场都满足

$$
F(S,\phi)=R e_r(\Theta)+H e_z,\qquad
F_s(S,\phi)=-e_r(\Theta),\qquad F_{ss}(S,\phi)=0.
$$

角向导数也由同一圆边界给出。将 $s\ge S$ 接为 $[R-(s-S)]e_r(\Theta)+He_z$，到换用 Cartesian 圆盘图为止，得到同一个 $C^2$ 平帽接口。所有新 cutoff 拼接处由 $\eta',\eta''$ 的零端值保证 $C^2$；不需要新的 $a'''$ 假设。

**准确同 $g$ 的末段在新空间中实际存在。** 在 $\lambda=1,\eta=1$ 的区间，(5) 简化为

$$
F_1=q+a e_r(\Theta)+(H-I)e_z.
\tag{7}
$$

取某个已有 mesh 节点 $s_j\ge s_b$，把该节点及其后的 $q$ 三 jet 取零，则原 Hermite 插值使 $q\equiv0$ 于 $[s_j,S]$。这只是证明空间含有该候选，不是在求解器中冻结这些仍然自由的变量。此时

$$
F_s=b e_r+c e_z,\qquad F_\phi=a\rho e_\theta,
$$

所以该整段准确满足

$$
|F_s|^2=1,\quad F_s\cdot F_\phi=0,
\quad |F_\phi|^2=a^2\rho^2.
\tag{8}
$$

若 $s_b$ 本身选为已有节点，则准确段可以直接从 $s_b$ 开始。此前的共享五次胞仍能接任意原 core jet 与这个零 residual 端口，因而整个表示是 $C^2$ 的；但此前的 metric、浸入、嵌入与 reach 尚须真正求解和验证。本条没有声称这个显式连接也等距。

## 3. R669 的 $t^8$ 缺项怎样被准确补上

沿用 R669 的 $t=S-s$ 和原 out ramp 常数 $A,B,C$：

$$
\beta(t)=\alpha(S-t)+\pi/2=At^4+Bt^5+Ct^6.
$$

由 $c=\sin\beta$ 与 (1)，准确参考高度满足

$$
z_*(S-t)=H-\frac A5t^5-\frac B6t^6-\frac C7t^7+O(t^{13}).
\tag{9}
$$

因此它不是最后单元的五次高度。为直接核对 R669 的具体缺项，令一个轴对称高度暂写为

$$
z=H+b_5t^5+b_6t^6+O(t^7).
$$

使用 $a=R+t+O(t^9),a'=-1+O(t^8)$，Darboux 左端 $z_{ss}\,aa'z_s$ 的 $t^7,t^8$ 系数分别为

$$
100R b_5^2,\qquad 100b_5^2+270R b_5b_6.
$$

代入 (9) 的 $b_5=-A/5,b_6=-B/6$，便得到

$$
4RA^2,\qquad 4A^2+9RAB,
$$

与 R669 的准确右端一致。新增的 $b_6$ 恰好支付原严格五次高度没有的 $9RAB$。

这不只是有限阶匹配：$z_s=c,z_{ss}=\kappa b$ 使准确 Darboux 方程两边都等于 $a\kappa c b^2$；完整 Gram 已由 (8) 直接恒等验证。因而 $\lambda=1$ 的新空间确实消除了该特定末胞表示障碍，而不是把它推迟到另一个有限 Taylor 阶。

仅作 $\chi H\mapsto\chi(H-I)$ 不具有这里的结论，因为 $\chi$ 在任何 $S$ 前邻域都不恒为1，剩余 $(1-\chi)I$ 从 $t^8$ 开始。只把径向 lift 加上 $\eta[a-(R+S-s)]$ 也不能宣称包含准确参考：末段会剩下需要由 $q$ 补偿的 $(1-\chi)(R+S-s)e_r(\Theta)$，它一般既含径向六次项，又带未截断的材料角依赖。(4) 直接把完整旧径向 lift 换成准确 $a$，避开这两个表示问题。

## 4. 完整真实微分，不复用旧高度列

固定 $\lambda$ 后，三个 scalar profile 及其两阶导数是新的已知数据。除旧 $f',f'',\chi',\chi''$ 外，所需准确公式为

$$
f_\lambda'=f'+\lambda[\eta'(a-f)+\eta(b-f')],
$$

$$
f_\lambda''=f''+\lambda[\eta''(a-f)+2\eta'(b-f')
                         +\eta(-\kappa c-f'')],
$$

$$
h_\lambda'=\chi'+\lambda[\eta'(1-\chi)-\eta\chi'],
$$

$$
h_\lambda''=\chi''+\lambda[\eta''(1-\chi)
                                  -2\eta'\chi'-\eta\chi''],
$$

$$
k_\lambda'=\lambda(\eta c-\eta'I),\qquad
k_\lambda''=\lambda(-\eta''I+2\eta'c+\eta\kappa b).
\tag{10}
$$

记 $r=e_r(\Theta),\tau=e_\theta(\Theta)$。物理六 jet 为

$$
\begin{aligned}
F&=q+f_\lambda r+(h_\lambda H+k_\lambda)e_z,\\
F_s&=q_s+f_\lambda' r+(h_\lambda'H+k_\lambda')e_z,\\
F_{ss}&=q_{ss}+f_\lambda'' r+(h_\lambda''H+k_\lambda'')e_z,\\
F_\phi&=q_\phi+f_\lambda\rho\tau,\\
F_{s\phi}&=q_{s\phi}+f_\lambda'\rho\tau,\\
F_{\phi\phi}&=q_{\phi\phi}
             +f_\lambda(\rho_\phi\tau-\rho^2r).
\end{aligned}
\tag{11}
$$

所有 $q$ 的角导数仍含原旋转 $\phi$ 标架的 connection，不能把分量数组当作固定 Cartesian 向量再微分。

原 core 方向给出的 $\delta\Theta,\delta\rho,\delta\rho_\phi$ 不变；$a,I,\eta$ 不依赖 core。于固定 $\lambda$，除原 $\delta q$ 相应六 jet 外，新增 lift 的准确线性化是

$$
\begin{aligned}
\delta F&=f_\lambda\delta\Theta\tau+h_\lambda\delta H e_z,\\
\delta F_s&=f_\lambda'\delta\Theta\tau+h_\lambda'\delta H e_z,\\
\delta F_{ss}&=f_\lambda''\delta\Theta\tau+h_\lambda''\delta H e_z,\\
\delta F_\phi&=f_\lambda(\delta\rho\tau-\rho\delta\Theta r),\\
\delta F_{s\phi}&=f_\lambda'(\delta\rho\tau-\rho\delta\Theta r),\\
\delta F_{\phi\phi}&=f_\lambda\big[(\delta\rho_\phi-\rho^2\delta\Theta)\tau
 -(\rho_\phi\delta\Theta+2\rho\delta\rho)r\big].
\end{aligned}
\tag{12}
$$

独立固定项 $k_\lambda$ 不产生未知量方向，但必须加入真实基场，不能从 residual 或曲率读出中省略。原 metric 分母 $a\rho$ 及其 core 导数也不变。

例如六 jet cotangent 按 (11) 顺序记为 $g_0,g_s,g_{ss},g_\phi,g_{s\phi},g_{\phi\phi}$。高度的逐点转置贡献是

$$
h_\lambda(g_0)_z+h_\lambda'(g_s)_z+h_\lambda''(g_{ss})_z.
\tag{13}
$$

core 的三个标量 cotangent 则为

$$
\begin{aligned}
g_\Theta={}&f_\lambda g_0\cdot\tau+f_\lambda' g_s\cdot\tau
 +f_\lambda''g_{ss}\cdot\tau
 -f_\lambda\rho g_\phi\cdot r-f_\lambda'\rho g_{s\phi}\cdot r\\
 &-f_\lambda(\rho_\phi g_{\phi\phi}\cdot r
                       +\rho^2g_{\phi\phi}\cdot\tau),\\
g_\rho={}&f_\lambda g_\phi\cdot\tau+f_\lambda'g_{s\phi}\cdot\tau
          -2f_\lambda\rho g_{\phi\phi}\cdot r,\\
g_{\rho_\phi}={}&f_\lambda g_{\phi\phi}\cdot\tau.
\end{aligned}
\tag{14}
$$

再按原 Fourier core 链转置，并加原 $q$ 端口及 metric 分母贡献。角 orbit、径向 quadrature 和谱目标权的约定不变，仍须各自准确计入一次。

## 5. 保持高度补偿为原五次空间的便捷 cutoff

可令 $s_b=S-w$，并把 $s_a$ 选为更早的已有 Hold mesh 节点。旧 $S-w$ 已是原观察计划的 symbolic 节点；$w=.05>h_o=.02$，故此 $s_b$ 在 out ramp 之前。整个 $[s_b,S]$ 仍使用原弯曲度量，**不是提前出现的 flat collar**。

此选择使 $\eta\chi=\chi$，故一般式 (4) 等价于

$$
f_\lambda=(1-\lambda)f+\lambda\eta a,
\qquad h_\lambda=(1-\lambda)\chi+\lambda\eta,
\qquad k_\lambda=-\lambda\eta I.
\tag{15}
$$

由于 $\eta,\chi$ 的 break 都是 mesh 节点，$h_\lambda$ 是原节点划分上的准确 $C^2$ 分段五次函数。因此，若原物理高度方向用某个同空间的 $B(s)$（core 零三 jet、帽端 $(1,0,0)$），可把补偿列准确写成

$$
\delta H=1,\qquad \delta q_Z=B-h_\lambda,
\qquad\Longrightarrow\qquad \delta F=B(s)e_z.
\tag{16}
$$

它能由原节点三 jet 精确编码，无须把一个十次的 $\eta\chi$ 乘积默默插值回五次空间。若选择一般的、与 $\chi$ 过渡重叠的 $\eta$，(4) 仍然数学有效，但这个准确五次高度补偿性质不自动成立，必须显式重做相应坐标图。

## 6. 真正接代码时的范围与尚未支付事项

原 free-coordinate 布局、mesh、固定 scalar $a$、$R$、core 条件、相对 Gram 三方程、原所有角行和径向观察行都可保留。lift 数据由旧六列扩为九列，例如按 $(h,h',h'',f,f',f'',k,k',k'')$ 明确储存；节点、中点、Gauss、任意位置、全空间 Jv/VJP、coarse 列及曲率 cotangent 必须共同消费 (10)–(14)，不能只改一个 residual 入口。

每个新实际场的身份须记录 $\lambda,s_a,s_b$、原 scalar/oracle 身份及新 lift 源。改变 $\lambda$ 一般会改变真实物理场；旧 $q$ 数组可以作为新候选坐标，但不能把它冒充未变的旧曲面。未截断的 $e_r(\Theta)$ 也使一般的径向 recenter 不能靠有限角投影得到准确的旧场等价变换。

R656 等旧区间几何实现依赖原 polynomial lift；新 $f_\lambda,k_\lambda$ 含准确非多项式 $a,I$，须扩展为消费这些 scalar 的向外包围和余项。旧连续 metric、curvature、embedding、diameter、held 或 reach 证书均不自动继承。证明 (8) 支付的是候选所含的准确末段；连接区与完整闭面、全 $t$ 家族、可见幅度和 reach 比例仍按课题 README 原完成标准真正求解、验证。

所有后续数值试算在本仓库公开 GitHub Actions 执行。本条没有新数值结果，没有把 R669 线性固定帽唯一性当作非线性存在或不存在的结论。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
