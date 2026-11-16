# R531 — 完整 current576 并行 cellFlow 的来源、调用与必要读回接口

作者：ChatGPT / amplitude（AI-assisted）  
日期：2026-11-16  
可信度：**已证明，限已列来源组合及条件命题；新并行源码尚未在 Actions 执行。** 本接口交付可实际接入的源、完整 literal 生成计划和条件证明，没有新的 workflow、已派发 request、并行性能、数值完成或接受结论。未来 request227 / R538 / R539 仅为协调预留。

## 1. 实际对象与交付范围

R531 从已刊 request224 的完整 binary64 current576 链派生。224 的发表提交为 498c03a7753a6f6caf66b563b2319cd42a447aaf，官方实际运行提交为 23176ac678ea92882fa38ec6ddcc09e98742ac89。本文不修改该运行，不继承其 H、J、数值末点或检查点。

唯一计算组织变化是：每次真实 withJ 当前场求值，将全部 576 个 cellFlow 交由 2–4 个真实工作线程；每个线程加载实际原工厂和 R523 flow。主线程按原 n=0,…,575 次序消费结果。原 noJ、原 RK/cusp、226 维状态、224 个形状方向、两个 mean、R273、全 338×112 响应、FD 与 full-DN 原门继续由原调用链支付。[条件证明](../results/R531-complete-current576-parallel-cellflow-source-and-conditional-equivalence.md) 给出准确边界。

此处“原 224”是明确的字节来源子合同。新的公开 Actions 运行必须记录自己的 run/source/request；原祖先号 224 不能被称为本次实际运行号。source 数量也是明确集合计数，不代替任意动态 import 的完整性证明。

## 2. 发布文件与不发布的展开视图

除本接口外，公开发布以下六件。源码与计划位于 computations，证明位于 results；临时交付 manifest 只用于文件传递，不是科学输入，不应入 Git。

| 角色 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| parent | geometry_20261116_complete576_parallel_cellflow.mjs | 21284 | 9434c8f003b19745446fbc798f12efc464719474bad3385553cff3368be225aa |
| pool | geometry_20261116_complete576_cellflow_pool.mjs | 29074 | ab6dff37f021cee82ace600ebc1e48ce32285f41a7a1f18b6f891aecff86369c |
| reader | root_20261116_parallel_cellflow_necessary.py | 20373 | da99e600bbfb4fd557890dae335c59135a00f2ad179b8050b9f5018cf0080c95 |
| generator | root_20261116_parallel_cellflow_source_views.py | 10495 | b628d09aa75b0f3942549a2f9f24b4fa5cd618766c82b76adb565a64254e9149 |
| plan | r531-complete576-parallel-cellflow-source-plan.json | 63026 | 499616558f05865726aefa63c10842fa1a8a73172da557a18dbf7b8d574e61b7 |
| proof | R531-complete-current576-parallel-cellflow-source-and-conditional-equivalence.md | 17455 | b0a7c748c44183de7921a0011fefe2713cbc3867425cdc87b8a87f9256b0dee9 |

新计划 schema 为 R531-complete576-parallel-literal-source-plan-v1。其 8 个视图从当前 job 内真实生成的原 224 文件逐字派生，记录每份 base 的 bytes/SHA、全部 before/after/count、输出 bytes/SHA。共 93 项 literal 应用；生成器校验实际次数和完整输出身份，不导入或执行科学模块。

