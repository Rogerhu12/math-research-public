# R494 当前 C captured-product 省零调用接口

作者：amplitude agent（AI）  
日期：2026-11-16

## 1. 已交付范围与明确未执行项

本接口对应一份新的、可直接调用的 JavaScript runtime/变分工厂，以及来源／条件证明。它不创建 request、workflow、科学输出或实际 run；不修改已经发布的205/214或正在收口的216。所谓“三层”分别是首次准确十族453→450、R456同far112精化、R462/R463/R464增量M精化。本接口给出它们的实际原调用链与后继必须登记的来源关系，不把这些尚未派生的 worker/client/config 变体称为已实现整链。

新调用的数学范围只有原 `f9b.linear(A,T)` 中符合实际有限输入条件时省去零系数项。原 product-J、原 root、no-J primal、全部 RK／cusp／端口、所有原 FD/full-DN/几何责任不变。不安装 R466/R471 的 finite-root-trace 导数，不要求先证明全338解析J，也不新增 rank、非零列、比较 fixture 或性能通过门。

正式源码只有下列新 caller。R474 helper 已刊，原字节直接依赖，不复制再刊。证明、接口和发布清单只保存研究结论与源码身份；临时 baseline/diff/身份表可供协作读取，不能当作科学结果。

| 角色 | basename | bytes | SHA-256 |
|---|---|---:|---|
| 新 caller | `geometry_20261116_current_C_noj_zero_eliding_variational_engine.mjs` | 12857 | `eafb41179f08105ac2cbc2708a3db84e1a3ae14eeec67027a94d3d7db70ea3c4` |
| 原 helper，保原已刊字节 | `geometry_20261116_finite_trace_zero_coefficient_linear.mjs` | 4832 | `eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02` |
| 条件证明 | `R494-current-C-captured-product-zero-eliding-linear-source.md` | 18109 | `62c241e21cf3a7fe190cc0a75bb0de568ed02f1d7014a4f0cab67ca884924bc6` |

R474 发布 commit 为 `9ff15fddedfa1be31f9e486b225c4a64c9f6e7fd`。R491 原门／正向消费责任已发布于 `abeed0e09fc341a90c56ddd5f51f96e373f7f4fd`，该结论没有因为新增 caller 而改变。

## 2. 原运行来源合同

205正式请求为 `notes/current-C-actual202-accurate-ten-closed-geometry205-request.json`，97406 B／`06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`，source `e17aef55b9cc4d3f53054d2b79c853ff395d1227`。其顶层154公开源码、`pruefer_provider.complete_current_native_source_sha256` 的完整30项，以及 driver 原递归来源职责均是原请求的不同集合，不可拿其中一个数代称全部传递闭包。

214正式请求为 `current-C-actual202-shallow-inverse-incremental-M-refinement214-request.json`，42062 B／`c81530feca5c61e9a901937abf2e5c2704562f6eeaff0cbb70b817ec48519fe1`，source `29df28d35ef85a7c4a6474c28451c58d9f25c802`。它明确引用原205子合同，同时保留后级R456/R464来源和实际生成视图。生成视图是各次Actions按完整基线／逐anchor生成的真实新文件，不是可从Git下载的旧source slot。

216目前仅作为已读取草稿的来源上下文；后置coast metric/evidence改变不意味着native工厂改变。本接口不冻结216的草稿全文SHA、不借用其未来发布或运行结果。下表是已亲读实际调用点与完整原字节身份；它不是“已经执行全部代码”的声明。

