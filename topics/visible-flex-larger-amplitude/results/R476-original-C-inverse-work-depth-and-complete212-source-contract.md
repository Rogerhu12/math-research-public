# R476：原 C 完整逆像的深度 2 工作实验与 request212 实际来源接口

作者：ChatGPT（AI，geometry）；2026-11-16。  
状态：源码合同与接线已作完整文本核对；request212 尚未执行。本件是原算法的一项明确工作参数实验及其完整执行接口，不另立已由原源支付的包含定理，不预填下一次采样、BVP、450 父或闭面证书。

## 476.1 真实动机及本次唯一科学控制改动

[R440](R440-actual203-complete112-far-and-physical-point-sampling-work-stop.md) 已记录实际203：原 C 闭域、全部112深端族与物理 far 传播已经返回，112条数值边界行也已形成；物理点逆像采样在全局1,000,000次工作尝试处停止。实际完成3个唯一点，完整field occurrence账为0，未启动native或两个BVP阶段。原采样时间为322.259322383秒，声明点采样时间1377.882223950492秒；不能把这次停止写成点采样墙钟耗尽、真实域反证、零向量或trial拒绝。

旧必要reader没有选出原待返点的8个定位字段。R440因此不恢复它未返回的半径、角色、当前stack或已写叶区间；这些原raw已经按该次真实读回清理。我们也不能从3个已完成点推断其下一半径。细分是否受到固有C族宽度支配仍是未证实解释，本实验不将它登记为实际首因。

request212沿完整已发布205链，唯一科学控制差异是：

| 字段 | 完整原205值 | 本次212值 | 性质 |
|---|---:|---:|---|
| `native_sampling.parameters.sample_inverse_depth` | 24 | 2 | 每个原候选闭panel的逆像工作深度 |
| `sample_value_bits` | 32 | 32 | 原相对全宽工作目标，不是接受条件 |
| `sample_max_nodes` | 1000000 | 1000000 | 原全局点逆像工作上限 |

实际采样器仍为 `geometry_20261115_current_C_pruefer_joint_radial_sampling.py`，69,702字节 / `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4`。不派生或猴补其科学函数。原205、207、209已冻结入口不变；它们的首个205子合同仍实际传入24、32、1000000，后继R456/M阶段不会替尚未完成的首采样补点。每次实际结果仍分别读取，不能把203的停止代填到在跑的其他run。

212使用原205的actual202准确投影候选及完整五输入；它不是把203的selected-coast起点或任何partial数值影子当父。原actual202参数来源、准确模板、lambda、全十控制及全部构造责任按完整205原件保持。

## 476.2 原源码已经允许的粗叶出口

以下直接对应原采样器的 `InverseSampler.original_candidates`、`complete_box`、`work_met`、`sample`，不另改任何包含公式。

原候选列表由原panel的向外半径端点范围产生。在这些左右列表确实单调时才使用二分索引；否则穷举全部panel。边界比较是闭的。对一个候选闭片，`complete_box`先做真实工作计数，随后以同一个原piece/radial-range路径计算所有cap分支，要求整个片上的 `w>0`、`radial_speed>0`，以及半径、`w`、`w_r`、`logw`、`w_r/w`全部有限。该步骤没有从一个中点认定正性，也没有挑一个root或cap分支。

只有真实半径严格小于向外下界或严格大于向外上界时，原代码才排除该片。若需要分裂，准确参数中点给两个闭半片；共享端点同时包含，不删缝。有限正盒的工作目标未达到且深度仍小于上限时才继续二分。达到上限后，同一个完整有限正盒原本就进入保留叶，并分别写：

- 原panel/piece、完整闭参数端点、真实深度和所有可能cap分支；
- 完整 `w`、`w_r`、`logw`、`dlogwdr` 包围；
- `numerical_work_resolution_met` 的原真假值；
- `valid_coarse_enclosure_retained`，明确它可能只是合法粗包围。

因此，把原上限设为2只会提前选择原算法本来就存在的这个粗叶出口。它不允许删除未访根片，不允许把未证有限或未证正的盒当作粗叶，也不允许把32bit工作目标未付改写为已付。若到深度2仍不能形成原要求的完整有限正盒，原异常仍向外返回，当前片和完整stack保为未付；不能借本次参数声明跳过它。

整点只有在全部候选完成后才返回。四个quantity分别对所有保留片作hull，再生成其数值词及完整误差回执；`point_count`只在这个返回点之后增加。`work_resolution_complete=false`不阻止一个合法完整点包含返回，原 `geometry.completed` 也没有新增这一工作精度门。

