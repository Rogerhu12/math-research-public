# R44 之后：理想范数、元素范数与分裂分母的缺口

日期：2026-11-12。会话：nonsplit_frobenius。

本笔记继续核验 R44 的奇惰性条件能否组合成更强的全局范数或理想类约束。得到一个精确的范数翻译及一个反例：理想范数结论成立；当 $B=1$ 时可提升为元素范数，但这没有新增筛选；一般 $B$ 的提升需要额外分裂分母条件，且这些条件并不由 CM 参考曲线与 Tate 曲线在分母处的真实局部同构自动给出。因此暂不单列新结果编号。

## 1. 设定

假设
$$
p>37,\qquad p\equiv19\pmod{24},\qquad
B>0,\qquad (B,6p)=1,
$$
并保留 R24 对每个 $\ell\mid B$ 的分母条件
$$
\ell\equiv\chi_{-4}(\ell)\pmod p.
\tag{N.1}
$$
令
$$
L=\mathbb Q(\sqrt{-p}),\qquad
U=\chi_{-4}(B)(-2)^\alpha B,\qquad F=L(\sqrt U),
$$
其中 $\alpha\in\{0,1\}$。允许 $U$ 是平方，此时把 $F=L$ 的范数理解为恒等映射。

令
$$
Q=\prod_{\substack{q\mid d\\q\ \mathrm{odd}\\q\equiv3\ (4)}}q
$$
为 $d$ 的正的奇惰性部分；这里允许 $q=p$ 出现在 $Q$ 中。于是 $Q$ 平方自由、$(Q,2B)=1$。空积取 $1$。

R44 的不依赖 III/III* 的条件等价于
$$
q\mid Q,\ q\ne p,\ \left(\frac qp\right)=1
\quad\Longrightarrow\quad
\left(\frac Uq\right)=1.
\tag{N.2}
$$
确实，对 $q\equiv3\pmod4$，
$$
\left(\frac Uq\right)
=\chi_{-4}(B)\left(\frac{-2}q\right)^\alpha
\left(\frac Bq\right)
=\left(\frac{-2}q\right)^\alpha\left(\frac qB\right).
$$

## 2. 完整理想范数解释

**命题。** 条件 (N.2) 等价于：存在 $F$ 的分式理想 $\mathfrak a$，使
$$
N_{F/L}(\mathfrak a)=(Q)
\tag{N.3}
$$
为 $L$ 中的理想等式。

**证明。** 对奇素数 $q\ne p$，
$$
q\text{ 在 }L\text{ 分裂}
\quad\Longleftrightarrow\quad
\left(\frac{-p}q\right)=1
\quad\Longleftrightarrow\quad
\left(\frac qp\right)=1.
$$

若 $q\mid Q$ 在 $L$ 分裂，两个对应的 $L$-素理想在 $(Q)$ 中指数均为 $1$。由于 $q\nmid U$，$F/L$ 在这些地方不分歧；这样的指数能来自理想范数，当且仅当对应素理想在 $F/L$ 分裂，也就是 $(U/q)=1$。这恰是 (N.2)。

若 $q\mid Q$ 在 $L$ 惰性，则其剩余域为 $\mathbb F_{q^2}$。$U$ 是来自 $\mathbb F_q^\times$ 的单位，所以在 $\mathbb F_{q^2}$ 中为平方。Hensel 引理使 $F/L$ 在该处分裂，因而指数 $1$ 允许。

若 $p\mid Q$，则 $(p)=\mathfrak p^2$ 在 $L$ 分歧。$p\nmid U$，所以 $F/L$ 在 $\mathfrak p$ 处分裂或是不分歧二次扩张；理想范数的剩余次数为 $1$ 或 $2$，都允许指数 $2$。

其余地方在 $(Q)$ 中指数为 $0$，不会造成理想范数限制。逐素理想取所需指数，得到 (N.3)；反向由理想范数的赋值公式同样成立。证毕。

这只是理想范数，尚未证明可以令 $\mathfrak a$ 为由一个元素生成的理想，更没有证明某个积分范数方程具有解。

