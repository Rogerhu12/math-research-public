# true53 四条新原行约束后的增广主问题与完整网格交换

日期：2026-11-16。此文定义一个新的有限研究任务；首次求解前必须加入[上一条完整方向观察](true53-positive-direction-complete-grid-unqualified-and-four-new-cuts-20261116.md)新得到的四条原行。旧finite主问题、旧正方向及旧64/32/Hildreth任务均已闭合；它们的全部费用只继承，不作为新配额。

## 1. 精确输入和要解决的新问题

唯一物理点仍为接受53，physical SHA `9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e`。g、b0、159→163原族、永久reference、配置、原pool顺序/版本、guard B=.00025及bank/learning记录全部保留。

输入只读取两个原始公开research log一次：

| 来源 | run / job | 执行源 | 原log字节 / SHA256 |
|---|---|---|---|
| 原完整MODEL/J/e/f | 43811870681 / 133115100791 | 42f95905deec3024dfee7a687bdc806d38c79baf | 35105831 / fa7edaf1419325ce31e6926de44f8c9ebbddf1ea554d140fafef61aecbc9ceb9 |
| 新四cuts、U/T和旧方向观察 | 43821568604 / 133145590135 | 323f36fefc0380898aa1e3c0f195e08a32f1fbc1 | 34802985 / cde578ee3e7c1046adbf2f7652aa8243679dca3ee1d1f7439938b82adb9c3454 |

原MODEL binding为e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1。第二来源CACHE字面JSON+LF共30232607B，SHA0c1826ad8f554b6eb2c440e54a5582a9711a05b023f4e2756c300d947d854b40，原U/T输入binding为75e07691773d43a00f4aa4192499721ff9490784feaaf18d983ef621e95893e7。

首次finite问题保原9658行，**额外先加**coarse43322、coarse91304、fine86645、fine182607，所以首次共9662行。它不能先重解原9658行作为基线或检查。原5743+5+4=5752个metric梯度均直接读入；四条新行保原grid/branch/row ID与de159/df159/g来源。

对每一新增原行，准确追加
$$
g_i^\mathsf T(\operatorname{step}\,z)+\mu h+\rho\gamma
\le \phi_0-\phi_i,
$$
其中rho=.001、mu=1e−6、step=.001qscale、d=.001gamma。原2937 hard、原163物理盒/范数652行、320上下界行、原常target=.26及全部已有metric行均不删除或放宽。变量仍为独立159的z、原物理范数h和gain gamma。

## 2. 同一任务的有限交换算法

1. 在首次9662行上执行原已公开的infeasible-start predictor/corrector代数。每个新problem至多96迭代、192个Newton系统；没有HiGHS、正则化、jitter、近等式投影或失败后备用求解器。只消字面完全固定坐标、字面零系数行，保原单位残差和dual。
2. 从最后有限161向量重取h=||Kz||∞，再由全部当前metric行修复gain。有限正primal只是候选，不自动宣solver最优或完整网格下降。
3. 原独立坐标做candidate=state+p，再取实际binary64的candidate−state；先按原3909 domain行及exact163盒判断。域未过即保记录，不做无意义源几何。
4. 对这个真正新方向做原两网全部一阶分支扫描：每点两个谱分支和原常target。未舍入理想p不另扫。旧已付方向或本任务已经完成的同方向直接读缓存，失败方向不自动重试。
5. 若完整原gain仍不合格，只对完整扫描的真正新argmax求原159梯度，并加入新有限矩阵。**下一次求解前必须至少新增一条不同原行**；同一problem binding不能重试。如果没有新行、没有有限正primal或达到明示轮数，保实际结果退出这个有限任务，不宣不可行、驻点或主课题完成。
6. 首个真正合格方向立即进入原合法区间scalar和原actual门；该固定源点任务最多接受一个新物理点。此后主课题消费结果继续open。

