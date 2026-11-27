# 完整 M160→M320 同目标入口：云端重建 v2、实际父场注入与完整历史

日期：2026-11-27。本文是独立完整源交付说明，**没有执行任何科学场、根、Jacobian、积分或区间算例**。代码构造和所有实际数值工作仍按课题规定在 public Actions 执行。

## 1. 本次版本和已完成范围

本次交付十三份完整科学/验证/入口源码（含完整 pure reader），以及三个完整 stdlib 再生器。全部源码均小于 100,000 bytes，并已分别保存到仓库中的**未引用 Git blob**；这不创建 commit、branch 或 ref。root 是唯一发布者。

第一版 M320 工作稿在 scratch 中曾完成并接受静态接口审读；环境失联时，它的十二份全文和再生器没有可靠的远端副本。不能从既有 SHA 推断全文已经保存。本次明确作为 **v2 新版本**，从原来已公开的完整源和已登记的接口要求重新纯文本派生；不声称逐字恢复那份失联工作稿，也不混用旧版 d43/e244 的来源。

原始父源码快照为 `291adcd2b2f4de1dac4c7118dbce69b471dc5813`。当前这份 v2 只注册两组完整 M160 科学来源：

- cc0a driver / 104e 完整纯 reader / a62c endpoint；
- 91c driver / c0cc 完整纯 reader / d5da endpoint。

后来独立修复的 compatible-current run08 家族（包括新的 5c5c driver、1e2ca9 memory、6cc restorer）**不在本次注册表内**。如果采用该真实父场，必须再明确派生新的完整来源合同，不能把它改标成 91c 或 c79/5f22。

没有“必须等某一个指定 run”的数学要求。只要真实完整父报告属于上述明确来源，并且通过自己的完整 reader、完整返回 checkpoint 和全部同输入约束，即可成为本入口的实际父。尚未返回的报告、仅有 initial-root failure 的报告或没有完整 final 的字段不能充当实际父场。

## 2. 唯一空间改变与不变的数学输入

原固定参考为 $M_0=160$、$J=923$，完整角观察为 $N=2048$。新的当前自由空间是 $M'=320$。以下保持完整原对象：

1. 4e 的准确 R690 scalar/profile 定义和完整参考模型；
2. 原材料图 $\theta_0$、原参考 core 和原参考 H；
3. R711 平滑三角 supported seed 的完整定义、mean kernel、所有 working 参数；
4. 原径向 mesh、全部 shared quintic 自由径向 jet、原积分规则和观察载体；
5. 十八个 literal Q 参数字、两个 bubble、gamma 和共同 32 段 normal partition；
6. 完整外参数 J/J*、全部 upstream normal-frame 与 zero-target 支路；
7. 所有既有 P0、旧/当前完整 G、三种位置角色、已知保护、全部 typed separation rows；
8. 原完整真实 Gram、curvature、radius、两个 witness 符号、cap/H 行以及非线性筛选。

原 reference problem 的 M 从不改成 320。新 base 同时保存 `reference_M=160` 与 `current_M=320`，把冻结参考频率和当前 core/omega 频率分开。原 reference provider、原 scalar reader、原 supported seed 的 M160 守卫保持原字。

本次不是径向精化，也不是角观察或积分精化。原 fixed scalar g 不从当前场重算；没有 moving mean 投影，旧原始 Gram 各行仍完整存在。

## 3. 完整零嵌入，不把三组旋转块当成三个等长块

原自由点按 free core、每个 free radial slot 的三组 omega、最后 H 排列。原 core 自由部分有 157 个词，新 core 自由部分有 317 个词。原三组旋转频率是

$$
\omega_x=\sum_{m=0}^{M}\omega^x_m\sin((2m+1)\phi),\qquad
\omega_y=\sum_{m=0}^{M}\omega^y_m\cos((2m+1)\phi),\qquad
\omega_z=\sum_{m=1}^{M}\omega^z_m\sin(2m\phi).
$$

