# R433：同一真实 shared field 之后的全像 held 与反射刚性输入接线

作者：AI。日期：2026-11-16。

## 433.1 本件范围与当前状态

本件把已经发表的 [R425](R425-current-C-whole-image-held-and-reflection-rigidity-inputs.md) 原消费者接到同一 job 的真实 shared field、原 cuff atlas 与真实 frozen450 checkpoint 之后。它只增加独立的标准库编排和必要读回；R425 的几何表达、完整位置覆盖、前缀非平面性、尾部共同背景消去、全部 marker 条件、部分结果和停止行为均保持原源。

前置生产器有两个明确来源分支：已发表 [R429](R429-same-job-ten450-postsolve-geometric-responsibility-composition.md)，以及以 R426 按需同 C 查询消费者替换 metric role 的独立 R434。两个分支都保同一 `radial_replay`、`original_cuff_atlas`、`shared_field`、`metric`、`reach` 五个地址。R433 只消费前三个生产器确切输出；后两项的通过、未决、错误或资源停止不作为 held 调用的数学条件。

本件尚无 request、workflow、run、实际 accepted450、witness 坐标或资源数值实例。没有本地 import、AST、编译、科学执行或 fixture。未来 caller 必须提供本节及后文规定的真实文件和显式参数；本件不会从摘要、来源 SHA 或较小残差制造一个场。

新增入口是 [geometry_20261116_current_C_ten450_postsolve_held.py](../computations/geometry_20261116_current_C_ten450_postsolve_held.py)。它有 `run` 与 `readback` 两个子命令，无自动 dispatch、下载、上传、Git 修改或 raw 删除。

## 433.2 冻结来源与受理分支

本件源码为 43538 B，完整 SHA-256 是 `dfd9eedd587f5c464142fa2b199137706483385242af17930ae7625dcc3a01df`。两条受理分支均使用已实际冻结的小源码；不存在待填 SHA、仅匹配标签或任意来源回退分支。

| 角色 | 文件 | 完整 SHA-256 |
|---|---|---|
| R433 编排及读回 | `geometry_20261116_current_C_ten450_postsolve_held.py` | `dfd9eedd587f5c464142fa2b199137706483385242af17930ae7625dcc3a01df` |
| R425 原科学 | `geometry_20261115_current_C_ten_held_and_rigidity_inputs.py` | `c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2` |
| R429 原编排/绑定/进程工具 | `geometry_20261115_current_C_ten450_postsolve_geometry.py` | `84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a` |
| R429 原静止读者工具 | `root_20261115_current_C_ten450_postsolve_necessary.py` | `79296f4ff205542cf99091ada7fd9a7055e68ffb04173bd242592769c8d4ca2f` |
| R434 独立 live-query 编排 | `geometry_20261116_current_C_ten450_live_query_postsolve_geometry.py` | `88996287da8df21b997cd55835dbf40315766bfb4533e949e7091d7f642c32f8` |

R429 的原 procedure schema 是 `current-C-ten450-same-job-postsolve-complete-geometry-v1`，其 input schema 是该字符串后接 `-input-v1`。R434 的对应两串是 `current-C-ten450-same-job-postsolve-live-query-complete-geometry-v1` 及其 `-input-v1`。

选择分支必须同时匹配原 procedure 的完整 producer SHA、procedure schema、原 input schema，并核对应实际源码。只给一个看似正确的标签不足以进入任一分支。R434 的 metric role 不会在 R433 中再次执行。R434 原 input 的完整 `c_queries` 十一字段仍由它自己的原 `validate_spec` 校验；R433 不补值、不运行查询，也不改写已完成的 shared field。当前调用的 quiet 纯函数始终来自冻结的 79296 读者；不会调用它原来的 `build` 或 metric 结果选择器。

原 R425 还会按自身冻结表核下列七源；R433 不重写该表：

