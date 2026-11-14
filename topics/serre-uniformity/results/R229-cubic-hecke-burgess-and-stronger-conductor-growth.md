# R229：三次 Hecke 角色的小素理想与更强的实际导子增长

日期：2026-11-13。

**状态：已证明。** 本文使用 Yang 已正式发表于 Compositio Mathematica 的固定数域 Hecke Burgess 界，通过指数平滑和坏素理想的 Euler 因子填补，得到带变化排除集合的三次小非剩余素理想界。用于 R116/R225 的同一个实际三次差角色后，将八个类数一二次域的导子下界指数从 $(e^{2/3}-1)/4$ 加强为

$$\boxed{\kappa_{\rm H}=\frac23 e^{2/3}-1=0.2984893607\ldots.} \tag{229.1}$$

常数对这八个域统一，但不将一个固定数域的 Hecke 界当作变化二次判别式的绝对统一界。结论仍是实际反例的必要增长，不给导子上界。

## 1. 一般三次小素理想定理

固定一个虚二次域 $K$。令 $\chi$ 为 $K$ 上非平凡有限三次 Hecke 角色，准确理想导子为 $\mathfrak f$，并置

$$Q=\max\{3,|D_K|\,N\mathfrak f\}.$$

令 $\mathcal B$ 为包含全部 $\mathfrak f$ 支撑的有限素理想集合，并假定

$$\prod_{\mathfrak p\in\mathcal B}N\mathfrak p\le Q^A\qquad(A>0\text{ 固定}). \tag{229.2}$$

**定理 229.1。** 对每个 $\epsilon>0$，存在有效常数 $C_{K,A,\epsilon}$，使存在 $\mathfrak p\notin\mathcal B$ 满足

$$\boxed{
\chi(\mathfrak p)\ne1,\qquad
N\mathfrak p\le C_{K,A,\epsilon}
Q^{\frac{3}{8e^{2/3}}+\epsilon}.
} \tag{229.3}$$

其中 $3/(8e^{2/3})=0.1925314\ldots$。若 $\chi$ 反圆分，且 $\mathcal B$ 包含 $K/\mathbb Q$ 的分歧素理想，则所找到的素理想必位于一个分裂有理素数 $q$ 之上，且 $N\mathfrak p=q$。

本文的有效性不表示已经算出一个实用数值常数；$C_{K,A,\epsilon}$ 使用所引用 Burgess 界的固定 $K$ 常数。§2 指出在这里所需的 Eisenstein 特化中为什么没有变化角色的 Siegel 无效常数。

## 2. 完整且均匀的 Hecke 输入

Yang 的 Corollary 1.2，式 (1.3)，给任意固定数域及任意酉 Hecke 角色

$$|L(1/2,\xi)|\ll_{K,\eta}C(\xi)^{3/16+\eta}. \tag{229.4}$$

将 $\xi=\chi|\cdot|^{it}$ 代入，对虚二次域有

$$\boxed{|L(1/2+it,\chi)|
\ll_{K,\eta}Q^{3/16+\eta}(1+|t|)^{3/8+2\eta}.} \tag{229.5}$$

这是固定 $K$、同时允许导子及 $t$ 变化的界。它不要求理想导子为素数或立方自由，也不要求角色来自有理 Dirichlet 角色。

来源中这个 GL(1) 推论取 $\pi=\mathbf1\boxplus\mathbf1$，所以 $L(s,\pi\times\xi)=L(s,\xi)^2$。这也核准了指数 $3/16$，不是把 GL(2) 的 $3/8$ 原样抄到 GL(1)。作者在引言式 (1.1) 后明确包括 $t$ 扭曲。

关于有效性：一般自守表示的放大下界在作者稿 §7.1.2 引用 Rankin–Selberg 留数。在当前 $\mathbf1\boxplus\mathbf1$ 特化，可直接用固定域中的素理想计数代替该步。具体说，§3.6.4 使用的微小变形为 $\pi^\dagger=|\cdot|^{is_0}\boxplus|\cdot|^{-is_0}$，$|s_0|\ll\exp(-c\sqrt{\log C(\xi)})$。对放大长度 $L=C(\xi)^{1/4+\eta}$ 中的素理想，

$$\mu_{\pi^\dagger}(\mathfrak q)=2\cos(s_0\log N\mathfrak q)$$

