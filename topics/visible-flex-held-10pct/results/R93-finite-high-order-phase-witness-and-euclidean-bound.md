# R93. 高阶活动矩的有限相位见证及全欧氏群定量下界

2026-11-28；Astra-held10-7c4e33ee-20261128，analytic_construction 核查有限差分与距离估计。**状态：条件几何引理已证明，准确小标量已执行；没有新的实际 λ1 曲面。**

[R67](R67-universal-threefold-marker-and-euclidean-noncongruence.md)已去掉指定三阶矩必须非零的假设：任意非圆三重凸核心都有某个有限 $N=3J$ 阶复面积矩非零，固定全谐波帽可使完整相位族非全等。本条给该接口一个有限、明确的相位集合及定量预算，不重新声称矩唯一性本身是新结论。

若新完整图真实支付 R87 的全部前提，则对每个已认证非零的阶数 $N=3J$，只须考察 $J$ 个明确相位，不需要先找到某个未指定的开区间见证。再将 R88 的三阶表面距离估计推广到同一完整秩 $N$ 张量。两部分都不继承旧 λ=.002 的数值矩或几何界。

## 1. 完整对称、张量和活动分解

设同一已完成闭族的有界内部为 $\Omega_\alpha$，沿用 R67 的完整张量分解
$$
T_N(\alpha)=\int_{\Omega_\alpha}X^{\otimes N}\,dV
 =R_\alpha^{\otimes N}A^{(N)}+B^{(N)},\qquad
I_N(\alpha)=\|T_N(\alpha)\|_F^2.
\tag{1}
$$

要求活动张量 $A^{(N)}$ 和固定帽张量 $B^{(N)}$ **各自**在旋转 $2\pi/3$ 及反射 $y\mapsto-y$ 下不变。这是 R67 的逐片真实分解合同；仅有总初态反射对称而任意拆成两项，不足以使用以下偶性。完整体积又保持三重旋转和 $z$ 反射，所以每个相位的质心均为零；(1)是中心矩，其范数对全部 $E(3)$、包括反射不变。

令最高水平权的复矩为 $A_N$ 和 $B_N$，分别是活动张量与固定帽张量在 $(x+iy)^N$ 上的收缩。活动项也可用 R67 逐片散度分解定义，不要求活动部分单独围成闭体。上述逐项 $y$ 反射给两者为实数；R67 的准确全谐波帽给
$$
B_N=2\int_{|z|<r_c}z^N f(z)\,dA
=\frac{6\pi\varepsilon\,2^{1-J}r_c^{N+2}}
 {(N+1)(N+2)(N+3)(N+4)}>0,\qquad N=3J.
\tag{2}
$$

张量空间在水平旋转下的不同权正交。完整最高权 $\pm N$ 的范数贡献为
$$
2^{1-N}|A_Ne^{iN\alpha}+B_N|^2.
$$
其余权严格小于 $N$；三重对称仅保留 $3h$，逐项反射使交叉项没有正弦。因此
$$
I_N(\alpha)=a_0+\sum_{h=1}^J a_h\cos(3h\alpha),
\qquad a_J=2^{2-N}A_NB_N.
\tag{3}
$$
完整张量中的所有较低权仍然存在，没有把完整范数换成单个水平复矩范数。

## 2. R87 时间域内的有限相位集合

取
$$
x_j=1-\frac{3j}{2J},\qquad
\alpha_j=\frac13\arccos x_j,\qquad j=0,\ldots,J.
\tag{4}
$$
则 $\alpha_0=0$、$\alpha_J=2\pi/9$，且
$$
0\le\alpha_j\le\frac{2\pi}{9}<\frac{44}{63}<\frac45,\qquad
\frac45-\frac{44}{63}=\frac{32}{315}>0.
\tag{5}
$$
全部相位严格落在 R87 的完整 $[0,4/5]$ 时间域内，未使用旧 $9/20$ 端点。$x_j$ 是准确有理数；$\alpha_j$ 由准确反余弦定义，实际查询须明确其角度近似或包围误差。

