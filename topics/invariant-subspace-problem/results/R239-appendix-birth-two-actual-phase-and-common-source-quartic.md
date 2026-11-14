# R239 附录：出生二一般内部位置的实际三参数相位、四点曲率与共同源四次式

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文证明完整有理归一化和必要域条件。一般出生二内部相邻比较仍开放。始终使用原二项式系数 Z 的实际相位，不把二阶 Hankel 行列式当成负实根多项式。配套[可导入函数和五维校准](../notes/2026-11-14-birth-two-actual-phase-quartic-0c.py)及[通用有理恒等证书](../notes/2026-11-14-birth-two-actual-phase-universal-identities-0c.py)均完整保存。

## 1. 真实对象、索引与原全逆

普通组大小为整数 $q,L\ge4$，权平方为 $z,1$，异常位权平方为 $w>0$。出生二高度为 $h=q+L-3$。首末前两边已证；本稿取 $2\le n\le h-2$，未付位置为 $3\le n\le h-3$。置
$$m=h-n,\quad k=n+1,\quad M=q+L-k=m+2,\quad N=k+1=n+2,\quad H=M+N.$$
未付范围有 $M,N\ge5$，它们不是原两个组大小。

使用原有限测度
$$\nu_j(i)=\binom qi\binom L{j-i}z^i,\quad Z_j=\sum_i\nu_j(i),\quad
\mu_j=\Theta\log Z_j,\quad V_j=\Theta^2\log Z_j,\quad\Theta=z\partial_z.$$
令 $\Delta_a(j)$ 为其 $a$ 阶矩行列式，$\Delta_0=1$，并记
$$\gamma_j=\frac{\Delta_1(j)\Delta_3(j)}{\Delta_2(j)^2}>0,\qquad C_j=Z_jV_j.$$
四点 $j=k-1,k,k+1,k+2$ 均有至少三个合法占据数，故 $V_j,\gamma_j>0$。

[一般互补 Hankel 与完整出生二源](R239-appendix-general-birth-dual-hankel-and-birth-two-full-source.md)给
$$a_j=\frac{\mathcal C_q}{C_{j+1}},\qquad
b_{j-1}=\frac{\mathcal C_q}{C_{j+1}\gamma_{j+1}},\qquad \mathcal C_q=(q!)^2z^q.$$
这里特意区分归一常数 $\mathcal C_q$ 与序列 $C_j$。原共同源来自完整五维群固定出生层：
$$H_j=E_w^*(A_jW_j^{-1}A_j^*)^{-1}E_w.$$
内层先作五维全逆，之后才压二维 primitive。原 MP 归约给
$$H_j=\begin{pmatrix}a_j+wa_{j+1}+B_j\kappa_j^2&-B_j\kappa_j\\-B_j\kappa_j&B_j\end{pmatrix},$$
$$B_j=\frac{wb_{j-1}b_j}{b_{j-1}+wb_j},\quad
\kappa_j=c_{j+1}-c_j,\quad c_j=\text{常数}-\Theta\log\Delta_2(j+1).$$
不要求 $q\le L$：相对出生 $2\le\min(q,L)$ 使缺失次数 $D=q-1$ 满足 $L+D\ge q+1$，短池额外最高源约束为空。$z<1$ 交换普通组并整体缩放为 $(L,q,1/z,w/z)$；$z=1$ 属已证两权模型。以下取 $z>1$。

## 2. 同一原 Z 的三个实际正参数

定义
$$p=(q-\mu_k)/M,\quad r=\mu_{k+1}/N,\quad
A=p(1-p),\quad B=r(1-r),\quad d=r-p.$$
原删位恒等式给
$$\frac{r(1-p)}{p(1-r)}=z,\qquad c=\frac{1-r}{1-p}>0,\qquad
\frac{Z_k}{Z_{k+1}}=\frac NM c.$$
故 $0<p<r<1,d>0$。再置
$$\theta=\frac{V_{k+1}}{NB}\in(0,1),\quad
V_k=MA(1-\theta),\quad V_{k+1}=NB\theta,$$
$$u=\frac{A(1-\theta)}{B\theta}>0,\quad
\eta=\frac{d^2\theta}{A}>0,\quad\tau=\frac\theta{1-\theta}>0,\quad g=B\theta.$$
同一实际身份还有 $q=(M-1+\theta)p+(N-\theta)r$。记
$$\alpha=N-1-u\eta,\quad\beta=M-1-\eta,$$
$$J=u(M+1+\eta)-N+1,\qquad K=N+1-u\beta.$$
[原出生一相位](R239-appendix-birth-one-actual-three-positive-parameter-normalization.md)的直接删位证明及[矩形 Turán 自足证明](R239-appendix-rectangular-turan-endpoints-and-sharp-curvature-caps.md)给
$$\alpha,\beta,J,K>0,$$
$$R=\frac N{Mu}-\frac{(N-1)J\tau}{Mu\alpha}
=\frac{C_{k-1}C_{k+1}}{C_k^2},$$
$$T=\frac{Mu}N-\frac{(M-1)K}{N\beta\tau}
=\frac{C_kC_{k+2}}{C_{k+1}^2},\qquad0<R,T<1.$$
这些是实际必要条件，不声称单凭它们刻画可实现相位。

