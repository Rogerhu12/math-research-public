# 同源二进制 gauge 幂的统一真实预算、有限变差插值与普通右旗目标

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文支付原同一 gauge 的全部 $1\le a\le2^{d-1}$ 幂的真实环境、全局 carry 及实际最小投影误差；给出绝对系数总和小于 $9$ 的准确插值。它把单幂锚中单独未付的高孔二次型并回原尾范数，并把剩余目标写成同一个实际来源的普通右旗联合预算。最后的普通右费预算没有被证明，原 $N=M$ 和普通 ISP 仍未完成。

依赖：
- [真正最小投影的带权窗口](R271-appendix-true-minimal-projection-weighted-window.md)；
- [真逆芽的原半径和系数](../notes/2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)；
- [全局实际后移与原 W 锚](../notes/2026-11-15-global-weighted-shift-to-true-head-gauge-carry-and-w-anchor-789f-next.md)；
- [完整原源与裸／普通右费](R239-appendix-full-tail-low-head-source-strip-and-bare-to-complete-right-bound.md)。

## 1. 只使用同一个真实有限头

取原 $N/Y$ 模型之一，固定
$$
m\ge10,\qquad d=2^m,\qquad
c_*=\frac{1601}{64},\qquad
\rho=e^{-25d^3/2},\quad \epsilon=e^{-d^3/4},\quad d_0=e^{-20}.
$$
写
$$
A_m=F_m(B_m),\qquad f_{0,m}(z)=F_m(z)/z,\qquad
h_m(z)=\frac{d_0^{-1}}{f_{0,m}(z)}.
$$
商在零点按解析延拓理解。原逆芽给
$$
|f_{0,m}(z)-d_0^{-1}|\le\epsilon\quad(|z|\le\rho),
\qquad h_m(0)=1.
\tag{1.1}
$$
令
$$
H_m=h_m(B_m)\otimes I=d_0^{-1}G_{1,m},\qquad
H_{m,a}=H_m^a.
$$
这些都是原物理头上的有界多项式。因 $h_m(z)-1$ 在零点消失，
$$
(H_m-I)^d=0.
\tag{1.2}
$$
下文的幂次数 $a$ 与原尾孔层、primitive birth 均不同，不把它们互换。

## 2. 指数多的幂仍只付一次原环境费用

由 (1.1)，
$$
|h_m(z)|\le(1-d_0\epsilon)^{-1}.
$$
对全部整数 $1\le a\le2^{d-1}$，
$$
|h_m(z)^a|
\le \exp(2a d_0\epsilon)\le2\quad(|z|\le\rho).
\tag{2.1}
$$
最后一个估计可直接由
$2^d\epsilon=\exp(d\log2-d^3/4)\le e^{-d^3/8}<1/2$
验证；$d\ge1024$ 远强于所需条件。

置
$$
p_{m,a}(z)=[h_m(z)^a]_{<d}.
$$
Cauchy 系数估计给
$$
|[z^k]p_{m,a}(z)|\le2\rho^{-k},\qquad 0\le k<d,
\qquad p_{m,a}(0)=1.
\tag{2.2}
$$
同时
$$
p_{m,a}(B_m)\otimes I=H_{m,a}.
\tag{2.3}
$$
注意：以后使用的是这个先合幂、再取 $<d$ 截断的全局多项式。
不将 $p_{m,a}(B)$ 无证换成 $p_{m,1}(B)^a$。

原实际权为
$$
W_k=\prod_{i\in\operatorname{bits}(k)}d_i,\qquad
d_i=e^{-\Lambda_i},\qquad
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i.
$$
带权窗口稿已从全部真实 carry 位置证明
$\|B_m^k\|=W_k$，且
$$
\max_{k<d}\rho^{-k}W_k
=\rho^{-(d-1)}W_{d-1}.
$$
原准确指数是
$$
\log\!\big(\rho^{-(d-1)}W_{d-1}\big)
=\frac{35}{6}d^4+\frac52d^3-(150m-275)d-\frac{850}{3}.
$$
所以 (2.2) 在全部上述 $a$ 上一致给
$$
\boxed{
\|H_{m,a}\|
\le2d\,\rho^{-(d-1)}W_{d-1}
\le\exp\!\left(\frac{35}{6}d^4+3d^3\right)
\le e^{47d^4/8}.
}
\tag{2.4}
$$
幂次数没有乘到 $35d^4/6$ 上。这一步只在同一个原物理度量中还原一次，没有逐次乘 $\|H_m\|$。

