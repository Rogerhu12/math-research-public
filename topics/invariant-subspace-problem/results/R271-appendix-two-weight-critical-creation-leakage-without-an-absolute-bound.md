# R271 附录：两权临界池及满射弱尾扩张的第二创建泄漏没有绝对常数上界

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root 与 boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：已证明的硬核模型反例。即使全部有限临界池权都在固定区间 $[1/2,1]$，真正第二创建泄漏也不能由一个绝对常数乘最大单权的平方控制；加入一个正弱位，再加入严格正的任意小无限弱尾，可以同时保留任意大的泄漏及所需完整固定孔层的满射。本稿不把这些可选权模型当作原固定无限连续尾的下界，也不否定原实际同源两费目标。

本稿沿用[原两下降 Schur 常数、第三尾桥与可支付的短 jet 锚](R239-appendix-two-descents-third-tail-and-paid-jet-anchor.md)中第二创建泄漏的物理定义。这里的有限临界孔层不满足该文无限原尾的所有满射假设；下文因此直接使用真实投影定义，不调用其 $\Gamma_1^{-1}$ 恒等式。

## 1. 模型、物理内积和真正泄漏

固定整数 $m\ge1$、实数 $0<t<1$。取 $2m$ 个硬核位，前 $m$ 位的删除权为 $1$，后 $m$ 位的删除权为 $t$。记

$$
D=\sum_{i=1}^{m}E_i+t\sum_{i=m+1}^{2m}E_i,
\qquad
D_3=\sum_{i=1}^{m}E_i+t^3\sum_{i=m+1}^{2m}E_i.
\tag{1.1}
$$

各物理子集向量正交且归一。令 $\mathcal H_\ell$ 为第 $\ell$ 孔层，

$$
K_\ell=\ker(D|_{\mathcal H_\ell}),\qquad
E_{j,\ell}=\ker(D^j|_{\mathcal H_\ell}),\qquad
U_{j,\ell}=E_{j,\ell}\ominus E_{j-1,\ell}.
\tag{1.2}
$$

在输出孔层 $n=m+1$ 上定义真正第二下降及其伴随：

$$
B_{2,n}=P_{K_m}D|_{U_{3,n}},
\qquad
B_{2,n}^*=P_{U_{3,n}}D^*|_{K_m}.
\tag{1.3}
$$

这些都是原物理内积中的正交投影和伴随，未经过非等距的去权规范。对 primitive $x\in K_m$，逐位交换子给

$$
D^2D^*x=-2D_3x,\qquad D^3D^*x=0.
\tag{1.4}
$$

又 $D^*x\perp\ker D$，故也可把 (1.3) 写为创建列到真实二阶核的距离：

$$
B_{2,n}^*x=P_{E_{2,n}^{\perp}}D^*x.
\tag{1.5}
$$

下节证明本模型在这个临界输出层上 $E_{2,n}=\{0\}$。于是 (1.5) 的投影在这里准确等于恒等，不是对某个受限试探空间的替代。

## 2. 临界层 $D^2$ 的完整单射性

先令全部 $2m$ 个权都为 $1$，相应删除记为 $D_0$，创建为 $D_0^*$，孔数算子为 $\mathcal N$。完整物理交换子为

$$
[D_0,D_0^*]=2mI-2\mathcal N.
\tag{2.1}
$$

在中层 $\mathcal H_m$ 上，(2.1) 给

$$
\|D_0v\|=\|D_0^*v\|,
\qquad
\ker(D_0|_{\mathcal H_m})=\ker(D_0^*|_{\mathcal H_m}).
\tag{2.2}
$$

若 $y\in\mathcal H_{m+1}$ 满足 $D_0^2y=0$，置 $v=D_0y\in\mathcal H_m$。由 (2.2)，$D_0^*v=0$，从而

$$
\|v\|^2=\langle D_0y,v\rangle=\langle y,D_0^*v\rangle=0.
$$

因此 $D_0y=0$。但 (2.1) 在 $\mathcal H_{m+1}$ 上又给

