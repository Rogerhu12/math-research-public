# R431：原总钟、实际 frozen450 父与必要读回的薄入口

作者：ChatGPT /root/amplitude（AI），2026-11-16。本文绑定两件独立标准库源码及 [R431 条件结论](../results/R431-same-clock-frozen450-mesh-owned-execution-and-necessary-readback.md)。没有请求号、实际 parent、max_nodes、资源参数、run 或新接受结果；未来科学只在本仓库 public Actions 执行。本次只读写文本、JSON 元数据与字节身份，没有导入、编译、运行科学模块或新增 fixture／测试／科学门。

## 1. 可发布文件与不变科学入口

| 新文件 | bytes | SHA-256 |
| --- | ---: | --- |
| `computations/geometry_20261116_current_C_frozen450_mesh_owned_launch.py` | 33598 | `4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868` |
| `computations/root_20261116_current_C_frozen450_mesh_necessary_readout.py` | 25196 | `3949b61a4d7c5d96b5751f33ca1fd20288a176b73a9df97dd087ae828e65428c` |
| `results/R431-same-clock-frozen450-mesh-owned-execution-and-necessary-readback.md` | 12813 | `61f6a1a499c248e317c316e81988faf5d543f18197adaa7cd53113d9bf36149a` |

本接口自身的完整 bytes／SHA／Git blob 在交付 manifest；不把含自身身份的表递归写入本文。

原 `geometry_20261115_continuous_ten_frozen450_mesh_refinement.py`，33251 B／`70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928`，是唯一新网格科学 child。它的正文和原 R427 proof、原 193 driver、R400 writer 均不改。新增 launcher 只绑定真实来源、生成小 recipe、管理进程与原绝对钟；新增 reader 只解析已有原输出并选单份必要结论。

原模型仍有完整 450 个未知量、338 物理状态、112 core、零 active、零固定低 core 目标行；112 模态、2048 角、两 mean、4096 material／physical angles、8 外迭代、17 档原试探、native 32×10、eta1、敏感度 eta0、tol2e−9、RMS1e−6、BC1e−11、FD5e−5、真实 current-H 与 338×112、final-J／fresh audit 全保。mesh 容量只限制资源，不删原 R427 必需节点或改成功谓词。

## 2. 直接依赖与完整 runtime 的边界

以下八个旧源是两个新增入口明确使用的直接身份。它们不是完整 native／full-DN closure 的替代品。

| 旧源 basename | 真实作用 | 固定 SHA-256 |
| --- | --- | --- |
| `geometry_20261115_continuous_ten_frozen450_mesh_refinement.py` | 原科学 child／原 adapter schema | `70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928` |
| `geometry_20261115_continuous_ten_full453_frozen450_launch.py` | 原同 job 起点及 deadline／输入 receipts | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` |
| `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py` | 原两阶段实际 producer，R427 runtime 的来源 | `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` |
| `geometry_20261115_continuous_ten_frozen450_checkpoint.py` | 原 R400 manifest／真实接受身份 | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| `geometry_20261115_current_C_ten450_postsolve_geometry.py` | 仅标准库生命周期、receipt、进程观察函数 | `84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a` |
| `geometry_20261115_current_C_pruefer_positive_tail_client.py` | 原 R427 实际 native client argv | `acb8b67b8e44dbfae9b0d166bfc75910f2c48a6aca238571db44d20520a0a1f9` |
| `root_20261115_continuous_ten_two_phase_necessary_readout.py` | 原纯字段 phase／FD／checkpoint／native 选择函数 | `622f4f3c8255a4980e931457f912cca1ee00d25af965da18f39aecc6860c8d72` |
| `root_20261115_current_C_pruefer_positive_full453_necessary_readout.py` | 原 metadata document／stream／log／identity 函数 | `34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9` |

launcher 直接 `PINS` 为前六件；reader 直接 `PINS` 为新 launcher、70a570、84d045、622f4f、34b49f。两件新源的直接并集是八旧加二新，不能称此十件已经替代原 193 全部源码。原 R427 继续调用实际 193 `runtime()` 并加入原 driver 和自身 source，再合并实际 current-target owner closure；所有旧 scientific pin 逐值保留。未来运行入口必须保原完整 computations、恢复 source-topic、原 accepted96 与 current native config 等真实输入。本文没有为未选请求捏造总 pin 数。

加载 84d045 仅取得其标准库函数，不构造其 `Procedure`、不执行 R409／R413／R418／R422 五阶段。加载 622f／34b 只取 metadata 函数，不调用旧 main 的两阶段 binder，也不导入 sampler／full-DN 科学模块。原科学模块只由实际 R427 child 加载。

## 3. 显式输入合同

launcher CLI：

```bash
python -u "$COMPUTATIONS/geometry_20261116_current_C_frozen450_mesh_owned_launch.py" \
  --input "$R431_INPUT" --input-sha256 "$R431_INPUT_SHA256"
