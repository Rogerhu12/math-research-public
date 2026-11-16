# R570　同次真实 cubic 捕获、准确 quintic 比较与当前完整调用链

**可信度：已证明（限下述源码组合及条件命题；没有本次科学运行或数值结论）。**

作者：OpenAI / ChatGPT geometry agent（AI）。日期：2026-11-16。

本结论把已刊 R569 的真实 `sol.sol.c` 读写器接入当前三条求解来源，并把其与准确 675 quintic 的比较接入当前 same-C 全域误差测量的原 prefix 单元。它不把从节点重新形成的 Hermite cubic 当作原 SciPy PPoly，不把保存来源当作实际场已接受，也不把这一旁诊断变成原 BVP 或 metric 的新门。

本次入口为独立 request239；实际结论仅预留 R571。这里没有 run、已接受父、捕获数组或误差常数。源码准备只进行完整文本、固定身份和 literal replacement；未在作者环境导入、AST、编译、执行科学、运行 fixture 或测试。所有数值及数组形成只在明示的公开 Actions 中进行。

## 570.1　实际缺口与本次支付的范围

[R569](R569-same-call-literal-cubic-accurate-quintic-and-complete-defect.md) 已区分：

1. 当前准确 quintic $Q$，由实际 675 `ExactFiniteField.prefix_coefficients` 定义；
2. 用 $Q$ 自己两端准确值及一阶 jet 定义的 canonical cubic $C^*$；
3. 同一次原 full-DN 求解真正返回的 SciPy PPoly $C_{\rm lit}$。

只凭 checkpoint 中的节点、重新计算的 RHS 或论文中的 Hermite 公式，不能恢复第三个对象。R569 因而保留了真实 recorder 与 current-field binder，但没有自动安装到正在用的 driver、owned launcher 或 necessary reader。本结论支付这一真实调用缺口。

当前基线是 R567 / request238 的完整 557 来源，而不是旧 R504 四族名字的抽象复用。其三条真实 driver 为 first453→450、refined112 和 incremental-M；它们分别经过当前 R544 的客户端/closed ENTRY 修复、R498 完整 gzip 账本及现行 sampler/worker 来源。新 caller 必须顺着这些真实来源传播，不能只在请求中添加 R569 标签。

本次新增内容限定为：

- 原求解调用周围的透明 recorder 安装与撤销；
- 原接受后完整 capsule 的同 job 临时写入；
- 所有当前来源的真实新名、bytes、SHA 和调用关系；
- 当前 same-C evidence 的同次 target/field/DFS 旁诊断；
- 原正常及 recovery necessary 中的完整新增语义；
- 原相同绝对钟、所有既有接受门及清理责任的真实接线。

原首采样仍为单 worker 的 R498 流式 gzip 来源；不自动混入 request234 的两 worker、R535/550 的另一 native 族或 R575 的新 Fourier 估计。

## 570.2　公开来源与同 job 生成关系

公开新桥为：

`computations/geometry_20261116_current_C_same_call_cubic_bridge.py`

其 schema 为 `R570-actual-same-call-cubic-capture-and-comparison-v1`，调用原 R569 修正后源 `6d27df22093e339fe8940bf24c57cff880d247a5f7f4fd478135adf2e4032f66`。R553、R521 仍分别为 `81d33e71…`、`4217bf9a…`；没有复制它们的数值核。

完整新 literal plan 有 56 个输出。它们必须在真正 computations 目录中、全部旧十层来源生成以后，以新 basename 创建；原文件不覆盖。旧 302 public 与 255 generated 全部保留。新加 R569、桥、当前 composer、当前 entry、完整新 plan 共五个 public，另加 56 generated，故实际来源集合为

$$
302+5=307,\qquad 255+56=311,\qquad307+311=618.
$$

这里的计数来自完整名称集合，不是用文件数代替依赖证明。所有输入及输出仍逐个绑定完整 bytes/SHA。生成层数为十一，其数量向量是

$$
(15,5,13,49,51,46,57,6,6,7,56).
$$

