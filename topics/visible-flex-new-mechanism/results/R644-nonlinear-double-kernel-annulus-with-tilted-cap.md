# R644：投影曲率、真实倾斜帽与双核的准确非线性环带

2026-11-28。本文将 R629 的非线性矩、R639 的统一双核背景和 R642 的真实旋转尾参考逆放入同一个状态相关系统。**结论是一个真正非零的小幅准确等距环带：外帽逐点固定，内帽具有非零相对倾斜。** 在取得一个非零幅值后冻结其旋转度量，可作准确相位族。

本定理给正的局部幅值区间和非零整像运动；它没有把该局部区间量化为宏观角，也没有给出 README 所需的 $0.3D$ 和 $0.03D$ 下界。后续有限几何必须使用这里实际得到的嵌入，不能把二阶系数直接当作有限角。

## 1. 已支付的固定输入与记号

取 R642 所选的一个固定两端全平正 profile $w_*$，其区间为 $(a,b)\Subset(0,\infty)$。令

$$
L_*=(w_*\partial_r)'+(w_*'/r)\partial_\theta^2,
\qquad \Phi=f_2\cos2\theta+f_3\cos3\theta.
$$

两个 $f_j$ 是同一 $w_*$ 的准确自然全平核，按 R637/R639 的固定中心规范归一化。其二阶端口系数记为 $\beta_*>1/4$。

固定两个 compact 归一泛函 $\ell_2,\ell_3$，满足

$$
\ell_i(f_j\cos j\theta)=\delta_{ij},\qquad i,j\in\{2,3\}.
$$

它们和两条 profile 控制的支持均可放在一个固定正区 $I_*\Subset(a,b)$。R639 的两个真实紧支撑 profile 参数给族 $w_\mu$，$\mu=(\mu_2,\mu_3)$，在 $I_*$ 外准确等于 $w_*$，且

