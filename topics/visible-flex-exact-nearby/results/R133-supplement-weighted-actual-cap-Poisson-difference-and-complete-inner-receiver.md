# R133：对称差恒等、径向加权源与实际帽内端 Poisson 差

2026-11-15。状态：完整解析接收式，待新小标量消费者作有向比较。本篇只消费原已成功的小结论与已证全模核，不重算原帽、残差、Riccati、Green 或 F 的成功算例。最终小于何阈值，必须以新公开运行的实际严格比较为准。

引用：
[I 全模实际帽比较](R133-supplement-actual-cap-inner-Poisson-perturbation-and-complete97-interface.md)，
[R 同一固定旧 reference 的全 height 球扩展](R133-supplement-actual-inner-cap-complete-tail-height-feedback-and-97-interface.md) R.13a--b，
[C 完整物理共轭](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)，
[L 局部三角 Hessian](R133-supplement-local-triangular-cap-Hessian-and-trial-source.md)，
[A 完整 global residual bridge](R133-supplement-actual-continuous-moving-cap-complete-residual-bridge.md)，
[RW 完整径向权重](R133-supplement-true-cap-local-receivers-and-radial-weighted-posterior-bounds.md)，
[RA 已成功的 RW 六组小结论](R133-supplement-actual-radial-weighted-cap-and-complete-left-receivers.md)。

## CP1. 一个固定 reference 与两个真实响应

帽区间仍是 $[L,R]=[9/10,25/8]$，固定 $\eta_0$、同一 ac1 连续修补440866中心、同一真实物理角和原 reflection sector：$B$ odd，$C$ even。固定原缓存使用的 $f_B^0$、$D_0$、$\mathcal H_0$ 以及 $\mathcal K_0$，不随当前帽输入重定义它们。

令实际帽为
$$
 W_*=\widehat W+x_*(\gamma,f_B),\qquad
 \|\gamma\|_{A^0_\theta}< r_\gamma=10^{-9},\qquad
 \|f_B\|_{\dot A^2_\theta}<2^{-60}.
 \tag{CP.1}
$$
实际值解由 M/R 原 product 域给出，$\|x_*\|_{\mathscr X_0}\le\rho=3\,10^{-6}$。新 $f_B$ 可与固定旧 $f_B^0$ 不同；R.13a--b 已准确保留这种比较的旧 residual Hessian 和完整外端差。

对任意物理 even nonmean 输入 $g\in L^2_\theta$，记
$$
 x_*^{\,g}=\mathcal K_*g,\qquad x_0^{\,g}=\mathcal K_0g,\qquad
 y=x_*^{\,g}-x_0^{\,g}.
 \tag{CP.2}
$$
I 的完整 Hilbert 模块是先各 Fourier 系数取径向 supremum、再取 $\ell^2$，两分量作 norm-sum，mean 权重为1。原已证
$$
 \|x_*^{\,g}\|_{\mathfrak M_\Sigma}<18\|g\|_2,\qquad
 \|x_0^{\,g}\|_{\mathfrak M_\Sigma}<14\|g\|_2,\qquad
 \|P_{\ne0}(x_*^{\,g})_C(R)\|_2<.009\|g\|_2.
 \tag{CP.3}
$$
其中旧界14直接来自 A §3 的13.367449；没有将局部 trial 当真列。

## CP2. 把旧 Hessian 留在旧列上的准确差恒等

以 $D_0$ 表示旧 physical bulk Jacobi；其完整旧 Robin/mean 行在下文另外写出。置
$$
 T_Q=D\mathcal R_Q(x_*),\qquad
 \mathcal Vq=(G\partial_\theta q,\beta q).
$$
$\mathcal R_Q$ 是 I.12 及其所引物理 Gauss 余项定理 A.18 的完整余项。两个真实列满足相应相同 inner 数据的方程，故准确相减得
$$
 \boxed{\quad
 D_0y=\mathcal V T_Qx_*^{\,g}-\mathcal H_0x_0^{\,g}.
 \quad}\tag{CP.4}
