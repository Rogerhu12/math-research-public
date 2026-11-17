# R36：raw m3 核的真积分、反函数误差与固定 atlas 的 metric 转移

**状态：已证明，范围如下。** 本文证明一个可执行的局部真积分包围公式、完整 raw 核的解析全角 $\rho$ 界、15 个指定实际材料点的真反函数与曲线 jets 误差界，以及将统一角余项接到 R31 固定 atlas 的扰动公式。后三节的 metric 转移是明确给定余项后的引理，**不声称当前 raw 候选已通过连续 metric 门、已经闭合，或已完成固定 $g$ 加密**。

本条没有重新求解 BVP，没有重跑 R32–R34，也没有对当前不合格 metric 候选铺全域几何盒。

## 1. 唯一物理核、来源及本条数值结论

实际输入为 raw 路径的 `beta4625-q040-raw-lam002/seed.json.gz`，SHA-256 为

`67bf84c2f485e500b92378dec67e2186ee0a874ab2f8d763a2a0855edc263607`。

它的类别必须为 `exact_m3_raw_local_circle_integral_lift`，控制路径为 `raw-mean-primary-compact-v1`。生产 reader 对原 checkpoint 的全部相关 source 哈希、完整控制参数、$M=J=8$、$q$、$\lambda$、各宽度和 exact lift 设置作一致性检查；不加载 canonical 控制基。

本条真积分对象采用原数学定义：

$$
n=3,\quad \eta=0,\quad L=\pi/3,\quad T=2L,\quad
a=21/100,\quad b_p=2/25,\quad b_c=4/25.
$$

这里 $b_p$ 是主核过渡宽，$b_c$ 是控制过渡宽，二者不可混用。反射中心是精确 $\pi/3$。$q$、$\lambda$ 和完整物理控制 $c_2,\ldots,c_8$ 是 checkpoint 浮点数代表的精确二进制有理数。其中

$$
q=\frac{5764607523034235}{144115188075855872},\qquad
\lambda=\frac{5764607523034235}{288230376151711744}.
$$

每个 $c_j$ 由原 `parameters[1:] * central_correction_scales` 的 binary64 乘积恢复，不把未缩放参数当成物理控制，不省略首个控制。它们的精确分数见执行记录。高精度定义控制矩时，源库已使用 `mp.mpf(str(width))`；因此上述十进制宽度是它的原定义。Gauss 积分、binary64 的 $\pi/3$ 和 cutoff 求值、数值求逆均只是原对象的求值近似，其误差没有被忽略或改为新物理输入。

**全角解析结论：** 对此完整 raw 核，

$$
\boxed{0.6611264617<\rho(\phi)<1.3386894072\quad(\phi\in\mathbb R),}
\tag{1}
$$

并且

$$
|\rho_\phi|<1.79256455,\qquad
|\rho_{\phi\phi}|<40.705614.
\tag{2}
$$

第三导数在 cutoff 分片内部满足 $|\rho_{\phi\phi\phi}|<4072.123312$；这最后一个界按分片及端点单侧极限理解。

**有限点结论：** 对第 6 节精确指定的 15 个 binary64 材料参数，以原 source 给出的近似法向角为起点，真弧长残差及真法向角误差分别小于

$$
1.590\cdot10^{-14},\qquad 2.404\cdot10^{-14}.
\tag{3}
$$

真曲线及其前三个材料导数相对原 source 输出的欧氏误差分别严格小于

$$
\boxed{3.192\cdot10^{-14},\quad4.816\cdot10^{-14},\quad
2.700\cdot10^{-13},\quad1.021\cdot10^{-11}.}
\tag{4}
$$

(1)–(2) 是全角结论；(3)–(4) **只对所列有限点成立**，不得作为连续角余项。

## 2. cutoff 的部分积分包围

令 $\chi_{a,b}(x)$ 为偶函数，在 $|x|\le a$ 等于 1，在 $|x|\ge a+b$ 等于 0，过渡段为

