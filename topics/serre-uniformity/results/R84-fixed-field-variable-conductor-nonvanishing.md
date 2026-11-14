# R84：固定底域的变化导子非消失及类数一分支的近二次下界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，独立复核完成；regular 界使用 R87 的独立计数。** 本文将 Feigon–Whitehouse 已发表相对迹公式中的正主项和 regular 误差直接比较。它允许环类导子变化，得到
$$
p\ge C_{K,\epsilon}c^{1+\epsilon}
\quad\Longrightarrow\quad
\exists g\in S_2(\Gamma_0(p))^{\mathrm{new}}:
L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.
$$
$K$ 固定，常数可有效选取；没有将该常数说成对所有虚二次域统一。对类数一的九个底域取有限最大值后，本题有非 exceptional 分母的实际小惯性分支必须满足
$$M\gg_\delta p^{2-\delta}\qquad(0<\delta<2).$$
这是导子必要下界，不是其上界，仍未完成 Serre 一致性。

## 1. 对象、导子及量词

设 $K$ 为判别式 $-D$ 的虚二次域，$D>0$。设
$$\mathcal O_c=\mathbb Z+c\mathcal O_K$$
且 $\eta$ 为准确环类导子 $c$、阶恰为 $3$ 的角色。把它看成平凡于 $\mathbb A_{\mathbb Q}^{\times}$ 的有限阶 Hecke 角色。令
$$M=Dc^2.$$

设素数 $p>37$，$p\nmid Dc$，且 $p$ 在 $K$ 惰性。本文的 $p$ 是模形式水平；FW 文中另外保留的 Hecke 测试素数不用作水平，本文在该处取单位测试函数。

**定理 84.1。** 对每个固定的 $K$ 和每个 $\epsilon>0$，存在可有效选取的正数 $C_{K,\epsilon}$，使任意上述 $c,\eta,p$ 若满足
$$\boxed{p\ge C_{K,\epsilon}c^{1+\epsilon},}\tag{84.1}$$
就有一个权 $2$、准确水平 $p$、平凡 nebentype 的新形式 $g$，满足
$$\boxed{L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right)\ne0.}\tag{84.2}$$

不要求 $p\equiv2\pmod3$；这一同余只在接回 R66 的实际小惯性情形时出现。这里是 unitary 归一化的中心 $1/2$，避免把经典 Rankin、椭圆曲线扭曲及 unitary 中心混写。

对任意固定有限集合 $\mathscr K$，可以用
$$C_{\mathscr K,\epsilon}=\max_{K\in\mathscr K}C_{K,\epsilon}$$
同时覆盖全部 $K\in\mathscr K$。这一步不允许把有限集合换成所有虚二次域。

## 2. 从已发表相对迹公式取出的三个输入

使用 FW 的 $F=\mathbb Q$、$E=K$、$\mathfrak N=(p)$、$k=1$、$m=0$，以及单位 Hecke 测试。所有有限处的极大序选择满足
$$R_q\cap K_q=\mathbb Z_q+q^{v_q(c)}\mathcal O_{K,q}.$$

令
$$S_c=\{q:q\mid c\},\qquad
\mathcal L_c=\prod_{q\mid c}\left(1-\frac{\chi_K(q)}q\right)^{-1}>0.$$
这里 $\chi_K$ 为二次 Dirichlet 角色。$\mathcal L_c$ 是有限集合 $S_c$ **上的局部 Euler 因子积**，不是删去这些因子的整条 $L$ 函数；FW Proposition 4.20 的证明中环面单位体积逐处给出这个积。

FW §2 的导子范数为
$$\boxed{\mathfrak c(\eta)=c^2\mathbb Z,\qquad c(\eta)=c^2.}\tag{84.3}$$
原文的局部指数定义为角色在 $(\mathbb Z_q+q^n\mathcal O_{K,q})^\times$ 上平凡的最小 $n$；准确导子使之等于 $v_q(c)$。因此不能在其 Lemma 6.7 中把 $c(\eta)$ 当成 $c$。

相对迹分解写作
$$I(f)=I_{\mathrm{irreg}}(f)+I_{\mathrm{reg}}(f).$$
由 FW Proposition 4.20 的正主项，以及 [R87](R87-uniform-cubic-orbital-bound-and-square-root-nonvanishing.md) §§3–7 独立证明的 regular 估计，有
$$
I_{\mathrm{irreg}}(f)=A_K\frac{\mathcal L_c}{c},\qquad A_K>0,
\tag{84.4}
$$
以及对每个 $a>0$，
$$
\boxed{|I_{\mathrm{reg}}(f)|\le B_{K,a}\frac{c^{2a}}p.}
\tag{84.5}
$$
这里 $B_{K,a}>0$ 与 $p,c,\eta$ 无关。在 FW 的完成 $L$ 函数及 Haar 测度约定下可以取
$$A_K=\frac{4L(1,\chi_K)}{\sqrt D}.$$
本文只使用该值正且在固定 $K$ 下可有效计算，不在别的周期约定下复用这个数值。单位测试时 $\widetilde I(1)=1$；可由 FW Lemmas 4.4–4.6 直接读出。水平 $p>1$，所以 Proposition 4.20 的第二个 irregular 轨道也不贡献。

