# R51：六帽热反射的径向开启障碍与饱和源半径修正

日期：2026-11-14。repo_sources 推导，mechanism 独立核，root 全文复核；准确种子的穿越不等式三方核同。独立完整证明，未在本地评价真实候选或进行研究扫描。

准确帽见 [R44](R44-S9-six-cap-exact-embedding-and-normal-chord.md)，固定角跳与无限热平滑接口见 [R48](R48-six-cap-angular-jump-and-heat-extension.md)。本稿分析**未饱和的反射源半径经过帽出生半径**时产生的另一条条件门，随后给一个保持全部端口二 jet 的明确修正。

结论只涉及给定基场加有限径向解析自由列的准确目标积分性 \(V_\theta=\partial_t(aT)\)。不否定准确帽、一般热平滑、其他连接表示、一般 \(C^2\) 等距面或给定小容差近似；不把预选 frame 的 \(R\ne0\) 自动等同于所有重构位置都不可能准确等距。

## 1. 一个源帽在 \(r=d\) 的出生阶数

令准确六帽的外半径为 \(R_c\)，内接六边形弦距为

\[
d=R_c\cos(\pi/6),\qquad w=R_c-d>0.
\]

法向角为 \(\theta_j=j\pi/3\)，帽幅度 \(A_j>0\)。每帽使用

\[
\alpha_j(r,\phi)=A_jS_9\!\left(\frac{r\cos(\phi-\theta_j)-d}{w}\right),
\]

S9 在非正自变量上为零，且 \(S_9(x)=126x^5+O(x^6)\) 于右端 \(x=0\)。源圈半径 \(r\le d\) 时所有帽都准确平；对

\[
r=d+\rho,\qquad \rho>0,
\]

每帽只在 \(|\eta|<\arccos(d/(d+\rho))=O(\sqrt\rho)\)、\(\eta=\phi-\theta_j\) 的小角区间出生，并有

\[
r\cos\eta-d=\rho-\frac d2\eta^2+O(\rho\eta^2+\eta^4).
\tag{1}
\]

固定严格正的热时间 \(\tau_*>0\)，用正的周期热核 \(K_{\tau_*}\) 对角变量平滑。记上下侧符号为 \(\sigma=\pm1\)，帽的 beta 用实 lift \(-\sigma\pi\)。由准确标量帽公式，帽中心附近

\[
\beta+\sigma\pi=\sigma\cos\eta\,\alpha_j+O(\alpha_j^3),
\qquad
v=\sigma\sin\eta\,\alpha_j+O(|\eta|\alpha_j^3),
\qquad u=O(\eta\alpha_j^2).
\tag{2}
\]

beta 增量是 eta 的偶函数，v、u 是奇函数。定义正数

\[
C_*:=\frac{126}{w^5}\sqrt{\frac2d}
\int_{-1}^{1}(1-z^2)^5\,dz>0.
\]

代换 \(\eta=\sqrt{2\rho/d}\,z\)，并对热核作局部 Taylor 展开，得到

\[
H_{\tau_*}(\beta+\sigma\pi)
=\sigma C_*\rho^{11/2}
\sum_{j=0}^5A_jK_{\tau_*}(\theta-\theta_j)
+O(\rho^{13/2}),
\tag{3}
\]

\[
H_{\tau_*}v=O(\rho^{13/2}),\qquad
H_{\tau_*}u=O(\rho^{23/2}).
\tag{4}
\]

这些余项在 theta 上一致，并可取任意固定有限阶 theta 导数。原因是所有 theta 导数落到光滑热核上。特别地，v 的朴素 \(\rho^6\) 项因奇性准确为零；下一项来自核的 eta 一次项，才是 \(\rho^{13/2}\)。u 同理，\(\alpha^2\) 给十次径向阶，奇性再多支付一个 eta 因子，得到 \(\rho^{23/2}\)。

热核严格正、各 \(A_j>0\)，所以 (3) 的系数在每个 theta 处都非零，且全圈同号。只要 \(\tau(t)\) 在考察位置严格为正并解析变化，\(\tau(t)-\tau_*\) 只进入 (3) 的较高阶项。

## 2. 未饱和反射为什么有一个不被其他源抵消的出生项

原反射采用

\[
\varepsilon(t)=a(t)-R_c,\quad
r_0=R_c,\quad r_1=R_c-\varepsilon,\quad r_2=R_c-2\varepsilon,
\]

\[
E=3g(r_0)-3g(r_1)+g(r_2),
\qquad \widetilde E=H_{\tau(t)}E,
\tag{5}
\]

