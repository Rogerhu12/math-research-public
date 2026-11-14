# 最终 M15 真联解之后：原目标上的连续认证最小路径

`/root/independent_geometry`，2026-11-09。**状态：只读接口／预算计划，不是新 M15 证书。** 没有读取活动候选，没有启动导出、root、flow、solver 或完整 metric／曲率后端。本文条件是：将来得到且冻结原方程的完整 M15 prefix/tail 真联解；某次内层响应成功、一个接受 trial 或 affine warm 均不能替代这个前提。

本计划负责连续 prefix／whole 认证及接口。tail 的另份计划负责原 moment root、RK 与实际 XYZ 表示三层之间的输入关系、critical 网格及端点层；不在这里重复设计 exporter。

## 1. 目标门与已有证据的边界

拟核对的更紧门为原精确 $g$ 上的完整相对 metric 误差

$$
\mathcal E_{15}\le B,\qquad B=2\cdot10^{-9}=1/500000000.
$$

这是需要连续证书证明的 metric 门。即使原求解器的某项停止 tolerance 也写作 $2\cdot10^{-9}$，两种量并不相同，不能由 solver success 直接推出本式。

旧 R21 M12 闭图已有严格点 lower $\mathcal E_{12}>1.95883\cdot10^{-8}$。因此不能继续对那张旧图加密证书，企图证明其完整误差小于 B。现有 M12 的两局部角弧验证只支付方法与接口，并没有改变该事实。未来新 M15 图也不能借用辅助 affine prefix 的 sampled metric：它需要自己的完整实际图与上界。

保持原精确 $g$、设计参数、保护端、有限校准常数、握持帽及 $t$ 范围。解的自由未知坐标可以通过原方程校正；不能把改变物理目标／尺度参数当作频率或网格收敛。原 analytic target 仍由固定物理参数、解析轮廓和 exact bridge 定义，不能改取新图自身的诱导度量作为目标。

## 2. 必须先冻结的对象

| 层 | 必要交付与身份检查 |
|---|---|
| 原联合求解 | 最终 prefix CP 及其原 `solver_success`、collocation／边界残差，最终调用的原 tail response／staged CP，原 shooting 验收与完整 seam audit。最终 cut H 必须来自这同一 prefix，不能拿另一 H 的缓存响应代替。 |
| 固定 g 与源码 | `frozen_profile`、cut、chart、`warp_reference_q`、物理 tail 参数和有限校准表；原自由 support 坐标与固定 gauge 明确分开。冻结实际导出依赖及本题适配脚本 hash，使用已有 `repro/source-root`，不再依赖旧 scratch 路径。 |
| prefix 有限图 | 用已审 flat loader 和 mirror wrapper 从该最终 CP 生成共享二 jet Cartesian Hermite。记录实际表示频率、网格、精确 mean increments、数据 hash、入口精确镜像条件及修改量。`source_modes=15` 不等于 Cartesian 表示 cutoff 必为 15。 |
| tail 有限图 | 从该最终 staged CP 生成完整 `IntegratedTail` manifest、全部分片、精确径向增量／比例、共享 first/second/mid 信息及本图自己的 R6 collar。finished、两个 anchor、分片共享行和物理参数须逐项核实。 |
| 共切闭图 | 已审 common-cut v2 绑定上述两图和本图 exact bridge，支付完整 Cartesian 两 jet、整 Z 反射、正确 mean gauge 与固定帽。不能只凭原非均值 slope residual 宣称已经精确 C² 拼接。 |

tail 已指出现 exporter 的 `angular-nodes` 同时影响其局部 root 求积和空间 Fourier 采样，不能称为纯插值分辨率；参数必须在最终数据中如实记录。其现有 interior critical 格不自动覆盖后续识别的 raw0/segment7 端点层。对应小型网格修订应由 tail 单独冻结审查，不能在连续认证时假定这些输入已完成。

最终几何表示、source RK 和 analytic target 是三层不同对象。允许构造有限显式近似，但所有连续上界必须针对明确冻结的那个有限图；不能混用 source RHS 的导数和另一 Hermite 图的位置。

## 3. 使用冻结代码时的实际依赖次序

现有接口的最小无改码路径为：

1. `db6f-root-mirror-hermite.py` 用最终 CP、原 port 与 flat loader 生成基础图；保持 `ell=0`，保留精确入口镜像条件。
2. `db6f-audit-metric-supplier.py` 对该基础图生成新的径向 target 包。它将图节点与原 analytic a/e 分段端点合并，真实 a/e 公式不变。
3. 原 `db6f-audit-metric-polynomial.py` 取得该基础图自己的完整源目标上界；用这份报告、新 target 和新 tail manifest 调用 `db6f-root-exact-bridge.py`，生成新的唯一根／转移绑定。
4. `db6f-root-common-cut-v2.py make` 生成最终共同图；它可增加所需 Cartesian mode padding，不能据 solver M 假定输出维数。原 target 仍绑定基础图并覆盖同一径向分区。
5. 用 common-cut 的 `metric` 入口得到**修正后最终图**的完整原系数界。它才是 `prefix-angular` 所需 baseline。第三步基础图报告不能代替这一步。
6. 按下一节运行已审第一档 angular wrapper；同时准备同一最终图自己的 geometry、moment、tail first-jet 和完整 tail metric／κ 证书。