第七层的 57 保含历史 217 八件与实际 R544 四十九件。第十层 R567 七件仍为真实祖先，不被假称本次重新命名后的输出。第十一层才形成 R570 的实际 56 件。

其中较多文件只改来源是必要的：first launcher 的真实身份改变后，same-far 的 ORIGINS 必须绑定新 launcher；新 sampler 又是 worker/client 的真实输入来源；incremental-M union、checkpoint、SavedPrefix、radial、shared、cut、atlas、帽、metric/reach/held/material/display 随同一真实 tuple 逐层传播。跳过其中任一硬绑定而只改外层名称，会在已启动 owner 之后失败，或者错误归因于旧来源。完整 plan 将所有这样的变化分列，数值正文保持原样。

## 570.3　三个真实求解切点

本次明确形成：

| 原责任 | 当前新 driver | 原 phase |
|---|---|---|
| first 三主动453后冻结450 | `geometry_20261116_request239_same_call_cubic_full453_frozen450.py` | `design453`、`frozen450` |
| 固定112的真实五分辨率重求 | `geometry_20261116_request239_same_call_cubic_refined112.py` | `refined450` |
| 完整旧112/新增模态 union 后重求 | `geometry_20261116_request239_same_call_cubic_incremental_M.py` | `refined-M` |

三个切点均位于原 actual current-H、五 cut 比较、完整原 FD 已真实返回之后，原 `d.hooks.solve` 之前。新段在形式上为：

```python
capture = d.same_call_cubic.SolveCapture(
    d, args, problem, phase_dir, phase, Path(__file__), row)
with capture:
    status, context = d.hooks.solve(...原完整参数...)
```

原 hook 仍进入原 full-DN main；没有以另一求解器替换它。R569 包装的是该真实模块的 `solve_bvp`，返回给 main 的仍是同一个原对象。原流、boundary、separated、native owner、当前 profile、scalar controls、FD、full J、均值行及最终 gate 均未修改。

从原 `driver-status.json` 读取 actual acceptance 后，调用 `capture.finish`；之后仍按原 exit 与 `new_coupled_finite_acceptance` 决定是否进入原 checkpoint writer。未接受时不制造 capsule.complete；接受时 capsule 也不能倒过来制造 checkpoint.complete。

R570 不在失败后自行重试 solve。原 main 若本来进行多次 `solve_bvp`，recorder 逐真实调用观察，冻结的必须是与最终原接受结果逐字绑定的最后实际返回对象。它不补算 RHS 来伪造 `sol.yp`，也不调用新的 full-DN 入口。

## 570.4　透明性命题

**命题 570.A。** 假定原来源绑定成立，原 absolute deadline 尚有资源，原 recorder 的数组复制可完成，则上述切点保持原求解调用参数、原返回对象及原接受谓词；其新增输出只观察同一实际调用。

证明分为三层。

第一，`SolveCapture` 进入前后的唯一原函数替身由 R569 上下文负责。该替身先调用原 `solve_bvp`，读取其实际结果，然后返回原对象。原对象的 x、y、yp、p、rms_residuals 或 PPoly 均不被赋值。

第二，当前 driver 对原 hook 的所有原参数逐字保留。新 deadline 两参数只供旁诊断绑定当前 owner 的原绝对钟。它们不进入原残差、Newton 方向、Armijo、RMS、FD 或 native 容差计算。

第三，driver 仍先读取原 exit/status，然后执行原接受条件及原 writer。普通诊断 setup、数组绑定或写入错误被记录为 unpaid；它不将原接受改为不接受，也不将原拒绝改为接受。原 deadline 的 RuntimeError 资源异常继续穿透，原 owner 的外部终止/回收仍有效。这种资源停可能使本次未得到 checkpoint，不能说新增观察没有时间/存储成本。

因此命题是相同输入及可完成资源下的调用透明性，不是两个独立实际 run 的逐位结果或性能等价声明。新增来源身份、诊断文件及 elapsed 值当然不同。

## 570.5　真实 capsule 与九类成员

