# 固定二点 Kummer 塔、局部惯性及严格商

**可信度：本文各比较已证明；未得到剩余类群核的跨素数上界。** 日期：2026-11-12。固定
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
P=(-1,4),\quad Q=(9,24),
$$
并取 R34–R36 的普通分裂素数
$p\ge13$、$p\equiv1\pmod4$、$p\ne17$。使用直接 Tate 字符
$\widetilde\chi=\rho_E|_\Delta$，$\rho_E(\gamma)=1+p$，以及
$$
\theta=T-p,\quad K_\infty=K(E[\pi^\infty]),\quad
C_p=X_\infty^{\widetilde\chi}/\theta,\quad
D_p=\mathcal A_p/\theta\mathcal A_p.
$$

本文实际识别固定二点 1-motive 提供的 Galois 商及其惯性格。结论不是“所有无分歧类都来自已知点”：这个 Kummer 商之外的核准确地保留了 $\Sha[p^\infty]$ 的对偶。严格商的系数还涉及两个局部椭圆对数的超越比值，不能由一个固定的代数系数行取得。

## 1. 固定二点的 Kummer 扩张是秩二整数格

选择相容的 $\pi^m$-原像，定义
$$
\mathscr L_p
=K_\infty\bigl(\pi^{-\infty}P,\pi^{-\infty}Q\bigr),
\qquad H_p=\operatorname{Gal}(\mathscr L_p/K_\infty).
\tag{1.1}
$$
在 $K_\infty$ 上 $T_\pi E$ 为平凡模，因此两个 Tate–Kummer cocycle 的限制给连续同态
$$
\kappa_{P,Q}:G_{K_\infty}\longrightarrow (T_\pi E)^2.
\tag{1.2}
$$
它们在 $K_\infty$ 上不依赖所选原像：两种选择之差是 Tate 模中的 coboundary，而限制后作用平凡。固定 Tate 基后，(1.2) 的紧像正是
$H_p\subset\mathbb Z_p^2$。

R4 的独立性及共轭给 $P,Q$ 在 $E(K)$ 中 $\mathcal O_K$-线性独立。它们的 Kummer 类在 $H^1(K,V_\pi E)$ 中因而 $\mathbb Q_p$-线性独立。在
$G=\Delta\times\Gamma$ 上，非平凡 tame 字符使
$H^1(G,V_\pi E)=0$，故限制到 $K_\infty$ 后仍线性独立。若 $H_p$ 的秩小于二，会有一个非零 $\mathbb Q_p$ 行消去 (1.2) 的像，矛盾。因此
$$
H_p\text{ 是 }\mathbb Z_p^2\text{ 中的满秩闭格。}
\tag{1.3}
$$

共轭作用满足
$$
\kappa_{P,Q}(\gamma\sigma\gamma^{-1})
=\rho_E(\gamma)\kappa_{P,Q}(\sigma).
\tag{1.4}
$$
此外，扩张 (1.1) 远离 $\mathfrak p$ 无分歧：在 $K_1$ 上曲线远离该素位有好约化，相应 $\pi$-同源为 étale；在 $\bar{\mathfrak p}$ 处同样如此。所需有限层 Kummer 无分歧事实及坏素数处理已在 R35 §1.1 按 Rubin Corollary 3.17 核查。因此 (1.2) 经过
$$
C_p\twoheadrightarrow H_p.
\tag{1.5}
$$

### 1.1 完整 Mordell–Weil 格确定其有限指数

令
$$
L_p=\bigl(E(K)/E(K)_{\rm tors}\bigr)
\otimes_{\mathcal O_K}\mathcal O_{K,\mathfrak p}
\simeq\mathbb Z_p^2,\qquad
L_{0,p}=\mathbb Z_pP+\mathbb Z_pQ\subset L_p.
$$
R27 的 Selmer 同构及全局 Kummer 列给
$$
0\longrightarrow L_p\otimes_{\mathbb Z_p}W
\longrightarrow\operatorname{Hom}(C_p,W)
\longrightarrow\Sha(E/\mathbb Q)[p^\infty]\longrightarrow0,
\tag{1.6}
$$
其中 $W=E[\pi^\infty]\simeq\mathbb Q_p/\mathbb Z_p$；最后使用 R7 的 $K$ 上 $\pi$ 分量与 $\mathbb Q$ 上 $p$ 分量比较。

