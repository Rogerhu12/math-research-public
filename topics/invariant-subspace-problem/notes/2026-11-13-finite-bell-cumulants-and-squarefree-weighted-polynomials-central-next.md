# 有限 Bell 累积量的联合解析分支与规范简单根多项式循环性

日期：2026-11-13（UTC）。独占作者：central_next。
状态：已证明的中间结论；root已逐节核验真实联合演算、自然域、低头A因子及Bell因式分解。
前置完整证明：[对称高位反射平均](../results/R236-appendix-symmetric-high-bit-averaging-excludes-canonical-bell-kernels.md)、[任意first指数权](../results/R236-appendix-all-first-exponential-weights-for-canonical-bell-kernels.md)及[R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)。

本稿只推广有明确局部差与高位二次差的有限联合解析系数；不宣称任意 Acal 扰动都可用。
普通 Hilbert ISP 仍未完成。

## 1. 定理

取规范 first
$$
u=\sum_{j\ge0}a_j\chi_j,\qquad a_j=\frac{(-1)^j}{j+1},\qquad a_*=0 .
$$
固定任意复 first 指数权
$$
w=c_*+\sum_{j\ge0}b_j\chi_j,\qquad b\in\ell^2,\qquad
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j).
$$
令 X_b 为 R176 的实际倾斜 first，DomX_b=DomX；令
$$
L_n(v)=\left.\frac{d^n}{dt^n}
\log(\cosh t+v\sinh t)\right|_{t=0},\qquad n\ge2 .
$$
每个 L_n 是标量多项式，L_n(1)=0。
固定有限整数 p≥2，定义实际累积量
$$
G_n=\sum_{j\ge0}a_j^nL_n(R_j)\in\mathcal A,
\qquad 2\le n\le p .
\tag{1.1}
$$
级数按算子范数绝对收敛，全部 G_n 字符为零，因而是交换拟幂零元。

**定理 A。** 对零点邻域中任一固定联合全纯函数
Phi(z_2,...,z_p)，有
$$
\boxed{\ker\bigl(X_b-\Phi(G_2,\dots,G_p)\bigr)=0.}
\tag{1.2}
$$

**定理 B。** 若非零标量多项式 q 的全部根互异，则
$$
\boxed{q(u)e^w\text{ 对实际 }A\text{ 循环}.}
\tag{1.3}
$$
非零常数也包含；一次情形已有 R125/R147。
本定理允许根之间恰好相差 2，故不依赖旧 R144 的首位平移互素条件。
它没有将含重根的所有多项式自动纳入。

## 2. 联合函数演算及实际范数差商

记 d=p−1。取零点附近闭多圆盘，使 Phi 在其邻域全纯；
为简记取所有坐标半径为 rho>0。
每个 G_n 的谱为 {0}，所以其围道 Gamma_n={|z_n|=rho} 都在真实预解集中。
定
$$
R_\Gamma=\max_{2\le n\le p,\ |z|=\rho}\|(z-G_n)^{-1}\|,
\qquad M_\Phi=\max_{\Gamma_2\times\cdots\times\Gamma_p}|\Phi|.
$$
真实联合函数值定义为
$$
\Phi(G)=\frac1{(2\pi i)^d}
\int_{\Gamma_2\times\cdots\times\Gamma_p}
\Phi(z)\prod_{n=2}^p(z_n-G_n)^{-1}\,dz_2\cdots dz_p .
\tag{2.1}
$$
此值属于 Acal。有限个交换拟幂零元允许任何零点邻域的解析芽：
等价 Taylor 级数在算子范数绝对收敛，因为每个 G_n 的幂对任意 epsilon>0
都满足 ||G_n^k||≤C_(n,epsilon)epsilon^k。

若另一交换元组 widehat G 满足
||widehat G_n−G_n||≤(2R_Gamma)⁻¹，
则其各预解式在同一圆周上至多 2R_Gamma。
若 gamma 是酉共轭，则 gamma G 的圆周预解式仍至多 R_Gamma。
逐因子相减 (2.1) 的预解式乘积，得到
$$
\|\Phi(\widehat G)-\Phi(G)\|
 \le C_\Phi\sum_{n=2}^p\|\widehat G_n-G_n\|,
