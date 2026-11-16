# 原加权九次矩阵的七元域逐原行秩接口

作者：Astra-ISP-789f / normal_annihilator（AI-assisted：GPT-6 Astra Pro）  
日期：2026-11-16

## 1. 完整范围及严格门

本入口保留全部十七个原梯度、全部十七个变量，以及原 Bell 三次幂在固定三次数域基 $1,d,d^2$ 中的三个有理分量。它独立于现有 direct9 标准基任务。

令 $M_9$ 为原权九来源矩阵，$c_0,c_1,c_2$ 为三个目标，则

$$
M_9:49368\times16442,\qquad
\widetilde M_9=[M_9\mid c_0,c_1,c_2]:49368\times16445.
$$

全部来源依次为十一条四次梯度乘全部 $1264$ 个权五单项式，以及六条五次梯度乘全部 $423$ 个权四单项式。已付 $396$ 条独立原 Koszul 关系给出

$$
\operatorname{rank}_{\mathbf Q}M_9\le16046.
$$

准确来源为 R150-appendix-original-weight-nine-koszul-rank-ceiling-and-rigorous-cube-obstruction.md；七元域系数资格和完整字典见 R150-appendix-original-bell-cube-prime-seven-admission-and-complete-weight-nine-dictionaries.md。

消费者仅在真实已处理原行的增广秩达到 $16047$ 时置 rationalCubeNonmembershipCertified。全部原系数为 $7$ 整，故这是原有理增广矩阵秩的下界；剩余行不能降低它。因此可以在阈值处结束，不必处理全部 $49368$ 行。

较小的前缀秩或较小的完整有限域秩均只作诊断，不转为有理成员或非成员。三个分量的合并门不声称每个分量都不在像中；只要有一个分量不在原有理像中，就足以排除原数域 Bell 三次幂。

## 2. 冻结源码

| 文件 | Git blob | 字节数 | SHA256 |
|---|---|---:|---|
| notes/2026-11-16-r150-original-weight9-prime7-stream-rank-789f.py | af9c7e4444dd101390417f917c2a5df9a0385279 | 22588 | 088c82c0d7198fcde9f4c9370aed8003957b3514bab51e4f5daa91875583c86f |
| notes/2026-11-16-r150-original-weight9-prime7-stream-rank-native-789f.cpp | 28539890e07fc69cb4a033bbd013d81a2f113f66 | 19143 | 11b82abe88ca35e698d6860aef94de49809d8b836a34668869e263db30f67e4b |
| notes/2026-11-16-r150-original-weight9-prime7-stream-rank-inputs-789f.json | 8290d3d6120eadfbec1a6dcd2e5e9dfc32de2ba7 | 3343 | b7669b555644c911787fd38c31490258b14be4e7dfeb03f3823eae0653284836 |

编译命令为 g++ -std=c++17 -O3 -march=native。实际编译器版本、二进制完整 SHA 及小测试回执另存运行身份。

数学绑定包含两份实际源码、原完整模型与字典 SHA、维数、素数、阈值、输入和状态协议。预算与临时绝对路径不进入数学绑定。源码改变必须使用新绑定；不能冒用旧检查点。

## 3. 原完整模型

父系数审计绑定为

~~~
4baed1013b72717e2773607c308a3f534b029c92f35592dcb6c5ff1025587339
~~~

父小回执为 $4312$ 字节，SHA 为

~~~
1cee8383ede9f0a458cb37ce5a384e461fdc51f20c81747411ae650df8cf4cda
~~~

临时完整模型 complete-original-weight9-prime7-model.json.gz：

- 压缩 $16999356$ 字节，SHA fe91efd8d4739de90b831449c40020a98e3b9775ee28a7e678a7b29ff2b683bd；
- 逻辑 $58953007$ 字节，SHA df9fb9657926a52a4c3c1a895a0ba5aa34f2d5f537d747d7f07e00d42f81bdfa。

诚实重算可改变父回执时间。消费者固定父状态、数学绑定、全部原门与上述完整模型字节，另记录此次父回执的真实 SHA，不改写新时间来冒充旧运行。

消费者再次逐项检查全部 $134399$ 个原有理系数：分母必须是 $7$ 单位，约化值必须逐项等于保存的有限域记录。还完整检查：

1. 十七原梯度、加权 Euler 及三个 Bell 分量的原多项式身份；
2. 输出、四次来源乘子和五次来源乘子的完整 SHA、无重性与原权；
3. 原匹配三次式模七升幂系数 $[6,0,6,1]$，七个值 $[6,6,3,3,5,1,4]$；
4. 原 $J_3$ 行列式模七为 $1$；
5. 三个原 Bell 三次幂有理分量的完整系数。

