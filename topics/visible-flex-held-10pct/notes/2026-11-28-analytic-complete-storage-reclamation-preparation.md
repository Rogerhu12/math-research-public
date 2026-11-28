# 完整 CSR/QR 的逐数组回收：真实源码定位与独立存储分支

会话：Astra-held10-7c4e33ee-20261128 / analytic。日期：2026-11-28。

**可信度：源码事实、系统接口合同和入口准备；没有新的因子、Jacobian、BVP 或数学接受结果。** 本条不把任何 `−9` 解释成 OOM，也不宣称已经观测到文件缓存或 cgroup 使用量下降。主线原方程、完整未知、域、RMS、BC、metric 与物理高度门保持。

## 1. 本次定位究竟说明什么

已冻结 `design/complete_csr_prefactor_mmap.py` 的 `BeforeQRMappedBlockQR.__init__` 顺序为：完整 CSR 映射；原 `_CONSTRUCTOR`；恢复 CSR 实例的原 `prune`；核原矩阵对象未替换；释放 CSR 映射页；最后调用 `CompleteFactorStore`。因此在本入口中，**因子专属** `complete-qr-*/all-arrays.bin` 已实际预分配，意味着原完整 QR 构造器已经返回，且因子 mapper 的完整 layout 元数据枚举也已经完成。它不同于外层 `factor_return` 日志；后者要等全部因子映射完成才记录。

主线 77523 的具体退出、398401536 B 因子 backing、原 97ec 全状态和 owner join 由 design 的独立真实终态记录负责。本条只给上述源码次序的解释，不能由因子文件是否存在推断终止原因或某个数组已经完整复制。

`CompleteFactorStore` **原本已经逐数组替换**：`_get → ravel(K) → 每块复制/逐字节检查/flush/MADV_DONTNEED → _set → del source, flat, mapped`。layout 仅保 path、shape、dtype、order、offset、长度和 SHA，不保旧 ndarray。已验证 C/F 连续的 `ravel(K)` 不需要第二份整套因子；不以不存在的“全量旧数组列表”解释峰值。

确实尚可改善的存储时点是：原 QR 返回时，递归旧 edge 与临时局部数组已失去引用，但原因子 mapper 要在**全部**数组复制完成后才调用 `collect_and_trim`。单个旧数组释放也不保证分配器立即把其空闲页归还内核。此外，对文件映射执行 `MADV_DONTNEED` 不等于保证该文件的缓存页已从系统或 cgroup 记账中移除。

## 2. 新分支保留的完整对象与最窄改动

实际可接入口为：

`scripts/resume_20261128/analytic/complete_mapped_storage_reclamation_v3.py`

API `ReclaimedBeforeQRMappedBlockQR` 与原 `BeforeQRMappedBlockQR` 的参数合同相同。顶层构造器使用同一个 Python code object，只将其全局字典中的两个存储类显式替换为独立新类；原递归 QR、全部行/列/参数、原完整 CSR、原求解/残差修正/诊断方法均保留。

新增操作仅为：

1. 每个原映射阶段开始前执行已有 `collect_and_trim`。因子阶段此时已在原完整 QR 返回之后。
2. 原映射循环执行 `_set` 和原 `del` **之后**，累计已经替换的原数组达到 16 MiB，再执行已有 `collect_and_trim`。逻辑字节累计只触发时点，不作为 RSS 信用。
3. 在原每块 flush 和原 `MADV_DONTNEED` 成功之后，对同一唯一自有 backing 文件的相同页对齐区间调用 `POSIX_FADV_DONTNEED`。CSR 和全部因子均覆盖；文件、完整内容及原哈希检查不删除。
4. 只读记录实际 RSS、RssAnon、RssFile、MemAvailable，以及当前可读的 cgroup 数字和 `memory.stat`。无法读取仍明确 unknown。追加的小 journal 每条 flush/fsync；它位于 backing 目录之外。

