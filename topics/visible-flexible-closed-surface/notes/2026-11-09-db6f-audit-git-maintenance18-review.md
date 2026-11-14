# 单个大重复 promisor 包的维护前独审

状态：预检 PASS，尚未执行维护。审查者 `/root/independent_geometry`。

在 root 必要发布关闭、primary 已同步 `f354bacff815847557d1918b0d8cc3a54a42ea8b` 后，fresh 检查实际退出 0（`4fd03c`，1.303 秒）。其前后 pack 元数据、refs/HEAD 和 loose 文件名集合相同。补充的小重构 payload 也在同一未变快照上核验完成（`8d31bf`，exit 0）。此前发布前的初扫没有当作本次冻结状态。

## 单一候选与精确缺口

本次只考虑移除 `pack-d44586219587f80e0b96f6485973557d6a009d35`，不同时移除其他小包。它带 promisor 标记，大小 **665,351,595 B**，索引包含 **2,493 个 OID**。

其余 promisor 包已覆盖其中 **2,466 个**；同分区联合独有集合恰为 **27 个 OID**。判定覆盖时没有借用 ordinary 包。救援列表按 40 位十六进制逐行 LF 排序，共 **1,107 B**，SHA-256：

`167dc0a63cea1652cd8561b09b67bd00d6d1e412c2edf91de46cc64e319f4802`

列表文件为 `2026-11-09-db6f-audit-git-maintenance18-rescue-oids.txt`。已经逐集合核实：

- 保留的 promisor 联合与这 27 个 OID 的并，精确等于原 promisor 集合；
- 两个原 ordinary 包完整保留，其固定 idx SHA 通过；
- 原 promisor 与 ordinary 的交集为 **0**，救援列表也不与 ordinary 相交；
- 两个 canonical promisor 包及两个 ordinary 包的冻结 idx SHA 均未改变。

27 个 OID 的数量本身不证明未来 rescue pack 的压缩大小。实际写包、校验其精确 OID 集合与字节大小仍由 root 支付。

## 原始集合与可重构证据

| 项目 | 冻结数值 |
| --- | ---: |
| 原 pack 数 | 23 |
| pack 总字节 | 5955061970 |
| promisor 不同 OID | 118413 |
| ordinary 不同 OID | 1708 |
| 全部已索引不同 OID | 120121 |
| loose 文件名对应 OID | 678 |
| 已索引与 loose 联合 | 120763 |

全部已索引集合的排序原始 20 字节序列 SHA-256 为 `61e809f1d8b4d335ee3cc3a5033d8e5bb927121253bd5889100d0cd88b70b06f`；全部已存在集合对应 SHA-256 为 `1cb5f16dc39e10acd26b8859a7537c079df609c16a444a1251b2093f23b2c000`。

预检 JSON 保存每个保留 idx 的完整 SHA、OID 摘要、pack 字节及 promisor 标记。小 gzip payload 只保存目标包的 **2,493 个 OID** 和 **678 个 loose 名称**，大小 **77,726 B**，SHA-256 `8bdea818a0156aa955a10218e92ac0b3853804ca807d1efe3f5b545c657cdc7a`。后验时，保留 idx 逐 SHA 不变，加上这一目标旧列表，即可重新构造旧的已索引全集；再加入旧 loose 名称得到旧全部存在集合。没有重复保存全库 OID 大快照。

原 **23 个 pack 文件的 mtime_ns** 已显式保存在 payload-binding JSON；预检 `inventory_stats` 还保存了所有相关文件的 `[bytes,mtime_ns,inode]`。因此本次能以真实前值核对保留 pack 的时间恢复，不能用维护后的值倒填。

## 必须另付的删除前条件

当前 MIDX **没有列入目标 d445 包**。这种缺席不是可过期删除的“selected owner 为零”证据。root 后续必须在 rescue 成功后重建包含全部保留包、目标包及 rescue 包的新 MIDX，核全 OID 覆盖与分区，并确认目标被列入且 selected owner 精确为零。之后才可走标准 MIDX expire，并核实际仅删除指定目标、集合及引用不变。

本报告不证明上述写包、MIDX 更新或 expire 已经发生。所有检查仅读取 idx/MIDX、引用、文件名与 stat；没有读取 pack 或 loose 内容，没有 Git 子进程、fetch、GC、repack、认证/环境读取或数学计算。
