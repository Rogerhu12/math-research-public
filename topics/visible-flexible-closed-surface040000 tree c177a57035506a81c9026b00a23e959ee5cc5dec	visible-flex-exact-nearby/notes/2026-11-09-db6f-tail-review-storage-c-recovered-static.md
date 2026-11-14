# Storage C 恢复源码：独立静态审查与未付运行门

**结论：接受最终 terminal-v3 及同批 angular/export/mesh-replay 的静态来源与读取适配；独立 v4 Python 重放仍未完成，Storage C 不记为完整执行通过。**  
审查人：/root/tail_review_continued_2，2026-11-09。只保存新文本 note，不改旧源码、HANDOFF、LOG 或 results。

本稿补存环境失联前后已经完成的全文审查和实际纯文本核对。恢复文件是 notes 下的 .py.txt 文本副本，不是已经安装的运行入口。没有恢复或上传任何数学数据包，没有调用 producer、BVP、DN、RK、角向验证器、连续后台、几何或网格生成。

## 1. 不可变恢复索引与最终身份

完整十件恢复索引：

[Storage C text recovery index](https://github.com/Rogerhu12/math-research/blob/c4851e5150b18245fa61d94dd885012b9e1bc088/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-text-index.md)

- commit：c4851e5150b18245fa61d94dd885012b9e1bc088。
- blob：28ec4dca109d3fea6a619ce5948ba2e885152e3d。
- SHA-256：1cab20b31ce6d9b9e24be44ed231f60b7cf21624e709f0844d041131b533e725。

审查人已在 2026-11-09 22:55:11 UTC 独立取回十件固定提交文本，逐项核完整 SHA-256、字节数和 Git blob，10 件一致，0 失败。总量 250,129 bytes，最大单件 48,711 bytes；全部是新小文本恢复件，没有数据文件。

最终四个入口的源码身份是：

| 原 scripts 文件名 | 恢复 commit | SHA-256 |
|---|---|---|
| db6f-prefix-angular-metric-storage.py | d32e71935164e190fe7d1c63051468f244363263 | 2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c |
| db6f-prefix-export-closed-mesh-storage.py | 31920c0c68ca98a180f9b67ec070bc6d046a6963 | d776e41ef75741be0d5d44a8156d2c71a70ad016ef3678605d718a32ba7684d1 |
| db6f-prefix-review-closed-mesh-storage.py | 35ba1b0a59361e663709b39119bf68d2be5ad373 | 698e8b0528ffa7b1bbe1bc84c574079f60261156f1d3a6ddae048af0f9c0c479 |
| db6f-prefix-terminal-error-storage-v3.py | 72ca9a7b743842f1aa4287e987efb66fdaea7dfd | 8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7 |

最终 terminal-v3 恢复 blob 为 430fee2a7109af8fa30f4ab519e856bba6fa25ba。terminal-v1 的 809cc7ab… 与 v2 的 a00f8210… 均为保留历史身份，不是最终终门；完整历史哈希在索引中。

最终纯检查器：

- 原名 db6f-prefix-check-storage-gates-v4.py。
- 恢复 commit 37395f9e0273251e37db86e886dd59e5d0363a6e。
- blob 7f9b450539fd1e5e4e4ccca355f7e29782bad784。
- 13,975 bytes，SHA-256 59c250c55cfe731753f0ee1639728dd4d8b67fca0134e480ebd9f7ca1e55426c。
- 已全文读取；尚未由本审查人实际运行最终 Python 检查器。

## 2. 完整源码差分的实际独立重放

审查人于 2026-11-09 22:55:33 UTC 在 JavaScript 隔离运行时，对三个冻结 transformation ledger 作严格顺序的完整前向替换；每次都要求旧片段唯一出现，最后比较完整新源码字节。

| 源变化 | 替换数 | 完整结果 |
|---|---:|---|
| 原 angular → storage angular | 13 | 全文相同 |
| 原 exporter → storage exporter | 5 | 全文相同 |
| 原 mesh reviewer → storage reviewer | 4 | 全文相同 |
| 原 terminal → storage terminal-v1 | 12 | 全文相同 |
| terminal-v1 → terminal-v2 | 7 | 全文相同 |
| terminal-v2 → terminal-v3 | 1 | 全文相同 |

合计 6 条完整重放、42 个替换步骤，均通过。对应 ledger 的 SHA-256 为：

- 0417ac80883dda492618f8535a06ce0eaab230decf0eec4751d2b8c41b25dd88。
- 82bbb53a65803c1f2531a6d2544f82d86f820d458acfeb5494f07f3d7b7f3d69。
- 4299872c6189de869d137682ace26eee965fdabc0af01a2c47a25342bab1e336。

这次实际运行是文本算法，Python、AST、存储包读取和数学对象构造均为 0 次。没有将前向文本相同冒称实际候选通过。

## 3. 旧 tail/reference 门与数学函数没有被放宽

完整静态差分采用独立的 PREFIX_SOURCES 和 Files.prefix_source。原 SOURCES 没有简单扩展成可同时接受新 prefix 身份的集合；旧 tail 与 reference 仍走原来源门。

审查人另于 2026-11-09 23:29:01 UTC 实际进行完整函数文本比较，身份为 tail-review-storage-c-preserved-functions-text-01：

- 原 terminal 的 14 个函数逐字相同：check、canonical、binary、exact、same、parameters、checkpoint_parameters、definitions、manifest_files、reference、transfer、tail_certificate、scalar_gate、main。
- angular 的 trig_table、verify_rows 两函数逐字相同。
- mesh 的 16 个原数学/写入及工具函数逐字相同：check、sha、module、resolve、distinct、flat_sampling_knots、interval_midpoint、polynomial_value、exact_chart_values、invert_material_angle、prefix_points、tail_coefficient_value、evaluate_tail、cap_points、triangle_faces、write_ply。

还独立比较了通用 Files.file/source/item 三个方法及 SOURCES/REFERENCE/BACKGROUND 三个完整字典，均逐字相同。它们的文件解析与旧来源规则没有因 prefix 的存储迁移而放宽。这些仍是实际 V8 文本检查，不是 Python AST 或数据读取。

## 4. 最终 terminal-v3 的实际来源闭包

新 PREFIX_SOURCES 单列 13 个冻结来源，覆盖 codec-v2、storage helper、新 fullxyz/mirror/continuous reader、polynomial、supplier、moment、common-cut、prefix arithmetic、metric/closed budget 和 angular。

candidate 分支显式核实际 base/common 的新 fullxyz 身份、mirror 包装身份、各实际报告对应的新 prefix 来源。普通 polynomial metric 与 angular baseline 均核新 continuous backend；moment 的 backend 和 arithmetic 绑定也明确。它们不能拿旧 tail continuous/poly 的哈希冒充新 prefix 数值实现。

prefix_storage 从实际 base 元数据出发，而不是用 common-cut padding 后的模式数重解释原数组。它要求 base/common 的 data_storage 相同且没有旧 data_file 字段，调用绑定 helper 的 hash-only read_payload，核重新读回的 base 与候选一致，并核逻辑容器 SHA 同时匹配 base/common。

这一步只重构和核字节身份，不构造 ExactHermite，不导入 NumPy/SciPy，也不独自宣称检查了新的连续几何。实际数组的 dtype/shape 读取责任仍在已审 reader/consumer 链及其未来真实运行中。定义数据的 base 模式数与 common-cut 的 padded 模式数必须分开；公共 M64 不能用于重解释旧 base M24 的实际数组 shape。

由 helper 返回的真实文件闭包，逐项用原 Files.file 和实际字节数核验。budget、metric、angular baseline、angular certificate、moment 等报告中的存储账本都与该实际闭包比较，不能只引用一个未解析的 descriptor 标签。

## 5. v2 迁移缺陷与 v3 修复的准确范围

环境失联前，本审查人曾实际复现 terminal-v2 的跨 checkout 迁移拒绝。旧独立观察回执为 68cd2b/exit0，观察文件 SHA-256 为
55a1fc16818682bce1167ce1fba77e8546a35bb35193393fbdaef7477057dc46。
这是当时真实负例的记录，不是最终 v3 的通过回执。

问题是 v2 先尝试按报告里的旧绝对路径解析本地文件；即使报告声明的 basename/bytes/SHA 全部与本次实际 descriptor 闭包相同，也会在迁移后因旧路径不存在而失败。

v3 唯一修改为 prefix_storage_ledger 的处理顺序：

1. reported 与 actual 必须都是同长度 list。
2. 每项必须恰有 file/bytes/sha256 三字段，file 是字符串，bytes 是严格 int（bool 不合格）且满足 \(0<\mathrm{bytes}<5{,}000{,}000\)，SHA 是 64 位小写十六进制。
3. 先比较 \((\mathrm{basename},\mathrm{bytes},\mathrm{SHA})\) 的完整多重集；实际闭包不得含相同身份的重复项。
4. 只有匹配成功后，才对独立解析出的 actual 真实路径调用原 Files.file，并核实实际文件大小。

因此旧报告路径可以整体移位，但内容身份、完整性和多重性没有放宽。reported 的旧绝对路径不再冒充当前可解析来源；真实读取仍由已核 base/descriptor 的 actual 路径控制。修复没有给通用文件 resolver 增加新的全局 fallback，也没有改旧 tail/reference 的路径策略。

这个修复在源码层面正确。最终八路径迁移正例及负例的**独立 Python 实际重放**仍应在执行器恢复后完成。

## 6. angular、mesh 以及 common-cut 关系

angular 新入口显式绑定新 prefix polynomial 与 continuous backend，并读取实际 base 的完整数组；它要求 common-cut 与 base 存储引用一致。其三角表和分区验证数学函数已在第 3 节逐字核同。共享 prefix arithmetic 使用同一新 prefix 多项式 I/P 类型，避免混入旧 tail 类型。

B 批已经处理的 common-cut 在 superclass 初次读取之后，自己重复读取以及 make 路径也必须走实际 base 的 read_arrays(basepath)。C 批保持该完整依赖，不把 superclass 已适配当成后续重复读取自动适配。exact-bridge 与 whole 等原数学入口不因存储方式被全局换成新 tail 来源。

exporter 的 prepare/plan/build 接线指向新 common-cut，并记录 reader、supplier、codec/storage 来源及实际存储闭包；上述 16 个数学/采样/写入函数不变。mesh reviewer 显式绑定新 exporter 哈希，并核输出 manifest/source/bytes 的相应身份。

mesh replay 本身不是整个连续证明链的唯一来源审计者。它没有独自硬绑定所有被导入数学依赖的全部身份；完整 prefix 连续来源闭包仍由 terminal、运行预检和最终来源清单承担。不能因一个采样 mesh replay 成功，便宣称所有连续 metric/curvature 或未来候选已经完成。

## 7. 最终 v4 纯检查器已读，但独立运行未付

已全文读取 v4。它的完整前向 source replay 设计避免了早先逆向全局替换遇到同名新 dict 后的计数歧义。旧失败仍保留；不是把未完成的检查涂成成功。

检查器预定核六条完整变换、34 个输入、原 sources 和数学函数不变、12 项负例，以及真实旧 M12 base 的 storage helper 和 reported 八路径整体移位。其正例明确只是把旧 base 放在两个 helper 身份位置；不制造 future common-cut candidate 或数值证书。fresh isolated child 用于确认 hash-only 入口未导入 NumPy/SciPy。检查器没有执行 angular、mesh、连续后台或新数学对象。

作者在失联前的实际执行链为：

- 开始 e21d05，session 68045。
- 完成 88ff38/exit0。
- 作者报告 SHA-256 f1daab8418dd20e722bfabf4688b813dc358300eed323dd04189747f973f380c。

该报告的完整字节目前没有恢复；上列只保存已经存在的作者来源记录，不重建或伪造报告。本审查人的最终 v4 Python 重放未发生。作者 exit0、十件文本 hash 相同、V8 完整 source replay 和 v2 的旧负例，均不能代替这项独立实际重放。

## 8. 当前可采纳结论与续接条件

可以采纳：最终四入口的完整静态适配、terminal-v3 迁移修复、旧 tail/reference 与数学语句的保留、全部恢复源码身份，以及本稿列出的实际纯文本核对。

不能记为已完成：

- 最终 v4 的独立 Python/旧包读取重放；
- 新 producer 的实际输出或未来图的 storage 闭包；
- angular/metric/moment/curvature 后台或整个闭图链；
- 任意新候选、网格、G5 或数学完成门。

A/B 的已有独立记录继续按各自原范围有效，不被这份静态恢复 note 扩张。执行器恢复后，先核实际脚本及依赖是否仍与冻结来源一致，再完成已授权的纯存储独立重放；不需要通过运行 BVP 或几何后台来替代该检查。

本文件以新文本路径封存，固定提交全文回读后交 root 登记。它保存一个可接手的真实断点，没有宣告整个研究完成。
