# Phi 全第一头图：两条真实权支持的精确相交输入

日期：2026-11-28（Asia/Taipei）  
状态：新输入，尚未执行。资源上限：120 秒、1 GiB；包含所有必要构造前缀。

## 1. 原范围与两个已成模型

范围是当前一般 unit211 的 $\Phi=0$、物理 $D\ne0$ 原图。整第一二次头零支已经由
[R150 整 H1 排除](../results/R150-appendix-unit211-Phi-zero-whole-H1-complete-original-exclusion.md)
关闭，因此三个原均值的完整规则在当前范围给出 $1,T,z$ 三生成元。

已成的[原六次必要式](../results/R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)
给出 $P_6(u,Q,\lambda)=0$。其真实 $\lambda^6$ 首项除已付权因子后是 $H_{19,11}(u,Q)$，双次数 $(19,11)$，137 项；其完整 QQ 不可约性已有原记录。本源只从已保存的原 $P_6$ 提取该首项，不重算原 cofactor 或不可约性。

已成的[完整最高项原 NV/F6 提升](../results/R150-appendix-unit211-Phi-zero-whole-first-head-highest-original-NV-F6-filtered-lift-and-twenty-one-generators.md)
给出真实原关系
$$
C\lambda^7=a_0+a_1T+a_2z,\qquad
\deg_\lambda(a_0,a_1,a_2)\le(6,5,5).
$$
完整原乘法规则把此关系提升为首项 $C^3\lambda^{21}$ 的原行列式关系。在 $C\ne0$ 上，直接按加权次数递降给出 21 个生成元。这个结论既不要求原三生成元自由，也没有声称 $C=0$ 是所有原点必须满足的条件。

## 2. 真正新增的目标

记 $\widehat r_{\rm NV},\widehat r_{F6},\widehat r_{N1}$ 为上述原式的三个已定义最高行，组成 $3\times3$ 矩阵 $A$。新源只读必要构造到这些行，随后用
$$
\alpha=e_0\operatorname{adj}(A)/\det A
$$
直接定义同一唯一常数目标；这不是重放旧五行 Gaussian。取三个约分后 $\alpha_i$ 的权分母最小公倍式 $C$，精确乘回。旧已成身份的 $C$ 和 $C_*$ 的哈希仅用于识别必要输入。

随后只算真正新增的
$$
G=\gcd_{\mathbb Q[u,Q]}(C_*,H_{19,11}),
$$
并把两个完整 QQ 整除都乘回。这里 $C_*$ 只剥已经关闭的原权单位。新源另允许剥 $2\ell-3$：它仅在本 $\Phi=0,D\ne0$ 范围由
[完整例外有序权图及 B/C 交换](../results/R150-appendix-unit211-Phi-zero-exceptional-weight-chart-complete-original-exclusion.md)
支付，绝不把它推广到一般 LS。$u+Q-1$ 的单位依据则是
[整个一般 Q=1-u 原排除](../results/R150-appendix-unit211-Q1minusU-complete-original-exclusion.md)，并非 H1 内部结论。

若 $G=1$，两条复仿射曲线没有共同分量；全部共同零点有限，按平面 Bézout 至多
$$
\deg_{\rm tot}(C_*)\deg_{\rm tot}(H_{19,11})
$$
个不同权点，包括任何投影首项退化和无穷点所可能消耗的交数。若 $G$ 非常数，则整个共同曲线保留，不声称这个界。

无论输出如何，在共同零集以外：$H_{19,11}\ne0$ 图可用原首一 $\lambda^6$ 和三生成元，给每个固定权的环境至多 18 个生成元；$C_*\ne0$ 图可用新的 21 生成元结论。两模型在共同零集上均不被偷用。有限例外权集不是整个原权集有限，更不是原图排空。

## 3. 执行身份与依赖

新源建议文件名：

`2026-11-28-unit211-Phi-zero-whole-highest-support-and-P6-head-exact-intersection-8542.py`

新源 blob `47aaafc94caf3880e330c2570fb2b8d8e8f76616`，7698 字节，SHA256

`a8d3f03e401a7a7c356da40e1f353ab5d3e879b9455a09a2f73d526c7df1af47`。

三个依赖按完整 basename 同目录暂存：

1. `2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.py`，SHA256 `4cebc8a6e7e16c58e9dff2bc055acd2bc9e262132bc08d7d9dfa2bff0ca3cd41`。只读旧 Gaussian 之前的 9094 字节，前缀 SHA256 `9bde53d859752f8ca1a873917ab9c5d633c9adeffd8ca256240c5a97964b2f7a`。
2. `2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，SHA256 `100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf`。上项内部只读 7097 字节必要规则，停在旧 D cofactor 之前。
3. 历史原参数 `2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json`，SHA256 `7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b`。由历史 loader 仅在 Actions 临时阶段取得；不经连接器传载荷，不再存入主线。实际读取键为 `polynomial`，原解包 SHA256 `9e50cc2a30cf8500b7bef25f8e579334c2b46f8d896662759cdc0ec85f35542c`，86039 字节。

支持环境覆盖名 `ISP_PHI_HIGHEST_SOURCE`、`ISP_PHI_FIRST_HEAD_RULE_SOURCE`、`ISP_PHI_SAVED_P6_JSON`；默认同目录 basename。嵌套前缀的 `alarm` 与 `setitimer` 均受本次唯一绝对截止钳制，不能延长 120 秒。

输出仅有定义身份、次数、项数、SHA、完整乘回标记及准确的相交范围。不输出或保存可重算系数、编码、分片。这里没有任何新的大投影、旧 cofactor、旧范数、旧行模块或旧 Gaussian 审计门。
