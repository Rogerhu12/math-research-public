# R90：类数三周期的完整消失表，以及实际椭圆曲线条件对四个例外的排除

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明；完整证明与严格球算术证书均已复核。** 本篇完成环类数恰为三的全部判别式和全部 $p>37$，不再限制 $M<3p$。一般三次角色确有四个中心值全消失例，但它们不能来自本题相应的实际小惯性表示。因此，在实际小惯性分支，环类数三时的非消失没有 $M/p$ 限制。

## 1. 两个不同量词的结论

令 $K$ 为判别式 $-D$ 的虚二次域，$\mathcal O_c=\mathbb Z+c\mathcal O_K$，$M=Dc^2$。设
$$h(\mathcal O_c)=3,$$
$\eta$ 是准确导子 $c$ 的原始三阶环类角色，$p>37$ 惰性于 $K$，且 $p\nmid M$。记实际素水平 Brandt 周期为 $P_\eta$。

**定理 90.1。** 下列三条件等价：

1. $P_\eta=0$；
2. 对每个 $g\in S_2(\Gamma_0(p))^{\mathrm{new}}$，都有 $L(\tfrac12,\pi_{g,K}\otimes\eta)=0$；
3. $(M,p)$ 是下表中的一对。

| $M=D$ | $p$ | 三个 CM 点共同约化的 $j$ | $p\equiv2,5\pmod9$ |
|---:|---:|---:|:---:|
| 379 | 43 | 41 | 否 |
| 643 | 41 | 28 | 是 |
| 883 | 47 | 9 | 是 |
| 883 | 59 | 28 | 是 |

在这些例子中 $c=1$；两个非平凡三次角色均消失。特别，所有 $p>59$、或所有 $h_K=1$ 且 $h(\mathcal O_c)=3$ 的情形均非消失。这张表表明：去掉大小条件后，对任意三次类域字符声称普遍非消失是错误的。

**定理 90.2（实际表示）。** 设无 CM 曲线 $E/\mathbb Q$、$p>37$ 满足完整非分裂正规化子像，且 $\rho_{E,p}(I_p)=C^3$。取 R66 的实际三次角色 $\eta$ 及准确导子 $c$。若 $h(\mathcal O_c)=3$，则
$$\boxed{P_\eta\ne0,\qquad
\exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.}\tag{90.1}$$
这里不要求 $M<3p$。证明使用实际 Frobenius 的整数迹和三次商值，把上表剩余的三例排除；没有假定一般类域字符都能来自椭圆曲线。

因此 R69/R72 的实际秩零商及尖点浸入在此分支适用。若该实际分支存在非 exceptional 分母素数，则
$$\boxed{h(\mathcal O_c)\ge6.}\tag{90.2}$$
这是对环类数三这一子问题的完成；它未排除更大的环类数、exceptional 分母或完整 Cartan 惯性。

## 2. 为什么类数三把周期问题化成线性三次方

选择一个具有 $\mathcal O_c$ 复乘的复椭圆曲线，在 $p$ 上方约化，令 $R$ 为其超奇异约化的最大自同态环。Deuring 的理想对应把 $R$ 的右理想类与 $\overline{\mathbb F}_p$ 上超奇异椭圆曲线的同构类识别；后者由 $j$ 不变量区分。环类群对 CM 曲线的作用与约化后的理想作用相容。因此三个类对应的 Brandt 基向量恰是三个 CM $j$ 值的约化。

这一步使用的是**右理想类**，不是只取左序的共轭类型。CM 序可能非极大，但 $p\nmid c$，相同的可逆理想作用及约化相容性仍成立。嵌入仍最优：在 $\ell\ne p$ 的 Tate 格上好约化保持原 CM 序，在 $p$ 处 $p\nmid c$ 使该序已极大，故 $R\cap K=\mathcal O_c$；这也是 R80 所用的最优性论证。可先在此约化整环中计算，再使用完整 Brandt 谱与 CST 公式传输至其他容许整环。

群 $\operatorname{Pic}(\mathcal O_c)$ 的阶为三，$\eta$ 在三个类上的值恰为 $1,\zeta_3,\zeta_3^2$。任一纤维的周期系数为这三个数的某个子和，只有空集和全集的子和为零。故
$$P_\eta=0
\quad\Longleftrightarrow\quad
\text{三个 CM 类约化到同一个超奇异 }j.\tag{90.3}$$

