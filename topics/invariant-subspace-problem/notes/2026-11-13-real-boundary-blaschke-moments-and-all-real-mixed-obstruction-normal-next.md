# 靠近负单位点的实 Blaschke 逆源与任意实参数混合族的全列障碍

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：完整证明的中间结论。** 对参数 $3/4\le a<1$ 的任意多实 Blaschke 逆因子，给出准确正概率表示及统一 $\mathcal H_{\sqrt3}$ 积分界。实际逆源乘积若收敛，则有效参数的平方预算自动可和；在 $\sum1/q_i<\infty$ 时，其实际逆源仍属于 $\mathcal H_{\sqrt3}$。

进一步，将任意实参数 $0<a<1$ 分为紧内部分和近圆部分。紧内分母可被真实有限列消去；近圆余因子由 $\sqrt3$ 双线性端点控制。这排除同一固定分块、同一正常正秩一态下，任意阶、任意实参数的成功 Blaschke 逆源族满足全列聚合界。**不推广到接近单位圆的任意复相位，也不排一般正常湮灭者。**

## 1. 纯块、实际源与有效参数

仍记
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad
Z_q=I-T_q,\qquad
\|T_q\|<1.
$$
对 $0<a<1$，
$$
R_a(T_q)=\frac{aI+T_q}{I+aT_q},
\qquad
U_a(T_q)=R_a(T_q)^{-1}
=\frac{I+aT_q}{aI+T_q}.
\tag{1.1}
$$
前向块收缩，逆块扩张。

以下块大小 $q_i\to\infty$（后文 $\sum_i1/q_i<\infty$ 或固定 $q_i=2^{4i}$ 均保证）；第 $i$ 块允许任意有限个参数 $a_{i\ell}\in(0,1)$，置
$$
R_i=\prod_\ell R_{a_{i\ell}}(T_{q_i}),\qquad
U_i=R_i^{-1},\qquad g_i=U_i\Omega,
$$
$$
\boxed{\tau_i=\sum_\ell\frac{1-a_{i\ell}}{1+a_{i\ell}}.}
\tag{1.2}
$$
其实际提升、正缩放和互不交源列沿用前稿：
$$
\widetilde U_i=X_{g_i}/(1-\varepsilon_i),\qquad
\widetilde g_i=g_i/(1-\varepsilon_i),
$$
并以真实算子范数 carry 预算确保扩张、收缩逆及准确源乘积。假设
$$
g^{(n)}=\prod_{i\le n}\widetilde g_i\to g
\quad\text{于 }H.
\tag{1.3}
$$
只有满足这个实际收敛条件的构造才在以下结论内。

## 2. 实逆源收敛强制 $\sum\tau_i^2/q_i<\infty$

先重列所需无限乘积事实。所有 $g_i$ 为实系数且范数至少为 $1$。对实际源范数
$s_i=\|\widetilde g_i\|\ge1$，(1.3) 给
$\sum(s_i-1)<\infty$。归一化块
$e_i=\widetilde g_i/s_i$ 的实真空重叠最终为正；准确尾乘积内积与 Cauchy 性给
$\sum(1-\langle e_i,\Omega\rangle)<\infty$。于是
$$
\sum_i\varepsilon_i<\infty,\qquad
\sum_i|\langle g_i,\Omega\rangle-1|<\infty,\qquad
\sum_i\|g_i-\Omega\|^2<\infty.
\tag{2.1}
$$

纯反射共轭给
$\|R_i^*\Omega-\Omega\|=\|R_i\Omega-\Omega\|$。
由 $R_ig_i=\Omega$、$\|R_i\|\le1$，
$$
0\le1-\operatorname{Re}\langle R_i\Omega,\Omega\rangle
\le|\langle g_i,\Omega\rangle-1|+\|g_i-\Omega\|^2.
$$
所以
$$
\sum_i[1-\operatorname{Re}\langle R_i\Omega,\Omega\rangle]<\infty.
\tag{2.2}
$$

### 全部有效参数的相位下界

实 Blaschke 因子的圆周相位满足
$$
\frac d{d\theta}\arg\frac{a+e^{i\theta}}{1+ae^{i\theta}}
=
\frac{1-a^2}{|e^{i\theta}+a|^2}
=
\frac{(1-a)/(1+a)}
 {1-\frac{4a}{(1+a)^2}\sin^2(\theta/2)}.
\tag{2.3}
$$
因此在 $|\theta|\le q^{-1/2}\le1/2$ 上，乘积的连续相位
$\psi(\theta)$ 是奇函数，$\psi(0)=0$，并满足
$$
\tau\le\psi'(\theta)\le2\tau.
\tag{2.4}
$$
这个估计对全部 $0<a<1$、任意因子数、任意大小的 $\tau$ 统一。

