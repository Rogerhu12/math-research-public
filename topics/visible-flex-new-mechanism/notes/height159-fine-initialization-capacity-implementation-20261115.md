# 五高度细网初始化容量修复：实现与首次公开入口

日期：2026-11-15。状态：新源码已完成静态审读及 AST 解析；新增人工入口和实际算法均未执行。源码不含新的曲面定义、门、LP 目标、步长政策或预算。

## 1. 已有失败与本次最小变化

run 43707849695 / source f9d8da4e9a7b783caa51b6da4790c473fe471920 / job 132792751708 的诊断明确给出：

> full eleven-group fine pool must retain every old row within unchanged capacity

原159输入阶段继承 fine 4049/4096，随后原 initialize_fine_pool 尝试保留全部旧行并添加每径向的两组度量最坏行及四组曲率最坏行，合并超容量。该阶段零 LP、零 Jacobian、零活动优化秒；SOC 条件持径没有调用。八个新增诊断检查通过；这不把失败阶段改称成功，也不补造上一轮未保存的内部异常。

本次保留失败及全部旧源。在两个明确阶段开始前各应用一次预先声明的容量规则，不删除任何旧行：

$$
B=N_r\{2\min(N_\theta,k_{\rm metric})+4\min(N_\theta,k_{\rm curvature})\}+2L,
\qquad C_{\rm new}=C_{\rm inherited}+B.
$$

这里 $N_\theta$ 是完整 fine 角数，$L$ 是该阶段继承的已记录度量峰数量。本配置 $k_{\rm metric}=2$、$k_{\rm curvature}=1$，所以 $B=8N_r+2L$。重复行只减少实际 union。原有 $C_{\rm inherited}-n_{\rm inherited}$ 个学习槽不会被这一次强制初始化消耗掉。

后续 learn_fine_violations 的原固定容量拒绝/预算路径保持；没有运行中自动扩容循环。第二次预留以前一次实际容量为起点，另行记录，不能隐藏在第一次名义参数里。

## 2. 新文件与复用边界

新增两个源：

- [frame_height159_fine_capacity.py](../scripts/frame_height159_fine_capacity.py)：纯整数容量规划、读取原 stage 已记录的初始化 union，以及仅针对新增容量接口的数组 fixture。
- [frame_metric_height159_capacity_soc_hold_audit.py](../scripts/frame_metric_height159_capacity_soc_hold_audit.py)：新编排和元数据适配。生产求解直接调用未修改的原159与条件持径驱动。

独立钉住的旧依赖包括：

| 旧源 | SHA256 |
|---|---|
| frame_metric_height159_soc_hold_audit.py | 172567136e6cfd9373cdd41556555a3cb92938dc2ee8c6e238f42dcb13ab927e |
| frame_metric_height159_soc_hold.py | c6fb9d46840c64f9b6a43146ebbece8928e78f9efe609a624cf8ee4cc1da47de |
| frame_metric_budget_recovery.py | ba3e2becec3ad750ef8818711d8034003f3077877d39115925c308d123dec9ff |

原第六阶段六源码的准确绑定继续由原 require_frozen_prefix_sources 执行。新实现未复制、替换或 monkeypatch 科学循环、objective、Jacobian、原 setter、门、LP、控制器或科学打印数值。

仅原 orchestration 的必要流程有两处新增配置接口：原154 handoff 成功后，给第六阶段预留一次；第六阶段原完整 handoff 成功后，给条件持径再预留一次。相对于旧生产编排的完整逐行差异可由两源直接比较。

## 3. 第六阶段是新的输入生产配置

前五个必要前缀——growth、strip、scaled SOC、103、154——各调用一次，原来源、参数、真实门、输出消费和费用分账均保持。

原 height159.handoff_restored_tail154 先完成全部真实检查。reserve_prepared_stage 此后只复制配置与描述性 replay，不重建 runtime field、exact H、原159/163系数、永久 c0、g、b0、帽高门或控制器。配置仅允许两键不同：

- max_fine_physical_pool_rows；
- fine_initialization_capacity_reservations。

第六次执行仍调用冻结的 height159.run_audit，但容量配置已经改变，故明确称“新容量159输入生产”，不能称原全参数精确恢复。它可能改变实际行池、LP 成本、数值轨迹与最后接受态。首次实际输出需要从本次实际初态计算其自身下降，不强求历史 b429 或其他 canonical。

原完整 handoff 不被旁路：它仍检查实际执行的新 configuration、源码、输入、准确系数、坐标映射、原物理盒、精确零总帽积分、两网实际门、全部行池和真实控制器。通过后，外层才重新标明输入生产的算法范围。条件持径从这个通过原门的实际末态开始；它的下降与第六阶段、前五次输入恢复分开。

原 controller 的 radius/streak 不被重置。若真实半径低于原最小半径，原退出路径仍有效。增加行容量不能授予重置半径、重新求解或改门的许可。

## 4. 诊断、日志和临时报告

每阶段在执行前打印原/new configuration hash、容量、旧池数量/hash、$N_r,N_\theta,k,L,B$、原剩余槽和一次预留身份。执行后仅从已有 snapshot 历史读初始化 union，不重新选行、求值或计算几何，打印：

