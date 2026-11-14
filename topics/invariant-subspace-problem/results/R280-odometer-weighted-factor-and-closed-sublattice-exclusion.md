# R280：原 Haar odometer 的加权因子与闭子格完全排除

日期：2026-11-14。代理：normal_annihilator / 789f。
作者：Astra-ISP-789f；AI-assisted，GPT-6 Astra Pro。

**状态：完整自含证明。** 对原算子 $A$，全部非零加权可测因子子空间若不变就等于 $H$；权函数可为任意几乎处处有限的可测复函数，不预设平方可积。由此排除所有非零真闭逐点子格，以及正交投影可经逐点相位共轭而保正的全部普通不变子空间。没有排除一般闭线性子空间，也没有解决普通复 Hilbert ISP。

## 1. 对象与准确序结构

沿用 [R9](R9-radial-odometer-and-nilpotent-approximants.md)、[R107](R107-centered-order-and-compactness-obstructions.md) 的原表示：

$$
H=L^2(\mathbb Z_2,\mu),\qquad
\tau(y)=y-1,\qquad Uf=f\circ\tau,\qquad A=M_wU.
\tag{1.1}
$$

$\mu$ 为 Haar 概率测度，$w>0$ 几乎处处且有界。实际权满足 $r(A)=0$，$A$ 单射；本证明只使用这些性质和 odometer 动态，不需要具体超指数系数。

本文的**保正**指逐点函数非负锥的保正，和 Hilbert 空间自伴正半定是不同条件。每个正交投影都 Hilbert 正，但并不自动逐点保正。

设 $\mathcal F$ 是 Haar 完备可测空间的子 $\sigma$-代数，所有关系按零测集完成。对任意几乎处处有限的可测复函数 $h$，令

$$
\nu_h=|h|^2\mu,\qquad
\mathcal M(h,\mathcal F)
=\{hg:g\text{ 为 }\mathcal F\text{ 可测},\ \int |g|^2\,d\nu_h<\infty\}.
\tag{1.2}
$$

这里 $\nu_h|_{\mathcal F}$ 允许无限，不假设 $h\in H$。乘法 $g\mapsto hg$ 是 $L^2(\mathcal F,\nu_h)$ 到 $H$ 的等距嵌入，故 (1.2) 是闭线性子空间。若 $h$ 在某集合为零，等距性按 $\nu_h$ 的通常零向量商理解。

**主定理。** 若

$$
\mathcal M(h,\mathcal F)\ne\{0\},\qquad
A\mathcal M(h,\mathcal F)\subseteq\mathcal M(h,\mathcal F),
\tag{1.3}
$$

则 $\mathcal M(h,\mathcal F)=H$。

以下先支付支撑和权函数的归一化，再分析真正的 Haar 因子。

## 2. 支撑与平方可积权的归一化

**引理 2.1。** 在 (1.3) 下，可以找到 $h_0\in\mathcal M(h,\mathcal F)$，使

$$
0<|h_0|<\infty\quad\mu\text{-a.e.},\qquad
h_0\in H,\qquad
\mathcal M(h,\mathcal F)=\mathcal M(h_0,\mathcal F).
\tag{2.1}
$$

**证明。** 取该闭子空间中的可数稠密列 $f_j=hg_j$，其中 $g_j$ 为 $\mathcal F$ 可测。选 $a_j>0$ 使

$$
\sum_j a_j\|f_j\|_2<\infty.
$$

因为 $h|g_j|\in\mathcal M(h,\mathcal F)$，有限部分和

$$
h\sum_{j\le n}a_j|g_j|
$$

在 $H$ 中收敛。令 $u=\sum_j a_j|g_j|$；在 $h\ne0$ 处，$u$ 几乎处处有限，极限为 $h_0=hu$。在 $h=0$ 处置 $h_0=0$，所以 $h_0\in\mathcal M(h,\mathcal F)\cap H$。

令

$$
E=\{h_0\ne0\}=\bigcup_j\{f_j\ne0\}
\quad\text{模零}.
$$

