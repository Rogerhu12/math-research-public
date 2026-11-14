# R269：解析 $A$ 系数的 Bell 多项式与有限头多模式循环性

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明；这是原 Haar 空间的中间结论，普通 ISP 未完成。

已对照 R145/R147/R160：旧结论给混合 Bell 域、首位平移互素或非零字符单位，没有覆盖本文的零字符有限头系数全部重数。本文接 R268 的实际熵预算，新增一个真实 $A$ 参数和有限头点态多项式的准确混合 Bell 识别。

## 1. 范围与主结论

取 R268 定理 A 的任意系数行 $a\in\ell^2(\mathbb C)$：
其非零幅度排序 $\rho_k$ 沿无穷尺度 $N$ 满足
$$
\sup_{k\ge N}k\rho_k\le D N\rho_N,
$$
$$
E_N:=\sum_{k\le N}\log(\rho_k/\rho_N)=O(N^2),\qquad
L_N:=1+\log^+(\rho_N^{-1})=O(N^{3/2}).
\tag{1.1}
$$
特别，R268 的弱 $\ell^1$ 上界加子序列指数下界
$$
\sup_k k\rho_k<\infty,\qquad
\liminf_{k\to\infty}k^{-1}\log^+(\rho_k^{-1})<\infty
\tag{1.2}
$$
足够。也允许 R268 的严格超指数阶梯例。

仍取
$$
u=a_*+\sum_ja_j\chi_j,\qquad
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2(\mathbb C),
$$
并使用真实倾斜 first、累积量
$$
t_j=e^{-2b_j},\quad R_j=V(t_jN_j),\quad
X=X_b,\qquad
G_n=\sum_ja_j^nL_n(R_j),\quad n\ge2.
\tag{1.3}
$$

### 1.1 解析系数的首一结论

设
$$
q(\zeta,z)=z^p+\sum_{k<p}h_k(\zeta)z^k,\qquad p\ge1,
\tag{1.4}
$$
其中每个 $h_k$ 是零点邻域上的真实解析芽。
定义有限 Bell 多项式
$$
\mathcal P(\zeta,z;\kappa)
=\exp\!\left(\sum_{n=2}^p
\frac{\kappa_n}{n!}\partial_z^n\right)q(\zeta,z),
\qquad
T=\mathcal P(A,X;G).
\tag{1.5}
$$
指数在有限多项式空间上截断。

**定理 A。**
$$
\boxed{
\operatorname{Dom}T=\operatorname{Dom}X^p,\qquad
\ker T=\{0\},\qquad \overline{\operatorname{Ran}T}=H.
}
\tag{1.6}
$$
因此
$$
\boxed{
u^pe^w+\sum_{k<p}h_k(A)(u^ke^w)
\text{ 循环}.
}
\tag{1.7}
$$
(1.7) 中 $h_k(A)$ 是实际有界交换算子作用，绝非点乘。
更一般的首系数 $h_p(A)$ 只要 $h_p(0)\ne0$，可先以解析单位除去。

### 1.2 有限头点态符号

设 $H_0=\{0,\ldots,h-1\}$，并在关系 $x_j^2=1$ 下先约化
$$
P(z,x_0,\ldots,x_{h-1})
=\sum_{F\subset H_0}p_F(z)x_F.
\tag{1.8}
$$
若它关于 $z$ 首一，则
$$
\boxed{
P(u,\chi_0,\ldots,\chi_{h-1})e^w
\text{ 循环}.
}
\tag{1.9}
$$
更一般地，若最高 $z$ 次系数为有限头函数 $g_p$，
只需 $g_p(1,\ldots,1)\ne0$。
全部根和各头分支的重数均可不同。

允许把有限头坐标换成任意有限个有限支撑 first 模式；代入后再按 (1.8) 约化即可。
例如 $(u^2-\chi_0)e^w$ 在 (1.1) 的全部行上循环。
这里没有把第二个无限慢模式收入结论。

