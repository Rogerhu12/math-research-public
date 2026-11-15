# R119 续篇：无限深源的完整 particular 二 jet 与真实坐标普通源逆

2026-11-15，visible-exact / tail_connector。

**状态：解析结论已证。** 本篇接
[强层衰减与齐次平端 C²](R119-supplement-strong-layer-decay-and-physical-flat-end-C2-reconstruction.md)
D.1--D.30。其完整根状态门不变；这里支付此前未包含的**胞内有源**
particular，给出一个明定的普通源空间，使全部无限深胞的源也可
消费完整逆和物理 $C^2$ 结论。

所有源都在同一 actual 背景和同一个 $\Gamma^*(a,\Omega)$ 上，
ordinary、两个 weak 分量、均值、端迹和 source 的真实图变换均保留。
混合根图中的源 norm 是本篇输入的实际坐标 norm；不由原
$L_t^2H_\theta^s$ 或只有径向连续性的解析角 norm 自动推出。

## 1. 完整物理单位和 classical 源条件

写原方程
$$
 \operatorname{div}(G\nabla h)=f-\operatorname{div}F,\qquad
 G=\mu\begin{pmatrix}1&-d\\-d&d^2-Qv^2\end{pmatrix}.
$$
沿用 D.18，令
$$
 H=\sqrt{\varepsilon_s/\rho}\,h,\quad
 \widetilde G=(\rho/\varepsilon_s)G,\quad
 \widetilde f=\sqrt{\rho/\varepsilon_s}\,f,\quad
 \widetilde F=\sqrt{\rho/\varepsilon_s}\,F .
 \tag{P.1}
$$
于是
$\operatorname{div}(\widetilde G\nabla H)
 =\widetilde f-\operatorname{div}\widetilde F$，
而实际归一化 total flux 是
$$
       \Pi=\widetilde\mu(H_t-dH_\theta)+\widetilde F^t .
 \tag{P.2}
$$
不能把 $\widetilde f$ 改成 $f$，也不能令 $\rho=\varepsilon_s=1$。

以下 classical 二 jet 结论要求每个有限片上的
$f-\partial_tF^t-\partial_\theta F^\theta$ 是连续函数，
且下文列出的角 norm有限。保留原子或只有弱可积源时，
原 U/D 的增广解仍采用 total flux 和单侧/BV迹；
本篇不称这样的函数为 $C^2$。
跨接缝另要求真实 raw 两迹及该 ordinary 分布密度相容，
使原方程给同一个第二径向迹。

定义直接可计算的 raw 源
$$
       \mathfrak r
        ={\widetilde f-\partial_t\widetilde F^t
                         -\partial_\theta\widetilde F^\theta
                         \over\widetilde\mu}.
 \tag{P.3}
$$
它仅用于本篇 classical 二 jet 的直接项。
网络源映射仍使用 total flux；没有把每个 weak 源都强行微分后
冒充原 weak 范数。

## 2. 真实根源、其两行和裸通量费用

使用实际根图 J.34--J.37，在每个负 collar 定义原 canonical 源
$$
 F_c=\alpha^{-1/2}(\mathfrak J^{-1}D\Psi F)\circ\Psi^{-1},
$$
$$
 f_c=\alpha^{-1/2}
 \left((f/\mathfrak J)\circ\Psi^{-1}
       -\tfrac12\nabla\log\alpha\cdot
                 [(\mathfrak J^{-1}D\Psi F)\circ\Psi^{-1}]\right).
 \tag{P.4}
$$
所有函数在右边的真实点上取值。
$u=\sqrt\alpha\,h\circ\Psi^{-1}$，故
$$
 u_{\xi\xi}-{\xi\over b^2}u_{\phi\phi}+Vu=r_c,\qquad
 r_c=f_c-\partial_\xi F_c^\xi-\partial_\phi F_c^\phi .
$$
第二状态是 $\pi_c=u_\xi+F_c^\xi$；
原平衡两行的准确 source 为
$$
 \mathcal E_c=
 \binom{-s^{1/2}F_c^\xi}
       {s^{-1/2}(f_c-\partial_\phi F_c^\phi)},
 \qquad s=(1+(|D_\phi|/b)^{4/3}+(|D_\phi|/b)^2\xi)^{1/2}.
 \tag{P.5}
