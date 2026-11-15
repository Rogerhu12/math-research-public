# R133：全频帽的伴随后验与 high-to-97 方向 Gram

2026-11-15，visible-exact-astra-0df9 / newton_source。

**状态：证明了下述全频后验恒等式、误差合同及加权接线。**
尚未生成或认证本篇所需的伴随试验列，也没有本篇新的数值
high-to-97 常数。本篇不把既成 97 个正向列转置成伴随解，
不假定帽算子自伴，不宣称完整无限逆或参数 Schur 已闭合。

固定原 continuous repaired M32 中心、物理 $\eta_0$、
$\delta=0$，定义 SHA
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47。
完整区间为 $[L,R]=[9/10,25/8]$。只使用
[完整 moving 帽边界](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md)
(P.1)–(P.19) 的反射类、同一真实外图与完整 even mean；
原物理 Green 和 residual Hessian 的权限保持不变。

## 1. 完整输入、测度与伴随

所有角 $L^2$ 均使用归一化圆周测度；本文配对为真实 $L^2$
内积，复化时按标准共轭内积理解。$u$ odd，$v$ even，
$m=\langle v\rangle_\phi\ne0$。保持原完整函数算子

$$
 \Theta_\phi=v/m,\quad Vf=f\circ\phi,\quad Ug=g\circ\Theta,
 \quad\mathcal S=M_vU,\quad
 B=(u/v)\circ\phi,\quad C=(1/v)\circ\phi .
 \tag{A.1}
$$

直接换元而非有限矩阵转置给

$$
 V^*=M_{v/m}U,\qquad \mathcal S^*=mV .
 \tag{A.2}
$$

这里 $m$ 可以为负；不得用 $|m|$ 替换准确算子式。
设 $I_\theta=\partial_\theta^{-1}P_\perp$，
$I_\phi=\partial_\phi^{-1}P_\perp$，其全 $L^2$ 伴随为 $-I$。
完整端点微分为

$$
 H_B=-M_{BC}V-M_{B_\theta}I_\theta M_CV,\qquad
 H_C=-M_{C^2}V-M_{C_\theta}I_\theta M_CV .
 \tag{A.3}
$$

本篇的 $P_H$ 始终是全部 moving even $|j|\ge97$，
$P_{96}$ 是 odd $j=1,\ldots,96$ 的正交投影。低奇输入基为
$\sqrt2\sin(4j\phi)$，独立 mean 基为常数 1。
这给完整 97 维原 regular 行坐标，没有额外的径向权或
非mean 的 $\sqrt2$ 漏费。

令 $\widetilde{\mathcal K}$ 是真实 moving 帽解在 physical
变量中的完整 inner nonmean $C$ Poisson 算子。对任意
$c\in L^2_{{\rm even},\perp,\theta}$，写
$x=\widetilde{\mathcal K}c$，则

$$
 \|x\|_{\mathfrak M}\le\kappa\|c\|_2,\qquad
 \kappa=\frac{13.316116}{1-.003840162}.
 \tag{A.4}
$$

$\mathfrak M$ 仍是先逐 Fourier 系数取径向上确界、后取
$\ell^2$、两分量取 $\ell^1$ 的原模块。特别地

$$
 \sup_r\|x(r)\|_{L^2_{\rm pair}}\le\kappa\|c\|_2,\qquad
 \|x\|_{L^2_rL^2_{\rm pair}}\le\sqrt{R-L}\,\kappa\|c\|_2 .
 \tag{A.5}
$$

第二式只用于体积分；所有点迹另用第一式，不能反推。

## 2. 真 physical 方程及不求系数角导的伴随式

用原物理 Green 定义的乘法系数
$q_B=Q_B$、$q_C=Q_c$，$\ell=K/C_{\rm ref}^2$，
完整 physical 线性化的主体为

$$
 A_{\rm phys}\binom b c=
 \binom{-2\beta b+\gamma\partial_\theta(q_Bb+(q_C-\ell)c)}
       {\gamma\partial_\theta b+\beta q_Bb+
                         \beta(q_C-\ell-1)c}.
 \tag{A.6}