$$
P(t)=1-126t^5+420t^6-540t^7+315t^8-70t^9,
\quad t=(|x|-a)/b.
$$

$P'(t)=-630t^4(1-t)^4$，所以 $0\le P\le1$。对 $x=a+b\tau$、$0\le\tau\le1$，写

$$
I_k(x)=\int_0^x\chi_{a,b}(s)e^{iks}\,ds
=\int_0^a e^{iks}\,ds+b e^{ika}\int_0^\tau P(t)e^{ikbt}\,dt.
$$

将 $P(t)=\sum_{j=0}^9p_jt^j$ 和指数的 $R$ 次 Taylor 多项式相乘后精确积分，得到

$$
Q_{k,R}(\tau)=
\sum_{r=0}^R\frac{(ikb)^r}{r!}
\sum_{j=0}^9\frac{p_j\tau^{r+j+1}}{r+j+1}.
\tag{5}
$$

因为实参数指数的所有导数模长为 1，Taylor 积分余项和 $0\le P\le1$ 给出

$$
\left|I_k(x)-\int_0^a e^{iks}ds-b e^{ika}Q_{k,R}(\tau)\right|
\le \frac{b|kb|^{R+1}\tau^{R+2}}{(R+2)!}.
\tag{6}
$$

乘 $e^{ika}$ 不放大复模；因此将右端分别加到实部和虚部的正负方向，便得到两个实区间。$k=0$ 的公式也成立，此时余项为 0。$x\le a$ 使用普通正弦/余弦原函数，$x\ge a+b$ 使用已经积分完的常数。跨越分片点的输入区间先切开后取包围；负半轴分别使用余弦原函数的奇性和正弦原函数的偶性。

脚本 `integral_core_intervals.py` 实现 (5)–(6)，本次 $R=64$。所有算术不等式使用 `Fraction`，每一步向外压缩到 80 位十进制有理数。正弦、余弦的 200 次 Taylor 余项及 $\pi$ 的 Machin 包围沿用 R33 的通用算术函数；这只复用算术，不复用其障碍结论。输入区间上的多项式 Horner 值、Taylor 余项上界、奇偶与分片包围均包含真实值，因此由运算次数归纳，输出包围有效。

## 3. 真支撑函数与弧长原函数

设局部法向角 $x=\phi-L-kT\in[-L,L]$。主核的真实单位曲率半径扰动为

$$
u_p(x)=8\cos3x+\lambda\{\beta+\chi_{a,b_p}(x)
                     [8-\beta-8\cos3x]\}.
\tag{7}
$$

$\beta$ 按均值为零的原积分定义确定。R32 已证明，对且仅对这里相同的 $a=.21,b_p=.08,n=3,\eta=0$，

$$
-0.2301638780908070253001170066934325491224
\le\beta\le
-0.2301638780908070253001170066934325491223,
\tag{8}
$$

以及真实圆心模长除以 $q$ 的常数 $C_*$ 满足

$$
9.0518983695329193804686089826045741030176
\le C_*\le
9.0518983695329193804686089826045741030177.
\tag{9}
$$

**本条只读复用 (8)–(9)。** 改主核宽度、$n$ 或 $\eta$ 时不得继续使用它们。$\lambda$ 可以变化，是因为 (7) 对 $\lambda$ 线性；没有把 $\lambda=.02$ 当成已经有圆弧。

令

$$
C(x)=\int_0^x\chi_{a,b_p}(s)[8-\beta-8\cos3s]\cos s\,ds,
$$
$$
S(x)=\int_0^x\chi_{a,b_p}(s)[8-\beta-8\cos3s]\sin s\,ds.
$$

利用积化和差，$C,S$ 只需要第 2 节在频率 $1,2,4$ 的原函数：

$$
C=(8-\beta)I^c_1-4I^c_2-4I^c_4,\qquad
S=(8-\beta)I^s_1+4I^s_2-4I^s_4.
$$

则主核支撑扰动为

