# R6. 固定虚二次特征下，非零惰性 Frobenius 迹可以任意迟出现

**状态：已证明。** 这是对一种可能证明路线的限制，属于中间结论；没有构造 Serre 一致性的反例，也没有假定下面的曲线具有异常模 $p$ 像。

日期：2026-11-12。会话：serre-uniformity-astra / frobenius。

## 1. 陈述

对椭圆曲线 $E/\mathbb Q$ 的良好约化素数 $q$，采用约定
$$
a_q(E)=q+1-\#E(\mathbb F_q).
$$
令 $\chi_{-4}$ 为 $\mathbb Q(i)/\mathbb Q$ 的二次特征；对奇素数，$\chi_{-4}(q)=(-1/q)$。定义
$$
q_{\mathrm{nz}}(E,\chi_{-4})
=\min\{q:\ q\text{ 为奇的良好约化素数},\ q\equiv3\pmod4,\ a_q(E)\ne0\},
$$
若集合为空，暂将最小值记为 $+\infty$。

**定理。** 令 $X\ge5$，并设
$$
M_X=\prod_{\substack{q\le X\\q\text{ 奇素数}}}q,
\qquad E_X:\ y^2=x^3-x+4M_X.
$$
则：

1. $E_X/\mathbb Q$ 无复乘。
2. 每个奇素数 $q\le X$ 都是 $E_X$ 的良好约化素数，并且其约化与 $E_0:y^2=x^3-x$ 相同。
3. 对每个 $q\le X$、$q\equiv3\pmod4$，都有 $a_q(E_X)=0$。特别地，$q_{\mathrm{nz}}(E_X,\chi_{-4})>X$。
4. 对任意无复乘的 $E/\mathbb Q$，上面定义的 $q_{\mathrm{nz}}(E,\chi_{-4})$ 都有限。因此，这些最小素数确实是一个无界的有限整数族。
5. 对有理数的绝对对数高度 $h$，有精确公式
   $$
   h(j(E_X))=\log(108M_X^2-1).
   $$
   由素数定理，$h(j(E_X))=2X+o(X)$，从而
   $$
   \liminf_{X\to\infty}
   \frac{q_{\mathrm{nz}}(E_X,\chi_{-4})}{h(j(E_X))}\ge\frac12.
   $$

因此，即使固定二次特征为 $\chi_{-4}$，也不存在只依赖“$E$ 无复乘”的绝对素数上界；更不存在对所有无复乘曲线均成立的 $q_{\mathrm{nz}}(E,\chi_{-4})=o(h(j(E)))$ 上界。

## 2. 曲线不奇异、无复乘及高度

短 Weierstrass 方程 $y^2=x^3+Ax+B$ 的不变量满足
$$
\Delta=-16(4A^3+27B^2),\qquad
j=1728\frac{4A^3}{4A^3+27B^2}.
$$
代入 $A=-1$、$B=4M_X$，得到
$$
\Delta(E_X)=64(1-108M_X^2),\qquad
j(E_X)=\frac{1728}{1-108M_X^2}.
$$
因为 $M_X\ge15$，所以分母不为零，且
$$
0<|j(E_X)|<1.
$$
复乘椭圆曲线的 $j$ 不变量是代数整数；若它属于 $\mathbb Q$，则是整数。这一标准复乘定理与上式矛盾，因此 $E_X$ 无复乘。

分母 $1-108M_X^2$ 与 $6$ 互素，而 $1728=2^6 3^3$，故上述分数已约分。分母绝对值大于分子，于是按有理数高度的定义，
$$
h(j(E_X))=\log(108M_X^2-1).
$$
若记 $\vartheta(X)=\sum_{q\le X}\log q$，则
$$
\log M_X=\vartheta(X)-\log2,
$$
并且
$$
h(j(E_X))
=2\vartheta(X)+\log27+o(1).
$$
使用已证的素数定理 $\vartheta(X)=X+o(X)$，即得所述渐近式。本结论的无界性部分不需要素数定理。

## 3. 所有指定小素数处的约化

取任意奇素数 $q\le X$。因 $q\mid M_X$，给定的整系数模型在模 $q$ 下变为
$$
y^2=x^3-x.
$$
且其判别式模 $q$ 等于 $64\ne0$，所以该模型是良好约化模型。

现在设 $q\equiv3\pmod4$，令 $\lambda_q$ 为二次特征，补定义 $\lambda_q(0)=0$。有
$$
\#E_0(\mathbb F_q)
=q+1+\sum_{x\in\mathbb F_q}\lambda_q(x^3-x).
$$
因为 $(-x)^3-(-x)=-(x^3-x)$、$\lambda_q(-1)=-1$，变量替换 $x\mapsto-x$ 把右端的特征和变为其负数。因此该和为零，$a_q(E_0)=0$。约化相同给出 $a_q(E_X)=0$。

注意，这里是整数迹严格等于零，而不只是模某个辅助素数为零。

## 4. 最小值的有限性：适用于任意非平凡二次特征

以下还证明一个独立的定性事实。

