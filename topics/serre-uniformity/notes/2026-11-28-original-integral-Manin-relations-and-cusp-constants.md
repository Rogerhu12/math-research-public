# 原尖点单位关系的整 p-primary 剩余、全尖点规范与常数消去

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**范围。** 本文给出原实际 modular-unit symbols 的一个关系提升定理。它只把已经在原函数格中定义、且已证明有理为零的常角色关系提升到 $p$-local 整 $K_2$；不证明任意两个原 Kummer 类的杯积为零，不构造四阶覆盖，也不把 $K_2[p^\infty]$ 与 $K_2/p$ 混同。全文为纸面证明，没有数学程序执行。

## 1. 原函数、系数与输入条件

固定 $p>37$，
$$
K=\mathbf Q(\zeta_p),\quad F=K^+,\quad
\Delta=\operatorname{Gal}(K/\mathbf Q),\quad
X=X_{\rm ns}^+(p),\quad Y=X_K-\mathscr C.
$$
原全部 $m=(p-1)/2$ 个几何尖点在 $F$ 上分裂。因此复共轭 $c\in\Delta$ **逐个固定** $\mathscr C$，不仅保持这个集合。记
$$
A=K_2(K(X))\otimes_{\mathbf Z}\mathbf Z_{(p)},\qquad
e_0=\frac1{p-1}\sum_{\sigma\in\Delta}\sigma .
\tag{1}
$$
$A[p^\infty]$ 指每个元素均被某个有限 $p$ 次幂杀掉的子群；不要求整个群有统一指数。

令 $\mathcal U_{\rm can}$ 为 R1064、R1070 的原实际 Siegel/Carlucci 乘积及其原全尖点规范生成的单位子群，保其实际函数代表。具体允许：

- 满足原整数指数条件、已经下降到 $K(X)$ 的原 Siegel 乘积；
- 原 $K/F$ norm、整数乘积、逆及 Galois 共轭；
- 以全部原 cusp leading 的乘积 $A(u)$ 所作的 $u^m/A(u)$ 规范；
- 原圆单位和根单位的常数乘积。

这里每个元素本来就在 $\mathcal O(Y)^\times$，不以“先取 $12p$ 次幂”替代指定 Kummer 函数。任意乘一个未经固定的 $K^\times$ 常数，不属于本文自动允许的规范操作。

定义原符号子群
$$
\mathcal S_{\rm can}
=\left\langle\,\{u,v\}:u,v\in\mathcal U_{\rm can}\,\right\rangle_{\mathbf Z_{(p)}}
\subset A.
\tag{2}
$$
只使用下列明确的 torsion 输入：
$$
\bigl(\ker s_{\mathscr C}[p]\bigr)^\Delta=0,
\tag{3}
$$
其中 $s_{\mathscr C}$ 在下一节构造。原 integral $K_2$ 笔记给 (3) 等价于
$J(K)[p]_{\omega^{-1}}=0$；[R1132](../results/R1132-original-full-Cartan-odd-cusp-and-constant-K2-torsion.md) 在 $p\nmid B_{p-3}$ 时为原曲线支付该输入。

**关系提升定理。** 若 (3) 成立，且 $z\in\mathcal S_{\rm can}$ 满足
$$
e_0z=0\quad\hbox{in }K_2(K(X))\otimes\mathbf Q,
\tag{4}
$$
则准确有
$$
\boxed{\ e_0z=0\quad\hbox{in }A.\ }
\tag{5}
$$
下面分别支付 finite $p$-power 剩余、全部 tame、specialization、原 leading 的算术整性及规范常数。不能由 (4) 直接略掉其中任何一项。

## 2. 不需 μ_(p^a) 的完整 specialization

令 $b\in X(K)$，$t$ 为实际局部参数。对 $u\in K(X)^\times$ 写
$u=t^{v_b(u)}u_0$，其中 $u_0$ 在 $b$ 为单位，并置
$\operatorname{ac}_t(u)=u_0(b)$。定义
$$
s_t\{u,v\}=\{\operatorname{ac}_t(u),\operatorname{ac}_t(v)\}
\quad\text{in }K_2(K).
\tag{6}
$$
这是整 $K_2$ 上的群同态。双线性明显；Steinberg 关系逐情形成立：

