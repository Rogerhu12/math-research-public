# TCX 原载体零科学失败与两种未匹配调度的输入恢复

2026-11-27；visible-exact-astra-fb31ed6-20261127 / trial_restore。

## 实际边界

原 [TC run45889161044/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45889161044)
在 2026-11-27 00:54:07 UTC 因完整有限 trial 的既定 wall budget 结束。
其 signed matrices 已完整，7724 个认证单元中的前 992 个完整单元已保存。
完整最终 prefix SHA 是
`35aab5a3ec53ee784b271536ab2ef79f06bb4b3d8e5b3d00ae545d6f31ba9cfa`。
该前缀包含全部 96 列、全部规定 source；本次输入诊断不调用其积分器。

唯一后继 [TCX run45920124552/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45920124552)
在 01:03:44 UTC 结束，完整 execution 是
12583 字节，SHA-256
`06ad7cf47fa5cfdb91093a7470eaaba813213d9137d5e0f23358b149f7135efb`。
它在必要的原 nodal-to-Hermite 恢复时失败：`scientific_children=0`、
`actual_child_returncode=null`，科学文件与完成目标列表均为空。
原 992 单元没有重复，TCX 三个互斥积分子进程均未启动。

完整原 cubic 应为
`3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402`，
此次得到
`d48ecd2b62b0dab7f42ab130e9da6b6d177c26aa4da63ffb438cdc52a7fa24a0`。
同一失败 SHA 已在
[原 runtime 记录](2026-11-27-TC-original-runtime-restoration.md)
登记于 run45881752490 的 Haswell 重物化。该完整失败证据直接保留；
不为了重现它再跑一次 Haswell 或 default 重物化。

本次 TCX 使用原不可变 Python 容器、原全包版本、全部单线程，并在
必要重物化子进程中取消 CORETYPE；它仍未匹配，故“相同容器即可恢复”
不成为新保证。原成功 TC 与失败 TCX 的公开 job 日志所记 runner image
版本分别为 `20261122.9.1` 与 `20261116.202.1`。两者日志未记录 CPU
型号或实际 BLAS core，不能从 region 名称猜测硬件或因果。

## 独立输入诊断的准确范围

新 owner `fourfold_codazzi_original_nodal_runtime_identification.py` 先在
公开 Actions 中只读记录 `/proc/cpuinfo` 首个 processor 的型号与 flags、
NumPy `__cpu_features__` / `show_runtime()`、实际 `OPENBLAS_VERBOSE=2`
core 输出、Python/包版本及 libc。default 只作这次元数据探测，不运行
nodal producer。然后只允许 `SkylakeX` 和 `Cooperlake` 两个此前尚未
匹配的明确候选；实际 CPU 没有所需 AVX512F/DQ/BW/VL 时记录跳过。
若明确调度的实际 core 回退到已失败 Haswell，则复用原失败 whole
receipt，并跳过该重物化。每种真正未匹配调度至多一次；每次单独保存
原 producer 完整小报告、日志整体字节数与 SHA、实际 core 和退出状态。

唯一允许执行的数值程序仍是原完整
`fourfold_codazzi_regular_trial_from_fixed_nodes.py`
（SHA `b1241673f837a8e775ddc99dad302ecf1c310580943ae41fd4ada7cf005a187c`）。
它拼回原三份 nodal answer，核原 full answer SHA，再调用原完整
`incremental_spline` 重物化原一侧导数和 6144 个 cubic pieces。
原代码、原模型、原历史 native 描述、原 candidate 与参数均不改。
它不调用旧 QR，不重算旧 residual 或 norm 目标。

接受条件仍是原 full answer、完整 cubic、原 full/nonmean index 和
其全部 shard 身份均通过原 producer 自身验证；外层另逐一核验 TC
所需全部 14 片的完整字节数和 SHA。不同 cubic 即使数值很接近也失败。
成功只证明本次原有限载体的身份恢复，不证明 TC 残差、真 PDE 列、
任何逆或 full Schur。

新 public worker 保留既成 worker 的整个 Git 输入恢复、容量、
每次 pull 后两 README diff 检查及非快进后立即 rebase/push 循环，
明确移除原 TC scientific pipeline、40 row 恢复、proposal、owner
preflight 和积分调用。全部 current inputs 在私有临时树中核验并
物化，周期 pull 不会因 sparse checkout 删除运行所需输入。
原 TCX whole manifest 与完整失败 execution 均为新 manifest 的
完整输入，原 992 前缀及 signed matrix 的身份仍由该 whole manifest
绑定。小诊断结果、真实失败或恢复 receipt 会原样公开；大数组仅临时。

本项没有自动启动 TC 的出口。只有真正恢复原完整载体后，后继 TCX
入口才可明确固定已验证调度，并继续原 992 之外的互斥缺域。
