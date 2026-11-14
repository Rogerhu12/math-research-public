# 既有空谱锚对近共振辅助问题的完整覆盖范围

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065。
性质：旧定理适用范围审计与明确推论，不登记为新的排核机制。
普通 Hilbert ISP 仍开放。

## 1. 审计结论

对非绝对可和主行 $a\in\ell^2\setminus\ell^1$，
只要存在相位 $\phi$ 满足
$$
\boxed{
\mathcal D(a,\phi)
=\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\phi}a_j)\right)<\infty,
}
\tag{1.1}
$$
既有 R134/R138 已给主 first 空谱。
既有 R134 §3 又给任意有界交换扰动及任意有界交换系数首一多项式的自然域双射与有界逆。
R155 已把这一结论落实到任意复 $\ell^2$ 指数权和任意有限组 $\ell^1$ 辅助模式的点态多项式。

因此，对任意常数 $a_*,b_*\in\mathbb C$、任意 $b\in\ell^2$、任意 $c\in\ell^1$，
(1.1) 已经保证
$$
\boxed{
\left[
u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)
\right]e^w
\text{ 非零且对原实际 }A\text{ 循环},
}
\tag{1.2}
$$
其中 $u=a_*+\sum a_j\chi_j$、$w=b_*+\sum b_j\chi_j$。

这里无需
$c_j\asymp a_j^\kappa$、偏离正相位、辅助排序预算或
$\operatorname{Re}b_j\ge0$。
特别，正同射线的规则慢幂
$a_j=e^{i\phi}(j+1)^{-\sigma}$、$1/2<\sigma\le1$，
即使 $a_*=0$，也全部在旧覆盖范围内。
不得将它们作为新近共振或新增生方法首次关闭的子类。

## 2. 已完整核读的实际来源

本次逐篇阅读全文的来源与 blob 为：

| 主文 | 关键位置 | blob |
| --- | --- | --- |
| [R128](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md) | §6 真实 Cayley 增生与图核心；§9 同射线非 $\ell^1$ 空谱及全部不变限制满射 | 68b0e472be3ab10afa2aa10e80d4848df4248b44 |
| [R134](../results/R134-empty-spectrum-first-chaos-polynomial-cyclicity.md) | §2 可和相位缺陷；§3.1 逆拟幂零；§3.2 首一有界系数与有界交换扰动；§3.3 不变限制完整域 | 915d801bce6d98aa5e8508a32971a0f15e115788 |
| [R138](../results/R138-first-chaos-complete-spectrum-classification.md) | §1 三分谱分类；§§3–7 空谱与全平面连续谱的两向证明 | 33ff17c7652b4606bca1c2efd473886223cb70d7 |
| [R155](../results/R155-empty-anchor-bounded-auxiliary-polynomials.md) | §1 任意有界辅助与复指数权；§§3–6 真实 Bell 最高单位、自然域有界逆与循环性 | 85f629c638815ef86a4e202d90405996df28efeb |
| [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md) | §§2–5 首一自然图及核上有界 first；§10 倾斜 first 与真实图循环判据 | 710c2042e08710f1f1fe20546c3996ade0b6a194 |

以下重列与近共振问题直接有关的短证明，
以免把来源中的“循环”误读为未经证明的限制预解界。

## 3. 空谱与真实有界逆的两个稳定步骤

令 $X_0=X_u$ 为原未倾斜 first。
由 (1.1) 和 R134，
$$
R=X_0^{-1}\in\{A\}'
$$
是有界、单射、稠密像的算子。
它是拟幂零的：
对每个 $\mu\ne0$，
$$
(R-\mu I)^{-1}
=-\mu^{-1}I-\mu^{-2}(X_0-\mu^{-1}I)^{-1}
$$
为真实有界双侧逆。
故 $\sigma(R)=\{0\}$。

逐次使用 $X_0R=I$ 与 $RX_0=I$ 于自然域，得到
$$
\boxed{\operatorname{Dom}X_0^p=\operatorname{Ran}R^p.}
\tag{3.1}
$$
因此这些自然幂是闭算子；没有借用“闭算子的幂自动闭”这一错误断言。

