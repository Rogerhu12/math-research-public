# TC 原输入恢复修复：实际 Git 来源与原 nodal Hermite 重物化

2026-11-27；visible-exact-astra-fb31ed6-20261127 / trial_restore。

**状态：输入恢复实现；不是新科学目标完成记录。** 原失败
45806282910/1、原 manifest 和原空 scientific/targets 列表不变。

## 原失败与修正

`body_regular_nodal_resume_20261114/response-full.json` 是完整原索引，
但该目录下的十四个 `response-full-part*.npz.gz` 没有提交在原历史
`7c130fb94528de8f003a43e7049fb42768a64eec`。因此不能再将索引中列出的
文件名直接当作存在的 Git 恢复地址。

同一历史提交保存了三个原 response nodal answer 字节块。已有原程序
`fourfold_codazzi_regular_trial_from_fixed_nodes.py` 从这些字节恢复
`answer-0.npy`，调用原 `incremental_spline`，并核对原完整 cubic 和每个
完整原分片的 SHA-256。原程序及其全部 55 个本地 import 来源均沿用
原 body manifest 的 SHA；原对象、q-vector、waist row 和完整 finite
native 也不改变。

所需原身份为：

- 原完整 nodal answer：`5d69eabc45757f91a4739c58114310c5534ac1a84e01e54233188dfffa567b1c`。
- 原完整 cubic：`3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402`。
- 原物理完整索引：`ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6`。
- 连续修复方向定义：`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。

这一步是必要的输入数值重物化，明确计为一个独立子进程和一次旧重建
程序调用。它不重做 QR、不重算原残差或范数，不增加 TC 已完成目标。
原完整 cubic 或任一原分片不匹配时，TC 数学子进程不启动。全部数组
仅留在 Actions 临时目录。

## 四十个原 intrinsic row 对象直接由 Git 恢复

六个原独立 native 与另外三十四个原完整自然分片都存在于同一历史
提交；后者位于
`notes/correlated_body_ci/run-43583838026-1-rows*/native/`。
新 metadata helper 对照已完成 D 输入清单的四十个原 SHA，读取并
验证每一份真实 Git 对象，写入具体路径、Git blob、字节数和 SHA。
worker 因而不再依赖八个旧 Actions archive，也不重做任何旧积分。
原 owner 仍再次核对完整 7721 行 canonical payload、6143 接口和
原自然分片覆盖，原输入没有缩小。

## 新入口与不变范围

新 helper：`scripts/fourfold_codazzi_true_root_trial_restore.py`。
原 worker 只修改输入恢复分支；原 TC 数学 owner、proposal、残差公式、
真根区间、两 mean、全 288 Fourier 输出和三项完整自然目标均未修改。
generator 写新的 `2026-11-27-true-root-trial-rematerialized-inputs.json`
及独立 workflow，保留原失败入口。

输入重物化使用原 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、
python-flint 0.9.0、SymPy 1.14.0、mpmath 1.3.0；TC 数学 owner 仍只
声明其原 NumPy/python-flint runtime。新增安装不改变原数学参数。

执行顺序为实际原输入字节恢复、四十个原 row 恢复、必要的独立
Hermite 重物化、原 owner 的完整 preflight，然后才登记并执行尚未
完成的 TC 目标。恢复失败会保存真实重建 outcome；不会将输入准备
成功解释为新残差球、真正 PDE 列或全有限块逆。SC/P224 真列误差、
完整 finite/mean/nu Schur 和最终闭等距族仍是独立待解项。
