# R150：两个原坐标 202 映射、同外来源配对与完整高核商接口

作者：Astra-ISP-789f / normal_annihilator。AI 辅助，模型 GPT-6 Astra Pro。

本接口连接已经实际完成的两个正规小映射、两个独立的原坐标 native 运输，以及同一所选来源补集上的高核商。总入口源码仅已作静态逐式审读；本文件不声称总入口已经通过 Python 解析、native 编译或新的数学执行。此前两个小映射的实际结果见 §2。

全部结论限于 $\mathbb F_{31}[[u]]$。本入口不计算特征零高核谱，也不证明所选子式最高系数为 $31$ 单位。

## 1. 冻结源码及依赖

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| 2026-11-15-r150-original-two-mapper-higher-quotient-runner-789f.py | 29018 | b5b2bcd1f5ff2a04c729afcdfb8afea6e09948ce7bdd466a66bc0f90bad7eae3 |
| 2026-11-15-r150-higher-two-regular202-mappers-preparation-789f.py | 22703 | a2e8fa4aa6d26c74b2f8000fb33fcda4b558021ab674582eecbd2c86edb9847e |
| 2026-11-15-r150-original-high202-source-transport-789f.cpp | 23360 | d0748649a3cd280fb620c85c61b82cb9d6c6fabeef8e9db81afaf9b9b01a4b2c |
| 2026-11-15-r150-original-outside202-left-transport-789f.cpp | 12826 | 92e534d74d465f99043ec293bdd5a82a67c661309767e42e476bf765e1244262 |
| 2026-11-15-r150-saturated-global-common-789f.hpp | 11284 | f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1 |
| 2026-11-14-r150-f31-bitplane-789f.hpp | 3030 | 73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec |

路径均在本课题 notes 目录。两个头文件必须与两个 native 源码置于同一个 scripts 目录；总入口编译前复制并逐字节核查。Python 只需已经实际使用的 python-flint 0.9.0 和标准库；两个 native 不链接系统 FLINT。

另一个固定的小输入是：

~~~
notes/r150-full-infinity-dual27-session-789f/
43731615668-full-kernel-deleted-original-output-projection.json
~~~

其字节为 20819，SHA-256 为
28b2605d03746fb5d1a4398c36d22650239d7989f5b68463ed9d6c9f99c5f830。
它保存同一原矩阵、同一 $I,J$ 的已付有限域分解
$$
243=66+2+149+26.
$$
本程序实际校验其中的 native model 和 selected receipt 身份，不能将另一子式的长度移入本入口。

## 2. 当前实际输入

run 43740928483 的 higher-two-regular202-mappers-preparation 已实际完成，执行源为 c3c2932fc50a3b17bca8eaaa7f73fcdd6f11afa8。数学时间为 7.464637823999965 秒。小回执路径为：

~~~
notes/r150-source-kernel-session-789f/
43740928483-higher-two-regular202-mappers-preparation.json
~~~

原临时回执 11358 字节，SHA-256 为
7a65b17569fb81463a06d4318d9088ee94b6635bed4156ce6008558937dcfac6。
实际绑定为
7d781d083a66e7cb2b66426ea47753b7a50e7de5e10426642eb4246de6c46cca。

两个正规映射各有 202 列，均保留 $u^0,\ldots,u^{21}$；高源小映射有 216 行，外来源左映射有 231 行。119988 个高源小系统产品和 128876 个外来源小系统产品均实际为零，两套原自由坐标块均实际为 $I_{202}$。

两个精度损失分别为 $11$ 和 $14$：前者使用独立的 full32，后者使用独立的 O35。因此保留阶是 $32-11=35-14=21$。两种损失没有相加。

本次实际 prepared-two-original-mapper-transports.json 为 34344 字节，SHA-256 为
5a1892f8787b85b788b9e940d11e4ebe597485097df9513e56f2be688dd98555。
两个 head 文件的 SHA-256 分别为：

- high202-native-heads.bin：
  a27ccfcf95192fde8b2c0caff8bd515da30e2bed28f97f1e71a7b655dc074b3d。
- outside202-native-heads.bin：
  0dcdcbf1edb733f92eef1568c3734342eb427b8c8d8eacc6446f08f882878ca1。

