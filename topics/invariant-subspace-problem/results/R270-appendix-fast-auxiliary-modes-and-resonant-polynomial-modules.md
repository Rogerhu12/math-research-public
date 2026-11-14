# R270 第五附录：快辅助模式与全阶共振多项式的点态组合

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明。本文是 [R157](R157-fast-modes-one-slow-affine-exponential-weight.md) 的真实无界主模式加强，并把 R270 的全部阶共振族与独立快辅助模式结合。

## 1. 主结论

取任意复主模式及指数权
$$
u=a_*+\sum_j a_j\chi_j,\qquad
w=b_*+\sum_j b_j\chi_j,\qquad a,b\in\ell^2.
\tag{1.1}
$$
主行没有 $\ell^1$、熵、排序下界或相位条件。

另取有限个快辅助模式
$$
z_\ell=d_{\ell,*}+\sum_j c_{\ell j}\chi_j,\qquad 1\le\ell\le d.
$$
记同物理位的联合幅度
$$
s_j=\left(\sum_{\ell=1}^d|c_{\ell j}|^2\right)^{1/2}.
$$
假设其非零支撑有限，或非增重排满足
$$
\boxed{\frac{-\log s_k^*}{k^3}\longrightarrow+\infty.}
\tag{1.2}
$$
辅助与主模式可完全重叠，也可任意独立排列；没有逐位比例条件。
每个辅助行在 $\ell^1$，但可有无限支撑。

对主模式定义
$$
v_n=\sum_j a_j^n(\chi_j-1)\quad(n\ge2),
$$
以及 R270 的共振多项式
$$
F_k
=
k![t^k]\exp\left(
tu+\sum_{n=2}^k\frac{2^{n-1}}n t^nv_n
\right),\qquad F_0=1,\quad F_1=u.
\tag{1.3}
$$

**定理。** 给定任意有限组标量多项式
$h_k\in\mathbb C[y_1,\ldots,y_d]$，若实际点态向量
$$
f=\sum_{k=0}^p h_k(z_1,\ldots,z_d)F_k
\tag{1.4}
$$
非零，则
$$
\boxed{f e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.5}
$$

$p=1$ 给出尤其直接的新接口：
$$
\boxed{
[h_1(z_1,\ldots,z_d)u+h_0(z_1,\ldots,z_d)]e^w
\text{ 非零即循环}.
}
\tag{1.6}
$$
它允许任意 $\ell^2\setminus\ell^1$ 主 first，且不要求
$h_1$ 在辅助字符处非零。
R157 已处理有界 $\ell^1$ 主 first 的仿射式；
本稿新增的正是无界主模式及非单位最高系数的实际域处理。
当 $p\ge2$，本稿使用明确的 $F_k$，不是任意慢模式点态幂 $u^k$。

## 2. 实际算子与有界快参数

令
$$
R_j=V(t_jN_j),\qquad t_j=e^{-2b_j},\qquad X=X_b.
$$
这是 R176 的实际倾斜 first，$e^w\in\mathcal D_\infty(X)$ 且循环。
每个快辅助的真实倾斜 first 为
$$
Y_\ell=d_{\ell,*}I+\sum_j c_{\ell j}R_j.
\tag{2.1}
$$
由于 (1.2)，此和范数绝对收敛，并且
$$
\boxed{Y_\ell\in\mathcal G.}
\tag{2.2}
$$
这里可以直接用已经证明的两类归一化幂预算，完整说明 (2.2) 及后面的混合系数归属。