### 1.3 有界 first 的非首一加强

若另外 $a\in\ell^1$，则 (1.4) 的首一条件可去掉：
任何非零解析系数多项式 $q(\zeta,z)$ 所给的 (1.5) 都单射稠密。
因此 (1.8) 中只要至少一个 $p_F$ 非零，
不要求任何最高系数的零点锚条件，(1.9) 仍成立。
例如
$$
[(1-\chi_0)u^2+(1+\chi_0)u]e^w
$$
在这个有界 first 子类中循环。

## 2. 首一自然域和核内有界 first

(1.5) 是首一的 $\mathcal A$ 系数 $X$ 多项式，次数为 $p$。
正式文件
[R176](R176-natural-polynomial-maximal-graphs-and-bell-domains.md)
的 §2 (2.1)--(2.2) 明确允许任意有界 $\{A\}'$ 系数且最高系数可逆，
以低阶相对界任意小证明自然图范数等价；§4 (4.2) 证明整个
$C_0$ 伴随域，§5 (5.1)--(5.3) 证明任意循环域向量的图核心和像循环判据。
其 §10.1 (10.5) 后的段落又明确把这个范围扩到真实有界倾斜 $X_b$，
不只处理特定的标量 Bell 多项式。
因此 $T$ 在准确域 $\operatorname{Dom}X^p$ 上闭、$C_0$ 自伴，
$e^w$ 是其真实图循环基向量。
R176 §8 (8.1)--(8.2) 对同一任意系数范围证明：
若 $M=\ker T$，则
$$
M\subseteq\mathcal D_\infty
:=\bigcap_{k\ge0}\operatorname{Dom}X^k,\qquad
X_M=X|_M\in B(M),
\tag{2.1}
$$
且全部 $\mathcal A$ 元素保持 $M$。
记 $B_M=\|X_M\|$。

每个 $h_k(A)$ 以原 $A$ 的真实全纯演算定义。
解析半径可以小于 $\|A\|$；这里使用围住零谱且位于解析域内的小圆周，不把原幂级数在错误的范数圆盘内代入。

## 3. 物理高位反射作用于 $A$ 的真实导子壳

本节是新增域步骤。记 $\delta_XB=[X,B]$，采用 R260 的完整域定义及范数
$$
\|B\|_{\delta_X}
=\sum_{s\ge0}\frac{\|\delta_X^sB\|}{s!}.
$$
该范数代数完备，Neumann 逆同时是实际逆并保完整域及全部自然幂域。

用原物理权 $\alpha_\ell$（不是归一化幂系数 $d_\ell$）写
$$
A=\sum_{\ell\ge0}\alpha_\ell W_\ell,\qquad
W_\ell=E_0^*\cdots E_{\ell-1}^*E_\ell,
$$
$$
\|W_\ell\|=1,\qquad
\alpha_{\ell+1}/\alpha_\ell=\eta_\ell,\qquad
0<\eta_\ell\le e^{-770\,16^\ell}.
\tag{3.1}
$$
这是 R260 使用的实际串展开的 $j=0$ 情形。

设 $F$ 是任意有限位集，$m=\min F\ge1$，
$J_F=\prod_{j\in F}M_{\chi_j}$、
$\gamma_F=\operatorname{Ad}J_F$。
当 $\ell<m$ 时整个局部串不变，故准确有
$$
\gamma_F(A)-A
=\sum_{\ell\ge m}B_{\ell,F},\qquad
B_{\ell,F}=\alpha_\ell(\gamma_F(W_\ell)-W_\ell),
$$
$$
\|B_{\ell,F}\|\le2\alpha_\ell
\le2\alpha_0\eta_{\ell-1}.
\tag{3.2}
$$
每个壳只作用于前 $\ell+1$ 位。

