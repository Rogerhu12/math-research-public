# R236 附录：有限多个可和辅助的矩阵块消元与准确池平均

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。
状态：已证明。
本稿把二位标量消元推广到一个闭主 first 与任意有限个可和辅助行。
不要求逐位幂比较，不要求空谱锚，不把多个独立无界模式纳入本结论。
一般 Hilbert 不变子空间问题仍未完成。

## 1. 真实多行目标与矩阵池条件

取复主行及共同权
$$
a,b\in\ell^2,
$$
并取 $d\ge1$ 个复辅助行
$$
c_\nu\in\ell^1,\qquad 1\le\nu\le d.
$$
令 $m=d+1$，并写
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v_\nu=\sum_jc_{\nu j}(\chi_j-1),\qquad
w=b_*+\sum_jb_j\chi_j.
\tag{1.1}
$$
所有支撑允许任意重叠，全部复相位与物理排列任意。

记每个位的实际系数列为
$$
\xi_j=(a_j,c_{1j},\ldots,c_{dj})^{\mathsf T}\in\mathbb C^m.
\tag{1.2}
$$
假设沿无穷整数子序列 $N$，存在 $m$ 个两两不交的物理位池
$$
I_{0,N},\ldots,I_{d,N},\qquad |I_{\nu,N}|=N,
$$
满足
$$
\boxed{
\min\bigcup_{\nu=0}^d I_{\nu,N}\ge\mu N,\qquad
\max_{\bigcup I_{\nu,N}}|a_j|\le C_aN^{-1/2}
}
\tag{1.3}
$$
对固定 $\mu,C_a>0$ 成立。

对每个横跨各池的选择 $j_\nu\in I_{\nu,N}$，组成真正标量方阵
$$
\Xi(j_0,\ldots,j_d)
=
[\xi_{j_0}\ \xi_{j_1}\ \cdots\ \xi_{j_d}].
$$
定义
$$
\delta_N=
\min_{\substack{j_\nu\in I_{\nu,N}\\0\le\nu\le d}}
|\det\Xi(j_0,\ldots,j_d)|.
$$
要求
$$
\boxed{
\delta_N>0,\qquad
\ell_N:=1+\log^+\delta_N^{-1}=O(N^{3/2}).
}
\tag{1.4}
$$

不要求任何一个辅助行在所选位上为 $O(N^{-1/2})$。
辅助选位和直接由其全局 $\ell^1$ 范数支付；
余子式只需要各系数行全局有界。

给定标量多项式
$$
F(U,V_1,\ldots,V_d)
=\sum_{k=0}^p f_k(V_1,\ldots,V_d)U^k,
$$
$$
\boxed{p\ge1,\qquad f_p(0)\ne0.}
\tag{1.5}
$$
记总次数为 $D$，所以 $D\ge p$。
在总次数 $D$ 以内定义
$$
\mathscr E(t_0,\ldots,t_d)
=
\exp\left[
t_0u+\sum_{\nu=1}^d t_\nu v_\nu+
\sum_{n=2}^D\frac{2^{n-1}}n
\sum_j\left(t_0a_j+\sum_{\nu=1}^dt_\nu c_{\nu j}\right)^n
(\chi_j-1)
\right],
$$
$$
\boxed{\mathfrak F_F=F(\partial_{t_0},\ldots,\partial_{t_d})\mathscr E(0).}
\tag{1.6}
$$
这是准确多行共振变换，不是未修正的普通点态 $F(u,v)$。

## 2. 主定理

固定 $\lambda\in\mathbb C$。
设对于每个满足 $F(\zeta,0)=\lambda$ 的标量根，都有
$$
\boxed{
\bigl(F_U(\zeta,0),F_{V_1}(\zeta,0),\ldots,F_{V_d}(\zeta,0)\bigr)
\ne0.
}
\tag{2.1}
$$

