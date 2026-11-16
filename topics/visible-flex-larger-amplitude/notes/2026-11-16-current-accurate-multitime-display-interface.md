# R461 — 当前准确完整场多时刻显示接口

本接口配套 `geometry_20261116_current_C_complete_multitime_display.py`。它是独立 Actions-only 显示消费者，没有 workflow、请求号、未来 parent、实际 mesh 或触发动作。当前 R458/R459 及已有求解/几何源完全不改；根代理是唯一 Git/ref/dispatch 方。

可信度：来源及条件包围命题见 [R461 正文](../results/R461-current-accurate-closed-multitime-display-and-projection-scope.md)；实际显示尚未执行。显示完成不表示 BVP、metric、reach、held、embedding、全 $t$ 或总任务完成。

## 1. 冻结件与实际 API

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `computations/geometry_20261116_current_C_complete_multitime_display.py` | 41,002 | `f3211ba9d74cf2be99d47fe56fcbd5526e8143f8a114364ffdc725382c286bf3` |

source schema：`R461-current-accurate-closed-multitime-display-v1`。

input schema：`R461-current-accurate-closed-multitime-display-v1-input`。

实际 callable：

```python
report, exit_code = produce(spec, input_receipt=actual_input_receipt)
```

或在现有真实 owned/rules host 内调用：

```bash
python "$COMPUTATIONS/geometry_20261116_current_C_complete_multitime_display.py" \
  --input "$ACTUAL_DISPLAY_INPUT" \
  --input-sha256 "$ACTUAL_DISPLAY_INPUT_SHA256"
```

这里变量必须由未来实际同 job 文件给出，示例不是已经选择的运行配方。`produce` 不启动或拥有任何 worker 子树，不自行清理；外层原 owner 的进程组、quiet 和错误日志责任不转移给它。

## 2. 输入字典：真实来源字段

以下键不允许用一个删除后旧摘要替代其实际文件。

| 键 | 合同 |
|---|---|
| `schema` | 上述 input schema |
| `repository` | `Rogerhu12/math-research-public` |
| `run_id`, `source_commit` | 本次实际 `GITHUB_RUN_ID`/`GITHUB_SHA` |
| `namespace` | 已存在的真实 `RUNNER_TEMP` 子目录 |
| `out` | namespace 内尚不存在的新目录，不覆盖 shared 输入树 |
| `computations` | 实际本 checkout 的公开源目录 |
| `proof_directory` | 实际 `results` 目录，供准确 cut loader 核 R416 原证明 |
| `origin_launch_directory` | 原193、joint203 或 actual202205 本 job launcher 目录 |
| `origin_launch_result_sha256` | 上一行真实 `result.json` 的 SHA256 |
| `job_deadline`, `job_deadline_sha256` | 原 launcher 实际消费的同一 clock 文件及 SHA |
| `field_family` | `current112`、`resolution112` 或 `completeM`，显式选择 |
| `shared_directory`, `shared_result_sha256` | 真实当前 shared producer 目录和其 `result.json` SHA |
| `atlas`, `atlas_sha256` | 同源真实 `original-cuff-target-atlas.json` 及 SHA |
| `checkpoint_directory` | 可选；若提供必须是 namespace 内真实当前 checkpoint；未提供沿 actual shared result 的目录 |

原 origin tuple 不靠 namespace 名称猜测：