`capture.finish` 只有在原 status=0 且原 acceptance=true 时，才请求原 R569 `write_for_accepted_result`。后者再次绑定真正 `actual.json.gz` 的原 c6a 来源、success/status、完整 mesh 和 augmented states。其 mesh/Y 必须等于 recorder 同次返回对象的真实字，不能只凭尺寸或摘要声称相同。

完整成员为：

| 成员 | 实际责任 |
|---|---|
| `mesh` | 所有实际 solver 节点 |
| `augmented_states` | 全增广状态字，含主动参数所需状态责任 |
| `original_spline_rhs` | 原返回的 spline RHS，非事后新的 RHS |
| `ppoly_coefficients` | 实际 `sol.sol.c` 的全部四个降幂系数、所有 span、所有列 |
| `original_rms_residuals` | 原返回每 span RMS 数组 |
| `solver_parameters` | 原返回参数字 |
| `physical_states` | 原完整物理状态 |
| `frozen_physical_rhs` | 原接受结果内的物理 RHS |
| `recomputed_augmented_rhs` | 原接受结果内重算的增广 RHS |

所有数组以完整 C-order、little-endian binary64 保存，保留实际 shape、负零、bytes 和 SHA；不抽样、不低精度转写、不按列截断。物理维为 $3M+2$，增广维由真实 flow.dimension 给出。首453阶段和后冻结阶段的维数各按其真实 flow；增 M 不固定成112。

这些是 same job 的科学临时原件。不会上传 Git、artifact 或 cache，也不会放进必要正文。R569 result 保完整成员描述；新桥 status 另保原调用、来源、原 clock、实际接受、capture 可用性及错误。若进程在写中断，已写成员及原未完成状态继续保留，不能从目录存在推出完整 capture。

## 570.6　原 spline RHS、当前 frozen RHS 与 canonical cubic 不混同

R569 原接线保留三种来源：

- 原 solver 用于其 PPoly 的实际字面系数与 `original_spline_rhs`；
- 原接受结果保存的 `frozen_physical_rhs` 与重算增广 RHS；
- 当前准确 quintic 使用的节点与完整一、二阶定义数据。

这些对象可能逐字不同。R570 不为它们添加相等假设。R569 只记录实际可比较的字关系；若当前场绑定不满足原合同，比较 unpaid。

对某个真实 span $[s_i,s_{i+1}]$，令 $h=s_{i+1}-s_i$，$t=(s-s_i)/h$。canonical $C^*$ 由 $Q$ 两端自己的值/一阶 jet 定义。R569 的准确公式

$$
Q-C^*=\frac{h^2}{2}t^2(1-t)^2\bigl((1-t)\delta_0+t\delta_1\bigr)
$$

只是 canonical 差，不能代替 $Q-C_{\rm lit}$。当前比较实际读取完整 `sol.sol.c`，把它的降幂行转成当前 span 的准确有理幂系数，再与真实六项 quintic 系数逐项相减。对 $0,1,2$ 阶完整差使用原 Bernstein 包围；不预设字面 cubic 在机器节点严格 $C^1$ 或等于 canonical 插值。

本次不重证 R569 的多项式恒等式，新增的是取得其第三个对象及保持同场来源的可执行调用。

## 570.7　当前 CP、field class 和真实系数 owner

新的 source closure 通过 `register_runtime` 加入原 R569、R553、R521 及桥的完整 SHA；真实 driver 必须与它们位于同 computations。原 CP writer 记录实际 driver/source closure，原节点和定义文件不重写。

对 current same-C field，`BoundComparison` 从

`current.field.saved.checkpoint.receipt`

定位真实 `accepted-checkpoint` 的 phase 父目录，只读该 phase 的 status 及 capture result。它绑定：

- 真实 current run/source；
- 原 current deadline 文件的实际 bytes/SHA；
- 该 phase 原 acceptance/capture 可用状态；
- capture result 对应的原 full-DN 文件；
- 原 R569 对 CP、driver、完整 Y/DY、actual675 方法 owner 的全部检查。

