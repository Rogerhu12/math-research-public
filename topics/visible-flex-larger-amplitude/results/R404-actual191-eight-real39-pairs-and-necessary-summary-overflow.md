# R404：actual191 的八对真实 39-query 进展与整链必要读回超限

作者：AI（ChatGPT，exact_refinement）；日期：2026-11-15。

## 404.1 本次结论及证据层次

actual191 已完成八次真实 model 调用及八次对应新 warm 的 fresh FD 调用。全部十六个原 child 返回 0；每批都实际保存必要记录，随后发出 `next_actual_parent_pair_retained=true`。结合冻结 worker 中产生该事件的唯一控制流，可以确认八次原进展接受、真实 warm/status 配对及对应 FD 的既有交接判据均已通过。这里的接受是原 warm 优化进展，不是完整 native、full DN 或课题最终接受。

本次 job 的失败发生在整链读回：首次必要摘要为 210886 B，always 恢复摘要为 215693 B，均超过原 90000 B 上限；两次均在输出正文前明确返回传输码 70。因而当前公开日志没有这八轮的原 alpha、merit、各拒绝 query 地址、完整 FD 误差或末场字值。不能从本次源代码、文件 SHA 或子进程退出码补造这些未输出字段；也不能据此判断新增 RIGHT-RMS459 后最近障碍移到了哪里。

本报告只读取本次唯一取得的官方 job 日志、官方终态及冻结源码；本地没有运行模型、FD、QP、矩阵、norm 或场重建。下文分别标明直接日志事实与由实际事件和冻结控制流共同支持的结论。

## 404.2 实际运行与源身份

| 项目 | 本次实际身份 |
|---|---|
| repository | `Rogerhu12/math-research-public` |
| request | 191 |
| source commit | `7891ee252147194137c2a933b6407a7c2c0ac19f` |
| run | `43766271165` |
| compute job | `132971948907`，`original-thirty-nine-batches` |
| 创建 | 2026-11-15 21:54:31 UTC |
| 官方终态 | completed / failure |
| workflow | `.github/workflows/visible-larger-public-thirty-nine-batches.yml` |
| request | `public-thirty-nine-batch-request.json`，11027 B / `941dd0cda2dff96f6889a3b327c86aee2df3f0a3484d96f12344e55801962b11` |
| recipe | `public-thirty-nine-model-recipe.json`，29930 B / `bf443e95b3f49438b45b81212485bae2261056238f20e5d9cec85b596c46dd0e` |
| batch worker | 28049 B / `9631f34cb0a0ccbcc08666e9ea8476174edaf3cfaf9bf544304cff4cdec8468b` |
| necessary reader / lifecycle helper | 52090 B / `f10cb06439daef0be952a465bf75790703265bd6565f39274d7fea8ce94fc4b1` |
| workflow bytes | 13045 B / `90e51773a675b6d0576ae8d1ff5dd3df0ce4183e1a40ccd89ab964d917762c3e` |

原官方日志只取得一次。连接器返回的完整字符串按 UTF-8 编码为 99194 B，SHA256 为 `e8ced76b8c034d5605b116495cb98df2f16c0c0f5cab110d089470ec06c63ace`。这是连接器解码字符串的 UTF-8 身份，不冒称未经解码的 HTTP 原响应字节身份。解析视图仅逐物理行移去一个行首 BOM，再移去锚定的 Actions 时间前缀；原字符串保留。实际没有完整 `BEGIN_REQUEST191_...` 摘要帧，因为超限 guard 在正文打印前已停止。

官方步骤明确分层：步骤 1–6 成功；步骤 7 原八批科学与规则 runner 失败；步骤 8 静止确认及整链必要读回失败；步骤 9 原规则终止元数据读回成功；步骤 10 cleanup step 成功，但该步骤实际执行的是“跳过删除”分支。不能把最后一个绿色步骤解释成 namespace 已删除。

运行与源码链接：

