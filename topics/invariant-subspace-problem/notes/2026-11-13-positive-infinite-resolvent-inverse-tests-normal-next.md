# 无穷正 first 预解式的收敛逆测试与固定真空配对障碍

日期：2026-11-13（UTC）。作者：normal_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明的中间结论；root已核完整实际域、正项carry、换序及有界测试。它关闭 R240 留下的非负行无穷预解式乘积这一普遍正则化接口；不排除依赖某个假想正常湮灭见证的专属正则器。

本文继续使用原 Haar 空间、实际 carry 和最小闭 first 实现。
主要新增点是：对累计行属于 $\ell^2$ 的任意非负行族，有限逆自然词在任意两个严格分离的指数次数空间之间按算子范数收敛。
证明先利用实际 first 词的交换性作对称化，再取 Walsh 矩阵逐项绝对值；不要求各行的 $\ell^2$ 范数之和有限，也不把随机半群混合等同于单一半群。

## 1. 输入、结论与已有无穷积分类

令
$$
H=L^2(\mathbb Z_2,\mu),\qquad
\mathfrak C=\{A\}',\qquad
\mathcal A=\overline{\mathbb C[A]}^{\|\cdot\|},
$$
$$
H_\sigma=\operatorname{Dom}e^{\sigma\mathcal N},\qquad
\|x\|_\sigma=\|e^{\sigma\mathcal N}x\|,
\qquad 0\le\sigma\le1,
\tag{1.1}
$$
其中 $\mathcal N\chi_F=|F|\chi_F$，$H_0=H$。

给定任意非负行
$$
b^{(\nu)}=(b_j^{(\nu)})_{j\ge0}\in\ell^2,\qquad
b_j^{(\nu)}\ge0,
$$
置
$$
X_\nu=X_{b^{(\nu)}}=\sum_jb_j^{(\nu)}V_j,\qquad
Q_\nu=(I+X_\nu)^{-1},
\qquad
P_n=Q_1\cdots Q_n,
$$
$$
c_n=\sum_{\nu\le n}b^{(\nu)},\qquad
c=\sum_{\nu\ge1}b^{(\nu)}
\quad\text{逐坐标求和}.
\tag{1.2}
$$
$X_\nu$ 为 R125/R128 的实际极大增生闭 first，故 $Q_\nu$ 为收缩。
[R230 无穷预解式附录](../results/R230-appendix-positive-infinite-resolvents-and-contractive-strong-units.md)
已证明：

- 若 $c\notin\ell^2$，则 $P_n\to0$ 于 WOT。
- 若 $c\in\ell^2$，则 $P_n\to P$ 于 SOT，其中 $P\in\mathfrak C$ 是非零收缩。
  还已有 $P$ 的收缩强主理想单位，故在所有有限放大不变旗商上单射稠密。

本文处理 $c\in\ell^2$ 的情况。
定义反向自然词
$$
F_n=(I+X_n)\cdots(I+X_1).
\tag{1.3}
$$
对每个 $H_\sigma$ 输入，有限词的全部中间实际域由 R207 的指数尺度支付。

**定理。** 对每个 $0\le\tau<\sigma\le1$，存在相容的线性映射 $F_\infty$，使
$$
\boxed{
F_n\longrightarrow F_\infty
\quad\text{于 }B(H_\sigma,H_\tau),
}
\tag{1.4}
$$
并有一个固定模型常数 $C_+<\infty$，使
$$
\boxed{
\|F_\infty:H_\sigma\to H_\tau\|
\le\sqrt2\exp\!\left(
\frac{eC_+^2\|c\|_2^2}{\sigma-\tau}
\right).
}
\tag{1.5}
$$
此外，
$$
\boxed{PF_\infty x=x\qquad(x\in H_\sigma,\ \sigma>0).}
\tag{1.6}
$$
因此每个正指数次数空间都包含于 $\operatorname{Ran}P$。
这里不宣称 $F_\infty$ 在全 $H$ 有界，也不使用全空间上的无界形式约分。

