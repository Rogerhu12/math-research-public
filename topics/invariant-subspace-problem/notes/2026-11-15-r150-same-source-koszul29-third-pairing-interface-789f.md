# 同一 29 个原 source 对现有 22 个真第二头的第三商完整配对

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。

状态：源码冻结，尚未执行本轮研究计算。本地环境已失联，新源码未做本地 AST；首次实际调用 Python 时由解释器解析。本轮不恢复失去的旧大块，不续 normal5 消元，也不解新的 M0 右端。

## 1. 为什么 29 个 source 测试现在是完整第三商

沿用同一自然无穷远方阵
$$
B(u)=B_0+uB_1+u^2B_2+u^3B_3+\cdots
$$
及相同原 $I,J$。令
$$
E=\mathbb Q^{4354}/\operatorname{im}B_0^T,\qquad
S\subset\ker B_0
$$
为已实际恢复的 29 维原 source 核。限制配对给
$$
\pi:E\longrightarrow S^*,\qquad \dim E=36,\quad\dim S^*=29,\quad\dim\ker\pi=7.
$$

实际第二配对已付
$$
W=\operatorname{span}_E[H_F,T],\qquad
\dim W=12,\quad \dim\pi(W)=5.
$$
因此
$$
\ker\pi\subset W,\qquad
\boxed{E/W\ \simeq\ S^*/\pi(W).}
\tag{1.1}
$$
两边维数均为 $24$。此为[完整第二连接秩 9 的正式结果](../results/R150-appendix-selected-natural-second-connection-exact-nine-from-koszul29-and-cost8623.md)中余维不等式取等的直接推论。

这项同构并不声称 $S$ 是完整的 36 维 source 核；它证明在商掉已付完整低页像 $W$ 后，少掉的七个 source 方向已被低页像支付。

## 2. 完整低层歧义和实际第三 forcing

对一个第二可延头，取真实原二阶 jet
$$
B_0^T\lambda_0=0,\quad
B_0^T\lambda_1+B_1^T\lambda_0=0,\quad
B_0^T\lambda_2+B_1^T\lambda_1+B_2^T\lambda_0=0.
$$
其第三 forcing 为
$$
R_3=B_1^T\lambda_2+B_2^T\lambda_1+B_3^T\lambda_0.
\tag{2.1}
$$
固定同一个头，两组二阶 lift 的差为
$$
\Delta\lambda_1=\Lambda Cy,\qquad
\Delta\lambda_2=E_{\rm old}Xy+\Lambda e.
$$
所以第三 forcing 的差在 $E$ 中属于
$$
\operatorname{span}\left(
B_1^TE_{\rm old}X+B_2^T\Lambda C,\ B_1^T\Lambda
\right)
=\operatorname{span}[T,H_F]=W.
$$
这里 $e$ 的全部 36 维、$y$ 的全部 33 维都保留；$B_1^T\Lambda C=-B_0^TE_{\rm old}X$ 在 $E$ 中为零。因而完整第三连接的目标商确为 $E/W$，没有丢掉零头低层自由度。

本轮只使用已有 **22 个显式真第二 jet**。完整第二头空间维数已知为 24，但另外两个显式代表尚未构造。本轮矩阵 $R_3$ 有 22 列，所有列由原实际来源生成。

实际旧变量列为 $c\in\mathbb Z^{33},t\in\mathbb Z^3,x_2\in\mathbb Z^{1546}$，还原为
$$
\lambda_0=\Lambda Cc,\qquad
\lambda_1=E_{\rm old}Xc+\Lambda Ft,\qquad
\lambda_2=E_{\rm new}x_2.
\tag{2.2}
$$
代码始终区分 $E_{\rm old}$ 和 $E_{\rm new}$，不把旧 $X$ 移入新规范。

每列完整还原后，允许同时除去三层所有整数系数的共同 gcd；这是同一 jet 的非零 Q 标量缩放。共同因子逐列保存。随后沿同一全部 $4354$ 个原来源行重新核三层恒等式，总计
$$
22\cdot4354\cdot3=287364
$$
个原整数产品。所有检查通过后，才接受该列的完整第三 forcing。

若后续用本轮的 22 头坐标返回旧未约化的 22 个 jet，必须再逐列除以所存 primitiveCoChainCommonDivisor。代码保存此运输说明，不将约化后的坐标直接当旧坐标。

