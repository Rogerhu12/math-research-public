# R119 续篇：全部 Sym2 的有限阶多项式分离与真实正定控制

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 对当前受控尾的每个真正未使用 quartic 区间，
本篇把全部对称平方态的控制下界改为显式多项式下界。
证明不从 rank-one 情形推断正定性，也不使用随 $M$ 指数增长的
复域 Cauchy 传播。核心是对真实核的三阶方程作有限次数的多项式
消元。常数刻意宽松，但对所有 $M\in4\mathbb N$ 统一有效，
不要求第56束的高振荡条件。

这是径向完整二维散射的新输入，未据此授予非径向多频簇的正定性、
原标签同权 Green 或整个非线性 $\mathcal F=0$。

## 1. 同一个真实区间、中心规范与全部二次型

使用[全部二次型控制](R119-supplement-all-quadratic-phase-preserving-positive-scattering-control.md)
的当前深尾 $j\ge8193$、$a_r,\Delta,B,K_j$，其中
$$
 0<a_r<1,\quad \Delta>80,\quad B=\Delta/a_r>2^{190},
 \quad K_j=2^{6000}(j+5)^8\delta_j^{-16}.
$$
取任意闭区间 $I\subset[7/16,15/32]$，长度 $\ell>0$，中心为 $c$。
所有旧 compact 方向及两个补偿 bump 离开 $I$ 的一个邻域；因此
这个邻域中的当前 profile 准确为
$$
 Q(x)=7+30Bx^2(1-x)^2,\quad dt=a_r\,dx,\quad
 \mu_t/\mu=-1-Q .                                      \tag{P.1}
$$
取 $\lambda=M^2$、$M\in4\mathbb N$，$k=\sqrt{7\lambda-16}$。
两条实际基本解在 $c$ 使
$Y=(\sqrt k\sqrt\mu h,(\sqrt\mu h)_t/\sqrt k)$
的 fundamental matrix 为单位阵。

对任意实 $A=A^T$、$\|A\|_F=1$，令
$$
 \begin{pmatrix}X&Y_b\\Y_b&Z\end{pmatrix}
 =\mu\begin{pmatrix}h_1&h_2\\(h_1)_t&(h_2)_t\end{pmatrix}
 A\begin{pmatrix}h_1&h_2\\(h_1)_t&(h_2)_t\end{pmatrix}^{T},
 \qquad K_A=Z-2\lambda Y_b+\lambda X .                  \tag{P.2}
$$
$A$ 可以不定。以下不使用 $X,Z\ge0$。
真实的两 phase 核都属于
$\{P/Q^{9/2}:\deg P\le19\}$；本篇方向将准确消去这个完整空间。

本篇首先证明
$$
 \boxed{\quad
 \sup_I\left|\partial_x^{20}(Q^{9/2}K_A)\right|
 \ge\epsilon_{\rm pol}:=
       2^{-1280}a_r\ell^{41}B^{-40}\lambda^{-8}.\quad}
 \tag{P.3}
$$
根上的 $Q^{9/2}$ 仅在实区间取正支；下文在复根使用的是一个
真正的多项式，不假设这个分支延拓穿过根。

## 2. 完整核的真实三阶方程

记 $s=1+Q$、$b=2\lambda(\lambda-1)$。原完整对称平方方程给
$$
 (K_A)_t=(s-2\lambda)K_A-bX_t,\qquad
 (K_A)_{tt}+[4\lambda Q-s^2-Q_t]K_A=bQ_tX .             \tag{P.4}
