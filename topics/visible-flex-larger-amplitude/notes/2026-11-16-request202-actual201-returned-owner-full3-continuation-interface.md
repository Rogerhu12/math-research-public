# Request202：actual201 真实返回 owner 的原完整十维三残差续算接口

作者：ChatGPT（AI，/root/exact_refinement），2026-11-16。本文对应独立 Request202；本请求尚未执行，实际结果预留 R439，由主控唯一读取。父结果见 [R430](../results/R430-actual201-complete-ten-49-accepted-and-resource-partial.md)，已发布于 `03e4f2a2e78ad42bad26b154c055041850f176d2`，正文13030字节、SHA256 `e5811de8a435541984cea4a03af97176a2caa2433f7d5ad18bd5bf79b007fc3f`。原完整方向与法向算法分别见 [R378](../results/R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md) 和 [R392](../results/R392-complete-three-residual-normal-correction-on-ten-parameter-predictors.md)。

## 1. 新初猜来自真实已返回的接受点

本请求以 actual201 最后真实被原三残差 Armijo 接受的十个 Decimal50 词作为新数值初猜，重新建立原有限字面模型。原16个八方向批、全局2400秒钟、每方向20个原 alpha、每 alpha 最多3次完整三残差法向修正及每次20档内回溯保持。独立入口仅增加当前明确父来源与新身份；已发布201七件和原运行不修改。

父 run 为 `43779219117`，source `aa2f1d05470df29f8e4546ccc990b99432a56a44`，compute job `133012382468`，report job `133025041213`。主控唯一读取两个终态 job；两份必要正文逐字相同，共72021字节，SHA256 `05677609373fa12f49a77ff4ac7ab9afff6c55b81fab1122a57194716f35a907`，此身份不含日志分隔 LF。实际原 status 为26610415字节，SHA256 `ad08a88e15ce2aba631f42a9061c0cfc37a1656b4fc444f3246bd94c379c7460`。

父完成49次接受、进入50个方向、记录148个原 alpha。方向0至48的原接受 alpha 均为0.25，normal_update2、normal_trial0、beta1；末真正接受坐标是 direction48、alpha_index2。随后 direction49 的 alpha1、normal_update1 完整响应尚未返回，原2400秒 whole-child 到时发送 SIGTERM，producer 受控返回75。该未返回响应和未访后缀不补记为数学拒绝。父 `diagnostic_completed=false`、`resource_partial=true`，`final` 与 `final_binary64_projection` 均未生成；末 FD、Arb 和453圆消费者未启动。父不是完整 completed checkpoint，也不是已接受的非线性 native/full-DN 场。

新初猜同时来自两个实际原字段：

- `current_accepted_ten_parameter_words`；
- `trial_conclusion.first_and_last_selected_original_points[1].original.actual_parameters`。

两路径十词相同，紧凑 JSON 为553字节，SHA256 `6997f1f39da6352df640f2a4ed0c458ba7682093a4be5b6f084cbc1206d22565`。完整原词按既定九系数加第十个 xi 的顺序写入配方：

```json
[
  "0.30062973421506012978085056886433029065227459871922",
  "0.23414995243815095772396826548078406374138322801271",
  "0.33647747984919215769881160722627287154578942138391",
  "-0.076788250748001044198553491053560316801285950761175",
  "-0.012644984398954316337192524040048383915654453873218",
  "0.93105463243557946020517305533089410280222845558971",
  "1.0603288865769761376496235316401386966048605641856",
  "0.48420097055766890836667277613635422160543274466952",
  "0.98024113195399845369795770161587595881297565345227",
  "1.0315706449400350571656845560403026865537136609228"
]
```

配方保留最后已返回点的原三残差：

```json
[
  "-0.01148012859003597209233890947990129916894713428656",
  "-0.0000049947198604813897321821989638208053362795205996",
  "-0.0061320261181862357764290952220839586346184794183927"
]
```

原 merit 为 `0.000084697560852552978246505900090867813381110759201695`，原接受 Armijo bound 为 `0.00013551471803799518912092218299363755135842067185466`。这些值仅是历史输入来源和只读对照；新 run 的 F、W、J、FD 与所有末消费者重新形成，不把旧读数作为本次评价或接受依据。

