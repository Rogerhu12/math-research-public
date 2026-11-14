# 同一固定标量度量下的 Rφ 精化与真实 live TailClient 接线

**状态：未执行的新消费者/求解包装源；不是新的数值接受结果。**
截至本条编写时尚没有可供此入口消费的真正接受 full-DN parent。三份新源只做了纯 AST 检查；没有本地 import、科学计算、尾部求解或伪造 parent。实际计算仍只能在本公开仓库自己的 Actions 运行。旧失联未推草稿不作为这三份文件的来源身份。

## 1. 文件与不变的有限问题

| 新源 | SHA-256 |
|---|---|
| `computations/geometry_20261114_same_metric_physical_response.py` | `ddefb80f40e1014bda90def8715138c0e3e21030bfed38691395aaa074017229` |
| `computations/geometry_20261114_same_metric_physical_full_dn.py` | `ea8c95192d3271175d9faeb16081cc535974d3a6b76e1ac41e1354c0a61e4f6e` |
| `computations/geometry_20261114_same_metric_physical_after_accept.py` | `62002f64530a4d1ef81ef24fe0f4b485e02909b2de868529d96d3d7c80fa9e09` |

入口调用原 `same_metric_prepare.validate_parent`，要求 parent 的真实 success/status、完整 RMS/BC、physical frozen RMS、对应完整最终 tail audit 与原 input-config SHA。另要求 parent 明确属于 `physical-phi-complete-DN-v1`，不把旧 Rθ 接受改称 Rφ 接受。prepared 的全状态、parent binding、完整标量规范、原 accepted96 来源和原 port 全部绑定。

沿用 R240 的 v4 定义：首个 v3 的完整标量构造、三个已解控制 $p_*$、全部区间/支撑和物理 cut 冻结；新 field/tail 模数均为 $M$，所有 core 自由，固定 core 数 $K=0$、活动标量数 $k=0$。物理状态 $3M+2$ 行包含完整 $z_0$；增广状态 $4M+2$ 行，左端 $3M+2$ 行，右端 $M$ 行。并未用空活动参数覆盖原三个冻结参数。

右边界仍调用已推 `PhysicalTestBoundary` 的完整 R252 映射

$$
R_\varphi=v_{\rm nonmean}-\gamma S(c)D\bigl(\epsilon_hP(c)z\bigr).
$$

原 Frenet 方程、完整 core、材料高度、native DN、所有 J 行保持原样。原 `same_metric_full_dn.py` SHA 为 `8aebffdb0047aed04f640d540e1c44255d995307ba7aa9b8ff3c5b5529cf57f6`。可选原完整 separated QR，或经小桥接调用已有完整 band LU；没有另写 solver，也没有把未接受的约束 LSMR warm 当成接受器。

## 2. 真实新 H/J 与同一进程所有权

response 入口先由新 prepared 端点和原完整 `MaterialTrace` 计算实际 $H$，再通过原 `exact_20261114_true_tail_client.py` 请求 `jacobian=True,audit=False`。新 $M$ 或新 $H$ 均真正求解；不把旧 T96/T112 零响应升格到新模数，也不阈值化小非零系数。native 的 modes/quadrature/steps/auditSteps 可以显式加密，其余物理和 solver 设置与 parent 一致；保留原容差、物理 depth、shooting partition、Newton 和 line search。

实际首响应核对其 request/response、runtime/input config、完整源清单、ready/checkpoint 参数、全部 shooting states/raw-node copies、完整 $(3M+2)M$ 个 J 元素、三个非均值 jet 和四个均值 jet。first-slope 和二阶/高度差分 J 的原方法亦明确保留；不会用 `ready.linearD` 充当真实 J。

随后原三个中心差分步长、两档四阶 Richardson、收缩检查及 `5e-5` 门均照旧执行。FD 只调用这个已完成真实 H/J 的**显式仿射图**，不向 native worker 发送扰动高度。完整 native 响应及 FD 的原粗误差全部保存。

`--with-response` 通过后，把**同一个 Python client、同一个仍存活的 Node worker 和同一个 FrozenCompleteProfile 对象**交给原 full main。原 native predictor 保持实际状态，没有跨进程导入非零响应，也没有手工捏造 predictor。原 full main 精确保留 warm 的已有端点；其首次同 H unaudited 请求可由该真实 client 自己的内存 cache 命中，`live-tail-handoff.json` 会记录实际 worker call 数变化。若 H 真变了，原 client 发真实请求。最终 `audit=True` 原生绕过 cache，仍真正计算完整最终 audit。任何 FD 失败、异常、完整求解返回或前置身份/写入失败都会关闭 live client。

