# 复近圆扇区的逆源：相位无关的平方预算与真实全列障碍

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065。

**状态：已证明的中间结论。** 本稿把实 Blaschke 近圆逆源的结论扩到
$$
\operatorname{Re}a\ge\frac34,\qquad |a|<1.
$$
对应前向零点位于负单位点附近。允许每块任意有限个因子、任意复参数及整体单位相位。若实际逆真空块乘积确实收敛，并且 $\sum_iq_i^{-1}<\infty$，则这个扇区的源仍属于 $\mathcal H_{\sqrt3}$。

证明的两个新步骤分别是：用相位不变的真空方差，而非实均值亏损，得到有效参数的平方可和；用正 Taylor 主控及整个函数的绝对系数和，处理复参数的加权范数。没有把复积分密度当作正概率测度。

最后与紧内复分母消去合并，排除同一固定分块、同一非湮灭正常态下，参数位于
$$
\{0<|a|\le3/4\}\ \cup\
\{|a|<1,\ \operatorname{Re}a\ge3/4\}
$$
的任意阶成功逆源族满足 R244 的全列聚合界。一般逼圆复相位、非块结构、无真空原像族和真正湮灭者专属配对仍未解决。

## 1. 准确有限块与实际构造前提

记
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad
Q=q+2,\qquad Z_q=I-T_q,\qquad
\Omega=\Omega_+^{\otimes q}.
\tag{1.1}
$$
$\|T_q\|<1$、$T_q^{q+1}=0$。纯反射共轭 $C$ 满足
$$
CT_q^*C=T_q,\qquad C\Omega=\Omega.
\tag{1.2}
$$

对 $0<|a|<1$，选在标量点 $1$ 归一的 Blaschke 因子
$$
\beta_a(z)=
\frac{1+\overline a}{1+a}\frac{z+a}{1+\overline a z},
\qquad \beta_a(1)=1.
\tag{1.3}
$$
单位前因子不改变收缩性。$\beta_a(T_q)$ 为可逆收缩，其逆为
$$
U_a(T_q)=
\frac{1+a}{1+\overline a}
(I+\overline aT_q)(aI+T_q)^{-1}.
\tag{1.4}
$$
逆存在因为 $a\ne0$、$T_q$ 幂零。收缩性也可直接由
$
(I+aT_q^*)(I+\overline aT_q)-(\overline aI+T_q^*)(aI+T_q)
=(1-|a|^2)(I-T_q^*T_q)\ge0
$
在两侧乘准确分母的逆得到。

第 $i$ 块允许任意有限参数集合，并允许整体单位相位，令
$$
R_i=\xi_i\prod_\ell\beta_{a_{i\ell}}(T_{q_i}),
\quad |\xi_i|=1,\qquad
U_i=R_i^{-1},\qquad g_i=U_i\Omega.
\tag{1.5}
$$
$R_i$ 收缩，$U_i$ 扩张，故 $\|g_i\|\ge1$。以下 $q_i\to\infty$。

与既有实际构造相同，假设已付清真实 Walsh 提升和正缩放：
$$
\widetilde U_i=\frac{X_{g_i}}{1-\varepsilon_i},
\qquad
\widetilde g_i=\frac{g_i}{1-\varepsilon_i},
\qquad 0\le\varepsilon_i<1/2,
\tag{1.6}
$$
并有准确的互不交源乘积收敛
$$
g^{(n)}=\prod_{i\le n}\widetilde g_i\longrightarrow g
\quad\text{于原 }H.
\tag{1.7}
$$
凡要使用 R244 最小逆，还另假设实际收缩逆积确已给出 $P$、
$Pg=1$ 及同一组一致有界强单位。于是
$$
G=P^{-1}=X_g,\qquad Gu=X_ug
\tag{1.8}
$$
在全部有限 Walsh 柱上准确成立，且这些柱为实际图核心。

在后面的混合分母定理中，使用已验证的完整 carry 预算
$$
16q_i5^{q_i}\max(1,\|g_i\|)
 \eta_{\min B_i}\le\varepsilon_i.
\tag{1.9}
$$
本稿不声称任意参数自动给 (1.6)--(1.9)。

## 2. 复源乘积强制相位无关的真空方差可和

复源不能照搬实情形的
$\sum_i|\langle g_i,\Omega\rangle-1|<\infty$；
单个块的单位相位可以只条件收敛。下面的论证始终保留这个区别。