$$
$$
\|\Phi(\widehat G)-\Phi(\gamma G)\|
 \le C_\Phi\sum_{n=2}^p\|\widehat G_n-\gamma G_n\|,
\tag{2.2}
$$
其中可取
$$
C_\Phi=2^d\rho^dM_\Phi R_\Gamma^{d+1}.
\tag{2.3}
$$
第二式不要求 widehat G 与 gamma G 的不同元组互相交换；
固定乘积次序的望远镜恒等式及单个有理逆差已足够。
每个元组内部的交换性只用于定义各自联合演算。

## 3. 任意 r 元高位反射的统一估计

沿用指数倾斜稿中已逐分母支付的常数
$$
L=\max(1,\sup_j|t_j|,\sup_j|t_j|^{-1}),\qquad
R=\sup_{j,\ s=\pm1}\|(I+s t_jN_j)^{-1}\|,
$$
$$
V=2R+1,\qquad C_V=2LR^2 .
$$
L、R 都有限；低位分别用真实拟幂零逆，高位用
N_j²=η_jN_(j+1)、η_j→0。
所有 ||V(s t_jN_j)||≤V。

写 L_n(v)=Σ_k ell_(n,k)v^k，定
$$
M_n=\sum_k|\ell_{n,k}|V^k,\qquad
D_n=\sum_{k\ge1}k|\ell_{n,k}|V^{k-1}.
\tag{3.1}
$$
于是范数≤V 的 U、W 满足
||L_n(U)||≤M_n、
||L_n(U)−L_n(W)||≤D_n||U−W||，
由每个单项式的有限望远镜求和证明，不要求 U、W 交换。

令
$$
m=\lceil e^{r^2}\rceil,\quad q=r^4,\quad
I_r=\{m,\dots,m+q-1\},\quad |F|=r,\quad F\subset I_r .
$$
J_F=∏_{j∈F}M_(chi_j)、gamma_F=AdJ_F；s_j=-1 对 j∈F，否则 1。
实际递归统一给
$$
\|\gamma_F(N_k)-s_kN_k\|\le
\begin{cases}
2\alpha_m/\alpha_k,&k<m,\\
2\eta_k,&m\le k<m+q,\\
0,&k\ge m+q.
\end{cases}
\tag{3.2}
$$
窗口未选位置也含在第二行；Σ_{k≥m}barη_k≤2barη_m。
同时
||V(t_k gamma_F(N_k))−V(s_kt_kN_k)||≤C_V||(gamma_F(N_k)−s_kN_k)||。

定义
$$
\widehat X_F=X_b+\sum_{j\in F}a_j
 \bigl(V(-t_jN_j)-V(t_jN_j)\bigr),
$$
$$
\widehat G_{n,F}=G_n+\sum_{j\in F}a_j^n
 \bigl(L_n(V(-t_jN_j))-L_n(V(t_jN_j))\bigr).
\tag{3.3}
$$
这些 widehat G 都在 Acal，字符仍为零。由 (3.1)，
$$
\|\widehat G_{n,F}-G_n\|
\le\frac{2M_nr}{(m+1)^n}
\le\frac{2M_nr}{(m+1)^2}\longrightarrow0 .
\tag{3.4}
$$
所以 (2.2) 的全部预解式界统一适用于充分大的 r、所有 F。

令 Y=Phi(G)、widehat Y_F=Phi(widehat G_F)、
T=X_b−Y，并定义
$$
A_F=(\widehat X_F-\widehat Y_F)-T,\qquad
E_F=\gamma_F(T)-(\widehat X_F-\widehat Y_F),\qquad
P_F=4\sum_{j\in F}a_jt_jN_j .
\tag{3.5}
$$
A_F∈Acal 且与 T 完整交换。
按 (3.2) 的真实 carry 和 (3.1) 的差商求和，
$$
\|\gamma_F(G_n)-\widehat G_{n,F}\|
\le8D_nC_V\bar\eta_{m-1}.
\tag{3.6}
$$
这里 |a_k|≤1，故各 n 次系数的低头/尾和都由指数倾斜稿相同的和控制。

