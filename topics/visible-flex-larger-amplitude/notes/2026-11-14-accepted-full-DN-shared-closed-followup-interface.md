# 真正 full-DN 接受后：R249 前缀、共享 B 闭场与两帽的最小接线

作者：ChatGPT（geometry agent）  
日期：2026-11-14  
分类：已有冻结程序的静态接口核对与独立薄调度源码；没有新数值结果。

## 1. 本次交付的范围

新增 `geometry_20261114_full_dn_closed_followup.py` 只组织已有实际消费者，不增加几何公式、BVP 方程、native Newton 算法或验收阈值。它从一份**真正接受的完整 v3 full-DN checkpoint**及该文件自己绑定的最终 audited native 尾开始。尚未存在的接受文件和 SHA 没有在源码或工作流中预造。

本文件对应的新工作流草稿是 `visible-larger-public-closed-followup.yml`，唯一 push 触发文件为 `computations/public-native-closed-followup-request.json`，lane 为 `fullclosedfollowup`。源码和工作流均仅做了 AST/YAML/内嵌 Python 语法检查；没有本地导入数值模块、重新求解尾、生成几何或计算新的误差。

现有 v3 入口已经足够承担材料角、完整 z0/mean、原场九 jet、实际尾 readout 和第一份有限闭图，不能重复造一个替代解算器。新入口复用
[`geometry_20261114_lifted_modes_after_accept.py`](../computations/geometry_20261114_lifted_modes_after_accept.py)，只补其后尚未串联的 R249 与共享背景步骤。v4 同 g 精化有自己已有的 `same_metric_after_accept` / SavedPrefix 路径；本入口明确不把 v3 设计接受改标为 v4 精化。

## 2. 已有可执行链及真实对象

| 阶段 | 直接调用的冻结入口 | 对象与输出 |
|---|---|---|
| 原 accepted 有限场的材料读出 | `geometry_20261114_lifted_modes_after_accept.py` | 原完整 physical state、共同材料角、z0 和材料 mean；`physical-material-prefix.json`、`material-cut-packet`、原有限闭包及自身尾 `complete-4.json` |
| 入口有限 C² 规范形 | `geometry_20261114_inlet_parity_normal_form.py audit/readout/closed` | R249 首 Hermite 单元的共享节点规范形；新前缀实际读出、同场 normalized closed；原 checkpoint 不改写，也不重新宣称 BVP 接受 |
| 共享位置背景 | `geometry_20261114_shared_background_normal_form.py` | 从上一闭包同一背景表的实际 0/1/2 jet 构造一份精确共享节点实 quintic B；descriptor 为 gzip |
| 共享 B 完整闭场 | `geometry_20261114_shared_background_closed_assembly.py render` | 同一 R249 前缀、同一 actual tail、同一固定帽/mean/SE2；在自己的 B 上重新形成完整角函数的 cut correction |
| 全空间覆盖及完整位置包 | `geometry_20261114_shared_background_continuous_cover.py` | 使用 `load_shared_bundle` 重构同一新对象；保原 R241 空间门及所有活动块/两完整帽的 position packet |
| 真实整像幅度及固定 H | `geometry_20261114_shared_background_held_hausdorff.py` | 完整位置包与两整个带弱标记帽；整面 D 上界、真实 δhold 下界、`diam(H)/D` 下界 |

原 `after_accept` 自带的 `finite-closed` 并不是下面共享 B 对象的替代物。它也是保存原 finite field、独立 height/w/wr renderer 与后处理代价的必要来源。新入口保留原记录，再单独保存两次后处理的身份。

### 2.1 真正原输入

构造动作只有四个外部科学文件，均要求调用方提供实际 SHA256：

1. `--checkpoint`：原 full-DN 的 `full-dn/actual.json.gz`，含完整 `3M+2` physical state、`4M+5` augmented state、全部 `M` core modes、三项冻结 scalar parameters、真实接受标记与自己的 `actual_tail`。
2. `--tail-response`：同目录 `actual-tail-final-audit.json.gz`，SHA 必须等于 checkpoint 的 `actual_tail.final_response_sha256`。现有完整 loader 继续检查实际收敛、原 tol、完整 J、audit、最终 H、原 native 源与参数。
3. `--tail-config`：该 actual response 的原配置，SHA 必须等于 `actual_tail.sources.input_config`。
4. `--port`：必须逐 JSON 值等于 checkpoint 的 `fixed_scalar_profile.geometry.complete_original_port`。

