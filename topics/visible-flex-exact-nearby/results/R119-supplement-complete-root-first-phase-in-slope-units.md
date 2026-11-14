# R119 续篇：同一根阈值上的完整首相位与斜率单位余项

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 在[实际根全输入高输出 Volterra](R119-supplement-root-high-output-Volterra-without-low-frequency-condition-number.md)的同一 canonical 根及同一阈值

$$
L_b=2^{4200}b,\qquad P_b=\mathbf 1_{\{|m|\ge L_b\}},
\tag{F.1}
$$

上，把准确的一次积分换成真正酉的同支首相位，仍有

$$
\boxed{\quad
\|P_b[U(\xi,\eta)-e^{B_{\xi,\eta}}]:
       H^s\longrightarrow H^{s+4/3}\|
 <2^{4098}b^{4/3},\qquad |s|\le1 .
\quad}
\tag{F.2}
$$

输入没有截断，包括两个 mean、两条 wave 行和两个 Fourier 锥。
这里 $B_{\xi,\eta}$ 在第1节准确给出；$e^B$ 同时为普通酉及 Green
$\mathsf J$-酉。它不是把实际传播改成模型。真实 root graph、自由
Airy 到 strict wave 的两行框架、strict 段与整个网络的重新复合仍须另付。

## 1. 同一个完整模型及其有限部

实际方程、完整自由基和势满足

$$
u_{\xi\xi}-{\xi\over b^2}u_{\phi\phi}+Vu=0,\quad
0\le\eta\le\xi\le H={1\over64},\quad
|V|<17,\quad |V_\xi|<129
\tag{F.3}
$$

于[第51束](R119-supplement-actual-nonradial-full-remainder-and-high-network.md)所用的固定角条带；所用较小条带宽为 $1/128$。
频率是 $m\in4\mathbb Z$。令 $D=|{-i\partial_\phi}|$，在 mean 上
置 $D^{-1/2}=0$；$\Pi_\epsilon$ 投到 $\epsilon m>0$。
自由 Airy 支按
$\operatorname{Bi}(-\xi(|m|/b)^{2/3})+i\sigma\operatorname{Ai}(-\xi(|m|/b)^{2/3})$
的原完整两行固定，mean 仍用原 $c(1\pm i\xi/\pi)$。
记 $\tau(q)=2q^{3/2}/(3b)$，定义真实实系数

$$
a_{\sigma\epsilon}^{\xi,\eta}(\phi)
 ={b\over2}\int_\eta^\xi
 {V(q,\phi-\sigma\epsilon\tau(q))\over\sqrt q}\,dq ,
\qquad
A_\sigma=\sum_{\epsilon=\pm1}
 \Pi_\epsilon D^{-1/2}M_{a_{\sigma\epsilon}^{\xi,\eta}}
 D^{-1/2}\Pi_\epsilon ,
\quad
B_{\xi,\eta}=i\,\operatorname{diag}(A_+,-A_-).
\tag{F.4}
$$

端点 $\eta=0$ 的积分绝对收敛。保持两个投影的准确位置使
$A_\sigma=A_\sigma^*$，故 $B^*=-B$；它又与
$\mathsf J=\operatorname{diag}(I,-I)$ 交换。反向传播使用反向有序积分；
其模型为 $e^{-B_{\xi,\eta}}$，同一证明成立。

不同 wave 符号约定会同时交换两个幅度支和射线方向。本文固定上面的
完整基，因而射线符号来自准确矩阵
$F_m^{-1}(0,0;-V,0)F_n$。四个系数的角平均完全相同：

$$
\langle a_{\sigma\epsilon}^{\xi,\eta}\rangle
 ={b\over2}\int_\eta^\xi{\langle V(q)\rangle\over\sqrt q}\,dq .
\tag{F.5}
$$

所以它仍是[实际首密度相位](R119-supplement-actual-nonradial-first-density-phase.md)
(B.10) 中真实根有限部的 potential 部分。自由两行的
$-5b/(48H^{3/2})$ 及右根交换矩阵没有被本篇删除或吸收成零。

## 2. 一次积分本身已有正确的 $b^{4/3}$ 费用

令 $T_1=\int_\eta^\xi K(q)\,dq$。这里使用
[R43](R43-first-airy-phase-and-four-thirds-remainder.md) §§2–6
的完整第一次 Dyson 矩阵证明；不使用该篇将多次 Dyson 合起来时的
小 collar 假设。令 Fourier 整数为 $n=m/4$，其实际 Airy 频率间距为
$q_0=4/b$。R43 (6.3)–(6.4) 的准确常数为

$$
C_{q_0}=4(50\pi+5)q_0^{-4/3}
       +150\pi\max(1,q_0^{-2/3})+3q_0^{-1}.
\tag{F.6}
$$

由于 $b>1$，用 $\pi<22/7$ 逐项得

$$
C_{q_0}<2^{11}b^{4/3}.
\tag{F.7}
$$

这不是只估可比的非零频率。该证明在可比同号对中先切
$q=(\min(|m|,|n|)/b)^{-2/3}$ 的真实根层，再用完整两行 Airy
振荡式；反支作一次真正径向分部积分，费用包含 $V_\xi$。
其余频率对满足大 lag，按完整 Airy 列估计，费用只有
$\max(1,q_0^{-2/3})$ 及 $q_0^{-1}$。两个 mean 和异号对正是在
后一项中支付。因而没有一个低模条件数乘进 (F.7)。

