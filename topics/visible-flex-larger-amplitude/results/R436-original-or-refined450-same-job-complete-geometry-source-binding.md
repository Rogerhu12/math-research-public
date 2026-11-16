# R436：原始或真实加密 frozen450 的同现场全几何来源分支

作者：AI（ChatGPT / exact_refinement）  
日期：2026-11-16

## 436.1 结论与当前范围

本项已实现一个独立、无请求号的标准库入口：既能接原 193 的真实 full453→frozen450 结果，也能接 R431 以原 R427 科学入口新求得的 refined450 checkpoint。后一分支完整识别实际 70a driver、原 43f writer、真正直接父、共同 193 origin、共同绝对 deadline、全部十个参数字词与同一准确目标身份。它随后对所选新 checkpoint 重新运行全部五阶段：R409 径向读出、R413 原帽口图册、R409 shared field、R426 同现场 C 查询 metric、R422 全 pair reach。

原 R400/R409/R413 科学读者实际上已支持这条真实来源，故本项没有复制或改写它们。这个判断来自原 writer 与各读者的源码，不能仅凭外层 status 增加一个 producer 标签得出。这里新增的是明确来源分支和必要读回，原数值式、域门、全维数、完整均值、全部角度、五阶段依赖与预算机制不变。

同一十参数准确 C/DAG 目标不意味着不同网格得到的有限场相同；若进一步声称完整闭面保持同一 $g$，还须固定首次实际闭合构造，具体条件见 §436.4。新 checkpoint 必须已有自己的原 full450 验收、FD、最终 native/J/audit 等全部 writer 责任；旧父的 metric、reach、held 或非平面证书均不能转贴到新场。五阶段全部从新 checkpoint 重建，独立 held 派生也只消费这次实际重建的前三阶段。

当前交付只是源码与条件接口。未选实际接受父、网格层数、空间参数、C 查询预算或 run；未在本地 import、AST、编译、执行科学或构造 fixture；没有获得新的场、误差值、reach 值或 held 结论。后续真实执行只能在公开 Actions 内使用实际同现场原件。

## 436.2 冻结文件与精确基线

三个新运行文件均放在 computations，旧文件保持原样：

| 文件 | bytes | SHA256 |
|---|---:|---|
| geometry_20261116_current_C_ten450_original_or_refined_postsolve.py | 65905 | 43565f7caf8e4de76b4d842a6a8cc8af94b38e3649c8c852f39c87fa3696a8e1 |
| root_20261116_current_C_ten450_original_or_refined_postsolve_necessary.py | 24739 | a565bc881fc3909ba4a4bb7769dce59202611b00c0d15597fabef28f6a5f4235 |
| geometry_20261116_current_C_ten450_original_or_refined_postsolve_held.py | 44160 | ad492e5766f71377367f7e143749a1bab1cbafd58617ac7bbaff6063acba0039 |

它们分别来自已刊 R434 producer 47084 B / 88996287da8df21b997cd55835dbf40315766bfb4533e949e7091d7f642c32f8、R434 reader 24444 B / ebed189dfcc879a1d357b5595a2cf29d697d4cc92620f11b8cf0e5ed721e6fa0，以及 R433 held 43538 B / dfd9eedd587f5c464142fa2b199137706483385242af17930ae7625dcc3a01df。R434 发布于 f9b34188f009d60e2c04cbe7844246828925b292，R433 发布于 e2da1847c9865f3309e2c56fe0ea3b41883b0d98。

R431 发布于 ae9f17e6a114d6e19d35b8129e88b4bb7b6ce47c：

| 实际来源 | bytes | SHA256 |
|---|---:|---|
| geometry_20261116_current_C_frozen450_mesh_owned_launch.py | 33598 | 4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868 |
| root_20261116_current_C_frozen450_mesh_necessary_readout.py | 25196 | 3949b61a4d7c5d96b5751f33ca1fd20288a176b73a9df97dd087ae828e65428c |
| geometry_20261115_continuous_ten_frozen450_mesh_refinement.py（原 R427） | 33251 | 70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928 |