用 Chebyshev 多项式 $\mathcal T_h$ 写
$$
P(x)=a_0+\sum_{h=1}^J a_h\mathcal T_h(x),\qquad Q(x)=P(x)-P(1).
$$
有 $Q(1)=0$、$Q(x_j)=I_N(\alpha_j)-I_N(0)$。$\mathcal T_J$ 的最高系数为 $2^{J-1}$（$J=1$也成立），故 $Q$ 的最高普通幂系数为 $2^{J-1}a_J$。

记 $h=-3/(2J)$。次数不超过 $J$ 的多项式满足准确有限差分身份
$$
\sum_{j=0}^J(-1)^{J-j}\binom Jj Q(1+jh)
=J!h^J\,2^{J-1}a_J.
\tag{6}
$$
第 $J$ 次差分消掉全部较低幂，并把 $x^J$ 变成 $J!h^J$，直接证明(6)。$j=0$项为零，其余权的绝对值之和恰为 $2^J-1$，所以
$$
\boxed{\max_{1\le j\le J}|I_N(\alpha_j)-I_N(0)|
 \ge c_J|A_NB_N|,\qquad
c_J=\frac{2^{1-3J}\,3^J J!}{J^J(2^J-1)}>0.}
\tag{7}
$$
例如 $c_1=3/4$、$c_2=3/64$。$J=1$时唯一新相位为 $2\pi/9$，完整三阶差值绝对值恰为 $3|A_3B_3|/4$。高阶时允许较低权在个别端点抵消，但它们不能同时消掉该有限集合中的全部差值。

本条不证明末端 $4/5$ 必为见证，也不证明不同相位两两不全等。README 的 $\delta_E$ 对全时间取最大，一个集合内见证已经足够。

## 3. 两个允许柱长给定量活动矩

记同一个非圆核心所围域的复面积矩为 $m_N=\int_Dz^N\,dA$。R67 已证明总柱长 $\ell$ 后
$$
A_N(\ell)=A_N(0)+\ell m_N.
$$
对准确允许长度 $\ell_1=1/200,\ell_2=1/100$，差为 $m_N/200$。三角不等式给
$$
\max\{|A_N(\ell_1)|,|A_N(\ell_2)|\}\ge |m_N|/400.
\tag{8}
$$
同一 $r_c,\varepsilon$ 的水平帽矩(2)不依赖帽高度，所以至少有一个允许长度和一个明确相位满足
$$
\boxed{|I_N(\alpha_j)-I_N(0)|
 \ge \frac{c_J}{400}B_N|m_N|.}
\tag{9}
$$

柱长是设计选择，须选定后与帽和所有物理输入一同冻结，再做该完整 $g$ 的相位族和精化。两个柱长不能混成固定 $g$ 的相邻精化。

若实际 CLI 使用 binary64 半柱长 $.0025,.005$，准确字面总长仍有 $\ell_2=2\ell_1,\ell_1>1/200$，故(8)的保守下界保持。但它们不等于准确 $1/200,1/100$；较大字面总长略大于 $1/100$ 时，完整几何须按字面值另付，不能借本段活动矩估计继承有理长度的几何上界。

R67 只保证某个有限 $N=3J$ 的 $m_N\ne0$，没有给未知最终核心的统一阶数上界。本条也不预报 $J=1$ 一定可用；仍须认证一个完整 $m_N$ 或直接认证一个 $A_N$。

## 4. 任意秩中心矩的表面 Hausdorff 控制

