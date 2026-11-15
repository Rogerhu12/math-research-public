# R271 附录：同一缺陷向量的跨头正交孔带与可发散倒数的负部费用

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root 与 boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：已证明的条件转换及同源跨头平方和。本文进一步放宽合并负部所需的增长门槛：在一个固定二次尺度上，费用可以比 $Q$ 大一个 $O(\log Q\log\log Q)$ 因子，只要相应倒数沿头参数的和发散。证明使用同一个 $w$ 的互不相交全物理孔带，不要求未知尾范数满足某种速率。所需实际负部估计本身仍未证明；$N=M$ 与普通 ISP 继续开放。

依赖：

- [真正最小投影的带权窗口](R271-appendix-true-minimal-projection-weighted-window.md)；
- [强物理尾位并头的同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
- [同顶部顺次投影负二次型](R271-appendix-same-top-sequential-projection-negative-form-and-complete-return-scalar.md)；
- [固定二次尺度与自适应慢窗口](R271-appendix-fixed-parabolic-and-adaptive-slow-windows-for-the-actual-negative-form.md)。

## 1. 全部头参数使用同一个原向量

固定原 $N/Y$ 模型之一及 $w\in W=M\ominus N$。记 $\mathcal N_{\rm all}$ 为全部物理位的总孔数；这是以下不同 $m$ 之间共同的物理观测，不随头尾分组改变。

固定一个 $L_0>0$。对充分大的整数 $m$ 取

$$
d_m=2^m,\qquad R_m=d_m,\qquad
h_m=d_m+R_m=2d_m,\qquad x_m=m+d_m,
$$

$$
Q_m=\lfloor L_0h_m^2\rfloor,\qquad
\eta_m=e^{-6d_m^4}.
\tag{1.1}
$$

于是 $h_m/x_m\to2$，且 $Q_m$ 最终落在已经支付的原窗口

$$
4d_m\le Q_m\le
\left\lfloor e^{(25+1/64)d_m^3}\right\rfloor.
\tag{1.2}
$$

本稿不使用逆芽或 Riordan 变换，不把 $R_m=d_m$ 用于另外要求远尾范数小于逆芽半径的结论。

记 $\mathcal N^{(m)}$ 为从第 $m$ 位起的原总尾孔数，$\mathcal N_>^{(m)}$ 为从第 $m+R_m$ 位起的远孔数。取原真正顶部

$$
u_m=P_{V_{m,Q_m}}w-P_{K_{m,Q_m}}w.
\tag{1.3}
$$

原投影结论给

$$
\|u_m\|\le\|w\|,\qquad
u_m\perp K_{m,Q_m},\qquad
\|u_m-P_{\mathcal N^{(m)}\le Q_m}w\|
\le2\eta_m\|w\|.
\tag{1.4}
$$

这里没有按 cut 或按远孔层重选顶部。不同 $m$ 的 $u_m$ 也都由同一个 $w$ 产生。

有限联块及连续远尾准确为

$$
C_m=A_m+\sum_{m\le i<m+R_m}b_iE_i,\qquad
D_m^>=\sum_{i\ge m+R_m}b_iE_i,\qquad
b_i=(i+1)^{-2},\qquad C_m^{h_m}=0.
\tag{1.5}
$$

只作物理张量分组，不把 $C_m$ 改成 $A_{m+R_m}$。

## 2. 晚 cut 的未来落在互不相交的全物理孔带

置

$$
a_m=\lfloor Q_m/2\rfloor,\qquad
b_m=Q_m-R_m-h_m-1,
$$

$$
I_m=\{p:a_m\le p\le b_m\},\qquad
n_m^{\rm cut}=|I_m|
=Q_m-R_m-h_m-\lfloor Q_m/2\rfloor.
\tag{2.1}
$$

固定 $L_0$ 时 $Q_m/h_m\to\infty$，故这些区间最终非空，且

$$
\frac{n_m^{\rm cut}}{Q_m}\longrightarrow\frac12.
\tag{2.2}
$$

每个 $p\in I_m$ 都满足 $p+h_m+R_m<Q_m$，原完整源流、自然旗和封口均适用。

定义这个窗口实际使用的未来投影

$$
F_m=\mathbf1_{\{a_m<\mathcal N_>^{(m)}
                  \le b_m+h_m\}}
=\mathbf1_{\{a_m<\mathcal N_>^{(m)}
                  \le Q_m-R_m-1\}}.
\tag{2.3}
$$

$F_m$ 本身随 $m$ 改变。但在它的物理像内，原强块孔数至多 $R_m$，前 $m$ 位的物理孔数至多 $m$。所以准确有

$$
F_m\le P_{\mathcal N^{(m)}\le Q_m-1},
\qquad
F_m\le
B_m^{\rm band}:=
\mathbf1_{\{a_m+1\le\mathcal N_{\rm all}\le Q_m+m-1\}}.
\tag{2.4}
$$

两个包含都是原正交物理孔投影的包含；没有用一个非正交头变换替代物理支撑。

由 $h_{m+1}^2=4h_m^2$ 和取整，

$$
Q_{m+1}\ge4Q_m,\qquad
a_{m+1}\ge2Q_m.
\tag{2.5}
$$

当 $Q_m>m-1$ 时，前一个全物理带的上端 $Q_m+m-1$ 严格低于下一个带的下端 $a_{m+1}+1$。所以取充分大的固定 $m_0$ 后，所有 $B_m^{\rm band}$，$m\ge m_0$，两两正交。由 (2.4)，实际 $F_m$ 也两两正交。因此

$$
\boxed{\sum_{m\ge m_0}\|F_mw\|^2\le\|w\|^2.}
\tag{2.6}
$$

这一步不要求不同 $m$ 的远孔数相同；它们各自的像都已嵌入共同总孔数的互不交谱带。

## 3. 真正顶部的跨头平方和

由于 (2.4) 的第一个包含，$F_mP_{\mathcal N^{(m)}\le Q_m}=F_m$。故 (1.4) 在同一个实际未来上给

$$
\|F_m(u_m-w)\|\le2\eta_m\|w\|.
\tag{3.1}
$$

在 Hilbert 直和 $\bigoplus_{m\ge m_0}\mathcal H$ 中用三角不等式，结合 (2.6)，得到

$$
\boxed{
\left(\sum_{m\ge m_0}\|F_mu_m\|^2\right)^{1/2}
\le
\left(1+2\sqrt{\sum_{m\ge m_0}\eta_m^2}\right)\|w\|.
}
\tag{3.2}
$$

特别，右侧有限。较粗但同样充分的形式为

$$
\sum_{m\ge m_0}\|F_mu_m\|^2
\le
\left(2+8\sum_{m\ge m_0}\eta_m^2\right)\|w\|^2.
\tag{3.3}
$$

这是跨不同实际最小投影的同源预算；它没有把无速率的 $\|P_{>a_m}w\|$ 乘一个增长常数。平方可和误差来自原一致的真正投影估计。

## 4. 同一未来上的精确负二次型及下界

以下所有 $D_n$、$P_{n,j}$ 都以本节固定 $m$ 的原连续远尾 $D=D_m^>$ 定义。每个固定孔层满射，故所用单步 MP 逆有界；不假定孔层直和上的有界 $D^\dagger$。

记 $u_{m,n}=P_{\mathcal N_>^{(m)}=n}u_m$，以及

$$
P_{n,j}
=(D_n^\dagger D_{n-1}^\dagger\cdots D_{n-j+1}^\dagger)D^j,
$$

$$
\mathscr A_{m,n}
=\sum_{\substack{1\le j\le h_m\\a_m\le n-j\le b_m}}P_{n,j}.
\tag{4.1}
$$

这些算子在真实 $E_{h_m,n}=\ker D^{h_m}\cap\mathcal H_n^>$ 上读取，并在有限联块头上张量恒等。两个端点的部分和都保留。

设 $r_{m,p}=C_mu_{m,p}$。原同顶部的完整右候选与左最小性给准确身份

$$
\boxed{
\mathcal L_m:=
-\sum_{n=a_m+1}^{b_m+h_m}
 \operatorname{Re}\langle\mathscr A_{m,n}u_{m,n},u_{m,n}\rangle
=
\sum_{p\in I_m}\mu_{m,p}(r_{m,p})^2.
}
\tag{4.2}
$$

同时

$$
\sum_{n=a_m+1}^{b_m+h_m}\|u_{m,n}\|^2
=\|F_mu_m\|^2.
\tag{4.3}
$$

令

$$
\beta_m=
\|\mathbf1_{\{\mathcal N_{\rm all}>a_m\}}w\|
+2\eta_m\|w\|\longrightarrow0.
\tag{4.4}
$$

每个 $p\in I_m$ 的同一左最小代表是
$P_{\mathcal N_>^{(m)}\le p}u_m$，而 $p+R_m<Q_m$。由 (1.4) 及物理孔数包含，

$$
\mu_{m,p}(r_{m,p})\ge\|w\|-\beta_m.
\tag{4.5}
$$

若 $w\ne0$，只取足够大的 $m$ 使 $\beta_m\le\|w\|/2$，并由 (2.2) 使 $n_m^{\rm cut}\ge Q_m/3$。于是

$$
\boxed{\mathcal L_m\ge\frac{Q_m}{12}\|w\|^2.}
\tag{4.6}
$$

没有从一个可能为负的范数下界直接平方。

## 5. 倒数费用发散已经足够

**条件定理。** 假设在以上同一实际来源上，对所有充分大的 $m$ 证明

$$
\boxed{\mathcal L_m\le c_m Q_m\|F_mu_m\|^2,}
\tag{5.1}
$$

其中 $c_m>0$，并且

$$
\sum_m\frac1{c_m}=\infty.
\tag{5.2}
$$

则 $w=0$。

**证明。** 若 $w\ne0$，由 (4.6)、(5.1)

$$
\|F_mu_m\|^2\ge\frac{\|w\|^2}{12c_m}
\tag{5.3}
$$

对充分大的每个 $m$ 成立。求和后，(5.2) 使右侧发散，与已证明的 (3.2) 矛盾。证毕。

更一般地，只在某个无限头参数集合 $\mathcal M$ 上有 (5.1)，且
$\sum_{m\in\mathcal M}c_m^{-1}=\infty$，同样成立。不能把任意稀疏子序列自动视为保留倒数发散。

(5.1) 只要求同一个 $u_m$ 的联合二次型。一个充分而更强的输入是对全部相关 $n$ 证明

$$
(\operatorname{Re}\mathscr A_{m,n})_-
\preceq c_m Q_m I.
\tag{5.4}
$$

若分开估计各个 $P_{n,j}$，仍必须支付相加的真实损失；本稿没有取消一个尚未估计的 $h_m$ 因子。

## 6. 对实际原尾研究门槛的具体含义

以下费用增长都满足 (5.2)：

$$
c_m\le C,\qquad c_m\le Cm,\qquad
c_m\le C m\log(m+1).
\tag{6.1}
$$

最后一项由 $\sum 1/[m\log(m+1)]=\infty$。因
$Q_m\sim4L_0\,4^m$，它对应于允许的实际合并负部量级

$$
\boxed{
M_m=c_mQ_m
=O\!\left(Q_m\log Q_m\log\log Q_m\right).
}
\tag{6.2}
$$

所有对数只对充分大的参数使用。原 $x_m\sim h_m/2$，故若在这一固定曲线上证明

$$
M_m\le
C\,\frac{Q_m^2}{x_m^2}
 \log Q_m\log\log Q_m,
\tag{6.3}
$$

也落入 (6.2)。常数可依赖固定的 $L_0$ 和所选原模型，不随 $m$ 增长。

这里的新收益来自互不交全物理孔带上的共同 $w$，不是要求
$c_m\beta_m^2\to0$。一个一般 Hilbert 尾可能不满足后者，但它不能在无限多个互不交物理带上各承担 (5.3) 而仍有有限总范数。

本文仍未证明 (5.1)、(5.4) 或 (6.3)。尤其旧高方差估计的 birth 是这里的 $n-t$，不是短高度 $t<h_m$；在 $n\asymp Q_m\asymp h_m^2$ 的本窗口中，不能仅因 $Q_m$ 大而把低 birth 结论套到整个 $E_{h_m,n}$。真正的连续尾联合 Schur、同源高返回和合并负部仍须继续控制。本文只降低足够条件，不宣称原边界闭合。
