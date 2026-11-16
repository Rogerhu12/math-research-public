# R428：完整 39-query 八对链的必要读回修订与 request200 合同

作者：AI（ChatGPT，exact_refinement）；日期：2026-11-16。

## 428.1 已发生的缺口与本修订的范围

[R404](R404-actual191-eight-real39-pairs-and-necessary-summary-overflow.md) 已记录 actual191：八次原 model 及八次 fresh FD 都实际返回 0，八个真实新 pair 按冻结控制流全部 eligible；但整链必要对象 210886 B、恢复对象 215693 B，均超过原 90000 B 上限，在正文打印前退出 70。原日志只保逐批 trial 数 4/3/4/3/3/2/2/3，未交付对应数值与失败地址。本修订没有读取或恢复这些已销毁字段，也不把后续运行称为 actual191 末场续接。

request200 明确从同一可恢复的 actual98 原 pair 另起，重做同一完整 39-query 八对实验。它保原 38 集合并含 RIGHT-RMS459、原 459/460 真实端点响应、free461 的完整仿射 QR 消元、完整 H/outside 恢复和既有模型/FD 接受判据。新两源只改变必要字段选择、请求身份及临时 namespace；五件数学源、全部原试探和资源上限不改。

本件是具体源码接口与包含范围，不宣称新数学收敛定理，不保证任意未来失败分布均可装入 90 KB。若完整必要内容仍超限，仍停止传输并返回 70；不删真实失败行、不拆包、不把大原科学树换编码输出。未执行本地科学、import、AST、编译、fixture 或数值对拍。

## 428.2 冻结源与真实基线

原基线是 actual191 的 commit `7891ee252147194137c2a933b6407a7c2c0ac19f`，不是早期审稿。完整 worker 及 reader 均已逐段读取，另读原 `e2e8ec32...` scalar selector、原 `7d75a44a...` full-angle engine、完整残差/RMS 输出接口及实际 QP summary 形成位置。

| 新件 | bytes | SHA256 |
|---|---:|---|
| `root_20261115_thirty_nine_necessary_chain_readout.py` | 62855 | `abf42d92c980566e20a4c8a7fbd90976669240bf8cc8bed06d3b6e1705fa79b8` |
| `geometry_20261115_thirty_nine_necessary_batches.py` | 29611 | `68d53286565c892cdcebd131fb73c2c32b25d6ff865a6da706bec03dbfdbe8e5` |
| `public-thirty-nine-necessary-model-recipe.json`（两源依赖的准确配方） | 31236 | `2b9c71c067dfb8a7ff9fcd7111e4eff884a68e197504c38e14b128b6ecb8692f` |

原 reader 为 `root_20261115_thirty_nine_temporary_readout.py`，52090 B / `f10cb06439daef0be952a465bf75790703265bd6565f39274d7fea8ce94fc4b1`；原 worker 为 `geometry_20261115_thirty_nine_temporary_batches.py`，28049 B / `9631f34cb0a0ccbcc08666e9ea8476174edaf3cfaf9bf544304cff4cdec8468b`。原件不改。

完整两源差异是纯文本 `core-readout-and-worker-relative-to-actual191.diff`，48448 B / `1667d64525c185b6f8a95533b1c284cc9b6af205f1ce0bbb9ec7047bc1bdce71`。该差异是源文件可再生的临时阅读材料，不要求作为数据另存。源未在本地解析或运行；后续公开 Actions 的既有源/参数校验和真实调用承担可执行行为。

## 428.3 所有科学动作仍由原实现执行

以下五件实际数学源继续用原字节：

| 原科学模块 | SHA256 |
|---|---|
| 39-query domain operator | `0dc60f8a43da0eed700e9e70235759b42890c038121c1f5a973fc6a417bf038d` |
| 39-query condensed warm | `568d1f22ef9de4fe31d1a9e570ed66b3b91fb51525fc5dd5eb27f99c4901d3a9` |
| 39-query condensed response | `fc92e7d900b0ccc24f6d6a162443112122f0e724c1e6b235914d23c593b4754c` |
| 39-query collocation observer warm | `59fa547d08f01f43b9000f8f58bb2c3eb03cc06a3a6f92dbeeedf728b08b19ea` |
| 非连续支撑仿射消元 | `b7a5f7e6d699a2ed9c9d4068c3f831d633b76a1df457630ca536fd5207186ce4` |

原完整 453 状态布局及 699 节点、所有 112 模态、原完整 236036 坐标问题、A/AT、B/BT、完整 H、原 C 对比及 outside 响应保留。真实 B 的 32 节点仍为 459、460、462 至 491；没有虚构 B461。内部 33 节点 cover 的 11266 front 先对真实自由 461 及原仿射列/RHS 一起消元，得到 10928 front、10819 local coordinates，再沿原完整恢复。没有通过删梯度项或常数行降低责任。

