# 零点自由 Cayley 指数块：收敛逆源仍有平方根三次数矩

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065。

**状态：完整证明的中间结论。** 对
$$
F_q=(I-T_q)(I+T_q)^{-1},\qquad
R_{q,t}=e^{-tF_q},\qquad U_{q,t}=e^{tF_q},
$$
证明有限块逆真空范数确可连续调节，但若实际逆真空块乘积收敛且 $\sum_iq_i^{-1}<\infty$，则自动有
$\sum_i t_i^2/q_i<\infty$，并且同一个实际逆源 $g$ 属于
$\mathcal H_{\sqrt3}$。因此该零点自由族仍不能为既有一次矩不在 $\ell^2$ 的固定正常态满足 R244 聚合界。

证明没有虚构有限分母；使用真空圆周密度、正的复合 Poisson 表示及整个积分尾。

## 1. 有限块的增生性与范数连续调节

仍记
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad
\|T_q\|\le\tau_q:=\frac{q+1}{q+2}<1,
\qquad \Omega=\Omega_+^{\otimes q}.
$$
置
$$
F_q=(I-T_q)(I+T_q)^{-1}
=2(I+T_q)^{-1}-I.
\tag{1.1}
$$
准确有
$$
\operatorname{Re}F_q
=(I+T_q^*)^{-1}(I-T_q^*T_q)(I+T_q)^{-1}
\ge\frac{1-\tau_q}{1+\tau_q}I
=\frac1{2q+3}I.
\tag{1.2}
$$
因此 $R_{q,t}=e^{-tF_q}$ 为收缩，其逆 $U_{q,t}=e^{tF_q}$ 扩张，$t\ge0$。

令
$$
g_{q,t}=U_{q,t}\Omega.
$$
有限维微分给
$$
\frac d{dt}\|g_{q,t}\|^2
=2\operatorname{Re}\langle F_qg_{q,t},g_{q,t}\rangle
\ge\frac2{2q+3}\|g_{q,t}\|^2.
$$
所以范数平方连续、严格递增，从 $1$ 趋于无穷。对每个 $\delta>0$，确有唯一 $t=t(q,\delta)>0$ 使
$$
\|g_{q,t}\|^2=1+\delta.
\tag{1.3}
$$
这只是有限块结论；并不自动给可和均值或全局源收敛。

## 2. 非零收敛实块乘积所强制的可和量

考虑互不交实际位块，大小为 $q_i\to\infty$，参数 $t_i\ge0$；主定理的 $\sum_iq_i^{-1}<\infty$ 自动保证这一点。纯源为
$g_i=g_{q_i,t_i}$，实际提升和正缩放的准确源为
$$
\widetilde g_i=g_i/(1-\varepsilon_i),
\qquad 0\le\varepsilon_i<1/2.
$$
如以真实 Walsh 提升后修正最小模，足够高的物理位可支付任意指定有限块误差；本节只使用准确源列，不把实际代数当作普通点乘。

假设
$$
g^{(n)}=\prod_{i\le n}\widetilde g_i\longrightarrow g
\quad\text{于 }H.
\tag{2.1}
$$
因为 $\|g_i\|\ge1$，所有块范数至少为 $1$，故 $g\ne0$。

记 $s_i=\|\widetilde g_i\|\ge1$、
$e_i=\widetilde g_i/s_i$。范数乘积
$\prod_{i\le n}s_i=\|g^{(n)}\|$ 收敛到有限非零值，所以
$\sum_i(s_i-1)<\infty$。归一化乘积 $\prod e_i$ 也收敛。

所有纯源及实际缩放均为实系数，故
$\beta_i=\langle e_i,\Omega\rangle$ 为实数，且最终为正并趋于 $1$。对归一化乘积，准确有
$$
\left\|\prod_{i\le n}e_i-\prod_{i\le m}e_i\right\|^2
=2\left(1-\prod_{m<i\le n}\beta_i\right).
$$
Cauchy 性给 $\sum_i(1-\beta_i)<\infty$。因此
$$
\sum_i|\langle\widetilde g_i,\Omega\rangle-1|<\infty,
\qquad
\sum_i\|\widetilde g_i-\Omega\|^2<\infty.
$$
又 $s_i\ge(1-\varepsilon_i)^{-1}$，故 $\sum_i\varepsilon_i<\infty$。撤去这些正标量后，得到
$$
\boxed{
\sum_i|\alpha_i-1|<\infty,\qquad
\sum_i\|g_i-\Omega\|^2<\infty,\qquad
\alpha_i=\langle g_i,\Omega\rangle.
}
\tag{2.2}
$$
这些是收敛实乘积的必要条件，并非仅从单项范数有界推出。