完整相对差异以三份正式冻结基线生成，35074 B / 86b8cbdbb8b8ede197137ac15a10ff283eda8b98952d766c9556b086779e19e6。差异和 publication manifest 是可由源码重得的临时审核材料，不包含科学 raw，也不要求长期存储。

以下原科学文件均逐字保留：

| 作用 | 原 basename / SHA256 |
|---|---|
| 完整 checkpoint writer/reader | geometry_20261115_continuous_ten_frozen450_checkpoint.py / 43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae |
| 新场的 SavedPrefix | geometry_20261115_continuous_ten_frozen450_saved_prefix.py / 1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520 |
| 全径向 Cartesian/native 读出 | geometry_20261115_current_C_ten450_radial_readout.mjs / 5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568 |
| 原帽口 target atlas | geometry_20261115_current_C_original_cuff_target_atlas.py / 02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2 |
| 完整 shared field | geometry_20261115_current_C_ten450_shared_field.py / 6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3 |
| R426 live-query metric | geometry_20261115_current_C_ten_live_query_complete_metric.py / 77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892 |
| 同现场 C 查询 provider | geometry_20261115_same_job_C_live_query_provider.py / 07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9 |
| 完整 reach | geometry_20261115_current_C_ten_complete_reach_cover.py / 3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834 |
| 完整 held/rigidity 科学 | geometry_20261115_current_C_ten_held_and_rigidity_inputs.py / c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2 |

R436 producer 的直接 pin 从 R434 的 13 件增为 15 件，只增加 R431 launcher 与 R427 driver；原 13 项逐值不变。其余科学依赖继续由原消费者读取自己的完整 closure，15 不是整个数学系统的总源数。R431 reader 只用于本说明定位原读回合同，不是新的科学入口 pin。R429/R434/R433 的旧源码身份保留为来源，未将它们重标成本实现。

## 436.3 为什么真实科学读者已经可消费新 checkpoint

### 436.3.1 R400 writer 绑定的是实际 driver

原 43f LiveCheckpointWriter 构造时接收实际 driver_source 与 complete_source_sha256。它先核原 full-DN/core、真实 flow、boundary、CurrentTenProfile 等完整来源，再要求 writer 自身和传入的实际 driver 文件都出现在同一真实 closure。这里没有 driver 必须等于原 11dd 的硬锁。

对于 $k=0$，writer 要求真实父 Checkpoint 的 $k$ 属于 $\{0,3\}$。R427 的 refined450 从实际 frozen450 父读取完整数组，形成初猜后重新执行原完整求解，再以 driver_source=Path(__file__) 调原 writer。因此合法返回的 actual_driver_source 是 70a，writer_source 仍为 43f；parent.manifest 是实际直接父的 receipt。

writer 的新接受责任不因来源分支放松：全450/338/112布局、完整左右边界、原 full-DN/RMS/BC、原两组 FD、实际 current-H 锚、最终完整 native/J、所有 stage 和切口审计等仍由原源码执行。R436 只读这些真实返回，不替代它们，也不从旧数组插值本身推导新接受。

### 436.3.2 R400 Checkpoint 与 SavedPrefix 不固定旧 mesh

原 Checkpoint 读者验证自己的 43f writer/schema、原接受字段、实际完整 runtime source closure、真实 factory/current target、实际全部数组和 FD/native/audit 原件。actual_driver_source 按真实文件与 closure 验证，没有只接受 11dd 的条件。

全数组的长度来自实际 mesh，而非固定 699。完整物理338、全450增广态、各均值、112 core、真实导数与 source/target 责任均保留。SavedPrefix 调用该原 Checkpoint.require_frozen450，并从新 checkpoint 的全部节点及完整数据生成它自己的有限 Hermite 场；它不读旧父的 shared-field 证书来替代新数组。

这只说明原加载协议能够读取真实新离散场。它不证明网格收敛，也不把 finite native replay 变成准确连续 C 的 ODE 轨迹。

### 436.3.3 原 R409/R413 后续实际绑定

