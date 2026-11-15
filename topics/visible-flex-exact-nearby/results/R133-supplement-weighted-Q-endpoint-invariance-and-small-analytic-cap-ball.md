# R133 续篇：加权 Q 端点门与小解析帽球的完整不变域

2026-11-15，visible-exact / root。

**已证明一个带明确系数门的完整非线性帽定理；新加权系数门尚待公开计算。** 下述同一个闭集合同时控制主体范数与真实右端输入。ordinary 源、线性 Q、二次 Q、真实 nonlinear outer 响应与两 mean 均有各自的项。唯一尚未支付的局部数值门是 (E.12) 的已知系数加权范数，不能在该门通过前宣称帽解已经存在。

对象严格为原固定 eta0、ac1 候选的440866连续修补、真实区间 [9/10,25/8]。帽的 intrinsic nu-bump 为0；从内端进入的 nu 变化仍是独立边界数据。本文不把一个帽 BVP 变成全 mixed-body、尾部 height/flux 或 README 的闭嵌入族。

## 1. 同一空间、独立数据与已成源

使用[实际 L1/端点消费](../notes/2026-11-15-R133-actual-cached-cap-L1-reference-endpoint.md)及[主体球证明](R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md)。记
$$
 I=[L,R]=[9/10,25/8],\qquad \sigma=1/8192,\qquad
 \|x\|_{X_\sigma}
 =\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_I|b_k|
  +\sum_{k\in4\mathbb Z}e^{\sigma|k|}\sup_I|c_k|.
 \tag{E.1}
$$
每个 Fourier 系数先取整个径向 supremum。均值权为1；没有将两个 mean 丢弃。真正非线性结论取原反射类：B奇、C偶，B的mean因该已指定对称而为0，C的mean仍为未知输出。其使用的 reference 源门本来覆盖全四重周期频率。

给定与中心相比的内端非mean曲率变化 gamma，以及原归一外高度 f_B，要求
$$
 \|\gamma\|_{A_\sigma}\le10^{-9},\qquad
 \|f_B\|_{\dot A^2_\sigma}\le2^{-60}.
 \tag{E.2}
$$
原背景的更强 dot A^2_(1/16) 条件足以满足第二式。物理高度是 s_B f_B，s_B>0 不设为1。独立mean高度、远端标签、flux及内端相位以后按原完整 matching 读出；它们不是本式暗含的零边界条件。

本篇复用43692857656/1的实际结论，不重算旧积分：
$$
 \eta_{\rm ord}<3.038615335\,10^{-7},\qquad
 e_{\rm ord}<2.379200346\,10^{-14},
$$
$$
 a_L<3.701695746\,10^{-9},\quad
 T_*<.823763628,\quad K_G<16.
 \tag{E.3}
$$
eta_ord是ordinary源到完整pair的增益，e_ord是同源到C_nonmean(R)的增益，a_L是左C到右C的完整衰减，T_*是右d到右C的完整增益。原7296/帽1341/reference949/共同1346的身份与原22pin保持不变。

## 2. 同一 Q 列在真实右端的逐模核

令 M=|k|>=4，d=b_ref+q_M c。原真正两端 reference 为
$$
 d'=A_Dd+(-M\gamma_r+q_M\beta)Q+F_B+q_MF_C,\qquad
 c'=-A_Cc+M\gamma_r d+\beta Q+F_C ,
 \tag{E.4}
$$
其中 gamma_r是原径向系数，不是(E.2)的内端数据。A_D>=M s_D、A_C>=M s_C，s_D,s_C取原每个闭行上已证正下界。径向正系数和完整 q_M 都保留其真实 r 依赖。

定义
$$
 S(t)=\int_t^R s_C(r)\,dr,\qquad
 w(t)=e^{-2S(t)},\qquad
 T_{DC}(t)=\sup_{L\le r\le t}
          \frac{\gamma_r(r)}{s_D(r)+s_C(r)}.
 \tag{E.5}
$$
此处 s_C 可取原逐行 piecewise 常下界；w连续、正且不大于1。所有接口和真正 dr 都包含。T_DC用完整前缀，不能改成当前小格的局部值。

