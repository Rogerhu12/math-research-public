# R271 后续附录：稳定像的准确低输出插值与真正核的范数差

日期：2026-11-13（UTC）。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d。状态：下述准确插值定理已证明；没有证明无权 $N=M$。

本稿接 [R239 原线性全整数窗](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md) 的线性真实提升，及 [R239 局部最小能量与真实投影条件](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)。后者证明坏单位低输出不能来自真实核单位球，但没有断言它不在真实投影的线性像。本稿证明该线性像确实是整个低输出空间，甚至全部数据都可由 $N$ 中同时属于每个正指数孔域的向量准确实现。代价一般不一致有界，故这不是无权核心结论。

## 1. 固定合法窗和真正最小修复

固定原线性头尾
$$
 m\ge5,\quad d=2^m,\quad 4d\le q\le e^{d^3/4},
 \qquad L_m=A_m+D_m.
$$
记
$$
 V=\mathcal H_{\le q}^{(m)}
   \cap\ker(P_{\le q-1}^{(m)}L_m),
 \qquad \Pi=P_V
$$
为原 Hilbert 正交投影。因为 $V\subseteq\mathcal H_{\le q}^{(m)}$，
$\Pi w=P_VP_{\le q}^{(m)}w$，就是 R239 的低输出投影
$v_{m,q}(w)$。

对任意 $v\in V$，令 $r=L_mv=A_mv_q$，并取原闭仿射修复集的唯一最小元 $c(v)$。完整 Gram 公式使
$v\mapsto c(v)$ 为有界线性映射；它满足
$$
 L_mc(v)=r,\quad
 c(v)\in\mathcal H_{[q+1,q+d]}^{(m)},\quad D_m^dc(v)=0.
$$
这些结论对全部 $v\in V$ 成立，不只对预先来自 $M$ 的数据成立：低方程给出的逐层身份
$D_m^kr=(-1)^kA_m^{k+1}v_{q-k}$
正是原证明的全部输入。

原相容修复作为一个候选，给
$$
 \lambda^{\rm loc}(v):=\|c(v)\|
 \le e^{F(m,q)}\|v\|,
 \qquad F(m,q)\le2d^4.
 \tag{1.1}
$$
这里 $F$ 保持 R239 的原定义及物理系数。

定义
$$
 Jv=v-c(v),\qquad
 \|v\|_{\rm rep}^2=\|v\|^2+\|c(v)\|^2,
 \qquad
 K=\sqrt{1+e^{2F(m,q)}}.
$$
由于 $v$ 与 $c(v)$ 的尾孔支撑正交，
$$
 \boxed{
 \|Jv\|=\|v\|_{\rm rep},\quad
 \|v\|\le\|v\|_{\rm rep}\le K\|v\|,\quad
 \Pi J=I_V.
 }
 \tag{1.2}
$$
$J$ 将 $V$ 送入
$\ker L_m\cap\mathcal H_{\le q+d}^{(m)}$。

## 2. 已有真实提升的线性和全部正指数域

[R239 全整数逐步稿](../notes/2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md) §6、式 (6.7) 已构造固定源次数上的有界线性映射
$$
 \Lambda:
 \ker L_m\cap\mathcal H_{\le Q}^{(m)}
 \longrightarrow N=\overline{BM},
\quad
 \|\Lambda k-k\|\le\delta\|k\|,
 \quad \delta=e^{-75d^4},
 \tag{2.1}
$$
其范围条件是 $Q\le e^{d^3/3}$。这里取 $Q=q+d$；
由 $q\ge4d$ 及 $q\le e^{d^3/4}$，
$$
 Q\le(5/4)e^{d^3/4}<e^{d^3/3},
$$
故完全在已付范围内。

此处必须使用原稿的真正线性提升：每步使用固定辅助头和固定相容逆，更新是线性；步范数误差的可和界给算子范数收敛，故极限线性。不存在依赖输入而另选不同头的问题。

同一原稿还证明，每个 $\Lambda k$ 属于
$$
 \mathscr N_{\exp}:=
 N\cap\bigcap_{a>0}\operatorname{Dom}e^{a\mathcal N}.
 \tag{2.2}
$$
具体地，第 $n$ 步的原总孔数至多 $Q+5\cdot2^n d$，误差至多
$2e^{-76(2^nd)^4}\|k\|$，所以对每个固定 $a>0$ 加权误差级数可和。输入的有限孔数也已支付。这里 $\mathcal N$ 是原全部物理孔数。

## 3. 在修复范数中作准确 Neumann 校正

令
$$
 U=\Pi\Lambda J:V\to V.
$$
由 $\Pi J=I$ 和 $\|\Pi\|\le1$，
$$
 \|(U-I)v\|
 \le\delta\|Jv\|=\delta\|v\|_{\rm rep}.
$$
再使用 (1.2)，得
$$
 \boxed{
 \|U-I\|_{\rm rep\to rep}\le\eta:=\delta K.
 }
 \tag{3.1}
$$
因 $K\le2e^{2d^4}$，
$$
 \eta\le2e^{-73d^4}\le e^{-72d^4}<1/4.
 \tag{3.2}
$$
所以 $U^{-1}$ 是修复范数下真正有界的 Neumann 逆，并且
$$
 \|U^{-1}\|_{\rm rep\to rep}\le(1-\eta)^{-1}.
 \tag{3.3}
$$

定义准确提升
$$
 \boxed{\mathfrak L_{m,q}=\Lambda J U^{-1}:V\to H.}
 \tag{3.4}
$$
其像在 $\mathscr N_{\exp}$，且
$$
 \boxed{\Pi\mathfrak L_{m,q}=I_V.}
 \tag{3.5}
