# 完整 direct-LD 接口：原 868 步的直接 longdouble 单步矩阵

类型：计算流程与源码接口；作者：geometry / root；日期：2026-11-14。

## 目的和对象

本入口将 actual 50 中实际较好的直接 longdouble 算法用于 actual 41 的全部原 868 步，形成一份新的、完整原坐标 binary64 有限矩阵。它只改矩阵形成的算术路径；原 native 方程、完整非零 H、原状态路径、profile、RK 的 x/h、port、far graph、gains、sigma 及验收规则保持原身份。

actual 50 的完整矩阵误差比较及工作精度见 [实际候选记录](2026-11-14-actual-request50-candidate-precision-and-bytes.md)。单块的改善尚不是新 1372 段系统的可解或方向准确性结论。新矩阵必须一致重解，然后限制回原 577 节点，实际调用原非线性试步。本入口不执行该试步，也不产生已接受的 native 响应。

## 冻结文件

下表文件均放在本课题 `computations/`。本地只做 AST、Node 语法和纯源码字符串反向恢复；没有运行 constructor、RHS、J、RK 或求解。

| 文件 | 字节数 | SHA256 |
| --- | ---: | --- |
| `geometry_20261114_native_rawcell0_direct_ld_capture.py` | 24,018 | `a63ffda643044787cb0ad5fb0d7c2aa4e4b34090fefa4b9053f4f2550bf85dbf` |
| `geometry_20261114_native_rawcell0_direct_ld_capture_hook.mjs` | 50,976 | `3499f7abb96a4f25c4c3a986d97dc8aea3b21742770aabe7abe2822ad8b3caf4` |
| `geometry_20261114_native_rawcell0_direct_ld_window.mjs` | 8,451 | `1ba3f30702b26aa78b4aceb0b2d3d5d71ea8fa858b114d982ead185330faa5d9` |
| `geometry_20261114_rawcell0_direct_ld_worker.py` | 11,428 | `87ab92d9234d6e58103d44d125ce5510f9cde34ac37df251b7e63dcb6747a9c8` |

算术 worker 还严格绑定已经执行过的 `geometry_20261114_saved_stage_rk_covariance.py`，SHA256 `01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548`。它直接调用其中未修改的 `direct_rk`，没有另抄一份数学实现。传入的 `OmittedWorkingFiles` 仅替代该函数的调试文件写入观察器，不修改数组或算术表达式；该函数的全部有限值检查保留。

原 actual 41 三个 producer 文件、原 history/seed/capture readers、完整 source78、原 worker/runtime 全链也按原 SHA 校验。原 `geometry_20261114_native_rawcell0_step_windows.mjs` 的 SHA256 是 `07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b`，没有修改。

## 调用

沿原 actual 41 native lane 的完整历史参数，只新增 actual 41 原件目录：

```sh
python "$C/geometry_20261114_native_rawcell0_direct_ld_capture.py" \
  --failed-directory "$FAIL17" \
  --cold-probe-summary "$COLD19_SUMMARY" \
  --first-candidate-summary "$FIRST21_SUMMARY" \
  --v2-candidate-summary "$V2_22_SUMMARY" \
  --candidate-directory "$CANDIDATE23" \
  --capture-directory "$CAPTURE28" \
  --step-directory "$STEP41" \
  --source-topic "$SOURCE_TOPIC" \
  --node-heap 6144 \
  --out "$VISIBLE_OUT/native-rawcell0-direct-ld"
```

`CAPTURE28` 指固定 artifact 28 内的完整 capture 目录，`STEP41` 指固定 artifact 41 内的 `native-rawcell0-step-capture`。其余变量与已运行 41/47 的父输入相同：17 的完整失败输入、19 的冷初值报告、21/22 的工厂诊断、23 的完整 signed-zero candidate。source78 按原 public 依赖恢复，不能换分支版本或另生成 zero 解。结果文件名为 `native-rawcell0-direct-ld/result.json`；下游必须从这个实际文件计算 SHA，不预填未来结果。

运行只允许 `Rogerhu12/math-research-public` 的 Actions。沿实际 Node 24.22.1、Python 3.12.14、NumPy 2.3.5 及现有 native lane 已锁依赖；不引入第三方 IPC 包。GitHub token 只属于父取件和发布步骤，不传给数值逻辑。