$$

$\beta,\gamma,\ell$ 仅依赖 $r$；$q_B,q_C$ 是真正完整 physical
角系数，不能用 Fourier 截断代替。对平滑反射试验 $z$，

$$
 \begin{aligned}
 (A_{\rm phys}^*z)_B
  &=-2\beta z_B-\gamma q_B z_{B,\theta}
                       -\gamma z_{C,\theta}+\beta q_Bz_C,\\
 (A_{\rm phys}^*z)_C
  &=-\gamma(q_C-\ell)z_{B,\theta}
                         +\beta(q_C-\ell-1)z_C .
 \end{aligned}
 \tag{A.7}
$$

(A.6) 的第一行本就是 divergence 排列，所以 (A.7)
没有额外 $q_{B,\theta}$ 或 $q_{C,\theta}$。
系数的完整 Fourier 余项仍乘试验的真实角导付清。

令 $\mathcal H_Rx=D^2\Psi[R,D\Psi^{-1}x]$，其中 $R$ 是该中心
的实际 residual。准确 moving-in-physical 算子与伴随是

$$
 \mathcal D=\partial_r-A_{\rm phys}-\mathcal H_R,\qquad
 \mathcal D^*=-\partial_r-A_{\rm phys}^*-\mathcal H_R^* .
 \tag{A.8}
$$

因而 $x=\widetilde{\mathcal K}c$ 满足 $\mathcal D x=0$。
不能因原中心 residual 小而删去 $\mathcal H_R$。

## 3. 伴随试验的完整分片恒等式

给定 $\lambda=(f,a)\in P_{96}L^2_{\rm odd,\phi}\oplus\mathbb R$，
令 $d=\mathcal S^*f=mVf$，目标泛函为

$$
 \Lambda_\lambda(x)
   =\langle d,x_B(L)\rangle_\theta+a\langle x_C(L)\rangle_\theta .
 \tag{A.9}
$$

取线性于 $\lambda$ 的任意分片 $C^1_r$、角光滑完整试验
$z_\lambda$。可取有限 Fourier 和分片径向多项式；它不是被
假定正确的伴随解。令

$$
 \zeta_\lambda=P_\perp z_{\lambda,C}(L),\quad
 e_{\lambda,L}=(z_{\lambda,B}(L)-d,\
                      \langle z_{\lambda,C}(L)\rangle-a),\quad
 r_\lambda^*=\mathcal D^*z_\lambda .
 \tag{A.10}
$$

所有内部径向节点保留准确的 $[z]_\rho=z(\rho+)-z(\rho-)$。
同一 physical 角中的 $x$ 连续，故逐片分部积分准确给

$$
 \begin{aligned}
 \Lambda_\lambda(x)
  ={}&-\langle\zeta_\lambda,c\rangle
      +\langle z_\lambda(R),x(R)\rangle
      +\int_L^R\langle r_\lambda^*,x\rangle\,dr\\
     &-\sum_\rho\langle[z_\lambda]_\rho,x(\rho)\rangle
      -\langle e_{\lambda,L},(x_B(L),\langle x_C(L)\rangle)\rangle .
 \end{aligned}
 \tag{A.11}
$$

证明是
$\partial_r\langle z,x\rangle=-\langle\mathcal D^*z,x\rangle$
以及每个节点的真实望远镜和。$C_0(L)$ 与 $a$ 完整保留。
因此 $-\zeta_\lambda$ 是完整输出 $(K_B,K_0)$ 的伴随作用
于 $(d,a)$ 的试验，不需要新伴随逆或 self-adjoint 性。

## 4. 真正外端 Robin 与 mean 费用

使用原相同参考外乘子 $Q_{\rm ref}$ 和
$J$（非零 Fourier 乘子 $i\,{\rm sgn}(k)$）。
零 affine 外源的真实完整图可写成

$$
 Jx_B(R)+Q_{\rm ref}x_{C,\perp}(R)
       =\Delta_Dx_{C,\perp}(R),\qquad
 \langle x_C(R)\rangle=\Delta_0x_{C,\perp}(R).
 \tag{A.12}
