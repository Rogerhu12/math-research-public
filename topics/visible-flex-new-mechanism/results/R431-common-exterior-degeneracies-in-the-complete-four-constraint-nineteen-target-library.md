# R431：四约束与十九根的同一母库可保持全部退化点的共同外区

日期：2026-11-16。**纯纸面存在证明；没有运行新的 profile、求积、符号程序、秩、零点计数或十九根研究检查。**

[R412](R412-complete-weight-zero-natural-null-mothers-and-nineteen-common-targets.md) 已给同一母库中的四个完整 $n_2$ 系数、共同低阶纤维与十九个真实目标，同时只保留有限简单退化性。它的固定纠正方向可能穿过原 $A_f$ 点，所以不能把 [R405](R405-common-exterior-packets-and-local-ordered-currents-at-all-internal-degeneracies.md) 另一母库的共同 cap 性质直接搬来。

本文从同一次存在构造的起点加强支撑选择。可以取一个中心小区间，使**全部最终母函数变化都严格在其中**，且该区间内 $A_f$ 始终严格负。其外的所有 $A_f$ 简单零点、邻域和全体 jets 准确共同，原四约束、共同 $D,E_5$、整个 $\mathcal F_{\rm rat}$ 及十九个完整值在同一点保持。

本结论使用 R412 已允许的函数类：活动内区为 $C^\infty$，真实平端保留严格正解析 prefactor。若另要求所有最终母在整个连通内部实解析，则共同开段会迫使它们完全相同；不能在这个更强类中同时使用下文非平凡紧支撑控制。

正文最后把共同 cap 的可用范围分清：R407 的完整 self cap 与 actual 有限 totals 可以用于同一实际成本；R405 的 Euler current 仍只在原 signed $\ker(E,\Lambda_{\rm all})$ 类上使用，不由有限自然查询零偷换出来。

直接来源另有 [R403](R403-one-pair-degeneracies-and-nineteen-exact-rational-targets-by-concentration.md)、[R407](R407-connected-moment-fibers-fix-self-caps-and-retain-the-actual-total-fluxes.md)、[R411](R411-positive-analytic-mothers-blind-to-the-weight-zero-natural-affine-orbit.md)、[R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md)、[R429](R429-complete-kk-minus4-values-and-actual-common-joint-sections.md)。

## 1. 需要保持的同一个对象与函数类

在共同母坐标 $-1<y<1$ 中，令
$$
q=(q_0,q_1,q_2,q_3)
$$
为 R411 的四个**完整**零权自然平移系数。每个 $q_j$ 都是局部、连续 $C^2$、五次多项式泛函。采用原
$$
F^\star=(\mathcal F_{\rm rat},D,E_5).
\tag{1}
$$
$D,E_5$ 是 R413 原两完整局部积分；$\mathcal F_{\rm rat}$ 含三矩、原 raw/corrected self、Green、有序接口及其必要平移系数。其数值从本文选出的新母 $u_0$ 冻结，不要求保持旧已发表圆的数值纤维。

原十九目标仍是 R412(3)的 $\mathcal V_{19}$；真实位置、宽度、八/十二副本、最后完整块及原交替系数不改变定义。以下只加强原 profile 存在选择，不重求其原 principal 秩或原科学值。

记
$$
p_u=u',\qquad
A_u=6u'u'''-2(u'')^2 .
$$
最终要得到有限个母 $U_i$ 与一个数 $\delta>0$，满足
$$
\boxed{
\begin{gathered}
q(U_i)=0,\quad F^\star(U_i)=F^\star(u_0),\quad
\mathcal V_{19}=0,\\
U_i=u_0\quad (|y|\ge\delta),\qquad
A_{U_i}<0\quad (|y|\le\delta),\\
\{A_{U_i}=0\}\cap(-1,1)
=\{A_{u_0}=0\}\cap(-1,1),
\end{gathered}}
\tag{2}
$$
且这些共同零点全部简单、位于外区，其上 $u_0'\ne0$。
全部非中心 $p$ 零点也在共同外区准确不动；中心的 p 零点简单。

这不是强加 R410 的一对零模式。共同的正半轴 $A$ 零点数可以是任意原构造所得的有限数。

## 2. 一个全内部解析、四约束正则且已简单化的起始母

