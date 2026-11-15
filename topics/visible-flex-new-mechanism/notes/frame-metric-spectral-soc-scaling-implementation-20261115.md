# 只改变二阶校正 LP 表示的可逆缩放

日期：2026-11-15。分类：第2–4节为准确有限维代数；其余为实现定义、人工开发检查和待公开执行的数值实验。新增文件为 `scripts/frame_second_order_correction_scaling.py`、`scripts/frame_metric_spectral_soc_scaling.py` 和 `scripts/frame_metric_spectral_soc_scaling_audit.py`。旧科学脚本不改。

## 1. 这一次试验回答什么

[strip-reserve 首次 actual](strip-reserve-first-actual-20261115.md) 的 run43684152565 以 source `c594eeb060f25dbc9c48911b4ec6511497692c0f` 执行。条带4/5提案floor使该新阶段的12个实际试探均通过原条带门；余下3个细网拒绝均有真实曲率58门失败。模型8的唯一 SOC 在10秒限时后未返回 primal。因此没有可用的校正向量，随后被接纳的四分之一步属于原主步回退。它不能被描述成“实际 SOC 校正失败”，更不能仅据超时证明病态。

本轮只问：把已有 SOC 的小变量及不同单位的仿射行可逆归一化，在同一原限时、原残差门和真实验收下，是否更容易得到可用的校正？不改变其数学可行集、目标最优集、曲率/条带提案floor或主 LP。旧末态的实际度量误差约 $.266523$，仍远离课题所需精度；一次表示试验若不改变可用下降方向，后继应检查有限表示的自由度或连接机制，不能用无限小预算续求代替结构进展。

这里 SOC 始终表示 **second-order correction（二阶校正）**。求解器接收的是普通线性规划，不是二阶锥规划。

## 2. 旧校正 LP 的准确变量与目标

当前接受态为 $x$，已有真实试探为 $y=x+p$。记原参数盒宽对角阵

$$
D=\operatorname{diag}(u-\ell),\qquad
r_c=\tfrac12\|D^{-1}p\|_\infty.
$$

旧校正变量 $w$ 写成 $v=D^{-1}w$，并引入逐分量辅助量 $h$。旧完整 LP 变量是 $\xi=(v,h)$，目标为 $\sum_jh_j$。其中

$$
\max\{-r_c,(\ell-y)/D\}\le v\le
\min\{r_c,(u-y)/D\},\qquad
0\le h\le r_c,\qquad -h\le v\le h.
$$

最后一个辅助上界是原源中已经存在的约束。因此下面变换不仅保留 $v$ 的投影可行集，而是对整个 $(v,h)$ 可行集给双射。若 $r_c=0$ 或主步没有原要求的预测改善，继续执行原来的零步／无改善返回；此时不做除法，也不调用新 LP。

保留原源组装的完整矩阵与右端：

$$
A\xi\le b,\qquad \ell_\xi\le\xi\le u_\xi.
$$

该矩阵包含全部已学粗细行、真实 $y$ 的软度量残差、所有硬行、帽高和辅助绝对值行。特别地，SOC 的硬行以

$$
c_i(y)+J_i(x)w\ge t_i
$$

表示，不重复减去主步 $J_i p$。软行预算仍来自主步预测改善的原保留比例，但其残差仍取这个同一个真实 $y$。本实现先按冻结 strip 源**完整组装原 $A,b$**，再把这两个数组交给缩放 helper；没有在新单位中重新推导或改写目标。

## 3. 可逆变量和正二幂行缩放

在 $r_c>0$ 时令

$$
v=r_c z,\qquad h=r_c t.
$$

于是 $t\in[0,1]$，$z$ 的所有上下界均是对应旧界除以 $r_c$。新目标为 $\sum_jt_j$，旧目标恰为它乘正数 $r_c$，所以最优解集合在上述变量双射下相同。

对每一条普通标量仿射不等式，选一个正数 $d_i$。记 $R=\operatorname{diag}(1/d_i)$，则新矩阵、右端和变量为

$$
\widetilde A=R A(r_c I),\qquad
\widetilde b=Rb,\qquad \widetilde\xi=\xi/r_c.
$$

准确算术下 $A\xi\le b$ 当且仅当 $\widetilde A\widetilde\xi\le\widetilde b$。正因子逐行除法仅用于这些标量仿射不等式，不是对一个向量锥的不同分量任意缩放。

具体的行尺度取

$$
m_i=\max\{\max_j|r_cA_{ij}|,|b_i|\},\qquad
 d_i=2^{\operatorname{clip}(\operatorname{frexp}(m_i).\mathrm{exponent},-1022,1023)}.