R260 的完整闭尾交换给，所有真实导子阶数都可在该壳上用有界头计算：
$$
\delta_X^sB_{\ell,F}
=\operatorname{ad}_{H_\ell}^sB_{\ell,F},\qquad
H_\ell=a_*I+\sum_{j\le\ell}a_jR_j.
$$
即使第一个交换子已非局部，此等式仍成立，因为 $H_\ell$ 和原壳都与同一个完整闭尾交换。
有
$$
2\|H_\ell\|\le C_0+C_1\|a\|_2\sqrt{\ell+1}.
$$
因此
$$
\|B_{\ell,F}\|_{\delta_X}
\le2\alpha_\ell
e^{C_0+C_1\|a\|_2\sqrt{\ell+1}}.
$$
求和得到
$$
\boxed{
\|\gamma_F(A)-A\|_{\delta_X}
\le\epsilon_m,\qquad
\epsilon_m\le C e^{-385\,16^{m-1}}.
}
\tag{3.3}
$$
常数不含 $|F|$ 或 $\max F$。

现在取任意固定解析芽 $h$。
选一个位于其解析域内的小圆周 $\Gamma$。
$R(z)=(z-A)^{-1}\in\mathcal A$，故
$\|R(z)\|_{\delta_X}=\|R(z)\|$，在 $\Gamma$ 上统一有界。
充分大 $m$ 时，
$$
(z-\gamma_F(A))^{-1}
=(I-R(z)(\gamma_F(A)-A))^{-1}R(z)
$$
在真实导子 Banach 代数内由 Neumann 级数成立。
于是实际 Cauchy 逆差给
$$
\boxed{
\|\gamma_F(h(A))-h(A)\|_{\delta_X}
\le C_h\epsilon_m.
}
\tag{3.4}
$$
两个元组之间不要求交换；预解式乘积按固定顺序。
(3.4) 的所有阶导数都是真正的保域导数，绝非仅有全空间范数小。

后续只对原固定有限个 $h_k$ 使用 (3.4)。
随 $N,F$ 改变的 Hermite 逆不需要共轭：左反射顺序使它先在 $M$ 内消去。

## 4. 新 $A$ 圆周的实际预算

原四次幂界给某些固定 $K,c>0$
$$
\|A^k\|\le K e^{-ck^4}.
$$
对任何 $\zeta\ne0$，实际绝对 Neumann 级数给
$$
\zeta(\zeta-A)^{-1}
=\sum_{k\ge0}\zeta^{-k}A^k.
$$
利用
$-ck^4+kL\le-(c/2)k^4+C_cL^{4/3}$，
得到
$$
\boxed{
\|\zeta(\zeta-A)^{-1}\|
\le K'\exp[C'(1+\log^+|\zeta|^{-1})^{4/3}].
}
\tag{4.1}
$$
这对所有复方向成立。

取满足 (1.1) 的尺度 $N$、$\delta=\rho_N$。
R268 的真实累积量联合预算，加上 (4.1)，给下述共同多圆周估计：
$$
|\zeta|=\varepsilon\delta^p,\qquad
|\kappa_n|=\varepsilon\delta^n,\quad 2\le n\le p.
\tag{4.2}
$$
若 $F(\zeta,\kappa)$ 在这些闭圆盘的邻域全纯、边界模长 $\le M_F$，则
$$
\boxed{
\|F(A,G_2,\ldots,G_p)\|
\le K M_F
\exp[C(E_N+L_N^{4/3}+N^2)].
}
\tag{4.3}
$$
每个圆周长度消去对应预解式的逆半径。
$A$ 坐标只增加固定常数乘 $L_N^{4/3}$，
已经包含在 R268 的原预算内。
所有参数一次共同求值，没有按反射位数重复支付。

## 5. 带 $A$ 参数的保重数 Hermite 余式

记 $q_0(z)=q(0,z)$，它仍首一、次数 $p$。
取 $q_0$ 的各根及其重数 $\mu_\nu$。
存在固定足够小的 $\varepsilon,\delta_0,a_0>0$，使在
$$
|\zeta|\le2\varepsilon\delta^p,\qquad
|\kappa_n|\le2\varepsilon\delta^n
\tag{5.1}
$$
内，$\mathcal P(\zeta,z;\kappa)$ 的各根团都落在
$|z-\lambda_\nu|<\delta/8$，并保留原总重数。