**定理 1。**
在 (1.3)–(1.5)、(2.1) 下，
$$
\boxed{
(\mathfrak F_F-\lambda)e^w
\text{ 非零且对原实际 }A\text{ 循环}.
}
\tag{2.2}
$$
没有额外的排序下界、可和幂条件或主／辅助幂比较。
主行可处于无空谱锚的全平面分支。

因 $F(U,0)$ 是次数恰为 $p$ 的多项式，
本判据只可能留下有限集合
$$
\mathcal E_F=
\{F(\zeta,0):
F_U(\zeta,0)=F_{V_1}(\zeta,0)=\cdots=F_{V_d}(\zeta,0)=0\}.
\tag{2.3}
$$
它至多有 $p-1$ 个值。
若该集合为空，全部标量位移均由 (2.2) 处理。
这里的“未排除”不表示这些值实际存在非零核。

## 3. 全部混合修正、最高系数与真实自然域

令
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad
X=X_{u,b},\quad
Y_\nu=\sum_jc_{\nu j}(R_j-I).
\tag{3.1}
$$
每个 $Y_\nu$ 是有界零字符 $\mathcal A$ 元。

对多重指标 $\omega=(\omega_0,\ldots,\omega_d)$、
$2\le|\omega|\le D$，置
$$
\boxed{
G_\omega
=
(-1)^{|\omega|-1}(|\omega|-1)!
\sum_j
a_j^{\omega_0}\prod_{\nu=1}^dc_{\nu j}^{\omega_\nu}
(R_j-I)^{|\omega|}.
}
\tag{3.2}
$$
各行都平方可和，且总幂至少2，故系数绝对可和。
全部级数按算子范数绝对收敛。

每个
$$
G_\omega\in\mathcal G,\qquad\chi(G_\omega)=0.
\tag{3.3}
$$
这可由明确的局部至少二阶消去证明；
也可对 R270C 的
$$
G_n\left(t_0a+\sum_{\nu=1}^dt_\nu c_\nu\right)\in\mathcal G
$$
作固定次数的有限多项式插值，提取各个参数系数。
这里只用 $\mathcal G$ 对有限线性组合的封闭，
不把它视为整个 $\mathcal A$ 的理想或任意范数闭代数。

定义有限系数多项式
$$
P_F(z_0,\ldots,z_d;\mathbf G)
=
\exp\left(
\sum_{2\le|\omega|\le D}
\frac{G_\omega}{\omega!}\partial_z^\omega
\right)F(z_0,\ldots,z_d).
\tag{3.4}
$$
R270C 的单个位共振恒等式、R186 的完整混合自然 jets，
以及辅助的有界性给实际域等式
$$
\boxed{
P_F(X,Y_1,\ldots,Y_d;\mathbf G)e^w
=\mathfrak F_Fe^w.
}
\tag{3.5}
$$
全空间的无界 first 指数没有被当作有界算子。

关于 $X$ 的实际最高系数是
$$
L=
\left[
\exp\left(
\sum_{\substack{2\le|\omega|\le D\\\omega_0=0}}
\frac{G_\omega}{\omega!}\partial_{(z_1,\ldots,z_d)}^\omega
\right)
f_p(z_1,\ldots,z_d)
\right]_{z_\nu=Y_\nu}.
\tag{3.6}
$$
它的字符为 $f_p(0)\ne0$，故为真实 $\mathcal A$ 单位。
不能以未经混合修正的 $f_p(Y)$ 代替它。

因此
$$
T_\lambda=P_F(X,Y;\mathbf G)-\lambda I,\qquad
\operatorname{Dom}T_\lambda=\operatorname{Dom}X^p
\tag{3.7}
$$
有 R176 的闭自然域、完整 $C$ 自伴性及 $e^w$ 的循环图核心。

反设 $M=\ker T_\lambda\ne0$。
则
$$
M\subset\mathcal D_\infty(X),\qquad X_M\in B(M),
$$
$$
\sigma(X_M)\subset\{\zeta:F(\zeta,0)=\lambda\}.
\tag{3.8}
$$
按有限根作 Riesz 分解，得到闭 $A$ 不变块 $M_\zeta$；
每个块均由全部 $\mathcal A$ 系数保持。
只需排除任意非零的这样一个块。

