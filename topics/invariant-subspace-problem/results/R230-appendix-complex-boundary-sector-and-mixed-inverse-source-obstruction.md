# R230 附录：复近圆扇区的逆源加权界与混合全列障碍

日期：2026-11-13。作者：Astra-ISP-0c017065 / normal_complex。
状态：完整中间结论；普通 Hilbert ISP 未完成。主会话已全文核验。
完整证明见[复扇区源稿](../notes/2026-11-13-complex-boundary-sector-blaschke-sources-and-mixed-obstruction-normal-complex.md)。

## 1. 原实际前提与结论

纯有限块取
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad Z_q=I-T_q,\qquad
\Omega=\Omega_+^{\otimes q},
$$
并以
$$
\beta_a(z)=\frac{1+\bar a}{1+a}\frac{z+a}{1+\bar a z},
\qquad 0<|a|<1,\qquad \beta_a(1)=1
$$
归一化 Blaschke 因子。每块允许任意有限个因子和整体单位相位：
$$
R_i=\xi_i\prod_\ell\beta_{a_{i\ell}}(T_{q_i}),\qquad
U_i=R_i^{-1},\qquad g_i=U_i\Omega.
$$
$R_i$ 是可逆收缩，$U_i$ 扩张。

始终假设互不交的真实源乘积
$$
g^{(n)}=\prod_{i\le n}\frac{g_i}{1-\varepsilon_i}\longrightarrow g
\quad\text{于原 }H,\qquad 0\le\varepsilon_i<1/2,\quad q_i\to\infty.
\tag{1.1}
$$
凡使用最小逆，再要求真实构造已给 $P\in A'$、$Pg=1$ 及同一组一致有界强单位。R244 此时给
$$
G=P^{-1}=X_g,\qquad Gu=X_ug,
$$
有限 Walsh 柱为准确图核心。混合列还使用原完整 carry 预算
$$
16q_i5^{q_i}\max(1,\|g_i\|)\eta_{\min B_i}\le\varepsilon_i.
\tag{1.2}
$$
任意参数本身不保证这些构造前提。

**定理 A。** 若全部参数满足 $\operatorname{Re}a\ge3/4$、$|a|<1$，
且 $\sum_iq_i^{-1}<\infty$，则实际收敛源 $g\in\mathcal H_{\sqrt3}$。

**定理 B。** 固定
$$
q_i=2^{4i},\qquad
f=1+\sum_i2^{-i-2}\chi_{B_i},\qquad \|f\|^2=49/48.
\tag{1.3}
$$
若每个参数位于
$$
\mathcal R=\{0<|a|\le3/4\}\cup
\{|a|<1,\ \operatorname{Re}a\ge3/4\},
\tag{1.4}
$$
且上述实际构造成功，则同一个正常态 $\phi_f$ 不满足 R244 全列聚合表示。
允许任意增长的因子数、任意单位相位，以及有限个同分块完整成功逆源的线性组合（若该组合本身又为某个合格 $P^{-1}1$）。

$f$ 连续、非负、实且 $C$ 实，已知不是慢主理想湮灭者。因此定理 B 仅限制这些正则器对一般正常态的适用范围，不排除真正正正常湮灭见证。

## 2. 相位无关的平方预算

令 $n_i=\|g_i\|\ge1$、$d_i=n_i^2-1$，
$g_i=\alpha_i\Omega+h_i$、$h_i\perp\Omega$。
由正缩放源乘积收敛及归一化张量尾内积的模，
$$
\sum_i d_i<\infty,\qquad
\sum_i\varepsilon_i<\infty,\qquad
\sum_i\|h_i\|^2<\infty.
\tag{2.1}
$$
这里不要求复数 $\alpha_i$ 的相位绝对可和。