所以原共有 $161+161+160=482$ 列，新共有 $321+321+320=962$ 列。对每个原径向自由槽，实际注入为：

| 组 | 原完整列 | 新完整列 | 原词数 |
|---|---|---|---:|
| x，odd sine | [0,161) | [0,161) | 161 |
| y，odd cosine | [161,322) | [321,482) | 161 |
| z，even sine | [322,482) | [642,802) | 160 |

原 157 个 free-core 词复制到新 free-core 前缀。H 复制到新完整点的最后一槽。其余新 core 和三组新 omega 槽显式为零。原固定前三 core 槽、全部结构性径向零槽、mesh 与固定 parent-core 数组也逐项核对。

`embed_outer_words` 只在 Actions 中读实际数组；它验证 finite native binary64、完整尺寸、每组字节相等、新增槽零以及 H 的准确 hex。它保存旧/新完整点 digest、三组实际 block digest、core 前缀 digest 和 H hex。**不同长度的旧/新完整数组不声称 byte-identical。**

actual checkpoint 必须有原 normal 的十三个完整成员，不能悄悄忽略另一个缓存或 hidden state。原 omega 数组要求 $923\times3\times482$，core 与 fixed parent core 各 160，mesh 923。原 checkpoint 的完整 model JSON、identity、base identity、fixed scalar identity、root policy、working integration order/full angles 均按原父报告核对。

之后，新 q.unpack 必须重建同一份旧 core 前缀、三个正确偏移的完整 omega 子块和 H；并再次检查所有新槽零。只有这一完整实际点才进入新的首次物理读取。

## 4. 准确包含与工作重读是两项不同责任

在准确 shared-quintic/Fourier 表示里，零嵌入保留原 $\Gamma_c$ 和 $\omega$ 函数。冻结的材料图、参考 seed、Q、gamma、共同 normal 方程未变。因此在对应的同一准确 implicit branch 上，原 trial function 属于新的完整空间。

这种准确包含不保证：

- 新布局下 ordinary floating evaluation 与旧场逐位相等；
- 新 source 的迭代在没有 branch 证据时必选同一数值根；
- 原 root、matrix、cache 或 field value 可以复制为新字段；
- 原 Gram/Phi、finite geometry 或 continuous certificate 已经为新点支付。

完整原场与新场的导数/转置关系按已刊同 g 精化设计的作用域陈述：raw Euclidean 或相应明确 isometric coordinates 下才可直接写相应嵌入转置公式。不能把带不同工作白化/权重的转置未经说明识别。

本次运行入口在报告内分列：

- 原父实际 complete model、norm、point、checkpoint 和完整 source；
- 实际零嵌入记录；
- 新 complete model、new norm identity 和新 initial point；
- 新 source 真正返回的 initial roots/Gram/geometry。

所有原 normal 32 段、Newton/J3、角 jet solve、detached J6/J9 producer、C1 graph 支路和完整物理六 jet 都保留。没有因为初点包含关系删除 stage，也没有把 raw closure defect 或 centered root residual 强置为零。

## 5. 冻结材料图与校准在新 current layout 中的准确区别

新 base 的当前 core/Fourier 频率为 320；固定材料图及原 parent core 仍为 160。base._core_and_cap 的冻结 $\theta_0,\rho_0,\rho'_0$ 用 reference frequencies；其当前逆图支路用 current frequencies。normal._chart 同样只使用 reference frequencies。

新 calibration 的完整固定点是“原参考 core/H 与 omega=0 的新布局零嵌入”。它有新的数组 digest，因为尺寸改变；但原物理 core/H/seed 不变。校准对象从同一完整新 base、同一 complete endpoint 的 core/cap 与 total 方法建立，保留完整 method codefile/source/schema 守卫。

