# 新实际 λ=1 输入后的原 full-H/native 续接：最小源码合同

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

本记录只核源码与已经返回的小记录，没有重跑旧 .25/.5 尾、没有新 λ=1 输入、没有修改在运行源码。四 worker 与较细 H 延续是下一实际执行选项，尚无新尾的速度或六小时完成保证。

## 1. 旧终态没有测试六小时的 full-H 预算

旧 material worker 从 05:43:38 UTC 计自身 5.5 小时，11:13:59 正常结束 worker 步骤；尾的第二个 fresh 请求直到约 09:24:56 才真正进入 native，实际只剩约 109 分钟。此前包括原冷恢复及 M16 的实际计算，不是同一个 full-H 尾的计算时间。

factor .25 已实际通过，下一 .5 请求为 10:08:01.260；factor .5 通过后下一 .75 请求为 10:44:57.849，两者间约 36 分 56.6 秒，包括该次求解、完整审计、记录及交接，不能当作纯 native 核时间。最后 .75 的记录停在 iteration 5、chord-cached-J、norm 2.5508842381632904；这是 worker 期限中断，没有观测到该请求的最终接受或数学失败。

依据：`notes/2026-11-26-recorded-lambda004-tail-factor025-actual.json`、`...factor050-actual.json`、`2026-11-26-recorded-tail-worker-interruption.json` 及本会话首次实际 request 观察。不能从这次中断推断新候选 full-H 必须超过六小时，也不能反推新候选会在六小时内完成。

## 2. 现有 runner 已有可直接重用的 chord 源和二进制

`scripts/resume_20261126/tail_recovery_setup.py` 的真实链是：

1. 原 70 源恢复及原 sparse 线性代数；
2. `multistage-source`；
3. `install_shared_tail_engines.py` 生成 `shared-source`；
4. 拷贝到 `periodic-source`，调用原 periodic installer；
5. `install_bounded_chord_tail.py` 生成 `chord-source`；
6. 编译 `frozen_flow_batch`，再为旧 M24/512/16 配置生成 `native-tail24`。

因此在这个 runner 内，新实际 λ=1 场若属于原 portable/R53 设计，动态 M 的准备可以直接调用已经存在的代码：

```sh
python @REPO@/topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended/prepare_recovered_native.py \
  --source-topic @WORK@/chord-source \
  --dest @WORK@/lambda1-native4 \
  --native-cli @WORK@/frozen_flow_batch \
  --modes ACTUAL_M --spacing 3 --quadrature ACTUAL_N \
  --steps ACTUAL_STEPS --workers 4
```

这里的三个 ACTUAL 数值须来自新场所用 port 的原完整配置，不能借旧 M24 设置替代。保留原 strict `N>4*M*spacing` 与现 kernel 的 M≤64 ABI 门。这个命令只产生新的源码/manifest 执行绑定，不求尾、不重复线性前缀、不重新编译。

新 runtime tail config 从**先通过原 port 的 config_sha256 检查的基线配置**完整复制，只加 `chordMaxCorrections=3`、新 `traceFile`；有同 runner 的实际完整合格 warm packet 才可加 `initialCheckpoint`。记录基线配置、runtime 配置、原 port、新 native manifest、原可执行文件与 chord-install manifest 的各自实际 SHA。核四份 prefix Python 文件与真正 source run 的原 source-topic 字节相同，再按 native manifest 核全部 owned/native 文件。不要把 runtime 配置的新 SHA冒充原导出 port 的配置 SHA。

然后从真正 source run 的原 `portable_prefix_continue.py` argv 继承全部 profile/chart/core/gauge/门，只替换 native `source-topic`、实际 source raw 的 `raw-restart`、上述 runtime `tail-config` 和新 `outdir`；移除旧 control-record 初猜选项，保其余原设置。环境沿已有 native launcher 指向新 manifest 及其 SHA，`VISIBLE_FLEX_NATIVE_RUN_DIR` 必须是尚不存在的新子目录，由 evaluator 自己创建。