在足够大且有效的阈值后绝对值至少一。剔除导子素理想至多 $O(\log Q)$ 个；固定 $K$ 的有效素理想定理给 $\gg_K L/\log L$ 个余下素理想。这提供所需的有效 $L^{1-\eta}$ 下界。其余固定域体积、局部估计、凸性上界、微小变形的复分析估计均是有效的；此特化不需要任何随 $\chi$ 变化的实角色 $L(1,\chi_0)$ 下界。因此这里可保留有效常数。没有主张该常数对无界变化的 $K$ 绝对统一。

## 3. 填补坏素理想，控制全部变化支撑

定义一个处处取三次单位根值的完全乘性函数

$$\widetilde\chi(\mathfrak p)=
\begin{cases}1,&\mathfrak p\in\mathcal B,\\
\chi(\mathfrak p),&\mathfrak p\notin\mathcal B.
\end{cases}$$

在 $\Re s>1$，其 Dirichlet 级数是

$$\widetilde L(s)=L(s,\chi)G_{\mathcal B}(s),\qquad
G_{\mathcal B}(s)=
\prod_{\mathfrak p\in\mathcal B}
\frac{1-\chi(\mathfrak p)(N\mathfrak p)^{-s}}
{1-(N\mathfrak p)^{-s}}, \tag{229.6}$$

其中在 $\mathfrak p\mid\mathfrak f$ 按惯例置 $\chi(\mathfrak p)=0$。这个有限积在 $\Re s>0$ 全纯。对任意 $\sigma>0,\eta>0$，

$$\boxed{\sup_t|G_{\mathcal B}(\sigma+it)|
\ll_{K,A,\sigma,\eta}Q^\eta.} \tag{229.7}$$

证明完全初等。每个因子绝对值不超过 $(1+(N\mathfrak p)^{-\sigma})/(1-(N\mathfrak p)^{-\sigma})$。对足够大的 $N\mathfrak p$，该值至多 $(N\mathfrak p)^{\eta/A}$；所有小范数素理想组成固定有限积。乘起来并用 (229.2) 即得。这里没有把变化坏素理想集的因子藏入依赖于集合的常数。

对 $X\ge1$ 定义指数平滑和

$$S(X)=\sum_{\mathfrak a}\widetilde\chi(\mathfrak a)e^{-N\mathfrak a/X}.$$

Mellin 反演及 (229.6) 给

$$S(X)=\frac1{2\pi i}\int_{(2)}
L(s,\chi)G_{\mathcal B}(s)\Gamma(s)X^s\,ds.$$

$\chi$ 非平凡，所以 $L(s,\chi)$ 整；在 $\Re s>0$ 无需跨越任何极点。移线至 $1/2$，用 (229.5)、(229.7) 与 Gamma 函数的指数衰减，重新命名任意小的 $\eta$，得到

$$\boxed{|S(X)|\ll_{K,A,\eta}Q^{3/16+\eta}X^{1/2}.} \tag{229.8}$$

此步骤对一般三次角色使用复数 Euler 因子，不要求卷积系数非负；下文只用最终 $\widetilde\chi$ 的值域是 $\mu_3$。

## 4. 指数平滑的光滑理想比例

记 $A_K(T)$ 为范数不超过 $T$ 的整理想个数，$\kappa_K=\operatorname{Res}_{s=1}\zeta_K(s)>0$。固定虚二次域的格点计数给有效公式

$$A_K(T)=\kappa_KT+O_K(T^{1/2}+1). \tag{229.9}$$

令 $\Psi_K(T,y)$ 数全部素理想因子范数不超过 $y$ 的整理想。若 $y<T<y^2$，每个被删去的理想恰有一个范数大于 $y$ 的素理想因子，且该因子的指数为一，因此

$$A_K(T)-\Psi_K(T,y)=
\sum_{y<N\mathfrak p\le T}A_K(T/N\mathfrak p).$$

固定域的有效 Mertens 公式与 Chebyshev 上界给

$$\sum_{y<N\mathfrak p\le T}\frac1{N\mathfrak p}
=\log\frac{\log T}{\log y}+O_K(1/\log y),$$

$$T^{1/2}\sum_{N\mathfrak p\le T}(N\mathfrak p)^{-1/2}
\ll_K T/\log T.$$

所以，只要 $\log T/\log y$ 留在 $(1,2)$ 的固定紧子区间，

$$\Psi_K(T,y)=\kappa_KT
\left(1-\log\frac{\log T}{\log y}\right)
+O_K(T/\log y). \tag{229.10}$$

