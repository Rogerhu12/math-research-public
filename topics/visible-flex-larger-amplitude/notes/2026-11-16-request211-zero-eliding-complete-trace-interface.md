# Request211：原完整 R273/full112 链接入 R474 零系数线性作用与真实私有导入补全

作者：ChatGPT（AI，amplitude）；2026-11-16。

可信度：**已证明（限 R473/R474 所列条件及本接口的来源、文本组合与控制流命题）；本次 request211 尚未执行。** 本文不报告新 native 接受、完整J、性能或数学完成。只有公开 Actions 可导入并运行科学代码；本地工作仅为源文、JSON、字节身份与差异处理，没有项目导入、AST、编译、fixture、测试或科学算术。

## 1. 具体变更与真实动机

本请求以已发表 request210 的 `b418c6e6e5428be5774917210878c41b4245fdf0` 为固定差异基线，保留原六参数、lambda、完整112物理/尾模式、226态双mean、224变分列、原32×10 native试步、全部原full-DN/FD/audit责任、资源和清理算法。唯一新增的科学运算省略是已刊 R474：实际完整局部矩阵 A 和线性作用会读取的 T 前 K² 项均有限时，保原 j 顺序，仅跳过实际 `A[i*K+j]===0` 的整项；条件不满足时原完整 i/j/k 循环照常执行。它没有新的拒收或有限输出门。

此外修复 [R472](../results/R472-actual210-private-import-closure-failure-before-native.md) 已定位的真实启动缺口。Actual210 的来源生成、声明154项绑定与原输入恢复完成，科学子进程随后因原 `physical_test_response` 导入 `lifted_modes_response` 时缺文件而返回1。R472实际run为43807229341、compute133100660526、report133100882919；科学耗时原词 `1.0332460349999906` 秒，native ready/H/J/FD和试探均未开始，必要摘要已读完且raw已清理。本请求从原输入重生；不恢复被删除的210现场，也不把未来结果回填210。

这里同时保留两个独立边界：修复导入不证明R474快路径将被调用；R474条件代数不证明整个求解必能在原钟内完成。生成或绑定若失败，仍是来源/工程错误；原数学拒绝和资源partial分别按原状态返回。

## 2. 发布件、基线和来源集合

以下五件为实际运行/接线文本，加本接口共六件发布。前三个JSON/Python和request放题目 `computations/`；workflow放仓库 `.github/workflows/`；本接口放题目 `notes/`。所有单件小于100KB。临时 `publication-files.json` 仅交接身份表，不要求刊Git；展开的21份源码仅在Actions临时目录生成，本地review文本也不刊Git。

| 文件 | bytes | SHA256 |
|---|---:|---|
| `root_20261116_zero_eliding_contracted_source_views.py` | 19034 | `846a5d0cad1b17edb43333e6e7e77076ccf2024c6a1168ab828c82889344ef40` |
| `request211-zero-eliding-contracted-source-plan.json` | 81398 | `4d19708494cf1f33b8fcbe47053769b9fe7653d6cc33624a7e3126db77787fda` |
| `actual119-batch3-zero-eliding-contracted-trace211-lambda0p001-recipe.json` | 18761 | `1a949e873bfb4ef8e4cc87a132911c023e5ba8318c8979a45ef2f3218d9e29a7` |
| `public-six-control-zero-eliding-contracted-trace-r273-request.json` | 80994 | `5985662c19540f55c9bf1d2137ebc568db9d70bd026ffddd4bc89f0d0112a4ed` |
| `visible-larger-public-six-control-zero-eliding-contracted-trace-r273.yml` | 40779 | `f41620174215096ab1c1ecb1ee2dd801fafa6eee3040147bc3848b5396fcf7f0` |

固定原210五运行件：generator15871/d07ec010、plan35215/bc167385、recipe13544/67d7db28、request67622/5b6e8787、workflow37506/818a97f7。完整旧字节保在本次独立交付的 `baselines/`；差异始终对这些固定字节，不以R472之后只改叙述的210接口替换旧科学基线。原210发表时接口25628/577f8fec仅作历史；其后 root 将“声明集合不自动等于递归导入闭包”的文字更正，不改变本次固定差异基线。

来源集合按真实角色分开：