本三次式在 $\mathbf F_7$ 上不可约。此入口不把模 $127$ 的线性根 $d=100$ 搬到模 $7$。

## 4. 全部原矩阵的构造

六个 $y$ 指数各用四位、十一个 $H$ 指数各用三位编码。所有乘积的权都是 $9$，故 $y$ 指数至多 $9$、$H$ 指数至多 $4$；相加代码没有指数槽间进位。该编码在完整输出字典上实核单射。

对每条原梯度、每个原乘子、每个非零系数，程序确定其原输出坐标，检查此矩阵位置此前为零，再插入规范值 $1,\ldots,6$。三个目标同样逐项插入。所有来源列标签的完整 SHA 另存。

在任何秩计算前，先完整写全部 $49368$ 行。协议为：

~~~
magic  : R15M9071
header : uint32[8] little-endian
         [1,7,49368,16445,16442,3,257,16047]
binding: 64 ASCII hex bytes
rows   : 49368 blocks of 3*257 uint64 little-endian words
~~~

完整输入大小为

$$
104+49368\cdot3\cdot257\cdot8=304501928.
$$

每个系数的三位面值 111 禁止；尾部未用位必须为零。先全文件写完、同步、原子改名，再核完整 SHA 和保存完整输入清单。没有完整清单的半成品不能恢复。

## 5. 算术、自测及原子式

native 自测全部 $49$ 个域加法与 $49$ 个域乘法。八个独立小矩形包含依赖行、领先空列和后到的较早主元；位面秩与独立标量高斯秩相等，原选中方阵的标量行列式也与保存主元系数乘积相等。另核 SHA 空串与 abc 两个已知值。

真实原行按序读入，每次取消主元后都实核该原坐标为零。新主元保留原行、原列、规范前系数及完整规范行。

到达顺序中的主元列未必递增。把选中行和同名主元列同时按领先列排序，规范方阵为单位上三角，两次相同置换的符号相消。原操作只加先前行；所以规范前系数的乘积就是到达顺序下真实原方阵的行列式。程序保存实际非零模七值，不只保存秩数字。

因为三个目标排在全部原来源之后，目标主元行在全部来源列上为零。它不能增加来源投影秩。因此 sourcePivotCount 确是已处理原行的原来源矩阵秩；仍硬核它不超过已付 $16046$ 上界。

## 6. 整行事务与恢复

两槽为 complete-row-state-slot-0.bin 和 complete-row-state-slot-1.bin。状态协议 R15M9S71 包含原尺寸、数学绑定、完整输入 SHA、已处理行数、主元数、取消次数、原子式值，以及全部主元数据。头长 $204$ 字节，每主元长 $12+3\cdot257\cdot8$ 字节。

只在完整原行处理后保存。先全写新槽、同步、改名、核完整 SHA，再替换 native-state-manifest.json。恢复时核：

- 全部字节 SHA、协议、绑定、原输入 SHA 和完整字节数；
- 原行标签严格递增，主元列互异；
- 全部系数范围、主元领先坐标与单位值；
- 保存主元系数乘积，以及没有隐藏尾字节。

即使旧状态已经达到阈值，外层仍调用 native 的完整恢复和终止门，不仅凭 rank 字段跳过验证。输入文件也重新核完整 SHA。

## 7. CLI、预算与范围

~~~bash
python 2026-11-16-r150-original-weight9-prime7-stream-rank-789f.py \
  --audit-receipt AUDIT_OUT/original-bell-cube-complete-prime7-coefficient-audit.json \
  --audit-out AUDIT_OUT \
  --native 2026-11-16-r150-original-weight9-prime7-stream-rank-native-789f.cpp \
  --out WORK/original-weight9-prime7-stream-rank \
  --seconds 600 --memory-mib 2048 --through final
~~~

600 秒是整体预算，包含完整再次核验、编译和输入构造；native 只获得扣除这些费用并预留保存时间后的实际余量。through=input 只付完整原输入，没有大秩结论。

预算退出为 75；续接须同源、同输入、同 out 和同绑定。只有完整输入与完整原行事务可复用。内存、格式、原核验和预算失败分别记入 parameters.error。预算退出不等同数学负结论。

矩阵位面约 $291$ MiB；最大主元数组约 $97$ MiB。启动 native 前释放大型 Python 构造数组。$2$ GiB 是实际硬界，接口不承诺每次预算都处理完全部原行。

主回执为 original-weight9-prime7-stream-rank-receipt.json。实际结论必须以其全门、实际范围及完整原文件身份为依据。本接口不硬编码任何运行结果。

全部模型、位面和状态数组只留临时；仓库仅存源码、参数、执行身份、输出大小与 SHA，以及完整证明。