校准定义明确保存 reference M、current M、新坐标布局说明及“不声称旧/新完整点字节相同”。baseline 既不取当前 coarse final，也不随外层方向重选。原 reference core/H 和 supported seed 对象完整不变。

当前物理六 jet 保留 R715 完整 raw lift。working radial Gram 仍实际读取，不能因为准确单位 meridian 模型而声明工作 $F_s$ 恒为单位。后续 continuous/root/quad 费用仍须按当前新表示和同场身份独立支付。

## 6. 父场来源、同输入与完整模型比较

新 transfer 不以一个任意 M160 JSON 或外部自报布尔量作为父证据。它先由 source registry 选择父场自己的完整 pure reader，并读同一份完整实际报告快照。完整 reader SHA、science source、schema、whole report bytes 和 returned final bundle 必须一致；读取结束再核文件未改变。

父和新的当前入口要求同一份五个完整输入：

- reference bundle；
- observation carrier；
- exact symbolic node report；
- scalar input；
- independent preparation report。

完整 fixed scalar identity、J/N、原 observation measure 的 positive legacy/Gauss 权重政策、spectral p/epsilon/scale、reach ratio、safety 与 amplitude budgets 保持。reach ratio 来自真实 `final_geometry.source_binding.reach_ratio`，不是一个不存在的顶层字段。norm kind、radial length、angular transition 必须相同；旧 norm 的完整 canonical identity 仍验证，但不被重新标签为新 norm。

模型比较只规范化预先声明的差别：

1. current M、完整新 layout/source/flags；
2. 实际新 source/schema；
3. 与新 base identity 和新的冻结 reference-point digest 相连的 Q/centering identity；
4. 明确新来源的、保留完整方程的 C1/detached/adjacent working producer。

完整旧/新 base 的所有其余对象逐项相等。原 seed、reference model、scalar profile、mesh、chart、radius、原固定 core 槽、十八 Q 词、support、gamma、root numerical policy、32 个准确 stage 节点及其 carrier 和完整 selection 描述不得变化。未知新字段不会被普遍删除或忽略。

新 complete model 因 source/current-layout 身份改变而重新 canonical。没有把新 model 或 Q input definition伪装成父场的旧 identity。

## 7. P0、G、保护与 typed memory 的完整转移

当前入口使用父报告真正绑定的 c79 或 5f22 原 consumer，保留这两个完整 loader、same-source restore、metadata 和 separation 方法原字。原 history walker 仍是完整 4d9。

父实际 whole report 加入完整 manifests。原 walker 按实际相同 carrier 解析历史 grid 地址；三种完整角色分别核成新 explicit union 的子集。旧/当前的完整 material grid union 和 origin-carrier identity 必须匹配，不能由相同 argv 猜相同节点。

每条 typed row 保留 family、location、partner、branch、sign、原 first-discovery point 和完整来源。没有 count cap、截尾、数值旧行复用或悄悄撤销保护。新 source_bound origins 只说明地址/类型来源，不说明旧值为新场的值。所有新行仍从新场完整 point VJP 和当前坐标转置重新建立。

先前报告中的 pending parallel obligations 单独完整保存，包括父 transfer identity、原 independent-branch provenance 和先前继承的 obligations。没有可用实际报告时，不声称 typed priority/数值字段已恢复。后续实际报告仍须按完整来源合并；M 变化不取消它。

同一 fine source 的 restart 走原完整 memory restore，保持已保存的 uncapped typed prefix 和全部历史。fine entry 不允许再伪装 independent branch 或未绑定另一个 seed。

## 8. 新完整入口与 restart 合同

新 launcher 和 driver 的 complete parse_args 逐字一致，仅 launcher 另有 install-torch、print-command 两个非科学控制旗标。新参数：

- `--current-modes 320`；
- 首次：`--frequency-parent-report` 与 `--frequency-parent-checkpoint` 成对；
- 后继：本 complete M320 source 自己的 `--restart-report` 与 `--restart-checkpoint` 成对。