- $v_b(u)>0$ 时，$\operatorname{ac}_t(1-u)=1$；
- $v_b(u)<0$ 时，$\operatorname{ac}_t(1-u)=-\operatorname{ac}_t(u)$，用 $\{a,-a\}=0$；
- $v_b(u)=0$ 时，若 $\operatorname{ac}_t(u)\ne1$，两首项相加为 $1$；若它等于 $1$，第一槽已为 $1$。

设 $t'=a t$，$a$ 为局部单位，$\lambda=a(b)$。按与原笔记相同的 tame 约定，
$$
\partial_b\{u,v\}
=(-1)^{v_b(u)v_b(v)}
 \frac{\operatorname{ac}_t(u)^{v_b(v)}}
      {\operatorname{ac}_t(v)^{v_b(u)}}.
$$
直接展开 (6)，并用 $\{\lambda,\lambda\}=\{\lambda,-1\}$，得到
$$
s_{t'}(\xi)-s_t(\xi)=\{\lambda,\partial_b\xi\}.
\tag{7}
$$
因此在 $\partial_b\xi=1$ 的子群上，(6) 不依赖参数。记此限制为
$\operatorname{sp}_b$。等价地，它是 Milnor residue
$\partial_t(\{-t\}\cdot\xi)$，但前述证明已直接给出其整性与参数无关性。

定义
$$
A_{\rm nr}=\{\xi\in A:\partial_x\xi=1\text{ 对全部闭点 }x\}.
$$
每个 $\operatorname{sp}_b:A_{\rm nr}\to K_2(K)\otimes\mathbf Z_{(p)}$
在常数上为恒等，且随实际 Galois 作用重标。故
$$
s_{\mathscr C}=\frac1m\sum_{b\in\mathscr C}\operatorname{sp}_b
\tag{8}
$$
是 $\Delta$-等变的常数 retraction。这里 $p\nmid m$，所以 (8) 在整个
$A_{\rm nr}$ 上合法，特别在全部 $p$-primary torsion 上合法。
不需要在 $K$ 中加入 $\mu_{p^a}$，也没有把仅对 $[p]$ 已证明的 Suslin 表示公式复制到 $[p^a]$。

由 (3)，立即推出
$$
\bigl((\ker s_{\mathscr C})[p^\infty]\bigr)^\Delta=0.
\tag{9}
$$
否则取一个非零元素的最高非零 $p$ 倍，就仍在同一规范 kernel 和同一 $\Delta$-平凡角色中，且阶为 $p$，与 (3) 矛盾。局部化到 $\mathbf Z_{(p)}$ 不产生新的阶 $p$ 元素：若代表 $u/s$ 被 $p$ 杀，乘一个与 $p$ 互素的整数即可由原整 $K_2[p]$ 代表它。

同一论证也适用于 R1131 已消去的其它指定偶角色；本篇的实际常数消去与结论 (5) 只针对 $e_0$。

## 3. 实尖点使偶 torsion 的 tame 自动消失

取 $\xi\in A[p^\infty]$，假设它在 $Y$ 无 tame，且 $c\xi=\xi$。
对 $b\in\mathscr C$，$\partial_b\xi$ 是
$K^\times\otimes\mathbf Z_{(p)}$ 的有限 $p$-power 扭元。
其扭子群来自 $K$ 的根单位；$K=\mathbf Q(\zeta_p)$ 不含
$\mu_{p^2}$，所以其 $p$ 部正是 $\mu_p$。

$c$ 固定 $b$，而在 $\mu_p$ 上取逆。故 tame 的等变性给
$$
\partial_b\xi
=\partial_b(c\xi)
=c(\partial_b\xi)
=(\partial_b\xi)^{-1}.
\tag{10}
$$
$p$ 为奇数，(10) 迫 $\partial_b\xi=1$。
因此 $\xi\in A_{\rm nr}$。

现在令 $z_0=e_0z$，其中 $z$ 满足定理条件。
(4) 说明 $z_0$ 是 $A$ 的 torsion；在 $p$-local 系数下它被某个有限 $p$ 次幂杀掉。它由 $Y$ 上实际单位符号构成，因此在 $Y$ 无 tame；它又是 $\Delta$-平凡的，所以 (10) 支付全部原 cusps，得到
$$
z_0\in A_{\rm nr}[p^\infty]^\Delta.
\tag{11}
$$
这个论证不宣称任意单位符号的 tame 为零；有限 $p$-power torsion 和偶角色两项均被使用。

## 4. 原 Siegel leading 确为 S-units

置
$$
\mathcal O_{K,S}=\mathcal O_K[1/(6p)],\qquad S=\{2,3,p\}.
$$
在原标准 Tate cusp 参数中，Siegel 函数
$g_{a/p,b/p}$ 的首项是根单位，或根单位乘 $1-\zeta_p^b$；
后一种情形是第一坐标为零而第二坐标非零。
这是其原两列 $q$-乘积的直接首项，不是有理化单位群中的等式。
对其它 cusp，真实 $\mathrm{SL}_2(\mathbf Z)$ 变换重标
$(a,b)$ 并乘根单位。

单个解析相位可以先在一个仅于 $2,3,p$ 分歧的有限 cyclotomic 扩域中读取。
但本文单位已经是 $K(X)$ 中的实际函数，故其完整首项在 $K$；
在扩域中为 $S$-unit 的元素与其逆都整，因而下降后仍为
$\mathcal O_{K,S}$ 的单位。
此外
$$
N_{K/\mathbf Q}(1-\zeta_p^b)=p
\qquad (p\nmid b).
$$
所以原完整乘积的每个 leading coefficient 都在
$\mathcal O_{K,S}^\times$。
整数乘积、逆、Galois 运输与原 $K/F$ norm 都保持此性质。
原 $A(u)$ 是全部 cusp leading 的乘积，因此
$u^m/A(u)$ 的每个 leading 同样是 $S$-unit。

若使用 R1070 的原 $\psi_c$ 乘积代表，(1070.24) 给其 leading 的平方是上述 $S$-unit；因有限素的 valuation 为整数，其 leading 本身也是 $S$-unit。

这些都是 R1064 原指数格及 R1070 (1070.19)–(1070.30) 的实际函数。
没有提升其 $p$ 次幂来消相位，也没有修改原 Kummer 类。
之所以保 $S=\{2,3,p\}$，是为了让全部 theta/cusp 规范的整性足够而无须另减小支撑；下面三处都没有基域 $p$ 扭。

由 (6)，对 $z_0$ 的每个 specialization，准确有
$$
\operatorname{sp}_b(z_0)
\in
\operatorname{im}\left(
 K_2(\mathcal O_{K,S})\otimes\mathbf Z_{(p)}
 \longrightarrow K_2(K)\otimes\mathbf Z_{(p)}
\right).
\tag{12}
$$
例如 $z_0=\sum_i a_i\{u_i,v_i\}$ 时，
$\operatorname{sp}_b(z_0)=\sum_i a_i
\{\operatorname{lead}_b(u_i),\operatorname{lead}_b(v_i)\}$。
这是双线性的实际 leading 符号和；不能由两个单位分别
$A(u),A(v)$ 规范就直接把它置零。

## 5. 把规范常数真实降到 Q 后消去

有限域的 $K_2$ 为零，因此 Dedekind localization 给单射
$$
K_2(\mathcal O_{K,S})\hookrightarrow K_2(K).
\tag{13}
$$
令 $a=s_{\mathscr C}(z_0)$。由 (8)、(11)–(13)，$a$ 是
$K_2(\mathcal O_{K,S})\otimes\mathbf Z_{(p)}$ 像中的
$p$-primary torsion，且被 $\Delta$ 固定。
这里始终是 $s_{\mathscr C}(e_0z)=e_0s_{\mathscr C}(z)$；
没有对未经投影的平均假定 $\Delta$-不变。

域 transfer $N_{K/\mathbf Q}$ 与 tame 相容，所以
$$
N_{K/\mathbf Q}(a)
\in K_2(\mathbf Z[1/(6p)])\otimes\mathbf Z_{(p)}.
\tag{14}
$$
亦可用 $\mathcal O_{K,S}/\mathbf Z[1/(6p)]$ 的有限 étale transfer。
在基域，$K_2(\mathbf Z)=\mathbf Z/2$，
而新增 localization residues 是
$\mathbf F_2^\times,\mathbf F_3^\times,\mathbf F_p^\times$；
它们都没有 $p$ 部。因此
$$
K_2(\mathbf Z[1/(6p)])\otimes\mathbf Z_{(p)}=0.
\tag{15}
$$
(14) 为零。Galois transfer 的 Mackey 等式给
$$
\operatorname{res}_{K/\mathbf Q}N_{K/\mathbf Q}(a)
=\sum_{\sigma\in\Delta}\sigma a=(p-1)a.
\tag{16}
$$
$p-1$ 在 $\mathbf Z_{(p)}$ 为单位，故
$$
s_{\mathscr C}(z_0)=a=0.                              \tag{17}
$$
于是 (11)、(17) 及 (9) 给 $z_0=0$，证明 (5)。

## 6. 对原 Manin/cochain 任务的准确消费接口

可以按以下顺序消费已发表的有理 Manin 关系：

1. 先给原整数指数和实际函数恒等式，使拟议的组合确实是
   $\mathcal S_{\rm can}$ 中的一个 $z$。这个步骤必须保原函数代表，
   原 cusp leading 和实际 Cartan/Galois 作用。
2. 用 Manin／Steinberg 关系证明 (4)。若引用的关系在
   $\mathbf Z[1/(6p)]$ 中成立，则在已有的 $p$-local 实际类上恰说明
   它是有限 $p$-power torsion，足够应用本文；不必再猜一个统一的消去指数。
3. 在 (3) 的范围内，(5) 给该**同一个**关系的整结论，且 §5 已支付全部规范常数。

这是从指定有理关系到整关系的接口，不是声称任意
$\{F_u,F_v\}$ 已在有理 $K_2$ 中为零。尤其：

- 用 $g_a^{12p}$ 创建一个新符号，再得到其关系，不能据此除回
  $p^2$ 并称原 Kummer 符号已零；
- 原 Kummer 类的给定整数提升及被 $p$ 除的 principal divisor 格，
  仍须在第一步实际辨认；
- integral $K_2[p^\infty]$ 中的关系提升，不等于
  $K_2(K(X))/p$ 中任意杯积消失；
- 四阶中央覆盖仍要求实际低阶 cochains、兼容性、算术下降和未分歧条件，
  本文不把形式角色和代替这些构造。

Brunault 已刊的 2008 三项关系在 $p>37$ 所需的 $3\nmid p$ 范围内有效。
本文并不为了引用该有理结论而消费更新未刊稿中的更强整分母结论；
若需要其显式 triangulation，仍应在原函数格中逐式复证。

## 7. 来源与复核

- 原 R1064、R1067、[R1070](../results/R1070-original-cuspidal-labels-by-division-polynomial-values.md)：实际曲线、实 cusp 域、Carlucci 整指数、
  theta/Siegel 相位、原全尖点 leading 规范。本文只用这些实际函数，
  不另挑代表来改掉 Kummer 类。
- [原 integral $K_2$ 笔记](2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md) §2–5：$[p]$ 的 Suslin 正合列与
  $\mu_p\otimes J(K)[p]$。本文 §2 单独证明整个 $p$-primary 的
  specialization 与最高 $p$ 倍步骤，未假设高次根单位存在。
- [R1131](../results/R1131-original-square-level-Eisenstein-lattice-and-odd-torsion.md)：指定非平凡偶角色的真实同素数整格消去。
  R1132：在 $p\nmid B_{p-3}$ 时原常角色条件 (3)。
- C. Weibel，*The K-book*，
  [Chapter III](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf)：
  Example 5.2.2（PDF 第36页）给 $K_2(\mathbf Z)=\mathbf Z/2$；
  Corollary 6.1.1（第48页）给有限域 $K_2=0$；
  Localization Theorem 6.5、Application 6.5.1（第52–53页）
  给 (13)、(15) 所需准确序列。
  §2 的 specialization 还按 Matsumoto 关系在本文自证。
- F. Brunault，*Beilinson–Kato elements in $K_2$ of modular curves*，
  Acta Arith. **134** (2008), 283–298，
  [正式全文](https://www.impan.pl/shop/en/publication/transaction/download/product/82036)：
  Theorem 1.4 及 §3 给所述有理 Manin 三项关系。
  其 proof 的最后一步只证明一个整数关系矩阵的 determinant 非零，
  没有证明该 determinant 是 $p$-unit；本文不偷加后者。

global_route 给出本文三步；
o2_high_coefficient 已独立纸核完整 $p$-primary specialization、
实 cusp 的 tame 消失及原 $S$-unit 常数 transfer。
关系 (5) 保持上述实际输入范围；原一般 $p$ 四阶覆盖及同点排除仍未完成。


精确全文复核：root、global_route、o2_high_coefficient 对候选cc0a4662全部七节独立纸核通过。root另核 Weibel III 的 Example 5.2.2、Corollary 6.1.1、Localization 6.5 / Application 6.5.1；本文specialization自证亦与其 Exercise 6.1、Theorem 7.3 一致。
