# R40：可变四次 CM 参考的三次类域与判别式增长

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明的全局必要条件；中间进展。** 将 R37 的三次分裂域机制推广到 R24 的全部可变四次参考曲线。这里允许参考参数 $d$ 变化，允许 $3$ 或 $p$ 整除 $d$，也允许整 $j$ 即 $B=1$。局部分歧、类群商及小素数论证均重新核实；没有从固定参考情形直接类推。结果仍是随参数变化的类群限制和增长下界，不是绝对一致性证明。

## 1. 假设、二次预解式域与结论

采用 R24 的实际异常子族：
$$
p>37,\qquad p\equiv7\pmod{12},\qquad
E_0[p]\simeq A_d[p],\qquad A_d:y^2=x^3-dx,
\tag{40.1}
$$
其中 $E_0/\mathbb Q$ 非 CM，$d$ 是非零、有符号平方自由整数，Cartan 商域为 $\mathbb Q(i)$。记
$$
j(E_0)=\frac{A^3}{B^p},\qquad (A,B)=1,\quad B>0,
$$
$$
A^3-1728B^p=\epsilon2^\alpha dZ^2,\qquad
M=\epsilon2^\alpha B,\qquad
e_A=v_2(A)\in\{1,2,3\}.
\tag{40.2}
$$
R24、R31 给出
$$
(B,6dp)=1,\qquad
\alpha=1\Longleftrightarrow e_A=1,
\tag{40.3}
$$
且 $\alpha=1$ 时 $d$ 奇。

定义
$$
D=\operatorname{sf}(dM),\qquad
F=\mathbb Q(\sqrt D),\qquad
H=\mathbb Q(E_0[2]).
\tag{40.4}
$$
此处 $d$ 始终指 CM 参考参数；$D$ 是带符号平方自由数；$D_F$ 指 $F$ 的基本判别式。这三者不可混同。

**定理 R40。**

1. $D\ne1$，且
   $$
   \operatorname{Gal}(H/\mathbb Q)\simeq S_3,\qquad
   H^{A_3}=F,\qquad
   \operatorname{Gal}(H/F)\simeq C_3.
   \tag{40.5}
   $$
   每个奇素数 $q\mid dB$ 上方的素理想都在 $H/F$ 中完全分裂，包括 $q=p$（若 $p\mid d$）。

2. 若 $e_A=1$ 或 $2$，则 $H/F$ 处处不分歧，$2$ 上方的素理想也全部完全分裂。因此
   $$
   G_0=
   \operatorname{Cl}(F)/
   \langle[\mathfrak q]:\mathfrak q\mid2dB\rangle
   $$
   满足
   $$
   \boxed{G_0/3G_0\ne0.}
   \tag{40.6}
   $$
   尤其 $3\mid h(F)$。另外，
   $$
   \boxed{
   |D_F|\ge
   \begin{cases}
   p^4/64,&F\text{ 实二次},\\
   \pi^2p^4/1024,&F\text{ 虚二次}.
   \end{cases}}
   \tag{40.7}
   $$

3. 若 $e_A=3$，则 $D=D_F\equiv5\pmod8$。唯一的二进素理想 $(2)$ 在 $H/F$ 中温和全分歧，全球导子恰为 $(2)$。令
   $$
   C=\operatorname{Cl}_{(2)}(F),\qquad
   G=C/\langle[\mathfrak q]:\mathfrak q\mid dB,\ \mathfrak q\nmid2\rangle,
   \tag{40.8}
   $$
   射线模数不含无限位，且令 $\overline I$ 为
   $$
   (\mathcal O_F/(2))^\times\simeq\mathbb F_4^\times
   \longrightarrow C\longrightarrow G
   $$
   的像。则
   $$
   \boxed{\overline I\not\subseteq3G.}
   \tag{40.9}
   $$
   特别地，所有全局单位必须模 $2$ 为 $1$，且
   $$
   r_3(C)=r_3(\operatorname{Cl}(F))+1.
   \tag{40.10}
   $$
   还存在素数 $\ell$ 满足
   $$
   \boxed{
   \ell\mid\frac{|D_F-1|}{4},\quad
   \ell\nmid2dBp,\quad
   \ell\text{ 在 }F\text{ 中分裂},\quad
   \ell\ge p^2/16,
   }
   \tag{40.11}
   $$
   从而
   $$\boxed{|D_F-1|\ge p^2/4.}\tag{40.12}$$