每个 $f\in\mathcal M(h,\mathcal F)$ 都在 $E^c$ 上为零，因为它是 $f_j$ 的 $L^2$ 极限。另一方面，$Ah_0\in\mathcal M(h,\mathcal F)$，而 $w>0$ 几乎处处给

$$
\operatorname{supp}(Ah_0)=\tau^{-1}E\quad\text{模零}.
$$

因此 $\tau^{-1}E\subseteq E$ 模零。保测性给 $\mu(\tau^{-1}E)=\mu(E)$，故实际有等号。Odometer 遍历，而 $E$ 非零测，遂有 $\mu(E)=1$。

特别，$h\ne0$ 几乎处处且 $0<u<\infty$ 几乎处处。$u$ 为 $\mathcal F$ 可测，所以对任意 $g$，$g/u$ 和 $ug$ 保持相应的 $\mathcal F$ 可测性。恒等式

$$
\int |g/u|^2|h_0|^2\,d\mu
=\int |g|^2|h|^2\,d\mu
$$

和反向替换给两边子空间相等，证明 (2.1)。$\square$

这一步没有把前向支撑包含直接说成遍历不变；先用保测性得到等号，再用遍历性。

以下将 $h_0$ 重新记作 $h$，因此 $h\in H$、$h\ne0$ 几乎处处。有限测度 $\nu_h$ 与 Haar 测度等价。

## 3. $A$ 不变性迫出 Haar 可测因子

由于 $h\in\mathcal M(h,\mathcal F)$，有 $Ah\in\mathcal M(h,\mathcal F)$，故

$$
q=\frac{Ah}{h}=w\frac{h\circ\tau}{h}
\tag{3.1}
$$

为 $\mathcal F$ 可测且非零几乎处处。这里 $q$ 不必有界，也不要求对数可积。

对任意 $B\in\mathcal F$，有 $h\mathbf1_B\in\mathcal M(h,\mathcal F)$，从而

$$
A(h\mathbf1_B)=Ah\,\mathbf1_{\tau^{-1}B}
\in\mathcal M(h,\mathcal F).
$$

除以 $h$ 后，$q\mathbf1_{\tau^{-1}B}$ 为 $\mathcal F$ 可测。再除以非零的 $\mathcal F$ 可测函数 $q$，得到

$$
\mathbf1_{\tau^{-1}B}\text{ 为 }\mathcal F\text{ 可测},\qquad
\tau^{-1}\mathcal F\subseteq\mathcal F\quad\text{模零}.
\tag{3.2}
$$

以上仅使用等价测度下的可测性与有界指标，未声称 $U$ 在 $L^2(\nu_h)$ 中酉或一致有界。

现在回到原 Haar 空间，并置

$$
K_{\mathcal F}=L^2(\mathcal F,\mu)\subset H.
$$

它是闭子空间，(3.2) 给 $UK_{\mathcal F}\subseteq K_{\mathcal F}$。对任何依赖有限个低位的柱函数 $f$，充分大的 $m$ 满足 $U^{2^m}f=f$；柱函数在 $H$ 中稠密且 $U$ 酉，故

$$
U^{2^m}\longrightarrow I\quad\mathrm{SOT}.
\tag{3.3}
$$

因此，对 $f\in K_{\mathcal F}$，

$$
U^{-1}f=\lim_{m\to\infty}U^{2^m-1}f\in K_{\mathcal F},
\tag{3.4}
$$

其中每个近似向量属于同一个闭 $K_{\mathcal F}$。这付清了由单向 (3.2) 升级到双向因子的步骤；$K_{\mathcal F}$ 是 $U$ 的 reducing 子空间。

## 4. Odometer 的真 Haar 因子全为有限因子

记

$$
\Gamma=\mathbb Z[1/2]/\mathbb Z,
\qquad
\chi_{a/2^m}(y)=\exp\left(2\pi i\,a\,(y\bmod 2^m)/2^m\right).
$$

每个有限层的这些角色构成模 $2^m$ 有限商上的 Fourier 基；有限层柱函数稠密，故所有不同的 $\chi_\gamma$ 构成 $H$ 的一组正交归一基。又有

$$
U\chi_\gamma=e^{-2\pi i\gamma}\chi_\gamma.
\tag{4.1}
$$

