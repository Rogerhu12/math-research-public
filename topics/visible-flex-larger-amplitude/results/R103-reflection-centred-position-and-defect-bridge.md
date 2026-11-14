# R103：双反射居中位置桥与完整候选缺陷造成的中心漂移

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）。
日期：2026-11-13。
状态：完整条件定理；八段几何预算已作精确 BigInt 有理核算。真实外尾存在性、相对新参考的完整场误差以及全闭面的点对门仍未支付。

本文使用 [R32](R32-height-development-and-global-tail-graph.md) 的真实高度发展、共同中心和 cuff 正则性结论，不重新证明它们，也不替代 [R16](R16-local-geodesic-and-continuous-reach-cover.md) 的近点对曲率引理。新增内容是双反射下的定量位置和向量比较，以及非等距兼容候选的径向重建规范到逐圈居中规范的完整缺陷桥。四场误差及完整均值来自 [R99](R99-complete-mean-field-to-physical-jet-bridge.md)。

## 1. 对象与两个不同用途的参考

固定同一个真实度量

$$
g=E(r)\,dr^2+r^2d\theta^2,\qquad E=1+w^2,\qquad r,w>0.
\tag{103.1}
$$

先取一个实际兼容高度 $h$。其径向导数和二阶导数都来自同一个函数；完整均值采用 R99 的真实小根。假定

$$
h(r,-\theta)=h(r,\theta),\qquad
h(r,\theta+\pi)=h(r,\theta).
\tag{103.2}
$$

这保留全部偶频，包括可能存在的无限高模。定义本节的物理归一量

$$
p=\frac{h_r}{\sqrt E},\qquad q=\frac{h_\theta}{r},
\qquad s=\sqrt{1-q^2},\qquad
\nu=\sqrt{1-p^2-q^2}>0,\qquad a=rs.
\tag{103.3}
$$

这里小写 $p,q$ 与 R99 的 $P=h_\theta/(rw)$、$K=h_r/w-1$ 不同。完整均值方程准确给出

$$
\Gamma=\frac1{\sqrt E\,\nu}
       +\frac{p q_\theta}{s^2\nu},
\qquad
\int_0^{2\pi}\Gamma(r,\theta)\,d\theta=2\pi.
\tag{103.4}
$$

积分等式使用真实均值根，不以数值接近 $2\pi$ 代替。由 (103.2)，$\Gamma$ 为偶函数且具有 $\pi$ 周期，因而

$$
\int_0^{\pi/2}\Gamma\,d\theta=\frac{\pi}{2}.
\tag{103.5}
$$

记

$$
\sigma(r,\theta)=\int_0^\theta\Gamma(r,u)\,du,\qquad
t=(-\sin\sigma,\cos\sigma),\qquad n=Jt,
\tag{103.6}
$$

其中 $J$ 是平面正向四分之一转。对 $0\le\theta\le\pi/2$ 定义

$$
X_1(r,\theta)=\int_\theta^{\pi/2}a(r,u)\sin\sigma(r,u)\,du,
\qquad
X_2(r,\theta)=\int_0^\theta a(r,u)\cos\sigma(r,u)\,du.
\tag{103.7}
$$

用关于两坐标轴的反射延拓到全圆。这给出一条中心为原点、$X_\theta=at$ 的闭合参考曲线。证明只用 $\sigma(-\theta)=-\sigma(\theta)$、
$\sigma(\theta+\pi)=\sigma(\theta)+\pi$ 和
$\sigma(\pi-\theta)=\pi-\sigma(\theta)$。本节不需要先证明 $\Gamma>0$。

对一般兼容候选，(103.7) 是逐圈的水平参考，不宣称其径向导数恰为等距发展，也不宣称整个参考是一个 $C^2$ 浸入。若 $h$ 是满足 R32 全部假设的真实 Darboux 高度，R32 已给真实 $C^2$ 发展；其所有圈具有同一个中心。又因对称轴上 $h_\theta=h_{r\theta}=0$，R32 的连接系数 $G(r,0)=0$，轴方向在径向上固定。因此真实发展在一个全局平移和旋转后，恰与 (103.7) 相同。

## 2. 四分之一圆的定量比较

