# R119 续篇：真实正型双端 DN 到完整 Airy Cayley 端口及全源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对强首剪切新尾，使用已经确定的实际 KAM
左右端角，把每个完整正型分量的两端 DN 转成根处完整 Airy
两行尺度中的 Cayley 散射算子。径向参考和真实算子都保留
两端互耦、全部 Fourier 模、mean 高度差、共同平移和通量
电荷。对 $|s|\le4$，全部内部正分量的真实相对和满足
$$
 \boxed{\quad
 \sum_I\|\mathcal C_I^{\,\rm true}-\mathcal C_I^0\|_{H^s\to H^s}
 <2^{400}\|X\|\le2^{-261744}.
 \quad}                                                     \tag{C.1}
$$
这里 $H^s$ 含**两个端点**的完整角函数。没有丢掉
$\mathsf S_m$ 的非对角项，也没有把一条 principal DN 根替代
完整正区 Green。独立普通/弱源的 affine 散射列在第7节给出。

这项结论是全根 Airy 平衡端口中的正型块，尚不等于所有正负
块已经在原全标签强范数中完成整个网络反演。

## 1. 同一个新对象及两张已选端角

采用
[新尾 KAM](R119-supplement-stronger-tail-joint-actual-return-KAM.md)
和[固定参考/共同端角](R119-supplement-KAM-selected-fixed-reference-and-exact-endpoint-phases.md)
的 $\Gamma^0,\Gamma^*(a),X$，$\|X\|\le2^{-262144}$。
算子门在实参数、实背景上证明；全部线性数据允许复数值。
本篇指标只包含两端均已有内部负分量端角的正分量；最外尚无
两张这种端图的分量留给 cut128/有限 connector，不给它补造反射。
正型分量 $I=[t_-,t_+]$ 在同一个实际上升 quintic 中，
$$
 A=-7+{\sqrt{12}\Delta^+\over\eta_j}S'(x),\qquad
 \Delta^+_{j,1}=\log K_j+|\log\delta_j|,\qquad
 \Delta^+_{j,2}=\log(65/64)+2|\log\delta_j|.
 \tag{C.2}
$$
新首剪切 $K_j=2^{128}$ 于 $j>8192$，此前为64。仍有
$j/2<\Delta^+<3(j+4)$。下降 bump 不与本区相交，所以本区
的 $A,w_{\rm ref}$ 及根 germ 对 $\Gamma$ 准确不变。
物理尺度统一为实际的 $\rho(\Gamma^*)$；所有源和 raw flux
都使用这个尺度。

两个相邻负分量已经给出共同真实端角 $K_-,K_+$，满足固定
参考的两支相位对齐。这两张图原样消费，不为正型段重新选择
一张方便的角图。令
$$
 \mathcal M_j=\sum_{\substack{|r-j|\le2\\r\ge129}}N_r,\qquad
 N_r=2^{184}h_r^{-5}{\zeta_r\over\mu_r\delta_r^2}.
$$
邻端所属负分量的层号至多相差1，其跨胞四态至多消费两相邻层。
由前篇 (F.14)、$\kappa_i^{-1}<2^{28}\sqrt i\,\delta_i^{-3/4}$
及 $\|a\|\le2\|X\|$，在角宽 $1/4$ 上可取
$$
 \|K_e-\mathrm{id}\|+\|K_e'-1\|
 <2^{86}(j+5)^2\mathcal M_j\delta_j^{-3/4}\|X\|,
 \qquad e=-,+.                                             \tag{C.3}
$$
有限前缀和两处规范接缝均包含在实际 $N_r$ 中。

真实正型光学长度
$L_+=\int_I\sqrt A\,dt$ 满足
$$
                L_+>{1\over32}\delta_j^{3/4}\sqrt j,\qquad
                |I|<\delta_j^{3/2},\qquad L_+<1.
 \tag{C.4}
$$
证明与原正型端角篇 (D.3) 相同，但重新使用 (C.2)：
在 $x\in[1/4,3/4]$ 上 $S'\ge135/128$，
$A>\sqrt{12}\Delta^+/(2\eta)$，积分这个真实子段即得显示下界。
新 $\log K_j$ 满足同一个跳幅门，因此没有转授旧 profile 的数值。

## 2. 真实 drift 后再作光学插值