$$
与 I.20 相比，这是另一准确 resolvent 次序。它并未将 $\mathcal H_0$ 删除；它将这个非零旧源作用在已经给定的旧响应上。本篇后续使用的是 $D_0$ 的 physical receiver，因而不再外乘 $(1-\chi_H)^{-1}$。

记旧外导界、完整新旧差界为
$$
 L_D=6\,10^{-6},\quad L_m=10^{-6},\qquad
 \Delta_D=.006006,\quad \Delta_m=.000751.
 \tag{CP.5}
$$
它们都是 I.9--11/R.13 已付的完整算子上界，含真实 regular 比较费。$y$ 的右端源为
$$
 e_D^{\,y}=(D_Zd_*-D_Zd_0)P_{\ne0}(x_*^{\,g})_C(R),\qquad
 e_m^{\,y}=(D_Zc_{0,*}-D_Zc_{0,0})P_{\ne0}(x_*^{\,g})_C(R).
 \tag{CP.6}
$$
同时还保留旧反馈 $D_Zd_0P_{\ne0}y_C(R)$、$D_Zc_{0,0}P_{\ne0}y_C(R)$。inner nonmean $y_C(L)$ 准确为零；其 mean 是输出，不能设零。

## CP3. 只选一条已成功的径向权重

取 RA/RW 已实际计算的 $\kappa=1/2$ 行。为免与 Poisson 算子混淆，本篇将该参数记为 $\kappa_w$。令
$$
 w(r)=\exp\left(-\int_L^r\lambda_{\kappa_w}(s)\,ds\right),
 \qquad w(L)=1,\quad 0<w(r)\le1.
 \tag{CP.7}
$$
所有 source、kernel、endpoint 和值界都从同一行读取，不跨行拼接。先读取
$$
 K_A=K_{Q,\mathrm{nonmean}},\quad D_w=D_{Q,\mathrm{left}},\quad
 M_w=K_{Q,\mathrm{mean}},\quad H_D,\ H_C,\ w_R=w(R).
$$
RW 的 $K_{Q,\mathrm{complete}}=\max(K_A,M_w)$ 是 joint Wiener pair-sum 的常数；本篇不将它直接当成 Hilbert module 的两分量 norm-sum。

为给出所需的 Hilbert 界，保留原 positive-budget 算法的相关结构。RW 的 run 函数使用固定
$q_{\rm alg}=\max_i\operatorname{up}(q_{i,+})$，而其 left_receivers 输出
$q_L=\operatorname{up}(q_{0,+})$。同一已成小记录可核
$$
 q_{\rm alg}\ge q_L>q_-=1.3899,\qquad
 1+q_{\rm alg}\le H_C<2.39,\qquad q_{\rm alg}<q_+=1.39.
 \tag{CP.7a}
$$
这里前后两个不等式均来自这个**已知正预算参数**的生成式；不把实际 Riccati 函数的 upper 当作函数 lower，也不由一个独立 $H_C$ 算子上界反推 $q_{\rm alg}$。

在每个 inverse-frequency bin，原 weighted_kernel 使用非负
$$
 c_j=T_jD_j+C_j,\qquad
 k_j=D_j+(1+q_{\rm alg})c_j,\qquad
 b_j=D_j+q_{\rm alg}c_j=\frac{D_j+q_{\rm alg}k_j}{1+q_{\rm alg}}.
$$
已成 $K_A$ 支配全部 $k_j$，$D_w$ 支配全部 $D_j$。
令
$$
 \widetilde D=\min(D_w,K_A),\qquad
 \overline C=\frac{K_A}{1+q_-},\qquad
 \overline B=\frac{\widetilde D+q_+K_A}{1+q_+},\qquad
 K_w=\overline B+\max(\overline C,M_w).
 \tag{CP.7b}
$$
因为 $D_j\le k_j\le K_A$，$\widetilde D$ 仍是完整上界且
$\widetilde D\le K_A$。故 $(\widetilde D+qK_A)/(1+q)$ 关于 $q$ 单调不减，给 $b_j\le\overline B$、$c_j\le\overline C$。先各模/各径向位置用这两个**分别统一**的包络，再取 $\ell^2$ 和两分量之和，得
$$
 \|\mathcal G_w\mathcal Vq\|_{\mathfrak M_\Sigma}
 \le K_w\|wq\|_{\mathfrak M}.
 \tag{CP.7c}