| 原责任 | 完整 SHA-256 |
|---|---|
| R416 accurate cut field | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| R413 original cuff atlas | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| R417 current caps | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |
| 原完整活动片六 jet | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` |
| R254 prefix 非平面内核 | `a40dc7a50d90694006342ec964f18fac90bb2743ad622e1b715d920d376c1aa6` |
| 原有理球/根界纯内核 | `ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6` |
| 完整闭像直径工具 | `b1c2dfb9bd99c0777805da938c38e428da32db8ed5fa6238c9433ed9aede5ad0` |

这些是来源闭包的一部分，不是新的计算验收门。真实 scientific 入口仍是原 c87b R425，而它再沿 R416、R413、R417 的真实 loader 取得同一个场。

## 433.3 从原 accepted450 到 held 的实际文件链

R433 首先读取 caller 指定 SHA 的原 postsolve `procedure.json` 以及原 runtime input。两个对象必须属于当前 `GITHUB_RUN_ID` 和 `GITHUB_SHA`；procedure 的 `input` bytes/SHA 必须等于实际输入原件。新 `out` 是同一 `RUNNER_TEMP` namespace 下的独立 sibling，不能覆盖或包含既有 postsolve、BVP、源文件或 witness 输入。

原 postsolve 进程必须已完成自身 `finally`，并同时具备记录上的 quiet 和当前 `/proc` quiet。父 Python 只按 PID 与 start ticks 判断，不把 runner 共用进程组当成自身独占组。各 scientific CLI 由原 `start_new_session=True` 建立的独占组按实际 PGID/SID 检查。读者不对原组发信号。

`OriginalBindingView` 只提供原 `Procedure.bind` 已实际使用的属性，并把重新读取的元数据写到 R433 自有 `original-binding-recheck.json`。它不调用原 `run`，不调用任何原 RHS、root、RK、J、BVP 或几何计算。其输入仍是原 postsolve spec，没有用新对象伪装原 input receipt。

因此原绑定方法继续要求：

1. 原两阶段 launcher、driver、checkpoint 的正确源、schema、run 和 source；原 453 后独立 450 的顺序和全部原接受标志。
2. 原 owner 已正确关闭，phase leases 已释放；真实 frozen450 的维数、活动参数数和固定 core targets 合同不变。
3. 两阶段实际十个 binary64 字与 checkpoint 完全一致；不是删去 453 的三行而改名。
4. 当前 geometry result 与 checkpoint `original_native_binding` 的真实 receipt 一致。
5. 同一个实际 C cover result 及原四件 C 输入文件存在并绑定；其余原 source ledgers 保留在同一 namespace，R433 不重新查询 C。
6. 原 deadline 文件必须是原 launcher 已消费的同一 bytes/SHA，且仍绑定该 launcher 的原 recipe 和当前 run/source。

R433 再把重新读出的 launch、adapter、checkpoint、geometry、四件 C 文件、十词、准确目标身份和 runtime source closure 身份与原 postsolve `inputs` 逐项对应。这个动作只核实际输入来源，不新增一个可替代原接受条件的判据。

前三个 prerequisite 的结果取自下列真实位置：

| 地址 | 文件 | 原责任 |
|---|---|---|
| `radial_replay` | `radial_replay/result.json` | 原 R409 完整现场径向重放 |
| `original_cuff_atlas` | `original_cuff_atlas/result.json` | 原 R413 真实 cuff/target 绑定 |
| `shared_field` | `shared_field/result.json` | 原 R409 同节点 shared-B 场定义 |

每件必须与其原 stage 的 `original_result` bytes/SHA、原 schema、producer SHA 和同 job 来源对应。原 `producer_completed` 的判定被原样复用；因此原 R413 已完整写出 plan 而 stdout 摘要超限的明确 exit70 分支仍按原合同处理。该例外只适用于原 plan 已完成的原生产器，不扩为任何几何成功。

R433 同时核 `r409-original-cuff-plan.json` 对应 R413 `generated_plan`、`original-cuff-target-atlas.json` 对应 R413 `target_atlas`。W、cap height、全部 marker、原 cuff 与 same-g 信息均来自这些原文件。R433 不选择或重构 W/H/K/tau，也不以缺失 marker 代成空列表。

## 433.4 显式输入对象

R433 runtime input 的 schema 为 `R433-current-C-ten450-same-job-held-after-shared-v1-input-v1`。它只允许下列顶层键，不包含 request number、未来 run、未来 accepted 字段或重启时钟的参数。

| 键 | 类型与含义 |
|---|---|
| `schema` | 本节固定字符串 |
| `postsolve_directory` | 原 R429 或 R434 实际输出目录 |
| `postsolve_procedure_sha256` | 该目录 `procedure.json` 原 bytes 的 SHA |
| `postsolve_input` | 原 postsolve runtime input 文件 |
| `postsolve_input_sha256` | 原 input 的实际 SHA，必须对应 procedure 的原 receipt |
| `witness_plan` | 显式小 witness 参数文件 |
| `witness_plan_sha256` | 该文件原 bytes 的 SHA |
| `held` | 下一表的八个原 R425 参数 |
| `resources` | 再下一表的三项显式资源 |
| `out` | 新独占 temporary sibling 输出目录 |

`held` 必须完整列出：

| 原字段 | 原 CLI | 原合同 |
|---|---|---|
| `active_depth` | `--active-depth` | 整数；原 R425 要求 0 到 30 |
| `position_max_depth` | `--position-max-depth` | 非负整数 |
| `position_radius_goal` | `--position-radius-goal` | 明确正有理数字符串，由原 R425 解释 |
| `interval_bits` | `--interval-bits` | 原 64 到 8192 整数范围 |
| `sqrt_bits` | `--sqrt-bits` | 原 16 到 4096 整数范围 |
| `max_position_cells` | `--max-position-cells` | 原正整数工作预算 |
| `max_prefix_points` | `--max-prefix-points` | 原正整数工作预算 |
| `max_tail_witnesses` | `--max-tail-witnesses` | 原正整数工作预算 |

源级输入检查不重新实现 R425 的数学验证。具体区间、工作资源和有理数有效性仍由原入口处理；若原入口拒绝输入，读回保该实际错误。

`resources` 必须显式给 `held_budget_seconds`、`child_shutdown_reserve_seconds`、`free_bytes_reserve`。前两项为有限正资源数，后一项为非负整数字节数。本件不选默认运行预算或阈值。

witness 文件保原 schema `R425-current-accurate-active-quarter-turn-witness-plan-v1`，完整对象是 `schema` 与非空 `points` 列表。每点只含原 `piece_index`、`radial`、`q`、`lower`。索引、上下片与有理参数必须由 caller 明确；原 R425 用真实完整 field 的 piece 定义核闭区间归属和 $0\le q\le1$，并真正评价当前 R416 场。`radial` 是该原 piece 声明的坐标，不能把所有片一律解释成另一个物理径向变量。

R433 不挑一个未来成功 witness，也不从材料点移动直接得出全像 Hausdorff 结论。

## 433.5 原时钟与独占子进程

设原 deadline 文件中的两个实际字段为 $t_0$ 与 $T_s$。所有科学阶段共享

$$
T_{\mathrm{abs}}=t_0+T_s.
$$

它们是原 `namespace_created_unix_seconds` 与 `science_seconds_from_namespace`，不是 R433 初始化时新记的时间。原 readback reserve 也作为原字段记录；R433 不增加一个新总时钟。

在实际启动 R425 前，令 $B$ 为显式 `held_budget_seconds`，$G$ 为 shutdown reserve，当前时间为 $t$。实际传给原 R425 的资源为

$$
B_{\mathrm{actual}}=\min\{B,T_{\mathrm{abs}}-t-G\}.
$$

若该值不正，完整 R425 阶段记为未开始。若实际临时盘低于显式 reserve，同样记录资源未开始。二者都不构成几何反证。

R425 通过 `Popen` 的参数列表调用，`shell=False`，独占新 session，原 scientific stdout/stderr 进入自有临时文件。子进程不继承 `GITHUB_OUTPUT`，因此原 R425 stdout 不会被混入另一份必要传输。

外层每次轮询检查实际 child、外部 SIGTERM/SIGINT、已分配 allowance、原绝对 deadline 和盘空间。停机沿原 `OwnedChild` 的已观察 PID/start ticks 发送信号，保实际 TERM/KILL/quiet 记录，不向未知 PID 或 runner 公共组发信号。剩余 stop allowance 被同一个原 deadline 裁剪，没有另加时钟。

这是一套明确的轮询与所有权停止控制，不是对操作系统调度延迟的零误差实时保证。R425 内部计时包括自身 input binding/setup，但只在原边界检查；外层停止可能发生在其收尾序列化期间。若完整必要对象没有写出，读回必须标未返回并保 raw，不能用预计 work count 补结果。未来 workflow 仍须给实际 step/job 上限和 `always` 读回；本件未创建这种 workflow。

## 433.6 实际唯一科学调用与参数位置

`run` 只有一项新增科学调用：原 c87b R425 CLI。所有 helper import 都限于两个或对应受理分支的标准库编排/读者源；不会在编排 Python 内导入 R425、Arb 或调用几何函数。

科学参数列表完整等价于：

```text
python -u geometry_20261115_current_C_ten_held_and_rigidity_inputs.py
  --computations ACTUAL_COMPUTATIONS
  --directory ACTUAL_POSTSOLVE/shared_field
  --result-sha256 ACTUAL_SHARED_RESULT_SHA
  --checkpoint-directory ACTUAL_GENUINE_FROZEN450_CHECKPOINT_DIRECTORY
  --proof-directory ORIGINAL_PROOF_DIRECTORY
  --cuff-atlas ACTUAL_POSTSOLVE/original_cuff_atlas/original-cuff-target-atlas.json
  --cuff-atlas-sha256 ACTUAL_ATLAS_SHA
  --witness-plan EXPLICIT_WITNESS_PLAN
  --witness-plan-sha256 ACTUAL_WITNESS_PLAN_SHA
  --active-depth EXPLICIT_ACTIVE_DEPTH
  --position-max-depth EXPLICIT_POSITION_DEPTH
  --position-radius-goal EXPLICIT_POSITIVE_RATIONAL_TEXT
  --interval-bits EXPLICIT_INTERVAL_BITS
  --sqrt-bits EXPLICIT_SQRT_BITS
  --max-position-cells EXPLICIT_POSITION_WORK
  --max-prefix-points EXPLICIT_PREFIX_WORK
  --max-tail-witnesses EXPLICIT_TAIL_WORK
  --budget-seconds ACTUAL_CLIPPED_ALLOWANCE
  --free-bytes-reserve EXPLICIT_TEMPORARY_RESERVE
  --out NEW_R433_OUT/held_and_rigidity
