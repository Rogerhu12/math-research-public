# 保存的节点 G 方向回到原十试步：独立消费接口

2026-11-14。本接口消费新节点 G producer 已经恢复为原 Q/Pi 坐标的完整方向，再取原 577 节点限制，使用原 native 的十档线搜索。它不导入或实例化 RawCell0GaugeSystem，不重新形成 G、Jacobian 或线性方向，不把新 producer 的输出冒称原 30a467… 逐步 producer 的产物。是否调度试步由真实方向结果决定；接口存在不表示方向已经准确、试步已经运行或 native 已接受。

## 1. 冻结文件与身份

| 文件 | 字节数 | SHA256 | Git blob |
|---|---:|---|---|
| [geometry_20261114_native_gauge_trial_replay.py](../computations/geometry_20261114_native_gauge_trial_replay.py) | 39181 | 10b3689a3dfa453082bae370f8f63e5f0ef1932a3a59e69930ed01949d24dd66 | 9a0aecdf0dc3751b6f79695e1e0c16d1b67cf932 |
| [geometry_20261114_native_gauge_trial_replay_hook.mjs](../computations/geometry_20261114_native_gauge_trial_replay_hook.mjs) | 62615 | 6d40cc9c14abb5c8dbcc85d66aff51ef1d4535dadd09e60d8f01d9f6c3f8c4ab | de0299f031b337aea4fadbf582e10eeb9c1b3d5f |

执行环境断连期间，依据根 README 第 8 条，仅从已保存及公开的冻结源码文本生成小于 100 KB 的独立 Git blobs，没有自行更新分支。上述是这两份实际交付文本的身份，没有捏造不可访问的本地检查或文件 SHA。原 step-trial、generic trial、原 worker、原 engine、G producer 与原动态 step-system 源均未改动。

本入口固定绑定以下新旧来源：

| 来源 | SHA256 |
|---|---|
| 新 G system exact_20261114_rawcell0_gauge_system.py | 24a51a4e804859bcdbed78b133599a073c6a0a890039e5fe5500281ef7e90b92 |
| 新 G producer exact_20261114_rawcell0_gauge_equilibrated_correction.py | 16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00 |
| 原动态 RawCell0StepSystem | fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81 |
| 原 actual 41 result | 6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf |
| 原 1372 段矩阵身份 | e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521 |
| 原 actual 28 result | ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7 |

原 actual 28/41 数值与审计范围分别见已有实际结论及 [actual 41 原步捕获](2026-11-14-actual-request41-rawcell0-step-capture.md)。新方向 producer 的结果身份必须通过 CLI 提供，不能由文件名、Actions success 或摘要的有限性旗代替。

## 2. 三个不同对象分别绑定

接口分别保留：

1. 原 1372 段保存矩阵及完整原方程身份。
2. 由保存的 G 系数、已保存变换块和显式 cut 行变换定义的新形成矩阵身份。
3. 已经从新坐标恢复的完整原 Q/Pi 方向及其 577 节点限制。

不把三个身份混成一个 matrix SHA。新 G 矩阵的浮点形成不声称精确等于原矩阵的实数共轭；恢复后的完整方向仍由 producer 对原 1372 段、原 sigma 的全部行作精确 binary-real 读回。旧原 576 长段矩阵不是本次已解矩阵，输出明确 original576_long_matrix_claimed_solved=false；旧长段线性缺陷不作为新表示方向的试步门。

### 2.1 实际 G 产物格式

完整结果为压缩文件 result.json.gz，schema：

~~~text
native-gauge-original1372-equilibrated-band-correction-v1
~~~

summary.json 只是小摘要。CLI 的 direction-result-sha256 必须是 summary.full_result.sha256，即 **result.json.gz 压缩文件的实际 SHA256**，不能用 summary.json 的 SHA，也不能用解压后的 JSON 文本 SHA。

输出清单 schema 为 native-gauge-original1372-output-arrays-v1。方向结果的四个字段仍为 step_delta、step_direction_checkpoint、restricted_old_node_delta、restricted_direction_checkpoint，但完整/限制 checkpoint 的 schema 分别为：

~~~text
complete-original1372-direction-from-saved-node-gauge-v1
complete-original577-restriction-of-gauge1372-direction-v1
~~~

两者的原输入键是 original_input_binding，不是旧 producer 的 input_binding；全部坐标明确 actual_coordinates_are_original_Q_Pi=true。新完整方向有 1373×224 项，原节点限制有 577×224 项。每行的 negative_zero_columns 参与精确 raw 字节恢复。

G binding 为 gauge-matrix-binding.json.gz，schema：

~~~text
native-original1372-saved-height-slope-gauge-binding-v1
~~~

