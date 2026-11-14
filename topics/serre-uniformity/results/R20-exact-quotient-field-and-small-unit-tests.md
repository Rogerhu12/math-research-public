# R20：$p\equiv1\pmod4$ 时由 $j$ 精确恢复商二次域，以及 $2,3$ 处单位判据

日期：2026-11-12。状态：**已证明的结构结论与必要条件；中间进展**。本结果不声称解决 Serre 一致性。

## 1. 精确二次域公式

设 $E/\mathbb Q$ 无 CM，$p>37$，$p\equiv1\pmod4$，且 $\bar\rho_{E,p}$ 不满射。沿用 R1、R5 的非分裂 Cartan $C$、正规化子 $N$ 和商特征 $\varepsilon$。

将 $j=j(E)$ 写成**通常的既约分数**
$$
j=\frac ab,\qquad a\in\mathbb Z,\quad b\in\mathbb Z_{>0},\quad\gcd(a,b)=1,
$$
并令
$$
n=a-1728b,\qquad \nu=v_2(n),\qquad
m=\operatorname{sf}\left(\left|\frac n{2^\nu}\right|\right),
\tag{1.1}
$$
其中 $\operatorname{sf}$ 取正的无平方因子部分。$m$ 是正奇数；$j\ne1728$ 保证 $n\ne0$。又定义
$$
\delta=
\begin{cases}
1,&v_2(j)\in\{3,6,9\},\\
0,&v_2(j)\notin\{3,6,9\}.
\end{cases}
\tag{1.2}
$$

**定理。** 商特征所确定的二次域恰为
$$
\boxed{K=\mathbb Q\bigl(\sqrt{-2^\delta m}\bigr).}
\tag{1.3}
$$
此外，$b$ 为奇数，$p\nmid bn$，且当 $\delta=0$ 时必有 $m\equiv3\pmod4$。

公式 (1.1) 使用 $j-1728$ 的实际既约分子：因为 $\gcd(a-1728b,b)=1$，它正好是 $n$。这里不把 $b$ 重新参数化成某个依赖 $p$ 的 $B^p$。因此对于固定的 $j$，所有满足 $p>37$、$p\equiv1\pmod4$ 的异常素数都给出**同一个**二次域 (1.3)。该结论只针对这一同余类的异常素数，并未声称 $p\equiv3\pmod4$ 时仍有同一公式。

## 2. 所用的已发表精确分歧输入

Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, Bull. London Math. Soc. **54** (2022), 2404–2417，[作者原文](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)，§1.1、Lemma 2.3，给出集合
$$
S(j)=\{2:v_2(j)\in\{3,6,9\}\}
\cup\{q\ge3:v_q(j-1728)>0\text{ 且为奇数}\}.
\tag{2.1}
$$
它的准确结论是：

- Lemma 2.3(i)：$\varepsilon$ 在 $p$ 以及所有 $q\notin S(j)$ 处不分歧。
- Lemma 2.3(ii)：若 $q\in S(j)\setminus\{p\}$，则 $\bar\rho_{E,p}(I_q)$ 含一个阶 $4$ 的元素，并含 $-I$。

这些结论包括 $q=2,3$，以及 (2.1) 中写出的全部小赋值例外。它们使用潜在好约化惯性分类；本结果明确引用这一已发表局部引理，不将其当作不言自明的温和惯性事实。

为了从“候选支集”得到“精确支集”，这里补写一步群论。若 $p\equiv1\pmod4$，则
$$
C\cap\mathrm{SL}_2(\mathbb F_p)
$$
为阶 $p+1\equiv2\pmod4$ 的循环群，不含阶 $4$ 的元素。对于 $q\ne p$，行列式在 $I_q$ 上平凡。如果 $q\in S(j)\setminus\{p\}$ 但 $\varepsilon$ 在 $q$ 不分歧，那么惯性像会全部落在 $C\cap\mathrm{SL}_2$ 中，与 Lemma 2.3(ii) 矛盾。因此
$$
\boxed{\varepsilon\text{ 在 }q\text{ 分歧}
\iff q\in S(j)\setminus\{p\}.}
\tag{2.2}
$$
这也是 Zywina 的 Remark 2.4；以上已完整展开由 Lemma 2.3 到该 remark 的推导。

## 3. 为什么本情形中无需从 $S(j)$ 删去 $p$

R2 给出 $v_p(j)\ge0$。R15 §6 的第一部分证明：在非分裂正规化子像下，$E$ 在 $p$ 必须潜在超奇异。该论证不要求 $p\equiv1\pmod3$，它只使用惯性像在 $C$ 中且含一个非标量元素；若潜在普通，约化到特殊纤维的 $p$ 挠点核会给出 Galois 稳定直线，产生矛盾。