| launcher schema | launcher SHA256 | 原 clock schema |
|---|---|---|
| `current-C-continuous-ten-full453-frozen450-owned-process-launch-v1` | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` | `request193-owned-job-science-deadline-v1` |
| `current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1` | `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7` | `request203-owned-job-science-deadline-v1` |
| `R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1` | `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7` | `request205-owned-job-science-deadline-v1` |

input clock receipt 逐 bytes/SHA 对照 `origin.actual_job_deadline`；再核该 clock 的 run/SHA、recipe SHA、18,900 s 原 science 和 2,700 s 原 readback reserve。没有一个新的 display start 能延长原绝对截止。

同 job 的 current checkpoint 可以是原450、真实 mesh/refinement450 或实际完整 M；display 不把 origin checkpoint 冒当前 checkpoint。当前场种类与全部来源由实际 selected accurate loader 和其原 shared/checkpoint loader 继续核，所用 actual_driver_source 原样入必要读回。

## 3. 精度、工作量与预算字段

| 键 | 默认或要求 | 真实含义 |
|---|---|---|
| `times` | 缺省 `["0","1/2","1"]` | 1–16 个互异准确有理时间词，位于 `[0,1]`；仅显示抽样 |
| `angular_frame` | 缺省 `physical-angle-image` | 可选另一个值 `first-material` |
| `grid.prefix_intervals` | 缺省 8 | prefix 显示径向区间数 |
| `grid.tail_intervals` | 缺省 8 | tail 均匀显示径向区间数，另纳真实 inner/cut-start/cut/cuff |
| `grid.cap_intervals` | 缺省 4 | 帽径向显示区间数，外圈与极点明确 |
| `grid.angular_intervals` | 缺省 32 | 完整参数圆上的显示角点数，至少 3 |
| `precision.interval_bits` | 必填，16–4096 整数 | 当前原 interval interpreter 的精度 |
| `precision.sqrt_bits` | 必填，1–4096 整数 | 原 accurate cut rational sqrt 精度 |
| `precision.max_inverse_steps` | 必填，0–4096 整数 | R457 inverse inclusion 的有限可选收缩次数；不要求指定宽度 |
| `budget.seconds` | 必填正数 | 本显示的工作秒数，仍受原 science 剩余钟限制 |
| `budget.shutdown_seconds` | 必填正数 | 原 science 结束前留给本 consumer 返回的 reserve |
| `budget.min_free_bytes` | 必填非负整数 | 当前输出卷的实际可用空间预留 |

默认的小网格不承诺画面足够美观、误差足够小或可完成的运行时。未来 host 应选择轻量显示预算，不能为显示把原 scientific/cleanup/readback 时间挪用。没有预选 actual parent、$τ$、K、held witness 或 refinement 倍数。

对指定过大的网格，源在申请数组前按保守环数上界给真实资源停止。此限制只保障每个文件小于 5 MB，不是数学接受条件。显示点数或拓扑计数不进入原接受式。

## 4. 两种角模式必须分别解释

### 默认物理角图像模式

`physical-angle-image` 在每个时间使用完整物理角 $\eta_k=2\pi k/N$，并实际评价

$$
R_{\pi t/2}K_\mathrm{current}\bigl(r,
I_\mathrm{current}(\eta_k-\pi t/2)\bigr).
$$

只声明完整圆重新参数化后的**图像相同**。它不声称 $k/N$ 是首次固定材料 $q$，不把不同时间同一顶点编号当固定首材料轨迹。此模式不读取或伪造 B；input 若同时给非空 `first_material` 会明确拒绝这项含混请求。

### 真实首材料模式

`first-material` 另必填：

```json
{
  "first_material": {
    "record": "实际 B 文件路径",
    "record_sha256": "该实际文件 SHA256",
    "plan": "实际首次 plan 路径",
    "assembly": "实际首次 assembly 路径"
  }
}
```

这些说明性字符串不是有效未来配方值。运行时每件都必须实际存在，并由 frozen R457 `bind_loaded_common_material` 核对其原来源、完整 first112 定义、当前 full ten/target、W/H/全 marker/cuff、registration/normalization、R437 或 R452 A/B。然后使用 $\eta_k=\Theta_\mathrm{first}(k/N)$。

B 不存在时不伪造第一材料，且不因此否决现有 metric/reach/held 或默认显示。只有本次明确请求的 first-material 显示范围尚未建立。两种模式都不声称全闭 target 旋转对称；非对称帽保持原 Cartesian 坐标不转动。

## 5. 三个实际 source 集合

每族仅加载自己明确选出的 accurate cut/atlas/caps，不能把同路径第一次导入的另一个 `Shared` class 冒当前 owner。R417/变体已按真实 `type(A).__module__` 绑定，原 class 所有权修复保留。

| 角色 | `current112` |
|---|---|
| accurate cut | `geometry_20261115_current_C_accurate_cut_patch.py` / `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| shared | `geometry_20261115_current_C_ten450_shared_field.py` / `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` |
| atlas | `geometry_20261115_current_C_original_cuff_target_atlas.py` / `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| caps | `geometry_20261115_current_C_ten450_fixed_cap_balls.py` / `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |

| 角色 | `resolution112` |
|---|---|
| accurate cut | `geometry_20261116_current_C_resolution_accurate_cut_patch.py` / `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` |
| shared | `geometry_20261116_current_C_ten450_resolution_shared_field.py` / `1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935` |
| atlas | `geometry_20261116_current_C_resolution_original_cuff_atlas.py` / `d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0` |
| caps | `geometry_20261116_current_C_resolution_fixed_cap_balls.py` / `ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364` |

| 角色 | `completeM` |
|---|---|
| accurate cut | `geometry_20261116_current_C_M_accurate_cut_patch.py` / `747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492` |
| shared | `geometry_20261116_current_C_ten_M_shared_field.py` / `db1f6fd39bef3d9ce2543276771cbcea1c2432a7221b8f295ed5b553b2171f87` |
| atlas | `geometry_20261116_current_C_M_original_cuff_atlas.py` / `97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621` |
| caps | `geometry_20261116_current_C_M_fixed_cap_balls.py` / `21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a` |

