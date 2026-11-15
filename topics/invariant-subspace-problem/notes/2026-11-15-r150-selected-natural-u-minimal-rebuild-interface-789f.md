# R150：丢失临时会话后的同 I,J 自然参数最小重建入口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15。

## 1. 本次恢复范围

旧 run43679903558 已结束。八阶、十六阶的完整小回执已发布；三十二阶计算虽在旧日志中完成，执行摘要叠加历史 pull 记录后超过 100000 字节，未发布其完整结果，临时数组随会话消失。本入口据原提交的输入和参数重新建立必要工作文件，完成新的真实运行及独立小回执。没有将消失的文件标成“已恢复”，没有把旧日志中的总阶 243 预填为新结果。

入口源码：

- `2026-11-15-r150-selected-natural-u-minimal-rebuild-789f.py`；
- Git blob `f68ace84577c79c13d74bbe3686bff38df636ad9`；
- 19311 B，SHA256 `bb4a217827ff7a8ac8faf9c0f1b2c5255e302c3bcc66f644cd31a8f8f50312c6`。

本地只对该完整字节作了 Python AST 解析；没有本地重跑数学。实际运行由 root 的新临时 Actions 会话调度。

## 2. 八个历史输入，合计 5228918 B

全部历史输入使用已知提交

`8c6304e273e64b0544d3dd58bc0e48a672a87c36`。

以下路径都相对于 `topics/invariant-subspace-problem/notes/`。通过该历史提交的 `git show` 原样恢复到当前 job 临时目录；逐项大小、SHA256 由源码与原引擎核验。禁止重新上传为 Git、Release 或 artifact 数据资产。

| 输入 | 历史相对路径 | 字节数 | SHA256 |
| --- | --- | ---: | --- |
| 原 native 模型 | `r150-module-actions-789f/43588728414-1/char31/native-normal-form-input.txt` | 128145 | `291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6` |
| 原 forward DAG | `r150-module-actions-789f/43588728414-1/char31/nf-forward.bin.gz` | 1660293 | `445ec1d9acfa14932d8c3122fe98b471d869b3a8df0fa09a9ce14027e67c96ca` |
| 原 backward DAG | `r150-module-actions-789f/43588728414-1/char31/nf-backward.bin.gz` | 2031817 | `b6a40b3bb5b54053ac71dd8eb0a2b3555ffc88bb958229ef23c756b705fb5a28` |
| 原选定集合回执 | `r150-selected-infinity-minor-dag-789f/selected-infinity-minor-dag-receipt.json` | 75700 | `5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68` |
| 原整数无穷常项 | `r150-selected-infinity-constant-bockstein-789f/actual-original-infinity-constant-model.json` | 87459 | `97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074` |
| 原完整核36 | `r150-selected-infinity-constant-bockstein-789f/actual-original-kernel36.bin` | 222788 | `c008e57b7a7e80312f8ba292bb24241d53bb59d4c57b2a8d07ec1017b9de0744` |
| 原985来源 DAG | `r150-selected-infinity-dixon-kernels-789f/actual-selected-image-source-dag.bin.gz` | 957557 | `c50e7bb8558a7f637d9d6951f64ae002c96cdce06dfcb7d1a4619ea6dc07337a` |
| 原 primitive 整系数多项式 | `r150-first-padic-residual-789f/original-primitive-integer-equations.json.gz` | 65159 | `44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe` |

这里不需要旧 p486/p768 大数组、已删除的 Release 资产、原有理二十九核、1603 有理求解结果、七方向的 4318 消元，也不需要 709321 B 的旧有理左核。

另取已发布小文本：

`notes/r150-infinity-remote-session-789f/43679903558-selected-natural-u-schur-through16.json`，93340 B，SHA256

`938d1796c73b780d3fdb379c83e21907381618dcd9e81c7b281b21c6e4a1484f`。

该文件保存旧 $0,\ldots,16$ 阶全部来源、余量、Schur 文件的大小和 SHA；它是本次逐系数比较的输入。

## 3. 原引擎字节和新输入绑定

保持以下数学源码原字节：

| 文件 | 字节数 | SHA256 |
| --- | ---: | --- |
| `2026-11-15-r150-selected-natural-first-connection-f31-789f.py` | 20861 | `45991f0744fe8b020170c77a6f99e4b6e3e9433a3f18ca4c0405cdd76132bab6` |
| `2026-11-15-r150-selected-natural-u-schur-source-jets-runner-789f.py` | 21664 | `80f6815133250cf559f81afb557f138952f7268ce2d2b43e2c15bfb822775e67` |
| `2026-11-15-r150-selected-natural-u-schur-source-jets-789f.cpp` | 16667 | `40dc42b367d241fb7d1cf0c3dd9ef35d61ad0ce756a63559ca8110188b2206dd` |
| `2026-11-15-r150-saturated-global-common-789f.hpp` | 11284 | `f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1` |
| `2026-11-14-r150-f31-bitplane-789f.hpp` | 3030 | `73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec` |

C++ 和两头文件置于 Schur Python 所在脚本目录；头文件也允许按旧引擎规则在 repo-notes 查找。运行只需要 g++、Python、python-flint，未引入 NumPy。

原 native 模型已明确列出 3333 个来源编号及主输出单项式；原 point 已列出余下 1021 个来源、1021 个输出与 985 个独立来源。二者直接给

$$
J=J_{3333}\sqcup J_{1021},\qquad
I=I_{3333}\sqcup I_{1021}.
$$

