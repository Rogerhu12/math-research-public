# Actual40：完整 QR 逆解原件与原算子读回

本条记录公开仓库 Actions run `43621054216`、job `132526640205` 的已完成结果；artifact `14123843853`，大小 `389895464` 字节。运行入口为 `geometry_20261114_twelve_query_qr_projection_warm.py`，SHA-256 为 `4b768828f754f75d760980d596f198984e92f5ceac79832123c74e42985a5c67`。这里专核 QR 因子身份、17 次逆解、原完整算子读回及对应数组。全角约束、C/H 候选选择、实际回溯和 FD 结论另见本次主记录；不把两类结论混为一个接受判据。

## 1. 实际模型与唯一线性化

`block-qr-live-model-binding.json` 与所有逆解报告绑定同一个 live `CompleteLinearization`。原完整 $A$ 为 `236036 × 236036`，完整 $B$ 为 `24576 × 236036`，阻尼为 `270`，B 模型 SHA 为 `18a5ad26655ec12a2c19eb0887a1895ee2bfeadf84f6fac9695f83d2a9f7977b`。本次与 actual39 的 C 基线使用相同的 actual37 父暖场和固定模型；本条没有把 actual39 新暖场当作父场。

实际父暖场 SHA 为 `dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8`，独立父 status SHA 为 `37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0`。入口、七项冻结依赖的当前完整文件 SHA 均与运行记录一致；所有17次报告的完整 input identity、原 `L/R/P/BY/BC/BP/inlet/S/Wr` 摘要逐项相同。实际账目是一次 `CompleteLinearization`、两次原 operator 构造、一次 QR factorization、零次旧 PCG 调用。

完整 H 候选保留全部236036个自由度。固定支持 `471–482` 与全局 p 只限定原 C 投影，未截掉 H 候选中的 node470、core 或其他坐标。因子没有额外使用 C 作列变换，即本次 `QR_column_preconditioner=none`。

## 2. 一次完整平方根因子化

本次因子来自冻结 `exact_20261114_regularized_block_qr.py`，SHA 为 `596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722`。报告的矩形系统维数为 `472072 × 236036`；698个物理块各338维，global border 为109个 free-core 加3个控制，共112维。全部物理阻尼行各加一次、global 阻尼行加一次，pure-global 残行完整累计；完整代数对应 [R268](../results/R268-complete-regularized-chain-border-QR.md)。

| 已保存的量 | 本次实际值 |
|---|---:|
| 完成物理块数 | 698 |
| 因子数组总字节 | 1,486,451,296 |
| factorization_seconds | 19.128500218 |
| maximum_RSS_kib | 3,337,860 |
| factor 超时标记 | false |
| 因子存储 | memory-only |

四个因子数组（diagonal、next-physical、global-border、global-diagonal）的 shape、字节数、原始 SHA 在所有17份逆解报告中相同；factor 在关闭前为 `factorized`。**本次未导出这四个大数组，其 `file` 均为 null，所以这里不声称独立核过因子的原始字节。** 同理，完整 L/R/P 等输入在本条仅核保存的来源和逐次哈希一致性；不把记录的哈希误称为重新导出后的原件审计。

## 3. 17 次逆解均读回原完整 H

以下数值直接取自本次 Actions 的 `block-qr-inverse-000.json` 至 `-016.json`。这里没有在本地重新执行任何点积、范数、矩阵作用或求解。$r=Hz-d$ 的范数使用原完整 $A/A^T$ 和阻尼读回；另存的 factor-normal residual 没有替代它。

| 次序 | 右端 | 原 $\lVert r\rVert_2$ | 原相对残差 |
|---:|---|---:|---:|
| 1 | complete-H center | 6.355194653366658e−10 | 6.290514339105675e−16 |
| 2 | B row 14336 | 1.6490300285652493e−10 | 4.831956917280009e−16 |
| 3 | B row 15349 | 1.169493035694256e−10 | 4.622292291469295e−16 |
| 4 | B row 4096 | 2.799071094129894e−10 | 5.82319451083956e−16 |
| 5 | B row 2048 | 2.8748894127588876e−10 | 5.296127775795332e−16 |
| 6 | B row 14358 | 1.325476239533693e−10 | 5.424825351004608e−16 |
| 7 | B row 18432 | 3.2591247640439027e−10 | 6.078312203200706e−16 |
| 8 | B row 19434 | 1.8313141284847982e−10 | 6.888219887686503e−16 |
| 9 | B row 4118 | 1.7801215253877418e−10 | 6.753966396974803e−16 |
| 10 | B row 14379 | 1.5132700620463668e−10 | 5.463187186487809e−16 |
| 11 | B row 10240 | 1.7865446572009809e−10 | 7.141860016873343e−16 |
| 12 | B row 0 | 3.5533993113497657e−10 | 5.7501918842003e−16 |
| 13 | B row 16384 | 2.2417060590755234e−10 | 6.004618148797604e−16 |
| 14 | B row 8192 | 1.5794167086886164e−10 | 7.11540738009969e−16 |
| 15 | B row 12288 | 1.1335788505980806e−10 | 4.886806893672718e−16 |
| 16 | B row 10262 | 8.856448815086289e−11 | 6.501278408851147e−16 |
| 17 | B row 15306 | 1.1418615509850889e−10 | 4.58100212305514e−16 |