原 radial 5cc 固定 writer43f、完整 frozen450 布局和实际 final-native/config/worker closure，再使用新 checkpoint 的真实 native 几何及全部输入进行完整读出；没有 11dd driver 条件。新数据的实际 mesh、226尾态与双均值、338物理/全角结构均按原路径读取。

原 atlas 02bb 读相同新 checkpoint、完整十词/current target、准确 C 与原帽口责任，并产生带新 checkpoint 身份的 plan/atlas。原 shared 6a5 则要求实际 SavedPrefix、新 radial 结果、相同 checkpoint/final-native/target 与这次真实 plan/atlas相符。

所以 R436 不需要“把新 driver 加进一个旧数学白名单”或重写这些计算器；需要的是把所有 CLI 的 checkpoint-directory 指向实际新 checkpoint，并保存来源关系。原消费者仍对真实原件承担各自全部检查。

## 436.4 条件包含与不可转移部分

设 $P$ 是全十个有限参数字词及其准确 dyadic 值，$G$ 是原完整准确 C/root-family/core/DAG 目标身份，$X_h$ 是某个原合法 frozen450 checkpoint，$X_{\widehat h}$ 是 R427 从其真实父新求得、且由原 43f writer完整接受的 refined450 checkpoint。

本入口的 refined 分支要求实际新 checkpoint、直接父和原 193 origin 的十词与 $G$ 相同；原准确 dyadic值也与 origin 相同。它还要求 writer 的 parent.manifest 与 R427 actual_parent、R431 actual_parent_checkpoint 的原字节身份相同。

这里的 $G$ 是 checkpoint 中准确 C/root-family/core/DAG/十词的目标身份，不包含一个此前 postsolve 已选定的全部闭面构造。若要把相邻 mesh 解释为**同一完整闭面度量 $g$** 的精化，还必须另固定首次实际构造 $\mathcal K$：原 $W$、cap_height、完整 marker 列表及其实际字值、材料坐标/运输选择、尾部与帽的选择，以及这些值在原固定构造源码中的解释。其后的 mesh 必须复用同一 $\mathcal K$；只核 $P,G$ 不能推出这个条件。

当前 R436 只显式接收本次 construction，并按原 R413/下游绑定验证其实际使用；它**没有**与某前一次 postsolve 的 construction 或完整 $\mathcal K$ 自动比较。这个附加条件是“同一完整闭面 $g$”这一数学断言的适用范围，不是本项已执行的比较，也没有因此新增运行门。首次真实 radial 后产生帽高再冻结 $W$/帽高/全 marker 等的策略由独立 R437 处理，本项不预填该策略的实际参数或返回。

因此由当前 checkpoint 来源绑定直接得到的是以下四项；其中若使用“同一完整闭面目标”的表述，须同时满足上述 $\mathcal K$ 固定条件：

1. 新旧有限求解针对同一固定 $P,G$ 的原 BVP 目标，而非把 active3 改标签成固定0；完整闭面目标还取决于固定的 $\mathcal K$。
2. 新有限场必须按 $X_{\widehat h}$ 的实际 mesh/数组重建，记为 $F_{\widehat h}$。
3. R409/R413/R426/R422 和独立 held CLI 的输入都绑定 $X_{\widehat h}$ 及其新生成数据，因此其实际返回若满足各自原条件，则只适用于 $F_{\widehat h}$。
4. 旧父 $F_h$ 的几何结论不参与新消费者的接受判断；$F_h=F_{\widehat h}$、几何误差单调缩小、mesh 已收敛均不是本条件推出的事实。

证明是原 writer 动态 driver/closure 合同与各消费者 checkpoint 绑定的直接组合。全十词和目标身份相同保证 $P,G$ 的目标来源相同；完整闭面目标的相同还需同一 $\mathcal K$，不能从 checkpoint 字段额外推出。真正 field 身份由完整 checkpoint receipt、实际数据及本次实际闭合构造确定。每个下游阶段把所选 checkpoint receipt 或由其生成的实际 plan/radial/shared receipt继续带入，故不能混用旧父几何。此组合没有新增数值阈值或新科学判定。

