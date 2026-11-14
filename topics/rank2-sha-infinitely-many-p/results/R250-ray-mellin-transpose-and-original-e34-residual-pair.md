# R250 — ray 来源的完整 Mellin 转置、实际三源消元及原 E34 剩余行

日期：2026-11-13。**状态：本文的带 $u$ CM5 转置、十二额外型的真实 dyadic 消去、三源 cofactor 消元、原 E34 的两个协变剩余行及其与 R246 的完整解析关系均已证明。尚未证明所得具体原曲线组合的中央导数非零。**

本篇接续 [R248](R248-ray17-conjugate-trace-and-original-yang-projections.md)、
[R246](R246-third-dyadic-bidirectional-cm17-and-complete-central-bridge.md) 和
[R245](R245-third-rank2-full-mellin-and-cm17-log-bridge.md)。
除了有限截面身份，还逐项给出中央尺度、质量导数及协变交换差。

## 1. 实际 CM5 的每一步 trace 与 Gaussian

先在新 degree-$68$ twist-$T_0$ 空间工作。置
$$
\pi=2+i,\quad\bar\pi=2-i,\qquad
\mathscr M=[\pi]_*[\bar\pi]^*,\quad
\mathscr N=\pi^{-1}\mathscr M.
$$
R248 已在完整十七维 $I=1$ 空间中证明 $\mathscr N^{16}=1$。
由于 $(\pi),(\bar\pi)$ 互素，有限平坦 base change 给
$$
\boxed{\mathscr M^j=[\pi^j]_*[\bar\pi^j]^*,\qquad
\mathscr N^j=\pi^{-j}[\pi^j]_*[\bar\pi^j]^*.}             \tag{1}
$$
这个等式使用同一线丛同构：两个 CM 范数相等，且模二相同。复合 pullback 时的指数因子直接相乘，不另选一个 Weil 相位。

具体地，令 $Q\in E_0[\pi^j]$，$\lambda=\pi^jQ\in\Gamma$。对 degree-$68\cdot5^j$ 截面，规范核 lift 是
$$
\mathcal U_Q^{(j)}f(z)=
\chi(\lambda)
\exp\!\left(-\frac{68\cdot5^j\pi\bar Q}{\Omega_0^2}
                         \left(z+\frac Q2\right)\right)f(z+Q),
                                                               \tag{2}
$$
其中 $\chi(m\Omega_0+ni\Omega_0)=(-1)^{m+n}$ 是该 twist 半特征。
(2) 准确固定 $[\pi^j]^*$ 的每个截面。于是
$$
\boxed{
\sum_{Q\in E_0[\pi^j]}
 \mathcal U_Q^{(j)}\bigl(f(\bar\pi^jz)\bigr)
=\pi^j(\mathscr N^jf)(\pi^jz).}                         \tag{3}
$$
这里保留 $Q=0$、全部核点和常数 Gaussian；(3) 不是不带权的椭圆函数平移和。

## 2. 带 $u$ 的完整转置矩阵

对固定惰性 $p>19$，置
$$
d=p+1,\quad U_\pi=\pi^d/5,\quad U_{\bar\pi}=\bar\pi^d/5,
\quad \ell_5=d\log_p(\pi/\bar\pi),
$$
$$
r_p(u)=\pi^{-1}(U_{\bar\pi}/U_\pi)^u,\qquad
J(f;u)=\mathcal J_{68c_0}(f;u).
$$
这些幂都使用标准 $1+p\mathcal O$ 的解析幂。定义实际非零核行
$$
K_j(f;u)=\pi^{-j}U_\pi^{-ju}
\sum_{Q\ne0}\mathcal J_{68\cdot5^jc_0}
 \left(\mathcal U_Q^{(j)}(f(\bar\pi^jz));u\right),
