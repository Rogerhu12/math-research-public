# R326：同一全局二阶规范支付有理端口奇部、三维初值及剩余联合核

日期：2026-11-15。**完整纸面证明。** 没有执行求积、符号程序、人工测试、几何恢复或研究计算。

[R324](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md) 已在同一个实际圆上支付二次高度端芽的整个中心偶商。本稿支付此前尚未支付的两个部分：实际入历史造成的完整奇部，以及原三维 $\mathcal W_e$ 初值。使用的二阶、三阶规范都是沿整个闭几何定义的同一个 profile 家族，不在各端口重置历史。

这项支付有一个必须保留的全局代价：二阶规范改变原第四周期。本文给出该改变的准确两个系数，并把后续“保持已付端口，同时修正周期”的同一二阶规范写成明确联合方程。没有从一个端口可解推出整个闭路径或全局第四 range 可解。

来源：[R47 三矩右逆](R47-fourth-order-range-and-third-gauge.md)、[R56 原完整恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 八矩原算子](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R183 八完整副本](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R184 同一规范的完整 joint 判据](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R259 真二次尾](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R312 原式中心比较](R312-quadratic-height-ports-and-rational-arctangent-logarithmic-ruling.md)、[R321 单反正切原系数](R321-complete-single-arctangent-gates-and-ten-dimensional-joint-control.md)与 R324。

## 1. 固定同一实际几何、圆、锚和目标

固定 R324 已经构成的实际有限圆 $(f,g)$，以及 R312 从起点安装、随后冻结的实际闭几何。整个几何满足
$$
M_{\rm total}=0,\qquad T_{\rm total}=\tau\mathfrak H,\qquad \tau\ne0.
\tag{1}
$$
这里 $\tau$ 是整个第三算子的系数，**不是**下文端芽的局部曲率 $\kappa$。同一固定目标、原右锚和全路径起点均不变。

令
$$
\phi_\theta=f\cos\theta+g\sin\theta,\quad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,\quad
\Delta=f\odot f-g\odot g.
\tag{2}
$$
圆的三个真实二次矩为零：
$\mathbf I(D_\theta)=0$。原二、三阶完整 range 已付，canonical 高阶场在 $\theta=0,\pi$ 为零。所有本稿规范也保持这两个准确种子。

在一个指定的实际端口，沿同一个物理坐标采用
$$
h=H(1+\varepsilon\sigma^2),\quad
H>0,\quad\varepsilon>0,\quad k=\kappa\ne0,\quad\omega=0,
$$
$$
K=1+\kappa^2,\quad e_{\rm g}=hx-\kappa,\quad
Q_{\rm g}=1+e_{\rm g}^2,\quad\gamma=2H\varepsilon\sigma .
\tag{3}
$$
这只是 R312 已付的共同坐标写法，不再次移动 profiles 或更换目标度量。

对 profiles 的原三矩记为
$$
I_0(a,b)=\int a''b'',\qquad
I_1(a,b)=\int xa''b'',\qquad
I_2(a,b)=\int(x^2a''b''+2a'b').
$$
端口的真实齐次配对是
$$
\mathcal E_h(a,b)
=\frac K{4h}I_0(a,b)-\frac\kappa2I_1(a,b)+\frac h4I_2(a,b).
\tag{4}
$$
三个几何函数独立，故
$$
\mathcal W_e=\operatorname{span}_{\mathbb R}\{h^{-1},1,h\}.
\tag{5}
$$
所有 $\mathcal W_e$ 系数都是与 $\sigma$ 无关的真实常量；可以依赖相位。

## 2. 原八复制还准确清掉所有 E8 三次配对

本节提取已经使用的八完整副本的一项准确后果，不增加新的形状观察或重求 R324 的圆。

对 R324 的实际最终圆，有
$$
\boxed{
I_j\{a,\Phi_X(b,c)\}=0,\qquad
a,b,c\in\operatorname{span}_{\mathbb R}(f,g),\
X\in E8,\quad j=0,1,2 .
}
\tag{6}
$$