## 3. 元素范数的精确附加条件

**命题。** 保持 (N.1)。在满足 (N.2) 的前提下，
$$
Q\in N_{F/L}(F^\times)
\tag{N.4}
$$
成立，当且仅当
$$
\boxed{
\ell\mid B,\quad v_\ell(B)\text{ 奇},\quad
\ell\equiv1\pmod4
\quad\Longrightarrow\quad
\left(\frac Q\ell\right)=1.}
\tag{N.5}
$$

**证明。** 若 $F=L$，则 $U$ 为平方，$B$ 的所有奇素数赋值均偶，(N.5) 为空，命题显然。以下取 $F/L$ 二次。

使用二次 Hilbert 符号。对有理数 $U,Q$，在任一 $w\mid\ell$ 处，
$$
(U,Q)_{L_w}=(U,Q)_{\mathbb Q_\ell}^{[L_w:\mathbb Q_\ell]}.
\tag{N.6}
$$
这是局部 Brauer 不变量在限制映射下乘以扩张次数的公式。因此在局部次数为 $2$ 的地方，符号自动为 $1$。

因为 $p\equiv3\pmod8$，$L$ 的基本判别式为 $-p\equiv5\pmod8$。所以 $2$ 在 $L$ 惰性，$p$ 在 $L$ 分歧；这两处的局部次数都是 $2$。复数无穷处也没有范数障碍。所有在 $L$ 惰性的其他有理素数同样由 (N.6) 自动通过。

只须考虑在 $L$ 分裂的奇素数：

- 若 $\ell\mid Q$，则 $U$ 为单位，局部符号为 $(U/\ell)$，恰由 (N.2) 保证为 $1$。
- 若 $\ell\mid B$，则 $Q$ 为单位，局部符号为 $(Q/\ell)^{v_\ell(B)}$。
- 若 $\ell\nmid QB$，则 $U,Q$ 均为单位，奇剩余特征处的 Hilbert 符号为 $1$。

最后，分母条件 (N.1) 给
$$
\left(\frac{-p}{\ell}\right)
=\left(\frac\ell p\right)
=\chi_{-4}(\ell).
$$
所以 $\ell\mid B$ 在 $L$ 分裂，当且仅当 $\ell\equiv1\pmod4$。因而全部剩余局部范数条件正是 (N.5)。

$F/L$ 为循环二次扩张，Hasse 范数定理将“处处为局部范数”等价于 (N.4)，完成证明。这里只对 $F/L$ 用循环范数定理；不能误对一般双二次的 $F/\mathbb Q$ 使用同一个定理。证毕。

## 4. $B=1$ 时的结论与边界

若 $B=1$，则 (N.5) 为空。因此：

- $\alpha=0$ 时 $U=1$，范数解释没有内容。
- $\alpha=1$ 时 $U=-2$，R44 的全部纯参数条件等价于存在 $x,y\in L$，使
  $$
  x^2+2y^2=Q.
  $$

这确实是一个全局元素范数方程，但其成立已经由 R44 的局部条件和 Hasse 定理保证，不能再次当作额外排除，也不能另外假设一个未证明的理想类障碍。

例如 $p=43$、$Q=7$ 时，$(7/43)=-1$，R44 的纯参数分支没有排除它；而
$$
(\sqrt{-43})^2+2\cdot5^2=7
$$
直接给出上述范数。相反，$7$ 不是 $\mathbb Q(\sqrt{-2})/\mathbb Q$ 的范数，因为 $7$ 在该扩张惰性且赋值为奇数；基域 $L$ 的作用不能省略。

这里的未知元属于数域 $L$，不是要求代数整数。若进一步强制积分范数解，可能重新出现理想类或积分局部整体障碍，但当前没有从实际异常曲线构造出这样的积分解，不能自行添加这个要求。

## 5. 完整分母局部同构并不自动补足 (N.5)

下面给出一个准确范围内的反例：理想范数条件、分母素数同余和 CM/Tate 的真实局部模 $p$ 同构均可成立，而元素范数升级失败。它不是全局异常曲线或完整参数方程的实例。