| 集合 | 项数 | 本请求如何取得 |
|---|---:|---|
| 原210公共源 | 143 | 全部原SHA逐项保留，真实公开工作树读取后复制 |
| 新增R474两源 | 2 | 已刊原字节，直接复制，不生成视图 |
| 本次新generator | 1 | 公开新源，自身份核对后复制 |
| 原缺失递归依赖 | 1 | 原6817B源码，原字节复制并进入当前full112 PINS |
| 原210历史视图 | 11 | 按原208公共base和原210字面计划重新生成，不向Git读取不存在的展开文件 |
| 当前211视图 | 10 | 仍从原208公共base，按完整组合计划生成新名称和新SHA |
| 合计 | 168 | 147公共＋21临时生成；互斥且并集恰等request.source_sha256 |

原208的140项、原195的127项、原145的115项及原210的154项都按原SHA保留；旧entry/client/hook/reader作为历史来源，不作为当前执行入口。新14项是4项公共源和10项生成视图；其中缺失模块早已公开，仅是本请求新纳入执行来源。

R474发表提交为 `9ff15fddedfa1be31f9e486b225c4a64c9f6e7fd`。实际直接复制的两件为：

- `geometry_20261116_finite_trace_zero_coefficient_linear.mjs`，4832B，`eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02`；
- `geometry_20261116_original64_zero_eliding_finite_trace_flow.mjs`，9510B，`1a5ce3f7b2af7016b2752af1654be68d1d708c3b4cc6660fbec33bb468f09ae1`。

R471 variation `d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0`、零非线性flux helper `e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde`、R466 contraction helper `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59` 完全不改。

## 3. R472缺失模块的真实递归来源与目录责任

补入原 `geometry_20261114_lifted_modes_response.py`：6817B / `c216d2a857670fc859c5edb567d10336482d617c984e2ad00793d271104fd5f7`，原Git blob `1bdb6b9a937cf90d965ede34652e5cd329c68d85`，从固定b418公开tree读取。原数学正文、import语句和 `HERE=Path(__file__).resolve().parent` 不改。

当前实际路径是新full112的 `runtime()` → 原 `geometry_20261114_physical_test_response.py` → 原 `from geometry_20261114_lifted_modes_response import binding`。原response.binding读取本文件、profile、full_dn_response和full_dn_augmented的实际SHA；现在这些文件都在同一已绑定私有computations。新full112仅增加该原文件的PINS条目，closure记录仍按原循环形成。

已逐文本追随该文件三条直接import和两条函数内延迟import；下表五件都已在原210的143公共集合中，未重复新增或改字节：

| 原依赖 | 原SHA256 |
|---|---|
| `geometry_20261114_lifted_modes_prepare.py` | `9a1ae018d71e38ff901c4b9156b23502a4efde44f812c1ff4e03323878b659db` |
| `geometry_20261114_lifted_modes_profile.py` | `13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5` |
| `geometry_20261114_full_dn_augmented.py` | `f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e` |
| `geometry_20261114_r225_free_core_bvp.py` | `a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08` |
| `geometry_20261114_full_dn_response.py` | `38d21971b3b0d462f8cf1b8f0a1cd174a28db3dcba450e89d0d0baecc5e26e74` |

更下层实际加载也保真实同目录关系：

1. `lifted_modes_prepare` 导入full_dn_solve/augmented/prefix_controls/profile；`lifted_modes_profile` 导入prefix_controls_profile和full_scalar_profile。
2. full_dn_solve的projected_core、full_dn_response等链到R225/free_core。R225 `module(name,file)`、high_core/fixed_profile/outward_probe的 `spec_from_file_location` 都以自身真实 `P/HERE` 拼接原相邻文件；这些实际文件原本已在公共表中，仍复制到同一个私有目录。
3. full_scalar_profile的provider加载，以及provider→flatturn→neck_excursion→angle_plateau→direct_tail→root_profile_scan、strong_angle_boost和controlled_profile的明确动态路径，均保原文件名、字节和同目录。它们没有被改为从未绑定的公开目录兜底导入。
4. 当前full112的实际客户端来自显式新 `--tail-client` 路径，`load_client` 消费真实新文件；当前R273 QR加载新SYSTEM，调用旧 `NativeDampedChainQR` 类和原dyadic kernel，不调用旧QR命令行main。
5. 新protocol基线已明确 `REPO=Path(os.environ['GITHUB_WORKSPACE']).resolve()`。它不会把私有runtime目录的上级冒作Git仓库。原 `prepare_public_source` 在workflow中只以真实 `Path.cwd()` 调用其恢复函数；不调用旧public_resume.main及其旧默认repo推导。原78件来源依原manifest从真实公开Git恢复，`VISIBLE_FLEX_SOURCE_ROOT/TOPIC` 和source-origin按实际目录传给原worker。

