# R271 附录：同一顶部负部预算的固定二次尺度与自适应慢窗口

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root 与 boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：已证明的条件转换。本文核清原真正顶部允许的窗口选择，证明当前合并负二次型只需在一个固定二次尺度曲线上有线性窗口费用；也给同一个 $w$ 上慢选更大窗口的完整方法。所需负部上界本身仍未证明。本文不将条件转换登记成 $N=M$ 或普通 ISP 的完成。

依赖：

- [真正最小投影的带权窗口](R271-appendix-true-minimal-projection-weighted-window.md)；
- [强物理尾位并头的同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
- [同顶部顺次投影负二次型](R271-appendix-same-top-sequential-projection-negative-form-and-complete-return-scalar.md)。

本文所用第二篇的准确原式是其 (2.2)、(2.8)、(6.3)，下文全部重新写出。所有孔层 MP 仍只在固定有限层上读取；不涉及全孔直和上的有界删除逆。

## 1. 可变 $Q$ 的真正顶部和与 $Q$ 无关的误差

固定原模型之一及同一个 $w\in W=M\ominus N$。取

$$
m\ge10,\qquad d_m=2^m,\qquad
Q_m^{\max}=\left\lfloor
 \exp\!\left(\left(25+\frac1{64}\right)d_m^3\right)
\right\rfloor,\qquad
\eta_m=e^{-6d_m^4}.
\tag{1.1}
$$

对每个整数 $4d_m\le Q\le Q_m^{\max}$，原带权窗口的同一证明给真正物理投影

$$
u_{m,Q}=P_{V_{m,Q}}w-P_{K_{m,Q}}w,
\tag{1.2}
$$

并且一致有

$$
\|u_{m,Q}\|\le\|w\|,\qquad
u_{m,Q}\perp K_{m,Q},\qquad
\|u_{m,Q}-P_{\mathcal N^{(m)}\le Q}w\|
 \le2\eta_m\|w\|.
\tag{1.3}
$$

这些结论不是只对最大值 $Q=Q_m^{\max}$ 成立。因此可以在既定范围内选择每个 $m$ 的一个 $Q$，随后在该窗口所有 cut 上继续使用同一个 (1.2)。

令 $R_m$ 为并入头部的强物理位数，置

$$
x_m=m+R_m,\qquad h_m=d_m+R_m,\qquad
C_m=A_m+D_{[m,m+R_m)},\qquad
D_m^>=D_{[m+R_m,\infty)}.
\tag{1.4}
$$

这里 $x_m$ 是远尾的首指标规范，$C_m^{h_m}=0$。本稿假设

$$
h_m\longrightarrow\infty,\qquad
\sup_{m\text{ 足够大}}\frac{h_m}{x_m}<\infty,\qquad
\mathcal A_m:=\frac{Q_m^{\max}}{h_m^2}\longrightarrow\infty.
\tag{1.5}
$$

例如原逆芽选择
$R_m=\lceil c_0e^{25d_m^3/2}\rceil$、固定 $c_0>1$，满足

$$
h_m/x_m\to1,\qquad
\mathcal A_m\sim c_0^{-2}e^{d_m^3/64}\to\infty.
\tag{1.6}
$$

仅对本稿的纯负二次型转换，已经可取 $R_m=d_m$；此时
$h_m=2d_m$、$x_m=m+d_m$、$h_m/x_m\to2$ 且 $\mathcal A_m\to\infty$，固定二次尺度窗口为
$Q_m\sim4L_0d_m^2$。较大的 $R_m=d_m^2$ 也满足 (1.5)。这些选择不使用逆芽半径，也不能据此调用另外要求
$\|D_m^>\|<\rho_m$ 的解析变换。

若某个后继变换采用更大的 $R_m$，只要重新核实 (1.5)，同样适用。当前条件转换不自动扩大旧 joint-flag 小常数的窗口，也不使用该额外小常数。

设置同一个与 $Q$ 无关的低端

$$
a_m=4h_m,\qquad
\beta_m=
\|\mathbf1_{\{\mathcal N_{\rm all}>4h_m\}}w\|
+2\eta_m\|w\|.
\tag{1.7}
$$

由于 $w$ 是固定 Hilbert 向量、$h_m\to\infty$，有 $\beta_m\to0$。这里的 $\mathcal N_{\rm all}$ 是全部物理位的总孔数；不把远孔数与原总尾孔数当成同一个截断。

## 2. 同一个 $u_{m,Q}$ 的准确合并负二次型

以下省略下标 $m$，记 $u=u_{m,Q}$，$u_n$ 为它的第 $n$ 个远孔分量。取

$$
a=4h,\qquad b=Q-R-h-1,\qquad
N_{\rm cut}=b-a+1=Q-R-5h>0.
\tag{2.1}
$$

每个 $a\le p\le b$ 均满足 $p+h+R<Q$，所以原全部自然旗、真实最小性及完整右封口在同一个顶部上成立。特别，若 $r_p=Cu_p$，则

$$
\mu_p(r_p)=\|P_{\mathcal N_>\le p}u\|
 \ge\|w\|-\beta_m.
\tag{2.2}
$$

在第 $n$ 个真实固定层上，令

$$
P_{n,j}
=(D_n^\dagger D_{n-1}^\dagger\cdots D_{n-j+1}^\dagger)D^j,
\qquad 1\le j\le h,
$$

并记包含两端部分和的完整算子

$$
\mathscr A_{n;m,Q}
=\sum_{\substack{1\le j\le h\\a\le n-j\le b}}P_{n,j}.
\tag{2.3}
$$

这里 $D=D_m^>$，每个 $P_{n,j}$ 在实际 $E_{h,n}=\ker D^h\cap\mathcal H_n^>$ 上读取。顺次单步 MP 与真幂 MP 没有被交换。

已付同源标量恒等式准确给

$$
\boxed{
\mathcal L_{m,Q}(u)
:=-\sum_{n=a+1}^{b+h}
 \operatorname{Re}\langle\mathscr A_{n;m,Q}u_n,u_n\rangle
=\sum_{p=a}^b\mu_p(r_p)^2.
}
\tag{2.4}
$$

由 (1.3)、(1.7) 还有

$$
\sum_{n=a+1}^{b+h}\|u_n\|^2
\le\|P_{\mathcal N_> >4h}u\|^2\le\beta_m^2.
\tag{2.5}
$$

若 $w=0$，待证结论已经成立；在 $w\ne0$ 时，以下只取充分大的 $m$，使 $\beta_m\le\|w\|$，因而 (2.2) 可以平方取下界。若在这个同一来源上证明

$$
\mathcal L_{m,Q}(u)\le M_{m,Q}\,\beta_m^2,
\tag{2.6}
$$

则必有

$$
\boxed{
N_{\rm cut}(\|w\|-\beta_m)^2
\le M_{m,Q}\beta_m^2.
}
\tag{2.7}
$$

一个充分而较强的输入，是对全部实际 (2.3) 给
$(\operatorname{Re}\mathscr A_{n;m,Q})_-\preceq M_{m,Q}I$；
但 (2.6) 本身只需原同一个 $u_{m,Q}$ 的联合二次型。若只分别估计每个 $P_{n,j}$，不能省掉随后可能出现的 $h$ 倍费用。也不能删除 (2.3) 两端的部分和。

## 3. 一个固定二次尺度已经足够

**条件定理。** 假设对某个固定 $L_0>0$，取

$$
Q_m=\lfloor L_0h_m^2\rfloor,
\tag{3.1}
$$

后，在所有充分大的 $m$ 上有同源估计

$$
\mathcal L_{m,Q_m}(u_{m,Q_m})
\le C_{L_0}\,Q_m\,\beta_m^2
\tag{3.2}
$$

其中 $C_{L_0}<\infty$ 不依赖 $m$。则 $w=0$。

**证明。** 由 (1.5)，充分大时 (3.1) 在原区间
$4d_m\le Q_m\le Q_m^{\max}$ 内。又 $R_m\le h_m$，所以

$$
\frac{N_{\rm cut}}{Q_m}
=1-\frac{R_m+5h_m}{Q_m}\longrightarrow1.
$$

将 (3.2) 代入 (2.7)，除以 $Q_m$，再用 $\beta_m\to0$，即得
$\|w\|^2\le0$。证毕。

特别，若尚待证明的负部预算只达到

$$
\boxed{
M_{m,Q}\le C\,\frac{Q^2}{x_m^2}
}
\tag{3.3}
$$

且它在 (3.1) 的一个固定 $L_0$ 曲线上成立，仍然已经足够。确实，

$$
\frac{M_{m,Q_m}}{Q_m}
\le C\,\frac{Q_m}{x_m^2}
\le C L_0\left(\frac{h_m}{x_m}\right)^2,
\tag{3.4}
$$

右侧由 (1.5) 有界。

因此当前负部转换不要求先在整个最大窗口内证明统一 $O(Q)$，也不要求
$h_m^2/Q_m\to0$。它只需要 $h_m/Q_m\to0$，而固定正 $L_0$ 的 (3.1) 已满足。式 (3.3) 在本文仍是假设，未由单权泄漏、独立 primitive Gram 或普通条件数推出。

## 4. 同一 $w$ 上慢选 $L_m\to\infty$ 的明确方式

若另一个后继接口还要求 $h_m^2/Q_m\to0$，也可同时保留 (3.3) 的充分性。

$w=0$ 时结论无须讨论。对 $w\ne0$，令

$$
\varepsilon_m=\frac{\beta_m}{\|w\|}>0,\qquad
L_m=\min\{\sqrt{\mathcal A_m},\,\varepsilon_m^{-1}\},
\qquad Q_m=\lfloor h_m^2L_m\rfloor.
\tag{4.1}
$$

由 (1.5)、(1.7)，$L_m\to\infty$。充分大时 $\mathcal A_m\ge1$，且

$$
Q_m\le h_m^2\sqrt{\mathcal A_m}
\le Q_m^{\max},\qquad Q_m\ge4d_m.
\tag{4.2}
$$

同时

$$
\frac{Q_m}{h_m^2}=L_m+O(h_m^{-2})\to\infty,\qquad
L_m\varepsilon_m^2\le\varepsilon_m\to0.
\tag{4.3}
$$

所以 (3.3) 若在这个允许的所选窗口中成立，则

$$
\frac{M_{m,Q_m}}{Q_m}\beta_m^2
\le C\left(\frac{h_m}{x_m}\right)^2L_m\beta_m^2
\longrightarrow0.
\tag{4.4}
$$

结合 (2.7) 仍得 $w=0$。

这次 $Q_m$ 的选择可以依赖固定的 $w$。原证明本来就是对一个假定存在的
$w\in W$ 作矛盾；(1.3) 对全部允许 $Q$ 一致，故选择合法。选定后，每个 $m$ 的所有 cut 都使用这同一个 $u_{m,Q_m}$，并未按 cut 重选来源，也未要求未知的尾收敛速率。

## 5. 任意有限的固定尺度常数：慢对角选择

更一般地，设对每个正整数 $\ell$ 存在有限的 $C_\ell$ 和门槛 $m_\ell$，使

$$
Q=\ell h_m^2,\quad m\ge m_\ell
\quad\Longrightarrow\quad
\mathcal L_{m,Q}(u_{m,Q})\le C_\ell Q\beta_m^2,
\tag{5.1}
$$

只要该 $Q$ 在原允许区间内。这里不要求预先给 $C_\ell$ 关于 $\ell$ 的任何增长界。

固定 $\ell$ 本身已由第 3 节足以推出 $w=0$。若还需同时使 $\ell$ 变大，可选严格递增的整数 $M_\ell$，令对所有 $m\ge M_\ell$ 都有

$$
m\ge m_\ell,\qquad
\mathcal A_m\ge\ell^2,\qquad
C_\ell\varepsilon_m^2\le\ell^{-1}.
\tag{5.2}
$$

每个 $M_\ell$ 存在，分别由原门槛、$\mathcal A_m\to\infty$ 和
$\varepsilon_m\to0$ 保证。再令 $\ell_m$ 是满足 $M_\ell\le m$ 的最大 $\ell$，并置

$$
Q_m=\ell_m h_m^2.
\tag{5.3}
$$

于是 $\ell_m\to\infty$，(5.2) 给 $Q_m\le Q_m^{\max}$，并且

$$
\frac{h_m^2}{Q_m}=\ell_m^{-1}\to0,\qquad
C_{\ell_m}\beta_m^2\le\frac{\|w\|^2}{\ell_m}\to0.
\tag{5.4}
$$

故 (2.7) 再次给矛盾。这是同一个 $w$ 上的真实慢对角选择，不是把逐个固定 $\ell$ 的极限未经证明地交换成任意增长窗口。

## 6. 准确的研究门槛

本稿把当前实际负部问题收窄为以下足够输入之一：

1. 在某一个固定 $Q/h_m^2=L_0>0$ 曲线上，合并负二次型满足
   $\mathcal L_{m,Q}(u)\le C_{L_0}Q\beta_m^2$；
2. 在所需窗口上有 $M_{m,Q}\le C Q^2/x_m^2$，再用第 3 或第 4 节；
3. 若另有接口要求 $h_m^2/Q_m\to0$，先付每个固定尺度的真实常数，再用第 5 节。

以上全部保留原 $w$、真正 $u_Q$、完整连续尾、同源多层和两端部分和。本文没有证明这些负部估计，没有把普适 $b_{\max}^2$ 泄漏界当成可用输入，也没有由窗口选择消除真正 Schur 返回。原 $N=M$ 与普通 ISP 继续开放。