$$
\|D_0y\|^2-\|D_0^*y\|^2=2\|y\|^2,
\tag{2.3}
$$

故 $y=0$。这证明 $D_0^2:\mathcal H_{m+1}\to\mathcal H_{m-1}$ 单射；两层维数相同，所以它也是双射。

对任意有限正权 $b_i$，设正对角算子

$$
Te_I=\left(\prod_{i\in I}b_i\right)e_I.
$$

则实际删除准确满足 $D=T^{-1}D_0T$，因而 $D^2=T^{-1}D_0^2T$。这里只用该可逆代数相似保持核，不把它当作等距变换。结论是

$$
\boxed{\ker(D^2|_{\mathcal H_{m+1}})=\{0\}.}
\tag{2.4}
$$

因此在 (1.1) 的原两权模型里，

$$
\boxed{B_{2,m+1}^*x=D^*x\qquad(x\in K_m).}
\tag{2.5}
$$

这里也有 $U_{2,m+1}=\{0\}$。特别不能在这个有限临界层引入一个不存在的单步 primitive 双射，或把无限原尾的 $\Gamma_1^{-1}$ 公式直接移来。

## 3. 完整群对称 primitive 源

令 $e_{k,\ell}$ 为第一组恰有 $k$ 孔、第二组恰有 $\ell$ 孔的归一群对称向量：

$$
e_{k,\ell}
=
\binom{m}{k}^{-1/2}\binom{m}{\ell}^{-1/2}
\sum_{\substack{|I\cap[1,m]|=k\\|I\cap[m+1,2m]|=\ell}}e_I.
\tag{3.1}
$$

这个子空间同时约化 $D,D^*$；其真正下降系数为

$$
De_{k,\ell}
=\sqrt{k(m-k+1)}\,e_{k-1,\ell}
+t\sqrt{\ell(m-\ell+1)}\,e_{k,\ell-1}.
\tag{3.2}
$$

取中层源

$$
\boxed{x=\sum_{k=0}^{m}(-t)^k e_{k,m-k}.}
\tag{3.3}
$$

在输出 $e_{k,m-1-k}$ 上，两项共有因子
$\sqrt{(k+1)(m-k)}$，其余系数为
$(-t)^{k+1}+t(-t)^k=0$。所以

$$
Dx=0,\qquad
\|x\|^2=\sum_{k=0}^{m}t^{2k}.
\tag{3.4}
$$

这里只以这个合法的全源向量给算子范数的下界；(2.4) 已在全部物理层证明，故没有把群对称试探逆当成完整 MP 逆。

## 4. 泄漏的精确能量和线性发散

记 $r=t^2$。实际总平方权为 $S=m(1+r)$，实际加权占据算子为

$$
W_{\mathrm{occ}}=\sum_{i\le m}n_i+r\sum_{i>m}n_i.
$$

在 $e_{k,m-k}$ 上，$W_{\mathrm{occ}}$ 的值是
$mr+(1-r)k$。由 $Dx=0$ 和 $[D,D^*]=SI-2W_{\mathrm{occ}}$，结合 (2.5) 得

$$
\boxed{
\frac{\|B_{2,m+1}^*x\|^2}{\|x\|^2}
=(1-r)\left(m-2\frac{\sum_{k=0}^{m}k r^k}{\sum_{k=0}^{m}r^k}\right).
}
\tag{4.1}
$$

有限几何级数的导数给

$$
\frac{\sum_{k=0}^{m}k r^k}{\sum_{k=0}^{m}r^k}
=
\frac{r}{1-r}-\frac{(m+1)r^{m+1}}{1-r^{m+1}}.
$$

因此精确形式为

$$
\boxed{
\frac{\|B_{2,m+1}^*x\|^2}{\|x\|^2}
=
(1-r)m-2r+
\frac{2(1-r)(m+1)r^{m+1}}{1-r^{m+1}}.
}
\tag{4.2}
$$

