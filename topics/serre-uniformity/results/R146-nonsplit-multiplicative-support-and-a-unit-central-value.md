# R146：全部新增乘法约化非分裂时的中心值单位与解析秩零

日期：2026-11-12。

**状态：已证明。** 设 $p>37$，$p\equiv3\pmod4$，且实际非 CM 曲线 $E/\mathbb Q$ 满足
$$E[p]\simeq A[p],\qquad A:y^2=x^3-x.$$
如果 $E$ 在全部新增乘法素数处都是**非分裂乘法约化**，则
$$
\boxed{v_p\left(\frac{L(E,1)}{\Omega_E^+}\right)=0.}
\tag{146.1}
$$
这里 $\Omega_E^+$ 是 Néron 微分的正实周期；若使用整个实点集上的积分，只相差因子 $1$ 或 $2$，结论不变。特别地，$E$ 的解析秩为零，$E(\mathbb Q)$ 和完整的 $\Sha(E/\mathbb Q)$ 都有限，而 $\Sha(E)[p^\infty]=0$。

R50 已经给出此分支的 $p$-Selmer 群为零。本篇增加的是**实际复 $L$ 函数的非零中心值和完整 $\Sha$ 的有限性**。此结果不排除这样的非 CM 曲线，也不界住 $p$。它不调用关于非 CM 超奇异曲线的未验证主猜想或 $p$-逆定理。

## 1. 实际数据与两个“分裂”的区别

由 R19，存在该文某一原始整数族 $(X,W,Z)$，满足
$$
|Z|>1,\qquad (Z,6p)=1,\qquad
N_E=32\operatorname{rad}(|Z|),\qquad
\Delta_{\min}(E)=2^\delta Z^p.
\tag{146.2}
$$
令
$$T=\{q:q\mid Z\},\qquad t=|T|.$$
我们的附加条件是
$$a_q(E)=-1\qquad(q\in T).\tag{146.3}$$
这只说明 $E/\mathbb Q_q$ 的乘法约化非分裂；**允许 $q$ 在 $\mathbb Q(i)$ 中分裂或惰性**。尤其不要求 $q\equiv-1\pmod p$。

以 R50 的记号，(146.3) 正是 $s=0$。若用原始坐标判断，它等价于
$$
\left(\frac{-3W}{q}\right)=-1\quad\text{对族 I、II 的全部 }q\mid Z,
$$
$$
\left(\frac{-6W}{q}\right)=-1\quad\text{对族 III 的全部 }q\mid Z.
\tag{146.4}
$$
原始性保证符号中的分子与 $q$ 互素。

以下只用 (146.2)、(146.3) 和真实挠点同构，因而覆盖三个族、$Z$ 的两个符号，以及所有合法的生成元和模型选择。

## 2. 选择与实际乘法符号相符的稳定化

令
$$f_A=\sum_{n\ge1}a_n(A)Q^n,\qquad f_E=\sum_{n\ge1}a_n(E)Q^n,$$
其中 $Q=e^{2\pi iz}$，两者是相应的归一化权二新形式。为区别素数和 Fourier 变量，下文以 $Q$ 表示后者。

### 2.1 新增素数的 Hecke 多项式

对 $q\in T$，$A$ 在 $q$ 好约化，而 $E$ 在 $q$ 非分裂乘法约化。真实同构 $E[p]\simeq A[p]$ 和 Tate 曲线的非分裂二次扭曲给
$$a_q(A)\equiv-(q+1)\pmod p.\tag{146.5}$$
因此
$$
U^2-a_q(A)U+q\equiv(U+1)(U+q)\pmod p.
\tag{146.6}
$$
在一个足够大的有限扩张 $F/\mathbb Q_p$ 中，对每个 $q\in T$ 选择根 $\alpha_q$，使
$$
\alpha_q\equiv-1\pmod{\mathfrak p},\qquad
\beta_q=q/\alpha_q.
\tag{146.7}
$$
记 $\mathcal O$ 为 $F$ 的整数环，$\mathfrak p$ 为其极大理想。两根均为 $\mathcal O$-单位。若 $q\equiv1\pmod p$，模 $p$ 多项式有重根，这不妨碍在代数闭包中选取 (146.7)。特征零的两个根始终不同，因为 $a_q(A)^2=4q$ 对素数 $q$ 不可能成立。