```

这些变量只表示未来实际路径与真实 SHA；本稿没有赋予其参数值或假定存在 accepted 父。输入是单个 UTF-8 JSON 原字节，SHA 在读取前核对。根对象必需字段如下；`resources` 必须恰含四键。

| 字段 | 类型和来源 |
| --- | --- |
| `schema` | `current-C-continuous-ten-frozen450-mesh-owned-launch-v1-input-v1` |
| `namespace` | 本次真实 `RUNNER_TEMP` 内的原 request-owned 目录 |
| `origin_launch_directory` | 原 193 launcher 的真实输出目录，内含其 `result.json` |
| `parent_launch_directory` | 首次等于 origin；后续可以是本同一冻结 launcher 实际接受返回的目录 |
| `job_deadline`、`job_deadline_sha256` | 原 193 launcher 已消费的那一份实际 deadline 文件及完整 SHA |
| `computations` | 当前固定 checkout 的完整 computations |
| `accepted`、`accepted_sha256` | 原 193 实际 consumed accepted96 输入，不是新 field 的接受凭证 |
| `tail_config`、`tail_config_sha256` | 原 193 实际 current-native config 原件 |
| `tail_source_root` | 原 193 argv 中真实 `--tail-source-root` 恢复目录 |
| `out` | namespace 内独占 fresh 目录；不得包含输入，须与 origin／parent solve 输出互不包含 |
| `max_nodes` | 显式整数且至少 2；实际完整 nested seed 超容量时仍按原 R427 资源返回，不删节点 |
| `resources.mesh_process_budget_seconds` | 本次显式正有限 process cap，不重置总钟 |
| `resources.child_shutdown_reserve_seconds` | 显式正有限 TERM／KILL／wait 共用关闭窗口 |
| `resources.minimum_free_bytes_at_start` | 显式正整数 startup 可用空间要求 |
| `resources.free_bytes_resource_stop` | 显式正整数，严格小于 startup 要求 |

参数词、H、J、residual、当前 merit、旧 field 数组或旧 FD 不在该调用者输入中。源码拒绝靠 caller 新填的十词替换实际 checkpoint；真正要取的词从真实 manifest 读取。

`origin.actual_input_files.accepted` 和 `current_native_config` 的原 bytes／SHA 必须与这两个真实文件相同。`tail_source_root` 必须等于 origin 原 command 唯一 `--tail-source-root` 后的实际解析路径。它是保原实际恢复来源；不重新下载或用相同显示名称伪装另一份 source-topic。

## 4. 实际 parent 与新小 recipe

origin 的 schema／source 分别为 `current-C-continuous-ten-full453-frozen450-owned-process-launch-v1`／6ff21118。其 `current_finite_BVP_accepted`、`completed_driver_return`、child exit0、quiet、无 resource／external stop 必须真实返回；其 11dd72 driver 原 adapter 还须同时记录 actual453 和 actual450 接受、owner closed、leases released、无 close exception。

首父 checkpoint 必须是原 R400 writer43f217 在此 job 真实写出、actual_driver11dd72、完整450／338／112／k0／固定core0／M112／N2048，原 full-DN 接受，且未把453删行重标成450。其 repository／run／source_commit 必须是当前实际 Actions。

后继父若不是 origin，须是**同一新 launcher 的实际冻结 SHA** 返回，仍指向同一 origin receipt 和同一 deadline receipt，actual70a570 mesh adapter 接受且 closed／quiet，再指向原 R400 写出的实际新 checkpoint。每次 complete_ten_float64le 和 current_target_identity 都与真实 origin 相同。此检查保来源和原算法责任，不从十词相同推出两个 field 相同或网格误差已减小。

绑定后写 `out/actual-mesh-recipe.json`，schema 为 `explicit-current-C-ten-frozen450-nested-mesh-refinement-v1`。其 parent SHA、accepted SHA、原 height_sign 由实际文件产生；十参数顺序固定为 `[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3,xi]`。全部科学常数来自原 R427 的明文合同，唯一 caller 提供的 mesh 容量为 max_nodes。原 193 recipe 和 deadline 均不改。

原 R427 child argv 全部具体为：

```text
--recipe <out/actual-mesh-recipe.json> --recipe-sha256 <actual SHA>
--accepted <original accepted96> --accepted-sha256 <actual original SHA>
--parent-directory <actual parent checkpoint directory>
--parent-manifest-sha256 <actual parent checkpoint SHA>
--tail-config <original current native config> --tail-config-sha256 <actual SHA>
--tail-source-root <original same-job restored source root>
--tail-client <computations/original acb8 client>
--jac-workers 2 --node-heap 6144
--out <out/refined-BVP> --work <out/banded-work>
```

原 R427 在 `prepare_refined` 用真实 parent 数组作插值初猜；原 mesh、可表示 midpoint、完整 literal knots 的并集仍由原源决定。所有450行 fresh RHS、preflight、current-H、FD、full-DN、final-J／audit 重新执行。parent 的旧 RHS、J、FD 和 native cache 不成为新 acceptance。

## 5. 原 deadline 与资源停止

实际 deadline schema 是 `request193-owned-job-science-deadline-v1`。launcher 先核其完整 bytes／SHA 等于 `origin.actual_job_deadline`，再核当前 run／source、origin recipe SHA，以及 `science_seconds_from_namespace=18900`、`readback_reserve_seconds=2700`。不能把 namespace 的另一个相似 JSON 当作同一个已消费时钟。

令原 `namespace_created_unix_seconds` 为 $t_0$；全部后继仍有同一个 $T=t_0+18900$。在真正启动前计算

$$
b_{\rm actual}=\min\{b_{\rm explicit},\max(0,T-t-q_{\rm shutdown})\}.
$$

绑定、父读取、小 recipe 生成及所有前序科学耗时均已经消耗原钟。child 同时受单调钟 cap 和原绝对截止减关闭预留的约束；finally 仅取得同一个关闭窗口的剩余部分，不再续发另一个 q。2700 秒仍是必要读回／关闭／清理余量，不变成额外科学。

空间要求、process cap、原 namespace 到期分别记实际 `resource_stop`；SIGTERM／SIGINT 另记 `external_interruption`。这些不是 mathematical rejection。原 child 75 仍保原75：它对应原 mesh 容量或无可表示新点的资源范围，不标为非线性拒绝／收敛。其他 child 非零码原样保，原 status／日志仍在临时树。没有 adapter 时不会按 exit0 或成功 job 猜阶段。

原 R427 `phases[0].started=false` 不能推出没有科学工作：prepare 的构造、fresh450 RHS 或 preflight 可能先发生。新摘要保 seed／preflight、current-H、FD、full-DN 和 final 的各自原字段；只在实际 child 尚未启动时声明这次 R427 未开始。

## 6. Owner 与静止责任

R427 用 shellFalse、新 session 启动；child 环境移除 token 项。stdout／stderr 留在本次独占目录。R429 `OwnedChild` 记录实际 PID／PGID／SID／start-time，信号仅对仍匹配的已观察进程。关闭、wait／reap 和原身份冲突完整留在 launch result。

新 reader 不只相信一个 quiet 布尔量。它再次观察 launcher 原 PID／start-time、child 已观察身份和其原进程组，并要求实际 child returncode 已返回、无身份冲突、无仍活跃成员。这个有限观察没有被包装成任意第三方逃逸进程的证明。已读原 acb8 的 `Popen` 没有 start_new_session、同步 bridge 的 `spawnSync` 没有 detached，但不能只由这两个点推断所有可能后代都被证明。

若 launcher 在 input／pin／初始化阶段尚未建立 `result.json` 即失败，本 reader 不假造 owner 记录，也不在未知静止状态下读可能仍写入的 entry logs。未来原规则 owner 的 always 错误记录应保该 bootstrap 失败；当前新 reader诚实输出缺失／未读范围，不写 cleanup marker。这不改变原 2700 秒规则同步、真实 pull 或 frozen science checkout。

## 7. 原输出路径与返回含义

| 本次 owned 路径 | 来源与含义 |
| --- | --- |
| `result.json` | 新 launcher 独立 schema；原 source／run／deadline／parent／child／quiet／resource receipts |
| `actual-mesh-recipe.json` | 本次实际父生成的小 recipe，非预填参数 |
| `mesh.stdout.log`、`mesh.stderr.log` | 原 child 完整临时文本，必要 reader 只选明确错误范围 |
| `refined-BVP/adapter-status.json` | 原70a570 status，不改 schema／source 标签 |
| `refined-BVP/refined450/initial-guess/` | 原 nested seed、mesh plan、preflight 等 |
| `refined-BVP/refined450/actual-H-response/` | 本次真实 current-H／FD／cut 比较 |
| `refined-BVP/refined450/full-DN/` | 原450 full-DN；其 `true-tail` 是本次新 native owner 的真实 ledger |
| `refined-BVP/refined450/accepted-checkpoint/` | 仅原新接受后由原 R400 writer 实际写出 |
| `banded-work/` | 原线性／数值临时工作目录 |

`actual_adapter_scope` 保存实际科学状态；`current_refined450_accepted` 只有实际原接受、child clean return、静止且无 resource／external stop 才给真。可消费后继还检查 launcher已返回、source、parent、deadline及原writer，不能仅取一个 bool。`completed_driver_return` 不替代原科学 accepted；`complete_necessary_summary_produced` 在 launcher 固定为 false，只有独立 reader 才能完成必要记录。

原 full-DN 接受之后捕获的新 manifest 指向实际70a570 producer；parent为实际原 manifest。新 field 不冒成原193，也不冒成任何旧 mesh 场。所有十词含负零完整保存，准确 dyadic另列，不经过caller浮点重写。

## 8. 必要 reader、单份上限与未返回大表

reader CLI：

```bash
python -u "$COMPUTATIONS/root_20261116_current_C_frozen450_mesh_necessary_readout.py" \
  --namespace "$ORIGINAL_NAMESPACE" --launch-directory "$ACTUAL_MESH_OUT" \
  --computations "$COMPUTATIONS" --out "$R431_NECESSARY_OUT"
