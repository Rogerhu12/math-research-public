# 第23次容量操作：旧 low46 辅助盒与 strong 分量诊断

2026-11-26，Astra-larger-e4e2a2bf-20261126。geometry完成来源准备，主会话已核完整说明、小记录及当前八件源码身份，并在同一普通提交中移出下面两份可重算的逐胞报告，共 **1,089,853 B**。原完整源码、输入参数和所有结论保留，精确旧字节有固定公开提交可恢复。本次没有科学重算，也没有把旧成功或失败移植到当前候选。

配套[完整小元数据](../computations/resume-20261126-legacy-low46-box-and-strong-component-retention.json)保两报告的字段清单、原有理端点、充分门、限制、既有标量结论、实际参数、完整资源记录和命令。除大逐胞数组外的原19项/27项字段都可按固定原report恢复；其中非正proposal坐标、Collatz历史、16项两周期、12项对角这四个已生成列表**只保字段名、原数量和已读小字段的canonical SHA**，不复制其数值元素。其他19项/23项参数、来源和标量字段保留。两套213逐胞数组也不转存，遵守README第15条的raw保留边界。

## 1. 两件对象与精确旧字节恢复

| 原相对路径 | 原大小 B | SHA256 | 固定恢复提交 / Git blob |
|---|---:|---|---|
| `notes/2026-11-12-closure-anisotropic-low46-box.json` | 588588 | `34b3556e5a8d96bb1ca9820b7de00e404377bc3c7e5ae7443c8c6da294ea0b91` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `746be553b1730cd73eda81e0e35e4a05e4411e01` |
| `notes/2026-11-12-closure-strong-split-components-r1.json` | 501265 | `ea6a43a3fa7bfcfe9cecc9010f24f5769ce91e3b59757c767ba6e37d5f172fdd` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `eb507234dcd1fd7f896efefbfd6fdf789c4d7de9` |

固定恢复提交为 `11273fd0828c303037de6c11e4cb9d98050e1548`。文件的 Git blob 已从该树的元数据逐项读取。第一件 SHA 由仍保留的 nonlinear-low-far-lift 报告末段 `input_hashes` 原值核对；第二件 SHA 和大小由仍保留的 strong-split-stable-manifest 原表核对。没有整读两份大报告来重新散列。

未来需要精确旧输出的消费者，可在 Actions 的隔离 scratch 中恢复：

```bash
git show 11273fd0828c303037de6c11e4cb9d98050e1548:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-anisotropic-low46-box.json > "$legacy_scratch/notes/2026-11-12-closure-anisotropic-low46-box.json"
git show 11273fd0828c303037de6c11e4cb9d98050e1548:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-strong-split-components-r1.json > "$legacy_scratch/notes/2026-11-12-closure-strong-split-components-r1.json"
```

`legacy_scratch` 为调用者事先创建的独立目录；恢复后核表中 SHA，再显式传给旧消费者。上述命令仅列为恢复说明，本次未执行它们。需要确切历史 SHA 时采用原 blob；新再生的计时、路径、普通浮点提案和运行库细节不保证逐字相同。

## 2. 辅助 low46 盒：完整生产输入与原执行

仅移出 `rows` 的213项。它们由完整 `closure_anisotropic_low46_box.py` 的真实输入生成：所有46低模、cells12至224、精度192，80次普通浮点半径提案和100次权重提案；提案固定为准确 dyadic 后重新用 Arb 外包核每项门。目标收缩提案为 `3/4`，接受门仍为 `4/5`；R23球和远端 `2^-2200` 门均由原源完整保留。U/W 是生成的逐胞盒与权重，不是本次被删掉的外部输入参数，完整原数组仍可按第1节恢复。

| 原相对路径 | 原大小 B | SHA256 | 固定恢复提交 / Git blob |
|---|---:|---|---|
| `notes/2026-11-12-closure-variable-green-low46-v2.json.gz` | 109582 | `17d91d6f73f85076734d2c621e693890d23a22edf7a04b0f2b8c1370e6fec7ed` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `49bd81ca02c6abf9dc4e0882ac5f114f4113bdc3` |
| `notes/2026-11-12-closure-variable-reference-farball.json` | 566768 | `592f43f17fb6c05fe32e4e6c3acda00e7c0b3d18fc8c4393d2d9f981034937ad` | `a93699427718235cb07d70c8f0971e5981dbfbe1` / `993e9ce14b49c8c909eb5b10f797f7bbd956a1ff` |
| `notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3` |

Green 和 ready 的固定恢复提交为8ef38046；原 variable reference 已在第22次容量操作移出，使用其已核 a9369942 恢复链，不把现树不存在的路径当作仍有输入。

