# R232：实际二次迹域、线性小素数障碍与更强导子增长

日期：2026-11-13。

**状态：已证明。** 保留 R116/R225/R229 的同一实际小惯性曲线、类数一商域、CM 参考及三次差角色。在下面任一条件下，实际迹的非有理部分只需一个二次实域：

$$
\boxed{p\equiv1\pmod4\quad\text{或}\quad K=\mathbb Q(i).} \tag{232.1}
$$

因此 R116 的 $p<256q^2$ 改善为 $p<9q$。结合 R229 的固定数域 Hecke Burgess 界，得到有效、对这些域统一的必要下界

$$
\boxed{c\gg_\epsilon p^{\kappa_{\rm lin}-\epsilon},\qquad
\kappa_{\rm lin}=\frac43e^{2/3}-1=1.5969787214\ldots.} \tag{232.2}
$$

这不要求 $j$ 整、不要求 nonexceptional，也不固定新的四阶惯性素数支撑。其余 $p\equiv3\pmod4$ 且 $K\ne\mathbb Q(i)$ 的分支仍只得到 R229 的指数；本文不将二次迹域论证推广到实际四次迹域。

## 1. 共同设置与实际性

设 $E/\mathbb Q$、$p>37$ 满足完整非分裂 Cartan 正规化子设置，商域 $K$ 类数一、$K\ne\mathbb Q(\sqrt{-3})$，且

$$\bar\rho_{E,p}(I_p)=C^3.$$

置 $D=|D_K|$。因此 $K$ 为 R116 的八个类数一虚二次域之一，$p$ 在 $K$ 惰性，且 $p\equiv2\pmod3$。沿用同一固定 CM 参考曲线 $A/\mathbb Q$、同向特征 $\lambda,\psi$，以及

$$\nu=\lambda/\psi,\quad \nu^{12}=\nu^{p+1}=1,\quad
\chi=\nu^4,\quad \mathfrak f(\chi)=cp\mathcal O_K. \tag{232.3}$$

把 $2,3,D_K$ 及 $A$ 的坏素数收入只依赖于 $K$ 的固定集合 $S_0$。
有限个 $p\in S_0$ 可有效收入最终常数。

若 $q\notin S_0$、$q\nmid cp$ 在 $K$ 分裂、$q<p$，且
$\chi(\mathfrak q)\ne1$，则 R116 §3 的实际全分歧循环好约化扩张给**同一个**整数迹 $a$，满足

$$|a|<2\sqrt q.$$

取 $\mathfrak q=(\alpha)$、$\alpha\bar\alpha=q$。将 CM 单位并入 $\zeta$ 后，该同一 Frobenius 给

$$
a\equiv t=\zeta\alpha+\zeta^{-1}\bar\alpha\pmod{\mathfrak P},
\qquad \zeta\in\mu_{12},\quad \zeta^4=\chi(\mathfrak q)\ne1. \tag{232.4}
$$

素数 $q$ 可以是 $E$ 的新四阶惯性素数。R116 的构造只要求 $\chi$ 在此不分歧、$A$ 好约化；没有将全部新支撑收入 $S_0$。因 $q<p$，潜在乘法情形会由同一局部 Cartan 条件迫 $q\equiv1\pmod p$，故不出现。

R116 §3 已证明 $t\notin\mathbb Q$。这里亦可直接保留其完整理由：若 $t\in\mathbb Q$，则 $\zeta\alpha$ 是 $T^2-tT+q$ 的非实根，因而生成一个虚二次域；其十二次幂 $\alpha^{12}$ 非实且生成 $K$，所以这个域只能为 $K$。遂有 $\zeta\in\mathcal O_K^\times$，而该单位群阶整除四，与 $\zeta^4\ne1$ 矛盾。$\alpha^{12}$ 非实是因为理想 $\mathfrak q^{12}$ 与 $\overline{\mathfrak q}^{12}$ 不同。

## 2. $p\equiv1\pmod4$ 时的二次实迹域

此时 $p\equiv5\pmod{12}$，故

$$\gcd(12,p+1)=6.$$

由 (232.3)，$\nu$ 的值域包含于 $\mu_6$。此外 $K\ne\mathbb Q(i)$：否则 $p$ 在 $K$ 惰性将迫 $p\equiv3\pmod4$。在其余七个允许域中，$\mathcal O_K^\times=\{\pm1\}$，所以将 CM 单位并入以后 (232.4) 中仍可取

$$\zeta\in\mu_6.$$

由于 $\zeta^4\ne1$，有 $\zeta$ 的阶为三或六。令

$$s=\zeta+\zeta^{-1}\in\{1,-1\},\qquad v=\alpha+\bar\alpha\in\mathbb Z.$$

