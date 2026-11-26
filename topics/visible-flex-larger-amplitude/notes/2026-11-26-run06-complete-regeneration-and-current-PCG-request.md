# Run06 完整依赖再生与当前全空间 PCG 的公开运行请求

日期：2026-11-26。本文是完整可执行输入与来源说明；尚未把任何第06次运行结果写成已发生。数学完成标准、连续同场认证、固定问题精化和全部永久地点责任不变。

## 1. 目的与已知父

Run04 的实际48/49已经完整返回第三个归一化SO3后退SOC方向，父末场为 `a801cf94cea863374b4453046c09bfb95a24903a8e6bb0e0a7ccbf6915de4b37`。其完整内层仍在64次iteration_limit，故继续研究需要实际新方向。其后原第四方向的单准入pair于21:49:59真实启动；22:07:10 GitHub API显示job和科学step均completed/cancelled，而公开小卷仍仅到49。不能补写第四方向结果、退出码或新地点。

第06次运行由完整可公开输入重建自身实际父，然后启用已刊当前8列全空间PCG。这里不会把旧缓存、检查点、完整报告或原始科学数组移到Git、Release或artifact，也不会从旧SHA造数据。依赖再生不重新宣告已登记的旧科学结论。

## 2. 入口与控制器

工作流文件是：

`.github/workflows/visible-larger-normalized-parent-20261126-06.yml`

其push触发路径仅为：

`topics/visible-flex-larger-amplitude/computations/resume-20261126-actions-request-06.json`

亦保留workflow_dispatch。并发组为独立的 `visible-larger-normalized-parent-current-PCG-20261126-06`，不会取消旧job。job预算350分钟，控制器准入预算20000秒；预算不是数学停止标准，亦不保证任意后继child能在硬截止前返回。

完整控制器 `public_actions_controller_parallel06_compact_metadata.py` 为19006B、SHA256 `acff1a861a5e080fc014627b8021ff40c4fa9848e36ebfec91c4e5b49e1b256f`。对已刊04控制器只替换独立06 HANDOFF槽和可见标签，完整执行、规则检查、源码绑定和发布逻辑不改。它仍使用已修正的完整followup源 `3cb1e706ab43dac6e952ce00b41e83055112d2ee65edb37682d1f05e94f2ee3f`，保留“先存runner返回事件，再发布”与cleanup紧凑计数修正。58KB、60KB、95KB、10KB及课题200MB限制全部保留。

工作流仍固定原Actions提交、Python3.12.14、NumPy2.3.5、SciPy1.17.0、Torch2.5.1 CPU和原线程设置；没有把依赖安装当科学验证。控制器每次pull检查根README与本题README，只读差异并据新规矩行动。初读两SHA分别是 `581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102` 与 `3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d`，首次请求读取提交曾填 `3f766c95e204380341c7b562512d935ccfb165ae`，该未公开对象导致首启动失败；[实际修复](2026-11-26-run06-startup-failure-unfetchable-rules-commit.md)将此唯一元数据改为根真实pull且核双README的公开 `28dbb9b17a47476f41d83782b90e059a6c0e0c67`，其余源/数值参数不改。

## 3. Bootstrap十二完整对象的精确对应

request先运行原完整 `rebuild_a04_chain.py --stop-after continue`，即已登记28段必要再生。随后是完整12对象，来源为04队列Git blob `939929d951a5cc2722f2d5c45addedbe48df0566`，该原队列93272B、SHA256 `86c0bfbf42e0bc0a5deb79f21d55b814f67f04780bd1a1b92a92119b294d18e6`。

| 06对象索引 | 04真实阶段 | 原完整入口 |
|---:|---:|---|
| 0 | 29 | 完整永久地点manifest压缩 |
| 1 | 30 | R671 full-Phi首方向 |
| 2 | 31 | 原R671 v3完整续方向 |
| 3 | 32 | R684完整physical-mean p4方向 |
| 4 | 33 | R688当前均值面PCG |
| 5 | 34 | 该实际场完整幅度几何读取 |
| 6 | 35 | 原幅度v1入口，保实际失败报告依赖 |
| 7 | 36 | 完整幅度v2方向 |
| 8 | 37 | 固定deep标量完整输入准备 |
| 9 | 38 | 完整固定deep幅度方向 |
| 10 | 39 | 实际归一化父profile完整SO3入口 |
| 11 | 40 | 完整严格内部恢复入口 |

