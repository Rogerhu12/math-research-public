# 已知 CM 点的有限处分离：交换子与约化饱和性

日期：2026-11-12；会话：`serre-uniformity-astra/2026-11-12`。

**状态：已证明的辅助命题。** 这里完整证明一个有限处交点的必要条件，并推出：素数层 $p\ge53$ 时，在任意辅助素数 $\ell\ge5$、$\ell\ne p$，标准的不同有理 Heegner CM 点有不同的约化。这只处理已知 CM 点之间的碰撞，未证明非 CM 点不存在，也未证明 QC 函数在 CM 点的导数非零。

这个必要条件对应 Love–Studnia–Vonk 2026 年预印本 Lemma 3.16 的简单部分；下文独立写出所需证明，**不把该预印本的完整算术交数公式当作已公认前提，也不声称必要条件的新颖性**。

## 1. 标准输入与符号

取两个不同的素数 $p,\ell$。令 $E_1,E_2/\overline{\mathbb Q}_\ell$ 为 CM 椭圆曲线，它们的完整几何自同态环为虚二次整环
$$
\mathcal O_i=\operatorname{End}_{\overline{\mathbb Q}_\ell}(E_i),
\qquad \operatorname{disc}(\mathcal O_i)=\Delta_i<0.
$$
假定 $p$ 在两环中均非分歧且惰性，即 $\mathcal O_i/p\mathcal O_i\simeq\mathbb F_{p^2}$。它们在 $E_i[p]$ 上的作用给出非分裂 Cartan 结构：这里将 Cartan 结构理解为 $\operatorname{End}_{\mathbb F_p}(E_i[p])$ 中相应的二次子代数，不选择该代数与 $\mathbb F_{p^2}$ 的定向同构。

CM 曲线有潜在好约化。取共同有限扩张 $L/\mathbb Q_\ell$，使两曲线均有好约化、所有几何自同态均定义于 $L$。必要时继续扩大 $L$。使用如下标准椭圆曲线事实：

1. 好约化给出自同态的单射约化映射；素于 $\ell$ 的挠群约化保持同构。
2. 若自同态杀掉 $E[n]$，其中 $n$ 素于域的特征，则它通过商映射 $[n]$ 分解。
3. 椭圆曲线的几何自同态代数是 $\mathbb Q$、虚二次域或正定四元数代数；其标准对合来自对偶同源，约化范数等于同源次数。

第 1、2 项可见 Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed. (2009), III §4、III §6、VII §3。第 3 项及这里使用的正定性在 John Voight, *Quaternion Algebras* (Springer, 2021), §42.1.3、Lemma 42.1.5 中；[开放原文](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)。同章 Theorem 42.1.9 的证明也明确给出第 2 项所需的 $\operatorname{End}(E)/n\operatorname{End}(E)\hookrightarrow\operatorname{End}(E[n])$。

以下范数、迹记作 $\operatorname{nrd}$、$\operatorname{trd}$；在虚二次域中分别就是通常的范数、迹。

## 2. C1：交换子的整数必要条件

**命题 C1。** 假定 $E_1,E_2$ 的几何约化存在一个同构，且此同构保持上述 $p$-Cartan 结构。把两条约化曲线据此认作同一条 $E_0$。若两 CM 域在
$$
R_{\mathbb Q}:=\operatorname{End}_{\overline{\mathbb F}_\ell}(E_0)\otimes\mathbb Q
$$
中的像不同，则存在整数 $t$，使
$$
\frac{\Delta_1\Delta_2-t^2}{4p^2}\in\mathbb Z_{>0}.
\tag{C1}
$$
特别地，$4p^2\le\Delta_1\Delta_2$。