从 R413 已证的 $D-E_5>0$ 开放子族起步，取 R411 的正解析母及四行非零 minor，再作 R412 §4 的有限约束 Morse 选择。所有扰动充分小时，先得到一个偶、正、真紧的光滑母 $u_{\rm m}$，满足
$$
q(u_{\rm m})=0,\quad \operatorname{rank}Dq(u_{\rm m})=4,\quad
u_{\rm m}''(0)\ne0,
\tag{3}
$$
其 p 和 A 的全部内部零点有限且简单，$D(u_{\rm m})-E_5(u_{\rm m})>0$。
端 collar 为 $\psi_3$ 乘原正解析 prefactor，
$\psi_3(y)=\exp[-3/(1-y^2)]$。

为了下一节的解析唯一性，只在这一步把整个起始母选成解析类。写
$$
u_{\rm m}=\psi_3 P_{\rm m}.
$$
因为原 Morse 改动严格在内区，$P_{\rm m}$ 在闭区间为正偶 $C^\infty$ 函数。
选取(3)的一组四个光滑内支撑正常方向 $e_\alpha$；
$e_\alpha/\psi_3$ 在端邻域为零，因而也在闭区间光滑。

用偶多项式分别在相对 $C^4$ 范数逼近
$P_{\rm m}$ 和 $e_\alpha/\psi_3$。
得到 $\widetilde u=\psi_3\widetilde P$ 与四个
$\widetilde e_\alpha=\psi_3\widetilde Q_\alpha$。
其 $Dq$ 四列仍可逆，且 $q(\widetilde u)$ 任意小。
对这四个真实方向作有限 IFT，准确解
$$
q\!\left(\widetilde u+\sum_\alpha a_\alpha\widetilde e_\alpha\right)=0.
$$
参数可任意小，于是取得
$$
u_{\rm a}=\psi_3P_{\rm a},\quad P_{\rm a}>0
\ \text{为偶多项式},\quad q(u_{\rm a})=0,
\quad\operatorname{rank}Dq(u_{\rm a})=4.
\tag{4}
$$

相对 $C^4$ 逼近保留(3)的所有简单内部零点及正性。
在平端不能只用绝对小范数：原 prefactor 的归一端式使
$u_{\rm a}'$ 定号，且
$(1-y^2)^8A_{u_{\rm a}}/\psi_3^2$
在端 collar 有严格正下界，故没有新增端部零点。
$D-E_5>0$ 也由完整 $C^2$ 连续性保留。

因此(4)同时是全内部实解析、四约束正则的母，并有全部所需简单性。四个 $\widetilde e_\alpha$ 都指数平零；用偶内 cutoff 在 $C^2$ 中逼近它们，四列 minor 仍非零。因此(4)的秩4也确在全偶 $C_c^\infty(-1,1)$ 变分域成立，后节可在该域使用解析唯一性。

这一辅助解析母不是十九根的最终形状；下一步之后允许原 R412 的 $C^\infty$ 内区。

## 3. 新局部秩引理：四个正常方向可全放进任意中心小窗

对每个 $q_j$，在紧变分上作真实分部积分：
$$
Dq_j(u_{\rm a})[h]
=\int_{-1}^1\mathscr E_j(y;u_{\rm a})h(y)\,dy.
\tag{5}
$$
$\mathscr E_j$ 是其局部 Euler 密度，至多使用 $u_{\rm a}^{(4)}$。
显式 y 系数与(4)均实解析，故 $\mathscr E_j$ 在整个连通内部解析。

变分空间为偶函数，应取密度的偶部
$$
\mathscr E_j^{\rm ev}(y)
=\frac{\mathscr E_j(y)+\mathscr E_j(-y)}2.
$$
不要求原密度本身已经为偶。

**局部秩引理。** 对任意非空正开区间
$J\Subset(0,1)$，$Dq(u_{\rm a})$ 限制到偶的
$C_c^\infty(J\cup(-J))$ 后仍满射 $\mathbb R^4$。

若不满射，存在同一个非零常向量 c，使
$\sum c_jDq_j$ 杀该空间。任取 J 中的实紧 test 并偶化，由(5)及基本变分引理得
$$
\sum_jc_j\mathscr E_j^{\rm ev}(y)=0\quad(y\in J).
$$
实解析唯一性使它在整个 $(-1,1)$ 为零。
(5)随即给全偶紧域中的同一线性关系，违(4)的秩4。
故结论成立。于是可从这个实际空间选四个固定光滑正常方向，形成一个真非零四阶 minor；不需要对它执行计算。