令 $V_q f(z)=f(qz)$，定义层
$$M=32\prod_{q\in T}q=N_E$$
上的旧形式
$$h=\prod_{q\in T}(1-\beta_qV_q)f_A.\tag{146.8}$$
它是归一化的全部 Hecke 算子的特征形式，且
$$U_qh=\alpha_qh\qquad(q\in T).\tag{146.9}$$
例如在一个新增素数处，$U_qf_A=a_q(A)f_A-qV_qf_A$、$U_qV_qf_A=f_A$，故
$$
U_q(f_A-\beta_qV_qf_A)
=\alpha_q(f_A-\beta_qV_qf_A).
$$
不同素数的稳定化彼此交换。

### 2.2 全部 Fourier 系数同余，包括 $p$

在 $q\in T$，(146.7) 和 (146.3) 给 $a_q(h)\equiv a_q(E)$。在素数 $\ell\nmid 2p\prod T$，挠点同构直接给出好约化迹同余。在 $2$ 处，两个新形式都有 $U_2=0$，稳定化不改变这一点。

还必须补上 $p$ 处。两条曲线在 $p$ 好约化；$A$ 因 $p\equiv3\pmod4$ 而超奇异，其模 $p$ 惯性半单化是 niveau 二的两个基本角色。若 $E$ 在 $p$ 普通，则模 $p$ 惯性半单化为 $1$ 与模 $p$ 分圆角色，不能与前者同构。因此 $E$ 也在 $p$ 超奇异。由于 $p>3$，
$$a_p(E)=a_p(A)=a_p(h)=0.\tag{146.10}$$
结合 Hecke 递推、坏素数的 $U_\ell$ 递推和系数的乘法性，得到真正的全系数同余
$$\boxed{h\equiv f_E\pmod{\mathfrak p}.}\tag{146.11}$$
这一步不是仅在避开层与 $p$ 的素数上比较迹。

### 2.3 中心因子是单位

由 Dirichlet 级数的稳定化恒等式，先在绝对收敛半平面再解析延拓，
$$
L(h,s)=\prod_{q\in T}(1-\beta_qq^{-s})L(A,s).
$$
在中心
$$
L(h,1)=\prod_{q\in T}(1-\alpha_q^{-1})L(A,1),
\qquad
\prod_{q\in T}(1-\alpha_q^{-1})\equiv2^t\pmod{\mathfrak p}.
\tag{146.12}
$$
所以此乘积是单位。不能把它与删除整个好约化 Euler 因子的表达式混为一谈；后者还含另一根，会引入与本篇所选 $U_q$ 特征值无关的零因子。

## 3. 规范周期同余：准确假设

