# R355：两种真实四阶排序与有限正宽支付 Y–W 的完整第二外矩

日期：2026-11-15。**完整有限纸面建设性证明；未执行求积、符号程序、研究计算、人工检查或数值扫描。**

[R353](R353-ordered-tails-and-three-positive-centers-pay-the-positive-minus-two-first-moment.md) 已支付 $Y$–$W_*$ 的完整第一外矩。本稿使用另外四个真实强块，支付同一 pair 的**完整第二外矩**，并把其旧面积、原尾和 $\Psi$ 代价全部接入实际正锥。

本文给原全正支撑分支的独立补偿器。同期 [R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md) 已在重新构造且具有真实正 $x+\omega$ 间隙的几何上，由完整反射一次支付包括本目标在内的三个矩，得到16个外矩；本文不把本目标再计成该分支的第17个矩。

关键并非仅将 R353 的六行矩阵添两行。第二矩的原 self 恰分成一个 $L/U$ 第一矩和一项真实有序 $\mu_2$ 尾。先在每个新原型上准确解 $\mathcal C_1=0$，局部余项是 $\delta^3$，有序尾是 $\delta$；两个真实排序使它们同时反号。四个有限正宽给出非退化二维正锥。

来源：[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md)、[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R271](R271-six-complete-blocks-pay-the-first-two-positive-negative-Gaussian-moments.md)、[R291](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)、[R343](R343-two-real-orders-and-positive-center-clusters-pay-the-third-Gaussian-second-moment.md)、[R346](R346-positive-six-target-cone-pays-a-further-complete-Gaussian-zero-moment.md)、[R348](R348-true-translation-and-Green-self-terms-pay-the-first-positive-minus-one-Gaussian-moment.md)、[R349](R349-complete-second-self-and-positive-cone-pay-the-fourth-Gaussian-area.md)、R353。

## 1. 原目标与两条完整 nonlegal self

沿用 R353 的 $P,R,S,L,U,Y,W_*=aR+bS,Z_*=dL+eU$、
$\mathcal M_j,\mathcal A_j,\mathcal B_j,\mathcal C_j,\mathcal P_j,\mathcal D_j$，
同一右锚与真实 $M=0,T=\kappa_H\mathfrak H$ 几何。
$0<t=\kappa^2<1/100$，原系数仍为
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e}.
\tag{1}
$$
本稿目标为
$$
\mathcal D_2(\theta)=I_2\{\phi_\theta,[W_*,Y](\phi_\theta;D_\theta)\}=0,
\quad D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{2}
$$
$I_2(u,w)=\int(x^2u''w''+2u'w')$；第二项从未删去。

取任意实紧 $u$，写 $v=u',r=u''$，
$C=J(x^2r^2+2v^2)$、$\mu_j=I_j(u,u)$。
原 self $S_{X,Y,j}=2I_j\{u,[X,Y](u;u^2)\}$ 满足
$$
\boxed{
S_{R,Y,2}=2S_{L,Y,1}-S_{U,Y,1},\qquad
S_{S,Y,2}=-S_{U,Y,1}-\frac{\mu_2^2}{4}.
}
\tag{3}
$$
右边两个第一 self 是 R348 的完整 nonlegal 原式，不是只在三矩为零时成立的对角式。

### 1.1 直接由原 cubic 和 Green 推导

原 local cubic 为
$$
F_{R,2}=\int(x^2r^3-4xvr^2+2ur^2),\qquad
F_{S,2}=\int(x^2r^3-2xvr^2).
\tag{4}
$$
R291 已付 $F_{Y,2}=0$ 的完整 local 身份；仍按 R259 原 local 变分／Green 接口使用它，不把 $R(u,u),S(u,u)$ 当作紧方向。

在 $D_{\rm loc}F_{S,2}[Y(u,u)]$ 中，$C$ 的准确系数为
$$
2xvr-\frac{x^2r^2}{2}
=(xv^2)'-\frac{x^2r^2+2v^2}{2}.
$$
由于 $C'=-(x^2r^2+2v^2)$、$C_{\rm left}=\mu_2$，
这部分完整等于
$$
\int xv^2(x^2r^2+2v^2)-\frac{\mu_2^2}{4}.
\tag{5}
$$
剩余含 $r'$ 的项为
$$
3x^4ur^2r'-5x^5vr^2r'-4x^3uvrr'
+4x^4v^2rr'+\frac32x^6r^3r'.
$$
分别按 $(r^2)'/2,(r^3)'/3,(r^4)'/4$ 积分，并合并原 local 项，
准确得到 $-S_{U,Y,1}$，外加(5)的真实 $-\mu_2^2/4$。