```

可显式加 `--entry-stdout`、`--entry-stderr` 指向本 namespace 的外层入口诊断。两个目录必须是不同 fresh siblings；reader自己不发送signal、解方程或删除文件。

reader完整读取存在的原 JSON／gzip／native trace／trial／linear child 流，使用原622f `phase_documents`、`fd_view`、checkpoint读回与 `native_view`，再选择必要scope。主要返回如下：

| 类别 | 必要正文 | 只保 identity／count 或不返回的范围 |
| --- | --- | --- |
| 来源／钟／owner | 实际source/run、deadline、input/parent/newcheckpoint receipts、quiet、resource、未起阶段 | 大source closure按完整identity，不重传每项 |
| mesh／seed | 原节点计数、容量、原words保留flag、fresh RHS／preflight状态 | literal knots和collapsed midpoint全集身份；后者只另返首末记录 |
| FD | 原 `fd_view` 显式逐方向／逐层误差、flags、原key-set含义 | 大扰动原数组按原reader身份范围 |
| 原门 | full-DN／RMS／BC／final-J／audit／cut／checkpoint原值若实际存在 | 未发生阶段不补数据，不由缺字段推出通过 |
| native | 每call原norm／converged／audit／history与trial count／error等15列；最后实际call detail；所有失败／未完成call scopes | 早期trial细节、大states/J、成功factor全RHS及完整stream正文只身份 |
| 错误日志 | 实际匹配错误行数、首2和末1行的选段与原line identity | 整日志不返回；没有匹配错误不代表科学成功 |

原34b通用 `small/short` 继续适用：一般长字符串最多1800原字节前缀并附完整UTF-8或surrogate映射身份；匹配日志行最多1200字节前缀；一般列表长度大于16时仅保identity／count。异常、traceback因此不是完整原文运输。FD显式选中的逐方向／逐层列表来自原 `fd_view`，没有借通用列表规则删掉这些已选层。缺键仍由原选择器区分于null，完整metadata原文件保留至清理。

完整 parsed document／log／omission index 留于 `necessary-readback-index.json` 临时文件；单份摘要只返计数、完整index身份和明确scope。不把原科学大表编码／拆片搬运；没有实际输出，不能保证所有可能失败记录都必小于90KB。

正常输出 `scalar-summary.json` 是一份按键排序、紧凑ASCII JSON，**含末LF**硬限90000B；stdout原标签为

```text
BEGIN_R431_FROZEN450_MESH_NECESSARY
<one actual necessary JSON>
END_R431_FROZEN450_MESH_NECESSARY
```

另打印 `R431_necessary_summary_identity`，字节口径为该完整ASCII正文含LF。GITHUB_OUTPUT为 `mesh_summary`（无末LF）、`mesh_summary_bytes`、`mesh_summary_sha256`；后两值对应含LF正文。

正常schema为 `current-C-frozen450-mesh-one-necessary-readback-v1`。超限只返回同前缀 `-over-budget` 小对象：拟完整summary的bytes／SHA、每section大小、错误数、quiet与临时index身份；exit70、completefalse、无marker、不清原件。没有更高第二上限，也不拆数据来假称完整。

## 9. 清理与后续真实分支

两个新源均不upload、写Git、删除raw或替调用者做namespace清理。必要 reader只有在实际quiet、原读取无错且单份summary未超限时才写 `readback-complete.json`。它明确还要求所有原readbacks及清理时的当前quiet；它本身不是通行删除整个namespace的授权。

未来同job工作流的最小顺序是：原193真实两阶段与原必要记录 → 本入口实际mesh child → wait/reap → 新必要reader → 已明确接入的下游消费者 → 所有原与新必要记录成功且当前owned进程静止后统一清理。若必要reader失败／超限／unknown quiet，不主动删除raw；runner销毁后不把仅存SHA冒充可恢复场。

原 continuous-E 的四metadata与 `large-arrays/complete-source-radial-panels.jsonl`、`large-arrays/source-piece-index.json` 要保到实际已接metric／provider结束。原factory／definition／numeric geometry、source-topic、真实450checkpoint也须留到它们最后一个现场消费者结束。R431不重C、不调用R426、不预选其precision或新增几何条件。

已刊R429只接受原193两阶段producer。若几何要消费这个新mesh field，必须独立明确增加真实R431/70a570/R400来源分支，再付新的R409径向、R413 atlas和原shared／metric／reach；不能把本result换schema送给旧R429，不能把父几何凭同十词转移。R433／R434的其它独立槽也不会被本入口隐式执行。

目前R431没有workflow／request、没有max_nodes与资源数值、没有实际accepted父或新field。完整接线需要未来参数声明和原source闭包；此源交付不添加批准、短跑、fixture或独立数值比对前门，也不承诺mesh／谱收敛、准确连续误差、metric、reach、held或刚性已付。

## 10. 相对先读草稿的变化与交付范围

数学源没有修改。新launcher含原accepted／current-native config的实际receipt绑定及原source-root argv身份，reader绑定其最终SHA。root已读的33598B／25196B运行两源到本次最终仍逐字相同。proof同步两源identity并准确补写原34b长字符串／日志／一般列表缩写范围；本文是首次完整接口。先读proof到最终的完整小diff单独交付，两个新增运行源另给相对空文件的完整diff，不把未发布旧草稿当作新科学来源。

交付manifest列出四件正式publication路径、bytes、SHA与小文本blob；私有完整新增diff和先读稿到最终的小diff仅供来源核对，不把新可重算科学raw放入仓库。全部科学仍未本地执行；本稿不报告本地AST、编译、数值或新fixture通过。