固定实际输入：

| 对象 | result SHA256 |
| --- | --- |
| actual 28 完整原 576 段 capture | `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7` |
| actual 41 完整原 RK 步 capture | `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf` |

不需要重新下载 47/50 的科学大包，也不重新计算 28 的整段 J、41 的旧 binary64 短 J 或 zero 解。

## 原状态与局部 A 的切入点

一个全新原 native 进程完成原握手，恢复 actual 23 的全部 577×224 个状态及负零位，并核对其与 actual 28 原 base、完整 H、原 graphs/gains/far/sigma 的身份。只在原第一请求的 `let initial,predicted=false` 后增加可逆的诊断调用；原 solve、evaluate、trial 和验收正文没有改写，也不会执行到它们。

对每个旧 stage 0…71，按 actual 41 的原 inner→outer 顺序依次取完整 226 维保存输入，包括两项 mean。每步仍用原 profile 对象和原 integrationGrid。普通分支保持原 `x=n*(1/12), h=1/12`，cusp 分支保持原 `x=grid[n], h=grid[n+1]-grid[n]`；不由相邻打印节点重新推导普通 h。实际 868 步来自原 schedule，含四个 13 步 cusp stage，不能硬改成 72×12。

新 window 在原 41 函数上只作两个可逆文本变化：选择当前原 profile/step；跳过旧 binary64 tangent 三重乘加。完整 state 的 increment、四次 `rhsWithJacobian`、最后 state 更新及原 root guard 保留原表达式。内部未使用的零 tangent 工作量不导出为 J。纯源码往返实核所得新 function SHA256 为 `d62fe2c45e4fbfda015ccac588e29e9ba2d7df932bb584124eff3704417876cb`；没有用这条源码检查冒充数值通过。

每步实际需要四次原 `rhsWithJacobian`，成功时总共 3,472 次，取得完整 226×224 局部矩阵。输入、四级状态、几何数值字段、原 root 标量记录、x/h、完整输出和 post-port shape 输出逐字与 41 比较。root 身份的范围是原保存的 `e.minA/e.minD/err/scale` 与累计标量，不声称已经逐字核对未保存的完整 root 系数数组。来源身份不符会如实停机，不把异场读出混入本次目标。

## 直接 longdouble 形成及单次 cast

原 Node 进程将四个完整 binary64 A 经有长度和 SHA 的 pipe 发给一个常驻 Python worker。worker 按原比特读取 h 和 port，在实际 longdouble 类型中调用 actual 50 的原 `direct_rk`。全部跨模项、224 个输入列和两行 mean 保留；mean 不进入下一阶段 shape 的乘法。只在原 stage 的最后一步对 Pi 输出行除原 port，其他步骤的 port 是 1。

工作矩阵最后只转一次 `<f8`，再按原字节切成 224×224 shape 与 2×224 mean。**这两份原坐标 binary64 数组是唯一的完整目标。** 当前没有 G-shadow，也不将每步 field-a/d frame 误当成唯一共享节点 G。下游若用坐标平衡，仍须对这里定义的原坐标目标和原 sigma 读回。

worker 记录实际 longdouble dtype、有效数位、指数范围与平台；不把 16 字节存储误称 binary128。成功步骤只保存最终 shape/mean 和完整来源记录，不保存全部工作 longdouble 矩阵或全部四 A raw。每个 A 的完整 hash、维数、原状态/几何身份及形成源都保留；失败步骤尽可能保留其已取得的完整 A raw 和最近完整输入，不把失败包装成一个完成 target。

## 完成输出合同

顶层 result 的 schema 是 `native-rawcell0-saved-step-direct-longdouble-maps-v1`。真实完成时 `completed` 与 `capture_completed` 同为 true，且只有一个原协议请求、原 worker 正常退出、完整 72 stage/868 map/3472 field 和预定 STOP 证据。`native_accepted`、`task_completed` 仍为 false。