固定任意 $0<t<1$ 后，右侧等于
$(1-t^2)m-2t^2+o(1)$，随 $m$ 线性趋于无穷，而最大单权平方始终为 $b_{\max}^2=1$。

具体取 $t=1/2$，全部权始终在 $[1/2,1]$，前三个非平凡值为

$$
\begin{array}{c|ccc}
m&2&3&4\\ \hline
\|B_{2,m+1}^*x\|^2/\|x\|^2&
15/14&603/340&855/341
\end{array}
\tag{4.3}
$$

故得到严格结论：

$$
\boxed{\text{不存在绝对常数 }c<\infty\text{，使所有有限正权硬核池及全部合法层满足 }
B_{2,n}B_{2,n}^*\preceq c\,b_{\max}^2I.}
\tag{4.4}
$$

## 5. 加一个正弱位后，第一步和第二步都可以完整满射

上一节的临界偶数池有 $U_{2,m+1}=0$。以下扩张说明这一有限临界缺失不是反例成立所必需的条件。

加入第 $2m+1$ 位，权为 $\varepsilon>0$，记

$$
D_\varepsilon=D+\varepsilon E_{2m+1}.
$$

原 $x$ 空着新位，仍有 $D_\varepsilon x=0$。考察 $D_\varepsilon^2:\mathcal H_{m+1}\to\mathcal H_{m-1}$。在 $\varepsilon=0$ 时，按新位是否占据分块，所得两个完整映射是

$$
D^2:\mathcal H_{m+1}^{(2m)}\to\mathcal H_{m-1}^{(2m)},
\qquad
D^2:\mathcal H_m^{(2m)}\to\mathcal H_{m-2}^{(2m)}.
\tag{5.1}
$$

第一块由 (2.4) 是双射。第二块也是满射：在无权模型中，(2.1) 分别在第 $m-2,m-1$ 层表明创建 $D_0^*$ 单射，所以其两步复合从 $\mathcal H_{m-2}$ 到 $\mathcal H_m$ 单射；取伴随即得删除平方满射。有限正对角相似再保持该满射性。$m=1$ 时第二块输出为空，结论按空空间理解。

因此 $\varepsilon=0$ 时的完整 $D_\varepsilon^2$ 已满射。它及其满射 MP 逆在充分小 $\varepsilon$ 下算子范数连续。具体地，满射算子 $A$ 的核投影为

$$
P_{\ker A}=I-A^*(AA^*)^{-1}A;
\tag{5.2}
$$

$AA^*$ 在当前固定有限维空间中严格正，因此 (5.2) 随 $\varepsilon$ 连续。

$\varepsilon=0$ 时，新位扩张的创建列仍为 $D^*x$，它空着新位，并且由第一块的单射性与整个 $\ker D_0^2$ 正交。于是

$$
\boxed{
P_{(\ker D_\varepsilon^2)^\perp}D_\varepsilon^*x
\longrightarrow D^*x
\quad(\varepsilon\downarrow0).
}
\tag{5.3}
$$

另一方面，任意 $\varepsilon>0$ 时这个 $2m+1$ 位模型的

$$
D_\varepsilon:\mathcal H_{m+1}\to\mathcal H_m
\tag{5.4}
$$

也是双射。在无权模型中，这两层同维；交换子在第 $m+1$ 层给
$\|D_0y\|^2-\|D_0^*y\|^2=\|y\|^2$，故删除单射。再由有限正对角相似，(5.4) 双射。其下一步
$D_\varepsilon:\mathcal H_m\to\mathcal H_{m-1}$ 亦满射，证明同样由无权创建的严格正交换子和相似得到。

所以对任意预定常数 $c$，先由 (4.2) 选 $m$ 使泄漏大于 $2c$，再由 (5.3) 选充分小的正 $\varepsilon$，便得到同时满足以下条件的有限正权模型：

$$
D_\varepsilon|_{\mathcal H_{m+1}}\text{ 满射},\qquad
D_\varepsilon^2|_{\mathcal H_{m+1}}\text{ 满射},\qquad
\frac{\|B_{2,m+1,\varepsilon}^*x\|^2}{\|x\|^2}>c.
\tag{5.5}
$$