这项包含责任仍限于原整个C/root族。不同quantity的包围或独立选出的数值代表，不因此成为同一准确全局C实现的联合选择；原 `common_exact_global_C_realization_of_all_representatives_certified=false` 保留。后续native使用的有限数值影子与准确族区间是两个明确层次。

## 476.3 工作量能说明什么，不能说明什么

对单个原候选panel，二叉深度上限为$d$时，完整遍历最多访问

$$
1+2+\cdots+2^d=2^{d+1}-1
$$

个片。上限2对应7个，24对应33,554,431个。这是每个根panel的组合上界，不是本次实际工作计数，更不是全部采样必在1,000,000内完成的证明。每点可能有多个完整原候选；原预算、域、有限性、严格正性、字词代表及后继误差责任仍在。

原 `radial_grid` 保持真实576个stage、577个node和 `steps=12` 配置。它以二进制字去重实际RK参数：初始0与1，加每个step的三个真实浮点表达式，再加完整端点表达式。故候选参数数目至多$4\,steps+3=51$，不是擅自把所有表达式当作相同实数而合并。含一次far采样，成功走完整计划前的调用出现次数可用

$$
1+577+576\times51=29954
$$

作保守上界，原字缓存可能进一步合并。这里没有计算本次真实计划，也没有用此数量推断每点的候选panel数。原 `x+h` 可能使实际参数词略超名义端点，源码仍采那个真实半径，不能clip或替换。

降低逆像深度也作用于最初的far点包含。因此，它可能改变far叶族的包围、`mu`、单位行数值代表以及后续所有场词。212从原输入重新计算完整deep、物理far及全部点计划，不复用203的部分或完整raw，不复用旧mu/QPi行，也不把此前源码相同等同于数值词相同。完整112模式、全部候选、取向/误差、双mean、338×112响应及原数学门保持。

## 476.4 两层请求与真正派生身份

为避免重复刊出近97KB的完整合同，212刊一个小outer及标准库composition源。两个原件必须逐字绑定：

| 原件 | bytes | SHA256 |
|---|---:|---|
| `notes/current-C-actual202-accurate-ten-closed-geometry205-request.json` | 97406 | `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4` |
| `.github/workflows/visible-current-C-actual202-accurate-ten-closed-geometry205.yml` | 95760 | `726d97e1aada5d34ddfa949753ce59c6909122d3de8c39bd5a2160fdb8712c36` |

前一项相对topic，后一项相对repo。小outer schema为 `public-actual202-shallow-inverse-complete-closed212-request-v1`、`request_number=212`。它保原件完整身份、真实动机、唯一科学改动、新metadata三源和完整资源/保留边界。

`root_20261116_request212_sampling_work_composition.py` 不导入数学模块。它实际读取上述原205两件，读取当前公开computations中的自身和两新reader，并核实际basename、字节数和SHA。然后deepcopy完整205对象，只允许这些member差异：

1. 逆像深度24→2；
2. `current_BVP_readout` 的真实file/bytes/SHA/schema四项；
3. 原154个source pins全保，另加composition、新BASE、新outer，共157；
4. 当前workflow路径、source_count及明确 `explicit212_composition` 来源对象。

它逐member输出差异清单，再把这些改动逐项复原；复原对象必须与完整原205对象相等。其余raw输入、数学source、recipe、控制、预算及所有门都来自完整原件，没有人工摘要替代原参数。新来源字段写本次实际repository/run/source，不预填未来run。

派生文件保原执行组件真实要求的205 schema、index与namespace：

- `public-actual202-accurate-ten450-closed-geometry-request-v1`；
- `request_number=205`；
- `visible-current-C-actual202-ten450-closed-geometry205`；
- `request205-owned-job-science-deadline-v1`。

这是原callee的来源合同兼容，不是原205字节，也不是原205实验或旧run。实际派生bytes/SHA独立计算，写入原deadline的request身份并在每个阶段继续使用。outer212、唯一改动及本次run/source始终伴随它。没有伪造原hash通过，也没有改原callee全局后仍冒原source。

真实临时文件为 `request212-derived205-dispatch.json` 和 `request212-composition.json`。原workflow随后写自己的实际 `dispatch-request.json`；其内容来自已绑定派生对象。所有后继科学CLI仍逐真实字段构造，包括实际 `--sample-inverse-depth 2`。小outer本身不被当成不完整的科学dispatch输入。

## 476.5 完整CLI与调用次序

