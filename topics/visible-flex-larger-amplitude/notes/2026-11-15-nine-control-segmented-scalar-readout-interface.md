# 九控制量原方向读回：完整分段日志与有界主摘要

作者：geometry；日期：2026-11-15；分类：工程读回接口，非新的科学验收条件。

状态：源码已冻结，只做源码、AST、字节与哈希检查。未调用 reader、模型、求解器、参数差分或任何数学计算。本接口没有实际九控制量运行结果，不填运行号、接受结论或证书。原六控制量读回器保持原字节。

## 1. 实际需要修补的范围

原六控制量 reader 把所有外方向及其 trial 行拼进一份不超过 90000 字节的 JSON。实际121第五批的科学 child 已正常完成；原 reader 的 compact 视图仍为93000字节，转成 metadata-over-budget schema，随后批次编排按协议停止。该事件不表示原数学接受门失败。父编排已经读全第五批 status、来源闭包与 trace，并完成临时 raw 清理；新的 reader 不声称能恢复已经没有进入原日志的第五批完整 trial 行和 Arb/circle 细项。

本次针对未来九控制量运行修改读回协议：全部实际外方向各自完整输出；主摘要只保存原主要字段、方向组身份和重建索引。若某一方向、原字段或字符串超过一块容量，则完整结构分段，不删 trial、不减少方向、不改精度、不截科学异常字符串。传输失败单列，不改求解返回或科学标志。

## 2. 冻结来源

| 角色 | 文件 | 字节 | SHA256 |
|---|---|---:|---|
| 新 reader | `root_20261115_small_core_nine_control_curved_scalar_readout.py` | 30892 | `f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d` |
| 原 reader，仅比较 | `root_20261115_small_core_six_control_curved_scalar_readout.py` | 以原文件为准 | `3e2c0515ee9759162e3736915674c86ca9a56441f2a7561df9dc09d37fea4d45` |
| 九 family，原样读取来源 | `geometry_20261115_small_core_nine_control_family.py` | 44390 | `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629` |
| 九 search，原样读取来源 | `geometry_20261115_small_core_nine_control_curved_recipe.py` | 54884 | `824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf` |

建议目标路径为题目 `computations/` 下同 basename。本地交付目录为 `/tmp/visible-small-core-nine-reader/`；完整旧到新差异为 reader basename 加 `.diff`。source-only 检查文件 `nine-control-segmented-reader-source-only-check.json` 为3543字节、SHA256 `d70b0d2dd712b1ea64d13a06998a40252a592e35b1a7b7aee9165b8fc959cfbe`。

reader 读取 status 中真实 `source_sha256`、全部 `consumed_source_sha256`、`source_roles`、四数学输入及 parameter recipe 来源。两个新源码的预期 SHA 与记录值逐项列出，比较只表示来源身份，不作为候选接受条件。完整来源检查仍由实际科学入口与 workflow 已有 pin 承担；本 reader 不导入任何模型。

## 3. CLI 与实际文件

CLI 与原 reader 相同：

```bash
python computations/root_20261115_small_core_nine_control_curved_scalar_readout.py \
  --directory "$NINE_OUTPUT" \
  --rules-directory "$RULE_OUTPUT" \
  --compute-outcome "${COMPUTE_OUTCOME}"
```

`--rules-directory` 可省略。`--directory` 是本次实际九参数 search 输出目录，其中主状态文件必须为 `nine-control-curved-status.json`，schema 为 `R259-nine-control-full-three-two-normal-curved-trust-recipe-v1`。所有 source/run/recipe/参数、接受结果和哈希都取该次原件与实际环境；不从121父状态复制新 J、W、完整场、FD 或证书。

执行 reader 时必须保留其 stdout 在原 Actions 日志中。不得把 stdout 重定向到将删除的临时文件后只保文件 SHA，也不得由报告步骤把所有方向 JSON 重新拼成一个主摘要。科学子进程本身的 stdout 可以继续按现有 workflow 临时记录，但 reader 的分段 stdout 是独立读回载体。

