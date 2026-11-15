# Request166：原37查询显式控制身份配对后的完整R334诊断

日期：2026-11-15。状态：独立源码与完整公开Actions接线已冻结，尚无本请求实际运行或数值结果。本请求修复actual158已定位的观察器绑定错误；原37模型、原FD及原接受责任没有改变。

## 1. 实际错误与本次修复范围

[R346](../results/R346-actual158-original37-accepted-step-and-post-model-binding-failure.md)记录actual158：run `43731669039`、source `de638f2ab272db4dbe0a695394c126b72a56fa42`、job `132865254053`。原模型exit0、实际新warm的原FD exit0；独立后置诊断exit2，原异常是 `ValueError('All base37 returns')`。原模型实际接受α=1/8，不能因诊断错误改称原模型失败。原日志没有导出原控制调用总数，本接口不把推测调用数写成实测值。

原capture包装原profile.control_jets的每次真实返回，包括原scalar_jets缓存填充调用和原B构造中的显式调用。原37个query不意味着总控制返回恰为37。原消费者却把二者计数强制相等并按数组位置直接配对，这是本次修复的具体来源。

新capture不另调用profile、RHS或J。它仍保留每次真实返回，增加连续的observed_call_index。每个原query完成后，从其真实原query_reports复制原B显式使用的控制数组身份：left-RMS使用scalar_control_jets；collocation-midpoint使用original_scalar_control_jets。新消费者以站点binary64原word和该完整数组身份配对，而不是假定第q个观察调用就是第q个query的控制。

若同站点有多个逐word相同的真实返回，新消费者保存全部匹配下标并选第一个作为值代表；明确不声称这个代表就是原显式调用的调用栈身份。若不存在相同完整数组，报告诊断绑定失败，保留完整观察清单；不从Bz反造值，不重算控制，不删除额外观察调用，不把失败转成原模型拒绝。

## 2. 冻结文件与基线

所有五件均小于100KB。前三件及request目标目录是topics/visible-flex-larger-amplitude/computations；workflow目标目录是.github/workflows。

|文件|字节|SHA-256|
|---|---:|---|
|`geometry_20261115_R334_thirty_seven_bound_return_capture.py`|20842|`e32e941648cc35aef45f4f19ef050f90798e2ca0759b887afc2fff5b782a962b`|
|`exact_20261115_R334_thirty_seven_bound_candidate_diagnostic.py`|54892|`6171fbbbbb79457751b7ba8a26c47c111ba5b1f4f91db8170689441df865eb00`|
|`geometry_20261115_R334_thirty_seven_bound_same_job.py`|23365|`0979811b4d2a3bf60cd2e4ac6fbc24ee89327c7eb3cc65934567eea28e566778`|
|`public-thirty-seven-R334-bound-diagnostic-request.json`|26229|`34d8773014637fb30f0dc3dfaf6ef5ef8ff66927901a134c638e42f88a04928c`|
|`visible-larger-public-thirty-seven-R334-bound-diagnostic.yml`|9738|`c3a4b0d86cc6a58f365e5c71daab259e03434a7c0bce2dcca2eb94a3d0330512`|

精确基线是actual158 source commit `de638f2ab272db4dbe0a695394c126b72a56fa42` 中下列原件：

|新件|原件及原SHA-256|
|---|---|
|bound_return_capture|geometry_20261115_R334_thirty_seven_return_capture.py；01a2638409893b60711c3af0ab4d14c6f9bc4272058f2e7577dd41b2db33c59d|
|bound_candidate_diagnostic|exact_20261115_R334_thirty_seven_candidate_diagnostic.py；3ed6fbc5bed4023197afd8441287fe6ae5655c769e3cb8f2b417fbf1a02d8047|
|bound_same_job|geometry_20261115_R334_thirty_seven_same_job.py；92d1adb0e5a43f132356d0dba2310545bd01cd85235011a759f01362c7edf392|
|bound request|public-thirty-seven-R334-diagnostic-request.json；2d678acda0e17dcd716c5d42574496e586046a7add0802729aaf95ed4d677428|
|bound workflow|visible-larger-public-thirty-seven-R334-diagnostic.yml；110ba1af40a834e1c0d6236ceeec3fb4df30edd41c199c996e28f18f92a13b4d|

