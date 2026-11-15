# 九控制、三active完整112场：同一原worker的H(s)入口

作者：ChatGPT（amplitude 子任务）。日期：2026-11-15。

**类型：源码接口／未执行。** 本文及新源不提供任何已接受native、未来参数、lambda、request或run；没有在本地调用科学依赖。本入口把已经公开的九控制完整设计场与已经公开的原worker高度路径接在一起，不等待低三unit阈值才允许提出有限非零实验。

## 1. 新旧来源与精确范围

新增独立文件：`computations/geometry_20261115_nine_control_height_continuation_full112.py`，46089B，SHA-256

```text
0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924
```

其直接基线是已公开的 `geometry_20261115_nine_control_full112.py`，43641B／`00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8`。接入的原 helper 是 `geometry_20261115_original_tail_height_path.py`，23078B／`e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48`，其完整同worker算法原字节不变。接法沿已发表的六控制H(s)入口 `geometry_20261115_six_control_height_continuation_full112.py`，45097B／`557f3aab83116c1d8eef83e4c83306e8058749ccdb56b2ec8808effd2e16bf21`；没有把六控制标量模型复制成九控制模型。

原九族数学来自 `geometry_20261115_small_core_nine_control_family.py`，44390B／`086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629`。新适配器保留原21项显式PINS，并只增加00e4基线与e830 helper两项；运行时继续合并原完整core与family的真实source闭包及新入口实际SHA。

可对照[已发表九控制三active接口](2026-11-15-nine-control-three-active-nonzero112-interface.md)。九设计量的独立标量身份、原有限装配顺序、完整形状和core自由度、完整边界及final门均承袭00e4。

## 2. 新身份与不变的453方阵

新入口schema：

```text
nine-control-height-path-three-active-nonzero112-complete-physical-DN-v1
```

新recipe schema：

```text
explicit-nine-control-height-path-nonzero112-recipe-v1
```

参数顺序仍为 `[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]`；active索引 `[0,1,2]`，固定六shape索引 `[3,4,5,6,7,8]`。固定的是三个原odd系数和三个raw quadratic系数，不将它们在求解过程中默认为零。

完整问题保留338个物理状态、112个core未知量、三个active标量，总453维。左边界341行、右边界112行；原高109core是自由未知量，native斜率全部112×112行列保留。原圆参考、zero-H线性响应只用于未接受初猜；它们不代替当前非零H的真实响应。

这仍是三active的**设计问题**。把九个设计量全部固定后的same-g问题为450维、K=k=0，需要独立重构／序列化／求解责任；该工作不在本入口内。旧v3/v4 scalar身份不能直接消费九族并沿用旧same-g声明。新源也不会把failed73、failed95、失败120或待完成124变成accepted parent。

## 3. 与00e4相比的十二处源码变化

完整差异在交付的 `relative-to-nine00e4.diff`，8665B／`e3d1b1c4e958a85ff8af549423dc01bacb0627b653b20edcb7f5bf1c841d47b7`。修改仅涉及：

1. 顶部用途说明，明确真正的zero请求、完整H路径与endpoint J。
2. 两个独立schema。
3. 显式增加00e4和e830两个source pin。
4. 运行时加载原helper为 `d.height_path`。
5. recipe必须明确填写与原helper完全相同的 `height_continuation`。
6. binding记录原九基线、helper、policy和同worker职责。
7. prepare-only事件及最终事件使用新名称。
8. 首次直接 `owner.solve(H,jacobian=True,audit=False)` 改为原helper调用及其返回责任。
9. 明确记录路径停止／资源partial；停止后不进入FD或fullDN。
10. 最终返回记录增加原路径receipt及endpoint是否完成。

这些内容占十二个精确文本替换区块。源码静态解析确认仅 `runtime`、`read_recipe`、`main` 三个函数AST有变化；`prepare_problem`、`active_profile`、`curve_with_exact_nodes`、`bound_original_preflight`、`actual_boundary_fd`、`SharedNativeClient`、`original_full_solve` 以及原恢复工具函数AST保持不变。没有运行数值fixture或把静态检查新增为科学门。

## 4. 显式recipe与初猜契约

