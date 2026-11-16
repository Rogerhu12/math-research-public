# R449：actual202 十词到新准确连续十族的可执行来源接口

作者：OpenAI ChatGPT（AI assistant，amplitude 源码责任；root 唯一 Git 发布）。本接口与 [R449 条件结论](../results/R449-actual202-to-accurate-continuous-ten-fresh-candidate.md) 配套。本件只给独立源、准确来源和后继调用合同，没有新 request、实际 run 或新场接受。所有候选投影、有理运算、C/factory/native/BVP 与科学输出只允许公开 Actions。

## 1. 本次冻结件

公开路径均相对 `topics/visible-flex-larger-amplitude/`；接口自身以本次公开 Git 文件为准。暂存 `publication-files.json` 仅是代理交给 root 的文件身份清单，不另入库，不是运行回执；本表所列源、参数和证明身份可直接从对应公开文件核取。以下 SHA256 针对文件完整 UTF-8 字节（保留末 LF）。

|公开路径|字节|SHA256|Git blob|
|---|---:|---|---|
|`computations/geometry_20261116_actual202_accurate_ten_candidate.py`|31495|`7b601a092b61d9c71d83836d7ae8aef5c0af9f25f187a856a21adec20ba0df49`|`e42d41921bff1d5fa15d90b15f76062c45b8d5d7`|
|`computations/geometry_20261116_actual202_accurate_ten_full453_frozen450.py`|34835|`6bb4910bd26849c141c94094cc0a7d05939655fbb8eefbd95129e8cb03ef1965`|`342255862ada50889d44d4aabe02cfed3ed7e345`|
|`notes/actual202-accurate-ten-candidate-input.json`|2165|`c980e9d4c6e15455459dc91a890b4fd9d8b02bced26eecd5d632ff9d250dbd4d`|`50a6d95fcd9ac61dfd722e912fa71c1b868b921d`|
|`results/R449-actual202-to-accurate-continuous-ten-fresh-candidate.md`|20011|`8756fa0051bd166b5aae9cca3f323e407d77de56c8ea943e6a2c9541b9e35a15`|`059c6c434d3ee225ffb1532002c1d89608a4e338`|

本地文本交付目录为 `/workspace/visible-larger-working/actual202-accurate-ten-R449/`。`candidate-driver.complete.diff` 是已发表 `5400aa4a…` driver 到当前独立 driver 的全部文本差异；8111 字节，SHA256 `3958ebdb2bb5f14e60edb65ce50552bf66273b67a4c34fa62e28a828835af976`，blob `0e788c88ae791dd21efe48027c45c18752f1a6ff`。`explicit-resource-reserve-only.diff` 是 root 已读初稿到本次显式预留修订的完整小差异；5747 字节，SHA256 `043979b6a09ed135957bdb692f8128587b168691f76d6b96257b9e9d665a0564`，blob `9053ee004ba8e1ff3b3114257d9b8c8668a73345`。这些差异和清单是源码复核材料，不是科学求值回执。

## 2. 输入只继承真实数词

唯一旧数值初猜来自 actual202：run `43784544723`，source `1a757004b7ebff1f43563bd57b5d13961648d681`，compute `133029129971`，report `133029647087`。已发表 [R439](../results/R439-actual202-ten-unit-tolerance-complete-final-diagnostics-and-projection-scope.md) 为15353字节、SHA256 `98946f81702019fb7902893deffe8a34fb021207c7ad55f7f8649a18821b346b`。原必要摘要65926字节（无分隔末 LF），SHA256 `ae541e15e47d5fac46dbda02e57d2487d9168ec1811d93d171d1d0989923df2f`；原 status1061043字节、SHA256 `db9a64398b10991fcccdd3b198d102604df89c7e7c3703a56142eba8b2195a23`。

十词顺序严格为 `[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3,xi]`。原紧凑 ASCII JSON 数组为553字节、SHA256 `ba7d7fe3c7fd2599bb7f06863c117b11c6c9f4feb255a160de13023e22129369`；新参数输入文件保全部原字符串及这个身份，既不重新计算原末值，也不复制原大状态/J/FD 输出。原202 raw 已清理，后继不得通过其 SHA 宣称恢复一个场。

本源明确采用新策略：在 Actions 内把每个原 Decimal50 字符串视为准确有理数 $q_i$，执行 binary64 投影 $v_i$，再把 $Q(v_i)$ 声明为新准确模型的初始系数。每一项同时保存原词、原有理词、binary64 数值/十六进制/小端八字节词、新准确 dyadic、准确差值 $Q(v_i)-q_i$ 及能否逐字准确表示。没有本地求这些新数值，没有假定十项都可逐字表示；新初点的准确系数与初始 finite BVP 数词一致，不等于证明 finite evaluator 与准确连续 C/DAG 相等。

