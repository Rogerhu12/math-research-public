# R100：四次差字符的二次商、实际二除法域与二处四阶惯性的排除

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文对所有 $p>37$、$p\equiv11\pmod{12}$ 的指定实际分支，精确识别 R21 的四次差字符之二次商，并用已发表的二进惯性分类排除 $e_2=4$。结论不限于 R98 的三个层数；整 $j$ 仍是不可省略的前提。

## 1. 设置和结论

设 $E/\mathbb Q$ 的实际模 $p$ 像为完整非分裂正规化子 $N$，Cartan 为 $C$，商域为
$$
K=\mathbb Q(\sqrt{-3}),\qquad p>37,\quad p\equiv11\pmod{12}.
$$
并假设
$$
\rho_{E,p}(I_p)=C^3,\qquad c(\eta)\in\{6,9\},\qquad j(E)\in\mathbb Z.
                                                               \tag{100.1}
$$
$\eta$ 是 R66 的实际原始三次环类角色，$c(\eta)$ 是其准确导子。

取 CM 参考曲线
$$A:y^2=x^3+1.$$
在 $K$ 上选择与 R21 的 $p$ 处十二次幂取向相容的 CM 剩余特征，记为 $\lambda_A$；原曲线的 Cartan 特征记为 $\lambda_E$。令
$$
\beta=\lambda_E/\lambda_A,\qquad \gamma=\beta^3,\qquad
\delta=\beta^6=\gamma^2.                                 \tag{100.2}
$$
R21 与 $h_K=1$ 给 $\beta^{12}=1$。$\gamma$ 的阶至多四，$\delta$ 的阶至多二。对 $d\in\mathbb Q^\times$，记 $\chi_d$ 为 $\mathbb Q(\sqrt d)$ 的二次特征，平凡平方类时按平凡字符解释。$\Delta$ 为任一有理 Weierstrass 模型的判别式，其平方类与模型和二次扭曲无关。

**定理 100.1。** 有精确的全局特征等式
$$
\boxed{\beta^6=\chi_\Delta|_{G_K}.}                       \tag{100.3}
$$
因此四次差字符的二次商就是实际 $E[2]$ 判别式特征在 $K$ 上的限制。

设 $e_2$ 为曲线在二处的有限惯性阶，则
$$
\boxed{
\begin{array}{c|c|c}
c(\eta)&e_2&[\Delta]\text{ 在 }\mathbb Q_2^\times/\mathbb Q_2^{\times2}\\ \hline
6&3\text{ 或 }6&1\text{ 或 }-3\\
9&1\text{ 或 }2&-3.
\end{array}}                                             \tag{100.4}
$$
特别，两支都不存在 $e_2=4$。

若 $c=9$ 且 $j\ne0$，还有
$$
\boxed{v_2(j)\ge12.}                                     \tag{100.5}
$$
按 R96 写 $j=3^bp^rX^3$，$b,r\in\{1,2\}$，便有
$$\boxed{16\mid X.}                                      \tag{100.6}$$

证明中特别处理二处的未分歧二次因子：只比较惯性不足以推出 (100.3)，下面会同时比较惯性与 $K_2$ 的 Frobenius。

## 2. 全局二面体结构与 Frobenius 平方

### 2.1 十二次差与反圆分作用

$\lambda_E^{12}$ 和 $\lambda_A^{12}$ 在 $p$ 以外均不分歧，且按取向在 $p$ 的惯性相同。商特征 $\beta^{12}$ 因而处处不分歧；$K$ 类数一且没有实无限处，故它平凡。这重述 R21 的准确用途，没有把模 $p$ 有理性提升为特征零 CM 系数结论。

令 $\iota$ 是复共轭。两条 Cartan 特征都满足
$$\lambda^\iota=\lambda^p.$$
因 $p\equiv-1\pmod{12}$ 且 $\beta^{12}=1$，
$$
\beta^\iota=\beta^{-1},\qquad\gamma^\iota=\gamma^{-1}.
                                                               \tag{100.7}
$$
$\ker\gamma\subset G_K$ 固定的域 $B/\mathbb Q$ 为二面体扩张，或其阶至多四的商。若 $\gamma$ 阶为四，则
$$
\operatorname{Gal}(B/\mathbb Q)=D_4
=\langle r,s:r^4=s^2=1,\ srs=r^{-1}\rangle,               \tag{100.8}
$$
其中 $\operatorname{Gal}(B/K)=\langle r\rangle$。这里 $D_4$ 的阶为八。扩张确实分裂，因为复共轭在 $K$ 上非平凡而本身的阶为二；不能把它误换成四元数扩张。