$$
对每个负 collar 取
$$
 \mathfrak P_{\rm rt}
   =\|\mathcal E_c\|_{L^1_\xi H^9}
       +\|F_c^\xi\|_{C_\xi H^{10}}
       +\|r_c\|_{C_\xi H^6}.
 \tag{P.6}
$$
第一项是两行直和；包括完整 mean。
若原 root-wave 合同采用 bare 两行，另保其准确 affine vector
$\mathcal F_e(0)^{-1}(0,F_c^\xi|_e)$；
其中 $\mathcal F_e$ 是原完整 Airy 两列，不用一条高度列代替。
所有此类已定义的 total-to-bare 弱端向量的 $H^9$ norm之和记为
$\mathfrak T_j$。它们只依赖实际源和背景架，不依赖未知解。
正、负方向和 $\varsigma_e$ 仍按 J.38--J.40。

由 U.6 的同一有限 commutator 展开重付 J.28--J.29 的9阶窗，
完整角 multiplier 的小量仍由 U.8 控制。因此同空间 Duhamel 给
零初值 particular 的平衡两行不超过
$2^{2208}\|\mathcal E_c\|_{L^1H^9}$。
恢复 bare $u_\xi$ 时减 $F_c^\xi$，再由原方程读取 $u_{\xi\xi}$。
实际 Jacobian 与密度二 jet正是 D.24--D.25 的那些量。
因此根 collar 的新增物理二 jet至多
$$
          2^{8192}b^3q_e^{-1/2}\mathfrak P_{\rm rt}.
 \tag{P.7}
$$
本式不假设弱源第一行具有一个错误的 $s^{-1/2}$ 因子。

## 3. 根图到固定径向切口的准确 affine drive

这是两种 source 窗之间必须显式保留的一步。
在负 collar 的 canonical 坐标中把真实切口写成
$\xi=\zeta_1(\eta)$、$\phi=\eta$；
取原小图同伦 $\zeta(s,\eta)=(1-s)\xi_0+s\zeta_1(\eta)$。
各曲线均位于原已付非特征 collar，
$\xi_0/2<\zeta<2\xi_0$。记
$$
 c=\zeta/b^2,\quad
 a=1-c\zeta_\eta^2,\quad B=c\zeta_\eta,\quad l=\zeta_s,
 \qquad |a-1|<1/4 .
$$
所有 $f_c,F_c$ 在 $(\zeta(s,\eta),\eta)$ 上取值。
沿该曲线的**total** conormal 为
$$
 q=u_\xi+c\zeta_\eta u_\phi+F_c^\xi-\zeta_\eta F_c^\phi,
 \qquad F_s=F_c^\xi-\zeta_\eta F_c^\phi .
 \tag{P.8}
$$
真实 Piola 矩阵形式上为
$(a/l,B;B,-cl)$，但展开为演化后没有除 $l$：
$$
 \begin{split}
 u_s&={l\over a}(q-Bu_\eta)+E_1,\\
 q_s&=-\partial_\eta\left({Bl\over a}q
                 -{cl\over a}u_\eta\right)-lVu+E_2,\\
 E_1&=-{l\over a}F_s,\qquad
 E_2=lf_c-\partial_\eta\left(lF_c^\phi-{Bl\over a}F_s\right).
 \end{split}
 \tag{P.9}
$$
因为 $a+c\zeta_\eta^2=1$，下右系数
$-cl-B^2l/a$ 准确等于 $-cl/a$。
(P.9) 可以直接对 (P.8) 微分验证，因此在 $l=0$ 或变号处仍成立；
不把同伦误当作全域单调的二维坐标图。
ordinary 的 potential 项 $-lVu$ 和两个 mean 行全保。

取真实已拉回的输入 norm
$$
        \mathfrak P_{\rm gr}
           =\int_0^1(\|E_1(s)\|_{H^{10}}
                            +\|E_2(s)\|_{H^9})\,ds .
 \tag{P.10}
