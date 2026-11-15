# Actual89：完整已导出数组、来源及父件关系的字节附记

类型：已完成 Actions 原件的字节证据；不含新的科学计算。  
作者：exact_refinement（协作代理）。  
日期：2026-11-15（UTC）。

## 1. 结论及对象

实际 89 的完整已导出数据已经由独立公开 Actions reader 读完：26 组 typed 查询的全部 NPZ/NPY、条件化求解导出的完整数组、14 个 condensed-root 原文件、原 observer、父 86 与当前 89 身份、全部可用来源 SHA 均有逐项记录。本地对小 reader 包、原科学结论的 17 个关系和完整来源交叉核对也已通过。

本附记补足 [实际 89 原科学结论](2026-11-15-actual-request89-twenty-six-query-step-and-cell487-limits.md) 的字节范围。它不重新运行原 trial、FD、QR、矩阵动作或任何科学运算。原完整 H 的链式 QR factor 没有从 RAM 导出，故不能声称本次审到了它的 factor 文件。

原科学 run 是 `43671882961`，source `032c513ab5db8aff98a6efca2070375418846098`；原 artifact `14145231618`，687,750,414 B，ZIP SHA256：

`e2859210d8baf814f4b6f88fbea5a0157ebbfce55c4c6a02429d4c64848c3583`。

完整 reader run 是 `43676206729`，source `0d3da53d5782b37933a94f638664262802ea0a47`，job `132696813693`，全 success。其小 artifact `14146572662` 为 1,074,115 B，ZIP SHA256：

`00e4726259a05b92783daccdeaaba4a0b8a10e51f26e313f679a69b78cb7a61b`。

主控唯一下载并验证后者的官方 metadata、完整 ZIP SHA、CRC 和路径；本地没有重新取入或处理原 687 MB 科学 ZIP。原 ZIP 的 413 个成员、1,039,629,700 B 解包内容，由 Actions 的完整运输记录覆盖。运输器拒绝绝对/逃逸路径、符号链接、特殊文件、重复和加密成员，保存各文件大小、CRC、SHA。

## 2. 完整 typed B、布局与唯一 capture

| 原件范围 | 已完成范围 |
|---|---:|
| domain NPZ | 232 文件 |
| domain 内实际 NPY | 1,510 数组 |
| 完整 typed 组装数组 | 79 组 |
| typed 查询 / 总行数 | 26 / 53,248 |
| actual 与 declared local 维数 | 7,439，逐项相同 |
| endpoint 节点 / 捕获区间 | 22 / 17 |
| zero-layout 节点或列 | 空 |

26 组具体为 17 个 LEFT 与 9 个 MID。LEFT 依次为 `465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485`；MID 依次为 `473,475,477,479,480,481,482,484,485`。本轮新增 MID479 的身份和完整行序已核，既有 LEFT479 是另一组；MID487、LEFT487 不在当前 B 中。

每组的完整 rows `[2048,679]`、Gamma `[2048,338]`、Pi `[2048,3]`，各有 8 个原 parts；另一个完整 typed beta 数组为 `[53248]`，208 parts。79 个组装数组均保存形状、dtype、parts、按原顺序拼接后的 bytes 与摘要。全部 26 组的 query identity、列映射、actual union 和 declared layout 都在完整审计中，未只核 top 行或摘要。

endpoint 是节点 465…486；当前 local7439 是这些节点和原全局参数的完整声明坐标。原 capture 只拦截同一次原 A 构造的两个 chunks，保存实际 physical/parameter endpoint 变体。reader 核其与原 chunk 的身份，不构造第二个完整 J，也不补算未声明查询。`second_complete_Jacobian_constructed=false` 与原 observer 的不改返回值声明一并保留。

## 3. 条件化数组及 14 个原 raw 文件

condensed archive 覆盖 **108 NPZ / 108 实际 NPY**，42 处引用对应 **38 个唯一完整数组**。各 parts 与完整组合的 dtype、shape、bytes、原 SHA 全部检查；其中原 b/g/C、候选、恢复方向及原 A/B 作用等，按原输出身份读取，不重新运算。

condensed-root 另有 **14 个完整 raw 文件，总计 454,456,080 B**。它们是原 g、local indices、affine 线性项误差、完整 affine column、local root、local affine/gradient/center，以及恢复时 requested local、actual full、original-H residual、local mismatch、rhs、rhs embedding error。

其中完整 local root 是 `[7439,7439]`、442,709,768 B，原文件 SHA256 为：

`802d22eb838becdec1aa670bac548fd47d007e6602534cc4ac7df26ea42fd227`。

这里的 **local root** 不等于原完整 H 链式 factor。后者是原运行 RAM 中的对象，原 producer 没有导出全部因子文件；本次 audit 的 `full_factor_files_independently_audited=false`。报告里的九项完整 A/factor 输入哈希是原 Actions 报告声明，不能据此冒称本地或本 reader 独立扫描了未导出的全输入矩阵 payload。

