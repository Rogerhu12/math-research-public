# R150 附录：一般复多模式的完整矩阵池与普通点态多项式循环性

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d；AI-assisted，GPT-6 Astra Pro。
状态：已证明；root 与 kernel 全文独立核查。一般无池行与任意向量不在结论范围。

本稿把[临界双模式全多项式稿](R150-appendix-critical-logarithmic-two-mode-full-polynomials-and-zero-parameters.md)的核内正则化与矩阵提升扩展到任意固定有限个复平方可和行。
原始输入来自 [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)、[R236 的准确普通矩逆](R236-appendix-ordinary-pointwise-moment-expansion-and-veronese-pools.md)、[R236 的实际矩阵块](R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md)，以及已核的[变化预解幂与词深度](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)。
本稿不再要求只留一条无界主模式，不要求主最高系数字符为单位，也不在未知核内作谱分块。

## 1. 原函数、实际完整矩列与主定理

固定整数 $m\ge1$。取任意复行
$$
a_\nu=(a_{\nu j})_{j\ge0}\in\ell^2,\qquad
u_\nu=a_{\nu,*}+\sum_{j\ge0}a_{\nu j}\chi_j
\quad(1\le\nu\le m),
\tag{1.1}
$$
全部常数 $a_{\nu,*}$ 固定且任意。令
$$
w=w_*+\sum_jw_j\chi_j,\qquad w_j\in\ell^2(\mathbb C).
$$
固定非零标量多项式 $F\in\mathbb C[x_1,\ldots,x_m]$，总次数为 $d\ge1$。
常数多项式另由 $e^w$ 循环处理。

定义完整有限矩指标
$$
\Omega_d=\{\omega\in\mathbb N_0^m:1\le|\omega|\le d\},
\qquad K=|\Omega_d|=\binom{m+d}{d}-1,
$$
以及每个原物理位的标量列
$$
\xi_j=(a_j^\omega)_{\omega\in\Omega_d},
\qquad a_j^\omega=\prod_{\nu=1}^m a_{\nu j}^{\omega_\nu}.
\tag{1.2}
$$
所有维数在令池大小趋于无穷前固定。

**实际完整矩池条件。** 沿无穷整数子序列 $N$，存在 $K$ 个两两不交的原物理位池 $I_{1,N},\ldots,I_{K,N}$，每池恰有 $N$ 位，满足固定常数 $\mu,C>0$ 下
$$
\min\bigcup_{\ell=1}^K I_{\ell,N}\ge\mu N,\qquad
\max_{\substack{j\in\bigcup I_{\ell,N}\\1\le\nu\le m}}|a_{\nu j}|
\le C N^{-1/2},
\tag{1.3}
$$
$$
\Delta_N=
\min_{j_\ell\in I_{\ell,N}}
\left|\det[\xi_{j_1}\ \cdots\ \xi_{j_K}]\right|>0,
\qquad
1+\log^+\Delta_N^{-1}=O(N^{3/2}).
\tag{1.4}
$$
这是全部跨池选择的共同下界，不能以少量不兼容的非零小行列式替代。

**定理。** 在 (1.1)—(1.4) 下，
$$
\boxed{F(u_1,\ldots,u_m)e^w\ne0,\qquad
[F(u_1,\ldots,u_m)e^w]_A=H.}
\tag{1.5}
$$
特别，若同一原行族对每个固定有限 $d$ 都满足上述条件，则全部非零有限标量多项式都成立。对非恒定 $F$，全部
$[F(u)-\lambda]^r e^w$ 及全部非零 $Q(F(u))e^w$ 随之成立。
若只知道一个次数 $d$ 的条件，不免费外推到次数 $rd$。

(1.4) 排除精确退化的完整矩行；有碰撞的矩行需另作真实合并及单位方向检查。
本稿的主定理不假定这些检查自动成立。

## 2. 精确普通矩逆与全空间常数偏导

