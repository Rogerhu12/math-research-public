# R715 中心化表示的严格同报告 seed 费用适配

## 1. 交付范围

本次独立派生两个完整科学源：R713 的准确中央 profile 矩及参考角 jet/node 费用消费者，以及完整准确 mean 方程积分 producer。原 `82e6f1a7…` 消费者和 `581fbcc3…` producer 均保留，原 schema 与守卫不放宽。新文件只接受明确绑定的 R715 driver、reader、normal 算子、calibration helper 及真实 seed batch。

这里没有选定实际 batch、没有运行积分或区间计算、没有构造假的报告或 fee request。两源是候选到达后可用的完整消费者，不是当前求解入口的前置条件。未运行的 plain R711 或 plain centered 分支不因本适配而成为必须先执行的科学步骤。

## 2. 精确完整来源

当前 plain-centered 变体固定接受：

| 角色 | SHA256 |
|---|---|
| R715 driver | `92233b4ffb0aaff1644e0c4bc9e7357a8eae37bd68e6d02ef0c6e0dcfbb31b81` |
| R715 pure reader | `7fc213c108245cb2c555d573a52961fd07f1b941d85411e8e6e8d8c22f20a5bb` |
| R715 normal field | `b2597012ec8ee063fabbb49a758b592d10f607de55ded3becaa8b62b6a50118d` |
| R715 calibration helper | `a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873` |
| 原完整 R711 provider | `0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b` |
| 原完整 R711 mean kernel | `f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917` |
| 原完整 R711 base | `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865` |

新完整执行文件为：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `reference_centred_smooth_triangle_seed_angular_jet_error_bounds.py` | 48220 | `ded2f37b2cccd98fff1b812e79013301cc04cc5bc34c3629e068cfc859727b11` |
| `reference_centred_smooth_triangle_accurate_mean_residuals.py` | 40316 | `7596defae9f81580c9db4e7ff593b98825843dcb9d16d73bc798d2be279ffd74` |

两源均小于 100000 字节。完整源码再生器 `derive_reference_centred_seed_fee_adapters.py` 严格读取原完整数学源与四份新执行源，再核实际 driver source registry、report/reader/field/helper schema 闭包。它只生成完整文件，不 import 科学模块，不构造任何候选。

## 3. 同实际对象的绑定

消费者首先执行本表示的完整 pure reader。它捕获原报告字节摘要，在读取前后核同一份报告，随后独立检查新 driver/schema、完整 field canonical identity、实际 endpoint/helper/source roles 和冻结参考定义。原初点、base、seed、mean kernel、固定 scalar 和 chart 都必须与该报告相同。

在原完整 batch 身份之外，新 binding 明确保留 outer report schema、完整模型摘要、operator 源、calibration 源和完整 centering 定义摘要，以及原冻结初点摘要。plain 变体明确拒绝含 `normal_frame_C1_reuse` 的 cached 模型；后继 cached 变体必须使用自己的独立硬 pin 和 schema，不能把缓存模型改标签送入 plain 消费者。

实际 batch 必须已由 provider 完整返回，并与 pure reader读出的 batch 列表一致。其 runner raw NPZ 的全文摘要、seed 模型、全部原角顺序、九个向量 jet 数组和六个标量/moment 数组均由原完整 `bind_actual_batch` 保留检查。显式 `--batch-arrays` 只改变文件位置，不能改变原字节身份。

fee request 必须使用新请求 schema，并同时匹配原报告摘要、seed、raw batch、固定 scalar/chart、实际 batch index 和完整新增 outer attribution。不能把旧报告、另一表示或另一 batch 的请求改标签消费。请求中每个实际 literal angle 仍有其完整准确误差输入；缺项不设为零。

## 4. 数学方法及 journal 没有被替换

实际静态 AST 比较得到：R713 原 33 个数学/工具顶层函数及 Interval 的全部 15 方法相同；只改 `bind_actual_batch`、main 的请求/输出归因，并新增 `bind_outer_report_scope`。准确 mean producer 的 ActualMeanBatch 全部 14 方法、CompleteLeafJournal 全部 10 方法和原 14 个非 main 顶层函数 AST 相同。

因此仍由原准确四段标量 law、全部准确 affine 节点和支持/端层边界组成积分分割，保留整个补集与无穷平尾。候选是实际返回的 $v,v_\phi,v_{\phi\phi}$ 全部 literal 字；边层归一化和三角 jet、完整准确 $K$、中央准确 mean 方程 $L_cv$ 的责任不变。原完整 leaf journal 的哈希链、自然小批返回、全覆盖后才产生请求、精度目标未到但完整盒仍有效等语义不变。

