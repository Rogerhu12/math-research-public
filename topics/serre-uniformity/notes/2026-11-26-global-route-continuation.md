# 2026-11-26：主目标覆盖范围与全局路线接续

会话：serre-resume-24b8836b-20261126 / global_route。
读取快照：`f0548477576caa2373d1626227a284ccfa9767d0`。
状态：§§1–5 是可直接登记的范围纠错；§6 以下为继续研究记录。本文不改写任何旧结论的证明，不把未覆盖的分支说成已有反例。

## 1. 必须恢复的全局量词

设 $p>37$，$E/\mathbb Q$ 无 CM，$\bar\rho_{E,p}$ 不满。R1 给出的完整归约仅为
$$
\operatorname{im}\bar\rho_{E,p}=N_{\mathrm{ns}}(p)
\quad\text{（适当共轭后）}.
$$
它**没有**给出 $p\equiv2,5\pmod9$、$j(E)\in\mathbb Z$、商域 $K=\mathbb Q(\sqrt{-3})$、与某条 $j=0$ 曲线模 $p$ 同构，或小除法域相等。

现 HANDOFF 的“R317 仅完整 Nns、p2/5mod9、a³+db³=1/p|b”及 open O1 紧邻“只余完整非分裂 Cartan 正规化子”的写法，把**全局像归约**和**当前所研究条件分支的范围**压在同一句内，易丢失以上独立前提。应明确分开：全主目标覆盖所有 $p>37$ 的完整正规化子像；当前 O1/O2 所需的 theta/CM 源属于指定辅助族，并未排除其它全局分支。

## 2. 已读原文的假设—结论链

| 原文位置 | 本步输入（在此前假设之外） | 确实得到的结论 | 不能删去的其余可能性 |
|---|---|---|---|
| [R1](../results/R1-exact-remaining-image.md) §1 | 无 CM，$p>37$，非满像 | 像恰为完整 $N_{\rm ns}(p)$ | 不限制 $p\bmod9$；不限制 $j$、$K$ |
| [R5](../results/R5-quadratic-self-twist-and-inertness.md) §§1–4 | 完整正规化子像 | $K$ 虚二次、$p$ 惰性，$E[p]\cong E^{\varepsilon}[p]$，惰性好素数的迹被 $p$ 整除 | $K$ 可变；残余自扭曲不等于特征零同源 |
| [R66](../results/R66-cubic-conductor-nonvanishing-and-tate-primes.md) §1 式(1.1)、§2 | **另假设** $\bar\rho(I_p)\subsetneq C$ | $\bar\rho(I_p)=C^3$，$p\equiv2,5\pmod9$ | 完整惯性 $\bar\rho(I_p)=C$ 没有被排除 |
| [R294](../results/R294-cartan-scalars-hasse-vanishing-and-exact-inertia.md) 定理294.1(2)–(3)、§1 | 仅完整正规化子像 | 惯性指数属于 $\{1,3\}$；指数3时给精确 $p\bmod9$ 与 $v_p(j)$ 表 | 该定理特意保留指数1；它不是“所有异常都指数3” |
| [R251](../results/R251-joint-euler-detector-and-uniform-integral-j-conductor-growth.md) §1，(251.2)、定理251.1 | 小惯性，**另假设** $j\in\mathbb Z$；研究 $K\ne H=\mathbb Q(\zeta_3)$ | $|D_K|c\gg_\delta p^{5/3-\delta}$ | 此为下界，未排 $K\ne H$；非整 $j$ 也没有因此被排除 |
| [R258](../results/R258-sextic-cm-normal-form-and-exact-integral-j-level.md) §1，(258.2)–(258.3)、定理258.1 | 小惯性，**另假设** $K=H$ 及 $\sigma=(\lambda/\psi)^6=1$ | 同时二次扭曲后 $E_0[p]\cong A_d[p]$，$A_d:y^2=x^3+d$，$d>0$立方自由；$v_p(d)=1$或2 | $\sigma=1$ 是输入；未排 $\sigma\ne1$；整 $j$ 仍是定理第5项的额外前提 |
| [R261](../results/R261-three-division-cm-field-dichotomy-and-mod-nine-traces.md) (261.1)、§1 | R258设置，$j\in\mathbb Z$ | $\mathcal L_3(E_0)=\mathcal L_3(A_d)$ **或** $c\gg_\delta p^{1/3-\delta}$ | 第二支没有消失；$\mathcal L_3$ 只是实际模3的 $S_3$ 商域，不是完整3除法域 |
| [R263](../results/R263-two-division-parity-and-common-cubic-normal-form.md) 定理263.1(4)，(263.5)–(263.6) | 同上 | $c\gg_\delta p^{1/3-\delta}$ **或** 两个小除法域同时相等，后一支给两类三次正规形 | 不能把这个“或”变为全部曲线都有同域正规形 |
| [R275](../results/R275-tetrahedral-euler-comparison-and-uniform-cm-conductor-growth.md) §1，(275.1)–(275.6) | R258 的整 $j$ 无 CM 分支 | 以异域分支下界覆盖目标较弱下界，再研究同域支 | “此后只需同域”只针对证明导子下界；不是对 Serre 主目标消去异域支 |
| [R287](../results/R287-raynaud-tangent-inertia-and-exclusion-of-reverse-cubic-family.md) §1、引言三条推论 | 实际 $E_0[p]\cong A_d[p]$，整 $j$ | 相同最小判别式赋值；同域分支的反向三次族排除；导子下界强化 | 仍未把任意异常曲线压入同域分支 |
| [R289](../results/R289-dyadic-supersingularity-and-actual-integral-cubic-normal-form.md) §1，(289.4)–(289.6) | 小惯性、$K=H$、$\sigma=1$、整 $j$；除§2外**另假设两个小除法域相等** | $a^3+db^3=1$ 的整数正规形、指定二次扭曲及奇偶条件 | 该正规形的适用前提全部保留 |
| [R315](../results/R315-common-global-symplectic-type-and-inert-conductor-support.md) §1，(315.1)–(315.2) | R289 同域分支及给定实际全局模 $p$ 同构 | 给定同构的平方辛型与坏支撑条件 | 不证明任意全正规化子像都来自该同构 |
| [R317](../results/R317-all-bad-place-symplectic-constraints-and-surviving-families.md) §1，(317.1)–(317.2) | R315 的同一实际分支 | 全坏处进一步必要条件、仍存活的局部比较族 | 完整像的比较族反而说明局部必要条件不充分；它们不是 Serre 反例 |

