# 新 Heegner 模性预印本的实际角色范围

日期：2026-11-26。**状态：已核原文的适用范围；下述原固定十三处角色排除已证明。** 没有将新预印本的主定理当作本课题已证输入。

## 1. 亲读的原文与结论类型

Tuoping Du, *Modularity of Heegner Cycles and Arithmetic Inner Products on Kuga–Sato Varieties*, [arXiv:2611.31153v1](https://arxiv.org/html/2611.31153v1)，2026-11-23 提交、文内日期 11-24。

本次逐核 §1.1–1.2、§2.7、§6.5、Corollary 1.6 及其证明、§9.5 和 Corollary 9.16。Theorems 1.1–1.2 讨论基本判别式的 genus-character 轨道和、Chow 值模性；Theorem 6.14 讨论相应 Hodge／各 $\ell$-adic AJ 像的模性及弱全纯关系的消失。后者没有断言 AJ 映射在非零 Chow 类上单射。Corollary 9.16 的非零结论由实高度检测 Chow 类，仍不是指定 ordinary AJ 非零。

尤其 §6.5 中的 $\ell$-adic 目标是随数域限制取直极限的全球 $H^1$。其中关于紧致到开放目标的 restriction 注入、及有限扩域上的 restriction 注入，不能改读为 ordinary 地方化注入。

## 2. 原 R814/R854 三份 cycle 不能直接由这些 genus 系数投出

这一区别可在原固定数据上直接证明，不依赖该预印本的模性或高度主定理。

[R814](../results/R814-common-fixed-good-pair-and-three-original-aj-squares.md) §§2–4 固定
\[
 \mathfrak l=(4+\omega)\mid13,\qquad
 \psi=\psi_{\rm b}\alpha,\qquad
 \chi_j=\chi_{{\rm b},j}\alpha^{-1},
 \qquad j=4,10,16.
\]
这里 $\alpha$ 是导子 $\mathfrak l^n$、$n\ge2$ 的非平凡 pro-$13$ 有限 ray 角色。$\chi_{{\rm b},j}$ 在十三处未分歧。因此在十三处的 wild inertia 上
\[
 \chi_j=\alpha^{-1};
\]
它对某个惯性元的值具有非平凡 $13$ 幂阶。这个结论对三份 $\chi_j$ 同时成立，不仅来自它们之间的三次角色比值。

Du §2.7, Proposition 2.9 的规范明确让 Galois 只作用于 cycle 因子、固定系数标量；其基本判别式 $\Delta$ 的规范化系数满足
\[
 \sigma Z_\Delta=\chi_\Delta(\sigma)Z_\Delta
\]
并下降到 $\mathbf Q(\sqrt\Delta)$。所以其在任一 pro-$13$ 惯性群上的作用为一。这个二次类型也可直接从 genus 轨道和读出：Galois 重排同一个完整轨道，权重是二次群角色，重排只乘该角色在相应 Artin 元上的值；系数标量不随 cycle 因子作用。这里不借用新文的 Chow 模性或高度非零定理。

取一个共同有限 Galois 域，包含实际 cycles、十三处角色及所用二次数域；取其十三处惯性像中的 $13$-Sylow 子群 $P$。可取 $\sigma\in P$ 使 $\alpha(\sigma)\ne1$。每个 quadratic 系数及它们的任意有限线性组合都被 $\sigma$ 固定。若 $\Phi$ 是一个定义于 $K$ 的实际代数对应，并保持 cycle-factor Galois 作用，则 $\Phi(Z_\Delta)$ 也被 $\sigma$ 固定。对任一原 $\chi_j$ 投影 $e_{\chi_j}$，
\[
 e_{\chi_j}\Phi(Z_\Delta)
 =e_{\chi_j}\sigma\Phi(Z_\Delta)
 =\chi_j(\sigma)e_{\chi_j}\Phi(Z_\Delta).
\]
特征零中 $1-\chi_j(\sigma)\ne0$，故
\[
 \boxed{e_{\chi_j}\Phi(Z_\Delta)=0.}
\]

因此，经 $K$ 上等变对应直接把该文的 quadratic genus 系数送到
[R854](../results/R854-original-canonical-cm-contraction-and-threefold-heegner-cycles.md)
的同一固定 $\chi_j$ cycle 因子，得到的是零。此处保留的是 R814 的真实十三处输入；不能先删除 $\alpha$ 再声称比较了同一 canonical cycle。若改用不在 $K$ 上定义的对应或另一个来源，必须实际构造并核算它的 Galois descent，本段不排除这种额外工作。

## 3. 换一个 Heegner 来源也没有自动关闭本题

可另取 weight4 形式 $\theta_{\lambda_j}$ 及不同的 CM 字段来研究 genus-character Heegner cycles；那是新的来源，不是第2节被排除的直接投影。但要回到本题仍须证明该新 cycle 与原 $Z_{02,j}$ 或 R814 固定 cycle 的实际对应，并证明指定全球 AJ 及 ordinary 局部化的非零。有限维 Chow 系数空间本身不保证其每个 $\ell$-adic realization 的像非零。

本文没有声称该预印本错误，也没有核完其所有主定理的证明。按本课题 README，若将其尚未被公认的新结果作为正面输入，仍须在本仓库给出完整证明。上述角色排除只使用本库已证 R814/R854 和该文 §2.7 实际定义的二次 Galois 类型。

本文没有数学程序执行或数值证书。
