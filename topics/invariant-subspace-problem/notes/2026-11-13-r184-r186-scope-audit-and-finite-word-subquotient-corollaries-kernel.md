# R184/R186 的范围复核与有限词、矩形分母及子商推论

日期：2026-11-13（UTC）。作者：kernel；提交 Astra-ISP-1cf8c51d 复核。
性质：既有定理的完整推论与范围订正，不登记新的排核或循环范围。

## 1. 本轮扣除的重复范围

本轮曾拟把任意有限个 first 的联合最大闭图写作 R145 新附录。对更早的完整源补核后，这个表述必须撤回：

- [R186](../results/R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) §§2–6 已给共同正则器、全部混合域、任意有界交换系数多项式的自然闭包与最大图、原空间 $C$ 自伴、未知不变限制、任意循环域向量的图核心及闭和闭积演算；其 §10 已给共同指数权的全部混合 Bell 域及准确核接口。
- [R184](../results/R184-universal-subquotient-regularization-and-closed-polynomial-koszul-calculus.md) §§2–6 已给一个 first 的固定正则器在所有有限放大子商上的强主理想单位、最大闭包、自然诱导及再次取商相容性。
- [R183](../results/R183-fast-coefficient-nonmonic-polynomials-and-closed-fraction-field.md) 对 $a\in\ell^2\setminus\ell^1$、$Y=X+H$、$H\in\mathcal A$ 且全部 dyadic 增量属于 $\mathcal G$，已给非首一 $\mathcal G[Y]$ 排核、最大闭包、闭分式场和全空间循环性双向传递。实际倾斜 $H_{a,b}$ 符合这些条件；固定 dyadic 只改变有限低位。这覆盖 R270C §§1–8 和 R270D 的无界分支，不应再次登记为新增排核。
- [R152](../results/R152-fast-gauge-increments-analytic-germs-and-closed-quotients.md) 定理 1.3、§7 处理有界 $S\in\mathcal A$、全部 dyadic 增量属于 $\mathcal G$ 的任意快系数多项式。$a\in\ell^1$ 时的实际 $X_b$ 符合它，故覆盖上述有界分支；必须保留实际 $P(X_b)\ne0$。其有理分支 §7.2 另保未知限制稠密，超越分支 §7.3 只得全空间结论。
- R270C §§9–10 的全阶共振 $F_p$ 是把真实 Bell 慢项准确消去后调用这些旧排核定理的应用；不能因排核底座已有，就把全阶生成式的构造也一并删去。R270E 的独立快辅助组合和 R270F 的不交慢点态乘积保各自完整证明范围。
- R186 §4.4 已有多项式闭乘积演算。把已知单射的单模式因子代入，只是直接推论；不属于一般不可约多变量排核。

本笔记只把 R186 的共同域表述扩写成任意选定词的实际自然域，并把其有限模式正则器放入 R184 的子商证明。后者是两项既有结果的直接组合，以下仍完整核对域，不把“多变量分式场”附会进去。

当前目录核对未见本课题 R186 后续独立附录；相关既有原稿与正式稿同源。已读主要 blob：
R186 为 66996b15f4ce60ac774efe6a63bd9b1820252260，
R184 为 37b34adcc351f6eae46551f15dd58a3ea4238350，
R183 为 66e361697ba189b97650b175eb6056163e441bda；R152 为 581d07f4f8be448a3a987aa24d4ab1412f4d9f1f。

## 2. 所有有限旗子商上的矩形分母

记 $\mathfrak C=\{A\}'$。固定有限个实际闭 first，允许各自加任意固定有界交换子：
$$
Y_i=X_{u_i}+H_i,\qquad H_i\in\mathfrak C,\qquad 1\le i\le d.
$$
这里没有因任意 $H_i$ 有界，就假定其满足某个排核定理的额外 gauge 条件。

对各 first 取实际正则器族
$$
R_i(s)\in\mathfrak C,\qquad
S_i(s)=Y_iR_i(s)\in\mathfrak C,\qquad R_i(s)\to I\ {\rm SOT},
$$
$$
R_i(s)=R_i(t)U_i(s,t),\qquad
S_i(s)=S_i(t)U_i(s,t),\qquad U_i(s,t)^{\pm1}\in\mathfrak C.
\tag{2.1}
$$
这些正是 R140、R184、R186 使用的真实单位关系；有界扰动只改变 $S_i$。

固定有限放大的闭不变旗子
$$
\mathcal N\subseteq\mathcal M\subseteq H^{(r)},\qquad
\mathscr Q=\mathcal M/\mathcal N.
$$
每个 $D\in\mathfrak C$ 都诱导为 $D_{\mathscr Q}$，并在 $A_{\mathscr Q}$ 的强多项式闭包中。该断言使用同一多项式对有限组商向量代表逼近，是 R184 §2.1 的论证。