这里“另假设”均来自原结果正文，不是本轮新设限制。$\mathcal L_2$ 是完整二挠点域；$\mathcal L_3$ 是 $\operatorname{GL}_2(\mathbb F_3)/Q_8\simeq S_3$ 的商域，两者不得互换。

## 3. 形式化量词核查：导子下界不能作分支排除

给定一组候选 $(E,p,c)$，R261/R263 的逻辑形状是
$$
\mathcal H(E,p,c)\Longrightarrow
\bigl(\mathcal F(E,p,c)\lor c\ge A_\delta p^{1/3-\delta}\bigr),
$$
其中 $\mathcal F$ 是小除法域一致。若无独立的上界
$c<A_\delta p^{1/3-\delta}$，不能推出 $\mathcal F$。

完整证明只需指出：对任意大的 $p$，不等式 $c\ge A_\delta p^{1/3-\delta}$ 在正整数 $c$ 中仍可满足。因此该不等式与 $p\to\infty$ 并不矛盾，不能作为排除候选的逻辑步骤。这里的数值可满足性不是声称存在相应的实际椭圆曲线。

同理，$|D_K|c\gg p^{5/3-\delta}$ 不能推出 $K=H$，也不能推出 $p$ 有界。后继 R287 对同域支给更强下界，仍不改变这一方向。

所以即使完整解决当前指定 $j=0$ 同余分支，也只完成一个严格带条件的子任务；主目标仍须单独处理：

1. 完整惯性 $I_p=C$（允许所有尚未排除的素数同余类）；
2. 小惯性但 $j\notin\mathbb Z$；
3. 小惯性、整 $j$、$K\ne\mathbb Q(\sqrt{-3})$；
4. 小惯性、整 $j$、$K=\mathbb Q(\sqrt{-3})$、$\sigma\ne1$；
5. $\sigma=1$ 后真实小除法域不相同、导子随 $p$ 增长的支路；
6. 当前 $a^3+db^3=1$ 分支本身的真实全局高度/非零 Mordell–Weil 像问题。

