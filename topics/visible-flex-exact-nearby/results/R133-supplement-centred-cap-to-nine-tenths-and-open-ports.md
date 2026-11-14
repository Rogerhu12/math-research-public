# R133：真实非零中心帽推进至 $r=9/10$ 及开放两迹图

**已证明。** 本篇在完整区间 $I=[L,R]=[9/10,25/8]$ 上证明真实无限 Fourier
Gauss–Codazzi 驱动帽存在，并给出开放内端曲率迹图。所有结论覆盖原准确仿射参数
$|\eta|\le10^{-9}$、完整角圆和全部 primitive 尾。它使用与
[完整非零中心帽及接口点源](R133-supplement-complete-nonzero-centred-cap-with-interface-jumps.md)
相同的真实度量、原 M64 有限中心和四独立端口，但内侧非零 $C$ 数据现在固定于
$r=9/10$，不是 $r=1$。所以这里首先得到新的驱动解；并未未经匹配就断言它在
$[1,25/8]$ 上恰等于此前内端数据固定于 $1$ 的解。

其完整 M128 内侧输入也被实际包含。内侧另一迹、mean、真实 nonlinear regular
条件和框架 holonomy 仍保留为联立方程；本篇不把曲率迹换名为高度或 grounded flux。

## 1. 方程、准确参考与完整函数空间

沿用真实正帽的 $\beta=a'/a$、$\gamma=\sqrt E/a$、旋转第二形式
$C_r<0$ 和 $\ell=A_r/C_r>0$。令 $U=(B,c)$、$C=C_r+c$，则

$$
Q(U)=\frac{B^2+\ell c^2}{C_r+c},\qquad
b_m=i\operatorname{sgn}(m)\widehat B_m,\qquad M=|m|.
\tag{T.1}
$$

对 $m\ne0$，准确方程为

$$
\begin{aligned}
b_m'&=M\gamma\ell c_m-2\beta b_m-M\gamma Q_m,\\
c_m'&=M\gamma b_m-\beta(\ell+1)c_m+\beta Q_m.
\end{aligned}
\tag{T.2}
$$

两个 mean 独立满足

$$
B_0'=-2\beta B_0,\qquad c_0'=-\beta(\ell+1)c_0+\beta Q_0.
\tag{T.3}
$$

所有物理模属于 $4\mathbb Z$。分片中心的环境空间为

$$
\|v\|_{X_0}=\sum_{m\in4\mathbb Z}\max_i\sup_{r\in I_i}|v_m(r)|,
\qquad \|U\|=\|B\|_{X_0}+\|c\|_{X_0}.
\tag{T.4}
$$

各径向片含两个闭端点，取片的最大值后再对模式求和。有限中心可以有准确 dyadic
接口跳；这些跳全部作为分布点源支付。真正未知解最终满足连续的积分方程，
并没有要求修正 $V=U-\widehat U$ 单独连续。

全频 $q_m$ 采用原真正 R74 regular Jacobi 线向内传播的正比值，保留
完整非零指数费用；$d_m=b_m+q_m c_m$。四输入为

$$
c_{\ne0}(L)=\widehat c_{\ne0}(L),\quad
\|d_{\ne0}(R)\|_{A_2}\le10^{-8},\quad
|B_0(R)|\le10^{-8},\quad |c_0(R)|\le10^{-8}.
\tag{T.5}
$$

这里 $A_2$ 的权为 $(1+|m|)^2$，两个 mean 不并入非零频率逆。
原紧支撑度量修正在 $r\ge.18$ 恒为零，所以此整个正帽的真实度量不依赖
有限 body 诊断中所用的 $\nu$；这一恒等式不允许向内侧修改区间外推。

## 2. 已付全频 Green 常数与相对中心导数

完整原生正帽的 949 个实际系数闭盒给出

$$
\begin{gathered}
C_*:=\inf_I|C_r|>.1705338016608,\quad
\ell\le\Lambda<1.693661030,\quad -\beta>3.051206775,\\
\sigma_D>2.925295874,\quad \sigma_C>.8601652212,
\quad q_+<1.389936764,\\
H_D<9.664149355,\quad H_C<2.389936764,
\quad K_G<15.952406835,\quad K_D<1.430261636.
\end{gathered}
\tag{T.6}
$$

