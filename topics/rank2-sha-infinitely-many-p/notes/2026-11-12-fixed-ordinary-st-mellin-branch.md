# 固定普通 CM 盘、实际 Heegner 点与指定 Amice 分支

日期：2026-11-12。状态：本文的固定周期/ST 比较、整测度、
实际 CM 点识别和原始 Gauss 恒等式均已证明。
Cornut 的全迹归纳及最终非零进程见
[配套证明](2026-11-12-cornut-fixed-branch-and-nonzero-progression.md)。
这里保留原始模参数化及全部类群和，不改成一个未说明 Euler 因子的
稳定化测度。本文不证明原课题的增广底层非零。

## 1. 固定的代数数据与普通素数

沿用 R103–R105、R114：
$$
F=\mathbb Q(\sqrt{-15}),\quad E:y^2=x^3-17x,\quad N=9248,
$$
$$
\Phi=\pi d_1+\pi d_3:X_0(3N)\longrightarrow E,\qquad
\Psi=[2]\Phi,\qquad \pi(\infty)=O.
\tag{1.1}
$$
这里 $d_1,d_3$ 表示两条退化映射；在 R105 中第二条也记作 $d_2$。
对相容的导子 $c$、$3\nmid c$ 的 Heegner 点，有实际等式
$$
\Psi(z_c)=2(1+\tau_3)P[c].
\tag{1.2}
$$
$\tau_3$ 是 R105 构造的可逆分歧理想的 Artin 元，$\tau_3^2=1$，
并非在求迹时任取的二阶提升。

对最大阶 CM 点 $c=z_1$ 及其 Galois 共轭，R100 的基层 Heegner
扭性与 R107 的 $E(F^{\rm ab})_{\rm tors}=E[2]$ 给
$$
\Psi(c)=O.
\tag{1.3}
$$
在每个这样的 $c$，选一次代数局部参数 $t$ 及 CM 本征 de Rham 基。
令 $v_c(t)$ 是由 Gauss–Manin 水平化定义的 Hodge 线比值，
规范为 $v_c(0)=0$、$v_c'(0)=1$。固定
$$
\mathcal F_c(v)=\log_E\Psi(t_c(v))
 =\sum_{m\ge1}b_{c,m}v^m,\qquad
h_{c,m}=m!b_{c,m},\qquad t_c=v_c^{-1}.
\tag{1.4}
$$
所有系数在一个固定数域内。这正是 R114 使用的系数，并非另选
随指标 $m$ 改变的普通坐标系数。

以后固定
$$
q=61.
\tag{1.5}
$$
它不整除 $3N\cdot15$，且
$61=N_{F/\mathbb Q}(1+2\sqrt{-15})$；故 $q$ 在 $F$ 中分裂，
其两个素理想均主。在 $E$ 上 $a_{61}=-12$，也为普通约化
（R107 已有准确点数）。最大阶 CM 椭圆曲线在此处普通，
且其约化自同态环仍为 $\mathcal O_F$：后者已为最大阶，
而普通约化的自同态代数是同一个虚二次域。

取一个 $q$ 进嵌入，令 $\mathcal R=W(\overline{\mathbb F}_q)$，
$\mathcal B=\operatorname{Frac}\mathcal R$，必要时先作一个固定的
有限未分歧扩张以容纳基点和 prime-to-$q$ 标记，再嵌入此环。
该环完备，估值规范为 $v_q(q)=1$。允许使用整个未分歧完备环
是为了选普通 Tate 模的基，不把这些基误说成固定数域中的元素。

## 2. 固定 period 比准确等于 ST 对数的常数倍

Serre–Tate 理论把 $c$ 的普通变形盘识别为
$$
\operatorname{Spf}\mathcal R[[T]],\qquad Q_{\rm ST}=1+T.
\tag{2.1}
$$
原点 $T=0$ 是 canonical lift；最大 CM 提升就是这个原点。
prime-to-$q$ 的 $N$ 与 $3$ 层结构唯一延伸，不增加变形参数。
也可先取一个细模 étale 图再忘记辅助标记。

这里使用 Katz，*Serre–Tate local moduli*（1981），
Theorem 2.1 及 Main Theorems 4.3.1–4.3.2。在其普通 Tate 基对应
的 de Rham 基中，椭圆曲线情形的公式为
$$
\nabla\omega_{\rm ST}
 =\eta_{\rm ST}\otimes d\log(1+T),\qquad
