# R17：旋转参考的线性平端相容性与固定圆领零 trace

## 结论范围

本结果只研究**一个旋转参考面附近的线性等距方程**，角模 m≥2，参考末段的母线角单调趋于平面，端圆半径严格为正。它说明：固定圆领的零位移 trace 在该末段只能产生零线性解；允许非零法向 trace 时也必须满足明确的 Robin 条件。特别地，从未弯曲的平基点出发，R128 平坦弯尾的小振幅方向不能满足这个相容性，除非该方向在端口范围内平凡。

这不排除远离旋转面的非旋转准确核心，不排除其他边界族，也不证明所有非线性嵌入不存在。不得把下面的线性局部结论扩大为本题的一般不可解性。

## 1. 参考面、法向号与 m 模方程

令

\[
 X(s,\theta)=a(s)e_r(\theta)+z(s)e_z,\qquad
 a'=\cos\beta,\quad z'=\sin\beta,\quad a>0.
\]

取

\[
 t=a'e_r+z'e_z,\qquad n=-z'e_r+a'e_z.
\]

因此 \(t_s=\beta'n\)、\(n_s=-\beta't\)，在沿 +z 方向的圆柱上该法向指向轴线。考虑一个实余弦模（另一角相位完全相同）

\[
 Y=U(s)\cos(m\theta)t+V(s)\sin(m\theta)e_\theta
       +W(s)\cos(m\theta)n,\qquad m\ge2.
\]

直接令一阶度量变分为零，得到

\[
 \boxed{U'=\beta'W},\qquad
 \boxed{aV'=mU+a'V},\qquad
 \boxed{a'U+mV-z'W=0}. \tag{1}
\]

最后一个是 \(\delta G=0\)，第二个是 \(\delta F=0\)，没有在 z′=0 处除法。只在 z′≠0 的开段，消去 V 后可写为

\[
 \boxed{V=(-a'U+z'W)/m},\tag{2}
\]

\[
 \boxed{
 W'=\frac{a'}aW+
 \frac{m^2-a'^2-a\beta'z'}{a z'}U
 =\frac{a'}aW+\frac{m^2-a'^2}{a}\frac U{z'}-\beta'U.
 }\tag{3}
\]

例如 m=1 的水平刚体平移具有 U=a′、V=−1、W=−z′，与这些符号相符；本结果的固定圆领障碍只对 m≥2 使用。

若端点 z′≠0，(1)、(3) 是普通线性系统，U=W=0 的端值由通常的唯一性得到零解。平端 z′=0 必须另作以下论证，不能直接调用这个普通端点结论。

## 2. 单调平端的严格 trace 引理

**假设。** 在 \([L-h,L]\) 上，\(a,\beta\in C^1\)、\(a\ge a_*>0\)，有 a′=cosβ。设

\[
 a(L)=R>0,\quad \beta(L)=\beta_0\in\pi\mathbb Z,
 \quad c=\cos\beta_0\in\{1,-1\}.
\]

β 在这个末段单调，且 \(\beta(s)\ne\beta_0\)、sinβ(s)≠0 对 s<L 成立。U、W 在闭末段为 C1，并在内部满足 (1)、(3)。单调可以减弱为下面所用的尾变差比值有界。

**引理 1。** 对 m≥2，端 trace 必须满足

\[
 \boxed{U(L)=V(L)=0},\qquad
 \boxed{W_s(L)=\frac{c m^2}{R}W(L)}.\tag{4}
\]

**证明。** 将 (3) 乘以 az′，再令 s↑L。a、β′、U、W、W′ 有界，而 z′→0，得到

\[
 (m^2-1)U(L)=0.
\]

故 U(L)=0，(2) 的连续极限又给 V(L)=0。记 δ(s)=β(s)−β0，w0=W(L)。积分第一式得

