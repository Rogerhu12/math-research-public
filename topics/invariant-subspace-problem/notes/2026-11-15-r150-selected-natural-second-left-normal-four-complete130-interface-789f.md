# 同一自然第二页：完整高核 130 的原单位解续接

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

**状态。** 下面两个阶段已经完成：旧新规范二阶族给出 22 个真头；normal4 高矩阵已经在 $\mathbb Q$ 上完整求核，维数恰 130。本文件冻结的续接源码只完成尚未支付的 130 个辅助单位解及其完整原残差，不重复高矩阵选元或有理高核求解。源码的同字节本地 AST 已通过；本接口在数学运行前冻结，实际结果另见该步骤小回执。

## 1. 固定来源和真实前缀

保持同一原 $4354\times4354$ 方阵 $B(u)$、同一原自然参数 $u$、原整数行列权、原输出集合 $I$ 和来源集合 $J$。旧二阶完整族采用两个不同的坐标嵌入：
$$
\begin{aligned}
\lambda_0&=\Lambda Cc,\\
\lambda_1&=E_{\rm old}Xc+\Lambda Ft+\Lambda Cy,\\
\lambda_2&=E_{\rm new}x+E_4\eta+E_{\rm old}Xy+\Lambda e.
\end{aligned}
$$
其中 $c,y$ 各有 33 个坐标，$t$ 有 3 个，$e$ 有 36 个。旧恒等式为
$$
B_0^{\mathsf T}E_{\rm old}X+B_1^{\mathsf T}\Lambda C=0.
$$
因此原未缩矩阵和完整二阶 forcing 是
$$
M_0=B_0^{\mathsf T}E_{\rm new},\qquad
M_4=B_0^{\mathsf T}E_4,\qquad
H_F=B_1^{\mathsf T}\Lambda F,\qquad
T=B_1^{\mathsf T}E_{\rm old}X+B_2^{\mathsf T}\Lambda C.
$$
实际要解的是
$$
M_0x+M_4\eta+H_Ft+Tc=0
$$
的全部 4354 个原来源坐标。$X$ 不从 $E_{\rm old}$ 移到 $E_{\rm new}$。

旧实际二阶入口保存了 1546 个修正变量、36 个原 forcing 列及其完整原残差 $S_{\rm old}$；$\operatorname{rank}_{\mathbb Q}S_{\rm old}=14$，得到 22 个独立头。其完成绑定是
`c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e`。

最新实际前缀：

- run：`43702348535`；
- step：`selected-natural-second-left-normal-four-continue`；
- 执行源：`c8d76ff9c19e248f9a2809bbef1ff06fc3b5d0ac`；
- 数学用时：21.356861559000208 秒；
- 主线小回执：`notes/r150-infinity-remote-session-789f/43702348535-selected-natural-second-left-normal-four-continue.json`；
- 完成高核绑定：`c18a0a21f0ca0e44aeaa65c138bbf02e5b26fc7d01542573aef47dbc7b532fec`。

该前缀保全 $M_4$ 的 4354 行、1485 列，取旧 $M_0,H_F,T$ 同时为零的完整 1736 行组成 $H_4$。已付
$$
\operatorname{rank}_{\mathbb F_{31}}H_4
=\operatorname{rank}_{\mathbb Q}H_4=1355,\qquad
\dim_{\mathbb Q}\ker H_4=130.
$$
原 1355 方块的模 31 行列式为 25。130 列完整有理解返回后，全部 1736 行 Schur 恰为零；全部 $1736\cdot130=225680$ 个原高产品已核零。实际退出 75 只表示后续辅助 worker 当时上限为 64，不是这次高核没有完成，也不是新的二阶不相容。

## 2. 最小输入和精确命令

在仍保持临时数组的同一 Actions session 中执行：

~~~text
python -B {scripts}/2026-11-15-r150-selected-natural-second-left-normal-four-complete130-789f.py
 --regauged-out {work}/selected-natural-second-left-regauged
 --rebuild-root {work}/selected-natural-u-rebuilt
 --high-prefix {work}/selected-natural-second-left-normal-four-continue
 --unit-worker {scripts}/2026-11-15-r150-selected-left-normal-four-unit-solve-worker-789f.py
 --out {work}/selected-natural-second-left-normal-four-complete130
 --seconds 600
 --memory-mib 4096
~~~

外层墙钟建议 660 秒。数学共享时钟不超过请求的 600 秒，每个进程继承 4096 MiB 地址限额；有具体需要时同一源码允许不超过 8192 MiB。无 native 编译、无安装、无 NumPy。Python-flint 固定 0.9.0。

主回执为：

`selected-natural-second-left-normal-four-complete130-receipt.json`。

源码：

