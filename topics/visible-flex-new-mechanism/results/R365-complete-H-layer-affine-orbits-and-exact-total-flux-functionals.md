# R365：完整 H 层的两个仿射轨道与真实总通量公式

日期：2026-11-15。**完整纸面证明；没有执行新的 profile 积分、旧根恢复、符号程序、秩计算或研究运行。**

[R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md) 从原 R56 恢复了完整速度一形式；
[R362](R362-full-H2-C2-remainder-and-nonzero-weight-minus-six-pure-kernel-flux.md) 给出实际状态 $S_*=(1,1,1)$ 上完整 $H_2$ 的非零三阶平方项及真实连续 $C^2$ 余项。
本稿关闭这个 H 层的逐状态展开问题：给出第二个完整基准泛函，并证明**所有实际状态的两个 H 泛函都由这两个基准的正仿射输运准确得到**。

这是一条完整 $\Lambda$ 身份，不只是 principal 归约。两个“轨道”不表示整个 H 像只有二维，也不表示其他正规层已经支付。

## 1. 原读出及两个实际 H 系数

保持原共同右锚，记
$$
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad u\in C_c^\infty((\ell,r_*)).
$$
[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 的自然总通量泛函为
$$
\Lambda_u(V)=
\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),
\tag{1}
$$
其中 $\mathscr G$ 是原 pure 的真实有序 $2+2$ 尾映射。它由实际位于 $u$ 右侧的辅助包及其三矩定义，不是自由补设的修正。原结论是
$\Lambda_u(\mathcal R)=0$。

