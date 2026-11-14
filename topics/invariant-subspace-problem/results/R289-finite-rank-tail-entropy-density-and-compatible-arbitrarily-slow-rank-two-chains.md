# R289：有限秩原密度的尾熵密度零与任意慢相容秩二链

2026-11-14，normal-annihilator / 789f。**状态：以下一般结构结论和非见证例均已证明；没有构造实际正常湮灭者。**

已知入口：[R253 §4](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)已明确 $\operatorname{rank}\nu_m\le r2^m$，[R276 §7](R276-positive-head-completion-and-compact-numerical-radius-criterion.md)已把给定有限秩尾密度的本步正完成压到有限支撑。这两项不作为新结论。本文补充由同一原密度得到的熵密度零结论，以及表明任意慢的正常尾与统一很小的 Schmidt 秩、全块熵界仍相容的准确实例。最后保留实际 $Q_m$、$Z_m$ 零式的缺口。

## 1. 同一有限秩密度的尾熵必为 o(m)

归一化 $\operatorname{Tr}\rho=1$，设 $\rho\ge0$、$\operatorname{rank}\rho=r<\infty$。在原 Haar/Walsh 张量表示中置

$$
\nu_m=\operatorname{Tr}_{<m}\rho,\qquad
\Pi_m=I_{<m}\otimes|\Omega_m\rangle\langle\Omega_m|,
\qquad
\delta_m=\operatorname{Tr}\rho(I-\Pi_m).
$$

则 $\delta_m\downarrow0$，$\langle\nu_m\Omega_m,\Omega_m\rangle=1-\delta_m$，且 $\operatorname{rank}\nu_m\le R_m:=r2^m$。这里全部 $\nu_m$ 来自同一个 $\rho$，并满足真实部分迹相容性。

定义 von Neumann 熵 $\mathsf S(\nu)=-\operatorname{Tr}(\nu\log\nu)$，$0\log0=0$；令 $h_2(t)=-t\log t-(1-t)\log(1-t)$。

**命题 1.1。** 对充分大的 $m$，

$$
\boxed{\mathsf S(\nu_m)
\le h_2(\delta_m)+\delta_m\log(r2^m-1),
\qquad \frac{\mathsf S(\nu_m)}m\longrightarrow0.}
\tag{1.1}
$$

**证明。** 记最大特征值为 $\lambda_1$，$\varepsilon=1-\lambda_1$。Rayleigh 商给 $0\le\varepsilon\le\delta_m$。其余至多 $R_m-1$ 个非负特征值之和为 $\varepsilon$，由 $-t\log t$ 的凹性，

$$
\mathsf S(\nu_m)\le h_2(\varepsilon)+\varepsilon\log(R_m-1).
$$

函数 $h_2(t)+t\log(R_m-1)$ 在 $0\le t\le1-1/R_m$ 上递增。对充分大的 $m$ 有 $\delta_m\le1/2\le1-1/R_m$，故可用 $\delta_m$ 代替 $\varepsilon$。最后除以 $m$，用 $h_2\le\log2$、$\delta_m\to0$ 及 $\log R_m=\log r+m\log2$ 即得。$\square$

此证明只用真实尾真空质量和有限维谱，没有调用一个维数固定的连续性定理后忽略随 $m$ 增长的维数。它没有给 $\mathsf S(\nu_m)\to0$；第 4 节说明后者对一般有限秩原密度甚至不成立。

## 2. 任意尾缺陷由一条秩至多二的相容尾链准确实现

对 $n\ge0$ 记原 Walsh 字符

$$
w_n=\chi_{[0,n)},\qquad w_0=1.
$$

它们两两正交且范数为 $1$。给定任意非增数列

$$
0\le d_m\le d_0\le\tfrac12,\qquad d_m\longrightarrow0,
$$

取复数 $b_n$ 满足

$$
|b_0|^2=1-d_0,\qquad |b_n|^2=d_{n-1}-d_n\quad(n\ge1).
$$

定义一个原 Haar 向量和原秩一正常态

$$
f=\sum_{n\ge0}b_nw_n\in H,\qquad \|f\|=1,
\qquad \rho=|f\rangle\langle f|.
\tag{2.1}
$$

**命题 2.1。** 此同一密度满足，对所有 $m\ge0$，

$$
\boxed{\operatorname{Tr}\rho(I-\Pi_m)=d_m.}
\tag{2.2}
$$

对每个切分 $m\ge1$，$f$ 的 Schmidt 秩至多二，所以

$$
\boxed{\operatorname{rank}\nu_m\le2,
\qquad \mathsf S(\nu_m)\le h_2(d_m)\longrightarrow0.}
\tag{2.3}
$$

