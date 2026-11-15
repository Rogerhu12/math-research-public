# R150：从真实 p486 继续的最小 Actions 接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。
日期：2026-11-15。

状态：已冻结新入口代码和输入合同；当前执行环境不可用，**没有对本入口作本地 AST、编译或数学运行**。已完成的旧计算到真实 p486，共23个完整原4367输出的精确有理核。新入口从该实际来源继续，不将原请求上限512误作已完成指数。

本接口遵守已读根 README 提交1063ed7dbb24b7a0422d72714b5b335511f6b226：可重算的大数据不长期保存在 Git、Release 或 Actions artifact；只发布小回执、源程序、参数、run编号和 SHA256。当前工作文件只在同一次 job 的临时目录中使用。

## 1. 先运行23核来源闭包，满36则跳过 Dixon

先按来源闭包程序检查已知23个真核的低次数子空间及其一次变量乘法，并保完整选列之外的消去约束。只有实际得到36个在同一4354列上支撑、原自由坐标矩阵可逆的真来源，才能由源级恒等式推出常数秩4318并跳过 Dixon。

闭包源码的冻结 blob 为52fc2fb36f3a1f5c8d9d8b18e863218f46aafee2，作者是并行代理 literature_audit。它尚未对新23证书执行。不能把自由坐标本身的次数当成完整来源向量的次数，也不能把模31组合直接当有理组合。

若未闭合36，调用本入口；它只读旧23证书和原p486来源，不依赖闭包可能产生的新候选核。

## 2. 准确旧输入与历史定位

完整机器可读位置清单为
2026-11-15-r150-selected-infinity-resume486-input-locations-789f.json，
blob c5a4bcc0fe8d182b641fe0cc2704dc962b42056d，
6251 B，SHA256
8b32fc742ec8b767beec7e1f1a614b8fd455f8814efd1aeeca73cdc3d0f9c6d4。

其中8项旧输入统一从历史提交

8c6304e273e64b0544d3dd58bc0e48a672a87c36

临时读取。它们在新规则清理 main 之前已实际保存，路径和哈希已通过旧小 manifest 核定。不要在新 main 找不到数据时重新生成旧数学。

| scope | 文件／用途 |
|---|---|
| repo | 原 native-normal-form-input.txt、nf-forward.bin.gz、nf-backward.bin.gz |
| paid | 同一 selected-infinity-minor-dag-receipt.json |
| bockstein | 原整数无穷远点模型、原36核和旧 Bockstein 小回执 |
| dixon | 已付985单位来源的完整 source DAG |

scope 路径必须恢复为位置清单的相对文件名；repo scope 的前三项保留 r150-module-actions-789f/43588728414-1/char31/ 前缀。

此外需要两个已存小源码头：

- 2026-11-15-r150-saturated-global-common-789f.hpp：11284 B，SHA256 f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1，放在新 runner 同目录；
- 2026-11-14-r150-f31-bitplane-789f.hpp：3030 B，SHA256 73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec，放在 repo scope 根目录。

这些是源文本依赖，不是另一组数值计算。

## 3. 仅临时使用已有 p486 恢复包

当前已经实际存在的旧 Release asset 为749870028：

isp-789f-infinity-p486-recovery.tar，
242145280 B，
SHA256 a9d8cf63d4173becb750c1155548fb0e148b5aae95af9ffb681d7ac949002df3。

按根的新规则，只临时取其中本轮必需的三个完整文件，结束后由根删除旧附件，不重新上传它或后继数据。

| tar内路径 | 保存字节 | SHA256 |
|---|---:|---|
| stage-p512/actual-p486-exact-source36.bin.gz | 22711275 | 49dd910f4750a639c33f9ec751ef3c1449887ef2b5dae90a5c5358afb94c6842 |
| stage-p512/actual-p486-receipt.json | 385 | d70ebd4b7552046f743644df71f09265a8218920e132e7abe9345e0887f37b44 |
| exact-rational-kernel-certificates.json.gz | 2133085 | 24913665ab0ff6f1eb41c26caf3b50d1d2fc11cf8568a5611943e91d2c29c184 |

