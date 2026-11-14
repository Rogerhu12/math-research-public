# 水平核心的有限平坦领：完整独立纸面审查

**审查结论：接受作者冻结稿所陈述的两项局部存在定理及完整环带的非全等结论。**  
审查人：`/root/tail_review_continued_2`，2026-11-09。本审查未参与本稿的构造或证明。没有运行新的 PDE、BVP、DN、RK、几何轨迹或纯数学检查程序；当前可用的 JavaScript 隔离运行时仅用于文本封存、字节数和 SHA-256。正文的接受依据是完整纸面推导，不能记成数值轨迹或程序独跑。

接受范围为：实际解析水平凸核心的一个共同长度、共同参数域的有限族，分别经 **全 jet 平入口** 或 **精确保留 R38 四阶开内领的 C² 入口**，接到有限正宽的平坦仿射出口；实际位置全圈闭合，所得整个有边环带嵌入并有统一正 reach，振幅参数不同的完整像在全欧氏群 \(E(3)\) 下不全等。两个入口使用不同的共同度量，不能混为同一候选的加密，也不能相互移交接合 jet。

本文不支付固定开握持区、闭曲面、README 的可见形变幅度或规范化 reach、R43 出口接合、主候选 G5 或其余完成门。

## 1. 冻结输入与实际审查范围

主稿：