**证明。** $w_n$ 落在 $\operatorname{Ran}\Pi_m$ 当且仅当 $n\le m$，故 (2.2) 由系数平方和望远镜直接得到。准确头尾分解为

$$
f=h_m\otimes\Omega_m+w_m^{\rm head}\otimes g_m,
$$

$$
h_m=\sum_{n<m}b_nw_n^{\rm head},\qquad
 g_m=\sum_{n\ge m}b_n\chi_{[m,n)}.
\tag{2.4}
$$

$h_m\perp w_m^{\rm head}$，因此

$$
\boxed{\nu_m=(1-d_{m-1})|\Omega_m\rangle\langle\Omega_m|
+|g_m\rangle\langle g_m|.}
\tag{2.5}
$$

这里 $\|g_m\|^2=d_{m-1}$，$|\langle g_m,\Omega_m\rangle|^2=|b_m|^2=d_{m-1}-d_m$。非零的两个特征值（允许其中一个为零）准确为

$$
\lambda_\pm(m)=\frac{1\pm\sqrt{1-4(1-d_{m-1})d_m}}2.
\tag{2.6}
$$

也可直接用最大特征值至少 $1-d_m$ 和秩至多二，得到 (2.3)。所有边缘都从同一 (2.1) 部分迹而来，并非逐层另选。$\square$

因此即使要求每条尾边缘的秩统一不超过二、熵本身趋零，也不能得到比任意指定 $d_m\to0$ 更快的尾速度。这个例子只实现几何、正性、相容性和正常性条件；没有声称它满足任何原慢理想湮灭方程。

## 3. 任意有限连续块秩至多三，且旧能量必要界可同时满足

对任意有限连续块 $[s,t)$，按 (2.1) 的指标 $n<s$、$s\le n\le t$、$n>t$ 三组分解并对块外部分迹，准确有

$$
\rho_{[s,t)}=
\left(\sum_{n<s}|b_n|^2\right)|\Omega\rangle\langle\Omega|
+|v_{s,t}\rangle\langle v_{s,t}|
+\left(\sum_{n>t}|b_n|^2\right)|\chi_{[s,t)}\rangle\langle\chi_{[s,t)}|,
$$

$$
v_{s,t}=\sum_{n=s}^{t}b_n\chi_{[s,n)}.
\tag{3.1}
$$

三组的块外 Walsh 字符两两正交；中间一组拥有同一个块外字符，所以保留为一个秩一项。因此每个此类块的秩至多三，熵不超过 $\log3$。若 $b_0\ne0$ 且 $d_m$ 严格递减、始终正，则每个正长度块的约化态至少秩二：对 $s\ge1$，(3.1) 的第一、第三项均非零且其向量正交；对 $s=0$，$v_{0,t}$ 有非零常数项，所以不平行于第三项的全块字符。

所以 [R236 正常交叉块附录 §5 的有限连续块非纯定理](R236-appendix-positive-normal-cross-blocks-and-pure-finite-head-exclusion.md)与本例仍相容。该旧结论用于真实首形式阶一的原尾符号，要求每个正长度连续块约化态的秩至少二；它没有给离开纯态的统一距离，也没有给熵正密度。

对任意非空有限位集 $I$，记 $p=\min I$，$R_I=\prod_{i\in I}(I-Q_i^-)$。字符串 $[0,n)$ 与 $I$ 相交当且仅当 $n>p$，故准确有

$$
\boxed{\operatorname{Tr}\rho(I-R_I)=d_p.}
\tag{3.2}
$$

例如取

$$
d_p=\frac{1}{2\log(p+e)}.
\tag{3.3}
$$

它严格递减到零，$d_0=1/2$。对规范 $a_i=(i+1)^{-2}$，对全部有限 $I$ 的 [R236 高位集合能量必要下界 (1.3)](R236-appendix-uniform-high-bit-set-energy-for-normal-positive-annihilators.md)

$$
\operatorname{Tr}\rho(I-R_I)
\ge\frac{\sum_{i\in I}a_i^2}{9\cdot2^{26}}
$$

在充分高位统一成立：右侧至多常数乘 $p^{-3}$，而 $d_p\asymp1/\log p$。所引旧定理的阈值 $p_0$ 只依原行和 carry，不依 $I$ 的跨度、态或秩；本例满足该数值不等式也只需再取一个与 $I$ 跨度无关的充分大阈值。

[原多项式柱尾定理 (1.2)](R236-appendix-polynomial-cylinder-tail-for-all-normal-positive-annihilators.md)在规范 $a_-=A=1$ 时要求 $\delta_p\ge1/(9\cdot2^{30}p^3)$（$p$ 超过其模型阈值）；本例的 $\delta_p=d_p$ 也在充分大的 $p$ 上满足这一精确必要界。

