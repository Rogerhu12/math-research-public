# R340 — actual157：完整九维残差二次平方模型的八方向原链、四次接受及读回范围

作者：ChatGPT（amplitude）；2026-11-15 UTC。本文只读取公开 Actions 的原 JSON、字符串、字节身份及整数记录计数，并作源码与条件代数分析；没有在本地运行模型、差分、矩阵乘法、范数、优化或科学 fixture。当前已完整核实 report job 的原链摘要；compute 大日志的完整分段尚未取得。这个未读范围在下文明确保留，不以流程 success 代替科学或完整字节审计。

## 1. 已实际得到的结论

Request157 完成原 8 方向批次，4 个方向接受、4 个完整拒绝。接受发生在方向 0、1、2、7，全部为 `residual_quadratic_straight` 的首档 `alpha="1"`；方向 3–6 每次先没有形成合格的主模型候选，再在原 `original149_normal_fallback` 路径试完 20 档而全部拒绝。原 report 共记 84 次真实试探：4 次直线、80 次 normal。没有未启动的外方向；各路径未访问的 trial 后缀仍按原记录解释，不能将“外方向全做”写成全部可用 trial 都执行。

原完整三方程 merit 初末字符串为：

```text
initial = 4.9632137876766619823138638310334280578058678269248
final   = 4.9632137875241047283817296655204217818016943746082
```

初值与 [R335 actual154](R335-actual154-full-nine-curvature-and-seventy-straight-trials.md) 已重建末 `final.unweighted_full3_merit` 逐字相同。方向 0 原实降为 `1.525572539263998816310751188272764882692E-10`，模型预测与真实下降接近；其后接受的下降已分别为 `5.7342838819311571768939884066E-21`、`2.9751698E-42`、`4.710E-46`。本次没有得到较大的原三残差下降。

初始探索半径 `0.01` 是已声明的新策略，并未假称继承 actual154 的末半径 `0.000078125`。方向 3–6 的四次完整拒绝依原规则将半径依次 quarter；末半径为 `0.0000390625`。

原 chain 明确：

- `phase="diagnostic-completed"`，`diagnostic_completed=true`。
- `original_Armijo_accepted_point_count=4`，`rejected_direction_count=4`。
- `high_precision_original_unit_stopping_tolerance_met=false`。
- `high_precision_full112_linear_right_tolerance_met=false`。
- 两项对应的 `binary64_projection_...` flags 也均为 false。
- `native_nonlinear_solver_called=false`、`nonzero_field_completed=false`、`success=false`。
- `scientific_native_or_BVP_acceptance_claimed=false`，`final_point_is_not_an_accepted_nonzero_field=true`。

这只是同一有限字面模型下的真实候选搜索结果。它没有给出非零完整场，也没有给出连续方程或区间证书。

## 2. 真实运行、停止原因与读取边界