$$
对第二式求导，代入第一式消去 $X_t$，再用第二式消去 $X$。
乘以 $Q_t$ 后全部分母消失，改回真实 $x$，令 $V=4\lambda Q-s^2$：
$$
 \mathscr LK:=(Q'K'''-Q''K'')
 +a_r^2Q'VK'
 +a_r^2[3(2\lambda-s)(Q')^2-Q''V]K=0 .                  \tag{P.5}
$$
这是全部 $A$ 的恒等式；本篇 prime 只表示 $x$ 导数。

置 $g=Q^{9/2}K_A$。对任意光滑 $P$ 定义
$$
 \mathscr DP=Q^{15/2}\mathscr L(P/Q^{9/2})
             =A_3P'''+A_2P''+A_1P'+A_0P,               \tag{P.6}
$$
其中准确系数为
$$
 \begin{split}
 A_3={}&Q'Q^3,\\
 A_2={}&-\tfrac{27}{2}Q^2(Q')^2-Q^3Q'',\\
 A_1={}&\tfrac{297}{4}Q(Q')^3-\tfrac92Q^2Q'Q''
                                      +a_r^2Q'VQ^3,\\
 A_0={}&-\tfrac{1287}{8}(Q')^4+\tfrac{99}{2}Q(Q')^2Q''
       -\tfrac92Q^2Q'Q'''+\tfrac92Q^2(Q'')^2\\
 &+a_r^2[-\tfrac92(Q')^2VQ^2
              +3(2\lambda-s)(Q')^2Q^3-Q''VQ^3].
 \end{split}                                               \tag{P.7}
$$
所以 $\mathscr Dg=0$ 在整个实 $I$ 上成立。
$A_3,A_2,A_1,A_0$ 的次数至多分别为 $15,14,23,22$。
特别 $\deg P\le19$ 时，$\deg(\mathscr DP)\le41$。

## 3. 从真实二十阶导数到有限次数残差

令 $F=\sup_I|g^{(20)}|$，取中心的真正十九阶 Taylor 多项式
$$
 P(x)=\sum_{r=0}^{19}\frac{g^{(r)}(c)}{r!}(x-c)^r,
 \qquad R=g-P .
$$
对 $0\le r\le3$，积分余项准确给
$$
 \sup_I|R^{(r)}|\le\frac{\ell^{20-r}}{(20-r)!}F\le F .     \tag{P.8}
$$
没有从一个未经支付的复解析 norm 估计真实解。
在实 $I$ 上，$Q<2B$、$|Q^{(r)}|<2^{10}B$（$1\le r\le4$）、
$|V|<2^5\lambda B^2$，所以 (P.7) 的系数绝对和小于
$2^{80}\lambda B^6$。于是多项式
$$
 H=\mathscr DP=-\mathscr DR,\qquad \deg H\le41,\qquad
 \sup_I|H|<2^{80}\lambda B^6 F .                         \tag{P.9}
$$
对次数至多41的多项式，用 $I$ 上42个等距点作完整 Lagrange
插值。在 $|z|\le3$ 上分子距离小于4，节点间距为 $\ell/41$。
完整权和为
$$
 4^{41}(41/\ell)^{41}
          \sum_{r=0}^{41}\frac1{r!(41-r)!}
 =\frac{(8\cdot41)^{41}}{41!}\ell^{-41}
 <2^{400}\ell^{-41}.                                   \tag{P.10}
$$
所以在每个 $|z|<2$ 点的半径1圆盘，Cauchy 只作用于这个次数固定的
多项式。前四个归一 jet 均满足
$$
 \max_{0\le l\le4}\frac{|H^{(l)}(z)|}{l!}
 <H_*:=2^{480}\ell^{-41}\lambda B^6 F .                 \tag{P.11}
$$
本步的次数固定，未出现 $\exp(CM)$。

## 4. 四个真实复根的有限三角消元

写 $e=\sqrt{7/(30B)}$。四根来自 $x(1-x)=\pm ie$。
以 $\sqrt{1+4ie}=u+iv$ 的正实部分支表示，有
$u\ge1,u<2,|v|=2e/u\ge e$。故四根满足
$$
 |z_i|<2,\qquad |z_i-z_k|\ge\sigma:=2^{-4}B^{-1/2}\quad(i\ne k),
$$
$$
 |Q'(z_i)|=60Be|1-2z_i|\ge\sqrt{840B}>16\sqrt B .        \tag{P.12}
$$
相邻的两根距离是 $|v|$，另两组的实部间距至少1；
这些是真正 quartic 根界，不依赖浮点根搜索。

在任一根 $z_i$ 展开 $P,H$，用归一 jet
$p_l=P^{(l)}(z_i)/l!$、$h_l=H^{(l)}(z_i)/l!$。
因为 $A_j$ 在该根至少消去 $j$ 阶，$h_l$ 只依赖
$p_0,\ldots,p_l$。第 $l$ 个对角系数准确为
$$
 (Q'(z_i))^4
 (l-\tfrac92)(l-\tfrac{11}2)(l-\tfrac{13}2).             \tag{P.13}
$$
对 $0\le l\le4$，后三因子绝对值依次为
$1287/8,693/8,315/8,105/8,15/8$，所以对角模大于 $2^{16}B^2$。

在 $|z|\le3$ 用 $|Q^{(r)}|<2^{14}B$、
$|V|<2^{32}\lambda B^2$，(P.7) 的每个系数小于
$2^{128}\lambda B^6$。半径1 Cauchy 给根上所需前四归一 jet。
组合 $P^{(j)}$ 时最多20项，每项 factorial 比至多24，
所以每个低三角系数小于 $2^{138}\lambda B^6$。
逐行除以真实对角：
$$
 |p_l|\le H_*+2^{122}\lambda B^4\sum_{r<l}|p_r|.
$$
因此所有四根上
$$
 \boxed{\quad
 \max_{i,0\le l\le4}|p_l|
 <2^{512}\lambda^4B^{16}H_*
 =2^{992}\ell^{-41}\lambda^5B^{22}F .\quad}              \tag{P.14}
$$
这里只解四个有限三角系统。没有将 $K_A$ 延拓到根，也没有为
$Q^{9/2}$ 选一条穿过 branch point 的路径。

## 5. 完整20维 Hermite 与中心可观测性

设 $P_*$ 为 (P.14) 右端。写
$H_i(z)=\prod_{k\ne i}(z-z_k)^5$。
在 $|z-z_i|=\sigma/2$ 上，$|H_i|\ge(\sigma/2)^{15}$；
故 $1/H_i$ 的前四归一 Taylor 系数不超过 $(2/\sigma)^{15+l}$。
完整 Hermite 恒等式是
$$
 P(z)=\sum_{i=1}^4H_i(z)\,
             \operatorname{Taylor}_{4,z_i}(P/H_i)(z).
$$
两边差次数至多19且有20个含重数零点，故准确为0。
对 $|z|\le2$，每个距离小于4，完整求和给
$$
 \sup_{|z|\le2}|P(z)|
 \le2^{64}\sigma^{-19}P_*\le2^{140}B^{10}P_* .           \tag{P.15}
$$
在 $c$ 用半径1多项式 Cauchy，且 $P^{(r)}(c)=g^{(r)}(c)$
对 $r\le19$ 准确成立，得到
$$
 \max_{0\le r\le2}|g^{(r)}(c)|
 <2^{1133}\ell^{-41}\lambda^5B^{32}F .                  \tag{P.16}
$$

最后必须使用真实中心态。到 $(\sqrt\mu h,\sqrt\mu h_t)$ 的矩阵
$$
 R_c=\begin{pmatrix}k^{-1/2}&0\\(1+Q(c))/(2\sqrt k)&\sqrt k\end{pmatrix}
$$
行列式为1，两向 norm 的平方均小于 $16B^2\lambda$。于是
$$
 \max(|X(c)|,|Y_b(c)|,|Z(c)|)>(32B^2\lambda)^{-1}.        \tag{P.17}
$$
在真实 $[7/16,15/32]$ 上 $B/2<Q'(c)<2B$。
用 (P.4) 解 $X$，再用
$X_t=((1+Q-2\lambda)K-K_x/a_r)/b$、
$2Y_b=X_t+(1+Q)X$、$Z=K+\lambda X_t+\lambda QX$，得
$$
 \max(|X|,|Y_b|,|Z|)
 <2^{12}a_r^{-1}\lambda B^2\max(|K|,|K_x|,|K_{xx}|).
$$
故
$$
 \max(|K|,|K_x|,|K_{xx}|)
                    >2^{-20}a_rB^{-4}\lambda^{-2}.      \tag{P.18}
$$
再以 $Q\ge1$、$|Q'/Q|<2$、$|Q''/Q|<32$ 微分
$K=Q^{-9/2}g$ 两次，完整系数和小于 $2^9$。保守地有
$$
 \max_{0\le r\le2}|g^{(r)}(c)|
                    >2^{-50}a_rB^{-4}\lambda^{-2}.      \tag{P.19}
$$
(P.16)、(P.19) 给
$F>2^{-1183}a_r\ell^{41}B^{-36}\lambda^{-7}$，从而证明 (P.3)。

## 6. 真实二十一阶上界与实际 compact 方向

原真实正反 Cauchy 门 $K_j$ 控制中心单位 wave state 在 $I$ 上的两解。
令 $u=\sqrt\mu h$、$U=(u,u_t)$，其准确 $x$ 系统为
$$
 U_x=\begin{pmatrix}0&a_r\\
 -a_r\lambda Q-Q'/2+a_r(1+Q)^2/4&0\end{pmatrix}U .       \tag{P.20}
$$
系数是次数至多8的多项式，至8阶归一 jet 均小于
$L=2^{40}\lambda B^2$。每个真实点有 $|U|<2\lambda K_j$。
归一 Taylor 递推
$(r+1)U_{r+1}=\sum_{l=0}^{\min(8,r)}A_lU_{r-l}$
给 $|U_r|\le(4L)^r|U_0|$。
$0\le r\le22$ 时 $r!<2^{70}$，所以
$$
 \sup_I|U^{(r)}|<2^{1024}\lambda^{24}B^{48}K_j .
$$
没有 $a_r^{-1}$ 的虚假费用，因为用了真实 $(u,u_t)$。

准确核是
$u_t^2+(1+Q-2\lambda)uu_t+
 ((1+Q)^2/4-\lambda Q)u^2$；
一般 $A$ 按两个实谱方向相加。完整 Leibniz 至21阶给
$2^{2200}\lambda^{49}B^{98}K_j^2$。
每个实点半径1/8复盘上，$Q/B$ 的正支无零，
$|(Q/B)^{9/2}|<2^{20}$，至21阶 Cauchy 费小于 $2^{153}B^5$。
再作完整 Leibniz，可安全取
$$
 \boxed{\quad
 \sup_I|g^{(21)}|<G_*:=2^{4096}B^{128}\lambda^{64}K_j^2 .\quad}
 \tag{P.21}
$$
复盘只估计显式 $Q^{9/2}$ 系数，没有用于传播未知解。

统一取
$$
 \rho=\frac{\epsilon_{\rm pol}}{16G_*}
 =2^{-5380}a_r\ell^{41}B^{-168}\lambda^{-72}K_j^{-2}<\ell/8 .
 \tag{P.22}
$$
在 $|g^{(20)}|\ge\epsilon_{\rm pol}$ 的真实见证附近，若靠近端点则
向内移动至多 $2\rho$，取新中心 $x_0$ 的半径 $\rho$。
整个支集上 $g^{(20)}$ 同号，模大于 $\epsilon_{\rm pol}/2$，
并且支集严格内含 $I$。定义
$$
 b(s)=(1-s^2)_+^{30},\quad f_0(x)=\rho^{24}b((x-x_0)/\rho),
$$
$$
 \psi_A=\frac{\operatorname{sign}(g^{(20)}(x_0))}
                    {2^{220}B^5}\,Q^{9/2}f_0^{(20)} .    \tag{P.23}
$$
它是实际 $C^9$ 紧支函数。$Q^{9/2}$ 前四导数小于 $2^{37}B^5$，
$b$ 至24阶导数小于 $2^{174}$，所以
$$
 \sum_{r=0}^4\|\psi_A^{(r)}\|_\infty<1,\qquad
 \|\psi_A^{(r)}\|_\infty\le\rho^{4-r},\quad
 \|\psi_A^{(r)}\|_{L^1(dx)}\le2\rho^{5-r}.               \tag{P.24}
$$
二十次分部积分准确消去每个 $P/Q^{9/2}$、$\deg P\le19$；
也给带原测度的严格正 pairing
$$
 \int_I K_A\psi_A\,dt
 >2^{-236}a_r B^{-5}\epsilon_{\rm pol}\rho^{25}>d_{\rm pol},
$$
$$
 \boxed{\quad
 d_{\rm pol}=2^{-140000}a_r^{27}\ell^{1066}
                      B^{-4245}\lambda^{-1808}K_j^{-50}>0 .\quad}
 \tag{P.25}
$$
未取整二进制费用为 $236+1280+25\cdot5380=136016$。
真实 $dt=a_rdx$ 和全部 $B^5$ 规范均在式中。

## 7. 同一个方向控制完整二维 complex scattering

定义中心对称矩阵 $\mathcal L\psi$，使
$\operatorname{tr}(A\mathcal L\psi)=\int K_A\psi\,dt$。
(P.25) 对每个 Frobenius 单位 $A$ 给 support function 下界
$d_{\rm pol}$；admissible 方向集合关于取负对称、凸。
用原完整有限球面网证明及三维 Carathéodory 定理，至多四个实际
方向的凸组合可给
$$
 \boxed{\qquad \mathcal L\psi_+=(d_{\rm pol}/4)I_2 .\qquad} \tag{P.26}
$$
仍支持在同一未使用 $I$，$C^4$ sum norm 至多1，准确消去两 phase。
每个组分的统一 $\rho$ 也相同。原两 bump 的一阶补偿为0；
有限参数位移仍通过原完整补偿图。

对真实完整二维 unitary scattering，原 Green identity 给
$$
 \boxed{\qquad -iS^*DS[\psi_+]\ge
                    \frac{d_{\rm pol}}{8K_j^2}I_2 .\qquad} \tag{P.27}
$$
这保留两个 incoming 端口，对复杂数据的实部、虚部分别消费
(P.26)，不假设 eigenphase 简单或有邻谱间隙。
中心归一保证所有 $I$ 外既有允许控制统一有效。

对 band $M\in[U/2,U]$，用 (P.25) 在 $M=U$ 的共同下界。
真实 matrix Hessian $H_G=2^{30}K_j^4(U+B)^2$ 仍覆盖这些
$C^4$ 单位方向，包含两个完整补偿 bump。于是原 band 盒中
$$
 r_n=\min\{2^{-n-80},d_{\rm pol}/[2^{36}K_j^6(U+B)^2]\},
 \qquad D_{j,M}=r_nd_{\rm pol}/(16N_{\rm band}K_j^2)      \tag{P.28}
$$
给整个盒上的正定 generator 下界。这把原指数型 $d$ 替换为已证的
多项式型 $d_{\rm pol}$，未改变 $\zeta_j,h_j$、profile 或 good-angle。

## 8. 完整源和当前还缺的非径向消费

这里 $M\ne0$；独立 mean 仍使用原完整 mean 电阻/holonomy 行。
compact profile 改变 mean 电阻与参考高度，不因两 phase-annihilator
而消失。第61束完整 Hamiltonian 核、actual 背景响应、
ordinary/weak 仿射源适用于本篇方向，仍保两个 bare/total 端荷。

(P.27) 是径向完整二维结论，优于只对每个实共振解非零。
它不说明同一方向在非径向完整频率矩阵上仍正定。
第62束的真实 $\rho^5$ 误差不能直接除以 (P.25) 的
$\epsilon_{\rm pol}\rho^{25}$；下一步要比较完整 kernel 的二十阶
结构，或在实际近共振簇上构造相应多参数控制。
原全空间源权和全网络同权重建没有在本篇自动付清。

[新有限阶代数程序](../scripts/fourfold_polynomial_all_sym2_profile_control_20261114.py)
及[实际执行记录](../notes/2026-11-14-R119-polynomial-all-sym2-profile-control-budget.json)
保存三阶消元、四个对角 indicial 值、固定次数、有理费用及最终幂。