另一方面
$$
F_{R,2}-F_{S,2}=2\int(u-xv)r^2.
$$
其变分中的 $C$ 系数为
$$
\frac{x^2r^2}{2}-2ur+2xvr
=(-2uv+xv^2)'+\frac{x^2r^2+2v^2}{2}.
$$
因此真 primitive 给
$$
\int(-2uv+xv^2)(x^2r^2+2v^2)+\frac{\mu_2^2}{4}.
\tag{6}
$$
剩余含 $r'$ 的部分为
$$
4x^2(u-xv)^2rr'+2x^4(u-xv)r^2r'.
$$
IBP 后的完整 local 正好是 $2S_{L,Y,1}$。
合(5)、(6)即得(3)的 local 和尾项。

$I_2$ 的 Green concomitant 是
$$
\begin{aligned}
g_2(X,Y)={}&x^2(X'''Y-X''Y'+X'Y''-XY''')\\
&+2x(X''Y-XY'')-2(X'Y-XY').
\end{aligned}
\tag{7}
$$
对二次多项式 $X=Ax^2+Bx+C_0,Y=Dx^2+Ex+F$，
它等于 $2(C_0E-BF)$。
原 $Y(u,u)$ 左尾为 $-\mu_2x^2/4$，
故与 $R$、$S$ 的真实 affine 尾配对均为零。
没有单包三矩假设；(3)中的 $-\mu_2^2/4$ 因而必须保留。

## 2. 全角完整尾的准确二次化

R259 的跨核仍为
$$
\Gamma_{R,Y,2}=0,\qquad
\Gamma_{S,Y,2}(\boldsymbol\mu,\boldsymbol\nu)
=-\frac{\mu_2\nu_2}{2}.
\tag{8}
$$
置
$$
X=2aL-(a+b)U.
$$
对真实不交 rank-one 包
$f=\sum a_i u_i,\ g=\sum b_i u_i$，写
$c_i=a_i\cos\theta+b_i\sin\theta$、
$d_i=a_i^2-c_i^2$、$m_i=I_2(u_i,u_i)$。
由(3)、(8)，完整 $2\mathcal D_2$ 是
$$
\boxed{
2\mathcal D_2
=\sum_i c_i^2d_i\,S_{X,Y,1}(u_i)-\frac b4 Q_2(\theta),
}
\tag{9}
$$
$$
Q_2(\theta)=
\sum_i c_i^2d_i m_i^2+
2\sum_{i<j}c_i^2d_jm_im_j.
\tag{10}
$$
$i<j$ 是实际左至右顺序。

完整 inner $D_\theta$ 的第二矩为零，即 $\sum d_i m_i=0$。
只在这个完整层级使用它，得到
$$
Q_2(\theta)=
\sum_{i<j}(a_i^2d_j-a_j^2d_i)m_im_j.
\tag{11}
$$
所以 $Q_2$ 只有 $\sin^2\theta$ 和 $\cos\theta\sin\theta$ 两项；
原十二完整副本清掉 odd 项。特别它没有独立的
$E_{22}-E_{04}$ 分量。这不意味着它为零。

取原两斜率
$$
\alpha=\frac9{20},\quad \beta=\frac{5-\alpha}{1-\alpha}
=\frac{91}{11},\quad q=\frac1{16(1-\alpha)^2}
=\frac{25}{121},\quad n=2^{11}.
\tag{12}
$$
每个最小包满足
$a_i^2(a_i^2-5b_i^2)=\alpha\beta\,b_i^2(a_i^2-b_i^2)$。
因 $X$ 为 $L/U$ 组合，其跨核全零，故(9)的 local 部分恰沿
$$
h_\alpha=(\alpha\beta,1)
$$
这个 even 方向；ordered 项沿 $h_1=(1,1)$。
$\alpha\beta\ne1$，两个方向独立。

## 3. 同一真实母小族上准确解旧 C1