真空圆周概率密度为
$$
w_q(\theta)=1+2\sum_{n=1}^q\frac{(q)_n}{(q+2)^n}\cos(n\theta).
$$
前稿已完整证明其非负性及
$q^{-1/2}w_q(x/\sqrt q)\to\sqrt{2\pi}e^{-x^2/2}$
的紧窗一致极限。因此在上述小窗内，
$w_q(\theta)\ge c\sqrt q$，$q$ 充分大。

令 $h=q^{-1/2}$、$A=\psi(h)\ge\tau h$。由
$\psi'\le2\tau$ 和
$A-\sin A\ge(A/10)\min(A^2,1)$，得到
$$
\int_{-h}^h[1-\cos\psi(\theta)]\,d\theta
\ge\frac{A-\sin A}{\tau}
\ge\frac h{10}\min(\tau^2/q,1).
$$
$\tau=0$ 时平凡。代入真空概率积分，得固定 $c_0>0$ 使
$$
\boxed{
1-\operatorname{Re}\langle R_i\Omega,\Omega\rangle
\ge c_0\min(\tau_i^2/q_i,1)
}
\tag{2.5}
$$
对所有充分大的块成立。结合 (2.2)，
$$
\boxed{\sum_i\tau_i^2/q_i<\infty.}
\tag{2.6}
$$
这里既控制小参数，也排除了无穷多个大参数块。

## 3. 近圆实因子的准确混合跃迁表示

现在只考虑 $3/4\le a<1$。令 $W_a$ 为以下非负随机变量：

- 概率 $a$ 时 $W_a=0$；
- 概率 $1-a$ 时，$W_a$ 服从参数 $1+a$ 的指数分布。

于是
$$
\mathbb E W_a=\frac{1-a}{1+a},
$$
并且
$$
\boxed{
U_a(T)=aI+(1-a)\mathbb E_{\mathrm{Exp}(1+a)}e^{SZ}
=\mathbb E e^{W_aZ}.
}
\tag{3.1}
$$
这是准确算子恒等式，因为
$\mathbb E_{\mathrm{Exp}(1+a)}e^{SZ}
=(1+a)(aI+T)^{-1}$。

多个因子用独立的 $W_a$，令 $S=\sum W_a$，则
$$
\boxed{
\left(\prod_\ell U_{a_\ell}(T_q)\right)\Omega
=\mathbb E[e^Sv_q(S)],
}
\tag{3.2}
$$
其中
$$
v_q(s)=
\bigotimes_{j=1}^q
\left[\left(1-\frac{s}{q+2}\right)\Omega_+
+\frac{s}{q+2}\chi_j\right].
$$
每个块因子数有限；所有矩和有限维 Bochner 积分均实际存在。

对 $0\le u<7/4$，
$$
\mathbb E e^{uW_a}
=1+\frac{(1-a)u}{1+a-u}.
$$
置 $\tau=\sum(1-a)/(1+a)$，用 $\log(1+x)\le x$，得到
$$
\boxed{
\log\mathbb E e^{uS}
\le\frac{\tau u}{1-4u/7}.
}
\tag{3.3}
$$
这不要求总因子数有界，只使用有效参数 $\tau$。

## 4. $\mathcal H_{\sqrt3}$ 的整个概率积分

记 $r=\sqrt3$。已有准确纯块估计
$$
\|e^sv_q(s)\|_r
\le\exp[2(s+s^2)/q],
\qquad
\|e^sv_q(s)\|_r\le e^{69s/40}.
\tag{4.1}
$$
第一式来自 $\log y\le y-1$；第二式来自全局
$1-2x+4x^2\le e^{29x/20}$。其严格积分余量在下文保留。

取 $q\ge2^{44}$、$\tau\le\sqrt q$，令 $b=q/64$、
$F(s)=\exp[2(s+s^2)/q]$，于是 $5\tau\le b$。在 $s\le b$，
$$
F(s)\le e^{s/16},\qquad
F'(s)\le(2+4s)e^{s/16}/q.
$$
(3.3) 的 $u=1$ 给
$$
\mathbb P(S>s)\le e^{(7/3)\tau-s}
\le e^{-s/2}\qquad(s\ge5\tau).
$$
所以
$$
\boxed{
\mathbb E[F(S)1_{\{S\le b\}}]
\le e^{(10\tau+50\tau^2)/q}+26/q.
}
\tag{4.2}
$$