$$
$C$ 的独立 mean 使用 $M_w$；$B$ mean 仅因原 reflection 为零。
这样不需要 $\sqrt2$ 费，也没有将逐模的 pair-sum 直接升级为 Hilbert pair-sum。新消费者必须先核 (CP.7a)，再计算 (CP.7b)。

完整 old $Q$ 线性乘法上界取 $q_0=.051432066$。定义
$$
 \chi_0=K_wq_0+H_DL_D+L_m .
 \tag{CP.8}
$$
这个式子只含旧 physical bulk 和旧外导；没有再加实际二阶余项或旧 Hessian feedback。其严格小于1必须用新的 Hilbert $K_w$ 独立比较；不能直接由原 Wiener posterior 的 $\chi_{\kappa_w}<1$ 代替。

RA 的同一完整 posterior 给
$$
 X_w^{\,*}:=\|w x_*\|_{\mathscr X_0}
 \le X_{w,\mathrm{affine}}+X_{w,\gamma}r_\gamma .
 \tag{CP.9}
$$
这里是实际非线性值解的 joint Wiener pair-sum。若另取较小 $\gamma$ 域，只能完整替换最后的 $r_\gamma$，不能删除 affine 项。

## CP4. 非线性系数差只对一个实际值因子加权

原 Gauss 分子是对称双线性型，norm 不超过2；$\|1/\widehat C\|<6$。在 $\|x_*\|\le\rho$ 上，完整 reciprocal 展开给
$$
 \|wT_Q u\|_{\mathfrak M}
 \le\left[\frac{24}{1-6\rho}
        +\frac{72\rho}{(1-6\rho)^2}\right]
                 \|wx_*\|_{\mathscr X_0}\|u\|_{\mathfrak M_\Sigma}
 <26X_w^{\,*}\|u\|_{\mathfrak M_\Sigma}.
 \tag{CP.10}
$$
第一项来自分子导数，第二项来自分母导数。$w$ 只给其中一个值因子；其余值因子用原 unweighted $\rho$。它不是将两个 weighted norms 相乘后遗失 $w^{-1}$。

由 (CP.3)，令
$$
                         a_Q=26\cdot18\,X_w^{\,*}.
 \tag{CP.11}
$$
则 $\|wT_Qx_*^{\,g}\|_{\mathfrak M}\le a_Q\|g\|_2$。完整 ordinary $C$ mean 同时保留在 $\mathcal V$ 中。

## CP5. 同一已成 positive budget 的逐项支配

在 RW source producer 的每个原闭行，定义其准确使用的非负预算
$$
 r_i^U=\operatorname{up}(\alpha\,\operatorname{up}R_{U,i}
                      +\varepsilon_{\rm repair}),\qquad
 r_i^V=\operatorname{up}(\alpha\,\operatorname{up}R_{V,i}
                      +\varepsilon_{\rm repair}).
 \tag{CP.12}
$$
这些控制同一 repaired moving residual 的完整 $A^0$；真实 $\alpha$ 已乘一次，完整 mean、原 primitive 及 repair 费均在内。

RW source a44357cfc1e8b5034a1daa587aff9bcaaf7d93ab 的 physical_source 函数先以其固定正参数 $c_{\rm alg},b_{\rm alg},c_{\theta,\rm alg},b_{\theta,\rm alg},E_{\rm comp}$ 形成
$$
 U_i=\operatorname{up}(E_{\rm comp}r_i^U),\quad
 V_i=\operatorname{up}(E_{\rm comp}r_i^V),
$$
$$
 F_{B,i}^+=\operatorname{up}
  \{c_{\rm alg}U_i+(b_{\rm alg}c_{\rm alg}
                    +b_{\theta,\rm alg}c_{\rm alg}/4)V_i\},
$$
$$
 F_{C,i}^+=\operatorname{up}
  \{(c_{\rm alg}^2+c_{\theta,\rm alg}c_{\rm alg}/4)V_i\}.
 \tag{CP.13}
