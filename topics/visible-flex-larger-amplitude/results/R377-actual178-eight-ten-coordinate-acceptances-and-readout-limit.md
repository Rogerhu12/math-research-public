# R377：actual178 完整十坐标已完成八次接受，必要摘要超限而未传回末点

AI 辅助研究记录。本文只读取本次官方 Actions 的原日志、JSON 字段、源码合同与字节身份，没有重新执行模型、梯度、QR、FD、范数、域或优化计算。全文范围以本次真正返回的必要记录为准。

## 1. 结论与准确边界

actual178 的科学 producer 返回 **0**，原 phase 为 `diagnostic-completed`，原 `accepted_point_count=8`，原停止字符串是：

```text
Explicit eight full-ten direction budget completed
```

因此，本次完整十坐标方法确实沿原三残差接受规则完成了八次接受。工作流 compute failure 的直接原因是随后 reader 的必要摘要为 **116,585 B**，超过既定 **90,000 B** 上限，reader 如实返回 **70**。它不是 producer 数学异常、八个方向全拒、规则变化或墙钟耗尽。

但是，超限后的 fallback **没有返回初末 merit、末十参数、逐方向动作、实际试步正文及初末 FD 数值**。这些信息的原身份仍有记录，而正文随 request-owned 临时目录清理而丢失；没有 artifact、Release 或仓库 raw 副本可供恢复。本文不能填入缺失的值，也不能把八次接受推成已完成原 unit、full112、native、BVP 或最终几何目标。

与 [R373](R373-actual164-r3-six-shapes-and-twenty-full-merit-rejections.md)、[R376](R376-actual174-all-station-odd-signsum-and-twenty-full-merit-rejections.md) 的单新坐标试探相比，本次**“八次接受”这一原计数**是明确的新进展；实际总降幅、末残差、最弱方向精度及后续参数选择仍须新的完整必要读回。不能靠摘要的字段字节数猜这些值。

## 2. 唯一实际运行与任务阶段

| 项目 | 实际身份 |
|---|---|
| repository | `Rogerhu12/math-research-public` |
| request | 178 |
| run | `43749066353` |
| source commit | `d9336e76fe9948d642e6e079bbdf26946b6d42d4` |
| created | `2026-11-15T18:51:07Z` |
| compute job | `132918741565`，failure |
| report job | `132919216018`，success |
| workflow | `.github/workflows/visible-larger-public-fixed-power-ten-joint-newton.yml` |

实际 job metadata 给出：steps 1–7 全部 success，包括112个来源、10个支持来源、实际157父参数与原四输入绑定，以及原78文件恢复。Step 8“Eight joint ten-coordinate directions and original20 full3 trials each”为 failure。随后 step 9 原读回、step 10 原错误日志保存、step 11 owned 清理全部 success。Report 成功只是完整打印了已存在的 fallback，不是重新执行科学，也不覆盖 compute 的失败状态。

原 wrapper 分责如下：

| 原字段 | 原值 |
|---|---|
| `started_experiments` | 1 |
| `completed_experiments` | 1 |
| `child_exit_code` | 0 |
| `reader_exit_code` | 70 |
| `scientific_diagnostic_completed` | true |
| `scientific_stop_reason` | `Explicit eight full-ten direction budget completed` |
| `explicit_wall_termination` | false |
| `received_signal` | null |
| `wrapper_exception` | null |
| `traceback` | null |
| `post_step_reader_exception` | null |
| `post_step_reader_exit_code` | null |
| `partial` | true |
| `wrapper_wall_seconds` | 44.28090299300004 |
| `report_did_not_run_or_resume_science` | true |

这里 `partial=true` 包括必要读回未完成的工程范围；不能反过来说 child 的八次计算没有完成。`actual_scientific_step_outcome="failure"` 是 Actions step 的组合结果，不能替代更具体的 `child_exit_code=0` 与 `reader_exit_code=70`。

## 3. 实际原件与传输身份

本次只各取得一次已终态的两份官方 job 日志。未读取运行中日志，也未另取不存在的大 artifact。