| 项目 | 路径 | 字节数 | SHA256 |
|---|---|---:|---|
| 主入口 | `notes/2026-11-15-r150-selected-natural-second-left-normal-four-complete130-789f.py` | 34812 | `6b478e60d9508d977c156bf55bc0efc89205cf80b4a8ccf544547afebedb8ba6` |
| 辅助 worker | `notes/2026-11-15-r150-selected-left-normal-four-unit-solve-worker-789f.py` | 16412 | `c9e1eee6142d29daf661682e177702825e90aef7222611baa2adadaffe0dc731` |

主入口 blob 是 `6e6f6fdb07089f89d31a4f06d3ac8ab7c7b24af7`；worker blob 是 `ba96a24c85eb543efafff03ac264b7de7144c42a`。worker 仅把原版本的 RHS 合法范围改为 $1\le k\le130$；本轮实际每批仍不超过 32。

十个固定输入如下。前三个新高核输入之外，七个旧完成输入保持原字节。

| 输入键 | 相对输入路径 | 字节数 | SHA256 |
|---|---|---:|---|
| paid_high_block | high-prefix/high-profile/complete-original-normal-four-block.json.gz | 911018 | `88d9f609c39c754913beaf06c4b5e945ce84fde5c0a0bde78f7e57216bd33f0e` |
| paid_high_kernel | high-prefix/high-kernel/complete-original-normal-four-high-kernel.json.gz | 1446855 | `46b047a303d68a3502aa076836f77dc0fde101ca93d6df2c8568380f2d190d63` |
| paid_high_main | high-prefix/selected-natural-second-left-normal-four-continue-receipt.json | 5667 | `161e2a48e5b82fd26c67a9100b95e75b88ce85ecb395eb59dc84a760c637aa34` |
| old_unit | regauged-out/prepared/second-left-m0-unit-input.json.gz | 9008513 | `c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe` |
| old_solution | regauged-out/unit-solve/complete-m0-unit-solution.json.gz | 18124389 | `9c3b02d2674af645ffcfd5297cf5c9ac287fe314d0c40f49c8bb99be9396352d` |
| old_full | regauged-out/full-products/second-left-full-products-receipt.json | 12690 | `b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70` |
| old_main | regauged-out/selected-natural-second-left-regauged-pipeline-receipt.json | 20323 | `2343123363d6c38a871c66770afb67b37a1b3a6b882baa7aed040134914a345b` |
| old_rref | regauged-out/full-products/complete-small-second-residual-rref.json.gz | 17625 | `de7bb03e76ca2dee0221d4f89e1de5db190b6c5b64fc4df70a67e13f405a7941` |
| coefficients | rebuild-root/rebuilt-first/same-original-natural-constant-and-first-coefficients.json.gz | 20580 | `7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1` |
| profile | rebuild-root/rebuilt-inputs/same-selected-original-output-indices.json | 21066 | `044b28d717749d23a2959a02c0f8ed7570bfa19bcdff04207056f2a66d2e413d` |

旧 36 个 `original-residual-column-%02d.json.gz` 依原 `old_full` 中逐项文件哈希读取。这里不把它们重新乘回，也不绕过哈希检查。

## 3. 只新增必要的单位解

将已付完整高核写成 $Z_4\in\mathbb Z^{1485\times130}$，其列均非零且在 $\mathbb Q$ 上独立。新入口读取它的原整数列，形成
$$
W=M_4Z_4\in\mathbb Z^{4354\times130}.
$$
保全所有 4354 行，原 1736 个高行再次随完整 $W$ 检查为零；这不是重新求高核。

使用旧同一 1546 个原单位行 $P$ 和同一 $M_0$。每个新方向只求
$$
M_0[P,:]\,X_j=-W[P,j].
$$
逐行除共同 content 时，矩阵和 RHS 按完全相同的有理比例运输。实际调用按原高核列顺序分成
$$
32,\ 32,\ 32,\ 32,\ 2
$$
五批，编号区间为 $[0,32),[32,64),[64,96),[96,128),[128,130)$。

每批 worker 先保存全部正最小公分母 $D_j$ 和 1546 项整数分子 $N_j$，然后逐列核
$$
M_0[P,:]N_j+D_jW[P,j]=0
$$
的全部 1546 个**未除行 content 的原坐标**。返回后存完整解和已核列数。下一批只在当前批真实完成后开始。若 native 尚未返回，不称已有该批候选。

所有批次完成后，assembly 核每批的输入、原 RHS 列序、原单位矩阵、源码、候选 SHA 和完整产品回执，再拼成一个 130 列解文件。该合并文件是在各批已验证之后形成，所以回执明确区分：

- 每批完整候选先于其产品检查保存；
- 合并本身只重排已核列，不声称合并文件早于那些检查；
- 已核原单位坐标总数恰 $1546\cdot130=200980$；
- 全 4354 行余式仍必须由下一阶段支付。

## 4. 166 列完整残差及真头