原 raw Jacobi 系数为
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2+Av^2\end{pmatrix},
 \quad \mu=(w_{\rm ref}/a)JD^{-3/2},\quad
 d=E(V-P)/J,\quad v=\sqrt D/J.
$$
这里 raw $h$ 是高度缺口 $v_{\rm deflection}$ 的 Jacobi 变化，
实际固定 ambient 高度为 $Z_{\rm ref}-v_{\rm deflection}$，
所以其变化是 $-h$；本篇完整两迹共同使用这一号数。
先取准确 drift 流
$\phi_t=-d(t,\phi)$、$\phi(t_-)=\mathrm{id}$。设
$$
 H_e=\phi_e^{-1}\circ K_e,\qquad
 \chi(t,\eta)=(1-s_+(t))H_-(\eta)+s_+(t)H_+(\eta),\qquad
 s_+(t)={1\over L_+}\int_{t_-}^t\sqrt A\,d\tau,
$$
$$
                         \Phi(t,\eta)=\phi(t,\chi(t,\eta)).
 \tag{C.5}
$$
于是 $\Phi_e=K_e$，原径向变量 $t$ 始终不变。完整四态和真实
flow/逆 flow 给宽 $1/8$ 上的共同界
$$
 \|H_e-\mathrm{id}\|+\|H_e'-1\|
 <a_j,\qquad a_j=2^{90}(j+5)^2\mathcal M_j\delta_j^{-3/4}\|X\|.
 \tag{C.6}
$$
例如 drift 的 $C^1$ 差小于
$2^{10}N_j\|X\|\delta_j^{3/2}$，在 (C.3) 下可直接吸收。
所有这些量远小于 $2^{-32}$。

写 $J_\chi=\chi_\eta$。准确有
$|J_\chi-1|<a_j$、
$|\chi_t|/\sqrt A\le2a_j/L_+$，后一式到根取连续极限。
必须先消 drift；直接插值物理角会留下不可用的 $d/\sqrt A$。
在 (C.5) 后，完整能量的矩阵，以
$(u_t,\sqrt A\,u_\eta)$ 为比较变量，是
$$
 \begin{pmatrix}
 (1+r_\mu)J_\chi&-(1+r_\mu)\nu_\chi\\
 -(1+r_\mu)\nu_\chi&
 [(1+r_\mu)\nu_\chi^2+1+r_\beta]/J_\chi
 \end{pmatrix},\qquad
 \nu_\chi={\chi_t\over\sqrt A}.
 \tag{C.7}
$$
其中 $|r_\mu|+|r_\beta|<512(4N_j\|X\|)$ 是真 drift
Jacobian、$JD^{-3/2}$ 和 $D^{-1/2}/J$ 的完整商式界。
这是实际整个散度二次型，而非只比 principal symbol。

逐项比较 (C.7) 与恒等矩阵，安全取
$$
 \epsilon_j=2^{104}(j+5)^2\mathcal M_j\delta_j^{-3/2}\|X\|,
 \qquad
 |\mathscr E_a(u,z)-\mathscr E_0(u,z)|
 \le\epsilon_j\|u\|_{\mathscr E_0}\|z\|_{\mathscr E_0}.
 \tag{C.8}
$$
$\mathscr E_0=\int\mu_0(|u_t|^2+A|u_\eta|^2)$，
$\mu_0=w_{\rm ref}/a$。此比较在宽 $1/8$ 的**复角平移**
后的全部系数上也成立；只把双线性形式作解析延拓，不给复
系数虚构实序。实角时有 $(1-\epsilon_j)\mathscr E_0
\le\mathscr E_a\le(1+\epsilon_j)\mathscr E_0$。

预算确实对全部层求和。前篇实际 $N_r$ 已证明
$$
 \sum_{r\ge129}r(r+4)N_r\delta_r^{-3/2}<2^{200}.
$$
这里129至8193的完整有限前缀由各项 $<2^{185}$ 和少于
$2^{14}$ 项支付，随后真实第三幂给几何尾。交换**非负**
有限邻胞和，
$$
 \sum_j(j+5)^2\mathcal M_j\delta_j^{-3/2}
 <2^8\sum_r r(r+4)N_r\delta_r^{-3/2}.
$$
因为每个 $r$ 最多出现5次，
$\delta_j^{-3/2}\le8\delta_r^{-3/2}$，
$(j+5)^2<4r(r+4)$。每层至多两个正分量，故
$$
                              \sum_I\epsilon_j<2^{320}\|X\|.
 \tag{C.9}