## 4. 一个根块内的梯度单位

以下固定 $M_\zeta\ne0$，省略限制记号。
定义各真实梯度算子
$$
D_\nu=(P_F)_{z_\nu}(X_M,Y;\mathbf G),
\qquad 0\le\nu\le d.
\tag{4.1}
$$
这里把所有 $G_\omega$ 当作系数保持固定。

$X_M-\zeta I$、$Y_\nu|_M$、$G_\omega|_M$ 为交换拟幂零元。
因此
$$
D_\nu-F_{z_\nu}(\zeta,0)I_M
$$
也拟幂零。
由 (2.1)，可选某个 $\nu_* \in\{0,\ldots,d\}$，使
$$
\boxed{D_{\nu_*}\in B(M)^\times.}
\tag{4.2}
$$
选择可随根块变化，但在该块的全部 $N$、全部所选位中固定。

该逆只要求在原未知核块上有界；
它与 $X_M$、全部 $\mathcal A$ 系数及 $A|_M$ 交换。
下面先用它形成核内输入，再施最左侧反射。
不把它擅自延拓为全空间逆，也不移到反射左侧。

## 5. 实际一次系数及一块矩阵消元

对于一个所选高位，记 $u_j=t_jN_j$。
真实高位符号差的一次系数为
$$
\boxed{
L_j=4\left(a_jD_0+\sum_{\nu=1}^dc_{\nu j}D_\nu\right)
=4\sum_{\nu=0}^d\xi_{\nu j}D_\nu.
}
\tag{5.1}
$$
每个混合 $G_\omega$ 的同位符号差都含 $u_j^{|\omega|}$，
所以 $|\omega|\ge2$ 保证它没有平方零一次项。

取一块
$$
B=(j_0,\ldots,j_d),\qquad j_\nu\in I_{\nu,N},
$$
并令 $\Xi_B$ 为其系数矩阵。
定义真实标量列
$$
b_B=\frac14\Xi_B^{-1}e_{\nu_*},
\qquad
4\sum_{i=0}^d b_{B,i}\xi_{j_i}=e_{\nu_*}.
\tag{5.2}
$$
取块输入
$$
\boxed{
Q_B=
D_{\nu_*}^{-1}
\sum_{i=0}^d b_{B,i}
\prod_{\substack{0\le k\le d\\k\ne i}}u_{j_k}.
}
\tag{5.3}
$$
它的位次数为 $d=m-1$，并把 $M$ 映入自身。

在该块的平方零商中，
$$
\begin{aligned}
\left(\sum_{i=0}^d u_{j_i}L_{j_i}\right)Q_B
&=
D_{\nu_*}^{-1}
\left(\sum_{i=0}^d b_{B,i}L_{j_i}\right)
\prod_{i=0}^d u_{j_i}\\
&=\prod_{i=0}^d u_{j_i}.
\end{aligned}
\tag{5.4}
$$
第一行只有补上缺失位的项能存活；
第二行正是 (5.1)–(5.2) 的矩阵恒等式。
没有把多变量互素当成单位理想。

## 6. r 块计数与绝对系数预算

固定
$$
r=r_N=\lceil\sqrt{N/\theta}\rceil,\qquad \theta>0.
$$
从每个池选 $r$ 位，记为 $J_0,\ldots,J_d$。
各集合按原物理位排序，并把各自第 $s$ 项组成第 $s$ 块。
只用这个确定匹配，不额外对 $(r!)^d$ 个匹配求和。

令
$$
E=J_0\cup\cdots\cup J_d,\qquad |E|=mr,\qquad
Q_{J_0,\ldots,J_d}=\prod_{s=1}^rQ_{B_s}.
\tag{6.1}
$$
输入总位次数为 $(m-1)r$。