$$

其中 $\|\Delta_D\|\le L_D$、$\|\Delta_0\|\le L_0$ 使用原
完整非线性外图导数及正的参考比较费；原已付表达式是

$$
 L_D=5.898255\,10^{-6}+\epsilon_{\rm old}+2^{-512},
 \qquad L_0=7.372818\,10^{-7}.
 \tag{A.13}
$$

$\epsilon_{\rm old}>0$ 沿原证书保留，不置零。
$q_M$ 或其有限 dyadic proposal 的差异也必须在
$e_R$ 或新增准确比较费中保留。

因为 $J^*=-J$、$J^{-1}=-J$ 于非mean空间，
令 $z_{C,0}=\langle z_C\rangle$，

$$
 e_{\lambda,R}=
       P_\perp z_{\lambda,C}(R)-Q_{\rm ref}Jz_{\lambda,B}(R).
 \tag{A.14}
$$

则 (A.12) 给

$$
 |\langle z_\lambda(R),x(R)\rangle|
 \le\kappa\|c\|_2\{
      \|e_{\lambda,R}\|_2+
      L_D\|z_{\lambda,B}(R)\|_2+
      L_0|z_{\lambda,C,0}(R)|\}.
 \tag{A.15}
$$

even mean 的最后一项独立保留。反射只使 odd 的 $B_0$ 准确为零。
若数值试验选择 $z_{C,j}(R)-q_jz_{B,j}(R)=0$，这只是参考
Robin 行，不能代替 (A.13) 或真实 outer mean。

## 5. Hessian 的 ordinary 对偶源

原完整局部合同写
$\mathcal H_Rx=-e x_\theta+Zx$，$e=I_\theta(CR_2)$，并给
$E_\infty,E_1,Z_{BB},Z_{BC},Z_{CC}$ 的全模式界。形式伴随为

$$
 \mathcal H_R^*z=e z_\theta+e_\theta z+Z^*z .
 \tag{A.16}
$$

所以在每个真实局部胞元，

$$
 \begin{aligned}
 \|(\mathcal H_R^*z)_B\|_2
   &\le E_\infty\|z_{B,\theta}\|_2
                          +(E_1+Z_{BB})\|z_B\|_2,\\
 \|(\mathcal H_R^*z)_C\|_2
   &\le E_\infty\|z_{C,\theta}\|_2
                +Z_{BC}\|z_B\|_2+(E_1+Z_{CC})\|z_C\|_2 .
 \end{aligned}
 \tag{A.17}
$$

这里使用原 $Z$ 的真实 upper triangular block 结构，伴随后
对应的 block 上界转置；这是逐块算子范数事实，不是把原
有限帽输入矩阵转置成逆。由试验的实际 Fourier/径向多项式
积分，可把 (A.17) 作为完整 ordinary $L^2_rL^2$ 源包络。
所有 mean 保留；试验角导的 mean 精确为0。
不要求未知 $x$ 具有额外角导。

令 $r_{\lambda,0}^*=-z_\lambda'-A_{\rm phys}^*z_\lambda$，
可分别付 $\|r_{\lambda,0}^*\|_{L^2}$ 和
$\|\mathcal H_R^*z_\lambda\|_{L^2}$，不把二者视为正交源。
已有更窄的准确 Hessian divergence 分解若使用，必须完整
重写其伴随、所有 primitive/mean 和对应 source norm。

## 6. 保留全部 97 方向的误差 Gram

设以下 PSD 矩阵均由完整实际试验、准确参数域和全部输出
余项认证，对每个 $\lambda$ 有

