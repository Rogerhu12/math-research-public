# R726：完整 Slerp seed 科学族的实际接线和恢复

本说明对应独立候选 namespace `fixed-fejer-r726-bhalf-first`。完整代码已形成，不是新计算已经通过的声明。新run、实际model、point、均值根、全场报告、连续证书均未知。原25/26/27及其他在跑源码没有改动；没有改ref或队列。

## 1. 直接母体和当前完整来源

直接母体是已刊R725科学族，固定publication `95801769a95b2940b14ad01fe7640581b2c2fb44`。完整current表：

- `computations/fixed-fejer-r725-current-complete-runtime-binding.json`，57,985B / SHA256 `f7ef58856c06e66b5450b0e745c98fc92ecc2f1bf69b0b3a2f06827a7be9e82b` / Git blob `a27e6bdc2621d7356a953fd3a1bdd2d2781d3984`。
- `computations/fixed-fejer-r725-complete-scientific-source-delivery.json`，25,162B / SHA256 `9929f153017ad195bf4d9aed8bbbad3d05dd32e81491cc2b11e7910a9811bb94` / blob `1c0c17981f4fcbca81eed5e09646bc007299fdea`。

新完整表 `topics/visible-flex-larger-amplitude/computations/fixed-fejer-r726-current-complete-runtime-binding.json`，55517B / SHA256 `6e5480838f54ecb50ce8baa085ebabed37504a3ba759d1ed958ec28c6d9df059` / blob `159d8c56b1b966cf5de5d19bceec68db3630144b`。它包含实际driver的整张137-role registry与全部23个current运行体。相对R725，19个current pair替换，118个pair原字不变；不是声称137个全对不变。旧源、原registry、其历史父记录都完整保留。

22个新运行体合1,169,185B；另复用原字42,637B scalar observer，current合1,211,822B。driver、launcher、reader等也有完整运行体身份，所以“23运行体”“137注册角色”和原157科学argv不是同一计数。原共享f848 mean本次成为实际新源，因而从R725的22个current运行体变成23个。

19个更新角色为 `root_packets`, `analytic_J3`, `analytic_J3_binding`, `seed_reference`, `seed_mean`, `meridian`, `geometry`, `geometry_selector`, `endpoint`, `new_moment_input`, `reference_calibration`, `frame_C1`, `stage_matrices`, `envelope_transfer`, `adjacent_matrices`, `analytic_frame`, `closure_values`, `detached_meridian_values`, `batched_geometry_binding`。所有其他角色的实际路径/SHA逐pair相同；不是用近似source或名字判相等。

## 2. 最小seed数学体与完整推导

最小阶段完整5件由 `topics/visible-flex-larger-amplitude/computations/fixed-fejer-R726-spherical-seed-complete-source-delivery.json` 保存，13688B / `278938b6072a44fdf2b0743a8986f0ed4b34da19d585d72199a27ca52bcaf2ec` / blob `ef950fc907929731802f6040d2420212d3c0d63d`。其中新mean为48,226B / `2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23`，seed为52,457B / `176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a`。

完整数学说明是 `notes/2026-11-28-R726-complete-spherical-seed-mean-angular-source.md`，23,146B / `192fc4a7dad2e61459bbf1a2b938d860049a6b17f9f2cd1c48e37c278010c802` / blob `4a645e48aede8380f914d7f3545dd686f08c3acd`。其式(5)已保留rho=q/2的正确链因子：一阶是(1/2)rho^(m−1)，二阶是(1/4)rho^(m−2)。4rho^m与16rho^m只可在rho=1/8代值，不用于较小q的逐点界。原统一截断常数及全部运行体未因这项说明修正而改变。

实际准确边界为 R726 的最短球面插值 S_chi(N(T0),N(v))。工作图先归一化两个输入，以q=|N(T0)−N(v)|²/2计算Slerp两系数，再归一化系数和。末次归一化在准确Slerp域上是恒等变换，但在实际浮点图中确实执行，所以其完整一阶、二阶与径向导数全部计算。没有只改metadata或只改field，却继续用旧chord均值。

真实总均值方程：
`Lc*v + integral_boundary S_chi(N(T0),N(v)) - K = 0`。
真实中央方程：
`a_delta(lambda) - norm(v) = 0`。

新程序求完整3×3 Jacobian和全部两角implicit方程。旧全角Newton/Armijo、原所有迭代/回溯/容差、全12片中心profile、lambda标量求根及projected frame原字保留。R724两个等长反号半波、R725 epsilon=1/8三片C3 cutoff与8个内部boundary切点不变。它们仍分别是物理中心半波、边界cutoff和辅助全12片profile积分，不混作同一切分规则。

