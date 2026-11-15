# R807：原 M6 共同清极因子与四个普通 V4 坐标的实际认证

日期：2026-11-15。状态：**本篇所列清极因子、残余秩和四个准确坐标已经由本公开仓库 Actions 实际算出并完整核验。** 原六个 θU_j 的正规坐标、函数极理想、η 与高度并未由这次计算完成。

数学依据为 [R805 两图/一次清极证明](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md) §7；执行规范为 [R807 原清极契约](../notes/R807-original-M6-pole-clearing-execution-contract.md)。已成的 [R805 铅笔/整基](R805-certified-original-affine-pencil-free-basis.md) 和 [R803 混合 Hodge 坐标](R803-certified-original-M6-mixed-Hodge-ratios.md) 保持原来源与尺度。

## 1. 原任务及真实结果

原普通 V4 基维数为962，整数尺度为82^8；取原 q_Y 的0至54阶，每阶20个实圆分坐标，共1100行。所用原 V4 矩阵的实际非零 minor 为

| 项目 | 实际值 |
|---|---:|
| 素数 | 1000000007 |
| 行数/列秩 | 962 |
| determinant mod prime | 290159643 |
| 五投影的138×5残余矩阵秩 | 2 |
| 完整残余核维数 | 3 |
| 新准确有理右端数 | 8 |
| 数学核心耗时（秒） | 375.01951452900005 |

没有预设残余秩为4。令 e_i=82²T_{1,i} 为原整数尺度 M2 行，本次按冻结核规范得到

$$
\theta=e_0-\frac{112648621}{282292255}e_1
+\frac{223442698}{282292255}e_2.
$$

其五个系数准确为
$$
(1,-112648621/282292255,223442698/282292255,0,0).
$$
第一非零原 M2 索引是0，系数规范为1；原146条基中其余系数为零。原五条 e_i 线性独立，故这个实际向量非零。四条原 M6 补行乘 θ 的坐标在同一个原962维 V4 基中已全部算出；其尺度字段均为 `2044140858654976`，没有另换普通基或删去原尺度。

## 2. 五个投影与四个成员必须分别解释

先对五个 E6·e_i 在同一962选行块作准确投影。这五个方程各自仅在所选行上成立，不能单独声称五个 E6·e_i 属于 V4。核心随后在剩余138行构成真实残余矩阵，计算其全部核，才选择上面的 θ。

| 实际右端 | Dixon 位数 | 准确回代范围 |
|---|---:|---|
| E6·e0 | 488 | 962选行；不是单独成员结论 |
| E6·e1 | 488 | 962选行；不是单独成员结论 |
| E6·e2 | 488 | 962选行；不是单独成员结论 |
| E6·e3 | 488 | 962选行；不是单独成员结论 |
| E6·e4 | 488 | 962选行；不是单独成员结论 |
| θ·F690 | 336 | 全部1100行 |
| θ·F691 | 464 | 全部1100行 |
| θ·F693 | 472 | 全部1100行 |

F692=(82^6)E6。它乘 θ 的准确坐标由已成五投影按真实核系数合成，随后在全部1100行验证；没有解第九个右端。其余三条 F690、F691、F693 各用同一已认证 minor 求解，并在全部1100行准确代回。

这四条原 M6 补行依次是原82尺度的 E4T_{1,0}、E4T_{1,73}、E6、η^12。后者保持原 q_Y^41 首项和原 ξ 相位。这里的准确 membership 由 R805 的零点次数界保证为全局恒等式：待比较对象位于4H+2E，次数1092，而20个 cusp 的55阶给1100个零阶。E6 的两处准确二阶主部继而给

$$
0\ne\theta\in H^0(H-2E).
$$

原 M6 前690行是普通 V3，乘 θ 属于 V4；配合这四条实际补行，全部694维原 M6 共同清极的接口成立。因而已成原 U_j 满足 θU_j∈V4，但这不表示 θU_j 的六组具体正规坐标已经在本次输出中计算。

## 3. 没有重算的输入与本次实际尾段

三组源绑定输入共997项：R775为7项、R786为982项、R805为8项。原 R805 已成的 e3·e73 和 e4·e73 的0至40阶作为必需来源核过。由于本次实际 λ3=λ4=0，两个依赖均无新增41至54阶；输出的 `actual_new_pair_tail_stages` 是空列表。后继不能把理论上可能需要的尾段登记成已经算出的数据，也不能要求不存在的 stage。

所有原 M2、V2、V4 前缀及 R805 已成乘积均未重算。原 ξ 的40维表示、实20维坐标、原 q_Y/v 相位和整数尺度均由冻结源及完整验证保持。没有调用旧已过期的 Release 存放 raw。

## 4. 实际 producer 与独立纯 IO 审读

数学 producer：