对 R240 的固定连续正循环向量 $f$，本定理给
$$
\boxed{
Pf\notin\operatorname{Dom}X_f,
\qquad
\phi_f(P\,\cdot)\text{ 不存在固定真空 }H\text{ 表示}.
}
\tag{1.7}
$$
所以任何非零弱或强极限的规范无穷正预解式乘积都不能普遍完成 R244 的配对正则化。

## 2. 实际 first 词的域、截断和有限换序

[R207 指数次数附录 §A](../results/R207-appendix-exponential-chaos-weights-and-bounded-branch-head-cost.md) 给
$$
\|X_b:H_\sigma\to H_{\sigma-\delta}\|
\le C\|b\|_2\delta^{-1/2},
\qquad 0<\delta\le\sigma\le1.
\tag{2.1}
$$
对有限系数截断
$$
X_{b,J}=\sum_{j\le J}b_jV_j\in\mathcal A
$$
同一估计一致成立，且
$$
\|X_{b,J}-X_b:H_\sigma\to H_{\sigma-\delta}\|
\le C\|b_{>J}\|_2\delta^{-1/2}\to0.
\tag{2.2}
$$
这些是实际闭算子的限制；从有限柱加权逼近和闭性得到完整域。

对固定长度 $k$，把总损失 $\sigma-\tau$ 分成 $k$ 个相等步长。
逐因子应用 (2.1) 给每个自然中间域，
逐因子 telescoping 再用 (2.2) 给有限截断词在
$B(H_\sigma,H_\tau)$ 中的收敛。
由于所有有限截断因子都是同一个 $A$ 的有界函数，它们两两交换。
取上述极限可得：

$$
\boxed{
X_{b^{(1)}}\cdots X_{b^{(k)}}x
\text{ 在 }H_\sigma\text{ 上不随这有限个因子的排列改变}.
}
\tag{2.3}
$$
本式只用于已经验证的指数次数输入，不宣称任意最大复合域都相同。

## 3. 保留全部 carry 的正项 Walsh 矩阵主控

在 Walsh 基中，纯局部 Cayley 算子为
$$
V_j^0=I-2E_j,\qquad
V_j^0=
\begin{pmatrix}0&-1\\1&2\end{pmatrix}.
$$
逐矩阵项取绝对值得
$$
W_j=|V_j^0|_{\rm ent}
=\begin{pmatrix}0&1\\1&2\end{pmatrix}
=c_j+c_j^*+2n_j.
\tag{3.1}
$$
下标 $\mathrm{ent}$ 始终指固定 Walsh 基中的逐项绝对值，不是算子绝对值。

[R171 §3](../results/R171-uhf-leading-polynomials-of-unbounded-first-multipliers.md) 与 R207 给真实局部 carry 展开
$$
V_j-V_j^0=\sum_{L\ge1}B_{j,L},
$$
$$
\operatorname{supp}B_{j,L}\subseteq[j,j+L],\qquad
\|B_{j,L}\|\le18\eta_j\eta_*^{L-1},
\qquad
\eta_*=\sup_j\eta_j\le e^{-770}.
\tag{3.2}
$$
每个 $B_{j,L}$ 是一个作用于 $L+1$ 位的真正有限矩阵，外面张量恒等。

令 $B_{j,L}^{+}=|B_{j,L}|_{\rm ent}$。
对 $d$ 维矩阵 $B$，
$$
\||B|_{\rm ent}\|
\le\||B|_{\rm ent}\|_{\rm HS}
=\|B\|_{\rm HS}\le\sqrt d\,\|B\|.
$$
故
$$
\|B_{j,L}^{+}\|
\le2^{(L+1)/2}\|B_{j,L}\|.
\tag{3.3}
$$
因为指数次数权在这有限块上的最大、最小比至多为
$e^{\sigma(L+1)}$，
$$
\|B_{j,L}^{+}:H_\sigma\to H_\sigma\|
\le(\sqrt2e)^{L+1}\|B_{j,L}\|
\qquad(0\le\sigma\le1).
\tag{3.4}
$$