第三步的 bridge 脚本目前要求输入一个基础图 metric 报告，即使参数差上界 $\eta$ 本身与解的形状系数无关。因此原接口确实有基础图与修正图两次不同的 metric 计算。不能用修正图报告伪装基础图来跳过这个依赖。若日后仅为节省这一步，要另审参数-only bridge 适配器；当前认证并不需要先改它。

数值 CP／seam 成功只使导出有合格输入。shared Hermite、mirror 和 common-cut 都定义新的明确有限近似；它们产生的 metric 变化应由最终图的后端直接计算，不能借旧 CP 的 sampled error 或另外手加一个猜测的“很小修正”。

## 4. 第一档 angular wrapper 可以原样复用

当前冻结 `db6f-audit-prefix-angular-metric.py` SHA 为 `42e7d222c40512fec2d4fd757544d630b3e372487322e27eb3571a06519eb2fb`。它没有硬编码 M12，适用于通过其原对象／来源 guard 的新 common-cut-v2 图。默认先继承有效旧界，只有不满足预算的原区间才计算角弧，128 初始弧后只二分仍超预算的弧。

首次完整运行建议使用其现有默认深度上限 4；这个上限不意味着全部角弧都会细化到 2048 弧。达到门的弧立即保留。也可以先用新 baseline 的实际 worst interval 作小 pilot，但不能把旧编号 0、74 预设为 M15 最坏处。若 pilot 已表明实际图误差不可能达到 B，应先分清图误差与验证过估计，不要盲扫完整域。

最终完整报告必须省略 `--intervals`，覆盖本图 target 的全部原区间。两局部 fixture 不能作为完整认证。需要 `finished=True`、`entire_prefix_covered=True`、完整叶覆盖／正分母和 `entire_prefix_target_met=True`；同时复核所有文件绑定和逐行最大值。

调用预算应直接写 **`--budget 2e-9`**，因为 wrapper 内部已经做一次精确 bridge 转移。不得在 CLI 先扣一遍 $\eta$ 后又让 wrapper 再扣。完整输出的 `metric_operator_upper` 仍是**源目标**上界；`exact_target_metric_operator_upper` 才是已转移值。旧 closed-budget 读取前者并转移一次，与这个接口相容。

原 baseline 只存完整全域最大值，未存每区间 ledger；当该最大值超过 B 时，wrapper 必须逐区间重新得到原界后才知道哪些可继承。它不能凭新图 sampled error 跳过某些原区间。这是现有无改码路径的计算代价，不是数学漏洞。若需要避免这种重复，新增每区间 baseline ledger 或局部证书合并器都要另审；当前没有必要先做这些扩展。

原 wrapper 的 `locate` 要求 repo 相对 `source_root` 可解析，因此从**仓库根 cwd** 启动并使用绝对 CLI 文件路径。已完成的局部测试记录了 topic cwd 下的安全拒绝；不要通过修改来源路径／hash 来绕过 guard。

## 5. 径向 target 包与 exact bridge 的预算

设新图的实际原目标差证书给出 $\eta$，源目标 metric 上界为 $\varepsilon$。必须使用

$$
\varepsilon_{\rm exact}\le\varepsilon(1+\eta)+\eta,
\qquad
\varepsilon\le\frac{B-\eta}{1+\eta}.
$$

若新图经核实具有与旧同一 $\eta=3.319321476658082\cdot10^{-13}$，则允许的源界约为

$$
1.9996680678516704\cdot10^{-9}.
$$

旧 $\eta$ 约占 B 的 $0.0166\%$，目前没有先收紧 exact bridge 的理由。但旧 bridge 文件绑定旧图／target，不能直接拿旧 hash 给新图使用；新调用应重新核实端点、源常数、唯一根及所有身份绑定。参数预计相同不等于已经生成新证书。

供应包宽度不能只看 `maximum_remainder`。本次只读旧 M12 包，用 Fraction 对每行计算

