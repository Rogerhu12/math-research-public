# R141 D 边界提升：零数学前缀后的线程环境恢复

2026-11-20，维护会话 `visible-exact-astra-ac637-20261120`。

## 首次实际结果

原公开运行 [44742799448/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44742799448)
在原科学 owner 的声明线程环境检查退出。完整记录仍在
`reference_boundary_lifts_ci/run-44742799448-1/`：

| 原完整文件 | bytes | SHA256 |
| --- | ---: | --- |
| actual-scientific-conclusion.json | 51083 | eaeb74c5eb82ceb5dbd054f3ae00eb372d43f8eacc53fafa3405f5d156965af1 |
| execution.json | 58697 | 7491a9f2372fa47c038590c58cf05fe70475f0678f855ca6cdd01863f9e37368 |
| report.md | 528 | d245d2a88f60e2fea08b0a70449bf8a4a6fabfc2c0a9d95974e50077c8fb4366 |

实际 source checkout 为 `57c9c4679d32e207188c7a1ca5f0fdc4103b5ee4`。
19 个完整只读准入门都通过；失败为 `ValueError: declared thread settings`。
数学时长 0.0 秒，child 时长 8.31568457 秒、返回码 1。
原定义、参考低模剖面、新 Gram panel、完成目标、保存科学球全部为 0；
旧 producer/旧成功 target/centre/family/Gf/GH/低逆/旧50图调用全部为 0。
保留这个失败及原 consumed marker，不把它当作完成的数学或可恢复科学前缀。

原因是原 workflow 未设 `OPENBLAS_NUM_THREADS`、`OMP_NUM_THREADS`、
`MKL_NUM_THREADS`；原 owner 要求三个值都为字符串 `1`。
共享 worker 不会代替这个 workflow 设置线程。

## 独立恢复入口

恢复只执行原先尚未开始的两个目标、十条完整结果球。
原 79 个 current 输入逐 bytes/SHA/git-blob 保持不变，
含原 owner、math、generator、共享 worker 和全部原证明；
21 项 historical identity、参数、scientific module binding、25 门、39 字段、
参考定义/剖面/Gram 分割、时限和完整 scope 均保持不变。

新增三项 current 输入是恢复 metadata generator 与上述两个完整失败 JSON。
新清单共 82 项，只有原 operation 的 consumed-marker 路径改为独立 v2。
workflow 只换 concurrency、新清单路径/SHA，以及明确的三个线程环境变量。
旧 v1 marker 与零前缀记录继续保留。没有自动重跑授权。

| 新文件 | bytes | SHA256 |
| --- | ---: | --- |
| make_reference_boundary_lift_recovery_manifest.py | 13171 | 7e139255e5a540706732211338d72df441c25f871aae407a7e7ccd455097aca7 |
| 2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json | 72957 | 38ff0e8f5f3ca03a752a5836ec43baa72a31aefcf29a2d3e4421d0d399323f6d |
| fourfold-codazzi-reference-boundary-lifts-public.yml | 1790 | 953065511919e2c1f0b4a94a49345098f180a0bef31b756afed11e16809b76db |

恢复 generator 读取原 70121B 清单并验证其 SHA
`9c4f0afe00aa1a5c1b3adb0f57df15d0773c67b8b163894eb06071b7e08f95f8`；
逐件验证原79输入、完整失败身份与所有零计数。
从原已 pin 的 generator AST 提取整段旧 workflow literal，
重建并核原 workflow SHA，再作上述有限替换。
因此现 workflow 更新后仍能逐字重建恢复清单与入口；未导入或执行科学模块。

root 已核全部82 current bytes/SHA/blob、原21 historical 整对象、
operation 唯一差异，以及 metadata 重建的逐字相等。
全部后继数值仍只在本公开仓库 Actions 运行。

## 未付结论

原 [D 边界证明](../results/R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md)
的 mean、真 root、Theta、同模 signed Gram、193 observations 与全域资格不变。
此恢复记录不授任何新数值界、低逆、内部反馈、
真正97+96物理外行、原 finite-rho、七 ports、两 RHS 或最终精确族。