对于非负 $b\in\ell^2$，定义有界正项矩阵
$$
K_b^+=\sum_jb_j\sum_{L\ge1}B_{j,L}^+.
\tag{3.5}
$$
该和在每个 $B(H_\sigma)$ 中绝对收敛，因为
$$
\begin{aligned}
\|K_b^+\|_{B(H_\sigma)}
&\le
\frac{36e^2}{1-\sqrt2e\eta_*}
\sum_jb_j\eta_j\\
&\le
\frac{36e^2\|\eta\|_2}{1-\sqrt2e\eta_*}\|b\|_2.
\end{aligned}
\tag{3.6}
$$
所以取逐项绝对值的有限维成本已经支付，没有把原 carry 范数界直接当作其绝对矩阵范数界。

定义辅助正项矩阵尺度映射
$$
\mathcal M_b=\sum_jb_jW_j+K_b^+.
\tag{3.7}
$$
纯部分的创建、消去、对角次数块范数分别至多为
$\|b\|_2\sqrt{q+1}$、$\|b\|_2\sqrt q$、$2\|b\|_2\sqrt q$。
与 R207 相同的三块估计给常数 $16$。
结合 (3.6)，可取
$$
C_+=16+\frac{36e^2\|\eta\|_2}{1-\sqrt2e\eta_*}
$$
使
$$
\boxed{
\|\mathcal M_b:H_\sigma\to H_{\sigma-\delta}\|
\le C_+\|b\|_2\delta^{-1/2}.
}
\tag{3.8}
$$
有限系数截断在这些尺度间按算子范数收敛；
$\mathcal M_b$ 对 $b$ 线性，且对非负 $b$ 保持 Walsh 系数非负锥。

若 $|x|$ 表示把 $x$ 的 Walsh 系数逐个取模，则
$\||x|\|_\sigma=\|x\|_\sigma$。
由局部矩阵的逐项三角不等式、(3.2)–(3.6) 的收敛，以及系数截断极限，
$$
\boxed{
|X_bx|\le\mathcal M_b|x|
\quad\text{逐个 Walsh 系数， }b\ge0,\ x\in H_\sigma,\ \sigma>0.
}
\tag{3.9}
$$
正锥在每个加权 $\ell^2$ 中闭，故所有比较在极限后仍成立。
有限词可以逐次应用 (3.9)，每次保留下一步需要的正指数权。

$\mathcal M_b$ 只作为这些相容指数尺度之间的辅助映射使用。
本稿不需要、也不声称它在全 $H$ 上生成某个有界半群。

## 4. 对称化给由累计行控制的统一指数界

先固定有限 $n$。
把 (1.3) 展开为子集之和。
对每个长度为 $k$ 的选中子集，用 (2.3) 把其实际词写成全部 $k!$ 个排列的平均。
随后才用 (3.9) 逐项取绝对值。

所有这些不同指标的有序词都包含在
$(\mathcal M_{c_n})^k$ 的展开内；后者还含非负的重复指标词。
因此
$$
\boxed{
|F_nx|
\le\sum_{k=0}^n\frac1{k!}
(\mathcal M_{c_n})^k|x|
\le\sum_{k=0}^\infty\frac1{k!}
(\mathcal M_c)^k|x|.
}
\tag{4.1}
$$
这里并没有假定不同辅助 $\mathcal M_b$ 交换。
$1/k!$ 来自实际 first 词在取模之前的换序；
若省略这一步，就不能用非交换正项矩阵的指数来控制原乘积。

令 $\delta=\sigma-\tau>0$。
均分总权损失，(3.8) 给
$$
\|(\mathcal M_c)^k:H_\sigma\to H_\tau\|
\le
\left(C_+\|c\|_2\sqrt{k/\delta}\right)^k.
\tag{4.2}
$$
每个中间映射都定义在正指数空间中。
由 $k!\ge(k/e)^k$，
$$
\frac{k^{k/2}}{k!}\le\frac{e^{k/2}}{\sqrt{k!}},
$$
再以 Cauchy–Schwarz 求和，
$$
\sum_{k\ge0}\frac{a^k k^{k/2}}{k!}
\le\sqrt2 e^{ea^2}.
\tag{4.3}
$$
$k=0$ 的项按 $1$ 解释。

