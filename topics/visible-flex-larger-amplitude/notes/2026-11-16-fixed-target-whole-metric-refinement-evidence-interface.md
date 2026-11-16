# R459 — 固定闭目标的全域误差测量与真实精化序列接口

作者：geometry agent（AI）。日期：2026-11-16。

## 1. 已实现范围与当前状态

本入口把真实 accepted 场的全闭域相对度量误差写成可比较的数值包围，而不是重复统计某个固定 `eta` 是否通过。它可读原 R416 场、R441/R448/R456 固定 112 模态的精化场，以及 R442/R451/R457 完整 M 场；三个来源分支分别绑定实际源码。共同材料图使用已发表 R457 的准确逆和完整六 jet API。

同一个原准确 C、全部根族、十个参数词、首次构造的 W/H/完整 marker 列表、原 cut/cuff、首次材料记录和时间区间必须真实绑定。新 M 的表示字段按 R457 已有语义处理，不能把“十词相同”替代其余目标责任。每一级仍是真正新求解、原全部 H/J/FD/fullDN/final/audit 返回后产生的完整 checkpoint；本入口不产生或伪造 accepted 父。

**尚未执行。** 当前没有本源的实际测量输入、场、精化因子、误差值、返回证书或 Actions run。本次交付没有 request/workflow，不修改任何已刊数学源或运行中任务。R458 可在原 job 内按实际返回的父与几何 receipt 调用；缺首次 B 或其他必要来源时，只使该测量责任未付，不能成为 BVP、M/mesh 精化、reach 或 held 的新前门。

完整数学论证见 [R459 固定目标误差与精化证据](../results/R459-fixed-closed-target-relative-error-and-refinement-evidence.md)。源为 [独立误差消费者](../computations/geometry_20261116_fixed_target_complete_metric_evidence.py)。本接口说明实际字段、流程和范围，不另设验证或审查流程。

## 2. 发布文件与直接来源

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `geometry_20261116_fixed_target_complete_metric_evidence.py` | 62091 | `494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05` |
| `R459-fixed-closed-target-relative-error-and-refinement-evidence.md` | 17097 | `b4c31fa4130a472ca8c6f8c05e0b4b438cdda60056d2504ec68699befad5dba3` |

本接口自己的最终身份及上述两件写入临时 publication manifest；manifest 与工作差异只是交接文件，不要求入库。源码所有运行依赖都来自实际 `computations` 目录，不从包名或当前默认 main 猜来源。

三个顶层 loader 分支：

| `field.family` | 原完整 metric loader | SHA-256 |
|---|---|---|
| `original112` | `geometry_20261115_current_C_ten_live_query_complete_metric.py` | `77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892` |
| `resolution112` | `geometry_20261116_current_C_resolution_live_query_complete_metric.py` | `fd263af28a7d55a7246a49283d367e420786f48f16556dd5a7d61406b1c8459b` |
| `completeM` | `geometry_20261116_current_C_M_live_query_complete_metric.py` | `fc35c6408aacbf2131a89fbac37ca4ae98c1665d9fbdc4ba78a50a43ca7f3a47` |

共同材料源是 `geometry_20261116_current_C_actual202_M_common_material_phase.py`，38151 B，SHA-256 `059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41`；schema 为 `R457-current-C-actual202-capable-complete-M-common-material-phase-v1`。它明确识别首 R437 与首 R452 的真实 A/B，并继续核当前 R416/R441/R451 对象，而不是修改已加载模块的全局来源表。

每个 loader 通过自身原 `load()` 再读七个实际依赖槽 `CUT_NAME/PREFIX_NAME/KERNEL_NAME/C_NAME/CUFF_NAME/CAP_NAME/LIVE_NAME`。三个分支共享：