原单模型命令继续使用一轮、damping270、LSMR200、projection200、17 档、1200 s、4096 angles、2 个 J workers、condensed600 s、trial reserve90 s、recovery reserve30 s、working512、dual200 及原 store-root。原 fresh FD 的全部方向、层次、Richardson、误差阈值和直接/分离两组判断都实际执行。

worker 的 `validate_completed_pair`、`move_pair`、`model_command`、`run_batch` 四个完整函数正文与 actual191 逐字相同。变化发生在被调用的纯字段选择 helper 及 `field_identity` 的三参数附记。旧 104 源身份全部保留，再加新 reader 和新 worker；配方 105 pins，独立 worker 另 1 pin，共 106。旧 191 reader/worker 仅来源与基线，不执行旧编排。

batch 之间仍只用上轮实际保存的新 warm/status；必须先通过原真实配对和 fresh FD，才晋为下一轮父。最多 8 对，between-batches 10500 s，科学 step175 min、job195 min、readback10 min 均保原约定；这些资源上限不修改任一原数学条件。

## 428.4 完整必要值如何选择

新读者没有读取一个大科学树再将其整体编码为短字典。它只选择以下明确有限内容；全状态、RHS、矩阵、Bz、乘子向量和完整迭代历史仍只在原 Actions 临时目录内，外部仅原文件 bytes/SHA。

### 428.4.1 全部已返回 trial

每个原 trial 的原索引、alpha、接受布尔、model slope、预测下降、实际固定权 merit、实际下降、实际/预测比、原因及其他原必要浅标量均保留。数字与布尔是原 JSON 值；原已选中的错误字符串完整保留，不再由旧通用 shallow helper 的 512 字符缩写代替。

`selected_linear_beta_squared`、`all_selected_linear_reserve_slack` 和原 `independent_actual_directional_check` 各自保原已有浅标量。后者只在原 engine 实际产生时存在；读者不新做方向校验。

共同列名只对这类人可读小标量表声明一次，各行仍对应原 batch/trial 索引。没有把科学数组、递归 JSON 或全部原对象变为可重建的数据包。每批保实际返回索引、原声明上限 17、未记录索引和最近原拒绝索引。未记录不自动解释为未执行：中断可能发生在某个原计算返回、但尚未提交记录之间。

原 merit 条件仍来自冻结 engine：实际下降超过 `64*binary64_eps*max(1,base_fixed_weight_merit)`，实际/预测比至少 0.1，并通过完整原域及 RMS 检查。engine 没有保存每 trial 的 floor 数字，新读者明确该数未记录，不自行重算并冒充原输出。

### 428.4.2 域、RMS 与失败地址

原域的 16 个门值/必要标量完整保留：node/midpoint failure counts、boundary/finite、全角 rho guard 及最小值、原边界错误、完整 RHS 已重算、core/control 常数状态身份、left residual、physical collocation、完整边界与常数残差、RMS failure count。

每条已返回的 selected-query 失败仍含 query index、kind、interval、fraction、station、input-finite，以及原 beta 的 minimum、angle index、phi、负/零/有限/非有限计数。原 complete39 定义只在共同来源中出现一次；不删“非最坏”的失败 query。

原 RMS 每个 fraction 的 points、invalid_count 及全部原返回的 `first_invalid_points` 保留，含 interval/s/left/right/minimum beta/phi/a/ap/app/curvature。原 `rms_domain` 自身只对每个 fraction 的前 24 个无效点产生这些样本；本读者不再限量，也不声称给出了超过原样本范围的所有失效点地址。总 invalid_count 仍保，尚无原地址的范围不会被伪造。

midpoint observer 的原 bad-index 集合可写为准确整数连续地址段；这只是地址元数据。每个原已返回失败 point 的 station、有限标志、classification、beta 最小值/角址及计数完整保留。物理 argmax 保原行/interval/端点站位/符号值/绝对值/分量与已有固定权值；不重复该点的状态六元组、原大数组描述或同一个 weight-array SHA 树。原 observer 错误字符串亦保。另独立遍历所有原返回 midpoint points，不受 bad-index 筛选：凡有 angular_observer_exception 或 observer_export_exception，均保原 point 索引、interval、station、original_solver_result_still_used 与完整异常字符串；原 traceback 仅附身份。report.collocation_weight_observer_error 的原异常、diagnostic_only、original_weights_returned_unchanged 等必要标量也完整保留，entry/traceback 仅身份。

若 `domain` 与 `complete_original_RMS_query_domain` 的必要记录确为同一原 JSON 值，则只用明确的“原 JSON 相等”标志复用一次；不从一项的通过推断另一项已评价。不同原对象分别保存。

### 428.4.3 QP、FD 与八个真实 pair

QP 仅保真实最终选择、原 C/condensed 对比目标值、helper 完成/回退/失败、完整实际模型的 slope/decrease/linear slack/finite/可行门、原后验标量及其非严格范围、已有 working/dual 停止原因与资源计数。完整 QP summary 的原文件及 canonical 身份绑定未输出历史；没有把工作集最优或浮点后验升级成完整 QP 证明。optional failure 的原 type/message 保留，完整 traceback 另有身份；原 child stderr 沿既有路径完整处理。