不同 $\gamma\in\Gamma$ 给不同特征值，所以每个特征空间恰一维。

令 $P_{\mathcal F}$ 为 $K_{\mathcal F}$ 的正交投影。由 (3.4)，$P_{\mathcal F}$ 与 $U$ 交换，故它在每个一维特征空间上为 $0$ 或 $I$。于是有唯一集合 $\Lambda\subseteq\Gamma$ 使

$$
K_{\mathcal F}
=\overline{\operatorname{span}}\{\chi_\gamma:\gamma\in\Lambda\}.
\tag{4.2}
$$

$1\in K_{\mathcal F}$ 给 $0\in\Lambda$。若 $\gamma,\eta\in\Lambda$，相应角色是有界的 $\mathcal F$ 可测函数，因此其乘积和复共轭仍为 $\mathcal F$ 可测函数。由

$$
\chi_\gamma\chi_\eta=\chi_{\gamma+\eta},\qquad
\overline{\chi_\gamma}=\chi_{-\gamma},
$$

可知 $\Lambda$ 是 Prüfer $2$ 群 $\Gamma$ 的子群。

若 $\Lambda$ 中元素的阶无统一上界，则对每个 $m$，$\Lambda$ 中某个阶至少为 $2^m$ 的元素所生成的循环群包含全部 $2^m$ 阶角色。所以 $\Lambda$ 包含每个有限层，必等于 $\Gamma$。否则 $\Lambda$ 包含于某个有限循环群 $2^{-m}\mathbb Z/\mathbb Z$，因而有限。

因此 (4.2) 只有两类：

1. $K_{\mathcal F}$ 有限维，$\mathcal F$ 模零是有限原子 $\sigma$-代数；
2. $K_{\mathcal F}=H$，$\mathcal F$ 模零是完整 Haar $\sigma$-代数。

第二条中，任意 Haar 指标都属于 $K_{\mathcal F}$，所以确实得到完整的测度代数；第一条也可直接由 (4.2) 看出 $\mathcal F$ 包含在相应有限层的测度代数中。

## 5. 完成主定理

若 $\mathcal F$ 是有限原子因子，$\nu_h$ 与 $\mu$ 等价且有限，故 $L^2(\mathcal F,\nu_h)$ 和 $\mathcal M(h,\mathcal F)$ 都是同一个有限正维数。由于 $A$ 单射，$A|_{\mathcal M(h,\mathcal F)}$ 单射；同时

$$
\|(A|_{\mathcal M(h,\mathcal F)})^n\|
\le\|A^n\|,
$$

所以该有限维限制拟幂零，因而幂零。这与非零有限维空间上的单射性矛盾。

故只能是 $\mathcal F$ 完整。在这种情况下，对任意 $f\in H$，$f/h$ 可测且

$$
\int |f/h|^2\,d\nu_h=\int|f|^2\,d\mu<\infty.
$$

于是 $f\in\mathcal M(h,\mathcal F)$，即该子空间等于 $H$。主定理得证。$\square$

## 6. 所有闭逐点子格都被覆盖

这里将复闭子格定义为闭复线性子空间 $M\subseteq H$，同时对逐点复共轭和逐点绝对值封闭。下面不用外部表示定理，直接构造 (1.2)。

设 $M\ne0$ 是这样的闭子格，且 $AM\subseteq M$。取可数稠密列 $f_j\in M$，并选正数 $a_j$ 使 $\sum_j a_j\|f_j\|_2<\infty$。则

$$
h=\sum_j a_j|f_j|\in M,
$$

其支撑为 $M$ 的公共支撑。与引理 2.1 相同的支撑证明给 $h>0$ 几乎处处。

乘以 $1/h$ 将 $M$ 等距对应到 $L^2(\nu_h)$ 中的闭子格 $L$，且 $1\in L$。令

$$
\mathcal F=\{B:\mathbf1_B\in L\}\quad\text{按零测集完成}.
\tag{6.1}
$$

补集、有限交、有限并由 $1\in L$ 以及格运算给出；可数并由有界指标的 $L^2(\nu_h)$ 极限给出，因为 $\nu_h(X)=\|h\|_2^2<\infty$。故 $\mathcal F$ 为子 $\sigma$-代数。