$$
v=-\cos3x+\lambda w,
\quad w=\beta+(9-C_*-\beta-S)\cos x+C\sin x,
\tag{10}
$$
$$
w'=-(9-C_*-\beta-S)\sin x+C\cos x.
$$

直接微分得 $v+v''=u_p$；R32 的 Green 常数给出 $T$ 周期的唯一支撑解。$D^2+1$ 在 $T=2\pi/3$ 周期函数上没有核，故这也是原 source 用 $(R_T-I)$ 方程选定旋转中心的同一数学支撑函数。这里没有把局部的 $h-R$ 误认为真实圆心。

raw 控制写成

$$
b(x)=(1-\lambda)\sum_{j=2}^M c_j(-1)^j\cos3jx
 +\lambda W_c(x)\sum_{k=0}^M D_k(-1)^k\cos3kx,
\tag{11}
$$

其中 $W_c=1-\chi_{a,b_c}$，$D_k=\sum_{j=2}^M c_jH_{j,k}$。每行 $H_j$ 的第 $j$ 个高频系数为 1，其余高频系数为 0；两个低系数由 $W_c$ 加权均值和主频为零的 **$2\times2$ 矩投影**唯一确定。未对高矩作 canonical 逆矩阵变换。

原 raw `moment_interval_bounds.py` 用有理三角积分包围真实矩阵 $B$，取任意有理近似逆 $R$，严格核实 $\|I-RB\|_\infty=\epsilon<1$，再用

$$
\|B^{-1}-R\|_\infty\le\frac{\epsilon}{1-\epsilon}\|R\|_\infty
$$

包住 $H$。高精度浮点求逆只是产生候选 $R$，不承担该不等式的正确性。本文直接使用实际库生成的这些 Fraction 系数区间，并再次向外取整；source 的浮点 $H$ 不作为真系数。

令 $B_c(x)=\int_0^x b(s)ds$，由 (11) 可使用普通余弦原函数与第 2 节控制 cutoff 的部分积分求出。于是

$$
h=1+qv+b,\quad h'=qv'+b',\quad
\Gamma(\phi)=h\,n(\phi)+h'\,t(\phi),
\tag{12}
$$

其中 $n=(\cos\phi,\sin\phi)$、$t=(-\sin\phi,\cos\phi)$。真实材料弧长为

$$
u(\phi)=\phi+qU_p(x)+B_c(x)+b'(x),
\tag{13}
$$
$$
U_p(x)=\frac83\sin3x+
\lambda\{\beta x+(8-\beta)I^c_0(x)-8I^c_3(x)\}.
$$

均值约束和反射对称给出 $U_p(\pm L)=B_c(\pm L)=b'(\pm L)=0$，故 (13) 确实满足 $u(0)=0$；没有引入逐层重调的弧长起点。微分 (12)–(13) 得

$$
\Gamma_\phi=\rho t,\quad u_\phi=\rho,
\qquad \rho=1+q u_p+b+b''.
\tag{14}
$$

## 4. 完整控制的全角解析界

设 $S_r$ 是单位 cutoff 第 $r$ 导数绝对值的有理上界，$S_0=1$。脚本把其导数多项式在 $[0,1]$ 分成 64 个有理区间，在每个区间精确转 Bernstein 系数，取系数绝对值最大值；Bernstein 基非负且和为 1，故此上界覆盖整个区间，并非节点采样。

定义

$$
A_r=\sum_{j=2}^M|c_j|(3j)^r,\qquad
D_r=\sum_{k=0}^M|D_k|(3k)^r,
$$

在 $r=0$ 使用 $0^0=1$，$|D_k|$ 取其区间绝对值上界。Leibniz 公式给出

$$
\|b^{(r)}\|_\infty\le B_r:=(1-\lambda)A_r+
\lambda\sum_{\ell=0}^r{r\choose\ell}
\frac{S_\ell}{b_c^\ell}D_{r-\ell},\quad0\le r\le5.
\tag{15}
$$

