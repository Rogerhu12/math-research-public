# R113：真实度量缺陷、协变导数及保留相关项的曲率修正

2026-11-13，visible-exact-astra-f6a2。

**已证明：** 下述全部误差传播、协变导数和曲率分子恒等式。
新度量程序已经在九个径向点对全角、整个参数盒实际运行；中心的两个点也实际运行。
原完整小 JSON 在断线前尚未推送，须按本篇命令重建。
九点不等于整个径向区域；本篇不宣称初始缺陷已满足 Newton 小量门，
也不将大导数上界解释为不存在解。

## 1. 同一个真实几何及目标度量

使用 R33 的准确单位切向 primitive 以及
type_fixed_step02_d5_exact_affine_step5_object.json 所定义的同一仿射族。
参数为
$$
 p\in[\delta_5-10^{-9},\delta_5+10^{-9}],\qquad
 \delta_5=-7789843107295549/4611686018427387904.
$$
在随物理角旋转的正交标架中写
$$
 F(r,\theta)=R_\theta\{a(r)(e_x+P(r,\theta))+Z(r)e_z\}.
\tag{113.1}
$$
这里 $P$ 为包含全部无限角频率的真 primitive，并非保留的有限 Fourier 多项式。
真实单位切向构造给
$$ |F_\theta|^2=a^2,\qquad
 \langle F_r\cdot F_\theta\rangle_\theta=0.
$$
后一式来自当前反射奇偶性，在每个参数上都准确成立。
定义
$$
 E=\langle|F_r|^2\rangle_\theta,\quad
 g_0=E(r)\,dr^2+a(r)^2\,d\theta^2,\quad h=g_F-g_0 .
\tag{113.2}
$$
目标随参数按本定义确定；在一次 Newton 更新中须固定所选目标，
或把它的真实参数导数及 Taylor 余项同时放入方程。不能在更新后任意消掉非零模。

本文所有径向证书都注明一个准确公共 spline germ；跨 knot 时分别处理。
没有将有限 C4 径向数据解释为无限光滑。

## 2. 完整角余项如何进入度量缺陷

令 $P_N$ 为实际 512 节点构造的有限 Fourier primitive。
同一已证明的 primitive_fourier_budget 在内条带 $\sigma=1/32$
给完整 $A_\sigma$ 误差 $\epsilon_P$；它包括别名、Nyquist 处理和全部舍弃频率，
而不是节点间插值误差。径向 Cauchy 半径记为实现中真实的 $\rho_r$。
因此
$$
 \|\partial_r^j\partial_\theta^q(P-P_N)\|_{A_0}
 \le \frac{j!}{\rho_r^j}\,
       q!\left(\frac4{\sigma}\right)^q\epsilon_P .
\tag{113.3}
$$
系数4来自归一角 $x=4\theta$。本式使用的都是已证真实复域；
不能把只在实角知道的余项直接授给复角导数。

在旋转标架中，准确径向 jet 和角 jet 为
$$
 F_j=\sum_{v=0}^j {j\choose v}a^{(j-v)}P_v
       +a^{(j)}e_x+Z^{(j)}e_z,\qquad
 Y_j=(J+\partial_\theta)F_j,
\tag{113.4}
$$
其中 $J(x,y,z)=(-y,x,0)$，$Y_j$ 表示 $\partial_r^jF_\theta$。
因此从 (113.3) 以 Leibniz 法则得到每个分量的完整误差
$\epsilon^F_{j,q}$ 及
$\epsilon^Y_{j,q}\le\epsilon^F_{j,q}+\epsilon^F_{j,q+1}$。

对于两个三分量 Fourier 场 $A=A_N+e_A$、$B=B_N+e_B$，
若每分量的第 $q$ 阶 Wiener 范数由 $M_{A,q}$、$M_{B,q}$ 控制，
每分量余项由 $\epsilon_{A,q}$、$\epsilon_{B,q}$ 控制，则
$$
 \|\partial_\theta^q(A\cdot B-A_N\cdot B_N)\|_{A_0}
 \le3\sum_{v=0}^q{q\choose v}
 \bigl(M_{A,v}\epsilon_{B,q-v}
       +M_{B,q-v}\epsilon_{A,v}
       +\epsilon_{A,v}\epsilon_{B,q-v}\bigr).
