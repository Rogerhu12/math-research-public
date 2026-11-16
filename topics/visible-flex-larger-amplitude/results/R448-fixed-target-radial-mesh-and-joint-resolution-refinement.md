# R448　固定准确目标下的完整径向网格与联合分辨率细化

作者：geometry agent（AI），2026-11-16。

本文只证明一个条件性的构造与调用合同，并给出对应独立源码。没有实际父场、配方、细化因子、运行编号或新的数值结论。所有科学求值、导入、编译及测试仍只在本仓库公开 Actions 执行；本文没有设置新的 fixture、独立审核或数学接受门。

## 448.1　已有入口与本次缺口

[R427](R427-current-ten-frozen450-nested-mesh-and-fresh-original-solve.md) 已给原 193 真正 frozen450 的嵌套中点初猜和完整重求；其原 owner 不接受 joint203。[R441](R441-fixed-target-angular-and-tail-step-refinement.md) 已给原 193 / joint203、真实新 native 样本、角求积与 native steps 的完整重求，但种子径向网格只是父节点与 literal knots 的并集。把任一源码改一个标签均不能支付 joint203 的真正径向加密责任。

本次独立驱动为 [geometry_20261116_continuous_ten_frozen450_radial_resolution_refinement.py](../computations/geometry_20261116_continuous_ten_frozen450_radial_resolution_refinement.py)，独立生命周期入口为 [geometry_20261116_current_C_frozen450_radial_resolution_owned_launch.py](../computations/geometry_20261116_current_C_frozen450_radial_resolution_owned_launch.py)。它们增加一个明确的径向正整数因子，同时保留 R441 的四个分辨率因子及原完整求解路径。

本次使用六个独立运行源。原 R441 checkpoint writer、SavedPrefix、径向读回、准确 cut、cuff、两帽、shared field、完整 metric、reach 和 held 数学源均保持原名称、schema 与完整 SHA。三个后闭合入口只注册新的实际 driver / owner / procedure 身份，不修改旧模块全局后冒用旧源码身份。

## 448.2　准确目标、数值程序与实际父场

令 $g_*$ 表示当前准确 C 根族、连续十族 DAG、原 core 输入、准确 cut、声明的窗口与校准参数以及十个冻结字值共同确定的目标族。其来源不是旧有限 Gauss / mask 目标，也不是某个新几何的 $1+B'^2$ 或诱导度量。使用区间盒计算时，盒中不相关的中点不能替代同一准确根选择。

父场必须是当前同一运行中已经由原完整门接受的 frozen450。它可以来自原 193、joint203、原 193 支线的 R431、已冻结 R441，或本 R448 的实际先前返回。每种来源使用明确的 producer / launcher / writer 身份。十参数按原 LE64 字值保持；准确目标身份与原有限标量 compiler 身份同时保持。父场的成功仅给初猜来源，不给新场成功。

父场的状态维数为

$$
n=3M+2=338,\qquad n+M=450,\qquad M=112.
$$

十个标量参数全部固定，不在 450 中增加活动行；112 个 core 分量仍是原完整边值问题的未知量。因此新求解可改变 core、对应的材料密度与 $\Phi$，也可改变实际高度输入 $H_{\mathrm{BVP}}$。这不等于改变冻结的十个标量参数。固定帽的常数高度 $H_{\mathrm{cap}}$ 是另一项完整构造数据，不能与 $H_{\mathrm{BVP}}$ 混称。

## 448.3　五个因子与可执行的纯径向情形

显式输入为

$$
(f_r,f_N,f_s,f_q,f_\phi)\in\mathbb Z_{>0}^{5},
$$

分别对应 `radial_mesh`、`field_and_native_angles`、`native_steps`、`material_angles`、`physical_angles`。请求中至少一个因子大于 1。后四个因子乘到父场实际七字段记录中的对应正整数；$M=112$ 与原 576 stages 不变。`native_steps_per_stage` 记录原 `steps` 配置及实际原 schedule 的来源，不把该配置普遍解释为每个程序都执行相同数目的原子步骤。

特别地，$f_r>1$ 且其余四个因子均为 1 是合法请求。原 R441 对四因子的 `any > 1` 检查已在这个独立入口中扩展为五因子合同；它不会阻断纯径向加密。反之，只有一个请求因子变大并不自动证明机器网格增加：若所有请求点均舍入到旧节点且后四因子全为 1，本入口给资源 partial，不声称加密成功或收敛。

