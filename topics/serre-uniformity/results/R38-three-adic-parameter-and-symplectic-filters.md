# R38：可变四次 CM 参数的三进筛与第三处辛相容

日期：2026-11-12。状态：**已证明的必要条件；中间进展**。

沿用 R24、R29、R31 的实际同余：
$$
E_0[p]\simeq A_d[p],\qquad A_d:y^2=x^3-dx,
\qquad p>37,\quad p\equiv7\pmod{12},
$$
$d$ 为有符号平方自由整数，且
$$
j(E_0)=\frac{A^3}{B^p},\qquad
n=A^3-1728B^p=\epsilon2^\alpha dZ^2,
\qquad M=\epsilon2^\alpha B.
$$
这里 $B>0$、$(B,6dp)=1$、$3\mid A$，$\epsilon=\pm1$、$\alpha\in\{0,1\}$。设
$$
k=v_3(A),\quad \nu=v_3(n),\quad
A_0=A/3^k,\quad n_0=n/3^\nu,
\quad \eta=\left(\frac{n_0}{3}\right)\in\{\pm1\}.
$$
非 CM 假设保证 $c_4c_6n\ne0$，所以这些赋值有限。

## 1. 结论：分母模 $9$ 的三个分支

所有实际异常数据必须满足下表。

| $B\pmod9$ | $k=v_3(A)$ | $\nu=v_3(n)$ 与 $d$ 的条件 |
|---|---|---|
| $\pm1$ | $k=1$ | $3\nmid d$ 时 $\nu$ 为偶数且 $\nu\ge6$；$3\mid d$ 时 $\nu$ 为奇数且 $\nu\ge7$ |
| $\pm2$ | $k\ge2$ | 必有 $3\mid d$、$\nu=3$ |
| $\pm4$ | $k=1$ | 必有 $3\mid d$、$\nu=3$ |

此外，在 $3\nmid d$、$\nu=6$ 的最浅好约化分支，还必须有
$$
\boxed{\eta B\equiv-1\pmod9.}
\tag{38.1}
$$

特别地，$\nu=4,5$ 均不可能；若 $B=1$，必有 $k=1$ 和 $\nu\ge6$。这些比 R24 中单独记录的 $3\mid A$、$\nu\ge3$ 及奇偶性更强。

若 $3\mid d$，则 $E_0$ 的极小判别式赋值 $\delta_3$ 为 $3$ 或 $9$。全局同一个辛符号又要求
$$
\boxed{
\begin{aligned}
&p\equiv7\pmod{24} &&\Longrightarrow&&\delta_3=3,\\
&p\equiv19\pmod{24} &&\Longrightarrow&&
(-1)^{(\delta_3-3)/6}=\left(\frac3B\right).
\end{aligned}}
\tag{38.2}
$$
右端为正奇整数 $B$ 上的 Jacobi 符号：当 $B\equiv\pm1\pmod{12}$ 时为 $+1$，当 $B\equiv\pm5\pmod{12}$ 时为 $-1$。所以第二行明确选择 $\delta_3=3$ 或 $9$。

式 (38.2) 约束的是 R24 已归一化的曲线 $E_0$，并不单独排除某个 $B\pmod{12}$ 类；不能将对二次扭曲的选择直接算成对 $j$ 的排除。下面给出全部证明及此限制的准确含义。

## 2. 一个只依赖 $j$ 的判别式单位恒等式

记 $D_3$ 为 $E_0$ 的极小判别式去掉全部 $3$ 幂后的单位。关键恒等式为
$$
\boxed{D_3\equiv\eta B\pmod9.}
\tag{38.3}
$$