$K_G$ 是完整 pair 的 $Q$ 源逆常数；一般两行残差使用各自的 $G_{\rm vec}$，
不能把它冒充标量 $Q$ 源。相应残差系数为

$$
K_B<3.303648510,\quad K_C<7.370324962,
\quad K_{0,C}<.171556979,
\quad K_{\rm mean}<.523455817.
\tag{T.7}
$$

保存这些线性常数的旧零中心 consumer 曾有 nonlinear 门失败；本篇只消费它
已通过的完整线性构造，未把旧 false 改为 true。

使用[相对中心完整导数预算](R133-supplement-relative-centre-full-derivative-budget.md)，定义

$$
B_\diamond=\sum_m\sup_I|\widehat B_m/C_r|,
\qquad c_\diamond=\sum_m\sup_I|\widehat c_m/C_r|.
\tag{T.8}
$$

未知修正仍按 (T.4) 的**绝对** pair 范数度量。若 $\|V\|\le\rho$，置

$$
b=B_\diamond+\rho/C_*,\qquad z=c_\diamond+\rho/C_*,\qquad d=1-z.
$$

由 $Q=C_r[(B/C_r)^2+\ell(c/C_r)^2]/(1+c/C_r)$ 直接微分和 Banach
代数乘法可得

$$
\|D_BQ\|\le\frac{2b}{d},\qquad
\|D_cQ\|\le\frac{2\Lambda z}{d}
             +\frac{b^2+\Lambda z^2}{d^2},
\qquad |C|\ge C_*d.
\tag{T.9}
$$

pair 范数为两分量之和，故 $\|DQ\|$ 取两列的最大值。
这里没有截断未知修正的高频。

## 3. 完整连续残差及所有接口点源

`fourfold_codazzi_cap_centered_residual_v5.py` 在原系数闭盒与完整 M64 三次分片
的公共分割上再各二分，共得到 **1988 个闭盒**。每一盒保持原 scalar germ；
到 $r=3/2$ 使用真实系数及中心的共同径向 Taylor 公式，与直接区间包络逐有限
Fourier 系数取交。其余正帽使用真实直接包络。中点和导数 provider 共享同一准确
germ 缓存，但每一个中点的完整 primitive 和尾界仍实际计算。

分子 $\widehat B^2+\ell\widehat c^2$ 的全部有限卷积与前三阶 Neumann 项
均保持完整，最终有限度为原四倍基频的 320，即物理频率达到 1280；没有混叠截断。
每个输出系数先在全部径向闭盒上取最大值，随后才求和，因此得到的是 (T.4)。
实际全径向值为

$$
\begin{aligned}
\|\widehat B\|_{X_0}&<.004351345444,&
\|\widehat c\|_{X_0}&<.003367844891,\\
B_\diamond&<.013982501845,&c_\diamond&<.010822199566.
\end{aligned}
\tag{T.10}
$$

准确商展开剩余满足

$$
\|Q-Q_{\le3}\|_{X_0}
\le \frac{\|\widehat B\|^2+\Lambda\|\widehat c\|^2}{C_*}
       \frac{c_\diamond^4}{1-c_\diamond}
<3.101755555\cdot10^{-12}.
\tag{T.11}
$$

它分别按 $\gamma$、$|\beta|/4$ 和 mean 的 $|\beta|$ 付入三条残差行。
完整实际残差界为

$$
\begin{aligned}
\|R_B/M\|_{X_0}&<1.196627853\cdot10^{-5},\\
\|R_C/M\|_{X_0}&<4.523175002\cdot10^{-6},\\
|R_{C,0}|_{C^0}&<1.903989880\cdot10^{-7},\\
\varepsilon_{\rm regular}&<7.301895359\cdot10^{-5}.
\end{aligned}
\tag{T.12}
$$

最后一行还含所有四边界端口费用。它未单独授存在：原完整三次中心有
**101 个内部接口、13029 个非零 dyadic 跳系数**。逐一使用有理数 Horner
准确求左右值，得到

$$
J_B<1.969852275\cdot10^{-19},\quad
J_C<1.362129183\cdot10^{-19},\quad J_0<3.744731911\cdot10^{-22}.
$$

由完整三角 Green 核，全部点源费用为

