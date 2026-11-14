# CM Frobenius 的四层递推：对称性只留下一个积分常数

**可信度：下述有限递推与唯一性已证明；没有证明无穷素数目标。** 日期：2026-11-12。本文使用 [第一层笔记](2026-11-12-cm-frobenius-first-layer.md) 的记号，并把它继续到四个 $p$-进除法层。结果给出实际可执行的计算，而不是只断言存在一个未知同源。

## 1. 固定坐标和结论

仍令
$$
X=y/x,\quad Z=x+17/x,\quad S(X)=X^4+68,
\qquad Z^2=S(X),\quad\omega=dX/Z.
$$
取 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，以及
$$
\pi=\psi_E(\mathfrak p),\quad c=\bar\pi^{-1},
\quad r=(p-1)/4,
\quad Q=\frac{68^{p-1}-1}{p}\in\mathbb Z.
$$
这里 $Q$ 是完整整数，不仅是模 $p$ 的 Fermat quotient。置
$$
Y_p=(1+pQ)^{-1/4}\in1+p\mathbb Z_p,
\qquad d_j=\binom{-1/4}{j}Q^j.
\tag{1}
$$
前四项为
$$
d_1=-Q/4,\quad d_2=5Q^2/32,\quad
d_3=-15Q^3/128,\quad d_4=195Q^4/2048.
\tag{2}
$$
它们在所列素数处均 integral。

**四层结论。** 可通过下文递推构造 $V_{1,p},\ldots,V_{4,p}\in\mathbb Z_p[X]$，满足
$$
X(X^4+68)\mid V_{j,p},\qquad
\deg V_{j,p}\le(j+1)p-j,
\tag{3}
$$
且每个非零项的次数都等于 $1\pmod4$，使得
$$
\boxed{\quad
X\circ[\pi]\equiv
\left(1+\sum_{j=1}^4p^jd_j\right)X^p
+\sum_{j=1}^4p^jV_{j,p}(X)
\pmod{p^5}.
\quad}
\tag{4}
$$
模同余仍解释在四次模型去掉两个无穷远点后的 $p$-进形式完备化中。舍去第四层便给模 $p^4$ 的公式。每一步仅用多项式运算、在 $\mathbb F_p(X)$ 中的一个确定的平方根 Hensel 递推、除以明确的 $p$ 次幂，以及一个确定的积分常数。

选择各步系数的整提升会改变后续的 $V_{j,p}$；式 (4) 的整体截断不变。本文不声称四个单独的 $V_{j,p}$ 不依赖提升选择。

## 2. 为什么极点阶每层只增长 $p-1$

involution $\tau(P)=T-P$ 固定 $X$，其商是以 $X$ 为坐标的 $\mathbb P^1_{\mathbb Z_p}$。$[\pi]T=T$，所以 $[\pi]$ 在此商上诱导一个 degree $p$ 的态射 $\varphi_p$，满足
$$
\varphi_p(X)=X\circ[\pi],\qquad
\overline\varphi_p(X)=X^p,\qquad
\varphi_p(\infty)=\infty.
$$
于是可以取互素整多项式 $N,D$，使
$$
\varphi_p=N/D,\quad
\deg N\le p,\quad\deg D\le p-1,
\quad N\equiv X^p\pmod p,\quad D\equiv1\pmod p.
\tag{5}
$$
说明规范化的存在：degree $p$ 的态射由两条 $\mathcal O(p)$ 的无公共零点截面给出；约化为 Frobenius 后，其齐次坐标为共同单位倍数的 $[X^p:Y^p]$。除去该共同单位，并在 $Y=1$ 的仿射图中写出两多项式即可。无穷远固定使分母的 $X^p$ 系数准确为零，而不仅是模 $p$ 为零。分母常数项为单位，可再规范为 $D(0)=1$。