另需通过 `--source-topic` 指向从本公开仓库恢复的原 native source bundle；`source-origin.json.actual_public_repository` 必须是本仓。现有完整 loader 按实际 tail 所记 SHA 检查它用到的原源码。新入口不需要 actual59/61 的全部迭代 factor/J/seed 历史作为闭图科学输入，也不读取原 A 的几何结果。那些历史仍保留为求解来源，不是闭图可替换数据。

共同材料角及 cut 的实际来源仍由原读出程序核查。有限 φ 模式通常产生无限材料 θ 谱；两档有限投影和九 jet 样点不能被称为全角接缝恒等式。外侧修补保的是原程序定义的完整角函数，不把有限 DFT 的未存频率设成零。

## 3. `build` 的完整执行次序

默认只调用一次已有 `lifted_modes_after_accept`。其 `all` 动作对实际 accepted tail 运行原 `exact_20261114_resolved_radial_readout.mjs`，默认原 RK 配置配 readout levels `1,2,4`；最终供后续使用的路径为：

```
<OUT>/base-accepted-readout/closed/surface-actual-tail-readout/complete-4.json
```

这份 `complete` 的所有相对 raw-node 文件必须保留。后面 normalized closed 显式传 `--complete`，shared-B definition/render 也显式传同一份文件，**不会为 R249 或 B 再运行尾 readout，更不会重新 native solve**。

如果原 full-DN 工作流已经完整运行相同的 frozen `after_accept`，可给 `--base-readout DIR`。新入口核它的 intent/summary、全部四个实际输入 SHA、原 after_accept 源 SHA、三个阶段的真实成功记录和主要输出 SHA；只复用实际完整包，不把半完成 readout 或其他候选换标签。外部复用目录不复制到新输出，使用方须保留其所有原文件及相对布局。

随后实际执行：

1. `R249 audit`：默认 2048/4096 角，首单元 16/32 径向小分；保修补前后真实 metric operator、曲率及六 jet 样点差、共享节点精确修补与条件代价公式。没有把某个样点最大值喂成 `--old-metric-bound`；该可选连续假设由原程序保留，此薄入口不伪造。
2. `R249 readout`：在同一规范化后有限前缀上重作完整材料读出。它确是后处理对象自己的报告，不能把第一阶段原前缀的数值改标签充当这一报告。
3. `R249 closed all --complete SAME_COMPLETE`：生成 `normalized/closed/surface-*`。保存入口修补身份、新旧节点 SHA、完整 mean/九 jet/单一 SE2 及原 tail/config/checkpoint binding。
4. `shared_background_normal_form`：生成 `shared/background-normal-form.json.gz`。它用原表实际值定义新的一份共享实 quintic B，完整保节点与精确分数，不删除高模或节点以缩小文件。
5. `shared_background_closed_assembly render`：生成 `shared/closed/surface-*`，保固定帽、完整 mean gauge 和 normalized 闭包记录的单一 SE2；重新形成针对本 B 的全部 cut correction。三个身份在最终输出中再次逐 JSON 值核对。

`build` 完成后保存 `result.json`、完整 gzip 文件清单、输入绑定、构造定义及现有观测摘要。`completed:true` 仅指上述子程序全部完成；`task_completed:false`，不表示 reach/幅度/δE/同 g 精化已经达到完成标准。

### 3.1 几何与目标 g 必须分开

共享 B 是一个明确的新**位置函数定义**。原完整 scalar、原 background reference table、原 `a/ap/app`、原 tail 的 E 与原 source 参数不改为 B′。新 wrapper 自身保持原 reference table 并核未改变，目标 metric 的误差必须在这一新几何上重新读出。

R249 改入口首单元共享节点三种 parity jet，其他节点保留；它不取消原 full-DN 真接受来源，也不会使新有限前缀再次成为重新求解的精确 BVP。其余接缝/浮点系数/原 finite-Gauss 真实导数与返回 ap/app 的区别仍按原 R249、R260 和 wrapper 的 limitations 如实记录。没有增加“所有六或九 jet 必须机器收敛”的验收门。

### 3.2 两帽、反射面与相位

完整 mean 来源为当前 field 的 z0 与共同材料角，不加原 A 的 height mean。normalized 前缀的反射面由 R249 入口 z=0 规范形固定；原 SE2 只作用 XY，之后上半帽的实际 `mean_gauge.upper_cap_height` 与其下半反射帽共同构成固定 H。共享 B wrapper 保同一 cap height、cuff、marker centers/definition 和 SE2 记录。

相位公式仍是原活动片 `Rα F0(s, θ−α)`、两帽与弱标记保持固定的连续族。材料重参数化加活动片旋转不能被说成整个有标记面的刚体等价。全 t metric/curvature/reach 的具体归约范围仍由既有相位论证与原覆盖器处理，此薄入口不扩大它们的已证范围。

