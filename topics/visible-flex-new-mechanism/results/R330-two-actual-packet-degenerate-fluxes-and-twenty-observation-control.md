# R330：实际紧微包的两个退化通量与二十个全局观测的同时支付

日期：2026-11-15。**完整纸面原式和有限实现证明；没有执行求积、符号程序、profile 扫描、数值秩、人工检查或研究运行。**

[R324](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md) 与 [R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md) 已给指定有理端芽的同一实际圆及一条真实全局二阶规范，使该端口的完整 ruling 可消。尚欠的整个 period 不能由此假定属于 $L_f$ 的像。[R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md) 的有限十三行系统也以两个真实周期特解存在为前提。

本稿直接支付其中两个此前未付的**内部退化点通量**。它们取自当前圆两个实际完整副本中的同一个最细紧包，不使用旧矩形导数包替换当前 profiles。完整原响应 $K_{P,[P,R]}$ 及其一次代数导子给一个准确二阶 Vandermonde。其真成本权为 $-8,-7$，从而可以在同一真实几何上与 [R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md) 的十个低权 self 坐标共同控制。

再用 [R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md) 的八个其余矩阵单位及 [R322](R322-full-self-scaling-shift-and-exact-reduction-to-the-matching-response-weight.md) 的真实权投影，得到二十个观测的块三角满射。真实有限控制保全部基准，最终可同时具有
$$
\boxed{\pi V_X=0,\qquad
F_{10}(V_X)=0,\qquad
\mathsf T(V_X)=0,\qquad
\mathcal F_0(V_X)=\mathcal F_1(V_X)=0.}
\tag{1}
$$
这里 $\mathsf T$ 是原有序平台三矩矩阵，$F_{10}$ 是 R323 的完整十坐标，$\mathcal F_j$ 是下文两条固定圆退化通量。它们不是全 period、全部 self 或整个 joint 系统。

这是从起点纳入新约束的实际几何选择。改变全局几何期间不称原度量不变；最终几何固定后才谈其同一度量和同一二阶规范。

## 1. 使用已经构造的真实圆，不改成一个同母近似

固定 R324 的最终有限频率 profiles
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
\phi_\theta=c f+s g,
\quad c=\cos\theta,\ s=\sin\theta.
\tag{2}
$$
最细包支撑严格分离，具有正间隙，$a_i\ne0$。每个实际 $u_i$ 经其原固定正仿射坐标具有
$$
u_i(y)=\psi(y)P_i(y),\qquad
\psi(y)=e^{-1/(1-y^2)},\qquad
P_i>0
\tag{3}
$$
的形式；$P_i$ 在闭区间邻域实解析，包含已取定的有限频率和有限纠正。不同基本包可以有不同 $P_i$。

原八个完整副本仍是同一实际基本 pair 的完整平移，幅度非零。后续十二副本、最后五块和正幅合成均保留这些内部副本。因此可在一个固定最终块、一个固定十二副本内，选择八副本中的两个：在它们内部选择**同一个基本微包**。在最终物理坐标中写为
$$
\begin{array}{ll}
f=\rho_j a\,u(x-t_j),&
g=\rho_j b\,u(x-t_j)
\quad\text{于所选第 }j\text{ 包},\\
j=0,1,\qquad \rho_0\rho_1\ne0,\qquad t_0\ne t_1 .
\end{array}
\tag{4}
$$
这里的 $u$ 已是最终实际形状，不是原未扰动母包。共同外幅已吸收进 $a,b$ 或 $\rho_j$。选同一个十二副本，避免把其 $g$ 反号与两包幅度混用。

原等平方背景编码给 $b^2=B_0$，而 $a^2$ 是 $B_0/2$ 或 $9B_0$，其中 $B_0>0$；故
$$
a\ne0,\qquad a^2-b^2\ne0.
\tag{5}
$$
共同正幅及物理正仿射变化不破坏这些条件。以下所有算子和导子均在该**最终**坐标、同一个右锚中定义。

## 2. 每个实际解析紧包都有可用的内部退化点

记基本包左端为 $\ell$，并置
$$
p=u',\qquad r=u'',\qquad s_3=u''',\qquad
A_u=6p s_3-2r^2.
\tag{6}
$$
(3)使 $u>0$ 于内部，且左平端附近 $p>0,r>0$。令 $b_*$ 是从左端向右的第一个 $p=0$ 点。它存在，因为 $u$ 必在内部取得正最大值；在 $(\ell,b_*)$ 有 $p>0$。