令
$$
v_{e_\nu}=u_\nu,\qquad
v_\omega=\sum_j a_j^\omega(\chi_j-1)\quad(|\omega|\ge2).
\tag{2.1}
$$
高矩行绝对可和：从其中取两个 $\ell^2$ 因子用 Cauchy–Schwarz，其余有限个因子有界。
不存在使用发散的 $\sum_j a_{\nu j}$ 的步骤。

以 $Z_\omega$ 为独立有限变量，定义
$$
Q_F(Z)=
\left.F(\partial_t)
\exp\left[
\sum_{\nu=1}^m t_\nu Z_{e_\nu}
+\sum_{\substack{\omega\in\Omega_d\\|\omega|\ge2}}
\frac{(-2)^{|\omega|-1}}{\omega!}t^\omega Z_\omega
\right]\right|_{t=0}.
\tag{2.2}
$$
只保留总参数次数至多 $d$。
给 $Z_\omega$ 权 $|\omega|$，则 $Q_F$ 的权次及普通次数均不超过 $d$。

令 $\phi(t)=(1-e^{-2t})/2$、$\psi(t)=-\log(1-2t)/2$，取零点解析分支。
对扩展行共振生成式代入
$s_{e_\nu}=t_\nu$、$s_\omega=(-2)^{|\omega|-1}t^\omega/\omega!$。
第 $j$ 位的参数组合到次数 $d$ 准确为 $\phi(\sum_\nu t_\nu a_{\nu j})$。
额外的高矩线性项与二次以上共振项合并为
$$
\sum_j
\left[\psi\!\left(\phi\!\left(\sum_\nu t_\nu a_{\nu j}\right)\right)
-\sum_\nu t_\nu a_{\nu j}\right](\chi_j-1)=0
$$
到全部所需次数。非线性系数的绝对收敛已由 (2.1) 支付。
所以扩展行的实际共振变换满足
$$
\boxed{\mathfrak F_{Q_F}^{\rm exp}=F(u_1,\ldots,u_m).}
\tag{2.3}
$$

写最高普通齐次部 $F_d(x)=\sum_{|\omega|=d}f_\omega x^\omega$，
选 $f_{\omega_*}\ne0$。$Z_{\omega_*}$ 在 (2.2) 中只能线性出现且不与其他正权变量同乘，因此
$$
\boxed{\partial_{Z_{\omega_*}}Q_F
=(-2)^{d-1}f_{\omega_*}=:c_*\ne0.}
\tag{2.4}
$$
参数阶乘 $\omega_*!$ 已抵消，不能再加一遍。
这是真正的标量常数，不是在某个未知核根上的局部单位。

## 3. 保留完整原 Bell 与规范最大图

记 $t_j=e^{-2w_j}$、$R_j=V(t_jN_j)$。
实际线性模式为
$$
Z_{e_\nu}=X_{u_\nu,w}=X_{u_\nu}+H_{\nu,w},
\qquad H_{\nu,w}\in\mathcal A,
$$
高矩模式为
$$
Z_\omega=\sum_j a_j^\omega(R_j-I)\in\mathcal A
\quad(|\omega|\ge2).
$$
倾斜差 $H_{\nu,w}$ 由 $\ell^2\times\ell^2$ 及有限低位另付，按范数绝对收敛；各项与全部原 first 完整域交换。

对扩展指标的多重指数 $\beta=(\beta_\omega)_{\Omega_d}$，定义
$$
G_\beta=(-1)^{|\beta|-1}(|\beta|-1)!
\sum_j\left(\prod_{\omega\in\Omega_d}
(a_j^\omega)^{\beta_\omega}\right)(R_j-I)^{|\beta|}
\quad(2\le|\beta|\le d).
$$
所有这些行绝对可和，且局部至少含二阶 $N_j$。
原完整有限共振多项式是
$$
P(Z;\mathbf G)=
\exp\left(\sum_{2\le|\beta|\le d}
\frac{G_\beta}{\beta!}\partial_Z^\beta\right)Q_F(Z).
\tag{3.1}
$$
不删除任何混合项。
把 $G_\beta$ 作为已定义系数保持固定，(2.4) 给
$$
\partial_{Z_{\omega_*}}P=c_*I.
\tag{3.2}
$$

