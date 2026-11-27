# Fejér 完整阶段矩阵作用域：不可写完整点的绑定、真实成本与全入口

日期：2026-11-27。状态：完整源码、全参数与来源构造已成；未运行该科学入口。现有 run12 原已排源保持原字。本项不构成科学预审、fixture 或独立准入门。

## 1. 具体改动与真实依据

原完整阶段矩阵核 `fixed_fejer_detached_stage_matrices.py` 为 47,791 B，SHA256 `7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7`。其 `CompleteDetachedStageMatrixScope._validate` 在每个真实矩阵请求前调用 `self.module._array_words(self.point_object,(self.q.free_size,))`，复制、检查并比较整个当前点。Fejér M160/J923 当前自由点为 1,333,370 个 binary64 词；该重复读与当前矩阵只包含三、六或九个控制变量无关。它发生于完整作用域内部，不是新的目标函数或 Jacobian 计算。

当前完整 normal `fixed_fejer_normal_lift_operator.py`（98,490 B，`1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778`）已在 `_select_point` 用 `np.frombuffer(value.tobytes(order='C'),dtype=np.float64)` 保存完整点。`_current_x` 除初始化 None 外只在这一处赋值；该 normal 的完整方法体在本次全部保持。这里的直接 owner 是内建不可变 bytes；没有把可写数组简单调用 setflags 后冒充不可变值。

本项只将阶段作用域内的重复整点词读取换为每次真实请求的强对象／owner／布局／点身份绑定。入口保原完整词读取和原 canonical array SHA 检查；出口增加完整词读取和入口逐字等号。完整当前点没有被压缩、投影、抽样或替换。

这是一项由真实源码定位的冗余消除。先前公开的 closure 累计 point_word_checks 属另一个 closure 核，不能把其数字冒充本阶段核的实测成本。旧阶段核没有新三种计时，本项也没有执行新科学运行，因此没有实测速度、加速倍数、命中率提升或误差结论。

## 2. 不可变 owner 与每次请求的完整条件

新 `_immutable_point_owner` 全函数字节取自已刊当前 closure 核的同名函数，保留所有条件：

- 当前点必须是 plain ndarray，不能是自定义 subclass；dtype 必须 native float64。
- 形状必须正好为当前完整 free_size 的一维数组，步幅为 8 字节，C 连续。
- 数组必须 readonly、non-owning，直接 base 的类型必须恰为内建 bytes。
- 完整 owner 长度、数组 nbytes 与 8×free_size 必须相等。
- 每次入口／阶段／出口都核对 q 的当前点对象与作用域持有对象是同一个对象、q 的点 SHA 与原作用域 SHA 相同；后续请求必须仍指向同一个 bytes owner。
- 作用域持有点和 owner 的强引用。source/model/base、真实 methods、carrier、全部 data tensors 及 versions/layout、完整 controls/frame/increment/zero target 字、角序与阶数仍按原路径核验。

精确长度的一维连续 view 覆盖完整 bytes owner；若是非零偏移的切片而保持同样完整长度，就会越过 owner 的末端。此条件排除了仅取 owner 一小段而伪装完整点。内建 bytes 的内容不能由普通 ndarray 写入口修改；readonly 标志也不能使它变为一个可写 owner。新策略针对原实际不可写点对象及其绑定程序，不声称容忍外部任意内存破坏或绕过 Python 对象语义。

因此，在入口已经取得真实完整词 W 并核对其 canonical array SHA 后，只要上述同对象、同完整不可变 owner、同 dtype/shape/stride、同点标识与全部原 source/model/data 守卫保持，阶段内部再次读出的完整词仍为 W。每次复制 W 对这个命题不提供新的数值信息。出口仍独立读取并比较 W，保实际作用域结束的完整证据。

## 3. 入口、阶段、出口与失败语义

入口顺序保留完整实际读数：

1. 绑定完整不可变点 owner。
2. 执行原 `_array_words` 全点词读取。
3. 用原 normal `array_sha` 重新取得 canonical point SHA，并核对原完整模型。
4. 继续原 carrier、data、角、阶、作用域及矩阵缓存构造。