| 槽 | basename | SHA-256 |
|---|---|---|
| `KERNEL_NAME` | `geometry_20261115_shared_field_relative_metric.py` | `a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17` |
| `C_NAME` | `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `LIVE_NAME` | `geometry_20261115_same_job_C_live_query_provider.py` | `07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9` |

其余真实分支为：

| 来源 | 槽及 basename | SHA-256 |
|---|---|---|
| original112 | `CUT_NAME`: `geometry_20261115_current_C_accurate_cut_patch.py` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| original112 | `PREFIX_NAME`: `geometry_20261115_continuous_ten_frozen450_prefix_metric.py` | `011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84` |
| original112 | `CUFF_NAME`: `geometry_20261115_current_C_original_cuff_target_atlas.py` | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| original112 | `CAP_NAME`: `geometry_20261115_current_C_ten450_fixed_cap_balls.py` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |
| resolution112 | `CUT_NAME`: `geometry_20261116_current_C_resolution_accurate_cut_patch.py` | `8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52` |
| resolution112 | `PREFIX_NAME`: `geometry_20261115_continuous_ten_frozen450_prefix_metric.py` | `011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84` |
| resolution112 | `CUFF_NAME`: `geometry_20261116_current_C_resolution_original_cuff_atlas.py` | `d0b03a367f3ece13b06949d5218a992e6ee3e9a41364499070d3f5f475a150a0` |
| resolution112 | `CAP_NAME`: `geometry_20261116_current_C_resolution_fixed_cap_balls.py` | `ca53bdc5c0cdd5764065301f0edb1259d083fdffa9f3d767a5a38b4a7cafe364` |
| completeM | `CUT_NAME`: `geometry_20261116_current_C_M_accurate_cut_patch.py` | `747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492` |
| completeM | `PREFIX_NAME`: `geometry_20261116_continuous_ten_M_prefix_metric.py` | `56a3a9fed5b52130199e0fd6d6d6d72d6d12a82fbbf9c248e77608e8bfd056be` |
| completeM | `CUFF_NAME`: `geometry_20261116_current_C_M_original_cuff_atlas.py` | `97e4a49f0a9913094dec5f78b173437028f553a5bf0aa36f0b0b9d53929a9621` |
| completeM | `CAP_NAME`: `geometry_20261116_current_C_M_fixed_cap_balls.py` | `21f755aad5bb5616356005f575db76c1a6826b3a33197a14e1d6910aa069984a` |

这些被调源继续递归核其 SavedPrefix、准确 factory/target、当前 shared、完整 checkpoint writer、Active 六 jet、原 C/runtime/proof 等既有闭包；R459 不复制或削弱它们。R426 live provider 原基线 metric 身份 `28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590` 保持原绑定。运行时 `input-binding.json.direct_sources` 记录本次真正加载的来源，原各层 receipt 保留其余闭包。

科学 runtime 仍用原 Python/flint 等完整依赖。新源只新增标准库有理端点与整数平方根运算，没有新模型库、原科学模块猴补或替代积分器。

## 3. 三个实际命令

运行均仅限本公开库 Actions。下面大写词表示调用者实际文件变量，不是已经存在的输入：

```sh
python geometry_20261116_fixed_target_complete_metric_evidence.py measure \
  --input ACTUAL_MEASUREMENT_INPUT --input-sha256 ACTUAL_INPUT_SHA256

python geometry_20261116_fixed_target_complete_metric_evidence.py compare \
  --input ACTUAL_SERIES_INPUT --input-sha256 ACTUAL_SERIES_INPUT_SHA256

python geometry_20261116_fixed_target_complete_metric_evidence.py readback \
  --directory ACTUAL_OUTPUT_DIRECTORY --result-sha256 ACTUAL_RESULT_SHA256 \
  --out FRESH_READBACK_DIRECTORY