若 $v_p(j-1728)>0$，取得好约化后的特殊纤维具有 $j=1728$。但 $p\equiv1\pmod4$ 时，$j=1728$ 曲线是普通的。具体地，在代数闭剩余域中写成
$$
y^2=x^3+Ax,\qquad A\ne0.
$$
其 Hasse 不变量为 $(x^3+Ax)^{(p-1)/2}$ 的 $x^{p-1}$ 系数，即
$$
\binom{(p-1)/2}{(p-1)/4}A^{(p-1)/4}\ne0\pmod p.
$$
所以 $v_p(j-1728)>0$ 不可能。结合 $p$ 处整性，得到
$$
v_p(j-1728)=0.
\tag{3.1}
$$
这说明 $p\notin S(j)$。

R2 还说每个分母素数 $q\mid b$ 满足 $q\equiv\pm1\pmod p$，故 $2\nmid b$、$p\nmid b$；由 (3.1) 又得 $p\nmid n$。

## 4. 从精确分歧支集恢复二次域

R5 已证明商域虚二次，因此存在唯一的正无平方因子整数 $D$，使
$$
K=\mathbb Q(\sqrt{-D}).
$$
对于任意奇素数 $q$，因为 $\gcd(n,b)=1$，有
$$
v_q(j-1728)>0\text{ 且为奇数}
\iff v_q(n)>0\text{ 且为奇数}.
$$
由 (2.2)、(3.1)，$D$ 的奇素因子恰好是右侧的那些 $q$，所以 $D=2^e m$，其中 $e\in\{0,1\}$。

仍需确定 $e$；仅知道哪些奇素数分歧，不能跳过 $2$ 处。

R15 §4 证明，当 $p\equiv1\pmod4$ 时，如果 $D$ 奇，则 $D\equiv3\pmod4$。因此 $D$ 奇时基本判别式为 $-D$，$2$ 不分歧。$D$ 偶时，基本判别式为 $-4D$，其 $2$-赋值为 $3$，$2$ 分歧。所以在当前假设下，
$$
2\text{ 在 }K\text{ 中分歧}\iff e=1.
$$
再由 (2.2) 和 (2.1)，左侧恰好等价于 $v_2(j)\in\{3,6,9\}$。于是 $e=\delta$，证明 (1.3)。$\delta=0$ 时 $m\equiv3\pmod4$ 也同时得证。

这里使用 R15 消除了基本判别式形如 $-4m$、$m$ 为奇数的另一种 $2$ 处分歧可能；若漏掉这一步，(1.3) 的 $2$ 次幂就不能从分歧支集唯一推出。

## 5. 任意 $p>37$ 下的 $2,3$ 进单位测试

以下部分不再要求 $p\equiv1\pmod4$；只设 $p>37$ 为异常素数。令 $K=\mathbb Q(\sqrt{-D})$ 为对应商域，$D>0$ 无平方因子。

**命题。**

1. 若 $v_2(j)=0$，则
   $$
   2\text{ 在 }K\text{ 中分裂},\qquad
   D\equiv7\pmod8,\qquad
   \left(\frac{-7}{p}\right)=-1.
   \tag{5.1}
   $$

2. 若 $v_3(j)=0$，则 $3$ 在 $K$ 中分裂、$D\equiv2\pmod3$。进一步：
   $$
   \begin{aligned}
   j\equiv1\pmod3&\Longrightarrow
   \left(\frac{-11}{p}\right)=-1,\\
   j\equiv2\pmod3&\Longrightarrow
   \left(\frac{-2}{p}\right)=-1.
   \end{aligned}
   \tag{5.2}
   $$

这些断言允许原来的 $E$ 在 $2$ 或 $3$ 坏约化；证明会显式选取同 $j$ 的好约化二次扭曲，不把 $j$ 为单位直接等同于原曲线好约化。

## 6. 显式局部模型与逐项证明

考虑全局有理模型
$$
F_j:\quad
y^2+xy=x^3-\frac{36}{j-1728}x-\frac1{j-1728}.
\tag{6.1}
$$
直接按 Weierstrass 不变量公式计算得
$$
c_4(F_j)=\frac j{j-1728},\qquad
c_6(F_j)=-\frac j{j-1728},\qquad
\Delta(F_j)=\frac{j^2}{(j-1728)^3}.
\tag{6.2}
$$
所以 $j(F_j)=j$。因为 $E$ 无 CM，$j\notin\{0,1728\}$，于是 $E$ 与 $F_j$ 在 $\mathbb Q$ 上相差一个二次扭曲。该扭曲在模 $p$ 表示上只乘以 $\pm I$；因此 $F_j[p]$ 的像仍在同一个 $N$ 中，其商特征仍为 $\varepsilon$。

