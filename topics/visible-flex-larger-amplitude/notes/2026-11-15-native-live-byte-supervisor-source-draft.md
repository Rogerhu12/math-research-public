# noJ-primal live 字节 supervisor / restore 最小源码草稿

作者：ChatGPT / geometry  
日期：2026-11-15 UTC  
状态：独立源码草稿；仅 Node 语法检查，未安装依赖、未启动子命令、未上传或下载 artifact、未执行科学计算。

## 1. 当前交付与范围

三份 `.mjs` 总计约 28 KB，正式源码均位于本课题 `computations/` 目录：

- `native_closed_iteration_bytes.mjs`：从已发布 live hook 的完整换行记录发现关闭的 correction，逐文件读取原字节、形成批次清单、核下载成员、回收已保全大数组、按原路径还原。
- `native_live_artifact_supervisor.mjs`：原 argv、cwd、shell=false 启动已有规则同步器及其原科学子链；异步观察已关闭目录，通常两轮一批。科学进程持续运行，后台保全不另开 live worker。
- `native_restore_artifact_batches.mjs`：从显式 SHA 绑定的 catalog 下载指定实际 artifact，核 digest 和全部成员，再还原到独立新目录。它不调用数值 reader 或 solver。

这不是新的求解入口。所需真实接受尾锚与完整 fullDN 命令由原 live client / driver 自身验证。实际73已线搜索失败，不是接受锚；详见[原结果](2026-11-15-actual73-noJ-primal-native-line-search-failure.md)。草稿不提供成功锚占位文件，不生成未来 request，不变更原 32 轮、十个 alpha、FD、同 H 缓存或最终 fresh audit。

已发表的存储研究依据见 [后台 artifact 接线](2026-11-15-noJ-primal-live-background-artifact-wiring.md) 和 [原闭合边界合同](2026-11-15-noJ-primal-live-lossless-archive-contract.md)。本草稿不修改那两份已冻结文本。

## 2. 严格限定的封存边界

当前只认识实际发布的 client `7aa2aba1…` / hook `0e802785…`，完整值在源码 `CLOSURE_SOURCE_PINS`。从 `live-client-spec.json.gz` 核实际 source，再读取 `call-0001/current-corrections.jsonl` 等文件。尚未形成完整换行的最后一行不读取。

一轮仅在以下原事实同时存在时入队：原 `snapshot_completed` 和 `linear_direction_returned` 均真；独立 `returned-correction.json` 与该行 direction 完全相同；独立 `qr-exit.json` 与该行 exit 完全相同，status=0、signal=null、error=null。随后核本轮 call / iteration / sequence、snapshot/result/manifest/context/child binding/checkpoint/full delta 的原 descriptor 字节。

这确认的是已有 source 的关闭协议，不能推导原十试探已经接受。十试探在返回内存 delta 后照原逻辑继续。失败或未关闭目录不会被本后台组件回收；仍由原进程退出后的普通 `always()` artifact 保存。

每批保存两个关闭目录的全部普通文件，而不只 manifest 所列的数组；同时保原 live spec、intent、verified intent 和对应 call 的原 request。原追加日志的那一条完整 UTF-8 原行以 base64 存于新批次清单，不给仍在增长的整本 JSONL 伪造“最终 SHA”。

## 3. 上传、复核、回收的顺序

临时 staging 在独立新存储目录中，用硬链接保存 `payload/<原相对路径>`。它不复制整批大数组，也不对共享 inode chmod。跨设备硬链接失败会如实成为存储错误，不暗中复制数 GB。目录可同处 runner 的同一文件系统，但不能位于 live output 内，因原 client 要求新空目录。

每批另写 `batch-manifest.json`，保存全部文件名、长度、SHA256、实际完整关闭行及 source/run/attempt 身份。上传文件集合显式列出；使用 SDK 流式 ZIP，唯一 artifact 名含 run/attempt/batch/manifest SHA 前缀，不 overwrite 同名 artifact。

Finalize 返回真实 id/digest 后，先落 catalog，再下载该 id 到新的验证目录，传入 `expectedHash="sha256:"+digest`。必须显式检查 SDK 返回 `digestMismatch===false`，并按清单核原全部文件集合、字节数和 SHA；仅下载 API 无异常不算完成。

只有完整 verified receipt 与 catalog 都已写入并 fsync，且 `evict_verified_payloads` 显式为 true，才逐件重新核源 SHA 并 unlink 原 `call-*/iteration-*/snapshot/large-arrays/` 和 `qr/large-arrays/` 文件。每个已 unlink 文件写独立回收日志。原科学 JSON、manifest、日志、描述器不修改。远端完整原件保留；最后撤下 staging 硬链接才真正释放原数据 inode。

若发生上传、下载、hash、空间或包依赖错误，catalog 单独记录 `storage_error`，不杀死、暂停、重启或调参科学进程，不把错误写成 native guard。所有未验证原件保留。原子命令的 exit code / signal 原样单列；科学正常而存储失败时，supervisor 的工程退出码为 86，不能冒原科学失败或成功。