普通类群条件 (40.6) 与射线条件 (40.9) 是相应抽象三次类域存在的充要条件；对实际 $E_0$ 只使用必要方向。本文没有断言每个满足这些类群条件的参数都来自异常椭圆曲线。

## 2. 二次预解式平方类与不可约性

R31 的全局平方类恒等式为
$$
\frac{\Delta_{E_0}^{\min}}{64d^3}\in M\mathbb Q^{\times2}.
$$
所以
$$\Delta_{E_0}^{\min}\in dM\mathbb Q^{\times2}.\tag{40.13}$$
将 $E_0$ 化为短 Weierstrass 方程，其 $2$ 除法三次式的判别式为椭圆判别式的 $1/16$ 倍；换模型只再改变一个平方。故 (40.13) 正是其三次分裂域的符号特征，二次预解式为 (40.4)。

R8 引用的 Lemos 定理排除 $E_0$ 的有理循环 $2$ 同源：若存在，则非 CM 曲线在每个 $p>37$ 的模 $p$ 像满射，与 (40.1) 矛盾。因此 $E_0[2]$ 没有非零有理点，$2$ 除法三次式不可约，其全局群是 $S_3$ 或 $C_3$。

先在后续局部论证中允许这两种可能。第 3、4 节证明：若 $e_A=1,2$，所有可能分歧处的分解群至多阶 $2$。若全局群为 $C_3$，这些群只能平凡，其余素数不分歧，故 $H/\mathbb Q$ 处处有限不分歧。次数为 $3$ 的 Galois 扩张也不能在实位分歧，因实位分歧次数只能为 $2$。这与 $\mathbb Q$ 的类数为 $1$ 矛盾。

当 $e_A=3$ 时，第 4.3 节直接证明二次判别式平方类在 $\mathbb Q_2$ 上非平凡，故也不是 $C_3$ 情形。至此 $D\ne1$、全局群为 $S_3$，并得到 (40.5)。

## 3. 全部奇素数，包括 q=3 和 q=p

R24 的约化分类是：每个奇 $q\mid d$ 处，$E_0$ 温和潜在好约化，惯性阶为 $4$；每个 $q\mid B$ 处为乘法约化；其余奇素数处好约化。$d$ 与 $B$ 互素。以下逐类比较的是 $2$ 挠点分裂域，不把剩余特征 $p$ 的模块分类当作 $2$ 挠点结论直接引用。

### 3.1 奇 q 整除 d：有限四阶惯性模 2 仍非平凡

在 $T_2(E_0)$ 上，惯性像是忠实的有限循环群 $C_4$；这是潜在好约化的有限惯性表示，$2\ne q$。设其生成元为
$$u\in\mathrm{GL}_2(\mathbb Z_2),\qquad u^4=I,\quad u^2\ne I.$$
惯性的行列式等于 $2$ 进圆分特征，而该特征在奇 $q$ 处不分歧。因此 $\det u=1$。在特征零代数闭包上，有限阶矩阵可对角化；阶为 $4$ 且行列式为 $1$ 强迫其特征值为 $i,-i$。所以
$$u^2=-I.$$

若 $u\equiv I\pmod2$，写 $u=I+2V$，则
$$u^2=I+4(V+V^2)\equiv I\pmod4,$$
与 $u^2=-I$ 矛盾。因此模 $2$ 的惯性像不是平凡群。它的阶整除 $4$，而 $\mathrm{GL}_2(\mathbb F_2)$ 只有阶 $1,2,3$ 的元素，故该像恰为一个 $C_2$。

局部分解群正规化惯性群，所以它的模 $2$ 像包含在
$$N_{S_3}(C_2)=C_2$$
中。于是整个分解群也恰为这个 $C_2$。它与 $A_3$ 交于单位元，故每个 $\mathfrak q\mid q$ 在 $H/F$ 中完全分裂。

