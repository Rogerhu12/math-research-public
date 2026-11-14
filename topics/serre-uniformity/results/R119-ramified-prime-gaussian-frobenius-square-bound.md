# R119：商域分歧素数的高斯 Frobenius 与平方级下界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 对实际非分裂正规化子表示，R118 在商域的 $q\equiv1\pmod4$ 分歧素数处给出 $p\le4q$。保留好约化特殊纤维的真实四阶自同构，可以把这个界加强为
$$\boxed{q\ge p^2+4.}$$
证明使用完整 Frobenius 自同态，而不只使用它的迹模 $p$。它不要求小惯性、环类数限制或整 $j$。

## 1. 定理及一个可直接计算的必要条件

设 $p>37$，$E/\mathbb Q$ 的模 $p$ 像包含于某个非分裂 Cartan 正规化子
$N(C)$，且商角色 $N(C)\to\{\pm1\}$ 非平凡，所定二次域为 $K$。
若素数 $q\ge5$、$q\ne p$ 在 $K$ 分歧，并且 $q\equiv1\pmod4$，则存在非零整数 $a,b$，使
$$\boxed{q=a^2+b^2,\qquad p\mid b.}\tag{119.1}$$
因此
$$\boxed{q\ge p^2+4.}\tag{119.2}$$

若先独立计算素数 $q$ 的唯一无序正整数平方和表示
$$q=u^2+v^2,\qquad u,v>0,$$
则 (119.1) 等价地给出必要条件
$$\boxed{p\mid uv.}\tag{119.3}$$
这仍只是必要条件，不声称满足它就能构造全局异常曲线。

在本课题的完整正规化子设置中，$p$ 在 $K$ 惰性，故 $q\ne p$ 自动成立。
若 $t$ 是 $D=|D_K|$ 中模四为一的奇素因子个数，则
$$\boxed{D\ge(p^2+4)^t.}\tag{119.4}$$
尤其，只要存在这样的素因子，就有有效的 $p\le\sqrt{D-4}$。
该结论仍依赖变化的 $D$，不是 Serre 一致性的绝对上界。

## 2. 全分歧四次好约化域及真实四阶自同构

先回顾并展开 R118 引理118.2在此处的输入。若 $E$ 在 $q$ 潜在乘法，模 $p$ 惯性在正规化子中只能为标量 $\{\pm I\}$，其商角色不分歧，与假设矛盾。因此 $E$ 潜在好约化。

因为 $q\ge5$，有限惯性温和循环，阶属于 $1,2,3,4,6$。取映到外陪集的惯性元素 $\tau$。其行列式为一、迹为零，所以
$$\bar\rho(\tau)^2=-I.$$
有限惯性在模 $p$ 中忠实，故惯性群恰为 $C_4$，由 $\tau$ 生成。忠实性来自有限群阶与 $p$ 互素，而 $\mathrm{GL}_2(\mathbb Z_p)$ 的主同余核为 pro-$p$。

因 $K_q/\mathbb Q_q$ 分歧二次，可选一个算术 Frobenius 提升 $g\in G_{K_q}$。温和关系给
$$g\tau g^{-1}=\tau^q=\tau.$$
模 $p$ 时，$\bar\rho(g)$ 属于 $C$ 并与外陪集的 $\bar\rho(\tau)$ 交换。
将 $C$ 识别为 $\mathbb F_{p^2}^\times$，这恰说明其 Cartan 特征值被 $x\mapsto x^p$ 固定，故
$$\bar\rho(g)=rI,\qquad r\in\mathbb F_p^\times,\qquad r^2=q.\tag{119.5}$$

令 $N$ 为真实 $p$ 进 Tate 模上惯性作用的核，$\Gamma=G_{\mathbb Q_q}/N$。
其有限惯性 $I\simeq C_4$ 与 $g$ 交换。由 $1\mapsto g$ 给出的连续同态
$\widehat{\mathbb Z}\to\Gamma$，与非分歧投影复合为恒等，故像
$H=\overline{\langle g\rangle}$ 与 $I$ 交于一，且 $\Gamma=IH$。
于是 $H$ 是指数四的正规开子群，其固定域 $L/\mathbb Q_q$ 是循环全分歧四次扩张。
惯性核判据给 $E/L$ 好约化，且剩余域仍为 $\mathbb F_q$。

记特殊纤维为 $B/\mathbb F_q$。分歧群作用在好模型的特殊纤维上，得到真实自同构
$$\iota\in\operatorname{Aut}_{\mathbb F_q}(B),\qquad \iota^2=[-1].\tag{119.6}$$
它的阶准确为四：其在 $p$ 挠点上的作用就是上述忠实外陪集元素，可能因规范而取逆，但阶及下文结论不变。它定义于 $\mathbb F_q$，也可从 $g\tau=\tau g$ 与好约化的忠实 Tate 模作用直接确认。

特征大于三时，原点保持的四阶自同构强制 $j(B)=1728$。在短模型
$y^2=x^3+Ax+B_0$ 中，四阶乘子满足 $u^2=-1$；自同构的系数条件给
$B_0=u^6B_0=-B_0$，所以 $B_0=0$，而非奇异性保证 $A\ne0$。

## 3. Frobenius 必须是高斯整数

令 $\pi\in\operatorname{End}_{\mathbb F_q}(B)$ 为实际 $q$ 次 Frobenius。它的特征多项式为
$$T^2-tT+q,\qquad t\in\mathbb Z,\quad |t|\le2\sqrt q.$$
因 $q$ 是素数，$t^2\ne4q$，所以其在 $V_p(B)$ 上的矩阵非标量，中心化子维数为二。

