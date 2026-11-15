# Request191 — actual98 独立39查询、非连续完整H凝聚与八批单摘要接口

日期：2026-11-15。此文对应全部冻结源与参数；没有预填 run、计算结果、接受率或末场。所有数学执行只在公共 Actions。本次制源仅做文字/JSON/字节身份工作，没有本地 import、AST、compile、fixture 或科学计算。

## 1. 明确的新实验与已观察依据

本请求从仍可恢复的 actual98 完整31查询原 pair 直接开始独立39查询轨迹。它保留 actual171 的全部38个选定 query，再加入真正 RIGHT-RMS459，fraction 原字面为 `0.8273268353539885`。每个模型仍完整重算 A、AT、weights、g、B、C、H及外变量响应；每批真实新 warm 完成原 FD 后，才作为下一批的父件。

R361 已记录 actual171 最后六个38阶段的最近拒绝均指向未选 RIGHT-RMS459；原38选定域与原 merit 可同时通过，却被该真实 RHS 域拒绝。这是新增一个具体约束的依据，不是更大步、收敛、QP最优、native接受或同一末场轨迹的保证。actual171 末pair已经删除，本次不用其SHA制造恢复，也不花3.7小时重演171再续接。原31→39第一步与171末场→39是不同实验。

实际依据为 R361 18655 B/`c2a0fc3f50a850628580b91497cba3174c96ff21ba57083bc512966e93142f52`，已发布 `d4ac5eccbcf339e9b3575ffe55fd053af5e5683a`。其 run43739787509/source`298c7dbebc28b5fa94bea030b4efe1426b21bf67` 只是依据身份，不是当前输入。

## 2. 冻结文件与完整来源数

下表文件除workflow外均放 `topics/visible-flex-larger-amplitude/computations/`；workflow放 `.github/workflows/`。本接口放 `notes/2026-11-15-request191-independent39-gap-condensation-and-one-chain-readback-interface.md`。

| 文件 | bytes | SHA256 |
|---|---:|---|
| `geometry_20261115_thirty_nine_query_domain_operator.py` | 38705 | `0dc60f8a43da0eed700e9e70235759b42890c038121c1f5a973fc6a417bf038d` |
| `geometry_20261115_thirty_nine_query_condensed_warm.py` | 50914 | `568d1f22ef9de4fe31d1a9e570ed66b3b91fb51525fc5dd5eb27f99c4901d3a9` |
| `geometry_20261115_thirty_nine_query_condensed_response.py` | 2622 | `fc92e7d900b0ccc24f6d6a162443112122f0e724c1e6b235914d23c593b4754c` |
| `geometry_20261115_thirty_nine_query_collocation_observer_warm.py` | 16732 | `59fa547d08f01f43b9000f8f58bb2c3eb03cc06a3a6f92dbeeedf728b08b19ea` |
| `root_20261115_noncontiguous_local_qp_condensation.py` | 13361 | `b7a5f7e6d699a2ed9c9d4068c3f831d633b76a1df457630ca536fd5207186ce4` |
| `root_20261115_thirty_nine_temporary_readout.py` | 52090 | `f10cb06439daef0be952a465bf75790703265bd6565f39274d7fea8ce94fc4b1` |
| `geometry_20261115_thirty_nine_temporary_batches.py` | 28049 | `9631f34cb0a0ccbcc08666e9ea8476174edaf3cfaf9bf544304cff4cdec8468b` |
| `public-thirty-nine-model-recipe.json` | 29930 | `bf443e95b3f49438b45b81212485bae2261056238f20e5d9cec85b596c46dd0e` |
| `public-thirty-nine-batch-request.json` | 11027 | `941dd0cda2dff96f6889a3b327c86aee2df3f0a3484d96f12344e55801962b11` |
| `visible-larger-public-thirty-nine-batches.yml` | 13045 | `90e51773a675b6d0576ae8d1ff5dd3df0ce4183e1a40ccd89ab964d917762c3e` |

R407 adapter 已单独发表在 `94c9eac2461e2b7285413b56639104a4765ea540`，本请求逐原字节引用，没有复制成旧8479同名文件，也不改其科学正文。

