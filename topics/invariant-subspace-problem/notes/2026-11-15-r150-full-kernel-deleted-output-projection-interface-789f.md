# 同一所选输出补集上的十三维形式核投影：实际数据消费者

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。
日期：2026-11-15。

## 1. 范围和已付输入

本入口使用 run 43731615668 已实际完成的两个有限域结果：

- 完整原自然无穷矩阵 $A(u)$ 的正 Smith 指数
  $1^4,3,4^3,5,6,7,8,10,11$，总长 $66$，最大值 $11$，
  完整形式左核秩 $13$；
- 同一所选原来源集 $J$ 的原 Koszul 外支撑矩阵 $O(u)$：
  正指数总长 $149$，最大值 $14$。

同一原方阵 $B=A[I,J]$ 的有限域长度 $243$ 也已付清。
本入口仅在 $\mathbf F_{31}[[u]]$ 上定位这三项之间的剩余长度 $28$，
不计算特征零投影，不宣称特征零最大指数为有限域最大指数，
不宣称所选多项式子式的最高系数为 $31$ 单位。

源码已经冻结，数学执行及首次 Python 解析由 Actions 完成。
本文不是执行成功回执。

## 2. 两个源码与兼容续接

主消费者：

- notes/2026-11-15-r150-full-kernel-deleted-output-projection-789f.py；
- blob c6392b08ccc29256007c93219de515371dcd96fc；
- $28000$ bytes；
- SHA256 16767d899ff5ad34afca4bd647d344ace846fa8d084c17a04d475718311997e3。

有界续层 native：

- notes/2026-11-15-r150-full-infinity-natural-dual-schur-through39-789f.cpp；
- blob ab69a115841f36b3674a9891f5448b0fb7992f94；
- $21017$ bytes；
- SHA256 54631a695dbd6dc41c446c8c3ab60ba527c5dd4f34fbe70187cdd0613caef1fb。

这个 C++ 文件相对已成功的 v2 native，只把请求次数门槛从 $21$ 改为 $39$。
主消费者实际逐字节验证除此之外完全一致。原递推、预基尾项、
反序转置运输、完整行乘回、二进制格式、原 profile 和原 ledger 均不改变。

旧数学 binding 保持

3e51cbe960ac668c9addb12be36856d2aaf13686f5acc15571317ccf3dd7d2ad。

新消费者将自身源码、新 native 源码、允许的唯一差异、实际输入和原 binding
合成另一个语义 binding，并明确登记真实执行源码，不能将新执行文件冒称旧文件。
全部 $66$ 个已完成的 $0,\ldots,21$ 层来源、残量和 Schur 文件，续接前后逐件
核其原 SHA256 不变。

两个原 header 与 v2 相同，放在新 native 源码同目录：

- 2026-11-15-r150-saturated-global-common-789f.hpp；
- 2026-11-14-r150-f31-bitplane-789f.hpp。

若已有完整 G 结论可从旧层得出，根本不进入编译和续层。
若需要续层，则实际 native 从原完整 ledger 恢复，仅计算缺少的新层。
没有新的 $4340$ 阶 Gaussian 消元。

## 3. 同一 $I^c$ 的原坐标核验

程序重新解析原 native 的全部 $3333$ 个预基字典，结合原 selected receipt 中
$1021$ 个原输出组件及单项式键，形成同一 $I$，再取其原输出补集 $I^c$。
它核验所有所选单项式键，而非只比较维数。

实际字典给出 $I^c$ 在已付 $27$ 个自由输出坐标中的序号

$$
[4,5,9,10,13,14,16,17,22,23,24,25,26].
$$

完整形式核的 $13$ 个自由头序号为

$$
[4,5,9,10,13,14,15,16,17,23,24,25,26].
$$

两者共有 $12$ 个坐标，只把自由头 $15$ 换成头 $22$。
这些是原 $27$ 头序号，不是原输出行号；回执同时保存真实原输出行号和单项式键，
防止混用。

设 $L(u)$ 为已付 $4367\times27$ 系列，始终保持其 $27$ 个原自由输出块为恒等。
设 $N(u)$ 为 $27\times13$ 正则形式核图，且选定 $13$ 个自由头块为恒等。
则

$$
K(u)=L(u)N(u),\qquad
G(u)=K(u)[I^c,:]=N(u)[I^c\text{ 的头序号},:].
$$

因此 $\det G$ 仅为 $N_{22,\operatorname{free}15}$ 乘一个常数符号。
程序实际计算该 $12$ 阶单位 cofactor 的符号，并逐层核验其余 $12$ 行恒等；
没有只凭列表声称该标量等式。

## 4. 十一阶精度损失

