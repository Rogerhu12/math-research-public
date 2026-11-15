# Request155：完整37查询、actual98新轨迹与逐原trial读回接口

本请求保留 R333 实际141的全部35查询，新增 MID489 与 MID490 两个各2048角的完整查询网格，并同步扩充原端点 Jacobian 捕获、局部 B 支持、凝聚外部响应和全部实际非线性读回。起点明确是可恢复的 actual98 original31 原 warm/status 对。实际141的末场已删除，本请求不从其 SHA 制造父场，也不先重跑141八批。

本接口只冻结可执行源码、参数、来源及读回责任。尚无155运行号、实际候选、接受步或数值结论；本地未导入或执行科学模块。原有35源码均保持原字节。根规则8的小文本对象保存不移动 Git ref；正式发布与调度由主控完成。

## 1. 真实依据及其不同责任

[R333](../results/R333-actual141-eight-complete-thirty-five-pairs-and-exterior-domain-failures.md) 的原始身份是 run43712613111、source a7ce55798404fec8fb3638c0fbf083250c5363b2、compute job132807257922。该正式结果20339 bytes，SHA256 cb466cc33809fe434c7f11e43da505154a9f783e46a13d5866b6efe4dbcc9dce。

实际141完成八个完整模型及八次新 warm FD；27次原 trial 中8次接受、19次域拒绝。第6批最近拒绝 alpha=0.5，唯一未选 MID489 的 beta_squared_minimum=-0.013450511611294402；第7批最近拒绝 alpha=0.0625，唯一未选 MID489 的原值=-0.0002213943346252023。这两档全部35已选查询均无负角。第7批较大档还实际暴露 MID490：alpha=1 时 MID489/MID490 为 -0.028913520835021078/-0.04137293008933174，alpha=0.5 时为 -0.01020692375812482/-0.028694435800344698。

这些原值只支持把两个真实未选 midpoint 加入当前有限线性模型。它们不解决另外两项已观察责任：

- 实际141的某些较大试探中，已选 LEFT463、LEFT464、MID471、MID472 仍发生非线性域拒绝；全71680线性 reserve 非负不推出实际非线性可行。
- 末模型的 ordinary-float stationarity_L2=20152.641542749137，R267 quadratic residual term=2785.5209955455302；这不能冒作完整有限 QP 最优性已付。原后验读数继续记录，不增加接受门。

155不承诺更大接受步、收敛或更优方向。原141八对只用于选点；其 final warm SHA104ecd329eceebed5558750cab3ed9c9fecce9779f9ca1b782b7d6fe04a42168 与 status SHA6102a5193f331d09581651649c0bb3b7666a9ba091521ba0fdf5baa00e3503d9 均不是155输入。

## 2. 完整查询、捕获与支持

原21个 LEFT 查询按原顺序保留：

~~~
463,464,465,466,467,468,469,470,471,472,473,475,477,
479,480,481,482,484,485,486,487
~~~

当前16个 MID 查询按递增顺序为：

~~~
471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490
~~~

每条查询保持原2048点物理 phi 网格。总行顺序为21个 LEFT 块后16个 MID 块，各块完整保留角索引0..2047；总75776行。LEFT fraction 仍0.17267316464601146；MID fraction 仍0.5，不能共用一条伪 fraction 身份。

| 范围 | 原35 | 当前37 |
| --- | --- | --- |
| LEFT/MID查询数 | 21/14 | 21/16 |
| 完整角行 | 71680 | 75776 |
| 去重实际 capture cell 数 | 22 | 24 |
| 新实际 capture | — | 489、490 |
| 实际端点 | 463..488，共26 | 463..491，共29 |
| 新端点 | — | 489、490、491 |
| 完整 B 局部坐标 | 8791 | 9805 |
| 原 baseline C 坐标 | 4059 | 4059 |
| 原完整全局坐标 | 236036 | 236036 |

当前 capture cell 是以下24项，而不是所有463..490 cell均新增求导：

~~~
463,464,465,466,467,468,469,470,471,472,473,475,477,
479,480,481,482,483,484,485,486,487,489,490
~~~

端点并集恰为连续29节点463..491。每节点原338物理坐标与原3个全局 p 坐标构成9805维 B 局部布局；ZERO_LAYOUT_NODES 仍为空，声明布局必须等于真实块列并集，不填额外零列。原 C 仍只含471..482十二节点和3个 p，因此4059；新增489..491及其余 B-outside-C 坐标仍进入原完整响应。不能把 C4059误写成当前全部 B 或 full H 的维数。

“新增支持”均相对冻结 original35 查询定义。源码中继承的 static support-expansion 元数据由 query_extension_reference 明确此参照；后续 own37 父对保持相同37查询支持，不是每批再次扩充支持。

## 3. 数学路径与原接受门

