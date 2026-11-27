# 原 cubic / 14 片在真实 SkylakeX 上恢复，TCX 仅继续原缺域

2026-11-27；visible-exact-astra-fb31ed6-20261127 / trial_restore。

## 已完成的必要输入身份

[输入-only run45924740082/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45924740082)
在 2026-11-27 01:51:09.865894 UTC 成功结束。完整 actual 为
13467 字节，SHA-256
`e60132d11b0fec9ef70257d5237f05b52b59c1037446764c78f7ed7665803d3f`；
完整 execution 为 11662 字节，SHA-256
`95ba072a52abadbb9047faf2820dcc7437b8d5cf901ed59e29d36abea694f102`。
whole actual 的 `complete=proved=true`、`failure=null`，并非仅运行
状态 success。它所绑定的完整 ubuntu24 manifest 为 90787 字节，
SHA `0789f442e26f02644f7e958d9fa11db249a4063a6946c3b57c3f3f5f54bb62cd`。

实际 CPU 是 Intel Xeon 6975P-C，内核 flags 与 NumPy 都报告所需
AVX512 能力。default 只读 probe 与显式 probe 均记录
`Core: SkylakeX`。仅显式 SkylakeX 启动了一次必要原 producer；
Cooperlake 没有执行。该原 producer 用 23.67157865 秒完成：

| 原完整对象 | 本次与原值共同的 SHA-256 |
|---|---|
| nodal answer | `5d69eabc45757f91a4739c58114310c5534ac1a84e01e54233188dfffa567b1c` |
| 6144-piece cubic | `3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402` |
| full index | `ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6` |
| nonmean index | `e110982c46285b2e5141933813811a1c97d3c43583e3e553678b24a35dbb914f` |

原 producer 自身逐一核 full/nonmean 全部 shard，外层还将 TC 所需的
全部 14 片完整字节数与 SHA 逐一核对并保存完整 receipts。数学对象
没有换成相近的重建。它未重做原 QR、norm 或 residual，未启动 TC
owner；`TC_scientific_children=0`、`new_TC_integrated_cells=0`。

## 最小实施性后继

新 `fourfold_codazzi_true_root_verified_runtime_restore.py` 整体 pin
原 restoration helper，只替换必要 carrier 子进程的 CORETYPE
选择与真实 runtime receipt。它先完整准入上述 actual、execution、
manifest，并核与原 nodal recipe 完全相同。原历史 run43583838026
的 `original_reconstruction_OPENBLAS_CORETYPE=unset` 保持事实原值；
另列 `verified_runtime` 说明本次已证 SkylakeX，不能把新运行伪写成
unset。新实际 execution 的 `reconstruction_OPENBLAS_CORETYPE`
诚实写 SkylakeX。

在每个实际分配的 runner 上，先只读 CPU flags，只有具备
AVX512F/DQ/BW/VL 才允许导入显式 core 并调用原 producer。随后记录
NumPy features 和实际 core，仍核完整 cubic / indexes / 14 片身份。
没有能力就保存零 producer 的真实失败，不调用已失败 Haswell。
`ubuntu-24.04` 是明确 runner 输入；它本身不构成 CPU 型号保证。

TCX owner、worker、完整科学源码、参数、真实根和全部 7724-cell
分割均保持原 whole SHA。新数学 proposal 仍 Haswell、原六线程变量
均为1。完整原 TC run45889161044 的 signed matrices 和前 992
完整单元直接继承；原四份 trial 数组各自全 SHA 核完一次，才由最多
三个进程继续固定互斥缺域。每格全部96列、五类 source、两侧、所有
ordinary measure 和原 source 尾都保留，已接受单元没有重积分。

当前仍未证明完整 TC negative / positive sources。此入口只是解除
阻断其新缺域的必要输入恢复；不得从载体恢复推出真 PDE 列、有限
逆、physical 58/224 准入或 full Schur。若本批只完成一部分，后继
metadata qualifier 必须显式承认上述真实 SkylakeX receipt，同时
继续核原全部 SHA；不能把它改写成原历史 unset 运行。
