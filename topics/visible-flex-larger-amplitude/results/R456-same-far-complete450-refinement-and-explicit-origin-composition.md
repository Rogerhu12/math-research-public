# R456 — 同一完整 far 条件、真实 450 细化与明确来源的组合

作者：geometry agent（AI）。日期：2026-11-16。

本文支付的是独立源码的条件组合责任。它把 [R450](R450-same-family-finite-far-reuse-and-fresh-native-sampling.md) 已证明的同场、同有限 far、同实际 $\mu$ 表示复用，接到 [R448](R448-fixed-target-radial-mesh-and-joint-resolution-refinement.md) 的真实径向及其余四分辨率细化；并为 actual202205 的实际 [R452](../notes/2026-11-16-actual202-ten450-first-closed-parameter-block-interface.md) 首构造来源登记独立分支。它不修改已发表的 R450、R448、R452 或任何正在运行的实验。

本文没有实际父场、细化因子、接受点、实际资源结果或运行号。全部新科学执行仅可在本公开仓库 Actions 进行。当前交付只有源码、条件证明和可调用接口；本地未导入、编译或执行这些科学源码，也未构造数值 fixture。源码中的原接受条件是既有有限程序的条件，不是连续曲面的完成证书。

## 456.1 对象与独立来源

固定 $M=112$，频率为 $m=2,4,\ldots,224$，原 native stage 数为 $576$。完整物理未知量是 $338$，冻结全部十个标量参数后的场未知量是 $450=338+112$。双 mean、所有模态、全部 $338\times112$ 末端响应、原 FD 和独立 audit 均保留。

称 $\mathcal C$ 为由当前真实 C 输入绑定指定的准确模型 C 根族。该绑定包括原参数、全部有限头和深端来源、原准确 cut、实际 C cover 和完整 deep graph 结果。准确目标还固定原连续十族的完整 DAG、cut/window 约定和全部十个准确 binary64 有理词。本文始终区分三层对象：

1. 准确模型 C 的完整根族与准确十族目标。
2. 原实际 full-far 生产器给出的全部候选、单位行族、误差和完整有限域证明记录。
3. 被原生产器明确选出的有限数值代表及后续 native 求解程序。

第三层不是第一层的已认证共同精确实现。新源码维持原 `exact_global_C_realization_of_numeric_representatives_certified=False`。单个几何盒、单位行盒的任意中心，或一个已返回的数值 J，都不能消去此区别。

新的原始调用来源只有以下三个实际元组；源码按完整 SHA 和 schema 匹配，不从目录名或 `completed` 标签猜来源。

| 来源 | 实际 full453→frozen450 驱动 | 实际 launcher | 原绝对时钟 schema |
|---|---|---|---|
| original193 | `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` | `request193-owned-job-science-deadline-v1` |
| joint203 | `5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592` | `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7` | `request203-owned-job-science-deadline-v1` |
| actual202205 | `56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615` | `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7` | `request205-owned-job-science-deadline-v1` |

actual202205 是 R449 的准确十族实验来源，不是把 joint203 的执行标签改名。此处采用含准确模板 `cut_radius` 的最终 R449/205 身份。旧 `6bb491…` 驱动和 `47f9e161…` launcher 不在新分支中。

## 456.2 允许复用的完整 far 对象

设原 full-far 生产器实际返回结果 $G_0$。复用条件是原 R450 的全部条件，特别包括：

- 本次同一仓库、同一 run、同一 immutable source checkout 的原完整结果与配置仍在临时目录；所有所需原件可实际读取。
- 原准确 C 输入绑定、物理 cut、有限物理 far、完整 deep 图、R380/R357 证明来源和全部 $112$ 模态相同。
- `actual_far_modes_completed`、`complete_factorized_far_modes`、`complete_unit_far_row_modes` 均是完整原模态表；全部 required leaf 已完整支付，没有未开始模态、未付候选或未提交 panel。
- 全部候选的完整单位行、方向、误差和逆像闭覆盖仍由原真实记录承担。原 far inverse span、全部 mode 行、完整行文件、矩阵、node-$\mu$、所需前缀与原大 ledger 字节身份全部保留。
- 原数值 far 点的半径、$w,w_r,\log w,(\log w)_r$ 及其误差记录不变；原有限 far 矩阵和 far node 的 $\mu$ 逐 LE64 字复用，含负零。

