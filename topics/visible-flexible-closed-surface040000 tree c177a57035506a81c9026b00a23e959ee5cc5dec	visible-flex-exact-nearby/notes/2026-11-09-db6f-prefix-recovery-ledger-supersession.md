# 09:32 恢复清单的活动 metadata 引用更替

状态：**数据来源说明；不改变任何恢复状态或数值结论。** 作者 `/root/coupled_prefix`，2026-11-09。

旧 `2026-11-09-db6f-prefix-live-recovery-snapshots-20261109T093205Z.json` 保存了两个真实原子 iteration checkpoint 的只读副本，同时记录了当时活动 `-reproduction.json` 的 hash。两个只读 CP 本体均未改动，现重新核对：

| 恢复副本 | SHA256 | 字节 |
| --- | --- | ---: |
| M15 call001 / iteration007 | `bd7ebfeab571198b50c909f5d614490de36ffd007846fcf754fd569284cda11c` | 262687 |
| M14/N512 call001 / iteration001 | `41f7576ba4cd659e6781a08f908a27265c425134428d534bdaa0369dabd95d5e` | 245076 |

两者仍保留显式 UNCONVERGED scope，不能用随后独立完成的响应反向重标它们。

## 发生变化的一个引用

M14/N512 当时尚在运行，其 `2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14-reproduction.json` 在完成后由原 driver 补写完成字段。旧清单保存的活动阶段 hash 是

`f3cf229e7896ada319fee9277dd9f7684cd02acef251777ef997920f7d7db38f`。

现已关闭且完整的该文件 hash 为

`0f5ded3b774e81d1e9d49e8901609672c08348c15a610b2ae4eb37c0dbda8655`。

原 driver `db6f-prefix-freeze-refine.py`（SHA256 `ad2bc1113795446f6be86d4f6efb8482967a05beaf986a233599733e1395cc7c`）在启动前保存命令/输入/源码绑定，运行结束后在同一文件补入 `exit_code`、`wall_seconds`、`success`、`error`、`actual_amplitude` 和 `amplitude_difference`。这类运行状态 metadata 并非运行期间不可变输入，旧 ledger 不应被当作其永久冻结副本。

只读搜索当前工作树、发布工作树的同名路径及本地 Git 全历史，没有找到以旧 hash 保存的历史文件。没有伪造或写出一个声称来自当时的旧文件。另在内存中移除当前 metadata 的上述完成字段，并按原 driver 的 JSON 编码重算 hash，得到的确是旧 `f3cf229e...`；这仅核对更替涉及这些完成字段，不冒充保存了历史文件。

## 现行绑定与旧清单的范围

当前发布和复算应采用已关闭的完整 `-reproduction.json`，由 `2026-11-09-db6f-prefix-m14q512-m15failed-publication.json` 绑定。该完整清单的 SHA256 是 `3aada1964b73cc92cc4860c97c46ccdda4cbf41988b4e6f474c6dbe7d8c76f53`。其中如列出旧 recovery ledger，该行只保证 ledger 文件自身的字节和历史记录，不意味着其指向的活动 metadata 路径仍具有旧 hash。

旧 ledger 的两份 CP、两份 tail-config、M15 已关闭 reproduction 和全部已列 loaded-worker 源 hash 均重新核对通过。唯一失效为现行路径绑定的是上述 M14 活动 reproduction 引用；本说明明确替代它，不撤销 CP 本体或其原状态标签。

## 随后的精确 hash 恢复副本

上述首次核查之后，主会话要求把已在内存核对完全匹配旧 hash 的字节实际保存，供后续读取。因此新增只读文件

`2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14-reconstructed-precompletion-reproduction.json`。

这是**事后按已有 SHA256 验证恢复的历史版本**，不是声称找到了原存活副本。构造仅从现完整 metadata 去除上述六个由 driver 结束时添加的字段，保留所有其余键的顺序和值，并使用原 `json.dumps(...,indent=2)+'\n'` 编码。保存后 SHA256 确为旧 ledger 早已记录的 `f3cf229e7896ada319fee9277dd9f7684cd02acef251777ef997920f7d7db38f`。对应来源、当前完整 hash、去除字段、旧 ledger hash 与字节大小另存 `2026-11-09-db6f-prefix-reconstructed-reproduction-provenance.json`。

原 ledger 及当前完整 reproduction 均未改写。现在旧 hash 有这个明确标为重构的可读取文件；现行复算结果仍以完整已关闭的 reproduction 为准。