令
$$
n_i=\|g_i\|\ge1,\qquad
s_i=\|\widetilde g_i\|=\frac{n_i}{1-\varepsilon_i},
\qquad e_i=g_i/n_i.
$$
由 (1.7)，$\prod_{i\le n}s_i$ 收敛到有限且至少为 $1$ 的数。因此
$$
\sum_i(s_i^2-1)<\infty,\qquad
\sum_i(n_i^2-1)<\infty,\qquad
\sum_i\varepsilon_i<\infty.
\tag{2.1}
$$
第一个结论由收敛的正乘积取对数得到；后两个由
$s_i\ge n_i$、$s_i\ge(1-\varepsilon_i)^{-1}$ 得到。

归一化的张量乘积 $\prod_{i\le n}e_i$ 也在 $H$ 中收敛。
写
$$
\beta_i=\langle e_i,\Omega\rangle,\qquad |\beta_i|\le1.
$$
两个归一化乘积的尾内积准确是
$\prod_{m<i\le n}\beta_i$（或其共轭，取模后相同）。
Cauchy 性使这些尾乘积的模一致趋于 $1$，所以
$$
\sum_i(1-|\beta_i|)<\infty.
\tag{2.2}
$$
严格地，对充分大的 $m$，全部 $n>m$ 的乘积模大于 $1/2$；
取负对数并令 $n\to\infty$ 即得尾部可和。

置
$$
\alpha_i=\langle g_i,\Omega\rangle,\qquad
h_i=g_i-\alpha_i\Omega,\qquad
d_i=n_i^2-1.
$$
$n_i$ 一致有界且
$\|h_i\|^2=n_i^2(1-|\beta_i|^2)$，由 (2.1)--(2.2)，
$$
\boxed{\sum_i d_i<\infty,\qquad
\sum_i\|h_i\|^2<\infty.}
\tag{2.3}
$$

令 $x_i=R_i\Omega$、$\mu_i=\langle x_i,\Omega\rangle$。
有限块函数演算保 $C$ 对称：
$R_i=CR_i^*C$，即使有复系数和单位相位仍成立。
由于 $R_ig_i=\Omega$，
$$
\langle x_i,Cg_i\rangle
=\langle\Omega,R_i^*Cg_i\rangle=1.
$$
故有正交分解
$$
x_i=\frac{Cg_i}{n_i^2}+z_i,\qquad
z_i\perp Cg_i,\qquad
\|z_i\|^2\le1-\frac1{n_i^2}=\frac{d_i}{n_i^2}.
\tag{2.4}
$$
这里使用 $\|x_i\|\le1$。同时 $\|x_i\|^2\ge n_i^{-2}$。
对真空正交补作投影，得到
$$
\begin{aligned}
1-|\mu_i|^2
&=1-\|x_i\|^2+\|P_{\Omega^\perp}x_i\|^2\\
&\le\frac{d_i}{n_i^2}
 +\frac{2\|h_i\|^2}{n_i^4}
 +\frac{2d_i}{n_i^2}\\
&\le3d_i+2\|h_i\|^2.
\end{aligned}
$$
因此
$$
\boxed{\sum_i(1-|\mu_i|^2)<\infty.}
\tag{2.5}
$$
这是本稿需要的相位不变结论。没有主张复均值的相位绝对可和。

## 3. 真空密度、双积分与全部大小参数的平方预算

### 3.1 准确的圆周概率测度

纯块真空矩为
$$
c_{q,n}=\langle T_q^n\Omega,\Omega\rangle
=\frac{(q)_n}{(q+2)^n}\quad(0\le n\le q),
\qquad c_{q,n}=0\quad(n>q).
$$
令
$$
w_q(\theta)=1+2\sum_{n=1}^q c_{q,n}\cos(n\theta),
\qquad d\sigma_q(\theta)=\frac{w_q(\theta)}{2\pi}\,d\theta.
\tag{3.1}
$$
严格收缩的 Cayley 正性给 $w_q\ge0$，常数 Fourier 系数给总质量 $1$。
有限块 Taylor 演算给
$$
\langle b(T_q)\Omega,\Omega\rangle
=\int b(e^{i\theta})\,d\sigma_q(\theta)
\tag{3.2}
$$
对每个在闭单位圆盘邻域解析的 $b$ 成立。