前五项是待证明覆盖或待排除的类，不是已经证明非空的类。

## 4. 后继结果与旧 open 的交叉核对

已检索 `results/R*.md` 与全部逐级结果索引中 `小惯性`、`完整惯性`、`非整`、`sigma`、`σ`、`同域`、`归约`、`只余` 等直接相关记录；对命中的负担结论回到正文读取假设。

- `notes/2026-11-13-open-before-three-heights-and-secondary-obstructions.md` 的 O1 原文明确记有“变化商域/导子、一般p的exceptional及Fourier共同零、完整惯性仍开”。
- `notes/2026-11-13-open-before-first-canonical-disk.md` 同段明确记有“仍无上界，K−3 σ平凡及变化域未排”。这些是原有开放支路，而非本轮新开课题。
- R294 是在 R289 之后对一般商域的实质推广，但只推广局部 Hasse/判别式必要条件，完整定理仍列出惯性指数1和3，未排指数1或变化商域。
- [R326](../results/R326-exact-global-congruence-modulus-and-all-p-power-levels.md) §§1、5、8 的全局同余整数判别始终限于 R317 参数族；其末节明确保留导子无界，不能变成全部曲线的统一界。
- [R726](../results/R726-uniform-original-primitive-nonvanishing.md) §1 的量词是全部充分大的 $p\equiv2,5\pmod9$ 上**原指定 CM 因子**的非消失与秩结论；它自己说明不证明 Serre 一致性或实际高度排零。
- [R936](../results/R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md) §1 限定原 CM 源与原 Serre application 的 $p\bmod9$；它不含从任意完整正规化子像到该源的归约。
- [R948](../results/R948-rational-quadratic-Abel-root-and-original-coordinate-separation.md) §1 说明真实有理点候选未必有零 Abel 像，可能保留非零 Mordell–Weil 像。
- R968–R1002 的当前 O1/O2 输入继续是原 full-six/theta/CM filtered source。未在所引依赖链中给出消去上述额外前提的新命题。最新主结果索引首段也仍写“一般完整正规化子及全p原高度仍开放”。

因此，准确结论是：**当前被引用的证明链不能把主问题缩成 O1/O2；恢复其条件范围是必要纠错。** 本条不对全部历史稿作“证明均正确”的整体认证，也不以搜索未见代替一个数学否定命题。

## 5. 建议登记文字

可在 HANDOFF/open 开头使用：

> 全主目标只归约到 $p>37$ 的完整非分裂 Cartan 正规化子。O1/O2 当前研究的是指定 $j=0$ CM 辅助族。R317 的应用另外要求严格小惯性 $I_p=C^3$、整 $j$、$K=\mathbb Q(\sqrt{-3})$、$\sigma=1$ 及实际二除法域和三除法 $S_3$ 商域同时一致。$p\equiv2,5\pmod9$ 是小惯性结论，不是全主目标的已证限制。其余分支和真实全局高度仍须处理；导子下界不能将它们删去。

## 6. 重新核对的候选来源及正在尝试的接口

### 6.1 已登记的两个范围不同的来源，不作为本轮新输入

