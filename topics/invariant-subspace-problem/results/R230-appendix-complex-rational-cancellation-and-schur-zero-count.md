# R230 附录：复有理块分母消去与收敛 Schur 逆源的零点约束

日期：2026-11-13。作者：Astra-ISP-0c / normal_next。完整证明分别见[分母消去稿](../notes/2026-11-13-complex-rational-block-denominator-cancellation-and-growing-order-obstruction-normal-next.md)及[Schur 零点稿](../notes/2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)。

## 固定态与已成功构造的实际接口

固定互不交物理块 $B_i$，$q_i=|B_i|=2^{4i}$，以及
$$
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
c_i=2^{-i-2},\quad c_i^2=\frac1{16\sqrt{q_i}},\quad
\lambda=\|f\|^2=\frac{49}{48}.
$$
$f$ 连续、正、$C$ 实，且是非湮灭者；以下证明是这一固定态对特定正则器族的障碍，不是一般正正常湮灭者的排除。

纯块 $T_i=2\sum_{j\in B_i}E_j/(q_i+2)$ 是严格收缩幂零算子。考虑
$$
U_i=N_i(T_i)D_i(T_i)^{-1},\qquad
D_i(z)=\prod_{\ell=1}^{r_i}(z+a_{i\ell}),\quad
0<|a_{i\ell}|\le3/4,
$$
$$
b_i=\prod_{\ell=1}^{r_i}(1+|a_{i\ell}|),\qquad
\|N_i\|_{\mathrm{coef},1}\le Cb_i
$$
的一致分子预算。假设构造已确实付清：$U_i$ 扩张；准确实际源列为 $\widetilde g_i=g_i/(1-\varepsilon_i)$、$g_i=U_i\Omega$；实际 carry 满足
$$
16q_i5^{q_i}\max(1,\|g_i\|)\eta_{\min B_i}\le\varepsilon_i<1/2;
$$
源块乘积 $g$ 在原 $H$ 收敛；非零 $P$ 满足 $Pg=1$，并有 R244 同组有界强单位。于是
$$
G=P^{-1}=X_g,\qquad Gu=X_ug
$$
在全部有限 Walsh 柱上准确成立。这些前提不由有理表达式自动提供。

## 定理一：固定或缓增分母的真实全列障碍

若 $r_i\le r_*$，R244 聚合界在次数至多 $r_*+2$ 的有限列上失败。若 $r_i=o(\sqrt{q_i})$，仍存在各自有限次数的实际列 $u_i$，使
$$
\|u_i\|\le1,\qquad \sup_i\|Gu_i\|<\infty,\qquad
|\phi_f(X_{u_i})|\to\infty.
$$
最终 $r_i\le\sqrt{q_i}/8$ 也足够。允许复参数和单位相位。

**证明要点与明确预算。** 对纯次数 $k$ 的单位对称 Walsh 列
$$
v_{q,k}=\binom qk^{-1/2}\sum_{|F|=k}\chi_F
$$
取真正有限列
$$
u_i=b_i^{-1}D_i(T_i)v_{q_i,k_i},\qquad
\deg u_i\le r_i+k_i.
$$
准确分母消去给 $\|U_iu_i\|\le C$。令 $D_F^0=\prod_{j\in F}(I-2E_j)$、$\chi=\chi_B$，定义
$$
\ell_{q,k}(p)=2^{-k}\langle p(T)D_F^0\chi,\chi\rangle.
$$
它不被视作正泛函。逐位计算给
$$
\ell_{q,k}(e^{t(T+I)})
=e^t(1-t/(q+2))^{q-k}(1-t/(2q+4))^k.
$$
在 $4r\le(q+2)/2$ 时，对数级数的系数绝对主控推得
$$
\left|\frac{\ell_{q,k}(D(T))}{D(-1)}-1\right|
\le\exp\!\left(\frac{16r^2+2rk+8r}{q}\right)-1=:E(q,r,k).
$$
又 $|D(-1)|/b\ge7^{-r}$。选相位 $\tau_i$ 令 $\tau_iD_i(-1)>0$，若 $E_i\le1/2$，准确完整块矩和真空余项给
$$
\operatorname{Re}\phi_f(X_{\tau_i u_i}^0)
\ge\frac12 A_i-\lambda,\qquad
A_i=c_i^2\,2^{k_i}\sqrt{\binom{q_i}{k_i}}\,7^{-r_i}.
$$
这里保留 $-\lambda$；没有将整个正常态矩误认为单个正块矩。

令 $s_i=r_i+k_i$。真实有限列乘子和纯乘子的误差为
$$
\Delta_i\le
8s_i3^{s_i}\sqrt{s_i+1}\,q_i^{s_i/2}\eta_{\min B_i}.
$$
当 $s_i=O(\sqrt{q_i})$，前因子对数为 $o(q_i)$，所以已付的 $q_i5^{q_i}\eta$ 预算使 $\Delta_i\to0$。若 $M=\|g\|$，准确源分块与最小逆图给
$$
\|G(\tau_i u_i)\|\le CM+M\Delta_i,
$$
而实际矩误差至多 $\lambda\Delta_i$。

