# R1127：原 Gaussian 的 irregular 补角色与一次尖点标签

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明，纯纸面。** 设 $p=4k+3\ge41$。若
$p\mid\operatorname{num}(B_{p-3})$，完整原尖点模块中准确出现
$\chi=\omega^2$，而这个角色自身始终 Bernoulli-good。
在原 Gaussian supersingular component 上，它的完整标签是
coarse 参数的一次多项式，斜率为明确单位。
因此这个分支不需要 R1116 的未知 $\mathcal H_p$。

本篇只证明原 coarse $\mathbf F_p$ 分量上各圆盘标签的注入；
不把圆盘内恒定的 Kummer 标签称为整个 $p$-adic 盘内点的单射。
没有新的数学执行，也没有删除 R1116 的 forced-good mask。

## 1. 原对象和出现判据

仍用 R1062 的完整原曲线 $X_{\rm ns}^+(p)$ 及
$$
V=U_p/pU\simeq C_\Sigma[p],\qquad
m=(p-1)/2,\quad \chi=\omega^2,\quad\psi=\chi^{-1}=\omega^{-2}.
\tag{1127.1}
$$
这里 $\omega$ 是 R1062 的同一个 Teichmüller 字符；Galois 作用没有反转。
对非平凡偶角色，原实际 Stickelberger 格给
$$
(C_\Sigma\otimes\mathbf Z_p)_\chi
 \simeq\mathbf Z_p/(S_\psi),\qquad
S_\psi=-\frac14J(\psi,\eta)B_{2,\psi^2},\qquad \eta=\omega^m.
\tag{1127.2}
$$
$\psi,\eta,\psi\eta,\psi^2$ 在本范围全部非平凡，
故这是 R1062 的真实 Jacobi/Bernoulli 因式，没有异常项。

直接模 $p$ 展开：
$$
J(\psi,\eta)\equiv
\sum_{z\in\mathbf F_p}z^{p-3}(1-z)^m
=-\binom m2\ne0\pmod p.
\tag{1127.3}
$$
唯一指数为 $p-1$ 的项来自二次项；
最高指数 $p-3+m<2(p-1)$，没有另一个贡献。
$m,m-1,2$ 均为单位。

广义 Bernoulli 的准确规范是
$$
\frac{B_{2,\omega^{-4}}}{2}
 \equiv\frac{B_{p-3}}{p-3}\pmod p,\qquad
B_{2,\omega^{-4}}\equiv-\frac23B_{p-3}\pmod p.
\tag{1127.4}
$$
于是
$$
\boxed{\quad
 V_{\omega^2}\ne0
 \quad\Longleftrightarrow\quad p\mid\operatorname{num}(B_{p-3}).
 \quad}
\tag{1127.5}
$$
出现时该分量准确一维，原函数基由 R1070 §10.2 支付。
这里只比较是否被 $p$ 整除；不由模 $p$ Kummer 同余声称两个数的
更高精确 $p$-valuation 相等。

### 1.1 对 (1127.4) 的有限规范核对

为避免把 Bernoulli 下标错移为 $p-5$，可不用一般广义版本，
直接从普通 Kummer 同余核对这一特例。
对 $1\le a\le p-1$，令
$q_p(a)=(a^{p-1}-1)/p$，只把它用于纸面同余。
Teichmüller lift 满足
$$
\omega(a)\equiv a^p=a(1+pq_p(a))\pmod{p^2}.
$$
因为 $\omega^{-4}=\omega^{p-5}$，
$$
a^2\omega(a)^{-4}
 \equiv a^{p-3}(1-5p q_p(a))\pmod{p^2}.
$$
置 $S_n=\sum_{a=1}^{p-1}a^n$，得到
$$
\sum a^2\omega(a)^{-4}\equiv6S_{p-3}-5S_{2p-4}\pmod{p^2}.
$$
这个非平凡偶字符的 $\sum\chi(a)$ 与 $\sum a\chi(a)$ 都为零，
故原定义给
$B_{2,\omega^{-4}}=p^{-1}\sum a^2\omega(a)^{-4}$。
Faulhaber 公式在这两个偶指标上给
$S_n\equiv pB_n\pmod{p^2}$；
高项中可能的 Bernoulli 分母至多含一次 $p$，仍不影响此精度。
普通 Kummer 同余又给
$$
B_{2p-4}\equiv\frac{2p-4}{p-3}B_{p-3}
 \equiv\frac43B_{p-3}\pmod p.
$$
所以 $6B_{p-3}-5B_{2p-4}\equiv-2B_{p-3}/3\pmod p$，正是 (1127.4)。
所有所用分母在 $p\ge41$ 下均为单位。

## 2. 这个实际角色自身恒 good

$\chi=\omega^2$ 的 circular-unit 读取使用 $B_2=1/6$，
不是触发其出现的 $B_{p-3}$。
取 R1071 同一原奇整数 $a_{\rm cyc}$，其类生成
$\mathbf F_p^\times/\{\pm1\}$，并保真实 Weil 相位
$$
\gamma=\overline{(\zeta_p-1)/\varpi^{p+1}}.
$$
则原系数
$$
b_\chi=
 \frac{B_2(a_{\rm cyc}^2-1)}{2\cdot2!}\gamma^2
 =\frac{a_{\rm cyc}^2-1}{24}\gamma^2
 \in\mathbf F_p^\times.