仍必须给真实的九个有限参数、完整参数次序／active／frozen索引、`field_modes=112`、`field_angular_quadrature=2048`、原四输入SHA，以及显式 `0 < lambda_target <= 1`。本文件不选任何一个参数点或lambda。lambda仅缩放原三个固定低core目标；原目标源文件与尾配置不改。

原两个初猜选项保持：

- `fresh-circle-low-three-linear`：完整圆／低三线性构造仅是初猜；高109初值可为零但仍保留全部自由未知量。新完整RHS和原节点／中点／两套RMS预检均真实执行。
- `same-family-complete-field`：必须供本新schema的真实完整文件和显式SHA；M112/N2048、完整field representation、九族source及全部九参数、453维全场均被读取。parent success仅记录，不能自动成为新目标的接受；当前RHS重新计算，不借用父RHS冒成新值。

原四输入的固定SHA仍是：

| 输入 | SHA-256 |
|---|---|
| accepted | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail_anchor | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail_config | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

新增必填的 `height_continuation` 是原e830完整POLICY，不能只给几个省略字段或隐式默认：

```json
{
  "schema": "explicit-original-complete112-height-path-policy-v1",
  "initial_positive_increment": 0.015625,
  "accepted_increment_multiplier": 2.0,
  "maximum_increment": 0.25,
  "mathematical_refusal_increment_multiplier": 0.5,
  "minimum_increment": 0.00000095367431640625,
  "maximum_bootstrap_requests": 64,
  "includes_zero_and_final_J_requests": true,
  "zero_request_jacobian": false,
  "intermediate_request_jacobian": false,
  "endpoint_request_jacobian": true,
  "bootstrap_audit": false,
  "endpoint_uses_original_H_star_words": true,
  "total_scientific_wall_clock_seconds": 18000,
  "resource_limits_are_not_mathematical_nonexistence_claims": true
}
```

从某个已记录九控制搜索点选初猜是未来请求的来源责任。低三unit未到阈值不禁止有限正lambda实验；初猜能够通过后续完整科学门与否仍由真实执行决定。

## 5. 原native输入与全112高度路径

本路径直接复用原client `exact_20261114_true_tail_client.py`，SHA `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`；原worker／core分别为：

| 原组件 | SHA-256 |
|---|---|
| 78718-prefix-tail-tangent-fourier-worker.mjs | 36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a |
| 78718-tail-tangent-core.mjs | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |

必须恢复原78来源文件和113已实际使用的两个原历史ready环境槽 `VISIBLE_FLEX_FROZEN_LEDGER_READY`／`VISIBLE_FLEX_FROZEN_STORED_READY`；不能让原client在清理后的main路径取空文件，也不能换成失败checkpoint。已读真实历史来自 `8bd267107cc8710d371f3b62c02986655ac965b0`，对应ready SHA分别为 `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` 和 `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d`。

helper要求真正的新M112/N2048 worker：调用数0、Python cache空、没有安装initialCheckpoint。原config若存在需要恢复的输入必须真实恢复并保来源；本适配器不会删改config字段去凑启动。原solveTolerance仍 `2e-9`，maxIterations仍32，原root／RHS／32×10 native求解不改。

`H_star`来自原 `core.true_height(problem.boundary,problem.values[-1])` 的全部112个实际分量。接法为：

```python
actual, path_receipt = d.height_path.continue_complete_height(
    owner, H, recipe['height_continuation'], out/'height-path', binding)
```

helper先作真实的全112零高度请求，再从原policy的正增量开始。中间高度是每个坐标的 `s * H_star[j]`；不会只保留低三、删掉非零高模或用旧zero-H线性响应代替。到s=1时直接复制原H_star的全部浮点词，而不是再乘1形成不明口径的新端点。

每个真正收敛的native请求才推进 `last_converged_s`；同一个原worker、原Python client及原owner继续使用，helper不直接赋值cache或worker last。中间请求设置 `jacobian=false` 只是不要求出口全J；原native内部Newton仍照原实现形成withJ。端点必须实际请求并得到 `jacobian=true` 的完整当前H响应。