$$
原 graph 的完整固定波架在 $\xi\asymp1/64$ 上，
两非mean行只含 $|D|^{\pm1/2}$、密度和真实 shear；
全架及 mean 的额外参数费可放宽为 $2^{128}b$。
其实际同伦 propagator由原有序 graph 定理和 U 的有限角重付
控制，不乘一个裸低频 $b^{1/2}$ 假界。
于是 graph 新源至 fixed-label strict 状态可安全取
$2^{512}b^2\mathfrak P_{\rm gr}$。
原曲线上 total-to-bare 差是 $(0,F_s)$，其实际框内端向量也计入
$\mathfrak T_j$。全部 primitive mean均按原框单列。

(P.10) 是源沿真实小图的 norm，不是用 $L^1_\xi H^9$ 的值
猜测它。对仅径向可测的源，某条曲线上的值可能没有意义；
该情形只使用原弱解合同，不消费本节 classical 源门。

## 4. strict 的全部有源密度、两 mean 与 raw 二阶项

严格负段使用原准确
$$
 F_d=\Lambda^{-1/2}F,\qquad
 f_d=\Lambda^{-1/2}
                  (f-\tfrac12\nabla\log\Lambda\cdot F),
$$
$$
 \mathcal S_\sigma={\sigma f_d\over2}
  -\tfrac12\partial_\theta[(\nu+\sigma d)F_d^t+\sigma F_d^\theta].
 \tag{P.11}
$$
归一化 (P.1) 后这些密度源数值不变：
$\widetilde\Lambda^{-1/2}\widetilde F=\Lambda^{-1/2}F$，
普通修正也同样准确。
令
$$
 \mathfrak S_9=\int_I\left[
            \sum_\sigma\|\mathcal S_\sigma\|_{H^9}
                    +\|\nu F_d^t\|_{H^9}\right]dt ,
$$
$$
 \mathfrak P_{\rm st}
   =\mathfrak S_9+\|\nu F_d^t\|_{C_tH^6}
                         +\|\mathfrak r\|_{C_tH^4}.
 \tag{P.12}
$$
原固定标签演化的两个 mean仍是
$$
 \alpha'=\tfrac12\langle f_d-\kappa w_d\rangle,\qquad
 c'=-\alpha'\langle S_+-S_-\rangle
 +i\sum_\sigma\langle C_{S_\sigma}D_\theta^{-1}Z_\sigma'\rangle
                         -\langle\nu F_d^t\rangle .
 \tag{P.13}
$$
最后这一项没有被 ordinary 化或投掉。
完整 Duhamel 给新增 fixed-label 状态
$<2^{48}K_j^{\rm st}\mathfrak S_9$；
高度行准确是
$(w_d)_t=d(w_d)_\theta+\nu\zeta-\nu F_d^t$。

D.22 的 raw 二阶式现在只在右边增加 $\mathfrak r$。
因此 D.21--D.23 的同一有序恢复，加上 (P.12)，支付全部
$H,H_t,H_{tt}$ 与角 mixed jets；不再对密度中的 $Q_t/Q$
作第二次径向微分。
对于只满足原 S.35 的弱源，$H_t$、bare flux 或 $H_{tt}$ 所需
额外 sup/迹不由该积分 norm自动给出，故在 (P.12) 中另列。

## 5. 完整正段零迹 particular

在同一个实际正型分量，先使用 C.25 的真实 fixed-$t$ Piola
角图把 (P.1) 的源写成 $(\widehat f,\widehat F)$。
令 $\widetilde\mu_0$ 为归一化径向参考，
$R_I=\int_I\widetilde\mu_0^{-1}dt$。对零 Dirichlet 测试，
径向 Cauchy--Schwarz准确给
$\sup_t\|z(t)\|_2\le\sqrt{R_I}\|z\|_{\mathscr E_0}$，
包括 mean。因此定义
$$
 \mathfrak E_{+,6}
  =\sum_{q=0}^6\left[
       \sqrt{R_I}\|\partial_\eta^q\widehat f\|_{L_t^1L_\eta^2}
                 +\|\partial_\eta^q\widehat F\|_{\mathscr E_0^*}
                 \right],