**先保真实跨尾。** 若 $a$ 真紧而 $p=Ax^2+Bx+C$，直接 IBP 给
$$
I_0(a,p)=I_1(a,p)=0,\qquad
I_2(a,p)=2A\int x^2a''+2\int a'(2Ax+B)=0.
\tag{7}
$$
最后一式中两项分别是 $4A\int a$ 与 $-4A\int a$；不能省略原 $I_2$ 的一阶导项。

所有 E8 算子的输入由同点的两个 profiles 及其导数组成，再施原右积分。不同完整副本的两个输入没有重叠，故其二次交叉输入准确为零。一个副本的二次输出在它右方为零、在它左方为 R259 所列的真实二次多项式尾。与另一完整副本的 outer 配对于是由(7)为零，不需要任何单副本的二次尾本身为零。

**同副本的有限差分。** 把 outer、两个 inner 一起平移 t。在原 E8 表中，局部坐标和 primitive 权的总平移次数至多四；再加 $I_j$ 的外权至多二，得到
$$
t\longmapsto I_j\{a(\,\cdot-t),\Phi_X(b(\,\cdot-t),c(\,\cdot-t))\}
\quad\text{次数至多六}.
\tag{8}
$$
这一结论可以直接从 $J_0,J_1,J_2$ 及 R259 的八个原二次式读取。原右锚仍在所有支撑右方；换元后积分至右零 collar，不产生额外初值。对两个不同 inner 用原双线性极化，次数界不变。

原八副本使用等距 $t_\ell=t_0+\ell L$ 和真实幅度
$$
\alpha_\ell=(-1)^\ell\binom7\ell^{1/3},\qquad 0\le\ell\le7.
$$
每项三次配对乘
$\alpha_\ell^3=(-1)^\ell\binom7\ell$，所以第七有限差分准确消掉(8)。这证明单个已完成基本块的(6)。

R324 的每一次有限频率修改都同步复制到同一基本块的八个实际副本，并没有在这八处分别选独立形状。因此上述结论对最终实际形状仍准确成立。后续十二完整副本、共同缩放和最后五个完整块的正幅组合继续保持(6)：每个完整块自身已经为零，跨块仍由(7)为零。g 的整块翻号也不改变零。

因此(6)是真实最终圆的既有恒等式；不是把某个未加入的三次约束偷偷并入 R324 的有限纤维。其列数可以冗余，本稿不据此作任何秩声明。

## 3. 由真实入矩阵确定的一个全局合法二阶规范

令 $\mathsf m_*$ 为**原整个路径**走到本端口中心时的真实累计第二矩阵。它由此前全部路径确定，不可自由指定。设
$$
X=\Phi_{\mathsf m_*},\qquad
w_\theta^*=XD_\theta,\qquad
\boxed{w_\theta^{\,c}=-XD_\theta.}
\tag{9}
$$

原 $\mathbf I(D_\theta)=0$ 使 $XD_\theta$ 的三个二次左尾准确消失；右尾原本为零。因此(9)是同双 collar 的实紧 profile，随相位光滑、$2\pi$ 周期，并在 $0,\pi$ 为零。

由(6)，
$$
\mathbf I(f,w_\theta^{\,c})
=\mathbf I(g,w_\theta^{\,c})=0.
\tag{10}
$$
于是对于整个实际闭几何的权
$$
\mathbf w_{\rm glob}(s)=
\left(\frac{d(s)^2+1}{4h(s)},\frac{d(s)}2,\frac{h(s)}4\right),
$$
有
$$
\mathbf w_{\rm glob}(s)\cdot
\mathbf I(\phi_\theta,w_\theta^{\,c})=0
\quad\text{对全部 }s,\theta .
\tag{11}
$$
R184 的准确第三合法性条件被全局支付；又由(1)，新增第三 forcing 的整个周期为零。

