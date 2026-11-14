# R248 附录：平方可和对数噪声下整个实际表示的有界相似

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；根代理独立核验热因子分解、稠密像唯一性及与旧强阻尼范围的区别。

状态：完整证明。本稿新增的是整个实际交换子表示的一个共同有界相似实现。对应正常矩的负权发散已经由[R150 实际矩判据](R150-appendix-actual-normal-moments-negative-occupation-criterion-and-witness-divergence.md)独立证明，不重复计为新结论。原 R248 取的多项式强阻尼不满足本稿假设。

## 1. 噪声与实际有界单位

设
$$
0<\delta_j\le1,\qquad
a_j=-\log\delta_j,\qquad a\in\ell^2.
\tag{1.1}
$$
允许 $a=0$、$a\in\ell^1$ 或 $a\in\ell^2\setminus\ell^1$。
在原 Walsh 基上定义
$$
D_\delta\chi_F=\delta_F\chi_F,\qquad
\delta_F=\prod_{j\in F}\delta_j=e^{-a(F)}.
\tag{1.2}
$$
它是有界、正、单射且稠密像的收缩。
若 $a\notin\ell^1$，则 $D_\delta^{-1}$ 不有界；下面不将它当作全域有界算子。

取原实际正 first 热因子
$$
P=e^{-X_a/2}\in A'.
$$
[准确热值域与双侧输入范数](R150-appendix-exact-weighted-occupation-ranges-of-positive-semigroups.md)
给
$$
U=e^{\mathcal N_a}P\in B(H)^\times,
\qquad
\|U\|,\|U^{-1}\|\le M_{0,1/2}.
$$
由原 $C$ 对称性及 $Ce^{-\mathcal N_a}C=e^{-\mathcal N_a}$，
同稿已经支付
$$
P=e^{-\mathcal N_a}U=U^\tau e^{-\mathcal N_a},
\qquad U^\tau=CU^*C.
$$
置
$$
R=U^\tau,\qquad M=M_{0,1/2}.
$$
于是有准确全域分解
$$
\boxed{
P=R D_\delta,\qquad
R\in B(H)^\times,\qquad
\|R\|,\|R^{-1}\|\le M.
}
\tag{1.3}
$$
$R$ 无须属于 $A'$。
这里不是把 $U$ 移过 $D_\delta$；(1.3) 来自对原分解取 $C$ 转置。

## 2. 同一个单位实现整个实际交换子

**定理2.1。** 对每个 $F\in A'$，在 $\operatorname{Ran}D_\delta$ 上自然定义
$$
F_\delta^{\,0}(D_\delta h)=D_\delta Fh.
\tag{2.1}
$$
该算子有唯一的有界全域延拓，并且
$$
\boxed{
F_\delta=R^{-1}FR,\qquad
D_\delta F=F_\delta D_\delta.
}
\tag{2.2}
$$
同一个 $R$ 同时适用于所有 $F$，且
$$
\|F_\delta\|\le M^2\|F\|.
\tag{2.3}
$$

**证明。** 由 $P\in A'$ 及其交换性，
$$
R D_\delta F=PF=FP=FRD_\delta.
$$
左乘有界 $R^{-1}$，得到
$$
D_\delta F=R^{-1}FRD_\delta
$$
作为原 $H$ 上的有界算子恒等式。
它在 $\operatorname{Ran}D_\delta$ 上正好实现 (2.1)。
这个像稠密，所以有界延拓唯一，且 (2.3) 来自 (1.3)。证毕。

特别
$$
\boxed{A_\delta=R^{-1}AR.}
\tag{2.4}
$$
所以 $F\mapsto F_\delta$ 是从 $A'$ 到 $\{A_\delta\}'$ 的有界代数同构，
其逆的范数也至多为 $M^2$。
这是真正的共同相似，不是 R88 的只线性有界乘法对应，也不只是稠密像交织。

## 3. 与 R248 的局部 carry 变形准确相同

还需识别 (2.4) 确实是 R248 原定义的噪声模型，而非另造一个有界算子。

若 $T$ 仅支撑在有限物理位块 $K$，令
$$
T_\delta=D_{\delta,K}T D_{\delta,K}^{-1}.
$$
则有准确局部交织
$$
D_\delta T=T_\delta D_\delta,
\qquad
\|T_\delta\|
\le e^{\sum_{j\in K}a_j}\|T\|
\le e^{\|a\|_2\sqrt{|K|}}\|T\|.
\tag{3.1}
$$
没有对全 $D_\delta^{-1}$ 作有界性要求。

R248 §3 引用的实际局部展开是
$$
N_j=\sum_{r\ge j}\frac{\alpha_r}{\alpha_j}
E_j^*\cdots E_{r-1}^*E_r,
$$
$$
V_j=(I-2E_j)+\sum_{r\ge j+1}B_{j,r},
\qquad
\operatorname{supp}B_{j,r}\subseteq[j,r],
\qquad
\|B_{j,r}\|\le18\,\frac{\alpha_r}{\alpha_j},
$$
且对 $r>j$，
$$
\frac{\alpha_r}{\alpha_j}\le e^{-770\,16^{r-1}}.
\tag{3.2}
$$
将每个局部项按 (3.1) 变形。
新增成本至多
$e^{\|a\|_2\sqrt{r-j+1}}$，
被 (3.2) 的实际 carry 衰减支付。
因此这些级数按算子范数绝对收敛，得到 R248 意义下的
$N_{j,\delta}$、$V_{j,\delta}$。

