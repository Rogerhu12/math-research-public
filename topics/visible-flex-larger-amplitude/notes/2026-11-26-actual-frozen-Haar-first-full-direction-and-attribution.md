# 实际准确 Haar 固定目标的第一条完整方向：76/77 返回、来源与尚缺字段

日期：2026-11-26。本文只登记公有 Actions `45762076394`、attempt 1 的实际 stage 76/77，以及同一个已完成 job `139714175671` 的完整日志读取。原始报告与数组保留在 runner；本文没有重新运行场、Jacobian、QP 或科学 fixture。

## 1. 实际结论与范围

准确材料 Haar 目标在 stage 75 冻结后，第一条完整固定目标方向已经自然返回并被真实线搜索接受。新目标自己的初始和最终数值如下；所有比较都使用本次同一个固定目标、同一工作 moment carrier、同一观察测度和 `p=4, epsilon=.001, scale=.05`。

| 量 | 本分支真实 initial | 本分支真实 final |
|---|---:|---:|
| 最大相对 Gram 数值残差 | 0.01500409670694389 | 0.014064593921178363 |
| 原 `Phi` | 0.00018636609821128157 | 0.00017062316420247088 |
| 减常数后的 `centered Phi` | 0.00018604609821128162 | 0.00017030316420247091 |

stage 77 的纯报告读取给出同测度变化：`Phi_change=-0.000015742934008810682`，`centered_change=-0.00001574293400881071`。两个版本在浮点末位的差异按实际字段保留，不改写成完全相同的十进制数。它们表示同一数学谱目标只相差常数；本次没有拿旧 moving-mean 或 deep-scalar 的 Phi 相减。

实际方向数为 1，实际接受数为 1，实际最后阻尼为 `.01`。末场有限曲率必要筛通过，`necessary_reach_product=0.9914426611231815`；全点幅度数值筛通过，`maximum_inequality_value=-0.045112775754112544`，永久位置集合完整标记为真。以上数值只说明这一条完整优化方向的实际返回。最大残差仍约 `1.4e-2`，没有达到连续 `1e-6` 要求；没有精化收敛、连续 reach 或新末场完整几何证书。

特别地，已公开的 76/77 摘要没有包含该方向的接受步长、QP 状态、实际 Hessian advance 数、末面投影梯度、容差、J/J* 计数或全步拒绝原因。完整 job 日志亦未补出这些字段。不能从计划 `maxiter=256` 推断这次实际 `iteration_limit`，不能从最后 `mu=.01` 推断接受了半步，不能把以前 mean/deep 分支的方向归因移植到这一条新 Haar 方向。

## 2. 本次输入、固定目标与来源身份

实际父场为：

`7ebb5f42b29e0979f7a84a93fb8decb0b45ae8ec2f8c713bed820a8adb33d37b`。

实际新末场为：

`bcdcdab759a234e7d02aab066fb5049b1792cf3ecb2cbcb2791e4313c2f7350d`。

| 身份 | 实际 SHA256 / commit |
|---|---|
| 固定准确 Haar target identity | `e35ce2d39863848238d08d2cc783292ed39929239ec6cae036deab88c9d73123` |
| 冻结目标 manifest | `4db6a26e5fa330e00ad5e25976731b5134e39f1d15639c7ca1338e76ee39fc99` |
| 材料角 identity | `0f21f1e2f6ec76b2df2ef50e2f255d1516cbb0bef404ffeb83b25215a00b213d` |
| 本次数值 working moment carrier | `027c36ae6f55a204a9636eabf2eda841609a784b823c76435d74bddce7f0c16f` |
| working moment full angles | `8192` |
| 实际完整 solver body | `b70bdcd7c9b0e0a8cf101d9a59b229d048359318f8b5289e3513fc96ce79d61f` |
| 实际 launcher | `991e7d4a4c0f8141f34844e07d2a76b26496ba1d5a74867f25042c5fb47d8cf1` |
| stage 76 source checkout commit | `93bbc4dac68b6bfb00b909a8ade1c30e132c3959` |
| 实际只读 reader | `d8d48df3597068ca76c9be71e2cd6a585ccb91b2a27b68f5dc29e4ae08e5e91c` |
| stage 77 reader checkout commit | `75cb37fa68037c083cace0cabafc599c59e1892b` |