三metadata源放在公开topic的 `computations/`，composition自己的 `HERE` 必须就是 `$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations`。临时base必须为本次 `$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205`。原文件只读，新文件排他创建。

```text
python root_20261116_request212_sampling_work_composition.py prepare
  --request <repo>/topics/visible-flex-larger-amplitude/notes/current-C-actual202-shallow-inverse-closed212-request.json
  --base <RUNNER_TEMP>/visible-current-C-actual202-ten450-closed-geometry205
  --computations <repo>/topics/visible-flex-larger-amplitude/computations
```

`verify` 与 `readback` 使用相同三个参数。`prepare` 形成原派生和receipt；`verify` 在科学前由同一原件重新形成metadata并逐字核现场文件；`readback` 在原rules必要读回之后再次核相等，输出一份完整小composition receipt。三命令均只做标准库来源/JSON/字节操作，不运行科学。

科学执行顺序沿原205：原五输入及原公开源码恢复；原180选取/实际202候选准备；完整f12f C与cut两jet；准确十族factory；全部112deep；真实物理far及全部采样；实际candidate/config绑定；原full453；只有原合法父成立时才冻结其真实末十词并真正full450；实际首次construction/atlas/shared、metric、reach及独立held。metric或reach失败没有新变成另一几何阶段的前门。每个原phase和依赖缺失/未开始路径保持。

全新native/RHS/H、112敏感度、338×112端点响应、全部原FD、fullDN、final/audit及真实checkpoint责任保持。没有把453删三行冒450，也没有把有限模型202的成功冒准确连续C闭面成功。

新的双阶段必要入口实际调用为：

```text
python root_20261116_actual202_sampling_scope_two_phase_necessary_readout.py
  --launch-directory <base>/BVP-launch
  --sampler-directory <base>/current-geometry
  [--sampler-result-sha256 <actual result SHA>]
  --candidate-binding <base>/actual202-ten-BVP-input/adapter-result.json
  --computations <actual public computations>
  --out <base>/BVP-scalar-readout
```

它真实load新的BASE，不是只替换回执标签。`sampler-result`不存在时原optional分支仍保缺失范围，不补造父。新outer输出schema为 `actual202-complete-sampling-scope-ten-two-phase-necessary-readback-v1`，原三个GitHub output键仍是 `bvp_summary`、`bvp_summary_bytes`、`bvp_summary_sha256`。

## 476.6 完整未付点字段与输出边界

原 `InverseSampler.sample` 的异常分支已经先把未提交当前片放回stack，再写完整原顺序pending。新BASE只把旧白名单漏掉的下列8键直接选出：

`point_index`、`radius_word`、`role`、`actual_error_type`、`actual_error`、`all_pending_closed_fragments`、`retained_original_leaf_rows`、`complete_point_not_returned`。

键缺失仍是缺失，显式null仍是null；全部pending片保原panel/piece、闭端点和depth，retained区间保原first/stop。没有重新算半径或误把已写若干叶当整点完成，没有经过 `small()` 的列表或字符串截断。旧源继续保为祖先pin；科学source及所有原成功数组的身份范围不变。

两新reader的完整来源、独立schema/frame和各旧调用路径详见[独立必要reader接口](../notes/2026-11-16-complete-physical-point-sampling-scope-readback-interface.md)。其修复范围是212首个205链。原207后置R457动态M的独立旧API也有同型字段遗漏，此次不冒已修；R456及R462/R464整行返回原未付记录的路径不需这项白名单补丁。不得把这张源码范围表当任何在跑分支的实际结果。

本次outer帧为 `BEGIN_ACTUAL202_COMPLETE_SAMPLING_SCOPE_TEN_TWO_PHASE_NECESSARY` / `END_ACTUAL202_COMPLETE_SAMPLING_SCOPE_TEN_TWO_PHASE_NECESSARY`。独立base正常被outer函数调用，不重复打印base main正文。workflow的读回后schema断言和cleanup的schema/marker核验均已改为真实新schema。

单份必要摘要仍最多90,000字节。全部pending保真后若超限，原error70、未写完整marker和raw留至runner销毁逻辑保持；本件不保证最大pending一定可传。未上调限制，未分片/编码大raw，也未删失败地址以伪造读回成功。原数值大数组、全部成功逐叶/逐mode原账仍按原选择范围只给身份与行数，不冒工具逐值独核。

## 476.7 一份原钟、七个原必要scope与清理

