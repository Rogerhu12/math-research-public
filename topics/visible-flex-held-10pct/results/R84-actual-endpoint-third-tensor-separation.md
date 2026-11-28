# R84 — 同一实际闭族的指定端点三阶张量分离

会话：Astra-held10-7c4e33ee-20261128。状态：**已证明（精确对称性推导与实际有理运算）**。

对 [R82](R82-actual-marked-closed-family-all-time-geometry.md) 的同一完整有限 C² 闭族及 [R83](R83-actual-closed-third-activity-and-euclidean-separation.md) 的实际第三活动矩，令
$$
T_3(\alpha)=\int_{\Omega_\alpha}X^{\otimes3}\,dV,\qquad
I_3(\alpha)=\|T_3(\alpha)\|_F^2.
$$
这里原点就是每个体积的质心。现得到指定端点的严格差
$$
\boxed{I_3(0)-I_3(9/20)>7\times10^{-19}.}
$$
因此这两个实际闭面在包含反射的完整 $E(3)$ 下不全等，其最小对齐 Hausdorff 距离严格为正。上式是**张量范数平方差**，没有把它换成数值 Hausdorff 下界。

场仍是同一 $\lambda=.002,q=.06,M24/N512$、mean1168、原 raw-H factor1、width=.12、真实字面短柱和 canonical R67 帽。未改变场、目标度量或原数值门；准确 $\lambda=1$、10% 握持、整尾连续度量及固定问题精化仍须继续。

## 1. 原点、三重对称和上下反射

R82 的真实完整映射在每个相位保持绕原点的三重旋转以及
$$
S_z(x,y,z)=(x,y,-z).
$$
前者来自完整 $3j+1$ 平面模、$3j$ 高度模、真实 R53 核及三重帽；实际相位只是活动部分的水平旋转与材料角重参数化，和三重旋转交换。后者由上、下前缀、完整尾、深领、柱和帽的显式全高度反射定义。正、负半柱长相同，双帽也按这一反射放置。

R82 已证明闭面嵌入。上述正交变换保持其唯一有界内部 $\Omega_\alpha$。体积质心因此同时被非平凡三重旋转及 $S_z$ 固定，故准确为原点。这里不以数值质心接近零为依据。

## 2. $\alpha=0$ 的完整实际图确实保留 $y$ 反射

记水平复坐标 $w=x+iy$，$S_y(w,z)=(\bar w,z)$。以下逐项核同的是 R73–R83 所定义的完整图，并非把数值求值器的微小误差当作准确恒等。

### 2.1 真实 R53 核

原支撑函数
$$
h(\phi)=1+\sum_j a_j\cos(3j\phi)
$$
的所有 $a_j$ 是同源冻结的实数。其正曲率半径 $\rho=h+h''$ 为偶函数，且以 $P=2\pi/3$ 为周期。单位材料弧长映射
$u(\phi)=\int_0^\phi\rho(v)\,dv$ 是奇函数，并满足
$u(\phi+P)=u(\phi)+P$。唯一反函数 $\phi_0$ 因而同样是奇函数并具有相同周期协变；$\kappa_0(u)=1/\rho(\phi_0(u))$ 为偶函数。

R53 的材料窗 $W$ 在一个扇区以 $P/2$ 为中心，依赖 $|u-P/2|$，再作 $P$-周期延拓，所以 $W(-u)=W(u)$。真实圆化曲率为
$$
\kappa_\lambda
 =\kappa_0+\lambda\{(1-W)(k-\kappa_0)+\beta W\}.
$$
真实积分定义的常数 $\beta$ 使每扇区总转角准确为 $P$，故 $\kappa_\lambda$ 仍为偶函数、$P$-周期函数，且
$\phi_\lambda(u)=\int_0^u\kappa_\lambda(v)\,dv$ 为奇函数、
$\phi_\lambda(u+P)=\phi_\lambda(u)+P$。

在共同旋转中心规范下，真实核心满足
$$
\Gamma'(u)=i e^{i\phi_\lambda(u)},\qquad
\Gamma(u+P)=e^{iP}\Gamma(u).
$$
函数 $H(u)=\overline{\Gamma(-u)}$ 与 $\Gamma$ 具有同一导数；其差是常数 $D$。二者又有相同三重协变，故
$D=e^{iP}D$，从而 $D=0$。这给出
$$
\Gamma(-u)=\overline{\Gamma(u)}.
$$
证明使用真实积分、反函数和唯一旋转规范。没有使用浮点 origin.real 截取或 reflection_roundoff 的大小来断言反射。

实际连续图使用 warm_phase_validated_core.py 的零 phase-control 特化及原 r53_validated_material_core.py 的真实积分定义；其 $P=2\pi/3$ 是真常数。没有把求值器缓存的浮点周期另当成数学定义。