更强地，对每个 $g\in G_{\mathbb Q}\setminus G_K$，
$$
\boxed{\beta(g^2)=1,\qquad\delta(g^2)=1.}                 \tag{100.9}
$$
事实上写 $g=h\iota$，$h\in G_K$，则
$\beta(g^2)=\beta(h)\beta(\iota h\iota^{-1})=1$。

### 2.2 在三处，$\delta$ 连整个分解群也平凡

令 $K_3=K\otimes\mathbb Q_3$。若 $\gamma$ 阶至多二，则 $\delta=1$，结论自动成立。否则在 (100.8) 中分析三处的分解群和惯性。

野惯性为 pro-$3$，在二群 $D_4$ 中平凡。因此惯性像为循环二群。它映到 $\operatorname{Gal}(K_3/\mathbb Q_3)$ 非平凡，因为 $K$ 在三分歧。$D_4$ 中不在旋转子群内的元素均为阶二反射，所以惯性像恰为一个反射子群 $\langle s'\rangle$。

分解群正规化这个阶二子群，也就中心化它。而
$$
C_{D_4}(s')\cap\langle r\rangle=\{1,r^2\}.
$$
$\delta=\gamma^2$ 在这两个旋转上均取一。因此
$$
\boxed{\delta|_{G_{K_3}}=1.}                            \tag{100.10}
$$
这里使用的是整个分解群，未遗留一个可能非平凡的未分歧二次字符。

R96 另给
$$\Delta\in-3\mathbb Q_3^{\times2},$$
而 $-3$ 在 $K_3$ 中为平方，所以
$$
\chi_\Delta|_{G_{K_3}}=1.                               \tag{100.11}
$$

## 3. 在二以外比较实际惯性

### 3.1 素数 $q\ge5$、$q\ne p$

整 $j$ 使 $E$ 潜在好约化。由于 $K$ 在 $q$ 不分歧，实际惯性在 Cartan 内，有限惯性群为循环群，其阶属于 $1,2,3,4,6$。它在模 $p$ 上忠实。

$A$ 在这些 $q$ 有好约化，所以 $\lambda_A$ 在惯性上平凡。于是 $\delta=\lambda_E^6$ 在惯性上仅当阶为四时非平凡，且此时给出该四阶群唯一的非平凡二次商。

另一方面，$E[2]$ 的三个非零点的置换符号正是 $\chi_\Delta$。惯性阶为三或六时，模二的非平凡部分是三循环，符号为正；阶二的自同构是 $[-1]$，在 $E[2]$ 上平凡。阶四生成元的平方为 $[-1]$，自身在 $E[2]$ 上是换位，符号为负。这个阶四元不能模二消失：若一个阶四的整二进矩阵为 $1+2M$ 且平方为 $-1$，模四就会给 $1=-1$，矛盾。

因此在每个这样的 $q$，
$$
\delta|_{I_q}=\chi_\Delta|_{I_q}.                        \tag{100.12}
$$

### 3.2 素数 $p$

R66 的小惯性给最小好约化分歧指数 $3$ 或 $6$。在相容取向下，$A$ 在 $p$ 好超奇异，而
$$\lambda_E|_{I_p}=\lambda_A|_{I_p}\,\xi,\qquad\xi^6=1.$$
故 $\delta|_{I_p}=1$。

同一温和公式给 $v_p(\Delta)\equiv2,4,8,10\pmod{12}$，所以 $\chi_\Delta$ 在 $p$ 也不分歧。这里判别式的偶赋值足够，不要求它在 $\mathbb Q_p$ 中为平方。

### 3.3 全局差只能是 $1$ 或 $\chi_{-2}$

由 (100.10)–(100.12) 及 $p$ 处比较，二次特征
$$\tau=\delta\,\chi_\Delta|_{G_K}$$
在 $K$ 的二以外均不分歧，且在 $K_3$ 的整个分解群平凡。

二在 $K$ 惰性且为主素理想，$h_K=1$。Kummer 理论因而给：任一仅允许在二处分歧的二次扩张，其平方类可取为
$$\epsilon\in\{1,-1,2,-2\}.$$
具体地，定义元在二以外的所有赋值为偶数；用主理想除去这些平方，再用
$\mathcal O_K^\times/\mathcal O_K^{\times2}=\{\pm1\}$ 即得到这个清单。

在 $K_3$ 中，$-1$ 和 $2$ 的单位剩余类为负一，均非平方；$1$ 和 $-2$ 为平方。因此
$$
\boxed{
\delta=\chi_\Delta|_{G_K}\,\chi_\epsilon|_{G_K},
\qquad \epsilon\in\{1,-2\}.
}                                                        \tag{100.13}
$$
这里尚未把 $\epsilon$ 擅自设为一；二处的比较将决定它。

## 4. 二处 Frobenius 如何消除未分歧歧义

记 $K_2/\mathbb Q_2$ 为未分歧二次扩张，它正是
$$K_2=\mathbb Q_2(\sqrt{-3}).$$
惯性 $I_2$ 已包含于 $G_K$。取任一 $\mathbb Q_2$ 的算术 Frobenius 提升 $g$；因二在 $K$ 惰性，$g\notin G_K$，而 $g^2$ 是 $K_2$ 的算术 Frobenius 提升。由 (100.9)，
$$\delta(g^2)=1.                                       \tag{100.14}$$

同样，对任意有理二次特征 $\chi_d$，
$$\chi_d(g^2)=\chi_d(g)^2=1.                            \tag{100.15}$$
因此在 $G_{K_2}$ 上，如果 $\delta$ 与 $\chi_d$ 的惯性限制相同，则它们在 Frobenius 提升上也相同，从而是同一个完整的局部字符。

特别，若 $\delta$ 在二不分歧，则
$$\boxed{\delta|_{G_{K_2}}=1.}                          \tag{100.16}$$

$A$ 在二的有限惯性为阶三，故 $\lambda_A^6$ 在 $I_2$ 上平凡；更一般地，CM 自同构仅给 $\mu_6$，也足以推出所需的六次幂平凡性。于是 $\delta|_{I_2}$ 非平凡恰对应 $E$ 的阶四惯性。

## 5. 导子六：精确比较和偶判别式赋值

$c=6$ 使 $\eta$ 在二分歧，因而实际有限惯性含有阶三元。$K$ 在二不分歧，模 $p$ 惯性在循环 Cartan 内；忠实性使实际有限惯性本身循环。椭圆曲线的循环自同构只可能有阶 $1,2,3,4,6$，故
$$e_2=3\text{ 或 }6.$$
所以 $\delta|_{I_2}=1$，再由 (100.16) 得
$$\delta|_{G_{K_2}}=1.                                 \tag{100.17}$$

取一个好约化扩张，其分歧指数为 $e_2$。判别式缩放关系给
$$12\mid e_2\,v_2(\Delta),$$
故 $v_2(\Delta)$ 为偶数。也可先在惯性域上使用同一关系；有限未分歧扩张不会改变该赋值。若需下沉到有限域，惯性商与 Frobenius 截面给分歧指数恰为 $e_2$ 的有限好约化扩张。

假设 (100.13) 中 $\epsilon=-2$。在 $K_2$ 上，(100.17) 就会给
$$[\Delta]=[-2].$$
但未分歧基变换保持赋值，左边的赋值为偶数，右边为奇数，不可能。于是 $\epsilon=1$，全局 (100.3) 得证。

再由 (100.17)，$\Delta$ 在 $K_2$ 中为平方。因为
$$\ker\bigl(\mathbb Q_2^\times/\mathbb Q_2^{\times2}
 \longrightarrow K_2^\times/K_2^{\times2}\bigr)=\{1,-3\},$$
得到 (100.4) 的第一行。

## 6. 导子九：先排除二处四阶惯性

$c=9$ 使 $\eta$ 在二不分歧。R66 的 $v_3(p^2-1)=1$ 保证 $\eta$ 在 Cartan 的阶三子群上忠实，所以有限惯性不含阶三元。它仍循环，因此
$$e_2\in\{1,2,4\}.                                     \tag{100.18}$$

假设 $e_2=4$。$\mathbb Q_2$ Frobenius 落在 $N\setminus C$；它把阶四惯性元共轭为其 $p$ 次幂，而 $p\equiv-1\pmod4$。因此实际局部模 $p$ 像非交换，完全满足下面已发表分类的非交换假设。

### 6.1 已发表二进分类的准确输入

使用 Freitas–Kraus，*On the symplectic type of isomorphisms of the $p$-torsion of elliptic curves*，Memoirs AMS **277** (2022), no. 1361。以下编号均为[作者 v5](https://arxiv.org/pdf/1607.01218v5)的编号，正式排印版编号可能不同。

1. **Proposition 6、Table 5，印刷 pp. 29–31；Proposition 8，pp. 34–35：** 当 $e_2=4$ 时，极小模型的赋值为
   $$
   (v_2c_4,v_2c_6,v_2\Delta)=(5,8,9)\quad\text{或}\quad(7,11,15).
   $$
   记波浪号为去除全部二幂后的奇单位。非交换情形满足
   $$
   \widetilde c_4\equiv5\widetilde\Delta\pmod8,\qquad
   \widetilde c_4\equiv1\text{ 或 }5\pmod8.               \tag{100.19}
   $$
2. **Theorem 17(2)，p. 32；Lemma 9(iii)，pp. 38–39：** 好约化四次域由
   $$
   X^4+12X^2+6\quad\text{或}\quad X^4+4X^2+6             \tag{100.20}
   $$
   定义；其唯一二次子域为 $\mathbb Q_2(\sqrt{-2})$，且这个二次域包含于实际 $p$ 除法域。

这些是已发表输入；没有使用之后未发表的简化稿或数值局部样本。

### 6.2 两个实际二次字符在二处恰好相差 $\chi_{-1}$

由 (100.19)，$\widetilde\Delta\equiv1$ 或 $5\pmod8$；$v_2(\Delta)$ 为奇数。在 $K_2$ 中，单位平方类 $5$ 与 $-3$ 同类，已成为平方，所以
$$
\boxed{\chi_\Delta|_{G_{K_2}}=\chi_2|_{G_{K_2}}.}        \tag{100.21}
$$

另一方面，(100.20) 的二次子域在惯性上给阶四群唯一的非平凡二次商。$\lambda_A^6$ 在二的惯性上平凡，$\lambda_E^6$ 正是这个二次商，故
$$\delta|_{I_2}=\chi_{-2}|_{I_2}.$$
这一等式没有自行消除未分歧因子；继续取第 4 节的 $g^2$。由 (100.14)–(100.15)，两边在这个 $K_2$ Frobenius 提升上都取一。因此
$$
\boxed{\delta|_{G_{K_2}}=\chi_{-2}|_{G_{K_2}}.}          \tag{100.22}
$$

式 (100.21)–(100.22) 给
$$
\tau|_{G_{K_2}}=\chi_{-1}|_{G_{K_2}}.                   \tag{100.23}
$$
但 (100.13) 要求 $\tau$ 为平凡字符或 $\chi_{-2}|_{G_K}$。二者在 $K_2$ 都不等于 $\chi_{-1}$：
$K_2/\mathbb Q_2$ 未分歧，不能包含分歧的 $\mathbb Q_2(i)$；而
$(-1)/(-2)=1/2$ 的赋值为奇数，不能在 $K_2$ 中为平方。
这与 (100.23) 矛盾，故
$$\boxed{e_2\ne4.}                                     \tag{100.24}$$

## 7. 导子九的好二次扭曲、全局恒等式和 $16\mid X$

由 (100.18)、(100.24)，$e_2=1$ 或 $2$。存在 $\mathbb Q_2$ 上的二次扭曲 $E_0$ 有好约化。对阶二情形，可以直接证明：有限惯性是中心 $\{\pm1\}$，惯性域与 Frobenius 截面构成 $C_2\times\widehat{\mathbb Z}$；将该惯性二次特征延拓并令 Frobenius 值为一，扭曲后由 Néron–Ogg–Shafarevich 判据得到好约化。已发表的 Coppola (2026) Lemma 4.2 也给出这个下沉结论，而非仅在最大未分歧域上扭曲。

二次扭曲不改变 $N/C$ 商域。$E_0$ 的二处 Frobenius 仍在 $N\setminus C$，所以
$$a_2(E_0)\equiv0\pmod p.$$
Hasse 界给 $|a_2|\le2\sqrt2$，而 $p>37$，故
$$a_2(E_0)=0.                                          \tag{100.25}$$

取 $E_0$ 的整好模型。其 $a_1$ 必为偶数：若 $a_1$ 模二为一，则对 $\mathbb F_2$ 的两个 $x$，关于 $y$ 的方程分别有恰一个解和偶数个解，因而 $\#E_0(\mathbb F_2)$ 为偶数，迹 $3-\#E_0(\mathbb F_2)$ 为奇数，与 (100.25) 矛盾。好约化又使 $a_3$ 为奇数；否则判别式模二为零。

于是
$$
4\mid b_2,\qquad2\mid b_4,\qquad b_6\text{ 奇}.
$$
使用整 Weierstrass 恒等式，
$$
c_4=b_2^2-24b_4,\qquad
\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6,
$$
得到
$$
16\mid c_4(E_0),\qquad \Delta(E_0)\equiv5\pmod8.         \tag{100.26}
$$
因此 $\Delta(E_0)$ 的二进平方类是 $-3$。二次扭曲使判别式乘以六次幂，换模型乘以十二次幂，所以
$$
[\Delta]=[-3]\text{ 在 }\mathbb Q_2^\times/\mathbb Q_2^{\times2}.
                                                               \tag{100.27}
$$

现在 $\delta$ 在二的惯性平凡，由 (100.16) 在整个 $G_{K_2}$ 平凡；(100.27) 使 $\chi_\Delta$ 也平凡。因而 (100.13) 中 $\epsilon=-2$ 不可能，$\epsilon=1$，完成全局恒等式 (100.3) 及 (100.4) 的第二行。

好模型判别式为单位；若 $j\ne0$，(100.26) 给
$$v_2(j)=3v_2(c_4(E_0))\ge12.$$
R96 的 $d=3^bp^r$ 为奇数，故 $v_2(j)=3v_2(X)$，得到 $16\mid X$。没有把局部好模型的导子或判别式赋值误当作原全局模型的相同数值；这里使用的均是扭曲不变的 $j$ 和平方类。

## 8. 与实际二除法域的相交关系

设 $\gamma$ 阶恰为四，记
$$B=\overline{\mathbb Q}^{\ker\gamma},\qquad
F=\mathbb Q(\sqrt\Delta),\qquad H=\mathbb Q(E[2]).$$
由 (100.3)，$B$ 中固定中心 $\langle r^2\rangle$ 的二次复合域正是
$$\boxed{B^{\langle r^2\rangle}=KF.}                     \tag{100.28}$$
特别，$F\ne K$，并且 $B$ 确实包含实际二除法域的二次子域。

R96 的三处实际 $S_3$ 惯性使 $\operatorname{Gal}(H/\mathbb Q)=S_3$。$B/\mathbb Q$ 为二群扩张，故 $H\cap B$ 的次数至多二；(100.28) 已使 $F$ 包含其中，所以
$$\boxed{H\cap B=F.}                                    \tag{100.29}$$
对原来的三次商域 $L$，其二次子域为 $K$，于是同样有
$$B\cap L=K,\qquad H\cap L=\mathbb Q.                    \tag{100.30}$$
对最后一个等式，两个 $S_3$ 扩张的非平凡正规公共子域只能是其唯一二次子域，或整个 $S_3$ 域；但它们的二次子域分别为 $F$ 和 $K$，且 $F\ne K$，故两种非平凡交都不可能。

这些结论以实际字符和实际除法域为对象，不声称任意满足相同抽象群结构的域都能来自一条曲线。

在 R98 的三个层数中，任何剩余非 CM 曲线都存在新的四阶惯性素数，因此 $\gamma$ 的阶确为四；(100.28)–(100.30) 适用于全部这些剩余候选。

## 9. 尚未排除的自由度与来源

本文把二处的四阶惯性彻底排除，也把四次差的二次商固定为实际 $\Delta$。但在 $q\ge5$、$q\ne p$，四阶惯性仍可在
$$q\equiv1\text{ 或 }11\pmod{12}$$
出现；R98 恰迫使剩余三个小层的非 CM 曲线至少出现一次。这些素数的支集尚未有上界。$\gamma$ 的四次提升及 $E[2]$ 的三次扩张仍是需要同时实现的全局数据；只取它们的群阶或密度不能给小素数界，也不能完成统一排除。

所用来源：

- [R21](R21-twelfth-power-signature-and-cm-twists.md)：十二次幂惯性型及类数一的 CM 比较。
- [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际小惯性与准确三次角色。
- [R96](R96-actual-cubic-discriminant-support-and-local-three-branches.md)：整 $j$ 下的三处实际同域、$\Delta\in-3\mathbb Q_3^{\times2}$ 及三次支撑。
- [R98](R98-small-levels-require-new-quartic-inertia.md)：三个小层必出现新的四阶素数。
- N. Freitas、A. Kraus，*On the symplectic type of isomorphisms of the $p$-torsion of elliptic curves*，Memoirs AMS **277** (2022), no. 1361；[出版标识](https://doi.org/10.1090/memo/1361)，[作者 v5](https://arxiv.org/pdf/1607.01218v5)。准确输入为作者 v5 的 Proposition 6/Table 5、Proposition 8、Theorem 17(2)、Lemma 9(iii)，页码见 §6.1。已在仓库 R22/R36 说明其编号与正式排印版可能不同。
- N. Coppola，*Wild Galois representations: elliptic curves with wild cyclic reduction*，Research in Number Theory **12** (2026), article 49，2026-05-04 正式发表，[出版全文](https://link.springer.com/article/10.1007/s40993-026-00730-5)，Lemma 4.2：二处 $C_2$ 惯性可在基域上用二次扭曲达到好约化。本文第 7 节同时给出所需下沉证明，不依赖其算法实现。