准确 C 的 root 族、原 $\lambda$、全部 source panel、原 query 自然域等责任继续由 R426/f12f 原程序承担。新 mesh 不允许重新挑一个 root；也不允许由某个旧 SHA 生成缺失的原件。相同准确目标并不免除新场相对于该目标的全闭 metric 比较。

## 436.5 两条明确的来源分支

producer schema 为 current-C-ten450-original-or-refined-same-job-live-query-geometry-v1，input schema 追加 -input-v1。必须显式给 upstream_kind，只有以下两个值：

| upstream_kind | 实际消费 |
|---|---|
| original193-frozen450 | 原 6ff launcher、11dd full453→frozen450 driver、43f checkpoint；原 R434 bind 正文完整保留，仅方法名改为 bind_original193 |
| R431-refined450 | 固定 4375 launcher、70a refinement driver、43f 新 checkpoint；同时显式给 origin_launch_directory |

refined 分支按真实字段做如下来源绑定：

- 当前 R431 result 必须是固定 schema/source receipt，run_id/source_commit 属于本实际 Actions checkout；origin_launch 精确绑定同现场原 193 result。
- 原 193、当前 R431、R436 共同读取同一实际 deadline 文件，bytes/SHA相同；original_193_recipe 对应原 origin.recipe。没有新创建 namespace clock。
- R431 自己必须已真实返回 original acceptance、child exit0、closed owner/quiet；resource_stop、external_interruption、error 必须为空。这个条件是消费真正 accepted checkpoint 的既有语义，不是本项新数学验收门。
- 原 193 adapter 仍须有真实 design453 与 frozen450 两阶段接受、owner关闭/lease释放。新 R427 adapter 则是独立 refined450 一阶段，必须实际 full450 求解返回、原接受 true，而非 drop 行重标。
- 直接父仅允许原 193 frozen450 或固定同源 R431 的真实 refined450。后一分支继续带同一 origin/deadline；新 writer 的 parent.manifest 与 R427/R431 三方一致。
- actual_refined_checkpoint、其目录、writer/driver、完整 runtime closure、338+112布局、左右338/112、$M=112,N=2048$、$k=K=0$均按原字段绑定。
- 十词、新/父/origin current_target_identity、新/origin完整 dyadic 值逐项同。现有 finite_fullDN_accepted_by_original_gates 等原字段不被改写。
- supplied geometry/result.json 必须等于新 checkpoint original_native_binding.actual_geometry_result；同现场 C result 必须等于新 checkpoint original_C_input_binding.actual_cover_result。前四 C 文件是完整实际原件；两 source-panel/index payload若缺失，记录 live-query 未付范围，不由旧摘要恢复。

输入记录中沿用原 common key original_launch、original_adapter_status，是为了保 R433 rebind 接口。在 refined 分支它们明确指“本次实际所选 R431 launch / R427 adapter”；额外保存 origin193_launch、origin193_adapter_status、origin193_checkpoint、direct_parent_checkpoint、actual_R431_input 和 parent_kind。common_original_receipt_keys_refer_to_actual_selected_producer 显式为 true，不能把这些旧字段名误解释成新 checkpoint 仍由 11dd 产生。

原 checkpoint 完整数组不是由这个标准库 binder重新加载或计算。它把实际新 checkpoint路径交给原 R400/R409，在真正科学消费者内完成原完整加载；new_checkpoint_full_array_loading_delegated_to_original_R400_R409 明确记录这一范围。

## 436.6 输入、CLI 与原五阶段

除新增 upstream_kind 和 refined 分支必需的 origin_launch_directory，原 R434 输入责任完整保留：

- 实际 namespace、upstream_launch_directory、可选实际 upstream_result_sha256；
- 原 job_deadline 路径及 SHA、实际 geometry_directory、continuous_e_directory 和 C result SHA；
- computations、proof_directory、source_topic、全新 out；
- construction 中完整 cut_correction_width、cap_height、fixed_cap.markers；没有从父场猜 W、帽高或省略 marker，也没有自动比较它们与前一次 postsolve 的值；同完整闭面 $g$ 的精化须按 §436.4 另保持首次实际 $\mathcal K$；
- 原 metric 的6参数、reach的12参数与资源项；
- R426 的11个显式 c_queries 参数。