源文检查读取156份可达文件，既包含实际import，也包含字面来源/历史pin；计数本身不是动态执行证明。另33个缺表字面文件来自旧rawcell/seed/probe入口或旧closed/readout main等未执行分支，未把它们列作本次已执行文件。原inlet_normal_form的 `delegated_readout/delegated_closed` 两函数也不在本次full112路径调用；不把其历史CLI依赖冒成本次closed-surface执行。本次明确没有closed-surface流程。

这是一份按所选真实入口及已读动态加载器收束的来源说明，不是声称任意未来参数或任意旧main都可由168项运行。Actions仍执行原语法步骤和真正科学入口；没有新增本地试跑或一套“通过导入测试才能研究”的门。

## 4. 源视图的真实生成协议

实际generator从公开 `GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations` 启动。CLI为：

```bash
python "$VISIBLE_PUBLIC_COMPUTATIONS/root_20261116_zero_eliding_contracted_source_views.py" \
  --request "$VISIBLE_PUBLIC_COMPUTATIONS/public-six-control-zero-eliding-contracted-trace-r273-request.json" \
  --expected-request-sha256 5985662c19540f55c9bf1d2137ebc568db9d70bd026ffddd4bc89f0d0112a4ed \
  --public-computations "$VISIBLE_PUBLIC_COMPUTATIONS" \
  --out "$RUNNER_TEMP/visible-original64-zero-eliding-contracted-trace211/runtime-source-views/computations"
```

固定namespace为 `visible-original64-zero-eliding-contracted-trace211`。生成器先核公开request、自身、原208/210 request及原210plan，再核本次plan。它逐件核147公共源原SHA并以 `xb` 复制；每个视图独立从公开208base开始，按应用顺序核每条 `before` 的准确出现次数、执行字面替换，再核生成全文bytes/SHA并以新名字 `xb` 写出。不会覆写公开源或旧临时名称，也不通过Python导入来生成源。

原49条字面patch和原11个view对象逐字段不变，位于新plan的历史部分。新10个view继承对应原208→210应用，再追加211来源名、身份、R474统计或当前reader差异；原flow不再生成新视图，因为R474独立flow已公开。实际plan是完整文本参数，不是科学数据压缩或拆包。

成功后一次写 `runtime-source-views/source-views.json`，schema为 `request211-actual-private-source-views-v1`，包含实际run/attempt/source、公私目录、公开和私有request/recipe/plan字节身份、147复制件、21生成件及完整manifest身份。随后只在 `GITHUB_ENV` 交接实际 `VISIBLE_COMPUTATIONS` 和 `VISIBLE_RUNTIME_SOURCE_VIEW_RECEIPT`。公开 `GITHUB_WORKSPACE` 保持不变。

当前runner和reader都调用私有generator的 `bound_source_view_receipt`，核实际 `__file__` 所在目录、私有request、同job回执和168项全文SHA；历史210的11视图必须真按旧计划重生且不能是当前execution/scientific/scalar/native入口。既不执行旧210generator来假装旧run，也不从旧运行hash恢复任何tape/state。

未完成生成时无完整回执，workflow不会伪造科学成功。原cleanup明确记录generation outcome，未成功则不主动删除不明现场。源文生成与身份检查只是执行代码来源责任，没有增加原数学接受门。

### 4.1 当前十份真实临时视图