## 3. 前向真空亏损与参数平方预算

记 $R_i=R_{q_i,t_i}$，
$\mu_i=\langle R_i\Omega,\Omega\rangle$。纯有限块的反射共轭满足
$CT_q^*C=T_q$、$C\Omega=\Omega$，因此
$$
\|R_i^*\Omega-\Omega\|=\|R_i\Omega-\Omega\|.
$$
由 $R_ig_i=\Omega$ 及收缩性，
$$
\|R_i\Omega-\Omega\|\le\|g_i-\Omega\|.
$$
将
$\langle g_i,R_i^*\Omega\rangle=1$ 展开并取实部，得到
$$
0\le1-\operatorname{Re}\mu_i
\le|\alpha_i-1|+\|g_i-\Omega\|^2.
$$
故 (2.2) 给
$$
\boxed{\sum_i(1-\operatorname{Re}\mu_i)<\infty.}
\tag{3.1}
$$

### 3.1 真空圆周密度及边界相位

[收敛 Schur 逆源的零点稿](2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)
已完整证明
$$
d\sigma_q(\theta)=\frac{w_q(\theta)}{2\pi}d\theta,\qquad
w_q(\theta)=1+2\sum_{n=1}^q\frac{(q)_n}{(q+2)^n}\cos(n\theta)\ge0,
$$
$$
q^{-1/2}w_q(x/\sqrt q)
\longrightarrow\sqrt{2\pi}e^{-x^2/2}
\quad\text{在每个紧 }x\text{ 区间一致}.
\tag{3.2}
$$
特别在 $|\theta|\le q^{-1/2}$，充分大的 $q$ 有
$w_q(\theta)\ge c\sqrt q$，其中 $c>0$ 固定。

标量前向函数为
$$
b_t(z)=\exp\left[-t\frac{1-z}{1+z}\right].
$$
它在单位圆盘内有界于 $1$。除 $\theta=\pi$ 外，边界值为
$$
b_t(e^{i\theta})=\exp[i\,t\tan(\theta/2)].
\tag{3.3}
$$
真空矩积分仍然合法：先用 $b_t(\rho z)$、$\rho<1$，再令 $\rho\uparrow1$。有限幂零函数演算给左侧收敛；右侧由 $|b_t(\rho e^{i\theta})|\le1$、绝对连续 $\sigma_q$ 和控制收敛得到
$$
1-\operatorname{Re}\langle R_{q,t}\Omega,\Omega\rangle
=\int[1-\cos(t\tan(\theta/2))]\,d\sigma_q(\theta).
\tag{3.4}
$$

### 3.2 对全部参数的必要下界

令 $h=q^{-1/2}$、$A=t\tan(h/2)$。对 $q\ge4$，
相位导数 $t/(2\cos^2(\theta/2))$ 在 $|\theta|\le h$ 内不超过 $t$。故 $t>0$ 时
$$
\begin{aligned}
\int_{-h}^h[1-\cos(t\tan(\theta/2))]\,d\theta
&\ge\frac2t(A-\sin A)\\
&\ge\frac h{40}\min(t^2h^2,1).
\end{aligned}
$$
这里使用
$A-\sin A\ge(A/10)\min(A^2,1)$ 及 $A\ge th/2$；
前一初等不等式由 $A\le1$ 的 Taylor 界和
$A\ge1$ 时 $\sin A/A\le\sin1<9/10$ 得到。$t=0$ 时结论平凡。

结合 (3.2)—(3.4)，存在固定 $c_0>0$，使充分大的 $q$ 对所有 $t\ge0$ 有
$$
\boxed{
1-\operatorname{Re}\langle R_{q,t}\Omega,\Omega\rangle
\ge c_0\min(t^2/q,1).
}
\tag{3.5}
$$
因而 (3.1) 强制
$$
\boxed{\sum_i t_i^2/q_i<\infty.}
\tag{3.6}
$$
特别最终 $t_i\le\sqrt{q_i}$。这一步不是把零点计数套到零点自由函数上；使用的是其实际边界相位。