- [actual191 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43766271165)
- [冻结 batch worker](../computations/geometry_20261115_thirty_nine_temporary_batches.py)
- [冻结必要读者及 owner 生命周期](../computations/root_20261115_thirty_nine_temporary_readout.py)
- [request191 完整接口](../notes/2026-11-15-request191-independent39-gap-condensation-and-one-chain-readback-interface.md)

## 404.3 这是一条从 actual98 另起的 39-query 轨迹

原输入仍是 actual98：run `43677587785`、source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`、artifact `14147700690`，原 ZIP 809042943 B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`；原 warm 4927052 B / `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`，原 status 3379453 B / `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。actual171 的末 pair 没有作为新输入；[R361](R361-actual171-real37-to38-sixteen-pairs-and-right459-barrier.md) 只提供查询选择依据。

本次保原 38 个 query，新增真正的 RIGHT-RMS459，fraction 原字面为 `0.8273268353539885`。完整端点支撑是 459、460、462 至 491，共 32 个节点；461 仍是完整场中的自由变量。实际 source-check 事件报告 39 queries、26 个 capture interval、10819 个 local coordinates、4059 个原 C coordinates；内部 cover 是 33 nodes / 11266 front，真实消去 hole 后为 10928 front。其 `free_node461_prefix_QR_not_zero_padded_B=true`。

[R407 及其原适配发布](https://github.com/Rogerhu12/math-research-public/commit/94c9eac2461e2b7285413b56639104a4765ea540) 所述独立适配将 461 的完整仿射平方根列与原 RHS 同时正交消元，再保原 109-core 消元和完整恢复；没有在 B 中补一个虚假的零响应节点。其源为 `root_20261115_noncontiguous_local_qp_condensation.py`，13361 B / `b7a5f7e6d699a2ed9c9d4068c3f831d633b76a1df457630ca536fd5207186ce4`。本次 source-check 原事件实际核了 97 个既有源、6 个新 query/gap/readout 源和 1 个独立 worker，共 104 个显式源及 1 件参数。

本次原 39-query 科学源：

| 源 | SHA256 |
|---|---|
| domain operator | `0dc60f8a43da0eed700e9e70235759b42890c038121c1f5a973fc6a417bf038d` |
| condensed warm | `568d1f22ef9de4fe31d1a9e570ed66b3b91fb51525fc5dd5eb27f99c4901d3a9` |
| condensed response / FD | `fc92e7d900b0ccc24f6d6a162443112122f0e724c1e6b235914d23c593b4754c` |
| collocation observer warm | `59fa547d08f01f43b9000f8f58bb2c3eb03cc06a3a6f92dbeeedf728b08b19ea` |

原完整 H、A/AT、B/BT、outside 恢复、线性 reserve、真实域与 merit 判据、17 档试步、fresh FD 和资源停止语义都未改。本次请求最多八个 model/FD 对；between-batches 预算 10500 s，科学 step 175 min，job 195 min；这些是资源上限，不是最终数学判据。

## 404.4 八个实际 pair：直接记录与控制流联证

原 child finished 事件直接给出下表。表中秒数和 trial 数均为原输出，没有重新计算科学量。

| batch | model exit | model 秒 | fresh FD exit | FD 秒 | 已保存原 trial 数 | 必要单批文件 B |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 794.193616772 | 0 | 20.517259364999973 | 4 | 33820 |
| 1 | 0 | 796.0074844 | 0 | 30.13381656499996 | 3 | 34381 |
| 2 | 0 | 793.856281613 | 0 | 18.100008745000196 | 4 | 37735 |
| 3 | 0 | 796.52703367 | 0 | 18.060375514000043 | 3 | 33476 |
| 4 | 0 | 790.564009493 | 0 | 17.79744062000009 | 3 | 33076 |
| 5 | 0 | 791.8431398230005 | 0 | 18.011741061000066 | 2 | 29871 |
| 6 | 0 | 799.2981521470001 | 0 | 18.149529799999982 | 2 | 27633 |
| 7 | 0 | 802.3557987649992 | 0 | 18.033178139000483 | 3 | 34039 |

十六个 child 的 stderr 都是 0 B，完整 stderr 读回标志为 true。model stdout 及 FD stdout 只保原 bytes/SHA，没有输出其完整科学正文；不能把它们的身份等同已读内容。

八件必要单批文件的原 SHA，依 batch 0–7：

1. `3a071fcb2968d1efad212bf48110fd7e2b5d270c58c67ada85d13cf87057731a`
2. `934ff8904e00cb5bfd148354b16623a73b7fc64de9e90a24d3eef77b0a202d21`
3. `5a9bd1ec5e4c96c8d2ed143edfc57a0b4ecddabc33594fced9571a59e41167a9`
4. `eba7ac0a5ec14604e76815aed385007bc68c0b5942caaf2a86ff2455fb676828`
5. `f87264d8f87d47deac085804e62b1ba564c61d848cd3163d895d69fa89a7be0e`
6. `a63278c643f22b92436c6fe802519e198a9d8901bfc36b4507a17e29e4ef8d8b`
7. `13319d780daaff0fcb7d7ab9ad831716fda5f9eb5efc583409ee853deb67ffec`
8. `50f43ebe75c2c60a79973b88ea14f77e580f944db9a4c16a6c568bc4b634007a`

**关于“八次接受及 FD 已付”的严格证据范围。** 原日志没有八份 status/FD 全文，因而本报告不把里面未输出的数值当作直接读到。冻结 worker 的 `run_batch` 和 `validate_completed_pair` 则明确：

- 只有原 model exit 0，原 status 的 `optimization_progress=true`、`accepted_warm_steps=1`，并且原 warm/status 的 schema、完整 producer 身份及文件 SHA 配对相符，才进入新 warm 的 FD。
- 只有 FD exit 0、原 `implementation_check_passed=true`、`prepared_sha256` 等于该新 warm 的 SHA，且 `complete_current_warm_boundary_FD_actually_recomputed=true`，才令 `eligible=true`。
- `move_pair` 只在 eligible 时运行，移动后再次核真实文件 bytes/SHA。之后实际发出的 `next_actual_parent_pair_retained` 就是这个 eligible 的布尔值。
- 本次八个退休事件该值全部为 true。因此上述原判据有“冻结控制流＋实际到达事件”的联证，不依靠仅看 exit 0 推测。

这些原 status 同时要求 `success=false`、`new_coupled_finite_acceptance=false`；原 warm 也保相同 false。八次进展并没有转成 native 或 full DN 接受。本次 wrapper 亦没有调用 nonlinear native/full DN。没有第九批记录；八批已达到请求的批次数上限，但程序最终返回 70 的直接原因仍是随后摘要超限，不应只写“预算正常结束”。

## 404.5 整链读回的真实断点

首次 `request191_necessary_summary_identity`：

- label：`whole-chain`；
- bytes：210886；
- SHA256：`10146b7213f5d3f545f5d6db8355bb017e931913162505b79510300742ccd835`；
- 口径：necessary scalar JSON **含一个 LF**；
- `summary_complete=false`；
- `reason=necessary-summary-exceeds-90000-bytes`；
- `transport_exit_code=70`，`full_result_not_split_or_encoded=true`。

原 worker 随后抛 `ReadbackIncomplete`，原错误字面：

> Necessary summary exceeds90000; preserve unread necessary records and surviving raw

always 读者在确认原 owner 静止后再次组装恢复摘要，得到 215693 B / `3726f2281af884f5d753704376a23c31e36d045ce86247d57a2b1b948a4e3bd4`，同样含一个 LF、同样超限、同样退出 70。恢复事件明确 `scientific_result_not_reclassified=true`、`unread_owned_output_not_deleted=true`。

这两个 SHA 是“原完整必要对象实际存在、但正文没有进入日志”的记录。它们不是可复原数据。当前日志无法逐值交付的范围包括：所有 24 条 trial 的 alpha 与真实判据值、接受前后 merit、最近拒绝位置、原 selected/RMS/midpoint 域详细地址、FD 数值误差与阈值、各真实 warm/status 的完整 pair 身份、最终场及参数。不得将默认字段、预测结果或 earlier actual171 数字填入这些空缺；也不得从 8 次 eligible 推出某个未选择 query 已经安全。

源级定位是必要读者的聚合范围仍过宽：`assemble_chain` 将每批 status、QP、FD、model-before、域/RMS 多份必要子对象与原 trial 标量一并纳入最终整链。它已经避免输出大数组和分包，但本次真实对象仍超过 90 KB。没有原完整正文，当前不能给出各字段的实际字节占比或把超限归因给某一特定域行。

## 404.6 实际静止、规则监控和清理

本次 owner 真实注册 pid=pgid=sid=2461，原 ppid=2334、start_ticks=6106。always 静止记录实际为：

- `quiescent=true`；
- `signals=[]`、`unknown_scope=[]`；
- `before=[]`、`after=[]`、`live_original_group_after=[]`；
- 不对未识别组发信号，不冒称追踪未登记的 detached process。

因此本次不是在仍有已登记 writer 活动时执行恢复读回；也没有使用信号强杀后冒称原模型正常返回。

原规则结果 482 B / `7a58f92a3c920b9c212ca89fb12322e97e3be8559fbd6e4f83a44b2476928c1f`，原时间 21:54:58–23:44:07 UTC；`science_returncode=70`、`wrapper_returncode=70`、`periodic_sync_failures=[]`、`README_change=null`、`science_terminated_for_actual_rule_change=false`，`sync_rounds_started=3`。没有规则变更终止证据，也不是科学墙钟耗尽所致。

清理要分两层。每批原大 model/FD raw 在完整必要单批文件已写后实际退休，八次 `batch_payload_removed=true`；新的真实末 pair 则作为下一批父保留。整链正文两次超限后，最终 workflow 的 cleanup 分支实际记录：

- `actual_necessary_readback_outcome=failure`；
- `actual_rules_readback_outcome=success`；
- `unread_surviving_raw_and_necessary_records_retained_until_runner_destruction=true`；
- 事件为 `request191_owned_cleanup_skipped`。

所以本次没有宣称最终 namespace 成功删除；未读小必要件和末 pair 留至临时 runner 销毁。它们没有上传 Git、Release 或 artifact，也不是后续可以按 SHA 直接取回的外部 checkpoint。

## 404.7 已付范围与下一具体工作

本次已付的是：从真实 actual98 另起的完整 39-query 接线运行成功；free461 的完整消元/恢复路径实际进入八轮原模型；八个真实原进展 pair 及其 fresh FD 按原交接条件相继通过；最后读回失败的地址、尺寸、退出及静止/清理语义明确。没有已读证据支持宣布新的最近障碍、末 merit、完整方程解、非零 native、full DN、finalJ 或 physical audit 成功。

下一改动应仅收窄必要摘要：保一份共同来源/查询定义、八个实际 pair 身份、每条真实 trial 的必要标量和所有已返回失败地址、FD 顶层判据/误差/阈值及原完整文件身份、真实停止与未访范围；删去重复的整子对象。仍保单份 90000 B 上限，超限诚实退出 70，不拆包、不上调阈值、不把读回成功加入科学接受条件。

若要得到本次未输出的数值，当前公开日志与 SHA 已不足；必须在新的公开 Actions 请求中从可恢复的真实 actual98 再执行明确的新轨迹，不能把重算称为续接已销毁的 actual191 末 pair。只有新请求真实得到必要字段后，才能判断下一科学动作。修读回无需更改原 39-query 数学源、原模型/FD 判据或 R407 消元公式。
