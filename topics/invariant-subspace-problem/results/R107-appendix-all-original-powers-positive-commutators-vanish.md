# R107 附录：原 Haar 全整数幂的正序交换子必零

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整原结构结论。** 对原 Haar 任意尾 $C$、任意整数 $r\ge1$ 及任意有界复算子 $T$，若 $C^rT-TC^r$ 保持函数正锥，则它必为零；$T$ 自身不必保正。因此原两侧正半交换子锥精确等于正交换子锥。本文不重计 [R107 §§5–7](R107-centered-order-and-compactness-obstructions.md) 已经证明的 AT 紧化失败或 AM-compact 支配失败。

## 1. 正序与抽象弱返回引理

本稿的 $D\ge_{\mathrm{cone}}0$ 始终表示 $D$ 把非负函数送成非负函数，不表示 $D$ 是 Hilbert 空间正自伴算子。保正算子的复合仍保正，其锥在弱算子拓扑中闭。

**引理 1.1。** 设 $B$ 是复 Banach 格上的有界保正算子，存在整数 $m_j\to\infty$、正数 $b_j$ 和常数 $\gamma>0$，使

$$
B^{m_j}/b_j\xrightarrow{\mathrm{WOT}}\gamma I.
\tag{1.1}
$$

若 $T$ 有界且 $D=BT-TB\ge_{\mathrm{cone}}0$，则 $D=0$。对相反正序也成立。

**证明。** 固定充分大 $j$，使 $m=m_j\ge1$。准确的有限望远镜为

$$
B^{m+1}T-TB^{m+1}
=\sum_{k=0}^{m}B^k D B^{m-k}.
\tag{1.2}
$$

所有项都保正，故

$$
\frac{B^{m+1}T-TB^{m+1}}{b_j}
\ \ge_{\mathrm{cone}}\
\frac{B^mD+DB^m}{b_j}.
\tag{1.3}
$$

由 (1.1)，左边弱趋于 $\gamma(BT-TB)=\gamma D$，右边弱趋于 $2\gamma D$。弱闭性给 $-\gamma D\ge_{\mathrm{cone}}0$。它与 $D\ge_{\mathrm{cone}}0$ 合起来迫 $D$ 在正锥上为零；正锥复线性张成整个空间，故 $D=0$。反向正序只需把 $T$ 换成 $-T$。证毕。

引理没有要求 $T$ 保正、紧或属于某个先验交换代数，也没有用 $T$ 的统一族范数。所有正序项是 $B^kDB^{m-k}$；不能把它们误当成一般 Hilbert 正半定序中的正项。

## 2. 真实 Haar 全幂及有限放大

固定原尾 $C=A^{(m_0)}$。对整数 $r\ge1$，记其二进位支撑为 $J_r$，$q_r=|J_r|$。原幂恒等式与 [R140 §2](R140-invariant-subquotient-type-and-fixed-first-regularization.md) 给

$$
\frac{C^{r2^j}}{\|C^{r2^j}\|}
=\prod_{\ell\in J_r}N_{j+\ell}
\xrightarrow{\mathrm{WOT}}2^{-q_r}I.
\tag{2.1}
$$

归一化分母是原实际正范数，非零。$C^r$ 是保正加权平移，所以对 $B=C^r$，
$m_j=2^j$、$b_j=\|C^{r2^j}\|$、$\gamma=2^{-q_r}>0$ 满足引理。因而

$$
\boxed{
C^rT-TC^r\ge_{\mathrm{cone}}0
\ \text{或}\ 
C^rT-TC^r\le_{\mathrm{cone}}0
\quad\Longrightarrow\quad C^rT=TC^r.}
\tag{2.2}
$$

同一结论适用于每个有限放大 $(C^r)^{(d)}$，按直和的逐坐标函数正锥取序；(2.1) 原样放大，$T$ 可以混合所有拷贝。

常数归一与标量平移也不改变结论。若 $a\ne0$、$b\in\mathbb C$，则

$$
[aC^r+bI,T]=[C^r,aT].
$$

所以只要该交换子在上述函数锥序下有一个符号，就必为零。这一步不需要声称复数倍 $aC^r+bI$ 本身保正；应用引理的正算子仍是 $C^r$。

## 3. 实际两侧半交换子锥的准确等式

特别对 $T\ge_{\mathrm{cone}}0$，得到

$$
\boxed{
\{T\ge_{\mathrm{cone}}0:TC^r\le_{\mathrm{cone}}C^rT\}
=
\{T\ge_{\mathrm{cone}}0:TC^r\ge_{\mathrm{cone}}C^rT\}
=
\{T\ge_{\mathrm{cone}}0:TC^r=C^rT\}.}
\tag{3.1}
$$

R107 §5 的定义确实把两侧半交换子作为更宽的形式条件来处理；其高位角证明未断言这些集合严格包含正交换子。新式 (3.1) 说明，在当前原 Haar 模型中，不能把该处“更大”理解为严格包含。旧的高位角、全部正半交换子族 AT 条件失败及 AM-compact 支配失败均继续有效，不需重新计算或重登记。

新[保持正锥的共同分母](R267-appendix-positivity-preserving-common-powers-and-no-compact-domination.md)及其各实际整数逆都属于右端这个正交换子锥。它们的存在并未改变旧 AT 条件失败的结论，也不提供所需复二次分子 $Y^2=CP^2$。

## 4. 原子商的边界

原不变旗商虽有 (2.1) 的同一标量弱返回，却未必具有从原 $L^2$ 继承的函数格结构；普通闭不变子空间也未必是子格。因此本稿不对任意普通原子商自动写下 (2.2) 的函数正序版本。

若某个具体限制或子商另已给定真正的 Banach 格正锥，使其原诱导 $C_Q^r$ 保正，并且同一弱返回 (2.1) 成立，则引理 1.1 当然直接适用。这是明确的附加正锥输入，不由 Hilbert 商本身提供。本文也不把正序交换子必零改述成自交换子、hyponormal 或普通 ISP 的结论。