首次实际 coarse inclusion 与同源 fine restart 互斥。旧 direct-base seed、旧 material-envelope-seed 入口和 independent/reset flags 不能混入。

同源 fine restart 还核 source/schema、complete final、全部输入、完整 representation、exact target、当前 complete coordinate_norm 与 returned current-point identity。不仅检查 M320 这一整数。

新 norm identity 依据完整 current space 重建。两个 ready 明确选新输入 $\mu=.01$、restoration $\mu=.01$，不从旧 source 的 damping 或旧 norm identity 暗中继承。这是显式算法参数，不是关于最佳 damping 的结论。

源从原 91c 的含缩进 `def save_report` 开始直到 EOF 的整段逐字相同：

`3a34eeb13a52579aacafb1598c52a94a42f8db2cfab03a3fef0d64c2b88937d5`。

因此保留完整原 initial/read failure 记录、QP/Phase I、all-row constraints、每个真实 trial、非线性筛、永久位置、正常预算停止与 final read。初始化变动仅负责新的完整来源、空间、历史和 actual parent injection。

## 9. 两套完整 ready，不预填未来实际报告

两文件分别选择 cc0a 与 91c actual parent path。科学步先依赖所选真实 final bundle；pure reader 的 parent 依赖是已存在的 reference.npz，因此科学初读失败时不会因 fine final 不存在而屏蔽诚实的 failure readout。

保留 N2048、stage-block64、angle-block8、integration-order8、J923、p4/epsilon.001/scale.05、legacy fraction .5、4.2/.9/1.01 amplitude、reach .03/safety .992、原 active192、完整32 normal stages及所有原 root/mean 参数。第一 budget 仍为一轮 metric、maxiter16、至多四轮 restoration/maxiter64；没有用新的低配观察或减少变量代替完整求解。

父实际 report/final/model、新 field、root 或证书 SHA 均不预填。是否已有真实 eligible parent 由当时实际返回决定。完整 raw 字段、cache 与 checkpoint 仍只留 runner，公开的是原完整 source、完整参数与紧凑实际返回。

只清理原行缓存 `rows-*`；不删除完整 reference cache，不要求提前重跑 plain R711，也不增加科学 fixture 或新的准确性门。

## 10. 完整源码表

以下每项的 Git blob 确实由 create_blob 返回；不是本地 hash-object。root 可逐份取回全文核对后正常发布。文件目标目录为原 topic 的 `scripts/resume_20261126/`。