```

`measure` 是实际科学测量。`compare` 只读取实际测量及末网格元数据作精确区间/字集合比较，不重求场或 C；本任务仍把这些算术保在 Actions。`readback` 不执行几何，只从真实结果形成相同必要选择。

`measure` schema：

```text
R459-same-accurate-closed-target-complete-relative-metric-evidence-v1-measure-input-v1
```

实际 result schema 去掉末尾 `-measure-input-v1`。series input 为基础 schema 加 `-compare-input-v1`；series result 为基础 schema 加 `-actual-series-v1`。

每次 `out` 必须新建，原件保留，不能覆盖前级或读回输入。`namespace` 必须是实际 `RUNNER_TEMP` 的严格子目录；当前 field、checkpoint、C、first A/B/plan/assembly 和时钟文件都保在同一 namespace 下，且不能被新输出目录包含。源码目录/proof 目录按实际 checkout 传入，不伪作数学 raw。

## 4. measure 输入的完整合同

最外层键集合必须准确为：

```text
schema, label, namespace, computations, proof_directory, job_deadline,
first_material_transport, first_plan, first_assembly,
field, work, c_queries, time_grid, out
```

`label` 是本次明确的 level 名。它没有数学作用，也不替代 source/CP 身份。凡下文称 descriptor，键集合均准确为 `{file, bytes, sha256}`，由实际文件完整读取产生；不要直接传混有 `rows/schema` 的大 receipt 或仅一个 SHA。路径应是本 job 可访问的真实路径。

### 4.1 原时钟与首次材料对象

- `job_deadline`：本 job 真正原 deadline descriptor。支持原 `request193-owned-job-science-deadline-v1`、`request203-owned-job-science-deadline-v1`、`request205-owned-job-science-deadline-v1`。新 job 复用某来源合同仍须保当前 run/source 的实际时钟文件，不能取历史 run 的文件。
- `first_material_transport`：第一次实际 R437/R452 shared 后生成的 `first-material-transport.json` descriptor，不能由首 A 或计划字代替。
- `first_plan`、`first_assembly`：上述 B 实际绑定的完整首 plan/assembly descriptor。R457 会按真 B、其 A 和完整 source/CP/clock/十词/构造核实；R459 再把实际加载的 plan/assembly bytes/SHA 对齐显式输入。

`repository/run_id/source_commit` 必须是当前实际运行值，B 的 `original_deadline` bytes/SHA 必须与显式 deadline 全同；原 `science_seconds_from_namespace=18900`、`readback_reserve_seconds=2700` 不变。只 matching schema 不能代替这项来源绑定。

### 4.2 field

`field` 键集合准确为：

```text
family, directory, result_sha256, checkpoint_directory,
cuff_atlas, continuous_e_result
```

`family` 取第 2 节三个值之一。`directory` 指本级真实 shared 结果目录，`result_sha256` 绑定其中原 `result.json`；不是 prefix-only 输出或上一级几何目录。`checkpoint_directory` 指本级原 loader 可读的完整 frozen 450/M checkpoint。`cuff_atlas` 是本级真实 R413 对应来源的 atlas descriptor。`continuous_e_result` 是同 job 原 f12f 完整 C result descriptor，且其原 source/index/primitive/query payload 仍在。

原 `load_accurate_cut_field` 继续读真实七元组、准确目标、全参数冻结状态和完整接受合同；`cp.k==0` 只是此后确认，不是把 453 丢三列重新命名。原件必须保留到该 role 的读回与外层 quiet 完成。

### 4.3 work

所有 11 个字段都必须显式给出，不使用隐藏“合理默认值”：

| 字段 | 类型/源码范围 | 用途 |
|---|---|---|
| `budget_seconds` | 有限正 int/float | 本 role 合作式 allowance，含本源绑定开始以来的时间 |
| `free_bytes_reserve` | 正整数 | 实际 namespace 所在盘的剩余空间保留 |
| `interval_bits` | 整数 64…8192 | 原准确 jet/材料逆的基础工作精度 |
| `sqrt_bits` | 整数 32…8192 | 新准确有理端点平方根位数 |
| `initial_angular_depth` | 整数 0…20 | 原完整根格角划分 |
| `max_depth` | 整数 0…30 | 原闭格 DFS 细分工作上限 |
| `max_cells` | 正整数 | 实际访问闭格数上限 |
| `measurement_width_goal` | 非负准确有理字符串/整数 | 误差包围宽度的细分工作目标 |
| `metric_reference_eta` | 严格在 0 与 1 之间的准确有理数 | 只供报告当前上界是否已小于所声明参考 |
| `max_inverse_steps` | 整数 0…4096 | 原准确材料逆包围的工作次数 |
| `max_phase_query_cells` | 正整数 | 真正 t/point/piece 查询工作上限 |

实际 Active 精度用 `interval_bits+max_depth`，全部原函数仍按自己的来源合同计算。工作宽度/次数不是新的科学接受阈值；到限保存真实 pending，不说目标不存在或解失败。`metric_reference_eta` 不决定 BVP、接受或是否继续精化，也不以它多次通过充当误差下降。

### 4.4 c_queries

完整 11 个原 R426 工作字段：

```text
precision_bits, integral_absolute_bits, integral_relative_bits,
analytic_guard_bits, integral_evaluation_limit, value_width_bits,
integral_max_depth, inverse_max_depth, max_panels, max_nodes, budget_seconds
```

R459 逐字段传成原 `c_query_<key>` 参数，并调用原 `parameter_record` 核其真实资源合同。原 f12f 同参数/同根族/同自然域完整六 primitive 不变；只在实际 native/collar 闭径向格没有界或误差包围尚宽时申请同语义新查询，绝不把 geometric `1+B'^2` 代替目标 E。