全局 carry 同样一致。原权位置证明给
$$
\|B^k-(B_m\otimes I)^k\|\le\alpha_m
\quad(1\le k<d),
$$
其中
$$
-\log\alpha_m=\frac{280}{3}d^4-90d^3+300d-\frac{850}{3}.
$$
由 (2.2)，
$$
\begin{aligned}
\|p_{m,a}(B)-H_{m,a}\|
&\le2d\,\alpha_m\rho^{-(d-1)}
\le e^{-80d^4}=:\eta_m .
\end{aligned}
\tag{2.5}
$$
最后的对数上界是
$-(485/6)d^4+(155/2)d^3-300d+850/3+\log(2d)$，
对 $d\ge1024$ 不超过 $-80d^4$。
这包含所有更高 carry，而非只比较两个有限矩阵。

## 3. 全家同时作用于原真正最小投影

固定同一个 $w\in W=M\ominus N$，原定义为
$M=\ker T$、$N=\overline{BM}$。
对 $4d\le Q\le e^{c_*d^3}$，令
$$
v_Q=P_{V_{m,Q}}w,\qquad
k_Q=P_{K_{m,Q}}w,\qquad
u_Q=v_Q-k_Q.
$$
这里全部投影和自然域都与带权窗口稿相同。
该稿已付
$$
\|v_Q-P_{\le Q}^{(m)}w\|,\ \|k_Q\|
\le e^{-6d^4}\|w\|,
\qquad
\|u_Q-P_{\le Q}^{(m)}w\|\le2e^{-6d^4}\|w\|.
$$
令 $\zeta_m=e^{-d^4/8}$。
(2.4) 于是对全部 $a\le2^{d-1}$、全部同窗 $Q$ 同时给
$$
\boxed{
\begin{aligned}
&\|H(v_Q-P_{\le Q}^{(m)}w)\|,\ \|Hk_Q\|
\le\zeta_m\|w\|,\\
&\|H(u_Q-P_{\le Q}^{(m)}w)\|\le2\zeta_m\|w\|,
\qquad H=H_{m,a}\ \text{或}\ H_{m,a}^* .
\end{aligned}}
\tag{3.1}
$$
没有因为使用指数多的幂而重复选择 $v_Q,k_Q$，也没有先求和这些误差。

$H_{m,a}$ 只作用头、与 $A_m,D_m$ 交换，因而保持原 $V_{m,Q},K_{m,Q}$。原同源反向投影反馈同样给
$$
\|P_{V_{m,Q}}H_{m,a}(I-P_{V_{m,Q}})w\|
\le\zeta_m\|w\|.
\tag{3.2}
$$

现在固定同一顶部
$$
Q_m=\lfloor e^{c_*d^3}\rfloor,\qquad u_m=u_{Q_m},\qquad
I_m=\{4d,\ldots,Q_m-d\}.
$$
对 $p\in I_m$，沿用原实际负图来源
$$
r_{m,p}=A_m(u_m)_p,\qquad
U_{m,p}r_{m,p}=P_{\le p}^{(m)}u_m,\qquad
L_{m,p}=U_{m,p}^*U_{m,p}.
\tag{3.3}
$$
$H_{m,a}$ 保持左方程和左零源核，所以
$$
H_{m,a}U_{m,p}r-U_{m,p}(H_{m,a}r)\in K_{m,p}.
$$
与原最小 $U_{m,p}r$ 配对，得到准确身份
$$
\langle U_{m,p}r,H_{m,a}U_{m,p}r\rangle
=\langle L_{m,p}r,H_{m,a}r\rangle.
\tag{3.4}
$$
(3.1) 的两侧估计遂给
$$
\left|
\langle L_{m,p}r_{m,p},H_{m,a}r_{m,p}\rangle
-\langle P_{\le p}^{(m)}w,H_{m,a}P_{\le p}^{(m)}w\rangle
\right|
\le4\zeta_m\|w\|^2.
\tag{3.5}
$$
这对所有 $p,a$ 一致；并未声称变换后的源仍满足原负图条件。

