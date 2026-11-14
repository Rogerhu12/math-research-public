# R273 完整阻尼方向接原生十次试探：独立接口

- 作者：`geometry`；日期：2026-11-14 UTC。
- 分类：可执行接口与纯源码验证；本文件不报告新科学计算。
- 前置证明：[R273 完整原生阻尼平方根链](../results/R273-complete-native-damped-square-root-chain.md)。
- 方向合同：[eta=1 与原十次试探](2026-11-14-native-damped-eta-one-trial-contract.md)；[完整 QR 生产者接口](2026-11-14-native-damped-chain-QR-interface.md)。

## 1. 对象与范围

本入口消费实际 R273 生产者给出的完整 **1373 节点、每节点 224 分量**原坐标方向，以及按同一 `old_to_new` 映射限制的完整原 577 节点方向。有限矩阵目标仍是实际54的 868 个 direct-longdouble 后一次舍入到 binary64 的短块，加上保留的 504 个原块；基态、残差、H、远端 Robin 条件及原残差尺度全部保持。

方向生产者用完整平方根链及显式 eta 求候选方向。阻尼最小二乘方向一般不满足 cut/far 线性方程为零；试探入口因此**保留全部 cut/far 方向分量**，不清零、不投影，也不再次乘 sigma。实际文件中的方向已经由生产者恢复成原 Q/Pi 坐标的 binary64 数组。

试探入口只替换原生求解器第一次迭代的两个调用：其 with-J 基态读出换成完整绑定的 actual28 缓存，其 correction 换成实际新方向的原 577 节点限制。原 `evaluate(..., false, scales)`、十个步长、D/S/A 与 root guard、严格原尺度范数下降判据保持原文。原始试探执行后即保存结果并停止；这里不重建旧 J，不运行新的 QR，不继续下一次 Newton，也不产生端点 J 或 fresh audit。

R273 的 L2 能量、模型梯度、完整精确线性缺陷都是生产者诊断；试探入口不根据这些数值增加接受阈值。即使候选不是原有限线性系统的精确 Newton 解，仍由同一原生非线性试探判定。

## 2. 冻结源码