第 5 阶按分片及单侧值理解。由于 $\beta<0$，(7) 是纯余弦与 mean-one 圆化主核的线性混合，故

$$
-8+\lambda\beta\le u_p\le8.
$$

所以

$$
1-8q+q\lambda\beta_--B_0-B_2\le\rho
\le1+8q+B_0+B_2.
\tag{16}
$$

将 $u_p^{(r)}$ 中无 cutoff 导数的项合并成 $(1-\lambda\chi)$ 乘余弦导数，$r\ge1$ 时得到

$$
\|u_p^{(r)}\|_\infty\le8\,3^r+
\lambda\sum_{\ell=1}^r{r\choose\ell}\frac{S_\ell}{b_p^\ell}
\begin{cases}16-\beta_-,&\ell=r,\\8\,3^{r-\ell},&\ell<r.\end{cases}
\tag{17}
$$

因此 $\|\rho^{(r)}\|_\infty\le q\|u_p^{(r)}\|_\infty+B_r+B_{r+2}$。把 checkpoint 的全部七个精确控制、实际 raw 矩投影区间和 (8) 代入 (15)–(17)，经有理运算得到

$$
\rho\ge0.661126461738056479146375847219909764698604968,
$$
$$
\rho\le1.33868940715947087522571806206793254190270053,
$$

以及 (2) 和上述第三导数界，证明 (1)–(2)。这些下界没有使用 source 的浮点 positivity guard、Gauss 求积或浮点最大值。

## 5. 真反函数与材料 jets 的转移引理

记 $m>0$ 为严格的全角 $\rho$ 下界，$R_1,R_2$ 为 $|\rho_\phi|,|\rho_{\phi\phi}|$ 上界。给定材料参数 $u_0$ 和任意近似法向角 $\widetilde\phi$，第 2–3 节的包围若给出

$$
|u(\widetilde\phi)-u_0|\le\varepsilon_u,
$$

则由单调性和中值定理，真实反函数满足

$$
|\phi(u_0)-\widetilde\phi|\le\varepsilon_u/m.
\tag{18}
$$

令小写 $\gamma$ 表示真材料参数曲线。由 (14)，

$$
\gamma'=t,\quad\gamma''=-n/\rho,\quad
\gamma'''=-t/\rho^2+n\rho_\phi/\rho^3,
\tag{19}
$$
$$
\gamma''''=n/\rho^3+3t\rho_\phi/\rho^4
 +n\rho_{\phi\phi}/\rho^4-3n\rho_\phi^2/\rho^5.
\tag{20}
$$

因而从 $u(\widetilde\phi)$ 移到 $u_0$，位置、一阶、二阶、三阶材料导数的欧氏变化分别不超过

$$
\varepsilon_u,\quad\frac{\varepsilon_u}{m},\quad
\varepsilon_u\left(\frac1{m^2}+\frac{R_1}{m^3}\right),
\tag{21}
$$
$$
\varepsilon_u\left(\frac1{m^3}+\frac{3R_1}{m^4}
 +\frac{R_2}{m^4}+\frac{3R_1^2}{m^5}\right).
\tag{22}
$$

证明是对 (19)–(20) 沿真实材料弧积分；位置使用单位速率，所以不需要再乘 $\rho_{\max}/m$。$\rho$ 为 $C^2$ 且严格正，所需导数在 cutoff 接口连续，跨接口积分也有效。对 (12)、(19) 在 $\widetilde\phi$ 的有理区间分别加上 (21)–(22)，即可包住 $u_0$ 处的真实值。该证明不假设原数值反函数已经满足它自己的停止门槛。

## 6. 15 点真实输入执行

脚本 `audit_true_integral_core_points.py` 使用上述同一 checkpoint。它以原 source 的

$$
\phi\in\{0,T\}\cup
\{L+d:d=-.37,-.29,-.21,0,.21,.29,.37\}
$$

求得材料值，再并入

