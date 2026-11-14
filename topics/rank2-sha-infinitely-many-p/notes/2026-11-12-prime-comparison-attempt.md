# 2026-11-12：把固定二次下降变成变化素数结论的尝试

**状态：逐素数比较与类群公式已证明；无穷素数命题未证明。** 固定曲线始终是
$$
E=E_{17}:y^2=x^3-17x,\qquad K=\mathbb Q(i).
$$
R4 给出严格的秩恰为 $2$ 证书。这里记录实际试过的算术映射、得到的统一输入以及尚缺的命题；完整可引用证明放在 R7。

## 1. 二次同源与 CM 分解实际保留了什么

对 R4 的二次同源 $\phi:E\to E'$、对偶 $\psi$，恒有 $\psi\phi=[2]$。所以任意奇 $p$ 上，$\phi$ 在 $p$-幂系数、全局/局部 Kummer 商、Selmer 群和 $\Sha[p^\infty]$ 上都是同构，逆是 $\psi/2$。核与余核均为零。在 $K$ 上，这只是 CM 素理想 $(1+i)$ 在其他所有素理想局部化后成为单位的事实。

这给出真实的传递，但传递只发生在**同一素数**的两条同源曲线之间。任何 $2$-初等挠群到奇 $p$-初等挠群的群同态都为零，因此不能把这个同构误读成从 $2$-Selmer 到 $p$-Selmer 的比较。

二次基变换也可完全写出：若 $A=\Sha(E/\mathbb Q)[p^\infty]$、$S=\Sha(E/K)[p^\infty]$，则
$$
S\simeq A\oplus A,
\qquad (a,b)\longmapsto\operatorname{res}(a)+[i]\operatorname{res}(b).
$$
若 $p=\pi\bar\pi$ 分裂，则目标的一个 CM 分量反而恰好等于原问题：
$$
e_\pi\operatorname{res}:A\xrightarrow{\sim}\Sha(E/K)[\pi^\infty],
\qquad\text{逆为 }\operatorname{cor}.
$$
有限层同样给出 $\operatorname{Sel}_p(E/\mathbb Q)\simeq\operatorname{Sel}_\pi(E/K)$。系数从二维降到一维，并没有把 Mordell–Weil 的必要维数 $2$ 降到 $1$；$E(K)$ 的 $\mathbb Z[i]$-秩仍为 $2$。

## 2. 得到的一项真正统一的局部输入

曲线有有理二挠点 $(0,0)$。对每个好素数 $p\ge7$，$\#E(\mathbb F_p)$ 为偶数；Hasse 区间又包含在 $(0,2p)$。若 $p\mid\#E(\mathbb F_p)$，这个阶只能等于奇数 $p$，矛盾。因此本曲线在所有好素数 $p\ge7$ 都非 anomalous。

对分裂 $p\ge13$、$p\ne17$，这给出两处 $p$-局部无 $p$ 挠点；局部 Euler 特征与形式群计算进一步给出
$$
\dim H^1(K_{\mathfrak p},E[\pi])
=\dim H^1(K_{\bar{\mathfrak p}},E[\pi])=1,
$$
而 $\pi$-Selmer 条件在 $\mathfrak p$ 处为全空间，在 $\bar{\mathfrak p}$ 处为零。

这里消除了一个随 $p$ 变化的异常素数障碍，且是对全部指定素数的证明。它没有控制全局类群部分；不能把“局部条件统一”替换成“全局 Selmer 维数统一”。

## 3. 固定四次去扭转为何没有继承秩零结论

令 $\delta^4=17$、$F_0=K(\delta)$。在 $F_0$ 上
$$
\theta:E_{17}\xrightarrow{\sim}E_1,
\qquad(x,y)\longmapsto(x/\delta^2,y/\delta^3),
\qquad E_1:y^2=x^3-x.
$$
若 $\sigma(\delta)=i\delta$，则 $^\sigma\theta=[i]\theta$。因此 $E_{17}$ 的点与上同调类被送入满足 $\sigma s=[i]s$ 的分块。基本曲线 $E_1/K$ 的限制像却满足 $\sigma s=s$。因为 $4$ 与奇 $p$ 互素，两者是完全分开的整 $p$-进特征分块。

R7 写出了四个投影
$$
e_k=\frac14\sum_{j=0}^3[i]^{-kj}\sigma^j,
$$
并证明 $e_k\Sha(E_1/F_0)[p^\infty]\simeq\Sha(E_{17^k}/K)[p^\infty]$。范数在平凡块上是乘 $4$，在其余三块上为零。目标是 $k=1$ 块；基本曲线在基域的有限性只控制 $k=0$ 块。

