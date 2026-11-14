# R230 附录：负实逼圆的粗逆源、准确 Gram 与大次数列

日期：2026-11-13。作者：Astra-ISP-0c017065 / normal_complex。
状态：主会话全文核验通过；普通 Hilbert ISP 未完成。
[完整证明](../notes/2026-11-13-signed-real-and-complex-sector-blaschke-large-column-obstruction-normal-complex.md)给全部纯块公式、实际提升及有限源组合。

## 1. 前提和固定正常态

纯块仍为
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\quad
E=|1\rangle\langle0|,\quad
\Omega=\Omega_+^{\otimes q},\quad D_j=I-2E_j.
$$
第 $i$ 块的前向 $R_i$ 是带整体单位相位的有限 Blaschke 积
$\prod\beta_a(T_{q_i})$，$a\ne0$、$|a|<1$；
$U_i=R_i^{-1}$、$g_i=U_i\Omega$、$n_i=\|g_i\|\ge1$。
保持准确实际构造前提
$$
\widetilde U_i=X_{g_i}/(1-\varepsilon_i),\qquad
g^{(n)}=\prod_{i\le n}g_i/(1-\varepsilon_i)\to g,
$$
$$
16q_i5^{q_i}\max(1,n_i)\eta_{\min B_i}\le\varepsilon_i<1/2.
\tag{1.1}
$$
使用聚合逆图时还要求 $P$、$Pg=1$ 及同一组有界强单位已实际构造；
此时 R244 给 $G=P^{-1}=X_g$ 和有限柱图核心。

固定同一分块及
$$
q_i=16^i,\qquad f=1+\sum_i2^{-i-2}\chi_{B_i},\qquad
\lambda=\|f\|^2=49/48.
\tag{1.2}
$$
这是已知非湮灭的连续非负 $C$ 实向量。本稿限制这些正则器对其正常态的聚合配对，未排除一般真正正正常见证。

## 2. 收敛逆源可以不在加权空间

负实参数 $a=-b$、$0<b<1$ 去掉整体相位 $-1$ 后，
$$
P_b(T)=\frac{I-bT}{bI-T}
=b^{-1}I+(1-b^2)\sum_{n=1}^q b^{-n-1}T^n.
\tag{2.1}
$$
系数非负。对 $W_r=r^{\mathsf N}$，所有次数的准确 Gram 核为
$$
\boxed{
\langle W_re^{sT_q}\Omega,W_re^{tT_q}\Omega\rangle
=\left(1+\frac{s+\bar t}{Q}
+\frac{(1+r^2)s\bar t}{Q^2}\right)^q,\quad Q=q+2.
}
\tag{2.2}
$$
因此
$$
\langle W_rT_q^m\Omega,W_rT_q^n\Omega\rangle
=\frac{m!n!}{Q^{m+n}}
\sum_{\ell=\max(0,m+n-q)}^{\min(m,n)}
\frac{q!(1+r^2)^\ell}
{(q-m-n+\ell)!(m-\ell)!(n-\ell)!\ell!}.
\tag{2.3}
$$
全部条目非负，包含非对角项。

令 $\delta_i=e^{-q_i/100}$、$b_i=1-\delta_i$，略去有限初块。
有限 Neumann 和给
$$
\|P_{b_i}(T_i)-I\|\le4e\,q_i\delta_i,
$$
所以纯逆算子积在范数中收敛到有界可逆算子。
但用 (2.3) 的非负 Gram 系数和 $s=q/2$，得到
$$
\boxed{
\|P_{b_i}(T_i)\Omega\|_{\sqrt3}
\ge e^{-1}\exp\left[
\left(\frac{\log3-1}{2}-\frac1{100}\right)q_i
\right]\to\infty.
}
\tag{2.4}
$$
括号严格为正。

同一分块的 (1.1) 蕴含
$\sum_iq_i5^{q_i}\eta_{\min B_i}<\infty$。
对充分大块取
$\varepsilon_i=32q_i5^{q_i}\eta_{\min B_i}$，
实际提升满足
$$
\|X_{g_i}-P_{b_i}(T_i)\|
\le8q_i(3\sqrt2)^{q_i}n_i\eta_{\min B_i}\le\varepsilon_i,
$$
$$
\|\widetilde U_i-I\|\le2\|P_{b_i}(T_i)-I\|+4\varepsilon_i.
$$
右边可和，故实际逆积也在算子范数中收敛，给有界可逆 $G$、$P=G^{-1}$、$g=G1$ 及同组收缩强单位。
其余源因子范数至少1，(2.4) 迫
$$
\boxed{g\notin\mathcal H_{\sqrt3}.}
$$
因此该加权空间只是先前某些源类的充分空间，不能作为全部成功逆源的必要条件。

