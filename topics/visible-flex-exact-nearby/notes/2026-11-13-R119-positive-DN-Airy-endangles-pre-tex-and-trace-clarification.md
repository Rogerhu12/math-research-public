# R119 续篇：在真实 Airy 两端角中的正型 DN、完整源与尺度导数

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 把相邻负型段已经构造的实际 Airy 端角直接作为
正型段的两个边界坐标。在这些同一端角中，实际完整两端 DN 与原
径向两端 DN 的能量相对误差，在全部内部正型分量上的和小于
$$
 \boxed{\quad 2^{-480}\,\overline X.\quad}                 \tag{D.1}
$$
这里是包括全部 Fourier 模、两个非对角反馈及 mean 的弱算子界。
比较没有把端角 pullback 当作同宽小算子，而是在正型光学坐标中
构造真实内部插值，并比较整个二次型。完整 ordinary source、
给定的散度源、两端真实通量以及度量尺度变化一并保留。

本篇不从这个 form 界推出尚未证明的整个 mixed-network Green。
特别，径向负型参考的双端条件数及正型能量迹与所需强 Airy 范数
之间的统一比较仍是另外的算子问题。

## 1. 同一实际对象及正型光学长度

使用 [真实射线振幅](R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md)
及 [完整 Airy 端口](R119-supplement-actual-Airy-balance-of-ray-coupling-and-sources.md)
的同一个 $\Gamma^*(a)$、$\Gamma^0$、$\ell^1_{224}$ 标签和宽角图。
记 $\overline X=(13/4)\|a\|_{224}<1$。每层仍是
$$
 \delta_j=\frac2{25}2^{-j},\qquad
 \eta_j=\frac{\delta_j^{3/2}}{4\sqrt2},\qquad
 dt=\frac{\eta_j}{\sqrt{12}}dx,\qquad j\ge129.
$$
本篇只处理两个端点都已有上述真实负型 Airy 端角的内部正分量。
最外固定 cut 的有限接合不被另行赋予一个不存在的双转向端角。

两个上升坡的 log 跳幅分别为
$$
 \Delta^+_{j,1}=\log64+|\log\delta_j|,\qquad
 \Delta^+_{j,2}=\log(65/64)+2|\log\delta_j|.
$$
它们满足 $j/2<\Delta^+<3(j+4)$。真实正型区间
$I=[t_-,t_+]$ 是
$$
 A=-7+\Lambda S'(x)>0,\qquad
 \Lambda=\frac{\sqrt{12}\Delta^+}{\eta_j},\qquad
 S(x)=10x^3-15x^4+6x^5
 \tag{D.2}
$$
的那个完整开分量加两端。所有度量参数 bump 都在下降坡内部，
所以这里的 $A,w$ 及端点邻域对 $\Gamma$ **准确不变**。
物理半径是 $a_{\rm phys}=\rho(\Gamma)e^t$，其中 $e^t$ 表示
本胞元实际的 $r\in[1,2]$；固定的时间平移不影响以下公式。

令
$$
 L_+=\int_I\sqrt A\,dt,\qquad
 s_+(t)=L_+^{-1}\int_{t_-}^t\sqrt A\,dt.
$$
在 $x\in[1/4,3/4]$ 上 $S'\ge135/128>1$、$\Lambda>14$，
所以 $A>\Lambda/2$。直接积分这个实际子段给
$$
 \boxed{\quad
  \frac1{32}\delta_j^{3/4}\sqrt j<L_+<1,
  \qquad |I|<\delta_j^{3/2}.
 \quad}                                                     \tag{D.3}
$$
确实先有 $L_+>\sqrt{\eta_j\Delta^+}/8$，再用
$\eta_j>\delta_j^{3/2}/8$、$\Delta^+>j/2$。
上界由 $S'\le15/8$ 及 (D.2) 直接得到，最浅层已远小于1。
这是真正的正型光学长度，不是把短径向长度 $\eta_j$ 误作
角图插值的分母。

## 2. 两个实际端角及逐层完整界