新 domain 构造仍通过同一次完整原 A 的 EndpointJacobianCapture 获取所有需要的端点 J/P。LEFT 查询继续原 CubicHermiteSpline 路径。MID489/490 使用真实 state.middle 及 problem.mid，并沿原完整中点链微分：

$$
\delta y_{\rm mid}
=\frac{\delta y_L+\delta y_R}{2}
-\frac{h}{8}(\delta f_R-\delta f_L).
$$

原端点完整物理 J、全3参数 P、标量控制的直接响应、Gamma/Pi/角矩阵链均保留。新增查询不是在旧 B 后补标签；实际中点、端点、global/local scatter、rmatvec、所有角行和保存范围一起扩展。这里每批 fresh 完整 J 指原 prefix 全残差线性化；没有把旧零高尾 T112 图冒称新的当前高度 nonlinear native Jacobian。

每批重新在真实父场建立原 A、权重 W、b、g=A^T b、B、baseline C 与完整阻尼 H。原 R270 全链 square-root 消去及 outside conditional response 保持；新增局部根随9805维实际模型重新形成，不能使用旧35局部因子。全 outside 响应继续优化，不固定为 baseline C correction 外的零变化。原 c+B_out z0_out、完整向量 radial repair、同一模型 segment safeguard 与原选择逻辑均保留。

下列逐字源码段已做纯文本比较，而不是数值测试：

- domain query_value/selected_actual_angles：1943 bytes 原字节相同。
- domain 构造中全部 midpoint Jacobian、块拼接和实际列并集：11251 bytes；仅错误消息中的查询数标签作反向替换后全段相同。
- warm 的 scalar/evidence/compact_metadata：4043 bytes 原字节相同。
- 原返回值 ObservedResidual：1530 bytes 原字节相同。
- CapturedLinearization、project、choose、原 search handoff 与 finally 恢复完整末段：16060 bytes 原字节相同。
- FD/observer仅独立 import、schema元数据及实际 producer pin 更新，原科学正文通过完整精确字符串逆变换回原35源码。

原参数完整保留：

~~~
--iterations 1 --damping 270 --lsmr-iterations 200
--projection-sweeps 200 --line-search-steps 17 --budget-seconds 1200
--angles 4096 --jac-workers 2
--condensed-budget-seconds 600
--condensed-trial-reserve-seconds 90
--condensed-recovery-reserve-seconds 30
--condensed-max-working 512 --condensed-dual-sweeps 200
--condensed-store-root
~~~

原完整 node/midpoint/RMS 域、rho guard、BC/物理残差、固定当前模型权重下 merit、原 reserve 和实际 trial 接受条件一字不改。原17档保留；不增加 QP 后验、字节比较或审查门。只读 collocation/midpoint observer 仍只读每次原返回数组，不能再次调用 RHS/J 或改变原 finite/merit。

## 4. actual98 原父、四数学输入与真实续对

首次输入固定如下：

| 身份 | 原值 |
| --- | --- |
| run/source | 43677587785 / 918fdb11dbb7a424b6149b405e2c7fab3cc0c737 |
| artifact | 14147700690 / visible-followup-condensedqp-43677587785-1 |
| 完整ZIP字节/SHA256 | 809042943 / 9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a |
| warm-001.json.gz | 4927052 / b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 |
| driver-status.json | 3379453 / b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |

原512247运输检查官方 artifact/source、全ZIP size/SHA、安全目录与选定两个原件的 size/SHA/CRC；不宣称解压或审计其它成员。真实原 status 是 original31 schema，accepted_warm_steps=1、optimization_progress=true，但 success=false、new_coupled_finite_acceptance=false。

四数学输入仍由历史918fdb11原 blob读取，路径与字节 pin 完整写在 helper INPUTS：

- accepted：notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz，SHA b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff。
- prepared：notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz，SHA 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714。
- tail anchor：notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz，SHA e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51。
- T112 config：notes/public-actions-43588155190-1-prepare112/T112-config.json，SHA 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5。

这些输入只是原有限模型/FD责任，不是当前 fullDN 或 native 成功锚。原78公开 source 通过原 public_resume 恢复一次；scientific checkout 不被规则镜像的 pull/rebase 切换。

首次 producer 只接受完整锁定的 actual98 original31 两文件；之后只接受本 job 真正产生的 own37 对，仍检查实际 gzip/status SHA、parent schema、latest warm、当前 producer/source 闭包。父 JSON/gzip 不重序列化，不改旧 producer subtree，不借已删除141的文件名或 SHA。

每批独立原模型子进程结束后，以其实际新 warm 路径和 SHA运行原完整 actual-warm FD。只有原模型确有一次 warm 进展且原 FD 实际通过当前 warm 的 implementation_check，才把这两个真实原件移到下一父目录。此 handoff 是原31/35生命周期，未增加科学门。字段 hash 比较只记录，不能因跨run差异否决当前有效场。

