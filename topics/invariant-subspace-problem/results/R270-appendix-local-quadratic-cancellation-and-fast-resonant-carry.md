# R270 第二附录：局部二阶消去的快类与精确共振的真实进位项

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。
状态：以下结构结论完整证明；尚不由此断言精确共振核为零。

本稿给 R270 第一附录的二次共振值一个真实有界结构：其剩余进位项属于 R151 的快解析逼近代数 $\mathcal G$。更一般地，任何在每个位具有统一解析系数界、且常数项和一次项都消去的局部级数，其全部实际位之和属于 $\mathcal G$。证明直接使用真实归一化幂的重复占据估计；不把 $\mathcal G$ 当作整个 $\mathcal A$ 的理想，也不作未付清的有界除 $A$。

## 1. 真实重复占据预算

写
$$
W_n=\|A^n\|,\qquad d_j=W_{2^j},\qquad
N_j=A^{2^j}/d_j.
$$
[R140 §5](../results/R140-invariant-subquotient-type-and-fixed-first-regularization.md)重述了 R110 的实际估计：
$$
\left\|\left(\frac{A^n}{W_n}\right)^k\right\|
=\frac{W_{kn}}{W_n^k}
\le \exp\left[-\frac14n^4(k-1)^4\right],
\qquad n,k\ge1.
\tag{1.1}
$$
对 $n=2^j$ 和 $k\ge2$，置 $r=k2^j$。因 $k-1\ge k/2$，
$$
\boxed{
\frac{W_{k2^j}}{d_j^k}
\le e^{-r^4/64}.
}
\tag{1.2}
$$
这里使用原实际权与原算子幂，并未将 $N_j$ 换为平方零纯位。

## 2. 统一局部二阶消去引理

**定理。** 设对每个 $j\ge0$ 给出标量解析芽
$$
f_j(z)=\sum_{k\ge2}c_{jk}z^k,
$$
且存在固定 $C,R>0$ 使
$$
|c_{jk}|\le C R^{-k}\qquad(j\ge0,\ k\ge2).
\tag{2.1}
$$
则双和按原算子范数绝对收敛，
$$
E=\sum_{j\ge0}f_j(N_j)
=\sum_{r\ge2}\beta_r\frac{A^r}{W_r},
\tag{2.2}
$$
其中
$$
\beta_r=
\sum_{\substack{j\ge0:\ 2^j\mid r\\ k=r/2^j\ge2}}
c_{jk}\frac{W_r}{d_j^k}.
\tag{2.3}
$$
并且 $E\in\mathcal G$。

证明：令 $D=\log^+(R^{-1})$。每个 $r$ 至多有
$1+\lfloor\log_2r\rfloor$ 个表示 $r=k2^j$、$k\ge2$。又 $k\le r$，故
$$
\sum_{\substack{j,k:\ k2^j=r\\ k\ge2}}
|c_{jk}|\frac{W_r}{d_j^k}
\le C(1+\lfloor\log_2r\rfloor)e^{Dr-r^4/64}.
\tag{2.4}
$$
右边对 $r\ge2$ 可和。这同时证明双和的绝对范数收敛、各局部解析求值的合法性、合并同幂与换序的合法性。

存在固定 $K<\infty$，使
$$
|\beta_r|\le K e^{-r^4/128}\qquad(r\ge1),
\tag{2.5}
$$
其中 $\beta_1=0$。把非零 $|\beta_r|$ 按降序写为 $\beta_\ell^*$。因为只有 $\ell-1$ 个正整数小于 $\ell$，(2.5) 的递减包络给
$$
\beta_\ell^*\le K e^{-\ell^4/128}.
$$
故无限支持时
$$
\lim_{\ell\to\infty}\frac{-\log\beta_\ell^*}{\ell^3}=+\infty.
\tag{2.6}
$$
有限支持时是有限多项式。由 [R151 §6.1](../results/R151-quartic-analytic-approximation-gauge-stability.md)的超三次归一化幂级数准则，两种情况均有 $E\in\mathcal G$。证毕。

注意，(2.1) 不要求不同位的系数随 $j$ 可和；局部至少重复占据两次已经支付全部 $j$ 方向的范数和。

由 R151，若 $E\ne0$ 且实际形式首阶为 $h$，则每个非零不变 Hilbert 子商 $Q$ 上
$$
E_Q\ne0,\qquad
\tau_4(E_Q)=\frac{100}{15}h^4.
\tag{2.7}
$$
它在全部不变限制与有限放大中单射且像稠密。这是对已证明 $\mathcal G$ 成员的应用，不是任意范数闭包元素的性质。

## 3. 任意固定局部多项式的线性部分与快余项

令 $(t_j)$ 为有界复数列，记
$$
R_j=V(t_jN_j)=(I-t_jN_j)(I+t_jN_j)^{-1}.
$$
每个逆存在，因为 $N_j$ 拟幂零。设 $H$ 为固定标量多项式，$H(1)=0$；令 $(b_j)$ 为任意有界标量列。

标量函数
$$
f_j(z)=b_j\big[
H(V(t_jz))-H'(1)(V(t_jz)-1)
\big]
\tag{3.1}
$$
在零点的常数项和一次项都为零。取固定小半径
$r_0<1/(2\max(1,\sup_j|t_j|))$，所有 (3.1) 在 $|z|\le r_0$ 统一有界。Cauchy 系数界于是满足 (2.1)。因此
$$
\boxed{
\sum_j b_j\big[
H(R_j)-H'(1)(R_j-I)
\big]\in\mathcal G,
}
\tag{3.2}
$$
且和按实际算子范数绝对收敛。