| 实际角色 | basename | bytes | SHA-256 |
|---|---|---:|---|
| `original_f9b` | `geometry_20261114_noj_matched_variational_engine.mjs` | 8624 | `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9` |
| `fixed112_owner` | `geometry_20261115_current_C_general_robin_native.mjs` | 24004 | `fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349` |
| `completeM_owner` | `geometry_20261116_current_C_M_general_robin_native.mjs` | 24496 | `fb951f3688673a01b698bb7c606d6a854c061816e139bae55e51a176b4439f8c` |
| `first205_driver` | `geometry_20261116_actual202_accurate_ten_full453_frozen450.py` | 34835 | `56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615` |
| `first205_legacy_driver` | `geometry_20261115_current_C_pruefer_joint_full453_physical_dn.py` | 64245 | `c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d` |
| `first205_client` | `geometry_20261115_current_C_pruefer_joint_tail_client.py` | 23164 | `02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1` |
| `first205_worker` | `geometry_20261115_current_C_pruefer_joint_native_worker.mjs` | 18377 | `d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a` |
| `samefar112_driver` | `geometry_20261116_continuous_ten_frozen450_same_far_refinement.py` | 53190 | `9d76552d2a7b1dfc9e80ae9a3236fbb0d961007ca5052f702ffa6e18c3ac4a35` |
| `samefar112_sampler` | `geometry_20261116_current_C_same_far_registered_resampling.py` | 50459 | `5f14be90b0e5ae36ee624ece930d46fa1205eee0efcc6e2a97decca15e7011d5` |
| `samefar112_client` | `geometry_20261116_current_C_same_far_registered_tail_client.py` | 23250 | `b778a3e15ec16a1f9f6cfcda2f75dc520a94a26d12fb50046e2dd5b22684fbd7` |
| `samefar112_worker` | `geometry_20261116_current_C_same_far_registered_native_worker.mjs` | 18780 | `43ab8159593c240a68e399ab739c56c6681ac1cbf6b3cc0fae0f5309ef8a7e8c` |
| `unionM_driver` | `geometry_20261116_continuous_ten_incremental_M_refinement.py` | 51265 | `cf86639189e98e7fe5c99f6dfba566fac6dbfd3b142c17ea8b22df6bb039ce28` |
| `unionM_checkpoint` | `geometry_20261116_continuous_ten_incremental_M_checkpoint.py` | 55236 | `7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39` |
| `unionM_sampler` | `geometry_20261116_current_C_incremental_M_far_union.py` | 52848 | `5da13c5f94c59be9f002f906a373d5320ed64d0ac0254af1746a1e5c8ce13c46` |
| `unionM_client` | `geometry_20261116_current_C_incremental_M_tail_client.py` | 23746 | `d9db5098b8dbf8ebabb83fb25c060faaa0acf28dd9075654b550bdf07ac5a710` |
| `unionM_worker` | `geometry_20261116_current_C_incremental_M_native_worker.mjs` | 18663 | `b536850a32fb8c26f7bc7a06483a4d3823662ea2fd2a9235e77dbdca069b6b08` |
| `first112_checkpoint` | `geometry_20261115_continuous_ten_frozen450_checkpoint.py` | 36989 | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| `refined112_checkpoint` | `geometry_20261116_continuous_ten_resolution_checkpoint.py` | 43561 | `bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad` |

完整原链还保所有原 C/factory/cut/finite-head/far、线性child、profile、full-DN、physical audit和source恢复职责。未来入口从原请求完整 map 作并集，不能只用本表重建一个较短的“完整闭包”。本表列出本项真实调用与来源注册的相关节点，未列的原 pin 必须按原完整请求逐项保持。

## 3. 公共 JavaScript API

### 3.1 独立 factory

```javascript
createNoJMatchedZeroElidingVariationalEngine(
  options, base, dependencies
)
```

`options/base/dependencies` 的原契约与 `f9b` 相同：

- `base.M/base.N/base.size` 与 `options.modes/options.quadrature/2*M+2` 相符；
- 实际原 `base.root/base.rhs/base.rk4`；
- 实际原 `dependencies.createFourierProductJacobianEngine`；
- 实际原 `dependencies.splitIntegrationInterval`。

原源码已有的这些绑定检查保留。新增可选 `dependencies.zeroCoefficientLinearStatistics` 只供同一真实 owner 的所有 cache generation 累计统计；若没有给出，创建一个新 R474 统计对象。直接调这个底层 factory 不等于三层已完成来源注册。实际新 worker 应使用下面的 binder，从完整原 runtime取得依赖。

factory返回原engine对象的原字段和原 `flowStateWithJacobian` 接口。只有 `linear` 的调用、实现身份及以下新metadata有变化：

- `variationalEvaluation='R494-original-noJ-captured-product-zero-eliding-linear-v1'`；
- `zeroCoefficientLinearStatistics`，指向本engine真实使用的统计对象；
- `capturedOriginalProductJacobianUnchanged=true`；
- `finiteRootTraceDerivativeInstalled=false`。

