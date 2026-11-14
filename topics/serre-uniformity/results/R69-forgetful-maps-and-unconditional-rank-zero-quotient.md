# R69：忘线映射直接构造实际秩零商

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文把 R66 的已发表非消失输入接到一个实际的模曲线 Jacobian 商。证明使用 $p+1$ 个忘线映射的完整推拉矩阵、有限 étale 下降，以及 Bertolini–Darmon (1997) 的已发表秩零定理；不引用 Studnia submitted 论文的商构造或 Theorem B。

具体地，在 R66 的小惯性分支，若三次商的 Artin 导子 $M$ 满足 $M<p$，则每个配对分支的同余模曲线 $X_E^\alpha(p)$ 都有一个正维 Jacobian 商，其有理点群有限。该商与一个非 Galois 三次域上的迹零 Weil 限制核同源。

这补上真实秩零商的接口，尚未证明分母排除：尖点处的模 $\ell$ 非退化与 exceptional 条件仍须处理；$M$ 也尚无统一上界。

## 1. 精确设置与结论

设 $p>37$、$E/\mathbb Q$ 无 CM，并有实际完整像
$$\rho_{E,p}(G_{\mathbb Q})=N=C\rtimes\langle c\rangle,\qquad C\simeq\mathbb F_{p^2}^{\times}.$$
采用 R66 的严格小惯性假设
$$\rho_{E,p}(I_p)\subsetneq C.$$
由 R66，$p\equiv2,5\pmod9$、惯性恰为 $C^3$。取阶三字符 $\vartheta:C\to\mu_3$，并记
$$
\eta=\vartheta\circ\rho_{E,p}|_{G_K},\qquad
L/\mathbb Q:\ \operatorname{Gal}(L/\mathbb Q)=S_3=N/C^3,
$$
其中 $K$ 是二次商域。令 $F\subset L$ 为任一个非 Galois 三次子域。R66 给
$$\mathfrak f(\eta)=c_\eta\mathcal O_K,\qquad
M=Dc_\eta^2,\qquad D=|D_K|,\qquad p\nmid M.$$
$\eta$ 是导子 $c_\eta$ 的原始环类字符。

对任意定义于 $\mathbb Q$ 的非退化 Weil 配对数据 $\alpha$，令
$$X=X_E^\alpha(p),\qquad J=\operatorname{Jac}(X).$$
几何上 $X$ 是连通的完整水平 $p$ 模曲线 $X(p)$；其非尖点参数化带有规定配对乘子的 $E[p]\simeq E'[p]$ 同构。这里不假定该配对分支一定已有有理点。

对水平 $p$、权二、平凡 nebentype 的归一化新形式 $g$，令 $A_g$ 是其 Galois 轨道对应的 $J_0(p)$ 因子，$d_g=\dim A_g=[K_g:\mathbb Q]$。置
$$
B_g=\ker\!\left(
\operatorname{Tr}_{F/\mathbb Q}:
\operatorname{Res}_{F/\mathbb Q}A_g\longrightarrow A_g
\right).
\tag{69.1}
$$
该核几何上为三份 $A_g$ 的求和映射之核，故连通、维数 $2d_g$。

**定理 69.1。** 对每个这样的 $g$，$J$ 都有一个定义于 $\mathbb Q$ 的商，与 $B_g$ 在 $\mathbb Q$ 上同源。若
$$L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0,\tag{69.2}$$
则
$$B_g(\mathbb Q)\text{ 有限},\qquad
A_g(F)\otimes\mathbb Q=A_g(\mathbb Q)\otimes\mathbb Q.
\tag{69.3}$$
后一等式在 $A_g(L)\otimes\mathbb Q$ 中理解。

**推论 69.2。** 如果 $p>M$，则 R66/Feigon–Whitehouse 给至少一个满足 (69.2) 的 $g$。所以对每个 $\alpha$，$J$ 有一个正维、Mordell–Weil 群有限的实际 $\mathbb Q$ 商。

