# 复参数 gauge 的正平均恒等与同源普通右旗费用

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；根代理提出单位根平均，boundary_core 完成原源、自然域和全部实际费用的接续；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文将[二进制幂联合稿](R271-appendix-dyadic-gauge-family-uniform-budget-and-source-interpolation.md)的插值绝对常数 $<9$ 降至 $1$，使用 $d$ 个复参数、每个参数模长为 $1$。全部作用仍是原有限头多项式，所有源和未来来自同一个实际顶部。未支付的仍是普通完整右旗费用，不以正平均本身宣布该费用有界。

## 1. 复参数并未改变原算子域

沿用上述联合稿的原对象：
$$
m\ge10,\quad d=2^m,\quad c_*=\frac{1601}{64},\quad
\rho=e^{-25d^3/2},\quad\epsilon=e^{-d^3/4},\quad d_0=e^{-20},
$$
$$
A_m=F_m(B_m),\qquad
h_m(z)=\frac{d_0^{-1}}{F_m(z)/z},\qquad
H_m=h_m(B_m)\otimes I=d_0^{-1}G_{1,m}.
$$
真逆芽给
$$
u_m(z):=d_0F_m(z)/z-1,\qquad
|u_m(z)|\le d_0\epsilon<\frac12\quad(|z|\le\rho).
$$
在该整个圆盘上取唯一满足 $\log h_m(0)=0$ 的解析支：
$$
\log h_m(z)=-\log(1+u_m(z)),\qquad
|\log h_m(z)|\le2d_0\epsilon.
\tag{1.1}
$$
对任意复数 $a$ 定义
$$
p_{m,a}(z)=\left[\exp(a\log h_m(z))\right]_{<d},
\qquad H_{m,a}=p_{m,a}(B_m)\otimes I.
\tag{1.2}
$$
在有限 Taylor 代数 $\mathbb C[z]/(z^d)$ 内，
$$
\boxed{
H_{m,a}=\sum_{\ell=0}^{d-1}\binom a\ell(H_m-I)^\ell,\qquad
H_{m,a}H_{m,b}=H_{m,a+b}.
}
\tag{1.3}
$$
这里 $(H_m-I)^d=0$；(1.3) 可由有限幂零代数中的 $\exp(a\log(1+K))$ 直接展开。
所以 $a\mapsto H_{m,a}$ 是次数不超过 $d-1$ 的算子值多项式。

每个 $H_{m,a}$ 都是原 $B_m$ 的次数 $<d$ 多项式，
因而保持原所有物理低头旗、完整源的尾核旗、左右方程和左零源核。
复系数不改变这些线性包含关系。
另外 $H_mA_m=B_m/d_0$，群律给
$$
\boxed{H_{m,a}A_m=d_0^{-1}H_{m,a-1}B_m.}
\tag{1.4}
$$
这里没有对 $A_m$ 或 $B_m$ 取一个未定义的逆。

## 2. 原 carry 和实际最小投影的全族统一性

若 $|a|\le2$，(1.1) 给
$$
|\exp(a\log h_m(z))|\le e^{4d_0\epsilon}\le2
\quad(|z|\le\rho).
$$
因此
$$
|[z^k]p_{m,a}(z)|\le2\rho^{-k}\quad(0\le k<d),
\qquad p_{m,a}(0)=1.
\tag{2.1}
$$
二进制幂联合稿 §2 的原权计算遂逐字适用：
$$
\boxed{
\|H_{m,a}\|\le e^{47d^4/8},\qquad
\|p_{m,a}(B)-H_{m,a}\|\le e^{-80d^4}=:\eta_m ,
\quad |a|\le2.
}
\tag{2.2}
$$
第二式里的全局候选明确是截断 $p_{m,a}(B)$，
不是先在全局取某个有限多项式的复幂。

取同一个 $w\in W$、同一个原顶部 $Q_m=\lfloor e^{c_*d^3}\rfloor$，
并始终沿用真正投影
$$
v_Q=P_{V_{m,Q}}w,\qquad k_Q=P_{K_{m,Q}}w,\qquad u_Q=v_Q-k_Q.
$$
令 $\zeta_m=e^{-d^4/8}$。带权真投影结论与 (2.2) 给全部 $|a|\le2$ 的一致界：
$$
\begin{aligned}
&\|H(v_Q-P_{\le Q}^{(m)}w)\|,\ \|Hk_Q\|
\le\zeta_m\|w\|,\\
&\|H(u_Q-P_{\le Q}^{(m)}w)\|\le2\zeta_m\|w\|,
\qquad H=H_{m,a}\ \text{或}\ H_{m,a}^* .
\end{aligned}
\tag{2.3}
$$
其自然域、窗口和真正最小性未变。

令 $u_m=u_{Q_m}$，对原同一族
$$
r_{m,p}=A_m(u_m)_p,\qquad
U_{m,p}r_{m,p}=P_{\le p}^{(m)}u_m,\qquad
p\in I_m=\{4d,\ldots,Q_m-d\},
$$
原左最小核正交给
$$
\langle U_{m,p}r,H_{m,a}U_{m,p}r\rangle
=\langle L_{m,p}r,H_{m,a}r\rangle .
\tag{2.4}
$$
所以同一低孔配对的误差至多 $4\zeta_m\|w\|^2$。

又 $p_{m,a}(0)=1$、$BM\subset N$，
故 $\langle w,p_{m,a}(B)w\rangle=\|w\|^2$。
于是全部 $|a|\le2$ 均有同一准确锚
$$
\begin{aligned}
\langle L_{m,p}r_{m,p},H_{m,a}r_{m,p}\rangle
={}&\|w\|^2
-\langle P_{>p}^{(m)}w,H_{m,a}P_{>p}^{(m)}w\rangle
+\mathcal E_{m,p,a},\\
|\mathcal E_{m,p,a}|&\le(4\zeta_m+\eta_m)\|w\|^2.
\end{aligned}
\tag{2.5}
$$

