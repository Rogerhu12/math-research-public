# 同一端点方程延拓的实际失败与纯 reader 修复：03b 第 28–32 步

日期：2026-11-26。本文补足已返回的第 28 步延拓初场失败：第 31 步取得第 29 步的真实 traceback，第 32 步用独立完整 v2 reader 成功读取同一份既有失败报告。两次纯读取没有重跑 Newton、场、J/J* 或 QP，也没有把科学失败改成成功。

证据：[公开 part-007](2026-11-26-public-actions-45820592817-1-part-007.md)，读取时完整文本 Git blob `a4a04434627656f169f259d7585e98ea5884c19b`，56,292 bytes。run 为 `45820592817/1`。

## 1. 原科学对象与实际失败

科学 driver SHA256 为 `9649ed99b614c468258646145948d7c06feb356c72806c73727728ea498ed88e`；完整 endpoint operator 为 `3f37789f1624b97cb7f83b1795ac5fe96be3b3026d4078115078f12e8fd4e34a`。当前模型 `73a9fb65ca3399c628bafa406c9a796ee5b2f16291bbf33544eb489d2290872f`，其 base 为 `9d4ccb16efe9a0c0f5b077c0e8919e76d1d04b06e669588b32e2de78c92f0258`，固定 g 为 `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb`，固定 18 字 Q definition 为 `05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e`。

第 28 步始终固定完整原自由点 `cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3`。辅助方程是
$$
H(z,\lambda;x,\phi)=C(z;x,\phi)-(1-\lambda)C(0;x,\phi)=0.
$$
辅助 λ 不是课题物理 t；既没有换目标，也没有在中途修改原自由点或冻结 Q。初始 λ=0,z=0，目标是 λ=1 后另读原方程 C=0。

实际第 28 步 41.35794009900201 s，exit 1；报告 `zero-closure-frozen-moment-Q-continuation-first/report.json` 为 366,286 bytes，SHA256：
`a2442ccad906f5fbc473376c5bd1644328235ae484ba8bebfcd8e4fa3019d335`。

停止原因是 `actual_initial_zero_closure_field_read_failed`；真实 root failure 为 `Continuation step exhausted before the original endpoint equation was reached`。最大实际残差 .06862860474650545，最大实际控制修正范数 .39909437428201144。不是 .75 球证明、不存在性证明或统一 IFT 失败判据。

## 2. 第 29 步的真实异常已经读到

第 31 步使用未修改的纯日志入口 `read_actual_followup_failure.py`，SHA256 `ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338`，实际 completed/0，6.056024680001428 s。

它绑定的原第 29 步 source 是 `a0c927aa9d7608a16ad7c051861903ebb533be3602325c2aada60ed6b1ccae61`，实际提交 `6c1b569ad6c6fadeba7edfd73f5db4efa9ef5ad1`，原 returncode 1、计时 6.034860249998019 s。原日志 1490 bytes，SHA256 `bc8ce160591ecff22ab6038f21ed7b56a522be661c620a42618c653c8caccd9f`。

真实最后 traceback 定位：
`read_report -> endpoint_roots(report.get('initial_endpoint_roots')) -> {key: value[key] for key in names}`，
最后异常为 `KeyError: 'endpoint_continuation_policy'`。有完整最后 Python traceback，bounded excerpt 没达到长度上限。这个因果结论现在来自实际 child log，不再只是静态候选。

第 31 步纯诊断文件为 `postprocess/actual-zero-continuation-reader29-failure-first.json`，2689 bytes，SHA256 `83c3fb606617c9481f79e685da796bd9aa819b659a3c68480628af3eb20424ef`。它明确 scientific_arrays_read=false、field_or_J_evaluations=0，未发布完整原日志。

## 3. v2 reader 实际成功，科学失败原样保留

第 32 步 source SHA256：
`75f4e9abd41972add063d3881cb4140aa6e259f09c2f9832c58c69be3c856e00`，
实际提交 `444a8b754d79b240056a8a9ddf224cb8a2fd61a6`，completed/0，6.056875335001678 s。

输出 `postprocess/zero-closure-frozen-moment-Q-continuation-first-readout-v2.json`，294,057 bytes，SHA256 `466e275fb86b13010adb93e8662ba16424490b2386756fa3f4115019c2c1ff13`。这是 runner 上的完整纯 readout；这里只发表紧凑实际结论，不把该大表转存为新输入。