后继finite问题采用前一问题最后有限161向量作为warm start；它的原行集合已经严格增加。所有32轮共用一个科学钟和总计数，不为每轮重置600秒。

## 3. 必要一阶输入如何复用

U、T、e、f、a、a_s、null、radial、theta直接读取原paid记录；不重新生成U/T，不调用源普通geometry、旧selected-J或旧方向JVP。

原CACHE没有全部scalar_grid.fields与变分frame系数，本任务只恢复这些缺失的一阶输入：每网原fields一次，以及原Tu/Tv和Ts_value_part所需的两乘加。它不调用target_frame去重新生成T/Ts/U。

原选点一阶式是
$$
\delta T=F_0R,\qquad
\delta U=(a_sP_0+aP_1)R+aP_0R'.
$$
因此de=2U·deltaU，df=T·deltaU+U·deltaT，null5贡献为2U_z C与T_z C。原helper即使second=False也读取未保存的a_ss；本入口只按上述原一阶式填同(jet,mode)排列，R″槽为结构零，再用原expand_radial_rows。没有伪造a_ss或把此式用于曲率二阶导数。

完整角周期原函数先在原全部theta上做，再取原点；fine theta直接用原已付数组，不重排浮点乘法。新的oracle binding明确引用原75e076…输入、MODEL和5752行manifest，不冒旧scope身份。

## 4. 合格方向后的原scalar和actual

完整gain按原phi0减全网线性最大值再减mu||Kz||∞；阈值仍1e−10。只有实际舍入方向通过原域且此gain为正，才计算原guard兼容alpha区间。

原scalar消费同一次已付e/f/de/df，至多64查询（搜索62加两次未试fallback）；alpha=0仍是真物理基线，不用合法区间左端冒它。保原两个谱分支及常target；没有新的JVP或几何藏在标量搜索内。

最多3个实际pair、6个普通值，每个实际舍入候选先过原exact163盒与hard域，再用原coarse/fine全部14门。严格接受量仍为原eta至少下降1e−7；metric目标.26和其余硬门不改。若失败实际值发现新行，按原规则保该行并停止本固定方向，不在同一个过时模型上反复试。源点53普通geometry请求一律拒绝。

如接受54，直接从已经发生的ordinary coarse/fine缓存导出新U/T/e/f，0再次评价；接受、失败、实际行学习以及全部pool/银行账户均保真实记录。

## 5. 唯一新科学账户

从数值imports及两来源log读取前起同一600秒钟，覆盖全部输入、源24参数恢复、有限矩阵装配、每轮Newton、所有新方向、新gradient、scalar、实际值、失败、序列化与输出。明确上限：

| 计数 | 新任务上限 |
|---|---:|
| 新finite problem | 32 |
| 总Newton迭代 | 3072 |
| 总Newton系统 | 6144 |
| 缺失一阶上下文恢复 | 1 |
| 新完整双网方向 | 32 |
| 真正新原行梯度 | 128 |
| scalar session / queries | 1 / 64 |
| 实际pair / grid values | 3 / 6 |
| 源点普通geometry、旧hard-J、旧finite、旧方向重算 | 0 |

既付祖先为 **1658.9797906909998秒 / 128普通值**，包含上一条50.40678669899998秒及此前全部已登记失败。旧任务预算不化成剩余额度。开始即记账；任何失败方向、新行或Newton系统都保started记录。不能在失败后另启动同一任务并把该成本置零。

最终FINAL_CLOCK在全部大输出之后取样；checkpoint内较早费用不能覆盖它。只读report不导入数值库、不作研究计算，其观测时间单列。

## 6. 输出、复用和原始来源

只输出原plain stdout，不上传Git/artifact/Release/跨run缓存。每个FINITE_RESULT保实际最后161、原单位dual/slack/residual、真实问题binding、收敛状态、系统账和候选。每个新FULL_GRID_SCAN及ATTAINER_GRADIENT有独立原字面JSON+LF身份。