$C$ 对称性和 $R_ig_i=\Omega$ 给
$$
R_i\Omega=\frac{Cg_i}{n_i^2}+z_i,\qquad
z_i\perp Cg_i,\qquad \|z_i\|^2\le d_i/n_i^2.
$$
所以 $\mu_i=\langle R_i\Omega,\Omega\rangle$ 满足
$$
1-|\mu_i|^2\le3d_i+2\|h_i\|^2,\qquad
\sum_i(1-|\mu_i|^2)<\infty.
\tag{2.2}
$$

准确真空矩 $c_{q,n}=(q)_n/(q+2)^n$ 给圆周概率密度
$w_q(\theta)=1+2\sum_{n=1}^qc_{q,n}\cos(n\theta)$。
[Schur 全稿](../notes/2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)
的局部 Gaussian 下界使它在 $|\theta|\le q^{-1/2}$ 上至少为 $c\sqrt q$。

令
$$
t_a=\frac{1-|a|^2}{|1+a|^2},\qquad \tau_i=\sum_\ell t_{a_{i\ell}}.
$$
复扇区中前向相位导数在该窗口内介于 $\tau/2$ 和 $2\tau$。
准确方差是
$$
1-|\mu|^2=\iint[1-\cos(\psi(\theta)-\psi(\varphi))]
\,d\sigma_q(\theta)d\sigma_q(\varphi).
$$
作双相位变量替换，长度 $L$ 的像区间贡献
$L^2-4\sin^2(L/2)$。其全部尺度下界给
$$
1-|\mu|^2\ge c_0\min(\tau^2/q,1).
$$
故
$$
\boxed{\sum_i\tau_i^2/q_i<\infty.}
\tag{2.3}
$$
这不是只在小参数上使用 Taylor 近似。混合区域 (1.4) 中相位导数仍有固定上下比较常数，故同一结论成立。

## 3. 复 Taylor 主控与完整加权尾

对扇区参数，
$$
U_a(T_q)=\frac{I-B_aZ_q}{I-A_aZ_q},\qquad
A_a=\frac1{1+a},\quad B_a=\frac{\bar a}{1+\bar a},
$$
$$
A_a-B_a=t_a>0,\qquad |A_a|,|B_a|\le4/7.
$$
去掉整体相位，有限积写为 $h(Z_q)$、$h(0)=1$，则逐系数有
$$
|[z^n]h(z)|\le[z^n]\exp\left(\frac{\tau z}{1-4z/7}\right).
\tag{3.1}
$$
右边是 compound Poisson 变量 $S$ 的矩母函数：
次数率 $7\tau/4$，跳跃为 $\operatorname{Exp}(7/4)$。
它只主控复函数的绝对 Taylor 系数，不把 $h$ 本身解释成正积分。

令 $W_q=3^{\mathsf N/2}$，
$\mathcal F_q(z)=W_qe^{zZ_q}\Omega$。
准确张量式给全复方向界
$$
\|\mathcal F_q(z)\|\le e^{69|z|/40},\qquad 69/40<7/4.
\tag{3.2}
$$
其真空差和非真空部分的绝对 Taylor 和分别满足
$$
H_{q,0}(s)\le\frac{4(s+s^2)}q e^{4(s+s^2)/q}
\quad(s\le(q+2)/4),
$$
$$
H_{q,\perp}(s)\le\frac{4s}{\sqrt q}e^{(6s+8s^2)/q}.
$$
全尾用半径 $(1+1/512)s$ 的 Cauchy 界，指数型
$35397/20480<139/80<7/4$ 留出严格余量。

$q\ge2^{52}$、$\tau\le\sqrt q$ 时，在 $s=q/1024$ 分头尾：
头用 $\mathbb P(S>s)\le e^{-s/2}$（$s\ge5\tau$）积分导数；
尾用 $\log\mathbb Ee^{139S/80}=(973/4)\tau$。
全部积分和绝对求和合法，得到
$$
\boxed{
\|h(Z_q)\Omega\|_{\sqrt3}^2
\le1+\frac{C(1+\tau^2)}q+Ce^{-cq},
\qquad c=\frac{187}{5\cdot2^{23}}.
}
\tag{3.3}
$$
常数不依赖参数、因子数或块长。
(2.3)、$\sum1/q_i<\infty$ 与源正缩放预算使有限乘积加权范数一致有界；
原 $H$ 收敛再用逐 Walsh 系数 Fatou 即证定理 A。
R255 给 $\|Gu\|\le C_g\|u\|_{\sqrt3}$。
(1.3) 的实际一次矩不在 $\ell^2$，故纯扇区已在一次聚合层失败。