这是现有 installer + 原 portable 的直接组合，不需要改变方程或新建尾求解器。目前 `continue_actual_mode_true_tail.py` 这**一个**通用协调入口没有 prepared-native override：它只 shared→periodic→native，没有调用 bounded-chord installer。因此单给其原配置增加 chordMaxCorrections 不会启用未安装的分支。若要一条 CLI 协调，最窄的改动是照已审 M24 `tail_continue_recovered_prefix.py` 的绑定方法接上上述现有源，显式使用实际 M/N/steps/workers；或在通用入口的 periodic 与 native 之间调用现有 chord installer，再传上述 runtime 配置。无需新增数学模型。

该原 portable 入口仍是 δ/support **设计**外迭代，不能标成固定全度量精化。本节操作保留完整 tail 背景与源，不额外改变 g；原设计本来释放的 prefix δ 仍按它原来的语义记录。其他 warm/phase 家族不能改名冒充此 R53 输入。v5 可通过原 generic provider 接入同一 fixed=False 主干，但须另按[实际 v5 来源/参数合同](2026-11-26-v5-full-dn-source-interface.md)核真实 SOLVER_RETURN、δ/高phase 含义及完整源；本节的原 R53 标签不会自动涵盖它。

## 3. 原 full-H 与外迭代合同不变

`portable_prefix_continue.py` 的真实执行顺序是：

- 对每个显式 warm factor f 请求完整 `H_j*f**j`，`jacobian=False,audit=True`；
- 再请求完整未缩 H，`jacobian=True,audit=True`；
- 最多八次 inner affine-prefix BVP；每次实际 BVP 成功后，重新对该完整 candidate H 请求原非线性 DN/J/audit，再用原实际 BC 判是否结束；
- 最终 physical prefix audit 与原 nonlinear seam audit。

八次是原最大外迭代数，不是把前八份不同 H 响应当作相同场；也不要求在已过原 BC 后再无意义迭代。临时 affine DN 只供一次 inner BVP，不可作为最终实际尾或审计。

`--tail-warmup` 本来就接收显式因子列表。较细序列例如 `.25 .5 .625 .75 .875 .9375` 可以用同一个持久 worker 请求；随后代码仍自动支付未缩 H 与全部原外迭代门。每一个额外因子是一份不同的真实 Dirichlet 请求，必须单独记录和接受，不能把较小 H 的接受贴到原较大请求上。

更多暖步并非免费：每份暖响应也要原 fresh-final-J 与全 audit。不能在未测新输入前认定多加暖步一定节省总时间；也不能把 audit 改成 false 来兑现速度。本记录不改审计缓存。

## 4. 持久 worker 实际允许复用什么

原 `950f-tail-stage-port-v3.mjs` 只在 `sol.converged` 后更新 last。下一请求以第一个高度的比值作为 warm 状态缩放；仅当该比值有限且位于 (.25,4) 才用 last。默认还加 `dn.tail.initial(delta)`，使**新完整 H 的边界**满足于初猜。之后仍由原 nonlinear root/RK/residual 判定。失败响应不会变成下个 accepted last。

配置项 `harmonicAmplitudePredictor=true` 的现代码只在请求的其余高度都恰为零时启用逐谐波幂缩放。新实际完整多谐波 H 不满足这个条件时，切换该标志不会自动获得逐谐波 predictor。

原 `initialCheckpoint` 读取完整包中的 `response.checkpoint`，核 geometry/spacing/depth 后用原 remesh。它可以作为另一 H 的**初猜**，不是另一 H 的响应。相同 M、parts、depth 的完整节点沿原 remesh 的已有节点分支复制；改变离散层时仍只得到 remesh 初猜。新 full-H 包的接受与哈希必须来自新请求。

## 5. 已实现的 Jac/积分复用，不再重复开发

| 对象 | 原源码已做的复用 | 明确界限 |
|---|---|---|
| 同一固定 DN 的 geometry/trig/RK grid | `native_batch_adapter.mjs` 仅建立一次 static template，保独立 scalar/variational grid 逐位一致核验 | 没有跨不同物理背景或离散 scope 的 cache |
| shooting Jacobian | 原 bounded-chord3 在一次 fresh J 上最多做三次 correction，包含 fresh 那一次 | 后两步是声明过的 chord 算法，仍须原实际残差严格下降与域门 |
| 上一次接受的 state-only trial | chord 的 pending 直接供下一轮 residual 使用 | 未接受 trial 不进入 pending；失败 chord 会在原 iteration 预算内刷新 |
| 最终 DN 导数 | 接受前 fresh 原完整 stage J；`linearizedFlowJacobians` 供 tangentGraphAtCut 使用 | 缓存旧 J 不能冒充最终新状态的导数 |
| heightJetJacobian | 一次原全节点 tangent 线性解得到 G，随后 2M 次局部 cutJets 差分 | 不是 2M 次重新积分整尾；没有这个虚构的整尾倍数可消除 |
| Python 同 H 请求 | 原 client 仅在完整高度逐项相同、所需 J 已有且 audit=False 时返回 cache | audit=True 仍真实执行；本次不改它 |

