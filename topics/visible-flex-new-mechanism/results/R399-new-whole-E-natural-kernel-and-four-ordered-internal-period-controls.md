# R399：完整纯、自项与全部自然通量核中的新四维双 period 内部残差

日期：2026-11-15。**只读已发表原式并作纸面证明；没有执行符号程序、求积、序列枚举、数值或人工测试。**

[R397](R397-actual-unsubtracted-internal-fluxes-and-the-ordered-two-period-remainder.md) 区分了真实未扣平台的两个内部通量，也证明旧十一维局部轨道看不见一个明确的两通道残差。本稿给出能改变该残差的真实响应：其 universal pure、完整 universal self 和全部自然总通量同时为零，但在原 $A_f=0$ 的内部点，部分通量不含 $A_f$ 因子。

在当前负布局的一个明确微包及其实际十二副本上，新响应的残差像准确为次数至多三的多项式。因此最多四个对应点的第二通道可与旧最多十一个第一通道联合控制。文末分别给出 whole $E$ 的实际版本、以及保原两条固定自然读出的响应分量版本；两种实际结论不拼成一个未经证明的 whole $E+\Lambda_{\rm all}$ 截面。

## 1. 原完整第三核中的新方向

记正右积分
$$
(Jv)(x)=\int_x^{r_*}v(\xi)\,d\xi,\qquad DJ=-1.
$$
所有 profiles 紧支撑于同一个合法窗口；全部原左尾与右端三个常数保留。采用
[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md) 的完整第三核 $\mathfrak J$，以及
[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md) 的 $\chi_{32},\chi_{34}$。定义
$$
\boxed{\tau_*:=64(\chi_{34}-3\chi_{32})-\frac12\mathfrak J.}
\tag{1}
$$
三项均属于原 $Z=\ker\Delta$，故 $\Delta\tau_*=0$。

对真实紧包 $u$，写
$$
p=u',\qquad r=u'',\qquad t=u''',
\qquad K_u^*(w)=\tau_*(w;u,u).
$$
原局部算子记为
$$
D^3K_u^*(w)=\mathscr A_u^*w,\qquad
\mathscr A=D^2(aD^2)+D(bD)+c,\qquad d=a''+b .
$$
其中 $d$ 是整个算子的 $D^2$ 系数，不是 $b$。R261§3 与
[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)(8),(12)
直接给下表：
$$
\begin{array}{c|ccc}
 &a&d&c\\ \hline
64(\chi_{34}-3\chi_{32})
&-2ur&-4u\,u^{(4)}-2pt&c_{\mathfrak J}/2\\
\mathfrak J/2
&-2(p^2+ur)&-4(pt+u\,u^{(4)})&c_{\mathfrak J}/2 .
\end{array}
\tag{2}
$$
因此完整相减为
$$
\boxed{
a_*=2p^2,\qquad d_*=2pt,\qquad c_*=0,\qquad
b_*=-4r^2-2pt.}
\tag{3}
$$
这是整个原算子的身份，不只保最高导数。特别
$$
\boxed{\mathscr A_u^*
=D^2(2p^2D^2)-D\{(4r^2+2pt)D\}.}
\tag{4}
$$
其自伴性、$\mathscr A_u^*u=0$ 也可从(4)逐项核对。若 $u\ne0$，$2p^2$ 不恒零，所以这个完整第三方向非零。

## 2. 真右常数与准确部分通量

R261 给 $K=-J^3\mathscr A$。由于(4)是一个完整导数，且其局部系数在右 collar 全零，
$$
\boxed{
(K_u^*(w))''
=(2p^2w'')'-(4r^2+2pt)w'.}
\tag{5}
$$
(5)允许 $w$ 有真实左二次尾；没有把 $K$ 或 $K'$ 的左仿射常数删掉。