[Schur 零点稿](2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md) 已完整给出局部一致极限
$$
q^{-1/2}w_q(x/\sqrt q)
\longrightarrow\sqrt{2\pi}e^{-x^2/2}.
\tag{3.3}
$$
其直接证明只用
$\log c_{q,n}=-n^2/(2q)+O_L(q^{-1/2})$ 对 $n\le L\sqrt q$
一致成立，以及 $c_{q,n}\le e^{-n^2/(3q)}$ 的全局主控，
把 Fourier 和写为 Riemann 和。
所以在 $h=q^{-1/2}$、$|\theta|\le h$ 上，
充分大 $q$ 有
$$
\frac{w_q(\theta)}{2\pi}\ge\frac{c_*}{h},
\qquad c_*>0\text{ 为绝对常数}.
\tag{3.4}
$$

### 3.2 相位导数的比较

记
$$
t_a=\frac{1-|a|^2}{|1+a|^2}>0.
\tag{3.5}
$$
$\beta_a(e^{i\theta})$ 的连续相位导数准确为
$$
\frac{1-|a|^2}{|e^{i\theta}+a|^2}
=t_a\frac{|1+a|^2}{|e^{i\theta}+a|^2}.
\tag{3.6}
$$
若 $\operatorname{Re}a\ge3/4$，则 $|1+a|\ge7/4$。
在 $|\theta|\le h\le1/2$ 上，
$|e^{i\theta}-1|\le h$，因此
$$
\frac12t_a\le
\frac{1-|a|^2}{|e^{i\theta}+a|^2}
\le2t_a.
$$
对任意有限产品，令 $\tau=\sum_\ell t_{a_\ell}$，
其连续相位 $\psi$（忽略常数单位相位）满足
$$
\boxed{\tau/2\le\psi'(\theta)\le2\tau
\qquad(|\theta|\le h).}
\tag{3.7}
$$

### 3.3 双积分付清大参数，而非只作局部 Taylor

因 $b$ 为有限内函数，$|b(e^{i\theta})|=1$。
(3.2) 给准确方差恒等式
$$
1-\left|\langle b(T_q)\Omega,\Omega\rangle\right|^2
=\iint[1-\cos(\psi(\theta)-\psi(\varphi))]
\,d\sigma_q(\theta)d\sigma_q(\varphi).
\tag{3.8}
$$
整体单位相位在这里准确消掉。

设 $\tau>0$。由 (3.7)，
$I=\psi([-h,h])$ 的长度 $L$ 满足
$\tau h\le L\le4\tau h$，且相位变量替换的 Jacobian 至少为 $(2\tau)^{-1}$。
(3.4) 因此给
$$
1-|\mu|^2
\ge\frac{c_*^2}{4\tau^2h^2}
\int_I\int_I[1-\cos(u-v)]\,du\,dv
=\frac{c_*^2}{4\tau^2h^2}
\left[L^2-4\sin^2(L/2)\right].
\tag{3.9}
$$
函数 $F(L)=L^2-4\sin^2(L/2)$ 单调递增，因为
$F'(L)=2(L-\sin L)\ge0$。
当 $0\le L\le1$ 时，直接用 $1-\cos x\ge x^2/4$ 得
$F(L)\ge L^4/24$。
当 $1\le L\le4$ 时，$F(L)\ge F(1)\ge1/24$；
当 $L\ge4$ 时，$F(L)\ge L^2-4\ge3L^2/4$。
由此，对全部 $A\ge0$，
$$
\frac{F(A)}{A^2}\ge\frac1{384}\min(A^2,1)
$$
（在 $A=0$ 按连续极限理解）。
代入 $A=\tau h$，得到绝对 $c_0>0$：
$$
\boxed{1-|\mu|^2\ge c_0\min(\tau^2/q,1).}
\tag{3.10}
$$
$\tau=0$ 时也成立。

结合 (2.5)，得到
$$
\boxed{\sum_i\tau_i^2/q_i<\infty.}
\tag{3.11}
$$
先由 (3.10) 排除无穷多个 $\tau_i^2/q_i\ge1$，
再在其余项上直接求和即可。

同一论证只需要 $c\tau\le\psi'\le C\tau$ 的两个固定正比较常数；
因此下文混合族改变这些常数不改变平方可和结论。