每个邻接负分量 $i=(j_i,k)$ 已给出
$$
 K_e=\chi_e^{-1}\circ\Upsilon_i^e,
 \qquad
 K_i=2^{18}\frac{\widehat\varepsilon_i}{\gamma_i^{\rm D}}
                 \overline X,
 \quad
 \widehat\varepsilon_i
   =2^{80}(j_i+4)\delta_{j_i}^{443/256}e^{-640}.
 \tag{D.4}
$$
$K_e$ 是原物理角到同一个端口参数的逆向参数化：端高度为
$h\circ K_e$，端通量为 $K_e'(p_h\circ K_e)$。
这里只用已经付过的那一组真实 KAM 图，不为正区重新选择角相位。

射线篇 (A.17)--(A.20) 及其 §9 的完整物理复合给，在保留的
宽 $64+1/16$ 上，
$$
 \|K_e-\mathrm{id}\|+\|K_e'-1\|<16K_i.
 \tag{D.5}
$$
其中 $\Upsilon_i^e-\mathrm{id}$ 至多 $2K_i$，其导数差至多
$3K_i$；$\chi_e^{-1}$ 的位移及一阶差由 $64n_i<K_i$ 支付。
复合像使用前篇宽 $64+1/8$ 以上的固定余量。因此 (D.5) 是
已经存在的端图的系数估计，未作用于任意边界函数来宣称小算子差。

由 $\kappa_i^{-1}<2^{28}\sqrt{j_i}\delta_{j_i}^{-3/4}$ 和
$\gamma_i^{\rm D}=\kappa_i/64$，
$$
 K_i<2^{132}(j_i+4)\sqrt{j_i}\,
       \delta_{j_i}^{251/256}e^{-640}\overline X.
 \tag{D.6}
$$
邻端层号至多相差1，$\delta_{j-1}=2\delta_j$。故两端的
$K_i$ 都不超过
$2^{133}(j+5)^2\delta_j^{251/256}e^{-640}\overline X$。

先在整个正区取真正的 drift flow
$$
 \phi_t(t,\zeta)=-d(t,\phi(t,\zeta)),\qquad
 \phi(t_-,\zeta)=\zeta,
 \quad d=E(V-P)/J.
 \tag{D.7}
$$
在这个单胞元实际域上可取
$N_j=2^{68}\delta_j^{443/256}e^{-640}\overline X$。
完整角余量给 $\|d\|+\|d_\theta\|<32N_j$；积分
$|I|<\delta_j$，微分真实流和逆流后，二者的 $C^1$ 差小于
$128N_j\delta_j$。这些估计也成立于上述宽角域再缩小固定
$1/32$ 的复域中。以下 form 比较只需实圆上的值。

定义两个端角在 drift 坐标中的准确表示
$$
 H_e=\phi_e^{-1}\circ K_e,qquad e=-,+,
$$
并采用统一包络
$$
 \mathfrak a_j
 =2^{142}(j+5)^2\delta_j^{251/256}e^{-640}\overline X.
 \tag{D.8}
$$
前述完整复合、逆图和一阶乘积的费用给
$$
 \|H_e-\mathrm{id}\|_{C^1}<\mathfrak a_j<2^{-400}.
 \tag{D.9}
$$
例如全部图费用可用 $64(\max K_i+N_j\delta_j)$ 控制；
(D.6) 与 (D.8) 仍留超过二倍余量。

## 3. 光学插值及实际弱系数

准确取
$$
 \psi(t,\xi)=(1-s_+(t))H_-(\xi)+s_+(t)H_+(\xi),
 \qquad \Phi(t,\xi)=\phi(t,\psi(t,\xi)).
 \tag{D.10}
$$
这里选用各个图已经固定的小 lift，故凸组合是 degree-one
圆周图，且 $\psi_\xi>0$。全径向变量 $t$ 始终不变。
两端准确是 $\Phi_e=K_e$。写 $j_\psi=\psi_\xi$，则
$$
 |j_\psi-1|<\mathfrak a_j,qquad
 \frac{|\psi_t|}{\sqrt A}
 \le\frac{2\mathfrak a_j}{L_+}.
 \tag{D.11}
$$
第二式在端点按连续极限解释：$\psi_t$ 本身趋0，比例是
固定的 $(H_+-H_-)/L_+$。因此没有除去一个未消失的 drift。
若直接插值物理端角而跳过 (D.7)，真实 $d/\sqrt A$ 就会留下
不合法的端点奇异；(D.7) 是本证明必要的一步。

