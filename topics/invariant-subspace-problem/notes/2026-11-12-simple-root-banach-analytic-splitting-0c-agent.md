# R142 接口：交换拟幂零系数上的简单根解析分裂

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。

状态：完整自含证明。本稿只提供根代理 R142 所需的 Banach 代数分裂及真实幂域接口，不单凭分裂宣称每个因子已有零核或稠密像。系数算子的通常范数不需要小。

## 1. 结论

设 $\mathscr B$ 为复幺 Banach 代数，$B_2,\ldots,B_p\in\mathscr B$ 两两交换且拟幂零。置 $B_0=I$、$B_1=0$。取首一标量多项式

$$
q(w)=\prod_{\rho\in\mathcal R}(w-\rho),
\qquad |\mathcal R|=p,
$$

假定其全部根互不相同。定义中心不定元 $w$ 上的算子系数多项式

$$
P(w)=\sum_{k=0}^p\frac{B_k}{k!}q^{(k)}(w)
=q(w)I+\sum_{k=2}^p\frac{B_k}{k!}q^{(k)}(w).
\tag{1.1}
$$

**分裂定理。** 存在 $Y_\rho$，均属于 $I,B_2,\ldots,B_p$ 生成的闭交换子代数，使

$$
\boxed{P(w)=\prod_{\rho\in\mathcal R}(wI-Y_\rho).}
\tag{1.2}
$$

它们满足：

- $Y_\rho-\rho I$ 拟幂零；
- 不同根的 $Y_\rho-Y_\sigma$ 在同一闭子代数中可逆；
- 对任意连续角色 $\chi$，$\chi(Y_\rho)=\rho$；
- 若原 $B_k$ 属于 $\mathscr B$ 的 Jacobson 根基，则 $Y_\rho-\rho I$ 也属于该根基。

特别地，根代理的 $B_k\in\mathcal A_h$ 情形完全在 $\mathcal A_h$ 内分裂。没有将系数移入更大的算子代数，也没有使用 $\|B_k\|$ 小的假设。

当 $p=1$ 时结论只是 $P(w)=wI-\rho I$。以下写 $p\ge2$；零次首一多项式 $q=1$ 对应空乘积 $I$。

## 2. 有限参数的标量根芽

令 $\beta=(\beta_2,\ldots,\beta_p)\in\mathbb C^{p-1}$，考虑

$$
P_\beta(w)=q(w)+\sum_{k=2}^p\frac{\beta_k}{k!}q^{(k)}(w).
\tag{2.1}
$$

因为 $k\ge2$，扰动项次数小于 $p$，所以 $P_\beta$ 始终是首一 $p$ 次多项式。

对每个简单根 $\rho$，选以 $\rho$ 为中心的小圆 $\Gamma_\rho$，使这些闭圆盘互不相交，且每个盘中 $q$ 只有根 $\rho$，圆周上不为零。令

$$
\delta=\min_{\rho}\min_{w\in\Gamma_\rho}|q(w)|>0,
\qquad
M_k=\max_{\rho}\max_{w\in\Gamma_\rho}
\frac{|q^{(k)}(w)|}{k!}.
$$

选正数 $r_2,\ldots,r_p$，使

$$
\sum_{k=2}^p r_kM_k<\delta/2.
\tag{2.2}
$$

那么在参数多圆盘 $|\beta_k|<r_k$ 内，各圆周上
$|P_\beta-q|<|q|$。Rouché 的零点计数说明：每个圆盘中 $P_\beta$ 恰有一个零点，按重数计也是1。总共已有 $p$ 个零点，故没有遗漏其他根。

定义

$$
y_\rho(\beta)=\frac1{2\pi i}
\int_{\Gamma_\rho}
w\,\frac{\partial_wP_\beta(w)}{P_\beta(w)}\,dw.
\tag{2.3}
$$

这是圆内唯一的根。它关于全部参数联合解析：由 (2.2)，圆周上的分母倒数有关于参数一致收敛的几何展开

$$
\frac1{P_\beta(w)}
=\frac1{q(w)}
\sum_{n\ge0}\left(
-\frac{\sum_{k=2}^p\beta_kq^{(k)}(w)/k!}{q(w)}
\right)^n,
$$

因此可以逐项积分，也可直接使用含参数 Cauchy 积分。特别有收敛根芽

$$
y_\rho\in\mathbb C\{\beta_2,\ldots,\beta_p\},
\qquad y_\rho(0)=\rho.
\tag{2.4}
$$

两边均首一，且根及重数完全相同，所以在上述参数邻域中有真正的解析系数恒等式

$$
\boxed{
P_\beta(w)=\prod_{\rho\in\mathcal R}(w-y_\rho(\beta)).
}
\tag{2.5}
$$

根芽不依赖满足要求的小圆选择：在两个构造的共同小参数邻域内，靠近同一简单根的唯一零点相同，因而芽相同。

## 3. 范数不小的交换拟幂零元上可以求值全部收敛芽

以下步骤明确区别“标量参数需要小”和“算子系数范数需要小”。前者用于构造根芽，后者不需要。

### 引理 3.1：绝对范数求值