入口逐项核验完整来源编号、乘子、输出单项式、无重复及 $|I|=|J|=4354$；原三十六自由来源同时与历史回执和已发布十六阶回执相等。它生成只含实际必要字典的 lean JSON，明确不冒充旧的 814572 B gzip 容器或旧 62084 B profile。

随后由原 point 的 17×77 整系数逐列建立同一 585×954 投影。调用原 stdlib first helper，只重建已丢失的有限域小核和原乘回缓存；原 first helper 仍核全 4433 个参数系数、1309 个原常项、全部原核支撑及全 4367 输出。这个步骤不做特征零 585 RREF。

外 wrapper 在导入后只将旧引擎的输入 PIN 表替换为这些已核重建文件的实际大小、SHA，并将 FIRST binding 替换为本次真实第一步绑定。数学函数与源码文件不改。新输入容器及首次回执有新的实际字节，因此 Schur 使用**新的绑定**；回执同时保旧绑定、wrapper SHA 和原引擎 SHA。没有借路径或旧 gzip 哈希绕过输入核验。

## 4. 已发布前十六阶的完整系数比较

旧绑定为

`1fdb07aa85a565c45d7adfe04721a29cdbe6911cc0cb50ca45044c51f88ccc01`。

来源、Schur、全余量文件的格式都是 24 字节尺寸头、64 字节绑定、完整有限域数组。对每个 $0\le k\le16$、三种数组分别读取新文件，仅把第 24 至 87 字节改为旧绑定，再与已发布旧文件的大小、SHA 比较。

总共核验 **51 个完整文件**，包括：

- 全 $6188\times36$ 来源坐标；
- 全 $36\times36$ 同 $I,J$ Schur 系数；
- 全 $4367\times36$ 原输出余量。

这不是只比较指数分布或秩。文件尺寸、magic、新绑定先严格检查；之后的比较不改变任何数学系数。全部 51 个匹配后，回执才记

`all51PaidPrefixFilesCoefficientIdentitiesVerified=true` 和
`allSeventeenPaidSmallSchurCoefficientsVerified=true`。

若共享时钟只走到 $k<16$，保存真实完成层并报告目前匹配的前缀，不把两个全完成标志置真。

## 5. CLI、时钟和恢复

建议新 job 一次请求到 32：

~~~text
python -B {scripts}/2026-11-15-r150-selected-natural-u-minimal-rebuild-789f.py
  --native-model {native_model}
  --point-model {bockstein_dir}/actual-original-infinity-constant-model.json
  --selected-receipt {paid_dir}/selected-infinity-minor-dag-receipt.json
  --kernel36 {bockstein_dir}/actual-original-kernel36.bin
  --source-dag {dixon_dir}/actual-selected-image-source-dag.bin.gz
  --primitive-equations {primitive}
  --paid16-summary {scripts}/43679903558-selected-natural-u-schur-through16.json
  --first-runner {scripts}/2026-11-15-r150-selected-natural-first-connection-f31-789f.py
  --schur-runner {scripts}/2026-11-15-r150-selected-natural-u-schur-source-jets-runner-789f.py
  --repo-notes {repo_dir}
  --out {work}/selected-natural-u-rebuilt
  --maximum-degree 32 --seconds 60 --memory-mib 512 --compile-seconds 30
~~~

历史恢复、依赖安装与下载单独记实际时长；数学共享 60 秒，native 编译另限 30 秒。入口数学时钟从历史输入核验和重建开始，传入 Schur 的时钟扣去已用重建时间。原 Schur 编译与实际数学时钟保持原分离规则。

输出主回执：

`selected-natural-u-minimal-rebuild-receipt.json`。

可见状态为 `completed`、`checkpointed-time-budget`、`failed-or-incomplete`。成功还必须真实满足：

- `completedNaturalDegree=32`；
- 全部原 jet、来源支撑、36 自由坐标完成标志；
- `all33CompleteOriginalFirstCorrectionsVerified=true`；
- `all4367FirstCorrectedProductsZero=true`；
- 两个完整已发布前缀比较标志为 true；
- 精确模 31 Smith 完成与阶数由本次 `smallSeriesSmith` 真实输出读取。

入口不预填三十二阶的阶数或完成值，也不要求实际尚未知的特征零结论。

临时目录包括 `rebuilt-inputs/`、`rebuilt-first/`、`natural-u/`。完整第一步缓存保逐文件哈希；若它已完成，后续重入不再改写含实际时间的第一回执，因此同一新 Schur binding 保持稳定。原 native 每层来源/余量/Schur 及 ledger、完整文件清单仍按原 checkpoint 逻辑恢复。未完成的原数学不在新数据不存在时冒称已续接。

## 6. 小发布边界和后继 Q 入口

wrapper 的主回执保存紧凑参数、真实新 native 摘要、完整前缀比较哈希及小 Smith 步表。原 legacy 主回执仅在序列化浅副本里删去重复的 4318 个单位行数组，不改内存原对象、native 输入或数学。发布器另须遵守 root 的新规则：只记当前 pull 及其摘要，不能再把整个旧会话 pull 历史拼入每条结果。

本入口没有保存大输出的 Git、Release 或 artifact 通道。全部可重算数组只在新 job 临时工作区继续供后继任务使用。

同一新临时目录给后继 Q 第一包络提供原 lean $I,J$、原投影整数输入及自然 $F_0,F_1$。该 Q 入口仍需另恢复/重算它原来确实已丢失的有理 585 左核；这不阻塞本次 natural-u 重建。模 31 完整 Smith 阶数即使本次成功，也不自动证明特征零同阶或首项 31 单位。