## 4. 复逆函数的正 Taylor 主控

置
$$
A_a=\frac1{1+a},\qquad
B_a=\frac{\overline a}{1+\overline a}.
$$
注意 $A_a,B_a$ 不是原 odometer 算子 $A$。
从 (1.4) 准确得到
$$
U_a(T_q)=\frac{I-B_aZ_q}{I-A_aZ_q},
$$
$$
A_a-B_a=t_a>0,\qquad
|A_a|,|B_a|\le\frac47
\quad(\operatorname{Re}a\ge3/4,\ |a|<1).
\tag{4.1}
$$

先去掉一个块的整体单位相位，它不影响任何范数。
写该块的标量逆为
$$
h(z)=\prod_\ell\frac{1-B_{a_\ell}z}{1-A_{a_\ell}z},
\qquad h(0)=1.
$$
在 $|z|<7/4$ 中取零点的对数分支。由
$$
\frac{|A_a^n-B_a^n|}{n}
\le t_a(4/7)^{n-1}
$$
得
$$
\left|[z^n]\log h(z)\right|
\le\tau(4/7)^{n-1}.
\tag{4.2}
$$
指数级数的逐系数三角不等式遂给
$$
|[z^n]h(z)|\le[z^n]M_\tau(z),
\qquad
M_\tau(z)=\exp\left(\frac{\tau z}{1-4z/7}\right).
\tag{4.3}
$$

右侧恰是一个真正非负随机变量 $S$ 的矩母函数：
取 $N\sim\operatorname{Poi}(7\tau/4)$，
令 $S$ 为 $N$ 个独立 $\operatorname{Exp}(7/4)$ 跃迁之和。则
$$
M_\tau(z)=\mathbb E e^{zS},\qquad
\mathbb E S=\tau,\qquad
[z^n]M_\tau=\frac{\mathbb E S^n}{n!}.
\tag{4.4}
$$
这个概率只用于主控绝对 Taylor 系数；
一般复 $h$ 本身没有被写成同一个正积分。

由于 $Z_q=I-T_q$ 且 $T_q^{q+1}=0$，
$\|Z_q^n\|$ 至多按 $n$ 的固定 $q$ 次多项式增长。
$h$ 的 Taylor 半径至少为 $7/4>1$，
所以 $h(Z_q)$ 的 Taylor 级数确在有限块算子范数中绝对收敛。
不要求 $\|Z_q\|<7/4$。

## 5. 整个函数的全复方向范数和绝对 Taylor 和

记 $r=\sqrt3$，$W_q=r^{\mathsf N}$。
考虑有限块整个函数
$$
\mathcal F_q(z)=W_qe^{zZ_q}\Omega.
$$
准确 tensor 公式为
$$
e^{zZ_q}\Omega
=e^z\bigotimes_{j=1}^q
\left[\left(1-\frac zQ\right)\Omega_+
+\frac zQ\chi_j\right].
\tag{5.1}
$$

### 5.1 全复方向的严格指数余量

先证明用于全尾的初等界
$$
1-2x+4x^2\le e^{29x/20}\qquad(x\ge0).
\tag{5.2}
$$
令 $\alpha=29/20$、$f(x)=e^{\alpha x}-1+2x-4x^2$。
$f'$ 的全局最小值出现在
$x_0=\alpha^{-1}\log(8/\alpha^2)$，为
$$
8/\alpha+2-(8/\alpha)\log(8/\alpha^2).
$$
而
$$
e^{109/80}
\ge\sum_{k=0}^4\frac{(109/80)^k}{k!}
>\frac{3200}{841}=\frac8{\alpha^2},
$$
故 $\log(8/\alpha^2)<109/80=1+\alpha/4$，
从而 $f'>0$。结合 $f(0)=0$，得到 (5.2)。

写 $z=Qxe^{i\theta}$、$c=\cos\theta$。
由 (5.1)，
$$
\log\|\mathcal F_q(z)\|
=q\left[cx+\tfrac12\log(1-2cx+4x^2)\right]+2cx.
$$
固定 $x$ 时，中括号对 $c$ 的导数为
$$
\frac{2x^2(2x-c)}{1-2cx+4x^2}.
$$
若 $x\le1/2$，最大值在 $c=2x$，等于 $2x^2\le x$；
若 $x\ge1/2$，最大值在 $c=1$，由 (5.2) 不超过 $(69/40)x$。
因此对全部复 $z$、全部 $q\ge1$，
$$
\boxed{\|\mathcal F_q(z)\|\le e^{\kappa_0|z|},
\qquad \kappa_0=\frac{69}{40}<\frac74.}
\tag{5.3}
$$