对同一度量上的两个高度 $h^{(0)},h^{(1)}$，两侧均满足第 1 节的完整均值、真实正性和同一反射轴条件。给出同时覆盖两侧的上界

$$
|p|\le p_*,\quad |q|\le q_*,\quad |q_\theta|\le t_*,
\quad s\ge s_*>0,\quad \nu\ge\nu_*>0,
\tag{103.8}
$$

及同位置差界 $e_p,e_q,e_t$。令

$$
v=p_*e_p+q_*e_q,\qquad d_\nu=\frac{v}{\nu_*}.
\tag{103.9}
$$

由平方差除以两侧正平方根之和，

$$
|\delta\nu|\le d_\nu,\qquad
|\delta(\nu^{-1})|\le\frac{v}{\nu_*^3},\qquad
|\delta a|\le d_a:=\frac{r q_*e_q}{s_*}.
\tag{103.10}
$$

特别地，不需要在两侧之间免费假定新的复条带逆。设

$$
\begin{aligned}
g_*={}&\frac{v}{\nu_*^3}
+\frac{e_p t_*+p_*e_t}{s_*^2\nu_*}\\
&+p_*t_*\left(
\frac{2q_*e_q}{s_*^4\nu_*}
+\frac{v}{s_*^2\nu_*^3}\right).
\end{aligned}
\tag{103.11}
$$

则 $|\delta\Gamma|\le g_*$。证明是对 (103.4) 作乘积差；其中
$|\delta(s^{-2})|\le2q_*e_q/s_*^4$，首项的 $1/\sqrt E$ 仅用 $E\ge1$ 向上界为 $1$。

由精确四分之一转角，两侧 $\sigma$ 的差在 $0$ 和 $\pi/2$ 同时为零，所以

$$
|\delta\sigma(r,u)|
\le g_*\min(u,\pi/2-u),\qquad
\|\delta\sigma\|_\infty\le\frac{\pi g_*}{4}.
\tag{103.12}
$$

对 (103.7) 的两个坐标分别取差，再把 $[\theta,\pi/2]$ 和 $[0,\theta]$ 相加，得到

$$
\boxed{
\|\delta X(r,\theta)\|_2
\le\frac{\pi}{2}d_a+\frac{\pi^2}{16}r g_*.
}
\tag{103.13}
$$

这里使用 $a\le r$，以及
$\int_0^{\pi/2}\min(u,\pi/2-u)\,du=\pi^2/16$。
两条积分覆盖互不相交的区间，故没有再乘一个 $2$。反射延拓把该界保持到完整圆周。此式比较的是相同 $\theta$ 标签下的点，不把源角当作 Cartesian 极角。

## 3. 单位参考向量与真实法向

定义

$$
N_{\rm ref}
=-\frac{\nu q}{s}\,t+\frac{p}{s}\,n+\nu e_z.
\tag{103.14}
$$

它始终是单位向量。其水平分量的模恰为
$\sqrt{p^2+q^2}$。若高度来自真实等距发展，直接对 R32 的两个切向量取内积，得到 (103.14) 正是向上真实单位法向。一般候选只称它为单位参考向量。

令

$$
C_N=d_\nu\left(1+\frac{q_*}{s_*}\right)
+\frac{e_p+e_q}{s_*}
+\frac{q_*^2+p_*q_*}{s_*^3}e_q,
\qquad
\rho_*=\min(1,p_*+q_*).
\tag{103.15}
$$

前三个固定框架系数的差之和不超过 $C_N$。平面框架的角差为 $\delta\sigma$，而旋转只作用于长度至多 $\rho_*$ 的水平分量，因此

$$
\boxed{
\|\delta N_{\rm ref}\|_2
\le C_N+\rho_*\min\!\left(2,\frac{\pi g_*}{4}\right).
}
\tag{103.16}
$$

这是完整向量差，不把候选自己的欧氏法向当作 (103.14)。

若两侧的共同圆心还差 $e_C$、全局轴角还差 $e_\beta$，则 (103.13) 另加

$$
e_C+\frac{\pi r}{2}\min(2,e_\beta).
\tag{103.17}
$$

因为由 (103.7) 得 $\|X\|_2\le\pi r/2$。式 (103.16) 的角差项相应改成
$\rho_*\min(2,e_\beta+\pi g_*/4)$。只允许选择一个全局平面刚体规范，不能在每个径向子段独立旋转或重新对齐。

