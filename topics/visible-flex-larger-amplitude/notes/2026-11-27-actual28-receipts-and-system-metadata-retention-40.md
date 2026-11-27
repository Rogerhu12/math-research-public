# 第40批空间保全：13份actual28下载回执与4份完整系统生成清单

日期：2026-11-27 UTC。性质：原数据来源、参数与精确恢复记录；不是新科学计算或新的数学结论。作者：ChatGPT /root/construction，GPT-6 Astra Pro，AI辅助。root是唯一refs、队列及当前树删除实施者。

## 1. 本批的精确范围

本批提出从当前树退存下表17件，共 **1,750,110 B**。其中13份actual28下载回执共577,453 B；另外四份完整系统绑定/数组身份清单共1,172,657 B。所有候选都已在同一实际固定树 `1e23dc9cd41e9335379254578ece6db20a3907fd` 逐路径核到完整Git blob和字节数。这里未读取任何候选正文；尤其没有整读或解压四份大清单，也没有读数值数组、ZIP或其他二进制内容。

[完整机器账本](../computations/legacy-actual28-receipts-and-system-metadata-retention-40-provenance.json) 保存全部17条记录、13个真实run及source commit、完整workflow身份、七份完整原请求对象、六份仍保留的完整请求identity文件、74个不同完整源版本的恢复身份、真实写入/读入位置及精确删除条目。未知整文件SHA256明确为null；没有拿文件名、相同尺寸、计数或新压缩值伪造旧摘要。

删除集合只有这17条路径。原源、完整请求/配置/spec、warm/status、已接受状态、科学payload、其他manifest、实际结果与结论均不在本批删除集合内。其他已经实施的退存保持其各自完整恢复账，不被本条改写成当前树仍有原raw。

| # | topic内相对路径 | 字节 | 完整Git blob |
|---|---|---:|---|
| 1 | `notes/public-actions-43615494107-1-nativeband/actual28-artifact-fetch-receipt.json` | 44420 | `e75c26980bc02326adb0be5d79036f49098fc1b8` |
| 2 | `notes/public-actions-43617334081-1-nativeequilibrated/actual28-artifact-fetch-receipt.json` | 44420 | `56abe5c384101941fba749f1047d35952a6fdfee` |
| 3 | `notes/public-actions-43619564953-1-nativesplitprobe/actual28-artifact-fetch-receipt.json` | 44420 | `20c722aef7f0c5600dd90951b4ad9593df6862b2` |
| 4 | `notes/public-actions-43620111146-1-nativesplitband/actual28-artifact-fetch-receipt.json` | 44420 | `061aab9f5c010e0baa0f71bf2f26305f9231218c` |
| 5 | `notes/public-actions-43622149326-1-rawcell0steps/actual28-artifact-fetch-receipt.json` | 44420 | `5b5597e3b1121461a28a44733bdf9c9acd087948` |
| 6 | `notes/public-actions-43623850723-1-rawcell0band/actual28-artifact-fetch-receipt.json` | 44420 | `80870165fad4d18fd9df0dc74d0dedad8ba667fb` |
| 7 | `notes/public-actions-43626121246-1-rawcell0gauge/actual28-artifact-fetch-receipt.json` | 44420 | `2bf6778a61e8e3627c2a002e6de4e639f32632b7` |
| 8 | `notes/public-actions-43630351235-1-stage43probe/actual28-artifact-fetch-receipt.json` | 44417 | `173ac1867fabf69b2e2659ef751417c1c22fbc66` |
| 9 | `notes/public-actions-43634201913-1-directld/actual28-artifact-fetch-receipt.json` | 44418 | `853c427f61173e359134f1d0ea0d33d31997b3f3` |
| 10 | `notes/public-actions-43634889730-1-directld/actual28-artifact-fetch-receipt.json` | 44418 | `78f9e785371dd16fb857d405fad7d51e853126dc` |
| 11 | `notes/public-actions-43636504089-1-directldtrial/actual28-artifact-fetch-receipt.json` | 44418 | `c054399c7395da63a1a152163ffb151cbb38320f` |
| 12 | `notes/public-actions-43637356027-1-dampedchain/actual28-artifact-fetch-receipt.json` | 44418 | `cb694cf91a6ee68eeb92102704c23dbad67b6340` |
| 13 | `notes/public-actions-43640772654-1-original576damped/actual28-artifact-fetch-receipt.json` | 44424 | `4c0f07d3646a27f98be9ecd70fd6701ca9f654ce` |
| 14 | `notes/public-actions-43634889730-1-directld/rawcell0-direct-ld-correction/input-binding.json.gz` | 335715 | `0c750ac433c3b63676bdf7605e6435867fa90fec` |
| 15 | `notes/public-actions-43637356027-1-dampedchain/native-damped-chain-qr/input-binding.json.gz` | 335715 | `0c750ac433c3b63676bdf7605e6435867fa90fec` |
| 16 | `notes/public-actions-43623850723-1-rawcell0band/rawcell0-step-equilibrated-correction/input-binding.json.gz` | 163834 | `582cf14113591e9f06601734a5d34507f2d830a1` |
| 17 | `notes/public-actions-43623850723-1-rawcell0band/rawcell0-step-equilibrated-correction/new-system-array-identities.json` | 337393 | `ee32358a8273840f863763bbd4d4e214b746b85a` |