$$
已成小记录中的同一算法参数满足
$c_{\rm alg}>5/16$、$E_{\rm comp}>4$。这两条是**正预算常数自身的下界**，不是实际函数振幅下界。因每步只向外取上端，逐行有
$$
 F_{B,i}^+\ge\frac54r_i^U,\qquad
 F_{C,i}^+\ge\frac{25}{64}r_i^V .
$$
RW 已按同一个真实正权及真交长完成积分，故令
$$
 U_w=\frac45F_{B,w}^+,\qquad
 V_w=\frac{64}{25}F_{C,w}^+,
 \tag{CP.14}
$$
即可控制 $\int_L^R w r^U\,dr$ 与 $\int_L^R w r^V\,dr$。
这里 $F_{B,w}^+,F_{C,w}^+$ 必须是那两个已成 positive-budget 字段的有向上端，不能用任意实际物理 source norm 代入 (CP.14)。本步是对原算法正加数的支配，不是从两个独立 norm 上界相除来反推未知源。它无需再读取或积分原1341行。

## CP6. 完整 Hessian 的 ordinary 源，含独立 mean

C.20/L.8--11 写作
$$
 \mathcal H_0x=\partial_\theta(-ex)+\mathcal O x,\qquad
 e=I_\theta(CR_v),\qquad
 \binom{\|(\mathcal O x)_B\|_2}{\|(\mathcal O x)_C\|_2}
 \le\begin{pmatrix}E_1+Z_{BB}&Z_{BC}\\0&E_1+Z_{CC}\end{pmatrix}
       \binom{\|x_B\|_2}{\|x_C\|_2}
 \tag{CP.15}
$$
的分量 norm 上界；这里未把真实算子 $\mathcal O$ 认作逐点常数矩阵。$-e x_\theta=\partial_\theta(-ex)+e_\theta x$ 已完整计入 $\mathcal O$。

原中心及其 repaired residual 的 Fourier degree 至多96；因此
$r_{U,1}\le385r^U,\ r_{V,1}\le385r^V$ 控制其完整 inhomogeneous $A^1$。用原已付界
$$
 C_*\le1/3,\ B_*\le1/128,\ C_1,B_1\le1/32,\quad
 V_*\le6,\ U_*\le1/50,\ J_*\le65/64,\quad H_2<38,\ H_C<.71
$$
代入 L.7--11，逐项有
$$
 \|(\mathcal O x)_B\|_2\le(418r^U+4r^V)\|x\|_{L^2\oplus_1L^2},\qquad
 \|(\mathcal O x)_C\|_2\le142r^V\|x\|_{L^2\oplus_1L^2}.
 \tag{CP.16}
$$
其中 $H_2<38$ 使用 C.17 已成37.594586，不由前述较宽 $V,C_1$ 再推。
证明的显式上界为：
$t_CV\le(2/3)r^V$，
$E_1\le(2/3)r^V$，
$Z_{BC}\le418r^U+4r^V$，
$Z_{CC}+E_1\le142r^V$；
这些由 $I_*=(1+65/64)/4$、$\pi<22/7$ 和 L.10 的正分项直接得出。第一行系数418与4同时支配其两输入列，不另收未知 Fourier 维数。

置
$$
 O_B=418U_w+4V_w,\qquad O_C=142V_w .
 \tag{CP.17}
$$
则对 $x=x_0^{\,g}$，两个完整 weighted ordinary $L^1_rL^2_\theta$ 源分别不超过 $14O_B\|g\|_2,14O_C\|g\|_2$。

本篇的全 joint transport 界取自 **A.5**：
$$
                         E_A=4.006101\,10^{-6}.
 \tag{CP.18}
$$
A 明确 $\|e\|_{\mathscr A_0}<E_A$；不能仅引用 L 表的 maximum_local_coefficients.EA 来得到这个全径向 joint 结论。因 $0<w\le1$，$\|we\|_{\mathscr A_0}\le E_A$，故两 divergence 势的模块 norm-sum 不超过 $14E_A\|g\|_2$。

