# R528 — actual225：同一真实 H 的一次 128 接受步、第二试步资源未完与完整必要读回

作者：OpenAI ChatGPT（AI 协作者）  
日期：2026-11-16（UTC）

**可信度：启发式/数值证据。** 本文依据 actual225 两个已经终止的官方 Actions job 的原必要正文、真实事件及冻结入口源码，确认这一次实际执行的范围；不把数值下降、来源生成、程序退出、完整运输或清理解释为数学存在性证明、完整 native 接受、全域 metric/reach 证明或性能比较。下述有限程序控制流含义限于本文所列实际输入、原门及其已返回记录。

## 528.1 本次确切结论

actual225 的独立来源生成、原 63/78/91 输入准备、一次真实当前 $H$ 的原 binary64 完整 withJ 与 R273、同 call 的 128 owner 都实际启动并返回了各自的必要范围。当前 call 的 owner 在原 6000 秒上限内接受一次 $\alpha=1$ 步：完整原归一化残差从

$14074125.7215534695603754375431894587$

下降到

$0.00119384020061276193473229654960738502$。

这两个值均来自各自完整 576 stage、129248 行评价。第二方向的首个 $\alpha=1$ 试步只有 534/576 stage、119840/129248 行完成；stage 534 至 575 的原错误全部是 `explicit-experiment-time-budget`。该试步没有返回全局 norm、worst row 或 mean，不被接受，owner 停于 `resource-partial-trial`。它不是一条已经完整计算并被数值下降门拒绝的试步。

最后保存的**已接受状态**仍是前述完整 $0.00119384020061276193473229654960738502$ 状态，其原 $2\times10^{-9}$ 容差旗标为 false。独立 fresh replay 返回 code 3、complete=false；后置 stage、boundary、endpoint、audit 四组件全未启动。因而本次没有完整 live response、没有原 affine FD 返回、没有原 fullDN 入口调用或最后 fresh audit。R522 配对点积与 R515 径向模式缓存的源视图均实际生成，但四个后置组件的编译/执行回执不存在；不能据这次 owner 时间推算这两个后置改动的加速。

原整个科学钟为 19200 秒。本次外层实际耗时 6982.009654177 秒，外层 `resource_stop=null`、`external_signal=null`；原内部 owner 上限耗尽与整个 job 总钟耗尽必须分开。两种必要正文均完整返回且在 compute/report 两 job 逐字相同；实际 owned quiet 完成之后，本 namespace 已真实删除。

## 528.2 官方 run、source、job 与运输身份

本次入口是 [R527](R527-live128-paired-stage-and-radial-cache-complete-chain.md) 及其[完整接口](../notes/2026-11-16-request225-live128-paired-cache-original-full112-interface.md) 的独立 actual225。旧 221 编号和来源只作祖先，不是续接旧 run、旧 completed61 或固定 actual91 的响应。