设 $B_0$ 是所有标量系数行及1的统一上界。
由有限余子式，
$$
\sum_{i=0}^d|b_{B,i}|
\le\frac{m!B_0^{m-1}}{4\delta_N}.
\tag{6.2}
$$
令 $T_b=\max(1,\sup_j|t_j|)$。
将每个块输入展开为 $N_j$ 单项式，其绝对系数和至多
$$
H_N=
\left(
\frac{C_{m,B_0,b}\|D_{\nu_*}^{-1}\|}{\delta_N}
\right)^r.
\tag{6.3}
$$
这是含算子单位因子的实际绝对系数预算；
不以可能出现消去的输入范数取代它。
特别，
$$
\log^+H_N\le r\ell_N+C_Mr.
\tag{6.4}
$$

在核上，带帽 $T_\lambda$ 的主差分多项式没有零次项，
其一次部分为 $\sum_{j\in E}u_jL_j$。
在其 $r$ 次幂乘 (6.1) 的平方零展开中：

- 输入已有 $(m-1)r$ 次。
- 任何一个提升因子若取二次或更高项，总次数就大于 $mr$，必有重复位。
- 全部因子取一次项时，任何块若收到两个变量也必有重复位。
- 因为共有 $r$ 个因子和 $r$ 个块，只能每块恰好收到一次。

由 (5.4)，唯一顶部项准确为
$$
\boxed{
A_E^rQ_{J_0,\ldots,J_d}
\equiv
r!t_EN_E
\pmod{(N_j^2:j\in E)}.
}
\tag{6.5}
$$
其中 $r!$ 是选择各块顺序的排列数。
它与匹配数无关。

## 7. 实际混合导子、自然深域与 carry

这里把 (6.5) 转回原实际算子。

由 (1.3) 及 $|E|=mr$，
$$
\sum_{j\in E}|a_j|\le mC_a r/\sqrt N=O_\theta(1).
$$
对每个辅助，
$$
\sum_{j\in E}|c_{\nu j}|\le\|c_\nu\|_1.
\tag{7.1}
$$
所以所有实际有限位增量的系数绝对和一致有界。
无需辅助逐位的 $N^{-1/2}$ 上界。

R260 的最高真实物理位壳证明及全阶混合推广给
$$
\|\delta_X^k(\gamma_EX-\widehat X)\|
+\sum_{\nu=1}^d
\|\delta_X^k(\gamma_EY_\nu-\widehat Y_\nu)\|
+\sum_\omega
\|\delta_X^k(\gamma_EG_\omega-\widehat G_\omega)\|
\le k!\varepsilon_N,
$$
$$
\varepsilon_N\le C_{D,m}e^{-385\,16^{\lfloor\mu N\rfloor-1}}.
\tag{7.2}
$$
每个明确的混合系数行平方可和，
局部多项式次数固定；有限系数乘积由完整导子 Banach 代数支付。
这不是仅从 $G_\omega\in\mathcal G$ 删除其反射变化。

对
$$
h_E=Q_{J_0,\ldots,J_d}f\in M
$$
先用核内有界 $X_M$ 给全部自然 jets。
$J_E=\prod_{j\in E}M_{\chi_j}$ 双向保持共同深域。
实际正规排序于是给
$$
\|X^kJ_Eh_E\|\le2R_{D,m,M,\theta}^k\|h_E\|
\qquad(0\le k\le4Dr).
\tag{7.3}
$$
全部误差词至多付
$\varepsilon_Ne^{C_{D,m,\theta}r\log(r+2)}H_N\|f\|$。
重复位则由
$$
N_j^2=\eta_jN_{j+1},\qquad \eta_j\le e^{-385\,16^j}
$$
支付；385 是实际 carry 的粗上界。

