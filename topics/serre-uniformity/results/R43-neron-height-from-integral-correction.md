# R43. 实际积分修正与坏素数处的 Néron／QC 局部高度

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明。** 本文把 R30、R33、R39 的实际垂直系数接到非辅助素数处的真实局部高度。主构造使用全部尖点除子 $D$，**不要求 $X(\mathbb Q)$ 有基点**。设层素数为 $p$，高度取值于 $\mathbb Q_\ell$，$\ell\ne p$；对已指定实际截面的无基点 Néron 高度 $H_{D,F,p}$，若局部点 $x,y$ 分别特化到分量 $i,j$，则
$$\boxed{\quad
H_{D,F,p}(x)-H_{D,F,p}(y)
=-\frac{k_i(F)-k_j(F)}2\log_\ell(p).
\quad}$$
因此 R39 的 $T_2$ 方向在坏素数 $p$ 的局部高度至多有 **4 个值**；当 $p\equiv1,9,25\pmod {56}$ 时，该高度为常数。若另取一个**局部**基点 $b\in X(\mathbb Q_p)$，与通常基点 Nekovář 高度的比较是 $h^{\rm Nek}_{F,p,b}(x)=(k_i-k_{i_b})\log_\ell(p)/(2d^2)$，其中 $d=(p-1)/2$；它不要求 $b\in X(\mathbb Q)$。$gT_2-\operatorname{Tr}(T_2)\mathrm{id}$ 在 $p>37$ 非零。

本结果不假设这个方向已经满足某个全局 Mordell–Weil 秩条件，也不把它自动投影到 Dogra–Le Fourn 所选的商 Jacobian。它控制的是确定的坏 $p$ 局部项；辅助素数 $\ell$ 处的迭代积分与全局高度仍保留。

## 1. 非辅助素数处唯一的双扩张高度

先作一个一般局部构造。设 $K/\mathbb Q_p$ 为有限扩张，$R$ 为整数环，$A/K$ 为阿贝尔簇，$A^\vee$ 为对偶；$\mathcal A,\mathcal A^\vee$ 为 Néron 模型。令 $\mathcal P$ 为带两个零轴刚性化的 Poincaré 线丛。已知其延拓
$$\mathcal P^{\rm ext}\quad\text{在}\quad
\mathcal A\times_R\mathcal A^{\vee,0}$$
是唯一的积分双扩张；见 Edixhoven–Lido Proposition 6.7.1。

固定辅助素数 $\ell\ne p$ 和连续加法字符
$$\chi:K^\times\longrightarrow\mathbb Q_\ell.$$
该字符在 $R^\times$ 上为零：主单位群有一个开 pro-$p$ 子群，它到加法 $\mathbb Q_\ell$ 的连续同态为零，余下商有限而目标无挠。故 $\chi(c)=v_K(c)\chi(\pi)$，其中 $v_K(\pi)=1$。

对 $x\in A(K)$、$y\in\mathcal A^{\vee,0}(R)$，其拉回积分线
$$P^{\rm ext}_{x,y}=R\cdot e$$
自由秩一。对非零泛纤维向量 $t=ce$ 定义
$$\lambda_\chi(t)=\chi(c).\tag{1.1}$$
换 $R$-基只乘单位，所以定义无歧义。它在所有积分可逆向量上为零。

对任意 $y\in A^\vee(K)$，取一个正整数 $m$，使 $my\in\mathcal A^{\vee,0}(R)$。双扩张的第二群律给出
$$t^{\otimes_2m}\in P_{x,my}^\times(K).$$
令
$$\lambda_\chi(t)=\frac1m\lambda_\chi(t^{\otimes_2m}).\tag{1.2}$$
当需要时可用分量群指数作共同的 $m$。

**引理 1。** (1.2) 与 $m$ 无关，是唯一满足以下条件的连续双扩张 splitting：

