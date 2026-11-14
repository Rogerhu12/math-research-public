# R165：限制交织的精确小集集中范数与 Orlicz 提升障碍

日期：2026-11-12。作者：l2_moments。
状态：完整证明。这是 R163 高位块机制的短加强，不是新的核排除定理。
根代理预留 R165；可作为 R163 的独立附录阅读。

## 1. 任意小测度上仍保留全部算子范数

设 $M\subseteq H=L^2(\mathbb Z_2,\mu)$ 为闭 $A$ 不变空间，
$B:M\to H$ 有界，且 $BA|_M=AB$。
对 $0<\delta\le1$，定义
$$
\omega_B(\delta)
=\sup_{\mu(E)\le\delta}\|1_EB\|_{B(M,H)}.
\tag{1.1}
$$

**定理1.1。**
$$
\boxed{\omega_B(\delta)=\|B\|\quad(0<\delta\le1).}
\tag{1.2}
$$
特别，非零 $B$ 的 $L^2$ 单位球像从不一致平方可积。

**证明。** 上界显然。
固定非零 $x\in M$，并选整数 $r$ 使 $2^{-r}\le\delta$。
令
$$
J_m=\{m,\ldots,m+r-1\},\qquad
F_m=\prod_{j\in J_m}N_j,
$$
$P_m$ 为物理位 $J_m$ 全为1的柱投影，测度为 $2^{-r}$。
R163 的实际高位引理给，对每个固定 $h\in H$，
$$
F_mh-P_mh\to0,\quad
\|F_mh\|_2\to2^{-r/2}\|h\|_2,\quad
\|P_mF_mh\|_2\to2^{-r/2}\|h\|_2.
\tag{1.3}
$$
其完整依据是
$\|\prod N_j-\prod E_j\|\le\sum_{j\in J_m}\eta_j\to0$，
及对固定有限柱函数 $\prod E_jh=P_mh$，
再用范数不超过1的算子和 $L^2$ 密度。

由于 $F_m$ 是 $A$ 的多项式，$F_mx\in M$，且
$BF_mx=F_mBx$。
充分大 $m$ 时 $F_mx\ne0$，所以
$$
\omega_B(\delta)\ge
\frac{\|P_mBF_mx\|_2}{\|F_mx\|_2}
=
\frac{\|P_mF_mBx\|_2}{\|F_mx\|_2}.
$$
先固定 $r$ 再令 $m\to\infty$，由 (1.3) 得
$$
\omega_B(\delta)\ge\frac{\|Bx\|_2}{\|x\|_2}.
$$
最后对 $x$ 取上确界，即得 (1.2)。
$P_m$ 只用于输出，不要求保持 $M$。证毕。

这里对每个给定 $\delta$ 已经得到精确等式，
没有把未知向量的尾速率当作一致估计。

## 2. 与一致平方可积算子的精确距离

令 $\mathfrak U_2(M,H)$ 为所有有界线性 $C:M\to H$ 中满足
$$
\lim_{\delta\downarrow0}\omega_C(\delta)=0
\tag{2.1}
$$
的那些算子。
这等价于其单位球像满足
$$
\sup_{\|x\|_2\le1}\int_E|Cx|^2\,d\mu\longrightarrow0
\quad\text{当 }\mu(E)\to0.
$$
该类是一个范数闭线性子空间；这由
$\omega_{C+D}\le\omega_C+\omega_D$ 和
$\omega_C(\delta)\le\omega_D(\delta)+\|C-D\|$
直接得到。不需要把它称为对任意左复合稳定的算子理想。

由 (1.2)，对任意 $C\in\mathfrak U_2(M,H)$，
$$
\|B-C\|\ge\omega_B(\delta)-\omega_C(\delta)
=\|B\|-\omega_C(\delta).
$$
令 $\delta\downarrow0$，得到
$$
\boxed{
\|B-C\|\ge\|B\|,\qquad
\operatorname{dist}(B,\mathfrak U_2(M,H))=\|B\|.
}
\tag{2.2}
$$
上界取 $C=0$。

每个紧算子都在 $\mathfrak U_2$：
其单位球像在 $H$ 中相对紧，用有限个 $L^2$ 函数的逼近和积分绝对连续性即可。
所以 (2.2) 包含 R114 的本质范数等于范数结论。

但 $\mathfrak U_2$ 严格大于紧算子类。
例如在全 $H$ 上，投影到全部第一 Walsh chaos 的正交投影 $Q_1$
是无限秩且不紧；
Rademacher 四阶矩给 $\|Q_1x\|_4\le\sqrt3\|x\|_2$，
所以
$$
\|1_EQ_1x\|_2\le\mu(E)^{1/4}\sqrt3\|x\|_2.
$$
故 $Q_1\in\mathfrak U_2$。
它当然不与实际 $A$ 交换；这里仅用它区分两个算子类。

因此本结论不只是重述紧性障碍。
不过其证明是 R163 同一高位集中机制的直接加强，
并不提供额外的核方程估计。

