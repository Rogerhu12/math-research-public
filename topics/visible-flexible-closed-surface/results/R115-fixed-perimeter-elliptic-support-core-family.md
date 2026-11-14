# R115：固定周长的椭圆支撑核族与强中央几何窗口

2026-11-12，constructive_geometry。正式结果 R115；供强目标固定 g 的新 BVP 消费。
**这里给出的是准确中央核族及其圆柱段，不是完整闭曲面或已解的尾匹配。**

## 1. 准确族与共同周长

固定 \(A=7/5,B=1/2\)，令

\[
h_E(\phi)=\sqrt{A^2\cos^2\phi+B^2\sin^2\phi},\qquad
a_0=\frac{2A E(1-B^2/A^2)}\pi.
\]

取任意有限 M，记 \(m_j=2j\)、\(c_j=1-m_j^2\)，定义

\[
h_p(\phi)=h_E(\phi)+\sum_{j=1}^M p_j\cos(m_j\phi),\qquad
n=(\cos\phi,\sin\phi,0),\quad t=(-\sin\phi,\cos\phi,0),
\]

\[
\Gamma_p(\phi)=h_p(\phi)n+h_p'(\phi)t,
\qquad \rho_p=h_p+h_p''.
\tag{1}
\]

对椭圆基项直接微分，

\[
\rho_E=\frac{A^2B^2}{h_E^3},\qquad
\frac{B^2}A=\frac5{28}\le\rho_E\le\frac{A^2}B=\frac{98}{25}.
\tag{2}
\]

因此全参数域

\[
\mathcal P_M=\left\{p:\sum_{j=1}^M(m_j^2-1)|p_j|<\frac5{28}\right\}
\tag{3}
\]

保证

\[
\rho_p\ge\frac5{28}-\sum_j(m_j^2-1)|p_j|>0.
\tag{4}
\]