原 raw Jacobi 弱系数和 source 是
$$
 M_h=\mu\begin{pmatrix}1&-d\\-d&d^2+Av^2\end{pmatrix},
 \quad \mu=(w/a_{\rm phys})JD^{-3/2},
 \quad v=\sqrt D/J,qquad s_h=w^2JD^{-3/2}e.
$$
先经 (D.7) 后，完整两项系数准确为
$$
 \widetilde\mu=\mu_0(1+r_\mu),\qquad
 \widetilde\beta=A\mu_0(1+r_\beta),\qquad
 \mu_0=w/a_{\rm phys}.
$$
[原正型弱 DN 篇](R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md)
(P.8)--(P.11) 的同一代数，加上本篇逐层 drift 界，给
$$
 |r_\mu|+|r_\beta|<512N_j<\mathfrak a_j.
 \tag{D.12}
$$
在再作 $\zeta=\psi(t,\xi)$ 后，真实能量恰为
$$
 \mathscr E_a(u,u)=\int_I\!\left\langle
 \mu_0\left[(1+r_\mu)j_\psi|u_t|^2
 -2\operatorname{Re}\bigl((1+r_\mu)\psi_tu_t\overline{u_\xi}\bigr)
 +\frac{(1+r_\mu)\psi_t^2+A(1+r_\beta)}{j_\psi}
                         |u_\xi|^2\right]\right\rangle dt .
 \tag{D.13}
$$
所有 $r$ 在 $\psi$ 处取值。实际角 Jacobian 与交叉项均保留。

以 $(u_t,\sqrt A\,u_\xi)$ 作仅用于比较的加权变量，矩阵为
$$
 \mathcal M=
 \begin{pmatrix}
  (1+r_\mu)j_\psi&-(1+r_\mu)\nu\\
  -(1+r_\mu)\nu&[(1+r_\mu)\nu^2+1+r_\beta]/j_\psi
 \end{pmatrix},qquad \nu=\psi_t/\sqrt A.
 \tag{D.14}
$$
若各小量绝对值之和为 $b<1/16$，逐行绝对值和给
$\|\mathcal M-I\|<16b$；此证明同样适用于复系数双线性 form。
由 (D.3)、(D.8)--(D.12)，可统一取
$$
 \varepsilon_j
 =2^{154}(j+5)^2\delta_j^{59/256}e^{-640}\overline X,qquad
 \|\mathcal M-I\|<\varepsilon_j.
 \tag{D.15}
$$
指数 $59/256=443/256-3/2$ 依次支付了负段 KAM 的
$\kappa^{-1}$ 和当前正型光学长度的 $L_+^{-1}$。
这里没有用 $\eta_j^{-1}$ 代替后者。

## 4. 完整两端 DN、全部模式及无限层相对和

令 $\mathscr E_0=\int_I\langle\mu_0(|u_t|^2+A|u_\xi|^2)\rangle$。
本篇端坐标中的径向两端参考仍是原准确矩阵
$$
 \mathsf S_m=\frac1{\beta_m}
       \begin{pmatrix}\alpha_m&-1\\-1&\delta_m\end{pmatrix},
 \quad
 \begin{pmatrix}\alpha_m&\beta_m\\\gamma_m&\delta_m\end{pmatrix}
  =\Phi_m(t_+,t_-),qquad m\in4\mathbb Z,
 \tag{D.16}
$$
其中 $\Phi_m$ 是 $(h,p)_t=(p/\mu_0,m^2A\mu_0h)$ 的真实
径向流。$\beta_m>0$，并且
$$
 \mathsf S_0=R_I^{-1}\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \quad R_I=\int_I\mu_0^{-1}dt.
$$
所有 $\mathsf S_m$ 及两个 $-1/\beta_m$ 均保留。
记该完整两端能量空间为 $\mathcal T_I$，在共同常数方向之外
的 quotient 为 $\mathcal T_I^0$；独立常高度的规范取
$\lambda(f)=((f_-)_0+(f_+)_0)/2$。