## 4. 逆源的正复合 Poisson 表示

固定 $q,t$。令 $N$ 为参数 $t$ 的 Poisson 随机变量；在 $N=n$ 条件下，令 $S$ 为 $n$ 个独立参数 $2$ 的指数随机变量之和，$N=0$ 时 $S=0$。则
$$
\mathbb E e^{uS}=\exp\left[\frac{tu}{2-u}\right]
\qquad(u<2).
\tag{4.1}
$$
又
$$
\mathbb E e^{J(I-T_q)}=2(I+T_q)^{-1}
$$
对单个参数 $2$ 的指数变量 $J$ 成立。复合 Poisson 公式因此给准确有限维恒等式
$$
e^{tF_q}
=\mathbb E e^{S(I-T_q)}.
$$
于是
$$
\boxed{
g_{q,t}=\mathbb E[e^S v_q(S)],
\qquad
v_q(s)=\bigotimes_{j=1}^q
\left[\left(1-\frac{s}{q+2}\right)\Omega_+
+\frac{s}{q+2}\chi_j\right].
}
\tag{4.2}
$$
每个有限块里 $v_q(s)$ 为有限次多项式，(4.1) 保证所有实际积分绝对收敛；没有形式指数或未付域的交换。

## 5. 整个 $\sqrt3$ 加权积分的统一上界

记 $r=\sqrt3$，$\|u\|_r=\|r^{\mathsf N}u\|$，$Q=q+2$。对 $x=s/Q$，
$$
\|r^{\mathsf N}v_q(s)\|^2=(1-2x+4x^2)^q.
$$
已在 R230 完整次数上界附录支付的全局初等不等式为
$$
1-2x+4x^2\le e^{29x/20}\quad(x\ge0),
$$
因此
$$
\|e^sv_q(s)\|_r\le e^{69s/40}.
\tag{5.1}
$$
另一方面，用 $\log y\le y-1$ 准确得到
$$
\boxed{
\|e^sv_q(s)\|_r
\le \exp[2(s+s^2)/q].
}
\tag{5.2}
$$

以下取 $q\ge2^{28}$、$0\le t\le\sqrt q$。令 $b=q/64$、
$F(s)=\exp[2(s+s^2)/q]$，则 $2t\le b$。在 $0\le s\le b$，
$F(s)\le e^{s/16}$、$F'(s)\le(2+4s)e^{s/16}/q$。

由 (4.1) 的 $u=1$，
$\mathbb P(S>s)\le e^{t-s}\le e^{-s/2}$ 对 $s\ge2t$ 成立。因此
$$
\begin{aligned}
\mathbb E[F(S)1_{\{S\le b\}}]
&\le F(2t)+\int_{2t}^bF'(s)\mathbb P(S>s)\,ds\\
&\le e^{(4t+8t^2)/q}+\frac{26}{q}.
\end{aligned}
\tag{5.3}
$$
常数可由
$\int_0^\infty(2+4s)e^{-7s/16}ds=1248/49<26$
直接核对。

大尾使用 (5.1) 和 (4.1) 的 $u=15/8$：
$$
\begin{aligned}
\mathbb E[e^{69S/40}1_{\{S>b\}}]
&\le e^{-(15/8-69/40)b}\mathbb E e^{15S/8}\\
&=\exp[-3q/1280+15t]\\
&\le e^{-3q/2560}.
\end{aligned}
\tag{5.4}
$$
最后由 $q\ge2^{28}$、$t\le\sqrt q$ 保证。

Minkowski、(4.2) 和 (5.3)—(5.4) 给
$$
\|g_{q,t}\|_r
\le e^{(4t+8t^2)/q}+26/q+e^{-3q/2560}.
$$
取对数时用 $\log(e^z+a)\le z+a$，得到
$$
\boxed{
\log\|g_{q,t}\|_{\sqrt3}^2
\le\frac{8t+16t^2+52}{q}
 +2e^{-3q/2560}.
}
\tag{5.5}
$$
该界控制整个块的加权范数，不只是某些逆方向。

## 6. 收敛实际逆源属于 $\mathcal H_{\sqrt3}$