### 3.1 任意有界交换扰动都保持空谱

取任意 $H\in\{A\}'$。
R88 的完整交换子代数可交换，故 $H$、$R$ 交换。
对任意 $\lambda\in\mathbb C$，
$$
X_0+H-\lambda I
=[I+(H-\lambda I)R]X_0
\quad\text{于 }\operatorname{Dom}X_0.
\tag{3.2}
$$
又
$$
\|[(H-\lambda I)R]^n\|^{1/n}
\le\|H-\lambda I\|\,\|R^n\|^{1/n}\longrightarrow0.
$$
所以方括号是真正有界单位，
$$
\boxed{
(X_0+H-\lambda I)^{-1}
=R[I+(H-\lambda I)R]^{-1}\in\{A\}'.
}
\tag{3.3}
$$
右侧的像属于 $\operatorname{Ran}R=\operatorname{Dom}X_0$。
(3.2)–(3.3) 两向相乘均在准确域上成立。
这不要求 $H$ 属于范数代数、字符为零或具有快尾。

R176 的倾斜 first
$$
X_b=X_0+H_{a,b},\qquad
H_{a,b}=\sum_ja_j(R_j-V_j)\in\mathcal A
$$
具有范数收敛的有界差：
高位差由常数乘 $|a_jb_j|$ 控制，Cauchy–Schwarz 保证可和；
有限低位逐个付实际逆。
因此对任意复 $b\in\ell^2$，(3.3) 适用。
不需要限制 $\operatorname{Re}b_j$ 的符号。

### 3.2 任意有界交换系数首一多项式

现在把 $X$ 记为任意上述有界交换扰动后的空谱 first，
仍令 $R=X^{-1}$。
取任意 $D_0,\ldots,D_{p-1}\in\{A\}'$。
定义
$$
P(X)=X^p+\sum_{k=0}^{p-1}D_kX^k,
\qquad \operatorname{Dom}P(X)=\operatorname{Dom}X^p.
$$
令
$$
U=I+\sum_{k=0}^{p-1}D_kR^{p-k}
=I+R\left(\sum_{k=0}^{p-1}D_kR^{p-k-1}\right).
\tag{3.4}
$$
括号是固定有界交换子，所以 $U-I$ 拟幂零。
$U$ 是有界单位，且 $U^{\pm1}$ 与 $R$ 交换并保持
$\operatorname{Ran}R^p=\operatorname{Dom}X^p$。
于是
$$
P(X)=UX^p=X^pU,
$$
$$
\boxed{P(X)^{-1}=R^pU^{-1}\in\{A\}'.}
\tag{3.5}
$$
该逆定义于整个 $H$，像落入指定自然域。
$U$ 有界可逆与 $X^p$ 闭共同给 $P(X)$ 闭。
减任意标量只改变 $D_0$，所以 $P(X)$ 仍为空谱。

## 4. 为什么逆确实保持未知不变限制

设 $M$ 为任意闭 $A$ 不变子空间。
R88 给每个有界 $A$ 交换子保持 $M$。
R128 另给真实域与像保持
$$
X(\operatorname{Dom}X\cap M)\subseteq M.
\tag{4.1}
$$
对有界交换扰动，定义域不变，新增有界项也保持 $M$，
所以 (4.1) 仍成立。

由 (4.1) 逐级归纳，
$$
\operatorname{Dom}X^p\cap M=R^pM.
\tag{4.2}
$$
一向由 $R$ 保持 $M$ 和 (3.1) 得到；
另一向对 $x\in\operatorname{Dom}X^p\cap M$，
先得 $Xx,\ldots,X^px\in M$，再用
$x=R^p(X^px)$。

(3.5) 的每个有界因子都保持 $M$，
因此每个 $P(X)-\lambda I$ 的限制
$$
\operatorname{Dom}X^p\cap M\longrightarrow M
$$
单射、满射，其逆就是全局逆在 $M$ 上的限制。
这里没有把全空间稠密像直接下放到未知限制；
使用的是明确的双侧有界逆及独立证明的域保持。

也可以用这条事实检查 R176 的核论证：
若某个首一自然多项式核 $M$ 非零，
R176 使 $X_M$ 成为全域有界算子；
而 (3.3)、(4.1) 使每个 $\lambda\in\mathbb C$ 都在其预解集。
非零 Banach 空间上有界算子的谱不为空，产生矛盾。
不过 (3.5) 已直接给出更强的全空间双射，无须只停在排核。

## 5. 近共振向量与一般慢辅助的直接回收

对任意 $c\in\ell^1$，令
$$
Y=\sum_jc_j(R_j-I),\qquad
B=\sum_ja_j^2(R_j-I)^2.
$$
它们都是有界交换子。
取 $p=2$、$D_1=0$、$D_0=Y-B$，(3.5) 给
$$
T=X_b^2+Y-B
$$
在 $\operatorname{Dom}X_b^2$ 上双射，
其逆属于 $\{A\}'$。
R176 的真实作用恒等式为
$$
Te^w=
\left[u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)\right]e^w.
$$
因此
$$
e^w=T^{-1}(Te^w)
$$
属于目标向量的闭 $A$ 循环空间；
$e^w$ 已循环，故得到 (1.2)，并自动保证目标非零。

