# R10：辅助素数 5 处的精确纤维计数与未被有理 CM 点占据的圆盘

**状态：已证明。** 这是有限域群作用与模解释的直接计算，不声称文献创新。它说明 CM 点之间的约化分离不能单独完成二次 Chabauty 的剩余圆盘排除；不提供非 CM 有理点，也不改变主要目标未解决的状态。

日期：2026-11-12。会话：serre-uniformity-astra。

## 1. 结论

令 $p\ge7$ 为素数，$\mathcal X/\mathbb Z_5$ 为 $X_{\rm ns}^+(p)$ 的标准好约化模型。令
$$
n_p=\#\{x\in\mathcal X(\mathbb F_5):j(x)=0\}.
$$
则
$$
n_p=
\begin{cases}
(p-1)/2,&\left(\frac{-5}{p}\right)=1,\\
(p+3)/2,&\left(\frac{-5}{p}\right)=-1.
\end{cases}\tag{1.1}
$$

每个这样的点对应 $X_{\rm ns}^+(p)(\mathbb Q_5)$ 中一个非空、与其他点不相交的残数圆盘。若 $p>163$，令
$$
\mathcal D_5=\{-3,-7,-8,-12,-27,-28,-43,-67,-163\},\qquad
m_p=\sum_{\Delta\in\mathcal D_5}\frac{1-\left(\frac{\Delta}{p}\right)}2.
$$
这些圆盘中不含有理 CM 点的数目**精确为** $n_p-m_p$，特别地至少有
$$
n_p-9\ \ge\ \frac{p-19}{2}.\tag{1.2}
$$
这里使用 R9 的有理 CM 点分类与约化单射性。这只是不含**有理 CM 点**，并非说其中没有 $\mathbb Q_5$ 点、没有代数 CM 点或已经没有非 CM 有理点。

## 2. 使用的模解释

在特征不同于 $p$ 的代数闭域中，固定椭圆曲线 $E$，令 $V=E[p]$。$j$ 映射在 $j(E)$ 上的几何纤维由
$$
\operatorname{Aut}(E)\backslash\mathscr C(V)
\tag{2.1}
$$
描述，其中 $\mathscr C(V)$ 是 $\operatorname{End}_{\mathbb F_p}(V)$ 中所有含单位的二次域子代数，自动同构于 $\mathbb F_{p^2}$；自同构群通过共轭作用。

确实，$\mathrm{GL}(V)$ 在这些子代数上传递，单个子代数的稳定子恰为其乘法群的正规化子 $N_{\rm ns}$，所以这是通常 $N_{\rm ns}$-级结构的模解释。以子代数、非分裂 Cartan 子群或无定向 necklace 表示，得到同一个集合。该解释与基域 Galois 作用相容。

我们使用特征零及素于级的标准模曲线理论：在 $5\nmid p$ 时，$\mathcal X$ 有好约化，上述非尖点几何点描述适用于特征 $5$。可参见 Deligne–Rapoport 的模曲线构造及 Rouse–Sutherland–Zureick-Brown (2022), §2.3；专门的非分裂 necklace 描述见 Rebolledo–Wuthrich (2018), §2。

在本结论中只需 $j=0$ 点处的光滑性。它也可从局部变形直接看出：素于 $5$ 的 $p$-级结构在椭圆曲线的变形上 étale 提升，椭圆曲线变形环是一变量形式幂级数环；该点的有效自同构稳定子阶数整除 $3$，与 $5$ 互素。其对形式参数的作用可用平均法线性化，取不变量仍是一变量形式幂级数环。因此这些粗模点在 $\mathbb Z_5$ 上光滑，不受 $5$ 是否整除整个 $N_{\rm ns}$ 阶数的影响。

## 3. 迹零元素固定多少个非分裂 Cartan？

### 引理 10.1

设 $F\in\mathrm{GL}_2(\mathbb F_p)$，$\operatorname{tr}F=0$，$F^2=aI$，$a\ne0$。则 $F$ 共轭作用在 $\mathscr C(\mathbb F_p^2)$ 上的固定点数为
$$
\begin{cases}
(p-1)/2,&a\text{ 为平方},\\
(p+3)/2,&a\text{ 为非平方}.
\end{cases}\tag{3.1}
$$