完整身份链是：

- actual171 recipe 的96份源逐键保留；
- 加其原 same-job worker `geometry_20261115_thirty_eight_same_job_batches.py`，SHA `2564be712a79aae29b5c2ce99518a8508e10f581e8a204a2162aec7b20859866`，共97份原来源；
- 新四份 query/model/FD/observer、已刊 R407 adapter 和新必要reader，形成 recipe 中103份完整映射；
- 新八批 worker 独立再pin，总显式104源。

旧96份recipe来源是 `public-thirty-eight-same-job-recipe.json`，24111 B/`947ace5169e6d3037ba61c561ed92a4be554f3e37b133966dd897c321e3fc890`，actual171 source `298c7dbebc28b5fa94bea030b4efe1426b21bf67`。没有用 pre-run cache替代实际发布身份。

原 `source-dependencies.json` SHA `7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941` 不变；其原public-source恢复协议仍由 `exact_20261114_public_resume.py` 承担。recipe、batch request、该原参数manifest是三份不同的参数文本，不把recipe的103源冒称worker自己的104源。

## 3. 当前唯一父场与四数学输入

初始父场必须来自官方完整已完成的 actual98 artifact：

| 字段 | 固定值 |
|---|---|
| run / artifact | 43677587785 / 14147700690 |
| artifact name | visible-followup-condensedqp-43677587785-1 |
| source | `918fdb11dbb7a424b6149b405e2c7fab3cc0c737` |
| 完整ZIP | 809042943 B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a` |
| 原 warm-001.json.gz | 4927052 B / `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67` |
| 原 driver-status.json | 3379453 B / `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff` |

原transport是 `exact_20261114_fetch_pinned_public_artifact.py`，SHA `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。同一次完整ZIP size/SHA验证后，只提原 warm/status 两成员并核CRC、size/SHA。完整中心目录检查与原路径安全规则保留；未解压成员没有冒称逐CRC/科学审计。ZIP随后删除，不上传raw。

原四数学输入从同固定历史source恢复：

| 文件 | SHA256 |
|---|---|
| accepted.json.gz | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared.json.gz | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail-anchor.json.gz | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail-config.json | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

完整历史相对路径逐字在reader.INPUTS。原 actual98 schema 为 `exact-constraint-thirty-one-query-condensed-complete-H-warm-v1`。它必须真实返回一个进展warm，`optimization_progress=true, accepted_warm_steps=1`，同时 `success=false,new_coupled_finite_acceptance=false`。该进展pair从来不是完整native或fullDN接受锚。

第一批使用原31父身份；后续只允许本job刚生成的39 own schema父身份。当前数学 producer 不能把原31/38来源改标签。每次传给原 `--expected-resume-sha`、`--expected-parent-status-sha` 的值均来自当前真实文件。

## 4. 全39 typed query、真正捕获和完整支撑

固定row order：

1. 22个 LEFT-RMS，fraction `0.17267316464601146`，区间 `462,463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487`；
2. 16个 collocation midpoint，fraction `0.5`，区间 `471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490`；
3. RIGHT-RMS459，fraction `0.8273268353539885`。

原38 row order逐项原样保留，新RIGHT append为第39组。原已付 N2048 selected-angle布局对应79872行；原实际非线性/FD命令 `--angles 4096` 另保持原语义，不将两者混成一个采样参数。

这不是只增标签。新增真实A捕获区间459及端点459/460的全J/P数据，完整26个唯一capture区间。左右RMS分别通过原general RMS类对同一完整capture作只读view，真实fraction参与原Hermite及其完整响应。新增RIGHT的角网格、label、row_slice、base、J/JT、frozen模型动作、condensed响应、导出与verify路径均同步。原16个MID的完整数学路径不改。

全部真实physical endpoint是
`[459,460,462,463,...,491]`，共32节点。**节点461不是保留的B列**，也不补零B列；它仍是完整H中的真实自由变量。