## 5. FD、未完成责任与停止

FD继续原真正零H T112 Jacobian的明确 affine路径，重算原全部方向、步长及 Richardson 检查；不能把它写成当前非零H nonlinear native求解、重新获得的 nonlinear tail J、最终敏感度或原物理审计。当前原0..112/full prefix参数和数学字节仍照原入口。

八批是最多八个真实 model/FD 对。停止可能来自原模型失败、未产生有效新对、原 FD 返回/报告失败、原10500秒批间预算、八批数额、原规则变化或外层175分钟 operational timeout。已完成的真实原值保留，未访问批次不补造。wrapper 的 success/new_coupled_finite_acceptance 固定 false，仅说明没有执行原 fullDN/native最终责任；GitHub job绿色也不改变这一点。

不同批次 W 权重与基点都重新形成。每批仅保存自己的 before/after原 merit字面值；不会跨模型减两个固定权重 merit或把其差冒共同目标变化。任何局部根/因子只在该 batch存活，不声称旧 RAM-only full factor已外部导出。

## 6. 完整试探与异常日志传输

新 helper 同时保留：

1. 原 model.trials 每个完整已解析 JSON对象，原顺序不变；
2. 原 status.iterations 中每条真实 trials 列表，保原 iteration索引；不以两个副本的全文件哈希相同为要求；
3. 原 compact domain/selected-query/RMS/midpoint/argmax、QP后验、FD、standalone/scientific-field关系及实际 source/文件SHA；
4. 每个非零退出 child 的完整原 stdout/stderr 合并日志字节，不只末4096字节摘要。

批摘要不超过90000 bytes时用 BEGIN/END_THIRTY_SEVEN_BATCH_SCALAR_SUMMARY 输出完整单帧。超过该界时不删试探/failed-query字段，改为 request155_complete_JSON_member/container/scalar_bytes/stream_end 的完整语义流。每条事件≤88000 bytes：记录原 document 的 canonical bytes/SHA、JSON_path、对象/数组成员数、完整子值或完整 scalar token字节。canonical严格指 sorted ASCII compact parsed JSON加一个LF，不冒原文件 byte SHA。原文件原压缩/JSON SHA另外保留。

异常原字节以12000-byte片保留，先 UTF8 surrogateescape 解码、再内层 JSON ASCII字符串；外层再 JSON ASCII。byte_offset/chunk_index/原file及chunk SHA足以逐字重建，不用base64、尾截断或只hash代替正文。这里是原日志传输，非拆分大数据入Git/Release。非有限 JSON token 仍由原 read() 显式保存 token名称，不能当成普通数值。

完整 print_batch 返回后才执行 move_pair 及其原文件身份检查，之后才删除该 batch payload和已消费父对；打印异常时原 status/trials 仍在 batch 目录。异常时新 owned_namespace 不自动删尚未读回目录；workflow always 的 --readback-only 扫描本请求 RUNNER_TEMP 名字空间，读取真实尚存 model/status/QP/FD及日志，并读取每个 parent-after-*/driver-status.json 内原 iterations/trials。搬移或身份检查异常可能使原 status 已位于 parent-after 目录；该补读不推断 model/FD成功或父对交接完成，允许与先前已完整打印的记录重复。选择/解析异常时逐字输出实际报告文件，不能用空 trial列表冒完整数学失败。没有 surviving file只说明现场没有相应文件，不说明科学成功。随后 always cleanup只移除该请求目录，所有raw均仅临时。

每批完成后原 raw按根规则15删除；末场因此不能凭输出SHA跨job续接。未来若要从其末场继续，必须在同一job有真实原件，或明确重做原同序工作；本请求没有外部raw checkpoint、artifact、Release或Git数据发布。

## 7. 接线、资源与规则同步

独立 trigger：
topics/visible-flex-larger-amplitude/computations/public-thirty-seven-batch-request.json。

独立 workflow：
.github/workflows/visible-larger-public-thirty-seven-batches.yml。

独立 concurrency group：visible-larger-thirty-seven-real-pair-batches，cancel-in-progress=false。不会取消141或任何在跑native线。

入口：

~~~sh
python -u computations/geometry_20261115_thirty_seven_temporary_batches.py \
  --repo-root "$GITHUB_WORKSPACE" \
  --request computations/public-thirty-seven-batch-request.json
~~~

实际 workflow 使用绝对 computations路径，并把此命令交给冻结3b8 rules_runner。最大8批、批间10500秒、science step175分钟不变。job195分钟比原141的185分钟增加10分钟纯读回余量；always readback自身最多10分钟。准备/运输/包安装与读取真实消耗可能使 operational timeout先到，不保证八批全付，不改任何原子数学预算。