完整 full 和 frozen-physical RMS `1e-6`、BC `1e-11`、原 Newton/17-trial backtracking、实际新 H 外迭代以及最终 audit 原门均未改。最终仍单独测量旧 Rθ、均值和完整角 seam，不能从新有限 Rφ 通过推断它们通过。

## 3. 真正接受 parent 后的调用

下列命令仅是未来 Actions 接线示例，变量必须指向实际接受原件；本条没有执行它们。

```bash
python "$C/geometry_20261114_same_metric_prepare.py" \
  --parent-field "$PARENT" \
  --parent-tail-response "$PARENT_FINAL_TAIL" \
  --parent-tail-config "$PARENT_CONFIG" \
  --field-modes "$MNEW" --angles "$NNEW" \
  --subdivisions 2 --max-nodes "$MAX_NODES" --out "$PREP"

python "$C/geometry_20261114_same_metric_physical_full_dn.py" \
  --with-response --linear-backend qr \
  --accepted "$ORIGINAL_ACCEPTED96" --port "$ORIGINAL_PORT" \
  --parent-field "$PARENT" \
  --parent-tail-response "$PARENT_FINAL_TAIL" \
  --parent-tail-config "$PARENT_CONFIG" \
  --warm "$PREP/prepared.json.gz" --out "$FULL" --work "$WORK" \
  --tail-client "$C/exact_20261114_true_tail_client.py" \
  --tail-config "$NEW_CONFIG" --tail-source-root "$SOURCE_TOPIC/repro/source-root" \
  --material-angles 4096 --physical-angles 4096 \
  --node-heap 6144 --jac-workers 2 --max-nodes "$MAX_NODES"
```

`MAX_NODES` 须按实际 parent 和后端资源设置：单纯径向二分已需要至少 `2*(parent_nodes-1)+1` 个节点，699点 parent 就至少1397点，不能照抄初次求解的1200预算。已有解上的明确同g加密与对失败初猜无依据抬上限不同；实际运行仍要保存所用预算和资源，不预报此时尚不存在的parent节点数。

`NEW_CONFIG` 可由原 true-client 的 `prepare_config` 从 parent config 生成，明确新模数/角数与需要加密的 RK 数。两个边界角网格都必须严格大于 $4M$，native 则继续满足原更强的 `quadrature > 4*M*spacing`。`WORK` 仍须在上传结果目录之外。`--linear-backend banded` 仅选择现有完整 band LU。

response 默认保存在 `$FULL/response`。不要先单独运行 response 再期待另一个 full 进程复用其 native predictor；独立 response CLI 完成后会关闭 worker。正常完整路径使用一次 `--with-response`。

若 parent 有原真实 producer 导出的标量 sidecar，可加

```bash
--parent-scalar-descriptor "$PARENT_SCALAR_DESCRIPTOR"
```

这要求其 SHA 绑定 parent 的 actual 文件且 `origin=actual-live-profile`，并逐项比较完整 finite-Gauss 数学表达。没有该 sidecar 时，仍绑定原 v3 全公式/p*，但报告 `parent_live_mathematical_identity_verified=False`；不会冒称已经确认不同进程浮点构造常数相同。

## 4. 接受结果、标量来源及后续读出

真正走完原完整接受路径后，新入口写出原 `actual.json.gz`、fresh `actual-tail-final-audit.json.gz`、`physical-test-final-cut-audit.json`，并从**实际用于这次求解的同一标量对象**导出 `frozen-scalar-descriptor.json`。该 sidecar 含真实 Gauss 表、构造常数、原支撑/分段和 $p_*$，并绑定完成后 actual 文件的 SHA，避免循环哈希。它定义同一有限 Gauss 实表达，不证明 literal binary64 evaluator 与该精确实表达的误差，也不自行证明 scalar 接口全局 C²。

```bash
python "$C/geometry_20261114_same_metric_physical_after_accept.py" \
  --checkpoint "$FULL/actual.json.gz" \
  --port "$ORIGINAL_PORT" --tail-config "$NEW_CONFIG" \
  --tail-response "$FULL/actual-tail-final-audit.json.gz" \
  --source-topic "$SOURCE_TOPIC" --out "$READOUT" \
  --angles 2048 4096 --radial-subdivisions 2 4 --readout-levels 1,2,4
```

该入口强绑定 actual/final-tail/config、独立 cut report 与 live scalar sidecar，调用原 v4 material-prefix、material-cut 和 own-tail closed 读出，保留新有限边界语义。没有继承 parent 的幅度、reach 或全域误差证书。R249 inlet normalization 仍是另行明确标识的有限场构造，不能混用未规范化 prefix 报告和规范化闭组装。采样全闭指标、真正同 g 加密下降、整面/全部 t 的 operator 与 reach/held 证明仍须实际完成。