采用 R184 的号：
$$
\widetilde Z_\theta=Z_\theta-Y_{w_\theta^{\,c}},\qquad
\widetilde U_\theta
=U_\theta+2Z_B(\phi_\theta,w_\theta^{\,c}).
\tag{12}
$$
$U$ 在这里是第三阶场，不是 R312 的第三 characteristic 原函数。式(12)中的 $Z_B$ 使用同一原右锚和全路径起点。它们是原全局合法的二、三阶场，未改变几何、f、g、固定目标或首阶圆。

负号不能改成正号：原第二恢复是 $Z=\widehat Z-Y_{XD}$，所以只有(9)使实际 $\widetilde Z$ 在此端口等于中心场。

## 4. 完整奇部消去时保住平方和真实第三初值

端口内原累计 history 准确为
$$
\mathsf m(\sigma)=\mathsf m_*+\mathsf o(\sigma),\qquad
\mathsf o(-\sigma)=-\mathsf o(\sigma).
$$
R312 §3.1 的真实比较给
$$
Z=\widehat Z-Y_{w^*},\qquad
U=\widehat U+2\widehat Z_B(\phi,w^*)+Y_{\chi^*}.
\tag{13}
$$
$\chi^*$ 是与 $\sigma$ 无关的真实齐次初值差。它可以带左尾；这里不把它预授为一个可任意加入的紧全局 gauge。

同一原第二恢复还给
$$
Z_B(\phi,w^*)=\widehat Z_B(\phi,w^*)-Y_{X(\phi,w^*)}.
$$
将它和(9)代入(12)，得到准确场身份
$$
\boxed{
\widetilde Z=\widehat Z,\qquad
\widetilde U=\widehat U+Y_{\chi^c},\qquad
\chi^c=\chi^*+2X(\phi,XD).
}
\tag{14}
$$
这里没有把中心第三初值重置为零。

令 $\mathscr K=-\mathfrak b(Z,Z)-2\mathfrak b(Y_\phi,U)$ 为完整第四 ruling。因为 outer $\phi$ 真紧，原 R221 的尾公式仍给
$\mathfrak b(Y_\phi,Y_{\chi^c})=\mathcal E_h(\phi,\chi^c)$，不要求比较用的 $\chi^c$ 自身先紧。因此
$$
\boxed{
\widetilde{\mathscr K}_\theta
=\widehat{\mathscr K}_\theta
-2\mathcal E_h(\phi_\theta,\chi_\theta^c).
}
\tag{15}
$$

也可直接核 gauge 平方没有被删除。R312 原比较是
$$
\mathscr K^0
=\widehat{\mathscr K}+\widehat{\mathcal B}(w^*)
-\mathcal E_h(w^*,w^*)-2\mathcal E_h(\phi,\chi^*).
$$
R184 在 $w=-w^*$ 的线性响应为
$$
-\widehat{\mathcal B}(w^*)+
2\mathcal E_h(w^*,w^*)-4\mathcal E_h\{\phi,X(\phi,w^*)\},
$$
其额外平方仍为 $-\mathcal E_h(w^*,w^*)$。三项平方系数 $-1+2-1$ 准确相消，剩下的正是(15)，而不是把平方从未取商的方程中省掉。

R324 已付
$\widehat{\mathscr K}_\theta\in\mathcal W_e$ 对全部相位成立。由(4)、(15)，
$$
\boxed{\widetilde{\mathscr K}_\theta\in\mathcal W_e
\quad\text{作为本端口的完整实际函数}.}
\tag{16}
$$
右侧全部偶。因此原先未支付的**完整奇部**现已准确消去；这不再只是对偶部取商。

## 5. 一次全局第三规范支付原三个初值

由(5)、(16)，唯一写成
$$
\widetilde{\mathscr K}_\theta
=A_{-1}(\theta)h^{-1}+A_0(\theta)+A_1(\theta)h .
\tag{17}
$$
三个系数含真实 $\mathsf m_*$、$\chi^*$ 和原中心恢复。它们没有被宣布为零。可取三个固定、h 值不同的端口点反解常系数；此处只是证明定义，不执行采样。其关于相位光滑、周期，在 $0,\pi$ 为零。

