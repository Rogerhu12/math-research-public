# R259. 小核心直线同伦的共振条件、完整尾耦合与可去退化

日期：2026-11-14。

**状态。** 这是完整的条件代数推导，不报告新数值，不宣称存在一个小幅或大幅非线性解。它分析一个明确的备用设计路径：保持当前完整 scalar 公式、三个 prefix 支撑、物理 cut 与原尾，令前三个固定核心目标等于原目标的同一个倍数。结论仅约束这条直线路径，不能据此排除其他振幅路径。当前大幅求解及其原全部验收门不变。

参照：[R244 的圆段设计核](R244-circular-support-scalar-control-null-direction.md)、[R255 的精确圆线性化](R255-circle-reference-linear-isometry-and-coast-shear.md)、[R256 的精确约束消元](R256-exact-constraint-collocation-and-damped-descent.md)。实现中的完整边界仍是 R252 的物理角测试，而不是删去模式后的代理。

## 1. 固定设计家族与本结果的范围

把三个 scalar 控制记为 $p=(p_1,p_2,p_3)$，避免与径向速度混用。原完整设计函数写成

$$a(s;p)=a_{\rm base}(s)+\sum_{i=1}^3p_i b_i(s),\qquad 0\le s\le S.$$

三个 $b_i$ 是原已序列化的、互不相交的 prefix 内部六次 bump；每个 bump 在支撑两端的 $0,1,2$ jet 为零。固定整个 base prefix、AngleConnector、coast、finite bridge、cut、原尾参数和三个支撑，不用其他小幅解的 scalar 替换它。$p$ 可以沿**设计搜索**变化；这条搜索并非本题最后交付的同一 $g$ 的形变族。最终候选成立后，仍须按 R240 冻结整个 $p_*$ 和 $a(s;p_*)$，再做同 $g$ 精化。

保留全部 $M=T$ 个场模态和全部 $M$ 个尾输入。设原前三目标为 $A=(A_1,A_2,A_3)$。直线同伦是

$$c_j(\lambda)=\lambda A_j\quad(j=1,2,3),\qquad c_4,\ldots,c_M\text{ 自由},\qquad\lambda>0.$$

$\lambda=1$ 恢复原三个大幅目标。即使某个小 $\lambda$ 的完整有限 BVP 真正通过原门，它也只是一站，不能替代本题幅度、闭合、reach 或同度量精化标准。

下文使用的必要条件针对可微分支：$p(\lambda)\to p_0$，且 $c_j(\lambda)/\lambda$ 对全部自由高模有有限极限。若高模不趋于零或比 $\lambda$ 更大，便不属于该假设；不能用本结果排除这种另一分支。

## 2. 圆形子空间的源方程：不把返回 ap 冒充有限求积半径的导数

先区分源程序给出的两个函数

$$a(s;p)>0,\qquad \nu(s;p)=\text{该源返回的 ap},\qquad q=\nu/a.$$

若 $\nu=\partial_s a$，则是通常的精确标量几何情形。若 $a$ 由有限 Gauss 表达式计算、$\nu$ 由单独角函数返回，则该导数身份必须另付；本节不假定它。

原 Frenet 方程在圆形状态

$$F_0(s,\phi)=R(s)e_r(\phi)+Z(s)e_z$$

上的曲率为 $\kappa=1/R$，$N=-e_r$，$B=e_z$，所以

$$\alpha=-\frac{\nu}{a\kappa}=-qR,\qquad
R'=qR=:V,\qquad Z'=W:=\sqrt{1-V^2}.$$

因此真正的源圆轨道是

$$R(0)=1,\quad Z(0)=0,\quad R'=qR,\quad Z'=W,$$

在 $R>0$、$|V|<1$ 的分支上成立。只有在 $a(0)=1$ 且 $\nu=a'$ 时，由唯一性才有 $R=a$。这避免把有限 Gauss 半径的独立 ap/app 字段当作其准确导数。

### 2.1 圆点的完整线性化

令变分为 $u e_r+v e_\phi+h e_z$。直接微分 Frenet 标架得到

$$\delta\kappa=-\frac{u+u_{\phi\phi}}{R^2},\quad
\delta N=\frac{u_\phi-v}{R}e_\phi+\frac{h_{\phi\phi}}R e_z,\quad
\delta B=\frac{h_{\phi\phi}}R e_r-\frac{h_\phi}R e_\phi.$$

