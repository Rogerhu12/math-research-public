# 续做第二轮：公开文献边界核验

日期：2026-11-12（Asia/Taipei）。会话：serre-uniformity-resume2；并行文献分支。

**状态：原始文献核验，不是 Serre 一致性的证明。** 已阅读根 README、本题 README、HANDOFF、open 及相关 R6/R7/R41。本文不增加结果编号；主会话统一提交。

## 1. 完整非分裂正规化子仍是实际剩余情形

L. Furio、D. Lombardo，*Serre's uniformity question and proper subgroups of $C_{ns}^+(p)$*，arXiv:2305.17780v2，2025-11-25，最终版、将刊 Algebra & Number Theory：[原文 HTML](https://arxiv.org/html/2305.17780v2)。

- Theorem 1.5：$E/\mathbb Q$ 非 CM、$p>37$ 时，像为整个 $\mathrm{GL}_2(\mathbb F_p)$ 或完整的 $C_{ns}^+(p)$。
- Theorem 1.6：对 $p\ne2,3$，指定指数三群 $G(p)=C_{ns}(p)^3\cup wC_{ns}(p)^3$ 能成为非 CM 曲线的像，当且仅当 $p=5$。
- Theorem 1.8：$p>37$ 时 $X_{G(p)}(\mathbb Q)$ 只有尖点和 CM 点。这里的曲线是 $X_{G(p)}$，不是 $X_{ns}^+(p)$。

文中的整性、$p^4\mid j(E)$、$j(E)=p^kc^3$ 及 Runge 上界针对 $G(p)$。不能删去这个像假设后套用到完整正规化子。其 Theorem 4.1 则确实适用于完整正规化子的高度依赖有效满射界，但界中保留 Faltings 高度，未给绝对常数。

**有限整点分类的核验提醒。** 同文 Claim 1.4 后指出，Bajolet–Bilu–Matschke 关于 $11\le p<100$ 的非 CM 整点不存在的论证似有 gap，并指向 Furio 博士论文 Remark 5.3.10。此处只如实记录作者提出的疑点，未在本轮重审该算法；不能把这个声称当成新增无疑点输入。Furio–Lombardo 的主定理并不依赖将其视为已证。

## 2. Le Fourn–Lemos 的整性逻辑

S. Le Fourn、P. Lemos，*Residual Galois representations of elliptic curves with image contained in the normaliser of a non-split Cartan*，Algebra & Number Theory 15 (2021), 747–771：[原文](https://arxiv.org/html/2002.02714v2)。

Theorem 1.2：非 CM 的 $E/\mathbb Q$，若 $p>1.4\times10^7$，或 $p\notin\{2,3,5,7,11,13,17,37\}$ 且 $j(E)\notin\mathbb Z$，则非满像必为完整正规化子。因此被证的整性方向是
$$\operatorname{Im}\rho_{E,p}=G(p)\Longrightarrow j(E)\in\mathbb Z,$$
并非完整 $C_{ns}^+(p)$ 像推出整性。

Remark 1.6 解释了秩零商障碍：BSD 预言 $J_{ns}^+(p)$ 没有非零秩零商。故用于 $X_{G(p)}$ 的秩零商和形式浸没论证不能直接移植。

Proposition 5.2 给真正适用于完整正规化子的局部条件：$p\ge5$ 时，所有 $\ell\not\equiv\pm1\pmod p$ 处潜在良约化，特别 $p\nmid\operatorname{den}(j)$。R2 已给包含 Tate 单位部分的更精确版本，本轮不重复登记。

## 3. Lemos 的两个家族定理

P. Lemos，*Serre's Uniformity Conjecture for Elliptic Curves with Rational Cyclic Isogenies*，Trans. AMS 371 (2019)：[原文](https://arxiv.org/html/1702.01985v2)。Theorem 1.1：非 CM、存在非平凡有理循环同源时，所有 $p>37$ 满像。Proposition 2.2 就是上节的潜在良约化条件。

P. Lemos，*Some cases of Serre's uniformity problem*，Math. Z. 292 (2019), 739–762：[原文](https://link.springer.com/article/10.1007/s00209-018-2189-8)。Theorem 1.4：存在某个素数 $q$ 的分裂 Cartan 正规化子像时，所有 $p>37$ 满像。Proposition 1.5 的整性需要同时满足 $p\ge11$ 的非分裂正规化子像和另一素数 $q\ne p$ 的分裂正规化子像；第二个条件不能删除。

所以实际 $p>37$ 异常族不能存在任何有理循环同源，也不能在任一辅助素数上落入分裂正规化子。这是后续小辅助素数分析使用的严格输入。

## 4. 2026 年的新方法与固定层

S. Hashimoto、G. M. Lido、D. Lombardo、N. Mascot、P. Parent，*Equationless quadratic Chabauty for non-split Cartan modular curves*，arXiv:2608.10919v1，2026-08-11：[原文](https://arxiv.org/html/2608.10919v1)。

Theorem 1.0.1 重新得到 $X_{ns}^+(13)(\mathbb Q)$ 的七个 CM 点。Remark 3.0.7 明确全文假设 $r=g$；该条件在具体层可借助 newform 的解析秩及 Kolyvagin–Logachev 验证。对一般层的秩受控商占比只给出预期。无模型算法并不提供随层一致的共同根排除。本课题 R45/R47 已处理实际 Heegner 商与完整必要方程，缺口仍是共同根，不应退回重做有限性。

L. Furio、D. Lombardo，*On 7-adic Galois representations for elliptic curves over $\mathbb Q$*，Proc. LMS 133 (2026), e70193，2026-08-12：[原文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.70193)。主结果处理固定层 $X_{ns}^+(49)$；Question 1.1 后仍明确记录 $\mathbb Q$ 上一致性开放。Proposition 1.8 的一般族结果带 $abc$ 假设，不可当无条件输入。

## 5. 最小满射素数的真正量词

T. Genao、J. Mayle、J. Rouse，*A uniform bound on the smallest surjective prime of an elliptic curve*，Ramanujan J. 70 (2026), article 22，2026-05-12：[原文](https://link.springer.com/article/10.1007/s11139-026-01376-8)。

Theorem 2 证明每条非 CM 曲线存在 $\ell\le7$，使整个 $\ell$ 进表示满像；除六个显式 $j$ 外，可取 $\ell\le5$。同段另指出至少一个模 $2,3,5$ 表示满像，但模 $2$、模 $3$ 满像和对应完整进表示满像应区分。

该定理给固定大小的辅助群，而不是固定大小的 Frobenius 检测素数：$\ell$ 是表示系数的素数，$q$ 才是待找的良好约化素数。后续推导见 `2026-11-12-small-surjective-prime-resume2.md`，在那里完整分析二次域交叠、判别式和有效 Chebotarev 的参数依赖。

## 6. 未得到的结论

本次原始文献检索没有找到排除全部充分大 $p$ 的完整 $C_{ns}^+(p)$ 情形的定理。上述结果分别给像约化、带额外结构的家族排除、具体层算法或依赖高度/导子的界。主目标仍须新的全局输入，且不能将有限计算、正密度或条件性估计登记为完成。
