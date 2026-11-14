# R119 续篇：紧缩放包及整个中高频段的当前实际混频正型

2026-11-14，visible-exact / tail_connector。

**状态：已证明的实际压缩型。** 本篇把新高缩放曲线和紧缩放
三维相位图接到同一个当前非径向背景、同一个真实
$\Gamma^*(\mathbf a,\Omega)$。保留全部 Fourier 输出、两个 mean、
当前端图传播和 joint 两列。结果覆盖：

- 高缩放曲线的全部 $M^2/B\ge2^{4000}J^{40}$，
  直到已经付清的中高频分界 $T_j=2^{65664}J^2\delta_j^{-9}$；
- 三维图的每个明确紧缩放包
  $|\kappa-\kappa_0|\le\eta_*$，$1/4\le\kappa\le2^{4000}J^{40}$。

同一包内使用同一实际参数方向，全部实际交叉项一并估计。
这里仍不声称一个任意全网 near-kernel 已落入上述某一个包，
也不从压缩正型直接宣布全 source-to-label 逆。

关键重付是分开真实支集：两个原 $\Gamma$ metric bump 在
strict 内部，只用 $\mathcal F_1$；整个负窗的 hat 响应只需
较低的物理能量，使用 $\mathcal F_{5/2}$ 和根 $H^3$。
不把这两项都粗送进根 $H^4$ 后增加不必要的输入频率损失。

## 1. 当前允许族和真正可达的小球

取 $j\ge8193$，$J=j+5$、$\delta=\delta_j$，
$$
 a=\Delta/B=\delta^{3/2}/(8\sqrt6),\quad
 80<\Delta<3J,\quad B<2^7J\delta^{-3/2}.
 \tag{A.1}
$$
全部 profile 是新高曲线、紧三维图和可并存的低曲线所在同一
原 $C^4$ 球；总形状范数小于 $2^{-79}$。
根 germ、旧两个 $\Gamma$ bump 支集和固定外端未变。

本篇使用
$$
                         \mathcal X\le2^{-8388608}.
 \tag{A.2}
$$
这不是一个尚未进入的新假设：
[整负窗物理证明](R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md)
开头已经为同一 fixed-stop incoming 证明
$\mathcal X<16\|\mathbf a^{\rm inc}\|_{224}
 <16\,2^{-60000000}10^{-8}$。
原 full-profile graph 对本允许球统一，故实际输入严格进入 (A.2)。
以前的 $2^{-1048576}$ 仍是较大的可用球。

$\mathcal N=\mathcal N_{i|j}$ 始终为原完整六项邻胞和，保留两个
接缝因子，满足
$$
 \mathcal N<2^{-20010}
       2^{-(31867/256)(j-8193)},\quad
 P_j=2^{-42}\delta^{-231/128}.
 \tag{A.3}
$$
令 $n=4\mathcal N\mathcal X$。
所有比较均取同一个当前 $\Gamma$ 和同一个当前 radial profile；
不是把实际对象换回原始 quartic 或把背景响应冻结为零。

采用原 physical total-conormal 中心输入
$$
 Z_m=\left(\sqrt{k_m}\,u_m,\
 \frac{v_m-(1+Q(c))u_m/2}{\sqrt{k_m}}\right),\quad
 k_m=\sqrt{7m^2-16},\quad u=\sqrt{\mu_0}h,\quad v=\pi/\sqrt{\mu_0}.
 \tag{A.4}
$$
实际非径向第二槽不是 $u_t/\sqrt{k_m}$。
完整 $\mathscr H^s$ 包括两个波槽和独立 flux mean；
常高度按原准确 null 槽保留。

## 2. 全输入的较低能量，只使用根 H3

本节使用第70束 (P.6)--(P.15) 的实际 strict、根和变图恒等式。
这些原 Cauchy 门已由第55束对完整当前 profile 球重实例化；
根端图、全部输出及两 mean 都在其中。
对全频中心输入，不再提前用 $M^2\le B$。
原准确 shear 消去后，(P.8) 的逐 Fourier 比较成为
$$
 \|Y_c\|_{\mathcal F_{5/2}}^2
                     <2^{128}B^{3/2}\|Z\|_{\mathscr H^3}^2 .
 \tag{A.5}