- 路径：`topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-horizontal-core-finite-flat-collar-v1.md`。
- 固定提交：`eb255a1a67a1e0ef6268a9dd31d9adb2b8e23493`。
- Git blob：`7b008db5aa71587c32ef90c6d2163964b0787f7e`。
- UTF-8 长度：15,050 bytes。
- SHA-256：`cbfe0ec65096c409880b5c1a6a3f4f88bbf6ffab593a14a175c47b3e36d03bb8`。
- [不可变全文](https://github.com/Rogerhu12/math-research/blob/eb255a1a67a1e0ef6268a9dd31d9adb2b8e23493/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-horizontal-core-finite-flat-collar-v1.md)。

全文核对的既有 R38：

- 同一提交下 `results/R38-ck-local-exact-isometric-collar.md`。
- Git blob：`203c3e8d707f6c332550546e16e9ef8ed1ae5f17`。
- UTF-8 长度：20,176 bytes。
- SHA-256：`a43ee6a726406570d09912225dea0c2e102c08c3f84ed583b9701345a0a113a1`。
- [不可变全文](https://github.com/Rogerhu12/math-research/blob/eb255a1a67a1e0ef6268a9dd31d9adb2b8e23493/topics/visible-flexible-closed-surface/results/R38-ck-local-exact-isometric-collar.md)。

解析尺度方法的先前完整独审为：

- [正 C epicycle 有限平坦领独审](https://github.com/Rogerhu12/math-research/blob/e927f688421290880733e8de0ddc2d017ef8c574/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-positive-epicycle-finite-flat-collar-v1.md)。
- 那次独立 63 项有理门属于其自己的固定源码和执行回执，不是本水平核心稿的程序独跑。
- Nishida 原讲义 Chapter III §2，Hypothesis 2.1、Theorem 2.1，印刷 pp.64–65，及 pp.72–73 的一阶拟线性应用，已经全文核对相关假设；其中演化变量只要求连续。仅在线读文本，未下载或逐页渲染 PDF。[讲义来源](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/bb/b2/bbb2303a-1e17-4807-a319-290a5b030b2f/n_nishida-102.pdf)。

本次逐节审查主稿，重新核对实际核心、分母、统一寿命、全 jet、位置单值、整体弦长、边界 reach、R38 入口及全像 \(E(3)\) 非全等。不是仅由前一 epicycle 结论或原 R38 的标题推断本应用成立。

## 2. 实际水平核心与统一解析邻域

作者取
\[
\lambda\in[1/32,1/16],\qquad
h_\lambda(\varphi)=1+\lambda\cos3\varphi,\qquad
\rho_\lambda=h_\lambda+h_\lambda''
=1-8\lambda\cos3\varphi.
\]
于是 \(1/2\le\rho_\lambda\le3/2\)。支撑函数表示
\[
\widetilde\gamma_\lambda
=h_\lambda e_r+h_\lambda'e_\varphi
\]
满足
\[
\partial_\varphi\widetilde\gamma_\lambda
=(h_\lambda+h_\lambda'')e_\varphi
=\rho_\lambda e_\varphi.
\]
因此它是严格凸解析闭曲线；其长度为
\[
\int_0^{2\pi}\rho_\lambda\,d\varphi=2\pi,
\]
对整个 \(\lambda\) 区间相同。

物质弧长坐标
\[
\theta=\Theta_\lambda(\varphi)
=\varphi-\frac{8\lambda}{3}\sin3\varphi
\]
有导数 \(\rho_\lambda>0\)，且满足
\(\Theta_\lambda(\varphi+2\pi)=\Theta_\lambda(\varphi)+2\pi\)。
故其反函数定义同一个物质圆周上的
\[
\gamma_\lambda(\theta)
=\widetilde\gamma_\lambda(\Theta_\lambda^{-1}(\theta)),
\quad
|\gamma_\lambda'|=1,
\quad
\kappa_\lambda=\rho_\lambda^{-1}\in[2/3,2].
\]
这是真实位置及真实弧长，不是只有曲率或框架的周期数据。

由于实域的导数统一离零，而 \(\lambda\) 区间和圆周均紧，解析反函数定理可在有限复邻域覆盖上统一使用；在重叠处由同一实反函数的唯一性粘合。缩小到一个共同复条带后，\(\gamma_\lambda,\kappa_\lambda\) 有统一上界，\(\kappa_\lambda\) 的复延拓有统一非零下界。也可先把 \(\lambda\) 作为被动复参数，再缩小其复邻域。这里没有把“每个 \(\lambda\) 各有一个宽度”误写成统一宽度。

初始柱带
\[
F_\lambda^{\rm cyl}(s,\theta)
=\gamma_\lambda(\theta)+s e_z,
\qquad -h_0\le s\le0,\quad h_0=1/10,
\]
确有与 \(\lambda\) 无关的第一基本形式 \(ds^2+d\theta^2\)。共同的固定高度平移 \(z_0e_z\) 可先加入全部初值；以后必须随同实际位置一起积分，不能独立移动出口。

\(\Theta_\lambda(\varphi+2\pi/3)=\Theta_\lambda(\varphi)+2\pi/3\)，故该参数化保留实际 \(C_3\) 对称。此事实不是非全等证明的替代品；后文另用实际面积不变量。

## 3. 全 jet 平入口的度量及其非循环选择

令
\[
E(s)=
\begin{cases}e^{-1/s^2},&s>0,\\0,&s\le0.\end{cases}
\]
选择作者给出的平坦截止 \(\psi\)，满足在 \(x\le1/4\) 为 1，在 \(x\ge3/4\) 为 0，并在 \(1/4<x<3/4\) 严格位于 0 与 1 之间。其具体平坦指数构造保证中间的严格正性；仅有抽象的 \(0\le\psi\le1\) 本身不足以保证下面所有严格不等式，故本审查保留作者的这个具体选择。

定义
\[
a_\epsilon''(s)=E(s)\psi(s/\epsilon),\qquad
a_\epsilon(s)=1+\int_0^s(s-r)a_\epsilon''(r)\,dr.
\]
逐项得：

1. 在 \(s\le0\) 有 \(a_\epsilon=1\)，且 \(a_\epsilon-1\) 的所有右侧导数在 0 为零。
2. 在 \(0<s<3\epsilon/4\) 有 \(a_\epsilon''>0\)。
3. 在 \(s\ge3\epsilon/4\) 有 \(a_\epsilon''=0\)，故这里存在实际开放的仿射段。
4. 仿射斜率严格为正，因为此前正积分非零。
5. 在固定小实区间上，\(a_\epsilon,a_\epsilon',a_\epsilon''\) 的界与 \(\epsilon\) 无关。例如正半区间 \(s\le1/4\) 上有 \(a_\epsilon'\le s\)、\(a_\epsilon\le1+s^2/2\)、\(a_\epsilon''\le1\)；负半区间是常数。

高阶径向导数会包含 \(\epsilon^{-1}\) 等因子，这不使上述三项低阶界失效。寿命论证必须只依赖已写出的低阶界；不能先拿一个随截止变化的 CK 寿命，再假定出口在寿命以内。

对某个共同选定的 \(\epsilon>0\)，
\[
g_\epsilon=ds^2+a_\epsilon(s)^2d\theta^2
\]
才是本族固定的共同度量。改变 \(\epsilon\) 是另一个构造选择，不是对原主候选作数值加密。

## 4. Gauss–Codazzi、统一寿命与参数依赖

取实际初始单位框架
\[
e_1=e_z,\qquad e_2=\gamma_\lambda',\qquad
N=e_z\times\gamma_\lambda',
\]
使 \(N\) 为平面内向法线。初值是
\[
M(0,\theta)=0,\quad C(0,\theta)=\kappa_\lambda(\theta)>0,
\quad L(0,\theta)=0.
\]
对于 \(g=ds^2+a^2d\theta^2\)，作者采用的三个系数满足
\[
LC-M^2=-aa'',\qquad
M_s=L_\theta-\frac{a'}aM,\qquad
C_s=M_\theta+\frac{a'}aC+aa'L.
\]
消去
\[
L=\frac{M^2-aa''}{C}
\]
只除以 \(C\)，并未除以 \(a''\) 或高斯曲率。初始 \(a''=0\) 以及出口 \(a''=0\) 均不会使这个正 \(C\) 解析正规形本身失效。R43 的 \(C=0\) 数据不在这个论证范围内。

记 \(U=(M,C)\)。其主部及低阶项为
\[
U_s=A(s,U)U_\theta+B_0(s,U),
\]
\[
A=
\begin{pmatrix}
2M/C&-(M^2-aa'')/C^2\\
1&0
\end{pmatrix},
\qquad
B_0=
\binom{-(a'/a)M}{(a'/a)C+aa'(M^2-aa'')/C}.
\]
这与代入原方程逐项一致。

在共同较宽条带上令初始解析范数有界于 \(B\)，再缩小条带使 \(|C_0|\ge1/3\)。取 \(c=1/6\)、半径 \(R\le c\)，则该球中 \(|C|\ge c\)。若 \(B_1=B+R\)，所有需要的系数界由 \(B_1,c^{-1}\) 和前节统一低阶径向界控制。例如
\[
|L|\le L_*=(B_1^2+2)/c.
\]
作者给出的
\(\Lambda=100(1+B_1)^3(1+c^{-3})\)
足够同时控制系数和其 \(U\) 导数。对解析条带的 Cauchy 估计只损失一个
\((\rho-\rho')^{-1}\)，并不产生两个空间导数的损失。

对增量 \(U-U_0\) 写 RHS 后，初始数据的角导数在较窄条带由较宽条带上界控制；相应 Lipschitz 常数和零增量 RHS 常数可统一写成作者的
\[
C_*=\Lambda(2+R+B/\rho_0),\qquad
K_*=\Lambda(1+B/\rho_0).
\]
它们与 \(\epsilon\) 无关，并可对整个紧 \(\lambda\) 区间统一选择。实演化参数的连续性满足所引 Nishida 定理的要求；该定理不要求 \(a_\epsilon\) 在 \(s\) 上解析，也不要求其高阶 \(s\) 导数统一有界。

因此先得到一个共同 \(T_*>0\)，然后才选择
\[
0<\epsilon<\min(10^{-2},T_*/2),
\]
并可继续缩小以满足后面的嵌入估计。这是出口确实落在同一存在区间内的依据。对于固定 \(\epsilon\)，系数在 \(s\) 上为 \(C^\infty\)，利用剩余条带宽度逐阶微分可把尺度解提升为联合 \(C^\infty\)。被动解析参数或有限复覆盖保证参数依赖和共同时间；没有将逐个参数的寿命下确界未经证明地当成正数。

## 5. 实际位置闭合及全部 Cartesian jet

径向重构是
\[
F_s=e_1,\quad
(e_1)_s=LN,\quad
(e_2)_s=(M/a)N,\quad
N_s=-Le_1-(M/a)e_2.
\]
角向兼容式为
\[
F_\theta=ae_2,\quad
(e_1)_\theta=a'e_2+MN,\quad
(e_2)_\theta=-a'e_1+(C/a)N,\quad
N_\theta=-Me_1-(C/a)e_2.
\]
在 \(s=0\)，这些角式与实际平面曲线的 Frenet 公式一致。Gauss–Codazzi 正是相应兼容条件；角向误差的径向系统齐次且初值为零，所以角式保持成立。框架保持正交，第一基本形式正好是 \(g_\epsilon\)。

对每个 \(\theta\) 从实际 \(F(0,\theta)=\gamma_\lambda(\theta)\) 积分径向 ODE。系数、位置初值和框架初值全都 \(2\pi\)-周期，ODE 唯一性直接给出
\[
F(s,\theta+2\pi)=F(s,\theta).
\]
这里已经比较了实际位置，不是由法线周期猜测不存在平移单值性误差。相同论证保留 \(C_3\) 作用。

在 \(s<0\)，度量严格为 \(a=1\)，且
\[
M=0,\qquad C=\kappa_\lambda(\theta),\qquad L=0
\]
是同一解析尺度 Cauchy 问题的解。唯一性使实际双侧解在负侧精确等于它。径向框架恒定，于是
\[
F_\lambda(s,\theta)=\gamma_\lambda(\theta)+s e_z
\]
在某个开负领成立。可以据此向下延长柱带到固定的 \(-h_0\)，无须要求原 \(T_*\ge h_0\)。

联合 \(C^\infty\) 跨过 \(s=0\)，加上负侧的精确柱面恒等，意味着每一个混合 Cartesian 导数在接口处都等于柱面的相应导数：
\[
\partial_s^j\partial_\theta^kF_\lambda(0,\theta)
=\partial_s^j\partial_\theta^k
(\gamma_\lambda(\theta)+s e_z)\big|_{s=0}
\quad(j,k\ge0).
\]
这才是全 jet 声称的证明；仅由 \(a-1\) 平坦或两 jet 相等本身不能跳到该结论。

## 6. 完整环带的嵌入与有边 reach

先核对一个对整圈有效的弦长下界。取两点间较短法向角弧，记其长度为 \(\Delta\varphi\le\pi\)。把弦投影到该弧中点的切向量，由 \(\rho\ge1/2\) 得
\[
|\gamma(\theta)-\gamma(\widehat\theta)|
\ge\frac12\int_{-\Delta\varphi/2}^{\Delta\varphi/2}\cos u\,du
=\sin(\Delta\varphi/2)
\ge\Delta\varphi/\pi.
\]
这条法向角弧的物质长度至多 \(3\Delta\varphi/2\)，因而最短物质角差 \(\Delta\theta\) 也不超过它。故
\[
|\gamma(\theta)-\gamma(\widehat\theta)|
\ge\frac{2}{3\pi}\Delta\theta
\ge\frac15\Delta\theta.
\]
此处并不要求较短法向角弧同时是较短物质角弧。

柱面纵向与平面内弦相互正交，所以在整个
\([-h_0,\epsilon]\times S^1\) 上，柱面映射关于最短角提升的欧氏参数距离有统一下界 \(1/5\)。

在新正领内，径向 ODE 和角兼容式给出
\[
|F_s-e_z|\le L_*\epsilon,\qquad
|F_\theta-\gamma_\lambda'|
\le(1+B_1)\epsilon.
\]
负领差值严格为零。令
\(C_1=L_*+1+B_1\)，再选 \(\epsilon C_1<1/10\)。
沿位于参数带内的直线和最短角提升积分导数差，得到整个带上的
\[
|F(P)-F(Q)|\ge\frac1{10}|P-Q|.
\]
因此证明的是全带嵌入，不只是局部浸入或单个截面的嵌入。

作者的方向 Hessian 上界
\[
M_*=L_*+4+3B_1
\]
覆盖新领内的二阶导数，也覆盖曲率至多 2 的柱带。其常数不要求 \(\epsilon\) 的高阶导数有统一界。

为了处理边界，不可只引用无边闭流形的法向论证。若 \(p=F(P)\) 是外点 \(z\) 的一个最近点，对任意可行参数线段方向 \(h=Q-P\)，约束最小性的单侧导数满足
\[
(z-p)\cdot DF(P)h\le0.
\]
Taylor 余项与全局弦长界给出
\[
|h|^2\le100|F(Q)-p|^2
\]
以及
\[
|z-F(Q)|^2-|z-p|^2
\ge(1-100rM_*)\,|F(Q)-p|^2,
\qquad r=|z-p|.
\]
当 \(r<1/(100M_*)\) 时，任何 \(Q\ne P\) 都不能成为另一最近点。参数域紧保证最近点存在，故
\[
\operatorname{reach}(F_\lambda)\ge\frac1{100M_*}>0
\]
对所有 \(\lambda\) 统一成立，包括边界。

此处是存在一个统一正下界。由于条带常数和 \(\epsilon\) 并未有效数值化，不得把它登记为 README 的 \(\operatorname{reach}/D\ge0.03\)。

## 7. 精确保留 R38 四阶开内领的另一版本

固定 \(A_4>0\)，改用
\[
a_\epsilon''(s)=12A_4s^2\psi(s/\epsilon),\qquad
a_\epsilon(0)=1,\quad a_\epsilon'(0)=0.
\]
在 \(0\le s\le\epsilon/4\) 有
\(a_\epsilon(s)=1+A_4s^4\)，正是 R38 固定度量。对固定 \(A_4\)，先取一个固定实区间以统一控制 \(a,a',a''\)，再用同一解析尺度论证选出 \(T_*\)，最后缩小 \(\epsilon\)。没有把 \(A_4\) 随 \(\epsilon\) 改动。

实际曲线、位置、框架和 \(M,C\) 初值都与 R38 相同。由于两侧 PDE 在开内领完全一致，唯一性给出这里实际位置 \(F\) 与 R38 解逐点相同；不是仅有相同第一基本形式或相同两 jet。

负侧必须注意：该四阶度量的双侧延伸本身并非柱带。作者组装的几何是在 \(s<0\) 接原柱带，并沿用 R38 已证的完整 Cartesian 两 jet 接合。这个组装按已证明的结论为 \(C^2\)，不得借用本审查第 5 节全平坦入口的全 jet 结论。R38 的四阶位置首项也明确说明一般不能把两个版本说成同一个 \(C^\infty\) 平入口。

四阶版本的出口同样在 \(s\ge3\epsilon/4\) 仿射，斜率正且不超过 \(4A_4\epsilon^3\)。对固定 \(A_4\) 可再缩小共同 \(\epsilon\) 以满足所有所需的小斜率与嵌入界。组装后的 \(C^2\) 正则性足够用于上一节的有界 Hessian 和边界 reach 证明。该版本和全 jet 版本各自有一个共同度量；两者之间不声称共同度量不变。

## 8. 不同振幅的整个像在全 \(E(3)\) 下不全等

本稿实际采用的是振幅 \(\lambda\)，不是仅移动三重谐波的相位。平面核心的围面积可直接算成
\[
\mathcal A(\lambda)
=\frac12\int_0^{2\pi}h_\lambda\rho_\lambda\,d\varphi
=\pi(1-4\lambda^2).
\]
它在正区间 \([1/32,1/16]\) 上严格递减，因此这些底边平面曲线彼此不全等。

还须证明完整环带的刚体运动必须把底边送到底边。整个嵌入环带的两个边界分量长度分别为
\[
2\pi,\qquad 2\pi a_\epsilon(\epsilon)>2\pi.
\]
后一严格不等式来自正径向积分，并非浮点近似。两个长度与 \(\lambda\) 无关，但彼此不同。任何把一个完整像送到另一个的欧氏等距变换都会把流形边界送到边界并保持弧长，故必须把唯一较短的底边送到底边。该底边就是平面曲线
\(\gamma_\lambda-h_0e_z\)（另可加共同高度）。

全 \(E(3)\) 包括反射，但刚体运动和反射都保持这条平面凸曲线的围面积。因此
\[
F_{\lambda_1}([-h_0,\epsilon]\times S^1)
\cong_{E(3)}
F_{\lambda_2}([-h_0,\epsilon]\times S^1)
\quad\Longrightarrow\quad
\lambda_1=\lambda_2.
\]
这核对的是整个像，而不只是指定物质标记不同。

取 \(\lambda(t)=1/32+t/32\)，\(t\in[0,1]\)，即可得到一个固定共同度量上的实际有限参数族。每个非初始参数的最小 \(E(3)\)-Hausdorff 距离严格为正：如果该下确界为零，非空紧像使有关平移有界，结合 \(O(3)\) 的紧性可取收敛刚体子列，极限将给出已排除的全等。不过这一步并未给出统一或有效的可见幅度常数。

反之，若只采用原 R38 的相位平移族，唯一性仍给出
\(F_\alpha(s,\theta)=R_\alpha F_0(s,\theta-\alpha)\)；
完整像依旧只是全局旋转，不能计为形变。本稿已经正确避开这个问题，没有改写原 R38 的相位结论。

## 9. 平坦出口的真实几何及尚未支付的事项

全 jet 版本仿射斜率为
\[
B_\epsilon=\int_0^{3\epsilon/4}
E(s)\psi(s/\epsilon)\,ds>0.
\]
利用正半轴上 \(E\) 单调，有
\[
B_\epsilon\le\epsilon e^{-1/\epsilon^2}.
\]
因此小 \(\epsilon\) 时内在圆锥角 \(2\pi B_\epsilon\) 严格很小。数值下溢到零不会把这个数学斜率变成零。仿射段上 \(a>1\)，不能把它识别为具有原 R43 边数据的平面圆环。

在出口 \(a''=0\) 时，Gauss 方程使第二基本形式行列式为零，但整个构造中 \(C\) 保持正，因此第二基本形式并不为零。应称其为平坦度量上的可展出口，而不能说实际面片已经成为平面。四阶版本同样保留它自己的 \(a>1\)、实际位置和边框架；不能通过独立移动出口去免除接合数据。

接受此稿不涉及：

- 固定二维开握持区 \(H\) 或同一局部二阶数据外的整体固定区；
- 无边闭曲面、混合端点或 R43 平面支路的实际位置及两 jet 接合；
- README 要求的可见幅度、规范化 reach 和最终网格/连续证书；
- 主轨迹的原候选身份、G5、尾包或其他完成门；
- 新 PDE 数值解、实际有限元/采样网格、终端执行或独立程序重放。

## 10. 独立审查判定与封存说明

未发现需要作者勘误的阻断问题。所审两种入口、同一 \(\lambda\) 区间的统一正宽、整个有边环带嵌入、统一正 reach 及全 \(E(3)\) 非全等均有完整证明。依赖的解析尺度寿命是存在性结论，参数宽度、最终形变幅度和规范化 reach 仍非有效数值。

本审查新建一个文本 note，保留作者主稿、R38 以及此前证明和回执原字节。失联执行器没有恢复；没有请求主求解、读优化数组、生成数据包、运行 producer 或数值几何后台。所有接受判定均限于以上明确范围。

本文件本身以新路径创建，再在实际返回的固定提交处全文回读；其 commit/blob/SHA-256 由审查人消息交 root 记录，不在正文中制造自引用哈希。HANDOFF、LOG、results 及完成状态由 root 按原规矩统一更新。
