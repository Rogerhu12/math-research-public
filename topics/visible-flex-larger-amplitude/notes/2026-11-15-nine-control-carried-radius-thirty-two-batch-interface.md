# Request135：九控制真实末半径续接，最多32个完整八方向批次

作者：OpenAI ChatGPT（amplitude agent）；日期：2026-11-15。本文是独立算法源码与公开 Actions 接线合同。尚无 Request135 的运行编号、计算结果、已接受非零场或成功声明。

## 1. 本次明确改变与证据

[实际134完整结论](../results/R296-actual134-thirty-two-nine-control-batches.md)记录了32个完整批次、256个接受方向和2322个原外层试探。每个旧批次都把相对信赖半径重新置为0.1；真实第32批末半径为0.000390625。新入口把这一原算法状态和同一原末点一起作为首批输入，此后逐批携带真实 `final_relative_trust_radius`。不重新设置为0.1，不作下限、夹取或修复。

原半径更新规则、完整八方向循环、每方向20档原外回溯、每个法向校正的12次迭代和20档内回溯全部保留。每批仍付完整初末九列参数 FD、新标量 Arb 域、453维圆检查及所有原最终判据。内层 `normal_target_tolerance_met=false` 仍不是外层接受门。原三方程的未加权 merit、实际斜率和0.2 Armijo 不变。

这是独立的 carried-radius 算法，使用新源码、新 schema 和新来源闭包。它改变跨批初始化，不能冒称旧824c的运行，也不能把32个独立子进程称为一个连续256方向求解器。数学上的重置成本及有限精度范围见[半径重置与理想模型下降分析](../results/R295-nine-control-radius-reset-and-ideal-model-descent.md)。该分析不保证携带半径就会克服实际134的弱响应或非线性曲率。

此前失联临时环境中的未发布135草稿不是本次源码。本文列出的三源是从已公开824c/f57/fd5全文重新生成的独立版本；不沿用旧草稿 SHA。

## 2. 最终文件与身份

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_small_core_nine_control_carried_radius_recipe.py` | 56710 | `ed78684f93c76cf1695a3a54f04d28528b5505fccf115b6fd6afddc7a657cd50` |
| `root_20261115_small_core_nine_control_carried_radius_scalar_readout.py` | 31218 | `24c5ff04203965bf49ab3a559eaaaa5b90ecccd16a58cc87eb148676cf885cd2` |
| `geometry_20261115_nine_control_carried_radius_temporary_batches.py` | 53016 | `df856e9ecf9d9bbd52c7c515d75aed0a50efbfd0f54126ec9dd07eed48521209` |
| `actual134-final-batch-nine-control-carried-radius-recipe.json` | 2407 | `494f73d108669feb547e26dabef6c71ef589cfae149611163453a86b98c45151` |
| `public-nine-control-carried-radius-request.json` | 46066 | `a68b9556148dcab3cf03e9a1ced32f31560ed2a7c149ac9bf2569d71347ca376` |
| `visible-larger-public-nine-control-carried-radius.yml` | 20027 | `06ef869693dddcf26819a691a975c2dca767a1ecab054daf8c081d0899e35996` |

前三源、recipe、request 位于本课题 `computations/`；workflow 位于仓库 `.github/workflows/`。接口本身不参与科学来源的循环自引用。

独立 push trigger 只认 `topics/visible-flex-larger-amplitude/computations/public-nine-control-carried-radius-request.json`。旧134 workflow、request、三个冻结基线源均不修改，不并行触发旧请求。

## 3. 真实首父与短配方

首父是原 run `43704292938`、source commit `19911f56968ad3581636e77d240c4d5e9064645f` 的第32批。原 compute job 为 `132781953477`，report job 为 `132785749291`。

| 原记录 | 字节数 | SHA256 |
|---|---:|---|
| 第32批完整 status | 6525034 | `14308777d3f7440e6aa3a1054022800a0800b73c6e51ab6123bc350b92bcba24` |
| 第32批 primary | 62594 | `7f732c5d4980b1a273682f56ca19de74721797101dbff36a5c5be795eef21fb5` |
| 第32批完整标量 view | 202798 | `cf4b67c4d4b1c147dadd531836cefd939d49aa698314dba3b084ed64b01e81ca` |
| 原32批 chain | 61799 | `4209a386f332be26a70c2bf91cfcff158ba4610e219b92067e0400de0702b422` |

短配方的九个参数直接取原 `final.parameters`，顺序不变：

```json
[0.3055203761844937,0.21645138982853507,0.3426956535903166,
 -0.06322286579803658,-0.017473800295252997,0.9376133742168962,
 1.075134071398223,0.6887022298418047,0.9385918098098012]