具体地，
$q(\zeta,z)-q_0(z)=\zeta\,h(\zeta,z)$；
在各固定根邻域中 $h$ 及有限个导数有界。
$|\zeta|\le2\varepsilon\delta^p$ 的扰动是
$O(\varepsilon\delta^p)\le O(\varepsilon\delta^{\mu_\nu})$。
纯 Bell 参数的权 $\deg\kappa_n=n$ 给与 R266 相同的
$O(\varepsilon\delta^{\mu_\nu})$ 界。
取 $\varepsilon$ 小后由 Rouché 得上述根团，不需要根简单。

若 $|F|=r$ 且 $\delta\le|a_j|\le a_0$，置
$$
\mathscr L_a(\zeta,z;\kappa)
=-2[\mathcal P(\zeta,z-2a;\kappa)
-\mathcal P(\zeta,z;\kappa)].
$$
各原根团与 $2a_j$ 平移团隔开。
R266 的真正圈积分余式遂给次数小于 $p$ 的 $\mathcal R_F$，
系数在 (5.1) 内全纯，满足
$$
\mathcal R_F\prod_{j\in F}\mathscr L_{a_j}
=1+\mathcal P\mathcal S_F,
$$
$$
|[z^k]\mathcal R_F|
\le C_q^{r+1}\delta^{-pr-p+1}.
\tag{5.2}
$$
积分分母是 $\mathcal P$ 与
$\prod_{j\in F}[-2\mathcal P(\zeta,z-2a_j;\kappa)]$；
它的非零性和系数界均在同一个带 $A$ 参数的多圆盘上成立。

用 (4.3) 对每个系数一次求值，在 $M$ 上设
$$
\mathfrak R_F
=\mathcal R_F(A|_M,X_M;G|_M).
$$
有
$$
\left(\prod_{j\in F}\mathscr L_{a_j}(A,X;G)\right)
\mathfrak R_F f=f,\quad f\in M,
$$
$$
\boxed{
\log^+\|\mathfrak R_F\|
\le K(E_N+L_N^{4/3}+N^2)+K_qrL_N+K_M.
}
\tag{5.3}
$$
与 R268 的完整输入成本相同。

## 6. 原自然域上的反射幂与平均

按 R268 选取前 $N$ 幅度，删去幅度前 $N/4$ 和物理前 $N/4$。
取 $Q_N=\lfloor N/2\rfloor$ 个实际位为 $I_N$，
$r=\lceil\sqrt{N/c}\rceil$，其中 $c>0$ 稍后固定。
则
$$
\min I_N\ge\lfloor N/4\rfloor,\quad
\rho_N\le|a_j|\le2\|a\|_2/\sqrt N,
$$
且所有 $r$ 元子集的 $\sum_F|a_j|$ 一致有界。
不用同幅比，也不控制最大物理位。

R260 给
$\gamma_FX=\widehat X_F+E_{X,F}$、
$\gamma_FG_n=\widehat G_{n,F}+E_{n,F}$，
全部基本误差在真实 $\delta_X$ 范数中
$\le\epsilon_N=Ce^{-38516^{\lfloor N/4\rfloor-1}}$。
本稿的 (3.4) 再把系数
$\gamma_Fh_k(A)-h_k(A)$ 纳入相同的误差类。
定义带帽算子时保持 $A$ 参数不变：
$$
\widehat T_F
=\mathcal P(A,\widehat X_F;\widehat G_F),
\qquad A_F=\widehat T_F-T.
$$