$$

零行取 $d_i=1$。在通常指数范围内，该尺度把每行最大绝对值放在约 $[1/2,1)$；指数截断只避免构造非有限二幂，不授普遍条件数界。helper保留原数组副本并拒绝不匹配的维数、非有限输入、非正半径、错误的辅助量上界或非有限缩放结果。

这是准确数学上的等价表示。实际构造 $r_cA$、除法和界值仍有 binary64 舍入，HiGHS 原有的 $10^{-9}$ primal/dual 容差现在作用于新单位；**数值轨迹不必与旧求解器相同**。这就是本轮唯一要观察的数值表示差，不能称为旧浮点行为逐位重放。

## 4. 原单位验收和同次对偶映射

若新求解器返回 primal $\widetilde\xi$，先恢复 $\xi=r_c\widetilde\xi$，再使用保存的原 $A,b,\ell_\xi,u_\xi$ 计算行和盒残差。原独立残差限仍为 $10^{-7}$。求解器success与原残差门都通过后，才允许构造 $w=Dv$ 及后续真实几何试探。原10秒单 LP 上限和所有共享计数不改。

新单位下很小的残差不代表原单位下足够小。人工例子明确产生缩放残差约 $5.12\times10^{-11}$ 而原残差约 $.001718$；它必须被原门拒绝。没有 primal 时所有 primal、达到floor和对偶值都记为不可用，不能以零填充。

采用 SciPy/HiGHS 当前最小化 marginal 约定，仿射上界行 multiplier $\mu\le0$，下界 marginal $l\ge0$，上界 marginal $u\le0$。新单位返回 $\widetilde\mu,\widetilde l,\widetilde u$ 时，对原目标的映射是

$$
\mu_i=r_c\widetilde\mu_i/d_i,\qquad
l=\widetilde l,\qquad u=\widetilde u.
$$

因为新目标已除以 $r_c$，原 stationarity 为

$$
c-A^T\mu-l-u=0,\qquad c=(0,\ldots,0,1,\ldots,1).
$$

原 primal 目标为 $c\cdot\xi$，原对偶目标为
$b\cdot\mu+\ell_\xi\cdot l+u_\xi\cdot u$。报告计算二者差、stationarity、互补性和符号残差，并按所有原行组列出同一个返回对偶的乘子与 stationarity 贡献摘要；帽高和辅助绝对值行也独立分组。不再求第二个 LP。

这些是浮点诊断，不是经过区间包围的最优性证书。冗余行和对偶退化可重新分配乘子，因此某个大乘子或非零组不能被单独解释成不可替代的几何瓶颈。

## 5. 保持哪些科学定义与验收

新库直接导入冻结 strip 的主提案函数；SOC 的旧目标、矩阵组装、原参数盒、同一点 $y$、帽高及软度量保留比例不变。组4/5的无量纲floor $10^{-7}$、组7–10的原曲率行单位floor $10^{-7}$ 全保。

新阶段仍为同一163维、同一 $g$ 与固定 $b_0$。目标度量仍为 $13/50$，可接纳的旧度量预算仍为 $167/625$，硬曲率仍为58。原粗384／细768值网和完整实际门不变，包括独立真实 $\eta$、实际曲率、PSD、球、内外条带、正高度、镜像点对、帽高、盒和非退化。每次接纳仍须完整两网真实最大 $\eta$ 严降，并支付原最小下降或达到目标的例外。未接纳试探不得替换保存态。

增长、缩步、最小半径、每模型最多一次SOC、抛物线回退和全部池继承不改。新阶段共享原12次主/SOC LP、40次粗细值调用和120优化秒；SOC的缩放准备和诊断时间也计入真实wall，另列 LP 本身的耗时。

## 6. 根15下恢复两段必要输入，不强迫历史终态

旧 strip actual 的完整机器系数及池不再持久化。因此仍用原24个有路径/SHA的旧输入，实际CLI仍98项。同一个 public job 内依次：

1. 原严格 loader 构造合法旧输入，调用一次冻结 growth 阶段。
2. 消费它的真实源码、配置、准确系数、两网末门、完整池和控制器，经旧 strip handoff，调用一次冻结 strip 阶段。
3. 新 handoff 核这一临时 strip 的完整源图、初态／输入绑定、精确 binary64 系数、同 $g/b_0$、两网末门、池的所有整数ID／坐标和控制器，再执行一个新的 SOC 缩放阶段。

必须保持的旧 strip 文件 SHA 是：

