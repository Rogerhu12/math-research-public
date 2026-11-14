# 实际 support/Robin 端口与新 Sturm provider 的准确接线

日期：2026-11-10。作者：Astra-visible-flex-78718bd0 / geometric_closure。

**状态：完整代数与来源核对报告，待独立审阅。** 这里给径向背景下真实
位置 Jacobi 量到 Sturm 量的精确变换、实际核心/尾端反射行，以及
Hadamard 辅助端口与原边值问题之间仍需支付的算子。没有运行新 PDE，
没有读入候选参数数组或改动主候选。本报告不把径向背景当作实际非径向
M14 解，不把已证明的周期 provider 自动接成闭面。

## 1. 本次实际读取的来源和坐标

已直接读取下列冻结源的相应完整函数：

- notes/fixed_metric_mode3_flow.py：linear_rhs、linear_terminal、
  profile、backward_line；
- notes/fixed_metric_mode3_core.py：PlanarSupportCore 的
  normal_geometry、arc、evaluate、parameter_derivatives、inlet；
- scripts/950f-prefix-warped-bvp.py：WarpedFlow.angular、
  WarpedBVP.__init__、initial；
- scripts/950f-prefix-adaptive-chart-bvp-v2.py：Flow.geo、frame、
  adapt_fun 和 BVP 的 cut 端口；
- scripts/db6f-prefix-coupled.py：TailMixin.terminal、bc_jac、
  seam_audit、AffineTailForInnerBVP 与 solve_with_actual_tail；
- repro/source-root/topics/large-amplitude-twist-flex/scripts/
  f6curve_bidirectional_bridge.py：DirectionalBridge；
- scripts/db6f-audit-metric-supplier.py：说明与 Target 的精确参数、
  bridge 常数和误差作用域。

前四组源亦在已恢复的旧 checkout 中逐字可读；这里引用相对于本题的
文件逻辑身份，不暗示恢复了旧进程。

必须分清三个角。$u$ 是本稿共同度量 $ds^2+a^2du^2$ 的物理弧长角，
$\phi$ 是平面 support 曲线的法向角，$\psi$ 是数值图的角变量。
入口固定图为
$$
u_{\rm ref}(\psi)=\psi-\frac{8q_{\rm ref}}3\sin3\psi,\qquad q_{\rm ref}=.1,
\tag{1}
$$
但一般 $\phi\ne\psi$。Flow.geo 的 quintic cutoff 在 cut 处
$1-S,S',S''$ 都为零，因此 $u=\psi$ 且坐标在径向至二阶为恒等；
这直接核自该函数的公式，未只采用注释。周期中间则存在真正的
$s$ 依赖角变换，不能把数值 $\psi$ 模当作全域物理 $u$ 模。

## 2. 位置 Jacobi 量到第二形式量的精确变换

设旋转背景
$$
F_0(s,u)=a(s)e_r(u)+z(s)e_z,\quad
c=a',\quad v=z'=\sqrt{1-c^2}>0,\quad \bar p=v^{-1}.
\tag{2}
$$
选择 $T=e_\theta$、$d=ce_r+ve_z$、$N=-ve_r+ce_z$。
对整数 $|n|\ge2$，考虑一个复 Fourier 模的位置变化
$$
\dot F=e^{inu}
\left(f(s)e_r+\frac{if(s)}n e_\theta+h(s)e_z\right).
\tag{3}
$$
实部对应源代码的
$f\cos(nu)e_r-(f/n)\sin(nu)e_\theta+h\cos(nu)e_z$。

从 $\dot g_{uu}=0$ 得到的切向系数恰是 $if/n$。另两条线性等距条件给
$$
cf_s+vh_s=0,\qquad
af_s=-(n^2-1)cf-n^2vh,
\tag{4}
$$
即
$$
\binom{f_s}{h_s}=
\frac1a
\begin{pmatrix}
-(n^2-1)c&-n^2v\\
(n^2-1)c^2/v&n^2c
\end{pmatrix}\binom f h.
\tag{5}
$$
它逐项等于冻结 Flow.linear_rhs；
不是只在某个端点相同。

