# 有限 Lorentz 锥新入口：完整恢复、原接受门及向量保存的执行前审阅

日期：2026-11-16。本文记录执行前的源码与原输出核读，不把源码检查记为已通过的程序检查。新运行结果另记。全部新研究、人工/API 检查和数值执行仅由本公开仓库 Actions 进行。

## 1. 唯一祖先与已关闭的费用

唯一最新来源是 run 43789033043 / job 133043031523，源提交 `a08ed9fb3bd44ece17befa23651b281e67f6bb1b`。原日志 2,957,208 B，SHA256 `a465b5f6b09de317c8b9b541953171968543e91f3de3ad52ae4bac9e6dc5f8c0`；MODEL/COMPLETE 的原 JSON+LF 身份见 request 与 transfer 源码。

[末槽实际](terminal-paid-slot-final-rejected-trial-and-capture-gap-20261116.md)已经用尽原64次：63 primary、1 SOC。末次候选真实两网试验拒绝，原14门虽过，目标改善为负；原任务不再有第65次额度。累计62次实际值、356.129820261科学秒包含两次入口失败，原 checkpoint 中较早的计时不能替代这个最终数值。

新入口只读这份完成日志一次，不再下载旧 direct 或两份失败日志。其原11项人工及更早9项几何检查通过 transitive 收据消费，不重执行。全部原168个源码/流程/说明绑定和原98项输入参数逐项保留，必要24份原输入仅用于原不可变对象恢复。根代理已对比这两个清单，均逐字相等。

恢复的当前点是原接受27，physical SHA `bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c`。原池4439/4533、版本8/6、半径1/8000、两streak0、bank512、learning36事件35提交且pending0，全部由这份实际输出恢复。原4条独立支持和末槽4个 witness 按原 append.kept_new_indices 精确保留，不根据数量猜其互异性；同ID不同normal不替换已有支持。

## 2. 已冻结的新方法与新预算

[预算与接受合同](finite-cone-restoration-budget-and-acceptance-contract-20261116.md)是这次新任务的依据：

- 新科学时钟1200秒，在读取最新来源与原输入之前启动；同时保持原累计1800秒上限。
- 新 solver 总数32，均为有限锥；旧 HiGHS LP 和 SOC 新调用数0。每个冻结模型最多4次。
- 新实际值96，同时保持原累计160上限；恢复所需粗细各1次计入，不另开免费几何。
- 单次 solver 上限10秒，实际 time_limit 取单次、新任务余时、原累计余时三者最小值。
- Clarabel 0.11.1，max_iter=200、max_threads=1、tol_gap_abs/tol_gap_rel/tol_feas=1e-9；实际全部后端 defaults 在覆盖后记录。
- 仅 Solved/AlmostSolved 可进入原候选门。状态、预算用尽或不存在可返回步均不构成驻点、可行性或主题完成证明。

原 cfg 的64/160/1800/10及所有原数值类型逐字保留。新方法另有明确 objective 身份；原 field、factorization、coordinate、参考、g、b0、grids、width、bank context、learning context 不改。外层字段 new_scientific_seconds_limit 与 adapter limits.max_scientific_seconds 显式同值校验，计数严格为真正整数。

## 3. 161变量中的完整有限锥

主程序仍使用159个独立物理方向及原rho、norm两个辅助量，保留原线性约束、边界、目标系数及全部已付 supporting rows。de/df 是物理159导数，原 step_scale 只乘一次。对每条原metric行的两个分支，使用四维 Lorentz 锥

```
(2(target+rho) − sigma*e, e, 2*f, epsilon) ∈ L4,  sigma ∈ {−1,+1}.
```

即原平滑谱分支的真实有限 affine norm 约束；不是把一个方向normal的线性支持重命名为完整锥。原非负线性块和有限上下界全部一起进入，二次目标矩阵为零。

每次返回先检查原161向量、线性与边界残差，再调用同一个完整网格 affine oracle。原 _candidate 的全rho修复、原norm辅助量、gain/gap/dynamic tolerance 保留；修复后所含锥的残差按原metric单位除以2核对。最多四次内部扩展仅来自刚实际观察到的原网格 attainers，当前模型已保留的全部 A/b 支持不因bank更新而消失。

早先 incumbent 已用完整rho上修，因此应满足后续新原行的锥；返回前仍对实际最终有限锥集检查，不能凭该推理跳过真实残差。inexact gap 可按原规则进入真实试验，但它不因此被标为精确锥最优解。

## 4. 原两网接受、学习与状态接续

ordinary assess 的6,880 B源码与已发布末槽版本逐字相同，SHA256 `451914f72334195033c100c2917048239ff8e0fd6ce61ad228c6d984601fc9be`。真实两网14门、原盒、严格目标下降、行学习、完整相对质量、经验curvature guard与原半径反馈都保留。新外层没有SOC入口，不重启原LP账。