后四因子所对应的实际正整数只做乘法，不缩小。超过原 JavaScript safe-integer 接口的计划是显式资源停止；不截断、取模或换用另一个算法。它们也没有改变 native 原 32 次方向、10 档、容差、方向 $\eta=1$ 与响应 $\eta=0$ 的接受公式。

## 448.4　全部父区间的准确候选定义

设真实父 mesh 为严格递增的有限 binary64 字值

$$
X=(x_0,\ldots,x_m),\qquad x_0<\cdots<x_m.
$$

记 $Q(x)$ 为该字值所表示的准确二进制有理数，$\operatorname{RN}_{64}$ 为本次实际 binary64 转换。对每一个父区间 $i=0,\ldots,m-1$，以及每一个 $j=1,\ldots,f_r-1$，定义

$$
\xi_{ij}=Q(x_i)+\frac{j}{f_r}\bigl(Q(x_{i+1})-Q(x_i)\bigr),
\qquad z_{ij}=\operatorname{RN}_{64}(\xi_{ij}).
\tag{448.1}
$$

源码使用 `Fraction.from_float` 和 `Fraction(j,factor)` 先形成整个准确有理式，随后仅做一次 `float(exact)`。不会用已舍入的步长反复累加，也不会只细化某些坏区间。$f_r=2$ 恢复 R427 的准确中点规则；$f_r=1$ 没有新的径向候选。

由于 $\xi_{ij}$ 位于两个准确端点之间，正常的最近舍入值属于机器闭区间 $[x_i,x_{i+1}]$。源码仍核实际结果有限且位于该闭区间；这属于候选来源与程序表示的一致性，不把该检查当作 BVP 数学接受门。候选可能与端点、另一个候选或 scalar knot 具有相同值。此时取集合并，但记录原地址 $(i,j)$、准确有理数、舍入字值、严格内部标志及是否已在并集中。

设 $K$ 为当前同一有限标量 profile 的全部 literal knots，包括原 piece / support 端点。完整请求种子为

$$
X^+=\operatorname{sort}\bigl(X\cup K\cup\{z_{ij}:0\le i<m,\ 1\le j<f_r\}\bigr).
\tag{448.2}
$$

重复值不重复计数；这不删除任何不同节点。父字值在同值位置优先重新写入，故包括带符号零在内，父 mesh 的完整 LE64 序列在子序列位置逐字不变。literal profile 的原 knot 字值并未被改写；严格递增 mesh 中相同数值只占一个位置，不能要求同一个位置同时保存两个不同的零符号。所有 knots 按值属于完整并集，原 profile 自身的字值仍由同一 compiler 保持。

## 448.5　完整覆盖与容量停止

**命题 448.A。** 若全部候选枚举返回、容量允许且原完整 preflight 返回，则种子包含全部父节点、全部 literal knots 和全部请求的舍入候选。其每个父节点与对应 450 维父状态保持原字值；原完整 preflight 也保留这些节点和所有请求种子节点。

**证明。** 构造从 $X\cup K$ 开始，按词典顺序遍历完整有限地址集合

$$
\mathcal A=\{0,\ldots,m-1\}\times\{1,\ldots,f_r-1\}.
$$

每一步仅将实际候选加入集合，不移除成员。归纳给出枚举终点的式 (448.2)。排序不改变集合。父位置用原字值重写并检查完整字节序列，因此保持父 mesh 子序列。原插值接口保父状态节点值；源码在 fresh RHS 前和原 preflight 后分别检查完整父状态子序列。preflight 后还检查整个请求并集的节点均存在。因此条件成立时得到所述完整种子。证毕。

这里没有声称末求解仍保存父状态字值。原 fullDN 必须能够更新全部未知状态，其实际末 mesh 也可能按原程序调整。命题只描述种子与 preflight 阶段；末 mesh 和末状态只能由实际返回的 fullDN / checkpoint 读出。

`max_nodes` 是显式资源容量，不隐含某个默认值必能容纳完整并集。若 $X\cup K$ 已超容量，立即保存完整必需来源和全部未访候选地址后停止。否则每次新增不同值后检查容量；首次超限时保留该实际候选、当前已处理计数与未访后缀，不删点继续求解。

地址后缀由“当前父区间、该区间尚未处理的闭 $j$ 范围、其后完整父区间闭范围及共同完整 $j$ 范围”表示。它是完整笛卡尔后缀，不是若干样本。被处理候选写入同 job 的原 JSONL 账本。正常资源停止保存精确下一地址；进程被外层强制终止时，最近已持久化 plan 可以保守地仍包含当前区间，原账本保留已实际写出的前缀。二者允许重叠，不把未持久化进度推成已付责任。