| 范围 | 维数 / 责任 |
|---|---|
| 完整原外变量坐标 | 236036 |
| B的真实physical节点 | 32×338 |
| 全3 scalar controls | 保留 |
| 真实local B维数 | 10819 |
| 原C选择 | 节点471..482与原全3 controls，共4059 |
| 自由core | 原109 |
| B在C外节点 | 459,460,462..470,483..491 |
| 真实gap | node461的338物理坐标在完整H内被消元 |

当前query的端点集合不再连续，因而不能直接调用8479原仅支持连续保留窗口的binder。这是本次必须实作的数学适配，而不是一般审计项目。

## 5. R407：gap461的完整仿射QR消元

原完整condensation源为
`root_20261114_complete_local_qp_condensation.py`，40393 B/`84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`。新adapter继承其完整块QR、平方根、H动作/求解、恢复、有限/零对角检查与资源协议，只把不连续真实保留集合接入R270允许的一般L。

实际过程：

- 先按原源构造连续cover459..491，共33节点的完整central front。包含全部原pure-global rows与affine RHS常数列；cover central维11266。
- 将真正待消的node461共338列置前，再依次放原109core、真实32节点、原3参数与affine末列。
- 用原 `_qr_prefix` 的同一次Q同时变换gap、core、其余变量和affine；消去的是正交旋转后可由gap最优满足的前338方程，不是直接删原行/列。
- 剩余central维10928，随后接原109core消元与local10819 QR。root、center、rhs、常数及全梯度沿同一个完整仿射平方根传递。
- 完整恢复仍解原H系统，rhs起点是原 `-g`，只有实际 `local_indices` 加入局部force。node461保持原 `-g` 及exterior-gradient责任，绝不把它设零。

原精确零对角/finite检查不变，没有新rank阈值。报告分别保 actual/cover/hole节点、两套front维度和内存责任；新adapter/source/schema进入最终model identity，不把基类 lexical `__file__` 的8479身份冒充新适配。

此为准确实数的条件平方根/恢复恒等，见已刊R407。它不证明binary64换序逐word相等，不保证600秒内完成，不预付QP最优性或原R267后验精度。若原资源路径触发完整C fallback，仍由原模型语义记录并按原真实试步判断。

## 6. 每批原模型与FD接口

模型入口是上表新observer，真实指向冻结warm/domain。完整命令由worker生成：

```text
python -u geometry_20261115_thirty_nine_query_collocation_observer_warm.py
  --accepted <actual original accepted bytes>
  --prepared <actual original prepared bytes>
  --tail-anchor <actual original complete anchor bytes>
  --tail-config <actual original config bytes>
  --resume <actual current warm>
  --expected-resume-sha <actual file SHA>
  --parent-status <actual paired original status>
  --expected-parent-status-sha <actual file SHA>
  --out <fresh batch/thirty-nine-condensed-warm>
  --iterations 1 --damping 270 --lsmr-iterations 200
  --projection-sweeps 200 --line-search-steps 17
  --budget-seconds 1200 --angles 4096 --jac-workers 2
  --condensed-budget-seconds 600
  --condensed-trial-reserve-seconds 90
  --condensed-recovery-reserve-seconds 30
  --condensed-max-working 512 --condensed-dual-sweeps 200
  --condensed-store-root
```

原 model成功产生真实进展pair后，执行新FD薄入口：

```text
python -u geometry_20261115_thirty_nine_query_condensed_response.py
  --accepted <same original accepted>
  --prepared <this batch original warm-001.json.gz>
  --tail-anchor <same original anchor>
  --tail-config <same original config>
  --out <fresh batch/physical-response> --angles 4096
```

FD所有原方向、步长、两级Richardson、原阈值与原实现检查均执行。继续下一批的条件保留原协议：原model return0且真实进展、精确paired文件身份、原FD return0、`implementation_check_passed=true`、FD的prepared SHA确等此新warm、`complete_current_warm_boundary_FD_actually_recomputed=true`。没有另加收敛阈值、数值匹配旧轨迹或新审计门。

原全域/RMS/selected39及merit共同判据、全部17档原线搜索、原material/physical字段、完整H和outside响应均保留。线性reserve合格不能代替非线性域，QP有限证据不能代替最优性或native接受。

## 7. 八批真实pair生命周期