## 3. 两个中间二阶曲率的直接计算

有 $\Delta_2=Z^2V$。设 $m_a=\sum_i i^a\nu(i)$，则
$$\Delta_2=m_0m_2-m_1^2,\quad
\Theta\Delta_2=m_0m_3-m_1m_2,\quad
\Theta^2\Delta_2=m_0m_4-m_2^2.$$
直接展开三阶行列式，
$$\Delta_2\Theta^2\Delta_2-(\Theta\Delta_2)^2=m_0\Delta_3.$$
因此
$$\boxed{\gamma_j=2V_j+\Theta^2\log V_j.}\tag{3.1}$$

置 $\delta=Mu-N,\ \mathcal D=\Theta/d$。由
$\Theta p=-A(1-\theta),\Theta r=B\theta$ 及上节 q 身份，逐项微分得到
$$\mathcal Du=u(2\theta-1)+\frac{(1+u)(2\theta-1)+\delta}{\eta},$$
$$\mathcal D\eta=\frac{(1-\theta)K}{u},\qquad
\mathcal D\theta=\frac{\theta(1-\theta)[u-\delta-(1+u)\theta]}{\eta u},$$
$$\frac{\Theta d}{d^2}=\frac{\theta(1-\theta)(1+u)}{\eta u}.$$
可用 $B=A+d(1-2p)-d^2$，即
$$(1-2p)/d=1+[(1-\theta)/u-\theta]/\eta,$$
消掉 p 核验以上身份。并且
$$\frac{\Theta\log V_k}{d}=-(1-\theta)+\frac{\theta(\delta+2)-1}{\eta u},$$
$$\frac{\Theta\log V_{k+1}}d=-\theta+
\frac{u-\delta-(2u-\delta)\theta}{\eta u}.$$
再次应用 $\Theta=d\mathcal D$，用 (3.1) 得
$$\boxed{\phi_0:=\gamma_k/g
=\frac{J[N+(N-1)\tau]-2u(H-1)}{\eta u},}\tag{3.2}$$
$$\boxed{\phi_1:=\gamma_{k+1}/g
=\frac{K[M-1+M\tau]-2(H-1)\tau}{\eta\tau}.}\tag{3.3}$$
分子减项全部保留；严格正性来自原 Hankel 行列式。

## 4. 双向一步相位与外侧曲率

同一个 Z 族在 $k+1$ 的相位为
$$\boxed{(M,N,u,\eta,\tau)_+
=\left(M-1,N+1,\frac{u\beta}{(M-1)T},
\frac{\eta NT}{u\beta},\frac{\beta T\tau}{M-1}\right),}\tag{4.1}$$
在 $k-1$ 为
$$\boxed{(M,N,u,\eta,\tau)_-
=\left(M+1,N-1,\frac{u(N-1)R}{\alpha},
\frac{u\eta M}{N-1},\frac{(N-1)\tau}{\alpha R}\right).}\tag{4.2}$$
证明：普通系数递推给 $c_+=c(M-1)/\beta,\ c_-=c\alpha/(N-1)$。
再用 $C_k/C_{k+1}=cu$ 以及 R,T 的真实比例先得到 $u_+,u_-$；邻阶递推给
$$u_+\eta_+=N\eta/(M-1),\qquad\eta_-=Mu\eta/(N-1).$$
最后将 $R_+=T,T_-=R$ 分别代入对应的 R,T 一次式，唯一解出所列 $\tau_+,\tau_-$；相应 $J_+,K_->0$ 保唯一性。全步骤也可直接在有理函数域核验。

又有 $g_-/g=Mu/(N-1),\ g_+/g=NT/(u\beta)$。于是以 (3.2)–(3.3) 的同一函数记号，
$$\boxed{\phi_-:=\gamma_{k-1}/g
=\frac{Mu}{N-1}\phi_0((M,N,u,\eta,\tau)_-),}$$
$$\boxed{\phi_2:=\gamma_{k+2}/g
=\frac{NT}{u\beta}\phi_1((M,N,u,\eta,\tau)_+).}\tag{4.3}$$
各高度不另取自由参数。

