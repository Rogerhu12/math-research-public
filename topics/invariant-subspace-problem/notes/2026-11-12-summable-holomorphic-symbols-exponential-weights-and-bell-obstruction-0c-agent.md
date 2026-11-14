# R160：任意可和联合模式的全纯符号倾斜、零点锚单位与慢 Bell 型障碍

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。根代理预留 R160。

状态：完整证明。前半部分覆盖无限 chaos 的全纯点态符号，不要求任何快速尾。后半部分给出一个自然慢二阶 Bell 修正确实不属于 $\mathcal G$ 的严格证明，控制整个算子幂的误差。它不是不循环向量或非平凡核的反例。

## 1. 任意 $\ell^1$ 联合模式的结论

取任意有限个第一阶模式

$$
u_\nu=a_{\nu,*}+\sum_{j\ge0}a_{\nu j}\chi_j,
\qquad a_{\nu\cdot}\in\ell^1,
\qquad 1\le\nu\le d.
\tag{1.1}
$$

它们有连续代表，令

$$
U=(u_1,\ldots,u_d):\Omega=\{0,1\}^{\mathbb N}\longrightarrow\mathbb C^d,
\qquad K=U(\Omega),
$$

$$
\beta_\nu=u_\nu(0)=a_{\nu,*}+\sum_j a_{\nu j},
\qquad \beta=(\beta_1,\ldots,\beta_d)\in K.
\tag{1.2}
$$

$K$ 是紧集，不要求凸、连通或没有代数关系。
设 $F$ 在 $K$ 的某个开邻域全纯，并取任意复第一阶指数

$$
w=c_*+\sum_jc_j\chi_j,\qquad c\in\ell^2.
\tag{1.3}
$$

**定理 1.1。** 存在规范的实际有界算子 $\Psi_w(F(U))\in\mathcal A$，满足

$$
\boxed{
F(U)e^w=\Psi_w(F(U))e^w,
\qquad
\chi(\Psi_w(F(U)))=F(\beta).
}
\tag{1.4}
$$

特别地，

$$
\boxed{
F(\beta)\ne0\Longrightarrow F(U)e^w
\text{ 对本题实际 }A\text{ 循环}.
}
\tag{1.5}
$$

这包括全部 $\lambda\ne F(\beta)$ 时的
$(F(U)-\lambda)e^w$。
当 $F(\beta)=0$ 时，本定理仍构造有界乘子，但不自动排除它的核。

没有快速重排、首位次序、相位或独立支撑假设。
$F$ 可以产生无限 Walsh 次数；例如对任意 (1.1) 和任意在 $K$ 邻域全纯的 $G$，

$$
\boxed{\exp(G(U)+w)\text{ 循环},}
\tag{1.6}
$$

因为 $F=e^G$ 满足 $F(\beta)\ne0$。
这允许 $G$ 是重叠慢模式的非线性函数。

## 2. 加权绝对 Walsh 代数与实际倾斜映射

对 $\kappa\ge1$，定义

$$
\mathscr W_\kappa
=\left\{
f=\sum_{J\subset\mathbb N,\ |J|<\infty}\widehat f(J)\chi_J:
\|f\|_{\mathscr W_\kappa}
:=\sum_J|\widehat f(J)|\kappa^{|J|}<\infty
\right\}.
\tag{2.1}
$$

这种级数一致收敛，故定义连续函数，且

$$
\|f\|_\infty\le\|f\|_{\mathscr W_\kappa}.
$$

$\mathscr W_\kappa$ 是 Banach 代数，乘法是实际点乘。
因为 $\chi_J\chi_L=\chi_{J\triangle L}$ 且
$|J\triangle L|\le|J|+|L|$，

$$
\|fg\|_{\mathscr W_\kappa}
\le\|f\|_{\mathscr W_\kappa}\|g\|_{\mathscr W_\kappa}.
\tag{2.2}
$$

