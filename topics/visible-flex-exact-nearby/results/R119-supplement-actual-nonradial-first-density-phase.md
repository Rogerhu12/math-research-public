# R119 续篇：真实非径向返回的首密度相位与两根有限部

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇在第46束所选、并由
[重建的两参数全尾图](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
重新实例化的同一个实际对象上，识别非零标签背景下的完整局部返回行的首个
\(1/n\) 系数。正型两端反射、两根、原径向严格切口、真实特征角图、height
乘子及 normal shear 均参加这个识别。没有用严格内部的形式相位替代返回算子。

本篇的“返回行”是原有序全网络方程中的行，尚未消去其它负分量或有限低块。
其跨分量列留在完整余项中。后文得到的是每个实际分量的首符号及显式标量
差预算；**没有**把逐分量的有限余项常数称作已支付的全网络 Green 常数。

## 1. 对象、单位和结论

采用
[完整径向返回](R119-supplement-actual-complete-radial-return-first-phase.md)
及
[两参数完整算术](R119-supplement-actual-two-parameter-complete-phase-arithmetic.md)
的固定径向参考 \(\Gamma^0\)，其每个负分量记为 \(I_i\)，较深胞元编号为
\(j\)。物理角周期为 \(\pi/2\)，\(m\in4\mathbb Z\)，标准角
\(x=4\theta\)，其正锥频率为 \(n=m/4>0\)。

真实背景由同一个完整标签图给出。写
\[
 N_j=2^{184}h_j^{-5}{\zeta_j\over\mu_j\delta_j^2},\qquad
 N_j^\#=N_j+\mathbf1_{j\ge130}N_{j-1},\qquad
 n_i=4N_j^\#\|X\|,\qquad \|X\|\le2^{-262144}.                 \tag{B.1}
\]
所有频率都在 \(X\) 内。后文的 \(n_i\) 是状态上界，不能与标准 Fourier
指标 \(n\) 混同。使用两参数复盒
\[
 |\gamma_1|<2^{-15},\qquad |\gamma_2|<2^{-29};
\]
涉及 selfadjointness 的结论在实背景上使用，标量函数及其差界同时延至已经
支付的复标签和复参数域。

真实齐次 Jacobi 算子是
\[
 P h=\operatorname{div}(G\nabla h),\qquad
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Qv^2\end{pmatrix},
\quad
 \mu={w_{\rm ref}\over a}JD^{-3/2},\quad
 v={\sqrt D\over J},\quad Q=-A_\Gamma>0.                    \tag{B.2}
\]
其中 \(d,J,D\) 以及 raw 高度、conormal 的定义完全采用
[实际严格密度证明](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)。
设
\[
 \Lambda=\sqrt{-\det G}={w_{\rm ref}\over a}{\sqrt Q\over D},
 \quad m_0=\Lambda^{-1/2},\quad
 \kappa={P(m_0)/m_0\over\Lambda}.                          \tag{B.3}
\]
在严格区，
\[
 \kappa=-\tfrac12\operatorname{div}((G/\Lambda)\nabla\log\Lambda)
        -\tfrac14\nabla\log\Lambda\cdot(G/\Lambda)\nabla\log\Lambda .
                                                                    \tag{B.4}
\]

每根的真实 canonical 坐标 \((\xi_e,\phi_e)\) 与
[联合解析根](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
相同；\(\xi_e>0\) 向负区，\(b_e=|A_t(t_e)|>0\) 是原参考的根斜率。
两个 compact bump 不进入根邻域，因此 \(b_e\) 不随它们改变。
令 \(\Omega_\epsilon\) 为整个负圆柱中删去两个
\(0<\xi_e<\epsilon\) collar 后的真实区域。定义
\[
 \mathfrak b_i(a,\Gamma)=
 \lim_{\epsilon\downarrow0}
 \left\{\frac12\int_{\Omega_\epsilon}\kappa\,dt\,{d\theta\over\pi/2}
       -\sum_{e=\pm}{5b_e\over48\epsilon^{3/2}}\right\},
 \qquad
 \boxed{\ \beta_i(a,\Gamma)=-\mathfrak b_i(a,\Gamma)/2.\ }     \tag{B.5}
\]
区域和完整密度均是真实非径向的。这个极限存在、与合法 root cut 无关，
并且是实际返回行的首相位。在把真实 principal return 共轭成
\(x\mapsto x+\omega_i\) 后，该行在正锥可写成
\[
 I+\mathcal U_{\omega_i}
       [I+i\,\operatorname{Op}(B_i(x)/n)]+\mathcal R_i,
 \qquad \langle B_i\rangle_x=\beta_i(a,\Gamma),              \tag{B.6}
\]
其中在任意固定有限 Sobolev 窗上
\(\mathcal R_i:H^s\to H^{s+4/3}\) 有界。这里的常数是每个真实分量的有限
常数；本篇不宣称其层和已付。负锥是对应的真实共轭行。两 mean、低模及
两端正型跨列保留在完整算子中；它们未被 (B.6) 的高频记号删除。

在 \(a=0\) 时，(B.5) 准确退化为径向篇的 \(b_i\) 及
\(\beta_i=-b_i/2\)，而不是另选的相位参数。

## 2. 两个准确不变量

若 \(\Psi\) 为保向坐标变换，\(\mathfrak J=|\det D\Psi|\)，则
\[
 G_c=[\mathfrak J^{-1}D\Psi\,G(D\Psi)^T]\circ\Psi^{-1},
 \quad \Lambda_c=\Lambda\circ\Psi^{-1},\quad
 \kappa_c=(\kappa/\mathfrak J)\circ\Psi^{-1}.                 \tag{B.7}
\]
第一式是散度密度的 Piola 变换；二维 determinant 直接给第二式，再对
\(m_0\) 应用散度变换即得第三式。因此
\(\kappa\,dt\,d\theta\) 是准确的二维密度。

若作真实 height 共轭 \(\widetilde P=tPt\)，则
\[
 \widetilde\Lambda=t^2\Lambda,\qquad
 {\,\widetilde P(\widetilde\Lambda^{-1/2})\over
       \widetilde\Lambda^{-1/2}}
 =t^2{P(\Lambda^{-1/2})\over\Lambda^{-1/2}},\qquad
 \widetilde\kappa=\kappa .                                  \tag{B.8}
\]
同时若 \(h=t\widetilde h\)，则密度高度
\(w=\sqrt\Lambda h=\sqrt{\widetilde\Lambda}\,\widetilde h\) 准确不变。
所以这里没有省掉 height 乘子的导数或 normal shear。

在 canonical 根中，真实 height 共轭给
\[
 P_c=\partial_\xi^2-{\xi\over b^2}\partial_\phi^2+V(\xi,\phi).
\]
此时 \(\Lambda_c=\sqrt\xi/b\)，故
\[
 \kappa_c=b\left({5\over16\xi^{5/2}}
                       +{V(\xi,\phi)\over\sqrt\xi}\right). \tag{B.9}
\]
\(V\) 在整根邻域解析，\(|V_0|<16,\ |V-V_0|<2^{32}n_i\)。
把 (B.9) 真正积分，得到
\[
 \frac12\int_\epsilon^H\langle\kappa_c\rangle d\xi
 -{5b\over48\epsilon^{3/2}}
 =b\left[\frac12\int_\epsilon^H
             {\langle V\rangle\over\sqrt\xi}d\xi
                      -{5\over48H^{3/2}}\right].           \tag{B.10}
\]
这证明 (B.5) 的存在；也固定了有限部的系数与符号。两根均使用正密度
Jacobian；右根的径向方向另在完整两行交换矩阵中保留。

## 3. 严格区的真实首符号

保留严格密度篇的两个独立 mean，写
\[
 y_\sigma=(w_\theta+\sigma\zeta)/2,\qquad
 (y_\sigma)_t+\partial_\theta(g_\sigma y_\sigma)
       =-\sigma\kappa w/2,\qquad g_\sigma=-d-\sigma\nu ,
 \quad \nu=\sqrt Q\,v .
\]
令真实流 \(H_\sigma\) 满足 \(H_{\sigma,t}=g_\sigma\circ H_\sigma\)，
\(S_\sigma=H_\sigma^{-1}\)，并令
\[
 X_\sigma=H_\sigma' y_\sigma\circ H_\sigma,\quad
 Z_\sigma=X_\sigma-\sigma\alpha,\quad
 w=c+\alpha(S_+-S_-)
       -i\sum_{\tau=\pm}C_{S_\tau}D_\theta^{-1}Z_\tau.        \tag{B.11}
\]
其中 \(D_\theta^{-1}\) 只在 mean 定义为0，\(\alpha,c\) 仍是独立状态。
准确 generator 的非mean部分为
\[
 (Z_\sigma)_t=
 {i\sigma\over2}\sum_\tau
  \Pi_0\mathcal D_{H_\sigma}M_\kappa C_{S_\tau}
              D_\theta^{-1}\Pi_0 Z_\tau
       +\hbox{完整 mean 列},                               \tag{B.12}
\]
\(\Pi_0=I-\langle\cdot\rangle\)，\(\mathcal D_H=M_{H'}C_H\)。
没有交换真实投影和 pullback。

对同支 \(\tau=\sigma\)，乘法准确化为
\(M_{H_\sigma'\kappa\circ H_\sigma}\)；因此其首 Dyson 项的
\(D_\theta^{-1}\) 系数为
\[
 {i\sigma\over2}\int H_\sigma'(t,x)
                      \kappa(t,H_\sigma(t,x))\,dt .
\]
它的角平均准确等于
\[
                  {i\sigma\over2}\int\langle\kappa(t)\rangle dt.
                                                                    \tag{B.13}
\]
这一步使用完整 Jacobian，不能把 \(H_\sigma\) 直接换成径向平移。

跨支的相位图是 \(S_\tau\circ H_\sigma\)；其径向导数为
\((g_\sigma-g_\tau)S_\tau'\circ H_\sigma\)，在本严格闭段上不为0。
对真实 Fourier 核作一次径向分部积分，原 \(D^{-1}\) 再得到一个
\(D^{-1}\)。边界项及所有实际径向分片跳变均保留，因此这一项为
\(H^s\to H^{s+2}\)。所需系数在每个实际片光滑、总变差有限；
原 log profile 的 \(C^2\) 接缝按此处理，不假设跨接缝径向解析。
二次及以上 Dyson 项也至少含两个降一阶因子，在任意固定 Sobolev
窗给同样的二阶增益。

上述结论是完整 Fourier 算子结论：同号频率用真实相位图；异号远锥的核
反复角分部积分；有限低频和 mean 列在解析角系数下为平滑列。
每个分量所需的角导及径向总变差有限。这同时证明 (B.13) 没有遗漏一个
来自低部/mean 的首符号，且不把低部/mean 从方程中删去。

## 4. 两个真实根的首项，包括角混合

在根的准确 canonical 方程中使用原两行 Airy 基，
\(\kappa_m=|m|/b\)。对实 \(V(\xi,\phi)\)，一次 interaction 的
Fourier 核是
\[
 F_m(\xi)^{-1}
   \begin{pmatrix}0&0\\-V_{m-n}(\xi)&0\end{pmatrix}F_n(\xi).
                                                                    \tag{B.14}
\]
因此全部 Fourier lag 都参加。令自由光学时间
\(\tau(\xi)=2\xi^{3/2}/(3b)\)。在同号锥上，一次同支项的首系数为
\[
 {i\sigma b\over2}\int_0^H
  {V(\xi,\phi+\sigma\tau(\xi))\over\sqrt\xi}\,d\xi\,
                  D_\phi^{-1}.                            \tag{B.15}
\]
改变自由流的原点只平移该系数，不改变其角平均。

这里可以直接使用径向篇的 Airy 两行估计证明完整混频余项，所需步骤如下。
将 Fourier lag \(k=m-n\) 分为 \(|k|\le |n|/2\) 与其余部分。在前一部分，
两 Airy 频率可比；用完整 Airy 两行渐近，把
\((|m||n|)^{-1/2}\) 换成 \(|n|^{-1}\) 的误差由
\(C|k||n|^{-2}\) 控制。根层切在 \((|n|/b)^{-2/3}\)，根层积分、
同支首项替换误差及跨支振荡积分均为 \(C|n|^{-4/3}\)。
需要的一次径向分部积分使用完整 \(V_\xi\)，它已由已付整复盘 Cauchy
控制。在其余 lag 上，真实角解析性给
\(|V_k|+|\partial_\xi V_k|\le C e^{-c|k|}\)，吸收所有 Airy 频率比例。
把这些逐 lag 界先乘 Sobolev 权比，再作卷积和，得到完整矩阵
\(H^s\to H^{s+4/3}\) 界。一次 interaction 的完整积分至多降 \(2/3\)
阶，故二次及以上 Dyson 积分给 \(4/3\) 阶；同一卷积论证允许在中间
因子分配这两个 \(2/3\) 权。有限频率及 mean 仍按原完整基直接保留。
这不是固定 Fourier 列的渐近替代。

在真实 \(H=1/64\) 处，密度高度满足准确两行关系
\[
 w={\xi^{1/4}\over\sqrt b}\,u,\qquad
 \zeta=\sqrt b\,\xi^{-1/4}
                  (u_\xi+u/(4\xi)).                       \tag{B.16}
\]
因此原 height 的 \(\alpha\)、根的 \(b\) 以及 normal shear 全部相消到
径向篇采用的同一 wave 单位。原自由 Airy 两行在该单位的次首相位是
\[
                          -{5b\over48H^{3/2}}D_\phi^{-1}. \tag{B.17}
\]
这是两行渐近的结果；单独 height 渐近不足以给出该值。
(B.15)--(B.17) 的平均正好是 (B.10)。

根的 constant canonical cut 到原固定 \(t\) cut 使用
[真实图迹两端口](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)。
图上密度态准确为
\[
 Y_\sigma=[1+\sigma c(g)g']y_\sigma(g,\phi),\qquad
 c=\sqrt\xi/b,\quad
 W_\phi=Y_++Y_-,\quad p_{d,g}=Y_+-Y_- .                    \tag{B.18}
\]
用第3节的同一真实 transport 对这段严格图区域积分，其首平均就是
该区域的 \(\frac12\kappa_c\,d\xi\,d\phi\)，有向图差可以变号；
没有除以图高。由 (B.7)，这与原固定 \(t\) 区域的密度积分完全一致。
从而 (B.5) 真正属于原物理两端口。

## 5. 实际正型完整双端反射不贡献一阶相位

本节重新实例化
[R45 完整 Ai/contact 论证](R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md)
的变分结构；不使用该旧帽的数值、度量或 Poisson 算子。

每个实际正型分量使用
[正型双端 DN](R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md)
及
[真实端角 DN](R119-supplement-positive-DN-in-actual-Airy-endpoint-angles.md)
的同一个非负 selfadjoint 双端 form。固定两根的 raw 高度后，
零边界子空间由径向 Poincare 控制，因此有完整 Dirichlet Poisson 解。
它在两个 canonical collar 中满足
\[
 \|U\|_{L^2_yH^{2/3}_\lambda}
 \le C_i(\|u_L\|_{H^{1/3}_{\lambda_L}}
             +\|u_R\|_{H^{1/3}_{\lambda_R}}),\quad
 \lambda_e=|m|/b_e,                                      \tag{B.19}
\]
其中 \(C_i<\infty\)。证明并不需要正型端间传输的逆：
在两根各作支集互不相交的径向 ramp，其长为
\(\min(H,\lambda_e^{-2/3})\)，求得有限试验能量；最小能量原理给真解能量。
在根处 \(u=\sqrt\alpha h\)，已付根界给
\(|\partial_\xi\log\alpha|<9\) 及极小角导，故
\(|\nabla\log\alpha^{-1/2}|_{\operatorname{diag}(1,y/b_e^2)}<5\)；
\(5H<1\) 吸收真正 height 梯度项。逐模按
\(y=\lambda_e^{-2/3}\) 分割的径向 trace 不等式，再给 (B.19)。
这包括两个 mean，未在内端另设人工边界。

对每端、每个非mean 输入取完整截断 Ai trial；另外一端 trial 为0。
真实 residual 恰为
\[
       -\chi VU_0-2\chi' U_{0,y}-\chi''U_0.               \tag{B.20}
\]
所有 cutoff 项保留。由
\(\int_0^\infty\operatorname{Ai}(z)^2dz=\operatorname{Ai}'(0)^2\)、
真实尺度 \(z=y\lambda^{2/3}\)、角乘法有界及正轴 Airy 指数尾，整个
residual 右乘 \(\langle\lambda\rangle^{4/3}\) 后仍有
\(L^2\to L^2_yH^{-2/3}_\lambda\) 的有限界。
这里先作径向平方积分及 Parseval，再估全 Fourier 卷积，故保留全部 lag。
(B.19) 的 Poisson 对偶给完整 contact 校正，包括另一端的 contact。
两端原 Airy frame 的 Wronskian 相同且非零；它们与真实 raw 两迹间的
height、角 Jacobian、normal shear 都是已付 Green 变换。
完整 selfadjoint 图因此给全空间酉反射 \(R_+\)。

若试验的 incoming/outgoing 图为 \(I+E_A,-I+E_B\)，则准确有
\[
 R_+(I+E_A)=-I+E_B,\qquad
 R_++I=E_B-R_+E_A .                                      \tag{B.21}
\]
无需反解 \(I+E_A\)，更无需反解 tiny cross。刚才的 contact 界给
\((R_++I)\langle D\rangle^{4/3}\) 有界；酉性及
\(R_++I=(R_++I)^*R_+\) 给左侧同阶界。
两根 mean 列采用原完整 mean Airy 基；trial 在这些列为0时
\(E_A=-I,E_B=I\)，所以它们有完整有限费用而非被指定反射值。
角微分该变分问题，并用真实解析系数的有限卷积界，给任意固定有限
Sobolev 窗的对应有界性。因此
\[
                    R_+=-I+\mathcal O_{4/3}              \tag{B.22}
\]
是完整双端算子结论，off-diagonal 也在其中。
这些每段常数的存在足以识别首符号；本篇没有借此授予其无限层和。

## 6. 返回代数与角图不变量

对保向圆图 \(H\)，准确 primitive 恒等式是
\[
 D^{-1}\mathcal D_H=C_HD^{-1}
                    +\hbox{完整 mean 修正}.               \tag{B.23}
\]
因此一个首项 \(M_aD^{-1}\) 在真实 density 角图共轭下的首系数为
\(H'a\circ H\)，其积分准确保持。其余项至少降二阶；
mean 修正是保留的平滑有限维列。等价地，在两锥的平衡空间用
\(|D|^{-1/2}\mathcal D_H|D|^{1/2}\)；正负锥间为平滑项。
因 signed primitive 的 Green 配对准确保持，该表示在各锥酉至平滑项，
可作平滑的 polar 校正而不改变首系数。这里没有假设裸 pullback 与恒等
在同一 Sobolev 阶上范数接近。

需要把一行的首个椭圆因子规范成恒等时，只反解它的足够高频块：
该块为 \(I+\mathcal O_1\)，选一个有限 \(N_i\) 使高块差小于 \(1/2\)，
在低块用恒等并保留全部交叉列。这个全空间行变换可逆；其有限低块及交叉
差都保留在余项中。没有借此假设原低 Schur 可逆，也没有给出一个免费的
统一 \(N_i\)。

在模掉 \(4/3\) 阶余项后，首项相乘只需相加：
两个降一阶项之积降二阶；把首项搬过真实 principal 图使用 (B.23)。
将第3、4节的两支完整两行传递按径向篇的原顺序相乘，右根保留其准确
交换矩阵，两根各保留 \(\pi/4\)。第5节的正型双端反射无降一阶项。
于是实际返回的首平均是负两支遍历密度积分之和。
在物理频率 \(m\) 中它为
\[
             -\operatorname{FP}\int\langle\kappa\rangle dt\,/m .
\]
改用 \(m=4n\) 正好得到 (B.5)--(B.6)。
此号数还可直接由径向两行式
\(\Phi=mS+\pi/2+b/m\)、返回 \(-2b/m\) 校准；
所有变换在同一实连通标签球连续，未另选分支或 Maslov 号。

若 principal return 已由实际 KAM 共轭为平移，令
\(B_i-\beta_i\) 为其零均值首系数。真实 Diophantine \(\omega_i\) 给
\[
 q_i(x)-q_i(x-\omega_i)=\beta_i-B_i(x).                    \tag{B.24}
\]
Fourier 除数与原 KAM 相同；真实解析角宽给 \(q_i\) 在任意较窄条带有限。
取自伴降一阶 \(Q_i\) 的首符号为 \(q_i/n\)，并在 mean 为0，令
\(T_i=e^{iQ_i}\)。直接乘开得
\[
 T_i^{-1}\mathcal U_{\omega_i}
 [I+i\operatorname{Op}(B_i/n)]T_i
 =\mathcal U_{\omega_i}\exp(i\beta_iD_x^{-1})
                  +\mathcal O_{4/3}.                     \tag{B.25}
\]
所有低模、两 mean 和 source 同时经这个有界可逆图变换。
(B.25) 不声称 \(T_i-I\) 的无限层统一费用已经足够全网求逆。

## 7. 完整标量差预算，而非形式相关误差

在原固定 \(t\) 严格切口之间，严格密度篇给
\[
 \int\|\kappa-\kappa_{0,\Gamma}\|_{\mathcal A_1}dt
       <2^{130}(j+4)^2\delta_j^{-5}N_j^\#\|X\|.             \tag{B.26}
\]
在每根的同一 canonical 点比较，真实
\(|V-V_0|<2^{32}n_i\)。在 \(H=1/64\) 处，其有限部差至多
\(2^{32}b_e n_i\sqrt H\)。原固定 \(t\) cut 是图
\(\xi=H+d(\phi)\)，\(|d|<2^{13}n_i\)；
\(H/2<\xi<2H\) 上 \(|\kappa_c|<2^{17}b_e\)。
所以图差的完整密度积分另付 \(2^{30}b_e n_i\)，两端都支付。
参考的对应图是常图，不漏移动 cut 的端项。
用
\[
 b_e<2^{16}\sqrt{j+5}\,\delta_j^{-9/4}
\]
及 (B.1)，得到刻意放宽的统一界
\[
 \boxed{\quad
 |\beta_i(a,\Gamma)-\beta_i(0,\Gamma)|
 <2^{144}(j+5)^3\delta_j^{-5}N_j^\#\|X\| .
 \quad}                                                     \tag{B.27}
\]
这是完整实际返回首系数的界。它没有比较两个发散积分的绝对误差。

同一界在参数的小复邻域成立：两 compact 支集的
\(|Q|>1/128\) 保持，平方根固定在正实支的解析延拓；
其它严格区的参考 \(Q\) 不变。严格篇的商法则只需绝对值下界，
根篇本来就在完整复域中。上式额外的 \(2^{14}(j+5)\) 余量已覆盖
实/复包络放宽。

用第43束的真实
\[
 \mathcal B_i=\sqrt{12}\Delta_i/\eta_j>\delta_j^{-3/2},
 \qquad K_j^{\rm ref}=2^{5000}(j+4)^5\delta_j^{-10},
\quad
 \sum_{j\ge129}(K_j^{\rm ref})^2N_j<2^{160000},              \tag{B.28}
\]
每一归一行的权小于
\(2^{144}(j+5)^3\delta_j^{-17/4}\le(K_j^{\rm ref})^2\)。
四过渡的每胞元至多四个负分量；邻层项用
\((K_j^{\rm ref}/K_{j-1}^{\rm ref})^2<2^{21}\) 支付。
因此完整无限行同时满足
\[
 \boxed{\quad
 \sum_i {|\beta_i(a,\Gamma)-\beta_i(0,\Gamma)|
                      \over\sqrt{\mathcal B_i}}
             <2^{160032}\|X\| .
 \quad}                                                     \tag{B.29}
\]
该和消费真实有限129--8192前缀及两个全局逆幂；
没有用深尾最终正指数替代它们。

## 8. mean、ordinary/weak source 和度量参数列的准确范围

识别齐次首系数不删除仿射方程。对
\(Ph=f-\operatorname{div}F\)，密度高度的真实源仍为
\[
 F_d=m_0F,\qquad
 f_d=m_0\big(f-\tfrac12\nabla\log\Lambda\cdot F\big).         \tag{B.30}
\]
原总 conormal、mean 方程准确保留：
\[
 p+F^t=\sqrt\Lambda\,\zeta-T\Lambda^{-1/2}w,\quad
 T={\mu\over2}(\ell_t-d\ell_\theta),\quad
 \alpha'=\tfrac12\langle f_d-\kappa w\rangle,
\]
\[
 c'=-\alpha'\langle S_+-S_-\rangle
       +i\sum_\sigma\langle C_{S_\sigma}D_\theta^{-1}Z_\sigma'\rangle
       -\langle\nu F_d^t\rangle .                         \tag{B.31}
\]
在根的真实坐标中先用 Piola
\(f_c=(f/\mathfrak J)\circ\Psi^{-1}\)、
\(F_c=(D\Psi F/\mathfrak J)\circ\Psi^{-1}\)，再作 height 变换：
\[
 F_u=\alpha^{-1/2}F_c,\qquad
 f_u=\alpha^{-1/2}
             (f_c-\tfrac12\nabla\log\alpha\cdot F_c).       \tag{B.32}
\]
随后按原图迹合同传递总通量。未对 \(F^t\) 求径向导；
若消费者要 bare conormal，必须继续提供原合同要求的真实法向端点迹。
常数 raw 高度在 canonical 中是 \(\sqrt\alpha\) 倍的函数，不能删成
canonical 的一个 Fourier 零槽。

当后续反调 \(\Gamma=\Gamma(a)\) 时，(B.5) 是该背景下**固定度量的**
齐次 Jacobi 首相位。全 \(D_aF\) 仍带 \(\dot\Gamma\) 的真实度量源；
固定物理半径还保
\(\dot t=-\dot{\log\rho}\)、移动 cut、完整 mean height 和 \(\lambda\)。
本篇没有把这些源列归入齐次相位后丢掉。

## 9. 剩余目标和证据身份

本篇给出可用于联立第二参数行的真正非径向标量 \(\beta_i\) 及
(B.29)，不只是径向导数。下一步是用实际两参数 Jacobian 保持
\(\omega_i,\beta_i\) 同时固定，再支付这些实际局部余项的全网络权、
移动中频 Schur 和完整 \(H D_0^{-1}EG\)。第48束的固定有限 head
并未因此自动扩大到所有频率；完整 \(F(a,f_*)=0\) 仍须实际闭合。

小预算由新的纯 JavaScript BigInt 有理程序
\(\texttt{scripts/fourfold_actual_nonradial_first_density_phase_20261113.js}\)
执行；输出
\(\texttt{notes/2026-11-13-R119-actual-nonradial-first-density-phase-budget.json}\)。
它核查显示有理费用、有限部代数及无限层归并的充分门。
算子、全频 Airy 和变分论证在正文给出；程序没有冒充旧 Python/native
或丢失环境的重放，也不以有限频率试验代替以上证明。