由 $u_{\rm a}''(0)\ne0$，可取一个小 $\delta>0$，使
$$
A_{u_{\rm a}}\le-c_A<0,\qquad
\left|u_{\rm a}'(y)/y\right|\ge c_p>0
\quad(0<|y|\le\delta),
\tag{6}
$$
且 $u_{\rm a}'(y)/y$ 与 $u_{\rm a}''(0)$ 同号。
中心商按偶性光滑延拓。所有 $A$ 零点及非中心 p 零点均在 $|y|>\delta$。

在 $(0,\delta)$ 内选两个闭包不交的正开小区间
$J_{\rm n},J_{\rm p}$。用局部秩引理在
$J_{\rm n}\cup(-J_{\rm n})$ 中选四个正常方向
$$
e_1,e_2,e_3,e_4.
\tag{7}
$$
未来的 principal 见证及集中点只放在 $J_{\rm p}$，所以(7)不改这些点附近的 jets。

这里仅在解析母 $u_{\rm a}$ 上使用了一次解析唯一性。以后选出的最大秩母可以非解析；(7)的可逆性由小邻域中的连续性保持，不能再次假借其解析性。

## 4. 固定整个外 cap 的受限最大 F 秩与同母十九见证

按 R403/R412 的原有限选择顺序，先固定用于主列的实际位置、宽度、全部 copy 平移及最后各块的布局。以下十九 minor 都使用这同一个布局。原随共同母三矩而定的正归一因子保留在列内；它们非零且在母邻域连续，选定 $u_0$ 后一并冻结，不在最终根之后移动或重排。

令 $\mathscr B_\delta$ 为偶 $C^2$ 函数组成的 Banach 空间：
其支撑在 $[-\delta,\delta]$，在 $\pm\delta$ 的零、一次、二次端 jets 为零。
所有变化在外区准确为零。令
$$
X=\ker Dq(u_{\rm a})|_{\mathscr B_\delta}.
$$
用(7)作四约束图册
$$
\chi(v)=u_{\rm a}+v+\sum_{\alpha=1}^4a_\alpha(v)e_\alpha,
\quad v\in X,\quad q(\chi(v))=0,
\quad a(0)=Da(0)=0.
\tag{8}
$$
它在一个固定小 $C^2$ 球内实解析。

在这个**同一个 cap 固定图册**上定义
$$
G(v)=F^\star(\chi(v)),\qquad
r=\max_{\|v\|_{C^2}<\varepsilon}\operatorname{rank}DG(v).
\tag{9}
$$
r 是这个受限空间的真最大秩；不称它等于原全域最大秩，也不把观察生成数当作 r。

光滑内支撑方向在 $\mathscr B_\delta$ 稠密；沿四个固定正常方向投影后，在 X 中仍稠密。因此(9)的一个最大非零 minor可由光滑母点和有限光滑切向实现。

R403 §4 的十九个 free-jet 见证在任意非空正开区间都成立：
原点对主列是关于 b 与二阶 jets 的多项式，若在
$b\in J_{\rm p}$ 的所有自由 jets 上有一个行关系，原多项式身份就迫其为 R324 已排除的普遍关系。
用偶 Hermite 扰动在 $J_{\rm p}$ 中实现有限个见证 jets；
投影进 X 及(8)的四个正常校正都支撑于 $J_{\rm n}$，所以不改变这些 jets。
因此这些十九阶 minor 在同一个(8)中不恒零。

将(9)的最大 minor 和各最终块所需的有限十九 minor 的光滑见证合入一个有限维参数空间。它们是该空间内的非零实解析函数；有限乘积不恒零，故在原点任意近处同时非零。
参数方向固定光滑，因而可使所得共同母
$$
u_0=\chi(v_0)
\tag{10}
$$
在 $C^4$ 中任意接近 $u_{\rm a}$。
它满足 q=0、受限最大 F 秩 r、全部所需十九 minor 非零，同时保(6)、正性和 $D_0-E_0>0$。

最重要的是
$$
u_0=u_{\rm a}\quad(|y|\ge\delta).
\tag{11}
$$
所以全部外部简单 p/A 零点的位置、邻域与所有 jets 从这一步已经准确冻结；不是用小扰动后另找对应点。