设 $T_1,\ldots,T_m$ 两两交换且各自拟幂零。若

$$
g(z)=\sum_{\nu\in\mathbb N_0^m}c_\nu z^\nu
\in\mathbb C\{z_1,\ldots,z_m\},
$$

则

$$
g(T_1,\ldots,T_m)
=\sum_\nu c_\nu T_1^{\nu_1}\cdots T_m^{\nu_m}
\tag{3.1}
$$

按算子范数绝对收敛，且给出一个保乘法、保幺的芽演算。

**证明。** 取 $g$ 的一个较小闭多圆盘 $|z_j|\le R_j$，其上解析且有界。Cauchy 系数界给某个 $C_g<\infty$，使

$$
|c_\nu|\le C_g\prod_{j=1}^mR_j^{-\nu_j}.
$$

选择任意 $0<\epsilon_j<R_j$。由 $T_j$ 拟幂零，存在有限 $C_j$，使对所有 $n\ge0$，

$$
\|T_j^n\|\le C_j\epsilon_j^n.
\tag{3.2}
$$

这包括有限多个小 $n$，只需相应增大 $C_j$。因此

$$
\begin{aligned}
\sum_\nu |c_\nu|
\|T_1^{\nu_1}\cdots T_m^{\nu_m}\|
&\le C_g\prod_{j=1}^m C_j
\sum_\nu\prod_{j=1}^m(\epsilon_j/R_j)^{\nu_j}\\
&=C_g\prod_{j=1}^m
\frac{C_j}{1-\epsilon_j/R_j}<\infty.
\end{aligned}
\tag{3.3}
$$

有限变量是这里的重要事实；各个 $C_j$ 可以很大，但其有限乘积仍有限。范数绝对收敛与变量交换性使 Cauchy 乘积、有限重组及芽乘法合法。证毕。

特别地，只要每个系数元拟幂零且彼此交换，就有本稿所需的全部联合求值估计，不需要额外假设 $\sum_j\|T_j\|$ 小，也不需要预先援引联合谱定理。

### 3.2 单位芽、常数项和拟幂零性

若 $u(0)\ne0$，则 $1/u$ 是一个收敛芽，故

$$
u(T)^{-1}=(1/u)(T)
\tag{3.4}
$$

存在于同一闭子代数中。

若 $g(0)=0$，则对每个 $\lambda\ne0$，$1/(g-\lambda)$ 是收敛芽。因此 $g(T)-\lambda I$ 可逆，即 $g(T)$ 没有非零谱点，所以拟幂零。

对任意连续角色 $\chi$，拟幂零性给 $\chi(T_j)=0$；例如由 (3.2) 取 $n$ 次方并开根即可。按绝对收敛级数求值，得到

$$
\chi(g(T))=g(0).
\tag{3.5}
$$

若 $T_j$ 属于 Jacobson 根基，所有无常数项有限多项式都属于该闭理想，故相应级数的范数极限也属于该根基。这给比仅在生成的交换子代数中拟幂零更强的根基结论。

## 4. 在完整 Banach 代数中分裂

把 §2 的根芽按引理 3.1 求值，定义

$$
\boxed{Y_\rho=y_\rho(B_2,\ldots,B_p).}
\tag{4.1}
$$

无论 $\|B_k\|$ 多大，这个级数都按范数绝对收敛，并位于这些 $B_k$ 生成的闭交换子代数中。

将 (2.5) 的有限个 $w$ 系数恒等式逐个应用保乘法的芽演算，即得到 (1.2)。这是 $\mathscr B[w]$ 中的准确多项式恒等式，不是某个小范数邻域内的近似。

又 $y_\rho(0)=\rho$，所以 §3.2 给

$$
Y_\rho-\rho I\text{ 拟幂零},\qquad
\chi(Y_\rho)=\rho.
$$

对 $\rho\ne\sigma$，芽 $y_\rho-y_\sigma$ 的常数项非零，由 (3.4)，

$$
(Y_\rho-Y_\sigma)^{-1}
=\left(\frac1{y_\rho-y_\sigma}\right)(B_2,\ldots,B_p)
\tag{4.2}
$$

也属于同一闭子代数。

### 4.1 根在指定根基分支上的唯一性

若 $Y$ 与全部 $B_k$ 交换，$Y-\rho I$ 拟幂零，且 $P(Y)=0$，则 $Y=Y_\rho$。

确实，$Y$ 与所有 $Y_\sigma$ 交换。两个交换拟幂零元之和仍拟幂零：对任意 $\epsilon>0$，分别取 (3.2) 的几何幂界，二项式展开给和的 $n$ 次幂界为 $C(2\epsilon)^n$，再令 $\epsilon\downarrow0$。因此当 $\sigma\ne\rho$ 时，

$$
Y-Y_\sigma=(\rho-\sigma)I+
\bigl[(Y-\rho I)-(Y_\sigma-\sigma I)\bigr]
$$

可逆。在 $P(Y)=\prod_\sigma(Y-Y_\sigma)=0$ 中取消这些可逆因子，得 $Y=Y_\rho$。