**证明。** 对任意二次域子代数 $A$，其迹零部分是一条一维直线 $\mathbb F_p X$。Cayley–Hamilton 给出
$$
X^2=-\det(X)I.
$$
它生成二次域当且仅当 $-\det(X)$ 为非平方。反过来，每条满足此条件的迹零直线唯一确定 $A=\mathbb F_p[I,X]$。因此可把 $\mathscr C$ 视作三维迹零矩阵空间中特定的射影直线集合。

$F$ 不可能是标量：标量且迹零会迫使 $F=0$。取基使
$$
F=\begin{pmatrix}0&a\\1&0\end{pmatrix}.
$$
由于 $F^2$ 为标量，共轭 $X\mapsto FXF^{-1}$ 是一个对合。$p$ 为奇数，所以其射影不变直线必须属于 $+1$ 或 $-1$ 特征子空间。

$+1$ 特征子空间是 $\mathbb F_pF$。它给出一个二次域子代数当且仅当 $a$ 非平方，贡献 $\bigl(1-\chi(a)\bigr)/2$，其中 $\chi$ 为二次特征。

$-1$ 特征子空间由反交换关系 $FX=-XF$ 给出，恰为
$$
X=\begin{pmatrix}x&-az\\z&-x\end{pmatrix},
\qquad -\det X=x^2-az^2.
$$
其中 $z=0$ 的射影点使该值为平方，不计。对 $z\ne0$ 可归一化为 $z=1$，于是所求数为
$$
\#\{x\in\mathbb F_p:\chi(x^2-a)=-1\}.
$$
方程 $x^2-a=0$ 有 $1+\chi(a)$ 个解。又有
$$
\sum_{x\in\mathbb F_p}\chi(x^2-a)=-1.
\tag{3.2}
$$
为完整起见，(3.2) 可由计数 $y^2=x^2-a$ 证明：写成 $(x-y)(x+y)=a$，因为 $2a\ne0$，每个 $u=x-y\in\mathbb F_p^\times$ 唯一决定 $x+y=a/u$ 和 $(x,y)$，所以共有 $p-1$ 对。另一方面该数为 $p+\sum_x\chi(x^2-a)$。

由零值数及 (3.2)，非平方值数为 $(p-\chi(a))/2$。两种特征子空间的贡献相加为
$$
\frac{p-\chi(a)}2+\frac{1-\chi(a)}2
=\frac{p+1-2\chi(a)}2,
$$
即 (3.1)。证毕。

## 4. 从级结构到粗模点：不能直接除以 3

取
$$
E_0/\mathbb F_5:\qquad y^2=x^3+1.
$$
在 $x=0,1,2,3,4$ 上分别有 $2,0,2,0,1$ 个仿射点，加无穷远点共 $6$ 个，所以 $a_5(E_0)=0$。记其 Frobenius 在 $E_0[p]$ 上的矩阵为 $F$，则
$$
F^2=-5I.
\tag{4.1}
$$

所有几何 $j=0$ 的椭圆曲线均与 $E_0$ 同构。由于特征为 $5$，其自同构群为 $\mu_6$。标量 $\{\pm1\}$ 对 Cartan 结构作用平凡，故有效自同构群为
$$
A=\operatorname{Aut}(E_0)/\{\pm1\}\simeq C_3.
$$
把 $A$ 的一个生成元记作 $\tau$。自同构所用的三次单位根在 Frobenius 下变为五次幂，即逆元，因此
$$
F\tau F^{-1}=\tau^{-1}
\tag{4.2}
$$
作为 Cartan 集合上的置换成立。

### 引理 10.2

设有限集合 $S$ 上有阶三群 $\langle\tau\rangle$ 与对合 $F$ 的作用，且 $F\tau F^{-1}=\tau^{-1}$。则
$$
\#(S/\langle\tau\rangle)^F=\#S^F.
\tag{4.3}
$$