这里的“实际商”不是仅指定一个抽象四维 Galois 表示；下文直接用曲线映射构造满射。

## 2. 全部忘线映射及完整推拉矩阵

令 $\Omega=\mathbb P(E[p])$ 为 $E[p]$ 中的一维子空间组成的有限 étale $\mathbb Q$ 概形。几何点数为 $p+1$。对每条几何线 $i\in\Omega(\overline{\mathbb Q})$，有忘线映射
$$
\pi_i:X_{\overline{\mathbb Q}}\longrightarrow X_0(p)_{\overline{\mathbb Q}},
\qquad (E',\varphi)\longmapsto(E',\varphi(i)).
\tag{69.4}
$$
它延拓到光滑射影模曲线。记 $J_0=J_0(p)$。

**引理 69.3。** 每个 $\pi_i$ 的次数为
$$d=\frac{p(p-1)}2,$$
且作为 $J_0\to J_0$ 的同态，
$$
\boxed{\quad
\pi_{i,*}\pi_j^*=
\begin{cases}
[d],&i=j,\\
[-(p-1)/2],&i\ne j.
\end{cases}
\quad}
\tag{69.5}
$$
另有严格同态等式
$$\sum_{i\in\Omega}\pi_i^*=0:J_0\longrightarrow J.
\tag{69.6}$$

**证明。** 几何覆盖 $X(p)\to X(1)$ 的甲板群是
$$G=\operatorname{PSL}_2(\mathbb F_p),\qquad |G|=p(p^2-1)/2.$$
某一条线的稳定子阶为 $p(p-1)/2$，其商为 $X_0(p)$，给映射次数 $d$。甲板群在 $\mathbb P^1(\mathbb F_p)$ 上双传递：它传递，而 $\infty$ 的稳定子含全部平移，故在另外的 $p$ 个点上传递。

令 $S=\sum_i\pi_i^*$。甲板群只置换这些映射，所以 $S$ 的像为 $G$ 不变。若 $q:X\to X(1)$ 为总商映射，则
$$\sum_{g\in G}g_*=q^*q_*=0\quad\text{在 }J\text{ 上},$$
因为 $\operatorname{Jac}(X(1))=0$。作用在 $S$ 上得到 $|G|S=0$。阿贝尔簇同态群无扭，故 $S=0$，证明 (69.6)。这不是只模去一个尖点挠点后的等式。

自推拉为 $\pi_{i,*}\pi_i^*=[d]$。对不同的 $i,j$，双传递及共同预复合一个甲板自同构说明 $\pi_{i,*}\pi_j^*$ 是与有序对无关的同一个同态 $U$。将 $\pi_{i,*}$ 作用在 (69.6) 上，得到
$$[d]+pU=0.$$
因 $d/p=(p-1)/2$ 为整数，同态群无扭给 $U=[-(p-1)/2]$。证毕。

因此完整矩阵为
$$
(\pi_{i,*}\pi_j^*)_{i,j}
=\frac{p^2-1}{2}I_{p+1}-\frac{p-1}{2}{\bf1}{\bf1}^{\mathsf T}.
\tag{69.7}
$$
对角方向是其核，在求和为零的方向上它恰为非零整数 $(p^2-1)/2$ 乘法。

## 3. 在 $\mathbb Q$ 上下降，而不是把非几何群元当甲板变换

定义
$$
\mathcal R=\operatorname{Res}_{\Omega/\mathbb Q}(J_0),\qquad
\mathcal T=\ker\!\left(\operatorname{Tr}:\mathcal R\to J_0\right).
\tag{69.8}
$$
这是沿有限 étale 概形的 Weil 限制。几何上
$$\mathcal R_{\overline{\mathbb Q}}=J_0^{\Omega},\qquad
\mathcal T_{\overline{\mathbb Q}}=\{(P_i):\sum_iP_i=0\},$$
故 $\mathcal T$ 为维数 $p\dim J_0$ 的阿贝尔簇。