记 $N_n=n^2-1$。对第二形式分量的实际变化直接计算得到
$$
\dot C=\frac{N_n}{v}f,\qquad
\dot M=-\frac{iN_n}{nv}\left(f_s-\frac ca f\right).
\tag{6}
$$
证明包括法向变化项。由 (3) 和 (4)，
$\dot d\cdot N=-f_s/v$，而
$$
\dot T\cdot N=
\frac{i}{a}\left(-\frac{N_n}{n}vf+nch\right).
$$
于是 $\dot N=-(\dot d\cdot N)d-(\dot T\cdot N)T$。
代入
$\dot C=\dot F_{uu}\cdot N+F_{0,uu}\cdot\dot N$，
先得到
$N_nvf-n^2ch-acf_s/v$，再用 (4)，恰简化为 (6) 第一式。
同理代入
$\dot M=\dot F_{su}\cdot N+F_{0,su}\cdot\dot N$
并用 (4)，得到第二式。没有遗漏移动法向的贡献。

由于背景 $C=av$、$M=0$，有
$$
\beta=\dot b=\frac{\dot M}{v},\qquad
\pi=\dot p=-\frac{N_n}{av^3}f.
$$
因此前稿的 Sturm 变量
$x=\beta/(\bar p/a)$、$y=\pi/\bar p^3$ 满足
$$
\boxed{\qquad
x=inN_n\left(h+\frac cv f\right),\qquad
y=-\frac{N_n}{a}f.
\qquad}
\tag{7}
$$
反变换为
$$
f=-\frac a{N_n}y,\qquad
h=\frac{x}{inN_n}+\frac{ac}{N_nv}y.
\tag{8}
$$
该矩阵的行列式是 $inN_n^2/a\ne0$，故对于所列模式是精确可逆变换。
它带 $n^2,n^3$ 因子；将位置源、端口行或算子范数换到第二形式空间时
必须保留这些角阶数，不能把两个范数当作同一个范数。

$n=0,\pm1$ 不属于这个反变换。刚体位移/转动及全局周期兼容的低模
必须另设有限维部分。当前非均值物理模式是 $n=3k$，故每个非零表示
模都在 (7) 的有效范围；均值和其它闭合行仍不能删除。

## 3. 真实平面 support 入口

未经数值投影的精确 support 曲线为
$$
H(\phi)=1+\sum_{k\ge1}c_k\cos(3k\phi),\qquad
\rho=H+H''>0,
$$
$$
A_c(\phi)=\phi+
\sum_{k\ge1}\frac{1-9k^2}{3k}c_k\sin(3k\phi),\qquad A_c'=\rho.
\tag{9}
$$
这里有限和就是当前 PlanarSupportCore，合适光滑收敛的无限和是其
相应数学版本。弧长角 $u=A_c(\phi)$，故精确柱边为
$$
b_0=0,\qquad p_0(u)=\rho(A_c^{-1}(u)).
\tag{10}
$$
这一项不要求高 support 系数为零。其法向角、切向标架和周期性由真正
平面曲线给出。固定弧长角下的变化是
$$
\dot p_0=
\dot\rho(\phi)-\frac{\rho_\phi(\phi)}{\rho(\phi)}\dot A_c(\phi),
\qquad \phi=A_c^{-1}(u),
\tag{11}
$$
所以非圆入口的线性化一般不对 $u$ 模对角。

在圆背景，$a=1,c=0,v=1$，位置入口平面性给 $h(0)=0$，因而
$$
x(0)=0,\qquad
z_-(0)=-z_+(0),\quad
z_\pm=(x\pm y)/\sqrt2.
\tag{12}
$$
这就是实际核心的背景端口约束。任意给定 Hadamard incoming 并不是
实际平面 support 初值的替代品。

冻结 WarpedBVP.initial 使用
$q=q_{\rm seed}\exp(p[0])$ 和其余13个高 support 修正（M14），
并以固定图 (1) 评价 core。随后还作有限 warped Fourier 投影。
只有实际 $q=q_{\rm ref}$ 且全部高修正为零，才有 $\phi=\psi$。
本文没有读取当前参数数组来假定这个特例，也没有把有限投影误差清零。

## 4. 任意真实截面的高度 Robin 行

先不强加 bridge 端点的理想匹配。设一个给定截面的背景值为
$a>0$、$c\ne0$、$v=\sqrt{1-c^2}>0$，实际线性高度边界为
$$
h_s-\lambda_n h=\eta_n,
\tag{13}
$$
其中 $\lambda_n$ 为实乘子，$\eta_n$ 是给定普通边界源。
将 (8) 代入 (4)，恰得到
$$
\boxed{\quad
B_nx+iK_ny=inN_n\eta_n,\qquad
B_n=\frac{n^2c}{a}-\lambda_n,\quad
K_n=\frac{nc(c-a\lambda_n)}v.
\quad}
\tag{14}
$$
这同时保留了非齐次边界列及其三次角因子。