读回步骤放在科学步骤之后，以已有 `always()` 语义记录真实完成、异常或资源中断。临时科学 raw 的删除必须在 reader 返回之后。该 reader 不上传 raw，不写 Release，不改参数或运行预算。

## 4. 正常 primary 与 GITHUB_OUTPUT

三个输出键保持不变：

```text
scalar_summary
scalar_summary_bytes
scalar_summary_sha256
```

`scalar_summary` 是一份 compact、ASCII 转义、键排序、无 NaN 的 JSON，其 UTF-8 字节数不超过90000。字节数与 SHA 的范围均为 JSON 本身，不含分隔 LF 或 GITHUB_OUTPUT 的多行 delimiter。

正常 schema：

```text
original-nine-control-full3-curved-trust-segmented-scalar-readback-no-raw-retention-v1
```

原 prepared scalar view 的 schema 为 `original-nine-control-full3-curved-trust-scalar-view-v1`。primary 的 `segmented_readout.original_view` 保存该完整 view 的 canonical JSON 字节数及 SHA；该 view 不需要再拼进日志。主要字段正常保持 inline：

- 原 status 完整 bytes/SHA、实际 run/source、完整 producer/source/input/recipe 来源；
- 初末九参数、三项方程、完整 $3\times9$ J、原奇异值和 old-six 子列读数、九列 FD；
- 原初末 W、方向预算、所有真正接受/拒绝计数、停止原因与全部最终布尔标志；
- 完整原 scalar-domain 与 circle-check 对象、原调用 trace 摘要和文件哈希清单；
- 零新增二次控制量对照的原标志与原 comparison-array table 的身份。

若这些字段自身过大，reader 将一个完整命名字段移到分段组，primary 中显式记录原字段名及该组身份。此举不是科学字段省略。所有外方向始终单独成组，primary 不包含它们的实际大 payload。

## 5. 每方向分段协议

每个实际 `searches` 元素按原顺序对应 `outer-000`、`outer-001` 等组。没有预设成功方向数、方向截断数或 trial 行上限。组保存本方向原参数、残差、J、W、半径、完整方向模型、曲线 frame、全部 trial 行、全部未校正 seed 行和原 failure examples。

每个段的 schema 为：

```text
original-nine-control-complete-direction-scalar-segment-v1
```

日志形态为：

```text
BEGIN_VISIBLE_NINE_CONTROL_OUTER_000_PART_00000
{完整的一段 JSON}
END_VISIBLE_NINE_CONTROL_OUTER_000_PART_00000
{"event":"visible-nine-control-scalar-segment-sha256",...}
```

每段 JSON 自带 group、part index、operation、精确 JSON path、reader SHA、原 status receipt、实际 run/source。每段打印前使用实际 encoder 检查长度；JSON payload 最多90000字节。BEGIN/END 分隔行及随后 receipt event 不在 payload 的 SHA 内。

随后 receipt event 的 `part` 是完整段描述器：index、bytes、SHA、BEGIN/END、operation、path，以及操作需要的区间或容器长度。primary 中每组保存完整原组的 canonical bytes/SHA、part count，以及按顺序排列的所有 `part` 描述器列表的 canonical bytes/SHA。完整列表可从该组 stdout receipt events 原样读得；不把所有列表或 payload 再复制进 primary。这让 primary 大小与实际 trial payload 分开。

## 6. 完整结构分段与重建

能放入一段的 JSON 值用 `value` 原样存储。否则按下表保持其完整结构：

| operation | 声明或内容 | 重建责任 |
|---|---|---|
| `value` | 某 path 的完整 value | 直接设置该值 |
| `begin_object` | 原对象 entry_count | 创建对象，后续按所有原 key 填满 |
| `begin_list` | 原列表 length | 创建该长度的列表，不省元素 |
| `list_items` | start、stop、完整 items | 按原半开索引区间放回全部元素 |
| `begin_string` | 原 codepoint_length、UTF-8 bytes/SHA | 创建原长度字符串序列 |
| `string_slice` | start、stop、完整 text | 按 Unicode codepoint 索引原样拼回 |