Tate 的有限域主定理给
$$\operatorname{End}_{\mathbb F_q}(B)\otimes\mathbb Q_p
\simeq\operatorname{Cent}(\pi\mid V_p(B)).$$
因此 $\operatorname{End}_{\mathbb F_q}(B)\otimes\mathbb Q$ 是二维代数。
它已由 (119.6) 包含 $\mathbb Q(\iota)\simeq\mathbb Q(i)$，故恰为这个域。
这里不用预先把 $B$ 判为 ordinary，亦不用忽略 supersingular 情形后引用一个更强的分类。

Frobenius 满足上述首一整系数多项式，因而是 $\mathbb Q(i)$ 中的代数整数；这个域的最大整环为 $\mathbb Z[i]$。所以
$$\pi=a+b\iota,\qquad a,b\in\mathbb Z.$$
比较其在 Tate 模上的迹和行列式，得
$$t=2a,\qquad q=a^2+b^2.\tag{119.7}$$
两坐标都非零，否则素数 $q$ 是整数平方。

同一个 $g$ 是 $B$ 的算术 Frobenius，其模 $p$ 矩阵由 (119.5) 是标量。
而 $\bar\iota$ 是正规化子外陪集元素，绝不为标量。因此 $I,\bar\iota$ 在
$\mathbb F_p$ 上线性无关。把 $\pi=a+b\iota$ 模 $p$，立即得到
$$p\mid b.$$
这证明 (119.1)，没有从 $p\mid(4q-t^2)$ 错误地直接推断平方整除；平方整除来自真实的高斯整数分解。

由于 $q$ 为奇素数，$a,b$ 奇偶相反。若 $b$ 奇，则 $|b|\ge p$，且非零偶数 $a$ 满足 $|a|\ge2$；若 $b$ 偶，则 $|b|\ge2p$，且 $|a|\ge1$。分别得到
$$q\ge p^2+4\quad\text{或}\quad q\ge4p^2+1,$$
故总有 (119.2)。高斯整数唯一分解给素数的平方和表示只相差符号与交换坐标，证明 (119.3)。将不同分歧素因子相乘即得 (119.4)。

## 4. 模四为三的分歧素数：局部论证的准确边界

若 $q\equiv3\pmod4$，温和关系变为 $g\tau g^{-1}=\tau^{-1}$。
R118 准确给出的是
$$\left(\frac{-q}{p}\right)=-1,\qquad\lambda(g)^4=q^2.$$
四阶自同构此时不与真实 Frobenius 交换，因此 §3 的高斯整数论证不能套用。

一个显式局部实现说明这个区别。固定任意 $q\ge7$、$q\equiv3\pmod4$，取全局曲线
$$E_q:y^2=x^3+qx+q^2.$$
它的
$$j(E_q)=\frac{6912}{4+27q}$$
非整：分母是大于一且与六互素的奇数，而 $6912$ 只含素因子二、三。因此 $E_q$ 无 CM。
在 $u^4=q$ 的全分歧四次扩张上令 $x=u^2X,y=u^3Y$，得到
$$Y^2=X^3+X+u^2,$$
有好约化 $B:Y^2=X^3+X$。惯性生成元在特殊纤维作用为
$\iota:(X,Y)\mapsto(-X,iY)$，阶为四。

因 $(-1/q)=-1$，在点数的二次角色和中用 $X\mapsto-X$ 配对，得真实迹为零。
所以
$$\pi^2=[-q],\qquad\pi\iota=-\iota\pi.$$
对每个 $p>37$、$p\ne q$ 且 $(-q/p)=-1$，代数
$\mathbb F_p[\bar\pi]\simeq\mathbb F_{p^2}$ 的乘法群给一个非分裂 Cartan。
$\bar\pi$ 属于它，$\bar\iota$ 在其正规化子的外陪集；整个局部分解群像由这两类元素生成，故落在该正规化子中，商二次角色在 $q$ 分歧。

这些局部输入可在固定的 $q$ 和任意大的适当 $p$ 上实现。此例不声称
$E_q$ 的**全局**像包含这个正规化子；它精确说明不能把 (119.2) 的局部推导扩到
$q\equiv3\pmod4$。主问题中只含这类小分歧素因子的变化二次域仍须新的全局约束。

## 5. 来源和连接

1. J. Tate, *Endomorphisms of Abelian Varieties over Finite Fields*, Inventiones Mathematicae **2** (1966), 134–144，[全文](https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf)，§1 Main Theorem、Lemma1及其 $\operatorname{End}$ 表述。这里准确用其有限域中心化子同构；二维和高斯整性在 §3 另行推出。
2. [R118 §6](R118-class-number-twelve-periods-and-ramified-frobenius.md)：真实有限惯性 $C_4$、商域分歧、同一个 Frobenius 和全分歧好约化截面。本文把该处的真实自同构继续保留至完整 Frobenius 环。
3. [R2](R2-exact-tate-local-criterion.md) 的潜在乘法惯性限制，以及 [R63](R63-all-prime-classes-and-quotient-discriminant-growth.md) 的惯性忠实性与连续截面接口。本文的局部模型、模 $p$ 线性独立、奇偶性和平方和必要条件均显式证明。

R119 不假设相应全局异常曲线存在，不构造反例族，也未完成一般变化商域或主问题。