\nabla\eta_{\rm ST}=0.
\tag{2.2}
$$
$\omega_{\rm ST}$ 生成 Hodge 线，$\eta_{\rm ST}$ 是单位根方向。
所以
$$
e_1=\omega_{\rm ST}-\log(1+T)\eta_{\rm ST},
\qquad e_2=\eta_{\rm ST}
\tag{2.3}
$$
是水平基，且在 $T=0$ 等于相应的 CM 本征基。普通 CM 点的两个
CM 本征方向正是 Hodge 方向和单位根方向。因此，与 (1.4) 的
固定 CM 基相比，(2.3) 的初值只差对角常数，不出现把 Hodge
本征线与另一条线混合的任意线性变换。Hodge 线在水平基中的
比值遂给准确形式恒等式
$$
\boxed{\quad v_c(t(T))=\kappa_{c,q}\log(1+T),
\qquad \kappa_{c,q}\in\mathcal B^\times.\quad}
\tag{2.4}
$$
规范 $v_c'(0)=1$ 给
$\kappa_{c,q}=(dT/dt|_0)^{-1}$。若初始代数参数及 CM 基选在
$61$ 处整且严格，则它是单位；对已有的任何固定代数规范，
只需保留非零常数 $\kappa_{c,q}$。以下非零论证不要求其为单位，
更不将它视为一个全局有理周期。

**收敛范围须区分。** (2.4) 及
$\mathcal F_c(\kappa_{c,q}\log(1+T))$ 首先是形式恒等式，
也在足够小的盘上是解析恒等式。在 $q$ 次幂根单位处，
不能把 $\log\zeta=0$ 直接代回 (1.4) 推断点像为零：
该复合展开未必在那里收敛。后面在整个开单位盘使用的是原映射
$\Psi(t(T))$ 的形式群对数及其有界微分所确定的原函数。

## 3. 原始整测度与准确阶乘

记实际映射的原函数为
$$
\mathscr F_c(T)=\log_E\Psi(t(T)),\qquad
D=(1+T)\frac d{dT},\qquad G_c(T)=D\mathscr F_c(T).
\tag{3.1}
$$
$E$ 在 $q$ 处好约化，固定映射在光滑模曲线模型上延伸为
到其 Néron 模型的态射；(1.3) 使其正式像位于 $E$ 的正式群。
故不变微分的拉回满足
$$
\mathscr F_c(0)=0,\qquad
\mathscr F_c'(T)\in\mathcal R[[T]],\qquad
G_c(T)\in\mathcal R[[T]].
\tag{3.2}
$$
特别地，$\mathscr F_c$ 的第 $n$ 个系数的估值至少 $-v_q(n)$，
它在整个 $|T|_q<1$ 上收敛。这里无需假定 $\mathscr F_c$ 本身
是有界幂级数。

存在唯一的有界 $\mathcal R$ 值测度 $\mu_c$，使
$$
G_c(T)=\int_{\mathbb Z_q}(1+T)^x\,d\mu_c(x).
\tag{3.3}
$$
这是 Mahler–Amice 对应；本处可直接构造：若
$G_c=\sum g_nT^n$，规定
$\int\binom{x}{n}\,d\mu_c=g_n$。Mahler 展开中系数趋于零，
而所有 $g_n$ 整，因此该规则唯一延伸为连续函数上的范数至多一
的线性泛函。故本篇所需的有界性不是从未经整化的 $L$ 值推测的。

由 (2.4) 作形式链式法则，$D=\kappa_{c,q}\partial_v$，遂有
$$
\boxed{\quad
\int_{\mathbb Z_q}x^{m-1}\,d\mu_c(x)
=D^{\,m-1}G_c(0)
=\kappa_{c,q}^{\,m}h_{c,m}\qquad(m\ge1).
\quad}
\tag{3.4}
$$
阶乘已在 $h_{c,m}=m!b_{c,m}$ 中，不能再删去或添加。

定义指定分支
$$
\mathscr M_c(W)
=\int_{\mathbb Z_q^\times}
x^{-1}(1+W)^{\log\langle x\rangle/\log(1+q)}
\,d\mu_c(x)\in\mathcal R[[W]].
\tag{3.5}
$$
这里 $\langle x\rangle=x/\omega(x)$，$\omega$ 是 Teichmüller 特征。
完整的 $x^{-1}=\omega(x)^{-1}\langle x\rangle^{-1}$ 保留了 tame
指数 $-1$，并保留 wild 变量的一次平移。
若 $q-1\mid m$，准确有
$$
\int_{\mathbb Z_q^\times}x^{m-1}\,d\mu_c(x)
=\mathscr M_c((1+q)^m-1),
\tag{3.6}
$$
$$
v_q\left(\int_{q\mathbb Z_q}x^{m-1}\,d\mu_c(x)\right)\ge m-1.
\tag{3.7}
$$
(3.7) 是直接的整测度估计，而不是未核定的去 Euler 因子公式。

