# 保留目标字符的有理微分：分母以外还需一个 p 变分子

**可信度：本文的有理函数、整性、有限精度及最低层公式均已证明。** 日期：2026-11-12。继续 [固定范数与奇字符笔记](2026-11-12-fixed-norm-loses-critical-character.md)。以下没有证明跨素数非消失；它将普通范数丢失的数据明确写成一个有理微分的分子，并给出模 $p^4$ 的有限计算式。

## 1. 设定与有理分子

沿用 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，以及
$$
L_p=K(E[\mathfrak p]),\quad
\Delta=\operatorname{Gal}(L_p/K),\quad
\rho=t(P_\pi),\quad
\rho_\chi=e_\chi\rho .
$$
在选定的 $\mathfrak p$ 完成中，基域为 $\mathbb Q_p$，$L_p$ 的局部扩张完全分歧、次数 $p-1$。R21 证明 $\rho_\chi$ 是非零的 $\widetilde\chi$ 本征均匀化元。记
$$
\mathcal F_p(X)
=\frac{e_\chi\log_p(1+X\rho)}{\rho_\chi}.
\tag{1}
$$
这里 $X$ 被 $\Delta$ 固定。对所有 $v_p(X)\ge0$，每个对数均收敛；对 $X$ 微分得
$$
\mathcal F_p'(X)=
\frac{1}{(p-1)\rho_\chi}
\sum_{\sigma\in\Delta}
\widetilde\chi(\sigma)^{-1}
\frac{\sigma\rho}{1+X\,\sigma\rho}.
\tag{2}
$$
前篇已经证明
$$
D_p(X)=\prod_{\sigma\in\Delta}(1+X\,\sigma\rho),
\qquad D_p(X)\in1+p\mathbb Z_p[X^4],
\quad\deg D_p=p-1.
$$
因此存在唯一多项式 $U_p$ 满足
$$
\boxed{\quad
\mathcal F_p'(X)=\frac{U_p(X)}{D_p(X)}.
\quad}
\tag{3}
$$
它还满足
$$
\boxed{\quad
U_p\in\mathbb Z_p[X^4],\quad
U_p(0)=1,\quad
\deg U_p\le p-5,\quad
U_p\equiv1\pmod p.
\quad}
\tag{4}
$$

下面逐项证明，而不把 (4) 作为额外假设。

## 2. 系数整性、CM 对称及不可消去的极点

式 (2) 的分子除以 $\rho_\chi$ 后被 $\Delta$ 固定，故各系数在 $\mathbb Q_p$ 中。设
$$
s_n=\frac{e_\chi(\rho^n)}{\rho_\chi}.
$$
投影 $e_\chi$ 的系数均为 $p$-进整数且 $p-1$ 为单位，所以
$$
v_p(s_n)\ge\frac{n-1}{p-1}.
\tag{5}
$$
同时 $s_n\in\mathbb Q_p$，因此其赋值是整数。特别地 $s_1=1$，$n\ge2$ 时 $s_n\in p\mathbb Z_p$。式 (2) 在原点的展开为
$$
\mathcal F_p'(X)=\sum_{n\ge0}(-1)^n s_{n+1}X^n.
\tag{6}
$$
故它的系数全部整，常数为一，其余系数均被 $p$ 整除。乘以 $D_p$，得到 $U_p$ 的整性与模 $p$ 结论。

还须解释次数降低。单纯通分 (2) 给 $\deg U_p\le p-2$。曲线的 CM 作用满足
$$
t([i]P)=i\,t(P),\qquad \widetilde\chi(i)=i.
$$
因此若 $s_n\ne0$，必须有 $i^n=i$，即 $n\equiv1\pmod4$。所以 (6) 只含 $X^{4j}$；$D_p$ 也只含这些幂，于是 $U_p\in\mathbb Z_p[X^4]$。写 $p=4r+1$，次数 $\le p-2=4r-1$ 的最大四倍数是 $4r-4=p-5$，得 (4)。

