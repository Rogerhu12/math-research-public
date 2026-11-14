# R163. 惰性 theta 连接的精确赋值与原混合列的共同共振

**状态：已证明；尚未给出严格的惰性饱和 jet 预算。**

沿 R162 的实际固定输入，记

$$
\mathcal A=A_2=P(s)e^{W(s)}=sZ(s),\quad
Z=p_0e^W,\quad V=B/A_2-1=-22s+\cdots,
$$

$$
W=\sum_{m\ge1}w_ms^m,\qquad
w_m=\frac{17}{m}\prod_{j=0}^{m-1}\frac{4j+1}{4j+3}.
$$

对每个惰性 $p\ge7$，定义
$\epsilon_h(m)=\mathbf1_{\{p^h/4<(m\bmod p^h)<3p^h/4\}}$。
逐个模 $p^h$ 计数给出全部 $m$ 的准确公式

$$
v_p(w_m)=-v_p(m)+\sum_{h\ge1}(-1)^h\epsilon_h(m).
$$

因此在 $1\le m<p^H$ 上，最小赋值是奇 $H$ 时的 $-H$、
偶 $H$ 时的 $-H+1$；边界 $m=p^H$ 的赋值另为 $-H$。
结合 $p_0'/p_0$ 整性，对每个 $a\ge1$ 得

$$
Z(s)^{-p^{2a}}\equiv1\pmod{p,\ s^{p^{2a}}}.
$$

保留实际源列 $\mathcal A^jV^c$、$0\le c\le j\le D$，
改用 $X=\mathcal A=w+\cdots$ 作输出参数。
再对全部列共同乘以固定形式单位
$\gamma=V'/\mathcal A'$，其常数为 $-22$。
所有准确饱和前缀核不变；对 $p\ne11$，各阶 jet quotient norm
也完全不变，不要求 $\gamma$ 的高阶系数整。

共同矩阵准确为

$$
\widetilde{\mathcal B}_{k;(j,c)}
=[s^{M-1}]V^cV'Z^{-M},\qquad M=k+1-j>0.
$$

在 $M=p^{2a}$ 时，其准确模 $p$ 行为是

$$
\widetilde{\mathcal B}_{j+p^{2a}-1;(j,c)}
\equiv(-22)^{p^{2a}}\mathbf1_{c=p^{2a}-1}\pmod p.
$$

因此 $j<p^{2a}-1$ 的整个次数块在该行消失；
$j=p^{2a}-1$ 时 $c=j$ 的单位边界项必须保留。
这是实际共同变换下的块关系，不是整个混合行同时被 $p$ 除。
它不使用两条原中央导数消失；相邻 $j$ 块的联合前缀消元、
以及 R159 平面门槛 $a_I+2b_I<2$，仍未支付。

见[完整证明](../notes/2026-11-12-actual-theta-inert-valuation-and-even-power-jet-resonance.md)。
