# 原 Euler 原函数不能直接取得普通有限阶分布呈示

日期：2026-11-14。**状态：已证明；范围为原非零有界测度及有限阶分布。**

本记支付 R598 的两个固定 Euler 原函数在普通地点的一项具体边界。其中央投影与原完整 Newton 导数的惰性关系保持不变；本记只排除将未投影 Euler 原函数直接加入 R579 的普通有限阶格。

## 1. 原 Amice 规范和命题

固定一个已支付原测度呈示的好普通地点。设 $\Omega\ne0$ 是原普通周期，
$\nu$ 是 $\mathbf Z_p$ 上的非零有界 $\mathbf C_p$ 值测度，并保持
$$
\mathcal A_\nu(T)=A\bigl(\Omega\log(1+T)\bigr),\qquad A(0)=0.
\tag{1}
$$
令
$$
U(z)=\int_0^z A(t)\,\frac{dt}{t},\qquad zU'(z)=A(z).
\tag{2}
$$
这里积分的分母是 Taylor 指标，不是 $D_z$ 原函数的平移型分母。

**命题。** 不存在任何有限整数 $r$ 以及对标准 $C^r$ 差商范数连续的分布 $\tau$，使
$$
\mathcal A_\tau(T)=U\bigl(\Omega\log(1+T)\bigr).
\tag{3}
$$
给 $U$ 添加任意固定多项式也不能使 (3) 成为有限阶分布的 Amice 变换。

## 2. 所用范数、算子连续性和实际密度

保持 [R579 §3](../results/R579-nine-coordinate-ordinary-divided-difference-and-saturated-jet-budget.md) 的全部节点差商范数
$$
\|f\|_{r,p}
=\max_{0\le j\le r}
 \sup_{x_0,\ldots,x_j\in\mathbf Z_p}
 |f^{[j]}(x_0,\ldots,x_j)|_p.
\tag{4}
$$
先在多项式上取此范数，再取完备化。R579 的完整重合节点恒等式给
$$
(f')^{[j]}(x_0,\ldots,x_j)
=\sum_{i=0}^j
 f^{[j+1]}(x_0,\ldots,x_i,x_i,\ldots,x_j),
$$
故
$$
\|f'\|_{r,p}\le\|f\|_{r+1,p}.
\tag{5}
$$
差商乘积律又给 $\|xg\|_{r,p}\le\|g\|_{r,p}$。所以
$$
\boxed{x\partial_x:C^{r+1}\longrightarrow C^r
\quad\text{连续，范数至多一。}}
\tag{6}
$$
这不是仅用逐点普通导数定义一个较弱范数。

这里所需的局部常值函数确实在多项式的 $C^{r+1}$ 完备化中。给出一个直接证明，避免从多项式恒等式未经密度论证就跳到小球测试。

设 $f$ 模 $M=p^N$ 周期，写其 Mahler 系数 $a_n=\Delta^nf(0)$。其生成函数准确为
$$
\sum_{n\ge0}a_n Z^n
=\frac{\displaystyle\sum_{j=0}^{M-1}
 f(j) Z^j(1+Z)^{M-1-j}}
 {(1+Z)^M-Z^M}.
\tag{7}
$$
分母的常数项为一，所有非恒系数均被 $p$ 整除，故它的倒数在某个半径严格大于一的闭盘解析。于是 $a_n$ 指数衰减。另一方面，R579 的下降阶乘全差商界给
$$
\left\|\binom{x}{n}\right\|_{r+1,p}
\le p^{\sum_{a\ge1}\min(r+1,\lfloor n/p^a\rfloor)}
\le p^{r+1}(n+1)^{r+1}.
\tag{8}
$$
因此 $\sum a_n\binom{x}{n}$ 在 (4) 的 $r+1$ 阶范数收敛；其一致极限是原局部常值 $f$。特别每个小球的示性函数都在该完备化中，且其导数为零。

## 3. 完整对偶矛盾

假设 (3) 成立。置 $u=\log(1+T)$，并只比较原点形式级数：
$$
\mathcal A_\tau(e^u-1)=\tau(e^{xu})
=U(\Omega u),\qquad
\mathcal A_\nu(e^u-1)=\nu(e^{xu})
=A(\Omega u).
$$
由 (2)，$u\partial_uU(\Omega u)=A(\Omega u)$，所以每个 $n\ge0$ 都满足
$$
n\,\tau(x^n)=\nu(x^n).
\tag{9}
$$
周期 $\Omega$ 的幂已经在两边准确约去。故对所有多项式 $f$，
$$
\boxed{\tau(xf')=\nu(f).}
\tag{10}
$$
$\tau$ 对 $C^r$ 连续，(6) 说明左边对 $C^{r+1}$ 连续；有界测度 $\nu$ 的右边对一致范数连续，因而也对 $C^{r+1}$ 连续。由 §2，(10) 因此适用于每个局部常值函数。

现在取任意小球的示性函数 $f=\mathbf1_{a+p^N\mathbf Z_p}$。有 $f'=0$，所以
$$
\nu(a+p^N\mathbf Z_p)=0
\quad\text{对全部 }a,N.
\tag{11}
$$
局部常值函数在连续函数的一致范数中稠密，有界性于是迫 $\nu=0$，与假设矛盾。这证明命题。

若把 $U$ 换成 $U+Q$，$Q$ 为多项式，则 (9) 的右边只增加一个由原点 Dirac 导数组成的有限阶泛函；$u\partial_uQ(\Omega u)$ 没有常数项，所以该附加泛函在所有局部常值函数上仍为零。取小球后还是 (11)。因此有限 Taylor 或 Dirac 修正也不能绕过此障碍。

## 4. 两条原来源的适用范围

R579 的原 $S_{34},T_{72}$ 在好普通地点都有非零有界测度呈示；非零可由其固定首项 $z^6$ 直接确认。故 R598 的
$$
U_{34}=\int_0^z S_{34}(t)\,\frac{dt}{t},\qquad
U_{72}=\int_0^z T_{72}(t)\,\frac{dt}{t}
$$
均不满足任何有限 $C^r$ 分布呈示。不能直接把它们添到 R579 的原九坐标格，并沿用那里的普通差商和全卷积成本。

这与 R575 的固定 $D_z$ 原函数不冲突：$D_z$ 在指数变换侧对应乘测试变量，Euler 算子 $zD_z$ 则对应本记的 $x\partial_x$，后者杀掉所有局部常值测试。

本记也不否定 R598 已付的真正 $\Pi_0$ 中央投影延拓条件，不讨论更大类别的超分布或另有补偿的投影呈示。原完整中央导数非零与主无穷素数问题仍须由其实际算术关系推进。