取 R20 使用的同 $j$ 模型
$$
F_j:y^2+xy=x^3-\frac{36}{j-1728}x-\frac1{j-1728}.
$$
直接计算给
$$
c_4(F_j)=\frac{j}{j-1728},\qquad
c_6(F_j)=-\frac{j}{j-1728},\qquad
\Delta(F_j)=\frac{j^2}{(j-1728)^3}
=\frac{A^6B^p}{n^3}.
$$
因为 $j\ne0,1728$，任意同 $j$ 的 $\mathbb Q_3$ 曲线均为 $F_j$ 的二次扭曲。二次扭曲使判别式乘以六次幂，模型缩放使其乘以十二次幂；去除 $3$ 的赋值后，单位部分仍只乘以单位的六次幂。所有 $\mathbb Z_3^\times$ 单位的六次幂模 $9$ 均为 $1$，故
$$
D_3\equiv\frac{A_0^6B^p}{n_0^3}\pmod9.
$$
又因为 $p\equiv1\pmod6$，$B^p\equiv B\pmod9$；$A_0^6\equiv1$；而 $n_0^3\equiv\eta\pmod9$。这便证明 (38.3)。证明不要求 $F_j$ 自身为整模型或极小模型。

由参数方程也可直接读出
$$
\eta=\left(\frac{\epsilon2^\alpha d/3^{v_3(d)}}3\right),
\tag{38.4}
$$
因为去除 $3$ 幂后的 $Z$ 单位以平方出现。因此 (38.3) 是可由整数参数计算的条件。

## 3. $3\nmid d$：好超奇异约化与最浅分支的迹

R24 已证明此时 $E_0$ 在 $3$ 好约化。$3$ 在 $\mathbb Q(i)$ 惰性，所以 $A_d$ 在 $3$ 的 Frobenius 迹为 $0$。实际模 $p$ 同余给
$$
a_3(E_0)\equiv0\pmod p.
$$
Hasse 界 $|a_3(E_0)|\le2\sqrt3$ 与 $p>37$ 将同余提升为整数等式 $a_3(E_0)=0$。因此约化超奇异。

取在 $\mathbb Z_3$ 上的好极小模型。因为 $2$ 可逆，完成平方后可写成
$$
y^2=x^3+a_2x^2+a_4x+a_6.
$$
超奇异条件 $j\equiv0\pmod3$ 使 $a_2\equiv0\pmod3$；好约化使 $a_4$ 为单位。具体地，
$$
c_4=16(a_2^2-3a_4),\qquad
\Delta\equiv-64a_4^3\not\equiv0\pmod3.
$$
故 $v_3(c_4)=1$。再作整平移 $x\mapsto x-a_2/3$，得到短的好极小模型
$$
y^2=x^3+ax+b,\qquad a\in\mathbb Z_3^\times,\quad b\in\mathbb Z_3.
$$
于是
$$
c_4=-48a,\qquad c_6=-864b,
\qquad v_3(c_4)=1,\quad v_3(c_6)=3+v_3(b)\ge3.
$$
由于 $v_3(\Delta)=0$，恒等式
$$
v_3(j)=3v_3(c_4)-v_3(\Delta)=3k,
\qquad
v_3(j-1728)=2v_3(c_6)-v_3(\Delta)=\nu
$$
给
$$
k=1,\qquad \nu=6+2v_3(b)\ge6.
\tag{38.5}
$$
并且
$$
D_3\equiv-64a^3\equiv\pm1\pmod9.
$$
结合 (38.3)，必有 $B\equiv\pm1\pmod9$。

现在设 $\nu=6$，所以 $b$ 也是单位。直接在 $\mathbb F_3$ 上数点：

- 若 $a\equiv1\pmod3$，则 $x^3+ax=2x$ 遍历全部三个元素，故对任意 $b$ 都有 $a_3=0$。
- 若 $a\equiv-1\pmod3$，则 $x^3+ax=0$ 对全部 $x$ 成立；当 $b\equiv1$ 或 $-1$ 时，分别给 $a_3=-3$ 或 $3$。

实际必须 $a_3=0$，故最浅分支只能有 $a\equiv1\pmod3$，从而 $D_3\equiv-1\pmod9$。利用 (38.3) 得到 (38.1)。若 $\nu\ge8$，则 $b\equiv0\pmod3$；两个 $a$ 单位类都给迹 $0$，这里不应再加同样的符号限制。

## 4. $3\mid d$：不能省略的温和 $e=4$ 三行