令 $z=p^{2/3}$。在这个开区间
$$
z''=\frac{A_u}{9p^{4/3}}.
\tag{7}
$$
左端 $z'$ 平坦趋于零且在邻域为正。由于 $p$ 实解析且其在 $b_*$ 的零点有限阶，
$p\sim C(b_*-x)^m$，所以 $z'<0$ 于 $b_*$ 左邻域；不要求 $z$ 光滑跨过该端点。于是 $z'$ 在严格内部取得一个正最大值。固定其中一个点 $x_*$，即有
$$
\boxed{A_u(x_*)=0,\qquad p(x_*)>0,\qquad r(x_*)>0.}
\tag{8}
$$
不要求这是 $A_u$ 的简单零点，也不数值寻找它。固定实际 profile 后，$x_*$ 是此后几何联调中不再移动的一个真实点。

两实际对应点为
$$
\ell_j=\ell+t_j,\qquad x_j=x_*+t_j.
\tag{9}
$$
因为 $f=\rho_j a u(\,\cdot-t_j)$，
$A_f=(\rho_j a)^2A_u$ 于该包，所以 $A_f(x_j)=0$；在 $\ell_j$，$f$ 的全部正阶 jets 为零。

## 3. 两条原 period 必要门及真实规范不变性

在整个原成本空间 $U$ 上定义
$$
\boxed{
\begin{aligned}
\mathcal F_j(V)
={}&\int_{\ell_j}^{x_j}
f'(x)\,\partial_x^2V(f^2,g)(x)\,dx\\
&-\{f(x_j)-f(\ell_j)\}\,
\partial_x^2V(f^2,g)(\ell_j),
\qquad j=0,1 .
\end{aligned}}
\tag{10}
$$
下文也以 $\mathcal F_j(G)$ 记 (10) 对单个输出函数 G 的同一线性读出。这个延拓始终用原完整函数 $V(f^2,g)$。当 $\pi V=0$ 时，它正是实际 $\sin^2\theta$ 周期系数 $V_d$ 的读出。第二项保真实左平台二阶导数，不是将全部右历史设零。

由 [R181](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md) 的全区间原式，
$$
f'L_f(w)''
=\partial_x\{A_f(f'w''-f''w')\}.
\tag{11}
$$
在 (10) 两端，右侧通量的边值均为零；原局部式还给
$L_f(w)''(\ell_j)=0$。所以
$$
\boxed{\mathcal F_j(L_f(w))=0}
\tag{12}
$$
对任意允许的全区间光滑 $w$ 成立。$w$ 不必支撑于该包，不能藉此删除它的外部 history。

若真正的目标 $G_d=-V_d^c/(2\tau)$ 属于 $L_f$ 的像，则 (10) 必为零。这是原退化方程的必要条件；并非从有限矩阵的行数得到的条件。

对于 R326 的真实首个规范
$$
w_c=-\Phi_{m_*}(f^2-\phi_\theta^2),
$$
其中 $m_*$ 随本次实际几何而定，完整周期代价为
$$
V_d^c=V_d-2\tau L_f\{\Phi_{m_*}(f^2-g^2)\}.
$$
由 (12)，准确有
$$
\boxed{\mathcal F_j(V_d^c)=\mathcal F_j(V_d).}
\tag{13}
$$
第三齐次规范在 $M=0$ 时不改周期。因此本稿清掉的确是 R326 之后那个同一 joint 问题所需的两条必要门，不是另一个重锚的 canonical 版本。

## 4. 完整最低权响应在 rank-one 紧包上的原式

统一使用
$$
J(F)(x)=\int_x^{r_*}F(\eta)\,d\eta,\qquad
P(a,b)=J(a''b''),\qquad
R(a,b)=a'b'+xJ(a''b'').
$$
记
$$
\tau_R=[P,R],\qquad
\mathcal K=\mathcal B_P(\tau_R).
\tag{14}
$$
[R217](R217-two-left-tail-invariants-independent-on-pure-zero-responses.md) 和 [R219](R219-eight-packet-fluxes-independent-on-pure-zero-responses.md) 已证明这是完整真实 pure-zero 响应，并给其同锚单层右积分结构。