现固定 $1<u<2$，置 $y=X^{1/u}$。由

$$\sum_{\substack{\mathfrak a\text{ 为 }y\text{-smooth}}}e^{-N\mathfrak a/X}
=\int_0^\infty e^{-v}\Psi_K(Xv,y)\,dv,$$

在 $1/\log X\le v\le\log X$ 使用 (229.10)。此区间内 $\log(Xv)/\log y=u+O_u(\log\log X/\log X)$；两端尾积分由 (229.9) 控制。于是

$$\boxed{\Psi_{K,\exp}(X,y)=
\kappa_KX(1-\log u)
+O_{K,u}(X\log\log X/\log X+X^{1/2}).} \tag{229.11}$$

同时

$$A_{K,\exp}(X):=\sum_{\mathfrak a}e^{-N\mathfrak a/X}
=\kappa_KX+O_K(X^{1/2}+1). \tag{229.12}$$

全部误差均有效。此处只用 $1<u<2$ 的单一大素理想分解，不援引一个参数依赖未说明的光滑数渐近式。

## 5. 小素理想定理的完成

假设没有 $\mathfrak p\notin\mathcal B$、$N\mathfrak p\le y$ 满足 $\chi(\mathfrak p)\ne1$。则每个 $y$-smooth 理想的 $\widetilde\chi$ 值为一，而所有其他值的实部至少 $-1/2$。所以

$$\begin{aligned}
\Re S(X)
&\ge\frac32\Psi_{K,\exp}(X,y)-\frac12 A_{K,\exp}(X)\\
&=\kappa_KX\left(1-\frac32\log u\right)+o_{K,u}(X).
\end{aligned} \tag{229.13}$$

选择 $1<u<e^{2/3}$，主系数严格正。另一方面，置 $X=Q^{3/8+\delta}$，在 (229.8) 中取 $\eta<\delta/2$，则 $|S(X)|/X\to0$，矛盾。因此存在所求素理想且

$$N\mathfrak p\le Q^{(3/8+\delta)/u}$$

在一个有效阈值以上成立。给定 $\epsilon>0$，选择 $u<e^{2/3}$ 足够接近该端点、再选 $\delta>0$ 足够小，使 $(3/8+\delta)/u<3/(8e^{2/3})+\epsilon$，并用一个常数覆盖剩余有界导子范围，证明 (229.3)。

这里有界导子范围只含有限个有限阶角色及有限个满足 (229.2) 的排除集合；可用素理想枚举求所需常数。反圆分角色在惰性素理想上由 $\chi(\mathfrak p)=\chi(\overline{\mathfrak p})=\chi(\mathfrak p)^{-1}$ 及三次阶数得值一，故最后的分裂素数断言成立。

## 6. 用于同一个实际三次差角色

取 R116/R225 的八个类数一域

$$K\in\{\mathbb Q(\sqrt{-1}),\mathbb Q(\sqrt{-2}),
\mathbb Q(\sqrt{-7}),\mathbb Q(\sqrt{-11}),
\mathbb Q(\sqrt{-19}),\mathbb Q(\sqrt{-43}),
\mathbb Q(\sqrt{-67}),\mathbb Q(\sqrt{-163})\}.$$

保留实际小惯性分支、实际 Cartan 特征 $\lambda$、同一个固定 CM 参考特征 $\psi$，以及 R116 构造的

$$\chi=(\lambda/\psi)^4.$$

它是非平凡反圆分三次 Hecke 角色，R225 (225.3) 的准确理想导子为 $cp\mathcal O_K$；因此

$$Q=|D_K|p^2c^2\le C_Kp^2c^2. \tag{229.14}$$

取 $\mathcal B$ 包含 $c,p$ 上方的素理想及 R116 所需的固定集合 $S_0$。其素理想范数乘积至多 $C_Kp^2c^2$，故 (229.2) 对某个固定 $A$ 成立。没有新增依赖于 $E$ 的任意坏素数集合。

R116 的同一条实际整数迹证明：若 $q\notin S_0$、$q\nmid cp$ 在 $K$ 分裂、$q<p$ 且 $\chi(\mathfrak q)\ne1$，则

$$\boxed{p<256q^2.} \tag{229.15}$$

这由非有理 CM 范数与 $E$ 的实际迹比较得到，已在 R225 §2 保留；这里没有换到任意抽象三次角色来冒充实际角色。