## 4. 根单位确实给原始导子 CM 点

设 $n\ge1$。Katz Theorem 2.1(4) 的提升判据在当前一维普通
情形表述为：若 $\alpha\in\mathcal O_F$ 在
$F\otimes\mathbb Q_q=\mathbb Q_q\times\mathbb Q_q$ 的两个分量为
$\alpha_1,\alpha_2$，则它提升为参数 $Q_{\rm ST}$ 上的自同态，
当且仅当
$$
Q_{\rm ST}^{\,\alpha_1-\alpha_2}=1.
\tag{4.1}
$$
若 $Q_{\rm ST}$ 是本原 $q^n$ 次根单位，此条件恰为
$\alpha_1\equiv\alpha_2\pmod{q^n}$。由 $q\nmid\operatorname{disc}F$，
满足它的全局阶正是
$$
\mathcal O_{q^n}=\mathbb Z+q^n\mathcal O_F.
\tag{4.2}
$$
约化映射对自同态单射，且约化端的自同态环为 $\mathcal O_F$，
所以没有额外的未知自同态需要排除。

也可从 canonical lift 的混合型循环 $q^n$ 子群构造这些商。
普通乘法型及 étale 型 Tate 基下，源的 ST 参数为一；
isogeny 的提升判据使其商参数满足 $Q_{\rm ST}^{q^n}=1$，
而下降到恰好 $\mathcal O_{q^n}$ 的商给本原根。
这把形式提升识别为实际代数 CM 椭圆曲线，而非仅一个形式
自同态条件的解。所有 prime-to-$q$ 层结构按商同源运输。

环类群的准确正合列为
$$
1\longrightarrow
(\mathcal O_F/q^n\mathcal O_F)^\times/
(\mathbb Z/q^n)^\times
\longrightarrow\operatorname{Pic}(\mathcal O_{q^n})
\longrightarrow\operatorname{Pic}(\mathcal O_F)
\longrightarrow1.
\tag{4.3}
$$
$\mathcal O_F^\times=\{\pm1\}$ 已在对角标量群内。由于 $q$ 分裂，
左侧由两个分量之比识别为 $(\mathbb Z/q^n)^\times$，
阶数恰为 $\varphi(q^n)$。
在 $q$ 的一个素位处，局部单位映入该比值的一个分量，因此
惯性满射左侧；这给环类扩张相对于最大环类域的全惯性轨道。
两个 $q$ 上素理想在 $\operatorname{Pic}(\mathcal O_F)$ 中均主，
所以取模曲线的既定 CM 理想层结构时，水平 Frobenius 不把这个
canonical 基点移到另一个类群点。

因此，固定相容的根单位与局部互反方向后，
$$
T=\zeta_{q^n}^{\,a}-1,\qquad
a\in(\mathbb Z/q^n)^\times
\tag{4.4}
$$
准确遍历一个最大阶 CM 点上方的全部原始导子 $q^n$ 提升。
它们是标准 $z_{q^n}$ 在 (4.3) 左侧群下的轨道；若最初选了
另一个相容代表，只对整条轨道施加一次 Galois 平移。
这里的 $N$ 理想取向与分歧 $3$ 层结构都沿用 (1.2)，因而
$$
\mathscr F_c(\zeta_{q^n}^{\,a}-1)
=\log_E\bigl(2(1+\tau_3)P[q^n]^{\sigma_a}\bigr)
\tag{4.5}
$$
（或者把所有 $\sigma_a$ 同时换成 $\sigma_{a^{-1}}$）。
这个结论不来自“导子相同”一个条件，而同时用了固定普通盘、
完整惯性轨道、CM 理想层结构及实际退化映射。

## 5. 原函数的 Gauss 公式：恰是所需 tame 分支

在 $|T|_q<1$ 中有收敛恒等式
$$
\mathscr F_c(T)
=\int_{\mathbb Z_q}
\frac{(1+T)^x-1}{x}\,d\mu_c(x).
\tag{5.1}
$$
$x=0$ 处的核按极限 $\log(1+T)$ 定义。严格的逐项交换依据是
$$
\frac{(1+T)^x-1}{x}
=\sum_{k\ge1}\frac1k\binom{x-1}{k-1}T^k.
\tag{5.2}
$$
对 $x\in\mathbb Z_q$，二项式系数整，故 (5.2) 在每个
闭子盘上对 $x$ 一致收敛；施加 $D$ 后得 (3.3)，常数均为零，
所以它就是原映射的实际原函数。

