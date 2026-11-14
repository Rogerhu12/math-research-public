# 原尾 creation 角度的非微扰推广：既有反例的范围澄清

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_continue；AI-assisted，GPT-6 Astra Pro。

状态：**既有已证结果的推论与范围说明，不登记为新的主要结论。**

本文只澄清 [R271 短规范 Fock 旗](../results/R271-appendix-short-canonical-fock-flags-and-q-over-d-prefix-window.md)中使用的辅助 creation 像角度估计，不能无条件延伸为单独依赖 $\delta HP$ 的非微扰下界。这里不否定实际规范短旗的任何已证结论，也不否定其他形式的非微扰规范旗估计。

## 1. 原权上的明确障碍

取原权 $a_j=(j+1)^{-2}$，尾起点 $m=q$，并令
$$
S_q=\sum_{j\ge q}a_j^2,\qquad
\delta_q=\frac{(q+1)^{-4}}{S_q}.
$$
将 Boolean 层等距嵌入通常对称 Fock 空间，记 $Q$ 为无重复占据部分的正交投影，令 $B^*$ 是单位一粒子向量 $(a_j/\sqrt{S_q})_{j\ge q}$ 的 bosonic creation。于是对 Boolean $q$ 孔层中的 $f$，
$$
QB^*f=S_q^{-1/2}C_qf,
\qquad
\|B^*f\|^2=\|f\|^2+\|Bf\|^2\ge\|f\|^2.
\tag{1}
$$

[R239 规范纯尾 creation 指数奇异界](../results/R239-appendix-pure-tail-creation-exponential-singular-bounds.md) §3.2 已构造单位向量 $f_q$，满足
$$
\|C_qf_q\|\le\frac{2}{\sqrt6}q\sqrt{q+1}\,e^{-\gamma q},
\qquad
\gamma=\frac32+\frac12\log3-\frac52\log2>0.
$$
积分比较给 $S_q\ge[3(q+1)^3]^{-1}$。因此同一组明确向量满足
$$
\boxed{
\frac{\|QB^*f_q\|}{\|B^*f_q\|}
\le\sqrt2\,q(q+1)^2e^{-\gamma q}\longrightarrow0.}
\tag{2}
$$
与此同时 $q\delta_q\to3$；取 $H=1$、输出最高孔数 $P=q+1$，便有 $\delta_qHP\to3$。

因此不存在普适常数 $C$，使对全部原尾、全部 Boolean 输入和全部 $H,P$，都有
$$
\|Qy\|\ge e^{-C\delta_mHP}\|y\|,
\qquad y\in (B^*)^H\mathcal H_{P-H}^{\mathrm{Boolean}}.
\tag{3}
$$
事实上，任何只依赖 $\delta_mHP$、并在 $3$ 的某邻域有正下界的函数，都不能在 (3) 的右侧替代 $e^{-C\delta_mHP}$。

## 2. 对规范短旗的精确限制

(2) 所用输入是任意 Boolean 输入，未被声明为 primitive。它只排除短旗证明中一个辅助 creation 像角度估计的直接全参数推广。

尤其 $H=1$ 时，真正规范短旗就是出生在当前物理层的 primitive 空间：其规范映射为恒等映射 $V=I$，没有任何条件数退化。故 (2) **不是规范短旗的反例**。

已证明的 $4\delta_mHP<1/2$ 短旗估计完全不受影响。要越过该窗口，须利用规范短旗与其完整正交补之间的结构；不能把任意输入 creation 像的良好投影角度当作已知。