| 完整文件 | bytes | SHA256 | remote Git blob |
|---|---:|---|---|
| so3_frequency_refinement_layout.py | 13582 | `ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27` | `8d459b9b1dc3defda44b58bc36c306fe586c484e` |
| so3_frequency_refined_smooth_triangle_meridian_operator.py | 42982 | `41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2` | `20b4707c1ea7628d7bd922d24ba0226da276c2d1` |
| frequency_refined_smooth_triangle_literal_zero_moment_input.py | 31068 | `bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971` | `6a4d1e1465a115175738e1f023cc9d9f6aa2767e` |
| reference_centred_frequency_refined_smooth_triangle_calibration.py | 12375 | `688e111664eaca9f57803388f18f220c22d8bc6c4b9472589df2e06f3c8d9e47` | `6da84c41e69705a3b2a662c76f70eca5f1625e13` |
| frequency_refined_normal_frame_c1_reuse.py | 34905 | `aaca0b63c132bf7cb3dd37385c8dff2329614e9852c2293cd93fd46f9364ae67` | `1b4b7829bf593dec303fc79b23dc29b04b9e37af` |
| frequency_refined_detached_normal_stage_matrix_reuse.py | 47222 | `d65f20fdd4d162482f041f8d85ddd0e3bc03238685e28dcaebbabb73b2b3d488` | `1adec57c2c26122a1420d46613ff0b995344a8e7` |
| frequency_refined_adjacent_normal_frame_matrices.py | 36272 | `d6c0c90784a6335874afc183ac65cc6de868c3c8d8b0bf821f8cbb25789c2b34` | `ab54ed88bbf2c84dbe986fcb961cc7b77ebfeb21` |
| so3_reference_centred_frequency_refined_smooth_triangle_normal_lift_operator.py | 96789 | `8349fc52c9b2d399b2511d2af5f2cf23b8be284f7fa0ae12f28fc5bd7d1d3404` | `eea5852f631e5a4ede21431d8fa7ba044d5ff493` |
| so3_reference_centred_frequency_refined_material_envelope_geometry.py | 68445 | `f22cab8d8d9f9773e42af542f0d1012733880188db9c8265da15739e2ad8f8af` | `3bee0ed114caf3879bddb472322e1de116ed515b` |
| transfer_material_envelope_to_frequency_refinement.py | 65540 | `b8ac67ee7e2a9f972b4c8377dd49e925b9b178937f47049b17989dc7c767c2c2` | `3d931e4ecf2ba27ca28fbc0689a60036f168a6c1` |
| fullclosed_frequency_refined_material_envelope_so3_qp.py | 79670 | `6a900861c01d0967dc585dd84797cc2428b62bd4a5969d594a68387c7a0175be` | `1c5eff9c52b705e20e889b5d02883f1d2cb969bb` |
| launch_frequency_refined_material_envelope_so3_actions.py | 22874 | `dbdf9cce0a2a294e601a6416b0084bdbc66a0257151d50e702a53b1c81514e43` | `67cff73554f39d5018b3ba94c629fd990aa2bcf7` |

| read_frequency_refined_material_envelope_so3_report.py | 98804 | `bc0c2c64d4f512fe4a42711e1b0f91ef4496a03a7b1d969c27febd5476c3f2eb` | `0ef6425b55876a8001b82765e814bbf393e63346` |

pure reader 由 solver 独占从原 e244 完整体派生 v2，保留原 22 个科学归因函数以及完整 snapshot/geometry/C1/matrix/memory 责任。最终完整体相对 e244 仅把顶层 DRIVER_SHA 换为本次 `6a900861c01d0967dc585dd84797cc2428b62bd4a5969d594a68387c7a0175be`；完整字节已独立取回、核对 SHA/bytes，并确认该唯一替换。旧 e244 全文和来源保持，不会静默替换。solver 对新 transfer 的 `_input_identity`、完整模型关系、两种 current-point 模式及纯 validator 作了文字审读；没有因此声称 Python AST 或科学运行。

## 11. 三个完整 stdlib 再生器

| 完整文件 | bytes | SHA256 | remote Git blob |
|---|---:|---|---|
| derive_frequency_refinement_transfer_v2.py | 66218 | `1cd4b726b98d98189b043e3b418ac111d851f1e619925ac583311a26582387f8` | `4d83085bbdaa9c9e8758eaab7f1afeb8dbe651ac` |
| derive_complete_frequency_refinement_sources_v2.py | 66439 | `2e701275eac35337634c10575970b0648261dd3ea3374a78b19b218ef7ea4226` | `df9520b5d26dc2962b24ca8242750cb9cd35e3aa` |
| derive_frequency_refined_reader.py | 11595 | `176fdb95374e03657516fd722bb00c41ec455170f9b686d5fe0080b412a59195` | `8817f3a1b94d05d94ecdd3bfdc088fcf6ff356db` |

主再生器接收 repo 和 fresh scratch outdir，先核完整原源 SHA，完整派生九个核心体；经第二完整 transfer 再生器形成 transfer，再形成完整 driver/launcher。第二体每个大函数按完整函数 SHA 和准确边界替换；没有省略函数或向 placeholder 导出。第三个再生器独立读取完整 c0cc 父 reader 与本次完整 driver，生成第十三份完整 pure reader；保全部既有归因，只增加已登记的 current-layout/source/transfer 边界。