采用 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 的正规系数：
$$
\bigl(H_1(S)h_s+H_2(S)k_s\bigr)
(h_s k_{ss}-k_s h_{ss}),
\qquad S=(h,k,\omega),\quad h>0.
\tag{2}
$$
[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、
[R134](R134-acceleration-layer-from-complete-local-v4.md) 已付
$H_1(S),H_2(S)\in U$。
本稿不把未经证明的局部模板直接算作实际成本。

另用真实水平坐标
$$
d=h\omega-k,\quad \gamma=h_s,\quad \delta=d_s,\quad
k_s=2\omega\gamma-2\delta.
$$
将相同速度面积写作
$$
(\widetilde H_\gamma\gamma+\widetilde H_\delta\delta)
(\gamma\delta_s-\delta\gamma_s).
$$
在施加 $\Lambda$ 后，准确有
$$
\boxed{
\Lambda(\widetilde H_\gamma)
=-2\Lambda(H_1+2\omega H_2),\qquad
\Lambda(\widetilde H_\delta)=4\Lambda(H_2).}
\tag{3}
$$
这里已经使用 [R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)
在每个实际状态上的 $\Lambda(\bar A_{hh})=
\Lambda(\bar A_{hk})=\Lambda(\bar A_{kk})=0$：
非线性速度坐标变换从这些平方项产生的附加项也被消去。
面积本身的因子 $-2$ 不能漏掉。

## 2. 基准状态的全部同锚数据

在 $S_*$ 置
$$
v=u',\qquad r=u'',\qquad t=u''',\qquad Q=1+x^2,
$$
$$
L=v-xr,\qquad G=u-\frac{xv}{2},\qquad
F=Qr-2xv+2u,\qquad E=ur-\frac{v^2}{2}.
\tag{4}
$$
全稿的 $E$ 只表示这一局部多项式，不是另一个成本空间。
原第二局部第一分子为 $a=\gamma A+\delta B$，其中
$$
\begin{aligned}
A&=\frac{2Qvr-2xv^2-xQr^2+J_0-J_2}{16},\\
B&=-\frac{Qr^2+2J_1}{16},
\end{aligned}
\tag{5}
$$
$$
J_0=J(r^2),\quad J_1=J(xr^2),\quad
J_2=J(x^2r^2+2v^2).
$$
准确有
$$
A'=\frac{QtL}{8},\qquad B'=-\frac{Qtr}{8}.
$$
真实左值是
$$
A_L=\frac{\mu_0-\mu_2}{16},\qquad B_L=-\frac{\mu_1}{8},
$$
$$
\mu_0=\int r^2,\quad
\mu_1=\int xr^2,\quad
\mu_2=\int(x^2r^2+2v^2).
\tag{6}
$$
定义 $j_A=J(QtA)$、$j_B=J(QtB)$。
不要求这些二次场、原函数或其左值为零。

为把两个完整余项写得简洁，记三个明确的局部系数
$$
\begin{aligned}
M_{00}&=(1-\tfrac32x^2)v+(x^3-x)r+xu,\\
M_{01}&=(3x^2-1)r-\tfrac72xv+2u,\\
M_{11}&=2xr-v,
\end{aligned}
\tag{7}
$$
以及 $K=2ur+v^2-2xvr$。这些是本文的标量缩写，不是 R73 的矩阵坐标。

定义
$$
\begin{aligned}
\mathscr L_\gamma
&=\frac1{16}\int t
\{2M_{00}j_B-M_{01}j_A-4GLB-KA\},\\
\mathscr L_\delta
&=\frac1{16}\int t
\{M_{01}j_B-2M_{11}j_A+KB+2vrA\},
\end{aligned}
\tag{8}
$$
$$
\begin{aligned}
K_{\gamma\gamma}
&=\frac1{24}\int t(-FM_{00}-2GL),\\
K_{\gamma\delta}
&=\frac1{24}\int t(-FM_{01}+K),\\
K_{\delta\delta}
&=\frac1{24}\int t(-FM_{11}-vr),
\end{aligned}
\tag{9}
$$
$$
\mathscr T_\gamma=2B_LK_{\gamma\gamma}-A_LK_{\gamma\delta},
\qquad
\mathscr T_\delta=B_LK_{\gamma\delta}-2A_LK_{\delta\delta}.
\tag{10}
$$
式 (5)–(10) 指定了全部真实原函数和左尾，不留未定义的“低阶项”。

最后置
$$
\boxed{
\begin{aligned}
\mathscr D_\gamma(u)
&=-\frac1{128}\int xQ^2LE\,t^2
+\mathscr L_\gamma+\mathscr T_\gamma,\\
\mathscr D_\delta(u)
&=\frac1{128}\int xQ^2rE\,t^2
+\mathscr L_\delta+\mathscr T_\delta.
\end{aligned}}
\tag{11}
$$
主基准身份为
$$
\boxed{
\begin{aligned}
\Lambda_u(H_2(S_*))&=\mathscr D_\delta(u)/15,\\
\Lambda_u(H_1(S_*)+2H_2(S_*))&=-2\mathscr D_\gamma(u)/15.
\end{aligned}}
\tag{12}
$$
第一行正是 R362 的完整式；第二行是本稿新增的完整另一坐标。

## 3. 从原完整速度一形式得到 (11)

本节只整理 R358 已付的
$$
\mathfrak C=\mathfrak C_0+\mathfrak T_0-\Theta+\Theta_{\rm tail}/3,
$$
其原 $YC$、$ZZ$、history 导数及两个有序尾的因子全部保持。
原正规化给
$$
\mathrm d_v\mathfrak C
=\frac{15}{4}
\{\Lambda(\widetilde H_\gamma)\gamma+
\Lambda(\widetilde H_\delta)\delta\}
\,\mathrm d\gamma\wedge\mathrm d\delta.
\tag{13}
$$

R362 已按同锚 Fubini 证明以下两份完整抵消，对两个速度系数都成立：

- $\mathfrak C_0$ 的第一项与 $-\Theta$ 的外微分准确相消；
- 前两个真实尾项与 $\Theta_{\rm tail}/3$ 合为
  $\mathrm d_v\{a_L\int t(\gamma-x\delta)a\}/6$。

另一项 $Ql a'\mathrm d_va'/2$ 是准确的速度三次梯度。
这些抵消都先保留真实左值，再取外微分；没有将单个场当成紧支撑。

余下乘 $\mathrm d_vj$ 的两个项合为
$$
\frac{t}{16}
(M_{00}\gamma^2+M_{01}\gamma\delta+M_{11}\delta^2)
\,\mathrm d_vj,\qquad j=\gamma j_A+\delta j_B.
\tag{14}
$$
故其外微分的两个系数分别为
$$
\frac{t}{16}(2M_{00}j_B-M_{01}j_A),\qquad
\frac{t}{16}(M_{01}j_B-2M_{11}j_A).
$$
剩余 $-ga'\mathrm d_va/Q$ 贡献 (8) 的另外两个局部项。
这里
$g=\gamma G-\delta v/2$，并且
$2\{(-v/2)L-Gr\}=-K$。

真正的三阶平方项只来自
$$
\frac{x}{2}\,g a'\,\mathrm d_va'.
$$
由
$$
\mathrm d_vg\wedge\mathrm d_va'
=-\frac{QtE}{8}\,\mathrm d\gamma\wedge\mathrm d\delta
$$
得到 (11) 的两个明确项。
最后剩余尾一形式为
$$
\mathrm d_va_L
(K_{\gamma\gamma}\gamma^2+
 K_{\gamma\delta}\gamma\delta+
 K_{\delta\delta}\delta^2),
$$
外微分正是 (10)；两个因子 $2$ 来自二次式求导。

所以
$$
\mathrm d_v\mathfrak C=
(\gamma\mathscr D_\gamma+\delta\mathscr D_\delta)
\,\mathrm d\gamma\wedge\mathrm d\delta.
\tag{15}
$$
(3)、(13) 立即给 (12)。本节没有改变原二阶选择或 normal 势。

## 4. 两个余项都真正连续于 C²

为避免把一次 $u'''$ 口头称作“低阶”，保留 R362 的准确同锚消元：
$$
j_B=\frac{Q^2r^3}{48}+\frac{QrJ_1}{8}
+\frac14J(xrJ_1)-\frac1{24}J(xQr^3),
\tag{16}
$$
$$
\begin{aligned}
j_A=\frac1{16}\bigg\{&
-Q^2vr^2+2xQv^2r+\frac{xQ^2r^3}{3}
-Qr(J_0-J_2)\\
&+J\left(4x^2v^2r+\frac{Q(1-x^2)}3r^3
-2xr(J_0-J_2)\right)
\bigg\}.
\end{aligned}
\tag{17}
$$
这些原函数全部只用 $u,u',u''$。将它们代入 (8)，每项仅剩一次 $t$，
并乘关于 $r$ 的有限多项式，其系数只依赖 $x,u,v$ 及连续 $C^2$ 密度的 primitives。

具体地，对这样的系数 $a(x,u,v)$、primitive 乘积 $G_0$ 和 $m\ge0$，
$$
\int a r^m tG_0
=-\frac1{m+1}\int r^{m+1}(a'G_0+aG_0').
\tag{18}
$$
两个边项由紧 $r$ 支付，未假设 $G_0$ 左端为零。
对应的 $J$ 身份也保留局部端项
$-a r^{m+1}G_0/(m+1)$。
因此 (8)–(10) 中所有 $t$ 都可准确消去。

所以，在每个固定紧窗口和固定空 collar 上，
$$
\boxed{
\mathscr L_\gamma+\mathscr T_\gamma,\quad
\mathscr L_\delta+\mathscr T_\delta
\text{ 均为连续 }C^2\text{ 五次多项式泛函。}}
\tag{19}
$$
它们允许有限个原 Volterra 节点，且保留 (6) 的真实三矩。
式 (11) 的两个 $t^2$ 项不在 (19) 之内。

## 5. 全部真尾的正仿射协变

固定常数 $H>0,c\in\mathbb R$，定义
$$
(C_{H,c}u)(x)=u\left(\frac{x-c}{H}\right),\qquad
P_{H,c}V=C_{H,c}^{-1}V(C_{H,c}\,\cdot).
\tag{20}
$$
输入的全部槽同步变换。
[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md) 已从原曲面与逐阶恢复证明
$$
\widetilde h=Hh,\quad\widetilde k=k,\quad
\widetilde\omega=(\omega+c)/H,
\qquad \widetilde X(s,\xi)=H^2X(s,H\xi+c).
\tag{21}
$$
所有右锚、初始历史、forcing 及 scalar 输出按同一个 (20) 输运。
scalar 成本没有额外的 $H^2$ 幅度；$H^2$ 是物理场的相似比。

对于三条真实矩，直接换元给
$$
\boxed{
\mu(C_{H,c}u)=
H^{-3}
\begin{pmatrix}
1&0&0\\
c&H&0\\
c^2&2cH&H^2
\end{pmatrix}\mu(u).}
\tag{22}
$$
第三行同时包括原 $2(u')^2$ 项。矩阵可逆。
因此将实际右辅助包和 outer $u$ 一起输运，仍准确匹配原三矩；
有序先后、同一右 collar 与非紧左尾都保持。

现在 $u'''(\xi)=H^3(C_{H,c}u)'''(H\xi+c)$，
而 $\mathrm d\xi=\mathrm dx/H$。
分别对 (1) 的 scalar、pure 和真实尾项换元，得到
$$
\boxed{
\Lambda_u(P_{H,c}V)
=H^2\Lambda_{C_{H,c}u}(V).}
\tag{23}
$$
最后一项使用 (22) 和原 $\mathscr G$ 的线性矩输运，
不是令某个传入尾为零。
因此 $\ker\Lambda$ 对这个正仿射作用不变。

## 6. 整个 H 层的准确输运

在 $(h,d)$ 坐标中，(21) 给
$$
\widetilde d=d+hc,\qquad
\widetilde\gamma=H\gamma,\qquad
\widetilde\delta=\delta+c\gamma.
\tag{24}
$$
其速度面积准确乘 $H$：
$$
\widetilde\gamma\,\widetilde\delta_s-
\widetilde\delta\,\widetilde\gamma_s
=H(\gamma\delta_s-\delta\gamma_s).
$$
这里 $H,c$ 始终是常数；没有沿路径使用
$H(s)=1/h(s)$ 一类改变实际水平控制的变换。

R89 的完整局部生成元协变与 R129 的速度外微分相容。
在 (24) 中，速度与加速度均作同一个常数线性变换，
所以加速度平方项不产生新的 H 项。
第三阶 jet 的原边势及速度三次势则按同一个线性变换输运，
或在速度外微分中准确消去。

原 $v-\mathcal B_mN$ 中，只有 $N_2$ 可能涉及导数权四；
但 $\mathcal B_{m_2}N_2$ 纯为速度四次，不能改变本节的 H 系数。
$N_0$ 只进入权零、二层。
故写 $V\sim_\Lambda W$ 表示所有紧 $u$ 上 $\Lambda_u(V-W)=0$，有
$$
\boxed{
\begin{aligned}
P_{H,c}\widetilde H_\delta(S)
&\sim_\Lambda H\,\widetilde H_\delta(\widetilde S),\\
P_{H,c}\widetilde H_\gamma(S)
&\sim_\Lambda H^2\,\widetilde H_\gamma(\widetilde S)
+Hc\,\widetilde H_\delta(\widetilde S).
\end{aligned}}
\tag{25}
$$

还需一个实际的源结论，不能只靠协变猜测：
R358 的完整 (24)–(31) 在写成
$h,d,\gamma,\delta$ 后，**全部两种 H 读出都不依赖独立的 $k$**。
其中 $e=hx+d$、$Q=1+e^2$、$a'=Qt(\gamma v-(x\gamma+\delta)r)/(8h^3)$、
$m_2$、完整 $c_2$、原 $ZZ$ 的 $P,B$ 及两个真尾皆只用这些量。
这包括真实 $P_{C,s}$ 中的 $m_2$ 项，不是只对 principal 作观察。
其余原 frame 项落在更低导数权，或只改变速度四次项。

特别，
$$
\Lambda(\widetilde H_\gamma(1,k,k))
=\Lambda(\widetilde H_\gamma(S_*)),\quad
\Lambda(\widetilde H_\delta(1,k,k))
=\Lambda(\widetilde H_\delta(S_*)).
\tag{26}
$$
原 scalar 恢复中看似依赖 $x+\omega$ 的分母已按 R56 完整相消；
这里使用的是这一真实分子身份，而非将不许可的 profile 支撑移过几何极点。
若需从共同合法开窗口推广到原有限函数表达式，
采用 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、
[R203](R203-general-pure-lowest-two-weights-vanish.md) 已付的有限原式 faithful 身份，
不添加新的几何可达性断言。

## 7. 任意状态的两个完整公式

现在固定一个实际状态 $S$，取常数
$$
H=1/h,\qquad c=-d/h.
$$
它把该状态送到 $(1,k,k)$。对给定原 profile $u$，定义
$$
u_S(\xi)=u\left(\frac{\xi-d}{h}\right).
\tag{27}
$$
这是 $C_{1/h,-d/h}^{-1}u$，不是为每个槽另外选择 profile。

由 (23)、(25)、(26)，
$$
\Lambda_u(\widetilde H_\delta(S))
=h\,\Lambda_{u_S}(\widetilde H_\delta(S_*)),
$$
$$
\Lambda_u(\widetilde H_\gamma(S))
=\Lambda_{u_S}(\widetilde H_\gamma(S_*))
-d\,\Lambda_{u_S}(\widetilde H_\delta(S_*)).
\tag{28}
$$
最后用 $d-h\omega=-k$ 与 (3)、(12)，得到完整主公式：
$$
\boxed{
\begin{aligned}
\Lambda_u(H_2(S))
&=\frac{h}{15}\,\mathscr D_\delta(u_S),\\
\Lambda_u(H_1(S))
&=-\frac{2}{15}
\{\mathscr D_\gamma(u_S)+k\,\mathscr D_\delta(u_S)\}.
\end{aligned}}
\tag{29}
$$
右边由 (4)–(11)、(16)–(18) 全部指定，
保留同一原 canonical 选择、所有同锚 primitives 和真实矩尾。

所以若将每个成本看成泛函 $u\mapsto\Lambda_u(V)$，
整个实际 H 层的像由
$\mathscr D_\gamma,\mathscr D_\delta$ 的两个正仿射轨道线性生成。
这不是二维秩结论；一个函数的仿射轨道本身可以张成多维空间。
本稿没有重新计算该空间的维数。

## 8. 与剩余正规层和实际路径的边界

(29) 结束了 H 层在不同状态上的重复展开。
它同时给出所有这些状态值的完整三阶平方部分和明确的连续 $C^2$ 余项。
在固定的状态紧集、$h$ 有统一正下界及共同紧 profile 窗口上，
所用仿射输运连续，余项的 $C^2$ 连续性也一致保持。

R358/R362 的非零商结论与本稿相容；
它们不意味着某条给定路径已消去原 $M/T$、所有 period 或整个 ruling。
本稿也不把 root 的实际局部环构造替换为成本线性空间论证。

尤其，导数权二的 $\widehat Q_2$ 与导数权四的 $\widehat Q_4$ 仍是不同的未付层。
本稿没有删除 $N_0$、$N_2$，没有宣称 $\Lambda U$ 已由 H 层全部张成，
也没有把一个 affine 共轭解释成原冻结几何上的免费操作。
下一原式应从完整 $v-\mathcal B_m(N_0+N_2)$ 消费这些真实余密度，
而不是再对 H 状态表重复计算。