$$
 \begin{aligned}
 \|e_{\lambda,L}\|_2^2&\le\lambda^*W_L\lambda,&
 \|e_{\lambda,R}\|_2^2&\le\lambda^*W_R\lambda,\\
 \|z_{\lambda,B}(R)\|_2^2&\le\lambda^*W_{RB}\lambda,&
 |z_{\lambda,C,0}(R)|^2&\le\lambda^*W_{R0}\lambda,\\
 \|r_{\lambda,0}^*\|_{L^2}^2&\le\lambda^*W_D\lambda,&
 \|\mathcal H_R^*z_\lambda\|_{L^2}^2&\le\lambda^*W_H\lambda,\\
 \|[z_\lambda]_\rho\|_2^2&\le\lambda^*W_\rho\lambda .
 \end{aligned}
 \tag{A.18}
$$

$W_D,W_H$ 含真实 $dr$，不能再重复乘局部格长。
令以下有限集合的每项完整保留：

$$
 \mathscr W=\{W_L,W_R,L_D^2W_{RB},L_0^2W_{R0},
                   (R-L)W_D,(R-L)W_H\}\cup\{W_\rho\}_\rho .
 \tag{A.19}
$$

对每个非零项选一个固定、严格正的准确数 $\alpha_T$，
置

$$
 W_{\rm err}
  =\kappa^2\left(\sum_{T\in\mathscr W}\alpha_T\right)
                       \sum_{T\in\mathscr W}T/\alpha_T .
 \tag{A.20}
$$

(A.4)–(A.5)、(A.11)、(A.15) 与加权 Cauchy 给

$$
 \|\, (K_B,K_0)^*(\mathcal S^*f,a)+\zeta_\lambda\,\|_2^2
                  \le\lambda^*W_{\rm err}\lambda .
 \tag{A.21}
$$

所有 jump 同时作用于同一个输入 $c$，因此必须使用 (A.20)
或更强的真实相关 Gram；不得把它们的误差平方当作独立源直接
相加。$\alpha_T$ 可依据实际矩阵上界选择，但选择后是固定
有向数，不依赖未知 $\lambda$ 或 $c$。Gram 的有符号非对角
元应保留到矩阵二次型/Loewner 运算之后。

## 7. 真 moving high-to-97 列的显式反向公式

由完整帽行 (P.14)，未知 moving high even 迹的低头负荷为

$$
 C_Hu_H=
 \binom{-P_{96}\mathcal E u_H}{-\mathcal M u_H},\quad
 \mathcal E=\mathcal S(H_B-K_BP_\perp H_C),\quad
 \mathcal M=-m^{-2}\Pi_0-K_0P_\perp H_C .
 \tag{A.22}
$$

因为 $\Pi_0u_H=0$，但不删除 $K_0$，
对 $\lambda=(f,a)$ 的伴随试验为

$$
 \widehat C_H^*\lambda
       =P_H\{-H_B^*\mathcal S^*f-H_C^*\zeta_\lambda\}.
 \tag{A.23}
$$

这可以准确改写成只用正向角图的表达式

$$
 \boxed{\quad
 \widehat C_H^*(f,a)=
 P_H I_\phi\left\{(u/v)f_\phi+
                  m^{-2}\big(z_{\lambda,C,\theta}(L)\circ\Theta\big)\right\}.
 \quad} \tag{A.24}
$$

证明：由 (A.2)–(A.3)，
$H_B^*=V^*(-BC+C I_\theta M_{B_\theta})$、
$H_C^*=V^*(-C^2+C I_\theta M_{C_\theta})$。
按 $\phi$ 求导得

$$
 \partial_\phi(-H_B^*\mathcal S^*f)=(u/v)f_\phi,\qquad
 \partial_\phi(H_C^*\zeta)=-m^{-2}U\zeta_\theta .
 \tag{A.25}
$$

这里两项本可分别多出
$\Theta_\phi\langle B_\theta Vf\rangle_\theta$ 与
$-(v/m^2)\langle C_\theta\zeta\rangle_\theta$。
本篇的 odd/even 反射使这两个被积函数准确 odd，故其 mean
准确为0。不能将 (A.25) 免费推广到任意未固定反射的全函数。
$\zeta=P_\perp z_C$ 的角导与 $z_C$ 相同，最后只有常数在
$P_H$ 下消去；独立 $a$ 始终通过完整 $z_C$ 保留。