它不把来自另一个 mesh level、另一个 M、另一个 job 或旧字段标签的 cubic 接到当前 Q 上。原 R569 仍从真实 `prefix_coefficients` 的函数/模块/source 确认 675 定义，而不是依赖继承后的 class 昵称。新 union SavedPrefix/CP loader 的实际生成身份也已传播，所以不能以原 R504 旧 tuple 短路当前检查。

## 570.8　同一次 target 与物理角量纲

same-C evidence 的原 `target` 返回已经由 R567 附带完整 prefix context，包括真实 numeric-s 区间、准确半径 $A$、准确弧长导数、二阶导数和径向度量项。R570 只消费这一返回，不为旁诊断另取一个可能不同的 C 盒。

设 $\mu^2=g_{ss}$，$\nu=A_s\mu$。准确物理角坐标中的目标为

$$
g_{\rm physical}=\operatorname{diag}\bigl(\mu^2,A^2\rho^2\bigr),
$$

其中 $\rho=\Phi_\phi$ 的下界必须来自当前真实 675 材料定义。R570 固定调用修正后的 R569；不使用已撤销的缺 $\rho$ 版本，不把物理角的目标简化为 $\operatorname{diag}(\mu^2,A^2)$。

$Q-C_{\rm lit}$ 的场导数差、完整 Gram 差及材料拉回都沿 R569 已付公式。共同材料共轭和全相位责任仍由原 field/target/coverage 链承担；单个 $q$ 或 $t$ 查询不能代替全部角圈或全 $t$ 证明。

本项量纲修正不改变 R553/R521 Frenet 正域多项式。若 $q=|d|^2$、$W=|d\times e|^2$，仍为

$$
P=A^2\mu^2W-\nu^2q^3.
$$

$\rho$ 的 metric 归一化与这个正域公式是不同责任；不能把 $\rho$ 再错误乘入 P 来改变已定义的 RHS。

## 570.9　完整 coefficient pair tube 与局部常数

同一原 prefix 单元上，R569 同时包住真实 Q、真实 $C_{\rm lit}$ 及二者全部仿射线段。所有 $3M+2$ 系数、两 mean、原 angular 子区间、完整 Fourier 合成责任都保留。它实际形成 $d,e,q,W,P$；只有原正域得到严格正下界时，才调用原 R521 常数接口。

单个 angular 子单元的 P>0 不是整个圆圈的 P>0；单个 prefix span 不是全 prefix。没有满足这些条件时，状态分别记录为：

- polynomial comparison 可用与否；
- geometric derivative gap 可用与否；
- whole pair positive tube 可用与否。

三者不是一个合并布尔门。多项式差可能已完整，而正域仍未付；不能把后者缺失反写为多项式不存在，也不能把前者存在升级为非线性 RHS 误差已证。

R521 所给仍是相应有限 Fourier/Frenet tube 的局部常数。原 cubic 的 whole-cell residual、FFT/table/RHS 形成误差、圆周投影尾项、准确 scalar 与 nominal scalar 差及原 worker branch 仍各自未付。R575 不是被本入口隐式执行；其 B2 全角条件也未由某个局部 cell 自动满足。

## 570.10　原 DFS 的分裂、退休与全域责任

R570 observer 放在原 `base_once` 的 prefix 分支中，原 relative operator norm、原 target 可用性、原 refine 判据、原四 Loewner 消费者及 root_plan 均不由它改写。

当原 cell 分裂，observer 返回 `original_cell_split=True`，该父格不作为已支付 terminal；完整子 frontier 仍归原 DFS。当原 cell 按原规则退休，observer 记录它的三项可用性、原准确地址及完整诊断身份。失败记录保原 cell、错误、unpaid 列表、scalar box 和 $d^2,W,P$ 原包围；全部逐列多项式/raw tube 仍在完整原 cell ledger。

**命题 570.B。** 若原 DFS 完成其完整闭域、未有原 error/stop/close error、完整 cell ledger 存在、同场 binder 可用，且每一个真实 terminal prefix cell 的某项诊断都可用，则对应 terminal 上界的最大值是该 actual prefix 的相应完整包围。