大尾取
$$
u=\frac{139}{80}<\frac74,\qquad
u-\frac{69}{40}=\frac1{80}.
$$
由 (3.3)，
$\log\mathbb E e^{uS}\le(973/4)\tau$。因此
$$
\begin{aligned}
\mathbb E[e^{69S/40}1_{\{S>b\}}]
&\le\exp[-q/5120+(973/4)\tau]\\
&\le e^{-q/10240}.
\end{aligned}
\tag{4.3}
$$
最后一步由 $\tau\le\sqrt q$ 和 $\sqrt q\ge2^{22}>973\cdot2560$ 保证。

Minkowski 和 (3.2) 给
$$
\boxed{
\log\left\|
\left(\prod_\ell U_{a_\ell}(T_q)\right)\Omega
\right\|_{\sqrt3}^2
\le
\frac{20\tau+100\tau^2+52}{q}
+2e^{-q/10240}.
}
\tag{4.4}
$$
各常数与因子数及 $a$ 到 $1$ 的距离无关。有限个初块分别有限维，不影响下面的无限结论。

## 5. 纯近圆族的实际逆源仍属于 $\mathcal H_{\sqrt3}$

若所有参数都在 $[3/4,1)$，实际逆源乘积收敛，并且
$\sum_i1/q_i<\infty$，则 (2.6) 与
$2\tau_i\le1+\tau_i^2$ 保证 (4.4) 右侧可和。
第2节还给 $\sum_i\varepsilon_i<\infty$。

实际真空列是准确普通块乘积，因此其 $\sqrt3$ 加权范数的有限乘积一致有界；原 $H$ 收敛和 Walsh 系数 Fatou 得
$$
\boxed{g\in\mathcal H_{\sqrt3}.}
\tag{5.1}
$$
R244 与 R255 于是给整个次数空间上的真实逆界
$\|Gu\|\le C_g\|u\|_{\sqrt3}$。特别，任何聚合表示都要求一次正常矩属于 $\ell^2$。

所以，靠负单位点的任意多实零点没有自动越过一次矩障碍；对既有固定非 $\ell^2$ 一次矩态，这类 $P$ 仍在一次层失败。这里不从近圆纯概率表示推出未经证明的实际乘法同态，仅用准确源列和已证实际最小图。

## 6. 任意实参数混合：取消紧内分母，控制近圆余因子

现在回到任意有限实参数集合 $a_{i\ell}\in(0,1)$，不限制因子总数。令
$$
r_i=\#\{\ell:a_{i\ell}\le3/4\}.
$$
由 (1.2)，每个紧内因子贡献至少 $1/7$，因此
$$
r_i\le7\tau_i,\qquad
\sum_i r_i^2/q_i<\infty,\qquad
r_i=o(\sqrt{q_i}).
\tag{6.1}
$$

将纯逆分为
$$
U_i=U_i^{\mathrm{near}}\,
\frac{N_i^{\mathrm{in}}(T_i)}{D_i^{\mathrm{in}}(T_i)},
$$
$$
D_i^{\mathrm{in}}(z)=\prod_{a_{i\ell}\le3/4}(z+a_{i\ell}),
\quad
N_i^{\mathrm{in}}(z)=\prod_{a_{i\ell}\le3/4}(1+a_{i\ell}z),
$$
并令
$$
b_i=D_i^{\mathrm{in}}(1)=N_i^{\mathrm{in}}(1).
$$
近圆部分的有效参数不超过 $\tau_i$。由 (4.4) 和
$\tau_i^2/q_i\to0$，其纯真空源
$g_i^{\mathrm{near}}=U_i^{\mathrm{near}}\Omega$
满足
$$
\sup_{i\text{ 足够大}}\|g_i^{\mathrm{near}}\|_{\sqrt3}<\infty.
\tag{6.2}
$$
本处只需各块统一界，不必预先断言近圆子积本身已经产生某个实际正则器。

设
$$
v_{q,k}=\binom qk^{-1/2}
 \sum_{\substack{F\subset B\\|F|=k}}\chi_F,
\qquad \|v_{q,k}\|=1.
$$
取 $k_i=r_i+2$，并定义真正有限列
$$
\boxed{
u_i=
\frac{D_i^{\mathrm{in}}(T_i)v_{q_i,k_i}}
 {b_i\,3^{k_i/2}}.
}
\tag{6.3}
$$
其范数至多 $3^{-k_i/2}$，Walsh 次数至多
$2r_i+2=o(\sqrt{q_i})$。

纯有限代数中分母准确消去。又
$\|N_i^{\mathrm{in}}(T_i)/b_i\|\le1$，与近圆逆交换。R255 的纯双输入 $\sqrt3$ 端点给
$$
\|U_i^{\mathrm{near}}v_{q_i,k_i}\|
=\|X_{v_{q_i,k_i}}^0g_i^{\mathrm{near}}\|
\le3^{k_i/2}\|g_i^{\mathrm{near}}\|_{\sqrt3}.
$$
所以
$$
\boxed{\|U_iu_i\|\le C_1}
\tag{6.4}
$$
对充分大 $i$ 一致。