| 项目 | 实际值 |
|---|---|
| repository | Rogerhu12/math-research-public |
| run / attempt | [43852521165](https://github.com/Rogerhu12/math-research-public/actions/runs/43852521165) / 1 |
| event / branch | workflow_dispatch / main |
| 实际 source/head | `5af07ed64877475bc05a488306246c9be22926bb` |
| workflow | `.github/workflows/visible-larger-public-live128-paired-cache-original-fullDN.yml` |
| compute | [133248437738](https://github.com/Rogerhu12/math-research-public/actions/runs/43852521165/job/133248437738)，completed/failure |
| report | [133308136127](https://github.com/Rogerhu12/math-research-public/actions/runs/43852521165/job/133308136127)，completed/success |
| 当前 request | `public-live128-paired-cache-original-full112-FD-fullDN-request.json`，64734 B / `42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285` |
| workflow 字节身份 | 18518 B / `5ed7a2c3fd2fdab0d2fe02aeb050a07e3bfe8f3344b23ba3bd16f7573b274d53` |
| namespace | `visible-live128-paired-cache225` |
| current policy | `R527-current-H-live128-paired-cache-client-policy-v1` |

本结论的唯一读者在终态后各取一次官方 job log。下表是连接器返回的官方日志**解码文本重新以 UTF-8 编码**的身份，不能称为官方 HTTP 原响应 bytes；没有重复下载日志。

| 官方 log 的解码文本 | UTF-8 bytes | SHA256 |
|---|---:|---|
| compute | 166692 | `37c471763c7b043b9edf4deb712016bed64de047bb4069b5bde7f25590d4e4af` |
| report | 314106 | `1fda78d0a0f6b8bad492fc6541632860a498641c6334f21c5ee3d5b7587c7f2a` |

解析视图只剥离实际行首单 BOM 和锚定的官方 timestamp；不改变 JSON body。report 的环境变量回显不是额外科学正文。以下各 frame 在两 job 中唯一实际输出并逐字相同，body 身份不含结束 marker 前的分隔 LF。

| frame | body bytes / SHA256（无分隔 LF） | producer 文件身份（含末 LF） |
|---|---|---|
| `BEGIN/END_REQUEST225_SOURCE_PREPARATION_NECESSARY` | 49780 / `0e5b3c590435cddaa6534a9be1f37fe7cb9dc791b9b29b60e782c82fb430e9d0` | 49781 / `1f205f97ef77a3babce8a2d28da74e66f7b022e706b4f050050d6103b4d94fd7` |
| `BEGIN/END_REQUEST225_PAIRED_CACHE_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY` | 51982 / `31927157d601caf3cf4766efc18c4911a99c99fb908d7a3ed341ac85b419b19c` | 51983 / `e3d8a314ecb48d192cfd8e3ae71ab882289f1b367456cbee68fb5eb3eff2d3d7` |

compute 实际 frame 行为 610–612、679–681；report 为 69–71、107–109。它们是两个独立语义 scope（来源生成与科学必要结论），各自小于原 90000 B；没有把同一个超限对象拆包。本次科学 reader 的 `necessary_readback_complete=true`、`metadata_read_errors=[]`，不意味着 `task_completed` 或 `fullDN_accepted`；后二者均 false。

官方步骤中，compute 1–10 全 success，11 原科学 failure，12 来源读回、13 owned quiet/科学读回、14 清理均 success。report 两种必要输出均 success。这些 step 标签只作运输/生命周期信息，具体科学范围由后文原字段决定。

## 528.3 全部实际源生成与原输入准备

### 528.3.1 当前 356 源闭包

实际 source preparation 在 10:51:41.4365698Z 返回 exit 0，完整本地 source receipt 为 143292 B / `a7037afb0c5071d4e096eda25bcdebfcea7f5613a1ee6ca8167fa9bada297ae9`。必要 scope 保留其身份与完整当前生成记录。

本次核定 342 个公开源（含原 336 个祖先源）和 14 个实际生成源，共 356；14 源由 3 个 R522 原输出与 11 个完整当前调用链视图组成。R518 的 12 个中间文本均按原字节形成并记录来源，不把只形成于内存的中间视图冒作另一次科学执行。`not_generated=[]`、`source_preparation_complete=true`。生成阶段原字段 `compiler_started=false`、`scientific_clock_created=false`、`scientific_code_evaluated=false`、`scientific_module_imported=false`；这些旗标只界定生成阶段，不能否定随后实际 owner 的科学执行。

| 当前生成角色 | 实际 basename | bytes | SHA256 |
|---|---|---:|---|
| R522/operator | geometry_20261116_native_paired_digit_operator_trace128.hpp | 29617 | `082d5a1fdd900071fb1cc008304c5a4c97bce92b173851bda1514ec1682eb7be` |
| R522/stage | geometry_20261116_native_paired_digit_stage128.cpp | 12880 | `49a7e226eadc7748d5d2b3f94119c2e4dd7024348e6878c673e73b1a33db3b55` |
| R522/component | geometry_20261116_live128_paired_digit_final_components.py | 33416 | `93ecdd833922f833bdb50a8f264bc5db1913f5ce16dbb0cb4f7fbc7d285070f1` |
| owner | geometry_20261116_live128_paired_cache225_same_call_owner.py | 18905 | `a587dd6833532c60296ed40ce105d9c190717071e8d6fb3e137f79a27d9209be` |
| assembly | geometry_20261116_live128_paired_cache225_response_assembly.py | 28613 | `5fa469847019a8fdaf040245a93ff6a447da13ecda468fc6285f90e2c096504c` |
| system | exact_20261116_live128_paired_cache225_current576_system.py | 29007 | `6158c460dc9abd7ea153a0b2708decdf1378f8b0a79e46bbe947d4d8b59074f6` |
| qr | exact_20261116_live128_paired_cache225_current576_chain_qr.py | 21846 | `9e393cd970554e48203f80f86d6734a74ba67ff7bfa51964cbd5ff9d4450b48c` |
| pipeline | geometry_20261116_live128_paired_cache225_call_pipeline.py | 19356 | `c01aae5614d00c746c671eb98abcdc6ab90aa39366e8c0a7d3b5da3ed83fd515` |
| call | geometry_20261116_live128_paired_cache225_current_call.mjs | 34385 | `c9f83fd2f1db33c66dae653291bf48db7e2cfe3a8f5f87b4ba01b92d6626eb50` |
| worker | geometry_20261116_live128_paired_cache225_worker.mjs | 8183 | `0be16b9bbfd1635c5bc0155f45b222534486c5491e1e6c14b32ad8e605ffb2bf` |
| client | geometry_20261116_live128_paired_cache225_tail_client.py | 32147 | `cfcc205cf0c291dc6a4dfd280a4c60f67f1d84062761e68c62117714867cb328` |
| fulldn | geometry_20261116_live128_paired_cache225_original_full_dn.py | 37222 | `4c5c0c0dab7fe1b96dc4065acc4c027ea872fedbf6b4f750f462cb0af6ee3aca` |
| runner | geometry_20261116_live128_paired_cache225_owned_run.py | 38997 | `9e3d7508cfd771e34003e6056020b316cd227f92154280a449226d415f86f400` |
| reader | root_20261116_live128_paired_cache225_necessary.py | 41304 | `85631e35dc9f8f3e2ce5b19a05e8b540ee802b2e8c9e6b3cb01cb3c730cbe8e3` |

R522 原三件字节不变。它的真实 generation child 返回 exit 0，完整 receipt 15815 B / `994a4add8ba1f66ea433bdf17bcfa2a49a332f976db6681d84f64db21055ee45`，原 stderr 为 0 B 的空串。源生成完成本身没有调用后置 stage 或 physical_jets。

本次实际读取的三份公开科学来源计划为：

| 计划 | bytes | SHA256 |
|---|---:|---|
| R515 physical128 radial mode cache | 8662 | `5950052fac0d9c23e96f29421c03df79f4748828b2d7a6e9a4ed7f40bd090666` |
| R518 complete current-H cached-radial chain | 48391 | `4f2097053bddff0bf07a18f09ffa846bd64eb2fa6dd3d9707ab7f24f3ef62f6b` |
| R522 paired-digit source plan | 16347 | `724e46e0d70aefd70309e03d77d4719666058e56001c7a78f7544bada76b9ce7` |

当前 R527 generator 为 22915 B / `b30d418965454b63d5a0e8f6bc50277e38849e959e24ec92552bc722ec83a3ce`；当前完整 plan 为 55391 B / `6e8109e64bafb6e78428298ccc25a5b4d71df29c0b224b0ea20076da006dd1c6`。10:51:43.4984198Z 的实际 binding 核过全部 356 source；Python 范围是 compiled-not-imported，Node 是 syntax-not-executed，此时未把 C++ 科学编译或计算预填为完成。

### 528.3.2 actual63/78/91 的真实作用

原准备在 10:52:14.4419317Z 完成，receipt 69033 B / `26c5e3c166e857894fafd16c0ce9852c7ea361d75544aa7f9e8771d33aa119f2`。原 actual63 只提供 prefix 初猜，actual91 只提供 tail 初猜；它们不是当前 $H$ 的已接受响应。完整实际原输入如下。

| 输入角色 | 实际 bytes | SHA256 |
|---|---:|---|
| accepted | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| frozen_ledger_ready | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| frozen_stored_ready | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |
| tail_config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| warm | 4799943 | `6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a` |
| warm_status | 231286 | `6443fce5e818ff20fd36075f6038ee60630d0b77e8ed2304d41e4d072ea6a005` |

其中 ledger-ready 使用完整 64 字符 `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6`，本次恢复已经成功。解压 actual63 status 为 1810333 B / `8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46`，`original_JSON_reserialized=false`。warm 中 `/complete_scalar_profile/complete_original_port` 的完整 JSON 对象另写 3601 B / `43c9e625ed740fcd8fbaa678ac371eaf1708246dee5bbea37a726e12aa457bc1`；这是完整对象提取，不声称它等于一份原历史 port 文件的原始 bytes。

actual91 初猜 seed 为 26106 B / `fd451e18178ba6f0f5f997b9974666503fb7c570829e42c9299052e8e822c936`。原公开源码准备 20424 B / `009381c5fa113612756e19471c7078c8430d7fbd0b816b5851b281c34f421c69`，actual63 producer 的 46 源合同保留。没有导入 completed61 或 completed91 native response/cache。

容量步骤实际 free=92022263808 B，minimum=68719476736 B，未删除 SDK 或科学数据；这是当时启动容量成立，不是全部最多 18 次 uncached protocol call 必能完成的证明。

## 528.4 同一个真实 H 的完整首调用与 R273

本次只形成 `call-0001`，`native_call=1`、`bootstrap=true`、请求 `jacobian=true,audit=false`。物理 height112 的实际 binary64 little-endian 字词 SHA 为

`21c3572384f906736d9a441ab4c92c0c0c319292c0f660efac28ce333785ec1d`。

没有负零。初始化原字段为 cold=true、first_seed_available=true、seed_assigned=true、original_initial_argument_supplied=false、original_tangent_prediction=false。

这次实际 binary64 原完整 withJ norm 为 $14074125.72142333$，原字词 `61e615b721d86a41`。它与随后 128 初始原 norm 是两种准确算术身份，本文不混写成同一字值。原记录明确：

- `fresh_original_withJ_returned=true`；
- `literal_packets_returned=true`；
- `original_current_R273_returned=true`；
- snapshot/native call/nonlinear iteration/sequence 分别为 1/0/0；
- 原 `complete_current_R273_eta="1"`、原 cusp=true；
- 原 current R273 complete delta SHA 为 `fb6a35ebf8440242ca4a92d1f0b1b42b114d898400d4419719189d08f611f932`。

complete literal packet 是 10348368 B / `800c280e3f07e80cbec8e769244dfe0875744e3f606d2c11c5198152ab2df89e`；physical packet 是 5104360 B / `1c9fab18574bb130f905daef5fcff66163a0fe987528ace2d9bc81829fc52151`。它们均来自本次真实 $H$、本次初始状态与本次 fullJ，不能由旧实验的静态 hash 替代。

实际 snapshot receipt 为 1311 B / `173a6776a6a9f324e21df1d049ccac718478cb3ac3f4368ef98c441fab07fea5`。当前 QR child 完整返回，诊断 elapsed=23.394583938000096 秒，`linear_direction_computed=true`、`actual_error=null`；外层 factor elapsed=23.820174839999936 秒、exit0。QR result.gz 为 4549 B / `f3fa059dd07cda03b6ab46cb9e9f71e2f55ad993011361487e5c4cb4e5303485`。这项诊断是原完整求解链的一部分，未另加新门或 fixture。

维数仍为原 112 modes、576 stage、577 径向节点、每节点 shooting state224；每个局部 RK state226 包含两个 mean，完整 stage 方向数224。这三个维数不能写成“577×224 的 226 状态”。原 physical endpoint/J 合同是 338 输出、338×112 混合 J；原真实行序为

`slope112, second112, meanSlopeCorrection, meanSecondCorrection, height112`。

R527 后续文档已明确修正原历史 request 中未参与索引的 `output_jets_order` 描述。这里不把那条错误文字当程序行序，也不声称本次已返回 endpoint/J。

## 528.5 128 owner 的全部实际有限轨迹

原同 call owner 总 elapsed=5999.060112429 秒；原 request 的 `owner_seconds_cap=6000`、`replay_reserve_seconds=1200`、threads=4 不变。以下是实际全部 initial、两方向、两 trial 和两轮 close；没有省略一个已经返回的 trial。

### 528.5.1 initial 与两个方向

initial 完整 576 stage、129248/129248 行，`evaluation_error=null`、failed_stages=[]、budget_exhausted=false、below_original_tolerance=false。

| initial 原量 | 完整原值 |
|---|---|
| norm 十进制 | 14074125.7215534695603754375431894587 |
| norm binary128 hex | `0x1.ad821b716f74d4277f6b2905ee36p+23` |
| mean height sum | 0.0226842463487103007644065167348694662 |
| mean hex | `0x1.73a8a00cef80fade5b77db67341dp-6` |
| worst row | Pi，stage11，input node12，output node11，mode one-based76，global row2763 |
| 原 residual | 0.000152003159643071247874039879778580579 |
| residual hex | `0x1.3ec6132f8f58ed97f415deb32p-13` |
| sigma（index11） | 1.08001848676319405107421646677400907e-11 |
| sigma hex | `0x1.7bff6ac6766ebp-37` |

两个方向的 lifted recovery 均完整577 nodes、224 columns，以下数字只描述本次实际 R273 delta64 与 persistent128 recovery 的差，不将其作为新的接受门。

| 原字段 | direction0 | direction1 |
|---|---|---|
| different_from_R273_delta64_entries | 129193 | 129246 |
| nonzero128_from_zero64_recovery_entries | 0 | 0 |
| maximum_scaled_recovery_difference | 3.85716491205609519159224270564494581e-21 | 1.41953544608456049717920726862991718e-22 |
| 上项 hex | `0x1.23706b87f27a0b3f33424eb419dp-68` | `0x1.5738fd00e0bd5eeb7a7aa9b84cf4p-73` |
| worst recovery difference index | 2536 | 26320 |
| scaled_z_infinity_norm | 9.085745629468973687432875596670101e-05 | 2.22873200671778566925437456425207472e-06 |
| 上项 hex | `0x1.7d15736aa2622p-14` | `0x1.2b22a60d7b40ep-19` |

### 528.5.2 两个实际 trial

| 地址 | $\alpha$ | elapsed s | changed128 state words | changed128 但 cast64 相同 | stage / rows | 原结果 |
|---|---:|---:|---:|---:|---|---|
| iteration-000/trial-00 | 1（`0x1p+0`） | 1617.182716662 | 128323 | 6109 | 576 / 129248 | accepted=true；strict-original-norm-decrease |
| iteration-001/trial-00 | 1（`0x1p+0`） | 1539.879553377 | 129186 | 12002 | 534 / 119840 | accepted=false；resource-partial |

首 trial 的完整 norm 是

$0.00119384020061276193473229654960738502$，

hex `0x1.38f542791ee361b99fc6420a22bdp-10`；mean 是
$0.0226842463487103007644175740389572371$，
hex `0x1.73a8a00cef80fade5ecf5fdfdbdp-6`。
worst row 是 Pi、stage12、input node13、output node12、mode one-based95、global row3006；signed normalized residual 为负的该 norm。原 residual 是
$-1.29116318358713427789247294030526012\times10^{-14}$，
hex `-0x1.d130c8b5df1df99f3eb17p-47`。
原 sigma index12 是
$1.08152094637491635005947600960005345\times10^{-11}$，
hex `0x1.7c86bf229a5b4p-37`。

首 trial complete=true、budget_exhausted=false、evaluation_error=null、failed_stages=[]，但 below_original_tolerance=false。iteration0 close 原 accepted=true，current 即该完整值。

第二 trial 原 expected_rows=129248，而返回119840；complete=false、budget_exhausted=true、evaluation_error=null。所有原失败地址是连续整数集合

$\{534,535,\ldots,575\}$，

每项 error 完整同为 `explicit-experiment-time-budget`。norm、mean_height_sum、worst_row、below_original_tolerance 都是 null。这里的 null 不能替成首 trial 的值，不能由119840已完成行推出全局范数上界，也不能把剩余42 stage 写成已数值拒绝。iteration1 close 的 accepted=false，`current` 仍指首 trial 保存的完整已接受状态。

owner final 原记录为：

- accepted_steps=1，directions_computed=2，trial_evaluations=2；
- requested_direction_indices=[0,1]；
- attempted_trial_addresses=[[0,0],[1,0]]；
- stop_reason=`resource-partial-trial`；
- 未访问方向完整集合为2至31；
- 最后已请求方向1中的未访问 trial 完整集合为1至9。

方向0在trial0接受后未尝试其余档，是原正常提前接受控制流；不能与方向1的资源未访问后缀混淆。最终 saved current 的 complete=true、budget_exhausted=false 指此前完整接受状态，不能覆盖最后 partial trial 的真实范围。

原 outer tolerance 为
$2.00000000000000012456318291555971284\times10^{-9}$，
hex `0x1.12e0be826d695p-29`；
root stop 为
$7.99999999999999999055447483647918958\times10^{-14}$，
hex `0x1.6849b86a12b9bp-44`；
root fallback 为
$4.99999999999999969748484640969905465\times10^{-12}$，
hex `0x1.5fd7fe1796495p-38`。
这些原门没有放宽。

原完整 owner summary 身份为137805 B /
`a5bd44340bc1ca6511a9c3f6b5d86440ba6711422511fab4f3ee1f51ad0f96e2`。
本次 reader 返回其中全部实际 owner records 及必要标量，不运输完整科学数组。实际 raw final state 为2067968 B /
`e341aad1f3711614ba1528f0d029c67f747201ac2305fb3bfab28bff39e71dc0`，
原 `state_never_roundtripped_through_binary64=true`。这一身份不允许从 hash 恢复已经清理的状态，也不构成后继完成响应。

## 528.6 replay、四组件与协议：各自未付范围

原 replay 返回 `returncode=3`、`wall_timeout=false`；`independent_fresh_replay_complete=false`、
`fresh_replay_all226_output_words_equal_owner=false`、
`fresh_replay_full_residual_words_equal_owner=false`。这是**未完成 replay 的原旗标**；没有完整比较结果支持“226词不等”或“残差词不等”的数值反证，本文不作此推断。

owner 的 post-components 原对象为：

- `all_requested_components_completed=false`；
- `not_started_reason="original-current-H-final-primal-tolerance-or-replay-not-complete"`；
- `remaining_scientific_seconds_after=12098`；
- 本 call 请求 cap：stages8000、boundary600、endpoint600、audit0（anchor 请求 audit=false）；原 request 的 audit cap1800仍存在，未执行的最终 audit 不能据此计作通过。

| 后置组件 | started | summary returned | 本次真实编译/新来源回执 |
|---|---|---|---|
| full stage576×224 | false | false | paired-digit binding 文件 present=false；returned process records=[] |
| boundary112 | false | false | height-forcing physical compiler binding 未返回 |
| endpoint338×112 | false | false | main physical compiler binding 未返回 |
| independent audit | false | false | main physical compiler binding 未返回 |

所有上述 reader 条目均明确 `compiler_execution_or_success_not_inferred_from_preparation=true`。R522 源已生成不等于 paired-digit stage 已编译/求值，R515 cache 计划已绑定不等于 physical_jets 缓存已执行。这次 owner 未修改的部分成为停止点，不能拿本次整体时间与别次不同轨迹作加速率。

实际 solve-response elapsed=5999.457127904 秒，开始前整体科学钟还剩18097.874651717秒。其子进程 `actual-owner-and-components` 返回0；这个子 exit0只表明其必要记录写出，不意味着owner最后原门通过。pipeline 检查原owner最终容差和replay后返回2，complete=false，原错误：

> RuntimeError: Actual current-H owner final tolerance/replay has not completed

其 `actual_owner_error=null`、`actual_owner_original_stop_reason="resource-partial-trial"`；原 `resource_partial=false` 是 pipeline 自身旗标，不能抹去 owner trial 的明确预算 partial。

本 call 结果已返回但不是协议完整响应：

| 原字段 | 值 |
|---|---|
| call_result_returned | true |
| elapsed_seconds | 6957.425 |
| owner_response_assembled | false |
| protocol_response_returned | false |
| actual_protocol_write_completed | false |
| actual failure location | mode=solve-response，status=2 |
| call result identity | 9254 B / `37f0b3a1c5abf5a34f5f619365d13c68690a9e7dcfdd1292d0e986a18b16fa4d` |
| pipeline solve-response identity | 4440 B / `9cac862d47f01bb60ddec68f51b1d7e2917a0434b2328579eadd6821c9bae1d8` |

worker error 为：

> Error: Current-H solve-response did not complete; real child result/stderr retained

原 fullDN wrapper 在 anchor 的 `client.solve(context["height"], jacobian=True, audit=False)` 抛：

> FloatingPointError: Actual complete finite tail rejected: {'failed': 'Error: Current-H solve-response did not complete; real child result/stderr retained', 'residual': None, 'lastIteration': None}

完整原 science stderr1116 B / `d4513ad8eb6811e1bdf9b2f696a90788be638e82cf3c09e709e1aa142590834f` 已随必要正文返回，没有截掉原错误。其位置为当前实际fullDN源line443调用、当前client line385抛出；不是未知 source guard 失败。

因此，原 `same_live_client` 为 load_client_calls=0、full_driver_solve_calls=[]、original_full_DN_entry_called=false；`original_affine_FD.returned=false`、`original_fullDN.started=false`，没有 last_saved_Newton_iterates、没有实际 original-newton-domain-evaluations正文。原直接/分离两组10方向、3步长层、2 Richardson层、全部适用收缩、$5\times10^{-5}$ FD阈值、prefix17档/$10^{-6}$ RMS/$10^{-11}$ boundary、最终同$H$ fresh audit等责任都没有因这一首call部分进展而支付。

## 528.7 唯一整体钟、规则、quiet 与本次实际清理

### 528.7.1 内外预算分责

实际 job deadline schema 是 `R493-original-full112-live128-job-deadline-v1`，起点 monotonic ns=78969844049，绝对截止ns=19278969844049；total_seconds=19200、原science step320min、job350min、读回清理reserve120s。所有真实$H$、原FD、fullDN共享这一钟，不为call、方向或组件重开。

本次 execution elapsed=6982.009654177秒，actual_exit_code/rules_returncode/science_returncode均1，error=null、external_signal=null、resource_stop=null；rules child已reaped，owned_processes_quiescent=true。尾时磁盘free=91214622720 B，total154993672192、used63762272256。不能把这次停点记为磁盘不足、外部信号或整个19200秒预算超时。确切未完来自上文原6000秒owner内的partial trial，随后未通过原final-primal/replay责任，完整原consumer如实停止。

实际deadline文件839 B /
`4cfcb790e4390f34ba88ac380e851133a478299be6e7d15327255d85f2537ad8`；
execution receipt2477 B /
`ba9a0876ce50694f78dc191383cb171e391676c104f43a7d71676808f539babd`。
source/input准备发生于科学钟之前，rules首次同步和first native factory计入原科学钟。

### 528.7.2 三次真实规则同步

原3b8 rules runner保持2700秒周期、原scientific argv及预算。实际三轮均普通Git push成功，README未变，periodic_sync_failures=[]、README_change=null、science_terminated_for_actual_rule_change=false、scientific_checkout_modified=false。

| round | 原实际read UTC | origin_main_read | published_commit |
|---:|---|---|---|
| 0 | 10:52:16 | `3c0b0833984677bc6e224567da9af4bb45386322` | `596f967f0e86430bd4398ff833de6e303d7a761a` |
| 1 | 11:37:21 | `fe7649afa86974eba204533434e24b7cae903307` | `26a39bb334bb8ee704f260be37cebfa7d8ac8eea` |
| 2 | 12:22:26 | `15c8187c16f9f2668a9881070141a1bcb0c78ad6` | `86aadf6dc1fbeb986ff6d91f2b8ab3ab88250f56` |

原实际两README blobs保持 root `21bd547f56590b7f2dd279d0297efb289a9b2783`、topic `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。这些规则行政提交没有换掉本次科学source/head或补造科学接受。

### 528.7.3 原owned quiet与真实删除

必要正文完整返回三个注册原组的pid/startticks/pgid/sid：

| 组 | pid/pgid/sid | ppid | start_ticks |
|---|---|---:|---:|
| rules | 3350/3350/3350 | 3349 | 7897 |
| science | 3478/3478/3478 | 3350 | 8243 |
| worker | 3479/3479/3479 | 3478 | 8413 |

三者原namespace环境匹配、uid1001。各组实际before/after检查均remaining_owned_processes=[]、unknown=[]、zombie_nonwriting=[]，signals=[]，quiescent=true。另有同uid外部PID1184、1219的environ PermissionError13，它们没有进入已建立own/suspected-own范围、未被信号处理；stat_error=null。本文不把“所有同uid环境都可读”写成已证，也不忽略真实own不可读：原 `unreadable_actual_or_suspected_owned_process_blocks_read_and_delete=true` 仍保。

12:48:36.6805493Z 实际science返回事件已记录quiet。12:48:37.9242565Z 的实际cleanup事件为 `removed=true`，删除的唯一namespace是

`/home/runner/work/_temp/visible-live128-paired-cache225`。

原ownership939 B /
`125f7d0baa02aadc0748ccace191f956f5c02cae5ed85259c6d1fc44d9d23041`，
科学必要文件在namespace外，51983 B/e3d8a314…的完整身份同§528.2。原科学成功不是清理条件；完整必要读回、同源ownership与真实quiet才是本次已满足的条件。**本次不是cleanup_skipped，也不保留可续用的raw final state、factor、packet或stage arrays。** 未来实验须真实重新求同$H$或使用明确允许的实际初猜输入，不得从这里的身份恢复已清科学正文。

## 528.8 本次支付与仍开放的责任

本次实际支付的是：完整原来源生成与输入恢复；一个当前真实$H$的原完整binary64 withJ/R273；128初始完整评价、两个完整lifted方向、一个完整接受试步；第二试步已执行534 stage及其全部原未完后缀；原owner停止、协议拒绝、全必要回传、真实quiet和清理。

仍未支付的是：原owner最后$2\times10^{-9}$容差、完整独立fresh replay、后置全576×224 stage/边界112/混合338×112 endpoint/独立audit、完整live response、原全FD/fullDN和最终same-$H$审计。因此 `fullDN_accepted=false`、`task_completed=false` 保持原值；不由accepted_steps=1、owner子exit0、来源生成或readback_complete改变。

本文不新设接受门，不修改225冻结源，不用本次未运行后置组件推断配对点积/径向缓存性能，也不把原有限prefix问题迁移为准确连续C或完整闭面结论。R527的条件实现结论继续有效；本条R528单独记录其真实第一次完整入口中的已付范围与当前停止点。