$$
$$
 \|\widehat F\|_{\mathscr E_0^*}^2
   =\int_I\left\langle
       {|\widehat F^t|^2\over\widetilde\mu_0}
       +{|\widehat F^\eta|^2\over A\widetilde\mu_0}\right\rangle dt,
 \qquad
 \mathfrak P_+=m_j^{-1/2}\mathfrak E_{+,6}
                       +\|\mathfrak r\|_{C_tH^4}.
 \tag{P.14}
$$
根处 $A=0$ 的弱权确需可积。这里只有零迹 particular 的
Poincare，完整解的共同常高度仍由其真实根状态保留。

C.8 的整个双端 form 给零迹 particular 的六角导能量
$E_6^{1/2}<2^{128}\mathfrak E_{+,6}$。
具体将零迹解算子作宽 $1/16$ 的真实角平移族；同一复 form
coercivity 给其能量 norm小于2。至多6个角 commutator 各由
$2q!16^q$ 支付，Leibniz 的总二项式计数至多 $2^6$，
再加原正逆角图和六项直和的固定倍数，严格低于所写的 $2^{128}$。
可先对平滑源和有限 Fourier 证明，利用同一个 coercive form
闭包取极限；零迹能量唯一性明确排除添加一个常高度。

令 bare flux $p=\widetilde\mu(H_t-dH_\theta)$。
对 classical 源，准确有
$$
 p_t=\partial_\theta(d p-\widetilde\mu Av^2H_\theta)
                                +\widetilde\mu\mathfrak r.
 \tag{P.15}
$$
这与 total flux (P.2) 一致；它没有抹去 $F^t$。
重复 D.27--D.28 的“平均一条截面、再积分真实 flux”论证，
新增项为
$\int_I\|\widetilde\mu\mathfrak r\|_{H^4}dt$。
用 D.26 的长度、$\widetilde\mu_{\max}/\widetilde\mu_{\min}$
和同一角乘法费即可。随后 raw PDE只增加 $\mathfrak r$。
一个宽但已逐项支付的结论是
$$
 \|H_{\rm part}\|_{C^2_{r,\theta}(I)}
                          <2^{2048}J^2\delta_j^{-6}\mathfrak P_+ .
 \tag{P.16}
$$
mean source 的 total outward flux之和仍等于
$\int_I\langle\widetilde f\rangle dt$。
其高度 particular虽零迹，不能据此把两端 flux同时置零。

## 6. 全部无限深胞的 particular 及物理 C²

对第 $j$ 胞取其实际 finite cover：
负 root collars、root 到固定径向切口的小图、strict 段及完整
正型分量，并保留相邻两胞。定义已知源量
$$
 \mathfrak P_j=\mathfrak T_j+
  \sum_{\rm rt}\mathfrak P_{\rm rt}
  +\sum_{\rm gr}\mathfrak P_{\rm gr}
  +\sum_{\rm st}\mathfrak P_{\rm st}
  +\sum_+\mathfrak P_+ .
 \tag{P.17}
$$
这是有限个显式源 integral/sup/端迹之和，不含待求的 particular。
覆盖重叠处重复收取上界只会增大该数，实际源方程仍沿原有序
Duhamel/Poisson接线，不重新相加两个物理解。

从 root 强迫到 strict 初值，完整自由架、graph和一次 source
积分最多增加 $2^{4096}\lambda_j^2$。
之后 D.20 的 strict 倍数和物理 density 二 jet，最坏幂为
$$
                       2\cdot(9/4)+10+7/2+9/2=45/2<32 .
$$
strict内部的直接 source更小；(P.7)、(P.16) 也严格在同一幂内。
有限角转换、mean frames和所有覆盖的固定计数均被
$2^{131072}J^{12}$ 包含。因此完整局部解满足
$$
 \|H\|_{C^2_{r,\theta}(I_j)}
 <2^{131072}J^{12}\delta_j^{-32}
                        (A_j^{\rm in}+\mathfrak P_j).
 \tag{P.18}
$$
这一步不把两条半波解当作两个独立 source，也不把 weak 端荷
当作单位 Poisson 列。

令
$$
             \mathcal P=\|wF^{-2}\mathfrak P\|_{\ell^2(j\ge8193)} .
 \tag{P.19}