真正顺序为
$$
T_\lambda^rJ_EQ_{J_0,\ldots,J_d}f
=
J_E(\gamma_ET_\lambda)^rQ_{J_0,\ldots,J_d}f.
\tag{7.4}
$$
先在核中做 (5.4) 的单位取消，再作用最左 $J_E$。
由于
$$
J_EE_E=(-1)^{|E|}E_E=(-1)^{mr}E_E,
$$
实际顶部提升是
$$
\boxed{
T_\lambda^rJ_EQ_{J_0,\ldots,J_d}f
=(-1)^{mr}r!t_EE_Ef+\mathcal E_Ef.
}
\tag{7.5}
$$
误差可取
$$
\|\mathcal E_Ef\|
\le
\varepsilon_Ne^{C_{D,m,\theta}r\log(r+2)}H_N\|f\|
+
Cr!|t_E|\,mr\,\eta_{\lfloor\mu N\rfloor}\|f\|.
\tag{7.6}
$$

## 8. m 个池的精确阶乘与符号

定义
$$
\boxed{
\mathcal V_N
=
(-1)^{mr}(r!)^{m-1}(2/N)^{mr}
\sum_{\substack{J_\nu\subset I_{\nu,N}\\|J_\nu|=r\ (0\le\nu\le d)}}
t_E^{-1}J_EQ_{J_0,\ldots,J_d}.
}
\tag{8.1}
$$
当 $m=2$ 时符号恒为正，恰回到原双池公式；
一般 $m$ 不得省去该符号。