例如纯项范数统一不超过 $3e^{\|a\|_\infty}$，
全部误差可由
$$
18\sum_{r\ge1}
e^{\|a\|_2\sqrt{r+1}}e^{-770\,16^{r-1}}<\infty
$$
统一控制。
所以 $N_{j,\delta}$、$V_{j,\delta}$ 在 $j$ 上均一致有界。

将局部交织取上述绝对范数极限，得到
$$
D_\delta N_j=N_{j,\delta}D_\delta,\qquad
D_\delta V_j=V_{j,\delta}D_\delta.
$$
再由 $\operatorname{Ran}D_\delta$ 稠密和定理2.1的唯一性，
$$
\boxed{
N_{j,\delta}=R^{-1}N_jR,\qquad
V_{j,\delta}=R^{-1}V_jR.
}
\tag{3.3}
$$
故原实际递归、Cayley 关系及全部 carry 都保持。

对原慢系数 $c_j=(j+1)^{-2}$，R248 的级数定义
$$
S_{N,\delta}=\sum_jc_jN_{j,\delta},\qquad
S_{Y,\delta}=\frac12\sum_jc_j(I-V_{j,\delta})
$$
按范数收敛。
用 (3.3) 得
$$
\boxed{
S_{N,\delta}=R^{-1}S_NR,\qquad
S_{Y,\delta}=R^{-1}S_YR.
}
\tag{3.4}
$$
原两个慢算子均已在全 $H$ 单射，因此
$$
\boxed{\ker S_{N,\delta}=\ker S_{Y,\delta}=\{0\}.}
\tag{3.5}
$$
这里使用有界相似；没有由一个一般拟仿射交织免费下传单射性。

## 4. 不变格的真实运输

对原任意闭 $A$ 不变空间 $M_0$，
$$
M_\delta=R^{-1}M_0
$$
闭且 $A_\delta$ 不变，反向亦然。
这给两不变格之间的实际双射，并按同一个有界单位传递有限旗和有限放大。

还可识别原噪声 $D_\delta$ 本身的像闭包：
$$
D_\delta M_0=R^{-1}P M_0.
$$
原热因子的同一组收缩强单位保证 $PM_0$ 在 $M_0$ 中稠密，所以
$$
\boxed{\overline{D_\delta M_0}=R^{-1}M_0.}
\tag{4.1}
$$
由已证准确限制值域，甚至有集合等式
$$
D_\delta M_0
=R^{-1}\bigl(M_0\cap H_{a,1}\bigr).
\tag{4.2}
$$
不是先假设 $D_\delta$ 或占据权保持原未知空间，再推出这些等式。
本节也不声称通常伴随或原 $C$ 在对应未知限制上仍有相同形式。

## 5. 正常矩的 Hilbert 化在本类中不能产生新慢核

本节是与已发实际矩判据的一致性检验，不新增一个负权发散定理。

令 $\phi$ 为原正常泛函，写
$$
m_F=\phi(V_F),\qquad
h_\delta=\sum_F\delta_F(-1)^{|F|}m_F\chi_F.
$$
假设右侧在 $H$ 中收敛，并且
$$
\phi(S\mathcal A)=0,\qquad S=S_N\text{ 或 }S_Y.
$$
R248 §4 的实际列估计与 $C$ 对称矩阵关系给
$$
\boxed{
B(S_\delta h_\delta,\chi_F)=\delta_F\phi(SV_F)=0.
}
\tag{5.1}
$$
此处其绝对收敛证明在本类仍适用：
对固定列 $S\chi_F=\sum_Gc_G\chi_G$，
原估计 $\sum_G6^{|G|}|c_G|<\infty$ 未变，
而 $|m_G|\le\|\phi\|6^{|G|}$。
(3.3)--(3.4) 又已识别这里所用的同一个真实 $S_\delta$。

Walsh 基完备给 $S_\delta h_\delta=0$。
由 (3.5)，$h_\delta=0$，从而全部 $m_F=0$。
R88 的有界强逼近再给 $\phi|_{A'}=0$。
特别，非零正正常泛函的 $\phi(I)>0$ 不可能满足这些条件。

在此前热矩表示中，对应原聚合源准确为
$$
h=R h_\delta.
$$
所以这里的有界相似解释与已经证明的直接负权判据完全吻合。

## 6. 范围扣除

若 $a\in\ell^1$，$D_\delta$ 自身已有有界逆，原对角相似属直接情形。
实质新增范围为 $a\in\ell^2\setminus\ell^1$：
$D_\delta^{-1}$ 无界，但整个变形表示仍由另一个有界单位 $R$ 实现。

原 R248 自适应强阻尼在未保留位上取
$\delta_j=(j+2)^{-\sigma}$，或固定倍数，故
$-\log\delta_j$ 不属于 $\ell^2$。
本稿不将该强阻尼模型判为与原模型相似，
也不撤销其可能存在的真实新核与逆阻尼域障碍。

本文只证明 (1.1) 是有界相似的充分条件，
未证明它是必要条件。
一般正常见证专属上界和普通 Hilbert ISP 仍未完成。

后续[尖锐阈值与真实乘积成本](R248-appendix-sharp-log-noise-similarity-threshold-and-product-cost.md)已经在明确局部类 $\delta_j\ge c(j+2)^{-s}$（任意固定有限 $s$）补出必要性：有界相似当且仅当 $-\log\delta\in\ell^2$。这是实际 $N_j$ 收缩乘积与全部相对 carry 的证明；不由非相似断言慢核存在。