stage 76 报告 schema 为 `complete-fixed-true-material-Haar-with-held-amplitude-budgets-v1`；stage 77 summary schema 为 `complete-fixed-true-material-Haar-held-amplitude-actual-summary-v1`。实际 reader 核对的是完整 `b70` 来源与准确 Haar 分支，未把旧的 finite-angular-mean 报告贴成新标签。

这一分支沿原 R671 `lambda=1` 物理尾模型，冻结数学对象是父场的全圆材料 Haar 平均。`exact_Haar=true`、`finite_target=false` 指目标的准确数学定义；`Q=8192` 指工作 moment carrier，不定义一个新的离散目标。stage 71 的 carrier 完整返回仍带 `accuracy_reached=false`，stage 75 也没有给出 target/metric/geometry certification。不能把“准确 Haar 定义已冻结”误写成“该工作 carrier 的全部误差已经足以证明最终 metric”。这组连续误差责任仍由相应 interval consumer 支付。

## 3. 真实命令所保留的全空间问题

stage 76 实际命令声明一条方向、最多 256 次 Hessian advance，显式新目标阻尼 `.01`，完整物理角网格 `N=2048`，stage block 64。谱参数为 `p=4, epsilon=.001, scale=.05`；QP `atol=0, rtol=1e-6`；曲率必要筛阈值 `.992`，active band `.025`。已登记的原完整 q/H² 坐标、原变量、所有 mean 约束、全量径向正权、current fixed-target K00/v5 入口继续保留。该源码使用原完整 ray 回溯，没有声称已经接入 Haar 多轮 SOC。

stage 77 返回：

- `original_free_variables=1332245`；
- `all_full_rows=45324288`；
- `all_fixed_target_mean_constraints_retained=true`；
- `old_target_Phi_improvement_claimed=false`。

这里 `all_full_rows` 是完整 metric 观察行数，不是有限几何半空间数；`original_free_variables` 也不等同于带 coarse 冗余坐标后的缓存列数。不能混用这些字段推导 QP 行列尺寸。实际命令保留原 192 几何工作行并按既有合同追加幅度行；本次公开摘要未抽取实际追加行数和末面大小，因此本文不把它们作为已经读到的实际标量。

幅度预算沿当前独立定义：marked diameter budget `4.2`，witness lower budget `.9`，height floor `1.01`；径向候选数 2、距离候选数 4，两个 `p` 符号及所有旧/新永久点在完整真筛中保留。父场已有 own-first 只用于说明输入预算，未充当新末场 `bcd` 的连续证书。

本次实际新末场的永久位置计数为 curvature `2758`、radius `2754`。reader 核对 `exact_permanent_set_complete=true`。这不表示有限观察集合等于连续域。

## 4. 自然返回的输出与成本

以下路径均相对于本次 runner 的 `research/`；SHA 为实际 controller 对自然返回文件读取所得。

| 输出 | bytes | SHA256 |
|---|---:|---|
| `frozen-true-Haar-7ebb-amplitude-p4-first/report.json` | 21768590 | `a76c4d55b3737ffa4a8ca3a3ed9f0a236ec5ba1c25237bae735b4fd4ff531ea5` |
| `frozen-true-Haar-7ebb-amplitude-p4-first/final.npz` | 10377207 | `bcdcdab759a234e7d02aab066fb5049b1792cf3ecb2cbcb2791e4313c2f7350d` |
| `frozen-true-Haar-7ebb-amplitude-p4-first/exact-tail-lift-profiles.json` | 11272 | `22cceaea7a49a97854a3be04b71c7f57411cb815704bbb916a48ee729899c414` |
| `frozen-true-Haar-7ebb-amplitude-p4-first/exact-tail-lift-profiles.npz` | 150838 | `3d5063c868245c155b6258f47d0ed5059ee48ae98da520f930a7e08153332cc8` |
| `frozen-true-Haar-7ebb-amplitude-p4-first-command.json` | 54605 | `5c92664d9f7703b19f362427cee5a34db1878d50078230a4b76754be714af08f` |
| `frozen-true-Haar-7ebb-amplitude-p4-first-inputs/complete-current-positions.json` | 177505 | `25c0db15cb8e01d615189b2aee5fa78128c4afb87cef414ba302f1e8ff608363` |
| `postprocess/frozen-true-Haar-7ebb-amplitude-p4-first-summary.json` | 10041 | `3208d593be7402a4ab731a0da6f58d5163a2b9538825e99f8354c228c0316c73` |