令ordinary源和端值暂为0。先从右积分d，再代入从左积分c。在Q(t)前的准确核是
$$
 e^{-\int_t^R A_C}
 \left[(M\gamma_r(t)-q_M(t)\beta(t))H_M(t)+\beta(t)\right],
$$
$$
 H_M(t)=\int_L^t M\gamma_r(s)
             e^{-\int_s^t(A_D+A_C)}\,ds
                  \le T_{DC}(t).
 \tag{E.6}
$$
第一式的正负号来自右向数据的 backward 解；没有把direct beta项遗漏。之后才取模。于是核模被
$$
 M s_C(t)e^{-MS(t)}\,K_e
 \tag{E.7}
$$
控制，其中可用完整固定预算
$$
 K_e=T_*T+(1+q_+T_*)K_C<5.
 \tag{E.8}
$$
这里原 T<3.625263015，q_+<1.389936764，K_C<.891297547；例如宽成
.824*3.626+(1+1.39*.824)*.892<5已足。三项都来自原完整reference，不重解Riccati。

对每个非零输出模，
$$
 \int_L^R M s_C e^{-MS}\,dt\le1,\qquad
 \int_L^R M s_C e^{-(M-2)S}\,dt\le\frac M{M-2}\le2.
$$
因此同一全模算子有两个不同的合法门：
$$
 \|(\mathcal G_Q Q)_{C,\ne0}(R)\|_{A_\sigma}
 \le K_e\|Q\|_{\mathscr A_\sigma},\qquad
 \|(\mathcal G_Q Q)_{C,\ne0}(R)\|_{A_\sigma}
 \le2K_e\|wQ\|_{\mathscr A_\sigma}.
 \tag{E.9}
$$
第二式先逐输出系数积分、再乘 e^(sigma|k|)求和；w可放在Q的径向系数上。它不把sup和Fourier求和交换。独立mean的R端值按原从右解的边界行指定，不是M趋0时(E.6)的一个特例。

## 3. 唯一新的已知加权系数门

在同一个修补中心的真实物理角中，保持
$$
 Q_B=2u,\qquad Q_C=\ell-u^2-Kv^2,\qquad
 u=\widehat B/\widehat C,\quad v=1/\widehat C .
 \tag{E.10}
$$
它们是已知背景系数，不是未知PDE解。完整联合加权范数为
$$
 q_w=\max\left\{
 \sum_k e^{\sigma|k|}\sup_I w|(Q_B)_k|,\
 \sum_k e^{\sigma|k|}\sup_I w|(Q_C)_k|
 \right\}.
 \tag{E.11}
$$
所需新门是
$$
                         q_w<10^{-5}.
 \tag{E.12}
$$
则由完整卷积及(E.9)，对任意未知全模pair x有
$$
 \|(\mathcal G_Q(Q_Bb+Q_Cc))_{C,\ne0}(R)\|_{A_\sigma}
                     <10^{-4}\|x\|_{X_\sigma}.
 \tag{E.13}
$$
包括b,c的mean与全部相互耦合；没有未知Fourier cutoff。

这个门可以只消费旧upper与一个新增的原多项式标量范围。原cap保存每个moving系数的global envelope a_k；原4650行保存完整row U_A0、V_nonmean_A0、intrinsic K/Cref。准确的mean偏移是alpha乘原65态三次多项式第32槽，不能用两个独立宽球mean_v与1/Cref之差冒准确消去。对共同分区中每行，置
$$
 D_v=|\alpha p_{32}|+\|v_{\ne0}\|_{\rm row},\quad
 L_B=2\|u\|_{\rm row},\quad
 L_C=\|u\|_{\rm row}^2+|K|(2|1/C_{\rm ref}|D_v+D_v^2).
 \tag{E.14}
$$
每个mode的合法局部界是min(a_k,L_B)或min(a_k,L_C)。先逐mode取
max_rows[w(right)*local_bound]，再求完整mode和。**不能直接把max_rows L_B或L_C称为joint norm。**

真实 inverse-angle h的joint A_(1/64)门仍为原h_*<.003774146。若sigma+h_*<1/64，完整指数卷积把原moving系数的
exp(|k|(sigma+h_*))加权和转授给(E.11)。径向scalar w与该组合交换；未知x没有被作未支付的同阶换角。