直接乘 $p$ 并用乘法法则：
$$
p(K_u^*(w))''
=\bigl[\,2p^2(pw''-rw')\,\bigr]'.
$$
令 $\ell$ 为该包的真实左零 collar，则
$$
\boxed{
\int_\ell^x p(K_u^*(w))''
=2p(x)^2\{p(x)w''(x)-r(x)w'(x)\}.}
\tag{6}
$$
左端为零只因 $u$ 的真实平零 jets，而非因 $w$ 左紧。

原固定第三 hook 的退化系数是
$$
A_u=6pt-2r^2.
$$
(6)与原 $L_u$ 的部分通量不同：在 $A_u(x)=0$ 而 $p(x)\ne0$ 时，右边通常非零。故不能将 $\tau_*$ 当作 $\mathfrak H$ 的倍数，或把其 period 输出免费视为合法 $L_f$ 的像。

## 3. 八个真实响应全部保持 whole $E$ 与 $\Lambda_{\rm all}$

对原八矩方向 $E\in E_8$，定义
$$
\mathcal R_E^*=\mathcal B_E(\tau_*).
\tag{7}
$$
R255(31)的完整响应为
$$
\mathcal R_E^*(f^2,\phi)
=2K_f^*\{\Phi_E(f^2-\phi^2)\}
 +4\Phi_E(\phi,K_f^*(\phi)).
\tag{8}
$$
因为 $\Delta\tau_*=0$，其 universal pure 为零。
[R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md)(36)
给完整 self：
$$
\mathfrak q_u(\mathcal R_E^*)
=-\frac14\int c_{*,u}\Phi_E(u,u)=0.
\tag{9}
$$
所以
$$
E(\mathcal R_E^*)=(\pi,\mathcal Q)(\mathcal R_E^*)=0
$$
是对所有真实紧 profiles 的完整身份。

全部自然通量也准确为零。这一步不需要把仅交换子子空间的某条结论扩大到新增 $\chi$。由 pure 零及
[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)
的实际右辅助包极化，natural 读出等于 raw self 收缩；于是
$$
\begin{aligned}
\Lambda_u(\mathcal R_E^*)
&=2\int u'''K_u^*(\Phi_E(u,u))\\
&=-2\int u\,\mathscr A_u^*(\Phi_E(u,u))\\
&=-2\int(\mathscr A_u^*u)\Phi_E(u,u)=0 .
\end{aligned}
\tag{10}
$$
紧 $u$ 与紧局部系数支付这些分部积分；$\Phi_E(u,u)$ 的原左尾仍保留。

结论为
$$
\boxed{\mathcal R_E^*\in
\mathcal R\cap\ker E\cap\ker\Lambda_{\rm all}.}
\tag{11}
$$
另一方面，(3)没有显式 $x$，真平移给 $N\tau_*=0$；其三次算子的真伸缩权为 $-3$。所以
$$
\mathscr M_*:=\operatorname{span}\{\mathcal R_E^*:E\in E_8\}
\tag{12}
$$
在原真实平移与正伸缩下稳定。其维数在本文不作无关的满八断言；下文只求一个明确查询像。

## 4. 当前 rank-one 圆上的真实有序残差

固定 R391 的实际不交微包
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i .
$$
对全部 $\tau\in Z$，原局部算子和右三常数给
$K_f^\tau(g)=0$：不同包的局部源为零，同包用
$K_{u_i}^\tau(u_i)=0$。因此(8)在当前圆上准确简化为
$$
\mathcal R_E^*(f^2,\phi_\theta)
=2K_f^*(\Phi_ED_\theta),\qquad
D_\theta=f^2-\phi_\theta^2.
\tag{13}
$$
第二个真实 history 项是在这里被完整身份支付，而非由“外支撑不交”删去。

沿 R397 定义
$$
\mathsf V_d=V(f^2,g),\qquad
\mathsf V_e=\frac12\partial_\theta
V(f^2,f\cos\theta+g\sin\theta)\big|_{\theta=0},
$$
$$
H_{b,j}(V)=\int_{\ell_i}^{x_j}f'\,\mathsf V_b'',\qquad
C_j(V)=R_iH_{e,j}(V)+T_iH_{d,j}(V).
\tag{14}
$$
对一般 V，(14)仍是 raw 线性查询；不先设其平台二次项或 pure 为零。

令 $\mu_k$ 是第 k 包的三个完整矩，且
$$
n_i=\sum_{k>i}(T_iR_k-R_iT_k)\mu_k.
\tag{15}
$$
在当前响应(7)上，左边包的二次输出在第 i 包为零，右边包则有原二次左尾 $p_E(\mu_k)$。本包自项在 $C_j$ 中准确相消。由(6),(13)得到
$$
\boxed{
C_j(\mathcal R_E^*)
=4a_i^3p_i(x_j)^2
\bigl[p_i(x_j)p_E(n_i)''(x_j)
-r_i(x_j)p_E(n_i)'(x_j)\bigr].}
\tag{16}
$$
此处 $p_i=u_i'$、$r_i=u_i''$；不能将它们误作含 $a_i$ 的 $f$ jets。

(5)还表明该响应的第二导数在零平台恒零。因此在这些新列上 raw 与扣平台的查询相同；这不改变 R397 对一般实际成本必须保平台项的规定。

## 5. 非零 suffix 的真实响应，及完整八尾表

按 R255 的 $P,R,S,L,U,V,T,Y$ 顺序，原左尾为
$$
\begin{array}{c|c}
E&p_E(n)\\ \hline
P&n_0\\
R&xn_0\\
S&n_1\\
L&-n_0x^2/4+n_2/4\\
U&xn_1+n_2/2\\
V&-n_1x^2/4\\
T&xn_2\\
Y&-n_2x^2/4 .
\end{array}
\tag{17}
$$
其中 $n_2$ 完整包含 $2\int u'^2$。L、U 的常数尾没有省略，虽它们在(16)的导数中消失。

令 $\mathscr D_E=p\,p_E''-r\,p_E'$。则
$$
\begin{array}{c|cccccccc}
E&P&R&S&L&U&V&T&Y\\ \hline
\mathscr D_E
&0&-rn_0&0&(xr-p)n_0/2
&-rn_1&(xr-p)n_1/2&-rn_2&(xr-p)n_2/2 .
\end{array}
\tag{18}
$$
因此只要 $n_i\ne0$、$p_i(x_j)\ne0$，至少一条(7)使 $C_j\ne0$。若 $r_i\ne0$，取对应非零 $n_k$ 的线性尾；若 $r_i=0$，取其二次尾。没有使用任意的积分常数或可独立指定的形状矩。

当 $n_i=0$ 时，本模块确实全盲。特别 R397 已付 first/last 完整 cell 边界点仍然属于该盲区，不能用本结论冒称那些点也新增一个自由通道。

## 6. 原负布局提供一个准确非零的 suffix

采用 [R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)(16)
的负布局：
$$
i=jK+k,\qquad R_i=r_j\in\{-B/2,8B\},\qquad
T_i=\epsilon_k\tau_j,\qquad
K=2^{11},\quad \tau_j>0.
$$
选一个完整八副本 cell 的最后副本，在其整个负布局末尾取倒数第二微包 i 和最后微包 i+1。
因为
$$
\epsilon_{K-2}=+1,\qquad\epsilon_{K-1}=-1,
$$
这两包满足
$$
R_i=R_{i+1}=r_j\ne0,\qquad
T_i=\tau_j,\quad T_{i+1}=-\tau_j .
$$
R397 已从实际八/十二/五块库及 R324/R391 的逐包矩保持证明：此 cell 后的全部完整 cells 的 R、T 加权三矩均为零。故在本副本的原归一中，
$$
\boxed{n_i=2r_j\tau_j\,\mu_{i+1}\ne0.}
\tag{19}
$$
最后一个不等式只用 $\mu_{0,i+1}=\int(u_{i+1}'')^2>0$。无须指定哪个17进制类是 high，也不使用“任意连续17点”之类不成立的编码断言。

真实共同幅度、g 翻号、平移与正伸缩均按完整矩变换输运(19)。R391 的同 $F_{\rm rat}$ 有限频率改形保每个基本包的全部三矩，并在其实际副本中同步使用。因此(19)在最后实际圆上仍准确成立，而不是仅初始母包的等宽近似。

## 7. 十二副本中的查询像准确为四维

固定上述倒数第二微包的真实母形 $u$。在其左侧 $u'>0$ 分支取 R345 的点：$(u'^{\,2/3})'$ 的一个正内部极大点。R391 已使所有 $A_u$ 零点简单，此点满足
$$
A_u(x_*)=0,\qquad p_*:=u'(x_*)>0,\qquad
r_\dagger:=u''(x_*)>0.
\tag{20}
$$
这里 $r_\dagger$ 表示该二阶 jet；共同右锚仍按原定义固定。

从实际十二副本中选不同平移 $t_j$ 的对应点 $x_*+t_j$。
设其额外共同正幅为 $\rho_j>0$、g 翻号为 $\varepsilon_j=\pm1$。固定八副本幅及最后五块幅可收入母副本常量；原加权系数不能删掉。
若最后微包的基本三矩为 $(m_0,m_1,m_2)$，则
$$
\mu_{i+1}(t)=
(m_0,m_1+tm_0,m_2+2tm_1+t^2m_0),\qquad m_0>0.
\tag{21}
$$
由(16),(19)，存在固定非零常数 $c_*$，使
$$
C_j(\mathcal R_E^*)=
\varepsilon_j\rho_j^7 c_*\,q_E(t_j),
\tag{22}
$$
而 $E=R,U,T,Y$ 四列依次为
$$
\begin{aligned}
q_R(t)&=-r_\dagger m_0,\\
q_U(t)&=-r_\dagger(m_1+tm_0),\\
q_T(t)&=-r_\dagger(m_2+2tm_1+t^2m_0),\\
q_Y(t)&=\tfrac12\{r_\dagger(x_*+t)-p_*\}
(m_2+2tm_1+t^2m_0).
\end{aligned}
\tag{23}
$$
其次数分别为 $0,1,2,3$，最高系数全部非零。
(18)中其余四列也属于同一次数至多三空间。因此在这组真实对应点上，
$$
\boxed{\operatorname{image}(\mathscr M_*\xrightarrow{C})
=\{(\varepsilon_j\rho_j^7q(t_j))_j:\deg q\le3\}.}
\tag{24}
$$
至多四个不同对应点的 C 查询独立；超过四个时，必须满足(24)的真实插值兼容。这个上界只指本八列模块，不是全响应空间的秩上界。

七次幅来自 C 本身：raw H 为五次，外乘 $R_i,T_i$ 再添二次。把(22)误写成 $\rho_j^5$ 会改变实际联合矩阵。

## 8. 与旧十一列拼合：有限内部像没有新增响应商

旧
$$
K_n=\delta^n\{\mathcal B_P[P,S]/3\},\qquad0\le n\le10
$$
满足 $E=\Lambda_{\rm all}=0$。
R345/R395/R397 给任意 $m\le11$ 个上述对应点的
$(H_{d,j}(K_n))_{j,n<m}$ 可逆，并且
$$
C_j(K_n)=0
\tag{25}
$$
对全部这些点成立。

在其中选 $r\le\min(4,m)$ 个不同点作 C 查询，令
$$
J_{\rm int}=(H_{d,1},\ldots,H_{d,m},C_{j_1},\ldots,C_{j_r}).
$$
旧 m 列与(23)的适当 r 列给块三角矩阵
$$
\begin{pmatrix}
M_{\rm old}&*\\0&M_{\rm new}
\end{pmatrix},
\qquad\operatorname{rank}=m+r .
\tag{26}
$$
星号是真实新列的第一通道值，不能置零；用旧列准确消掉它即可。

所以
$$
\boxed{J_{\rm int}
(\mathcal R\cap\ker E\cap\ker\Lambda_{\rm all})
=\mathbb R^{m+r}.}
\tag{27}
$$
这是同一 profiles、同一所有复制权、同一右锚的实线性结论。它直接表明即使 universal E 与全部自然总通量为零，这些选定的第二通道内部条件也不能省略。

若把 $J_0=(E,\Lambda_{\rm all})$ 作为原线性观测，(27)给
$$
(J_0,J_{\rm int})(U)=J_0(U)\times\mathbb R^{m+r},
$$
相应响应商仍是原 $J_0(U)/J_0(\mathcal R)$。本文不因此声称该商已有实际截面。

## 9. 两种准确、但不相互拼接的实际支付

### 9.1 保 whole E 的版本

R345 的实际 whole-E 增强方法可将(26)的有限核列全部纳入原响应库。R302 对新增 $\chi$ prototypes 的真实字、共享倒行、frame/九约束与保护端芽接口继续适用。

所有列的完整基准先纳入原 whole-E 截面；随后真实响应词的有限复制，使内部方程具有
$$
\mathcal E(t,z)+n(a+Mt)=b,\qquad \det M\ne0,
$$
其中 $\mathcal E$ 包含原 whole-E 校正的全部内部代价。参数盒与小族重复整数先固定，最后选择一个有限 n，原一致 $C^1$ 收缩给准确根。Klein 的完整基准照原式减去并除以4。

因此可以在同一实际闭 hook 上取
$$
\boxed{E=0,\qquad H_{d,j}=0\ (j\le m),\qquad
C_{j_\ell}=0\ (\ell\le r).}
\tag{28}
$$
在选定 r 个点，$R_i\ne0$，故(14)给 $H_e=0$。结合 R391 的简单 $A_f$ 判据及 R397 的 incoming-$L_f$ 不变性，两完整 period 在这 r 个点的内部逆 germ 都已支付。

这里最多取 r=4；其他点、总通量、全部端 germ、平台仿射 gluing 与同一相位十三行仍未因此全部支付。此版本不保 R390 的两条固定 A 值。

### 9.2 保原两条固定自然读出的版本

令 $F=P_{\mathscr L}E$、$A=(\Lambda_{u_+},\Lambda_{u_-})$，
沿用 [R396](R396-actual-joint-response-E-two-natural-and-selected-internal-fluxes.md) 的固定 profiles 和投影。

增广 $F^+=(F,J_{\rm int})$。因(11),(26)，旧 E 响应基加上本有限内部列后的真实矩阵仍满行秩，且所有响应均被 A 杀掉。两模块在真平移/正伸缩下稳定，所以共同 $\omega$ 安置后仍可在同一模块重选实际基，不移动查询点。

R396 的完整原型清 A、整组 n 次复制及后置 A 截面原样给
$$
A(V_{\widetilde Z})=\lambda,\qquad
F^+(V_{\widetilde Z})=
\mathcal E^+(t,\lambda)+n(a^++M^+t).
\tag{29}
$$
后置 A 校正的全部新内部通量进入 $\mathcal E^+$；有限 n 的一次收缩同时解全部目标。因此
$$
\boxed{(F,A,J_{\rm int})\ \text{具有原范围内的实际紧目标 }C^1\text{截面}.}
\tag{30}
$$
原未付 $qE$ 仍包括端块、n 倍原型基准及后置 A 校正三项。未付其他 $\Lambda_u$ 也没有被两条 A 替代。尤其不能把(28)和(30)拼成 whole $E+A$ 联调。

本文的新完成项是原方向(1)、完整局部通量(6)、真实有序残差(16)、原负布局上的非零源(19)、四维对应像(24)以及保持既有基准的有限实际增强。R394 的其余真实 period/十三行条件仍是后继问题。