## 3. 一般 Banach 函数空间提升

设 Banach 函数空间 $\mathscr X$ 连续嵌入 $H$，并满足
$$
\lim_{\delta\downarrow0}
\sup_{\substack{\|f\|_{\mathscr X}\le1\\\mu(E)\le\delta}}
\|1_Ef\|_2=0.
\tag{3.1}
$$
若 $\operatorname{Ran}B\subseteq\mathscr X$，
则把 $B$ 视作 $M\to\mathscr X$ 的映射时图闭：
$\mathscr X$ 收敛推出 $H$ 收敛，再用原来的有界 $B:M\to H$。
闭图定理给
$\|Bx\|_{\mathscr X}\le C\|x\|_2$。
于是 (3.1) 使 $B\in\mathfrak U_2$。
结合 (1.2)，
$$
\boxed{\operatorname{Ran}B\subseteq\mathscr X\Longrightarrow B=0.}
\tag{3.2}
$$
这只用集合包含，未额外假定提升后的算子范数界。

## 4. 任意慢的超二次 Orlicz 类

令 $\Phi$ 为有限值 Young 函数，并假设
$$
\boxed{\frac{\Phi(t)}{t^2}\longrightarrow\infty\quad(t\to\infty).}
\tag{4.1}
$$
取其 Luxemburg 范数的 Banach Orlicz 空间 $L^\Phi$。
它连续嵌入 $L^2$。
确切地，对每个 $\varepsilon>0$，可选 $T$ 使
$t^2\le\varepsilon\Phi(t)$ 对 $t\ge T$ 成立。
若 $\|f\|_\Phi\le1$，Luxemburg 定义与 Fatou 给
$\int\Phi(|f|)\,d\mu\le1$，所以
$$
\int_E|f|^2\,d\mu
\le T^2\mu(E)+\varepsilon.
\tag{4.2}
$$
先取小 $\varepsilon$，再取小 $\mu(E)$，即得 (3.1)；
取 $E$ 为全空间也给连续嵌入的有限常数。

因此
$$
\boxed{
\operatorname{Ran}B\subseteq L^\Phi,\quad
\Phi(t)/t^2\to\infty
\quad\Longrightarrow\quad B=0.
}
\tag{4.3}
$$
它覆盖比任意固定 $L^{2+\varepsilon}$ 弱得多的提升。

例如令 $\ell:[0,\infty)\to[1,\infty)$ 连续、不减且趋于无穷，
速度可任意慢，并定义
$$
\Phi(t)=\int_0^t2s\ell(s)\,ds.
\tag{4.4}
$$
其导数 $2t\ell(t)$ 不减，所以 $\Phi$ 为 Young 函数，
而
$$
\frac{\Phi(t)}{t^2}\ge\frac34\ell(t/2)\longrightarrow\infty.
$$
可以取 $\ell(s)=\log\log(e^e+s)$，
或任意更慢的不减无穷增长函数。
不需要对 $\Phi$ 作 $\Delta_2$ 假设；
Luxemburg 范数与上面的单位球估计已经足够。

## 5. 固定目标空间与单个向量的区别

(4.3) 排除的是一个固定 Orlicz 目标空间，
或单位球上的一致平方可积性。
它不能被改写成“每个非零输出不属于任何更小 Orlicz 类”。

事实上，每个给定 $h\in L^2$ 都属于某个满足 (4.1) 的 Orlicz 空间。
可自含构造如下：
选 $T_n\uparrow\infty$，使
$$
\int_{\{|h|>T_n\}}|h|^2\,d\mu\le2^{-n}.
$$
取一个连续不减、趋于无穷的 $\ell$，
在各个阈值之间缓慢上升，并满足
$$
1\le\ell(t)\le2+\sum_{n\ge1}1_{\{t>T_n\}}.
$$
则
$$
\int |h|^2\ell(|h|)\,d\mu
\le2\|h\|_2^2+\sum_{n\ge1}2^{-n}<\infty.
$$
以 (4.4) 定义 $\Phi$，有
$\Phi(t)\le t^2\ell(t)$，故 $\int\Phi(|h|)<\infty$，
而仍满足 (4.1)。

所以，目标 Orlicz 函数若允许随每个单独向量任意改变，
本稿没有产生矛盾。
同样，它不排除某个特别的核向量偶然具有高可积性。

## 6. 当前核问题的准确接口

若未来由真实核方程证明：
某个候选闭不变核 $M$ 上存在非零有界交织 $B$，
且其单位球像一致平方可积，
或 $BM$ 包含于一个固定的 (4.1) Orlicz 空间，
那么本稿将直接迫使 $M=0$（或迫使该交织为零）。

R161 已给共振核上的通常伴随同域、
$X|_M$ 与 $X^*|_M$ 有界，以及压缩自交换子正性。
这些是有用的算子域和二次型约束，
但尚未证明 (3.1) 或任何固定 Orlicz 提升。
不能把有界自交换子误认为点态函数可积性，
也不能用未知向量的尾速率补足这一缺口。