这里“完整读取”有明确层次。原 R450 binder 实际解析需要的所有 mode/candidate/leaf 记录并核完整字节；成功 coefficient、factor、panel 等大流只以原完整 hash/计数和其原生产者证明责任绑定，不重新进行每数值的科学证明。新必要摘要不会声称这些大正文已经工具侧逐值读回。

这些是被复用对象的身份及其已经声明的数学范围，不能用一个 `completed=True` 或仅 cut 三盒替代。若缺任何原件，不能从旧 SHA 重建它，也不能把缺失解释为真实共振或域失败。

## 456.3 为什么必须连同实际 $\mu$ 复用

在原 $(Q,\Pi)$ 坐标中，物理量关系为

$$H=r^4Q,\qquad H_r=m^2r^3Q+\frac{\sqrt{12}\,\mu}{r^4w}\Pi.$$

因此，从同一物理 $(H,H_r)$ 法向行转到 $(Q,\Pi)$ 的行系数依赖同一个实际 $\mu$。若仅重新取一个 far 点盒中心导致 $\mu$ 改变，不能继续复制旧 $(Q,\Pi)$ 行。R450 已给出该表示的条件证明；本组合不重新选择 far 点或 $\mu$。

新 sampler 把原完整 far sample 装入同一实际半径词对应的缓存，将新网格中的该点绑定到原 sample。新 node-$\mu$ 的 far 端点明确复制原词。其它新节点的样本和 $\mu$ 必须由同 C 原查询/区间接口重新产生。由此，新 native 使用的 far 行与其 far 节点坐标保持原关系；不是把另一 $\mu$ 的数值行或误差重标。

更换 $M$ 不在本结论内。对新增模态，没有可由本次 $112$ 行自动推出的 far 行。R442 的 M 路线、R451 的 M 几何以及它们与本调用者的注册继续独立未付。

## 456.4 新网格与旧边界条件的组合

设 $\mathcal S_{N,h}$ 表示由实际参数 $N$ 和原 `steps` 配置及其实际 schedule 生成的完整数值 native 系统。新采样保持原 $576$ stage 和全部 $112$ 模态，仅采用显式新 $N'$、steps 及其它角参数；其有限算术映射一般不同于旧映射。

在同一 $G_0$ 的条件下，把原 far 行和同 $\mu$ 表示用于 $\mathcal S_{N',h'}$，是同一个原 finite-far 条件在新离散系统中的使用。由 456.2–456.3，其候选族和误差责任没有缩窄，边界行也没有被另一个坐标行替换。由 R450 的 fresh-grid 合同，全部新所需点除准确绑定的原 far 点外都真实重新采样。因此可复用的仅是 far 条件，不是以下任何对象：

- 旧 native 非线性状态或旧 response；
- 旧 $H\mapsto\text{response}$ 映射或旧 affine predictor；
- 旧 J、QR、因子、同一批 RHS 解或其接受状态；
- 旧 mesh、FD、full-DN、末 audit 或闭面几何证书。

新 worker 与 client 的派生只改独立 source/schema 和当前 sampler 名称。原完整 native owner、同步 bridge、QR 核和原数学运行源仍按原完整 SHA 载入。新 worker 的第一次状态仍是原完整零初猜；后续 predictor 只能来自此次实际 live owner 已返回的状态和完整敏感度。原 $32$ 次、十档、$2\times10^{-9}$、$\eta=0$ 全敏感度、两 mean、全部 far/cut 行保持。

因此，若新 native 或 full-DN 原程序接受，它只表示新离散系统通过自身原门。它不证明精确 C 的无限非线性 DN，也不证明相邻网格的误差递减或某种收敛阶。

## 456.5 真实父链和重复细化

原始来源必须真实完成 full453 和独立 frozen450 两阶段，具有它自己的完整 final/FD/checkpoint/quiet 状态。新 R456 owner 只接受以下父链：

1. 原始来源本身的实际 frozen450；
2. 对 original193，已发表 R431 的真实 mesh450；
3. 已发表 R441 的真实 resolution450；
4. 已发表 R448 的真实 radial-resolution450；
5. 本独立 R456 owner 自己已真实返回并被原门接受的 refined450。

每个分支核实际 launcher、driver、writer、checkpoint、origin 和同一 deadline。旧 R441/R448 父用原 `bf7dedd2…` writer；原始 193/203/205 或 R431 用其真实原 `43f217…` writer，不能改旧 manifest 的 writer 或 driver 标签来进入新分支。R441 已有 `load_parent_checkpoint` 负责读取这两个真实 checkpoint 类，R456 不更改它。

