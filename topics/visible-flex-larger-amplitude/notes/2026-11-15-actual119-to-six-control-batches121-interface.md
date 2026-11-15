# Actual119 第8批六参数到 Request121 独立原批次续接

- 日期：2026-11-15。
- 范围：source-only 可执行接线；没有执行新的科学计算，没有当前121 run/source/result，没有成功或收敛预报。
- 父来源：实际119 `43693462669`，source `6fffce1f36e876f3b08a1c73198a7fde259d94d6`，第8个独立原子批次的真实 `final.parameters`。
- 数学仍由原 `geometry_20261115_small_core_six_control_curved_recipe.py` 执行。新文件只编排独立子进程和原件读回；不改变三个方程、六控制族、曲线候选、原Armijo、normal corrector或任何最终诊断。

## 1. 四个独立运行件

本组只新增以下路径，原119 wrapper、recipe、request、workflow均不改。

| 文件 | 字节数 | SHA256 | 目标 |
|---|---:|---|---|
| `geometry_20261115_six_control_temporary_batches121.py` | 31414 | `8ac33f77b3438a4417cbd6b4840428ff25706911464d7ae0a530b82501c674bd` | topic `computations/` |
| `actual119-batch008-explicit-six-control-parameter-recipe.json` | 1568 | `cb2e9c8338f8428e11d0aff49f89f8d5c0a36cae6dfa3a4eda2d131b39e5e904` | topic `computations/` |
| `public-six-control-batch121-request.json` | 47253 | `ae4d1b170d490c2fcae5084b122fc0f633a4a5ebaf5e68587d160d2ba004c055` | topic `computations/` |
| `visible-larger-public-six-control-batches121.yml` | 14809 | `8f5ea35da9d559ce930cc7635967466f757db2395698d16b5612c33a3197b240` | `.github/workflows/` |

各文件完整差异在同名 `.diff`，基线是已执行119的四件。请求的新 schema 为 `public-six-control-from-actual119-temporary-batch-request-v1`；编排输出新 schema 为 `same-six-control-original-eight-direction-from-actual119-temporary-batches-v1`。

以下三件保持原字节和实际身份：

| 角色 | 原文件 | SHA256 |
|---|---|---|
| 科学入口 | `geometry_20261115_small_core_six_control_curved_recipe.py` | `e154afe28c588ce0c2ae936d4304b67ec84e2b46c96b03e48ce4113e2401a761` |
| 六控制族 | `geometry_20261115_small_core_six_control_family.py` | `79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf` |
| 原标量reader | `root_20261115_small_core_six_control_curved_scalar_readout.py` | `3e2c0515ee9759162e3736915674c86ca9a56441f2a7561df9dc09d37fea4d45` |

原81个主source pins保持，只有独立wrapper替代119 wrapper，共82个；两个workflow支持source pins也保持。真正子科学producer的24项闭包与实际119第8批 `consumed_source_sha256` 完全相同。原rules runner仍为 `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`。

## 2. 初始参数是实际119第8批原字面值

按原 `p1,p2,p3,theta1,theta2,theta3` 顺序：

```json
[0.40855353135667855,0.2533699868941391,0.5021559985345984,-0.031251649006886886,-0.031154210452212065,0.5519994439954063]
```

已读的父summary为77,719 B，SHA `74926bcbac824e230342a109ae9ddb227c056ed9c459d00293656c94d418fffd`。其 `original_status` 记录原 `six-control-curved-status.json` 为1,977,219 B，SHA `33e7b1fd672ed3c4f4bf063232155ff006bef568c875797ff5379a21bdda3a5a`。该完整status在原119执行中被119 wrapper及原reader实际读过；本次源准备只读上述已保存summary和chain，不声称重新持有或重读那份大status。

实际chain元数据62,919 B，SHA `d687fba9470bcef7a985ad91b9ae0b25ce39176b674c4149b6c915efd7c77cab`，明确8个原读回完成，`stop_reason=explicit_independent_batch_count_completed`。其 `last_restart_recipe` 指 `recipes/after-batch-008.json`，1568 B、SHA `cb2e9c83…`。本次按原119 `encode` 的 `ensure_ascii=True, sort_keys=True, separators=(',',':'), allow_nan=False`、无附加LF编码重建五字段参数recipe，实际逐字哈希与该记录一致。六参数的binary64 words也分别与summary、last accepted、chain以及新请求一致。