R268 的正规排序词证明逐字适用：
每个含误差的 $pr$ 阶词只有 $O_p(r)$ 个有界字母，
总导数阶数至多 $pr$。
在同一 $M$ 的输入 jets 上只付
$\epsilon_N e^{C r\log(r+2)}$，
且全部字母和导数保 $\mathcal D_\infty$。
特别，
$$
\|[(\gamma_FT)^r-\widehat T_F^r]\mathfrak R_Ff\|
\le\epsilon_N e^{C r\log(r+2)}
\|\mathfrak R_F\|\|f\|.
\tag{6.1}
$$

Boolean 替身为
$$
\widetilde A_F=
\mathcal P\left(
A,X+4\sum_{j\in F}a_jt_jN_j;\
G_n+4L_n'(1)\sum_{j\in F}a_j^nt_jN_j
\right)-\mathcal P(A,X;G).
$$
固定的 $A$ 参数不参与高位线性项。
仍有
$$
4L_n'(1)=-2(-2)^n,\qquad
\partial_{\kappa_n}\mathcal P=\partial_z^n\mathcal P/n!,
$$
故一次项正是
$\sum_{j\in F}t_jN_j\mathscr L_{a_j}(A,X;G)$。
$r$ 个正次因子给
$$
\widetilde A_F^r
\equiv r!t_FN_F
\prod_{j\in F}\mathscr L_{a_j}(A,X;G)
\pmod{(N_j^2:j\in F)}.
$$
每个弃项真含 $\eta_j$，全部系数在 $M$ 上的绝对范数和
由固定 $B_M$、解析系数范数及 $\sum_F|a_j|$ 控制为 $C^r$。

左反射
$$
T^rJ_F\mathfrak R_Ff
=J_F(\gamma_FT)^r\mathfrak R_Ff
$$
让 (5.3) 的有限差乘积先在 $M$ 内消去。
再用 $J_jE_j=-E_j$，得到与 R268 相同的实际主项
$$
T^rJ_F\mathfrak R_Ff
=(-1)^rr!t_F\prod_{j\in F}E_jf
+\text{已付真实误差}.
$$
定义
$$
\mathcal V_N=(-1)^r(2/Q_N)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F.
$$
则其像属于所需共同深域，且
$$
T^r\mathcal V_Nf\rightharpoonup e^{-1/c}f,
$$
$$
\log^+\|\mathcal V_N\|
\le K(E_N+L_N^{4/3}+N^2)+K_qrL_N+O(r)+K_M.
\tag{6.2}
$$
真正的误差上界为这个输入成本乘
$\epsilon_Ne^{Cr\log(r+2)}$，再加 $2^rr\eta_{\lfloor N/4\rfloor}$；
两者都趋零。

反射输入的 $X$ jets 仍由
$X^kJ_Ff_F=J_F(\gamma_FX)^kf_F$
及正规排序支付：
对每个固定物理头 $h$，
$$
\|Z_h^k\mathcal V_Nf\|
\le2A_N R_{h,M,c}^k\|f\|,
\quad 0\le k\le(p-1)r,
\tag{6.3}
$$
其中 $Z_h=X-a_*I-\sum_{j<h}a_jR_j$，
$A_N$ 是 (6.2) 的绝对系数上界。
新增解析 $A$ 参数不改变这些实际 jets。

## 7. 解析系数的局部 $A$ 因子与排核

固定前 $h$ 位上的局部矩阵 $D_0$。
以 $q_0(z)=q(0,z)$ 定义真正的尾多项式
$$
T_{\rm tail}
=\exp\!\left(\sum_{n=2}^p
G_{n,\ge h}\partial_z^n/n!\right)
q_0(z)\Big|_{z=Z_h+s_h},
\quad s_h=a_*+\sum_{j<h}a_j.
$$
$D_0$ 与这个闭尾表达完整交换。

有限低头的 $X,G_n$ 差都有 R268 的明确有界 $A$ 因子。
新增部分也准确有
$$
h_k(A)-h_k(0)=A\widetilde h_k(A),
$$
其中 $\widetilde h_k$ 是真实解析芽。
因此
$$
T-T_{\rm tail}=A W_h(Z_h),\qquad
\deg W_h\le p-1,
\tag{7.1}
$$
系数在 $\mathcal A$ 中有界。
首一系数恒为1保证最高 $z^p$ 项的这个差消失；
未将一般零字符元直接除以 $A$。