对于首个 R456 细化，保留的 original full-far 结果必须正是父配置所消费的结果；`original_config` 必须与实际父 checkpoint 的 native 配置具有相同 bytes/SHA。对于后继 R456，必须沿父结果的 `same_original_far_family_reuse.original_result`、原目录及父配置的 `R456_same_far_fresh_grid_origin.original_config` 追到同一个真实原件。不能把已经复用的结果伪称重新传播的原 full-far 生产者。

原配置与新配置除明确变化的 N/steps、样本路径与身份、公开 provenance、以及三个独立 sampler/worker/client source 项之外，全部字段相同。阈值、资源参数、原算法来源、runtime closure 或未知配置项不能在此比较中被顺带丢掉。新驱动在实际加载父 checkpoint 后再次独立绑定新结果和原 far receipt/$\mu$，不只信 owner 的状态标签。

归纳地，任何有限次成功 R456 细化仍固定同一个准确 C/根族/十参数目标及同一个由其父链明确指定的原 finite-far 条件；每一步的状态、J、接受和 checkpoint 均来自该步真正的新求解。该归纳不需要、也不推出每一步都会成功。

## 456.6 五个细化因子与完整原 450 算法

五个因子为 `radial_mesh`、`field_and_native_angles`、`native_steps`、`material_angles`、`physical_angles`。每个是显式正整数，至少一个大于 $1$。仅径向细化时，其余四个可全部为 $1$；不能用旧 R441 的条件拦住这个合法分支。

对每个父闭区间 $[x_i,x_{i+1}]$，径向因子 $f$ 请求

$$\operatorname{RN}_{64}\left(\frac{f-j}{f}Q(x_i)+\frac{j}{f}Q(x_{i+1})\right),\qquad j=1,\ldots,f-1,$$

其中 $Q$ 表示原 binary64 字对应的准确有理数。新 seed 并入全部原节点和全部 literal profile knots；相同值优先保父词。每个区间和每个细分地址均须考虑。实际机器折叠、重复值、当前区间、未访后缀与资源容量按原 R448 记录。

父 Y/DY 只定义新初猜的原 Hermite 插值；父 DY 不是新解的 RHS。全部 $450$ 行在新节点上真实重求，随后执行原完整 preflight、当前 $H$、完整 $338\times112$ J、原 FD、原 full-DN、真实末 J 和独立 finite audit。若原求解器进一步自适应，其末网格以实际输出为准；保父节点词是新 seed 的合同，不是末解不许变化的断言。

显式 `max_nodes` 无法容纳完整并集，或所要求径向细化没有产生机器新点，是资源 partial。不得删点、遗漏 knots、截掉模态或宣称收敛。N 等整数超过原接口的安全整数范围也按原资源责任停止。

## 456.7 单一原时钟与三个实际 child

owner 不创建新的 namespace 科学时钟。它核真实 origin 的 `actual_job_deadline` 原文件 bytes/SHA，recipe 来源和原 $18900+2700$ 计划；绝对科学终点仍是原 namespace 创建时刻加 $18900$ 秒。外部规则同步、工作流硬限和原必要读回仍由后续具体 caller 负责，本 requestless 源不假称已经接好一个工作流。

三个 owned child 分别是：

1. `sampling`：原完整 far binder 加真正 fresh-grid；
2. `configure`：只生成新配置的元数据进程；
3. `refinement`：全新原 450 求解。

`sampling` 与 `configure` 共用一个显式 process allowance。configure 启动前从该 allowance 扣去 sampling 开始以来实际经过的时间，不能再给它一份全额预算。每个 child 的有效预算还裁剪到原绝对科学剩余量，保原 shutdown reserve。TERM/KILL/reap、PID/start-ticks、独占 PGID 和实际 quiet 全由原 OwnedChild 合同支付。

这不是“所有 setup 和输出操作都零成本”的承诺。父级元数据绑定、返回记录写入和原 shutdown 仍有实际成本；所有实际阶段和资源停止必须报告。尤其 sampling 成功但 configure 未完成时，`actual_sampling_completed` 保真实完成，而 `actual_configuration_complete` 不会伪置真。完整新 BVP 只在两者确实成功且 quiet 后才启动。

资源截止、信号、文件缺失和工程异常不等于数学拒绝。完整停止状态、未付 scope、未开始阶段以及真实 child 日志都留在 owned 临时目录；这些源码不会删除原件。