\[
 U(s)=-\int_s^L\beta'(t)W(t)\,dt
      =\delta(s)w_0-\int_s^L\beta'(t)(W(t)-w_0)\,dt.
\]

由于 β 单调，\(\int_s^L|\beta'|=|\delta(s)|\)，因此

\[
 \left|\frac{U(s)}{\delta(s)}-w_0\right|
 \le\sup_{t\in[s,L]}|W(t)-w_0|\longrightarrow0.
\]

再由 sinβ/δ→c，严格得到

\[
 \frac{U(s)}{z'(s)}\longrightarrow c w_0.
\]

将这些极限代入 (3) 的最后一个表达式，β′U→0，其余项有有限极限：

\[
 W'(s)\longrightarrow \frac cR w_0+
    \frac{m^2-1}{R}c w_0=\frac{cm^2}{R}w_0.
\]

这就是 (4)，并非对奇异系数作形式代入。若只预设 W′ 在内部有界而 W 连续，右端计算仍给出导数极限；由积分平均同样得到相同的单侧端导数。□

## 3. 固定圆领的零 trace 只能是零线性解

**引理 2。** 在引理 1 的假设下，若 W(L)=0，则 U=V=W 在一个左端邻域恒为零，并在 z′≠0 的整个相连参考段上恒为零。

**证明。** 缩小 h，使 \(|\delta|\le\pi/2\)。单调性及 \(|\delta|/|\sin\delta|\le2\) 给出

\[
 \int_s^L|\beta'|\le2|z'(s)|.
\]

记 \(M(s)=\sup_{t\in[s,L]}|W(t)|\)。由 U(L)=0 和 U′=β′W，

\[
 |U(s)/z'(s)|\le2M(s),\qquad |U(s)|\le2M(s).
\]

设 B=sup|β′|，利用 |a′|≤1，将其代入 (3)，得到

\[
 |W'(s)|\le C_m M(s),\qquad
 C_m=\frac{2m^2+3}{a_*}+2B<\infty.
\]

因为 W(L)=0，对任何 v∈[s,L] 有

\[
 |W(v)|\le\int_v^L C_m M(t)\,dt
 \le C_m(L-s)M(s).
\]

取上确界，得 \(M(s)\le C_m(L-s)M(s)\)。当 \(C_m(L-s)<1\) 时只能 M(s)=0，继而 U=V=0。离开该小邻域后，普通线性 ODE 唯一性将零解延续到整个 z′≠0 的相连段。□

因此在这种参考上，把 m≥2 的端口位移和二 jet 全部固定为圆领数据，并不存在可通过调整 β 参数找到的局部线性 kernel；事实上零位移已经足够，额外二 jet 条件不是这一障碍的原因。

若中间只有有限个孤立回折零点，每个零点两侧都满足同类的局部尾变差条件，则可逐段将零解延续过去。这里的结论不覆盖平面开区间中的任意自由法向场，也不覆盖在端点积聚的无限零点。

## 4. 有限阶平端的二阶 trace

为了匹配实际二 jet，再设 x=L−s，且

\[
 \beta(s)-\beta_0=B_0x^p+O(x^{p+1}),\quad
 \beta'(s)=-pB_0x^{p-1}+O(x^p),\quad
 B_0\ne0,\quad p>1,
\]

并假设 W 有单侧二阶展开。写 \(w_j=\partial_s^jW(L)\)。积分分部给出

\[
 \frac U\delta
 =W(s)+\frac{\int_s^L\delta(t)W'(t)\,dt}{\delta(s)}
 =w_0-\frac p{p+1}w_1x+o(x).
\]

又有 a=R−cx+o(x)、a′=c+o(x)、β′U=o(x)。将这些代入 (3) 并比较常数与一次项，得到

\[
 w_1=\frac{cm^2}{R}w_0,\qquad
 \boxed{w_2=\frac p{p+1}\frac{m^2(m^2-1)}{R^2}w_0}.\tag{5}
\]

对公开脚本的 S5 平端，p=3，系数为 3/4。若 p>2 且参考相应导数存在，U、V 的端部二 jet 都趋于零，法向的 w0、w1、w2 则受 (4)、(5) 约束。无限阶平尾不能直接把 p 当作一个有限数套用 (5)；(4) 和引理 2 在单调假设下依然有效。

将第一阶条件对 m≥2 分量重组，可写为

\[
 W_s(L,\theta)=-\frac cR W_{\theta\theta}(L,\theta).
\]

以端部几何半径 r 为变量，\(\partial_s=c\partial_r\)，故对这些分量，与 c 的符号无关地变成

\[
 \boxed{R W_r+W_{\theta\theta}=0\quad\text{在 }r=R}.\tag{6}
\]

对于一般 W，严格要求的是 (6) 左边的 m≥2 Fourier 投影为零；本引理不以此约束允许设计的 m0 度量变分。对于 S5，m≥2 二阶角形式为 \(W_{ss}=\frac{3}{4R^2}(W_{\theta\theta\theta\theta}+W_{\theta\theta})\)。单独给任意 W(θ) 并不足以给出可接的完整 trace。

## 5. R128 的允许弯平尾在平基点的 trace

公开 R128 型平坦尾为

\[
 P(r,\theta)=(r\cos\theta,Y(r\sin\theta),Z_c-H(r\sin\theta)),
\]

\[
 Y'(y)=\cos\alpha(y),\qquad H'(y)=\sin\alpha(y),
 \qquad \alpha=0\text{ 在 }|y|\le c_0.
\]

考虑准确尾族的小方向 \(\alpha=\epsilon f(y)+o(\epsilon)\)。在未弯曲平基点，\(\delta Y=0\)，\(\delta H=F(y)\)，其中 \(F'=f\)、F(0)=0。沿向内经线 s=R−r，参考法向 n=−ez，所以该方向只有法向分量

\[
 W(r,\theta)=F(r\sin\theta),\qquad U=V=0.
\]

其第一、二径向导数为

\[
 W_s=-\sin\theta f(y),\qquad
 W_{ss}=\sin^2\theta f'(y),\qquad y=r\sin\theta.
\]

然而在 r=R，(6) 的左边准确化为

\[
 R W_r+W_{\theta\theta}
 =(R^2-y^2)f'(y).\tag{7}
\]

如果这种尾要线性匹配引理 1 的旋转曲面末端，(7) 的 m≥2 投影必须为零。这个条件已足以推出整个 (7) 为零，**不必对 m0 度量设计额外设限**：否则 (7) 只能是 A+B sinθ+C cosθ；它作为 sinθ 的函数满足 θ↦π−θ 对称，故 C=0；又因 f′ 有界，它在 θ=π/2、3π/2 均为零，故 A+B=A−B=0。因此 f′(y)=0 对所有 |y|<R 成立。由于内开平条带上 f=0，得到 f=0、F=0 在整个 |y|≤R 上。

**推论。** 从“旋转连接面 + 未弯 R128 平尾”这个基点出发，R128 的小弯幅参数不能提供非平凡、满足该末端相容性的 m≥2 边界方向。这解释为何放开少数 tail amplitude 未必修复旧椭圆小幅 continuation 的线性不相容。

此推论没有否定 R128 本身：它仍是准确的有限弯曲平坦尾。它否定的是上述特定旋转基点附近的线性拼接方向；从强非旋转核心与非零有限尾数据联合设计，仍是不同问题。

## 6. 自由帽的刚体位姿只提供 m0、m1

在平面圆盘 \((r\cos\theta,r\sin\theta,z_0)\) 上，刚体无穷小运动 \(T+\Omega\times X\) 的法向分量为

\[
 W=c\{T_z+r(\Omega_x\sin\theta-\Omega_y\cos\theta)\}.
\]

它只包含 m=0 的法向平移和 m=1 的倾斜。水平平移在切向分量中也是 m=1，绕轴旋转为切向 m=0。因而自由帽的六个刚体位姿参数不能补偿 m≥2 的上述 trace 残差。

将一个仿射法向函数加到 R128 的 W 上，也不会改变 (7) 的残差，因为仿射函数自身满足 (6)。固定握持若最终锁定这些刚体参数，应在完整构造中另外执行；本节没有把自由帽位姿当作已固定握持。

## 7. 无限振荡末段为什么不在当前证明范围内

引理 2 真正用到的是

\[
 \sup_{s\uparrow L}
 \frac{\operatorname{Var}_{[s,L]}\beta}{|\sin\beta(s)|}<\infty.\tag{8}
\]

单调末段自动满足它。有限阶解析平端也在足够小的末段单调。无限振荡可以破坏 (8)，即使参考仍为 C∞、曲率有界、β−β0 在端点平坦到无限阶。

例如对 x=L−s>0 定义

\[
 \delta(x)=e^{-1/x^2}\bigl(2+\sin(1/x^4)\bigr),\qquad
 \beta=\beta_0+\delta,
\]

并令 δ(0)=0。它为正且 C∞ 平坦；故邻域内 sinβ 没有额外零点，但 β 不单调。置 u=1/x²，则尾变差包含

\[
 \int_u^\infty e^{-v}
 |2v\cos(v^2)-(2+\sin(v^2))|\,dv.
\]

只在 [u,u+1] 积分，并利用大 u 时 \(|\cos(v^2)|\) 在该区间包含越来越多完整周期，即得它至少为常数乘 \(u e^{-u}\)；而 \(|\sin\beta|\le\delta\le3e^{-u}\)。因此 (8) 的比值无界。

这个例子仅证明当前变差估计不再适用，**不证明存在非零 kernel**。其他唯一性估计仍可能成立。若改用带无限零点的振荡 β，还需处理积聚特征圈的无限匹配条件；不能因有限回折的证明不覆盖它，就宣布得到了可用的分岔机制。没有为这些未建立目标的情形运行搜索。

## 8. 对当前公开参考与计算的直接影响

`scripts/core_to_tail_bvp.py` 中的 `UnitMeridian` 采用有限次多项式 β，并指定末端 β=π、β′=β″=0；`FoldedMeridian`、`InwardMeridian` 的末次 S5 过渡单调到 β=π，随后是准确平段。`scripts/folded_collar_search.py` 的有限平滑过渡同样没有由“平端奇异”自动产生的固定圆领 kernel。

对这些旋转参考，应停止搜索已经由引理 2 排除的 m≥2 固定圆领零 trace eigenkernel。若要作允许非零 trace 的传输检测，必须先明确边界族，并使用 (4)、必要时 (5) 的完整条件；R128 的平基点子族已由 (7) 排除，不能把任意非零 W(θ) 当作该尾族的真实可用参数。

本题新多模 ψ-warp 准确核心远离旋转参考，且可随连接带共同设计。R17 不适用于把它直接判为不存在；其实际 BVP、闭帽及几何认证应继续推进。

### 公开来源与本地接口

- `topics/visible-flexible-closed-surface/results/R128-exact-flat-developable-tail-with-fixed-collar.md`：准确平坦尾机制；本题已有 `notes/source-audit-20261114.md` 与 `notes/collar-control-20261114.md` 记录其公式及完整端口。
- `scripts/core_to_tail_bvp.py`：`UnitMeridian`、`FoldedMeridian`、`InwardMeridian` 的实际 β 参考。
- `notes/warped-ruled-controls-20261114.md`、`scripts/warped_ruled_core_controls.py`：不受本旋转基点线性结论直接排除的强非旋转核心控制接口。

本结果为独立解析推导；未执行新的研究扫描，未将有限数值残差当作存在或不存在证明。