外乘正 cutoff \(\chi(t)\)，加到旧场及有限自由列上。假设某个内部点 \(t_0\) 有 \(r_i(t_0)=d\)、\(r_i'(t_0)\ne0\)、\(\chi(t_0)>0\)、\(\tau(t_0)>0\)。

- 若 \(r_1=d\)，则 \(\varepsilon=w\)、\(r_2=d-w<d\)，第二个内源在整个邻域准确平。
- 若 \(r_2=d\)，则 \(\varepsilon=w/2\)、\(r_1=(R_c+d)/2>d\)，另一个内源在邻域严格高于出生半径。

不存在两个源同时出生的抵消。

**另一个源的正则性。** 对任一固定 \(d<r<R_c\)，每帽的角支撑端点 \(\pm\arccos(d/r)\) 随 r 实解析，且最大超出量 \(r-d<w\)，尚未碰到 S9 的上端饱和分支。在这两个端点之间，准确标量公式与正热核都有局部解析表达。把积分改到固定区间后，热平均随 r、theta 和正 tau 实解析。半径小于 d 的源恒为平场；外源 \(r_0=R_c\) 固定，正热时间的变化也给解析函数。因此，除正在出生的那个源外，(5) 的其他项在 \(t_0\) 附近形成径向解析背景。

有限径向 B 样条自由场，在各样条片内也只是径向解析背景。若 \(t_0\) 恰在结点，取出生侧的一片，其解析表达仍能延拓到该片端点；整数阶 Taylor 项不能抵消下文的半整数首项，不要求跨结点本身解析。

于是以 \(\rho=r_i(t)-d\) 作局部径向坐标，整个标量场在出生侧具有

\[
\beta=\beta_{\rm reg}+B(\theta)\rho^{11/2}
+O(\rho^{13/2}),
\]

\[
v=v_{\rm reg}+O(\rho^{13/2}),\qquad
u=u_{\rm reg}+O(\rho^{23/2}),
\tag{6}
\]

其中 \(u_{\rm reg},v_{\rm reg},\beta_{\rm reg}\) 是该侧整数阶解析背景，并且

\[
B(\theta)=b_i\chi(t_0)\sigma C_*
\sum_j A_jK_{\tau(t_0)}(\theta-\theta_j)\ne0,
\qquad b_1=-3,\ b_2=1.
\tag{7}
\]

式 (6) 也对一个 theta 导数成立。

## 3. 准确积分性迫该整圈的角法曲率为零

仍写 R28 的单位正交 frame

\[
N=e_r(\theta+u),\quad
T=\frac{e_\theta(\theta+u)+ve_z}{\sqrt{1+v^2}},\quad
M=T\times N,\quad V=\cos\beta\,N+\sin\beta\,M.
\]

设 \(W=T\times V=-\sin\beta\,N+\cos\beta\,M=V_\beta\)。目标积分性残差沿 T 的分量准确为

\[
R_T=T\cdot\{V_\theta-\partial_t(aT)\}
=-a'-V\cdot T_\theta,
\tag{8}
\]

这里只用了 \(T\cdot V=0\)、\(|T|=1\)，没有把坐标二阶导数误当曲率。

将 (6) 代入 (8)。T 与 \(T_\theta\) 不依赖 beta，而 u、v 的非整数首项比 \(\rho^{11/2}\) 更高。因此

\[
R_T=R_{T,{\rm reg}}
-B(\theta)\,W_0\cdot (T_\theta)_0\,\rho^{11/2}
+O(\rho^{13/2}),
\tag{9}
\]

下标 0 表示在 \(t=t_0\) 的共同值。解析背景只有整数次 Taylor 项；若 \(R_T\equiv0\)，先消掉至五阶整数项，再除以 \(\rho^{11/2}\) 取极限，得到

\[
B(\theta)\,W_0\cdot (T_\theta)_0=0.
\]

因 (7) 处处非零，故

\[
W_0\cdot (T_\theta)_0=0\quad\text{对全部 theta}.
\tag{10}
\]

若完整 \(R=0\)，一阶形式 \(Vdt+aT d\theta\) 局部可积成浸入 X，且准确第一基本形式为 \(dt^2+a^2d\theta^2\)。其单位法向可取 W，角第二基本形式系数为

\[
\mathrm{II}_{\theta\theta}
=W\cdot X_{\theta\theta}=aW\cdot T_\theta=0.
\]

Gauss 方程随即给

\[
K(t_0)=\frac{\mathrm{II}_{tt}\mathrm{II}_{\theta\theta}
-\mathrm{II}_{t\theta}^2}{a(t_0)^2}
=-\frac{\mathrm{II}_{t\theta}^2}{a(t_0)^2}\le0.
\tag{11}
\]

**条件命题。** 未饱和反射的任一单独源出生圈若位于 \(\chi>0\)、\(\tau>0\)、目标 \(K>0\) 的内部，则上述热基场加有限径向解析自由列不可能准确满足 \(R=0\)。这里没有要求角向非解析；正热核已经使内部角向解析，障碍来自径向半整数项。

## 4. 当前固定径向种子的两次出生确在正曲率补丁内

本节仅用准确参数和解析不等式，不评价候选位置或进行数值积分。当前椭圆柱半轴为 \(1,7/25\)，长度 \(L=9/10\)，平尾比例 \(3/50\)，核心比例 \(1/25\)，活动三段比例 \((1/4,7/20,2/5)\)，斜率落差 \(3/10\)，末段为 S11。于是

\[
R_c=\frac{11}{50}+\frac9{10}\frac3{50}=\frac{137}{500},
\qquad h=\frac1{10},\qquad
\ell_3=L\left(1-\frac1{25}-\frac3{50}\right)\frac25
=\frac{81}{250}.
\]

令 \(a_0\) 为准确椭圆周长除以 \(2\pi\)。逐点的加权均方根不小于加权平均，给
\(\sqrt{\sin^2\phi+(7/25)^2\cos^2\phi}\ge\sin^2\phi+(7/25)\cos^2\phi\)；再对平均用平方根凹性，得到纯解析界

\[
\frac{16}{25}\le a_0
\le\sqrt{\frac{1+(7/25)^2}{2}}<\frac34.
\]

种子定义给

\[
\nu=\frac{40}{27}\left\{\frac{100}{81}
\left(a_0-\frac{11}{50}\right)-\frac{107}{300}\right\},
\qquad \mu=\nu+\frac3{10}.
\]

上述粗界已足推出 \(0<\nu<1/2\)、\(0<\mu<4/5\)。末段斜率为

\[
-a'(t)=\nu+(1-\nu)S_{11}(x),
\quad x=1-\frac{t_f-t}{\ell_3}.
\tag{12}
\]

在整个长 h 的补丁中 \(x\ge1-h/\ell_3=56/81>1/2\)。S11 严格递增且 \(S_{11}(1/2)=1/2\)，故 \(-a'(t)>1/2\)。因此

\[
a(t_f-h)-R_c
=\int_{t_f-h}^{t_f}(-a'(t))\,dt
>\frac h2=\frac1{20}.
\tag{13}
\]

又因 \(\sqrt3/2>5/6\)，

\[
w=R_c(1-\sqrt3/2)<\frac{R_c}{6}
=\frac{137}{3000}<\frac1{20}.
\]

\(\varepsilon(t)=a(t)-R_c\) 在补丁中严格递减，并在 \(t_f\) 等于零。因此 \(\varepsilon=w\) 和 \(\varepsilon=w/2\) 各有唯一内部解；这正是 r1、r2 的两次出生。它们都严格处于末 S11 段内部，那里

\[
K=-a''/a=\frac{(1-\nu)S_{11}'(x)}{a\ell_3}>0,
\]

且 \(\chi=1-S_9((t_f-t)/h)>0\)、\(\tau=\tfrac1{128}((t_f-t)/h)^6>0\)。所以当前未饱和、长 \(h=1/10\) 的准确热基场满足 §3 的条件门，而不只是“可能碰到”出生点。

## 5. 保留端口二 jet 的明确饱和修正

无需把 cutoff 区间缩得很短。保持同一准确帽、同一径向度量 a、同一 h 和热时间，改用

\[
c=\frac w4,\qquad
e(\varepsilon)=c\tanh(\varepsilon/c),
\qquad
\widehat r_1=R_c-e(\varepsilon),\quad
\widehat r_2=R_c-2e(\varepsilon).
\tag{14}
\]

三项反射仍是 \(3g(R_c)-3g(\widehat r_1)+g(\widehat r_2)\)，只是源半径的连续定义发生改变。准确有

\[
e(0)=0,\quad e'(0)=1,\quad e''(0)=0,
\]

\[
e'(\varepsilon)=\operatorname{sech}^2(\varepsilon/c),\qquad
e''(\varepsilon)=-\frac2c\operatorname{sech}^2(\varepsilon/c)
\tanh(\varepsilon/c).
\tag{15}
\]

所以原反射的全部端口 value、t、tt 及其角导数保持不变。实现中应使用真实链式

\[
\frac d{dt}e(\varepsilon(t))=e'(\varepsilon)a',\qquad
\frac{d^2}{dt^2}e(\varepsilon(t))
=e''(\varepsilon)(a')^2+e'(\varepsilon)a'',
\tag{16}
\]

然后再放入同一个 Gaussian 路径 Jet，而不是继续沿用未饱和的半径导数。

另一方面，只要 \(\varepsilon>0\)，便有 \(0<e<c\)，从而

\[
R_c>\widehat r_1>R_c-c>d,
\qquad
R_c>\widehat r_2>R_c-2c=\frac{R_c+d}{2}>d.
\tag{17}
\]

所有内源始终在准确、不交的源帽域中，并且永不经过出生半径 d。本稿的半整数径向条件门因此被明确移除。补丁内部各源热平均在径向、角向均局部解析；帽端仍用真实端口分支，热时间趋零及 (15) 保持已证二 jet 拼接。

这是一项**新的连续基场设计**，不是原未饱和热场的数值精化；但准确度量 g 和物理帽均未改变。身份必须锁定 \(c=w/4\) 的准确代数来源、完整 tanh 函数、三源定义、热时间、cutoff 与原固定 \(c_0\)。有限 GH、FFT 和径向求积仍只是该新连续场的评价，需分别作同参数精化及误差控制。

## 6. 证明的实际边界

饱和修正只解决 R48 的固定角跳及本稿的内部出生两种特定障碍，并未构造准确 \(R=0\) 解。它也不保证初态成本小、条件数好、误差达到 \(10^{-6}\)、位置嵌入、幅度或全闭面 reach。新的真实评价与任何求解仍须在公开仓库自己的 Actions 运行；本稿不包含这些结果。