现在进一步假设
$$
\sum_iq_i^{-1}<\infty.
\tag{6.1}
$$
这包括同一正常态使用的 $q_i=2^{4i}$，以及目前的快速分块构造。

由 (3.6)、$2t_i\le1+t_i^2$，(5.5) 的右侧可和。有限个初块各自有限维，不影响结论。第2节还给
$\sum_i\varepsilon_i<\infty$，所以正缩放成本
$-2\log(1-\varepsilon_i)$ 也可和。

由于实际源列仍准确是互不交普通块乘积，
$$
\sup_n\|g^{(n)}\|_{\sqrt3}^2
=\sup_n\prod_{i\le n}
 \frac{\|g_{q_i,t_i}\|_{\sqrt3}^2}{(1-\varepsilon_i)^2}
<\infty.
$$
原 $H$ 收敛给逐 Walsh 系数收敛，Fatou 得
$$
\boxed{g\in\mathcal H_{\sqrt3}.}
\tag{6.2}
$$
所有 actual/pure 使用都停在已证准确真空列；没有声称指数块在实际提升后仍满足未经验证的纯有理恒等式。

若这些实际块产生 $P$、$Pg=1$ 和同组强单位，则 R244 与 R255 进一步给真实逆
$$
\|Gu\|\le C_g\|u\|_{\sqrt3},\qquad
H_{\log\sqrt3}\subseteq\operatorname{Ran}P.
\tag{6.3}
$$
完整一次层特别有界。因此其任何聚合表示都要求一次正常矩平方可和。

既有固定
$f=1+\sum_i2^{-i-2}\chi_{B_i}$、$|B_i|=2^{4i}$
的实际一次矩不在 $\ell^2$。所以本族中凡逆源确实收敛的 $P$，都不能为这个同一个 $\phi_f$ 满足 R244 聚合界；它已经在一次层失败。

## 7. 原一次 Gram 调幅预算在该族中甚至不收敛

可进一步准确检验“先把范数调成 $1+\delta$”的方案。

无权情形有
$$
\log(1-2x+2x^2)+2x\le\frac83x^3\qquad(x\ge0).
$$
证明只须求导：左侧导数为
$4x^2/(1-2x+2x^2)\le8x^2$，再从零积分。因此
$$
\|e^sv_q(s)\|
\le\exp[2s/q+(4/3)s^3/q^2].
$$
在 $s\le q/64$ 上重复第5节分段法，导数为
$(2/q+4s^2/q^2)$ 乘原指数，小尾积分至多
$$
\exp[4t/q+(32/3)t^3/q^2]+8/q.
$$
大尾使用无权全局界 $\|v_q(s)\|\le e^{s/2}$，
再取 (4.1) 的 $u=7/4$，得到
$$
\mathbb E[e^{3S/2}1_{\{S>q/64\}}]
\le e^{-q/256+7t}\le e^{-q/512}.
$$
所以对 $q\ge2^{28}$、$0\le t\le\sqrt q$，
$$
\|g_{q,t}\|
\le e^{4t/q+(32/3)t^3/q^2}+8/q+e^{-q/512}.
$$
右侧指数至多 $44/(3\sqrt q)$，从而有安全的统一界
$$
\boxed{
\|g_{q,t}\|^2\le1+\frac{100}{\sqrt q}
\quad(0\le t\le\sqrt q).
}
\tag{7.1}
$$

若沿原调块预算
$$
q_i=2^{4i},\qquad \delta_i=\delta_*2^{-i},
\qquad \delta_*>0,
$$
用第1节唯一参数强制
$\|g_{q_i,t_i}\|^2=1+\delta_i$，则
$\delta_i\sqrt{q_i}=\delta_*2^i\to\infty$。由 (7.1)，最终必有
$t_i>\sqrt{q_i}$。这直接违反第3节从实际逆源收敛推出的
$\sum_i t_i^2/q_i<\infty$。

所以在这个零点自由族里，原来可和的范数增量并不支付可和均值：上述特定调幅方案的逆源乘积不能收敛。若改用其他预算使逆源真正收敛，则第6节又使它回到
$\mathcal H_{\sqrt3}$，仍不能修复同一正常态的一次矩障碍。

这不否定无真空原像前向族、其他非块结构或见证专属正则器。本稿未给一般正常湮灭者的配对，没有给慢符号有界分母，普通 ISP 保持开放。