1. $\lambda_\chi(ct)=\chi(c)+\lambda_\chi(t)$；
2. 对 Poincaré 的两个部分群律都可加；
3. 两个零轴上与给定刚性化相容。

它也与阿贝尔簇同态的对偶性和 Poincaré 的规范转置同构相容。

**证明。** 两个可用整数可同乘到公倍数。积分双扩张的群律使积分基的张量积仍为积分基，所以 (1.1) 对两个群律可加；这证明公倍数上的计算相同，也证明 (1.2) 的前两项性质。零轴刚性化同样由积分延拓保留。局部平凡化中的赋值局部常值，故连续。

若有两个这样的 splitting，差值在 $\mathbb G_m$ 纤维上不变，所以下降为 $A(K)\times A^\vee(K)\to\mathbb Q_\ell$ 的连续双加性函数。固定其中一个变量，另一变量的定义域是一个紧 $p$ 进 Lie 群，具有开 pro-$p$ 子群，商有限。它到加法 $\mathbb Q_\ell$ 的连续同态必须为零。因此差值为零。将 splitting 经对偶性或转置同构拉回仍满足这些性质，唯一性给出最后一句。证毕。

这个函数是非辅助素数处的 Néron 双扩张局部高度。用互不相交的次数零除子 $D,E$ 表示 Jacobian 点时，它与通常的 Néron／Coleman–Gross 局部配对相同：在范数描述中
$$\lambda_\chi(E^*c)=\chi(c)+h_\chi(D,E).\tag{1.3}$$
这里 $E^*c$ 表示 $\operatorname{Nm}_E\mathcal O(D)$ 中以规范有理截面表示的向量。其相容性也可从正则模型上的交数定义直接看出：将一个除子加有理垂直除子修正到全分量次数零后，范数向量的赋值就是修正后的交数；乘 $\chi(\pi)$ 得局部配对。主除子的变换公式 $h_\chi(D,\operatorname{div}f)=\chi(f(D))$ 保证更换代表不影响 (1.3)，双加性给两个群律，再由引理 1 的唯一性识别。DHS 的 Lemma 4.13 将同一计算写成非辅助素数处的局部高度公式。

**符号约定。** 对 $K=\mathbb Q_p$、通常圆分 $\ell$ 进全局高度，取
$$\chi_p(p)=-\log_\ell(p),\qquad \chi_p(\mathbb Z_p^\times)=0.\tag{1.4}$$
这是使主有理数的各局部字符之和为零的约定。若采用相反全局字符，全文高度同时变号，有限取值数与恒零结论不变。有限非分歧基扩张使用经次数归一化的范数字符，使 $\chi_p(p)$ 保持 (1.4)。

## 2. 无基点族与通常基点族相差 $d^2$ 和常数线

设 $X/K$ 光滑射影几何连通，$J=\operatorname{Pic}^0(X)$，$D$ 是次数 $d>0$ 的有效除子。设 $b\in X(K)$，
$$i_b(x)=[x-b],\qquad e_b=[db-D],\qquad
u_D=d i_b+e_b.$$
令 $a:J^\vee\to J$ 为 Abel–Jacobi 拉回；$f:J\to J^\vee$ 满足 R14 的次数零条件。记
$$\kappa_b=[(i_b,fi_b)^*\mathcal P]\in J(K),
\qquad q_b=a^{-1}\kappa_b.$$
相应基点族和无基点族是
$$h_b(t)=f(t)-q_b,\qquad
h_D(t)=f(t)-a^{-1}\eta_D,$$
其中 R14 的已证明恒等式为
$$a^{-1}\eta_D=dq_b+(f+f^\vee)e_b.\tag{2.1}$$
于是
$$h_Du_D=d\,h_bi_b-f^\vee e_b.\tag{2.2}$$

