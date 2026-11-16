# R150 权十完整 Macaulay 的独立编译与控制入口

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / literature_audit、root。AI-assisted: GPT-6 Astra Pro。

**本包仅已冻结，尚未编译或运行。** 它不读取原 200 列父数据，不重建完整矩阵，也不判断原目标成员性。只有实际完成回执中的全部门通过，才可称新实现的控制检查已完成。

## 1. 固定四文件

|文件|Git blob|字节|SHA256|
|---|---|---:|---|
|2026-11-16-r150-original-weight10-macaulay-controls127-789f.py|aeec2f5df1ed1ccb16042315b1d1079244f8dc56|7583|fc5992ab257f3b6f535033a4fb6500af419ab84a8bc64d3f633de87bbfc1912c|
|2026-11-16-r150-original-weight10-full-macaulay127-789f.cpp|1748de326c9dc7a1505486f80c97a43b1fafb777|26864|0a53cd6179904977404db186dbc88bf1a04339c2bf4569b90a9007744f0a50df|
|2026-11-16-r150-original-weight10-full-ordinary-verifier127-789f.cpp|409944c79213e5befad574ba71f25c4a08666dfc|17046|bf10b7ba832123c6208e8e7b4cf2a6e63ba1cfbd2f17cbf6d26e4f4c8a53f295|
|2026-11-15-r150-original-f127-bitplane-789f.hpp|796c0d4c790b3f2294bc203f057e78c0fb16d4ed|4691|03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3|

参数清单文件为 2026-11-16-r150-original-weight10-macaulay-controls127-inputs-789f.json，blob 6f9589f330a520ab424840d7726df992d6b7440e，2723 字节，SHA256 a5d87fd6f4db4d83b4f0914c9060b25bf5ebf43cf4262f32863a07a229d02fd1。四文件只保存代码，未包含计算数组。

## 2. 独立运行

使用 Python 3.12.14；这个入口不需要 flint，不读取任何旧 run 的临时目录。当前预算为 120 秒、1024 MiB，外层至少 150 秒。调用参数完整记录在上述 JSON，入口为：

    python 2026-11-16-r150-original-weight10-macaulay-controls127-789f.py
      --native-source 2026-11-16-r150-original-weight10-full-macaulay127-789f.cpp
      --checker-source 2026-11-16-r150-original-weight10-full-ordinary-verifier127-789f.cpp
      --bitplane-header 2026-11-15-r150-original-f127-bitplane-789f.hpp
      --out TMP/weight10-macaulay-controls127
      --seconds 120 --memory-mib 1024

各参数路径在实际 job 中必须指向按上述全 SHA 取得的四文件。编译参数为 -O3、-std=c++17、-DNDEBUG、-Wall、-Wextra；所有验收使用显式异常，不依赖 assert，故 -DNDEBUG 不关闭验收门。实际编译器版本、两二进制全 SHA、每个过程的返回码和日志全 SHA 均入临时完成回执。

## 3. 实际控制门

新 native 首先重跑旧 F127 header 的 244,990 个控制，再对所有 126 个非零标量、全部 127 个当前值、四个 32-lane 批次验证 2,048,256 个独立普通乘加、不同 stride 和外部 sentinel。九个陪集代表以至多三个有符号二幂直接加到当前列，仍只保存一份基列。

小矩阵保非单调主元到达、零列、依赖列。必须逐普通坐标验证每条规范基的原来源、正目标全部原列乘回、负目标对所有原列的左乘回及原目标读数，并验证完整前四列保存、读取、继续与一次完整运行的状态逐值相同。实际原乘回计数须为 43。这里的小 checkpoint 只留在 TMP。

独立 checker 不导入 bitplane header 或 native。其迭代单项式生成、原字典编码和普通标量控制计数须为 93,412。它对完整问题的 13,808 列证明门仍待后续实际运行；本控制入口不冒称已经支付。

## 4. 完成、失败和后继

临时回执为 full-weight10-controls-receipt.json，临时状态为 full-weight10-controls-manifest.json。只有两个真实编译及所有控制均成功才返回 0 和 completed。任何编译错误、控制不等式、内存或外层预算失败均返回 1 并保实际错误与已有日志；不把它写成数学负结论或可以空续的 75。

完整矩阵入口后续可以显式读取同一 job 中这个 completed 包，核 source、binding、实际回执、二进制及控制日志的全 SHA 后复用。已结束 job 的临时目录不视为存活；跨 job 必须重跑这份小入口。仓库只记录来源、参数、run 和输出哈希，完整 raw、二进制、小矩阵及 checkpoint 不进入 Git、Release 或新 artifact。
