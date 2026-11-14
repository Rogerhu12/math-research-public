# R230 附录：零点自由指数源与任意实 Blaschke 逆块的全列边界

日期：2026-11-13。作者：Astra-ISP-0c / normal_next。

本附录处理前稿紧内复零点计数尚未覆盖的两类逆源。完整逐步证明见[零点自由指数稿](../notes/2026-11-13-zero-free-cayley-exponential-blocks-and-sqrt3-inverse-source-boundary-normal-next.md)及[近圆实因子与混合稿](../notes/2026-11-13-real-boundary-blaschke-moments-and-all-real-mixed-obstruction-normal-next.md)。结论仍限于同一实际分块和指定固定非湮灭正常态，普通 ISP 未完成。

## 1. 公共实际前提

取互不交实际位块，纯块算子
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad
\Omega=\Omega_+^{\otimes q}.
$$
各纯前向块 $R_i$ 收缩可逆，$U_i=R_i^{-1}$ 扩张，纯源 $g_i=U_i\Omega$。实际准确源列是
$$
\widetilde g_i=g_i/(1-\varepsilon_i),\quad0\le\varepsilon_i<1/2.
$$
假设真实 Walsh 提升已付扩张及逆图 carry，且互不交源乘积在原 $H$ 收敛到 $g$。只有构造另已给 $P$、$Pg=1$ 和同组有界强单位时，才使用 R244 的 $G=P^{-1}=X_g$ 及全有限柱图核心。

本文两个族均为实源。准确范数乘积和归一化真空重叠的尾乘积给
$$
\sum_i\varepsilon_i<\infty,\quad
\sum_i|\langle g_i,\Omega\rangle-1|<\infty,\quad
\sum_i\|g_i-\Omega\|^2<\infty.
$$
纯反射 $C$ 对称、$R_ig_i=\Omega$ 和收缩性随后给
$$
\sum_i\bigl[1-\operatorname{Re}\langle R_i\Omega,\Omega\rangle\bigr]<\infty.
$$
不能把这一实源论证直接用于未归一化的复相位无限乘积。

真空概率密度
$$
w_q(\theta)=1+2\sum_{n=1}^q\frac{(q)_n}{(q+2)^n}\cos(n\theta)
$$
非负，且 $q^{-1/2}w_q(x/\sqrt q)\to\sqrt{2\pi}e^{-x^2/2}$ 在紧窗一致。对以下内函数的边界相位积分，这给真实的局部下界；指数函数在 $-1$ 的边界奇点由径向逼近和控制收敛支付。

## 2. 零点自由 Cayley 指数块

令
$$
F_q=(I-T_q)(I+T_q)^{-1},\qquad
R_{q,t}=e^{-tF_q},\quad U_{q,t}=e^{tF_q},\quad t\ge0.
$$
$\operatorname{Re}F_q\ge(2q+3)^{-1}I$，所以逆真空范数从 $1$ 连续严格增到无穷，每个有限目标 $1+\delta$ 确能唯一调到。这不蕴含无限源乘积收敛。

标量前向边界值为 $e^{it\tan(\theta/2)}$。对 $|\theta|\le q^{-1/2}$ 作单调相位变量替换，使用 $A-\sin A\ge(A/10)\min(A^2,1)$，得到
$$
1-\operatorname{Re}\langle R_{q,t}\Omega,\Omega\rangle
\ge c_0\min(t^2/q,1)
$$
对全部 $t\ge0$ 一致。故实际逆源收敛强制
$$
\boxed{\sum_i t_i^2/q_i<\infty.}
$$

令 $S$ 为 $\operatorname{Poi}(t)$ 个独立 $\operatorname{Exp}(2)$ 跃迁之和，其矩母函数是 $\mathbb Ee^{uS}=\exp[tu/(2-u)]$。准确有限维函数演算给
$$
g_{q,t}=\mathbb E[e^S v_q(S)],\qquad
v_q(s)=\bigotimes_{j=1}^q
\left[\left(1-\frac{s}{q+2}\right)\Omega_+
+\frac{s}{q+2}\chi_j\right].
$$
整块的 $\sqrt3$ 次数加权范数满足
$$
\|e^sv_q(s)\|_{\sqrt3}\le
\min\left(e^{2(s+s^2)/q},e^{69s/40}\right).
$$
在 $q\ge2^{28}$、$t\le\sqrt q$，以 $q/64$ 分段；小尾用矩母函数 $u=1$，大尾用 $u=15/8>69/40$。全部积分给
$$
\boxed{
\log\|g_{q,t}\|_{\sqrt3}^2
\le\frac{8t+16t^2+52}{q}+2e^{-3q/2560}.
}
$$
所以若另有 $\sum_i1/q_i<\infty$，实际收敛逆源必属于 $\mathcal H_{\sqrt3}$。R255/R244 使完整一次层上的真实逆有界，因而不能表示一次矩非 $\ell^2$ 的固定正常态。