对标准 Fourier 指标 $\ell$，

$$
w_\ell:=\sup_q\bigl(|V_{4\ell}(q)|+|(V_\xi)_{4\ell}(q)|\bigr)
 \le146e^{-|\ell|/32}.
\tag{F.8}
$$

$|s|\le1$ 时 R43 的 lag 权次数至多 $11/3<4$。用
$e^{-x/32}=e^{-x/64}e^{-x/64}$、
$x^4e^{-x/64}\le4!\,64^4$ 及
$\sum_{\ell\in\mathbb Z}e^{-|\ell|/64}<129$，得到完整的

$$
\sum_\ell(1+|\ell|)^4w_\ell
 <146\cdot8\cdot129(1+4!\,64^4)<2^{48}.
\tag{F.9}
$$

从 $\langle n\rangle$ 回到物理 $\langle4n\rangle$ 的 Sobolev
权比费用小于 $2^7$；R43 中的两个 wave 行和附加权因子再付 $2^4$。
当 $\eta>0$ 时，把 $[0,\xi]$ 和 $[0,\eta]$ 两个已经证明的准确
一次积分相减，再付2。因此，所有输入和输出上都有

$$
\boxed{\quad
\|T_1-B_{\xi,\eta}:H^s\to H^{s+4/3}\|
 <2^{128}b^{4/3},\qquad |s|\le1 .
\quad}
\tag{F.10}
$$

这是先乘完整 Sobolev 权比再作 lag 卷积的算子结论。没有用单列范数
代替 Hilbert 空间算子范数，也没有在低输入端加投影。

## 3. 首相位指数化不再损失额外 $b^{2/3}$

同一实际势的卷积给

$$
\|B:H^r\to H^{r+1}\|<2^{128}b,\qquad |r|\le3.
\tag{F.11}
$$

真实非径向背景在根上的 $V-V_0$ 为 $2^{32}n_i$；
角条带及两行有限常数给 $B$ 的非径向部分在
$H^r,\ |r|\le3$ 上的范数小于 $2^{128}bn_i$。
原[根图小球](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)
(G.5) 已给 $b^2n_i\le2^{-512}$，所以此数小于 $2^{-384}$。
径向部分在每个 Fourier 模上是纯虚对角，准确保持所有 Sobolev
范数。对这个完整径向部分作 interaction，真实有序 Duhamel 因而给

$$
\|e^{tB}:H^r\to H^r\|<2,\qquad |t|\le1,\quad |r|\le3.
\tag{F.12}
$$

这项费用来自实际非径向小量；没有取径向大平均的绝对指数。
在更小角条带的复平移族中，同一论证仍成立：径向部分不变，其余
部分的完整复范数已由相同固定余宽支付。

记 $E_B=e^B-I-B$。准确有

$$
E_B=\int_0^1(1-t)e^{tB}B^2\,dt,\qquad
\|E_B:H^s\to H^{s+2}\|<2^{256}b^2 .
\tag{F.13}
$$

另一方面，在 **同一个** (F.1) 的输出 cut 上，

$$
\|P_bE_B:H^s\to H^s\|
 \le2+1+2^{128}b/L_b<4 .
\tag{F.14}
$$

固定输入空间 $H^s$，对输出 Hilbert Sobolev 标度在
(F.13) 与 (F.14) 之间插值，参数为 $2/3$。于是

$$
\|P_bE_B:H^s\to H^{s+4/3}\|
 <4^{1/3}(2^{256}b^2)^{2/3}
 <2^{172}b^{4/3}.
\tag{F.15}
$$

这一步所用的同阶界是完整高输出算子界，不是逐 shell supremum；
因此不需要把没有求和的 dyadic 估计当作插值输入。
本篇也没有把全空间 $E_B$ 的同阶范数误写成固定常数：
只有乘了明确的 $P_b$ 后才使用 (F.14)。

## 4. 接入已经证明的完整二次 Volterra

精确分解为

$$
P_b(U-e^B)=P_b(U-I-T_1)+P_b(T_1-B)-P_bE_B.
\tag{F.16}
$$

第一项是前篇全输入的 (V.2)，其常数为 $2^{4096}b^{4/3}$；
第二、三项分别由 (F.10)、(F.15) 给出。三项费用的和严格小于
$2^{4098}b^{4/3}$，证明 (F.2)。两次 Volterra 需要的频带行列
Schur 已在前篇支付；本篇只消费其已成立的完整强算子界。

原 ordinary 与 weak 源仍用真实
$\int U(\xi,q)s(q)\,dq$，高输出费沿用前篇的2倍完整源积分。
total flux、Piola、height 修正、mean charge、两个端点荷及
$\Gamma^*$ 两列仍按第51束和原根图篇处理。本篇没有求参数导数，
因此不把固定 canonical 坐标中的 (F.4) 当作已经包括全部移动端点项。

本篇的 stdlib 消费器只核查显示的整数/有理常数门，并绑定正文及全部
前置证明的独立 SHA。新的数学执行只允许公开
Rogerhu12/math-research-public 的 GitHub Actions；未用本地数学运行
代替公开过程。本篇没有声称新全网络 cutoff 或最终非线性存在已经成立。