原158三个诊断源码仍在来源闭包中，只作为来源，不执行。原94 pins逐项保留，新增上述三个独立源码，总97 pins。原155 recipe的90源码、原batch worker一件以及原三参数文件不变；三个新源码各用新basename和v2 schema，不覆盖旧158。完整request列出全部97项，不依赖此表省略的短名。

新schema依次为R334-original37-actual-return-capture-v2、R334-original37-complete-candidate-exact-readout-v2、actual98-original37-one-model-FD-then-R334-diagnostic-v2；request为actual98-original37-R334-post-model-request-v2。

## 3. 原科学与新绑定的边界

原37四科学源保持以下原SHA：domain 2e189fbf48ddeb5bb2ffba60047ee544bc39b22c6fe5073a91dad6bb2a1074e3；warm 293045c6e52ef7760f3e3f275aa6d7ec63f9d38ef070178932dcb9022e717ef4；response b87385e38108cbb405bcdec00fb1bc55fd241428f5ca42464679aef18f6210da；observer 2f70133e81f235af4439a1d2b173be835532ae5e8521e3be5216ed2750bd8778。

消费者中原精确dyadic运算、polynomial、point_P、exact_action、hermite、affine_row、commit_affine_row、point_rows、hermite_defect及原Budget/Ledger/Packets等44个顶层函数或类片段全部逐文本不变。只新增match_original_query_controls；原bind去除错误的总调用数等式并调用配对；main只新增原观察清单读回，并将所用控制记录改成已配对的matched_query_controls。main内新的矩阵动作、FFT、九系数、Bernstein和完整453分量恒等式仍是原158明确申报的Actions后置科学算术，不是字节检查。

配对的原数组身份按原array_identity形成：shape文本、NUL、dtype文本、NUL、完整C-order原数组字节的SHA-256，同时核shape、dtype、bytes。真实station用原float64le word。所有同站点候选都经原Packets字节绑定；维数必须为完整3×3，原值必须有限。无匹配或观察错误只限制后置诊断，不回写原模型、原FD或接受标志。

完整原query报告和配对结果保存在result.complete_original_domain_binding；其中query_control_matching_readback保留每query显式身份、所有同站点观察候选身份、全部匹配下标、选取的值代表及不主张调用栈身份的声明。原完整controls列表不被matched列表覆盖。

## 4. 实际输入与一次真实重建

本次仍从真实actual98恢复原父对，另起一次完整原37模型及实际新warm的原FD。actual158/155/141的已删除warm不作为输入，不能从hash制造恢复。

父run为43677587785，source为918fdb11dbb7a424b6149b405e2c7fab3cc0c737；artifact 14147700690，name visible-followup-condensedqp-43677587785-1，ZIP809042943B，SHA9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a。原warm 4927052B/b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67；原driver-status 3379453B/b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。原status逐字使用，不重序列化成伪父件。

原公开完整archive的运输、size/SHA验证和所需原件提取仍用已冻结512247内核和原155支持层，临时写RUNNER_TEMP。原留存历史输入由原918fdb提交恢复；科学checkout固定本次真实触发source，不换成历史代码。

原155 recipe public-thirty-seven-model-recipe.json，27755B/f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea，完整保留原request155/schema，未改标签。actual158只是修复依据，不是本次warm父对象。

## 5. 完整范围与不可混同的结论

原查询为21个left-RMS和16个collocation-midpoint，固定typed顺序、每query全部2048角，共75776行。原capture按原interval保存两端原J/P和真实调用身份，不合并不同chunk的同节点words。

诊断仍消费原最终实际选择方向z、完整系数方向和原原点，形成明确的后置有限参考，再逐行支付9个精确多项式系数、全部9个Bernstein系数以及17档α=2^(-j)、j=0..16。正公共Bernstein分母280、完整degree8不变；严格affine正性不冒实际非线性可行。

对每个实际已访问trial，仍分别保原返回点态域值、原正常公式与cross公式差、完整453分量的Hermite缺陷分解：实际端点形成、原literal J/P的精确RHS余项、query有限形成差、formed query方向的舍入项。未访问17档、未完成query/角/分量、预算停止及失域均保明确范围，不补造返回值。点态缺陷不冒整个α区间的RHS二阶界。