又 $\delta\alpha=-q(u+u_{\phi\phi})$，$\delta\beta=-(Vq/W)(u+u_{\phi\phi})$。代入 $\delta(\alpha N+\beta B)$，得到

$$u'=q(u+u_{\phi\phi})+\frac WRh_{\phi\phi},$$
$$h'=-\frac VRh_{\phi\phi}-\frac{Vq}W(u+u_{\phi\phi}),\qquad
v'=-q(u_\phi-v)-\frac WRh_\phi.$$

对 $k=2j$，写 $u=U_j\cos k\phi$，$h=H_j\cos k\phi$，$v=T_j\sin k\phi$。于是

$$\binom{U_j}{H_j}'=B_j\binom{U_j}{H_j},\qquad
B_j=\frac1R\begin{pmatrix}
V(1-k^2)&-Wk^2\\
V^2(k^2-1)/W&Vk^2
\end{pmatrix}.\tag{259.1}$$

并且 $\ell_j=U_j+kT_j$ 满足 $\ell_j'=q\ell_j$。这里仅使用 $a,\nu,R,W$，没有使用 app。

原物理 $\phi$ 核入口的单位系数满足 $U_j(0)=1$、$H_j(0)=0$、$T_j(0)=-k$，所以

$$T_j(s)=\frac{(1-k^2)R(s)-U_j(s)}k.\tag{259.2}$$

这与共同材料角下的入口相容。确切地，$\Theta_c(\phi)=\phi+\sum_j(1-k^2)c_j\sin(k\phi)/k$；在圆点固定 $\theta$ 反解时，切向项变为 $T_j-(1-k^2)R/k=-U_j/k$。径向 $U_j$ 和高度 $H_j$ 不变。因而不能把 raw $\phi$ 入口 $T_j=-k$ 错写成 $-1/k$，也不能因此误判两种坐标的高度传输不同。

## 3. 原有限 collocation 上也有可直接构造的圆基准

本节固定原节点 $s_0<\cdots<s_n$，不把连续圆轨道的采样值声明为已解的有限 collocation。原公式为

$$Y_m=(Y_L+Y_R)/2-h(f_R-f_L)/8,$$
$$\mathcal C=Y_R-Y_L-\frac h6(f_L+f_R+4f_m).$$

圆半径满足 $f_R^{\rm radius}=qR$。在一个 cell，令 $q_L,q_m,q_R$ 为原函数在三个位置的实际值，则其两个系数是

$$L_r=-1-\frac h6(q_L+2q_m)-\frac{h^2}{12}q_mq_L,$$
$$R_r=1-\frac h6(q_R+2q_m)+\frac{h^2}{12}q_mq_R.$$

若 $R_r\ne0$，可递推 $R_R=-L_rR_L/R_r$。中点半径必须使用原 Hermite 公式，而不是另取连续轨道值。检查全部这些半径为正、$1-(qR)^2>0$ 后，取相应 $W_L,W_m,W_R$，再递推

$$Z_R=Z_L+\frac h6(W_L+W_R+4W_m).$$

这在实数代数层恰满足圆子空间的原 collocation。浮点实现仍应把构造结果送回完整原 FFT 流、原中点和 RMS 查询，记录真实残差及域，不以代数推导替代机器回执。

每个非零模的 $(U,H)$ 切线 cell 使用 (259.1) 在**上述实际节点/中点半径**处的 $B_L,B_m,B_R$，其原完整切线块为

$$L_j=-I-\frac h6(B_L+2B_m)-\frac{h^2}{12}B_mB_L,$$
$$R_j=I-\frac h6(B_R+2B_m)+\frac{h^2}{12}B_mB_R.$$

如 $R_j$ 可逆，可作 $X_R=-R_j^{-1}L_jX_L$；若不可逆，传输实现失败，不等于 BVP 无解，应回到保持两端未知的同一线性系统。二维小块并不保证长程数值良态；需报告其条件、传播大小及重代回残差。这个有限基准和其线性化仍使用原场/原 scalar 方程，并未宣称有限 Fourier 场已精确等距或闭合。