**证明。** 记 $R=\operatorname{End}(E_0)$。选择 $a_i\in\{0,1\}$ 满足 $a_i\equiv\Delta_i\pmod2$，并取 $\mathcal O_i$ 的生成元
$$
u_i=\frac{a_i+\sqrt{\Delta_i}}2.
$$
仍用 $u_i$ 表示它在 $R$ 中的约化。其约化迹为 $a_i$。因为两个 Cartan 子代数在 $E_0[p]$ 上相同，$u_1,u_2$ 在此挠群上的作用交换。因此
$$
w=[u_1,u_2]=u_1u_2-u_2u_1
$$
杀掉 $E_0[p]$。由同源商的性质，存在 $\beta\in R$ 使
$$
w=[p]\circ\beta=p\beta.
\tag{C1.1}
$$
若 $w=0$，则 $u_2$ 位于非实二次元素 $u_1$ 的中心化子中。在虚二次代数中这是整个二次域；在四元数代数中这也是 $\mathbb Q(u_1)$。因此两 CM 域的像相同，与假设矛盾。故 $w\ne0$，并且 $R_{\mathbb Q}$ 是正定四元数代数。

设 $x_i=2u_i-a_i$。则 $x_i$ 的约化迹为零，$x_i^2=\Delta_i$。记
$$
t=\frac12\operatorname{trd}(x_1x_2)
  =2\operatorname{trd}(u_1u_2)-a_1a_2\in\mathbb Z.
$$
最后的整数性来自椭圆曲线自同态的整数特征多项式。由于 $x_i$ 为纯四元数，$\overline{x_1x_2}=x_2x_1$，所以
$$
x_1x_2+x_2x_1=2t,
\qquad
\operatorname{nrd}(x_1x_2)=\Delta_1\Delta_2.
$$
由 $w=(x_1x_2-t)/2$，得到
$$
\operatorname{nrd}(w)
=\frac{\Delta_1\Delta_2-t^2}{4}.
\tag{C1.2}
$$
另一方面，(C1.1) 给出
$$
\operatorname{nrd}(w)=p^2\operatorname{nrd}(\beta)
 =p^2\deg(\beta).
$$
因为 $\beta\ne0$，其次数为正整数，结合 (C1.2) 即得 (C1)。证毕。

## 3. C2：交换子为零时只能改变约化素数处的导子

先证明需要的饱和性，避免把不同 CM 环约化后可能重合的情况漏掉。

**引理 C2a。** 设 $E/\overline{\mathbb Q}_\ell$ 有好约化 $E_0$，$\mathcal O=\operatorname{End}(E)$，$R=\operatorname{End}(E_0)$。在约化嵌入下，商
$$
(R\cap\mathcal O_{\mathbb Q})/\mathcal O
$$
是 $\ell$-初等幂阶群，即它的阶只能有素因子 $\ell$。

**证明。** 只需证明该有限群没有素于 $\ell$ 的挠元。令 $n$ 素于 $\ell$，$\alpha\in R\cap\mathcal O_{\mathbb Q}$ 且 $n\alpha$ 是某个 $\varphi\in\mathcal O$ 的约化。扩大好约化的定义域，使相关映射和挠点定义良好。约化 $\bar\varphi=n\alpha$ 杀掉 $E_0[n]$；素于 $\ell$ 的挠群在约化下同构，故 $\varphi$ 也杀掉 $E[n]$。

于是 $\varphi=[n]\circ\psi$，其中 $\psi\in\mathcal O$。约化后得 $n\alpha=n\bar\psi$。自同态环作为阿贝尔群无挠，故 $\alpha=\bar\psi\in\mathcal O$。证毕。

**命题 C2。** 在 C1 的设定下，不再要求两 CM 域的像不同。若不存在满足 (C1) 的整数 $t$，则
$$
\Delta_1/\Delta_2=\ell^{2r}
\quad\text{对某个 }r\in\mathbb Z.
\tag{C2}
$$

**证明。** C1 表明两个 CM 域的像必相同，记为 $K\subset R_{\mathbb Q}$。令 $\mathcal O_0=R\cap K$，它是 $K$ 中的一个二次整环，包含两环的像。由 C2a，$[\mathcal O_0:\mathcal O_i]$ 都是 $\ell$ 的幂。二次整环的判别式在指数为 $d$ 的子环下乘以 $d^2$，因此 $\Delta_i=\ell^{2b_i}\operatorname{disc}(\mathcal O_0)$，其中 $b_i\ge0$。两式相除即得 (C2)。证毕。