| 角色 | 实际新 basename | bytes | SHA256 |
|---|---|---:|---|
| system | exact_20261116_parallel_input_support_contracted_trace_r273_current576_system.py | 29888 | 1b51c672277ab1e0919bb00392bfc2634e36e7e64caa58b43d62d6781ca3385a |
| qr | exact_20261116_parallel_input_support_contracted_trace_r273_current576_chain_qr.py | 22153 | 9b20fab094c12c471f8c61a968a0dde0249ee1a1e71c30cdd2bb88a46bfc1b42 |
| hook | geometry_20261116_parallel_input_support_contracted_trace_r273_tail_client_hook.mjs | 60059 | 6911a4b3224dc5b726d435f3b44e4127c05e8d8a15f6cdaccaf8872c932234ba |
| client | geometry_20261116_parallel_input_support_contracted_trace_r273_tail_client.py | 23870 | a8571e0c47c8f2e264c76ce3ee1554ca19cbcaa0366fbc6b7fdc2fe71e9856b2 |
| height | geometry_20261116_parallel_input_support_contracted_trace_r273_height_path.py | 24104 | 2c92d191b8cedecf235176209cc6eb7d432622d0f8f416bfe4572c1c12584a3b |
| full112 | geometry_20261116_six_control_parallel_input_support_contracted_trace_r273_full112.py | 52339 | 525be2072fee4f53122d5802ef57d8b00f24e7b08408a3ed0441fd1872686311 |
| runner | root_20261116_parallel_input_support_contracted_trace_r273_run.py | 15716 | 4c7e13df26c39ab881ac878429150b79e7536e55908d3ae69d097bba3c4afe19 |
| readerview | root_20261116_six_control_parallel_input_support_contracted_trace_r273_scalar_readout.py | 50519 | fb8899e0da24ff8b6b7d5e728b3906c5096f57e0e93c0e511bfc506ddd32ea96 |

上述八份展开全文只在 Actions 临时实际 computations 生成，不作为 Git 中已有文件下载，不以旧 basename 或旧 SHA 冒充新源。所有旧文件原字保留。完整 193 源分为：

| 集合 | 数量 | 实际责任 |
|---|---:|---|
| 原 224 公开源 | 150 | 当前 job 从公开来源按原 SHA 读取 |
| 原 224 生成源 | 31 | 从已刊各原计划真实重生，并核全文 |
| R531 新公开 helper | 4 | 本接口 parent/pool/reader/generator |
| R531 新生成视图 | 8 | 本计划逐字派生，完整新身份 |
| 合计 | 193 | 154 个公开源、39 个生成源 |

原 78 个数学源的 source-topic 恢复、四个原字节输入、两份原 native ready 输入仍是各自独立的原合同，不被这张 computations 数量表替代。

## 3. 字节祖先、参数与输入

原 request、recipe、生成器、计划均保持：

| 文件 | bytes | SHA256 |
|---|---:|---|
| public-six-control-input-support-contracted-trace-r273-request.json | 88551 | 6aa2f23f2e92f326ea2bf17b58f084c28580f5a44420c8cf47816597e9e5b980 |
| actual119-batch3-input-support-contracted-trace224-lambda0p001-recipe.json | 21539 | 0c9fa04642835dd37f9da5aeb03a35abae4be4e75283c3e2203a73dcec6544ea |
| request224-input-support-contracted-source-plan.json | 36611 | 9a184000c0b8e81dc3d247e39b873a2c66cc7be4a42cfa01090df8ebf2fd7326 |
| root_20261116_input_support_contracted_source_views.py | 23213 | 7b83c7c69b155bb99d402f9d03e24dbb11bf0d57ab239c1d23c9839d2e583f1f |

数学初猜顺序仍为 p1,p2,p3,theta1,theta2,theta3，全部原字：

~~~json
[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]
~~~

活动坐标为前三个 p；后三个 theta 冻结；lambda=0.001。新程序重新产生原 fresh-circle/low-three 初猜，不能以实际211正高度接受、实际224尚未返回的状态或已删 raw 作为新输入。

四个原字节输入保持：

| 角色 | bytes | SHA256 |
|---|---:|---|
| accepted | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail_anchor | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail_config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

原高度路线从零开始，initial_positive_increment=0.015625，接受后倍数 2，maximum_increment=0.25，maximum_bootstrap_requests=64。零点和中间请求的外层 jacobian=false，末 H 请求 jacobian=true；这不省去求解器内部实际需要的完整切向、mean 或 predictor。首次确认的正高度原数学拒绝停止；资源、来源、协议或未分类异常不冒原数学拒绝。

原数值与资源政策如下，R531 未另填数值：

| 原项目 | 值 |
|---|---|
| modes / angular quadrature | 112 / 2048 |
| stages / shape columns / state entries | 576 / 224 / 226 |
| native iterations / noJ trials / tolerance | 32 / 10 / 2e-9 |
| full-DN outer iterations / inner trials | 8 / 17 |
| RMS / boundary / boundary FD tolerance | 1e-6 / 1e-11 / 5e-5 |
| max_nodes / material angles / physical angles | 1200 / 4096 / 4096 |
| original jac_workers / main Node heap MiB | 2 / 6144 |
| original science clock | 18000 seconds |
| original science-step / compute-job limits | 330 / 350 minutes |
| original rule-sync interval | 2700 seconds |
| R273 eta / factor workers / factor byte cap | original CLI “1” / 2 / original 2 GiB |