最后一个完整候选只保存它的de/df（合格则原line完整四数组只存一次）；源U/T/e/f不重复。若末方向只完成一个网格或末gradient链式比较失败，已算原数组仍保留并准确标记未完成/未安装，不能因失败消掉费用或已付数据。各已闭不合格方向保完整标量和哈希，不导出32组大张量，也不重扫它们。

新数学stdout总上限96MiB，原log只读上限112MiB，语义report上限7MiB。新接受点ordinary cache与最后方向cache是两个明确不同记录。报告保所有重复tag的序号/原字面哈希；完整checkpoint只给来源，不把大数组读入对话。

## 7. 新源码及执行

以下11模块均为源文本；没有运行开发、compile、旧例程或独立核验。唯一执行在本公开仓库新workflow上，由新request一次触发。

| 新文件 | UTF8字节 | SHA256 |
|---|---:|---|
| frame_metric_true53_augmented_scope.py | 5777 | `123f279783d21f6a983c63112c43afab5727c6139ed333643ef52b4c07e8c569` |
| frame_metric_true53_augmented_core.py | 17081 | `c8da03acc3a1665696bc820983be637be2c9678e5804c82302b84f996aaf1e1b` |
| frame_metric_true53_augmented_master.py | 9770 | `3d8c20abcb73be55538defed59a0646dceafa068d09e6c2b317bc4fb01b96458` |
| frame_metric_true53_augmented_domain.py | 11421 | `3190852c21ce49dc8629c39cb20b1928f56ebcf276ee18ac91bd109423f4db58` |
| frame_metric_true53_augmented_first_jets.py | 63146 | `5e80eac089ab8aafbcc32992147ba20754142ac1b33ead65c4be86e2169840f4` |
| frame_metric_true53_augmented_line.py | 13197 | `f2ca0df87344f2c7b27056794d01c760ad0d1d39318c0da97e0cfb7e6ded5f81` |
| frame_metric_true53_augmented_actual.py | 26577 | `e4dfaf7f09d0077b51033e9f3fcab44f0d1c885b7801b6d816ba4b7c91314f6d` |
| frame_metric_true53_augmented_transfer.py | 12210 | `de035d4da64b62dfaee16ac8e1929a63a790f85512531f0f63d2cd28071b619c` |
| frame_metric_true53_augmented_accepted_cache.py | 18292 | `5bf6396cdb98b5ab1ed7c718f58930b84f37439b1fee458ac588e5405194bdef` |
| frame_metric_true53_augmented_audit.py | 33988 | `d5e2784e7870ceefde77fdb8e91cdc4afda986a10eeef620b132222b3f9c4601` |
| frame_metric_true53_augmented_report.py | 35224 | `5a626951c9def598259759178e69de1c1297176c4226e7823f8a600c402dd895` |

工作流 `.github/workflows/visible-true53-augmented-master.yml` 使用原固定Python3.12.14、NumPy2.3.5、SciPy1.17.0、Clarabel.11.1及单线程。每个research/report job先真实pull两个仓库，检查根/题README差异及私有QUEUE本会话唯一进行中，然后清除MR_TOKEN，再回到绑定源提交；有规则变化先交差异而不越过。

root已全文读新cache-fed oracle、finite入口及其同一账/原门接线；所有来源由request的源码SHA绑定。旧predictor/corrector纯代数helper引用原 `frame_metric_true53_paid_master_central_path.py`，SHA29672cb2cd041adfce547c3fb04a679b7d4d6238f464c3af3ee6e9f061e56ae6；它的旧执行不重启，新的严格增广矩阵在新owner下计费。

无论本次找到新点、产生更多cuts、遇输入错误或达到某个有限任务上限，都继续下一实际子问题。原固定g误差、连续C²、全时嵌入/reach、hold幅度和精化下降完成门仍未达到，不能以本设计或任何有限solver状态收尾。