Galois 对 (69.4) 的作用准确为
$$\sigma(\pi_i)=\pi_{\sigma i}.$$
目标 $X_0(p)$ 定义于 $\mathbb Q$；这个等式只用 $\varphi$ 运输子群的模解释，和配对分支 $\alpha$ 无关。因此
$$
\Psi:\mathcal R\longrightarrow J,\qquad
(P_i)\longmapsto\sum_i\pi_i^*P_i
\tag{69.9}
$$
与
$$
\Theta:J\longrightarrow\mathcal R,\qquad
Q\longmapsto(\pi_{i,*}Q)_i
\tag{69.10}
$$
都由 Galois 下降定义在 $\mathbb Q$ 上。

在 $\mathcal R$ 上记 $\mathcal J$ 为“先求和、再取对角”的整数同态，并令
$$P_0=(p+1)I-\mathcal J.$$
其像在 $\mathcal T$ 中，在 $\mathcal T$ 上为 $[p+1]$。由 (69.7)，
$$
\Theta\Psi|_{\mathcal T}=[(p^2-1)/2],\qquad
(P_0\Theta)\Psi|_{\mathcal T}=[(p+1)(p^2-1)/2].
\tag{69.11}
$$
所以 $\Psi|_{\mathcal T}$ 具有有限核，$P_0\Theta:J\to\mathcal T$ 为满射。所有这些是实际阿贝尔簇同态，分母已由 $P_0$ 清除。

**此处的群必须区分。** 计算 (69.5) 使用真正的几何甲板群 $\operatorname{PSL}_2(\mathbb F_p)$。而 $N$ 在本节只通过 Galois 对有限集合 $\Omega$ 的置换作用出现；下节的 $C^3$ 不会被冒充为保持某一配对分支的几何子群。

## 4. 三轨道投影给非 Galois 三次域的迹零核

令 $H=C^3\triangleleft N$。因为 $p\equiv-1\pmod3$，$3\nmid p-1$，故标量群 $\mathbb F_p^\times\subset H$。

$C$ 在 $\Omega$ 上传递，点稳定子恰为标量群；因此 $H$ 在 $\Omega$ 上恰有三个等长轨道。$N$ 对三轨道集合的作用是
$$N/H\simeq S_3$$
的自然三点置换作用：$C/H$ 作三循环，$N\setminus C$ 作反演。这一三点有限 étale $\mathbb Q$ 概形为 $\operatorname{Spec}(F)$，其中 $F=L^{\langle\text{一个换位}\rangle}$。

在 $\mathbb Q^{\Omega}$ 上取平均幂等元
$$e_H=|H|^{-1}\sum_{h\in H}h.$$
它的矩阵在 $\mathbb Q$ 中，且因 $H\triangleleft N$ 而与 Galois 的置换作用交换。因此它定义 $\mathcal R$、$\mathcal T$ 上的 $\mathbb Q$-有理**准同态**；乘以 $|H|$ 后是实际同态。个别 $h$ 不必定义一个 $\mathbb Q$ 同态，平均后的 Galois 不变性才是下降的理由。

几何上，$e_H\mathcal R$ 的三个坐标是三个轨道上的常值。将一个轨道坐标重复到该轨道的每条线，给
$$e_H\mathcal R\sim_{\mathbb Q}\operatorname{Res}_{F/\mathbb Q}J_0.$$
每个轨道大小是 $(p+1)/3$，所以原求和映射在三个轨道坐标上为该整数乘以三坐标之和。其连通核因而给
$$
e_H\mathcal T\sim_{\mathbb Q}
\ker\!\left(\operatorname{Tr}:\operatorname{Res}_{F/\mathbb Q}J_0\to J_0\right).
\tag{69.12}
$$

再在每个 $J_0$ 坐标上应用新形式轨道 $g$ 的有理 Hecke 幂等元 $e_g$。它定义于 $\mathbb Q$，与所有坐标置换、求和及 $e_H$ 交换，故
$$e_ge_H\mathcal T\sim_{\mathbb Q}B_g.$$
将 $e_ge_H$ 的分母清除后与满射 $P_0\Theta$ 合成，即得 $J$ 到该 $2d_g$ 维像阿贝尔簇的满射。若要以 (69.1) 的具体 $B_g$ 为目标，再合成一个同源即可。

