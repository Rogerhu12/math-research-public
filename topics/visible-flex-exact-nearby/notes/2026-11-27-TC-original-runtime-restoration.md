# TC 必要输入重建：恢复原成功运行的容器与 BLAS 选择

2026-11-27；visible-exact-astra-fb31ed6-20261127 / trial_restore。

## 新实际失败没有改变 Z

[run45881752490/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45881752490)
已实际完成 137 个当前输入核验、18 个原历史对象恢复及全部 40 个原
intrinsic row 对象恢复。独立的必要 nodal 重建进程运行 35.127590682 秒后
被完整 cubic SHA 门拒绝：

- 期望原 cubic：`3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402`。
- 本次实际 cubic：`d48ecd2b62b0dab7f42ab130e9da6b6d177c26aa4da63ffb438cdc52a7fa24a0`。
- 实际重建报告：895 字节，SHA-256 `55531625b8f9433aa2132529c4f7235ae0acf4b322c106119a1bb3518d4cd306`。

数学 owner 没有启动，`scientific_children=0`，完整目标和科学文件列表
均为空；原 QR 没有重做。本次真实失败由提交
`ab61131aa09e8789ed57f5f2bdeabb159af8444e` 保存，不能改成成功。
新 cubic 没有被接纳为原 Z。

## 找到的实际环境差异

读取原成功 [run43583838026/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43583838026)
的 prepare job132414020963 日志，以及原 workflow 提交
`596f9681e978c4ff5f6641cba6ffe2a6a3f91a73`，可核实：

1. 原重建用 Docker `python:3.12.14-trixie`；该实际运行拉取的镜像 digest
   是 `sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7`。
2. 原 workflow 固定 BLAS/OMP 单线程，但没有设置 `OPENBLAS_CORETYPE`。
3. run45881752490 使用宿主 setup-python，并继承 TC 新 proposal 的
   `OPENBLAS_CORETYPE=Haswell`。相同 Python 与包版本并不消除这些
   原浮点载体重建环境差异。

这尚不证明哪一项差异导致 SHA 不匹配。后继实际执行仍必须通过原
完整 cubic 与十四个分片 SHA，才算恢复成功。

对原 nodal 目录、`current_root_phase_response_20261114` 目录的精确
`response-full-part000.npz.gz` 路径，以及 nodal 的 `trial-cubic.npy`
路径，已作 `git log --all -- <path>` 元数据查询，均无历史记录；
没有找到可绕过必要重物化的原完整 Git 载体。

## 后继修正

新 workflow 固定上述原不可变 Docker 镜像，不再调用宿主
`actions/setup-python`。必要 nodal 重建子进程显式移除
`OPENBLAS_CORETYPE`，保留原单线程及原全部软件版本；记录实际平台、
libc 与明确的 core 选择。独立 TC 数学 owner 的 proposal 仍保留其
原已声明 Haswell 选择，不修改数学参数或计算公式。

新入口是 `2026-11-27-true-root-trial-original-runtime-inputs.json` 和
独立 `fourfold-codazzi-true-root-trials-original-runtime-public.yml`。
前两次失败入口、原字节身份和未完成状态不改写。不放宽任何 SHA 门，
不把新浮点重建当作原连续方向；若仍不匹配，继续依据实际结果定位
输入重建环境，尚未完成的 TC 科学目标保持未启动。

## 原容器第一次启动与挂载目录修正

[run45883126797/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45883126797)
的 job140127118048 于 2026-11-26 19:22:53 UTC 停在 worker 首条
`git rev-parse HEAD`。不可变容器拉取、Git 安装、checkout 和全部原版本
Python 包安装均成功；实际错误为 Git 对容器挂载 checkout 的
`detected dubious ownership`。尚未恢复 nodal 输入、运行重物化或进入
任何数学目标，不能把这次结果归因于 cubic SHA 或 BLAS。

checkout action 的 safe.directory 使用其临时 global config，后续容器
shell 没有承继该条配置。workflow 和 generator 现在在 checkout 后为
明确的 `$GITHUB_WORKSPACE` 单路径执行
`git config --global --add safe.directory "$GITHUB_WORKSPACE"`；不用
通配或更换仓库。完整 cubic/分片 SHA 和数学 owner 均保持不变；新
`original-runtime-mounted` manifest 只重新 pin 已修正 generator 与
对应具体入口，保留失败时的原 manifest/workflow。挂载修正第一次
必要恢复仍须通过全部原 SHA 门后才允许调用数学 owner。
