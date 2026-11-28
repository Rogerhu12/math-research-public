# RET83：两份旧 prefix-cache 身份描述的完整保全

本批只将两份历史缓存身份 JSON 从当前树移出，毛计 **281,565 字节**。完整原文仍由固定公开 Git 提交 `a7ee59c79535235b4161da7780b77556e9760940` 和各自 Git blob 恢复。完整保全账是 [legacy-prefix-cache-identity-retention-83-provenance.json](../computations/legacy-prefix-cache-identity-retention-83-provenance.json)。

两份候选的正文分别超过 100 KB，本次没有读取。分类依据是已完整读取的原生成源码、真实原参数、原实际 adapter 的源码 SHA、原小检查／资源记录、完整历史清理记录及树元数据。没有读取二进制缓存或运行科学程序。

## 1. 精确对象与恢复身份

| 对象 | 原字节 | whole SHA-256 | Git blob |
|---|---:|---|---|
| q096 三点检查的 identity.json | 138602 | `7a904bf3fedd45dcba2d7840cd2fd9506657955ddc5801bc7b3ff6fc06a2f1be` | `12b4e03dabdd03840c380cb4f137aaafd0f772cb` |
| 已退 q122 缓存的身份副本 | 142963 | `aeafb7602a850aab4408a039b607bc4e369cdceb6355e9aa8161ae2632ebe5c7` | `003c5b292020bfec15e9251c7d8c0eb1ad43853e` |

精确路径：

- `notes/2026-11-12-strong-q096-prefix-call-cache/6d879d5dd2101cee8e9b15e8b07b01c5aebbc161d5ade458d1d6d322c666ca80/identity.json`。
- `notes/2026-11-13-strong-q122-retired-prefix-cache-identity-r1.json`。

路径均相对本课题根目录。两个 whole SHA 都来自原已刊小记录，没有把文件名内的 digest 当作 whole SHA。q096 whole SHA 的原依据为 8746 字节的 prepared-stable-files；q122 的依据为原 3632 字节 completed cleanup 和 596 字节 retired-cache manifest。其完整文件身份与固定恢复位置在保全账中。

## 2. 原 writer 写了什么

原完整 writer 是 `computations/strong_prefix_evaluation_cache.py`，20928 字节，SHA-256 `97a2b5b0eccbef3a9645167b2c91c73503a820507136b10bfdb300a97df7f6ea`。q096 与 q122 的真实 original adapter 都逐字记录这一 SHA；本次取得的完整源与其相等。

`Runtime.initialize` 的身份对象完整字段为：

- `schema`、`source`、`runtime`、`batch_sizes`、`cached_operations`；
- `mathematical_side_effect_restore`；
- `no_boundary_or_tail_or_acceptance_cache`；
- `diagnostic_counts_and_internal_memoization_warmth_not_replayed`。

`source` 包含实际文件 SHA、编译函数 SHA 和 adapter 文本变换；`runtime` 包含 Python、NumPy、SciPy、平台、CPU、字节序和线程环境。生成操作是先对完整 identity 作原 canonical JSON，再以该 canonical 文本的 SHA 命名目录，最后写入 canonical 文本加一个换行。

因此目录名 `6d879d…` 与整个 identity.json 的 `7a904b…` 分别对应不同字节对象，不可互换。原 q122 身份副本的目录 digest 没有从未读正文猜出，保全账也没有补造。

原 `Runtime.request` 才另外建立当前调用的完整对象与 t/y/p 描述。`Runtime.save` 将真正的 t/y/p、fun、J、PJ 数组字节写进另一份 `key.bin.gz`。这两份待退 identity.json 不承载那些数组。原缓存没有保存边界判断、Newton 接受决定、RMS 验收或非线性尾部结果；本批不扩大其能力。

## 3. 全来源与全参数仍完整可取

