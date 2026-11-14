# single-target s=1 闭失败记录的独立核查

核查者：/root/coupled_prefix，2026-11-09。

**结论：闭记录、输入身份和拒绝路径核查 PASS；这次实际请求失败，不能生成 single-target readiness。** 本稿不判断该目标是否存在正分支，不安排新求解，也不接管原 continuation02。

本审查者编写了薄 runner，故这里不把自己的记录核查冒充该 runner 的独立源码审查。runner 的全文独审由 tail-theory 提供（SHA2ba599331ee9ac7e22b9af732abac7a9dc9df31018dd20244849731945708ac4），root 也已全文核查。本稿另外核对由 root 实际执行并关闭的输入、响应、退出收据和原失败代码路径；没有复跑其数学求解。

## 1. 实际执行身份及退出码

实际运行 stem 是 prefix-harmonic-s1-audited-target-01。root launch SHA08e2ffc4aa3d73240962cc71315e3be3d941f3cde2c350d050106dd02b66c707，observed-execution SHA88c823cbbc09b536da2bf3707445055de55c881e8c108274d5c3bde716e15c73。

独立重新哈希了 launch 的 **98项来源**及观察记录的 **6件闭输出**，集合、字节和 SHA 全部吻合；实际 argv 与原 reproduction 一致。source-root、已审 v2 runner、原目标、逐模 warm 和当次新 config 的绑定均相符，原始响应的八源逐一重核。

退出须分三层读取：

| 层级 | 真实记录 |
|---|---|
| root 工具会话 | session28395；write_stdin 最终收据75bf61；实际 exit2 |
| root 直接等待的 runner 子进程 | 实际 exit2；总用时16.028842021005403秒 |
| 原 WeightedTailPort worker | finally close 后实际 poll 为0 |

root 的工具观察字段明确说明从最终工具返回取得退出码，而非由文件存在或进程缺失推断。reviewer 读取并核对这份闭观察，不声称自己重新持有或轮询了 root 的工具会话。正常 worker 关闭仅表示协议结束，不构成数学成功；runner 如实非0退出。

## 2. 实际请求和问题保持

实际 config 与绑定原 config 的 canonical 差异恰为五个 I/O 键。原 maxIterations36、solveTolerance2e-9、M15/N256/depth12/parts8/steps32以及原 source 不变。floor 和 correctInitialBoundary 键仍未覆盖，保持原默认值。输出路径全部属于独立 stem，输入仍是此前明确 UNSOLVED 的逐模 warm。

实际 request 精确等于固定 affine goal、jacobian=True、audit=True，且与 reproduction、trace 请求逐类型相同。这里的 True 是**请求**语义，不能据它说完整 Jacobian 或 source audit 已返回。

trace 恰有三个事件：

1. warm_initial_state，来源为已审逐模输入；
2. call1 的唯一实际 request；
3. call1 的 failure：Error: momentum Newton line search failed。

没有 iteration 事件。原程序只有在完整基点评价返回后才发送带状态的 progress；本次未形成这样的保存记录。原 trial diagnostic 是后续线搜索路径的记录器，因此本次没有 trials、stage-input 或 iteration CP 文件，与关闭数据一致。

## 3. 原失败包与 wrapper 拒绝

原响应文件 SHA：

    8205dcefb590623700d14dd111bbf0ef6f9cd6defb8e9802de2e12dbad090c8e

它的 response 精确只有 failed、lastIteration、checkpoint 三键；失败文字如上，后两项均为 null。原包没有 converged、residual、jets、heightJetJacobian、history 或 audit。client 错误字符串中的 residual=None 是对缺字段的格式化显示，不是向原包补了 residual 字段。

原 wrapper summary 为 SINGLE_TARGET_NOT_ACCEPTED_PREFIX_UNSOLVED；actual_request_count=1，validated_target_response 为 null。原始失败包先由原 client 保留，随后 client 抛出实际 FloatingPointError；success-schema 验证另因 No complete original successful response schema 而拒绝。两项错误都与原代码路径一致，没有将 schema 拒绝伪装成一次新的数学测试。

由于原 checkpoint 为 null，不能将输入 warm 或它的旧来源 call9 当作本次新求解状态。没有可接续的本次新 shooting CP，也没有足以作为 prefix 真尾输入的成功响应。条件式接续说明因此仍然只是条件说明；本轮没有生成 readiness、coupled config 或启动绑定。

## 4. 可得结论的精确范围

本次只支持：这个特定逐模初猜在原目标请求形成首个完整迭代基点记录之前，发生了原 momentum Newton 线搜索失败。

原闭包没有保存失败 stage、RK 子点、角位置、初始 normalized residual 或 minA。不能从运行耗时、旧 call10 的位置或以前的 A-floor 现象推断这些值，也不能声称已经定位到默认 root seed 或某个具体 guard。请求中的 audit=True 不支付任何未返回的 audit 数值。

同一目标的其它初猜、原连续延拓路径及正分支存在性不由这一失败决定。本稿没有读取原02的活动 trace，也没有修改它的状态；root 所持原流程继续独立处理。

## 5. 独立只读核查与复跑

自有 scripts/db6f-prefix-review-single-target-closed-failure.py 实际工具退出0（收据ec7b4f）。它只用标准库读取 JSON/gzip、哈希和比较闭元数据；没有导入或调用 worker、engine、root、flow、RK、DN 或几何后端。

    cd /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface
    python scripts/db6f-prefix-review-single-target-closed-failure.py \
      --out notes/2026-11-09-db6f-prefix-review-single-target-closed-failure-independent.json

须使用新输出路径。报告绑定98来源、6输出及实际 root 收据，重核了原 config／目标／八源、原失败 schema、三事件 trace 和没有新 CP 的事实；不包含候选或 shooting 数组。其 PASS 只是这些闭失败事实与身份的核查结论，不是数学成功。