主入口：

```text
python -u geometry_20261115_thirty_nine_temporary_batches.py
  --repo-root <fixed source checkout>
  --request <public-thirty-nine-batch-request.json>
```

本job最多8批。每个child新的Python进程，重新建立当前完整模型。父warm/status仅原字节移动，禁止重新序列化JSON/gzip、修改producer或强迫历史hash相等。

原3b8以 `start_new_session=True` 启动本worker；其源码没有统一的外部SIGTERM/finally子组回收。为避免science step终止后独立子session仍在写，本请求在恢复输入、原model及FD之前，由真实worker记录其 `pid=pgid=sid`、`/proc/<pid>/stat` 的 `start_ticks`、boot_id、当前run/attempt/source及request/worker/helper SHA。记录位于本job RUNNER_TEMP的本请求固定前缀文件，不读或保存argv、环境或token。原每个model/FD通过 `Popen(start_new_session=False)` 留在该真实session，启动即将实际pid/pgid/sid/start_ticks追加并fsync；原命令、科学参数与正常wait语义不变。注册失败不冒已启动科学，也不以目录名猜测进程所有权。

每批顺序固定：

1. 原model返回，读取原status/model/QP；只有真实新warm才作原FD。
2. 把所有实际trial必要标量、全部原返回失败query地址、FD门、原pair和大文件身份完整保存为临时必要记录，flush/fsync后核size/SHA。
3. 原FD允许继续时，移动两份真实文件到 `parent-after-XXX`，再次核原bytes/SHA。
4. 删除本批已选取必要字段的大raw及已消费旧父pair，只留下下一真实pair和必要小记录。
5. 最终把八批或实际partial合成**一份**必要整链摘要，完整输出后才删除剩余本namespace。

必要记录在pair移动前完成，避免此前155的move后输出异常导致漏原status/trials。后续移动/identity异常时，always-reader同时读必要记录、未完成batch原文件和仍存 `parent-after-*/driver-status.json`。不存在原model时不生成虚构trial，不根据进程颜色推断科学完成。

原字段subset hash只作读取身份，不是原array byte hash，也不作为后续有效新轨迹的数学门。没有跨模型不同weights的merit相减。

## 8. 一份≤90000 B必要整链与错误保全

正常最终schema：

`request191-one-necessary-whole-chain-readback-v1`

原帧：

```text
BEGIN_REQUEST191_WHOLE_CHAIN_NECESSARY_SUMMARY
<one ASCII JSON plus LF, at most90000 bytes>
END_REQUEST191_WHOLE_CHAIN_NECESSARY_SUMMARY
```

中断恢复只输出同样一份 `WHOLE_CHAIN_RECOVERY`，不是每批另开90KB。source/input/typed query定义只报告一次；每批保：

- 实际原model/FD exit、status门、原pair字节身份、是否允许下一批及原stop reason；
- 所有真实已返回trial的索引、alpha、原merit/域/线性slack等必要标量；
- 原完整RMS检查返回的失败地址与值、原MID failure indices/records、所有返回失败selected query；
- 原query实际访问index ranges，不把只报坏点误成只计算坏点；
- 完整返回trial计数与原17限制。缺失记录明确为 `not_recorded`，中断时不把它冒称已算或未访；
- 原QP/condensation必要标量、原模型与status重复字段对照、原输出文件size/SHA；
- FD原顶层误差/阈值/两组判定以及每个实际方向名和真实层数。全部数值层历史只留原response-check原文件身份，不搬全FD树。

必要trial可用透明共同列的小表；这些只是选定原标量及地址的键去重，不是原大数组/科学树的字典编码。相同必要domain记录仅在原JSON字段逐值完全相等时引用一次，明确这是原记录相等，不是重做科学等价判断。原大model/trial tree、数组、QP矩阵、root、完整FD数值历史均只Actions临时。

`not_represented_batch_indices` 与有证据的 `unstarted_batch_indices` 分开；只有已正常写出的真实final state才据原attempted_batches确定后缀。恢复时若无该终态，未启动字段为null并保原starting state/现存地址，不把丢记录变成未启动证明。