\qquad K_0=0.
$$
由 (3) 及完整 CM 缩放，准确得到
$$
\boxed{K_j(f;u)=J(\mathscr N^jf;u)-r_p(u)^jJ(f;u).}       \tag{4}
$$
若 $\boldsymbol J(u)$ 是 $W,WU,\ldots,WU^{16}$ 基上的中央**行向量**，那么
$$
\boxed{\boldsymbol K_1(u)=
\boldsymbol J(u)\bigl(\mathscr N-r_p(u)I\bigr).}          \tag{5}
$$
这是实际转置系统，不是 $J$ 与 $\mathscr N$ 交换。
设 $j(f)=J'(f;0)$、$m(f)=f(0)$，则其一阶项准确为
$$
\boxed{K_j'(f;0)=j(\mathscr N^jf)-\pi^{-j}j(f)
                     +j\pi^{-j}\ell_5m(f).}             \tag{6}
$$
最后一项来自 $r_p'(0)=-\ell_5/\pi$；对质量非零来源不能删除。

(5) 在完整解析环中可逆：
$$
\boxed{
(\mathscr N-rI)^{-1}
=\frac{\sum_{h=0}^{15}r^h\mathscr N^{15-h}}{1-r^{16}}.}  \tag{7}
$$
准确有
$$
N_{\mathbf Q(i)/\mathbf Q}(\pi^{16}-1)
=2^{11}3^2\cdot5\cdot17^3\cdot337.
$$
因此对所有本篇惰性 $p>19$，(7) 的分母是解析单位，没有新惰性例外。

对共同 $[2]$ 模型，每条 (4) 同时乘 $q_2^u$，$q_2=2^{p-1}$。
其导数还增加 $(p-1)\log_p2$ 乘该行质量。后文的单位商显式包含 $q_2^u$，所以不遗漏这个项。

例如原 $H$ 的投影可以完整地写为
$$
16a_{k,1}J(H;u)=
\sum_{j=0}^{15}i^{-j}K_j(T_k;u)
 +\left(\sum_{j=0}^{15}(r_p(u)/i)^j\right)J(T_k;u).       \tag{8}
$$
这把 R248 的 $\Pi_4$ 放回实际逐步 trace。对原点求导时，有限和的导数是
$-\ell_5\sum_j j(1/(i\pi))^j$，仍乘 $T_k(0)$。

## 3. 十二额外型由真实 dyadic 投影准确消去

令 $\Pi_v$ 是 R246 的新 dyadic 线投影，且
$$
\Pi_{\mu_4}=\frac14(1+\mathscr N^4+\mathscr N^8+\mathscr N^{12}).
$$
在本篇新 half-$(-,-)$、全局 $I=1$ 的十七维空间中，
$$
\boxed{\Pi_v=\Pi_{\mu_4}.}                              \tag{9}
$$
证明保留真实二处型：在 half-$(-,-)$ 的四维二处空间，$I_2=1$ 的唯一线是 R239 的 $v$。全局 $I=1$ 后，它与 $I_{17}=1$ 的五维空间张量，故 $\Pi_v$ 的像准确为
$$
S_8(\beta z),\ S_8(\bar\beta z),\ H,\ S_{2312},\ S_{39304}.
$$
R248 的 $\Pi_{\mu_4}$ 也恰有这五维像。实际 norm-five correspondence 在二处属于同一 compact torus，所以与它的特征线投影 $\Pi_v$ 交换。两个交换幂等有同一像，故相等。

因此 R246 的 $\mathcal V$ 和 $Q_{+,v}=Q_{+,0}\mathcal V$ 作用于三个 $T_k(2z)$ 时，十二个额外型全被准确杀掉。这里是先作用实际投影再取 $J$，没有把一个已取值的中央行改成另一条。

还须保留一个有限秩事实。R248 的两个 CM 系数准确满足
$$
d_{k,+}=(1-4i)d_{k,-}\qquad(k=1,2,3).                    \tag{10}
$$
故三个 $T_k$ 的全部 $\mathscr N$ 轨道秩为十六，而不是十七。
唯一缺少的维度在两维 trivial CM 块中；这与同向核投影为零一致。
脚本直接核验该秩及 (10)。不把十七维完整环境误当成三个来源已经张成的空间。

## 4. 三源 cofactor 消元：没有额外秩零 primitive 导数