置
$$
v_\theta=\left(
\frac{2A_{-1}(\theta)}K,\
-\frac{A_0(\theta)}\kappa,\
2A_1(\theta)\right).
\tag{18}
$$
则端口上 $2\mathbf w_{\rm glob}\cdot v_\theta
=\widetilde{\mathscr K}_\theta$。

对非零紧 profile $\phi$，R47/R184 已证明 $\chi\mapsto\mathbf I(\phi,\chi)$ 到 $\mathbb R^3$ 满射，其 adjoint 密度是
$$
L_0\phi=\phi'''',\quad
L_1\phi=x\phi''''+2\phi''',\quad
L_2\phi=x^2\phi''''+4x\phi'''.
$$
f、g 实线性无关，故每个 $\phi_\theta$ 非零。真实 Gram 矩阵
$$
G^\theta_{ij}=\int(L_i\phi_\theta)(L_j\phi_\theta)
$$
严格正定，其逆在紧相位圆上光滑有界。准确选择
$$
\boxed{
\zeta_\theta
=\sum_{j=0}^2[(G^\theta)^{-1}v_\theta]_jL_j\phi_\theta .
}
\tag{19}
$$
这是一个同 collar、实、光滑周期的**全局** profile 家族，且种子处为零。由 $\mathbf I(\phi_\theta,\zeta_\theta)=v_\theta$，在(12)的第三场上加 $Y_{\zeta_\theta}$，得到
$$
\boxed{\mathscr K_\theta^{\,c}=0
\quad\text{在指定实际端口的全部 }\sigma,\theta.}
\tag{20}
$$

这一步真实支付三维初值，而非把它们重新置零。第三规范不改变第四整个周期，因为该改变是 $-2\Phi_{M_{\rm total}}(\phi,\zeta)=0$。

它在整个闭路径的 ruling 改变仍是
$$
-2\mathbf w_{\rm glob}(s)\cdot v_\theta .
\tag{21}
$$
其他几何段一般会受影响；本稿没有称它们保持原值或已经可解。

## 6. 同一二阶规范的全局周期代价

R184 的准确全函数公式在(1)下为
$$
\Delta V_\theta=2\tau L_f(w_\theta),\qquad
L_f(w)=\mathfrak H(w;f,f).
\tag{22}
$$
它不是某个 scalar 积分，也不是只取周期的一个 Fourier 系数。

对(9)，
$$
\boxed{\Delta V_\theta=-2\tau L_f(XD_\theta).}
\tag{23}
$$
保留原 universal pure-zero 后，设 canonical 周期写成
$$
V^0_\theta=\sin^2\theta\,V_d
+2\sin\theta\cos\theta\,V_e .
$$
因为
$D_\theta=\sin^2\theta\,\Delta
-2\sin\theta\cos\theta(f\odot g)$，(23)给
$$
\boxed{
V_d^c=V_d-2\tau L_f(X\Delta),\qquad
V_e^c=V_e+2\tau L_f(X(f,g)).
}
\tag{24}
$$
两个量均是真实固定的 profile 函数；没有从(20)推它们为零。第三规范(19)不再改变(24)。

因此“全端口已付”的新成果不能与“第四周期已付”混称。所用的 w 只有(9)这一个，原 incoming 矩阵并没有因中心记号变成可控参数。

## 7. 保持新端口的后续规范：完整十个显式线性门

继续只允许 R184 的真实全局规范。任意后续二阶选择写成
$$
w_\theta=w_\theta^c+k_\theta.
$$
种子、相位和双 collar 条件仍要求于同一个 $k_\theta$。由于(11)，第三合法性只需检验 k。又本端口三权独立，故对整个几何的合法性在这里等价于
$$
\boxed{\mathbf I(\phi_\theta,k_\theta)=0.}
\tag{25}
$$
必要性由本端口推出，充分性对整个 s 范围由三个常矩为零推出。