R186 的共同自然词、规范最大闭图和完整 $C$ 自伴给
$$
\mathsf T=\overline{P|_{\mathcal D_d^{\rm orig}}},\qquad
\mathsf T^*=C\mathsf TC,\qquad
\mathsf Te^w=F(u)e^w.
\tag{3.3}
$$
其中 $\mathcal D_s^{\rm orig}$ 包含所有原 first 长度至多 $s$ 的自然词序。
原自然域不被默认视为闭域。$e^w$ 的原多项式轨道是该最大图的图核心。
后续使用 (3.3) 的原实现，不把正分量的最大图另行认作它。

## 4. 任意复行的变化共同正则器

将全部 $a_\nu$ 的实部与虚部各拆为正负部。
得到有限个非负 $\ell^2$ 行及其未加常数的最大增生 first $T_\eta$，数量不超过 $4m$。
删掉零行。R128、R186 §2 给实际收缩预解
$$
R_\eta(t)=(I+tT_\eta)^{-1}\in A',\qquad
R(t)=\prod_\eta R_\eta(t).
$$
这些因子有真实单射和稠密像，且因 $A'$ 交换而互相交换。

R186 的 (2.2)、(3.5) 直接适用于原复行。写
$S_\nu(t)=Z_{e_\nu}R(t)\in A'$，由
$T_\eta R_\eta=t^{-1}(I-R_\eta)$ 得
$$
\|S_\nu(t)\|\le C_w+8/t.
\tag{4.1}
$$
系数 $\pm1,\pm i$ 只给四个正分量，固定中心与倾斜项收入 $C_w$。

取
$$
q_r=(8d+8)r,\qquad t_r=r^{-2},\qquad
\boxed{\mathcal R_r=R(t_r)^{q_r}.}
\tag{4.2}
$$
对任何长度 $s\le q_r$ 的原 first 自然词，
$$
\boxed{
\mathcal R_rH\subset\mathcal D_{q_r}^{\rm orig},\qquad
\|W(Z)\mathcal R_r\|\le(C_w+8r^2)^s.
}
\tag{4.3}
$$
逐次作用时保留 $q_r-s$ 个共同正则因子，下一次输入的真实域由 R186 (3.5) 支付。

这个构造还落在正分量的共同自然深域。
只需要并使用
$\mathcal D_s^{\rm positive}\subseteq\mathcal D_s^{\rm orig}$；
不声称两域相等。复线性抵消可能扩大原域。

在全部 $T_\eta$ 的稠密共同一阶域上，预解恒等式与收缩性给
$$
\|(\mathcal R_r-I)f\|
\le q_rt_r\sum_\eta\|T_\eta f\|\longrightarrow0.
$$
因为 $\|\mathcal R_r\|\le1$，延拓到全 $H$ 得
$$
\boxed{\mathcal R_r\to I\quad{\rm SOT}.}
\tag{4.4}
$$
这里 $q_rt_r=(8d+8)/r$ 趋零。

令 $M=\ker\mathsf T$。R186 原最大图写成有界方程
$F_Pf=R_0^d g$，故 $M=\ker F_P$。
由 $\mathcal R_r\in A'$ 得
$$
\boxed{\mathcal R_rM\subset M\cap\mathcal D_{q_r}^{\rm positive},
\qquad \mathcal R_rf\to f\ (f\in M).}
\tag{4.5}
$$
没有要求 $M$ 自身先进入 first 域，也不使用 $\mathcal R_r^*$ 保持 $M$。

## 5. 有限正分量下的反射误差与全部词预算

这里明确扩展已核正则引理的双导数估计。
只对本稿实际 first、高矩及 (3.1) 的局部 Bell 公式使用该估计；
不把任意 $A'$ 系数的反射变化当作已知。