- Run：[43729310294](https://github.com/Rogerhu12/math-research-public/actions/runs/43729310294)。
- 触发源码：`c71cbeac7fd13c65cf50c7eb39842e9949737b25`。
- compute job `132858021333`、report job `132861152631` 均 completed / success。
- 元数据逐项显示源码和父绑定、78 源恢复、科学步骤、读回、完整 child 错误保留、临时清理步骤全部 success。
- 科学原 `seconds=599.243845649`；wrapper 原 `seconds_wrapper=604.8866475630001`。
- 子进程与 reader 返回码均 0；`partial=false`、`resource_partial=false`、`received_signal=null`、`wrapper_exception=null`。
- 科学停止字符串：`explicit total direction budget completed, counting accepted and rejected directions`。
- wrapper 停止字符串：`explicit_single_original_eight_direction_batch_completed`。

### 2.1 已完整取得并核验的对象

终端不可用时，从已授权的 GitHub 官方集成读取 report 原日志。接收的完整文字按 UTF-8 编码为 **64,026 B**，SHA256：

```text
d4e60ea1eca7a4cd81d607915fd13e6f810133b89d52e3307a4266ecf879a314
```

只去掉严格锚定的 GitHub 行首时间戳及首行 BOM；59 个原行运输前缀被识别，没有替换 JSON 数字、空白正文或参数词。原 `BEGIN_VISIBLE157_CHAIN_SUMMARY` 对象为 **29,684 B**，SHA256：

```text
9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd
```

该身份与其后原 `visible157-chain-summary-sha256` 事件一致。run/source 字段亦与实际 metadata 一致。所有本文科学数值均从这个原对象选择；对记录条数的相加仅为整数计数，未重新评价 merit、模型、导数或误差。

### 2.2 仍未取得的完整 compute 对象

compute 日志接口连续两次在约 3–4 秒返回 `Transport closed`，没有交付日志正文；metadata 与较小 report 日志接口正常。不能据此判定是 GitHub 丢失日志、模型异常或确定的大小上限。停止了重复拉取。

已暴露的 `github_fetch_workflow_job_logs` 接口只有 `repo_full_name` 与 `job_id`，没有 Range、step、start/end 参数；通用 `github_fetch` 接口只有 URL，并明确拒绝过大或非 UTF-8 响应。未猜测私有日志端点、未请求凭据、未以重新运行科学代替读取原结果。

原 chain 引用：

| 对象 | 原声明字节数 | 原声明 SHA256 | 当前核实范围 |
| --- | ---: | --- | --- |
| producer 完整 status | 51842612 | `931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0` | report 原描述器已核；status 正文未取 |
| 分段 primary | 89063 | `7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2` | report 原描述器已核；primary 正文未取 |
| producer stdout | 155590 | `9f5d91d729e5af2aa19ab14fa8f5daf2221831223fa5c9c67270acdb77cdb0de` | report 原描述器已核；stdout 正文未取 |
| producer stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | report 记为空；未重读 compute 错误块 |

完整 view 的每段、每模型候选的全部向量/shift/QR 残差、80 个 normal 的完整轨迹、原初末 FD 各数值和 Arb/circle 原细项，目前没有完成本次独立逐段重建。本文不填写这些缺失数值，也不使用“完整 fullview 已核”“162 项均 valid”或“所有域均过”等超出已读对象的表述。原 chain 的 `full_scalar_normal_and_projection_records_in_compute_log=true` 是原 producer 对输出位置的声明，不是本次独立传输核验的替代。

## 3. 八个方向的原完整摘要与未访问责任

方向编号沿原 0–7。表中的“模型点”是原 `polynomial_model_points_evaluated`，“合格池”是原 `polynomial_model_candidate_count`；后者只计已满足原点形成斜率严格负及完整模型 merit 下降等有限条件的点，不是无约束全局候选空间。

| 方向 | 入半径 | 模型更新 | 有限模型点 | 合格池 | 真实直线 / normal trial | 实际结果 | 出半径 |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| 0 | 0.01 | 32 | 1408 | 1300 | 1 / 0 | 直线，α=1 | 0.01 |
| 1 | 0.01 | 32 | 1766 | 1542 | 1 / 0 | 直线，α=1 | 0.01 |
| 2 | 0.01 | 32 | 1864 | 1593 | 1 / 0 | 直线，α=1 | 0.01 |
| 3 | 0.01 | 32 | 1920 | 0 | 0 / 20 | 两路径均未接受 | 0.0025 |
| 4 | 0.0025 | 32 | 1920 | 0 | 0 / 20 | 两路径均未接受 | 0.000625 |
| 5 | 0.000625 | 32 | 1920 | 0 | 0 / 20 | 两路径均未接受 | 0.00015625 |
| 6 | 0.00015625 | 32 | 1920 | 0 | 0 / 20 | 两路径均未接受 | 0.0000390625 |
| 7 | 0.0000390625 | 32 | 1915 | 1 | 1 / 0 | 直线，α=1 | 0.0000390625 |

整数记录总计：256 个模型更新、14,633 个有限模型点、4,436 个合格池记录、84 个真实 trial。这里的合格点记录允许相同数值点在不同实际记录位置出现，不能称为 4,436 个两两不同的点。每方向 `polynomial_optimizer_completed=true` 只表示该有限模型算法完成了声明的路径/预算，不表示找到模型全局最小点。

每个接受方向的主直线路径只访问 trial 0；原 `unvisited_trial_indices=[1,...,19]`。其 normal 回退 `started=false`，原理由是 `not reached because a straight candidate passed original merit`，20 个 normal trial 槽均未访问。

方向 3–6 的主路径 `started=true` 表示已尝试形成模型方向，但实际直线 trial 数为 0，全部索引 0–19 未访问。原错误位于：

```text
complete_path_status.residual_quadratic_straight.direction_model_error
= NumericalFailure('No completely evaluated model point supplies negative original formed slope and model decrease')
```

外层摘要的 `direction_model_error` 字段在这些行仍为 null；本文沿实际嵌套路径读取错误，不用该 null 覆盖已记录的形成失败。随后 normal 路径的 `trial_count=20`，`unvisited_trial_indices=[]`，原停止为 `all20 actual trials rejected`。这些行的原结果理由是：

```text
both bounded proposal paths failed or rejected; current point unchanged
```

四次半径更新均声明 `current_parameters_state_and_J_unchanged=true`、`parameter_point_accepted=false`，只 quarter 半径，没有暗中接收新的参数点。

## 4. 四次实际接受及模型预测

下表保留原输出字符串；没有本地计算差值或比值。

| 方向 | 实降 | 原预测降 | 原实降/预测降 | 接受后原完整 merit |
| ---: | --- | --- | --- | --- |
| 0 | `1.525572539263998816310751188272764882692E-10` | `1.525574546850866876029784519173585690378E-10` | `0.99999868404538329258618895697598388393451926982823` | `4.9632137875241047283874639494023529389785913386556` |
| 1 | `5.7342838819311571768939884066E-21` | `5.7342838818809847658346151505E-21` | `1.0000000000087495513115258401499180081906761649779` | `4.9632137875241047283817296655204217818016973502490` |
| 2 | `2.9751698E-42` | `2.9777457E-42` | `0.99913494963656567449665026801986482593191218444208` | `4.9632137875241047283817296655204217818016943750792` |
| 7 | `4.710E-46` | `1E-49` | `4710` | `4.9632137875241047283817296655204217818016943746082` |

方向 0 的全步确实通过原完整三残差接受条件，并且在这个实际很小的方向上模型预测与实降接近。这和 actual154 某些较大试探出现巨大真实 merit 的情况不同，但本次接受并没有实现较大距离或较大残差下降；不能仅因 `alpha=1` 或半径上限 `0.01` 就称它为“大步”。

方向 1、2 的下降分别降到约 $10^{-21}$、$10^{-42}$。方向 7 的记录是预测 `1E-49`、实降 `4.710E-46`、比值 `4710`。该比值的分母已处于有限 Decimal50 merit 字面的极末端；它不构成可靠的总体曲率精度或相对误差证书。仍保留它为真实原记录，不修写为 1、不删除该接受，也不将它证明为精确实下降。

## 5. 原直线动作与共同回退方向

以下仅逐字抄录 chain 已保存的参数方向、三响应和原 slope。它们不包含完整九轴 J 或全 Hessian，不能据这些方向性点积计算全梯度范数或矩阵秩。

### 5.1. 方向 0 的原直线记录

```text
actual_direction = [
  1.1249411220714946445816961457072054577205592174973E-8,
  -7.5912233315800779450379554816703521655014908194830E-8,
  3.5208745188969773763381391288756534363057594935412E-7,
  -2.2567751476740358574664302182140001886195870437034E-7,
  -5.6703447172245156481258036611063292019245707062457E-8,
  -2.3075161501125120919427073221025284596135256506428E-7,
  1.4286785574840402757097002377739833239077614315941E-7,
  -3.5755211011389817982528443580542626635076604225868E-7,
  -0.0000033671480189493384101964726678748179298048961780651
]
actual_direct_response = [
  6.037462792855099480041180729603436983704579115558E-10,
  -9.5032606044276421288837703501022910582836551669328E-7,
  -0.000074981280872870564528514611399752885403015823900733
]
actual_full3_slope = -9.440443767701830731503064708255845923767006114724E-11
selected_polynomial_model_merit = 4.9632137875241045276287771434304496058885092578870
actual_accepted_merit = 4.9632137875241047283874639494023529389785913386556
```

### 5.2. 方向 1 的原直线记录

```text
actual_direction = [
  3.1377896323654202993680112747281696045229255614680E-13,
  -4.6336591553336947615322936420737019267360452974770E-14,
  -5.9083767167092161275074748222274403776432353573563E-13,
  -6.5412078742966885756899212125143981053345742190352E-13,
  1.6680329691047720180440822586831626868765898247574E-13,
  -5.4022340619049707415000212171519429453420466506549E-13,
  1.4036821972206899523584426470923754201726234637477E-12,
  -1.9302322987261760491558997959564414803489365332457E-13,
  1.0413523570443998633885942349311873692962923670198E-11
]
actual_direct_response = [
  -7.7295062880443705163507047987370137357808445815E-17,
  -6.0271320605101438779158972375075680699635065224038E-14,
  5.8320391560869314277841301036300545880822643330815E-11
]
actual_full3_slope = -1.146854800770797978608355805044598730947208421E-20
selected_polynomial_model_merit = 4.9632137875241047283817296655204719542127567235051
actual_accepted_merit = 4.9632137875241047283817296655204217818016973502490
```

### 5.3. 方向 2 的原直线记录

```text
actual_direction = [
  -9.6655247918049695213497092980801481394525004502949E-25,
  1.6087678759964974767406704460370294853790500057586E-23,
  -4.6032142010921778793632497582916681334849093019074E-23,
  4.6663149390009263831180412560278985115683478364673E-24,
  7.8808882081015240638552299491425598759853444482125E-24,
  1.5631037618270504084606312353607221834324041756471E-23,
  -7.2849989122650628154677507091994638932829152174324E-24,
  5.4225429686904175231603873396552527926417958021049E-23,
  4.7772309136047620812158256246285688970658104278214E-22
]
actual_direct_response = [
  -2.45326684608175368404699879085265868487084541E-30,
  6.17592155764837238978187720919204168873708310543E-27,
  -5.554163006620399738343920914854345465730719011427E-27
]
actual_full3_slope = -5.955490749187277468746225671229162447451E-42
selected_polynomial_model_merit = 4.9632137875241047283817296655204217818016943725033
actual_accepted_merit = 4.9632137875241047283817296655204217818016943750792
```

### 5.4. 方向 7 的原直线记录

```text
actual_direction = [
  -1.3388705061309679382220650033068063326738009353863E-28,
  -1.9538461843192148259595691999638508327859268841418E-28,
  2.4049240054581121732181521222695286114875831419503E-28,
  -9.2740754131832229714335327513528598829978759312573E-29,
  5.9233455949937200582957723935864399888495032288848E-29,
  2.2824144454296613146907088131217115481881289670298E-28,
  -1.7334795000491970450980185078741138782302971329630E-29,
  -9.7110543401773665992656732845162527832508130628107E-30,
  1.8010503018080409705120001396770915812145803199537E-29
]
actual_direct_response = [
  7.99825145353648907785357118661130153489E-40,
  -2.0056236456447269739868742908376109260820588E-36,
  2.6055439296697124359062264941766373487816E-39
]
actual_full3_slope = -9.001213996316682550837284723895131415607E-54
selected_polynomial_model_merit = 4.9632137875241047283817296655204217818016943750791
actual_accepted_merit = 4.9632137875241047283817296655204217818016943746082
```

### 5.5. 方向 3–6 的共同原 normal 提案

四条记录的下列 direction 字符串经元数据逐字比较完全相同；source point 按原半径记录保持未变。该事实不推断 80 条内部 normal 轨迹逐字相同，因为这些完整轨迹尚未取得。

```text
actual_direction = [
  -5.2009053298512379196262046224685341700075904675181E-12,
  -7.5898072197443487146651033810511902194907545231880E-12,
  9.3420401902936614753572707626074156113263684138581E-12,
  -3.6025581282878086413616784269977392730448382716731E-12,
  2.3009514015346623207398171774307913738783126408234E-12,
  8.8661460535630078445624483479078552842010409498132E-12,
  -6.7337824903222741078481200149869721415259842113293E-13,
  -3.7723046437296896751502917783014254555301107195668E-13,
  6.9962644416392262107811082879053688421390555825301E-13
]
actual_direct_response = [
  1.321531523682309497271463388E-35,
  -3.2860137765986219947793523056252E-32,
  4.2689231936543551437295509019E-35
]
actual_full3_slope = -3.4965638300494613080580642847083231438219954216472E-37
```

这个提案的真实方向性 slope 仍被报告为严格负，但极小；每次原 20 档真实试探均拒绝。没有读取每个 normal 的目标误差、内部接受点和原实际 merit，故不能把拒绝唯一归因于 normal 精度、域、曲率、目标可达性或某一个未读取字段。

## 6. 原调用、初末责任和当前有限范围

原 chain 的调用计数完整为：

```text
primal_attempts = 193
primal_returns = 193
forward_attempts = 125
forward_returns = 125
forward_columns = 1061
second_forward_attempts = 10
second_forward_returns = 10
second_forward_axes = 90
second_forward_symmetric_pairs = 450
exceptions = 0
```

这是原持久高精度模型的已存计数。`exceptions=0` 不替代全部 polynomial 运算、normal 逻辑、原64投影域、Arb 和最终圆检查的逐条结果；这些细项属于仍未取回的 compute 分段。

原 chain 将 `original54_FD_checks_and_high_precision54_FD_checks_completed` 和 `initial_and_final_second_axis_checks_completed` 均记为 true。冻结源码的初末合同是完整 9 列、三档的原64投影一阶、Decimal 一阶、Decimal 二阶读回，合计每端 81 条、两端 162 条；“合同要求与原完成 flag”已读，但本次没有据原 fullview 独核每条 `valid`、误差及异常。Arb160/depth14、完整453圆、full112 的原责任保留于源码；本报告不借用 actual154 的 1586 leaves 或圆残差作为 actual157 数值。

四项最终 unit/full112 flags 均为 false 已由 chain 直接给出。没有取得本轮末三方程、full112 向量或其最大项正文，因此不把旧154的末方程字符串当作本轮值。即使 high109 在别轮被记录为零，也不能据此补写本轮高模值、Schur 或 nonresonance。

## 7. 真实末九词与下游来源

以下是本轮 report 直接保存的 `final_persistent_parameters`，与同一对象的 `current_persistent_parameters`、`last_accepted_parameters` 和 restart literal 字段一致。它们是有限 Decimal50 科学输入词，不是已接受非零场，也不是精确实根：

```text
0: 0.30552142546786087419329326763885317892313777930545
1: 0.21644987290946319325196797861927627381324526334114
2: 0.34270150727769461288268268825412573632054712673319
3: -0.063223623342288894213621979760433326917938764055697
4: -0.017474541697462463794792191406211542045739295377083
5: 0.93761104499027068067117010211647732552611947830979
6: 1.0751309729055790270477681013298138652831191583353
7: 0.68868893897292614021176494008067699691013641552647
8: 0.93853282406083699927458787857662556746972349511891
```

末半径原词：`0.0000390625`。若后继改变探索半径，必须显式声明新策略，不能假称原 radius 原样续接。本轮 `exact_persistent_restart_components` 自身仍标记 `this_record_alone_is_not_a_ready_parent_recipe=true`；实际父配方还必须绑定本轮 source/run/status/primary 身份。旧 large raw 被正常临时清理不改变这个责任，也不许可人工重造时间字段或伪造旧 raw 身份。

真实父为 actual154：run `43724606619`、source `2a4ce61f26a2f9d6f0f2729e037ee6c0b8220e5b`；父 status 5,917,531 B / `b4c1e07a3d81dd8eb64f3ba28a889f2868accd3b666c14c3deb4ddccef835e83`；父 primary 88,658 B / `7e03106069419b6d701bc0b86479c96fbf9615bdb8b761e01142110bd6ab5fed`。report 中全部 origin 字段与本次原配方对应字段逐字一致。

## 8. 原模型与源码责任

本轮仍用原 Decimal50 字面节点/表/边界模型。新算法在每个真实方向形成全部三残差、完整 $3\times9$ 一阶响应及三个 $9\times9$ Hessian，并冻结相对尺度 $D$。主模型为

$$
Q_i(y)=F_i+(JD)_i y+\frac12y^T(DH_iD)y,
\qquad
\Phi(y)=\frac12\sum_{i=1}^3Q_i(y)^2.
$$

它与 [R336](R336-complete-nine-residual-quadratic-square-and-finite-globalization.md) 的完整模型及有限选择责任一致，不是只将原曲线路径的 ray 二次项重新定标。真实主路径仍是 $p+\alpha Dy$，原 complete merit/strict slope/Armijo 才接受；原 normal 是单独标签的失败后回退，不混用路径二阶预测。

本次源码和配方身份：

| 文件 | 字节数 | SHA256 |
| --- | ---: | --- |
| geometry_20261115_nine_control_decimal_residual_quadratic_trust.py | 31941 | `ef61c5f19370a302b198901a7691fda31ed0a6619d9f9dcafc147f6b1bdc3180` |
| geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py | 28570 | `54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100` |
| root_20261115_nine_control_decimal_residual_quadratic_scalar_readout.py | 17532 | `a49ebce03156e8ee620ea7cab62e51c32f2a924458ad6d2320e85cf91398897d` |
| geometry_20261115_nine_control_decimal_residual_quadratic_temporary_batch.py | 22398 | `c992f30af23a94535a6dff70342172f5a066498c77e53a15e60e0e2222ac90f8` |
| public-nine-control-decimal-residual-quadratic-parameter-recipe.json | 3184 | `2dba85467fd34435efc0a4f44ed0335c787c049a6095735b955ad365aa62f49f` |
| public-nine-control-decimal-residual-quadratic-request.json | 55526 | `94e01eeb04f24f93463d0d59602b228c7ea061186edb54f5d99bb35168199dd6` |
| visible-larger-public-nine-control-decimal-residual-quadratic.yml | 22302 | `905e137e0d4724f9aa2a7d60aadb265e1643e73afa543a17ff4527aa883aceaf` |

执行接口见 [request157](../notes/2026-11-15-request157-complete-nine-residual-quadratic-square-interface.md)。

report 的实际 producer SHA、reader SHA、wrapper SHA、request SHA 均与上述冻结字节相同。原 consumed closure 记 41 源，canonical SHA `d150b2a732792ce330419f6f132d965a0c7c609dca69c6fc8657cc94a569c250`，与本次 request 中完整41源表的 canonical 身份一致；这个比对是已读原报告中的身份对照，不宣称所有运行期数组重新导出独审。

四个原输入的已报告 SHA 与 request 一致：

| 角色 | SHA256 |
| --- | --- |
| accepted | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail_anchor | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail_config | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

actual154 与 actual157 全字面数组 descriptor 的逐项比较尚需未取回的 `literal_model_binding`，本文不以“旧源码未改”冒充已经独核每个新实例数组。

## 9. 对驻点、秩和下一路线能够严格说到哪里

### 9.1 有限候选空池不等价于驻点

真实 search 源先形成并保存 `original_formed_relative_gradient=A^T F`。每个已实际有限评价的点只有同时满足“在半径球内、原点形成斜率严格负、完整模型 merit 严格下降”，才进入全局有限池。方向 3–6 的池为 0，只说明这些已访问点没有同时通过这些条件；不说明所有球内点不存在下降。

同一源把全部 $A$、原完整 J/H、全9梯度、每更新谱/shift/QR 及候选记录写入 status。现在这些字段只知道其输出合同和描述器，未取得数值。不能把已读的约 $10^{-37}$ 或 $10^{-54}$ 单方向 slope 说成全9梯度范数，也不能推断最小奇异值、正定 Hessian、严格驻点或精确秩亏。

### 9.2 精确实条件下的必要关系

只对同一字面表达的光滑准确实延拓，令 $W(p)=\frac12\|F(p)\|_2^2$，则

$$
\nabla W=J^T F.
$$

若 $J\in\mathbb R^{3\times9}$ 行满秩，$JJ^T$ 可逆，故 $J^TF=0$ 必须推出 $F=0$。所以，**非零残差的准确无约束驻点必伴随 $\operatorname{rank}J<3$**。反向不成立：秩小于3并不自动令 $J^TF=0$，也不证明不存在别处的根。

满行秩情形还有条件不等式

$$
\|J^TF\|_2\ge\sigma_{\min}(J)\|F\|_2.
$$

一个有限小梯度、一个有限小奇异值或几个方向性小点积都不是上述准确前提的证明。当前 Decimal50 forward/Hessian 不是区间外包；原 binary64 表也不是精确连续模型。若没有对真 $F,J$ 及其误差的控制，就不能由打印字面替代准确 rank 判断。

可逆换参 $p=p_0+Tz$ 给 $J_z=JT$，从而准确秩不变。新 QR 基底可以改善有限形成误差，但不能把准确秩亏“换基修复”。若真驻点处 $J^TF=0$，准确方向导数对所有方向均为零；在准确算术的原严格 slope 条件下，非零直线方向不能通过该条件。有限程序可能打印极小的负值，但这不是准确非驻点的证明。因此即便存在负曲率模型逃逸，也不能悄悄放宽原接受规则来把它记为已接受。改变初猜、增加真实新控制或另设明确的求解路径，都必须具有独立身份和原接受责任。

这里没有断言 actual157 已满足这些准确条件；这些是解释下一选择必须区分的代数事实。

### 9.3 有证据的后继边界

本轮首步已经显示：完整残差二次平方模型可以在实际所选微小方向上给出准确的下降预测。随后连续极末位下降、四次完整原 normal 拒绝和半径 quarter，均不支持直接机械追加相同8方向批次作为实质改进。

下一数学选择应据已经生成的完整 $J^TF$、三行响应、原 Hessian/负曲率与内部候选记录，分清有限形成误差、有限模型搜索未找到远处下降，以及同一九族的局部非零残差驻点这几个不同情形。读取既有记录只补证据，不是新的科学验收门；也不能因读取暂时受限就假填这些数值。若现有记录最终支持近驻点或秩退化，具有意义的独立后继应处理该数学机制：例如实际新增独立函数方向并完整重形成响应，或明确选择另一个不继承当前接受的初猜；不能仅继续缩小半径、只替换坐标名称或将浮点最低模型点称为全局最优。

任何后继仍保原三残差、原域、原 strict slope/Armijo 和完整最终检查；未有数据支持前不指定唯一原因，也不预称某个方案会收敛。

## 10. 真实规则同步、清理和未付项

report 保存了一次真实规则同步：`actual_read_utc="2026-11-15 15:20:56 UTC"`，`completed_utc="2026-11-15 15:20:57 UTC"`，原 main read `22889e90bc66c833bac107fb562f254c7cb63758`；普通 push 成功，发布规则记录 commit `f6e7bcc3d9329e16cff769cc498ac552b2636f90`。双 README blob：

- 根：`21bd547f56590b7f2dd279d0297efb289a9b2783`。
- 题：`bff8aea253a9e6a7a4fac28d810ac454c5499fec`。

原 runner 从 `15:20:57 UTC` 至 `15:31:02 UTC`，`README_change=null`、`periodic_sync_failures=[]`、`science_terminated_for_actual_rule_change=false`、`scientific_checkout_modified=false`。运行未跨45分钟周期，不能写成执行了多次中途 pull。原 argv/预算保持，runner 返回0。

metadata 明确 owned temporary cleanup 步骤 success；chain 为 `raw_payload_retention=false`。本文不提交51.8MB可再算 status 或日志数据到 main、Release 或新 artifact，仅保存本正式结论、已公布脚本/配方/run 与原输出身份。未取得的完整 compute 段、具体末方程/FD/Arb/circle 细项及全部内部模型矩阵均仍待原日志读取，不以报告摘要代替；非零112全场、native/finalJ/audit、连续误差及几何闭合责任继续未付。