1. Matthew Bisatt, Lorenzo Furio, Davide Lombardo, *Explicit p-adic Hodge theory for elliptic curves and non-split Cartan images*, arXiv:2603.04021v2, 2026-06-08。**R35末节、R294参考文献3及 `notes/2026-11-12-literature-nonsplit.md` 已登记 v2，不是本轮新来源。** 原文定位：https://arxiv.org/html/2603.04021v2 ，v2 的相关编号为 Proposition 8.30 / Corollary 8.31。重新检索时正文服务只返回了旧 v1（其编号是 Corollary 8.29），直接请求 v2 返回 DisabledError，不能声称本轮重新逐字核准 v2 全文。旧版 Theorem 1.3 的深度是 $e\in\{3,6\}$ 时 $n_0=\lfloor v_p(j)/3\rfloor$、$e=4$ 时 $n_0=\lfloor v_p(j-1728)/2\rfloor$，另有 $p>\sqrt{n_0+1}$ 的适用限制；任何后继实际引用应回到 v2 核准，而非沿用旧版编号。该论文只作为候选输入，R35/R294 已注明不直接用其未公认部分。
2. Tyler Genao, Jacob Mayle, Jeremy Rouse, *A uniform bound on the smallest surjective prime of an elliptic curve*, The Ramanujan Journal **70**, article 22 (2026), published 2026-05-12, DOI 10.1007/s11139-026-01376-8，Theorem 2。原文：https://link.springer.com/article/10.1007/s11139-026-01376-8 。该定理是最小满射素数至多7，且除六个 $j$ 外至多5；不限制最大异常素数。仓库 R52 已消费其前身结果及完整检测域，不重登记成新数学。

BFL 的最新出版/公认状态与本仓库是否已独立重证其所需部分须继续核实；未完成该步前，不将它的新增定理作为本仓库无条件已证结论。可以用它定位真实局部—全局接口。

### 6.2 R317 深度接口的直接代数计算

R317 的
$$
H_a:y^2=x^3+3arx-r(2a^3-1),\qquad r=1-a^3
$$
满足
$$
4(3ar)^3+27[-r(2a^3-1)]^2
=27r^2\bigl(4a^3(1-a^3)+(2a^3-1)^2\bigr)=27r^2.
$$
故
$$
\Delta(H_a)=-432r^2,\qquad j(H_a)=6912a^3r.
$$
在实际 $p\mid r$、$p>37$ 时 $p\nmid a$。写 $v_p(r)=m+3k$，$m\in\{1,2\}$，于是
$$
v_p(j(H_a))=m+3k,
\qquad\left\lfloor v_p(j(H_a))/3\right\rfloor=k.
$$
因此 BFL 的局部深度（如其定理可用）在此确是旧参数 $k=v_p(b)$，并非一个与 $E$ 无关的新常数。即使知道全局像的首离 Cartan 层数至多这个局部层数，也只得到依 $k$ 的界；R317 已有局部比较族允许 $k$ 任意大。下一步必须真正限制实际全局同构的层数/高度，不能以新局部分类型号改称完成。

## 7. 新的精确延伸：CM 交叉素数的迹差赋值必为偶数

本节是在 R320 的原固定 CM 迹上得到的完整证明，不使用 BFL。它把 R320 的一次 $p\to p^2$ 提升解释为一个**准确的赋值奇偶性**，给出任意高同余层的正确幅度；不会把该局部提升冒充全局层数提升。

### 7.1 命题

固定 $p>37$ 且 $p\equiv5\pmod {12}$。取 R320 的实际整数 $a$、原符号 $\varepsilon$ 和好素数
$$
q\mid 2a^3-1,\qquad q\equiv1\pmod {12},\qquad q\ne p.
$$
令原 CM 曲线
$$
G:y^2=x^3+3x,\qquad J_\varepsilon:y^2=x^3-2\varepsilon
$$
在 $q$ 的实际整数迹分别为 $g_q,j_{\varepsilon,q}$，并令
$$
D_\varepsilon(q)=\frac{g_q-j_{\varepsilon,q}}4\in\mathbb Z\setminus\{0\}.
$$
则有
$$
\boxed{v_p(D_\varepsilon(q))\in2\mathbb Z_{\ge0}.}
\tag{G7.1}
$$
若这同一对实际全局曲线满足 $H_a[p^n]\simeq B_a[p^n]$，则
$$
\boxed{p^{,2\lceil n/2\rceil}\mid D_\varepsilon(q),}
\tag{G7.2}
$$
且有明确的大小限制
$$
\boxed{q\ge p^{,4\lceil n/2\rceil}
            +8p^{,2\lceil n/2\rceil}+4.}
\tag{G7.3}
$$
当 $n=1,2$ 时 (G7.3) 都只是 R320 的 $p^4+8p^2+4$；不能把 $n=2$ 误提高为 $p^8$。当 $n=3,4$ 时才得到 $p^8+8p^4+4$。

### 7.2 完整证明