写 $N=X^p+pN_1$、$D=1+pD_1$。在 $p$-进完备化中展开几何级数，
$$
\varphi_p=X^p+
\sum_{j\ge1}p^j
\left(N_1(-D_1)^{j-1}+X^p(-D_1)^j\right).
\tag{6}
$$
第 $j$ 项的次数至多 $(j+1)p-j$。

因此，只要已经有一个满足正确次数界的近似
$$
A_{k-1}=X^p+\sum_{j<k}p^jP_j(X)
\equiv\varphi_p\pmod{p^k},
$$
残差
$$
\overline E_k=\frac{\varphi_p-A_{k-1}}{p^k}\pmod p
$$
就是次数至多 $(k+1)p-k$ 的多项式。较早各项的系数进位不会破坏这个界，因为相应次数界更小。这里没有把除以 $p$ 后的极点界未经证明地维持不变。

## 3. CM 对称性消去其他导数核方向

原模型的 $[i]$ 为 $(x,y)\mapsto(-x,iy)$，故在四次模型上
$$
[i]:(X,Z)\longmapsto(-iX,-Z).
$$
由于 CM 同源交换，
$$
\varphi_p(-iX)=-i\varphi_p(X).
\tag{7}
$$
因此所有近似均可、且下文将始终选择为仅含次数 $1\pmod4$ 的项。

现在令 $1\le k\le4$。若两个次数至多 $(k+1)p-k$、具有上述对称性的多项式具有相同导数，它们之差必须是 $X^p$ 的倍数：导数为零的单项式是 $X^{mp}$；由于 $p\equiv1\pmod4$，对称性又要求 $m\equiv1\pmod4$。在次数严格小于 $5p$ 的范围内，唯一可能的正整数 $m$ 为 $1$。常数项也被对称性排除。

所以在这四层内，每一步只剩一个未知系数
$$
\kappa X^p.
\tag{8}
$$
到第五层，该论证允许新的 $X^{5p}$ 方向，故不能不加证明地无限推广此唯一性。

## 4. 分支点精确确定全部四个常数

四个分支点满足 $Z=0$、$X=b$、$b^4=-68$，也即 $[2]P=T$。$[\pi]$ 置换这些点，且约化为 Frobenius。因此
$$
\left(\frac{\varphi_p(b)}{b^p}\right)^4
=68^{1-p}=(1+pQ)^{-1},
\qquad\frac{\varphi_p(b)}{b^p}\equiv1\pmod p.
$$
$4$ 是单位，主单位中四次根唯一，所以有精确等式
$$
\boxed{\quad \varphi_p(b)=b^pY_p.\quad}
\tag{9}
$$
这对四个分支点给出同一个比值，不涉及选择某个未定的四次单位根。

如果一个多项式 $I(X)$ 只含次数 $1\pmod4$ 的项，那么
$$
j(I):=I(b)/b^p\in\mathbb Z_p
\tag{10}
$$
与所选四次根 $b$ 无关：每个比值单项式 $b^{n-p}$ 的指数是 $4$ 的倍数，故是 $-68$ 的整数次幂。由于 $68$ 是单位，负次幂也 integral。于是
$$
I(X)-j(I)X^p
$$
在四个分支点都为零，并且被 $X$ 整除。因此它被 $X(X^4+68)$ 整除。

## 5. 每一层的可执行递推

假设已经构造 $P_j=V_{j,p}+d_jX^p$，$j<k$，满足 (3) 及
$$
A_{k-1}=X^p+\sum_{j<k}p^jP_j
\equiv\varphi_p\pmod{p^k}.
$$
下面构造第 $k$ 层，$1\le k\le4$。

### 5.1 求出相应的 $Z$ 比值

