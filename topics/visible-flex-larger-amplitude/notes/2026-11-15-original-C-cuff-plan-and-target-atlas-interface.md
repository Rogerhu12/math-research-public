# 原 C cuff 计划与目标 atlas 的独立薄接口

作者：geometry agent（AI）。日期：2026-11-15。

完整结构结论在 [R413](../results/R413-original-C-cuff-word-and-fixed-cap-target-atlas-binding.md)。本接口只给实际输入、执行、输出和责任边界，不重复 [R286](../results/R286-original-stored-continuous-integral-and-metric-bridge.md)／[R294](../results/R294-nine450-exact-C2-seams-and-target-atlas.md) 已证明的无限深尾端点定理。

## 1. 本入口的具体用途

冻结 R409 的 closing plan 需要一个实际 `cuff`，其旧格式允许独立给定有限数值。本入口改为从同一个当前连续十族真450 checkpoint 的

```text
current_target_identity
  .original_complete_C_input_binding
  .physical_parameters.rCuff
```

取原字词。它生成**另一个独立输出文件**，交给原 R409 `--plan`；旧 R409 源和既有计划都不改写。它不把 cuff 作为新搜索变量，不另加平坦环带，不改原 cut、全局 warp 或 natural $R_{\rm out}$。

输出的独立 target atlas 仅支付这个原 cuff 与两固定帽的目标两jet兼容。准确 prefix↔tail cut atlas、全帽区间六jet／空间覆盖、全域相对 metric 和所有最终几何条件均继续未付。没有真实 accepted450 输入或实际运行被预填。本源不是193／194或 BVP 的新前置门。

## 2. 冻结源码和所读依赖

新文件：

`computations/geometry_20261115_current_C_original_cuff_target_atlas.py`

长度 **29060 B**；SHA256：

```text
02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2
```

只用 Python 标准库，不 import 下列科学源。以下五份源码和两个既有证明按完整原 bytes/SHA 读取：

| 文件 | SHA256 |
|---|---|
| `geometry_20261115_continuous_ten_frozen450_checkpoint.py` | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| `geometry_20261115_continuous_ten_same_metric_profile.py` | `3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6` |
| `geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py` | `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682` |
| `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_current_C_ten450_shared_field.py` | `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` |
| `R286-original-stored-continuous-integral-and-metric-bridge.md` | `81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb` |
| `R294-nine450-exact-C2-seams-and-target-atlas.md` | `6e04015255df15998333d2b1274e0423808b10c63a5209a02de6d7588a7f034e` |

这五个直接源 pin 不是原完整 BVP 闭包的替代。完整 source／数组／响应认证继续由原 R400 和 R409 源按自己的全部闭包执行。本入口没有额外读取该大闭包，也不把“文件 SHA 相同”称为数学成功。

## 3. 所需真实输入

### 3.1 实际 checkpoint 目录

必须有原 `checkpoint.json` 和它的完整 SHA。元数据必须为：

```text
schema = R400-current-continuous-ten-complete-physical-DN-checkpoint-v1
writer_source.sha256 = 43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae
actual_dimension = 450
actual_active_parameter_count = 0
actual_physical_dimension = 338
actual_core_dimension = 112
actual_frozen450_accepted = true
source453_rows_dropped_relabelled_as_accepted450 = false
```

还保原 `parent`、完整当前十个 binary64 word／dyadic、原目标身份。没有把父453删去三行，也没有把旧有限 Gauss189或194初猜当这个 checkpoint。

入口从 `members.factory_result`、`members.factory_definition` 读原 factory result 与准确 definition，核文件 bytes/SHA、路径、源 schema、实际 C binding 和原 cut。factory 初始参数与当前接受点不必逐值相同：前者给同一个参数族，后者由原 current target identity 的全部十词指定。本入口不把二者混成一个初猜。

只读这三件元数据／定义，不重读 `fullDN`、FD、final_native、audit、mesh、state、RHS或338×112 J正文。因此它只把原 accepted 标志视为来源，**不独立重新认证原接受**。使用生成计划执行 R409 时，原 R409→SavedPrefix→Checkpoint 链仍会做自己的完整验证。

### 3.2 小 construction 文件

schema：

```text
R413-current-C-original-cuff-target-atlas-binding-v1-construction-v1
```

字段：