对有限位集 $E$，令 $J_E=\prod_{j\in E}M_{\chi_j}$。
带帽变量表示在原局部公式中，仅把 $j\in E$ 的 $t_jN_j$ 改成 $-t_jN_j$。
[R260 §§2–4](R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md) 的真实最高物理位壳给每个反射差
$$
\gamma_E Z-\widehat Z=\sum_{\ell\ge\min E}B_{\ell,E},
\qquad
\|B_{\ell,E}\|\le C\eta_{\ell-1}.
\tag{5.1}
$$
每个壳局部于前 $\ell+1$ 位，常数与 $|E|,\max E$ 无关。
高矩和混合 Bell 系数的行属于 $\ell^1\subset\ell^2$，同一壳证明适用；固定有理局部因子的逆由 R260 的有限低位和尾平方关系分别支付。

对所有正分量 $T_\eta$ 同时求真正的域导数。
每个局部壳与各闭尾 first 完整交换，而有界头满足
$$
\sum_\eta 2\|T_{\eta,\le\ell}\|\le C+C'\sqrt{\ell+1}.
$$
所以对有限多重指标 $\gamma$，
$$
\|\operatorname{ad}_{T}^{\gamma}B_{\ell,E}\|
\le\prod_\eta d_{\eta,\ell}^{\gamma_\eta}\|B_{\ell,E}\|.
$$
以足够大的固定半径对这些导数作 $\gamma!$ 加权绝对和，
真实 Leibniz 和逐个闭 first 的图极限给联合导子 Banach 代数。
各导数在共同二阶域上由原交换词恒等式互相交换，再延拓为有界导数恒等式。
于是
$$
\|\gamma_E Z-\widehat Z\|_{\partial}
\le C\sum_{\ell\ge\min E}\eta_{\ell-1}e^{C'\sqrt{\ell+1}}
\le C''e^{-c16^{\min E-1}}=:\varepsilon_E.
\tag{5.2}
$$
固定半径的增加只改变常数，不改变双指数费用。

原倾斜 $Z_{e_\nu}$ 是正分量的有限复线性组合加有界 $H_\nu\in A'$。
$H_\nu$ 与正分量完整域交换，但不必与误差壳交换。
准确使用
$$
\|\operatorname{ad}_{H_\nu}^a B\|_\partial
\le(2\|H_\nu\|)^a\|B\|_\partial
$$
及真正的有限二项式卷积，可得原倾斜混合导数的
$C^s s!\varepsilon_E$ 上界。
这一步没有丢掉 $\operatorname{ad}_{H_\nu}$。

有限反射 $J_E$ 双向保持正分量共同词域：
先在 $\max E+1$ 处分离有界头，全部闭尾与 $J_E$ 完整交换，再用共同词域的有限展开。
定量费用则用 (5.2)，不用这个最大位的粗头范数。

从每池选 $r\asymp\sqrt N$ 位时，(1.3) 使各原行及其正分量的选位绝对和一致有界。
因此带帽 first 的有界增量、全部高矩带帽系数也一致有界。
对有界交换 $N_j$ 多项式 $Q_E$，以 $H_N$ 记其实际绝对系数和。
将长度 $s\le4dr$ 的原 first 字移过 $J_E$ 并正规排序：
每个字或者保留到右侧，或者消耗为一次系数导数，所以总词深度不会增长。
至多 $(C(s+1))^s$ 个项，各阶乘乘积不超过 $s!$。
由 (4.3) 得
$$
\boxed{\|W(Z)J_EQ_E\mathcal R_rf\|
\le H_N e^{C_dr\log(r+2)}\|f\|.}
\tag{5.3}
$$
含至少一个真实反射误差的项另带因子 $\varepsilon_E$。
重复位由 $N_j^2=\eta_jN_{j+1}$ 支付，同样至多付 (5.3) 的费用。
$q_r=(8d+8)r$ 严格超过全部这些 $O(dr)$ 自然中间词所需深度。

## 6. 全空间单位方向与真正矩阵块顶部

取一块 $B=(j_1,\ldots,j_K)$，每池一个位，令
$$
\Xi_B=[\xi_{j_1}\ \cdots\ \xi_{j_K}],\qquad
b_B=\frac14\Xi_B^{-1}e_{\omega_*},\qquad u_j=t_jN_j.
$$
原符号差的一次项是
$$
L_j=4\sum_{\omega\in\Omega_d}\xi_{\omega j}\,\partial_{Z_\omega}P.
\tag{6.1}
$$
每个 $G_\beta$ 的局部差至少二阶，故没有遗漏其一次项。

定义真正有界交换块输入
$$
Q_B=c_*^{-1}\sum_{\ell=1}^K b_{B,\ell}
\prod_{h\ne\ell}u_{j_h}.
\tag{6.2}
$$
它的位次数是 $K-1$，并保留原规范核与全部自然词域。
在平方零商中，准确有
$$
\left(\sum_{\ell=1}^K u_{j_\ell}L_{j_\ell}\right)Q_B
=c_*^{-1}\left(\sum_{\ell=1}^K b_{B,\ell}L_{j_\ell}\right)
\prod_{\ell=1}^K u_{j_\ell}
=\prod_{\ell=1}^K u_{j_\ell}.
\tag{6.3}
$$
最后一步用 (3.2) 的全空间常数，不使用未知核内的无界逆。

取固定 $\theta>0$，稍后选小，并令
$$
r=r_N=\lceil\sqrt{N/\theta}\rceil.
$$
从每池选 $r$ 位，各池按物理位排序，取一个固定匹配形成 $r$ 个块。
令 $E$ 为全部 $Kr$ 位，$Q_E=\prod_BQ_B$。
有限余子式及全局有界系数给
$$
H_N\le(C\Delta_N^{-1})^r,\qquad
\log^+H_N\le r\log^+\Delta_N^{-1}+Cr.
\tag{6.4}
$$
不再对所有匹配求和。

对核内深输入 $Q_E\mathcal R_rf$，原 $P$ 的零次部分作用为零；
它与全部带帽差分在已付共同深域上交换。
$r$ 次提升加上已有 $(K-1)r$ 个位：
一个提升若取二次以上，或某块收到两次，必有重复位。
唯一无重复顶部是每块恰好一次，由 (6.3) 得 $r!t_EN_E$。
真实重复位和反射误差由 (5.2)—(5.3) 支付。

严格保留次序
$$
\mathsf T^rJ_EQ_E\mathcal R_rf
=J_E(\gamma_E\mathsf T)^rQ_E\mathcal R_rf.
$$
由于 $J_EE_E=(-1)^{Kr}E_E$，实际式为
$$
\boxed{
\mathsf T^rJ_EQ_E\mathcal R_rf
=(-1)^{Kr}r!t_EE_E\mathcal R_rf+\mathcal E_{E,N}f.
}
\tag{6.5}
$$
其中所有反射、重复位及 $N_E-E_E$ 的误差均由
$$
(\varepsilon_{\lfloor\mu N\rfloor}+\eta_{\lfloor\mu N\rfloor})
e^{Cr\log(r+2)}H_N
+C r!|t_E|Kr\,\eta_{\lfloor\mu N\rfloor}
\tag{6.6}
$$
乘 $\|f\|$ 主控，放宽固定常数即可。
此处每个自然作用都最多消耗 $O(dr)$ 个 first 字；不把形式商恒等式直接当作原算子等式。

## 7. 准确平均与非零弱极限

定义
$$
\mathcal V_N=(-1)^{Kr}(r!)^{K-1}(2/N)^{Kr}
\sum_{\substack{J_\ell\subset I_{\ell,N}\\|J_\ell|=r}}
t_E^{-1}J_EQ_E.
\tag{7.1}
$$
$K$ 个组合数、一个固定匹配和前因子给
$$
\|\mathcal V_N\|\le A_N,\qquad
A_N=\max\left(1,\frac{C^{Kr}}{r!}H_N\right),\qquad
\log A_N\le r\log^+\Delta_N^{-1}+C'r.
\tag{7.2}
$$
提升再给一个 $r!$，顶部总阶乘是 $(r!)^K$。
令
$$
C_{\ell,N}=\frac2N\sum_{j\in I_{\ell,N}}E_j,\qquad
\mathcal C_N=\prod_{\ell=1}^KC_{\ell,N}^r.
$$
(6.5)—(7.2) 及双指数误差给
$$
\|\mathsf T^r\mathcal V_N\mathcal R_rf
-\mathcal C_N\mathcal R_rf\|\to0
\quad(f\in M).
\tag{7.3}
$$
不要求 $\mathcal V_N$ 一致有界。

纯池平均满足
$$
\|\mathcal C_N\|\le(1+1/N)^{Kr}.
$$
在任意固定有限柱之间，全部池最终位于其外，矩阵系数乘子准确为
$\bigl((N)_r/N^r\bigr)^K\to e^{-K/(2\theta)}$。
有限柱稠密和统一范数界给
$$
\mathcal C_N\rightharpoonup cI,\qquad
c=e^{-K/(2\theta)}>0.
$$
又由 $\mathcal R_rf\to f$，
$$
\boxed{\mathsf T^r\mathcal V_N\mathcal R_rf\rightharpoonup cf.}
\tag{7.4}
$$
强正则化位于右输入，因而没有把 $r$ 增长造成的弱零错误改称近单位。

## 8. 局部四次费用排除原规范核

固定任意局部全矩阵 $D_0$。在实际低位将 $R_j$ 置为 $I$；
每个低位差
$$
R_j-I=-2t_jN_j(I+t_jN_j)^{-1}
$$
准确含一个 $A$ 因子，因为 $N_j=A^{2^j}/d_j$。
实际有限多项式相减给共同深域上的
$$
P=P_{\mathrm{tail},h}+A\,U_h(Z),
\qquad \deg U_h\le d.
\tag{8.1}
$$
尾与 $D_0$ 完整域交换，全部系数为明确有界交换子。
原各项在共同深域上交换，所以
$\operatorname{ad}_P^rD_0=\operatorname{ad}_{AU_h}^rD_0$。

第 $j$ 项保留
$A^jU_h^jD_0A^{r-j}U_h^{r-j}$。
将 first 字移过固定 $D_0$，其真正联合导数只付固定几何费用；
两侧 $A$ 幂仍保留在局部测试的有界导数两边。
R109 的原四次幂界、$j^4+(r-j)^4\ge r^4/8$ 和 (5.3) 给
$$
\|(\operatorname{ad}_P^rD_0)\mathcal V_N\mathcal R_rf\|
\le
A_N e^{-5r^4/6+105r^3+C_{D_0,d}r\log(r+2)}\|f\|.
\tag{8.2}
$$
这是指定深输入的估计，不是全空间有界交换子结论。

由 (1.4)、$N\sim\theta r^2$ 和 (7.2)，
$$
\limsup_N\frac{\log A_N}{r^4}\le C_\Delta\theta^{3/2}.
$$
先取固定足够小的 $\theta$，使右侧小于 $1/4$。
该选择与局部测试 $D_0$ 无关。于是 (8.2) 趋零，全部双指数 carry 同时趋零。

对任意 $f,g\in M$，原完整 $C$ 自伴及所有已付中间自然词给
$$
B(D_0\mathsf T^r\mathcal V_N\mathcal R_rf,g)
=(-1)^rB((\operatorname{ad}_P^rD_0)\mathcal V_N\mathcal R_rf,g).
\tag{8.3}
$$
展开右侧时，每个左正次 $\mathsf T$ 用全空间 $C$ 对称移至 $g$，
再由 $\mathsf Tg=0$ 消掉。
没有使用 $CM=M$、$D_0M\subset M$ 或正则器伴随保核。

(7.4)、(8.2) 给 $B(D_0f,g)=0$ 对所有局部全矩阵成立。
实际局部矩阵代数不可约，故 $M=0$。
由 $\mathsf T^*=C\mathsf TC$，其像稠密；
$e^w$ 的原多项式轨道为图核心，所以 (3.3) 给 (1.5)。
若 $F(u)e^w=0$，非零 $e^w$ 已在核中，亦矛盾。
主定理得证。

## 9. 明确的复幂行族：全部次数有池，全部 first 为全平面连续谱

固定复数
$$
\rho_\nu=\sigma_\nu+i\tau_\nu,\qquad
\frac12<\sigma_\nu<1,\quad \tau_\nu\ne0
\quad(1\le\nu\le m).
$$
假设它们在整数系数下没有非平凡关系：
$$
\sum_\nu n_\nu\rho_\nu=0,\quad n_\nu\in\mathbb Z
\quad\Longrightarrow\quad n_\nu=0\ \text{对全部 }\nu.
\tag{9.1}
$$
取原行和任意固定原常数
$$
\boxed{a_{\nu j}=(j+2)^{-\rho_\nu},\qquad
u_\nu=a_{\nu,*}+\sum_j(j+2)^{-\rho_\nu}\chi_j.}
\tag{9.2}
$$
正实底上的复幂使用确定实对数。
这些行属于 $\ell^2\setminus\ell^1$。

### 9.1 全部有限矩的实际跨池下界

对任意固定 $d$ 和 $\omega\in\Omega_d$，置
$$
\beta_\omega=\sum_\nu\omega_\nu\rho_\nu.
$$
(9.1) 使不同矩指标的 $\beta_\omega$ 两两不同，而真实矩行恰为
$$
a_j^\omega=(j+2)^{-\beta_\omega}.
\tag{9.3}
$$

先证明可以选固定分离正区间，使函数 $t^{-\beta_\omega}$ 的所有跨区间取点矩阵一致可逆。
在变量 $x=\log t$ 中，函数是 $e^{-\beta_\omega x}$。
其 Wronskian 为
$$
\det_{\omega,\,0\le h<K}
\left[(-\beta_\omega)^h e^{-\beta_\omega x}\right]
=
e^{-x\sum_\omega\beta_\omega}
\prod_{\omega<\omega'}(-\beta_{\omega'}+\beta_\omega)\ne0
$$
（固定一次行序）。
在 $K$ 个节点 $x_\ell=x_0+\epsilon\ell$ 作有限 Taylor 展开，
行列式的最低非零项等于该 Wronskian 乘非零实 Vandermonde，
再乘 $\epsilon^{K(K-1)/2}/\prod_{h=0}^{K-1}h!$。
所以充分小的某个固定 $\epsilon>0$ 给一个真实非零取值行列式。
这里不把复指数函数宣称为全正轴上的实 Chebyshev 系统。