设类多项式
$$H_{-M}(X)=X^3+A_MX^2+B_MX+C_M\in\mathbb Z[X].$$
由 (90.3)，周期消失等价于其模 $p$ 为 $(X-j)^3$。此共同根自动属于 $\mathbb F_p$，因为 $p\ne3$ 且 $j\equiv-A_M/3$。定义
$$G_M=\gcd(A_M^2-3B_M,\ A_M^3-27C_M)>0.$$
于是有完全整数的判据
$$\boxed{P_\eta=0\quad\Longleftrightarrow\quad p\mid G_M.}\tag{90.4}$$
这里始终保留 $p>37$、$p\nmid M$ 和惰性条件。

$P_\eta$ 次数为零。素水平 Brandt 模的次数零部分完全分解为层 $p$ 的权二新形式的特征线；Cai–Shu–Tian Theorem 1.2 在每条特征线上给中心值等于正的非零常数乘周期投影的平方范数。因此所有中心值全零等价于 $P_\eta=0$，得到定理 90.1 的前两个条件等价。该方向不只使用非消失蕴含。

## 3. 原始导子的完整有限清单

扩张可逆理想给满射
$$\operatorname{Pic}(\mathcal O_c)\twoheadrightarrow\operatorname{Cl}(\mathcal O_K),$$
所以 $h_K$ 只能为一或三。

若 $h_K=3$，两个类群同阶，上述满射为同构。任何三次角色都经极大序类群分解，原始性因而迫使 $c=1$。Watkins 已发表的无条件分类给 $h_K=3\Rightarrow D\le907$，共有十六个域。对这个有限区间完整枚举 primitive 约化正定二元型，得到
$$D=23,31,59,83,107,139,211,283,307,331,379,499,547,643,883,907.$$

若 $h_K=1$，九个基本判别式绝对值为
$$3,4,7,8,11,19,43,67,163.$$
此时 $c>1$。令 $u_K=[\mathcal O_K^\times:\{\pm1\}]\in\{1,2,3\}$，环类数公式给
$$3u_K=\prod_{q^e\parallel c}q^{e-1}\bigl(q-\chi_K(q)\bigr).\tag{90.5}$$
由各因子至少相应的 Euler 因子，$\phi(c)\le9$；而
$$\frac{\phi(c)^2}{c}
=\prod_{q^e\parallel c}q^{e-2}(q-1)^2\ge\frac12,$$
所以 $c\le162$。这是导子枚举的证明界，不是经验搜索截断。

也可以直接分解 (90.5)：对 $D\ne3,4$，右边等于三，仅可能 $c=2$ 且二惰性；对 $D=4$ 右边为六，无解；对 $D=3$ 右边为九，只有 $c=6,9$。所有原始非极大序恰为

| $D$ | $c$ | $M$ |
|---:|---:|---:|
| 11 | 2 | 44 |
| 19 | 2 | 76 |
| 3 | 6 | 108 |
| 43 | 2 | 172 |
| 3 | 9 | 243 |
| 67 | 2 | 268 |
| 163 | 2 | 652 |

每个角色确实原始：所有准确小于 $c$ 且整除 $c$ 的导子所对应环类群均无三阶商。总计二十三个序；判别式 $-92,-124$ 的类数虽也为三，其角色降至导子一，所以不能重复列入本表。

## 4. 严格计算和完整素因子支集

对每个 $M$，证书枚举全部约化型 $(a,b,d)$，满足
$$b^2-4ad=-M,\quad |b|\le a\le d,\quad
b\ge0\text{ 当 }|b|=a\text{ 或 }a=d,$$
以及 $\gcd(a,b,d)=1$。每个型给
$$\tau=\frac{-b+i\sqrt M}{2a},\qquad
H_{-M}(X)=\prod_{[a,b,d]}(X-j(\tau)).$$

`verify_class_number_three_periods.py` 使用 Arb 的严格复数球，在512位精度下计算该乘积。每个系数的实部球含有唯一整数、半径严格小于 $2^{-200}$，虚部含零且绝对值上界小于 $2^{-200}$。复乘理论已知这些系数属于 $\mathbb Z$，因此唯一整数就是精确系数；没有把高精度近似后取整当成证明。

随后仅以整数算术求 $G_M$，对不超过1000的素数逐项除尽，并验证余数为一。所有素因子实际上不超过59。完整系数、素因子指数及约化型保存在 JSON；下表列全部素因子支集。