| 原对象 | 字节数 | SHA256 |
|---|---:|---|
| compute 官方日志 | 84416 | `c4351404787e8622173424eff508d1f0835fc37f3c38226d3a2ad84538e10183` |
| report 官方日志 | 16064 | `9e78bf85cd92b9204ae191564bfaca8e1a93e61853855d4d696357f86fe69f43` |
| 原科学 status | 970456 | `ee99fd4a5475cea69ec4ccb23d023abd8e8d007802ec64885dd8a7b32ef694ea` |
| reader 已形成但未运输的完整必要摘要 | 116585 | `2d4f8af521b80aa5f79f73dc9ff6b72a8b50f9e4c83f243f2c17efe2f248e872` |
| reader fallback | 4297 | `59a9dc3bdfbe532a836b976b641e9bf6f4cd057fc337094702db64e8a7278efc` |
| 加上 wrapper 实际责任后的最终 compute/report 摘要 | 5678 | `0f36d8de98d22692f58193340912c5887214d1dc95a9f257c9336c248e3fe130` |
| producer stdout | 436 | `f21b1d7448f8b02013b95e0657d51bef0c5f2e00e348b8d51c77241b14106138` |
| 原 reader stdout | 8664 | `a98eda51611f5fe349070ce8fc3b1ad49b72de0e14e720873d9ed503b0f01b85` |
| producer stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| reader stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

5678 B 摘要身份不含日志分隔 LF。两份日志各自原字节身份保留；JSON解析视图只剥每个物理行首一个 BOM 和锚定的 GitHub 时间戳，不改变正文数字、字符串或 source 身份。Compute 与 report 的最终必要 payload 相同。原 reader stdout 的工程文本块已完整读取，其中只有 section 字节计数、4297 B fallback 及其身份；它**不含**116585 B 完整摘要正文。

原 status 文件名是 `fixed-power-ten-joint-newton-status.json`。这里列出其身份只表示 producer/reader 原记录绑定了该原件，不表示本文取得了970456 B status 或逐值读取了它。也不能根据完整摘要 SHA 反造正文。

## 4. 本次实际执行的独立算法合同

原源、request 及 startup 实际元数据共同绑定了本次算法：

1. 从 actual157 的九个持久 Decimal50 参数字符串独立重建原有限模型，额外坐标 $\xi$ 初值为0；没有导入已删除的164或174场、旧 J、旧 FD 或旧末状态。
2. 新形状固定为 support1、power4。它是真正十坐标族；每轮均重形成完整十列响应。形状不随旧九轴 FD、试步或最终检查重新选择。
3. 物理尺度为事先声明的 $S_j=0.01\max(1,|p^{157}_j|)$，新坐标尺度为0.01，缩放信赖球半径为1；父 radius 只记录为来源，没有假称沿用。
4. 每个方向由实际完整 $3\times10$ 响应形成。主方向使用全十维缩放最小范数 Newton/clip；若实际算术或方向条件不能使用主方向，才走原已声明的全十维 Cauchy 分支。形成的 rank 或线性残差不是额外科学通过门。
5. 原八方向、每方向二十档真实 full3 线搜索、严格下降与精确 binary64-lift 的原 Armijo 系数均保留；没有缩减试步或把单一新坐标残差当目标。
6. 原完整699节点链、固定112终端责任、初末十轴三尺度的 Decimal 与 binary64 对照，以及显式投影处的原域/453圆/最终责任仍在 producer 合同内。读回不完整不准把这些约定改说成本次已逐值核实。

相应代数条件见 [R378](R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md)。该证明区分精确实 QR 恒等式、有限形成误差和真实非线性余项。本次八次实际接受不自动支付这些误差的严格界，更不是最小范数方向准确性或 full3 驻点的证书。

原 startup identity 还明确：

- `source_count=112`，`workflow_support_source_count=10`；
- `origin_child_source_count=41`，`current_child_source_count=45`；
- `actual157_nine_persistent_words_are_only_initial_numerical_inputs=true`；
- `independent_ten_coordinate_family=true`；
- `parent_state_J_merit_FD_not_reused=true`；
- `raw_output_retention=false`。

这些是本次原实际来源事件，不是把 support1 形状移植成新连续 C 目标。旧有限 Gauss 链与准确定义 R323 族仍须依 [R298](R298-original-finite-Gauss-clip-seam-and-same-target.md) 区分。另一支线关于准确 coast 的域反证与修正，不由本次十坐标接受计数消除。

## 5. 超限位置：确有可去重复，不能删科学试步

原 reader 首先输出了全部 section UTF8 字节计数，再执行90000 B上限；因此这次可以定位工程开销，无须猜测参数或重新计算科学。

| 原摘要字段 | 原编码字节数 | 实际含义 |
|---|---:|---|
| `original_outer_steps` | 36724 | 八方向的重复状态、动作及中间读回 |
| `all_original_real_trial_rows` | 21039 | 所有实际真实试步的标量表 |
| `last_original_direction_model` | 10107 | 最后实际方向的完整必要模型 |
| `initial` | 6409 | 初始描述及FD摘要 |
| `final` | 6456 | 最终描述及FD摘要 |
| `initial_binary64_projection` | 4266 | 初始显式投影描述 |
| `final_binary64_projection` | 4283 | 最终显式投影描述 |
| `original_complete_circle_check_at_binary64_projection` | 3021 | 原完整圆检查必要记录 |
| `complete_scalar_domain_at_binary64_projection` | 987 | 原标量域必要记录 |
| `complete_planned_outer_rows` | 1463 | 完整八方向计划/已启动/未访责任 |

