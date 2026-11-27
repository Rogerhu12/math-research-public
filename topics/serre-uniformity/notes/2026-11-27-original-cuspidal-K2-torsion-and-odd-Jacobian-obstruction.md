# 原全尖点规范下的整 $K_2[p]$ 剩余与奇 Jacobian 扭点

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126。

## 0. 范围

本札记只确定一个整 $K$ 理论剩余类的准确去向。它不证明原 Siegel 单位的指定杯积为零，不构造新的中央覆盖，也不提供新的有理点排除。

设 $p>37$，$K=\mathbf Q(\zeta_p)$，$X/\mathbf Q$ 为原
$X_{\mathrm{ns}}^+(p)$，$J=\operatorname{Jac}(X)$。
原几何尖点集 $\mathscr C$ 在 $K$ 上分裂，大小
$m=(p-1)/2$，且为 $\Delta=\operatorname{Gal}(K/\mathbf Q)$ 稳定的集合。
这些实际曲线与尖点来源仍按 R1062、R1064、R1067。
下面的论证一般适用于有 $K$ 有理点的光滑、射影、几何整曲线，以及任何大小与 $p$ 互素的 Galois 稳定有理点集。

记 $F=K(X)$。本文的 $K_2(F)$ 是域的整 Milnor $K_2$，与 Quillen $K_2$ 相同；用加法记符号。
定义

$$
K_{2,\mathrm{nr}}(F)[p]
=
\{\alpha\in K_2(F)[p]:
 \partial_x\alpha=1\text{ 对每个 }x\in X_K^{(1)}\}.
$$

这里 $\partial_x$ 为乘法记号的 tame symbol。
全文不把此群改成 $K_2(F)/p$。

## 1. 实际使用的 Suslin 输入

只使用以下两项。

1. 对含原始 $p$ 次单位根 $\zeta$ 的域 $F$，每个
   $\alpha\in K_2(F)[p]$ 都可写作 $\{\zeta,u\}$，$u\in F^\times$。
2. 若 $F_0$ 为 $F$ 的常数域且 $\{\zeta,u\}=0$，则
   $u=cw^p$，其中 $c\in F_0^\times$、$w\in F^\times$。
   并且常数符号 $\{\zeta,c\}$ 若在 $K_2(F)$ 中为零，
   就已在 $K_2(F_0)$ 中为零。

