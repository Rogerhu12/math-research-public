# 九控制H(s)完整112场的独立进程外壳与原字段读回

作者：ChatGPT（amplitude 子任务）。日期：2026-11-15。

**类型：源码接口／未执行。** 本项只接已冻结九H适配器的真实身份，没有选定九参数、lambda、来源末点、request或run。没有运行native、科学模块、进程外壳或reader，也不把旧六控制124或任意失败记录改名成九控制成功。

## 1. 冻结文件与来源

主适配器及其数学／生命周期接口见[九控制同worker高度路径接口](2026-11-15-nine-control-same-worker-height-path-full112-interface.md)。新增两份独立小源为：

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| root_20261115_nine_control_height_path_run.py | 9687 | d075af46b0dc57aafa4b484eee292e309fcd83adcd95e7c0a30a2a534e770d5e |
| root_20261115_nine_control_height_path_scalar_readout.py | 26840 | c756ede79cba7a4490f97801e8afe31e51e373a5e0946df89c7ab0f489ec2427 |

外壳直接基线是 `root_20261115_six_control_height_path_run.py`，9677B／`0836ed339974d5f21cdbd110f1a78ba5fb9232f5ee4f22c74849b2ee16d133dc`；reader基线是 `root_20261115_six_control_height_path_scalar_readout.py`，26540B／`4a0ab4a7ad8fbd62dd5fced0f15431498934d000af2681e137dc237b8ebaf5be`。旧文件完全不动。

两份完整差异分别为 `root_20261115_nine_control_height_path_run.py.diff`，3343B／`b9e4fd60b49794304f3e926b42cff78a65b1c306cd011fffa973384fccb4e142`；`root_20261115_nine_control_height_path_scalar_readout.py.diff`，5457B／`d8d4a4bde54926a7f862cc2d49b28e12b30393674b6218add5926af3f9f7a1cb`。本地只解析源AST／文本／SHA，未执行任何fixture。

## 2. 外壳只替换入口身份

新外壳固定运行：

```text
geometry_20261115_nine_control_height_continuation_full112.py
SHA 0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924
```

原true client仍为 `exact_20261114_true_tail_client.py`，SHA `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`。原helper e830由适配器绑定；它的事件名带request124仍然表示其冻结源码，未改成未来请求编号。

新请求schema为 `public-nine-control-height-path-request-v1`；新进程状态schema为 `nine-control-height-path-full112-process-wrapper-v1`。外壳新事件是 `nine_control_height_path_full112_launch` 和 `nine_control_height_path_full112_process_returned`。除这些字面身份、入口pin和说明文字外，原argv形成、输入SHA、进程组、TERM／KILL、预算／deadline、stdout复制及finally原样保留。`digest`、`write`、`stop_group` AST完全不变；main内未改数学参数或算法分支。

命令行合同保持：

```text
python root_20261115_nine_control_height_path_run.py
  --request <未来真实请求文件>
  --recipe <未来真实九控制正lambda配方>
  --inputs-directory <本请求临时四输入目录>
  --source-topic <临时恢复的原来源课题目录>
  --out <RUNNER_TEMP下不存在的本请求独立目录>
```

请求实际必须提供：

- `schema`，取上述新schema；
- `parameter_recipe.sha256`，与实际recipe全部字节相同；
- `inputs.accepted/prepared/tail_anchor/tail_config`，每项含 `runtime_basename/bytes/sha256`；
- `execution.jac_workers/max_nodes/material_angles/physical_angles/node_heap/outer_iterations/scientific_wall_clock_seconds`；
- 供reader记录的 `source_sha256`，及原门字段 `original_inner_trial_count/original_native_max_iterations/original_native_trial_count/collocation_tolerance/boundary_tolerance/native_tolerance/boundary_FD_tolerance`。

未来接线须把真正的来源末点与原输出身份写入recipe，可放在 `initial_parameter_origin` 供reader明确选取；它只是原始出处元数据，不是补造父J／merit／checkpoint。recipe自身仍需满足0433原完整合同，包括全部九参数、原四输入SHA、显式正lambda和完整e830 policy。

这份与124对应的薄外壳目前转发的是四原输入和新recipe，没有新增 `--continuation` 文件转发。它适用于首次真实 `fresh-circle-low-three-linear` 实验。适配器自身保留own-schema完整场continuation合同；未来若使用该分支，必须显式接入真实完整文件与SHA，不能只改recipe而假称外壳已传入一个未提供的文件。

## 3. 总预算、真实规则监控与临时树

外壳在启动子进程前，以同一进程的 `time.monotonic()` 和请求中显式预算建立 `VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC`。原helper用此截止检查请求间剩余时间；外壳同时监控整个子进程，覆盖单个native请求内、实际H FD和后续fullDN。未来请求应把所声明的科学预算与helper policy的18000秒口径明确一致；外壳沿原124只验证预算为显式正整数，不暗加一个新的数值阈值比较门。

科学子进程保留原独立进程组；外层规则runner的TERM由本wrapper转发到该组，涵盖native Node后代。到期／外部中断分别保留 `wall-clock-budget-partial`／`external-interruption-partial`，不伪写数学拒绝或accepted。需要KILL时仍沿原8秒等待责任。stdout／stderr边读边写临时日志并原样传到Actions日志；错误标志写入 `stdout_copy_errors`。