这11项为 precision_bits、integral_absolute_bits、integral_relative_bits、analytic_guard_bits、integral_evaluation_limit、value_width_bits、integral_max_depth、inverse_max_depth、max_panels、max_nodes、budget_seconds。每项仍以原 --c-query- 对应 CLI传给固定 R426；本项不选择默认实验值。

入口为：

    python geometry_20261116_current_C_ten450_original_or_refined_postsolve.py --input ACTUAL_INPUT_JSON --input-sha256 ACTUAL_INPUT_SHA256
    python root_20261116_current_C_ten450_original_or_refined_postsolve_necessary.py --directory ACTUAL_NEW_POSTSOLVE_DIRECTORY --out ACTUAL_NECESSARY_JSON

这里大写项是尚未选择的实际同现场路径/字节身份，不是可由旧摘要合成的科学输入。未来 workflow 必须实际生成相应小输入对象；本次没有新增 workflow、recipe 或 dispatch。

原五阶段命令及依赖正文逐字保留。radial 和 atlas 产生新场原件；只有这两个完整返回才启动新 shared field；shared 完整返回后，metric 与 reach 分别按原职责执行。reach 不以 metric 通过为前置，metric未决、反证、资源部分或错误不自动阻止独立 reach。所有全角、两帽、接缝、self/AA/CC/AC pair、曲率和法向责任均由原对应消费者保留，不在新 wrapper 中缩减。

## 436.7 原绝对期限与进程静止

R431 已绑定原 namespace 的18900秒科学期限与2700秒读回保留。R436 读取同一 deadline原文件，把 namespace_created_unix_seconds + science_seconds_from_namespace 作为绝对截止；不会从 R436 启动时重置计时。每个原 stage allowance 继续按剩余实际时间和原 shutdown reserve裁剪，没有保证五阶段能在某个剩余时长内全部完成。

新 refined binder还只读实际 R431 launcher PID/start-time 与其真实 child session/group，确认旧 owner已静止；不发送信号，不伪造“已 reaped”。若真实 R431接受或静止未返回，五阶段均保持 not-started，记录 upstream_stop。该检查只防可变原件被并发读取，不是科学误差门。

新五阶段的 OwnedChild、信号处理、shutdown、invoke、原停止/依赖判定、finish以及读者 process_quiet 均沿正式 R434原正文。资源截止、外部中断、错误、未启动后缀和真实 child exit分别保存。procedure_returned 只说明控制流完成，既不是几何全成功，也不是 native再接受。

本实现及其 reader 不删除任何 raw、不上传 artifact、不创建 Release。真正清理由未来同 job最外层在原 BVP/mesh、所有已调用消费者、必要读回与真实 quiet齐备后处理。缺预算或读回不完整不能假称已清理；绝不从清掉原件的 SHA 假续。

## 436.8 单份必要读回

新 reader schema 为 current-C-ten450-original-or-refined-postsolve-one-necessary-conclusion-v1。它先核固定 R436 producer、当前 run/source、procedure finally 已完成、实际所有 owner静止，然后读取全部五个 stage行及原返回文件身份。原所有科学必要投影、错误位置、计数、未决/未启动范围选择器保持 R434正文。

新增必要字段只有所选 upstream_kind、actual_refined450_selected、old_parent_geometry_certificates_reused=false、实际 mesh quiet evidence、R434来源以及原193 origin receipt；完整 common inputs带上述新/父/origin checkpoint关系。它保 R426实际 provider状态、11参数及未付查询范围，不运算 C、不读取大 ledger去形成新数学结论。

