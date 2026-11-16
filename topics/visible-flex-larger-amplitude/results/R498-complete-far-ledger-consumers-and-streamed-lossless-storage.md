# R498 — 完整传播账本的实际消费者、流式压缩与原行责任

- 日期：2026-11-16。
- 作者：ChatGPT（AI，geometry 协作代理）。
- 可信度：**已证明（限下述表示等价和实际源码依赖命题）；未运行新科学、未测压缩率、未取得新接受场。**
- 本结论由 [R478](R478-request212-complete-shallow-physical-sampling-and-BVP-startup-storage-stop.md) 的真实资源停止提出。它不修改 request212、214、216 或已冻结的 R496；后继 request218 必须按自己的真实来源组合接线。

## 498.1 本次已经查明的资源事实

request212 的浅逆采样确实完成全部 112 个 far 族、112 条联合 nominal 行、13,850 个唯一物理点和 16,128 个字段出现位置。原 sampler 的必要读回没有剩余 point/field 记录。随后原 launcher 在启动 BVP 前真实观察到：

- 实际可用空间为 11,761,553,408 B；
- 原启动资源要求仍为 34,359,738,368 B；
- 因此实际科学子进程没有启动，两个求解阶段、native/current-H/J/FD/fullDN/final/audit 及 accepted450 都未产生。

其中，临时文件 far-accepted-panels.jsonl 实际为 95,028,212,980 B、1,604,049 行，SHA-256 为 aba486e649d354a61857e03de6927a300ed1373b34bc41676c36025354af177c。该文件包含每个 prepared panel 的完整入射状态、系数行引用及完整 Prüfer 包围。它不是只含几条最后端点的结果文件。

这些是 R478 已返回的必要事实。原 rules 必要正文因 94,138 B 超过 90,000 B 没有回传，且原主动清理实际跳过；本结论没有据此补填未知规则正文或声称全部临时文件已经安全退役。以下判断来自实际源文，不从约95 GB的尺寸推断数学失败或压缩效果。

## 498.2 实际写入者与消费者

以下均为已刊源码的文字核对；没有导入或运行这些模块。

| 实际入口 | 实际读取或写入 | 与大 prepared 账的关系 |
|---|---|---|
| f12f 的 Journal.add/finish | 对原 canonical(value) 写一行并 flush；累计原字节 SHA、长度、行数；最后 fsync/close | 32b0 原账本的真实明文 writer |
| 32b0 的 point_column | 先写 prepared panel，再写候选 tube，最后写 commit；commit 之后才安装 next_state/coverage/hull | prepared 与 commit 的索引及事务次序必须保留 |
| 32b0 的 main | 建十条 Journal，完整传播后形成 general-row JSON、geometry.json 和四个 f64le 数组 | 全部账本 descriptor 留在 result.detailed_ledgers |
| 47d7 的 sampler_readback/line_stream | 对 prepared、commit、coefficient 等完整读字节和行数；对 modes/candidates/coverage/unpaid/numeric selection 另解析所需行 | prepared/commit 的读回没有逐值再证明，但原完整字节身份仍实际核验 |
| c71d 的 bind_current_native | 实际 config、sampler result、完整 C 绑定和 geometry JSON | 不读取 prepared 行的数值正文 |
| d015 的 loadGeometry | sampler result、geometry JSON、node_radii/node_mu/field_geometry/far_matrix 四完整数组 | 完整 nonlinear/root/RK/means/J/audit 的数值输入来自这些实数组与真实 runtime；未解析 prepared 账 |
| 02e1 的 TailClient 与 fae2 owner | 真 config/source closure、由 worker 装入的几何和实际当前 H | 不将 prepared 行当作 native 数值输入 |
| 43f 的 native_context/Checkpoint | 真 geometry result/JSON、实际 client/owner、source closure、最终响应/FD/final/audit | checkpoint 不复制完整几何 payload，也没有把 prepared 行读成有限场 |
| 5cc 的 radial bind/produce | 真 accepted450、实际 final native/config、再次调用真实 worker.loadGeometry | 径向重放的上述输入仍需保留；没有读取 prepared 行 |
| 6a5 的 shared prepare/load_shared_bundle | 真 radial 节点、accepted prefix、plan/B/assembly 和完整来源 | 不从原 far prepared 账直接构造 shared 场 |
| 5f14 的 bind_original_far/bound_stream | REUSED_LEDGER_NAMES 的每一完整文件均按原 bytes/rows/SHA 实读；prepared 取 selected=False | **这是仍存在的后继真实消费者，不能直接删除** |
| 5da13 的 bind_old/readback | 调用 5f14 的完整旧112绑定；另真读原 far inverse span；新 mode 账也由 bound_stream 读回 | 增 M 的 union 仍继承全部旧 prepared/commit 来源责任 |

