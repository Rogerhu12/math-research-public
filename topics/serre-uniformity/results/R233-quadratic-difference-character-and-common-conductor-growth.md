# R233：实际二次差角色、四阶支撑与全部类数一共同导子增长

日期：2026-11-13。

**状态：已证明。** 在同一实际小惯性分支中，用
$\sigma=(\lambda/\psi)^6$ 连接固定 CM 参考、变化的四阶惯性支撑 $b$ 和 R224 的指定二次 Frobenius 检测。新的测试素数可以落在三次导子 $c$ 上：只需 $\sigma$ 不分歧，仍能使用同一实际总分歧好约化扩张中的整数迹。这避免了把变化 $c$ 错收入固定排除集。

主要结论如下，所有下界均有效。

1. 对七个类数一域 $K\notin\{\mathbb Q(i),\mathbb Q(\sqrt{-3})\}$，若 $\sigma\ne1$，则
   $$b\gg_\epsilon p^{\sqrt e-\epsilon}.$$
2. 对全部八个 $K\ne\mathbb Q(\sqrt{-3})$ 的类数一域，无同余分支限制地有
   $$\boxed{bc\gg_\epsilon p^{\frac43e^{2/3}-1-\epsilon}.} \tag{233.1}$$
3. 对 $K=\mathbb Q(\sqrt{-3})$，若 $\sigma\ne1$，则
   $$\boxed{b\gg_\epsilon p^{2\sqrt e-\epsilon}.} \tag{233.2}$$
   这里不要求 $c=6,9$，也不要求 $j$ 整。

它们仍是必要增长；没有给 $b,c$ 或 $j$ 高度的上方控制。

## 1. 同一个实际差角色与实二次域

设 $E/\mathbb Q$、$p>37$ 满足完整非分裂 Cartan 正规化子设置，商域 $K$ 类数一，并假定

$$\bar\rho_{E,p}(I_p)=C^3.$$

沿用 R214 的共同导子参数 $b,c$：$c$ 为实际三次角色的准确环类导子，$b$ 为最高二部分类型额外看见的 $p$ 外导子，$\gcd(b,c)=1$。置 $D=|D_K|$。

取一条固定的有理 CM 参考曲线 $A$，CM 极大序为 $\mathcal O_K$。九个类数一域各取一条即可。把 $A$ 的坏素数、$2,3,D$ 的素因子收入固定集合 $S_0(K)$。有限个 $p\in S_0(K)$ 以后收入有效常数。

R21 的同向比较给

$$\nu=\lambda/\psi,\qquad
\nu^{12}=\nu^{p+1}=1,\qquad \nu^{\mathsf c}=\nu^{-1}.$$

定义准确的二次差角色

$$\boxed{\sigma=\nu^6:G_K\longrightarrow\{\pm1\}.} \tag{233.3}$$

这个定义无复值提升的选择歧义。$\sigma^{\mathsf c}=\sigma$。
选取阶二复共轭 $\mathsf c$，在
$G_{\mathbb Q}=G_K\rtimes\langle\mathsf c\rangle$ 上按

$$\widetilde\sigma|_{G_K}=\sigma,\qquad
\widetilde\sigma(\mathsf c)=1$$

延拓，得到一个连续二次特征。

若 $\sigma\ne1$，令 $F$ 为 $\widetilde\sigma$ 的固定域。则 $F$ 为**实二次域**，与虚二次域 $K$ 不同，而 $KF/K$ 的角色恰为 $\sigma$。对于在 $K$ 分裂、且不分歧于 $KF$ 的有理素数 $q$，

$$\sigma(\mathfrak q)=\chi_F(q) \quad(\mathfrak q\mid q). \tag{233.4}$$

$F$ 不是任意抽象二次域；它来自同一实际 $\lambda$ 与同一固定 $\psi$。

## 2. 二次域判别式由 $b$ 控制，不含变化 $c$

先取 $K\ne\mathbb Q(i)$，所以 $\mathcal O_K^\times$ 的阶为二或六。
固定参考 $A$ 在任何有限处的 CM 惯性均包含于这个单位群，故

$$\psi^6|_{I_w}=1\qquad(w\nmid p). \tag{233.5}$$

在 $p$ 处，小惯性 $C^3$ 的实际局部好约化分歧指数为三或六（R66；亦为 R220 使用的同一局部分类）。R21 选择的同向 $\psi$ 在相应好约化惯性子群上与 $\lambda$ 相同，所以 $\nu|_{I_p}$ 的阶整除六。于是

$$\sigma|_{I_p}=1. \tag{233.6}$$