这个证明对 $q=3$ 同样成立，因为惯性次数 $4$ 与 $3$ 互素。对 $q=p$ 也成立：此处使用的是 $T_2$，而 R24 的 (24.7) 及引理 24.1 已证明当 $p\mid d$ 时 $E_0$ 为 III 型、具有温和四阶惯性。没有在特征 $p$ 处套用不适用的模 $p$ 不分歧判据。

### 3.2 q 整除 B：Tate 模 2 的整个局部像

在乘法约化的奇素数 $q$ 处，Tate 曲线的模 $2$ 表示在合适基中为上三角，两个对角元均为 $1$，因为 $\mu_2$ 和 $\mathbb Z/2$ 的模 $2$ 特征均平凡。若为非分裂乘法约化，还需乘以一个二次扭曲特征；但 $\pm1$ 模 $2$ 相同，所以不改变模 $2$ 像。

因此整个局部像包含在
$$
\left\{
\begin{pmatrix}1&a\\0&1\end{pmatrix}:a\in\mathbb F_2
\right\}\simeq C_2.
$$
同样与 $A_3$ 相交平凡，故每个 $q\mid B$ 上方的素理想在 $H/F$ 中完全分裂。这里不要求 $v_q(B)$ 为奇数，也不要求模 $2$ 惯性非平凡。

### 3.3 其他奇素数

其余奇素数为好约化处，$T_2(E_0)$ 及其模 $2$ 商在惯性上平凡，故 $H/\mathbb Q$ 不分歧。这一结论适用于所有这些素数；若是 $q=p$，也仍因为使用 $T_2$、且 $2\ne p$ 而有效。

至此，$H/F$ 的唯一可能有限分歧处只剩 $2$，并已证明 (40.5) 后半项中的全部奇坏素数完全分裂。

## 4. 二进模型逐行检查

### 4.1 共同二次扭曲不会改变 H

R36 将 $E_0,A_d$ 同时二次扭曲，使二进导子指数归一化为 $5$ 或 $8$。椭圆曲线的二次扭曲在挠点表示上乘以值为 $\pm1$ 的特征；模 $2$ 后该特征平凡。因此这种共同扭曲不改变 $E_0[2]$、$H$、$F$ 或判别式平方类。

可据此使用 R36 已证明的六种归一化二进类型。设归一化曲线的极小不变量为 $c_4,c_6,\Delta$。在 $\mathbb Q_2$ 上写短方程
$$
y^2=x^3+a_4x+a_6,\qquad
a_4=-c_4/48,\quad a_6=-c_6/864.
\tag{40.14}
$$
所有下表行都使 $a_4,a_6$ 在 $\mathbb Z_2$ 中；不要求这个短方程本身是原先所选的整极小模型。它与曲线在 $\mathbb Q_2$ 上同构，因而有同一个 $2$ 挠点分裂域。

R36 的已证明赋值表，转为短系数后是：

| 类型 | $e_A$ | $v_2(a_4)$ | $v_2(a_6)$ |
|---|---:|---:|---:|
| $D_a$ | $2$ | $0$ | $\ge3$ |
| $D_b$ | $2$ | $2$ | $\ge6$ |
| $D_d$ | $1$ | $0$ | $1$ |
| $D_e$ | $2$ | $1$ | $\ge4$ |
| $D_f$ | $2$ | $3$ | $\ge7$ |
| $D_c$ | $3$ | $3$ | $4$ |

这里用 $v_2(48)=4$、$v_2(864)=5$。$D_a,D_b$ 的加强下界分别来自 R36 的 $v_2(c_6)\ge8,11$；$D_e,D_f$ 对应偶参考参数 $d$。

### 4.2 前五行都有一个 Q2 根

令
$$f(x)=x^3+a_4x+a_6.$$

- 在 $D_a,D_d$ 中，$f(0)$ 为偶数、$f'(0)=a_4$ 为单位，故 Hensel 引理给 $\mathbb Q_2$ 根。
- 在 $D_b$ 中，令 $x=2z$ 并除以 $8$，得到
  $$
  z^3+(a_4/4)z+a_6/8.
  $$
  一次项系数为单位，常数项被 $2$ 整除，故仍有简单的模 $2$ 根 $z=0$，并可提升。
