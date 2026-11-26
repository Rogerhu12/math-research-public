# 真实分批末态与中断检查点的峰容量续接（2026-11-26）

本包续接run45796862274/sourcecada9c850a1a90a6709bf182bac8b8414497919b。两lane的原收据已分别登记，不把B038中断补造为FINAL。

## 两份输入及不同完整性

| lane | 原actual | 本次采用的recorded proposal | q/trust来源 |
| --- | --- | --- | --- |
| B030 | 450径向、1536角、1021峰轨道 | 494径向、1536角、1129峰轨道 | 自然FINAL的完整保留q；trust1.20135498046875原样 |
| B038 | 500径向、1536角、538峰轨道 | 502径向、1536角、540峰轨道 | outer3最后完整START的恢复q；actual trust.9010162353515625原样 |

B030的最后fine观察eta=.2651373529074538、raw几何V=0，因1129>1024真实峰库容量返回。本次把额外峰容量改为2048；**径向仍513**。没有丢任何旧均匀约束或已知峰，也不回放早先joint/513/batched初轮。

B038的最后完整START q与outer2 OUTER的保留q逐项相等，实际500/538与上一proposal逐项相等。其1001×3072扫描和566候选全定位得到eta=.4946622256480169、raw V=0。本次采用START写出的两个额外pending坐标；outer3被拒callback另报了一个pending计数却没有坐标，随后runner shutdown。这个原缺口仍明确为1，不能宣称本次恢复关闭瞬间全部pending，更不能用未写出的被拒trial q。

两lane的完整81q、实际/提议径向和峰库、trust及q二进制SHA已经只从原日志逐项核验。B038下一trust是明确保留当前实际trust，不冒称未完成outer3已经产生了trust更新。每个新网格都重新完整fine扫描/定位并据新门判资格，原有限合格不自动继承。

实际状态JSON：B030124272 B、SHA256 ee286ba4fde3b2977746dae9065fab1978b33c80cf9a2fff7fd56f748dbe5712；B03876227 B、SHA256 f0abeb56f361906a93a9245867bbd2292323c7ec337b26b791981f138cb0435d。这些是实际下一计算参数，不是原日志/场数组缓存。

## 完整输入的 stdin 传输

B030状态已经接近单argv常见131072字节上限，后续峰库继续增长不能截断或丢峰。新独立stdlib runner run_inverse_state_stdin_20261126.py 将完整JSON直接传给子进程stdin，argv只保@stdin和SHA256。SOURCE输出精确字节数/digest；子入口核digest后解码，DEFINITION完整输出解析后的输入。没有临时科学输入文件、artifact或跨run缓存。

真实公开/私库pull、README差异/QUEUE核、固定源checkout与版本核、科学前删除凭证的函数与原runner逐AST相同。传输修改不改任何pull或授权边界。新入口 source-state-sha256 是runner生成的实际传输摘要，不能用一段缩减状态冒充完整输入。

## 完成 callback 即刷出可恢复状态

B038实际shutdown暴露了只有后端返回时才刷q/pending的缺口。新独立driver在每次完整callback评估结束、后端继续前，输出THETA_PEAK_CALLBACK_CHECKPOINT和原JSON hash，包含：

- 当前实际保留q及其完整fine/角峰观察；
- 当前实际径向、1536均匀角、完整额外峰轨道与actual trust；
- 全部本轮pending坐标和明确尚未优化的下一径向/峰库；
- 已完成的最后trial q、资格、实际约束违约、完整fine结果和FFT比较；
- 已闭outer的oracle总账、当前尚未折入的两oracle计数和row/AD计数；
- 本次实际elapsed与完整原成本ledger。

既有几何恢复规则会保留每个完整可行trial，即使违约改善不到1e-10计数阈值。该保留更新现移到快照之前，标记finite_observed_geometry_restored_below_progress_threshold；接受计数和trust计数规则不变，打印后只触发原GeometryRestored退出。这样快照不再落后于同次完整callback产生的实际保留态。

trust适应尚未发生时明确标记；只有后端结束后的原规则才改下一trust。新检查点不把trial自动当接受，也不将新proposal叫actual。原最后自然OptimizeResult、实际末态、pending和最后trial的分离继续保留。

计数快照将“当前未折入”与“已闭outer”分开，不能将两者在同一最终总账重复相加。旧B038shutdown后未刷出的工作仍单独携带，不因新入口重置时钟而消失。

## 科学算子及接受门不变

原locate_peaks与本次版本逐AST相同：每个枚举候选按原顺序完整处理，512只是batch size；剩余候选被时钟截断时保其描述且不接受。原1536约束/3072fine、任意真实角点、均匀角定义Ebar、原空间jets、分块参数AD均不变。旧parity/方向核有精确来源，本次新执行次数0；没有单开先验验证run。

物理仍R566两核心，联合R=1.012、Y=.3928、tau=.06072；Ebar>=.25、det>=.1、raw fine容差1e-8与working margin .001均不变。细峰只有超过当前实际违约/epigraph覆盖才urgent；其余pending按原规则批量采用。原SLSQP、函数行、trust规则及全fine接受都保留。

本次只是解决已经实见的峰库容量与外部中断可恢复性；没有因为原eta下降而删几何门，也没有把待采用3072观察网换作已优化实际约束。

## 成本身份

B030旧链科学累计2254.7471333500002 s完整精确记录；新科学时钟可加到该链。

B038此前精确链2668.197903319 s，加本次原最后OUTER明确444.54369729100006 s，得到已记录科学下界约3112.74160061 s。此后还发生约131.0866664 s的日志墙钟区间，含一轮完整定位、Jacobian、被拒callback及未刷出工作；最终科学时钟/总计数缺失。新输入保存这个区间及其工作内容，标recorded_chain_scientific_seconds_is_exact=false。

新FINAL字段明确为accumulated_recorded_scientific_seconds_lower_bound，并另保previous_unflushed_work_intervals_remain_charged_separately；不会把B038的已知下界重新命名为精确总耗时。

## 冻结文件与验证

- inverse_r566_theta_peak_checkpoint_20261126.py：52472 B，SHA256 a879573a4dbfd1a58ff7a25e07ac7d03a41916edac250116348dc008b7542a27。
- run_inverse_state_stdin_20261126.py：12009 B，SHA256 7fde98e3337eb537b18b18789b125fcac57e7382e8f22c755947e907c0ea7785。
- request-inverse-theta-peak-checkpoint-20261126.json：220229 B，SHA256 891df0ec391243fe309256f08f76f28ba27fae513ee73a0f179a8ac55eea8439。
- workflow visible-inverse-theta-peak-checkpoint-20261126.yml：3677 B，SHA256 7c40bbb6426adc6f3ce52525a748775d26f2a8a9ceeb43fe4dd4b953c7587d36。

两lane/max2，2400秒合作科学段、50分钟job，原Python3.12.14/numpy2.3.5/scipy1.17.0和两个固定Actions SHA，只stdout。全部13源绑定、sparse依赖、声明CLI、两源完整q/grid/peaks/trust及q二进制digest已作静态核验；本地未导入或执行科学模块。

这仍是会改变设计g的有限逆设计。全连续角/径向误差、全pair reach、冻结g非线性精化、有限可见等距族及README完成标准都未付，任何一个新容量或时间返回都不是收尾。