由连续性，给这些不同的正节点各取一个小的互不相交闭邻域，
可使所有跨邻域取点的行列式模有正下界。
同时把全部节点放大一个充分大的固定正数 $M$，矩阵各行只多因子 $M^{-\beta_\omega}$，非零性不变。
故可以在各放大邻域内选择不同的正整数 $L_\ell$，使
$[L_\ell,L_\ell+2]$ 完整包含其中。

取真实物理位池
$$
I_{\ell,N}=\{L_\ell N+s:0\le s<N\},\qquad N\ge2.
$$
各池恰有 $N$ 位、互不相交，最小位至少 $\mu N$。
跨池位 $j_\ell$ 的 $t_\ell=(j_\ell+2)/N$ 属于上述固定不交紧区间。
将 (9.3) 的第 $\omega$ 行因子 $N^{-\beta_\omega}$ 提出，得到
$$
\boxed{
\Delta_N\ge C_d
N^{-\sum_{\omega\in\Omega_d}\operatorname{Re}\beta_\omega}.
}
\tag{9.4}
$$
其对数成本仅为 $O_d(\log N)$。
原各行的选位幅度是 $O(N^{-\sigma_\nu})=O(N^{-1/2})$。
因此同一 (9.2) 行族对每个固定有限 $d$ 都满足主定理，得到
$$
\boxed{F(u_1,\ldots,u_m)e^w
\text{ 对全部非零有限标量多项式 }F\text{ 循环}.}
\tag{9.5}
$$
池和固定维数允许依赖 $d$，始终先固定它们再令 $N$ 增长。

