# 三层 Cartier 数据不决定原字符积分的临界第三位

**可信度：已证明的方法边界。** 日期：2026-11-12。本文针对字符有理核
$$
K_p(X)=\frac{U_p(X)}{D_p(X)}
$$
检验一个具体的固定维数化方案：保留前三个 $p$-进层的 Cartier 像。它们确实落在一个极小的空间中，但丢掉的 exact 部分能够改变模 $p^4$ 的目标。本文不是对原始椭圆单位或真实 $\widetilde\chi$ 分子的反例。

## 1. 前三个层的 Cartier 像都只有一个标量

由前篇，
$$
D_p\in1+p\mathbb Z_p[X^4],\quad\deg D_p=p-1,
$$
$$
U_p\in1+p\mathbb Z_p[X^4],\quad\deg U_p\le p-5.
$$
记 $d=(D_p-1)/p$、$u=(U_p-1)/p$。系数意义下
$$
K_p\equiv
1+p(u-d)+p^2(d^2-ud)+p^3(ud^2-d^3)\pmod{p^4}.
\tag{1}
$$
因而可以逐系数选取 $p$-进数字，写为
$$
K_p\equiv1+pK_1+p^2K_2+p^3K_3\pmod{p^4},
$$
其中每个 $\overline K_j\in\mathbb F_p[X^4]$，且
$$
\deg\overline K_j\le j(p-1)\qquad(1\le j\le3).
\tag{2}
$$
取系数的 Teichmüller 数字或通常整数数字均可；以下在同一数字规范下比较。

在 $\mathbb F_p(X)$ 上，Cartier 算子作用于多项式微分的公式为
$$
\mathcal C\left(\sum_n a_nX^n\,dX\right)
=\sum_{m\ge0}a_{(m+1)p-1}X^m\,dX.
\tag{3}
$$
因为 $p\equiv1\pmod4$、$\overline K_j$ 只含四倍指数，且 (2) 的次数不到 $4p-1$，被选中的指数只能是 $p-1$。因此
$$
\boxed{\quad
\mathcal C(\overline K_j\,dX)=\kappa_j\,dX,
\qquad
\kappa_j=[X^{p-1}]\overline K_j,\qquad
\mathcal C^2(\overline K_j\,dX)=0.
\quad}
\tag{4}
$$
所以这三个层的 Cartier 像确实由三个 $\mathbb F_p$ 标量描述。

第一层甚至完全不见 $U_p$ 的任何非恒定系数：
$$
\kappa_1=-\frac{[X^{p-1}]D_p}{p}\pmod p.
\tag{5}
$$
写 $X\circ[\pi]=N_p/D_p$。在 $O$ 处 $X=-1/t$，而 $[\pi](t)=\pi t+\cdots$，所以
$$
[X^{p-1}]D_p=\pi[X^p]N_p.
$$
又因 $N_p\equiv X^p\pmod p$，
$$
\boxed{\quad \kappa_1=-\pi/p=-\bar\pi^{-1}\pmod p.\quad}
\tag{6}
$$
这就是一个固定一维 Frobenius 标量，却没有包含字符分子的自由部分。

## 2. Cartier 所去掉的 exact 部分

每个 $\overline K_j$ 有唯一分解
$$
\overline K_j(X)\,dX
=dF_j(X)+\kappa_jX^{p-1}\,dX,
\tag{7}
$$
其中 $\deg F_j\le j(p-1)+1$、$F_j(0)=0$、$[X^p]F_j=0$，且 $F_j$ 只含指数 $1\bmod4$。

证明是逐项积分。除 $X^{p-1}$ 外，所有出现的 $X^n$ 都满足 $p\nmid n+1$，故可除以 $n+1$。次数界和模四条件排除了 $2p-1,3p-1$ 等其他导数核位置；排除 $X^p$ 的原函数系数给唯一性。

这里的 $F_j$ 次数可达 $j(p-1)+1$。Cartier 只记录 $\kappa_j$，把 $dF_j$ 全部杀掉。然而原目标是对固定 $\alpha$ 求原函数值后取迹，并不只取微分的 Cartier 像：
$$
\mathcal Q_p=2\operatorname{Tr}_{M/K}\int_0^\alpha K_p(X)\,dX.
\tag{8}
$$
所以 (7) 中的 exact 部分不能直接舍弃。

## 3. 一个改变临界第三位但保留全部三层 Cartier 数据的扰动

固定任意 $a\in\mathbb Z_p$，定义
$$
U_p^{(a)}(X)=U_p(X)+p^3aX^4,\qquad
K_p^{(a)}=\frac{U_p^{(a)}}{D_p}.
\tag{9}
$$
这个扰动保留以下所有已经使用的粗条件：

- $U_p^{(a)}(0)=1$，$U_p^{(a)}\equiv1\pmod p$；
- $U_p^{(a)}\in\mathbb Z_p[X^4]$，$\deg U_p^{(a)}\le p-5$；
- 分母 $D_p$、普通范数 $D_p(\alpha)$ 以及全部固定单位接口不变；
- 第一个、第二个层不变，第三个层仅增加 $\overline aX^4$；而 $\mathcal C(X^4dX)=0$，故三个 $\kappa_j$ 全不变。