对 $q\notin S_0(K)\cup\{p\}$，$K/\mathbb Q$ 不分歧。
如果 $E$ 潜在乘法，残余惯性标量阶至多二，故 $\lambda^6$ 平凡。
如果 $E$ 潜在好约化，惯性像是保原点自同构群中的循环群，其阶属于
$\{1,2,3,4,6\}$；模 $p$ 作用忠实。六次幂非平凡恰当惯性阶为四。

若 $\sigma\ne1$，则必有 $p\equiv3\pmod4$；否则 $\gcd(12,p+1)=6$ 已使 $\nu^6=1$。因而上述四阶惯性在非分裂 Cartan 模标量后的像为阶二。R214 的定义和局部导子计算给

$$\boxed{q\mid\operatorname{cond}(\sigma)
\quad\Longleftrightarrow\quad q\mid b
\qquad(q\notin S_0(K)\cup\{p\}).} \tag{233.7}$$

这里左边指 $K$ 上至少一个 $q$ 上方素理想分歧；若 $q$ 分裂，两个共轭分量具有相同非平凡二次惯性；若 $q$ 惰性，唯一分量相同。对于 $q\ge5$，分歧为温和二次，其导子指数恰为一。

特别，三次惯性素数 $q\mid c$、$q\notin S_0(K)$ 不使 $\sigma$ 分歧。真实四阶支撑与三次支撑相离，且六次幂杀死后一惯性。这一点将允许后面的测试素数进入 $c$。

因为 $K/\mathbb Q$ 在 $S_0(K)$ 外不分歧，(233.7) 等价于 $F/\mathbb Q$ 在同一有理素数分歧。基本二次判别式在每个奇分歧素数的指数为一；在二处指数至多三。$b$ 在二、三处的指数由 R214 一致有界，且固定集合 $S_0(K)$ 的其余素数有限。因此存在有效的、只依赖固定 $K$ 和固定 $A$ 的常数 $C_K\ge1$，使

$$\boxed{C_K^{-1}b\le |D_F|\le C_Kb.} \tag{233.8}$$

可以直接把 $S_0(K)$ 中全部可能素因子的最大指数乘起来，给出这样的 $C_K$。后文只需上界。没有声称 $D_F$ 的二、三部分与 $b$ 完全相同；也不需要判断 $F$ 与某个二除判别式域是否相同。

## 3. 允许 $q\mid c$ 的实际整数迹

假定 $K\ne\mathbb Q(i)$、$\sigma\ne1$。取

$$q\nmid 2D_KD_F\prod_{r\in S_0(K)}r,\qquad
\chi_K(q)=1,\qquad\chi_F(q)=-1. \tag{233.9}$$

因为 $p$ 在 $K$ 惰性，$q\ne p$。若 $q\ge p$，后面所需的
$p<256q^2$ 或 $p<4q$ 都自动成立；以下只需考虑 $q<p$。

在 $q$ 处，实际残余局部像包含于 Cartan。若潜在乘法，R63 §3.1 迫
$q\equiv1\pmod p$，与 $q<p$ 矛盾。故潜在好约化。

R63 §§3.2–3.4 的忠实惯性与 Frobenius 交换论证适用于这里全部循环惯性阶，包括 $q\mid c$ 时的三阶或六阶情形。它给一个**总分歧循环好约化扩张**，剩余域仍是 $\mathbb F_q$，以及该同一个实际约化曲线的整数迹

$$a\in\mathbb Z,\qquad |a|<2\sqrt q.$$

取此扩张所用的 Frobenius 提升 $\phi$。固定 CM 参考 $A$ 在 $q$ 好约化；其 CM Frobenius 特征零值可记为

$$\alpha\in\mathcal O_K,\qquad \alpha\bar\alpha=q.$$

$\psi(\phi)$ 是这个 $\alpha$ 的模 $p$ 约化。令 $\zeta\in\mu_{12}$ 为
$\nu(\phi)$ 的相容特征零提升，则

$$a\equiv t=\zeta\alpha+\zeta^{-1}\bar\alpha\pmod{\mathfrak P}.
\tag{233.10}$$

即使 $\nu$ 或三次角色在 $q$ 分歧，$\sigma=\nu^6$ 仍不分歧，所以由 (233.4)、(233.9) 有

$$\boxed{\zeta^6=\sigma(\phi)=\chi_F(q)=-1.} \tag{233.11}$$

因此 $\zeta$ 的阶为四或十二；改变 Frobenius 提升可能改变其三部分，却不会改变 (233.11)。这正是无需排除 $c$ 的原因。

断言 $t\notin\mathbb Q$。若相反，$\zeta\alpha$ 是整数迹、范数 $q$ 的非实二次代数整数。其十二次幂 $\alpha^{12}$ 非实且生成 $K$，故该二次域只能是 $K$，迫 $\zeta\in K$。但是对于
$K\ne\mathbb Q(i)$ 的其余八个类数一域，单位群阶为二或六，不含阶四或十二的元素，矛盾。