因 $K\ne\mathbb Q(\sqrt{-3})$，双二次域 $K(\zeta_3)$ 的最大实子域 $F$ 真为二次域；$t\in F$。其非平凡共轭为

$$t'=\zeta^{-1}\alpha+\zeta\bar\alpha.$$

直接计算给

$$t+t'=sv,\qquad tt'=v^2-3q,$$

故

$$\boxed{N_{F/\mathbb Q}(a-t)=a^2-sva+v^2-3q.} \tag{232.5}$$

这是非零整数，并由 (232.4) 被 $p$ 整除。$|v|<2\sqrt q$，因为 $\alpha$ 非实。写

$$x=\frac a{2\sqrt q},\qquad y=\frac v{2\sqrt q},$$

则 $|x|,|y|<1$，而范数除以 $q$ 为

$$4x^2-4sxy+4y^2-3.$$

二次型 $x^2-sxy+y^2$ 非负，且在 $|x|,|y|<1$ 上严格小于三。因此

$$-3q\le N_{F/\mathbb Q}(a-t)<9q,$$

并且绝对值严格小于 $9q$。于是

$$\boxed{p<9q.} \tag{232.6}$$

不需要分别给模三角色与模 $p$ 同余选择不同的 Frobenius 或不同的约化曲线。

## 3. $K=\mathbb Q(i)$ 时的二次实迹域

现在 $p\equiv3\pmod4$，但

$$K(\zeta_{12})=\mathbb Q(i,\sqrt3),\qquad
K(\zeta_{12})^+=\mathbb Q(\sqrt3)$$

仍给一个二次实迹域。取 $\alpha=A+Bi$、$A,B\in\mathbb Z$，有

$$A^2+B^2=q.$$

令 $\zeta=\zeta_{12}^k$。条件 $\zeta^4\ne1$ 等价于 $3\nmid k$。逐个计算实部：

- $k$ 偶时，$t$ 形如 $\pm A\pm B\sqrt3$；
- $k$ 奇时，$t$ 形如 $\pm B\pm A\sqrt3$。

所以总可写成

$$t=\epsilon U+\delta V\sqrt3,
\qquad \epsilon,\delta\in\{\pm1\},\quad
\{U,V\}=\{A,B\},\quad U^2+V^2=q.$$

$q$ 是分裂素数且 $q\notin S_0$，所以 $A,B$ 都非零，$t$ 非有理。令 $v=2\epsilon U$，则 $v\in\mathbb Z$、$|v|<2\sqrt q$，并有

$$t+t'=v,\qquad tt'=U^2-3V^2=v^2-3q.$$

故

$$N_{\mathbb Q(\sqrt3)/\mathbb Q}(a-t)=a^2-va+v^2-3q.$$ 

与 §2 相同的二次型估计再次给非零整数范数的绝对值小于 $9q$，而 $p$ 整除该范数。因此 (232.6) 也成立。它容许 $\nu$ 或并入单位后的 $\zeta$ 实际具有十二阶。

## 4. 新的一致小素理想恒一窗口

由 §§2–3，在任一条件 (232.1) 下，若

$$q\notin S_0,\quad q\nmid cp,\quad q\text{ 在 }K\text{ 分裂},
\quad q\le \frac p{10},$$

则

$$\chi(\mathfrak q)=1. \tag{232.7}$$

否则 $p<9q\le9p/10$，矛盾。这个窗口从 R229 使用的 $\sqrt p/17$ 扩大到 $p/10$。

取 $\mathcal B$ 为 $c,p$ 及 $S_0$ 上方的全部素理想。保持 R229 的填补函数

$$\widetilde\chi(\mathfrak q)=
\begin{cases}1,&\mathfrak q\in\mathcal B,\\
\chi(\mathfrak q),&\mathfrak q\notin\mathcal B.
\end{cases}$$

因 $\chi$ 为反圆分三次角色，惰性素理想上的值也必为一。
分歧素理想已收入 $\mathcal B$。于是所有
$N\mathfrak q\le p/10$ 的素理想均满足 $\widetilde\chi(\mathfrak q)=1$。

准确导子仍是 $cp\mathcal O_K$，分析导子参数仍是

$$Q=|D_K|p^2c^2.$$

坏素理想范数乘积至多固定常数乘 $p^2c^2$，所以 R229 的变化 Euler 因子及全部常数控制完全适用；本步骤没有引入 $b$ 或其他未受控支撑。

## 5. Hecke Burgess 与导子指数

**定理 232.1。** 对每个 $0<a_0<\kappa_{\rm lin}$，存在有效常数 $P_{a_0}$，对八个允许类数一域统一，使每条满足 (232.1) 的实际曲线在 $p>P_{a_0}$ 时都有

$$\boxed{c>p^{a_0}.} \tag{232.8}$$

