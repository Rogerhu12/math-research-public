# 每个真实 DN 请求的线性高度延拓：独立实现与纯准备

作者 /root/coupled_prefix，2026-11-09。**状态：新控制层已实现、隔离协议验证已通过、单外请求 pilot 输入已纯准备；真实 DN/root/flow/BVP 调用均为0。待未参与实现者全文审查和 root 复核后，才由 root 决定是否启动。** 原 continuation03 和已绑定原始源码未改。

静态依据是 `prefix-matched-cut-linear-dn-continuation-plan-v2.md`，SHA `a65890daff2c55ff8e0593445c0f7689e06d445024e87988444160762da04fe6`；其全文独审为 `tail-review-linear-dn-plan.md`，SHA `bace29e460fd4db391c09a2fd935395cd7ef1faad1a0c6a5e8a613e8c2198878`。这份实施说明不把协议测试代作数学成功。

## 1. 四个新的可执行源

| 源 | 本次作用 | 冻结 SHA-256 |
| --- | --- | --- |
| `scripts/db6f-prefix-tail-linear-continuation-client.py` | 原 client 外的有界协调层及单外请求入口 | `d0d06d44fe1a99c50a2d20890ec7e91909578851a9d763172b3b48f2639d169e` |
| `scripts/db6f-prefix-flat-linear-continuation-coupled.py` | 仅重定向原 shared-client import 的未来 coupled 选择器 | `7c381f042b505131ceb81bf47ca8f6d7ac6794c504f48e087c5b33832a537ab9` |
| `scripts/db6f-prefix-prepare-linear-dn-pilot.py` | 验证旧真实材料，生成新五 I/O 配置、策略和 pilot launch | `d2023e9497cd2c65c98fda11b7a7e96998fefeabc6fd350e78cc00eb38201ba8` |
| `scripts/db6f-prefix-test-linear-dn-protocol.py` | 一维抽象协议 stub、分类器和旧真包 schema 检查 | `6ae0759a5a7b510067297bb5ffacad07dfe2c6a895c345fb2e519e3b8c00a523` |

原 trial-client/worker/core/split、两个 closing factory、subdivision/remesh 共八个真实源全部保留原字节。新原始物理请求包的来源集合明确是**原八源加 adapter，共九源**。构造器在发第一个求解请求之前将自身 SHA 加到原 base 实例的 `sources`，由原 base 的保存代码写入每个包。选择器、策略、preparer 及传递依赖另由输入闭包绑定；没有假称仍是旧八源运行。

## 2. 实际控制与原问题保持

`Coordinator` 只协调物理 cut-height 请求。初次没有当前进程真成功包时，先在绑定 seed 标签做原真实 bootstrap；输入 seed 本身只当 warm。其后每个不同外目标采用固定原点的线性 $H(\tau)$，初步长/最大步长 $1/8$、最小 $1/1024$、成功保持步长，每个外请求最多32个实际请求，至少留一位置作必要的最终验证。

每个中间请求只调用原 base.solve，Jac/audit 均 false；这仍执行原 shooting 全 Jacobian、原 root/RK、末 cutRaw 和 cutJets，绝不是仿射 DN。只有完整真响应、原 residual 门及完整有限数值 schema 都有效，才原子更新 last-good **包引用**。失败检查的是原闭包；FAILED states 不作自动回退源。原 worker 在成功前的数组复制和 `last` 更新位置支付同进程回退；ratio 不在原 $(.25,4)$ 内时仍沿原代码用 linear 初猜，adapter 没有另造 warm 规则。

可步半失败只有已审三类。原汇总线搜索失败必须核本 call 全部已闭 trial 行与最后完整十档；unknown/other/I/O 不论出现在哪一轮都终止。正常 `converged=false` 也不能掩盖此前未知 trial 错误。仅三键 failed 包、明确两个 JSON null、原中间 false/false 和36轮下的已核 momentum 白名单，才使用“第一次 progress 前”分类。有 history 的同名非汇总错误不能排除末后处理，因而停止。最后 requested Jac/audit 阶段的任何失败都停止，不退而返回中间解。

原实际 cache 仍只按 `np.array_equal` 命中；不引入容差或近似键。同浮点 H 可以在 dyadic 格作有限逻辑推进，但不增加实际请求/数学成功次数。精确 goal 到达后仍显式 `goal.copy()`，并使用外请求原 flags。原 source Jacobian 的705项及需要时原8字段 audit 不可用插值代付。

`.calls` 始终是原物理请求计数。另存最后真成功包号；正常返回要求它等于 `.calls`。失败导致计数领先时，必须等后续真成功刷新才可返回，或终止此实例。终止状态禁止以后取旧 cache。最终 seam 的原记录号规则因而不变。未来 coupled 选择器不改原方程、实际 BC、outer 次数或 seam；这次没有生成 coupled launch。

## 3. 原参数、数值门和有限性