这里的“不读取 prepared 数值正文”不等于“后续可以删除文件”。5f14 明确列出 far-all-mode-rows、far-complete-tubes、far-inverse-leaf-coverage、far-panel-commits、far-accepted-panels、coefficient-boxes、sample-inverse-leaves；joint 来源还包括 numeric-far-row-selection。它对每一项实际调用 bound_stream。

在该调用中，far-all-mode-rows 全部解析，sample-inverse-leaves 只保原 far anchor span 的对象，其余指定文件仍完整读字节、核 LF 和行数。然后每个 mode 的 complete_step_rows、complete_panel_commit_rows、complete_far_tube_rows、complete_far_leaf_coverage_rows 都必须从上一 stop 连续接起，最终恰好覆盖对应原账本的 rows。实际 Q/Pi 数值矩阵还要同全部原 coefficient words 逐字相等；原 node_mu 最后一个字必须等于所复用 far 的原 mu 字。

因此，**按现有完整续链合同，没有证据允许把95 GB账本仅换成一个摘要或提前删除**。首个 BVP 不数值消费它，并不能绕过随后真实的 same-far/union 输入绑定。本结论不把“只核 hash”改写成“没有消费者”。

## 498.3 不删行的最小表示

新增标准库 helper：

[geometry_20261116_complete_jsonl_gzip_storage.py](../computations/geometry_20261116_complete_jsonl_gzip_storage.py)

和明确 literal 合同：

[r498-complete-ledger-gzip-core-source-plan.json](../computations/r498-complete-ledger-gzip-core-source-plan.json)。

对 original canonicalizer 实际交给 Journal 的第 i 行字节串 $r_i$，定义

$$
g_i=\operatorname{gzip}_1(r_i),\qquad
S=g_0g_1\cdots g_{n-1},\qquad
R=r_0r_1\cdots r_{n-1}.
$$

每行是一个完整 gzip member；writer 使用 level=1、mtime=0，先形成该单行 member，再完整写入、flush。不存在先写全明文文件再压缩的阶段，也没有保留第二份明文 ledger。内存只增加当前一行的压缩表示及压缩器工作空间；并未把全部账本积累在内存。

