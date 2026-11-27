# Run06 已返参数归档与完整 current-PCG 后继准入参数

## 实际来源与归档边界

本条只整理已公开完整参数及已实际返回的小记录，不执行或预填科学方向。所有写操作仍由根代理审读后统一提交；此时没有改 main/ref 或触发运行。

原活动队列 `computations/resume-20261126-followups-06.json` 实际从 main 读取，并与公开提交 `7a771e602bbdb8ee25a845d8d690b27e2e4896bd` 的同文件逐字比较一致：76950 bytes，Git blob `6f7e74a38ed821a59949da6882a72a98be23536e`，SHA256 `88681682ff4865d4f15d6585f312314a4d48acf044b970b9c6d768c258e9a8c9`。

只将 run `45904402595/1` 已实际返回的29–35从活动列表移入完整参数档案。29–34均 completed/0；35为原 ae6 v1入口的 failed/1，51.50014264499987秒，完整实际失败 record 保留，不改写成成功、不删除其新位置责任。实际35没有最终场，其完整runner报告的路径/SHA/bytes和所有缺项保持原小卷记录。

对应实际记录来自三份完整公开有限小卷：

| 卷 | Git blob | bytes |
|---|---|---:|
| `2026-11-26-public-actions-45904402595-1-part-001.md` | `dc3127378217208c3f97c7b41b5ee32f8b01f938` | 57842 |
| `2026-11-26-public-actions-45904402595-1-part-002.md` | `2edd57cbf0cd7baf1afe14a70b669abe5b758a39` | 40593 |
| `2026-11-26-public-actions-45904402595-1-part-003.md` | `2e9e007da047b3c8448887559f142529b090d4a5` | 37543 |

实际36在最新第3卷也已完成返回，但本轮选择范围固定为29–35；36–40的原五个完整对象全部保留在活动队列中。不能因暂未见新的索引快照就断言未启动，也不能从归档行为推断下一方向已准入。

## 完整参数档案

七份完整原 step 对象加七份完整实际 record 超过100KB，所以分成两份独立合法小文件。各文件都有原完整 queue header、原 queue 身份、实际run/attempt、原小卷的完整bytes/SHA/blob指针、完整返回 record 和完整 step 对象；不靠删字段压缩科学责任。

| 文件 | 范围 | bytes | SHA256 |
|---|---|---:|---|
| `resume-20261126-run06-returned-steps-archive-001.json` | 29–32 | 65112 | `fa2190781ad9f8fe4461237f65949c26528ff85be40671701d8ae9f8fc403047` |
| `resume-20261126-run06-returned-steps-archive-002.json` | 33–35 | 76659 | `89a986d83fa4dafb1bd3f96bc969406e6d889cd982588890e7d77edf517d8153` |

每个 record 的原实际 source_commit、source_sha256、input_files、parent_sha256、outputs、state/returncode、command、metrics、summary_errors、missing_outputs 和 cleanup 元数据都保持完整。原大 raw、逐点科学报告、矩阵或日志没有下载、转存到参数档案或重包成“输入”。

controller 的持久 attempted IDs 不变；归档不重跑已有ID，不移走runner原输入/最终场/位置报告，也不清除永久地点。

## 完整后继的准确拼接

新活动队列保原全部 header 字段和原 scope，先逐对象保留原36–40；其后接已刊完整四个 normalized history 对象；最后接已刊 current-PCG science+pure 单次准入对象。总计10步，69726 bytes，低于原95000 bytes守卫；未放宽任何发布或大小守卫。

scratch新队列文件为 `resume-20261126-run06-after-archive001-002-plus-history-and-current-PCG.json`，SHA256为

`bd9f89b6fb6476cc0c373ca6313f28df5cd3696486dccbf39c1cecd701d1b3c4`。

四history来源为已刊 `resume-20261126-run06-complete-normalized-history-ready.json`，32872 bytes，SHA `323be223ed09c95d6e0f52ab1fb9b2b6a839f67efb4a55116c47cca5a3f57278`。它们逐一重建本run的完整全空间 backtracked-SOC 父及历史，不能把旧run04的 bundle/source/target 身份当成本run已再生。

最后单次准入对象来自已刊 `resume-20261126-run06-current-PCG-complete-pair-ready.json`，12940 bytes，SHA `f33901a2617c9db26157cf02061efd5c4d70effcd52bea6125b035f173fb5aa1`。它的完整双child参数仍独立保存在已刊 `resume-20261126-run06-current-PCG-complete-pair-parameters.json`，SHA `b4b29103189374f0269ff5d5dcb7ba7c3bae742bdf50745731ae125f2e1f3e3a`。

此处没有把旧μ抄成新父μ。已刊完整 wrapper 在真正执行时核实际同run父报告、checkpoint、固定目标、全部四输入、范数和谱测度后，只填两个声明的 μ placeholder；其他所有参数、历史、原完整 source、未知输出责任保持。新8列预条件器、原Phase I、完整全行后退SOC以及全部真实非线性门继续使用其已刊完整来源。

## 实际验证范围

已对保留的五个对象、追加的四个history对象和最终pair对象分别作完整JSON对象逐值比较；每条argv、summary、cleanup、output和parent字段都匹配原来源。所有被归档ID都有对应唯一已实际返回record；没有删除pending对象。

完整 remove/keep/append 映射、各原文件和新文件SHA已另存 `resume-20261126-run06-archive001-002-and-current-PCG-correspondence.json`，供根代理逐项审读。这里的比较是元数据操作，不是科学运行或新的fixture门。

此时只准备完整后继准入，不能把排队称作实际执行，把迭代极限称作驻点，把有限真筛称作连续证明，或将时限视作课题完成。

## root 复核及实际准入

root 按上述每卷固定 Git blob 先核实际size及完整SHA，再读取完整小卷中的实际record；七个完整参数对象与原活动队列逐值相等，七个完整返回record与原公开记录逐值相等。只移29–35；原36–40五对象逐值不动。随后与已刊两份完整ready逐值对照四history及最后单次pair对象，十步和原完整header逐值相同，finish_when_done仍false。此提交将该69726-byte完整queue写入真实run06动态入口，完成准入，不预填实际开始、父字、μ或科学结果。