原202的三个支撑都在旧 prefix 的三个默认窗口；新连续族仅第一个支撑沿原第一窗口，第二支撑是准确 first-velocity-transition，第三是准确 coast。旧第十项在中间 prefix 窗口；新第十项在准确第一速度过渡。相同坐标名和相同形状公式不表示相同函数。R449 正文逐源说明了自然长度、cut root 和材料坐标的差别。原有限 Gauss 的三残差、J、域、unit 接受和完整112线性读数均不转移为新族的任何接受。

## 3. `prepare`：先声明新准确系数与新模型配方

精确调用如下；路径和值由后继实际同 job 传入，尖括号是接口占位，不是假造的现场。

```bash
python computations/geometry_20261116_actual202_accurate_ten_candidate.py prepare \
  --parameter-input notes/actual202-accurate-ten-candidate-input.json \
  --model-recipe-template <真实恢复的actual180-selected-recipe.json> \
  --out <RUNNER_TEMP内新的candidate-prepare目录>
```

结构模板必须是实际180原九族 recipe：2136字节、SHA256 `cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb`，schema `R300-new-continuous-nine-scalar-model-recipe-v1`。它是同一准确构造的几何政策模板，不保旧180参数/选择/域证书。只复制 `core_end,kappa,collar_width,first_transition_width,last_transition_width,first_support,root_choice,collar_mode` 八个结构字段；原九系数全部替换，并显式加入第十项。

实际生成三件仅驻留本 job 临时目录：

|文件|用途|
|---|---|
|`candidate-ten-parameters.json`|十个原词、投影和新准确 dyadic 的完整逐项声明|
|`actual202-projected-accurate-ten-model-recipe.json`|原72c factory真正消费的新连续十族配方|
|`adapter-result.json`|当前 source/run/commit、两个输出 receipt、原输入/模板身份及 `phase="candidate-prepared"`|

`prepare` 不调用 C、factory、native 或 BVP；`actual_design453_accepted` 与 `actual_frozen450_accepted` 为 false。其新模型 schema 是 `R300-new-continuous-ten-fixed-support1-power4-model-recipe-v1`，十项逐项给出 `(parameter_index,support_index,power)`。shape 是原准确 $w^2,64x^3(1-x)^3(2x-1)^k$，第十项 `support_index=1,power=4`；无重选候选或暗置 `xi=0`。

## 4. 两次 adapter 之间必须真实支付的现场

外部 pipeline 须在同一个真实 job 中重建原准确 C、cut 读回、72c 连续十 factory、112 joint native geometry/config，才可进入 `bind`。此接口不允许给 JSON 贴旧 result schema 代替 producer。

|责任|实际原 source SHA256 / 合同|
|---|---|
|完整准确 C|`f12f747041783b…f424df7df`；完整值在 helper `C_SHA`，result schema `R286-original-stored-convention-C-continuous-E-cover-v3`，模型 schema `R286-original-stored-continuous-model-convention-C-v1`|
|完整 cut twojet 读回|`1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed`|
|准确十族 factory|`72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682`，真实 `result.json` 与 `model_definition`|
|明确 finite numeric 编译|`7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd`|
|当前 joint sampler|`32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4`|
|当前 joint worker|`d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a`|
|当前 joint client|`02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1`|
|当前 joint representative|`24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97`|

factory 的 `exact_model_definition_created`、原结构严格条件、十准确参数及同 job 完整 C/cut 输入必须真实吻合。原 `base_domain` 与 `requested_parameter_domain` 的 complete/未解/未访、最小半径、最大速度和原 ledger 身份如实回读；这些区间 sufficient 证书没有变成 BVP 新门。原 current-C 入口自己的完整30 native pin、所有原政策值、geometry readiness 和 C 语义对应仍由未改的 c71d driver 执行。

基底继续使用原真实 accepted96（SHA256 `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`）中 `/fixed_scalar_profile/geometry`，以及原独立699×453 seed（SHA256 `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`）。accepted96 是原几何/目标数据，seed 只是当前新 BVP 的初猜。没有把202的旧699 Gauss状态移入新场。

## 5. `bind`：在最终 recipe 身份形成前明确资源

```bash
python computations/geometry_20261116_actual202_accurate_ten_candidate.py bind \
  --preparation-result <candidate-prepare/adapter-result.json> \
  --preparation-result-sha256 <该文件实际SHA> \
  --factory-directory <当前真实72c输出目录> \
  --factory-result-sha256 <当前factory-result实际SHA> \
  --current-C-directory <当前完整C目录> \
  --current-C-result-sha256 <当前C-result实际SHA> \
  --cut-twojet-readout <当前完整cut读回JSON> \
  --cut-twojet-readout-sha256 <当前cut实际SHA> \
  --BVP-recipe-template <原179十千字节recipe> \
  --tail-config <当前joint-complete112-config.json> \
  --tail-config-sha256 <当前config实际SHA> \
  --code-directory <当前computations目录> \
  --candidate-driver-sha256 6bb4910bd26849c141c94094cc0a7d05939655fbb8eefbd95129e8cb03ef1965 \
  --request-number <后继真实request号> \
  --sampling-startup-reserve-seconds <该request明确采样启动预留> \
  --out <RUNNER_TEMP内新的candidate-bind目录>
```

