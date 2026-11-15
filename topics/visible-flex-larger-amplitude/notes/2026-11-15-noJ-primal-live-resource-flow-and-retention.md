# noJ-primal live fullDN：资源流与完整文件生命周期

作者：/root/geometry，GPT-6 Astra Pro（AI-assisted）。日期：2026-11-15 UTC。
状态：源级与固定文件布局核查完成；未运行 RHS、J、ODE、QR、试步或新的科学计算。第 73 轮的实际迭代数和成败仍须读取它的真实回执。

## 1. 本次明确结论

每个完成的 current576 correction，现有源固定写出的 binary 为 **704,387,088 B**，至少 **1,750 个 binary 文件**。旧未发布 live 草稿中的 704,385,296 B 少计了 `formed-cut-rho` 与 `formed-far-rho` 两个固定 112 项数组，共 1,792 B。此处只纠正容量元数据；原数学、容差、32 轮循环、十试步、FD、最终 sensitivity/J/audit 均不改变。

32 轮单协议请求的固定量为 **22,540,386,816 B / 56,000 个 binary 文件**。默认八 outer 的 driver 按 `1 bootstrap + 1 当前 warm + 2×8 outer + 1 final audit` 保守计最多 19 个协议请求，故固定项最坏为 **428,267,349,504 B / 1,064,000 个 binary 文件**。上述数量均不包含可变 exact 行账、JSON、日志、失败阵、prefix 工作文件和上传暂存。不能把单请求的 32 GiB 检查解释为整个 fullDN 的容量保证，也不能把这些固定项解释为总磁盘上界。

## 2. 固定文件账

以下仅代入源码已声明的 M=112、K=224、D=576 和每项 binary64 的 8 字节；没有读取数组数值计算任何科学量。

| 固定类别 | 文件与原形状 | bytes | binary 文件数 |
|---|---|---:|---:|
| 本轮真实 snapshot | 10 个完整数组，J 为 576×224×224；按最多 4 个首维行分块 | 234,318,472 | 583 |
| QR 对原输入的副本 | 同 snapshot 的 9 个非 J 数组，逐原 bytes 复制 | 3,107,464 | 9 |
| R273 完整链因子和纯常数 | 576 个 [R,S,affine]、末节点 [R,affine]；577 份纯常数 | 464,891,392 | 1,154 |
| 方向 | 完整 scaled z 与恢复后的 delta，各 577×224 | 2,067,968 | 2 |
| 形成后的两端 rho | cut112 与 far112 | 1,792 | 2 |
| 合计 | 不删节点、模式、边界或常数 | **704,387,088** | **1,750** |

因子与纯常数的源码公式为 `8*(D*K*(2*K+1)+K*(K+1)+(D+1)*K)`。两端 rho 来自冻结 `NativeDampedChainQR.boundary_rho` 的独立 `output.save`；不包含在该因子公式内。`model_readback` 对 formed V/rho 再读/形成作诊断，仅保哈希和标量，不额外保存一份完整 576 J，所以本表没有重复计算这部分。

完整逐数组形状、固定原件来源及整数账在同目录 `static-resource-account.json`。原 source-of-truth 为 `captureCurrent/saveArray`、adapter 的 `export_inputs`、冻结 QR 的 `boundary_rho/save_factor/solve` 和 `OutputArrays.save`。

## 3. 真正的生命周期

单个 live worker 顺序处理实际协议请求。bootstrap 是新 worker 对成功 73 JSON 初猜的真实 H/J 求解；导入初猜不导入旧响应缓存或 predictor。后续所有新 H 仍走同一原进程；原相同 H 非 audit cache 可以减少协议次数，最终 audit 仍要求真实新请求。

每次需要 correction 的原 fresh withJ 已先完成。hook 在 `call-NNNN/iteration-NNNN/snapshot/large-arrays/` 同步保存本轮 states、J、r、out、H、target、sigma、cut、far。snapshot manifest/context/result 在对应原件之后完成；它不能代表未导出的最后无 correction 的 withJ 或全部 noJ 返回阵。

随后 `spawnSync` 启动本轮独立 QR 子进程；stdout、stderr 是本轮文件描述符，不用 worker 协议 stdout 传递日志，也不把大量输出收进 `spawnSync` 的内存缓冲。子进程先核 snapshot，依序写因子/常数，再回代、写完整 z/delta/checkpoint、exact ledger 与诊断。它退出后，Node 的 `checkedCurrentDirection` 完整读回身份和 delta；原 native 继续真实十试步。