### 9.2 每个原 first 的谱类型

对固定 $\rho=\sigma+i\tau$ 如上，求和与积分的单位区间误差由
$|(\partial_x)x^{-\rho}|\le Cx^{-\sigma-1}$ 支付，所以
$$
\sum_{j<n}(j+2)^{-\rho}
=\frac{(n+2)^{1-\rho}}{1-\rho}+O(1),\qquad
\sum_{j<n}(j+2)^{-\sigma}
=\frac{(n+2)^{1-\sigma}}{1-\sigma}+O(1).
$$
对任意固定实角 $\theta$，
$$
\begin{aligned}
\sum_{j<n}\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)
&\ge
\left(\frac1{1-\sigma}-\frac1{|1-\rho|}\right)
(n+2)^{1-\sigma}+O(1)\\
&\longrightarrow\infty.
\end{aligned}
\tag{9.6}
$$
严格正系数由 $\tau\ne0$ 得到。
[R138 的完整谱分类](R138-first-chaos-complete-spectrum-classification.md) 因而给
$$
\boxed{\sigma(X_{u_\nu})=\sigma_{\rm ap}(X_{u_\nu})=\mathbb C,
\quad\text{每个谱点均为连续谱点}.}
\tag{9.7}
$$
固定原常数不改变全复平面结论。