Runner环境 ubuntu-24.04、Python3.12.14、numpy2.3.5/scipy1.17.0、BLAS线程1，原 jac-workers2。完整局部根从8791扩成9805维，真实工作量与内存随实际完整支持增长；未做本地科学估计或承诺资源足够。所有真实失败、资源中断和未访问后缀都照原记录输出。

根 README pin21bd547f56590b7f2dd279d0297efb289a9b2783，课题 README pinbff8aea253a9e6a7a4fac28d810ac454c5499fec。启动与每2700秒由原 rules_runner在独立镜像真实 pull/rebase，读到规则差异则原流程停并保差异；不能伪称发生新的本地pull。merge.stat=false只避免旧已删大blob diffstat，无科学作用。所有token只供原运输/Git进程环境；科学子进程移除GITHUB_TOKEN/GH_TOKEN/MR_TOKEN，不写credential文件。

原141 recipe的85 source pin全部原值保留，新四数学源与新helper增加5个，recipe共90；独立worker另1，共91个显式代码pin。原 source-dependencies.json参数manifest另1，原recipe26893 bytes/c190e447b35e073db54ad5b06d10d6e85c94931280164093fd79b0a42b2f1f93也单独核原字节。新增recipe/request本身不是伪造的原141请求。

## 8. 冻结文件及完整差异

以下为九个运行文件。除workflow目标在.github/workflows，其他目标均在本课题computations。旧文件均不修改，所有来源的明确baseline commit是a7ce55798404fec8fb3638c0fbf083250c5363b2。

| 文件 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| geometry_20261115_thirty_seven_query_domain_operator.py | 35648 | 2e189fbf48ddeb5bb2ffba60047ee544bc39b22c6fe5073a91dad6bb2a1074e3 | 82033da4ed72668fcbed3b03b2302093131d3904 |
| geometry_20261115_thirty_seven_query_condensed_warm.py | 50236 | 293045c6e52ef7760f3e3f275aa6d7ec63f9d38ef070178932dcb9022e717ef4 | 8ccb5e727a742a1e0529fa5c34f64d6b947b3318 |
| geometry_20261115_thirty_seven_query_condensed_response.py | 2625 | b87385e38108cbb405bcdec00fb1bc55fd241428f5ca42464679aef18f6210da | d5d5c562860c1cb1529c432eb3554d3b84e3b925 |
| geometry_20261115_thirty_seven_query_collocation_observer_warm.py | 16736 | 2f70133e81f235af4439a1d2b173be835532ae5e8521e3be5216ed2750bd8778 | 801cecbd63fe9ccd4782a1291237abc99ebdaad5 |
| root_20261115_thirty_seven_temporary_readout.py | 26989 | f5d598cdde4c46d2904eea2ef0d20b6009e8eb284ee9a2f6f18d20cbdfc582b7 | 411d351eae14e52d17acc486f82d6cc63a95efa1 |
| geometry_20261115_thirty_seven_temporary_batches.py | 27012 | 0e5ded8435cd31b7dbedb31dc15a36239ca946f80a346c0c5104cb703f86a89d | cf10373b6b933cb026d159470dc09072ab9f1242 |
| public-thirty-seven-model-recipe.json | 27755 | f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea | 110f2cb1e6891efe19ddc2adeca3a0d52fdf7caa |
| public-thirty-seven-batch-request.json | 7901 | 4349e1b343bb655b18a233cb68a0f2a8a59bcfd929b06b3ac49e073ccaa2e295 | 675c2a88cbdbf3c40cfc8fe9da17c3757112bd93 |
| visible-larger-public-thirty-seven-batches.yml | 9038 | b0393ce72cc8b7d4204ec114bf4c053f802d7180d5971827ce8b2af8cea3b245 | ba6a139fccdea9588c6988dbd26d5feea610121e |

四科学源分别对该commit的同名thirty_five版本；helper/worker亦对应旧thirty_five basename。完整精确字符串替换清单及各文件unified diff可重建，六源码已逆变换逐字恢复公开baseline SHA。原85pin集合与原数学flags/parent tuple逐字段等同；最终workflow原shell/inline接线只加独立名字、当前pins和完整always-readback。

本地环境在最后纯传输修正前断开。最终这些身份完成了纯字符串全逆变换、source/pin/参数一致性检查；没有声称最终版本在本地已经 ast.parse、bash -n或科学运行。断线前原型AST不能替代最后新身份的语法结论。公开workflow仍按原方式逐源SHA与Python AST解析后实际执行；不新增科学fixture或等待审查门。

本接口、脚本和参数按根规则公开；diff/纯静态回执只是临时可重现审读材料。没有155未来run、输出SHA、候选或接受结果被预填。