新 producer 采用独立 journal schema，且实际 binding 包含新完整 producer 源与消费者源。因此旧 journal 不能静默当作新来源计算的完整证据；同一新真实 batch 的后继可以按原准确字节和 journal 接口继续。

R713 中央十二段 profile 的准确绝对矩、Taylor 余项、$A,A',A''$ 盒与真正 $λ$ 参数费用保持原完整公式。准确 mean producer 仍明确 `profile_moments_computed_here=false`，不冒已经计算 R713 中央矩；这两步具有不同职责。

## 5. 已付和未付责任

这些源支付的是固定参考 seed 的完整 mean 方程 residual，以及在外部准确输入成立时的参考角 jet/node 误差。它们不会因为 outer report 是中心化表示，就把下列量混为一谈：

- 准确 mean 方程的中央项 $L_cv$；
- provider 实际使用的 $λ,d,w$、中央正权规则及其误差；
- outer normal 的原胞 Gauss/cumsum 工作积分；
- helper 实际记录的 $\delta_{\rm ref}=P_0-\Gamma_0-Q_ST_{\rm ref}$；
- 当前 normal 根及全部跨段隐式角 jet；
- 当前 raw closure lift 与六个物理 jet。

新增输出明确保留 `numerical_raw_reference_calibration_paid=false`、`complete_outer_normal_root_and_implicit_error_paid=false` 和 `complete_R715_physical_lift_and_sixjet_error_paid=false`。完整 source/model attribution 只是证明这些 seed 数据属于哪一个真实运行报告，不能提升为整个 outer 场的误差证或几何证。

后继要完成 R715 同场费用，仍须把准确参考 node/整胞费用、实际 outer 归约误差、原 core inverse、当前 normal 误差和完整 lift 的 $h,h',h''$ 传播接起来。R707/R715 的完整误差账不能被本次 source adapter省略。未知费用也不能因为参考工作残差小而默认为零。

## 6. 真实数据到达后的完整使用接口

只有真实报告中出现完整 `mean_batch_records` 后，才可选择其实际 index。选择时记录该报告的实际 source/model/字节摘要与该 batch raw NPZ 身份；当前文件没有预填 index=0 或任何未来报告摘要。

第一步准确 mean producer接收 `--repo`、`--report`、实际 `--batch-index`、必要时仅定位同字节 NPZ 的 `--batch-arrays`、同报告的五份原 reference 输入，以及独立 `--outdir`。其预算、panels、precision-bits、width-goal 和 maximum-transitions 沿原完整 CLI。完整覆盖才生成 `fee-request.json`；不足覆盖则保留 journal及诚实未返状态。

第二步新 R713 消费者读取同一 report/index/NPZ 与这份真正生成的新 fee request，使用独立 `--output`。它按原完整规则计算所有已请求实际角的参考费用，不额外调用当前 F/J、normal 求根或几何扫描。

这些科学步骤只允许公开 Actions 执行。不存在为了当前 solver准入而必须先跑的 fixture，也不强加未来费用消费者作为完成标准之外的新门。

## 7. Cached 后继的独立来源

construction 的 R714 cached-centered 表示拥有新的完整 operator、calibration helper、driver、geometry 和 reader。只有其终版完整来源确定后，才在再生器中加入一条精确固定合同，另生成独立 cached-consumer 和 cached-producer。

cached 合同需要额外核同一实际 source registry 的 C1 helper、模型 `normal_frame_C1_reuse` 的完整 canonical identity、保全所有 stage 和一次外参数导数的来源声明；它不能只换一个来源标签或复用 plain 的 byte-bound 读取入口。准确 seed 数学方法和全积分 journal仍可逐 AST 保留，实际报告与 batch责任则重新绑定。

## 8. 完整再生器与实际纯文本再生

本次完整再生器为 16689B，SHA256 `9cb26e3173c3085eebf5d9e17f6d7861dfb06957ede66cd2b0cb759b2b3c0a95`。以 `--variant reference-centred`、完整仓库 `--repo`、上述六源所在 `--entry-source-directory` 和仓库外 `--outdir` 即可纯文本再生。根全文核全部派生逻辑，并实际在临时目录再生，两完整执行体逐字匹配上表；所有原算术/积分/journal方法保留。没有导入科学模块或生成实际 batch。

可再生的 `reference_centred_smooth_triangle-fee-adapter-source-lock.json` 仅在临时目录；2623B，输出 SHA256 `8f9324266e99f017bf0f8170d463b6c12ecdfbc81b8c3a9bfd4b55637cee27c6`，不入 Git/Release。完整来源与真实输出身份仍分别按本说明和将来的实际运行记录保存，未支付费用不改为零。
