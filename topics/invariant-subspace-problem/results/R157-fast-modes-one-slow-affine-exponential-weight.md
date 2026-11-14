# R157：快模式与一个任意慢 $\ell^1$ 模式的仿射点态式及指数权

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。根代理预留 R157。

状态：完整证明。使用 R154 的快 Bell 系数与 R152 的 $\mathcal G$ 系数多项式排核。慢方向只要求系数绝对可和，不要求空谱、首位次序、相位或平移互素。点态式对这个慢方向保持仿射；不把一般慢方向的高阶 Bell 系数归入 $\mathcal G$。

## 1. 结论

取有限个快模式

$$
u_\nu=a_{\nu,*}+\sum_{j\ge0}a_{\nu j}\chi_j,
\qquad 1\le\nu\le d,
$$

记联合幅度

$$
s_j=\left(\sum_{\nu=1}^d|a_{\nu j}|^2\right)^{1/2}.
$$

假定非零联合幅度有限，或其非增重排满足

$$
\frac{-\log s_\ell^*}{\ell^3}\longrightarrow+\infty.
\tag{1.1}
$$

另取一个任意复慢模式及任意指数方向

$$
v=b_*+\sum_j b_j\chi_j,\qquad b\in\ell^1,
$$

$$
w=c_*+\sum_j c_j\chi_j,\qquad c\in\ell^2.
\tag{1.2}
$$

允许所有模式的支撑完全重叠，也允许常数模式。
对任意标量多项式 $r,q\in\mathbb C[z_1,\ldots,z_d]$，令

$$
f=r(u_1,\ldots,u_d)v+q(u_1,\ldots,u_d).
\tag{1.3}
$$

**定理 1.1。** 若实际点态函数 $f$ 不是零向量，则

$$
\boxed{f e^w\text{ 对本题实际 }A\text{ 循环}.}
\tag{1.4}
$$

如果 $f$ 非本质常数，则 $(f-\lambda)e^w$ 对全部 $\lambda\in\mathbb C$ 都循环；若 $f$ 为常数，只排除使括号为零的那个参数。

更具体地，证明构造

$$
S_w\in\mathcal A,\qquad
\gamma_\zeta(S_w)-S_w\in\mathbb C\{A\}
\quad(\zeta\text{ dyadic}),
$$

以及 $a_w,b_w\in\mathcal G$，使

$$
f e^w=B_w(a_wS_w+b_w)\xi_w,
\tag{1.5}
$$

其中 $B_w$ 是有界交换单位，$\xi_w$ 循环。
只要 $f\ne0$，实际算子 $a_wS_w+b_w$ 非零，因而由 R152 单射稠密。

## 2. 有界模式、指数基与倾斜 Bell 函数

沿用实际算子

$$
N_j=A^{2^j}/W_{2^j},\quad
V_j=(I-N_j)(I+N_j)^{-1},
$$

以及

$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z).
$$

(1.1) 保证 $\sum_js_j<\infty$，所以全部 $u_\nu$ 与 $v$ 都连续有界。
它们的实际第一阶乘子也有界：

$$
X_\nu=a_{\nu,*}I+\sum_j a_{\nu j}V_j,\qquad
Z=b_*I+\sum_j b_jV_j,
\tag{2.1}
$$

级数按算子范数绝对收敛，且 R154 给 $X_\nu\in\mathcal G$。
这里没有对 $Z$ 假定快速四次尾型。

令

$$
\lambda_j(t)=\sum_{\nu=1}^d t_\nu a_{\nu j},
\qquad
\mathcal B(t,s,\tau)=\prod_j H(\lambda_j(t)+s b_j+\tau c_j,V_j).
$$

所有系数列属于 $\ell^2$，所以 R145 的联合 Bell 定理给一个范数整单位函数。
置

$$
B_w=\mathcal B(0,0,1),\qquad
\xi_w=B_w^{-1}e^w,
$$

$$
\widetilde B(t,s)=\mathcal B(t,s,1)B_w^{-1}.
\tag{2.2}
$$

R147 的 R16 乘积论证给 $e^w\in H$ 且循环，故 $\xi_w$ 循环。
$B_w$ 和 $\widetilde B$ 均属于 $\mathcal A$，前者可逆，后者对全部有限参数为单位。

