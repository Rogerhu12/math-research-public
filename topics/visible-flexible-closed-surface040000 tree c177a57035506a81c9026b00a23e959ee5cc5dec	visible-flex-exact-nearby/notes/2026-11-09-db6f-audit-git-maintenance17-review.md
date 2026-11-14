# maintenance17 独立只读验收

审查者：`db6f/independent_geometry`。状态：**PASS，已实际执行原始索引集合比较；不涉及数学求解。**

## 冻结输入与实际执行

此前只读预检报告 SHA256 为 `f6be4675466dd82f9589fc10cb16021cd09d38bc56bca07b5e5eaf9f40b839bf`，逐包 OID 冻结 gzip 为 `c7701e26f4f56ff5e52050696f19064262bd497df77471d9fa2667dc9940ddf5`。原预检实际 exit 0，receipt `8b7ef7`，1.619 s。

本次绑定 root 完成记录 `2026-11-09-db6f-root-git-space-maintenance-17.json`，SHA256 `7c1e20145df61c3ef1563f93eb3f9063ba61b3b34d61c32415ca41773688ef24`。独立程序 `scripts/db6f-audit-git-maintenance17-postcheck.py` 导入原已冻结的只读 idx/MIDX reader，用新读出的当前索引与旧 gzip 中的**完整集合逐元素比较**；不是只检查 root 摘要中的布尔字段。

命令（本题目录作为 cwd）：

```sh
python -B scripts/db6f-audit-git-maintenance17-postcheck.py --out notes/2026-11-09-db6f-audit-git-maintenance17-postcheck.json
```

实际 exit 0，receipt `f7aff9`，2.575 s。小报告 SHA256 为 `c340a5dfa11fdc406c18ff12bc65c49617e899ebf40c780105d464e1318b330f`。原输出已冻结，重放时应使用新的 `--out`。

## 已独立核实

- 新包 `181ee1706f018d61bf0f1640334ebaf1a4d8ecf0` 为 known-promisor，idx 恰等于旧大包 `466847…` 与 `b3912f…` 的**联合缺口 66 OID**，不是各自独有的 17 与 43 的简单并集。差集 sorted hex＋LF SHA256 为 `4c75c24571f764148c47a710ebc08a7a3c986cbaf5017cec0a4fc1a2469d59b8`。
- 相对于原 15 包快照，只新增该 rescue 包，只移除指定两大包；当前 14 包合计 5,261,709,057 B。其余每份 idx 哈希、pack 大小和 promisor 标记均不变。
- indexed 115,207、包括 loose 文件名的 all-present 115,682、known-promisor 113,499、ordinary 1,708，**四个集合全部与原冻结集合逐元素相同**；promisor 与 ordinary 仍不相交。
- all-present 的 sorted raw SHA256 为 `c1e10c30d3976e78dcee158c6dc2d4a64571af6f703abe197090d1743a9cfb62`。重复 loose 的移除没有改变该集合。
- 当前 MIDX 校验和正确，覆盖全部 14 包的精确索引并集；115,207 个 selected owner 的 OID 和物理 offset 均逐项与所选 idx 对上。当前 owner 计数与 root 报告的删除前 owner 计数相同；结合两分区不交，owner 不会跨 promisor/ordinary 分区。
- 所有冻结 refs、主 HEAD 及关联工作树 HEAD 的原始文件逐字相同，规范化记录 SHA256 为 `91809fb7ef239baaaf5b8039da30f44680cf6d19b64015119df9cb58910b3e6e`。读取期间包目录元数据、refs/HEAD 与 loose 文件名清单均稳定。

原预案的 6,356 OID promisor 差集文件仍是原冻结集合的有效差集；本次紧急维护实际采用 66 OID rescue 后释放两大包，而没有声称已执行整个差集合并。

## 作用域

本次只读 idx/MIDX、refs/HEAD、文件名和大小，未读取 pack 或 loose 对象内容，未运行 Git 子进程、fetch、fsck、verify-pack、求解器或后端；只新增小程序、小验收报告和本说明，没有新增完整大 OID 快照。

原 preflight 没有保存各 pack 的原始 mtime，故**mtime 恢复不在本次独立认证范围内**。root 的实际执行顺序、删除前零选检查及时间恢复记录作为已绑定的作者执行记录保留；本次认证维护后的集合、分区、索引 owner 与 refs/HEAD，不从事后状态虚构运行时历史。