设 $L=K(\zeta_{12})$，则 $L^+$ 的次数至多四。$(a-t)$ 是其中非零代数整数，范数被 $p$ 整除，各共轭的绝对值均小于 $4\sqrt q$，故

$$\boxed{p<256q^2.} \tag{233.12}$$

这个结论已对 (233.9) 的全部 $q$ 成立，因为 $q\ge p$ 的情形先前已处理。

## 4. $K=\mathbb Q(\sqrt{-3})$ 的更强二次范数

现在取 $K=\mathbb Q(\sqrt{-3})$。由 (233.11)，可写

$$\zeta=i\epsilon,\qquad\epsilon\in\mu_6\subset\mathcal O_K^\times.$$

令 $\gamma=\epsilon\alpha$。则 $\gamma\in\mathcal O_K$、$\gamma\bar\gamma=q$，且

$$t=i(\gamma-\bar\gamma)=-m\sqrt3,\qquad m\in\mathbb Z.$$

整数性来自 $\mathcal O_K=\mathbb Z[(1+\sqrt{-3})/2]$。
$m\ne0$，否则 $\gamma$ 是范数为素数 $q$ 的有理代数整数，不可能。
因此 $(a-t)$ 在 $\mathbb Q(\sqrt3)$ 中的非零范数为

$$a^2-3m^2,$$

被 $p$ 整除。因 $|a|<2\sqrt q$、$|t|=\sqrt3|m|<2\sqrt q$，两个平方都在 $[0,4q)$ 中，所以

$$\boxed{0<|a^2-3m^2|<4q,\qquad p<4q.} \tag{233.13}$$

这里不需要迹 $a$ 的额外奇偶条件，不需要 $c=6,9$，也不需要 $j$ 整。
$\sigma$ 是同一实际差角色，其不分歧性在 $c$ 上已经证明，故没有将 R107 的旧前提直接删去；本文重新给出了所需迹不等式。

## 5. 指定二次 Frobenius 检测与 $b$ 的下界

应用 R224 定理 224.1，固定 $K$、取上述实际实二次域 $F$。
把固定整数

$$B_0=\prod_{r\in S_0(K)}r$$

作为排除集；选择只依赖 $K$ 的固定 $A>0$，使对全部二次判别式 $|D_F|\ge3$ 都有 $B_0\le|D_F|^A$。于是对任意 $\eta>0$，存在满足 (233.9) 的素数，且

$$q\ll_{K,\eta}|D_F|^{\frac1{2\sqrt e}+\eta}
\ll_{K,\eta}b^{\frac1{2\sqrt e}+\eta}. \tag{233.14}$$

注意 $B_0$ 没有包含 $c$；§3 已完整说明不必这样做。
将 (233.14) 代入 (233.12)，得到

$$p\ll_{K,\eta}b^{\frac1{\sqrt e}+2\eta}.$$

给定 $\epsilon>0$，选足够小的 $\eta>0$ 并反演，得

$$\boxed{b\gg_\epsilon p^{\sqrt e-\epsilon}}
\qquad(K\notin\{\mathbb Q(i),\mathbb Q(\sqrt{-3})\}, \sigma\ne1). \tag{233.15}$$

常数可在七个固定域之间取有限最大值，故有效统一。
$K=\mathbb Q(\sqrt{-3})$ 时用 (233.13) 代替 (233.12)，同样得到

$$\boxed{b\gg_\epsilon p^{2\sqrt e-\epsilon}}
\qquad(K=\mathbb Q(\sqrt{-3}), \sigma\ne1). \tag{233.16}$$

如果 $b$ 的支撑只在固定 $S_0(K)$ 内，(233.8) 使 $D_F$ 有界，上述论证已给有效的 $p$ 上界；不存在遗漏的“有界 $b$、非平凡 $\sigma$”大素数分支。

## 6. 除去 $K=\mathbb Q(\sqrt{-3})$ 后八个域的共同导子

记

$$\kappa_{\rm H}=\frac23e^{2/3}-1=0.2984893607\ldots,$$
$$\kappa_{\rm lin}=\frac43e^{2/3}-1=1.5969787214\ldots,$$
$$\kappa_{\rm mix}=\sqrt e+\kappa_{\rm H}=1.9472106314\ldots.$$

对 $K=\mathbb Q(i)$，R232 已在全部允许 $p$ 上证明
$c\gg_\epsilon p^{\kappa_{\rm lin}-\epsilon}$，从而 $bc$ 至少同样大。

对另外七个域，分两种实际情况。