由 R184 的原线性响应和(14)，新 ruling 取模 $\mathcal W_e$ 后，只剩中心的
$$
\begin{aligned}
\widehat{\mathcal B}_\theta(k)
={}&2\mathcal T_\sigma(k;D_\theta)
-4\mathcal T_\sigma(\phi_\theta;\phi_\theta,k)\\
&-2\mathcal E_h(\mathsf oD_\theta,k)
+4\mathcal E_h\{\phi_\theta,\mathsf o(\phi_\theta,k)\}.
\end{aligned}
\tag{26}
$$
原 global $Z_B$ 与 centered $\widehat Z_B$ 的差、现有 $\chi^c$、新旧 gauge 的平方和交叉都只增加 $\mathcal W_e$ 项。没有把它们在未取商式中删掉。

$\mathcal T_\sigma$ 和 $\mathsf o$ 奇，(4)的权偶，所以(26)为奇。要保持端口商为零，必要且充分的是
$\widehat{\mathcal B}_\theta(k)\equiv0$；一个非零奇函数不能由第三规范的偶空间 $\mathcal W_e$ 支付。

以下列出这个全函数条件的原式坐标。写
$$
\mathsf o=\sigma\mathsf A(h)+EB,\qquad
E=\frac{\arctan(\sqrt\varepsilon\,\sigma)}{\sqrt\varepsilon},
\quad\mathsf A(h)=\sum_{p=-3}^{1}h^pA_p.
\tag{27}
$$
以原 E8 方向 $R=r_1,L=p_0,U=s_1,T=t_1,V=p_2,P_1=p_1$，
$$
a=\frac{K(\varepsilon-2K)}{32H^2},\quad
e=\frac{\kappa K}{4H},\quad t=-\frac{\varepsilon}{4},
\qquad B=aR-2eL+eU+tT,
$$
$$
\begin{aligned}
A_{-3}&=-K\varepsilon HR/12,&
A_{-2}&=K\varepsilon R/48,\\
A_{-1}&=HaR+\varepsilon HT/4,&
A_0&=\kappa^2P_1-KT/8-\kappa HV/3,\\
A_1&=-\kappa V/6 .
\end{aligned}
\tag{28}
$$
这些是 R312/R321 的真实 centered history，不是新选的拟合基。

令
$$
H_{X,j,\theta}(k)=
-I_j(XD_\theta,k)
+2I_j\{\phi_\theta,X(\phi_\theta,k)\}.
\tag{29}
$$
保留原 $J$ 与全尾的局部 pairing 记为
$\mathcal T_\sigma=\gamma\mathcal T_h^\#$。为使(26)完全可审，原式是
$$
\begin{aligned}
\mathcal T_h^\#(c;a,b)=\frac1{32h^4}\int\big[&
Q_{\rm g}^2c'''(a'b''+a''b'-xa''b'')\\
&-2he_{\rm g}Q_{\rm g}c'''a'b'\\
&+F_c\{(K-h^2x^2)a''b''-2h^2a'b'\}\big],
\end{aligned}
$$
$$
F_c=Q_{\rm g}c''-2he_{\rm g}c'+2h^2c .
\tag{30}
$$
(26)中的 outer k 或 $\phi$ 都真紧，inner 槽也真紧，所以此处直接处于 R221 原完整 pairing 的适用范围，没有把某个非紧 self 的缺失边项隐藏进(30)。