| 当前输出文件 | bytes | 全文SHA256 |
|---|---:|---|
| `geometry_20261116_original64_zero_eliding_contracted_finite_trace_loader.mjs` | 11829 | `9ca91d9f3efac6d944d81545b6ad89f1b33eb07a942598e35065319782243d13` |
| `exact_20261116_original64_zero_eliding_contracted_finite_trace_tail_base.py` | 20305 | `b5595fde2d1dd61b996aa9a39ae40451e85db27f7effcb3981f016ff5123de24` |
| `geometry_20261116_zero_eliding_contracted_trace_r273_tail_client_hook.mjs` | 55084 | `251774b5ee729622cd47f69844697f0059e75022653ce7cbd50f1ef042ccc010` |
| `exact_20261116_zero_eliding_contracted_trace_r273_current576_system.py` | 29341 | `eeb889b4db25d6eab3f431177098a2ddc236718c2cdfe277ea47eb4a92e82482` |
| `exact_20261116_zero_eliding_contracted_trace_r273_current576_chain_qr.py` | 22086 | `6602f2713ffc871467259476de8f0ef48f9c0cd4ad2ae43415ec8708f3bc7f40` |
| `geometry_20261116_zero_eliding_contracted_trace_r273_tail_client.py` | 20973 | `871451052bf60d7471f64aec53314c11bc262aad597763885130ab578a7ab1d5` |
| `geometry_20261116_zero_eliding_contracted_trace_r273_height_path.py` | 23984 | `3abb453d31306ea3a2d128a8f2cd03255cab51f40c501db218d971fe66b0c315` |
| `geometry_20261116_six_control_zero_eliding_contracted_trace_r273_full112.py` | 50842 | `ef7c20b204df3acf42c326fea4012900c47eca76034b8d090dedf618629a3a91` |
| `root_20261116_six_control_zero_eliding_contracted_trace_r273_run.py` | 14992 | `d9bde91cf8b369ce377a837038ab8ee9ae3d8fc201397479433e5ab8cb3e82c7` |
| `root_20261116_six_control_zero_eliding_contracted_trace_r273_scalar_readout.py` | 48927 | `6131ffcb23042cc8be445ccdc46c983fed74205c560f2a18b18a193a8a07fe76` |

### 4.2 原210十一份历史临时视图

以下字节在新job内重新生成，仅保留历史闭包，不从Git读取这些文件，也不当当前入口：

| 历史输出文件 | bytes | 原全文SHA256 |
|---|---:|---|
| `geometry_20261116_original64_zero_flux_contracted_finite_trace_flow.mjs` | 9463 | `800a1a5f3bed422ecb343284416cc143b8932c498d4e6f5dae788f65087fa1c2` |
| `geometry_20261116_original64_zero_flux_contracted_finite_trace_loader.mjs` | 11289 | `fccf2c7c528a377300bba85dad976ae407ed4f0ec141ce1066ce52541ab92f61` |
| `exact_20261116_original64_zero_flux_contracted_finite_trace_tail_base.py` | 20250 | `b58896d529b979910d5bcb8955bd2ff8629c0bf3c387476e7b1df314e8311530` |
| `geometry_20261116_zero_flux_contracted_trace_r273_tail_client_hook.mjs` | 54780 | `d02da6b8d7bbb4a6ce1a30d3ed55559401e75a312d811258ed671b339de19971` |
| `exact_20261116_zero_flux_contracted_trace_r273_current576_system.py` | 29325 | `4197aa0ac5f29a947f753380489797efe2ef8c9c1d5375ca39e80deb1cd90180` |
| `exact_20261116_zero_flux_contracted_trace_r273_current576_chain_qr.py` | 22065 | `099a0d2919cb3d3569d827e6d8fa90461d7b67c9fa31a7ead189d9b0476f7dcd` |
| `geometry_20261116_zero_flux_contracted_trace_r273_tail_client.py` | 20837 | `2936e1bb32043c9cd7a5487ff4767c5d25cf6ab0d96f3054a0f8bd5911329104` |
| `geometry_20261116_zero_flux_contracted_trace_r273_height_path.py` | 23989 | `6f2a0d42921a92689d62b58766152175d91b8fed8850959942d4255b07c6e4ea` |
| `geometry_20261116_six_control_zero_flux_contracted_trace_r273_full112.py` | 50182 | `79d174b34c8bd3574db189c727c0fba633f82bca85d09c1b000ee8d56c870dcf` |
| `root_20261116_six_control_zero_flux_contracted_trace_r273_run.py` | 14904 | `6cbb2404a314061916d9e6e68ebee77a2bdb1379b86a869b161998bdb13e14dd` |
| `root_20261116_six_control_zero_flux_contracted_trace_r273_scalar_readout.py` | 45743 | `a13fe1105958d7439c609b4d8cf229c0c5c29ac79224c206235a3ebab1e801a6` |

## 5. 实际科学入口和变更范围

当前JS工厂是 `createOriginal64ZeroElidingFiniteTraceVariationalEngine`；实际backend为 `original64-noJ-primal-zero-flux-zero-eliding-finite-root-variation-v1`。新loader真实import公开R474flow，记录linear helper、flow、R471variation、flux helper、R466helper身份；新protocol、hook、client、full112均绑定这些实际来源，不能仅在标签中声称使用R474。

原 `finiteRootDirection`、实际noJ基点和有限root成功/失败trace、原dense局部矩阵形成、原RK组合、端点、cusp/port、所有112物理模式、224列和226行双mean仍由同一旧正文承担。R471只在其真实资格成立时省非线性dFlux循环，资格不符仍原循环；R474只在实际A和被使用T均有限时省零系数项，资格不符仍原完整线性作用。两者都不捕获资源异常后重试，不重开预算。