每次原 `_validate` 先作新的阶段 owner 检查，随后仍作原来其余全部守卫。只删除原条件中的全点 `_array_words(...)[0] != self.point_words` 那一项；原点对象／SHA 比较仍同时留在原守卫内。没有借“no_grad”放宽原 active/transform 限制，没有删除 data version、control angular jets 或逐阶段 tau 检查。

出口不论成功或已有异常，都实际尝试 owner 检查及整点词读取。报告明确记录 attempted、immutable_binding_valid、complete_point_words_equal 和各具体异常。只有出口全部成立且作用域内没有阶段点绑定失败，`scope_point_binding_complete` 才为 true。出口总会清理作用域缓存、点、owner 和 data 引用，并将自己的完整记录加入原 kernel。

若正文已经抛异常而出口也失败，保原正文异常为外层原因；出口失败保在同一已关闭作用域记录内。若正文成功但出口失败，必须抛出失败，不能把该作用域当成功。入口未完整构造的作用域不会被补为 closed，也不会凭空产生一个完整成本记录；scopes_started 与 scopes_closed 的差仍如实反映此边界。

## 4. 科学程序保持的范围

新核继承原阶段复用策略，不重新定义其浮点复用等价性。原 `_request`、`_original_value`、`scalar`、`angular`、`_complete`、`_discard`、`_optional_failure`、`_carrier_identity` 方法完整原字；其原矩阵 key、digest、clone/store 和可选缓存失败语义未变。

同一完整 normal 的所有方法都原字保持；只把其 stage 与 adjacent 全源身份换为真实新体。adjacent 的全部函数／类主体不变，只更新真实 stage 来源。旧 root packet 完整 registry 各项保留，新增当前 normal 的完整来源条目；捕获不触发新的 F、J、root 或角阶升级。

本次完全复用原字的 reference、seed、base、literal Q、closure values、解析 J3、解析 frame、C1、reference calibration、memory 与 rows。强 source pin 仍指各自真实文件；没有把相同数学表达式当作可伪装原 whole SHA 的理由。normal schema 保原完整数学／表示模式，真实 source SHA 和 stage/adjacent policy 已明示本次实现差异。

全当前变量、原 32 个固定 stage、18 个 Q 字、gamma、全部角／径向积分、完整隐式 J/J*、原六jet、全幅度与 reach 行、原 permanent 集合、line search、接受准则和数值预算不减。closure 核每 stage 与 final 的强制完整原方程重读原字保留。

driver 从含缩进的 `def save_report(` 到 EOF 为完整 20,121 B，SHA256 `eb1d8813bd161358c451b06b47b570cdfdb9173b12f2661ee7ec37344dbf5254`，与真实 477499 父逐字相同。该版本没有增添数学标量进度钩子；后续若单独增加只读观测，须另标完整 source，不把新 suffix 冒成本版。

## 5. 成本记录严格分账

新增十二项整数计数：

| 类别 | 实际计数 |
|---|---|
| owner 入口 | point_owner_entry_checks / point_owner_entry_failures |
| owner 阶段 | point_owner_stage_checks / point_owner_stage_failures |
| owner 出口 | point_owner_exit_checks / point_owner_exit_failures |
| 全点入口词读 | whole_point_entry_reads / whole_point_entry_read_failures |
| 全点出口词读 | whole_point_exit_reads / whole_point_exit_read_failures |
| 入口 canonical SHA | whole_point_entry_array_sha_checks / whole_point_entry_array_sha_failures |

另有三个真实累计计时：`point_owner_binding_seconds`、`complete_point_word_read_seconds`、`complete_point_array_sha_seconds`。前者是入口／阶段／出口 owner 条件成本，后两者分别是完整词读取与原 canonical SHA 成本。它们按已关闭作用域累计，定义明确；未关闭／构造失败的请求不虚计完成。

原 scope_seconds 从原位置开始，包括自己的 stage chain 和现在的出口，但不包括更早的入口全词读。因此不能把三种新计时与原 scope_seconds 当成互不交叠的分项求和，也不能断言它们必小于旧 scope_seconds。原 original_method_seconds 仍保原语义。