两个原 mapper 的块起点为页对齐 array offset 加 8 MiB 的整数倍；原 `mmap.flush(lo, round_up(hi)-lo)` 已覆盖最后部分块的整页，且范围在已预分配文件内。CSR 原零压缩之后先全映射 flush 再释放全部页。因子/CSR readonly 后的原 solve 只有读取，不新增 mapped dirty 数据。追加建议使用短寿命只读 fd，`finally` 关闭，不留下 fd 或 factor/matrix/旧 ndarray 回指。

`POSIX_FADV_DONTNEED` 返回成功只表示建议被接口接受；不能登记成已降低 cgroup 内存。它可能增加之后实际读取的 I/O。原完整构造峰和外层 RAM/磁盘预算仍须保留，不能减去逻辑映射字节来虚构可用 RAM。

## 3. 系统语义和本次只读文件系统事实

Linux man-pages 的 [`madvise(2)`](https://man7.org/linux/man-pages/man2/madvise.2.html) 说明，共享文件映射的 `MADV_DONTNEED` 后重新访问会从底层文件恢复；物理页回收可延迟。[`posix_fadvise(2)`](https://man7.org/linux/man-pages/man2/posix_fadvise.2.html) 说明其建议不具强制性，`DONTNEED` 尝试回收文件缓存，部分页可被忽略，未写回 dirty 页不会被回收。这里沿用原同步 flush，并使用页对齐范围。Linux 内核 [cgroup v2 文档](https://docs.kernel.org/admin-guide/cgroup-v2.html) 的 `memory.stat` 区分 anonymous、file cache、mapped file、dirty/writeback 等项目；进程 RSS 不能代替这些真实观测。

root 的实际只读 `findmnt`（工具回执 `bc28c2`）显示 `/workspace` 为 `/dev/vdb`、`ext4`，选项 `rw,nosuid,nodev,relatime`，不是 tmpfs。本条没有挂载、改 cgroup/限额或清理系统全局缓存。该文件系统事实支持使用磁盘 backing 的方案，但仍不证明本次 advice 的收益。

## 4. 入口历史与实际执行范围

三份源都保留原字节：

- 初版 `complete_mapped_storage_reclamation.py`，SHA `310874d19c77cc74b8e82e4a2d96898dd705aea1e4b785446f245d38e3b39c40`。编译实际 0；`--help` 导入实际 1：`textwrap.dedent` 后的 mapper 源比字符串锚少四格缩进。工具 `4f9be9`，未构造因子或运行数学。
- v2，SHA `abba44f46e4a5b547a04276b90d59aa19792b5f22fedf8c957d57cd008b313af`。仅修正两个锚和插入语句的缩进，compile/help/describe 全部 0，1.3299310809998133 s，子进程峰 48976 KiB。之后只读发现其 journal 若位于 store 根，会违反原 owner cleanup 的严格目录合同；v2 没有用于数值。
- **v3**，SHA `2dac1ddb506c7065c8f53c29e407b53ca797a298c2cc59dbb274b95cbfdf9f06`。仅把 journal 改为 store 的同级 `mapped-factor-storage-reclamation.jsonl`，并修正说明字段。原 cleanup 不放宽。compile/help/describe 全部实际 0，1.413794845000666 s，子进程峰 48972 KiB；真实 `constructor_code_identical=true`、`solve_method_identical=true`。

v3 准备记录：`held10-analytic-work/storage-reclamation-preparation-20261128-c/preparation.json`。前两次各在同名前缀 `-a`、`-b`，保实际错误和来源。小汇总见同名 JSON。

后续使用时仍需真实 owner 等待子进程终态再执行原 `mapped_complete_storage_cleanup`。journal 在其删除域之外，原科学状态、矩阵、参数和来源不在删除域内。调用方必须显式绑定 v3 的真实 SHA，不能把新行为贴成原 storage 源。当前只有入口准备；同 97ec 的下一次实际求解若执行，另行登记完整真实结果。