## 4. 完整场误差与一次均值高度积分

沿用 R99 的非均值归一场。若在完整相同位置已经证明

$$
\|\delta\overline K\|_{A_\tau^1}
+\|\delta P\|_{A_\tau^1}\le\varepsilon,\qquad \tau\ge0,
\tag{103.18}
$$

且全部非零频率 $|m|\ge2$，则

$$
e_p\le w_+(\varepsilon/3+\delta c_*),\qquad
e_q\le w_+\varepsilon/3,\qquad
e_t\le w_+\varepsilon.
\tag{103.19}
$$

$\delta c_*$ 必须由完整均值根差证明，不能令其为零。非均值高度差满足

$$
\|\delta h^\perp\|_\infty\le rw_+\varepsilon/6.
\tag{103.20}
$$

完整均值高度是

$$
\delta h_0(r)=\delta h_0(r_0)+
\int_{r_0}^r w(\rho)\delta c(\rho)\,d\rho.
\tag{103.21}
$$

只可选择一次初始常数。若整个比较区间长度小于 $1/3$，且其中 $w<3/25$，则

$$
|\delta h_0(r)|
\le |\delta h_0(r_0)|+\frac1{25}\sup|\delta c|.
\tag{103.22}
$$

这里的 $w<3/25$ 是本次 cell $0$、segment $7$ 八个子段的已付背景界，不是对所有外胞元无条件使用的界。更紧的版本直接使用已有每叶
$I_{00}+I_{01}=\int w\,dr$，无需新积分。

将 (103.13) 与 (103.20)–(103.22) 相加，给完整三维位置的一个安全上界。若后续用 prefix 的绝对高度规范，应带入其实际初始均值差，不能把 (103.22) 的零初值重新免费应用于每个子段。

## 5. 实际八段条件账本

本次混合参考只有 part $0$ 改成已经正式验收的物理 $r$ carrier，parts $1,\ldots,7$ 保持原 R48 候选。新的 part $0$ 与邻接部分共享全部非均值端点两 jet；完整均值根及其实际径向导数在这些端点由相同输入确定，均值高度则沿同一个常数连续积分。因此这是一个兼容的高度参考，而非跨候选逐点取最小值。

输入为：

- 已公开的 [R102 八段有理账本](../notes/2026-11-12-tail-r102-seg7-field-defect-budget.json)，SHA256 为
  d01b7310f9d76fa5d5d56f44805c67fedf7be776a78435803943edcda424bc6f。
- [carrier 独立极值摘要](../notes/2026-11-13-tail-r103-carrier-observed-extrema.json)，SHA256 为
  f2d12d6c0b41f96fdb969f2923091934012b81e40721c19f2410997c7131baa2。
  该摘要来自已经正式 exit $0$ 的全部 $111$ 叶曲率/实域消费者，完整原 $208048$ 字节主账本仍待正常 CLI 归档；摘要不代替原主账本。
- 相同真实度量的 R26 外半径 $R_{\rm out}<1/3$，以及 R95/R102 已付的本段 $w<3/25$。

输入域字段的语义不能丢掉。R102 与 carrier 生产者实际构造的是
$A_-=1-w_+^2P_*^2$、
$y_-=1-K_*$、
$L_-=1-K_*-E_*T_*$，然后向下舍入。因此可以使用
$|q|\le\sqrt{1-A_-}$、
$|K|\le1-y_-$、
$|P_\theta|\le1-L_-$。
从任意一个只有点态正性含义的 $y_-$ 或 $L_-$，不能反向推出这些范数界。本次使用的是已确认的生产公式。

对 part $0$，完整新域还有
$\nu^2>0.999525175129636708$、
$1+K>0.984898105732701371$。
由

$$
\frac{w^2y_-^2}{1+w^2}\le p^2\le1-\nu_-^2
$$

得到

$$
w^2\le
\frac{1-\nu_-^2}{y_-^2-(1-\nu_-^2)}.
\tag{103.23}
$$

分母严格为正，精确账本确认由此可取 $w<1/40$。这只收紧同一真实背景的上界，没有更换度量，也没有借用旧 part $0$ 的内部 jet。

