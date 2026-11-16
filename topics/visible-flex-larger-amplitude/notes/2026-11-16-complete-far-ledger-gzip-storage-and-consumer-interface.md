# R498：完整临时传播账本的 gzip writer / decoder 和218来源追加接口

日期：2026-11-16。作者：ChatGPT（AI，geometry 协作代理）。

本接口交付一个标准库 helper、四处完整 literal source-view 合同及 [R498条件结论](../results/R498-complete-far-ledger-consumers-and-streamed-lossless-storage.md)。没有新请求、实际450父、运行、压缩数据或压缩后free数。本组件不修改当前212/214/216或R496已冻结49视图，不降低原34,359,738,368 B的BVP启动空间要求。

## 1. 为什么是完整新表示

R478真实212中，depth2全部物理点/字段返回，BVP在原磁盘门停下。约95 GB的far-accepted-panels不是native数值输入，但5f14的bind_original_far仍完整核它的字节/行数/SHA，5da13 union也调用该完整来源绑定。按现有调用链，不能因为首BVP不数值解析它就先删除。

本次从第一行即写压缩member，保留全部解码后原始字节；stored与decoded身份各自真实记录。没有明文镜像、临时压缩副本、抽样替代、仅留hash、raw上传或事后伪造存在路径。原native/FD/fullDN/final、同g/材料/闭场责任与完整原输入均不变。

## 2. 正式文件与身份

| 文件 | bytes | SHA-256 |
|---|---:|---|
| computations/geometry_20261116_complete_jsonl_gzip_storage.py | 15744 | d07d1844aaf54b5aaea550a1c0d8aea63b9306f9ce44f66bd0b1e18aa3e40089 |
| computations/r498-complete-ledger-gzip-core-source-plan.json | 16786 | eb4925e33fe4cc98001dd0cfbb2fc472c5c2e00b94c9cabd10f384b6eb7851f3 |

source-plan的schema为R498-complete-temporary-gzip-core-source-view-contract-v1。其R496基线是原77274 B/e1bef5ad7727107014c9a4c494b22fd066a2866b7f5d97eb8dc1a424b0268360完整计划。它对其中真实生成的same/union两文件作追加，没有重写那49条定义。

此处各文件是源/证明元数据；它们不是科学payload。四个展开预览只供真实来源组合时形成新文件，未经运行，不把展开源码重复加入Git。plan具有完整before/after/count，能在已有源全部真实生成并绑定以后按明确次序构成新名。

## 3. 实际来源层级和必须级联的差异

完整顺序为：

1. 原冻结公开源与祖先生成计划按原入口恢复、核身份；
2. R496的49个实际新source先按其原完整合同生成并绑定；
3. 对原32b0与47d7，以及刚实际生成的R496 same/union，应用本plan四处准确差异，输出独立新basename；
4. 对218自己的worker/client/driver/CP/owner/pipeline/readers/postsolve来源闭包作真实新名和SHA级联；
5. 在真实computations/HERE下核最终全部实际字节，再调用原相应CLI。

第4步由218完整入口负责。没有用“原tuple数学相同”绕过任何实际source检查。plan的output身份是**第3步的精确预览**，不是第4步完成后的218最终身份；若第4步还需改变来源常量，则最终文件必须另记真实bytes/SHA，不能继续引用预览SHA。

### 四个实际基线

| 角色 | 基线file | bytes / SHA-256 |
|---|---|---|
| first sampler | geometry_20261115_current_C_pruefer_joint_radial_sampling.py | 69702 / 32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4 |
| same-far | geometry_20261116_current_C_zero_linear_same_far_resampling.py | 51367 / 5cb69b92c1cdf1d95b613f62d260b5dbbf9f95169d984f78999d3cf17b3d8c2a |
| union | geometry_20261116_current_C_zero_linear_incremental_M_far_union.py | 53547 / 7d1aaa9504fd8fe2722ab58a5e1cf1b53e152c921848f9030c27144fc10fcf72 |
| BASE reader | root_20261116_current_C_sampling_scope_necessary_readout.py | 55606 / 47d7ec771331f417dffb783a79e02d1ae9720e9ad0a699a72c37cf3031718cb2 |

same/union两基线已在本次按原77274计划逐条literal count恢复，完整bytes/SHA同该计划所记。这里只做文本恢复与字节哈希，没有import、执行或AST。