两个335,715 B的gzip确实具有同一Git blob。它们仍是两个不同run路径：这一字节事实不合并actual54和actual57的方向、目标、时间或实际验收结论。

## 2. 下载回执为何是生成的行政记录

13个原workflow实际调用同一个完整取件源 `exact_20261114_fetch_pinned_public_artifact.py`，其源SHA为 `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`、28,006 B、Git blob `8ee390d0c1449a6a532d72158172af278f1c7cf3`。本次在13个各自真实source commit的目录元数据中核到了这个同一完整对象，没有用当前同名文件代替原版本。

原完整PIN和六个必填CLI参数都保留：

| 参数 | 原值 |
|---|---|
| `--run-id` | `43611175099` |
| `--artifact-id` | `14120548264` |
| `--artifact-name` | `visible-mainline-nativecorrection-43611175099-1` |
| `--expected-size` | `235561097` |
| `--expected-sha256` | `0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee` |
| `--out` | 各原workflow的真实RUNNER_TEMP路径或明确的VISIBLE_CAPTURE28变量；两份完整原命令模板与逐run对应均在账本中 |

取件源的 `main` 先核公开artifact元数据及完整archive，安全提取全部文件；然后写出schema、PIN、实际source/run、UTC时间、下载/完整提取清单、runner路径及发布事实。该源不导入数值包。其 `_pinned_public_artifact_receipt.json` 最后随验证后的目录发布，原workflow再原字复制为这里的 `actual28-artifact-fetch-receipt.json`。这份回执不是235,561,097 B的archive本体，也不是原576段J、基态、残差、H、sigma、cut/far数组。

回执含真实时间与运行路径。重下同一archive会产生新回执，不能声称重下就重造了旧回执的每一个字。**旧回执的精确恢复方式是完整固定Git对象。** 本次无需新下载、新Actions步骤或额外科学扫描。

原actual28 result仍为 `native-correction-capture/result.json`，完整SHA `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`，原source commit `6bd52b446241be53e8842d4db5a24f9c2069e6e5`。完整J raw SHA `394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19` 继续是该原数组的身份；没有用回执身份替代它。

## 3. actual42两份生成清单的实际写入点

完整 `RawCell0StepSystem` 读取原actual28以及actual41全部原步捕获。它先核原result、source、spec、summary、完整数组描述、chunk字节、全部schedule/cell映射；actual41的868个局部J与未改的504个原J组成1372段系统。这里没有重新计算ODE或J。

`exact_20261114_rawcell0_step_equilibrated_correction.py` 的真实写入顺序为：

