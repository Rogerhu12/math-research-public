# 固定 Fejér 目标的完整 M160 → M320 模态精化入口

日期：2026-11-27。状态：完整源码、完整两种参数计划和纯文本再生器已成体；没有科学执行、没有 M320 结果，也没有据进度填造父 final。此说明不新增数学结论编号。

## 1. 本次交付的确切范围

本包把已刊固定 Fejér 族的当前表示从 M160 扩为 M320。固定参考仍为 M160、J923、N2048；maker、R690 参考、支持区 seed、固定输入纯绑定和全材料包络 memory 五个原完整源原字共享。当前试探 core 与三分量 SO(3) rotation 的频率增加，固定图、完整标量法则、径向网格、观测权重、Q、gamma、32 个 normal stage 及数值预算均保留。

输入有两个完整计划。独立计划从同一参考的完整初点作零扩张，显式保 run12 及旧四个未知 peer 的来源责任。真实父计划只能消费实际返回的 `477499` / `274d` Fejér M160 完整报告和全部 13 个 checkpoint 成员；进度文件、某个新 point digest、输入准备成功、command.json 或尚未返回的求解都不能代替它。源码还保完整同源 M320 restart 和显式终态历史后参考初点模式；本次两个 ready 没有伪造这两种模式的未来路径或结果。

本包没有改当前运行中的 M160 源或队列。18 个新完整运行体各小于 100,000 B；driver 128 个 source roles 保留实际 M160 父的全部 110 个 `(path, SHA256)` pair，包括被新角色替换者的明确父别名。旧 run10 M320 是完整构造来源，不是同目标的实际父。

## 2. 同一个数学目标与不同的表示身份

精确固定目标由已刊 maker `fixed_fejer_r690_reference_inputs.py` 的 `mathematical_target_recipe()` 定义。七个预先指定有理系数先按 binary64 ties-to-even 转换；转换得到的二进制有理数本身为准确参数，后面 153 个参考系数是正零。它们不是旧优化输出。R717 的理想有理设计与舍入界不被本包重做。

记固定参考支撑函数为 `p0(phi)=1+sum(cbar_m*cos(2*m*phi))`，`rho0=p0+p0''`，`Theta0'=rho0`。准确目标仍为 `g=ds^2+a_R690(s)^2*dTheta0(phi)^2`，完整 R690 尾部仍属于该法则。物理相位仍用 R248 的 `R_alpha U(s,Theta0^{-1}(Theta0(phi)-alpha))`，`alpha=pi*t/2`；本次不改 t、帽、握持构造或它们的证明责任。

M320 base 同时保存 `reference_M=160` 与 `current_M=320`。固定 `parent_core` 和 `reference_freq` 长度 160；当前 `core` 和 `freq` 长度 320。normal 的 `_chart` 明确读 `reference_freq`。固定参考的完整对象、160 个 chart words、标量参数、mesh、reference bundle 与 maker target 都保原实际对象。M320 外层模型、Q 的自身完整点 digest、calibration 的坐标布局及当前 norm 身份会改变；这些新 canonical 摘要不被解释为更换数学 g。

实际 run12 的已返输入给出数学目标摘要 `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`、参考模型 `ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac`。它们是已返输入来源，不是尚未求得的 M320 场摘要。运行时仍完整读取与核对实际输入，不以本说明替代数据绑定。原 run10 的 e711 / 081 / 4ace 证据不被重命名为本目标。

## 3. 完整自由量与三个不等偏移块

J923 的 3J=2769 个径向 Hermite 槽只去掉原来的三项结构零槽 `0, 3*(J-1), 3*(J-1)+1`，留下 2766 个自由径向槽。K=3 固定 core 系数保持原意义。旧 157 个自由 core、全部旧 rotation words 和 H 均保；M320 另加 160 个自由 core 和每径向槽 480 个自由 rotation 模态。

| 项目 | M160 | M320 |
|---|---:|---:|
| 固定参考 M | 160 | 160 |
| 当前 core 总数 | 160 | 320 |
| 当前自由 core | 157 | 317 |
| 每径向槽 angular channels `3M+2` | 482 | 962 |
| 自由径向槽 | 2766 | 2766 |
| 完整自由量（含 H） | 1,333,370 | 2,661,210 |

外 rotation 的 x 分量用 odd-sine，y 分量用 odd-cosine，z 分量用 even-sine。完整旧数组按下表复制；不是把旧 482 列作为新 962 列的一个连续前缀。

| 分量 | 旧半开列区间 | 新半开列区间 | 保留列数 |
|---|---|---|---:|
| x odd-sine | [0,161) | [0,161) | 161 |
| y odd-cosine | [161,322) | [321,482) | 161 |
| z even-sine | [322,482) | [642,802) | 160 |