runner 还核对解压后的原来源和核证书 SHA、6188×36格式、旧 native 绑定、23个原核的完整4367输出标志及自由坐标字典。没有把这些检查换成只有一个 hash 的任意矩阵。

## 4. 新源码、CLI 和预算

新 native：

2026-11-15-r150-selected-infinity-dixon-through1024-789f.cpp，
19389 B，
SHA256 6ff3cb4a9ee7415bef17495f2b6d140e80d035754489bc86a8029e291e7e4709，
blob25eb132bf5c7f8327e4182526367e20e7f321fa7。

相对于已运行版本，实际数学算术不变；只扩大允许目标指数到1024、检查点改为512／640／768／1024，并纠正历史注释。仍用 GMP 任意精度整数，所有完整原乘积和整除保留。

新 runner：

2026-11-15-r150-selected-infinity-dixon-resume486-runner-789f.py，
23721 B，
SHA256 a220810454b6c75feb8a661203615d1205687759b135334daa9f2690ae605d23，
blobf75471d1e173bd0ae27d43aa11783cb5434da5b2。

~~~bash
python -B SOURCE/2026-11-15-r150-selected-infinity-dixon-resume486-runner-789f.py \
  --repo-notes WORK/repo \
  --paid-dir WORK/paid \
  --bockstein-dir WORK/bockstein \
  --dixon-dir WORK/dixon \
  --p486-dir WORK/p486 \
  --out WORK/result \
  --seconds 120 --memory-mib 512 --compile-seconds 30 \
  --maximum-exponent 768
~~~

源码目录的两个头文件须按上一节恢复。native 由 runner 用 g++、-std=c++17、-O3、-lgmpxx、-lgmp 编译；编译上限30秒另计。数学共享真实时钟120秒，每进程512 MiB，不为每个阶段重置时钟。数据下载和小回执哈希汇总不属于新数学。

native 直接调用顺序是：

~~~text
native native-model.txt prepared-exact-model.txt forward.bin backward.bin
       actual-p486-exact-source36.bin paid-selected-image-source-dag.bin
       output-prefix remaining-seconds
~~~

prepared 模型中包含新绑定、旧来源绑定、实际起始486和目标指数、17×77原整数点系数，以及同一1021来源、1021输出、985单位来源和36自由来源列表。所有坐标来自已锁实际输入，不由新采样重选。

## 5. 输出、退出码和准确完成范围

唯一长期发布的数学输出是：

selected-infinity-dixon-after486-small-summary.json。

程序要求它严格小于100000 B。小回执包括全部输入与源码哈希、编译结果、真实到达指数、每阶段起止和退出码、每个原检查点的来源／乘积／残量哈希、精确核的slot及分母位数、两种原输出范围的秩界、重建状态计数。它不包含大整数矩阵或二进制编码。

完整来源、原整数乘积、逐位校正、精确核证书和完整流水线回执继续写到同一临时 WORK/result，以便该 job 内接真正的下一数学步骤；不得把该目录整体上传 artifact、Release 或 Git。它们的 SHA 和重算来源已经在小回执中。

退出与语义：

- 0，completed：可能是全部36个精确选定核闭合，也可能仅完成指定有限精度；必须读 outcome 和两个精确核计数；
- 75，checkpointed-time-budget：已经保存最后一个完整真实指数，可以在同一 job 内从该指数续算；不把原请求指数当成实际到达值；
- 1，failed-or-incomplete：保存实际错误和已有临时检查点，不宣称数学完成。

若精确选定核数为36，结合原模31秩下界可证明同一选定方阵的特征零秩4318。只有完整4367输出精确核数也为36时，才能同时证明完整选列矩阵的秩4318。当前23个核都已经满足后者；未来不预填。

若首次出现真正非零所选余障碍，按实际原来源提供的秩增量更新下界；若只有额外13行失败，则不得把它误作所选方阵障碍。平衡重建未完成仍不排除有理核存在。

本接口没有新增数值结果，也没有替代原 Hilbert 不变子空间问题的完成标准。得到所选常数核结论后，仍须研究同一齐次子式在无穷远的真实后续连接和 Smith 阶。
