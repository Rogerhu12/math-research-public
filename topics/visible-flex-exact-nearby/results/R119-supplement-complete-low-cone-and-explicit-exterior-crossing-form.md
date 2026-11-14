# R119 续篇：共同方向的完整低锥及全部带外交叉费用

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 第73束的同一个实际 compact 方向同时控制
中心的全部 $4\le |m|\le\sqrt B/2$ 两迹和 flux mean，不再要求
输入处于一个 dyadic band。当前整个有限参数盒、真实
$\Gamma^*(\mathbf a,\Omega)$ 及其全部响应列均保留。物理常高度
仍是准确 null 槽。对任意完整中心数据，本文另外给出一个显式
带外负项，因而没有把未知的带外交叉项设零。

实际全网络近核若满足文末明确的中心定位不等式，则这一方向
对它严格为正；本文尚未证明所有全网络近核满足那个不等式。
所有源、principal 端图及其参数依赖继续保留，未由本篇宣布
完整外方程 $\mathcal F=0$ 已解。

## 1. 同一对象、原有限盒和完整中心空间

采用[第73束](R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md)
的当前真实对象，不改变原 $\zeta_j,h_j,b_m$、fixed-stop、
两个相位目标或可达标签球。记
$$
 j\ge8193,\quad J=j+5,\quad \delta=\delta_j,\quad
 a=\Delta/B=\delta^{3/2}/(8\sqrt6),\quad
 80<\Delta<3J,\quad B>2^{190},\quad
 \mathcal X\le2^{-1048576}.
 \tag{E.1}
