# 剩余三层的四阶惯性与全局整数范数

日期：2026-11-12。状态：**必要条件已证明；未排除剩余实际曲线。**

接续 R96/R97，关注 $p\in\{47,59,83\}$、$K=\mathbb Q(\sqrt{-3})$、精确三次商导子 $c=6,9$，并已知 $j\in\mathbb Z$。证明适用于任意 $p>37$、$p\equiv11\bmod12$ 的同样实际设置。本文不使用 BBM 整点分类。

执行环境重置后从原证明恢复；所列无界整数族始终不被当作实际异常曲线族。

## 1. 全局整数范数条件

若 $E/\mathbb Q$ 的实际模 $p$ 像为完整非分裂正规化子，商域为 $K=\mathbb Q(\sqrt{-3})$，惯性 $I_p=C^3$，三次商精确导子 $c=6$ 或 $9$，并且
$$p\equiv11\pmod{12},\qquad j\in\mathbb Z,\qquad j\ne1728,$$
则存在整数 $U,V$，使
$$
\boxed{j-1728=U^2-3V^2.}                                  \tag{1.1}
$$
结合 R96 的逆三次类，$j\ne0$ 时还必须满足
$$
\begin{array}{c|c}
c&dX^3-1728=U^2-3V^2\\ \hline
6&d=2^a3^b p^r,\quad a,r\in\{1,2\},\ b\in\{0,1\},\\
9&d=3^b p^r,\quad b,r\in\{1,2\},
\end{array}                                               \tag{1.2}
$$
其中 $X,U,V$ 均为整数。下面通过素因子分解证明真正的整数范数，不只给有理范数或局部可解性。

## 2. 奇素数处的真实四阶惯性

记 $N=j-1728\ne0$。设 $q\ge5,q\ne p$ 且 $v_q(N)$ 为奇数。整 $j$ 保证 $j$ 为 $q$ 进单位，潜在好约化的特殊纤维有 $j=1728$。由
$$
j-1728=c_6^2/\Delta
$$
知 $v_q(\Delta)$ 为奇数；实际温和惯性公式
$e_q=12/\gcd(12,v_q\Delta)$ 给 $e_q=4$。也可接 R20 已核的 Zywina Lemma 2.3(ii)，再用此特殊纤维的自同构群为 $\mu_4$。

$q$ 在 $K$ 不分歧，惯性 $C_4$ 在 Cartan 内。若 $s$ 是其生成元，$g$ 是实际 Frobenius 提升，则
$$gsg^{-1}=s^q.$$
$q$ 在 $K$ 分裂时 $g\in C$，故 $q\equiv1\bmod4$；惰性时 $g\in N\setminus C$，按 $s\mapsto s^p=s^{-1}$ 共轭，所以 $q\equiv-1\bmod4$。因此
$$
\left(\frac{-1}{q}\right)=\chi_K(q)=\left(\frac{-3}{q}\right),
$$
即
$$
\boxed{v_q(j-1728)\text{ 奇}\Longrightarrow(3/q)=1.}        \tag{2.1}
$$
所有 $q\equiv5,7\bmod12$ 在 $N$ 中的指数为偶数。例外素数 $p$ 本身满足 $(3/p)=1$，故不会造成范数障碍；不需要额外预设 $v_p(j)$ 下界。

## 3. 三处单位条件

R96 的实际局部商同域给
$$\Delta\in-3\mathbb Q_3^{\times2}.$$
故
$$N=c_6^2/\Delta\in-3\mathbb Q_3^{\times2}.$$
写 $e_3=v_3(N)$，则
$$
e_3\text{ 奇},\qquad N/3^{e_3}\equiv-1\pmod3.              \tag{3.1}
$$
不能只保留赋值奇性；单位条件会确定全局范数的正确符号。

## 4. 直接构造整数范数

$\mathbb Z[\sqrt3]$ 是最大整环且范数欧几里得：将商的两有理坐标取最近整数，误差 $u,v$ 的绝对值至多 $1/2$，故
$$|u^2-3v^2|\le3/4<1.$$
因此所有素理想有生成元。

在 $F=\mathbb Q(\sqrt3)$ 中可选
$$
\pi_2=1+\sqrt3,\ N\pi_2=-2,\qquad
\pi_3=\sqrt3,\ N\pi_3=-3.
$$
对分裂素数 $q\ge5$，取范数为 $q$ 的素理想之生成元 $\pi_q$。元素范数为 $\pm q$，而
$$N(a+b\sqrt3)\equiv a^2\pmod3.$$
故其符号唯一确定：
$$
N\pi_q=\begin{cases}q,&q\equiv1\bmod12,\\-q,&q\equiv11\bmod12.\end{cases} \tag{4.1}
$$
无需寻找范数为负一的单位；该实二次域没有这种单位。

