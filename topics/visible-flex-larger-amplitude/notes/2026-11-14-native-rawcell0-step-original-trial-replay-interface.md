# 原始逐步矩阵方向回到原 577 节点的一次十试步接口

2026-11-14。本文交付一个独立的后继消费者。它使用已保存的完整逐步矩阵方向，取其在原 577 节点上的精确限制，然后调用原 native 的十档线搜索。没有在本地执行 constructor、RHS、RK、Jacobian、线性求解或非线性试步；没有预填尚未取得的方向 result SHA，也没有把源码就绪写成数值成功。

## 1. 冻结文件与恢复身份

执行环境在最后一次 AST/hash 读取时断连。按根 README 第 8 条的 GitHub 小文本后备方式，从已经公开的冻结 generic 两源和本轮实际写入的完整差异恢复以下文件，仅生成 Git blob，没有更新分支。

| 文件 | 字节数 | SHA256 | Git blob |
|---|---:|---|---|
| [geometry_20261114_native_rawcell0_step_trial_replay.py](../computations/geometry_20261114_native_rawcell0_step_trial_replay.py) | 27617 | f944c877a47013621a9753f2769e3687f6d6a4b2daf5d91fd6dd1021b102fa1e | 720325951efd8f5a7abec485158ab655e70fcf64 |
| [geometry_20261114_native_rawcell0_step_trial_replay_hook.mjs](../computations/geometry_20261114_native_rawcell0_step_trial_replay_hook.mjs) | 55163 | 347ce7ed21382655cc1c68c58fa6a6f7a8c75f83b5b8120b7dcaa3da6d8f8da4 | e1525599207874e89b70a42e1fc3f789a4d475aa |

hook 恢复后的 SHA256 与断连前最后一次成功 Node 语法检查、纯源码变换检查所读的完整本地字节完全相同，因此不是另造一个近似版本。Python 最终本地 SHA 尚未读到；以上是可靠重建所得实际新 blob 的身份，不声称已经证明它与不可访问的最后本地文件逐字相同，也不标记断连后已跑最终 Python AST。

冻结 generic 源保持不变：

- Python 基础源 SHA256：e357426aa6e81cbab526ea74f7f9fd3e1fd69d917000dd7f9847972745823b80。
- hook 基础源 SHA256：31c9bda7775322e9cc487903f842d755bf1c82d9102a434096ce5683791123fd。

恢复时已核从公开仓取得的两份基础文本确实具有这两个 SHA256。没有修改原 frozen worker、engine、原 tail 方程、实际 28/41 producer、动态 step-system consumer 或原 generic 消费者。

## 2. 方向属于哪个有限系统

入口固定消费：

- actual 28 的完整原始基态、H、graph/gain、far、原 sigma 和原数组。
- actual 41 的完整 72 段逐原 RK 步捕获。
- 冻结动态构造器 exact_20261114_rawcell0_step_system.py，SHA256 fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81。
- 冻结方向 producer exact_20261114_rawcell0_step_equilibrated_correction.py，SHA256 30a467e8f08d73fcdcd8a69b2d911e0d9f57489c3397c21c775ed1ec4f6cabe6。

方向 result 的真实 schema 为 native-rawcell0-step-equilibrated-band-correction-v1。两个输入 result SHA 均由 CLI 明确提供：

1. step-result-sha256：实际逐步捕获的 result。
2. direction-result-sha256：实际完整线性方向的 result。

已完成 actual 41 的 result SHA 为：

~~~text
6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf
~~~

它实际有 868 个局部步，替代原 72 个长段，加上其余 504 个旧段，形成 1372 段、1373 节点、307552 个未知量。接口依真实 layout 和 oldToNew 读取这些维数，不把“每段恰 12 步”硬编码；四个 cusp 段实际各有 13 步。实际采集与审计范围见 [actual41 结论](2026-11-14-actual-request41-rawcell0-step-capture.md)。

方向 producer 的完整 step_delta 和 restricted_old_node_delta 都被保留。Python 先调用冻结 RawCell0StepSystem 重新核全原 28/41 输入身份；这只消费已保存的数据并按已声明规则形成 output-minus-node 的有限残差，不调用 RHS、ODE、J 或线性求解。随后逐项核对：