### 5.2 真空与非真空部分的小圆估计

写
$$
\mathcal F_q(z)=F_{q,0}(z)\Omega+F_{q,\perp}(z),
\qquad F_{q,0}(z)=e^z(1-z/Q)^q.
$$
令 $R=|z|$、$u=\operatorname{Re}z$。准确平方差和
$A^q-B^q\le q(A-B)A^{q-1}$ 给
$$
\|F_{q,\perp}(z)\|
\le\frac{\sqrt3R}{\sqrt q}
 \exp\left(\frac{3R+2R^2}{q}\right).
\tag{5.4}
$$
具体使用
$A=1-2u/Q+4R^2/Q^2$、
$B=1-2u/Q+R^2/Q^2$、
$A-B=3R^2/Q^2$，随后用 $\log A\le A-1$。
因此 (5.4) 适用于所有 $z$，并未除以可能很小的真空系数。

若 $R\le Q/2$，零点分支的对数满足
$$
|z+q\log(1-z/Q)|\le\frac{2R+R^2}{q}.
$$
于是
$$
|F_{q,0}(z)-1|
\le\frac{2R+R^2}{q}
 \exp\left(\frac{2R+R^2}{q}\right).
\tag{5.5}
$$

令 $H_{q,\perp}(s)$ 为 $F_{q,\perp}$ 的 Taylor 系数范数绝对和，
令 $H_{q,0}(s)$ 为 $F_{q,0}-1$ 的 Taylor 系数绝对和，
均在非负实变量 $s$ 上求值。
在半径 $2s$ 上用 Cauchy，并求和
$\sum_{n\ge1}2^{-n}=1$，得到
$$
\boxed{
H_{q,\perp}(s)\le
\frac{4s}{\sqrt q}
 \exp\left(\frac{6s+8s^2}{q}\right),
}
\tag{5.6}
$$
$$
\boxed{
H_{q,0}(s)\le
\frac{4(s+s^2)}q
 \exp\left(\frac{4(s+s^2)}q\right)
\qquad(0\le s\le Q/4).
}
\tag{5.7}
$$

全尾改用半径 $(1+1/512)s$。
由 (5.3) 和几何和 $\sum_{n\ge1}(1+1/512)^{-n}=512$，
$$
H_{q,\perp}(s)\le512e^{\kappa_1s},\qquad
H_{q,0}(s)\le1024e^{\kappa_1s},
\tag{5.8}
$$
其中
$$
\kappa_1=\frac{69}{40}\left(1+\frac1{512}\right)
=\frac{35397}{20480}
<\frac{139}{80}<\frac74.
\tag{5.9}
$$
(5.8) 对全部 $s\ge0$ 成立。

## 6. 全部概率尾与统一整块加权界

去掉整体单位相位后，记 $g_q=h(Z_q)\Omega$、
$\gamma_q=\langle g_q,\Omega\rangle$。
由 (4.3)--(4.4) 的逐系数主控和非负 Tonelli，
$$
|\gamma_q-1|\le\mathbb EH_{q,0}(S),\qquad
\|P_{\Omega^\perp}W_qg_q\|
\le\mathbb EH_{q,\perp}(S).
\tag{6.1}
$$
下面的全尾界同时验证这些绝对求和和积分合法。

取 $q\ge2^{52}$、$0\le\tau\le\sqrt q$，令 $b=q/1024$。
由 (4.4) 在 $u=1$ 的矩母函数，
$$
\mathbb P(S>s)\le e^{(7/3)\tau-s}
\le e^{-s/2}\qquad(s\ge5\tau).
\tag{6.2}
$$
此时 $5\tau\le b$。

