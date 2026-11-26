# 秩至少为 2 的椭圆曲线：对无穷多个 $p$，$\text{Ш}[p^\infty]$ 有限

> 2026-11-14 从私有仓库 `Rogerhu12/math-research` 迁入本公开仓库（路径不变）；之后只在本仓库工作，计算用本仓库的 GitHub Actions（根 README 规矩第 13 条）。

## 问题

对 $\mathbb Q$ 上**解析秩** $\operatorname{ord}_{s=1}L(E,s)\le1$ 的椭圆曲线，Gross–Zagier–Kolyvagin 给出代数秩等于解析秩及 $\text{Ш}(E/\mathbb Q)$ 有限。这里不能仅以代数秩 $\le1$ 作为该定理的输入（见 R1）。对秩 $\ge2$ 的曲线，目前不知道任何一条曲线的 $\text{Ш}$ 有限；对单条曲线，只能逐个素数检查 $\text{Ш}[p^\infty]$ 是否有限。

**问题：** 证明存在一条椭圆曲线 $E/\mathbb Q$，满足 $\operatorname{rank}E(\mathbb Q)\ge2$，并且对无穷多个素数 $p$，$\text{Ш}(E/\mathbb Q)[p^\infty]$ 有限。

## 完成标准

- 主要目标：给出（或证明存在）这样一条 $E$，完整证明：
  1. $\operatorname{rank}E(\mathbb Q)\ge2$；
  2. 存在无穷多个素数 $p$，使 $\text{Ш}(E/\mathbb Q)[p^\infty]$ 有限（等价地，$p^\infty$-Selmer 群的 $\mathbb Z_p$-余秩等于 $\operatorname{rank}E(\mathbb Q)$）。
- 更强的目标：
  - 对这条 $E$ 和**所有**素数 $p$ 成立；若还证明除有限多个 $p$ 外初级部分为零，则进一步得到 $\text{Ш}(E/\mathbb Q)$ 有限（每个初级部分有限本身不足以推出全群有限，见 R1）；
  - 对这条 $E$ 再证明 $\operatorname{ord}_{s=1}L(E,s)=\operatorname{rank}E(\mathbb Q)$，或完整 BSD 公式；
  - 对一族无穷多条秩 $\ge2$ 的曲线成立；
  - 对 $\mathbb Z$ 中一个正密度的素数集合成立。
- 以下只算中间进展：
  - 只对有限多个 $p$ 成立，不论多少个（包括逐个素数用下降法或 $p$-adic 方法算出的结果）；
  - 依赖未证明的假设，例如 $p$-adic 高度非退化（Schneider 猜想）、$p$-adic $L$ 函数的零点阶、Iwasawa 主猜想中尚未证明的部分、GRH 或其他猜想；
  - 只对秩 $\le1$ 的曲线，或只对 Selmer 余秩 $\le1$ 的情形成立；
  - 只对"大多数 $p$"在启发式或数值意义下成立；
  - 只证明了存在无穷多对 $(E,p)$，而没有固定一条 $E$；
  - 数值验证。
- 来源中尚未被公认的论证，若要使用，必须在本仓库内给出完整证明，不能直接引用。
- 开工前先核对文献现状，写清已证明的范围和出处。

## 来源

- B. Gross, D. Zagier, *Heegner points and derivatives of L-series*, Invent. Math. 84 (1986)；V. A. Kolyvagin, *Euler systems*（Grothendieck Festschrift II, 1990）。
- K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004)。
- P. Schneider, *p-adic height pairings I, II*, Invent. Math. 69 (1982), 79 (1985)；B. Perrin-Riou 关于 $p$-adic 高度与 $p$-adic BSD 的工作；B. Mazur, J. Tate, J. Teitelbaum, *On p-adic analogues of the conjectures of Birch and Swinnerton-Dyer*, Invent. Math. 84 (1986)。
- W. Stein, C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013)：对秩 2 的具体曲线，逐个素数证明 $\text{Ш}[p^\infty]$ 有限的计算。
- C. Skinner, E. Urban, *The Iwasawa main conjectures for GL₂*, Invent. Math. 195 (2014)；X. Wan、W. Zhang、C. Skinner 等关于 $p$-逆定理的工作。
- J. Cremona 的椭圆曲线表和 LMFDB 中秩 2 曲线（例如导子 389 的曲线 389a1）的 $\text{Ш}$ 解析阶数据。
- OpenAI 公开预印本（仓库 [openai/math](https://github.com/openai/math)，2026 年 9–10 月），秩或 Selmer 余秩 $\le1$ 的结果：*Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank*、*The Selmer converse for elliptic curves at every prime*、*The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one*（结果族 002）。
- 本仓库相关课题：`topics/q-bsd`。

以上书目信息凭记忆列出，卷号年份以原文为准；OpenAI 预印本的标题取自其公开目录。

## 状态

进行中（Astra-rank2-Sha-7d29daa5-20261126 / 2026-11-26）。原检查点未发表的 R235/R237 已重做并登记，继续原中央非零、Heegner 低阶项与实际深关系；主目标尚未完成。背景与全群有限性的两处逻辑措辞已据 R1 校正；固定曲线和无穷素数的完成标准未改变。