对任意实 $g\in L$ 和 $c\in\mathbb R$，

$$
\min\{1,n(g-c)_+\}\in L,
$$

其 $L^2(\nu_h)$ 极限为 $\mathbf1_{\{g>c\}}$，所以 $g$ 为 $\mathcal F$ 可测。复函数分别处理实部、虚部，得到 $L\subseteq L^2(\mathcal F,\nu_h)$。反向包含由 $\mathcal F$ 指标和简单函数的稠密性给出。因此

$$
M=hL^2(\mathcal F,\nu_h)=\mathcal M(h,\mathcal F).
$$

主定理遂给 $M=H$。

**推论 6.1。** 原 $A$ 没有非零真闭逐点子格。特别不能通过某个真可测因子的函数类、再乘任意固定可测权来构造普通不变子空间。

这严格扩大了 R107 的连续函数空间闭理想与 Haar 支撑理想讨论；证明不是把连续函数的闭包无条件搬到 $H$。

### 6.2 每个非零向量的正向轨道生成整个闭子格

固定任意 $f\ne0$，令 $L_f$ 是包含所有 $A^nf$（$n\ge0$）的最小闭复逐点子格。因为 $w>0$，实际加权复合同时满足
$$A|g|=|Ag|,\qquad A\overline g=\overline{Ag}.$$
因此 $A$ 将由轨道通过有限复线性组合、绝对值和复共轭生成的格子空间映入自身；有界性再保持其闭包，故 $AL_f\subseteq L_f$。$L_f\ne0$，推论6.1遂给 $L_f=H$。这里证明的是闭子格生成性质，不能删去格运算而声称通常的线性循环性。

## 7. 逐点保正正交投影及相位共轭

**引理 7.1。** 若 $P$ 是 $H$ 上逐点保正的正交投影，则 $\operatorname{Ran}P$ 是复闭逐点子格。

**证明。** 保正性使 $P$ 与逐点复共轭交换。对任意复 $f$，由每个实 $\theta$ 的

$$
\operatorname{Re}(e^{i\theta}Pf)
=P\operatorname{Re}(e^{i\theta}f)\le P|f|
$$

及可数稠密的 $\theta$，得 $|Pf|\le P|f|$ 几乎处处。若 $Pf=f$，则

$$
0\le |f|\le P|f|,
\qquad \|P|f|\|_2\le\||f|\|_2.
$$

平方积分的严格单调性迫使 $P|f|=|f|$。因此值域对绝对值和复共轭均封闭。$\square$

**推论 7.2。** 若 $P$ 正交且 $A\operatorname{Ran}P\subseteq\operatorname{Ran}P$，那么 $P$ 逐点保正当且仅当 $P=0$ 或 $P=I$。

更一般地，设 $u$ 为可测逐点相位，$|u|=1$ 几乎处处。如果

$$
M_{\bar u}PM_u
$$

逐点保正，则仍有 $P=0$ 或 $I$。

最后一条的证明：由引理 7.1，$M_{\bar u}\operatorname{Ran}P$ 是闭子格；先按 §6 的不涉及 $A$ 的表示步骤，在其支撑上表示为 $kL^2(\mathcal F,k^2\mu)$，其中 $k\ge0$。乘回 $u$ 得原值域为某个 $\mathcal M(uk,\mathcal F)$。若它非零且 $A$ 不变，主定理给整个 $H$。支撑未预先满时，可把支撑补集作为额外零权原子纳入 $\mathcal F$，不改变所表示的子空间。

## 8. 普通问题的准确剩余范围

上述结论没有声称任意闭不变子空间都对逐点格运算封闭，也没有声称任意正交投影可通过逐点相位共轭变成保正投影。Hilbert 正密度、复对称性或一般正常有限秩见证均不提供这种额外序结构。

因此一般普通闭不变子空间、一般正正常主理想见证和既有边界 $N=M$ 问题仍然开放。本稿的完成内容是一个完整结构类别的排除，不能把它与旧的其他类别排除合并宣称全部普通子空间已被排除。
