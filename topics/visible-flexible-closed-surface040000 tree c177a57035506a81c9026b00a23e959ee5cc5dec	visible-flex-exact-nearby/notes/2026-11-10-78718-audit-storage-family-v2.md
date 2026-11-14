# 新 prefix 分片存储家族 v2：来源修正闭包的完整独立审查

日期：2026-11-10。审查者：本会话未参与主 M14 数值候选优化的 independent_audit；会话 Astra-visible-flex-78718bd0。

## 1. 审查结论与准确范围

**通过此次冻结版本的完整存储语义与来源修正闭包审查。** 这里的“通过”由前一份完整 v1 审查与本稿对全部 v1→v2 差异的独立核对共同给出：v1 中两个报告函数、三个错误的旧来源路径已在另名 v2 源中全部修正；其实际消费者、源码哈希、终门选择分支和检查入口同时传播，没有留下已知的来源缺口。

这一结论不采纳有缺口的完整 v1 家族，也不把 v1 的实际执行回执移到 v2 名下。v1 原源、账本及测试保留。两个存储 core、十个未改变的 adapter 与完整数学函数审查继续按各自原字节成立。四件 v2 adapter 在已全文核过的 v1 上，只有本稿列明的来源路径、导入路径及相应固定 SHA 变化。所有数学公式、原 tail/reference 家族、终门误差与改善倍数条件保持。

这是一条可供未来真实生产调用的已审存储支路；**不是一个已通过生产链的曲面候选**。本次没有成功 CP 上的 producer/common-cut/candidate 整链执行，没有新的 metric/reach/G5 证书，没有真实网格，也没有最终原种子全链独跑。作者读取器报告里的 production_ready=false 在原报告定义的“只做有限合成检查、还未做真实候选生产”范围内保持准确。

前置完整审查为 [v1 完整审稿](2026-11-10-78718-audit-storage-family-v1.md)，20,819 B，SHA256 4912e2cd32bb2df8b8095d1e93e968bbe9417aa357894114caddd22cda230093。该稿完整覆盖 16 件源、原→v1 的 134 项变换、codec 字节等价、全部读取及证明消费者、M24 defining base 与 M64 expanded metadata、实际终门存储/账本函数及网格路由。本稿不是另做一次局部抽样替代那份审查。

## 2. 本次实际读取与独立核查方法

我全文读取了 [修正说明](2026-11-10-78718-storage-provenance-fix-v2.md)、9,745 B 的 [六源完整差异](2026-11-10-78718-storage-provenance-fix-diff-03.txt)、ledger-02→ledger-03 的完整差异和 12,678 B 的新读取器报告 metadata。此前 ledger-02 的每一项旧/新文本与 16 件源已经全文检查；本次完整 ledger 差异将未改的原 134 项与新增的三项明确衔接，不借助“摘要相同”代替实际源核对。

我另用 stdlib 编写并实际执行一次独立核查，不调用作者 builder 或任何数学 backend。真实工具 **ef561e，自然 exit 0**。它完成：

1. 从 14 件原数学/恢复源逐件读取实物，核大小和 SHA；依 ledger-03 顺序执行全部 137 项旧字符串→新字符串替换，每一步要求旧字符串恰好出现一次；最终输出字节与相应实物新源码全等。
2. 独立用 AST 遍历比较原/新完整函数集合、188 个完全相同函数，以及所有改变函数的准确名字；与账本逐项相合。AST 数量仅佐证完整字节关系，不替代改变函数的语义检查。
3. 比较 ledger-02 与 ledger-03：十个 adapter 的整个来源行完全相同，两个 core 的实际 SHA 保留；只有四个 adapter 另名。共十二件源字节不变。
4. 直接从实际六对源码重新生成完整 unified diff，与冻结 9,745 B 文本逐字一致；核 builder-v3 的 NEW 表与账本输出名完全一致。
5. 不 import 数学程序，从 AST 读取新终门的 13 项 PREFIX_SOURCES、21 项原 SOURCES，以及新 angular 的 11 项 SOURCES；对每一个实际文件重算 SHA。原 21 项 tail/reference 表与 v1 完全相同。
6. 比较新旧终门 REFERENCE、BOUND、FACTOR、LOWER 的完整赋值 AST；比较 prefix_storage 与 prefix_storage_ledger 的完整函数 AST。全部相同。
7. 核四件 v2 中不再出现三个已另名 adapter 的旧 v1 路径；核两个报告函数现在声明实际导入链的 polynomial/continuous 来源。
8. 对 root 新读取器报告的全部 33 项 source_bindings 和 script 自绑定重新读取实物、核大小/SHA。将实际行为结果与本人 v1 独跑报告比较，除了脚本/来源身份、执行时长与临时 fixture 目录，其他全部字段一致。

