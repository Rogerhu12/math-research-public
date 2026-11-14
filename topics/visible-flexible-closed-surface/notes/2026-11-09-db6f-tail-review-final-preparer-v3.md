# Final preparer v3：五行身份迁移的独立全文审查

2026-11-09，`/root/tail_theory`。审查者未参与 v3 实现。本轮重新读原 v2 全文、逐字比较 v3、核新的来源说明，并独立运行一次真实只读负门及一个自有静态/哈希检查。没有构造未来成功包、最终正 fixture、候选、配置或任何数学求解。

**结论：所绑定 v3 的五行 continuation03 身份迁移 PASS。** 原数学/schema/验收逻辑保持 v2；这不是 continuation03 已完成的声明。

## 1. 冻结来源与严格差分

| 对象 | SHA256 |
|---|---|
| 原 `scripts/db6f-prefix-prepare-final-m15-coupling-v2.py` | `8b235dfd97d558fc16e446b65bff2412642b041b9bbe6efb193fc88147426b81` |
| 新 `scripts/db6f-prefix-prepare-final-m15-coupling-v3.py` | `273bb318dfaa2839be8fa6c532152cf708880c13591ac0fcbae5f4e97bdacdb5` |
| 作者 `notes/2026-11-09-db6f-prefix-final-m15-preparer-v3.md` | `02f41feaf685cf44e267334cc20b85797ed1904b27c18382b389addda79560af` |
| 作者同名前缀 `-sources.json` | `f879f6b04cccae80736d8ab3f8ab735fad59925d8dd3cdac5e1f12975a4cf035` |

独立逐字检查显示，改变恰在原第 2、23、26、104、239 行：模块说明、CONTINUATION 常量、RESUME_LAUNCH 常量及两条 ValueError 文字。用明确的五次唯一字符串替换作用于冻结 v2，即逐字节得到 v3；没有额外换行、数值、函数或逻辑改变。全部函数 AST 在归一化两条错误文字后也逐项相同。

旧 v2 保持原 SHA。OUTPUT 仍是原 `outer-after-amplitude` 新结果前缀；新源没有改旧记录、原控制器、client、worker 或当前活动 03 文件。

## 2. 新身份如何进入原验收门

CONTINUATION 同时决定缺省值和唯一允许的 continuation stem。因此显式传旧 02 不能通过路径门；最终响应 regex、progress、reproduction、config、input-bindings 都自动限定在真实 03 名字下。RESUME_LAUNCH 现在读已审的真实 03 启动文件，取其 call15 初猜，而不是原 quarter 恢复记录。

03 launch 的 SHA 为 `0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c`。它保留已闭合 $s=31/32$ 的实际响应，首新目标为 $63/64$。本轮重新核其全部 83 绑定。真实 warm 的原 native 网格仍为 865×30、rawNode 0、72、…、864；新源仍从该真实 CP 比较原参数、状态数和 raw 映射，没有生成模拟 warm。

v3 保留原已审 restart mesh/cut-height roundtrip 检查、完整 command/restart 来源、progress/reproduction/input-binding 一致性，以及原 M15/spacing3/depth12/p8/steps32/N256/max36/tol2e−9/.05 guard。这里源文件中的比较方式也逐字保留，没有借本次身份迁移扩大或声称另行加强任意 JSON 的通用验证策略。

## 3. 原最终 DN 和真实 prefix 门保持不变

未来准备动作仍必须先取得真实 $s=1$ 的 `jacobian=true`、`audit=true` 请求与响应。原 residual 门、705 个有限 Jacobian 条目、17 个 cut-jets 字段、八项源 audit、实际完整历史基点及八个响应源哈希均未修改。source audit 与 full XYZ/连续全图证书的范围仍明确分开。

通过这些门之后，才从原 coupled config 复制并换五个 I/O 路径；命令仅换 `--tail-config` 和 `--out-prefix`，原 restart、自由 inlet/support 参数、原 BC、数值标志和空 warmup 列表不变。新的初猜仍须接受原完整 prefix 外层实际 DN/BC 校正；v3 没有把 continuation 目标冒充完整 prefix 解。

默认全模边界修正仍开启。旧 v2 原样保留，因此本次也没有混入零态 pilot 的 `correctInitialBoundary=false`。

## 4. 三层执行身份及外层 guard 的范围

原 controller 的 progress 记录 worker 退出。guard 的 child-execution 记录 controller child 退出。根的实际 tool receipt 则是外层工具真正结束的观察。这三者不相互代替。

v3 原观察门仍要求 `status=observed-process-completed`、`observer=/root`、`actual_exit_code=0`、精确 03 stem，并且观察文件绑定该运行最终 progress、reproduction、config、response。故：

- 根现有 started 记录不是完成观察；其真实 tool exit 仍为 null。
- guard 的 `CHILD_COMPLETED_AWAITING_ROOT_TOOL_OBSERVATION` 状态和 `tool_exit_observed_by_root=false` 不能直接通过该门。
- 旧 02 的根观察为 exit 1 且 stem 为 02，不能被重新标成 03 成功。它的 call15 warm 有效不意味着整个 02 clean exit。

另已重新核 root guarded-launch `9d2495ea6b48872b40a3c813f0c3076819f48a88f1f5bd9dc1b1ec33bfa49594` 的全部 89 绑定，并核其 `original_mathematical_command` 与 03 launch.command 逐项相同。作者 13 项来源账本也全部重新核验，三组共涉及 95 个不同已冻结文件。

作者说明准确限定：五行迁移没有新增一个独立的 guard-schema 检查谓词。未来根完整来源审查仍须把 guarded-launch、guard 源和实际关闭的 child-execution 同根观察一起保留、绑定，并核实际 child 结果；不能把这一未来审查责任说成新五行代码已自动完成。这里没有要求修改原验收算法或伪造任何结束记录。

## 5. 两次本轮实际检查

我独立实际运行：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-prepare-final-m15-coupling-v3.py --check-current-gate
```

cwd 为仓库根，receipt `3f8467` 实际 exit 0。其输出是 ready=false，理由为当前缺少 `...amplitude-continuation-03-reproduction.json`；files_written=0，solver_launches=0。该诊断模式 exit 0 仅表示负门结果成功报告，绝非数学成功。此次没有改动活动 03，也没有重新运行要求 O03 为空的恢复准备器。

另写 `scripts/db6f-tail-review-final-preparer-v3.py`，不导入 preparer/controller/solver，只做源码与冻结文件检查。receipt `113aad` 实际 exit 0；报告 `notes/2026-11-09-db6f-tail-review-final-preparer-v3.json`，SHA `46c28da69281b03ac0613ba0cbceb41d91b103b04d4be0733284a9680fdbf95e`。它核五行唯一替换、全部函数 AST、13/83/89 绑定及原命令，且确认 started/旧 exit1 没有被重标成成功。

## 6. 审查作用域

本轮只通过来源与接口迁移，不执行将来的成功分支。当前缺 reproduction 的事实只属于上述检查时刻；它不预言随后数值成败。真正完成时必须使用真实根观察再运行完整原门，随后才有原 prefix 联解、N512 校正和实际闭图认证。G5 及 README 的全部最终要求不因本审查而改变。