十二对象分别就是04原队列索引0–11。更早来源是02完整archive001的索引0–9、14，以及当时02活动队列的索引1；原 `reconstruction_origin` 全保留。

已逐对象核实：**只改fresh id、scope说明，新增reconstruction_source**；完整script、args、parent_bundle（存在时）、outputs、summary、cleanup和所有其余字段逐JSON值完全相同，没有缩减科学参数或改变失败处理。完整逐项映射、原/新对象SHA、参数数目和精确来源见：

[十二对象完整对应](../computations/resume-20261126-run06-bootstrap-twelve-object-correspondence.json)

该15599B小文件SHA256为 `87cb13247941a744861d904bc774d2accd2f0557f320727c5ca28c01d67ada2f`。其中对象SHA约定是完整解析对象按原属性顺序compact JSON.stringify后UTF8；这是参数对象身份，绝不是科学raw身份。

新的bootstrap队列76950B、SHA256 `88681682ff4865d4f15d6585f312314a4d48acf044b970b9c6d768c258e9a8c9`。其finish_when_done=false，不在再生父后人为结束。

## 4. 四个完整历史方向

独立完整history-ready保原892f的四个科学对象：原实际44、46、48，以及原已准入但未返的第四方向完整科学child。每个都保原全部数值argv与每个前序report/history/cache来源，按本runner实际路径续接：

1. `so3-closed-actual-profile-cached-backtracked-SOC-v2-first`；
2. `...-v2-second`；
3. `...-v2-third`；
4. `...-v2-fourth`。

该ready为32872B、SHA256 `323be223ed09c95d6e0f52ab1fb9b2b6a839f67efb4a55116c47cca5a3f57278`。第四是本run真实计算，不声称恢复了原第50项结果。原纯读45/47/49不产生科学后继输入，故其数值原数组不需要为了再生重复读取；其全部原参数、源与已返结论仍公开保留。原41/42/43是已经明确的入口key失败与纯trace，没有后继数值父，不把已修v2冒称原v1成功。

活动队列须按既有完整参数归档机制滚动：先把**已经实际返回**的bootstrap对象连原headers与实际紧凑证据完整归档，再追加四完整方向与下节PCG单准入对象。76950B+32872B本就超过95KB，不能直接合并、缩字段或降低守卫；未返对象不能移出。

## 5. 永久地点与跨runner的边界

完整源归纳令P包含两个初始完整memory及所有传入prior-report的literal地点，G包含实际 `observation_cells[p], hex(observation_u[p]), hex(phi[a])` 网格地址。72f的grid极值及幅度pool只经unravel_index转原网格地点；permanent扫描只复制既有P；e783保护邻域只选已有代表；e716分离只复制真实扫描地点并添加typed角色；892f的add_location只解析/去重literal地点，不做连续新u或phi搜索。因此每次新增地址都在P∪G。

这个来源结论**不删除历史**。保护状态、两主曲率分支、±幅度符号、typed请求、原C前缀以及每轮真筛都有算法作用；P必须包括prior-report导入的地址，不能只取warm。跨run要证明G相同必须比较实际carrier与phi字，不能仅比较N或argv。即便字段计数相同，也不能声称永久集合逐字一致。上述四完整方向和全部report union仍保留；06公开报告须如实记录其自己的模型、目标、carrier、全点和历史身份。

[完整永久地点源码归纳](2026-11-26-normalized-so3-permanent-location-source-closure.md)为8755B、SHA256 `fa536948ef12b60ca8133c3fa0ae30ac1ddbb553b51387ba38afcfaeeb552fa9`，属于来源条件说明，不新增R号，也不是连续几何证明。

## 6. 新PCG完整单准入

完整新driver/launcher/reader/cache/deriver已在 `02e4d60c5bff539a645301b6e5f888904db5d9ea` 刊出；八列frame已在 `11273fd0828c303037de6c11e4cb9d98050e1548` 刊出。没有改这些锁定字节。