```

大写项是运行时绑定位置说明，尚未赋值，不是可运行的已选 recipe。原 shared result、atlas、checkpoint 都取自上节原实际 receipt；没有用旧 finite scalar 场、单独帽图或盒中点替代当前准确场。

R425 的原输出 schema 没有 `run_id/source_commit`。R433 保该 schema 和原 bytes，不插入伪造字段。新来源通过实际同 job 的 wrapper、原参数、确切输入回执、实际启动的 producer SHA、子进程所有权和输出原件 receipt 绑定。读回还对应 R425 `input-binding.json` 中的 `original_R409_result`、`actual_R413_atlas`、`witness_plan` 三条实际来源。

## 433.7 全像、反射与未付几何责任

本接线保 R425 原数学对象和包含关系：

- 位置覆盖同时含全部实际 active pieces、反射片、完整两个帽及原全 $F_0$ 直径范围；$D$ 没有被改成 core 或某一材料切片直径。
- 原 quarter-turn witness 使用准确旋转和 R248 材料逆运输。对照的是完整像的覆盖责任，不是仅比较同一个材料点的位置。
- prefix 的 R254 内核和 tail/collar/patch 的 R274 共同 B 消去仍针对同场、同半径、完整原系数。成功 witness 的大矩阵保临时原件及身份；原失败组、当前地址与未访后缀在必要摘要中完整保留。
- marker 使用原完整列表、side、cuff 和实际高度绑定；负振幅、重叠及不满足原四 marker 充分条件的布局不会被摘要隐藏。
- 原 R238 结论包含反射，即正交群是 $O(3)$。`conditional_Euclidean_quotient_distance_strictly_positive_if_same_field_embedding` 保原条件含义；没有把它改成已经支付的定量 $\delta_E$。

特别地，R425 原 `actual_global_closed_embedding_certified`、`actual_delta_E_certified`、`actual_reach_or_metric_or_same_g_refinement_certified` 仍不由本接线付出。原 Native/RK 轨迹到新准确场的误差责任也不由一次 source binding 消除。

### 条件性来源组合

假设输入来自上述允许的实际前置源，且原绑定和三个 prerequisite 已完整返回。原输入 receipt 比较给出同一 checkpoint、同一十词、同一当前 C 对象、同一 shared result 与 cuff atlas。R425 的冻结 loader 再据这些原件构造它原来声明的 R416/R417 对象。因此 R433 所调用的消费者仍是 R425 原条件命题中的对象；包装器没有新的几何运算来改变它。

若任一来源或资源尚未付，R433 只产生相应未开始、异常或未返回记录。若 metric/reach 已失败或未决，而三个 prerequisite 及实际 quiet 已具备且原钟还有资源，R425 仍可运行。这里需要的静止性是避免读取可变原件的进程条件，不是把 metric/reach 的科学判定变成前门。

本段是来源与调用包含证明，不是新增的数值收敛、嵌入或 reach 证明。

## 433.8 必要读回、错误与单份 90000 字节

新读者只读实际关闭后的元数据和原必要 JSON。它先复核 R433 producer/input/current run/source，要求原 `finally` 已返回，并用原静止工具检查父 PID/start ticks 及独占子组。读取期间不向进程发信号；不在活动流上进行摘要或删除。

若 R425 已写 `necessary-summary.json` 与 `result.json`，读者核二者原 schema、c87b source 和 `summary.original_result` 的 bytes/SHA，并把**整份原必要对象**作为 `original_R425_necessary` 返回。不会再次选择掉任何原错误、失败组、当前 group 定义、prefix 当前格或未访后缀。原成功大 witness/ledger 的 scope 仍按 c87b 摘要声明，只返回身份、计数与成功地址范围，没有声称大原件逐行独立核数值。

若原 input-binding 已返回，读者按原 result member SHA 读它，并核上述三条真实 field/atlas/witness 对应；若原 producer 在 binding 前已停止，该字段缺失如实记录，不用假绑定覆盖其原 error/unstarted。

原 stdout 全文只留临时文件和身份，避免重复搬运同一个必要摘要。原 stderr 在自身不超过 90000 B 时以完整实际文本保留；超限时标明完整 stderr 未返回，整体必要读回为 false。原 R425 error 字段始终随原摘要保留。这里没有按末尾几行冒充完整首错的分支。

若原 R425 只有 `necessary-readback-over-budget.json`，原 attempted bytes/SHA 与完整 result 身份照抄，读回仍为 false；不会从大 result 截选一个较小对象来掩盖原超限。若被外部截止且必要对象缺失，记录全部已存在主要成员身份和完整未返回范围，不填造 pending 数值。

外层把上述原必要对象与小的实际来源、预算、退出及 quiet 记录合成一个 ASCII compact JSON 加一个 LF。总长仍以 90000 B 为限。即使 R425 自己的摘要已小于限额，外层元数据也可能使总长越界；这时返回真实 attempted bytes/SHA 的小 failure，退出 70，不删任何失败行、不升限、不拆包、不编码大 raw。

因此“必要摘要完整返回”只说明这一次声明的原必要内容可用，不表示科学成功。原 R425 error、resource partial、所有条件 flags 及真实子退出码保持原义。

## 433.9 CLI 与未来 caller 的顺序

独立入口为：

```text
python geometry_20261116_current_C_ten450_postsolve_held.py run
  --input ACTUAL_R433_INPUT_JSON
  --input-sha256 ACTUAL_R433_INPUT_SHA