独立结果为 [v2 来源闭包实际检查](2026-11-10-78718-audit-storage-v2-source-closure-01.json)，18,128 B，SHA256 **7215eeda5b88d5895e804f659873762c348b8a3a15c19fbaaffa081c07a8a6dd**。该报告明确 solver/backend 调用为零，未重复读取器执行，未支付任何候选几何门。

两 README 对此前已全文读版本的 diff 也实际为空（ce2e93，exit 0）。没有修改任何原数学源、主计算入口、HANDOFF/open/results 或 git 状态。

## 3. 两个原缺口如何逐项消除

### 3.1 metric-budget 的实际导入与诊断报告一致

v1 中 metric-budget 实际导入新 arithmetic，其 poly 指向新 polynomial，poly.base 指向新 continuous。诊断报告 backend_sha256 却还列旧 polynomial、旧 continuous。这两个路径是完整家族的真实来源错误；即使其数值公式没有改、该诊断不充当完整 angular 证明，也不能用它声称所记录来源就是实际执行来源。

v2 的完整函数差异只有：

- 导入 arithmetic 从该家族 v1 换到另名 v2；
- backend_sha256 中 arithmetic 同步列 v2；
- polynomial 与 continuous 分别明确列 78718-prefix-metric-polynomial-storage-v1.py、78718-prefix-continuous-hermite-storage-v1.py；
- common-cut 仍列实际未改变的 78718-prefix-common-cut-storage-v1.py。

原全部 interval 选择、metric budget 计算、输入 hash、报告的 full_prefix_recertified=False 与 new_map_constructed=False 均未改变。程序输出的 backend 来源由实际 SHA 动态取得，所列文件与导入链吻合。

### 3.2 arithmetic 的独立 tail CLI 来源报告一致

v1 arithmetic 的 run 报告 polynomial_backend_sha256 已列新 polynomial，但 interval_backend_sha256 还列旧 continuous；实际 poly.base 是新 continuous。v2 只把后一个路径改为实际新 continuous。它不改 tail 曲率、导数、多项式界、分割或输出数值算法。

这个 arithmetic 独立 tail CLI 原本不在声明的 prefix 正式生产路由：原 tail 证书仍用原 tail 家族。因此不能把此缺口扩大成主尾部数学证书无效，也不能因它不在当前生产路由就允许一个公开来源字段继续写错。此次另名修正确实把它一并解决。

新增的三个唯一变换正好是一处 arithmetic 报告路径与两处 metric-budget 报告路径。137=134+3；其它旧变换改变的是跟随新文件名/新 SHA 的依赖身份，不是另增数学步骤。

## 4. 四件 adapter 和两个入口的完整传播

| 新文件 | 本次实际改变 | 为什么足够 |
| --- | --- | --- |
| angular-arithmetic-storage-v2 | 一个 interval backend 报告路径 | 实际 polynomial/continuous 导入仍是已审同一实现；报告与它相合 |
| metric-budget-storage-v2 | arithmetic 导入/报告改 v2；两处 backend 报告改实际新源 | 消费修正 arithmetic，同时消除自身两个旧来源 |
| angular-metric-storage-v2 | budget、arithmetic 的路径和 SHA；实际 helper 导入改 budget-v2 | 11 项 SOURCES 与运行时 helper 链同时闭合 |
| terminal-error-storage-v2 | arithmetic、budget、angular 三项 prefix 路径和 SHA；angular 证书选择和 prefix_source 核验名 | 不会把 v1 angular 证书身份误当 v2；正式候选门检查的是完整新来源链 |
| build-storage-adapters-v3 | 四个输出名，三个额外 report rename | 所有原源 SHA、原变换的唯一性要求、拒覆盖机制及数学保持 |
| check-storage-readers-v2 | builder-v3 与 terminal-v2 两个入口名 | 实际重建/import/终门子程序检查指向本次新家族 |