只有同源、同配置、同H、原trace与record均明确绑定的原数学拒绝，且Python cache确认未变，才按原policy缩小增量。任意IPC、记录异常、协议不明确不能猜worker last；这类结果记为partial并停止。零高度本身拒绝时直接保留原事实，不推出正高度路径不存在。

## 6. 端点之后仍是原FD、完整DN与最终审计

路径helper返回后仍执行00e4已有的检查：响应必须 `actual_nonlinear_solve=true`、`converged=true`、无failed，checkpoint的全cutHeight与原H相同。仅路径返回或中间高度收敛不会设置完整DN接受。

原 `actual_boundary_fd` 随后执行，保完整物理边界、原方向／步长和 `5e-5` 阈值。通过后才让同owner进入原complete-band/full-DN主入口。完整453场、原17次内回溯、`1e-6` collocation／冻结RMS、`1e-11` BC、原实际tail更新、原最终native full J与audit均不变。原main仍控制 `new_coupled_finite_acceptance`；新入口只在原返回0且该标志真实为true时声明自身success。

本项不提供最终封闭Cartesian装配、same-g450加密或课题的全部t嵌入／reach结论。高度路径成功也不是对这些责任的替代。

## 7. 失败、partial、生命周期及预算

`HeightPathStopped`保留原 `outcome`、status receipt和`resource_partial`：资源partial返回75，原明确路径拒绝返回3；两类都设置 `height_path_endpoint_completed=false`，不进入FD或fullDN。其它原异常照旧记录并抛出。所有结束分支由原 `SharedNativeClient` 的唯一owner关闭worker；helper不关闭owner，也不建立第二个owner。

输出目录和factor目录必须是独立、空的RUNNER_TEMP子目录。临时文件包括原prepared、原native记录、height-path binding／请求日志／status、actual-H FD和原full-DN输出；消费并打印紧凑原标量与SHA后由请求自己的外壳清理。无raw写Git、Release或新artifact。原e830事件名中仍含 `request124` 是冻结helper的source标签；新adapter的schema／binding／run记录区分本次使用，不能把事件名当成实际新run编号。

helper要求环境变量 `VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC`。它必须由实际进程预算外壳用同一机器的 `time.monotonic()` 建立总截止时刻，覆盖bootstrap、FD、fullDN等科学过程；不能写一个任意墙钟字符串或每个高度重置。最多64次请求及最小增量是显式资源边界，不是新的数学非存在判据。主进程外壳还应承担单个请求内的到期终止，不能只依赖helper的请求间检查。

已公开 `root_20261115_six_control_height_path_run.py` 写死了六入口文件名与557f SHA，**不能原封当九入口通用runner使用**。未来真实九请求需独立薄身份接线，保其原进程组、预算、stdout和partial职责；本文不预写该请求或假造未来run，也不改旧runner。原2700秒真实规则监控同样仍由未来Actions接线承担。

## 8. 可执行CLI与尚未选择的输入

CLI保留00e4全部参数，仅使用新basename及新recipe：

```text
python geometry_20261115_nine_control_height_continuation_full112.py
  --recipe <真实新recipe>
  --expected-recipe-sha256 <该recipe实际SHA>
  --accepted <原accepted> --prepared <原prepared>
  --tail-anchor <原zero-anchor> --tail-config <原T112-config>
  --tail-client <原exact_20261114_true_tail_client.py>
  --expected-tail-client-sha256 1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09
  --tail-source-root <临时原repro/source-root>
  --out <RUNNER_TEMP下独立结果目录>
  --work <RUNNER_TEMP下独立factor目录>
```

原可选 `--continuation`、`--jac-workers`、`--max-nodes`、`--material-angles`、`--physical-angles`、`--node-heap`、`--outer-iterations` 全保留。原默认outer8、max_nodes1200、两类angles4096、jac_workers2；未来请求须按实际资源需要显式列出，不能把资源调整伪称数学阈值更改。`--prepare-only`仍只输出未接受初猜，不能冒成运行完整native、FD或fullDN。

当前只交源及完整差异／接口，没有任何已执行数值、选定九参数、正lambda或完整场。下一真实请求可以根据实际九控制读回明确选择初猜，同时继续保留全部失败和partial范围；不需要先等低三到根才有权运行这一原门完整的有限实验。