令 $\psi$ 是 conductor 恰为 $q^n$ 的乘法字符，$n\ge2$，
且其 tame 部分平凡。置
$$
\tau(\psi^{-1})
=\sum_{a\in(\mathbb Z/q^n)^\times}
\psi(a)^{-1}\zeta_{q^n}^{\,a}.
$$
原始 Gauss 正交性及 (5.1) 给
$$
\boxed{\quad
\sum_{a\in(\mathbb Z/q^n)^\times}
\psi(a)^{-1}\mathscr F_c(\zeta_{q^n}^{\,a}-1)
=\tau(\psi^{-1})
\int_{\mathbb Z_q^\times}x^{-1}\psi(x)\,d\mu_c(x).
\quad}
\tag{5.3}
$$
具体地，对 $q\nmid x$，代换 $b=ax$ 给内和
$\psi(x)\tau(\psi^{-1})/x$；对 $q\mid x$，原始性使内和为零。
核的常数项因 $\sum_a\psi(a)^{-1}=0$ 消失，$x=0$ 的极限项
因 $\log\zeta_{q^n}=0$ 消失。Gauss 和非零；互反方向或一次
轨道平移仅改非零标量或把所有字符取逆。

若 $\xi=\psi(1+q)$，则右侧积分恰为
$\mathscr M_c(\xi-1)$。结合 (4.5)，(5.3) 是实际
$2(1+\tau_3)P[q^n]$ 的 primitive wild Fourier **对数**，
已包含将来需要的全部类群和与 tame 求和。
故
$$
\mathscr M_c\equiv0
\quad\Longrightarrow\quad
\text{各层新的 primitive wild 对数分量全部为零}.
\tag{5.4}
$$
不能仅靠 imprimitive Gauss 和去掉旧层，也不能以
$E(H)\otimes\mathbb Q_q\to\mathbb C_q$ 的虚假注入性处理它们。
配套证明先对实际点施加整数算子
$q-\sum_{\operatorname{Gal}(H_n/H_{n-1})}g$，
再用原始 Heegner 迹递推，逐层得到真实点扭性，最后与 Cornut
的已发表原始迹非扭定理矛盾。因而它得到的正是
(3.5) 的非恒零性，而不是“存在某个分支非零”。

## 6. 与固定系数的接口及精确范围

一旦配套证明给出 $\mathscr M_c\ne0$，其首个非零系数和 (3.7)
给：存在固定整数 $k,m_0$，使
$$
m\ge m_0,\qquad 60\cdot61^k\mid m
\quad\Longrightarrow\quad h_{c,m}\ne0.
\tag{6.1}
$$
完整估值证明在配套证明 §5。要点是指定单位分支在
$W=(1+61)^m-1$ 的估值为 $O(\log m)$，而非单位测度的误差
估值至少 $m-1$；因此充分大 $m$ 不会抵消。

对 R114 所需的有限个 Galois 共轭基点，可逐一应用同一论证，
再取最大的 $k,m_0$。也可固定一个系数数域并对 Galois 共轭
的非零 $h_{c,m}$ 取范数。这里只有固定 $q=61$ 的解析插值；
其他输入素数处的单位性仍须用独立的分母、高度和素数乘积
估计完成，不从 (6.1) 直接推出。

## 7. 原始来源

1. N. Katz, *Serre–Tate local moduli*, in *Surfaces algébriques*,
   Lecture Notes in Mathematics **868** (1981), 138–202：
   Theorem 2.1，尤其 (4) 的同态提升判据；Main Theorems
   3.7.1–3.7.3 及 4.3.1–4.3.2，后者在印刷第 175 页。
   [作者原文](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)。
2. K. Mahler, *An interpolation series for continuous functions of a
   p-adic variable*, J. reine angew. Math. **199** (1958), 23–34，
   [DOI](https://doi.org/10.1515/crll.1958.199.23)；
   Y. Amice, *Interpolation p-adique*, Bull. Soc. Math. France
   **92** (1964), 117–180，
   [原刊](https://www.numdam.org/articles/10.24033/bsmf.1606/)。
   本文 (3.3) 所需有界泛函的构造已直接给出。
3. C. Cornut, *Mazur's conjecture on higher Heegner points*,
   Invent. Math. **148** (2002), 495–523：
   引言主定理及 §4.1 Lemma 4.2；
   [发表排版版](https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf)。
   其全迹非扭输入及所有初层因子由配套证明单独核定。