$$
\theta=\psi-e_{\rm ref}\sin3\psi/3,
\qquad\psi=2\pi j/12,\quad j=1,3,5,7,9,11.
$$

本段的 source 运算仅产生待审计的 **binary64 材料输入**；它们既不是积分包围，也不是极值证据。去重后为 15 个点。source 再给出各点的近似法向角；随后全部真原函数、真实反函数转移和 jets 包围由第 2–5 节执行。

每个原 source 输出视为一个精确的 binary64 数字。以坐标误差绝对值之和上界欧氏范数，得到 (3)–(4)。原 source 的第三材料导数通过其实际 $\rho_\phi$ 和 (19) 计算；不把名义 `coefficients/frequencies` 当作完整核的 Fourier 系数。

本次正常 `exit_code=0`，终端会话 `20813`，耗时约 22.61 秒。完整可再生输出的 SHA-256 为

`f1e02ee99223b78b1fbf1daea6253bea5f0b8a37afa90bfe13df276a607ebb93`。

输出包含各有限点的详细区间；依根规矩第 15 条不提交该数据，只提交脚本、紧凑最大值和哈希。所列点之外的 source 反函数/求值误差，本文没有给出统一界。

## 7. 固定 atlas 及同一角余项的合并

R31 的 `TruePrefix` 只依赖原物理 profile 输入、真实桥积分、物理 $r_{\rm cut},w_{\rm cut}$ 和一个冻结的材料长度锚点。对本次新物理输入，锚点取本 checkpoint 的

$$
L_{\rm bin}=1.3603133321372538.
$$

由原 `physical_tail_parameters` 的 $r_{\rm cut}=.3,w_{\rm cut}=.08$ 和本次冻结 $\delta$ 计算真实 $L_*$，继续用 R31 的固定坐标映射

$$
\sigma(s)=(L_*/L_{\rm bin})s+
\text{固定的零端值 cut Hermite 修正}.
\tag{23}
$$

它把同一个物理 $g$ 拉回共同材料区间，不调整物理桥长或给每个加密层重选 $g$。$L_{\rm bin}$ 一经作为本同 $g$ 序列的锚点，后续 $M$/径向加密均使用同一锚点。本次新输入得到 $L_*/L_{\rm bin}-1$ 在 $1.76881624908793\cdot10^{-16}$ 与 $1.7688162491553687\cdot10^{-16}$ 之间；坐标修正的值和一阶导误差分别小于 $3.633\cdot10^{-18}$、$4.541\cdot10^{-16}$。

这些是 **新输入的坐标描述量**；没有把旧 R31 的数值 metric 上界搬来。当前 raw 导出还没有接实际尾部及施加末端 matching lift，故 (23) 也不宣称当前图的实际 cut 二阶缝已匹配；未来 matching lift 必须固定来源、实际施加并支付误差。

下面说明可复用的代数接口。设已导出的图在中心条带为

$$
X=C+fH+\sum_{j=0}^2 h_j\{J_j-C_j(0)-f_j(0)H\},
\tag{24}
$$

$C$ 是共同二阶 jets 的有限 Cartesian 图，$f$ 是已共享化的标量 lift，$h_j$ 是中心 Hermite 基，$H=\gamma(\theta_r)-E_r-qV_{\rm in}$。此 flat 入口有 $f_j(0)=(1,0,0)$，且

$$
J_0=\gamma(\theta_c),\quad J_1=e_z,\quad
J_2=b_\psi\gamma'(\theta_c),
$$

这里 $b_\psi=-E''(0)\sin3\psi/3$ 是一个已冻结角函数，非支撑控制 $b(x)$。$\theta_r=\psi-e_{\rm ref}\sin3\psi/3$，$\theta_c=\psi-E(0)\sin3\psi/3$。

取任意有限三角近似 $G_N,T_N,E_N$，分别近似 $\gamma(\theta_r),\gamma'(\theta_c),E_r$，记其真实余项为 $R_G,R_T,R_E$。令 $P$ 为把这些有限近似代入 (24)，并以 $G_N$ 代替 $J_0$ 后的有限主部。**精确代数恒等式**为