### 四个追加预览

| 角色 | 新预览file | bytes / SHA-256 |
|---|---|---|
| first sampler | geometry_20261116_current_C_joint_gzip_radial_sampling.py | 71361 / 21032e3c4fef44b022a7d91394ff0269dcfd3f94f8ee1a9cab9a0696b2530eb6 |
| same-far | geometry_20261116_current_C_zero_linear_same_far_gzip_resampling.py | 52092 / 2abf6d20b2e1904b68daae07dd35a86a695a13fe4e87d8edf11353d207618012 |
| union | geometry_20261116_current_C_zero_linear_incremental_M_gzip_far_union.py | 55405 / 349bc8af3b428bd54610efb53d73359000c26644b551a4331052d86b48e765b2 |
| BASE reader | root_20261116_current_C_gzip_sampling_scope_necessary_readout.py | 57097 / 47a1c4438a2f1d66733daf46f10da2cbb0f65c4912822e0e42402033d05a4149 |

原科学行/结果schema保留，以便同一次原传入行的canonical bytes完全不因日志格式变化；新storage.schema独立。实际producer的basename/source_sha256必为新文件，不能仍说运行原32b0或旧R496输出。这个来源区别贯穿新config及原所有核对者。

## 4. Helper API

### 4.1 GzipJSONLJournal

精确签名：

~~~python
GzipJSONLJournal(path, root, *, canonicalizer, compression_level=1)
journal.add(value)
descriptor = journal.finish()
~~~

构造参数是既有producer的实际临时路径与原canonical函数：

- first指定流：path为large-arrays/far-accepted-panels.jsonl.gz；
- union指定流：path为large-arrays/new-mode-accepted-panels.jsonl.gz；
- root为该实际producer的args.out；
- first canonicalizer=B.canonical；union canonicalizer=S.B.canonical；
- compression_level明确固定1，不是科学精度或接受门。

路径必须在实际RUNNER_TEMP下、在其独占root之内，无symlink，父目录已存在，文件须新建xb。新的存储组件不创建/覆盖任何原source文件，不接纳另一输出目录的假路径。

add收到原value后只调用传入的canonicalizer一次。canonical bytes必须一条完整LF结束记录；然后gzip.compress对这一行生成一个完整member。os.write实际完成全部member后flush，add才返回，原caller才可能继续其tube/commit写入。当前一行的raw和encoded是唯一新增的记录缓冲，没有全账累积。

journal.rows仍指已成功写成的原行数。内部journal.bytes/hash仍是逻辑原字节流；stored_bytes/stored_hash另计。finish幂等地返回完整descriptor；其顶层bytes/SHA改为物理stored表示，下面decoded保原逻辑身份。正常fsync/close失败抛原真实I/O错误，不造成功receipt。

### 4.2 descriptor的精确意义

| 字段 | 意义 |
|---|---|
| file | 相对实际producer root的.gz路径 |
| bytes | 实际写出的全部gzip物理字节数 |
| sha256 | 实际物理gzip完整字节SHA |
| rows | 已完整写成的原JSONL逻辑行数 |
| decoded.bytes | 完整原canonical行串总字节数 |
| decoded.sha256 | 完整原canonical行串SHA |
| decoded.rows | 同一个原逻辑行数 |
| storage.schema | R498-complete-canonical-JSONL-gzip-members-storage-v1 |
| storage.encoding | concatenated-gzip-members-one-original-JSONL-row-per-member |
| storage.compression_level | 实际明确level |
| storage.complete_encoded_stream | 当前物理表示是否完整，不等价于完整mode科学成功 |
| storage.complete_member_count | 完整成功member数 |
| storage.incomplete_member | 若实际写入失败，则原行地址/双bytes与SHA/实际写入前缀/异常；否则null |
| storage.python_version / zlib_compile_version / zlib_runtime_version | 实际格式实现来源 |
| storage.gzip_mtime | 0 |

部分mode可以留下一个“文件表示本身完整”的前缀；其科学未付仍由原pending/mode/result指出。不能看到storage.complete_encoded_stream=true就把mode或全部field标成功。

反过来，写入当前member失败时，前面的完整members和当前实际已写字节都留在原目录；当前行不会获得完整逻辑rows计数。storage不完整，不能供complete far reuse。原point_column仍保in-flight/transaction/pending所有责任。

### 4.3 完整绑定 reader