分解
$$
N=\epsilon\,2^{e_2}3^{e_3}\prod_{q\ge5}q^{e_q},
\qquad\epsilon\in\{\pm1\}.
$$
所有惰性 $q$ 的 $e_q$ 为偶数。定义
$$
\gamma=(1+\sqrt3)^{e_2}(\sqrt3)^{e_3}
\prod_{(3/q)=1}\pi_q^{e_q}
\prod_{(3/q)=-1}q^{e_q/2}\in\mathbb Z[\sqrt3].              \tag{4.2}
$$
范数绝对值为 $|N|$，符号为
$$(-1)^{e_2+e_3+\sum_{q\equiv11\ (12)}e_q}.$$
在 (3.1) 中代入有理素因子分解；惰性 $q\equiv5\bmod12$ 的指数为偶数，其他惰性素数为一模三，得到
$$
-1\equiv\epsilon(-1)^{e_2+\sum_{q\equiv11\ (12)}e_q}\pmod3.
$$
$e_3$ 为奇数，所以上式正好使构造的范数符号等于 $\epsilon$。于是 $N\gamma=N$。写 $\gamma=U+V\sqrt3$ 即证 (1.1)，也同时解决了二处和符号兼容，不遗留局部条件。

## 5. 为什么这不是层 41 的有限 Thue 列表

R97 在层 41 得到的是
$$j-1728=-3mY^2,\qquad m\in\{1,-1,2,-2\}.$$
代入三次支撑后，二次范数因子的实部固定为 $24$，所以能列有限个 Thue 方程。

本节的 $U,V$ 都变化，不能把其中一个擅自固定为 $24$。事实上，对任意允许的正 $d$ 和非零整数 $t$，取
$$
j=d^4t^6,\quad X=dt^2,\quad U=d^2t^3,\quad V=24,
$$
便有
$$
j=dX^3,\qquad j-1728=U^2-3V^2.                            \tag{5.1}
$$
这些整数等式允许高度无界。对于 $c=6,v_3(d)=0$，取 $3\mid t$ 还满足 R96 的 $v_3(j)\in3\mathbb Z_{>0}$；对于 $c=9,v_3(d)=1,2$，分别给 $v_3(j)=4+6v_3(t)$ 或 $8+6v_3(t)$，同样落在 R96 的准确允许集合中。$v_3(j)>3$ 还使 $j-1728$ 的三进平方类为 $-3$。

(5.1) 没有保证完整三次角色或全部真实有限惯性，**不是实际异常曲线族**。它仅说明不能从这两条整数等式及所列 $j$ 赋值条件推出有限性或高度上界。

## 6. 实际仍变化的四次数据

R21 的类数一比较允许 $p\equiv11\bmod12$ 时有四次差字符。它不属于 $j=0$ 曲线的自同构群，不能当作有理 sextic twist 吸收。三次部分已由 $c=6,9$ 固定，四次部分仍可能在 (2.1) 允许的新素数处分歧。

因此 $\lambda^4$ 的导子受控不等于 $N_E$ 只支撑在 $2,3,p$。真正后续要把变化四次数据与实际 $E[2]$、$E[3]$ 或全局同余刚性联系起来。

一个可单独完整处理的子范围是：所有 $q\ge5,q\ne p$ 都没有四阶惯性。这时各这些 $q$ 的最小判别式赋值均偶，$p$ 处的三/六阶惯性也给偶赋值；全局平方类只支撑二、三。再用 (3.1)，只余
$$[\Delta]\in\{-3,6\},\qquad j-1728=-3Y^2\text{ 或 }6Y^2.$$
这恢复固定实部。[R98](../results/R98-small-levels-require-new-quartic-inertia.md) 已完成三层的完整 Thue 归约：396 个方程均以无 GRH 模式求全部整数解，49 组解恢复出的十三个非零 $j$ 全被实际惰性 Frobenius 迹排除，只余 CM 值零。因此剩余无 CM 曲线必须有新的四阶惯性素数；一般整数范数曲面及变化四次分歧仍未排除。

## 来源

- [R96](../results/R96-actual-cubic-discriminant-support-and-local-three-branches.md)：真实三处局部商、判别式平方类、三次支撑和精确 $j$ 赋值。
- [R97](../results/R97-level41-class-three-exclusion-by-certified-thue-equations.md)：层 41 的固定实部 Thue 归约。
- [R20](../results/R20-exact-quotient-field-and-small-unit-tests.md) §2 已核的 Zywina，*On the surjectivity of mod $\ell$ representations associated to elliptic curves*，Bull. London Math. Soc. **54** (2022), 2404–2417，Lemma 2.3；[作者原文](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)。
- [R21](../results/R21-twelfth-power-signature-and-cm-twists.md)：实际有限惯性及四次差字符的准确范围。