令 $A=(a_{k,j})_{1\le k,j\le3}$ 为 R248 的三个 primitive 系数矩阵，按行列分别排列 $T_k$ 与 $H,S_{2312},S_{39304}$。准确有
$$
\Delta=\det A=
\frac{476318521478702583612833+18546337116737865377239i}{2^{79}}
\ne0.                                                     \tag{11}
$$
定义实际三个固定来源
$$
\begin{pmatrix}Z_1\\Z_2\\Z_3\end{pmatrix}
=\operatorname{adj}(A)\begin{pmatrix}T_1\\T_2\\T_3\end{pmatrix},
\qquad \nu=1-4i.
$$
若 $\delta_j$ 是 $\operatorname{adj}(A)(d_{k,-})_k$ 的第 $j$ 项，则
$$
\boxed{\Pi_vZ_j=\Delta R_j+
           \delta_j\bigl(S_8(\beta z)+\nu S_8(\bar\beta z)\bigr),}
                                                               \tag{12}
$$
其中 $R_1=H,R_2=S_{2312},R_3=S_{39304}$。所有 $\delta_j$ 非零；需要的前两项是
$$
\delta_1=
\frac{-1835055276838485424508-5035780583443517235659i}{5\cdot2^{82}},
$$
$$
\delta_2=
\frac{275035722821912997125313-99729497524220909075071i}{2^{80}}.
                                                               \tag{13}
$$
完整 adjugate 和第三项也保存在准确输出中。

下面付一个实际 CM 相位，供原 B 运输使用。置
$$
F_0=(x^2-1)\sigma^4,\qquad F_0(0)=1.
$$
在 R229/R231 的原 degree-$68$ 八项 $Q_{+,0}$ 中，准确有
$$
\boxed{Q_{+,0}\vartheta(2(4\pm i)z)
       =2\kappa_4F_0((4\pm i)z),\qquad\kappa_4=2^{-1/4}.} \tag{14}
$$
两个方向都是正号。这个符号不能从基础 degree-four 的
$Q_{+,0}\vartheta(2z)=-2\kappa_4F_0(z)$ 沿用。

给出完全有限的验证。令 R229 四次坐标为 $T,F,G,H_4$，则
$$
\vartheta(2\beta z)=\sum_{j=0}^4q_jT^{17-4j}H_4^{4j},
\quad(q_0,\ldots,q_4)=(1,12-20i,-10+28i,-20-12i,1+4i).
$$
把 R229 的 $M,N$ 原矩阵代入
$$
Q_{+,0}=\tfrac14\{(M^2-1)(N+N^3)-(M+M^3)(1+N^2)\}.
$$
再用 $T=(U+1)\sigma^4,F=(U-1)\sigma^4,G=2x\sigma^4,H_4=2y\sigma^4$，准确结果为
$$
2\kappa_4\sigma^{68}
      \bigl(UQ_\beta(U)^4-K_\beta(U)^4\bigr)
=2\kappa_4F_0(\beta z).
$$
系数共轭给另一方向；脚本检查全部十七次多项式系数。

## 5. 三个完整 ray 观察行准确留下原 A/B/H

采用 R246 的 $q_2=2^{p-1},q_4=4^{p-1}$，并写
$$
U_-=\beta^d/17,\quad U_+=\bar\beta^d/17,
$$
$$
J_8=\mathcal J_{4c_0}(S_8),\quad
J_0=\mathcal J_{4c_0}(F_0),\quad
J_\vartheta=\mathcal J_{c_0}(\vartheta).
$$
三个参考都是真实常数项一的解析单位。下列单位商保留其原导数，没有把各参考的中央连接分别设为零。

令 $h=\Delta/\delta_1$、$b=320i\Delta/\delta_2$，定义
$$
Y_H(u)=\frac{J(\Pi_vZ_1;u)}{\delta_1J_8(u)},
$$
$$
Y_A(u)=\frac{\mathcal J_{272c_0}(\mathcal V(\Pi_vZ_1)(2z);u)}
                {\delta_1q_4^uJ_\vartheta(u)},
$$
$$
Y_B(u)=\frac{\mathcal J_{272c_0}(Q_{+,v}(\Pi_vZ_2)(2z);u)}
                {2\kappa_4\delta_2q_2^uJ_0(u)}.