精确签名保持原bound_stream调用位置：

~~~python
chosen, identity = bound_stream(
    directory, descriptor, budget,
    selected=None, visit=None, progress=None)
~~~

budget是原caller当前对象，不是新预算。gzip路径先完整核stored bytes/SHA，再用gzip.open以二进制逐原行读取，核完整decoded bytes/SHA/rows。两个pass都在原budget.check下。没有把解压后的全文件写回盘。

selected/visit与5f14原接口完全同义。prepared/commit仍可selected=False，但它们的每字节、每行、完整双身份仍真核；far modes和anchor leaves保原选择和原科学检查。

返回值保原：

- directory及完整descriptor；
- actual_full_bytes_read/actual_full_rows_read/actual_sha256，此三项明确为解码后的完整原逻辑流；
- 另给actual_stored_bytes_read/actual_stored_sha256；
- actual_decoded_identity；
- original_stream_fully_verified；
- complete_plaintext_ledger_materialized=false。

progress新增stored与decoded的声明/实读范围及当前行地址。预算或解码中断时，complete_original_scope_returned=false，保当前阶段和原异常类型。外层仍负责原剩余ledger列表、全部unpaid和总体terminal记录。helper不吞ResourceStop，不重新分类为数学失败。

旧未压缩descriptor保持原bytes/rows/SHA。带.gz而没有本storage合同的文件不被当成已登记新流；有storage却不完整时也不伪通过。

### 4.4 原必要 reader上的补充

~~~python
binding = verify_decoded_readback(descriptor, actual_line_stream_result)
~~~

该函数利用原47d7已实际计算的rows、decoded_stream_bytes、decoded_stream_sha256核对应decoded期望，返回双身份绑定事实。它不重算科学量，不另扫一个新fixture。

## 5. 四处差异的完整范围

### 5.1 first

保持原load_runtime、F.bind_inputs、InverseSampler、radial_grid、far行形成、全字段/数组、完整pending和预算。新增r498_storage_helper实际file/SHA加载。只有for name创建Journal时，far-accepted-panels选新writer，其余九账本原B.Journal逐字不动。

report额外记录actual_complete_ledger_storage，包括实际helper来源、compressed_logical_streams、level1以及stored/decoded分责。必要reader真实选择该小字段。

原scientific schemas保留，但source_sha256取新实际文件。view/caller必须实际登记新source，不得让PINS仍指32b0而仅把输出result标签换掉。

### 5.2 same-far

R496生成的same-far文件只增加helper、登记新的joint sampler来源，并把整个原bound_stream的表示读取替换为helper调用。原REUSED_LEDGER_NAMES不减少。原all112 mode/candidate/row/幅度/far点/mu/矩阵字/完整span/末后缀条件不改。

它的sample阶段仍用原clock与原full-C/deep绑定，真正产生新grid。其本次四条generated ledger仍明文；没有额外gzip的新生成账需要另一个读取分支。

原readback额外选择actual_complete_ledger_storage；既有same_original_far_family_reuse和original_reused_ledger_identities继续完整保原descriptor，包含新storage/decoded字段。

### 5.3 union

R496生成的union明确调用上述新same-far名字/实际SHA。先完整绑定旧112真实输入，再加载原全M math sampler；不把旧112 input_binding改成新M。只将new-mode-accepted-panels改写gzip，canonicalizer仍真实S.B.canonical。

原new-mode-matrix形成、Pi槽迁移、fresh node_mu/field_grid、全部新deep和有限头传播不改。原result额外保actual_complete_ledger_storage。

**union readback本来就逐ledger调用R.bound_stream。** 因而新new-mode-accepted-panels由同一新decoder完整核stored/decoded，modes/unpaid原选择仍在该原调用。不能用旧M API/只选择union摘要省略此调用。

### 5.4 BASE必要读取

使用新basename，真实登记新first sampler/helper；原SOURCE_PINS祖先责任由218完整source closure保留。原mode、unit、全候选/coverage、全部point未决8字段、native trials、FD/error、large-array身份及90KB/70合同不动。

原line_stream已支持.gz。返回前新增verify_decoded_readback，不把物理压缩长度与原decoded长度混同。failure、scope未知或超90KB仍不能产生完整清理marker。

## 6. 外层读回不能走错分支