又因 $p_{m,a}(0)=1$，$BM\subset N$ 给
$$
\langle w,p_{m,a}(B)w\rangle=\|w\|^2.
$$
结合 (2.5)、(3.5) 及头乘子与孔截断交换，
$$
\begin{aligned}
\langle L_{m,p}r_{m,p},H_{m,a}r_{m,p}\rangle
={}&\|w\|^2
-\langle P_{>p}^{(m)}w,H_{m,a}P_{>p}^{(m)}w\rangle
+\mathcal E_{m,p,a},\\
|\mathcal E_{m,p,a}|&\le(4\zeta_m+\eta_m)\|w\|^2.
\end{aligned}
\tag{3.6}
$$
单独每个高孔二次型仍不能用未知速率的尾范数乘 (2.4) 删除。下一节在共同源上准确相消它们。

## 4. 二进制节点的有限变差插值

以下是一个自足有限维代数引理。
若 $H=I+K$、$K^d=0$，则
$$
H^t=\sum_{\ell=0}^{d-1}\binom{t}{\ell}K^\ell
$$
是 $t$ 的次数 $\le d-1$ 算子值多项式；对非负整数 $t$ 与通常幂相同。

取互异节点
$$
a_j=2^j,\qquad 0\le j<d,
$$
以及 Lagrange 系数
$$
c_{d,j}=\prod_{\substack{0\le k<d\\k\ne j}}
\frac{-2^k}{2^j-2^k}.
\tag{4.1}
$$
在 $t=0$ 求值，严格得到
$$
\boxed{I=\sum_{j=0}^{d-1}c_{d,j}H^{2^j},\qquad
\sum_{j=0}^{d-1}c_{d,j}=1.}
\tag{4.2}
$$
这些系数为实数，符号是 $(-1)^j$。令 $q=1/2$，则
$$
|c_{d,j}|=
\frac{q^{j(j+1)/2}}
{\prod_{h=1}^{j}(1-q^h)\prod_{h=1}^{d-1-j}(1-q^h)}.
$$
把 $\prod_{h=1}^{d-1}(1+tq^h)$ 按 $t$ 展开，或对因子数作直接归纳，得到有限恒等式
$$
\boxed{
C_d:=\sum_{j=0}^{d-1}|c_{d,j}|
=\prod_{h=1}^{d-1}\frac{1+2^{-h}}{1-2^{-h}}<9.
}
\tag{4.3}
$$
为明确验证数值常数，前三个因子之积为 $45/7$。
对 $h\ge4$，令 $x=2^{-h}\le1/16$，有
$$
\log\frac{1+x}{1-x}\le\frac{2x}{1-x}\le\frac{32}{15}x.
$$
尾和 $\sum_{h\ge4}2^{-h}=1/8$，故其乘积不超过
$e^{4/15}\le15/11$。总乘积因而至多 $675/77<9$；
因子数小于三时更直接。

将引理用于同一个 $H_m$，(1.2) 保证
$$
\boxed{\sum_{j=0}^{d-1}c_{d,j}H_{m,2^j}=I.}
\tag{4.4}
$$
所以，对任意原物理高孔向量 $w_{\rm hi}$，
$$
\boxed{
\sum_{j=0}^{d-1}c_{d,j}
 \langle w_{\rm hi},H_{m,2^j}w_{\rm hi}\rangle
=\|w_{\rm hi}\|^2.
}
\tag{4.5}
$$
这是准确的同一向量身份。它不需要每个二次型为实数或非负，
也不要求截断的 $N$ 分量与 $w$ 正交。

将 (3.6) 按这组系数相加，误差总量至多
$9(4\zeta_m+\eta_m)\|w\|^2$；
左侧又由 (4.4) 准确等于 $\mu_{m,p}(r_{m,p})^2$。
因此高孔部分只留下原 $\|P_{>p}^{(m)}w\|^2$。
这个联合步骤不产生 $d$、$2^d$ 或原头条件数的额外插值损失。

## 5. 同一实际来源的普通右旗联合费用

仍固定 (3.3) 的原 $r=r_{m,p}$、$u_m$，不重新选 $w$ 或顶部。
定义 $d$ 个合法原源
$$
s_{m,p,j}=H_m^{2^j-1}B_m(u_m)_p,\qquad 0\le j<d.
\tag{5.1}
$$
$H_mA_m=B_m/d_0$，故
$$
H_{m,2^j}r=d_0^{-1}s_{m,p,j}.
\tag{5.2}
$$
这些头多项式保持原完整源的尾核旗，所以 (5.1) 都在同一个 $\mathscr R_{m,p}$。
它们未被宣布为原负图来源；所需的普通右旗最小化本来就对全部 $\mathscr R_{m,p}$ 定义。