所以在 $\mathcal D_\infty$ 上
$\operatorname{ad}_T^rD_0=\operatorname{ad}_{AW_h(Z_h)}^rD_0$。
保持 $A$ 在 $D_0$ 两侧而不穿过它，(6.3) 给
$$
\|(\operatorname{ad}_T^rD_0)\mathcal V_Nf\|
\le
2\|D_0\|A_N C_{h,M,c}^r
e^{-(5/6)r^4+105r^3}\|f\|.
\tag{7.2}
$$
由 (1.1)、(6.2)，选择同一个固定小 $c$ 使
$K_0c^2+K_1c^{3/2}<1/4$，
即可使 (7.2) 对每个固定局部矩阵趋零。
$c$ 不依赖这个局部测试。

完整 $C_0$ 自伴性和深域 Leibniz 给
$$
\mathcal B(D_0T^r\mathcal V_Nf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD_0)\mathcal V_Nf,g)
\quad(f,g\in M).
$$
左端趋 $e^{-1/c}\mathcal B(D_0f,g)$，右端趋零。
原局部全矩阵代数不可约，故 $M=0$。
$C_0$ 自伴性给像稠密；R176 图循环判据给 (1.7)。
这证明定理 A。

## 8. 有界 first 时去掉首一条件

现在假设 $a\in\ell^1$，故
$X\in\mathcal A$ 有界，字符为
$$
s=a_*+\sum_ja_j.
$$
$\mathcal A$ 中 $A$ 及各 $G_n$ 的字符为零。
设 $q(\zeta,z)$ 为任意非零解析系数多项式。
若它的 $z$ 次数为零，则 $q(A)=A^m h(A)$、$h(0)\ne0$，
其中 $h(A)$ 是实际单位；$A^m$ 单射稠密，结论直接成立。
以下考虑正 $z$ 次数。

先取各非零系数解析芽的最小消失阶 $m<\infty$，写
$$
q(\zeta,z)=\zeta^m\widetilde q(\zeta,z),
\qquad \widetilde q(0,z)\not\equiv0.
$$
有限 Bell 算子与这个因子交换，所以
$T=A^m\widetilde T$。
$A^m$ 单射，故两者核相同。
以下将 $\widetilde q$ 重新记为 $q$，其最大 $z$ 次数记为 $p$。

若 $q(0,s)\ne0$，$T\in\mathcal A$ 的字符非零，已经是单位。
否则 $s$ 是非零多项式 $q_0=q(0,\cdot)$ 的某个重数 $\mu\ge1$ 的根。
取围住 $s$、不含 $q_0$ 其他根的固定小圆。
参数 $(\zeta,\kappa)$ 足够小时，圆内准确有 $\mu$ 个根。
对它们的幂和用
$$
\frac1{2\pi i}\int z^\ell
\frac{\partial_z\mathcal P(\zeta,z;\kappa)}
{\mathcal P(\zeta,z;\kappa)}\,dz
$$
定义，再用有限 Newton 恒等式，得到参数解析的首一 $\mu$ 次因子
$W(\zeta,z;\kappa)$。
多项式长除法给
$$
\mathcal P=U W,
$$
$U$ 的系数也解析，且 $U(0,s;0)\ne0$。
因此 $U(A,X;G)\in\mathcal A$ 是实际单位。
从 $Tf=0$ 得
$$
W(A,X;G)f=0.
\tag{8.1}
$$