$$
两个全局因子 $\delta_{4096}^{-3/2}$、
$\delta_{8192}^{-485/4}$ 从未删除。

## 3. 完整双端 DN 和共同常数

同一径向方程
$$
 (h,p)_t=(p/\mu_0,\ m^2A\mu_0h),\qquad
 \Phi_m=\begin{pmatrix}\alpha_m&\beta_m\\\gamma_m&\delta_m\end{pmatrix}
$$
满足 $\det\Phi_m=1$、$\beta_m>0$。完整 outward DN 为
$$
 \mathsf S_m={1\over\beta_m}
       \begin{pmatrix}\alpha_m&-1\\-1&\delta_m\end{pmatrix},
 \quad m\in4\mathbb Z,\qquad
 \mathsf S_0=R_I^{-1}\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \quad R_I=\int_I\mu_0^{-1}dt .
 \tag{C.10}
$$
所有非对角项保留。它定义完整能量迹形式
$\mathcal N_0=\bigoplus_m\mathsf S_m$；其唯一零方向是 raw 两端
共同常数。真实 Dirichlet lift 由在同一迹类中最小化
$\mathscr E_a$ 得到，真实完整 DN 记为 $\mathcal N_a$。
由 (C.8)，
$$
 (1-\epsilon_j)\mathcal N_0\le\mathcal N_a
                      \le(1+\epsilon_j)\mathcal N_0.
 \tag{C.11}
$$
它们输出 $( -p(t_-),p(t_+))$ 在实际两端角中的密度。
两端共同常数、mean 高度差和源造成的 mean flux 均不删除。

若把所有角系数平移至 $\eta+z$、$|\operatorname{Im}z|<1/8$，
同一复 form 的 Dirichlet 修正由 Lax--Milgram/Neumann 在原
零迹能量空间解出。与参考 lift 相减，得到完整复比较
$$
 |\langle(\mathcal N_a(z)-\mathcal N_0)f,g\rangle|
 \le2\epsilon_j
       \langle\mathcal N_0f,f\rangle^{1/2}
       \langle\mathcal N_0g,g\rangle^{1/2}.
 \tag{C.12}
$$
具体地，修正能量不超过
$\epsilon_j(1-\epsilon_j)^{-1}$ 倍参考 lift 的能量，
再在差的 Green identity 中使用一次系数差即可。
共同常数在复形式中仍准确为零。

## 4. 根处完整 Airy 两行，及一个保留 mean 的 Cayley 变换