- 原初始化实际返回的 union 数量/hash；
- 实际新增唯一行数和原11组计数；
- 所有原 ID 是否保留、剩余学习槽及结构上界是否兑现；
- 原 stage.status/error/budget；
- 若原 initializer 未记录返回值，明确不可用，不补造 proposed union。

调用原驱动时，原 stdout 暂存在内存；输出适配只替换“六个阶段全是旧参数恢复”的旧文字标签。所有原科学数值、失败、模型、trial、SOC、两网门、controller 和时间仍逐项输出。原驱动异常若已打印内容，也先输出该内容再走原失败摘要路径。

最终临时报告只有新的 metric_height159_capacity_soc_hold_stage。完整科学记录仍来自原驱动；另保 invoked_frozen_driver_schema/status/source_files_sha256 作为准确调用来源。原旧计数标签保存在 inherited_driver_counter_labels，外层用五次旧恢复、一次新容量输入生产、一次持径调用明确分账。原报告中的 legacy restoration 键仅为兼容结构；algorithm_stage_scope 与第六项 purpose 明确它不再是旧全参数恢复。

顶层 new_scientific_solver_calls 明确计新容量输入生产与持径两个阶段的实际驱动调用之和；完整调用时为2，输入生产失败且未进入持径时为1，在此前 guard 失败时为0。这是阶段调用数，不是 LP 次数；原 hold 单阶段计数保在 inherited_driver_counter_labels，各自的 LP/值/活动秒仍用原记录。第六阶段 handoff 摘要的固定旧标题也单独改为 NEW CAPACITY159 INPUT PRODUCTION，其余原数值行不动。

每个阶段的容量诊断均进入原生 summary 和直接 stdout。若原阶段发生异常，新增 wrapper 保留其原 error 和最后可用 checkpoint；不会据“可留更多行”把异常视为可用输入。若发现已记录 union 与声明上界不符，则报新接口错误，保原记录而不修补机器数据。

运行临时文件在同 job 消费后清理。遵守根 README15，只发布源码、参数/run/SHA 及人类结论，不保存可重算完整输出、summary、状态向量、机器证书或 artifact。

## 5. 资源范围

每一阶段仍为原12 LP / 40粗细完整值 / 120活动优化秒，原10秒 SOC LP 限制和独立最终两次同态值检查保持。两个阶段各自的原预算、初始化费用、prefix费用和总壁时必须单列。容量变更不是增加这些求解预算。

新增 selected-J 的单份存储最坏上界为 $B\cdot159\cdot8$ 字节。例如 $N_r=160,L=0$ 时是 1,628,160 字节。这仅是该数组的容量增量，不是峰值 RSS 保证；原几何163列 Jacobian的构建成本没有减少。

容量属于算法/评价配置，不加入物理 g、b0、准确系数或场定义。保全部行使问题与旧初始化欲构造的 union 一致；增加后续可保存行数也可能改变学习轨迹，仍须如实报告。

## 6. 首次公共新增开发范围

新入口为 --check-capacity-only；--check-only 是同一新增入口的兼容拼写。它们均不调用已通过的旧15个检查，也不重复旧8个诊断检查。开发代码已写但未执行。

纯数组 fixture 直接使用原 MetricRecoveryObjective.set_fine_pool、initialize_fine_pool、learn_fine_violations 方法，不构造其真实 objective，不构造曲面、不调用 geometry/J/LP。它覆盖原容量失败、新容量保留同一 union/旧余槽、原 ID 与峰位置拒错、k 截断/重复峰、后续固定 cap、两阶段一次性及错误时不补造 union。

新 orchestration fixture 用明确字典桩测试五旧前缀/新输入生产/持径各一次、两次容量边界、原半径及状态不变、失败在 handoff 前保 error 且不调用 hold、单原生 stage、summary 字节绑定、公共仓库 guard、开发 CLI 不调用科学或旧套件。科学方法仅由桩替代，未把这些人工结果写成已通过。

本地只进行了文本生成、差异比较、SHA 和 AST 语法解析，没有 import 新模块或执行这些函数。首次公共开发通过后才进入真实阶段。

## 7. 接线参数

推荐 lane：metric_height159_capacity_soc_hold。

原生 stage：metric_height159_capacity_soc_hold_stage。

实际入口：frame_metric_height159_capacity_soc_hold_audit.py。原24输入、全部输入 SHA 和98个 CLI 参数原样保持；仅 --out 的文件名改为 metric-height159-capacity-soc-hold-audit.json。

新增开发输出：metric-height159-capacity-soc-hold-development.json。
原生临时 summary：metric-height159-capacity-soc-hold-audit-summary.json。

workflow 只需新增 lane/driver/新原生 summary跳过项、compile 两个新源、调用新开发入口并继承原实际98参数。publisher 只新增对应分类；metadata-only主体不变。两新源的最终 hash 与既有旧来源绑定写入 request。当前接线/派发由 root 负责，本稿不宣称新 lane 已执行。