当前原 C 盒/累计不确定性不一定能由空间细分消除。完整 coarse 界可以继续有效，query work-resolution false 不自动抹掉它；没有“加大预算一定精化成功”的承诺。缺 retained 原 payload 不能由历史 SHA 重新造积分状态。

### 4.5 time_grid

准确键为 `subdivisions` 和 `witnesses`。前者为正整数 n；实际执行全部 `k=0,…,n` 的 `t=k/n`，包含两个闭端点。每个 witness 的键准确为：

```text
kind, coordinate, q, lower
```

`kind='prefix'` 时 coordinate 是公共 `u=s_num/L_num` 的准确有理数，范围 [0,1]；`kind='radial'` 时是原非负物理 r。`q` 是首次材料图的准确有理数，范围 [0,1]；`lower` 是真实布尔 side。不存在只靠名字默填四个点或实际接受参数的行为。

代码把 prefix u 乘当前真实数值长度找到原片归属；原 r 不再归一。按所有闭 piece 枚举 membership，共用端点上的多个表达全部查询。若指定点根本不在当前真实域，报告实际输入错误，不能挑最近样点。每个已完成点保原完整六 jet/来源在临时 ledger，必要正文保地址、失败和最大下界见证。

本源提供可用的嵌套方式是调用者保持同一完整 witness 列表，并使下一级 n 是前一级 n 的整倍数；尚未完成所有实际查询时不会记 complete nested grid。具体 n、点或 level 数由新实际实验显式给出，本接口未预填未来工作量或结果。

## 5. 与原场消费者的实际接点

`Measurement.bind` 先读首 B 和原 deadline，建立合作式预算，然后按第 2 节来源加载原完整 metric 模块及其依赖。它没有调用原布尔 eta driver 再把状态换名字，而是复用真实定义与原闭域覆盖函数。

本次实际调用的关键接口为：

1. 所选 `CUT_NAME.load_accurate_cut_field(args)`，产生准确场、target、source_bundle、实际 Active 与全部 piece。
2. R457 `bind_loaded_common_material(current, first_material_transport=..., first_material_sha256=..., first_plan=..., first_assembly=..., budget_check=...)`，产生准确 `Theta_current^-1` 与首材料定义。
3. 原 cuff `bind_loaded_shared_bundle`、cap `bind_loaded_shared_bundle` 与 metric `cap_metric_identity`，绑定完整两帽和目标完全同式。不是重新扫数值格才能准许误差为 0。
4. 原 metric `ActualCompleteCTarget`，读取实际 C result 和四件原成员；再由 R426 `LiveQueryTarget` 消费本 job 保留的原 head/primitive/inverse payload。
5. a601 `root_plan/roots/split_cell`，保完整两反射片、所有实际 prefix/native/collar/patch、原 radial cuts、全角闭根及后缀。
6. 当前场 `evaluate` 的完整六 jet；及准确 target `closed_range` / same-C `bounds`，组成每格真正 Gram/目标。
7. 每个真 t 点调用 **`evaluate_active_cell(piece_index, radial, angular, time_interval, lower, interval_bits=..., max_inverse_steps=...)`**，并用 `encode_active_cell` 保存原包围。不是不存在的简称 `active_cell`。