纯读器通过完整新 helper 的 stdlib validator 验证新的整数关系、非负有限计时、own-point 最后作用域、完整 owner 布局及失败状态。新自由变量数按原模型完整 J/M/fixed_core_first3 推导，不写死为 1,333,370。原 38 个 own-point snapshots 没有捏造新的 stage 成本字段；它们的原完整校验继续。新增 stage 成本来自 latest_operator_metadata 的完整独立 stage record，不能把 latest 回填成各旧 snapshot 的观测。

科学 summary 路径为 `latest_operator_metadata.detached_stage_matrix_reuse.actual_counts.<key>` 及该对象下三个 seconds；纯 summary 为 `detached_stage_matrix_diagnostics.actual_counts.<key>` 及同对象下三个 seconds。每份完整 summary 增加 15 个标量。

## 6. 同目标的真实父场与完整历史

本版新增严格的 **477499/274d Fejér 同目标父族**，为必要的真实后继提供完整入口，不把旧不同目标改标签。

完整旧 driver／reader／normal／binding 和旧 110 个 source role 必须实际逐字核验；旧 3b3 validator 先验证原完整模型，新 validator 再验证新完整模型。完整 frozen base、seed、chart、scalar、Q、free layout、32 stage partition、四个未改 working policies 均保持整对象相等。只剥除已经分别完整验证的 normal source、calibration 的 endpoint 来源以及 stage/adjacent 两个 policy 字段；不做不受约束的字段忽略。

terminal history 读取原整 pure reader 及原 whole report；其每个实际 inbound history 文件递归重新读取、全 SHA 比较、顺序保留。原 explicit/protected 三角色数组、全部 typed 行、原 ordinal、首次发现来源和 nested transfer 记录完整迁入 runner 报告。所有原已知地点必须是当前完整集合的子集，不凭 counts 当集合。旧不同 g 的四个父族仍只有来源／未返义务，不能由其继承当前物理值或 typed 优先级。

complete-parent 还必须实际核对全 13 个 final NPZ 成员及完整 dtype/shape/layout/core/omega/H/mesh/fixed words，与原 whole final report／metadata／geometry point 同一。原完整 final 复制主体保持；current model、norm、roots、Phi、geometry 和归因仍按新完整入口重读。旧 final 的接受数和原失败／可行状态只作为父来源，不自动成为新结果。

独立模式保持原四个未知 peer，并明确追加 Fejér run12 `46011377225/1` 的真实 source `477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd`。它从原固定 reference 初点开始，不造未来父 final，不把未知 typed 首次发现顺序或未返回末点补成空。真正父模式由真实父的完整 nested lineage 继承原义务，因原 parser 语义不会并传 independent/pending flags。

同源完整 restart 仍保持其原 whole model/norm/checkpoint/source 守卫。所有实际来源和输出先后字节复核继续，没有来源宽松分支。

## 7. 两份完整参数

| 模式 | science argv 数 | pure argv 数 | science / pure selectors | 活进度 selectors | 两完整 step 紧凑字节 |
|---|---:|---:|---:|---:|---:|
| independent | 157 | 7 | 398 / 385 | 48 | 90,846 |
| complete-parent | 144 | 7 | 398 / 385 | 48 | 90,381 |

两份都从实际 92,380 B 原 Fejér ready `ab5c00086e21faaa5017ea469c4a63e7d389ecc3019b03a28e46b9daaa129578` 完整派生。原 153 个 science argv 的数值项与顺序全部保留；差异只有明确的模式 flags、完整父报告／checkpoint／manifest 和独立输出路径。pure 原 7 参数完整保留。原 383 / 370 summary selector 每一项原值保，原 48 progress 每一项原值保；不借减少原参数凑文件大小。完整计划用紧凑 JSON 序列化，所有真实 step 字段保全。

原数值配置仍是 angles2048、stage-block64、angle-block8、integration-order8、norm jet-sum/ell0.05/tau24、threads4、damping0.01、metric directions1/maxiter16、restoration directions4/maxiter64/damping0.01、line-trials15、active rows192、qp atol0/rtol1e-6、reach0.03/safety0.992/activeband0.025、markedD4.2/witness0.9/height1.01、spectral p4/eps0.001/scale0.05/legacy0.5、target1e-9、panels128、normal32、原 endpoint 与全部 mean/profile/root budgets。完整两个 Q bubble、gamma、18-word frozen input 与每一 flag 的实际字以各 ready 为准，本段不代替完整 argv。