小角工作式为32次多项式，系数从同一递推生成，q一二导和a导都针对该同一图。大角分支保完整acos/sin链，不在零角调用其奇异表达。统一2^-98、2^-91、2^-84、2^-96仅是准确系数截断界，未支付系数生成、Horner舍入、实际q、输入/输出归一化、积分、根、全场误差。有限工作式在q=1/4切换不声称准确C2。

没有新增急角数值门。工作域仍明确要求实际非零、非反极和导数有限；R726急角存在/唯一性的假设没有因为数值函数返回而成立。旧R709欧氏球势、旧R722专用后验公式不继承。父任务另写的R727亦没有被本源码宣称已消费或已通过。

## 3. 实际入口、输出和保存数组

seed构造仍是：

```text
SupportedUnitMeridianJet(
    problem, prepared, *,
    expected_bundle_sha256=None,
    seed_parameters=None,
    mean_kernel_module=None,
    cache_directory=None)
```

无新增keyword。完整mean模块及实际solve/field/definition函数代码来源均硬pin新2513完整文件。实际边界入口为：

```text
spherical_boundary_jets(T0,T1,T2,v,v1,v2,chi,*,Ts,chi_s)
```

它消费实际已记录的raw v与两角，而不是从d重新制造一个不同的归一化图。函数仍输出T0、T0_s、T0_phi、T0_phiphi，与原完整seed后续接口相同。

原十二数组v/d/w/lambda及各自两角、全J_v、profile、B三个角阶和三分量总均值残差全保。每个真正返回的batch保原literal角字顺序、全径向节点与全源身份。null或未返回batch不伪装成完成；seed缓存写中断的实际记录数和已cache数继续按原合同分别报告。

## 4. base、完整Q与所有normal层

base继续读取原e717完整reference、3da完整输入绑定及89cc固定maker；scalar、预定Fejér chart、全部节点/域/原输入参数不变。只有实际seed提供者、模型描述和来源切到R726。新的校准由新的完整base/seed/mean构造，不借旧seed均值、旧root或旧校准值。

完整Q binder保十八literal词、两bubble、原nodes、完整chart/scalar/reference/H和当前seed模型检查。它新增纯标准库 `_spherical_boundary_definition`，逐字段等于新mean的纯定义，source指向实际2513。seed模型、working定义、准确field和总方程字符串都显式核同，不能拿旧欧氏工作定义换标签。

normal除构造器里的当前seed schema外，完整从 `def __getattr__` 到EOF的后缀原字保持。全部32stage、每stage原Newton/回溯、完整control、全角一二jet、all integration/query、raw hDelta和bubble保留。每stage末尾与最终endpoint的强制原残差重读仍在；active J/J*仍走原完整图。不可写point owner、完整controls字、data/version、严格plain/transform旁路、缓存计数和scope保留。

analytic J3、analytic frame、C1、stage/adjacent matrices、closure和meridian reuse只传播实际current base/helper/schema/pin。原AST历史锚及完整wrapper例外仍指向真实原体，不以新source假冒原方法来源，也不去除精确guard。原math方法不换公式，不减变量或求和范围。

root packet仅新增一个完整R726条目，整个旧registry逐字保留。每个旧条目仍保自己的normal、base、calibration/helper身份；没有广域改旧hash。packet仍要从实际point/source/order和完整角/32stage缓存记录产生，模型相同或mutable progress不能代替真实snapshot。

## 5. geometry、driver、launcher与pure

selector只替严格current normal和meridian-helper whole pin；原同build_rows的完整曲率transpose缓存、literal key、计数、fallback、行序都原样。geometry只递归必要来源和schema，完整有限域、原各族、原batch预解/逐点回读、聚合/所有预算不动。有限geometry complete仍不是准确全域feasible证书。

batch纯binding同时钉实际geometry和selector的完整名、bytes、SHA；原policy抽取与完整validator保留，没有通过新F/J/root或Torch执行判断成功。

driver实际加载新的seed、mean、base、Q、normal和sourcebinding。实际SOURCE_PINS整表与本次完整registry逐对相等。完整 `save_report` 到EOF共21,481B / `d3396f3294750a1b607f8314545a44467a244c09e6a888a2d9f9c32db4599531`，与完整R725母体原字相同：restoration、LM、QP、line search、接受不等式、stats→geometry顺序、保存时点与预算均未改。本族不混23 adaptive damping或另外geometry-first设计。