若另有 $b\in\ell^1$，两部分本身都按范数收敛，可以写成真实分解
$$
\sum_jb_jH(R_j)
=H'(1)\sum_jb_j(R_j-I)+E,\qquad E\in\mathcal G.
\tag{3.3}
$$
未假设线性慢和也属于 $\mathcal G$。R160 已给自然慢二阶 Bell 项不属于 $\mathcal G$ 的实例，与 (3.3) 完全相容。

对 Bell 累积量
$$
L_n(v)=
\left.\frac{d^n}{dx^n}\log(\cosh x+v\sinh x)\right|_{x=0},
\qquad n\ge2,
$$
有 $L_n(1)=0$，且
$$
L_n'(1)=
\left.\frac{d^n}{dx^n}\frac{1-e^{-2x}}2\right|_{x=0}
=-\frac{(-2)^n}{2}.
\tag{3.4}
$$
故任意有限组 $\ell^2$ first 行的混合累积量
$$
K_\nu=\sum_j b_{\nu j}L_{|\nu|}(R_j),\qquad
b_{\nu j}=\prod_\ell a_{\ell j}^{\nu_\ell},\quad |\nu|\ge2,
$$
准确分解为
$$
\boxed{
K_\nu=-\frac{(-2)^{|\nu|}}2
\sum_jb_{\nu j}(R_j-I)+E_\nu,\qquad E_\nu\in\mathcal G.
}
\tag{3.5}
$$
乘积系数 $b_\nu\in\ell^1$：任取其中两个 $\ell^2$ 因子用 Cauchy--Schwarz，其余有限因子用上确界。因此这里两个范数和分别有定义。

(3.5) 是逐个系数的准确分解。它不允许把快余项乘任意慢系数后仍无证称为 $\mathcal G$。

## 4. 二次精确共振的真实算子

取任意非常数 first
$$
u=a_*+\sum_ja_j\chi_j,\qquad
a\in\ell^2,\quad a\ne0,
$$
以及任意 first 指数权
$$
w=b_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$
置 $t_j=e^{-2b_j}$、$R_j=V(t_jN_j)$，并令 $X=X_b$ 为对应主行的真实倾斜闭 first。

R270 第一附录的共振辅助为
$$
v_2=2\sum_ja_j^2(\chi_j-1).
$$
该级数绝对收敛，中心为零。真实辅助算子为
$$
Y=2\sum_ja_j^2(R_j-I).
$$
混合 Bell 恒等式、$L_2(v)=1-v^2$ 给
$$
\begin{aligned}
T&=X^2+\sum_ja_j^2(1-R_j^2)+Y\\
&=X^2-B,
\end{aligned}
\qquad
B=\sum_ja_j^2(R_j-I)^2.
\tag{4.1}
$$
因而在完整自然域 $\operatorname{Dom}X^2$ 上，
$$
\boxed{
Te^w=(u^2+v_2)e^w,\qquad
B=4\sum_ja_j^2t_j^2
N_j^2(I+t_jN_j)^{-2}\in\mathcal G.
}
\tag{4.2}
$$
$T$ 的闭性、完整 $C$ 自伴性和图核心来自 R176；$B$ 的快类归属来自 §2 或 §3 的二阶消去。

为了给出直接可复核的归一化系数，展开
$$
B=4\sum_j\sum_{k\ge2}
a_j^2(-1)^k(k-1)t_j^k\,\frac{A^{k2^j}}{d_j^k}.
\tag{4.3}
$$
设 $T_0=\max(1,\sup_j|t_j|)$。由 (1.2)、$k-1\le r-1$ 和 $\sum_j|a_j|^2<\infty$，合并系数满足
$$
\boxed{
|\beta_r|
\le4(r-1)\|a\|_2^2
\exp\big[r\log T_0-r^4/64\big].
}
\tag{4.4}
$$
所有换序由这个可和的绝对范数主控支付。

若 $j_0=\min\{j:a_j\ne0\}$，则最低幂
$$
h=2^{j_0+1}
$$
只能来自 $j=j_0,k=2$，其形式系数为
$$
4a_{j_0}^2t_{j_0}^2/d_{j_0}^2\ne0.
$$
所以 $B$ 实际非零，首阶准确为 $h$。R151 遂给
$$
\boxed{
\tau_4(B_Q)=\frac{100}{15}2^{4(j_0+1)}
}
\tag{4.5}
$$
对每个非零不变子商以及有限放大中的非零不变子商成立。

这些证明不需要 R268 的熵条件；它们对任意上述 $\ell^2$ 主行与 first 权成立。

## 5. 共振核内已经得到的性质与剩余步骤

若 $M=\ker(X^2-B)$，R176 给 $M\subset\mathcal D_\infty$、$X_M\in B(M)$，且
$$
X_M^2=B_M.
\tag{5.1}
$$
由 $B\ne0$、$B\in\mathcal G$，若 $M\ne0$，则 $B_M$ 单射且像稠密。因此 $X_M$ 也单射且像稠密：其核包含于 $B_M$ 的核，而其像包含 $B_M$ 的像。

这仍不是 $M=0$。本文没有把 $\mathcal G$ 系数的有界慢变量定理无证外推到整个无界 $X$，也没有从 (5.1) 推出 $X_M$ 有有界逆。要关闭共振，仍须在完整自然域上支付快系数多项式的 gauge 消元，或另给真实核排除机制。

本文也未将 (4.2) 改写为未经证明的 $B=A^2C$、$C$ 有界；快归一化系数与指定有界除法是不同要求。普通 ISP 与实际边界缺陷仍开放。
