# R787：runner 失联与真实 518 位断点恢复

本记录只处理实际运行丢失及其恢复，不登记不存在的新数学断点，也不重复已完成的 518 位全格结论。

## 1. 实际结束证据

[公开运行 43766834509](https://github.com/Rogerhu12/math-research-public/actions/runs/43766834509)的源提交为 `0084d2e067710af828ae071e7850764791e41300`，数学 job 为 `132973847087`。运行在 **2026-11-16 02:49:29 UTC** 结束为 failure；GitHub check-run 的实际注记为托管 runner 与服务器失去联系。注记列举的进程终止、CPU/内存耗尽或网络阻断只是可能原因，现有证据不能指定其中任何一种为事实。

实际 job schema 仍将数学步记为 in_progress，后续输出上传步 pending；job 日志读取返回 404 BlobNotFound。02:54 UTC 再读 artifacts，只有 rules 产物，没有本次数学 manifest、current、history 或 core/run 回执。因此不能把本次结束称为核心 BudgetStop，不能宣称它已经达到某个新位数，也不能以未保存的进行中状态作为续算来源。

唯一 rules artifact 是 `14182522987`，677 B，SHA256 `3e2f8d7211cad357b7a4f5fdc918e47a91b19332561215680944c101a5e9e70c`。它不含数学断点。

## 2. 最近可恢复的真实原断点

仍使用[已登记的 518 位断点](R787-518-digit-checkpoint-and-precision-increment-activation.md)：

| 项目 | 实际值 |
|---|---|
| run / job | `43737413555 / 132883028161` |
| source commit | `4092d1cc4d1156bc24a10ff820fd39c5713e8ad7` |
| artifact | `14181899102` |
| artifact name | `serre-global-R787-original-power5-function-relation-43737413555-1` |
| archive | 451202899 B / `343bee0a0fb5bf8d9143d2dbc8b8d8fc0f0da3649bbb1d94748ef34f19d87249` |
| manifest | 430709 B，1262 件 / `7a22beb22912c1d5c4c56a5faa577a529f6c5dab5bb4ea5251e9cd5c4264ba3f` |
| latest complete lift | `R787-prime-1000000753-dixon-00000518.json.gz` |
| lift bytes / SHA256 | 73180954 B / `4997a05b79ab9e7c7f9286fc483b1f459ff6e23fa18df5344bd8ef0eb80f10f5` |
| history | 120502 B / `07875f05c10549fdbc6eeaf2bdd2071bcc2d74e35695c20698bfb86f634d1eed` |
| expires | 2026-11-16 21:50:48 UTC |

02:58 UTC 的实际 artifact API 仍给 expired=false，并给相同源、字节与 SHA。这里没有重新运行旧 1–518 位、旧模分支或旧全格；失联作业在 518 之后可能做过但未留下可验证输出的工作，不能冒充已完成阶段。

## 3. 恢复请求唯一变化

本次原请求 `R787-public-original-power5-relation-request.json` 的 resume 原样不变，只将运行预算 **300 → 120 分钟**，使正常预算结束及断点上传更早发生。此举不保证托管 runner 不再失联。

- 核心仍为 `R787_original_power5_relation_solver.py`，SHA256 `93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04`。
- wrapper 仍为 `R787_public_original_power5_relation.py`，SHA256 `42157e0d95eb5d9aed28ef828a86dc5e7bec89e806e3e0a92aa0bcb1a36988b6`。
- 原 proof、method、field core、全部 R781/R786 来源、prime 起点及每 8 位严格有理重构不变。核心的数学 configuration/tag 不含运行预算；wrapper 的 continuation 等同性检查也明确只比较原数学字段。预算变化不改旧阶段标签或算术。

恢复仍核真实旧 ZIP、manifest、完整 latest lift 及源绑定，再从下一个未完成位继续。此前 518 全格的 56 个 detU1/56 个新 D 非零结论已闭，不再次激活精度增量格作业。

## 4. 当前边界

准确展开关系尚未恢复。本次恢复不影响正在运行的新清转置作业；primal 的 518 位从未充作 dual 位数。原 A.1、指定高度、全 p 同标签单位与 Serre 主目标均保持 OPEN。