对固定 $t>0$，
$$
R_i(t)_{\mathscr Q}\text{ 单射，且像稠密}.
\tag{2.2}
$$
直接证明如下。若 $R_i(t)^{(r)}x\in\mathcal N$，则 (2.1) 给
$R_i(s)^{(r)}x\in\mathcal N$，令 $s\downarrow0$ 得 $x\in\mathcal N$。
又各 $R_i(s)_{\mathscr Q}$ 的像由单位关系相同，且强趋于恒等，因此该像稠密。

更强地，(2.1) 加上强多项式逼近给
$$
I_{\mathscr Q}\in
\overline{R_i(t)_{\mathscr Q}^{\,n}\mathbb C[A_{\mathscr Q}]}^{\rm SOT}
\qquad(n\ge0).
\tag{2.3}
$$
同一证明适用于 $\mathscr Q$ 的所有有限放大和其闭不变旗子。

对任意有限矩形指数 $m=(m_1,\ldots,m_d)$，固定参数并置
$$
Z=\prod_iR_i^{m_i}.
\tag{2.4}
$$
有限次使用 (2.3) 或逐因子逼近给
$$
I_{\mathscr Q}\in
\overline{Z_{\mathscr Q}\mathbb C[A_{\mathscr Q}]}^{\rm SOT}.
\tag{2.5}
$$
因而 $Z_{\mathscr Q}$ 单射、像稠密；在任何闭不变 $L\subseteq\mathscr Q^{(k)}$ 上还满足
$$
\overline{Z_{\mathscr Q}^{(k)}L}=L,\qquad
Z_{\mathscr Q}^{(k)}x\in L\Longrightarrow x\in L.
\tag{2.6}
$$
这只是 R184 的普遍分母性质，有限个 first 的乘积保留它。

## 3. 子商中的 first 与任意单词自然域

在 $\mathscr Q$ 上定义各 first 的规范闭实现
$$
\widehat Y_i=(R_i)_{\mathscr Q}^{-1}(S_i)_{\mathscr Q}.
\tag{3.1}
$$
R184 §3 给其稠密最大域、原分母图核心和与原实际 first 的限制／诱导相容性。

所有诱导的有界交换子完整交换每个 $\widehat Y_i$：若
$(S_i)_{\mathscr Q}x=(R_i)_{\mathscr Q}y$，乘任意 $D_{\mathscr Q}$ 仍满足同一方程。因此它们保持每个真正的自然词域，逐个字母交换。

取有限个有序词 $W_\omega$，按指定顺序组成这些闭 first。
每个词保留自己的实际自然域，不先把它们缩到 R186 的全部长度不超过 $p$ 的共同域。
用 $\alpha(\omega)$ 记计数，选
$$
m_i\ge\max_\omega\alpha_i(\omega).
$$
若另要求有限个额外词也有定义，$m$ 同时覆盖这些额外词的计数。
取系数 $E_\omega\in\mathfrak C$，令
$$
P_{\rm nat}=\sum_\omega(E_\omega)_{\mathscr Q}W_\omega
$$
定义于所列全部实际词域的交。

置
$$
Q_\omega=\prod_iS_i^{\alpha_i(\omega)}
R_i^{m_i-\alpha_i(\omega)},\qquad
Q=\sum_\omega E_\omega Q_\omega.
\tag{3.2}
$$
逐个实际字母施加可证明
$$
\boxed{
Z_{\mathscr Q}\mathscr Q\subseteq\operatorname{Dom}W_\omega,\qquad
W_\omega Z_{\mathscr Q}=(Q_\omega)_{\mathscr Q}.
}
\tag{3.3}
$$
确实，每到下一字母 $i$，尚余的分母中至少有一个 $R_i$；其余因子有界且保持该 first 的域，所以可把此 $R_i$ 换为 $S_i$。该归纳没有假设无界 first 的两个原乘积域相同。

在整个原自然词域上，又由有界分母的逐字域交换得到
$$
Z_{\mathscr Q}W_\omega x=(Q_\omega)_{\mathscr Q}x.
$$
因此
$$
P_{\rm nat}Z_{\mathscr Q}=Q_{\mathscr Q},\qquad
Z_{\mathscr Q}P_{\rm nat}x=Q_{\mathscr Q}x.
\tag{3.4}
$$
这两式分别给核心的包含与整个自然图的包含，缺一不可。

## 4. 同一个最大闭包及对词域的独立性