一般 Banach 代数中不能仅凭某一个角色的值 $\chi(Y)=\rho$ 就断言 $Y-\rho I$ 拟幂零；唯一性使用的是已明确写出的拟幂零或根基分支条件。在本题 $\mathcal A_h$ 的零字符部分已知属于根基时，这个条件自动满足。

## 5. 与闭第一 chaos 乘子的真实幂域接口

本节只核验代数代入和域，不承担各因子的核或循环性证明。

设 $X$ 是稠密定义的闭算子，每个 $B_k$ 有界、保持 $\operatorname{Dom}X$，且在该域上与 $X$ 交换。则每个 $Y_\rho$ 也具有相同的域交换性质。

证明可以直接使用根级数的有限部分 $Y_\rho^{(N)}$。对 $u\in\operatorname{Dom}X$，

$$
Y_\rho^{(N)}u\to Y_\rho u,
\qquad
XY_\rho^{(N)}u=Y_\rho^{(N)}Xu\to Y_\rho Xu.
$$

$X$ 闭，所以 $Y_\rho u\in\operatorname{Dom}X$ 且 $XY_\rho u=Y_\rho Xu$。归纳给所有幂域的保持与交换。

在自然复合定义域上，任意排列的有限乘积

$$
\prod_{\rho\in\mathcal R}(X-Y_\rho)
$$

恰好以 $\operatorname{Dom}X^p$ 为定义域，并在该域上等于

$$
\boxed{
\sum_{k=0}^p\frac{B_k}{k!}q^{(k)}(X).
}
\tag{5.1}
$$

域相等可按因子数归纳。前 $r$ 个因子的乘积在 $\operatorname{Dom}X^r$ 上为
$X^r+\sum_{j<r}C_jX^j$，所有 $C_j$ 都是保持 $\operatorname{Dom}X$ 的有界交换系数。对 $u\in\operatorname{Dom}X^r$，每个低阶项 $C_jX^ju$ 已在 $\operatorname{Dom}X$；因此这个和属于 $\operatorname{Dom}X$ 当且仅当 $X^ru$ 属于该域，也即 $u\in\operatorname{Dom}X^{r+1}$。这给自然复合域的两个包含。最后由 (1.2) 的系数恒等式得到 (5.1)。

本节没有声称 $X^p$ 或这个自然乘积自动闭；一般闭算子的幂不自动闭。根代理的点态多项式应用只需已由 R134 证明的
$1\in\operatorname{Dom}X^p$，所以 (5.1) 在 $1$ 上的代入完整合法。

具体地，若 R134 的修正系数满足

$$
u^r=\sum_{k=0}^r\binom rk B_kX^{r-k}1,
$$

则对标量多项式 $q$ 有

$$
\boxed{
q(u)=\left(\sum_{k=0}^p\frac{B_k}{k!}q^{(k)}(X)\right)1
=\left(\prod_{\rho\in\mathcal R}(X-Y_\rho)\right)1.
}
\tag{5.2}
$$

这些具体修正系数的拟幂零性也可直接核验。R134 的范数解析生成函数为

$$
B(t)=\lim_N\prod_{j<N}
e^{-ta_jV_j}\bigl(\cosh(ta_j)I+V_j\sinh(ta_j)\bigr).
$$

因为 $\chi(V_j)=1$，每个有限乘积的字符恒为1；范数极限及导数给
$\chi(B_0)=1$、$\chi(B_k)=0$（$k\ge1$）。这些 $B_k$ 属于 $\mathcal A$ 的零字符根基，彼此交换，故满足 §1 的假设。若 $\mathcal A_h$ 是包含它们的指定幺闭子代数，§3 的幂范数估计与级数范数收敛完全在该子代数内成立。

这里的每个 $B_k$ 和 $Y_\rho$ 都是真正有界算子；有限个闭因子的所有中间域由上段归纳保证。要从 (5.2) 得循环性，还应使用根代理对这些具体因子的核、正则化或循环性传递的已证结论，而不能仅凭标量 $q$ 有简单根就跳过该步骤。

## 6. 简单根假设的准确边界

简单根假设保证根随有限参数为收敛解析芽。若 $q$ 有重根，这个分裂一般不能留在原 Banach 代数中。

例如在本题 $\mathcal A$ 中取 $q(w)=w^2$、$B_2=A$，则

$$
P(w)=w^2I+A.
$$

若它在 $\mathcal A[w]$ 中分解成 $(wI-Y_1)(wI-Y_2)$，比较系数得
$Y_2=-Y_1$、$Y_1^2=-A$。字符给 $\chi(Y_1)=0$；R32 的忠实形式系数使任意非零 $Y_1$ 的平方具有偶数形式首阶，而 $A$ 的形式首阶为1，不可能。因此这里没有所需的两根分裂。

这个例子不否定某个具体重根点态多项式仍然循环，只说明本稿的解析分裂接口不能删去简单根条件。也不能通过“简单根多项式稠密”把循环性取极限到全部重根多项式。

本接口自含使用有限参数轮廓根、几何幂界和闭图定义域，没有使用外部文献或小算子范数假设。
