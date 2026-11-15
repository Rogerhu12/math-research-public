# R405：共同外区的十九根、跨包真实局部式与全部内部残差的公共 current

日期：2026-11-15。**纸面原式证明；没有执行研究积分、符号程序、profile 零点计数、数值秩或人工测试。**

[R403](R403-one-pair-degeneracies-and-nineteen-exact-rational-targets-by-concentration.md) 已把每个实际微包的内部 $A_f$ 零点减为一对，同时支付原十九个完整有理目标。本稿作一个独立的初选变体：全部形状修改与低阶纠正都限制在固定内区，使每个最终包的两个退化点及整个外区与同一个参考函数**完全相同**。

这个变体不要求活动区内部处处解析；内区的 $A_f$ 始终严格负，端 collar 仍为原解析指数平零形状。原完整 $\mathcal F_{\rm rat}$ 定义、十九目标、全部复制、三矩与有序接口仍保持。使用的是固定 affine 子空间上的真最大秩，不冒称它等于原全域最大秩，也不保持旧冻结母函数的数据。

随后从 R292/R56 给出一个新准确身份：真实跨包 period 可以写成局部二次式加**仅三个**原二次 primitives。whole-$E=0$ 使其二阶导数成为局部表达；再在真正的 signed $\ker(E,\Lambda_{\rm all})$ 上，由完整有序 $3+2$ 恒等得到一个显式三次局部 current。因此所有实际镜点的两通道残差都使用同一个有限系数表。

这不证明同包 self $S_u''$ 只由外区和三矩决定，不支付所有自然通量的实际 joint，也不把现有四维响应像扩大为任意多个包上的满射。

直接来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md)、[R324](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md)、[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md)、[R397](R397-actual-unsubtracted-internal-fluxes-and-the-ordered-two-period-remainder.md)、[R399](R399-new-whole-E-natural-kernel-and-four-ordered-internal-period-controls.md)及 [R401](R401-one-packet-mirror-degeneracies-and-four-complete-period-flux-controls.md)。

## 1. 共同外区的新母函数选择

固定
$$
u_{\rm ext}(y)=\psi_3(y)=e^{-3/(1-y^2)},\quad |y|<1,
\qquad u_{\rm ext}=0\quad |y|\ge1.
$$
R403(4)—(5)已证明
$$
\mathcal A(u_{\rm ext})
=\frac{72u_{\rm ext}^2}{(1-y^2)^8}
(27y^8+102y^6-46y^4-10y^2-1)
$$
恰在 $\pm a_*$ 有简单零点，其中 $1/\sqrt2<a_*<1$；在 $|y|\le1/2$ 严格负。$u_{\rm ext}'$ 仅在中心有一个简单零点。

令 $\mathscr B$ 为支撑于 $[-1/2,1/2]$、在这两个端点的零至二阶 jets 均为零的偶 $C^2$ Banach 空间。初选对象属于固定 affine 空间
$$
u_{\rm ext}+\mathscr B.
\tag{1}
$$
最终只取其中的光滑紧扰动。于是所有最终形状在
$$
\{1/2\le |y|<1\}
\tag{2}
$$
上与 $u_{\rm ext}$ 一字相同。

仍用原整映射 $\mathcal F_{\rm rat}$，令
$$
r_{\rm in}
=\max_{u\in u_{\rm ext}+\mathscr B}
\operatorname{rank}\left(D\mathcal F_{\rm rat}(u)|_{\mathscr B}\right).
\tag{3}
$$
这是真正的**限制微分秩**。本文不声称它等于原全域的最大秩；后续全部扰动和纠正也都在 $\mathscr B$ 中，所以(3)正是需要的对象。

光滑偶紧扰动在 $\mathscr B$ 中 $C^2$ 稠密：先在 $\pm1/2$ 附近 cutoff，再作内区光滑逼近。原端二阶 jets 为零保证 cutoff 的 $C^2$ 误差趋零。因此(3)的非零最大 minor 可由一个光滑 $v_{\rm F}\in\mathscr B$ 和固定光滑方向
$$
e_1,\ldots,e_{r_{\rm in}}\in C_c^\infty((-1/2,1/2))_{\rm even}
\tag{4}
$$
实现。若 $r_{\rm in}=0$，有限纠正为空。