mean 还可直接读准确恒等：
$$
 \langle(\mathcal H_0x)_C\rangle_\theta
 =2z_Rz_h/m^3=-2(z_R/m)\langle x_C\rangle_\theta .
 \tag{CP.19}
$$
这里 $z_R=\langle R_v\rangle_\phi$，$z_h=-m^2\langle x_C\rangle_\theta$。
$|m|>3$ 给该 mean 在 weighted ordinary 左端核下的费用
$(2/3)V_w\|x\|_{\mathfrak M_\Sigma}$。此式保留实际 mean；不是令它消失。$B$ mean 仅在本篇原 reflection sector 中准确为零。


## CP7. 同一个 weighted rotational Green 的普通与散度列

记原完整速率下界及全帽 $q$ 上界为
$$
 s_D^-=2.9252958741,\qquad s_C^-=.8601652212,\qquad q_+=1.39.
$$
只从同一 RW 行读取 $\lambda_+$，定义
$$
 d_-=s_D^--\lambda_+/4 .
 \tag{CP.20}
$$
新消费者必须核 $d_->0$。对所有 $M=4,8,\ldots$，
$A_D-\lambda\ge Md_-$，$A_C+\lambda\ge Ms_C^-$。
第二条没有免费加 $\lambda_-/4$：当 $M\to\infty$ 时 $\lambda/M\to0$。

令该行已成 ordinary 两列为
$$
 G_B=H_D,\qquad G_C=(q_{\rm old,+}H_D+H_C)_{\rm certified}.
$$
$G_C$ 直接读取原完整 positive-budget 值，不从另一个独立 upper 反解 $q_{\rm old,+}$。
同一个逐模核及 Minkowski 不等式给
$$
 \|\mathcal G_{w,\rm ord}(F_B,F_C)\|_{\mathfrak M_\Sigma}
 \le G_B\|F_B\|_{L^1_rL^2_\theta}
       +G_C\|F_C\|_{L^1_rL^2_\theta}.
 \tag{CP.21}
$$
证明仍使用同一个 $q_{\rm alg}$ 及 $T_*=\max_jT_j$。普通 $B$ 源的两分量逐模包络分别为
$1+q_{\rm alg}T_*$ 和 $T_*$；普通 $C$ 源的两分量包络是这对乘以 $q_{\rm alg}$ 后再加 $(q_{\rm alg},1)$。它们的和分别被原
$H_D=\operatorname{up}\max_j[1+(1+q_{\rm alg})T_j]$
及原 $G_C$ 支配。每个分量先取 $\sup_r|\int K F|$，再用 $\ell^2$ Minkowski，最后相加。右 $d_R$ 的两分量也正是第一对，因此下文继续使用 $H_D$ 不漏 module 费。独立 $C$ mean 的核不超过1，被第二分量中的1支配；原 reflection 的 $B$ mean 为零。故这里证明的是分别统一的 component kernel 界，不是从抽象 Wiener norm 转授 Hilbert norm。

同样，散度源的 $M$ 抵消 kernel mass：
$$
 G_{\partial B}=H_D/d_-,\qquad
 G_{\partial C}=q_+H_D/d_-+H_C/s_C^- .
 \tag{CP.22}
$$
divergence 的 physical mean 准确为零；独立 ordinary mean 仍在 (CP.21)。
由 (CP.15)--(CP.18)，完整旧 Hessian 源到 weighted body 的上界为
$$
 H_w=14\{E_A\max(G_{\partial B},G_{\partial C})
                        +G_BO_B+G_CO_C\}.
 \tag{CP.23}
$$
这里没有把每个 residual cell 的 $L^2$ supremum 冒成全 joint norm；
只有已付 global $E_A$ 用于 divergence，ordinary 项使用真 $L^1dr$。

## CP8. 先给完整 weighted 差场，再读真实左端

记 $z_*=.009$。对单位 $\|g\|_2=1$，由 (CP.4) 的原完整三角 Green，
$$
 \|wy\|_{\mathfrak M_\Sigma}
 \le\chi_0\|wy\|_{\mathfrak M_\Sigma}
          +K_w a_Q+H_w+w_R(H_D\Delta_D+\Delta_m)z_* .