$$
同一原未使用区间和共同方向是
$$
 \rho=2^{-1024}J^{-8},\qquad
 \psi=2^{-720}F^{9/2}\mathcal A_\phi^*
                         [-f_\rho'/\Delta-f_\rho].
 \tag{E.2}
$$
其中 $F,f_\rho,\mathcal A_\phi$ 全部按第73束 (M.1)--(M.4)
的完整有限 $e=1/B$ 定义，不能以 $e=0$ 的方向替换。
特别 $\psi$ 不依赖角频率，且两相位准确 annihilate，
$\|\psi^{(l)}\|_\infty\le\rho^{4-l}$、
$\|\psi^{(l)}\|_{L^1_x}\le2\rho^{5-l}$，$0\le l\le4$。

为指明实际参数盒，固定一个已经允许的 anchor band
$U_a/2\le M\le U_a$，满足
$$
 2^{-40}\delta^{-1/8}\le U_a/2,\qquad U_a^2\le B/4.
$$
仍采用原第68束的
$$
 \begin{split}
 d_a&=2^{-22050}U_a^{50}B^{-39}\Delta^{-103}
                                  (1+U_a^2/B)^{-96},\\
 r_a&=d_a/[2^{36}K^6(U_a+B)^2],\qquad
 K=2^{6000}J^8\delta^{-16},\\
 \Xi^{(n)}&=(r_a/N_a)\sum_{M\ {\rm in\ anchor}}\theta_M\psi,
                         \qquad |\theta_M|\le1 .
 \end{split}
 \tag{E.3}
$$
这些仍是原独立参数；没有以一个公共 band 坐标替代全网络的
单频条件化参数。本文的未缩放方向是 $\psi$，沿任意一个
$\theta_M$ 的结论准确再乘 $r_a/N_a$。

在共同中心 $c$，令 $\mu_0=w/r$、$u=\sqrt{\mu_0}h$、
$v=\pi/\sqrt{\mu_0}$，$\pi$ 是总通量。对所有 $m\ne0$ 定义
$$
 Z_m=\left(\sqrt{k_m}\,u_m,\
       \frac{v_m-(1+Q(c))u_m/2}{\sqrt{k_m}}\right),
       \qquad k_m=\sqrt{7m^2-16}.
 \tag{E.4}
$$
这是同物理角的两迹；对实际非径向解第二分量不是实际
$u_t/\sqrt{k_m}$。mean 取 $v_0=\pi_0/\sqrt{\mu_0(c)}$，
以 $h_0(c)=0$ 选取常高度商空间的代表元。独立常高度可在最后
准确加回。

全文 $H^s$ 使用 Fourier 权 $(1+|m|)^s$。令
$$
 \|Z\|_{\mathscr H^s}^2
 =|v_0|^2+\sum_{m\in4\mathbb Z\setminus\{0\}}
                               (1+|m|)^{2s}|Z_m|^2.
 \tag{E.5}
$$
这不是只量高度的 norm。令 $\Pi_j$ 保留 $v_0$ 和全部
$4\le|m|\le L_j:=\sqrt B/2$，记 $Z_< =\Pi_jZ$、
$Z_>=(I-\Pi_j)Z$。物理常高度无论频率投影如何都单独保留。

## 2. 从第四模开始的统一径向正性

第73束完整矩阵已经在整个
$16e\le\kappa=m^2/B\le1/4$ 证明
$C_e>2^{-48}\kappa^2I$。因此它直接适用于从 $m=4$ 开始的
每一真实非零模；这里不需要 $M\ge\widehat M_j$。
其真实密度、$dt$ 和中心 wave 换算给
$$
 L_\psi^0(m)>
 2^{-800}\rho^8\Delta^3m^5B^{-3}|Z_m|^2.
 \tag{E.6}
$$
mean 则单独有
$L_{\psi,0}^0>2^{-800}\rho^8\Delta^3B^{-1}|v_0|^2$。
故在整个中心低锥上，径向 Parseval 准确给
$$
 L_\psi^0>d_\ell\|Z_<\|_{\mathscr H^0}^2,\qquad
                  d_\ell=2^{-800}\rho^8\Delta^3B^{-3}.
 \tag{E.7}
$$
这是同一方向同时控制任意低模式组合，不是相加不同模式的方向。

原盒并未放大。由 $J<U_a^{1/64}$、$U_a\le\sqrt B/2$，
$$
 \frac{d_\ell}{d_a}
 \ge2^{13108}J^{-64}B^{11}\Delta^{106}>2^{13000}.
 \tag{E.8}
$$
对本锥的任意 $4\le M\le\sqrt B/2$，
$R_M=M+B/M<B$。第72束完整中心 Hessian
$\|D_\Xi L_\psi\|<2^{22}K^3R_M^2$ 在原半径 $r_a$ 上的变化
小于 $2^{-14}d_a$，对所有这些模式统一成立。
第72束辅助径向补偿路径准确终止于同一当前
$\Gamma^*(\mathbf a,\Omega)$；真实非零径向补偿
$|v^0|_1\le2r_a$ 保留。

mean 按真实积分
$L_{\psi,0}=\int\psi\,\mu_0(c)/\mu_0(t)\,dt$ 支付。
当前 compact 盒使其比值的相对变化小于 $4r_a$；
两补偿 bump 的 mean 贡献沿第73束整窗能量支付。
由 (E.8)，此前所有 $r_a/d_a$ 费用仍足够，故同点全盒径向型
大于 $d_\ell\|Z_<\|^2/2$。没有在每一模换一个参考参数点。

## 3. 真低锥的全部非径向交叉项

局部能量使用第69束的 $\mathcal N_{L_j,k}$，其比较频率取
$L_j$，而输出始终保留所有 Fourier 模。由于
$\Omega_{L_j}=B+L_j\sqrt B=3B/2$，中心低锥满足
$$
 \|Y_c\|_{\mathcal N_{L_j,k}}^2
             <2^8B\|Z_<\|_{\mathscr H^0}^2,\qquad0\le k\le3 .
 \tag{E.9}
$$
证明是对每一 $m\ge4$ 代入 (E.4)：$2M<k_m<3M$，
$|m|/L_j\le1$；高度、角梯度和完整 shear 后的通量三项分别
小于常数乘 $B/M+\sqrt B$。四个角导层求和用 $2^8$ 覆盖。
mean 代表元只有 $v_0$，同样满足此界。没有模式数因子。

第69束的完整 Fourier 能量和实际 Duhamel 差于是仍适用；
其源项中的径向参考输入满足全部 $|m|\le L_j$，因而
$BM^2/\Omega_{L_j}\le L_j\sqrt B$。角乘子仍用
$\ell^1*\ell^2\to\ell^2$，不对输出作频率投影。
实际直接 compact 型的差可取
$2^{112}a n B^2\rho^5\|Z_<\|^2$，其中
$n\le4\mathcal N_{i|j}\mathcal X$。

整个负窗包括两真实根。第70--73束的中心密度估计只用
$M\ge4$ 和 $M^2\le B$：在 $\mathcal F_{5/2}$ 中费用
$2^{128}B^{7/2}$，在 $\mathcal F_{7/2}$ 中费用
$2^{128}B^{9/2}$。逐 Fourier 项求和后同样成立。
因此所有输出、两个 mean、root 变图取值、physical normal
shear 原顺序保留，且
$$
 E_{\rm low}<2^{7840}J^{16}\delta^{-32}\|Z_<\|^2,\qquad
 E_{\rm strong}<2^{8440}J^{20}\delta^{-34}\|Z_<\|^2 .
 \tag{E.10}
$$
这里 $E_{\rm strong}$ 是实际
$\|u\|_{H^2}^2+(1+Q)\|u_\theta\|_{H^1}^2+\|v\|_{H^1}^2$。
仍只消费原 strict $7/2$ 和 root $H^4$ 闭窗。

当前联合参数导数完整分解为
$$
 \begin{split}
 e_i&=D_\psi\Gamma_i^*-v_i^0,\\
 |e_i|_1&<2^{1130}\mathcal W_i\mathcal XP_j\rho^5
                              +2^{280}\mathcal W_i\mathcal Xr_a,\\
 \|e\|_\infty&<2^{161150}\mathcal XP_j\rho^5
                                      +2^{160300}\mathcal Xr_a,
 \end{split}
 \tag{E.11}
$$
其中 $\mathcal W_i=J_i^4\delta_i^{-6}\mathcal N_i$、
$P_j=2^{-42}\delta^{-231/128}$。这些是第72束全行费用，
不是固定其它层参数的逐点公式。

新的准确归一比为
$$
 \frac{\rho^5}{d_\ell}
 =2^{3872}J^{24}a^{-3}
                     <2^{3887}J^{24}\delta^{-9/2}.
 \tag{E.12}
$$
将 (E.9)--(E.12) 代入第61束的准确型，四个完整误差相对于
$d_\ell\|Z_<\|^2$ 分别小于
$$
 \begin{array}{ll}
 2^{4400}\mathcal N_{i|j}\mathcal XJ^{28}\delta^{-8},
 &2^{13000}\mathcal N_{i|j}\mathcal XJ^{40}\delta^{-39},\\
 2^{14000}\mathcal N_{i|j}\mathcal XJ^{48}\delta^{-47},
 &2^{174000}\mathcal N_{i|j}\mathcal X^2J^{40}\delta^{-39}.
 \end{array}
 \tag{E.13}
$$
它们依次是局部全部混频差、完整固定参数 hat 响应、$e_i$ 的
metric 列和整个 $e$ 的背景列。例如第二项的真实指数为
$32+231/128+9/2<39$；第三项为
$34+6+231/128+9/2<47$。两者未取整 bits 为12541和13467。
第四项保留全参数 $2^{161150}$，未取整 bits 为172923。
直接项用 (E.9)，不用一个不存在的低输入有限输出假设。

四个 $r_a$ 列仍由 (E.8) 和第73束 (M.29) 给
$2^{-27000},2^{-28000},2^{-27000},2^{-1900000}$。
真实邻胞和
$$
 \mathcal N_{i|j}<2^{-20010}
         2^{-(31867/256)(j-8193)}
$$
保留两个原全局接缝因子。四项 (E.13) 首层对数分别小于
$-990000,-730000,-660000,-1590000$，以后层比的衰减指数大于77。
实际 incoming 原本已进入 (E.1)，没有另选一个不可达小球。

于是当前整个有限盒、同一个实际联合参数上的整窗型满足
$$
 \boxed{\quad
 \mathfrak G_\psi(Z_<)
 :=\int_{I_i}[\Psi_{\rm tot}\mathcal K_{\rm act}
                     -\mathcal H_{\widehat z_{\rm tot}}]dt
       >\frac{d_\ell}{4}\|Z_<\|_{\mathscr H^0}^2 .
 \quad}
 \tag{E.14}
$$
这包括任意不同低模式之间、两锥之间及与 flux mean 的实际
交叉项。常物理高度与任意场的型准确为0，因为核仅含
$h_\theta,\pi$；因此没有从物理空间删除高度 mean。

## 4. 全频中心数据的真实连续型

本节给出 (E.14) 之外全部高模式的明确费用。对任意完整
$Z\in\mathscr H^4$，第70束中心密度式仍可逐项使用，但不再
将 $M$ 替成 $\sqrt B$。径向主式为
$$
 w_d=\sqrt q\,u,\qquad
 \zeta_d=q^{-1/2}\left[\sqrt{k_m}(Z_m)_2+
                                    \frac{Q_t}{4Q}u_m\right].
 \tag{E.15}
$$
准确 shear 消去在先，随后才估计。因为 $q\asymp\sqrt B$、
$|Q_t/Q|<B$，非零模的三项原平方分别小于常数乘
$\sqrt B\,M$、$M/\sqrt B+B^{3/2}/M$ 和 $\sqrt B/M$。
再乘 $\mathcal F_{7/2}$ 的 $(1+M)^7$ 权，得到
$$
             \|Y_c\|_{\mathcal F_{7/2}}^2
                <2^{128}B^{3/2}\|Z\|_{\mathscr H^4}^2 .
 \tag{E.16}
$$
实际角乘子、两个 mean 和全部 lag 用第70束相同 Peetre 预算
支付。特别 (E.16) 所需的是两迹 wave norm $\mathscr H^4$；
它不是声称未平衡的 $h,\pi$ 各自只需 $H^4$。

将 (E.16) 送入已付 strict $7/2$、两根 balanced $H^4$ 和
实际 graph 的径向基本定理，可得
$$
 \sup_{I_i}E_{\rm strong}(t)
              <2^{8500}J^{16}\delta^{-30}
                                      \|Z\|_{\mathscr H^4}^2 .
 \tag{E.17}
$$
与第71束 (C.26) 相比，中心费用由 $B^{9/2}$ 变为 $B^{3/2}$，
所以根区和 strict 区的 $\delta$ 次数分别是
$107/4$、$113/4<30$；$J$ 次数至多 $27/2<16$。
新100 bits 覆盖所有全频求和和范数转换。没有增加任何所需的
输出角导或假设 canonical graph 为径向截面。

在当前实际小球，全部方向列还满足
$$
 \int_{I_i}|\Psi_{\rm tot}|\,dt<4\rho^5,\qquad
       \sup_{I_i}\widehat n_{\rm tot}<\rho^5 .
 \tag{E.18}
$$
这里必须包括径向补偿和所有参数响应。其详细足够界为
$$
 \frac{r_a}{\rho^5}<2^{-30916}J^{-8}\delta^{96},\qquad
 \frac{|e_i|_1}{\rho^5}
 <2^{1130}\mathcal W_i\mathcal XP_j+
                  2^{280}\mathcal W_i\mathcal X\frac{r_a}{\rho^5},
$$
$$
 \frac{\widehat n_{\rm tot}}{\rho^5}
 <2^{832}\mathcal N_{i|j}\mathcal XP_j+
 2^{64}\mathcal N_i\mathcal X
 \left[2\frac{r_a}{\rho^5}
      +2^{161150}\mathcal XP_j+
                   2^{160300}\mathcal X\frac{r_a}{\rho^5}\right].
 \tag{E.19}
$$
每个已用原 bump 的幅度小于1，直接 compact 积分
$2a\rho^5<\rho^5$；这些列的首层指数和深向衰减由新的预算
逐项支付。特别第二行保完整 $\ell^\infty$ 参数方向，没有只计
当前层的背景反馈。

第61束准确核满足
$|\mathcal K_{\rm act}|\le2^{40}E_{\rm strong}$、
$|\mathcal H_{\widehat z}|\le2^{24}\widehat nE_{\rm strong}$；
后式按第70束含 $Q$ 的物理能量读取，不在根处除 $Q$。
结合 $|I_i|<1$，得到整个 Hermitian 型的连续界
$$
       |\mathfrak G_\psi(Z)|
           \le C_j\|Z\|_{\mathscr H^4}^2,\qquad
       C_j=2^{8600}\rho^5J^{16}\delta^{-30}.
 \tag{E.20}
$$
先对光滑数据证明，再以 (E.17) 完备化。这同时给所有不同
频率与 mean 的双线性界
$$
 |\mathfrak G_\psi(Z,W)|
       \le C_j\|Z\|_{\mathscr H^4}\|W\|_{\mathscr H^4}.
 \tag{E.21}
$$
该结论由 Hermitian Riesz 表示和 (E.20) 直接给出，未用径向
Parseval 删除实际非对角核。

## 5. 全部带外分量的明确负项

因为 $1+\sqrt B/2<\sqrt B$，
$\|Z_<\|_{\mathscr H^4}\le B^2\|Z_<\|_{\mathscr H^0}$。
将实际型准确分成两个对角块和两个交叉块，用 (E.14)、
(E.20)--(E.21) 与一次 Young 不等式，得到
$$
 \mathfrak G_\psi(Z)
 \ge\frac{d_\ell}{8}\|Z_<\|_{\mathscr H^0}^2
                    -D_j\|Z_>\|_{\mathscr H^4}^2,
 \qquad
        D_j=2^{18200}\rho^2J^{36}\delta^{-71}.
 \tag{E.22}
$$
具体 $D_j$ 覆盖 $C_j+8C_j^2B^4/d_\ell$。第二项在放宽前是
$$
 2^{18003}\rho^2J^{32}\delta^{-60}B^7\Delta^{-3}
 <2^{18045}\rho^2J^{36}\delta^{-141/2}.
$$
所以 (E.22) 包含任意无限带外输入及其全部回填，未将它们
误认为平滑输入或齐次低频数据。

一个真正足够的中心定位条件是
$$
 \boxed{\quad
 \|Z_>\|_{\mathscr H^4}
 \le2^{-12600}J^{-42}\delta^{38}
                               \|Z_<\|_{\mathscr H^0}.
 \quad}
 \tag{E.23}
$$
在此条件下，(E.22) 直接给
$\mathfrak G_\psi(Z)\ge d_\ell\|Z_<\|^2/16$。
确实
$$
 \frac{d_\ell}{16D_j}
 >2^{-19019}\rho^6J^{-36}\delta^{151/2}
 >2^{-25200}J^{-84}\delta^{76},
 \tag{E.24}
$$
其中第一步保 $a^3=(8\sqrt6)^{-3}\delta^{9/2}$，第二步保
$\rho^6=2^{-6144}J^{-48}$。这给一个可实际比较的门，不是
“足够接近低频”的未定量说法。

## 6. 两端、源与尚须接入的实际门

所有中心数据沿同一个真实方程传到两个原物理截面。完整
height、total flux、两 mean、端角图、normal shear 和参数
导数按第59--61、70--73束的顺序保留。对 ordinary/weak 源，
准确输入依然是
$$
 s=(-a_{\rm Jac}F^t,\ g-\partial_\theta(F^\theta+dF^t)),\qquad
 \widehat s=D_{\psi,\Gamma^*}s-\Psi_{\rm tot}\mathsf Bs .
 \tag{E.25}
$$
没有 $F^t_t$，也没有由 $L^2$ weak 源自动得到裸通量两端的
$F^t$ 迹。物理均值满足
$\pi_{0,t}=g_0$、
$h_{0,t}=\langle dh_\theta+a_{\rm Jac}\pi-a_{\rm Jac}F^t\rangle$；
两个独立积分常数按原全网络合同保留。

本篇已把单个中心 band 扩大为整个低锥，并付清任意带外状态
的全部交叉费用。下一实际门是：在真实 physical principal
端图和完整正片反馈下，证明相关全网络近核的中心原像满足
(E.23)，或以另一个共同方向支付其不满足的部分。径向
$M^{1894}$ 端口逆本身不授予这个非径向定位。完整 source
原像及外方程 $\mathcal F$ 也不能由齐次 crossing form 删除。

新增有理预算及依赖身份：
[源码](../scripts/fourfold_complete_low_cone_exterior_form_20261114.py)、
[实际记录](../notes/2026-11-14-R119-complete-low-cone-exterior-form-budget.json)。