另一方面，R403 的十九点对见证全可取在
$J=(1/8,1/4)$。在这些有限个不同正点，用局部光滑偶 Hermite 函数可任意指定二阶 jets，仍属于(1)。因此每个原十九阶 principal minor 在(1)上都不恒零。

这些固定 minor 沿有限维光滑母方向是多项式。把各自的有限见证合在
$$
u_{\mathbf s}=u_{\rm ext}+\sum_\nu s_\nu v_\nu,\qquad
v_\nu\in C_c^\infty((-1/2,1/2))_{\rm even}
\tag{5}
$$
中，其非零多项式的乘积仍不恒零。可以在任意小的 $\mathbf s=0$ 邻域中同时使全部所需 minor 非零。取参数足够小于 $C^4$ 范数，得到共同母包
$$
u_0=u_{\rm ext}+v_0
\tag{6}
$$
严格正、严格单峰，内区 $\mathcal A(u_0)<0$，并具有(3)的最大限制秩及十九个真实主方向。

外区(2)完全未变；故其两个退化点准确还是 $\pm a_*$，不是仅仅靠近这两个点。所固定的新纤维值是 $\mathcal F_{\rm rat}(u_0)$，不是旧圆的数据。

## 2. 保共同外区的符号保护脉冲与有限十九根

取一个固定非负偶 cutoff $\chi$，
$$
\chi=1\quad(|y|\le3/8),\qquad
\operatorname{supp}\chi\subset(-1/2,1/2).
$$
沿 R403 定义
$$
g_{N,b}(y)=\sqrt N
\{e^{-N^2(y-b)^2}-e^{-N^2(y+b)^2}\},\qquad b\in J,
$$
以及 $\zeta_{N,b}'''=g_{N,b}$、零点处前三初值为零的偶原函数。现在使用真实紧扰动
$$
w_{N,b}=\chi\,u_{\rm ext}\,\zeta_{N,b}.
\tag{7}
$$
其 $C^2$ 范数为 $O(N^{-1/2})$，且
$$
w_{N,b}'''=\chi\,u_{\rm ext}\,g_{N,b}+O(N^{-1/2}).
\tag{8}
$$
这里所有 cutoff 导数只乘 $\zeta,\zeta',\zeta''$，因而属于显示误差；没有把 cutoff 放进最高脉冲后另丢一个大项。

逐基本包用(4)纠正：
$$
u_{i,N,z}=u_0+z_iw_{N,b_i}
+\sum_\ell c_{i\ell,N}(z_i)e_\ell,\qquad
\mathcal F_{\rm rat}(u_{i,N,z})=\mathcal F_{\rm rat}(u_0).
\tag{9}
$$
在限制空间(1)中，所选 $r_{\rm in}$ 行在邻域独立，而整限制映射的秩不超过 $r_{\rm in}$。所以只解这些坐标便保持整个 $\mathcal F_{\rm rat}$。对固定有限幅度盒，
$$
c_{i\ell,N},\quad\partial_{z_i}c_{i\ell,N}
=O(N^{-1/2})
\tag{10}
$$
且有限纠正方向的 $C^4$ 误差同阶。