原 BVP 模板固定 `current-C-riccati-full453-physical-DN179-recipe.json`，10294字节、SHA256 `d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811`。源只做明确的身份/来源转换：旧 initial nine 改完整 ten，原三 active `[0,1,2]`、七 frozen `[3,4,5,6,7,8,9]`；第二完整问题450/K0/k0；native 实际 source/config 改当前 joint 现场。原 M112/N2048/453与338维度、4096角、1200节点、8外迭代/17内回溯、RMS/BC/FD、正 lambda `.001` 与 height sign `-1` 原样保留。

**采样预留和完整 BVP 上限是两个字段。** 原179采样启动预留7200秒；完整双 BVP process 上限也为7200秒，不能据数值相同混为一项。`bind` 必填 `--sampling-startup-reserve-seconds` 且无默认值，在写最终配方/SHA之前设 `execution.pruefer_sampling_startup_reserves_original_BVP_seconds`，同时存 `explicit_resource_binding`：原模板 receipt、原7200、实际传入值、CLI字段名、未改的完整BVP7200、绝对钟未启动/重启。

205若沿203已声明的3600秒采样预留，外部 pipeline 必须从同一个显式资源计划：先以3600决定真实采样预算，再以3600调用 `bind`。不能在采样后声称此前用的就是3600，不能在已写 recipe 上覆值而继续用旧绑定 SHA。剩余绝对时间仍真实裁剪采样/BVP/下游；3600不是保证所有112 mode 或后继阶段完成，也不是新的科学接受条件。

`bind` 输出 `actual202-accurate-ten-full453-frozen450-recipe.json` 和新的 `adapter-result.json`，后者 `phase="BVP-input-bound"`。其中 `generated_BVP_recipe`、`actual_candidate_driver`、完整 factory/definition/C/cut/config/preparation receipts 是下一 driver 真正消费的绑定。此时 `actual_native_calls=0`、`actual_BVP_calls=0` 指本 adapter 本身；不能用它们抹去此前外部 sampler 已实际执行的科学工作。

coast center 诊断只在 Actions 用当前 factory 原完整 `coast_length` hull 形成 $-\kappa+2L_C\theta_3$ 区间。它记录 center 的严格速度包围或全 root 选择的 center 反证；宽盒不能叫数学失败，center 通过不能付完整 coast 域。它既不换参数，也不改变 solver/factory 标志；原完整域与原 BVP 各负本责。

## 6. 独立 driver 的完整参数与来源

```bash
python computations/geometry_20261116_actual202_accurate_ten_full453_frozen450.py \
  --recipe <candidate-bind/actual202-accurate-ten-full453-frozen450-recipe.json> \
  --recipe-sha256 <实际最终recipe SHA> \
  --candidate-binding <candidate-bind/adapter-result.json> \
  --candidate-binding-sha256 <实际adapter-result SHA> \
  --accepted <真实原accepted96> --accepted-sha256 <原b4d2完整SHA> \
  --complete-seed <真实原699乘453初猜文件> \
  --factory-directory <当前72c输出> --factory-result-sha256 <实际SHA> \
  --tail-config <当前joint config> --tail-config-sha256 <实际SHA> \
  --tail-source-root <当前临时恢复的原source-root> \
  --tail-client <computations/geometry_20261115_current_C_pruefer_joint_tail_client.py> \
  --jac-workers 2 --node-heap 6144 \
  --out <当前owned完整科学输出目录> --work <当前owned临时work目录>
```

driver schema `R449-actual202-projected-accurate-ten-joint-full453-to-frozen450-physical-DN-v1`；recipe schema `R449-explicit-actual202-projected-accurate-ten-joint-full453-to-frozen450-recipe-v1`；helper schema `R449-actual202-new-accurate-ten-candidate-adapter-v1`；参数文件 schema `R449-actual202-original-ten-word-candidate-input-v1`。

driver 相对已刊5400只改独立身份、helper/原5400基线 pin、非零xi的新候选校验及输入/事件元数据。`PhaseLease`、`prepare_design`、`prepare_frozen`、`run_phase` 完整文本不变。新 `recipe_input` 调用 `read_bound_candidate`，按当前 helper/driver实际文件身份、当前生成recipe/factory/config receipts及全部十个 binary64 words 绑定，不接受给旧180点换一个 origin 名字。

