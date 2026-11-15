# R733 — 两条实际三次扭点的全部 p 椭圆对数代数线性独立

日期：2026-11-15。**状态：已证明。**

本篇固定两个实际代数点，证明它们在同一条 CM 椭圆曲线上的 p-adic 对数对每个素数 p 都在嵌入的 $\overline{\mathbf Q}$ 上线性独立。论证不使用 ordinary 假设、复解析秩一、未证明的 p-adic 调节子非退化，或不同周期的自由选择。

这付清 R732/R734 后续所需的一个独立算术输入。原型五负一矩是否准确等于这些对数乘**同一个**非零周期及代数常数，仍须 R735 的完整有限角色、Euler 因子和周期比较。本文不预付该等式，也不删除原 paired-T 的相反外部项。

## 1. 固定曲线、点与同一代数微分

固定
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad
t^3=17,\qquad L=K(t),
$$
并取
$$
E_1:y^2=x^3+1,\qquad
E_2:y^2=x^3+17^2,\qquad
E_4:y^2=x^3+17^4.
\tag{1}
$$
下标2、4表示17的指数。各曲线使用指定的代数微分
$$
\varpi_i=\frac{dx}{2y}.
$$
令
$$
P_2=(-4,15)\in E_2(\mathbf Q),\qquad
P_4=(42,397)\in E_4(\mathbf Q).
\tag{2}
$$
这些是实际点，不是由一个未核实的 Heegner 点规范代替的形式符号。

定义同一代数域上的同构
$$
\phi_2:E_2\longrightarrow E_1,\qquad
(x,y)\longmapsto(x/t^2,y/17),
$$
$$
\phi_4:E_4\longrightarrow E_1,\qquad
(x,y)\longmapsto(x/t^4,y/17^2).
\tag{3}
$$
因为 $t^3=17$，(3) 确实保持方程且保持无穷远原点。相应点为
$$
Q_2=\left(-\frac4{t^2},\frac{15}{17}\right),\qquad
Q_4=\left(\frac{42}{t^4},\frac{397}{17^2}\right)
\quad\text{in }E_1(L).
\tag{4}
$$
微分的运输准确为
$$
\boxed{\phi_2^*\varpi_1=t\varpi_2,\qquad
       \phi_4^*\varpi_1=t^2\varpi_4.}
\tag{5}
$$
这里没有独立归一两个 p-adic 周期。

### 1.1 两点非扭

Nagell–Lutz 定理对整短 Weierstrass 方程的有理扭点给出：若 $y\ne0$，则 $y^2$ 整除该方程的判别式。两式 (1) 的判别式分别为
$$
-432\cdot17^4,\qquad -432\cdot17^8;
$$
其素因子都在 $\{2,3,17\}$ 中。
$P_2$ 的 y 坐标含素因子5；$P_4$ 的 y 坐标397大于1且与 $2\cdot3\cdot17$ 互素。因此两个点均不可能是扭点，(3) 下的 $Q_2,Q_4$ 也非扭。

(2) 的曲线上关系和上述整除判据，亦已由公开脚本
[check-r732-two-cubic-rank-one-bounds.py](../scripts/check-r732-two-cubic-rank-one-bounds.py)
在 run 43701949704、job 132774806522 中作精确整数核算。
本篇只使用其这部分有限恒等式，不使用该脚本中尚需另付导子及根号假设的解析秩结论。

## 2. 在代数点上支付完整 CM 独立性

17在K中不分歧；其上任一素点的规范赋值满足 $v(17)=1$。故17不是K中的三次幂，$X^3-17$ 在K上不可约。因为 $\omega\in K$，$L/K$ 是三次循环扩张，其生成元为
$$
\sigma(t)=\omega t.
$$
在 $E_1$ 上取原 CM 自同构
$$
[\omega](x,y)=(\omega x,y).
$$
于是直接从 (4) 得
$$
\boxed{\sigma Q_2=[\omega]Q_2,\qquad
       \sigma Q_4=[\omega^2]Q_4.}
\tag{6}
$$
$E_1$ 的全几何自同态环为 $\mathcal O_K=\mathbf Z[\omega]$，所有这些自同态都在K上定义；所以它们与 $\sigma$ 的代数作用交换。

**引理 1。** 对 $a,b\in\mathcal O_K$，
$$
[a]Q_2+[b]Q_4\text{ 是扭点}
\quad\Longrightarrow\quad a=b=0.
\tag{7}
$$