设两个真实闭面 $S_0,S_1$ 是 C² 嵌入球面，每个原点坐标中的点满足
$$
|X|\le R,\qquad X\cdot n\ge\sigma>0,\qquad R\ge\sigma,
\tag{10}
$$
并各自保持三重旋转和 $z$ 反射。(10)必须覆盖完整表面，局部/采样界不够。记其中心秩 $N$ 体积矩为 $T_i$，$I_i=\|T_i\|_F^2$，令
$$
d_E(S_0,S_1)=\inf_{Q\in O(3),\,a\in\mathbb R^3}d_H(S_0,QS_1+a).
$$
定义
$$
\begin{aligned}
d_*&=\sigma/3,& M&=R+\sigma/2,& V&=\frac{4\pi}{3}R^3,\\
L&=1+\frac{\pi R^2}{\sigma^2},&
C_{\rm vol}&=4\pi M^2L,\\
K_N&=2VR^N\left\{M^N C_{\rm vol}+\frac32NV M^{N-1}\right\}.
\end{aligned}
\tag{11}
$$
则
$$
\boxed{d_E(S_0,S_1)\ge
\min\left\{\frac{\sigma}{3},\frac{|I_0-I_1|}{K_N}\right\}.}
\tag{12}
$$

下面保留 R88 的真实表面距离和非凸体积，并把平移估计从 $3d$ 改进为 $3d/2$；旧 R88 的记录不改。

### 4.1 全部平移和反射

对紧凸集定义
$$
s(K)=\frac3{4\pi}\int_{\mathbb S^2}u\,h_K(u)\,d\omega.
$$
球面积分给 $s(QK+a)=Qs(K)+a$，包括反射。两个凸包各自的三重与 $z$ 反射使该积分点为零。对任意 $Q,a$，设 $S'=QS_1+a$、$d=d_H(S_0,S')$。支撑函数差 $\Delta h$ 的绝对值至多 $d$。若 $a\ne0$，取 $e=a/|a|$，有
$$
|a|=\frac3{4\pi}\left|\int_{\mathbb S^2}(e\cdot u)\Delta h(u)\,d\omega\right|
\le\frac{3d}{4\pi}\int_{\mathbb S^2}|e\cdot u|\,d\omega
=\frac32d.
\tag{13}
$$
最后一个积分为 $2\pi$，可在以 $e$ 为北极的球坐标直接算出；$a=0$时同界显然成立。凸包只用于平移控制，没有替换原体积。

若 $d\le\sigma/3$，则 $|a|\le\sigma/2$。原正支撑球面内部含 $B_\sigma(0)$；变换后内部含 $B_\sigma(a)$，原点仍在内部，外法向支撑至少 $\sigma-|a|\ge\sigma/2$。两个表面相对于原点都是唯一正径向图，半径 $\rho_0,\rho'$ 至多 $M$。这里使用既有正支撑球面引理的全部嵌入/拓扑前提。

### 4.2 最近表面点和真实体积差