R155 的原定理其实更广：
有限多个 $\ell^1$ 辅助 $v_1,\ldots,v_d$ 可完全重叠且任意慢，
若
$$
F(U,V)=\sum_{k=0}^p U^k r_k(V),\qquad p\ge1,
$$
最高点态系数在辅助的实际全零物理锚处非零，
则任意 $(F(u,v)-\lambda)e^w$ 循环。
其真实最高 Bell 系数的字符恰为该非零锚值，
所以是实际单位。
这已覆盖首一主变量多项式及任意有界辅助低次项；
本次范围审计不把它重复登记为新结论。

## 6. 有界主行的另一旧单位分支

若 $a\in\ell^1$，则 $X_b\in\mathcal A$，
且倾斜不改变字符：
$$
\chi(X_b)=a_*+\sum_j a_j=:\alpha.
$$
$Y,B$ 字符均为零，故
$$
\chi(X_b^2+Y-B)=\alpha^2.
$$
当 $\alpha\ne0$，唯一字符的范数代数使该目标算子本来就是单位。
所以可和主行的真正困难分支是
$a_*+\sum_j a_j=0$；
不能把一般未居中的正系数可和例子作为新排核机制的证据。

这条简单单位分支与非 $\ell^1$ 的空谱分支不同：
非绝对可和主行不应指定一个不存在的绝对系数和或范数代数字符。

## 7. 真正不落旧空谱范围的规则慢幂

取
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad \frac12<\sigma\le1.
\tag{7.1}
$$
对每个 $\phi$，偶数和奇数位的相位缺陷分别是
$$
(j+1)^{-\sigma}(1-\cos\phi),\qquad
(j+1)^{-\sigma}(1+\cos\phi).
$$
两子行质量都发散，这两个非负因子又不同时为零。
因此
$$
\mathcal D(a,\phi)=\infty\quad\text{对每个 }\phi.
$$
R138 给 $X_u$ 的全平面连续谱。
这一类才需要新的近共振、支撑或核内估计。

新的稀疏偏离支撑定理可以在
$S=\{\lceil k^{1/\sigma}\rceil-1:k\ge1\}$ 上取
$|c_j|\asymp|a_j|^\kappa$，在 $S^c$ 上取 $c_j=0$，
并保留完整 (7.1) 的每个主系数。
它使用的子行幅度为 $k^{-1}$，
偏离的排序幅度为 $k^{-\kappa}$，不属于超三次快辅助。
该明确例子不与上述旧空谱结论重复。

另一方面，(7.1) 在所有充分大位上都有
$|c_j|\asymp|a_j|^\kappa$ 的全支撑高阶偏离，
不能由本次空谱审计关闭。准确地，$\sigma=1$ 已由新的近共振统一准则关闭；
这里真正尚未闭合的全支撑规则慢幂范围是 $1/2<\sigma<1$。
R259 的原点解析 Bell 分支也没有提供这个二次分歧核上的统一预解界。
需要继续处理的是真正的任意相位慢分支，而非已经覆盖的同射线特例。