父实际 raw 已于 `2026-11-16T00:55:46.2136389Z` 清理。202不凭 status SHA 复造原数组、响应、checkpoint 或未返 normal 状态。主控交付的3405字节参数与来源文本 SHA256为 `26dea8ad93c57a4f535affe52862ffe4a08b57faa41bc14e95fd16d2c356ac5f`，只用于生成本请求的明确原词与 provenance；不作为新科学状态。

## 2. 七件发布范围

下表为六个运行／参数文件的完整 UTF-8 字节身份；本文是第七件文档。临时 `publication-files.json` 列七件准确映射，清单与文本差异是可从源重新生成的临时元数据，不作为科学输出保存。

| 仓库相对路径 | 字节 | SHA256 |
|---|---:|---|
| `topics/visible-flex-larger-amplitude/computations/geometry_20261116_actual201_ten_predictor_normal_resume.py` | 56686 | `874d81aeeaaaf68e4802fe8b11b4e87e334ebf27b9ed39e21e4618dd92b98c24` |
| `topics/visible-flex-larger-amplitude/computations/root_20261116_actual201_ten_predictor_normal_resume_readout.py` | 49199 | `b146e743a397386613393afe807849375df4c790b1c251d1d522fc04ace8d2b4` |
| `topics/visible-flex-larger-amplitude/computations/geometry_20261116_actual201_ten_predictor_normal_resume_temporary.py` | 22890 | `e07f1cf82d582d3f23bcb8964e5cec987f417ca2c27854439c0a34454ec3e87d` |
| `topics/visible-flex-larger-amplitude/computations/actual201-returned-ten-predictor-normal-parameters.json` | 23072 | `4ccea87c28a79f4714169ca7a670e3fd61cbc1a7bcda3bfb8394bdd45e5451b9` |
| `topics/visible-flex-larger-amplitude/computations/public-actual201-ten-predictor-normal-resume-request.json` | 80466 | `f56f97cb96ee37a53b3a5fb19e73386f53f2d6b84e5421b1485a840e358d749c` |
| `.github/workflows/visible-larger-public-actual201-ten-predictor-normal-resume.yml` | 33535 | `193fa3af9e6e404858fd229cabd3075b19555f54b5ba2eeefb5d9cf6984ac7b5` |

新身份明确为：

- 科学 schema：`R259-actual201-returned-owner-full-three-normal-continuation-v1`；
- 科学 status：`actual201-ten-predictor-normal-resume-status.json`；
- 配方 schema：`R259-actual201-returned-owner-ten-predictor-normal-continuation-recipe-v1`；
- 请求 schema：`public-actual201-ten-predictor-normal-resume-request-v1`，`request_number=202`；
- wrapper schema：`request202-one-persistent-ten-predictor-normal-continuation-v1`；
- 必要读回 schema：`request202-persistent-ten-full3-normal-necessary-readback-v1`；
- 最终正文帧：`BEGIN_VISIBLE202_COMPACT_SUMMARY` 与 `END_VISIBLE202_COMPACT_SUMMARY`。

## 3. 相对已发布 actual201 的全部改动边界

基线是 source `aa2f1d05470df29f8e4546ccc990b99432a56a44` 的完整七件，而非某个审稿缓存。旧 producer 为54384字节／`2911f896d2366b0cc4cf4095e7f260a412dada90cbd790936751810d036f4da1`；旧 reader 为49199字节／`cb724a6e5c3c7f79a9381b53d6e77e13edc5bd4323e08dfb826a438143b02df9`；旧 wrapper 为22890字节／`809cf513f25dbed1ff937e28d5a7b949c93d49f8fe20e55338d35e28539eed43`。旧配方21198／`119d751645425d343f38720a4145bf50831551756a431b5dda53e90df18d7712`、旧请求77482／`9c30ac0d61c7cb3672c3dbc1f2f5fab47cd3b65b879226ce1357f9a7344ae981`、旧 workflow33137／`5b836f552375445d2d36e476cf07bf954aff87b8331ca7e415c389adbc948f9b`均按真实字节取作差异基线。

producer 新增 `ACTUAL201_PRODUCER`、其 SHA、完整真实 `ACTUAL201_ORIGIN` 与十词，旧 ACTUAL183／185／189／194／198 常量逐行保留。当前 recipe 分支明确从实际198切换到实际201；原来源检查、独立新 basename/schema、当前来源计数和事件标签随之更新。完整 `original_normal_counts` 与 `continue_original_blocks` 函数正文逐字不变，原数学模型、QR/Cauchy、法向 helper、真实试探、全部末消费者正文不改。它是有独立身份的新 producer；不能把源字节相同或原 source SHA 继续成立作为描述。