绝对求和保证对称差卷积合法。完备性来自加权 $\ell^1$ 的完备性。

沿用

$$
N_j=A^{2^j}/d_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1},
\qquad d_j=W_{2^j}.
$$

对固定指数系数 $c_j$，置

$$
R_j(c_j)
=(V_j\cosh c_j+I\sinh c_j)
(I\cosh c_j+V_j\sinh c_j)^{-1}.
\tag{2.3}
$$

分母的字符为 $e^{c_j}\ne0$，所以它是 $\mathcal A$ 的真实单位。
等价的精确式为

$$
\boxed{
R_j(c_j)
=(I-e^{-2c_j}N_j)(I+e^{-2c_j}N_j)^{-1}.
}
\tag{2.4}
$$

因此每个 $R_j(c_j)$ 属于 $\mathcal A$，字符为1，而且各位算子彼此交换。

### 2.1 对全部物理位的统一有界性

$c_j\to0$，且 $\|V_j\|\le6$。
选固定小 $\delta>0$，使 $|z|\le\delta$ 时

$$
|\cosh z-1|+6|\sinh z|\le1/2.
$$

于是这些高位的 (2.3) 分母逆范数至多2，分子范数也有统一界。
余下低位有限，各自的真实逆有有限范数。
所以

$$
M_c:=\sup_j\|R_j(c_j)\|<\infty.
\tag{2.5}
$$

取 $\kappa\ge\max(1,M_c)$。
对 $f\in\mathscr W_\kappa$ 定义

$$
\boxed{
\Psi_w(f)=\sum_J\widehat f(J)R_J(c),
\qquad R_J(c)=\prod_{j\in J}R_j(c_j).
}
\tag{2.6}
$$

这是算子范数绝对收敛和，并有

$$
\|\Psi_w(f)\|\le\|f\|_{\mathscr W_\kappa},
\qquad
\chi(\Psi_w(f))=\sum_J\widehat f(J)=f(0).
\tag{2.7}
$$

$w$ 的常数项不进入 (2.3)，但仍保留在向量 $e^w$ 中。

这里 $\Psi_w$ 是线性映射，**不**是点态乘法的代数同态。
例如 $\chi_j^2=1$，而由 (2.4)，

$$
R_j(c_j)^2-I
=-4e^{-2c_j}N_j(I+e^{-2c_j}N_j)^{-2}\ne0,
$$

因为 $N_j$ 单射非零，其余因子为单位。
所以不能把点态全纯演算直接替换成 $\Psi_w$ 像的通常算子全纯演算。

## 3. 指数向量上的真实作用

对有限位集合 $J$，有

$$
\boxed{\chi_Je^w=R_J(c)e^w.}
\tag{3.1}
$$

先对有限截断的 $w$ 验证。记

$$
T_j(z)=\cosh z\,I+V_j\sinh z.
$$

真实恒等式 $V_J1=\chi_J$ 给

$$
e^{w_N}=e^{c_*}\prod_{j<N}T_j(c_j)1.
$$

而

$$
R_j(c_j)T_j(c_j)=V_j\cosh c_j+I\sinh c_j.
$$

将这条式子用于 $j\in J$，其他因子不变，展开后恰对应
$\chi_Je^{w_N}$，因为各位至多出现一次，$V_L1=\chi_L$ 对有限 $L$ 精确成立。
固定 $J$ 后令截断包含 $J$ 并趋于无穷。
R145/R147 的指数矩及 R16 乘积极限给
$e^{w_N}\to e^w$ 于 $H$；固定的有界 $R_J(c)$ 允许取极限，得到 (3.1)。

现在 $f\in\mathscr W_\kappa$ 的有限 Walsh 和同时在函数一致范数和 (2.6) 的算子范数中收敛。
因 $e^w\in H$，(3.1) 线性相加并取极限得

$$
\boxed{fe^w=\Psi_w(f)e^w.}
\tag{3.2}
$$

