# NoJ-primal live：原始产物生命周期与无损归档合同

类型：源码与存储接口说明，未实施归档器、未运行新科学计算。  
作者：ChatGPT / exact_refinement。  
日期：2026-11-15 UTC。

## 1. 可直接采取的结论

当前 live 五源完整保留每轮 snapshot、QR 因子、全部纯常数、方向、输入副本和精确整数行账，没有压缩 raw 或按轮迁移的逻辑。现有 gzip 用于 JSON/精确行账；`large-arrays/*.f64le` 仍是完整原二进制。最终 upload artifact 即使压缩传输，也不会在此前的 live 求解期间释放这些文件。

独立无损归档可以在**该轮 QR 子进程退出、方向已恢复到 JS 内存、returned-correction 与完整 JSONL 记录均已落盘之后**处理该轮目录。它不得提前移动当前 QR 仍读的 snapshot/J/因子，也不得让原 descriptor 悄悄指向压缩内容。归档后的原始字节必须能按原路径完整恢复，所有原 SHA、signed zero、常数和整数账保持。

按完整源清单，每轮已知固定 binary 为 **704387088 B**，含先前容量元数据遗漏的 `formed-cut-rho` 和 `formed-far-rho` 各 896 B。32 轮为 22540386816 B，默认多请求结构的 19 次调用合计固定项为 428267349504 B；这些仅是整数文件尺寸账，尚不含可变 JSON、exact ledger、日志、前缀 work 和归档临时空间。geometry 负责完整容量/RAM 账及未发布 live 的容量元数据修正；原 73 已发布源不改。

**没有实际压缩率时，不能保证本地压缩使完整多请求运行适合 32 GiB。** 完整预算的直接方案是提供足够持久磁盘。较小本地盘若采用流式外移，还须有实际可用的持久存储、逐包成功回执及独立还原核对；当前源码尚未实现这条路径。

## 2. 最后读取边界

核对对象为 `geometry_20261114_noj_primal_live_tail_client_hook.mjs` 的 `currentCorrection`、`checkedCurrentDirection`、`finishRequestContext`、`finishAll`；我们的 live QR CLI；冻结 R273 类 `NativeDampedChainQR`；以及 live Python client 的 `solve/close`。

| 对象 | 当前求解最后读取位置 | 后续保留用途 |
|---|---|---|
| 本轮完整 snapshot/J | QR `factorize`、`exact_current_readback`、`model_readback`；都在同步子进程内 | 来源与完整字节审计 |
| 全 577 因子及纯常数 | `solve`、`model_readback`；随后进程退出 | 能量账、因子与常数完整性 |
| 完整 delta/raw/checkpoint/binding/manifest | JS `checkedCurrentDirection`，恢复为独立完整 `Float64Array` 行 | 原十试探使用内存 delta；文件供回溯 |
| 精确行账与最坏见证 | 子进程写完并退出；bridge 不以其数值门控 | 原矩阵精确缺陷诊断 |
| 迭代记录、call summary | 元数据读取/写出；不重读旧 J/因子 | 请求/迭代索引与来源 |
| 当前 worker states、cache、predictor | 原 worker 内存和后续原协议 | 后续实际 native 请求，不能用归档替换 |

`currentCorrection` 的成功次序是：snapshot → `spawnSync` → 子进程状态检查 → `checkedCurrentDirection` → 当前 state/target/scales 与原几何不变核 → `returned-correction.json` → 将完整记录追加到 `current-corrections.jsonl` → 返回内存 delta。后两步之前只观察到文件名存在，不足以宣称迭代目录已封闭。

`ctx.records` 和 `requestRecords` 保存 receipts/标量/元数据，不持有旧 J 或因子 payload。`finishRequestContext` 与 `finishAll` 用这些记录生成摘要；Python 外层读原响应和记录 cache 命中，不重新打开旧迭代的 J/因子。因此成功迭代的**数据 payload**存在可封存边界，而活跃 call 的摘要/trace 仍可能继续增长。