因此完整 high 输出获得真正的积分因子

$$
 \|P_H I_\phi F\|_2\le\frac1{388}\|P_HF\|_2 .
 \tag{A.26}
$$

它只用于 (A.24) 的已知试验输出，不把未知 high 方向截断，
也不将帽的无限 mode coupling 变成主体 band64。
$z_C\circ\Theta$ 通常具有无限 Fourier 支撑，其完整解析
composition 尾必须认证；只有保存的有限数组不够。

## 8. 与实际低头 Poisson Gram 的接线

原全频 $H_C$ 的范数由 (P.9) 给 $\|H_C\|\le c_*$。
(A.21)–(A.23) 因而给

$$
 \|(C_H^*-\widehat C_H^*)\lambda\|_2^2
                      \le c_*^2\,\lambda^*W_{\rm err}\lambda .
 \tag{A.27}
$$

若 $W_T$ 是包括全部 composition/primitive/alias 尾的实际
试验 high 输出 Gram，
$\|\widehat C_H^*\lambda\|_2^2\le\lambda^*W_T\lambda$，
则对任意固定 $\tau>0$，

$$
 C_HC_H^*\preceq
 W_{\rm cap}:=(1+\tau)W_T+(1+\tau^{-1})c_*^2W_{\rm err}.
 \tag{A.28}
$$

这是完整无限 high 输入到原 97 行的 Loewner 上界，mean 行
保留。不是原 97 低输入矩阵的未授权反向使用。

现在令 $G_R$ 为真正有限193 BVP 的右端 Poisson 算子，
其同一个输出空间 $Y$ 已有实际 $G_R^*G_R\preceq H_Y$，
可来自
[完整97右端 Gram 合同](../notes/2026-11-15-R133-complete97-right-Poisson-Gram-contract.md)
的实际成功报告。则

$$
 \|G_RC_H\|^2
 \le\|H_Y^{1/2}W_{\rm cap}H_Y^{1/2}\|
 \le {\rm tr}(H_YW_{\rm cap}) .
 \tag{A.29}
$$

第一步用有界算子 $C_H$ 的极分解/非零奇异值等价与
$G_R^*G_R\preceq H_Y$；第二步只因两个矩阵 PSD。
准确平方根可由验证的 Cholesky/有理包络代替，或直接用
有符号矩阵乘积后的 trace 上界，不能先把各 entry 取模。

$Y$ 可以是全 inner-body $L^2$、固定完整负区 $L^2$ 或真
cut 点迹，必须使用对应的实际 $H_Y$，不能把体 $L^2$
当 trace。后续完整全频反馈仍须保留 high body 与 high cut
的独立输入、帽内完整 low head、negative high BVP 逆、
low-to-high 列及参数/背景转移。

## 9. 可审计的数值实现范围

后继数值工作可以构造 97 列新的 finite physical adjoint
试验，明确保存全部 257 状态（128 odd、even mean 和128
nonmean even）以及精确 dyadic 径向多项式；该维数只是试验
的存储选择，(A.18) 的 residual 输出及 (A.24) 的 high 输出
仍是完整全频对象。原 $Q_B,Q_c$ 全系数包络与 cached scalar
jets 可以原样复用；所有新的 proposal、residual 和 Gram
算术只在本公开仓库 Actions 执行。

原 finite 正向帽列不自动满足 (A.8)、(A.10)、(A.14)。
若复用它们作为任意试验，仍须支付这里全部实际缺陷；否则
另构造新的伴随列。每个原真节点和 jump、确切 $L=9/10$
入口（不是 binary64(.9)）以及真实外端都必须保留。
原中心/参数、原低头 Poisson 行单位与全 cap operator 的
身份由完整 SHA 清单绑定。

本文没有运行新的数值试验，没有新的已成 $W_T,W_{\rm err}$
或 $W_{\rm cap}$ 数值，更没有把 (A.29) 宣称为已小于1。
已证成果是完整准确伴随后验、反射类下的 (A.24)、全部
mean/source/端点费用及可消费的方向 Gram 合同。