R273 的全部 577 个 penalty blocks、129248 行、原全列因子/回代及剩余时间和 transport reserve 原字保留。上述内容继续由原 recipe/request 实际绑定；future outer 必须声明并行线程资源，它们不能藏进原 recipe 后仍用旧 SHA。

## 4. 原实际 HERE 与两层生成顺序

首先在新 job 中按原公开入口恢复 224 来源子合同。原生成器的公开输入必须仍位于实际 GITHUB_WORKSPACE/topic/computations；原隔离临时输出仍使用其明确的祖先 namespace：

~~~bash
python "$VISIBLE_PUBLIC_COMPUTATIONS/root_20261116_input_support_contracted_source_views.py" \
  --request "$VISIBLE_PUBLIC_COMPUTATIONS/public-six-control-input-support-contracted-trace-r273-request.json" \
  --expected-request-sha256 6aa2f23f2e92f326ea2bf17b58f084c28580f5a44420c8cf47816597e9e5b980 \
  --public-computations "$VISIBLE_PUBLIC_COMPUTATIONS" \
  --out "$RUNNER_TEMP/visible-original64-input-support-contracted-trace224/runtime-source-views/computations"
~~~

原 generator 在本次 job 真实生成旧 31 份、复制原 150 份，写 source-views.json，设置 VISIBLE_COMPUTATIONS 与 VISIBLE_RUNTIME_SOURCE_VIEW_RECEIPT。固定字符串 224 是该字节子合同的目录/来源名，不是重新使用旧 run 的文件。

然后将本次四个新公开 helper 按本接口完整 SHA 复制进**同一个实际 VISIBLE_COMPUTATIONS**，并调用新生成器：

~~~bash
python "$VISIBLE_COMPUTATIONS/root_20261116_parallel_cellflow_source_views.py" \
  --computations "$VISIBLE_COMPUTATIONS" \
  --plan "$R531_PLAN_FILE" \
  --plan-sha256 499616558f05865726aefa63c10842fa1a8a73172da557a18dbf7b8d574e61b7 \
  --out "$R531_FRESH_PREPARATION_DIRECTORY"
~~~

这里两个 R531 路径由未来 outer 显式给定；receipt 输出必须是本 job RUNNER_TEMP 下新建的自有目录。生成器要求公开 Actions 环境、真实 repository/run/source/attempt、实际 VISIBLE_COMPUTATIONS；源码不在别处生成后标记为旧 HERE。

生成顺序为：先核真实四 helper 和八 base，按完整 literal count 生成新名，核新全文 SHA，最后提交 receipt。已有新名只有完整字节相同才可记为实际已存在；旧科学名不覆写。新 receipt schema 是 R531-complete576-parallel-actual-source-views-v1。成功后环境中增加：

~~~text
VISIBLE_R531_SOURCE_VIEW_RECEIPT
VISIBLE_R531_SOURCE_PLAN_SHA256
~~~

真实调用者使用：

~~~python
bind_prepared_views(
    actual_computations,
    expected_plan_sha256,
    actual_receipt_file,
)
~~~

它重新核当前 job/context、真正 HERE、生成器、计划、四 helper、八 base/输出及完整 receipt。原 181 来源绑定和新 12 来源绑定分别保留；不能只通过新 plan 的计数就略过祖先源。

此生成层没有数值运行或自己的科学钟。future workflow 必须保留原单次 namespace/18000 秒科学 owner 的实际来源与起点；不能在多次 H、迭代或 worker 启动时重启 deadline。源准备时间、原 step/job 上限和科学 owner 起点应如实分列，不能把 source-only 计划称为已执行的科学阶段。

## 5. 新真实 wrapper 与完整原求解入口