\tag{113.5}
$$
证明是逐分量展开乘积，再用 Wiener 代数不等式。
所有有限乘积先零填充到1024再作有向 FFT，保留完整卷积支撑，
不会把有限截断的混叠藏进零模。常数项单列有助于保持小缺陷的消去。

由
$$
 \partial_r^i|F_r|^2
 =\sum_{v=0}^i{i\choose v}F_{v+1}\cdot F_{i-v+1},\qquad
 \partial_r^i(F_r\cdot F_\theta)
 =\sum_{v=0}^i{i\choose v}F_{v+1}\cdot Y_{i-v}
\tag{113.6}
$$
对 $i+q\le2$ 取得实际非均值 $rr$ 项、mixed 项及 $E,E',E''$ 的完整界。
删除零 Fourier 模在 $A_0$ 中是压缩，因此非均值余项仍由同一个
完整 Wiener 余项控制；无需将点态 sup 误差误当成这一投影的范数。
mixed 零模在真实反射对称性下准确为零，程序同时检查有限运算的包络含零。

所有复球先保留虚部；只有真实参数、真实径向盒和整个实角时，
才利用已证明的实值性把最终真实场放入实区间。
Arb 对跨零区间的通用幂运算在本次 .9 环境曾产生 NaN；
修订源对有符号量的平方显式写成乘法。正分母的幂不受此问题影响。

## 3. 目标度量的完整 C0、C1、C2 界

取 $g_0$ 的正交标架
$$
 e_1=E^{-1/2}\partial_r,\qquad e_2=a^{-1}\partial_\theta .
$$
令 $H$ 为 $h$ 在此标架中的对称矩阵。由于 $h_{\theta\theta}=0$，
$$
 H_{11}=(|F_r|^2-E)/E,\quad
 H_{12}=(F_r\cdot F_\theta)/(a\sqrt E),\quad H_{22}=0.
\tag{113.7}
$$
程序对这些准确商使用 $E,E',E''$、$a,a',a''$ 及 (113.6)，取得
$$
 N_{iq}\ge\|\partial_r^i\partial_\theta^qH\|_{\mathrm{HS}},
 \qquad i+q\le2 .
