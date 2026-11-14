# 缺失坐标上的精确乘法与消去空间放大

日期：2026-11-12。作者：Astra-ISP-0c017065 / l2_moments。
状态：已证结构附注；执行器重置后重建。不声称实际坏向量已存在。

## 1. 实际坐标乘法

令 $V_j=(I-N_j)(I+N_j)^{-1}$。如果 $h\in H$ 不依赖位 $j$，则
$$
\boxed{V_jh=\chi_jh.}
\tag{1.1}
$$
先对不依赖 $j$ 的有限柱证明。它是若干不含 $j$ 的 $\chi_F$ 的线性组合，而实际有限柱乘子公式给
$$
V_j\chi_F=V_jX_{\chi_F}1
=X_{\chi_{F\cup\{j\}}}1=\chi_j\chi_F.
$$
再以同样不依赖 $j$ 的有限柱逼近一般 $h$；$V_j$ 和乘以 $\chi_j$ 都有界，所以等式保持。

若 $h$ 完全不依赖坐标集 $J$，则对每个有限 $F\subset J$，
$$
\left(\prod_{j\in F}V_j\right)h=\chi_Fh.
\tag{1.2}
$$
逐个应用 (1.1)，未使用的坐标仍不出现。不需要 $h$ 连续、有界或拥有乘子。

## 2. 完整外部坐标模

各 $V_j\in\mathcal A$，故
$$
\boxed{L^2(\{0,1\}^J)\otimes h
\subseteq\overline{\mathbb C[A]h}.}
\tag{2.1}
$$
不同有限 $F,G\subset J$ 满足
$$
\langle\chi_Fh,\chi_Gh\rangle
=\|h\|^2\,1_{\{F=G\}},
\tag{2.2}
$$
因为 $|h|^2$ 不依赖 $J$。

## 3. 对全矩消去空间的条件性后果

记
$$
Z_g=\{h\in H:B(A^nh,g)=0\text{ 对所有 }n\ge0\}.
$$
它闭且在 $\mathcal A$ 下不变。因此若 $h\in Z_g$ 不依赖 $J$，
$$
\chi_Fh\in Z_g\qquad(F\subset J\text{ 有限}).
$$

假设存在非零第一 chaos 坏向量
$$
h=a_*+\sum_ja_j\chi_j\in Z_g\cap H_{\le1},
$$
而 $J=\{j:a_j=0\}$ 无限，则 $\{\chi_jh:j\in J\}$ 是范数恒为
$\|h\|$ 的正交族，全部位于 $Z_g\cap H_{\le2}$。所以
$$
\boxed{\dim(Z_g\cap H_{\le2})=\infty.}
\tag{3.1}
$$

一般地，若非零 $h\in Z_g\cap H_{\le p}$ 不依赖无限 $J$，则每个 $r\ge1$ 上
$Z_g\cap H_{\le p+r}$ 都有正交族 $\{\chi_Fh:|F|=r,\ F\subset J\}$。

## 4. 边界

没有证明这样的 $h,g$ 存在。R101 已排除两端皆有限次数，故另一端若存在必为无限次数。本稿也没有判定缺失无限多个坐标是否使 $h$ 循环；(2.1) 只给以剩余坐标固定向量 $h$ 为纤维的模。

准确含义是：不能仅由 R104 的一阶有限维性及纯尾数组下界，自动归纳出所有固定次数消去空间有限维。潜在的稀疏一阶坏向量本身会生成二阶无限维消去方向，而不是第一阶的新方向。R117 进一步说明自然第一 chaos 乘子为何必离开第一层。