(D.13)--(D.15) 给整个体空间的 form 比较
$$
 (1-\varepsilon_j)\mathscr E_0\le\mathscr E_a
             \le(1+\varepsilon_j)\mathscr E_0 .
$$
在各个固定两端高度的仿射空间上最小化，即得真实
$\mathcal N_a^{K}$ 与 $\mathcal N_0=\bigoplus_m\mathsf S_m$：
$$
 \boxed{\quad
 \|\mathcal N_a^{K}-\mathcal N_0\|_{
       \mathcal T_I^0\to(\mathcal T_I^0)^*}<\varepsilon_j.
 \quad}                                                     \tag{D.17}
$$
它输出同一实际端角中的 $(-P_-,P_+)$。
这个比较适用于任意该能量空间输入，而非仅由低标签生成的方向。
两者都准确消去共同常数；mean 高度差、mean flux 从未删除。

全部无限层的预算完全可求和。准确整数不等式
$(7/6)^{256}<2^{59}$ 给 $2^{-59/256}<6/7$，而
$$
 \sum_{j=129}^{\infty}(j+5)^2(6/7)^j<1/2.
$$
每层至多两个正分量、$e>2$、$\delta_j<2^{-j}$，故
$$
 \sum_{\text{全部内部正分量}}\varepsilon_j
 <2^{154}2^{-640}\overline X<2^{-480}\overline X.
 \tag{D.18}
$$
未用一个有限频率或有限层截断替代这个和。

## 5. 与完整 Airy 两迹的准确接口

相邻负段在其真实端图中给 $(z_{0,e},p_{0,e})$ 和 $D_e$。
本篇的 $K_e$ 就是该端图，所以端口不再有一个未支付的
额外 reparametrization。准确高度与 flux 是
$$
 f_e=(f_e)_0+\partial_\xi^{-1}(\sqrt{D_e}\,z_{0,e}),qquad
 P_e=D_e^{-1/2}p_{0,e},qquad
 \langle\sqrt{D_e}\,z_{0,e}\rangle=0.
 \tag{D.19}
$$
独立的 $(f_e)_0$ 不由 $z_{0,e}$ 决定。
若有普通源，完整正区方程是
$$
 \begin{pmatrix}-D_-^{-1/2}p_{0,-}\\D_+^{-1/2}p_{0,+}\end{pmatrix}
 =\mathcal N_a^K\begin{pmatrix}f_-\\f_+\end{pmatrix}
                                      +q_{\mathcal F}.
 \tag{D.20}
$$
由此确切给出一个负段--正段--负段的共同两迹合同。
尤其 $z_0$ 的未加权零模不能删除，$p_0$ 的未加权平均也不是
完整 holonomy。物理 grounded normal/shear 继续由这些全部
raw 两迹按原准确变换恢复。

## 6. 原物理普通源及实际逐层权

完整图是 $\Xi(t,\xi)=(t,\Phi(t,\xi))$，记
$J_\Xi=\Phi_\xi>0$。原物理 scalar Darboux source $e$ 的
真实密度在本坐标中为
$$
 \widehat s=J_\Xi\,(w^2JD^{-3/2}e)\circ\Xi.
 \tag{D.21}
$$
这是对原物理角的直接公式，没有先对任意 $L^2$ 输入宣称
解析同宽复合的小差。在实 $L^2$ 空间中普通换元和
$1/2<J_\Xi<2$ 给
$\|\widehat s(t)\|_2<16w_{\max}^2\|e(t)\|_2$。

令 $M_I=\int_I A\mu_0dt$。同一实际 profile 还满足
$$
 R_I<2^9\frac\rho\epsilon\delta_j^{-11/2},qquad
 M_I>2^{-10}\frac\epsilon\rho\delta_j^5.
 \tag{D.22}