## 3. 新矩阵、真秩范围和正向存在性

使用本次已经恢复且逐来源 SHA 绑定的同一个 $K\in\mathbb Q^{4354\times29}$，只新增
$$
P_3=K^T[H_F,T,R_3]\in\mathbb Q^{29\times58}.
$$
前 36 列原字节不变，实际旧秩仍为 5。设新总秩为 $r$，定义
$$
b=r-5.
$$
由 (1.1)，$b$ **正是**完整第三商中、现有 22 维第二头子空间上的连接秩，而不只是某个必要投影的秩下界。因此其中第三可延头维数恰为
$$
22-b.
\tag{3.1}
$$

完整第三连接的定义域只有另外两个头方向，故
$$
b\le\operatorname{rank}_{\mathbb Q}\beta_3\le b+2.
$$
同一常块、第一、第二层在 Q 与模 31 下的秩已经分别相等为 $4318,3,9$。可以沿这些真正的 31 单位层消元，所以已付第三模 31 秩 3 给出合法 Q 下界。合并得到
$$
\boxed{\max(3,b)\le\operatorname{rank}_{\mathbb Q}\beta_3\le b+2.}
\tag{3.2}
$$

| 实际结果 | 完成 outcome | 正确范围 |
|---|---|---|
| $b=1$ | complete-selected-third-rank-three | 完整第三秩恰为 3，第三可延头恰为 21 维 |
| $b\ge2$ | restricted22-third-exact-image-and-full-rank-interval | 保存 (3.2) 与 $22-b$ 维真第三头存在性 |
| $b=0$ | failed | 与已付完整第三下界 3、仅缺两域方向矛盾；必须查输入/实现 |
| 超时 | completed-prefix，退出 75 | 只保已完成真实阶段，不发布完整第三秩 |

程序还完整构造 $P_3$ 的核并核原 $29\times58$ 产品，将其后 22 个坐标投影，实际投影秩必须为 $22-b$。

**配对核中的前 36 个系数未必已经是最终原方程的低层补偿系数。** 它们只消除了配对；不可见部分还可能属于 $\ker\pi$。由 $\ker\pi\subset W$，存在另外的低层补偿消掉该部分，随后存在 $\lambda_3$。所以 (3.1) 的头存在性是完整的，但本轮不构造这些额外补偿或显式 $\lambda_3$，不将配对核列直接命名为完整原第三 jet 证书。

## 4. 同一自然坐标与原 F3

原 primitive 整数参数模型完整 bytes/SHA 固定。代码按与旧第一、第二阶段相同的自然权提取 $F_0,F_1,F_2,F_3$：

- $N$ 线性系数从 $s^{10},s^9,s^8,s^7$ 取；
- $N$ 二次部分为 $u$ 常数，其后三项为零；
- $\Gamma$ 二次系数从 $s^5,s^4,s^3,s^2$ 取；
- $\Gamma$ 线性系数整条必须为零。

先逐系数核 $F_0,F_1$ 与已付自然文件完全一致，再构造原 $B_2,B_3$ 的作用。没有使用共动三阶导数，也不丢来源坐标变化的项。

normal 变量仍是 $m_0,\ldots,m_8$，纯变量为 $d=m_9,c=m_{10}$。全部左向量用原 $4367$ 输出字典展开；实际检查使用同一所选 $J$ 的全部 $4354$ 来源。它们是所选左 jet，不把检查范围夸成原全部 $6188$ 来源的全矩阵左核。

## 5. 固定源码、输入与 CLI

新源码：

- notes/2026-11-15-r150-same-source-koszul29-third-pairing-789f.py
- blob c7c617d345bc7a236038028aff9efb273da4957e
- 26847 B
- SHA256 3d54a3c8359667149792ad98a66bebe8f5487ccca8492725307958a3df2664b2

主要实际输入：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| 旧第二 unit input | 9008513 | c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe |
| 旧第二完整产品回执 | 12690 | b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70 |
| 完整常左头 | 633788 | 3107ab8547071205466ff5b5aa2ef5f0e3ea81a976258a25184c9a0d7e709fe2 |
| 33 原第一 jet | 1701626 | 2aabfc92860f66942e7a8eb3d9254ab911e7b8b2f255d40bfaa1235ed4d482fe |
| 原自然 F0/F1 文件 | 20580 | 7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1 |
| 完整原 primitive 参数模型 | 65159 | 44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe |
| 实际旧 29×36 配对 | 112488 | b1b4c81c2e827fa92a375dfdc94d183604741badba3962de9e998add821946b1 |
| 实际旧配对 worker 回执 | 15304 | 11b0f10e9c0750b73644c425f91b48a249e5829a8dc7960e68e7713ef545f289 |