它另绑定 node-gauge-anchors.json.gz、alpha/beta/eta 原始数组、869 个已形成的变化块、完整 1372 块虚拟流、显式 cut 行乘子、原 H/far/sigma/残差及 actual 41 来源。869 个变化块包含新段 868 的混合接口；其后 503 个段使用原矩阵块。这里没有将“G 在节点 869 后为恒等”误写成“段 868 不变”。

### 2.2 Python 的完整绑定

Python 在公开 Actions 内只实例化冻结的原 RawCell0StepSystem。该构造器消费保存的 actual 28/41 字节，并按原声明的 output-minus-node 规则形成原有限残差；它不调用 RHS、ODE、J 或线性求解。随后：

- 逐文件核完整结果、所有输出数组、G binding、anchors 与两 checkpoint 的真实大小和 SHA。
- 逐项比较 original_input_binding 与原构造器身份，核完整 oldToNew、原 H/far/sigma 与原残差 SHA。
- 核 G producer 和 G system 源 SHA、policy、formation、scaling 与实际维数。
- 读保存的 alpha/beta/eta 字节，仅作有限性、非零性、恒等后缀与显式 cut 乘子身份检查；不从 r/w 重新计算 G。
- 从 actual 41 的 field0 与 cut 末 field3 元数据重建节点 anchor 身份记录，核节点、原段/步、状态哈希、r/w/mu/port 字节；不重算几何量。
- 逐块流读已保存的 formed_changed_blocks 和其余旧块，核 1372 块来源、虚拟矩阵流哈希及 canonical binding SHA；不乘 GJG^{-1}。
- 完整恢复两 checkpoint 的有序原 Q/Pi 行、全部负零，逐字节核 raw 数组及 577 个 oldToNew 限制。

规范 JSON 身份使用与 producer 相同的 Python json.dumps：sort_keys=True、separators=(",",":")、allow_nan=False。不能用另一套 JSON 排序/浮点打印规则替代其 canonical SHA。

LAPACK 状态按真实新结构读取：顶层 lapack_factor_info 和 initial_solve.lapack_solve_info。它们及完整有限方向旗只说明产物存在，不说明方向质量。本接口没有追加 norm 门，也不以新坐标范数替代原方程范数。

### 2.3 Node 再核范围

首次实际请求前，Node 再核源/结果/清单、G binding、anchors、保存系数、原输入及 full/restricted 方向的完整字节关系。完整 formed 文件通过流式读取核 SHA，避免将约 349 MB 变化块一次放入内存。

Node 不导入 G 模块，不重新形成矩阵。对内部数值只进行已有输入恢复、位模式与身份核验；真正原非线性试步仍由原 native evaluate 完成。新 source pin、输出 schema、完整方向身份都独立记录，未套用旧 30a467… 结果身份。

## 3. 原基态、缓存与原十试步

沿 17/19/21/22/23 的同一完整非零 H 历史链，基态仍为 actual 23/28 的原 577×224 状态，raw SHA：

~~~text
6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8
~~~

原 sigma raw SHA：

~~~text
ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc
~~~

首次基态 norm/minA/minD 明确复用 actual 28 完整 withJac 缓存；原 norm 为 0.04177307820740199。本入口没有新算该基态，也没有重新计算原 correction。记录 new_baseline_evaluations=0、new_J_evaluations=0、new_corrections=0；第 0 个 progress 行不能冒称新 withJac 回执。

与原 engine 的稳定图/恢复处理之后的 runtime core 相比，仍只有三处精确可逆变换：

1. 第一次原 evaluate(states,target,true,scales) 读取已绑定缓存。
2. 第一次原 correction(ev,states,target) 读取保存的原 577 节点方向。
3. 在原十档循环之后插入保存与计划停止观察器。

原十档正文 SHA 不变：

~~~text
603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99
~~~

完整保留原 lambda=2**(-k)、k=0,…,9；原 states+lambda*delta；原 evaluate(trial,target,false,scales)；原 D/S/A 与全部 root/域约束；原 trialDiagnostic；原严格 test.norm<ev.norm；原 accepted recovery progress。没有增加缩步档、Armijo、容差或改变原验收函数。

完整原 no-J trial 使用旧 576 段实际非线性流。新表示的线性方向只通过 oldToNew 限制回到原存储节点；不能从新矩阵求解的线性缺陷自动推断它会在该真实原流下降。

### 3.1 函数身份与可逆源码

原公开 dn.tail.solve 是不变箭头包装；其真实 Function.toString SHA 仍为：

~~~text
283de19115a958e0268f6a719e17c53aa9c0a5473692d8a22aa09bf28b81378a
~~~

本次改变的是内部 core solve 的三处源码，不伪造公开或内部 Function.toString。完整保存 instrumented 内部源、恢复的原内部源和各自 SHA。

