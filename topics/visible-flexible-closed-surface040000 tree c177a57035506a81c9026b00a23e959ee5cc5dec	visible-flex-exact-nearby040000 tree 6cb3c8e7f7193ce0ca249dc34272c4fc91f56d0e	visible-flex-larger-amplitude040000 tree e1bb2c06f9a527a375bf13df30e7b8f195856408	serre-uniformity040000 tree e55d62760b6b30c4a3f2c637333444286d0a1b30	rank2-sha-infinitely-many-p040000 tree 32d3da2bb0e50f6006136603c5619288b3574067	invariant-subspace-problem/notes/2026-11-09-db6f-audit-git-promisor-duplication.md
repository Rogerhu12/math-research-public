# Git 2.51.1 重复 promisor 包：只读因果诊断

日期：2026-11-09。审查者：`db6f/independent_geometry`。本项是发布可复现性的运营诊断，不参与 M15 数值优化。

## 1. 结论与证据层级

**最具体的上游解释是 `OI_DBCACHED` 被误当作非 promisor 对象；当前不能将 `core.deltaBaseCacheLimit=0` 称为关闭缓存或已证修复。** Git 官方后续提交 `7a4bd1b836c7437dfb8ff3650096750b98a6b3e4` 明确修正了这一分类问题，所点名的两个调用者与本机版本的源码一致。[S1–S4]

本机实际输出为 `git version 2.51.1`。已直接读取官方 `v2.51.1` 的 `builtin/index-pack.c` 与 `builtin/pack-objects.c`，确认相关判据；已读该版本标签指向的提交与后续修复的父提交。没有对本机二进制作逐字节源码认证，也没有捕获造成当前大包的运行时 `whence` 值。因此，这是**有具体上游缺陷支持、与本地索引现象相符的首要诊断**，不是已经复现并定位到某条运行时分支的结案。

## 2. 本地只读索引证据

原始观测冻结在 `2026-11-09-db6f-audit-git-promisor-index-observation.json`，SHA256 为 `7f50b1d30363d2dcbf86b1d8a33af012ba307f8d8cbafabaaa9b095b4d5f8db3`。只读 `.idx`、MIDX、文件大小与 marker 是否存在；没有读取 `.pack` 内容。

| 项目 | 观测值 |
| --- | ---: |
| 当前大包 `pack-46684770d20796511bfae2110567a4142002db43` 大小 | 663,969,684 B |
| 该包 OID 数 | 2,174 |
| 同时存在于其他包的 OID | 2,151 |
| 同时存在于两份 canonical promisor 包的 OID | 1,997 |
| 与普通非 promisor 包的 OID 交集 | 0 |
| 不在其他包中的 OID | 23 |
| 该包 OID 中还存在 loose 副本的个数 | 23 |
| MIDX 已覆盖的该包 OID | 2,149 |

MIDX 对上述 2,149 个 OID 的 selected owner 分别为 canonical `2bb64…` 的 1,026 个、canonical `3eb380…` 的 971 个、promisor `086b47…` 的 152 个；三包的 `.promisor` 标记均在。全部 `.idx` SHA-1 trailer、排序与唯一性，以及 MIDX 的校验和、每个 selected owner 对应索引中的成员关系均通过。大包 OID 集的 SHA256 已写原观测，未在对话中传送 OID 列表。

这些结果排除了“当前 MIDX 将这些 OID 指到普通包”作为该批重复的解释；也说明旧 loose 副本并不足以解释 2,151 个已打包对象再次入包。23 个 loose 的计数与 23 个不在其他包中的计数相同，但本观测没有单独声明这两个集合逐项相等。

## 3. 已核对的源链

官方 `v2.51.1` 标签指向 `81f86aacc4eb74cdb9c2c8082d36d2070c666045`，标签时间为 2025-10-15。[S1]

在该标签的 `index-pack.c` 中，`--promisor` 使 `record_outgoing_links` 为真；末尾直接调用 `repack_local_links()`。该函数检查本地可找到的 outgoing OID，仅在 `info.whence == OI_PACKED` 且所选包的 `pack_promisor` 为真时跳过。其余对象交给本地 `pack-objects --exclude-promisor-objects-best-effort`，输出包随后取得一个**空** `.promisor` 文件。[S2]

同标签的 `pack-objects.c` 将 `is_not_in_promisor_pack_obj()` 作为遍历的筛选函数；该函数同样把 `whence != OI_PACKED` 当作应纳入的条件。它并不是对全部 promisor 对象及其引用闭包做完整成员测试。[S3]

官方 2026-01-12 提交 `7a4bd1b8…` 的说明直接点名这两个调用者：缓存中的 packed 对象可能报告 `OI_DBCACHED`，因而漏过上述排除门。修改删除该枚举，令 packed 信息统一报告 `OI_PACKED`。[S4] 这给出即使 `.promisor` 标记和 MIDX owner 都正确，仍可能重打包旧对象的具体路径。

这条源链与 root 已观察到的“接收小包后，本地额外生成大包”及空 marker 形态一致。空 marker 本身不是运行时归因的充分条件。该提交还修正了 2025-11-23 引入的另一项 streaming 崩溃；**本报告不把那项较晚引入的崩溃归给本机 2.51.1**。