$$
这是真正等号，不再只是低投影误差很小。

还可保留原最小修复的点态成本：
$$
 \boxed{
 \|\mathfrak L_{m,q}v\|
 \le\frac{1+\delta}{1-\eta}
       \sqrt{\|v\|^2+\lambda^{\rm loc}(v)^2}.
 }
 \tag{3.6}
$$
确实，$\|\Lambda\|\le1+\delta$，$J$ 是 (1.2) 中的等距嵌入，随后使用 (3.3)。

与原混合核代表本身的距离也已支付：
$$
 \begin{aligned}
 \|\mathfrak L_{m,q}v-Jv\|
 &\le\|(\Lambda-I)JU^{-1}v\|
      +\|J(U^{-1}-I)v\|\\
 &\le\frac{\delta+\eta}{1-\eta}\|v\|_{\rm rep}\\
 &\le e^{-71d^4}\|v\|_{\rm rep}.
 \end{aligned}
 \tag{3.7}
$$
最后的固定常数由 $d\ge32$、$\delta\le\eta\le e^{-72d^4}$ 吸收。

## 4. 真实线性像是全部低输出空间

由 (3.5)，准确有
$$
 \boxed{
 \Pi(\mathscr N_{\exp})=\Pi(N)=\Pi(M)=V.
 }
 \tag{4.1}
$$
因此，“真实低输出范围更小”只能指指定范数球的像；若指线性像，则在当前合法窗内不成立。

特别，R239 的坏单位输入 $v_q^{\rm bad}\in V$ 确实有
$$
 n_q=\mathfrak L_{m(q),q}v_q^{\rm bad}
 \in N\cap\bigcap_{a>0}\operatorname{Dom}e^{a\mathcal N},
 \qquad \Pi n_q=v_q^{\rm bad}.
 \tag{4.2}
$$
这与其真实原像的巨大范数下界一致。旧观测定理给每个满足
$\Pi w=v_q^{\rm bad}$ 的 $w\in M$
$$
 \|w\|\ge
 \exp[(c_0-o(1))(\log q)^{4/3}],
 \qquad c_0=0.1747818284\ldots .
 \tag{4.3}
$$
本稿给的实际正则原像同时满足
$$
 \|n_q\|\le
 \exp[(K_*+o(1))(\log q)^{4/3}],
 \qquad K_*=3(16/770)^{1/3}.
 \tag{4.4}
$$
这里 (4.3) 的下界和 (4.4) 的常数均沿用旧结果，不重新登记它们；新增是 (4.2) 的确切存在及其有界线性实现。不能因为坏数据有真实原像，就把该原像擅自归一化后仍要求低投影保持同一个单位数据。

## 5. 闭空间 M、N 的准确插值 Gram

令 $P_M,P_N$ 为原 Hilbert 正交投影，在 $V$ 上定义
$$
 H_M=\Pi P_M|_V,\qquad H_N=\Pi P_N|_V.
$$
若
$$
 C_{m,q}=\frac{1+\delta}{1-\eta}K,
$$
则 (3.6) 给 $\|\mathfrak L_{m,q}\|\le C_{m,q}$。
由于它是 $\Pi|_N$ 的右逆，伴随配对给
$$
 \boxed{
 C_{m,q}^{-2}I_V\le H_N\le H_M\le I_V .
 }
 \tag{5.1}
$$
这两个插值 Gram 与旧修复 Gram $G_{m,q}$ 是不同算子，不能混同。

对 $S=M,N$，闭仿射集合
$\{s\in S:\Pi s=v\}$ 非空，具有唯一最小范数元，且
$$
 \boxed{
 \mathfrak e_S(v)^2
 :=\min_{\substack{s\in S\\\Pi s=v}}\|s\|^2
 =\langle H_S^{-1}v,v\rangle.
 }
 \tag{5.2}
$$
若 $W=M\ominus N$ 为真正缺陷，则
$$
 \boxed{H_M-H_N=\Pi P_W|_V\ge0.}
 \tag{5.3}
$$
所以全部有限窗口的线性像相同，并不意味着它们诱导的最小原像范数相同。

## 6. 尚未解决的是范数，而非局部数据可实现性

取全整数头 $m(q)$ 和对应 $V_q,\Pi_q$。旧低投影估计给每个固定
$w\in M$
$$
 \|w-\Pi_qw\|
 \le\tau_q(w)+e^{-74d(q)^4}\|w\|\longrightarrow0.
 \tag{6.1}
$$
若 $0\ne w\in W$ 并归一化，令 $v_q=\Pi_qw$。则
$v_q\to w$、$P_Wv_q\to w$。由 (5.3)，
$$
 \langle(H_M^{(q)}-H_N^{(q)})v_q,v_q\rangle
 =\|P_Wv_q\|^2\longrightarrow1.
$$
又两者的差始终位于 $0$ 与 $I_{V_q}$ 之间，故
$$
 \boxed{
 W\ne0\ \Longrightarrow\
 \|H_M^{(q)}-H_N^{(q)}\|\longrightarrow1.
 }
 \tag{6.2}
$$
反之若 $W=0$，每个差都为零。此式只是把真正缺陷准确放在最小插值范数的差中，不是对该差的新上界。

当前得到的是：任意固定合法窗口的所有低输出数据，都有真实、正则、属于 $N$ 的准确原像；其点态范数由 (3.6) 控制。对任意固定 $w\in M$，仍未证明
$\|\mathfrak L_{m(q),q}\Pi_qw\|$ 有有界子列，或能够以另一选择取得这样的有界子列。因而不把 (4.1) 当成 $N=M$，也不把每个有限窗口的正则可实现性当成无权核内稠密。后续应继续控制真正数据的完整最小能量与末端泄漏。