原 224 wrapper 的 ENTRY/CLIENT 硬 pin 不会自动选择新 full112。第八视图因此是实际必要调用者，不是额外包装仪式：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" \
python -u "$VISIBLE_COMPUTATIONS/root_20261116_parallel_input_support_contracted_trace_r273_run.py" \
  --request "$VISIBLE_COMPUTATIONS/public-six-control-input-support-contracted-trace-r273-request.json" \
  --recipe "$VISIBLE_COMPUTATIONS/actual119-batch3-input-support-contracted-trace224-lambda0p001-recipe.json" \
  --inputs-directory "$VISIBLE_MATH_INPUTS" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --out "$VISIBLE_BASE/execution"
~~~

wrapper schema 为 R531-complete576-parallel-owned-process-wrapper-v1。它同时绑定原 source_view_binding 与新 actual_parallel_source_views，ENTRY 真指 525be207…、CLIENT 真指 a8571e0c…；状态中分列 actual_request、immutable_source_request_ancestor=224、真实 run/source、wrapper/adapter/client SHA 和完整 argv。

future outer 必须提供：

~~~text
VISIBLE_R531_ACTUAL_REQUEST
VISIBLE_R531_CELLFLOW_WORKERS
VISIBLE_R531_CELLFLOW_WORKER_HEAP_MB
~~~

前者是未来实际 request 的明确值；后两项是本次真实资源选择。R531 不预填其实际值，不声称它们已在某次 job 使用。

原 --out 必须为 execution 根；wrapper 自己建立其下 science 与 factors。不要把 --out 改成 execution/science 后仍让 reader 读取旧层级。原规则 owner、Popen start_new_session、PGID/SID/startticks、deadline、signal、终态 stop/reap 等 body 均沿原 wrapper 保留；events 显式改为 R531_parallel_height_path_full112_launch / R531_parallel_height_path_full112_process_returned。

实际新 full112 CLI 与原 full112 相同：

- 必需 --recipe、--accepted、--prepared、--tail-anchor、--tail-config、--out、--work、--expected-recipe-sha256；
- 科学运行使用真实 --tail-client、--expected-tail-client-sha256、--tail-source-root；
- 仍传原 --jac-workers、--max-nodes、--material-angles、--physical-angles、--node-heap、--outer-iterations。

full112 schema 是 R531-six-control-parallel-cellflow-three-active-nonzero112-physical-DN-v1，recipe schema 仍为 explicit-six-control-input-support-contracted-trace-r273-height-path-nonzero112-recipe-v1。完整原 recipe 同时是不可变的数学政策输入与旧实现 provenance；其旧 native_correction 来源字段不冒新生产者。实际代码从新 PINS、真实 client argv 和 source receipts 选择，数值 policy/height 参数从原 recipe 读取；没有在绑定后静默修改 recipe。

此 full112 仍先真实完整 H 路线，再实际原 FD、原 complete-band full-DN main、原最终响应与 audit。没有“先证明全解析 338×112 才准运行”的新门；原混合响应合同保持。

## 6. 同次 profile capture 与真实线程工厂

parent helper 的公开入口：

~~~javascript
const make = await loadParallelCellflowConstructor();
const pool = make({
  output,
  spec,
  sourceFiles,
  workerCount,
  workerHeapMb
});
const result = pool.evaluate({
  cells, states, target, scales, M, K, depth, steps, options, context
});
const current = pool.snapshot();
pool.close();
~~~

hook 的实际闭包把真实 cells、states、target、scales、完整 M/K/depth/steps 和原工厂 options 传入。原 options 包括 modes、spacing、quadrature、该 cell 的 mu、原 orientation/projectionFloor、cusp 选择。每次 H/iteration 重新绑定实际输入字节，不复用旧场的 J、旧 profile tape 或旧 trial 返回。

主线程先按原 stage / ordinary step / cusp substep / RK a,b,c,d 的顺序实际调用当前 profile。重复 midpoint 是原调用顺序的一部分，照样调用。profile 的真实 cache 命中、淘汰、插入顺序由主线程原调用产生；线程只按该次完整值序列消费。不得把任意有副作用 callback 的全程序等价从这个已核具体 plain-number profile 推出。

实际已核 profile 返回字段是普通数值；完整成功路径保有限词、负零、字段取值与原调用顺序。capture 全部后才开始分派，会改变异常发生前已执行的 profile 前缀和工作量。这个差异单独记录为 preparation partial，不宣称任意失败的副作用顺序、耗时或资源前沿与串行相同。