prefix 基相位图是原数值 s；目标 g11 为 `(L_true/L_num)^2`，角系数是全 ten DAG 半径平方乘当前完整材料角导数平方。在公共 u 点查询中，径向 jet 同乘 L_num，目标 g11 成为 L_true²。tail/collar/patch 使用原 r 与同 C E(r)，不把不同坐标的量相减。所有新几何仍是准确 Hermite/patch 明确定义的场，原 RK 轨迹误差及数值 shadow 不被来源标签消除。

## 6. 测量流程、全相位与上下界

实际顺序是：绑定、执行声明 t 网格、完整基相位空间 DFS、关闭 ledger 与读回。t query count 到限只停止有限网格，保其后缀，然后在仍有原时间时继续空间覆盖；原时间/盘/外部信号到限停止本 role。此顺序没有性能保证，某阶段可耗尽真实剩余量。

活动目标为正对角矩阵时，用完整 Gram 的准确相对算子范数式

```text
a = H11/g11 - 1
c = H22/g22 - 1
error = abs((a+c)/2) + sqrt(((a-c)/2)^2 + H12^2/(g11*g22))
```

R459 先保原区间真实端点，再用有理向外计算和整数平方根包围；目标正下界未付就留下该格未付。它没有取宽球中点，也没有把分量最大误差当作该谱量。

两帽在同 actual graph/side/full markers/cuff 绑定后误差准确为零。活动部分整圈完整覆盖通过 R443/R447/R457 的共同材料相位共轭及 `(E,G)` 同余不变性转移至全部 `t∈[0,1]`。准确目标自身包含角材料系数；证明没有假设全 g 或不轴对称帽在旋转下不变，更没有从有限时间点外推全部 t。

全域上界仅在所有原根责任都已有真实界时给出，包括有界但工作尚未细化完的当前 frontier。任一原根未访、退役格无界、pending 格缺有效父界或原 C/帽条件未付，upper 为 null。有效父格上界继承给每个子格，已付 coarse 不能因子查询未返被丢弃。下界来自真实非空格的统一下界或实际公共点/time 的下端；保取得最大下界的地址。

`complete_domain_upper_available`、`completed_all_DFS_work`、`actual_time_grid.complete_queries`、满足参考 eta 和原 BVP 接受是独立状态，不能互相代替。若继承/新包围发生数学不一致，保具体错误和现场，不输出假全域上界。

## 7. 原时钟、异常与 raw 生命周期

本源的测量计时从 `measure` 开始，覆盖输入读取后的实际绑定/查询/遍历工作；预算对象先绑定真正原 deadline，随后检查原绝对终点、显式本 role allowance 和实际盘 free。预算不从每格/每 query 重启。

给 R426 的外层 query allowance 是创建 provider 时的**实际剩余量**，不是重新赠予完整测量时长。原 live provider 继续按自身参数保全部原积分/逆像资源。若此前已无剩余，直接保 resource stop，不用极小正数绕过时钟。

这些是合作式检查，不是异步硬截止；导入/底层算子运行期间仍需 R458 的真实 OwnedChild、TERM→KILL、wait/reap、quiet 与原 job/step 硬限。源码不启动子进程，因此没有另一个 child group。SIGTERM/SIGINT 只置实际 signal flag，下一检查保完整 DFS 事务后停止；外层仍保最终强制停止能力。它不把外部中断称为数学拒绝。

预算异常 `ResourceStop` 继承 RuntimeError，不会被本源数值 ArithmeticError/ValueError 处理误吞。普通闭格/point 数值错误保具体地址；全局绑定/执行错误保 phase/type/message。原 flint precision 在 finally 恢复，失败也不污染随后角色的全局精度。

