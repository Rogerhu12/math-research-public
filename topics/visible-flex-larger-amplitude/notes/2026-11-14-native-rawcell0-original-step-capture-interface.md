# rawCell0 的全部原 RK 步：局部 J 与完整状态采集接口

2026-11-14。[actual39](2026-11-14-actual-request39-native-split-direction-failed.md) 的新578段系统仍有巨大完整缺陷；51个已报块最大值大于1，全部位于 rawCell0，且原43已拆出的短块仍参与。因此本入口直接回到同一 actual28 基态，在 **原 stages0..71** 保存逐原 RK 步的局部 J。它不只针对当前一个最坏段，也不沿用失败方向。

本文冻结时尚无本入口的 Actions 数值。以下为已完成的独立源与可执行接口；本地只做 AST、Node语法与纯字符串源变换/逆变换核验，没有运行原 constructor、RHS、RK、J或科学读出。

## 1. 冻结源与同一原输入

| 独立源 | 字节 | SHA256 |
|---|---:|---|
| `geometry_20261114_native_rawcell0_step_capture.py` | 13149 | `c2341018c6293e15ee8e5ba9109b331b29bee2e3e944514e1a0308afe8e6ffd5` |
| `geometry_20261114_native_rawcell0_step_capture_hook.mjs` | 43277 | `2695cd2dc0abc66fe3f8ae8987b6ae3b50b884f692a418198347a61dddf24435` |
| `geometry_20261114_native_rawcell0_step_windows.mjs` | 11654 | `07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b` |

原 finite尾的源、参数和验收方法不改。launcher复用冻结25历史绑定与28数组绑定，锁定 actual17/19/21/22/23、同一112项非零 H、完整577×224 seed及其9546个负零、原 config/source/ready/capacity、graphs/gains/far、全原σ和live stage layout。原 actual28 result 固定：

`ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。

`CapturedArrays` 仍核整个原artifact的全部数组字节；只为72目标段复制 input224、原 withJac `stage-out`224、原 `[minA,minD,meanHeight]`3项小参考。不复制或重算72个原长 J，更不重算576段整尾 J。原余504块将在独立后继消费者中逐位复用。

原 worker 仍先正常完成真实构造和握手。只有第一条原协议请求、完整身份核完之后，才进入采集函数。请求 flags 保原 `jacobian=true,audit=true` 以保持协议身份，**不表示本次实际计算完整 endpoint J 或 audit**。

## 2. 原状态路径与新的局部切向表示

窗口模块逐字锁定原 `78718-tail-fourier-product-flow.mjs`：

`717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f`。

它从该源取出原 `flowStateWithJacobian` 函数，保原 profile loop、RK四个 field/increment、state/tangent更新算式和返回语句。五处插入仅增加只读观测，以及在**每个原 RK 步开始时**把局部 tangent重置为原224列单位基。删除五处插入必须逐字恢复原函数；实际运行时还记录源、函数和改动清单 SHA。

这定义了独立的逐步有限 variational 表示。没有把新局部 J 的浮点乘积称作旧长 J，没有相乘重建旧长 J，也没有将计算所得 J等同精确实数程序导数。后继缺陷账仍遵守 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md) 的对象区分。

每个原 stage 的入端取原 `states[n+1]`，前224项保持bits；按原 cellFlow 初值在末尾补两个正零 mean积分状态。**完整226项状态贯穿所有原步及profile**，只在下一个原 stage 开始时重新采用该段原入端。新插入节点不清零mean，不改变state RHS或state更新。

出口沿原 cellFlow 表达式：仅原段最后一步将Pi及J的Pi行除原 `portRatio`。其他局部步骤不施加port。额外两行 mean tangent也保存；它们不被误充作224项shape未知量。最终mean仍用原 `state[224]+state[225]` 加法，整尾 mean的原归并和最终读出未由本采集替代。

## 3. 普通调度与 cusp 调度分别保留

原 `integrationGrid` 从原 source root的同一module URL导入，固定原源：

`b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f`。

该 hash 必须同时出现在已经核定的原 consumed-source map，并与实际恢复文件一致。没有重写grid，也没有把 `steps` 改小或将profile重新映射到小区间。

- ordinary分支保原 `x=n*(1/12), h=1/12`。
- 有cuts时保原 `integrationGrid(12,cuts)` 及原 `x=grid[n], h=grid[n+1]-grid[n]`。
- 真实profile observer保原cuts、grid、count、ordinary_h的全部 f64位；真实step observer保实际x/h位。普通分支的h不从相邻打印grid节点重算。
- 本入口不运行独立no-J路径；原no-J的 `k/12` 浮点算式不被冒称与withJac处处相同。

总步数L只取原函数实际生成的profile count和完成记录。原live metadata显示4个rawCell0 stage带cuts，但此入口不把总数预编成一个假定常量，也不忽略cusp插入的步。

每次原 `rhsWithJacobian` 已返回的 `root.g` 中全部number字段均按bits保存，明确包含实际可用的 `r,drdx,w,w2,E`。同时保其原 minA/minD、root error/scale、实际x/h及输入state SHA。这个只读观测不增加任何RHS、root、geometry或J调用；缺字段如实标记，不补造数值。

## 4. 大数组流式合同

每个原stage的四个数组均采用 `<f8`、C order，按照真实 **inner→outer flow顺序** 逐步写入 `large-arrays/`：

| report中的array key | 完整shape | 内容 |
|---|---|---|
| `full_states` | `[L+1,226]` | 初值及每原步完成后的完整state；不施加出口port |
| `shape_outputs` | `[L,224]` | 各步实际shape输出；仅最后一行按原port转换 |
| `shape_jacobians` | `[L,224,224]` | 每原步从单位切向出发的局部J；仅最后一步按原port转换 |
| `mean_tangent_rows` | `[L,2,224]` | 同次实际局部变分的两条mean行，未施加port |

每步完成后即时同步写文件并hash，之后才进入下一步的tangent重置。内存不保存整个rawCell0的新J，也不等待72段全完才落盘。

`rawcell0-step-array-manifest.json` 的 `arrays` 条目兼容原28字节规则：

```text
{name, dtype:"<f8", order:"C", shape, total_bytes,
 raw_sha256, completed, chunks:[
   {array, chunk_index, row_start, row_stop, file, bytes, raw_sha256}
 ]}
