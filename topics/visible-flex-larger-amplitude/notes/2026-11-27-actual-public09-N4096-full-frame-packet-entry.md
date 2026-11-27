# 实际 run09 固定目标上的 N4096、完整解析 frame/J3 与 packet 观察入口（revision2）

这是完整源码、来源关系、参数与连续责任说明。N4096 新入口尚未科学执行。实际 run09 原 `e3cb0f5a...` 首次入口返回早退，仅有 command 元数据、没有科学 report。随后原 child 日志已完整读回：GeometryScreen 读取不存在的 `all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained`，而实际解析 J3 家族的 adjacent definition 提供 `all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained=True`，因此来源守卫拒绝。原科学 log 为6387字节，whole SHA `33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de`；pure 因无 report 而失败，不能归因为求根或物理场失败。

本 revision2 独立绑定修复后的完整父四源，修正派生几何的同一键名，并重新闭合来源 pins、严格 terminal/final 父与完整参数。原候选31个全文blob保持不动；没有改写旧失败来源、伪造原 e3cb report，或把13个未变 runtime 数学体重称新算法。所有本地操作仅完整文本、stdlib AST/compile、source-only 再生及参数打印；没有导入生成的 NumPy/Torch/SciPy 科学模块，没有 F、J、root、求积或 fixture。

## 1. 此次真正冻结的输入

本入口以实际 run09 `45943410994/1` 已返回的完整目标为准。目标 schema 为 `independently-frozen-actual-public-run09-scalar-and-material-chart-v1`，canonical identity 为 `7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a`。原完整参考模型 identity 为 `d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75`。实际完整 binding 文件的 whole SHA 为 `2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d`；其 430906 字节完整文件只在 runner 读取，不把摘要替代全文验证。

实际目标由完整 `actual_public_reference_input_binding.py`（`306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a`）和 `freeze_run09_public_reference_and_restore_run05_carrier.py`（`9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18`）建立。它包含完整原 public 返回证据、六个真实输入文件、整个参考模型和 bundle、完整 scalar 参数/定义、全部 923 个准确 affine 节点、全部 160 个 canonical fixed-chart 字以及完整 old/current carrier。

当前 fixed-chart 全数组 SHA 为 `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e`，其实际字摘要与历史 chart 相等；因此本目标原定义的 `same_original_fixed_chart=true` 被完整保留。同时 `same_mathematical_g_claimed=false` 也完整保留。未声称相等不是已证明不等，更不能只凭 chart 摘要相等推完整 scalar/参考/数值场相等。新 N 入口所证明的固定目标不变，是相对于这个完整已冻结 run09 目标逐对象相等，不是把另一个 run08 的 `7c4c9b...` 输入改标签。

六个输入角色为当前 warm、node report、scalar input、carrier、preparation report、reference bundle。原完整 public09 pure binding 会核实际 run/attempt/step、文件 path/bytes/SHA、完整目标 canonical、真实参考定义和 caller 传入的五个实际路径；warm 由完整 preparation/目标所绑定。原 target validator 在 N 适配中不作删改。每次纯读仍重读这些真实文件，既不接受自报布尔，也不因维数相同接受另一次 warm/reference。

## 2. 唯一新的数值参数与模型分层

此次只改当前观察层 full N：2048 → 4096。固定 reference 仍为 N2048、M160、J923，原固定材料图 $\Theta_0$、全部 scalar 定义/准确节点/支持、完整 seed 输入与均值定义、每胞八个 outer radial Gauss 节点、18 个 literal Q 字、两 bubble、gamma 和 32 个共同 normal 分段都保留。

| 项目 | 固定参考 | 当前观察/外场 |
|---|---:|---:|
| full N | 2048 | 4096 |
| quarter literal angles | 513 | 1025 |
| M / core Fourier layout | 160 | 160 |
| J / radial mesh | 923 | 923 |
| 原全部外自由变量 | 同一固定初值来源 | 所有 core、三 omega 通道、H 保留 |
| outer radial Gauss order | 同一径向定义 | 8 |
| normal partition | 准确共同 $i/32$ | 全部 32 stages |