冻结的数据是 $F^\star(u_0)$，包括原三矩与共同 $D_0,E_0$。
这些是同一次新构造的数据，不是旧数值纤维的重命名。

## 5. 全部低阶纠正也严格在中心

选(9)最大 minor的光滑切向，在 $u_0$ 处记其实际方向为
$f_1,\ldots,f_r$。它们和(7)均严格支撑于中心区间，且
$$
Dq(u_0)f_\ell=0.
$$
取相应 r 个 F 分量 $F_I$，其实际 Jacobian 为
$$
D(q,F_I)(u_0)[e_1,\ldots,e_4,f_1,\ldots,f_r]
=
\begin{pmatrix}
Dq[e_1,\ldots,e_4]&0\\
*&DF_I[f_1,\ldots,f_r]
\end{pmatrix},
\tag{12}
$$
两个对角块可逆。若 $r=0$，第二块为空，以下结论读为受限 $F^\star$ 在局部常值。

全部邻近母都在 cap 固定的 q=0 图册中。
所选 minor 在邻域非零，整受限微分秩又不超过(9)的 r，
所以局部常秩证明：解 q 与 $F_I$ 就保持整个 $F^\star$。
这正是只保某个非零 minor 不足、必须使用真实受限最大秩的地方。

固定方向 $e_\alpha,f_\ell$ 可以穿过中心 p 零点，但不能碰外区任何 A 根。
它们的高阶范数只作为固定有限常数进入后续误差；没有随 N 改换正常方向。

## 6. 有号集中：总 C3 不小，但 A 的大项处处非正

令
$$
g_{N,b}(y)=\sqrt N
\{e^{-N^2(y-b)^2}-e^{-N^2(y+b)^2}\},\quad b\in J_{\rm p}.
$$
它为奇函数，且
$$
y\,g_{N,b}(y)\ge0 .
\tag{13}
$$
取偶原函数 $\zeta_{N,b}'''=g_{N,b}$，在0取前三个零初值。
令 $\chi_0$ 为非负偶 cutoff，严格支撑于
$J_{\rm p}\cup(-J_{\rm p})$，在全部选中集中点附近等于1。
设
$$
\sigma=-\operatorname{sgn}u_0''(0),\qquad
w_{N,b}=\sigma\chi_0u_0\zeta_{N,b}.
\tag{14}
$$
与 R403/R412 同一次积分估计给
$$
\|w_{N,b}\|_{C^2}=O(N^{-1/2}),\qquad
w_{N,b}'''=\sigma\chi_0u_0g_{N,b}+O(N^{-1/2}).
\tag{15}
$$
所有 cutoff 导数只乘 $\zeta,\zeta',\zeta''$，故属于显示误差。
最高脉冲高度为 $\sqrt N$，不宣称全 $C^3$ 小。

对每个基本位置的固定非负幅度 z，用(12)解
$$
U_{i,N,z}
=u_0+z_iw_{N,b_i}
+\sum_\alpha c_{i\alpha,N}(z_i)e_\alpha
+\sum_\ell d_{i\ell,N}(z_i)f_\ell,
$$
$$
q(U_{i,N,z})=0,\qquad F^\star(U_{i,N,z})=F^\star(u_0).
\tag{16}
$$
在固定有限幅度盒 $0\le z_i\le Z$ 内，
全部系数和一次参数导数为 $O(N^{-1/2})$。
因为方向固定光滑，其纠正的 $C^4$ 量也为同阶。
因此
$$
U_{i,N,z}'''
=u_0'''+\sigma z_i\chi_0u_0g_{N,b_i}+e_{i,N,z},
\quad
\|e_{i,N,z}\|_\infty+
\|\partial_{z_i}e_{i,N,z}\|_\infty=O(N^{-1/2}).
\tag{17}
$$

所有函数仍偶。由 $C^2$ 小量与偶性，
$$
|(U_{i,N,z}'-u_0')(y)|
\le |y|\,\|U_{i,N,z}''-u_0''\|_\infty .
$$
故有限 N 足够大时，中心整个区间上
$U_{i,N,z}'(y)/y$ 与 $u_0''(0)$ 同号，且离零；
中心 p 零点仍简单。

