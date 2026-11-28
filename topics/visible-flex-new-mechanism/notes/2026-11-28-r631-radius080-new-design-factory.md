# R631：R=.8 的真实新设计 factory

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。
**源码实现，尚未运行新的科学计算；没有 R=.8 的已接受连接解。**
源码 `scripts/r631_radius080_design_factory_20261128.py`。
它与仍在运行的原 target86da/centered 范围并行，不更改或冒用该范围。

## 1. 本次真正改变的数学输入

新核心半径为 $R=4/5$，对应 R631 的厚宏观核心，而不是 R579 的 $R=17/20$。
默认 profile 仍取 $r_c=.22,\ell=.2,\alpha=.55$、core onset .55、
core scale .5、中央半高 .04 和原 gain 形状。
新 Profile 的资格预算明确为 R631 的 `ball_budget=1.032`、`reach_budget=.062`，
不是旧 R579 的1.05/.063；这些字段是设计目标，尚不授予实际场相应几何界。
$H=.5188903877153482$ **仅作为显式设计初值**，没有继承原 H 的可解性或误差。

新 pre-tanh 基线只含 $\mathrm{amp}\,F_2$，其余 pre-tanh/local/force 系数默认0；
force 自身仍实际重建，使用声明的新归一化常数（默认1），不取原16533归一化。
新1130维post设计响应只有 H 非零，其余全0。
若以后传入另一个完整设计初值，其全部系数会进入新定义。
默认 amp 是调用者显式输入；它不继承一个旧候选的已接受标签。

## 2. 哪些真来源重用，哪些实际重建

只重用 $R$ 无关的内尾 germ 选择、finite-M Cauchy 输入和已经保存的 mouth 数据。
从这些数据恢复实际密集尾场所需的 ODE 仍照实计费；不再次求内 DtN slope。
旧有限 M、Cauchy 和 dense ODE 的未付误差没有因重用而变零。

随后在新的 Profile(R=.8) 上重算全部11个 connector/core 模式、原 j4 强迫解、
新的 $A_{\rm core}$ 归一化、envelope 和 mean-height 函数。
旧 R=.85 的 connector/core 矩阵和归一化都不拿来冒新半径。

BS 只借用原67结点的拓扑：$.65$ 以下保原物理结点，以上按

$$r_{\rm new}=.65+(r_{\rm old}-.65)\frac{.8-.65}{.85-.65}$$

定义新结点，终点准确置为 .8。原全部 compact 支持都在 .65 以前，保其原物理定义，
但实际径向值与新 work/fine 网格重新生成。
原 core correction cutoff .65 到 .78 仍严格位于新端点 .8 之前。
这是新的字典与参考场，没有把原1130个巨大接受系数移植进来。

## 3. 静态设计可以改变 W/H/E

`Radius080Design.evaluate_design/jacobian_design` 消费新实际场，使用 R613 的完整
变量 $E$ turning 链、全部位置行与完整 H 导数。
模型明确标记：当前 $E$ 随静态设计而变，设计参数不是最终等距族的时间。
这允许在找宏观候选阶段调 W/H/E；不假设任意支撑路径必能在旧小幅 g 内延续。

`actual_core_seed` 返回新对象当前响应的实际 $P_0$、完整 $P_1$ 与 scalar root，
绝不会把它叫作旧会话已接受的核心。
后继 hard-total-P 应约束**总**核心，保留 H 作为设计变量；其源接口继续实现。

选到实际静态候选后，`candidate_metric_definition` 可以明确保存全部已选 q、
新 profile、字典和完整连续 turning 定义，生成**新** target 身份。
此后才对那个固定 g、固定参数和固定时间范围进行精化。
这个函数只给定义，不自动证明候选满足嵌入、reach 或 README。

本轮仅做源级构造器/调用链、AST及序列化检查，没有本地科学执行，也没有新 workflow。
旧接受步数、旧 eta、旧 core match 和旧 target86da 一项都未移交；
完整新构造成本和失败会由本身实际 Actions scope 记录。