原四输入字节和两个ready环境槽必须在启动前真实恢复。科学output和factors分别位于本请求 `out/science`／`out/factors`，不预先创建适配器要求空的新子目录。wrapper自己保留 `process-status.json` 与科学日志的实际SHA。所有运行数据只在RUNNER_TEMP；readback及必要终态标量／SHA进入日志后，未来workflow才清理该请求自己的可重生树，不删其他运行或只读原来源。

2700秒真实pull／README检查仍是未来workflow外层原规则runner责任。两份新源没有新增Git、网络、上传、数据归档或dispatch操作。

## 4. 九控制原字段reader

新reader schema为：

```text
nine-control-height-path-full112-existing-scalar-readout-v1
```

CLI保持原格式：

```text
python root_20261115_nine_control_height_path_scalar_readout.py
  --directory <外壳out>
  --request <同一真实请求>
  --recipe <同一真实九控制配方>
  --rules-directory <原规则runner输出目录>
  --compute-outcome <实际Actions步骤状态>
```

reader仅JSON／日志读取、原字段摘取和字节SHA，不导入科学模块、重算域、norm、J、FD或响应。它保留原全部bootstrap请求表、原请求证据和warm/predictor事件；原native记录、trace／trial；实际H FD；fullDN状态／原内层评价；已有banded残差报告；原规则记录。没有完成的阶段保持缺失，不用上一轮FD或旧zero-HJ填补。

与六reader的身份差异只有：新schema／事件／BEGIN-END标签；recipe的 `initial_six_parameters` 改为 `initial_nine_parameters`，来源文字改为可选 `initial_parameter_origin`；原Newton stdout selector识别新0433 adapter事件，仍识别原e830 `request124_height_path_finished`。

为使真正接受产物的身份可供后继450消费者核对，新reader还原样摘取已存在的 `accepted_result.schema/source_sha256/field_representation/finite_boundary_scheme/complete_nine_scalar_parameters`，并对原 `nine_control_full112_implementation` 整对象记录canonical JSON身份。这个读回不产生accepted标志，也不要求科学流程为reader额外计算任何内容。

外壳代码会返回真实科学子进程状态，reader本身则沿原设计在普通读回错误时保存失败对象并返回0。故report步骤success从来不能代替原process／adapter／fullDN科学成功。未来workflow应分别保留这两个实际状态。

## 5. 90KB协议及不能混淆的完整性

正常原输出由以下标记包围：

```text
BEGIN_NINE_CONTROL_HEIGHT_PATH_SCALAR_SUMMARY
<一份compact JSON，不含人为补齐的缺失阶段>
END_NINE_CONTROL_HEIGHT_PATH_SCALAR_SUMMARY
```

身份事件为 `nine_height_path_scalar_summary_identity`；SHA范围是compact UTF-8 JSON本身，不含分隔换行。GITHUB_OUTPUT仍为 `scalar_summary`、`scalar_summary_bytes`、`scalar_summary_sha256`。

源沿原124保留90000B上限与显式缩减顺序。过大时先输出各section字节数；保全部bootstrap primary行，细节改为计数／SHA并将 `summary_complete=false`，不会默删后仍声称complete。若继续过大，按照原次序压缩具名sections，最终给小失败对象。该过程不新增科学门，也不把传输缺口算成native失败。

完整bootstrap请求事件仍由未改的e830 helper在compute时原样打印；reader减小report不能使已保留compute事实改名为“独立全文原数组核验”。完整factor未由reader读取时不声称factor审计；已有文件身份只覆盖实际列明的JSON／日志。对于原fullDN日志中未打印的临时raw，摘要只保其来源和hash，不能声称已永久保存。

## 6. 未来真正accepted九H产物与450父合同

0433的原writer将 `prepared.json.gz`、pending、`driver-status.json`、真正的 `actual.json.gz` 绑定到

```text
schema = nine-control-height-path-three-active-nonzero112-complete-physical-DN-v1
source_sha256 = 0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924
```

顶层 `nine_control_full112_implementation` 保留原input／recipe／全部source闭包／九参数／固定六shape／三active／453行列责任；新增 `original_00e4_adapter_baseline_sha256`、e830 helper SHA及POLICY、同owner职责，只有endpoint真实完成才加入 `completed_height_path_status` 原receipt。原fullDN核心生成的最终response／audit字段不改，只有它实际接受才由adapter声明success。

真正actual还保 `complete_scalar_profile` 的新九族schema、完整冻结九参数，`original_metric_identity.schema=nine-control-material-metric-v1`，原物理cut审计及最终native责任。后继same-g450应显式接受这个新producer及其真实source/binding，不能把字段改回00e4身份去绕旧硬锁。本文未声称当前已经存在这样的accepted文件。

以上三源及两接口可先公开作为无请求的可执行准备。任何未来run仍要单独选择实际九参数、正lambda、预算及来源，执行原完整门；不从本接口、流程exit0或H路径中间收敛推断最终闭曲面完成。