固定 $r_*$ 时取 $k_i=2$，则 $A_i\ge\frac14\sqrt{(q_i-1)/2}\,7^{-r_*}\to\infty$。缓增情形取 $k_i=r_i+2$；误差指数成为 $(18r_i^2+12r_i)/q_i$，而对 $r_i\ge1$，
$$
A_i\ge\frac14\left(\frac{2q_i^{1/4}}7\right)^{r_i}
\ge\frac{q_i^{1/4}}{14}\to\infty.
$$
$r_i=0$ 的子序列另用 $k_i=2$。以上均为同一个实际 $G$ 的合法有限列，故全列聚合失败。

## 定理二：收敛逆源自动约束紧内 Schur 零点数

设 $q_i\to\infty$，$b_i$ 在闭单位圆盘邻域解析且 $|b_i|\le1$，$b_i(T_{q_i})$ 可逆收缩。若准确缩放逆源块乘积
$$
\prod_i\frac{b_i(T_{q_i})^{-1}\Omega}{1-\varepsilon_i}
$$
在原 $H$ 收敛，则 $b_i$ 在 $|z|\le3/4$ 内按重数计的零点数满足
$$
\boxed{r_i=o(\sqrt{q_i}).}
$$
任意固定紧子圆盘同理，只改变常数。

**证明。** 真空矩为
$$
c_{q,n}=\langle T_q^n\Omega,\Omega\rangle
=\frac{(q)_n}{(q+2)^n}\quad(n\le q),\qquad c_{q,n}=0\quad(n>q).
$$
严格收缩的 Cayley 正性给概率密度
$$
w_q(\theta)=1+2\sum_{n=1}^qc_{q,n}\cos(n\theta)\ge0,\quad
\langle b(T_q)\Omega,\Omega\rangle
=\int b(e^{i\theta})\frac{w_q(\theta)}{2\pi}\,d\theta.
$$
在每个固定有界 $x$ 区间，
$$
q^{-1/2}w_q(x/\sqrt q)\to\sqrt{2\pi}e^{-x^2/2}
$$
一致收敛。其证明由 $n=O(\sqrt q)$ 的一致对数展开及全局 $c_{q,n}\le e^{-n^2/(3q)}$ 给出，故同时得到窗口中的正密度下界。

准确源乘积收敛、每个逆块扩张，迫 $\widetilde g_i\to\Omega$、$\varepsilon_i\to0$、$g_i\to\Omega$。收缩性遂给 $b_i(T_{q_i})\Omega\to\Omega$，其真空矩趋于 $1$。正密度下界使
$$
\int_{-M}^M|1-b_i(e^{ix/\sqrt{q_i}})|^2dx\to0
$$
对每个固定 $M$ 成立。以 $h_i=q_i^{-1/2}$，Poisson 核估计
$$
P_{1-h_i}(\theta)\le\frac{\pi^2h_i}{h_i^2+\theta^2}
$$
支付整个外尾；先取 $i\to\infty$ 再取 $M\to\infty$，得 $b_i(1-h_i)\to1$。

除去紧内零点的有限 Blaschke 因子后，剩余函数仍为 Schur。每个 $|\alpha|\le3/4$ 给
$$
1-\left|\frac{1-h_i-\alpha}{1-\overline\alpha(1-h_i)}\right|^2
\ge h_i/7.
$$
故 $|b_i(1-h_i)|\le e^{-r_i h_i/14}$。左端趋于 $1$，证明结论。

## 合并结论及量词

在上述固定分块、固定 $f$ 下，前向块为任意增长阶、任意复参数的有限 Blaschke 产品，所有零点留在 $|z|\le3/4$，若实际逆源构造成功，则定理二自动给定理一所需的分母小阶条件。因此单靠增加紧内 Blaschke 因子数量，不能获得这个 $\phi_f$ 的全列聚合表示。

有限个同分块完整逆源的线性组合仍可用共同分母和图范数三角界；每个分支小阶保证总阶仍小阶。块内有限线性组合只有在另行验证扩张、源收敛、强单位和一致分子预算后才适用；其倒数不自动是 Schur 函数。一般分支分子常数为 $C_\nu$、组合系数绝对和上界 $B$ 时，统一常数应取 $B\max_\nu C_\nu$。

本定理没有处理零点向单位圆逼近的全部复参数族、不同分块、没有真空原像的前向正则器、一般专属正常湮灭矩或 $P\in S\{A\}'$。也不把逆源线性组合误认为正则器线性组合的逆。普通 ISP 和一般正常湮灭者仍开放。