result 与 summary 均保存 `source_sha256`、`hook_sha256`、`window_module_sha256`、`worker_source_sha256`、`direct_arithmetic_source_sha256`、`actual41_result_sha256` 与 `original_capture_result_sha256`；后者还以兼容字段 `capture_result_sha256` 保存。`summary`、`array_manifest`、`stage_reports` 都是 `{file,bytes,sha256}` 描述器。不得把一次诊断 STOP 写成 native 失败的数学结论，也不得把完整捕获写成已接受响应。

summary schema 为 `native-rawcell0-saved-step-direct-longdouble-summary-v1`。manifest schema 为 `native-rawcell0-direct-longdouble-output-arrays-v1`，以 list `arrays` 保存 144 个数组：每个旧 stage 两个。entry 沿原 StepArrays 规则保存 `name,dtype,order,shape,total_bytes,raw_sha256,completed,chunks`；每个实际步骤一 chunk，含 `array,chunk_index,row_start,row_stop,file,bytes,sha256,raw_sha256`。交错 JSONL journal 保实际写入顺序，不要求先写完一整数组。

每个 stage report 的 schema 为 `native-rawcell0-direct-longdouble-stage-report-v1`，主要字段如下：

| 字段 | 含义 |
| --- | --- |
| `stage` / `original_stage`、`step_count` | 原 stage 与真实 L |
| `arrays.shape_jacobians` | manifest name；`[L,224,224]`，inner→outer |
| `arrays.mean_jacobians` | manifest name；`[L,2,224]`，相同顺序 |
| `actual41_full_states_raw_sha256` | 原完整 `[L+1,226]` 输入/输出字节身份 |
| `actual41_shape_outputs_raw_sha256` | 原 `[L,224]` post-port shape 字节身份 |
| `schedule`、`profile_schedules` | 原 41 字典逐项原样保留 |
| `direct_ld_step_reports` | 完整新逐步证据 gzip 描述器 |

原 schedule 内的 `shape_J_statistics` 属于原 41，report 明确标识其原件身份；不能当作新目标的统计。新逐步 packet schema 是 `native-rawcell0-direct-longdouble-step-evidence-v1`，包含 `steps` 与 `fields`。每个 step 有原 stage/step、完整 schedule、五个来源身份布尔项、四 A 的 hash 列表、四级原/新状态与几何 hash 对照、worker 的完整结果收据。每个 field 去掉新 `local_A` 描述器后与原 41 field 记录相同。

新 J 的 shape raw 总量为 348,422,144 字节，mean raw 为 3,110,912 字节，合计 351,533,056 字节，均在独立 `large-arrays/` 中，仅进 artifact。四 A 若全存需另 1,406,132,224 字节，本接口没有为机械审计扩大到这项存储。原 47 已保存最坏代表一步的四个 A；其他步骤保完整 source/input/hash 可再生身份。

## 与新 1372 系统及原试步连接

独立 `exact_20261114_rawcell0_direct_ld_system.py` 绑定原 28/41 完整系统，只替换前 868 个短块，后 504 个原块逐字复用。旧 `old_to_new`、1373 个 base 节点、全部原 residual、cut、far、sigma、mean/port 语义与 577 节点限制保持原件。新 target 有自己的 matrix identity，不能沿用旧 `e929…` 有限矩阵身份。

`exact_20261114_rawcell0_direct_ld_equilibrated_correction.py` 对该新目标形成方向并在同一原坐标、原 sigma 下读回；它的实际 result SHA 由后续运行决定。原十试步薄入口属于下一消费者：用真实新方向的原 577 节点限制，保持原 evaluate、guard、十个 alpha、严格原范数下降，首个接受步后 STOP。没有新增 exact 小缺陷门，也不会重派早已证坏的 43 方向。本次仍只是必要的有限矩阵构造，不宣称大核闭面或本课题完成。

## 54 运输修复版本

实际52在启动worker前命中完整spec的旧明文1MB上限。当前表更新到[完整gzip transport](2026-11-14-direct-LD-gzip-specification-transport.md)的真实源身份；旧52由原commit保留。spec现在完整存direct-ld-spec.json.gz，两读取端按magic解压且spec SHA仍绑定压缩file bytes；没有改变任何数学表达式或省略字段。54真实结果尚待Actions。