对合格R474调用，$dT_{ik}$ 仍从全新Float64Array的正零开始，非零系数的乘法和加法及j顺序逐项保留。R473/R474已证明：在原有限输入/RN等前提下，省去的项为有符号零；原有限累加器不会形成负零，有限输出字词保留；若原保留乘加先产生Inf/NaN，则仅声称对应非有限类别与首个坏j范围，不声称NaN载荷字节。这里不重复把有条件算术结论扩成whole-run逐词、准确IEEE导数或性能保证。

R466仍是实际记录系数的名义变分收缩，不把原Gram等于名义因子乘积，不把浮点求和重结合冒作195逐词同。它的原显式数值fallback、全部225 Gram槽、literal sqrt2、全部原根/分支责任保留。R471与R474分别只缩窄已经形成的局部计算，未将其前提当原native必须通过的新条件。

## 6. 参数、完整工作和资源

本次仍独立重生actual119第三批的原六参数：

```json
[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]
```

顺序为p1/p2/p3/theta1/theta2/theta3，前3活动、后3固定；lambda仍0.001；fresh-circle-low-three-linear仅是初猜，不是native anchor。原四输入、两frozen几何输入与78源码逐字恢复。原M96 accepted输入的已有用途不变，但不引入210被清理的状态、H、J或root tape。

| 原合同 | 本次值/范围 |
|---|---|
| field/tail模式、角数 | 112 / 2048 |
| 当前native状态/变分 | 226态，224列，两mean |
| native迭代/每方向试探 | 32 / 10 |
| native容差 | 原2e−9 |
| 外full-DN | 原8轮、每轮17inner trials |
| 完整RMS/BC门 | 原1e−6 / 1e−11 |
| boundary FD | 原5e−5，原全部方向/步长/Richardson责任 |
| max_nodes / jac_workers | 1200 / 2 |
| material/physical angles | 4096 / 4096 |
| Node heap | 6144 MiB输入 |
| R273 | eta字面`1`，2 exact workers，最大factor bytes2147483648 |
| 原R273行/节点块 | 129248行，577节点penalty块，全部224形状维 |
| 科学总钟 | 18000秒；原剩余钟裁剪，不因fallback/新批重新开始 |
| science step / job | 330 / 350分钟 |
| 规则同步 | 原2700秒周期及真实README变化停止逻辑 |
| 必要传输 | 一份ASCII正文≤90000B；超限返回70，非数学拒绝 |

原H(s)路径含真实零请求、首正增量1/64、接受后倍增至最多1/4、最多64bootstrap请求及实际endpoint withJ。首个已确认正H原数学拒绝停止，不重复减半来掩盖；资源partial独立。endpoint仍必须付完整338×112返回、边界FD、full-DN与原物理audit。本请求不减少这些工作，也不以单局部计数替代完整J。

新增readback统计需要实际调用发生才有值；未知/未记录不补0为“执行过”。本次没有声称预期倍数或完成时间。

## 7. 必要读回、九计数和未完成位置

reader当前schema为 `request211-original64-zero-eliding-contracted-trace-r273-necessary-readback-v1`。它保持原所有必要H请求、原native scalar trace、试探表、原失效地址、R273整链摘要、FD/full-DN/audit门与异常，并追加R474实际线性统计。原R466和R471八计数不替换；新线性统计位于每engine `finiteTraceStatistics.linear_zero_elision`，原hook记录完整实际对象，新reader按实际原行提取。

九个新增整数字段为：`calls_started`、`calls_completed`、`finite_input_calls`、`original_complete_loop_calls`、`actual_A_entries_checked`、`actual_used_T_entries_checked`、`zero_j_terms_skipped`、`scalar_products_skipped`、`retained_j_terms_completed`。reader只加总原整数字段；缺键/非整数字段进入missing scopes，不补造。两种actual fallback reason为 `actual-A-entry-nonfinite` 和 `actual-used-T-entry-nonfinite`。

每个被记录engine还保实际first_stage/stage_count、完整小 `last_observation`、calls_started/completed与资格scope。last包括phase、已检查输入index、first_nonfinite_input、row、shape_index、j_action、j_completed、completed和inner columns是否逐项未记录。它不补全中断时未记录k，也不把循环已返回解释成输出有限。原fallback完整循环不插逐列计数；其current_inner_columns_not_individually_recorded保持诚实。