定义 (5.6)--(5.7) 的右侧为 $G_\perp(s),G_0(s)$。
在 $0\le s\le b$，指数均不超过 $e^{s/64}$。
两者递增。对任一这样的递增函数，分布积分给
$$
\mathbb E[G(S)1_{\{S\le b\}}]
\le G(5\tau)+\int_{5\tau}^bG'(s)\mathbb P(S>s)\,ds.
\tag{6.3}
$$
在 $s=5\tau$ 处，因 $\tau^2/q\le1$，
$$
G_\perp(5\tau)\le C\tau/\sqrt q,\qquad
G_0(5\tau)\le C(\tau+\tau^2)/q
$$
以某个绝对 $C$ 成立。
而其导数在 $[0,b]$ 分别由
$$
\frac C{\sqrt q}(1+s+s^2)e^{s/64},
\qquad
\frac Cq(1+s+s^2)e^{s/64}
$$
主控。结合 (6.2)，导数积分由
$\int_0^\infty(1+s+s^2)e^{-31s/64}ds<\infty$
支付。因此
$$
\mathbb E[H_{q,\perp}(S)1_{\{S\le b\}}]
\le\frac{C(1+\tau)}{\sqrt q},
$$
$$
\mathbb E[H_{q,0}(S)1_{\{S\le b\}}]
\le\frac{C(1+\tau^2)}q.
\tag{6.4}
$$
这里以及下文 $C$ 只表示固定绝对常数，不依赖因子数、参数或块大小。

大尾取 $u_*=139/80$。由 (4.4)，
$$
\log\mathbb E e^{u_*S}
=\frac{u_*\tau}{1-4u_*/7}
=\frac{973}{4}\tau.
$$
所以 (5.8)--(5.9) 给
$$
\mathbb E[H_{q,\bullet}(S)1_{\{S>b\}}]
\le1024\exp\left[-\frac{187}{5\cdot2^{22}}q
+\frac{973}{4}\tau\right]
\le1024e^{-cq},
\tag{6.5}
$$
$$
c=\frac{187}{5\cdot2^{23}}>0.
$$
最后一步由 $q\ge2^{52}$、$\tau\le\sqrt q$ 支付：
$c\sqrt q\ge(187/5)2^3=1496/5>973/4$。

(6.1)、(6.4)--(6.5) 遂给
$$
|\gamma_q-1|\le C(1+\tau^2)/q+Ce^{-cq},
$$
$$
\|P_{\Omega^\perp}W_qg_q\|
\le C(1+\tau)/\sqrt q+Ce^{-cq}.
$$
真空与非真空部分正交，且 $(1+\tau^2)/q\le2$。
吸收平方项，得到整块统一估计
$$
\boxed{
\|g_q\|_{\sqrt3}^2
\le1+\frac{C(1+\tau^2)}q+Ce^{-cq}
\qquad(q\ge2^{52},\ \tau\le\sqrt q).
}
\tag{6.6}
$$
原块整体单位相位不改变 (6.6)。

## 7. 复扇区实际逆源属于 $\mathcal H_{\sqrt3}$

假设全部参数满足 $\operatorname{Re}a\ge3/4$、$|a|<1$，
实际源 (1.7) 收敛，且
$$
\sum_iq_i^{-1}<\infty.
\tag{7.1}
$$
第3节给 $\sum_i\tau_i^2/q_i<\infty$，
因此最终 $\tau_i\le\sqrt{q_i}$。
有限个初块分别有限维，不影响加权结论。
(6.6)、$\log(1+x)\le x$ 和
$\sum_i\varepsilon_i<\infty$ 给
$$
\sup_n\|g^{(n)}\|_{\sqrt3}^2
=
\sup_n\prod_{i\le n}
\frac{\|g_i\|_{\sqrt3}^2}{(1-\varepsilon_i)^2}<\infty.
$$
这里 $\sum_ie^{-cq_i}<\infty$ 由 (7.1) 立即推出。
原 $H$ 收敛给逐 Walsh 系数收敛，Fatou 得
$$
\boxed{g\in\mathcal H_{\sqrt3}.}
\tag{7.2}
$$

若还满足 (1.8)，R255 的实际双输入端点和最小闭图给
$$
\|Gu\|\le C_g\|u\|_{\sqrt3}
$$
对有限 Walsh $u$ 成立，并由闭性扩到整个 $\mathcal H_{\sqrt3}$。
特别，完整一次层上的 $G$ 有界，R244 聚合表示必要求实际一次矩为 $\ell^2$。