\tag{1127.6}
$$
故 R1069 的唯一全局 good 坐标确实适用。
没有在不 good 的原 $\omega^{p-3}$ 角色上除零；
使用的是由 (1127.5) 证明实际出现的另一个角色。

取 R1070 同一 primitive smoothing 整数 $c$，则
$$
\kappa_\chi=c^2-\chi(c^2)=c^2-c^4\ne0.
\tag{1127.7}
$$
它与原函数基、Weil root 和标签规范同时保留。

## 3. 原 Gaussian 完整 profile 的精确斜率

固定 R1071/R1116 的真实 Gaussian reference
$$
E_a:y^2=x^3+ax,\qquad a\in\mathbf F_p^\times,\qquad
\omega_E=dx/(2y).
$$
保原 $\beta_0,\lambda$ 和 fine 参数 $t_*$；
不将它们另行归一为一。
本角色的 $R=2$，所以原总阶 $N=(p+1)R=2p+2$。
R1071 §§4–5、15 的全部高 log 分母和 Lucas 边界已经支付
$$
\deg_{t_*}\mathcal P_{\chi,s}\le2.
$$
Gaussian 的实际 $\mu_4$ 下降只允许偶次，
故整个多项式只有常数和二次项。
在原 coarse 参数
$$
z=t_*^2
$$
上，它准确为 affine，不是只取第一 jet 的近似。

二次项的原指数和二项式为
$$
d_2=N-2(p-1)=4,\qquad
\binom{d_2-1}{2-1}/2=3/2.
$$
R1071 原 division-polynomial identity 在同一 eigenparameter 上给
$$
A_4=\frac{(c^4-c^2)a}{15}=\kappa_\chi G_4,\qquad
G_4=-a/15.
\tag{1127.8}
$$
这些都是实际低阶有限系数，没有新的共振或高尾。

将 (1127.8) 代入完整 (1071.20)，再乘原
$m/(\kappa_\chi b_\chi)$，并用 $p+1\equiv1$、$m\equiv-1/2$，得到
$$
\boxed{\quad
 c_{\chi,s}(z)-c_{\chi,s}(0)
 =-\frac{a\,\beta_0^4\lambda^2}{20b_\chi}\,z.
 \quad}
\tag{1127.9}
$$
右侧全部外因子为单位。regularizer $\kappa_\chi$ 准确相消，
$\beta_0,\lambda$ 和 $b_\chi$ 内的原 Weil 相位没有丢失。

这条公式在原 coarse 分量上下降成立；
不要求每个 $\mathbf F_p$ coarse 值都有某个预先选定的
$\mathbf F_p$ fine 平方根，也不合并未经识别的不同 twists。
对每个保持其原标架的实际 Gaussian coarse component，
(1127.9) 都给相应的 affine unit 标签。

## 4. 严格完成的门与仍开放的门

在假设 $p\mid B_{p-3}$ 下，
$\chi=\omega^2$ 是完整原 $V$ 的一个真实 good 分量。
式 (1127.9) 因而证明：

- 该 Gaussian coarse $\mathbf F_p$ 线上两个不同原参数值，
  给不同的完整原尖点标签；
- 任一固定全局候选在此分量内至多对应一个原
  $\mathbf Q_p$ 剩余圆盘；
- 若该候选等于规范 CM 中心的标签，则只能对应该中心的原圆盘。

这些结论没有要求其它实际角色 good。
它们不证明该剩余圆盘内只有一个有理点，也不完成一般 $p$ 的全局辅助筛选。

由此，一般 Gaussian 标签注入的后继可以把本支移出未知范围，
继续处理
$$
p\nmid B_{p-3}.
$$
在这个剩余分支中，第一 forced 角色 $\omega^{p-3}$ 本身 good，
但其原斜率仍由 R1082/R1116 的未知 $\mathcal H_p$ 读取；
本篇没有证明 $\mathcal H_p$ 单位。
也没有改变其它 forced 角色的 good mask。

原 bare $r=2,8$、primitive/Legendre 条件、
$f_N/e$、短 $\eta_k,\nu_k$ 以及 R1114 的邻位混合系数
都没有被 (1127.9) 代换。
新增结论是**原完整 cuspidal 标签的一个实际 affine 补支**，
不是这些高系数的单位定理。

## 5. 来源与独立核对

- R1062 §§1–3：完整原 cusp 格、真实 Galois 方向、
  $S_\psi=-J B_{2,\psi^2}/4$ 与每角色至多一维。
- R1070 §10：完整实际 $V$ 的原函数基及 smoothing 规范。
- R1069：Bernoulli-good 角色的原全局定位同构。
- R1071 §§4–6、11、15：完整 $R=2$ profile、高分母边界、
  真实 circular-unit/Weil 尺度及 $A_4$。
- 普通 Kummer 同余可见
  [NIST DLMF 24.10.3](https://dlmf.nist.gov/24.10.E3)；
  同一广义规范的完整证明另见 Kartik Prasanna
  [Lecture 8, Theorem 8.3](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/L8.pdf)。
  上文 §1.1 已把所需特例还原为普通 Kummer 和两个有限幂和。

root/global_route 已独立纸核 (1127.2)–(1127.9) 的角色、出现判据、
原 $3/2$ 因子、斜率及 coarse 范围。
全部为纸面证明，没有数学程序执行。