目标无关的三份已锁完整 source——observer、N 分层 base、对应 Q binder——逐字复用。真正绑定 run09 的 memory、source relation、history transfer、driver、reader 则从实际 run09 完整来源派生。generic source 可复用，不意味着可以省略 run09 的完整输入验证。

原 base 33 个类方法中，除 constructor 和 domain 的 reference/current N 分离外其余 31 个 AST 相同。domain 原正性读取尺寸用冻结 `reference_full_N`，避免 `full_N` 含义变化暗改另一项筛查。当前 N 不进入固定 seed 模型。全部 free mask、packing/unpacking、三频道 omega、径向 Hermite、width、J/J*、H 槽不变。

## 3. 完整角载体与准确平均关系

令原实际 quarter 字为 $\phi_j$，$0\le j\le512$。新角数组在每个偶数位置直接复制原字：

$$
\widetilde\phi_{2j}=\phi_j,
\qquad
\widetilde\phi_{2j+1}=\operatorname{binary64}\!\left(\frac{\pi(2j+1)}{2048}\right).
$$

旧字来源仍按原 $\operatorname{binary64}(\pi j/1024)$ 的完整读取合同，不能用另一种计算次序重算偶数列再宣称逐位保留。完整两个 hex 列表、array SHA、source 与 definition canonical 都保存并重核。当前 multiplicity 为 $(2,4,\ldots,4,2)$，准确整数和 4096；偶数列权质量 2048，奇数列权质量也为 2048。没有角样本 cap 或误差选择性删角。

对同一当前 raw Gram buffer 与同一损失参数，准确算术给出

$$
\langle L\rangle_{4096}
=\frac12\langle L\rangle_{\rm old\ even}
+\frac12\langle L\rangle_{\rm new\ odd}.
$$

实现沿完整原径向权读取 all/even/odd 三组统计，并保存实际工作 half-sum 差。它不再调用 F，不拿父 report 的 Phi 代替当前偶数列，也不把浮点求和差默认为零。对 nonlinear spectral mean 的各中间量和原始完整统计分别按真实定义读取；不能无条件把非线性后处理的最终 Phi 当线性平均。

因此有限观察目标发生变化，旧 Phi 不能作为当前 baseline。这个入口重新读当前全部原始 Gram、相同 $p,\epsilon,\mu$ 与范数下的初始目标，完整正权行照常进入 QP。新旧有限目标的归因用同一新场的共同偶数列；不是把另一批形下的旧浮点场当同字。此角网格关系是 [R679](../results/R679-dyadic-angular-refinement-and-common-grid-attribution.md) 的明确实际来源实现，不重复登记一般精化结论。

## 4. 完整 analytic frame/J3 与 implicit 链

当前派生父 normal 是最终 `3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc`，不是更早只有 analytic J3 的 normal。新源保留父完整解析六控制 frame、完整 working Rodrigues 微分的 J3、C1、detached stage matrices、adjacent frame 后置 J6/J9、reference centering 与 immutable packet。

新 normal 与父 normal 的所有原函数和类方法 AST 相同；source/schema/base/依赖 identity 为明确新完整常量。其余七个核心 helper 的完整函数/类数学体也同样保留。各 stage 的原 residual、domain、Armijo、Newton、角一/二阶 solve、previous/frame/target 全上游参数图、完整隐式转置都不删。两角 jet 的外参数一次 J/J* 仍含完整 frame 的高阶链，不能由前向值零推其导数零。

GeometryScreen 的当前 C1 guard 明确核本包真正 `angular_refined_public_reference_frame_c1.py`，不存在先前另一个未执行候选中继承历史 ba3d 的错误。严格来源关系覆盖 constructor globals、实际 codefile、whole model、helper definition 与 cal/endpoint 循环来源；没有为精化放宽。

同一 constructor 的 adjacent guard 现在严格读取实际 selected-J3 key；完整构造器逐字核它恰出现一次且实际 adjacent.definition 的该项为 literal True，并拒绝旧 original-key 残留。这里保留的是当前已明确选择的解析 J3 与完整 stages/角solve，不宣称从未更换过历史 AD Newton J3。