旧 36 个实际原残差整列复用。新 130 个残差逐列计算并立即保存：
$$
S_{{\rm new},j}=M_0N_j+D_jW_j\in\mathbb Z^{4354}.
$$
每列保全部 4354 坐标和单位行零条件。然后对
$$
S=[S_{\rm old}\mid S_{\rm new}]
$$
的完整原非零行作一次精确 RREF，列数恰 166。

这里有一个已经证明、但仍与实际 RREF/头投影共同核验的约束。若
$$
E_{\rm new}x+E_4Z_4a\in\ker B_0^{\mathsf T},
$$
完整常左核仅在 normal 次数不超过 2 支持，故 normal4 坐标迫 $Z_4a=0$，继而 $a=0$；旧新规范的真补空间再迫 $x=0$。所以新 130 个 $W_j$ 在 $\operatorname{coker}M_0$ 中独立。取单位解不会改变此事实：
$$
\operatorname{rank}_{\mathbb Q}S_{\rm new}=130.
$$
记 $i=\dim(\operatorname{im}S_{\rm old}\cap\operatorname{im}S_{\rm new})$，则
$$
\operatorname{rank}_{\mathbb Q}S=144-i,\qquad
\dim\ker S=22+i.
$$
旧 22 头仍在，已付完整第二连接模 31 下界为 9，且真实 $c$ 投影单射，故本轮必须有
$$
0\le i\le2,\qquad142\le\operatorname{rank}_{\mathbb Q}S\le144.
$$
**130 个修正方向不是 130 个新头。**

对每个真实剩余核向量 $\gamma=(\gamma_{\rm old},\gamma_{\rm new})$，按各列原分母恢复
$$
\begin{aligned}
(t,c)&=\operatorname{diag}(D_{\rm old})\gamma_{\rm old},\\
x&=N_{\rm old}\gamma_{\rm old}+N_{\rm new}\gamma_{\rm new},\\
\eta&=Z_4\operatorname{diag}(D_{\rm new})\gamma_{\rm new}.
\end{aligned}
$$
逐项原乘回
$$
M_0x+M_4\eta+H_Ft+Tc=0
$$
并另算 33 行 $c$ 投影的实际有理秩。全部 4354 原坐标零、$c$ 投影秩等于剩余核维数后才记录独立头。保原完整 $y_{33},e_{36}$ 自由和两个不同的 $E$。

## 5. 完成和未完成的精确分支

正常完成的 `status=completed` 有两种数学 outcome：

1. `same-selected-second-rank-nine-proved`：实际头数 24，全部原乘回真，结合已付下界给同一所选方阵的 $\mathbb Q$ 第二连接秩恰 9。
2. `restricted-second-left-support-only`：实际头数 22 或 23，只闭 normal 次数不超过 4 的这一完整支撑；第二连接上界分别为 11 或 10，下界仍为 9。更高 normal5 修正尚未排除。

最终字段保：

- `secondHeadImageDimension`、`newIndependentHeads`；
- `extendedSmallResidualRank`、`oldNewResidualIntersectionDimension`；
- `actualHeadProjectionRank`；
- `all4354OriginalSecondLeftProductsZero`；
- `fullOriginalSecondJetProductCoordinates=4354*secondHeadImageDimension`；
- `completeFixedSupportSecondEnvelopeComputed=true`；
- `selectedSecondConnectionRankOverQLowerBound=9`；
- `selectedSecondConnectionRankOverQUpperBound=33-secondHeadImageDimension`；
- `selectedSecondConnectionRankExactly9` 和 `completeSelectedSecondHeadSpaceProved` 仅在 24 头全核时为真。

共享时间到时为 `status=checkpointed-time-budget`、exit 75。算术/输入/绑定不符为 `failed-or-incomplete`、exit 1，绝不把不足的检查记为负定理。所有分支保持 `leadingUnitProved=false`。

## 6. 真实检查点与重入

本轮新 binding 绑定主源码、worker 源码、十输入 SHA、原完成二阶绑定、原完成高核绑定及实际批宽 32。绑定不含绝对恢复目录、时间或内存限额。

临时阶段目录是：

- `paid-high/`：只换本轮语义绑定，保旧原数组和继承 SHA；
- `new-images/`：完整 $W$、130 列 unit input、五个按原列序的 batch input；
- `additional-unit/batch-000-031/` 等：每批全候选、完整1546产品、实际已核列数；
- `additional-unit/`：五批都完成后的合并候选和审计回执；
- `full-products/`：逐新残差、完整166列RREF、实际头源及其4354产品回执。

同一 CLI/输出目录重入会核同输入和源码绑定，跳过完整阶段、完整 batch、完整残差和已核头。不重算旧 36 列，不重高 130 列求核；尚未返回的单个 native batch 只能重启该批，不能声称恢复其内部未保存计算。

全部可重算数组仅留同 job 临时目录。按根 README 规则，只发布小文本源码、参数、实际执行身份、小回执和 SHA；不上传大 Git blob、Release 附件或可重算数据工件。