| 文件 | SHA-256 |
|---|---|
| `frame_metric_spectral_strip_reserve.py` | `0d653e66947b95efe56e518e8bf4705076bc9ef687e5a596a1884b8367d22ae3` |
| `frame_metric_spectral_strip_reserve_audit.py` | `4347bdc3afc2504b2a6546d41176e0e3a9e340533ee1eee16ff831257e149e38` |

先前观察到的 strip 终态为 `267c41ff9cfe565cb859531ab505b3cab85069ff0ad77955fccb5e00354e824e`，其临时完整报告SHA为 `eba499be5bfbf9e74e0cf9af4a62e2799cafadbb0b33378deba797c41dbd4f25`。它只作历史观察，不是要求恢复重复到相同hash的门。wall停止位置可能改变临时末态；只能在本次真实两网合格的接受态上继续，新阶段改善由这个实际初态计算。不能增加恢复预算以强迫旧hash。

控制器也不重新取配置种子。新手交接先绑定 strip 的原始 continuation，再按其已完成 `scale_feedback_update` 依次读取半径／streak。最后未完成模型只贡献其 `trust_before_model` 和之前已完成的 streak；没有新模型时保留 strip 已继承的控制器，不回到 growth 的原种子。已低于原最小半径时继续执行原preflight退出。

这两个前缀分别有原预算，故整个job不是总共只用120秒。报告和stdout单列两次恢复的源码／配置摘要、实际canonical、是否匹配历史观察、初末门、LP／值次数、准备／运行／优化时间；总进程时钟包含它们和新阶段。临时文件位于结果目录外，结束清理，不发布payload或artifact。

## 7. 本轮必须可读的日志

结果目录只有一个新顶层科学audit、一个原生stage `metric_spectral_soc_scaling_stage`；旧前缀只有嵌套元数据。现有 `print_research_outcomes.py` 通过唯一含solver/checkpoint的stage自动识别，继续打印全部新模型、试探、SOC、增长、接受、初末门、终态hash和耗时，无须为新名字修改打印器。

driver另直接打印以下紧凑科学表，均只读已算数组，不额外调用几何：

- 两个必要前缀的完整初末门、真值、来源、控制状态与耗时；
- 每个实际trial的粗细完整gate布尔向量。表头逐项定义顺序，`?`表示未得到该值，不填true；
- 每个primary／SOC的曲率7–10及条带4/5原目标、请求目标、达到最小值、floor亏量与原行残差；
- 每个SOC的半径、行divisor范围、是否有primal、status／message、缩放准备／LP时间、原／新单位残差；
- 同次原单位对偶及所有行组摘要；
- 每个实际trial已选曲率行的预测／实际余差，以及实际最紧已选行的原索引、材料位置、$q$、两个主曲率。

对曲率行，真实源使用

$$
\widehat H_\pm=(\lambda q I\pm qII)/100,
\qquad
\det\widehat H_\pm=\frac{q^4}{10000}(\lambda\pm\kappa_1)(\lambda\pm\kappa_2).
$$

因此日志在同一点检查此恒等式的浮点差，避免把 $10^{-7}$ determinant 余量误当成相同量级的曲率余量。一般trace也不是在非正交实际度量中直接取主曲率之和。主步预测以接受点加 $J$ 总位移比较；直接SOC校正以真实主trial $y$ 的残差加旧 $Jw$ 比较；两种标签明确分开。发生粗网提前返回时不伪造细网值。

新增stdout压力fixture覆盖12模型槽、20个粗细trial对、6个SOC诊断，约44.5KB；它比真实共享12LP／40值允许的同时组合更宽。它只输出人可读汇总，不dump全部系数、数组或原JSON。通用科学表另按其原35KB门打印。根15 publisher只登记来源、参数、run和SHA。

## 8. 内存与人工范围

SOC helper需要旧矩阵只读副本和缩放矩阵，量级与选中行数乘 $2n$ 成正比；例如8000行、326列的一个float64矩阵约20MiB，暂存多个版本约数十MiB。没有新增完整384／768角Jacobian，已有geometry／selected-row缓存和分批规则保持。完整实际峰值RSS仍应由公开run报告，不把数组估算当实测。

本地只执行新增人工路径：小LP的可逆映射／同最优点、原单位KKT与缺primal、异量纲残差反例；捕获旧／新SOC组装逐项相同；真实小人工jet接口的缓存／group-major索引和同点曲率恒等；两恢复各一次、真实控制状态承接、错误状态／门／池拒绝、单顶层输出、错误后保checkpoint；小数组家族走新initial/final/summary，以及新增日志压力。未运行任何实际候选、旧优化或旧开发套件。

这些新增人工检查已通过。新真实研究尚未运行；人工通过只说明接口和所测代数正确，不证明SOC在实际问题上会更快或会改善几何。