## 4. C3：标准有理 Heegner CM 点在 $\ell\ge5$ 的统一分离

考虑标准的十三个类数一判别式
$$
\mathcal D=\{-3,-4,-7,-8,-11,-12,-16,-19,-27,-28,-43,-67,-163\}.
$$
对每个 $\Delta\in\mathcal D$，只在 $p$ 惰性时考虑由其 CM 自同态环产生的 Heegner Cartan 结构。这里的结论针对这些明确指定的点，无须先把“所有有理 CM 点均为 Heegner 点”的一般分类当作前提。

**命题 C3。** 若 $p\ge53$，$\ell\ge5$ 是不同于 $p$ 的素数，则上述不同 Heegner CM 点在 $X_{\rm ns}^+(p)$ 的模 $\ell$ 约化中两两不同。

**证明。** 假设判别式不同的两点约化相同。因 $\ell\ne p$ 且 $\ell\ge5$，非尖点部分在几何点上的模解释把它给为保持 Cartan 结构的约化曲线同构。可在共同有限扩张取得好约化，再应用 C1、C2。

对于不同的 $\Delta_1,\Delta_2\in\mathcal D$，有
$$
0<\Delta_1\Delta_2\le163\cdot67=10921
<4\cdot53^2\le4p^2.
$$
故 (C1) 不可能，必须满足 (C2)。但列表中两个不同判别式的比不可能是素数 $\ell\ge5$ 的非零偶次幂：若交换下标使 $r>0$，则 $\ell^{2r}\le163/3<55$，所以只需考虑 $\ell^{2r}=25$ 或 $49$；列表中没有比为 $25$ 或 $49$ 的一对数。$r=0$ 又要求判别式相同。矛盾。证毕。

同一类数一判别式给出唯一的几何 CM $j$ 值，且其完整 CM 环产生的子代数不依赖生成元的定向，因此不同指定点确实对应不同判别式。

## 5. 对 QC 的实际用途和界限

C3 允许统一取辅助素数 $\ell=5$，并在 $p\ge53$ 时确定：已知标准 CM 点占据互不相同的第一层剩余圆盘。于是逐圆盘 QC 认证不必先解决“两个不同已知 CM 点落在同一圆盘”的问题。

它没有给出 QC 函数的简单根条件。交换子范数控制的是两个 CM **点** 的碰撞；QC 函数的导数涉及所选 Hecke 对应、全局高度和 Mordell–Weil 闭包的数据。也没有证明不含 CM 点的圆盘无有理点。两项缺口都不能由 C3 或类数一分类补齐。

## 6. 2026 年文献的位置

Jonathan Love, Élie Studnia and Jan Vonk, *Arithmetic intersections on non-split Cartan modular curves*, [arXiv:2604.06963](https://arxiv.org/abs/2604.06963)，2026-04-08；[作者原文](https://jonathanlove.info/Love_Studnia_Vonk.pdf)。作者网页列为 submitted。

其 Theorem A 给出正规模型光滑非尖点部分的模解释；Theorem B 对互素基本判别式给出完整有限处交数；Lemma 3.16 处理更一般判别式的必要条件。§4 与 Table 1 还确定全部有理 CM 点的有限处交数。需特别区分同 CM 域、不同导子的退化配对：$(-3,-12)$、$(-3,-27)$、$(-4,-16)$、$(-7,-28)$ 在素数 $2$ 或 $3$ 可能持续相交。因此“足够大层的 CM 点在所有有限处均分离”是错误的表述。C3 的 $\ell\ge5$ 限制有实际意义。

本笔记只重证用于辅助好约化素数处的必要条件，未复现该预印本的完整交数公式和坏约化模型。
