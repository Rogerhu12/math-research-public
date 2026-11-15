# Request134：最多 32 个原九控制八方向批次的临时串接接口

作者：ChatGPT（`amplitude`，AI 协作研究）；2026-11-15。

**分类：源码与执行接口；没有新科学运行，没有非零场接受结论。** 本稿将已实际运行的八批编排扩为最多 32 个独立批次。每批仍执行原九控制科学入口、原八方向预算和全部原末端检查。它没有把原科学程序改成一次连续 256 方向求解，也没有携带前批的信赖半径。慢降机制的范围另见 [半径重置与慢降分析](../results/R295-nine-control-radius-reset-and-ideal-model-descent.md)。

## 1. 直接接线文件与身份

| 角色 | 文件 | SHA-256 |
|---|---|---|
| 新编排入口，48,045 B | `geometry_20261115_nine_control_thirty_two_temporary_batches.py` | `fd5d78f3a24b4f5bbcb38c59bc25ca9405244f6253de5438bc00776b4e1fb5bb` |
| 八批历史编排，只核身份、不执行 | `geometry_20261115_nine_control_temporary_batches.py` | `b15a6571a1ebc5dc72f1037212fd86a10d7a5848957c2faca4ae9e7fd69f21bb` |
| 原九控制科学入口 | `geometry_20261115_small_core_nine_control_curved_recipe.py` | `824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf` |
| 原九控制标量族 | `geometry_20261115_small_core_nine_control_family.py` | `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629` |
| 原完整分段读者 | `root_20261115_small_core_nine_control_curved_scalar_readout.py` | `f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d` |

新的 workflow 为 `.github/workflows/visible-larger-public-nine-control-thirty-two-batches.yml`。它只由 `main` 上独立请求路径 `topics/visible-flex-larger-amplitude/computations/public-nine-control-thirty-two-batch-request.json` 的变更触发，使用独立 concurrency group，不更改旧八批 workflow。