## 4. 为什么 `deltaBaseCacheLimit=0` 不是已证关闭

直接可取的两个官方 `packfile.c` 快照是 `v2.51.0-rc0`（blob `5d73932f50ce6854d695e92d049c6a6c0a1421a7`）及修复父提交 `123e8186a72cd71863668b6acb23a2faa30e6968`（blob `08a0863fc3374c982029d50116f6018e4fcdde92`）。两者的相关控制流相同：[S5–S6]

1. `unpack_entry()` 在 base 不是 external base 时调用 `add_delta_base_cache()`，没有 `limit > 0` 的调用门。
2. 新 base 的大小先加入累计量。
3. 依次清除旧 LRU 项，直到累计量不超过 limit 或旧项耗尽。
4. **随后无条件为新 base 建立缓存项。**

所以空缓存、正大小 base、limit 为 0 已构成一个源级反例：清旧项的循环没有可清对象，新 base 仍插入。后续查询它仍可能得到 `OI_DBCACHED`。这不是实际 fetch 试验，而是对已读 C 控制流的直接推论。

可严格说的较弱性质是：**每次插入一个正大小的新 base 时，0 limit 会清空全部旧项，然后保留这个新项；若所有缓存 base 均为正大小，则缓存至多保留一项。** 零大小 base 的边界不能被这句话无条件覆盖。即使只有一项，该项仍足以触发错误的 `whence` 分类。因此 0 可以改变缓存驻留规模与重复概率，但没有消除该缺陷的保证，且可能增加重复解压成本。

`v2.51.1/packfile.c` 的单页及对应范围 diff 在本次网页工具中不可取，不能把两个邻近快照冒称为该 exact tag 的文件；精确标签的两个**调用者**已直接取得。官方 2.51.1 配置文档说明默认 96 MiB，但未承诺 0 是关闭开关。[S7] 所以仅凭该文档更不能给 0 作关闭语义。

## 5. MIDX 与可控下一步

已读官方 packfile 源中，MIDX 改变 packed copy 的查找路径；`.promisor` 文件用于设置每个 pack 的 `pack_promisor` 标记。它没有把 `OI_DBCACHED` 改成 `OI_PACKED`。[S5] 当前观测的 selected owners 全为正确的 promisor 包，故本次没有证据支持先试 `core.multiPackIndex=false`。此参数保持不变。

当前最稳妥的执行选择仍由 root 按既有同 OID 维护流程推进必要发布。**本报告没有发现可直接称为修复的单次 fetch 参数。** 真正对应此分类错误的上游代码修正是 `7a4bd1b8…`；本次没有安装、编译、升级或补丁操作。

若 root 以后决定在一次本来就必要的 fetch 上仅附加 `-c core.deltaBaseCacheLimit=0`，应标记为**减少缓存的受控经验试验**，保留其他参数、二进制、认证、对象布局和 MIDX 设置，并比较新包大小及其 OID 与既有 promisor 集的重叠。观察到变小只支持此次缓解，不证明修复；没有改善也不否定缓存误分类，因最近项仍可能缓存。这里没有发起该试验，也不依赖另一次 fetch 才交付本诊断。

## 6. 来源与范围

详细 URL、blob/commit 身份及读取状态见同 stem 的 `-sources.json`。本次未读凭据、认证进程或环境变量；安全配置查询仅限 `core.multiPackIndex`、`core.deltaBaseCacheLimit`、`fetch.writeCommitGraph`、`fetch.unpackLimit`、`transfer.unpackLimit`、`maintenance.auto`，结果均未显式设置。没有 fetch、git 配置变更、refs 变更、pack 写删、fsck、verify-pack、数学求解或重后端调用。

- [S1] [官方 Git 镜像 v2.51.1 标签](https://chromium.googlesource.com/external/github.com/git/git/+/refs/tags/v2.51.1)
- [S2] [v2.51.1 builtin/index-pack.c](https://chromium.googlesource.com/external/github.com/git/git/+/refs/tags/v2.51.1/builtin/index-pack.c)
- [S3] [v2.51.1 builtin/pack-objects.c](https://chromium.googlesource.com/external/github.com/git/git/+/refs/tags/v2.51.1/builtin/pack-objects.c)
- [S4] [官方修复 7a4bd1b836c7437dfb8ff3650096750b98a6b3e4](https://code.googlesource.com/git/+/7a4bd1b836c7437dfb8ff3650096750b98a6b3e4) 与[完整 diff](https://code.googlesource.com/git/+/7a4bd1b836c7437dfb8ff3650096750b98a6b3e4%5E!/)
- [S5] [v2.51.0-rc0 packfile.c](https://kernel.googlesource.com/pub/scm/git/git/+/refs/tags/v2.51.0-rc0/packfile.c)
- [S6] [修复父提交的 packfile.c](https://code.googlesource.com/git/+/123e8186a72cd71863668b6acb23a2faa30e6968/packfile.c)
- [S7] [官方 git-config 2.51.1](https://git-scm.com/docs/git-config/2.51.1)