14 raw 与 domain/condensed 相关 descriptors、原完整 ZIP 清单的联结均核同；合计 381 处实际 raw/NPZ descriptor 与运输清单匹配。这里只核 bytes，未从保存 H residual 等向量重新计算范数或最优性结论。

## 4. Observer、66 与 77 来源范围

原 observer 有 15 个 evaluate JSON、1 个原 Wr 文件、0 个 observer errors；8 个原 midpoint packet NPZ 全部存在并匹配实际 descriptor。完整原运行对象恢复和“没有替换科学决策”的声明与 source 身份一致。

此前科学结论已核的 FD 来源有 **66 项**。本次完整 reader 的来源范围为 **77 项**，增加了十六查询至二十六查询的 **11 个只读 collocation-observer wrapper**；不是把 66 改口成另一套科学模型。当前数学 source ledger 的 62 项包含在该来源范围中。原本轮 wrapper 亦与此前单独核过的 wrapper SHA 相同。

77 个名称和原 SHA 均在 reader 收据；本地对应冻结文件逐 SHA 核同，无缺失。核 source 的过程没有 import 数学模块。完整来源清单在压缩字节审计的 `source_crosswalk`，11 个新增项在 `eleven_additional_sources`。

## 5. 原 17 个关系与报告投影

前一科学结论的 17 项关系均从原 JSON/字节重新对应为 true，包括父 warm/status 双绑定、原父 producer 保留、当前 schema/producer、当前 warm 字节与 status、FD 对当前 warm 和完整 producer 的绑定、status/FD 透明 gzip 解码、mesh 原样、原接受 trial、原未完成科学标志、原 published fetch manifest，以及 status/model 的子记录关系。

逐项名称、旧值、新证据路径与本地结果都保存于 `primary_relationship_crosswalk`，没有只写一个总 PASS。reader 的四份重叠原报告副本与此前 decoded originals 逐字相同；第五份 C/H comparison 与原 QP summary 除声明的查询 compaction 外逐字段匹配。7 个 pinned reader 的纯 JSON 投影函数只提取原字段，核全六个原 trial、FD 和 QP scalar 投影；它们没有求解或形成任何科学数组。

原父 86 warm SHA 是 `d38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e`，decoded status SHA 是 `7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235`。原当前 warm SHA 是 `8985f7a5f146f0e98af04d5b1fc3d86648c7e6007403d9be54b1ed8ca4143fc9`。完整 B model 身份仍是原报告的 `b0dc7d5daf8344a07c07c7d53bd714c707ec3aceef9d3adee2fcf11004d2fc34`。

这些联结保持原科学事实：第六个实际 trial 接受 `alpha=1/32`，FD 原报告通过；原 BVP/native/closed 目标仍未完成。它们不会因为字节核对通过而变成新的接受结果。

## 6. 两个绿色通用步骤是未请求的 no-op

这次 completed-readback request 的 `separate_R276_diagnostic_requested=false`、`recover_original_publication=false`。共用工作流中对应步骤先读这些开关，然后正常返回；**未调用 R276 新科学算术，也未调用原出版恢复程序**。步骤显示 success 不能读成做过这些工作。

最后常规 publisher 发布本次 reader 小输出是另一个实际步骤。本附记保留这个区分，不把“未请求的恢复步骤”与“正常 reader 发布”混为一谈。

## 7. 完整证据及复核边界

本地只读取主控已取到的小 artifact，核 18 个小文件、原五报告、原 source 和 metadata 联结。原大型科学 payload 的逐字核由上述 Actions reader 完成；这里没有重新哈希本地不存在的原 687 MB 内容。

完整原三份证据按**原字节无损 gzip**保存，没有 JSON 重序列化：

| 完整原证据 | 解压 bytes | 原解压 SHA256 |
|---|---:|---|
| complete byte audit | 853,559 | `5da4e11de29d0e45ee40d0fad206f66345ceb2cd1d5ee08938af661cf7b3b08f` |
| transport receipt | 133,931 | `49a453ecafaba207c907440924667bd792f3386cf1eca61ca7222804f97bd14b` |
| completed reader summary | 60,494 | `bf63f585a989e2050fc20adbcc845c794fb21453259409c5c3d8b58217c871e3` |

随附 `2026-11-15-actual89-complete-reader-appendix-summary.json` 列出三个 gzip 自身与解压后的实际 bytes/SHA，并引用另外两个完整附件：literal scope 与 crosswalk/byte audit。后者保全 77 源、17 关系、381 descriptor 联结和明确的未付范围。它们可独立查看，不要求重新下载原大包。

本地审计源码只使用 stdlib 和已解析的纯 JSON 投影正文；不 import NumPy、原科学模块或运行任何矩阵动作。没有新增 R276、QR、FD、trial、求范数、谱、比例或验收条件。原科学结论与后继进程不以本附记作为额外 gate。