把(17)代入完整 A，并把高项的系数保留为**实际**的 $U_{i,N,z}'$：
$$
\boxed{
A_{U_{i,N,z}}
=A_{u_0}
+6U_{i,N,z}'\sigma z_i\chi_0u_0g_{N,b_i}
+O(N^{-1/2}).
}
\tag{18}
$$
余项中只含有界的 $u_0'''$、$U_i'$ 与二阶差，以及(17)的固定方向误差，因此一致为所示大小。

由(13)、$\chi_0\ge0$、$u_0>0$、$z_i\ge0$ 和
$\sigma=-\operatorname{sgn}u_0''(0)$，
(18)的高项在**左右整个中心区间**都非正。
这不是只检查右半区，也没有将
$(U_i'-u_0')g_{N,b_i}$ 错归为一致小量。
由(6)、(10)缩小邻域后保留的严格负界，得到
$$
\boxed{A_{U_{i,N,z}}\le-c_A/2<0\quad(|y|\le\delta)}
\tag{19}
$$
于整个固定非负幅度盒上成立。

外区则由全部支撑的真实限制给
$$
U_{i,N,z}=u_0=u_{\rm a}\quad(|y|\ge\delta).
\tag{20}
$$
所以没有新增 A 根、没有旧根位移；所有外区 p 根也准确不动。
端 collar 一字不变，不再需要以绝对小范数估计指数微小量。

## 7. 原十九个完整值仍在一个有限 N 上同时为零

(16)的四个正常与 r 个切向纠正都是原 R412 的完整有限 IFT，只将允许空间缩至中心。
第4节已在这个同一空间支付了所需十九 minor。
原十九量的完整最高三阶导分裂仍是
$$
\mathcal V_{19}(\mathbf U)
=\mathcal B(\mathbf U)
+\sum_i\lambda_i\int
\mathbf P_i(x,U_i,U_i',U_i'')(U_i''')^2\,dx ,
\tag{21}
$$
其中 $\mathcal B$ 是原全部 $C^2$ 余项、self、Green 与真实 ordered/history。
这是 R296/R324/R403 已付的完整分裂，不重新研究其秩或主式。

(15)—(17)的高脉冲 $L^2$ 有界、$L^1=O(N^{-1/2})$；
其与固定三阶基线的交叉趋零。
二阶系数及参数导的误差一致趋零，乘有界的三阶平方积分仍趋零。
$\sigma^2=1$，所以改变高项的保护号不改变原主列。
于是完整映射仍有
$$
\mathcal V_{19,N}(\mathbf z)
=\mathbf b+\sum_i z_i^2\mathbf v_i+o_{C^1}(1).
\tag{22}
$$
$\mathbf v_i$ 保留全部实际位置、宽度、copy 权及点对系数；
$\mathbf b$ 是原完整有限基线，不被置零。

原十二交替位置给每形状组严格正核，第4节给联合行秩十九。
沿原 R403/R412 的同一个有限非退化根论证，
先固定一个严格正幅盒，再取充分大的**有限** N，取得
$$
\boxed{\mathcal V_{19,N}(\mathbf z_N)=0,\qquad
q(U_i)=0,\quad F^\star(U_i)=F^\star(u_0).}
\tag{23}
$$
此幅盒包含在第6节的非负盒中，故(19)—(20)同时适用于真实根。
每个基本位置的全部实际副本同步改变；各块的有限阈值统一取最大值。

这里只复用已付十九根机制，并证明新的支撑与正常修正不破其原 $C^1$ 极限。
没有新增 $t^4$ 项、遗漏非局部基线、假设离散 $1/N$ 光滑，或将无穷集中当作实际母。

## 8. 同矩连通路径也留在中心，R407 因而适用于所有外根

在最终有限 N 上，(16)的低阶 IFT 在整个
$[0,Z]$ 上定义，且正常/切向系数在0为零。
对最终每个 $z_i^N>0$，取真实路径
$$
U_{i,t}
=u_0+t z_i^Nw_{N,b_i}
+\sum_\alpha c_{i\alpha,N}(t z_i^N)e_\alpha
+\sum_\ell d_{i\ell,N}(t z_i^N)f_\ell,
\quad0\le t\le1.
\tag{24}
$$
它准确保持 q 和整个 $F^\star$，特别
$$
\mu(U_{i,t})=\mu(u_0).
\tag{25}
$$
全部变化严格在 $(-\delta,\delta)$，所有外 cap 完全相同。
中间 t 不要求十九值为零；这里只把它作为原 universal 输入空间中的同矩恒等式路径。真正研究圆取 t=1。

