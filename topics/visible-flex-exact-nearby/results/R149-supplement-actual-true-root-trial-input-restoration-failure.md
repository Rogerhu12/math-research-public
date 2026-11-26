# R149 补篇：真根连续试列首入口的输入恢复失败及完整证据

2026-11-26，visible-exact-astra-198c63d-20261126。

## 实际结果

[公开 Actions 45806282910/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45806282910)，job139862303902，在2026-11-26 10:59:20 UTC恢复历史输入时失败。事件提交与实际入口checkout均为 `7ce1007b7df3d72919e0ec77312aa6f697848cb5`。

完整 [execution](../notes/true_root_trial_residual_ci/run-45806282910-1/execution.json) 为5169B，Git blob `fe9146919336606026c3a80bd907687d2d702b30`，SHA256 `d62f6aaddce361e2c426b32e18c6f01490548d0c442165dbe40e11d3ddedfd0e`。结果保存提交为 `64473529729f90cf3bf85a4cc23eec674da0e60c`。根逐字段读取了整件，不依据简略日志补造状态。

| 字段 | 实际值 |
|---|---|
| complete | false |
| scientific_children | 0 |
| actual_child_returncode | null |
| scientific_files | [] |
| completed_natural_targets | [] |
| historical_restoration | {} |
| original_row_restoration | {} |
| new_arrays_published / new_artifacts / new_Releases | 0 / 0 / 0 |

因此没有产生任何新的矩阵、残差球、PDE列或可恢复科学前缀。本次失败不证明数学门失败，也没有旧科学重算。

## 准确失败位置

worker在 `restore_history()` 调用 `checked_bytes`，用Git验证下列地址：

```
7c130fb94528de8f003a43e7049fb42768a64eec:topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part000.npz.gz
```

Git实际返回该路径不存在。原 `response-full.json` 索引的存在和其14个分片的已存SHA，不构成这些分片已提交在该目录的证据。首manifest把索引所列文件误当成这个历史目录可直接恢复的对象，执行器正确拒绝了这一地址。

首入口说明中“27历史全核”须据此限定：当时完成的是manifest字段、原索引和定义的一致性检查，没有完成27个实际历史地址的逐项存在性检查。不能将那次静态一致性检查冒充本次实际恢复成功。失败execution中的空恢复记录保持原样。

## 已完成的实际入口检查

78个当前UTF8输入在科学启动前整件核验，其receipt SHA256为 `0a9fb622236c13b581c4d086ffc8fea1db04e16778ba67757c76e7300cc6bf95`。原manifest为40412B，SHA256 `948e8e3775b4a396d60e05c298f5f6c99c1f9a3ce7795de646bf3c7afa577169`。这两项不修复上述历史路径错误。

worker进行了两次pull/README差异检查，均无规则差异，完整receipt链SHA256 `6bcaecfee4eb6cbdf220651c42efc6b9549d13e91efaa2c1ff8a6570a40ef648`。入口完整topic字节数199048888B。所有这些值保留在原execution中。

## 后继的范围

下一次入口必须先核实每个原输入的真实恢复来源。若原分片没有现存完整副本，允许使用仍存在的原三份nodal answer及已固定原Hermite定义，重物化科学输入载体；必须核对原whole answer、完整cubic和每个旧分片的原SHA，不得重新求QR解、改变Z定义或重新计算任何旧残差/范数目标。

这种步骤明确属于必要输入载体重物化，不能称为纯字节复制，也不能藏进“旧科学0”的计数。其独立子进程、完整输入与输出哈希必须真实登记；数学owner仍只执行尚未开始的三项TC新目标。恢复成功之前不得预登记任何科学完成目标。

原失败run、首manifest、失败状态和上述空科学列表均永久保持。后继是修正真实输入来源后的新显式入口，不把本次失败改成成功。三项TC目标、584球、真根、两mean、完整有符号矩阵和全残差域不减；真PDE误差仍另等P224与SC，完整finite/mean/ν Schur及最终闭等距族仍未完成。