总项数为 $\binom Nr^m$。
因此，令 $L_b=\max(1,\sup_j|t_j|^{-1})$，
$$
\|\mathcal V_N\|\le A_N,\qquad
A_N=
\max\left\{1,\frac{(2L_b)^{mr}}{r!}H_N\right\},
$$
$$
\boxed{\log A_N\le r\ell_N+C_M'r.}
\tag{8.2}
$$
$(r!)^{m-1}$ 与 $m$ 个组合数相消后仍只剩一个 $1/r!$；
不存在隐藏的额外匹配因子。

另一方面，(7.5) 再给一个 $r!$，
所以顶部总共得到 $(r!)^m$，恰为每个池各自的 $r$ 次纯平均。
置
$$
C_{\nu,N}=\frac2N\sum_{j\in I_{\nu,N}}E_j.
$$
由 (7.5)–(7.6)，
$$
\left\|T_\lambda^r\mathcal V_Nf-
\prod_{\nu=0}^d C_{\nu,N}^rf\right\|
\le
\left[
\varepsilon_Ne^{C_{D,m,\theta}r\log(r+2)}A_N
+C2^{mr}mr\,\eta_{\lfloor\mu N\rfloor}
\right]\|f\|\to0.
\tag{8.3}
$$
纯平均的范数不超过 $(1+1/N)^{mr}$。
在固定有限柱之间，矩阵系数准确为
$$
\left(\frac{(N)_r}{N^r}\right)^m
\longrightarrow e^{-m/(2\theta)}.
$$
故
$$
\boxed{
T_\lambda^r\mathcal V_Nf
\rightharpoonup e^{-m/(2\theta)}f.
}
\tag{8.4}
$$
该非零弱极限一致有界；
没有把 $r\gg\sqrt N$ 的弱零提升改称近单位。

## 9. 固定低头的四次成本及完整排核

固定任意前 $h$ 位的局部全矩阵 $D_0$。
把主 first 和每个有界系数分成该固定真实低头与高尾。
所有低头是真解析有限和，有零常数项，故实际可提出一个 $A$。
高尾与 $D_0$ 完整域交换。
得到共同深域上的准确分解
$$
T_\lambda=T_{\lambda,\mathrm{tail},h}+A\,U_h(X),
\qquad \deg U_h\le p.
\tag{9.1}
$$
次数允许为 $p$，因为最高主系数也可能变化。
未将完整慢辅助除以 $A$。

各项在共同深域上交换。
$\operatorname{ad}_{T_\lambda}^rD_0$ 因而由
$$
A^kU_h(X)^kD_0A^{r-k}U_h(X)^{r-k}
$$
组成。
主变量总阶至多 $pr$，由 (7.3) 的 $4Dr$ jets 支付。
固定局部 $D_0$ 的 $\delta_X$ 导数只给固定几何常数。

原实际 $A$ 的四次幂界及
$k^4+(r-k)^4\ge r^4/8$
给
$$
\boxed{
\|(\operatorname{ad}_{T_\lambda}^rD_0)\mathcal V_Nf\|
\le
2\|D_0\|A_NC_{D,m,D_0,M,\theta}^r
e^{-5r^4/6+105r^3}\|f\|.
}
\tag{9.2}
$$
这是具体深域输入上的估计，不是全空间有界交换子结论。

由 (1.4)、(8.2)，
$$
\limsup\frac{\log A_N}{r^4}
\le C_\ell\theta^{3/2}.
$$
取固定足够小的 $\theta$，使右边小于 $1/4$；
该选择与局部测试 $D_0$ 无关。
(9.2) 便趋零，双指数 carry 同时支付 (8.3)。

对同一根块中的 $f,g$，原完整 $C$ 自伴性与
$T_\lambda g=0$ 给
$$
\mathcal B(D_0T_\lambda^r\mathcal V_Nf,g)
=
(-1)^r
\mathcal B((\operatorname{ad}_{T_\lambda}^rD_0)\mathcal V_Nf,g).
\tag{9.3}
$$
所有有限词都在已核准的共同深域中合法；
不要求 $CM=M$。
结合 (8.4)、(9.2)，
$$
\mathcal B(D_0f,g)=0
$$
对全部局部全矩阵成立。
其不可约性迫这个根块为零。

有限个根块逐一排除，遂有 $\ker T_\lambda=0$。
完整 $C$ 自伴性给稠密像，
(3.5) 的真实循环图核心证明 (2.2)。
定理得证。

## 10. 三池与两个独立慢辅助的明确例子

取
$$
a_j=(-1)^j(j+1)^{-\sigma},
\qquad \frac12<\sigma<1,
$$
并允许任意 $a_*$、任意复 $\ell^2$ 指数权。
把物理位按模3分成 $S_0,S_1,S_2$。
定义
$$
c_{1j}=
\begin{cases}|a_j|^2,&j\in S_1,\\0,&j\notin S_1,\end{cases}
\qquad
c_{2j}=
\begin{cases}|a_j|^2,&j\in S_2,\\0,&j\notin S_2.\end{cases}
\tag{10.1}
$$
两个辅助都可和。
它们各自有无限零位，均不与全部主支撑逐位双侧比较；
两者也不是同一个辅助方向。

对 $\nu=0,1,2$，取
$$
I_{\nu,N}=\{3(N+k)+\nu:0\le k<N\}.
\tag{10.2}
$$
这些池各含 $N$ 位、两两不交、最小物理位至少 $3N$。
主幅度一致为 $O(N^{-\sigma})$，因 $\sigma>1/2$ 而满足 (1.3)。
跨池系数矩阵呈三角形：
$$
\begin{pmatrix}
a_{j_0}&a_{j_1}&a_{j_2}\\
0&c_{1j_1}&0\\
0&0&c_{2j_2}
\end{pmatrix}.
$$
所以
$$
|\det\Xi|
=|a_{j_0}|\,|c_{1j_1}|\,|c_{2j_2}|
\ge C N^{-5\sigma}.
\tag{10.3}
$$
故 (1.4) 的成本仅为 $O(\log N)$。
这些行亦可附加任意相位，行列式模长不变。

取
$$
F(U,V_1,V_2)=U^3+V_1^2+V_2.
\tag{10.4}
$$
它关于 $U$ 的最高系数为1，且 $F_{V_2}=1$，
故 (2.1) 对每个 $\lambda$ 都成立。
该多项式关于 $V_2$ 是系数为1的线性式，
在 $\mathbb C[U,V_1,V_2]$ 中不可约。

令
$$
v_\nu=\sum_jc_{\nu j}(\chi_j-1).
$$
准确共振符号为
$$
\boxed{
\mathfrak F_F=
u^3+6u\sum_j a_j^2(\chi_j-1)
+8\sum_j a_j^3(\chi_j-1)
+v_1^2+2\sum_jc_{1j}^2(\chi_j-1)+v_2.
}
\tag{10.5}
$$
因此对于全部 $\lambda\in\mathbb C$，
$$
\boxed{(\mathfrak F_F-\lambda)e^w\text{ 非零且循环}.}
\tag{10.6}
$$

所有辅助在最早主位 $j=0$ 都为零，且 $a_0=1$。
该位翻转使共振生成式乘上 $(1-2a_0t_0)$，故两个真实字符切片为
$$
p_0(z)=z^3,\qquad p_1(z)=z^3-2a_0(3z^2)=z^3-6z^2.
$$
它们在 $\lambda=0$ 确有共同形式根 $z=0$，与 $a_*$ 无关。
旧切片判据因而保留这个候选；这里不称每个 $a_*$ 的实际共同谱根都为零。
本稿矩阵块消元处理了这一旧判据未排除的值。
(10.5) 含一个辅助平方与另一个独立线性辅助，
不能删除修正项后称普通 $u^3+v_1^2+v_2$ 已闭。

### 10.1 扣除已有空谱锚范围

R189 的一个空谱锚附录已处理两个加性方向，
以及总增量类秩至多二且含一个实际空谱常系数组合的列表。
这些已有范围不作为本稿新增。

本例的主行正、负子列各自有无限绝对质量，
所以任意固定方向的相位缺陷和都发散。
任意非零常数倍的主行，加上有限个辅助行的线性组合，
只增加一个 $\ell^1$ 行，仍不能变成可和相位缺陷的非可和 first。
主系数为零的组合则有界，不构成空谱 first 锚。
故本列表没有 R189 所需的那个实际空谱组合。
也没有为规避旧范围而把主行改成同射线。

R270C/D 处理单闭 first 的快系数多项式；
这里 $Y_1,Y_2$ 是独立慢有界输入。
本稿使用明确三池行列式处理它们，
没有从单变量快分式场自动推出任意多辅助多项式。

## 11. 范围边界

本稿的全部辅助都可和，故只留下一个闭无界主变量，
并能由真实最高系数单位把原核收入主自然深域。
多个独立无界慢方向仍需另外证明域与可逆性。

矩阵池条件是充分条件。
其行列式必须对全部跨池选列统一受控；
不能只找到若干彼此不兼容的非零小行列式，就套用完整平均。

条件 (2.1) 排除字符纤维上的全梯度零点。
一个高重数或奇异根若所有梯度都为零，
则 (4.2) 没有给出任何单位；
本文不靠较高形式偏导跳过这一步。

对于没有矩阵池、没有可用尾预算的可和极快临界行，
此前的实际成本障碍继续保留。
本稿不把一般多个慢累积量或一般不可约多项式全部判为循环。

## 12. 来源

- [双行平滑字符纤维源](../notes/2026-11-13-two-row-resonant-smooth-character-fibers-and-sylvester-dichotomy-central-review.md)：
  最高主系数完整修正、混合实际 jets、不同根块上的梯度单位及局部次数预算。
- [全阶二位 Bézout 源](../notes/2026-11-13-all-order-resonant-two-site-bezout-and-derivation-budgets-central-review.md)：
  标量输入、完整自然域与原四次配对。
- [R189 一个空谱锚附录](R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md) §§4.1、8：
  已闭范围、共振混合有限插值及真实多模式 jets；本稿不重计其空谱分支。
- [R176](R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  最高系数单位的自然闭域、核内有界 first、完整 $C$ 自伴与图核心。
- [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)：
  完整混合自然词及通常伴随核心。
- [R260](R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md)：
  任意跨度实际壳与完整导子预算。

新增的是 (5.2)–(6.5) 的多行矩阵块消元、
(8.1) 的正确符号与全部阶乘归一化，
以及无需逐位比较的多个独立可和辅助范围。