协调 child 与原主 Node 同进程组/会话，由它创建 2–4 个 worker_threads。每个工作线程：

1. 绑定本次真实 source files、run/context 与 capacity/source receipt；
2. 加载原 capacity loader 和实际 R523 finite-trace loader；
3. 调用真实 Fourier-root split factory，建立对应当前 engine；
4. 按固定 engine_index mod worker_count 归属接收阶段；
5. 同 worker 内按原 n 递增执行完整 flowStateWithJacobian；
6. 返回完整 226 状态与 226×224 J，以及实际计数/last_observation。

不会在线程中 import 原完整 stdin 协议 worker，因而不会重复启动父端协议循环。原 source-topic 不是传入同名伪 JSON；sourceFiles 真指已恢复的文件、bytes、SHA。

## 7. 完整结果归并与等价边界

主线程只在完整成功时按 n=0,…,575 消费 stage 输出。原 evaluate 中残差、边界、norm、端口和两个 mean 的形成/加法顺序继续保留；每个非线性 root、方向收缩、R523 T 支撑运算、RK 和 cusp 内部算术由相同实际 flow 源完成。

传输使用 V8 typed-array/raw 临时文件。它是本次实际数值数据，不是将数组压成 Markdown、拆成多个必要摘要或编码进 Git。有限 binary64 输入和输出词及 ±0 的保存属于所列条件证明；不声明跨序列化的 NaN payload 字节相同或对象属性布局等于所有原私有对象。

完整输出必须仍有 576 段、每段 226 状态和 226×224 J。源/维数合同用于识别真实输入输出，没有增添 residual、非零 J、秩、速度、有限性接受或其它数学阈值。

并行不消除以下未付责任：原舍入误差/严格区间责任、IEEE 程序导数与名义线性化的区别、邻域 root 分支稳定、full-DN 最终接受、准确全闭面或几何认证。R531 也不宣称一定加速；profile capture、序列化、I/O、线程复制和内存竞争均可能影响真实全链。

## 8. 资源、时间与进程退出

worker_count 必须显式为 2、3 或 4；每个 worker_heap_mb 至少 256 MiB，且 W×worker_heap_mb ≤6144 MiB。原主 Node 的 --max-old-space-size=6144 保持。工作线程的额外 heap ceiling 与主 Node 6144 分别报告；它们之和不是原单进程 6144 的总内存承诺。

Node resourceLimits 不覆盖所有 ArrayBuffer、外部 native 内存或全进程 RSS。每个线程仍复制实际 factory/runtime，额外 data/tape/result 消耗也真实发生。原容量与内存前提不降低；新 heap 参数不能称作已证明实际 RSS 低于某阈值。

worker 的 execArgv / NODE_OPTIONS 处理确保原主 Node max-old-space-size 不暗中覆盖显式线程 resourceLimits。主 runtime 的真实 Node 版本、源码、环境和线程参数进入 receipt。本实现依赖公开 Actions 的实际 Linux /proc 与继承的原 monotonic clock 合同；不声称所有平台的 Python / Node clocks 自动共用原点。

所有工作沿原 VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC 与原 R273 global_deadline_unix_ms；不按 evaluation、stage、worker、H 或 iteration 重置。资源异常不捕获后重跑原科学。parent.close 的 5 秒正常关闭等待与必要时同一实际 child 的 SIGKILL、额外 1 秒观察，仅为 transport/lifecycle；不是重新增加科学时钟。

主端记录 PID/PGID/SID/startticks，协调端记录实际线程 exit。/proc 中 Z/X 只表示没有活动 JavaScript 线程，不冒 parent 已 wait/reap。协调端监视原 owner 是否仍为相同 startticks；outer 原 owned-group quiet 是清理的最终真实依据。元数据写盘异常不能跳过 worker.terminate；无法证明静止时保留 raw。

## 9. 失败、部分执行与阶段地址

完整阶段地址列固定为：

~~~text
stage, rawCell, rawSegment, engine_index, worker_index
~~~

所有阶段在开始 profile capture 前建立地址。状态原字为：

~~~text
unvisited
assigned_not_started
started_without_completed_return
completed
stage_error
interrupted_without_completed_return
~~~