对既有固定
$$
q_i=2^{4i},\qquad
f=1+\sum_i2^{-i-2}\chi_{B_i},
\qquad \|f\|^2=49/48,
\tag{7.3}
$$
纯一次矩在 $j\in B_i$ 上是 $2c_i^2$，
$c_i=2^{-i-2}$。
其平方和每块贡献
$4q_ic_i^4=1/64$，所以发散。
实际 $V_j-(I-2E_j)$ 的误差至多 $8\eta_j$，
对 $\phi_f$ 的矩误差为一个 $\ell^2$ 序列。
故实际一次矩也不在 $\ell^2$。
因此本扇区的所有成功逆源族仍在一次聚合层失败。

## 8. 紧内复参数与复近圆扇区的任意混合

现允许每个参数属于
$$
\mathcal R=
\{a:0<|a|\le3/4\}
\cup
\{a:|a|<1,\ \operatorname{Re}a\ge3/4\}.
\tag{8.1}
$$
保持 (1.6)--(1.9) 的实际前提和 (7.3) 的同一固定分块、同一 $f$。

所有 $a\in\mathcal R$ 都有 $|1+a|\ge1/4$。
在 $h=q^{-1/2}\le1/8$ 上，
$|e^{i\theta}+a|/|1+a|$ 在 $[1/2,3/2]$ 内。
所以 (3.6) 给总相位导数
$$
\tau/4\le\psi'\le4\tau,\qquad
\tau=\sum_\ell t_{a_\ell}.
$$
第3节的一般比较常数版本因而仍给
$$
\sum_i\tau_i^2/q_i<\infty.
\tag{8.2}
$$

令 $r_i$ 为 $|a_{i\ell}|\le3/4$ 的因子数；
边界重叠因子任选归入紧内部分。
每个紧内因子有 $t_a\ge1/7$，故
$$
r_i\le7\tau_i,\qquad r_i=o(\sqrt{q_i}).
\tag{8.3}
$$
其余因子的有效参数不超过 $\tau_i$。
由 (6.6)，对应纯近圆源 $g_i^{\rm near}$ 满足
$$
\sup_{i\text{ 足够大}}\|g_i^{\rm near}\|_{\sqrt3}<\infty.
\tag{8.4}
$$
这里不需要近圆子积本身已生成另一实际正则器。

令
$$
D_i(z)=\prod_{\rm in}(z+a_{i\ell}),\qquad
b_i=\prod_{\rm in}(1+|a_{i\ell}|),\qquad k_i=r_i+2,
$$
并定义真正有限 Walsh 列
$$
\boxed{
u_i=\frac{D_i(T_i)v_{q_i,k_i}}{b_i3^{k_i/2}},
\qquad
v_{q,k}=\binom qk^{-1/2}\sum_{|F|=k}\chi_F.
}
\tag{8.5}
$$
$\|u_i\|\le1$，次数至多 $2r_i+2=o(\sqrt{q_i})$。

在纯有限代数中紧内分母准确消去。
余下紧内分子的系数绝对和不超过 $b_i$，单位相位无影响，
故它除以 $b_i$ 的算子范数不超过 $1$。
R255 的纯双输入端点与 (8.4) 给
$$
\|U_i^{\rm near}v_{q_i,k_i}\|
=\|X_{v_{q_i,k_i}}^0g_i^{\rm near}\|
\le3^{k_i/2}\|g_i^{\rm near}\|_{\sqrt3}.
$$
因此
$$
\sup_{i\text{ 足够大}}\|U_iu_i\|<\infty.
\tag{8.6}
$$

准确源分块与 $\|g_i\|\ge1$ 给
$\|X_{u_i}^0g\|\le C\|g\|$。
实际有限列的完整误差（设 $s_i=2r_i+2$）满足
$$
\Delta_i:=\|X_{u_i}-X_{u_i}^0\|
\le8s_i3^{s_i}\sqrt{s_i+1}\,q_i^{s_i/2}\eta_{\min B_i}.
\tag{8.7}
$$
非 carry 部分的对数为 $o(q_i)$，由 (1.9) 已付预算可知
$\Delta_i\to0$。
(1.8) 遂给同一个实际最小逆的统一界
$$
\boxed{\sup_i\|Gu_i\|<\infty}
\tag{8.8}
$$
（略去有限初块，或把它们另行吸入常数）。

## 9. 同一正常态的实际矩仍发散