若完整并集没有比父 mesh 多出任何机器点，且后四分辨率也未增加，则没有实际分辨率增加。本入口以明确资源原因停止，不重复标记同一问题为“新加密成功”。若另一个分辨率真实增加，径向候选塌缩不阻止该独立联合请求，但实际径向增加标志必须为 false。

## 448.6　父 Hermite 仅给初猜

父实际数组记为 $Y_i\in\mathbb R^{450}$ 与已保存的 $D_i\in\mathbb R^{450}$。调用的仍是原 `curve_with_exact_nodes`，用父的实际 $(X,Y,D)$ 定义数值 Hermite 初猜。这里 $D_i$ 是原保存的有限程序数据；本文不把它声明为准确连续解的导数，也不把旧 RK 轨迹误差置零。

在 $X^+$ 上求出初猜 $Y^+$ 后，对全部节点重新调用当前实际完整 flow：

$$
D_i^+=\operatorname{Flow}_{\mathrm{actual,new}}(x_i^+,Y_i^+).
\tag{448.3}
$$

完整 450 行均需有限并具有正确形状。父 $D_i$ 只参与初猜插值，不作为新 RHS、Jacobian、残差或证书。随后由新 $(X^+,Y^+,D^+)$ 重新建立插值并调用原完整 domain / RMS preflight。若该过程失败，按原实际异常与剩余阶段返回，不能把父成功当作新域成功。

这个构造没有修改准确目标或有限标量 compiler。它也没有给新的区间 a priori / a posteriori BVP 误差界：种子的嵌套性是一个可复现的输入合同，不是误差估计。

## 448.7　原完整 450 求解仍须逐项发生

新的 `run_phase` 保留 R441 对原完整方法的调用正文。实际依赖顺序是：完整初猜及 fresh preflight、由当前场形成新的 $H_{\mathrm{BVP}}$、真实 native `withJ`、原完整边界 FD、原 fullDN、原末 native/J 与独立 fresh audit，最后才可能调用原 writer。

所有完整物理 338 行、core 112 行、两 mean、末端完整 $338\times112$ 响应和原边界责任保留。没有从 453 删除三行后标记 accepted450，没有把旧 $H$、旧零响应、旧每节点 graph / gains 或旧 Jacobian 转给新场。原 native source family由真实父记录决定；本入口不会把原 193 的独立正端点行代表与 joint203 的共同 nominal-row 算法混称为同一计算。

原 fullDN 外层 8、原内部 17 档、原 RMS $10^{-6}$、BC $10^{-11}$ 与 FD $5\times10^{-5}$ 门保持；原 native 的 32 / 10、$2\times10^{-9}$、$\eta=1$ 与 $\eta=0$ 也保持。这些是已有合同，不是本文重新证明有限程序一定成功的条件。所有未调用或未返回的完整阶段继续列为未付。

## 448.8　真实新 checkpoint 与来源闭包

本入口复用 [geometry_20261116_continuous_ten_resolution_checkpoint.py](../computations/geometry_20261116_continuous_ten_resolution_checkpoint.py) 的原 schema。该 writer 本来就接受实际 `driver_source` 与完整 runtime closure，不硬锁 R441 驱动名；新记录必须指向 R448 的真实源码 SHA、实际新数组、actual resolution、实际同 job 父 manifest 及全部原末门。

因此复用 writer 不表示复用旧 accepted 记录。成功时写的是新目录、新成员、新数组字节和新 driver 身份；失败时没有新 accepted450。原 schema 留作 writer 的真实格式身份，不能为了看似“全新”而把它机械改名。SavedPrefix、径向 readout、shared field 等同样重新加载完整新数组与实际源码闭包，而不是按父 SHA 补造数据。

R448 owner对原 193 / joint203 的来源与绝对钟逐项核实；R431 只限其已实现的原 193 路径。R441 与本入口的后继父还须绑定同一原始 origin、同一 deadline、实际 quiet 和真正成功的 450。输入格式与来源一致性不替代数学成功，也没有新增独立求解接受阈值。

## 448.9　同一原绝对钟与中断边界