launcher只接实际新driver文件和whole SHA。pure reader92,808B，保原完整source/model/history/typed/endpoint/normal/geometry和作用域检查；没有为100KB限额删旧检查。新seed实际metadata由新的stdlib sourcebinding完整消费。

| 实际对象 | 新schema |
| --- | --- |
| report | `complete-fixed-fejer-r726-dk-cache-SO3-QP-v1` |
| pure | `actual-fixed-fejer-r726-dk-cache-observed-SO3-readout-v1` |
| normal | `complete-fixed-fejer-r726-detached-meridian-normal-layer-v1` |
| base | `complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1` |
| seed | `complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1` |
| mean batch | `complete-R726-spherical-boundary-paired-halfwave-seed-working-mean-and-angular-jets-v1` |

pure输出中 `supported_unit_seed_definition.spherical_boundary_definition` 与 `seed_diagnostics.spherical_boundary_definition`均为完整公式对象。新batch核全literal角、全部boundary节点、小角/大角pair计数总和P×A、有限0<=qlo<=qhi<2。sampled acute仅等于qhi<=1，且显式不构成whole-domain或存在证书。R726准确域证书与旧R709/R722继承均为false。

## 6. 全问题、参数与历史

固定g仍来自预定Fejér图和原scalar，M160/J923/N2048完整定义不动；157个自由core系数、全部923×3×482 omega及H不减。新seed是同固定target下新的完整物理候选，不自动承接旧physical field、均值根、法向inverse或reach证书。

新源码无新增scientific CLI词。父任务组完整参数时仍保原157 science词、7 pure词、所有预算、458/445正式投影和64 live以及全部history/peer；按真实来源替换current pins及独立namespace。预定比较仍b/S=1/2、profile delta=1/32、restoration/metric初阻尼.01，epsilon=1/8由实际完整seed固定。本交付没有创建新queue或执行science；所有新run/input/model/point/fee值null。

memory transfer保原所有family、全部13成员、typed first-discovery及未知责任。旧source记录不改成R726；固定target相同不意味旧seed物理final可以迁移。same-source restart仍要求本族自己实际complete report和全final bundle。未返peer不当空历史，不从progress构造断点。

准确后继必须真正处理R726完整球面B、准确零角、root域/branch、全两角、完整参考partition、cutoff/half cuts及current全控制闭合链。旧R722/chord/欧氏势代码不能仅换source hash接过来。这个要求是数学对象本身变化，不是额外执行前门；新working science无需等准确费用实现后才运行，但不能据working返回宣称它们已付。

## 7. 全文文字再生与恢复

最小两体的24个完整patch、完整父源和输出仍在37,039B再生器 `reproduce_fixed_fejer_R726_spherical_seed_sources.mjs`，SHA `6aff8eb886e36c41a5ce46d74a160bed73c2055596b8efd7293800c936b7d9c6`，blob `7395c0a2e8adc81317ac95142c5c25d9ffa4d8b3`。

其余20体的全部176个带次数before/after patch保存在 `topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_R726_complete_scientific_sources.mjs`，85151B / `536f859b824ef3652180bfdfce1a2a353185301a25ac88be6c373a3cfb214757` / blob `8a53ac527e291783e05872debd41eeb032a9f4b1`。该完整MJS还含每一母体/输出全identity，不依赖丢失的scratch。命令参数：

```text
--source-directory <complete-source-root>
--generated-directory <independent-generated-directory>
```

输入可以是repo根、topic根或完整父源码平铺目录。逐文件先核完整bytes/SHA，按全部patch顺序产生完整输出，核完整输出身份，再反向恢复母体并要求全文相等；不覆盖不同已有文件。20体全部正逆文本构造已经完成，没有运行Python、AST、compile、fixture、数值field/root/J或benchmark。新恢复脚本是完整来源恢复能力，不是额外科学准入门或数值等价证明。

工作环境在完整源码与绑定保护后曾重置。全部runtime、两reproducer和完整数学note可从远端固定blob恢复；本说明和最后总表据这些同一完整记录整理，没有重做或改变数学程序。无真实source内容被摘要替代。

## 8. 全新运行体

完整path和Git blob在当前binding。以下给每个完整文件的SHA，便于检查范围；执行恢复仍用全文件。

