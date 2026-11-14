# Hilbert 空间上的不变子空间问题

> **2026-11-14 已迁移：本课题整体搬到公开仓库 `Rogerhu12/math-research-public`，路径不变（`topics/invariant-subspace-problem/`）。**从现在起只在那边工作：clone 那个仓库（部分克隆，见其根 README 规矩第 10 条），在那边 pull、commit、push；计算直接用那个仓库自己的 GitHub Actions（规矩第 13 条）。本目录不再更新，迁移后仍推到这里的内容由协调员补搬过去。令牌不变。

## 问题

设 $H$ 是可分、无穷维的复 Hilbert 空间，$T:H\to H$ 是有界线性算子。

**问题：** 是否每个这样的 $T$ 都有非平凡的闭不变子空间，即存在闭子空间 $\{0\}\ne M\ne H$ 使 $TM\subseteq M$？

证明或否定均可。

## 完成标准

- 完整答案二选一：
  - 证明 $H$ 上每个有界算子都有非平凡闭不变子空间；
  - 构造 $H$ 上一个有界算子，并完整证明它没有非平凡闭不变子空间。
- 以下只算中间进展：
  - 只对某一类算子成立，例如与非零紧算子交换的算子、次正规算子、多项式紧算子、谱满足某种条件的压缩算子、拟幂零算子的某个子类；
  - Banach 空间（包括 $\ell^1$ 等非 Hilbert 空间）上的结论；
  - 只得到不变闭凸集、几乎不变子空间、非闭不变子空间，或关于超不变子空间、不变投影、传递代数的结论；
  - 条件性结论，或把问题化归到另一个未证猜想；
  - 有限维截断或数值实验。
- 来源中尚未被公认的论证，若要使用，必须在本仓库内给出完整证明，不能直接引用。
- 开工前先核对文献现状：若某些情形已被证明或已有公认的完整答案，写清出处和范围，再以尚未解决的部分为目标。

## 来源

- N. Aronszajn, K. T. Smith, *Invariant subspaces of completely continuous operators*, Ann. of Math. 60 (1954)。
- A. R. Bernstein, A. Robinson, *Solution of an invariant subspace problem of K. T. Smith and P. R. Halmos*, Pacific J. Math. 16 (1966)；P. R. Halmos 对多项式紧算子的后续证明 (1966)。
- V. I. Lomonosov, *Invariant subspaces for the family of operators which commute with a completely continuous operator*, Funct. Anal. Appl. 7 (1973)。
- S. Brown, *Some invariant subspaces for subnormal operators*, Integral Equations Operator Theory 1 (1978)；S. Brown, B. Chevreau, C. Pearcy, *On the structure of contraction operators II*, J. Funct. Anal. 76 (1988)。
- Banach 空间上的反例：P. Enflo, *On the invariant subspace problem for Banach spaces*, Acta Math. 158 (1987)；C. J. Read, *A solution to the invariant subspace problem*, Bull. London Math. Soc. 16 (1984)；C. J. Read, *A solution to the invariant subspace problem on the space ℓ¹*, Bull. London Math. Soc. 17 (1985)；C. J. Read, *Quasinilpotent operators and the invariant subspace problem*, J. London Math. Soc. 56 (1997)。
- S. A. Argyros, R. G. Haydon, *A hereditarily indecomposable L∞-space that solves the scalar-plus-compact problem*, Acta Math. 206 (2011)。
- 综述：H. Radjavi, P. Rosenthal, *Invariant Subspaces*（1973，Dover 2003）；I. Chalendar, J. R. Partington, *Modern Approaches to the Invariant-Subspace Problem*（Cambridge, 2011）。
- OpenAI 公开预印本（仓库 [openai/math](https://github.com/openai/math)，结果族 293 "Invariant projections, hyperinvariant subspaces, and transitive algebras"，2026-09-27）：
  - [*Backward intertwiners and a transitive commutant*](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026)（16 页）。摘要：在每个可分无穷维复 Hilbert 空间上构造非零、范数拟幂零的有界算子，它没有非零真闭超不变子空间，从而否定回答超不变子空间问题；其交换子是真的、强算子拓扑闭的、含单位的传递复算子代数。主结果列为已在 Lean 中形式化，范围见 [lean/docs/293.md](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/293.md)。
  - [*Invariant-projection counterexamples for every irrational rotation*](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026)（47 页）。摘要：对每个无理角，构造一个只有一个零点、对数积分为 $-\infty$ 的连续非负圆周权，使相应的加权旋转在超有限 II$_1$ 因子中没有非平凡不变投影，否定回答 Zhu、Fang、Shi 的问题；该算子非零且范数拟幂零。
- 近年未被公认的声称：P. Enflo 2023 年 arXiv 预印本声称对 Hilbert 空间给出肯定证明；C. W. Neville 的 *A Proof of the Invariant Subspace Conjecture for Separable Hilbert Spaces*（[arXiv:2307.08176v2](https://arxiv.org/abs/2307.08176v2)，2023）也声称给出肯定证明。书目方向已于 2026-11-12 对照原文更正；本会话对来源状态与局部缺口的核查见 `notes/2026-11-12-literature-audit.md`。

以上书目信息凭记忆列出，卷号年份以原文为准。

## 状态

进行中（Astra-ISP-789f / 2026-11-14）。主问题未解决；已证中间结论见 `results.md`，具体缺口见 `open.md`。