本次纯源码核得到：

| 源码对象 | SHA256 |
|---|---|
| 原处理后的 runtime core | f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f |
| 本 G hook 的 instrumented runtime core | a606d998ed529599d54520e639f243a97cd459de26d1299c9b1ba5447719fad3 |
| 本 G hook 的 instrumented 内部 solve 切片 | be7e34aac88f27c693e18a144607b49cbc4a2c985bbd2b4caac164c4ad728828 |
| 精确反向还原的原内部 solve 切片 | d7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615 |

恢复核对覆盖原 runtime 全文；原十试步正文逐字不变。切片 SHA 没有冒称另一个公开函数的运行时 Function.toString 身份。

## 4. 输出与计划停止

逐个原 trial 保存实际 index/lambda/baseNorm/trialNorm，或原 guard/异常、stage/rawCell/rawSegment，以及原回调可提供的完整失败输入和位模式。发生部分异常时，原 no-J 完成调用数为 null；另报实际观察到的完整 trial 回调数，不补造缺失调用。

若原严格下降接受第一步：

- 原 accepted callback/recovery progress 照常先执行。
- 保存完整原 577 节点 selected-state 与 checkpoint，包含负零和原 H/参数/rawNode。
- checkpoint 绑定原 actual 28、actual 41、原 1372 矩阵、新 formed G 矩阵、coordinate identity、完整恢复方向及限制方向。
- 抛计划标记 VISIBLE_NATIVE_GAUGE_TRIAL_REPLAY_ACCEPTED_STOP_V1；原 worker catch 如实返回 failed，launcher 将其单列为计划诊断停机。
- 只声明 trial_accepted=true；native_accepted、task_completed、完整 response、converged 仍为 false。

若十步都拒绝，保原 multiple-shooting line search failed at … 与完整实际试步记录。协议 request 仍为 jacobian=true,audit=true，但计划停止发生在 endpoint J/fresh audit 前；这两项明确没有执行。没有将候选伪装成 worker 已接受 last 或缓存响应，也没有捏造跨进程 tangentPredictor。

## 5. Actions CLI

以下仅是已冻结接口，不表示当前某个方向已经值得运行。GAUGE_DIRECTION 必须是完整新 G artifact 的提取目录，包括形成块、系数、anchors、所有方向 raw/checkpoint 与 manifest；不能只提供 summary。CAPTURE28 与 STEP41 也要求已钉完整 artifact。大数组只作 Actions artifact 输入，不进 Git。

ACTUAL_GAUGE_RESULT_GZ_SHA256 应从实际 summary.full_result.sha256 读取。

~~~bash
python "$C/geometry_20261114_native_gauge_trial_replay.py" \
  --failed-directory "$TOPIC/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$TOPIC/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$TOPIC/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$TOPIC/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$TOPIC/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --capture-directory "$CAPTURE28" \
  --step-directory "$STEP41" \
  --step-result-sha256 6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf \
  --direction-directory "$GAUGE_DIRECTION" \
  --direction-result-sha256 "$ACTUAL_GAUGE_RESULT_GZ_SHA256" \
  --direction-source-file exact_20261114_rawcell0_gauge_equilibrated_correction.py \
  --direction-source-sha256 16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00 \
  --source-topic "$REPO/topics/visible-flexible-closed-surface" \
  --node-heap 6144 \
  --out "$OUT/native-gauge-one-line-search"
~~~

输出目录独立且为空。单个新 worker 的原 config/source/ready/capacity 完整核对不变，Popen 仅增加本新 hook。退出码 0 仅表示这一个原线搜索已完成并接受一试步；不代表完整 native 求解成功。

## 6. 实际静态验证范围

已完成：从公开/已保存文本重建源身份；纯 V8 解析移除 ESM 声明后的 hook 语法且不执行模块；原 frozen core/engine 文本 SHA 核；两处调用替换及一处观察器插入的唯一性与全文精确反向恢复；原十试步正文 SHA；公开包装与内部切片身份的区分；新 G 源/schema/文件字段的只读核。

没有执行最终 Python AST/import，因为执行环境不可用；没有据此写“最终 Python AST 已过”。没有在本地执行 constructor、RHS、RK、J、G 形成、线性求解、norm 或非线性试步。后续 Actions 的编译与真实身份检查如实决定是否可以进入原试步；本组件不修改本题科学完成标准。

同原 RK 级间坐标换算的数学边界见 [R271](../results/R271-discrete-RK-stage-gauge-covariance.md)：已形成矩阵的节点共轭、原 RK 各级的等价递推，以及连续变换方程重新 RK 是三个不同对象，本 trial 只消费 producer 明确保存的前一对象恢复出的原坐标方向。
