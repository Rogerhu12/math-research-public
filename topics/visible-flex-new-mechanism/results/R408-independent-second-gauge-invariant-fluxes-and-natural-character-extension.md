# R408：同一二阶规范的逐包通量不变量与自然正字符的准确延拓边界

日期：2026-11-16。**完整纸面原式证明；没有执行求积、符号程序、人工测试、秩计算或新的研究运行。**

[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md) 已证明 canonical 成本的全部自然通量承载正字符 $\lambda_+$。该结论的定义域是原 universal 成本空间，不能直接用于在一个固定圆上任意选择的二阶齐次规范。本稿准确处理这个差别。

结果有两层。对原允许的任意光滑相位家族 $w_\theta$，每个真实活动包的总通量、每个 $A_f=0$ 点的累计通量以及平台二次项全部不变；左仿射尾和一般内部部分通量则可以改变。对由固定双线性规则 $w_\theta=W(D_\theta)$ 给出的规范，其完整周期改变量另外具有 $\pi=\mathcal Q=\Lambda_{\rm all}=0$，故 $\lambda_+$ 可良定义延拓到相应算子和空间并湮没该规范。后一结论仍不是固定圆评价后的正字符定理；本文给出那里所需的准确因子化条件。

来源：[R181](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)、[R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md)、[R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md)、[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md) 与 R406。R394 中“全部自然通量零”只是一项条件；本稿不把该条件当成已经实际构成的背景。

## 1. 固定实际几何、目标、同一个规范及完整平方成本

固定同一实际闭几何、共同右锚和全路径初值，满足
$$
M=0,\qquad T=\tau\mathfrak H,\qquad \tau\ne0.
\tag{1}
$$
这里 $\tau$ 是整个第三算子的实际系数，不是端芽局部曲率。固定同一个第一圆、目标和全部真实包：
$$
f=\sum_{i=1}^n a_i u_i,\qquad
g=\sum_{i=1}^n b_i u_i,\qquad a_i\ne0,
$$
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
F=f\odot f,\qquad D_\theta=F-\phi_\theta\odot\phi_\theta .
\tag{2}
$$
各 $u_i$ 在 $J_i=(\ell_i,r_i)$ 真紧，包从左到右严格不交，全部端点平坦并留正间隙。幅度、宽度、平移、真实八/十二副本和最后组合均已固定；不以一个新同母模型替换。

原允许的二阶规范是同一个实家族
$$
w_\theta\in C_c^\infty(I),\qquad
w_{\theta+2\pi}=w_\theta,\qquad w_0=w_\pi=0,
\tag{3}
$$
随相位光滑。它可以穿过间隙，不要求在每个 $J_i$ 上分别紧，也不限制为有限 Fourier 多项式。

记原几何三权为 $\mathbf w_{\rm geom}(s)$。准确第三合法性条件为
$$
\mathbf w_{\rm geom}(s)\cdot\mathbf I(\phi_\theta,w_\theta)=0
\quad\text{对所有 }s,\theta .
\tag{4}
$$
在 R326 的有理端口，三权独立，故(4)等价于 $\mathbf I(\phi_\theta,w_\theta)=0$。六条分别与 $f,g$ 配对的矩条件只是更强的充分条件，不替代(4)。

沿 R184 的号，原二、三阶场改变为
$$
\widetilde Z=Z-Y_w,\qquad
\widetilde U=U+2Z_B(\phi,w)+Y_\chi .
$$
完整第四 forcing 的差是
$$
\Delta H_4
=2H(Z,Y_w)-H(Y_w,Y_w)
-4H(Y_\phi,Z_B(\phi,w))-2H(Y_\phi,Y_\chi).
\tag{5}
$$
平方项没有删除。因为 $M=0$，它和第三齐次项的整个周期都准确为零；原第三 hook 的循环身份给
$$
\boxed{\widetilde V_\theta
=V^0_\theta+2\tau L_f(w_\theta),\qquad
L_f(w)=\mathfrak H(w;f,f).}
\tag{6}
$$
这是完整函数身份，不是切向近似。