$$
若 $\chi_0<1$，定义
$$
 \boxed{\quad
 Y_w=
 \frac{K_w a_Q+H_w+w_R(H_D\Delta_D+\Delta_m)z_*}{1-\chi_0}.
 \quad}\tag{CP.24}
$$
实际差场和端口已经存在；此式是其有条件后验估计。它没有以一个尚未证明的小差先假设新帽解存在，也没有重新执行原帽解。

左端使用 RW 已证 $H(L,t)=0$ 的准确核，而不是把整个 (CP.24) 直接当最终输出。由于 $y_{C,\ne0}(L)=0$，非零模 $y_B(L)$ 由单一 backward $d(L)$ 核给出。对加权 $Q$ 源，它和 $C$ mean 的完整 pair 接收系数可取
$$
                              D_w+M_w .
$$
对 Hessian ordinary 源，非零模 $B$ 收 $O_B+q_+O_C$；
$C$ mean 使用 (CP.19) 的独立 $(2/3)V_w$。
对两 divergence 势，$B(L)$ 收 $E_A\max(1,q_+)/d_-$；
mean 没有 divergence 输入。因此令
$$
 \boxed{\quad
 H_L=14\left\{
 \frac{q_+E_A}{d_-}+O_B+q_+O_C+\frac23V_w
 \right\}.
 \quad}\tag{CP.25}
$$
$q_+>1$ 只是本已知常数。该式没有再次乘 whole-body resolvent。

从同一 RW 小记录的原 unweighted 左端核读取 $e_D,e_m$：
它们分别控制右 $d_R$ 与右 $C$ mean 到左端的传播。全部 old outer feedback 和实际变化给最终
$$
 \boxed{\begin{aligned}
 \kappa_{\partial}={}&
 (D_w+M_w)(q_0Y_w+a_Q)+H_L\\
 &+\left(\frac{e_D}{w_R}L_D+\frac{e_m}{w_R}L_m\right)Y_w\\
 &+(e_D\Delta_D+e_m\Delta_m)z_* .
 \end{aligned}}\tag{CP.26}
$$
于是
$$
 \|(K_{B,*}-K_{B,0})g\|_{L^2_\theta}
       +|(K_{0,*}-K_{0,0})g|
 \le\kappa_{\partial}\|g\|_{L^2_\theta}.
 \tag{CP.27}
$$
(CP.26) 中 $e_D/w_R,e_m/w_R$ 必须用完整正球的 $w_R$ 下端计算，
不能拿 $w_R$ 的 upper 作除数。$D_w,M_w$、$\chi_0,Y_w$ 等上界参数使用有向 upper，$1-\chi_0$ 使用严格 positive lower。

(CP.27) 是 **inner $(B,C\text{ mean})$ pair 输出的算子界**。
它不把 $\kappa_{\partial}$ 冒为 $\mathcal K_*-\mathcal K_0$ 的 unweighted whole-body module norm。原 $1/5$ whole-body 结论继续保留；本篇另有 (CP.24) 的 weighted 差场界。

## CP9. 对原完整 97 行的合法用途

在原 Cdelta/F 固定 $S_\delta,H_{C,\delta}$ 坐标中，
$$
 \Delta B_{\rm actual}h=
 \left(-P_{\mathrm o,96}S_\delta
       (K_{B,*}-K_{B,0})P_{\ne0}H_{C,\delta}h_2,\
       -(K_{0,*}-K_{0,0})P_{\ne0}H_{C,\delta}h_2\right).
 \tag{CP.28}
$$
故已成同坐标的 full-input 系数 $c_{\rm cap}$ 给
$\|\Delta B_{\rm actual}\|\le c_{\rm cap}\kappa_\partial$。
这里直接需要 (CP.27) 的两个端口，因而不需要更强的 unweighted whole-body 差界。mean 输入、未知 high 输入、原 $\phi/\theta$ 换元和 projection 次序完整保留；无 $\sqrt{97}$ 维数因子，也不把 $H_C$ 输出误作物理有限97支撑。