- input-binding.json、两份 checkpoint 的完整 input_binding，以及新 matrix identity。
- 全部输出数组清单、大小和 SHA。
- 全 1373×224 方向的原坐标 raw binary64 字节；实际维数由完整 layout 给出。
- 原 577×224 限制方向的 raw binary64 字节。
- 每个 checkpoint 的有序节点、完整 224 项及负零侧表。
- 577 个 oldToNew 索引对应的完整方向字节恰等限制方向，没有插值、拟合或重新缩放。

Node 在真正首次原生请求前再核同一小文件、方向原字节、负零与限制关系。方向来自新逐步矩阵，显式记录 original576_long_matrix_claimed_solved=false。原长段 A 的缺陷只能作为已有诊断；本入口不以其大小拒绝新表示的方向。入口也没有另设新系统线性缺陷数值容差；LAPACK 状态和完整有限方向的结构旗只证明产物确实存在，不证明质量或 native 接受。实际方向是否值得调度仍依据真实计算结果决定，不从文件结构自动推断。

若未来换用其他节点规范或其他 producer，必须另绑定其真实来源和结果，不能把其文件称为本冻结 30a467… producer 的输出。原十试步正文可复用，但来源身份不能偷换。

## 3. 使用原哪一个基态

基态是 actual 23 已完成 no-J 探针的原 577×224 states，包含全部负零。其 raw SHA256 为：

~~~text
6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8
~~~

入口沿原 17/19/21/22/23 历史链核同一个完整非零 H。没有阈值置零、截频、幅比变换或 geometric initialCheckpoint 重映射。原 residual-scale raw SHA256 为：

~~~text
ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc
~~~

线搜索基态 norm/minA/minD **缓存复用实际 28 完整 withJac 的真实读数**，不是这次新评估。原 norm 为 0.04177307820740199。绑定的 actual 28 result SHA 为 ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7；summary、manifest、begin、spec、原 live identity 以及所有基础数组由冻结 binder 完整核验。

这个新消费者为重新建立完整 step-system 身份，确实需要实际 28 和 41 的完整输入 artifact，包括完整 J；它没有继承旧 generic “只需八件 metadata” 的输入精简假设。不过它**不重算这些 J**，所有大数组仍只在 Actions artifact 中消费，不写进 Git。

输出明确保留：

~~~text
baseline_is_cached_from_actual28 = true
new_baseline_evaluations = 0
new_J_evaluations = 0
new_corrections = 0
~~~

原 progress 的第 0 行只能解释为这个已绑定缓存来源，不能计为本次新 withJac 工作。

## 4. 原十试步与源身份的确切范围

沿原 frozen engine 的 stable-graph/recovery 处理后的 runtime core，唯一改变是：

1. 第一次 evaluate(states,target,true,scales) 读取已绑定的 actual 28 缓存基态。
2. 第一次 correction(ev,states,target) 读取已保存的原 577 节点方向。
3. 在原十试步之后、原 exhausted-line-search 错误语句之前插入保存/计划停止观察器。

每项替换必须恰出现一次；反向去掉这两处替换与一处插入必须恢复原 runtime core 全文。原十档循环本身逐字保留，SHA256 为：

~~~text
603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99
~~~

实际规则仍是原 lambda=2**(-k)，k=0,…,9；原 states+lambda*delta；原 evaluate(trial,target,false,scales)；原所有 momentum D/S/A 与 root/其余域异常；原严格 test.norm<ev.norm；原 trialDiagnostic 和 accepted-trial recovery progress。不添加 Armijo、额外缩步、容差或 guard，不用新逐步矩阵残差代替旧完整非线性 readback。

saved direction 的 maxChartCondition 为 null，因为这次没有计算原 Riccati chart；不填旧 chartCondition，也不虚构全矩阵条件数。

### 公开包装与内部 solve 的身份勘误

源码核对发现，原 split adapter 对外的 dn.tail.solve 是调用内部 solveQ 的不变箭头包装。其真实 Function.toString SHA256 为：

~~~text
283de19115a958e0268f6a719e17c53aa9c0a5473692d8a22aa09bf28b81378a
~~~

这恰等 actual 28 保存的公开函数身份。被本次三处变换改变的是内部 core solve。因此，先前“旧 generic 的公开 live snapshot 必然因这些插入失败”的静态判断不成立。本新源没有为绕过它伪造 Function.toString，也没有修改原公开函数哈希核验。

本入口分别记录：

- 实际公开包装的真实 source 和 SHA，与原 live snapshot 直接比较。
- 即将被实际编译的内部 solve 源码切片及 SHA。
- 从该切片精确反向移除三处变更后的原 runtime 内部 solve 切片及 SHA。