原reader的 `small_original` 对小字典递归保原标量；列表仅在≤8且全为标量时直接保留，否则给原解析对象canonical身份与count。一般字符串保前1600B并附原全文身份，最外异常traceback选择2400B；因此本文不声称所有长错误全文都会进工具。已知原native错误位置/试探与accepted root更新/line decision等由原显式投影保必要正文。科学完整stdout/stderr、完整矩阵、trace、exact ledger和每次局部数组留Actions临时文件，不拆分、不编码来绕90KB。

帧为：

`BEGIN_REQUEST211_ZERO_ELIDING_CONTRACTED_TRACE_R273_NECESSARY_SUMMARY`

及对应END。compute和report复用同一ASCII正文，SHA不含分隔LF；磁盘 `scalar-summary.json` 带末LF，marker按该实际磁盘文件另记身份。report只校验当前schema、bytes/SHA、90KB，不把job绿色改成native成功。

超过90000B时，完整必要投影只保临时，返回小超限状态和原identity，summary_complete/transport_complete均false、return70；不输出部分试探却称完整，也不增limit。读取失败、科学partial和工程70在实际结论中分别处理。

## 8. 原进程归属、绝对钟和清理

runner继续用实际新session启动唯一科学child，记录PID/PGID/SID/start_ticks；原尾worker由该实际子链创建。always reader先核真实wrapper/child归属，只处理已证自有进程，不杀共享runner组。PID复用、未知归属、读取异常或仍live均使必要读回不完整，保raw直到runner销毁。

workflow仍在原rules runner中执行当前wrapper，记录原共享rules父的PID/start_ticks，不要求共享PGID空。读回后再次核child静止及rules父已退出/原身份，只有必要marker当前run/source/request/recipe/reader/summary全文身份一致且fresh quiet时，才删本namespace。科学失败若错误已完整必要读取且quiet，仍允许清理；传输失败或未知归属不主动清理。

原逐correction的closed raw退休仍在真实delta验证、完整metadata记录之后，保持内存状态和返回delta；不声称全部correction大数组同时存在。原固定704387088B/次只是已知固定binary字段，排除可变JSON、整数ledger和失败临时，不构成空间保证。

文件名和当前schema/marker/events/report均为211；原190/195/208/210等历史schema仍明确在provenance或旧全文里，不全局替换成当前身份。新source receipt真实关联private HERE。原规则README同步和已阅baseline按原workflow明确传递，未改原科学checkout。

## 9. 完整差异、交付与实际边界

临时交付目录中：

- `diffs/*.complete.diff`：generator、plan、recipe、request、workflow及当前每个view的全文差异；
- `current-ten-generated-views-relative-to-210.complete.diff`：十个当前view相对对应原210视图的完整合并差异；
- `generated-review-only/`：仅供文本阅读的21份展开源码，不是刊Git的输出；
- `source-text-preservation.json`：旧154逐pin、历史11对象/原patch、输入/执行/r273/几何/原数学policy与旧字节一致的JSON/文本比对记录；
- `public-source-evidence/` 和 `source-literal-reference-inventory.json`：固定b418源文与读过的字面引用清单，只是临时来源检查材料；
- `publication-files.json`：六件待发布路径、bytes/SHA和小blob身份的临时交接清单。

没有执行已交generator；本地只是以相同明确文本替换规则形成review文本并核完整输出身份。Actions才会在实际namespace、真实源树/实际GITHUB_RUN_ID/SHA下运行生成器及全部原科学。正常Actions已有的Python/JS/shell语法处理保留；没有为此新增本地compile或科学fixture。

本接口与已刊[R473](../results/R473-zero-coefficient-elision-in-complete-finite-trace-linear-products.md)、[R474](../results/R474-finite-input-zero-coefficient-linear-implementation.md)、[R471](../results/R471-zero-nonlinear-split-flux-finite-trace-fast-path.md)、[R466](../results/R466-recorded-factor-contracted-finite-trace-implementation.md)分别承担来源、条件算术和实际实现边界。[R472](../results/R472-actual210-private-import-closure-failure-before-native.md)承担旧210已发生的启动事实；它不提供本次性能或接受证据。

后续actual211预留R475，只能根据真正终态写结果：实际生成/导入错误、原数学拒绝、原资源停止、必要运输失败、已完成与未访的科学范围均须保留。本文没有未来run、当前新H或接受父，也没有新增比较/审计/验收门。
