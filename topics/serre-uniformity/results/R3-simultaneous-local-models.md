# R3：同时满足 p 处和全部潜在乘法处条件的显式曲线

日期：2026-11-12。状态：**已证明的路线边界**。所有结论均只针对写出的局部条件；最后还给出全局满射的子族。**不是 Serre 一致性的反例。**

## 1. 构造与结论

取素数 $p>37$，$p\equiv2\pmod3$，以及素数 $q\equiv1\pmod p$。设
$$D=1728q^p-p^{3p},\qquad
E_{p,q}:y^2=x^3+\frac{3p^p}{D}x+\frac2D.$$

则：

1. $E_{p,q}/\mathbb Q$ 无 CM；
2. $p$ 处有好超奇异约化，局部模 $p$ 像为完整 $N_{\rm ns}(p)$；
3. 只有 $q$ 是负 $j$-赋值的素数，在该处的模 $p$ 像包含于标量群 $\{\pm I\}$。

因此全部潜在乘法约化处都满足 R2 的完整判据，而不仅是其中的赋值和同余必要条件。

## 2. 不变量、好约化与无 CM

直接计算得到
$$\Delta(E_{p,q})=-\frac{2^{12}3^6q^p}{D^3},\qquad
j(E_{p,q})=\frac{p^{3p}}{q^p}.$$
因 $p\ne q$，$D$ 在 $p,q$ 处都是单位：模 $p$ 它为 $1728q^p\ne0$，模 $q$ 它为 $-p^{3p}\ne0$。$D\ne0$，否则取 $p$-赋值立刻矛盾。

有理 $j$ 非整数，所以由 CM 的 $j$ 为代数整数这一经典定理，曲线无 CM。负 $j$-赋值恰在 $q$ 处，值为 $-p$。

在 $p$ 处给出的方程已为好约化方程：$A$ 的赋值为 $p>0$，$B$ 是单位，$\Delta$ 是单位。约化形如 $y^2=x^3+\bar B$。因为 $p\equiv2\pmod3$，立方映射在 $\mathbb F_p$ 上双射，故
$$\#\widetilde E_{p,q}(\mathbb F_p)
=p+1+\sum_{x\in\mathbb F_p}\left(\frac{x^3+\bar B}{p}\right)=p+1.$$
于是约化超奇异。

Serre 1972, §1.11, Proposition 12（印刷页 275）给出：在绝对分歧指数 $1$ 的局部域上，好超奇异约化的模 $p$ 惯性像为完整 $\mathbb F_{p^2}^\times$。对 $\mathbb Q_p$，Frobenius 共轭按 $p$ 次幂作用，非平凡地正规化此 Cartan；因此总局部像为完整正规化子。这里使用的是已发表的惯性定理；[原文](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)。

## 3. 唯一潜在乘法处的 Tate 参数

在 $q$ 处，$c_4=-144p^p/D$ 为单位，所以曲线实际上有乘法约化。其 Tate 参数 $t$ 满足
$$t=j^{-1}(1+u)
=\left(\frac q{p^3}\right)^p(1+u),\qquad u\in q^p\mathbb Z_q.$$
由于 $p\ne q$，$1+u$ 在 $\mathbb Q_q$ 中为 $p$ 次幂。因而 $t$ 本身为 $p$ 次幂。又 $q\equiv1\pmod p$，所以 $\mu_p\subset\mathbb Q_q$；Tate 曲线的全部 $p$-挠点已定义在 $\mathbb Q_q$ 上。原曲线只可能多一个二次扭曲，故局部像包含于 $\{\pm I\}$。

## 4. 参数确实可取任意大

$p\equiv2\pmod3$ 的素数无穷多：有限性假设下取这些素数之积 $P$，整数 $3P-1$ 必有一个新的 $2\pmod3$ 素因子。

对固定的这样的 $p$，不用寻找算术级数中的素数也能选 $q$。取
$$q\mid\Phi_p(p)=1+p+\cdots+p^{p-1}$$
的任一素因子。该数模 $p$ 为 $1$，故 $q\ne p$。$p$ 在 $\mathbb F_q^\times$ 中的阶整除 $p$；若阶为 $1$，则上式模 $q$ 等于 $p$，迫使 $q=p$，矛盾。故阶为 $p$，$q\equiv1\pmod p$。

## 5. 一个全局满射的无穷子族

进一步取
$$p\equiv41\pmod{60},\qquad q\equiv1\pmod{5p}.$$
这样的 $p$ 无穷多，由 Dirichlet 算术级数素数定理。固定 $p$ 后可取 $q$ 为 $\Phi_{5p}(5p)$ 的任意素因子：$q\nmid5p$，而在剩余特征不整除 $5p$ 时，$\Phi_{5p}$ 的根恰为 $5p$ 阶单位根（$X^{5p}-1$ 可分），所以 $5p$ 是 $5p\bmod q$ 的阶，给出所需同余。

在 $5$ 处，$D\equiv2$，且
$$A\equiv4,\qquad B\equiv1\pmod5.$$
这是好约化，约化为
$$\widetilde E:y^2=x^3+4x+1\quad\text{over }\mathbb F_5.$$
对 $x=0,1,2,3,4$，右侧分别为 $1,1,2,0,1$，因此共有 $8$ 个点（含无穷远点），$a_5=-2$。

Frobenius 在模 $p$ 表示中的特征多项式为
$$X^2+2X+5,$$
判别式 $-16$。因 $p\equiv1\pmod4$，它在 $\mathbb F_p$ 中为非零平方，而迹 $-2\ne0$。R1 说明任何非分裂 Cartan 正规化子都不含这样的矩阵。因此此曲线的全局像不包含于非分裂正规化子。

甚至不必使用 R1 所引用的近期分类。$p$ 处的惯性使全局像包含一个完整非分裂 Cartan；Serre 1972, §2.7, Proposition 17（印刷页 282–283）说明含完整 Cartan 的子群只能是全部 $\mathrm{GL}_2$、某 Borel 的子群，或某 Cartan 正规化子的子群。非分裂 Cartan 不可约，排除 Borel。它有阶为 $p^2-1$ 的元素，而分裂正规化子的元素阶都不超过 $2(p-1)$，排除分裂正规化子。刚才的 Frobenius 排除非分裂正规化子。故
$$\bar\rho_{E_{p,q},p}(G_{\mathbb Q})=\mathrm{GL}_2(\mathbb F_p).$$

例如 $p=41,q=821$ 满足条件，给出明确的
$$j=\frac{41^{123}}{821^{41}}.$$
$821$ 为素数，可检查不被不超过其平方根的素数 $2,3,5,7,11,13,17,19,23$ 整除。

## 6. 精确解释

这个构造否定的是“$p$ 处局部非分裂正规化子加上全部潜在乘法处的局部非分裂正规化子条件足以排除大 $p$”这一中间设想。第 5 节更说明满足这些条件的曲线仍可能全局满射，别的好约化素数可以检测出差别。

本构造没有让所有好素数的 Frobenius 同时落在同一个正规化子内；做到这一点才会触及真正的反例。$p$ 处超奇异局部模型与乘法处 Tate 条件都需要进一步的全局输入才能解决课题。