保全账列出 47 份由原两个 adapter 与原 launch plan 共同登记的本地科学／包装源码完整文件记录；本次取得的 whole SHA 均与原声明相同。另外列出实际资源 supervisor 与完整 archive reader，共 49 个保留源码记录。科学数学正文没有改动、截断、重新解释或执行。

两个原 adapter 分别为：

- q096：47584 字节，SHA `00177401f1c7bc077859cc223a95807e9b2be7753b29b5092e90504d08b85030`，固定历史 blob `f4b638d45b3451be16651c5ffccaf0994898aec6`；
- q122：66678 字节，SHA `bbfcc81eb32780cde567af68a040532ef8df010e9eca372525a5a42b2c2cb059`，blob `f261679b211cd0c8e2ba8ebcca0903ce8bba5403`。

它们完整保存原 source_sha256、编译变换、实际内层 argv、缓存预算及输入绑定。各自的 `prepared-only` 状态原样保留，不因后来独立的资源／结果记录而改写 adapter。

本批同时保留并登记三个完整计划：

1. q096 原三点检查的 6291 字节 plan；
2. q096 r4 的 7192 字节 continuation plan；
3. q122 m28 pure-secant 的 12957 字节 launch plan。

账中保存其原全部 run argv 和 owned resource argv；完整 warm profile、target、外部 shift、原输入与既有 warm screen 则仍在相应 whole 原计划中，没有选字段另造一个不完整计划。资源预算、线程、所有原参数值与原输入 SHA 均不改。

q096 原检查使用 M24、2004 个节点和三个真实抽取点；原 argv 的 max-nodes 为 2400，radial/collocation batch 为 16/12，node heap 为 96，young semispace 为 4，prefix cache 预算为 192 MiB。q122 launch 的原 batch 为 48/24，point cache 为 8，heap 为 512，young semispace 为 16，max-nodes 为 3600，prefix cache 预算为 256 MiB；原 full secant scale 为 2。上述仅复述原完整参数，不安排任何新计算。

## 4. q096 实际结论及未完成边界

原 2748 字节 check 记录：完整三个点的 fun/J/PJ original-miss-hit 字节相等，selected parameters 与 baseline Flow 恢复，t/y/p 一 ULP 改变的 miss、几何参数改变与相应真实 RHS 比较、reference chart／profile 改变 miss，以及负零 roundtrip，均有原记录。该检查的 `finished` 和 `passed` 为 true。

原 supervisor 从 2026-11-12 19:32:44.513401 UTC 到 19:32:52.533001 UTC，实际 exitcode 0、wall_seconds 8.02857548099928、peak_rss_kib 178792，wait4 已观测。缓存 summary 为 hits 8、misses 9、completed_writes 9、write_errors 0。原检查明确 **没有 Newton、RMS 接受或 Node 工作进程，也没有新解**。

后续 r4 计划的状态仍是 `prepared-not-executed`。其中记载更早 r3 的 tool exit 137、child exit -9、原因 unknown、complete Jacobian false、新 accepted steps 0。这些失败与未知全部保留；本次不把 r4 的计划状态或三个点检查升级为完整求解结果。

在固定现树中，q096 老缓存目录只剩这份 identity。原 prepared-stable-files 曾列出的九份独立 .bin.gz 的 size、whole SHA 和历史 Git metadata 仍完整保全；它们已经不在本次现树中，本批不重复删除，也不声称本次重新生成过它们。

## 5. q122 原有限结果与先前清理

原 owned supervisor 确实记录 q122 pure-secant 实际 exitcode 0，2026-11-13 10:55:14.992592 UTC 开始、13:02:47.314175 UTC 完成，wall_seconds 7652.336446283998，peak_rss_kib 440024。