结合 (2.2)，可取
$$
C_E=8C_V\left(1+C_\Phi\sum_{n=2}^pD_n\right),
\qquad
C_A=8L^3+2C_\Phi\sum_{n=2}^pM_n,\qquad K=4L+1,
$$
使充分大 r 时
$$
\boxed{
\|E_F\|\le C_E\bar\eta_{m-1},\qquad
\|A_F-P_F\|\le\frac{C_Ar}{(m+1)^2},\qquad
\|A_F\|\le\frac{Kr}{m+1}.
}
\tag{3.7}
$$
X 的线性根式余项仍由 8L³rbarη_m/(m+1) 控制，
选充分大 m 后纳入所写二次界。
所有常数只依赖固定 b、p、Phi。

## 4. 输出强逼近的完整域和全部误差

取 ell=m+q−1，令 X_(b,>ell)=X_b−Σ_{j≤ell}a_jR_j。
有限柱是真实图核心。先在核心上与任意前 ell+1 位局部矩阵交换，
再由闭性延拓，给完整闭尾域交换。
所有 Acal 元素同样保持该域，并与尾 first 交换。

E_F 的具体表达是有限个 gamma_F(R_k)−V(s_kt_kN_k)，
再加 gamma_F(Y)−widehat Y_F。
因此 E_F 保域并与 X_(b,>ell) 完整交换。
置
$$
d_r=2\left\|\sum_{j\le\ell}a_jR_j-Y\right\|=O_{b,\Phi}(r^2).
$$
全部嵌套交换子保域且
||ad_T^s E_F||≤d_r^s C_E barη_(m−1)。

M=kerT 上，Q_0=I、
Q_(n+1)=ad_T Q_n−Q_n(A_F+E_F) 的递推同时给
J_FM⊂DomT^n 及真实自然幂公式。
同一加权非交换单词计数给
$$
\|T^rJ_Ff-(-A_F)^rJ_Ff\|
\le(r+1)!C_E\bar\eta_{m-1}
(1+\|A_F\|+d_r)^r\|f\|.
\tag{4.1}
$$

用准确倾斜权
$$
p_{F,b}=\prod_{j\in F}a_jt_j,\qquad
\mathcal B_{r,b}=\frac1{(-2q)^r}\sum_{|F|=r}p_{F,b}^{-1}J_F .
$$
有
$$
\|\mathcal B_{r,b}\|
\le \frac{L^r(m+q)^r}{2^rr!}
\le\frac{L^re^{r^3}}{r!}.
\tag{4.2}
$$
由 (3.7)，逐项求和的四类误差分别不超过固定常数乘
$$
(r+1)\bar\eta_{m-1}
\left(\frac{L(m+q)O(r^2)}2\right)^r,
$$
$$
\frac{C_Ar}{K(m+1)}
 \left(\frac{KLe}{2}\right)^r e^{rq/m},
\qquad
\bar\eta_m(2eL^2)^r e^{rq/m},
\qquad
2^rr\bar\eta_m .
\tag{4.3}
$$
它们依次来自非交换误差、A_F^r→P_F^r、重复 N_j 指标、
以及 (∏N_j)J_F→∏E_j。
每一项都趋零；没有留下未支付的 r 次归一化系数。

准确主项仍为
$$
C_{m,q}^r,\qquad C_{m,q}=\frac2q\sum_{j=m}^{m+q-1}E_j .
$$
其有限占据层范数给 ||C_(m,q)||≤1+1/q，
有限柱上 ||(C_(m,q)−I)v||=q^(−1/2)||v||，
所以 C_(m,q)^r→I 强，范数一致≤e。
于是
$$
\boxed{
\mathcal B_{r,b}M\subseteq\operatorname{Dom}T^r,\qquad
T^r\mathcal B_{r,b}f\longrightarrow f\quad(f\in M).
}
\tag{4.4}
$$
仅使用原 Haar 强平均，没有假设核向量的尾速率。