连续repair另加原A_(1/32)全pair E<4.832e-18：
QB差<=2E，QC差<=2U_*E+E^2+K_*(2V_*E+E^2)。U_*,V_*,K_*须分别来自原同对象joint/scalar门；不能用逐row最大冒joint。原mean gap、角量ω_ang=(v-m)/m及cap各mode envelope给这些门，新的consumer须显式核验。该repair不是0，也不把原ac1改标为440866。所有已成target、原1346完整卷积、原7296 residual和本次已成L1积分均不重跑。

## 4. 精确二次源与两mean

主体球证明A.17--A.19在sigma<=1/64的同一Banach代数中仍给
$$
 \mathcal R_Q(b,c)
 =\frac{b^2-2ubc+(Kv^2+u^2)c^2}{\widehat C+c},\qquad
 \|\mathcal R_Q(x)\|_{\mathscr A_\sigma}<13\|x\|_{X_\sigma}^2,
$$
$$
 \|\mathcal R_Q(x)-\mathcal R_Q(y)\|
 <13(\|x\|+\|y\|)\|x-y\|,\qquad \|x\|,\|y\|\le10^{-3}.
 \tag{E.15}
$$
原||v||<6、||u||<1/50、||Kv²+u²||<2本来在更宽的已知条带支付。mean完整卷积和分母变化费用已在13内。因而(E.9)第一门给
$$
 \|(\mathcal G_Q\mathcal R_Q(x))_{C,\ne0}(R)\|_{A_\sigma}
                            <65\|x\|_{X_\sigma}^2.
 \tag{E.16}
$$
不需要假设未知二次源自身具有w衰减。它的mean仍通过主体Green与true outer mean行确定。

## 5. 原已成源转入小正角宽，无旧积分重算

原moving residual及repair后的差都有完整标签支撑至96，即物理频率384。原L1 consumer的C、B、C_theta、B_theta和inverse displacement常数是在joint A_(1/64)支付。因此每个原row的physical ordinary源上界在(E.1)只增加
$$
 e^{384\sigma}=e^{3/64}<64/61<21/20 .
 \tag{E.17}
$$
在原已积分的每个正核前乘这个统一系数即可，不重新评价旧row或重复积分。这个步骤只用已知有限残差；未知物理解仍为无限Fourier。

[右端原完整物理矩](R133-supplement-final-moving-centre-actual-regular-boundary.md)的 F.11--F.16给所有j>128的解析尾。对有限|j|<=128，新增权至多
e^(512sigma)=e^(1/16)<16/15。尾另用同一个完整几何公式。原P<1.480385e-11、U<1.643190e-9、|m|>5.8及d>.124999999985给x=e^(-4(d-sigma))<2/3；J=128的完整C尾为8P*x^(J+1)*[(J+1)-Jx]/(|m|*(1-x)^2)，完整B尾为2U*x^(J+1)/(|m|*(1-x))。同时保两尾，合计小于1e-30。故旧真Robin行A0界1.256750e-15在A_sigma小于1.35e-15，旧Z的A_sigma小于3e-13。这里没有重算任何旧物理矩、alias或FFT。

真实long图的Green、regular multiplier与所有boundary lifts都逐频对角；A_sigma的指数权次乘性使原完整Banach-algebra proof逐项不变。真实holonomy小根的mean输出保持独立。原较小rZ=1e-12的value门因而仍可用于这同一个已知背景，给其d与c0的原完整小界。再积分原repair路径的A_(1/64)第一微分，宽取
$$
 \|Z_0\|_{A_\sigma}<3\,10^{-13},\quad
 \|r_D\|_{A_\sigma}<2\,10^{-15},\quad
 |r_{C0}|<2.05\,10^{-19},\quad r_{B0}=0.
 \tag{E.18}
$$
Bmean的最后等式只用当前反射类。含未知方向时所有普通mean列仍保。

连同(E.2)、原H_C<3/H_D<10及(E.3)，总已知负荷可统一宽取
$$
 \eta_\sigma<3.23\,10^{-7},\qquad
 e_\sigma<3\,10^{-14}.
 \tag{E.19}