完整十九量的准确 $t=u'''$ 二次分裂、全部真实 $C^2$ 余项及点对 $C^1$ 极限沿 R403 §§7—9 原样适用；(7)在两集中点等于未 cutoff 的扰动。原十二交替位置、真实复制权及十九阶 minor 因而给一个有限 $N$ 的准确根
$$
\mathcal V_{19}=0
\tag{11}
$$
于固定严格正幅盒内。不是只对主项求根。

内区的高项仍须合写为实际
$$
6u_{i,N}'\,z_i\chi u_{\rm ext}g_{N,b_i}\le0.
$$
其余误差为 $O(N^{-1/2})$。相对 prefactor 在内区 $C^2$ 小，故 $u_{i,N}'$ 仍与 $y$ 反号；内区 $\mathcal A$ 保持严格负。外区则准确相同，不需用绝对范数控制平端的微小量。

因此每个最终形状满足
$$
\boxed{
u_i=u_{\rm ext}\quad(|y|\ge1/2),\qquad
\mathcal A(u_i)^{-1}(0)\cap(-1,1)=\{-a_*,a_*\},
}
\tag{12}
$$
两个根简单，$u_i'$ 只有中心简单零点。每个包的全部实际副本仍同步改变，(9)逐包保持真实三矩及原有序接口。

本稿的活动内区可以非解析，但那里没有 $A_f$ 零点，且除中心外 $f'$ 不为零。R394 的有限内部核证明只用这些事实和光滑匹配，不需要在一个没有退化的开段上额外假设解析。端 collar 仍准确是 $\psi_3$，所以原解析零端证明继续保留其真实累计常数后使用。本文不把整个活动区重新称为解析类。

## 3. 两种结论的条件必须分开

以下 profiles 已由 §§1—2 固定。把实际幅度全部吸收入 $a_i,b_i$，保留每个实际正宽 $w_i$，写
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,\quad a_i\ne0.
\tag{13}
$$
这里 $u_i(x)=U_i((x-\xi_i)/w_i)$，$U_i$ 是 §§1—2 的最终母坐标形状。所有 $w_i>0$ 都是原完整库已选定的真实数值，本文不假定它们相同，也不将它们作为新的控制变量。

关于 geometry/cost，先采用实际或真实有限线性组合的条件
$$
M=0,\qquad T=\tau_{\rm hook}\mathfrak H,\quad\tau_{\rm hook}\ne0,
\qquad E(V)=(\pi V,\mathcal QV)=0.
\tag{14}
$$
它不是由(11)继承的旧几何结论。若消费实际控制，必须按相应原定理在这些新 profiles 冻结后重新支付。

只有在 §§8—10 的 current 结论中再加入
$$
\Lambda_u(V)=0\quad\text{对同一合法区间内的每个真实紧 }u.
\tag{15}
$$
两个固定自然读出为零不够；也不把 $\pi V=0$ 当成(15)。对原响应子空间 $\mathcal R\cap\ker E$，R389 给(15)；对一般实际 $U$ 成员，本文没有构造这个全联合背景。

## 4. 真实右包的三矩与完整跨包第三场

令
$$
\mu(u)=\left(\int r^2,\int xr^2,
 \int(x^2r^2+2p^2)\right),\qquad p=u',\ r=u'',\ t=u'''.
$$
对外包 $u$ 右方的一个包，其二阶左尾只依赖
$n=(n_0,n_1,n_2)=\mu(v)$。沿 R292 用 $\beta=\beta_n(s,x)$、$\tau=\tau_n(s)$ 表示该真实尾的第三恢复系数。这里的 $\tau_n$ 不同于整几何的 $\tau_{\rm hook}$。