- [公开 run 43707939269](https://github.com/Rogerhu12/math-research-public/actions/runs/43707939269)，source `2c44d02595d57c22b5ea2c10defa93f63252061d`。
- core `scripts/R807_original_M6_pole_clearing.py`，SHA256 `d92cf79bb3a30fe8e28709a4e2eaa706a724e195c8d8393e7649466a79cec018`。
- wrapper `scripts/R807_public_original_M6_pole_clearing.py`，SHA256 `d499a33bd6e471c621753b06d2fc1f7868ed6e8b7700fbed4ff9d4807e595ae7`。
- 冻结请求 `notes/R807-public-original-M6-pole-clearing-request.json`，SHA256 `d82e5c7fe029b8ddceda8f309f1af927e43cfbf4cd974e616115f48c383cc6b2`。
- 原 artifact 14159481627，60,771,931 bytes，ZIP SHA256 `74c801509f554024d0246bf62227e38c30f4e84a14d4e0af8fa917350f875a56`；到期2026-11-16 11:20:47 UTC。

完整纯 IO 审读：[run43709814489](https://github.com/Rogerhu12/math-research-public/actions/runs/43709814489)，source `c8d76ff9c19e248f9a2809bbef1ff06fc3b5d0ac`，job132798714655。原 ZIP 的1005个文件、1003个完整 manifest 项、995个数学 stage、全部997个原输入逐 size/SHA 核对。保留输入包的34,167,815 bytes也核其实际 SHA；原冻结 wrapper.verify 原样执行并返回0，未 import 数学 core 或 flint，未重算任何数学。

审读脚本 `scripts/R807_public_success_io_audit.py` 的 SHA256 为 `b066ceaeadf9a06110857835f13a8b2af4c71208553710126cef71b10b3cec5c`。小摘要 `R807-success-IO-review-summary.json`，18070 bytes，SHA256 `c0e6ecd67bc0e995ec1f7c16c7a86eed2d6e5a8aac7a51898752b2fcd65e3658`。一日直接续接 artifact14159593339保留15个原文件及审读摘要，3,670,454 bytes，ZIP SHA256 `87b422c7fb0bc02335f24c38d31ca29894c18530a61ead5a8901faffbf5902d3`，到期2026-11-16 11:37:45 UTC。小包只是传输载体；原 producer/run/source/SHA 不更换。

该审读于2026-11-15 11:37:35.821619 UTC真实部分clone并 pull --rebase到c8d76ff9，两README相对e68dd23d无变化。后续终端pull的最新已读提交见HANDOFF。

## 5. 可供直接后继消费的准确身份

这里只登记必要的文件身份，不把可重算证书或矩阵放入Git/Release。

| 文件 | bytes | SHA256 |
|---|---:|---|
| p41-original-M6-pole-clearing-certificate.json | 12202 | `2680e9224eef98cc34117156b02605e5a1425f5a5fdd34b6596aa0e5e93bd07b` |
| R807-stage-manifest.json.gz | 51774 | `e771ed25cdd9dcffdfce3cc15d9568fb358f67a0ec9138e70378eac8333998d0` |
| R807-original-nonzero-pole-clearing-theta.json.gz | 2464 | `f11e7225d3a4cdb6bd32403514e07aa54ea8d3df7f371f680828d1c5360c8970` |
| R807-original-five-projection-residual-and-kernel.json.gz | 377696 | `18e71b59bc317915bcf9d7c7a4cecb029683cfa9bfed232454fc1080070cf339` |
| R807-original-four-M6-pole-clearing-coordinate-index.json.gz | 2729 | `358e73a299eae7f108f05142e66ee7d1109011fdcd6ef9c431a064251e6eb5de` |
| R807-exact-V4-M6-index-690.json.gz | 412266 | `710331a3ffad4c95711bf18c1dc052db5befea1248af99e3c27717a4d505c775` |
| R807-exact-V4-M6-index-691.json.gz | 972057 | `7b904f4cccf21a669411515eff248d0a0aa32846f6a86dec68f8df0ae658aad7` |
| R807-exact-V4-M6-index-692-from-kernel.json.gz | 690799 | `7ec0fd41e08dbaf7e1f4b1931c101b6f1ad8d03f38e55fb79969e339877e381d` |
| R807-exact-V4-M6-index-693.json.gz | 985133 | `fb9b9e759ef17d9e023b7e71041aec063566c9c11ba101aa6322d3ac24ad0dd6` |
| full-outputs-manifest.json | 350485 | `eeac0a85efa554bcfec2a55d5bb440b23ed0d91f803e1920349cce3fe9b05de5` |
| R807-retained-producer-inputs.tar.gz | 34167815 | `afa18c12f746f804585524d73ac1ab1c370c0931445a5f23359f4c785291058f` |

R809应直接读本次真实 θ、四成员证书、原R803六组坐标及原基展开。它先恢复六个 τθU_j 的普通S5坐标，最高项为零后得到 θU_j/τ^4 的正规向量。原R787成功后才追加A/B；本次没有原 y 函数、极理想、三重数缩小、双flip、主函数刚性化、η或高度结果。主Serre一致性完成标准仍未达到。