独立新wrapper `run_current_pcg_complete_pair.py` 为22356B，SHA256：

`f3dd1f8137532742252aa2796f1e05ff4470fec89dfa8642b99b4b1e4a2b99d1`。

它保原789f完整science→pure控制流，只使用明确的新333e/a0e/0d65源码身份，并增加一条事先声明的参数政策：从**本run已经完成的实际父报告**继承final_damping与final_restoration_damping。不能预填旧run的0.01为新run观测。

绑定先调用4243或6420完整全体source binder及9ca完整固定父metadata检查，再核同run、complete、final NPZ SHA、5输入文件SHA、全model canonical、norm canonical/kind/ell/角参数、p/epsilon/scale、正权fraction及N。只有这些同单位条件成立，才把两个明确占位词填成报告中实际有限正值的repr与hex，并再次核report与checkpoint未改。全部其他argv元素逐项不变。原driver之后仍从真实输入完整重建并执行自身所有守卫；wrapper没有绕过它们。

完整子参数为16561B、SHA256 `b4b29103189374f0269ff5d5dcb7ba7c3bae742bdf50745731ae125f2e1f3e3a`；含112项science argv、七完整历史来源、原1×64 metric／4×64 restoration／15ray／8SOC，以及完整pure reader的final-bundle与cache检查。单准入ready12940B、SHA256 `f33901a2617c9db26157cf02061efd5c4d70effcd52bea6125b035f173fb5aa1`。

成功setup真实支付8个完整A和8个完整A*；全空间QP、原mu²I、原C/b、Phase I v3与完整非线性筛不变。任何setup数值失败按已刊完整代码诚实回原v3；中途PCG失败不能被包装成收敛。源码身份失败直接报错。所有小Gram、frame、对角及其摘录都只留runner；公开summary只取来源SHA、耗时、计数、skew和正因子等标量。

## 7. 实际成本与未测成本

仅从公开紧凑记录汇总**已经发生**的阶段耗时，不运行新的科学计算：

| 组合 | 已返耗时 |
|---|---:|
| 原04阶段1–40 | 8693.365913540001秒 |
| 原44 | 1994.287288255秒 |
| 原46 | 2004.633996777秒 |
| 原48 | 2044.3290403350002秒 |
| 上述总和 | 14736.616238907001秒，约245.61分钟 |

完整逐阶段元数据为6604B、SHA256 `ae56adbf2e4e4c457a240067d642cc51807cb9389694e32a4177f286d7fe3ec3`。仅作预算示意：若第四方向耗时与旧48相近，则约279.68分钟；相对350分钟约余70.32分钟，相对20000秒准入约余53.65分钟。**这不是预测保证**，安装、发布、等待、未知数值路径和新8A/8A*成本均未由这个简单加和支付。旧原50没有返回耗时，不能给它造实际值。新PCG是否更快、是否能接受更大步长，只能由本次实际返回判断。

## 8. 已做的纯验证与尚未做的事

控制器diff只有06标签；所有JSON可解析；十二完整对象剩余字段逐值全等。新pair实际AST/compile、重复literal key和尾空白检查通过；geometry独立完整核了父绑定、两个参数替换、原命令回写、输出互斥、非零后继续pure与硬时限边界。没有导入科学模块、执行fixture或作本地F/J/QP/root计算。

修复后的实际运行已是[45904402595/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45904402595)，其22:23:43公开索引显示recipe_start/running，源5990361、request4dffef与controlleracff吻合。实际父、所有后继新SHA、实际阻尼、PCG成本和物理结果仍待真实返回，不能由本说明预先推定。持续求解与同固定目标的精化/连续证明责任不因重建、runtime或预算而解除。

根独立逐值比较四个history-ready全对象与已刊04队列、archive002及原第四pair完整参数：每个只有id/scope/reconstruction_source变化，全部源、数值argv、父、输出、summary和cleanup同原对象。根完整读取22356B新wrapper、16561B完整双子参数及12940B单准入ready，并核原报告字段来源；尚未执行新PCG或把ready加入活动queue。
