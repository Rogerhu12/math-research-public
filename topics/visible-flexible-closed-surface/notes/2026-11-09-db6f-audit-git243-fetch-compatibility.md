# 已装 Git 2.43 的临时 fetch 兼容性与范围

状态：已关闭的只读源码及元数据独审。审查者 `/root/independent_geometry`。本次没有执行 fetch，也没有改变 Git 配置、对象、引用、认证、程序或求解状态。机器记录为 `2026-11-09-db6f-audit-git243-fetch-compatibility.json`，SHA-256 `f383993ac6d606943f234aa6b23c7b7b03cdbcaac19e9a99e615075da3247ae4`。

## 结论

下一次原本必需的 fetch，可以在 root 控制下仅把该次可执行程序换成 `/usr/bin/git` 2.43.0，保留原有认证、remote、refspec 和 partial-clone filter，并加 `--no-auto-maintenance`。可另加 `--no-write-commit-graph` 关闭该项可选写入；本次读到 `fetch.writeCommitGraph` 未设置。merge/push 及其他操作无需跟着更换。

这是一项有源码依据、尚未实跑的限定用途缓解：2.43.0 没有后来的本地链接重打包调用链，因此该旧程序不能执行那条新增路径。它不等于已经证明下一次不会生成重复包，也不等于已经排除其他重复对象成因。本次不建议任何缓存或 MIDX 配置试验。

## 精确版本源码

[官方 v2.43.0 标签](https://code.googlesource.com/git/+/refs/tags/v2.43.0/) 的树为 `203ad4fd3f91e9990c72a65d820068d4ccbdac4f`，其 builtin 子树为 `c6fb469640c2c25c475e0363e2fc92d584fbce11`。先前暂不可取的 exact-tag 页面已成功通过目录导航取得，因此此处没有仅凭 rc 版本代替正式版本的缺口。

[该标签的 index-pack.c](https://code.googlesource.com/git/+/refs/tags/v2.43.0/builtin/index-pack.c) 的 blob 为 `dda94a9f46d9a9401c298ee304f57e55db25f217`。全文不含 `repack_local_links`；`--promisor` 分支仍为已解析参数的空操作，接收完成时为收到的包写 promisor 标记，`main` 尾部没有本地链接重打包调用。[同标签的 pack-objects.c](https://code.googlesource.com/git/+/refs/tags/v2.43.0/builtin/pack-objects.c) 也没有后来加入的 `is_not_in_promisor_pack_obj` 判别函数。

[Jonathan Tan 于 2024-11-01 发出的原始补丁](https://marc.info/?l=git&m=173049178601320&w=2) 明确添加这两部分。补丁还说明它们的保护作用：新收到的 promisor 对象可能引用已有本地对象，后者可能只经 promisor 对象可达；若未妥善保留，后续垃圾回收可能丢弃它们。因此不能把绕过该新路径理解为对所有 Git 操作都更安全。

这里证明的是旧版本没有这条新增路径，并没有证明旧版本不存在 delta-base 缓存或一般的 `OI_DBCACHED` 枚举。先前对 Git 2.51.1 的根因诊断与本次限定用途判断应分别理解。

## 实际安装及仓库读取

三组只读命令均实际退出 0，工具收据分别为 `a9d2ec`、`29ce17`、`888a17`。完整选择项和哈希在机器记录中。

| 项目 | 实际结果 |
| --- | --- |
| 现用程序 | `/usr/local/bin/git`，2.51.1 |
| 可临时使用程序 | `/usr/bin/git`，2.43.0 |
| 2.43 的有效 helper 路径 | `/usr/lib/git-core` |
| 仓库格式 | `core.repositoryformatversion=1`，SHA-1 |
| 唯一 extension 键 | `extensions.worktreeConfig=true` |
| 两版本的工作树/裸仓库读取 | 均为 `true` / `false`，无错误 |
| 两版本读取的 refs | 同一快照 11 条，输出逐字节相同 |

两份 refs 输出的 SHA-256 均为 `2ecc86bdfd85d6a581aef3780b91abead107fdc8839813c4f93226039a7e3f7c`。这个同一时点的读取没有证明后续 refs 不会移动。

`/usr/bin/git`、`/usr/lib/git-core/git`、`/usr/lib/git-core/git-index-pack` 三件实际程序均为 4,066,232 字节，SHA-256 均为 `2a8c18fbf43da9f692d75474c72bea9dfd796c260b0f3dfe456376abc3bbd668`；helper 的 `git --version` 也实际报告 2.43.0。因此已经核实此次显式程序路径所对应的常规 Git/index-pack helper，并非只看一个外层版本字符串。

`extensions.objectFormat`、`extensions.compatObjectFormat`、`extensions.refStorage` 未设置。虽然 `extensions.partialClone` 也未设置，这不能据以否认仓库是 partial clone：本次没有读取 remote 的 promisor/filter 配置。此处只给出实际通过的格式和引用读取门，不宣称已验证全部对象、MIDX 下所有操作或全部新版本功能。

## 使用边界与后验观察

[官方 2.43 fetch 文档](https://git-scm.com/docs/git-fetch/2.43.0.html) 提供 `--no-auto-maintenance` 和 `--no-write-commit-graph`。前者是此次限定调用的重要边界，因为旧版本缺少上述保护性本地链接处理。

root 的计划为：仅在原本需要 fetch 时作该次显式程序选择；继续完整 OID 保留及 promisor/ordinary 分区维护；不执行会仅依可达性丢弃对象的 GC 或普通 repack。这个范围与本审查一致。后续真实调用的退出状态、新包字节/索引及旧 OID 保留，才是减包效果的运行证据。本次没有安排额外试 fetch，也没有提出改变既有认证、filter、refs 或 shell 函数。

本报告不参与数学优化，不改变最终 M15 独立全流程重跑的分工。