$$
第一式使用 $w\ge\epsilon\delta_j^7/256$、
$a_{\rm phys}\le2\rho$ 和 (D.3)。第二式可直接核真实端值：
型别根 $x_-$ 满足
$x_-(1-x_-)=\sqrt{7/(30\Lambda)}$，故
$\Delta^+S(x_-)\le80\Delta^+(7/(30\Lambda))^{3/2}<1/4$。
对称性给另一端相同的余 log。因而
$p_{*,+}>p_{\rm out}/2$、$p_{*,-}<2p_{\rm in}$。
这里 $p_{\rm out}\ge\delta_j^{-1}$、$p_{\rm in}\le1$。
于是 $\mu_{0,+}>\epsilon\delta_j^5/(512\rho)$，
$\mu_{0,-}<2\epsilon\delta_j^6/\rho<\mu_{0,+}/2$。
最后准确使用
$$
 M_I=\mu_{0,+}-\mu_{0,-}+\int_I\mu_0dt
$$
而得 (D.22)，没有借用一个方便的常系数正段。

原正型篇的全部四重 Poincare、径向 Cauchy--Schwarz 仍给
$$
 C_I=1+2\sqrt{R_I}+\frac1{4\sqrt{M_I}}
 <1+2^7\sqrt{\rho/\epsilon}\,\delta_j^{-11/4}.
$$
所以真实 source 泛函
$\mathcal F(u)=\int_I\langle\widehat s\,\overline u\rangle dt$
在包括独立高度常数的完整能量空间上有 norm
$$
 \begin{split}
 \mathcal S_I&=C_I\int_I\|\widehat s(t)\|_2dt\\
 &<\left(2^{16}\epsilon^2\delta_j^{43/4}
       +2^{23}\epsilon^{3/2}\rho^{1/2}\delta_j^8\right)
                             \|e\|_{L^2(I\times\mathbb S^1)}.
 \end{split}                                                 \tag{D.23}
$$
这里 $w_{\max}\le64\epsilon\delta_j^5$；没有假设
$\epsilon$ 与 $\rho$ 的一个未给出的大小关系来删去第一项。
两个真实源权都是可和的正次幂。

零 Dirichlet 解的能量 norm 至多
$\mathcal S_I/(1-\varepsilon_j)$；完整双端源通量满足
$\|q_{\mathcal F}\|_{\mathcal T_I^*}<2\mathcal S_I$，而准确 mean 是
$$
 \langle q_{\mathcal F},(1,1)\rangle
 =\int_I\langle\widehat s\rangle dt
 =\dot M(t_+)-\dot M(t_-).
 \tag{D.24}
$$
共同平移虽然在齐次 DN 中是核，在这个有源通量行中并未被 quotient
删除。真实物理高度平均按反变换恢复，不能用本端坐标的角平均
替代它而漏掉 moving-mean 项。

## 7. 给定散度源、端点项及所有参数导数

若原物理方程已经准确给为
$\operatorname{div}(M_h\nabla h)=f+\operatorname{div}Z$，
本图下的完整 Piola 变换是
$$
 \widehat f=J_\Xi f\circ\Xi,qquad
 \widehat Z=J_\Xi(D\Xi)^{-1}(Z\circ\Xi)
  =\begin{pmatrix}J_\Xi(Z^t\circ\Xi)\\
           Z^\theta\circ\Xi-\Phi_t(Z^t\circ\Xi)\end{pmatrix},
 \tag{D.25}
$$
最后一式中的 $J_\Xi,\Phi_t$ 在新坐标评价，只有 $Z$ 复合
$\Xi$。相应
$$
 \mathcal F(u)=\int_I\langle\widehat f\,\overline u
                       -\widehat Z\cdot\nabla\overline u\rangle dt.
$$
一个完整充分 norm 是 (D.23) 的密度版加上
$$
 \left[\int_I\left\langle
  \frac{|\widehat Z^t|^2}{\mu_0}
  +\frac{|\widehat Z^\xi|^2}{A\mu_0}\right\rangle dt\right]^{1/2}.
 \tag{D.26}
$$
必须实际有限，不能把 $A=0$ 的源权隐去。此时 (D.20) 输出的是
总通量 $p-\widehat Z^t$；若要输出 bare Jacobi flux $p$，需再加
两端 $(-\widehat Z^t_-,\widehat Z^t_+)$。这明确保留了 metric-source
可能带来的两个端点项，并未声称任何未转换的 R37 强源自动满足
(D.26)。

