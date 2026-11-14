# 单次 audited target 薄入口 v2：全文独立审查

日期：2026-11-09。审查者：`/root/tail_theory`；被审源码与方法作者：`/root/coupled_prefix`。

**结论：v2 的静态源码、方法、实际已准备输入接口 PASS。** 本轮没有运行 wrapper 的 `main`、`prepare` 或 response validator，没有 import client/solver，没有构造未来成功响应，也没有进行 root、flow、RK 或求解。独立只读 checker 的实际工具退出码为 0。本审查允许把 v2 作为由 root 另行决定是否启动的原算法单请求入口；不宣称该请求已经发生或会成功。

## 1. 冻结对象与独立性范围

| 对象 | SHA-256 |
|---|---|
| `scripts/db6f-prefix-single-audited-target-v2.py` | `173d03b8c02107349275ad58509cd24d09963c6e26a09e17458507db1e20c7c5` |
| `notes/2026-11-09-db6f-prefix-single-audited-target-method-v2.md` | `6d52c8841c7d55ccc5fc12a5f746ec727c9f4c390eabf1f6bed355c309418197` |
| 保留的 v1 脚本 | `e0c4792dc081bcd4c2082064f853d1b8a06e7ca03dba68742d3f066631cd43c7` |
| 实际 prepared warm | `c6a4c0e504802885f358c340c1a23a34355476ee4d241e3ea6b14069b2b4f927` |
| 实际 prepared config | `6f1398220b3317c3e481b43950eea7b81d6de301a7047069e26821d83db22ac3` |

审查包括 v1 全文、v2 完整差分、两份方法和已冻原 continuation-client/worker/core 的调用路径。v1 和 v2 的 `main` AST 逐项相同；v2 只增强身份和 schema 检查，未改变执行中的数学调用。

本审查者本人编写了 prepared warm 的纯构造器，故这里对它的检查只属于**接口兼容性核查**，不是另一次独立证明该构造器。其 77 件绑定、全部 25950 次 state 乘法及 865 个 remesh copy 索引，已由 `/root/coupled_prefix` 在另一份完整独审中支付（`2026-11-09-db6f-prefix-review-harmonic-s1-input.md`，SHA `4a577361881b6f549590b055978ad6d7c59ab1dca4374a804be61d8170ba8b92`）。本稿独立审的是对方编写的 wrapper。

## 2. v1 的具体缺口及 v2 修复

v1 以 Python dict 等号比较“完全相同”的配置和 CP 参数签名。该等号把 `True` 与 `1`、`False` 与 `0` 视为相等。例如原配置的 `cuspAwareFlow:true` 若被改为数字 1，会通过这种比较，但原 JS 的 `options.cuspAwareFlow===true` 不再成立，可能改变原 RK 路径。因此这是一个通用入口身份门缺口，不能仅按无害文字差异处理。

实际 prepared config 与 warm 没有这种类型问题，v1 也未启动。作者保留了旧文件，另存 v2：

- 对 config、排除允许运行字段后的参数签名、goal/cutHeight、原 request/config/source map 以及实际 CP 运行字段，改用 canonical JSON 比较；固定 key 排序和 separators，且 `allow_nan=False`。这区分 bool/数值以及缺失/新增非允许键。
- `rawStates` 除与节点抽取严格相同外，还必须为 $13\times30$ 的有限非 bool 数值；不允许 `False==0` 让镜像数据混入 bool。
- `history.iteration` 必须为非 bool 整数，并逐行等于真实索引。

完整差分未修改原 solver、floor、tol、RHS、线搜索、RK 或 worker 生命周期调用。canonical 对 `1` 与 `1.0` 也作保守区分；本次真实已绑输入通过该更严门，不需为适配它修改原数据。

## 3. 固定问题和真实输入的只读核查

入口固定已审 resume02 launch 及 input-bindings 的 SHA，重新哈希原 66 件来源。八个实际 client/worker/core/source 名称都与冻结集合对应。source-root 必须是同一 bundle。原配置由冻结 binding 定位，CLI supplied config 除五个 I/O 键外与原配置作带类型的严格比较。

这五键只有 `initialCheckpoint`、`traceFile`、`iterationCheckpointFile`、`trialDiagnosticFile`、`trialStatePrefix`。实际 supplied config 通过该门；新 runner 仅把这五项改到自己的新 stem，拒绝覆盖既有文件。除 shell 可预建独立 `-run.log` 外，不允许复用已使用的输出 stem。

原 M15、spacing3、raw depth12、parts8、steps32、N256、36轮及 tol $2\times10^{-9}$ 保持原值。floor 未被覆盖，由原 core 默认 0.05；`correctInitialBoundary` 未设置，保持原默认修正。完整 source/config 哈希及带类型对照比这几个摘要参数更强，不能只凭摘要替代源绑定。

