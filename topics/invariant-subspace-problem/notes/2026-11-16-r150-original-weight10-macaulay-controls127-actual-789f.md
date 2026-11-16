# R150 权十完整 Macaulay：两份冻结 C++ 的实际编译和独立控制

作者：Astra-ISP-789f / literature_audit，与 root 协作。AI-assisted: GPT-6 Astra Pro。
日期：2026-11-16。范围：本页记录真实编译和控制执行；没有生成或消元完整权十原矩阵。

## 1. 实际执行

GitHub Actions [run 43922052588](https://github.com/Rogerhu12/math-research-public/actions/runs/43922052588)，job 133491622542，步骤
`original-weight10-macaulay-compile-controls120`，实际退出码 0。
开始于 2026-11-16 17:47:54 UTC，观察器于 17:48:02 UTC 记录完成。
冻结控制器预算 120 秒 / 1024 MiB；外层观察器 150 秒。数学控制器实耗
8.018645535999894 秒，观察器 8.504441904999908 秒，外层步骤 8.688487140999996 秒。
观察器未请求终止；等待到的子过程峰值为 255596 KiB。

运行使用 Python 3.12.14 和 g++ 15.2.0，编译参数为
`-O3 -std=c++17 -DNDEBUG -Wall -Wextra`。两份 C++ 都是实际编译，随后两个实际控制程序均退出 0。
该控制器不读原 200 列父件，不生成完整 77276 × 13808 矩阵，也不依赖 Singular。

实际发布身份文件是
[43922052588-original-weight10-macaulay-compile-controls120.json](r150-original-exact-low20-execution-789f/43922052588-original-weight10-macaulay-compile-controls120.json)。
这份仓库身份只保存来源、参数、运行和输出哈希；完整回执与控制二进制保留在完成作业日志或临时目录。

## 2. 固定来源及实际控制

| 来源 | Git blob | SHA-256 |
|---|---|---|
| 控制器，7583 字节 | aeec2f5df1ed1ccb16042315b1d1079244f8dc56 | fc5992ab257f3b6f535033a4fb6500af419ab84a8bc64d3f633de87bbfc1912c |
| 完整原矩阵 native，26864 字节 | 1748de326c9dc7a1505486f80c97a43b1fafb777 | 0a53cd6179904977404db186dbc88bf1a04339c2bf4569b90a9007744f0a50df |
| 独立 ordinary verifier，17046 字节 | 409944c79213e5befad574ba71f25c4a08666dfc | bf10b7ba832123c6208e8e7b4cf2a6e63ba1cfbd2f17cbf6d26e4f4c8a53f295 |
| 原 F127 bitplane 头，4691 字节 | 796c0d4c790b3f2294bc203f057e78c0fb16d4ed | 03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3 |

四个子过程按次序为编译 native、编译 ordinary verifier、native controls、ordinary controls，全部退出 0。实际门如下：

- 原 bitplane 头的全标量等控制共 244990 项全部通过。
- 新 signed-scalar / rotation 控制共 2048256 项全部通过。
- tiny 原矩阵的 43 个原乘积全部通过；包括非单调主元顺序、零列、依赖列、正来源、负左证及完整 checkpoint roundtrip。
- 独立 ordinary / 字典控制共 93412 项全部通过。

这些计数是冻结代码实际执行的控制门，不是完整原矩阵的秩或成员性结论。

## 3. 完整身份与独立日志核对

控制器 semantic binding：

`12cc5bff4faf0914561e4377e14ff0351ea587beeaf65ca79ee146d5f737420c`

临时原回执为 4022 字节，SHA-256：

`45225626d24c434a302f2af86a91f4be0a781f6d90ff1105aa4e61f7ddb875d9`

临时 manifest 为 1945 字节，SHA-256：

`16a63e9001d9a3ad99d68904086371533c06a4f13fbc975c37089ba8f7d28176`

实际 native 二进制 155552 字节，SHA-256：

`588ee8e3ecae977843fdb5a6bae4bc4ba7a335538e85684ab07788bc7b54ab33`

实际 ordinary verifier 二进制 94432 字节，SHA-256：

`a851c7067ac01e2cb3dc2574a218474a117b7e58e908295f4fee3ad69232ba79`

root 已全文读实际记录并无损重构回执。literature_audit 随后独立获取完整 job 日志，保留原浮点 JSON 数字字面量，按冻结 Python 控制器的 canonical JSON 规则重构原回执及 manifest，再独立重算 semantic binding。三者的完整字节数及 SHA-256 均与作业记录相同。标准输出恰为原回执加一个换行：4023 字节，SHA-256
`76f555934fe48731e608cc4a6cc3605eb65155b6aee4e2dc2884906db358c753`。
本次下载并审读的 job 日志 UTF-8 为 31417 字节，SHA-256
`3390e24d7c0b19260adf667c4c0b5d3378ec74967af85d334aa5ed24f51457c3`。

## 4. 尚未执行的完整数学门

本次实际只支付两份冻结 C++ 的编译、全标量控制和 tiny 原矩阵控制。完整 77276 × 13808 入口仍须逐原来源构造、完整列消元、完整状态审计以及独立 13808 原列乘回。正分支还必须回填全部原十坐标、十八来源及十七物理梯度；负分支必须给实际原目标读数为 1 的全原列左见证。本页不预填完整秩、目标余式或特征零结论。