最后，FW Lemma 3.6 使一维谱项消失：它只能由阶至多二的范数组合角色产生，而 $\eta$ 的阶为三。Proposition 3.9 因而将 $I(f)$ 写成
$$
\boxed{I(f)=\sum_{g\in\mathcal F(p,2)} b_{g,K,c}\,
 L\!\left(\tfrac12,\pi_{g,K}\otimes\eta\right),\qquad b_{g,K,c}>0.}
\tag{84.6}
$$
这里 $\mathcal F(p,2)$ 是准确水平 $p$ 的新形式集合；正系数包含正的 adjoint 分母和局部体积。只需由 $I(f)>0$ 推出至少一个中心值不为零，无需把每个系数规范为一。

这里使用 FW 已发表的谱端与正主项公式，regular 上界由 R87 的独立整数计数给出；以下正主项比较和本题推论在本文证明。

## 3. 局部 Euler 积的有效下界

对任意 $q$，
$$
\left(1-\frac{\chi_K(q)}q\right)^{-1}
\ge1-\frac1q.
$$
故
$$\mathcal L_c\ge\frac{\phi(c)}c.$$

给定 $b>0$，置
$$
\beta_b=\prod_{\substack{q\ \mathrm{素数}\\q\le2^{1/b}}}\left(1-\frac1q\right)>0.
$$
若 $q>2^{1/b}$，则 $q^{-b}<1/2\le1-1/q$。逐素数相乘，
$$
\frac{\phi(c)}c
\ge\beta_b\prod_{\substack{q\mid c\\q>2^{1/b}}}q^{-b}
\ge\beta_bc^{-b}.
$$
因此
$$\boxed{\mathcal L_c\ge\beta_bc^{-b}.}\tag{84.7}$$
这是完全有效的初等估计。常数 $\beta_b$ 不依赖 $K$；后续常数对 $K$ 的依赖来自 (84.4)–(84.5)。

## 4. 正主项压过误差

给定定理中的 $\epsilon>0$，在 (84.5) 取
$$a=\epsilon/4,$$
在 (84.7) 取
$$b=\epsilon/2.$$
于是
$$I_{\mathrm{irreg}}(f)\ge A_K\beta_{\epsilon/2}c^{-1-\epsilon/2},$$
且
$$|I_{\mathrm{reg}}(f)|\le B_{K,\epsilon/4}c^{\epsilon/2}/p.$$

可取
$$
\boxed{
C_{K,\epsilon}=
\max\left\{1,\frac{2B_{K,\epsilon/4}}{A_K\beta_{\epsilon/2}}\right\}.
}
\tag{84.8}
$$
若 $p\ge C_{K,\epsilon}c^{1+\epsilon}$，则
$$
|I_{\mathrm{reg}}(f)|
\le\tfrac12 A_K\beta_{\epsilon/2}c^{-1-\epsilon/2}
\le\tfrac12 I_{\mathrm{irreg}}(f).
$$
因而
$$I(f)\ge I_{\mathrm{irreg}}(f)-|I_{\mathrm{reg}}(f)|>0.$$
由 (84.6)，至少一个 $g$ 满足 (84.2)。定理 84.1 得证。

不需预先假设 $p>M$ 或 $M<3p$；R87 的 regular 估计在稳定范围以外仍有效，并独立重证本题所需的 FW Lemma 6.7 型界。这里没有用截断近似值判断某个中心值是否为零。

## 5. 常数的有效性与当前没有计算的量

固定 $K$ 时，R87 的完全显式估计给 $|I_{\mathrm{reg}}|\ll_a M^a/p=D^ac^{2a}/p$，所以可有效选取 (84.5) 的 $B_{K,a}$。其证明保留所有分歧环面体积，以截断赋值及通过零点的整数倍计数处理单元素边界；不调用 FW Lemma 6.6 的一般平移进程上界。R87 §9 解释了该区别，因此本文不从原计数证明中未经修复的单元素步骤推导有效性。

具体地，整数除数估计的常数也可有效选取。若 $u>0$，则
$$
\tau(n)\le T_u n^u,\qquad
T_u=\prod_{\substack{q\ \mathrm{素数}\\q\le2^{1/u}}}
\max_{e\ge0}(e+1)q^{-ue}.
$$
每个最大值可有限求出：相邻项之比趋于 $q^{-u}<1$；而 $q>2^{1/u}$ 时 $(e+1)\le2^e<q^{ue}$，无需额外因子。R87 中各处这种小幂损失可按预先指定的 $a$ 分配。

分歧处以紧环面体积的显式平方界处理，拱处本篇 $k=1,m=0$，没有增长参数。$A_K$ 则是固定非零 Dirichlet 值及明确拱因子；也可通过二次类数公式计算。

因此“可有效选取”是可证明的性质。本文**没有实际算出**某个最优或实用的 $C_{K,\epsilon}$，也没有以隐含常数给出具体有限素数范围的数值排除。若要执行固定实例，须将这些体积、除数常数和 (84.8) 逐项数值化。

