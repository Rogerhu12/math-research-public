# NoJ-primal live：已关闭迭代的后台 artifact 外移最小接线

作者：ChatGPT / geometry  
日期：2026-11-15 UTC  
分类：源码、运行资源及字节保全接口；未实施上传器，未运行科学计算。

## 1. 结论与范围

可以在同一 live worker 与同一 fullDN 进程持续运行时，由独立的字节保全组件上传已经关闭的 correction 目录。当前五个科学源无需改变：新组件观察原成功尾记录，原 worker 中的 states、cache、predictor 和下一次实际 H 请求继续留在原进程。上传本身不能替代成功 73 锚、不能产生 native 接受，也不能把跨进程旧响应冒成 live cache。

当前仓库没有直接完成这条工作的上传器。现有 `strong_prefix_cache_archive.py` 与 `strong_exact_stage_cache_archive.py` 提供原成员 SHA、确定性 tar/gzip、原路径还原等可复用模式，但分别锁旧 magic/旧 cache schema、较小 Git 分片；前者默认还会省略小 RHS call。它们没有 Actions artifact 上传或成功上传后的空间回收。因此不能只换输入目录套用。

最小新增范围是：一个 Node JavaScript action supervisor、一份固定依赖锁、一个逐批恢复/核字节入口，以及独立 catalog。无需新增数学 solver、重算 J、复制整个历史或改原 noJ/32 轮/十试探/FD/final audit。

## 2. 原实现中可安全外移的位置

精确源码边界已由 [无损归档合同](2026-11-15-noJ-primal-live-lossless-archive-contract.md) 给出。当前 hook 的 `currentCorrection` 完整次序为：

1. 当前 freshwithJ snapshot；
2. 同步 QR 子进程及其 model/exact readback；
3. 子进程退出，stdout/stderr 文件关闭；
4. `checkedCurrentDirection` 完整读取当前结果、manifest、577 行 delta/checkpoint，并恢复独立内存数组；
5. state/target/σ/原几何不变核；
6. 写 `returned-correction.json`；
7. 将 `linear_direction_returned=true` 的完整记录追加至本 call 的 `current-corrections.jsonl`；
8. 返回内存 delta，原十个 noJ 试探继续。

后台观察者只能接收第 7 步完整换行后的记录，交叉核对应 returned 文件、成功 `qr-exit.json`、snapshot/result/manifest 的原 SHA；不能只看目录存在、文件暂时不变或 QR 的 solve 阶段结束。QR 的后续 model_readback 仍需读取全部因子/J。

`finishRequestContext`、`finishAll` 及后续 call 只读原 ctx 元数据，不重新打开已返回 correction 的 raw J/因子。失败 iteration 则必须等相关子进程/worker 完全退出后才能整体保全；不套成功闭合标志。

可仅移走已核保全的 `iteration-*/snapshot/large-arrays/` 与 `iteration-*/qr/large-arrays/` 数据，其他原 JSON、manifest、日志和 descriptor 保持原名字、原字节。后台批次应同时收齐该 iteration 全部文件作为远端原件；不能遗漏精确行账、常数、失败证据或 manifest 以外的元数据。

## 3. 已读官方实现与可直接复用的能力

本仓现用 `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` 即 v4.6.2。该提交的 license 元数据明确实际 artifact 库为 2.3.2，不只依据 package.json 的 caret 范围。亲读官方 toolkit commit `c40bccc9c31c29df15c93abbea5b18bb474a4add` 中 package 2.3.2 的六个小源：

- `uploadArtifact(name, files, rootDirectory, options)` 创建 artifact、流式上传 ZIP、Finalize 后返回 id/size/digest。
- `createZipUploadStream` 直接将 archiver 输出接入流，不先生成一份完整本地 ZIP。
- 上传字节流同时进入 SHA256 哈希器；Finalize 请求携带该 digest。
- 下载 API 可使用同 job runtime 服务取得 signed URL，流式解压到指定新目录。
- `downloadArtifact` 的 `expectedHash` 比较只返回 `digestMismatch` 布尔。调用成功并不自动证明 digest 相等；新组件必须显式要求 false，并核全部原成员长度/SHA。
- v4 artifact 上传完成即可供 UI/API 访问，不必等 job 终态；同名 artifact 不可追加，单 job 最多 500 个 artifact。不能用一轮一件覆盖最坏 608 轮。

来源：