这里重算其在当前 rank-one 包上的具体值，不能把旧导数分包的公式未经证明移植。对一个 $u$，置
$$
A=P(u,u)=J(r^2),\qquad
\mathscr J_u(x)=J\{(\eta-x)r^2s_3^2-p r s_3^2\}.
$$
其中积分内的 $p,r,s_3$ 在 $\eta$ 取值，外 $x$ 不当作积分变量。

原完整三槽式
$$
\tau_R(a;b,c)
=a'b''c''+
J\{a''(b'''c'+b'c''')+(x-\eta)a''(b''c'')'\}
\tag{15}
$$
给
$$
\begin{aligned}
\tau_R(A;u,u)&=-r^4+4\mathscr J_u,\\
\tau_R(u;u,A)&=r^4/4-2\mathscr J_u,\\
P\{u,\tau_R(u;u,u)\}&=-r^4/4 .
\end{aligned}
\tag{16}
$$
最后一式使用真实 $\tau_R(u;u,u)=-J(r^3)/3$，没有设其左常数为零。

将 (16) 代入 R83 的完整响应
$$
\mathcal B_E(\tau)(F,\phi)
=2\tau(\Phi_ED;D)-4\tau(\phi;\phi,\Phi_ED)
+4\Phi_E\{\phi,\tau(\phi;D)\},
$$
对 $f=a u,\phi=c_0u,d_0=a^2-c_0^2$，得到
$$
\boxed{
\mathcal K(a^2u^2,c_0u)
=a^2d_0\,\mathscr K_u,\qquad
\mathscr K_u=-2r^4+8\mathscr J_u.}
\tag{17}
$$
这里用了 $d_0^2+c_0^2d_0=a^2d_0$；最后一条真实 history 没有丢掉。

R181 的单层原式又给
$$
L_u(A)=\frac52r^4-12\mathscr J_u,
$$
因而完整恒等为
$$
\boxed{\mathscr K_u=-\frac13r^4-\frac23L_u\{P(u,u)\}.}
\tag{18}
$$
$A$ 自身有真实左常数，但 (18) 允许它；(12) 的退化通量不要求 $A$ 是紧包。

R219 已由原组合证明 $\mathcal K$ 是局部四次密度加单层 $J$，没有嵌套积分；其有限导子也保这一结构。故在 (2) 的不交**值支撑**上，
$$
\mathcal K(f^2,\phi_\theta)
=\sum_i a_i^2(a_i^2-c_i^2)\mathscr K_{u_i},
\quad c_i=a_i\cos\theta+b_i\sin\theta .
\tag{19}
$$
这是完整原函数身份，包括左尾；不是将 $P(u_i,u_i)$ 当紧函数之后的形式分包。

## 5. 本包通量的严格非零值

对基本包 $f_*=a u,\ g_*=b u$，令 $\mathcal F_*$ 按 (10) 定义，积分从 $\ell$ 到 $x_*$。其原平台修正对 $\mathcal K$ 为零，因为 (17) 左尾至多仿射。

由 (18)、(12)，
$$
\mathcal F_*(\mathcal K)
=-\frac{a^3(a^2-b^2)}3
\int_\ell^{x_*}p(r^4)''.
$$
两次普通分部积分保右端 $x_*$ 的真实 jets：
$$
\int_\ell^{x_*}p(r^4)''
=4p r^3s_3-\frac45r^5\bigg|_{x_*}.
$$
而 (8) 给 $p s_3=r^2/3$，所以
$$
\boxed{
C_*:=\mathcal F_*(\mathcal K)
=-\frac8{45}a^3(a^2-b^2)r(x_*)^5\ne0 .}
\tag{20}
$$
严格性只用 (5)、(8)。不要求母包同形扫描，不用一个未经评价的数值余量。

(20) 也说明这些通量不由 whole pure 自动清掉；下一节会进一步在保旧十坐标的同一响应核内改变它们。

## 6. 两个对应副本给准确二阶 Vandermonde

采用原代数导子
$$
\mathscr D=x^2\partial_x-2x,\qquad
\delta A=\mathscr D_{\rm out}A-\sum_{\rm in}A(\ldots,\mathscr D\,\cdot,\ldots).
$$
它不是新的实际坐标变形。R217 已证 E8 与完整第三交换子在该导子下闭合。因此
$$
\delta\mathcal K\in\mathcal R\cap\ker\pi
\tag{21}
$$
是有限个真实响应的线性组合。具体地
$$
\delta P=-2R-2S,\qquad
\delta R=4L-2U_1,
$$
$$
\delta\tau_R=-2[S,R]+4[P,L]-2[P,U_1],
$$
其中 $S=\Phi_{s_0},L=\Phi_{p_0},U_1=\Phi_{s_1}$。这给全部所需实际原型的有限来源。

令 $\mathcal N=\mathscr L_{\partial_x}$，
$\mathcal H=\mathscr L_{x\partial_x-1}$。完整原式有
$$
\mathcal N\mathcal K=0,\qquad
\mathcal H\mathcal K=-5\mathcal K,\qquad
[\mathcal N,\delta]=2\mathcal H,
$$
所以
$$
\boxed{\mathcal N\delta\mathcal K=-10\mathcal K,\qquad
\mathcal N^2\delta\mathcal K=0.}
\tag{22}
$$
在最终坐标搬回平移 $t$ 后，准确得到
$$
\mathcal T_t\mathcal K=\mathcal K,\qquad
\mathcal T_t\delta\mathcal K=\delta\mathcal K-10t\mathcal K.
\tag{23}
$$

$\delta\mathcal K$ 的左尾次数至多二。所选包左方的其他包输出在此为零，右方包只留下二次尾；(10) 的平台项逐个消掉它们的常二阶导数。因此 R219 的分包理由原样给
$$
\mathcal F_j(\mathcal K)=\rho_j^5 C_*,
\qquad
\mathcal F_j(\delta\mathcal K)
=\rho_j^5(C_1-10t_jC_*),
\tag{24}
$$
其中 $C_1=\mathcal F_*(\delta\mathcal K)$ 是原公式确定的有限数，不需要另评价。第五次幅度来自四次输出与读出中的一个 $f'$ 或 f 值差。

于是
$$
\boxed{
\det
\begin{pmatrix}
\mathcal F_0(\mathcal K)&\mathcal F_0(\delta\mathcal K)\\
\mathcal F_1(\mathcal K)&\mathcal F_1(\delta\mathcal K)
\end{pmatrix}
=-10\rho_0^5\rho_1^5C_*^2(t_1-t_0)\ne0.}
\tag{25}
$$
这不是以两条行数授秩；真实基点、幅度、间距和尾项已全部进入行列式。

## 7. 与十个已付完整 self 坐标的同一个响应矩阵

令 $F_{10}$ 为 R323(40)—(41)的十个真实线性观测：先减去对应 pure 截面，再读成本权 $-6$ 的两个完整 self 坐标与权 $-4$ 的八个完整坐标。后者包括
$$
Z(u)=\frac12\left(\int(u'')^2\right)^2 .
$$
不把这个非局部项删除。

原真成本分级给
$$
P:-3,\qquad R:-2,\qquad
\tau_R:-5,\qquad
\boxed{\mathcal K\in U_{-8},\quad\delta\mathcal K\in U_{-7}.}
\tag{26}
$$
也可由 (22) 的 $\mathcal H$ 与四个输入槽之间的三个单位权差，得到 $\mathscr L_{x\partial_x}\mathcal K=-8\mathcal K$；$\delta$ 升一权。这里没有将 sl2 的 $-5$ 错当作成本权。

由真不同权及 (21)，
$$
\boxed{F_{10}(\mathcal K)=F_{10}(\delta\mathcal K)=0.}
\tag{27}
$$
R323 已给十条完整 pure-zero 响应 $J_1,\ldots,J_{10}$，使 $F_{10}$ 矩阵 $B$ 可逆。对十二观测
$$
F_{12}=(F_{10},\mathcal F_0,\mathcal F_1)
$$
及十二列 $(J_1,\ldots,J_{10},\mathcal K,\delta\mathcal K)$，完整矩阵为
$$
\begin{pmatrix}
B&0\\
C&D
\end{pmatrix},
\tag{28}
$$
其中 $D$ 正是 (25) 的非退化矩阵。未知的 $C$ 是旧十响应带来的真实两通量代价，保留而不设为零。

故
$$
F_{12}(\mathcal R\cap\ker\pi)=\mathbb R^{12}.
\tag{29}
$$
这给的是同一响应核上的联合结论，不是把两个独立满射命题相加。

## 8. 可同时清全部九个平台矩阵条目：二十观测加强

R297 的原九条响应为
$$
\mathcal J_{ij}=16\mathcal B_{\Phi_{p_j}}(\sigma_i),\quad
(\sigma_0,\sigma_1,\sigma_2)
=(64\chi_{32},-32\chi_{37},64\chi_{40}),
$$
$$
\pi\mathcal J_{ij}=0,\qquad
\mathsf T(\mathcal J_{ij})=\mathsf e_{ij}.
\tag{30}
$$
不由矩阵标签猜整条成本同权。按 R322 的真实有限 Laurent 权投影，取
$$
\widehat{\mathcal J}_{ij}=\Pi_{i+j-4}\mathcal J_{ij}.
\tag{31}
$$
$\Pi_\sigma\mathcal R\subset\mathcal R$、pure 与该投影交换；原有序矩阵坐标 $\mathsf T_{ij}$ 的真成本权恰为 $i+j-4$。因此权独立性准确给
$$
\pi\widehat{\mathcal J}_{ij}=0,\qquad
\mathsf T(\widehat{\mathcal J}_{ij})=\mathsf e_{ij}.
\tag{32}
$$
即使采用的原代表非齐次，(31)也足够。真实权投影是已有有限正缩放作用的实线性组合，其原型与基准按原响应实现保留，不执行新的成员计算。

对 $(i,j)\ne(0,0)$，这些权为 $-3,-2,-1,0$，均不是 $-6,-4$，所以
$$
F_{10}(\widehat{\mathcal J}_{ij})=0.
$$
原十列只在 $-6,-4$，对这八个矩阵条目均为零；(26)的两列对全部矩阵条目均为零。

在 pure 核上，R323 的 $Z$ 坐标正是 $\mathsf T_{00}$，而其他权不贡献 $\mathsf T_{00}$。在全 U 上还须保其 pure 截面修正；最终 $\pi V=0$ 时该修正准确消失。因此不要再把 $\mathsf T_{00}$ 作为第21个独立目标。

取
$$
\boxed{
F_{20}=\bigl(F_{10},
(\mathsf T_{ij})_{(i,j)\ne(0,0)},
\mathcal F_0,\mathcal F_1\bigr).}
\tag{33}
$$
上述二十个 pure-zero 原响应列的完整矩阵为
$$
\begin{pmatrix}
B&0&0\\
0&I_8&0\\
C_0&C_1&D
\end{pmatrix},
\qquad \det B\,\det D\ne0.
\tag{34}
$$
所有底行代价仍保留。于是
$$
\boxed{F_{20}(\mathcal R\cap\ker\pi)=\mathbb R^{20}.}
\tag{35}
$$
二十是此明确观测像的维数，不是整个 U、$\mathcal R$ 或 fixed-circle joint 商的维数。

## 9. 从响应满射到实际几何：固定局部芽、profiles 和点

(35)满足 [R222](R222-simultaneous-real-pure-and-eight-flux-control.md) 一般有限联调定理的全部代数前提；原 pure 商仍保留。所用原型是 R323 的原型、(30)—(31)的有限原型及第6节明确列出的 R71 交换子。没有一个新未实现的第三模板。

选择顺序如下。

1. 先把这些有限原响应、小二阶族、真实第三原型、full-pure 库、背景闭 hook 和必要 M0/frame 桥纳入同一个有限库。按 R312 选择允许的真实有理端口，固定
   $$
   h=H(1+\varepsilon\sigma^2),\quad
   k=\kappa,\quad\omega=\omega_e,\quad
   H>0,\ \varepsilon>0,\ \kappa\ne0 .
   $$
   所需 M0 端口搬移和成对正则前缀保原型的真实完整第三量；其第四基准必须计入。共享原语及真倒行使用相同当次参数。
2. 固定这一局部芽参数后，取 R324 的最终有限频率圆。其十九门、整个中心角恒等及同一芽参数都已确定。此后选择(4)的两真实包和(8)的点，固定全部二十观测。**不在 profiles 已定后通过另缩 $\varepsilon$ 或改 $\kappa$ 来重新解释旧十九门。**
3. 在这些固定查询下，按 R222 记全部实际 prototype 基准，先作原 whole-pure 校正，再保其对 $F_{20}$ 的全部成本。真实复制字给
   $$
   V=E_0(t)+n\left(2\sum\widehat v_j+
   \sum t_j K_j\right).
   $$
   最后原 pure 截面的全部二十观测代价进入同一个有界 $C^1$ 余项。有限大 n 的原收缩/IFT准确支付指定的 whole-pure 与 $F_{20}$ 目标；不把 signed 列当成零基准路径。
4. [R302](R302-regular-chi-prototypes-shared-reversal-and-enhanced-Morse-control.md)的整字正则化和增强目标 IFT在同一个固定有限字上应用。指定有理核心及其参数始终保护，只在核心之外使用自由 masked 几何扰动；原型第三量可以漂移，但共享整原型/真倒行使整个控制字仍 $M=\mathbf T=0$，全部目标由增强 IFT恢复。其所需背景 hook 结构保持 $\mathbf T=\tau\mathfrak H$、$\tau\ne0$；本证明不以某个旧数值 $\tau$ 为不变量。
5. 同一真实 Klein 闭合使用改变后 prototype 的实际位移。整个全局几何取得 whole-pure 零、$F_{20}=0$，并可在同一精确约束族中取全域 Morse。此后冻结新几何，才得到它自己的固定度量。

这里第4步不以“有限观测”代替几何正则性。对 $F_{10}$ 与 $\mathsf T$，原真实查询承载和光滑几何变分密度已由 R323/R302 证明。两条 (10)也是固定 x 点、固定 profiles 和固定积分端点的原函数线性读出。在有限真实 U 上可用有限函数评价表示；或直接对原 R56 Duhamel 恢复在 x 上积分。其紧支撑 s 几何导数仍是光滑积分密度，不是几何变量的 Dirac 约束。因此 R302 的 two-jet 横截/Morse论证增加这两行后仍适用。

这一构造不能理解为在原冻结几何上免费加 $K$ 或 $\delta K$。所有新基准、全局 history、时长、位移和度量变化均由上述真实字产生并计入。固定的只是指定局部芽和实际 profiles；全局入矩阵 $m_*$ 允许改变。

## 10. 已付的真 period 门与仍须使用同一规范的部分

在所得新实际闭几何上，(1)准确成立。R324的已付中心条件只依固定局部芽和已固定 profiles，故没有因第9节的全局几何联调而改变。对本次真实 $m_*$ 重取 R326 的
$w_c=-\Phi_{m_*}D$，其六交叉矩仍由原八完整副本逐槽支付；相应第三规范也按本次完整 We 初值重取。因此指定端口仍可完整消去，且 (13)保两条真实目标通量为零。

将 $\mathsf T=0$ 放回 [R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md) 的全平台递推，准确只剩
$$
R_iq_i=0,\qquad T_iq_i=0,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i.
\tag{36}
$$
当前 $a_i\ne0$，$(R_i,T_i)$ 不同时为零，所以全部平台的二次门仍要求**每个真实 $q_i=0$**。本稿的十个低权 self 坐标没有支付其余权的完整 $q_i$，不得将(36)删掉。

本稿新付的内部通量仅是两个实际点上的(10)。当全部平台二次门后来也付清时，其平台修正项才为零；此时它们就是
$$
\int_{\ell_j}^{x_j}f'(V_d^c)''=0.
$$
目前使用修正形式是为了使其在平台仍未付时也为一个独立、准确的规范不变量，而不是提前假定平台成功。

仍未支付：

- 其他 $A_f$ 零点及 $V_e^c$ 的全部必要通量；
- 每包总通量、原仿射平台和右锚常数是否共同匹配；
- 退化点的光滑除法、内部临界点延拓和真实端 Green 分支；
- 两个完整目标是否属于 $L_f$ 的像；
- 即便周期特解存在，R327 的十三行是否有同一相位光滑、种子为零的解；
- 指定端口以外的全部 ruling、后续阶数与有限等距族。

本稿没有另给这些未付门可达性。已经完成的是：在当前真正解析紧微包圆上明确识别两个内部退化点，原式算出其响应的非零常数与真实二阶行列式，并把它们和旧十 self 坐标、全部有序平台矩阵放进**同一个**保全部成本的实际有限控制系统。它推进了原全 period 的真实必要条件，同时保留后续同一个二阶规范的完整 joint 欠账。