**证明。** 反设 $c\le p^{a_0}$。因为

$$\frac34(1+a_0)<e^{2/3},$$

可固定选取

$$\max\!\left(1,\frac34(1+a_0)\right)<s<e^{2/3}.$$

置 $X=p^s$、$y=p/10$，于是

$$u_p=\frac{\log X}{\log y}=s+O_s(1/\log p)$$

留在 $(1,e^{2/3})$ 的一个固定紧子区间。R229 §4 的指数平滑光滑理想估计对这个紧区间一致，§4 的恒一窗口遂给

$$\Re\sum_{\mathfrak a}\widetilde\chi(\mathfrak a)e^{-N\mathfrak a/X}
\ge \kappa_KX\left(1-\frac32\log u_p\right)
+O_{K,s}(X\log\log X/\log X+\sqrt X)
\gg_{K,s}X. \tag{232.9}$$

另一方面，R229 (229.8) 给任意 $\eta>0$ 下的有效上界

$$
\begin{aligned}
\frac1X\left|\sum_{\mathfrak a}\widetilde\chi(\mathfrak a)e^{-N\mathfrak a/X}\right|
&\ll_{K,a_0,\eta}Q^{3/16+\eta}X^{-1/2}\\
&\ll_{K,a_0,\eta}
p^{\frac38(1+a_0)-s/2+2(1+a_0)\eta}.
\end{aligned} \tag{232.10}
$$

由 $s>\frac34(1+a_0)$，可取足够小且固定的 $\eta>0$，使指数严格负。
这与 (232.9) 矛盾。全部阈值有效；最后对有限个 $K$ 取最大值，证明定理。$\square$

由有限小 $p$ 范围中 $c\ge1$，有对每个 $\epsilon>0$ 的统一有效推论

$$\boxed{
c\gg_\epsilon p^{\kappa_{\rm lin}-\epsilon},\qquad
h(\mathcal O_c)\gg_\epsilon p^{\kappa_{\rm lin}-\epsilon},\qquad
Dc^2\gg_\epsilon p^{2\kappa_{\rm lin}-\epsilon}.
} \tag{232.11}$$

中间一式由固定八域中的环类数公式及有效
$\varphi(c)\gg_\delta c^{1-\delta}$ 得到；重新分配任意小的指数损失。

## 6. 同一规范扭曲的导子与范围

接 R220 的同一个全局二次扭曲及其准确支撑，$M^*=D(bc)^2$，有

$$N_{\rm tw}\gg p^2DM^*T,$$

其中常数绝对，$T\ge1$；非整 $j$ 时 $T\gg p$。因此满足 (232.1) 的实际曲线还必须满足有效下界

$$\boxed{N_{\rm tw}\gg_\epsilon
p^{2+2\kappa_{\rm lin}-\epsilon}
=p^{\frac83e^{2/3}-\epsilon}.} \tag{232.12}$$

若 $j\notin\mathbb Z$，则进一步有

$$\boxed{N_{\rm tw}\gg_\epsilon
p^{3+2\kappa_{\rm lin}-\epsilon}
=p^{1+\frac83e^{2/3}-\epsilon}.} \tag{232.13}$$

这仍是必要增长，未给 $c$、$M^*$、$N_{\rm tw}$ 或 $j$ 高度的上界。$p\equiv1\pmod4$ 分支由 R226 还有 $b=1$，但这个等式本身也不限制三次导子 $c$ 的大小。一般 $p\equiv3\pmod4$、$K\ne\mathbb Q(i)$ 的十二阶比值可能产生真正四次实迹域，不能套用 (232.6)。

## 来源定位

- R116，§§2–3，式 (116.2)、(116.5)、(116.8)–(116.9)：同一个实际差角色、$cp\mathcal O_K$ 准确导子、全分歧循环好约化上的真实整数迹，以及新四阶支撑不需排除的理由。本文在该同一迹上显式计算二次实范数，没有改变实际性前提。
- R229，§§2–5，特别式 (229.8)、(229.11)–(229.13)：固定域有效 Hecke Burgess、坏素理想填补和指数平滑光滑理想计数。
- Liyang Yang，*Relative trace formula and twisted L-functions: the Burgess bound*，Compositio Mathematica **162** (2026), no.11, 2591–2641，[原刊](https://doi.org/10.1017/S0010437X26103327)，[作者稿](https://arxiv.org/abs/2305.10719)，Corollary 1.2 (1.3)。这里仅沿用 R229 已核的固定 $K$ 常数；八个域的有限最大值不依赖实际曲线。
- R220，§§4–6：单个实际规范扭曲的导子与 $T$ 支撑；R226，§2：$p\equiv1\pmod4$ 时 $b=1$。