断连前纯源码核得到内部 instrumented SHA 为 14422c0add9aa8c4821a13307e2f4c93f022f86dd046e33343611e74960ab904，恢复的 runtime 内部 solve SHA 为 d7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615。二者不是上述公开包装的 SHA。core-instrumentation.json 与 actual-replay-method-identities.json 将完整记录这些各自的身份和可逆关系，不将源码切片冒作另一个函数的 Function.toString。

## 5. 输出与停止语义

每个已观察到的真实原 trial 保存 index、lambda、baseNorm、trialNorm 或原 rejection kind/error/stage/rawCell/rawSegment；关键数值同时保 binary64 bits。若原回调给出失败段输入，另保完整 224 项原始 f64le gzip，负零和非有限位模式不会被 JSON 改成普通零。

若原严格下降接受某一步：

- 原 accepted callback 和 recovery-only progress 先照常执行。
- 保存全 577×224 selected-state.f64le.gz 和完整 checkpoint。
- checkpoint 绑定原 H/参数/rawNode、actual 28 基态、actual 41 step result、真实新 matrix identity、完整方向及限制方向。
- 观察器抛 VISIBLE_NATIVE_RAWCELL0_STEP_TRIAL_REPLAY_ACCEPTED_STOP_V1，原 worker 的原 catch 如实返回 failed；launcher 将它单列为计划诊断停机。
- 仅 trial_accepted=true；success、converged、native_tail_response、native_accepted、task_completed 仍为 false。下一 Newton、endpoint Jacobian 与 fresh audit 没有执行。

若十步都拒绝，保留原 multiple-shooting line search failed at … 错误与全部十项读数。若在完成前出现 I/O、身份或其他异常，只保留实际记录；不补造遗漏试步，也不将观察到的回调数冒作确定的完整调用数。此时 original_no_J_trial_evaluations 为 null，另给 observed_complete_original_trial_callbacks 和部分执行标志。

原协议 request 仍为 jacobian=true,audit=true，以保持原请求身份；计划停机发生在末端 J/audit 之前，报告明确二者均未计算。没有把候选设成 worker 的已接受 last 或 response cache，也不伪造跨进程 tangentPredictor。

## 6. Actions 调用

STEP41 为实际 41 完整提取目录；DIRECTION 为未来实际完整动态 step-system 方向目录。后者 result SHA 必须从真实回执读取，不用示例哈希代填。CAPTURE28 与 STEP41 的大输入仅从已钉公开 artifact 恢复。

~~~bash
python "$C/geometry_20261114_native_rawcell0_step_trial_replay.py" \
  --failed-directory "$TOPIC/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$TOPIC/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$TOPIC/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$TOPIC/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$TOPIC/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --capture-directory "$CAPTURE28" \
  --step-directory "$STEP41" \
  --step-result-sha256 6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf \
  --direction-directory "$DIRECTION" \
  --direction-result-sha256 "$ACTUAL_STEP_DIRECTION_RESULT_SHA256" \
  --direction-source-file exact_20261114_rawcell0_step_equilibrated_correction.py \
  --direction-source-sha256 30a467e8f08d73fcdcd8a69b2d911e0d9f57489c3397c21c775ed1ec4f6cabe6 \
  --source-topic "$REPO/topics/visible-flexible-closed-surface" \
  --node-heap 6144 \
  --out "$OUT/native-rawcell0-step-one-line-search"
~~~

输出目录必须独立且为空。握手沿原 TailClient 的 complete config/source/ready/capacity；Popen 只对唯一 frozen worker 加载新 hook，其他子进程不受影响。所有科学数值只由本公开仓库 Actions 执行。

## 7. 实际已做与未做的验证

已做的是源码和字节工作：原 generic 两源 SHA 核；新 hook 断连前 Node --check；生成 engine 源的 Node 语法检查；三处字符串变换与原 runtime 全文恢复；内部 solve 和公开包装身份区分；原十试步正文 SHA；动态 consumer 与两 checkpoint 的字段合同只读核。hook 恢复后的完整 SHA 恰等这些本地检查的最终对象；恢复后另用 V8 仅解析移除 ESM 声明的语法，没有执行模块。

Python 之前草稿通过 AST；最后 schema/doc 修正后的本地 AST/hash 调用因环境失联没有返回。此处只登记恢复 blob 的完整身份，不补写“最终 AST 已过”。没有任何新 direction、no-J trial、完整 native、endpoint J 或 audit 的成功结论。本接口交付本身不改变课题原完成标准。