## 456.8 actual202205 的第一闭构造 A/B

新 resolution checkpoint 的完整径向、shared field、accurate cut、帽、metric、reach 和 held 仍使用原 R441 数学消费者。此处的新增内容仅是实际来源注册与同一构造的消费，不重造几何核。

所有来源都保 R448 的 first-shared 合同：实际同目标 shared result、完整 plan、全部 W/H/marker 词及顺序、原 cuff 与实际 first checkpoint 均须绑定。cap height 不进入帽的 target metric；冻结 H/W 仍是本次具体几何构造保持责任，不能据此掩盖材料 $\Phi$ 的变化。

对 actual202205 再明确读取实际 R452 首 procedure：

- procedure 的 source、input schema、`upstream_kind=actual202205`、原 origin launch 和 deadline 相同；
- `shared_field` stage 的真实原结果就是本次声明的 first-shared；
- `actual_selected_construction` 指向原 `initial-construction` 的 A 文件；A 的 policy source、deadline、首 checkpoint、准确 target、十词、完整 construction words 和首完整112材料定义均实际读取并绑定。

若实际 B（`first-material-transport.json`）已存在，新来源核其完整原 bytes/SHA、policy、A、首 checkpoint、target、十词和全部构造词，并实际读取完整原内容；大 registration/normalization 正文仍留在临时目录。若 B 因原 held-witness 阶段尚未产生而缺失，明确记录未付，不把它变成新的 metric/reach/held 成功前门。原几何在当前材料图上仍可按既有合同进行；共同首材料图的结论继续未付。

特别地，保存 B 不等于已经执行 [R443](R443-common-material-angle-pullback-and-fixed-closed-target.md) 的 $\Theta_j^{-1}\circ\Theta_0$。新来源也未注册执行 R447 的公共材料 evaluator。当前 core、$\Phi$、SE2 和 R249 归一化仍由当前真实场重新产生。本文不声称闭域 tensor 分量逐词等于首场，也不声称统一 $C^2$ 收敛。

## 456.9 几何责任和读回范围

新 postsolve 对同一新 checkpoint 重新执行原五个角色：radial replay、原 cuff atlas、shared field、live-query metric、完整 block reach。metric 与 reach 独立；reach 不借 metric 成功，held 仍只以真实前三几何输入为前置，并独立使用原 held 数学源和原时钟。所有 K、$\tau$、$\eta$、工作预算和 witness 参数必须由未来实际 recipe 明确给出，本文不选择它们。

新的 owner 必要 reader 只导入原标准库元数据 helper。对 sampler，它采用 R450 必要范围：完整复用模式 scope、原 far/$\mu$ 身份、全部新 unpaid 记录、所有新 ledger 字节/行数以及完整新数组身份。成功的大候选、factor、点值、J、state 正文不搬运，也不声称工具侧已逐值核阅。

对新 450，它保全部实际 mesh 地址和未访范围、原 FD 全层、真实末门、每次 native call 原标量、末 call 明细与全部失败/未完成 scope。对 postsolve，它保原 block/frontier、当前 singleton、union、curvature/live-query 未付地址，以及新增第一 A/B 来源摘要。缺键与显式 null 不混同。

每份必要正文仍只允许 $90000$ 字节。超过即如实返回70，保原件，不分包、编码或改限。必要 readback marker 只有完整已选择 scope 成功且实际 quiet 时才写；仍不能单靠它删除旧 origin、第一 A/B、原 complete far 或其它尚未读完的责任。没有流程会把 reader 成功解释为科学成功。

## 456.10 本结论的精确边界

本组合可执行地消除了“R450 有 sampler，但 R448 仍重算 far 且只认旧 source”的接线缺口，保同一准确 C、完整 root family、原 far 表示及新求解责任。它不提供任何实际成本减少或完结保证。

尚未支付的责任包括：真实 accepted450 的出现；本调用链实际执行及全部末门；finite geometry 到准确 C 的共同 realization；无限 DN；统一收敛；完整同首材料图的实际共轭；最终全域 metric、reach、held、$\delta_E$；以及变 M 后本调用链的真实来源注册。它们均不能由 source/schema、配置比较或一个新 checkpoint 标签自动支付。

本文的充分条件若由未来实际运行支付，所得结论严格限于原有限程序及相应原几何消费者实际返回的范围。任何停止都保未付，不把条件结论冒充完成课题。