```python
B.write(out/'input-binding.json', system.binding)
report['bound_new_system_arrays'] = system.export_inputs(output)
B.write(out/'new-system-array-identities.json',
        dict(new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
             arrays=system.arrays,
             complete_stage_blocks=system.J_rows,
             complete_large_J_is_a_virtual_stream_not_a_duplicated_array=True))
```

`system.binding` 是完整来源和映射：原28绑定、actual41原文件/源/hash、各原步schedule、旧新节点/段索引、全部块来源及字节摘要、raw数组摘要与有限模型范围。其cell记录含schedule和索引等数值元数据，不能称为毫无科学含义的杂项；但它没有序列化全部J、状态或方向数组值。相应完整数值payload通过 `export_inputs(output)` 另行导出，原捕获的数组与chunk又在完整输入artifact中独立保存。

`system.arrays` 的值是shape、dtype、order、byte count、raw SHA和virtual-stream标记。`J_rows` 为每个实际stage保完整新旧stage/step索引、来源、bytes和SHA。337,393 B的身份清单是这些完整描述符的生成展开，不是一个新的J数组文件。本批不删对应output-array-manifest或任何数值payload。

该系统的完整identity为 `e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521`。其actual42数值失败结论与来源均保持原义，不因清单退存而升级。

原writer写的是未压缩 `input-binding.json`。真实actual42 publisher是9,803 B源，SHA `3774a67e8456229659f73da1a06fa3e2c70e3368778a6239a57d7f8f05f091a1`、blob `3f38c5cfe57a5a9abeeca1df0b76c592baa4f661`；它对超过1,000,000 B的JSON/JSONL/log使用 `gzip.compress(..., mtime=0)`，另加 `.gz` 后缀。因此这里的163,834 B公开件是原JSON的透明gzip，并不是原writer原本采用了一个新的文件定义。

## 4. actual54和actual57完整binding的实际写入点

两次入口都构造同一个完整 `RawCell0DirectLDSystem`，然后执行：

```python
report['input_binding'] = B.write(
    out/'input-binding.json.gz', system.binding, compressed=True)
```

其绑定包含完整嵌套原1372对象、actual54新direct原结果、完整source/summary/manifest/stage描述、全部块和旧新节点映射、J raw摘要、所有未改非J数组摘要及精确有限模型身份。数值数组和方向仍由独立payload/checkpoint保存。新direct矩阵identity为 `76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999`，不冒原576或更早的 `e929e642…` 矩阵。

原B.write对compressed=True采用完整JSON、最终换行、`allow_nan=False`及mtime=0的gzip。两份公开gzip同blob的事实与[actual57完整原读回及字节审计](2026-11-14-actual57-damped-chain-QR-and-original-exact-readback.md)一致。该已刊小记录给出的whole compressed-file SHA为：

```text
32cb5a0b92ab4ce642b65c0b75ba010ff26dcab5cbf77b1b847b5b469ea5279f
```

本次只读这份小记录，并独立核两路径的Git blob/size相同；没有整读大gzip来重新求该SHA。其余候选未从小记录取得的whole SHA继续为null。

actual54的原计算已生成方向和完整读回，但后继trial因把旧28 `result.json` 写成 `result.json.gz` 而在native调用前失败。actual57则确实完成十次原no-J求值而均未严格下降。两者的失败性质不同，完整原记录继续分别保留。

## 5. 历史读数器确实仍需要完整binding

不能把“生成元数据”写成“任何程序都不会读”。本次已读三个真实历史consumer交界：

- direct-LD trial与damped-chain trial按原result的 `input_binding.file` 取件，核whole SHA与bytes，并把完整JSON值与重建的expected binding以及full/restricted checkpoint绑定逐项比较。
- 原逐原步trial显式读取 `input-binding.json`，并与完整重建绑定及两个checkpoint核等。
- 这些原guard没有删除、放宽或用布尔替换。后续若确实需要运行旧reader，必须先把完整旧件恢复到它实际需要的路径。