“分派过”不等于完成；“profile 已捕获”不等于 root/J 已计算。每次实际 evaluation 保存完整地址和所有已观察状态，连同 preparation 的已完成调用数及当前真实位置。缺失进度记录不补成零。

只有五条明确绑定的原 root 数值 guard 消息、真实 original flow 阶段、没有资源/来源错误标记且所有更小 n 已完成时，才可按原 n 顺序选择首个原数学错误。其它 RangeError、allocation、来源、transport、未分类 original-flow 错误保各自实际记录，不从“flow 抛错”直接升级成数值拒绝。

高 n 在低 n 错误被观察前可能已计算。必要 scope 保留这些实际结果/中断，不声称并行走到和原串行同一资源边界。第一次协议或资源异常不触发另一轮科学“验证”；原 deadline/owner 负责停止。

## 10. 原始现场与必要读回选择

原 execution 根下的并行现场为：

~~~text
science/full-DN/true-tail-input-support-contracted-trace-r273/parallel-cellflows
~~~

其主要路径包括 launch.json、spawn.json、pool-owner.json、pool-ready.json、progress.json、events.jsonl、pool-closed.json、parent-close.json；worker-NN 下有真实 capacity/source receipts 与 stdout/stderr；evaluation-NNNNN 下有 evaluation-start、preparation-events、input.v8/input-identity、stage-NNNN.v8、error-stage-NNNN.v8、result、parent-consumed 与 parent-failure。

路径列举不表示所有文件已生成。reader 保留缺失、空文件、完整文件及截断事件尾的区别，并逐原文件记 bytes/SHA/实际读取范围。完整成功 state/J/RK 大数组仅在 Actions 临时现场，必要正文只保身份和完整范围；没有把全部数组读回说成已在 chat 逐值读取。

公共 reader helper 的 API 是：

~~~python
collect_parallel_cellflows(original_reader, relative, owned_quiet=True)
add_parallel_cellflows(original_reader, original_summary, owned_quiet=True)
~~~

owned_quiet 必须是原 owner 真实返回的 bool。新 helper 不建立独立接受 gate、frame、marker 或 cleanup；它在原单份必要摘要中加入一次 parallel_cellflows。

保留范围为：

| 对象 | 必要正文实际范围 |
|---|---|
| 每次 evaluation | 完整原地址、所有已观察阶段状态、preparation/返回/消费/失败 scope |
| 每个实际 worker/engine | 完整 source、归属、实际最后已观察 counters、flags、scope、fallback reasons、last_observation |
| 原算法统计 | 原 finite trace 全计数，R466 factor_contraction、R471 zero_nonlinear_flux、R523 linear_input_support 的完整字典和 14 计数 |
| 线程/进程 | 真 PID/startticks、worker id、观察到的 exit/terminate、original outer quiet |
| 错误 | 实际 error 类型、原位置、已选原日志范围及完整文件身份 |
| 成功大数组 | 全范围/尺寸/文件身份；不逐值刊出 |
| 在途统计 | 最后已收到快照；尚未收到的内部进度明确未知 |

主线程原 engine 统计仍在原 R273 section，线程统计在新 section。两者不相加后冒某个原单 engine 的累积字典，也不从 profile 数量补 root 或 J 数量。

固定语义表示只对明示的 addresses、contexts、source、status、engine metadata、完整 counter 与 observation 字典使用相等共享；相同的实际完整值及类型才可引用。各表保原行索引、原 key 集、列名、全部原值；缺键与 null、bool/int/float、负零不混合。counter 只拆固定的 zero_nonlinear_flux / factor_contraction / linear_input_support 三个原嵌套角色，其余所有键保在 main。这里不是任意对象树数字编码。

完整成功事件流在 Actions 逐字节扫描并绑定身份；必要正文选择原 scope/地址/结果，未逐条重复所有成功事件 timestamp。原普通错误文字仍沿 1600 字节、traceback 2400 字节的既存选择范围，不把这些前缀称为完整异常全文。

## 11. 新必要 CLI、frame、marker 与清理边界