## 6. 换成 $M$，以及类数一底域的统一性

给定 $\nu>0$，在定理 84.1 使用 $\epsilon=2\nu$。因 $M=Dc^2$，可将条件写成
$$
\boxed{p\ge C'_{K,\nu}M^{1/2+\nu},}\tag{84.9}
$$
其中
$$C'_{K,\nu}=C_{K,2\nu}D^{-1/2-\nu}>0.$$
这只是固定 $K$ 下的重参数化，未得到所有 $K$ 共用的 $C'_\nu$。

对 $h_K=1$，经典完整分类给
$$D\in\{3,4,7,8,11,19,43,67,163\}.$$
该已发表分类的有限性及最大判别式也列于 Watkins 的完整类数分类表。对这九个固定域取最大值，得到：对每个 $\epsilon>0$，有可有效选取的 $C_{1,\epsilon}>0$，使
$$
\boxed{
h_K=1,\quad p\ge C_{1,\epsilon}c^{1+\epsilon}
\quad\Longrightarrow\quad \exists g:\ L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.
}
\tag{84.10}
$$
这里三次角色必须有 $c>1$，否则普通类群平凡；这与 R66 的实际分支一致。这个有限集合论证不依赖关于所有判别式的无效 Siegel 常数。

## 7. 接回实际小惯性与分母

R66 的小惯性分支有 $p\equiv2,5\pmod9$，准确三次角色 $\eta$ 及 $M=Dc^2$，并满足本篇的惰性和互素条件。只要 (84.2) 成立，R69 构造实际三次秩零商，R72 的尖点形式浸入排除非 exceptional 的分母素数。

因此，如果实际候选曲线存在至少一个非 exceptional 的 $j$ 分母素数，定理 84.1 的逆否命题给
$$\boxed{p<C_{K,\epsilon}c^{1+\epsilon}.}\tag{84.11}$$
对 $h_K=1$ 可统一写作
$$
M=Dc^2>D\left(\frac p{C_{1,\epsilon}}\right)^{2/(1+\epsilon)}.
\tag{84.12}
$$
给定 $0<\delta<2$，取
$$\epsilon=\frac{\delta}{2-\delta},\qquad\frac2{1+\epsilon}=2-\delta.$$
九域中 $D\ge3$，故
$$
\boxed{M>A_\delta p^{2-\delta},\qquad
A_\delta=3C_{1,\delta/(2-\delta)}^{-(2-\delta)}>0.}
\tag{84.13}
$$
这是类数一实际小惯性分支中的有效必要下界。它覆盖变化的 $c$，比仅固定角色后令水平增长更强；但没有禁止 $c$ 随 $p$ 同时增长。

对一个固定而类数大于一的 $K$，同样有依赖 $K$ 的 (84.12)–(84.13)。R67 控制的是随 $K$ 变化时 $D$ 的必要下界，不能用它把 $C_{K,\epsilon}$ 换成绝对常数。

## 8. 和其他结果的准确关系

- R81 的 $M<3p$ 对所有虚二次域统一，且是明确线性范围；本篇的近平方根范围在固定底域时渐近更强，但常数依赖底域。
- R83 的类数判据对 $K,c$ 同时统一且常数显式；其 Siegel 推论有无效性。本篇固定 $K$ 的论证没有使用该推论。
- Michel–Ramakrishnan 的普通类群角色结论不能直接替代本篇中 $c>1$ 的环类角色。这里实际使用变化导子的 regular 估计，并由 R87 重新证明其全局计数。
- (84.13) 只针对存在非 exceptional 分母的实际小惯性分支。全部分母 exceptional、完整惯性及真实 QC 共同根仍需分别处理；本篇没有对这些开放项给排除。

## 9. 原始来源

1. B. Feigon, D. Whitehouse, *Averages of central L-values of Hilbert modular forms with an application to subconvexity*, **Duke Mathematical Journal 149** (2009), no. 2, 347–410。[作者全文](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)，[作者出版目录](https://bfeigon.ccny.cuny.edu/papers.html)，[大学接受稿登记](https://ueaeprints.uea.ac.uk/id/eprint/18579/)，[DOI](https://doi.org/10.1215/00127094-2009-041)。核验位置：§2 的导子定义；Lemma 3.6、Proposition 3.9；Proposition 4.20 及其体积证明。Lemma 6.7 作为文献对照；本文实际 regular 界用 R87 的独立证明，不调用 Lemma 6.6。上述编号按作者接受稿。
2. M. Watkins, *Class numbers of imaginary quadratic fields*, **Mathematics of Computation 73** (2004), no. 246, 907–938。[作者全文](https://magma.maths.usyd.edu.au/~watkins/papers/smallcn.pdf)，[期刊全文](https://www.ams.org/mcom/2004-73-246/S0025-5718-03-01517-5/S0025-5718-03-01517-5.pdf)。末节分类表给类数一共有九个基本判别式，最大绝对值163；这里只用于有限底域推论，未把该分类当作本文主定理的证明。
3. [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)、[R69](R69-forgetful-maps-and-unconditional-rank-zero-quotient.md)、[R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md)：实际三次角色、秩零商与分母接口。