## 3. 全部负实参数仍有完整列障碍

任意有限负实逆积 $U_i$ 去掉单位相位后保持非负物理坐标锥。
因为 $|\chi_{B_i}|=\Omega$，
$$
\|U_i\chi_{B_i}\|\le n_i.
$$
准确源张量分解以及完整 carry 给
$$
\|X_{\chi_{B_i}}^0g\|\le\|g\|,\qquad
\|X_{\chi_{B_i}}-X_{\chi_{B_i}}^0\|
\le8q_i3^{q_i}\eta_{\min B_i}\to0.
$$
故同一个 $G$ 的这些列逆像一致有界。
另一方面 $q_i$ 为偶数，纯矩准确为
$$
\phi_f(D_{B_i})=2c_i+c_i^2\,2^{q_i},
\qquad c_i=2^{-i-2}.
$$
实际矩误差趋零，而此值发散。
因此全部负实成功逆源族都违反同一 $\phi_f$ 的全列聚合，不需加权结论或负实相位导数平方预算。

## 4. 与紧盘复因子、复近圆扇区的任意混合

参数可任意混合于
$$
(-1,0)\ \cup\ \{0<|a|\le3/4\}\ \cup\
\{|a|<1,\operatorname{Re}a\ge3/4\}.
\tag{4.1}
$$
把负实因子归入正系数逆积 $P_i$，其余紧盘因子数为 $r_i$，
剩余近圆积为 $H_i$，有效参数为
$\tau_i^+=\sum_{\rm cap}(1-|a|^2)/|1+a|^2$。
完整源收敛给整个 Schur 前向积在 $1-q_i^{-1/2}$ 趋1，
径向模亏损迫
$$
r_i=o(\sqrt q_i),\qquad\tau_i^+=o(\sqrt q_i).
$$
不对负实因子施加错误的总相位平方条件。

置 $k_i=\lfloor q_i/3\rfloor$，
$D_i(z)=\prod_{\rm compact}(z+a)$、
$b_i^{\rm c}=\prod_{\rm compact}(1+|a|)$，
$$
u_i=D_i(T_i)v_{q_i,k_i}/b_i^{\rm c},\qquad \|u_i\|\le1.
$$
全部 $2^{q_i}$ 个 Walsh 系数直接 Cauchy–Schwarz 给
$$
\boxed{
\Delta_i=\|X_{u_i}-X_{u_i}^0\|
\le8q_i(3\sqrt2)^{q_i}\eta_{\min B_i}\to0.
}
\tag{4.2}
$$
不能在这些大次数列上用 $q^{(\deg u)/2}$ 粗界。

纯幂准确行列和给
$$
\|T_q^n\|\le
\left(\frac{q+1}{q+2}\right)^n
e^{-n(n^2-1)/(6(q+1)^2)}.
$$
近圆绝对系数主控在半径 $5/7$ 上付完整算子指数
$$
c_\rho=\frac{2\sqrt2}{3}\left(\log\frac75\right)^{3/2}<\frac15.
$$
结合负实正锥和 $\|P_i\Omega\|\le n_i$，
$$
\|Gu_i\|
\le\|g\|\left[
56\sqrt{\binom{q_i}{k_i}}\,
e^{c_\rho(q_i+1)+1/(6q_i)+133\tau_i^+}+\Delta_i\right].
\tag{4.3}
$$

大次数矩的正确中心是
$$
\xi_{q,k}=-1+\frac{2+k/2}{q+2}\to-\frac56,
$$
不能继续使用小次数的 $-1$ 中心。
准确中心生成式从二次项开始，给相对分母误差
$e^{256r_i^2/q_i}-1\to0$，且
$|D_i(\xi_i)|/b_i^{\rm c}\ge28^{-r_i}$。
对齐单位相位后，矩至少为
$$
\frac1{32\sqrt q_i}2^{k_i}\sqrt{\binom{q_i}{k_i}}\,
28^{-r_i}-\lambda-o(1).
$$
因此
$$
\boxed{
\liminf_i\frac1{q_i}
\log\frac{|\phi_f(X_{\omega_i u_i})|}{\|G(\omega_i u_i)\|}
\ge\frac{\log2}{3}-c_\rho>\frac1{45}.
}
\tag{4.4}
$$
有限个同分块完整逆源的线性组合取共同紧盘分母，仍保持上述界；
不把正则器之和的逆当作源的线性组合。

本稿尚未覆盖其他复圆弧、不同分块、无真空原像前向族或真正湮灭矩专属配对。
负实粗源例和固定非湮灭者的全列障碍必须分开理解。