actual42恢复先取回本表精确gzip对象，再在隔离恢复目录透明解压为旧reader需要的 `input-binding.json`。不能只把gzip改名，也不能把compressed SHA称为原JSON SHA。actual54/57原逻辑文件名本来就是 `input-binding.json.gz`，应完整恢复该gzip。这里未取得的raw JSON摘要不编造；精确的已存Git对象身份仍完整保留。

## 6. 完整参数与科学输入留存

13个run的实际source commit、workflow完整bytes/SHA/blob与真实状态都在账本中。前七份旧 `public-mainline-request.json` 已从各自原commit完整取回，原对象完整放入账本，原raw文件的SHA与Git blob另记。它们有并行prefix lane时，整个请求对象照录，未只留下与当前收据同名的一小部分。

后六份完整request identity仍在各原公开目录；账本逐份绑定完整path/bytes/SHA/blob、其中完整 `request` 与 `source_sha256` 的JSON位置，以及原request文件SHA。**saved identity包装文件的whole SHA与其中声明的原request SHA是两个不同身份，不能互换。** 原workflow中的全部CLI及source位置也保留；本批不改任何参数。

已有[第27批完整参数账](../computations/legacy-generated-manifests-retention-27-complete-parameters.json)仍完整保留（63,501 B，SHA `d941f0d1e02678d81ce64cb85f567083203ebee76444c737609db443e1c58c2e`，blob `43ec88a8e537b158c5281128c771a9bacc85c73f`）。其完整native intent、全部input/runtime config与原request/source清单继续作为完整原参数来源，未用本条摘要替换。原180,567 B step spec、145,192 B direct gzip spec及其正确source/输入身份仍不在本批候选中。

actual41原完整artifact为run43622149326、artifact14124209116、349,636,774 B，ZIP SHA `356d9d81959739a22e9347d7ceba6fd4880ad61db70dca73096a4c5b71dc73a8`，原result SHA `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf`。

actual54原完整artifact为run43634889730、artifact14129522378、457,357,361 B，ZIP SHA `df3a54716ecbed8645783373657f7e40b08429173ca976efc73ecc7e8ce5f819`，capture result SHA `e60da64312819a87388cfa96c209fc9188dca02c0ab055cbcc934f3507888ac6`。其完整新J、full1373方向和577限制仍由原输入和原payload定义，本批不删它们。

[第37批actual41下载收据保全](2026-11-27-actual41-eight-download-receipts-retention37.json)仍保68,987 B完整账，SHA `ebb79d44069b4068b8cc6823448f62a4aa2c3c8d39589a6e992f993ce9781cc8`。该批针对下载收据，不是数值数组；本条不把其已退存路径误称为仍在当前树，也不把它冒成恢复全部数组的证明。

本条只保证指定17件的固定Git恢复，以及全部原输入/参数/源责任不被删除或更名；不保证外部artifact服务未来永久在线，也不声称缺失的科学payload能由摘要自动还原。若未来请求旧科学replay，其完整原payload和所有原guard仍须真实满足。这不是现在增加的独立准入门。

## 7. 保持真实的运行结论

下列结论来自仍保留的完整小note及实际run元数据；它们不是本次重新计算结果。workflow的success/failure也不直接等于科学成功/失败。