这证明定理 69.1 的几何部分。只需水平 $p$ 的 Hecke 因子存在，完全没有使用 $L$ 值或秩的假设。它也不把这个商与 $X_{\rm ns}^+(p)$ 的 Heegner 商 $A$ 混同：这里的源是对应实际 $E[p]$ 的完整同余曲线。

## 5. 单个非零值传给整个新形式轨道

Bertolini–Darmon 的秩零定理以
$$L(A_g/K,\eta,1)=\prod_{\sigma:K_g\hookrightarrow\mathbb C}L(g^\sigma/K,\eta,1)\ne0$$
为输入，而 R66 的平均公式起初只给一个 $g$ 的非零值。需要明确补上这一步。

**引理 69.4。** 在本题条件下，若一个 $g$ 满足 (69.2)，则每个 $g^\sigma$ 都满足同一非消失。

**证明。** 采用 Bertolini–Darmon (1997), §1 Theorem 1.1 的 Gross 型公式。这里平方自由水平为 $p$，$p$ 惰于 $K$，环类字符 $\eta$ 原始且导子素于 $p$，正是该公式的设置。

可在判别式为 $p$ 的定四元数代数的理想类模上取 $g$ 的 Hecke 本征向量 $v_g$，其坐标在完全实系数域 $K_g$ 中。取导子 $c_\eta$ 的 Gross 点 $x_a$，由环类群的元素 $a$ 编号。相应代数周期为
$$P_\eta(g)=\sum_a\eta(a)^{-1}v_g(x_a)\in K_g(\zeta_3).$$
Gross 公式将 $L(g/K,\eta,1)$ 与这个周期的正定平方范数联系，全部比例因子非零。因此
$$L(g/K,\eta,1)\ne0\quad\Longleftrightarrow\quad P_\eta(g)\ne0.$$
不同的非零本征向量正规化不影响是否为零。

将 $\sigma:K_g\hookrightarrow\mathbb C$ 延拓到 $K_g(\zeta_3)$。由于 $\eta$ 阶三，$\eta^\sigma$ 是 $\eta$ 或 $\eta^{-1}$，而
$$\sigma(P_\eta(g))=P_{\eta^\sigma}(g^\sigma).$$
非零代数数在嵌入下仍非零。系数域完全实且 $x_a$ 相同，所以 $P_{\eta^{-1}}(g^\sigma)$ 是 $P_\eta(g^\sigma)$ 的复共轭；两者同时为零或同时非零。再用相同 Gross 公式，得到每个 $g^\sigma$ 的非消失。证毕。

本引理只使用零/非零的 Galois 相容性，不把未经固定的复周期本身当成 Galois 不变实数。酉中心 $1/2$ 与本节算术中心 $1$ 的换元按 R66 (7.1)。

## 6. 已发表秩零定理与 Weil 限制核

令 $H_{c_\eta}/K$ 为导子 $c_\eta$ 的环类域。R66 已证明 $L\subset H_{c_\eta}$。Bertolini–Darmon，*Annals of Mathematics* **146** (1997), 111–147，Theorem B，断言：对于平方自由水平、奇数个水平素数惰于 $K$、导子与水平互素的原始环类字符，若 $L(A_g/K,\eta,1)\ne0$，则
$$A_g(H_{c_\eta})^\eta\text{ 有限}.\tag{69.13}$$
逐项核对如下：本题水平是单个惰性素数 $p$；$p\nmid D c_\eta$；$\eta$ 原始；引理 69.4 保证整个 $A_g$ 的乘积 $L$ 值非零。所以 (69.13) 适用。共轭字符 $\eta^{-1}$ 也同样适用。