新 core 第 161–320 项、以及这三个区间以外的新 angular 槽，在包含时初始化为零，随后全部属于求解自由量。原 core 前 160 words、每一旧 rotation block 和最后 H word 在 Actions 内以完整字节比较核对。新源 `embed_outer_words` 还按实际解包再核各块及所有新增零槽，保两个不同布局的完整点摘要；它不宣称两个不同长度数组 byte-identical。

准确代数上，给高模态补零后当前支撑函数及其所有经典角导数不变；三个 Fourier 分量及所用角导数也不变。径向 shared-quintic 结点、系数槽意义和分片公式未改，所以同一旧完整系数在准确算术下给同一 current rotation 函数。这是有限表示的包含关系。实际浮点归约、当前 norm 及 normal 隐式选支仍要重读；本包不从零补 alone 宣称工作浮点场逐字相同，也不从系数相同推断已经验证全角唯一选支。选取相容 normal branch 时才可使用准确场的表示包含解释。

## 4. 固定参考与完整 normal / J / J*

新 base 从已刊完整 M320 base 派生，将真正的 Fejér reference、seed 和 layout 逐一硬绑定。它保全部原 `rotated_jets`、radial、angular、完整 field、残差、J/J*、正定范数及 domain 逻辑。当前 Fourier 表完整使用 M320，不能只加 shape 标签而保 M160 计算。固定参考图则始终以 160 个参数计算。

new normal 从实际 Fejér `1aa64d77...` 完整源派生，数学方法唯一必要变化是 `_chart` 的固定 `reference_freq` 读取。其余方法原字保，包括 32-stage normal chain、endpoint 原残差复读、原回溯、活动上游依赖、完整 implicit angular solves、全部六控制 frame 与原积分。

closure helper 将这个完整 `_chart` 函数加入明确 `DERIVED_METHOD_SOURCES`，不把 source 差异隐藏在宽松允许表中。原 plain detached / no dual / no transform 条件、由 bytes 拥有的不可写点、entry/exit 全词读回、每 key 的 immutable owner 绑定、全部 data/control angular words、每 stage 与最终 endpoint 强制原式复读和计数都保。解析 J3、解析六控制 frame、C1、detached / adjacent stage matrices 的完整数学体未改。新 packet registry 添加真实当前 normal/base/各 helper 整源身份，旧条目原样保留，不触发新 root 或将未算 order2 填成计算值。

当前 norm 会按 M320 完整自由布局重新构造。父 norm 的完整记录与 identity 只作为父来源保存；原 damping 参数 .01 在新 norm 下按本次明确算法参数使用，不声称继承了旧单位下的相同方向。原完整 J/J*、完整行约束 C、真正 Phi、full observation measure、谱参数和原 directions/maxiter/restoration/rays 的执行逻辑未删。

## 5. 真父、独立初点与同源 restart

完整真父入口先硬核实际父 driver `477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd`、reader `274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b`、binding `3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88`。父完整 110 roles 均在当前 128 roles 中以全 pair 保留，并逐文件核 SHA。原完整纯 reader 先读父报告；原 binding 先验证父完整模型；新 binding 独立验证新模型之后，才比较明确允许的 M 布局/source/policy 差异。

比较会逐一核完整 base、固定 reference/seed、Q 全部原 words、support/gamma、normal partition、observer、固定 scalar/profile/chart 和各自完整冻结点关系。只有已经验证的六个 working policies、真实源/模式字段、M 布局和对应 Q/calibration 的坐标身份允许归一；其余整个对象必须相等。不能借删除 model 字段来把旧 e711 或未知场混作 Fejér 父。

完整 final 的 13 个成员必须恰为：`schema`, `omega_jets`, `core`, `Hcap`, `mesh`, `fixed_parent_core`, `zero_closure_model_json`, `zero_closure_model_identity_sha256`, `base_so3_model_identity_sha256`, `fixed_scalar_metric_identity_sha256`, `endpoint_root_policy_json`, `working_integration_order`, `working_full_angles`。保存的全模型/策略、finite dtype/shape、固定三 core、原 mesh/parent_core、结构零和 whole final SHA 都核对。由这些成员重构的完整旧自由向量必须等父 latest metadata 与完整 final geometry 的实际同一点；然后才作零包含。

完整 final 的 source_report / checkpoint / driver 在读取前后再核字节。旧 field values、已求 roots、norm、Phi、accepted 标志、geometry 或证书不会借用为新点结果。父终态报告没有 complete final 时可用于源码支持的显式终态历史模式，但本次 complete-parent ready 不会把它降格当可用 final。