**证明。** 设左端为扭点T。对关系作用 $\sigma$，再减去 $[\omega]T$，由 (6) 得
$$
[(\omega^2-\omega)b]Q_4=\sigma T-[\omega]T.
$$
右端是扭点。若 $b\ne0$，左侧使用一个非零椭圆曲线自同态，因而是同源映射；一个点在非零同源映射下映成扭点，会使原点本身成为扭点。这与 $Q_4$ 非扭矛盾。因此 $b=0$，再用 $Q_2$ 非扭得 $a=0$。证毕。

等价地，$Q_2,Q_4$ 在
$$
E_1(\overline{\mathbf Q})\otimes_{\mathbf Z}\mathbf Q
$$
中对K线性独立。这里所有 Galois 运算均发生在代数点上；没有假定 $\sigma$ 对某个给定的 p-adic 完备化连续，更未将它直接作用到对数值。

## 3. 对每个 p 定义同一代数微分的对数

现在任取一个素数 p 和嵌入
$$
\iota_p:\overline{\mathbf Q}\hookrightarrow\mathbf C_p.
$$
在以下式子中，把L及代数系数按这个嵌入视为 $\mathbf C_p$ 的子域。

取包含 $Q_2,Q_4$ 坐标的有限扩张 $F/\mathbf Q_p$。
$E_1(F)$ 是紧 p-adic Lie 群；在原点存在一个足够小的开子群V，
使按 $\varpi_1$ 归一的 formal logarithm 与 exponential 互逆。
商 $E_1(F)/V$ 有限，所以存在正整数n同时使
$$
[n]Q_2,\ [n]Q_4\in V.
\tag{8}
$$
用
$$
u_{i,p}=\log_{E_1,\varpi_1}(Q_i)
       :=\frac1n\log_{E_1,\varpi_1}([n]Q_i),\qquad i=2,4,
\tag{9}
$$
定义全点的对数。两个容许整数的共同倍数证明定义与n无关。
它是群同态，与所有代数同态及其 Lie 导数相容。

这一定义对坏素数2、3同样成立：使用足够小的解析子群即可，不需要普通约化，也不要求 (1) 在p处是极小模型。
若要将任意代数点与有限个自同态同时放在上述讨论中，扩大F及缩小V仍可。

对有限扩张F上的点，对数的核准确为扭子群：
扭点由群同态性映成零；反过来，若对数为零，取n使其倍点在V内，
formal logarithm 在V上的单射性给 $[n]P=O$。
因此
$$
u_{2,p}\ne0,\qquad u_{4,p}\ne0.
\tag{10}
$$

对 $a\in\mathcal O_K$，$[a]^*\varpi_1=a\varpi_1$，故
$$
\log_{E_1,\varpi_1}([a]P)=\iota_p(a)\log_{E_1,\varpi_1}(P).
\tag{11}
$$
若 $a u_{2,p}+b u_{4,p}=0$，先清K分母令 $a,b\in\mathcal O_K$，
由 (9)–(11) 得 $[a]Q_2+[b]Q_4$ 是扭点；
引理1遂给 $a=b=0$。所以两个对数已经在K上独立。

## 4. 从 CM 独立升级到所有代数系数

这里使用的已发表定理是：

> 对定义于 $\overline{\mathbf Q}$ 的简单阿贝尔簇A，若若干处在实际指数定义域内、指数为代数点的对数在 $\operatorname{End}(A)$ 上线性独立，则它们在 $\operatorname{End}_{\overline{\mathbf Q}}(\operatorname{Lie}A)$ 上线性独立。

这是 Fuchs–Pham，
[*Some applications of the p-adic analytic subgroup theorem*](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf)，
*Glasnik Matematički* 51(71) (2016), 335–343，
Theorem 2.2（第338页）；其证明见 §3.2（第340–341页），基础解析子群定理为同文 Theorem 1.1。
引用中的标量域是 $\overline{\mathbf Q}$，不是其打印文本抽取时可能丢掉上横线的 $\mathbf Q$。

取 $A=E_1$，这是简单阿贝尔簇。
按 (8) 可使 $n u_{2,p},n u_{4,p}$ 同时处在真实 exponential 定义域内，且
$$
\exp_{E_1}(n u_{i,p})=[n]Q_i\in E_1(\overline{\mathbf Q}).
$$
第3节及引理1保证它们在 $\operatorname{End}(E_1)=\mathcal O_K$ 上独立。
另一方面 $\operatorname{Lie}E_1$ 在 $\overline{\mathbf Q}$ 上是一维，
所以其代数线性自同态环就是 $\overline{\mathbf Q}$。
上述定理遂直接给：