## 5. 同一个原源的合同、几何倍数和异常权

三个相邻矩阵使用同一个
$$S=\begin{pmatrix}1&0\\\kappa_n&\sqrt{\gamma_k}\end{pmatrix},$$
并将第 j 阶乘 $f_j=(C_k/\mathcal C_q)c^{k-j-1}>0$。由于
$f_{n-1}f_{n+1}=f_n^2$，这保相邻 Schur 比较；共同 S 保全逆次序与源。只把异常权重命名 $\omega=cw>0$。

规范高、低四元组为
$$\boxed{(a,b,c_*,d_*)=(1/(uR),1,u,u^2/T),}\tag{5.1}$$
$$\boxed{(p_*,Q_*,r_*,s_*)=
\left(\frac{\phi_0}{uR\phi_-},1,
\frac{u\phi_0}{\phi_1},\frac{u^2\phi_0}{T\phi_2}\right).}\tag{5.2}$$
整个新高组等于出生一旧低组；新低组中的二阶曲率不可省略。
[实际两权全部出生严格定理](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)给
$$\boxed{0<R_2:=R\phi_-\phi_1/\phi_0^2<1,\quad
0<T_2:=T\phi_0\phi_2/\phi_1^2<1.}\tag{5.3}$$

令
$$\chi_2=(z-1)^2c^2\gamma_k=\frac{\eta\phi_0}{u\tau}>0.$$
[实际两向 Pearson](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md)在上述同源合同下给中心剪切零及
$$\boxed{x=\sqrt{\chi_2}\frac{1/p_*-u}{n},\qquad
y=\sqrt{\chi_2}\frac{d_*/r_*-u}{n+1}.}\tag{5.4}$$
所有平方与交叉项都为实际三参数的有理式。有效反向参数是
$$zc^2=B/A=1/(u\tau),$$
故写 $(A_2,B_2,C_2,D_2)=(\phi_-,\phi_0,\phi_1,\phi_2)$ 时，
$$\boxed{RA_2-B_2=\frac{n\tau}{uR(m+1)}(RC_2-B_2),}$$
$$\boxed{C_2-TD_2=\frac{mu}{\tau(n+1)T}(C_2-TB_2).}\tag{5.5}$$
这可消去两外曲率，不能把有效参数误写成原 z。

## 6. 完整四次式和未付的严格目标

沿上节记号，置
$$\Lambda=(ac_*-b^2)+\omega(ad_*-bc_*)+\omega^2(bd_*-c_*^2),$$
$$\Phi=p_*Q_*(Q_*s_*-r_*^2)+\omega Q_*r_*(p_*s_*-Q_*r_*)
+\omega^2r_*s_*(p_*r_*-Q_*^2).$$
对完整相邻差 $\mathcal K=\widetilde H_{n-1}-\widetilde H_n
\widetilde H_{n+1}^{-1}\widetilde H_n$，有
$$P=\det\mathcal K\,(p_*+\omega Q_*)(Q_*+\omega r_*)^2(c_*+\omega d_*)s_*/\omega,$$
$$\begin{aligned}
P={}&Q_*\Lambda\Phi
-\omega p_*Q_*^3r_*(c_*+\omega d_*)(r_*+\omega s_*)x^2\\
&-\omega Q_*^2r_*^2s_*(a+\omega b)(p_*+\omega Q_*)y^2\\
&-2\omega p_*Q_*^2r_*s_*(b+\omega c_*)(Q_*+\omega r_*)xy\\
&-\omega^2p_*Q_*^3r_*^2s_*x^2y^2.
\end{aligned}\tag{6.1}$$
所有剪切费用保留。首主子式及 $P_0,P_4$ 已由两条实际两权标量严格比较支付。剩余需证明 $P(\omega)>0$ 对全部实际相位和 $\omega>0$；三个中系数分别正是充分途径，本稿不宣称已完成。

## 7. 精确核验的范围

可导入程序的独立主程序用
$$(q,L,n,z,w)=(4,4,2,4,9),(4,6,3,4,4),(5,7,4,4,9),(6,4,3,4,9)$$
核双向相位、四曲率、高低原范数、$\chi_2$，并在原五维层先取全逆，逐个核三个相邻矩阵及其清分母行列式。这排查尺度与源次序，不从实例推断正性。

另一个自含程序在未代参数的有理函数域核二阶曲率微分、双向相位一步、两向 Pearson 消外曲率和完整 Schur 四次式。两个程序均由作者在终端失联前运行通过；根代理已全文核推导，失联时发起的根重跑未完成，不另计一份通过记录。正文的全参数身份由上述有限代数推导承担，一般正性保持开放。
