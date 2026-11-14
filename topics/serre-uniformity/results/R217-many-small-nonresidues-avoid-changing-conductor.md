# R217 重建：多个小非剩余允许避开变化导子

日期：2026-11-13。

**状态：已证明。** 本文使用 Pollack 已发表于 *Proceedings of the AMS* 的定理，从多个小惰性素数中避开随 $p$ 变化的坏集，再结合 R215 已完成的正 Hecke 卷积及平方代价，得到实际阶四类型的非 CM 中心非消失范围。主指数为 $1/(2-1/\sqrt e)=0.71763329\ldots$；删除实际类数所用的 Siegel 常数一般无效。

## 1. 输入定理及准确量词

置

$$\alpha=\frac1{4\sqrt e}=0.15163266\ldots.$$

Pollack (2017), Theorem 1.1 给出：每个 $\epsilon>0$ 都有 $m_0(\epsilon)$、$\kappa(\epsilon)>0$，使每个 $m>m_0(\epsilon)$ 及每个模 $m$ 非主 Dirichlet 字符 $\chi$ 满足

$$\#\{q\text{ 素数}:q\le m^{\alpha+\epsilon},\ \chi(q)\notin\{0,1\}\}>m^{\kappa(\epsilon)}. \tag{217.1}$$

对二次字符，条件即 $\chi(q)=-1$。这是多个**素数**的结论，不仅是存在一个小非剩余整数，也不是只有最小素数非剩余的上界。

## 2. 避开任意多项式大小的坏素数积

**定理 217.1。** 给定 $A>0$、$\epsilon>0$ 和整数 $s\ge1$，存在 $P_0(A,\epsilon,s)$，使每个 $p>P_0$、$p\equiv3\pmod4$，以及每个满足

$$1\le B\le p^A$$

的整数 $B$，都至少有 $s$ 个不同素数 $q$ 同时满足

$$\boxed{q\le p^{\alpha+\epsilon},\qquad q\nmid B,\qquad
\left(\frac{-p}{q}\right)=-1.} \tag{217.2}$$

Kronecker 符号用于 $q=2$；若需要奇素数，只需令 $2\mid B$。全部这些 $q$ 自动不同于 $p$。

**证明。** 因为 $p\equiv3\pmod4$，$-p$ 是基本判别式，其二次字符 $\chi_{-p}$ 是模 $p$ 非主角色。由 (217.1)，至少有严格多于 $p^\kappa$ 个候选素数，其中 $\kappa=\kappa(\epsilon)>0$。

另一方面，不同素因子的乘积不超过 $B$，且每个素因子至少为二，所以

$$\omega(B)\le\frac{\log B}{\log2}\le\frac{A\log p}{\log2}.$$

被 $B$ 排除的候选至多有 $\omega(B)$ 个。选择 $P_0$ 足够大，使

$$p^\kappa-\frac{A\log p}{\log2}>s,$$

便至少留下 $s$ 个素数。$\chi_{-p}(q)=-1$ 还保证 $q\ne p$，并等价于 $q$ 在 $\mathbb Q(\sqrt{-p})$ 惰性。证毕。

更一般地，不必假设 $B\le p^A$；精确可用条件为

$$\omega(B)<p^\kappa-s. \tag{217.3}$$

多项式界只是便于统一表达的充分条件。

## 3. 对实际共同导子的接口

R181 的阶四 CM 边界只在 $p\equiv3\pmod4$ 出现，唯一可能 CM 二次域为

$$F_p=\mathbb Q(\sqrt{-p}).$$

保留 R214 的共同 prime-to-$p$ 环类导子 $a^*=bc$、正规化子二次域判别式 $-D$，并令

$$M^*=D(a^*)^2.$$

如果 $M^*\le p^A$，那么

$$2Da^*\le2M^*\le p^{A+1}\quad(p\ge2).$$

在定理 217.1 取 $B=2Da^*$，得到任意固定数量的奇素数 $q$，使

$$q\le p^{\alpha+\epsilon},\quad q\nmid2pDa^*,\quad q\text{ 在 }F_p\text{ 惰性}. \tag{217.4}$$

因此这些 $q$ 同时处于原自守形式、$K$、全部实际角色的未分歧位置，并杀死全部 $F_p$-CM 新形式的 $q$ 次 Hecke 特征值。

这里**不要求** $q$ 在正规化子二次域 $K$ 中惰性或分裂。若后续几何计算额外要求该符号，需要另证同时指定两个二次符号的素数定理；单独 (217.1) 不给这一附加条件。合适的 Hecke 轨道估计应同时处理 $q$ 在 $K$ 的两种未分歧情形。

也不能从 (217.1) 推出对完全无界的 $D,a^*$ 仍可找到同样小且不除 $Da^*$ 的 $q$。例如可令 $B$ 包含区间内所有候选素数。使用多非剩余定理的价值正是它允许明确、可核对的坏集大小，而不是消除了这个量词。

## 4. 实际阶四类型的非 CM 非消失

现在保留 R215 的实际阶四参数，$a$ 为其准确 prime-to-$p$ 环类导子，$M=Da^2$。对每个 $\delta>0$，R215 定理 215.2 已给出与 $K,a,p,q$ 无关的有效常数 $A_\delta$，使满足 (215.1) 的奇素数 $q\le M$ 有

$$p\ge A_\delta q^2\frac{M^{1+\delta}}{h(\mathcal O_a)}
\quad\Longrightarrow\quad
\exists\text{ 非 CM }f\in\mathcal F_\theta(p^2):
L(\tfrac12,\pi_{f,K}\otimes\Xi)\ne0.
\tag{217.5}$$

此外 R215 的稳定范围 $p\ge q^2M$ 不要求 $q\le M$。

**定理 217.2。** 令