$$
\varepsilon_{\rm jump}
\le H_DJ_B+(H_Dq_++H_C)J_C+J_0
<4.059297111\cdot10^{-18}.
\tag{T.13}
$$

每一项都按点源支付，没有使用常规残差的 $1/M$ 收益。中心 $B$ 的 mean
恒为零。总费用和准确修正方程为

$$
\begin{aligned}
\varepsilon&=\varepsilon_{\rm regular}+\varepsilon_{\rm jump}
 <.000073018953589,\\
V&=Hh_{\rm diff}-G_{\rm vec}
 \left(R_{\rm regular}+\sum_i j_i\delta_{r_i}\right)
 +G_Q[Q(\widehat U+V)-Q(\widehat U)].
\end{aligned}
\tag{T.14}
$$

Green 分部积分恒等式把每个中心跳与 $V$ 中的反向跳抵消，故真实解满足
$U=Hh+G_QQ(U)$。有界分片源的 Green 积分连续，于是 $U$ 在所有接口连续。

## 4. 实际收缩和未知解的强角正则

在原半径 $\rho=1/2000$，实际有向计算给

$$
\lambda=K_G\sup\|DQ\|<.763531304<1,\qquad
\varepsilon+\lambda\rho<.000454784606<.0005.
\tag{T.15}
$$

所以 (T.14) 在完整分片 $X_0^2$ 中有唯一固定点，且该固定点的真实 $U$ 连续。
随后只作一次显式半径选择

$$
\rho_1=\frac{2\varepsilon}{1-\lambda(0)}
 \simeq .000362923661026425,
\qquad \lambda(0)<.597607093.
\tag{T.16}
$$

在这个完整新球上重新计算 (T.9)，而非把中心处导数当作整个球的导数，得

$$
\lambda_1<.717867141,
\quad \varepsilon+\lambda_1\rho_1<.000333549925<\rho_1,
\quad \rho_1-\varepsilon-\lambda_1\rho_1>.00002937373655.
\tag{T.17}
$$

由同一固定点的残差界，

$$
\|U-\widehat U\|_{X_0^2}<.000258810526,
\qquad \inf|C|>.1684294403.
\tag{T.18}
$$

完整 $A_2$ 正则来自原角平移论证，不预先假定无限高频消失。具体地，角平移在
$X_0$ 强连续；端口曲线在 $X_0$ 中具有两次强导数。严格内点余量允许局部平移
固定点，$(I-G_QDQ)^{-1}$ 的界为 $(1-\lambda_1)^{-1}$。取

$$
J_2=\Lambda\left(2/d_*+4S/d_*^2+2S^2/d_*^3\right),
\quad S=\|\widehat B\|+\|\widehat c\|+\rho_1,
$$

其中 $d_*$ 为球内真实 $|C|$ 下界，就由两次微分得到

$$
U_1\le\frac{H_1}{1-\lambda_1},\qquad
U_2\le\frac{H_2+K_GJ_2U_1^2}{1-\lambda_1}.
\tag{T.19}
$$

逐 Fourier 坐标的强导数分别等于 $imU_m,-m^2U_m$，所以这是完整
$\sum_m|m|^j\sup_r|U_m|$。实际结果为

$$
\|\partial_\theta U\|_{X_0}<.113854022,
\quad \|\partial_\theta^2U\|_{X_0}<16.655361,
\quad \|U\|_{X_2}<16.891151.
\tag{T.20}
$$

mean 的角导数准确为零，外侧 $d$ 的导数由原非齐次 $A_2$ 预算支付。
这些是曲率场角正则界，不是材料位移 Hessian。方程和原目标的一侧/接缝正则
给真实连续径向曲率场，R126 的局部框架重建给局部 $C^2$ 等距浸入；
周期闭合仍须保留完整 holonomy 方程。

## 5. 在 $r=9/10$ 的开放全频图与完整 M128 输入

现在允许 $c_{\ne0}(L)=\widehat c_{\ne0}(L)+h$，$\|h\|_{A_0}\le10^{-5}$，
其余三个外输入仍为 (T.5)。从已证 $\rho_1$ 记录取内侧端点，不外扩原管。
实际球像为

$$
\varepsilon+H_C10^{-5}+\lambda_1\rho_1
<.000357449293<\rho_1,
\qquad\text{margin}>.00000547436892.
\tag{T.21}
$$