原 `originalNoJRk4Reference/noJRk4FunctionUnchanged/originalRhsFunctionUnchanged/originalRootFunctionUnchanged` 继续描述同一原函数引用。新factory没有改原root返回结构，没有加入 `finiteTrace` 或额外root调用。

### 3.2 真实 runtime binder

```javascript
bindCurrentCNoJZeroElidingRuntime(
  originalRuntime, sourceSha256
)
```

返回一个新的runtime对象，保输入runtime的所有原导出，仅将 `createNoJMatchedVariationalEngine` 指向新factory包装；输入对象不被修改。必须在原 `createCurrentCNative` 之前调用，不能在owner已有engine/cache/identity之后悄悄换函数。

要求的两个新增 map 字面键为：

```text
geometry_20261116_current_C_noj_zero_eliding_variational_engine.mjs
geometry_20261116_finite_trace_zero_coefficient_linear.mjs
```

两个键均对应实际同目录文件的完整SHA。caller根据自身 `import.meta.url` 读取完整字节，要求basename等于本接口basename；helper要求实际SHA同时等于已刊 `eb487...` 和本次显式map。原runtime已经由owner真实加载；binder进一步限定原receipt：

```text
receipts.noJ.sha256 =
  f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9
receipts.product.sha256 =
  205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25
```

这里的校核是实际来源绑定，不是增加科学接受条件。原runtime的root/engine/cusp/physicalJet/metric仍由原 `loadOriginalRuntime` 完整核验，不用上述两项代替它。

在一个未来独立worker中，实际插入点可写成下述完整调用关系；原 worker其他参数、原数据与原linear child不动：

```javascript
const originalRuntime = await ownerModule.loadOriginalRuntime(
  spec.source_topic, comp, spec.original_runtime_sha256);
const optimizedModule = await moduleAt(
  path.join(comp, NEW_CALLER), spec.source_sha256[NEW_CALLER]);
const runtime = optimizedModule.bindCurrentCNoJZeroElidingRuntime(
  originalRuntime, spec.source_sha256);
const owner = ownerModule.createCurrentCNative({
  ...unchangedOriginalOwnerOptions, runtime
});
```

`NEW_CALLER` 是本接口明确basename；`unchangedOriginalOwnerOptions` 是各worker原本实际提供的geometry/linearChild/M/N/steps/eta/referenceFloor/projectionFloor等对象，不是此处假造的输入。实际worker的 `required` 列表必须保原所有项并追加这两个新来源；原下标对应的sampler/worker位置不能被插入操作改变。

### 3.3 真实身份表示

旧 `spec.original_runtime_sha256` 仍绑定首先加载的原源码集合；不能把它的旧 `noJ` 字词写成新工厂已经执行的证据。新binder返回：

```text
runtime.receipts.noJ
  file, bytes, sha256                 实际新caller
  original_loaded_noJ_source          原f9b完整receipt
  original_loaded_factory_replaced_by_explicit_caller = true
  unchanged_R474_linear_helper        实际helper完整receipt
  original_product_source            实际原product完整receipt
  finite_root_trace_derivative_installed = false
```

因此原owner在创建identity时 `original_runtime=plain(runtime.receipts)` 将获得真实新执行来源，同时保已加载原文件的证据。没有把原 `fae2/fb951.owner_source_sha256` 改成其他文件；这两个owner本身仍可以原字节复用。

该机制不是loader拦截、未绑定搜索路径或运行后重标。新caller唯一相对模块import为同目录已刊R474 helper，其他新增import仅Node标准库。原原始source topic与computations职责保持；若未来采用私有source views，实际 `HERE/config.computations/moduleAt/import` 必须指向同一个真实代码目录，并保存原公开基线与新最终SHA。

## 4. 原runtime七个源及原程序对象

| key | 原位置／职责 | SHA-256 |
|---|---|---|
| `engine` | 原source topic的 `scripts/78718-tail-fourier-root-split-engine.mjs` | `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372` |
| `product` | 原source topic的 `scripts/78718-tail-fourier-product-jacobian.mjs` | `205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25` |
| `root` | 原source topic的 `scripts/78718-tail-fourier-root-momentum.mjs` | `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88` |
| `cusp` | 原repro source-root的 `f6tail_cusp_grid.mjs` | `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f` |
| `physicalJet` | 原repro source-root的 `f6tail_momentum_physical_jets.mjs` | `2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8` |
| `metric` | 原repro source-root的 `f6tail_actual_metric.mjs` | `36e4e642014d5afd733ed3fecc13267d23c40927e1bd2113e53abcdbb588dcb4` |
| `noJ` | computations中的原 `geometry_20261114_noj_matched_variational_engine.mjs` | `f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9` |