| $M$ | $G_M$ 的全部素因子 | 大于37且惰性的因子 |
|---:|---|---|
| 23 | 5, 7 | 无 |
| 31 | 3, 13 | 无 |
| 44 | 2, 7, 13 | 无 |
| 59 | 2, 13 | 无 |
| 76 | 2, 3, 13 | 无 |
| 83 | 2, 3, 5, 13 | 无 |
| 107 | 2, 5, 7 | 无 |
| 108 | 2, 3, 5 | 无 |
| 139 | 2, 3, 17, 19 | 无 |
| 172 | 2, 3, 5, 7 | 无 |
| 211 | 2, 3, 7 | 无 |
| 243 | 2, 3, 5, 17 | 无 |
| 268 | 2, 3, 5, 7, 11, 13 | 无 |
| 283 | 2, 3, 5, 17 | 无 |
| 307 | 2, 3, 5, 13 | 无 |
| 331 | 2, 3, 7, 13 | 无 |
| 379 | 2, 3, 7, 13, 43 | 43 |
| 499 | 2, 3, 7, 11, 13, 19 | 无 |
| 547 | 2, 3, 5, 7 | 无 |
| 643 | 2, 3, 5, 13, 17, 19, 41 | 41 |
| 652 | 2, 3, 5, 7, 13, 23, 29 | 无 |
| 883 | 2, 3, 5, 7, 19, 47, 59 | 47, 59 |
| 907 | 2, 3, 5, 7, 11, 17, 29 | 无 |

四个实际约化恒等式为
$$\begin{aligned}
H_{-379}(X)&\equiv(X-41)^3\pmod{43},\\
H_{-643}(X)&\equiv(X-28)^3\pmod{41},\\
H_{-883}(X)&\equiv(X-9)^3\pmod{47},\\
H_{-883}(X)&\equiv(X-28)^3\pmod{59}.
\end{aligned}\tag{90.6}$$
这证明定理 90.1。独立运行 PARI/GP 的 CRT 类多项式算法得到相同的全部二十三个精确多项式。

## 5. 实际表示提供额外的 Frobenius 约束

以下使用 R63 已独立证明的全局和局部接口。对本题实际 $\lambda:G_K\to\mathbb F_{p^2}^\times$，选定二次方向后
$$\mu=\lambda^{12},\qquad
\mu((\alpha))=\widetilde\alpha^{12}\quad(p\nmid N\alpha).\tag{90.7}$$

若 $q$ 在 $K$ 分裂且 $q\not\equiv1\pmod p$，局部残余像在 $C$ 排除潜在乘法约化。R63 §3 构造了循环总分歧的好约化扩张，剩余域保持 $\mathbb F_q$。其真正的 Frobenius 根 $\beta\in\mathbb F_{p^2}$ 满足
$$\beta+\beta^p\equiv a_q,\quad
\beta^{p+1}\equiv q,\quad |a_q|\le2\sqrt q,\quad
\beta^{12}=\mu(\mathfrak q).\tag{90.8}$$
这里 $a_q$ 是整数，不能换成任意模 $p$ 元；允许 $E$ 在 $q$ 原本为加性约化。

设 $h_K=3$、$\mathfrak q$ 非主，并取
$$\mathfrak q^3=(\alpha),\qquad
\alpha=(T+Y\sqrt{-D})/2,\qquad T^2+DY^2=4q^3.$$
由 (90.7)–(90.8)，有 $\beta^{36}=\widetilde\alpha^{12}$。定义整数递推
$$S_0(t,n)=2,\quad S_1(t,n)=t,\quad
S_{r+1}(t,n)=tS_r(t,n)-nS_{r-1}(t,n).$$
取迹给必要条件
$$\boxed{S_{36}(a_q,q)\equiv S_{12}(T,q^3)\pmod p.}\tag{90.9}$$
换二次方向不改变该条件。下列所选 $q$ 均分裂、与 $Dp$ 互素、满足 $q\not\equiv1\pmod p$。所列 $\alpha$ 的坐标不同时被 $q$ 整除，故其理想仅支撑在 $q$ 的一支，确为该素理想的三次方。又因 $4q<D$，不存在范数 $q$ 的非实二次整数，故该素理想非主。

| $D$ | $p$ | $q$ | $(T,Y)$ | $S_{12}(T,q^3)\bmod p$ | (90.9) 中剩余的 $a_q$ |
|---:|---:|---:|---|---:|---|
| 379 | 43 | 5 | $(11,1)$ | 21 | 无 |
| 643 | 41 | 23 | $(131,7)$ | 17 | 无 |
| 883 | 47 | 29 | $(233,7)$ | 45 | $\pm4,\pm10$ |
| 883 | 59 | 17 | $(137,1)$ | 34 | 无 |