这个分子没有消去分母的任何根。对于
$$
x_\sigma=-\frac1{\sigma\rho},
$$
式 (2) 在 $x_\sigma$ 的留数为
$$
\operatorname{Res}_{X=x_\sigma}
\bigl(\mathcal F_p'(X)\,dX\bigr)
=\frac{\widetilde\chi(\sigma)^{-1}}{(p-1)\rho_\chi}\ne0.
\tag{7}
$$
所有 $x_\sigma$ 互异，故
$$
\gcd(U_p,D_p)=1.
\tag{8}
$$
因此 $\mathcal F_p'$ 有恰好 $p-1$ 个不同有限极点。作为整个有理函数，它不可能由固定有限组、极点集合固定的有理函数作标量线性组合得到。这个结论只针对整条有理微分，不排除在单点 $\alpha$ 或特定迹中另有特殊公式。

## 3. 原目标正好是这条微分的固定域积分迹

令 $\alpha=v/u\in M$ 为 R18 的固定数。它在所有目标素位为单位，且
$$
\operatorname{Tr}_{M/K}\alpha=0.
$$
由于式 (1) 的常数为零，
$$
\mathcal F_p(\alpha)=
\int_0^\alpha\frac{U_p(X)}{D_p(X)}\,dX.
\tag{9}
$$
这里积分是原点幂级数的逐项积分再在 $\alpha$ 处求值。分母的所有根满足 $v_p(x_\sigma)=-1/(p-1)<0$，因此积分级数的收敛半径大于一，求值没有路径或分支选择问题。

原来的标量恰为
$$
\boxed{\quad
\mathcal Q_p
=\frac{e_\chi\log_p\Phi(P_\pi)}{\rho_\chi}
=2\operatorname{Tr}_{M/K}
\int_0^\alpha\frac{U_p(X)}{D_p(X)}\,dX.
\quad}
\tag{10}
$$
所以 R31 的固定单位恒等式给了分母的一个值 $D_p(\alpha)$，而目标实际还需要字符分子 $U_p$ 及其与分母的积分配对。仅将 $\log D_p(\alpha)$ 取迹并不等于 (10)。

若要对所有 $X$ 重建加权对象，额外数据可具体选为
$$
U_p(X)=1+p\sum_{j=1}^{r-1}u_{p,j}X^{4j}.
$$
这是一个精确的有限数据描述；这里没有证明这些 $r-1$ 个系数独立，也没有证明某个特定迹必需这么多个参数。它们的个数随 $p$ 增长，不能直接称为固定有限个数域元素。

## 4. 模 p^4 只需三个分母修正项

记
$$
d_p(X)=D_p(X)-1\in p\mathbb Z_p[X^4].
$$
则
$$
\boxed{\quad
\mathcal Q_p\equiv
2\operatorname{Tr}_{M/K}
\left[
\int_0^\alpha
U_p(X)\bigl(1-d_p(X)+d_p(X)^2-d_p(X)^3\bigr)\,dX
\right]\pmod{p^4}.
\quad}
\tag{11}
$$
这个有限式使用 $U_p,D_p$ 模 $p^4$ 即可，不需因为积分而整体再多算一位。

完整尾项论证如下。几何级数的第 $k$ 项为
$U_p(-d_p)^k$，其系数在 $p^k\mathbb Z_p$ 中，且积分后的次数至多
$$
(p-5)+k(p-1)+1=(k+1)(p-1)-3.
\tag{12}
$$
只会出现 $X^n/n$，其中 $n\equiv1\pmod4$。当 $k=4$ 时，这个次数小于 $5p$，唯一可能被 $p$ 整除的 $n$ 为 $p$。另一方面
$$
b_0=\operatorname{Tr}_{M/K}\alpha^p\in p\mathbb Z_p,
\tag{13}
$$
因为固定域在目标位不分歧，$\alpha^p\equiv\sigma_\mathfrak p\alpha\pmod p$，而 $\operatorname{Tr}\alpha=0$。故取迹以后，$n=p$ 的积分分母也被 (13) 抵消，第四项仍在 $p^4\mathbb Z_p$ 中。

若 $k\ge5$，对 $p\ge13$ 有
$$
(k+1)(p-1)<p^{k-3}.
$$
从 $k=5$ 开始验证后逐次乘 $p$ 即得。于是 (12) 中任意 $n$ 满足
$v_p(n)\le k-4$，积分最多损失 $k-4$ 位，第 $k$ 项仍在 $p^4\mathbb Z_p$ 中。实际统一赋值下界为
$$
k-\left\lfloor\log_p\bigl((k+1)(p-1)\bigr)\right\rfloor
\longrightarrow\infty,
$$
所以积分后的尾项确实收敛，也可逐项取有限域迹。

最后，(11) 内各多项式积分后的次数小于 $5p$，仍只有 $n=p$ 可能出现一个 $p$ 分母，而 (13) 抵消它。因此把输入系数改变 $p^4$ 的倍数，不改变 (11) 模 $p^4$ 的值。这个精度结论依赖取固定域迹；未取迹的单点积分不能直接使用同一结论。

## 5. 分子的最低非平凡层可用固定级数给出

令
$$
A(t)=\frac{\log_E(t)}t
=\sum_{j\ge0}
\frac{(-1)^j\binom{2j}{j}17^j}{4j+1}\,t^{4j},
\qquad L(t)=\log A(t).
$$
对 $1\le j\le r-1$，有
$$
\boxed{\quad
[X^{4j}]U_p(X)\equiv
[X^{4j}]D_p(X)
+\pi(4j+1)[t^{p-1-4j}]L(t)
\pmod{p^2}.
\quad}
\tag{14}
$$
式中固定级数的指数随 $p$ 变化；该等式不把它化成固定有限个系数。

证明使用 R21 的 tame 线性化坐标 $z(t)$，满足
$$
z(t)=t+\cdots,\qquad z([\omega]t)=\omega z(t),
\qquad z(\rho)=\rho_\chi.
$$
其逆级数记 $t=H(z)\in\mathbb Z_p[[z]]$。形式对数的同一等变性说明
$$
\log_E(H(z))=z+\text{次数至少为 }p\text{ 的项}.
$$
故 $H(z)$ 在次数小于 $p$ 的部分等于椭圆形式指数 $\exp_E(z)$。

令 $\beta=\rho_\chi^{p-1}$。在 $z$ 坐标中，$[\pi](z)$ 模 $p$ 为 $z^p$，且线性项为 $\pi z$；将非零核点代入得
$$
\beta\equiv-\pi\pmod{p^2}.
\tag{15}
$$
对 $n=4j+1$，$5\le n\le p-4$，tame 投影只保留次数
$1+k(p-1)$，于是
$$
s_n\equiv\beta\,[z^p]H(z)^n\pmod{p^2}.
\tag{16}
$$
决定右侧系数所需的 $H$ 次数至多 $p-n+1<p$，所以可以换成 $\exp_E$。Lagrange 反演给
$$
[z^p]\exp_E(z)^n
=\frac np[t^{p-n}]A(t)^{-p}
\equiv-n[t^{p-n}]L(t)\pmod p.
\tag{17}
$$
最后一步只涉及次数小于 $p-1$ 的 $A,L$，这些系数均 $p$-整，故
$A^{-p}=\exp(-pL)\equiv1-pL\pmod{p^2}$ 在所需次数上成立。由 (15)–(17)，
$$
s_{4j+1}\equiv
\pi(4j+1)[t^{p-1-4j}]L(t)\pmod{p^2}.
$$
再用 $U_p=D_p\mathcal F_p'$：两边所有非恒定系数均在 $p$ 中，乘积交叉项在 $p^2$ 中，遂得 (14)。

## 6. 对研究主线的作用与尚缺输入

式 (3)、(10)、(11) 保留了目标字符，并把未知对象精确定位为 $U_p$。式 (14) 的第一层已经出现固定椭圆对数级数的变化指数系数，和 R17、R21 的变化权现象一致。

当前固定单位 $u$ 的 Frobenius quotient 控制分母在 $\alpha$ 的值；它没有控制这个字符分子。另一方面，精确辅助67比较在正确字符块上已经证明只回到原来的 $\mathcal Q_p$。因此本文没有从固定单位非挠性、普通范数非零或局部均匀化元的已知估值推出 $\mathcal Q_p$ 的浅深度，更没有推出双权成功或有限类群证书对无穷多个 $p$ 存在。

继续使用此公式时，真正需要增加的是对 (10) 或 (11) 中**实际原始字符分子与固定导子迹的配对**的跨素数非消失控制。

## 依赖

- R18：$\alpha$ 的整性、固定域不分歧、$\operatorname{Tr}\alpha=0$。
- R19、R21：$\Phi$、目标字符、tame 线性化与 $\rho_\chi$ 的均匀化元性质。
- R29 及 Padé 桥：$D_p$ 的全局次数和 $D_p\equiv1\pmod p$。
- 前篇固定范数笔记：$D_p$ 的核点乘积式、正确加权 resolvent 与原目标的准确关系。
- 本文其余结论已在上述各节逐项证明。
