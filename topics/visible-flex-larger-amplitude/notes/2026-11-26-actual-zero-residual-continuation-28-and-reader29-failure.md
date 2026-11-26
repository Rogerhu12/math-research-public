# 实际28同方程残差延拓与独立29纯读取失败

本条登记 [Actions 45820592817/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45820592817) 的[第7卷](2026-11-26-public-actions-45820592817-1-part-007.md)实际返回。root亲读完整紧凑块。28与29是不同角色：28确实运行了新完整根策略，但未得到原闭合初场；29只是其纯归因reader，另因真实程序异常没有产生readout。没有把第二件失败混入第一件科学结果。

## 1. 真实28来源与未成功的最终方程

完整六源/全部参数/条件推导见[残差延拓入口](2026-11-26-same-endpoint-residual-continuation.md)。实际launcher e57eb3d7f85a0abb44fb75ea56e918a9cd254025a718936bc163b82131f774d9、driver 9649ed99b614c468258646145948d7c06feb356c72806c73727728ea498ed88e、endpoint 3f37789f1624b97cb7f83b1795ac5fe96be3b3026d4078115078f12e8fd4e34a，source checkout **75a24f53a68572ff8e735420e52352363fce1c3f**。

同一reference/自由初点/原H和18字05dc保持。实际固定g为6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb，新model为73a9fb65ca3399c628bafa406c9a796ee5b2f16291bbf33544eb489d2290872f。原1333370自由量、45324288 metric行是完整模型的维数；初场读取失败不意味着已经完成这些行的数值计算。

五份完整地点输入含实际26的cfe87积分报告，实际已被消费；没有发生因该前序文件不存在而跳过历史的情况。Q未重算，旧球/场证书未继承。数值policy仍是原开球0.75、root tolerance 2e-12、每阶段Newton24/回溯18，以及明确的辅助初步长0.25、最小步长1/65536、最多64次阶段尝试、predictor=true。

| 实际返回 | 值 |
|---|---|
| 控制器状态 / exit | failed / 1 |
| 实际子进程秒数 | 41.35794009900201 |
| report complete | false |
| stop_reason | actual_initial_zero_closure_field_read_failed |
| 最后batch最小已完成lambda | 0.8342783749103546 |
| 最后batch最大已完成lambda | 0.8343435525894165 |
| 已记录拒绝阶段合计 | 149 |
| 最终原C是否独立读取验收 | false |

没有达到lambda=1。这里的中间值只属于辅助残差方程；没有任何一条被返回为原闭合初场、QP接受场或物理弯曲族成员。当前公开首摘要未包含具体失败角、当前Cz、最后残差和阶段失败原因；不能把旧15/19的角5或其奇异值复制过来，也不能把batch min/max猜成每角完整轨迹。

| runner真实输出 | 字节 | SHA256 |
|---|---:|---|
| zero-closure-frozen-moment-Q-continuation-first/report.json | 366286 | a2442ccad906f5fbc473376c5bd1644328235ae484ba8bebfcd8e4fa3019d335 |
| zero-closure-frozen-moment-Q-continuation-first-command.json | 14792 | 849c5880b536c27a80d2acbc256369adba60ba96dae2505e0c292691ec9a32b5 |

完整报告仍在runner，只保上述身份和紧凑结论。28 summary_errors和missing_outputs均为空，意味着已声明的报告/命令确实产生；它不把complete=false改为成功。没有新的initial/final字段文件、Phi或完整方向结果可宣称。

## 2. 真实29纯reader的独立失败

原a0c927aa9d7608a16ad7c051861903ebb533be3602325c2aada60ed6b1ccae61完整reader在source checkout **6c1b569ad6c6fadeba7edfd73f5db4efa9ef5ad1** 运行，实际6.034860249998019秒、failed/1，没有产生postprocess/zero-closure-frozen-moment-Q-continuation-first-readout.json。

因此29的metrics为空、outputs为空；summary_errors一项和missing_outputs一项均报告这同一个不存在的readout。只根据这个缺文件还不能断言具体Python异常，尤其不能据此改写28的科学原因。

源码静态审已经定位一个需要核实的接口不一致：9649的endpoint_readout是未添加延拓三字段的有限snapshot，而a0c的endpoint_roots使用value[key]读取continuation policy/counts/last summary。完整latest_operator_metadata实际另有这些字段。这个静态事实尚不等同于实际29的首个traceback；须读取其真实child log确认，并保持snapshot与完整metadata的来源/时点区分。修复不得凭别处字段回填一份未产出的snapshot或给缺项补零。

## 3. 已排完整纯诊断及继续方向

2026-11-26 17:26:56 UTC：采用未改的完整read_actual_followup_failure.py，SHA256 ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338。它只读取同runner的实际status中这一个已失败step和其真实child log，保有限末traceback/实际log SHA/exit；不运行root/F/J、不打开科学数组，完整log不上传。控制器另外按明确字段从既有a244报告读取失败原因、真实角字/lambda、计数及位置，报告缺字段仍原样保留。

完整参数 computations/resume-20261126-actual-zero-continuation-reader29-trace-ready.json，7305B，SHA256 41bb83b3860be771d0b50f6c530f4f2c448b2a004a9f0deefc9c368734045ad2；已加入03b活动队列。原两个655d同范数续算步骤逐值不改，运行中的child不被插队或中断；此pure何时实际运行以控制器返回为准。尚无新诊断输出，未预填traceback。

[真实26–27的655d积分父](2026-11-26-actual-integral-SO3-first-direction-26-27.md)已接下一完整方向，显式保a244整报告的地点责任；[独立gamma及完整KKT](2026-11-26-zero-endpoint-fold-and-added-shape-kkt.md)实现仍继续。同方程路径在该预算内失败不证明端点像不存在或严格fold，不给降低H的符号；原完整支撑必要条件通过的适用范围不变。README全部目标继续求解。