配方仍只有原两种合法入口语义：本次明确固定的 actual201 partial 返回 owner，或本新 schema 将来真正完成且至少一次原接受的 own-schema 记录。后一个分支仍要求真实 status/summary/source/run/size 与本 producer 来源，不能把本次 partial 父伪称 own completed。对未来其它 partial 续接也不能伪造完成状态。

reader 只更新当前 producer/schema/status/hash、request202标记与53件当前闭包；所有必要标量选择、原字段读法、错误／未返范围和90KB策略保持。wrapper 只更新新三源／配方／请求身份、123+21 pins、52→53闭包及标签；原 `Processes` 生命周期、2400秒终止、readout、错误和静止清理语义保持。

请求另外纠正了一处纯文字历史残留：旧 `arithmetic_contract.persistent_owner` 仍写 Actual189；本请求将它准确写作 Actual201。该对象其它数值／算术字段不动。冻结 helper 的 `future_initial_parent_must_be_actual183_complete_final_words_not_prefilled` 字段仍逐字保留；它是首次引入历史标签，现行父入口由本 recipe 与独立 schema 明确绑定，不让这个历史标签虚构一个新父 gate。

工作流保留旧全部 explicit pin 项，再新增本三件；不能用名称替换覆盖旧祖先 pin。当前 parent guards、配方完整 hash、request hash、source计数与 namespace 同步。原 setup、源恢复、规则 runner、科学命令参数、report 与 cleanup 的控制流不改。

## 4. 完整来源闭包

整个请求保留原201的122个科学 pins，再新增当前 producer，合计123。工作流支持保留原19个 pins，再新增 reader 和 wrapper，合计21。原 ancestor来源、原metadata支持文件和四个数学输入均不替换或删除。

当前 producer 真正消费的闭包从 actual201 的52件扩为53件。新 `origin_producer` 完整等于旧 `current_producer`；新 `current_producer` 是该52件加新 producer 一件。原41件九控制基础及全部后继来源准确保留，不能把父52冒作当前53。科学 producer、reader、wrapper、request 与 workflow 都以同一数目和每个 basename/SHA 绑定。

原201 producer 现在只作字节绑定的来源；它的 main 不再次执行。原6b55完整十维方向、原3bec完整三残差法向 helper、原0924 family及8cb8 model仍为实际数学调用者。原低维／旧搜索主程序没有因保存在 pin 集里而重复执行。R378与R392的完整原算法责任不变。