独立 ready 没有任何父 final 或 restart 参数，原参考 core/H 加全部 outer rotation 零值完整零扩张。它仍保五个实际 peer 的 run/source 声明：07 `45909290354/1`，08 `45929088658/1`，09 `45943410994/1`，10 `45972294636/1`，以及本 Fejér run12 `46011377225/1`。未知末点、未知 typed 首次发现顺序和未返证书不补为空。旧不同目标的 literal material addresses 继续按已声明的新确定性 mesh 重解释，不能称同物理 s；Fejér M160→M320 本身的 reference、mesh 和 current grid 则完整相同。

同源 M320 restart 保原 actual source/model/norm/point/full checkpoint 守卫，恢复原当前点及完整 typed annotations，不重置到参考初点，也不把粗父模式混作同源。

## 6. 历史与永久包络的实际消费

memory `complete_fixed_fejer_material_envelope_memory.py` 原字共享。真实父的完整 `history.sources` 逐 whole record 递归重读，原 walker 的 curvature/radius/protected 三角色和全部输入 payload 继续消费。父报告本身及全部新分离行都进入当前 memory；每条 family/location/partner/branch/sign、原首次发现 point、原 ordinal 和 source_report 来源保存，不截条数、不只搬 worst、不丢保护。

父全 typed rows 以原 `_separate` 语义加入；新场数值不沿用。其完整 grid/P0 包含关系按实际 carrier 与整组地址确认，不以“同 count”替集合。complete-parent 不带仅属于独立模式的 pending CLI token；旧义务通过实际父的整 `independent_branch_origin` / prior-transfer / inbound sources 保存。独立模式显式保五个未知 peer；后续有真正返回时仍需实际来源绑定合并。

## 7. 完整科学正文与纯读边界

新 driver 从 `    def save_report():` 起至 EOF 的完整 20,121 B，与原 Fejér driver 逐字相同，SHA256 为 `eb1d8813bd161358c451b06b47b570cdfdb9173b12f2661ee7ec37344dbf5254`。这保实际 first-field/statistics/full geometry、metric/restoration QP、line trials、row memory、acceptance、final readback 及所有错误保存的原执行正文；新增仅首 F 前的完整 layout/source/输入点选择与来源记录。

纯 reader 继续读全部原 source/model/seed/calibration/cache/normal snapshots/packet、完整同点行与 prefix、actual final 与 memory policy。新增 `frequency_refinement_binding` 独立核布局、当前 norm、实际初点及四个明确输入 mode。它没有把原 layout helper 的窄 `validate_report` 当作独立模式通用接口；真正调用的是完整新 binding 的 mode-aware validator，避免用只允许 coarse-final 的旧 helper 误拒真实独立初点。没有拆掉完整 reader 来规避大小限制。

自然返回报告保所有新增计数和来源。public summary 仍仅标量/摘要，不发矩阵、控制数组、final NPZ、packet 数组或 mesh；所有这些输出只留 runner。未自然返回时 progress 只是进度，不成为 M320 结果或完整科学证书。

## 8. 两份完整参数计划

| 模式 | 科学 argv 数 | 纯读 argv 数 | 科学 / 纯读标量 selectors | progress selectors | 两 step 紧凑大小 |
|---|---:|---:|---:|---:|---:|
| independent | 159 | 7 | 397 / 384 | 48 | 89,236 B |
| complete-parent | 146 | 7 | 397 / 384 | 48 | 88,620 B |

两份都从完整实际 Fejér ready `ab5c00086e21faaa5017ea469c4a63e7d389ecc3019b03a28e46b9daaa129578` / 92,380 B 派生。原 383 / 370 summary selector 每一项值保持；只加 14 个 M/layout 标量。原 48 progress selector 每项保持，不越 controller 的 48 项限制。完整 argv、output、cleanup 和文件路径均在各 ready，不以说明替参数。

共同实际预算仍为 angles2048、stage_block64、angle_block8、integration_order8、jet-sum 径向 .05/角24、threads4、damping .01、metric 1×16、restoration4×64/.01、15条 line trials、192 active rows、near-active32、root24/backtracks18/tolerance2e-12、normal32、seed全8/16quadrature及mean128/64scalar iterations，以及原完整谱、reach、安全、幅度和目标参数。M-only 增加 `--current-modes 320`；未缩任何科学预算。源中其它默认也仍是完整原 parser 的默认，不新添隐含缩减。

独立输出为 `{work}/fixed-fejer-frequency-M320-independent-first`；完整真父输出为 `{work}/fixed-fejer-frequency-M320-parent-first`。真父 report 路径为 `{work}/fixed-fejer-immutable-point-first/report.json`，checkpoint 为同目录 `final.npz`，同时以完整 manifest 输入。两 step 的启动 parent_bundle 均是已经实际存在的完整参考；它不是把未返 final 伪装为存在。若所需真父不存在，严格入口会诚实拒绝；独立计划不需要该未来文件。