## 4. 混合分母的真实列

令 $r_i$ 为第 $i$ 块中 $|a|\le3/4$ 的因子数。
每个此类因子 $t_a\ge1/7$，由 (2.3)，
$$
r_i\le7\tau_i=o(\sqrt{q_i}).
$$
置
$$
D_i(z)=\prod_{\rm in}(z+a),\quad
b_i=\prod_{\rm in}(1+|a|),\quad k_i=r_i+2,
$$
$$
v_{q,k}=\binom qk^{-1/2}\sum_{|F|=k}\chi_F,\qquad
u_i=\frac{D_i(T_i)v_{q_i,k_i}}{b_i3^{k_i/2}}.
\tag{4.1}
$$
这是真有限 Walsh 列，$\|u_i\|\le1$，次数至多 $2r_i+2=o(\sqrt q_i)$。
紧内分母准确消去，余下分子系数绝对和除以 $b_i$ 后至多1。
近圆源由 (3.3) 有一致加权界，纯双输入端点支付
$3^{k_i/2}$，故 $\|U_iu_i\|$ 一致有界。
互不交源分块及 (1.2) 付完整实际列误差
$$
\Delta_i\le8s_i3^{s_i}\sqrt{s_i+1}\,q_i^{s_i/2}\eta_{\min B_i}\to0,
\quad s_i=2r_i+2.
$$
于是
$$
\sup_i\|Gu_i\|<\infty.
\tag{4.2}
$$

[复分母完整稿](../notes/2026-11-13-complex-rational-block-denominator-cancellation-and-growing-order-obstruction-normal-next.md)
的准确生成式
$$
2^{-k}\langle e^{t(T+I)}D_F^0\chi_B,\chi_B\rangle
=e^t(1-t/Q)^{q-k}(1-t/(2Q))^k
$$
给相对误差 $\le e^{(18r_i^2+12r_i)/q_i}-1\to0$，
并有 $|D_i(-1)|/b_i\ge7^{-r_i}$。
选单位相位 $\omega_i$ 对齐 $D_i(-1)$ 后，
$$
\operatorname{Re}\phi_f(X_{\omega_i u_i}^0)
\ge\frac12 A_i-\frac{49}{48},\qquad
A_i=\frac1{16\sqrt{q_i}}
 \left(\frac2{\sqrt3}\right)^{r_i+2}
 \sqrt{\binom{q_i}{r_i+2}}\,7^{-r_i}\to\infty.
$$
实际矩误差至多 $(49/48)\Delta_i$，所以
$$
\frac{|\phi_f(X_{\omega_i u_i})|}{\|G(\omega_i u_i)\|}
\longrightarrow\infty.
\tag{4.3}
$$
固定正常态和分块始终相同。
有限个同分块完整逆源组合取共同紧内分母，仍有总阶 $o(\sqrt q_i)$，
每支的近圆端点预算与有限三角和保持 (4.2)；
同一共同分母给 (4.3)。
这不适用于正则器之和的逆，也不自动适用于块内任意有理和。

## 5. 继续范围

(1.4) 不是全部单位圆盘；其他逼圆弧可能缺相位比较或 Taylor 指数余量。
不同分块、无真空原像的前向族、真正湮灭矩选取的特殊正则器以及慢符号有界分母仍开放。
本稿不将一般正常性改称加权次数矩条件，也不将固定非湮灭者的构造障碍扩成普通 ISP 结论。