所以 (4.1) 右端在 $H_\tau$ 中绝对收敛，并且
$$
\boxed{
\sup_n\|F_n:H_\sigma\to H_\tau\|
\le\sqrt2\exp\!\left(
\frac{eC_+^2\|c\|_2^2}{\sigma-\tau}
\right).
}
\tag{4.4}
$$
这只使用累计非负行 $c\in\ell^2$，
不使用 $\sum_\nu\|b^{(\nu)}\|_2<\infty$。

## 5. 尾行给真正的算子范数 Cauchy 性

取 $n>m$。
$F_n-F_m$ 展开中的每个子集词至少包含一个编号大于 $m$ 的行。
对每个词继续采用上一节的实际对称化。
对每个 $k$，其正项主控被
$$
\frac1{k!}\left[
(\mathcal M_{c_n})^k-(\mathcal M_{c_m})^k
\right]
$$
支配。
该差逐矩阵项非负，因为其展开恰含所有至少一次使用尾行的有序词，允许重复。

令 $d_m=c-c_m\ge0$。
对非交换幂使用准确 telescoping：
$$
A^k-B^k=
\sum_{\ell=0}^{k-1}
A^{k-1-\ell}(A-B)B^\ell.
$$
利用正项矩阵的单调性，
$$
\boxed{
|(F_n-F_m)x|
\le\sum_{k\ge1}\frac1{k!}
\sum_{\ell=0}^{k-1}
(\mathcal M_c)^{k-1-\ell}
\mathcal M_{d_m}
(\mathcal M_c)^\ell|x|.
}
\tag{5.1}
$$
因此每个词都有一个小的真实累计尾行因子。

仍把 $\delta=\sigma-\tau$ 均分给 $k$ 次作用。
若令 $g=1+\|c\|_2$，则 (3.8) 给
$$
\|F_n-F_m:H_\sigma\to H_\tau\|
\le
\frac{\|d_m\|_2}{g}
\sum_{k\ge1}
\frac{k}{k!}
\left(C_+g\sqrt{k/\delta}\right)^k.
\tag{5.2}
$$
右侧级数有限，常数只依赖固定的 $\delta,c$。
例如对 $a=C_+g/\sqrt\delta$、$t=2ea^2$，
与 (4.3) 相同的 Cauchy–Schwarz 估计给
$$
\sum_{k\ge1}\frac{k\,a^k k^{k/2}}{k!}
\le\sqrt{2(t^2+t)}\,e^{t/2}<\infty.
\tag{5.3}
$$

$c_m\uparrow c$ 逐坐标，且 $c\in\ell^2$；
由支配收敛，$\|d_m\|_2\to0$。
所以 $F_n$ 在 $B(H_\sigma,H_\tau)$ 中 Cauchy，证明 (1.4)。
不同指数尺度间的极限相容，因为它们在共同输入上具有相同的 $H$ 极限。
(1.5) 随即来自 (4.4)。

## 6. 与原有界无穷积的逆关系及有界代数测试

对每个有限 $n$ 和 $x\in H_\sigma$，
全部自然中间域已有保证，依次消去相邻逆因子得
$$
P_nF_nx
=Q_1\cdots Q_n(I+X_n)\cdots(I+X_1)x=x.
\tag{6.1}
$$
不需要交换无界因子。

由 $P_n\to P$ 强、$\|P_n\|\le1$ 和 $F_nx\to F_\infty x$ 于 $H$，
$$
PF_\infty x
=\lim_nP_nF_nx=x.
\tag{6.2}
$$
这证明 (1.6)。
若 $c=0$，全部行都为零，$F_n=F_\infty=P=I$；
上述结论也直接成立。