R147 已证明任意 (1.3) 的 $e^w$ 循环。
如果 $f(0)\ne0$，(2.7) 及 $\mathcal A$ 的唯一字符谱性质使 $\Psi_w(f)$ 为有界交换单位。
所以 (3.2) 的向量循环。

因此定理 1.1 只剩证明：对任意有限 $\kappa$，给定的 $F(U)$ 都属于 $\mathscr W_\kappa$。

## 4. 非凸紧值域上的有限头全纯展开

固定 $\kappa\ge1$。
因 $F$ 在紧集 $K$ 的开邻域全纯，可选 $\delta>0$，使

$$
K+\{z:\|z\|_\infty\le4\delta\}
$$

包含于该开邻域，并使 $|F|\le M$ 在这个紧邻域上成立。

取足够大的有限物理头 $[0,m)$，使对每个 $\nu$ 都有

$$
\kappa\sum_{j\ge m}|a_{\nu j}|<\delta.
\tag{4.1}
$$

令尾函数

$$
r_\nu=\sum_{j\ge m}a_{\nu j}\chi_j,
\qquad
\|r_\nu\|_{\mathscr W_\kappa}
=\kappa\sum_{j\ge m}|a_{\nu j}|<\delta.
\tag{4.2}
$$

对每个头模式 $\varepsilon\in\{-1,1\}^m$，置

$$
c_{\varepsilon,\nu}
=a_{\nu,*}+\sum_{j<m}a_{\nu j}\varepsilon_j,
\qquad
c_\varepsilon=(c_{\varepsilon,1},\ldots,c_{\varepsilon,d}).
$$

任选该头模式的一个无限尾，所得 $U$ 值在 $K$ 内，且与 $c_\varepsilon$ 的每个坐标相差不超过
$\sum_{j\ge m}|a_{\nu j}|<\delta$。
因此 $\operatorname{dist}_\infty(c_\varepsilon,K)<\delta$。

以 $c_\varepsilon$ 为中心、各半径 $2\delta$ 的闭多圆盘落在 $K$ 的 $3\delta$ 邻域内，故 $F$ 在其上全纯且有界 $M$。
多变量 Cauchy 界给

$$
F(c_\varepsilon+z)=\sum_{\alpha\in\mathbb N^d}
f_{\varepsilon,\alpha}z^\alpha,
\qquad
|f_{\varepsilon,\alpha}|\le M(2\delta)^{-|\alpha|}.
\tag{4.3}
$$

在真正的点乘 Banach 代数 $\mathscr W_\kappa$ 中代入 $(r_1,\ldots,r_d)$。
由 (4.2)—(4.3) 和 (2.2)，

$$
\sum_\alpha |f_{\varepsilon,\alpha}|
\prod_{\nu=1}^d\|r_\nu\|_{\mathscr W_\kappa}^{\alpha_\nu}
\le
M\prod_{\nu=1}^d
\left(1-\frac{\|r_\nu\|_{\mathscr W_\kappa}}{2\delta}\right)^{-1}
\le M2^d.
\tag{4.4}
$$

所以这一尾 Taylor 和在 $\mathscr W_\kappa$ 中绝对收敛。

头模式指示函数

$$
p_\varepsilon
=\prod_{j<m}\frac{1+\varepsilon_j\chi_j}{2}
$$

属于 $\mathscr W_\kappa$，且

$$
\|p_\varepsilon\|_{\mathscr W_\kappa}
=\left(\frac{1+\kappa}{2}\right)^m.
$$

有限头分解

$$
F(U)=\sum_{\varepsilon\in\{-1,1\}^m}
p_\varepsilon
\sum_\alpha f_{\varepsilon,\alpha}
r_1^{\alpha_1}\cdots r_d^{\alpha_d}
\tag{4.5}
$$

在 $\mathscr W_\kappa$ 中成立。
事实上右边在 $\mathscr W_\kappa$ 中收敛，从而一致收敛；每个物理点只有一个头指示非零，其 Taylor 和精确等于对应 $F(U)$。
一个明确有限界为