所有 future M320 run/report/checkpoint/model/point 身份均为 null。ready 是完整待选参数，不表示 root 已排入队列或 Actions 已运行。若跨新 runner 使用，必须先由已刊两完整 maker/reference 步骤实际构造其本次输入并保完整来源；不能搬 run12 原 raw 到 Git/Artifact。

## 9. 完整源再生与实际做过的工作

所有源码只用完整公开父文本作精确字符串/整函数替换。完整 source reproducer 固定 24 份完整构造输入及原 110-role 表，生成全部 18 体并逐 whole SHA/bytes 比较；115 个声明替换按逆序恢复各完整父文本。这里已经实际用 JavaScript 作了该完整前向/反向文本构造，18/18 全字相等；没有导入 Python/NumPy/Torch，没有 AST/compile，也没有 F/J/root/科学 fixture。再生器是源保存能力，不是求解前新增一轮审查或数值 gate。

最后的已保护源码识别如下；其余每件完整 SHA/bytes/blob/路径在总表。

- driver `fullclosed_fixed_fejer_frequency_so3_qp.py`：96268 B，`fff956cc086c8f69c7de87c2d9117792b6b1d5e1de853e59a992fb67e04b4e51`，blob `557e4823a9dd5892699767a55515339ac02c88a1`。
- reader `read_fixed_fejer_frequency_so3_report.py`：98354 B，`b79c352d11b41de5384016f103c07db7abc2a41bf438ef92fe20b8a9b43e75bb`，blob `a84b93ef25817001ef99ec4ee953bf78e4d45658`。
- normal `fixed_fejer_frequency_normal_lift.py`：98459 B，`60769d4999af17f6dc904400e414e3f34ec1000bd84529ad168dca67f6889b5f`，blob `2fca2cd110ea329788e8cfe1d18984a5c8717cfc`。
- binding `fixed_fejer_frequency_source_binding.py`：35685 B，`caf16fbc87ef618ddae5ba42616d9bbe136beac6d32487224073ac6958c4d3c0`，blob `8a25d59f8a2fa2c818af8d3d17875d1ca5ae8a33`。
- transfer `transfer_fixed_fejer_frequency_memory.py`：84194 B，`1d35b2e7231ed5609e066e602f0f4722bb931b89bb9b3acea132cb45cc510bb8`，blob `66571893cb9f27a6b830b831e83052d5950059c0`。
- 完整 source reproducer `reproduce_fixed_fejer_frequency_sources.mjs`：64491 B，`4ad186519e8f70303ad1d4d9800edaadf1335f4f420da8605cb3023a3a9f00c8`，blob `752f0f98f2394c47373dd89bd842ae6722f3faac`。
- 完整 parameter reproducer `make_fixed_fejer_frequency_ready.mjs`：17977 B，`02771941588369e3fe6435bcc51fdcb88ab8fd1d436bf9b309af87ed4e1f6496`，blob `55149847e10bae4c77d3eb69685d2c7569d460ad`。
- independent ready：98814 B，`1941939829a67aedf328277af9fe3446d711e2d9f502eae2cb5ca8a84d0ef149`，blob `3111a25616f1e28b1f1e0d521c1dae036acdc68d`。
- complete-parent ready：98966 B，`900d195f35884aada85925e51df6372f8651f123be7cb37f66ae645140c98b83`，blob `e10fce334aea173097ee2d79726f49dd2c7d3109`。

源再生器使用 `--source-directory` 指向本题 `scripts/resume_20261126` 的完整已刊父源目录，`--generated-directory` 指向另一不存在的新目录。参数再生器对应使用 `--parameter-directory` 指向完整 computations 目录。这两个工具不执行任何生成的 Python；root 是否为发布复原它们不构成实际求解前提。

## 10. 保留的未知项

M320 当前没有科学返回。没有新的 metric/Gram 残差、reach、幅度、δhold、δE、root-error 或连续全域费用数值。旧 run10 已取消且科学5没有自然返回，不能提供本目标父；当前 run12 仍待真实自然返回。独立 M320 与 M160 的一次有限空间包含说明不能替代准确 normal 支、完整误差费用、连续全域/全 t 几何、握持和最终任务完成标准。

本包让合法同目标精化可以实际执行，并保留完整证据归属。求解后的数值差异及误差解释须由各自真实完整场、同一固定目标和明确 norm/观测规则给出；本说明不预报速度、收敛或成功。