这些**只是原字段的编码长度**。不能从长度推出其数值、试步数或最终 flags。最小修复方向是消除 outer/统一试步表/最后方向之间的真实重复，同时保留全部实际 trial 标量、八个实际 $d,Jd,$ slope、接受参数词、未访和错误，以及全部初末FD与最终责任。读回容量不构成缩短科学预算或放松门的理由。

当前 fallback 原值为 `complete_original_readback_not_transported=true`、`scientific_failure_not_inferred_from_summary_size=true`。本文没有把工程 fallback 当完整科学摘要，也没有把116585 B原摘要切块或编码传送以规避大小限制。

## 6. 已付与尚未取得的范围

**本次原值已付：**固定来源的科学 child exit0；八次接受；八方向预算停止的原字符串；reader oversize116585及exit70；完整 wrapper 终态、两个空stderr、规则同步和owned清理；以上所有实际原件身份。

**本次正文未取得：**

- 初末 full3 merit、三个残差与末十个 Decimal50 参数；
- 八个实际选中方向的数值、Newton/Cauchy 分支及完整QR误差；
- 每方向接受 alpha、真实试步总数、每一档的 merit/Armijo/域/理由；
- 初末120项FD比较的原值与全部异常；
- 原 Arb、453圆、full112、unit 各终态的具体布尔与数值。

不能补造末父，不能把原157父或任何此前末点改名成actual178末点，也不能把“producer约定执行了最终程序”写成“报告已经逐值核过最终门”。当前需要的后继是读回工程修订后的一次**新实际运行**；科学 producer/search/recipe 与原门保持原字节。它不是恢复本次已清理的raw，也不承诺重算会获得相同浮点轨迹。

## 7. 规则与生命周期

原规则同步事件为 round0，时间 `2026-11-15 18:51:59 UTC`，实际读取 `d9336e76fe9948d642e6e079bbdf26946b6d42d4`，随后规则记录发布 commit `98e10f4f9197d3630dbbcac76c5598c0d65d12d6`。冻结规则监控周期2700秒未改。本次约44.28秒 wrapper 期间不因没有第二个周期事件而假称漏过一次应执行的45分钟同步。

实际清理事件列出三个本 request-owned 目录：`visible-fixed-power-ten-joint-newton/fixed-power-ten-joint-newton-temporary`、`visible-fixed-power-ten-joint-newton/original-inputs` 和 `fixed-power-ten-joint-newton-original-source`。事件明确未上传artifact或Release。清理是在错误文本读回之后完成，但必要完整科学摘要尚未成功。后继178r2应把主动清理限定为“必要摘要成功且 owner 已静止”；reader超限时保留同job owned现场供工程处置，不能再以清理成功掩盖必要读回失败。该生命周期修复不改变科学接受门。

## 8. 冻结来源与可复现范围

| 原文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_fixed_power_ten_scaled_newton.py` |15144|`6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861`|
| `geometry_20261115_fixed_power_ten_joint_newton_recipe.py` |30304|`3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e`|
| `root_20261115_fixed_power_ten_joint_newton_scalar_readout.py` |38363|`0610bc3ff66494370018df8c8cd5cb04371fe33c1e48b7160033cbf4e951221a`|
| `geometry_20261115_fixed_power_ten_joint_newton_temporary.py` |19273|`9bb076c098115d701804cfbdf32cb4c1af0689c5e060e6e9dc55a0b2646ee224`|
| `fixed-power-ten-joint-newton-actual157-parameters.json` |8891|`c8bb1ca8dfbd745845fab11e421ca9189bfdd20af101931c5ddb7a4ab8cd37a7`|
| `public-fixed-power-ten-joint-newton-request.json` |44351|`f7b24f5754b4461b5d2fc0a93ccd044e1699932f0a4e7dd4e420b21ae3edb438`|
| `.github/workflows/visible-larger-public-fixed-power-ten-joint-newton.yml` |22327|`799e0b79be2d3c7f4de3e34c57cb7b6712bfdaa885bdcacf7f5bb873491141f3`|

源码、参数、实际run与输出SHA足以登记本次可复算实验；不重新保存可复算status或完整数组。下一actual须另列run/source和新的原结果，不能借本次未取得的末词作为父输入。