$$
\|F(U)\|_{\mathscr W_\kappa}
\le M2^d(1+\kappa)^m.
\tag{4.6}
$$

不要求这个界对不同 $\kappa$ 或不同截断 $m$ 一致。

$\kappa$ 任意，故

$$
\boxed{F(U)\in\bigcap_{\kappa\ge1}\mathscr W_\kappa.}
\tag{4.7}
$$

整个构造分别在有限头中心附近展开，没有假定 $K$ 的凸包也包含在 $F$ 定义域内。
它允许不连通邻域及不同头所在的不同解析分支。
同时，(4.4) 用的是 Walsh 点乘代数，不是非同态 $\Psi_w$ 的算子像。

取 §2 的 $\kappa\ge M_c$，用 §§2–3 即证明 (1.4)—(1.5)。
(1.6) 用 $F=e^G$ 即得。

## 5. 一个纯慢二阶 Bell 修正确实不属于 $\mathcal G$

下面完整检验 R157 慢变量高次项的一个真实障碍。
取

$$
v=a_*+\sum_j a_j\chi_j,
\qquad a_0\ne0,
\qquad a_j=(j+1)^{-2}\quad\text{对充分大 }j.
\tag{5.1}
$$

有限前缀可以任意修改，包括复相位；仍有 $a\in\ell^1$。
令

$$
D=\sum_j a_j^2(I-V_j^2)
=4\sum_j a_j^2N_j(I+N_j)^{-2}\in\mathcal A.
\tag{5.2}
$$

这是 norm-entire Bell 函数
$\prod_jH(ta_j,V_j)$ 在零点的二阶导数：
$H(0,V)=I$、$H'(0,V)=0$、$H''(0,V)=I-V^2$。
级数按范数绝对收敛，因为 $\sum|a_j|^2<\infty$。

**定理 5.1。** 实际全空间算子 $D$ 满足

$$
\boxed{\operatorname{ord}D=1,\qquad \tau_4(D)=0,
\qquad D\notin\mathcal G.}
\tag{5.3}
$$

证明将控制整个 $\|D^n-(D_m^{\rm app})^n\|$，不只控制选中的某个有序项。

### 5.1 真实低头截断

使用精确物理递推

$$
N_j=E_j+\eta_jE_j^*N_{j+1},
\qquad E_j=e_{10}^{(j)},\qquad
N_j^2=\eta_jN_{j+1},
\qquad \eta_j\le e^{-770\,16^j}.
\tag{5.4}
$$

对 $m\ge1$，从上往下定义

$$
Q_{m,m}=0,\qquad
Q_{j,m}=E_j+\eta_jE_j^*Q_{j+1,m}
\quad(0\le j<m).
\tag{5.5}
$$

$Q_{j,m}$ 只作用于第 $j,\ldots,m-1$ 位。
它按物理二进位数把头向上移 $2^j$，在头的最上端停止，所以是严格三角的有限维头算子。
递推的二乘二块形式还给

$$
\|Q_{j,m}\|=1,\qquad
Q_{j,m}^2=\eta_jQ_{j+1,m}.
$$

由 (5.4)—(5.5) 逐层相减，

$$
\|N_j-Q_{j,m}\|
\le\prod_{i=j}^{m-1}\eta_i
\le\eta_{m-1}
\le e^{-770\,16^{m-1}}
\quad(j<m).
\tag{5.6}
$$

这里每个 $\eta_i<1$，未从单个低位误差直接替换成一个没有根据的高位误差。

### 5.2 一个不要求交换的统一函数差界

设

$$
K(X)=4X(I+X)^{-2}.
$$

对 $X=N_j,Q_{j,m}$ 或 $E_j$，都有 $\|X\|\le1$、$\|(I+X)^{-1}\|<3$。
例如前两者由

$$
(I+X)^{-1}=(I-X)(I-X^2)^{-1},
\qquad \|X^2\|\le\eta_j
$$

