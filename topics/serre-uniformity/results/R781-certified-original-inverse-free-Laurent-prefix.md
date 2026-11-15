# R781：原 p41 无逆 Laurent 前缀的公开准确计算

日期：2026-11-15。状态：**原 $R_0,\ldots,R_{142}$ 已由公开 Actions 准确生成并逐阶验证。**

本结果执行 [R781 的原切向下降和无逆递推](R781-original-tangent-descent-and-inverse-free-Laurent-relations.md)，仍使用原第 4 号、次数 1206 的映射、原 $b,\xi$ 和原 Hodge 微分。它完成后继原函数关系的一项真实输入；$A/B$、$\beta$ 和高度尚未由本次运行生成。

## 1. 已完成的准确对象

原 $L=\mathbb Q(\sqrt{-3},b)$，$v=\xi^{-10}u$，系数字段为
$$
M^+=L(\xi+\xi^{-1}),\qquad [M^+:\mathbb Q]=280.
$$
用 R774 的原 $H^3=\sum_{n\ge1}\kappa_n v^n$，$\kappa=\kappa_1\ne0$，
置 $v=\kappa w$，并保持
$$
\widetilde A_0=1,\qquad
\widetilde A_n=\kappa_{n+1}\kappa^{n-1}\ (n\ge1),\qquad
c_*=246^6b\kappa^4.
$$
公开核心实际产生 $R_0=1$ 和全部 $R_1,\ldots,R_{142}$，满足
$$
(R-wR')^3=\widetilde A(R^2-c_*w^2)^2\pmod {w^{143}}.
\tag{781C.1}
$$
每个系数为原 280 维整数基上的 primitive 整数向量乘准确有理尺度。原 $\xi^{10n}$ 相位逐项运输并检查实切向不变性；没有用平均替代原系数，也没有求代数元素 $\kappa^{-1}$。

对每个 $1\le n\le142$，暂取 $R_n=0$ 得到左减右残差 $\mathcal E_n$，再取
$$
R_n=\frac{\mathcal E_n}{3n+1}.
\tag{781C.2}
$$
核心在加入该系数后，准确检查 (781C.1) 的第 $n$ 项。已有低阶系数不变，故逐阶归纳证明完整前缀。它同时保存该阶所需的 $W,R^2,W^2,U,U^2,\widetilde A,\kappa^n$，其中 $W=R-wR'$、$U=R^2-c_*w^2$；后继无需重新递推。

R774 的原输入已完成至 820 阶，本次只读取原尺度阶段和前五个 32 阶块，以取得所需至 143 阶的 $H^3$。生产者 run/source、ZIP digest、manifest 和六个实际输入文件的 SHA 全部核对。原 Hodge 立方、R775 选基及 R777 准确短基均未在本次重算。

## 2. 公开运行和可复核来源

- 源提交：`f0292795817a534937d35904e2e11275631e878d`。
- 公开运行：[43679703344](https://github.com/Rogerhu12/math-research-public/actions/runs/43679703344)，attempt 1，2026-11-15 05:13:02 UTC 完成，结论 success。
- 核心：[scripts/R781_original_Laurent_prefix.py](../scripts/R781_original_Laurent_prefix.py)，SHA-256 `d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751`。
- 包装：[scripts/R781_public_Laurent_prefix.py](../scripts/R781_public_Laurent_prefix.py)，SHA-256 `7ddd32655169550c85e9a9210392e12d2cd58304c07c62f1620eaf9004aee674`。
- 请求：[notes/R781-public-Laurent-prefix-request.json](../notes/R781-public-Laurent-prefix-request.json)。参数为 $p=41$、Laurent 上界 142、Hodge 输入上界 143、预算 300 分钟；具体原模型和 R774 输入由请求逐项绑定。
- 原证明 SHA-256：`152c723da76b5c899b433db640fb6ac69082b46543f3d6bfa85d1cead7d78de0`；R778 短注入证明 SHA-256：`b23357b3fa74773c1ee45c1740b988ee9d7c96a658d5cdec99881947faf8c727`。
- 可重算的完整证书 SHA-256：`b9e1a2282d6fc0de12df401abbc3014ded525757c7102d11967f0bd33a40f3f0`。
- 144 个原实字段／逐阶输入文件的阶段清单 SHA-256：`5afc21e1c6ef36b7c27886c5d29dcbecd950c33e329f71f7c2e6b4c3a3ba8b82`。
- 完整输出名称／字节数／SHA 清单：[full-outputs-manifest.json](../computations/R781-original-p41-inverse-free-Laurent-prefix/43679703344-1/full-outputs-manifest.json)，SHA-256 `ce0554fab03fda8d124e9e0ee338335bca6f7b39ee8499550bbec36358a1a7fd`。
- 最后一阶 $R_{142}$ 及其递推状态的文件 SHA-256：`ee6174baac6e7d547cde91f09c0fd1799e6a154f2b4d8b20780c1002eeeaa2b0`。

[run receipt](../computations/R781-original-p41-inverse-free-Laurent-prefix/43679703344-1/run-receipt.json) 记录 exit 0、complete=true、原 source 和 core receipt SHA。
公开 job 132707441875 的最终 verification 步骤实际成功；它逐个核对完整阶段文件的大小和 SHA，并核对原字段维数、全部原切向相位、逐阶准确等式及三个尚未计算的接口标志。以上是该真实运行的结果，不是把请求中的预计秩或界当成输出。

按根 README 第 15 条，系数表、完整证书与原始日志不入 Git 或 Release。当前继续计算所需的临时 artifact 14148041703 仅作一日转交；ZIP SHA-256 为 `b5dc71fa2f675c75ca0b6999192ec1de6ffed7486b9506bfb529c37823f286dd`，名称为 `serre-global-R781-original-p41-inverse-free-Laurent-prefix-43679703344-1`。持久记录为上述脚本、原参数、run 和输出哈希；消费者用后删除临时副本。

## 3. 后继的原函数条件

由 R781 的严格推导，原 $A-yB=0$ 所需 143 条关系可直接使用本次系数：
$$
246^3\kappa^{n+2}A_n+
 \sum_{j=0}^{n+1}\kappa^j R_{n-j+1}B_j=0,
\qquad -1\le n\le141,
\tag{781C.3}
$$
其中 $A_{-1}=0$，保留 $M^+/L$ 的全部 20 个坐标。输入原 R777 的准确权十二基后，得到 2860 行、3028 个 $L$ 未知的关系。

本次未构造该矩阵，未计算其核，也未生成原 $y$、$\beta$、第二类周期、Poincaré 求值或高度 jet。对后继非零候选仍须准确代回 (781C.3) 的全部原项，使用 R778 的全局注入认证。固定层的这一输入完成，不改变 Serre 一致性主目标的 OPEN 状态。