**引理。** 若 $E/\mathbb Q$ 无复乘、$\chi:G_{\mathbb Q}\to\{\pm1\}$ 非平凡，则存在无穷多个良好约化素数 $q$，使 $\chi$ 在 $q$ 不分歧，并有
$$
\chi(\operatorname{Frob}_q)=-1,\qquad a_q(E)\ne0.
$$

**证明。** 使用 Serre 已证的逐曲线开像定理，取辅助素数 $\ell\ge5$，使
$$
\bar\rho_{E,\ell}(G_{\mathbb Q})=\mathrm{GL}_2(\mathbb F_\ell).
$$
考虑有限像同态
$$
(\bar\rho_{E,\ell},\chi):G_{\mathbb Q}
\longrightarrow\mathrm{GL}_2(\mathbb F_\ell)\times\{\pm1\}.
$$

若 $\chi$ 不经 $\bar\rho_{E,\ell}$ 分解，则上述像是整个直积：投影到第一因子满射，而其核在第二因子的像是非平凡子群，故等于第二因子。这时像含有 $(I,-1)$，且 $\operatorname{tr}(I)=2\ne0$。

若 $\chi$ 经 $\bar\rho_{E,\ell}$ 分解，则得到非平凡同态
$$
\psi:\mathrm{GL}_2(\mathbb F_\ell)\to\{\pm1\}.
$$
$\mathrm{SL}_2(\mathbb F_\ell)$ 由初等幺幂矩阵生成，这些矩阵的阶为奇数 $\ell$，故 $\psi$ 在 $\mathrm{SL}_2$ 上平凡。于是 $\psi$ 经行列式分解，且只能是行列式的二次特征。由于 $\ell\ge5$，可以选非平方元 $u\in\mathbb F_\ell^\times$，使 $u\ne-1$。这时
$$
g=\operatorname{diag}(u,1)
$$
满足 $\psi(g)=-1$ 且 $\operatorname{tr}(g)=u+1\ne0$。

无论哪种情形，有限扩张 $\mathbb Q(E[\ell])K/\mathbb Q$ 的 Galois 群都含一个共轭类，其 $\chi$ 值为 $-1$，且模 $\ell$ 迹非零。Chebotarev 密度定理给出无穷多个对应的不分歧素数。排除有限个坏约化素数及 $\ell$ 后，Frobenius 迹公式给出
$$
a_q(E)\not\equiv0\pmod\ell,
$$
所以 $a_q(E)\ne0$。证毕。

取 $\chi=\chi_{-4}$ 即证明定理第 4 条。由第 3 条与高度公式，定理其余断言全部得证。

## 5. 与非分裂 Cartan 路线的精确关系

若实际的 $\bar\rho_{E,p}$ 像在非分裂 Cartan 正规化子中，令 $\varepsilon$ 为正规化子除以 Cartan 的二次特征。对良好约化素数 $q\ne p$，
$$
\varepsilon(q)=-1\quad\Longrightarrow\quad p\mid a_q(E).
$$
结合 Hasse 界，若还满足 $q<p^2/4$，则必须 $a_q(E)=0$。所以，一种充分的排除方式是对实际异常子族证明存在
$$
q<p^2/4,\quad \varepsilon(q)=-1,\quad a_q(E)\ne0.
$$

本定理排除的是把上述存在性仅归因于“无复乘”和“$\varepsilon$ 为给定虚二次特征”，并寻求绝对的有限 Frobenius 检查窗口。它**没有**排除借助异常像本身、Tate 赋值限制或模曲线算术，对实际异常子族证明更强的素数界。

作为一个额外的精确检查，本族总有 $v_2(j(E_X))=6$。因此，在 Zywina 的二次特征分歧素数必要条件中，素数 $2$ 确实属于允许集合，$\chi_{-4}$ 不会仅因其在 $2$ 分歧就被排除。但是，本族没有被证明满足所有其他异常像必要条件；尤其不能声称其分母各素因子的赋值都是同一个大素数 $p$ 的倍数。

## 6. 使用的已证外部事实与文献

- J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. **15** (1972), 259–331：逐曲线开像定理。此处只用于证明每条固定非 CM 曲线的 $q_{\mathrm{nz}}$ 有限，没有把其依赖曲线的界改成统一界。
- Chebotarev 密度定理：第 4 节仅使用定性存在性，没有使用任何不依赖扩张判别式的有效界。
- 复乘 $j$ 不变量的整性。参见 P. Habegger, *Singular moduli that are algebraic units*, Algebra & Number Theory **9** (2015), 1515–1524，开头说明此标准事实并指向 Lang 的复乘理论：[原文](https://msp.org/ant/2015/9-7/ant-v9-n7-p01-s.pdf)。
- D. Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, [作者原文](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)，Lemma 2.3 给出二次特征可能分歧的素数集合，Lemma 2.6 给出 Frobenius 迹必要条件。
- 素数定理只用于第 5 条的渐近常数 $1/2$；前四条和高度精确公式均不依赖它。
