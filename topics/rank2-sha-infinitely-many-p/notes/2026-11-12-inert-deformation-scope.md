# “几乎所有 inert 素数”的变形像定理为何还不是 Sha 判据

日期：2026-11-12。会话：Astra-rank2-Sha / literature_scope。

**状态：范围核查完成；本课题未完成。** 检索超奇异路线时发现一个确实含“除有限多个外的所有 inert $p$”的经典定理。本笔记核对它的对象，并完整证明首阶变形类与本题 Selmer 类属于不同系数表示。没有否定该定理，也没有否定本题的预期答案。

## 1. 定理原文及假设

Álvaro Lozano-Robledo，*Bernoulli–Hurwitz numbers, Wieferich primes and Galois representations*，Journal of Number Theory 130 (2010), 539–558。

- [作者文本（2009-04-08，27 页）](https://production.wordpress.uconn.edu/alozano/wp-content/uploads/sites/490/2014/01/lozano_robledo_BH.pdf)
- [发表版本 DOI](https://doi.org/10.1016/j.jnt.2009.10.013)

已独立核对作者文本 Introduction、Theorems 1.1–1.3、Lemma 2.1 及 §2 的变形模说明；没有逐行复核其后全部椭圆单位计算。

其固定假设为：$K$ 是类数 $1$ 的虚二次域，$D_K\ne-3,-4$；$A/\mathbb Q$ 的 CM 环为 $\mathcal O_K$；$p\ge7$ 不分歧。Rohrlich 构造
$$
\rho_A:G_{K(\mu_{p^\infty})}\longrightarrow\operatorname{SL}_2(\mathbb Z_p[[X]])
$$
在 $X=0$ 特化为 Tate 模表示 $\bar\rho_A$。Theorem 1.2 证明：若 $p$ inert 且 $BH_2^0$ 是 $p$-adic 单位，则变形的像为 Cartan 群在 $X=0$ 投影下的全逆像；特别地，除有限多个外的所有 inert $p$ 都成立。

这里 $BH_2^0$ 取自该 CM 域的最小导子曲线 $A_0$，是固定的权重 $2$ Bernoulli–Hurwitz 数，而不是 $A$ 的 cyclotomic $p$-adic $L$ 函数在 $T=0$ 的二次 Taylor 系数。

**直接的适用性限制：** $E_{17}$ 的 CM 域为 $\mathbb Q(i)$，判别式 $-4$，不在原定理假设内。即使换用其他 CM 域中已知的秩 $2$ 曲线，下一节的系数表示区别仍需解决。

## 2. 首阶变形类是 adjoint 类

### 已证明引理

令 $k$ 为特征不为 $2$ 的域，$\rho_0:G\to\operatorname{SL}_2(k)$ 为表示。若
$$
\rho:G\to\operatorname{SL}_2(k[\epsilon]/(\epsilon^2))
$$
是其一阶变形，写
$$
\rho(g)=(1+\epsilon c(g))\rho_0(g).
$$
则 $c$ 是取值于 $\operatorname{ad}^0(\rho_0)=\mathfrak{sl}_2(k)$ 的 $1$-cocycle，其中 $G$ 以共轭作用。

**证明。** 由 $\det\rho(g)=\det\rho_0(g)=1$ 及
$$
\det(1+\epsilon c(g))=1+\epsilon\operatorname{tr}c(g)
$$
可知 $\operatorname{tr}c(g)=0$。另一方面，比较 $\rho(gh)=\rho(g)\rho(h)$ 的 $\epsilon$ 系数，得到
$$
c(gh)=c(g)+\rho_0(g)c(h)\rho_0(g)^{-1},
$$
即 cocycle 等式。变换与恒等矩阵同余的基只增加相应 coboundary。证毕。

因此，“该变形的第一层足够大”直接约束的是 adjoint 系数类，不是
$$
H^1(\mathbb Q,V_pE),\qquad V_pE=T_pE\otimes\mathbb Q_p,
$$
中的 elliptic Selmer 类。把两个幂级数环的变量都记成 $T$，并不会改变系数表示。

还有一个可直接核查的表示障碍。若 $\rho_0(G)$ 含 $-I$，则相应群元素在 $\operatorname{ad}^0(\rho_0)$ 上作用为 $+1$，在标准二维表示 $V$ 上作用为 $-1$。若 $f:\operatorname{ad}^0(\rho_0)\to V$ 是 $G$-线性映射，则
$$
f(x)=f((-I)x)=(-I)f(x)=-f(x),
$$
故 $f=0$。反向的 $G$-线性映射也只能为零。Cartan 群含 $-I$，本处正具有这种差异。

在一个把 Cartan 分裂的系数扩张上，也可把差异看得更具体：若 $V$ 的两个特征为 $\lambda,\lambda^{-1}$，则 trace-zero adjoint 的三个特征为
$$
\lambda^2,\quad1,\quad\lambda^{-2}.
$$
需要额外的算术构造，才能把这类信息传到本题的 $V$-系数 strict Selmer 群；原定理没有提供这条比较。

## 3. 二次扭转不变性进一步显示对象的区别

原文 Lemma 2.1 明确指出：上述最大像性质在二次扭转之间保持。设扭转特征为 $\chi$，则
$$
\rho_{A^\chi}\simeq\rho_A\otimes\chi;
$$
投影到 $\operatorname{PSL}_2$ 后，二次标量特征消失。相应地，
$$
\operatorname{ad}^0(V\otimes\chi)\simeq\operatorname{ad}^0(V),
$$
而 elliptic Selmer 群使用的标准表示变成 $V\otimes\chi$。扭转曲线的 Mordell–Weil 秩及所需的 cyclotomic leading term 并不由这个表示同构识别。

这并不证明“变形理论永远无用”；它准确指出了目前缺少的桥：必须从该 adjoint 变形最大像，独立推出一个标准表示系数的 Selmer 维数上界或适用的二次导数非零结论。原文的 Theorem 1.2、固定 $BH_2^0$ 的单位条件以及 Lemma 2.1 都没有给出该桥。

因此，不把这里的“几乎所有 inert $p$”登记为本题无穷初级有限性的进展。supersingular 路线仍回到上一笔记 §1 的 signed 二次项判据。