无消去极点这一条件也保留。每个 $D_p$ 的根 $x$ 满足
$v_p(x)=-1/(p-1)$。因 $U_p\equiv1\pmod p$、$\deg U_p\le p-5$，有
$$
U_p(x)\in1+\mathfrak m_{\overline{\mathbb Q}_p}.
$$
新增项的赋值至少为 $3-4/(p-1)>0$，所以
$U_p^{(a)}(x)$ 仍是单位，不可能消去分母的根。

定义扰动后的积分迹
$$
\mathcal Q_p^{(a)}
=2\operatorname{Tr}_{M/K}\int_0^\alpha K_p^{(a)}(X)\,dX.
$$
则
$$
\boxed{\quad
\mathcal Q_p^{(a)}-\mathcal Q_p
\equiv
\frac{2p^3a}{5}\operatorname{Tr}_{M/K}\alpha^5
\pmod{p^4}.
\quad}
\tag{10}
$$

为核对 (10)，需证明
$$
\operatorname{Tr}\int_0^\alpha\frac{X^4}{D_p(X)}\,dX
\equiv\frac{\operatorname{Tr}\alpha^5}{5}\pmod p.
$$
展开 $D_p^{-1}=\sum_{k\ge0}(-pd)^k$。$k=1$ 项积分后的次数至多 $p+4<5p$；模四条件使唯一可能含 $p$ 分母的幂为 $\alpha^p/p$，而
$\operatorname{Tr}\alpha^p\in p\mathbb Z_p$，故整个迹仍在 $p$ 中。$k\ge2$ 时积分次数至多 $k(p-1)+5<p^k$，所以分母最多损失 $k-1$ 位，仍在 $p$ 中。实际下界
$k-\lfloor\log_p(k(p-1)+5)\rfloor\to\infty$ 还证明该积分迹级数收敛。这给 (10)。

## 4. 变化系数不是恒为零的固定数

这里
$$
b_5:=\operatorname{Tr}_{M/K}\alpha^5
$$
是一个固定非零代数数。证明如下。由
$$
\log\Phi(t)=
2\sum_{\substack{n\ge1\\n\ {\rm odd}}}
\frac{\operatorname{Tr}\alpha^n}{n}t^n,
\qquad\operatorname{Tr}\alpha=0,
$$
以及 $\exp_E(z)=z+O(z^5)$，五次项没有来自一次项的贡献，三次项的下一次贡献则到七次。因此
$$
\lambda_5=\delta^5\log\Phi(O)=48b_5.
\tag{11}
$$
R19 的精确特值公式给
$$
\lambda_5=-2\cdot4!\,f^5\Omega_\infty^{-5}
L_{\mathfrak f}(\overline\psi^5,5).
$$
最后这个 Hecke $L$ 值不为零：在 $s=5$，其 Euler 因子的非平凡项绝对值为
$N\mathfrak l^{-5/2}$，Euler 积绝对收敛而且没有零因子。删除有限个 Euler 因子也不改变非零性。故 (11) 的 $b_5\ne0$。

所以除固定有限个素数外，$b_5$ 在目标素位是单位。对这些 $p$，式 (10) 可以通过改变 $a\bmod p$ 任意改变 $\mathcal Q_p$ 的第三个 $p$-进数字，而前三层 Cartier 数据全不变。特别地，若已知 $\mathcal Q_p\in p^3$，这些粗数据不能区分其赋值是三还是至少四。

## 5. 此边界没有替代真实字符约束

真实 $U_p$ 当然并不任意：它的每个留数满足
$$
\operatorname{Res}_{X=-1/\sigma\rho}
K_p(X)\,dX
=\frac{\widetilde\chi(\sigma)^{-1}}{(p-1)\rho_\chi}.
$$
扰动 (9) 一般不保留这些精确的 Teichmüller 留数关系，也不满足原始严格 LT 三对角公式。因此本文没有构造另一个同曲线的椭圆单位，更没有构造对本题目标的算术反例。

它证明的是一个具体结论：**分母、整性、次数、无消去极点，以及前三层 Cartier 像这组有限数据，不足以决定实际模 $p^4$ 的积分迹。** 用它们建立一个固定维数 Frobenius 模型后，若将 exact 部分丢掉，就已丢掉判别临界第三位所需的信息。

仍可能有更强的模型同时保留 Teichmüller 留数及 exact 原函数在固定导子点的迹；本次尚未构造这样的统一有限模型，也没有从 Cartier 数据推出 $\lambda\le3$ 或 $G_p\notin(p,T)^2$ 的无穷性。

## 依赖

- R18、R19：固定域迹、$\alpha$ 的整性及五次矩的特值公式。
- 字符有理核笔记：$U_p,D_p$ 的整性、次数、极点和积分迹。
- 严格 LT 三对角笔记：真实字符分子的额外精确约束。
- 本文的 Cartier 计算、扰动和第三位变化已完整证明。