| Run | 原request | 实际workflow conclusion | 保留的实际范围 |
|---|---|---|---|
| 43615494107 | 20261114-public-large-core-mainline-34 | success | Complete saved band factorization/readback returned; the original-scale exact defect remained huge. No accepted native tail or nonlinear trial is inferred. |
| 43617334081 | 20261114-public-large-core-mainline-36 | success | The complete equilibration workflow returned, but no usable original native Newton direction was obtained. No nonlinear trial was run. |
| 43619564953 | 20261114-public-large-core-mainline-38 | success | Four short Jacobians and four independent no-J half windows completed with the recorded old exit/mean words preserved. The planned probe stop was not native acceptance. |
| 43620111146 | 20261114-public-large-core-mainline-39 | success | The new 578-stage system completed factorization and full exact defect readbacks; its original-scale defect remained huge and refinement worsened it. No nonlinear trial followed. |
| 43622149326 | 20261114-public-large-core-mainline-41 | success | All 868 original-step local Jacobians over 72 rawCell0 stages were captured; the published audit records old exits and means word-preserved. This did not solve the new global system. |
| 43623850723 | 20261114-public-large-core-mainline-42 | success | The 868 captured local blocks plus 504 original blocks formed the complete 1372-stage system, but the direction was numerically unusable. The contemporaneous note distinguishes published small reports from large-array audit not then performed. |
| 43626121246 | 20261114-public-large-core-mainline-43 | success | The complete node-G solve and original-coordinate exact row readbacks returned; the best original defect remained large. No new ODE/J, nonlinear trial or native acceptance was claimed. |
| 43630351235 | 47 | success | The specified saved stage43/step11 four-stage local matrices and same-run short Jacobian were captured. The retained note separates this byte audit from the independent subsequent exact-action calculations. |
| 43634201913 | 52 | failure | The run failed while writing the complete specification at the original text-size limit, before native or direct-LD numerical workers started. It is an input-record transport failure, not scientific rejection of the maps. |
| 43634889730 | 54 | failure | All 868 direct-LD maps and the complete new 1372-stage direction/readbacks completed; the linear defect remained huge. The subsequent trial launcher used the wrong original28 result pathname and failed before all nonlinear trial calls. |
| 43636504089 | 55 | failure | All ten original nonlinear attempts were rejected inside the original evaluation: nine momentum-branch rejections and one momentum-Newton line-search failure. No complete trial norm was returned, no selected state was accepted. |
| 43637356027 | 57 | failure | The complete eta=1 damped chain direction was followed by ten finite original no-J evaluations. Each norm equalled the recorded base norm and was rejected for no decrease; no accepted state resulted. |
| 43640772654 | 59 | success | The complete original 576-stage matrix direction and both exact readbacks were recorded; the first original nonlinear step at alpha=1 was accepted. This was one decrease, not completion of the full native solve, final height Jacobian or fresh audit. |

每行完整原note的path、bytes、SHA、Git blob都在机器账本中。特别保留actual52的spec写入失败、actual54的旧输入路径错误、actual55求值内部失败、actual57完整norm不降，以及actual59真实首步下降之间的区别。

## 8. 已核生成/消费源码的精确身份