recipe恰有 `schema/origin/literal_parameters/input_sha256/family` 五项。`origin`仍是原六控制producer `e154…` 的实际run/source、原status与原summary字节/SHA、`parameter_field=final.parameters`。初始child只读该参数recipe；`first_origin_status_payload_read_in_this_run=False`，不把1568字节recipe冒作大status，不复用父J、W、state、FD、域判定或证书作为fresh值。

原四到六控制引入记录保存在 `first_introduction_history`，其中原117的recipe和更早116来源逐字JSON值保留。119的请求、117参数recipe与chain身份另列 `intervening_batch_history`。本次仍是同六维族和恒等参数顺序，没有新增控制或列映射。

## 3. 正常原reader省略记录的正确范围

新wrapper的常量仍逐字为：

```python
READER_SCHEMA = 'request117-original-six-control-full3-curved-trust-scalar-readback-no-raw-retention-v1'
```

每批stdout标记是 `BEGIN_VISIBLE121_BATCH_001_ORIGINAL117_SUMMARY` / 对应END，批号依实际1至8递增。后半 `ORIGINAL117_SUMMARY`、原reader schema与原reader本体均未改。

已读的实际119第8批是正常原schema，带 `log_budget_omission_columns=["field","bytes","sha256"]` 及11项 `log_budget_omissions_not_changed_science`：`output_hashes`、`original_top_and_final_boolean_flags`、iteration0–7的`uncorrected-seeds`，以及iteration1的`normal-failure-examples`。每项原bytes/SHA完整保存在新请求的 `original119_batch008_summary_provenance`；原 `omitted_fields_enclosed_by_original_status_hash` 也原样保留。省略的是这些列出的派生/重复内容，原reader正常schema和全部trial行仍在；这不是over-budget失败。

121没有检测或拒绝 `log_budget_omission_columns`。它只沿原119逻辑核每份原reader实际GITHUB_OUTPUT协议、原字节数与SHA、当前真实run/source；完整正常summary原样输出。只有原reader本身返回非正常fallback schema、未完成协议、非零退出或超其原90,000 B界，才作为编排/记录问题停止链，不能写作原数学拒绝。八份summary分开输出，不拼成一份90 KB限制内的假完整摘要。

## 4. 每个子批次保留原数学预算与fresh计算

每批均是一个新的原科学进程，显式 `--initial-relative-radius 0.1`。实际父末radius `0.00078125` 只作来源说明，不携带进下一批。每批内部的原radius更新公式保持；此编排也不是把原单次方向预算改成64。

| 项目 | 本次值/行为 |
|---|---|
| 独立子批次上限 | 8 |
| 每批原方向预算 | 8，原语义包括接受与拒绝方向 |
| 每方向原outer回溯 | 20 |
| 原normal corrector预算 | 12轮，每轮20回溯 |
| 初始relative radius | 每批明确reset0.1 |
| candidate resonance / normal target tolerance | 原 `1e-8` / `1e-8` |
| 标量Arb配置 | 原160bits、depth14 |
| 原mesh/M/T/角度配置 | 699 /112/112；physical2048、material与boundary4096 |
| 原RHS worker / BLAS threads | 1 /1 |
| 整链wallclock预算 | 3600秒，仅批间检查 |
| science step / compute job | 75分钟 /90分钟 |
| 原规则同步周期 | 2700秒，覆盖整个wrapper进程组 |

原六控制入口自己fresh形成初始真实响应和完整3×6J，执行原全部行/列、域判定、曲线候选、full3 Armijo和normal校正；每批完整执行其原最终FD、scalar Arb、circle与全部原标志。编排器不比较不同批次的merit，不以rank、奇异值、下降幅度或额外容差选择下一点。

原四数学输入及SHA与119完全相同，缺文件时仍只按原 `8bd267107cc8710d371f3b62c02986655ac965b0` 历史ref恢复；原78公开数值源码只恢复一次。Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0及已锁setup Actions均不改。recipe只带同四输入SHA，不保存父数值数组。

## 5. 当前真实子status产生下一recipe的顺序

每批原科学stdout/stderr重定向到自己临时目录，只存/输出其bytes/SHA。child真正退出后，原reader使用该批独有临时 `GITHUB_OUTPUT`，输出被核验并完整打印。wrapper随后完整读取本批status，核原schema/producer24闭包/四输入/family/实际incoming recipe；若有原trace描述器，也逐字核其完整文件SHA。

