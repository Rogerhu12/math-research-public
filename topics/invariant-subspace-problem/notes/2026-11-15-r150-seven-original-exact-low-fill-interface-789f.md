# 原 4292 核的有界精确低填充续算合同

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。2026-11-15 UTC。

本入口从已完成的 26 步精确剥离直接继续，不重复构造原矩阵、模 65521 选元、强连通分解或未完成的大有理求解。

## 1. 唯一实际输入和预算

输入为同一 job 的

~~~text
seven-exact-sparse-structure/seven-exact-peeled-core-and-backsubstitution.json.gz
~~~

它是 1605177 B，SHA256 为 9032a239fd7e0ff617f8248181b3caa72f8689472df4ec836ce40629b187f47f，parent binding 为 808f8f923a6787ef2f9c7044a2238cf73add420c004d02cb4370f317ee65650a。输入包含真实 4292 方块、七右端、原 4325 来源字典及已有 26 条逆代记录。

固定命令：

~~~sh
python -B SCRIPT \
 --state WORK/seven-exact-sparse-structure/seven-exact-peeled-core-and-backsubstitution.json.gz \
 --out WORK/seven-exact-low-fill \
 --seconds 30 --memory-mib 2048
~~~

实际数学期限预留最后 3 秒给保存；完整工作数组的压缩用时另在 checkpointSeconds 如实报告。所有长期文件仍只是源码、小回执、参数和 SHA。

## 2. 精确运算与预先固定的启发式

先把每行的系数和七右端除以它们的整数内容。之后只在当前最稀的 64 行中选择候选项，按

$$
(\text{行非零数}-1)(\text{列非零数}-1)
$$

排序，依次检查前 128 个候选的实际更新工作量。这是固定的低填充启发式，不声称取得全矩阵的最优 Markowitz 枢轴。

当前枢轴行为

$$
a x_j+\sum_{k\ne j}b_kx_k=e,\qquad a\ne0.
$$

另一行的 $x_j$ 系数为 $c$，令 $g=\gcd(a,c)$。该行及全部七右端作

$$
r\longmapsto (a/g)r-(c/g)(\text{枢轴行}).
$$

这严格消去 $x_j$，只作非零有理倍的可逆行变换。结果按整行内容约去，再保存枢轴行的完整逆代式。源变量仍是同一原 4325 来源中的坐标，没有新建不受控来源。

## 3. 三个实际门槛与整步提交

默认门槛预先固定为：

| 门槛 | 值 |
|---|---:|
| 剩余矩阵非零项 | 500000 |
| 任一新行的系数及七右端整数高度 | 4096 bit |
| 单次枢轴预计更新工作量 | 60000 |

工作量按所有受影响行的真实支撑长度、枢轴行长度及七右端计算，不假设每个大整数操作耗时相同。

每次消元先在独立 pending 数组中算出所有新行及七右端；期间随时检查真实期限。只有整个枢轴更新完成、且所有门槛通过后，才一次性改动当前矩阵、来源索引和 DAG。若时间或门槛在中途到达，丢弃这一次未提交更新；之前所有已提交枢轴仍形成完整的精确有理等价系统。

因此不会留下只改了一半的行变换，也不会把部分新行称为可续的完整状态。保存文件记录每个实际已完成的枢轴及当前全部整数数组；其原有 26 步不会重做。

## 4. 输出、恢复范围与后续核验

主小回执：

~~~text
seven-exact-low-fill-receipt.json
~~~

status 为 completed、completed-bounded-compression、budget-exhausted 或 failed。达到填充或高度门槛只是这条有界压缩路径停止，不是原有理核不存在。

完整临时状态：

~~~text
seven-exact-low-fill-core-and-backsubstitution.json.gz
~~~

它包括原 4325 来源映射、全部剩余整数系数、七个真实右端、已有及新增全部逆代 DAG、原输入身份和本次 binding。后继可直接接这个最后完成状态；尚未实现下一调用时，不冒称已经运行恢复。

若剩余核确实缩小，下一步才对它求确切有理解并逆代到原 4318 单位变量。最终仍须回到原七方向流程，支付全部 4367 整数输出残量、七残量的完整有理核、6188 来源支撑及完整自由坐标秩。压缩本身不产生新的核或新的特征零秩。

冻结源码 SHA256：

~~~text
b89a0f97efb30d5fcc865a2aa498a6407941d6355999df2259ff440333c06a53
~~~

源码在本合同冻结时尚未声称执行或通过 AST；实际入口会保存真实状态。