四个原数学输入仍由既定历史 commit `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复原文件字节：

| 输入角色 | 原字节 | SHA256 |
|---|---:|---|
| `accepted` | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| `prepared` | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| `tail_anchor` | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| `tail_config` | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

原公开78源缓存仍由原恢复接口生成于 RUNNER_TEMP，原source身份全部保持。它与123科学pins、21支持pins、当前53消费闭包是不同层级，不能合并一个计数来省略真实来源。

## 5. 数学方法与原门完全保持

十维 owner 是 Decimal50／ROUND_HALF_EVEN；九个原表系数与 xi 全部可以参与当前完整3×10响应。固定形状仍是 catalogue3、support1、power4，对原 stored-width、support、完整699节点／698 cell、原112终端和有限字面表逐项保持。没有改成新的准确连续 C，也没有以旧零 core／线性锚当非零 native 成功。

原固定尺度 S 来自 actual157 的九个原词，九个尺度仍为 `0.01*max(1,abs(actual157_p_j))`，xi尺度为0.01。它们不由新201返回点重算；原 `0.0000390625` 半径只留父 provenance，本轮原缩放信赖半径仍是1。所有原外步与法向工作共用这一个 S／半径；批间不会重置 owner、尺度或总钟。

原全三未加权 merit、原 Jd 形成、原 full3 slope 和 Armijo 门保留；Armijo系数仍为原 binary64 0.2 的准确 Decimal 提升，原停止阈值仍为原 binary64 1e-8 的提升。完整 QR 与其原 Cauchy fallback 是数值候选，不新加 rank截断、误差对拍、响应一致性或区间精度门。

每一个原 alpha 都冻结其原 outer base、F、W、Jd、斜率与 Armijo bound。最多3次法向更新使用 fresh 完整3×10响应，针对完整三分量 `F(base)+alpha*Jd` 的偏差；每次最多20个真实法向试探。候选总位移仍投回同一 S 球。仅原 full3 Armijo 接受可改 owner；其它 working point 即使偏差下降也不成为接受锚。下一原 alpha 重新从该 outer base 开始，不继承未接受 working point。

一个新 run 最多16个原八方向块，即128方向；每方向最多20个原 alpha。只有原完整八方向预算停止文本允许下一块。遇原全部20档拒绝、域／数值失败或资源终止，依原控制流停止；不在相同点悄悄重新开一块来绕过拒绝。批间下一完整响应 fresh 形成，未访与未返地址保持不同状态。

新202不是201中断调用的内存续执行，而是从真实十词重新评价的新实验。201的旧 W／F 可显示只读差异，但不能补新评价、重用旧 J 或声明201未访后缀已经完成。

## 6. 末责任与资源范围

原初始／末尾共120项轴向FD义务不变：初始及末尾各十轴、三步 Decimal 检查与各十轴、三步显式 binary64 投影检查。它们全局各执行一组，不按16块重复。十参数、三残差、完整112固定锚及原响应仍逐本次模型 fresh 形成。

原 final消费者保留160bits／depth14的完整十族 scalar域和原453 physical circle视图；七形状系数按末真实值冻结，再用原三 active 坐标与原完整物理行。显式 binary64投影是末消费者输入，不能覆写 Decimal owner。未开始或未返回的FD／Arb／circle／full112义务不能由搜索进展或绿色report代付。

该有限低核搜索本身不调用非线性 native/full-DN求解，不生成已接受的非零完整场。所有这类标志按原 producer范围保存；真实低三接近根也不自动支付后继112非线性场、完整J／FD和独立审计。

| 资源 | 原固定范围 |
|---|---|
| producer与whole-child | 各2400秒，含本次import/setup/初FD/搜索/末消费者 |
| 原方向预算 | 16×8，最多128；每方向20档原alpha |
| 法向预算 | 每alpha最多3次更新，每更新20档 |
| 终止宽限 | SIGTERM后90秒，之后才强制结束并等待回收 |
| 必要reader | 300秒，终止宽限30秒 |
| 科学step／compute job | 50分钟／65分钟 |
| 规则同步 | 原2700秒真实pull/rebase／双README变化即原停止 |
| 必要正文 | 单份ASCII JSON最多90000字节 |

预算只定义资源上界，不能保证128方向或末消费者会在一次 run 内付完。原有实际201就是在 final未开始时触及2400秒。202不因当前 W 已下降而缩短或跳过任何门，也不为“必须完成”延长2400秒。

## 7. 原规则与生命周期

工作流仍使用冻结 `root_20261114_current576_rules_runner.py`。真实启动时按源码 hash 与当前 checkout 两份已读 README Git blob 绑定，再把原 runner的明确 BASELINES更新成这两份文字；PERIOD_SECONDS、原实际pull/rebase、差异停止、H规则同步行和日志边界不变。

当前已读 root README blob为 `21bd547f56590b7f2dd279d0297efb289a9b2783`，topic为 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。有真实变更按原规则停，不能自行跳过或宣称未发生的pull。compute保原 `contents:write`／`actions:read`；token只供原实际Git与必要Actions元数据，不写文件，不交科学child。

wrapper所开科学和reader children不另建 detached session，继承该规则控制路径；wrapper转发中断，原宽限后强制结束时仍wait/reap，并记录每个已launch/reap child及同run/source/wrapper身份。独立 always读回仅按现有完整原status处理，不重启科学。

明确删raw前仍须必要summary成功、必要error读回成功、实际owner静止回执吻合同一run/source/current wrapper、所有wrapper children回收。若任一不齐，记录真实失败／partial并跳过主动删除，随后由runner生命周期销毁临时目录。不能把数学partial等同传输失败，也不能把读回0等同科学接受。

全部原payload只在RUNNER_TEMP，保原large stdout身份而不搬运科学树；不upload-artifact、不Release、不把可重算raw提交Git。token从科学child环境剥离。旧原输入Git对象缓存也只在ephemeral runner。

## 8. 单份必要读回责任

reader完整读取实际status与原嵌套记录，只做JSON／字节／地址与原字段选择。它不重算FD、Merit、投影、矩阵或接受门。单份必要正文保以下范围：

- 全128计划方向与16块地址、所有实际原alpha的地址／决策／原必要计数、每个真实接受Armijo bound与owner merit；
- 全部已执行与未启动后缀、normal更新／primal／response已开始但未返回状态、原停止原因与错误；
- 所有实际嵌套试探在Actions中的完整分类和完整原对象身份；必要正文选取首末实际owner点、相应真实参数／三残差／merit与投影／工作点范围；
- 初始／末十词、三残差、merit，原FD各必要级别最大误差／flags／异常，原scalar／circle／full112实际存在的终检字段；
- 当前source／input／recipe／origin／status字节身份，wrapper与规则运行实际结局、传输／资源／数学停止分责。

原完整Q/R/J、全FD扰动表、完整112矩阵、所有中间working vector等仍只在Actions临时对象中，必要正文不字典编码或分段重构它们。中间所有 formed slope／predictor merit历史按原201已声明的必要选择，不冒逐词已被主控重读；首末原值、全history身份、全部地址／决策／owner merit和接受bound范围准确保留。

完整工程stderr每文件≤12000字节时保原text；更大时仅全身份与显式首末6000字节片段，必要error步骤失败且主动cleanup不合格。这一原传输限制不冒完整错误全文。必要summary若超过90000字节，原over-budget身份/范围与exit70保留，标明传输不完整，不扩大上限、不拆包、不截科学树来假称完整。

compute与独立report通过原GITHUB_OUTPUT传同一必要JSON。report只打印完整单份正文、bytes/SHA和实际compute结果；它不运行或恢复科学。summary SHA口径为最终ASCII正文原字节，不含日志分隔LF。未来实际字节数未预言，也未在本地以科学fixture演示能够容纳。

## 9. 完整重算入口与本轮未做事项

公开Actions的完整命令由workflow按实际checkout和临时输入路径生成。唯一科学child实际参数保持：

```text
python -u geometry_20261116_actual201_ten_predictor_normal_resume.py
  --accepted <original accepted bytes>
  --prepared <original prepared bytes>
  --tail-anchor <original anchor bytes>
  --tail-config <original config bytes>
  --parameter-recipe actual201-returned-ten-predictor-normal-parameters.json
  --parameter-recipe-sha256 4ccea87c28a79f4714169ca7a670e3fd61cbc1a7bcda3bfb8394bdd45e5451b9
  --out <request-owned temporary science directory>
  --directions 128 --backtracks 20 --decimal-digits 50
  --interval-bits 160 --interval-depth 14 --wall-seconds 2400