原完整 argv 如下；原记录没有显式 `--precision`，完整源默认192，配套JSON也明确保留该默认。

```json
[
  "/workspace/scratch/c0de65fac774/research-venv/bin/python",
  "computations/closure_anisotropic_low46_box.py",
  "--green",
  "notes/2026-11-12-closure-variable-green-low46-v2.json.gz",
  "--reference",
  "notes/2026-11-12-closure-variable-reference-farball.json",
  "--ready",
  "notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json",
  "--out",
  "notes/2026-11-12-closure-anisotropic-low46-box.json"
]
```

原资源记录 exitcode0，wall1.947737216949463秒、峰RSS44640 KiB；报告内计时1.6614909240001907秒、峰RSS41440 KiB。其已付结论仅为辅助的逐点低46投影系统，含完整均值根和线性R18远边界；非线性远图反馈、高频头强迫、外侧cells0至11、真正strong H和prefix拼接仍是另项责任。[R35](../results/R35-low46-variable-strip-anisotropic-fixed-point.md)和[R36](../results/R36-nonlinear-low-far-graph-feedback.md)原文不改。

## 3. strong 分量诊断：显式三个输入和隐式三个输入

仅移出旧完整报告本体；其中 `source_scale_profiles` 的213项是从完整 low 输入复制的 source_factors/canonical_rest 逐胞值，可由同完整源和下列原输入重现。四个其他生成列表按第1节保字段身份/数量及完整原report恢复位置；已有标量失败结论和完整来源不变，不另复制一份生成列表。

| 原相对路径 | 原大小 B | SHA256 | 固定恢复提交 / Git blob |
|---|---:|---|---|
| `notes/2026-11-12-closure-strong-same-tau-four-green-r1.json.gz` | 1525444 | `841c42ff527f2ca3846abf7ede8e9e03eb296a1f979cf7b01f48069197d312ac` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `ef21e40deb2540573962be202c86822d6b8299e5` |
| `notes/2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz` | 753297 | `b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `ebb06e5ed88da8c2a7752d1ffc6aac5245833896` |
| `notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz` | 281853 | `e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `4fa687d3fbe636a0f3ce18181a1b44f8c2e266d2` |
| `notes/2026-11-12-closure-recovery2-centred-four-green-r1.json.gz` | 1521189 | `31c65d6c8053325502542c008720f880d7386cd39168be79ca466851e76bb7ee` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `61ba7aa06b31fa17875a83871a80515c7afda5fd` |
| `notes/2026-11-12-tail-r50-split-middle-r1.json.gz` | 748483 | `4ab9e668ab582fe1916c5ef764dc97ecb81984096ab2da7c57ceeba52d58e078` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `676e4043a2ebd040874211c493285505fadccae4` |
| `notes/2026-11-12-tail-r33-plateau2-density-window.json.gz` | 240282 | `0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9` | `8ef38046e8b04adc6da1093c0730e1fc8747c2c9` / `e0f0dbee70503b828f2722cf56bc2f2884731d4b` |

前三项为原 `--low/--split/--density`。后三项不能漏记：

- 主源从 low 的 `input_hashes` 取原 recovery2 q Green，实际读取其 row families，给模态见证归因。
- `closure_split_joint_io_v2.validate_common` 实际读取并核 q split 来源，保原 q 逐字identity，不把新的strong缩放上界冒作同值。
- 该 helper 还散列原 q density，核真实相同连续strip来源，不能仅保三个CLI文件。

这些读入边来自完整小源码，且与固定8ef树的原75KB low summary和5.5KB strong split summary逐项相等。配套小记录保两summary的恢复身份、真实原输入hash表、完整 q_split_origin 和 continuous_strip_origin。其余 low.input_hashes 的祖先名字是该生成器保留的来源元数据；本次生成器并不再读它们，不能把这些名字误列成已经重新计算的科学输入。

原完整 argv 如下；`--physical-domain-log2` 默认−30，metric target显式31/32，不能回退成源默认3/4。

```json
[
  "python3",
  "computations/closure_split_joint_component_diagnostic.py",
  "--low",
  "notes/2026-11-12-closure-strong-same-tau-four-green-r1.json.gz",
  "--split",
  "notes/2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz",
  "--density",
  "notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz",
  "--metric-target",
  "31/32",
  "--out",
  "notes/2026-11-12-closure-strong-split-components-r1.json"
]
```