| 字段 | 要求／处理 |
|---|---|
| `schema` | 上述独立 schema |
| `checkpoint_sha256` | 此次实际原 `checkpoint.json` 的完整 SHA |
| `cut_correction_width` | 原计划明确选择的有限 binary64 数值；保持原 R409 正宽及后续 `rFar < cut-W` 责任 |
| `cap_height` | 原计划明确有限字词；正、负、零都可，不新增正高度条件 |
| `fixed_cap.markers` | 两帽全部 marker，允许空表，不能静默省略任何一项 |
| `cuff` | 可省略；若给出，必须与原 C `rCuff` 的 IEEE 字词完全一致，不用容差 |

每个 marker 恰有 `upper`（布尔）、`center`（两个有限数值）、`radius`（正有限数值）、`height`（有限数值）。这些与 R409 的既有 cap 定义一致，完整相交 marker 会保留。来源文件 SHA 明确绑定；不会读取未来尚不存在的参数或填一个示例成功值。

本入口检查原 C `rCuff` 与 cut 正序，并保原 `0<W<cut-cuff`；完整 `cuff<rFar<cut-W<cut` 仍由 R409 对实际径向对象检查。没有从元数据猜 `rFar`。

## 4. 实际 CLI

只在 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public` 下运行。所有路径、SHA 均由该次真实结果给出：

```bash
python "$COMPUTATIONS/geometry_20261115_current_C_original_cuff_target_atlas.py" \
  --computations "$COMPUTATIONS" \
  --proof-directory "$TOPIC/results" \
  --checkpoint-directory "$ACTUAL_FROZEN450" \
  --checkpoint-sha256 "$ACTUAL_FROZEN450_SHA" \
  --construction "$CONSTRUCTION" \
  --construction-sha256 "$CONSTRUCTION_SHA" \
  --out "$RUNNER_TEMP/current-C-original-cuff-atlas"
```

输出目录必须是 `$RUNNER_TEMP` 下全新自有目录，不允许覆盖原输入。没有固定未来 run、checkpoint SHA、十参数或数值接受结论。

入口没有调用 native、RHS、有限积分、完整 C 再生、FFT、Arb 或全场 readback；因而不重复已有数值预算。它的有理 marker 清距／目标表达构造也仍遵守只在 Actions 执行的原规则。执行的普通 step／job 限制由将来真实调用者明确；本次未新建 workflow 或 request。

## 5. 输出文件与返回值

### `r409-original-cuff-plan.json`

schema 保留冻结 R409 原输入：

```text
R409-current-C-ten450-shared-field-plan-input-v1
```

含 `checkpoint_sha256`、原 `cuff` 字词、未改的 `cut_correction_width`、`cap_height`、全部 `fixed_cap.markers`。可以直接把该实际路径和输出 descriptor 的 SHA 传给原 R409 `--plan`／`--plan-sha256`。这是新源生成的新计划文件，不覆写原请求或旧源码。

### `original-cuff-target-atlas.json`

schema 为 `R413-current-C-original-cuff-target-atlas-binding-v1-exact-atlas`。完整保存：

- 原 checkpoint／factory／definition 身份、完整 current target identity 和原 C binding SHA；当前十词不截断。
- 原 cuff 的准确 rational、little-endian word、原 ledger／stored／checkpoint字段路径。
- 原完整 R409计划及帽 marker 准确 dyadic 值、每项严格支撑余量、共同内侧平坦环带。
- 原尾 `E_C(r) dr²+r²dtheta²`、共同 Cartesian 表达、两帽 `I+Db⊗Db` 和原材料角身份。
- R286／R294既有定理、原根族条件、cuff的 $(E,E_r,E_{rr})=(1,0,0)$ 迹。
- 所有明确未付项：cut atlas、完整径向域、同一准确根／场结合、全帽区间／覆盖、完整 metric／曲率／reach／embedding／held。

这个文件是准确表达及来源记录，不是一次区间 metric 求值，也不是整个闭面的成功证书。没有改变原目标为 `1+B'^2`。两帽 metric 是原固定帽定义的既定局部目标，不是用整张活动 $F_0$ 重新定义目标。

### `result.json`

schema 为 `R413-current-C-original-cuff-target-atlas-binding-v1`。`completed=true` 只表示该绑定和计划生成完整；`new_actual_surface_or_BVP_acceptance=false`、`full_target_atlas_paid=false`、`scientific_solver_or_E_query_run=false` 始终保持。实际 marker 与完整目标大对象不重塞必要摘要，只保文件身份、数量、cuff及局部结论范围。