文件位于 `computations/`，均为独立入口，没有覆盖原55的源。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_native_damped_chain_trial_replay.py` | 32623 | `ebd3110e7ba9b2edeca155370d2c7fd6f02d3757ae285379d54a2b4a39793ccd` |
| `geometry_20261114_native_damped_chain_trial_replay_hook.mjs` | 60281 | `884d2d44439151d0dbc5d474e20ebe5c024e577396088f01717d33a522b50323` |

固定来源如下。

| 用途 | 源文件 | SHA256 |
|---|---|---|
| 实际方向生产者 | `exact_20261114_native_damped_chain_qr.py` | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |
| actual54 完整目标与原件绑定 | `exact_20261114_rawcell0_direct_ld_system.py` | `b64b6ed8b387834b5cc9332675127a1dcbb15a317c3400f5b768d18cdbdf5a8e` |
| 生产者精确读回核的来源身份 | `exact_20261114_native_allrows_dyadic_residual.py` | `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` |
| 原1372布局与全部原件绑定 | `exact_20261114_rawcell0_step_system.py` | `fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81` |

原55 Python/hook 源分别为 `41976f4298d361ad06d0753698eebcd5149d3ce56410904768d6426610c2984e` 与 `373c82c75152a800246e84618fb2ba72fc0b3960e3b3e4eff9b7590724bad4ce`。新入口按新的 R273 schema 读取真实文件，没有把新生产者冒充原带状校正器。

## 3. 实际输入绑定

旧 actual17、19、21、22、23 的 H、seed、config、source、graphs/gains、far 与尺度证据沿原55接口全部保留。actual28 使用**真实文件名 `result.json`**；新的 R273 生产者则使用 `result.json.gz`。两者不得互换。

| 实际输入 | 必须绑定的 SHA256 |
|---|---|
| actual28 `result.json` | `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7` |
| actual41 `result.json` | `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf` |
| actual54 捕获 `result.json` | `e60da64312819a87388cfa96c209fc9188dca02c0ab055cbcc934f3507888ac6` |
| 本次 R273 `result.json.gz` | **实际生产完成后计算，以 CLI 显式传入；本接口不虚构未来值** |

Python 使用冻结的 `RawCell0DirectLDSystem` 绑定全部 actual28/41/54 来源及完整有限矩阵。该绑定器会按既定表示恢复 stored-output-minus-stored-node 的残差数组，不调用 RHS、ODE、J、native、精确点积核或 QR 类，也不重新形成 direct-LD 块。

随后核 R273 result、完整 input binding、array manifest、两个 checkpoint 和两个完整原坐标 raw direction 文件。每个 checkpoint 的 `negative_zero_columns` 恢复为真实 binary64 负零，再与 raw 文件每一字节对照；完整1373方向按实际映射提取的577行，也必须与 restricted raw/checkpoint 全字节相同。Node 再核同一来源与完整方向身份后，才向原 live worker 发唯一请求。

### 3.1 新生产者字段

`result.json.gz` 的 schema 为：

```text
complete-native-direct-LD-J1372-damped-square-root-direction-v1
```

实际字段包括 `source_sha256`、`system_source_sha256`、`kernel_source_sha256`、`new_matrix_identity_sha256`、`actual_direct_result_sha256`、`input_binding`、`eta_cli_text`、`eta_binary64`、`factor_summary` 及四个方向描述器。试探接口没有沿用旧带状生产者的 `initial_solve`、LU `info`、顶层 `M/K/depth/dimension` 或 checkpoint `scaling` 字段。

完整 factor inventory 中的 rows/columns、两倍 augmented rows、1373 个 penalty block 和307552个常数行仅用于确认消费的是声明的完整生产者结果。入口不比较 triangular diagonal、gradient、model energy 或 exact defect 的大小。

### 3.2 eta

工作流可以按本次选择调用 QR 的 `--eta 1`。试探 CLI **没有 eta 默认值，也没有 `--expected-eta`**；它读取实际生产者的原始 `eta_cli_text` 与 `eta_binary64`，验证原 CLI 文本解析后的 f64 bits，并同两 checkpoint、Python spec 和 Node 再核一致。实际 eta 被原样写入试探 provenance 和任何 selected checkpoint。

这种检查绑定已经生成的方向，不重选参数，也不将阻尼加入原非线性方程或原验收容差。

### 3.3 完整数组与按需读取

`output-array-manifest.json.gz` 的 schema 为：

```text
complete-native-damped-chain-direction-arrays-v1
```

试探绑定其完整文件字节和全部唯一相对路径描述器；真正重新读取的方向 payload 是：

| 描述器键 | 数组名 | shape |
|---|---|---|
| `step_delta` | `complete-original-coordinate-delta` | `[1373,224]` |
| `restricted_old_node_delta` | `complete-old-node-restricted-delta` | `[577,224]` |

两个 checkpoint schema 分别为：

```text
complete-native-damped-chain-direction-v1
complete-original-node-restriction-of-damped-chain-direction-v1
```

生产者的 QR 因子 payload 保留在原 artifact；原 trial 不需要再次读取这些约GB级因子来应用已保存方向。完整 manifest 来源保留，接口也明确写出 `QR_factor_payloads_not_reloaded=True`，没有冒称独立重审因子。

## 4. 原生调用与完整结果保全

与原55相同，启动 Node24.22.1 的原 `TailClient`，保完整原 config、原 source-root、容量和 ready 身份，以及 `--node-heap 6144`。Python `Popen` 转接只给指定 frozen worker 额外加载新 hook；无关 git 子进程照常放行。请求仍是同一完整 H、`jacobian=True,audit=True`，但本接口在一次原生试探结束即停，因此不把这些协议请求标志误称端点 J/audit 已完成。

首次基态采用 actual28 已存 with-J 结果，明确标 `baseline_is_cached_from_actual28=True`，没有伪造本次新 baseline evaluate。原基态 norm 由原记录及其 f64 bits绑定；试探不本地重算该数。

原十步长为 $1,1/2,\ldots,1/512$，保持原完整循环正文。每次都由原 `evaluate(...,false,scales)` 重算非线性流并应用原 guard。只有原 trial 返回有限 norm 且严格小于同一原基态 norm，才能选择状态。

若首次有接受，保存完整原577节点 selected state 的 gzip binary、带负零列的 checkpoint、真实 trial 记录及全来源，随后抛出本接口明确的计划停止标记：

```text
VISIBLE_NATIVE_DAMPED_CHAIN_TRIAL_REPLAY_ACCEPTED_STOP_V1
```

selected checkpoint 中 `success=False`、`converged=False`、`native_tail_response=False`、`endpoint_J_computed=False`、`fresh_endpoint_audit_computed=False`。一轮接受只是可继续的状态，不是达到原 native 容差或完成课题。

若十次全拒，保留原 `multiple-shooting line search failed at ...` 原生失败信息、完整十条诊断及原失败阶段输入数组，不改成计划成功。入口 exit0 只表示本次 replay 完整且有一条原试探接受；完整十次全拒或非预期失败返回2。所有输出均应通过工作流的 `always()` artifact 保存。

内部 solve 的 `toString` 仍是实际 instrumented 函数。hook 同时保存三处精确可逆插入、还原后的原 solve 字符串及各自 SHA，并检查原十次试探正文逐字不变；没有改写 `Function.toString` 冒充原函数。

## 5. CLI

下列变量由工作流指向已经校验的实际原件。`QR_RESULT_SHA` 必须从本次实际 QR 输出计算，不能填历史带状方向或未经生成的 hash。

```bash
C=topics/visible-flex-larger-amplitude/computations
QR_RESULT_SHA=$(sha256sum "$QR_OUT/result.json.gz" | cut -d' ' -f1)

