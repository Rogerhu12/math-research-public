# R75：局部正 weight 密度的唯一 IBP 分解及有限 word 改写

日期：2026-11-14。状态：已证明的限定代数结论。它不是实际 profile 函数的全部 word 独立性定理，也不支付曲面构造。用途是区分 P1 旧正规化遗漏的非局部关系与已经完整处理的局部关系。

## 1. 代数、次数与允许的边界

令

$$\mathcal A=\mathbb Q[x,q_0,q_1,q_2,\ldots],\qquad
D=\partial_x+\sum_{j\ge0}q_{j+1}\partial_{q_j}.$$

每个元素只含有限多个 jet。profile weight 是一个 monomial 中所有 $q_j$ 因子的总数。固定任意正 weight 分量；它在 $q$ 的零右 collar 上恒为零。

称 monomial 为余类型，当且仅当它满足以下之一：

1. 只含 $q_0$ 与 $x$；
2. 它的最高 jet $q_m$ 满足 $m\ge1$，且该因子出现至少两次。

这里的“余类”仅指局部密度模去全导数，不是把非局部原函数当成自由独立变量。

**零阶 jet 是明确的例外。** $q_0$、$xq_0$ 及任意 $x^p q_0^k$（$k\ge1$）都属于第一类，即使最高 jet 只出现一次也不作降阶；它们没有局部多项式原函数。下文降阶规则始终要求最高 jet 阶 $m\ge1$。word 的 letter 可以有 weight $1$，例如 $q_0$ 或 $xq_0$。

## 2. 准确局部分解

**命题。** 对任意正 profile weight 的 $f\in\mathcal A$，存在唯一分解

$$f=DB+R,\tag{1}$$

其中 $B$ 有同一正 profile weight，$R$ 是余类型 monomial 的有限线性组合。因此在共同零右 collar 下，

$$I(f)=B+I(R),\qquad I(f)(x)=\int_r^x f(t)\,dt.\tag{2}$$

**存在性。** 若某个 monomial 的最高 jet 是仅出现一次的 $q_m$，$m\ge1$，可写成

$$f_0=x^p q_m q_{m-1}^{\ell}\,G(q_0,\ldots,q_{m-2}).$$

取

$$B_0=\frac{x^p q_{m-1}^{\ell+1}G}{\ell+1}.$$

则 $DB_0$ 中含 $q_m$ 的项准确为 $f_0$，其余项的最高 jet 阶最多是 $m-1$。将 $f_0$ 替换为 $DB_0$ 减去这些余项，并按最高 jet 阶递降。每步保持 profile weight，严格降低待处理 monomial 的最高阶，故有限终止，得到 (1)。

**唯一性。** 若 $DB=R$ 且 $R$ 是余类型组合，取 $B$ 实际依赖的最高 jet $q_j$。于是

$$DB=q_{j+1}\partial_{q_j}B+\text{仅含 }q_0,\ldots,q_j\text{ 的项}.\tag{3}$$

$\partial_{q_j}B\ne0$，故 (3) 含线性的 $q_{j+1}$ 项；另一方面，$R$ 中凡含最高 jet $q_{j+1}$ 的 monomial，其幂至少为 $2$，也不可能有更高 jet。因此线性的系数必须为零，矛盾。若 $B$ 根本不依赖 $q_j$，它是纯 $x$ 多项式；正 profile weight 排除了这一情形。所以 $B=R=0$，证明唯一性。证毕。

此命题解释为什么继续添加“含重复最高 jet 的局部 IBP 猜测”不是首要方向：在这个明确的局部多项式代数中，旧 producer 的唯一最高 jet 规则已经能完整处理模全导数问题。真正新增的是让局部全导数击中任意非局部 word，以及让所有原语乘积遵守完整 shuffle。

## 3. 含 word 的递归为什么有限

对非空或空 word $w$，设待处理项是

$$I(f_0I_w).$$

使用上面的 $DB_0=f_0+r_0$ 和右锚乘积法则，

$$I(f_0I_w)=B_0I_w-I(r_0I_w)-I(B_0I_w').\tag{4}$$

式 (4) 的第二项保留相同 word 长度，但局部最高 jet 阶严格下降；第三项用

$$I_w'=m_1I_{\operatorname{tail}(w)}$$

使剩余 word 长度严格下降。所有步骤都不增加整项中已存在的最高 jet 阶。以“剩余 word 长度、局部最高 jet 阶”作字典序，就得到严格下降的递归尺度。

若局部前因子没有 profile 因子而是 $x^p$，在非空 word 上用

$$I(x^pI_w)=\frac{x^{p+1}I_w}{p+1}
-\frac{I(x^{p+1}m_1I_{\operatorname{tail}(w)})}{p+1}\tag{5}$$

也严格缩短 word。这里局部代数使用多项式的 $p\ge0$；一般有理系数或对数扩展不在本命题内。对空 word 的纯多项式原函数必须保留右端常数，不能用 (5) 丢掉它。

本 P1 应用的总 weight 不超过 $4$，正规化后的每个 letter 有正 weight，故 word 长度不超过 $4$。完整 shuffle 每次只是有限 interleaving 之和。因而数学上的这些指定改写有限终止；代码的项数、时间、缓存和 RSS 限制仍有作用，用于防止有限但过大的展开。保守循环 fallback 仅保留原表达式，不能授予新的零关系。

## 4. 尚未证明的事

局部命题不推出所有余下 word 在**任意一个真实函数 $q$** 上线性独立，也没有在本稿证明其作为所有 $q$ 的普适函数关系的完整基。额外非局部关系、特殊 profile 条件或不同真实桥控制仍可能降低实际函数 span。

因此新 word 检验若成功给出原始目标与响应的准确组合并核为零，这是一个可用正结论；若失败，仍只能报告指定改写层中的剩余结构。其精确列关系可以给真实普适函数 span 的维数上界，但代表秩本身不自动给维数下界，更不是构造目标的不可能性结果。


## 5. 与可执行层的对应

独立实现为 [全深度 word 层](../scripts/literature_pure_bulk_word_normal_form.py)，设计与人工检查范围见 [设计说明](../notes/literature-word-normal-form-design-20261114.md)。本证明不借用研究候选的数值评价；程序中局部降阶只在 `max(jets) >= 1` 且最高 jet 出现一次时执行。正 weight 的零阶 letter 被保留。完整 shuffle、精确右锚与原始括号回验分别承担其他准确恒等式，不能用本命题替代它们。