定义泛纤维上平凡的实际线丛
$$L_b=(i_b,h_bi_b)^*\mathcal P,\qquad
L_D=(u_D,h_Du_D)^*\mathcal P.$$
$L_b$ 在 $b$ 的纤维由第一变量为零而有规范基，故有唯一的处处非零全局截面 $s_b$，满足 $s_b(b)=1$。$L_D$ 任取一个处处非零全局截面 $s_D$；R14、R18、R33 给出了实际构造，而不只是几何 Picard 类。

**定理 2（带双扩张结构的基点比较）。** 有规范线丛同构
$$\boxed{\quad
L_D\simeq L_b^{\otimes d^2}\otimes_K C_b,
\quad C_b=P_{e_b,-dq_b-f^\vee e_b}.
\quad}\tag{2.3}$$
它与局部双扩张高度相容，因而
$$\boxed{\quad
\lambda_\chi(s_D(x))-\lambda_\chi(s_D(b))
=d^2\lambda_\chi(s_b(x)).
\quad}\tag{2.4}$$

**证明。** 置 $v=i_b(x)$。将 (2.2) 代入 Poincaré 纤维，并用两个群律展开：
$$\begin{aligned}
P_{dv+e_b,\,d(fv-q_b)-f^\vee e_b}
\simeq{}&P_{v,fv-q_b}^{\otimes d^2}
\otimes P_{v,f^\vee e_b}^{\otimes(-d)}\\
&\otimes P_{e_b,fv}^{\otimes d}
\otimes P_{e_b,-dq_b-f^\vee e_b}.
\end{aligned}$$
对偶性的规范同构 $P_{v,f^\vee e_b}\simeq P_{e_b,fv}$ 抵消中间两个因子，得到 (2.3)。这里没有要求 $f=f^\vee$；使用的是 R14 中准确的 $f+f^\vee$ 平移式。

两边截面的比是完整几何连通曲线上的可逆函数，所以是一个 $K^\times$ 常数；在 $b$ 处取值把该常数并入 $C_b$ 的固定向量。引理 1 使张量积、群律与对偶抵消均保持局部高度。因此 $s_D(x)$ 的高度等于 $d^2\lambda_\chi(s_b(x))$ 加一个与 $x$ 无关的常数；在 $b$ 处 $s_b(b)=1$ 的高度为零，减去此值即得 (2.4)。证毕。

这一步不是将一个任意 Picard 同构当成等距同构：同构 (2.3) 逐项来自实际双扩张群律和对偶性，局部高度相容性由引理 1 保证。

## 3. 积分模型给出的准确赋值

现在取 $X=X_{\rm ns}^+(p)$，$p\ge17$，$D$ 为全部尖点，$d=(p-1)/2$，数据定义于 $\mathbb Q_p$。在有限非分歧扩张后可看见涉及的几何分量，计算仍以 $v(p)=1$ 归一化。

对 R14 的实际规范族，R30 证明 $2h_Du_D$ 落于对偶 Néron 恒等分量。因此有真正的积分线丛
$$\mathscr L_D^{(2)}=(u_D,2h_Du_D)^*\mathcal P^{\rm ext}
\quad\text{在 }U=\mathcal X^{\rm sm}\text{ 上}.$$
它的泛纤维规范识别为 $L_D^{\otimes2}$。R28、R33 计算 $s_D^{\otimes2}$ 的除子为
$$\operatorname{div}_{U}(s_D^{\otimes2})=\sum_i k_i(F)U_i.\tag{3.1}$$
改变 $s_D$ 的常数只给全部 $k_i$ 加同一常数；所以差 $k_i-k_j$ 内在。

每个 $\mathbb Q_p$ 点都延拓到 $U$：共同奇点 $P$ 满足 $p\in\mathfrak m_P^\rho$、$\rho>1$，一个分歧度 $1$ 的截面不可能经过它，见 R33。有限非分歧扩张上的点也一样。