R24 证明此时 $E_0$ 在 $3$ 温和潜在好约化，惯性阶恰为 $4$。完整使用 Freitas–Kraus 作者 v5 的 Proposition 6、Table 5 中 $B_{4,i},B_{4,ii},B_{4,iii}$ 三行。令
$$
s=v_3(c_4),\quad t=v_3(c_6),\quad\delta_3=v_3(\Delta).
$$
全部可能为：

| 原文类型 | $(s,t,\delta_3)$ | 额外单位条件 | 得到的 $(k,\nu)$ |
|---|---|---|---|
| $B_{4,i}$ | $(2,t\ge5,3)$ 或 $(4,t\ge8,9)$ | 无 | $k=1$，$\nu$ 奇且至少 $7$ |
| $B_{4,ii}$ | $(s\ge2,3,3)$ | $D_3\equiv2,4\pmod9$ | $k=s-1\ge1$，$\nu=3$ |
| $B_{4,iii}$ | $(s\ge4,6,9)$ | $D_3\equiv2,4\pmod9$ | $k=s-3\ge1$，$\nu=3$ |

最后一列只是代入 $3k=3s-\delta_3$、$\nu=2t-\delta_3$。这既证明 $\delta_3\in\{3,9\}$，也说明 $\nu=5$ 不在任何温和 $e=4$ 行中。将 $q\ge5$ 的简化表直接照搬到 $q=3$，会遗漏后两行。

第一行有 $\nu\ge7$。写 $A=3A_0$，则
$$
n=27(A_0^3-64B^p).
$$
模 $9$ 得 $A_0^3\equiv B\pmod9$，所以 $B\equiv\pm1\pmod9$。

在后两行中 $\nu=3$，于是
$$
n_0=3^{3k-3}A_0^3-64B^p,
\qquad D_3\equiv\eta B\in\{2,4\}\pmod9.
\tag{38.6}
$$

若 $k=1$，$n_0$ 是单位迫使 $A_0\not\equiv B\pmod3$，故 $A_0\equiv-B\pmod3$，进而 $\eta=(B/3)$。因此 $\eta B\equiv1\pmod3$，(38.6) 只能取 $4$。逐一看六个单位类，等价于
$$
B\equiv4,5\pmod9.
\tag{38.7}
$$

若 $k\ge2$，则 $\eta=-(B/3)$。因此 $\eta B\equiv-1\pmod3$，(38.6) 只能取 $2$，等价于
$$
B\equiv2,7\pmod9.
\tag{38.8}
$$

将 (38.5)、第一行及 (38.7)、(38.8) 合在一起，六个 $B$ 单位类恰好分成第 1 节的三个分支。没有把必要条件误写成整个全局问题的充分条件。

## 5. $3$ 处的辛符号化为 $B$ 的一个二次特征

仍设 $3\mid d$。令
$$
r_3=(\delta_3-3)/6\in\{0,1\}.
$$
R29 的温和四阶公式与 R31 的判别式平方类给
$$
\kappa=\left(\frac3p\right)^{r_3}
\left(\frac2p\right)^{t_3},
\qquad (-1)^{t_3}=\left(\frac M3\right).
\tag{38.9}
$$
因为 $p\equiv7\pmod{12}$，总有 $(3/p)=-1$。

若 $p\equiv7\pmod{24}$，则 $(2/p)=1$。R29 在 $2$ 处已经给出同一个全局符号 $\kappa=1$。代入 (38.9) 得 $r_3=0$，故 $\delta_3=3$。

若 $p\equiv19\pmod{24}$，则 $(2/p)=-1$，而 R31 的完整 $p$ 处公式给 $\kappa=(M/p)$。利用 R24 的分母条件，也就是 R31 的 $(B/p)=\chi_{-4}(B)$，有
$$
\kappa=\epsilon(-1)^\alpha\chi_{-4}(B),
\qquad
\left(\frac M3\right)=\epsilon(-1)^\alpha\left(\frac B3\right).
$$
由 (38.9)，约去共同因子后得到
$$
(-1)^{r_3}=\chi_{-4}(B)\left(\frac B3\right)
=\left(\frac3B\right),
$$
最后一步是二次互反律。于是 (38.2) 全部证明。此式不需要 $p\mid n$、$p\mid d$ 或 $B$ 无平方因子。