$$
使用 R246 的五块运输、(12)、(14)，得到整条解析恒等式
$$
\boxed{\begin{aligned}
Y_H&=U_-^u+\nu U_+^u+h\,\frac{J_{136}}{J_8},\\
Y_A&=-U_-^u+\nu U_+^u+\frac{ih}{22}\frac{J_{17}}{J_\vartheta},\\
Y_B&=-U_-^u+\nu U_+^u-b\,\frac{J_{34}}{J_0}.
\end{aligned}}                                               \tag{15}
$$
所以十二个额外型及其他秩零 primitive 行的未知导数已经全部消去。
现在留下的是三个**明确实际 ray 观察行**及两个明确 CM 单位。
特别
$$
\boxed{Y_A-Y_B=
\frac{ih}{22}\frac{J_{17}}{J_\vartheta}
       +b\frac{J_{34}}{J_0}.}                            \tag{16}
$$
如果以后证明 (16) 左端的中央导数非零，就立即得到原 A/B 中至少一个非零；本文没有把该左端非零作为免费输入。

## 6. 原 E34 的两个准确协变伴随

继续用 R245 的 $F=S_8^{17}$、$\nabla_8=\partial-F'/F$、
$$
r=\frac{x-1}{x+1},\quad
K_I=\frac{S_8(\bar\beta z)-S_8(\beta z)}{2i},\quad
K_R=\frac{S_8(\bar\beta z)+S_8(\beta z)}2.
$$
R248 已精确认定 $R_2=S_{2312}=WP_2(U)$。在 R245 的同一协变矩阵下，它的两个余类是
$$
\beta_{2,\mathrm{eff}}=-\frac{23027643318272}{1043119},
\qquad\gamma_2^{\rm raw}=\frac{7766131072}{195}.
$$
因此有两个非零有理数
$$
a_I=\frac{8235327}{3310819},\qquad
a_R=-\frac{218637}{274334},                              \tag{17}
$$
及明确的固定对数伴随 $C_I,C_R$，满足
$$
\boxed{\nabla_8^2C_I=R_2-a_IK_I,\qquad
       \nabla_8^2C_R=R_2-a_RK_R.}                        \tag{18}
$$
它们的完整形式是
$$
C_\epsilon=F\left[
 \frac{xR_\epsilon(U)}{U^8(U-1)^7}
       -\frac{\gamma_\epsilon}{8}\log r\right],
\qquad\deg R_\epsilon\le14.                             \tag{19}
$$
脚本输出列出两个 $R_\epsilon$ 的全部十五个有理系数及 $\gamma_\epsilon$。
例如
$$
\gamma_I=-\frac{471121690512128}{645609705},\quad
C_I=\frac12z^2+\frac{726164027}{66216380}z^6+O(z^{10}),
$$
$$
C_R=\frac{1-a_R}{2}z^2+
              \frac{459+133a_R}{60}z^6+O(z^{10}).        \tag{20}
$$
所以不能把 $C_I$ 当作 R245 的 $z^6$ 起始伴随 $C_*$。

证明直接使用 R245 的可逆十七维矩阵：减去 $a_IK_I$ 或 $a_RK_R$ 后，$\beta_{\rm eff}$ 准确为零。再用
$$
\nabla_8^2(F\log r)=-4F-8F/(U-1)
$$
消去第二余类，便得 (18)。整个多项式恒等式在输出中逐系数验证。

## 7. 真正 E34 转置与完整参考单位

令 $F_2=F(2z)$、$C_{\epsilon,2}=C_\epsilon(2z)$、
$\nabla_2=\partial-F_2'/F_2$。R246 与 (14) 给
$$
Q_{+,v}K_I(2z)=-2i\kappa_4F_R(2z),\qquad
Q_{+,v}K_R(2z)=2i\kappa_4F_I(2z),                        \tag{21}
$$
其中 $F_R=(F_0(\bar\beta z)+F_0(\beta z))/2$，
$F_I=(F_0(\bar\beta z)-F_0(\beta z))/(2i)$。
同时 $Q_{+,v}R_2(2z)=-640i\kappa_4B(2z)$。