$$
若 D.3 的 $\mathcal G$ 与 (P.19) 均有限，则在各有限片的上述
classical/接缝条件下，
$$
 \boxed{\quad
 \|H-\lambda\|_{C^2_{r,\theta}(I_j)}
  <2^{1800000}J^{20}\delta_j^{22}(\mathcal G+\mathcal P).
 \quad}
 \tag{P.20}
$$
回原 ambient Cartesian 坐标，准确再乘
$2^8\sqrt{\rho/\varepsilon_s}\max(1,\rho^{-2})$，
同 D.30。该函数在平盘内延拓为相同物理常高度后为 $C^2$。
无源假设已在这里被明确的有源 norm取代。

## 7. 一个可直接消费的普通源空间：在实际图中声明范数

现在取真正 ordinary Darboux 源，
$$
                   f=w_{\rm ref}^2JD^{-3/2}e,\qquad F=0.
$$
原参考系数定义保持
$$
             N(t,\theta)={\mu_jp_*^2\over12r^{10}}\,e(t,\theta),
             \qquad \mu_j=\varepsilon_s m_j .
 \tag{P.21}
$$
$N$ 包含 mean；不是只保非zero Fourier 的有限前缀。

对每个胞元与相邻两胞，取以下真实 pullback：
原 fixed-$t$ 圆周、root 的 constant-$\xi$ 截面、
(P.8) 的实际小图同伦，以及正段 C.5 的 fixed-$t$ 角图。
令 $\mathfrak N_j^q$ 为这些 pullback 的
$\sup H^q$ norm之和。源必须给相应真实连续代表；
在混合 root 图上，这是实际 $N\circ\Psi^{-1}$ 的 norm。
定义
$$
 \mathcal S_{\rm at}
    =\sup_{j\ge129}{\delta_j^4\over\zeta_j}\,
                    \mathfrak N_j^{1026},\qquad
 \zeta_j=\begin{cases}
       \varepsilon_s\delta_j^{39/4},&j\le8192,\\
       \varepsilon_s\delta_{8192}^{-485/4}\delta_j^{131},
                                                   &j\ge8193 .
          \end{cases}
 \tag{P.22}
$$
它是一个完整具体源 norm，保留原 $\zeta$ 的真实接缝因子。
没有把原仅 fixed-$t$ 的 $\mathcal S_2$ 与它宣称等同。
当有实际 joint root producer时，可按该 producer直接核
(P.22)；缺此入口时，原 J.37 的混合图警示仍适用。

下面给出 (P.22) 到本篇两个必需源量的完整收费。
为了显示原物理尺度，记
$$
      C_{\rho,\varepsilon}=\rho+\varepsilon_s+
                                     2\sqrt{\rho\varepsilon_s}.
 \tag{P.23}
$$
此常数使用实际固定数值的原单位，不声称它尺度不变。

### 7.1 普通源的胞内 particular

令 $E_j$ 是同样实际图中的 $e$ 的 $\sup H^{10}$ norm之和。
原 $p_*\ge\delta/2$、$r\le2$，以及根处已付完整解析密度商，
给
$$
 E_j<2^{4096}{\zeta_j\over\varepsilon_s m_j}
                       \delta_j^{-6}\mathcal S_{\rm at}.
 \tag{P.24}
$$
这里只需10阶角乘法，actual根图中的 $p_*^{-2}$ 由 J.18、
J.22--J.25 的同一非零复域读取，未对一般源作复径向外推。

直接的 raw 源是
$$
 \mathfrak r=\sqrt{\varepsilon_s/\rho}\,
                a_{\rm phys}w_{\rm ref}e
             =\varepsilon_s\sqrt{\rho\varepsilon_s}\,
                         {m_jp_*\over r^6}\,e .
 \tag{P.25}
$$
strict 的密度 ordinary 源为原 S.37：
$a_{\rm phys}^{1/2}w_{\rm ref}^{3/2}J/(\sqrt qD)\,e$；
root 的 $f_c$ 还含准确的
$\mathfrak J^{-1}\alpha^{-1/2}$，故至多常数乘
$\varepsilon_s\sqrt{\rho\varepsilon_s}
 m_j^{3/2}p_*^{3/2}b^{-3/2}E_j$。
