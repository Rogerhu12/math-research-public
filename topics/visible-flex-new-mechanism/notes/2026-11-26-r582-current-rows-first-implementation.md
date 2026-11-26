# R582 从真实 97q 继续：先完成当前全部后端硬行，再支付 fine 与峰交换

日期：2026-11-26。状态：源码与明确新输入准备完成；本地仅 AST、文本与已付公开日志解析，未执行科学。主课题未完成。

## 1. 这次改变针对哪条实际失败

直接父运行是公开 `45850216756/job140014319556`，源提交
`2f9f5939dee3a41f8436c1a90567388517e7ea73`。其完整原收据为
`notes/2026-11-26-r582-paid-angular-original-terminal-receipt.md`，已由提交
`e43ae41a7f4708e8424e907955bbe6cceab9569d` 公开。

该运行的两次 metric 中间候选都尚未满足已经加入的 metric 行。最后一次实际粗网 metric 峰为
$.002493756000619629$，epigraph 只有 $.00022280580520586733$，但 callback 已先花完整细扫，然后被新的径向曲率峰迫使 `ExchangeGrid`。原五个 outer 都在第一个完整 callback 结束，没有自然 `OptimizeResult`。两次 `urgent_missing_angular_peak` 都为 false；角翻倍是随径向重启附带采用的不紧急提议。

本次不原样重做这些 outer，也不只把角上限再翻倍。它保留实际末态与全部物理证据，改变 **何时执行完整细扫和峰交换**。

## 2. 准确继承与新首网

实际保留向量是 97 维，binary64 SHA256：
`eb37b419ccb59cfca020b21290953ebf36353984dc409ede51832991e9e19635`。
固定 $p=.181$、$\epsilon=.0010000000000000009$；原实际 trust、原提议 trust 与本次初始 trust 都为 2。

| 身份 | 径向与角网 | 是否已经在父运行采用 |
|---|---:|---|
| 父实际约束 | $185\times1536$ | 是 |
| 父完整 fine | $10934\times3072$ | 已完整观察 |
| 父未采用 proposal | $189\times3072$ | 否 |
| 本次首约束 | $189\times1536$ | 本次真正构造后才算采用 |
| 本次 fine | 原 10934 圈加新约束/中点，角数 3072 | 本次完整扫描后才给新资格 |

四个待加径向点全部采用，原所有 3072 个细角与 10934 个细径向位置全部保留。原 $3072$ **约束角** proposal 单独保存在输入和所有检查点中，注明没有在本次入口采用。理由是原提议来自尚不满足现有 metric 行的中间候选，且未触发紧急角漏峰；本次先让现有全行系统真正迭代。

之后若一个已经满足当前全部后端行的候选确有新的角漏峰，本次仍输出并保留提议。每个角见证包含 field、实际 $s,\theta$、细角值、同圈旧角最大值、当前 epigraph/覆盖值、角差及其候选 q 身份。只有这类新见证才会再次请求角升级；它不是把原 proposal 删除或伪称已算。

原径向容量 769、约束角容量 1536 保持不变。若真正的新证据仍需要更高容量，记录完整未采用 proposal 与实际末态，不把容量终止当数学完成。本次第一份 metric Jacobian 有
$[9(1536/4+1)+1]\cdot189=655074$ 行及 98 列，一份 binary64 矩阵为 513578016 B；这不是整个后端的总内存，也没有声称最大容量网已经实际分配过。

## 3. 完整后端行优先的 callback

原 `NonlinearRows.fun`、解析空间 jets、参数 AD、97q 参数空间、参数盒和完整 fine 接受公式全部保持。新的 callback 按以下实际次序工作：

1. 记录原 SLSQP 候选 q、epigraph、p/stage/outer 与是否为自然返回点。该记录明确不是已接受态。
2. 调用**同一个传给 SLSQP 的 `current_rows.fun(value)`**，读全部现有不等式行；同时检查原实际信赖盒/参数盒。此处含原两条 metric 谱范数 epigraph 行，没有另造较弱替代残差。
3. 若最大行/盒违约超过原 $10^{-8}$ 容差，只输出 `FINITE_LOCAL_TAIL_BACKEND_INFEASIBLE`，记录真实费用与原候选，随后返回同一次 SLSQP。这个中间点不触发 fine、接受或 `ExchangeGrid`。
4. 只有当前后端行已经合格的候选才执行原完整 fine 扫描，再按原几何/metric 条件决定是否保留，并根据真实未覆盖峰请求交换。

后端自然返回若仍不可行，保留完整原 `OptimizeResult` 及原行违约身份，不能把它替换为实际 q。实际 q 只来自此前完整 fine 已接受态。外层仍按原规则调整 trust/采用已观察 pending；没有用停止信号冒充数学否定。

