# 原临界核：闭模映射的平方零结构与谱二择

日期：2026-11-12（UTC）。子任务：critical_kernel。

完整推导已整理为 [R58](../results/R58-critical-kernel-square-zero-module-maps.md)。

## 本次闭合的逻辑链

固定任意循环参考向量 $h$ 和假设的 $f\in K=\ker D$，取核心映射
$$
p(A)h\longmapsto p(A)f
$$
的闭包 $X$。R34 的可闭性和定义域不变性给
$$
\operatorname{Ran}X\subset K,\qquad
D\operatorname{Dom}X\subset\operatorname{Dom}X,\qquad
XD=DX=0\quad\text{在 }\operatorname{Dom}X\text{ 上}.
$$
闭性与定义域稠密性于是给
$$
\overline{\operatorname{Ran}D}\subseteq\ker X.
$$
R53 的 $K\subseteq\overline{\operatorname{Ran}D}$ 恰好将两边接上：
$$
\operatorname{Ran}X\subset K\subseteq\overline{\operatorname{Ran}D}
\subseteq\ker X.
$$
因此**原始闭包本身**满足 $X(\operatorname{Dom}X)\subset\operatorname{Dom}X$，且 $X^2u=0$ 对所有定义域内 $u$ 成立。

对 $\lambda\ne0$，
$$
\operatorname{Ran}(\lambda I-X)=\operatorname{Dom}X,\qquad
(\lambda I-X)^{-1}v=\lambda^{-1}v+\lambda^{-2}Xv.
$$
于是 $f\ne0$ 时，若 $X$ 全域则有界、谱为 $\{0\}$，且它是 UHF 之外的非零有界交换平方零元；若 $X$ 非全域，则它无界、预解集为空、谱是整个复平面。定义域必须保留，不能把非全域平方零写成一个全域有界零算子恒等式。

由同样的代数逆，
$$
\operatorname{Ran}(I+cX)=\operatorname{Dom}X
$$
稠密。图核心的像闭包恰为 $[h+cf]_A$，故
$$
\operatorname{Cyc}(A)+K=\operatorname{Cyc}(A).
$$

## 放弃的不必要延伸

最初考虑将 $X$ 通过 $P_{CM}$ 因子化并扩大定义域，其中 $M=[f]_A$。可以构造从 $CM$ 到 $M$ 的闭交织映射，但这会引入额外的定义域最大性问题。随后发现直接对 $D\operatorname{Dom}X$ 取闭包，就已经使 $K$ 包含在原始 $X$ 的核内；因此无需扩大定义域，R58 完全不依赖那个辅助构造。

## 仍然存在的两个分支

目前没有证明完整交换子不含非零平方零元；R32 无零因子仅覆盖 $\mathcal A$，R38 仅把 UHF 内部交换子识别为 $\mathcal A$。也没有证明这里的闭模映射具有非空预解集；R39 已说明一般闭模映射的谱行为不能按有界直觉猜测。

故 R58 是条件结构约束，不是非零核构造或无核证明。后续要么排除完整交换子中的平方零分支，要么利用真实进位估计排除无界全谱分支；仅重复闭性或循环性不足。