无权同一积分还给
$$
\|g_{q,t}\|^2\le1+100/\sqrt q
\qquad(q\ge2^{28},\ t\le\sqrt q).
$$
故原 $q_i=2^{4i}$、$\delta_i=\delta_*2^{-i}$ 的有限块调幅若要求 $\|g_i\|^2=1+\delta_i$，最终必 $t_i>\sqrt{q_i}$，直接违反源收敛的必要平方预算。可和范数增量没有支付可和均值。

## 3. 任意多近圆实 Blaschke 因子

对 $0<a<1$，记
$$
R_a(T)=\frac{aI+T}{I+aT},\qquad
U_a(T)=\frac{I+aT}{aI+T}.
$$
每块允许任意有限个因子，定义
$$
\tau_i=\sum_\ell\frac{1-a_{i\ell}}{1+a_{i\ell}}.
$$
完整前向相位在 $|\theta|\le q^{-1/2}$ 满足 $\tau\le\psi'(\theta)\le2\tau$、$\psi(0)=0$。同一密度下界给实际收敛逆源的必要条件
$$
\boxed{\sum_i\tau_i^2/q_i<\infty,}
$$
对全部 $0<a<1$ 和任意因子数成立。

若 $a\ge3/4$，令非负 $W_a$ 以概率 $a$ 为零，以概率 $1-a$ 服从 $\operatorname{Exp}(1+a)$。则
$$
U_a(T)=\mathbb Ee^{W_a(I-T)},\qquad
\mathbb EW_a=\frac{1-a}{1+a}.
$$
同一块的独立跃迁和 $S$ 满足
$$
\log\mathbb Ee^{uS}\le\frac{\tau u}{1-4u/7}\qquad(0\le u<7/4).
$$
用上述准确 $v_q$ 表示，小尾取 $u=1$，大尾取 $u=139/80>69/40$，得到
$$
\boxed{
\log\left\|\prod_\ell U_{a_\ell}(T_q)\Omega\right\|_{\sqrt3}^2
\le\frac{20\tau+100\tau^2+52}{q}+2e^{-q/10240}
}
$$
对 $q\ge2^{44}$、$\tau\le\sqrt q$ 成立，常数与因子数及距圆周的距离无关。有限初块分别有限维。因此纯近圆族若源收敛且 $\sum1/q_i<\infty$，仍有 $g\in\mathcal H_{\sqrt3}$，一次聚合已失败。

## 4. 全部实参数混合族的真实消去列

现固定原来的
$$
q_i=2^{4i},\qquad
f=1+\sum_i2^{-i-2}\chi_{B_i},\qquad
c_i^2=(16\sqrt{q_i})^{-1},\quad\|f\|^2=49/48.
$$
这是同一个连续正 $C$ 实非湮灭态，未随测试列改选。

将任意 $0<a_{i\ell}<1$ 分成 $a\le3/4$ 的紧内部分和其余近圆部分。紧内因子数 $r_i\le7\tau_i$，所以 $r_i=o(\sqrt{q_i})$。写其分母为 $D_i^{\rm in}$、$b_i=D_i^{\rm in}(1)$。近圆部分的纯源 $g_i^{\rm near}$ 由上节的整体积分具有一致 $\sqrt3$ 加权范数上界。

取 $k_i=r_i+2$ 和真实有限列
$$
u_i=\frac{D_i^{\rm in}(T_i)v_{q_i,k_i}}{b_i3^{k_i/2}},
\qquad
v_{q,k}=\binom qk^{-1/2}\sum_{|F|=k}\chi_F.
$$
纯有限代数中紧内分母准确消去，剩余分子除以 $b_i$ 的范数不超过 $1$。R255 的纯双输入端点支付近圆余因子：
$$
\|U_i^{\rm near}v_{q_i,k_i}\|
\le3^{k_i/2}\|g_i^{\rm near}\|_{\sqrt3}.
$$
因此 $\|U_iu_i\|$ 一致有界。输入次数 $2r_i+2=o(\sqrt{q_i})$ 的实际提升成本对数是 $o(q_i)$，由原 $q_i5^{q_i}\eta_{\min B_i}$ 预算支付，所以同一个实际 $G=P^{-1}$ 满足 $\sup_i\|Gu_i\|<\infty$。

[复分母稿](R230-appendix-complex-rational-cancellation-and-schur-zero-count.md)的精确块矩及其相对误差给
$$
|\phi_f(X_{u_i})|
\ge\frac12 A_i-\frac{49}{48}-o(1),\qquad
A_i=\frac1{16\sqrt{q_i}}
\left(\frac2{\sqrt3}\right)^{r_i+2}
\sqrt{\binom{q_i}{r_i+2}}\,7^{-r_i}.
$$
$r_i\ge1$ 时 $A_i\ge q_i^{1/4}/(42\sqrt3)\to\infty$；$r_i=0$ 时 $A_i=(1/12)\sqrt{(q_i-1)/2}\to\infty$。故全列配对比值发散。

这排除同一固定分块和同一 $f$ 下任意阶、任意实参数 $0<a<1$ 的成功 Blaschke 逆源族。尚未覆盖逼近单位圆的任意复相位、非乘积块、不同分块、无真空原像族或真湮灭者专属配对，也未构造慢符号的有界分母。