准确模型可包含同一固定参考/同自由点的场，需要选取同一个完整 implicit 分支。N 增加改变实际读取顺序、批形和缓存安排，不能自动推出工作 F 字逐位相同，也不能从每角数值根推出完整全角分支。连续根、逆矩阵、AD/积分/舍入费用仍欠；本入口未付款。

## 5. P0、oldG/currentG、保护与全部 typed 行

原 complete memory `2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb` 的四个函数 `validate_public_binding`、`_validate_independent_target_binding`、`read_carrier`、`_original_p0` 在新 N memory 中全 AST 相同。`MaterialEnvelope` 除 constructor 新增真实观察载体外原成员 AST 相同。

完整原 P0 的十一份来源、whole dc5 carrier `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`、当前 carrier、当前 preparation 的全部 new_locations、caller 的每个 manifest 都保留。新永久非线性责任为全部已绑定旧/当前径向地址并集乘以全部 1025 当前角，再并全部显式地址。旧 513 literal 角全在偶数列，所以旧两 G 无遗漏。若旧/current 径向字有额外层，原 complete extra-layer 读取仍保，不用数量相等替代逐字比较。

每份含 stage/angle 索引的原历史必须按其自身声明的 N 解析为 literal cell/u/phi 后才进入新并集。原 prepared/P0 使用 N2048；新 same-source restart 使用 N4096。缺原 N 或含未支持 N 的索引历史诚实拒绝。新 geometry 的全部 scan、world dp、两 principal curvature、正负 reach、全部幅度、原 192-prefix、append 行和 line search 身体逐 AST 保留。原完整 selector `729910dc...` 已按实际 `q.N`/shape 工作，因此其 source 不改。

原 prefix 行、amplitude 行和 envelope 行的三项计数恒等式、真实 row-cache 字节、完整列数和各摘要均保持。新增近活动 cap32 只约束当轮候选；真实拒绝产生的 typed separation 永久 append-only、没有该 cap。partial scan 保它自己实际 point/覆盖，不把缺数据补成 complete。

## 6. 实际 N2048 父的完整转移

严格 N 父族是明确修复后的完整 `ff5444af...` driver / `aee22caf...` reader / `3d8d3ed8...` normal / `25181333...` memory。它必须先被原完整 reader 读通，whole snapshot、model、target、六文件、carrier、terminal scope 和所有源都真实一致。旧 cc0a、95559、0dfb 保作明确未知 peer 来源登记；不能借它们有相似形状或 chart 就作实际 run09 同目标完整父。

新 `compatible_legacy_model` 先用原完整 `15f6393a...` pure binding 验证旧 normal/helper/policy 关系，再用新 binding 验新关系。只规范化明列 source/schema、current observer 三字段、五个已单独完整验证的 frame/matrix 工作策略和依赖 base identity 的 Q/calibration 字段。其余完整 base、scalar/profile、准确 mesh、fixed chart/seed、全部 Q 字、gamma、tau、free layout 都逐对象相等。每个 Q/calibration 先验证自己的原 identity，再规范化，不拿同形错误 base 通过。

父 `history.sources` 全递归文件闭包逐个 path/bytes/SHA 读取，不截祖先。准备文件核整个 reference_definition；原 N2048 的索引逐份解析，完整 curvature/radius/protected 三个角色集须包含在新 memory。所有 carrier 成员、完整 radial union/extra、旧角摘要和完整目标对象都作新旧包含核。

每个 typed 行按原 ordinal 无 cap 转入，完整原 row、原第一次发现 source point、report/model/driver 与已有祖先 provenance 保留。原 `material_envelope_transfer` 整体保存；纯读会重新读原完整文件而非相信迁移里的几个 true。迁移不把旧 physical g 或 feasible 当新结果，也不声称重建未知保护排序。

## 7. 全部末点变量、冻结参考与三种参数模式

若有真实 complete final，必须用成对 seed-report/seed-checkpoint，且报告已被上述严格迁移完整读入。原 reader 必须验证 final 全文件。全部 13 个 NPZ 成员、完整 old model/base identity、原工作 full N2048、radial order8、policy 与 scalar identity 均核。原 checkpoint 的 base identity 与旧父比较，不与新 N4096 base 误比较。