还需要真正属于 $\mathcal A$ 的有界测试，而不能直接把 $F_\infty$ 插进一个正常泛函。
固定 $\sigma_0>0$，取
$$
F_{n,J}=
\prod_{\nu=n}^{1}
\left(I+\sum_{j\le J}b_j^{(\nu)}V_j\right)
\in\mathcal A.
\tag{6.3}
$$
对固定 $n$，第 2 节的自然词截断证明
$$
F_{n,J}\longrightarrow F_n
\quad\text{于 }B(H_{\sigma_0},H)
\quad(J\to\infty).
$$
依次选择 $J_n$，使
$$
\|F_{n,J_n}-F_n:H_{\sigma_0}\to H\|\le2^{-n}.
$$
置 $T_n=F_{n,J_n}\in\mathcal A$，则
$$
\boxed{
T_n\longrightarrow F_\infty
\quad\text{于 }B(H_{\sigma_0},H).
}
\tag{6.4}
$$
不要求这些 $T_n$ 在 $B(H)$ 中一致有界。

## 7. 有限次数层上的逆测试成本

若 $x$ 的 Walsh 次数至多为 $q$，
在 (1.5) 中取 $\tau=0$、$\sigma=(q+1)^{-1/2}$。
由于 $\|x\|_\sigma\le e^{\sqrt{q+1}}\|x\|$，
$$
\boxed{
\|F_\infty x\|
\le\sqrt2
\exp\!\left((D_c+1)\sqrt{q+1}\right)\|x\|,
\qquad D_c=eC_+^2\|c\|_2^2.
}
\tag{7.1}
$$
这控制整个次数层，与最高物理位无关。
成本是 $e^{O_c(\sqrt q)}$，即次数的次指数增长。

## 8. R240 的同一个循环正向量仍不能配对正则化

沿用
[R240](../results/R240-cyclic-positive-functional-without-fixed-vacuum-factor.md)
的固定向量
$$
J_p=[4p^2,4p^2+2p)\cap\mathbb N_0,\qquad
\varepsilon=\frac1{16},
$$
$$
f=1+\varepsilon\sum_{p\ge1}2^{-p/4}\chi_{J_p}.
\tag{8.1}
$$
它连续、严格正、$Cf=f$，且已知对实际 $A$ 循环。
实际测试满足
$$
V_{J_p}1=\chi_{J_p},
$$
$$
\operatorname{Re}\langle V_{J_p}f,f\rangle
\ge\varepsilon^2 2^{3p/2}+2\varepsilon2^{-p/4}-o(1).
\tag{8.2}
$$
这里真实 carry 误差至多为
$16p6^{2p-1}e^{-77016^{4p^2}}\|f\|^2$。
而
$$
f\in H_{\sigma_0},\qquad
\sigma_0=\frac{\log2}{16},
\tag{8.3}
$$
因为
$\|f\|_\sigma^2=1+\varepsilon^2\sum_pe^{4\sigma p}2^{-p/2}<\infty$
对 $0<\sigma<(\log2)/8$ 成立。

假设存在 $h\in H$，使
$$
\langle PFf,f\rangle=\mathcal B(Fh,1)
\qquad(F\in\mathfrak C),
\tag{8.4}
$$
其中 $\mathcal B(x,y)=\langle x,Cy\rangle$。

用第 6 节对这个固定 $\sigma_0$ 选出的 $T_n\in\mathcal A$。
对固定 $p$，使用真正有界测试
$$
F=T_nV_{J_p}\in\mathcal A.
$$
所有有界交换子相互交换，(6.2)–(6.4) 给
$$
\langle PT_nV_{J_p}f,f\rangle
=\langle V_{J_p}PT_nf,f\rangle
\longrightarrow\langle V_{J_p}f,f\rangle.
$$
另一方面，实际交换子均为 $C$ 对称，
$$
\mathcal B(T_nV_{J_p}h,1)
=\mathcal B(h,T_nV_{J_p}1)
=\mathcal B(h,T_n\chi_{J_p})
\longrightarrow\mathcal B(h,F_\infty\chi_{J_p}).
$$
故
$$
\langle V_{J_p}f,f\rangle
=\mathcal B(h,F_\infty\chi_{J_p}).
\tag{8.5}
$$
由 (7.1)，右侧的模至多为
$$
\sqrt2\|h\|
\exp\!\left((D_c+1)\sqrt{2p+1}\right).
$$
但左侧的实部由 (8.2) 按 $2^{3p/2}$ 增长，矛盾。