如果输入语法/来源/目录在 Measurement 构造前失败，或实际 I/O/强杀使 result 无法写完，外层必须保原 stdout/stderr、真实退出和全部现存文件，不能补一份成功 result。闭合错误单列 `close_errors`。

**不删除任何 raw，不写可供自动清理的 quiet marker。** 原 C、CP、A/B、shared、逐格和原 query payload 必须保到所有原必要读回及外层真实静止后，才由原总 workflow 决定清理；本源的 `no_subprocess_started` 不等于整个 namespace 已静止。

## 8. 实际输出和单份必要读回

每次 measure 的 `out` 写：

- `result.json`：完整实际结果；核心 `global_relative_operator_error.lower/upper` 为准确有理字符串或 null，包含实际下界见证及完整域状态。
- `summary.json`：真正单份必要选择。无分包或编码大数组协议。
- `large-arrays/input-binding.json`：完整实际场、目标、C、first/current material、CP、原 clock 与源闭包 receipt。
- `large-arrays/actual-final-mesh-words.json`：原 solver 真正末网格全 binary64 little-endian words，末网格不假称逐字等于 seed。
- `large-arrays/full-active-root-plan.json`：实际完整根集合定义。
- `large-arrays/complete-relative-error-cells.jsonl.gz`：每个原格地址、完整评估、继承界、split/terminal；退役无界格的全部地址始终在此。
- `large-arrays/phase-grid-plan.json` 与 `actual-t-grid-point-queries.jsonl.gz`：完整实际时间/点/片计划与每个返回包围/错误。
- `large-arrays/complete-coverage-and-pending.json`：当前原 root、完整 stack/fallback、未访 rank 后缀、全部计数和域责任。
- 原 accurate_field/common_material/cap/target 定义 receipt，以及原 provider `live-C-queries/` 的完整 ledgers。

必要正文保当前 frontier 的 rank/path/depth/继承界、完整未访 rank 后缀、所有失败 time/point/piece 地址、原错误/资源、闭合错误和完整 ledgers 的 bytes/SHA/行数。大成功六 jet/所有成功格以及退役无界格逐项正文不全部重传，明确由原 ledger 保持其地址/身份；不声称工具侧已逐值独核。

stdout 原 frame：

```text
BEGIN_R459_FIXED_TARGET_METRIC_EVIDENCE
{one necessary JSON}
END_R459_FIXED_TARGET_METRIC_EVIDENCE
```

每份上限 **90000 B**。若超限写真实 summary，打印小的真实 over-budget 记录并 exit70，原件保留；不提高阈值、不删必要失败/未访、不拆 raw。声明有限工作数不能保证任何实际错误分布下都低于 90KB。

正常写入的 step outputs 是 `metric_evidence_summary`（实际文件路径）、`metric_evidence_summary_bytes`、`metric_evidence_summary_sha256`。父级 report 宜只转身份/outcome，完整正文由 compute 原 frame 保存，不把多个 90KB 正文再拼成一个超限对象。

原执行/闭合错误 exit2；没有该类错误但数学域或资源尚未付，可 exit0 并明确 partial。这是读回语义，不是 metric pass 或新接受。readback 重新完整读 result 的必要范围并核本源/当前 run/source；大 ledger 只如实标身份范围，不重做科学。

## 9. compare 输入与精化证据

series input 键准确为：

```text
schema, namespace, measurements, out
```

`measurements` 是按实际 level 顺序给出的 result descriptors，至少一个；每件必须由当前本源、同一实际 run/source 返回。比较器不会读取 future、从 SHA 填数或把别的 schema 重新标成测量结果。

它核所有非空 fixed-target signature 完整相等，并核原 clock bytes/SHA。当前 signature 包含首 B、R457 common accurate target、同原 C 输入、全十词、完整构造/cuff 和时间范围/共同图定义。某一级缺 binding 时仍保该实际结果，但不声称可比较的同完整目标。

每对实际 level 分别输出：