| 实际阶段 | 完整原流读取入口 | 保留到外层的关键对象 |
|---|---|---|
| first sampler | 新BASE.sampler_readback→line_stream→verify_decoded_readback | 原complete_necessary_unpaid、全部原stream双身份、实际field/arrays、true/false状态 |
| R456 same-far | 新same.bind_original_far→新bound_stream；随后其原readback | same_original_far_family_reuse、original_reused_ledger_identities、完整新unpaid |
| R462 union | 新union.bind_old→新same；新union.readback→新same.bound_stream | 原112完整绑定、新M完整mode/unpaid、complete_generated_ledger_identities |
| R464外围M必要 | 真正调用新union的原readback；保存actual_new_sampling完整结构 | actual_original_R462_readback_exit、original_result_identity、original_necessary_identity、complete_original_necessary_scope等，不能误按旧sample.original扁平挑字段 |

后两阶段并不依赖首个BASE替它们核gzip。它们拥有各自真实完整调用。若218生成的某个原M/native辅助reader还有独立文件扫描，则必须按真实调用路径显式适配或确认只读原数值数组；不能仅把它的source label改名就当来源闭合。

## 7. 实际CLI、目录与资源

本helper没有科学CLI，没有独立新run，也不创建后台任务。四处视图沿原各CLI：first使用原sampler完整参数，same和union保sample/configure/readback，BASE保原metadata argv。没有增加一个科学门或独立审核步骤。

level1是公开source中明确的存储工作选择。首入口depth2、32bit work-only目标、全部field plan/原13,850等只作为R478实际事实，未来数量必须由新的实际plan决定。不得把R478旧words或旧C盒当作218的新结果。

原namespace 18900秒科学计划、末2700秒必要读取、每个原OwnedChild、TERM→KILL/reap/quiet、同actual deadline和所有remaining clip沿218真实组合。编码/解码耗时实际落在各原调用中；不偷偷重开钟。存储helper没有seconds参数。

每个原resource free观察仍是真实disk_usage；BVP启动仍34359738368，原free-stop/2GiB等按对应入口既有参数，不能因逻辑文件大或压缩已启就无条件放行。

caller仍须完成：

- 源的完整实际生成与身份绑定；
- 原同job field/geometry/accepted父来源；
- 所有实际必要readback与其原90KB限制；
- 进程确已quiet后，按原总workflow的真实marker与scope判断最终清理。

本helper从不删原文件、缓存或生成目录，也不上传raw。单份必要仍可能因过多失败/未决超限70，本次不承诺必低于90KB。

## 8. 218级联的最低清单

源文件修改使用新名，不覆写被冻结文件。在真实输出进入BVP之前至少要贯通：

1. sampler runner实际文件名/SHA及结果source_sha；
2. first/same/union三个worker与client的sampler源常量、真实config/source_sha256和原runtime来源；
3. first actual202 driver/launcher/pipeline/candidate来源；
4. same-far、union driver/CP/owner的原来源校验及源生成先后；
5. 三层必要reader真BASE/producer、新schema若外层另定义则如实匹配；
6. 同accepted CP的后闭radial/shared/material来源finder与完整source closure；
7. 原Quiet、全部末门、90KB和真实cleanup。

first科学row schema不变不等于source相同；新configuration必须包含实际新source身份。R496 zero-linear运算不因为压缩被撤销或扩大。完整科学源可以仍从原request205/216祖先恢复，但新实际调用者必须使用218最后真实输出。

本plan刻意没有把四预览当作最终218闭包。未来实际C/采样/launcher/reader/result必须各自实际返回；没有任何accepted450或新存储成功的预填字段。

## 9. 原论证和未付范围

R498证明只说明对原同一次logical流，完整gzip成员表示和完整解码核可以保所有原字节/行序/span；并源码确认旧流存在真实后继消费者，不能直接删。原全部ODE/Prüfer/单位行/误差/当前C族证明直接复用，不增加新的数学接受条件。

没有测压缩比、速度、最终盘占用或BVP能否启动。gzip可能增加CPU成本；member独立方式不利用跨行字典，不能宣称最优。原全部C/root/H/J/FD/fullDN/闭场metric/reach/held/全t/固定g的条件与实际未返均保。

本次只读取小源码/已回传必要事实，写源和完整差异，计算文本字节身份。没有本地源码执行、AST、compile、fixture、科学算术、旧大raw回取、删除或Git ref改变；实际科学仍仅Actions。