共同材料 helper：`geometry_20261116_current_C_actual202_M_common_material_phase.py` / `059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41`，已发布 R457。

完整六 jet 解释器：`geometry_20261115_shared_active_interval_balls.py` / `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b`。

其余完整递归依赖继续由所选原 loader 逐实际 source pin 核；上表不能冒整个运行闭包。R416 证明仍由原 loader 对 `3aac8f52…` 全 SHA 绑定。新源不复制这组数学实现，也不以 prototype/mock 替任何 source。

## 6. 点值表达、入口与帽的实际调用

加载次序是：原 origin/clock → 当前 shared result → 所选 accurate cut loader → 同源 atlas attachment → 同源完整 cap binder → 当前材料 inverse 或可选真实首材料 binder。当前 checkpoint 的 run/SHA 必须与这次 job 相同。

每个 angle/time 只形成一次包含准确实逆的区间；所有 radial 查询复用该实际区间。活动点调用 `current.field.evaluate` 而非限制 $q\in[0,1]$ 的便利 wrapper，也不取模丢失跨期 lift。field 返回六 jet，显示仅取 `.d[0]`。原所有 FFT/core 模态仍在这个点求值中，既不截频也不从旧点表复制。

入口共享环来自实际 `normalize_inlet` 定义；source receipt 与 normalization identity 返回。原 source 已投影首节点对应零块，新显示不再做一个投影或数值零检验。这个 current normal form 相对 BVP 的修正误差没有被本源支付。

cut 环选择同准确 common-cut 的 prefix endpoint 值；cuff 环选择同源帽值。帽按真实 `side*(H+b_side)`，每个 side 的所有 marker 求和，含负振幅/重叠/支撑边界。极点也走完整帽公式，不假定极点恰好是 H；这点对中心 marker 尤其必要。

## 7. 每顶点与必要摘要中的误差含义

实际点区间 $[\ell,u]$ 的中点 $m$ 只用于显示坐标 $d$。逐坐标保存半径 $\varepsilon$，准确核

$$
\mathbb Q(\varepsilon)\ge
\max\{|\mathbb Q(d)-\ell|,|\mathbb Q(d)-u|\}.
$$

这个半径包括对所声明有限表达的原 interval 点包围宽度与最终 float64 坐标投影误差。没有把中点当 C/cut/材料逆系数；没有回写 actual parameter、native 或 field 数组。

**每个 PLY vertex 的实际布局**：6 个 little-endian binary64，顺序 `x,y,z,error_x,error_y,error_z`，再一个 unsigned piece byte，共 49 B。任何完整 PLY 的第 $v$ 个顶点均有其自己的三个 outward 半径，可直接组成三个准确二进有理闭区间。

piece 编码：0=prefix，1=native/collar，2=upper cap（含上 cuff），3=lower cap（含下 cuff）。它是显示分组，不是 marker 曲率排序或科学结论。

必要摘要每帧保以下三种误差的 x/y/z 实际最大值，并保向上浮点值及其原 16 hex 字节词、达到最大值的显示地址：

- `evaluation_halfwidth`：$(u-\ell)/2$；
- `midpoint_projection`：$|\mathbb Q(d)-m|$；
- `total_point_error`：$\max(|\mathbb Q(d)-\ell|,|\mathbb Q(d)-u|)$。

另保真正存入 PLY 的最大半径、完整精确 maxima 小表的 canonical identity、实际已投影顶点数。逐点原区间不通过工具搬运；逐点半径随实际 PLY 仅留本次 Actions 临时目录。摘要不声称根代理已逐顶点阅读原文件。

这些都是有限**点**误差，未付三角面内误差、法向误差、全像 Hausdorff、全 $t$ 或 $C^2$ 估计。相对原 BVP/native 的离散误差与 inlet 归一化修正误差也未包含。实际 interval 太宽仅会如实形成较大显示半径；没有新增“画得足够准”接受阈值。

## 8. 文件与字节上限

每个已完成时刻产生：

- `display-NNN.ply`：实际 bounded binary little-endian PLY；
- `display-NNN.ply.gz`：同一原 PLY 的 gzip，`mtime=0`，level 6；
- 对应两文件的实际 bytes/SHA 记入 result 与必要摘要。

两种文件都必须**严格小于 5,000,000 B**。源的 `LimitedWriter` 在 gzip 写入越界块之前停止，partial 文件也不超过这个界。没有将大数据按块经工具转送；gzip 只是在 Actions 临时目录的一份显示文件。

其余实际临时 metadata 文件为 `accurate-field-binding.json`、`caps-binding.json`、`accurate-cut-definition.json`、可选 `first-material-binding.json`、`display-plan.json`、`result.json`、`necessary-summary.json`、`necessary-readback-complete.json`。每件也使用相同严格上限。它们不进入 Git、artifact 或 Release。