固定 Tate 基后取 Pontryagin 对偶，得到
$$
0\longrightarrow\Sha(E/\mathbb Q)[p^\infty]^\vee
\longrightarrow C_p
\longrightarrow L_p^\vee\longrightarrow0.
\tag{1.7}
$$
这里 $L_p^\vee=\operatorname{Hom}_{\mathbb Z_p}(L_p,\mathbb Z_p)$。对偶满射在 $P,Q$ 上的坐标恰是 (1.2)，因此
$$
\boxed{\quad
H_p=\operatorname{im}\bigl(L_p^\vee\longrightarrow L_{0,p}^\vee
\simeq\mathbb Z_p^2\bigr),\qquad
\ker(C_p\to H_p)=\Sha(E/\mathbb Q)[p^\infty]^\vee.
\quad}
\tag{1.8}
$$
等式中的最后一项不预先假设有限。由于 $L_{0,p}$ 有有限指数，对偶限制为单射，所以 $H_p$ 也被典范地识别为 $L_p^\vee$；在已知点坐标中，它可能不是完整的 $\mathbb Z_p^2$。

取固定正整数 $I$ 使
$$
I\bigl(E(K)/E(K)_{\rm tors}\bigr)
\subset\mathcal O_KP+\mathcal O_KQ.
\tag{1.9}
$$
则对偶限制的余核被 $I$ 消去，故
$$
p^{v_p(I)}\mathbb Z_p^2\subset H_p\subset\mathbb Z_p^2.
\tag{1.10}
$$
特别地，对所有 $p\nmid I$ 都有 $H_p=\mathbb Z_p^2$。这一步不需要声称 $P,Q$ 已是完整 Mordell–Weil 基。

## 2. 惯性格是两个已知点对数的一列

记
$$
\ell_P=\log_E(P),\qquad\ell_Q=\log_E(Q).
$$
本素数范围非异常，局部 Kummer 格的对数像为
$\pi\mathbb Z_p$。R36 §3.1 的规范化局部互反律给
$$
\delta_\infty(u_\infty)=\kappa_0\mathbf t,\qquad
\kappa_0=\frac{1-\pi}{\beta}\in\mathbb Z_p^\times,\quad
\beta^{p-1}=1-\pi,\quad\beta\equiv1\pmod p,
$$
以及任一全局点 $R$ 的局部字符值
$$
c_R=\kappa_0\frac{\log_E(R)}{\pi}.
\tag{2.1}
$$

令 $I_p\subset H_p$ 为 $\mathfrak p$ 的惯性像。由于
$U_\infty^{\widetilde\chi}/\theta$ 由 $u_\infty$ 生成，(2.1) 给出准确整数等式
$$
\boxed{\quad
I_p=
\mathbb Z_p\cdot
\kappa_0\left(\frac{\ell_P}{\pi},\frac{\ell_Q}{\pi}\right)
\subset H_p\subset\mathbb Z_p^2.
\quad}
\tag{2.2}
$$
这不是只确定有理方向：局部范数极限的完整整数基给出所写的整个格。局部未分歧 $\mathbb Z_p$ 商的 $\Delta$ 作用平凡，目标字符非平凡，故它不补充另一条局部方向，见 R34 §2。

两个对数都非零，所以 $I_p$ 为秩一格。定义其在 $H_p$ 中的饱和
$$
I_p^{\rm sat}=H_p\cap\mathbb Q_p I_p.
\tag{2.3}
$$
则
$$
I_p^{\rm sat}/I_p\simeq\mathbb Z/p^{e_p^{\rm MW}}\mathbb Z,\qquad
H_p/I_p^{\rm sat}\simeq\mathbb Z_p.
\tag{2.4}
$$
这里的指数恰是 R35 §5.1 的 $e_p^{\rm MW}$：在 $H_p=L_p^\vee$ 的识别下，(2.2) 就是完整 MW Tate 格的局部化行的对偶。该行的 Smith 指数，正是其对偶列在饱和中不原始的长度。因此作为整数模
$$
H_p/I_p\simeq
\mathbb Z_p\oplus\mathbb Z/p^{e_p^{\rm MW}}\mathbb Z
\tag{2.5}
$$
非典范地成立。

### 2.1 两个已知点给有限误差的准确界

置 R36 的
$$
b_p=\min\{v_p(\ell_P),v_p(\ell_Q)\}-1\ge0.
$$
局部对数闭格满足
$$
\log_E(L_{0,p})\subset\log_E(L_p)\subset\pi\mathbb Z_p,
\qquad
I\,\log_E(L_p)\subset\log_E(L_{0,p}).
$$
因此
$$
\boxed{\quad
\max\{0,b_p-v_p(I)\}\le e_p^{\rm MW}\le b_p,\qquad
e_p^{\rm MW}=b_p\quad(p\nmid I).
\quad}
\tag{2.6}
$$
所以 R35 中的有限 MW 修正，在固定有限例外外就由 $P,Q$ 的两个局部对数的最小赋值准确计算。这个等式不控制 $b_p$ 随 $p$ 的大小，也不把它视为 $\Sha$ 的阶。

## 3. 最大无分歧 Kummer 商与严格类群核

