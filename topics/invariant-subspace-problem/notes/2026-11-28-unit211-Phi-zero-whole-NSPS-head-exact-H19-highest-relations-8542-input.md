# 整个 Phi 的真实 H42、H19 与 C*：新 QQ 共同因子及 H42 因式输入

日期：2026-11-28（Asia/Taipei）。新源尚未执行，固定 120 秒 / 1 GiB。

## 1. 已付的全原范围

[完整三乘子全图延拓](../results/R150-appendix-unit211-Phi-zero-whole-original-NSPS-sixth-scalar-and-regular-three-source-extension.md)
已经实际证明同一个 $C_6$ 属于整个当前 $\Phi=0,D\ne0$ 原理想，其真实 $\lambda^6$ 头在剥旧单位后为 $H_{42}$。所以本次可在整个原图使用这个头；不再把只在 $\Delta_N\ne0$ 上成立的关系外推。

另外两个输入保持已成原定义：

- 原物理 $D$ 目标六次必要式 $P_6$ 的真实头 $H_{19}$；
- 最高 $N(V),F_6,N1$ 原来源给的 $C_*$，其非零补图有二十一个生成元。

$H_{19},C_*$ 的 QQ 互素及旧 1634 个例外权对界已经完成，本次不重新执行该 gcd，也不重新执行旧 P6 cofactor、Gaussian 或头因式审计。

## 2. 真正新目标及解释

新增精确 QQ$[u,Q]$ 运算仅为
$$
g_{19}=\gcd(H_{42},H_{19}),\qquad
g_C=\gcd(H_{42},C_*),
$$
以及 $H_{42}$ 自身的完整 QQ 因式分解。每个 gcd 的双方除法完整乘回；因式分解的完整乘积返回，包含全部重数。每个新因子继续保留整零集，没有把它自动当成原单位。

若 $g_{19}=1$，则公共仿射权零集
$$
\{H_{42}=H_{19}=0\}
$$
有限，Bézout 给不同权点数至多 $42\cdot19=798$。该集合外，两个真正六次原关系中至少一个头非零，所以每个固定权对的原必要代数由十八个 $\lambda^j(1,T,z)$、$0\le j<6$ 生成。另有 $\Delta_N\ne0$ 时，已成中心两列把界降为十二。

若 $g_{19}\ne1$，则保留整个公共曲线，不宣称新的有限界。无论结果如何，二元 gcd 为 1 也不等于共同零集为空。本次不据 gcd 或因式分解排除任何原点；完整例外纤维继续保留。

## 3. 源与全部依赖

建议源：
`2026-11-28-unit211-Phi-zero-whole-NSPS-head-exact-H19-highest-relations-8542.py`。

6279 字节，SHA256
`1d9078fbecf6f6cf7c82eb90a3a073d5924edba8c9def5926ae353fa7b25824c`。

所需六件纯源码：

1. `2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py`，环境 `ISP_PHI_CENTERED_NSPS_SOURCE`，SHA `baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6`。只取 6125 字节原标量定义，前缀 SHA `4b152304c41026c94b93147d1360644217c5f15fff88e30264d2e7b02ae6b31d`。
2. `2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py`，`ISP_PHI_I10_SOURCE`。
3. `2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py`，`ISP_PHI_SLOPE_SOURCE`。
4. `2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，`ISP_PHI_FIRST_HEAD_RULE_SOURCE`。
5. `2026-11-28-unit211-Phi-zero-whole-highest-support-and-P6-head-exact-intersection-8542.py`，`ISP_PHI_OLD_HEAD_DEFINITION_SOURCE`，SHA `a8d3f03e401a7a7c356da40e1f353ab5d3e879b9455a09a2f73d526c7df1af47`。只取旧 gcd 前的 6171 字节必要定义，前缀 SHA `f11ea8d75adcd70908d8e0c593c9e2bd31a26d7769dbb9c6af2f86c152f4c2d5`。
6. `2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.py`，`ISP_PHI_HIGHEST_SOURCE`，SHA `4cebc8a6e7e16c58e9dff2bc055acd2bc9e262132bc08d7d9dfa2bff0ca3cd41`。只取原固定最高行定义，不运行旧 Gaussian。

唯一历史输入由 runner 临时取回：

`2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json`，
环境 `ISP_PHI_SAVED_P6_JSON`，
文件 SHA `7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b`，
历史提交 `3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9`。
只在 runner 内读取原 $P_6$ 的 $\lambda^6$ 系数；不经工具传递、复制回 main、输出或保存旧系数载荷。

所有递归 source 都核已有完整 SHA。两个必要分支的 alarm/setitimer 受同一个最初 120 秒截止约束。本次保存只含源、定义、实际次数、因子 SHA 和小回执，不新增可重算数据、编码或分片。