在缩小的参数多圆盘
$|\zeta|\le2\varepsilon\delta^p$、
$|\kappa_n|\le2\varepsilon\delta^n$ 上，
这个根团保持在 $|z-s|<\delta/8$。
对足够小的选中 $|a_j|$，
$-2\mathcal P(\zeta,z-2a_j;\kappa)$
在 $|z-s|\le\delta/4$ 无零，且模长下界为固定常数乘 $\delta^\mu$。
现在在 Hermite 余式的分母和差商中使用首一因子 $W$，
在 $H_F$ 中仍使用原
$\prod_j[-2\mathcal P(\zeta,z-2a_j;\kappa)]$。
得到次数小于 $\mu$ 的 $\mathcal R_F$，满足
$$
\mathcal R_F\prod_{j\in F}\mathscr L_{a_j}
=1+W\mathcal S_F.
$$
系数界不超过 §5 所用的较松
$C^{r+1}\delta^{-pr-p+1}$。
由 (8.1)，仍得到核内真实逆 (5.3)。

§6 的有限差及 Boolean 恒等式使用原 $\mathcal P$，无需其首一性；
全部算子在这里已全域有界。
局部差 $T-T_{\rm tail}$ 仍有真实 $A$ 因子，
但其 $Z_h$ 次数可以是 $p$。
因为 $X,Z_h$ 有界，整个因子 $U_h$ 仍有界，
直接有
$$
\|\operatorname{ad}_T^rD_0\|
\le\|D_0\|(2\|U_h\|)^r
e^{-(5/6)r^4+105r^3}.
$$
同一输入成本和弱配对排除核。
乘回单射的 $A^m$ 不改变结论。
$T\in\mathcal A$ 的 $C_0$ 对称性给像稠密。
这证明 §1.3 的非首一加强。

这个加强只在 $a\in\ell^1$ 的全域有界情形使用。
没有据此宣布一般非单位最高系数的闭自然图或未知核上的 $X$ 自动有界。

## 9. 有限头点乘的准确混合 Bell 识别

本节明确支付 (1.8)--(1.9)，不把 $\chi_j$ 点乘当作 $R_j$ 的算子乘法。
若约化后的 $P$ 关于 $z$ 的次数为零，它是非零有限头函数 $g$；
其实际倾斜乘子是非零解析芽 $h(A)$，由 $h(A)e^w=g e^w$ 识别。
写 $h(A)=A^m h_0(A)$、$h_0(0)\ne0$，直接得到循环性。
这一度零处理不依赖 §8 中 $\mu\ge1$ 的根团步骤。

对有限 $F\subset H_0$，定义真正的二变量解析芽
$$
K_F(t,\zeta)
=\prod_{j\in F}
V\left(e^{-2(b_j+a_jt)}\frac{\zeta^{2^j}}{d_j}\right).
\tag{9.1}
$$
有限头确保其在 $(t,\zeta)=(0,0)$ 的邻域解析，
所有分母在该点为1。
$K_F(t,0)=1$ 对全部小 $t$ 成立。

实际有限位倾斜恒等式给
$$
\left[\prod_{j\in F}V(e^{-2(b_j+a_jt)}N_j)\right]
e^{tu+w}
=\chi_Fe^{tu+w}.
\tag{9.2}
$$
可先对 $u,w$ 的有限截断验证。
每个位的准确有理比值是
$$
\frac{\sinh(a_jt)I+R_j\cosh(a_jt)}
{\cosh(a_jt)I+R_j\sinh(a_jt)}
=V(e^{-2(b_j+a_jt)}N_j).
\tag{9.3}
$$
有限个不交位因子作用于基向量后就是对应的点态 $\chi_F$。
有限截断的 $H$ 极限和这些固定有界因子的连续性给 (9.2)。

只需要有限阶 $t$-jets。
R145/R176 的真实倾斜 Bell 恒等式给
$$
e^{tu+w}
=\exp\!\left(\sum_{n=2}^pG_nt^n/n!\right)
e^{tX}e^w
\quad\text{到 }t\text{ 的 }p\text{ 阶 jet}.
\tag{9.4}
$$
这里 $e^{tX}e^w$ 的符号只表示由真实
$X^ke^w\in H$ 构成的有限 Taylor jet；
不声称 $e^{tX}$ 在全 $H$ 上有界。
(9.4) 可在有限截断中求导，再用各实际自然幂向量和累积量的收敛传到原空间。