若 $v_2(j)=0$，则 $j$ 和 $j-1728$ 均为 $2$ 进单位。(6.1) 在 $\mathbb Z_2$ 上整，(6.2) 的判别式为单位，故是好约化模型。模 $2$ 后为
$$
y^2+xy=x^3+1.
$$
$x=0$ 时有一个 $y$，$x=1$ 时有两个 $y$，再加无穷点，共四点。因此
$$
a_2(F_j)=2+1-4=-1.
$$
其模 $p$ Frobenius 迹非零，所以不在 $N\setminus C$ 中，故 $\varepsilon(2)=1$。这给出 $2$ 在 $K$ 中分裂。二次域的 $2$ 分裂判据随后给 $D\equiv7\pmod8$。

这个 Frobenius 的特征多项式为 $T^2+T+2$，判别式为 $-7$。由于 $p>37$，判别式非零；而非标量 $C$ 元素的特征多项式在 $\mathbb F_p$ 上不可约，所以 $(-7/p)=-1$，证明 (5.1)。

同理，若 $v_3(j)=0$，(6.1) 在 $3$ 处也是好约化模型。其约化与点数如下：

| $j\bmod3$ | 约化方程 | $x=0,1,2$ 时的 $y$ 个数 | $\#F_j(\mathbb F_3)$ | $a_3(F_j)$ |
|---|---|---|---|---|
| $1$ | $y^2+xy=x^3+2$ | $0,2,0$ | $3$ | $1$ |
| $2$ | $y^2+xy=x^3+1$ | $2,1,2$ | $6$ | $-2$ |

两种迹都非零模 $p$，所以 $\varepsilon(3)=1$，即 $3$ 在 $K$ 中分裂。因此 $D\equiv2\pmod3$。

两种 Frobenius 多项式的判别式分别为
$$
1-4\cdot3=-11,\qquad
(-2)^2-4\cdot3=-8.
$$
它们非零模 $p$，必须为非平方。$(-8/p)=(-2/p)$，从而得到 (5.2)。

## 7. 与精确公式合并得到的直接排除

回到 $p\equiv1\pmod4$，按第 1 节从 $j$ 算出 $\delta,m$。

- 若 $\delta=0$ 但 $m\equiv1\pmod4$，则没有任何这样的异常素数。
- 若 $\delta=1$，则 R15 给出：$m\equiv3\pmod4$ 时只能有 $p\equiv1\pmod8$；$m\equiv1\pmod4$ 时只能有 $p\equiv5\pmod8$。
- 若 $v_2(j)=0$，则进一步必须 $m\equiv7\pmod8$。因为此时 $\nu=0$，也等价于 $|n|\equiv7\pmod8$；这里应保留 $n=a-1728b$ 的符号，不能在 $0<j<1728$ 时把 $|n|\bmod8$ 擅自换成 $a\bmod8$。
- 若 $v_3(j)=0$，则必须 $2^\delta m\equiv2\pmod3$，并满足 (5.2) 的素数剩余类限制。

这些条件可以直接用于精确的异常素数筛。它们仍然随 $j$ 变化，并且不排除全部 $j$，所以没有完成课题 README 的主要目标。

## 8. 与判别式平方类的区别

由 $j-1728=c_6^2/\Delta$，可以把 $j-1728$ 的平方类与 $\Delta$ 联系起来。但若有乘法约化素数 $q$，$v_q(\Delta)$ 可以为奇数，而 R2 保证 $\varepsilon$ 在 $q$ 不分歧。因此不能直接断言 $K=\mathbb Q(\sqrt{\pm\Delta})$。

正确公式 (1.3) 先使用 $j-1728$ 的**分子**，剔除了分母处的负赋值；再单独按 $v_2(j)$ 确定 $2$ 因子；最后由虚二次性确定负号。三个步骤均必要。

## 9. 外部输入

- Zywina (2022)，§1.1、Lemma 2.3、Remark 2.4，已在第 2 节准确陈述。
- R2 的分母与潜在乘法约化判据；R5 的虚二次性及 $p$ 惰性；R15 的奇分歧素数互反条件及潜在普通约化排除。
- Weierstrass 不变量、Hasse 不变量、二次域分裂判据属于标准输入；实际所需模型、系数、点数和二次剩余计算均已在上文写出。