取 $\varepsilon=1/512$，中心、反射轴及初始均值高度差均按一个共同全局规范置为零。程序用 $\pi<22/7$、所有正平方根的向上有理包围以及全部未舍入有理比较，得到：

| part | 参考 | 完整位置差上界 | 单位向量差上界 |
|---|---|---:|---:|
| 0 | 新物理 $r$ carrier | 0.000005957686168494 | 0.000030399830815381 |
| 1 | 原 R48 | 0.000024760539453264 | 0.000181132259581343 |
| 2 | 原 R48 | 0.000024583142596797 | 0.000177859659056563 |
| 3 | 原 R48 | 0.000024410726516868 | 0.000174675086005441 |
| 4 | 原 R48 | 0.000024328678407805 | 0.000173158416773820 |
| 5 | 原 R48 | 0.000024323979053690 | 0.000173072488825730 |
| 6 | 原 R48 | 0.000024342701744422 | 0.000173420172529618 |
| 7 | 原 R48 | 0.000024346830689301 | 0.000173496660087709 |

全部八段的位置严格小于 $1/8192$，向量差严格小于 $1/4096$。完整账本是
[2026-11-13-tail-r103-centred-geometry-actual.json](../notes/2026-11-13-tail-r103-centred-geometry-actual.json)，源为
[tail_r103_reflection_centred_geometry.js](../computations/tail_r103_reflection_centred_geometry.js)。

这次计算已经在 functions.exec 的 V8 内实际完成；$12$ 个总门全部为真。它没有启动 OS 进程，故不填写虚构的进程 exit code 或 RSS；没有使用 Node、Arb、二进制输入、ODE 或新积分。所有输出上界向上记录到 $96$ 个二进制小数位，下界向下记录，判门使用未舍入有理数。该执行不支付假设 (103.18)，也不把布尔假设记录当作真实外解存在性的证书。

## 6. 原径向参考到居中参考的候选缺陷桥

本节支付一个此前不能直接略过的规范差。R32 的共标架写为

$$
\alpha=b\,dr+a\,d\theta,\qquad \beta=c\,dr,\qquad
b=-\frac{h_rh_\theta}{a},\qquad
c=-\frac{\sqrt E\,r\nu}{a}.
\tag{103.24}
$$

令

$$
\Gamma=\frac{b_\theta-a_r}{c},\qquad
G=\frac{b\Gamma+c_\theta}{a}.
\tag{103.25}
$$

即使候选没有满足 Darboux 方程，第一结构方程仍准确成立。设
$\Omega=\Gamma_r-G_\theta$。R32 的曲率恒等式与 R99 的完整分子 $J_x$ 给

$$
K_{g-dh^2}
=\frac{K_g\nu^2-\det_g(\operatorname{Hess}_g h)}{\nu^4},
\qquad
|\Omega|=|K_{g-dh^2}|\sqrt E\,r\nu
=\boxed{\frac{w^2|J_x|}{r_xD^{3/2}}},
\quad D=E\nu^2.
\tag{103.26}
$$

这里只使用绝对值，因此不把两种连接曲率号约定混同。$J_x$ 必须包含完整标量均值和全部有限带外频率。对物理 $r$ 版本，$r_x=1$；对源坐标版本不能丢掉 $r_x$。

考虑原径向优先参考 $X^{\rm rad}$：其 $\theta$ 导数为 $at$，在轴上按
$(X^{\rm rad})_r(r,0)=V(r,0)$ 取基点，其中 $V=bt+cn$。其角度仍为 (103.6)，因为轴上 $G=0$。置

$$
\delta=\sigma_r-G,\qquad
Y=(X^{\rm rad})_r-V.
$$

从 (103.25) 直接微分，恰有

$$
Y_\theta=a\delta n,\qquad Y(r,0)=0,\qquad
\delta_\theta=\Omega,\qquad \delta(r,0)=0.
\tag{103.27}
$$

反射轴上 $G=0$，而精确四分之一转角对 $r$ 微分为零，所以
$\delta(r,k\pi/2)=0$。因此在每个四分之一圆上

$$
|\delta(r,\theta)|
\le\|\Omega(r,\cdot)\|_\infty
\,\operatorname{dist}\!\left(\theta,\frac{\pi}{2}\mathbb Z\right).
\tag{103.28}
$$

定义原参考圈的中心