把 $p_F(z)=\sum_k c_{F,k}z^k$ 写开，定义
$$
\boxed{
q(\zeta,z)=
\sum_{F\subset H_0}\sum_k c_{F,k}
\sum_{\ell=0}^k\binom k\ell
\partial_t^\ell K_F(0,\zeta)\,z^{k-\ell}.
}
\tag{9.5}
$$
这是一个真正的解析 $\zeta$ 系数多项式。
对 (9.2)--(9.4) 作有限阶导数及 Leibniz 展开，得到完整实际等式
$$
\boxed{
P(u,\chi_{H_0})e^w
=
\left[
\exp\!\left(\sum_{n=2}^p
\frac{G_n}{n!}\partial_z^n\right)q(A,z)
\right]_{z=X}e^w.
}
\tag{9.6}
$$
(9.5) 中所有 $\ell\ge1$ 项正是有限头与主模式重叠产生的混合 Bell 项。
它们不能删掉。

由于 $K_F(t,0)=1$，
$$
q(0,z)=\sum_Fp_F(z)=P(z,1,\ldots,1).
\tag{9.7}
$$
若 $P$ 关于 $z$ 首一，则最高项仅来自 $F=\varnothing$，
所以 $q(\zeta,z)$ 也首一。
更一般的最高系数为
$$
c_p(\zeta)=\sum_F c_{F,p}K_F(0,\zeta),
\qquad c_p(0)=g_p(1,\ldots,1).
$$
若这个零点值非零，$c_p(A)$ 是实际解析单位；
除去它后应用定理 A，再乘回有界交换单位，得到 (1.9)。

若 $a\in\ell^1$，只需 (1.8) 约化后至少一个系数多项式非零。
取最大的真实 $z$ 次数 $p$，其有限头系数 $g_p$ 非零。
上式最高解析系数满足
$$
c_p(A)e^w=g_p(\chi_{H_0})e^w\ne0.
$$
因为 $e^w$ 几乎处处非零，非零有限头函数有正测非零集。
故 $c_p(\zeta)$ 不是零芽，$q(\zeta,z)$ 不是零多项式。
§8 的非首一结论适用，完成 §1.3 的点态推论。

## 10. 一个核验例子与范围

以 $P(z,x_0)=z^2-x_0$ 为例，(9.5) 给
$$
q(\zeta,z)=z^2-V(t_0\zeta/d_0).
$$
因而实际乘子是
$$
X^2+G_2-R_0,
$$
作用于 $e^w$ 恰为 $(u^2-\chi_0)e^w$。
这是真正的有限头耦合，既没有把 $R_0$ 与点乘 $\chi_0$ 认同为全空间算子，
也没有把 $u^2$ 偷换成 $X^2$。

当 $P$ 含 $z\chi_0$ 时，(9.5) 还出现
$\partial_tK_{\{0\}}(0,A)$；
这项通常不为零，恰展示必须保留的混合修正。

本文完成的是：在 R268 的行条件下，
解析 $A$ 系数的首一 Bell 多项式、有限头辅助的首一/锚单位点态多项式；
在 $a\in\ell^1$ 子类中还去掉有限头最高系数限制。
没有把两个独立无限慢模式或任意有限 chaos 收入结论。
规则 $1<\alpha\le3/2$ 行的全部重数仍不由本稿消失，
因为原 R268 熵条件尚未在该类闭合。
正常湮灭者、边界 $N=M$ 和普通 ISP 仍开放。

## 依赖

R109 原四次幂；R145/R147 的真实混合 jets 与有限位倾斜；
R176 自然首一多项式最大图及图循环；
R260 完整导子 Banach 代数和真实物理串；
R266 非同幅 Hermite；
R268 实际熵联合预算、全部自然词与平方弱平均。