v2 对已刊科学 driver 的短 snapshot 只读取其实际生产的键；完整 `latest_operator_metadata` 中的延拓 policy/counts/last_summary 仍独立严格绑定。没有给短 snapshot 缺项填零，没有把另一点的 metadata 回填到当前点，也没有改变任何科学源码或来源守卫。

实际读数继续为 complete=false、initial_failed=true；initial/final bundle、Phi、max、geometry 均 null；metric/restoration 方向和接受数都 0。失败没有形成一个可用的新场。

## 4. 八个真实角及 λ 轨迹摘要

每角都实际尝试 28 个 stage；下表按物理角数组的索引排列。`first_failed_angle_indices=[0,1,3,4,7]` 是此次最小步长耗尽的五个角，不能把这一五项列表的序号错配成八角数组的序号。

| 角索引 | literal φ hex | 最后接受 λ | 初始端点残差 | 接受 / 拒绝 stage | corrector updates |
|---:|---|---:|---:|---:|---:|
| 0 | `0x0.0p+0` | .8342783749103546 | .414119791001204 | 9 / 19 | 132 |
| 1 | `0x1.921fb54442d18p-9` | .8342783749103546 | .41411913939640227 | 9 / 19 | 131 |
| 2 | `0x1.921fb54442d18p-8` | .8342946693301201 | .41411718455182156 | 10 / 18 | 128 |
| 3 | `0x1.2d97c7f3321d2p-7` | .8343001008033752 | .41411392637793215 | 9 / 19 | 133 |
| 4 | `0x1.921fb54442d18p-7` | .8343001008033752 | .4141093647287637 | 9 / 19 | 124 |
| 5 | `0x1.f6a7a2955385ep-7` | .8343163952231407 | .4141034994062813 | 10 / 18 | 133 |
| 6 | `0x1.2d97c7f3321d2p-6` | .8343326896429062 | .41409633016479813 | 10 / 18 | 131 |
| 7 | `0x1.5fdbbe9bba775p-6` | .8343435525894165 | .414087856712987 | 9 / 19 | 118 |

完整本批计数：224 次 stage attempt、75 次 accepted stage、149 次 rejected stage、1030 次 corrector 更新、28 次 batch stage。C 按实际整批角计算 20,816 次；Cz 为 1760 次；backtrack angle evaluation 18,816 次；predictor angle 224，predictor fallback 0。

原策略仍 tolerance=2e−12、branch_radius=.75、每 stage Newton 24 / backtrack 18 / Armijo=1e−4。延拓 initial_step=.25、minimum_step=1.52587890625e−5、growth=1.5、shrink=.5、最大 stage attempts 64，预测开启。实际是步长耗尽，不是把 64 次预算用尽后冒作完成。

所有最后接受 λ 都小于 1，`all_parameters_reached_one=false`，`final_original_equation_checked=false`。失败记录的原 C 范数在最后接受控制处读取，用于诊断；它不是成功 λ=1 后的最终原方程验收。

## 5. 根、导数、历史位置和责任

成功缓存角数为 0，完整网格根不可用；这不等于没有尝试 Newton。root_iterations=1030、root_failures=1，升级角 jets 和 implicit blocks 都为 0。当前最大 root residual/correction、最小 Cz singular value、first/second jet residual 均 null。尤其没有原始 λ=1 的 Cz 奇异值，不能从 null 推断奇异，也不能据此补造分支折叠证明。

当前 initial/current 曲率与半径位置数均为 1763。这个失败发生在初场完整读取阶段；它没有形成新的接受场或 metric 方向。后继仍须用真实完整报告 walker 继承地点，不能仅凭这两个摘要计数猜测整个报告对地址并集的贡献为零。

第 31、32 步各有三个摘要索引缺项，只对应预设的 `first_failed_angle_indices.5/.6/.7`：实际失败列表只有五项。两个纯 child 均 completed/0；不把摘要缺项转成科学异常，也不给不存在的失败角填零。

现有证据说明：同一固定原端点方程的这条 residual continuation 实际没有达到 λ=1。它没有证明该原场的根不存在、整个 .75 球唯一、完整同族不可能，或课题无解。新 gamma 控制族与 H 初值变化需各自真实执行、重新绑定输入/模型，并保全旧地址和同目标责任；不能把更换数值方法本身写成成功。