该向量的系数平方为 $d_{n-1}-d_n\asymp1/(n\log^2n)$。准确地区分两个量。最高位置算子定义为

$$
\mathsf M\chi_F=(1+\max F)\chi_F\quad(F\ne\varnothing),\qquad
\mathsf M\chi_\varnothing=0.
$$

在 $w_n$ 上它取值 $n$，所以本例 $\operatorname{Tr}(\rho\mathsf M^3)=\sum_{n\ge1}n^3|b_n|^2=\infty$，与[同一柱尾稿 §6 的临界三次最高位置矩必要发散](R236-appendix-polynomial-cylinder-tail-for-all-normal-positive-annihilators.md)相容。

另外，对于每个指数参数 $R>1$，本例的 **指数 Walsh 次数矩** 为

$$
\mathcal E_R(\rho)=\sum_F R^{2|F|}\langle\rho\chi_F,\chi_F\rangle
=\sum_{n\ge0}R^{2n}|b_n|^2=\infty.
$$

这特指指数权 $R^{2|F|}$，不是把“正指数”用作任意正幂 $|F|^s$ 的简称。[R255 正常态排除定理 B 的已证阈值](R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)是 $R=\sqrt3$（及更大 $R$）；实际非零正见证必须 $\mathcal E_{\sqrt3}(\rho)=\infty$。本例自行算得的所有 $R>1$ 发散比满足这个必要后果更强，不声称旧排除定理已覆盖 $1<R<\sqrt3$。它仍是原秩一正常态，全块熵界 $\log3$ 和尾熵趋零同时成立。

这些比较并不证明它满足其他已证湮灭必要条件，更不证明它是实际见证。要排除此例必须使用原 $Q_m\mathcal B_m$ 零式或更强的真实结构，不能只并列上述尾、秩、熵及有限块非纯条件。

## 4. 一般有限秩原密度的尾熵可以无界

命题 1.1 的 $o(m)$ 不能普遍加强为熵趋零，甚至不能加强为尾熵有界。给出一个原秩一例子。

取彼此不交、依次排列的有限位块，每块由一个标记位 $a_n$、长度 $L_n$ 的左段和长度 $L_n$ 的右段组成。令

$$
\psi_n=2^{-L_n/2}\sum_{F\subseteq\{1,\ldots,L_n\}}
\chi_{\{a_n\}\cup F^{\rm left}\cup F^{\rm right}}.
\tag{4.1}
$$

不同 $\psi_n$ 及 $\Omega$ 两两正交。置

$$
p_n=2^{-n-1},\quad L_n=4^n\quad(n\ge1),\qquad
f=\sqrt{1-\sum_np_n}\,\Omega+\sum_n\sqrt{p_n}\,\psi_n.
\tag{4.2}
$$

这是原 $H$ 中的单位向量，$\rho=|f\rangle\langle f|$ 仍秩一。令 $m_n$ 是第 $n$ 块左右段之间的切点，$D_n=2^{L_n}$。

对每个非空 $F\subseteq\{1,\ldots,L_n\}$，尾向量 $\chi_{F^{\rm right}}$ 是 $\nu_{m_n}$ 的特征向量，特征值准确为 $p_n/D_n$。原因是第 $n$ 块在头部的 $D_n$ 个带标记字符两两正交，也与所有较早块及头真空正交；较晚块的尾字符只使用更远位，与这些非空右段字符正交。

因此

$$
\mathsf S(\nu_{m_n})
\ge p_n(1-D_n^{-1})\log(D_n/p_n)
\ge p_n(1-D_n^{-1})L_n\log2\longrightarrow\infty.
\tag{4.3}
$$

而 $m_n\asymp L_n$，所以此下界只是约 $\sqrt{m_n}$，与普遍的熵密度零没有矛盾。正常尾缺陷仍趋零。

## 5. 对实际正头完成接口的剩余任务

一般有限秩原见证除 R253、R276 的实际方程外，现在可再要求 (1.1)。但第 2–3 节给出同一原秩一密度的完整相容链，表明旧能量、非纯、秩和熵条件本身不能相互矛盾。

尚须从真实零式

$$
\nu_{m+1}(Z_m^2-t_m)\in\mathcal N_{m+1},\qquad
\nu_{m+1}Z_m+X_m+X_m^*t_m\in\mathcal N_{m+1}
$$

导出独立的支撑或熵增长，或者给出某一步正距离证书。这里 $\mathcal N_{m+1}$ 内的非零缺陷不允许删去，$Z_m$ 及其真实单位规范化的移动费用仍须保留。本文没有从固定秩、低熵或全链相容性跨越这一步。