已付小 Schur 系列 $S(u)$ 的形状为 $1848\times27$。
使用原成功计算记录的 $14$ 个原行、$14$ 个原头，记对应方块为 $S_{R,C}$，
其余 $13$ 个头为 $F$。解

$$
S_{R,C}X+S_{R,F}=0,\qquad
N=E_F+E_CX.
$$

消费者只对这个实际 $14$ 阶方块作单位分块递归。
每次先核完整单位逆、完整 Schur 常数和右端常数，再除 $u$；
回填保原行列顺序。它重新核出相同的十四个正指数，
所以逆的最大极点为 $11$。

若原 $S$ 已知至 $u^n$，本入口只声称 $N$ 已知至 $u^{n-11}$。
从原 $0,\ldots,21$ 层首次得到 $N$ 至 $u^{10}$。
若标量已经非零，即可确定 G 的完整谱。
若仍全零，则仅续原 native 至 $u^{39}$，得到 $N$ 至 $u^{28}$。
不把 $28$ 阶 $N$ 冒称为已核至 $39$ 阶的完整形式核。

原精确序列的有限域长度分解给出

$$
243=66+\lambda_I+149+\delta_{\mathrm{high}},
\qquad
\lambda_I,\delta_{\mathrm{high}}\ge0.
$$

故 $0\le\lambda_I\le28$。因此通过 $28$ 次系数仍全零应判输入或实现失配，
不能将其登记为一个“更高长度”结果。

## 5. 全原身份和真实输出

每一层读入原 $L$、完整 $6188\times27$ 残量及 $1848\times27$ Schur，
逐件核 SHA256，并核：

- 全部 $4340$ 个原单位来源残量为零；
- 全部 $1848$ 个小行确是完整原残量中同一尾来源行；
- 全部 $27$ 个原自由输出块在整条系列中恒等。

随后实际核

$$
\sum_{i=0}^k S_iN_{k-i}=0
$$

的全部 $1848\times13$ 坐标。结合上述原 $4340$ 单位行，
这付清全部 $6188\times13$ 原来源方程至当前保留次数。
原乘积坐标数按实际次数记录，不沿用 $39$ 次作为未经核验的精度。

程序保存实际

$$
K_k=\sum_{i=0}^k L_iN_{k-i}
$$

的全部 $4367\times13$ 坐标，并核其原 $13$ 自由输出块及真实 $I^c$ 投影。
每个完整 K 层、N 层和 G 层均原子保存，带 child binding 和 SHA256。
恢复时先核已完成层，不重复完整原乘积。

成功后输出：

- outputProjectionTorsionLengthModulo31：$\lambda_I$；
- outputProjectionPositiveExponents：若 $\lambda_I>0$，只有该一个指数；
- outputProjectionUnitFactorCount：$12$，若 $\lambda_I=0$ 则为 $13$；
- selectedOutputDeterminantalLengthModulo31：$66+\lambda_I$；
- remainingHigherKernelQuotientLengthModulo31：$28-\lambda_I$；
- 所有实际标量系数、符号、原坐标字典和完整身份门槛。

上述两个剩余长度仍只在有限域中。特征零原始左核的模 $31$ 平坦运输未经本入口证明，
因此不能直接以有限域的 $\lambda_I$ 作为特征零同量的上界。

## 6. CLI、预算和恢复

建议实际命令参数为：

    --full-out {work}/full-infinity-natural-dual-schur-v2
    --outside-out {work}/koszul-outside-minimal-field-smith
    --native-model {native_model}
    --selected-receipt {work}/inputs/repo/selected-infinity-minor-dag-receipt.json
    --original-native-source {scripts}/2026-11-15-r150-full-infinity-natural-dual-schur-v2-789f.cpp
    --extension-native-source {scripts}/2026-11-15-r150-full-infinity-natural-dual-schur-through39-789f.cpp
    --out {work}/full-kernel-deleted-output-projection
    --seconds 180 --memory-mib 1024 --compile-seconds 30

实际 full 与 O 回执分别固定为：

- $21358$ bytes，
  SHA256 540fd2d44e7d49f9d4284d8966e9994397320f145e353c1560c7807f76caf9b4；
- $15832$ bytes，
  SHA256 eeddfe8782d06338d15d834bdf387de5cd2f85d8334415f59411d24bfca244a6。

主回执名称为 full-kernel-deleted-output-projection-receipt.json。
成功状态 completed，对应 outcome 为 complete-original-deleted-output-projection，
退出 $0$。时间到或完整前缀退出 $75$，保最后完整 native ledger 与已完成原核层；
身份失配退出 $1$。原失败回执、旧成功原数据和新执行源码均单独记录。

仅小源码、参数、run、回执和散列可永久登记。所有可重建矩阵与二进制层只保留在
本次临时 job；没有跨已结束作业取回旧数组的假设。