例如可取两个模式
$$
\rho_1=2/3+i,\qquad \rho_2=3/4+i.
$$
整数关系的虚部先给 $n_1+n_2=0$，实部再给 $n_1=n_2=0$，所以 (9.1) 成立。
这两个原 first 都有 (9.7)，而 (9.5) 仍覆盖全部非零二变量多项式及任意复 $\ell^2$ 指数权。

在这个同虚部的例子中，任何非零常系数组合也没有空谱 first 锚：
取该组合最慢衰减的非零项，它的旋转主项给 (9.6) 的严格正主系数，
其余有限项的绝对和只是 $o(n^{1-\sigma_{\min}})$。
再加任何 $\ell^1$ 行只改有限缺陷费用。
因此本例不靠一个未写出的空谱线性组合来消去第二无界方向。

## 10. 范围与后续接口

本稿付清的是有限原复模式、明确的完整矩池条件、实际有限矩逆和全部原 Bell 的循环性。
关键变化是：原最大核内的测试向量随阶数作真实收缩正则化，仍强趋原向量；
其余全部自然词成本只增长为 $e^{O(r\log r)}$，由原局部双侧四次 $A$ 费用支付。
不需要核内 first 有界，也没有把多变量互素当成单位理想。

以下事项没有由本稿自动得到：

- 精确碰撞的矩行必须先合并，并重新检查真实单位方向；零行列式不能保留在 (1.4) 中。
- 缺少兼容跨池下界的任意慢行，以及无限模式，不满足本稿已付输入。
- 任意 $L^2$ 向量、真实正常见证源的全预算、原边界无权 $N=M$ 及普通复 Hilbert ISP 仍未完成。

[R109](R109-invariant-restriction-exact-quartic-type.md) 的四次费用、
[R260](R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md) 的真实物理壳、
[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 的最大图与完整 $C$ 自伴，以及开头所列两份 R236 矩阵来源，是这里逐项使用的实际依据。