```

外层wrapper绑定本请求完整SHA `f56f97cb96ee37a53b3a5fb19e73386f53f2d6b84e5421b1485a840e358d749c`、整个仓库目录、原四input路径文件、同namespace `rule-sync` 和 `actual201-ten-predictor-normal-resume-temporary`。它通过原rules runner启动；无法把上面命令从源身份／输入／规则环境中拆出后冒作已经完成的公开实验。

六份完整文本差异如下，可由两份公开正文重新生成：

| 临时完整diff | 字节 | SHA256 |
|---|---:|---|
| `producer-relative-to-actual201.diff` | 13696 | `da688356fbdd8ace071f93e619b65064712efcea10d169ec1b1d1a1dab69b37e` |
| `reader-relative-to-actual201.diff` | 5588 | `e5551f7e51f1ceaeb848743af1dd25e6143ef113c89c6daea23eb8c06aa8a2c4` |
| `wrapper-relative-to-actual201.diff` | 12654 | `6b23ffae276a2e2da7ef9f4e2c97f22bfac930654935d1f090a6ebe0677db3c3` |
| `recipe-relative-to-actual201.diff` | 9872 | `fae22aab7e1f412862b5eb646f646378e9d30ccf8efc03d4fc10c76a457836c4` |
| `request-relative-to-actual201.diff` | 23338 | `850ec49c4ed986f7f00d758746281baf17b7778f5c343aeed6552ea5178cdd22` |
| `workflow-relative-to-actual201.diff` | 35023 | `abbb14cf6cbfee51f7fc87ab127887c9f81792c50476e7034af8c7c9c43afe9b` |

本地仅进行了原源读取、精确字符串修改、JSON字段比较、完整SHA与逐字方法正文比较；没有import、AST、compile、fixture或科学数值执行。原Actions内源码语法步骤仍在原workflow，不另造审核门。本次不创建Gitref、commit或dispatch；主控唯一发布。当前没有202 run/job、输出SHA或科学结论，不预填R439。源与参数一旦正式执行，全部当前结果及未付范围以真实Actions必要读回为准。