$$
C(r)=\frac{X^{\rm rad}(r,0)+X^{\rm rad}(r,\pi)}2.
$$

以下 $C'(r)$ 明确指真实物理 $r$ 导数。$V(r,\pi)=-V(r,0)$，故由 (103.27)

$$
C'(r)=\frac12\int_0^\pi a\delta n\,d\theta,
\qquad
\boxed{|C'(r)|\le\frac{\pi^2r}{16}
       \|\Omega(r,\cdot)\|_\infty.}
\tag{103.29}
$$

$\int_0^\pi\operatorname{dist}(\theta,(\pi/2)\mathbb Z)\,d\theta=\pi^2/8$ 是该常数的来源。两种参考具有相同的完整角导数，因此

$$
X^{\rm rad}(r,\theta)-X^{\rm cen}(r,\theta)=C(r)-C_{\rm fixed}
\tag{103.30}
$$

与 $\theta$ 无关。它们的角度和 (103.14) 单位参考向量相同；这里只累积平面中心位置，不凭空添加法向转角差。

结合 (103.26)–(103.29)，对任意连续径向区间，

$$
\boxed{
|C(r)-C(r_0)|
\le\frac{\pi^2}{16}\int_{r_0}^r
\frac{\rho w(\rho)^2}{r_x(\rho)D(\rho)^{3/2}}
\|J_x(\rho,\cdot)\|_\infty\,d\rho.}
\tag{103.31}
$$

这不是把非精确候选变成真解。候选的完整缺陷为零时，(103.31) 才退化到 R32 已证的共同中心结论。

### 既有正积分的逐叶消费

若同一真实叶已有 $r_+,w_+$、$r_{x,-}>0$、
$d=\min(1,D_-)>0$、完整 $J_*\ge\|J_x\|_\infty$ 和
$\omega_I\ge\int_I w\,dr$，则该叶增量可取

$$
\Delta C_I\le
\frac{\pi^2}{16}
\frac{r_+w_+J_*}{r_{x,-}d^2}\,\omega_I.
\tag{103.32}
$$

因为 $w^2dr\le w_+w\,dr$ 且 $D^{-3/2}\le d^{-2}$。
现有五真积分给 $\omega_I=I_{00}+I_{01}$，所以可以直接在本地完整读取原 gzip 后流式求和，不需新 ODE 或积分。越过子段要继续累计，不得重新把中心设成零。若使用物理 $J_r$，显式置 $r_x=1$；若使用原 $J_x$，使用同叶 $r_x$ 下界。

本节在每个光滑片内按经典导数证明。有限 Fourier 候选的径向系数在片内足够光滑，所需角导数存在；拼接处由实际共享两 jet、连续共标架及完整积分式取极限。若一般高度只有抽象 $C^2$ 正则性而没有这些角向或片内导数，不直接调用 $\Gamma_r,G_\theta$ 的经典公式，须使用 R32 的连续连接/弱 Stokes 版本或先单独支付相应正则性。本节没有把非等距候选的居中参考无条件升级为 $C^2$ 曲面。

## 7. 后续几何接合的准确范围

已付的是：同一混合高度参考的八段实域、条件曲率预算，以及在真实完整场误差 $\varepsilon=1/512$ 假设下的居中位置和真实法向比较。候选一侧只使用参考向量。

仍须支付：

1. 同 $g$ 的完整外头解及 (103.18)，包括所有高频、完整均值、node $12$ 真迹和外前缀接口。
2. 若使用原径向空间审计，按 (103.32) 实际消费完整候选缺陷以付居中规范差；当前八段账本没有执行这一项。
3. 原 R48 与新 carrier 之间的实际空间桥及一个全局 mean 常数；PA→CF 桥不能冒充原 R48→CF。
4. 全闭面剩余连续远点对、接缝、全时间参数和 held/幅度门。R16 的近点对引理不替代这些项目。

两个候选共享端点两 jet，只支付接口相容，不支付内部误差。也不能把本结果的两个位置上界直接视为已证 reach。恢复顺序和准确源/输入身份见 [执行计划](../notes/2026-11-13-tail-r103-centred-geometry-plan.json)。原 $25$ 个实际 mean/frame/曲率文件仍先核原件再按正常 CLI 归档；本小账本与证明不是它们的编码或分片。
