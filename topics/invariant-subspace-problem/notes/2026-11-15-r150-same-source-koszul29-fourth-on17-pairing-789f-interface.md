# 真实 17 条三阶来源的第四原式与同源 29 配对接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

## 1. 冻结状态与唯一新增工作

程序：2026-11-15-r150-same-source-koszul29-fourth-on17-pairing-789f.py。

源码 26401 字节，SHA256 为 a257de5a251ce8d0d8890041524760eb716b8ef7bf51d4fbb74817457a294aec。已对这组完整字节实际执行 Python ast.parse，成功；没有在本地运行数学。

本入口只新增：

1. 从同一原 primitive 整数多项式提取自然 $B_4$，逐项核 $B_0,\ldots,B_3$ 与已付字节一致；
2. 对 **17 条真实、已完整乘回的三阶来源**形成全部 $4354$ 个原来源坐标的第四右端；
3. 用同一组 29 条真原来源核形成 $29\times17$ 新配对，拼接已付 $29\times58$ 低像矩阵后得到 $29\times75$；
4. 保存完整原小矩阵核、对 17 个实际头坐标的投影和准确的完整第四秩区间。

不重做 21 个新单位解、旧 36/130 个单位解、29 来源的有理支撑恢复、原法五消元或已付的 296072 个低层产品。低层乘回只在对应候选和 verified 文件全部字节匹配后继承。

预算为共享数学 120 秒、每进程 2048 MiB，无 native 编译。全部新完整数组保临时目录，只允许小回执、源码、参数、运行身份和 SHA 长期保留。

## 2. CLI 与输出

命令如下，路径占位符沿当前 run43702348535 的实际 context。

    python -B {scripts}/2026-11-15-r150-same-source-koszul29-fourth-on17-pairing-789f.py
      --consumer-out {work}/third21-normal-four-original-consumer
      --second-out {work}/selected-natural-second-left-regauged
      --pairing-out {work}/same-source-koszul29-second-pairing
      --third-out {work}/same-source-koszul29-third-pairing
      --primitive-equations {primitive}
      --out {work}/same-source-koszul29-fourth-on17-pairing
      --seconds 120
      --memory-mib 2048

主回执名为 same-source-koszul29-fourth-on17-pairing-receipt.json。

完成时 status=completed，outcome 固定为 restricted17-fourth-image-and-full-rank-interval。这不是预报实际像秩；数值必须来自完成的有理计算。共享时间耗尽返回 75、status=completed-prefix；输入或算术身份失败返回 1、status=failed。正常完成返回 0。

两个阶段目录为 original-forcing 与 pairing。每个实际完整阶段可按输入和程序 SHA 绑定直接复用；每条完整 $R_4$ 也独立保存。未返回的原生小 RREF 不冒称已有解。

## 3. 八个固定入口文件

每个输入必须同时匹配字节数和 SHA256。

| 键 | 字节数 | SHA256 |
|---|---:|---|
| old_unit | 9008513 | c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe |
| consumer_products | 10890 | 8a147b79e6f7a502aacc58fc07605c6754addf5d550295e838929955f5d1055f |
| through3 | 40272 | 795a0ae79597cdd55ace1ccc215aedc639e19100e1e2e1942fd30f99b373951a |
| primitive | 65159 | 44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe |
| old_pair | 112488 | b1b4c81c2e827fa92a375dfdc94d183604741badba3962de9e998add821946b1 |
| old_pair_receipt | 15304 | 11b0f10e9c0750b73644c425f91b48a249e5829a8dc7960e68e7713ef545f289 |
| third_pair | 152226 | 912a777573f261446f87fda25b71fe889963f31cb5a7f34dc192b42045a1af47 |
| third_pair_receipt | 2365 | f25f2b7c8f3c2cba1999bf4bf9f96721038f29f78960834dbd2b6fb990de0415 |

实际路径由 CLI 固定展开：

- old_unit：second-out/prepared/second-left-m0-unit-input.json.gz；
- consumer_products：consumer-out/original-products/third21-complete-original-four-layer-products-receipt.json；
- through3：third-out/original-forcing/same-original-natural-through-third-coefficients.json.gz；
- old_pair：pairing-out/pairing/actual-koszul29-by36-original-forcing-pairing.json.gz；
- old_pair_receipt：pairing-out/pairing/same-source-koszul29-pairing-worker-receipt.json；
- third_pair：third-out/pairing/actual-same-source29-by58-third-pairing.json.gz；
- third_pair_receipt：third-out/pairing/same-source29-third-quotient-worker-receipt.json。

17 条完整来源及各自 verified 文件的身份由 consumer_products 的固定字节清单逐一确定。29 条原来源核由 old_pair_receipt 的固定实际清单确定；证书从 pairing-out/reconstructed-source29 只读。所有这些实际字节也在消费前复核。

输入绑定不包含绝对路径，仅含程序身份、八个输入身份和数学范围。跨目录恢复不会因路径文本变化而伪造新数学。

## 4. 原自然参数与新右端

原模型仍为 17 个方程、77 个一次/二次 moment 项。自然系数严格按原权提取：