stage 76 用时 `829.8936677929996 s`，stage 77 纯读取用时 `6.180354200001602 s`；两者 returncode 都为 0，`summary_errors=[]`、`missing_outputs=[]`。stage 76 报告进程峰值 RSS 为 `3258188 KiB`。这些总时间不分解成尚未读到的 QP、Gram 构造或真筛时间。

自然返回后，controller 依明确清理模式删除该新步骤自己的两个再生缓存目录：combined rows `2105130968 bytes`，original geometry rows `2051701248 bytes`，`skipped=[]`。没有删除父场、输入或上述自然返回输出。这些实际清理字节只是磁盘责任记录，不证明预条件器已加速，也不代替 J/J* 计数。

## 5. 完整 job 日志没有补出缺失的方向归因

实际日志读取来源为 [job 139714175671](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394/job/139714175671)。连接器返回的完整解码日志为 801706 个字符、按换行分割 5507 行。stage 76 的 `followup_started` 时间为 `2026-11-26T10:46:36.4246095Z`，`followup_returned` 为 `2026-11-26T11:00:31.3184374Z`。中间 220 行仅含 git 同步、规则检查和 compact conclusion 发布，没有这个 Haar 子进程的 QP/trial 进度。stage 77 于 `11:00:40.4430468Z` 返回的事件仍只包含上面既有摘要字段。

因此，当前能够确认的是本次完整来源核对、实际同目标改善、真实接受数、末场必要筛和永久点责任。下面这些仍是**未从可用原始输出抽取到的字段**，不是数值零或不存在：

| 尚缺字段 | 不能据此作出的判断 |
|---|---|
| accepted alpha、true trial count、逐 trial 分类 | 不能判断本次是否几何截步、是否 full step 通过 |
| QP status、advances、末面 Pg 与 tolerance | 不能判断本次达到驻点或耗尽 256 步 |
| active face、adds/releases、same-face advances | 不能移植旧 mean/deep 的活动面切换归因 |
| actual J/J*、coarse construction、fallback 与各段秒数 | 不能宣称实现加速、0额外 J 或某项成本占主导 |

现有只读 reader 的完整输出实际上已有若干方向字段，但第一次 controller summary 未选择它们；完整大报告也保留更多 QP 字段。追加 pure reader/标量 summary 的方案因此合理，且不需要重跑优化。然而本次新增步骤尚未被该 job 执行，不能提前写成读取成功。

## 6. job 收尾边界和下一实际责任

完整日志最后的实际 controller 事件为：

`2026-11-26T11:04:33.5840583Z followup_controller_checkpoint`，
`reason=budget_checkpoint`，`actual_returned_steps=49`，`research_complete=false`。

该 job 的总公开 stage 仍止于 77；`actual_returned_steps=49` 是 followup 控制器自己的返回数，不与总 stage 编号混为一谈。后来登记的新 pure attribution 和 `bcd` own-first 没有在本 job 被 admission，不能记作 stage 78/79、不能填实际输出或证书。本报告没有利用 job 正常结束来声称课题结束。

接续时必须保留本次真实 `bcd`/`a76c` 来源和准确 target `e35ce`；新末场 own-first 使用本次自己的 reference carrier。先补出真实方向归因后才能据实判断是否沿当前层续步、调整谱目标或接入同父 SOC。当前一条方向的 Phi 与 max 都下降，没有证据判定 p4 的最大误差已经停滞；也没有依据把此分支误差直接与 deep 分支相减。完整固定 g 精化、连续 metric 上界、全场 reach 及标记幅度证书仍然未完成。

实际公共证据：[stage 73–77 compact record](2026-11-26-public-actions-45762076394-1-part-009.md)；[stage 75 准确目标冻结](2026-11-26-actual-frozen-material-Haar-target.md)；[完整 Haar 入口与责任](2026-11-26-complete-frozen-Haar-amplitude-actions.md)。本文登记一条实际优化返回，未增加条件定理编号、未重复已登记的准确 Haar 定义证明。