## 5. 联合函数的有限低头差有明确 A 因子

固定局部矩阵 D，支撑在位 h 以前。
定义 G_(n,≥h) 为 (1.1) 的 j≥h 尾和，
Y_(≥h)=Phi(G_(2,≥h),...,G_(p,≥h))，以及
$$
Z_h=X_{b,\ge h}-Y_{\ge h}+\left(\sum_{j<h}a_j\right)I,
$$
$$
K_h=\sum_{j<h}a_j(R_j-I)-(Y-Y_{\ge h}).
\tag{5.1}
$$
则 T=Z_h+K_h 于完整域上成立。
Z_h 只作用物理尾，D 与其完整交换；K_h∈Acal 保域、与 Z_h 完整交换。

因 L_n(1)=0，写 L_n(v)=(v−1)tilde L_n(v)。
有限低头差有准确有界分解
$$
G_n-G_{n,\ge h}=A U_{n,h},
$$
$$
U_{n,h}=-2\sum_{j<h}\frac{a_j^nt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1}\widetilde L_n(R_j)\in\mathcal A .
\tag{5.2}
$$
first 低头差也有
$$
\sum_{j<h}a_j(R_j-I)=A U_{1,h},\qquad
U_{1,h}=-2\sum_{j<h}\frac{a_jt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1}.
$$

本节两个元组全部在同一个交换代数中。
对 (2.1) 的预解式乘积逐坐标相减，实际有限差商积分给
$$
Y-Y_{\ge h}
=\sum_{n=2}^p(G_n-G_{n,\ge h})D_{n,h},
\qquad D_{n,h}\in\mathcal A .
\tag{5.3}
$$
具体地，D_(n,h) 的积分中，第 n 因子是
(z_n−G_n)⁻¹(z_n−G_(n,≥h))⁻¹，
小于 n 的坐标取完整 G，大于 n 的坐标取尾 G，乘同一个 Phi(z)；
所有圆周都避开 {0}，所以固定 h 时界有限。
这是真实有界差商，未从零字符自动除 A。

因此
$$
\boxed{K_h=A U_h,\qquad
U_h=U_{1,h}-\sum_{n=2}^pU_{n,h}D_{n,h}\in\mathcal A.}
\tag{5.4}
$$
实际四次幂界随即给
$$
\boxed{
\|\operatorname{ad}_T^rD\|
=\|\operatorname{ad}_{K_h}^rD\|
\le\|D\|(2\|U_h\|)^r
e^{-(5/6)r^4+105r^3}.
}
\tag{5.5}
$$
完整一阶域交换与所有有界嵌套交换子逐次归纳，
同时付清 D 及所有 ad_T^kD 保持每个自然幂域。

## 6. 配对排核，完成定理 A

T=X_b−Y 是真实 C 自伴，因为 Y∈Acal 有界。
对 f,g∈M，由完整 Leibniz 域等式，
$$
B(DT^r\mathcal B_{r,b}f,g)
=(-1)^rB((\operatorname{ad}_T^rD)\mathcal B_{r,b}f,g).
$$
所有低阶项的正次 T 移到 g 后为零。
右端用 (4.2)、(5.5) 不超过
$$
\frac{\|D\|(2L\|U_h\|)^r}{r!}
e^{-(5/6)r^4+106r^3}\|f\|\|g\|\longrightarrow0 .
$$
左端由 (4.4) 趋于 B(Df,g)，故对任意固定有限局部矩阵 D，
B(Df,g)=0。

实际 Haar 有限局部 *-代数不可约：前 h 位参考态投影强趋于 1 的秩一投影，
再用局部代数作用于 1 的稠密性，排其交换子中的非平凡投影。
所以每个非零 f 的局部矩阵轨道稠密。
取 g=f，B(Df,f)=0 迫 Cf=0。
因此 M=0，定理 A 成立。

## 7. 真实 Bell 多项式的简单根解析分解

