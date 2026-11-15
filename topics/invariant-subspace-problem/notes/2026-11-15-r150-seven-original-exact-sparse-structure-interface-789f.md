# 原七方向有理求解的精确稀疏剥离与结构分块接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15 UTC。

**当前状态：算法与来源保持证明已完成；本入口尚未执行。** 它接已完成的原整数输入和真实单位行列，不重新运行模 31/65521 消元，不重算正常形，不预报分块规模。

## 1. 为什么有一个新的可执行入口

run 43679903558 的 seven-original-exact-rational 实际在 592.119801265 秒后结束，内部 fmpq Dixon 求解到 580.83246211 秒时被共享期限终止。它没有返回有理解，没有新增真核。

以下两个实际文件已经完整保存于该 job 临时目录：

- seven-original-integer-core.json.gz：1497227 B，SHA256 5cd0c5430089a3d4431ef6d058ec36a55d084d70e311cf13790fd60a5457efcc。
- seven-original-unit-row-profile.json：62084 B，SHA256 43cd638dfe13978f375490db9afdca5f318e137a384820b69bbc74b0ce48a7df。

原 binding 为 74bf887ac9ce134b551b8957061bc713cded79bd6a88e7a35fe8faa3101bb58c。它们包含原 4367 输出、删除已付前 29 个自由来源后的 4325 原来源，以及真实 4318 个单位来源和原 $I$ 内的 4318 个单位输出。这个 $4318\times4318$ 原整数方块 $U$ 的行列式模 65521 非零，故在 $\mathbb Q$ 上可逆。七个其余来源构成同一右端 $E$，待解系统为 $UX=E$。

本入口从这两个原字节文件出发，只做精确低支撑消元和结构分块，目的是把一次大有理求解改为若干真实较小块；是否确实变小由本次运行决定。

## 2. 一项或两项来源行的有理等价消去

假设当前一行是

$$
a x_j+b x_k=e,\qquad a\ne0,
$$

其中 $e$ 同时保留七个右端；单支撑时省略 $b x_k$。保存这一整行作为逆代记录，然后对其他含 $x_j$、系数为 $c$ 的行 $r$ 作

$$
r\longmapsto a r-c\,(\text{枢轴行}).
$$

右端作完全相同的变换。所得行再除以其全部系数及七个右端的整数 gcd；这只乘一个非零有理标量。删除枢轴行和变量 $x_j$ 后，原系统与剩余系统之间有严格双射

$$
x_j=(e-bx_k)/a.
$$

逐步保存原来源编号、原输出编号、真实 $a,b,e$，逆序代入即可恢复全部原单位来源。每一步对有理系统合法，不要求 $a$ 是 31 单位，也不把旧有限域预基系数解释成有理系数。当前方块已付可逆，因此精确消去不可能留下零系数行。

保存的 reduced-core 文件保留全部剩余整数行、七右端和完整逆代 DAG。时间到时也写实际已完成的整步状态，不把部分状态称为完整分解。

## 3. 纯支撑匹配和强连通分块

对剩余可逆方块的非零支撑做完美匹配。这个匹配只决定行列排列，不把所匹配的单个数值当作 Gaussian 枢轴。

将某行匹配到的来源作为该行的节点；从它向该行其余非零来源作有向边。每个强连通分量对应一个方阵块。不同分量之间的依赖图无环，程序保存“所有被依赖块先求解”的确切次序，并逐条核验每个非对角非零项遵循该次序。

这样重排后的整个方块为块三角形。由于原方块及精确剥离后的方块均可逆，每个对角块在 $\mathbb Q$ 上可逆。这是原方程的精确分块，不是根据模秩或估计的谱作近似。

它不要求相同乘子次数的来源只能连到同一次数输出。程序另外报告原来源次数及原输出次数的分布，以判断实际分次结构；不会把这种统计分布当作已经证明的三角性。

## 4. 固定命令和输出

源码：

2026-11-15-r150-seven-original-exact-sparse-structure-789f.py

源码 SHA256：

~~~text
b61ec2545cd66cfc22ec0cdade64431bdf505ad130620f25c178f5244ddf2d13
~~~

在同一 job 中的命令为：

~~~sh
python -B SCRIPT \
  --core WORK/seven-original-exact-rational/seven-original-integer-core.json.gz \
  --profile WORK/seven-original-exact-rational/seven-original-unit-row-profile.json \
  --out WORK/seven-exact-sparse-structure \
  --seconds 30 --memory-mib 512
~~~

共享结构计算预算 30 秒，每进程地址空间 512 MiB。没有 native 编译，没有数学外的独立复核门槛。根已完成源码阅读、AST及SHA核验；数学执行仍待实际回执。根仅把次数/块尺寸的简短元数据同步放入parameters，确保现有保存器完整保留这些结果，未改变消元或匹配算法。

主小回执为 seven-original-exact-sparse-structure-receipt.json。status 为 completed、budget-exhausted 或 failed。全部 events 项是对象，兼容现有 remote-session 的小回执保存器。

真实临时文件：

1. seven-exact-peeled-core-and-backsubstitution.json.gz：完整原来源映射、原七右端、剩余整数矩阵、逆代 DAG 和已成匹配状态。
2. seven-exact-structural-blocks-and-order.json.gz：完整匹配、各块来源/输出编号及依赖次序。

回执只长期保留参数、输入和输出 SHA、实际剥离数、块尺寸分布、最大块、次数分布及实际时间。大工作文件仍只在当前 job 临时存在，遵守仓库规则 15。

## 5. 下一真实求解的边界

若得到有用分块，按依赖顺序逐块求解原七右端，并将每块的确切有理解及时保存；全部块完成后按逆代 DAG 回到原 4318 单位来源。之后仍接原七方向流程的全部 4367 整数残量、七残量的完整有理核、6188 原来源支撑和 36 自由坐标独立性检查。

若分块没有缩小，回执只说明这一次精确低支撑/支撑分块没有收益，不说明七个有理核不存在，也不说明原大 Dixon 已经足够或不可能完成。原 29 真核和现有秩区间保持原样。