当 $\eta_n=0$ 时，$B_n,K_n$ 不会同时为零：
若 $B_n=0$，则
$K_n=-nN_nc^2/v\ne0$。
该齐次行可写成
$(x,y)=(-iK_n,B_n)t$，于是实际右反射为
$$
\boxed{\quad
z_+(R)=\mathcal R_nz_-(R),\qquad
\mathcal R_n=\frac{B_n-iK_n}{-B_n-iK_n},\quad
|\mathcal R_n|=1.
\quad}
\tag{15}
$$
分母确实不为零。$B_n=0$ 也由此式直接覆盖，没有人为除掉一个合法
Robin 方向。零通量只说明这个真实边界是反射型；不说明两端反馈可逆。

## 5. 与代码中径向 linearSlope 的严格关系

在理想匹配截面，若
$$
a=r_{\rm cut},\quad E=1+w^2,\quad
c=\frac{\sigma}{\sqrt E},\quad v=\frac w{\sqrt E},
\quad\lambda_n=\frac{\sigma D_n}{\sqrt E},\qquad w>0,
\tag{16}
$$
则 (13) 齐次条件在位置坐标中是
$$
\frac f h=\frac{\sigma w(aD_n-n^2)}{N_n}.
\tag{17}
$$
这正是冻结 Flow.linear_terminal 返回的向量
$[\sigma w(aD_n-n^2)/N_n,1]^T$。
相应 Sturm 边界向量为
$$
\boxed{\quad
(x,y)=h\left(in(aD_n-1),
-\frac{\sigma w}{a}(aD_n-n^2)\right).
\quad}
\tag{18}
$$
这个核对没有只猜一个 Robin 符号；$\sigma$、$n^2-1$ 和两种坐标的
全部因子都保留。若 $aD_n=n^2$，则 $y=0$，(18) 仍有效。

不过原解析 Target 明确把 bridge 的 $L,p_t,p_s$ 当作冻结二进常数，
不宣称它们是理想匹配根。其桥端半径/导数差由原数值认证另行包围。
因此 (16) 不能无误差地强加给当前二进桥；一般实际值应先用 (14)。
若只求本题数值完成门，原匹配误差应留在同一图的证书里；若求严格精确
闭合，必须真的消去该差或选择并固定真正匹配的几何，不能静默设零。

更重要的是当前 TailMixin 已不是这个径向线性乘子模型。其真实回调为
$$
H_{\rm tail}=\sigma h_{\rm cut},\qquad
h_s-\frac{\mathcal T(H_{\rm tail})}{\sqrt E}=0,
\tag{19}
$$
在实际程序中 $h_{\rm cut}=q\,y_{\rm height}$。线性化涉及
$\sigma\,D\mathcal T(H_{\rm tail})/\sqrt E$。
冻结 bc_jac 从完整 heightJetJacobian 取 slope 的前 M 行；
在非零非径向高度处它一般是耦合各角模的矩阵，并非 $\operatorname{diag}D_n$。
只有在真正径向基线、且已有对应真尾 DN 时，才可使用 (16) 的对角公式。
普通源和 mean/second 两 jet 的其余行也由原 seam_audit 保留，不能由
一个非均值 Robin 行代替。

AffineTailForInnerBVP 明确只供内步线性化；solve_with_actual_tail
最终重新调用真实 $\mathcal T$ 核原边界残差。本报告没有把临时 affine
响应当作真尾，也未运行新的尾请求。

## 6. 第一周期与真正 cut 之间还有 bridge

新全周期 provider 的右端是 $s=T_u+T_d$。真实主 prefix 的右端另包含
bridge；原程序按 prefix_end 加 bridge.L 构造并存储 end，而严格解析
Target 保留元数据的二进 end，记为
$$
s_{\rm cut}:=\mathrm{Target.end}.
\tag{20}
$$
它与精确 $T_u+T_d$ 加冻结 bridge.L 的舍入差也由原解析目标的边界
sliver 处理；本文不重新定义 end 或把该差静默设零。
DirectionalBridge.profile 明确在周期后另接
$a_s=\sigma\sin\varphi(s)$ 的桥；这是实际几何的一部分。
不能把周期末端的 $a=1,c=0$ 当成 cut 的 $a=r_{\rm cut}$。

