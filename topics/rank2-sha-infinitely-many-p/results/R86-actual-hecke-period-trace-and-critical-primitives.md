# R86：实际 Hecke 关系、完整周期迹与临界原函数

日期：2026-11-12。状态：标签、权重、晶体运输及原函数结论已根端独审。
完整证明见[真实 Hecke–同源–GM 迹](../notes/2026-11-12-actual-hecke-isogeny-gm-trace.md)。

## 1. 原级结构和微分权重全部运输

在 $\Lambda_\tau=\mathbb Z+\tau\mathbb Z$、标签 $(a+b\tau)/N$ 的规范中，
$N=68$。有限分支 $\tau_j=(\tau+Nj)/p$ 运输标签为 $(a,pb)$，
无穷分支 $p\tau$ 运输为 $(pa,b)$。R82 的惰性 Hecke 零关系准确成为

$$
\sum_{j=0}^{p-1}G_{\operatorname{diag}(1,p)\mathcal S}(\tau_j)
+pG_{\operatorname{diag}(p,1)\mathcal S}(p\tau)=0.
$$

转到代数 Legendre 微分时，权重分别为
$d_j=\omega_1(\tau_j)/\omega_1(\tau)$、
$d_\infty=p\omega_1(p\tau)/\omega_1(\tau)$。
它们是实际代数微分拉回比，不需把复周期嵌入 $p$ 进域。
惰性标记交换实际半线：
$M_e^{\rm tr}=(c_e/c_o^\sigma)M_o^\sigma$、
$M_o^{\rm tr}=(c_o/c_e^\sigma)M_e^\sigma$。
结合两条 Hecke 关系和有理 Taylor 系数后，得到

$$
\sum_jd_jM_e(t_j)=0,\qquad\sum_jd_jM_o(t_j)=0.
$$

## 2. 迹是在临界分支上取值

令 $\xi=(b/(pa))u(t)$。实际邻点满足
$\xi=K(t_j)/L(t_j)$、$dt_j/d\xi=-s(t_j)L(t_j)^2$。
因此对全部 $p+1$ 个分支，

$$
\sum_jK(t_j)M_e(t_j)=0,\qquad
\sum_jK(t_j)M_o(t_j)=0.
$$

这里的目标 $u(t_j)=1/\xi$ 在无穷附近；
不是原点同一个 $u$ 级数的 $p+1$ 份副本。
复 Cayley 展开亦保留完整尺度：第 $m$ 阶 Maass 导数的无穷分支
权重为 $p^{2m+1}$，有限分支为一。
所涉及的是导子 $p$ 的 CM 邻点值，不能直接替换成原 $C_m$。

## 3. 一个完整原函数迹为零，另一个需要真实对数正规化

记

$$
I(t)=H_i(u(t))=\int_0^t\frac{M_eK}{sL^2}\,dt.
$$

$J=L/t$ 的最近零点半径为 $p^{-1/(p^2+p)}>\rho$，
所以 $I$ 在所有 $K$ 零点均有规范解析值。
由 $dI(t_j)/d\xi=-K(t_j)M_e(t_j)$，其完整迹为常数；
$I$ 为奇函数，$\xi=0$ 的根成正负对，故准确有

$$
\sum_jI(t_j(\xi))=0.
$$

这与已知 $p=7$ 的中央非零证书并存，不能据此认定中央导数为零。
另一原函数 $E'=M_e/(sK)$ 在每个 $K$ 根 $r$ 有真实留数

$$
\operatorname{res}_r(E',dt)=-L(r)M_e(r)\ne0,
\qquad v_p\operatorname{res}=5/(p+1).
$$

$H_o'=E/(sKL)$ 的最高局部项为
$\tfrac12L(r)M_e(r)\log(t-r)^2$。
因此 $E,H_o$ 的邻点值必须保留一致的对数或 Coleman 正规化；
不能当作在零点解析的原函数直接取迹。
下一问题是实际带权迹或完整对数比较如何约束中央行。