| 角色 | 完整源 | Whole SHA256 |
|---|---|---|
| actual28取件核 | [exact_20261114_fetch_pinned_public_artifact.py](../computations/exact_20261114_fetch_pinned_public_artifact.py) | `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` |
| actual41取件适配 | [exact_20261114_fetch_pinned_rawcell0_steps.py](../computations/exact_20261114_fetch_pinned_rawcell0_steps.py) | `328403614476954cddfdc9b7c764e27d668d44042f8da3efa63cb2e8076c5b79` |
| actual54完整取件 | [root_20261114_fetch_pinned_direct_ld54.py](../computations/root_20261114_fetch_pinned_direct_ld54.py) | `96e07ffe20e8d28f15d77c1f2acca1ff9d60b5646de1144978b0add777b82331` |
| 原捕获绑定与JSON/gzip读写 | [geometry_20261114_native_captured_band_correction.py](../computations/geometry_20261114_native_captured_band_correction.py) | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` |
| 完整逐原步系统构造 | [exact_20261114_rawcell0_step_system.py](../computations/exact_20261114_rawcell0_step_system.py) | `fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81` |
| 42清单写入 | [exact_20261114_rawcell0_step_equilibrated_correction.py](../computations/exact_20261114_rawcell0_step_equilibrated_correction.py) | `30a467e8f08d73fcdcd8a69b2d911e0d9f57489c3397c21c775ed1ec4f6cabe6` |
| 完整direct-LD系统构造 | [exact_20261114_rawcell0_direct_ld_system.py](../computations/exact_20261114_rawcell0_direct_ld_system.py) | `b64b6ed8b387834b5cc9332675127a1dcbb15a317c3400f5b768d18cdbdf5a8e` |
| 54绑定写入 | [exact_20261114_rawcell0_direct_ld_equilibrated_correction.py](../computations/exact_20261114_rawcell0_direct_ld_equilibrated_correction.py) | `42e10320252935015c65bbc34579947e559182bb1b2a74ca1aa13a6597c064b9` |
| 57绑定写入 | [exact_20261114_native_damped_chain_qr.py](../computations/exact_20261114_native_damped_chain_qr.py) | `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33` |
| 旧逐原步trial读入 | [geometry_20261114_native_rawcell0_step_trial_replay.py](../computations/geometry_20261114_native_rawcell0_step_trial_replay.py) | `f944c877a47013621a9753f2769e3687f6d6a4b2daf5d91fd6dd1021b102fa1e` |
| 旧direct-LD trial读入 | [geometry_20261114_native_direct_ld_trial_replay.py](../computations/geometry_20261114_native_direct_ld_trial_replay.py) | `41976f4298d361ad06d0753698eebcd5149d3ce56410904768d6426610c2984e` |
| 旧damped trial读入 | [geometry_20261114_native_damped_chain_trial_replay.py](../computations/geometry_20261114_native_damped_chain_trial_replay.py) | `ebd3110e7ba9b2edeca155370d2c7fd6f02d3757ae285379d54a2b4a39793ccd` |

机器账本另保74个不同完整源版本的原commit/blob/size与已知whole SHA。read_text表示本次或本会话实际已读的小完整源正文；original_request表示原完整请求声明的SHA；unknown保null，不假装做过全文验证。未改动这些完整源，也未以此表替代源码。

actual42、54、57各自publisher的完整身份分别保留。对于其他收据，原workflow/source commit中的完整publisher继续存在；没有用后来的新版publisher替换早期发布时的来源语义。

## 9. 当前warm入口的直接依赖边界

复用已刊[第34批完整源复核](../computations/legacy-condensed-intents-retention-34-provenance.json)的精确范围：`rebuild_axisymmetric_so3_warm`→`reproduce_and_solve`默认实现→`rebuild_fullclosed/rebuild_closed_warm`→完整pulse/assembly/Hold/mode warm。该五源身份和21项recipe源pin已在原完整review中核过，本条明确引用该完整记录，不冒本次重新跑过warm。

其原历史raw seed仍是commit `60321451c058c6a51da58c37ae5ec6f2d1145f74` 的 `notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz`，whole SHA `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`。本批17件既不是该seed，也不是当前warm/config/status。这个直接源链结论不推广成“所有历史诊断永远不需要旧binding”；第5节的历史恢复责任完整保留。

## 10. 精确恢复与实施边界

精确恢复以机器账本的同一固定commit、候选完整路径、Git blob和bytes为准。可按该固定树直接取回完整blob到隔离恢复目录；不能把新生成的摘要放进旧basename，也不能仅保存目录名或hash后宣称原payload已还原。原件所在Git历史不重写、不force，不把新下来的receipt当旧receipt。

本次只做小源/请求/说明全文与Git目录元数据读取、V8纯文本/JSON/SHA处理。没有科学import、F/J/root、数组运算、精确有理/区间算例、AST/compile新声明、数值fixture、新Actions重跑或额外扫描。没有读取17个候选正文。root若实施，使用机器账本的精确17个delete_entries；所有其他路径保持原样。

## 11. 本批交付

账本与本note均完整小于100,000 B，远端未引用blob先保护。原始候选gross减去这两个完整新增记录就是本批净空间收益；原科学源、全部参数和结果范围不为容量目标裁减。构造代理不改refs、不删除tracked文件，也不自行触发队列。