R34 的整正合列为
$$
0\longrightarrow U_\infty^{\widetilde\chi}/\theta
\longrightarrow C_p\longrightarrow D_p\longrightarrow0.
\tag{3.1}
$$
将 (1.8) 与 (3.1) 对比。左端局部单位格到 $H_p$ 的像是 $I_p$，而该映射由 (2.2) 为单射。蛇引理给
$$
\boxed{\quad
0\longrightarrow\Sha(E/\mathbb Q)[p^\infty]^\vee
\longrightarrow D_p
\longrightarrow H_p/I_p\longrightarrow0.
\quad}
\tag{3.2}
$$
扩张 $\mathscr L_p^{\,I_p}/K_\infty$ 是 (1.1) 内最大的处处无分歧子扩张；其 Galois 群恰是右端的 $H_p/I_p$。这里“最大”仅在这个已知 Kummer 扩张内部，不是整个无分歧类域。

将 (3.2) 再接上
$$
H_p/I_p\twoheadrightarrow H_p/I_p^{\rm sat}\simeq\mathbb Z_p
$$
就得到 R35 的 $\lambda_p:D_p\twoheadrightarrow\mathbb Z_p$，至多相差一个单位。准确地，其未饱和的已知点行是
$$
p^{-r_p}(\ell_Q,-\ell_P),\qquad
r_p=\min\{v_p(\ell_P),v_p(\ell_Q)\};
$$
它消去 (2.2)，而对在 $H_p$ 上的整数像进行饱和，正是 R35 的定义。

若 $N_p=\ker\lambda_p$，由 (3.2) 得到另一方向的准确序列
$$
\boxed{\quad
0\longrightarrow\Sha(E/\mathbb Q)[p^\infty]^\vee
\longrightarrow N_p
\longrightarrow I_p^{\rm sat}/I_p\longrightarrow0.
\quad}
\tag{3.3}
$$
这正是 R35 式 (5.5) 的对偶，并将其有限项实现为具体 Kummer 扩张的惯性饱和误差。若该 $p$ 的 $\Sha$ 有限，则
$$
|N_p|=p^{e_p^{\rm MW}}|\Sha(E/\mathbb Q)[p^\infty]|;
\qquad
|N_p|=p^{b_p}|\Sha(E/\mathbb Q)[p^\infty]|
\quad(p\nmid I).
\tag{3.4}
$$
没有选择一个不明的 MW 补空间来把 $N_p$ 与 $\Sha^\vee$ 宣称典范直和。

## 4. 为什么这个无分歧方向不是固定代数行

按 Bertrand-height-and-completed-strict-line 笔记已经核查的 Fuchs–Pham $p$-adic analytic subgroup theorem，$P,Q$ 的 $\mathcal O_K$-独立性给
$$
a\ell_P+b\ell_Q=0,\quad a,b\in\overline{\mathbb Q}
\quad\Longrightarrow\quad a=b=0.
\tag{4.1}
$$
特别地，$\ell_Q/\ell_P$ 超越于 $\mathbb Q$。

假设一个非零代数系数行
$\varphi=(a,b)\in\overline{\mathbb Q}^{\,2}$ 在已知点坐标中消去惯性线
$\mathbb Q_p I_p$。由 (2.2)，必须有
$a\ell_P+b\ell_Q=0$，与 (4.1) 矛盾。因此
$$
\boxed{\quad
\text{在固定 }P,Q\text{ 坐标中，没有非零代数系数行给出该严格商。}
\quad}
\tag{4.2}
$$
尤其不能用固定格 $[\mathcal O_K^2\to E]$ 的一个固定代数线性关系来代替 $\lambda_p$。这个陈述限定于明确的已知点坐标和格上关系；不从它推断任意 $p$-adic Galois 商都必须来自代数几何。

另一方面，整个秩二 Kummer 塔本身确由固定对象给出，(1.8) 甚至准确写出它接收的全局类群商。这仍没有限制 (3.2) 左端：已知商的秩是二，只给全局模的秩下界。要完成主问题，仍需对无穷多个 $p$ 控制该商之外的核，或证明 R35 的一个整 Rubin–Stark 值在中心非零。固定 1-motive 的存在、两个对数分别非零以及 Chebotarev 的辅助素数选择，都没有给出这个额外的上界。

## 来源与接口

- R7、R27、R34–R36：全局及局部 Kummer 比较、直接字符、局部范数控制、完整整数互反常数及有限 MW 误差；本文的 (1.8)、(2.2)、(3.2) 是这些已证映射的明确组合。
- J. Fuchs、D. H. Pham，*Applications of the $p$-adic analytic subgroup theorem*，Theorems 1.1、2.2，[作者全文](https://arxiv.org/pdf/1412.1248)。只用其代数系数线性独立性，不用未证明的二次式或调节子非零。
- 与 one-motive-localization-barrier、one-motive-auxiliary-torsion 两篇笔记区别：本文不交换无限个局部积与张量，也不把辅助素数的有限挠子消失作为假设；全部关键序列来自本曲线已经核查的整 Selmer 与类域论比较。