对象按原 JSON key 的排序遍历；列表保原顺序。完整单个列表项若仍过大，递归拆该项的结构。长字符串仅分成连续、无遗漏的原字符片段，不使用 repr 或截断替换原字符串。数值不做量纲转换、舍入或再计算。极端单一不可框定 path/标量失败时明确报告传输失败，不假造完整读回。

重建者应读取各组全部段，验证每段 bytes/SHA、连续 part index、声明容器和列表/字符串区间的完整唯一覆盖；再用相同 encoder 核组 canonical bytes/SHA。按 primary 的 `moved_primary_fields` 放回所有原命名字段；依原是否存在 `outer_searches` 重建完整有序方向列表；将 schema 还原为 `original_view.schema`，删除 `segmented_readout`，核完整 original view 的 canonical bytes/SHA。这是记录格式的确定性重建，非科学重算。

## 7. Trial 行保全的精确范围

原17个列名及顺序逐 AST 保持：trial、alpha、accepted、reason index、实际返回九参数、实际三方程、actual merit、原 Armijo bound、实际 constraint target/error、normal tolerance 标志、normal stop index、normal iteration record 数、evaluation/J attempts、domain/evaluation failures、original exception index。

原因、normal stop 和异常文字仍由原 reader 的完整 intern 表引用。这些表若大，也通过完整字段组分段。所有 `uncorrected_seed_readout` 行保留。每方向原 $9\times2$ normal basis、$9\times7$ tangent basis、$12\times9$ direction 模型声明与原作用/斜率都按原 JSON 读取，不由 reader 重做矩阵运算。

本读回协议继承原 reader 已声明的标量范围，并不伪装成完整 status raw 归档：全部 inner normal trial 的逐条大对象仍只由原 complete-status SHA、原计数及首末 failure examples 定位；零扩展对照的完整数组 table 也仅保原 count/bytes/SHA。该范围在 primary 中明确写出。新的传输分段没有进一步删减原 prepared view。

`log_budget_omissions_not_changed_science` 正常为空；移动到完整日志组的字段不是 omitted。没有旧 reader 在 primary 超限后删 uncorrected seed 或 direction/frame 字段的行为。

## 8. 异常与原科学责任

原状态未生成、JSON/schema 异常、科学失败、reader 自身 framing/输出失败是不同事实。reader 保存其真实异常类型和已有原 status 身份，不把任一种转换成数学拒绝。主结果的 `compute_step_outcome` 来自真实前置步骤。

传输失败 schema 为 `nine-control-segmented-readout-transport-exception-v1`；已完成段继续保留在原日志，并明确完整 scalar transport 未成立。准备视图本身失败使用独立 exception schema。成功生成异常报告也不表示科学正常完成。最后 stdout event 分别给出 transport 是否完成、是否有完整正常 scalar view，以及实际已输出组数和段数。

reader 没有重新定义接受条件：完整原三方程、原全域/FD/circle、原外8方向与20回溯、原内12乘20、原半径规则和原所有最终标志完全由冻结九 search/family 决定。九控制量扩展本身是显式新科学模型；reader 不把它称为保持同一个固定 $g$ 的六参数原模型。

## 9. 已完成的静态核与未做事项

已对原 reader、新 reader、九 family、九 search 做 AST parse；`encode`、`digest`、`pick`、`file_record`、`boolean_flags` 五个函数与原 reader 逐 AST 相同。原17个 trial columns 完全相同；新字段/schema/status 名已按实际冻结 producer 对齐。只允许标准库 imports，未加载任何科学模块。

source-only check 明确未执行 `prepare`、`SegmentEmitter`、reader main、family、search、任何 fixture 或 Actions job。不存在实际九参数成功结果，也不以本静态检查作为发起科学请求的新增门。唯一需要 workflow 保持的工程约束是：reader stdout 原样保留；primary 只传一次；raw 清理在读回之后。