新粗值失败但实际geometry已经启动时仍计费；缓存命中不算新实际值。恢复36个已提交事件不再重复commit。当前完整 checkpoint、真实接受点及全bank/池/learning始终独立于是否出现新的可接受点。

末态的门收据来自准确的旧接受27，或确实产生新接受的那个完整粗细试验。没有另起独立末审几何，没有把原取样14门当连续同g、全时reach或嵌入证明。

## 5. 在所有过滤之前保存真正返回向量

旧末槽输出的 new_candidate_step_record=null 与硬编码 saved=true 不一致，已经在原实际说明中承认，不能重演旧LP补全。本次修复的是实际捕获位置：

1. solver.solve()返回后立即读取有限161向量，转换实际physical159步并存 exact binary64 字符串。
2. 该捕获发生在 status、solve_time 等附带metadata读取之前，也在状态资格、剩余时钟、原残差、全oracle修复之前。
3. 启动调用前，event 已挂入模型同一个 lp 容器，并先计入独立额度。constructor、metadata、修复或后置预算异常保留事件、费用和已经存在的向量。
4. 每个 MODEL 输出保留全部候选exact159、全部trial exact159/physical163、原14门、学习及质量；只将重复的大初始cone tags、row来源及bank重建明细按字段转成count/hash。
5. COMPLETE保完整可恢复末checkpoint，只不重复MODEL。所有“实际已保存”旗由原events/向量列表真实存在及长度推出；零实际返回或零trial记null和count0，不把空集当作已经保存某次执行。
6. 外层共享报告对象，使进入科学过程后的save/emit异常不会被重标为“输入未就绪、0次调用”。开发失败保已经测得的总开发秒；来源解析失败保已起科学钟。

不使用旧的全树数组长度过滤器，不在Git、artifact、Release或cache保存这些科学payload。runner临时JSON及原stdout是唯一实际载体，输出另记真实bytes/SHA，不凭路径存在推断已上传。

## 6. 仅本次新接口的必要检查

公开流程只安排3组共12项新检查，组数3/4/5：

- 新固定版Clarabel真实微型API：1次新小锥，核版本/设置、解析解和实际计时。
- 161变量与原修复接口：两条分支的尺度和半锥残差、完整rho、真实有限步捕获、拒绝状态仍保向量。
- 独立账/时钟/错误路径：额度用尽不启动，time_limit取交，constructor失败、计费后的settings metadata失败，以及返回后global deadline耗尽仍保向量而不做oracle。

总计4次新labelled stub constructor，另有一次计费后但尚未到constructor的metadata注入失败；不调用原geometry、原J/JVP、HiGHS或旧开发组。这些费用与正式新32锥科学账分开如实报告。源码核读不代替这些检查实际通过；若失败，先消费其真实报告与费用，再按实际失败修正。

## 7. 本次源码与唯一流程

| 路径（脚本相对本课题） | 字节 | SHA256 |
| --- | ---: | --- |
| `scripts/frame_metric_finite_cone_primary.py` | 27820 | `7e69048c424ee46948c4e86d90b91cfdbd87013383d37bd5dd862ddfd60fc7b9` |
| `scripts/frame_metric_finite_cone_epoch.py` | 26942 | `89e73d86d1e2260120e8cd070f76b53a47e73ed0ae47c10b0669d130b257eb98` |
| `scripts/frame_metric_finite_cone_recovery.py` | 32239 | `437d6edc5bfc3890c83c07222ba2162a4ac4ac1a04d0bfa110f8d7c77d07ae03` |
| `scripts/frame_metric_finite_cone_transfer.py` | 19941 | `62df34b369144b8e967bb4360114acfd5243e982dd5ad8f907d47c741451451a` |
| `scripts/frame_metric_finite_cone_development.py` | 14010 | `95957b0cb76c0b78386755ee551f79be042185620f8eb55b06243a22fd05cf1c` |
| `scripts/frame_metric_finite_cone_audit.py` | 33436 | `9c64e7aae25d7d6b8daceea148661fe422a6bfbf6d29f1f7c32624ca208da337` |
| `computations/request-finite-cone-primary.json` | 41315 | `340d6f063831331cfa56f9da64785a05f74a60c7d76c9a858be6c63c5563df64` |
| `.github/workflows/visible-finite-cone-primary.yml` | 4432 | `afc9112fc7c13e001a34135ce93b147c927629b44520d83094385e10a0b2f306` |

完整 request 共175绑定=旧168+新6脚本+新workflow，Python闭包164=旧158+新6。流程部分克隆、实际pull公开main与私有规则，核双README新diff；不符即停止新研究让根读差执行。之后 detach 本次源提交、核全部175来源，才进入上面新检查和正式科学过程。没有 py_compile 或旧测试、缓存、上传步骤。

本说明对应一次新方法入口，既不是原末槽任务的重跑，也不授权原实例预算延长。真正数值结论以本次原Actions输出为准。理论的共同J、共同cap及全部内部period研究继续，主题完成门仍未支付。