因此失败点非常具体：扩张次数控制的是限制到**不变子群**的核和余核，不能控制整个扩域群中新增的非平凡特征块。去扭转后 $E_1(F_0)$ 的目标块仍包含 $\mathbb Z[i]$-秩 $2$；Weil 限制的分解也仍含有 $E_{17}$ 的高秩因子。

## 4. 同一障碍在变化除法域中的精确形式

这一节进一步检查“去扭转只用了固定次数 $4$，所以可否转而比较基本曲线的类群”。仍取分裂的好素数 $p\ge13$、$p\ne17$，固定位于 $p$ 上的 $\pi$，并令
$$
L_{1,p}=K(E_1[\pi]),\qquad N_p=F_0L_{1,p}.
$$
记基本曲线的除法特征为 $\chi_{1,p}:G_K\to\mathbb F_p^\times$，四次 Kummer 特征为
$$
\eta(g)=g(\delta)/\delta\in\mu_4\subset\mathbb F_p^\times.
$$
这里 $\mu_4$ 到 $\mathbb F_p$ 的嵌入由所选 $\pi$ 固定。上面的去扭转公式直接给出
$$
\chi_{17,p}=\chi_{1,p}\eta^{-1}.\tag{4.1}
$$

基本曲线在 $\pi$ 处的形式群为高 $1$ 的 CM 形式群。$[\pi](T)/T$ 的 Weierstrass 多项式次数为 $p-1$、为 Eisenstein 多项式：线性项系数 $\pi$ 的赋值为 $1$，模 $\pi$ 的第一个非零项来自次数 $p$。故非零 $\pi$-挠点生成的局部扩张全分歧且次数为 $p-1$。全局除法特征的像又包含在 $\mathbb F_p^\times$，所以
$$
[L_{1,p}:K]=p-1,\qquad\operatorname{Gal}(L_{1,p}/K)\simeq\mathbb F_p^\times.
$$
此除法域在 $2,\pi$ 以外无分歧：在其他不同于 $p$ 的好素点用好约化的挠点无分歧性，在 $\bar\pi$ 处用对应的 étale $\pi$-挠群。

另一方面 $F_0/K$ 在位于 $17$ 上的点由 $X^4-17$ 的 Eisenstein 性全分歧，且任一非平凡中间扩张仍在这些点分歧。因此
$$
F_0\cap L_{1,p}=K,\qquad
\operatorname{Gal}(N_p/K)\simeq\mu_4\times\mathbb F_p^\times.
$$
在这个积群中，(4.1) 是 $(a,b)\mapsto ba^{-1}$。于是
$$
L_{17,p}:=K(E_{17}[\pi])
=N_p^{\{(a,a):a\in\mu_4\}},\qquad [L_{17,p}:K]=p-1.
$$
共同子域
$$
B_p=L_{1,p}\cap L_{17,p}
$$
恰对应 $\ker(\chi_{1,p}^4)=\ker(\chi_{17,p}^4)$；故
$$
[B_p:K]=(p-1)/4,
\qquad[L_{1,p}:B_p]=[L_{17,p}:B_p]=4,
\qquad[N_p:B_p]=16.
$$
这确实把“变化四次扭转”变成同一个 $B_p$ 上的两条四次扩张，但 **$B_p$ 仍随 $p$ 变化，次数随 $p$ 增长**。

对于次数与 $p$ 互素的 Galois 扩张 $N/L$，理想扩张与范数满足 $N\circ\operatorname{ext}=[N:L]$、$\operatorname{ext}\circ N=\sum_g g$，所以在 $p$-类群上
$$
\operatorname{Cl}(L)[p^\infty]
\simeq\operatorname{Cl}(N)[p^\infty]^{\operatorname{Gal}(N/L)}.
$$
这不要求扩张无分歧。对 $N_p/L_{1,p}$ 的四次群而言，基本曲线的特征是平凡的，而 $\chi_{17,p}$ 的限制为 $\eta^{-1}$，非平凡。其范数在目标特征块上为零。因此“$E_1$ 的相关类群块已知很小”仍然不能沿固定次数 $4$ 的范数映射控制目标块。障碍与上一节的 $\Sha$ 比较完全一致，已经定位到具体的角色，而非只说两条曲线不同。

## 5. 从实际单位–类群列得到的明确缺口

