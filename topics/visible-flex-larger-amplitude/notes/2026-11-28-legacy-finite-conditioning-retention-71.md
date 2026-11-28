# RET71：有限线性条件数与较大切口静态报告的完整退存

## 1. 本批范围

本批只移出当前树的三个旧生成 JSON，总计 **242,948 B**。所有原程序、参数文件、数学说明、旧输入的逐字恢复记录，以及当前活动求解源、输入、队列和结果都保持。原结果仍由固定 Git 提交恢复，不把下面的结论摘要当作原完整数据。

固定恢复提交为 `851d3a515d04872fdd16c4c0f667d1d7306468aa`。本批已在该提交的完整树元数据中核到三个路径、Git blob 和字节数；root 发布前仍只按 fresh 树的精确三元组实施。

| 相对本题的旧输出 | 字节 | Git blob |
|---|---:|---|
| `notes/numerical-m2-tail-conditioning.json` | 77,895 | `335253166486fd72cf45e689997a656c9c3f229a` |
| `notes/numerical-m2-tail-conditioning-flat.json` | 79,806 | `1c1a5a33c1617c5e1d56786fc0f54756feefdaef` |
| `notes/2026-11-12-strong-larger-cut-static.json` | 85,247 | `dbc4d23579f694075b2d9991d73cfbe5a44f4710` |

完整来源台账是 [legacy-finite-conditioning-retention-71-complete-provenance.json](../computations/legacy-finite-conditioning-retention-71-complete-provenance.json)。它保存三个完整文件的 SHA256、精确恢复记录、22 个完整来源体、全部实际参数、18 个线性诊断配置和 10 个静态配置，以及实际标量结论与失败边界。没有把旧数组转成编码、分片或字节差分。

## 2. 两份有限线性条件数报告

完整 writer 是 `computations/numerical-m2-tail-conditioning.mjs`，4,065 B，SHA256 为 `782fc5956e77692188a42d156d1a2d6bbe72369a49d38d4ada4760189b635e5d`。它接受五个位置参数：source topic、port 文件、height 文件、输出、可选 variant 文件。

原实际高度是 −0.010872411228584962；固定 physical depth 24、每胞 parts 4、linearSteps 512、linearFar 48。稳定图取 modes 1、spacing 2，每个 subprofile 再分八小段、各调用八步原线性传输，并保留原 cusp 分裂。这里没有 nonlinear shooting，也没有用一个线性响应代替完整非线性尾。

第一份九个配置包括 prefixR 为 2、4、8、16、32、64，以及 prefixR=8 时给前 16 个谷加 1、2、4。第二份九个配置是 flatOuterThroughCell 为 0、2、6 与 flatSlope 为 .02、.1、.3 的全组合，flatOuterStartSegment 全为 2。完整 base 参数，包括所有谷控、pulse/valley caps 和 warp weights，原文件与台账均完整保留；台账另逐行保存实际 resolved config，没有从文件名猜参数。

原 prefixR2 的 max|L| 为 6836.346933183083，最大位置 rawCell 6。加大 prefixR 的五个配置都没有降低这项最大值；prefixR8-valleyplus2 记录了 540628278393.0812 的有限线性峰值和负 cutSlope −477.50937432338105。所有九行的实际 seconds、cutSlope、maxL/P/Q、峰值地址和原 quarter-scale 指标均保留。

flat0-w0.3 的 max|L| 为 6430.0572396870275，确比原 prefixR2 略低；其余变化没有成为真实非线性解。flat6 三行的 max|L| 仍约为 3.49–3.85×10^11。原笔记对这轮设计筛选的总体结论保持原字；新台账列出全九个实际标量，避免把总体“不改善”的表述误解成每个标量都严格变坏。

两份报告共有 18 个已写出的完整行，没有行级 error；这不是过程 exit code 的记录，更不是非线性成功标志。原报告没有记录 writer 自身 SHA、OS argv、Actions run、Node 构建或进程退出码，因此这些字段仍为 null。当前完整 writer 的 schema、输入、九行配置规则与原两 imported source SHA 均对应；它是完整可用的再生成程序，不借此伪造原报告未记下的自身份。

### 完整旧高度输入

writer 只读取 height report 的首个 `full_prefix_target_height ?? full_target_height` 值，但恢复时必须保留完整原 report：