准确全局源分块给
$\|X_{u_i}^0g\|\le C_1\|g\|$，因为 $\|g_i\|\ge1$。
实际有限列提升误差仍由前稿的
$$
8s_i3^{s_i}\sqrt{s_i+1}\,q_i^{s_i/2}\eta_{\min B_i},
\qquad s_i=2r_i+2,
$$
控制。其非 carry 对数为 $o(q_i)$，原 $q_i5^{q_i}\eta$ 预算足够。因此
$$
\boxed{\|Gu_i\|\le C_2}
\tag{6.5}
$$
对同一个实际 $G=P^{-1}$ 成立。

## 7. 同一固定正常态的矩仍趋于无穷

本节固定前稿一次选定的分块
$$
q_i=2^{4i},\qquad
f=1+\sum_i2^{-i-2}\chi_{B_i},\qquad
c_i^2=\frac1{16\sqrt{q_i}},\quad\lambda=49/48.
$$
不改变 $f$，不为各测试列另选正常态。

前稿精确 Boolean 指数生成式给：对紧内分母、$k_i=r_i+2$，
$$
\langle X_{u_i}^0\chi_{B_i},\chi_{B_i}\rangle
=
\left(\frac2{\sqrt3}\right)^{k_i}
\sqrt{\binom{q_i}{k_i}}\,
\frac{D_i^{\mathrm{in}}(-1)}{b_i}(1+\zeta_i),
$$
$$
|\zeta_i|
\le\exp[(18r_i^2+12r_i)/q_i]-1\longrightarrow0,
\qquad
\frac{|D_i^{\mathrm{in}}(-1)|}{b_i}\ge7^{-r_i}.
\tag{7.1}
$$
原精确生成式为
$2^{-k}\langle e^{t(T+I)}D_F^0\chi_B,\chi_B\rangle
=e^t(1-t/Q)^{q-k}(1-t/(2Q))^k$；
因此 (7.1) 包括重复位及分母相对误差，而不是只保留正主项。

次数 $2r_i+2<q_i$ 保证纯矩中没有完整块交叉项。取相位消去 $D_i^{\mathrm{in}}(-1)$ 的符号，并保留至多 $\lambda$ 的真空项，则
$$
|\phi_f(X_{u_i})|
\ge\frac12 A_i-\lambda-o(1),
$$
其中
$$
A_i=
\frac1{16\sqrt{q_i}}
\left(\frac2{\sqrt3}\right)^{r_i+2}
\sqrt{\binom{q_i}{r_i+2}}\,
7^{-r_i}.
\tag{7.2}
$$
实际与纯矩差由同一个 carry 范数界趋于零。

若 $r_i\ge1$，充分大时 $r_i+2\le\sqrt{q_i}$。
由 $\binom qk\ge(q/k)^k$，
$$
A_i\ge
\frac1{12}
\left(\frac{2q_i^{1/4}}{7\sqrt3}\right)^{r_i}
\ge\frac{q_i^{1/4}}{42\sqrt3}\longrightarrow\infty.
$$
$r_i=0$ 时，(7.2) 直接给
$A_i=(1/12)\sqrt{(q_i-1)/2}\to\infty$。
结合 (6.5)，得到
$$
\boxed{
\frac{|\phi_f(X_{u_i})|}{\|Gu_i\|}
\longrightarrow\infty.
}
\tag{7.3}
$$

因此，在同一固定分块、同一 $f$ 下，任意阶、任意实参数
$0<a<1$ 的这类成功 Blaschke 逆源构造均不能满足 R244 全列聚合界。分母根趋近 $-1$ 的部分不需要强行归入紧内零点计数；它由正概率表示与真实双输入端点支付。

这没有覆盖接近单位圆的任意复相位、块内非乘积组合、不同分块或无真空原像族。所用 $f$ 连续非负，早已不是慢主理想湮灭者。本稿仍是正则器范围的严格障碍，未完成一般正常见证专属配对或普通 ISP。


## 完整依赖

- [复分母消去与 Schur 零点约束](../results/R230-appendix-complex-rational-cancellation-and-schur-zero-count.md)：真实有限列、相对矩误差和 carry。
- [零点自由指数块记录](2026-11-13-zero-free-cayley-exponential-blocks-and-sqrt3-inverse-source-boundary-normal-next.md)：实源乘积可和量与全概率尾处理。
- [R255 双输入端点](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)：纯有限块及实际最小闭图。