$$
X-P=fR_G-(f-h_0)R_E+h_0\Delta\gamma+h_2 b_\psi R_T,
\tag{25}
$$

其中 $\Delta\gamma=\gamma(\theta_c)-\gamma(\theta_r)$。由于同一个 $\gamma(\theta_r)$ 同时出现在 $H$ 和中心修复中，必须先合并成 $fR_G$；把二者独立取绝对值会产生不必要的中心条带导数放大。

对 (25) 可直接求 $s,\psi$ 导数。若 $d=|E(0)-e_{\rm ref}|$，单位速率及 $\|\gamma''\|\le1/m$ 还给出

$$
|\Delta\gamma|\le d/3,\qquad
|\partial_\psi\Delta\gamma|\le d+(1+|e_{\rm ref}|)d/(3m).
\tag{26}
$$

所以同一 source 角定义产生的 ulp 差有显式预算，不需要把两个入口角默认为精确相同。有限主部 $P$ 仍是共同径向多项式乘有限 Laurent 角函数；扩大频带并显式保持三重协变后可用 R31 的分子与 Bernstein 代数。必须重新计算此新主部的界。

## 8. 归一化微分的 metric 扰动引理与尚缺项

在共同物理 atlas 中

$$
g=\sigma'(s)^2ds^2+a(\sigma(s))^2d\theta^2,\qquad
\theta=\theta(s,\psi),\quad\theta_\psi>0.
$$

设有限主部 $P$ 相对同一真实 $g$ 的 metric 算子误差不超过 $\eta_0$。令 $Z=X-P$，若全域统一界给出

$$
\left|\frac{Z_s-(\theta_s/\theta_\psi)Z_\psi}{\sigma'}\right|
+\left|\frac{Z_\psi}{a(\sigma)\theta_\psi}\right|\le\varepsilon,
\tag{27}
$$

则完整图满足

$$
\boxed{\eta_X\le\eta_0+2\sqrt{1+\eta_0}\,\varepsilon+\varepsilon^2
\le\eta_0+2(1+\eta_0)\varepsilon+\varepsilon^2.}
\tag{28}
$$

证明：把 $P$ 的两个归一化微分列写成矩阵 $A$，把 (27) 的两列写成 $B$。假设给出 $\|A^TA-I\|\le\eta_0$，所以 $\|A\|\le\sqrt{1+\eta_0}$；(27) 给出 $\|B\|\le\varepsilon$。展开 $(A+B)^T(A+B)-I$ 并用三角不等式即得。第二个界只用有理运算即可支付。

从本条局部原函数到 (27) 尚需**统一角余项**。例如，(19)–(20) 给出的真实导数界和每个中心点的真积分包围，可与 Taylor 的积分余项组成整个角区间上的包围；跨 cutoff 接口要保留分片的真实定义。也可对有限三角主部的误差直接作区间估计。15 点的最大误差本身不能替代这一步。

因此当前明确尚缺：统一的 $R_G,R_G',R_T,R_T',R_E,R_E'$ 界；此新主部在全部径向区间相对真 $g$ 的 metric 界；实际尾部与共同 cut lift；全闭曲面的几何和同 $g$ 加密。本文完成的是可复用的真实积分/反函数及误差转移接口，没有扩大已经证明的完整候选范围。

## 9. 复现来源

本条新增来源为 `scripts/resume_closed/integral_core_intervals.py`、`audit_true_integral_core_points.py`；命令、完整控制精确分数、来源哈希、退出状态、紧凑界和输出哈希见 `true_integral_core_points_execution.json`。

复用来源分别为 R32 的主核常数证明、R33 的通用有理算术、原 raw 库的 $2\times2$ 矩投影包围、当前严格分派 reader，以及 R31 的 `prefix_true_profile.py`。这些分别承担不同部分的定义和界，不能互相替代。