又 \(\Gamma_p'=\rho_p t\)，所以 (1) 是严格凸、正则、闭合的平面曲线。
全部修正项均为零均值，且 h′ 为周期函数，因此

\[
L_p=\int_0^{2\pi}\rho_p\,d\phi
=\int_0^{2\pi}h_p\,d\phi=2\pi a_0
\tag{5}
\]

**与全部 p 无关**。这不是每次迭代重新缩放周长；a0 自始至终相同。
由 (3)，\(\sum|p_j|<5/84<1/2\)，故 h_p 也严格正，原点位于凸体内部。

## 2. 准确弧长、两 jet 与材料参数

令 \(S_E(\phi)=\int_0^\phi\rho_E(v)\,dv\)。它可通过椭圆积分直接计算：
将
\(\theta=\operatorname{atan2}(B\sin\phi,A\cos\phi)\)
连续展开到同一周数后，

\[
S_E(\phi)=A\{E(\theta-\pi/2\mid 1-B^2/A^2)+E(1-B^2/A^2)\}.
\]

定义

\[
S_p(\phi)=S_E(\phi)+\sum_j\frac{c_jp_j}{m_j}\sin(m_j\phi),
\qquad S_p(\phi_p(\sigma))=a_0\sigma.
\tag{6}
\]

由 (4)，反函数全周存在且光滑。取材料角 \(\sigma\in\mathbb R/(2\pi\mathbb Z)\)，
准确中央圈为 \(\gamma_p(\sigma)=\Gamma_p(\phi_p(\sigma))\)。
其导数特别简单：

\[
\gamma_{p,\sigma}=a_0t,\qquad
\gamma_{p,\sigma\sigma}=-\frac{a_0^2}{\rho_p}n.
\tag{7}
\]

所以全部 p 的中央材料度量同为 \(a_0^2d\sigma^2\)。
在任意固定长度的中央圆柱段取

\[
X_p(s,\sigma)=\gamma_p(\sigma)+s e_z.
\tag{8}
\]

则该段诱导度量准确为 \(ds^2+a_0^2d\sigma^2\)，并且

\[
X_s=e_z,\qquad X_{ss}=X_{s\sigma}=0.
\tag{9}
\]

(7)、(9) 是中央位置、全部一阶和二阶数据的约定。
随后使用同一个 frozen a(s)，不能随 p 更改径向背景或重新缩放 a0。
每个 p 的潜在闭曲面相位仍平移 \(\sigma\)，不是平移法向角 \(\phi\)。

也可采用一个**与 p 无关**的基准偏心角 θ，以减少准确椭圆初值的 Fourier 复杂度。
令 \(r(\theta)=S_E^{\rm ecc}(\theta)/a_0\)，其中 \(S_E^{\rm ecc}\) 是原椭圆从偏心角计算的弧长。
则 \(r'=\ell_E/a_0\)、\(r''=\ell_E'/a_0\)，并取
\(\widetilde\gamma_p(\theta)=\gamma_p(r(\theta))\)。所有 p 的角度量仍准确为
\(\ell_E(\theta)^2d\theta^2\)，后续为
\(ds^2+(a/a_0)^2\ell_E(\theta)^2d\theta^2\)。
角导数和参数角导数都按
\(D_\theta=D_\sigma r'\)、
\(D_\theta^2=D_\sigma^2(r')^2+D_\sigma r''\) 转换。
这不是用每个 p 自己的偏心角或法向角替换材料坐标。
如果使用这一坐标连接尾 DN，尾的 Fourier 角仍是 σ，必须通过固定 r 映射转换。

## 3. 对全部中央参数的准确导数

在固定材料角 \(\sigma\) 下对 (6) 微分：

\[
\partial_{p_j}\phi_p=-\frac{c_j\sin(m_j\phi_p)}{m_j\rho_p}.
\tag{10}
\]

固定法向角时，\(\partial_{p_j}\Gamma=\cos(m_j\phi)n-m_j\sin(m_j\phi)t\)。
再加 \(\Gamma_\phi\partial_{p_j}\phi=\rho_pt\partial_{p_j}\phi\)，得到

\[
J_j:=\partial_{p_j}\gamma_p
=\cos(m_j\phi_p)n-\frac{\sin(m_j\phi_p)}{m_j}t.
\tag{11}
\]

这里已包括随参数移动的法向角；漏掉 (10) 会给错 BVP 中央 Jacobian。
写 \(\rho'=\partial_\phi\rho_p\)，继续对材料角微分得到

\[
\partial_\sigma J_j
=\frac{c_ja_0\sin(m_j\phi_p)}{m_j\rho_p}n,
\tag{12}
\]

\[
\partial_\sigma^2J_j
=\frac{c_ja_0^2}{m_j}\left[
\left(\frac{m_j\cos(m_j\phi_p)}{\rho_p^2}
-\frac{\rho'\sin(m_j\phi_p)}{\rho_p^3}\right)n
+\frac{\sin(m_j\phi_p)}{\rho_p^2}t\right].
\tag{13}
\]

参数 Hessian 也有闭式：

\[
\partial_{p_k}J_j
=-\frac{c_jc_k\sin(m_j\phi_p)\sin(m_k\phi_p)}{m_jm_k\rho_p}n.
\tag{14}
\]

它显式对称。所有 \(\partial_{p_j}X_s\)、\(\partial_{p_j}X_{ss}\)、
\(\partial_{p_j}X_{s\sigma}\) 在中央柱段均为零。
(10)–(14) 通过对 (1)、(6) 的直接微分得到，不涉及有限差分或截断 Fourier 假设。

## 4. 一个有严格余量的统一强中央核窗口

以

\[
\bar p=(1/200,0,\ldots,0),\qquad p=\bar p+q,
\qquad \sum_j(m_j^2-1)|q_j|\le\frac3{250}
\tag{15}
\]

为具体搜索窗口。由 \(m_j^2-1\ge3\)，\(\sum|q_j|\le1/250=.004\)。
因而整个窗口内

\[
\rho_p\ge\frac5{28}-\frac3{200}-\frac3{250}
=\frac{1061}{7000}>.136,
\quad |\kappa|\le\frac{7000}{1061}<6.598<7.1.
\tag{16}
\]

长、短轴的支持值记为

\[
A_p=h_p(0)=A+\sum_jp_j,
\qquad B_p=h_p(\pi/2)=B+\sum_j(-1)^jp_j.
\]

全部偶频率使 h′ 在两个轴上为零，故 \((\pm A_p,0)\)、\((0,\pm B_p)\)
都是准确曲线点，且严格凸性说明它们给相应轴向支持。
由 (15)，

\[
A_p\ge1.401,\qquad B_p\le.499,\qquad
A_p-B_p=.9+2\sum_{j\ \mathrm{odd}}p_j\ge.902.
\tag{17}
\]

因此中央圆柱相位旋转 π/2 后的长轴点，对原圆柱的距离至少 .902。
这给强握持所需 .9 留出 .002 的**中央**余量。
还可由 h_p≤A+Σ|p_j|≤1.409 得整个中央平面曲线位于半径 1.409 的圆盘内。

对圆柱本身，(16) 不只是局部曲率估计。
\(h_p-r\) 在 \(r=1061/7000\) 时仍有非负曲率半径，给一个凸体的支持函数，
所以原平面凸体是该凸体与半径 r 圆盘的 Minkowski 和。
每个边界点有半径 r 的内滚圆；外滚圆由凸性得到。
这使平面闭曲线的 reach 至少 r。正交乘以任意闭区间时最近点投影逐因子分解，
因此 (8) 的圆柱片作为闭子集也有 reach≥r。
把其他活动片和固定帽接入之后，仍须验证它们没有进入这些法球；不能据此直接给整个闭面的 reach。

## 5. 哪些 R113 条件直接保留，哪些仍须检查

以下两点是对固定帽证明的直接保留，不需要完整活动轨迹来改变帽参数。

1. **周长、中央度量和固定 cuff 要求。** (5) 保持 v2 的 a0，故这个族提供 M 个真正的中央外在自由度。
   若新 BVP 得到准确圆 cuff 的共同两 jet，原固定帽嫁接照常适用。
   目前并未得到这个 cuff 条件。
2. **欧氏商的八点支撑部分。** R113 的两个中央轴点原取 `(±1.4,0,0)`。
   这里有真实点 `(±A_p,0,0)`，且 A_p≥1.401>1.4。
   两个原中央点属于这两个新点之间的线段，所以加入原来的六个固定帽标记后，
   新标记凸包包含旧标记凸包。固定帽的近点误差不变，R113 的标记内接球下界不会下降。

其余条件不能从 A_p、B_p 自动继承，具体如下。

- **完整窄板条件。** 中央圈确有 `|y|≤B_p≤.499`，但 R113 需要整个实际活动核在相位 0 时 `|y|≤.75`。
  新曲线沿 s 演化后是否仍在该窄板内，必须从实际 XYZ 检验。
  只有该全核条件通过，旋转 π/2 后的活动核与固定帽才共同落入 x 半宽 .75 的窄板，
  此时上述八点凸包论证才给原有严格欧氏商下界。
- **完整 held 保护曲线。** R113 的充分条件是实际相位 0 活动核在 `|z|≤.9` 内满足
  `y≤.5+(5/9)z²`。中央柱段由 (17) 自动满足，但沿 s 的所有后续部分仍需重验。
  若该旧充分条件及原帽位置条件都通过，则球心 `(0,1.4,0)` 的半径 .9 球仍被避开。
  本族的真实旋转见证为 `(0,A_p,0)`；全表面 y≤max(.75,1.37+.0001+.000001)<1.4≤A_p，
  所以把球心从 1.4 增加到 A_p 只会增大各点到球心的距离。
  因此该**已验证的全核保护条件**仍足以支付强 held，而不是只凭轴支持支付。
- **整个旧闭核的全时 reach、球包和上下接口高度。** (16) 仅覆盖中央圆柱。
  完整活动核需重新检查所有 s、所有角度的实际主曲率及全局法球、球半径 2.25、
  高度窗口、准确 cut/cuff 接合。相位转动后的帽—活动片跨片法球也必须满足 R113 的假设。
- **度量与尾匹配。** 每个初始曲线有同一准确周长，不表示它沿完整 frozen a(s) 一定有解，
  更不表示有限线性尾条件就是非线性条件。须保持原完整 E、F、G 检验及真实非线性尾 DN。

## 6. 可直接消费的实现

`scripts/fd2d_ellipse_support_core.py` 提供：

- `EllipseSupportCore(p).evaluate(sigma)`：准确族的 F、Fσ、Fσσ、Xs、Xss、Xsσ；
- `parameter_derivatives(sigma, angular_order=0|1|2)`：公式 (11)–(13)，形状为 M×N×3；
- `parameter_hessian(sigma)`：公式 (14)；
- `evaluate_reference_angle(theta)` 与 `parameter_derivatives_reference_angle(theta,order)`：
  同一个基准椭圆偏心角下的准确求值及链式导数，便于一阶 Gauss–Codazzi 入口；
- `inlet(flow,angular)` 与 `inlet_jacobian(flow,angular)`：投影到已有 flow 的材料角 Fourier 基，
  并报告实际位置、一阶、二阶和相对角度量投影误差；
- `summary()`：真实系数、整个参数凸性下界、轴支持及是否位于 (15)。

可从 `p=(.005,0,...,0)` 开始，固定 v2 的整个 a(s)，以 p 为中央参数解 M 个真实尾条件。
原 `SupportBVP` 的基准核心是平均半径 1 的单余弦族，不能只改函数名后沿用它的 a0=1 假定。
新 flow 的背景半径、核心投影目标和线性基准都必须使用本题 a0。
内部参数缩放可由 `(m_j²−1)|q_j|` 的预算选取，不得把参数缩放混同为度量缩放。

`2026-11-12-fd2d-ellipse-support-core-check.json` 保存有限输入核对及参数 jet 的中心差分比较。
这些检查用于发现实现错误；准确共同周长、C∞ 核、解析 Jacobian 和窗口 (15) 的结论由上述计算证明。