使用 R346§5 已构造的真实 even 母小族
$$
\mathcal F_\kappa(v_\tau)=0,\qquad
\mathcal J(v_\tau)=h_m\tau,\qquad |\tau|<\tau_*,
\tag{13}
$$
其中母宽 $h_m>0$ 已固定，全部有限维 IFT Jacobian 已在真实正宽上非退化。
没有假定任意母函数 regular，也没有给母积分任意赋值。

对每个实际 $v_\tau$，定义
$$
C_4=\int(v_\tau'')^4,\quad X_2=\int y^2(v_\tau'')^4,\quad
N=\int yv_\tau'(v_\tau'')^3,
$$
$$
W=3\int(v_\tau')^2(v_\tau'')^2+\int v_\tau(v_\tau'')^3,\quad
\mathcal J=W-2N,\quad \nu=I_2(v_\tau,v_\tau)/I_0(v_\tau,v_\tau).
$$
R349 的准确母身份是
$$
X_2-C_4\nu=\frac85N-\frac{16e}{5(d+7e)}\mathcal J.
\tag{14}
$$

对任意 $A_{\lambda,\mu}=\lambda L+\mu U$，记
$$
a_4(\lambda,\mu)=\frac{5(\lambda-5\mu)}{24},\qquad
\Gamma_{\lambda,\mu}
=\frac{\lambda(d+3e)-\mu(3d+e)}{d+7e}.
$$
其原母常数 $\mathscr D_{\lambda,\mu}$ 是 R270(11)中
$d,e$ 换为 $\lambda,\mu$ 的同一个实际积分，保全部项。
令完整 copy 的实际中心矩为 $\bar V_H,\bar V_L,\bar M_{4,H},\bar M_{4,L}$，
$$
V_\rho=\bar V_H-q^2\bar V_L,\quad
G_\rho=C_4\{\bar M_{4,H}-\bar M_{4,L}+6\nu V_\rho\},\quad
w_4=1-q^4.
$$
所有位置都包括真实八／十二副本，$\rho=0,20$ 为原两个实际排序。
R348／R349 的完整第一矩准确写成
$$
\boxed{
E_{04}^{A_{\lambda,\mu},1}
=2K\delta\xi\left[
\Gamma_{\lambda,\mu}\mathcal J
\left\{\frac{(1-q^2)\xi^2}{3}+\delta^2V_\rho\right\}
+\delta^2\{a_4(\lambda,\mu)G_\rho+
\mathscr D_{\lambda,\mu}w_4\}\right],
}
\tag{15}
$$
$K=64nq(1-\alpha)\mathcal W>0$，
$\xi>0$ 为最终真实中心，$\mathcal W$ 为全部复制四次权和。
$E_{04}$ 始终是完整 $2I_1$ 的 raw 系数。

取
$$
\Gamma_Z=\Gamma_{d,e}=\frac{d^2-e^2}{d+7e}\ne0.
$$
将(15)的方括号对 $A_{\lambda,\mu}=Z_*$ 置零。
在 $(\tau,\delta^2)=(0,0)$，其 $\tau$ 导数是
$$
\Gamma_Z h_m(1-q^2)\xi^2/3\ne0.
$$
因此在每个最后位置、每个有限 $A$ 与排序固定后，存在真实
$$
\tau=\tau_\rho(\delta^2;\xi)=O(\delta^2)
$$
使
$$
\boxed{\mathcal C_1(\theta)=0\quad\text{对全部 }\theta.}
\tag{16}
$$
这里使用同两斜率的准确 $E_{22}=\alpha\beta E_{04}$ 和已付 odd；
不是只把某个 leading 系数设零。

## 4. 消 C1 后的 local 余项仍是原完整值

对 $X=2aL-(a+b)U$，写
$$
\Gamma_X=\frac{(5a+3b)d+(7a+b)e}{d+7e},\qquad
r_*=\Gamma_X/\Gamma_Z.
$$
用(16)从(15)中减去 $r_*$ 倍 $Z_*$ 行，$\mathcal J$ 的两项同时准确相消：
$$
\boxed{
E_{04}^{X,1}
=2K\delta^3\xi\left[
\zeta_\kappa G_\rho+
(\mathscr D_X-r_*\mathscr D_Z)w_4
\right],
}
\tag{17}
$$
$$
\begin{aligned}
\zeta_\kappa
&=a_4(X)-r_*a_4(Z_*)\\
&=\frac{5(d+7e)\{(a+b)d+2ae\}}{12(d^2-e^2)}\\
&=\frac{5(81t+7)(8+26t-39t^2-255t^3)}
{384h_e^2(1-9t)(39t+1)}>0 .
\end{aligned}
\tag{18}
$$
最后严格号只用 $0<t<1/100$；分子括号大于
$8-39/10^4-255/10^6>0$。
(17)使用实际 $\tau_\rho(\delta^2;\xi)$ 下的全部积分；
它不是仅三阶主尺度。

## 5. 两种排序的真实四阶差严格反号

本节先取真实母 $v_0$、固定其 $\nu$，
再选择有限间距 $A$。
低／高中心和真实方差仍为 R269/R271：
$$
t^L_{k,l}=64A(k-c)+A(l-31.5),\quad c=(n-1)/2,
$$
$$
t^H_k=B_\rho(k-c)+\rho A\sigma_k,\qquad
B_\rho^2=
\frac{A^2((64n)^2-1)-12\nu(1-q^2)-12\rho^2A^2}{n^2-1}.
\tag{19}
$$
$\sigma_k$ 是原每四个 cell 同号的 TM 序列。
其零、一次、三次带号矩为零，故四阶展开中的两个奇混合项准确为零。

先核全部 copy 费用。令 $V_{\rm cp}$ 是完整复制中心的真实加权方差。
因各 copy 总中心和三次中心均零，
$$
\bar M_{4,H}-\bar M_{4,L}
=M_{4,H}-M_{4,L}+6V_{\rm cp}(V_H-V_L),
$$
$$
\bar V_H-q^2\bar V_L=V_H-q^2V_L+(1-q^2)V_{\rm cp}.
$$
而真实三矩给 $V_H-V_L=-\nu(1-q^2)$，所以
$$
\boxed{
G_\rho=C_4\{M_{4,H}-M_{4,L}
+6\nu(V_H-q^2V_L)\}.
}
\tag{20}
$$
共同 copy 方差在这一组合中准确相消；没有把各个方差直接删掉。
$G_\rho$ 的后项仅为 $O(A^2)$。

置 $N_c=64n$、
$$
V=\frac{N_c^2-1}{12},\qquad
\kappa_n=\frac95-\frac{12}{5(n^2-1)},\qquad
\kappa_{N_c}=\frac95-\frac{12}{5(N_c^2-1)}.
$$
真实有限等差点的二、四阶中心矩给
$$
A^{-4}(M_{4,H}-M_{4,L})\longrightarrow
\Delta_\rho
=(\kappa_n-\kappa_{N_c})V^2
+(6-2\kappa_n)V\rho^2+(\kappa_n-5)\rho^4.
\tag{21}
$$
这个极限只用于选一个有限 $A$；没有替代实际矩。

$\Delta_0<0$。
对 $\rho=20$，通分后
$$
\boxed{
60(n^2-1)\Delta_{20}
=2887680n^4-11059905n^2+7675200>0.
}
\tag{22}
$$
$n\ge2$ 时已有
$2887680n^2-11059905\ge490815>0$，
故(22)严格成立，当然涵盖原 $n=2048$。

因此选择一个足够大的**有限** $A$，还能同时满足全部支撑排序间隙，
并使
$$
\mathscr K_0<0<\mathscr K_{20},
\qquad
\mathscr K_\rho=
\left[\zeta_\kappa G_\rho+
(\mathscr D_X-r_*\mathscr D_Z)w_4\right]_{\tau=0}.
\tag{23}
$$
$\mathscr D_X,\mathscr D_Z$ 是同母的有限常数，不随 $A$ 增长。
选择有限 $A$ 后才取小 $\delta$；(23)因连续性保留到真实(16)根。

## 6. 有序 μ2 尾的完整宽度与 copy 方差

对一个普通两斜率 base，记
$B_i=b_i^2,\ R_i=a_i^2-b_i^2$，
实际第二矩是
$$
m_i=m_\tau\{(\xi+\delta t_i)^2+\nu_\tau\delta^2w_i^2\},
\quad m_\tau=I_0(v_\tau,v_\tau)>0,\quad w_i\in\{q,1\}.
$$
令 $v_i^0=t_i^2+\nu_\tau w_i^2$。
R271 的完整有序量为
$$
U_{01}=\sum B_iR_it_i+
\sum_{i<j}B_iR_j(t_i+t_j).
$$
另定义一个真实有限和
$$
U_{12}=\sum B_iR_it_iv_i^0+
\sum_{i<j}B_iR_j(t_iv_j^0+v_i^0t_j).
\tag{24}
$$
不求值，也不将 $U_{12}$ 设零。

将这些原矩代入(10)，使用完整
$\sum R_i=\sum R_it_i=\sum R_iv_i^0=0$ 和真实反射配对，
偶次中心项准确消失：
$$
Q_2(\pi/2)=4m_\tau^2
\{\xi^3\delta U_{01}+\xi\delta^3U_{12}\}.
\tag{25}
$$
例如 $\xi^3\delta$ 系数使用
$\sum_{i<j}(B_iR_j-B_jR_i)(t_i+t_j)=2U_{01}$。
常数和二次系数由反序严格变号，未用点质量近似。

每个完整副本 inner 三矩零，副本之间(8)跨项准确为零。
实际四次权加总、中心均值与三次矩均零以后，(25)成为
$$
Q_2(\pi/2)=4\mathcal Wm_\tau^2
\{\xi^3\delta U_{01}+\xi\delta^3\bar U_{12}\},
\quad
\bar U_{12}=U_{12}+3V_{\rm cp}U_{01}.
\tag{26}
$$
这一次 copy 方差并不相消，故明确保在 $\bar U_{12}$ 中。

原精确 cell 公式给
$$
U_{01}^{(\rho)}
=nq(1-\alpha)(64q+1)
\left\{\frac{16}{3}(B_\rho-64A)(n^2-1)
+A\left(\frac32\rho^2-512\right)\right\}.
\tag{27}
$$
R271 已用真实(19)严格证明，有限 $A>\sqrt{\nu}$ 时
$$
U_{01}^{(0)}<0<U_{01}^{(20)}.
\tag{28}
$$

合(9)、(17)、(26)，完整 raw even 向量准确为
$$
\boxed{
( E_{22}^{D,2},E_{04}^{D,2})
=K_\rho(\delta,\xi)\,h_\alpha+
O_\rho(\delta,\xi)\,h_1,
}
\tag{29}
$$
$$
K_\rho=2K\delta^3\xi
\left[\zeta_\kappa G_\rho+
(\mathscr D_X-r_*\mathscr D_Z)w_4\right],
$$
$$
O_\rho=-b\mathcal Wm_\tau^2
\{\xi^3\delta U_{01}+\xi\delta^3\bar U_{12}\}.
\tag{30}
$$
全部量都在真实 $\tau_\rho(\delta^2;\xi)$ 上取值。
两种排序各同时满足
$$
K_0/\delta^3<0,\quad O_0/\delta<0,\qquad
K_{20}/\delta^3>0,\quad O_{20}/\delta>0
$$
于足够小的实际正 $\delta$，因为 $-b>0$、$\xi>0$。
这些号没有删除(30)中的 $\delta^3\bar U_{12}$。

## 7. 四个有限正宽的完整二维正锥

先选四个互异的最后正中心，每种排序各两处。
记相应有限非零极限
$$
k_i=\lim_{\delta\downarrow0}K_{\rho_i}(\delta,\xi_i)/\delta^3,\qquad
o_i=\lim_{\delta\downarrow0}O_{\rho_i}(\delta,\xi_i)/\delta.
$$
同一列的 $k_i,o_i$ 同号，$\rho=0$ 为负，$\rho=20$ 为正。

令每种排序的两列分别标记 $r_i=1,2$，
选择固定有限
$$
\lambda_i=\sqrt{r_i|o_i|/|k_i|}>0,\qquad \delta_i=\eta\lambda_i.
\tag{31}
$$
在 $(h_\alpha,h_1)$ 坐标中，施共同可逆行缩放
$\operatorname{diag}(\eta^{-3},\eta^{-1})$ 后，四个真实列趋于
$$
(k_i\lambda_i^3,o_i\lambda_i)
=\operatorname{sgn}(o_i)|o_i|\lambda_i(r_i,1).
\tag{32}
$$
故其极限是沿
$$
-(1,1),\quad -(2,1),\quad +(1,1),\quad +(2,1)
$$
的严格正倍数。它满秩2，且有一个全分量严格正 kernel。

固定一个非零两列 minor，仅修正两个 kernel 坐标，便在充分小的**有限正** $\eta$ 保留真 rank2 和严格正核。
此时每个实际母参数由(16)恢复，所有支撑严格分离；每个 $\delta_i$ 都正且有限。
因此
$$
\boxed{\operatorname{cone}_+\{\text{四个新真实 }\mathcal D_2\text{列}\}
=\mathbb R^2,\qquad\mathcal C_1=0\text{逐列准确成立}.}
\tag{33}
$$
没有将未知母常数当自由坐标，没有以无限频率或零宽 profile 作为实际解。

## 8. 所有旧成本与新的联合矩阵

每个新列保 R346/R273 已付的
$$
\mathcal M_j=\mathcal A_j=0\ (j=0,1,2),\qquad
\mathcal B_0=0,\qquad
\mathcal C_1=0,
$$
真实三矩、强 hook、八副本完整第三和十二副本全部 odd。
同一个完整两斜率张量给
$$
\Psi=\psi_i\sin^2\theta,\qquad \psi_i>0.
$$
没有假定 $\mathcal B_1,\mathcal B_2,\mathcal C_0,\mathcal C_2,\mathcal D_1,\mathcal P_1$ 为零；以下全部保原真实值。

完整 dilation 权为
$$
\mathcal B_1:-5,\quad
\mathcal B_2,\mathcal P_1:-4,\quad
\mathcal D_1,\mathcal C_0:-3,\quad
\mathcal C_1,\mathcal D_2:-2,\quad
\mathcal C_2:-1,\quad
\Psi:-7.
\tag{34}
$$
特别 $I_2$ 的两个积分项同权，并未只估 principal。

先给出不依赖未来额外支付的原 R353 版本。
取其实际 $M_{12}$，删除 $\mathcal C_2$ 两行：
剩下
$$
(\mathcal B_1,\mathcal B_2,\mathcal D_1,\mathcal C_0,\mathcal C_1)
$$
十行，仍满秩并保原严格正 kernel；旧列的 $\mathcal D_2$ 和 $\mathcal C_2$ 真值全部保留。

将(33)四列作共同大有限正伸缩 $H$，第四幅度乘 $H^2$。
它们对前十行的影响趋零，唯一同权 $\mathcal C_1$ 已逐列准确为零。
新的 $\mathcal D_2$ 列保持原值。
极限矩阵是
$$
\begin{pmatrix}M_{10}&0\\D_{\rm old}&D_2^{\rm new}\end{pmatrix}.
\tag{35}
$$
$M_{10}$ 有严格正核，$D_2^{\rm new}$ 的正锥为全 $\mathbb R^2$，
故先取旧正核，再取新严格正权消其下部真实值，就得极限严格正核与 rank12。
有限 $H$ 后由一个固定非零 minor 继续保留，未忽略旧 $D_{\rm old}$。

最后加入 R349 的四个 $\mathcal C_2$ 正锥原型，作新的大有限伸缩 $H'$、第四幅度乘 $H'$。
它们对旧十二行全趋零，新的 $\mathcal C_2$ 两行保持。
同一论证得到完整14行实际正锥，目标为
$$
(\mathcal B_1,\mathcal B_2,\mathcal D_1,
\mathcal C_0,\mathcal C_1,\mathcal D_2,\mathcal C_2).
\tag{36}
$$
各阶段先固定原有限列，后选择新的有限伸缩。
新增正支撑可同时推到此前所有库列右方，库内相对位置不再变。

### 8.1 与 R354 已付 PY1 的实际接口

R354 第6节已经构造了另一个实际库：
$$
(\mathcal B_1,\mathcal B_2,\mathcal D_1,
\mathcal C_0,\mathcal C_1,\mathcal C_2,\mathcal P_1)
$$
满秩13、含严格正 kernel，且所有列有相同真实三阶／旧零条件和正 $\Psi$。
它由 R353 原24列及一个完整反射列组成；原24列的大有限 $A$ 选择满足 R347 的真半平面，先以原正核合成负 $\mathcal P_1$ 整块，再将该完整块反射取得正 $\mathcal P_1$ 列。此处直接消费其已付完整列，不重算或者把微包尾删掉。

同一构造先删 $\mathcal C_2$ 两行，给11行；
用(33)四列给13行，再加 $\mathcal C_2$ 四列给15行。
原 $\mathcal P_1$ 的真实新成本按(34)趋零，绝不被设零。
这是完整 block-triangular 接口，不要求新 D2 原型自行支付 PY1。

该25列库含负坐标支撑，必须使用 R354 已证明的共同物理域建设；不能据此声称保留一个此前冻结的仅正坐标几何。相应33列15行正锥是已完成实际接口，但 R354 更直接的整弱圆反射已同时消去 $\mathcal P_1,\mathcal D_0,\mathcal D_2$，所以本段的用途是提供独立的非偶补偿自由度，而不是提升其16矩计数。

## 9. 同一个最后弱圆的精确支付与 Ψ 费用

从 R353 最后全72零强控制器以前接入，旧弱核心、宽 cutoff、补矩、中心和完整复制均不再移动。
全部旧面积为零，$\Psi=-\Delta_0\sin^2\theta$、$\Delta_0>0$；
记当前完整 $\mathcal D_2$ even 残差为 $r_2\in\mathbb R^2$。

固定(36)的严格正 kernel $k$ 和一个实右逆 $R$。
对整个实际库作共同正伸缩 $S$，第四幅度取 $S^5c_i(S)$，
$$
c(S)=k+R(0,0,0,0,0,-r_2/S^3,0).
\tag{37}
$$
当 $S$ 是足够大的有限数，$c(S)>0$。
(34)及原矩阵恒等准确保持全部旧零，并给 $\Delta\mathcal D_2=-r_2$。
新增 $\Psi$ 全代价是
$$
S^{-2}\sum_i c_i(S)\psi_i\,\sin^2\theta,
$$
可严格小于 $\Delta_0/2$。

采用§8.1已付实际库的分支时，(37)只需在 $\mathcal P_1$ 位置添零；其外尺度为 $S$，仍准确保零。
所有旧列与新列的真实其他坐标都已收入这个同一矩阵。

最后使用原同 $F^\star$ 的全72零强控制器，支付三 directed 行及剩余 $\Psi$。
它自身的全部 Gaussian 面积为零，所以也不改变新 $\mathcal D_2$。
不同完整 blocks 的 inner $D$ 三矩为零，原跨 block 核准确消失；
本稿一直保留的微包内部有序尾则已计入(9)—(30)。

## 10. 有限选择次序与范围

先固定母宽、R346 真小族和 $\alpha=9/20$；
预选四个最后正中心和全部真实复制；
再取有限大 $A$ 满足(23)、(28)和支撑间隙；
定义四个有限 $\lambda_i$，最后取有限正 $\eta$，
分别解真实 $\mathcal C_1=0$，得到四个正宽原型。
以后只作已列的完整正 dilation 和正四次幅，逐次固定每个有限库。

全部额外观察均为原完整值，未重新执行旧科学。
共同合法区间须在全部有限 profiles／几何包络的原允许范围内一次固定；
不得以本构造任意扩大一个先前冻结的窄区间。
若接入含负坐标模块的§8.1库，则还须使用该库已证明的共同几何安装与允许区间，而不能援用仅正支撑的旧放置论证。

本稿准确新增
$$
\boxed{\mathcal D_2(\theta)=0\quad\text{对所有 }\theta,}
$$
保 R353 的全部旧13个外矩、完整三阶、三矩、$\Psi$ 和三 directed 行。
采用§8.1实际接口时也保持其 $\mathcal P_1=0$，并遵守 R354 新几何的范围。

在本文独立全正支撑分支上，$Y$–$W_*$ 的第零矩和尚未另行支付的 $Y$–$P$ 外矩仍欠；在 R354 整体偶弱圆分支上，$\mathcal D_0,\mathcal D_2,\mathcal P_1$ 已由反射支付，准确只剩 $\mathcal P_0,\mathcal P_2$。两条结论不混计。本稿不宣 complete fourth period、全局 ruling 或同一 gauge 的 joint 解。