- 在 $D_e$ 中，取 $x_0=-a_6/a_4$。其赋值至少为 $3$，所以
  $$
  v_2(f(x_0))=v_2(x_0^3)\ge9,\qquad
  v_2(f'(x_0))=v_2(3x_0^2+a_4)=1.
  $$
  由 $9>2\cdot1$，Hensel 的强形式给根。
- 在 $D_f$ 中，同样取 $x_0=-a_6/a_4$，此时 $v_2(x_0)\ge4$，所以
  $$
  v_2(f(x_0))\ge12,\qquad v_2(f'(x_0))=3,
  $$
  而 $12>2\cdot3$，仍给根。

若某行的 $a_6=0$，根 $0$ 已直接存在；实际非 CM 情形无须这个例外。每个根使局部分裂域至多为二次扩张。故当 $e_A=1,2$ 时，$H/\mathbb Q$ 的二进分解群至多为 $C_2$，其与 $A_3$ 的交平凡。这证明 $2$ 上方素理想在 $H/F$ 中完全分裂。

### 4.3 Dc 行是唯一的温和三次分歧

在 $D_c$ 中，仍置 $x=2z$、除以 $8$。得到
$$z^3+2uz+2v,\qquad u,v\in\mathbb Z_2^\times.$$
这是 $2$-Eisenstein 多项式，所以定义一个完全分歧的三次局部扩张。其多项式判别式是
$$
-4(2u)^3-27(2v)^2
=4(-8u^3-27v^2).
$$
括号内的单位模 $8$ 为 $5$。故符号特征的平方自由代表满足
$$D\equiv5\pmod8.$$
二次预解式域 $F_2/\mathbb Q_2$ 是非分歧二次扩张，而局部分裂域的群为 $S_3$，分歧次数为 $3$、剩余次数为 $2$。于是 $H/F$ 在唯一的 $(2)$ 处温和全分歧，次数恰为 $3$。

因此 $D$ 本身就是奇基本判别式 $D_F$。非平凡温和阿贝尔扩张的局部导子指数为 $1$，而第 3 节已排除其他有限分歧，故全球导子恰为 $(2)$。

## 5. 类群、射线惯性及无穷位

$H/F$ 为循环三次扩张时，无穷位不能发生分歧，因为实位分歧需要阶 $2$ 的局部群。因此所有以下类群均可使用不含无限位的普通版本；不需要用窄类群补上未检查的实位。

### 5.1 普通类群商

当 $e_A=1,2$，由第 3、4 节，Artin 互反给
$$\operatorname{Cl}(F)\twoheadrightarrow\operatorname{Gal}(H/F)\simeq C_3,$$
并杀掉所有位于 $2dB$ 上方的素理想类，故经过 $G_0$。这证明 (40.6)。

反过来，$G_0/3G_0$ 的任意非零线性泛函通过类域论产生一个具有相应分裂条件的处处不分歧循环三次扩张。二次共轭在 $\operatorname{Cl}(F)$ 上取逆，因为 $\mathfrak a\overline{\mathfrak a}=(N\mathfrak a)$；故这个三次层在 $\mathbb Q$ 上正常，且群为取逆半直积 $S_3$。这个反方向只分类抽象数域，不构造 $E_0$。

### 5.2 射线商与真实惯性

当 $e_A=3$，有限模数 $(2)$ 的射线类群给满射
$$C\twoheadrightarrow C_3.$$
因真实分歧，其限制到
$$I=\operatorname{im}(\mathbb F_4^\times\to C)$$
必须非零；又它杀掉全部奇 $q\mid dB$ 上方的素理想类，所以经过 $G$。映射 $G\to C_3$ 都经过 $G/3G$，因此在 $\overline I$ 上非零正等价于 (40.9)。

反过来，若 (40.9) 成立，选取一个在 $\overline I$ 上非零的线性泛函，类域论给导子恰为 $(2)$、且指定素理想完全分裂的三次层。二次共轭也在 $C$ 上取逆：对与 $(2)$ 互素的理想，
$$
\mathfrak a\overline{\mathfrak a}=(N\mathfrak a),
$$
而奇整数 $N\mathfrak a\equiv1\pmod{2\mathcal O_F}$。因此该层同样在 $\mathbb Q$ 上给 $S_3$ 扩张。

### 5.3 单位及 3 秩的必要条件

射线正合列为
$$
\mathcal O_F^\times\longrightarrow\mathbb F_4^\times
\longrightarrow C\longrightarrow\operatorname{Cl}(F)\longrightarrow0.
\tag{40.15}
$$
只要有一个单位模 $2$ 不等于 $1$，它就生成阶 $3$ 的 $\mathbb F_4^\times$，导致 $I=0$，矛盾。因此必须
$$\varepsilon\equiv1\pmod2\quad
\text{对所有 }\varepsilon\in\mathcal O_F^\times.$$

此时 $I\simeq C_3$，且
$$0\longrightarrow I\longrightarrow C\longrightarrow\operatorname{Cl}(F)\longrightarrow0.$$
真实三次惯性要求 $I\not\subseteq3C$；对该列取模 $3$，核的维数恰为 $1$，即 (40.10)。若 $I\subseteq3C$，则所有 $C_3$ 商都杀掉惯性；例如 $C=C_9$、$I=3C$ 就会发生这一现象。因此射线类数被 $3$ 整除仍不够。

在实二次域中，所有单位模 $2$ 为 $1$，等价于基本单位的迹为偶数：模 $2$ 的共轭为平方映射，$\mathbb F_4^\times$ 中只有 $1$ 的迹为零。因此，任何 $D_F=n^2\pm4$ 的正平方自由判别式（$n$ 奇、第二式 $n\ge3$）都被单位 $(n+\sqrt{D_F})/2$ 的奇迹排除。

这里与固定参考的 R37 有一个需明确保留的区别：变量参数允许 $3\mid d$，所以不能先验排除 $F=\mathbb Q(\sqrt{-3})$。若它出现于射线分支，其六次单位的模 $2$ 像为阶 $3$，恰由 (40.15) 排除。对其余虚二次域 $D_F\equiv5\pmod8$，单位只有 $\pm1$，单位筛自动满足，但 (40.9) 仍须成立。

## 6. 小好素数与残余特征处的独立检查

### 6.1 奇好素数不等于 p

设奇素数 $\ell\nmid dB$ 且 $\ell\ne p$。R24 保证两曲线 $E_0,A_d$ 在 $\ell$ 好约化，(40.1) 给
$$a_\ell(E_0)\equiv a_\ell(A_d)\pmod p.$$
若 $\ell<p^2/16$，则
$$|a_\ell(E_0)-a_\ell(A_d)|\le4\sqrt\ell<p,$$
故二者作为整数相等。

这里不需要 $A_d$ 有全有理 $2$ 挠点：它始终有非零有理点 $(0,0)$，在奇好素数处仍给非零 $2$ 挠点，所以其约化群的阶为偶数，$a_\ell(A_d)$ 为偶数。因此 $a_\ell(E_0)$ 也为偶数。

$\mathrm{GL}_2(\mathbb F_2)\simeq S_3$ 中，阶 $3$ 元素的迹为 $1$，其他元素的迹为 $0$。所以 $\ell$ 的 Frobenius 阶至多为 $2$。若阶为 $1$，它在 $H/F$ 已平凡；若阶为 $2$，$\ell$ 在 $F/\mathbb Q$ 中惰性，相对 Frobenius 是其平方，也平凡。故每个 $\mathfrak l\mid\ell$ 在 $H/F$ 中完全分裂。

### 6.2 l=p

不能在上一节把 $\ell=p$ 当作一般迹同余素数。

若 $p\mid d$，第 3.1 节的 $T_2$ 有限四阶惯性论证已经给出完全分裂。

若 $p\nmid d$，R24 引理 24.1 给 $E_0,A_d$ 均在 $p$ 好约化。因 $p\equiv3\pmod4$，$A_d$ 为好超奇异，其模 $p$ 惯性表示不可约。$E_0[p]\simeq A_d[p]$ 排除 $E_0$ 普通，所以 $E_0$ 也好超奇异；$p>3$ 时其整数迹为
$$a_p(E_0)=0.$$
于是模 $2$ Frobenius 迹为零，仍得到每个 $\mathfrak p\mid p$ 在 $H/F$ 中完全分裂。这与 R24 §7 的独立残余特征系数检查一致。

因此，无论 $p$ 是否整除 $d$，都已处理，不存在遗漏的“类群生成素数恰为 $p$”例外。素数 $2$ 则由第 4 节独立处理。

## 7. 普通分支的 Minkowski 下界与参数含义

假定 $e_A=1$ 或 $2$。综合第 3、4、6 节，所有有理素数 $\ell<p^2/16$ 上方的素理想都在 $H/F$ 中完全分裂；全部位于 $2dBp$ 之上的素理想也完全分裂。

Minkowski 定理给普通类群一个整理想代表集，代表范数至多
$$
B_F=
\begin{cases}
\tfrac12\sqrt{D_F},&F\text{ 实},\\
\tfrac2\pi\sqrt{|D_F|},&F\text{ 虚}.
\end{cases}
$$
分解这些代表，说明 $\operatorname{Cl}(F)$ 由范数至多 $B_F$ 的素理想生成。若 $B_F<p^2/16$，这些生成素理想下方的有理素数也小于 $p^2/16$，其 Artin 符号全部为零，与 $\operatorname{Cl}(F)\twoheadrightarrow C_3$ 矛盾。因此 $B_F\ge p^2/16$，得到 (40.7)。

这个论证只用于普通类群分支；射线分支的二进惯性不能由同一代表界忽略。

### 7.1 直接约束参考参数与分母平方自由部分的乘积

令 $b_0=\operatorname{sf}(B)>0$。由 $(B,d)=1$、$B$ 奇，以及 (40.3)，可精确写成
$$D=\epsilon2^\alpha d\,b_0.$$
特别地：

- $e_A=1$ 时，$d$ 奇、$\alpha=1$，所以 $D_F=8\epsilon d b_0$；
- $e_A=2$ 时，$\alpha=0$，所以 $D_F$ 是 $\epsilon d b_0$ 或 $4\epsilon d b_0$；
- $e_A=3$ 时，$D_F=D=\epsilon d b_0\equiv5\pmod8$。

在普通分支，记 $\gamma=1/64$ 当 $F$ 实、$\gamma=\pi^2/1024$ 当 $F$ 虚。则
$$
|d|\,\operatorname{sf}(B)\ge
\begin{cases}
\gamma p^4/8,&e_A=1,\\
\gamma p^4/4,&e_A=2.
\end{cases}
\tag{40.16}
$$
同样的下界当然适用于 $|d|\operatorname{rad}(B)$ 和 $|d|B$。尤其 $B=1$ 时，这给出 $|d|$ 的统一四次方增长下界，而非只适用于有分母的曲线。

该结论没有限制 $d$ 或 $B$ 从上方增长，所以不是绝对 $p$ 界。

## 8. 射线分支的明确见证

假定 $e_A=3$，于是 $D_F\equiv5\pmod8$。置
$$
\omega=(1+\sqrt{D_F})/2\in\mathcal O_F,\qquad
N(\omega)=(1-D_F)/4.
$$
其范数为非零奇整数，模 $2$ 的 $\omega$ 生成 $\mathbb F_4^\times$。实际三次 Artin 特征 $\chi:C\to C_3$ 在惯性上非零，故
$$\chi((\omega))\ne0.$$

因此 $(\omega)$ 的素理想分解中至少有一个 $\mathfrak l$ 满足 $\chi(\mathfrak l)\ne0$。其下方素数 $\ell$ 整除 $|D_F-1|/4$，不等于 $2$，不整除 $dB$，也不等于 $p$，因为这些位置已分别由第 3、6 节证明完全分裂。

该 $\ell$ 必在 $F$ 中分裂。如果惰性，唯一素理想为 $(\ell)$，而奇整数 $\ell\equiv1\pmod2$，其射线类平凡；如果分歧，则 $\ell\mid D_F$，与 $\ell\mid D_F-1$ 矛盾。最后，第 6.1 节迫使 $\ell\ge p^2/16$。这证明 (40.11)、(40.12)。

若该见证还满足 $\ell\equiv3\pmod4$，则好约化的 $A_d$ 有 $a_\ell(A_d)=0$。Hasse 界只需 $2\sqrt\ell<p$ 就排除非平凡三次 Frobenius，因此这类见证满足更强的 $\ell\ge p^2/4$。

由 $D_F=\epsilon d\,\operatorname{sf}(B)$，还得到粗略但直接的参数下界
$$|d|\,\operatorname{sf}(B)\ge p^2/4-1.$$
它来自指定的射线惯性类，不是从普通类群的 Minkowski 界移植而来。

## 9. 额外高次同余假设下的放大

本节**另加**假设：对某个已给定的整数 $s\ge1$，
$$E_0[p^s]\simeq A_d[p^s]$$
作为实际 $G_{\mathbb Q}$-模。$s>1$ 的同构不是 R24 现有假设的推论，不能把 $s$ 任意提高。

所有局部分支与类群结构只需模 $p$，所以保持成立。对奇好素数 $\ell\ne p$，新增假设给
$$a_\ell(E_0)\equiv a_\ell(A_d)\pmod{p^s}.$$
于是第 6.1 节的阈值提升为
$$\ell<p^{2s}/16.$$
$\ell=p$ 仍由第 6.2 节独立处理。

完全重复第 7、8 节中已经写出的有限群与范数论证，即得：

- 普通分支：
  $$
  |D_F|\ge
  \begin{cases}
  p^{4s}/64,&F\text{ 实},\\
  \pi^2p^{4s}/1024,&F\text{ 虚};
  \end{cases}
  $$
- 射线分支：存在 (40.11) 同样的素数见证，并有
  $$
  \ell\ge p^{2s}/16,\qquad |D_F-1|\ge p^{2s}/4.
  $$
  若见证 $\ell\equiv3\pmod4$，还满足 $\ell\ge p^{2s}/4$。

这些是带明确额外假设的推论，可与 R35 的高次 Tate 同余条件配合。它们没有为只有模 $p$ 同构的原问题提供自动提升。

## 10. 真实缺口与来源

普通分支现在要求一个指定坏素数全部分裂的非平凡 $3$ 类群商；射线分支要求局部三次惯性在杀掉指定素理想后仍能被一个 $C_3$ 商检测到。进一步的统一排除，必须证明这些实际参数的商群或对应曲线点不存在，或者获得与下界冲突的上界。本文没有这样的上界，也没有把类群非零本身视作矛盾。

使用的已证明仓库输入：

- [R24](R24-quartic-parameter-and-discriminant-rigidity.md)：实际四次同余、所有奇素数约化类型，包含 $3,p$，以及参数互素性。
- [R31](R31-discriminant-character-and-two-prime-obstruction.md)：判别式比的全局平方类及 $\alpha$ 的精确二进取值。
- [R36](R36-variable-quartic-dyadic-inertia.md)：共同二次扭曲的归一化、六种二进不变量及所需加强赋值。本文已经逐行重做 $2$ 除法多项式的根与分歧检验。
- [R8](R8-rational-isogeny-isolation.md)：Lemos 统一性输入所给的有理循环同源排除。
- [R37](R37-cubic-descent-and-class-group-obstruction.md)：固定参考情形的背景；变量参数的奇加性素数、$2$ 处模型与 $p$ 的两种情形已在本文另外证明。

外部经典输入：

- P. Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Trans. Amer. Math. Soc. **371** (2019), Theorem 1.1，[作者版本](https://arxiv.org/abs/1702.01985)，DOI [10.1090/tran/7198](https://doi.org/10.1090/tran/7198)。
- N. Freitas、A. Kraus, *On the symplectic type of isomorphisms of the p-torsion of elliptic curves*, Memoirs AMS **277** (2022), no. 1361，[出版页](https://doi.org/10.1090/memo/1361)，[作者 v5](https://arxiv.org/pdf/1607.01218v5)。R36 已核查其 Theorems 9、17、18 及相关赋值表；本文使用的是 R36 给出的精确表。
- J. S. Milne, *Class Field Theory*, v4.03 (2020)，[作者原文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)，Chapter V Theorem 1.7、§3、Example 3.9，以及 Chapter I §1.9：射线正合列、互反与存在定理、普通 Hilbert 类域及温和导子。
- J. S. Milne, *Algebraic Number Theory*, v3.08 (2020)，[作者原文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)，Theorem 4.3、4.9：Minkowski 类群代表界与 $\mathbb Q$ 无非平凡处处不分歧扩张。

没有使用未证的类数分布猜想、GRH、$abc$ 或高次同余提升猜想。