实际父运行是 [actual131 / 43703108343](https://github.com/Rogerhu12/math-research-public/actions/runs/43703108343)，源码提交 `2d211e0d443605cb9d1a4923a1c04779ae0fb7f3`；compute `132778318692` / report `132779364699` 均已 success。现已从原八批读回中明确选择**第8批真实末点**，不是借用 actual129 或尚未生成的场。其末 merit 为 `5.003044586685377`，原单位/full112/非零场/native/success flags 均 false。完整事实另见 [R292](../results/R292-actual131-eight-nine-control-batches.md)。

```json
[0.3057074693619713,0.21544106767239993,0.34809352591797277,-0.06492906012951118,-0.017596440125950196,0.9344695470130586,1.0750055163710799,0.6824836558052793,0.8828952762682266]
```

所选原 status 为 2,369,304 B / `34841beafbc0261eb189f0898c6903e675a82f017b4d7fdb5c28671c6c57baf9`；原 primary 62,567 B / `f6ce9ba64fc74db62f37e60e78dac5f9b7e6c580efec12930a19e5a8a8603c20`；完整分段 view 129,655 B / `639aadd57dc3b58373a2ffd21c66826c2760705a82b3682e91651f54ba8ea096`。原 status 数据已在原 Actions 按规则消费清理，本地从原日志重建的是 primary/view/链的文字身份，不冒重新独立读取原 status payload。

直接可发布接线为：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `actual131-final-batch-nine-control-parameter-recipe.json` | 2287 | `bf8e80aada9f4b009257f4bd8144fbbbeadda1dc99ec1808c25ee2bdb02d95cc` |
| `public-nine-control-thirty-two-batch-request.json` | 43351 | `aaef1c381c2e15ef3f0552b8360b26ce8628fa4ebd1617653a5f6ad5863aabd7` |
| `visible-larger-public-nine-control-thirty-two-batches.yml` | 18690 | `262e5175fb27d4fae9f54e92c298f94a6ad418a28e0b7fd99f90aed3c6fbc896` |

新 pretty recipe 不冒等于原 compact recipe；由原字段按原紧凑编码重建的原 restart 正好 1,840 B / `21bebe26f6690981d8cf13c396d090e7194e51723e17fbc08c2343f26450f2b3`。这些是 JSON 字节与参数位串核对，没有新模型运算。Request134 的未来 run 与实际结果仍未预填。

## 2. 唯一变化与原科学责任

新编排的 `CHAIN` 为：

```json
{"max_batches":32,"chain_budget_seconds":3600,"budget_checked_only_between_complete_batches":true,"reset_initial_relative_radius_each_batch":0.1,"carry_final_relative_trust_radius":false,"one_continuous_two_hundred_fifty_six_direction_solve":false}
```

每个原子批次仍使用：初始相对半径 `.1`、8 个总方向、20 档外回溯、12 次法向迭代、每次 20 档内回溯、原单位法向目标精度 `1e-8`、原候选单位停止精度 `1e-8`、Arb 160 bits / depth 14。原全三未加权 merit、实际曲线候选、原 `.2` Armijo、完整 $3\times9$ 响应、$12\times9$ 正阻尼 QR、两法向及七切向、初末九列三步 FD、完整标量域、原圆参考与所有 final flags 均由同一个冻结科学源执行。

原 `requested_constraint_error_tolerance_met=false` 不变成新外接受门，也不变成新批次拒绝门。旧低三与 full112 候选停止 flag 仍按原科学输出处理；它们不等于非零耦合场、native 收敛或课题完成。

新源码不导入模型。相对旧 b15，`science_argv`、`Processes`、`read_status`、`genuine_next_recipe`、`original_stop`、`main` 等原函数/类的 AST 相同。变化只有独立身份、32 批上限、明确历史源职责及链元数据的完整性/超限说明。没有数值 fixture、独立重跑或额外数学门。

## 3. 初始 recipe 与后续真实来源

recipe 仍使用原 `R259-explicit-nine-control-raw-quadratic-shape-recipe-v1`。九参数顺序仍是 `[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]`。完整原三支撑偶、奇、原二次形状公式不变；不把实际非零二次系数重标为零。

首 recipe 必须绑定实际131所选成功读回批次的：

- 原 run/source、原科学 basename / SHA / schema；
- 原 status 的 bytes/SHA；原正常 primary 的 bytes/SHA；
- `parameter_field=final.parameters` 及九个原字面参数；
- 原四输入 SHA 与原完整九族 family；
- 明确选的是哪个实际批次，而非只写“最后点”。

workflow 把已实际读回的 actual131 run/source、完整九参数、recipe bytes/SHA 和两份原件 SHA 写入守卫；短 request/recipe 同时精确绑定这些值。`original131_summary_provenance` 保留选中的原 status/primary 身份，明确它是正常分段读回，不是超限 fallback。这里读的是先前公开日志中的真实字面来源，不声称新 job 读取了已经按第15条删除的父原始 status payload。

从第二批起，来源更强：本 job 完整读取刚结束批次的真实 status、原 reader primary 和分段完整性声明，逐值核当前 recipe/family/source/input；原 `final.parameters` 与 `last_accepted_parameters` 按 binary64 字节比较。随后才能生成短的 own-schema recipe，记录本 job 的真实 run/source/status/primary 身份。新批次重新 evaluate 并形成初始完整 description/J；不传旧 J、merit、状态数组、FD 或域结果。

原半径在每批新 `main` 中显式重设为 `.1`。recipe 不携带信赖半径状态，所以这一轨迹不能写成连续信赖域状态的延拓。

## 4. 继续条件与停止的准确含义

原 `original_stop` 未改。只有本批子进程正常、`phase=diagnostic-completed`、无原异常、原正常分段 primary 完整、原两个候选停止 flag 均未触发、至少一次真实 Armijo 接受，而且停止文字恰为：

```text
explicit total direction budget completed, counting accepted and rejected directions
```

并且 `total_direction_attempts=8`，才可进入下一批。批数上限 32 或批间 3600 秒预算结束时不再启动后继。原科学失败、零接受、非八方向预算停止、外部规则/资源信号或 reader 协议失败均按原对应原因停。

即使一批包含未接受方向，只要原八方向预算实际付完、有真实接受且其它原继续条件成立，也沿原规则继续；新编排不发明“每方向都须接受”的门。

正常 32 批完成的链文字仍为 `explicit_independent_batch_count_completed`，其精确含义由 `batch_chain.max_batches=32` 界定。批间预算耗尽是 `between_batch_resource_budget_exhausted`，记录 resource partial；不冒科学拒绝。`zero_original_accepted_points` 等原停止也不冒根或解。

## 5. 每批完整读回与临时生命周期

同一批的顺序严格是：原 science 完成或失败 → 原 reader 运行 → reader stdout 逐字写入本批外框 → primary 逐字单独输出 → 完整原 status 与输入、来源、trace 字节身份读取 → 形成可用的下一短 recipe → 删除该批自有临时树。中途失败时，不跳过必要读回去生成继承 recipe；工作流末尾只清理本请求所有的临时目录。

每批框架保留原通用标签：

```text
BEGIN_VISIBLE_NINE_BATCH_001_ORIGINAL_READER_STDOUT
... 原 reader 全部具名分段和原事件 ...
END_VISIBLE_NINE_BATCH_001_ORIGINAL_READER_STDOUT
BEGIN_VISIBLE_NINE_BATCH_001_PRIMARY
... 原完整 primary JSON ...
END_VISIBLE_NINE_BATCH_001_PRIMARY
```

批号可至 `032`，每份原 reader stdout、primary 与重启 recipe 都有单独字节数/SHA。原 reader 内部段名/路径/组 SHA 不改；各批外框分隔同名组。独立 report job 只传链索引，不把 32 份 primary 拼入一个 GITHUB_OUTPUT。所有可重算大 status、trace、域证书与科学数组都只在 Actions 临时目录，消费后删除，不上传 artifact/Release、不提交到 Git。

若父 raw 已按规则清理，日志保存的输出 SHA 是再现身份，不等于该 raw payload 仍可独立下载核验。原子读回当时完成与后续保留范围要分开表述。

## 6. 全32行的链索引与未完成后缀

正常链索引 schema 为 `same-nine-control-original-eight-direction-thirty-two-temporary-batches-v1`；请求 schema 为 `public-nine-control-own-source-thirty-two-temporary-batch-request-v1`。

`batch_index_columns` 保留原 32 列，实际已启动批次逐字段复制原记录，包括 process/reader 返回码、原 status/primary/view/stdout/trace 身份、原 phase/stop、方向/接受/拒绝数、原初末 merit、原 final flags、真实初末九参数、初末半径、重启 recipe 和 cleanup 状态。没有对科学数值作差、重新计算、舍入简写或填造。

全部计划行必须出现：未启动批次仅有实际批号和 `phase=not_started`，其它列为 JSON `null`。未启动不是科学失败，也不能从上一批复制参数或成功字段。已启动但尚未完整读回的批次保留已有字段；`unfinished_started_batch_indices` 单独列出。`batch_plan_coverage` 还记录真正完整输出 primary/分段的批次号，日志完整性布尔值从本次记录推导，不对尚未发生的后缀作断言。

如果编排尚未建立 chain 文件就失败，report 使用独立 `nine-control-thirty-two-chain-output-unavailable-v1`，不伪造32批的实际活动。

## 7. 90KB 责任：实测完整输出，超限诚实退出

编码仍是 `ensure_ascii=True`、排序键、紧凑分隔符、`allow_nan=False`。正常链的完整 JSON 必须不超过 90,000 B。新 report **先**输出实际完整索引字节数/SHA、各 section 字节数、每行字节数与计划覆盖，然后检查硬界限。

超过界限时，不删除真实行、不切短异常文字、不减少 32 的声明、不把省略版叫完整结果。独立 `nine-control-thirty-two-chain-index-over-budget-v1` 明示 `compact_chain_transport_complete=false`、原完整索引 bytes/SHA、实际 stop/读回数、全部未访与未完成批号和最后真实 restart 指针，report 返回 70。小失败通知不声称足以重建整个超限索引；已输出原 reader 字段仍留在 compute 日志，不重跑科学子程序来掩盖传输失败。

仅作资源估计的既有观测：[R291 actual129](../results/R291-actual129-eight-nine-control-batches.md) 的原 8 行链是 20,087 B，32 列；每个原行紧凑编码 1,685–1,694 B，旧固定头（空行数组）6,572 B。旧头加32个最大已观测行的整数容量估计为60,811 B。它不是未来134结果、不是数值 fixture，也不能保证真实异常、更多规则同步或新字段不会使链变大。最终依据上述实际长度检查。

## 8. source closure、恢复与墙钟预算

新请求的 `source_sha256` 为85项：原84项保留，再加新独立 wrapper；原 b15 只作历史身份，不被 import 或执行。workflow support2项仍为原规则 runner 与原分段 reader。原科学 producer 的 consumed source closure 仍是26项，并要求 origin/current 两套值相同。工作流核每个实际源字节；不会把 source85误称为一次模型实际 import85。

四原数学输入从公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 临时恢复，原78 public source 的恢复机制保留，不恢复可重算大数据进 main。原 source topic 放独立 RUNNER_TEMP namespace。

规则监控仍是冻结 `root_20261114_current576_rules_runner.py` 的真实 `pull --rebase` / 两 README 比较 / 2700秒周期；只用请求中确已阅读的当前 README 原字节替换旧内嵌 baseline。HANDOFF 原唯一“规则同步记录：”行和10KB边界保持。`merge.stat=false` 仅避免 Git diffstat 读取已删大 blob，不改监控或数学。

compute job 90分钟、science step 75分钟、report job10分钟保持。3600秒是**批间**检查，不中断一个正在执行的原 child，也不是新科学误差门。外部时间或规则信号保原进程组传播和 partial 读回语义；没有延长某个原子求解的方向/回溯/精度预算。

## 9. 冻结与实际执行边界

此目录仅完成源码构造、原 JSON 元数据字节计数、Python AST、YAML 与 `bash -n`：新 wrapper 与8个 shell/5个内嵌 Python 通过语法检查。原科学入口/标量族/reader 均未改，未 import 科学模块、未形成数值 fixture、未本地执行算法。

actual131 第8批的真实 recipe/request 及所有85+2源 pin 已完整接好；初始九参数与原链、原最后 recipe、原 status 读者的 final/last_accepted 四处位串一致。root 独占发布与唯一调度；本文不声明 Request134 已运行、32批必全部完成或低三/非零完整场必收敛。