`frozen_flow_production.cpp` 已对每个原 RK 点一次求 root，然后一次 literal implicit Jacobian 处理全部 K=2M 列，再积分变分方程；没有对每列重复一遍完整 Newton 尾。它在返回近似 root 处求原隐式 Jacobian，不是对停止规则作 AD。

四 worker 只分段执行原 native batch，依原索引重组；其先前字节等价证据见 `notes/2026-11-26-four-worker-native-execution.md`。它不并行化原 JS cutJets/audit 或 Python sparse 解，所以不能把总 wall time 简单除以二或四。

数学上，在同一 chord 周期，Js、scales 与 deepGraph 逐字不变，sparse helper 的矩阵相同，只有右端变；不过当前 helper 每次以新 Python 子进程装配并作 LU。另一个 H 的 scales 在浮点运算下不能仅凭代数比例认作字节相同。若未来实际测得该段成为主成本，必须按实际矩阵字节绑定才可考虑 LU 复用。当前没有增加这种机制。

## 6. 下一次真实输入的最小观察

不先假设瓶颈，直接沿现有小事件计时：native `events.jsonl` 的 batch_start/batch_terminal 给实际 J/state batch；worker trace 从 iteration 到 phase=correction 覆盖该次原 sparse correction；最后 converged iteration 到 response 覆盖剩余 cut/audit/必要 tangent 与记录。三段不是同一种成本。可用现有 `VISIBLE_FLEX_SPARSE_TRACE` 留其小标量，但 helper 的 seconds 只从 LU 前开始，不含其早先 JSON/装配时间。

先将现有 chord3 与四 worker、原持久状态连续使用到新完整 H；实际返回前不承诺速度、不放宽门、不换较小目标。若需改变暖步，只改变明确记录的 continuation 路径，最终完整目标和八次真实外迭代合同不变。

## 源码身份

旧原 worker/core/client/coupler：`34a036028256ad59c702a3fc8088275dad7c2948`，目录 `topics/visible-flexible-closed-surface/scripts/`。本次实际读到：

- `950f-tail-stage-core.mjs`：`53fdd936cf65f0a42929b6ce42c6ea12f183628abc9c9f3a351aac9c31ffbd6d`；
- `950f-tail-stage-port-v3.mjs`：`41a3fc113a8565dc2382966ed0dd299532a0510bee279552fb191aca3cb99f45`；
- `950f-tail-client-v3.py`：`12ff3db3867f4f4919032199e5954b830180a9b3697ed53b6feae4ebca0f86b1`；
- `db6f-prefix-coupled.py`：`37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a`。

当前主要组合源：

- 原 portable：`6dafa9551d5ae4a4f4d59e1b2d4c177efdc6b823e0a7ade826974e4ecdc5c9ea`；
- generic actual-mode coordinator：`a78623eaf09c51b0761f1fc610dfe6d46b42b79efa13912d5410430c6498ae52`；
- bounded-chord installer：`8f9bc468e89bc0523d14e45601e131c723931955d4642781fdaeca4b267fd3a9`；
- 四 worker native preparer：`08f6f0de7e1737a41864d9d420f48255a523c8aebea36dfa75de1a45940bc99b`；
- native adapter：`9931feea9bc905cdc700c4f5078a6ad2af0a215fa5bc2fd1c84212662cbd2718`；
- production C++：`e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf`；
- sparse helper：`a52567b2bfaded2fa9271a08f3cd969dc0291261f22cf2847c83234d93462fa5`。

这些是本次实际读的源身份，不冒充未来运行中新生成 native manifest 的 SHA，也不转移任何旧场的数值接受。