独立目录是 `{work}/fixed-fejer-stage-point-independent`。父场目录是 `{work}/fixed-fejer-stage-point-complete-parent`，真实父路径为 `{work}/fixed-fejer-immutable-point-first/report.json` 和 `final.npz`；该父必须实际返回才能消费。原 reference/input 路径不变，全部本次真实文件仍由固定 input binder 验证。若在新 runner 使用，先执行已刊两个完整输入构造步骤；不迁 raw 输出到 Git/Artifact，不预填本次参考或 field SHA。

future run、report、model、point、checkpoint、accepted count 与 complete 均为 null。完整 step 的 parent_bundle 仅是文件依赖路径声明，不能冒实际文件已经存在或已经完成。

## 8. 十个独立运行体与共享源码

| role | 完整文件 | 字节 | SHA256 | 未引用 Git blob |
|---|---|---:|---|---|
| stage_matrices | `fixed_fejer_immutable_point_stage_matrices.py` | 61280 | `e4d42910f9550a20d0afc16aab8f54b5ea1ceb18ace375128f3a79bfef0e76ce` | `002985b6b754585f08f05b349f305adf03ad2f9e` |
| adjacent_matrices | `fixed_fejer_stage_point_adjacent_matrices.py` | 36766 | `d04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5` | `d5ab132b50b7f5caae92a417f590ee44e77c6ca0` |
| endpoint | `fixed_fejer_stage_point_normal_lift.py` | 98490 | `42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10` | `ffdaf4a094c7a0363bd6bc3ed316ba1e7e8ec25c` |
| root_packets | `fixed_fejer_stage_point_root_packets.py` | 73070 | `140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf` | `310aa66a367efe0bb6ca26da12b4b4395abd3f08` |
| analytic_J3_binding | `fixed_fejer_stage_point_source_binding.py` | 38356 | `9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f` | `fb9dc94fa9b137dd64f602d9cd84b8997d36bdc2` |
| envelope_transfer | `transfer_fixed_fejer_stage_point_memory.py` | 78863 | `afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed` | `7f1f3971893d8895d7e1b8cc3612e563a44d3095` |
| geometry | `so3_fixed_fejer_stage_point_geometry.py` | 70709 | `2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471` | `2677d379e87b359088177b244428894311348996` |
| driver | `fullclosed_fixed_fejer_stage_point_so3_qp.py` | 93158 | `050a6067fbb2fb4d054a97bf73899cfe5d4629197e42c39f00846a1f6a63b268` | `b0374f2db88ca38a936c7eadfc97f5377922c146` |
| launcher | `launch_fixed_fejer_stage_point_actions.py` | 21785 | `8fed7b6a7ff6c988ee2240a4193f9440fd91ef158e5ac47d6248868d4e19214c` | `fed243876328a2933fcfb10288f6f42edda16211` |
| reader | `read_fixed_fejer_stage_point_so3_report.py` | 97975 | `42e198f8d886641048059c3cdd8110b8bc3d000cdf350da1de54ac4bb83014a0` | `4304a1fdbe907bdb9c6708d7a89f5a18733ce15b` |

十体共 670452 B，每体小于 100,000 B。完整 driver 共 119 个角色；原 110 个 pair 全部仍在真实当前 SOURCE_PINS 中，不只按 role 数宣称完整。新增 parent aliases 与原 driver／reader 明确区分旧源和当前源。

未改的 reference/seed/base/Q/closure/J3/frame/C1/calibration/memory/rows/旧历史源全部复用正式已有整文件。本项没有复刻它们来换名制造另一科学算法。

normal 数学 schema 保持 `complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1`；新 driver schema 为 `complete-fixed-fejer-stage-point-material-envelope-SO3-QP-v1`；新 pure schema 为 `actual-fixed-fejer-stage-point-envelope-SO3-readout-v1`。各新 helper 和 transfer definition 全部真实新 whole 来源固定，旧各源保持原字。

## 9. 完整再生与实际已做的文本工作

