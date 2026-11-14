# R119 续篇：真实外 Schur、完整弱源与无需标签反演的 Wronskian 外行

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 固定新强尾的实际零标签参考 $\Gamma^0$ 和它的同一个
全模好 bump。本文把内部带标签 Green 与真正外边界条件精确分开，并证明
外 affine Robin 源行不需要先反演极小的尾标签幅度。其真实线性长段给完整
$L$ 单位角增宽。普通源与两分量弱源都保留；弱源的径向导数通过总通量
准确移入状态，不被隐藏地计入一个 $L^1$ 源 norm。

在离散完整两行源的单位中，新增外行合同是

$$
 \boxed{\quad
 \|r(f)\|_{\dot A^1_{L+\beta-88823/400}}
       <2^{-390}\|f\|_{\mathcal F_\beta},\qquad \beta\ge0.
 \quad}                                                    \tag{E.1}
$$

对于下文准确归一的连续普通或弱源，右边可换成
$2^{60}\|\mathcal J\|_{\mathcal S_{1,\beta}}$。
这是实际外 affine functional 的全频定理，不把它称为同权内部边值逆。
那个不同的算子准确是 (E.24) 的 $\mathcal H D_0^{-1}E\mathcal G$。

## 1. 唯一参考对象及两个不应混淆的解算子

