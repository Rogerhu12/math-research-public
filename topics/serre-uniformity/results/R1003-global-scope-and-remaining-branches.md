# R1003：恢复主目标的全局量词与真实未覆盖分支

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。

**状态：已证明的依赖范围纠错。** 本文核对现有各命题实际写出的假设，证明当前引用的依赖链不能把 Serre 一致性主目标缩成指定 CM 源的 O1/O2。它不撤销带原假设的既有结论，也不声称剩余分支存在实际反例。root 已回到 R1/R66/R251/R258/R289/R294/R317 正文核对关键输入；本文是逻辑范围的恢复，不是对全部历史证明的正确性认证。

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
| [R1](R1-exact-remaining-image.md) §1 | 无 CM，$p>37$，非满像 | 像恰为完整 $N_{\rm ns}(p)$ | 不限制 $p\bmod9$；不限制 $j$、$K$ |
| [R5](R5-quadratic-self-twist-and-inertness.md) §§1–4 | 完整正规化子像 | $K$ 虚二次、$p$ 惰性，$E[p]\cong E^{\varepsilon}[p]$，惰性好素数的迹被 $p$ 整除 | $K$ 可变；残余自扭曲不等于特征零同源 |
| [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md) §1 式(1.1)、§2 | **另假设** $\bar\rho(I_p)\subsetneq C$ | $\bar\rho(I_p)=C^3$，$p\equiv2,5\pmod9$ | 完整惯性 $\bar\rho(I_p)=C$ 没有被排除 |
| [R294](R294-cartan-scalars-hasse-vanishing-and-exact-inertia.md) 定理294.1(2)–(3)、§1 | 仅完整正规化子像 | 惯性指数属于 $\{1,3\}$；指数3时给精确 $p\bmod9$ 与 $v_p(j)$ 表 | 该定理特意保留指数1；它不是“所有异常都指数3” |
| [R251](R251-joint-euler-detector-and-uniform-integral-j-conductor-growth.md) §1，(251.2)、定理251.1 | 小惯性，**另假设** $j\in\mathbb Z$；研究 $K\ne H=\mathbb Q(\zeta_3)$ | $|D_K|c\gg_\delta p^{5/3-\delta}$ | 此为下界，未排 $K\ne H$；非整 $j$ 也没有因此被排除 |
| [R258](R258-sextic-cm-normal-form-and-exact-integral-j-level.md) §1，(258.2)–(258.3)、定理258.1 | 小惯性，**另假设** $K=H$ 及 $\sigma=(\lambda/\psi)^6=1$ | 同时二次扭曲后 $E_0[p]\cong A_d[p]$，$A_d:y^2=x^3+d$，$d>0$立方自由；$v_p(d)=1$或2 | $\sigma=1$ 是输入；未排 $\sigma\ne1$；整 $j$ 仍是定理第5项的额外前提 |
| [R261](R261-three-division-cm-field-dichotomy-and-mod-nine-traces.md) (261.1)、§1 | R258设置，$j\in\mathbb Z$ | $\mathcal L_3(E_0)=\mathcal L_3(A_d)$ **或** $c\gg_\delta p^{1/3-\delta}$ | 第二支没有消失；$\mathcal L_3$ 只是实际模3的 $S_3$ 商域，不是完整3除法域 |
| [R263](R263-two-division-parity-and-common-cubic-normal-form.md) 定理263.1(4)，(263.5)–(263.6) | 同上 | $c\gg_\delta p^{1/3-\delta}$ **或** 两个小除法域同时相等，后一支给两类三次正规形 | 不能把这个“或”变为全部曲线都有同域正规形 |
| [R275](R275-tetrahedral-euler-comparison-and-uniform-cm-conductor-growth.md) §1，(275.1)–(275.6) | R258 的整 $j$ 无 CM 分支 | 以异域分支下界覆盖目标较弱下界，再研究同域支 | “此后只需同域”只针对证明导子下界；不是对 Serre 主目标消去异域支 |
| [R287](R287-raynaud-tangent-inertia-and-exclusion-of-reverse-cubic-family.md) §1、引言三条推论 | 实际 $E_0[p]\cong A_d[p]$，整 $j$ | 相同最小判别式赋值；同域分支的反向三次族排除；导子下界强化 | 仍未把任意异常曲线压入同域分支 |
| [R289](R289-dyadic-supersingularity-and-actual-integral-cubic-normal-form.md) §1，(289.4)–(289.6) | 小惯性、$K=H$、$\sigma=1$、整 $j$；除§2外**另假设两个小除法域相等** | $a^3+db^3=1$ 的整数正规形、指定二次扭曲及奇偶条件 | 该正规形的适用前提全部保留 |
| [R315](R315-common-global-symplectic-type-and-inert-conductor-support.md) §1，(315.1)–(315.2) | R289 同域分支及给定实际全局模 $p$ 同构 | 给定同构的平方辛型与坏支撑条件 | 不证明任意全正规化子像都来自该同构 |
| [R317](R317-all-bad-place-symplectic-constraints-and-surviving-families.md) §1，(317.1)–(317.2) | R315 的同一实际分支 | 全坏处进一步必要条件、仍存活的局部比较族 | 完整像的比较族反而说明局部必要条件不充分；它们不是 Serre 反例 |

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
- [R326](R326-exact-global-congruence-modulus-and-all-p-power-levels.md) §§1、5、8 的全局同余整数判别始终限于 R317 参数族；其末节明确保留导子无界，不能变成全部曲线的统一界。
- [R726](R726-uniform-original-primitive-nonvanishing.md) §1 的量词是全部充分大的 $p\equiv2,5\pmod9$ 上**原指定 CM 因子**的非消失与秩结论；它自己说明不证明 Serre 一致性或实际高度排零。
- [R936](R936-explicit-polynomial-trace-of-the-whole-supersingular-pairing.md) §1 限定原 CM 源与原 Serre application 的 $p\bmod9$；它不含从任意完整正规化子像到该源的归约。
- [R948](R948-rational-quadratic-Abel-root-and-original-coordinate-separation.md) §1 说明真实有理点候选未必有零 Abel 像，可能保留非零 Mordell–Weil 像。
- R968–R1002 的当前 O1/O2 输入继续是原 full-six/theta/CM filtered source。未在所引依赖链中给出消去上述额外前提的新命题。最新主结果索引首段也仍写“一般完整正规化子及全p原高度仍开放”。

因此，准确结论是：**当前被引用的证明链不能把主问题缩成 O1/O2；恢复其条件范围是必要纠错。** 本条不对全部历史稿作“证明均正确”的整体认证，也不以搜索未见代替一个数学否定命题。


## 5. 对后继研究的精确要求

解决当前 O1/O2 的指定系数问题，必须另外给出从全部候选曲线到该 CM 源的覆盖论证，或分别排除第3节列出的其它分支；真正有理点还必须满足全局高度条件。不能从 `c ≫ p^a` 推出 `c` 有界，不能把“或有共同小除法域，或导子足够大”改写成全部曲线有共同小除法域。当前主目标仍未完成。

本文只使用仓库已列命题的原文假设和一阶逻辑，没有使用新预印本的未重建结果。2026文献核对和后续路线记录另见 [本轮全局笔记](../notes/2026-11-26-global-route-continuation.md)。