摘要超过90000 B：打印必要身份/真实超限bytes，`summary_complete=false`、退出70，不分包、不base64、不上调限额，也不改变原科学结果。保未读临时必要记录与当时仍存raw，直到成功always读回或runner销毁。此前已完整选取必要字段并退休的大raw不会假称仍在。

原stdout不作为大科学流转发。原stderr≤64000 B时逐字以ASCII JSON的surrogateescape文本保留；更大或完整错误摘要超过90000时明确传输未完成70，保原文件身份和未读字节。FD阶段的这种异常专门重新抛出，不误记为原FD数学拒绝，也不进入raw退休分支。原失败stdout只保明确标注的末4096字节必要错误片段及全文件身份；不称完整stdout。源原错误字段的短文本与前缀身份规则明确继承原纯reader。

## 9. ALWAYS读回与真实清理条件

always入口：

```text
python -u root_20261115_thirty_nine_temporary_readout.py
  --readback-only --temporary-root "$RUNNER_TEMP"
  --code-directory <fixed computations>
```

它不导入科学模型，不做norm/Fraction/matrix动作。首先只读取本请求实际进程身份文件，并核当前run/attempt/source、三个源/参数SHA、boot_id及独占session。随后扫描当前 /proc，区分活进程与不再写文件的Z/X状态。只有存在启动时间完全相同的原worker或已记录child活锚，且同组成员sid及启动次序全部相符时，才能对该own pgid发SIGTERM；等最多15秒仍存活时，再经fresh成员/启动锚核对发SIGKILL，等最多5秒。首次已锚定组内观察到的后代也保其实际pid/start_ticks作后续锚。每次signal前再次观察，发现PID复用、未知成员或不可读scope即停止，不signal当前读者组，也不按cmdline字符串猜归属。已退出组的ProcessLookupError通过最终实际扫描判断，不冒发送成功。

必须在最终扫描没有活own组成员且没有未知scope后，才读可变科学JSON/日志。缺owner记录、无法绑定、无活原锚却仍有组成员或停后仍活，一律明确transport partial70，保原科学结果独立，**不读取或删除仍可能变化的科学payload**。本合同不声称能发现未记录且另行脱离session的任意进程；本请求的实际model/FD启动均明确不创建新session。完整own身份、发出signal和末扫描是小过程元数据，不是数学验收条件。

静止成立后，它在单份摘要中保所有已保存batch、实际中断batch和未记录parent carrier。无namespace时仅记录“没有幸存payload”，不由此推断科学成功。

workflow随后只读原rules `runner-result.json`。最终cleanup同时要求：

- `steps.necessary_readback.outcome == success`；
- `steps.rules_readback.outcome == success`；
- cleanup调用同一已pin纯helper再作一次fresh `quiesce_owned(...,terminate=False)`，仍无活own组成员且无未知scope。

最后一项只观察，不再发signal；不以先前quiet文件自报true替代当前/proc。任一失败/超时或静止无法证明则明确skip cleanup，记录实际outcome，幸存原件/必要记录留给runner销毁。路径必须位于本job RUNNER_TEMP并匹配 `visible-thirty-nine-191-*`，拒绝symlink/逃逸路径；不删共享缓存或原repo。正常worker已在完整整链打印后删除自己的namespace时，always读者不重建/重复输出旧科学payload。

无upload-artifact、Release或Git原数据步骤。末pair删除后其hash不构成下一run可恢复状态；未来若无同job保留现场，须明示重新从actual98起步。

## 10. 资源与停止分责

资源是原155八批合同，不因39查询或gap461自动声称可在原时间内完成：

| 层 | 原值及范围 |
|---|---|
| 每model |1200秒；原内部check和原判据|
| condensation |600秒|
| trial/recovery reserve |90 /30秒|
| working rows /dual sweeps |512 /200|
| line-search limit |17档|
| damping /LSMR /projection |270 /200 /200|
| fresh FD |原完整方向/steps/Richardson，原流程|
| 批次数 |最多8|
| between-batches loop |10500秒，从初始恢复/public-source完成后计时，不中断已进入的原call|
| Actions science step |175分钟，包含该step内的恢复、模型及FD|
| always必要读回 |10分钟|
| job |195分钟，包含setup、science、读回、cleanup|