四个 adapter 的完整字节差异已在第 2 节逐字验证。旧 arithmetic/metric-budget/terminal 的数学表达式均没有替换；angular 的 actual helper 指向的 budget 数学仍同源。sourcepins 更新所产生的新 hash 不被当成一个新数学定理，而是准确指认已全文审查、已精确派生的实现。

完整新终门的 13 项 prefix 来源中只有上述三项变化；21 项原 tail/reference 来源完全保留。angular 的 11 项来源中只有 arithmetic、budget 的对应名字和 SHA 变化。terminal 的 metric 选择继续要求 geometry SHA、logical data SHA、entire_prefix_covered、完整 partition 与其余原门；它只是把识别的 angular 来源从家族 v1 改为 v2，不增加替代的宽松分支。

BOUND、FACTOR、LOWER 与 REFERENCE 的赋值 AST 均全等，因此原 2e-9 门、改善倍数常数和原 reference 身份没有变动。没有把原 tail family 换成新 prefix arithmetic，也没有把 M12 旧证书移植给新图。

## 5. 未改变部分为什么继续成立

两个 core 与十个 adapter 保持实际字节和先前审稿 SHA。因此完整 opaque gzip/NPZ payload P 的分片/拼接等价、每片压缩前后 hash 与大小检查、严格 descriptor schema、写前冲突预检、读取时长度与全局 hash 核验不变。dtype、shape、内存顺序、NaN payload、正负零等逻辑 NPZ 字节的保持也不受本次报告路径变化影响。

SharedHermite、ExactHermite、fullxyz、mirror、supplier、moment、common-cut、closed-budget、mesh exporter 与 reviewer 都是上述十个未改 adapter 的成员。镜像 parity 只执行一次，原 NPZ payload 保存规则、精确 interval 读取和源码闭包均继续按 v1 全文审查。

尤其 M24 是 defining base 的 storage 维度；M64 是 common-cut 扩展后的 metadata 维度。common-cut 先以 base 路径装载旧模式，再做原 padding/correction；helper 不得以 M64 expanded metadata 冒充 M24 defining base。这些实现未改。terminal.prefix_storage 和 terminal.prefix_storage_ledger 两个完整函数 AST 也未改：仍实际读取 defining base/descriptor/parts/helper/codec 的闭包，而不只相信旧账本字段；仍把 common-cut logical hash、storage reference 和实际文件账本逐项核对。

mesh exporter/reviewer 不依赖此次另名的 arithmetic/budget/angular/terminal 路径；它们绑定的 common-cut、两 reader、helper、codec 与 exporter 审查 SHA 都未变，故无需为了来源修正再制造两个等价新网格入口。原 whole-metric-reach 与 exact-bridge 的接口也是先前已核的 JSON/hash 消费，不暗藏一个新增单容器 prefix 读取点。

先前 v1 routing/source-pins 记录是历史冻结身份，不应拿它的四个 v1 路径作为修正家族的新生产命令。未来真用这条支路时应选本稿表列四件 v2 及另十二件原字节源，并将真实新报告绑定到它们。当前 success-only 后链计划以原单容器家族为首选；本稿不代替该计划自己的完整审核。

## 6. 实际执行证据及不重复测试的理由

本人先前冻结 reader-v1 的真实独跑是 **313f38，exit 0**，报告 [独立读取器实跑](2026-11-10-78718-audit-storage-readers-check-01.json)，12,732 B，SHA256 a1fc17051140e4f99c73ed887fffff04ba3ce2282822ecef63f493d3dea5e759。完整测试覆盖两种有限 synthetic payload、原/新浮点与精确读取器、全部 14 源重建、16 新源 import、actual terminal 两个存储函数的 stdlib-only fresh 子进程、M24/M64 区分和三个破坏案例。

