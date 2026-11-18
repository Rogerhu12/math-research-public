# n4 原生批求值的四进程接入：独立源码安装

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 本次完成的范围

已在新的 `n4_work/native-parallel-source-v1` 安装四进程批求值入口。安装程序真实退出为 0，四个 `node --check` 均退出 0；没有构造新物理模型、执行新 flow、重算 Jacobian 或启动新 DN。原串行 DN 会话 `35038` 的源码、manifest、输入与运行进程保持原样。

四进程包装器本身的完整 2304 段数值字节等价与单次耗时已经由[独立批次记录](2026-11-18-n4-parallel-original-native-byte-identity.md)登记。本条只处理其进入现有 Node 接口时的执行及来源绑定，不重复该数值计算。

## 接口变化

新安装器从已记录的串行 owned tree 复制源码，只修改 `native_batch_adapter.mjs` 的六处进程启动或元数据块。把这六处补丁逆向应用后，得到原 `9931feea…` 源的完全相同字节；其余 45 个 owned `.mjs` 源的字节全部不变。完整输入的几何、三角系数、实际 cusp 网格与状态打包，以及输出解码、动量行的 `portRatio` 变换，均沿用原实现。

每次原 `evaluate` 现在通过明确的 Python 路径启动冻结包装器，再由它启动四个原 C++ CLI 子进程。`native_files.executable` 仍然是 `1b47ed47…` 的原 C++ 可执行文件。Python、包装器、执行计划及已完成的等价记录列在单独的 `execution_provider` 字段中；包装器的哈希没有替代 C++ 二进制哈希。

执行计划使用同一个冻结包装器、原 CLI、四个 worker，并保留各子进程输入、输出与日志。原完整批次的输入身份与来源身份分别检查。Node 在读取合并后的原 wire 之前，核对包装器的实际来源、计划、原 CLI、父返回码及四个子进程的文件哈希。原完整输入或任何数学求值没有在该来源检查中重新生成。

包装器按原 stage 次序合并结果，原首个数学域失败仍通过原 wire 和返回码传给已有解码器；工程失败保留为工程失败。原 DN 的目标、归一尺度、远端 Robin 条件、线性校正、线搜索、`2e-9` 门、cut 数据和审计实现均未改动。本次安装不声明新的实际尾接受，更没有声明 full H、前缀联立、精确圆弧或闭族完成。

## 可追溯文件

| 对象 | SHA-256 |
| --- | --- |
| 安装源 `scripts/resume_n4_tail/native_extended/install_native_parallel_adapter.py` | `3d157b4e5fbe59d1df073781faa2eab319d819b0fef122c997d028ad5bdd1a15` |
| 新 owned adapter | `0eab1ee41a2c1851dbf9c17f2c608d68547ca779558c350ad954ed8ecfb5f530` |
| 新 manifest | `1661d97aba9dc5ac332ca859ad968b93164e8255df9d52a814d61338ada599c6` |
| 新执行计划 | `4f463dc37b27338e07d48c8520059c0e707806e178bebd184467026007022677` |
| 原安装输出 `preparation.json` | `bb88d0a4850a7b6c546c6513b09a31f6bdab1a1edbeae123f01090b5ae17a709` |

紧凑记录为 `scripts/resume_n4_tail/native_parallel_adapter_entry.json`，包含实际命令、四个语法检查的退出码与全部来源路径。安装器的真实工具会话为 `88519`，终态 chunk 为 `c11888`、退出码为 0；单独的 `prepare-terminal.json` 明确是该工具结果的记录，并非另一个数学程序的 observer。完整 manifest、补丁、子目录及后续运行文件仍留在 scratch，不把场、节点或逐段表复制到 Git。

`closed_geometry` 已只读核对六处逆向补丁、其余 45 源、111 个来源引用和实际进程协议，未执行新的模型或流。后续实际 DN 将使用独立的新运行目录与完整目标，并继续支付原接受门和审计。