- $N$ 的一次 moment 系数取 $s^{10},s^9,s^8,s^7,s^6$；
- $N$ 的二次 moment 项只出现在常项；
- $\Gamma$ 的二次 moment 系数取 $s^5,s^4,s^3,s^2,s^1$；
- $\Gamma$ 的一次 moment 项必须精确为零。

程序检查完整原多项式字节及所有自然次数规则，核前四层共 $4\cdot17\cdot77=5236$ 个系数与已付来源相同，保原 $J$ 排列和原 4367 个输出单项式序。

每条真实来源直接使用已保存的 primitive 整数四层，不重新改动其列尺度：
$$
R_{4,a}=B_1^T\lambda_{3,a}+B_2^T\lambda_{2,a}
        +B_3^T\lambda_{1,a}+B_4^T\lambda_{0,a}.
$$
完整 4354 个坐标先落临时文件 original-fourth-forcing-NN.json.gz，再进行配对。该文件绑定完整候选、verified 回执、四层 SHA 及同一原来源排列。

不得把共动系数替代自然系数，也不得删除来自 $B_4$ 或法四 $\lambda_3$ 的项。

## 5. 配对和列比例

旧 $29\times58$ 配对的秩必须实际仍为 6，前 36 列必须与更早的原 $29\times36$ 配对逐项相同。同一组 29 条原核的完整 6188 来源、J 外零、4367 原产品零和来源 SHA 均从已付真实证书核定。

新矩阵按
$$
P_{75}=[\,K_{29}^TH_F,\ K_{29}^TT,\ K_{29}^TR_3(\text{旧22}),\
                       K_{29}^TR_4(\text{实际17})\,]
$$
拼接，绝不按单位行 content 改变原配对。

为小 RREF 可分别除各行/各列的非零整数 content；完整核系数必须按列 content 除回原 75 列坐标。程序随后在未缩放原 $P_{75}$ 上核全部核产品为零。再取最后 17 个坐标的完整投影，生成其独立头组合。

实际输出包括：

- actual-same-source29-by75-fourth-on17-pairing.json.gz；
- complete-fourth-pairing-kernel-and17-head-projection.json.gz；
- same-source29-fourth-on17-worker-receipt.json。

大整数矩阵与完整核只保在临时目录，长期回执只写实际大小/SHA及小数字。

## 6. 完整域与受限域的量词

现有完整第三头域为 21 维，本次实际域为 17 维，缺四个显式头。已知来项 $W_{13}$ 维 13，完整来项 $W_3$ 维 15，缺两个像方向。此前已经证明
$$
E/W_{13}\simeq K_{29}^*/\pi(W_{13}),
\qquad \dim E/W_{13}=23.
$$

设实际总配对秩为 $6+r$。本次真实域的像秩就是
$$
r=\operatorname{rank}P_{75}-6,\qquad 0\le r\le17.
$$
完整 21 维域多四维，再商缺少的两维来项至多降秩二，因此输出
$$
\max(3,r-2)\le \operatorname{rank}_{\mathbb Q}\beta_4\le r+4.
$$
下界 3 只引用同一 $\mathbb Q/\mathbb F_{31}$ 原单位 Schur 前三页已经相等的秩 $3,9,3$。程序不把原 mod31 高阶数搬成特征零结论。

受限域上 $r=0$ 合法，给完整秩区间 $[3,4]$。$r=3$ 也不能闭完整秩为 3，因为本次域并未包含所有 21 个头。

原 75 列配对核对最后 17 坐标的投影必须实际为 $17-r$ 维；它们通过完整已知商同构给真实第四头的存在性，但不是新 $\lambda_4$ 证书。主回执始终保 explicitLambda4SourcesConstructed=false、all21CompleteThirdHeadsExplicit=false、completeFourthIncomingImageComputed=false。

对应的合法新增指定子式下界为
$$
v_\infty(D)\ge114+(17-r),
\quad
v_\infty(\mathrm{cofactor})\ge110+\max(16-r,0).
$$
所有原来源换列按完整原正则列 Laplace 取得同一 cofactor 下界。费用需使用运行完成时最新已出版公共因子重新代入，源码不把历史 K104 或其后因子硬写为当前事实。

## 7. 完成字段

主回执保以下实际字段及范围：

- actualFourthForcingColumns=17，originalFourthForcingCoordinates=74018；
- all17PaidFourLayerProductsInheritedByExactHashes=true；
- all5236PaidNaturalCoefficientIdentitiesVerified=true；
- completeCombined29By75PairingRank；
- restricted17FourthRankModuloKnownIncoming13；
- fullSelectedFourthRankOverQLowerBound / UpperBound；
- provedFourthHeadDimensionLowerBound；
- allOriginal75PairingKernelProductsZero=true；
- actualExplicitThirdHeadDimension=17，completeGlobalThirdHeadDimension=21；
- missingExplicitThirdHeads=4，missingIncomingImageDirections=2；
- newM0RightHandSidesSolved=0；
- explicitLambda4SourcesConstructed=false，leadingUnitProved=false。

任一原来源、文件身份、自然系数或完整核产品失败，都停止该阶段并保实际已成前缀；不将失败覆盖为某个秩结论。