固定[强尾全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
及[真实 raw/source/Robin](R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md)
中的新 profile：8193 层后首剪切为 $2^{128}$、规范幂为131，两个全局
规范因子原样保留。参数取联合 KAM 的零标签值 $\Gamma^0$，bump 取在
这个值上重新选定的同一个 $t_0$。以下不把变化后的非径向背景当作此参考。

非mean离散状态及源为

$$
 X_{m,j-1}=A_{m,j}X_{m,j}+f_{m,j-1},\qquad
 X=\mathcal H a+\mathcal G f,
 \quad \ell(\mathcal H a)=a,\quad\ell(\mathcal G f)=0,
                                                               \tag{E.2}
$$

$$
 \|\mathcal H\|_{\ell^1_\beta\to\mathcal X_\beta}<9,
 \qquad \|\mathcal G\|_{\mathcal F_\beta\to\mathcal X_\beta}<2^{16}.
                                                               \tag{E.3}
$$

所有 $m\in4\mathbb Z\setminus\{0\}$ 的两行和所有层都在这些 norm 中；
仍先对径向取上确界，再对 Fourier 模求和。真正 mean 在第4节单独保留。
源为0时的 $\mathcal H$ 是真实平尾允许线，$\mathcal G$ 固定的是内部标签，
并没有固定外 Dirichlet 值。

## 2. 实际弱源的准确两行 canonical forcing

在 mixed tail 使用原实际坐标和单位

$$
 a=\rho r,\quad h=\rho H,\quad t=\log r,\quad y=\sqrt{12}t,
 \quad w=\mu_jp_*/r^7,\quad \mathfrak m=w/r.
                                                               \tag{E.4}
$$

本节 $h$ 是物理竖直 Jacobi 高度；$H$ 是其无量纲化。
具体采用 R74 的 $h=C=\delta Z$ 号数。若从非线性图的
$Z=Z_{\rm ref}-v$ 记号消费本篇，则 $h=-\delta v$，全部两行状态、
标签和源同时取负；线性 $\mathcal H,\mathcal G$ 及所有 norm 不变。
不只翻高度而保留原 flux 或源的号数。
固定整体符号，使源约定为

$$
 \partial_t(\mathfrak m H_t)
       +\partial_\theta(\mathfrak m A H_\theta)
       =s-\partial_t F^t-\partial_\theta F^\theta.
                                                               \tag{E.5}
$$

因此真正总通量为 $\pi=\mathfrak m H_t+F^t$。纯 ordinary 源的单位是
$s=w^2e$，与前篇完全一致。负号约定使 Green 公式的源泛函为
$\int sg+\int F\cdot\nabla g$，与实际 positive-DN 续篇一致。

对 $m\ne0$ 定义

$$
 \nu_m=\frac{m^2(m^2-1)}{12},\qquad
 k_m=\frac{m^2-4}{\sqrt{12}},\qquad
 c_j(r)=\frac{r^4}{\sqrt{12}\mu_j},\quad
 q_j(r)=\frac{r^4}{12\mu_j},
                                                               \tag{E.6}
$$

$$
 W_1=\nu_mH_m/r^4,\qquad
 W_2=\frac{p_*}{\sqrt{12}r^4}(H_{m,t}-m^2H_m),\qquad
 \widetilde W=(W_1,W_2+c_jF^t_m)^T.
                                                               \tag{E.7}
$$

这里 $c_j(r)$ 是显示的源换算函数，**不是** 胞元端点比例
$c_j^{\rm cell}\in\{64,16\sqrt2\}$。准确微分给

$$
 \boxed{\quad
 \widetilde W_y=
 \begin{pmatrix}k_m&\nu_m/p_*\\-p_*&-k_m\end{pmatrix}\widetilde W
 +\mathcal J_m,
 \quad
 \mathcal J_m=
 \binom{-\nu_m c_jF^t_m/p_*}
       {q_j\,[s_m-imF^\theta_m+m^2F^t_m]}.
 \quad}                                                     \tag{E.8}
$$

证明中唯一可能出现的径向导数准确相消：未移动的第二行源含
$-q_j\sqrt{12}(F^t_m)_y$，而移动总通量产生
$c_j(F^t_m)_y$，且 $c_j=\sqrt{12}q_j$。
剩下 $c_{j,y}+k_mc_j=m^2q_j$。第一行同时产生
$-\nu_mc_jF^t_m/p_*$，不能只保第二行。
当 $F=0$，第二行就是

$$
 q_js_m=\frac{\mu_jp_*^2}{12r^{10}}e_m=N_m,
                                                               \tag{E.9}
$$

恢复原 ordinary 源的两个 $p_*$ 因子。

采用前篇 $\mathcal S_{1,\beta}$，把其中 $|N_m|$ 替成
$\|\mathcal J_m\|_\infty$，即

$$
 \|\mathcal J\|_{\mathcal S_{1,\beta}}
 =\sum_{m\ne0}(1+|m|)^{312}\sup_{j>128}
 \frac{e^{|m|(\tau_{j-1}+\beta+\beta_j)}}{\zeta_{j-1}}
              \int_{I_j}\|\mathcal J_m(y)\|_\infty\,dy.
                                                               \tag{E.10}
$$

这个 norm 只含实际源与已知几何系数，不含未知解、未知 DN 或未知基本解。
实际新 profile 的完整内部正逆流界
$2^{450}(1+|m|)^{312}e^{|m|\beta_j}$ 对整个矩阵成立，因此 Duhamel 给

$$
 f_{m,j-1}=(-1)^{j-1}\zeta_{j-1}^{-1}e^{|m|\tau_{j-1}}
 D_j\int_{I_j}\Phi_{m,j}(y_+,s)\mathcal J_m(s)ds,
 \quad D_j=\operatorname{diag}(1,(c_j^{\rm cell})^{-1}),
                                                               \tag{E.11}
$$

$$
 \|f\|_{\mathcal F_\beta}
       \le2^{450}\|\mathcal J\|_{\mathcal S_{1,\beta}}.
                                                               \tag{E.12}
$$

在共同物理切口，总通量连续；$D_j$ 对总状态的第二行和原第二行作同一个
换算，因为 $c_jF^t=p_*F^t/(\sqrt{12}r^4\mathfrak m)$。
若源含明确的界面荷，先将它作为该切口总状态的实际跳量加入 (E.11)。
不能把有荷接缝当成无荷的连续状态。

## 3. Bare 状态、原标签和端点荷

在每个离散端点，把 $(0,c_jF^t_m)$ 用原 $(-1)^j\zeta_j^{-1}
e^{|m|\tau_j}$ 和实际端点换算变为 $Q_{m,j}$。于是准确有

$$
 \widetilde X=X^{\rm bare}+Q,\qquad
 a^{\rm tot}=a^{\rm bare}+\ell(Q),\qquad
 \|\ell(Q)\|_\beta\le2\|Q\|_{\mathcal X_\beta}.
                                                               \tag{E.13}
$$

最后一式使用真实特征基逆 norm 小于2。固定总标签为0的 particular 是
$\widetilde X^p=\mathcal Gf$；固定原 bare 标签为0时，则是
$\widetilde X^p=\mathcal Gf+\mathcal H\ell(Q)$，最后都要减 $Q$
恢复 bare 状态。两个定义只差一个真实齐次允许线。

下文源仅支持于 mixed tail，finite connector、双 bump 和 $[0,B]$ 无源；
因此 $F^t(B)=F^\theta(B)=0$，这些外部两迹的 total/bare 没有另一个端点差。
内部各端点的 (E.13) 始终保留。如果源延至外切口，必须另加该切口的
真实 weak 通量荷，不能从 (E.10) 这个径向 $L^1$ norm 猜一个端点迹界。

## 4. 全部 mean 及真正物理正则性

没有将 $m=0$ 代入不可逆的 $\nu_mH$ 状态。直接平均 (E.5) 得

$$
 \pi_0(t)=\int_{t_f}^{t}s_0(u)du,
 \qquad
 H_0(t)=\lambda+
       \int_{t_f}^{t}\frac r w\,[\pi_0(u)-F^t_0(u)]du.
                                                               \tag{E.14}
$$

这里采用平端真实总 flux 为0的分支；$\lambda$ 是唯一独立高度常数。
cut128 的总 flux 是第一式的输出，bare flux 是
$\pi_0-F^t_0$。如果额外需要零 holonomy flux，必须满足这一真实输出的
兼容条件，不能再把它自由置0。有限无源部分和长段继续积分同一个总 flux。
在物理高度单位，第二式乘 $\rho$；之后使用 $a/w$ 积分，故完整外高度为

$$
 h_0(0)=\rho\lambda+
 \rho\int_{t_f}^{t_e}\frac r w(\pi_0-F^t_0)dt
 +\pi_0(t_e)\int_{t_e}^{t_B}\frac a wdt
 +4\omega L\pi_0(t_e).
                                                               \tag{E.15}
$$

这些 mean 项不获得非mean的 $e^{-4L}$ 筛选。
ordinary 情形仍可直接消费前篇 (V.25) 的完整两个 mean 界。

对 weak 数据，(E.10)、$Q$ 的端点 norm 与 (E.14) 的实际收敛积分给全
弱解和 total/bare 两迹。它们自身不授予 $C^2$。如果需要该几何正则性，
还必须使实际有效 ordinary 源
$s-\partial_tF^t-\partial_\theta F^\theta$ 的
$N^{\rm eff}=q_j(s-\partial_tF^t-\partial_\theta F^\theta)$ 满足前篇
完整 $\mathcal S_1,\mathcal S_2$ 和接缝连续合同，再消费前篇 (V.17)。
因此本文没有以弱 $L^1$ 源偷偷替代二阶源或径向端点迹。

## 5. 真正外行的 Wronskian，不先求标签修正

先对有限 Fourier 源和有限胞元支持证明，随后取真实 Green 的极限。
这里不能声称有限胞元支持在径向 $\ell^\infty$ norm 中稠密。
原 $\mathcal G_0$ 的每个固定输出行是绝对可和的标量核；真实
$\mathcal G$ 是它与局部矩阵误差的 norm 收敛 Neumann 级数。
因此它的每个固定输出行仍为绝对可和核。截断径向源时，固定行由支配收敛
收敛到原 $\mathcal Gf$，而所有 norm 界一致；最后 Fourier 截断才使用
显示的 $\ell^1$ norm 收敛。这给下面实际外行的唯一指定延拓。
令 $q_m$ 为同一实际径向参考的平尾 regular 解，外端 grounded 归一为
$v(q_m;0)=1,p(q_m;0)=-\gamma_m^\ddagger$。
R74 的未改长段坐标是 $u\in[0,B]$，$L=\omega B$，
$Y=(y,y_u/M)$。前篇真实好 bump 的完整夹角给

$$
 \|Y(q_m;B)\|_2<2^{42}e^{-ML},\qquad M=|m|\ge4.
                                                               \tag{E.16}
$$

同一外 grounded 两迹与实际竖直高度的准确式是

$$
 v=A_0y-4y_u/M^2,\quad p=-y+4y_u/A_0,
 \quad h=4\omega y-4y_u/M^2,
 \quad p_h=(w/a)h_t=y-y_u/\omega.
                                                               \tag{E.17}
$$

这里 $t=\omega(B-u)$ 加同一个固定常数；$A_0$ 指当前长段的 R74 标量，
不与 Darboux 的 $A$ 混用。两组矩阵相对于 $(y,y_u)$ 的行列式分别为
$4(1-M^{-2})$ 与 $-4(1-M^{-2})$。因此完整符号为

$$
 r_m:=p_m(0)+\gamma_m^\ddagger v_m(0)
 =4(1-M^{-2})M\det(Y(q_m;B),Y^p_m(B))
 =-\big(h_qp_h-p_qh\big)(B).
                                                               \tag{E.18}
$$

给 particular 加任意齐次真允许线都不改变 (E.18)。这正是外 affine 列
不必先计算 $D_0^{-1}$ 的原因，不是删去 particular。

若保留全 continuous weak 源，令 $q_h$ 是 $q_m$ 的物理竖直高度。
物理 raw 系数为 $w/a$，其源仍是 (E.5) 的 $s,F$，因为
$h=\rho H$、$a=\rho r$。直接微分总通量 Wronskian 得

$$
 \frac d{dt}(q_h\pi-p_qh)
 =q_h(s_m-imF^\theta_m)+(q_h)_tF^t_m.
                                                               \tag{E.19}
$$

因此，存在下述绝对收敛积分时，同一准确外行也可写成

$$
 r_m=-\int_{\rm mixed\ tail}
   [q_hs_m-imq_hF^\theta_m+(q_h)_tF^t_m]dt.
                                                               \tag{E.20}
$$

平端 Wronskian 为0，原因是两个非mean场的实际平端高度/flux 极限，
不是对 source-free 公式作无端项的形式积分。内部荷需加其真实 Wronskian
跳量。若使用无量纲 $q_H=q_h/\rho$，(E.20) 右边必须整体乘 $\rho$。
对一般 (E.10) 输入，(E.20) 也可按上一段的真实 Green 行极限定义；
绝对收敛时与显示积分相等。没有把一个未证明收敛的积分当作定义。

## 6. 完整 $L$ 角增益的实际费用

设 $X^p=\mathcal Gf$。原 balanced finite connector 的线性两行估计只用
cut128 的两分量大小，不要求该向量属于齐次允许线。因此它同样给

$$
 \|(f_B^p,k_B^p)\|_{\mathfrak C_{s_\beta}}
 <2^{-447}\|X^p\|_{\mathcal X_\beta}
 <2^{-431}\|f\|_{\mathcal F_\beta},\qquad
 s_\beta=\beta-88823/400,
                                                               \tag{E.21}
$$

其中 $\mathfrak C_s=\sum_{m\ne0}e^{sM}
(M^2|f_m|+M|k_m|)$。线性传播逐模成立，所以 $s_\beta<0$ 时 (E.21)
仍是加权序列估计；这时不宣称整个 particular 在 finite connector 中
已定义一个分布场。下面的外 affine functional 仍由有限 Fourier 输入
和一致界合法闭延拓。实际 $\beta=224$ 则已有 $s_\beta=1.9425>0$，
没有这个分布范围问题。

真实全两迹变换还给
$\|Y^p(B)\|_2<a(B)^2(|f_B^p|+|k_B^p|/M)/8$，且 $a(B)^2<1$。
由 (E.16)--(E.18)，逐模准确得到

$$
 M|r_m|<2^{41}e^{-ML}
                    (M^2|f^p_{B,m}|+M|k^p_{B,m}|).
                                                               \tag{E.22}
$$

求和即得 (E.1)，然后 (E.12) 给 $2^{60}\|\mathcal J\|_{\mathcal S_{1,\beta}}$。
普通源直接令 $\mathcal J=(0,N)$。原 $\mathcal S_{1,2304}$ 是一个足够
支付内部外边值重建的输入档，计算此 affine functional 本身并不需要它。
全 $eta\ge0$ 时输出宽度仍为正，因为实际 $L>24514072$。

## 7. 内部真正外 Schur：精确公式与当前合法域

令 $T$ 是 cut128 到 $B$ 的同一完整 source-free 两迹传播，定义

$$
 E X=(k_B+\mathsf C_Lf_B)(X),\qquad
 \mathsf C_L=(M\coth(ML))_m,
 \qquad D_0=E\mathcal H.
                                                               \tag{E.23}
$$

真正零外 Dirichlet 条件是 $EX=0$。对每个有限 Fourier 源，唯一解是

$$
 \boxed{\quad
 X^{\rm reg}=\mathcal Gf-\mathcal H D_0^{-1}E\mathcal Gf,
 \qquad a^{\rm tot}=-D_0^{-1}E\mathcal Gf.
 \quad}                                                     \tag{E.24}
$$

若给定非zero外负荷 $g$，就在两式分别加
$\mathcal H D_0^{-1}g$ 和 $D_0^{-1}g$。weak 源的 bare 状态最后减 $Q$，
bare 标签再减 $\ell(Q)$；它们不是额外可以任意指定的边界值。

(E.24) 是真正 Schur 消元：将 (E.2) 代入 (E.23) 得到它，反向代入又
同时恢复所有内部两行和外条件。唯一性来自 $\ker E\cap\operatorname{ran}
\mathcal H=0$，即已证 $D_0$ 的全模可逆性。

现有付清的完整 Banach 合同如下。对 $\beta\ge0$，输入
$f\in\mathcal F_{\beta+2080}$，(E.21) 的输出宽为
$\beta+1857.9425$。因此与 $D_0^{-1}$ 所需宽 $\beta+1850$ 相差
$3177/400$。使用 $\coth(ML)<2$ 并在 $\mathfrak C$ 中保两行，可取
$\|E\mathcal Gf\|_{\mathfrak Z_{\beta+1857.9425}}
<2^{-430}\|f\|$；这里实际 $\coth(ML)<1+2^{-100}$，故系数2足够。
又

$$
 \frac1{16}e^{-4(3177/400)}<2^{-49},
$$

所以

$$
 \|a^{\rm tot}\|_\beta<2^{-479}\|f\|_{\mathcal F_{\beta+2080}},
 \qquad
 \|X^{\rm reg}\|_{\mathcal X_\beta}<2^{17}
                          \|f\|_{\mathcal F_{\beta+2080}}.
                                                               \tag{E.25}
$$

ordinary 的完整 $\mathcal S_{1,\beta+2080}$ 给右端
$2^{467}\|N\|_{\mathcal S_{1,\beta+2080}}$，随后按 $\mathcal S_2$ 得
真实 $C^2$ 平尾。weak 的同一陈述使用 (E.10)，并另付 (E.13) 的
$Q$ 与第4节完整 mean；全部实际 bare/source 边界行都保留。

在同一个权 $\beta$ 上，正确的定义域则是

$$
 \mathcal F^{\rm reg}_\beta=
 \{f\in\mathcal F_\beta:
             D_0^{-1}E\mathcal Gf\in\ell^1_\beta\},\qquad
 \|f\|_{\rm reg,\beta}=\|f\|_{\mathcal F_\beta}
                  +\|D_0^{-1}E\mathcal Gf\|_\beta.
                                                               \tag{E.26}
$$

在这个明确 graph norm 上，(E.24) 有界，小于 $2^{17}$。
这没有证明更新后的实际算子差把全部 $\mathcal X_\beta$ 映入 (E.26)。
恰恰必须支付的相对项是

$$
 D_0^{-1}E\mathcal G\,\delta\mathcal L_a,
                                                               \tag{E.27}
$$

加上已有的 $\mathcal G\delta\mathcal L_a$、真实参数/有限 connector/长段
列和完整 mean。外 affine functional (E.1) 的很强筛选不消掉 (E.27)。

## 8. 与正段 DN 网络的准确对应

在一个实际径向正段，令全 Cauchy transfer
$T=(\alpha,\beta_T;\gamma,\delta)$，$\det T=1$。
以同向 raw flux 写 Cauchy 残差

$$
 r_h=h_R-\alpha h_L-\beta_Tp_L,\qquad
 r_p=p_R-\gamma h_L-\delta p_L.
$$

以左外法向 $-p_L$、右外法向 $p_R$ 写参考 DN 残差 $q_L,q_R$，直接有

$$
 q_L=r_h/\beta_T,\qquad
 q_R=r_p-(\delta/\beta_T)r_h;
 \qquad r_h=\beta_Tq_L,\quad r_p=q_R+\delta q_L.
                                                               \tag{E.28}
$$

前篇的真实 Airy diagonal shear、full source 及所有端角变换都可以先做，
然后再按其真实两行换算回 (E.28)。这一恒等式说明为什么不能仅把正段
half-optical cross 的小 norm 代入内部 $\mathcal G$：$\beta_T$ 的剩余
指数费也必须付。mean 仍使用它自己的 $\beta_T=\int\mu^{-1}$，不以
高频渐近代替。下一步针对 (E.27) 的实际核继续，不将 (E.1) 或
(E.25) 宣称为已完成的非线性全网络逆。

## 9. 必要代数与数值检查

`scripts/fourfold_actual_exterior_Schur_Wronskian_20261113.py` 检查准确
weak 两行、total/bare 标签关系、两个真实两迹行列式、Wronskian 源号数、
DN/Cauchy 双向残差、输出宽和全部新数字费。
报告为 `notes/2026-11-13-R119-actual-exterior-Schur-Wronskian-budget.json`。
全频、闭延拓、物理 mean 与各算子定义域由上述证明给出。