**局部函数引理。** 设 $\beta_j$ 的非零重排满足 (1.2)，$H$ 为固定多项式且 $H(1)=0$，并且 $t_j=e^{-2b_j}$。
则
$$
\sum_j\beta_j H(V(t_jN_j))\in\mathcal G.
\tag{2.3}
$$
因为 $b\in\ell^2$，$t_j$ 一致有界；在同一个足够小的 $z$ 圆盘内，
$$
\beta_jH(V(t_jz))
=-2\beta_jt_jH'(1)z+f_j(z),
\qquad f_j(0)=f'_j(0)=0,
\tag{2.4}
$$
且全部 $f_j$ 有一致的解析系数界。
一次和 $\sum_j[-2\beta_jt_jH'(1)]N_j$ 的归一化幂系数仍超三次，故由 R151 §6.1 属于 $\mathcal G$。
二阶余和 $\sum_j f_j(N_j)$ 则由 [R270 第二附录](R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md) 的真实局部二阶消去定理属于 $\mathcal G$。
这是两个已经逐项支付的实际和，不使用 $\mathcal G$ 的范数闭性。
二者相加证明 (2.3)。

具体地，
$$
Y_\ell=
\left(d_{\ell,*}+\sum_jc_{\ell j}\right)I
+\sum_jc_{\ell j}(R_j-I).
$$
取 $H(R)=R-1$ 和 $\beta_j=c_{\ell j}$，引理立即给 (2.2)；标量和因快行在 $\ell^1$ 而有定义。

以下只求固定有限阶 jets。
不声称 $\mathcal G$ 对任意范数极限闭合，也不把整个参数函数当成
$\mathcal G$ 值的无穷级数。

## 3. 全变量一位生成式

令
$$
\psi(z)=-\frac12\log(1-2z),\qquad
\lambda_j(\mathbf s)=\sum_{\ell=1}^d s_\ell c_{\ell j}.
$$
在零点附近考虑点态生成函数
$$
\mathscr F(t,\mathbf s)
=
\exp\left[
tu+\sum_{n\ge2}\frac{2^{n-1}}n t^nv_n
+\sum_{\ell=1}^d s_\ell z_\ell+w
\right].
\tag{3.1}
$$
因为 $a$ 有界且平方可和，对固定小 $|t|$，
$n\ge2$ 的和在 $L^\infty$ 中绝对收敛；
辅助模式有界，主 first 及 $w$ 的全部有限指数矩存在。
因此 (3.1) 是某个小多圆盘内的真实 $H$ 全纯函数。

有限位的准确不同位倾斜恒等式把第 $j$ 位对应为
$$
e^{-[\psi(ta_j)-ta_j]}
\bigl[
\cosh(\psi(ta_j)+\lambda_j)I
+R_j\sinh(\psi(ta_j)+\lambda_j)
\bigr].
\tag{3.2}
$$
设
$$
\begin{aligned}
H(z,\lambda;R)
={}&-\psi(z)+z
+\log\bigl(\cosh(\psi(z)+\lambda)+R\sinh(\psi(z)+\lambda)\bigr)\\
&-zR-\lambda R.
\end{aligned}
\tag{3.3}
$$
对数取零点分支。
对每个固定 Taylor 阶数，其系数是 $R$ 的有限多项式。
由于
$$
H(z,\lambda;1)=0,
\tag{3.4}
$$
每个系数多项式在 $R=1$ 消失。

在 $\lambda=0$ 时，R270 的准确恒等式给
$$
H(z,0;R)
=
\sum_{n\ge2}\frac{(-1)^{n-1}}n z^n(R-I)^n.
\tag{3.5}
$$
这保留了全部纯主模式修正，且每项在 $R-I$ 中至少二次。
不是把慢 Bell 修正遗漏。

## 4. 每个实际混合 jet 都属于快代数

定义有界算子参数函数的有限 jets
$$
\mathscr C(t,\mathbf s)
=\sum_j H(ta_j,\lambda_j(\mathbf s);R_j).
\tag{4.1}
$$
该和在小多圆盘内范数一致收敛：
$H$ 没有总参数次数 0 或 1 的项，
统一局部解析界给
$$
\|H(ta_j,\lambda_j;R_j)\|
\le C\bigl(|t|^2|a_j|^2+|\lambda_j|^2+|t a_j||\lambda_j|\bigr).
$$
右边按 $j$ 可和。有限低位可以缩小共同小圆盘处理。

现在逐类验证每个固定非零 Taylor 系数在 $\mathcal G$ 中。

### 4.1 不含快变量的项

由 (3.5)，纯 $t^n$ 系数为
$$
\frac{(-1)^{n-1}}n
\sum_j a_j^n(R_j-I)^n,\qquad n\ge2.
\tag{4.2}
$$
每个局部函数在 $N_j=0$ 至少二阶消去，
在一个与 $j$ 无关的小圆盘内有统一解析预算。
R270B 的局部二阶消去定理遂给 (4.2) 属于 $\mathcal G$。
这一步适用于任意 $\ell^2$ 主行，无须主行快速。

### 4.2 含至少一个快变量的项

取主阶 $r\ge0$、辅助多重指标 $\nu\ne0$。
相应系数是有限线性组合
$$
\sum_j a_j^r
\prod_{\ell=1}^d c_{\ell j}^{\nu_\ell}
\,H_{r,\nu}(R_j),
\qquad H_{r,\nu}(1)=0,
\tag{4.3}
$$
其中 $H_{r,\nu}$ 是固定有限多项式。
$X$ 没有在此和中作无界求值；$a_j^r$ 只是标量系数。

由于 $a\in\ell^2$ 有界，
$$
\left|a_j^r\prod_\ell c_{\ell j}^{\nu_\ell}\right|
\le \|a\|_\infty^r s_j^{|\nu|}.
\tag{4.4}
$$
右侧的非零重排仍满足超三次衰减。
$H_{r,\nu}(1)=0$ 给实际局部表示
$$
H_{r,\nu}(R_j)=N_j U_{r,\nu,j},
\qquad \sup_j\|U_{r,\nu,j}\|<\infty,
\tag{4.5}
$$
且每个 $U_{r,\nu,j}$ 为真解析芽在 $A$ 上的值。
这个局部商来自同一个统一小圆盘的 Taylor 展开和实际 Cayley 演算。
更直接地，将 (4.4) 的快系数作为 $\beta_j$，在第 2 节局部函数引理中取固定多项式 $H_{r,\nu}$：
其一次归一化项由超三次系数支付，全部二阶余项由真实 carry 支付。
因此 (4.3) 确实属于 $\mathcal G$；没有仅从 $\sup_j\|U_{r,\nu,j}\|<\infty$ 外推快类归属。

所以 (4.1) 的每个固定 Taylor 系数都在 $\mathcal G$。
这个结论包括全部主/辅助重叠混合项，没有假设支撑不交。

## 5. 有限 Bell 组合给 $\mathcal G[X]$

由 (3.2) 的有限位乘积、(3.3)，所需的有限 jets 具有形式
$$
\mathscr F(t,\mathbf s)
=
\exp\bigl(\mathscr C(t,\mathbf s)\bigr)
\exp\left(tX+\sum_\ell s_\ell Y_\ell\right)e^w
\quad\text{到任意所需固定阶}.
\tag{5.1}
$$
此式的解释始终是 $H$ 中的真实有限 jets，
不是把整个 $e^{tX}$ 当作全空间有界算子。

对每个固定主阶 $k$ 和辅助多重阶 $\nu$，
右侧的 Taylor 系数是有限个 $\mathscr C$ 系数、$Y_\ell$ 与
$X$ 的多项式，关于 $X$ 的次数至多 $k$。
由 §§2、4 及 $\mathcal G$ 的有限代数封闭性，
所有 $X$ 系数都在 $\mathcal G$。

左侧对 $t$ 取 $k$ 阶导数时正好得到
$$
F_k(u,v_2,\ldots,v_k)
\exp\left(\sum_\ell s_\ell z_\ell+w\right).
$$
再应用 $h_k(\partial_{\mathbf s})$ 并令 $\mathbf s=0$，
逐 $k$ 相加，得到有限多项式
$$
\boxed{
Q_f(t)\in\mathcal G[t],\quad \deg Q_f\le p,\qquad
Q_{f,\rm nat}(X)e^w=f e^w.
}
\tag{5.2}
$$
不要求其实际最高系数的字符非零，也不要求它可逆。

## 6. 真实自然域与截断极限

为明确 (5.2) 的域，固定整个计算所需的有限 Taylor 阶。
保持指数权 $w$ 固定，先把主行与辅助行截断到有限物理集合；(3.2) 是 R147 的不同位恒等式；
所有有限算子有界，可合法作有限微分。

然后取截断极限：

1. 主 first 截断在所有有限 $L^q$ 及与固定指数权相关的有限矩中收敛；
   $e^{w}$ 和所需乘积都在 $H$ 中。
2. 每个 $v_n$ 按 $L^\infty$ 收敛，
   因为 $\sum|a_j|^n<\infty$。
   每个快辅助也按 $L^\infty$ 收敛。
   所以点态左端的所需 jets 在 $H$ 中收敛。
3. $Y_\ell$ 与 (4.1) 的每个固定 jet 按算子范数收敛。
4. R176 的实际倾斜 Bell 幂恒等式给
   $X_m^ke^w\to X^ke^w$ 对每个固定 $k$。
   这可由点态 $u_m^ke^w$ 与二阶以上 Bell 系数的收敛逐阶解出，
   不要求 $X_m$ 在整个 $\operatorname{Dom}X$ 上图收敛。

于是 (5.2) 是准确的自然域等式，
且 $e^w\in\operatorname{Dom}X^p$。
有界混合系数与 $X$ 完整域交换，所有有限词都在该自然域内定义。

## 7. 实际非零条件与循环传递

若实际 $f\ne0$，因为 $e^w$ 几乎处处不为零，
$$
Q_{f,\rm nat}(X)e^w=f e^w\ne0.
$$
所以这是一个实际非零的 $\mathcal G$ 系数自然多项式。
[R270 第四附录](R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md) 给其准确最大闭包单射稠密，
并将每个循环域向量送成循环向量。
$e^w$ 循环且属于自然域，故 (1.5) 成立。

若最高的形式 $h_p$ 在实际辅助模式上发生代数抵消，
(5.2) 的次数可以降低；这不影响结论。
非零标量多项式本身不保证实际 $f$ 非零，
所以定理始终保留点态非零条件。

把 $h_0$ 换为 $h_0-\lambda$ 立即处理全部减标量参数。
如果 $f$ 非本质常数，则 $(f-\lambda)e^w$ 对每个 $\lambda\in\mathbb C$ 循环；
若 $f$ 是常数，只需排除使其为零的那个参数。

## 8. 零字符最高系数的无限例子

取
$$
z=\sum_{j\ge0}e^{-(j+1)^4}\chi_j,\qquad
s=\sum_{j\ge0}e^{-(j+1)^4}.
$$
这是一个与任何主行都可完全重叠的快模式。
$z<s$ 几乎处处：$z=s$ 只有在全部位均为 $+1$ 时出现，
该事件的 Haar 测度为零。
因此
$$
(z-s)^2>0\quad\text{a.e.}
$$

取任意非零无限支撑复 $\ell^2$ 主行；例如
$$
a_j=\frac{(-1)^j}{(j+1)^{3/4}}.
$$
该行不在 $\ell^1$，正负两部分都不可和，故不是 R157 的有界慢模式假设。
本稿给
$$
\boxed{(z-s)^2u\,e^w\text{ 循环}}
$$
对任意复 first 指数权 $w$ 成立。

更一般地，R270 已证无限主支撑下每个 $F_p$ 非零，
故
$$
\boxed{(z-s)^2F_p\,e^w\text{ 循环}\qquad(p\ge0).}
$$
实际最高快系数的字符为 $(s-s)^2=0$，
所以不能用一个未经证明的有界逆把它归一为首一。
去非单位最高系数的闭图定理在这里有直接用途。

## 9. 与原结论的边界

R157 的假设是慢主行 $\ell^1$，使主算子有界后可直接套 R152。
本稿只在真实闭 first 的正则化、有限深核配对和最大闭包
已被 R270 完整处理之后，去掉这个假设。

辅助快速条件仍用于含至少一个快变量的全部混合 jets。
本稿没有把两个任意慢独立 first 都放进 $\mathcal G[X]$，
也没有把普通 $u^p$ 的纯慢 Bell 修正当作快系数。
高阶主模式使用的是 (1.3) 中已准确取消局部一次项的明确族。