原准确 Cauchy 给任意合法 $s$
$$
|\langle Lr,s\rangle|
\le\operatorname{flat}(r)\lambda(s),
\qquad
\operatorname{flat}(r)^2=\langle GLr,Lr\rangle,\quad
\lambda(s)^2=\langle G^{-1}s,s\rangle.
$$
由 (4.4)、(5.2)，
$$
\mu(r)^2
=\sum_{j=0}^{d-1}c_{d,j}\langle Lr,H_{m,2^j}r\rangle.
$$
置真正的联合普通右费
$$
\mathfrak R_{m,p}^2
=\sum_{j=0}^{d-1}|c_{d,j}|\,\lambda_{m,p}(s_{m,p,j})^2.
\tag{5.3}
$$
对同一 $G$ 度量作一次 Cauchy，得到
$$
\boxed{
\mu_{m,p}(r_{m,p})^4
\le\frac{C_d}{d_0^2}
 \operatorname{flat}_{m,p}(r_{m,p})^2\,\mathfrak R_{m,p}^2
\le\frac9{d_0^2}
 \operatorname{flat}_{m,p}(r_{m,p})^2\,\mathfrak R_{m,p}^2.
}
\tag{5.4}
$$
(5.3) 是普通完整右链费用，不是 $\Xi$ 中的裸链费用。
本稿没有以环境范数 (2.4) 估掉它。

若使用同一实际 $u_m$ 的后续孔段，
$-d_0H_{m,2^j}(u_m)_{p+t}$ 确满足 (5.1) 的首输出及到原顶部前的内部方程。
但顶部封口和全部高返回仍须另付。
全局候选相应是 $d_0p_{m,2^j}(B)w$ 的未来，
不是仅用 $B_mw$；也不把 $p_{m,2^j}(B)$ 换成未截断的全局高幂。

## 6. 与当前实际窗口的精确充分尺度

令 $n_m=|I_m|=Q_m-5d+1$。对同一个假定非零 $w$，原全窗预算给某个 $\beta_m\to0$：
$$
\inf_{p\in I_m}\mu(r_{m,p})\ge(1-\beta_m)\|w\|,
\qquad
\sum_{p\in I_m}\operatorname{flat}(r_{m,p})^2
\le2d\beta_m^2\|w\|^2.
\tag{6.1}
$$
例如可取带权窗口稿中的原总孔尾量除以 $\|w\|$，
再加 $2e^{-6d^4}$。这不是额外速率假设。

把 (5.4) 的平方根求和，得到真实必要不等式
$$
\boxed{
\left(\sum_{p\in I_m}\mu(r_{m,p})^2\right)^2
\le\frac{C_d}{d_0^2}
 \left(\sum_{p\in I_m}\operatorname{flat}(r_{m,p})^2\right)
 \left(\sum_{p\in I_m}\mathfrak R_{m,p}^2\right).
}
\tag{6.2}
$$
因此，若将来能仅对这个实际来源证明
$$
\sum_{p\in I_m}\mathfrak R_{m,p}^2
\le K_m n_m\|w\|^2,
\qquad
\frac{K_m d}{n_m}=O(1),
\tag{6.3}
$$
则 (6.1)–(6.2) 给
$$
(1-\beta_m)^4
\le\frac{18}{d_0^2}\frac{K_m d}{n_m}\,\beta_m^2,
$$
与 $\beta_m\to0$ 矛盾。
特别，$K_m=O(\rho_m^{-2})=O(e^{25d^3})$ 落在当前窗口中，因为
$$
\frac{\rho_m^{-2}d}{n_m}
=O\!\left(d\,e^{-d^3/64}\right)\longrightarrow0.
$$

(6.3) 只是接下来的明确充分目标，本稿不把它当成已付。
新无条件结论是 (2.4)–(3.6) 的整组真实预算、
(4.2)–(4.5) 的有限变差准确消元，以及保完整普通右域的 (5.4)、(6.2)。
高孔二次型不必再单独乘巨大 gauge 范数，但原普通右旗的封口、
高返回和同源 $P_KG_1u$ 反馈没有因插值自动消失。