最大单权仍为 $1$。这里的 $B_{2,\varepsilon}$ 始终由完整物理核投影定义，不是压到旧两组对称线后再取逆。

## 6. 严格正的无限弱尾仍保完整固定层满射和任意大泄漏

固定第 5 节已经选定的奇数正权池，记其删除为 $D_{\mathrm{old}}$，并固定 $n=m+1$。在它后面接无限多个硬核位，初始将这些新权设为零。

在固定总孔层 $\mathcal H_n$ 上，按外部孔数 $j$ 作真正正交直和。零尾时的删除在输出的每个非空块上为

$$
D_{\mathrm{old}}:
\mathcal H_{n-j}^{\mathrm{old}}\otimes\mathcal H_j^{\mathrm{out}}
\longrightarrow
\mathcal H_{n-j-1}^{\mathrm{old}}\otimes\mathcal H_j^{\mathrm{out}},
\quad 0\le j\le n-1.
\tag{6.1}
$$

这些旧池删除映射的输入孔数都在 $1,\ldots,m+1$，均满射。对应平方在全部非空输出块上为

$$
D_{\mathrm{old}}^2:
\mathcal H_{n-j}^{\mathrm{old}}\otimes\mathcal H_j^{\mathrm{out}}
\longrightarrow
\mathcal H_{n-j-2}^{\mathrm{old}}\otimes\mathcal H_j^{\mathrm{out}},
\quad0\le j\le n-2,
\tag{6.2}
$$

也均满射。这只涉及有限种旧池矩阵，其右逆范数的最大值有限；张量外部层的恒等及正交直和不会增加这一最大值。因此零尾时，完整无限物理层之间的 $D$ 和 $D^2$ 都是有界满射，(5.2) 也在这些无限维固定层上适用。

现在选择严格正外尾 $c=(c_j)$，且 $\|c\|_2$ 足够小；例如可取 $c_j=\delta 2^{-j}$，于是还同时有 $c\in\ell^1\cap\ell^2$。在任何固定有限孔层上，

$$
\left\|\sum_jc_jE_j\bigm|_{\mathcal H_k}\right\|
\le\sqrt{k}\,\|c\|_2.
\tag{6.3}
$$

所以外尾加入使上述固定层的 $D,D^2$ 发生任意小的算子范数扰动。满射性由有界右逆的 Neumann 扰动保留，(5.2) 保证二阶核投影及泄漏列连续。原有限源 $x$ 空着外部全部位，仍严格 primitive。取外尾足够小时，(5.5) 中的泄漏下界因而继续成立。

这证明：即使再要求无限严格正的 $\ell^1\cap\ell^2$ 权，以及当前第一、第二下降所需的完整固定孔层满射，仍不存在仅由 $b_{\max}^2$ 乘一个绝对常数给出的普适第二创建泄漏上界。这里没有把固定孔层 MP 拼成整个孔层直和上的有界逆。

## 7. 对原连续尾问题的准确范围

本稿排除的是不保位置分布、birth 和真实源结构的普适创建泄漏估计。它不反驳已知
$B_2B_2^*\preceq SI$：临界偶数池中 $S=m(1+t^2)$ 也线性增长，(4.2) 与该界一致。

第 6 节的无限尾是为保连续性而选择的任意弱尾，不是原 $b_j=(j+1)^{-2}$ 的固定连续衰减尾。没有据此证明原真无限层泄漏具有相同下界。原实际 $u_Q$ 的同源来源，以及完整负二次型求和仍须各自保留。尤其，本稿既不是原顺次 jet 负部的反例，也不是原 $N=M$ 或普通 ISP 的反例。

原连续尾后续若要改进创建泄漏，必须使用该尾的额外位置结构、真实源条件，或完整多层抵消；不能只凭逐位平方零、固定层满射、权的平方可和及最大单权，套用一个绝对常数。