[复分母消去稿](2026-11-13-complex-rational-block-denominator-cancellation-and-growing-order-obstruction-normal-next.md)
的精确生成式是
$$
2^{-k}\langle e^{t(T+I)}D_F^0\chi_B,\chi_B\rangle
=e^t(1-t/Q)^{q-k}(1-t/(2Q))^k.
$$
它付清全部重复位，并给相对于 $D_i(-1)$ 的误差
$$
E_i\le
\exp[(18r_i^2+12r_i)/q_i]-1\longrightarrow0.
\tag{9.1}
$$
又 $|D_i(-1)|/b_i\ge7^{-r_i}$。
选单位相位 $\omega_i$ 使 $\omega_iD_i(-1)>0$。
对 (8.5)，纯完整块矩加上至多 $\lambda=49/48$ 的真空项给
$$
\operatorname{Re}\phi_f(X_{\omega_i u_i}^0)
\ge\frac12 A_i-\lambda
$$
对充分大 $i$ 成立，其中
$$
A_i=
\frac1{16\sqrt{q_i}}
\left(\frac2{\sqrt3}\right)^{r_i+2}
\sqrt{\binom{q_i}{r_i+2}}\,7^{-r_i}.
\tag{9.2}
$$
输入次数小于 $q_i$，因此不同完整块与真空之间的纯交叉矩为零。

若 $r_i\ge1$，由 $r_i+2\le\sqrt{q_i}$ 及
$\binom qk\ge(q/k)^k$，
$$
A_i\ge\frac1{12}
\left(\frac{2q_i^{1/4}}{7\sqrt3}\right)^{r_i}
\ge\frac{q_i^{1/4}}{42\sqrt3}\to\infty.
$$
$r_i=0$ 时，
$A_i=(1/12)\sqrt{(q_i-1)/2}\to\infty$。
实际矩误差至多 $\lambda\Delta_i\to0$。
结合 (8.8)，
$$
\boxed{
\frac{|\phi_f(X_{\omega_i u_i})|}
{\|G(\omega_i u_i)\|}
\longrightarrow\infty.
}
\tag{9.3}
$$

这证明任意阶的混合区域 (8.1) 成功逆源族都不能为同一个
$\phi_f$ 提供 R244 全列聚合表示。
没有为不同列更换正常态或物理分块。

### 有限个完整逆源的组合

同一分块上有限个已经成功的此类完整源 $g^{(\nu)}$，
若其线性组合 $g=\sum_{\nu=1}^Kz_\nu g^{(\nu)}$
又确为某个合格 $P$ 的 $P^{-1}1$，也有同样障碍。
取各分支紧内分母的共同乘积，令总阶数为 $r_i$；
由每个分支的 (8.3)，仍有 $r_i=o(\sqrt{q_i})$。
对第 $\nu$ 分支，分母消去后多出的其他分支分母，
与本支紧内分子一起的系数绝对和不超过共同 $b_i$。
其近圆源仍满足 (8.4)，故同一个 (8.5) 的逆像范数
由有限个分支常数的三角和控制。
矩下界只用共同分母，所以 (9.3) 不变。

这里组合的是完整逆源；没有将正则器之和的逆误认作逆源之和。
块内任意非乘积有理组合也没有自动满足本文的前向内函数、
收敛源或分子预算条件。

## 10. 尚未覆盖的范围

参数区域 (8.1) 仍不包含所有接近单位圆的复参数。
例如某些靠近其他圆周弧的因子没有本文的统一相位导数比较，
或没有 $7/4$ 大于整个函数指数型的 Taylor 余量。
不能仅凭系数形式把它们移入本文结论。

固定 $f$ 连续非负，早已被已证正锥结果排除为慢主理想湮灭者。
本稿的作用是精确限制正则器构造的适用范围，
不是排除一般正正常见证。
不同物理分块、无真空原像的前向族、
真正湮灭矩所选的特殊正则器和慢符号有界分母仍开放。
普通 Hilbert ISP 未完成。

完整依赖：
- [R255 真实双输入端点与最小闭图](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)；
- [R244 聚合逆图](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)；
- [Schur 真空密度与紧内零点](2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)；
- [复有理分母消去](2026-11-13-complex-rational-block-denominator-cancellation-and-growing-order-obstruction-normal-next.md)；
- [实近圆和全部实混合源](2026-11-13-real-boundary-blaschke-moments-and-all-real-mixed-obstruction-normal-next.md)。