证明：原 root/piece/闭端点/反射和角分区的覆盖仍是原 DFS 覆盖。每次分裂由闭子集并覆盖父集；本 observer 不删任何子集。每个 terminal 的原 R569 包围在整个该闭单元成立。有限个 terminal 的最大值因此覆盖原所有 prefix 点。没有完整 DFS 或存在任何未付 terminal，代码不发 global-prefix complete 的布尔或上界。

代码还要求真实 prefix terminal 数大于零；空计数不产生 vacuous 成功。完整性依据原 `completed_all_DFS_work` 和错误/停止/ledger，不只是 terminal 计数相等。

即使本命题成立，它仍只给 prefix 的 Q/cubic 差或 tube。不能以它替代原尾、collar、patch、两帽、所有 seam 的完整 metric 结论。原全闭域 metric 路线继续独立运行；这个诊断没有新增 solver/metric 接受门。

## 570.11　三个实际必要 reader 与总读回

原 first reader、refined112 reader、incremental-M reader 使用不同真实 phase 路径。尤其后两者的原 `phase_documents` 来自两个独立 API，普通 JSON 分支会经过 `small`；仅在 phase 内写新 JSON 并不能声称完整字段已经传回。

本次因此在三条实际 reader 的原静止检查之后分别调用桥的纯 metadata 函数 `phase_capture_necessary`：

- first：`full-BVP/design453` 和 `full-BVP/frozen450`；
- refined112：`refined-BVP/refined450`；
- incremental-M：`refined-BVP/refined-M`。

它完整读 status、R569 result 和每一个登记成员；对成员流式核 bytes/SHA，但不计算数组数值、不 import 数值 backend。完整 result 为 true 时必须有全部九类成员。无结果但目录/成员存在时保真实 orphan identities；status 记录了 capture 而原件不在，则明确读回失败。缺 phase 是未启动，缺 status 是未返回；不会填成成功。

每一条调用在独立的原 quiet 分支中，不因前面的另一 scope 选择异常而悄然跳过。原必要错误仍进入原 L.fail/完整读回决定。后继总 reader 的 `solve_view` 明确新增 `actual_same_call_literal_cubic`，而不是假设 inner summary 的新键会自动穿透旧选择列。原同C reader 完整返回新 measure/compare summary，recovery 使用相同新增字段。

## 570.12　原时钟、owned lifecycle 与资源异常

三个真实 owned launcher 均将原 deadline 路径及真实 SHA 转给新 driver；其中 same-far、union sampling 原本就用该 clock，新增 driver 参数没有重建它。

桥绑定同一个 repository/run/source，要求原 schema、namespace 起点、18900 科学秒与2700读回秒。绝对截止点仍是原起点加18900；科学 observer 的工作和数组写入也耗用这同一余额。原 owner 的 stage cap、BVP 最大值、sampling cap、末900及 TERM→KILL/回收保持。

新 `OriginalDeadlineStop` 是 RuntimeError，普通数学/数据 guard 不吞它。源绑定、字节复制或文件 I/O 普通诊断失败留 unpaid，不能新增数值接受要求。原 noJ/J、全部576 stages、两mean、全列敏感性、当前H、FD、fullDN、原RMS/BC、final native、physical cut audit 均没有取消或放宽。

32 GiB 原启动门保持，R498 stored/decoded 全账本仍真正消费。这里不删除后继可能用到的原 far/candidate 数据，也不承诺复制 cubic 所需磁盘或源必要读回一定有余量。

## 570.13　同一字段、不把新来源误作新场证明

本入口在首次真实 accepted450 以后，仍按原完整 mesh→M、五几何、held、R459 全域 metric evidence/display 路径前进。新 source tuple 描述的是增加观察的实际执行代码；它不是一个已经运行过的新几何对象。

同 C/source/root 与十词仍依原合同；各 refinement 的 field 本来可能变化。固定目标的完整 construction/material 同场条件、准确材料共轭、全 t 证明和实际嵌套 t 查询仍原样保留。只有 actual current CP 与同 phase capture 绑定成功，才能比较当前 Q 与当前 $C_{\rm lit}$。