直接 source 闭包保原 c71d joint driver、3bc profile、43f checkpoint、62010 live hooks、72c factory、7ded numeric、a248 augmented，并明确新增 helper 和原5400 baseline。运行时继续合并原 c71d 的真实递归 closure；这里不把九个直接 PINS 误称完整全部 runtime，也不把原5400作为当前执行入口。未改的 hook 用实际传入 `driver_source` 记录当前身份，不硬锁旧5400。

第一阶段 `design453` 真实执行新族七shape固定、三active的完整453方程；原 actual-H FD、全部 native 32×10/tol2e−9、完整338×112与原 final audit、fullDN/collocation/BC 均保。只有原453完整接受且43f实际 capture 后，第二阶段才从该实际十词和场产生 fresh450 seed；它独立重新形成全450 RHS、preflight、current-H、FD/native/fullJ/final audit。第二阶段不是删除三个方程后重标原453结果。

两个阶段共享同一真实 raw client；lease的 `close` 仅释放本phase引用，实际 owner 只在 driver `finally` 关闭。原成功/异常/native关闭字段和每phase未访后缀保留。`adapter-status.json` 的 `actual_final_checkpoint` / `actual_final_checkpoint_directory` 仅在实际当前450成功后有值，43f checkpoint中 `actual_driver_source` 是本新driver，不伪造旧203来源。

## 7. 下一完整入口和真实原钟

原 cb057 launcher、c825 pipeline 与已有 postsolve 分支有明确的旧 tuple；本稿不让它们误认 R449。下一独立205接线必须逐项注册新 pipeline、owned launcher/必要reader与driver，保全部旧科学 callee/source pins，明确当前 namespace/deadline schema和真正 `GITHUB_RUN_ID/SHA`。root独占总体request/workflow及后继来源注册。

外壳必须传入原 job deadline 的实际文件及 receipt。它在 C/采样/两BVP/闭面消费者之间不重启、不复制新的start。候选准备/绑定本身不提供一个新钟。两个BVP的共享7200 process上限还受 job剩余时间裁剪；采样预留为显式caller参数；原2700读回/清理余量、quiet/reap和原内外科学预算不变。原197在m212资源停止、joint数值代表未开始的实际结果不被重写为joint方法已成功或失败。

205计划保留首次真实450后的全链：R437真实首次construction冻结、原径向读回、cuff atlas、shared场、metric、reach以及独立held在同一原钟内运行。R449 driver 的 `downstream_shared_prefix_metric_radial_tail_or_closure_not_paid` 诚实只描述本组件，不能让总体workflow在BVP成功后提前清掉下游还需的raw。只有必要读回完成且所有自有owner静止，才按原策略清理。若450未接受或下游预算用尽，保真实未启动/未完成范围，不造任何几何证书。

## 8. 读回、失败和清理范围

adapter每phase只输出一个必要JSON：`BEGIN_R449_CANDIDATE_NECESSARY` / `END_R449_CANDIDATE_NECESSARY`。`adapter-result.json` 是相同 canonical ASCII JSON含末LF；完整body限90000字节。超限保实际临时文件与身份，输出明确 `complete_necessary_readback=false` 并返回70；不编码、切块或截字段骗过限制。正常退出0，实际异常2，运输超限70；科学producer/native自己的失败不能借这些数字改称成功。

adapter异常保 `repr(error)` 与 traceback 于该临时小报告，若因完整异常造成超限也诚实70。driver的原异常/phase/native调用和原大科学表继续由未来必要reader按已声明范围读，不在此重复搬运。所有文件落在严格 `RUNNER_TEMP` 子目录，adapter要求fresh目录；本源自身不删除/上传raw、不建立artifact，不给过去已删raw造恢复文件。

来源不匹配和真实科学域失败分开：前者是参数/程序绑定错误；原严格结构条件保原factory含义；原domain证书未完成不等价BVP新增拒绝；center诊断不控制dispatch。新的准确点能否满足全域、112 far/native、453/450、全闭metric/reach/held都留待真实公开计算。没有以有限维投影、函数独立或浮点秩当准确证书。

## 9. 已完成的静态工作与未完成责任

本地只读取原source/已刊R439文字，选择十词、核原553字节身份，编辑标准文本/JSON并形成完整差异与hash。没有导入科学源、AST、编译、数值计算、独立fixture或额外审核门。所有 CLI语法/真实求值只在未来Actions既有流程。

本稿可以被作为新来源发布，不代表205运行已派发，也不预填当前204或任何未来run的结果。R449完整条件证明只说明新点的定义、合法结构合同和责任分离；它不宣称旧202 unit根移植到准确C，也不保证新点的coast严格速度、原BVP接受或全t闭面目标。