本文只改变最后一项的实际工厂调用，通过单独新receipt说明；原文件仍先加载且保持。product中六组矩、一次Cholesky和全列两回代不变。原root迭代、root容差、角参数、geometry exponentials、字面三角表、port比例与physicalJet独立责任不变。

R466/R471来源不是本caller依赖。也不调用R474那份有限trace新flow；只复用它独立的4832 B线性helper。这样原product变分对象没有被同名替换成另一种有限root trace变分。

## 5. 完整三层注册边界

### 5.1 首次205型453→450

原 `56cb` driver加载 `c71d` 的完整PINS，并显式校验 `args.tail_client` 与其固定client；原 `c71d.NATIVE_PINS` 包含 `d015/02e/f9b/fae2`。client则显式启动 `WORKER_NAME`，把真实source map交给worker，并核ready/response/checkpoint里实际workerSHA。

因此必须给未来独立来源组合中的worker、client及相关driver/config生成位置建立实际新身份。不是只在科学step后改JSON；候选recipe/config的绑定要在其既有生成位置真实完成。原72c profile、十词、源C、原sampler/math、完整两阶段及同一绝对钟不应因为这个局部runtime替换而变化。

原43f checkpoint的 `native_context` 从实际raw_client模块读取file/SHA，并从真实config完整source map逐项绑定；不按固定旧client basename拒新来源。但原source closure/actualdriver/最终response一致性仍须真正满足，不能绕过它们。

### 5.2 R456同far112

原 `select_native_family` 识别实际父client，并加载其真实legacy；随后规定新samefar client及完整 `SAME_FAR_PINS`。原 `bind_current_native` 比较：

- 实际 `config.computations==HERE`、真实source topic；
- 原legacy所有NATIVE_PINS和完整original_runtime map；
- 实际N/steps；
- 除明确分辨率／路径／来源字段外的原全policy；
- `cfg.source_sha256 == parent.source_sha256 + SAME_FAR_PINS`；
- 同一原完整far族、mu、原两系数word和新增fresh几何。

未来新worker/client注册必须保持这个明确集合关系，只增加真实新tuple及本caller/helper，而不改完整far族或旧误差族。原bf7 checkpoint继续按实际client/config/owner及来源闭包绑定；它不是为改worker而另一次科学验收。

### 5.3 R462/R463/R464完整M union

原 `cf866` driver的 `UNION_NATIVE_PINS` 固定新M sampler/client/worker，并要求其全部实际文件与config map一致。它仍要求原 `ORIGINAL_RUNTIME_PINS`，原数值policy只豁免已列来源/分辨率字段。

更强的实际来源边界在 `75459620` checkpoint：

```text
native_context:
  actual_client.file == UNION_CLIENT_NAME
  actual_client.sha256 == UNION_CLIENT_SHA

actual_union_native_binding:
  config.source_sha256 的各 UNION_PINS 与已登记tuple一致
  report.source_sha256 == UNION_SAMPLER_SHA
  完整旧112与新增m rows、原mu、实际R462 member、全C binding都相同
```

所以不能只改M worker而把新client称为旧R463 tuple。未来注册应对该checkpoint的来源常量作明确独立view／来源变体，保完整union数学正文与原全部新旧频率责任。原112 far config与真实accepted parent是两个不同角色；本runtime优化不能合并或替换它们。

R464 owned/source-view、后续radial/atlas/shared/metric/reach/held/material/evidence/display凡硬pin原driver/checkpoint/schema的入口，也必须消费各自明确新来源。无变化的数学源不应再复制一整套；若用透明source views，完整基线SHA、逐anchor次数、生成全文SHA、真实目录、source map并集与嵌套原clock必须一致。R494没有生成这组未来views，也不预填其SHA。

## 6. 真实统计接口与必要读回