- [固定 upload action README](https://github.com/actions/upload-artifact/blob/ea165f8d65b6e75b540449e92b4886f43607fa02/README.md)
- [固定 action 实际 artifact 版本](https://github.com/actions/upload-artifact/blob/ea165f8d65b6e75b540449e92b4886f43607fa02/.licenses/npm/@actions/artifact.dep.yml)
- [2.3.2 上传及 Finalize](https://github.com/actions/toolkit/blob/c40bccc9c31c29df15c93abbea5b18bb474a4add/packages/artifact/src/internal/upload/upload-artifact.ts)
- [2.3.2 ZIP 流](https://github.com/actions/toolkit/blob/c40bccc9c31c29df15c93abbea5b18bb474a4add/packages/artifact/src/internal/upload/zip.ts)
- [2.3.2 上传流与 digest](https://github.com/actions/toolkit/blob/c40bccc9c31c29df15c93abbea5b18bb474a4add/packages/artifact/src/internal/upload/blob-upload.ts)
- [2.3.2 下载与 digestMismatch](https://github.com/actions/toolkit/blob/c40bccc9c31c29df15c93abbea5b18bb474a4add/packages/artifact/src/internal/download/download-artifact.ts)

这些是明确版本的可行性依据，不是已打包的新 uploader。实际实现须再固定其完整 npm lock/integrity 或预先打包源码；不能临时安装浮动最新版冒成上述版本。

## 4. 最薄运行接线

采用 JavaScript action supervisor 包住原规则同步命令：它以原 argv 和 shell=false 启动原 rules-runner 及其 live fullDN driver，同时处理仅含已关闭 iteration 的字节队列，依次上传、复核、登记。native worker 和 fullDN 没有拆分，也没有新 selector。

普通 workflow `run:` 步骤不应假定能取得 artifact runtime 凭据。官方 runner 的 NodeScriptActionHandler 明确注入 `ACTIONS_RUNTIME_TOKEN`、`ACTIONS_RESULTS_URL`；已读 ScriptHandler 没有相同注入。因而新小组件宜由 `runs.using: node20` 的 JavaScript action 启动，与现用 v4 uploader 运行接口一致；科学子命令仍使用已固定 Node24.22.1/Python/BLAS 环境。

新增 artifact runtime token 和 URL 仅保留在 supervisor/uploader 环境，不向原规则同步/native 子进程继承，不落日志或 catalog。原规则同步器目前自身需要 GITHUB_TOKEN/GH_TOKEN；不能为了新 uploader 把它现有必需凭据一并去掉。新增 token 隔离与原规则同步器原有环境范围应分别写明。

[官方 runner 的 Node action 注入源码](https://github.com/actions/runner/blob/6b19888d3b095800904158fb926c455820010b68/src/Runner.Worker/Handlers/NodeScriptActionHandler.cs)。

Supervisor 不修改科学 cwd、原命令参数、科学源、请求或 stdout 协议；上传日志独立文件。它等待原进程结束并排空保全队列，分别记录 science exit 与 storage exit，不能把远端网络错误写成数学 guard，也不能把成功保全写成 native 成功。

## 5. 两轮一批的完整字节合同

按本 run/attempt、递增 batch 序号和成员清单 SHA 使用唯一 artifact 名，overwrite=false。通常每两轮闭合 correction 一批；末尾不足两轮仍完整保全。不按成功 α 或数值大小筛文件，不重编码 JSON/f64，不压缩三角非零部分来取代完整原数组。

建议每批操作：

1. 对两个闭合目录做安全路径、普通文件、无重复/无 symlink、原 file set/bytes/SHA 清单，记录原 call/iteration 与 returned/JSONL receipts。批次清单本身也作为上传成员。
2. 向 SDK 提交全部明确文件路径，以同一原输出根作 rootDirectory，保原相对目录。SDK 直接 ZIP 流上传，无整批本地 ZIP 副本。
3. Finalize 后记录 artifact id/name/size/digest。随后同 job 下载该实际 id 至新的一批验证目录，明确传 `expectedHash='sha256:'+digest`。
4. 显式核 `digestMismatch===false`、全部成员路径集合与长度/SHA、无额外路径/重复/逃逸，和上传前原清单一致。此验证只读字节，不运行任何数值程序。
5. 先原子写/刷新 catalog 和该批 verified receipt，再撤下对应原 large-arrays payload 和验证副本；原 scientific manifest/小记录仍留本地。未验证或失败时不撤原件。
6. final 普通 artifact 保上传 catalog、全部小记录及未外移 partial，独立 publisher 只发 bounded 小文本。每个远端批次包含自己的原清单，进程中断时仍可按 run/attempt/batch 名找到完整原件。

这是本任务建议的最小实现；尚未创建或上传任何批次。SDK 自带上传传输重试可复用，但不能无限新建不同 artifact 名重试而越过 500 件限制。最多 19×32 个 correction 若全部成功闭合，两轮一批至多 304 件；失败尾、最终摘要和任何新建重试都必须单列 artifact 数量账。

旧完整 byte-reader 不能直接读取已撤下的 raw 路径。新增恢复入口必须从 catalog 按 artifact id/digest 下载，核成员原 SHA 后恢复到独立目录的原相对路径，拒绝不同现存内容覆盖。可以逐 iteration 恢复、运行既有纯 byte-reader 后释放验证副本；不得把 ZIP/gzip 路径替换原 descriptor，或声称原 reader 已支持 catalog。

## 6. 容量能保证到哪里

[已冻结资源账](2026-11-15-noJ-primal-live-resource-flow-and-retention.md) 给出每轮固定 704387088 B，包括两份边界 rho；32 轮固定 22540386816 B，19 call 最坏固定 428267349504 B。所有数字排除可变 exact ledger/JSON/log/prefix work，不能当完整上界。

两轮原固定 payload 为 1408774176 B。上述 SDK 下载复核保留一批验证副本，单批原件与验证副本合计固定 2817548352 B；若同时再有一个完整活动 correction，固定合计 3521935440 B。**这不是总峰值上界**：尚有上传积压、可变账、当前失败/未关闭目录、原 inputs、prefix work、SDK 内存和其他进程。收益是历史已验证批次不再无限留在活动盘，而非假设某个压缩比例。

后台上传速度不足、存储 quota 不足或网络不可用时，队列仍会增长。只有实际持久存储成功回执及复核才能释放；因此单纯加后台上传不能无条件证明 32 GiB 足够完整 fullDN。若余量耗尽，应保留现场并明确工程失败，不能删未验证原件、降低 32/10/outer/FD 门，或把中断改写成科学拒绝。这里不建议 SIGSTOP 暂停 native：其壁钟期限、规则同步和子进程生命周期需另算，不能默认为无影响。

本方案只消除“必须等整个 fullDN 完成才上传”的现有存储阻点。真实 73 成功锚尚须由原结果给出，全部科学接受仍由原完整 solve/J/fresh audit 判断。