原资源记录 exitcode0，wall11.279587030410767秒、峰RSS70836 KiB；报告内计时10.337944623000112秒。报告明确记录 NumPy2.3.5。原641维诊断、427维正因子提案、scaled_underflow_count94623、spectral_radius_float61.059409231403926、condition_2_float252675.1427491033以及非正proposal坐标存在的失败结论都保持原归因：这是普通浮点失败诊断，`mathematical_gates_paid=false`，没有输出通过的 `proposal_rows`。坐标名单自身只存数量/digest/恢复身份。不把特征值、逆矩阵符号或下溢当作精确障碍证明。[R55](../results/R55-two-material-kernels-and-low-near-interface.md)及原two-material说明保留。

## 4. 完整源、相对路径和未来重生约定

以下八件完整小源均在当前树；本次实际读取其完整文本并核SHA，且逐字比对固定11273恢复树。没有只留下source hash而删除源。完整import链包含box经green载入的projective helper，以及component的两层io reader。

| 原相对路径 | 原大小 B | SHA256 | 固定恢复提交 / Git blob |
|---|---:|---|---|
| `computations/closure_anisotropic_low46_box.py` | 6960 | `cde09c4a3f6031c2e9787bb2a215752ee726ddf5c4ecaca45c023504368db045` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `b7245ffcee74eae094a9ccd7ad47f3c696d1b1ef` |
| `computations/closure_real_head_source_enclosure.py` | 20321 | `97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `7fe97d00cdc7271590c8e21bf2f5991c953dcd31` |
| `computations/closure_real_head_green_enclosure.py` | 11896 | `4b2e74d07f678e11631c51cf01831a4c1e588e8d207c144e2f1dace8413022e0` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `d2ecd12c72080f93c435bc43a4de50fcc41043ba` |
| `computations/closure_projective_interval_column.py` | 3594 | `45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `bd0e759f32cc41958d3d0de4279e5c46fbbc56c1` |
| `computations/closure_split_joint_component_diagnostic.py` | 15254 | `6454b8792160c49ce304212ed52aabab64aa3f278898ebb0631a526f2d6c812a` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `5c7589ed3e4b7e64320938b935c3c742e381e5cf` |
| `computations/closure_split_joint_io.py` | 6174 | `cd03e2fc375e19c8b4d291b601e423a37c584a3e4402957c9f377e82b8cce390` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `9c385a667c2e631283618fb39a356fbe85647907` |
| `computations/closure_split_joint_io_v2.py` | 5738 | `6cbcb8cf69a39d8df5d10be35a29b941b47fd66456364eb90fab7bbb22b386f0` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `0665797ae957dbd27becb4985196778e11ccd82d` |
| `computations/strong_resource_run.py` | 1658 | `bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59` | `11273fd0828c303037de6c11e4cb9d98050e1548` / `eaee7a65816b3d6b75946ff18306154d2db8ffc8` |

科学重生只在本公开仓库 Actions 进行。调用者在隔离目录中保留 `notes/...` 原相对名字和完整 `computations/` import目录，把上表输入从相应固定提交逐字恢复，核SHA后运行完整原 argv。原box按路径键检查Green的输入身份；strong helper沿原relative q origin再读文件，不能仅换CLI路径而漏恢复其相对来源。生成的raw留runner，不另改名或塞进本小记录。

原本地Python/python-flint版本、OS镜像及Actions run没有记录，不补造。component只把实际记录的NumPy2.3.5注明。原绝对Python可执行路径按历史字符串保留；未来Actions应使用实际可用Python解释器，同小源/全参数/输入身份重生，再如实记录其自身版本及结果。

## 5. 本次读取与当前任务边界

box只读首12000B及末12000B；component只读首24000B及末12000B。另只读原low-far-lift末12000B核box输入摘要。没有读取或遍历被移出的213数组；通过完整生成器的输出构造核对完整顶层字段清单。四个生成列表的canonical SHA只从这次已读的小元数据计算，不再读取大报告，不重新计算科学值。两个历史summary均小于100KB，允许完整只读，用于隐式输入闭包；历史大gzip的payload没有在这次审查中解码。

对小于100KB的scripts/computations/results/notes做准确路径搜索，完整命中列表留在JSON。命中为旧证明、原资源/manifest、旧nonlinear-lift资源及第22次保留记录；这些引用保持，未来需要原数组时先按固定提交恢复。本条不声称所有大历史文件都已搜遍或没有引用。

当前归一化SO3、direct、supported seed、normal、PCG、所有完整输入、源码、模型参数、永久点历史、待返报告及controller journal均不移出。普通容量整理不改已登记结论，不重放旧科学，也不使当前课题达到完成标准。