真实新 reader 使用：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" \
python "$VISIBLE_COMPUTATIONS/root_20261116_six_control_parallel_input_support_contracted_trace_r273_scalar_readout.py" \
  --directory "$VISIBLE_BASE/execution" \
  --request "$VISIBLE_COMPUTATIONS/public-six-control-input-support-contracted-trace-r273-request.json" \
  --recipe "$VISIBLE_COMPUTATIONS/actual119-batch3-input-support-contracted-trace224-lambda0p001-recipe.json" \
  --rules-directory "$VISIBLE_BASE/rule-sync" \
  --compute-outcome "$ACTUAL_SCIENCE_STEP_OUTCOME" \
  --out "$VISIBLE_BASE/scalar-readout"
~~~

新 reader 的 quiet 进程名检查已明确匹配实际新 runner basename，未继续把旧 runner 当当前 owner。原 PID/PGID/SID/startticks、boot/UID 和未知进程责任不降低。

| 项目 | 字面 |
|---|---|
| body schema | R531-original64-parallel-complete576-necessary-readback-v1 |
| pool section schema | R531-complete576-parallel-cellflow-necessary-v1 |
| marker schema | R531-owned-complete-parallel576-necessary-readback-v1 |
| BEGIN | BEGIN_R531_PARALLEL_COMPLETE576_NECESSARY_SUMMARY |
| END | END_R531_PARALLEL_COMPLETE576_NECESSARY_SUMMARY |
| identity event | R531_parallel_necessary_summary_identity |
| body 文件 | scalar-readout/scalar-summary.json |
| 完成 marker | scalar-readout/readback-complete.json |
| 原 transport limit / failure exit | 90000 bytes / 70 |

打印 body 的 identity 不含末 LF；scalar-summary.json 文件和 marker 记录的文件 identity 含实际末 LF。原 summary 完整且 transport 完整才返回 0；否则 70。不能因新字段较多任意删除原必要值、扩大 90K、分包或再发第二 frame；本接口不保证任何未来运行的摘要一定小于 90K。

新 section 只在实际 owner 静止后读取。若超限、未知 owner、缺必要输入或未能完整返回，沿原规则保留 raw，不主动删除。future workflow 的 report、rules-parent 读回和 cleanup 必须明确核**新** reader SHA、body/marker schema 和实际身份；原224 workflow中写死的旧 literal不会自动变成R531。这部分属于未来R538入口实接，本文没有伪造它已经完成。

## 12. 未来完整入口的确定责任

R531 已提供真实计算 caller 和 bounded-reader；future outer 仍须实际完成以下串联，不能只换 request 标签：

1. 绑定本七件及原224公开request/recipe/generator/计划，保全部原输入/源恢复。
2. 在当前job生成原181源；再在同实际HERE生成R531八视图并核完整193集合。
3. 明确实际request标识、2–4线程数、每线程heap及其资源含义，不修改原recipe字节或钟。
4. 原规则owner真实调用新runner，其实际ENTRY/CLIENT与完整新source receipt吻合。
5. 原科学结束或中断后调用新necessary reader；所有缺失/partial均原样返回。
6. report与cleanup使用新marker/reader实际身份；原所有quiet/readback条件成立才清理。

这些是待完成入口的具体连接项，不是新科学前门。尚未指定本次实际worker/heap值，不预先填成功H/J/FD/full-DN状态，不宣称“全阶段返回”即原native接受。完整数学消费仍沿原门，真实资源结果和必要传输责任由未来Actions实际承担。

## 13. 来源依据与检查方式

条件证明逐项引用原 tangent core、原 root factory、有限 trace loader/flow、cusp 与 profile/cache 源。Node 线程与V8传输边界采用对应运行版本的官方文档：[worker_threads](https://nodejs.org/docs/latest-v24.x/api/worker_threads.html)、[v8 serialization](https://nodejs.org/docs/latest-v24.x/api/v8.html#serialization-api)。尤其 resourceLimits 不是全RSS上限，terminate/exit 与父进程reap不同；没有把文档能力当作这份新代码已实际执行。

本交付已做的工作仅为完整原源阅读、条件推导、纯文本literal应用与UTF-8/JSON/bytes/SHA身份生成。没有在本地 import、AST、compile、科学运算、数值对拍、fixture 或 benchmark。八展开视图可由公开计划完整重建；不为另存可重建diff而新增发布门。实际科学与原既定语法/编译步骤只属于公开Actions。