定义
$$
\mathscr G=
\{(x,y)\in\mathscr Q^2:Q_{\mathscr Q}x=Z_{\mathscr Q}y\}.
\tag{4.1}
$$
由分母单射，这是单值闭图；它包含
$(Z_{\mathscr Q}h,Q_{\mathscr Q}h)$，故定义域稠密。
该图闭且 $A_{\mathscr Q}\oplus A_{\mathscr Q}$ 不变。

应用 (2.6) 于这张图，有
$$
\overline{Z_{\mathscr Q}^{(2)}\mathscr G}=\mathscr G.
$$
而
$$
Z_{\mathscr Q}^{(2)}(x,y)
=(Z_{\mathscr Q}x,Q_{\mathscr Q}x).
$$
所以
$$
\boxed{
\mathscr G
=\overline{\{(Z_{\mathscr Q}h,Q_{\mathscr Q}h):h\in\mathscr Q\}}.
}
\tag{4.2}
$$
自然图由 (3.4) 包含 (4.2) 的核心，并包含于 (4.1)。于是
$$
\boxed{
\overline{P_{\rm nat}}=
Z_{\mathscr Q}^{-1}Q_{\mathscr Q}.
}
\tag{4.3}
$$

这与先使用 R186 的完整共同域再取闭包相同。原因是完整共同域也包含足够高共同分母的参数核心，且自然图满足相同最大方程；可直接用 R186 §4，或重复上述夹逼。

若改变词序，相同计数的有界 $Q_\omega$ 不变；故闭包不变。
若改变分母，记另一组为 $Z',Q'$，则真实核心上的计算给有界等式
$$
QZ'=Q'Z.
$$
由于诱导分母仍单射，该等式双向识别两个最大图。
它同时处理矩形指数、填充次数、固定参数的改变。

原自然词域可以不同，原自然乘积也可以不闭。本节只说明这些自然图具有同一个闭包；没有宣称额外的强交换意义。

## 5. 与先限制、先取商及再次取商相容

令 $T=Z^{-1}Q$ 为原 $H$ 上同一多项式的最大闭实现。
R186 已证明其保持每个闭不变空间的域内部分；亦可由 (2.6) 的饱和性直接核验：
$x\in L$ 且 $ZTx=Qx\in L$ 迫使 $Tx\in L$。

在有限放大上先取 $T^{(r)}$ 的实际部分于 $\mathcal M$，再作对 $\mathcal N$ 的代数诱导。
若两个域代表相差于 $\mathcal N$，其像差仍在 $\mathcal N$，所以诱导单值。
所得自然诱导图包含于 (4.1)。

另一方面，原限制图含全部
$$
(Z^{(r)}h,Q^{(r)}h),\qquad h\in\mathcal M.
$$
它们投影成商上所有原分母参数对。因此
$$
\boxed{
\overline{\text{原最大多项式在 }\mathcal M/\mathcal N
\text{ 的自然诱导图}}
=
\operatorname{Graph}\bigl(Z_{\mathscr Q}^{-1}Q_{\mathscr Q}\bigr).
}
\tag{5.1}
$$
结合 (4.3)，右端同时等于先闭合诱导的各 first、再取它们的自然多项式闭包。
所以这两个程序确实给同一个闭算子。

对 $\mathscr Q$ 中进一步的闭不变子空间，(2.6) 再给域保持；
参数图投影仍覆盖下一级商的全部参数图，因此 (5.1) 可继续迭代。
这就是 R184 §6 的证明用于 R186 的有限模式共同分母，没有新增分子稠密假设。

原 $H$ 上的 $C$ 自伴性已经由 R186 证明。在一般子商上，本笔记只给最大闭图与自然闭包；没有自然的同一个 $C$，不能把该自伴性降下去。

## 6. 剩余问题没有改变

(4.3) 准确给
$$
\ker\overline{P_{\rm nat}}=\ker Q_{\mathscr Q},\qquad
\overline{\operatorname{Ran}\overline{P_{\rm nat}}}
=\overline{Q_{\mathscr Q}\mathscr Q}.
$$
一般分子 $Q_{\mathscr Q}$ 未被证明单射或像稠密。
因此这些接口既不建立多变量分式场，也不清空任何一般不可约慢耦合核。

把已知单射的原空间单模式多项式作为闭因子，R186 §4.4 与有界分子相乘给其闭积单射稠密、全空间循环性双向传递；这是既有结论的推论。任意有界 $H_i$ 的域构造范围不能自动当作 R183 或 R270 排核范围。

研究应继续处理同模不同根共振、两个独立慢方向的单核，以及普通 Hilbert ISP；不把本次范围整理当作这些目标已经完成。