正段的零迹能量输入则由 (P.14) 和 D.26 支付。
用 $m_j<1$、$b>\delta_j^{-9/4}$、$q>1/16$，
以及各 strict 长度 $<4\delta_j$，全部可统一为
$$
 \mathfrak P_j
 <2^{4096}\varepsilon_s\sqrt{\rho\varepsilon_s}\,
                               m_j\delta_j^{-1}E_j
 <2^{8192}\sqrt{\rho\varepsilon_s}\,
                               \zeta_j\delta_j^{-7}\mathcal S_{\rm at}.
 \tag{P.26}
$$
ordinary 情形所有弱端向量为0；root 小图只剩 $E_2=lf_c$。

对 $j\ge8193$，乘 $wF^{-2}$ 后，全部深幂准确为
$\delta_j^{131-7-54}=\delta_j^{70}$。
第一深行的未缩减接缝费用是
$\delta_{8192}^{-485/4}\delta_{8193}^{70}
 =2^{-70}\delta_{8192}^{-205/4}<2^{420000}$；
以后平方和的比小于 $2^{-140}$。
因此
$$
             \mathcal P<
               2^{430000}\varepsilon_s
                         C_{\rho,\varepsilon}\mathcal S_{\rm at}.
 \tag{P.27}
$$
这里使用
$\sqrt{\rho\varepsilon_s}\le C_{\rho,\varepsilon}/2$。
没有删除巨大的 $\delta_{8192}^{-485/4}$ 全局因子。

### 7.2 普通源到完整根网络：先 full word，后 source Schur

原 ordinary source按 (P.4)、(P.9)、S.33和 C.25--C.33
进入各自完整两行。所有标签/角图和两端密度均是同一 actual 对象。
在 $H^{1025}$ 输出中，ordinary输入的 $H^{1026}$ 留足全部
primitive、半阶框及一次角导余量。

这里实际重付一次所用常数，不将 U 的声明范围悄悄改大：
U.6 的有限展开已到整数1030，完整 moments已到1088。
在本段最多使用1026阶；同样的三组 multiplier/角恢复各收
$B_*=2^{65536}$，径向 Fourier乘子仍准确交换。
完整负 word 任意剩余子乘积仍用
$2^{8192}\lambda^{12}$；root source换到其同一波架至多再收
$2^{128}\lambda$。反演 scattering 的 source行用真正
$B^{-1}$ 和 $DB^{-1}$，在这一同阶比较中 norm各小于2，
而不是再乘一个整个负段 Cauchy条件数。
strict ordinary source无额外角导，
root $f_c$ 的 $b^{-3/2}$ 因子原样保留。

正段 source用完整 C.28 的两个 mean和 C.29 的有序 resolvent。
可用
$C_I<2^{1024}(1+\sqrt{\rho/\varepsilon_s}\,
m_j^{-1/2}\delta_j^{-1})$、
$\Lambda_I<2^{1024}\sqrt{\rho/\varepsilon_s}\,
m_j^{-1/2}\delta_j^{-1}$；
实际 $f$ 与 $N$ 的准确关系为
$f=12\varepsilon_s m_jr^{-4}JD^{-3/2}N$。
长度 $<\delta^{3/2}$ 后，所得三个尺度项分别被
$\varepsilon_s$、$\sqrt{\rho\varepsilon_s}$、$\rho$ 支付。
再转完整 Airy框仍包含于下述宽界。
由这些有序公式，可对一个实际胞的全部原位根源取
$$
 \|\widehat g_j^{\rm body}\|_{H^{1025}}
       <2^{262144}J^{16}\delta_j^{-32}
                        C_{\rho,\varepsilon}\mathfrak N_j^{1026}.
 \tag{P.28}
$$
最大的参数幂由 $\lambda^{13}$ 给
$\delta^{-117/4}$，strict 源本身的最坏额外负幂为 $1/2$；
总和 $119/4<32$。其余 root/positive项更小。
主要 bits 为 $3\cdot65536+8192+13\cdot32$，
加显示的1024、128、mean和邻胞费用，严格低于262144；
$J^{13/2}$ 及源的有限 $J$ 因子被 $J^{16}$ 包含。
源的位置、两个输出和完整 mean保留，不是单列采样 bound。