**定理 229.2。** 对任意 $a<\kappa_{\rm H}$，有与这八个 $K$、实际曲线及 $c$ 无关的有效 $P_a$，使 $p>P_a$ 时

$$\boxed{c>p^a.} \tag{229.16}$$

证明可直接把 (229.3)、(229.14)、(229.15) 合并，也可如下保留严格指数余量。假设 $c\le p^a$，选择

$$\frac34(1+a)<s<\frac12e^{2/3}.$$

令 $X=p^s$、$y=\sqrt p/17$。由 (229.15)，全部范数不超过 $y$ 的好素理想均有 $\chi=1$；惰性素理想也有值一；坏素理想已经填成一。因此 (229.13) 仍适用，其中

$$u=\frac{\log X}{\log y}=2s+O_s(1/\log p)<e^{2/3}$$

在充分大 $p$ 时给 $\Re S(X)\gg_s X$。而 (229.8)、(229.14) 给

$$\frac{|S(X)|}{X}
\ll_{K,a,\eta}p^{\frac38(1+a)-\frac s2+O_a(\eta)}=o(1)$$

只要 $\eta$ 足够小，矛盾。所有域只有八个，取其有效阈值最大值便得统一 $P_a$。允许 $a<0$ 的平凡情况可直接扩大常数覆盖；有内容的范围是 $0<a<\kappa_{\rm H}$。

特别，对每个 $\epsilon>0$，

$$\boxed{
c\gg_\epsilon p^{\kappa_{\rm H}-\epsilon},\qquad
h(\mathcal O_c)\gg_\epsilon p^{\kappa_{\rm H}-\epsilon},\qquad
Dc^2\gg_\epsilon p^{2\kappa_{\rm H}-\epsilon}.
} \tag{229.17}$$

类数式的有限 Euler 乘积给 $h(\mathcal O_c)\gg_\eta c^{1-\eta}$，这在固定的八个类数一域中有效；重新分配任意小的指数损失即得中间一式。

## 7. 范围与后续缺口

定理 229.1 是固定二次域中的一般三次 Hecke 检测命题，允许变化的多项式大小坏素理想集。定理 229.2 用了同一条实际椭圆曲线的整数迹，因而比单纯构造抽象三次角色更强；它不要求 $j(E)$ 已整，也不要求某个 Fourier 特征是否 exceptional。

$K=\mathbb Q(\sqrt{-3})$ 没有被偷偷纳入：那里 R116 所用三次差角色的固定参考解释不同，R224 的实际四阶支撑路线仍须单独处理。变化 $K$ 时，Yang 的固定域常数、格点常数及 Mertens 常数不能视为绝对常数；本文没有这样做。

本结果仍允许 $c$、$b$ 及 $D$ 很大。要接到绝对 $p$ 排除，仍需与这些必要下界相矛盾的实际导子或高度上界，或直接排除整 $j$ 的实际异常表示。增加必要增长下界本身没有完成主目标。

## 主来源定位

- Liyang Yang, *Relative trace formula and twisted L-functions: the Burgess bound*, **Compositio Mathematica 162** (2026), no.11, 2591–2641，2026-10-28 online，[原刊](https://doi.org/10.1017/S0010437X26103327)，[作者稿](https://arxiv.org/abs/2305.10719)，[作者全文 HTML](https://arxiv.org/html/2305.10719v1)。作者稿 p.3 Corollary 1.2 (1.3) 为准确 GL(1) 界；p.2 的引言说明 $t$ 扭曲；§3.6.4 与 §7.1.2 给 Eisenstein 特化及放大下界，§7.3 完成主定理。本文未将其固定域常数误用到变化域。
- S. R. Garcia and E. S. Lee, *Unconditional explicit Mertens' theorems for number fields and Dedekind zeta residue bounds*, **Ramanujan J. 57** (2022), 1169–1191，[原刊](https://doi.org/10.1007/s11139-021-00435-6)，[作者稿](https://arxiv.org/html/2007.10313v4)，Theorem 1 的 (B1)、(B2) 支持固定域有效 Mertens 估计。本文 §4 直接完成所需平滑理想渐近式。
- R116/R225：同一个实际三次差角色、准确导子与实际整数迹不等式 (229.15)。本文用 Hecke 的导子整体界替换逐模 $c$ 分班的短盒估计，保留全部实际性前提。