总入口不重新计算这些小映射。它检查完整阶段 manifest、所有实际字节散列、原源码身份、父任务绑定及源/余坐标字典，然后消费上述结果。当前两个父绑定是：

~~~
full32:
9e86556a7a82c1c2306b395c87a49a7059d0945f12db7d4962c789717bd35dc6

O35:
f07acb3347e775dc41658f95e015c2e169b4df34c6c1e829a2737fe83acb2781
~~~

## 3. CLI 和预算

~~~
python 2026-11-15-r150-original-two-mapper-higher-quotient-runner-789f.py \
  --mapper-source {scripts}/2026-11-15-r150-higher-two-regular202-mappers-preparation-789f.py \
  --source-native {scripts}/2026-11-15-r150-original-high202-source-transport-789f.cpp \
  --outside-native {scripts}/2026-11-15-r150-original-outside202-left-transport-789f.cpp \
  --native-model {native_model} \
  --paid-projection-summary {scripts}/43731615668-full-kernel-deleted-original-output-projection.json \
  --prepared-out {work}/higher-two-regular202-mappers \
  --full-out {work}/full-infinity-natural-dual-schur-through32 \
  --outside-out {work}/koszul-outside-natural-through35 \
  --out {work}/original-two-mapper-higher-quotient \
  --seconds 600 \
  --compile-seconds 30 \
  --memory-mib 1024 \
  --through final
~~~

共享数学预算为 600 秒，两个首次 native 编译各有 30 秒上限并单独记时，地址空间限制 1024 MiB。建议外层墙钟 700 秒。编译命令为 g++ -std=c++17 -O2。既成编译由源码、头文件、编译选项及实际 binary SHA 绑定并复用。

可以先以 --through transports 运行两个完整原坐标运输，之后使用相同源码、参数、目录及 --through final 继续。through 和秒数不参与数学绑定，因此这一顺序不重算完成的 native 或既成配对层。不得换源码后伪装成同一缓存。

原数据始终在同一 Actions job 的临时目录。长期只保存小源码、参数、实际 run、回执和散列。

## 4. 两个原坐标 native

高源 native 从完整 4340 常单位的原 F/B/G 轨迹出发，保留 3333 预基的真实降 moment 次数尾及 1007 后继单位块。它将 216 行小核回填到 6188 个原来源坐标。第 $d$ 层完整核验
$$
\sum_{i=0}^{\min(10,d)} A_i K_{d-i}=0
$$
的全部 $4367\times202$ 个坐标，并核实际 1848 尾坐标和 202 个自由坐标，之后才提交该层。$d=0,\ldots,21$ 共计 19406948 个原输出产品。

外来源左 native 使用 O 的同一 1603 常单位。其回填矩阵是 $U_0^{-T}$，不是 $U_0^{-1}$。第 $d$ 层对完整 $1834\times202$ 左核 $\Lambda_d$ 核验
$$
\sum_{i=0}^{\min(10,d)} O_i^T\Lambda_{d-i}=0
$$
的全部 $1632\times202$ 个坐标，并核全部 231 个原尾坐标和 202 个原自由坐标。22 层共计 7252608 个原 Koszul 产品。

各 native 在每一完整层后保存原坐标系数、完整零产品及原子 ledger。总入口重新核实际每个文件的 SHA、field header、所有零产品及整个自由单位块。完成的 native 不再启动编译或运输；时间耗尽时从最后完整层继续。所有原始 F/B/G、O 系数、常逆和 head 输入同时绑定，恢复目录的绝对路径不构成数学身份。

## 5. 同一外来源补集上的高核商

令 $J^c$ 是同一所选 4354 原来源的 1834 元补集。总入口从两个实际原坐标数组生成
$$
D(u)=\Lambda_O(u)^T K_H(u)|_{J^c},
\qquad D\in\operatorname{Mat}_{202}(\mathbb F_{31}[[u]]).
$$
具体逐项计算
$$
D_d=\sum_{i=0}^d \Lambda_{O,i}^T K_{H,d-i}|_{J^c}.
$$
同一有序 $J^c$ 的字典由原模型和 selected receipt 形成并已经核过；程序继续检查该有序列表的散列，不能只按两矩阵行数相等直接相乘。