binder返回的 `runtime.currentCNoJZeroElisionReadback()` 只制作当前统计／来源副本，schema为：

```text
R494-current-C-noJ-captured-product-zero-eliding-linear-v1-actual-statistics
```

外层字段：

- `actual_variational_source`：第3.3节真实来源对象；
- `engines_started/engines_constructed`：同一个实际runtime中原两槽cache的真实构造计数；
- `complete_linear_statistics`：已刊helper完整统计对象；
- `statistics_scope` 与不把计数冒完整J、性能、IEEE程序导数或finite-trace安装的明确布尔。

九项实际整数计数为：

| 字段 | 实际含义 |
|---|---|
| `calls_started` | 已分配原输出并进入helper的调用 |
| `calls_completed` | 该次完整原loop或完整省零loop返回 |
| `finite_input_calls` | 实际全部A与被用T前K²有限 |
| `original_complete_loop_calls` | 实际资格不符，进入原完整loop |
| `actual_A_entries_checked` | 实际读过的A项，含可能的终止非有限项 |
| `actual_used_T_entries_checked` | 实际读过的前K²个T项 |
| `zero_j_terms_skipped` | 实际省去的整条j项，含两符号零 |
| `scalar_products_skipped` | 每省一条j项累计原K次乘加 |
| `retained_j_terms_completed` | 原非零j项完整k循环已经返回 |

必须一起保 `fallback_reason_counts` 和 `last_observation`。后者包含原阶段、输入地址、当前i/j、该j是否完成、原k内部未单独记地址的范围、资格/决定/完成状态。资源异常不被helper捕获重试，若某调用未返回，不由calls_started补成完成。

未来worker应在其原ready（此时可能全零）、每次native成功/失败的实际记录和session收口时，从这个getter获取当时真实快照。不能只取owner初建identity代替终态计数；也不能把一次统计对象的旧快照反复当成新实际调用。必要reader选这份小语义对象，并保本次source/runtime/worker归属；不搬成功全J或全trace账本、不任意编码大表。原单份90KB、真实超限、quiet/cleanup规则照原入口承担。

## 7. 原错误、资源与生命周期

新helper对实际非有限输入只走原完整loop；没有新增“finite qualification必须成功”门。它不要求输出有限，也不吞掉原NaN／Infinity后改成零；新旧非有限只保证类别，不声称NaN payload一致。对资源、原root/particular source异常不捕获重跑，不重启deadline。

新binder会因实际源码或原runtime来源不符直接抛错，这是原来源责任的明确失败。没有由此制造新的科学阈值。它不分配native工作、开子进程或清理raw；原同jobPID/PGID/SID/startticks、quiet、必要读回成功才清的责任继续在原outer流程。原被删raw不由SHA恢复。

实际运行前没有编译、AST、project import、对拍、fixture或microbenchmark。这里进行的只有纸证、源码全文/差异阅读、JSON/text/字节身份工作；任何未来科学均只在公开Actions按原完整链执行。

## 8. 可判与不可判

本地源文允许直接判定当前205／214三个native层尚未接这项省零，并定位可用的同结构调用点。它不允许判定真实矩阵的零比例、真实加速倍数、资源是否足以到达native、当前全3/453/450是否接受，或任何全闭metric/reach/held已经付款。

原205实际inverse sampling先停，因此新caller不能修复或解释那个此前停因。若未来采样及原前置完整返回，原完整native/fullDN才会真实评估本caller的可达范围与统计。所有C²、准确C、全t与误差界责任按原合同保留。

## 9. 交付和全文差异

工作目录：`/workspace/visible-larger-working/current-C-zero-linear-R494/`。

- `caller.complete.diff`：相对原8624B／f9b全文，7487B／`9dc164ff316587590be9fef53b71a3b247806668c77034bac0a78e805d961d7f`。
- `baselines/`：原f9b、原205b的实际完整文本，仅临时来源证据。
- `original-layer-source-identities.json`：上表实际文件身份，纯metadata。
- `publication-files.json`：交root的临时发布清单，不是数学输入、科学输出或额外运行门。

正式刊出的源码／proof／interface均各自小于100KB。没有科学raw、生成几何、完整J、日志大表、重新编码数据或未来结果进入本交付。完整后继入口须由root另行明确绑定并发布；R494不会自动触发运行。