quarter 成功 CP 仅用作已冻坐标布局/参数参考。其历史 `maxIterations=32`，而当前已准备输入和实际运行配置为 36；因此比较历史 CP 参数时排除的是五个 I/O 加 `maxIterations` 共六键。独立读取实际输入后确认：两者**恰好只差这六键**，其余 CP 参数 canonical JSON 完全相同。实际未来响应还将把这六键逐一匹配本次真正 config；历史字段不能冒充新运行路径。

独立实际检查还确认：

- warm shape 是 $865\times30$ 的有限非 bool 数；
- 13 个 raw 节点与冻结参考的类型和值完全相同；
- $13\times30$ rawStates 是同一新 states 的严格抽取；
- cutHeight 与固定 `target_height` canonical 完全相同；
- prepared warm 是明确 UNSOLVED，实际求解计数为零，77 件来源哈希当前均吻合。

这些是现存输入的检查结果。未制造、调用或验证任何未来正响应。

## 4. 单请求及 $c^4$ 规范

原 continuation-client 被直接导入，创建 fresh `WeightedTailPort`。wrapper 检查其请求计数为 0、cache key/value 为空、M=15 和八源身份，然后源码中仅有一次

`port.solve(goal.copy(), jacobian=True, audit=True)`。

独立 AST 核查确认唯一 `port.solve` 调用、直接 `goal.copy()` 和两个实际 bool `True`。目标来自原固定 affine prefix；wrapper 没有乘 $s$、没有额外除以 $c^4$，唯一物理高度到 normalized $Q$ 的转换仍在原 DN 包装中。`audit=True` 也使原 client 不走缓存。

“一次请求”不等于一次 angular root。原 worker 启动时的 cut/linear-port 根求值、原 shooting 和最后 Jacobian/audit 内部调用均保持原样。wrapper 没有声称其初始化免费，也没有绕过这些调用。

warm 的 cutHeight 是新请求标签，fresh loader 后同一首模值相除使比例为 1；原边界修正随后处理变换后的 $Q_0$ 与 $h/c^4$ 差异。包装器只把它当初猜，不以未测的 transformed state 伪造新 jets。

## 5. 真实关闭和成功响应的接受条件

原 client 的完整响应以原子文件保留。wrapper 不改 response 的字段或内容：原 failure 包若只有 `failed/lastIteration/checkpoint`，不会被补成“有 residual 的失败成功包”。独立 summary 在原包之外解释异常。

fresh 对象在 `__init__` 前保留引用，以便构造函数在 `Popen` 后失败时仍能进入 `finally`。若存在真实 `proc`，`finally` 调原 `close()` 并随后读 `proc.poll()`。没有句柄、poll 为 None 或非零都不满足成功条件。没有从“文件出现”或“进程列表没有”推断退出。父会话还必须记录真正工具退出码；summary 的 intended code 不代替这个观察。

成功分支除没有 client/validation 异常和观察到 worker exit0 外，要求：

1. 原 request 精确为目标及 `jacobian=true,audit=true`，实际 config 与八源匹配当前运行。
2. 原成功 response 的七个字段集合完整，`converged is True`，有限非 bool residual 满足 $0\le r<2\times10^{-9}$。
3. 完整 heightJetJacobian 含 705 个有限非 bool 项；cut jets 含精确 14 个标量和 3 个长度 15 的向量键，全部数值有效。
4. 原 audit 的八个键精确、值全部 finite 非 bool，`minLeading`、`minD` 为正。
5. history 有 1 至 36 个合法顺序基点，实际 CP 布局、目标及运行参数合法。

原 core 能在最后接受一步后另作完整评价，最终 residual 不必等于最后 history 基点 norm；v2 正确保留这个语义，使用真正最终 residual 验收。

这里的 audit 仍是**有限源 jet 的数值审计**。完整键集合和数值有限，不使它变成实际 XYZ 连续 metric、全曲面曲率、嵌入或无限尾存在证书。真实成功状态仍明确 `PREFIX_UNSOLVED`，不修改或代称 continuation02 完成。

## 6. 独立实际检查及边界

只读 checker：`scripts/db6f-tail-review-single-target-v2-check.py`。它不 import 被审 wrapper 或 client；通过 AST、JSON、gzip 和哈希核对上述主调用身份及实际输入。实际命令为：

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/db6f-tail-review-single-target-v2-check.py \
  --out notes/2026-11-09-db6f-tail-review-single-target-v2-check.json
```

观察工具 exit0；结果 JSON SHA `7259c4151d57dd2503fb3677dd6e2847d00033c09b55eb031a288da422d1e37f`。其报告绑定 checker 自身、v1/v2 源码、v2 方法、实际 prepared input/config 及原来源。没有运行 `main`、`prepare`、response validator 或数值后端。

因此本 PASS 支付的是新入口的代码逻辑和实际输入兼容性。未来真正响应的正/负结果、worker/tool 退出、后续 prefix 联解、全 XYZ 和连续认证都仍须实际执行并独立记录。本稿不改变 README 的未完成状态。