python "$C/geometry_20261114_native_damped_chain_trial_replay.py" \
  --failed-directory "$FAIL17" \
  --cold-probe-summary "$COLD19" \
  --first-candidate-summary "$FIRST21" \
  --v2-candidate-summary "$V2_22" \
  --candidate-directory "$CANDIDATE23" \
  --capture-directory "$CAP28/native-correction-capture" \
  --step-directory "$CAP41/native-rawcell0-step-capture" \
  --step-result-sha256 6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf \
  --direct-directory "$ACT54/native-rawcell0-direct-ld" \
  --direct-result-sha256 e60da64312819a87388cfa96c209fc9188dca02c0ab055cbcc934f3507888ac6 \
  --direction-directory "$QR_OUT" \
  --direction-result-sha256 "$QR_RESULT_SHA" \
  --source-topic "$SOURCE_TOPIC" \
  --node-heap 6144 \
  --out "$VISIBLE_OUT/native-damped-chain-original-trial"
```

没有新增第三方包：试探 Python 使用原绑定器所需的 NumPy 及现有原 TailClient 依赖，Node 使用原24.22.1。新入口不调用 SciPy QR；上游 R273 生产者的 NumPy/SciPy 运行环境由其原接口规定。

完整 spec 保存为 `trial-replay-spec.json.gz`。压缩文件 SHA 是 Python、Node、verified intent 和结果的共同身份，另保未压缩字节数与 SHA；Node 按 gzip magic 解压。没有删字段或截断规避 metadata 大小问题。若完整压缩 spec 本身越公开单文件限额，明确报运输失败，不冒数学失败。

## 6. 已执行与未执行

已执行的本地操作只有源文本与语法验证：Python AST；`node --check`；逐字比较原28 `validate_capture`；对原core转换/worker注入在只替换新 Symbol 与来源标记后作源文本相等检查；baseline 调用、完整 direction 调用和 trial observer 逐字相同。对新 R273 实际源的字段合同已作静态核对。

本接口冻结时没有新的 R273 direction result，没有运行绑定构造器、RHS/J/ODE/QR 或原 trial；因此没有填未来结果 SHA，也没有声明 eta=1 的方向在实际原非线性域中可接受。实际57回执应分别报告完整方向计算、原 trial 事实、selected 状态和仍未完成的完整 native 求解。