```

`large-array-chunks.jsonl` 按实际完成顺序即时交错记录四个数组，不能假定其顺序等于manifest按array分组后的flatten。独立消费者按 `(array,chunk_index)` 核唯一、完整coverage及各array连续行序，并重核完整raw SHA。

每stage的 `stage-NNN-completed-report.json` 包含 `stage,step_count,arrays,profile_schedules,schedule`。`profile_schedules` 每项有 `profile_index,grid_branch,step_count,cuts,grid,ordinary_h`；`schedule` 每步有 `global_step,profile_index,grid_index,grid_branch,x,h,final_original_step,port_applied,port_ratio`。其中 `port_applied`为bool，`port_ratio`与x/h一样是带 `float64le_hex` 的number record。

真实field-geometry记录按stage gzip，放在同一 `large-arrays/` 下，manifest的 `metadata_packets` 另列压缩/解压 SHA。shape J、fullstate、mean与field数据均artifact-only；Git保源、结果、manifest和小结，不能把几百MB新J加入仓库。

## 5. 原出口对照、部分失败和停机

每个原stage都将最后出口与 actual28 `stage-out` 逐位对照，并记录原σ下的浮点最大差；将原 `[minA,minD,meanHeight]` 三项同样比较。这些是实际观测，**差异不作为新增科学接受门**，不能因probe流程完成就宣称出口一致或新矩阵有效。

原guard或其他异常发生时，保此前完成的所有chunks、当前stage已完成步、实际profile/schedule，以及最近一次field的完整226项输入和实际错误。`completed_local_J_evaluations` 与完整保存的 `completed_local_J_blocks` 分开，实际field入口与成功返回数也分开。返回了非有限局部J而原函数未抛错时，原bits和位分类仍保存，不阈值化、不删模、不编造失败原因。

全72段采集完成后写summary、manifest和候选layout，然后在原native solve之前抛出：

```text
VISIBLE_NATIVE_RAWCELL0_STEP_CAPTURE_COMPLETE_V1
```

原worker如实返回failed字符串；Python只有核到这个planned STOP、单次协议请求、正常进程退出、全72段完成及全部计数一致时，才置 `capture_completed=true`。`native_accepted=false,task_completed=false`始终保留，原worker成功响应cache、last和tangentPredictor不填入诊断对象。

关键文件：

- `result.json`：schema `original-native-rawcell0-step-capture-result-v1`，实际身份由后继CLI显式给定SHA。
- `rawcell0-step-spec.json`、`rawcell0-step-summary.json`；summary的 `stage_reports`是72个 `{file,bytes,sha256}` 描述符，含真实 `total_step_count`。
- `rawcell0-step-array-manifest.json`、即时chunk ledger、每stage报告和field packets。
- `prospective-rawcell0-step-layout.json`：尚未安装进原dn的新shooting索引和显式σ说明。

## 6. 动态新系统的合同

动态消费者直接以原 actual28 的576段为父，不在失败578系统上累叠。原0..71被本次实际局部J替换；原72..575共504个J及对应旧入端、输出、残差逐位复用。

若原stage n有L步，shooting row以外→内排序，故本stage flow step k对应新row `offset+L-1-k`。旧577节点保持原bits；插入节点取对应 `full_states[k][:224]`。内部块输出减其真实中间节点，最外块用真实带port出口减旧节点，不能用旧r掩盖实际出口差。

全部旧节点σ保持；各插入节点明确复制其原parent stage的σ。`explicit-step-node-scales` 的shape为 `[1,newDepth+1]`。新layout同时记录 `oldToNew`、原stage与实际step来源、全cut/far/H的原身份，以及真实D下的资源预算：

`dimension=(D+1)*224`，`kl=112`，`ku=335`，LAPACK AB为 `560 × dimension` 个binary64。

预算另列可能LU副本；它不是实际RSS或新系统成功声明。新完整矩阵有独立source/result/所有局部J身份，不能称为原 `394ca2…` 长矩阵。新方向未来限制到旧节点后，仍要真实执行原完整nonlinear no-J/trial及原验收；旧长J缺陷只留诊断。

## 7. Actions CLI

沿actual38同一输入接线，仅换新入口和独立输出：

```bash
python "$C/geometry_20261114_native_rawcell0_step_capture.py" \
  --failed-directory "$TOPIC/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$TOPIC/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$TOPIC/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$TOPIC/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$TOPIC/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --capture-directory "$CAPTURE28" \
  --source-topic "$REPO/topics/visible-flexible-closed-surface" \
  --node-heap 6144 \
  --out "$OUT/native-rawcell0-step-capture"
```

`CAPTURE28`仍由固定原artifact下载器提供，只读使用。不需要actual39坏方向，不重算zero solve，不改变 `linearSteps`、far graph、原容差或原g。数值只能在公开仓库Actions运行。