RFC1952 §2.2 把一个 gzip 文件定义为依次连接的 members；它是无损格式。Python3.11 的 gzip.open/GzipFile 提供二进制文件流接口，gzip.compress 对给定 bytes 生成 gzip 表示。依据这些原接口，完整解码 $S$ 恰得 $R$，并不是对 JSON 数值作另一次格式化。[RFC1952](https://www.rfc-editor.org/rfc/rfc1952.html)；[Python3.11 gzip](https://docs.python.org/3.11/library/gzip.html)。

本实现没有对 $r_i$ 做 JSON load/dump、浮点转换、区间取中心或字段选择。它接受原 B.canonical 的实际 bytes，只核该 bytes 是一条完整 LF 结尾记录。因此所有有符号词、完整区间、误差、状态、候选、分母条件及原 row schema 均在解压后逐字保留。

### 条件命题

若原 producer 对一次实际执行形成有限序列 $r_0,\ldots,r_{n-1}$，原 canonical 函数没有改动，每次新 writer 的完整 add 成功，且所绑定 gzip 解码满足其格式规范，则新存储解码得到的完整逻辑流就是原序列的逐字连接。按原行计数的任意闭、半开 span、事务编号和前后缀地址不变。

证明由每个 member 的无损逆和连接次序直接得到。行 i 对应 member i，但 consumer 不把 member 的压缩字节偏移当作行号。整个原算法仍按解码后第 i 条 JSONL 行工作。对于任意 span [a,b)，其值就是原 $r_a,\ldots,r_{b-1}$，没有选择、遗漏或重排。证毕。

这个命题是同一次给定实际逻辑流的表示等价，不是两次不同墙钟执行必然产生同一末状态的结论。压缩和解压会消耗时间；原预算可能让新实验在另一真实边界停下。所有状态和停止仍以该次实际输出为准。

## 498.4 原 prepared/commit 事务

32b0 原 point_column 的次序是：

1. 在内存构造完整 incoming state、candidate、准备写入的 step 和预期索引；
2. 原 budget.check；
3. steps.add(step)；
4. 按原顺序写全部 far_rows；
5. commits.add(...)；
6. 无中间新的资源检查或科学运算，安装新 state/coverage/hull。

R498 只替第3步所用指定 Journal 的存储表示。每个 gzip member 的完整 header、压缩数据和 trailer 都在 add 返回前实际写出；没有一个等待“整账最后 close”才补写的压缩缓存被偷放在 commit 之后。新 helper 的 rows 仍是成功完整写出的原逻辑行数，bytes/hash 内部仍保原逻辑流含义；descriptor 的 stored 身份另列。

若写入中途失败，新 helper 不递增该失败行的逻辑 rows，也不假称该行已经付清。它记录真实原行索引、原行 bytes/SHA、完整预期 encoded member bytes/SHA、已写 member 前缀长度和原异常。原 point_column 的异常路径仍负责保当前 in-flight、未访 stack、prior state、transaction_open 和完整未付后缀。已经存在的 encoded 前缀不被删除。

若 prepared 完整写成但之后原 tube/commit 失败，仍按原 uncommitted spans 处理；gzip 不把 prepared 行自身改成 paid。只有原 commit 加原后续状态安装才属于原已付前缀。若外部强杀导致没有完整 result 或 trailer，只能按实际存在字节读回并标记不完整，不能由若干可解码行补造完整 mode。

fsync/close 失败按原 I/O 异常传播，不被转成成功 descriptor。原预算 RuntimeError、信号及其他异常类型穿透 storage reader，不能被改造成数学 ArithmeticError 而被上层数学 guard 吞掉。

## 498.5 两套身份，不把压缩 hash 冒原字节 hash

完整新 descriptor 的顶层 file/bytes/sha256 指**物理存储的 gzip 文件**；rows 仍指原逻辑行数。decoded.bytes/sha256/rows 指完整解压后 canonical JSONL 原流。storage 中明确：

- schema = R498-complete-canonical-JSONL-gzip-members-storage-v1；
- encoding = concatenated-gzip-members-one-original-JSONL-row-per-member；
- level、完整 member 数、是否完整及真实失败记录；
- 原字节没有重新格式化、原行序/索引未变、没有明文镜像；
- 实际 Python/zlib 版本和 mtime=0。

stored SHA 不冒原 decoded SHA，decoded SHA 不冒原磁盘文件 SHA。Python3.11 mtime=0 的 header 细节可依实际 zlib 改变，故本实现记录真实 stored 身份，不承诺不同 runtime 的压缩字节逐词相同。[Python3.11 gzip.compress](https://docs.python.org/3.11/library/gzip.html#gzip.compress)

旧明文 descriptor 仍按原 bytes/rows/SHA 使用；没有 storage 字段的 .gz 文件不被此 helper 当作已登记的新表示。所有实际 member 必须仍处于真实 RUNNER_TEMP、原独占目录和非 symlink 的完整路径。

## 498.6 后继仍完整读，不能用 descriptor 豁免正文

新 bound_stream 保留原参数位置：directory、descriptor、原 budget、selected、visit、progress。

对于新 gzip 表示，它先按块读完全部 stored 字节并核实际 size/SHA，再按二进制 gzip 流逐原行解码，核每行 LF、完整 decoded bytes/SHA/rows。selected/visit 的选择语义和原函数相同：没有指定 selection 时解析原全部行；选择只影响保留/解析哪些对象，不影响完整流的读取与身份核验。

这两遍都调用原 budget.check，不创建新钟，不把读前来源核验移到未计时的后台，也不省掉任何未访原字节。中断时同一个 progress 对象保物理文件、declared stored/decoded 长度、已读 stored 字节、已读 decoded 字节、当前原行索引、行 bytes/SHA、真实阶段和异常；complete_original_scope_returned 保 false。

对于旧明文账本，仍以原原始行流读取并核原身份。没有因为新增 gzip 路径取消原文件包含关系、source、原 mode span 或原 mu/matrix 的核对。

原47d7必要 reader 本来已经按 .gz 后缀使用 gzip.open，并返回 decoded_stream_bytes/sha256；R498 的最小新增是把这两项和 decoded 期望真实比较，不只核压缩文件 hash。成功 prepared/commit 仍只是字节和行数的完整读回，不被提升为逐值数学再证明。全部 original unpaid、mode 失败、point 地址、closed fragments、异常及未返责任仍用原选择规则。

## 498.7 四个实接点及表示范围

本次精确 literal 合同基于原32b0、原47d7及 R496 已冻结49视图中的两个实际输出。每条 replacement 有完整 before/after/count；预览文字身份可复核，但不代表 request218 最终 source closure 已生成。

| 角色 | 精确变化 |
|---|---|
| 首个 joint sampler | 只有 far-accepted-panels 选 GzipJSONLJournal，传原 B.canonical，level=1；其余九账本、所有 JSON/四数组、完整采样计划不改 |
| 同 far sampler | 显式登记新的首 sampler 来源；bound_stream 调新完整 stored/decoded reader；原 source/mode/span/mu/matrix 条件和新 grid 科学正文不改 |
| incremental-M union | 原112仍经上述完整绑定；只有 new-mode-accepted-panels 选新 writer，传原 S.B.canonical；新 M deep、真实新增 modes、新 grid/native 全责任不改 |
| 首 sampler 必要 reader | 实际登记新首 sampler/helper，保原全部选择；对 encoded stream 追加 decoded 期望比较 |

同 far 的“本次生成”账本仍是 coefficient-boxes、sample-inverse-leaves、numeric-point-values-and-errors、complete-unpaid-scope，保持明文。它的 readback 保存原复用账本完整 descriptor 和已付完整核验来源。union 的 readback 原本就对每条本次 ledger 调 R.bound_stream，因此新 mode 的 gzip 也由同一新 decoder 全读，不借旧 M API 或只靠首个47d7替它付账。

新原始数据从产生之初只有明确压缩表示，故没有“退掉未消费行”的动作。所有包含完整候选/误差/原轨迹的账本继续同 job 临时保留，直到原必要读回和真实 quiet/cleanup 条件允许最终清理；不上传 Git、artifact 或大 raw 编码块。

## 498.8 科学范围和固定目标保持

以下原责任没有减少：

- 同一个完整 C、原 root 族、原 cut/far 物理字、旧112全候选及全部误差；
- old112 的原 input_binding 不能重标成 newM；新模式真传播、Q/Pi 槽在新2M布局真实重排；
- 原 far_sample 和实际 mu 字不能因另一盒中点而改变；
- 全部577节点、576 stages、原 steps 实际 schedule、全部物理字段；
- 全新 current-H/root/noJ/全 Jacobian/两 mean、原 FD、fullDN、final audit；
- 真实连续十参数453→独立450、完整同场几何、公共材料与固定g的责任；
- 同一原绝对预算、原资源停语义和原全部数学接受门。

存储保持命题并不证明 interval enclosure 更窄、native 更接近准确 C、完整 C 族有共同 numeric realization、g 已付或场已接受。它也不把原有限敏感度、有限线性误差或旧 accepted 状态重用为新结果。

## 498.9 原空间门和成本边界

原 BVP 启动门34,359,738,368 B保持。新源码不会把 free bytes 伪造为压缩前大小，不把 logical size 当物理 disk use，也不因为某个压缩成功就直接放行 BVP。原 launcher 仍在真实启动时观察磁盘；不够就原资源 partial。

新表示只避免“先产生95GB明文，再用剩余约11GB尝试复制压缩”的不合理生命周期。它没有证明新实验的 stored size、压缩率、CPU时间、总体 disk requirement 或原 deadline 下必能完成。每行独立 member 明确牺牲跨行压缩机会以保持完整行边界和事务次序，实际成本需由新 Actions 真记录。

所有 source 绑定、runtime setup、读前核验、linear/sampling及外层绝对钟的既有范围仍照原入口披露。不能仅因为存储变小而写“原预算一定够”或改声明预算。首采样仍完整使用后继明示的 depth2/value_bits32 work-only 合同；gzip 不替代任何候选覆盖计算。

## 498.10 218 注册尚须实际闭合的内容

R498 不猴补已刊32b0、5f14、5da13或 R496 模块全局。它提供新 helper 和准确源差异。218 必须把新实际文件名/SHA逐层登记到：

1. 首 sampler 的实际调用与 config/pipeline；
2. 三个 worker/client 及实际 original/derived source map；
3. 原453/450、same-far与union driver/owner/checkpoint 的真实来源分支；
4. 实际 sampler/union 必要 reader 和最终 postsolve/held/material loader；
5. 源生成顺序、原 absolute deadline、90KB必要输出、真实 quiet 和最终清理。

未生成的 view不能先假验，不改已刊文件，不把当前预览 SHA当作完成了218额外级联的最终 SHA。所有同g、完整几何和公共材料数学核仍复用原逻辑。该来源闭合是使实际程序可调用所需的接口责任，不是新增科学前门。

## 498.11 源文依据与本次交付边界

主要已核原件：

| 原件 | bytes | SHA-256 |
|---|---:|---|
| geometry_20261115_stored_continuous_E_cover_v3.py | 89307 | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df |
| geometry_20261115_current_C_pruefer_joint_radial_sampling.py | 69702 | 32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4 |
| root_20261116_current_C_sampling_scope_necessary_readout.py | 55606 | 47d7ec771331f417dffb783a79e02d1ae9720e9ad0a699a72c37cf3031718cb2 |
| geometry_20261116_current_C_same_far_registered_resampling.py | 50459 | 5f14be90b0e5ae36ee624ece930d46fa1205eee0efcc6e2a97decca15e7011d5 |
| geometry_20261116_current_C_incremental_M_far_union.py | 52848 | 5da13c5f94c59be9f002f906a373d5320ed64d0ac0254af1746a1e5c8ce13c46 |
| geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py | 20657 | 227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7 |
| geometry_20261115_current_C_pruefer_joint_full453_physical_dn.py | 64245 | c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d |
| geometry_20261115_current_C_pruefer_joint_native_worker.mjs | 18377 | d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a |
| geometry_20261115_current_C_pruefer_joint_tail_client.py | 23164 | 02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1 |
| geometry_20261115_current_C_general_robin_native.mjs | 24004 | fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349 |
| geometry_20261115_continuous_ten_frozen450_checkpoint.py | 36989 | 43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae |
| geometry_20261115_current_C_ten450_radial_readout.mjs | 23039 | 5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568 |
| geometry_20261115_current_C_ten450_shared_field.py | 48583 | 6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3 |

以上源只按原文件读取、查函数及调用链；本文表示等价只依赖完整原字节与解码语义，不重复原 R347/R357/R380/R442/R450/R462 的数学定理。新 source-plan 的完整字面应用和身份由文本运算形成，未运行新源码、import、AST、compile、科学计算、fixture或额外审计。没有实际 accepted450、压缩后新 free数、BVP启动或218执行结果。
