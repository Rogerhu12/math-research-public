# Phi：整个 H42 曲线的固定十二阶原标量交点输入

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。

## 1. 全原范围与两条已成来源

本输入针对当前 $\Phi=0,D\ne0$ 的整个权面中 $H_{42}=0$，不以其补图的十八列 determinant 反推该曲线。依赖两条已完成的全图原身份：

- [第一头原 D 六次必要式](../results/R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)给 $P_6D\in I_4$；整第一头已经排空，故该原表示覆盖当前整个 Phi 图。
- [全 Phi 的正则三来源六次式](../results/R150-appendix-unit211-Phi-zero-whole-original-NSPS-sixth-scalar-and-regular-three-source-extension.md)给 $C_6\in I_{10}$，包含原斜率判别式的整零支。

这里 $I_4\subset I_{10}$ 均在既有原权单位环中。不能把第一条写成未经 $D$ 局部化的 $P_6\in I_4$。

$P_6,C_6\in\mathbb Q[u,Q,\lambda]$ 的真实 $\lambda$ 次数均为六；$C_6$ 的最高系数除已付权因子后为 $H_{42}$。已刊
[三头互素及 798 例外权点](../results/R150-appendix-unit211-Phi-zero-whole-three-heads-coprimality-and-798-sixth-head-exceptional-weights.md)
支付 $H_{42}$ 在 QQ$[u,Q]$ 中不可约、总次数 42。本输入不重新因式分解。

## 2. 固定十二阶普遍多项式来源

定义固定尺寸 Sylvester 矩阵：前六列是 $\lambda^jP_6$，后六列是 $\lambda^jC_6$，$0\le j<6$；十二行是 $\lambda^0,\ldots,\lambda^{11}$ 的完整系数。令
$$
G(u,Q)=\det\operatorname{Syl}^{6,6}_\lambda(P_6,C_6).
\tag{1}
$$
矩阵条目属于 QQ$[u,Q]$；不需要展开巨大 QQ determinant。

固定矩阵的 adjugate 恒等式给多项式 $a,b$，满足
$$
G=aP_6+bC_6.
$$
因此
$$
\boxed{D G\in I_{10}.}
\tag{2}
$$
在当前原物理图 $D\ne0$ 上，全部原点都满足 $G=0$。这是整个 $H_{42}=0$ 曲线上的必要条件；包括 $P_6$ 六次头即 $H_{19}=0$ 的所有零纤维。没有为了 (1) 或 (2) 倒置任何六次头。

程序对这个固定十二阶矩阵的实际 QQ 条目总次数作最大权匹配，并逐项返回完整对偶；由此给出明确的 $d$，使 $\deg G\le d$。该上界不依赖模次数猜测。

## 3. 首个仅按原单位选择的 H42 点

固定 $p=1009$。先把 $H_{42}$ 作有理常数 Gauss 归一，使其系数 $p$ 整且至少一个系数为单位；同时逐项核 $P_6,C_6$ 的全部 QQ 系数 $p$ 整。

依预定顺序 $u=3,\ldots,32$，$Q=0,\ldots,1008$，寻找首个满足
$$
\overline H_{42}(u,Q)=0
$$
且全部原权单位及 $P_6$ 的六次头均非零的点。选点过程完全不读取 gcd、determinant 或原理想秩。

在唯一选中的点，程序计算两实际模 $\lambda$ 多项式的完整 Bézout 和固定十二阶 determinant。此时 $\deg\overline P_6=6$，$\deg\overline C_6\le5$，固定尺寸 (1) 仍是原 QQ determinant 的真实约化；它非零当且仅当二者互素。

如果该点返回非零 determinant，才继续下面的结论。若首个点不互素，准确保留整个 $H_{42}$，不按结果换点，不宣称本条已建立有限交。

## 4. 非零见证怎样排除 QQ 整曲线公因子

设固定原点确给 $\overline G\ne0$。若 $H_{42}\mid G$ 于 QQ$[u,Q]$，用已 Gauss 归一的 $H_{42}$ 写
$$
G=H_{42}^{\rm norm}J.
$$
多元 Gauss 赋值相乘相加；$G$ 的系数 $p$ 整，$H_{42}^{\rm norm}$ 的最小系数赋值为零，故 $J$ 的系数也 $p$ 整。约化后在选定 $H_{42}$ 点必有 $\overline G=0$，矛盾。因此
$$
H_{42}\nmid G.
$$
结合已付 QQ 不可约性，$\gcd_{\mathbb Q[u,Q]}(H_{42},G)=1$；特征零基域扩张不产生共同曲线成分。故整个 $H_{42}=0$ 原物理权支持是有限集，且不同复权点数至多
$$
42d.
\tag{3}
$$
本条不由一个模点宣称整个 Phi 空，也不把 $H_{42}$ 称为绝对不可约。只有 (1) 的真实 QQ 来源、$p$ 整性和不可约性共同给 (3)。

## 5. 冻结源及准确依赖

建议文件
2026-11-28-unit211-Phi-zero-whole-H42-fixed-twelve-original-scalar-intersection-8542.py。

源 9789 字节，SHA256
150c6d10552e97914de24d46da398371740963205022cebd92f80586aa917e94。

四件小源码依赖如下，沿用其当前 main 路径及已有环境变量：

1. 2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py，ISP_PHI_CENTERED_NSPS_SOURCE；只取 6125 字节必要定义前缀。
2. 2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py，ISP_PHI_I10_SOURCE。
3. 2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py，ISP_PHI_SLOPE_SOURCE。
4. 2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py，ISP_PHI_FIRST_HEAD_RULE_SOURCE。

另有一件历史输入仅在 Actions 终端临时恢复，不经工具传载荷、不重新入库：
2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json，
ISP_PHI_SAVED_P6_JSON；历史提交
3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9，
文件 SHA256
7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b。

源逐项核历史文件、原多项式参数身份和完整新系数输入。没有重算旧 P6 原 cofactor、旧三头因式、旧十八列点值秩或任何 norm。所有必要前缀受同一绝对 120 秒截止约束，固定 1 GiB；只输出小单位检查、固定矩阵次数对偶、Bézout/矩阵 SHA、点值与回执。