python geometry_20261116_current_C_ten450_postsolve_held.py readback
  --directory ACTUAL_R433_OUT
  --computations ACTUAL_COMPUTATIONS
  --out ACTUAL_R433_OUT/necessary-readback.json
```

`run` 的实际子进程退出码原样返回；外部信号按 `128+signal` 返回，包装器异常或不能确认 quiet 返回 2，未启动而无 child exit 的责任返回 3。这些退出码不重新定义 R425 的科学结论。`readback` 完整时返回 0，必要内容缺失、quiet 未付或超限时返回 70。

stdout 只含 R433 小运行回执，以及读者的单帧：

```text
BEGIN_R433_CURRENT_C_POSTSOLVE_HELD_NECESSARY
ONE_COMPLETE_NECESSARY_JSON
END_R433_CURRENT_C_POSTSOLVE_HELD_NECESSARY
```

读者向自己的 `GITHUB_OUTPUT` 写 `postsolve_held_summary`、`postsolve_held_summary_bytes`、`postsolve_held_summary_sha256`、`postsolve_held_readback_complete`；原科学子进程不会写该文件。

未来 caller 必须在真实前置输出仍存在时调用本入口，并在任何 raw 清理之前完成其 `always` 必要读回。它仍须保原 BVP、原 postsolve 的各自必要读回与 quiet 合同。当前没有 outer workflow、rules runner 新接线或清理授权；两子命令都保持 `cleanup_allowed=false`，没有 `unlink/rmtree` 路径。即使必要读回成功，本件也不自行删除 R425、C、checkpoint 或任何前置 raw。

## 433.10 未执行范围

发布本 source/interface 只支付确切接口和条件性来源组合。它没有：

1. 产生新的实际 accepted453/450、十参数或 C root 选择；
2. 选择 W、cap height、K、tau、held 阈值、witness 或资源实例；
3. 重新运行 R429/R434 的 radial/atlas/shared、metric、reach 或 R426 查询；
4. 证明某个实际完整场的 held、全像变化、全局嵌入或定量 $\delta_E$；
5. 提供一个会自动完成的资源预算、科学 fixture 或新独审前门。

原 source/参数、所有条件与未来 actual readout 必须继续逐次区分。本件的完整输出只有新源码和本接口；可重算 raw 仍仅是未来 Actions 临时文件。