因此完整无限 $A_0$ 邻域内真实解存在并可对四输入 Fréchet 微分；若新内迹另属于
$A_2$，仍有强二阶角正则，不要求其 $A_2$ 范数也小于 $10^{-5}$。

[开放端口恒等式](R133-supplement-open-nonlinear-curvature-port-graph.md) (O.7)–(O.14)
逐字适用于此新区间：

$$
b_L=-q_Lc_L+Td_R+\mathcal N(U),\quad
B_0(L)=\tau_BB_0(R),\quad
c_0(L)=\tau_Cc_0(R)+\mathcal N_0(U).
\tag{T.22}
$$

此处完整非零迹导数余列为

$$
\|D_{c_L}b_L+q_L\|<.545212856,
\quad q_m(L)>.9429307446,
\quad \|(D_{c_L}b_L)^{-1}\|<2.514346.
\tag{T.23}
$$

最后一界是完整无限非零模 Neumann 逆。两个 mean 另有真实线性传递
$\tau_B<1.293411892\cdot10^{-10}$、$\tau_C<7.117370118\cdot10^{-11}$；
$c_0$ 对内侧非零数据的非线性导数列小于 $.199540303$。从 D/mean 行直接消费
全部残差与接口费用，得到基准内端误差

$$
e_{bL}<2.290749048\cdot10^{-5},\qquad
e_{c0L}<6.129153664\cdot10^{-6},\qquad
|B_0(L)|<1.293411892\cdot10^{-18}.
\tag{T.24}
$$

完整 M128 候选的真实二进制 $\nu=-6837290349363917/288230376151711744$。
消费其所有分片和全部128正模/负共轭，在准确 $r=9/10$ 有理 Horner 求值后，
与完整 M64 数据之差实际满足

$$
\|\Delta c_L\|_{A_0}<2.430488274\cdot10^{-10},\qquad
\|\Delta b_L+q_L\Delta c_L\|_{A_0}<7.535284882\cdot10^{-10}.
\tag{T.25}
$$

故其整个内侧非零 $C$ 迹位于 (T.21) 的开放图中。取以该准确输入驱动的真实帽，
由 (T.23)–(T.25) 得

$$
\|b_L^{\rm cap}-b_L^{128}\|_{A_0}<2.290837652\cdot10^{-5},\qquad
|c_{0,L}^{\rm cap}-c_{0,L}^{128}|<6.129212922\cdot10^{-6}.
\tag{T.26}
$$

真实帽的无限高模全在这些界内。非零 $C$ 迹由输入定义准确一致，另两迹误差没有
消失；有限 body 的 PDE、每个 PPoly 接口、真正 regular 尾和周期框架必须继续联立。
特别地，$Q\le0$ 的 mean 行仍禁止把非平凡正帽两端的 $c_0$ 同时免费置零。

## 6. 实际执行的数据

主 producer 为 `scripts/fourfold_codazzi_cap_centered_residual_v5.py`。
一次完整执行得到 `notes/2026-11-13-R133-centered-cap-r09-v5-native.json.gz`，
含全部1988闭盒、完整逐模式上界、真实输入和依赖身份；运行约2616秒。
实际接口与强正则消费分别保存在

- `notes/2026-11-13-R133-centered-cap-r09-v5-jumps-native.json.gz`；
- `notes/2026-11-13-R133-centered-cap-r09-regularity-native.json.gz`。

它们使用已有的 `fourfold_codazzi_centered_cap_interface_jumps.py` 与
`fourfold_codazzi_centered_cap_regularity.py` 的相对中心分支，没有改写旧 $r=1$ 结果。
开放图和全 M128 内迹的实际运算为

- `notes/2026-11-13-R133-open-curvature-ports-r09-v2-native.json.gz`；
- `notes/2026-11-13-R133-M128-actual-inner-cap-r09-trace-native.json.gz`。

对应源分别为 `fourfold_codazzi_cap_open_curvature_ports_v2.py` 和
`fourfold_codazzi_cap_M128_inner_trace.py`，只将输入改为上述新区间报告。
这里保留原全谱、mean、真实 regular Jacobi 费用和接口跳；原未含跳的中间
`actual_driven_cap_exists` 字段不被单独消费。最终存在性明确以完整 jump 报告及
(T.14)–(T.19) 为依据。