| role | bytes | 完整文件 | SHA256 |
| --- | ---: | --- | --- |
| seed_reference | 52457 | `fixed_fejer_R726_spherical_halfwave_meridian_reference.py` | `176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a` |
| seed_mean | 48226 | `fixed_fejer_R726_spherical_seed_mean_jets.py` | `2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23` |
| meridian | 40841 | `fixed_fejer_r726_meridian_operator.py` | `bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37` |
| new_moment_input | 43818 | `fixed_fejer_r726_literal_zero_moment_input.py` | `b0b8d3fdffd587ac23b081f69201d9a7fcc52b0369ab483a0d5571fbadcac8b7` |
| closure_values | 59438 | `fixed_fejer_r726_closure_values.py` | `6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3` |
| analytic_J3 | 25695 | `fixed_fejer_r726_analytic_stage_jacobian.py` | `81d532e6816c90e38eb5fe12e6202cc13e72a83d3260269648b3047ec0169eb4` |
| analytic_frame | 47429 | `fixed_fejer_r726_analytic_normal_frame.py` | `56c66f8b5130a4280ef68a0f4ef71b3fa60116fc2be3139daaa588e59f55610a` |
| frame_C1 | 37361 | `fixed_fejer_r726_normal_frame_c1.py` | `2ffc3c0ca8567c3db082ce5ae047c2cfb5d3992128fe617826a7f6fe815793ac` |
| stage_matrices | 61280 | `fixed_fejer_r726_stage_matrices.py` | `4ba1195259862fe968a56df5484b321d19c92a81fcf720a32436c44d290f0c84` |
| adjacent_matrices | 36766 | `fixed_fejer_r726_adjacent_matrices.py` | `21968326848f975fa42e660400f270d3551542a1f26b8c09e9379c41a4b94062` |
| reference_calibration | 11850 | `fixed_fejer_r726_reference_calibration.py` | `1371d69aa40d467e4341cbd4064f950dcdc568441abe7c41c1f7353c5641148f` |
| detached_meridian_values | 41124 | `fixed_fejer_r726_detached_meridian_values.py` | `587dd1070f58a3a4fa0b036b7e4d22f7d2a7cdf413e2fdc2be3bef9b235be9d0` |
| endpoint | 96262 | `fixed_fejer_r726_normal_lift.py` | `335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9` |
| root_packets | 75687 | `fixed_fejer_r726_root_packets.py` | `9da481209cd48d82cb297b213650cc94c4f2148c097602f3495d57ba8f4508fc` |
| analytic_J3_binding | 52866 | `fixed_fejer_r726_source_binding.py` | `77c4a98d8736f10edcb33e640749033499366e41acbe8b962a0877d304235cfa` |
| envelope_transfer | 78993 | `fixed_fejer_r726_memory_transfer.py` | `01e6f6a80b3556ec941d9f46431e7b5b6b6de7892865040c5f61a09117b5bc03` |
| geometry_selector | 35982 | `fullclosed_point_inequalities_v2_r726_curvature_cache.py` | `4386ce195c9709e0bb204cd749b89429652a177bb497bbc2fcf2756564496253` |
| geometry | 88434 | `so3_fixed_fejer_r726_dk_cache_geometry.py` | `b46cd96f5bfe019137b1332750ab3f81b3c100895cff33187898ab0e1daaaa65` |
| batched_geometry_binding | 20516 | `fixed_fejer_r726_dk_cache_binding.py` | `f24ff296f0a058d43a779c17d11916c4eec1fbcf26e337ede73f433b7db61422` |
| driver | 99231 | `fullclosed_fixed_fejer_r726_dk_cache_qp.py` | `58630a875941be3612947e724aa25d9556b903c5ee1c392ff79f8def974e2813` |
| launcher | 22121 | `launch_fixed_fejer_r726_dk_cache_actions.py` | `36a7a0a286c7a983cdec7bc1ed19299c1ec57901df7d0daea707e20891e412c1` |
| reader | 92808 | `read_fixed_fejer_r726_dk_cache_report.py` | `1aae949feefb2e6bfb457d755aaa6a16412d9b5333344fa351b4ab598287248c` |

唯一current共享observer是 `fixed_fejer_complete_geometry_location_progress.py`，42,637B / `4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94` / blob `bad0be021443e7fa7a8fbfe4ee473f3e05ccadad`。它只读取已有完整返回值，未增F/J。

所有新运行源<100,000B：最大driver99,231B，normal96,262B，pure92,808B。没有裁片、拆出不完整科学主体或删除参数以满足限额。此时完成的是完整独立Slerp工作求解族与其来源/纯消费闭包；实际运行结果与准确几何证书仍待真实求解和相应完整证明。