输出仅一份 $\le 90000$ bytes 的必要对象。超过上限照原 write_output 返回一个明确 necessary_readback_complete=false 的小失败并 exit70；不拆包、不字典编码或搬运全数组、不截断后称完整。大径向/全部角度/包围/pair/source-query表只保原 bytes/SHA与明确未逐值读范围。新 frame 是 BEGIN_CURRENT_C_TEN450_ORIGINAL_OR_REFINED_POSTSOLVE_NECESSARY，结束标记对应 END；原 postsolve_summary 等 GITHUB_OUTPUT key不变。

上游“accepted”与下游每个实际责任分别保留。whole_task_or_unexecuted_geometric_responsibility_certified 始终不由本 reader设真。

## 436.9 独立 held 三分支兼容

冻结 R433 两分支源码不改。新 geometry_20261116_current_C_ten450_original_or_refined_postsolve_held.py 以独立 schema R436-current-C-ten450-original-or-refined-same-job-held-after-shared-v1，精确支持三个 producer/schema/input-schema三元组：

1. 已刊 R429 84d；
2. 已刊 R434 8899；
3. 本项 R436 4356。

这不是任意 source 白名单：每个实际文件全SHA、procedure schema和input schema都固定，实际 prior procedure/source/run/input必须相符。它仍用原79296 reader的 generic process_quiet 标准库函数，不调用旧 reader 的科学字段选择器或旧 schema build。

原 OriginalBindingView 接口复用被选 producer 的 validate_spec、Procedure.bind 和 producer_completed。为支持该无继承 metadata view，R436 dispatch显式调用 Procedure.bind_original193(self) 或 Procedure.bind_refined450(self)，不要求 view自行拥有这些方法；view不执行任何五阶段科学。rebind后 common inputs、新 checkpoint/current target/全十词/真实C四文件必须与 prior记录一致。

随后只以新场前三阶段 radial_replay、original_cuff_atlas、shared_field的真正完整返回作为原 R425 CLI的输入来源。metric/reach成功不是 held启动门；但旧场的前三阶段不能替代当前 prior procedure所绑定的原件。真实 plan、完整 marker、accurate witness与原 held参数仍必须作为显式实际输入，未在本接口挑选。

新 held 的 bind/run/finish 科学调用及 necessary readback正文与 R433逐字相同，除自身来源/三元注册、模块别名和独立标记外没有改数学。完整 O(3)、全像、共同 B消去/反射及非平面责任仍由原 R425实现；不能用一个材料位移或旧场直径代替。新 run/readback 子命令、input字段和参数格式沿 R433，schema改为本项；输出一份原90000字节上限必要对象，frame 为 BEGIN_R436_CURRENT_C_ORIGINAL_OR_REFINED_HELD_NECESSARY。相应 GITHUB_OUTPUT postsolve_held_* key不变。

本分支也不创建真正 held结论：必须等待新场实际 R425返回并按原 flags读取。若没有新 checkpoint、前三阶段、准确 witness或原剩余预算，保存原未付范围，不制造参数或假接受。

## 436.10 静态工作与后续实际责任

本轮完成的是完整源文本读取、实际callee字段对照、纯字符串完整差异和字节身份计算。以下原正文已按连续文本段逐字确认：

- 原 193 bind，只改方法名；
- OwnedChild；
- skip、shutdown、invoke、producer_completed、全部五 stage commands 与 finish；
- reader科学必要选择器与 process_quiet；
- held 的 bind、run、finish 主体。

没有 AST、import、编译、局部科学、对拍或 fixture。因此不能以这份静态说明声称新入口已经实际成功，也没有附加必须先通过的数值测试门。未来 Actions原实际返回是唯一科学事实来源。

必须保持的最终边界是：同 $P,G$ 的新 full450接受是来源；同完整闭面 $g$ 的精化还需冻结首次实际 $\mathcal K$，而当前入口不自动作这项跨 postsolve 比较；重新构造的完整 $F_{\widehat h}$ 是新几何对象；每项 metric/reach/held/反射或全局任务条件仍各付各的原证据。全 C/root族、全部338/112/450数据、两均值、完整角度、帽 marker/接缝与 pair universe均未因本来源分支省略。