例如第二行 $a_q=0,1,\ldots,9$ 的左边依次为
$$20,22,13,22,13,1,13,19,20,1,$$
没有17；第四行 $a_q=0,1,\ldots,8$ 时为
$$11,40,49,11,37,16,57,49,49,$$
没有34。偶次迹关于 $a_q$ 为偶函数，已经覆盖负迹。

表中三条已排空的行不需要小惯性假设；唯一仍存活的 $(D,p)=(883,47)$ 则必须保留下面的真实三次商值。

## 6. $(883,47)$：被十二次幂丢掉的三次信息完成排除

在定理 90.2 的这个例子，$c=1,h_K=3$，$\eta$ 是整个类群的一个忠实三阶角色。因为 $\mathfrak q\mid29$ 非主，
$$\eta(\mathfrak q)\ne1.\tag{90.10}$$

$\eta$ 在 $q$ 未分歧，故改变 Frobenius 的惯性提升不改变其值；总分歧好约化扩张中的 Frobenius 仍给同一 $\eta(\mathfrak q)$。由 $\eta=\vartheta\circ\lambda$，其中 $\vartheta$ 的核是 $C^3$，真正的根 $\beta$ 必须**不是** $\mathbb F_{47^2}^\times$ 中的立方。

另一方面，(90.9) 只容许 $a_{29}=\pm4,\pm10$。在
$$\mathbb F_{47^2}=\mathbb F_{47}[s],\qquad s^2=10$$
中，十为非平方，全部满足这些迹且范数为29的根是
$$\pm(5\pm3s),\qquad \pm(2\pm16s).$$
但有直接有限域恒等式
$$\boxed{(11-15s)^3=5+3s,\qquad
(10-7s)^3=2+16s.}\tag{90.11}$$
二次共轭和乘以 $-1=(-1)^3$ 保持立方性质，所以八个根全部为立方。与 (90.10) 矛盾。

这排除了最后一行可能性。实际小惯性又要求 $p\equiv2,5\pmod9$，因此一般表中的 $(379,43)$ 本来就不在其范围；其余三例现已由实际条件全部排除，定理 90.2 得证。

## 7. 证书、复算及准确边界

相关文件：

- `scripts/verify_class_number_three_periods.py`：枚举全部基本判别式与准确导子，用严格球算术确定所有类多项式，验证完整 $G_M$ 分解、四个线性三次方以及实际 Frobenius 排除。
- `scripts/data/class_number_three_periods.json`：完整有限证书，SHA256 `e91af69048622711f061c8a8ace7aa45c0f9bf3da7e1865204907cfc32fca093`。
- `scripts/class_number_three_polynomials.gp`：独立 CRT 算法重新计算二十三个类多项式，根会话已逐项比较一致。

在课题目录运行：

```bash
python -B scripts/verify_class_number_three_periods.py
gp -q -s 268435456 scripts/class_number_three_polynomials.gp
```

本篇没有构造任何异常椭圆曲线。一般周期零例是真实的类域及中心值现象；实际排除额外使用了椭圆曲线的全局主理想公式、局部好约化整数迹及其原三次角色。仅用类多项式或仅用十二次幂，在 $(883,47)$ 处都不够。

## 来源

- M. Watkins, *Class numbers of imaginary quadratic fields*, Mathematics of Computation **73** (2004), 907–938；[作者全文](https://magma.maths.usyd.edu.au/~watkins/papers/smallcn.pdf)，末表给 $h_K=1,3$ 的完整数量与最大判别式。此处只以已发表的全局完备界为外部输入，具体有限清单和多项式全部重算。
- L. Cai, J. Shu, Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra & Number Theory **8** (2014), 2523–2572；[期刊全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)，Theorem 1.2 及其前的 Brandt 模、周期、正定配对定义。
- J. Voight, *Quaternion Algebras*, Springer, 2021；[第42章](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)，Deuring 的超奇异曲线与理想类对应。约化相容及任意序传输也见 [R76](R76-three-point-fibres-and-cubic-nonvanishing.md)、[R80](R80-three-colour-collapse-and-class-number-one-nonvanishing.md)。
- [R63](R63-all-prime-classes-and-quotient-discriminant-growth.md) §§2–3：实际十二次幂主理想公式和剩余域不变的好约化扩张；[R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际三次角色及小惯性同余；[R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)、[R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：非消失到分母必要条件。
- [FLINT 的模函数接口](https://flintlib.org/doc/acb_modular/index.html)、[python-flint 复数球](https://python-flint.readthedocs.io/en/latest/acb.html)和[唯一整数提取](https://python-flint.readthedocs.io/en/latest/arb.html)：严格球包围和 `unique_fmpz` 的接口；不是未认证的十进近似。