由 R407 的完整原恢复，
$m(U_{i,t},\partial_tU_{i,t})=0$ 的三个真实矩
使 $Z(U_{i,t},\partial_tU_{i,t})$ 在中心两侧都准确为零。
对原 $M=0$、同端口闭 frame 成本，若 universal $\mathcal QV=0$，则
$$
\partial_t S_{V,U_{i,t}}
=-4\mathscr K(Z_{U_{i,t}},Z(U_{i,t},\partial_tU_{i,t}))
$$
在左外区为真实二次多项式、右外区为零；
whole $\mathcal Q$ 杀其二次项。
故
$$
\boxed{
S_{V,U_i}''=S_{V,u_0}''
\quad\text{于 }|y|\ge\delta .
}
\tag{26}
$$
这只消二阶导的差，不删真实左仿射 history。
参考是整个 $u_0$，不能仅因外区相同便把它换成内部不同、三矩未证相同的 $u_{\rm a}$。

因此原 R407 仅用于一对外镜点的 cap 身份，现在可合法同时用于所有外区简单 A 根。没有把一阶纤维导数零外推到不连通纤维。

## 9. 全部实际根、宽度与两通道的准确共同 cap 表

将实际幅度并入原圆系数一次，写
$$
u_i(x)=U_i((x-\xi_i)/w_i),\quad w_i>0,\quad
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad a_i\ne0.
$$
令原正半轴共同 A 根为
$$
\delta<b_1<\cdots<b_m<1.
$$
它们有限、简单，数目 m 不预设为1或11。实际根与 jets 为
$$
x_{i,\alpha}^{\pm}=\xi_i\pm w_i b_\alpha,\qquad
u_i^{(k)}(x_{i,\alpha}^{\pm})
=w_i^{-k}u_0^{(k)}(\pm b_\alpha).
\tag{27}
$$
不同实际宽度继续保留。

取完整参考 $v_{\xi,w}(x)=u_0((x-\xi)/w)$。
对每个 $\alpha$ 定义原 self cap 积分
$$
s_{V,\alpha}^-=\int_{\xi-w}^{\xi-wb_\alpha}v' S_{V,v}'',
\qquad
s_{V,\alpha}^+=\int_{\xi+wb_\alpha}^{\xi+w}v' S_{V,v}''.
$$
跨包 cap 同样记
$$
L_{V,\alpha}^-(\xi,w,n)
=\int_{\xi-w}^{\xi-wb_\alpha}v'\mathcal U_{V,n}(v)'',
$$
$$
L_{V,\alpha}^+(\xi,w,n)
=\int_{\xi+wb_\alpha}^{\xi+w}v'\mathcal U_{V,n}(v)''.
\tag{28}
$$
这里 $\mathcal U_{V,n}$ 保 R405 的原完整三矩右尾及整个 s-history。
whole $E=0$ 下其二阶导是原局部式；self 则使用(26)，没有冒称任意 self 由 cap jets 决定。

仍令
$$
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,\quad
n_{R,i}=\sum_{j>i}R_j\mu(u_j),\quad
n_{T,i}=\sum_{j>i}T_j\mu(u_j).
\tag{29}
$$
所有实际次序、正宽、幅权和后续完整复制均保留。
原两个真实 partial 在每个根上准确为
$$
\begin{aligned}
H_{d,i,\alpha}^-&=
a_i^3\{R_i s_{V,\alpha}^-+
L_{V,\alpha}^-(\xi_i,w_i,n_{R,i})\},\\
H_{e,i,\alpha}^-&=
-a_i^3\{T_i s_{V,\alpha}^-+
L_{V,\alpha}^-(\xi_i,w_i,n_{T,i})\},
\end{aligned}
\tag{30}
$$
$$
\begin{aligned}
H_{d,i,\alpha}^+&=\mathcal T_{d,i}
-a_i^3\{R_i s_{V,\alpha}^+
L_{V,\alpha}^+(\xi_i,w_i,n_{R,i})\},\\
H_{e,i,\alpha}^+&=\mathcal T_{e,i}
+a_i^3\{T_i s_{V,\alpha}^+
L_{V,\alpha}^+(\xi_i,w_i,n_{T,i})\}.
\end{aligned}
\tag{31}
$$
所有参考量使用实际 $\xi_i,w_i$。右换端消耗的是整个真实
$\mathcal T_{d/e,i}$，不是另选常数。

