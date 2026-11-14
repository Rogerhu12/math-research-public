# Serre 一致性问题

> 2026-11-14 从私有仓库 `Rogerhu12/math-research` 迁入本公开仓库（路径不变）；之后只在本仓库工作，计算用本仓库的 GitHub Actions（根 README 规矩第 13 条）。

## 问题

对 $\mathbb Q$ 上椭圆曲线 $E$ 和素数 $p$，记
$$\bar\rho_{E,p}:\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)\to\mathrm{GL}_2(\mathbb F_p)$$
为 $p$ 挠点上的 Galois 表示。Serre（1972）证明了：$E$ 无复乘时，对充分大的 $p$（依赖于 $E$），$\bar\rho_{E,p}$ 是满射。

**问题（Serre 一致性）：** 是否存在绝对常数 $C$，使得对 $\mathbb Q$ 上每条无复乘的椭圆曲线 $E$ 和每个素数 $p>C$，$\bar\rho_{E,p}$ 都是满射？预期可取 $C=37$。

## 完成标准

- 主要目标：完整证明存在这样的绝对常数 $C$（不必显式）。
- 更强的目标：证明 $C=37$ 可取，即对所有 $p>37$ 成立；或对任意数域 $K$ 证明存在只依赖于 $K$ 的常数。
- 反面也算完整答案：给出无复乘椭圆曲线 $E_n/\mathbb Q$ 与素数 $p_n\to\infty$，并完整证明 $\bar\rho_{E_n,p_n}$ 都不是满射。
- 以下只算中间进展：
  - 只对部分曲线成立，例如半稳定曲线、有有理同源的曲线、$j$ 不变量整的曲线、指定导子或高度范围的曲线；
  - 只排除部分可能的像（例如只排除 Borel、分裂 Cartan 正规化子或例外像），而没有排除全部；
  - 只对有限多个 $p$ 成立；
  - 密度或"几乎所有曲线"意义下的结论；
  - 条件性结论（例如依赖 GRH、abc 或其他未证猜想）；
  - 数值验证或对有限多条曲线的计算。
- 来源中尚未被公认的论证，若要使用，必须在本仓库内给出完整证明，不能直接引用。
- 开工前先核对文献现状：写清哪些子群情形已被排除、出处和范围，再以尚未解决的部分为目标。

## 来源

- J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972)。
- B. Mazur, *Rational isogenies of prime degree*, Invent. Math. 44 (1978)。
- Yu. Bilu, P. Parent, *Serre's uniformity problem in the split Cartan case*, Ann. of Math. 173 (2011)；Yu. Bilu, P. Parent, M. Rebolledo, *Rational points on X₀⁺(p^r)*, Ann. Inst. Fourier 63 (2013)。
- J. Balakrishnan, N. Dogra, J. S. Müller, J. Tuitman, J. Vonk, *Explicit Chabauty–Kim for the split Cartan modular curve of level 13*, Ann. of Math. 189 (2019)。
- D. Zywina, *On the possible images of the mod ℓ representations associated to elliptic curves over Q*（arXiv 2015）；D. Zywina, *Explicit open images for elliptic curves over Q*（arXiv 2022）。
- S. Le Fourn, P. Lemos, *Residual Galois representations of elliptic curves with image contained in the normaliser of a nonsplit Cartan*, Algebra Number Theory 15 (2021)；P. Lemos, *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies*, Trans. AMS 371 (2019)。
- L. Furio, D. Lombardo, *Serre's uniformity question and proper subgroups of C_ns^+(p)*（arXiv 2023）。
- 非分裂 Cartan 模曲线的有理点：B. Baran 关于 $X_{\rm ns}^+(p)$ 的工作；P. Bruin, F. Najman 等的相关计算。

以上书目信息凭记忆列出，卷号年份以原文为准。

## 状态

进行中（serre-public-resume-20261114/2026-11-14）。主要目标尚未解决；见 HANDOFF.md 与 open.md。