得到逆界；$E_j^2=0$ 时直接成立。

如果 $X,Y$ 满足这两个界，记 $R_X=(I+X)^{-1}$、$R_Y=(I+Y)^{-1}$。
预解式恒等式给

$$
\|R_X-R_Y\|\le9\|X-Y\|,
$$

而

$$
R_X^2-R_Y^2
=R_X(R_X-R_Y)+(R_X-R_Y)R_Y
$$

给平方差界 $54\|X-Y\|$。
于是

$$
\boxed{\|K(X)-K(Y)\|\le252\|X-Y\|.}
\tag{5.7}
$$

此计算不要求 $X,Y$ 交换。
并且 $K(E_j)=4E_j$。

令 $A_2=\sum_j|a_j|^2<\infty$，构造

$$
D_m^{\rm app}
=\sum_{j<m}a_j^2K(Q_{j,m})
+4\sum_{j\ge m}a_j^2E_j
=:H_m+B_m.
\tag{5.8}
$$

$H_m$ 只作用于低 $m$ 位且严格三角，$B_m$ 只作用于其余尾位，所以它们交换。
两算子都一致有界：

$$
\|D\|,\ \|D_m^{\rm app}\|\le36A_2.
\tag{5.9}
$$

由 (5.6)、(5.7) 及 $\|N_j-E_j\|\le\eta_j$，得到完整范数误差

$$
\begin{aligned}
\|D-D_m^{\rm app}\|
&\le252\sum_{j<m}|a_j|^2 e^{-770\,16^{m-1}}
 +252\sum_{j\ge m}|a_j|^2e^{-770\,16^j}\\
&\le252A_2e^{-770\,16^{m-1}}.
\end{aligned}
\tag{5.10}
$$

### 5.3 整个 $n$ 次幂的误差预算

令 $M=1+36A_2$。
即使 $D$ 与 $D_m^{\rm app}$ 不交换，有限望远镜仍给

$$
\boxed{
\|D^n-(D_m^{\rm app})^n\|
\le252A_2\, nM^{n-1}e^{-770\,16^{m-1}}.
}
\tag{5.11}
$$

取

$$
m=m_n=\lceil\log_2(n+1)\rceil.
$$

则 $16^{m-1}\ge(n+1)^4/16$，所以

$$
\|D^n-(D_{m_n}^{\rm app})^n\|
\le252A_2\, nM^{n-1}
\exp\!\left[-\frac{770}{16}(n+1)^4\right].
\tag{5.12}
$$

这就是 $m\asymp\log n$ 时所需的全算子幂误差
$\exp[-c n^4+O(n)]$。

### 5.4 一个精确纯尾矩阵元

取两个单位有限张量向量：

- 低 $m$ 位在输入、输出中都取全零物理态；
- 位 $m,\ldots,m+n-1$ 在输入中全零，在输出中全一；
- 其余位都取常参考向量。

$H_m$ 的每个正幂在低头全零态上的对角矩阵元为零。
$H_m,B_m$ 交换，所以 $(D_m^{\rm app})^n$ 的这个矩阵元仅剩 $B_m^n$。

尾 $E_j$ 是真实独立平方零 raising 算子。
要把选定的 $n$ 个位全部从0变为1，恰好必须在 $n$ 个因子中各使用这些位一次。
其他项至少漏掉一个所选位，矩阵元为零。
绝对范数收敛允许展开，因此该矩阵元精确为

$$
4^n n!\prod_{j=m}^{m+n-1}a_j^2.
\tag{5.13}
$$

当 $n$ 足够大，所有这些位已经超过 (5.1) 的有限修改段。
又 $m_n\le n$（$n\ge2$），故其模长 $\ell_n$ 满足

$$
\ell_n
=4^n n!\prod_{j=m_n}^{m_n+n-1}(j+1)^{-4}
\ge4^n n!(2n)^{-4n}
=\exp[-O(n\log n)].
\tag{5.14}
$$