外层175分钟可能先于内部between-batches检查终止一个原call；这是可复现资源partial，不能称原模型拒绝或所有8批完成。LAPACK/QR原不可抢占调用仍可能越过内部deadline后才返回；没有新性能保证。已刊R407只支付其数学消元，不支付本次运行速度、内存或实际QP可用性。

原600/90/30资源退出、原C备选、真实line-search全拒、FD未完成、文件/protocol错误、操作层timeout与传输70分别保留原事件。最大批数终止也不等于原课题完成。

## 11. Workflow、权限与规则同步

独立trigger：
`topics/visible-flex-larger-amplitude/computations/public-thirty-nine-batch-request.json`。

独立concurrency：
`visible-larger-thirty-nine-real-pair-batches`，`cancel-in-progress:false`，不取消旧171或其他run。runtime沿ubuntu24.04/Python3.12.14/numpy2.3.5/scipy1.17.0；BLAS/OMP/MKL/numexpr线程1，原jac_workers2。

权限沿原 `contents:write,actions:read`。token只process env/原Git CLI；transport官方redirect不把认证带去外部地址，绝不存token文件或科学日志。科学child环境删除GH_TOKEN/GITHUB_TOKEN/MR_TOKEN。

原3b8 rules runner SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` 不改。上述own组登记与always静止检查在新helper/worker及workflow外围实现，补的是独立session生命周期，不把旧runner描述成已有SIGTERM/finally回收器。真实checkout双README须分别匹配根 `21bd547f56590b7f2dd279d0297efb289a9b2783`、题 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`，以这些实际原字节建立显式baseline，原2700秒pull/rebase/diff停止协议保留，固定科学checkout不变。Git merge.stat关闭以免清理后的旧raw diffstat触发无谓blob获取。HANDOFF原规则同步行仍由原runner检查；未绕过。

Actions的正常source阶段逐完整103+worker pin、原参数manifest、原171来源96+worker1与原模型flags/父artifact/queryprefix进行文本绑定，并对实际Python做正常语法解析；这不导入科学，也不作新增数学验收。此接口不声称已在本地完成AST或bash检查。

## 12. 完整差异与本次检查范围

科学四源相对实际171的完整原diff、R407适配与warm/observer依赖刷新diff已独立提供；旧源未改。生命周期修补前已读runtime完整diff相对actual155 `0aa9dca2d8029721cd1e820948699206a7da4388`：

- helper原26989 B/`f5d598cdde4c46d2904eea2ef0d20b6009e8eb284ee9a2f6f18d20cbdfc582b7`；
- worker原27012 B/`0e5ded8435cd31b7dbedb31dc15a36239ca946f80a346c0c5104cb703f86a89d`；
- 原workflow9038 B/`b0393ce72cc8b7d4204ec114bf4c053f802d7180d5971827ce8b2af8cea3b245`。

三件修补前完整diff84435 B/`5fd380706f984e462c496a3019ee06a24ede34081a32975a77b3ffcf6c939f42`，小文本blob `5383dd15d72984fc64084c5dbf7532d361e24fd6`。它是可从公开原源重得的临时审读材料，无需作为科学数据保存。

本次另提供相对root已读 helper06af28e4、worker7d390a8a、recipe6b7263d7、requestde176275、workflow3948d85b、interface117bfbff 的六件完整小diff，只有进程登记/继承/静止后读删及连锁身份和说明变化。五数学源、原97来源pin、原model/FD命令及全部数值资源/科学判据保持原字节或原字段。没有本地启动、杀进程fixture、import、AST或compile；真实/proc行为及退出结果由Actions实际执行记录。

完成的是全部新源的文字构造、已读原API/字段/完整capture与QR语义核对、JSON原字段/来源集合/唯一替换与SHA绑定；没有科学预试、没有local AST/compile、没有虚构fixture、没有计算下一方向。实际public Actions source、run、job、全部trial/FD、末pair与是否资源partial都只能由未来真实输出给出。后续结果预留R404，未预写。