五个物理数组 `core,omega_jets,Hcap,mesh,fixed_parent_core` 的 finite/dtype/shape 和字序全核；omega 仍为原 $(J,3,n)$ SO3 三频道，按原全部 radial_free mask packing。新 q.unpack 必须逐字重建全 core、全部 omega 和 H。冻结 `base.initial()`、reference point、seed/model/Q 都保持原字；只是 current outer initial 取旧完整自由点。

参数计划分三种完整模式：

1. `independent`：明确取原参考自由点；原全部 P0/twoG 与未读 peer 责任保留，不把原 e3cb 无 report 当终态空历史，也不预填修复后 ff544 的返回。
2. `terminal`：真实完整父 terminal report 的全部地址/typed 迁移，仍取固定原参考自由点；适用于具有正式 initial-field-failure report、无 final 的真实父。只有 command 元数据不满足该 terminal 合同。
3. `final`：真实 complete 父 report+final，经 13 成员完整转移后取全部外变量作为新初点；新 Phi/root/sixjet/geometry/norm 必须全部重读。

same-source restart 另由原完整 guard 保。三个计划都没有填未来父 report/final 的 SHA，不保证某个指定路径将来产生文件。实际原 e3cb 早退无 report，不满足两严格计划。修复后的 ff544 只有在真实 report/final 存在并由其独立 aee22 pure 完整核过后，才能分别使用 terminal/final 计划。源码和完整独立计划不以该未来文件为前置条件；不预填它的值或 SHA。

run07 在 05:02:15 被观察为 completed/cancelled，API updated_at 为 05:00:28。观察时刻不是科学子进程结束时刻，其 child 时刻/原因未知。旧 compact 的 step4 running 不是最终科学返回。`pending` 指未付实际报告/地址/typed 来源责任，并不声称工作流仍活着。取消和首场未返不能推成无新增点。

## 8. 全科学循环、数据包与实际参数

新 driver 从实际 run09 完整修复源 ff544 派生。该父与原 e3cb 仅几何 source/path pin 不同，其科学后缀逐字保留。`save_report()` 至 EOF 的完整科学后缀，只在原同 raw buffer 的统计中插入 observer attribution 两行；删去这两行后逐字回原后缀，whole SHA 为 `d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376`。原 Phase I、正权全部 Gram 行、完整 C、QP/J/J*、line trials、真实 descent/domain/全 geometry、永久 memory、唯一 accepted 出口都保留。

packet 原两处只读 hook 仍在同位置。helper 的原 registry 保留并添加真正 N4096 normal/base/calibration/analytic-frame/J3/adjacent 完整 source；所有原函数/类方法保留。只复制已存在的 current-cache 数据，不触发 F/J/root 或升级，outer point 与 cache point 分开；I/O 失败不用旧包冒成功。

数值参数只有 `--angles 2048 → 4096`。原 1×16 metric、4×64 restoration、mu .01、15 trials、192-prefix、near-active32、全 norm、spectral p4/epsilon .001/scale .05、reach .03×.992、全部幅度预算均保。normal32、outer8、seed radial8、profile16、boundary1/16、delta1/128、root/mean全部迭代与容差原值保。新的 source/path/显式父模式另列，任何原 scalar summary selector不删。

每份完整计划保全部 science argv 与7个 pure argv，science/pure summary 的333/317个原标量 selector全部保留，再新增 N/共同buffer标量。 参数中的75个运行来源以 `[path, whole_SHA256]` 二元组逐项完整内联；原失败完整证据用已锁父ready的whole path/bytes/SHA及准确字段路径引用，关键原log/键错配另内联。仅去掉重复的历史证据正文，不删任何数值参数、地址输入、source角色或summary selector。整个两步队列小于95000字节；每份完整参数文件小于100000字节。纯读 controller parent 始终为真实原 reference，所以没有新 final 不阻断对已存在初失败 report 的读取。只清新outdir rows-*；固定reference cache、packet/raw保runner，不写Git。

## 9. 全源复现与验证范围