若 $\sigma=1$，则 $\nu^6=1$。因为这些域的单位群只有 $\{\pm1\}$，R232 §2 的二次实迹域计算完全适用：它唯一使用 $p\equiv1\pmod4$ 的地方，是推出 $\nu^6=1$，此处已经由实际角色平凡性直接给出。所以同一个三次差角色 $\chi=\nu^4$ 的全部小测试素数满足 $p<9q$，R232 §§4–5 的证明给

$$\boxed{c\gg_\epsilon p^{\kappa_{\rm lin}-\epsilon}}
\qquad(\sigma=1). \tag{233.17}$$

若 $\sigma\ne1$，则 (233.15) 与 R229 的同一实际三次角色下界同时成立。重新分配任意小的指数损失，得

$$\boxed{bc\gg_\epsilon p^{\kappa_{\rm mix}-\epsilon}}
\qquad(\sigma\ne1). \tag{233.18}$$

因为 $\kappa_{\rm mix}>\kappa_{\rm lin}$，两种情况合并，得到不依赖 $p\bmod4$、不依赖 $\sigma$ 是否平凡的

$$\boxed{bc\gg_\epsilon p^{\kappa_{\rm lin}-\epsilon}}
\qquad(h_K=1, K\ne\mathbb Q(\sqrt{-3})). \tag{233.19}$$

注意这里是共同导子 $bc$ 的统一下界，不能误写成所有分支的 $c$ 下界；$\sigma\ne1$ 时只对乘积使用了较大指数。

## 7. 共同判别式、规范扭曲导子及精确剩余情形

R220 的同一实际规范扭曲给

$$M^*=D(bc)^2,\qquad
N_{\rm tw}\gg p^2DM^*T,$$

其中 $T\ge1$，而 $j$ 非整时 $T\ge2p-1$。所以全部八个
$K\ne\mathbb Q(\sqrt{-3})$ 的类数一域都有有效必要条件

$$\boxed{M^*\gg_\epsilon p^{2\kappa_{\rm lin}-\epsilon},\qquad
N_{\rm tw}\gg_\epsilon p^{2+2\kappa_{\rm lin}-\epsilon}.} \tag{233.20}$$

第二个指数为 $\frac83e^{2/3}=5.1939574428\ldots$；非整 $j$ 时再增加一。
七域的 $\sigma\ne1$ 分支可把 $\kappa_{\rm lin}$ 换为
$\kappa_{\rm mix}$，得到

$$N_{\rm tw}\gg_\epsilon p^{5.8944212628\ldots-\epsilon},$$

非整 $j$ 时指数再增加一。

$K=\mathbb Q(\sqrt{-3})$ 且 $\sigma\ne1$ 时，(233.16) 给

$$\boxed{M^*\gg_\epsilon c^2p^{4\sqrt e-\epsilon},\qquad
N_{\rm tw}\gg_\epsilon c^2T p^{2+4\sqrt e-\epsilon}.} \tag{233.21}$$

这包含任意变化 $c$、整或非整 $j$；其不带 $c^2T$ 的指数与 R224 在 $c=6,9$ 整 $j$ 分支相同。

$K=\mathbb Q(\sqrt{-3})$ 且 $\sigma=1$ 时，本证明没有给对应的 $c$ 增长：$\nu$ 的值域在 $\mu_6\subset K$，实际 CM 迹可能为整数，非零范数步骤确实消失。对于其他域，全部结论也仍允许 $b,c$ 更快增长。缺少的是能与上述必要增长矛盾的全局上界，或一个不依赖导子大小的有理点排除。

## 来源定位

- R21 §§5–6：实际 $\nu^{12}=\nu^{p+1}=1$、反圆分关系及 $p$ 外循环惯性阶分类。
- R63 §§3.2–3.4：循环惯性的忠实性、Frobenius 在特征零交换惯性、总分歧循环好约化扩张及同一整数迹；本文在 $q\mid c$ 时仍使用该完整版本。
- R66、R214：实际小惯性在 $p$ 的三/六阶好约化分歧、最高二部分导子 $b$ 的准确支撑与小素数指数上界。
- R224 定理 224.1：固定虚二次域中、指定第二二次域的有效小素数检测，允许固定或多项式大小排除集；底层来源为 P. Pollack，*Bounds for the first several prime character nonresidues*，Proc. AMS **145** (2017), 2815–2826，Proposition 2.1，[DOI](https://doi.org/10.1090/proc/13432)，及 S. R. Garcia、E. S. Lee，*Unconditional explicit Mertens' theorems for number fields and Dedekind zeta residue bounds*，Ramanujan J. **57** (2022), 1169–1191，Theorem 1，[DOI](https://doi.org/10.1007/s11139-021-00435-6)。
- R229、R232：同一实际三次差角色的 Burgess 下界，以及 $\mu_6$ 比值与 Gaussian 域的二次迹范数；R220：共同导子到同一实际规范扭曲导子的比较。