最终再生器对十二份完整输出逐 SHA/bytes 核验，并在可用 Python 环境中执行 stdlib AST/compile、literal重复键检查和原完整 loop/parse 等号检查。它不 import 生成的 NumPy/Torch 科学模块，也不调用任何 field/root/matrix。

当前云端已经逐项重放全部文本替换，十二份输出 whole SHA 和 bytes 都与已保存完整源相等，launcher parse 和原完整 loop 也已按纯文本核对。环境不可用，所以**不声称已经运行 Python AST/compile**；再生器明确提供这一步可复核纯静态程序。没有把这个实施状态伪装为科学返回或连续证明。

示例的纯源码入口：

```text
python derive_complete_frequency_refinement_sources_v2.py \
  --repo /path/to/checked-out-repo \
  --outdir /path/to/fresh-source-output \
  --transfer-deriver /path/to/derive_frequency_refinement_transfer_v2.py
```

上式只再生源码，科学 CLI 仍是两个 complete ready 中的完整 Actions 参数，不在本机运行。

## 12. 适用范围和未支付责任

本次完成了一个实际可执行的全空间 M320 源入口及其独立来源、字节注入和历史责任；尚未得到任何 M320 科学场。没有初始/末态 Phi、root residual、有限 geometry 或 continuous bounds 可以登记为本次已返。

准确 trial-function 包含、工作首次重读、准确 branch association、完整六 jet 误差和全时 reach 是分开的责任。已有 R703/R707/R711/R714/R715 的条件论证和已刊同 g 精化合同仍按原假设使用，不因新源码本身自动满足。新 current M 不使旧观测或证书自动精化，也不允许丢弃全 E 或混合参数责任。

若实际初读、数组/来源 guard、normal root 或真实几何失败，应按实际完整报告归因，再作新的明确输入/完整 source 修正；不改真实数据的 identity，也不把未完成值宣布为通过。

## 13. 两份完整待执行参数与远端保存

以下参数均完整保留两步、所有数值 argv、51 个 runtime source 角色和 scalar summary selectors；这不是省略版命令。科学步从被选择的真实 complete final 读起，pure 步依赖已存在的 reference。尚未知的实际 parent/report/model/final 身份为 null，必须由真实原报告和完整来源 guard 得到；没有预填未来科学返回。

| 完整参数文件 | bytes | SHA256 | remote Git blob |
|---|---:|---|---|
| M320-frequency-refinement-cc0a-v2-ready.json | 72978 | `150277da610fa7c6aa5b47866ca35f04f38e65b2b193b10433ae8d038b8f86ef` | `9779a7a0502aca0361187ac195c160d5754a66e8` |
| M320-frequency-refinement-91c86-v2-ready.json | 73050 | `c88934fc77dae689a3879bc4e280ed0b8f1219a4b672fcce149165a1bac5c6bb` | `35e21de003d709dea5942dcfb992f8f5a697b15d` |

cc0a 参数的两个完整 step ID 为 `complete-frequency-M320-from-cc0a-20261127-v2` 与 `actual-frequency-M320-from-cc0a-20261127-v2`；91c 参数相应为 `complete-frequency-M320-from-91c86-20261127-v2` 与 `actual-frequency-M320-from-91c86-20261127-v2`。两份均使用 fresh v2 输出目录。它们不会接受新 repaired-08 5c5c 家族；若需要该来源，须另派生独立完整版本并保本版本历史。

独立纯 reader 的完整实现说明为 5,406 bytes，SHA256 `f6fc51221e537530ae9922101be8b77830d5c566fc5d96d66974b6344792cfd7`，remote Git blob `63408bffdec2baeb2659bd46fe54b743244fa098`。本说明、两参数和所有源码仅保存为未引用 blob，发布与实际 Actions 准入由 root 负责。