## 6. 与完整惯性核的区别和不可过度解释之处

在 $3$ 处，阶 $4$ 的温和惯性核已经是唯一可能的核：最大非分歧扩张上的温和惯性为 procyclic 群，其阶 $4$ 商的核唯一。也可用 Freitas–Kraus Theorem 17(1)：此处 Frobenius 将阶四惯性生成元取逆，整个局部像非交换，故共同好约化域可取 $\mathbb Q_3(3^{1/4})$。

因此 (38.2) 不由“$3$ 处完整惯性核相同”本身给出；它使用 Frobenius 作用与全局同一个 Weil 配对符号。具体地，对任何当前温和四阶局部曲线作二次扭曲 $3$，$\delta_3=3,9$ 互换；$j$、(38.3) 的单位以及惯性核都不变。故不能从这些不变数据独自选定 $r_3$。

另一方面，(38.2) 的两种 $B\pmod{12}$ 值均有一个允许的 $\delta_3$，所以此式本身也没有排除这些分母类。它是 R24 归一化曲线的约化型约束，不是一个新的统一高度上界。完整模 $9$ 参数筛和 (38.1) 则直接删除此前显式整数条件中的部分三进分支。

## 7. 一个显示参数筛有效的整数样例

取任意这里允许的 $p$，并考虑整数数据
$$
A=108,\quad B=1,\quad d=546=2\cdot3\cdot7\cdot13,
\quad Z=48,\quad\epsilon=1,\quad\alpha=0.
$$
直接验证
$$
108^3-1728=1257984=546\cdot48^2.
$$
这些数满足 R24 已显式列出的基本参数方程、互素性与支集限制；还满足 R36 的偶 $d$ 分支：$v_2(A)=2$、$v_2(n)=9$，取 $\delta_2=9$ 时 $\chi_{-8}(A/4)=\chi_{-8}(27)=1$。

但它们有 $B\equiv1\pmod9$、$v_3(A)=3$、$v_3(n)=3$，违反本结果的第一行。为直接看见遗漏的局部信息，可取同 $j$ 的实际曲线
$$
E:y^2=x^3-4914x+132496.
$$
其不变量为
$$
c_4=235872,\quad c_6=-114476544,\quad
\Delta=10417365504=64\cdot546^3,\quad j=108^3.
$$
在 $2$ 处为 $(5,9,9)$，单位 $\widetilde c_4\equiv3\pmod8$，满足 R36 列出的二进数值筛；在 $3$ 处却为 $(4,3,3)$，且 $D_3\equiv8\pmod9$，不在第 4 节任何温和 $e=4$ 行中。因此它不可能满足本题要求的全局同余。

这只是说明将完整局部类型翻译为整数参数仍能删除真实遗漏的分支；它没有满足 R24 原先的完整 Galois 同构假设，也不是主问题的反例。

## 8. 来源和剩余缺口

外部的精确分类与辛判据来自 N. Freitas、A. Kraus, *On the symplectic type of isomorphisms of the p-torsion of elliptic curves*, Memoirs AMS **277** (2022), no. 1361，[出版页](https://doi.org/10.1090/memo/1361)、[作者 v5](https://arxiv.org/pdf/1607.01218v5)。这里使用**作者 v5 的编号**：Theorem 5（允许 $q=3$ 的温和四阶辛判据），Proposition 6、Table 5 的 $B_{4,i},B_{4,ii},B_{4,iii}$，以及 Theorem 17(1)。正式排印版编号可能不同。

判别式单位恒等式、好约化模型、模 $3$ 点数、模 $9$ 分流和二次互反简化均已在本文直接计算。结果仍没有控制 $|d|$、$B$ 或曲线高度，也没有证明剩余整数分支对充分大的 $p$ 为空；Serre 统一性主问题仍未解决。