**定理 3。** 若 $x,b\in X(\mathbb Q_p)$ 分别特化到 $U_i,U_{i_b}$，则
$$\boxed{\quad
\lambda_{\chi_p}(s_b(x))
=\frac{k_i(F)-k_{i_b}(F)}{2d^2}\chi_p(p).
\quad}\tag{3.2}$$

**证明。** 在 $x$ 的整数截面附近，(3.1) 表示 $s_D^{\otimes2}$ 恰为 $p^{k_i}$ 乘一个积分可逆基。没有额外依赖 $x$ 的单位高度，因为 $\chi_p$ 在整数单位上为零。因此
$$\lambda_{\chi_p}(s_D^{\otimes2}(x))=k_i\chi_p(p).$$
双扩张乘二给左侧等于 $2\lambda_{\chi_p}(s_D(x))$。对 $b$ 同理，相减后使用 (2.4)，得到 (3.2)。非分歧基扩张不改变已固定的赋值和字符归一化，故所得等式下降。证毕。

这个证明也覆盖相应分量上的所有局部点，而非只覆盖分量泛点；泛点计算确定 Cartier 除子后，正则性保证除子零的剩余因子在每个局部环中都是单位。

**主定义不需要基点。** 利用 R33 中一维常数线的任一非零有理向量固定 $s_D$，定义
$$H_{D,F,p}:X(\mathbb Q_p)\longrightarrow\mathbb Q_\ell,
\qquad H_{D,F,p}(x)=\lambda_{\chi_p}(s_D(x)).$$
这只使用 $D,F$ 和指定的常数线基，不要求 $X(\mathbb Q)$ 或预先选定的 $X(\mathbb Q_p)$ 基点。更换该基只加一个常数。直接由 (3.1) 得
$$\lambda_{\chi_p}(s_D(x))-\lambda_{\chi_p}(s_D(y))
=\tfrac12(k_i-k_j)\chi_p(p).\tag{3.3}$$
故有限取值数结论不依赖于存在全局有理 CM 基点。基点版只是按一个已有局部点把常数归零。

## 4. 与标准 QC 局部项的确切对应及符号

令 $F=a\circ f$ 来自一个实际对称对应线丛 $\mathcal B$，且 trace 为零。为表述通常的 divisor 公式，先选择一个实际对称 Cartier 对应代表 $Z$，使其不含对角线或两个 $b$ 轴，且不经过 $(b,b)$。在必要时，可先对 $\mathcal B$ 取平方，做下面的计算后再除以 $2$：平方后的交换线性化在对角线上为 $+1$，可取一个交换不变的有理截面，在对角线泛点及 $(b,b)$ 附近为单位。其存在性可由局部平凡化、弱逼近及对两因子交换取平均得到。因此这一步不要求原来含有恒等对应的虚除子能够不经处理直接与对角线相交。

记 $B=Z|_{X\times b}$、$K_Z=\Delta^*Z$。对避开有限支集的 $x$，令
$$E_x=Z|_{X\times x}+B-K_Z,\qquad
D_{Z^\top}(x,b)=K_Z-B-Z|_{X\times x}=-E_x.\tag{4.1}$$
它们次数为零，因为 trace-zero 等价于 $\deg K_Z=2\deg B$。类的计算是
$$[E_x]=F(i_b(x))-\kappa_b,$$
所以 (1.3) 中的范数线正是 $P_{i_b(x),h_bi_b(x)}$。

R33 的范数消去（这里取 $D=b,d=1$）还确定了截面：实际族
$$\mathcal B\otimes\operatorname{pr}_1^*
\bigl(\mathcal O(B)\otimes(\Delta^*\mathcal B)^{-1}\bigr)$$
在对角线和 $b\times X$ 上的规范有理截面相同。对称性使二者相消，所以其评价—范数截面就是以 $b$ 归一化的 $s_b$。因此在上述开集上有真正的配对等式
$$\lambda_{\chi_p}(s_b(x))=h_{\chi_p}(x-b,E_x).\tag{4.2}$$
这不是只比较两个次数零类；它还比较了范数中的实际向量。