精确可读来源是 C. Weibel，*The K-book*，Chapter III，
Theorem 6.8 及 Remark 6.8.1，该作者 PDF 第55–56页：
[作者全文](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf)。
Theorem 6.8 附证明；Remark 6.8.1 明确给出第二项并引 Suslin。
原论文书目为 A. A. Suslin，*Torsion in $K_2$ of fields*，
$K$-Theory **1** (1987), 5–29，
[DOI](https://doi.org/10.1007/BF00533985)。
本次未成功读取原论文 PDF，故不声称已逐页核过原论文；
上述实际核读限于作者 K-book 的精确表述与所附证明。

由于 $X_K$ 几何整，$K$ 在 $F$ 中代数闭；本处第二项的常数域正是 $K$。
特征为零，$p$ 可逆，所需 $\mu_p\subset K$ 均成立。

## 2. 未分歧剩余的精确正合列

存在自然的 $\Delta$ 等变正合列

$$
0\longrightarrow K_2(K)[p]
 \longrightarrow K_{2,\mathrm{nr}}(F)[p]
 \xrightarrow{\;\pi\;}
 \mu_p\otimes_{\mathbf F_p}J(K)[p]
 \longrightarrow0.
\tag{1}
$$

这里 $\mu_p$ 视为一维 $\mathbf F_p$ 向量空间。

固定 $\zeta=\zeta_p$，写 $\alpha=\{\zeta,u\}$。
对闭点 $x$，

$$
\partial_x\{\zeta,u\}=\zeta^{v_x(u)}.
$$

因为 $K\hookrightarrow\kappa(x)$，该值为 $1$ 当且仅当
$p\mid v_x(u)$。所以未分歧性等价于

$$
\operatorname{div}(u)=pD
\tag{2}
$$

对某个 $K$ 有理次数零除子 $D$ 成立。定义

$$
\pi(\{\zeta,u\})=\zeta\otimes[D].
\tag{3}
$$

若同一符号也写成 $\{\zeta,u'\}$，则 Suslin 的第二项给
$u/u'=cw^p$。因此对应的 $D-D'$ 为主除子，(3) 定义良好。
它对乘法及 $\zeta$ 的更换均相容，故不依赖所选基 $\zeta$。

若 $[D]=0$，可写 $D=\operatorname{div}(w)$，于是
$u=cw^p$，$\alpha=\{\zeta,c\}$，得到核等于常数像。
常数的单射由 §1 第二项及第一项给出。

反之，有 $K$ 有理点保证
$\operatorname{Pic}^0(X_K)=J(K)$：Picard 的 Brauer 障碍被该点的评价消去。
因此任意 $P\in J(K)[p]$ 可由 $K$ 有理次数零除子 $D$ 表示，
且 $pD=\operatorname{div}(u)$，所以 (3) 满射。
这一步不以一个仅几何存在的除子冒充 $K$ 有理除子。

若 $\sigma(\zeta)=\zeta^{\omega(\sigma)}$，则

$$
\sigma\{\zeta,u\}
=\{\zeta,(\sigma u)^{\omega(\sigma)}\},
$$

其对应的除子类为 $\omega(\sigma)\sigma[D]$。
这正是 (1) 右端的 $\mu_p$ 张量作用，不能去掉该扭曲。

## 3. 每个尖点的 specialization 与全尖点平均

给定 $b\in\mathscr C$，在 $b$ 取 $K$ 有理局部参数 $t_b$。
由 (2)，写

$$
u=t_b^{pn}v,\qquad v\in\mathcal O_{X_K,b}^{\times}.
$$

定义

$$
\operatorname{sp}_b(\alpha)=\{\zeta,v(b)\}
\in K_2(K)[p].
\tag{4}
$$

此定义同时不依赖参数和符号代表。

参数改变 $t_b'=a t_b$，其中 $a$ 是局部单位，使 $v(b)$
乘以 $a(b)^{-pn}$；其与 $\zeta$ 的符号为零。
若 $u/u'=cw^p$，则写 $w=t_b^k w_0$ 后，
两个 regularized leading 值的比为 $c\,w_0(b)^p$。
因 $\{\zeta,c\}=0$ 已在 $K_2(K)$ 中成立，(4) 的差为零。
这也证明其为群同态。

对常数 $\alpha$，$\operatorname{sp}_b(\alpha)=\alpha$。
各 $\operatorname{sp}_b$ 随 Galois 作用准确重标。
由于 $p\nmid m$，定义

$$
s_{\mathscr C}=\frac1m
 \sum_{b\in\mathscr C}\operatorname{sp}_b
 :
 K_{2,\mathrm{nr}}(F)[p]\longrightarrow K_2(K)[p].
\tag{5}
$$

这里 $1/m$ 是在指数 $p$ 群上的逆标量。
(5) 是 $\Delta$ 等变的常数项 retraction。
故

$$
K_{2,\mathrm{nr}}(F)[p]
 =
K_2(K)[p]\oplus\ker s_{\mathscr C},
\qquad
\ker s_{\mathscr C}
 \simeq\mu_p\otimes_{\mathbf F_p}J(K)[p].
\tag{6}
$$

全尖点平均避免了任选单个尖点造成的 Galois 规范偏移。
它使用与原全尖点 leading 规范一致的点集，但并不声称任何尚未计算的 Siegel 剩余已经满足 $s_{\mathscr C}=0$；
必须实际减去 (5) 的常数项。

## 4. 偶剩余的真实目标是奇扭点

设 $\alpha$ 已按 (5) 规范，即 $s_{\mathscr C}(\alpha)=0$。
若 $\alpha$ 在 $\Delta$ 的特征 $\theta$ 上，则其对应 Jacobian 类在

$$
J(K)[p]_{\theta\omega^{-1}}
\tag{7}
$$

上。特别，若复共轭固定 $\alpha$，则复共轭在 $\mu_p$ 上作用为 $-1$，
所以 (6) 将 $\alpha$ 对应到

$$
J(K)[p]^-.
\tag{8}
$$

原尖点扭点模块 $V=\operatorname{Cusp}[p]$ 来自实尖点域，
因此是偶模块。已付的 $V$ 维数、good 角色、原 Kummer 标签及局部满射，
均不自动控制 (8)。
不能用原 $V$ 的计算断言此规范化剩余为零。

若未来对某个指定 $\theta$ 确实证明 (7) 为零，
则相应规范化未分歧整 $K_2[p]$ 剩余为零；
这才是 (6) 可消费的明确消去条件。

## 5. 对原四阶任务的适用边界

要将某个原 Siegel/Manin 剩余放入 (1)，仍须逐项证明：

- 它是原函数域上的**整** $K_2$ 元素，且已被 $p$ 杀掉；
- 每个闭点的 tame symbol 都为 $1$，包括全部尖点；
- 它的实际 $\Delta$ 作用及 (5) 的常数规范已计算；
- 所需的特定奇 Jacobian 扭点分量已消去，或剩余本身已另行计算为零。

若只知某元素被 $p^a$ 杀掉，(1) 只能先应用于其 $p^{a-1}$ 倍，
不能因为 $\mu_p\subset K$ 就假设 $\mu_{p^a}\subset K$ 或直接复制 (1)。

即使某个整 $K_2$ 关系已为零，原非阿贝尔覆盖仍要求明确连接到
所选原 Kummer 类、相容的低阶 cochain、算术下降及未分歧条件。
这里没有把 integral $K_2[p]$ 的核判据改成 $K_2/p$ 的 Brauer norm 判据，
也没有把有理系数 Manin 关系的 $p$ 分母视为可逆。
四阶中央覆盖与原同点排除仍未获得。

## 6. 复核

global_route 给出上述正合列、全尖点平均与角色计算；
o2_high_coefficient 已亲读 Weibel III Theorem 6.8 / Remark 6.8.1，
root 亦亲读这两项，并独立纸核 §2–4 的正合性、参数无关性与 $\mu_p$ 扭曲。
本札记不包含数学程序执行。