完整模块解释是
$$
\ker A=\operatorname{im}\Phi
 \oplus j\!\left(E_{216}\ker(SE_{216})\right).
$$
这里 $\Phi$ 是原 1632 条真实 Koszul 曲线，原常项 1632 单位子式和全 216 补列已付。两个正规映射都是用实际单位 Schur 与回代获得的形式核基，原自由块为单位。因此 $K_H$ 给高核直和项的完整基，而 $\Lambda_O^T$ 满射、核为 $\operatorname{Sat}(\operatorname{im}O)$。由此 D 的 cokernel 正是本次所计算的完整高核商；没有把某个任意 202 列独立子族冒充完整模块。

原 $32/35$ 精度按各自已经付清的逆极点得到两映射的 0…21 项；相乘不会再损失精度。原常单位回填也不再除 $u$。

## 6. 实际停止门槛和小 Schur

先实际计算 $D_0$ 的秩 $r$、主元行列及 $r\times r$ 单位逆。剩余 $k=202-r$ 个方向均有正 Smith 指数。已付总阶 26 因而要求 $1\le k\le26$，但 k 的实际值不预填。

随后逐阶求规范源图 $Y(u)$，使所选 $r$ 个单位行的 $D(u)Y(u)$ 严格为零，自由源坐标严格为 $I_k$。每个完成阶都保存完整 $D_d$、$Y_d$、202 行产品及原常单位 profile。只对余下 $k\times k$ 系列做逐层单位 Schur；每次除 $u$ 之前先核整个常数 Schur 块为零。

程序只有在全部 k 个正方向都实际退出后才认为谱完整。它不以“目前累计长度等于 26”替代这个秩覆盖门槛。最终仍检查完整正谱的总和严格为 26，且最大正指数不超过同一所选子式给出的 21。若实际在较小阶已经完成，就停止新的配对卷积；不为凑到 21 重算无用阶。

这个 cutoff 可在同一原选择下直接说明：原泛像在所选 $I$ 坐标上的投影单射，故 $\ker A_I=\ker A$。由所选来源列与其补集的精确序列，$\operatorname{coker}\Psi$ 嵌入 $\operatorname{coker}B_I$，而高核商是前者模外 Koszul 扭子的商。因此它是同一 $\operatorname{coker}B_I$ 的子商。已付所选矩阵最大正指数 $21$（本次父 full32 回执的 paidSelectedMaximumExponent31=21）杀此高核商，证明截止充分。有限域中已知总长 $26$ 用于约束和交叉核查；没有把该数字用作特征零输入。

## 7. 回执与恢复

主回执名为 higher-original-two-mapper-quotient-receipt.json。

--through final 成功时：

- status = completed；
- outcome = complete-original-higher-kernel-field-smith；
- completeOriginal202SourceTransport = true；
- completeOriginal202OutsideLeftTransport = true；
- all19406948OriginalSourceProductCoordinatesVerified = true；
- all7252608OriginalOutsideProductCoordinatesVerified = true；
- higherQuotientActuallyComputed = true；
- completeHigherKernelSmithComputedModulo31 = true；
- completeOriginalHigherKernelModuleJustifiedModulo31 = true；
- higherKernelPositiveExponents 为实际正谱；
- higherKernelTorsionLengthModulo31 = 26；
- highestActuallyPairedDegree 是实际停止阶。

--through transports 的成功 outcome 为 complete-original-two-mapper-transports；此时 higherQuotientActuallyComputed=false。

时间耗尽退出 75，status=budget-exhausted，outcome=checkpointed-original-higher-kernel。任何输入、乘回或算术身份不符退出 1。程序保留具体异常及日志尾，不将失配包装成数学否定。

同目录继续时，两个 native 分别按完整原 ledger 恢复；配对按 complete-quotient-layer-ledger.json 的连续完整阶恢复。已保存的常单位逆、D/Y/完整产品和输入散列全部核对。整个数组仅临时保存，不进入 Git 或 Release。

以下字段始终为 false：characteristicZeroHighSmithComputed、characteristicZeroFullSmithComputed、selectedLeadingCoefficientUnitProved。即使本步所有有限域身份通过，也不改变这三个范围。
