# R394：全自然通量零前提下的真实 period 与十三行同规范有限接口

日期：2026-11-15。**纸面原式归约；没有运行求积、符号消元、人工测试、数值秩或研究计算。**

本稿接 [R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、[R391](R391-analytic-simple-degeneracies-and-complete-selected-inverse-germs-on-the-rational-circle.md) 与 [R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md)。新的结论是一个完整的条件性接口：若同一实际几何已经有 universal whole pure/self 零与全部自然总通量零，那么两条真实 period 的像问题只剩下显示的内部有序部分通量；这些门成立后，原十三行同规范问题又等价于一组准确有限的相位多项式条件。

本文**不证明**上述自然通量与 whole-$E$ 已能实际联合控制，不把任何新行授为满射。三个层次始终分开：原成本的真实内部值、全区间 gauge 的值闭合、同一个 gauge 的十三行兼容。特别，给 $k'$ 作间隙积分修正会改变 k 的平台值，必须进入十三行真实右端；不能当作盲方向。

其他直接来源：[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md)、[R324](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md)、[R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md)、[R345](R345-local-whole-E-kernel-orbit-and-eleven-corresponding-degenerate-fluxes.md) 与 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)。

## 1. 明确的实际假设，不继承另一几何的已付值

固定 R391 从起点选择的同一个有理端口圆：
$$
f=\sum_{i=1}^n a_i u_i,\qquad
g=\sum_{i=1}^n b_i u_i,\qquad a_i\ne0.
\tag{1}
$$
最细活动包 $J_i=(\ell_i,r_i)$ 从左到右严格不交，之间及共同外 collar 留正间隙。所有真实幅度、平移、宽度、八/十二副本和最终五块都已经展开在(1)中。每个实际包有正解析 prefactor；$p=f'$ 在每包只有一个简单零点，$A_f=6f'f'''-2(f'')^2$ 的所有内部零点简单，且这些点上 $p\ne0$。

实际几何满足
$$
M=0,\qquad T=\tau\mathfrak H,\quad\tau\ne0,
\qquad E(V):=(\pi V,\mathcal Q(V))=0.
\tag{2}
$$
另作本稿的明确额外假设
$$
\boxed{\Lambda_u(V)=0\quad\text{对全部实紧 profile }u.}
\tag{3}
$$
这里 $\Lambda$ 是 R352 的原自然读出，含原 pure 和有序 $2+2$ Green 补偿；不是一般情况下的裸 self 总通量。只有使用(2)的 $\pi V=0$ 后，R389 才给它与裸收缩的准确身份。

(3)是对当前实际成本 V 的条件，不是“纯零响应”一词的同义语，也不由 R333 的 whole-$E$ 结论或 R390 的两个固定读出推出。本稿下面只使用 $\Lambda_{u_i}$ 和 $\Lambda_{u_i+u_j}$ 的有限一组值；因此也可用这些具体值全零替代(3)，但不宣它们独立或已经可控。

原 R324 十九个完整值及 R326 的指定端口接口保留。没有把本稿的条件性范围扩到旧冻结度量、Morse、其余路径段或整个主课题。

## 2. 从整包通量到原有序部分通量

令
$$
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,\quad
c_i=a_i\cos\theta+b_i\sin\theta,\quad
d_i=a_i^2-c_i^2.
$$
沿 R389 的完整原恢复记
$$
S_i=V(u_i^2,0),\qquad
U_{ij}=[a^2b^2]\,V((au_i+bu_j)^2,0)\quad(i<j).
\tag{4}
$$
所有输出保同一个右锚及完整 s-history。whole pure 极化已给
$$
V^0_\theta
=\sum_i a_i^2\left[d_iS_i+\sum_{j>i}d_jU_{ij}\right].
\tag{5}
$$
这些输出在其 outer 包右方为零，左方原本为二次多项式。现在使用(2)的 universal $\mathcal Q=0$：先对每个 $u_i$，再对 $au_i+bu_j$ 极化，得到每个 $S_i,U_{ij}$ 的真实左尾二次系数都为零。因此它们在 outer 包左方是**原仿射尾**，不是被重新置零。

在第 i 包内定义真实部分积分
$$
s_i(x)=\int_{\ell_i}^{x}u_i'(t)S_i''(t)\,dt,\qquad
s_{ij}(x)=\int_{\ell_i}^{x}u_i'(t)U_{ij}''(t)\,dt.
\tag{6}
$$
所有其他 outer 包的输出在 $J_i$ 上是零或仿射，所以其二阶导准确为零。(6)因此完整保留了(5)在当前包内的作用。

不能把(6)换成 $\int_{\ell_i}^x u_i'''S_i$ 而不保上端 jets。准确关系为
$$
s_i(x)
=u_i'(x)S_i'(x)-u_i''(x)S_i(x)
+\int_{\ell_i}^x u_i'''S_i,
\tag{7}
$$
$U_{ij}$ 同理。只有到包右端，两个真实端项才全零。

R389 的原有序 $3+2$ 身份给
$$
s_i(r_i)=\Lambda_{u_i}(V),\qquad
s_{ij}(r_i)=\Lambda_{u_i+u_j}(V)
-\Lambda_{u_i}(V)-\Lambda_{u_j}(V).
\tag{8}
$$
所以(3)使全部(8)为零，却不使内部的(6)自动为零。

### 2.1 右方包仍只通过三个真实矩进入

记原三矩向量为 $\mu_j=\mu(u_j)$。对固定左包 $u_i$，R352 的真实二阶左尾 $\mathscr T_n$ 对 $n\in\mathbb R^3$ 线性，并保原 s 初值。定义整个输出
$$
\mathscr U_i(x;n)
=4\mathscr P H\!\left(
Y_{u_i},\operatorname{Range}H(Y_{u_i},\mathscr T_n)
\right)(x).
\tag{9}
$$
这与 R389(22)使用同一个原恢复，只暂不作最终总通量积分。R288 的跨包局域性使
$\mathscr U_i(\,\cdot\,;\mu_j)=U_{ij}$ 对每个 $j>i$ 成立。于是
$$
\mathfrak a_i(x;n)
=\int_{\ell_i}^x u_i'\,\partial_x^2\mathscr U_i(\,\cdot\,;n)
\tag{10}
$$
对 n 线性，且 $s_{ij}(x)=\mathfrak a_i(x;\mu_j)$。

这里没有将右方的真实形状换成任意矩模型。先对真正右包证明身份，再用三个真实右包的矩基延拓；其系数唯一。$\mathscr T_n$ 和内部第三 Range 的原 history、初值和 ordered 方向全部保留。

因此两组 suffix 可准确写为
$$
R_i s_i(x)+\mathfrak a_i\!\left(x;\sum_{j>i}R_j\mu_j\right),
\qquad
T_i s_i(x)+\mathfrak a_i\!\left(x;\sum_{j>i}T_j\mu_j\right).
\tag{11}
$$
这些是固定当前包的一个真实 self 部分函数及三个真实混合部分函数，不是局部 jet 的替代品。

## 3. 两个实际 period 的全部剩余内部点门

按原规范
$$
V_\theta^0=\sin^2\theta\,V_d+2\sin\theta\cos\theta\,V_e.
$$
R389 给
$$
V_d=\sum_i a_i^2\left[R_iS_i+\sum_{j>i}R_jU_{ij}\right],
$$
$$
V_e=-\sum_i a_i^2\left[T_iS_i+\sum_{j>i}T_jU_{ij}\right].
\tag{12}
$$
真实 incoming 矩阵给 $X=\Phi_{m_*}$。先前已选
$w_c=-XD_\theta$，故
$$
G_d=-\frac{V_d-2\tau L_f(X\Delta)}{2\tau},\qquad
G_e=-\frac{V_e+2\tau L_f(X(f,g))}{2\tau},
\quad\Delta=f^2-g^2.
\tag{13}
$$
这里 $D_\theta=f^2-\phi_\theta^2=\sin^2\theta\,\Delta-2\sin\theta\cos\theta(f,g)$，与 R326(2)、(24) 的原规范一致。

列出第 i 包的全部简单 $A_f$ 点为 $x_{i,\alpha}$。原不除 p 的通量身份使任意允许光滑 $L_f$ 像在这些点的累计通量为零。因此由(6)、(12)得到
$$
\boxed{
\begin{aligned}
F_i(x_{i,\alpha};G_d)
&=-\frac{a_i^3}{2\tau}
 \left[R_i s_i(x_{i,\alpha})
       +\sum_{j>i}R_j s_{ij}(x_{i,\alpha})\right],\\
F_i(x_{i,\alpha};G_e)
&=+\frac{a_i^3}{2\tau}
 \left[T_i s_i(x_{i,\alpha})
       +\sum_{j>i}T_j s_{ij}(x_{i,\alpha})\right].
\end{aligned}}
\tag{14}
$$
$F_i(x;G)=\int_{\ell_i}^x f'G''$ 始终从原包左端起算，未在各退化点重设常数。输出已含 $a_i^2$，读出再乘一次 $a_i$，得到显示的 $a_i^3$；$R_i,T_i$ 仍含另外两次幅度。因此完整共同副本幅仍为第五次，不把显示的第三次因子误作整个缩放。

把(14)右边的两组括号记为 $\mathcal B_{\rm int}(V)$。这是一个有限真实读出向量；显示位置数为两倍全部 $A_f$ 点数，不称其为秩。它保持整右尾和完整历史，而不由(8)的零推出。

## 4. 完整 range 的 iff，分开处理 k 的值闭合

在(1)—(3)下，两个原全函数问题
$$
L_fk_d=G_d,\qquad L_fk_e=G_e,
\quad k_d,k_e\text{ 在共同双 collar 为零}
\tag{15}
$$
可解，当且仅当
$$
\boxed{\mathcal B_{\rm int}(V)=0.}
\tag{16}
$$

必要性由 R391(24)及(14)。充分性包含三件不同的事，必须分别完成。

**第一步：活动包上构造 $v=k'$，并连接真实端 jets。**
whole-$E$ 给全部平台 $G''=0$ 和原右 collar $G=G'=0$。R389 与(3)、(8)给每包总通量及两端真实光滑逆 germ。R391 又证明 p 的简单零点没有额外 Laurent 门，而(16)准确支付全部简单 A 点。

因此在每个活动包使用同一个原累计量构造
$$
v=p\left(C+\int\frac{F_i(x;G)}{A_fp^2}\,dx\right).
\tag{17}
$$
跨内部点匹配后，v 在整个闭包光滑。其端 jets **未必为零**；原平端逆解只要求它们能光滑延拓，不能称为全平。用实际一侧延拓和固定 cutoff 将有限个活动包接入正长度零间隙，并在最外 collar 取 $v=0$。间隙里 $A_f=V_f=G''=0$，所以连接不改微分方程。

**第二步：准确支付 k 的两端值。**
每包跳量
$$
J_i=\int_{\ell_i}^{r_i}v
$$
一般不为零，齐次 $Cp$ 确实不能改变它，因为
$\int_{\ell_i}^{r_i}p=f(r_i)-f(\ell_i)=0$。
不能省掉这项闭合。

在一个固定正长度间隙内取真紧光滑 $\eta$，$\int_I\eta=1$。把上述 v 换成
$$
v^\#=v-\left(\int_Iv\right)\eta .
\tag{18}
$$
这不改任何活动端 jets 或微分方程，却准确给 $\int_Iv^\#=0$。随后定义
$$
k(x)=\int_{r_*}^{x}v^\#(t)\,dt .
\tag{19}
$$
原右 collar 和(18)使 k 在两个共同 collar 都为零。这一步使用的是允许的正间隙；若另强加 k 必须逐活动包紧支撑，就不能引用此结论。

给 $k'$ 加(18)通常改变 k 在其左侧各包的平台值。它不是十三行的盲方向，其真实代价必须保在最终特解的所有配对中。

**第三步：消掉算子输出的全局仿射差。**
现在才由原式得到
$$
(L_fk-G)''=0.
$$
原同右锚恢复在共同右 collar 同时给该差和一阶导数为零，所以它在整个 I 为零。这支付了真实左仿射尾；不能用这一步反过来代替(18)对 k 自身的值闭合。

上述构造是 R225 第7节的完整右逆在当前简单退化类上的准确消费。在固定有限维可解目标空间中，先对一组实际基选定所有延拓、cutoff 和(18)，再线性延拓，可取得一个固定线性右逆 S。不假设对无限维 germ 空间存在未说明的统一选择算子。

## 5. 原 incoming history 不作为自由平台常量删除

为清楚展示实际联合数据，先对
$$
G_d^0=-V_d/(2\tau),\qquad G_e^0=-V_e/(2\tau)
$$
使用第4节的固定线性右逆。仍按(13)的符号，取
$$
k_d=S(G_d^0)+X\Delta,\qquad
k_e=S(G_e^0)-X(f,g).
\tag{20}
$$
原 $\Delta$ 与 $(f,g)$ 的三矩为零，故两个 X 槽是同右锚的真实紧函数；这不是将单个 $X(u_i,u_i)$ 假定为紧。

令
$$
k_\theta^0=\sin^2\theta\,k_d+2\sin\theta\cos\theta\,k_e .
\tag{21}
$$
它准确解(15)对应的全相位 period。虽然 $w_c$ 与(21)里的 X 部分按原 $D_\theta$ 规范相消，端口方程使用的是
$\mathcal A_\theta(k_\theta^0)$，该右端仍必须代入(20)的真实 $m_*$。不能因总二阶 gauge 的一种表达变短就把 incoming history 置零。

第4节不同的线性连接选择只使两个特解相差 $\ker L_f$。R327 已严格给
$$
\ker L_f=
\operatorname{span}\{u_1,\ldots,u_n,\chi_1,\ldots,\chi_n\}
\oplus\mathscr G,
\tag{22}
$$
其中 $\chi_i$ 在第 i 包邻域为1，在其他包邻域为0；$\mathscr G$ 是 k 本身在所有活动包上为零的间隙函数。只有 $\mathscr G$ 对原十三行全盲。平台列 $\chi_i$ 的真实二次尾作用一般不零，恰承载(18)可能引入的代价。

所以原右逆选择不改变后面的可解性，但它会改变显示右端，必须由(22)的原列变换准确吸收。$m_*$ 与 V 也是实际几何共同产生的数据，不在本稿中被宣为可独立指定。

## 6. 把两个 seed 准确纳入同一十三行系统

沿 R327，记
$$
\mathcal A_\theta(k)
=\bigl(\mathbf I(\phi_\theta,k),
(P_{\ell,\theta}(k))_{\ell=-4}^2,
(H_{B,j,\theta}(k))_{j=0}^2\bigr)
$$
为原十三个完整读出，并令
$$
C_\theta=
\bigl(\mathcal A_\theta(u_1),\ldots,\mathcal A_\theta(u_n),
\mathcal A_\theta(\chi_1),\ldots,\mathcal A_\theta(\chi_n)\bigr).
\tag{23}
$$
母函数列及平台列严格使用 R327(12)、(14)—(17)，全部原 tail、$I_2$ 的 $2u'v'$ 和 local T 均保留。

为了同时满足 $k_0=k_\pi=0$，准确写
$$
q_\theta=\sin\theta\,k_d+2\cos\theta\,k_e,
$$
$$
k_\theta=\sin\theta\left[
q_\theta+\sum_{\nu=1}^{2n}\eta_\nu(\theta)v_\nu\right],
\quad
(v_\nu)=(u_1,\ldots,u_n,\chi_1,\ldots,\chi_n).
\tag{24}
$$
任何光滑周期 $\beta_\theta$ 在0、$\pi$ 为零，当且仅当
$\beta_\theta=\sin\theta\,\eta_\theta$，其中 $\eta$ 光滑周期；这是两个简单零点处的真实 Hadamard 除法，非额外的 Fourier 限制。

由线性，原 joint 因而准确等价于
$$
\boxed{C_\theta\eta_\theta=b_\theta,\qquad
b_\theta=-\mathcal A_\theta(q_\theta).}
\tag{25}
$$
在 $\sin\theta\ne0$ 处是原式除法，在两个 seed 处由连续性延拓；反向代入(24)直接得到原方程。所有真实 seed 的消失阶已在(25)中保留，不能只在两个点任意指定 $\beta=0$。

(23)前三行相位次数至多1，其余十行至多2；$q_\theta$ 次数1，因此 $b_\theta$ 的次数至多3。这里的次数指实际 $\sin\theta,\cos\theta$ 多项式，系数是固定 profiles、真实两特解和 incoming history 的完整配对值。

## 7. 全圆的准确有限条件与一个五十二阶总界

令 $z=e^{i\theta}$，把原三角多项式写为 Laurent 多项式。定义
$$
M(z)=z^2C_\theta,\qquad
b(z)=z^3b_\theta,\qquad
\zeta(z)=z\eta_\theta.
$$
则(25)准确变为
$$
\boxed{M(z)\zeta(z)=b(z),\quad |z|=1,}
\tag{26}
$$
其中 M 是 $13\times2n$ 的复多项式矩阵，逐项次数至多4；b 的次数至多6。z 在相位圆上可逆，没有增加零点处的物理条件。

记 r 为 M 在 $\mathbb C(z)$ 上的秩，不把十三当成 r。它也是实际相位圆上的最大秩：一个不恒零的 minor 只在有限个圆上点为零，所以其余某个真实相位达到同一秩。若 r=0，条件就是 $b(z)\equiv0$。若 r>0，在主理想整环 $\mathbb C[z]$ 中作精确多项式行列消元，可取 unimodular U、V，使
$$
U(z)M(z)V(z)
=\begin{pmatrix}
d_1&&&0\\&\ddots&&\vdots\\&&d_r&0\\
0&\cdots&0&0
\end{pmatrix},
\qquad d_i\mid d_{i+1},\quad d_i\ne0.
\tag{27}
$$
这里只陈述对实际矩阵的精确代数，不执行新消元或预定秩。令 $\widetilde b=Ub$。完整全圆条件恰为：

1. 对每条零行，$\widetilde b_i(z)$ 恒等于零，即其全部有限多项式系数为零；
2. 对每个 $d_i$ 在 $|z|=1$ 上的根 $\zeta_*$，若其重数为 $\nu_{i,\zeta_*}$，则
$$
\partial_z^j\widetilde b_i(\zeta_*)=0,
\qquad 0\le j<\nu_{i,\zeta_*}.
\tag{28}
$$

这些是实际值和实际导数，不是有限相位采样。对实数据，共轭条件相关，可保复写法而不冒独立行数。

还有一个无需求出 r 或根的保守总界。非零 r 阶 minor 的次数至多 $4r$。Smith 的行列式因子
$d_1\cdots d_r$ 整除每个这种 minor，故
$$
\boxed{
\sum_{\substack{|\zeta_*|=1\\1\le i\le r}}
\nu_{i,\zeta_*}
\le \deg(d_1\cdots d_r)\le4r\le52 .
}
\tag{29}
$$
五十二只界(28)的局部整除次数总和，不把恒等零行的系数数目计入，也不声称实际控制秩为52。z=0 不在相位圆上，其可能因子不产生新的 joint 门。

## 8. 必要性、充分性和同一个真实 gauge

若原光滑 joint 解存在，由(24)—(26)得光滑 $\zeta$。对(27)变换后的每一行，$d_i$ 的单位圆零点必须被 $\widetilde b_i$ 以相应阶数消去；零行必须恒零。因此(28)及零行条件必要。

反过来，若这些条件成立，取
$$
\xi_i(z)=\widetilde b_i(z)/d_i(z)\quad(i\le r),\qquad
\xi_i=0\quad(i>r),\qquad
\zeta=V\xi.
\tag{30}
$$
单位圆上的所有候选 pole 已准确可去；其他有限 pole 与单位圆有正距离，所以这些有理函数在一个包含整单位圆的环域中解析。令 $\eta=z^{-1}\zeta$。回到 $\theta$ 后，原 C、b 均实，故取 $\eta$ 的实部仍解(25)，且得到实解析、$2\pi$ 周期的相位系数。

代入(24)取得同一个实际 $k_\theta$，同时满足双 collar、两个 seed、完整 period 和原十三行。再按 R326 的同一全局第三 Gram 右逆支付剩余 $\mathcal W_e$ 部分，指定有理端口的完整 ruling 与第四 period 同时成立。这没有对两者各自另选 gauge。

换第4节的右逆或平台插值时，(22)使 $b_\theta$ 只加一个原 $C_\theta$ 列组合；故(25)、(27)—(28)的可解性不变。具体显示的 b 会变，不能将实际尾或平台值从其定义中删去。

## 9. 可控接口与仍未付的真实像

在固定最终 profiles、保护芽及原有限成本空间后，本稿给出的接口依次为：

- 由(6)、(10)、(14)定义的真实内部有序通量；
- 其零子空间上的固定线性 period 右逆，含实际间隙连接、总 $\int k'$ 修正和原右锚；
- 由该右逆、真实 incoming $m_*$ 及原 $2n$ 核列给出的有限多项式 joint 右端；
- 恒等零行与(28)的全部准确相位整除条件。

这些读出对相应固定实际成本/入历史数据线性，或在冻结背景后为仿射。整个低阶成本与 $m_*$ 仍由同一真实路径产生；本文没有将二者分开赋值，也没有因为能写有限矩阵就宣新增响应像满。

R345 已实际付的至多十一个对应 $V_d$ 点可在(14)中使用，其余点、$V_e$ 及(25)的相位兼容仍需真控制或真阻碍。若(3)尚未实际支付，则 R389 的原整包通量和两端条件也必须恢复，不能直接跳到本稿的(16)。

本稿的 iff 仅针对同一指定有理端口与完整第四 period。其余路径段 ruling、所有更高阶、Morse、固定旧度量上的变形、闭面嵌入和宏观可动性仍在本结论之外。新成果是把平台二次、全包尾、内部点、k 的值闭合以及十三行 seed/秩降分开后，给出了没有遗漏原常数或相位光滑性的准确有限目标接口。