18个 runtime：3个已刊generic完整复用、15个实际public09家族完整派生；9个完整构造源包含7个构造/附加正文、总reproducer和参数构造器。总reproducer读取20个完整parent-source，逐次生成全部18体，核75个完整runtime roles及全部bytes/SHA；逐体AST/compile、重复literal key/keyword、尾空白与单源<100000字节。没有导入生成的科学模块。

```sh
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_public_reference_angular_refined_sources.py \
  --topic-directory topics/visible-flex-larger-amplitude \
  --construction-directory topics/visible-flex-larger-amplitude/scripts/resume_20261126 \
  --output-directory /tmp/public09-N4096-complete-source
```

对已刊完整体比较可将 output-directory 指向实际 scripts 目录并加 `--verify-existing`。参数构造器从 whole `2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f`、93108字节的修复后 `run09-public-reference-analytic-frame-v2-complete-ready.json` 读取全部参数，不复制摘要当全参数。该完整父又绑定原 d0ffe2cc/96250 全参数，全部145/7 argv 与333/317 selectors保持。它保全部真实 input/public-output元数据及未读 peer责任，不预填修复后 ff544 的科学返回。

本地已经完成 revision2 全18体 source replay 和75角色检查；没有执行科学运行。完整修复后的父4体已逐字逆替核：geometry仅 original→selected 这一键；driver仅 geometry path/pin；launcher/pure仅 driver path/pin。新 N 的13个 runtime 与原 N 候选逐字相同，另5体仅该必要守卫、实际新父pair和依赖来源闭合。原31个候选远端未引用blobs保为不变历史。

## 10. 未付连续范围与后继

此包未证明 normal 全角存在、同支唯一性、每stage逆矩阵界、积分/三角/AD/舍入误差、全径向/全角几何或 full-t reach。N4096有限通过不等于全域证书；SO3 exp 与 implicit root 也不因原 M160 而自动有限带宽。R714/R715 的误差职责、实际参考moment/总均值/节点费用以及packet真实含量仍须同场消费。

径向精化尚欠固定 J0/current J 的真实拆分、所有新准确 affine query、完整 quintic jet restriction/injection、新旧积分路径与全部历史地址/parent bytes迁移。不能把新局部u经舍入后送进旧cell/u并称同准确节点。M320也为另一明确完整布局族；本包仍M160，组合必须独立闭合actual source/target/transfer，不把观察N精化叫径向或频率精化。

## 11. 完整运行体 revision2 身份

下表不替代完整源码。全部未科学执行；完整源/参数、原候选及真实失败均分别保存。

| 完整文件 | Bytes | SHA256 |
|---|---:|---|
| `angular_observation_refinement.py` | 11045 | `8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3` |
| `angular_refined_public_reference_adjacent_matrices.py` | 36761 | `5d8bc302e0bbbb48de1c47b7c7470a6904cc09c9dcda84a71c5f93455d8e9602` |
| `angular_refined_public_reference_calibration.py` | 11886 | `dffb102d4daed36735a34f69e920c10fc41f5e8fb2aa606a0d86acda9cf6eeb9` |
| `angular_refined_public_reference_frame_c1.py` | 35894 | `65b3c988178c766c3715cd08c8200b93816067e316cd260ee7da254b890fada4` |
| `angular_refined_public_reference_history_transfer.py` | 75765 | `bb47e4dcbaf4ae159d6ad04b5d1715a0093b934ba7b9896b4820f474febb78ce` |
| `angular_refined_public_reference_memory.py` | 52209 | `74bd35b283434fca103b62f6dbaf93dc3a710fd7a962f239b67c6c3916aca385` |
| `angular_refined_public_reference_normal_frame.py` | 33669 | `a3afa4762a0573a8eb3de026d56a0922977c6b5359b7567f322fa4c866f51aff` |
| `angular_refined_public_reference_source_binding.py` | 28014 | `0e00f37b2a504b05d5d7b5535e2bf06085f9715bd7f0992df2ad4589af85e140` |
| `angular_refined_public_reference_stage_jacobian.py` | 24225 | `7257ff8cb625ada848a41b1ce0d37bf88a0e095196dfb7ab072f210c3da030c4` |
| `angular_refined_public_reference_stage_matrices.py` | 47775 | `29c20d6831f15abac6b6701d4b471d75154b915c6739d9a0df84c79438c2928b` |
| `angular_refined_smooth_triangle_literal_zero_moment_input.py` | 30940 | `a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d` |
| `fullclosed_angular_refined_public_reference_so3_qp.py` | 86720 | `3ff2a0bfd2c49847c0d17514842ee9542fccca050f0a054c4ee75a24cf33a9c5` |
| `immutable_angular_refined_public_reference_root_packets.py` | 69730 | `ac34e4a1ded37726545fc743ca002706a8f40a1d5e3cf153472b9429559644cb` |
| `launch_angular_refined_public_reference_so3_actions.py` | 21571 | `a4f36f7f89adc5b487bdaca683bec3518df5aa22cc18faf075165f93103c19da` |
| `read_angular_refined_public_reference_so3_report.py` | 97289 | `44053d738dd3b08525130487c2e2eb33c4839adc17bfb4ec294d16155e6523bb` |
| `so3_angular_refined_public_reference_envelope_geometry.py` | 68856 | `a243377b5dccfdb6787d0053d6e835df8ca46697dddcd26a756f5b51559bc24b` |
| `so3_angular_refined_public_reference_normal_lift.py` | 96515 | `ceaaab5f05c9faaddaff8174be9f97e9aa5b0936b9cf586990877433a9cce100` |
| `so3_angular_refined_smooth_triangle_meridian_operator.py` | 41592 | `1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529` |

