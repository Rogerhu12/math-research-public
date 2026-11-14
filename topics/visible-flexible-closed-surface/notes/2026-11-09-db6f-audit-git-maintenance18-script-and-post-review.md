# 维护 18 脚本静审与独立后验

结论：**已审脚本静态 PASS；维护后的独立只读重构实际 PASS。** 审查者 `/root/independent_geometry` 没有执行维护脚本，也没有运行任何 Git 子进程或网络请求。

## 实际后验结果

独立入口 `scripts/db6f-audit-git-maintenance18-postcheck.py` 实际退出 0，工具收据 `18b7ad`，耗时 2.002 秒。报告 `2026-11-09-db6f-audit-git-maintenance18-postcheck.json` 的 SHA-256 为 `54e6c798c7636e64231670cd3ec9947c9aa984859c70a672dafc2a11e511cf08`。

这次不是照抄 root 的集合摘要：从当前 **22 个保留 idx** 逐 SHA/完整元数据核对不变，再加入预先冻结的目标包 **2,493 个 OID** 与 **678 个 loose 名称**，独立重构旧集合，并与新索引和实际 loose 集合逐元素比较。

| 核对项 | 独立结果 |
| --- | --- |
| 实际去除的原 pack | 仅 `d44586219587f80e0b96f6485973557d6a009d35` |
| 实际新增 rescue | `54c9604895d20ebd3d60fe9d9246d0fb7832fd4b` |
| rescue 对象与原同分区缺口 | 精确相等，27 个 OID |
| rescue 大小 | 414,447 B |
| 当前 pack 数 / 总字节 | 23 / 5,290,124,822 B |
| 净减少 pack 字节 | 664,937,148 B |
| promisor 集合 | 118,413 个，与原集合逐元素相等 |
| ordinary 集合 | 1,708 个，与原集合逐元素相等 |
| 两分区交集 | 0 |
| 已索引集合 | 120,121 个，与原集合逐元素相等 |
| 已索引与 loose 联合 | 120,763 个，与原集合逐元素相等 |
| 原 loose 名称集合 | 精确不变 |
| refs/HEAD 原始文件 | 精确不变 |
| 所有 22 个原保留 pack | 原 `mtime_ns`、inode、字节数逐项相同 |

保留 idx/标记的原完整元数据也未改变。目标原文件已经全部消失，新增文件恰为 rescue 的 pack/idx/promisor 三件。所有时间对照都使用此前真实冻结值，而不是维护后再构造“原时间”。新 rescue 没有原始时间可比较；已删目标也不在“22 个保留包时间恢复”声明中。

当前 MIDX 的全部 OID、选中 pack 与 idx 偏移逐项重验，完整覆盖全部 120,121 个已索引 OID。其当前完整摘要与 root 最终记录相同，选中 owner 计数与 root 删除前摘要相同。由于每个 owner 的 OID/offset 已与实际 idx 核对，且两分区互不相交，当前 owner 的分区也没有跨越。

## 运行脚本的静态独审

root 最终脚本 `scripts/db6f-root-git-space-maintenance18.py` 的 SHA-256 为 `1f82bf0328f46b570831c8a0046d6cacc8e1fc3ec4df680ef203f857b96be34f`。先前完整审读的版本为 `ddb6d2d4d1e05896f9f50d047b97020f64fba38d31470540cfb960a2f09ea803`。最终两处修订完成后，独立作了精确反向替换，整文件恢复原 SHA（工具收据 `a34686`，实际 exit 0），因此没有仅凭作者声称“其余不变”。

逐条审过的保护链如下：

1. 任何写操作前，绑定 fresh 预检 SHA、读取器 SHA、23 包完整 inventory、refs/HEAD、各 idx 完整元数据及全部集合；重新计算同分区 27 个缺口并与救援文本逐字核对。
2. 使用 stdout 生成自包含 rescue，再 index-pack，验证其精确 OID 集合为缺口、标记为已知 promisor。安装 rescue 时保留全部旧包；不存在以 ordinary 数据代付 promisor 缺口的分支。
3. 派生 MIDX 有独立备份。仅给保留 promisor 包设置临时优先时间；重建后核全部包、全部 OID、每个 owner 的真实 idx 偏移，以及保留加 rescue 的 promisor 联合与 ordinary 联合分别不变。
4. 删除前要求零 owner 包列表严格等于 `[d445...]`。最终修订将完整 MIDX 摘要与零 owner 名单放在此断言之前记录，所以额外零 owner 会安全停止并留下证据，不扩张删除范围。
5. 标准 expire 返回后再次核 pack 名精确差集、保留 idx 元数据、两分区、loose、refs 和新 MIDX；没有把“调用返回 0”单独当作完整保留证明。
6. finally 恢复全部仍在的原 pack 时间。最终修订把恢复布尔量升级为完成硬门：失败先记 `FAILED_ORIGINAL_MTIME_RESTORATION` 并写记录，再断言，不能继续打印成功。

没有发现违反本次单包、同分区保留条件的接受路径。静审结论本身不是操作执行证据；root 随后真实执行的记录与本次独立后验分开绑定。

## 执行记录与范围

root 完成记录 `2026-11-09-db6f-root-git-space-maintenance-18.json` 的 SHA-256 为 `300bb6762758c9ff03ef872540aa1a59aafd4af529b84c14f553eb8f06062bb0`；root 独立 observed-execution 记录的 SHA-256 为 `c3e96e17f5b9ec807b573105f5ff76a88b72b6f948bfa09f6a7a5116b72c4b1e`，记载 session 84439 / completion `f368cf` / exit 0。后验核查实际绑定并读取了这两件文件。

删除前的历史 MIDX 状态、标准 expire 的运行过程，依据已审源与绑定的 root 执行记录；本后验没有声称回到过去另行观察它们。当前 MIDX、实际对象集合与文件状态则已独立重验。没有解码或重新哈希 pack 对象内容；独立检查的范围是 idx 校验和、OID/offset、MIDX、文件元数据和引用。原 atime 未由本审查冻结，不纳入独立恢复结论。

未新增全库 OID 大快照，也未改变数学候选、求解输入、HANDOFF、LOG、results 或 Git 状态。此次运营审查不改变最终 M15 未参与优化的独立全流程角色。