## 4. 未来接线参数；未生成实际部署请求

Supervisor CLI 为 `node native_live_artifact_supervisor.mjs --spec <真实新spec.json>`。spec 字段：

| 字段 | 语义 |
|---|---|
| `schema` | `native-live-byte-artifact-supervisor-spec-v1` |
| `command` / `cwd` | 既有 rules-runner → live fullDN 的完整真实 argv / cwd；无 shell 拼接 |
| `live_output` | 原 driver 实际 `full-dn/true-tail-noj-primal-current576-bridge` 目录 |
| `storage_directory` | 与 live output 不重合的新目录；原 client 启动前不创建 live output |
| `source_pins` | 源码列出的实际 client / hook 完整 SHA |
| `iterations_per_batch` | 2；末尾可完整保存单轮 |
| `max_batches` | 明确工程上限 304–499，需给本 job 最终 artifact 留余量；不是 solver 迭代限制 |
| `artifact_prefix` | 独立安全名称前缀 |
| `poll_milliseconds` | 至少 1000 的观察间隔，不变科学超时 |
| `compression_level` / `retention_days` | 明确上传参数，不假定压缩率 |
| `evict_verified_payloads` | 明确布尔；false 时只保全不回收 |
| `sdk.dependency_root` / `sdk.lock` | 真实构建依赖根及完整 lock 的 file/bytes/SHA receipt |

不能把这些字段中的占位说明直接提交成一次科学 request。本草稿没有 action.yml 或 workflow，也没有虚构完整 npm lock。实际部署应由一个 JavaScript action 执行，以获得 runner 注入的 artifact runtime 凭据；既有科学 Python / Node24 环境仍沿原 workflow。

已核官方 SDK 为 `@actions/artifact` 2.3.2，默认导出和 `DefaultArtifactClient` 均存在。未来需要真实生成完整 lock（含 transitive integrity）、固定并 `npm ci` 或构建固定 bundle。本草稿运行时核该实际 lock receipt、安装包名/版本和 lock 中的 artifact integrity；这不是对任意既有 `node_modules` 内容作完整审计，不能代替受控构建。

`ACTIONS_RUNTIME_TOKEN` / runtime URL / results URL 等新存储凭据不传给原子链，也不写进 spec/catalog/log。既有 rules-runner 原来依赖的 GITHUB_TOKEN/GH_TOKEN 不删，避免改坏原规则同步。错误报告移除 token 和传输 URL。

## 5. 还原合同及明确未覆盖部分

Restore CLI 同样 `node native_restore_artifact_batches.mjs --spec <真实restore-spec.json>`，schema 为 `native-live-byte-artifact-restore-spec-v1`。需给实际 catalog 文件及 SHA、两个互不嵌套的新 `output_directory` / `work_directory`、同一完整 SDK lock receipt。跨 run 可显式给 `find_by.repository_owner` / `repository_name`，下载 token 只从环境取，不序列化。

该入口要求所列批次已远端验证，不会把 incomplete batch 静默跳过。普通 final artifact 中的 active/failed/partial 原件仍需另取；本组件不声称一个不完整 catalog 能独自恢复整个 fullDN。成员还原不得覆盖不同现存内容；相同文件只做字节核并保留。所有原 manifest 路径保持不变，完成后才可供旧字节 reader 读取。

上限仍是物理资源问题：固定每 correction 704387088 B，608 个潜在 correction 共 428267349504 B，另有可变 ledger/JSON/prefix/失败尾。两轮批次与一次验证副本可减少历史驻留，不能保证网络、quota 或磁盘始终足够。上传队列落后时原数据继续增长；没有未经授权的 SIGSTOP 背压，也不通过删未验证数据、降低门槛或改预算解决。

当前只做源码和语法检查。真正 SDK 构建、同 job 上传/下载回执、取消与 runner 清理行为、完整 catalog 还原验证都尚无实际运行证据。它们属于存储集成测试，不是新的数学通过门。第73轮原结果及完整字节已发表；其失败不冒接受锚。独立SDK锁构建不需要成功锚，也不部署本supervisor。

## 主控发表状态

三个源码保持原SHA不变；[原静态回执](2026-11-15-native-live-storage-source-static.json)记录准备时的原接口c95148e0，其[原稿](2026-11-15-native-live-byte-supervisor-original-preparation.md)逐字保留。本版只纠正发布路径和已完成73状态，并补当前链接。[独立源码审阅](2026-11-15-noJ-primal-live-storage-source-review.md)与[真实锁构建接口](2026-11-15-native-live-sdk-lock-build-interface.md)分别给出范围；后者只触发公开Actions生成真实锁和禁脚本安装，不启动科学或执行SDK存储API。[主控发布回执](2026-11-15-native-live-storage-root-integration.json)记载所有实际文件字节。
