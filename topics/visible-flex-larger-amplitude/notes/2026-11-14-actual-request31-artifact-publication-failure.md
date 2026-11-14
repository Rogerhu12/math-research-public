# actual31：完整输入已核，目录发布失败，科学计算未开始

公开 run [43614888444](https://github.com/Rogerhu12/math-research-public/actions/runs/43614888444)，source `65bc77555648c2abd5fcb88b371884c0e6211516`，job `132507703327`。运行创建于2026-11-14 16:18:33 UTC。下载步骤失败；后续带状重解没有执行，不能把此失败解释为矩阵、分解或数学失败。

原下载器 SHA `523ba20e28008607304223d684775f3d2ec3e2f554188b2be36c40b8aa776504`。实际日志16:19:03.7228901Z记录 metadata verified；16:19:19.3094740Z记录完整收到235561097字节后，在 `publishing-validated-read-only-payload` 阶段报 `ATOMIC_PUBLISH_FAILED`，程序exit2。日志中的 archive_received_bytes 与硬锁大小一致。按该冻结代码实际控制流，此阶段只能在完整 ZIP 大小/SHA、提取路径和逐成员 CRC/大小/SHA 全部通过、临时 ZIP 删除、回执生成和只读权限设置后进入。

原目标为 actual28 artifact14120548264，ZIP SHA `0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee`。失败点是 `renameat2(RENAME_NOREPLACE)` 返回非零。旧代码没有保存errno，因此不臆断是权限、已存在目录或文件系统功能导致。没有完整发布成功；后续科学步骤被跳过。完整原输入仍在actual28公开artifact，未改字节。

## 传输修复与续算

request33只修传输发布：目标带实际run/attempt以隔离各次计算；普通 `mkdir` 独占创建全新0700目录，若已存在则失败，不覆盖；移动已经核验过的payload子项，回执最后移动，完成后目标0555。这不是整目录原子发布；所有科学消费者只在该命令成功返回后启动。失败记录固定phase/数字errno，清理由此程序独占新建的目标，不输出异常URL或凭据。metadata/ZIP/路径/CRC/SHA/只读字节检查和原PIN均不变。

下载器新SHA `0108d824f39e1808cf64bbd599667efa707f852b0ed715627a7ee87e46e280e8`。带状计算源仍为 `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390`，科学输入、尺度、方程、方向恢复和全部原读回均未改。此修复未本地执行网络或科学计算；仅AST/源码/字节/工作流静态核验，重新执行属于公开Actions。