## 4. 完整尾 Jacobian 给出的首阶必要条件

记真正完成的同一配置零高度尾 map 为 $D$，$D(0)=0$，其完整 slope Jacobian 为 $J_0\in\mathbb R^{M\times M}$。实际记录必须读取全部 $J_0$，量出非对角项；不能用 ready.linearD 替代，也不能预先截成三个对角数。

记原高度符号 $\epsilon_h$ 和 cut 系数 $\gamma=\epsilon_h\epsilon_r/\sqrt E$。在圆点，原材料换角的两个投影 $P,S$ 都是恒等；其 core 导数乘以零高度/零非均值 slope，故首阶右条件是

$$H'_j(S)\,C_j-\gamma\sum_{m=1}^M(J_0)_{jm}\epsilon_h H_m(S)\,C_m=0.$$

这里 $(U_j,H_j)$ 是单位 inlet core 的解；导数 $H'_j(S)$ 是原末端 RHS 的高度切线。定义完整矩阵

$$L(p)=\operatorname{diag}(H'_j(S;p))-
\gamma J_0\operatorname{diag}(\epsilon_h H_j(S;p)).\tag{259.3}$$

则任何上述可微直线分支必须满足

$$L(p_0)\binom{A}{d}=0,\qquad
d=\lim_{\lambda\to0}(c_4,\ldots,c_M)/\lambda.\tag{259.4}$$

**证明。** 对完整有限边界 map 关于 $c,p$ 在 $(0,p_0)$ 微分。所有 $p$ 的圆形状态都具有零非均值高度、零非均值 RHS 和零尾输入，所以仅改变 $p$ 的一阶贡献在右边界为零。这正是圆支的设计核。core 一阶变化依次通过原场切线、原完整 height map、$J_0$，给出 (259.3)。对路径除以 $\lambda$ 并取极限即得 (259.4)。证明既没有抹去 $p$ 的影响，也没有把圆点的 $p$ 列宣称非零；$p$ 通过 $L(p)$ 影响首阶传输。

### 4.1 有真实非对角耦合时的 Schur 条件

按低三行/列 $L$ 和其余行/列 $H$ 分块。若 $L_{HH}(p_0)$ 可逆，则

$$d=-L_{HH}^{-1}L_{HL}A,$$
$$f(p_0):=\bigl(L_{LL}-L_{LH}L_{HH}^{-1}L_{HL}\bigr)A=0.\tag{259.5}$$

不能在保留 $J_0$ 的非对角泄漏后，仍默认全部自由高 core 一阶值为零。只计算低三模式时，必须至少输出完整 $M$ 行泄漏，并把尚未求解的高块消元明确记为未支付。

### 4.2 对角情形及零目标例外

只有在所用实际 map 的 $J_0$ 对角、且其余模式没有相应共振时，才简化成

$$d_j(p)=H'_j(S;p)-\gamma\epsilon_h(J_0)_{jj}H_j(S;p),$$
$$A_jd_j(p_0)=0\quad(j=1,2,3),\qquad d_j(p_0)\ne0\quad(j>3).\tag{259.6}$$

如果三个 $A_j$ 都非零，直线分支因此需要三个首阶共振同时成立。若某个 $A_j=0$，其一阶方程恒为零；不能除以它，也不能声称仍有三个独立标量条件。需保完整向量方程，并在更高阶或另一分支参数化上分析。

## 5. 小正振幅为什么不自动消除退化；一个严格的条件续接定理

在未缩放未知量中，沿小幅分支的控制响应通常为 $O(\lambda)$；因此“从一个很小但正的 $\lambda$ 开始”本身并不提供一个良态 Newton 问题。若原 $p=0$ 不满足 (259.4)，简单缩小旧大核 warm 不会凭空成为接近非线性零点的种子。

设 $\mathcal R(c,p)$ 是某个明确的完整有限问题的右端约化 map：可以是有限模 ODE 的准确流与完整有限尾，也可以是在可解的原有限 collocation 中消去内部状态后得到的 map。假设其在所考虑的圆支附近为 $C^2$，且 $\mathcal R(0,p)=0$，$D_c\mathcal R(0,p)=L(p)$；原域及分支在一个共同邻域内保持。对 $C=(A,d)$ 定义

$$G(d,p,\lambda)=\begin{cases}
\mathcal R(\lambda C,p)/\lambda,&\lambda\ne0,\\
L(p)C,&\lambda=0.
\end{cases}$$

恒等式

$$G(d,p,\lambda)=\int_0^1D_c\mathcal R(t\lambda C,p)C\,dt$$

证明该延拓为 $C^1$。若 (259.4) 成立，且

$$\left[\;L_{[:,H]}(p_0)\quad
\partial_{p_1}L(p_0)C_0\quad
\partial_{p_2}L(p_0)C_0\quad
\partial_{p_3}L(p_0)C_0\;\right]\tag{259.7}$$

为可逆的 $M\times M$ 矩阵，则有限维隐函数定理给出某个 $\varepsilon>0$ 内的 $d(\lambda),p(\lambda)$，使完整有限问题对所有 $|\lambda|<\varepsilon$ 成立。在 (259.5) 可用时，此可逆性等价于高块可逆加上 $D_pf(p_0)$ 的 $3\times3$ 可逆性；这是对块矩阵作可逆消元的直接结果。

这个定理的假设需要真正核验。一个浮点很小的 $f(p_0)$ 或一次数值 SVD 不是上述存在证明；当前诊断只提供候选和条件性的数量证据。该局部结论也不保证路径可一直延到 $\lambda=1$，不保证大幅条件、曲率/reach 或接尾后的完整闭面条件。

## 6. scalar 全区间合法性与实际种子的责任

对任何候选 $p_0$，必须保持完整区间的 $a(s;p_0)>0$、$|\nu(s;p_0)|<1$，而不只是在699个节点通过。若使用第二节的实际源圆，还须检查其 $R>0$、$|qR|<1$；有限 collocation 圆则需其全部节点、中点和原 RMS 查询均在域内。控制只在 prefix 改动，故可对所有原 scalar 分片和控制支撑分裂后的多项式作全区间 Bernstein/区间核验，并把不变的 turn/coast/bridge 及其原有限求积定义完整纳入。有限 Gauss 函数的导数身份和普通浮点评值误差仍须依各自实际定义处理，不能用密网格通过冒全区间界。

若已得到合法候选，可从一阶全场构造一个**未接受**的 $\lambda>0$ 初猜：保持完整均值圆轨道，加全部求得的首阶 $r,t,z$，使用 (259.2) 的 raw $\phi$ 切向系数，并保留全部自由高 core。$\lambda$ 可按实际原 node/mid/RMS 域和首阶余量选取，但不能预先宣称余差为零。之后仍须：

1. 在实际完整场上重算原 RHS、原全部边界及其 Jacobian/FD；
2. 把完整材料角 $H$ 送入实际同配置的非线性尾，不沿用零响应冒新 $H$；
3. 通过原全部 RMS、BC、分支和最终 fresh audit 门；
4. 真正保存每个已接受 $\lambda$，再以可回退的参数续接推进到1；终点若未达幅度目标继续设计，不能在小幅分支收尾。

既有旧A完整闭包采用另一条 scalar 设计，不能作为这里保持同一完整公式的已接受 parent。它只能提供明确标注的几何/数值初猜经验；不得把旧A的成功身份搬到当前完整 scalar 上。

## 7. 本条件不覆盖非直线同伦

例如固定目标取

$$c_1=\lambda A_1,\qquad c_2=\lambda^2 A_2,\qquad c_3=\lambda^3 A_3$$

时，$\lambda=1$ 仍是原目标，但一阶低目标仅为 $(A_1,0,0)$。因此首阶只适用该向量版的 (259.4)，并不强制 $d_2=d_3=0$。在对角理想情形，二阶第二模和三阶第三模还分别含由低模非线性产生的强迫，可示意写成

$$d_2(p_0)A_2+Q_2(p_0;A_1)=0,$$
$$d_3(p_0)A_3+Q_3(p_0;A_1,A_2)=0,$$

并同时包含其他模态/控制展开的兼容条件。这里 $Q_2,Q_3$ 必须从完整场方程、材料换角和真正非线性尾的相应高阶导数推得，当前没有把它们设成零或计算出数值。该例严格说明直线的三重首阶共振不是所有设计同伦的强制门，但不提供另一条未经计算的成功路径。