定义实际转置行
$$
\Psi_B(u)=\frac{\mathcal J_{272c_0}
       (Q_{+,v}\nabla_2^2C_{I,2};u)}{8i\kappa_4a_I},
$$
$$
\Theta_B(u)=-\frac{\mathcal J_{272c_0}
       (Q_{+,v}\nabla_2^2C_{R,2};u)}{8i\kappa_4a_R}.
$$
置 $C_p=(U_+^u+U_-^u)/2$、$D_p=(U_+^u-U_-^u)/(2i)$。准确有
$$
\Psi_B=q_2^u\left(C_pJ_0-\frac{320}{a_I}J_{34}\right),
\qquad
\Theta_B=q_2^u\left(D_pJ_0+\frac{320}{a_R}J_{34}\right).
                                                               \tag{22}
$$
对两者除以同一个真实单位 $q_2^uJ_0$，得到
$$
\boxed{\widehat\Psi_B=C_p-\frac{320}{a_I}\frac{J_{34}}{J_0},
\qquad
\widehat\Theta_B=D_p+\frac{320}{a_R}\frac{J_{34}}{J_0}.}   \tag{23}
$$
两行的中心质量分别为一和零。原 B 失效时，它们的中央导数分别是
$$
\boxed{\widehat\Psi_B'(0)=\frac{p-1}{2}\log_p17,
\qquad
\widehat\Theta_B'(0)=\frac d{2i}\log_p\frac{4+i}{4-i}.}   \tag{24}
$$
两种真实剩余行由此都与原 E34 精确连接。

## 8. 交换差、移权和对数支均未删除

写 R246 的实际有限算子 $Q_{+,v}=\sum_sb_s\mathcal T_s$，令
$$
A_s=\partial_z\log\frac{\mathcal T_sF_2}{F_2}.
$$
对每一个 $\epsilon=I,R$，准确有
$$
Q_{+,v}\nabla_2^2C_{\epsilon,2}
=\nabla_2^2Q_{+,v}C_{\epsilon,2}+\mathscr E_\epsilon,
$$
$$
\mathscr E_\epsilon=
\sum_sb_s\{-2A_s\nabla_2(\mathcal T_sC_{\epsilon,2})
                  +(A_s^2-A_s')\mathcal T_sC_{\epsilon,2}\}.     \tag{25}
$$
完整有限 theta lifts 使 $Q_{+,v}$ 保持全局 $i$ 特征，所以
$g_\epsilon=z^{-2}Q_{+,v}C_{\epsilon,2}$ 在原点正则。
沿用 R246 的 $W=zF_2'/F_2$、$W_0=W-dcz^d$、$c=272c_0$、$E=z\partial_z$，令
$$
f=\mathcal J_c(g_\epsilon),\quad
g_1=\mathcal J_c(W_0g_\epsilon),\quad
h_1=\mathcal J_c((W_0^2+EW_0-W_0)g_\epsilon).
$$
那么 (25) 的完整 Mellin 左端是
$$
\begin{aligned}
\mathfrak L_\epsilon(u)={}&(du+1)(du+2)f(u)
 +du(d-3-2du)f(u-1)+d^2u(u-1)f(u-2)\\
&-2(du+1)g_1(u)+2dug_1(u-1)+h_1(u)
                 +\mathcal J_c(\mathscr E_\epsilon;u).
\end{aligned}                                               \tag{26}
$$
由 (22)、(23)，它准确等于
$$
\mathfrak L_I=8i\kappa_4a_I q_2^uJ_0\widehat\Psi_B,
\qquad
\mathfrak L_R=-8i\kappa_4a_R q_2^uJ_0\widehat\Theta_B.    \tag{27}
$$
特别中央求导保留 $3df(0)$、$d(d-3)f(-1)$、$-d^2f(-2)$、
$2dg_1(-1)$ 和 $\mathcal J_c(\mathscr E_\epsilon)'(0)$，没有从 (18) 跳过它们。

这里的对数都取 $\log_pr(2(z-s))$ 的完整支，包括 $\log_pr(-2s)$。
R246 的 $\mathcal V$ 位移在十六格中两个坐标均为奇数；
附加的 $Q_{+,0}$ 四挠运输在共同 $[2]$ 模型中增加偶坐标，
故 $2s$ 仍为真正八挠点，没有落到 $r$ 的二挠零极点。
其局部非恒定对数在原 $R=p^{-1/(2p)}$ 半径上的范数至多 $p^{1/2}$；
这与 R246 §7 的证明相同。固定阶微分与固定连接差只付固定幂 $R^{-C}$，
全部 Newton 尾项仍收敛。因此 (26)–(27) 是完整解析式。

## 9. 与 R246 两个实际剩余行的精确闭环

记
$$
a=-\frac{14548243}{4370281080},\qquad
\widetilde\Phi=\frac{\Phi_*}{J_8},\qquad
\widehat\Psi_A=C_p+\frac1{22a}\frac{J_{17}}{J_\vartheta}.
$$
R245 给 $\widetilde\Phi=J_{136}/J_8-aD_p$。
于是 (23) 给出两条整解析关系
$$
\boxed{
\widehat\Psi_B-\widehat\Psi_A
=-\frac{320}{a_I}\frac{J_{34}}{J_0}
 -\frac1{22a}\frac{J_{17}}{J_\vartheta},}                 \tag{28}
$$
$$
\boxed{
\widehat\Theta_B+\frac{\widetilde\Phi}{a}
=\frac1a\frac{J_{136}}{J_8}
 +\frac{320}{a_R}\frac{J_{34}}{J_0}.}                    \tag{29}
$$
这就是原 B 失效所给的真正剩余行关系，全部来自 (18)、(21)、(25)，而非由有限算子可逆性猜测。

同时，两条 B 剩余行自身满足准确的非齐次式
$$
\boxed{a_I\widehat\Psi_B+a_R\widehat\Theta_B
                    =a_IC_p+a_RD_p.}                   \tag{30}
$$
它的 CM 右端不能因为两个协变余类已相消而删除。
在三个原中央导数同时为零时，(28)、(29) 迫
$$
\widehat\Psi_B'=\widehat\Psi_A'=C_p'(0),\qquad
\widehat\Theta_B'=-\Phi_*'(0)/a=D_p'(0).
$$
(30) 的中央导数是非零代数系数的 norm-$17$ 与 norm-one-$17$ 对数组合；
由 R246 已核的 Brumer 定理，它非零。
因此本闭环是带准确 CM 右端的关系，没有制造两个独立对数之间的虚假齐次等式。

前面的实际 ray 观察行也已直接接到这两个 R246 剩余行。由 (15)，
$$
\boxed{\begin{aligned}
Y_B={}&(\nu-1)\widehat\Psi_A
 -\frac{i(\nu+1)}a\widetilde\Phi
 +\frac{i(\nu+1)}a\frac{J_{136}}{J_8}\\
&-\frac{\nu-1}{22a}\frac{J_{17}}{J_\vartheta}
 -b\frac{J_{34}}{J_0}.
\end{aligned}}                                               \tag{31}
$$
所以若三个原导数都为零，则这一个明确的有限 ray 观察行必须满足
$$
\boxed{Y_B'(0)=-4i\widehat\Psi_A'(0)
                    -\frac{4+2i}{a}\Phi_*'(0)\ne0.}     \tag{32}
$$
这给下一次实际对数来源比较一个准确目标。尚需证明的是该具体观察行
与新算术来源之间的额外关系，或直接证明 (16) 的中央非零；
不是再给 $J$ 添加一个未经证明的交换性质。

## 精确证书

[脚本](../scripts/check-e2312-transposed-companions-and-mellin-system.py) 及
[输出](../scripts/check-e2312-transposed-companions-and-mellin-system.json)
保存两个完整 $R_{14}$ 与对数系数、(14) 的全部原矩阵核验、
带 $u$ 转置矩阵的逆与质量一阶项、实际十六维轨道秩、
三个 cofactor 行及全部 CM 系数。
计算使用固定有理数、高斯有理数及已证明的 R245/R248 矩阵，
没有扫描目标素数或数值拟合。