Balakrishnan–Dogra (2018), Theorem 6.3 的局部高度比较（DHS Theorem 8.10 与 Proposition 8.11 以同一符号重述）给
$$h^{\rm Nek}_{F,p,b}(x)
=h_{\chi_p}(x-b,D_{Z^\top}(x,b))
=-\lambda_{\chi_p}(s_b(x)).\tag{4.3}$$
上述先平方的处理使对应与高度均乘 $2$，故除回去不改变等式。局部函数均连续，而避开的有限集合的补集在每个光滑 $p$ 进圆盘中稠密，故等式延拓到全部 $X(\mathbb Q_p)$，包括 $b$，且值在 $b$ 为零。

**定理 4（准确的坏 $p$ 高度公式）。** 用 (1.4)、(4.1)–(4.3) 固定约定后，
$$\boxed{\quad
h^{\rm Nek}_{F,p,b}(x)
=\frac{k_i(F)-k_{i_b}(F)}{2d^2}\log_\ell(p).
\quad}\tag{4.4}$$
它不要求 $r=g$：这里仅识别一个局部高度。若还要使用某个全局 QC 有限性定理，必须另外满足该定理的商 Jacobian、秩和对数映射条件。

对 R33 的小 Hecke 整数组合，设
$$w_i(F)=e_i(H_{ii}(F)-\nu_i(F)).$$
由于 $k_i=6n+dw_i$，(4.4) 简化为
$$\boxed{\quad
h^{\rm Nek}_{F,p,b}(x)
=\frac{w_i(F)-w_{i_b}(F)}{p-1}\log_\ell(p).
\quad}\tag{4.5}$$
若没有小次数条件，R33 保留尖点范数项时应将 $w_i$ 换成 $e_i(H_{ii}-\nu_i)-2\tau_i$；本文没有自行把一般的 $\tau_i$ 设为零。

## 5. $T_2$ 的统一四分支界和恒零剩余类

取
$$F_2=gT_2-\operatorname{Tr}(T_2|H^0(X,\Omega^1))\mathrm{id}.$$
对 $p>19$，$3<\rho$，所以 R33 的小次数条件成立。R39 已由实际固定点闭包和总拉回证明：除
$$j_i\in\{1728,8000,-3375\}$$
的至多三个超奇异分量外，$w_i(F_2)$ 都相等；这三个整数来自确切恒等式
$$\Phi_2(T,T)=-(T-1728)(T-8000)(T+3375)^2.$$

**推论 5（先给无基点陈述）。** 对任意辅助素数 $\ell\ne p$，无基点高度 $H_{D,F_2,p}$ 在 $X(\mathbb Q_p)$ 上至多有 $4$ 个值。若另有局部基点 $b\in X(\mathbb Q_p)$，则
$$\boxed{\quad
\#\{h^{\rm Nek}_{F_2,p,b}(x):x\in X(\mathbb Q_p)\}\le4.
\quad}\tag{5.1}$$
若
$$p\equiv1,9,25\pmod {56},$$
则无基点高度为常数，任意局部基点归一化的 $h^{\rm Nek}_{F_2,p,b}$ 恒为零。在 $p>37$ 时，$F_2\ne0$，故这不是零对应的形式例子。

**证明。** (3.3) 直接把 R39 的至多四个 $k_i$ 值转为无基点高度值；(4.5) 再给基点版本。只有在 $\mathbb Q_p$ 上可见的分量有局部点，所以实际值数还可能更小；若局部点集为空，界也成立。指定剩余类中，三个例外 CM $j$ 均普通，R39 证明所有 $w_i$ 相同，于是 (3.3) 为零，而 (4.5) 恒零。非零性已由 R39 的次数 $3$ 对应与 Abramovich gonality 下界完整证明。证毕。

