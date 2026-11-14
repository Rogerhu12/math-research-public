# 新存储家族的来源声明修正：v2

日期：2026-11-10；作者 /root，Astra-visible-flex-78718bd0。
状态：实际生成与读者小检查通过，修正闭包待未参与者完整核审。
本记录不把来源/存储检查称为真实候选、整图 metric、reach 或 G5 成功。

## 1. 实质缺口及其真实范围

未参与者全文检查 16 件新源、全部 134 项变换及消费者时发现：

- `78718-prefix-metric-budget-storage-v1.py` 的诊断报告 `backend_sha256`
  仍列旧 polynomial/continuous reader，实际 backend 使用新家族。root 877083 实读核实。
- `78718-prefix-angular-arithmetic-storage-v1.py` 的独立 tail CLI 报告
  `interval_backend_sha256` 仍列旧 continuous，实际 `poly.base` 是新 continuous。
  该 tail CLI 不在声明的 prefix 生产路由，但同样修正这项来源。

这些是报告来源错误，不是数值公式改动。完整 v1 源、账本与实际测试
全部保留，不将 v1 的全文审查伪记为无缺口通过。它们不被正在运行的
restart8000 BVP 使用，不修改该主计算。其完整历史见
[先前生成及真实读者检查](2026-11-10-78718-storage-adapters-and-reader-check.md)。

## 2. 最小另名修正与完整闭包

新 builder-v3 逐字派生自 v2，只改四个输出名字、增加三个报告路径 rename：

1. angular-arithmetic-v2 报告其实际新 continuous reader；
2. metric-budget-v2 引用 arithmetic-v2，并报告实际新 polynomial/continuous；
3. angular-metric-v2 把上述两依赖的文件名与实际 SHA 同步，调用新 budget；
4. terminal-error-v2 同步这三项 prefix pins 与 angular metric 选择名。

另 10 个 adapter 及两个 core 与已测试版本逐字相同。没有改原数学源、
序列化 payload、镜像公式、任何 interval/metric/moment/reach 数学公式、
原 tail/reference 家族、原 2e-9 终门及改善倍数常数。
新 checker-v2 仅把 builder-v3 和 terminal-v2 两个实际路径改为新入口。

root 实际工具 76e4d4 自然 exit 0：14 adapters、137 项唯一文本变换、
188 个完整函数 AST 与各自原数学来源相同；生成过程零数学 backend/solver。
实际 5a9e17 先核完整 12 件不变源再复制四件新源；无既有源被覆盖。
完整 v1→v2（含 builder/checker）diff 为 9745 B，root 用 a7b3aa 全文读完。
全部原→新变换的完整文本及源身份仍在 source-ledger-03，不由 AST 数量
单独推断改变函数的数学语义。

## 3. root 的真实读者及终门存储子程序检查

实际命令（仓库根为 cwd）：

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python topics/visible-flexible-closed-surface/scripts/78718-check-storage-readers-v2.py --scratch-dir /tmp/78718-storage-reader-fixtures-03 --source-ledger topics/visible-flexible-closed-surface/notes/2026-11-10-78718-storage-adapters-source-ledger-03.json --report topics/visible-flexible-closed-surface/notes/2026-11-10-78718-storage-readers-check-03.json
```

启动 5a9e17/session97276，完成回执 d9d110，真实自然 exit 0。
两种有限合成 payload 使用同一原 logical gzip/NPZ 字节；完整浮点/精确
读者系数、导数和 interval 范围比较通过。全部 14 源重放、16 源真实 import、
原完整 tail/reference 家族、13 prefix pins 与 11 angular pins 均实核。
新 terminal 的 `prefix_storage` 与 `prefix_storage_ledger` 在 fresh
stdlib-only 子进程实际运行，验证 defining base M24 与 expanded M64 分离，
迁移账本匹配及三个破坏案例拒绝。没有完整 producer/common-cut/candidate 调用，
`solver_calls=0`、`production_ready=false`。

这次实际小检查与之前独跑 313f38 的 v1 检查各自保留；不把旧检查
回执贴到新源上。后续仍须独审修正依赖闭包及在真实成功 CP 上运行生产链。

## 4. 冻结身份

| 文件 | B | SHA256 |
| --- | ---: | --- |
| `scripts/78718-build-storage-adapters-v3.py` | 21748 | `110457adcd109dcfd28cc285dc6458c97b37cd68858962b6ad44a5d3d8f43683` |
| `scripts/78718-check-storage-readers-v2.py` | 13224 | `78faf566f9b3ca3800d221b02fcd0363f64826025c4a4f8ac3c359bc42747565` |
| `scripts/78718-prefix-angular-arithmetic-storage-v2.py` | 23060 | `4977cb407bc9cdd64a580c999727a9978bf4041011e89cab192be7ecd2c2f5dd` |
| `scripts/78718-prefix-metric-budget-storage-v2.py` | 9661 | `18599b65771eae53199442589547105292489c323aac333e5eee6f2dacadb3aa` |
| `scripts/78718-prefix-angular-metric-storage-v2.py` | 24403 | `7f60b8431c10ef93878049be0ae9d9677df268b7cb3963315096103bafdd0dc1` |
| `scripts/78718-prefix-terminal-error-storage-v2.py` | 48878 | `882086b30a5af04fbac558234295eab035e24608727c605a9dfd9aae36a0cabd` |
| `notes/2026-11-10-78718-storage-adapters-source-ledger-03.json` | 61588 | `1b7e05df897d10e77c056151e2beb0b8eee1ea7e86e28fb9bdef9899b22a6dde` |
| `notes/2026-11-10-78718-storage-provenance-fix-diff-03.txt` | 9745 | `100fd59c1ca1281f8b455dbf4dc77c019cfc0e715fae38b453c6c18477fc9c9b` |
| `notes/2026-11-10-78718-storage-readers-check-03.json` | 12678 | `0cd8154250c031eb41304d07374f4b1cc7692b5be8b612c730e62b0abd4dcdb7` |