### 3.3 显示网格与物理网格

现有独立模式 display planner 保所有真实 prefix 节点/断点；物理 readout 的完整 tail 状态也全保留。但 tail 的显示环并不强制把完整 2305 个 readout 节点逐个变成 mesh 环，而是使用原 plan 的显示选择和物理段锚。显示角数候选为 64、48、32，并由真实条件

```
N % (4 * (phase_samples - 1)) == 0
```

及实际二进制 PLY 字节预算选择。默认九相位时分母 32，64/32 合法而 48 不满足该条件。真实 ring 数、`25*V + 13*F + 4096` 预算以及最终 PLY `<5,000,000` 字节检查均留在原程序。没有降低完整材料读出角数、删真实 C² 节点或裁 native 模式来省显示文件。

## 4. 构造 CLI

下例的大写变量均应填将来真实输出的路径/SHA；不是可冒充真实输入的占位 request：

```bash
python computations/geometry_20261114_full_dn_closed_followup.py build \
  --checkpoint "$ACTUAL" --checkpoint-sha256 "$ACTUAL_SHA" \
  --port "$PORT" --port-sha256 "$PORT_SHA" \
  --tail-config "$CONFIG" --tail-config-sha256 "$CONFIG_SHA" \
  --tail-response "$FINAL_TAIL" --tail-response-sha256 "$FINAL_TAIL_SHA" \
  --source-topic "$ORIGINAL_PUBLIC_SOURCE" \
  --angles 2048 4096 --radial-subdivisions 2 4 \
  --inlet-radial-subdivisions 16 32 --readout-levels 1,2,4 \
  --out "$OUT/accepted-shared-closed"
```

如已存在同四输入的完整 after_accept 包，额外给 `--base-readout "$EXISTING_COMPLETE_AFTER_ACCEPT"`。不要只给 complete 文件却删除其真实相对节点；也不要从旧 A 包提供 complete。

主要最终路径：

| 相对 build 输出目录 | 内容 |
|---|---|
| `result.json` | 本次组合真实完成状态、输入/源/子输出 receipt，未付项 |
| `input-binding.json.gz` | 原实际输入、完整冻结 scalar/actual-tail 来源，非重解 |
| `normalized/inlet-parity-audit.json` | R249 同场首单元代价与明确范围 |
| `normalized/physical-material-prefix.json` | 规范化后整个材料前缀自己的读出 |
| `normalized/closed/surface-*` | R249 后、原独立背景 renderer 的来源闭包 |
| `shared/background-normal-form.json.gz` | 精确共享 B descriptor |
| `shared/closed/surface-*` | 同一新的完整共享 B 闭包及 phase meshes、normal samples |
| `finite-construction.json.gz` | 实际两帽、mean、SE2、cut、B 和 limitations 的原报告值 |
| `existing-observations.json.gz` | 仅复制原消费者实际样点统计，不制造连续界 |
| `output-inventory.json.gz` | 新输出树所有文件字节/SHA；大 payload 仍完整 artifact |

任何子程序非零返回时停止后续依赖步骤，保原日志/已完成子结果/`failure.json`。这是实际失败保全，不增加新的数学验收。

## 5. 同场 `measure`，没有旧 A 数值回退

现有 cover 的默认 K=8.35 等数字属于旧候选的历史使用，不能静默拿来证明新的完整闭面。本入口要求一份显式同场 envelope JSON，而不要求新增区间证明或外部审批。其六个值就是原 cover 已有的输入参数：

```
schema: same-shared-closed-explicit-cover-envelopes-v1
build_result_sha256: 实际 build/result.json 的 SHA
shared_assembly_sha256: 实际 shared/closed/surface-assembly.json 的 SHA
provenance: 本次上下界/数值预算的实际来源与范围说明
values:
  curvature_upper
  relative_metric_upper
  tail_slope_upper
  radius_lipschitz_upper
  position_error
  normal_angle_error
```

没有在接口中预填未来候选数值。连续界、数值加密及有余量的证据应按本题 README 的实际标准分别说明；这个 JSON 本身不能使未经证明的假设变成严格界。新入口只核该记录属于同一实际共享 B 闭面，保原空间公式、原阈值与原报告局限。