另一方面，整个第四 ruling 仍为
$$
\widetilde K_\theta
=K^0_\theta+\mathcal B_\theta(w_\theta)
-\mathbf w_{\rm geom}\cdot\mathbf I(w_\theta,w_\theta)
-2\mathbf w_{\rm geom}\cdot\mathbf I(\phi_\theta,\chi_\theta),
\tag{7}
$$
$$
\mathcal B_\theta(w)
=2\int Z_x\cdot(Y_w)_x
-4\int(Y_\phi)_x\cdot Z_B(\phi,w)_x .
$$
只有在真实三维几何函数商中，平方与第三齐次项才不出现。R184 的同一全局 Gram 右逆实际支付这些项；其第三 adjoint 密度是
$x^2\phi''''+4x\phi'''$，保留其中的 $x$。本文不以周期线性性冒称未取商的第四 forcing 线性。

## 2. 原同锚公式：一般 $w$ 的全部端项

设
$$
J(a)(x)=\int_x^{r_*}a(y)\,dy,\quad
p=f',\quad q=f'',\quad
A_f=6pf'''-2q^2,\quad V_f=6(qf''')'.
$$
R181 的完整原式为
$$
\begin{aligned}
L_f(w)(x)={}&-3w'(x)q(x)^2-J(w''q^2)(x)\\
&+6\int_x^{r_*}(y-x)w''(y)q(y)q'(y)\,dy
-6J(w''pq')(x).
\end{aligned}
\tag{8}
$$
所以
$$
L_f(w)''=(A_fw'')'-V_fw',
\qquad
\boxed{pL_f(w)''=\{A_f(pw''-qw')\}'.}
\tag{9}
$$
这里没有除以 $p$ 或 $A_f$；它在真实退化点和间隙仍成立。

对任一包及任意 $x\in J_i$，从该包原左平端积分：
$$
\boxed{
\int_{\ell_i}^x f'(y)\,\partial_y^2\Delta V_\theta(y)\,dy
=2\tau A_f(x)\{f'(x)w_\theta''(x)-f''(x)w_\theta'(x)\}.
}
\tag{10}
$$
左端常数确为零，因为 $f',f'',f'''$ 在 $\ell_i$ 全平。没有要求 $w$ 或其导数在 $\ell_i$ 为零。因此，在每个原 $A_f(x_*)=0$ 点，
$$
\boxed{\Delta\mathcal H_i^\theta(x_*)=0.}
\tag{11}
$$
这包括简单或高阶零点，不需要先证明相应 ODE 逆解存在。

到右平端，(9)的通量也为零。再保两次 IBP 的真实边项：
$$
\begin{aligned}
\int_{J_i} f'''\Delta V_\theta
&=\int_{J_i} f'(\Delta V_\theta)''
+\big[f''\Delta V_\theta-f'(\Delta V_\theta)'\big]_{\ell_i}^{r_i}\\
&=0.
\end{aligned}
\tag{12}
$$
最后括号由 outer $f$ 的平端支付，不是把 $\Delta V$ 的左尾设为零。于是所有允许的 $w_\theta$ 均满足
$$
\boxed{\Delta\mathcal T_i^\theta=0,\qquad
\mathcal T_i^\theta:=\int_{J_i} f'''V_\theta .}
\tag{13}
$$

若 $f$ 在开放间隙为常数，则(9)直接给 $(\Delta V_\theta)''=0$。因此所有平台二次系数不变；不能据此说平台函数本身不变。式(10)在一般 $A_f\ne0$ 点也通常不为零，所以本稿不把全部内部部分通量授为不变量。

## 3. 真实逐包仿射尾与确实存在的规范自由度

式(8)只含 $f$ 的同点二次导数乘积。不同包不交，故作为整个同锚函数有
$$
L_f(w)=\sum_i a_i^2L_{u_i}(w).
\tag{14}
$$
令 $p_i=u_i',r_i=u_i'',t_i=u_i'''$。第 i 项在该包右方为零，在左方准确为
$$
L_{u_i}(w)(x)=c_{i,0}(w)+xc_{i,1}(w),
$$
$$
\boxed{\begin{aligned}
c_{i,1}(w)&=-6\int_{J_i}w''r_it_i,\\
c_{i,0}(w)&=-\int_{J_i}w''r_i^2
+6\int_{J_i}y\,w''r_it_i
-6\int_{J_i}w''p_it_i.
\end{aligned}}
\tag{15}
$$
所以任一间隙中的输出是其右方各包的真实
$2\tau a_i^2(c_{i,0}+xc_{i,1})$ 之和。不能将相邻包的两个 affine 常数逐包重新清零；若目标要求某个外 collar 的周期函数为零，这些常数仍须准确匹配。

例如取一个共同紧 $w$，在每个包邻域仿射为 $C_ix+B_i$，其连接全部放在间隙。所有原 $I_j(f,w),I_j(g,w)$ 均为零，所以第三合法性确已付；式(8)准确给
$$
L_f(w)=-3\sum_i C_i a_i^2(u_i'')^2.
\tag{16}
$$
这是实际有符号周期自由度，并不与(13)矛盾：
$\int u_i'''(u_i'')^2=0$。它不自动属于下文保持有理端口的十三行核，也不自动支付其他段的完整 ruling。

## 4. 有限 $\omega_i$、ordered $\mathcal A_i$ 与被保护的两组实际量

本节使用原 canonical 背景
$$
E(V)=(\pi V,\mathcal Q(V))=0.
\tag{17}
$$
不另假全部自然通量为零。记
$$
S_i=V(u_i^2,0),\qquad
U_{ij}=4\,\mathscr P H\big(Y_{u_i},C(u_i;u_j^2)\big)\quad(i<j),
$$
$$
\omega_i=\int u_i'''S_i=\Lambda_{u_i}(V).
\tag{18}
$$
R389 的原 pure 极化与完整跨尾局域性给
$$
V^0_\theta
=\sum_i a_i^2\left[d_i(\theta)S_i+
\sum_{j>i}d_j(\theta)U_{ij}\right],
\quad d_i(\theta)=a_i^2-(a_i\cos\theta+b_i\sin\theta)^2 .
\tag{19}
$$
每个 $U_{ij}$ 对真正右包仅通过其三矩 $\mu_j$ 线性依赖。用三个真实右包的矩基延拓，写
$$
U_{ij}=\mathscr U_{V,u_i}(\mu_j),\qquad
\mathcal A_i(n)=\int u_i'''\mathscr U_{V,u_i}(n).
\tag{20}
$$
原右锚、全 s-history 和恢复初值都在 $\mathscr U$ 中，不把它换成局部 jet 模型。

令
$$
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,\quad
n_{R,i}=\sum_{j>i}R_j\mu_j,\quad
n_{T,i}=\sum_{j>i}T_j\mu_j .
$$
按 $V^0_\theta=\sin^2\theta\,V_d+2\sin\theta\cos\theta\,V_e$，每包实际总量准确为
$$
\boxed{\begin{aligned}
\mathcal T_{d,i}&=a_i^3\{R_i\omega_i+\mathcal A_i(n_{R,i})\},\\
\mathcal T_{e,i}&=-a_i^3\{T_i\omega_i+\mathcal A_i(n_{T,i})\}.
\end{aligned}}
\tag{21}
$$
这里显示的 $a_i^3$ 之外，$R_i,T_i$ 和 suffix 仍含两次真实幅度。

式(13)证明：加入任意允许 $w_\theta$ 后，整包总量仍是
$\sin^2\theta\,\mathcal T_{d,i}+2\sin\theta\cos\theta\,\mathcal T_{e,i}$，其两个系数都不变；即使修改后的周期函数本身含更高相位谐波，额外谐波的这些读出也准确为零。

为对应有限 natural 查询，可在全部实际包右方选择三个真实紧辅助 $v_\alpha$，其三矩 $\nu_\alpha$ 成基。若
$n=\sum_\alpha q_\alpha(n)\nu_\alpha$，则原有序 $3+2$ 极化给
$$
\mathcal A_i(n)=\sum_{\alpha=1}^3q_\alpha(n)
\left\{\frac{\Lambda_{u_i+v_\alpha}(V)+\Lambda_{u_i-v_\alpha}(V)}2
-\Lambda_{u_i}(V)\right\}.
\tag{22}
$$
$\Lambda_{v_\alpha}$ 在取两号平均时按五次齐次性消去；显示的 $1/2$ 不能再乘或除一次。

**定义域边界。** 一般 $w_\theta$ 只给当前一个圆上的函数，不定义对任意辅助 profile 的 universal 成本。因此，不能把(22)中的每个 $\Lambda_{u_i\pm v_\alpha}$ 独立写成一个由该 $w_\theta$ 引起的改变量。canonical $V$ 及其 $\omega_i,\mathcal A_i$ 是不变的原背景资料；被本稿证明不变的是(21)的实际组合。修改后的周期输出不必仍属于 R389 的 canonical $S/U$ 分解类。

若要保内部点，将(18)、(20)换成真部分函数
$$
s_i(x)=\int_{\ell_i}^x u_i'S_i'',\qquad
\mathfrak a_i(x;n)=\int_{\ell_i}^x u_i'\mathscr U_{V,u_i}(n)''
$$
即可。准确关系
$$
s_i(x)=u_i'(x)S_i'(x)-u_i''(x)S_i(x)+\int_{\ell_i}^x u_i'''S_i
\tag{23}
$$
保上端 jets。在 $A_f=0$ 点，两个(21)型部分组合由(10)不变，不能用裸积分替代(23)。

## 5. 保原 incoming 和同一个十三行未知量

R326 的实际入矩阵给 $X=\Phi_{\mathsf m_*}$，先前合法规范为
$$
w_\theta^c=-XD_\theta.
$$
原三矩与八完整副本确保它真紧、第三合法。它的真实周期基准是
$$
V_d^c=V_d-2\tau L_f(X\Delta),\qquad
V_e^c=V_e+2\tau L_f(X(f,g)),\quad
\Delta=f^2-g^2 .
\tag{24}
$$
因此(21)和全部 $A_f$ 点读出对这个已安装规范也不变；但两个完整函数(24)一般改变，不能把 $\mathsf m_*$ 清零。

后续写同一个 $w_\theta=w_\theta^c+k_\theta$，沿 R326 的完整定义记
$$
H_{Y,j,\theta}(k)
=-I_j(YD_\theta,k)+2I_j\{\phi_\theta,Y(\phi_\theta,k)\},
$$
$$
\mathcal A_\theta(k)=
\left(\mathbf I(\phi_\theta,k),\
(P_{\ell,\theta}(k))_{\ell=-4}^{2},\
(H_{B,j,\theta}(k))_{j=0}^{2}\right).
\tag{25}
$$
$P_{\ell,\theta}$ 是 R326(30)—(32)保全部 local pairing/真尾的七个原系数，B 是该端口原单反正切矩阵。本稿不重定义或省略任何一行。

指定端口加完整周期的实际方程仍恰为
$$
\boxed{\mathcal A_\theta(k_\theta)=0,\qquad
V_\theta^c+2\tau L_f(k_\theta)=0,}
\tag{26}
$$
并保相位光滑、周期、两个 seed 和共同 collar。只有这个同一 $k_\theta$ 可以进入两式。平方和交叉的 $\mathcal W_e$ 部分仍由(7)的同一个第三 Gram 右逆支付。

本稿的不变量只给(26)的必要门，不把它们称为充分。若两条原函数方程已找到真实特解
$$
L_fk_d=-V_d^c/(2\tau),\qquad
L_fk_e=-V_e^c/(2\tau),
$$
则
$k_\theta^0=\sin^2\theta\,k_d+2\sin\theta\cos\theta\,k_e$ 是一个全相位特解。任意其他光滑解与它之差在 $\ker L_f$，而不是被限制到相同两谐波。

在 R327 的实际解析包类中，
$$
\ker L_f=\operatorname{span}\{u_i,\chi_i:1\le i\le n\}\oplus\mathscr G .
\tag{27}
$$
$\chi_i$ 在一个包邻域为1、其他包为0；$\mathscr G$ 是函数本身在所有包上零的间隙空间。只有 $\mathscr G$ 对十三行盲。真实平台列 $\mathcal A_\theta(\chi_i)$ 通常非零，不能用调 $\int k'$ 的间隙连接掩去其成本。

因此 R327/R394 的实际有限系统
$$
C_\theta\beta_\theta=-\mathcal A_\theta(k_\theta^0)
\tag{28}
$$
及相位秩降处的光滑、种子整除条件完整保留。十三只是显示行数。R394 使用全自然零消去包总量的条件，可用实际有限(21)为零替代；R406 之后不能再把全自然零当作一般实际构造的前提。

## 6. 固定双线性规则的 universal 周期改变量

现在给出可以谈 universal 读出的一个明确子类。令 W 是一个**预先固定**的实对称双线性规则，输入 profiles、输出同 collar 真紧 profile；不要求它属于 E8，不要求它是局部算子。原 E8 算子 X 的单个 self 一般带二次左尾，不能自动作为这里的 W；若它仅在当前 D 槽真紧，可使用第7节的有限秩提升。令
$$
w_\theta=W(D_\theta).
$$
只在它另外满足(4)、(26)等原条件时，才作为实际合法规范使用。下面的算子身份不预授这些条件。

把(6)提升为明确的 quartic 周期算子
$$
\boxed{
G_W(F,\phi)=2\tau\mathfrak H(W(F-\phi\odot\phi);F).
}
\tag{29}
$$
右槽对 $F\in\operatorname{Sym}^2$ 线性。对固定 F，它的相位次数至多二，所以原第四 pure 模式准确为零：
$$
\pi G_W=0.
\tag{30}
$$
其原 self 是
$$
G_W(u^2,0)=2\tau L_u(W(u,u)).
$$
由(15)，该 self 的左尾至多仿射；由(12)，其整个裸 self 通量为零。因此
$$
\boxed{
\mathcal Q(G_W)=0,\qquad
\Omega_u(G_W):=\int u'''G_W(u^2,0)=0\quad\text{对全部 }u.
}
\tag{31}
$$
没有要求 $W(u,u)$ 逐子包紧，也没有把它的真实左尾放进零边界。$\mathcal Q$ 是原左二次 self 系数，不是完整 self 函数。

原自然读出与裸 $\Omega$ 的差只由 pure 和其原有序尾补偿决定。式(30)使这些补偿准确为零，故
$$
\boxed{E(G_W)=0,\qquad \Lambda_{\rm all}(G_W)=0.}
\tag{32}
$$
这是整个算子身份，不只是对当前 f、g 的有限观察。它**不证明** $G_W\in U$ 或 $G_W\in R$；本稿不把新增规范成本改名成旧 canonical response。

令 $\mathscr G_{\rm quad}$ 为所有(29)的线性空间。在原 universal quartic 周期算子的共同函数空间中取
$U+\mathscr G_{\rm quad}$。若 $G_W$ 恰落入原 U，R406 的自然读出正字符下降与(32)给
$$
\lambda_+(G_W)=0.
$$
所以
$$
\boxed{\lambda_+^{\rm ext}(V+G_W)=\lambda_+(V)}
\tag{33}
$$
是良定义线性泛函。若一个输出有两种表示，两种 canonical 部分之差在
$U\cap\mathscr G_{\rm quad}$，正好由上述零值消除歧义。相同论证给自然读出在和空间上的一致延拓。

因此，在 R406 原实际闭路径范围中，加入这类 universal 规范不改变其正值
$$
\lambda_+^{\rm ext}(V+G_W)
=\lambda_+(V)=\int k^2
=L+\int(h'/h)^2>0.
\tag{34}
$$
这里只说该原实际成本的算子延拓；不把任意 W 称为一个新几何路径，也不把(34)升为固定圆评价后的字符。

## 7. 两谐波特解有此提升，但 kernel 家族和十三门仍不可删

固定实线性无关的 f、g，取连续实线性泛函 $\ell_f,\ell_g$，满足
$$
\ell_f(f)=\ell_g(g)=1,\qquad
\ell_f(g)=\ell_g(f)=0 .
$$
例如用 f、g 的真实 $L^2$ Gram 逆得到。给任意两个真紧 profiles $w_d,w_e$，定义有限秩规则
$$
W(a,b)=w_d\ell_f(a)\ell_f(b)
-w_e\{\ell_f(a)\ell_g(b)+\ell_g(a)\ell_f(b)\}.
\tag{35}
$$
则
$$
W(D_\theta)=\sin^2\theta\,w_d+2\sin\theta\cos\theta\,w_e .
\tag{36}
$$
所以一旦完整周期有两谐波特解，它确有一个固定规则的 universal 提升；这不是仅把固定圆记号重命名。

不过，(36)本身不保证第三合法性或十三门。任意实际解还可需要一个相位任意光滑的 $\ker L_f$ 家族，准确修正(28)。对该 kernel 家族，固定圆上的周期改变量为零，但它在 ruling/平台列中仍有真实作用。不能因(36)有低谐波就限制整个允许 $w_\theta$ 的相位类型。

## 8. 固定圆上的正字符需要的准确附加条件

记 $\operatorname{ev}_{f,g}V$ 为原成本在整个固定圆上的周期函数。对一个准确规定的允许线性规范域 $\mathscr D$，令
$$
\mathscr I_{f,g}
=\{\theta\mapsto 2\tau L_f(w_\theta):w\in\mathscr D\}.
\tag{37}
$$
$\mathscr D$ 可取(3)、(4)的全部家族，或在已付基准 $w_c$ 后取(25)的十三行核；后一种必须保真实 affine 基准 $V^c$。

存在一个在
$\operatorname{ev}_{f,g}U+\mathscr I_{f,g}$ 上良定义的线性读出，等于原 $\lambda_+$ 且湮没规范像，当且仅当
$$
\boxed{
\{V\in U:\operatorname{ev}_{f,g}V\in\mathscr I_{f,g}\}
\subseteq\ker\lambda_+ .
}
\tag{38}
$$
必要性直接；充分性取
$\ell(\operatorname{ev}V+G)=\lambda_+(V)$，两种表示之差由(38)支付。

R406 的 universal 自然字符定理和(33)都没有单独证明(38)：一个非零 universal 输出可以在一个固定圆上消失。相反，本稿(11)、(13)、(21)提供了准确的 gauge-annihilating 实际读出。如果能在当前有限包上把 $\lambda_+$ 写为这些读出的线性组合，就会真正支付(38)，并得到该固定圆上不能被二阶规范逃避的障碍。这个读出必须从实际包/幅/宽/原 tail 推出，不能把辅助 natural 查询独立赋给 w。

## 9. 完成范围

本稿已准确回答独立二阶规范的三项作用：

- 每包总通量、所有原 $A_f=0$ 累计通量和平台二次项不变，证明保完整 flat-end 边项；原 affine 尾变化为(15)。
- 对 canonical 有限 $\omega_i$ 和 ordered $\mathcal A_i$，实际不可变的是(21)两组及其内部点版本；一般单圆 w 不定义各辅助 universal 查询的改变量。
- 固定双线性规则给(32)完整 universal 核与(33)正字符延拓；固定圆结论另需(38)，不能把两种定义域合并。

全函数周期特解、全部内部退化逆解、两端值闭合、十三行相位兼容、其余几何段 ruling 仍必须由同一个 w 联合满足。没有改变原几何、目标、首阶圆、入历史或预算，也没有从这些必要不变量授完整第四解或一般无解。
