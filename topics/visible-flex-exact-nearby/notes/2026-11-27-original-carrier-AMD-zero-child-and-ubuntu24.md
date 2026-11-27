# 原载体诊断的实际 AMD 零进程结果与明确 ubuntu24 后继

2026-11-27；visible-exact-astra-fb31ed6-20261127 / trial_restore。

[run45923136710/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45923136710)
已经真实结束。完整 actual 为 5187 字节、SHA-256
`c99fc9f96ed753e6c493d44d55906b97450f0fcbfe584dda5b7ec9ce1e6d5c29`；
完整 execution 为 12330 字节、SHA-256
`e6f8e2c9a8aae7a483dc8698ad877a757462d043ae5d2175b7299a4f503818be`。
它读到真实 CPU `AMD EPYC 7763 64-Core Processor`，vendor
`AuthenticAMD`，family25/model1，实际 BLAS `Core: Haswell`。
NumPy 报告 AVX/AVX2/FMA3 可用，但 AVX512 全不可用；内核 flags
也没有 AVX512F/DQ/BW/VL。因此两个声明候选 SkylakeX、Cooperlake
都如实跳过，`necessary_input_reconstruction_children=0`；没有再跑
Haswell，没有产生新的 cubic，也没有 TC scientific child 或积分单元。

这不是两种声明算法的 SHA 失败，它们仍未在有能力的硬件上执行。
原 TC 992 个完整单元、完整 signed matrices、原 cubic 与全部14片
身份继续保留。失败 actual 与 execution 均作为下一入口的完整输入。

[GitHub 官方标准 runner 文档](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)
列出公开仓库可用的免费 x64 `ubuntu-22.04`、`ubuntu-24.04` 和
`ubuntu-26.04` 标签；该资源表不承诺具体 CPU 厂商或 AVX512。
故后继只固定一个尚未采用的 `ubuntu-24.04` 标签，不把它称为 Intel
或 AVX512 保证，也不按 region 猜型号。

新独立入口复用已经冻结的输入-only owner/worker。进入后仍先实际
读取 CPU、NumPy dispatch 和 BLAS core；没有 AVX512 能力就保存新的
零进程实际结果，不调用 producer。实际具备能力时才执行两种尚未
实际执行的明确 core，每种至多一次，且只以完整原 cubic、原 full /
nonmean index 和全14片 SHA 通过作为恢复成功。它不会自动重试，
不会滚动申请随机 runner，也不会启动 TC。此前 default / Haswell
已失败完整证据直接复用，原科学前缀不动。

新 metadata-only generator 先核上述两个 whole 结果确为同一次已
结束、无 producer、无科学目标的真实执行，再生成唯一 ubuntu24
manifest/workflow。全部旧输入映射及容量 / README / 非快进处理
继续继承原完整发布器。若成功，后继 TCX 仍须单独准入实际恢复
receipt 与原 992 前缀后，才能执行此前未完成的互斥缺域。