$$\gamma_2=1-2\alpha=1-\frac1{2\sqrt e}=0.69673467\ldots,$$

$$\boxed{\beta_2=\frac1{2\gamma_2}
=\frac1{2-1/\sqrt e}=0.71763329\ldots.} \tag{217.6}$$

则对每个 $\nu>0$，存在与变化的 $K,a,p$ 和实际角色无关的常数 $C_\nu$，使

$$p\ge C_\nu M^{\beta_2+\nu} \tag{217.7}$$

推出 (217.5) 的实际非 CM 中心非消失结论。$C_\nu$ 因所用的 Siegel 下界而一般无效。

**证明。** 环类数公式和普通 Siegel 下界给，对任意 $\eta>0$，

$$h(\mathcal O_a)\ge c_\eta M^{1/2-\eta},$$

其中 $c_\eta>0$ 对全部 $K,a$ 统一。因此 (217.5) 的右侧不超过

$$A_\delta c_\eta^{-1}q^2M^{1/2+\delta+\eta}.$$

给定 $\nu>0$，可选择足够小的正数 $\epsilon,\delta,\eta$，使

$$\frac{1/2+\delta+\eta}{\gamma_2-2\epsilon}<\beta_2+\nu,$$

同时保证 $\gamma_2-2\epsilon>0$ 及 $3(\alpha+\epsilon)<1$。在 (217.7) 的范围取 $C_\nu\ge1$，便有 $M\le p^{1/(\beta_2+\nu)}\le p^2$。从而 $B=2Da\le2M\le p^3$，定理 217.1 可以统一选取满足 $q\nmid2pDa$、在 $F_p$ 惰性且

$$q^2\le p^{2\alpha+2\epsilon}$$

的素数。

如果 $q>M$，则 $q^2M<q^3\le p^{3(\alpha+\epsilon)}<p$，直接落入 R215 的稳定范围，得到所求非 CM 非消失。如果 $q\le M$，使用 (217.5)，此时只需

$$p^{\gamma_2-2\epsilon}>
A_\delta c_\eta^{-1}M^{1/2+\delta+\eta}.$$

由上面的严格指数不等式，扩大 $C_\nu$ 后，(217.7) 对所有足够大的 $p$ 保证此式。对 Pollack 定理要求的有限小 $p$，继续扩大 $C_\nu$ 即可：因 $M\ge3$，可让这些小 $p$ 全部不满足 (217.7)。证毕。

有实际类数时，直接保留更精细的充分不等式

$$p^{\gamma_2-2\epsilon}>
A_\delta M^{1+\delta}/h(\mathcal O_a),$$

并另外检查 Pollack 的阈值 $p>m_0(\epsilon)$ 及 $\omega(2Da)<p^{\kappa(\epsilon)}-1$，无需引入 Siegel 的无效常数。此处也取 $3(\alpha+\epsilon)<1$；若选出的 $q>M$，同样直接使用稳定范围。

若几何代价只有更粗的 $q^4$，同一换算得到

$$\beta_4=\frac1{2(1-4\alpha)}
=\frac1{2(1-1/\sqrt e)}>1.$$

因此 R215 中实际证明的 $q^2$ 轨道代价具有实质意义。旧交接中 $\beta_2=1-1/(2\sqrt e)$ 指的是移到左边后的 $p$ 指数；本文把它明确记为 $\gamma_2$。导子幂阈值的指数是 $\beta_2=1/(2\gamma_2)$，不能混用两者。

## 5. 全部实际参数的共同范围及剩余缺口

令 $a^*=bc$、$M^*=D(a^*)^2$。由 R214，每个参数的 $M\le M^*$。对阶四参数应用定理 217.2，对所有阶 $r>4$ 的参数应用 R213 的统一 $M^{1/2+\eta}$ 范围，并对三次 Steinberg 行应用 R87，扩大共同常数后得到：

$$\boxed{p\ge C_\nu(M^*)^{\beta_2+\nu}}$$

使每个所需的实际深度零类型都存在一个非 CM 新形式，具有对应实际角色的非零中心值；三次 Steinberg 行也非零。两种符号均逐个适用，常数不依赖参数数量。这里只是每个参数各有非零因子，不声称同一个新形式同时对全部参数非零。

当 $(p+1)/6$ 为奇数时，R181 的全 Mellin 阶系统可以只用奇阶参数，故本来就不需阶四 CM 过滤；R213 与 R87 的 $M^{1/2+\nu}$ 范围更强，且可用原三次导子 $c$。需要全部偶阶参数时，必须保留 R214 的共同导子 $bc$。

这些是实际非消失范围，仍没有给变化的 $D,a^*$ 上界，也没有排除整 $j$ 的异常曲线。不满足主题 README 的主问题完成标准。

## 来源

- Paul Pollack, *Bounds for the first several prime character nonresidues*, **Proceedings of the American Mathematical Society 145** (2017), 2815–2826，Theorem 1.1；[AMS 原刊 DOI](https://doi.org/10.1090/proc/13432)，[作者 PDF](https://www.pollack-math.net/hudson.pdf)，[作者稿全文](https://arxiv.org/html/1508.05035v2)。这里仅引用已经发表的多素数非剩余定理；避坏集与指数换算的证明已写在本文。
- R181：阶四 CM 边界、唯一可能的 CM 二次域以及全部 Mellin 阶所需的实际参数；R214：变化的共同 prime-to-$p$ 导子。
- R215：正 Hecke 卷积的完整谱端、两个 $K_q$ 分裂情形的主项与 regular 计数、$q^2$ 有效估计及稳定范围。R213、R87：其余实际参数的统一非消失。
- R83 §7、R87 §8：对变化虚二次域和环类导子的 Siegel 类数下界及其无效性。