## 12. 本次严格最小修复与旧候选边界

父四件采用独立 `_v2.py` 文件：geometry `e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13`，driver `ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5`，launcher `c1888457b67c85185aebe6c91d2bd4942ccc2d2074407e17f7f54a2825927d23`，pure `aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32`。旧 ef121/e3cb/474 全部保留，它们不是新来源的别名。

N4096 当前18体的变化恰5件：geometry必要 key；history_transfer 严格父 driver/reader与实际reader文件名；driver对应runtime/parent pins；launcher/pure对应新driver pin。全部13个数学/目标/数据核，包括normal、解析frame/J3、C1、stage/adjacent矩阵、packet、observer、base、Q binder、memory与source binding均原字不变。7个源码构造/附加正文中只有必要3件依赖锁更新，另总reproducer、参数构造器、全note/readies同步真身份；完整reproducer核新20父体/75运行role。

该修复不证明科学成功、存在性、有限目标下降、性能改善或连续误差闭合。它闭合已经真实定位的 source guard API 错配；下一次实际运行仍须按它自己的真实返回归因。

## 13. Root独立完整复核与执行环境边界

2026-11-27 07:35:26 UTC，root在公开连接器重新读取全部31个完整交付blob，逐体核整SHA/字节数；再完整读取60个既有父源，核driver的全部75个来源角色。读取全部9个构造/附加/参数源及本说明，未执行任何科学模块。三份完整ready相对真正2ea114父逐数组检查：原145词science参数除N与明列新目录/父模式外无变；independent/terminal/final分别149/138/142词，pure均7词。全部原333/317个selector逐键保留，新349/327项；outputs与cleanup只换新目录。所有75个内联源path/SHA与实际完整源码匹配。

root还直接对两份完整driver，从save_report至EOF剔除唯一同buffer归因两行后逐字比较，原19574字节及整SHA d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376完全相同。六输入/whole target、N2048固定参考、13成员完整转移、全typed/全部祖先读取的构造代码均按完整正文核查。

construction已经实际完成的18体source-only再生、AST/compile及75角色验证保留；root原本安排的第二轮本地再生因执行环境失联没有发生，**不把远端整SHA/文本检查称为一次新的本机再生或科学运行**。失联和最后真实pull完整事实见[第30次note§5](2026-11-27-legacy-condensed-generated-manifests-retention-30.md)。此次云核head `7391e43a5b083200026a7e1a6afff6cb790986ab` 的双README整SHA无变；云API不冒git pull，恢复后立即真实拉取。

三完整计划作为可复现入口发布，本次没有把尚未返回的09科学/pure步骤移出活动队列，没有提交或假造未来父report/final，也没有声称实际N精化或连续证书已经返回。继续当前完整场与后续真正精化。