完整 primitive 模型解压后 SHA256 为
fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3。

此外，22 个旧第二候选按已付完整产品回执逐文件核 SHA；29 个原 source 证书按此次配对回执逐文件核 SHA、原 $6188$ 系数向量 SHA 和所有既有原产品标志。旧 source binding 为
2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2；
旧配对 binding 为
ea772f01fa0ab8a761287893c15a94f83ebc6326703b40b82a5846e02b020e39。
因此本轮不重新求旧 1603 单位块，也不重新发现这 29 个核。

~~~text
python -B {scripts}/2026-11-15-r150-same-source-koszul29-third-pairing-789f.py
  --first-out {work}/selected-natural-first-left-envelope
  --second-out {work}/selected-natural-second-left-regauged
  --rebuild-root {work}/selected-natural-u-rebuilt
  --pairing-out {work}/same-source-koszul29-second-pairing
  --primitive-equations {primitive}
  --out {work}/same-source-koszul29-third-pairing
  --seconds 120
  --memory-mib 2048
~~~

一次真实数学时钟 120 秒，每进程 2048 MiB，建议外墙 150 秒。没有编译或软件安装。源码仅依赖当前 Python、标准库和已在本 job 使用的 python-flint 0.9.0。

## 6. 两阶段真检查点

第一阶段 original-forcing：

- 逐列重建实际三层 cochain；
- 逐列核全部三个原低层产品；
- 保存完整 4354 维 R3 列及原 jet/输入 SHA；
- 保存逐列 verified 回执。
- 已完成列可在同 binding 下直接复用。

第二阶段 pairing：

- 验全部原 source 与新 forcing 的实际文件身份；
- 构造并保存完整 29×58 整数矩阵；
- 再进行精确小 RREF、原坐标核回移与 22 头投影。
- 若 RREF 阶段未完，已保存完整矩阵可直接接续。

binding 包含源码和实际输入身份，不含目录路径或预算。超时只保完整文件，不将未完成产品标成已核；共享时钟到时终止子进程并保全部已成检查点。

所有大矩阵和来源只留当前 job 临时目录，不加入 Git、Release 或其他永久存档。永久保存源码、参数、run ID、小回执和 SHA。

## 7. 回执与条件次数增益

主回执：
same-source-koszul29-third-pairing-receipt.json。

主要完成字段：

- all22OriginalSecondCoChainsReverified；
- all287364LowerOriginalProductsZero；
- oldLowerPagePairingRank = 5；
- completeCombined29By58PairingRank；
- restricted22ThirdConnectionRankOverQ；
- completeRestricted22ThirdImageComputed = true；
- allLowerPageKernelFreedomRetained = true；
- quotientRestrictionIsomorphismProved = true；
- completePaired22HeadProjectionDimension；
- fullSelectedThirdRankOverQLowerBound / UpperBound；
- fullSelectedThirdRankExactly3；
- provedThirdHeadSpaceDimensionLowerBound；
- explicitNewLambda3SourcesConstructed = false；
- full24SecondHeadsExplicit = false；
- newM0RightHandSidesSolved = 0；
- originalTargetMembershipProved = false；
- leadingUnitProved = false。

若本轮实得 $r_*=22-b$ 个第三可延头的存在性，则同一所选方阵有
$$
\operatorname{ord}_\infty D\ge93+r_*,
$$
全部 cofactor 及原来源换列子式有
$$
\operatorname{ord}_\infty D_{\rm cofactor/replacement}
\ge90+\max(r_*-1,0).
$$
这是第三头维数经 Smith 阈值计数的存在性推论，不要求提前写出巨大显式 $\lambda_3$。

代码按实际 $r_*$ 及当前 $K_{101}$ 自动列出原非基、转移、目标三个条件成本。若且仅若实际 $b=1$，便得到完整第三秩 3、21 个第三可延头、$114/110/110$ 阶界，以及条件统一费用 8603、目标分支 187。本文没有预填该实际 $b$ 值。