$$
\left(\int f_jL'_{j,w_*}[\partial_{\mu_i}w_\mu]f_j\,dr\right)_{j=2,3;i=2,3}
\quad\text{可逆}.                                     \tag{1}
$$

每个负曲率组件另取 Hu 物理坐标附录中实际构造的 $\chi_m$，支持严格离开根，规范为 $DT_m[\chi_m]=1$。取

$$
w_{\mu,\kappa}=w_\mu\exp\left(\sum_m\kappa_m\chi_m\right).
                                                               \tag{2}
$$

支持互不重叠，且与 $I_*$ 不交。所有简单根及其完整 germs 固定。每个负组件的参考角 $T_m$ 对全部整数 $j\ge1$ 满足

$$
|\sin(jT_m)|\ge\gamma_m/j,
\qquad \gamma_m^{-1}\le E_m^C.                         \tag{3}
$$

中心用 R639 的二次无理角，尾用 R642 重新选择的真实平尾。

本文用正坡 $h_w'=w$，且取外帽高度为零。与 R628 的负坡记号通过一次固定竖直反向相联，两个一阶核同时反号不改变交叉系数；下面的正倾角约定为 $z=h\cos\vartheta-r\cos\theta\sin\vartheta$。

所引用的分析输入限于已逐项给条件的引理：Hu 可读稿 [§3](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/03-linearization.tex) 的准确曲率/类型身份，[§10](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/10-tame-spaces.tex) 的带权 tame 空间，[§11](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/11-negative-components.tex) 的特征返回校正和固定根坐标，以及 [§12–13](https://github.com/Rogerhu12/math-research/blob/3871f5ce2dd5f4b221dd60a24211cb814f043b09/papers/flexible-surface-readable-4/13-volume-inverse.tex) 的正组件 graph 比较。原偶模单核非线性结论不作为本稿的前提。

## 2. 固定空间和真实帽图

### 2.1 反射空间及端点权

取 $\delta=3/4$ 为端点指数，以免与端口系数混淆。用 Hu 的完整径向坐标 $d\varrho=dr/\ell(r)$ 及权

$$
H=e^{-2x_\partial^3/3},\qquad
M=e^{1+x_\partial^{5/2}\log^2(e+x_\partial)},
\qquad x_\partial=\sqrt{\log(d_0/d_\partial)}.
$$

令 $X^0_\delta$ 为实、$2\pi$ 周期、关于 $\theta\mapsto-\theta$ 偶对称的全平空间，范数为

$$
\|v\|_s^2=
\sum_{i+j+k\le s}
\|M^k(\ell\partial_r)^i\partial_\theta^j(H^{-\delta}v)
                                    \|_{L^2(d\varrho d\theta)}^2.
                                                               \tag{4}
$$

不加 half-turn 条件。Hu §10 的 unit-cylinder Fourier retract 和 smoothing 与反射投影相容，去掉半周投影不改其证明。有限维直和、两个 compact 行的核、下面两个 compact 矩的核也都是 tame 直和因子。

控制空间 $K_\delta$ 是实序列的 $H_m^{-\delta}M_m^k$ 加权平方和；circle 空间 $Z_\delta$ 再包含角导数。底序列空间记为

$$
B_\delta=\ell^2(H_m^{-2\delta}).
$$

### 2.2 固定 cutoffs

在 $I_*$ 左侧的一个固定普通正区选两个 cutoffs $\chi,\chi_0$：整个左尾取一，整个右尾取零，其变化均位于该正区，且在 $I_*$ 上为零。该区与任何负组件不交。

令 $h_a=h_w(a)$，定义真实旋转参考

$$
z^{\rm ref}_{w,\vartheta}
=h_a+(h_w-h_a)\cos(\vartheta\chi)
                    -r\cos\theta\sin(\vartheta\chi),
$$
$$
\rho_{w,\vartheta}
=\cos(\vartheta\chi)+w\sin(\vartheta\chi)\cos\theta.
                                                               \tag{5}
$$

在完整左尾，(5) 是整个旋转背景的真实刚体转动；在右尾为原背景。只在固定正 cutoff 区有额外残差。

外参数为 $q$；未知量为

$$
x=(v,A,B,\mu,\kappa,h_L),
\quad
\ell_2v=\ell_3v=1,
\quad A,B\in\mathbb R,
$$

其中每个 $h_{L,m}$ 是递增的奇 lift，满足 $h_L(\theta+2\pi)=h_L(\theta)+2\pi$，且 $h_L-\mathrm{id}\in (Z_\delta)_{\rm odd}$。物理倾角为

$$
\vartheta=qB.
$$

实际高度图为

$$
\boxed{z=z^{\rm ref}_{w,qB}
             +q\rho_{w,qB}v+qA\chi_0,
\qquad w=w_{\mu,\kappa}.}                             \tag{6}
$$

其内帽准确为平面

$$
z=h_a+qA-r\cos\theta\sin(qB),
$$

外帽准确为高度零。由于 $v$ 全平，所有 jets 与两条真实帽一致；没有把慢于 $H^\delta$ 的旋转项放入 $v$。

初始状态为

$$
q=0,\quad x_*=(\Phi,0,0,0,0,\mathrm{id}).              \tag{7}
$$

取固定低阶位移范数

$$
\mathfrak n_s=|q|+\|v-\Phi\|_s+|A|+|B|+|\mu|
                       +\|\kappa\|_{K_\delta,s}
                       +\|h_L-\mathrm{id}\|_{Z_\delta,s}.
                                                               \tag{8}
$$

以后只在一个 $\mathfrak n_{b_0}<\epsilon_0$ 的邻域工作。$b_0,\epsilon_0$ 在任何输出阶之前固定。其选择使所有度量正性、简单根、图单调性和底阶算子小量同时成立。

这里给出无限尾上高度法向系数下界所用的实际小量，不能只在每个 compact 子区间分别缩邻域。Hu 物理坐标附录的 profile/reciprocal jets 界和 $\ell=d_\partial/(1+x_\partial)$ 给

$$
w_*^{-1}\le \exp\{n^{5/2}+Cn^2\},\quad
\ell^{-1}\le \exp\{Cn^2\},\quad
H^{3/4}=\exp\{-n^3/2+O(n^2)\}.                     \tag{8a}
$$

固定 $b_0\ge5$，complete-cylinder Sobolev 嵌入给

$$
|v|+|v_\theta|+|v_{\theta\theta}|
 \le C\|v\|_{b_0}H^{3/4},\qquad
|v_r|\le C\|v\|_{b_0}H^{3/4}\ell^{-1}.              \tag{8b}
$$

控制写成 $\kappa_m=H_m^{3/4}b_m$，$\sup_m|b_m|\le\|\kappa\|_{B_\delta}$。控制 profile 的固定 jets 至多为 $e^{C_kn^2}$，故先取一个底阶控制小量，便在所有尾同时有 $1/2\le w/w_*\le2$ 以及 $|\partial_r\log w|\le Ce^{Cn^2}$；这使用 $\sup_nH_n^{3/4}e^{Cn^2}<\infty$，不逐尾选邻域。

在两个完整尾，$Q=z_r+(1+w^2)z_{\theta\theta}/r$ 的纯旋转值准确为 $w\rho$。对 (6) 的 body 项逐项求导，利用 $\rho_r=w'\sin\vartheta\cos\theta$、$\rho_\theta=-w\sin\vartheta\sin\theta$ 及 (8a)–(8b)，有

$$
\frac{|Q-w\rho|}{w}
\le C|q|\|v\|_{b_0}
       \exp\{-n^3/2+n^{5/2}+Cn^2\}.                 \tag{8c}
$$

这里 $C$ 只涉及已经固定的几何和一个固定低阶，有限最初尾片也并入常数。于是

$$
K:=\sup_{n\ge1}\exp\{-n^3/2+n^{5/2}+Cn^2\}<\infty.
                                                               \tag{8d}
$$

取倾角小量使 $\rho\ge7/8$，并要求

$$
|q|\le[16CK(\|\Phi\|_{b_0}+1)]^{-1},\qquad
\|v-\Phi\|_{b_0}<1.
$$

则 (8c) 在全部尾至多为 $1/16$。在 cutoff 的固定正紧区，$w$ 有一个共同正下界，cutoff derivatives 有界；另取有限的 $q|A|$、$q|B|$ 小量，使额外 cutoff 误差至多为 $w/16$。其余固定紧段用同一个有限最大常数。因此这个单一低阶邻域满足全域 $Q\ge3w/4$。同样的 (8a)–(8b) 控制高度一阶 jets，结合纯旋转 $D=\rho^2$ 与有限 cutoff 界，再缩同一个 $\epsilon_0$ 即给 $D\ge1/2$。以后不随输出阶或尾编号改变它。

### 2.3 真正的高度切向框架

固定 $w,q$，令 $\phi_\vartheta=\partial_\vartheta z^{\rm ref}_{w,\vartheta}$。对 $(v,A,B)$ 的变分，$q^{-1}\delta z$ 准确为

$$
\eta=\rho_{w,\vartheta}\dot v+\dot A\chi_0
 +\dot B\left(\phi_\vartheta
                     +q(\partial_\vartheta\rho_{w,\vartheta})v\right).
                                                               \tag{9}
$$

最后一项的 $q(\partial_\vartheta\rho)v$ 是真正 $H^\delta$ 全平项。第一项是可逆正乘法；两个帽标量由内帽的常数和第一余弦系数唯一读出，因为 $\cos\vartheta>1/2$。所以 (9) 给一个光滑 tame 的切向框架及其逆。由于所有 cutoffs 在 $I_*$ 为零，$\ell_2\eta=\ell_3\eta=0$ 正好等价于 $\ell_2\dot v=\ell_3\dot v=0$。

## 3. 准确曲率残差与固定两矩投影

令 $g_w=(1+w^2)dr^2+r^2d\theta^2$，$\gamma=g_w-dz^2$。用 Hu 的符号

$$
\mathcal N_h(z)=-\sqrt D\,K_\gamma,
\quad D=(1+w^2)(1-z_\theta^2/r^2)-z_r^2,
$$

定义 raw 归一残差

$$
\mathcal A(x,q)=\frac{r\mathcal N_{h_w}(z)}q
\quad(q\ne0).                                        \tag{10}
$$

它是负的曲率密度除以 $q$。在 $q=0$ 处由单变量积分延拓，得到

$$
\mathcal A(x,0)
=L_w(v+A\chi_0-Br\chi\cos\theta).                    \tag{11}
$$

在两个完整尾，纯参考旋转和常数高度准确零曲率；(10) 的其余各项至少含一个全平 $v$ 或控制变化。固定 cutoff 残差为 compact 支持，并且 $\cos(qB\chi)-1$ 除以 $q$ 光滑。因此 $\mathcal A$ 光滑 tame 地落入全平源空间，而不只是普通 $C^\infty$ 空间。

把内盘填满，并在外盘外延拓 $g=e,z=0$。小邻域内 $\gamma-e$ 的固定低阶范数小。R629 的规范化等温坐标 $P=(P_1,P_2)$ 因而存在，并满足准确身份

$$
\int\mathcal A=0,\qquad \int P_1\mathcal A=0,
\qquad \int P_2\mathcal A=0.                           \tag{12}
$$

反射使最后一个矩自动为零。取 R629 的两个固定 compact 源 $B_0,B_1$，使

$$
\lambda_0F=\int F,\quad
\lambda_1F=\int r\cos\theta F,\quad
\lambda_iB_j=\delta_{ij}.
$$

定义

$$
\Pi=I-B_0\lambda_0-B_1\lambda_1,
\qquad Y_\delta=\Pi X^0_\delta.
$$

记

$$
\Psi_xF=(\int F,\int P_1F),\qquad
M_x=\Psi_x(B_0,B_1).
$$

在初始状态 $M_x=I$；固定低阶邻域可使 $\|M_x-I\|<1/2$。由 (12)，准确有

$$
\boxed{\mathcal A=T_xF,\quad F=\Pi\mathcal A,
\quad T_x=I-(B_0,B_1)M_x^{-1}\Psi_x.}                  \tag{13}
$$

特别 $F=0$ 推出完整曲率方程 $\mathcal A=0$。

这里 $P$ 的状态依赖也是 smooth tame：R629 的 Beltrami 方程
$q_0=\mu_\gamma(1+\mathcal Bq_0)$ 在一个固定 $\|\mu_\gamma\|_\infty<1/2$ 邻域由 $L^2$ Neumann 逆解出。对固定次数状态变分和空间导数使用同一个逆，Leibniz tame 乘积估计只把一个因子放在高阶；Cauchy 积分在固定 compact 区上的导数估计随后给 $P$。这产生一个固定阶位移，不随输出阶增长。故 (13) 的 $T_x$ 是实际的光滑 tame 线性源算子，不是形式的“余核校正”。

## 4. 类型和特征返回的准确残差校正

固定 $w$ 对高度变分，Hu §3 的连接一形式给

$$
rD_z\mathcal N_h(z)\eta
=\partial_r(a\eta_r+b\eta_\theta)
 +\partial_\theta(b\eta_r+c\eta_\theta)=L_x\eta,
$$
$$
ac-b^2=\frac{ww'/r}{D^2}+ED^{-3/2}\mathcal N_h(z),
\quad E=1+w^2.
$$

由 (8a)–(8d) 的单一邻域，$D\ge1/2$，$Q=z_r+Ez_{\theta\theta}/r\ge3w/4>0$。设 $\mathfrak B=E/(rQ)$，将切向系数改为

$$
\bar c=c-\mathfrak B\,r\mathcal N_h(z).
$$

则 $a\bar c-b^2=(ww'/r)/D^2$；法向通量不变，真实根及类型不动。对 (10) 的高度切向变量有

$$
D\mathcal A[\eta]
=\bar L_x\eta+q\partial_\theta(\mathfrak B\mathcal A\eta_\theta).
                                                               \tag{14}
$$

每个负组件取 $\bar L_x$ 的 minus 特征返回 $f$。令 $S\theta=-\theta$，并置

$$
\widetilde h_R=R_{-T_m}h_Lf^{-1},\quad
h_R=\mathsf O\widetilde h_R,\quad
e_m=(\mathsf E\widetilde h_R)\circ h_R^{-1}.             \tag{15}
$$

所有 lifts 现在为 $2\pi$ 周期偏移；反射仍给 plus 返回 $SfS$。故 $e=0$ 同时给两条真实返回的规定旋转。

Hu §11 的内支持流 isotopy 用
$K=f^{-1}h_R^{-1}R_{-T_m}h_L$、$J_r=\mathrm{id}+\chi_m^{\rm corr}(K-\mathrm{id})$，再从校正速度恢复对称 divergence 系数。它保留根 germs 与法向系数，并给一个算子 $\widehat L_x$，使

$$
\bar L_x-\widehat L_x=\mathscr E_x(e),                 \tag{16}
$$

其中 $\mathscr E_x(\epsilon)\eta$ 对独立占位源 $\epsilon$ 和 $\eta$ 双线性、smooth tame。其原证明只用奇 lift、反射、内支持和正速度，不用半周周期；因而在这里全部 $2\pi$ 模上适用。

固定根坐标和正组件的状态 comparison extension 按 Hu §11–12 构造，但参考正高度因子采用 R642 的 $(w_*J_*)^{-1/2}$，再乘实际倾角参考的 $\rho_{w_*,\vartheta}$。在正区只延伸相对于这个参考的边界 jets；在 $I_*$ 保持 reference 不动。所有 canonical value/conormal transmissions 因而相同。

相对于倾角参考，剩余尾系数差全部具有 $H_m^\delta E_m^{C_s}$ 因子：profile 控制为 $H^\delta$，高度 body 为 $qH^\delta$，两个端帽非平项已经放在真实参考中。固定 cutoff 区的差为普通 compact 小量。R642 已把参考倾角本身单独支付，不再把它混入这些差中。

## 5. 同一低阶邻域中的状态相关体源逆

### 5.1 实际有限增广块

令 $k_i=D_{\mu_i}\mathcal A$ 为真实 profile 导数，包含 (6) 中高度图对 $w$ 的依赖。它们支持于 $I_*$ 和固定正 cutoff 区。设 $K_x=D_\kappa\mathcal A$。

所需体源方程为

$$
\widehat L_x\eta+k_2\dot\mu_2+k_3\dot\mu_3
             +B_0c_0+B_1c_1=f,
\qquad \ell_2\eta=\ell_3\eta=0.                       \tag{17}
$$

$\eta$ 使用 (9) 的 body 和两个真实帽标量；$c_0,c_1$ 是临时源列标量，求得后丢弃，不加入物理未知。

在初始状态，配对两个核先给 (1) 的可逆二乘二方程，解出 $\dot\mu$；去掉相应源后，第二/第三模用约化 Green 逆，零/一模用 R629 的真实自由内帽 primitives，其余整数模用 R639/R642。两个源矩由 $B_0,B_1$ 去掉。故 (17) 的初始增广逆存在且唯一。

这也说明真实 profile 列不必预先等于对称 kernel border 的列：将每个 $k_i$ 分成 kernel 配对部分和相容部分，后者用约化逆作一次有限列变换，剩下的有限矩阵正是 (1)。列变换仅增加固定中心到两个全平模的映射，保留 R642 的端点 block 界和零角阶。

### 5.2 与真实倾角参考比较

记 $P_\vartheta$、$G_\vartheta$ 为 R642 的完整增广参考和逆。它的输出明确分为全平 body 与有限帽/核/源标量。倾角势只作用 body，帽列是实际真齐次 lifts 的 compact 像。canonical body 的两个归一化 rows 固定为参考 rows；帽 lift 在这些 rows 中的变化归入有限列。由于 comparison 图在 $I_*$ 不变，这也正是 (9) 的固定 affine slice。令 $P_x$ 为 (17) 在固定 canonical 源/域坐标中的算子。

在共同闭 graph 域上比较

$$
R_x=(P_x-P_\vartheta)G_\vartheta.                       \tag{18}
$$

负组件的 principal part 已准确固定，故其差只是 $H^\delta E^{C_s}$ 的势差。正组件的 principal 差在边界三阶消失，写成

$$
-\partial_a\bigl(d^3e_x^{ab}\partial_b\bigr)+\delta V_x,
\qquad d=y(1-y).
$$

Hu §13 的任意边界值 graph 估计控制
$du_y,d^{3/2}\Lambda u,d^2u_{yy},d^{5/2}\Lambda u_y,d^3\Lambda^2u$。这里参考含非径向势 $q_\vartheta$，所以实际使用径向 $P_0u=F-q_\vartheta u$；该势是零阶且其固定系数由 R642 控制，得到同一个 graph 界。没有把非径向 $P_\vartheta$ 当作 Fourier ODE。

R642 在 $5/8$ 和 $7/8$ 的同一个自然逆给 $G_\vartheta$ 的两指数 block 衰减。与输出端的 $H_k^\delta E_k^{C_s}$ 相乘后，所有材料权都可用 Schur 求和吸收。有限列差具有 compact 或 $H^\delta E^{C_s}$ 源，依 (9) 同样有小底阶范数。

因此存在固定 $d_*$，在一个固定低阶邻域内有

$$
\|R_xF\|_{t,s}
\le C_{t,s}\left[
\epsilon\|F\|_{0,s}
 +\mathfrak n_{t+s+d_*}\|F\|_{0,s_0}\right].           \tag{19}
$$

取底阶 $(t,s)=(0,s_0)$，缩小一次 (8) 的邻域，使该算子范数小于 $1/2$。这给

$$
P_x=(I+R_x)P_\vartheta,
\qquad G_x=G_\vartheta(I+R_x)^{-1}.                    \tag{20}
$$

闭域身份先在 compact 光滑源上成立，再由底阶收敛和分布收敛识别；所有 value/conormal transmissions 已在第 4 节固定，因此极限没有换端点实现。

### 5.3 非对角参考的交换子及固定损失

$G_\vartheta$ 不是 Fourier 对角，不能在本段省去其交换子。准确 resolvent 身份给

$$
[\Lambda,G_\vartheta]
=-G_\vartheta[\Lambda,P_\vartheta]G_\vartheta.
                                                               \tag{21}
$$

其中 $[\Lambda,P_\vartheta]$ 只有 R642 的零阶旋转势交换子和有限列/行交换子。前者乘 $G_\vartheta$ 的共同底阶有界性由 R642 (17)–(19) 的同一尾积控制；后者是固定中心的有限项。故在估计 $[\Lambda,R_x]$ 时，新增的
$(P_x-P_\vartheta)[\Lambda,G_\vartheta]$ 仍满足 (19) 型界。

用同一个底阶逆恢复角正则性，再用局部方程恢复 normal derivatives；$H^\delta$ 的余量恢复材料权。每一步完整参考系数乘积先合并成 $E^{C_s}$，再用 $E^{C_s}\le C_sM$，只花一个固定材料阶；微分表达式本身只有固定有限阶。因此最终损失 $d_*$ 与输出阶无关。

这给 $G_x$ 的存在、唯一、连续及 tame 界。算子族本身 smooth tame；Hamilton 的线性逆族定理遂给 $G_x$ smooth tame。它是实际状态相关逆，已经包含真实帽列、两 profile 列与两个临时矩源列。高阶范数只需有限，不另缩小低阶邻域。

## 6. circle 导数、控制平滑与完整 coupled 逆

### 6.1 全部整数的 chart 逆

在一个负组件，令 chart 变分为 $\dot h_L=\psi\circ h_L$。Hu §11 的直接微分给

$$
D_h e[\psi]=\mathcal M_T\psi+\mathcal Q_h(e,\psi),
\qquad \mathcal M_T\psi=\mathsf E[\psi(\theta+T)].       \tag{22}
$$

在零均值偶函数上，其准确逆为

$$
\mathcal M_T^{-1}(g_j\cos j\theta)
=\frac{g_j}{\sin(jT)}\sin j\theta,\qquad j\ge1.        \tag{23}
$$

由 (3) 它只花一阶角导数和固定材料权。$\mathcal Q_h$ 对独立残差占位符和 $\psi$ 双线性；其所有内部 composition paths 固定在当前状态。半周限制没有用于这两条身份。

设 $C_x^\circ$ 为高度变分对 circle 的导数，$D_x^\circ=D_\kappa e$，并记

$$
R_x^\circ=\langle C_x^\circ\rangle,\qquad
J_x=\langle D_x^\circ\rangle.
$$

这里还需检查真实帽列的 circle 像。对任意径向 $w$，完整纯旋转尾的特征速度与倾角无关，故其精确 $C^\circ\phi_\vartheta=0$。从纯旋转尾到当前状态的差为 $q\rho v$，因此在当前状态对该帽列的 circle 导数至少含一个 $H^\delta$ body jet；(9) 另一个 $q(\partial_\vartheta\rho)v$ 项本来就在全平空间。高度常数帽列和 cutoff 区不进入任何负组件。故 $C_x^\circ$ 在真实有限帽坐标上同样落入 $Z_\delta$，不会引入一个慢于端点权的 circle 源。

profile 控制 $\mu$ 只在正区，其引起的尾高度变化为常数或固定正 cutoff 项，所以 $D_\mu e=0$。每个 $\kappa_m$ 只影响本负组件的特征图，故 $J_x$ 对角。初始点 $J_*=I$；一个固定低阶邻域保其条目离零并给 tame 逆。

完整 circle 微分为

$$
\dot e=q C_x^\circ\eta+D_x^\circ\xi
                 +\mathcal M_T\psi+\mathcal Q_h(e,\psi).
                                                               \tag{24}
$$

### 6.2 $K_x=D_\kappa\mathcal A$ 的两类真实源

在每条完整尾，对任意径向 $w$，纯 $z^{\rm ref}_{w,\vartheta}$ 都准确零曲率。因而 $K_x$ 的尾部局部项在 (10) 的积分展开后，每项均含一个全平 body $v$ 的 jet（也允许乘 $\rho$ 后的零阶 $v$），以及一个控制系数。写

$$
\xi_m=H_m^\delta b_m,\qquad \|b\|_{\ell^2}=\|\xi\|_{B_\delta}.
$$

body 给 $H_m^\delta$，控制再给 $H_m^\delta$；除以源的 $H_m^\delta$ 后仍留下一个 $H_m^\delta$，它吸收任意固定输出材料阶与所有固定几何成本。

改变 $h_a$ 产生的另一个曲率源只在固定 cutoff 区。其系数为

$$
I(\xi)=\sum_{m\ \text{left of cutoff}}
                  \xi_m\int w\chi_m\,dr.
$$

由实际 $w$ 界及 control profile 固定 jet 界，$I:B_\delta\to\mathbb R$ 有界。其高度因子为

$$
I(\xi)\frac{\cos(qB\chi)-1}{q},
$$

这个高度因子在 $q=0$ 光滑，在完整左尾为常数、右尾为零；它本身不是 compact 支持。divergence 高度算子准确消去其两尾常数，所以其曲率源只在固定 compact cutoff 区。这里的求和只遍历 cutoff 左侧的控制组件；cutoff 右侧控制同时等量改变 $h$ 与 $h_a$，在该区仅留下一个常数高度，不产生这项源。这个有限泛函项不计入上述两因子局部项，但同样从底序列范数平滑到每个源阶。

于是

$$
\|K_x\xi\|_{Y_{\rm full},s}
\le C_s(1+\mathfrak n_{s+d_*})\|\xi\|_{B_\delta},
$$
$$
U_x:=G_xK_x
$$

也从底控制空间 smooth tame 地平滑到全部高度/compact 参数阶。物理 $\eta$ 的端帽部分由有限坐标读出，不要求它们的正阶角 jets 全平。

### 6.3 明确的 coupled 右逆

给定目标源 $(f,g)\in Y_\delta\times(Z_\delta)_{\rm even}$，令 $g_0=\langle g\rangle$。$G_x$ 先解 (17)，随后丢弃两个临时矩源标量；$R_x^\circ,C_x^\circ$ 只作用于其物理高度输出。取 $q$ 和低阶邻域，使

$$
\|qJ_x^{-1}R_x^\circ U_x\|_{B_\delta\to B_\delta}<1/2.
                                                               \tag{25}
$$

这是底阶算子条件，且由上一节实际控制平滑性支付。定义

$$
\begin{split}
\xi={}&(I-qJ_x^{-1}R_x^\circ U_x)^{-1}J_x^{-1}
               (g_0-qR_x^\circ G_xf),\\
(\eta,\dot\mu)={}&G_xf-U_x\xi,\\
\psi={}&\mathcal M_T^{-1}
             (g-qC_x^\circ\eta-D_x^\circ\xi).
\end{split}                                                   \tag{26}
$$

第二行同时包含由 (9) 读回的 $\dot v,\dot A,\dot B$。第一行的控制方程保证第三行输入零均值；因此 (23) 真正适用。

(26) 解出

$$
\Pi(\widehat L_x\eta+k\dot\mu+K_x\xi)=f,
\quad \ell_2\eta=\ell_3\eta=0,
$$
$$
qC_x^\circ\eta+D_x^\circ\xi+\mathcal M_T\psi=g.        \tag{27}
$$

控制逆先在 $B_\delta$ 以 (25) 解出。将已解方程写成“数据项 + $qJ^{-1}R^\circ U\xi$”，第二项在每个高阶只用 $\|\xi\|_{B_\delta}$ 和一个高阶状态范数；故恢复所有控制阶无需新小量。随后代回高度和 chart。连续性来自底阶 resolvent identity 与这些高阶估计，再由线性逆族定理得到完整 smooth tame 依赖。

## 7. 准确双线性残差身份与非线性根

真正要求解的固定目标空间残差为

$$
\mathcal R(x,q)=(F,e)=(\Pi\mathcal A,e).
$$

由 (11)、(7) 与双核，$\mathcal R(x_*,0)=0$。它在第 2 节的固定 tame 空间之间 smooth tame。

令 $V(x,q)(f,g)$ 为 (26) 给出的真实切向变量。结合 (14)、(16)、(24)、(27)，并用 (13)，准确有

$$
D_x\mathcal R\,V(f,g)
=\left(
f+\Pi\{q\partial_\theta(\mathfrak B T_xF\,\eta_\theta)
                       +\mathscr E_x(e)\eta\},
\quad g+\mathcal Q_h(e,\psi)\right).                   \tag{28}
$$

临时矩源列在 (28) 中由 $\Pi B_i=0$ 准确消失。没有假设未解状态的导数以旧 $r\cos\theta$ 为余核。

对独立占位源 $(r_1,r_2)$，冻结当前状态和全部 composition paths，定义

$$
\mathcal Q_x[(r_1,r_2),(f,g)]
=\left(
\Pi\{q\partial_\theta(\mathfrak B T_xr_1\,\eta_\theta)
                         +\mathscr E_x(r_2)\eta\},
\quad\mathcal Q_h(r_2,\psi)\right).                    \tag{29}
$$

$\eta,\psi$ 线性依赖 $(f,g)$，故 (29) 对两个残差槽双线性。所有系数均 smooth tame；端帽高度增量的非平角 jet 只作为有限标量乘固定真 lift，其与 $r_1$ 或 $r_2$ 的积仍有一个 $H^\delta$ 因子，允许固定材料损失。故 $\mathcal Q$ 在同一低阶邻域 smooth tame。

于是 (28) 正是

$$
\boxed{D_x\mathcal R(x,q)V(x,q)y
=y+\mathcal Q_x[\mathcal R(x,q),y].}                   \tag{30}
$$

使用 [Hamilton 1982, Part III, Theorem 3.3.1, pp. 211–212](https://www.ams.org/journals/bull/1982-07-01/S0273-0979-1982-15004-2/S0273-0979-1982-15004-2.pdf)：smooth tame 的 (30) 在一个零点附近给 smooth tame 的参数根。这里全部前提已经在同一个实际低阶邻域中支付，不是只写一条形式 Lyapunov–Schmidt 方程。

所以存在 $q_0>0$ 和光滑分支 $x(q)$，$|q|<q_0$，经过 (7)，满足

$$
\Pi\mathcal A(x(q),q)=0,\qquad e(x(q),q)=0.
$$

由 (13)，完整 $\mathcal A=0$；因此

$$
K(g_{w(q)}-dz(q)^2)=0
$$

准确成立。所有高阶结论使用同一个 $q_0$。

## 8. 从高度根得到准确嵌入和真实内帽姿态

在填满内盘并延拓到外平面的 $\gamma_q=g_{w(q)}-dz(q)^2$ 上，R629 给

$$
\gamma_q=P_q^*(e^{2\varphi_q}|dy|^2),\qquad
P_q(z)=z+O(|z|^{-1}),\qquad \varphi_q=O(|y|^{-2}).
$$

刚才的准确平坦性给 $\Delta\varphi_q=0$；在整平面上衰减的光滑调和函数为零。因此

$$
\gamma_q=P_q^*|dy|^2,
\qquad
X_q=(P_{q,1},P_{q,2},z(q))
$$

准确满足 $X_q^*e=g_{w(q)}$。$P_q$ 是全局近恒等微分同胚，故 $X_q$ 是嵌入。外部 $\gamma_q=e,z=0$，$P_q$ 在该开集为保持方向的欧氏等距；无穷远规范使它准确等于恒等。因此外平帽逐点固定。

内帽的度量 $\gamma_q$ 在原 Cartesian 坐标为

$$
\cos^2\vartheta(q)\,dx^2+dy^2,
\qquad \vartheta(q)=qB(q).
$$

其 developing map 为仿射，写成 $P_q(x,y)=L(x,y)^T+c$。令 $S=\operatorname{diag}(1,-1)$；反射使 $\gamma_q$ 关于 $S$ 对称，而 $P_q(z)=z+O(1/z)$ 的规范化 Beltrami 解唯一，所以 $P_q\circ S=S\circ P_q$。因此 $LS=SL$ 且 $c_y=0$，即 $L$ 为对角矩阵。又

$$
L^TL=\operatorname{diag}(\cos^2\vartheta(q),1).
$$

保持方向且近恒等的规范排除负号，给 $L=\operatorname{diag}(\cos\vartheta(q),1)$。这同时排除了另一个平面转角和 $y$ 平移。因此

$$
P_q(x,y)=(c_x(q)+x\cos\vartheta(q),\ y).
$$

所以内帽在空间中的准确姿态是

$$
\boxed{X_q(x,y)=
(c_x(q)+x\cos\vartheta(q),\ y,
 h_a(q)+qA(q)-x\sin\vartheta(q)).}                     \tag{31}
$$

这是一个真实刚体平帽，不是只在旧水平圆盘上添加倾斜高度。所有尾和帽 jets 光滑相接。$\kappa(q)$ 已在 $K_\delta$ 中，且 $w_*$、控制和 body 的实际尾界足以使 $w(q),X_q$ 光滑全平延拓；此处不额外声称旧偶模定理的更强 $K_{2\delta}$ 结论。

## 9. 倾斜首项和整像的正位移

在 $q=0$ 对整个系统微分。circle 均值的高度导数消去非零频率，而 $\Phi$ 只有第二、第三模，故

$$
\kappa'(0)=0.
$$

曲率第二次项由 $\Phi^2$ 产生的角频只有 $0,1,4,5,6$。配对第二、第三核，(1) 遂给

$$
\mu'(0)=0.                                           \tag{32}
$$

于是第一阶真实度量不变，完整一阶等距场就是 R628 的两条同背景场之和（按本稿固定竖直方向作对应反号）。其在内外帽都为零，故
$c_x(q)=O(q^2)$。第二阶的径向度量变化只在零角模，不能改第一角模方程。R628 的全部 $rr,r\theta,\theta\theta$ 交叉计算、R635 的边界消去和 R637/R639 的严格端口因而给

$$
\boxed{\vartheta(q)=\beta_*q^2+O(q^3),
\qquad \beta_*>1/4.}                                 \tag{33}
$$

若将旋转方向改号，(33) 同时改号而绝对值不变。本稿 (5) 的约定给上式正号。光滑分支允许再选一个正的 $q_1\le q_0$，使

$$
|\vartheta(q)|\ge\tfrac12\beta_*q^2
\quad(0<|q|<q_1).
$$

现在固定任一这样的非零 $q$，冻结 $w(q)$ 和整个旋转度量。令

$$
X_{q,\phi}(r,\theta)
=R_{-\phi}X_q(r,\theta+\phi).
                                                               \tag{34}
$$

其第一基本形式准确为同一个 $g_{w(q)}$；外平帽逐点固定。内帽的法向围绕竖直轴作半角 $|\vartheta(q)|$ 的锥形变化，因此 (34) 是真实可动端口。

这里也可以直接给整像而非标记点的正位移。取 $q$ 更小，使 $|c_x(q)|<a/8$、$|\vartheta(q)|<1/16$。相位 $0$ 与 $\pi$ 的内帽平面，在空间横坐标 $X$ 下分别为

$$
z=H+c_x\tan\vartheta-X\tan\vartheta,
\qquad
z=H+c_x\tan\vartheta+X\tan\vartheta,
$$

其中 $H=h_a+qA$。取第一平面上 $X=a/2,y=0$ 的点。它到第二平面的准确距离为 $a|\sin\vartheta|$；垂足的横坐标为 $a/2-a\sin^2\vartheta$，因 $|c_x|<a/8$、$|\vartheta|<1/16$，它严格在第二内帽的椭圆投影内部。这个点到第二内帽投影边缘的水平距离大于 $a/4$，而 $a|\sin\vartheta|<a/16$。全局微分同胚 $P_q$ 将其余 annular graph 投到该椭圆外，故那些点不可能更近。因此对于足够小的同一个 $q$，最近点确实在第二内帽，得到

$$
\boxed{d_H(X_{q,0}(\overline D_b),X_{q,\pi}(\overline D_b))
\ge a|\sin\vartheta(q)|
\ge\frac{a\beta_*}{4}q^2>0.}                          \tag{35}
$$

若在外部连接一个固定光滑闭合部分，可先使它与这个内帽紧子盘保持正距离；该距离在足够小分支中保留，同一个 (35) 仍适用于整个闭曲面像。这样可以获得一个准确闭嵌入相位族及任意预先放在外刚性部分的开握持 patch；这里的量仍为局部 $q^2$ 尺度。

## 10. 本定理实际支付的范围

R628 的相邻双模交叉端口现已积分为一个非零有限 $q$ 的准确嵌入；R642 的独立旋转参考已用于实际状态相关逆；两个全局曲率矩、两个 profile 核列、每个负组件的返回图与残差校正都在同一个系统中处理。最终相位动作 (34) 才是在同一个冻结度量上的连续族，幅值设计分支不被误称为固定度量分支。

余下任务是实际的宏观量化与几何构造：本稿没有给有效下界的 $q_0$，也没有给足以推出 $d_H\ge0.3D$ 或 $\operatorname{reach}\ge0.03D$ 的有限角、有限形状和厚度界。式 (35) 说明新机制的整像运动确实非零；它不能用来省略上述两个数量门槛。