原完整A/W/b/g/λ270、B/C、图/metric/source、全部非线性门、两套RMS、boundary、merit、线性reserve、17档回溯以及原FD保持。新的匹配检查和新R334诊断都在原模型/FD之后，不作为原接受门，也不主张QP最优、native/fullDN成功或更大步必可接受。

## 6. 执行顺序、预算与完整错误传输

顺序是原actual98恢复→一次原37模型→按原handoff允许的实际新warm FD→先完整输出原科学摘要→独立R334诊断→always完整读回→仅本请求临时清理。原模型/FD各自exit、原异常和实际访问trials先保；诊断缺输入或失败不回写它们。

总science绝对6000秒，前置source恢复、ZIP运输、完整J/QR、原FD都计入，清理读回预留180秒。诊断最多1800秒且受总剩余期限裁剪。原模型参数仍iterations1、damping270、lsmr200、projection200、17trial、model1200s、angles4096、jacworkers2、condensed600s、trialreserve90s、recoveryreserve30s、working512、dual200、store-root。全部临时未压缩ledger共享8GiB上限。独立science step110分钟、job135分钟、always读回15分钟，不声称预算内必完成全部新算术。

RUNNER_TEMP/visible-R334-166与visible-R334-166-rules为本请求独立命名空间；owned身份包含run、attempt、source。新concurrency group和trigger均独立，cancel-in-progress=false，不取消155或其他任务。

原complete_semantic_JSON stream逐字段保全所有原trials、诊断完整result/summary、全部未决范围和错误。原helper沿用request155事件词，但标签内容为request166；这只是冻结运输协议复用。所有原child错误日志按12000字节、surrogateescape加ASCII JSON无损分段，没有70KB截尾。

新增capture-status在always读回中完整输出各domain的真实query/control/angular计数、每个control调用原packet descriptor和每个query原显式身份。即使后置bind先失败，也不会再次只剩无法解释的总capture hash。成功后result完整域对象另外输出全部匹配证据。原pair不在完整主读回前搬走；清理要求已有readback-complete标记。大NPZ、全部逐行ledger、原warm与status仅暂存本job，不上传artifact、Release或Git。

## 7. CLI与规则同步

唯一新入口：

```text
python -u geometry_20261115_R334_thirty_seven_bound_same_job.py
  --repo-root <fixed scientific checkout>
  --request <computations>/public-thirty-seven-R334-bound-diagnostic-request.json
  --work <RUNNER_TEMP>/visible-R334-166
  --mode run
```

同一CLI的--mode readback和--mode cleanup由always步骤调用。不得单独将cleanup当科学结论。capture和consumer参数由新same_job保原精确顺序传递；consumer所用实际result/方向/packet身份只在运行时取得，不预造未来run。

原3b8规则runner不修改，工作流先核已读README blob并用这两个真实文本覆盖原BASELINES；原每2700秒真正pull/rebase和差异停止保留。根README为21bd547f56590b7f2dd279d0297efb289a9b2783，topic为bff8aea253a9e6a7a4fac28d810ac454c5499fec。Git设置merge.stat=false；凭据只环境，不写文件，不force。规则镜像写入的H不是科学checkout。主控仍是唯一源码发布者。

## 8. 静态范围与实际待付责任

本次已做完整源字符串、SHA、所有94旧pin保留和新增3pin、精确基线差异、实际原query_reports字段的源码核对；44个消费者顶层数学/支撑片段逐文本相同。未在本地导入科学模块、运行AST/CPP编译、执行fixture或任何数值。新工作流会在公开Actions核97源码SHA并作原普通Python语法解析，然后直接执行授权实验；没有额外数学验收门。

全部新的运行结论须来自真实166输出。此次修复既不承诺原模型再次选择相同α，也不承诺新诊断在1800秒内覆盖全部75776行；每个已付/未付范围将按实际结果保留。完整精确差异可由上述已公开158基线和五件新源码重得，不要求额外持久保存可重算差异或审计raw。
