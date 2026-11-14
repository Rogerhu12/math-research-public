# C² 流式比较的 batch 元数据补记

审查者：`/root/tail_theory`，2026-11-09。

冻结适配层 `db6f-prefix-tail-c2-stream.py`（SHA256 `8da5bb581fbe45bbec10dde3cabce9d755cfdc43fb4d5a334aff90713828c4ea`）的默认 `--batch` 为 64，而它调用的原比较器再次解析命令行时，原默认值是 128。因此，若未来运行完全省略 `--batch`，实际 batch 会是 128，适配层记录却会是 64。

**本次 critical 两档真实运行不受影响。** 作者确认实际命令显式传入 `--batch 64`，已保存的复跑命令 `db6f-prefix-tail-m12-critical-c2.md` 同样显式传入该参数。两次解析都得到 64，当前报告的元数据真实一致。

这个默认值差异不改变逐盒数学公式、精确共同分割、向外误差界或已完成的存储/轴变换审查；它影响的是将来省略参数时的批大小记录与内存预估。当前冻结源和已运行报告均保留不改。未来若需要无显式参数的入口，应另存修订版统一默认值或显式传递已解析的 batch。

作者随后另存 `db6f-prefix-tail-c2-stream-v2.py`，SHA256 `eebc6b4e1c204840f3339cdddc56c88bde7a8894c230f9caa432359d3d47cf6e`。审查者已独立核全文 diff：唯一差异是 wrapper 的默认 batch 从 64 改成 128，现与 backend 一致；显式参数的行为完全不变。这一源码修复静态审查 PASS，没有重新运行数值，也未改变旧版或当前已审输出。