**定理 2。** 对每一个素数 p、每一个 $\iota_p$，有
$$
\boxed{
\alpha u_{2,p}+\beta u_{4,p}=0,\qquad
\alpha,\beta\in\iota_p(\overline{\mathbf Q})
\quad\Longrightarrow\quad \alpha=\beta=0.
}
\tag{12}
$$

这是单个p上的完整结论，故当然也同时适用于后续已付的任何无限 ordinary 素数子族。
系数 $\alpha,\beta$ 可以随p、N或实际测试改变；它们须每次确是代数数。
(12) 不断言两个对数代数独立，也不把一般 $\mathbf C_p$ 单位当成代数系数。

由 (5) 及对数的自然性，还得到原两条有理曲线上的准确形式
$$
\boxed{
u_{2,p}=\iota_p(t)\log_{E_2,\varpi_2}(P_2),\qquad
u_{4,p}=\iota_p(t^2)\log_{E_4,\varpi_4}(P_4).
}
\tag{13}
$$
所以这两条有理点对数也在 $\iota_p(\overline{\mathbf Q})$ 上线性独立。
特别，$u_{2,p}/u_{4,p}$ 不属于嵌入的 $\overline{\mathbf Q}$。

## 5. 可直接用于原负矩的准确接口

以下推论把所需的周期条件明确列出，不提前宣称任何未核实的 theta 识别。

**推论 3。** 假设两个实际数 $I_{2,p},I_{4,p}$ 已另行证明满足
$$
\Omega_p I_{2,p}=c_{2,p}u_{2,p},\qquad
\Omega_p I_{4,p}=c_{4,p}u_{4,p},
\tag{14}
$$
其中 $\Omega_p\in\mathbf C_p^\times$ 是**同一个**非零因子，
$c_{2,p},c_{4,p}\in\iota_p(\overline{\mathbf Q})^\times$。
则 $I_{2,p},I_{4,p}$ 在 $\iota_p(\overline{\mathbf Q})$ 上线性独立。

**证明。** 一个代数系数关系乘 $\Omega_p$ 后，由 (14) 变成 (12) 的关系；
因为两个c都非零，两系数均零。证毕。

(14) 也可使用共同因子的倒数，或先给两因子但完整证明其比值为非零代数数；
这三种写法相同。仅知每条数“与某个对数成比例”不足够。

特别，当 R735 以全部原局部角色、Euler 因子及周期支付
$$
I_{2,p}=\mathfrak I(D_{\omega,17}),\qquad
I_{4,p}=\mathfrak I(D_{-,17})
$$
的 (14) 时，R734 的实际代数系数 $c/a,1/a$ 给
$$
\frac ca\mathfrak I(D_{\omega,17})
+\frac1a\mathfrak I(D_{-,17})\ne0.
\tag{15}
$$
R734 已明确它们来自 $K(\lambda,\kappa,\kappa^N)$ 的实际方阵逆，
而 $\lambda=-\bar\pi_0^{-1}$、$\kappa=p\lambda^2$ 都是代数数；
这里没有用“p-adic 单位”偷换“代数数”。

(15) 仍只是原冻结负一组合的非零。
斜门提取中的外部 T 行有准确的相反补偿；
从 (15) 到原完整 $J'_T$、或者到固定 rank≥2 曲线的全 $\Sha[p^\infty]$ 有限，
尚需完整原域上的额外论证。本文没有赋原 q、P 或新的 CM 乘子任何额外中央零。

## 6. 依赖与复现范围

- 两个实际有理点、Nagell–Lutz 判据：第1节已完整列出；其有限整数核算见
  [公开回执](../ci/exact-check-20261115-r732-rank-one-bounds.json)。
- 两条同曲线上的K独立性：第2节原 Kummer 角色证明，无数值输入。
- 每个p的对数及核：第3节的紧群与局部 exponential 论证，涵盖所有p。
- 代数系数升级：上述 Fuchs–Pham Theorem 2.2，所有适用条件已逐项核定。
- 原型五线来自 [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md)，
  实际联合测试来自 [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)。
  其真实负一值的共同归一由R735继续，不是本篇的假设外结论。

本篇不需要新增数学运算，也不存储可重算输出。