每次后端启动还输出 `FINITE_LOCAL_TAIL_BACKEND_START`，包含真正初始 epigraph、全部行数与初始行违约。该行值随后由同一 SLSQP 算子 cache 复用，避免另开预检计算。

新 `last_backend_callback_candidate`、`last_completed_full_scan_trial`、`actual_retained_state` 和 `last_natural_OptimizeResult` 四类状态分开。若时钟在原行读取中到达，候选记录中的 `current_complete_rows_check_completed=false` 保留未完成身份；若原行已读但未作 fine，也不会给它一个旧 fine scan。

## 4. 严格同态复用，避免再读已经付完的相同点

同一个 p、q binary64 身份、完整 fine 径向网身份和角数完全一致，而且原扫描明确 `complete_fine_scan=true` 时，下一 outer 的起点直接复用该已付扫描。相同实际模型网也复用原准备对象。任何 p/q/网变化都重新评估，没有跨状态移用资格。

自然 `OptimizeResult` 若与最近完整细扫的 p、q、epigraph、fine 网完全相同，直接复用那个完整判断；已经发现的 pending 仍照常采用。只有这个严格同态才省去重复终态扫描，不将某个相近向量或相近网视作相同。

所有曾构造的旧 fine 径向位置在下一网中继续保护，包含本次新增中点；添加约束不会让旧观察中点从物理库消失。实际构造网 p 与实际保留态 p 继续分别记录，防止新 p 初扫中断时把旧资格挂到新 p。

## 5. 科学范围与费用

没有新变量方向、没有改物理模型、没有改固定 $p$ 的阶段目标、没有重跑原 97q 方向核或七点 Hermite/旧峰诊断。原两次运行的全部成本在 ancestry ledger 中保留。由于完整内部场仍没有存为科学数组，本次必要的同口 dense/material 重建依旧是新费用，单独记账。

新增计数区分原行检查、因现有行不合格而省去的 fine、真正完整 callback fine、严格同态复用，以及原自然后端返回。额外 callback 行查询可能命中原 cache；若产生新 value 工作，计入实际 `Rows` 与 model 计数，不能直接把它等同于优化器自己的 `nfev`。

R604 observer 仍只读取本次已有 geometry blocks，保留原有限网格、FFT、ODE/Hermite 与曲率平滑的限制。R608 已单独证明真实圆参考全尾，但紧区间参考条件和有限非圆连续扰动范数都尚未支付；本次不借该纸证授予任何非圆全 reach。当前完整主目标仍需有限幅度、固定 $g$ 后的真实精化与全部连续/全点对条件。

科学时钟仍为 2400 s，预留 30 s 检查点；job 不超过 50 min。入口继续真实部分 clone/pull 公私 main、核对应根与课题规则及 QUEUE，源码和 23 个绑定先做完整 hash 校验。科学只 stdout，没有 artifact/cache 或原始科学数组入库。

## 6. 新配置的公开来源逐项映射

新 stdin 配置 254768 B，SHA256
`bfb95ba6682cc0cf5c97b257af2836db9eae515f1490dd5314219e381d10762b`。
它是必要续接参数，通过本地 CLI 随 request 提交；没有通过集成上传、分块或编码大输入。

- `original_source_state_json` 是父公开 request 中逐字不变的 233584 B 输入，SHA256 `89eb8404f2bbf8f5601b9b246368263412d6b359c19a0efc94481909a8e0b4bf`。
- `origin` 是父公开 run/job/source/request/input/raw/FINAL 的固定身份；不包含私有正文。
- `resume97_state` 的实际 q、scan、trust、网、pending、proposal 均直接取父公开 FINAL；各 identity 只是这些公开 binary64 数组的 SHA256。10934 圈由父输入的 10905 圈、父实际 185 圈及其中点准确重建，入口核整个数组 hash。
- `source_metric_callback_evidence` 是父公开 outer 3、4 的原 PROGRESS 小字段：原候选 q identity、原 epigraph、实际覆盖、pending/urgent 身份。
- `source_unadopted_angular_proposal` 固定原 proposal 及来源 trial identity，并明确本次不采用的范围；这是已公开结果的实施选择。
- `new_paid_cost_ledger` 的 counts/geometry/model/field/observer 计数直接取公开 FINAL；Jacobian 和扫描计时来自对应公开原记录求和。时钟包含关系明确，不混加嵌套耗时。

本地只运行了这些公开文本的解析/hash/AST，没有 import 或执行科学源码。新算法实际是否使 metric 收敛，留待这一明确新 scope 的公开真实运行；当前不能预报为成功。