(5.12) 除以 (5.14) 趋于零，所以充分大 $n$ 有

$$
\|D^n\|
\ge\ell_n-
\|D^n-(D_{m_n}^{\rm app})^n\|
\ge\frac12\ell_n.
$$

于是 $\tau_4(D)\le0$。
另一方面任意有界算子均满足
$-\log\|D^n\|\ge-n\log\|D\|$，所以 $\tau_4(D)\ge0$。
故

$$
\tau_4(D)=0.
$$

(5.2) 中最低形式项来自 $j=0$，系数为 $4a_0^2/d_0\ne0$；其余 $j\ge1$ 至少为二阶。
故 $\operatorname{ord}D=1$。
如果 $D\in\mathcal G$，R151 的精确型定理将给
$\tau_4(D)=100/15$，矛盾。
定理 5.1 得证。

## 6. 慢变量扩展的准确边界

本稿给出一个确实越过 R157 仿射形式的正结论：
任意有限 $\ell^1$ 模式的全纯符号，只要 $F(\beta)\ne0$，允许任意次数甚至无限 chaos，并允许任意 $\ell^2$ 指数权。
例如对慢模式

$$
v=\sum_{j\ge0}(j+1)^{-2}\chi_j
$$

已有

$$
\exp(v^2+w)\text{ 循环}
$$

对全部 (1.3) 成立。

但一般临界 $F(\beta)=0$ 未由单位论证解决。
定理 5.1 还严格排除了以下未经证明的补法：把慢模式所有高阶 Bell 系数都收入 $\mathcal G$，再直接套 R152 的 $\mathcal G[S]$ 多项式定理。
甚至自然的二阶修正就可以不属于 $\mathcal G$。

为将这一障碍放在真正的临界符号旁，允许在 (5.1) 中取有限前缀

$$
a_0=1,\qquad
a_1=-\sum_{j\ge2}(j+1)^{-2},\qquad
a_j=(j+1)^{-2}\ (j\ge2),\qquad a_*=0.
$$

这时 $\beta=\sum_j a_j=1$，而 $f=v^2-1$ 非零，其
$\chi_0\chi_2$ 系数为 $2/9$，但 $f(0)=0$。
它的自然实际乘子为

$$
X_v^2+D-I.
$$

上面的 $D\notin\mathcal G$ 证明仍成立，因为只改了有限前缀。
因此这个分解不能被无证据地当成 $\mathcal G[X_v]$ 的那个标准二次表达式。
这不是断言不存在其他有用表示，也不是断言该向量不循环。
它准确说明了本稿的单位方法与 R157 的直接快系数方法尚未提供什么。

本稿不将 $\Psi_w$ 视为点态代数同态，也不从有界乘子存在推断零字符算子无核。
完整 ISP、一般慢临界全纯符号以及一般高阶核问题仍未由这些结论解决。

依赖与对应接口：

- R32：$\mathcal A$ 的唯一字符、形式忠实性及单点谱。
- [R147：任意第一阶指数的 R16 循环性与实际 Bell 整轨道](../notes/2026-11-12-exponential-weighted-first-mode-polynomial-cyclicity-0c-agent.md)。
- [R156：局部莫比乌斯倾斜因子与有限位实际作用](../notes/2026-11-12-bounded-finite-chaos-exponential-tilt-and-empty-anchor-0c-agent.md)。
- [R151：$\mathcal G$ 的精确首阶四次型](../notes/2026-11-12-quartic-analytic-approximation-gauge-stability-0c-agent.md)。
- [R157：快模式与一个慢模式的仿射点态式](../notes/2026-11-12-fast-modes-one-slow-affine-point-symbol-exponential-0c-agent.md)。
- R158 的有限头全纯展开使用相同的紧值域思路；本稿前半只取其无需快尾的加权绝对 Walsh 部分，并在 §§2–4 给出完整证明。