| 项目 | 原样合同 |
|---|---|
| job硬上限 | 360分钟 |
| namespace科学资源计划 | 18900秒 |
| 原读回预留 | 2700秒 |
| sampler linear声明预算 | 14400秒、25,000,000 panels |
| sampler point声明预算 | 1800秒、1,000,000 attempts |
| sampling后未来BVP预留 | 3600秒 |
| 原BVP最大进程预算 | 7200秒，再按真实剩余裁剪 |
| precision / Taylor / defect | 256bit / 24 / 12 |
| linear depth / norm | 32 / 1/4 |
| cache / free disk reserve | 65536 / 2GiB |
| representative最高精度 | 4096bit |

原阶段资源会受真实namespace剩余裁剪。sampling内部phase计时仍不包含其输入绑定/runtime setup；原namespace资源计划不是此前所有stage的新增绝对kill钟。真正BVP/闭面owner的原绝对期限、TERM→KILL、wait/reap和quiet语义保留。composition不重开科学钟，也不把残余预算不足变成数学域拒绝。

原7必要scope全保：C、cut、deep-far、实际construction/candidate、sampler及两个BVP阶段、closed/held及其postsolve资源、其他原rules/owner资源。新composition小receipt在原rules步骤之后独立打印 `BEGIN_REQUEST212_SOURCE_COMPOSITION_NECESSARY` /END，不把另一份巨大科学树拆成新scope。

原report继续转发5个有实际bytes/SHA的bounded primary；它们沿原205来源帧名，但新增212事件明确实际本run、outer212、原205合同及24→2。新closed/held/资源3正文仍只在compute，report仅其身份和outcomes；composition完整小正文也只在compute。不能把原frame名称当成原run来源。

清理保原7步骤成功、原完整marker、真实同run/source和所有自有process quiet。新增composition marker只证明不可变metadata已读：schema为 `request212-original205-explicit-sampling-work-composition-v1-readback-complete`，同时核receipt及派生dispatch的真实bytes/SHA。它不能替代原科学/quiet证据。

任何必要读回缺失、错误、超限或owner范围未知都不授权cleanup。主动清理仅本次owned namespace；无artifact、release或Git raw，未读raw只随runner最终销毁，不从身份重建大数据。原规则2700秒真实pull/变更停止与所有原README字节绑定继续执行。

## 476.8 最终发表文件及复核范围

| 文件 | bytes | SHA256 |
|---|---:|---|
| `computations/root_20261116_request212_sampling_work_composition.py` | 14847 | `d98e01cab681471a532194e6a02622bc3cdd3ee655bcbec22caa8df77b790d67` |
| `computations/root_20261116_current_C_sampling_scope_necessary_readout.py` | 55606 | `47d7ec771331f417dffb783a79e02d1ae9720e9ad0a699a72c37cf3031718cb2` |
| `computations/root_20261116_actual202_sampling_scope_two_phase_necessary_readout.py` | 30114 | `6e40dc6365246113d8abc07110582a030b4930195070a71ba08e9872a11bb1e7` |
| `notes/current-C-actual202-shallow-inverse-closed212-request.json` | 9965 | `8803750dbb21bcc24e0809e7bdc4389c567de9b8a10532d52b42b2f7a7ee30bf` |
| `.github/workflows/visible-current-C-actual202-shallow-inverse-closed212.yml` | 99644 | `d1022e74a6217d582f08692b2458bb4d20a3a5dec61ba4dc88907a27e13c3cc0` |
| `notes/2026-11-16-complete-physical-point-sampling-scope-readback-interface.md` | 10057 | `6ddabf6b8fd988274153e443375fc4a04f49b2d63df6c633d851c3d2dcde5b0e` |

除workflow外表内路径相对topic。本件R476的最终字节身份在临时publication manifest列出。manifest、完整diff、原件副本仅为临时交付/审读依据，不刊为科学数据。

workflow相对完整原205的全部差异另交：14,833字节 / `12f339b9dd407faa8677d799a1d02f637666d83fccfecfa474890ad270f9b814`。两reader完整差异分别3,378与4,020字节；composition为完整新标准库源。所有原154pin、完整原205两件和三个新实际metadata文件在Actions再作真实来源/语法前置。此处未执行任何项目模块、AST、编译、科学、测试或fixture；本地只读源码、写文本及核字节/JSON/diff。

本次待支付的是新工作分配下的实际完整采样及其后全部原链。它既没有把粗叶的work目标当完成，也没有把此次参数选择本身当改进证据。真正的完成数量、原未访stack、数值误差、native/BVP返回及准确闭面责任只由下一次真实运行记录。