在同一新母库上、满足 R429 明写的共同合法物理窗口及同端口实施前提时，消费其 actual whole $E$ 与共同有限自然截面，
这些 totals 可以同时为零；(30)—(31)便成为全部内部点的真实共同表。
仍未证明该表的原成本/响应像覆盖全部目标。

## 10. Euler current 只能在原 universal 自然核范围使用

R405 的局部 current 需要
$$
V\in\ker(E,\Lambda_{\rm all}).
\tag{32}
$$
它从对全部紧 u、任意三矩参数 n 的自然恒等，
推出局部三次密度 $\mathcal D_{V,n}$ 的 Euler 导数为零，
再由明确齐次 current 得
$$
\int_{\ell_u}^{x}u'\mathcal U_{V,n}(u)''
=\mathcal J_{V,n}(x;u).
\tag{33}
$$
本稿没有将 R429 的有限自然查询零升级为这个 universal 恒等。

对于原满足(32)的 signed 类，特别是已证的
$\mathcal R\cap\ker E$ 响应列，(27)现使(33)同时可用于全部实际 A 根。
原消 self 组合
$$
C_{i,\alpha}^{\pm}
=R_iH_{e,i,\alpha}^{\pm}+T_iH_{d,i,\alpha}^{\pm}
$$
准确具有
$$
\boxed{
C_{i,\alpha}^{\pm}
=a_i^3\sum_{\ell=0}^{6}\sum_{j=0}^2
c_{\alpha,\pm,\ell j}(V;w_i)
\,\xi_i^\ell(n_i)_j,\quad
n_i=T_i n_{R,i}-R_i n_{T,i}.
}
\tag{34}
$$
这是原 Euler current 在固定共同 jets 上的值；不任意指定其系数。

每个固定实际宽度、每个镜点对至多有42个显示生成位置。
若不同宽度集合为 $\mathscr W$，总上界为
$42m|\mathscr W|$；不称该数为秩。
保持 n 为外参数时位置次数至多六；
整个真实布局平移时 n 仍按原三矩三角法输运，所以完整次数可到八。
没有冻结 suffix 后误报完整阶数。

一般 actual 成本即便已 whole $E=0$、有限 $\mathcal A=0$，也不能据此直接使用(33)。
应使用(30)—(31)的完整 cap 积分表，并把实际 totals 按 R429 支付。
它的响应校正列若属于(32)，可以用(34)描述；
这两种范围在同一线性控制问题中可以同时保留，不能互相替代。

## 11. 解析限制、初选次序与真正未付的部分

若两个最终母都在整个连通 $(-1,1)$ 实解析，并在一个非空开 cap 相同，则实解析唯一性迫它们处处相同。因此不能在这个更强类中一边保共同开 cap、一边作非平凡不同母的紧支撑控制。
本构造的最终母在中心仅为 $C^\infty$，这是 R412 已明示允许的类；
平端及所有外部退化邻域仍是同一个解析 $u_{\rm a}$，没有丢掉原端 germ 条件。

无循环次序是：

1. 从 R411/R412 的 q 正则/simple 起点取得第2节解析母，固定中心负 A 区间和全部外根；
2. 用解析 Euler 局部秩引理固定中心四正常方向，并按原来源冻结所有真实位置、宽度、复制和平移布局；
3. 在同一个外 cap 固定、q=0 图册上，使用这同一实际布局选择 restricted 最大 $F^\star$ minor 与原十九 minor，产生新的 $u_0$ 和共同数据；
4. 冻结原列中随共同母数据而定的正归一因子，选有限正幅盒；
5. 用(16)、(22)在一个充分大的有限 N 上取得同一十九根，并保(18)的实际非正高项；
6. 冻结新 profiles、根、所有实际 suffix 和查询，再消费 R429 或后继的同一个实际控制模块。

本稿没有保持某个旧数值纤维，没有把 R410 一对根和 R412 四约束分别支付后拼接，也没有重新计算十九目标的原秩或原科学值。

完成的是(2)与其原函数后果(26)、(30)—(34)：
同一完整四约束/共同 $D,E_5$/十九根的库，全部内部 A 点都有共同外 cap 和共同 jets，且原同矩连通路径精确存在。
仍须求同一个实际成本在这些原 partial 目标中的真实像，并支付全部内部通量、平台与 k 值闭合及十三行同规范。
共同表是合法接口，不是自由目标矩阵。