原径向图法向公式给 $|\nabla_{\mathbb S^2}\rho_0|\le R^2/\sigma$。给定 $y=\rho'(u)u$，取 $x=\rho_0(v)v$ 满足 $|x-y|\le d$。由 $|x|\ge\sigma$，
$$
\big||x|-|y|\big|\le d,\qquad |u-v|\le2d/\sigma.
$$
球面测地距离至多弦长的 $\pi/2$ 倍，所以
$$
|\rho'(u)-\rho_0(u)|
\le d+\frac{R^2}{\sigma}\frac{\pi d}{\sigma}=Ld.
$$
两个真实内部都是同原点径向体，故
$$
\operatorname{Vol}(\Omega_0\mathbin\triangle\Omega')
=\frac13\int_{\mathbb S^2}|\rho_0^3-(\rho')^3|\,d\omega
\le4\pi M^2L\,d=C_{\rm vol}d.
\tag{14}
$$
没有要求最近点在同一射线上，也没有要求原内部凸。

### 4.3 完整秩 N 张量

原体积至多 $V$，所以 $\|T_i\|_F\le VR^N$。变换后的中心张量为
$$
Q^{\otimes N}T_1=\int_{\Omega'}(x-a)^{\otimes N}\,dx.
$$
秩一张量的 Frobenius 范数是 $|x|^N$，逐因子相减给
$$
\|x^{\otimes N}-(x-a)^{\otimes N}\|_F
\le NM^{N-1}|a|.
$$
先比较积分域再付中心平移，由(13)—(14)
$$
\|T_0-Q^{\otimes N}T_1\|_F
\le\left\{M^N C_{\rm vol}+\frac32NV M^{N-1}\right\}d.
\tag{15}
$$
$Q^{\otimes N}$ 对所有正交 $Q$ 都是等距，乘上两端张量范数和即得 $|I_0-I_1|\le K_Nd$。若 $d>d_*$ 已有第一分支，$d=0$则两个中心不变量相同。对所有刚体变换取下确界证明(12)，无需先找到最优配准。

## 5. R87 的条件代入与完整变化量

若最终同一新图真实支付 R87 的全部闭图/柱/帽预算，则
$$
D\le67251/25000<27/10,\qquad \sigma=41/500.
$$
完整体积质心为零，故 $0\in\operatorname{conv}(S)$，每个点到原点的距离不超过完整直径。因此可保守取 $R=27/10$；这从完整图得来，不能从 R87 首圆片或首周期局部界直接取全图半径和支撑。

将(11)中每个 $\pi$ 替成 $22/7$，所有正向单调项给完全有理的 $\overline K_N$。对一个已选定且有真实 $|A_N|$ 下界的固定长度，(7)、(12)给
$$
\delta_E\ge\min\left\{\frac{41}{1500},
\frac{c_J|A_N|B_N}{\overline K_N}\right\}.
\tag{16}
$$
使用两长度选择和已认证的核心矩，则至少一个合法设计满足
$$
\delta_E\ge\min\left\{\frac{41}{1500},
\frac{c_J|m_N|B_N}{400\,\overline K_N}\right\}.
\tag{17}
$$
除以同一完整 $D$ 的真实上界即可得归一化下界。共同逐时刚体握持校正保留这些全 $E(3)$ 取商距离。

下界可能很保守；活动矩增益不等于最优距离的同比增益。柱长、帽和完整物理输入选定后仍须固定同一 $g$，不能以(16)—(17)替代频率/径向/时间精化。

## 6. 准确标量执行与未付输入

新入口 scripts/resume_20261128/analytic/high_order_phase_witness.py 只用 Fraction、整数二项式和完整多项式。实际对 $J=1,\ldots,8$ 核了全部低阶 Chebyshev 差分为零、最高项准确等于 $J!h^J2^{J-1}$、(7)的系数、两长度的 $1/400$ 预算、(5)相位余量，并以 $R=27/10,\sigma=41/500$ 生成完整有理 $\overline K_N$ 和条件距离系数。

初次执行使用 R88 的较粗 $3d$ 平移预算，随后采用本条(13)的 $3d/2$ 改进，重新完整执行真 exit0；当前小标量输出 SHA-256 为 f22292618a725d2f82cc3a202112a25087e557fea5b7c5ef46c28b7f95322a4e。见[实际小证书](../notes/2026-11-28-high-order-phase-witness-scalars.json)，绑定当前源和 R67/R87/R88 全 SHA。有限列表检查未被当作全 $J$ 证明；全阶结论由上文直接推导。

~~~bash
python scripts/resume_20261128/analytic/high_order_phase_witness.py \
  --max-j 8 --radius 27/10 --support 41/500 \
  --out /tmp/held10-r93-phase-scalars.json
~~~

没有提供或编造新 λ1 的核心矩、活动矩、最终 physical-H、完整几何或网格。真正最终场仍须支付(1)、(2)、(10)以及所用矩的认证；本条将已证明的高阶非全等接口变成有限明确相位和可代入的全 $E(3)$ 预算，不是课题完成声明。

