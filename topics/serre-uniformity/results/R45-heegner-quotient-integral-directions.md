# R45. Heegner 商的维数下界与真正容许的积分 QC 方向

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明。** 设 $X=X_{\rm ns}^+(p)$，$p$ 为素数，$J=\operatorname{Jac}(X)$。令 $A$ 是 Dogra–Le Fourn 的 Heegner 商，$a=\dim A$；令 $n$ 是 R28 最小正则模型特殊纤维的几何分量数，即超奇异 $j$ 不变量数。本文证明：

1. 对所有 $p\ge151$，$T_2|_A$ 非标量，故存在明确的非零、消去互补商、trace-zero 的有理 Hecke 方向。
2. 对任意 $\varepsilon>0$，有无条件下界
   $$\boxed{\quad a\gg_\varepsilon p^{3/2-\varepsilon}.\quad}$$
   常数不在本文中显式化，并容许 Hoffstein–Lockhart／Siegel 下界的无效常数。
3. 真正属于 $A$、满足 Dogra–Le Fourn Chow–Heegner 条件的 trace-zero 整数 Hecke 格中，存在秩至少 $a-n$ 的子格，使 R30 的实际积分 Poincaré 族在全部光滑开集上平凡。因而充分大 $p$ 时，这个子格非零，且其秩也为 $\gg_\varepsilon p^{3/2-\varepsilon}$，取任意固定 $0<\varepsilon<1/2$ 即可。
4. 对该子格的每个方向，R43 的无基点坏 $p$ 局部高度为常数；若有局部基点，则相应基点归一化的标准 QC 局部高度恒零。

这里的维数是 **$a=\dim A$，不是 $g=\dim J$**。所用分析输入都是已发表结果；本文从它们直接推出较弱的非消失计数，不使用平方水平的正比例非消失猜测，也不把仅在素数水平明确陈述的 $7/8$ 比例移到 $p^2$。本结果仍不控制辅助素数处的完整 QC 函数及其共同根。

## 1. 所用的商与额外的 Chow–Heegner 条件

令 $\mathcal B_p$ 是
$$S_2(\Gamma_0(p^2))^{+,\mathrm{new}}$$
的标准化 Hecke 特征新形式集合，包含每个 Galois 共轭形式一次；标准化指 $a_1(f)=1$，上标 $+$ 指 Fricke 特征值 $+1$。在权 $2$ 这恰对应函数方程符号 $-1$。