首右端范数为 `1010282.1980483998`，首原残差无穷范数为 `3.4924596548080444e−10`。全部17次报告的原残差通过原 `1e−8` 相对诊断；这属于求逆读回，不是新增的科学接受门。各次三角解约0.233–0.247秒，完整调用含输入重新哈希和两套读回约1.700–1.750秒；首入口另含因子化，槽位总耗时 `22.028170842999998` 秒。全部调用没有跨越所记录的 deadline。

每次在同一实际返回向量上，supplied A 与冻结 reconstructed A 的作用差、以及在同一 A*x 上两者转置作用差，其已保存 L2/Linf 均为0。这是本次17个实际向量上的一致性，不能提升为任意黑盒算子恒等的形式证明。首 factor-H 与原 H 的作用差 L2 为 `6.097761735269027e−10`；两个误差报告被分别保留，未混用。

## 4. 所有保存的逆解数组逐字核对

`block-qr-inverse-array-manifest.json` 的68个文件等于17次各自的 rhs、candidate、original-complete-H-residual、factor-normal-residual。每个实际数组是 `shape=(236036,)`、`dtype=<f8`、C-order，raw 字节 `1888288`。本条用纯标准库流式读取，核对以下全部项目：

- 68个压缩文件各自的字节数、SHA、唯一 `actual.npy` 成员和完整 NPY header；总压缩64,783,718字节，总 raw128,403,584字节。
- manifest 的 `shape + NUL + dtype + NUL + raw` identity，与 report 内另一种 raw-only SHA，均从同一原始 payload 核对，不重新解释或转换浮点值。
- 17份 readback 文件的完整 SHA；accounting call、独立报告、factor.solve_reports 三处逐字对应。
- 全部引用完整覆盖68个实际数组，调用次序、完整 slice、候选/原残差 identity 与所有 source bindings 一致。

全部通过。完整68文件摘要、17份原报告标量、来源身份与审计范围保存在 [同名 JSON](2026-11-14-actual40-complete-QR-inverse-byte-audit.json)，SHA 为 `fda2236d8bf5a9735c3f9f4388f085c2aef9cb40f9571ae21d41998af21a70ff`。该 JSON 是本地纯字节审计记录，明确标 `scientific_calculations_performed=false`；数学数值全部来自本次实际 Actions。

三个关键原报告的 SHA 分别为：

| 原件 | SHA-256 |
|---|---|
| block-qr-inverse-accounting.json | a079d996b7d3c8ed19e712d7c21ee1798e3280941834f1549ce01b13be263b45 |
| block-qr-live-model-binding.json | 90de5e4d8e369b436bb653ab7f72e0d41b4b0601f1507859212c6f00b9bbf6a6 |
| block-qr-inverse-array-manifest.json | ebf3f6695745aeeff0fcaad0d95707b32999ef6d0e34ed14fb71d68908873fa4 |

## 5. 费用与结论范围

helper 的原完整作用账为 `A=116, AT=57, B=101, BT=54, H=17`，另作冻结 reference 的 A/AT 各17次；合计该范围内原 A133次、AT74次。此账**仅包含 fixed-H helper 及其额外 reference 读回**，不包含 raw LSMR、原 C 投影、外层 selector 与前置实现核验。一次 factor 与 R 三角解作为独立工作记录，没有冒充1200个 H-product 预算内的相同成本。

本次证据支持：保持原全部变量、原权重及原阻尼，完整平方根 QR 实际提供了17个原算子残差很小的逆作用，actual30 的内层 PCG 截停问题不再出现在这批逆作用上。该结论不包括整个不等式 QP 最优性，也不包括新的 full-DN 接受。有限工作集之外仍有实际约束违反，必须采用已保留的全行核验、修复、原同 f 比较及真实非线性回溯；其结果见主记录。固定 g 的完整候选、闭曲面与全部完成标准仍按原 README 推进，不新增六 jet 机器精度门。