失败迭代不能套成功标志。`bridge-failure.json`、QR 的 partial manifest 或 summary 可尚在写入；只有对应子进程与 worker 的写入生命周期确实结束，才可扫描并封存失败目录。不能仅凭一段时间未变化、`native_accepted=false` 或缺失 success 标志删改文件。

## 3. 最小独立归档格式

未来若采用归档，应新建独立的纯字节组件，保持冻结数学源及所有原 artifact 逻辑身份。建议单包单位是一个已封闭的 `call-NNNN/iteration-NNN/`，不是整个多调用运行：这样单包形成期间只需一轮 raw 与一轮压缩包并存；不先复制整棵 raw 目录。

新 catalog 可使用独立 schema `complete-native-live-byte-archive-v1`。每项至少保：真实 run/source、call/iteration、原 snapshot/result/manifest SHA、原相对路径、实际文件 bytes/SHA、归档成员路径、归档文件 bytes/SHA、编码、封闭依据、验证完成标志。该 schema 是设计建议，当前没有实际 archive 或成功回执。

完整封存过程应为：

1. 核定成功轮两个尾部记录完整且指向同一结果；或确认失败轮所有相关写入进程终止。限定到该独立输出目录，拒绝目录逃逸、符号链接、重复成员和已有目标覆盖。
2. 枚举全部实际文件，保 manifest 中每份 raw/J/factor/constant/delta、完整 JSON/gzip、精确 ledger、日志及不在 manifest 中的元数据。不能仅收集成功数组而遗漏 partial 或错误文件。
3. 分块读取原文件，写新 `.partial` 归档；同时记录原 bytes/SHA。直接保存原文件字节，不解码 f64、不重编码 JSON、不重算整数、不截掉三角零位、padding 或 signed zero。
4. 关闭并刷新归档后，再**流式解包到哈希器**核每个成员的原长度/SHA、路径集合和压缩 CRC。核对期间无需生成第二棵展开目录，也不做科学计算。
5. 校验完成才发布最终归档和 catalog。原 scientific manifest/descriptor 完全保留；catalog 是额外的存储定位层。原字节审计器使用前须原路径还原，或由独立 archive-aware reader 按成员流式验原 SHA，不能让旧 reader 把 gzip 当 raw。

上述动作若只添加归档而保留 raw，不会减少磁盘。若将已校验 raw 从活动盘撤下，必须先确保完整原字节已持久保全，并以新 catalog 明记该副本的存储变化；这属于新存储实现，当前未执行任何删除、迁移或原目录改写。不得把“已开始上传”或仅有 object 名称冒成远端持久保全成功。

## 4. 资源与错误范围

只做本地压缩时，每包需要 raw 加压缩输出的峰值空间，已封存历史包仍不断累积。不能预估其含零量来声称确定压缩比例；应只报告 Actions 实际文件大小。跨请求压缩如与 QR 并发，会竞争 CPU/I/O；应明确额外存储工作时间，不暗中削减原 32/10 次循环、outer budget、eta、tol 或最终 fresh audit。

若未来远端流式外移，上传步骤仅处理已封闭字节包，并单独记录失败。上传失败时保留本地原件与 partial/错误记录；不能丢原数据后继续声称完整归档。空间不足也须诚实区分工程中止与原科学拒绝，保当时产物，不改数学接受条件。

新归档器不需要导入 NumPy、SciPy、adapter、QR 或科学模块，不需要重新求 J/RHS/范数。压缩/哈希/安全路径与回执可由标准库和实际存储接口完成。原 kernel、所有节点罚项和常数、完整 exact 读回、十次 nonlinear 试探与最后 J/audit 都保持原职责。

本说明未声明任何 73 成功锚，未调度新 run，也未实施归档策略。当前 live 启动条件仍是未来真实成功 73 原件；本说明只给出可以无损保全完整产物的生命周期接口。