## 3. 单位根的正平均准确等于单位

取
$$
a_j=\exp(2\pi i j/d),\qquad 0\le j<d.
$$
由于 $a\mapsto H_{m,a}$ 是次数 $<d$ 的多项式，
而
$$
\frac1d\sum_{j=0}^{d-1}a_j^\ell=0\quad(1\le\ell<d),
$$
其常数项正是 $H_{m,0}=I$，故
$$
\boxed{\frac1d\sum_{j=0}^{d-1}H_{m,a_j}=I.}
\tag{3.1}
$$
所有平均权均为 $1/d$，绝对权重总和等于 $1$。

特别，对同一个高孔向量有
$$
\frac1d\sum_{j=0}^{d-1}
\langle P_{>p}^{(m)}w,H_{m,a_j}P_{>p}^{(m)}w\rangle
=\|P_{>p}^{(m)}w\|^2.
\tag{3.2}
$$
对 (2.5) 作这个正平均，左侧准确是 $\mu(r_{m,p})^2$，
误差仍至多 $(4\zeta_m+\eta_m)\|w\|^2$。
所以单独的高孔 gauge 二次型准确并回原尾范数，
不用估计它们各自的绝对值，也不用截断 $N$ 的虚假正交。

复参数没有造成新源问题：$|a_j|=1$、
$|a_j-1|\le2$，因此后续两类头乘子都已在 (2.2)–(2.3) 的同一预算内。

## 4. 原同源普通右旗目标，常数一

定义实际完整源
$$
s_{m,p,j}=H_{m,a_j-1}B_m(u_m)_p .
$$
由 (1.4)，准确有
$$
H_{m,a_j}r_{m,p}=d_0^{-1}s_{m,p,j}.
\tag{4.1}
$$
所有 $s_{m,p,j}$ 保留原完整 source 尾核旗；无需声称它们各自仍在原负图中。

令
$$
\mathcal R_{m,p}^2
=\frac1d\sum_{j=0}^{d-1}
  \lambda_{m,p}(s_{m,p,j})^2,
\tag{4.2}
$$
其中 $\lambda$ 是普通完整右链费用。
它没有被替换成已付 $\Xi$ 中的裸链费用。

由 (3.1)、(4.1) 及原同一 $G$ 的 Cauchy 不等式，
$$
\mu(r_{m,p})^2
=\frac1d\sum_j
 \langle Lr_{m,p},H_{m,a_j}r_{m,p}\rangle,
$$
$$
\boxed{
\mu(r_{m,p})^4
\le d_0^{-2}\operatorname{flat}(r_{m,p})^2
       \mathcal R_{m,p}^2 .
}
\tag{4.3}
$$
这是复数 Hilbert 空间中的普通直接和 Cauchy；
有限平均中的各项不需要分别为实数或非负。

还可准确看清 (4.2) 的强度。令 $Z_m=\log H_m$ 为有限幂零多项式，
$Z_m^d=0$；它不是一个未经定义的全局无界对数。
由 $H_{m,a}=\sum_{k<d}a^kZ_m^k/k!$，同一 $G^{-1/2}$ 度量中的离散 Parseval 给
$$
\boxed{
\mathcal R_{m,p}^2
=d_0^2\sum_{k=0}^{d-1}
 \lambda_{m,p}\!\left(Z_m^kr_{m,p}/k!\right)^2
\ge d_0^2\lambda_{m,p}(r_{m,p})^2.
}
\tag{4.4}
$$
所以这个正平均不是一个已被证明比原 ordinary 费用更弱的目标；
其作用是准确合并高孔二次型，同时保留全部共同右费用。

(4.2) 的同未来候选，至原顶部前，准确是
$$
-d_0H_{m,a_j}(u_m)_{p+t}.
$$
它的首输出是 $s_{m,p,j}$，并满足已有内部方程。
全局相应使用 $d_0p_{m,a_j}(B)w$ 的未来。
原顶部封口、完整高返回及全部 ordinary 费用仍须另付，(3.1) 不会支付这些项。

## 5. 全窗口的准确充分条件

记 $n_m=|I_m|$。将 (4.3) 的平方根在同一顶部族上求和，
$$
\boxed{
\left(\sum_{p\in I_m}\mu(r_{m,p})^2\right)^2
\le d_0^{-2}
 \left(\sum_{p\in I_m}\operatorname{flat}(r_{m,p})^2\right)
 \left(\sum_{p\in I_m}\mathcal R_{m,p}^2\right).
}
\tag{5.1}
$$
原预算存在 $\beta_m\to0$，满足
$$
\inf_{p\in I_m}\mu(r_{m,p})\ge(1-\beta_m)\|w\|,
\qquad
\sum_{p\in I_m}\operatorname{flat}(r_{m,p})^2
\le2d\beta_m^2\|w\|^2.
$$
因此，若以后能对这个实际族证明
$$
\sum_{p\in I_m}\mathcal R_{m,p}^2
\le K_mn_m\|w\|^2,\qquad
K_md/n_m=O(1),
\tag{5.2}
$$
则得到
$$
(1-\beta_m)^4
\le2d_0^{-2}(K_md/n_m)\beta_m^2,
$$
从而排除该非零 $w$。
特别 $K_m=O(\rho_m^{-2})$ 满足当前窗口尺度。

(5.2) 是尚未证明的普通右旗联合上界。
本文已付的是同一全局截断多项式、同一实际最小投影、
同一原负来源上的正平均恒等和 (4.3)–(5.1)。
它把插值损失降为 $1$，没有把原源 Schur 或 ordinary 封口免费补齐。