这里 `publication-files.json` 仅是代理之间传递源码/正文/接口身份的临时 manifest，不是数学 raw，也不要求随这些运行文件发布。

## 9. 完整、partial 与未访字段

`result.frames` 仅含已完成原 PLY 和 gzip 的时刻；每条保 index/准确 time、实际 point/inverse counts、源及两文件身份、vertices/faces、误差 maxima。`current_frame` 保正在处理但尚未完成的时刻，不能与已完成帧混用。

具体原字段：

| 字段 | 范围 |
|---|---|
| `angle_inclusions_completed` / `planned_angle_inclusions` | 完成的材料 inverse 包含地址前缀 |
| `ring_pairs_completed` / `planned_ring_pairs` | 以 upper-ring-major 顺序的上下点对；首 equator 共用一个顶点 |
| `poles_completed` | 下/上极点完整前缀 |
| `active_interpreter_calls`, `cap_graph_calls` | 实际 source 调用数量 |
| `inverse_maximum_iterations`, `inverse_stop_counts` | 实际可选包含收缩终态，不是接受门 |
| `inverse_enclosure_width_upper` | 已形成 inverse 区间宽度的实际向上最大值 |
| `pending` | 当前剩余角/点对/pole 地址范围及全部未起时间后缀 |
| `resource_partial`, `external_interruption`, `error` | 真实资源、信号、类型/message/traceback 分开 |
| `vertex_error_statistics_initialized` | 当前 partial frame 若在统计对象建立前中断，明确 false 且 vertex_errors 为 null；不伪造统计 |
| `owned_files` | 返回时实际存在的 owned 文件 size/SHA，含 partial 文件 |

网格地址由实际 `display-plan.json` 唯一定义，未访范围不靠猜测一个未来成功 parent。连续空间/时间不属于离散 display 计划，始终明标未证；它不是一个被遗漏后伪称已访的表。

输入格式/path 错误若早于 fresh `Display` 对象建立，不会有伪造 result 或 readback marker；其异常由原外层完整 stderr/错误读回保留。不要把无 marker 当一次显示数学否决。

## 10. 单份必要读回与清理

输出 marker：

```text
BEGIN_R461_CURRENT_MULTITIME_DISPLAY_NECESSARY
一份完整 ASCII 必要 JSON
END_R461_CURRENT_MULTITIME_DISPLAY_NECESSARY
```

后接 `R461-necessary-summary-identity` 事件。该 JSON 以 source 同一 canonical 方式形成，bytes **≤90,000**。不分包、不另编码搬完整科学表，不通过删失败或未访范围假装满足上限。

若超限：返回 70，输出 `R461-current-accurate-closed-multitime-display-v1-necessary-over-budget` 及完整原 result、尝试 bytes/SHA，`complete_necessary_readback=false`，文件不主动删除。正常有限显示完成返回 0，真实资源 partial 返回 124，其他实际异常返回 2；都不更改原科学接受布尔。

只有必要 JSON 已真实输出，才写 `necessary-readback-complete.json`。即使写了它，本 consumer 不声称全 owner 树已 quiet：外层还必须等它实际退出，并沿原 owned process 机制确认静止，再按根规则删除本次 raw。该 source 永不自行清理 input/output，也不向网络上传。

## 11. 最小未来接线及不支付的范围

未来 host 在真实 shared/atlas 文件存在时，以明确 family、actual cp/source、原clock和小显示预算调用本源即可；不需要先让 metric/reach/held 成功。若几何求解尚未形成真实 current shared，显示整个计划诚实未启动。R458 首版不等 R461，不在已运行205内插入新 step。

若以后从新网格或新 M 生成显示，必须重新使用那个实际 current accurate bundle；不能把旧 PLY/SHA 或 first shared 的采样点冒新场。若选择 first-material，须消费原真实 B 并保完整 fixed construction；默认物理角仅按同图像范围解释。

本源不检查或证明新 $τ$/K/held 比值，不选数学阈值，不补 native/CDAG 误差，也不声称连续全 $t$ 强 $C^2$。对应需要仍由原完整数学消费者支付。

## 12. 准备与发布记录

源码与本文由独立文本/JSON/字节工作产生；未本地 import、AST、compile、fixture、benchmark 或 scientific evaluate。根代理已先读 40,794 B 源稿；最终 41,002 B 仅补其指出的统计初始化/SIGTERM 写回窗口，完整小 delta 单独提供，数学和查询体不变。正文、接口及小 source blob 由根统一审读发布；本代理不改 ref，不创建 workflow，不触发科学运行。