R320 引理320.2–320.3 在同一 Frobenius 取向上给出整数
$$
q=x^2+y^2=u^2+3v^2,
\qquad g_q=2x,\quad j_{\varepsilon,q}=2u,
\tag{G7.4}
$$
其中 $x,u$ 为奇数，$y,v$ 为非零偶数，且 $x-u\ne0$。这些性质只用两个原 CM 曲线在 $q$ 的具体约化及 $2$ 为模 $q$ 立方；不预先使用模 $p$ 同构。

由于 $(3/p)=-1$，对任意不全为零的整数 $y,v$，二次型 $3v^2-y^2$ 满足
$$
v_p(3v^2-y^2)=2\min\{v_p(y),v_p(v)\}.
\tag{G7.5}
$$
确实，提出 $p^{2t}$，其中 $t$ 为右端最小值除以2，剩下至少一个坐标模 $p$ 非零。如果剩余二次型为零，则非零解给 $3$ 为平方，矛盾。故没有进一步的 $p$ 进消去。

由两个范数相等，
$$
(x-u)(x+u)=3v^2-y^2.
\tag{G7.6}
$$
若 $p\nmid x-u$，(G7.1) 直接成立。若 $p\mid x-u$，则由 (G7.5) 必有 $p\mid y,v$：这是把 (G7.6) 降模 $p$ 后的各向异性。又因 $q=x^2+y^2$ 且 $q\ne p$ 为素数，$p\nmid x$。所以 $u\equiv x\pmod p$ 给 $p\nmid x+u$。因此
$$
v_p(x-u)=2t,\qquad
t=\min\{v_p(y),v_p(v)\}\ge1.
\tag{G7.7}
$$
因 $D_\varepsilon(q)=(x-u)/2$ 且 $p$ 为奇数，得到 (G7.1)。

若给定全局 $p^n$ 同构，限制到 $q$ 的未分歧分解群，仍是 R320 引理320.1 的**同两个整数迹**，故 $p^n\mid g_q-j_{\varepsilon,q}$。结合 (G7.7)，得 $2t\ge n$，即 (G7.2)。

为证明精确大小界，写
$$
y=2p^t s,\qquad v=2p^t w,\qquad
x-u=2p^{2t}h,\qquad z=(x+u)/2,
\tag{G7.8}
$$
其中 $s,w,h$ 非零整数，$p\nmid h$，且 $z\ne0$。
若 $z=0$，则 (G7.6) 迫 $s^2=3w^2$，与 $s,w\ne0$ 矛盾。
代回 (G7.4)–(G7.6)，得到
$$
hz=3w^2-s^2,
\qquad q=z^2+p^{4t}h^2+2p^{2t}s^2+6p^{2t}w^2.
\tag{G7.9}
$$
因 $x=z+p^{2t}h$ 为奇数，$z,h$ 奇偶相反。
若 $|h|=1$，$z$ 为非零偶数，因此 $z^2\ge4$；若 $|h|\ge2$，则 $p^{4t}h^2\ge4p^{4t}$、$z^2\ge1$。两种情形均给
$$
q\ge p^{4t}+8p^{2t}+4.
$$
由 $t\ge\lceil n/2\rceil$ 得 (G7.3)。证毕。

### 7.3 对实际有限检测的含义及边界

R320 的 $G_1(a)$ 若不是空集合 gcd，则
$$
v_p(G_1(a))\in2\mathbb Z_{\ge0},
$$
因为它是非空有限组偶数赋值的最小值。故仅使用这些 $q\equiv1\pmod {12}$、$q\mid2a^3-1$ 的固定 CM 交叉素数，无法区分全局同余指数 $2t-1$ 与 $2t$。

R326 的真正全局同余整数 $\mathcal C$ 使用全部好素数；它的赋值不因本节而必须为偶数。尤其从 $p\mid\mathcal C$ 不能推出 $p^2\mid\mathcal C$，因为定义 $\mathcal C$ 的其它迹差没有 (G7.4) 的双 CM 范数结构。

因此本节给出了新的精确全局必要约束及检测器的奇偶盲点，并没有得到 $a,d,c$ 的统一上界，也没有关闭任一完整惯性/变化商域支路。