- `strict_real_sup_decrease_proved_by_separated_bounds`：只有 `U_new<L_old` 且两级完整同目标界均有时为真；只是足够证明，不是接受或精化前门。
- `certified_upper_envelope_improved`：真实上界数值下降，只称上界改善。
- `strict_real_sup_increase_proved_by_separated_bounds`：只有 `L_new>U_old` 才称已证明真实 supremum 增大。
- 其余 `actual_sup_comparison='undetermined_overlap_or_unpaid_complete_bound'`，允许原 caller 继续预算内原精化或更紧测量。
- 真实 7 个 resolution 字段逐项 before/after；实际 CP parent 是否前一级；实际末 mesh 全词嵌套/计数/长度；实际 t 网格共同 witness/整数倍/是否完整执行。

7 个 resolution 字段是 `field_modes`、`field_angular_quadrature`、`native_quadrature`、`native_steps_per_stage`、`material_angles`、`physical_angles`、`native_stage_count`。原无 `actual_resolution` 的 CP 按它真实原 config/边界记录提取，不把请求 factor 当成已执行值。

末 mesh 的全词由实际临时文件读取比较；原 R448/R456 的父词/knots 完整保留是 seed 合同，原 solver 若自适应则末 mesh 仍以真实输出为准。不因末字集合变化伪造原 seed 失败，也不把同一 CP 重测当作 fresh solver。M 与 mesh 只是不同 level 的真实字段；两个独立分支不冒为直接父链。

series 输出自身 result/summary，仍使用第 8 节单90K frame。包含每级实际界、时间未付、所有 pending 大件身份、原停止证据及相邻比较。它不选择新的 epsilon 或停止 BVP，不声明有限序列证明精确极限或统一 C² 收敛。

## 10. 原容差、机器精度与 README 标准 5

原 checkpoint 的接受证据原样保留：`original_acceptance`、`original_law`、实际 writer、native policy 中原有的 max_iterations/line_search_trials/nonlinear_tolerance/sensitivity_eta，原 final native 统计、完整 FD 与 cut audit receipts。现有 frozen450 文档阈值 RMS `1e-6`、BC `1e-11`、physical RMS `1e-6` 的原适用范围不变；native `2e-9` 仍是其自己的归一残差合同。

这些数与全闭域相对 opnorm 没有自动的同单位比较定理。结果因此明确 `tolerance_to_metric_error_transfer_bound_produced=false`，不能把其一作为 metricfloor 或由二进制字停滞推出准确误差为零。区间固定 C 宽度、工作 precision、原 solver 容差与实际场误差分开报告。

R458 可明确安排最多若干级、各级 300 秒等实际新预算，并保原 absolute deadline；这些属于新实际实验参数，本接口不预填或保证全完成。上界改善、区间尚重叠、真实原机器无新节点/容量/solver 停止等应逐项公开。相邻界严格分离不是 README 附加门；同一固定 eta 反复 pass 也不能冒误差持续下降。

本入口落实的是可执行的真实量及其证据链。是否最终满足 README §5，仍须看实际同 g 的 mesh/M/t 精化序列和真实原停止范围；§6 全 t reach/嵌入、held/δE、输出网格，以及准确解与有限程序之间的其余数学责任由原各自工作继续承担。当前没有新结果可填为 true。

## 11. 给 R458 的最小实际调用顺序

在每一级真实 geometry 已返回后，调用者只用它的 actual shared、atlas、CP、同 job f12f 结果与首次 A/B/plan/assembly 构造该级新 measurement input。使用原总 owned child 和剩余时钟启动 `measure`，完整保退出/原 stdout/stderr；该 role 未付不阻其他原 role。

一级结束后保原 result/summary/大件，分别执行必要 readback。所有已有 level 的 result descriptors 才交 `compare`，再次原样保单90K结果。测量不把 metric/reach/held 互设前门，也不触发新的 BVP。

最后清理由外层真实 owner/quiet 与全部原必要结果决定。本源未宣称已接 R458 的 workflow；R458 完整接线须记录实际 argv、来源和 role 状态。当前只交独立源码/完整证明/本接口，未派发或运行。