F 已完成的 $\kappa=0$ comparison 支付 $\epsilon_{\rm coord}$。
新的完整 boundary fee 只能取
$$
 \epsilon_{\rm new}
 =\epsilon_{\rm coord}+c_{\rm cap}\kappa_\partial .
 \tag{CP.29}
$$
新消费者可只为这个新上界计算 F.7--10 的一套新矩阵和完整四列；旧 $\kappa=0$ 与 $1/5$ 的实际值、通过/失败记录必须原字复制，不重新计算或覆盖。若新矩阵任何充分门未过，照实保留数据，不作分母除法。F 的诊断 sufficient threshold 仅是另一可核比较，不替代 (CP.27) 的真实对象范围。

这个改善不支付 affine cap mismatch、非线性 boundary Taylor 余项、独立 $f_B$ 方向、waist 荷或未知 high/core 解差。NF 的固定 $S_\delta$ 接线保留它们。若实际 $\gamma$ 尚未被全局 matching 放入 (CP.1)，本篇不给它免费准入。原 low/shell 接收门与 core high-block 仍独立。

## CP10. 最小新公开消费的 exact fields

唯一有数值积分内容的输入是 RW 已成功完整 science：
目录 notes/radial_weighted_cap_receivers_ci/run-43729429382-1-radial-weighted-cap-receivers/，
文件 actual-radial-weighted-cap-receivers.json，
blob a4d46696df6125524d7491cd1d4efde156794aee，
57702 B，SHA256
ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9。

先核全部15原门、6个原候选语义、source/参数/输入身份。然后只用 new_weighted_candidates 的字符串键 1/2：

| 本篇量 | 完整字段路径 |
|---|---|
| $F_{B,w}^+,F_{C,w}^+$ | new_source_and_output_integrals.weighted_B_ordinary_L1 / weighted_C_ordinary_L1 |
| $w_R$ | new_source_and_output_integrals.weight_R |
| $K_A,D_w,M_w$ | complete_kernel_bounds.K_Q_nonmean / D_Q_left / K_Q_mean；$K_w$ 由 (CP.7b) 新计算 |
| $H_D,H_C,\lambda_+$ | complete_kernel_bounds.H_D / H_C / lambda_max |
| $G_B,G_C$ | complete_affine_and_feedback.ordinary_B_gain / ordinary_C_gain |
| $X_{w,\mathrm{affine}},X_{w,\gamma}$ | posterior_bounds.Xw_affine / Xw_gamma_gain |

此外使用顶层 new_left_ordinary_receivers 的 e_D/e_Cmean/q_L；q_L 与同一 weighted_kernel 的 H_C 一起核 (CP.7a)。
以及顶层 physical_source_constants_copied 的 C/composition 两个**算法正参数**。这些是字段名，不是重新计算请求。
原 process 为 blob df608c6a12fb193106fba64fb23fd7afad37de29，
16350 B，SHA256 daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6。
原 RW SCI 为 blob a44357cfc1e8b5034a1daa587aff9bcaaf7d93ab，
31066 B，SHA256 f8d97a14aa7c2ebac746a9732e7b9fd00bf939db95b2b610edcd47f22f9388bb；
其 physical_source/weight_integrals 的正预算语义是 (CP.12)--(CP.14) 的必要原证据。

F 的实际完整 execution 为 blob efb276148b5297f5418d3d55da1d7c1d78450483，
35578 B，SHA256 9c7710ec10d8826320ba6d1cdee204884728b224944d5eb181e7e00a0c257e10，
路径 notes/selected_parameter_finite193_scalar_feedback_ci/run-43737257903-1/execution.json。
它的完整 actual_scientific_receipt 是唯一旧 F 数值来源；原 cases 和完整原13输入身份必须绑定，不能换成仅转录的小数。

新科学只做 (CP.8)--(CP.29) 的有限有向标量运算。原1341/1346/949行、原目标、primitive、repair、Riccati、Green sweep、Poisson Gram、F旧两case的重算计数均为零。允许分别报告全 $\gamma$ 半径和 $r_\gamma/128$ 的完整新case，但不得跨case逐项取最小。新 actual 不预设通过。