极限顺序明确为：先固定 $p$ 令 $n\to\infty$，再令 $p\to\infty$。
从未要求 $h$ 属于 $F_\infty$ 或任何逆自然词的域。

因此 $\phi_f(P\,\cdot)$ 不存在固定真空 $H$ 表示。
若 $Pf\in\operatorname{Dom}X_f$，由于 $Cf=f$，
[R244 的实际配对域引理](../results/R244-paired-domain-regularizers-and-normal-annihilator-factorization.md)
会给
$$
\langle PFf,f\rangle
=\mathcal B(FX_fPf,1),
$$
恰是已被排除的 (8.4)。
所以
$$
\boxed{
Pf\notin\operatorname{Dom}X_f,\qquad
PH\not\subseteq\operatorname{Dom}X_f.
}
\tag{8.6}
$$

若 $c\notin\ell^2$，已有分类给弱极限为零，不能作为具有非零迹锚或强主理想单位的候选。
结合两种情况，所有非零规范无穷正 first 预解式积都被 (8.6) 覆盖，
无论各行如何重叠，也无论 $\sum_\nu\|b^{(\nu)}\|_2$ 是否有限。

## 9. 有限混合附加因子

还可以在 $P$ 外乘任意固定有限个实际有界复杂 first 预解式和非负 first 半群。
这里复杂 first 只在其有界预解式已经存在时使用；不假定它生成有界半群。

具体地，令 $R_0$ 为
[R240 第二附录](../results/R240-appendix-positive-first-semigroups-fail-paired-regularization.md)
已处理的某个有限混合有界乘积。
该附录已给相容逆测试 $G$、有界代数截断，
以及每个正指数尺度上的
$$
R_0Gx=x,\qquad
\|G:H_\sigma\to H_\tau\|
\le A(\sigma-\tau)^{-k/2}
\exp\!\left(B/(\sigma-\tau)\right),
\tag{9.1}
$$
其中 $k$ 是其中线性逆测试因子的个数；所有有限自然复合域已支付。引用正文写出 $\tau=0$；对一般 $\tau$，逐个因子按同一 R207 估计分配总损失 $\sigma-\tau$，末端保留 $\tau$ 权，便得到 (9.1) 及同尺度截断收敛。

令 $R=PR_0$。
先用 $F_\infty:H_\sigma\to H_{\sigma/2}$，
再用 $G:H_{\sigma/2}\to H$，定义 $G F_\infty$。
其全部输入仍有正指数权，所以
$$
R(GF_\infty)x
=P R_0G F_\infty x
=PF_\infty x=x.
$$
有界代数截断在中间尺度逐因子相乘、再作对角选择，
给 $GF_\infty$ 的真实有界测试。
总成本至多为
$$
A'\sigma^{-k/2}e^{B'/\sigma}.
$$
在次数 $\le q$ 的层上仍只有
$(q+1)^{k/4}e^{O(\sqrt q)}$ 成本。
第 8 节的实际矩矛盾于是原样成立：
$$
Rf\notin\operatorname{Dom}X_f.
\tag{9.2}
$$
只对有限个附加因子作这个推论。

## 10. 结论边界

本文没有声称一般复杂行的无穷预解式积存在有界强极限；
正系数的强极限和收缩性使用了已有分类。

本文也没有把 $P$ 的随机半群表示换成单一 first 半群。
新的统一估计来自真实有限词的对称化和累计行的正项矩阵主控，
因此覆盖一般重叠行，是比单坐标单位等价或有限词估计更大的范围。

R240 的 $f$ 已知循环，其正秩一态不湮灭目标慢主理想。
因此 (8.6) 排除的是“这些正则器能对每个有限秩正常态自动完成配对域”的普遍命题。
它没有排除：对一个具有额外慢理想湮灭方程的假想见证，
适配选择某个无穷预解式积满足 R244 的指定配对域。

R230 无穷积附录提供的收缩强单位仍然有效；
本文没有将状态锚与配对域混同。
一般正常正湮灭者排除、R253 的 $q_m$ 一致非零下界、
以及普通复 Hilbert 不变子空间问题的完成标准仍未关闭。