$$
w_f=\sum_j(c_{j,\rm hi}-c_{j,\rm lo})+2\,\mathrm{remainder},
\qquad f\in\{a,e,e'\}.
$$

这是 $u\in[0,1]$ 时允许系数／余项的点态全宽上界，不是 metric 上界。旧包得到：

| 量 | 全宽最大值的向上显示 | 原区间 |
|---|---:|---:|
| a | 3.3735310237859903e−12 | 2574 |
| e | 1.114561967441079e−16 | 503 |
| e′ | 2.2291874292659775e−16 | 328 |

旧 a 的 remainder 最大值只有约 $1.26\cdot10^{-16}$，而末段 anchor 的系数包宽更大。新网格可能改变累计包宽，必须重看本图的全部系数宽及余项。角弧细分会改善角相关性，不会消除 a 的累计 anchor 宽度或已固定的径向 Bernstein 过估计。

所有 target 不确定性和浮点卷积包围已进入系数相消后端，不能再用上述表的 raw 宽度直接相加到 metric，或反过来从 metric 里扣掉它。若只有目标包造成可量化的预算缺口，再有针对性收紧该包的 analytic anchor／Taylor 包；e 的 exact spline、flat ramp 的 exact 分段及已审 sliver guard 保持。

本次所有标量和 hash 在 `audit-m15-certification-readiness.json`（SHA `73b870838a269b398a9f57bf295c4c1fae378f89441f2c126322a885aa69ba63`）中。其条件预算使用旧 $\eta$，宽度使用旧 M12 数据，均未冒充新 M15 证据。

## 6. 什么时候才需要改代码或改表示

| 实际剩余问题 | 最小后续动作 |
|---|---|
| 同一原径向盒，角分母／残差相关性过估计 | 继续现有第一档的局部角二分；不必先写二阶角 Taylor。 |
| 局部角充分细后仍由径向 Bernstein 过估计主导 | 另审同一原多项式／target 包的仿射限制及矩形覆盖，验证域细分即可；现 wrapper 不支持这项，不应声称已经实现。 |
| analytic target 系数宽／余项本身形成底噪 | 只收紧相应源包。保留原解析 g，重新支付所变供应器、目标及 bridge 绑定。 |
| 实际 Hermite／共切图的严格点 lower 已超过 B | 验证细分无法解决；需更准确的同 g 有限表示或真正加密原解，并重新绑定整张新图。不能另造目标。 |
| 只有少量新盒未达门，想复用已有通过记录 | 可以另审局部替换／完整覆盖合并器；否则使用原 wrapper 重新完整运行。不能把多个 partial 的数值最大值无覆盖证明地拼成全域证书。 |
| 新最终 CP 只增加诊断／运行元数据键 | tail 正规划明确的 same-g transfer 小适配器；仅在静态证实纯数值语义后加白名单，不能广泛忽略未知键。 |

最后一项有实际下游依赖：冻结 `closed-budget-v2.py` 不仅检查旧 transfer 脚本 SHA，还会重新 import 旧 `NUMERICAL_KEYS`。若使用新四键 adapter（`iterationCheckpointFile/sharedEngines/trialDiagnosticFile/trialStatePrefix`），相应 consumer 必须有已审的最小绑定适配；不能只把新报告写成旧 script hash。这项元数据联动不要求改变 prefix-angular 的数学后端。

本轮不默认改变 prefix Hermite 节点、Fourier cutoff、目标参数、core 形状或 patch 宽度。更换图的表示与细分验证域必须分别标记；只有后者可直接复用原图的其他几何证书。

## 7. 从完整 prefix 到完整闭图

原 all-phase 机制和固定帽继续适用时，完整 metric 界为各区域上界的最大值，而不是给 prefix/tail 各分一半预算：

$$
\mathcal E_{15}\le\max(\varepsilon_{p,\rm exact},\varepsilon_{t},0).
$$

因此 prefix 和 tail 都必须各自达到 B。时间方向沿已审相位共轭／固定帽结构处理，是全 $t$ 的论证；若干 t 网格不能取代该量词。

旧 w/wr 背景包在同 g 的精确网格 transfer 后可以复用，背景的六项定义 hash 应保持；但旧 M12 实际 κ、metric、first-jet、moment、witness 数值都不能用于新 M15 manifest。新图至少需要一次自己的完整实际 κ 与几何证书；在**同一个新 manifest** 上，之后可用更紧 w 包仅重跑 metric，再与这份同图 κ 证书合并。更小的 C¹ metric 误差并不控制 C² 曲率。

`whole-metric-reach-v2.py` 现有硬门是 $10^{-6}$，它本身不宣告 B。完整新报告生成后，只需另加一个轻量的已审 Fraction 标量核查，检查 `whole_metric_operator_upper.exact <= 1/500000000`；无需为这个门重做已经有效的所有后端。其输入仍须全部属于这同一闭图。

若该上界真实通过，与旧 R21 指定 M12 图的严格点 lower 可推出

$$
\mathcal E_{12}>9.79415\,\mathcal E_{15},
$$

其中新图正误差时是严格下降比较；新图若恰为零则下降亦成立。比较必须保留两图同 g／同时间范围的身份核查，不能只比较两个报告打印的上界。

单个更紧上界仍不是 README 自动完成。还需保留固定几何下频率／径向等加密的完整序列及实际下降证据，核 all-phase embedding/reach、握持／非全等、同图最终网格，并由未参与数值优化者实际重跑。旧 M8 网格可以保留作中间交付，最终候选应有对应自己的几何导出与验证。

## 8. 最小实施判断

就连续 prefix 而言，当前第一档已足以开始新图认证，不需要预先实现 Taylor 阶、普遍径向加密或新 target。先取得真正最终 CP／seam／有限表示，再按已有依赖生成本图 target、bridge、共同图和原 baseline；只有实际未达预算的具体原因，才触发上表中的额外修改。

本文没有对尚未提供的最终 M15 图声称上界，也没有从任何活动求解状态推断成功。它给出的是保持原目标和已审实现的最短可审核路线。