在以 $p$ 为均匀化参数、剩余域为 $\mathbb F_p(X)$ 的离散赋值环中，求唯一的平方根
$$
W_{k-1}^2\equiv\frac{A_{k-1}^4+68}{S(X)}\pmod{p^k},
\qquad W_{k-1}\equiv S(X)^{(p-1)/2}\pmod p.
\tag{11}
$$
这里 $S$ 在 $\mathbb F_p(X)$ 中非零，故是该赋值环的单位；Hensel 递推合法。初始平方根确实满足条件，因为
$$
(X^{4p}+68)/S\equiv S^{p-1}\pmod p.
$$
若从 $W^{(j-1)}$ 提升一位，其修正明确为
$$
W^{(j)}=W^{(j-1)}+p^j
\frac{p^{-j}((A_{k-1}^4+68)/S-(W^{(j-1)})^2)}
{2S^{(p-1)/2}}\pmod{p^{j+1}}.
\tag{12}
$$
式 (12) 分子中的除法先在整赋值环里进行，再在剩余域中求值。

实际的 $(Z\circ[\pi])/Z$ 是 (11) 的同一个平方根，所以
$$
W_{k-1}\equiv\frac{Z\circ[\pi]}Z\pmod{p^k}.
\tag{13}
$$

这个实际比值在仿射部分的形式完备化中整。理由是 $Z=0$ 定义四个不分歧的分支截面，$[\pi]$ 置换它们，故整函数 $Z\circ[\pi]$ 被它们的主理想生成元 $Z$ 整除。比值又是 $\tau$-不变函数，因而属于以 $X$ 为变量的整的限制幂级数环。由此，每个在此前整多项式近似之后取得的 $p$-进系数都是多项式，而不会在分支点留下一个隐藏的极点。

### 5.2 计算多项式导数

