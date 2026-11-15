# 五高度输入阶段的细网初始化容量预留：准确失败链与最小新算法设计

日期：2026-11-15。状态：静态源分析与设计；没有运行新的人工检查、几何或求解。

## 1. 本次错误已经定位，保留历史失败

公开 run 43707849695、source f9d8da4e、job 132792751708 的新增诊断实际输出为：

- 原五高度阶段 error 为 ValueError，message 为 “full eleven-group fine pool must retain every old row within unchanged capacity”；
- 继承 coarse 为 4,421/12,000、fine 为 4,049/4,096；
- 该阶段零 LP、零 Jacobian、零活动优化秒；新 SOC 条件持径阶段未调用；
- 八个新增纯诊断检查通过。

这次证据关闭了上一轮丢失内部 error 的信息缺口。它不能反过来补造上一失败运行的未知异常，也不把两次失败改称科学进展。

旧 frame_metric_entry_tail_height159.py 的初始化依次执行：安装接受初态及 reference、coarse 扩池、initialize_fine_pool、preflight、首次 linear_rows、begin_optimization。错误发生在前述细池初始化，而非首次 Jacobian。

## 2. 为什么确实是容量，而不是坐标或丢旧行

frame_metric_budget_recovery.py 的 initialize_fine_pool 先令 chosen 包含全部 inherited fine IDs，然后逐径向加入：

| 组 | 每径向的最坏行数 |
|---|---:|
| 0、1 两谱支 | 各 min(Ntheta, k_metric)，目前 k_metric=2 |
| 7、8、9、10 四曲率行 | 各 min(Ntheta, k_curvature)，目前 k_curvature=1 |
| 已记录 metric 峰 | 每个加入两谱支原 ID |

排序和索引生成均沿原完整网格，已记录峰仍由原位置容差检查。随后调用未修改的 set_fine_pool；其统一拒绝条件包括空池、越界、缺旧行和超过配置容量。

这条调用中 chosen 明确包含全部原行，原行已在上游真实 handoff 核过，自动索引位于原 11 组网格，继承池非空；峰坐标不匹配会先发另一个具体错误。因此本次实际 message 与已知调用链合起来，准确定位到新增 union 超过 4,096。至少有 48 个新增唯一 ID；没有输出完整 proposed union，不能补造其准确数量。

初始化强制每径向种子与后续学习的控制流不同。后续 learn_fine_violations 超容量时已有明确 budget 返回并保留最后接受点；初始化直接使用严格 setter，所以在任何 LP 以前以 error 停止。

## 3. 一个不猜任意新常数的容量规则

设原 nominal fine 容量为 C，已有行数为 n，径向数 Nr，完整细角数 Nt，已有峰记录数为 L。定义准确整数上界

$$
B=Nr\{2\min(Nt,k_{\rm metric})+4\min(Nt,k_{\rm curvature})\}+2L.
$$

本配置通常即 B=8Nr+2L。它是本次原初始化逻辑最多可能新增的行数；重复行只会减少实际 union。定义新 stage 的固定容量

$$
C_{\rm new}=C+B.
$$

则初始化后行数不超过 n+B，所以仍至少保留原有的 C−n 个学习槽。此规则只支付强制初始化的结构最坏增量，不增优化 LP、真实值次数或活动时间预算；不删旧行，也不放松任何实际几何门。

这里选择保留原空槽，而非把容量恰设为实际 union；后者可能在初始化后立即没有任何学习位置。也不直接选择一个与此次初始化无关的任意倍增容量。规则在 stage 开始前固定，后续学习中不得继续自动增长。

如五高度容量变体完成后要进入条件持径 stage，其控制器同样会强制初始化。那个 stage 须从实际继承的 C 单独应用一次同一公式，并列记录第二次容量预留。不得静默覆盖。两个 stage 的最坏累计容量界为原 C 加两个各自 B；峰数按各自真实已保存记录定义。

## 4. 这是什么变化，不是什么恢复

旧 growth、strip、scaled SOC、103、154 五个必要前缀及全部输入字节/源码参数保持。第六步明确称“同冻结五高度实现的初始化容量变体输入生产阶段”，不能仍称原完整参数的精确恢复。

可在原 height159.handoff_restored_tail154 完成全部真实检查之后，对其 returned prepared tuple 作窄的配置复制：只改变 max_fine_physical_pool_rows，并附上原配置 hash、旧/新容量、Nr/Nt/k/L/B、原池行数/hash 和新算法定义。原 g、b0、永久 c0、exact reference、H、初态 159/163 系数、原控制器 radius/streak、两网和所有门逐项保持。

原 height159.run_audit 接受该 prepared 配置，内部直接用它构造 objective，不再次把 fine cap 重置。无需修改原六个源码，不需要 monkeypatch objective 或绕过原 setter。

其完成结果仍必须通过原 source/configuration/state/exact-height/两网/gate/全部 pool handoff。此处 expected configuration 必须是实际执行的新配置。通过后，新 wrapper 应把“冻结第六前缀/纯输入恢复”的文字改成“冻结实现、新容量配置的实际输入生产”，保留原返回报告与所有失败。不能伪装旧配置或强迫历史 state hash。

新阶段从这个实际接受末态开始度量改善。初始化产生不同 LP 行集合，可能改变数值轨迹、模型成本和最终状态；这必须在结论中单列，不能把此前失败的目标问题宣称已收敛。

## 5. 需要打印的真实元数据

每个应用新规则的 stage 至少打印：

1. 原/new configuration hash 与容量，旧池行数/hash，Nr/Nt、两个 k、已记录峰数量、B；
2. 原 initializer 返回后的实际 union 行数/hash、逐组新增数量、剩余槽数，以及所有旧 ID 保留的结果；
3. 若初始化仍异常，原 status/error 及已经存在的 metadata，保持上一轮新增诊断；
4. 初态与末态的完整原两网 gate、实际 accepted/controller、LP/值/J 次数和所有费用；
5. 本 stage 是否为新容量变体输入生产，随后持径 stage 的自身初态与自身下降，两个费用不混。

容量改变属于求解配置及评价/算法身份，不进入物理 g 或 profile 系数定义。选行 J 的保留空间随新增行线性增加：每行 159 个 binary64 数；若 Nr=160 且不计峰，结构上界 1,280 行对应 1,628,160 B 的一份 selected J。它不是整体 RSS 或 LP 临时内存保证，也不改变仍构建的原 full geometry Jacobian。

## 6. 只测试新增接口的开发定义

公开首次仅运行新增纯数组/字典 fixture，不重做已过的旧 15 个开发检查，不运行真实候选：

- 构造旧池在原容量内、强制初始 union 超原容量的实际分支；原 setter 失败，新声明容量完整接收同一 union；
- 原 IDs、11 组与原坐标保持；错误 ID、删旧行及非法峰仍被原检查拒绝；
- k 按 Nt 截断、known peaks 重复时上界仍有效；源配置和源 pool 对象不原地修改；
- 初始化完成后超新固定 cap 的学习请求仍走原 budget/拒绝路径，没有第二次隐式扩容；
- 两个 stage 各一次规则及来源标签完整；旧 radius/streak/门/系数未被改写。

人工未执行、算法未运行。最终容量选择及是否同 job 接持径由 root 统一调度；本稿没有发起任何 Actions。