取
$$
p=43,\qquad B=\ell=184901=1^2+430^2,\qquad
d=39=3\cdot13,\qquad \alpha=0.
$$
$\ell$ 是素数，试除至 $\lfloor\sqrt\ell\rfloor=430$ 即可确定性核验。并且
$$
\ell\equiv1\pmod{43},\qquad
\ell\equiv1\pmod4,\qquad
\ell\equiv5\pmod{12}.
$$
此时 $Q=3$、$U=\ell$。因为 $(3/43)=-1$，(N.2) 为空，理想范数条件成立。但
$$
\left(\frac3\ell\right)=-1,
$$
所以 (N.5) 失败，$3\notin N_{L(\sqrt\ell)/L}(L(\sqrt\ell)^\times)$。

还要检查这个失败并非由于只保留了很弱的分母迹条件。考虑实际 CM 曲线
$$
A_{39}:y^2=x^3-39x.
$$
有
$$
\left(\frac{13}{\ell}\right)
=\left(\frac2{13}\right)=-1,
\qquad
\left(\frac{39}{\ell}\right)=1.
$$
$\ell$ 在 $\mathbb Q(i)$ 分裂，标准 CM 曲线 $A_1$ 的 Gaussian Frobenius 范数为 $\ell$。由于 $A_1$ 的全部 $2$-挠点在 $\mathbb F_\ell$ 有理，其迹为 $2\pmod4$，故 Gaussian Frobenius 的实部为奇数。$\ell=1^2+430^2$ 的平方和分解在单位和共轭之外唯一，所以该 Frobenius 为 $\pm1\pm430i$。

$A_{39}$ 是 $A_1$ 的四次扭曲，而 $(39/\ell)=1$ 使四次扭曲因子属于 $\{\pm1\}$。因此 $A_{39}$ 的 Frobenius 同样为 $\pm1\pm430i$，从而在
$$
\mathbb Z[i]/43\mathbb Z[i]\simeq\mathbb F_{43^2}
$$
中为标量 $\pm1$。这证明
$$
\rho_{A_{39},43}(\operatorname{Frob}_\ell)=\pm I,
$$
不只是证明其迹模 $43$ 为 $\pm2$。

取 Tate 参数 $t=\ell^{43}$，并按上述标量符号作平凡或不分歧二次扭曲。$t$ 已为 $43$ 次幂，Tate 模 $43$ 扩张类为零；又 $\ell\equiv1\pmod{43}$，Frobenius 恰为同一个标量 $\pm I$。故得到一个实际的局部乘法曲线 $T/\mathbb Q_\ell$，满足
$$
T[43]\simeq A_{39}[43]
$$
作为完整 $G_{\mathbb Q_\ell}$-模。这个分母地方通过了完整 CM/Tate 同构测试，仍不强迫 (N.5)。

因此，若想对一般 $B$ 从理想范数升级为元素范数，必须增加真正的全局输入，或从参数方程推导 (N.5)。不能仅把“分母处已存在实际局部同构”代入来消掉缺口。这里没有声称上述数据满足 $A^3-1728B^{43}=\epsilon2^\alpha dZ^2$，更没有声称有全局异常曲线。

## 6. 来源

局部 Brauer 限制的次数公式以及循环扩张的 Hasse 范数定理，可参见 J. S. Milne, *Class Field Theory*, v4.03 (2020)，III §2，公式 (29)，及 VIII Theorem 3.1：[作者全文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)。前者精确给出 $\operatorname{inv}_{L_w}\operatorname{Res}=[L_w:\mathbb Q_\ell]\operatorname{inv}_{\mathbb Q_\ell}$，后者只用于循环扩张 $F/L$。这里使用的是经典已证明定理；不是调用新的研究预印本。

CM Gaussian Frobenius 与 Tate 模比较的背景和完整局部判据已在 R24、R35 给出。本笔记的素数分解、Hilbert 符号支集和反例均在上文直接核验。