$[\pi]^*\omega=\pi\omega$ 给出
$$
\varphi_p'(X)=\pi\frac{Z\circ[\pi]}Z=pc\frac{Z\circ[\pi]}Z.
$$
定义
$$
F_k(X)=\frac{pcW_{k-1}-A_{k-1}'(X)}{p^k}\pmod p.
\tag{14}
$$
分子可被 $p^k$ 整除，因为实际的差 $\varphi_p-A_{k-1}$ 可被 $p^k$ 整除，而 (13) 代入后仅带来 $p^{k+1}$ 的误差。

由 §2，$F_k=\overline E_k'$ 实际属于 $\mathbb F_p[X]$，次数至多 $(k+1)p-k-1$；Hensel 计算中临时出现的有理函数分母会在这里消去。由 (7)，它只含次数 $0\pmod4$ 的项。在该次数范围内唯一可能使积分分母被 $p$ 整除的指数是 $p-1$，其系数准确为零，因为 $F_k$ 是一个多项式导数。

写 $F_k=\sum_n f_{k,n}X^n$，并定义
$$
I_k(X)=\sum_{n\ne p-1}\frac{f_{k,n}}{n+1}X^{n+1}
\in\mathbb F_p[X].
\tag{15}
$$
所有实际出现的分母均为单位。根据 §3，$\overline E_k-I_k$ 只可能为 $\kappa_kX^p$。

### 5.3 用分支值固定常数并返回整多项式

取保持相同单项式支撑的任意整提升 $\widetilde I_k\in\mathbb Z_p[X]$，令
$$
V_{k,p}=\widetilde I_k-j(\widetilde I_k)X^p,
\qquad P_k=V_{k,p}+d_kX^p.
\tag{16}
$$
§4 保证 $V_{k,p}$ 满足 (3)。又因此前的每个 $V_{j,p}(b)=0$，在分支点有
$$
\frac{\overline E_k(b)}{b^p}
\equiv\frac{Y_p-1-\sum_{j<k}p^jd_j}{p^k}
\equiv d_k\pmod p.
$$
式 (16) 的 $P_k$ 也有同一分支值，其导数又为 $F_k$。由唯一性 (8)，
$$
P_k\equiv\overline E_k\pmod p.
$$
因此 $A_k=A_{k-1}+p^kP_k$ 满足 $A_k\equiv\varphi_p\pmod{p^{k+1}}$。归纳完成四层构造。

## 6. 第一层的方便整提升与第二层的明确接口

为避免仅把递推停留在抽象描述，可选择一个分支点处准确为零的第一层提升：
$$
V_{1,p}(X)=c\sum_{j=1}^r
\frac{\binom{2r}{r+j}68^{r-j}}{4j}
X^{p-4j}\left(X^{8j}-68^{2j}\right).
\tag{17}
$$
其分母均为单位，且每项被 $X(X^4+68)$ 整除。把第一层笔记中的 $k=r+j$ 与 $k=r-j$ 两项配对，即见 (17) 的约化为那里的 $J_p$。所以 $P_1=V_{1,p}-QX^p/4$ 是合法首层。

令
$$
H=\binom{2r}{r}68^r,\qquad
\mathcal V_p(X)=\sum_{j=1}^{p-1}\frac1p\binom pj
68^{p-j}X^{4j}.
$$
从曲线方程直接比较第一次修正，得到
$$
W_1=S^{(p-1)/2}+pR_1\pmod{p^2},
$$
其中
$$
R_1(X)=
\frac{4X^{3p}\overline P_1(X)-68\overline Q-
\overline{\mathcal V}_p(X)}{2S(X)^{(p+1)/2}}
\in\mathbb F_p[X].
\tag{18}
$$
这里属于多项式环的断言来自 (13) 及同一极点/对称性论证，也可直接由第一层公式验证分子具有所需的 $S$ 次幂因子。

对 (17) 求导，有准确的整系数等式
$$
V_{1,p}'=cS^{(p-1)/2}-cHX^{p-1}
+pV_{1,p}/X.
$$
所以第二层导数 (14) 可直接写为
$$
\boxed{\quad
F_2=cR_1-V_{1,p}/X+
\left(\frac{cH-1}{p}+\frac Q4\right)X^{p-1}
\pmod p.
\quad}
\tag{19}
$$
$cH\equiv1\pmod p$ 已由第一层的点数计算证明，所以这里的除以 $p$ 合法。式 (19) 的 $X^{p-1}$ 系数必须消失；这提供一个准确的 Hasse 系数与 CM unit root 的二阶同余，但不能把它误记成新的 Sha 非零证书。其余系数按 (15)、(16) 积分即得到第二层。

## 7. 固定 torsion trace 和当前限制

在 R18 的 $\alpha=X(P_f)$ 处，CM reciprocity 给 $\varphi_p(\alpha)=\sigma_{\mathfrak p}\alpha$。对 (4) 取 $M/K$ 的 trace，利用 $\operatorname{Tr}\alpha=0$，得到
$$
\boxed{\quad
Y_p\,b_0(p)
\equiv-\sum_{j=1}^4p^j
\operatorname{Tr}_{M/K}V_{j,p}(\alpha)
\pmod{\mathfrak p^5}.
\quad}
\tag{20}
$$
因 $Y_p$ 是单位，式 (20) 给出 $b_0$ 的四层正规化，且第一层退化为上一篇笔记的准确公式。把前三层代入 R17 的四项表达式可逐项计算目标剩余量；无需将形式对数错误地在单位 $\alpha^{-1}$ 处求无限和。

这一算法没有引入未知的代数点或积分常数；输入为 $p$、对应的 CM 生成元 $\pi$、固定整数 $68$ 和固定 $\alpha$。但各多项式的次数是 $O(p)$，其系数包含长度随 $p$ 增长的二项式和及积分运算。因而这里没有得到一个固定有限矩阵的 Frobenius 判定，也没有证明 (20) 与 R17 后三层组合后在无穷多个 $p$ 上不消失。尤其固定整数 $68$ 的 Fermat quotient 已可全部追踪，却不能因此忽略这些迹之间的相消。

本文保留原始 $\Phi$ 和原始 torsion orbit，没有用会人为增加中心零阶的辅助函数取代它。与 R20 的关系是提供具体的低层计算输入；不是从范数分布或 $\mu=0$ 自动推导所需的小深度。
