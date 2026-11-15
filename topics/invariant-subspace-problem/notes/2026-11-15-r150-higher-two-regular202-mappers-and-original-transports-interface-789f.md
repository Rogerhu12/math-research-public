# 两个原始 202 mapper 与原坐标运输：执行合同

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。

## 1. 新阶段与范围

[已付来源直和](../results/R150-appendix-original-koszul-source-direct-sum-and-216-column-reduction.md)把原来源核缩为 $27\times216$ 的真实 $SE$。本入口读取新长会话已经完成的 full $0,\ldots,32$ 与 outside $0,\ldots,35$ 系数，恢复

$$
N_H\in\mathbb F_{31}[[u]]^{216\times202},
\qquad
N_O\in\mathbb F_{31}[[u]]^{231\times202},
$$

两者均到次数 $21$。第一式满足 $(SE)N_H=0$；第二式满足原 outside 小 Schur 的转置乘回为零。

本页冻结代码时，新 mapper 和新运输 native 尚未执行。它们是有限域算法，不把模 $31$ 的 DAG 当成有理消元，不从 Q13 左核整性推出原 source 核平坦。父实际 binding 为：

- full32：9e86556a7a82c1c2306b395c87a49a7059d0945f12db7d4962c789717bd35dc6；
- O35：f07acb3347e775dc41658f95e015c2e169b4df34c6c1e829a2737fe83acb2781。

两父阶段各自已经逐 $66$ 文件核原 $0,\ldots,21$ 系数不变。

## 2. 冻结源

| 作用 | 文件名 | 字节 | SHA256 |
|---|---|---:|---|
| 两个小 mapper 及运输头准备 | 2026-11-15-r150-higher-two-regular202-mappers-preparation-789f.py | 22703 | a2e8fa4aa6d26c74b2f8000fb33fcda4b558021ab674582eecbd2c86edb9847e |
| 原 $202$ 来源回代 | 2026-11-15-r150-original-high202-source-transport-789f.cpp | 23360 | d0748649a3cd280fb620c85c61b82cb9d6c6fabeef8e9db81afaf9b9b01a4b2c |
| 原 outside $202$ 左核回代 | 2026-11-15-r150-original-outside202-left-transport-789f.cpp | 12826 | 92e534d74d465f99043ec293bdd5a82a67c661309767e42e476bf765e1244262 |

对应 blobs：

- d0a4baa6a338bf88b9bddc1442a251ca0ba311d7；
- 7bc603752084085a591cc2db10761e3f54e7a212；
- 37c90205d197930a247621dc18e5f85ac7c09a1f。

三文件均在本课题 notes 下。两 C++ 只用已固定的 saturated-global-common 与 f31-bitplane 两头文件，无额外 FLINT 开发库。

## 3. 同一原坐标的输入链

准备程序固定 native model $128145$ 字节、SHA256
291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6；
selected receipt $75700$ 字节、SHA256
5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68；
以及已付 $216$ 小摘要 $14075$ 字节、SHA256
ba8bd267563e7cb24f49704c76d0f12a5226e2255d5a3b70ffa7249e90f6b484。

新 $216$ 临时对象首先按当前 complete-stage-manifest 核全部字节。原 gzip 生成器保当前 mtime，所以重建后的压缩 SHA 可改变；另逐一核已付 $E_{216}$、原来源列表、$1632$ 单位行 SHA、RREF SHA、determinant $15$ 与不变数学 binding。不会硬套已失旧作业的压缩 SHA。

当前 full native 的全部 $P,R,H$ 字典必须与新 $216$ profile 相同。$J^c$ 则从原 $3333$ pre 来源和实际 $1021$ selected 来源恢复，按原编号排序；其 SHA 必须等于当前 outside 回执。因此后续配对没有混用两个仅维数相同的来源空间。

## 4. 实际单位 Schur 与正规核

对当前矩形系列 $M(u)$，计算真实 $M(0)$ 的秩及单位行列，排列为

$$
M=\begin{pmatrix}U&V\\W&Z\end{pmatrix},
\qquad
S=Z-WU^{-1}V.
$$

逐阶求 $U^{-1}$ 并逐系数核 $UU^{-1}=I$。只有完整 Schur 常项已经核零，才对这个剩余块除 $u$；原列索引始终保留。若递归得到 $S$ 的核 $Y$，上一层回代是

$$
\binom{-U^{-1}VY}{Y}.
\tag{4.1}
$$

回代只保子层实际返回的精度，不把缺失高项声称为已知。泛秩分别为 $14$ 和 $29$，全部 active 正方向剥完后，仍核剩余矩形的所有已算系数为零，再将剩余 $202$ 个原坐标置为恒等自由块。因而得到正规原始基，不仅是泛型列空间。

所有恢复系数接受原小矩阵完整乘回：

- full 侧 $27\times202\times22=119988$ 个坐标；
- outside 侧 $29\times202\times22=128876$ 个坐标；
- 两侧 $202$ 自由行的常项 $I$ 及高项零逐项核验。