$$
第一式含3||gamma||、ordinary pair、right d与Cmean；第二式含a_L||gamma||、ordinary端点和T_*r_D。Cmean不冒非mean端点源，也不从主体预算删除。

## 6. 真long域、完整外响应与明确闭集合

43692857656/1实际检查了同一个long图的barZ=1e-9、b=2^-60域及其mean/height列；完整原domain与image门均过。原逐模与代数论证在A_sigma中逐字成立。其真导数，包括原/当前regular multiplier差，给
$$
 T_Z<.006,\qquad
 \chi_{\rm lin+outer}<.879 .
 \tag{E.20}
$$
chi包含K_G max(||QB||,||QC||)、H_D T_Z及Cmean导数，且一般两mean合同不因反射读取而消失。固定f_B；其独立变化仍有原有序height列，不能以相同数代替外行Schur。

取
$$
 \rho=3\,10^{-6},\qquad \zeta=9.9\,10^{-10},\qquad
 {\cal B}=\{x\in X_\sigma:\|x\|\le\rho,\
                      \|c_{\ne0}(R)\|_{A_\sigma}\le\zeta\}.
 \tag{E.21}
$$
由(E.18)，||Z0||+zeta<barZ，因此整个闭集合中实际outer map都有定义；它不是先在一个非法大球使用图，再事后截断。右Cmean是图的真实输出，未知Bmean按所给反射保留其确切条件。

令mathcal T为原两端reference Green，施加准确known residual、linear Q、完整(E.15)以及
d(Z0+c_ne(R),fB)-d(Z0,fB)、c0的完整非线性差和原regular比较费。内C_ne数据是gamma；没有另加一个任意的内Cmean条件。此映射的主体预算为
$$
 \|\mathcal T x\|
 <3.23\,10^{-7}+.879\rho+208\rho^2<.99\rho,\qquad
 {\rm Lip}_{X_\sigma}\mathcal T<.879+416\rho<.881 .
 \tag{E.22}
$$
所有列只消费一次未闭reference核，未再次乘已闭resolvent。

真实R端则由(E.13)、(E.16)、(E.19)与T_*T_Z<1/200给
$$
 \|(\mathcal T x)_{C,\ne0}(R)\|_{A_\sigma}
 <3\,10^{-14}+10^{-4}\rho+65\rho^2+\zeta/200
                                      <.9\zeta .
 \tag{E.23}
$$
这是对整个mathcal B的端点保持式，确实含全部三类未知反馈。known ordinary端点的小量本身不被当作(E.23)的替代。

## 7. 系数门通过后的准确存在性结论

mathcal B是X_sigma中的非空闭集合，端点evaluation连续。若(E.12)实际通过，则(E.22)--(E.23)使mathcal T为其严格压缩自映射。因此有唯一完整全模帽曲率解W=What+x，满足指定内C_ne、真实nonlinear long曲率图与其even mean。其相对中心pair小于rho；原C的实负下界与||vc||<6rho保Gauss分母不为0。

对实对称数据取实对称解。所有源、边界图及完整Neumann分母在所述复参数小域上解析；同一均匀压缩的迭代给gamma、fB的解析依赖。在一个稍小角条带，角导数由Cauchy控制。实际总场满足原Codazzi等式；中心的分片残差与校正的对应项准确相消。因此真实target平滑的各处，径向导数由原等式恢复，原人工cubic接口不留下实际方程跳。此为正帽的有限阶乃至局部光滑读出，不替代全体接缝验证。

内端输出仍为B(L)、C0(L)、实际mean高度/flux及相位。moving读出使用真实C的平均值、primitive和inverse angle；不声称任意未知A0组合有免费同阶界。这里选择正sigma正是为了保留合法的较小条带读出。

远端的真实height标签方程、全负体与无限尾、两Gamma、nu Schur及四标点/held/reach几何仍须按原合同联立。尤其本帽存在性定理，即使(E.12)通过，也不单独完成这些全局门。目前新weighted门尚未运行，故本篇只登记完整解析条件与固定数值参数，未登记实际帽存在性。
