# R15：商二次域的分歧素数分裂条件与 $p\equiv1\pmod3$ 时的立方分子

日期：2026-11-12。状态：**已证明的必要条件；中间进展**。不声称文献优先权，也不声称获得一致性界。

## 1. 陈述

设 $p>37$，$E/\mathbb Q$ 无 CM，且 $\bar\rho_{E,p}$ 不满射。由 R1，其像可取为完整的非分裂 Cartan 正规化子 $N$。记 $C\subset N$ 为 Cartan，$\varepsilon=\bar\rho_{E,p}\bmod C$，并写
$$
K=\overline{\mathbb Q}^{\ker\varepsilon}=\mathbb Q(\sqrt{-D}),
\qquad D>0\text{ 无平方因子}.
$$
R5 已证明 $K$ 虚二次，$p$ 在 $K$ 中不分歧且惰性。以下结论成立。

1. 每个在 $K$ 中分歧的奇素数 $q$ 都满足
   $$
   \boxed{\left(\frac{-p}{q}\right)=1.}
   \tag{1.1}
   $$
   因而这些 $q$ 全部分裂于 $\mathbb Q(\sqrt{-p})$。这里包括 $q=3$；证明没有把 $3$ 处的野惯性误当作平凡。

2. 写 $D=2^\delta D_0$，其中 $D_0$ 为正奇无平方因子整数、$\delta\in\{0,1\}$。则有以下必要同余条件：

   | $p$ 的同余类 | 对 $D$ 的限制 |
   |---|---|
   | $p\equiv1\pmod4$ 且 $D$ 奇 | $D\equiv3\pmod4$ |
   | $p\equiv1\pmod8$ 且 $D$ 偶 | $D_0\equiv3\pmod4$ |
   | $p\equiv5\pmod8$ 且 $D$ 偶 | $D_0\equiv1\pmod4$ |
   | $p\equiv3\pmod8$ | $D$ 必须为奇数 |
   | $p\equiv7\pmod8$ | 本表不给 $D$ 的奇偶性以额外限制 |

   例如，$p\equiv1\pmod4$ 时，$K$ 的基本判别式在 $2$ 处的赋值不可能为 $2$；若 $2$ 分歧，则该赋值只能为 $3$。这是一项全局推论，不能把它的证明替换成未经证明的 $2$ 处温和性断言。

3. 若 $p\equiv1\pmod3$，则存在互素整数 $A,B$，$B>0$，满足
   $$
   \boxed{j(E)=\frac{A^3}{B^p},\qquad p\nmid AB.}
   \tag{1.2}
   $$
   $A$ 可以为负数。尤其，$j(E)$ 的既约分子是整数立方，而且 $v_p(j(E))=0$。在 $2,3$ 处无需添加未定的立方自由因子。

这些条件均来自**实际全局异常表示**。它们不由 R7 的有限 Frobenius 窗口自动保证，也没有提供所缺的全局高度上界。

## 2. 群论记号

把 $V=\mathbb F_{p^2}$ 视为二维 $\mathbb F_p$-向量空间。对 $a\in\mathbb F_{p^2}^\times$ 记 $m_a$ 为乘法，记 $s(x)=x^p$。则
$$
C=\{m_a:a\in\mathbb F_{p^2}^\times\},
\qquad N=C\sqcup Cs,
$$
$$
s m_a s^{-1}=m_{a^p},\qquad
\det(m_a)=a^{p+1},\qquad\det(s)=-1.
$$
若 $t\in N\setminus C$ 且 $\det(t)=1$，写 $t=m_b s$，则
$$
-b^{p+1}=1,\qquad t^2=m_{b^{p+1}}=-I.
\tag{2.1}
$$
所以每个这样的 $t$ 的阶恰为 $4$。此外，$C\cap\mathrm{SL}_2(\mathbb F_p)$ 是阶为 $p+1$ 的循环群；$N\cap\mathrm{SL}_2(\mathbb F_p)$ 的阶为 $2(p+1)$。

## 3. 任意奇分歧素数的局部证明，包括 $3$

固定在 $K$ 中分歧的奇素数 $q$。由 R5，$q\ne p$。令
$$
I=\bar\rho_{E,p}(I_q),\qquad P=\bar\rho_{E,p}(P_q),
$$
其中 $P_q$ 为野惯性。因为行列式为模 $p$ 圆分特征，而 $q\ne p$，有 $I\subset\mathrm{SL}_2(\mathbb F_p)$。$P$ 是奇 $q$ 群，故其到 $N/C$ 的映射平凡，因而
$$
P\subset C\cap\mathrm{SL}_2(\mathbb F_p).
$$
特别地，$P$ 为循环奇阶群。由于 $\varepsilon(I_q)\ne1$，循环群 $I/P$ 的生成元可选取一个提升 $t\in I\setminus C$。由 (2.1)，$t^2=-I$，且 $P$ 为奇阶，因此 $t$ 在 $I/P$ 中的阶也是 $4$。