- `notes/numerical-m2-q20-tail-d8s16p4n256-summary.json`，11,640 B；
- SHA256 `325915212b3428c9f47900ca0fde575fbf305298b9d0233395b28d06cedbc5a8`；
- Git blob `83bf775585d72909505319464f7c3736d93b4da4`；
- 固定恢复提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74`。

该输入的原 target_reached 为 false，停止理由是实际失败非线性尝试后达到 minimum homotopy step。七次失败的完整 scale、error 和 seconds 已保留；不能因为它提供了目标高度，就把它称作成功尾解。本批不删除或重新生成这个输入。

### 外部尾源不是同名占位

`closing_weighted_tail.mjs` 与 `950f-tail-subdivision.mjs` 的整 SHA 分别精确等于原输出记录的 `740e672e…`、`e4431757…`。完整 `closing_recalibrated_tail.mjs`、loader、nine-file dependency manifest 和九个实际模块均保留。

loader 会先逐个核对九个完整 Git blob，再导入模块。台账完整列出这些模块及 transitive imports，覆盖 balanced、rejoin、smooth cells、momentum、raw Cauchy、Cauchy、cusp、compact control 和 height transport。复现时应还原整个精确 source-root；若 loader 优先的 adjacent-topic 目录存在，它也必须满足同一九文件身份。不能把任意同名 cache 作为该来源。

## 3. 较大切口静态报告

完整 writer 是 `computations/strong_cut_radius_static.py`，8,109 B，原报告记录的 SHA256 与现完整源同为 `1402acd41a6e0d7b9fa051d7b444c37385b497c15d669ed2e2f131e4ca28dc9b`。三个 CLI 参数是 checkpoint、source-topic、out，程序强制三类 BLAS/OpenMP 线程数为 1。

实际输入为已成功的 `2026-11-12-strong-angle-vu034-q085-m20.json.gz`，必须恢复原完整 17,785 B 压缩字节；SHA256 `901d1f9f5e1e879035f379f7c8186cc597a63752499ddcaf5b7a44ffb8ae199c`，Git blob `6cbd86c678ef1452199ef74e9651d15ad67a47cf`，恢复提交同为 `60321451…`。本批没有读取、解压或重压缩它，也不删除这一恢复输入。其 SHA 是原报告实际记录的输入身份。

writer 消费完整 frozen_profile 与 physical_tail_parameters，保持真实 loop_ratio=1.1；没有把 provider 默认 2.2 偷换进来。provider → flatturn → excursion → plateau → direct → root_profile_scan 的完整来源和 angle-boost hook 均已记录。静态程序不调用 provider.install 的 BVP 路径；冻结尾模块只被整字 hash，不执行尾校准。

原十行覆盖两个 loop 策略和 rCut=.30、.45、.55、.65、.75。每段取 2049 个位置，保原 64 点高度积分及原单位弧长网格余量。台账完整保存每一行 profile、cut 二阶匹配参数、宽度/cuff、背景尺度/曲率样本、球包络最大位置与数值一致性差。

原报告的三个布尔值仍全为 false：nonlinear_solution、tail_recalibrated、dn_reused。背景半高随切口增加而下降，但原球包络样本增大；所有候选背景最大主曲率样本均为 7.5。这不是柔曲映射的曲率，也不是完整闭面的 reach。原 `D_upper_prefix_bridge_estimate` 包含网格 Lipschitz 余量与 provider 端点高度差，但后者不是严格区间积分误差，因此仍只是设计估计。新 tail、cap、真实非线性耦合和全相位闭面义务均保持未付。

原完整解释 [2026-11-12-strong-larger-cut-static.md](2026-11-12-strong-larger-cut-static.md) 保持；其关于曾误用默认 ratio 的更正以及固定外半径不适用域也完整保留。

## 4. 恢复与消费合同

需要原完整旧输出的读者，在独立恢复目录执行对应的 Git 字节恢复，例如：

```bash
git show 851d3a515d04872fdd16c4c0f667d1d7306468aa:topics/visible-flex-larger-amplitude/notes/numerical-m2-tail-conditioning.json > <recovery-root>/topics/visible-flex-larger-amplitude/notes/numerical-m2-tail-conditioning.json
```

其它两输出同理。完整 source/parameter 文件亦可由该提交的精确路径恢复；旧 height summary 和 accepted gzip 用上节的 `60321451…` 提交。原绝对 scratch alias 与仓库记录的逐项映射在台账中。目录须先存在；上述文本是恢复说明，本次没有运行命令。

两 writer 都不读自己的输出。已读消费者是保留的 status 与原静态说明；搜索不是全仓无消费者证明。任何另有 wholeSHA 或完整数组要求的历史读者，都先恢复完整原文件，不能使用本台账的标量摘要。

完整重算 argv 已列在台账，明确是按完整源与原输入记录重构的合法命令，不冒充未记录的原 OS argv。重新执行只能写新路径、保留新平台与计时记录；不能保证路径文本、浮点库和 seconds 重生为原整 SHA。精确原字恢复由 Git 提供，不要求新科学复跑作为退存条件。

## 5. 未纳入本批的对象

两份 rational-trace 的 entrypoint 旧 SHA 虽已由完整源码精确恢复，但两个 adapter 旧版本尚未闭合，因此仍留树。五份 alternative-outward 的旧 maxstep 缺项仍未消除，也不退。Nelder / Hermite 由 solver 独立调查，本批不重复、不代其许可；ports、parent91、三个 scratch 缺口、当前活动输入以及 canonical 参数全部排除。

本批只读取完整小文本及树元数据，没有读取 ≥100 KB 或二进制正文，没有本地科学、AST、fixture、重放、源码改动、ref 或 queue 写入。root 在普通提交中统一应用三条精确删除和完整附件。