```

算法状态直接取原 `final_relative_trust_radius=0.000390625`。新 recipe 的 `algorithm_state` 仅包含 `relative_trust_radius`；它不是第十个标量控制。来源同时保留 `parameter_field=final.parameters` 和 `radius_field=final_relative_trust_radius`。

首配方是2407字节的参数和半径配方，不能称为旧1838字节、仅参数的 after-batch-032 配方原件。原 status、完整 view 与大数组不重新下载或入库；这里消费已经由原日志重建核对的字面参数、半径及来源元数据。新子程序重新评价，重新形成 J、merit、FD 和域证据，绝不复用原父 J、merit、模型数组或 FD。

实际134的 unit/full112/nonzero/native/success 判据均未通过；首配方没有已接受非零场的意义。

## 4. Producer：保完整数值主体，仅独立初始化与来源

新 producer 是公开824c文件的完整独立副本。下列六个数值函数正文逐字保留：

`norm`、`full3_trust_direction`、`next_radius`、`full_column_qr_solve`、`curve_frame`、`curved_candidate`。

整个 `for iteration in range(args.candidate_steps)` 方向循环，以及 `original-final-diagnostics` 起的完整 final、except、finally 尾部，也逐字保留。完整文本差异说明每一个替换，未创建数值 fixture。

当前 finite 公式保持完整3×9响应、12×9正则 QR、9×2法向和9×7切向。所有九个控制都保留；没有正规方程、奇值截断或新的最小奇值门。相对坐标仍是 `d=S z, S_j=max(1,abs(p_j))`，最大半径仍为1。法向校正不保证实际完整参数改变量落在预测方向的信赖球内，这一原范围未改变。

新增 `--initial-relative-radius` 是必填字面算法状态。它必须与当前 recipe 的半径具有同一 binary64 word。合法输入范围为有限 `0<=radius<=1`，不把真实零半径修复为正值；若原方向函数随后因零半径而停止，保留原停止责任。此输入身份约束不是新的非线性接受条件。

新 recipe schema 为：

```
R259-explicit-nine-control-parameters-and-radius-recipe-v1
```

顶层六个字段严格为 `schema, origin, literal_parameters, algorithm_state, input_sha256, family`。九参数必须有限、顺序完整；来源接受已冻结的旧九 producer 或本新 producer，不能把旧六维来源重标为九维，也不能把来源缺失补成未来成功。

新 status schema 和文件名为：

```
R259-nine-control-full-three-two-normal-carried-radius-trust-recipe-v1
nine-control-carried-radius-status.json
```

原字段增加明确的算法说明：`incoming_actual_final_radius`、`carry_original_final_relative_trust_radius=true`、`radius_reset_at_child_start=false`、`original_eight_direction_numeric_loop_unchanged=true`。完整实际 final 半径仍从原循环真实变量写出；没有另用最后一次接受记录推算半径。

## 5. 来源闭包与旧基线职责

原134的85个源码 pin 全部保留；只增加新 producer 和新 wrapper，共87个 `source_sha256`。原两个 workflow support pin 全部保留，再增加新 reader，共3个。科学 family 的冻结 SHA 仍是 `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629`。

首父原 producer 闭包为26源；当前 producer 闭包为27源，即这26源加本新 producer。首次来源仍明确是824c；后续来源是实际新 status 的本新 producer，使用完整27源身份。原26源无一被移除或修改。

旧824c、旧f57 reader、旧fd5 reset32 wrapper，以及更早b15八批 wrapper 仅按声明保留来源或 hash 基线。新 wrapper 实际执行新 producer 和新 reader；旧 wrapper 的 main 不执行。旧824c作为完整数值文本的来源被 hash，但其 main 不运行。原117/119/121等历史来源保留历史意义，不冒称这次重新计算了它们。

每批仍允许原 zero-added-quadratic 反事实读回。当前真实三个 eta 非零，不能把该反事实改称当前点 eta 为零；反事实异常仍按原 setup 异常处理，不增加新接受门，也不增加旧六维 J 比对调用。

## 6. 每批生命周期与完整半径继承

wrapper 不导入科学模型。它只执行固定子进程、读取完整 JSON、核来源与输出字节、生成下一短配方并负责临时文件生命周期。

首批读取上述真实134配方。每批开始前用配方原九参数及原半径构造 CLI；新的 J、预测器、法向框架和所有诊断均由新子进程按原算法重建。半径从 `algorithm_state` 来，不从固定 OPTIONS 猜测或旧 request 的0.1默认值来。

子进程结束后依次付清：

1. 完整 status 的实际文件大小、SHA、schema、当前27源闭包、原四输入和入参/入半径身份。
2. 分段 reader 的完整 stdout、primary 和全部具名组，保留完整原 trial rows。
3. status 和 reader 的真实末九参数、真实末半径一致性；若字段被原 reader 搬到完整具名段，则按其原 moved-field 合同核对，不能因搬段而丢弃算法状态。
4. 从完整实际 status 生成下一 recipe，保留本次 run/source、status 和 primary 字节身份，并携带实际 `final.parameters` 与 `final_relative_trust_radius`。
5. 输出 batch 外框、完整原 reader stdout 和紧凑行后，才清理该批自己拥有且已消费的可重算 raw。

特别地，若第8方向全部20档拒绝，原循环会把半径 quarter。下一配方取 final 状态中的这个 quarter 后值，而非最后接受点的半径。参数仍是最后真实接受点；没有采用被拒绝的候选。零半径不加下限、不回退0.1。

每批重新初始化除了半径和九参数之外的工作状态，仍执行原初末 FD/Arb/circle。即使数值助手相同，这也不宣称与一个无进程边界的256方向程序逐位等价；新的 setup、初始描述和反事实读回仍实际执行。

## 7. 继续或停止：保留 fd5 原决策正文

`original_stop` 正文逐字保持原fd5。信号/规则资源中断、子进程非零退出、诊断未完成、原异常、reader 不完整，都如实停止。原 unit stopping flag 或原 full112 candidate flag 为真时停止并报告其实际范围。

原 accepted-point count 为零时保持旧 wrapper 的停止行为；不新增“强制继续到改善”的循环。只有完整诊断、完整 reader、原停止字符串为八方向预算用尽且实际方向数为8、至少一个原接受点、最终旗标仍需继续时，才进入下一批。

这一旧决策没有添加 inner-target、FD最小误差、奇值、秩、每批下降量或新的 native 门。若某批没有接受点但 final 半径已 quarter，仍完整保留该实际 final 半径和停止原因；不会伪造下一批已执行。

最多32批；3600秒只在两个完整批次之间检查，不能中途截断一个子程序再称完成。达到明确批数或批间时间预算时记录实际 stop；未运行后缀逐行保留 null，不假装被科学拒绝。

## 8. 紧凑而完整的读回与90KB责任

reader保留f57的原字段选择、逐方向 trial 列和具名分段机制，仅换实际 producer/schema/status身份并增加上述半径原字段。新主 schema 为：

```
nine-control-carried-radius-full3-curved-trust-segmented-scalar-readback-no-raw-retention-v1
```

完整 view schema 为 `nine-control-carried-radius-full3-curved-trust-scalar-view-v1`；方向段 schema 为 `nine-control-carried-radius-complete-direction-scalar-segment-v1`。每份输出的 UTF-8 原 JSON 字节和 SHA 都有责任。stdout prefix 为 `VISIBLE_NINE_CARRIED_RADIUS_`；workflow 不能只保存其 hash 而丢掉原段正文。

每批 primary 与所有方向段直接进入 compute 原日志，并有批次外框。report job只接紧凑 chain，不把32份 primary 合并成巨型 GITHUB_OUTPUT。chain 保留32行、所有真实失败文本、状态、原预算、初末参数/半径、原旗标和未运行后缀。

90000字节仍是硬上限。超限时保留原计数和显式 incomplete/overflow 责任，诚实退出；不删字段、截失败文本、丢后缀或把部分 chain 标成 complete。科学结果和运输失败分开，不能由 cleanup 成功推科学成功。

## 9. Actions 实际接线和资源范围

workflow 使用原 Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0，单线程环境不变。公开 Actions 才执行科学。workflow 在执行前实际核87+3文件 SHA，并仅做 Python AST/compile 检查，不执行模型 fixture。

四个原数学输入仍从公开历史 commit `8bd267107cc8710d371f3b62c02986655ac965b0` 临时恢复，核原字节长度和 SHA；原78公共源码恢复一次。所有可重算输入、子状态、数组、source cache 都只在 RUNNER_TEMP。没有新 artifact/Release 上传或 raw 提交。

独立 compute job 为90分钟、科学 step75分钟；report job10分钟。3600秒链预算仅批间检查，Actions 墙钟仍可能把正在执行的原子批截断；这种情况按资源 partial 记录，不解释为全回溯失败或无根。

规则 runner 仍是原 `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`，2700秒真实 pull/rebase、两份 README 差异处理和规则变更停止责任不改。仅把其 metadata BASELINES 显式绑定本次实际读过的 README：
root `74c08a36f6c997d0bc1e64a7956b42276f5fa5d7`，topic `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。保留 HANDOFF 唯一真实规则同步行和10KB界限；`merge.stat=false` 仅避免已删除大数据的 diffstat 读取，不改科学。

清理限于本请求拥有的 RUNNER_TEMP 子树；拒绝跟随 symlink，检查属主，并只在需要时给自己拥有的只读文件添加写权限。always-chain report 在最终清理之前执行。没有 SDK 上传、远程删除或存储实验。

## 10. 交付核对范围和未付责任

本次 fallback 仅做完整源文本替换、纯 JSON 字段/来源选择、完整 diff 和 SHA。六个数值助手、完整方向循环、final/except/finally 及 wrapper 原停止函数均进行了文本相同性核对；完整 diff 从旧、新文本逐行重构验证。没有本地 Python 导入、科学计算、数值 fixture、FD 或新矩阵动作。终端不可用期间没有假称执行本地 AST；正式 workflow 会对实际源码执行静态语法检查。

源/recipe/request/workflow 都是小于100KB的独立文本，以 Git blob 暂存给主控；本 agent 未更新 ref、未创建本请求的运行、未操作 Git 分支。主控统一实际发布。

新计算是否获得更大下降、响应是否可靠、最终低三/full112是否通过，都只能由真实135记录回答。携带半径既不是精确秩证明，也不是已接受非零场的替代。当前三方程残差、全部112右端责任、完整圆/域检查和 native 未调用的范围继续如实保留。