**证明。** 一个 $F$ 固定的 $\tau$-轨道长度为 $1$ 或 $3$。长度为 $1$ 时，其唯一元素也是 $F$ 固定点。长度为 $3$ 时，取其中 $s$ 并写 $F(s)=\tau^c s$，则
$$
F(\tau^k s)=\tau^{c-k}s.
$$
固定点条件为 $2k=c$ 于 $\mathbb Z/3\mathbb Z$，恰有一个解。非 $F$ 稳定的轨道没有 $F$ 固定元素。故每个固定轨道恰贡献一个固定元素，证毕。

在 $S=\mathscr C(E_0[p])$ 上，(4.1) 说明 $F$ 的共轭作用为对合，(4.2) 给出引理的另一条件。根据模解释，$n_p$ 正是 $(S/A)^F$ 的大小。因此引理 10.2 表明它**等于** $F$ 固定的 Cartan 数，不能将后者机械地除以自同构群阶数。将引理 10.1 应用于 $a=-5$，即得 (1.1)。证毕。

## 5. 残数圆盘与有理 CM 点的数目

$\mathcal X$ 在上述点处光滑且相对维数为一；在每个 $x\in\mathcal X(\mathbb F_5)$ 处可选形式参数，其提升构成一个 $5$-进圆盘。Hensel 提升保证该圆盘非空。不同 $x$ 对应的约化纤维不交。

R9 证明：当 $p>163$ 时，每个类数一 CM 判别式在 $p$ 惰性时恰给一个有理 CM 点，分裂时不给有理点。查看 R9 的十三项 $j$ 值表，其中恰有 $\mathcal D_5$ 中的九项满足 $j\equiv0\pmod5$；余下判别式 $-4,-11,-16,-19$ 的 $j$ 模 $5$ 分别为 $3,2,1,4$。

所以有理 CM 点中恰有 $m_p$ 个约化到所计数的 $j=0$ 纤维。R9 还证明它们在模 $5$ 时两两不同，因此恰占据 $m_p$ 个不同圆盘。其他 $n_p-m_p$ 个圆盘都不含有理 CM 点。由 $m_p\le9$ 和 (1.1) 得到 (1.2)。

例如，$p=167$ 时 $\left(\frac{-5}{167}\right)=1$，因此 $j=0$ 纤维有 $83$ 个 $\mathbb F_5$ 点，至少 $74$ 个相应圆盘不含有理 CM 点。例子只是代入公式；主结论对所有素数 $p>163$ 统一成立。

## 6. 对当前研究的含义

把已知 CM 点在模 $5$ 的位置彼此分开，在这个 $j=0$ 纤维中最多处理九个圆盘。即使每个含 CM 点圆盘都已经有 QC 简单根证书，仍需为其余至少 $(p-19)/2$ 个圆盘给出排除有理点的全局条件。

这里没有断言这些圆盘通过 QC 条件：二次 Chabauty 或 Mordell–Weil 筛完全可能把它们全部排除。结论仅确定必须实际完成的另一步，防止把 CM 分离误作全部有理点分类。

## 7. 来源

- P. Deligne and M. Rapoport, *Les schémas de modules de courbes elliptiques*, Lecture Notes in Mathematics 349 (1973), 143–316，尤其 IV §3 的级结构与商模解释。
- J. Rouse, A. V. Sutherland and D. Zureick-Brown, *$\ell$-adic images of Galois for elliptic curves over $\mathbb Q$ (and an appendix with John Voight)*, Forum of Mathematics, Sigma 10 (2022), e62，§2.3：<https://doi.org/10.1017/fms.2022.38>。
- M. Rebolledo and C. Wuthrich, *A moduli interpretation for the non-split Cartan modular curve*, Glasgow Mathematical Journal 60 (2018), 411–434，§2 与 §3.5（特别是 Lemmas 10–11 的相关对合计数）：<https://doi.org/10.1017/S0017089517000180>；[作者稿](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf)。本文件另给出所用有限域计数的完整矩阵证明。