所有端图、drift、$\Gamma^*(a)$ 都在原标签球中全纯。
$s_+(t)$ 与该球无关，因为正型 profile 没有被 retune；其
$C^1$ 正则性已足够定义本篇的弱变换，无需将它宣称为跨转向
径向接缝的全解析二维图。按 (D.13) 对固定的实体空间定义复
系数 form，再用小扰动逆，得到全纯弱 DN 家族。
复参数时直接用该完整矩阵定义 sesquilinear form，而不把实系数
公式中的 $\operatorname{Re}$ 当作参数运算。减去两个弱方程给
复域 DN 差至多 $\varepsilon_j/(1-\varepsilon_j)<2\varepsilon_j$。
由 (D.18) 实际得到的更强和 $2^{-486}\overline X$，这额外因子2
仍在本篇采用的 $2^{-480}$ 复域总包络内。

物理尺度 $\rho=\rho(\Gamma^*(a))$ 必须另行保持。若
$\rho_0=\rho(\Gamma^0)$，令
$$
 \overline{\mathcal N}_a=(\rho(a)/\rho_0)\mathcal N_a^K.
 \tag{D.27}
$$
这样参考能量空间是固定的 $\rho_0$ 空间，径向参考恰为
$\mathcal N_0^{\rho_0}$。在 $\|a\|_{224}\le1/8$ 上，复方向半径
$1/16$ 的一阶 Cauchy 界和两个各 $1/32$ 的二阶方向 Cauchy 界，
连同 (D.18)，给完整无限层的
$$
 \sum_I\|D_a(\overline{\mathcal N}_a-\mathcal N_0^{\rho_0})\|
          <2^{-476},\qquad
 \sum_I\|D_a^2(\overline{\mathcal N}_a-\mathcal N_0^{\rho_0})\|
          <2^{-470}.
 \tag{D.28}
$$
这些是全部标签及其联立度量参数的导数，不是逐层固定其余参数。
恢复未归一物理 DN 时准确有
$$
 D\mathcal N_a^K
 =\frac{\rho_0}{\rho}D\overline{\mathcal N}_a
                    -(D\log\rho)\mathcal N_a^K.
 \tag{D.29}
$$
二阶导由此完整再微分，包含两项混合尺度导数、
$(D\log\rho)^2$ 和 $D^2\log\rho$；均不能省略。

端口也须微分整个函数/密度变换。令
$v_e=(\delta K_e)/K_e'$，准确有
$$
 \delta f_e=(\delta h)\circ K_e+v_e\partial_\xi f_e,qquad
 \delta P_e=K_e'(\delta p_h)\circ K_e+\partial_\xi(v_eP_e).
 \tag{D.30}
$$
所以物理 holonomy 平均仍保持；二阶变化包括完整的
$\delta v_e$ 和再次作用的角导数。对于一般只有 $L^2$ 的给定源，
本篇只给实背景的 (D.23)，不从端图的全纯性免费推出该源的
参数角导数。若使用解析源，必须继续采用已授予的实际角余宽。
在固定物理 $a_{\rm phys}$ 微分最终目标时，原重调篇的
$\delta w=w(\sum\psi_i\delta\gamma_i+A\delta\ell)$ 以及 mean 高度
移动切口项保持原式；它们不能被 (D.27) 的纯尺度归一抹去。

## 8. 已闭接口与剩余算子

(D.17)--(D.20) 将正型完整两端 DN 置于相邻负段已经付过的
**同一实际 Airy 端角**；(D.23)--(D.26) 给连续普通源和准确
散度源合同；(D.27)--(D.30) 保持真实尺度、所有标签和端图导数。
这一步用的是完整二次型，故没有高频固定相位小差的漏洞。

尚待完成的是同一径向负型参考的全两迹 Green/散射估计及其与
本 $\mathsf S_m$ 空间的强比较，然后才能对整个无限 mixed 网络、
最外有限 connector 和 regular 匹配作相对逆。不能仅把两个已小的
局部误差相加，就跳过这个参考网络条件数。

[准确预算程序](../scripts/fourfold_positive_DN_Airy_endangles_20261113.py)
与 [完整 native 报告](../notes/2026-11-13-R119-positive-DN-Airy-endangles-budget.json)
核对实际光学下界、完整矩阵和源幂、两端密度及无限层和。