首 453 捕获只是原设计阶段实际对象，不能被 frozen450 或后继 M 当作其 cubic；完整 four-stage 标识及每 phase 目录防止这种替代。没有已接受450、没有同次 capsule、或同C measurement 未启，均只给精确未付状态。

## 570.14　必要容量、部分结果与清理

新完整来源层、capture member identities、每个真实 unpaid terminal 都保留。每个独立原必要语义体仍为90000 B；超过返回70，保持完整同job原件且不发该 scope 的 cleanup marker。本结论不证明 618 来源或任意失败数量必能装入90000 B。

正常/recovery不能把未知 quiet、缺原 reader、目录存在或 source生成complete 当作科学成功。全 source generation 记录十一层的完整已付/未访；不是只保第十一层。

清理顺序仍为实际 public239 guard →完整 source-generation marker →当前 same-C composition/必要/quiet →实际 source-entry marker →原 refinement reader 的所有原必要 outcomes/quiet。新的 capture 数据位于实际 BVP phase 内，随原完整 owned namespace 最终清理；原任何未付读回、超限或未知 scope 都阻止清理。没有额外抢先删除 callback。

## 570.15　完整合同的条件性与未付事项

**命题 570.C。** 对实际公开 Actions，若全部固定来源存在并与完整 plan 匹配，原科学链产生真实 accepted CP，原 recorder 成功保留同次 PPoly，后续 current-field binder 与原同C全域消费者真实完成，则本入口的新增报告描述的就是该同次 literal cubic、该当前准确 quintic及原 target 上的原 R569 条件量；它不伪造 accepted parent，不覆盖原科学判据。

证据是前三节实际源码切点、第五至七节完整 capsule/CP 绑定、第八至十节同次 target/原闭DFS、第十一至十四节必要与资源合同的组合。任何前提未发生，都由对应真实状态和未访范围保留，不从 SHA、源标签或成功子阶段推出后续前提。

当前仍未支付：

- 本 request 的实际 run、owner 接受、真实三层 CP；
- 真正捕获的完整 PPoly 与任一数值差；
- 原全部 angular/full-prefix tube 正域或 R521 常数的实际完成；
- 原 cubic 的全域等距误差及 solver容差到准确 metric floor；
- FFT/table/RHS/accurate-scalar形成差、R575 所需同场全角 B2；
- 原全闭场 metric/reach/held/反射 inclusive δE 与显示结果的实际完成；
- 固定预算/单90K中的必然完成、性能收益或误差下降。

这些不是新增门。原公开求解与消费者只按其原责任继续；本结论完成的是此前缺失的真正同次对象来源和当前 caller，不把来源工作当作课题终点。

## 570.16　固定来源定位

- 原 R569 source：`geometry_20261116_same_call_cubic_quintic_defect.py`，`SameCallCubicCapture.__enter__ / write_for_accepted_result`、`BoundCubicQuintic.__init__ / cell`，正式修正后 `6d27df22…`。
- 原675：`geometry_20261115_shared_active_interval_balls.py`，`ExactFiniteField.prefix_coefficients`，`675ab8df…`。
- 原 full-DN：`geometry_20261114_full_dn_solve.py`，真实 `solve_bvp` 调用与原接受输出，`c6a1f4d8…`。
- 新桥：`register_runtime`、`SolveCapture`、`phase_capture_necessary`、`BoundComparison`。
- 新 plan：`notes/r570-same-call-cubic-complete-source-plan.json`，56 baseline/output 与完整135个去重 literal 条目。
- 当前 source ancestor：[R567](R567-current-source-prefix-tubes-and-original-complete-field-chain.md)，完整238请求/工作流原字绑定；其已刊 source head 为 `a4c45fc70851164436ed2be48c531a54fbbec11b`。
- 真实 CLI、完整56输出身份、11层顺序与 cleanup字段见配套 `notes/2026-11-16-request239-same-call-cubic-complete-chain-interface.md`。

本记录不引用或转存正在运行233、238的科学日志，也没有用它们的未来状态充当上述任一前提。