成功 correction 尾部的 `returned-correction.json` 与完整 `current-corrections.jsonl` 记录，连同成功 QR 退出，构成一个可识别的已完成输出单元。`ctx.records` 和 `requestRecords` 继续保元数据、描述器和小报告，不持有旧 J 或因子的数组。`finishRequestContext`/`finishAll` 只访问这些元数据；原后续 native 用恢复后的 delta 和当前状态，不再读这一轮旧因子文件。

失败路径不同：只有在相关子进程完全退出、流关闭之后才能认为目录不再写入。snapshot 完成而 QR 失败、QR 已有部分因子却没有方向、或 Node 返回后原试步失败，都必须保留自己的真实阶段身份，不能生成成功方向或完整 native 标签。

## 4. 内存参数与磁盘参数不能互换

`--max-factor-bytes=2147483648` 检查的是完整因子/常数的**文件字节预算**，并非 Python RSS 限额。QR 逐 stage 处理一个有界 front：最大 672×449 个 f64 的主 front 为 2,413,824 B；实现还会有 QR 工作副本、R/S、LAPACK workspace、Python 元数据和当前块。它不会构造完整 129248×129248 稠密矩阵，也不会把全部 464 MB 因子留作一张 RAM 阵。

本轮 576 个原 J 自身为 231,211,008 B；Node 原 `ev.flows` 在同步 child 工作时仍存活。其 TypedArray/Buffer、原生库、缓存和操作系统页缓存不由 V8 `--max-old-space-size=6144` 单独覆盖，因此该参数不是 Node 总 RSS 或整个 job RSS 的证明。Python adapter 仅缓存 9 个非 J 原输入，J 按最多四 stage 的 chunk 流读；两个 exact worker 最多排入四个 stage task，仍有 Python 整数/序列化/子进程开销，不能由原始 J 字节直接推总 RSS。

fullDN 外层 Python 与内层 prefix solver 也仍存活；它们的稀疏/带状模型、解和工作数组不计入上述 native 文件账。实际峰值需分别保父进程、Node、QR 及其 exact children 的真实资源记录；单个 `RUSAGE_SELF.ru_maxrss` 不等于整棵进程树同时峰值。此说明不新增科学验收门。

## 5. 保全与后续可选归档边界

当前已完成源不会删除旧 snapshot/factor；磁盘与 inode 数随实际 correction 总数单调累计。上传原件时若另建 ZIP/tar，也可能临时并存原目录与压缩包，压缩率不能预先保证。Git publisher 只出版 bounded metadata；`large-arrays/` 仍由完整 Actions artifact 承载。

独立无损归档若以后实现，可在上节已完成 correction 边界或已完成 call 边界处理；应保完整目录路径、原文件 size/SHA、压缩容器身份及逐件解包核，不改任何科学数组 bytes。只有经过明确新运输策略保全原件后才有讨论本地重复副本回收的基础。旧 reader 仍期待 manifest 所列原 raw 路径，不能直接把 `.f64le` 换成 gzip 后冒充兼容；应先原路径无损还原，或使用明确新 archive-aware reader。此 note 不实施归档、上传或删除。

无论哪种运输方案，都保原 32 次循环、十 alpha、完整 FD、真实 endpoint sensitivity 与 fresh audit。资源不足只能记录实际中断和已保存范围；不能缩短科学迭代、以旧回应补新 H，或把跨进程初猜重标成旧缓存。

## 6. 本次源码更正身份

仅新 live client 两处容量字面值、新 driver 一处容量常量及其依赖 client SHA 改动。相对未发布前稿的完整可逆 diff 保在 `/tmp/noj-primal-live-resource/`；前稿完整保存在 `/tmp/noj-primal-live-multi-before-capacity-accounting-correction/`。

- client：29877 B / `7aa2aba10e44f0a0fd0e6eee47e9239a2f2244bb9663b8ec5ede294edc71bb64`。
- fullDN driver：32522 B / `bb8ad207c5b85fb10e0a5ee83b36eed4317c757646055eaec58b2bc3c8945c14`。
- hook 仍为 `0e802785329c73d5a951ca69942414ca5dcc40a9284dae9d31c4ca6cb819daa1`。
- adapter/QR 仍为 `e30e53e635f84ae4762ef045e6510c20d63524efd604ba617cec3a849bdfb3d3` / `c3284d556e76f389d084bc612579c485697f15aeb4c5b7a5caa49567a9920909`。

已发布 73、原 native、原 QR、exact 核和任何数学函数均未改。实际 73 的成功锚尚须由真实 result/J/audit 决定，本账不填未来回执身份。