算法不假设任意固定 $14$ 或 $29$ 原子式有最小逆极点。实际单位 Schur 的累计除式次数及全部谱必须分别匹配 full 的最大值 $11$ 与 outside 的最大值 $14$。

## 5. 两个精度损失独立

full 输入到次数 $32$，损失 $11$，保 $0,\ldots,21$；outside 输入到次数 $35$，损失 $14$，同样保 $0,\ldots,21$。后继使用原 outside 左核与原来源直接配对，不对已经恢复的来源再串行作一次非单位除法。因此损失不是 $11+14$。

## 6. 准备 CLI 与真实阶段缓存

~~~text
--native-model {work}/inputs/repo/native-normal-form-input.txt
--selected-receipt {work}/inputs/repo/selected-infinity-minor-dag-receipt.json
--paid-source-summary {scripts}/43736746064-higher-kernel-original-216-source-preparation.json
--source-native {scripts}/2026-11-15-r150-original-high202-source-transport-789f.cpp
--outside-native {scripts}/2026-11-15-r150-original-outside202-left-transport-789f.cpp
--source-prepared-out {work}/higher-kernel-original-216-source-preparation
--full-out {work}/full-infinity-natural-dual-schur-through32
--outside-out {work}/koszul-outside-natural-through35
--out {work}/higher-two-regular202-mappers
--seconds 180
--memory-mib 1024
~~~

本阶段无 native 编译，建议外墙 $205$ 秒。主回执为 higher-two-regular202-mappers-receipt.json。成功时：

- status=completed；
- outcome=complete-two-original-regular202-mapper-heads；
- maximumVerifiedMapperDegree=21；
- sourcePrecisionLoss=11、outsidePrecisionLoss=14；
- all119988OriginalHighSmallProductsVerified=true；
- all128876OriginalOutsideSmallProductsVerified=true；
- 两侧全部自由坐标标志为 true。

完整原 source 运输、outside 左运输、最终高商的标志仍为 false。完整一侧做完后单独原子保存阶段，预算停时复用已成一侧，不把半个 native RREF 记为完成。

临时输出包括两份完整 kernel series、各自 metadata、high202-native-heads.bin、outside202-native-heads.bin、prepared-two-original-mapper-transports.json 和 complete-mapper-stage-manifest.json。所有大数组仅在本作业使用。

## 7. 原 $202$ 来源回填

source native 复用 full v2 全部真实常单位构造，包括 $3333$ 预基的低次数三角尾和 $1007$ 来源操作。sourceSolve 是原 transposeSolve 每个线性赋值的逆序转置，依次对应：

- 原预基单位三角回代的转置；
- 原剩余输出三角回代的转置；
- $G$ DAG 逆序转置；
- backward 操作逆序转置；
- forward 操作及 scale 逆序转置。

因此作用的是同一个原常单位 $U(0)^{-1}$，其来源支撑严格限于原 $P$。

给定 $h=E N_H$，逐阶求 $K_H$；全部 $1848$ tail 坐标始终等于 $h$，而 $P$ 坐标由原单位求解。每层核完整 $4367\times202$ 原乘回为零后才提交。

native 的九个参数为：

~~~text
model prepared-full-profile forward backward full-operations
high202-native-heads.bin prefix 21 remaining-seconds
~~~

输入 magic R15HKS31，含版本、两层 binding、实际 $216$ 原来源行、实际 $202$ 自由头及 $22$ 层系数。输出 source/product 为 R15HKX31、R15HKR31；ledger 绑定整份头文件 SHA 和父 full binding。保存完整来源与产品，不只保存秩。

## 8. 原 outside $202$ 左核回填

原 $O$ 分块为

$$
O=\begin{pmatrix}U_O&V_O\\W_O&Z_O\end{pmatrix}.
$$

给定小左核尾 $N_O$，完整左核为

$$
L_O=\binom{-U_O^{-T}W_O^T N_O}{N_O}.
\tag{8.1}
$$

使用已经核过的常逆和全部原次数 $0,\ldots,10$ 系数逐阶回代。常逆必须取转置，不能直接用 $U_O^{-1}$。每层核全部 $1632$ Koszul 方程、全部 $1834$ 原坐标与 $202$ 自由块。

native 的六个参数为：

~~~text
outside-original-natural-coefficients.bin
outside-constant-unit-inverse-field31.bin
outside202-native-heads.bin prefix 21 remaining-seconds
~~~

输入 magic R15OLH31，包含原单位行、原单位列、全部 $231$ tail 行和自由位置。输出 left/product 为 R15OLX31、R15OLR31。全部输入 SHA 与父 outside binding 绑定，只有完整层可续接。

## 9. 最终商的未付步骤

两个原运输都完成后才能形成

$$
D_{\mathrm{high}}=L_O^T\Pi_{J^c}K_H.
$$

必须按同一 $J^c$ 顺序取原来源，保完整单位自由块和全部原乘回。准备阶段尚未算这项配对。后继在其 $202$ 阶常项上实际选单位，然后只对剩余小方阵继续 Smith；任何所得模 $31$ 长度都不自动成为特征零结论。