原实际 deadline 来自 origin launcher 实际消费的 `actual_job_deadline`。两个来源分别保原 193 与 joint203 的真实 schema、recipe、run/source 与字节身份；总科学时间仍由原 namespace 创建时刻加 18900 秒确定，读回预留仍为原 2700 秒。本入口不重启钟、不由后来启动时刻再给同样预算。

实际 fresh sampler 和完整 BVP 各有显式过程工作上限，启动时取其与原剩余科学时间减关闭预留的较小值；运行中继续检查原截止与存储资源。它们分别建立自有 session / PGID，沿原 `OwnedChild` 观察 PID/start ticks、TERM、KILL、join 与 quiet。父 Python 的公共 PGID 不当作科学独占组。外部信号、预算、存储不足和程序异常各保真实原因，不等同数学拒绝。

源码没有保证显式工作上限之和能装进剩余时间，也没有宣称 Actions 的最终调度、信号处理或机器故障必按理想实时间终止。后继 caller 仍须给真实 step / job 限制和必要读回位置。中断发生在 seed、RHS、preflight 或后续阶段时，只有实际已持久化的结果与完整未访范围可供结论。

## 448.10　新场的完整几何与同一闭目标

独立后闭注册在实际新 450 成功且 quiet 后，调用未改的 R441 五个真实角色：完整径向重生、原 cuff atlas、shared field、live-query relative metric 和完整块 reach。held 独立使用 R441 的 R425 消费者，不以 metric 或 reach 通过为前门。它们的数学 schema 与源码 SHA 保持原身份。

首次完整构造的 $W,H_{\mathrm{cap}}$、所有 marker 及列表顺序按字值保持，真实 cuff 仍由同一原 C 输入决定。常数帽高不进入帽诱导 metric；冻结它是本次几何构造保持责任，不是“它改变原目标”的论证。

求解改变 core 时，$\Phi$ 与 SE2 / R249 几何记录可重新生成。要比较同一抽象闭目标，须使用 [R443](R443-common-material-angle-pullback-and-fixed-closed-target.md) 的正确方向

$$
\psi_j=\Theta_j^{-1}\circ\Theta_0,
\qquad \Theta_j(q)=\Phi_j(2\pi q),
$$

以及 prefix 公共 $u=s_{\mathrm{numeric}}/L_{\mathrm{numeric}}$、tail 同一物理 $r$、帽 Cartesian 恒等图和相容 gluing。它要求真实正密度等原前提。四 Loewner 关系在同一可逆坐标拉回下由 congruence 保持同一 $\eta$；完整像、reach、held 和含反射 $\delta_E$ 是对应像的性质。但 R448 没有执行已发表 R447 的准确 common-material consumer，也不把“来源相同”当作材料系数表逐字相等。该条件责任必须继续明确。

## 448.11　必要读回与未付范围

owner reader逐份读取实际新 sampler、driver、原 FD / RMS / BC / final / audit / checkpoint 及原 native 调用的必要范围。新增径向 plan 的完整 pending 闭地址、容量原因、实际候选计数、实际 mesh 增加标志与首末机器塌缩见证进入单份必要结论。全部 literal knots 和完整 candidate ledger 有原件身份；候选大账正文不编码、分段或宣称已全部返回。

原 R441 phase reader是纯元数据函数 API，原字节复用。新 reader不是通过修改其全局状态来声称另一个 schema。后闭与 held 各保其原完整必要范围和独立单份 90000 字节上限。任何一份超限仍诚实返回 70，实际必要不完整则不写完成 marker。科学成功与读回完成是不同字段。

所有原 raw 暂留同 job。这里没有清理、上传、外部 archive 或 request/workflow；任何后继 workflow 只能在各原必要读回完成且真实 quiet 后按自己的完整合同清理。

## 448.12　结论与仍未付的责任

条件满足并实际返回时，R448 给出真正父网格的完整有理细分种子、全部新 RHS、原完整 450 重求与真实新 checkpoint；可以联合原四项分辨率增加，也允许纯径向细化。它补的是实际执行入口和来源责任。

它没有给 $M$ 维数扩展，没有改变 576 stages 或有限远端，没有证明同一准确 C 族中某个根选择的单值数值代表误差，没有证明 mesh / angular / tail-step 序列收敛，也没有证明任何新场是准确连续 BVP 的解。metric、reach、全像 held、含反射 $\delta_E$、全参数 $t$ 几何及各 seam 的严格责任仍需真实新场的原完整消费者支付。当前没有 actual parent、因子、request、run、实际节点数、accepted450 或已过几何常数。