定义七个线性泛函
$$
\begin{aligned}
P_{\ell,\theta}(k)=[h^\ell]\bigg[
&2H\varepsilon\{
\mathcal T_h^\#(k;D_\theta)
-2\mathcal T_h^\#(\phi_\theta;\phi_\theta,k)\}\\
&+\sum_{p=-3}^{1}\left\{
\frac K4h^{p-1}H_{A_p,0,\theta}(k)
-\frac\kappa2h^pH_{A_p,1,\theta}(k)
+\frac14h^{p+1}H_{A_p,2,\theta}(k)
\right\}\bigg],
\end{aligned}
\quad -4\le\ell\le2.
\tag{31}
$$
原 $\mathcal T_h^\#$ 只含 $h^{-4},\ldots,h^0$，所以没有范围外的有理系数。由 $\gamma=2H\varepsilon\sigma$，
$$
\boxed{
\begin{aligned}
\widehat{\mathcal B}_\theta(k)
={}&2\sigma\sum_{\ell=-4}^{2}h^\ell P_{\ell,\theta}(k)\\
&+2E\left\{
\frac K{4h}H_{B,0,\theta}(k)
-\frac\kappa2H_{B,1,\theta}(k)
+\frac h4H_{B,2,\theta}(k)\right\}.
\end{aligned}}
\tag{32}
$$
原 E 对有理函数的单值差非零，故不可能是有理函数。于是(32)恒零先迫 E 的有理系数零；再由 $h^{-1},1,h$ 独立，以及 $\sigma h^\ell$ 的独立性，得到准确等价
$$
\boxed{
P_{\ell,\theta}(k)=0\ (-4\le\ell\le2),\qquad
H_{B,j,\theta}(k)=0\ (j=0,1,2).
}
\tag{33}
$$
这是十个列出的全函数系数条件，不宣称它们线性独立或其映射满射。

## 8. 真正剩余的同规范联合问题

对固定相位定义
$$
\mathscr N_\theta=
\{k\in C_c^\infty(I;\mathbb R):
\mathbf I(\phi_\theta,k)=0,\ 
P_{\ell,\theta}(k)=0,\ 
H_{B,j,\theta}(k)=0\}.
\tag{34}
$$
它由十三个显示的线性泛函给定，可能有冗余；不能把十三写成控制秩。

在已经支付的这一个端口上，后续二阶规范保留第三合法性及端口商，当且仅当 $k_\theta\in\mathscr N_\theta$。此时新的偶 $\mathcal W_e$ 剩余，包括完整新平方和交叉，仍由同一个全局第三 Gram 右逆支付。

因此保留这个端口并支付第四周期的准确剩余方程是
$$
\boxed{
k_\theta\in\mathscr N_\theta,\qquad
2\tau L_f(k_\theta)=-V_\theta^c
\quad\text{作为整个 }I\text{ 上的函数}.
}
\tag{35}
$$
还须同一 $k_\theta$ 随相位光滑、周期并在 $0,\pi$ 为零。逐相位有解不自动给光滑家族；核秩改变等问题不能被“点态满射”字样略过。

式(35)是**指定端口加第三合法性加完整第四周期**的准确接口。要获得整个闭路径第四 range，还必须在其他全部几何段施加 R184 的原 joint ruling 条件，而且仍使用这同一个 k 和同一个第三规范。不能给每个端口另选 $\mathsf m_*$、二阶 w 或独立三维向量后拼接。

## 9. 本次真实支付与下一未付问题

本稿在 R324 的同一实际圆、同一已冻结几何与目标上，完成了指定有理端口的完整奇部和三个真实初值的支付。所需规范由真实入矩阵、原八复制和原三矩 Gram 显式给出，不需另一个高频存在性定理或新的数值搜索。

付出的全局周期改变是(24)，其他 s 段的改变包含(21)。二者都必须保留。下一具体问题是(35)的全函数像及其与其他段 ruling 的共同限制，而不是再次证明已付十九个偶部 principal 的秩。

本稿没有证明(35)已有解，没有证明全局第四校正、平台/flux 与内部逆解的所有联合条件，更没有证明高阶收敛、有限非零参数的精确等距族、闭面嵌入、reach 或握持幅度。新结果是：在原合法规范范围内，**该实际有理端口本身已能完整支付**；它留下的是一个保真成本、同一未知函数的全局联合问题。