$$
确实三个原平方权分别由
$\sqrt B\,M$、$M/\sqrt B+B^{3/2}/M$、
$\sqrt B/M$ 控制，再乘 $(1+M)^5$，只需 $(1+M)^6$。
完整 Wiener 乘子和 Peetre 比照原证明付全部有符号 lag；
没有截断输出，mean 也不套 $M^{-1}$。

strict Cauchy 仍是
$2^{1100}J^5\delta^{-10}$。
两个真实根的 (P.13) 各只从中心走一次 strict，
其 balanced $H^3$ 范数带 $\sqrt b$，物理重建 (P.15)
平方带另一 $b$。
原根界 $b^2<2^{38}J\delta^{-9/2}$ 与
$B^{3/2}<2^{11}J^{3/2}\delta^{-9/4}$
使根区 $\delta$ 费用为
$20+9/2+9/4=107/4$。
strict 重建 (P.9) 的费用为 $20+6+9/4=113/4$。
因此
$$
 \boxed{\quad
 \sup_{I_i}E_0(Y)
 <2^{7900}J^{16}\delta^{-29}\|Z\|_{\mathscr H^3}^2,\qquad
 E_0=\|u\|_{H^1}^2+Q\|u_\theta\|_2^2+\|v\|_2^2 .
 \quad}
 \tag{A.6}
$$
(P.14) 的径向基本定理仍在真实变图上使用
$U,U_\phi,U_\xi$，没有取消输出角导或令图为径向直线。
所有 mean 和物理腰尺度也沿 (P.4)--(P.15) 原样保留。

## 3. strict metric 源只需 F1