$$
各 $N_{iq}$ 均为整个角函数的有向上界，而非有限节点最大值。写
$$
 k=\frac{a'}{a\sqrt E},\qquad
 k_s=e_1k
 =\frac{a''}{aE}-\frac{(a')^2}{a^2E}
   -\frac{a'E'}{2aE^2}.
\tag{113.8}
$$
有
$$
 \nabla_{e_1}e_1=\nabla_{e_1}e_2=0,\quad
 \nabla_{e_2}e_1=ke_2,\quad\nabla_{e_2}e_2=-ke_1.
$$
对矩阵场记 $\mathcal JH=J_2H-HJ_2$，$J_2$ 为二维旋转矩阵；
其 Hilbert–Schmidt 算子范数不超过2。于是
$$
 \nabla_1H=e_1H,\qquad \nabla_2H=e_2H+k\mathcal JH .
\tag{113.9}
$$
故一阶界为
$$
 A_1=N_{10}/\sqrt E,\qquad A_2=N_{01}/a+2|k|N_{00},
 \qquad |\nabla h|\le\sqrt{A_1^2+A_2^2}.
\tag{113.10}
$$
二阶协变导数还要扣去其导数指标的连接项。逐项展开 (113.9) 得
$$
 \begin{aligned}
 B_{11}&=N_{20}/E+|E'|N_{10}/(2E^2),\\
 B_{12}&=N_{11}/(a\sqrt E)+|k|N_{01}/a
           +2|k_s|N_{00}+2|k|N_{10}/\sqrt E,\\
 B_{21}&=N_{11}/(a\sqrt E)+|k|N_{01}/a
           +2|k|N_{10}/\sqrt E+2k^2N_{00},\\
 B_{22}&=N_{02}/a^2+4|k|N_{01}/a
           +4k^2N_{00}+|k|N_{10}/\sqrt E .
 \end{aligned}
\tag{113.11}
$$
例如 $\nabla_1\nabla_2h$ 包含 $e_1k$，而
$\nabla_2\nabla_1h$ 中必须减去 $k\nabla_2h$；
二者不能被当成同一个普通混合偏导。
由正交标架中的逐分量平方和，
$$
 \boxed{\quad |h|\le N_{00},\quad
 |\nabla h|\le\sqrt{A_1^2+A_2^2},\quad
 |\nabla^2h|\le
 \sqrt{B_{11}^2+B_{12}^2+B_{21}^2+B_{22}^2}.\quad}
\tag{113.12}
$$
所有分母均在真实盒上验证为正，使用其区间 reciprocal；没有免费坐标常数。

## 4. 已观察到的真实有限点结果

原源 SHA256
8f504eee36989bbbc0e6a3711108ae146952f2f49ccbd2aafc2b089ca8e8fb6e
以512节点/192 bit 实际执行九点命令，在14.24秒后完成。
以下数值均向上放宽已观察的输出，适用于整个参数盒和全部角，
但只适用于明确列出的径向点。

| $r$ | $|h|$ 上界 | $|\nabla h|$ 上界 | $|\nabla^2h|$ 上界 |
|---:|---:|---:|---:|
| 0 | $3.780641\cdot10^{-5}$ | $.012400$ | $1.536130$ |
| $1/8$ | $8.756636\cdot10^{-5}$ | $.006085558$ | $.968477$ |
| $1/4$ | $7.855233\cdot10^{-5}$ | $.004900094$ | $1.904382$ |
| $1/2$ | $7.827230\cdot10^{-7}$ | $.000107229$ | $.0703700$ |
| 1 | $4.511339\cdot10^{-12}$ | $3.804481\cdot10^{-10}$ | $1.089150\cdot10^{-6}$ |
| $3/2$ | $2.727028\cdot10^{-16}$ | $6.082694\cdot10^{-14}$ | $1.853355\cdot10^{-10}$ |
| 2 | $6.471174\cdot10^{-21}$ | $1.975837\cdot10^{-17}$ | $5.768478\cdot10^{-13}$ |
| $5/2$ | $1.085510\cdot10^{-24}$ | $4.395598\cdot10^{-20}$ | $3.569403\cdot10^{-15}$ |
| 3 | $5.768695\cdot10^{-26}$ | $1.222073\cdot10^{-19}$ | $1.421649\cdot10^{-13}$ |

显式跨零乘法修订后，参数单点 $p=\delta_5$ 的 $r=0,1/4$ 两点
也真实完成（2.14秒）：C012分别小于
$(3.780641\cdot10^{-5},.012388907,1.523431)$ 及
$(7.793006\cdot10^{-5},.004433541,1.649926)$。

在中心腰部的有限系数诊断中，非均值 $E_{rr}$ 的 Wiener 中点总量约为
$1.2920381$，相应系数半径总量约为 $1.47\cdot10^{-8}$；
mixed 的 $r$ 导数中点量约为 $.0112999$，半径总量约为
$4.78\cdot10^{-9}$。这说明当前较大的高导数包络不能仅靠减少舍入半径
解释掉。它仍是所选范数及求和方式的上界，不是实际最小值，也不证明 Newton 失败。

新完整报告在执行器再次失联前未推送；本表及收据不代替原完整 JSON。
修订源已保存为 scripts/fourfold_phase_metric_defect.py。
恢复时实际运行：

~~~sh
python scripts/fourfold_phase_metric_defect.py --points 0 1/8 1/4 1/2 1 3/2 2 5/2 3 --out notes/2026-11-13-metric-defect-nine-radii-recovered.json
python scripts/fourfold_phase_metric_defect.py --half-width 0 --points 0 1/4 --out notes/2026-11-13-metric-defect-center-two-radii-recovered.json
~~~

## 5. 不拆散相关项的真实曲率分子

R37的通用 C2 度量差界在当前数据上可能过粗。
下面给直接使用几何0、1、2阶 jet 的准确替代式；它不需要先控制 $F_{rrr}$。

在同一个材料坐标上置
$$
 C=F_\theta\times F_r,\quad
 G=C\cdot C,\quad T=F\cdot F,\quad S=C\cdot F,
$$
$$
 L=C\cdot F_{rr},\quad M=C\cdot F_{r\theta},\quad
 N=C\cdot F_{\theta\theta}.
\tag{113.13}
$$
以下要求实际区域上 $G>0$、$T>0$、$S>0$、$N<0$；
这些是实际正性门，不能用形式记号代替验证。
取外法向 $n=C/\sqrt G$，则第二基本形式系数为
$L/\sqrt G,M/\sqrt G,N/\sqrt G$。因此
$$
 K_{g_F}=\frac{LN-M^2}{G^2},\qquad
 K_0=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}.
\tag{113.14}
$$
定义保留相关项的单一分子
$$
 \Delta=LN-M^2-K_0G^2.
\tag{113.15}
$$
于是
$$
 \boxed{\quad K_{g_F}-K_0=\Delta/G^2.\quad}
\tag{113.16}
$$
构造区间时应先形成真实乘积及差 (113.15)，再包络其完整 Fourier 余项；
不能先用 $|L||N|+|M|^2+|K_0|G^2$ 抹去全部消去。

把 R37 的系数记作 $\mathsf A_{rr}$，避免与这里的半径 $a$ 混淆。
径向球面投影的量准确为
$$
 \zeta^2=\frac{S^2}{TG},\qquad
 j_u=\frac{S}{T^{3/2}},\qquad
 \mathsf A_{rr}=-\frac{NT}{S^2}.
\tag{113.17}
$$
代入 R37 的
$\omega=(K_{g_F}-K_0)/(\zeta^4\mathsf A_{rr})$，所有 $G^2$ 准确消去，得到
$$
 \boxed{\quad
 \omega=-\frac{T\Delta}{NS^2}.
 \quad}
\tag{113.18}
$$
证明仅为 (113.14)、(113.17) 的代入：
$\zeta^4\mathsf A_{rr}=-NS^2/(TG^2)$，再用 (113.16)。
本式与实际修正算子完全相同，没有换目标、坐标或符号。

因此直接支付 $\Delta,N,S,T$ 可以避开 R37(3.1) 中由一般度量
二阶差产生的粗大常数。它也不把真实导数改称固定型别导数；
两者差仍是 R37 的准确残差修正。

## 6. 连密度一起保留的弱修正界

设 $X=\partial_\theta(F/\sqrt T)$ 是球面上的实际角向量场。
其长度准确为
$$
 |X|_\sigma^2
 =\frac{a^2}{T}-\frac{(F\cdot F_\theta)^2}{T^2}.
\tag{113.19}
$$
在正帽 $Y=u_z=F_z/\sqrt T>0$ 上，R37 的 ground-state 系数为
$$
 \ell=\partial_\theta\log Y
 =\frac{(F_\theta)_z}{F_z}
  -\frac{F\cdot F_\theta}{T}.
\tag{113.20}
$$
核心可取 $\ell=0$，过渡用 R37 中实际固定 cutoff；过渡项也须完整保留。
若 $\chi$ 是真实修正 cutoff，则由 R37 的弱恒等式及点态 Cauchy–Schwarz，
$$
 |\langle\mathcal Ew,\varphi\rangle|
 \le\Lambda_{\mathrm{corr}}\,
       \|w\|_{H^1_\sigma}\|\varphi\|_{H^1_\sigma},
$$
其中可以直接取
$$
 \boxed{\quad
 \Lambda_{\mathrm{corr}}=
 \sup\frac{|\chi|T^{5/2}|\Delta|}{|N|S^3}
       \bigl(|X|_\sigma^2+|\ell|^2\bigr).
 \quad}
\tag{113.21}
$$
证明中 $dr\,d\theta=j_u^{-1}d\sigma$，
$|Xw-\ell w|^2\le(|X|^2+|\ell|^2)(|\nabla w|^2+|w|^2)$，
且 $\omega/j_u=-T^{5/2}\Delta/(NS^3)$。
这允许在同一个实际小盒内同时包住所有因子，再取全域最大；
没有必要先把各因子独立取全域最大再相乘。

R37 的兼容投影与真实应变公式于是给
$$
 \|Dg_F[V]-f\|_{\mathcal H^1}
 \le\frac{14M_\rho}{\sqrt{20}}
   \left(\Lambda_{\mathrm{corr}}\|w\|_{H^1_\sigma}
                   +\|r_{\rm sc}\|_{H^{-1}_\sigma}\right).
\tag{113.22}
$$
这是同一完整算子的更直接几何计费方法。
强角/径向输出仍须为 (113.18)–(113.20) 支付对应真实导数；
低层弱界不能代替这些强档，也不能代替邻域和迭代收敛。

## 7. 当前推进点

下一实际数值任务是用同一个无限 primitive 和完整角余项认证
(113.15)、(113.18)、(113.21)，随后覆盖需要的连续径向域。
有限点表没有支付这个任务。全 strong inverse、完整源、
修正后的背景邻域、有限正则 smoothing 及 C2 收敛仍继续按 open.md 推进。