### 2.2 有限前缀、完整核心提升和中心修补

M3CartesianPrefix 和 ActualR53CartesianPrefix 的字面有限平面部分为
$$
\sum_m c_m(s)e^{im\psi},\qquad c_m(s)\in\mathbb R,
$$
高度部分为完整实余弦和及实径向零模。共享 Hermite 数据与所有径向权均为实数。因此将 $\psi$ 变为 $-\psi$ 正好把平面值复共轭、保持高度不变。有限截断并不破坏这项恒等，它也不要求被截尾系数为零。

完整真实核提升使用
$$
\theta_0(\psi)=\psi-E_0\sin(3\psi)/3,
$$
这是奇函数。由上一节、圆映射的共轭恒等以及源完整初始系数的同一实 Fourier 结构，真实核减去圆和有限初始补偿的整个提升也保留 $S_y$。该提升乘以同一实径向共享 Hermite 函数，未只保留某几个入口模。

中心修补的目标零阶、径向一阶、径向二阶分别是
$$
\Gamma(\theta_0),\quad e_z,\quad
b(\psi)\Gamma'(\theta_0),\qquad
b(\psi)=-E''_0\sin(3\psi)/3.
$$
$b$ 是奇函数，而
$\Gamma'(-u)=-\overline{\Gamma'(u)}$，所以第三个目标也准确保留 $S_y$。目标减去原完整端点 jet 再乘实 Hermite 权，保持该反射。这里包括真实二阶中心修补及全部 angular derivatives，未省略 $\Gamma''$、$\Gamma'''$ 项。

声明的新有限均值一直是实径向函数。它与源 mean primitive 不是同一函数的事实已经由 R73–R74 单独处理；这一差异不会破坏当前图的反射，也不能借此继承旧图数值。

### 2.3 完整尾、实际 .12 cut、角图、柱和固定帽

ActualFiniteTailV2.fourier 明确使用全部实平面系数乘 $e^{im\psi}$ 和全部实高度系数乘 $\cos(m\psi)$。1152 段的共享径向插值、完整共同均值、深领径向 Hermite 及真背景 primitive 均不引入角向奇高度项或非实平面系数。因此完整尾和深处也保留 $S_y$。

ActualCutTarget 使用相同完整尾两 jet、实 $R,w,z_{\rm cut},\mu_{\rm cut}$ 及唯一实表达式
$$
w_R=-7w/R,\quad a'=-1/\sqrt{1+w^2},\quad
a''=-ww_R/(1+w^2)^2.
$$
它给出的完整 Cartesian 目标保留反射。CartesianCutLift 仅以实径向权乘完整目标与前缀端点之差，故当前实际 width=.12 修补仍保留该恒等。这里没有把不同 cut 宽度的失败场换回当前场。

共同 PhaseAngleChart 为
$\theta=\psi-e(s)\sin(3\psi)/3$。其 $\psi$-导数已有严格正下界；该函数为奇函数，故唯一逆图也为奇函数。材料角重参数化因此不改变上述镜面对称性。

中央柱是同一核心乘对称高度区间；下半是同一上半全高度反射，均与 $S_y$ 交换。固定 canonical 帽的准确函数为
$$
f(w)=\varepsilon(1-|w/r_c|^2)_+^3
 \Re\frac{(w/r_c)^3}{1-(w/r_c)^3/2}.
$$
径向因子为实，分式的系数为实，所以 $f(\bar w)=f(w)$。完整双帽也保留 $S_y$。

以上覆盖当前完整闭图的全部组件及接缝。因此 $\Omega_0$ 准确被 $S_y$ 保持，
$$
C(0):=\int_{\Omega_0}w^3\,dV\in\mathbb R.
$$

## 3. 此处三阶张量的所有低旋转权都为零

不能仅用“最高频率不被抵消”来宣称某个指定端点分离。这里利用本场更强的准确对称性消去所有低权。

含奇数个 $z$ 指标的三阶矩因 $S_z$ 为零。含恰好两个 $z$ 指标的分量组成水平向量
$$
\left(\int xz^2\,dV,\ \int yz^2\,dV\right),
$$
其被三重旋转固定，故也为零。只剩水平部分，写
$$
a=T_{xxx},\quad b=T_{xxy},\quad c=T_{xyy},\quad d=T_{yyy}.
$$
向量
$$
\left(\int x(x^2+y^2)\,dV,\ \int y(x^2+y^2)\,dV\right)
=(a+c,b+d)
$$
同样被三重旋转固定，所以 $c=-a,d=-b$。因此
$$
C(\alpha)=\int_{\Omega_\alpha}(x+iy)^3\,dV
=(a-3c)+i(3b-d)=4(a+ib),
$$
以及完整 Frobenius 范数恒等式
$$
I_3(\alpha)
=a^2+3b^2+3c^2+d^2
=4(a^2+b^2)=\frac14|C(\alpha)|^2.
$$
这已包括全部 27 个有序 Cartesian 张量分量及其重复计数，不留未控制低权项。

## 4. 实际活动矩、正帽矩与指定端点

同 R67/R83 的完整通量分解给
$$
C(\alpha)=A e^{3i\alpha}+B,\qquad B=\frac{\pi\varepsilon r_c^5}{140}>0.
$$
这里 $A=A_3(\ell)$ 包含同 .12 cut 前缀、完整尾/深盘和**只加一次**的真实字面柱长项；$B$ 包含固定双帽，原始平盘的三阶矩为零。上一节 $C(0)$ 实、$B$ 实，所以 $A$ 实。无需另算一个虚部积分。

R83 的准确实部区间已真积分并合成，给
$$
A\ge0.1392755359019308>\frac{139}{1000}.
$$
此处严格比较实际使用 R83 公布的准确大分数，而非展示十进制。实际帽字面常数为
$$
r_c=\frac{900719925474099}{36028797018963968},\qquad
\varepsilon=\frac{4722366482869643}{75557863725914323419136}.
$$
它们与 R82 actual query、完整 bundle、同 raw-H packet 和 R83 正帽矩逐项核同。

于是
$$
I_3(0)-I_3(\alpha)=\frac{AB}{2}(1-\cos3\alpha).
$$
在实际声明的端点 $\alpha=9/20$，交错余弦级数的余项符号给
$$
1-\cos(27/20)\ge\frac{(27/20)^2}{2}
-\frac{(27/20)^4}{24}
=\frac{989253}{1280000}>0.
$$
再用 $\pi>3$，全部严格有理运算得到
$$
I_3(0)-I_3(9/20)>
\frac{1154920179582272261904290009503372082834580208781621178366986542218511242865654165848584431609416357}
{1643979807941683259522636417752535919162977784235823909495103680072546317580225910424589298869338092122354483200000000}
>\frac7{10^{19}}.
$$
第一项约为 $7.025148204394738\times10^{-19}$，该十进制只供展示。

## 5. 含反射非全等及范围

中心体积矩在平移后重新取质心、在任意 $O(3)$ 变换下按张量作用变换；其 Frobenius 范数在完整 $E(3)$ 下不变。上面的指定端点差因此排除包括反射的所有全等。

同 R67/R83，对两紧致曲面，使 Hausdorff 距离趋零的等距列具有有界平移；再取 $O(3)$ 的紧子列便得到极限全等。因此这对不全等端点的最小对齐 Hausdorff 距离严格正。这里没有由微小张量差推算距离常数、体积稳定性常数或任何新的数值 $\delta_E$ 下界。

当前结果只加强 R83 为指定端点。它不补充未付的整尾度量，不把原 raw-H 代替最终 coupled physical-H，不证明 $\lambda=1$ 准确握持，也不证明固定问题的非零极限。

## 6. 实际执行与可复查来源

独立小源 [endpoint_tensor_exact_certificate.mjs](../scripts/resume_20261128/tail/endpoint_tensor_exact_certificate.mjs) 的 SHA-256 为
f23439e4bd82bc070565e129fe2494ab93ee49d2542521e9eaee6595c1186024。
它已在 functions V8 中用原生 BigInt 实际求值，准确核同 R83 小记录中的 source run、accepted packet、完整 bundle、完整 mean、actual query、几何报告、合成报告、字面柱长、cut 宽度和帽矩，并验证所有分数不等式。没有调用不可用的 executor，也没有重新运行积分。

实际输入是 commit 4cbd74a0b22de4345fee878d9e06de97dd14c102 的 R83 JSON，小文本 SHA-256 为
d435200a5a1a8361cda6c05c7d4ba0a049391fd58cb809a9c96c8d54e7e9661f。
完整执行小记录及 9 个实际源码的 SHA-256 见
[2026-11-28-actual-endpoint-third-tensor-separation.json](../notes/2026-11-28-actual-endpoint-third-tensor-separation.json)。
相关源码均从该真实已发布提交读取，未改数学定义。另有独立代理对第 3–4 节的完整张量计数、$1/2$ 系数和三角有理下界作只读复核；它没有把该代数复核冒充全 source 或数值重跑。

当时 executor 已 unavailable；尾度量 successor TTY79580 的最后实际确认是 61 个完整 stages，之后状态未知。本证明不声称该进程完成。