将 (P.28) 代入 D.2 的两个真实 Poisson。
其全部层权合同给
$$
 \mathcal G_{\rm body}
 \le2^{1024}
 \left\|(v^{-1}F^2+wF^3)
               \|\widehat g_j^{\rm body}\|_{H^{1025}}\right\|_{\ell^2_j}.
 \tag{P.29}
$$
没有把消元后的源称作紧支，high仍需真实一次角导。
浅段 $\zeta=\varepsilon_s\delta^{39/4}$，
两权对应最坏负幂分别为
$79+32+4-39/4=105.25$ 和
$1073/32+10+32+4-39/4=69.78125$；
按所有 $j\le8192$ 直接收费，有限项数也保留。
深段两剩余正幂分别为16和 $1647/32$。
连原全局因子、全部 $J$ 幂和常数，较大的 $v^{-1}F^2$
分支在浅前缀末行及第一深行的 bits 都小于
$$
 262144+608192+1024+
 \left({485\over4}-{1647\over32}\right)8196
                  +14(4165+8+16)<1502000 .
$$
这里 $\delta_{8192}^{-1}<2^{8196}$，
$8192+5<2^{14}$，没有删除 $J^{4189}$。
另一 $wF^3$ 分支的账为
$$
       262144+12288+1024+
                    (485/4-16)8196+14(12+16)<1140000 .
$$
同样两个式子控制全部浅层，因为其最坏负幂正是上述
$105.25$ 和 $69.78125$，而 $J$ 在前缀上单调。
在深层，$J^{4189}$ 的相邻比小于2，
故两个分支分别至少有 $2^{-15}$、$2^{-50}$ 的几何衰减。
平方和、有限前缀的实际项数及邻胞计数全部包含后，
可以统一取
$$
 \boxed{\quad
       \mathcal G_{\rm body}
        <2^{1600000}\varepsilon_s
                           C_{\rho,\varepsilon}\mathcal S_{\rm at}.
 \quad}
 \tag{P.30}
$$
这里保留 (P.22) 的全部层权、真实 $\mu_j$ 的两段 profile及
$\delta_{8192}^{-485/4}$ 接缝因子；没有以一个纯深层幂
代替尚未到8193的有限前缀。

## 8. 可消费的完整 ordinary 结论及仍独立的列

对于 (P.22) 的 ordinary源，加上任意已付 D.3 的独立外源，
以 $\mathcal G_{\rm ext}$ 记外源费用。
真实通量兼容仍恰为
$\mathcal L_a k=0$，否则保 U/Z 的唯一辅助荷。
在指定物理高度 gauge下，(P.20)、(P.27)、(P.30) 给
$$
 \|H-\lambda\|_{C^2_{r,\theta}(I_j)}
 <2^{3400002}J^{20}\delta_j^{22}
 \left(\mathcal G_{\rm ext}
           +\varepsilon_s C_{\rho,\varepsilon}\mathcal S_{\rm at}\right).
 \tag{P.31}
$$
ambient高度二 jet仍再乘 D.30 的实际尺度。
它是整个无限深 ordinary源到真实平端 $C^2$ 的明确合同，
不只是对 root traces 的结论。

完整 weak/metric/两 $D\Gamma^*$ 列可直接使用 (P.3)--(P.20)；
必须提供其真实 tensor-to-scalar 源、图 pullback、weak端迹及
这些原位 norm。只有原 S.35/C.28 的弱可积性时，继续保 BV/单侧迹，
不增加未经证明的 classical 结论。
一般 metric 方向也不能用径向 C.50 替换非径向实际系数的导数。

(P.22) 的 mixed-root 输入仍需其自己的 producer。
它没有被改名成原 fixed-$t$ 的 $\mathcal S_2$ 或
$\ell^1_{224}$ 标签。因此当前全参数非线性迭代、原 analytic
标签空间中的逆、moving/full-$\delta$ 帽和 $\nu$/joint Schur
仍按各自真实范围继续联立；本篇没有以有限角阶代替这些要求。
全部新增费用来自显示的精确恒等式及完整旧核，无新增数值实验。