FD 保原顶层误差、阈值及判断、直接/分离两组原标量、各方向标签和实际层数。对原 refined_directional_check 的 second_order_contraction，每个 contracts is False 项均另保 group、direction、direction_index、record_index 和完整原五标量记录（coarse_step、fine_step、observed_error_ratio、contraction_test_applies、contracts）；仅选择原布尔值，不重新计算收缩判据。其余成功层数值历史仍只在原 response 文件。它保新 warm 的 preparedSHA、来源以及原完整文件身份。新的读回选择不减实际 FD 计算。

每批只保必要 status（phase、进展/接受数、success/full acceptance、原最新 warm 身份、elapsed/error/stop）、真实输入 pair、真实输出 pair、原过程返回码、eligible 与 stop，以及必要原 model/FD 文件身份。source/输入/查询定义放共同部分，不在八批和每个失败点反复复制 producer 树。原 model/status 的共同字段关系继续如实记录，不成为新数值门。

### 428.4.4 末 pair 的准确原三参数

worker 已在原 `validate_completed_pair` 后读取真实新 warm。新 `field_identity` 直接选择：

- `complete_scalar_profile.frozen_design_parameters`；
- `optimization_warm.actual_global_scalar_parameters`。

两者均要求作为已有三项记录读出；没有从状态反求参数、没有重新 profile 求值，也没有数值比较门。若某项在原件缺失或形状不是三项，报告原来源存在性与 `original_parameter_readout_complete=false`，不截取伪造三项。完整 profile 与原 native-height 字段只附 canonical JSON 身份；不输出高度/场数组。

每个真实 pair 可给这三参数，最终状态再明确最后一个完成 pair 的参数与 warm/status 身份。它们不构成一个可续接的完整场 checkpoint。缺少完整 warm，不能仅凭三参数或 SHA 冒用为后续原 native/full BVP 输入。

## 428.5 原子保存、静止与清理

每批仍先保存完整必要单批记录，再移动已经消费完的真实 warm/status，并在移动后核原 bytes/SHA，最后退休大原输出。下一个科学 child 不使用 reader 投影对象作为数学输入。

整链只在 `finish_chain` 组装完成后调用 `publish`。输出按 sorted ASCII compact JSON 加一个 LF 计 bytes/SHA；只有总长不超过 90000 才打印一个完整帧。超限先报告真实 bytes/SHA、`summary_complete=false` 和 transport70，正文不打印；不拆包、不截断、不伪称成功。读回失败与原科学接受明确分开。

原 `3b8` rules runner 的独立 session 行为保留。新请求在任何恢复/科学调用前登记自身 pid/pgid/sid/start-time/boot-id，并绑定当次 run/source/request/worker/helper；原 model/FD 子进程继承该 session。always 只对已确认属于自身的活动组实施原受控 TERM/KILL 与复核。未知 ownership、PID reuse 或无法证明静止时，读回为 partial70，不读删可能仍变的输出。

正常最终读回、always 恢复以及 cleanup 都只认 request200 的独立 namespace 和真实身份。恢复读者可读取已保存必要件、尚存 batch 与已搬到 parent-after 的真实 status；它不由无文件推断科学成功。cleanup 仍须必要读回成功、原规则读回成功以及新的静止确认。任何一项未付就保 surviving output 到临时 runner 销毁，不能仅因为 cleanup step 绿就称已经删除。

本修订没有将 90 KB 容量检查提前成候选/FD 的接受门，也没有通过少执行后续科学来保证摘要容量。若未来实际失败地址过多，仍可能诚实超限；该情形需要新的必要范围设计，不能悄悄少报地址。

## 428.6 重新执行与尚未完成的责任

request200 的唯一首父仍是 actual98 artifact `14147700690`、run `43677587785`、source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`。原 ZIP 809042943 B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`，完整运输核验后只解原 warm/status；四数学输入、原 104 源、同一数学参数与全部 fresh 模型过程沿原合同。

核心 worker CLI：

```text
python -u computations/geometry_20261115_thirty_nine_necessary_batches.py
  --repo-root <fixed scientific checkout>
  --request <public-thirty-nine-necessary-batch-request.json>
```

always 必要读回 CLI：

```text
python computations/root_20261115_thirty_nine_necessary_chain_readout.py
  --readback-only
  --temporary-root <this job RUNNER_TEMP>
  --code-directory <fixed scientific computations>
```

两源发布并不代表已经执行。正式 request/workflow 另绑定当前已读 README、确切新配方和两源 SHA 后，由唯一主控发布；不得执行旧191请求而把新读者结果贴成原191。所有实际输出只能来自新的公开 Actions。即使 request200 将来八对完成且必要摘要通过，也仍只有原 warm 优化进展；完整 native、full DN、finalJ、敏感度与物理 audit 的责任不由此替代。