R7 采用包含全部 $p$-挠点的域
$$
M_p=K(E_{17}[p]),\qquad\Delta_p=\operatorname{Gal}(M_p/K),
$$
而非上一节单个 $\pi$ 的除法域。若 $\chi_{\bar\pi}$ 是 $\Delta_p$ 在 $E[\bar\pi]$ 上的特征，令
$$
c_p=\dim_{\mathbb F_p}\operatorname{Cl}(M_p)[p]^{\chi_{\bar\pi}}.
$$
R7 的证明将全局 Kummer 类写成 $S$-单位和 $S$-类群，其中 $S$ 为位于 $2,17,p$ 上的素点。逐一检查这些点的分解群上目标字符非平凡后，得到：

- 单位的目标分量恰为一维；这来自 Dirichlet 单位表示，不使用 Leopoldt 猜想。
- $S$-类群与完整类群的目标 $p$-初等分量相同。
- 只剩 $\bar\pi$ 处的一维局部化条件，其秩记为 $\varepsilon_p\in\{0,1\}$。

因此
$$
s_p:=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
=1+c_p-\varepsilon_p.
$$
用已经证明的 $w(E)=+1$、Dokchitser–Dokchitser 的 $p$-奇偶定理，以及 Cassels–Tate 配对在商去最大可除子群后的交错性，进一步得到
$$
s_p=2\left\lceil\frac{c_p}{2}\right\rceil,
\qquad
\Sha(E/\mathbb Q)[p^\infty]=0
\Longleftrightarrow c_p\in\{1,2\}.\tag{5.1}
$$
整个奇偶步骤没有先假设 $\Sha$ 有限。若其可除部分余秩为 $t_p$，$p$-奇偶定理给出 $t_p$ 偶；有限商的 $p$-挠维数再由交错配对给出偶性。

故当前真正未闭合的充分命题是：

> 对无穷多个分裂素数 $p\ge13$、$p\ne17$，上述具体类群特征分量的维数 $c_p$ 至多为 $2$。

R4 强迫 $c_p\ge1$，所以试图把它一概证明为零已经不可能。单个小素数的类群计算、有限多个 $p$ 的计算，以及无条件局部非 anomalous 性，都未证明所需的无穷性。式 (5.1) 给出的是主目标的一条充分路线；允许非零有限 $\Sha[p^\infty]$ 的主目标比它弱。

## 6. 与近年相对类群结果的关系

De–Majumdar–Mondal 的 *Relative p-class groups and p-Selmer groups*（[arXiv:2412.13022，2024-12-17 版本](https://arxiv.org/abs/2412.13022)；[2026 年正式版 DOI](https://doi.org/10.1016/j.jpaa.2026.108222)）在该预印本 Theorem 2.4 中，用单个 CM 除法域的相对四次类群目标维数 $r_\pi(E_D)$ 给出
$$
r_\pi(E_D)\le s_p(E_D/\mathbb Q)\le r_\pi(E_D)+1,
$$
再由根数确定奇偶。其共同基域对扭转参数 $D$ 不变，但仍依赖 $p$。这与上一节的精确同态分析相符。

这篇论文提供了有效的逐素数描述，不提供固定秩 $2$ 曲线在无穷多个变化 $p$ 上的上界。它的预印本与正式版定理编号不同，引用时应标明版本。此处最初保留了单个除法域维数 $r_\pi$ 与全 $p$-除法域维数 $c_p$ 的比较缺口。随后 R12 已用理想范数、复共轭及相对群投影完整证明 $c_p=r_\pi(E)$，没有额外核、余核或局部修正项；仍未得到无穷多个 $p$ 的小维数上界。

## 7. 仍可合法利用的量词变体

若以后能找到一个**预先固定的有限集合** $E_1,\ldots,E_m$，每条均有严格秩至少 $2$ 证书，并证明每个充分大的 $p$ 至少有其中一条满足 $\Sha(E_j/\mathbb Q)[p^\infty]$ 有限，则抽屉原理会给出一条固定曲线适用于无穷多个 $p$。这与允许 $E$ 随 $p$ 在无限族中任意变化不同。

本次没有找到满足这个统一覆盖条件的定理。固定四次去扭转的四个特征块也没有给出这种覆盖：已知秩零块的控制不对另外三块施加所需上界。此处只保留一个逻辑上正确的可继续尝试方向，不将它列为已证明结果。

## 交接

可直接引用的完整结果为 R2、R4、R7；根数和周期输入位于 `2026-11-12-cm-local-inputs.md`。R7 已给出所有同源、限制/余限制、CM 分量与局部条件的实际映射。当前工作没有完成题目要求的无穷素数断言，也没有从有限数据推断无限结论。