使用 Vatsal，*Canonical periods and congruence formulae*，Duke Math. J. **98** (1999)，397–419，§§1.1–1.3、Proposition 1.7 和 Theorem 1.13 的 prime-to-$p$ 情形。[作者全文](https://personal.math.ubc.ca/~vatsal/research/bah.PDF)

我们采用微分
$$\omega_f=2\pi i f(z)\,dz,$$
故本篇规范周期 $\mathcal P_f^+$ 是该文的 $2\pi i\Omega_f^+$。相同的整体符号对所有形式一致，不影响下列同余与赋值。

定理所需条件在这里逐一如下。

1. **层素于 $p$，权小于 $p$。** 由 $(Z,p)=1$，有 $p\nmid M$，且权为 $2<p$。Theorem 1.13 的第一种情形给出局部化的整 Betti 上同调与整 cusp forms 的 Hecke 模同构；不要求 $p$ 普通。作者版本该定理前一句写明正在验证 §1.2 的 Condition 2，定理首句的条件编号印为 1；下文引用的是其证明中的上同调对偶陈述。
2. **残余不可约。** 本题的 $A[p]$ 在 $\mathbb Q$ 上绝对不可约。因此相关极大理想 $\mathfrak m$ 非 Eisenstein，整抛物上同调与局部化的通常上同调相同。
3. **特征零的 Hecke 局部因子是一维。** $f_E$ 是新形式，满足此条件。$h$ 对应的 $f_A$-旧空间由各新增 $q$ 的两个稳定化组成；每一处的两个特征零 Satake 根不同，故选择所有 $U_q=\alpha_q$ 后，全部 Hecke 特征空间一维，局部因子为 $F$。模 $p$ 两根可能重合，不影响此特征零条件。精确的远离层的 Hecke 特征由强重数一排除别的新表示。

特别地，可选择规范周期，使
$$
\delta_f^+=\frac{\omega_f^+}{\mathcal P_f^+}
\in H^1(X_1(M),\mathcal O)^+_{\mathfrak m}
\tag{146.13}
$$
为**原始**整类。原始性来自 Vatsal §1.3 的同构
$$
\theta^+:H^1(X_1(M),\mathcal O)^+_{\mathfrak m}
\simeq S_2(\Gamma_1(M),\mathcal O)_{\mathfrak m},
\qquad \theta^+(\delta_f^+)=f:
$$
归一化条件 $a_1(f)=1$ 保证 $f$ 不被 $\mathfrak p$ 整除。

Proposition 1.7 及其 §1.6 的整性证明给
$$
\frac{L(h,1)}{\mathcal P_h^+},\quad
\frac{L(E,1)}{\mathcal P_E^+}\in\mathcal O,
\qquad
\frac{L(E,1)}{\mathcal P_E^+}
\equiv\frac{L(h,1)}{\mathcal P_h^+}\pmod{\mathfrak p}.
\tag{146.14}
$$
平凡 Dirichlet 角色包含在此结论中：§1.5 的定义允许角色导子为一，而 §1.6 用非 Eisenstein Hecke 算子消去边界，所除的标量为单位。所以这里没有把只有非平凡扭曲时成立的公式擅自用于未扭中心值。

## 4. 整退化类与周期比例：不需要预设饱和

令 $\mathcal P_A^+$ 是层 $32$ 的规范周期，令
$$\delta_A^+=\omega_A^+/\mathcal P_A^+$$
为对应的原始整 Betti 类。第 6 节将证明规范周期与 Néron 周期的比例为 $p$-单位。R50 已精确计算
$$L(A,1)/\Omega_A^+=1/4,$$
故
$$\frac{L(A,1)}{\mathcal P_A^+}\in\mathcal O^\times.\tag{146.15}$$

在从层 $n$ 升到层 $nq$ 的每一步，令
$$d_1,d_q:X_1(nq)(\mathbb C)\longrightarrow X_1(n)(\mathbb C)$$
为对应 $z\mapsto z$、$z\mapsto qz$ 的退化映射。它们在 **Betti 整上同调** 上的拉回是整的，并且
$$
d_q^*\omega_f=q\omega_{V_qf}.
$$
因为 $q\ne p$，$\beta_q/q\in\mathcal O^\times$，于是
$$
\frac{\omega_h^+}{\mathcal P_A^+}
=\prod_{q\in T}\left(d_1^*-\frac{\beta_q}{q}d_q^*\right)\delta_A^+
\in H^1(X_1(M),\mathcal O)^+_{\mathfrak m}.
\tag{146.16}
$$
乘积按升层顺序理解。映射与复共轭交换；在残余极大理想处投影保持整性。这里不能只用 de Rham 微分的整性代替 Betti 格上的断言。

由于 $h$ 的特征空间一维，(146.13)、(146.16) 给
$$
\frac{\omega_h^+}{\mathcal P_A^+}
=c\delta_h^+,
\qquad c=\frac{\mathcal P_h^+}{\mathcal P_A^+}\in F.
$$
左侧整，右侧的 $\delta_h^+$ 原始，所以
$$c\in\mathcal O.\tag{146.17}$$
此时还没有假定 $c$ 是单位，也没有假定退化映射的像饱和。

另一方面，(146.12)、(146.15) 给出单位等式
$$
\underbrace{\prod_{q\in T}(1-\alpha_q^{-1})
\frac{L(A,1)}{\mathcal P_A^+}}_{\in\mathcal O^\times}
=\frac{L(h,1)}{\mathcal P_A^+}
=c\frac{L(h,1)}{\mathcal P_h^+}.
\tag{146.18}
$$
右侧两个因子都整，故两者都必须是单位：
$$
\boxed{\mathcal P_h^+/\mathcal P_A^+\in\mathcal O^\times,
\qquad L(h,1)/\mathcal P_h^+\in\mathcal O^\times.}
\tag{146.19}
$$
这封口了周期归一化问题，尤其覆盖 $q\equiv1\pmod p$ 的重根剩余情形。没有把可能的同余模或周期分母悄悄忽略，也不需要另外引用 Ihara 饱和性。

## 5. 实际中心值与算术推论

把 (146.19) 代入 (146.14)，得到
$$\frac{L(E,1)}{\mathcal P_E^+}\in\mathcal O^\times.\tag{146.20}$$
第 6 节证明 $\mathcal P_E^+/\Omega_E^+$ 为 $p$-单位，遂得 (146.1)。

因此 $L(E,1)\ne0$，解析秩等于零。已发表的 Gross–Zagier–Kolyvagin 解析秩零定理给出
$$\operatorname{rank}E(\mathbb Q)=0,\qquad \#\Sha(E/\mathbb Q)<\infty.$$
这里使用的是已知方向“中心值非零推出有限性”。它不要求 $E$ 半稳定，也不要求新增乘法素数处残余表示分歧。有关完整定理的准确陈述可见 Jetchev–Lauter–Stein (2009), Theorem 1.1，所引用的原始 Kolyvagin 定理及辅助二次扭曲非消失结果。

同时，R50 的 $s=0$ 情形已经独立证明
$$\operatorname{Sel}_p(E)=0.$$
Kummer 正合列给 $\Sha(E)[p]=0$，进而 $\Sha(E)[p^\infty]=0$。所以此分支不存在“代数秩零但解析中心仍消失”的未决替代项，也不存在完整 $\Sha$ 有限性上的剩余假设。

此结论对 $g=\gcd_{q\mid Z}v_q(Z)$ 的所有取值都成立，包括当前主要的 $g=1$、$g=3$ 以及变化惰性素因子分支。

## 6. 好约化处的规范周期与 Néron 周期

这里单独证明所需周期比较，避免把只为普通 Iwasawa 理论陈述的命题套到超奇异 $p$。

设 $B/\mathbb Q$ 是与一个权二有理系数新形式 $f$ 对应的曲线，$p\nmid N_f$，且 $B[p]$ 不可约。令 $B_1$ 是该同源类的 $X_1(N_f)$ 最优商，$\pi_1:X_1(N_f)\to B_1$。其 Manin 常数满足
$$\pi_1^*\omega_{B_1}=c_1\omega_f,\qquad c_1\in\mathbb Z_p^\times.\tag{146.21}$$
这里可用 Greenberg–Vatsal，*On the Iwasawa invariants of elliptic curves*，Invent. Math. **142** (2000)，17–63，**Proposition 3.3** 的好约化情形。该命题比较 $X_0$、$X_1$ 两个 Manin 常数，只要求 $p$ 在层中至多一次；其证明明确覆盖 good reduction，不要求 ordinary。我们不直接援用同文 Proposition 3.1 的 ordinary 表述。[作者版本](https://arxiv.org/pdf/math/9906215)

最优性给同调满射
$$H_1(X_1(N_f),\mathbb Z_p)\twoheadrightarrow H_1(B_1,\mathbb Z_p).$$
由于 $p$ 奇，投影到 $+$ 部分后仍满射。规范上同调类 $\omega_f^+/\mathcal P_f^+$ 原始，故 $\omega_f^+$ 在整 $+$ 同调上的积分像由 $\mathcal P_f^+$ 生成；满射与 (146.21) 则说明同一积分像由 $\Omega_{B_1}^+/c_1$ 生成。因此
$$\mathcal P_f^+/\Omega_{B_1}^+\in\mathbb Z_p^\times.\tag{146.22}$$

最后，$B[p]$ 不可约意味着同源类内没有有理 $p$-同源。任意两条该同源类曲线之间都可选择次数素于 $p$ 的有理同源：若一个同源的核有非平凡 $p$-部分而无 $p$ 阶稳定直线，该核必包含全 $B[p]$，于是可除去乘 $p$，重复即可。次数素于 $p$ 的同源在 $\mathbb Z_p$ 上比较 Néron 微分及 $+$ 同调均给单位。因此
$$\mathcal P_f^+/\Omega_B^+\in\mathbb Z_p^\times.\tag{146.23}$$
将此分别用于 $B=A$ 和 $B=E$，得到第 4、5 节需要的两个比较。基变换到 $\mathcal O$ 后仍为单位。此论证不要求两曲线在 $p$ 普通。

## 7. 严格边界及后续所需输入

结论使用了全部新增素数的符号 $a_q(E)=-1$。若存在分裂乘法素数，匹配的根为 $\alpha_q\equiv1$，(146.12) 的对应中心因子就不再是单位；第 4 节的单位乘积论证不能照搬。本文也没有把有限迹同余当成实际模形式同余：输入始终是完整 $E[p]\simeq A[p]$。

解析秩零及中心值 $p$-单位与非 CM 性、非整 $j$ 和 $Z$ 的原始高幂均相容。故本篇没有证明这三个 Diophantine 族无解，也没有得到绝对 $p$ 上界。要关闭 $s=0$ 分支，仍需一个与本篇确定的解析行为相冲突的实际全局输入；不能仅将已有的零 Selmer 群再叙述一次作为矛盾。

## 8. 可复核来源

- V. Vatsal，**Canonical periods and congruence formulae**，Duke Mathematical Journal **98** (1999)，397–419，§§1.1–1.3、Proposition 1.7、Theorem 1.13。[作者全文](https://personal.math.ubc.ca/~vatsal/research/bah.PDF)，[DOI](https://doi.org/10.1215/S0012-7094-99-09811-3)。正文使用其 prime-to-$p$ 整上同调论证，不使用普通 $p$-进 $L$ 函数部分。
- R. Greenberg、V. Vatsal，**On the Iwasawa invariants of elliptic curves**，Inventiones Mathematicae **142** (2000)，17–63，Proposition 3.3、其后的整同调积分论证及 Remark 3.4。[作者全文](https://arxiv.org/pdf/math/9906215)。只使用好约化 Manin 常数比较和最优商，不调用该文 ordinary Iwasawa 结论。
- D. Jetchev、K. Lauter、W. Stein，**Explicit Heegner points: Kolyvagin's conjecture and non-trivial elements in the Shafarevich–Tate group**，Journal of Number Theory **129** (2009)，284–302，Theorem 1.1。[作者全文](https://wstein.org/papers/kolyconj/paper/jetchev-lauter-stein-kolyconj.pdf)。给出已知解析秩至多一时的秩等式和完整 $\Sha$ 有限性准确陈述。
- V. A. Kolyvagin，**Finiteness of $E(\mathbb Q)$ and $\Sha(E,\mathbb Q)$ for a subclass of Weil curves**，Mathematics of the USSR-Izvestiya **32** (1989)，523–541。[原刊全文](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=1191&what=fullteng)。其 Heegner 点定理与已发表的辅助二次扭曲非消失共同给上述解析秩零结论；未将原文中的辅助 Heegner 非挠假设省略为新论断。
- 仓库 [R19](R19-converse-fermat-fixed-cm.md)、[R50](R50-actual-selmer-alternating-matrix.md)：真实整数模型、局部条件、$L(A,1)/\Omega_A^+=1/4$ 和 $s=0$ 时的零 Selmer 群。
