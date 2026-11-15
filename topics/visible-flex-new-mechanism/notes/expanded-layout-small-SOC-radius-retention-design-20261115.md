# 扩池模型覆盖后的 SOC 半径保持：准确合同与当前最佳点后继设计

**状态：纸面及静态源码设计；新策略、开发例与后继科学均未执行。**

本设计提出独立的下一半径规则。它只适用于：一次完整原试步学到新的软约束行；同一个原中心上的完整扩池模型已经覆盖这些行；原 SOC 产生的修正点通过全部原验收，而且修正很小。规则不改接受点、不改 SOC 方程、不抹去原试步的学习事实，也不把旧的“所有新行必须为零”规则改称通过。

下一公开目标从 run 43744903357 的当前最佳 m7 终点直接开始，不再重播历史 m10。根代理持有全部 Git refs、请求与 Actions 权限。本设计只给出新方法、可审实现边界和必要开发范围。

## 1. 已完成证据与旧策略的范围

唯一新历史试验是 [run 43750302276 / job 132922557741](https://github.com/Rogerhu12/math-research-public/actions/runs/43750302276/job/132922557741)，source 为 b2d9ce66118948254c9c8fa376092c41b807ec62。完整结论见同目录 observed-m10-expanded-SOC-first-actual-result-20261115.md。本设计只消费已完成输出，没有重新评价几何或执行新的控制规则。

| 已观察量 | 原值 |
|---|---:|
| 历史中心 x 的两网最大 eta | 0.26636800393715654 |
| 原失败 y 的粗网 / 细网最大 eta | 0.2663651531755449 / 0.2663651530478497 |
| 新修正 z 的粗网 / 细网最大 eta | 0.2663651531755449 / 0.2663651530478497 |
| x 到 z 的真实下降 | 0.000002850761611661312 |
| y 的粗网 / 细网最大绝对曲率 | 58.00000333192753 / 58.00002409366549 |
| z 的粗网 / 细网最大绝对曲率 | 57.99996262976777 / 57.99998339149647 |
| y 新粗 / 细行 | 1 / 1 |
| z 新粗 / 细行 | 0 / 0 |
| 两个试点遗漏硬行 | 全部 0 |
| 新 SOC / 新 primary LP | 1 / 0 |
| 完整实际总步预测比 | 0.937958084659154 |
| 实际修正 common-body norm | 0.00000011483055695205024 |
| 实际总步 common-body norm | 0.00012500000000015277 |
| 模型原半径 B / 旧下一半径 | 0.000125 / 0.0000625 |

y 新增的原 ID 为粗网 72480、细网 144960，均属 metric_plus，即 soft group 1。原池从 4417/4091 扩到 4418/4092，版本从 4/7 到 5/8。重建在同一 x 上完成，selected 矩阵从 8191×159 到 8193×159。

SOC 实际使用原 scalar RHS 0.006366096552539042；报告中的假想完整 affine RHS 0.006366259406804464 没有代入 LP。finite primal、原单位残差、精确盒和两网实际门全部保留。

冻结 next_soc_hold_trust 仍给 8 个 false：

| 类别 | 数量 | 准确原因 |
|---|---:|---|
| 单次原试步与接受 SOC 的 result 标签 | 1 | 历史专用 driver 的标签不同于普通连续 outer |
| 接受下降、同模型绑定、ratio、修正 norm、总步 norm | 5 | 旧函数读取 accepted_SOC_base_total_step_diagnostic，本次正确使用独立 accepted_rebound_SOC_base_total_step_diagnostic |
| 原模型与 correction 池版本相同 | 1 | 本次定义上就是原 4/7 到新 5/8 |
| 两个试点新增软硬行全零 | 1 | y 的 1+1 新软行是真实学习事实 |

其余 9 条旧条件为 true。上述分类不改变任何旧 guard；有完整扩池证据也不能自动豁免原“新行全零”。新输出必须完整保存旧 next-radius、success streak、failed-conditions 和原 y 学习记录，另加新策略条件表。

实际证据只说明此历史试点被一次小 SOC 修复，不证明新保径策略优于旧策略。历史 z 的 eta 高于当前最佳 m7，后继不能退回历史 z。

## 2. 对象、两个模型及实际位移

令 x 为真实已接受中心，y 为第一条 alpha=1 的完整失败 primary 试点，z 为唯一 SOC 修正后通过原两网门的试点。令 d=y−x、c=z−y、s=z−x，全部是原 binary64 数组的实际差。

P 是 primary 的原粗/细有序 ID 池，P+ 是 y 学习后的有序 ID 池；B 是该 primary 的真实半径。159 独立坐标、159→163 映射 M、原物理宽度、原参考和 source cfg 均不变。

原 primary 的历史 signature 只记录 P。扩池 selected 和 complete factories 在同一 x 上生成另一模型；它的最终 binding 必须在两个 factories 都完成后取得。两种签名不能强迫整体相等，也不能混写。最终 binding 必须包括实际 x、M、原宽度、P+ 行序、版本、选中 J 和最终 observable/model identity。

## 3. 独立新规则的全部条件

建议 policy：

**same159-covered-expanded-pool-small-SOC-retains-model-radius-v1**。

先实际调用冻结旧控制器，取得 B_old、streak_old、old_report。仅下列条件全部成立时返回 B、0；否则逐项返回原 B_old、streak_old。

### 3.1 原验收及唯一一次执行结构

- 恰有两条 full trials、一次 correction。第一条是 alpha=1 的未接受 primary，第二条是 alpha=1 的已接受 SOC；无 backtracking、第二次 SOC、递归扩池或另一拒绝。
- 两条都有真实完整粗/细值及原 gate flags。
- y 和 z 的真实两网 eta 下降都达到原 minimum_accepted_eta_decrease_exact=1/10000000。
- y 除曲率相关门外的原全部个别门通过，至少一个原曲率门失败。仅允许相应汇总 hard/admissible 标志随曲率失败而 false，不能豁免其他硬门。
- z 通过原全部个别门、cap/box 及两网完整实际门。
- 两个试点的 omitted-hard 数均为零。本次新保持规则不适用于新增硬行。

新规则只改变接受 z 之后的下一半径，不参与 z 的接受判断。

### 3.2 新软行已经被同中心完整模型覆盖

- 学习事件非空，P+ 保留 P 的全部 distinct IDs。
- 从 frozen 完整原网格 point_count 核每个差集 ID 的 group；P+\P 全部为 group 0 或 1。grid definition、点数、ID 上界、顺序均严格核实。
- 各差集个数等于 y 原 new-coarse/new-fine 记录；原学习记录不改。
- 原 capture 的 x/y SHA、实际 d、bitwise apply 重现 y、原池/新池 SHA 和版本都与当前唯一 rebound context 对齐。
- 冻结 rebuild_failed_context 在 x 上重建全部 P+ 的 base/J/groups/tolerances。原坐标、M、物理盒、宽度、step_scale、trust 和 objective 权重由原 validate_rebuilt_primary 核同。
- rebuilt selections 的每个 ID 与 P+ 逐项相同；完整 grid 定义与 frozen y full views 相同。
- correction 原 primary binding 指向 P；rebound binding、complete-observable binding 和总步诊断都指向两个 factories 完成后的 P+ 模型。
- z 新粗/细行和遗漏硬行全部为零。接受后真实有序池及版本仍与这个 rebound context 完全相同。

控制器读取内存中的唯一 ReboundContext，使用 frozen old_ids/new_ids/full views 形成覆盖证据。不能只信一个孤立 covered=true。报告保具体新 ID、组别、计数、池 SHA/版本及两类 binding；没有可核 context 就回旧控制器。

### 3.3 原 SOC 数学、完整总步质量与小校正

冻结 rebound_budget 和 solve_rebound_correction 保持原样：实际 y 残差、x 上扩池 J、真实 d、原 scalar RHS、原 fraction/floors/retention/scaling 和原单位残差限不改。要求真实 LP 启动、finite primal、success/status 和原 row/bound residual gate 通过。假想 full-affine RHS 仍只报告，不代入。

总步证据使用原 complete-affine actual_total_step_diagnostic，输入 rebound.primary 及真实 x,y,z：

\[
 R_{\rm total}=
 \frac{\eta(x)-\max\{\eta_{\rm coarse}(z),\eta_{\rm fine}(z)\}}
 {\max(0,\eta(x)-\eta_{\rm target})-\widehat\rho_{x,P^+}(z-x)}.
\]

\(\widehat\rho\) 是完整原两网的 affine-e/f convex spectral slack，保原 epsilon、constant/outside 分支和实际总步；不是 y 处 correction-model ratio，也不是旧 P 的 selected 预测。冻结实现以真实 eta(x) 的 target excess 构造分母，不能擅自改成 \(\widehat\rho(0)-\widehat\rho(s)\)。

要求：

\[
 R_{\rm total}\ge 1/2,\qquad
 \|z-y\|_{\rm common}\le B/10,\qquad
 \|z-x\|_{\rm common}\le 11B/10.
\]

分母须有限且超过原 improvement floor。任一预测、位移、norm 非有限或未绑定就回旧结果。common norm 从原 M/163 物理宽度与实际 rounded 位移得到，不用 nominal correction、auxiliary objective 或普通159无穷范数替代。

完整 JVP 费用保原 active clock；新控制器只读已有总步诊断，不额外调用几何、J、JVP、LP 或 ordinary values。

### 3.4 只撤销本次唯一曲率缩径，绝不增长

还要求旧原因表中：

- 两条 trial quality 均无 poor-complete-ratio 或 coarse-only-poor-ratio；
- y 的 request_shrink 仅由实际曲率失败引起，z 不请求 shrink；
- trigger_trial_indices 恰为 [0]；
- current_trust 仍等于 B，无更早 rejection/backtrack/另一缩径；
- 旧映射控制器结果恰为原 shrink_factor×B，原 shrink_factor 仍为 1/2。

全真时保持 B、success streak 置零，不增长。下一 primary 必须从真实 z 重新构造中心模型；不能把 x 上数值 cuts/J 当成 z 上数值 cuts/J。

该规则是明确的新控制启发式，不是 B 内全可行、连续域证书或收敛定理。

## 4. 输出和失败语义

每模型追加独立 expanded_layout_SOC_radius_retention，包含：

- 新 policy、全部 checks/failed-conditions；
- 原 17 条 guard 原报告及原 next-radius/streak；
- 原学习记录、新 ID 覆盖、原/扩池/complete 三类 identity；
- x/y/z、实际 d/c/s 摘要；
- 原 scalar RHS、未使用的 hypothetical full RHS；
- complete ratio、common norms、B 和最终 next B；
- 接受后 current layout 与 frozen rebound layout 的一致性；
- 原接受点/门/学习记录均未改，策略仅决定下一半径。

缺字段、类型错、非有限、binding 不符均产生 false 并回旧结果。不能将缺 new-rows 当零、缺 binding 当相等。证据提取异常也只记录并回旧控制器，不能丢掉已经真实接受的 z。

来源、物理/坐标/cfg/bank 校验错误在科学前停止；它们不属于可忽略的控制证据缺失。

## 5. 唯一后继输入：当前最佳 m7

输入为 [run 43744903357 / job 132905938795](https://github.com/Rogerhu12/math-research-public/actions/runs/43744903357/job/132905938795)，source 5fa2424a6316b1daa8453864ce223b128a43d72f。

runner 读取已完成日志的 EXPANDED_SOC_COMPLETE.future_direct_checkpoint 及七条原 MODEL；旧 optimizer/primary 执行次数为零。原日志为 3,194,767 bytes，SHA256：

14cafc198a1df4e7de2882994b37b9dffcf4284daacc49c670a9f65240926c3d。

| 当前最佳量 | 原来源值 |
|---|---|
| m7 canonical physical SHA | 981e092c54a5a7059bc75ffaea2f2c8bfa47c0b4c2f5932a67bd3fc74cee5376 |
| 两网最大 eta | 0.26634752076125723 |
| 最大绝对曲率 | 57.99998852110966 |
| terminal trust / success streak | 0.000125 / 0 |
| 完整粗 / 细池 | 4418 / 4188 |
| 原记录池版本 | 1 / 4 |
| 粗 / 细容量 | 12000 / 6684 |
| 完整 norm bank | 11 entries |
| bank state SHA | d5b1b9d6128f05e0003baa1c22b109d0d9d4fb6598bfa0ba93f0ec969c127cb8 |

检查点已有完整 original reference163、selected159 exact binary64、selected physical163 exact rational、ordered pools、bank context 和完整 ordered entries。保持同参考/同物理身份，不能 reanchor height 或以浮点近似豁免 SHA。继承 terminal B/streak，不重置到最大半径。

source cfg SHA 必须仍为：

b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6。

## 6. 11-entry bank 的正确恢复

冻结 ExpandedPoolSOCObjective 构造器只接受旧 9-entry bank。不能传假9再改字段，不能把当前11条删成旧9条。新 checkpoint-aware 输入合同为：

1. 读取完整 ordered entries/context，不重播 old event、不用源 e/f 重新归一化 normal。
2. 严核 original soft ID/tag/group/grid、三个有限 binary64 normal、exact-binary64 norm²≤1、distinct key、原顺序及 source binding。
3. 原 NormDirectionBank 只装 context 和 ordered entries；无旧 numeric A/b、旧 J、旧 optimizer。历史 insertion/rebuild 计数只作来源 metadata，本次新计数从零，恢复条数另记。
4. 第一份当前中心完整模型 bind 后，在第一 LP 前核 context、state_digest 和11条都准确匹配原值。
5. 各后续模型用原 bank.rebuilt 和当时中心 de/df 重建支持面，保原单位球合法性，不复用旧数值 cuts。

新 policy 只放显式 kw、evaluation definition 和 request，不写入 cfg。原 factorization definition 含 cfg digest，不能以“仅元数据”忽略 bank context 改变。

可用一个显式子类继承 ExpandedPoolSOCObjective 以保 outer 类型合同；新 constructor 从原 RememberingCompleteObjective 的初始化入口建立 bank、完整 registry 和上述 checkpoint 来源，明确不采用仅限旧输入的9条构造合同。不是构造后伪造原 expected size。已有 capture/rebuild/SOC 数学和 binding 检查不改。snapshot 对旧21-event标签另列 inherited 来源，不能误报本次重播了事件。

## 7. 最小新增源和已付缓存接口

拟新增：

- frame_metric_expanded_layout_hold.py：独立 controller、live context coverage、checkpoint-aware objective 与 bank gate、并列新/旧 metadata。
- frame_metric_expanded_layout_hold_recovery.py：从冻结 expanded outer 显式派生；只接新 radius-update 和已付 y-cache恢复，原 primary/SOC 数学不改。
- frame_metric_expanded_layout_hold_development.py：只查新增 controller/checkpoint/必要 outer 接线。
- direct-checkpoint transfer/audit 和独立 request/workflow：根代理统一接线，冻结时列全递归绑定。

不 monkeypatch 旧函数或模块全局。primary 与 rebound registry 保持显式分离，不能将 rebound model 插入旧主模型 zip。

新 outer 必须在学习之后、capture 之前调用已付 restore_failed_y_layout。学习使 epigraph selected cache 失效，但普通 y 几何仍可留存；该 helper 用原 evaluate/fine_decision 重装布局，真实计数增量须记录并为零，miss 则按原预算语义停止，不能假称零。

此 helper 已在成功公共科学中到达真实 full_views/capture，不重跑其 positive/charged 开发。冻结旧 outer 本身仍没有此修复，其原真实扩池分支曾为零；直接复制旧 outer 会重新带入已知缓存错误。

## 8. 必要新开发、单次科学与输出

所有新增检查首次只在公开 Actions 执行：

- 一个小人工完整 qualifying context：旧同布局规则仍 false，新规则只保持 B、不增长、streak0，原 learning 不变。
- 对同一小 fixture 的定向拒绝：新 hard ID、z 新行、覆盖/最终 factory binding/版本不符、ratio 缺失或分母无效、校正/总步过大、旧 shrink 有其他原因，全部精确回旧结果。
- 普通 primary 与同布局 SOC 逐项回原控制器，不重旧17条 suite。
- 小人工 ordered checkpoint bank：真 context/hash/order 恢复；重复 ID、非法 normal、错 hash/reference/cfg context 拒绝。真实 m7 payload 不放 developer fixture。
- 若需要 outer stub，仅查“学习→已付cache helper→capture/rebuild→唯一SOC→新radius report”的新增顺序与 registry，不调用旧科学或旧开发入口。

旧10、旧7、已付 cache positive/negative 都只按源/hash/回执复用。

后继只从 m7 运行一个新方法 stage，预算仍为12共享LP、40共享ordinary values、120秒原active clock、每SOC至多10秒且受剩余active限制。不增 reserve，不改 gates/RHS，不播m10，不重旧optimizer。来源恢复、初始化值、active算法及final grids分账，不以初始化时间冒算法active时间，也不从total隐藏它。

新规则 qualified 之后，必须报告是否真的继续用了保持的 B；若预算已尽，仅说“保径发生、未观察到使用”。若本次没有触发新规则，准确记录未检验；不以普通接受点数量作归因，不重复同 stage 等待触发。

完整检查点只在 runner 临时及 job stdout；公开保源、参数、run/hash与人读结论，不发布可重算 payload。

## 9. 静态来源与责任

以下均只读，未执行：

| 来源 | bytes | SHA256 |
|---|---:|---|
| frame_metric_height159_soc_hold.py | 51237 | c6fb9d46840c64f9b6a43146ebbece8928e78f9efe609a624cf8ee4cc1da47de |
| frame_metric_expanded_pool_soc.py | 31656 | 4226ff562467cf49a62b71de4b0300bb69bae4abe1df1c04ebb2845171f719bf |
| frame_metric_expanded_pool_soc_recovery.py | 38489 | db447f3395b3754a7adc95432fbb288aed2efe7393382bf6c6cbf9bc49ca963e |
| frame_metric_norm_direction_memory.py | 20436 | f1e62dd9525b5d5b9fe692b903b1b976e04fc46fc8b221788ec60b7b7338def1 |
| 已付 m10 driver | 67762 | 91d3112d1ce4cb132ac43353af9613940f8c5ddb5ae6cbf972053a85529914be |
| 其中同 y cache helper 单独文本 | 3025 | 5fe5e49de48ce2fc37c72d4319616a44149204286c4cfe584b7aa1efeaad1e79 |

tail_cost 负责新设计。mechanism 只作窄合同纸核：同 x/新池对真实 z−x 的完整预测、无效分母回退、原学习与旧hold false 保留。它不是新源码/开发/科学已通过的声明。根代理负责最终审阅和唯一公开调度。