独立原 accepted-fullflow recovery manifest 23782 字节，SHA `400c60e4314203b197b3d3079d435c1e739ae5c2c1e78b06ca4d8723c59dfe3c`，记录 M28、2587 节点、1024 角、原有限验收 complete，原 RMS 为 9.957361490725915e-8、容许值 1e-7；真实物理 BC 为 6.082947372145787e-11、容许值 1e-10。完整尾部、原全流、raw、primary 和资源关系仍在该 whole 原记录中。它明确不声称无限闭合、闭面握持或 reach。

原 3632 字节 cleanup 记录的行政事件发生在 2026-11-13 17:09:36–37 UTC：旧 q122 函数/J 缓存目录当时已有 1116 个文件，实际移除 1116 文件、2 目录。它记录 science primary 与 full-flow manifest 的 before/after SHA 完全相等，活动 q126 A 缓存和共享 tail-stage 缓存未触动，并把这份 142963 字节 identity 副本保留。原 free-space 读数受并发 publisher 影响，文件也没有把差值当作独占测量。

本批不重演那次删除事件。原一次性 copy/cleanup 程序没有在本次来源集中定位；这一限制明确保留。身份生成器及实际原调用已明确，身份副本自身由原 whole SHA 与固定 Git blob 无损恢复，不为这份历史行政描述添加一个网络或清理事件重演门。

## 6. 旧 reader 仍然需要原完整身份

本批没有宣称这两文件“没有消费者”。

`strong_prefix_evaluation_cache.py` 的 `atomic_new` 会在同一 identity 目录已存在时比较完整字节；`Runtime.load` 按完整 request 与独立 binary entries 读取数值。另一个保留 reader `computations/strong_prefix_cache_archive.py` 是 10369 字节，SHA `1698ecaefa8438d19cd0c2d6cfdf17d81ae51dfcb102933aedbaa7328624adb4`。其 archive 入口直接读 identity.json，检查 canonical digest 与目录名；其 restore 路径核验整个 archive 和每一 member，并保完整 J/PJ。

因此以后重开旧缓存目录，必须先按固定 Git 把原 identity 恢复到原路径；需要的数值缓存 member 也按各自完整历史记录恢复。原 archive reader、原 source/hash guard 和旧数学验收一律不放松。不能用小摘要替代原 identity，也不能把新机器重算出的另一份 runtime identity 强塞进旧目录。

原 prepared-stable-files 及 retired-cache manifest 的链接同样遵守这条恢复关系。它们是历史证据引用；从当前树移走文件不等于历史证据不存在。

## 7. 当前保留与历史全字的区别

固定候选恢复提交为 `a7ee59c79535235b4161da7780b77556e9760940`。更早已退小检查和 input 记录的完整恢复基点为 `60321451c058c6a51da58c37ae5ec6f2d1145f74`。不同 record 的恢复位置各自明确，不能拿旧 queue、旧参数版本或格式调整前的 whole SHA 充当当前文件检查。

保全账明确列出实际当前应保留的 57 个 whole 文件；原数值 input 另以完整原 adapter/plan SHA 和固定历史 Git metadata 登记，压缩正文未读。原科学来源、全部参数和原 actual 结论不删。未重做全外库数学审查；旧 identity 所含完整 foreign/source 闭包仍在其精确历史全文中，未来实际恢复时照原 reader 验证。

root 只需在普通提交前将两条删除项与 fresh tree 的 path/blob/size 对应，再完整加入本说明、保全账和交付总表。若某个保留描述后来仅作合法词法格式整理，其旧 whole 仍按自己的固定提交恢复，不把历史版本误当当前 guard。

## 8. 本次工作的边界

本次进行了原小源和小参数／结果记录阅读、Git metadata 对应及新保全文件的文本哈希。没有读取两大候选正文、二进制 payload，没有运行原检查、Newton、尾部、F/J/root、AST、fixture 或新 benchmark，没有改任何 ref、queue、科学源、参数或证明。

完整输入、结果和失败由原 whole 文件与本账的具体恢复关系保存。缓存身份跨环境可能变化，这不是丢失旧身份的理由，也不是本批宣称任何新数值结论的依据。