设 q 为次数 p 的非零标量多项式，首系数 q_p≠0，根
lambda_1,...,lambda_p 互异。
令 beta_k(kappa_2,...,kappa_p) 是定义于
$$
\exp\left(\sum_{n=2}^p\kappa_n\frac{t^n}{n!}\right)
=\sum_{k=0}^p\beta_k(\kappa)\frac{t^k}{k!}+O(t^{p+1})
$$
的有限多项式：beta_0=1、beta_1=0。
定义标量系数的联合解析多项式
$$
\mathcal P_q(z;\kappa)=
\sum_{k=0}^p\frac{\beta_k(\kappa)}{k!}q^{(k)}(z).
\tag{7.1}
$$
其首系数是 q_p，
mathcal P_q(z;0)=q(z)。

每个根 lambda_l 都简单，故零点邻域上存在联合全纯根
Phi_l(kappa)，满足 Phi_l(0)=lambda_l。
可以选互不相交的小圆包围各 lambda_l；
当 kappa 足够小时，每个圆恰包一根，并用
(2πi)⁻¹∮ z ∂_z mathcal P_q(z;kappa)/mathcal P_q(z;kappa) dz
给出该全纯函数。
因此在同一个零点多圆盘上有精确标量恒等式
$$
\mathcal P_q(z;\kappa)=q_p
\prod_{l=1}^p(z-\Phi_l(\kappa)).
\tag{7.2}
$$

R176 的倾斜 Bell 生成函数满足
$$
\log\mathcal B_b(t)=\sum_{n\ge2}G_n\frac{t^n}{n!}.
$$
取到 p 阶，得到其实际闭点态多项式
$$
P_{q,b}(X_b)=\sum_{k=0}^p
\frac{\beta_k(G)}{k!}q^{(k)}(X_b)
=\mathcal P_q(X_b;G).
\tag{7.3}
$$
把 (7.2) 在交换拟幂零元组 G 上作真实联合演算：
$$
\boxed{
P_{q,b}(X_b)=q_p\prod_{l=1}^p(X_b-Y_l),
\qquad Y_l=\Phi_l(G)\in\mathcal A .
}
\tag{7.4}
$$
各 Y_l 有界、两两交换并与 X_b 完整交换。
有限有界交换扰动的自然幂归纳保证该乘积的准确域为 DomX_b^p；
也可直接用 R176 的同域自然多项式结论。
没有把仅形式因式分解用于更大域。

定理 A 分别给每个 X_b−Y_l 单射。
所以 (7.4) 在其自然域上的有限乘积单射。
R176 已证明 P_(q,b)(X_b) 在此域 C 自伴，并给
$$
q(u)e^w=P_{q,b}(X_b)\xi_w,\qquad
[q(u)e^w]_A=\overline{\operatorname{Ran}P_{q,b}(X_b)}.
$$
单射与 C 自伴给像稠密，完成定理 B。

## 8. 准确范围与仍在的重根障碍

本稿覆盖任意固定简单根 q，次数不设统一上限，并容许任意复 ell² first 指数权。
常数可以随 q、b 变；没有声称对次数取无穷时仍有统一预算。

R144/R147 原有的首位平移互素判据仍独立覆盖许多含重根 q，
包括全部单根位置的点态幂。不能只由简单根多项式逼近就推出全部重根情形，
因为循环向量类不对 H 范数极限封闭。
当 scalar q 有重根时，(7.1) 的根支未必是 kappa 的联合全纯函数；
Puiseux 形式根、非交换 companion 矩阵或未知子空间上的根不能直接代入定理 A。

一般正常湮灭者、两个边界 N=M、任意慢行的所有 Bell 分支以及完整普通 ISP
均未由本稿关闭。

## 并行稿对照

同一检查点的并行R259源稿 `3ce94764c48a800a50733b393dae817ae500fb45` 将相同机制推广到双侧同幂慢尾（任意复相位、幂次大于1/2），范围更广。本稿保留规范行的独立逐项常数与域核验；不把两次证明计算为两个独立新接口，也不据此覆盖混合重根。