$\beta_n$ 是二次 $x$ 多项式，$\beta_n,\tau_n$ 对 $n$ 线性，并保留同一个真实 $s$ 起点与全部累计 history。写
$$
e=hx+d,\qquad Q=1+e^2,\qquad d=h\omega-k.
$$
R292 的完整局部交叉场给
$$
W_C=\beta p-\beta' u,
$$
$$
A_C=\left(\frac\beta2+\frac{\tau Q}{8h^2}\right)r
-\frac{\tau e}{4h}p
+\left(-\frac{\beta''}2+\frac\tau4\right)u,
$$
$$
A_C'=\left(\frac\beta2+\frac{\tau Q}{8h^2}\right)t
+\frac{\beta'}2r-\frac{\beta''}2p,
$$
$$
A_C-W_C'=\left(-\frac\beta2+\frac{\tau Q}{8h^2}\right)r
-\frac{\tau e}{4h}p+
\left(\frac{\beta''}2+\frac\tau4\right)u .
\tag{16}
$$
其分子为 $(A_C,zP_C+B_C,eA_C-hW_C)$；中间分量按 R292(16)为一个仅含 $u,p$ 的原局部式。没有把内包的真实尾改成零。

令
$$
I_n(u)=V_{Y_u,x}\cdot V_{C_n,x}.
$$
由 $V_{Y_u}=(-p/2,0,hu-ep/2)$，
$$
I_n(u)
=\frac12\{(hep-Qr)A_C'
+h(hp-er)(A_C-W_C')\}.
\tag{17}
$$

## 5. 一个保全部右端项的准确密度原函数

定义
$$
A_\beta=he\beta-\frac Q2\beta',
$$
$$
B_\beta=he\beta\,pr-\frac{Q\beta}2r^2
+\frac{Q\beta''-2h^2\beta}2p^2
-he\beta''up+h^2\beta''u^2,
$$
$$
B_\tau=heQ\,pr-\frac{Q^2}2r^2
-2h^3e\,up+2h^4u^2 .
\tag{18}
$$
将(16)代入(17)，仅用 $e'=h,Q'=2he,\beta'''=0$，逐项得到
$$
\boxed{
I_n(u)=\frac14(A_\beta r^2+A_\beta''p^2)
+\partial_x\left(\frac{B_\beta}4+
\frac{\tau B_\tau}{16h^2}\right).
}
\tag{19}
$$

可直接核其两部分。$\beta$ 部分先将 $pt=(pr)'-r^2$、$rt=(r^2)'/2$ 降阶；余下 $pr$ 和 $ur$ 分部后，$r^2,p^2$ 的系数分别恰为 $A_\beta,A_\beta''$。$\tau$ 部分中的 $r^2,pr,p^2$ 余项逐对相消，剩余 $4h^4up=(2h^4u^2)'$，正是 $B_\tau$。

$A_\beta$ 的三次项消失，令
$$
A_\beta(x)=\sum_{j=0}^2 a_{\beta,j}x^j.
$$
置三个原 primitives
$$
J_j(u)(x)=\int_x^{r_*}
\{y^j(u''(y))^2+2\mathbf1_{j=2}(u'(y))^2\}\,dy.
\tag{20}
$$
则 $(J_0,J_1,J_2)$ 的左值是 $\mu(u)$。R56 真 $P$ 是 $J I_n/(2h)$；(18)在原右 collar 为零。因此
$$
\boxed{
P_n(u)
=-\frac{B_\beta}{8h}-\frac{\tau B_\tau}{32h^3}
+\frac1{8h}\sum_{j=0}^2a_{\beta,j}J_j(u).
}
\tag{21}
$$
这是完整右锚身份，未设置任何新的左常数。

## 6. 整个跨包 period 的局部加三 primitive 形式

记原完整交叉周期
$$
Q_{V,n}(u)=\mathscr P H(Y_u,C_n(u)).
$$
R56(5)中的所有量保持周期。对原 $s$ 总导数分部而不删基准，得
$$
Q_{V,n}(u)=\int_{\rm path}
\left\{\frac{T_s}{2h^2}
+\left(\frac{K_0}{z}+\left(\frac\gamma{h^2}\right)_s\right)B
+(K_0+\lambda_s)P_n(u)\right\}ds,
\tag{22}
$$
其中 $B=V_Y\cdot V_C/(2h)$，
$K_0/z=kz-(k^2+1)/h$ 为原多项式。式(21)代入后得到
$$
\boxed{
Q_{V,n}(u)(x)
=L_{V,n}(x,u,p,r)+\sum_{j=0}^2m_{V,j}(x,n)J_j(u)(x),
}
\tag{23}
$$
$$
L_{V,n}
=\int_{\rm path}\left\{
\frac{T_s}{2h^2}
+\left(\frac{K_0}{z}+\left(\frac\gamma{h^2}\right)_s\right)B
-(K_0+\lambda_s)
\left(\frac{B_\beta}{8h}+\frac{\tau B_\tau}{32h^3}\right)
\right\}ds,
$$
$$
m_{V,j}(x,n)=\frac18\int_{\rm path}
\frac{K_0+\lambda_s}{h}a_{\beta,j}(n)\,ds .
\tag{24}
$$
这些是真实几何/history 的确定值，不是独立可选系数。

式(23)有以下准确阶数：

- $L_{V,n}$ 对 $(u,p,r)$ 齐次二次，关于 $n$ 线性；系数关于 $x$ 的次数至多六。
- 每个 $m_{V,j}(x,n)$ 关于 $x$ 次数至多二，关于 $n$ 线性。

次数界可逐原分子支付：$V_Y$ 的位置次数至多一，$V_C$ 至多三；故 $T_s,B$ 至多四。$B_\beta,B_\tau$ 至多四；乘 $K_0+\lambda_s$ 至多二后至多六。$s$ 导数不增加 $x$ 次数，R56 已准确消掉全部 $1/z$ 项，所以这里没有隐藏的非多项式平移系数。

在 outer 包左方，局部项为零、$J_j=\mu_j(u)$，故(23)的左尾正是
$$
\sum_jm_{V,j}(x,n)\mu_j(u),
\tag{25}
$$
与 R292(22)—(23)的整个三项平台矩阵相同。

若两个 outer profiles 在某个左外 cap 相同且三矩相同，则(20)在该 cap 相同，故它们的整个 $Q_{V,n}$ 在该 cap 相同。在右外 cap，(20)本来只积分该 cap，结论更直接。这里说的是(23)的**跨包**函数；没有将同包 $S_u$ 代入这个公式。

## 7. whole self 如何准确删除唯一非局部二阶项

R389 的 whole pure 极化给
$$
U_{V,u,v}=4Q_{V,\mu(v)}(u)
$$
作为整个有序 self 交叉函数。whole self $\mathcal QV=0$ 使其原左二次系数对每一对不交真实 $u,v$ 为零。

在一个固定右开区间取三个同形、同宽但不同中心的实包，它们的矩向量是
$$
m(1,c_j,c_j^2+\nu),\qquad j=1,2,3,
$$
其行列式为非零的中心 Vandermonde 倍数。左侧矩像同样张成三维。因此(25)的二次系数整个矩阵为零，即
$$
\boxed{m_{V,j}''(x,n)=0
\quad\text{对每个 }j\text{ 和任意 }n\in\mathbb R^3.}
\tag{26}
$$
这只消二次尾，没有消 $m_{V,j}$ 的两个仿射系数。

令
$$
j_j(u)=x^jr^2+2\mathbf1_{j=2}p^2.
$$
由(23)、(26)，原有序函数
$\mathcal U_{V,n}(u):=4Q_{V,n}(u)$ 满足
$$
\boxed{
\mathcal U_{V,n}(u)''
=4\left[
D_x^2L_{V,n}
-2\sum_jm_{V,j}'j_j(u)
-\sum_jm_{V,j}D_xj_j(u)
\right].
}
\tag{27}
$$
右侧是真正的局部二次 jet 多项式，最高只到 $u^{(4)}$。若没有 whole self 条件，必须再保
$4\sum_jm_{V,j}''J_j(u)$；不能仅凭 cap 数据或一个旧平台判据删除它。

式(27)对 signed 成本线性延拓。对同一个 pure-zero 成本的两种路径表示，R389 的三个实际右矩基使 $\mathcal U_{V,n}$ 相同；(25)确定 $m$，再由(23)确定局部式。因此这里没有选择一个更有利的 history 表示。

## 8. 从全部自然通量零得到一个明确的局部 current

本节额外使用(15)，其量化不能缩为当前有限包上的查询。

固定任意紧 $u$，在其右侧取任意真实紧 $v$。由于 $\pi V=0$，R389 的完整 natural→raw 步骤及有序 $3+2$ 系数给
$$
[a^3b^2]\Lambda_{au+bv}(V)
=\int u'''\,\mathcal U_{V,\mu(v)}(u)
=\int u'\,\mathcal U_{V,\mu(v)}(u)''.
\tag{28}
$$
两次 $x$ 分部只用紧 outer 的真实零 jets。由(15)，左边为零。三个实际右包的矩张成 $\mathbb R^3$，且 $\mathcal U_{V,n}$ 对 $n$ 线性，所以
$$
\boxed{
\int \mathcal D_{V,n}(u)=0
\quad\text{对全部紧 }u\text{ 和任意 }n\in\mathbb R^3,
\qquad
\mathcal D_{V,n}(u)=u'\mathcal U_{V,n}(u)''.
}
\tag{29}
$$
这里不声称任意 $n$ 是一个正实包的矩，只使用三个真实包及线性延拓。辅助包可以在原右 collar 前的非空间隙内选择；不移动固定研究圆，也不把 universal 输入极化当成新的合法轨道。

由(27)，$\mathcal D_{V,n}$ 是关于
$u,u',\ldots,u^{(4)}$ 的局部三次齐次多项式，系数关于 $x$ 次数至多六、关于 $n$ 线性。(29)对所有紧变分成立，故其 Euler 多项式准确为零：
$$
\mathscr E_u(\mathcal D_{V,n})
=\sum_{k=0}^4(-D_x)^k
\frac{\partial\mathcal D_{V,n}}{\partial u^{(k)}}=0 .
\tag{30}
$$
取三次 Euler 齐次恒等式并逐项分部，得到明确 current
$$
\boxed{
\mathcal J_{V,n}
=\frac13\sum_{k=1}^4\sum_{\alpha=0}^{k-1}
u^{(k-1-\alpha)}(-D_x)^\alpha
\left(\frac{\partial\mathcal D_{V,n}}{\partial u^{(k)}}\right),
\qquad
D_x\mathcal J_{V,n}=\mathcal D_{V,n}.
}
\tag{31}
$$
准确依据是
$$
3\mathcal D_{V,n}
=u\,\mathscr E_u(\mathcal D_{V,n})+
D_x(3\mathcal J_{V,n}).
$$
$D_x$ 对 $x$ 和 profile jets 求真实总导数；$n$ 作为外参数，不在此被微分。

(31)最高可保守取到 $u^{(7)}$，关于 $x$ 的次数仍至多六，关于 $n$ 线性。它三次齐次，故在左右零 collar 为零，不含另选的积分常数。因此
$$
\boxed{
\int_{\ell_u}^{x}u'(t)\mathcal U_{V,n}(u)''(t)\,dt
=\mathcal J_{V,n}(x;u).
}
\tag{32}
$$
这是完整 partial 通量身份，不是只说明其总积分为零。

## 9. 所有实际镜点残差使用同一张有限表

仍在(14)下，按 R397 定义两个未扣平台的真实内部查询
$$
H_{d,i}^{\pm}=\int_{\ell_i}^{x_i^\pm}f'V_d'',\qquad
H_{e,i}^{\pm}=\int_{\ell_i}^{x_i^\pm}f'V_e''.
$$
whole self 已使其他 outer 包在当前包上只留下仿射项，其二阶导数为零。令
$$
n_i=\sum_{j>i}(T_iR_j-R_iT_j)\mu(u_j).
\tag{33}
$$
这是原完整有序 suffix，含所有真实副本及幅权，不能换成一个裸 cell 的均值。

R389/R397 的原全函数分解准确给
$$
\boxed{
C_i^\pm:=R_iH_{e,i}^{\pm}+T_iH_{d,i}^{\pm}
=a_i^3\int_{\ell_i}^{x_i^\pm}
u_i'\mathcal U_{V,n_i}(u_i)''.
}
\tag{34}
$$
自己的 $S_i$ 在这个组合中消去；没有把它单独宣布为局部。

在各自真实母坐标中，
$$
x_i^\pm=\xi_i\pm w_i a_*,\qquad
u_i^{(k)}(x_i^\pm)=w_i^{-k}u_{\rm ext}^{(k)}(\pm a_*).
$$
由(12)，这些点附近的**所有** jets 都准确按此式给出，不随十九根或内区纠正改变。若同时使用(15)，把(32)代入(34)，得到
$$
\boxed{
C_i^\pm
=a_i^3\sum_{\ell=0}^{6}\sum_{j=0}^2
c_{\pm,\ell j}(V;w_i)\,\xi_i^\ell(n_i)_j.
}
\tag{35}
$$
相同实际宽度的包共用这两组系数；一般情形保留显示的 $w_i$。它们是(31)在上述缩放后固定镜点 jets 上的明确线性读出，并非任意指定的数字。

对每一个固定实际宽度，每侧至多 $7\times3=21$ 个生成位置。设原有限库中的不同实际宽度集合为 $\mathscr W$，则总生成上界为 $42|\mathscr W|$；本文不称此上界为秩。真实输入 $(\xi_i,w_i,n_i)$ 不能独立指定，必须使用原库与(33)。

具体地，母坐标三矩保持为 $m(1,0,\nu)$ 时，实际
$$
\mu(u_i)=w_i^{-3}m(1,\xi_i,\xi_i^2+w_i^2\nu).
$$
所以原宽度、真实方差和所有幅权都进入(33)，没有把不同宽度的包当成同一个点质量。

次数界同样必须区分：式(35)在保持 $n$ 为外参数时对 $\xi$ 次数至多六；若整个真实布局平移 $d$，其矩向量还要按
$$
(n_0,n_1,n_2)\mapsto
(n_0,n_1+dn_0,n_2+2dn_1+d^2n_0)
\tag{36}
$$
输运。因此共同平移后的完整读出可到次数八，不能把真实 suffix 冻结后误报成六次。全部复制正权、翻号和当前顺序都已经在 $a_i,R_i,T_i,n_i$ 中保留。

式(35)适用于整个 signed $\ker(E,\Lambda_{\rm all})$ 的真实线性类，特别适用于 R399/R401 的响应列；它不把这些响应列的像直接认成整个 $42|\mathscr W|$ 个生成位置。

## 10. actual 只付 whole $E$ 时，右镜点仍保哪一项

若当前实际几何只有(14)，而没有(15)，不能使用(31)—(35)删除有序总通量。

由(27)及共同外区，可定义两个真实 cap 量
$$
L_V^-(\xi,w,n)=\int_{\xi-w}^{\xi-wa_*}
v_{\xi,w}'(x)\,
\mathcal U_{V,n}(v_{\xi,w})''(x)\,dx,
$$
$$
L_V^+(\xi,w,n)=\int_{\xi+wa_*}^{\xi+w}
v_{\xi,w}'(x)\,
\mathcal U_{V,n}(v_{\xi,w})''(x)\,dx,\qquad
v_{\xi,w}(x)=u_{\rm ext}((x-\xi)/w).
\tag{37}
$$
这里(27)使实际 integrand 只用 cap，写整个参考函数不改变该区间的值。$L^\pm$ 在每个固定 $w$ 下对 $\xi$ 的次数至多六，对 $n$ 线性。

保留 R389 的真正 ordered 总通量
$$
\mathcal A_{V,u}(n)=\int u'\mathcal U_{V,n}(u)''
=\int u'''\mathcal U_{V,n}(u).
\tag{38}
$$
则(34)的完整两侧式为
$$
\boxed{
C_i^-=a_i^3L_V^-(\xi_i,w_i,n_i),\qquad
C_i^+=a_i^3\{\mathcal A_{V,u_i}(n_i)-L_V^+(\xi_i,w_i,n_i)\}.
}
\tag{39}
$$
右侧换端恰花掉(38)。内区形状即使具有相同 $\mathcal F_{\rm rat}$ 和三矩，也不能据此将 $\mathcal A_{V,u_i}$ 默认为零或相同。

两个固定自然读出的实际控制没有证明全部(38)为零。R396 的 actual $(P_LE,\mathcal A,\text{selected partial})$ 与 R401 的 actual whole-$E$ 加四 partial 仍是不同结论；(39)不拼接它们的基准成本。

## 11. 尚欠的同包项与真正的控制映射

同包项始终是
$$
S_u=V(u^2,0)=4\mathscr P H(Y_u,C(u;u^2))
$$
于 whole pure 零背景。与第4节不同，内二阶场在自己的包上不是真实仿射尾，故不能把(16)用于它。本稿没有证明
$$
S_u''\big|_{\rm cap}
\quad\text{只由 cap jets 与 }\mu(u)\text{ 决定}.
$$
其完整自 history 继续进入 $H_d,H_e$ 中未被(34)消掉的另一通道。共同外区不自动抹去这个代价。

原响应模块的下一准确线性接口现在是：把 R399/R401 及其他已证 whole-$E$、全自然核响应送入(35)的共同系数表，取其**真实像**，再与实际目标的(39)比较。未证明这张图满射前，不能从指定四点的 Vandermonde 扩成全部包上的自由控制。

若背景尚未实际支付全自然条件，还须同时保(38)的原有序目标；若 whole-$E$ 也未付，R397 的原平台二次项还要先加回。所有这些条件属于同一最终 profiles 和同一实际成本，不能各换一个几何后拼接。

## 12. 完成的范围

本稿完成了三条可以直接使用的原式结论：

- 同一个新的限制 affine 空间中，完整低阶纤维与原十九根可同时保持，并使全部实际包在外区准确相同、每包只有原参考的一对简单退化点。
- 原跨包 period 有完整局部加三 primitive 形式(23)；whole self 正好删除其二阶导数中的唯一非局部部分，所有真实左仿射系数仍保留。
- 在真正的 signed $\ker(E,\Lambda_{\rm all})$ 上，完整有序自然恒等给显式 Euler current(31)，全部实际镜点残差由同一有限表(35)读出；没有多包各自独立的隐含自由参数。

actual 只有 whole-$E$ 时应使用(39)，保留右镜点的总通量。一个包的剩余 self 通道、所有包的实际响应像、全局平台仿射与 $k$ 值闭合、十三行同规范问题均继续保留；本稿不把共同外区或有限生成表冒作这些条件的实际联合支付。
