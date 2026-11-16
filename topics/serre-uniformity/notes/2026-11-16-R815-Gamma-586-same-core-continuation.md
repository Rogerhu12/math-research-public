# R815：原 Γ 的 586 素数断点与同核续算

日期：2026-11-16。本文只登记实际已结束产物及同核恢复请求，不新增数学计算或成功结论。

## 实际结束与未完成边界

公开 run `43853995004` / job `133253466821` / source `c1b3bfb1a0deae3c4b75da514ffcbb8530ae59d3` 已结束。原 wrapper 的数学步骤和一日 checkpoint 上传完成，最终完整成功要求没有通过。

真实 `core-receipt.json` 为 549 B，SHA256 `b1c43fd3e7ded69a59bfdd1ff726f6c5f5cc36097eb6982a5d4c245831212257`，明确记录 `BudgetStop: Complete original operator stages and latest CRT states retained.`。真实 `run-receipt.json` 为 591 B，SHA256 `3ab5a912be25fe08d5ece94783b5a29477df94c3bb9c78f4d7f144a2740e1972`，记录退出码 1、`complete=false`、`error=null`，结束时间 `2026-11-16T16:07:58.496714+00:00`。不能把 wrapper 的 `error=null` 或数学步骤的工作流状态读成 Γ 已完成。

该产物没有最终完整证书。原已成 $M_g$ 的 `R815-target-g-component-00-certified-multiplier-index.json.gz` 本次原字节继续存在：7,469 B / `f27130f00ea3b2cd17284e531eb8f6145b37200c49e7002baf0b7cd053281033`，实际 `complete=true`、`actual_CRT_prime_count=696`。本次续算不重建它，不独立构造 $M_h$。

## 最新真实 Γ current

最后完整回执是 `R815-target-Gamma-component-00-CRT-step-000586-receipt.json.gz`，3,964 B / `8aaa4ccfd2a8d877ced307c0f0d2b2c098ccdf3ce0eee14b367033588ba91497`。其原字段为：

| 项目 | 实际值 |
|---|---|
| 已消费素数数目 | 586 |
| 最后素数 | 1000012019 |
| 最后素数序号 | 585 |
| CRT 模数位数 | 17520 |
| 当前完整文件 | `R815-target-Gamma-component-00-CRT-current.json.gz` |
| 当前完整文件字节数 | 579860820 |
| 当前完整文件 SHA256 | `d361a554e5a17e3a566d20557ed3cebc2915daf2134f9c8d6db4b61080768878` |
| 前一 current SHA256 | `12e9dce0c42c16b4cd91624c757aadc3831ee61483618e946cc8354635b50691` |
| Γ target configuration SHA256 | `8e25a6651b3bbdf4d1d6ad4482738ac2e618a409ef0a85953b2949b4280cb08e` |

step 585 小回执仍为 3,973 B / `ae920ebe971c27a5ab8406604a6e24feb6e7b2dd080e6b54121224e9c2503a24`。step 586 回执与完整 manifest 中 current 的大小/SHA 一致。本次只读元数据，没有在本地下载、解压或重新计算这个约 580 MB 的大 current。

恢复沿冻结 core 读取 current 的全部已消费素数与序号，再从其真实下一序号继续；若同一产物内已有下一步的完成小阶段，也由原 `cached` 逻辑原样复用。不能退回前一预算产物或仅恢复旧 prime count。

## 完整活动载体

原 artifact `14246345143`，名称 `serre-global-R815-original-normal-derivation-operators-43853995004-1`，平台 ZIP 大小 4,854,538,446 B，SHA256：

`e33c97bbcd2516623839e67031ceb6bd46b39ac92ff4204ab808a411c4ba29f4`

API 实际到期时间为 `2026-11-17T16:08:03Z`。其完整 manifest 为 1,831,214 B，7,076 条，SHA256：

`42e141cbf6d05ce4e1e5a01f1b6599880eeb106d11f46148f695f34768e99855`

reference 为 368 B / `5b3fae76aa1a6eb4eaf78f3dd2d9b3816927828f6ed2b2c4db0464bab90c2e33`；public input 为 10,259 B / `3fd4b163260165440b64a4912f9990b96fd8601e1fc538a45bcb153835db5c0f`。

原 `R815-retained-producer-inputs.tar.gz` 为 109,958,828 B / `051571e117cdaafe31f9851c664c72583f55181444dbe112bbcbb7f2d2fbf1b3`。真实 `retained-inputs-receipt.json` 为 16,388 B / `7de014be25e8d963d651662a7670ba32c7fef4a1a571eb9854edb8a6868c28a0`，明确保存原 53 个 R806/R813 输入并逐件认证。

v24 纯 IO run `43905614017` 的约 5.3 MB artifact `14246206260` 只保所需元数据和小回执；它不含当前大 CRT 向量，也不能充当数学恢复源。新请求直接绑定上面的原 4.85 GB 活动 artifact。

## 唯一请求改动及冻结身份

新 `notes/R815-public-original-normal-derivation-operators-request.json` 只更新 `job.resume`：真实 ended run/source/artifact/ZIP/manifest 身份。它与本次实际 `public-actions-input.json` 中的原 job 对照，其他全部字段相同，预算仍为 300 分钟，原 53 输入、目标 `[g,Gamma]`、素数起点、每 8 素数 RR、16 行块、完整整数点恒等式出口保持。

冻结程序不改：

- core `R815_original_normal_derivation_operators.py`：`80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d`；
- wrapper `R815_public_original_normal_derivation_operators.py`：`ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454`；
- framework `R811_original_regular_multipliers.py`：`849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3`。

原 wrapper 恢复时核整个原 manifest、原 job 的数学字段、源身份、全部完整阶段和 current；真实 BudgetStop 回执不需要任何 schema 例外。本次没有新 adapter、没有补造 receipt、没有重算，尚未自行触发续算。Git 仅收请求与本简明说明；矩阵、CRT、大载体仍只在一日 artifact/carrier 中续传。