在整个 strict 部分，第45束
[完整密度传递](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
的 (S.16)、(S.21) 给
$R_H:\mathcal F_s\to H^{s+1}$，
而 $\zeta_d$ 的重建是同阶。
所以物理 $u\in H^2$、$v\in H^1$ 只需 $\mathcal F_1$。
实际一阶角乘子用 (S.10) 的剩余角宽支付，完整重建可取
$$
 \|u\|_{H^2}^2+(1+Q)\|u_\theta\|_{H^1}^2+\|v\|_{H^1}^2
          <2^{160}J^2\delta^{-6}\|Y\|_{\mathcal F_1}^2.
 \tag{A.7}
$$
这是 (P.9) 同一准确两行公式多取一个角导：
$q>1/16$、$|\ell_{0,t}|<2^{29}J\delta^{-3}$ 不变，
各实际角乘子的一阶 norm 仍由原宽2到1的系数界控制；
新增32 bits 覆盖完整乘积和。没有在这里使用根图。

与 (A.5) 同样的中心比较给
$\|Y_c\|_{\mathcal F_1}^2
 <2^{128}B^{3/2}\|Z\|_{\mathscr H^{3/2}}^2$。
于是
$$
 \boxed{\quad
 \sup_{\rm strict}E_1(Y)
 <2^{2600}J^{14}\delta^{-29}\|Z\|_{\mathscr H^2}^2,\quad
 E_1=\|u\|_{H^2}^2+(1+Q)\|u_\theta\|_{H^1}^2+\|v\|_{H^1}^2 .
 \quad}
 \tag{A.8}
$$
未放宽的 bits 小于2552、$\delta$ 幂为113/4，
$J$ 幂为27/2。
两个原 $\Gamma$ bump 和三个局部形状支集都在此 strict 区内；
它们不需要 (A.7) 以外的 root trace 费用。

## 4. 实际解与同点径向解的完整 strict 比较

还必须比较两个不同解，不能只用同一个 $Y$ 的系数差。
本节从同一 (A.4) 出发定义 actual 和 radial 两个解；
它们在各自真实密度标签中的初始转换也一并比较。

在控制中心，$Q\asymp B$、$|Q_t/Q|<B$。
由 (S.6)、(S.10) 和准确
$w_d=\sqrt{q/D}\,u$、
$\zeta_d=\sqrt{D/q}\{v+(\mu/\mu_0)
                   (\ell_t-d\ell_\theta)u/2\}$，
对 $s=1,2$ 有
$$
 \|Y_c^{\rm act}\|_{\mathcal F_s}+\|Y_c^0\|_{\mathcal F_s}
       <2^{65}B^{3/4}\|Z\|_{\mathscr H^{s+1/2}},
$$
$$
 \|Y_c^{\rm act}-Y_c^0\|_{\mathcal F_s}
       <2^{80}n B^{3/4}\|Z\|_{\mathscr H^{s+1/2}} .
 \tag{A.9}
$$
这里用当前 radial shear 先消去
$-(1+Q)u/2$，不是以 $Q$ 的最大值多乘一次条件数。
两 mean 由完整 $c,\alpha$ 行定义，所需角乘子保全卷积。

把两个特征流都从中心取 identity 初值。
原 (S.19)--(S.22)、(S.28)--(S.31) 对任意两个 strict 截面
给真实相对 interaction。先在第55束 (N.2)--(N.4) 的当前完整
$C^4$ 系数盒中重用 (S.10)--(S.22) 的逐项积分界
$\int\|\mathcal A_H-\mathcal A_0\|<2^{256}J^3\delta^{-5}n$。
interaction generator 必须同时乘两个当前参考 Cauchy 因子，故
$K_{\rm st}^2\int\|\mathcal A_H-\mathcal A_0\|
 <2^{2456}J^{13}\delta^{-25}n$。
加入邻胞与原规范转换后，可安全用
$$
 K_{\rm st}=2^{1100}J^5\delta^{-10},\qquad
 \eta<2^{2500}J^{13}\delta^{-25}n,\qquad
 \|U_H-U_0\|_{\mathcal F_s\to\mathcal F_s}
                          <2^{3602}J^{18}\delta^{-35}n .
 \tag{A.10}
$$
(A.2) 保证 $\eta<1/2$。
此处 $U_H$ 是拉回真实两特征流后的完整四态，
不是 physical 圆周上裸 pullback 的同阶小差。

由 (A.9)--(A.10)，标签态差小于
$2^{3670}J^{18}\delta^{-35}nB^{3/4}
                         \|Z\|_{\mathscr H^{s+1/2}}$。
恢复到原物理角时保留 (S.20) 的真实一阶损失：
$$
 \|(w_d,\zeta_d)_{\rm act}-(w_d,\zeta_d)_0\|_{H^2\oplus H^1}
 <2^{3700}J^{18}\delta^{-35}nB^{3/4}\|Z\|_{\mathscr H^{3/2}}
$$
$$
 \hspace{35mm}
 +2^{1300}J^6\delta^{-10}nB^{3/4}\|Z\|_{\mathscr H^{5/2}} .
 \tag{A.11}
$$
第一项用 $R_H$ 的一阶增益，第二项用
$R_H-R_0:\mathcal F_2\to H^2$ 和
$\mathcal D_S-\mathcal D_{S^0}:H^2\to H^1$。
真实角差的完整 $C^8$ 大小小于 $2^{40}Jn$。
因此 (A.11) 没有把一个裸角小位移当成同阶 operator 小量。

将物理重建 (A.7) 同时用于两个状态。
其 norm 及 actual-minus-radial 系数差分别可取
$2^{80}J\delta^{-3}$ 和 $2^{80}J\delta^{-3}n$，
由 (S.10) 的一阶角系数逐项给出。
于是以 $E_1^{1/2}$ 记对应的物理三项 norm，
$$
 \|Y^{\rm act}\|_{E_1}+\|Y^0\|_{E_1}
 <2^{1280}J^6\delta^{-13}B^{3/4}\|Z\|_{\mathscr H^{3/2}},
$$
$$
 \|Y^{\rm act}-Y^0\|_{E_1}
 <2^{3800}nB^{3/4}
 [J^{19}\delta^{-38}\|Z\|_{\mathscr H^{3/2}}
              +J^7\delta^{-13}\|Z\|_{\mathscr H^{5/2}}].
 \tag{A.12}
$$

第61束 (J.13)、(J.17)--(J.18) 的完整物理 kernel
不含 $Q$，并有同状态系数差 $2^{16}n\mathcal E_1$；
径向 kernel 的全部双线性项也由 $E_1$ norm 控制。
把 (A.12) 用于完整两个解差，安全地
$$
 |\mathcal K_{\rm act}(Y^{\rm act})-\mathcal K_0(Y^0)|
 <2^{5200}nB^{3/2}
 [J^{25}\delta^{-51}\|Z\|_{\mathscr H^{3/2}}^2
  +J^{13}\delta^{-26}
     \|Z\|_{\mathscr H^{3/2}}\|Z\|_{\mathscr H^{5/2}}].
 \tag{A.13}
$$
两状态的极化及所有频率交叉均在这一 Hilbert norm 估计中。

## 5. 四种实际误差的共同完整合同

取一条当前方向 $\Psi$，其三个真实支集位于原 strict 区内，
并满足
$$
 \|\Psi^{(l)}\|_\infty\le2\rho^{4-l},\quad
 \|\Psi^{(l)}\|_{L^1(dx)}\le4\rho^{5-l},\quad0\le l\le4,
 \qquad D\mathsf C(\Xi)[\Psi]=0 .
 \tag{A.14}
$$
高曲线和紧图当前方向均满足此式。径向参考
$v^0=D\bar\Gamma=0$；不是把 actual $D\Gamma^*$ 设为零。
同一当前点的72束 (F.17)--(F.23) 因而给
$$
 |e_i|_1<2^{1134}\mathcal W_i\mathcal XP_j\rho^5,\quad
 \|e\|_\infty<2^{161154}\mathcal XP_j\rho^5,\quad
 \mathcal W_i=J_i^4\delta_i^{-6}\mathcal N_i .
 \tag{A.15}
$$
其原 $r_a$ 列来自非零 $v^0,f^0$，这里准确为0。
whole-profile-ball gauged 响应仍给
$\widehat n^{\rm fixed}<2^{836}\mathcal N\mathcal XP_j\rho^5$；
全部参数背景响应小于
$2^{161218}\mathcal N\mathcal X^2P_j\rho^5$。
所有当前 KAM 平均行和第一密度相位行都按实际联合方程反演。

假设中心输入仅支持 $|m|\le U$，$U\ge4$；
这只限制输入，所有后续输出和 mean 不作投影。
(A.13) 用 $B^{3/2}<2^{11}J^{3/2}\delta^{-9/4}$、
$(1+U)^r<2^rU^r$，再乘真实
$\int|\Psi|dt\le4a\rho^5$，给直接项
$$
 E_{\rm dir}<
 2^{5402}\mathcal N\mathcal X\,a\rho^5
                 J^{30}\delta^{-54}U^4\|Z\|^2 .
 \tag{A.16}
$$
原 $\mathcal H_{\widehat z}$ 用70束 (P.18) 的
$2^{24}\widehat n E_0$ 估计，不把 $Q$ 错乘到通量项。
(A.6) 给整负窗的全部 fixed-parameter hat 项
$$
 E_{\rm hat}<
 2^{8800}\mathcal N\mathcal XP_j\rho^5
                 J^{16}\delta^{-29}U^6\|Z\|^2 .
 \tag{A.17}
$$
两个 $\Gamma$ metric bump 在 strict 内，
其幅度小于1，真实窗长度小于1。
(A.8)、(A.15) 给
$$
 E_{\Gamma,{\rm metric}}<
 2^{3900}\mathcal N\mathcal XP_j\rho^5
                 J^{18}\delta^{-35}U^4\|Z\|^2 .
 \tag{A.18}
$$
最后，全部 $\ell^\infty$ 参数反馈的背景项用 (A.6)，得到
$$
 E_{\Gamma,{\rm hat}}<
 2^{170000}\mathcal N\mathcal X^2P_j\rho^5
                 J^{16}\delta^{-29}U^6\|Z\|^2 .
 \tag{A.19}
$$
(A.16)--(A.19) 对相邻胞元使用完整 $\mathcal N_{i|j}$；
(A.18) 的20 bits 邻胞费用已包含，(A.19) 保留原全行
$2^{161154}$，没有只计当前层参数。

这四项均以当前实际解评价。
它们覆盖 local 非径向核、实际与同点径向解之差、整窗背景、
两个 metric 参数及所有其它层引起的背景响应；
没有把一个绝对小数直接称为相对谱隙。

## 6. 高缩放直到真实 delta^-9 分界

用已证明高曲线
$\rho_h=2^{-40}J^{-2}$、
$r_h=2^{-1000}\rho_h^{13}$。
对
$$
 M^2/B\ge2^{4000}J^{40},\qquad M\le U\le T_j,
 \quad T_j=2^{65664}J^2\delta^{-9},
$$
[高振荡篇](R119-supplement-exact-two-phase-curve-complete-oscillatory-generator.md)
(O.39) 在原物理中心波单位给整个曲线的径向下界
$$
 L_\alpha^0>d_h\|Z\|^2,\qquad
                    d_h=2^{-800}\rho_h^7 B\,U^{-3}.
 \tag{A.20}
$$
所有这些频率使用同一个当前 $\Psi_\alpha$，没有模式数因子。

把 (A.16)--(A.19) 分别除以 $d_h\|Z\|^2$。
保留 $a/B=a^2/\Delta<\delta^3$、$B^{-1}<\delta^{3/2}$，
$\rho_h^{-2}=2^{80}J^4$ 和 $P_j$，得到安全的四项
$$
 \begin{array}{ll}
 2^{467000}\mathcal N\mathcal XJ^{48}\delta^{-114},
 &2^{601000}\mathcal N\mathcal XJ^{38}\delta^{-111},\\
 2^{465000}\mathcal N\mathcal XJ^{36}\delta^{-99},
 &2^{762000}\mathcal N\mathcal X^2J^{38}\delta^{-111}.
 \end{array}
 \tag{A.21}
$$
例如第二项的未取整 $\delta$ 指数为
$29+81+231/128-3/2=110+39/128$；
第一项为 $54-3+63=114$。
最大的 $U^9$ 常数 $2^{590976}$ 也真实包含在601000中。

在 $j=8193$，$J<2^{14}$、
$\delta^{-1}<2^{8197}$，由 (A.2)--(A.3)，
四项都小于 $2^{-6000000}$。
其后每层衰减超过10 bits，因为
$31867/256-114>10$，且
$((j+6)/(j+5))^{64}<2^{1/4}$，仍有严格余量。
所以对当前实际全盒与实际 joint 参数，
$$
 \boxed{\quad
 \mathfrak G_\alpha(Z_{\rm high})>
             \frac{d_h}{2}\|Z_{\rm high}\|^2,\qquad
 \mathfrak G_{\theta_h}(Z_{\rm high})>
             \frac{r_hd_h}{2}\|Z_{\rm high}\|^2 .
 \quad}
 \tag{A.22}
$$
这是整个高缩放中心输入子空间的实际混频型，
两 Fourier 锥之间和同一锥内的交叉项都已付。
这里的高压缩空间不含 flux mean 输入；由真实解生成的低输出
和两个 mean 始终在 (A.6)、(A.13) 中。独立 mean 输入由低曲线
保留并支付，不被本压缩子空间的记号删除。

## 7. 紧缩放每个共同包的当前实际型

使用
[三维相位图](R119-supplement-compact-scaled-three-parameter-phase-chart.md)
的
$$
 L_*=1+2^{4000}J^{40},\quad
 \rho_m=2^{-2240}J^{-2}\Delta^{-11}L_*^{-10},
 \quad \sigma_*=2^{-2110}\Delta^{-5}L_*^{-4}\rho_m^9,
$$
$$
 R_*=2^{-2300}\Delta^{-5}L_*^{-5}\rho_m^{10},\qquad
 \eta_*=2^{-16}\sigma_*\rho_m^{-5}.
 \tag{A.23}
$$
在任意当前三维盒点，对
$|\kappa-\kappa_0|\le\eta_*$、
$\kappa,\kappa_0\in[1/4,2^{4000}J^{40}]$，
同一个方向 $v(\kappa_0)$ 的自然完整型由原 (N.30) 正定。
在未乘 $R_*/3$ 的 $q$ 方向单位中，(N.31)--(N.33) 给
$$
 L_{q,v}^0>d_m\|Z\|^2,\qquad
                    d_m=2^{-6}\Delta\sigma_*/(L_*\sqrt B).
 \tag{A.24}
$$
它对包内任意模式组合成立。

用 $\Delta<4J$、$L_*<2^{4001}J^{40}$，有
$$
 \frac{\rho_m^5}{d_m}
     =2^{2116}\Delta^4L_*^5\rho_m^{-4}\sqrt B
        <2^{192000}J^{1857}\delta^{-1},
$$
$$
                 U\le\sqrt{B\,2^{4000}J^{40}}
                         <2^{2004}J^{41/2}\delta^{-3/4}.
 \tag{A.25}
$$
这包括 $\rho_m^{-4}$ 的全部 $J,\Delta,L_*$ 幂。
四个实际误差 (A.16)--(A.19) 归一后分别小于
$$
 \begin{array}{ll}
 2^{207000}\mathcal N\mathcal XJ^{1969}\delta^{-57},
 &2^{214000}\mathcal N\mathcal XJ^{1996}\delta^{-37},\\
 2^{205000}\mathcal N\mathcal XJ^{1957}\delta^{-41},
 &2^{375000}\mathcal N\mathcal X^2J^{1996}\delta^{-37}.
 \end{array}
 \tag{A.26}
$$
首层各小于 $2^{-7000000}$；
其后 $((j+6)/(j+5))^{2000}<2^{1/2}$，
而 $31867/256-57-1/2>66$，故逐层至少衰减66 bits。

因此整个当前实际参数盒与 joint 参数上，
$$
 \boxed{\quad
 \mathfrak G_{q,v(\kappa_0)}(Z_{\rm packet})
               >\frac{d_m}{2}\|Z_{\rm packet}\|^2,\qquad
 \mathfrak G_{\theta,v(\kappa_0)}(Z_{\rm packet})
               >\frac{R_*d_m}{6}\|Z_{\rm packet}\|^2 .
 \quad}
 \tag{A.27}
$$
输入只要求其真实 $\kappa$ 位于这个包；
实际解的 Fourier 输出仍完全保留。
三维方向在整个盒上统一，并不是为当前某个解临时冻结背景。

## 8. 端口、原源和下一项全网消费

(A.22)、(A.27) 是原物理整负窗 crossing 的当前压缩正型。
两内根的 physical Green 配对仍按真实 height/total-flux
连续关系与正片 outward 符号相消。
principal 端角共轭的导数不能单独删除：
若 $U$、$V$ 真酉，
$\widetilde U=V^*UV$、$A=-iV^*V'$，则附加项是
$A-\widetilde U^*A\widetilde U$；
在 $r=(I-\widetilde U)x$ 上准确为
$2\operatorname{Re}\langle r,Ax\rangle-\langle r,Ar\rangle$。
它的 domain 和残差费用仍须随完整网络接入。

ordinary/weak 源继续是61束 (J.4)、(J.26) 的完整两行：
$$
 s=(-a_{\rm Jac}F^t,\
       g-\partial_\theta(F^\theta+dF^t)),\qquad
 \widehat s=D_{\Psi,\Gamma^*}s-\Psi_{\rm tot}\mathsf Bs .
$$
有源 Green 恒等式中的两个源 pairing 继续保留；
这里没有从齐次压缩正性制造一个 arbitrary-source Green。
粗 $F^t$ 不取径向导数，bare flux 的真实端迹仍由原 source
空间授予。两 mean 及全局唯一高度常数没有被投掉。
(A.6)、(A.8) 是齐次 Cauchy 能量合同，不能免费当成全网逆。

新的实际结果已经支付紧/高缩放包内的所有非径向交叉项，
并把原全参数响应放在同一个当前点。
仍须证明完整 near-kernel 的中心质量和频率定位，或通过完整
Schur/参数选择支付不同包之间及不同窗口的混合。
不能只拿每个包的 PSD 相加后将那些交叉块设为零。
原层权、完整外响应以及从原普通/weak 源回到全部标签的映射
也继续保留，外方程 $\mathcal F=0$ 尚未由本篇自行完成。

本篇为解析推导，没有新数值实验；复用的旧能量与 polynomial
源身份保持不变，未将任何未运行的门填写为通过。