按 Dogra–Le Fourn (2021), Definition 4，取
$$A=\prod_{[f]:L'(f,1)\ne0}A_f,
\qquad B=\prod_{[f]:L'(f,1)=0}A_f.\tag{1.1}$$
乘积按 Galois 轨道取。非消失在共轭下保持；因此这些是定义于 $\mathbb Q$ 的商。Chen–Edixhoven–de Smit 的 Hecke 相容同源给出
$$J\sim_{\mathbb Q}J_0^+(p^2)^{\rm new}\sim_{\mathbb Q}A\times B.$$
特别地
$$a=\#\{f\in\mathcal B_p:L'(f,1)\ne0\}.\tag{1.2}$$
这不是 Galois 轨道的个数，而是所有嵌入所给的形式总数。

Dogra–Le Fourn 的 Proposition 3、Definition 4 和 §4.3 已证明
$$\operatorname{rk}A(\mathbb Q)=\dim A=\rho(A),\tag{1.3}$$
并证明：在其标准基点设置下，每个 $[L]\in\ker(d_{\pi_A})\subset\operatorname{NS}(A)$ 都满足
$$\theta_{X,\pi_A,\pi_B}([L])=0
\quad\text{于 }B(\mathbb Q)\otimes\mathbb Q.\tag{1.4}$$
这里 $d_{\pi_A}$ 是沿 $X\to J\to A$ 拉回后的次数，$\theta$ 是该对应的 Chow–Heegner 点在 $B$ 上的投影。因此只知道 (1.3) 并不足够；下文使用的是同时包含 (1.4) 的已发表定理。

令 $\mathbb T\subset\operatorname{End}_{\mathbb Q}(J)$ 为非分歧 Hecke 对应生成的整数代数，$\mathbb T_{\mathbb Q}=\mathbb T\otimes\mathbb Q$。重数一分解给
$$\mathbb T_{\mathbb Q}=\prod_{[f]}K_f,\qquad
\dim_{\mathbb Q}\mathbb T_{\mathbb Q}=g.$$
令 $e_A\in\mathbb T_{\mathbb Q}$ 在 (1.1) 的 $A$ 因子上取 $1$，在 $B$ 因子上取 $0$。它是有理、Rosati 对称的中心幂等元，且
$$\dim_{\mathbb Q}(e_A\mathbb T_{\mathbb Q})=a.\tag{1.5}$$
这些算子的 Rosati 对称性来自非分歧 Hecke 算子的自伴性；在这个交换代数内，加法、乘法和有理系数均保持该性质。

在主极化的识别下，$e_A\mathbb T_{\mathbb Q}$ 是来自 $\operatorname{NS}(A)_{\mathbb Q}$ 的对称方向。对它们，沿 $X$ 拉回的次数为零等价于
$$\operatorname{Tr}(F|H^0(X,\Omega^1))=0.\tag{1.6}$$
可以用 R33 的实际对应公式检查：若实际对称对应 $Z$ 的两投影次数为 $r$，则
$$\deg(\Delta^*Z)=2r-2\operatorname{Tr}(F|H^0(X,\Omega^1)).$$
于是 R14 所要求的次数零条件恰为 $\deg(\Delta^*Z)=2r$。该公式对整数虚对应同样成立。下文每次使用规范平移都限于 (1.6)，没有把单个 $T_2$ 本身当成 trace-zero 对应。

**基点范围。** (1.1)、(1.2)、(1.5)、后面的分析估计和无基点积分构造均不要求 $X(\mathbb Q)$ 有点。引用通常的 Dogra–Le Fourn 基点解释时，只在 $X(\mathbb Q)\ne\varnothing$ 的分支中选 $b\in X(\mathbb Q)$；若该集合为空，这个水平的有理点排除已经成立。没有假设存在有理 CM 基点。R43 的局部归一化只需要 $b\in X(\mathbb Q_p)$。

## 2. $T_2$ 在实际 Heegner 商上非标量

使用 Dogra–Le Fourn §5 的未除体积 Petersson 范数
$$\|f\|_{p^2}^2=
\int_{\Gamma_0(p^2)\backslash\mathfrak H}|f(x+iy)|^2\,dx\,dy.$$
定义
$$S_m(p)=\sum_{f\in\mathcal B_p}
\frac{\overline{a_m(f)}L'(f,1)}{\|f\|_{p^2}^2}.\tag{2.1}$$
Dogra–Le Fourn §5.3 在平方水平给出，对所有 $p\ge151$，
$$S_1(p)>0,\qquad 0<\frac{S_2(p)}{S_1(p)}<1.\tag{2.2}$$
其中 $S_1>0$ 的范围甚至为 $p\ge47$，见其 Proposition 5；这里只使用共同的范围 $p\ge151$。

**命题 1。** 对 $p\ge151$，$T_2|_A$ 不是标量算子。

**证明。** 假设它是标量 $c$。由于算子定义于 $\mathbb Q$，对 $H^0(A,\Omega^1)$ 取迹得到 $c\in\mathbb Q$。每个 $a_2(f)$ 为代数整数；而对所有 $L'(f,1)\ne0$ 的 $f$ 都有 $a_2(f)=c$，所以 $c\in\mathbb Z$。这也可以从该算子保持同调整数格看出。

式 (2.1) 中其余形式的项为零，且 $a_1=1$，故
$$S_2(p)=cS_1(p).$$
这与 (2.2) 矛盾。证毕。

令
$$t_A=\operatorname{Tr}(T_2|H^0(A,\Omega^1))\in\mathbb Z.$$
它是 Galois 稳定的代数整数之和，因而是整数。于是
$$\boxed{\quad
F_A=e_A(aT_2-t_A\operatorname{id})
\ne0
\quad(p\ge151).
\quad}\tag{2.3}$$
这是一个有理 Hecke 算子，消去 $B$，在 $J$ 上 trace 为零；乘适当正整数即为实际整数 Hecke 对应，并可进一步清除来自商的线丛与 Chow–Heegner 挠点所需的有限分母。

**这里不继承 R39 的四值界。** (2.3) 含有 $e_A$。将它写成实际对应通常需要更多 Hecke 算子，故它不是原来的 $gT_2-\operatorname{Tr}_J(T_2)\operatorname{id}$，不能自动沿用只支撑于三个自 $2$ 同源不变量的计算。下一节用维数和积分障碍映射寻找真正消去坏高度的方向。

## 3. 平方水平的一阶矩给出 $a\gg p^{3/2-\varepsilon}$

### 3.1 一阶矩的大小

Dogra–Le Fourn §5.2, equations (37)–(38)，在 $m=1$ 时给出
$$\begin{aligned}
\frac{S_1(p)}{4\pi}
={}&E_1(2\pi/p)
-\frac{E_1(2\pi/\sqrt p)}{p-1}
-\frac{\log p}{2(p-1)}e^{-2\pi/\sqrt p}\\
&+O\left(\frac1p+\frac{\log p}{p^{3/2}}\right),
\end{aligned}\tag{3.1}$$
其中 $E_1(y)=\int_y^\infty e^{-t}\,dt/t$。由
$$E_1(y)=-\gamma-\log y+O(y)\quad(y\to0^+)$$
立即得到
$$S_1(p)=4\pi\log p+O(1).\tag{3.2}$$
所有旧形式的扣除均已在 (3.1) 中，不把全空间的矩误当成新空间的矩。

### 3.2 个体导数的直接上界

**引理 2。** 对任意标准化 $f\in\mathcal B_p$，有绝对上界
$$|L'(f,1)|\ll p^{1/2}\log(2p).\tag{3.3}$$

**证明。** Dogra–Le Fourn Lemma 15 的精确公式为
$$L'(f,1)=2\sum_{m\ge1}\frac{a_m(f)}m E_1(2\pi m/p).$$
Deligne 的系数界及新形式在坏素数的标准局部关系给
$$|a_m(f)|\le\tau(m)\sqrt m.$$
这里 $p^2$ 水平、平凡 nebentypus 的新形式满足 $a_p=0$，所以被 $p$ 整除的项不会使此界失效。

对实数 $x\ge1$，记
$$A(x)=\sum_{m\le x}\frac{\tau(m)}{\sqrt m}.
$$
将 $m=uv$ 展开并使用 $\sum_{v\le y}v^{-1/2}\le2\sqrt y$，得到
$$A(x)\le 2\sqrt x\sum_{u\le x}\frac1u
\le2\sqrt x(1+\log x).\tag{3.4}$$
Abel 求和以及 $\frac{d}{dx}E_1(2\pi x/p)=-e^{-2\pi x/p}/x$ 给
$$\begin{aligned}
\sum_{m\ge1}\frac{\tau(m)}{\sqrt m}E_1(2\pi m/p)
&=\int_1^\infty A(x)\frac{e^{-2\pi x/p}}x\,dx\\
&\le2\int_1^\infty x^{-1/2}(1+\log x)e^{-2\pi x/p}\,dx\\
&\ll p^{1/2}\log(2p).
\end{aligned}$$
最后一步代换 $x=pu$；$u^{-1/2}e^{-2\pi u}$ 和其乘 $|\log u|$ 的积分均有限。这证明 (3.3)，不需另引导数凸性定理。证毕。

### 3.3 Petersson 范数的统一下界：平方水平与 CM 都包含

**引理 3。** 对任意 $\delta>0$，有仅依赖于 $\delta$ 的正常数 $c_\delta$，使所有标准化权 $2$、平方水平 $p^2$ 的新形式满足
$$\|f\|_{p^2}^2\ge c_\delta p^{2-\delta}.\tag{3.5}$$
该常数在本文中允许无效；没有排除 CM 形式。

**证明与归一化。** Hoffstein–Lockhart (1994), Theorem 0.2 及紧随其后的说明给出任意小幂的统一无效下界。其 p.164 最后的 Remark 明确将整个结论推广到全纯权 $k$，将参数 $\lambda N$ 换成 $kN$。固定权 $2$ 后，对每个 $\eta>0$，
$$L(1,\operatorname{Ad}f)\gg_\eta N^{-\eta}.$$

Hoffstein–Lockhart 在 p.161 定义的是**除以双曲体积**的范数；为不误搬其 Corollary 0.3 的首系数归一化，这里直接展开所需的未归一化积分。记
$$I_N=[\mathrm{SL}_2(\mathbb Z):\Gamma_0(N)],
\qquad R_f(s)=\sum_{m\ge1}\frac{|a_m(f)/\sqrt m|^2}{m^s}.$$
对无穷尖点宽度为 $1$ 的标准 Eisenstein 级数展开，再于 $s=1$ 取留数，给出
$$\|f\|_N^2=\frac{I_N}{48\pi}\operatorname*{Res}_{s=1}R_f(s).$$
Hoffstein–Lockhart (0.7)–(0.9) 的坏因子 $L_N(s)$ 定义为
$$\zeta(2s)R_f(s)=\zeta(s)L_N(s)L(s,\operatorname{Ad}f),$$
且其 p.163 证明 $L_N(1)\gg_\eta N^{-\eta}$，包含全部局部分歧类型。因此
$$\|f\|_N^2=
\frac{I_N}{8\pi^3}L_N(1)L(1,\operatorname{Ad}f)
\gg_\eta N^{1-2\eta},$$
这里使用 $I_N\ge N$。在 $N=p^2$ 时取 $\eta=\delta/4$，即得 (3.5)。这一步的体积因子不能省略。

范围方面，Hoffstein–Lockhart Theorem 0.2 在 p.164 明确给全部形式的统一无效版本；p.175 的证明第一段先处理 monomial（从二次域 $\mathrm{GL}_1$ 提升）情形，借二次 Dirichlet 与 Hecke $L$ 函数的分解和 Siegel 下界处理它，再处理非 monomial 情形。因此 CM 并未被略去。其 p.163 的坏局部因子估计覆盖全部分歧类型，故这里也没有平方自由水平假设。证毕。

作为归一化复核，令 $\lambda_f(m)=a_m(f)/\sqrt m$。在 $N=p^2$、$a_p=0$ 时，对 $\infty$ 尖点的标准 Eisenstein 级数展开可得
$$\|f\|_{p^2}^2=\frac{p^2}{8\pi^3}
L^{(p)}(1,\operatorname{Ad}f).\tag{3.6}$$
确实，展开积分的右侧为
$$\frac{\Gamma(s+1)}{(4\pi)^{s+1}}
\sum_{m\ge1}\frac{|\lambda_f(m)|^2}{m^s},$$
而该 Dirichlet 级数等于
$$\frac{\zeta^{(p)}(s)L^{(p)}(s,\operatorname{Ad}f)}
{\zeta^{(p)}(2s)}.$$
在 $s=1$ 取留数，并用 Eisenstein 级数留数等于双曲体积的倒数，得到 (3.6)。这再次显示 $p^2$ 而非 $1$ 才是未归一化 Petersson 范数的主尺度。引理 3 的证明不依赖额外猜测或局部 adjoint 因子的逐型选取。

### 3.4 去掉权重后的计数

**定理 4。** 对任意 $\varepsilon>0$，
$$a\gg_\varepsilon p^{3/2-\varepsilon}.\tag{3.7}$$

**证明。** 对固定 $\varepsilon>0$，在 (3.5) 中取 $\delta=\varepsilon$。引理 2、3 给每个形式
$$\frac{|L'(f,1)|}{\|f\|_{p^2}^2}
\ll_\varepsilon p^{-3/2+\varepsilon}\log(2p).$$
由 (1.2)，$S_1$ 中至多 $a$ 项非零。三角不等式与 (3.2) 于是给
$$\log p\ll S_1(p)
\le a\max_f\frac{|L'(f,1)|}{\|f\|_{p^2}^2}
\ll_\varepsilon a p^{-3/2+\varepsilon}\log(2p).$$
消掉对数因子即得 (3.7)。此证明不使用各项 $L'(f,1)$ 的正性，也不把一种嵌入上的非消失多算成独立轨道。这里的渐近下界指所有充分大的素数 $p$；不对亏格为零的小水平声称正的维数下界。证毕。

超奇异质量公式给
$$n=\frac{p-1}{12}
+\frac12\mathbf1_{j=1728\ \mathrm{ss}}
+\frac23\mathbf1_{j=0\ \mathrm{ss}}
\le\frac{p+13}{12}.\tag{3.8}$$
固定任意 $0<\varepsilon<1/2$，由 (3.7) 得 $a/n\to\infty$。因而存在一个绝对阈值 $p_0$，使 $p>p_0$ 时 $a>n$；这里没有给出 $p_0$ 的有效数值。

## 4. 把维数变成真正容许的积分子格

定义
$$V_A^0=\{F\in e_A\mathbb T_{\mathbb Q}:
\operatorname{Tr}(F|H^0(X,\Omega^1))=0\}.$$
由于 $\operatorname{Tr}(e_A)=a\ne0$，
$$\dim_{\mathbb Q}V_A^0=a-1.\tag{4.1}$$
令 $\Lambda_A=\mathbb T\cap V_A^0$。这是秩 $a-1$ 的自由整数格。证明完整秩只需取 $V_A^0$ 的一个有理基，逐个清除其在 $\mathbb T_{\mathbb Q}$ 中的分母；这些倍数属于 $\Lambda_A$ 且仍线性独立。反向秩界来自 (4.1)。所以不是先取得一个 $\mathbb Q_\ell$ 核，再假定它含有足够多的有理方向。

每个格元素均由实际整数 Hecke 虚对应表示：$\mathbb T$ 按这些对应的加法与复合生成，负系数表示对偶线丛或虚循环。必要时对有限基取共同整数倍，使所有方向在所选同源 $J\to A\times B$ 下确实来自 $\operatorname{NS}(A)$ 的实际有理线丛。主极化与商极化之间的有理同构只带来有限分母；阿贝尔簇的有理原点允许将 Picard 类刚性化为实际线丛。

在 $X(\mathbb Q)\ne\varnothing$ 时，取任一 $b\in X(\mathbb Q)$。由 (1.4)，每个基元素的 Chow–Heegner 点在 $B(\mathbb Q)$ 的像为挠。再取这些有限多个挠阶的公倍数，即可使整个子格的 $B$ 投影实际为零。加法性保证一个共同倍数已足够。取这些有限指数子格始终保留秩 $a-1$；下文仍记作 $\Lambda_A$。

这也消去了无基点 $D$ 族的平移在 $B$ 上的投影。为与维数 $a$ 区分，把 R14 的 Abel–Jacobi 拉回识别记为 $\alpha:J^\vee\to J$，于是 $F=\alpha f$、$q_b=\alpha^{-1}\kappa_b$。R14 的准确公式为
$$\alpha^{-1}\eta_D=dq_b+(f+f^\vee)e_b,
\qquad e_b=[db-D].$$
以 $\pi_B\circ\alpha$ 投影右侧：$F$ 及其 Rosati 对偶都消去 $B$，故最后两项投影为零，剩下 $d\pi_B\kappa_b$。$\kappa_b$ 与所用 Chow–Heegner 类只差所选对应的符号约定，其 $B$ 投影已被上述共同倍数消去。因此整个规范平移在 $B$ 方向为零；从基点条件转到实际 $D$ 族没有另加未知的常数 $B$ 坐标。

设 $D$ 为全部尖点之和，$d=(p-1)/2$，$u_D(x)=[dx-D]$。对每个 $F\in\Lambda_A$，用 R14 的实际规范平移记第二坐标为 $h_{D,F}u_D$。R30 证明
$$2h_{D,F}u_D:U\longrightarrow\mathcal J^{\vee,0},$$
所以有真正的积分线丛
$$\mathscr L_F=(u_D,2h_{D,F}u_D)^*\mathcal P^{\rm ext}
\quad\text{于 }U=\mathcal X^{\rm sm}.\tag{4.2}$$
其泛纤维由 R14、R18、R33 的范数构造实际平凡。

**引理 5（加法性）。** $F\mapsto[\mathscr L_F]$ 是整数格到 $\operatorname{Pic}(U)$ 的群同态。

**证明。** Poincaré 在第二坐标可加。R14 中 $\kappa$、$\eta_D$ 与 $f$ 均对对应 $F$ 可加：例如 $(u_D,(f_1+f_2)u_D)^*\mathcal P$ 是两个拉回线丛的张量积，Picard 类取和；规范除根公式保持此加法，故 $h_{D,F_1+F_2}=h_{D,F_1}+h_{D,F_2}$。R30 乘二与积分双扩张的群律相容。因此
$$\mathscr L_{F_1+F_2}\simeq\mathscr L_{F_1}\otimes\mathscr L_{F_2}.$$
负系数给逆线丛。常数线的基选择只改变平凡化，不改变上述 Picard 类。证毕。

在把几何分量展开的有限非分歧扩张上，由 R33 §6，
$$\ker\bigl(\operatorname{Pic}(U)\to\operatorname{Pic}(X_K)\bigr)
\simeq\mathbb Z^n/\mathbb Z(1,\ldots,1).\tag{4.3}$$
这里垂直除子给满射；若一个垂直除子为主，其函数在完整泛纤维上可逆，故为 $K^\times$ 中的常数，在所有约化分量上赋值相同。反过来常向量正是全纤维 $(p)$ 的倍数。式 (4.3) 的秩是 $n-1$。

由泛纤维平凡性与引理 5，得到实际障碍同态
$$\Phi_A:\Lambda_A\longrightarrow
\mathbb Z^n/\mathbb Z(1,\ldots,1),
\qquad F\longmapsto[\mathscr L_F].\tag{4.4}$$
这个构造允许一般 Hecke 对应的非零尖点范数缺陷，未使用 R33 的小次数条件，也未擅自令一般的 $\tau_i$ 为零。

**定理 6。** 子格
$$\mathcal K_A=\ker\Phi_A$$
满足
$$\boxed{\quad\operatorname{rank}\mathcal K_A\ge a-n.\quad}\tag{4.5}$$
其中每个对应均消去 $B$、满足 trace-zero 与 Dogra–Le Fourn 的 Chow–Heegner 条件，而且 $\mathscr L_F$ 在整个 $U$ 上有实际积分平凡化。

**证明。** 同态 (4.4) 的定义域秩为 $a-1$，目标秩为 $n-1$，所以核秩至少为 $(a-1)-(n-1)=a-n$。核中线丛类为零恰是全 $U$ 积分平凡化的存在性。若先在展开分量的非分歧扩张上计算，泛纤维有理截面的垂直系数全部相等，除以同一 $p$ 幂后即在原来的 $U$ 上给出单位截面，故没有遗留的下降障碍。

其余容许条件来自 $\Lambda_A$ 的构造与 (1.4)。若希望在最后一步才消去 $B$ 投影的挠点，对 $\mathcal K_A$ 的有限基取共同倍数也保留 (4.5)。证毕。

结合 (3.7)、(3.8)，固定 $0<\varepsilon<1/2$ 后，充分大 $p$ 时
$$\operatorname{rank}\mathcal K_A
\ge a-n\gg_\varepsilon p^{3/2-\varepsilon}>0.\tag{4.6}$$
这给出真正属于秩受控商的大量积分方向；没有把 R33 全 Jacobian 的 $g-n$ 直接当成商的结果。

## 5. 对坏 $p$ 局部高度的后果与仍缺的全局输入

对 $F\in\mathcal K_A$，R33 的实际泛纤维截面的除子为
$$\operatorname{div}(s_{D,F}^{\otimes2})=\sum_i k_i(F)U_i,$$
而 (4.4) 在核中等价于所有 $k_i(F)$ 相等。于是对任意辅助素数 $\ell\ne p$，R43 给
$$H_{D,F,p}(x)-H_{D,F,p}(y)
=-\tfrac12(k_i-k_j)\log_\ell p=0
\quad(x,y\in X(\mathbb Q_p)).\tag{5.1}$$
这个结论使用 $D$，无须全局或局部预选基点。若已有局部点 $b\in X(\mathbb Q_p)$，相应标准归一化给
$$\boxed{\qquad h^{\rm Nek}_{F,p,b}(x)=0
\quad\text{对所有 }x\in X(\mathbb Q_p).\qquad}\tag{5.2}$$
R43 已证明每个这样的局部点落在 $U$：共同奇点的局部重数 $\rho>1$ 排除了分歧度 $1$ 截面经过它。因此 (5.2) 覆盖所有局部点，不仅是预先选定分量的泛点。

本结果消掉的是一个确切的坏素数局部变化项，并同时满足 DLF 所需的商和 Chow–Heegner 条件。它没有给出 $\mathcal K_A$ 的统一小系数基，也没有控制 $e_A$、同源分母、共同挠倍数或 Mordell–Weil 对数格的积分指数。特别地，辅助素数 $\ell$ 处的完整局部高度仍包含迭代积分；全局高度的二次型和线性项仍需确定。不能把这些方向对应的某个 Hecke 二次微分单独视为完整 QC 函数的二阶系数。

即使所有坏 $p$ 分支现在合并为一个常数，有限 QC 集合中是否仍有非 CM 有理点，依然需要随层统一的共同根排除或其他全局输入。因此本文是 O5 的实质接口推进，尚未达到 Serre 一致性的完成标准。

## 6. 精确来源与本文的推导范围

- N. Dogra and S. Le Fourn, **Quadratic Chabauty for modular curves and modular forms of rank one**, *Mathematische Annalen* **380** (2021), 393–448, DOI [10.1007/s00208-020-02112-3](https://doi.org/10.1007/s00208-020-02112-3)；[期刊全文](https://link.springer.com/article/10.1007/s00208-020-02112-3)，[作者机构保存的期刊版](https://kclpure.kcl.ac.uk/ws/portalfiles/portal/147929133/QuadraticChabautyForModular_DOGRA_Accepted_26_Oct_2020_GOLD_VoR.pdf)。Definition 4、Proposition 3 和 §4.3 给准确的 $A,B$ 与 Chow–Heegner 条件；§5 开头定义未除体积范数；Lemma 15 给导数级数；equations (37)–(38) 给平方水平新空间一阶矩；§5.3 给 $p\ge151$ 的矩比范围。Remark 8 的 $7/8$ 注记明确限于至少已知素数水平，本文没有将其用作平方水平输入。
- J. Hoffstein and P. Lockhart, **Coefficients of Maass forms and the Siegel zero**, with an appendix by D. Goldfeld, J. Hoffstein and D. Lieman, *Annals of Mathematics* **140** (1994), 161–181, DOI [10.2307/2118543](https://doi.org/10.2307/2118543)；[期刊页面](https://annals.math.princeton.edu/1994/140-1/p04)，[作者站点正文](https://www.math.columbia.edu/~goldfeld/CoeffMaassForms.pdf)。p.161 为体积归一化定义；p.163, (0.9) 及坏局部因子范围；p.164, Theorem 0.2、Corollary 0.3 与最后的全纯权推广 Remark；p.175, Theorem 0.2 证明首段处理 monomial 情形。所链接正文至 p.176，附录不用于本文。
- P. Deligne, **La conjecture de Weil. I**, *Publications Mathématiques de l'IHÉS* **43** (1974), 273–307，Théorème 8.2, p.302；[原刊存档](https://www.numdam.org/articles/10.1007/BF02684373/)。这里只使用其权 $2$ 推论与新形式局部关系所得 $|a_m(f)|\le\tau(m)\sqrt m$。
- A. O. L. Atkin and J. Lehner, **Hecke operators on $\Gamma_0(m)$**, *Mathematische Annalen* **185** (1970), 134–160，Theorem 3, p.147，DOI [10.1007/BF01359701](https://doi.org/10.1007/BF01359701)：平方水平平凡特征新形式的 $a_p=0$ 及坏素数递推。
- B. de Smit and B. Edixhoven, **Sur un résultat d'Imin Chen**, *Mathematical Research Letters* **7** (2000), 147–153，Theorems 1–2；[作者全文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。非分裂正规化子 Jacobian 与平方水平新部分的 Hecke 相容同源。
- 仓库 R14、R18、R30、R33、R43 分别给出规范平移、实际范数、乘二积分延拓、全 $U$ 障碍映射、Néron 局部高度比较。本文的 $T_2|_A$ 非标量推论、从一阶矩到 (3.7) 的计数，以及将 (4.4) 限制到真正容许格后的 (4.5)，均已在上文完整证明；不对这些由已知结果组合得到的结论作未经核实的优先权声称。
- 同会话笔记 `notes/2026-11-12-square-level-norm-derivative-cont.md` 给出了平方水平范数与导数估计的独立展开，也处理了本文无需使用的负 Fricke 符号。