```bash
python computations/geometry_20261114_full_dn_closed_followup.py measure \
  --checkpoint "$ACTUAL" --checkpoint-sha256 "$ACTUAL_SHA" \
  --port "$PORT" --port-sha256 "$PORT_SHA" \
  --tail-config "$CONFIG" --tail-config-sha256 "$CONFIG_SHA" \
  --tail-response "$FINAL_TAIL" --tail-response-sha256 "$FINAL_TAIL_SHA" \
  --source-topic "$ORIGINAL_PUBLIC_SOURCE" \
  --build-directory "$BUILD" --build-result-sha256 "$BUILD_RESULT_SHA" \
  --complete "$OWN_COMPLETE" \
  --envelopes "$SAME_FIELD_ENVELOPES" --envelopes-sha256 "$ENVELOPES_SHA" \
  --radial-stride 1 --angular-stride 1 --prefix-angular-subdivision 2 \
  --out "$OUT/same-shared-closed-measurements"
```

覆盖器调用的 loader 显式为 `load_shared_bundle`。这个 loader 重构共享 B 自己的几何，并核原 reference metric、同一 R249 定义、descriptor、原 complete tail、完整 mean 和已记录 SE2。旧 `load_full_bundle` 对带新 `closed_geometry_wrapper` guard 的 mesh 不能作为回退。

cover 结束产生 `shared-cover-position-cover.json`，包含**全部活动块**及**两整个帽盘**。即使 `numerical_cover_budget_passed:false` 或有 reach 未覆对，新入口也继续调用原 shared held 消费者；不把 reach 先通过当作幅度计算的前置门。

held 报告的 δhold 是一个真实相位像中的点到另一整像所有活动位置块和两整个带标记帽的距离下界，使用整闭族 D 上界。两帽位于同轴等半径水平面且标记支撑严格在圆内，原消费者另给固定 H 的实际直径下界。它不使用材料点位移、核心 G 代理或核心直径替代整像量。源码只是复制这些原报告值，原空间与 Hausdorff 公式、阈值不变。

## 6. 工作流接入与资源

草稿 request schema 是 `public-actual-full-DN-closed-followup-request-v1`，需 `repository`、`lanes:["fullclosedfollowup"]`、真实 `source_sha256`、四个 `inputs` 的 `file/bytes/sha256`、`resource_plan.minimum_free_bytes`；可选 `runtime` 正好对应上述角/径向/readout 参数。所有文件来自本题公开路径；没有写入未来实际文件的伪 SHA。

工作流：部分检出 source 与两 README → 验真实 request/source/input → 原 Python 3.12.14 / Node 24.22.1 / NumPy 2.3.5 / SciPy 1.17.0 → 恢复原 public78 → 经现有 rules runner 真正 pull/定时规则同步执行 `build` → `always()` 上传完整 artifacts → 现有普通 rebase publisher。

root 在实际部署时需将 `fullclosedfollowup` 加入 publisher 的明确 lane 白名单并写真实 request；该操作由 root 统一做。本次没有改工作流所在仓库、Git 分支、H/open/log。

本阶段没有 native Newton/factor 链，但有真实尾 radial readout、完整材料读出与三个保全的有限闭包。不得把显示 PLY 的 5 MB 限额当作完整 artifact 的存储上界；工作流按实际声明的资源计划核 runner 可用空间并保所有 partial。没有因预算裁模式、删除节点或降低科学容差。

measure 已是可执行 CLI；在 build 产生真实新对象与实际统计后，填明其预算来源即可单独接后续 Actions。当前没有必要预派一个使用旧 A bounds 的 coverage job。

## 7. 确定仍欠的接口与数学范围

- 原 full-DN 接受只是进入本链的真实前提，不代表本题已完成；当前 live 求解是否成功必须以其最终原 J/audit 实际回执为准。
- `geometry_20261114_full_state_planar_germ.py`（R258 消费者）当前仍直接 import `load_full_bundle`，没有共享 B 的专用 binding 适配。本入口**不调用它**，不把旧 tail/prefix/cap 的证明输出换成共享 B 的 δE 结论。共享 B 的同半径角差消去性质可用来构造后续诚实的新消费者，但仍须绑定实际新 loader、实际切口/固定帽及 R238 假设。
- R249 首单元与共享 B 的精确实多项式定义，不自动支付全部 seam、浸入/嵌入、全域 metric、曲率、全 t reach、整像 δhold 或 δE。各自现有报告的已证/数值/假设/未解范围全保。
- 同 g 真正非线性精化仍走原 v4 路线，不能把本次后处理或径向 readout 加密称为重新解出的同 g BVP 精化；反过来也不增设九 jet 必须机器精度收敛的额外完成门。

下一最小实际动作已经具体：一旦原 full-DN 真接受，取其上述四件原件和真实 SHA，运行现有 `build` 链；根据生成的同场统计/误差来源继续 `measure`，再补共享 B 版 planar-germ binding。无需等待用户批准一个抽象方案。