在桥确有 $a>0,|c|<1$ 的背景范围内，第 2 节变换和精确 Sturm 系统
继续成立。设其实际传递为 $T^{\rm br}_n$。则 cut 行拉回到周期端口是
$$
\ell^{\rm cyc}_n=\ell^{\rm cut}_nT^{\rm br}_n,\qquad
\ell^{\rm cut}_n=(B_n,\ iK_n).
\tag{21}
$$
有普通源时还必须加上
$$
\ell^{\rm cut}_n
\int_{\rm bridge}T^Z_n(r_{\rm cut},r)\,g_n(r)\,dr.
\tag{22}
$$
(21)–(22) 是精确接线公式；没有因为桥是有限长度就删除普通源列。
新的单中央非正势区证明只覆盖第一周期，不能凭它自动延伸到 bridge。
桥的实际势、源范数及 cut 匹配必须按其自己的真实函数验证。

源代码的桥使用给定 cut 构造，但其样本角度检查、浮点求根和64点
求积本身不是严格无限维传输表。本报告没有将它们提升为这样的表。

## 7. 辅助 Hadamard 逆与真正反馈分母

记新的两端口散射关系（包括其真正普通源列）为
$$
\mathrm{out}=\mathcal S\,\mathrm{in}+\mathcal L f.
\tag{23}
$$
在径向背景的两个实际反射端口上，物理边界是
$$
\mathrm{out}=\mathcal R_{\rm bd}\,\mathrm{in}+g_{\rm bd},
\qquad
\mathcal R_{\rm bd}=\operatorname{diag}(-1,\mathcal R_{\rm right}),
\tag{24}
$$
右端须先用 (21) 拉回周期，不能直接贴 cut 公式。
所以真正需要求逆的是
$$
(\mathcal S-\mathcal R_{\rm bd})\mathrm{in}
=g_{\rm bd}-\mathcal Lf.
\tag{25}
$$
两者均酉并不保证它们的差可逆。例如在某模恰相同就有核。
因此 $|D_j|\ge1$（传递矩阵的一个块）不是 (25) 的非共振证书。

等价地，若把周期和桥全接入实际 $T^Z_n$，
核心 $x(0)=0$ 使 cut 数据为
$(t_{12,n},t_{22,n})\,y(0)$。真正齐次反馈分母是
$$
\Delta_n=B_n t_{12,n}+iK_n t_{22,n}.
\tag{26}
$$
它与新的辅助传播常数是不同对象。没有在本报告中宣称某个具体
$\Delta_n$ 为零或非零；当前设计的实际幅度、有限低模和全部高模
仍须分别核验。原有限数值 DN 也不是全部 $n$ 的严格乘子数据。

## 8. 新普通源 provider 对旧接口能支付什么

新的周期结果若完成全部内部/普通源证明，就确实支付：

1. 同一固定 flat17 周期上的非截模线性方程、均值及真实普通源；
2. 在指定辅助端口下的有限角阶数损失和实际 source-to-boundary 列；
3. 由 (7)、(14)、(21) 明确转换物理位置、边界行和桥源的办法。

它尚不能直接充当旧 Schur 笔记中的原选定 $K_0$。旧引理还要求
同一个真实边值问题的右逆、规定的 range、具体有限矩阵可逆性与无限尾
范数门。把 Hadamard 端口换成 (24) 必须先解 (25)，并保留 (22) 与
全部低模/均值/标量列。

也不能直接套旧 weighted-inverse 稿的严格反馈结论。那里要求相应
cross-block 有全空间有界逆；这里只知道每模 $D_j$ 不为零，并未给
$\sup_j|D_j|<\infty$。端口 transmission $1/D_j$ 的逐模非零不等于
它作为无限维乘子有有界逆。真正所需的主返回相位、低头部和高频余项
仍应在实际端口归一化下证明，而不能借用另一简单根模型。

最后，当前 M14 解是有限 Fourier/角求积的非径向候选，其完整线性化
不再逐物理模解耦；新径向普通源表没有提供这一当前算子的全加权表。
需要真实非线性/当前线性化 provider、原真尾 DN 与 source 行、实际
反馈逆和全局几何证书，才能从这些已支付接口走到闭曲面。这个清单
没有改动主 $g$、没有新增题设正则性要求，也没有放宽原 G5 完成门。