所有有限放大版本都成立：对 $H^{\oplus d}$ 的不变 $M$ 与
$B:M\to H^{\oplus s}$，使用点态欧氏范数和共同物理柱，
(1.3) 各分量相加后原样适用。
完整 ISP 及一般慢共振核仍未解决。


## 7. 实际模型中超小近似交织误差仍不够

本节给一个与主定理相容、但会阻止常见近似推理的实际构造。
令 $\mathbb E_m$ 为 $L^2$ 到低 $m$ 位函数的条件期望：
$$
\mathbb E_m:H\longrightarrow H_{[0,m)}.
$$
它是秩 $2^m$ 的正交投影，
不是一个有限局部矩阵张量尾恒等的 UHF 算子。
有
$$
\mathbb E_m\longrightarrow I\quad\text{强收敛},\qquad
\|\mathbb E_m\|_{L^2\to L^\infty}=2^{m/2}.
\tag{7.1}
$$
后一个等式由每个测度 $2^{-m}$ 柱上的 Cauchy–Schwarz 得上界，
取归一化柱指示函数取到。

把实际 $A$ 在输出 $2^m\mathbb Z_2$ 上的权删掉，
得到 R9/R44 的有限链截断
$$
A_m=J_m\otimes I_{\rm tail},\qquad A_m^{2^m}=0.
$$
其误差精确为
$$
\boxed{\|A-A_m\|=\alpha_m.}
\tag{7.2}
$$
因为被删的权在该柱上的本质上确界是 $\alpha_m$，
并在赋值恰为 $m$ 的正测度子柱上取到。

$\mathbb E_m=I_{\rm head}\otimes|\Omega_{\rm tail}\rangle
\langle\Omega_{\rm tail}|$ 与 $A_m$ 交换，
所以
$$
\boxed{\|[\mathbb E_m,A]\|\le2\alpha_m.}
\tag{7.3}
$$
这个误差随 $m$ 超快趋零。
因此对任何闭 $A$ 不变 $M$，
$\mathbb E_m|_M$ 都是有界到有限柱、从而到 $L^\infty$ 的正则化，
并满足
$$
\|\mathbb E_m A|_M-A\mathbb E_m|_M\|\le2\alpha_m.
\tag{7.4}
$$
它们还在 $M$ 上逐向量强逼近恒等包含。

但是固定 $m$ 后，归一化高位的交织缺陷没有趋零。
对任意固定 $x\in H$，
$N_j\rightharpoonup I/2$ 于弱算子拓扑，而 $\mathbb E_m$ 有限秩，所以
$$
\mathbb E_mN_jx\longrightarrow\tfrac12\mathbb E_mx
\quad\text{于 }H.
\tag{7.5}
$$
当 $j\ge m$ 时，$\mathbb E_mx$ 不依赖第 $j$ 位，因此
$$
E_j\mathbb E_mx=\tfrac12(I-M_{\chi_j})\mathbb E_mx.
$$
再用 $\|N_j-E_j\|=\eta_j\to0$，得到准确强渐近
$$
\boxed{
[\mathbb E_m,N_j]x
=\tfrac12\chi_j\,\mathbb E_mx+o_H(1)
\quad(j\to\infty,\ m\text{ 固定}).
}
\tag{7.6}
$$
这里交换子约定为 $\mathbb E_mN_j-N_j\mathbb E_m$，
所以右侧的符号是正号。
因 $|\chi_j|=1$，
$$
\lim_{j\to\infty}\|[\mathbb E_m,N_j]x\|_2
=\tfrac12\|\mathbb E_mx\|_2.
\tag{7.7}
$$

先固定 $x\in M$、$\|x\|=1$，再对固定向量的下界取上确界，给
$$
\boxed{
\liminf_{j\to\infty}
\|[\mathbb E_m,N_j]|_M\|
\ge\tfrac12\|\mathbb E_m|_M\|.
}
\tag{7.8}
$$
若 $M\ne0$，取其中一个单位向量并用 (7.1)，得到
$$
\|\mathbb E_m|_M\|\longrightarrow1.
\tag{7.9}
$$
所以 (7.3)—(7.4) 的超小 $A$-交织误差，
与归一化高位测试上接近 $1/2$ 的持续缺陷同时存在。

这不是一个抽象反例，而是本题实际 $A$、实际归一化幂与实际有限柱正则化。
它说明仅有极小的 $\|BA|_M-AB\|$，
即使误差达到 $\alpha_m$ 的超快尺度，
仍不能把 R163 或本稿的精确交织结论用于 $B$。
从 $A^{2^j}$ 改用 $N_j=A^{2^j}/W_{2^j}$ 时，
极小分母不能未经估计直接取消。
本节没有证明这些 $\mathbb E_m$ 保持未知 $M$；
把它们当作 $M\to H$ 的近似交织已经足够给出上述严格障碍。