更一般地，固定一个有限 Hecke 素数集合 $S$，当其全部素数满足 $q+1<\rho$ 时，R39 给出的
$$2+2\sum_{q\in S}q$$
也是任意多条实际 trace-zero 整数组合的**联合坏 $p$ 高度向量**的取值数上界。不能把每条的值集合独立作笛卡尔积：同一个局部点必须使用同一个分量，联合界保留这个相容性。

## 6. 这一结果对 O5 的准确贡献和限制

现在不再只是“某个积分 torsor 可能与高度有关”：式 (4.4) 给出了实际局部配对、基点归一化、双扩张截面和对应转置符号的完整接口。小 Hecke 的最终垂直数据确实给出标准 QC 的坏 $p$ 局部项；对 $T_2$，这个项有随层统一的有限分支数。

仍须保留以下数学问题。第一，某个适用于全部充分大层的 QC 有限性定理可能使用特定的秩等于维数商，$F_2$ 在完整 Jacobian 上非零并不自动说明它在该商上非零，也不说明它已经因子化到该商。投影到商会改变实际对应，不能原封不动继承小次数支集界。第二，辅助素数 $\ell$ 处的局部高度及迭代积分、全局高度的 Mordell–Weil 数据和各残数圆盘上的共同根排除，都没有被坏 $p$ 的四分支界解决。第三，(4.5) 中仍有分母 $p-1$；当 $\ell\mid p-1$ 时不能据此声称积分系数或单位导数。

这些限制不影响已经证明的局部高度公式和有限分支界，但阻止把它们当成 Serre 一致性的完成证明。

## 7. 已核对的原始文献

- B. Edixhoven and G. M. Lido, **Geometric quadratic Chabauty**, *Journal of the Institute of Mathematics of Jussieu* **22** (2023), 279–333, DOI [10.1017/S1474748021000244](https://doi.org/10.1017/S1474748021000244)；[作者版本](https://arxiv.org/abs/1910.10752)。Proposition 6.7.1 给积分 Poincaré 双扩张，Proposition 6.9.3 给积分范数格与垂直修正，§9.3 解释高度 splitting。
- J. Duque-Rosero, S. Hashimoto and P. Spelier, **Geometric quadratic Chabauty and $p$-adic heights**, *Expositiones Mathematicae* **41** (2023), no. 3, 631–674, DOI [10.1016/j.exmath.2023.05.003](https://doi.org/10.1016/j.exmath.2023.05.003)；[作者版本](https://arxiv.org/abs/2207.10389)。本文核对的作者版 v3 中，Proposition 3.10 证明范数上的高度 splitting，Lemma 4.13 给非辅助素数处的负交数公式，Theorem 8.10 和 Proposition 8.11 给 Nekovář 与对应除子的局部配对比较；这里精确使用这些已发表比较，不引用该文对一般系数积分性的猜测。
- J. S. Balakrishnan and N. Dogra, **Quadratic Chabauty and rational points, I: $p$-adic heights**, *Duke Mathematical Journal* **167** (2018), no. 11, 1981–2038, DOI [10.1215/00127094-2018-0013](https://doi.org/10.1215/00127094-2018-0013)；[作者版本](https://arxiv.org/abs/1601.00388)。Theorem 6.3 是式 (4.3) 所用的局部高度比较来源。
- R. F. Coleman and B. H. Gross, **$p$-adic heights on curves**, in *Algebraic Number Theory*, Advanced Studies in Pure Mathematics **17** (1989), 73–81。非辅助素数处使用经典 Néron 交数配对；辅助素数处才需要选择 Hodge splitting，本文不在后者声称同一赋值公式。
- 仓库 R14：实际规范平移与式 (2.1)。R18、R28：范数和积分 Poincaré 接口。R30、R33：乘二、实际 $k_i$ 与小 Hecke 范数。R39：真实对角交数的有限支集及 $F_2$ 非零性。