每端令 $b_e=|Q_t(t_e)|$ 是已付真实根斜率，$\varsigma_e$
指向相邻负分量。因此它也恰是**正型区的 outward 方向**。
参考根规范由
[真正根图](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
给出：
$$
 \alpha_{0,e}=b_e\mu_{0,e},\quad
 \sigma_{e,m}=(1+(|m|/b_e)^{4/3})^{1/2},\quad
 W_e=\operatorname{diag}_m(\sqrt{\sigma_{e,m}}).
 \tag{C.13}
$$
这是同一完整、含 $m=0$ 的根两行平衡，不是把 $m=0$ 代进
$m^{-1}$。根处参考 normal shear 准确为
$$
 \ell_{0,\xi}(0)=-{\varsigma_e\over b_e}+{2\over5}
                     (14d_{0,e}-1/28),\qquad
 |\ell_{0,\xi}(0)|<1/32 .
 \tag{C.14}
$$
因为 $0<d_{0,e}<2^{-10}$、$b_e>2^{200}$；此式保留 $g_x/g^2$
及真实参考密度导数。

在两端同时定义参考归一化的完整状态
$$
 Y_h=W\sqrt{\alpha_0}\,f,\qquad
 Y_p=W^{-1}\left(\alpha_0^{-1/2}p_{\rm out}
                       +\tfrac12\ell_{0,\xi}\sqrt{\alpha_0}\,f\right).
 \tag{C.15}
$$
这里 $f,p_{\rm out}$ 已在 (C.5) 的真实端角中；
共同角和两端 density factor 均不省略。
设 $\mathcal H=L^2(\mathbb T_{\pi/2})\oplus
L^2(\mathbb T_{\pi/2})$，令
$$
 L=\alpha_0^{-1/2}W^{-1},\quad
 P_0=L^*\mathcal N_0L,\quad P_a=L^*\mathcal N_aL,\quad
 T_0=\tfrac12W^{-1}\ell_{0,\xi}W^{-1}.
$$
则 $P_0,P_a$ 是非负闭形式，
$\|T_0\|<1/64$，且
$$
                   Y_p=\mathcal R_aY_h,\qquad
                   \mathcal R_a=P_a+T_0.                  \tag{C.16}
$$
形式域在 $\mathcal H$ 中稠密，因为含全部有限 Fourier 数据。
闭性可由完整原迹空间直接证明：$L$ 有界到边界 $L^2$，
所以在 $\|u\|^2+\langle P_0u,u\rangle$ 中 Cauchy 的序列，
其 raw mean 与能量迹同时收敛；极限仍为 $Lu$。
实际 form 由 (C.11) 有同一域。加有界实 $T_0$ 后，
$\mathcal R_0,\mathcal R_a$ 均是 selfadjoint 算子。

此处无需先证明 $\mathsf S_m$ 与某个对角乘子有均匀上下界。
即使某模两个端点强烈耦合，闭形式和下面的 resolvent 仍完整。
raw 共同常数对应 $Y_h=(\sqrt{\alpha_{0,-}},
\sqrt{\alpha_{0,+}})$ 的零频向量，$P_0$、$P_a$ 在该向量上为0；
它没有从 $\mathcal H$ 删除，$T_0$ 仍按真实 normal shear 作用。

准确定义 incoming/outgoing 两端向量
$$
 a_{\rm in}=(Y_h-iY_p)/\sqrt2,\qquad
 a_{\rm out}=(Y_h+iY_p)/\sqrt2.
$$
则
$$
 \boxed{\quad
 a_{\rm out}=\mathcal C_a a_{\rm in},\qquad
 \mathcal C_a=(I+i\mathcal R_a)(I-i\mathcal R_a)^{-1}
             =-I+2i(\mathcal R_a+i)^{-1}.
 \quad}                                                     \tag{C.17}
$$
两者在完整 $\mathcal H$ 上 unitary，包括整个 mean 部分。
这只是完整 $2\times2$ 双端关系的 Cayley 表达，没有把它拆成
两个彼此不通的单端反射。

## 5. 相对 form 差给同空间全频算子差

先在实角 $L^2$ 上证明。若 $\mathcal R=P+T_0$，
对 $u=(\mathcal R\pm i)^{-1}f$，selfadjoint 性给
$\|u\|\le\|f\|$，而
$$
 \langle Pu,u\rangle
 =\operatorname{Re}\langle f,u\rangle-\langle T_0u,u\rangle
 \le(1+\|T_0\|)\|f\|^2 .
$$
结合 $P_a\ge(1-\epsilon_j)P_0$ 和 form resolvent identity，
$$
 \|\mathcal C_a-\mathcal C_0\|
 \le {2(1+\|T_0\|)\over\sqrt{1-\epsilon_j}}\epsilon_j
 <8\epsilon_j.                                            \tag{C.18}
$$
该证明支付两个完整 resolvent；不是由一个 DN 特征根的差
猜测整个散射算子。

为把它放进所需 Sobolev 窗，不能只说系数光滑。使用 (C.12)
的真实复角平移族。参考
$$
 \|P_0^{1/2}(\mathcal R_0\pm i)^{-1}\|<2,\qquad
 \|P_0^{1/2}(\mathcal R_0\pm i)^{-1}P_0^{1/2}\|<2 .
$$
第二式由 $P_0+i$ 的谱演算及 $\|T_0\|<1/64$ 的有序
resolvent identity 得到；不要求 $P_0$ 有界。将 (C.12) 的
$2\epsilon_j$ form 因子置入该 sandwich，Neumann norm
小于 $4\epsilon_j<1/2$。故在整个 $|\operatorname{Im}z|<1/8$
有
$$
                 \|\mathcal C_a(z)-\mathcal C_0\|_{\mathcal H}
                 <64\epsilon_j .                         \tag{C.19}
$$
它是该复条带上的全纯有界算子族。对实角平移，它准确是
共轭族，所以 Cauchy 给全部 $0\le k\le6$：
$$
 \|\operatorname{ad}_{\partial_\eta}^{\,k}
                  (\mathcal C_a-\mathcal C_0)\|
 <64\,k!\,8^k\epsilon_j .
$$
用
$\partial_\eta^r B=\sum_{k=0}^r\binom rk
(\operatorname{ad}_{\partial_\eta}^{\,k}B)\partial_\eta^{r-k}$
得到所有非负整数至6阶的同空间界。对 adjoint 使用
$\mathcal R_a-i$ 的同一证明，再由对偶与插值覆盖负阶及分数阶。
连范数等价因子，统一可取
$$
 \boxed{\quad
 \|\mathcal C_a-\mathcal C_0\|_{H^s(\mathbb T)^2\to H^s(\mathbb T)^2}
 <2^{50}\epsilon_j,\qquad |s|\le4 .
 \quad}                                                     \tag{C.20}
$$
整个论证在已选实际端角中进行，没有对裸 $C_K-I$ 作同宽小量估计。

## 6. 实际根密度和 normal/shear 的完整再转换

(C.15) 使用固定参考根尺度。现在准确接到已经构造的实际
canonical 根两行，不能只说两种高度相差小。
实际根图在根上满足 $\phi=\theta$，有
$$
 u=\sqrt\alpha\,h,\qquad
 p_{\rm out}=\sqrt\alpha\,
                       (u_\xi-\tfrac12\ell_\xi u).
$$
作实际端角 $\theta=K_e(\eta)$ 后，canonical 高度是
$u\circ K_e$，canonical 通量是 $K_e'u_\xi\circ K_e$。
因此令
$$
 r_e=\sqrt{(\alpha_e\circ K_e)/\alpha_{0,e}},\quad
 L_e=K_e'\,\ell_{\xi,e}\circ K_e,\quad L_e^0=\ell_{0,\xi,e},
$$
实际根 Airy 状态 $Z_h=W(u\circ K_e)$、
$Z_p=W^{-1}(K_e'u_\xi\circ K_e)$ 与 (C.15) 的关系准确为
$$
 \binom{Z_h}{Z_p}
 =\mathcal A_e\binom{Y_h}{Y_p},\qquad
 \mathcal A_e=
 \begin{pmatrix}
 W r_e W^{-1}&0\\
 \tfrac12W^{-1}(L_er_e-r_e^{-1}L_e^0)W^{-1}
                    &W^{-1}r_e^{-1}W
 \end{pmatrix}.
 \tag{C.21}
$$
所有未标成 Fourier multiplier 的量都按真实函数乘法理解。
上右为0并不允许删去显示的下左 shear。该矩阵保持完整高度/
通量 symplectic pairing。

根证明给
$\|\log(\alpha/\alpha_0)\|<2^{20}n_e$ 和
$\|\ell_\xi-\ell_{0,\xi}\|<2^{24}n_e$ 于根附近的实际宽角域。
连同 (C.3) 和真正复合，宽 $1/8$ 上
$\|r_e-1\|\le2^{24}n_e$、
$\|L_e-L_e^0\|\le2^{28}n_e+k_e/16$。
$W$ 的权是至多 $1/3$ 阶，且 $b_e>1$，所以
$$
 {\sqrt{\sigma_{e,m}}\over\sqrt{\sigma_{e,n}}}
 \le(1+|m-n|)^{1/3}.
$$
完整 Fourier 卷积和实际宽 $1/8$ 足以支付 (C.21) 所有
$|s|\le4$ 乘子。安全取
$$
 \|\mathcal A_e-I\|_{H^s\oplus H^s}
 <\delta_e:=2^{80}(n_e+k_e),\qquad
 \|\mathcal A_e^{\pm1}\|<2 .
 \tag{C.22}
$$
这只比较幅度乘子和明确的剪切，未把端角 pullback 隐藏在小差内。

用同一个固定 unitary 把 $\mathcal A$ 转到 incoming/outgoing
两行，写为块 $A_{++},A_{+-},A_{-+},A_{--}$。
原 $a_{\rm out}=\mathcal C_a a_{\rm in}$ 于是变为
$$
 \mathcal C_a^{\,\rm true}
 =(A_{-+}+A_{--}\mathcal C_a)
                 (A_{++}+A_{+-}\mathcal C_a)^{-1}.
 \tag{C.23}
$$
$\|\mathcal C_a\|_{H^s}<2$，分母与恒等的差小于 $3\delta$，
故完整 Neumann 逆存在，且
$$
 \|\mathcal C_a^{\,\rm true}-\mathcal C_0\|_{H^s}
 <2^{50}\epsilon_j+32(\delta_-+\delta_+).
 \tag{C.24}
$$
这是两个根的全部 Airy 高度/flux 行，而非只消去高度后的主符号。

由 (C.3) 的邻胞计数和同一个真实 $N_r$ 和，
$\sum_e(n_e+k_e)<2^{300}\|X\|$；
(C.9)、(C.22)--(C.24) 给
$2^{370}\|X\|+2^{385}\|X\|<2^{400}\|X\|$，证明 (C.1)。
根参考 $\alpha_0\propto1/\rho$，原 $\mathcal N_0\propto1/\rho$，
所以 $P_0=L^*\mathcal N_0L$ 准确消去整体相似尺度；$T_0,W$
也与 $\rho$ 无关。故 $\mathcal C_0$ 是本次已固定新参考的算子，
不随标签暗中改变。

## 7. 完整普通、弱源和 affine Cayley 列

原物理方程写成
$Ph=s_h-\operatorname{div}F$，$s_h=w_{\rm ref}^2JD^{-3/2}e$。
在 (C.5) 的完整角图 $\Xi(t,\eta)=(t,\Phi(t,\eta))$ 后，
准确 Piola 公式是
$$
 \widehat s=\Phi_\eta(s_h\circ\Xi),\qquad
 \widehat F^t=\Phi_\eta(F^t\circ\Xi),\qquad
 \widehat F^\eta=(F^\theta-\Phi_tF^t)\circ\Xi .
 \tag{C.25}
$$
使用 total outward 通量，即 raw outward flux 加
$\widehat F\cdot n$。其完整两端关系是
$$
                         p_{\rm out}^{\,\rm tot}=\mathcal N_af+q_{\mathcal F},
$$
$$
 \langle q_{\mathcal F},g\rangle
 =\int_I\langle\widehat s,H_ag\rangle dt
                 +\int_I\langle\widehat F,\nabla H_ag\rangle dt .
 \tag{C.26}
$$
原零 Dirichlet particular 的能量项与 $H_ag$ 正交，这才是
完整 affine DN source；没有凭空留下或删去该 particular 的端迹。

定义真实有限区间量
$$
 R_I=\int_I\mu_0^{-1}dt,\quad M_I=\int_I A\mu_0dt,\quad
 C_I=1+2\sqrt{R_I}+{1\over4\sqrt{M_I}},\quad
 \Lambda_I={1\over2}
        (\alpha_{0,-}^{-1}+\alpha_{0,+}^{-1})^{1/2}.
 \tag{C.27}
$$
四重 Poincare 和径向 Cauchy--Schwarz 给
$\sup_t\|u(t)\|_2\le C_I(\mathscr E_0(u)+|\lambda(u)|^2)^{1/2}$，
$\lambda(u)=((u_-)_0+(u_+)_0)/2$。
又 $|\lambda(Lz)|\le\Lambda_I\|z\|$、
$\|H_aLz\|_{\mathscr E_0}\le2\langle P_0z,z\rangle^{1/2}$。
故以
$$
 \|\widehat F\|_{\mathscr E_0^*}
 =\left(\int_I\left\langle
       {|\widehat F^t|^2\over\mu_0}
          +{|\widehat F^\eta|^2\over A\mu_0}\right\rangle dt\right)^{1/2}
$$
为实际弱源合同，归一化电荷
$q^\sharp=W^{-1}\alpha_0^{-1/2}q_{\mathcal F}$ 满足
$$
 \|q^\sharp\|_{(P_0+I)^*}
 \le C_I\sqrt{4+\Lambda_I^2}\|\widehat s\|_{L^1_tL^2_\eta}
                         +2\|\widehat F\|_{\mathscr E_0^*}.
 \tag{C.28}
$$
左边表示对 norm
$(\langle P_0z,z\rangle+\|z\|^2)^{1/2}$ 的 dual norm，
不是把 $q^\sharp$ 未经证明地当作 $L^2$ 函数。
在 $A=0$ 处，显示的弱源权需要真正可积；没有授予任意裸
向量源这一性质。

(C.16) 变为 $Y_p=\mathcal R_aY_h+q^\sharp$，准确解得
$$
 a_{\rm out}=\mathcal C_a a_{\rm in}+g_{\mathcal F},\qquad
 g_{\mathcal F}=-\sqrt2(\mathcal R_a+i)^{-1}q^\sharp .
 \tag{C.29}
$$
前节两个 resolvent 的同一能量估计给
$$
 \|g_{\mathcal F}\|_2
 <4\big[C_I\sqrt{4+\Lambda_I^2}\|\widehat s\|_{L^1L^2}
                             +2\|\widehat F\|_{\mathscr E_0^*}\big].
 \tag{C.30}
$$
它包含 mean 电荷：对 raw 两端共同常数测试，
$$
             \langle(q_{\mathcal F})_-+(q_{\mathcal F})_+\rangle
                         =\int_I\langle\widehat s\rangle dt .
 \tag{C.31}
$$
弱源的梯度项在此测试下为0，不能同时把两个 outward mean 设0。
独立平均高度仍由完整 incoming 数据和 (C.15) 恢复。

这些源列也有全频 Sobolev 窗。把输入 norm 中各角 $L^2$ 换成
$H^s$，记相应加权弱范数为 $\mathscr E_0^{*,s}$。
在 (C.19) 的真实复系数条带上，Poisson/source/resolvent
组成的有序算子族有同一 base 能量界的固定倍数。
具体可取 (C.28) 右侧的16倍：复数系数 Dirichlet lift 的
参考能量增益小于2，而完整 form resolvent 到 $\mathcal H$
的增益小于4，均由同一个 $4\epsilon_j<1/2$ 余量支付。
先对固定坐标中的 $\widehat s,\widehat F$ 作此族，再按真实
平移共轭读取 commutator；到6阶的 Cauchy、对偶和插值与第5节
相同。完整共同常数的 $\Lambda_I$ 项保留。因而可取
$$
 \boxed{\quad
 \|g_{\mathcal F}\|_{H^s}
 <2^{60}\left[
 C_I\sqrt{4+\Lambda_I^2}\|\widehat s\|_{L^1_tH^s_\eta}
                  +2\|\widehat F\|_{\mathscr E_0^{*,s}}\right],
 \qquad |s|\le4 .
 \quad}                                                     \tag{C.32}
$$
这里没有因 $s$ 较高而重复使用一份未支付的频率增益。
也没有声称 source 本身是解析函数；系数条带仅用来控制
这些有界算子的 commutator。

回到实际根 Airy 状态 (C.21) 时，affine 列准确乘
$A_{--}-\mathcal C_a^{\,\rm true}A_{+-}$，其 $H^s$ norm 小于4。
若需 bare canonical 通量，而不是 total 通量，还必须另外
提供并减去 $\widehat F^t(t_\pm)$ 的真实端点迹。
(C.28) 的体源范数本身并不提供这两个迹。

普通源 $F=0$ 的原物理单位也明确：在实 $L^2$ 中
$\|\widehat s(t)\|_2<16w_{\rm ref}(t)^2\|e(t)\|_2$。
在 $|s|\le4$ 中，完整 $\Phi$ 的实 $C^6$ composition、
Jacobian 和 $JD^{-3/2}$ 乘子给保守界
$$
 \|\widehat s(t)\|_{H^s}
 <2^{40}w_{\rm ref}(t)^2\|e(t)\|_{H^s}.
 \tag{C.33}
$$
因此 (C.32) 可直接消费原物理 ordinary source，保留实际
$C_I,\Lambda_I,w_{\rm ref}^2$；若改用径向 $L^2$，须对
显示的真实径向权再作 Cauchy--Schwarz。

## 8. 完成的算子权限

这里已从真实正型 form 推出同一个完整根 Airy 平衡空间中的
全频双端算子界和完整源列。无需先估指数大的
$\alpha_m,\beta_m,\delta_m$ 各自大小；它们在 (C.10) 的真实
双端正形式中整体参与，mean 零方向也在 Cayley 中保留。

下一步仍是整个混合网络：把这些完整正块与两侧已经支付的
负型 Cauchy、根图和实际全标签规范共同消元，付其真实强空间
转换与参数/metric-source。最外 cut128、有限 connector、
真实非线性正帽入口和 $F(a,f_*)=0$ 不由 (C.1) 单独解决。

[完整 Cayley/两迹/源与全层预算程序](../scripts/fourfold_positive_full_Airy_Cayley_20261113.py)
及[定向报告](../notes/2026-11-13-R119-positive-full-Airy-Cayley-budget.json)
记录本篇的准确代数、root normal shear 和完整参数费用。