root 对新家族的实际测试记录为启动 **5a9e17/session97276**，完成 **d9d110，exit 0**；其报告 [reader-check-03](2026-11-10-78718-storage-readers-check-03.json)，12,678 B，SHA256 **0cd8154250c031eb41304d07374f4b1cc7692b5be8b612c730e62b0abd4dcdb7**。这是 root 的新源实际执行，本人没有冒称亲手重跑它。本人本次已完整读其 metadata、核全部实物绑定并与本人旧版执行结果逐项比较；差异只在预期的来源身份、时长与 fixture 路径，行为完全相同。

由于 byte codec/reader 数学和两个 terminal 存储函数未改变，且新检查入口已由 root 实际指向 v2 重跑，本次重复同一有限 reader 测试不能解决新的具体风险。独立 ef561e 专门解决剩余的风险：全源变换、报告路径、依赖传播及 hardpin 闭包。两份真实执行证据与这份来源证据分别保留，不互相冒充。

root 原 core 的 4 正例/23 拒绝报告仍是原实际记录，其代码与 core 字节不变；本次没有把它再算成一轮本人执行。所有有限 fixture 检查都没有运行成功 CP 上的 producer、完整 common-cut 或完整 candidate 门，报告的这些 false 状态保持准确。

## 7. 本次冻结身份

| 文件 | B | SHA256 |
| --- | ---: | --- |
| scripts/78718-build-storage-adapters-v3.py | 21748 | 110457adcd109dcfd28cc285dc6458c97b37cd68858962b6ad44a5d3d8f43683 |
| scripts/78718-check-storage-readers-v2.py | 13224 | 78faf566f9b3ca3800d221b02fcd0363f64826025c4a4f8ac3c359bc42747565 |
| scripts/78718-prefix-angular-arithmetic-storage-v2.py | 23060 | 4977cb407bc9cdd64a580c999727a9978bf4041011e89cab192be7ecd2c2f5dd |
| scripts/78718-prefix-metric-budget-storage-v2.py | 9661 | 18599b65771eae53199442589547105292489c323aac333e5eee6f2dacadb3aa |
| scripts/78718-prefix-angular-metric-storage-v2.py | 24403 | 7f60b8431c10ef93878049be0ae9d9677df268b7cb3963315096103bafdd0dc1 |
| scripts/78718-prefix-terminal-error-storage-v2.py | 48878 | 882086b30a5af04fbac558234295eab035e24608727c605a9dfd9aae36a0cabd |
| notes/2026-11-10-78718-storage-adapters-source-ledger-03.json | 61588 | 1b7e05df897d10e77c056151e2beb0b8eee1ea7e86e28fb9bdef9899b22a6dde |
| notes/2026-11-10-78718-storage-provenance-fix-diff-03.txt | 9745 | 100fd59c1ca1281f8b455dbf4dc77c019cfc0e715fae38b453c6c18477fc9c9b |
| notes/2026-11-10-78718-storage-readers-check-03.json | 12678 | 0cd8154250c031eb41304d07374f4b1cc7692b5be8b612c730e62b0abd4dcdb7 |
| notes/2026-11-10-78718-audit-storage-v2-source-closure-01.json | 18128 | 7215eeda5b88d5895e804f659873762c348b8a3a15c19fbaaffa081c07a8a6dd |

原 16 件 v1 的完整身份及未改数学来源表见前置审稿；独立 source-closure JSON 保留本次每件实际旧/新源、全部 terminal pins 与准确范围。所有文件均低于用户单件 5 MB 限制。

## 8. 对当前主研究状态的影响

本次未读取消耗任何主 solver 的工具会话，未改变 M14 参数、初猜、预算、方程、BC 或停止条件。restart8000 主运行是否有真实自然出口、是否产生自己的成功 CP/尾包，仍必须由 root 持有的真实会话回执及完整出口门独立判定。来源/存储层通过不会生成这些事实。

若未来生产实际选用分片家族，仍需以同一真实成功候选重新运行该图的完整生产链、全图 metric/reach/误差与网格门，按 README 原要求提供真实原种子独立重跑。这里不新增 README 之外门，也不把存储修正降低成主问题完成。