## 3. 慢方向一次项的真实中心化

定义

$$
C_0=\partial_s\widetilde B(0,0)
=\sum_j b_jH'(c_j,V_j)H(c_j,V_j)^{-1}.
\tag{3.1}
$$

此和范数绝对收敛。对高位 $j$，$c_j\to0$ 且 $\|V_j\|$ 一致有界，局部对数导数由常数乘 $|c_j|$ 控制，所以相应项范数受 $C|b_jc_j|$ 控制；该乘积可和。
有限低位的因子各自为有界解析乘子，单独保留。
于是 $C_0\in\mathcal A$。

重要的是它的每个 dyadic 差仍为真正解析芽。
若 $\zeta$ 的阶为 $2^m$，则 $\gamma_\zeta(N_j)=N_j$ 对全部 $j\ge m$ 成立。
因此 (3.1) 中这些高位项被严格固定；范数绝对收敛允许逐项取 gauge 差，得到

$$
\begin{aligned}
\gamma_\zeta(C_0)-C_0
=\sum_{j<m}b_j\bigl[&H'(c_j,\gamma_\zeta(V_j))
H(c_j,\gamma_\zeta(V_j))^{-1}\\
&-H'(c_j,V_j)H(c_j,V_j)^{-1}\bigr].
\end{aligned}
\tag{3.2}
$$

每个 $V_j$ 是 $A$ 的真正有理解析芽；$H(c_j,V_j)$ 的字符为 $H(c_j,1)=1$，所以其逆也是真正标量解析芽在 $A$ 上的演算。
故 (3.2) 是有限真解析和，不仅是一个抽象 $A$ 幂的有界倍数。

$Z$ 的 gauge 差也只有有限个低位项，故同为真解析。
令

$$
S_w=Z+C_0,\qquad
\widehat B(t,s)=e^{-sC_0}\widetilde B(t,s).
\tag{3.3}
$$

便有

$$
\boxed{\gamma_\zeta(S_w)-S_w\in\mathbb C\{A\}
\subseteq\mathcal G,}
\tag{3.4}
$$

而且

$$
\widehat B(0,0)=I,\qquad
\partial_s\widehat B(0,0)=0.
\tag{3.5}
$$

不要求 $C_0$ 或 $S_w$ 本身属于 $\mathcal G$。
如需使用 R152 的零字符规范化，可把 $S_w$ 减去其字符，并把这个常数吸收进 (1.5) 的 $b_w$，不影响 $\mathcal G$ 系数结构。

## 4. 带至少一个快系数的混合 Bell 项属于 $\mathcal G$

记

$$
B_{\mathrm{fast}}(t)=\widetilde B(t,0)=\widehat B(t,0),
\qquad
B_\alpha=\partial_t^\alpha B_{\mathrm{fast}}(0).
$$

R154 给

$$
B_\alpha\in\mathcal G\qquad(\alpha\in\mathbb N^d),
\quad B_0=I.
\tag{4.1}
$$

对每个位取局部对数

$$
L_j(z)=\log H(z,V_j),
$$

在谱点1处以 $\log1=0$ 规范化。
R154 §3 的实际 $\rho N_j$ 计算已证明：对每个固定 $k\ge1$，

$$
L_j^{(k)}(c_j)=N_jU_{kj},
\qquad\sup_j\|U_{kj}\|<\infty,
\tag{4.2}
$$

且每个 $U_{kj}$ 都是真正解析芽在 $A$ 上的值。
统一范数来自真实 $N_j^2=\eta_jN_{j+1}$ 的逆界和小圆盘 Cauchy 估计；有限低位的解析商另作有限最大值。此处不从形式零常数项擅自推断有界除法。

局部对数导数给

$$
\partial_s\widehat B(t,0)
=B_{\mathrm{fast}}(t)J(t),
$$

$$
J(t)=\sum_jb_j\bigl[L_j'(c_j+\lambda_j(t))-L_j'(c_j)\bigr],
\qquad J(0)=0.
\tag{4.3}
$$

这些和在小紧参数邻域范数一致绝对收敛。
例如高位的局部二阶导数一致有界，差的范数由 $C|b_j||\lambda_j(t)|$ 控制；$b\in\ell^1$、$s_j$ 有界使其可和。
有限低位选共同小邻域即可。
因此可用 Cauchy 微分逐项求每个固定多重导数。

对 $\alpha\ne0$，令 $k=|\alpha|$、$a_j^\alpha=\prod_\nu a_{\nu j}^{\alpha_\nu}$。由 (4.2)，

$$
J_\alpha:=\partial_t^\alpha J(0)
=\sum_j b_j a_j^\alpha L_j^{(k+1)}(c_j)
=\sum_j b_j a_j^\alpha N_jU_{k+1,j}.
\tag{4.4}
$$

设 $B=\sup_j|b_j|<\infty$。有

$$
|b_j a_j^\alpha|\le B s_j^k.
$$

非零系数的降序模长因而仍满足超三次条件 (1.1)。
R154 的带真正解析统一有界因子尾引理，使用真实归一化幂的重复占据估计，给

$$
\boxed{J_\alpha\in\mathcal G\quad(\alpha\ne0),
\qquad J_0=0.}
\tag{4.5}
$$

再令

$$
D_\alpha=\partial_t^\alpha\partial_s\widehat B(0,0).
$$

Leibniz 公式与 (4.3) 给有限和

$$
D_\alpha
=\sum_{\beta\le\alpha}\binom{\alpha}{\beta}
B_\beta J_{\alpha-\beta}.
\tag{4.6}
$$

全部项都属于 $\mathcal G$，故

$$
\boxed{D_\alpha\in\mathcal G,\qquad D_0=0.}
\tag{4.7}
$$

这只涉及每个固定导数的有限 Bell/Leibniz 组合，没有使用 $\mathcal G$ 对任意范数极限封闭的未证性质。

## 5. 点态式的实际有界乘子

所有 $X_\nu,Z,S_w,C_0$ 都有界且交换。
有限位截断的真实生成恒等式、范数极限和 R145/R147 给

$$
\boxed{
e^{\sum_\nu t_\nu u_\nu+s v+w}
=B_w\widehat B(t,s)
e^{\sum_\nu t_\nu X_\nu+sS_w}\xi_w.
}
\tag{5.1}
$$

这里没有新增的无界乘法域：快模式与 $v$ 的截断在函数一致范数收敛，实际 $X_\nu,Z$ 的截断在算子范数收敛，$e^{w_N}\to e^w$ 在 $H$ 中，而 Bell 单位及其逆局部一致范数收敛。
因此 (5.1) 可先对截断验证再取极限；两边关于有限参数都是 $H$ 整函数。
左边的整性也直接来自 $u_\nu,v$ 有界和 $e^w\in H$。

对任意多项式 $p$，定义

$$
\mathcal P_p
=\sum_{\alpha\ge0}\frac{B_\alpha}{\alpha!}
(\partial^\alpha p)(X_1,\ldots,X_d),
$$

$$
\mathcal D_p
=\sum_{\alpha\ge0}\frac{D_\alpha}{\alpha!}
(\partial^\alpha p)(X_1,\ldots,X_d).
\tag{5.2}
$$

每个和都有限。由 $X_\nu,B_\alpha,D_\alpha\in\mathcal G$，

$$
\mathcal P_p,\mathcal D_p\in\mathcal G.
\tag{5.3}
$$

对 (5.1) 先关于 $s$ 求一次导数，再关于 $t$ 施加 $r(\partial_t)$ 并在零点取值，得到

$$
r(u_1,\ldots,u_d)v e^w
=B_w(\mathcal P_rS_w+\mathcal D_r)\xi_w.
$$

不关于 $s$ 求导而施加 $q(\partial_t)$，则有

$$
q(u_1,\ldots,u_d)e^w=B_w\mathcal P_q\xi_w.
$$

合并为

$$
\boxed{
f e^w=B_wT_f^w\xi_w,\qquad
T_f^w=\mathcal P_rS_w+\mathcal D_r+\mathcal P_q
\in\mathcal G[S_w].
}
\tag{5.4}
$$

这就是 (1.5)，其中 $a_w=\mathcal P_r$、$b_w=\mathcal D_r+\mathcal P_q$。
中心化 (3.3) 的作用是让混合系数的零阶项消失；若不中心化，慢一次项 $C_0$ 一般不能被直接收入 $\mathcal G$ 常数系数中。

## 6. 排核、循环传递与准确非零条件

由于 $f$ 有界、$e^w\in H$，加权向量确实属于 $H$。
$e^w$ 几乎处处非零，所以 $f\ne0$ 保证 $f e^w\ne0$。
(5.4) 遂给 $T_f^w\ne0$。

(3.4) 使 $S_w$ 满足 R152 的 gauge 假设。
(5.3) 使 (5.4) 是 $\mathcal G$ 系数的有限多项式，因此 R152 §7 给

$$
\ker T_f^w=0,\qquad\overline{T_f^wH}=H.
$$

$\xi_w$ 循环且 $T_f^w$ 是有界稠密像交换子，所以 $T_f^w\xi_w$ 循环。
再乘有界交换单位 $B_w$，即得 $f e^w$ 循环，定理 1.1 完成。

反向，若 $f=0$，则 (5.4) 给 $T_f^w\xi_w=0$；由 $\xi_w$ 循环与 $T_f^w$ 有界交换，可知 $T_f^w=0$。
因此这里的非零条件精确对应实际点态函数，不要求模式代数独立，也不从非零标量多项式本身推断向量非零。

把 $q$ 换为 $q-\lambda$ 可处理全部 $f-\lambda$，给 §1 的参数结论。
当 $w=0$ 时，$B_w=I$、$\xi_w=1$，所以 $T_f^01=f$ 是该点态函数的真实有界乘子；一般指数权时不声称整个加权函数来自一个有界点乘算子。

## 7. 一个完全重叠的无限例子

取实模式

$$
u=\sum_{j\ge0}e^{-(j+1)^4}\chi_j,\qquad
v=\sum_{j\ge0}(j+1)^{-2}\chi_j.
$$

二者都在每个位有非零系数，$u$ 满足超三次重排条件，$v$ 仅要求绝对可和且可任意慢。
点态函数

$$
f=(1+u^2)v
$$

非零：$u$ 为实函数，$1+u^2\ge1$，而 $v\ne0$。
故对任意复 $\ell^2$ 第一阶指数 $w$，

$$
\boxed{(1+u^2)v e^w\text{ 循环}.}
$$

这个结论没有空谱第一阶锚；$u,v$ 的乘子均有界。
它也没有要求慢模式满足超三次条件，更没有要求模式支撑不交。

## 8. 范围

慢模式 $v$ 的 $\ell^1$ 假设用于得到真实有界 $Z\in\mathcal A$，从而可直接应用 R152。
本稿没有把任意 $\ell^2\setminus\ell^1$ 的无界第一阶代入该有界多项式定理。

同样，若对 $v$ 求二次或更高次幂，会出现不带任何快系数的纯慢高阶对数导数
$\sum_j b_j^kN_jU_{kj}$；本稿没有证明这些算子属于 $\mathcal G$。
所以结论保留关于单个慢变量的仿射形式，而没有扩大成任意多变量点态多项式。

一般超越分支的 $T_f^w\in\mathcal G[S_w]$ 仅已证明全空间单射稠密；不能因此声称它在每个未知不变限制上像稠密。
完整 Hilbert ISP 及一般慢高阶核仍未由本稿解决。

依赖：

- [R154：快模式全部点态多项式与指数权、统一对数导数商](../notes/2026-11-12-supercubic-modes-all-polynomials-and-exponential-weights-0c-agent.md)。
- [R152：$\mathcal G$ 系数多项式的实际排核](../notes/2026-11-12-fast-gauge-increments-analytic-germs-and-closed-quotients-0c-agent.md)。
- [R147：指数基循环性与倾斜 Bell](../notes/2026-11-12-exponential-weighted-first-mode-polynomial-cyclicity-0c-agent.md)。
- [R145：真实多模式 Bell 恒等式](../notes/2026-11-12-multimode-bell-mixed-domains-cyclicity-0c-agent.md)。