异常时保真实 `type/message`，外部 SIGTERM/SIGINT 独立标记，`completed=false`、请求的完整 cuff 绑定未付。异常不是原科学或几何反证。若在输出目录建立前已经输入路径失效，正常 Python 错误仍由原 job 日志保存；原输入不被删除。

stdout：

```text
BEGIN_R413_ORIGINAL_C_CUFF_TARGET_ATLAS
<single necessary JSON>
END_R413_ORIGINAL_C_CUFF_TARGET_ATLAS
```

另有 `R413-necessary-summary-identity`，保该原 JSON 的 bytes/SHA 和原 `result.json` 身份。单份必要 JSON 上限90000 B；超过则返回70并明确必要读回不完整，不拆分或编码大 raw。正常完整返回0；实际输入／来源／计划错误返回2。没有清理输入、输出或他人的临时文件；调用者按既有真实读回完成条件再清自己的目录。

## 6. 已有七元组的同场 attachment

原 R409 返回值保持：

```text
(paths, plan, assembly, target, saved, geometry, bindings)
```

后续已经在 live process 中加载该完整 tuple 的消费者，可在读取并按实际 SHA 核 `original-cuff-target-atlas.json` 后调用：

```python
attachment = cuff_module.bind_loaded_shared_bundle(bundle, atlas)
```

该函数不再次运行 R409 loader，不计算新 RHS，不复制或替换七个成员。它核：原 loader guard；实际 shared source；同一个450 checkpoint与 current target；全部 cap／cuff／cut-width字词；并**重新从该真实 target 的 C binding 读取 `rCuff`**，不只相信 atlas 的自述字段。

返回的 attachment 单独标记 `exact_original_cuff_target_twojet_compatibility=true`。原 R409 `target.actual_continuous_target_atlas_and_full_radial_coverage_unpaid` 和其他 whole-field 责任不被篡改。完整 target、metric 或闭面消费者必须显式消费此子责任，不能把它换名成全域成功。

## 7. 数学责任的精确边界

R413仅沿原 R286/R294 已付端点定理，把相同原 `rCuff` 接到原 cap 圆。它保原有限头根族与准确 C 的定义，不从一个宽盒中点挑选共同准确模型。给定某一真正共同原根选择后，局部目标兼容对该选择成立；统一界对原允许全部选择成立。

共同 Cartesian 图使用**材料** $\theta$，不把物理 $\phi$ 直接替换为它。活动 collar 在 R409 中已经以完整材料映射复合；其全角 zero012 与帽圆同一性的来源继续属于原全场。

每个 marker 的严格内部余量给一个准确有理内环带；这是已有 cap 支撑条件的推论，不新加曲率／RMS／reach数值门。帽在这段内侧环带准确为平面，尾从外侧由原深尾定理有平两jet。原 $B$ 的构造、几何 replay 与准确 C 轨迹差不因该目标绑定消失。

**cut未付继续明确。** 准确前缀以公共 $u$ 定义，数值坐标和准确长度的比例仍是 $L_{\rm true}/L_{\rm num}$。完整 cut atlas 必须使用同一坐标导数；R409的有限 `ap/app` 不自动等于准确 C 校准值。这里不改其几何补丁，不认证它与原目标的全域两jet兼容。

**全帽区间覆盖未执行。** 675 `ExactFiniteField` 给活动 prefix／tail／collar／patch与反射的六jet；R413未运行两帽 Cartesian区间六jet或完整空间cell覆盖。帽目标表达可供后续准确消费者使用，但不能将这里的表达记录当作已算全帽 curvature／metric／reach。

原完整453→450、native32/10、FD/final/同g等全部既有责任均无改动；本源不产生新的 accepted state、native response、阈值、数值运行或 geometry plan的实际成功结论。

## 8. 当前交付状态

本轮只进行了来源文本阅读、独立源码／正文写入、字节身份和完整文本核对，没有 import、AST、编译或科学执行。没有创建 accepted input、request、workflow或真实 run。R409已经独立发布且保持原字节；193的既有两阶段任务并未把本源加入为前门。

本接口及 R413正文可独立随源码发布。将来有真实 current-C450且要在同 job 构建闭场时，按实际文件恢复本输入即可；若此前任务已依规则清理450raw，不能凭其摘要或 SHA 重建，须按原完整源／参数重新真实执行并接入。