限制到 $L$ 并张量 $\overline{\mathbb Q}$，便得 $A_g(L)$ 的两个非平凡 $C_3=\operatorname{Gal}(L/K)$ 特征空间均为零。有限群作用在特征零中半单，因此
$$A_g(L)\otimes\mathbb Q=A_g(K)\otimes\mathbb Q.\tag{69.14}$$
这不声称 $A_g(K)$ 有限；它只消去了新增的两个三次特征空间。

在 (69.14) 中取定义 $F$ 的换位不变量。该换位在 $K$ 上是非平凡自同构，故
$$A_g(F)\otimes\mathbb Q=A_g(\mathbb Q)\otimes\mathbb Q.$$
而 $F/\mathbb Q$ 的迹映射在右边是乘三。于是其核张量 $\mathbb Q$ 为零；Mordell–Weil 有限生成性说明 (69.1) 的 $B_g(\mathbb Q)$ 有限。这证明 (69.3) 及定理 69.1。

最后，由 R66 的已发表 Feigon–Whitehouse 平均公式，$p>M$ 保证某个 $g$ 满足 (69.2)。它对应的 $d_g\ge1$，故实际有限群商正维，推论 69.2 得证。

## 7. 可用的几何尺度和尚未完成的尖点步骤

本构造还有一个明确优点：忘线映射的 Gram 标量
$$c_p=(p^2-1)/2$$
已完全算出，而不是仅知道某个未知次数的同源。对 $\ell\equiv\pm1\pmod p$ 的素数 $\ell$，$p>37$ 蕴含 $\ell>p+1$：小于 $p+1$ 的正候选只有 $p-1$，它不是素数；$p+1$ 也不是素数。因此 $\ell$ 不整除 $p(p^2-1)$。在这种剩余特征，忘线部分和有限置换平均的上述整数标量都为单位。

不过，这不自动给实际 $g$ 商在尖点上的非零微分。还需控制该商的整模型、Hecke 因子投影与尖点展开，尤其要证明相应的三个三次 Fourier 和不会在同一个 $\ell$ 上方素理想同时消失。有限群表示在这种特征半单，也不能单独排除某个具体矩阵系数为零。

所以本文没有直接推出 $j(E)$ 整性。它将此前小惯性接口中的“需要一个实际秩零商”改成已完成：在 $p>M$ 时已有明确的实际商和已发表的有限性证明。剩余问题是 $M$ 的全局控制，以及真实尖点/exceptional 条件的全层排除。完整惯性分支也仍未被本论证处理。

## 8. 来源、证明范围与已有接口的关系

- [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际小惯性 $C^3$、三次环类字符及 $M=Dc_\eta^2$；Feigon–Whitehouse 已发表公式的 $p>M$ 非消失。
- M. Bertolini and H. Darmon, **A rigid analytic Gross–Zagier formula and arithmetic applications**, with an appendix by B. Edixhoven, *Annals of Mathematics* **146** (1997), 111–147，DOI [10.2307/2951833](https://doi.org/10.2307/2951833)，[期刊页](https://annals.math.princeton.edu/articles/12969)，[作者保存的发表版](https://www.math.mcgill.ca/darmon/pub/Articles/Research/16.Rigid-analytic%20/pub16.pdf)。引言 Theorem B（p.113）、§1 Theorem 1.1、§7 给本文使用的已发表输入；[作者排印稿](https://www.math.mcgill.ca/darmon/pub/Articles/Research/16.Rigid-analytic%20/paper.pdf) 可检索公式。
- 全部忘线推拉、Galois 下降、三轨道投影、实际满射和迹零核论证均已在 §§2–4、§6 给出。只使用完整水平模曲线的标准忘子群模解释、Jacobians 的推拉与有限群商。
- Studnia，arXiv:2507.20801v2 的 Theorem B 有相同用途的有限商结论，但本篇未把该 submitted 论文作为证明输入；本篇也未重证其 Theorem D。其 exceptional 定义仍按独立[接口笔记](../notes/2026-11-12-studnia-small-inertia-and-cubic-character-resume2.md) 保存。

本结果只完成上述子问题，不将秩零、有限性或一个实际商的存在登记为 Serre 一致性的完成。