令 $h$ 为某个算术 Frobenius 提升的矩阵像。有限温和商中的 Frobenius 关系给出
$$
h t h^{-1}=u t^q\qquad\text{对某个 }u\in P.
\tag{3.1}
$$
这里没有断言 $u=1$。对 $a\in P$，由 $a\in C$、$\det(a)=1$ 得 $a^p=a^{-1}$，故 $t$ 对 $P$ 的共轭作用是取逆。因为平方映射在奇阶循环群 $P$ 上可逆，可取 $w\in P$ 使 $w^2=u^{-1}$。置 $h'=wh$，则
$$
h't(h')^{-1}
=w u t^q w^{-1}
=u w^2t^q=t^q,
\qquad\det(h')=\det(h)=q\bmod p.
\tag{3.2}
$$
这一步消除了 (3.1) 中的野惯性误差，也说明为什么证明适用于 $q=3$。

若 $q\equiv1\pmod4$，则 $t^q=t$。在 $N$ 中，与 $t=m_bs$ 交换的 $C$ 元素只有标量：
$$
m_a t=t m_a\iff a=a^p\iff a\in\mathbb F_p^\times.
$$
同理，外陪集中与 $t$ 交换的元素恰为标量乘 $t$。这些矩阵的行列式都是平方，因为 $\det(t)=1$。于是
$$
\left(\frac{q}{p}\right)=1
\qquad(q\equiv1\pmod4).
\tag{3.3}
$$

若 $q\equiv3\pmod4$，则 $t^q=-t$。任选 $\eta\in\mathbb F_{p^2}^\times$ 满足 $\eta^p=-\eta$。这时 $\eta^2\in\mathbb F_p^\times$ 是非平方：若其为平方，则 $\eta\in\mathbb F_p$，与 $p$ 奇且 $\eta^p=-\eta$ 矛盾。矩阵 $m_\eta$ 与 $t$ 反交换。$N$ 中所有与 $t$ 反交换的矩阵为
$$
\mathbb F_p^\times m_\eta\ \sqcup\ \mathbb F_p^\times m_\eta t.
$$
其行列式均属于 $-\eta^2(\mathbb F_p^\times)^2$，因此
$$
\left(\frac{q}{p}\right)
=-\left(\frac{-1}{p}\right)
\qquad(q\equiv3\pmod4).
\tag{3.4}
$$

最后应用二次互反律。若 $q\equiv1\pmod4$，(3.3) 直接给出 $(-p/q)=1$。若 $q\equiv3\pmod4$，(3.4) 给
$$
\left(\frac{p}{q}\right)
=\left(\frac{q}{p}\right)\left(\frac{-1}{p}\right)=-1,
$$
再乘以 $(-1/q)=-1$，同样得到 (1.1)。

本节只用了 $N$ 的矩阵结构、行列式为圆分特征和局部惯性结构。因此分裂结论并非依赖于另一个未经证明的椭圆曲线全局定理。

## 4. $2$ 的条件由全局互反关系推出

对每个奇素数 $q\mid D_0$，它在 $K$ 中分歧，故满足上节结论。由 (3.3)、(3.4)，
$$
\prod_{q\mid D_0}\left(\frac q p\right)
=
\begin{cases}
(-1/D_0),&p\equiv1\pmod4,\\
1,&p\equiv3\pmod4.
\end{cases}
\tag{4.1}
$$
这里 $(-1/D_0)$ 为 Jacobi 符号，$D_0=1$ 时取值 $1$。另一方面，$p$ 在 $K$ 中惰性给出
$$
-1=\left(\frac{-D}{p}\right)
=\left(\frac{-1}{p}\right)
\left(\frac2p\right)^\delta
\prod_{q\mid D_0}\left(\frac qp\right).
\tag{4.2}
$$
若 $p\equiv1\pmod4$，这等价于
$$
\left(\frac2p\right)^\delta\left(\frac{-1}{D_0}\right)=-1.
$$
若 $p\equiv3\pmod4$，则等价于 $(2/p)^\delta=1$。用 $(2/p)=(-1)^{(p^2-1)/8}$ 展开，即得第 1 节的表。全过程没有假设 $2$ 处野惯性为循环或平凡。

## 5. $p\equiv1\pmod3$ 时所有正 $j$-赋值都是 $3$ 的倍数

先取任意有限素数 $q\ne p$，且 $v_q(j(E))\ge0$。椭圆曲线具有潜在好约化。设 $L/\mathbb Q_q^{\mathrm{nr}}$ 为使它取得好约化的最小扩张，令 $e=[L:\mathbb Q_q^{\mathrm{nr}}]$。这里可在一个足够大的有限非分歧基域上作相同计算。

标准潜在好约化惯性定理说明：$e$ 等于 $p$-进 Tate 模上的有限惯性像的阶，此像嵌入好约化曲线的自同构群。因此 $e$ 的素因子只有 $2,3$。由于 $p>37$，从该有限惯性像到模 $p$ 像的约化是单射：约化核是 pro-$p$ 群，不能与阶互素于 $p$ 的有限群有非平凡交。因此
$$
e=|\bar\rho_{E,p}(I_q)|
\mid |N\cap\mathrm{SL}_2(\mathbb F_p)|=2(p+1).
$$
如果 $p\equiv1\pmod3$，右端不被 $3$ 整除，故 $3\nmid e$。

在 $\mathbb Q_q$ 取极小 Weierstrass 模型，其判别式为 $\Delta$、不变量为 $c_4$。将其基变换到 $L$ 后，与一个好约化模型之间的 Weierstrass 坐标变换使判别式相差一个十二次幂。因好约化模型的判别式赋值为零，
$$
12\mid e\,v_q(\Delta).
$$
既然 $3\nmid e$，就有 $3\mid v_q(\Delta)$，所以
$$
v_q(j(E))=3v_q(c_4)-v_q(\Delta)\equiv0\pmod3.
\tag{5.1}
$$

这同时涵盖 $q=2,3$：在那里可以有野惯性，但以上论证只需要 $3\nmid e$，不需要逐一假定 Kodaira 类型，也不需要它们温和。

## 6. $p$ 处：潜在普通约化不可能，故 $v_p(j)=0$

R2 给出 $v_p(j(E))\ge0$。R5 所用的 Zywina Lemma 2.3(i) 给出 $\bar\rho_{E,p}(I_p)\subset C$。行列式在 $I_p$ 上的像为全部 $\mathbb F_p^\times$，因此该惯性群不能只由标量组成，因为标量的行列式都是平方。它含有一个非标量的 $C$ 元素；这种元素在 $\mathbb F_p^2$ 上没有不变直线。

现在说明 $E$ 不能在 $p$ 具有潜在普通约化。否则，取一个有限 Galois 扩张 $M/\mathbb Q_p$，使 $E/M$ 有好普通约化。几何 $p$ 挠点到特殊纤维的约化映射的核为一个阶 $p$ 的子群。由于好约化模型在进一步扩张下唯一，并且 Galois 的半线性作用保持单位元及约化映射，这个核在全部 $G_{\mathbb Q_p}$ 下稳定。它给出 $E[p]$ 的一条 $G_{\mathbb Q_p}$ 不变直线，特别是 $I_p$ 不变直线，与上一段矛盾。

因此 $E$ 在 $p$ 潜在超奇异。若 $v_p(j(E))>0$，取得好约化后的特殊纤维具有 $j=0$。但在 $p\equiv1\pmod3$ 时，$j=0$ 曲线普通。可直接由 Hasse 不变量验证：在代数闭剩余域中写作 $y^2=x^3+b$，$b\ne0$；$(x^3+b)^{(p-1)/2}$ 的 $x^{p-1}$ 系数为
$$
\binom{(p-1)/2}{(p-1)/3}\,b^{(p-1)/6},
$$
它非零模 $p$。这里 $p\equiv1\pmod6$，故各指数为整数。这与潜在超奇异矛盾，因而
$$
v_p(j(E))=0.
\tag{6.1}
$$

由 (5.1)、(6.1)，$j$ 的既约分子中每个素数的指数均为 $3$ 的倍数，故分子为某个整数 $A$ 的立方。R2 已证明既约分母为 $B^p$ 且 $p\nmid B$。再由 (6.1) 得 $p\nmid A$，证明 (1.2)。

## 7. 范围与不能推出的结论

- 对 $p\equiv1\pmod3$，(1.2) 只固定分子、分母的幂次，不给 $|A|$ 或 $B$ 的上界。无穷多个满足这种形式的有理数仍然存在；它们一般并不来自异常曲线。
- (1.1) 限制的是实际商二次域的分歧素数。它没有证明 $D$ 有统一上界。固定 $p$ 时，分裂于 $\mathbb Q(\sqrt{-p})$ 的素数仍然无穷多。
- 当 $K=\mathbb Q(i)$ 且 $p\equiv3\pmod4$，奇分歧素数集合为空，表中条件也相容。因此本结论不排除 R11、R13 所聚焦的固定 CM 参考曲线同余情形。
- 若 $p\equiv1\pmod3$，则 $3$ 不可能在 $K$ 中分歧，因为 (1.1) 在 $q=3$ 会要求 $p\equiv2\pmod3$。这是本定理的直接推论，不是对主目标的完整解答。

## 8. 外部输入与出处

1. D. Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, Bulletin of the London Mathematical Society **54** (2022), 2404–2417；[作者原文](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)，Lemma 2.3(i) 给出商特征在 $p$ 不分歧；其 Lemma 2.3 的证明也明确给出潜在好约化时有限惯性像嵌入特殊纤维自同构群。
2. J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Inventiones Mathematicae **15** (1972), 259–331，§1.3（温和惯性）、§5.6（潜在好约化惯性）。
3. J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed. (2009), Chapter III（Weierstrass 坐标变换、不变量、Hasse 不变量），Chapter VII（约化与惯性）；本证明用到的有限群计算、$3$ 处野惯性修正和全局二次互反运算均已在上文展开。

本结果不使用 2026 年尚未确认发表的新预印本作为必要输入。