完整 source reproducer `reproduce_fixed_fejer_stage_point_sources.mjs`：54988 B，SHA256 `442a45f849badc2bc054ca4b3d288b627f72a5383821768c9449e3db4e78bfd5`，blob `5e5f9010842c03ca406b94a460df4a6d80a964a6`。它读十九个完整小源：九个 Fejér 下层、八个上层，以及已刊 M320 binding/transfer 两个纯来源／历史函数的完整源母体。后两者只供完整纯文本方法复用，**不消费 M320 科学输出，也不是当前 runtime M320 依赖**。

实际已用 JavaScript 将十个完整源逐字重建，再按每次真实替换的确定位置逆还原到完整父源。某些 after 片段在文本中本来不唯一，逆还原用正向记录的完整位置和原片段，而不是用不唯一字符串盲换；每次旧片段 multiplicity 与全部最终字节都核对。实际补丁数分别为 stage26、adjacent1、normal2、packet1、binding9、transfer18、geometry3、driver4、launcher2、reader4，总70。

完整 parameter reproducer `make_fixed_fejer_stage_point_ready.mjs`：16366 B，SHA256 `3626ade28637edbfa12988c11d8055b5a216bdb43fb9c4479ec64f160b7ad87e`，blob `52d78852d4f07fca0fb3aa0cb47a7d01821af0a1`。实际 JS 从原 whole ready 重建两份完整 JSON，结果逐字相等，并逐项比较全部原数值 argv 顺序、全部原 summary 和 48 progress 映射。原 ready 的真实 basename 在 INPUT 内明确存在，文件路径与 whole SHA 一致。

未执行 Python AST、compile、NumPy/Torch、F/J/root、局部 fixture、全科学求解或费用计算。两构造器是已授权完整源码与全参数保全工具，不是另加的执行门。只有实际完整 Actions 运行才能产生本版真实成本、场值、接受与完成状态。

## 10. 如何接后续 N、M、J 完整族

公开 API 保持 `CompleteDetachedStageMatrices(q, frame_c1_module=...)` 与原 `scope(data,keys,order,phase)`；scope 的 scalar/angular 请求 API、原 zero_target、stage/order/角词和矩阵返回合同全不变。当前入口已完整闭合 Fejér M160/N2048/J923。

N4096、M320、J1845 的当前完整族不可仅改此 helper 的 source 标签复用。其完整 base、C1/J3/closure 的真实 SHA、normal layout/方法锚、adjacent、packet registry、绑定器、geometry、driver/launcher/reader 和实际 parent 模型关系仍需用各自已登记完整母体明确派生；原所有 source pair 必须保。M320 必须继续冻结 reference M160，J1845 必须继续完整精确 quintic 限制与 non-nested Gauss 并集，N4096 必须继续冻结 reference N2048。这个 helper 的 free_size/owner/layout 读取按实际 q，不对这些族另加数学缩减或新方程。

本版证明可用于各相同不可变点持有机制；它不证明另一族已经改过、已运行或已加速。其他三族在其 owner 完整源未正式派生前保持各自冻结来源。任何未来父仍必须用本次真实 full13/point/history 绑定，不能因同目标或 schema 相似迁移 unknown final。

## 11. 交付状态与后续真实观测

- independent ready：99934 B，`db456635a1811b993398d8ade8276ab753e63a2ac13ea878d27b98d313ef4b39`，blob `87b735efa8f879ded64cac07e878b41a6385834f`。
- complete-parent ready：99478 B，`7709e8d96db33d4722ff4128b475a237972932411e51b4705186eaadab1d96df`，blob `83631109484a92ef5bcf6efece8a6e741dcaab10`。
- 两份都是完整紧凑 JSON，99,934 / 99,478 B；公开保存应保原字而不展开后超过单文件边界。
- 现有 run12 未被此工作修改；其根计数与新 point digest 不作为 accepted/final。
- 本版原 48 活进度映射未改。根已要求下一独立观测派生输出已真正取得的 initial/current Phi、完整有限 Gram／geometry violation、接受数与 stop，并保各项自身点与阶段；该后继不得新算 F/J，不把尚未完成的数据补值。本交付不冒称该后继已经存在。

本项没有删除变量、方程、stage、集合、迭代预算、原 guard 或历史责任来换取短运行。它明确移除一个被真实不可变 owner 证明为冗余的全点读取，并为新旧实际成本留出可读的完整记录。