本次纯准备逐值并按 JSON 类型核实：M15、spacing3、N256、physicalDepth12、p8/s32、原36轮、solveTolerance $2\cdot10^{-9}$、默认 projectionFloor .05、原 auditSteps32、默认开启的全模边界 warm 修正完全保持。与旧配置差异严格限于 initialCheckpoint、traceFile、iterationCheckpointFile、trialDiagnosticFile、trialStatePrefix 五 I/O 键。没有向原 factory 传入协调策略键。

adapter 对真实 normal response 核：17-key jets 的14标量与3个长15向量全部有限且禁 bool；705 Jacobian、必要 audit 的8字段；history 合法，但不要求最后历史基点 norm 等于最后 reevaluation residual；865×30 states、13个 raw 节点及对应13×30镜像；运行参数同实际 ready 参数；物理请求标签与 flags/source/config。这里没有增加 Cartesian 二 jet、曲率、reach 或其它几何阈值。

原 base gzip 包仍由原非原子写法产生；若写入、解码、schema、哈希或 journal/last-good 引用保存失败，协调层直接终止。不会因为内存中的 worker 可能已经更新，就猜一个未完整留存的成功点。last-good 小引用另用临时文件、flush/fsync 与 replace；其保存失败同样不允许正常返回。

## 4. 隔离协议验证的实际范围

最终 `prefix-linear-dn-protocol-02.json` 的实际 receipt 为 **47e346，exit0**，SHA `2a7c21f4d2e65e4b664e0fe223ec8be681513215ae8d289a8c116299a914ec14`。15类核查覆盖：

- 已知数值失败之后保持旧真 cache/worker-good，下一子请求从它出发，包号保留失败次数。
- unknown、partial-record 和“worker 已更新后的 I/O”均停止；首次 bootstrap 失败不伪造 last-good。
- 物理预算预留最终验证、最小步长和逻辑步预算耗尽均不返回中间值。
- 一个 ULP 的目标通过同浮点逻辑格到达 goal 的精确副本；原 flags 和 audit 绕缓存保留。
- 最后 requested Jac/audit 失败，即使已有同 H 的纯 DN 成功，也不把外请求标完成。
- journal、原子引用写入失败和 `.calls` 领先 cache 都不能正常返回。
- 分类器拒绝 missing/null 混用、错误阶段、早期 unknown trial 和不完整十档；真实旧首包 schema 可读，五个仅在内存中的非法数值变体拒绝。

抽象 stub 故意只用一个标量，不含实际有限 DN 的 CP/jet schema；所有 stub 包只留内存，路径名明确不是实际文件。它没有调用 `WeightedTailPort` 构造器、Node、root、flow、DN 或 BVP，也没有生成未来正候选包。真实旧首包只作已关闭元数据读取。

第一次本地协议检查 d2032b/exit0 的 report01 也保留。封存前把“正常未收敛也检查所有旧 trial 错误”收紧后，才运行最终02。report01 对应的两份旧源已通过反向恢复并严格匹配其存储 SHA 保存为 `db6f-prefix-linear-client-protocol01-source-snapshot.py` 和 `db6f-prefix-linear-protocol01-test-source-snapshot.py`；它们只作历史源码，不被当前 launcher 选用。

## 5. 已实际纯准备的唯一 pilot

新 stem 为 `2026-11-09-db6f-prefix-linear-dn-matched-h0-h1-pilot-01`。真实 pure-prepare receipt **c27be6，exit0**；没有端口构造。preparer 重新核旧121输入及 root 真实失败观察所绑定的闭文件，再生成142策略绑定、143 launcher 绑定。

| 材料 | SHA-256 |
| --- | --- |
| 新 `-launch.json` | `d09a7b6b918c6a35eac9d122aaa754cef67caa630678635fbe61156616fd9241` |
| 新 `_tail-continuation-policy.json` | `6493fb9fc1b90b4352666a241ff17cde7bcc711e83eb526b9810e9e23a2ec510` |
| 新 `-preparation.json` | `da774ee91424761680d4330f3f4c9be6d6ded3ade52aa607338815c847e38a1e` |

seed 是旧 matched `_tail_0001` 真成功包（SHA `6f4de10c22fc05cedc87994c274c3643b5390add7bfe0ca71001e02a440a7a86`），但仍需在新进程作真实 bootstrap。唯一外目标完全复制旧 `_tail_0002` 的真实 request，保留 Jac=true/audit=false；该源包仍是失败三键 schema，没有改写为成功。当前 prepared metadata 不包括任何新 response。

launch 中已有完整可执行 argv/cwd/stdout_log。下面仅列其入口，**本次没有执行**：

```bash
python -B topics/visible-flexible-closed-surface/scripts/db6f-prefix-tail-linear-continuation-client.py \
  --pilot-launch /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-linear-dn-matched-h0-h1-pilot-01-launch.json
```

实际 root 应以绑定 launcher 的原 argv 为准，并另绑定其空间 guard 与真实工具退出观察。pilot 若成功，只得到这个实际 H1 的原有限 DN/J；prefix 仍 UNSOLVED，也没有 final seam audit。若失败，summary 保存真实错误、最后真成功包引用和 worker 关闭后实际 poll；tool/worker 正常退出不自行代付数学成功。后续完整自由切口联解、N512 真校正、闭图/G5 证书都仍需要。