只有真实完成status与正常原reader的final参数相符，才生成本批 `after-batch-NNN.json`。新origin取**本次实际** `GITHUB_RUN_ID/GITHUB_SHA`、刚完整读取status和summary的原bytes/SHA，仍写原 `e154…` producer。接续点只来自原 `final.parameters` / `last_accepted_parameters`，不替换为某个中间trial或预测点。生成的小recipe不会承载旧J/W/曲率/FD/circle。

停止条件保持119原文逻辑：实际外部资源/规则signal，child非零退出或异常/未完成，原reader非正常完整summary，原unit停止标志true，原full112候选标志true，原接受数为零，或者本批不是明确8方向预算结束。另有最大8批和批间3600秒资源结束。停止只是相应原原因，不从进程exit0或8批完成推出BVP/native/闭场完成。

`Processes`不设置child timeout、不创建新session，仍在原rules runner管理的进程组中。批间3600秒不截断已经启动的原8方向批次；75/90分钟外部资源截止仍可能产生partial，必须按实际输出记录。

## 6. 输出和临时原件生命周期

初始参数recipe放在本次自有 `recipes/batch-001.json`；每批用独立 `batch-NNN/science/`。完成上述原summary、完整status及trace读回、落本批元数据和下一小recipe后，原119的 `shutil.rmtree(batch)`删除该批自己拥有的可重算raw；未来child只读下一recipe，没有旧数值模型文件依赖。

如异常、readback未完成或资源中断发生在该删除点之前，失败批临时目录不会被提前删除或冒充已读。workflow的always步骤只读chain与真实rules日志作摘要，**没有新增always递归删除**。这些未完成临时raw不上传、不入Git/Release，最终随该runner生命周期销毁。原source恢复目录和临时恢复的四输入也只在该runner内存在。这与119原文件生命周期一致。

chain只保存各批真实来源、参数、stop flags、summary/status/trace等SHA和实际过程元数据；其compact报告单独受原90 KB限制。每份原科学summary分别有BEGIN/END及bytes/SHA。完整原summary的读取范围与其原省略列表并列，不能把summary的部分视图冒作status全字段公开输出。

## 7. 独立触发和CLI

新workflow唯一push路径：

```text
topics/visible-flex-larger-amplitude/computations/public-six-control-batch121-request.json
```

独立concurrency为 `visible-larger-public-six-control-batches121`，`cancel-in-progress:false`；无workflow_dispatch、无旧119请求更新、无artifact或Release上传、无旧publisher运行。

workflow在实际run计算新request文件SHA后，交原rules runner调用：

```text
python geometry_20261115_six_control_temporary_batches121.py
  --request <public-six-control-batch121-request.json>
  --request-sha256 <实际请求SHA>
  --repository-directory <当前checkout>
  --rules-directory <本次out>/rule-sync
  --out <本次out>/six-control-temporary-batches121
```

always报告调用同文件 `--report-only --out ... --rules-directory ... --compute-outcome <实际step结果>`。科学child环境移除token/动态Git auth等字段；metadata rules runner保原同步权限与实读规则的行为。两README仍锁已读 `74c08a36…` / `bff8aea2…`，若后续规则变化由原机制真实报告/停止，不假称pull已发生。

## 8. 本地完成的范围

仅进行了原JSON字面读数、bytes/SHA核对、source差异、AST和bash语法检查。20个原函数/类AST不变；更改仅在 `bind`、`emit_original_summary`、`run`、`report` 的新父来源、request/schema及日志/chain身份。原 `science_argv`、`Processes`、`parse_reader_output`、`read_status`、`genuine_next_recipe`、`original_stop`、`main` 全部AST一致。7段shell、4段inline Python通过源级语法检查。

完整证据为同目录 `request121-static-check.json`（6821 B，SHA `93fb983bf09fcdb9a4ce9fba2b5e0f945f64e5ad53f50418661a8e3e8346ac46`）及四份diff；这是已完成接线记录，不是额外科学接受门。没有导入或执行wrapper、原模型、NumPy/SciPy/Arb，没有新数值试验、下载或Git变更。后续实际121原读数必须来自其自己的公开Actions。
