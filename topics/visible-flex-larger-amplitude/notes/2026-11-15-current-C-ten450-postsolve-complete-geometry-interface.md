# R429：真实 453→450 后的完整几何编排接口

AI 辅助源码接口；2026-11-15。本文件与 [R429 条件组合证明](../results/R429-same-job-ten450-postsolve-geometric-responsibility-composition.md) 配套。当前没有新请求号、实际run、accepted450、$K$、$\tau$、$\eta$ 或新计划参数。只完成独立可执行源码，不改正在运行的193。

## 1. 最小实际接点

原冻结入口：

| 角色 | basename | bytes / SHA256 |
| --- | --- | --- |
| 原两阶段driver | `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py` | 33794 / `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` |
| 原两阶段launcher | `geometry_20261115_continuous_ten_full453_frozen450_launch.py` | 19366 / `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` |

driver的原 `run_phase` 在每阶段原fullDN真实通过后捕获自己的五份原件。第二阶段得到真实450时，`adapter-status.json` 中有 `actual_final_checkpoint_directory` 和该 `checkpoint.json` 的原receipt；最后 `finally` 关闭共享raw owner并记录所有lease已释放。launcher在自己的 `result.json` 记录原driver receipt、真实exit及进程组静止。

这些临时文件仍然存在。driver／launcher未删除它们；旧193 workflow最后清理步骤才调用 `shutil.rmtree` 删除整个请求namespace。因此新组件应放在**旧launcher返回、原owner静止以后；原namespace清理以前**。不须让旧worker继续存活，也不重新解两次BVP。

## 2. 新增文件与冻结身份

| 目标路径（相对课题） | bytes | SHA256 |
| --- | ---: | --- |
| `computations/geometry_20261115_current_C_ten450_postsolve_geometry.py` | 43042 | `84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a` |
| `computations/root_20261115_current_C_ten450_postsolve_necessary.py` | 23903 | `79296f4ff205542cf99091ada7fd9a7055e68ffb04173bd242592769c8d4ca2f` |
| `results/R429-same-job-ten450-postsolve-geometric-responsibility-composition.md` | 15725 | `01f0554896cb7ea048e480584f8af3ec609d8c7ed1017062776bea614f3c10ab` |

两件新Python文件只导入标准库。runner通过CLI启动原科学消费者；reader只解析原JSON／字节／进程元数据。没有本地执行、科学import、AST、编译、benchmark、fixture或数值对拍。

新runner schema为：

```text
current-C-ten450-same-job-postsolve-complete-geometry-v1
```

输入为该schema加 `-input-v1`。新reader schema为：

```text
current-C-ten450-postsolve-one-necessary-conclusion-v1
```

它固定核上表runner SHA，没有借用190、193等旧请求号常数作为新输出身份。

## 3. 输入合同：实际路径与全部显式参数

runner只有两个CLI参数：

```text
python -u computations/geometry_20261115_current_C_ten450_postsolve_geometry.py \
  --input <actual-postsolve-input.json> \
  --input-sha256 <actual-input-SHA256>
```

输入JSON必须有以下实际字段；它们不是本文已选择的值。

| 字段 | 类型／来源 |
| --- | --- |
| `schema` | 上述独立input schema |
| `namespace` | 当前 `RUNNER_TEMP` 下实际原请求namespace |
| `upstream_launch_directory` | 真实旧launcher目录，内有 `result.json`、`full-BVP/adapter-status.json` |
| `upstream_result_sha256` | 可选；已知时明确核本次launcher结果字节。省略时仍读该固定实际文件并绑定其来源、run、receipt和真实gates，不接受外给成功旗标 |
| `job_deadline`、`job_deadline_sha256` | 原实际 `current-BVP-deadline.json` 及SHA |
| `geometry_directory` | checkpoint原native绑定实际消费的同job geometry；结果bytes/SHA必须一致 |
| `continuous_e_directory`、`continuous_e_result_sha256` | 同一个原C目录／原result字节，通常namespace下 `continuous-E` |
| `computations`、`proof_directory` | 当前冻结源和已刊proof路径 |
| `source_topic` | 当次真正恢复的78原源topic根，R409原runtime实际消费 |
| `out` | namespace下独立、尚不存在的输出目录，须与原BVP目录为互不包含的分支 |
| `construction` | 只含 `cut_correction_width`、`cap_height`、`fixed_cap` |
| `construction.fixed_cap.markers` | 完整marker列表；每项沿R413原 `upper/center/radius/height`，不自行补旧 `index/kappa` |
| `metric` | 第5节全部原参数 |
| `reach` | 第5节全部原参数 |
| `resources` | 第6节全部资源参数 |

新的construction不含自选cuff；原R413从绑定C取得真实cuff。$W$、$H$和marker有限词沿R413原数值／准确lift合同；source不替它们选值。

runner先读取实际原launcher；若它没有返回原accepted450或owner没有静止，记录 `upstream_stop` 和五阶段未启动，不尝试从旧摘要重建 field。成功时，继续核：

- 原launcher／driver source、当前 `GITHUB_RUN_ID/GITHUB_SHA`；
- 当前deadline文件的bytes／SHA与原launcher `actual_job_deadline` receipt相同；再核原schema、run、source和recipe，不接受同job另建start／预算文件；
- 原adapter receipt和两阶段顺序、原main退出及接受；
- 原native owner已关闭、lease已释放、无close exception；
- 真正R400 writer的450 receipt、$k=K_0=0$、未删453行重标；
- 两阶段与checkpoint全十word字面一致；
- 本次geometry result与checkpoint原native绑定的bytes/SHA一致；
- 本次C result与checkpoint原完整C绑定的bytes/SHA一致。

这里没有再次判断RMS／FD／native阈值；这些原责任仍由原求解器和R400完整消费者承担。完整数组内容最终还由原R409读入并按原合同核对。

## 4. 五阶段真实CLI与数据流

### 4.1 R409径向

新输入临时文件 `radial-input.json` 的schema为：

```text
current-C-ten450-complete-radial-Cartesian-readout-v1-input-v1
```

它只把实际checkpoint目录／SHA、geometry目录、computations、source_topic、显式budget／reserve交给冻结Node：

```text
node --max-old-space-size=<explicit> \
  --import computations/exact_20261114_tail_capacity_loader.mjs \
  computations/geometry_20261115_current_C_ten450_radial_readout.mjs \
  <actual-radial-input.json>
```

这一步新增真实全576×原steps的226态RK／root／完整角读出，不是BVP重解，不是纯读表。原二mean、全部112模／224shape和真实schedule完整保留。

### 4.2 R413原cuff计划

runner形成 `cuff-construction.json`，增加真实checkpoint SHA及原schema：

```text
R413-current-C-original-cuff-target-atlas-binding-v1-construction-v1
```

调用原R413 CLI：

```text
python -u computations/geometry_20261115_current_C_original_cuff_target_atlas.py \
  --computations <actual> --proof-directory <actual> \
  --checkpoint-directory <actual450> --checkpoint-sha256 <actual> \
  --construction <actual-cuff-construction.json> --construction-sha256 <actual> \
  --out <fresh-original_cuff_atlas>
```

得到原 `r409-original-cuff-plan.json` 和 `original-cuff-target-atlas.json`。两输出均核原 `result.json` 的receipt。原R413不执行BVP或新E查询。

如果原R413真实result已 `completed=true/error=null`，但仅原stdout摘要超限导致exit70，仍消费其已完整写出的两件原文件；报告保留这个明确transport分支。没有把任意非零退出改成科学成功。

### 4.3 R409共享场

同时具备真实径向complete和原cuff计划以后调用：

```text
python -u computations/geometry_20261115_current_C_ten450_shared_field.py prepare \
  --computations <actual> \
  --checkpoint-directory <actual450> --checkpoint-sha256 <actual> \
  --radial-directory <actual-radial> --radial-result-sha256 <actual> \
  --plan <actual-r409-original-cuff-plan.json> --plan-sha256 <actual> \
  --budget-seconds <actual-remaining-stage-cap> \
  --free-bytes-reserve <explicit> --out <fresh-shared_field>
```

保原 `result.json/payloads`、全field绑定及七元组。本接口没有直接构造假的assembly、normal-form或旧675 loader别名。

### 4.4 R418 metric

对刚形成的真实shared result和R413 atlas调用原R418 CLI，同时传同一个原C result及其SHA。R416准确cut场和R417完整帽由该冻结消费者按真实API加载，不先运行一个额外的“几何验证门”。

### 4.5 R422 reach

shared和atlas完整即可调用原R422。无论metric原返回pass、unresolved、resource_partial、error或它自己的summary70，都不会因为这个metric结果拒绝启动reach。只有外部终止、owner未静止或原整体资源不再允许时按真实原因留未访。

R422内部完整AA、CC、AC及全相位、闭边界、帽marker责任不改变。它不调用R418通过旗标作为前提。

## 5. 原消费者的全部显式科学／覆盖参数

这些参数必须在实际新recipe中指定，source没有默认科学阈值。

| 分支 | 必需键 |
| --- | --- |
| metric准确常数 | `eta`（非空准确文本） |
| metric资源／覆盖 | `interval_bits,sqrt_bits,initial_angular_depth,max_depth,max_visited_cells` |
| reach准确常数 | `curvature_upper,target_reach`（分别为原$K,\tau$准确文本） |
| reach完整覆盖 | `active_depth,curvature_max_depth,pair_max_depth,max_cells,max_pair_nodes,max_pairs` |
| reach工作精度／缓存 | `interval_bits,sqrt_bits,cache_entries,max_constant_levels` |

所有键原样转成原CLI的连字符参数。它们的合法域仍由各冻结原消费者校验；runner不代入科学公式、不按输出调节常数、不另选$K$或$\tau$。

metric与reach可声明不同的工作precision／覆盖预算；这不改变全十词、共同原C根族、$W/H/marker$或准确表达式。实际形成的bound文件可能不同，不能预称字节相同。

## 6. 资源、规则与所有权

`resources` 必须显式给出：

- `free_bytes_reserve`：非负整数；
- `node_heap_mib`：正整数；
- `child_shutdown_reserve_seconds`：正资源数；
- `stage_budgets_seconds`：恰含 `radial_replay,original_cuff_atlas,shared_field,metric,reach` 五个正数。

原deadline仍为实际 `request193-owned-job-science-deadline-v1`，必须属于当前run／source且recipe SHA与原launcher一致。source不改deadline文件、不延长 `science_seconds_from_namespace`。每阶段只取原绝对截止前剩余量，预留一次明确的TERM/KILL/wait窗口；记录实际科学／wall allowance、真实exit和耗时。不宣称OS调度零延迟或必能在deadline前终止。

每个科学CLI用独立新session启动，并保存实际PID／PGID／SID／start-time。停止只向观察到且start-time仍吻合的自有进程发信号；不扫描后向其他项目进程发送信号。reader不发送任何信号。

整体仍应运行在原3b8规则monitor控制之下，2700秒真pull／差异／规则停止不改。未来workflow的最小变化是在同一被monitor的主命令中，原launcher结束后调用本组件；或以同一个显式reviewed baseline启动后续原monitor入口。不能仅把timeout放大却让原namespace钟失效。

## 7. 真实C临时生命周期

按原实际路径保存：

```text
continuous-E/result.json
continuous-E/input-binding.json
continuous-E/query-plan.json
continuous-E/query-results.json
continuous-E/large-arrays/complete-source-radial-panels.jsonl
continuous-E/large-arrays/source-piece-index.json
```

新runner完整保留这六件的实际存在状态和字节身份。前四件是当前R418实际输入；后两件是R426未来live-query需要的source材料。后两件若缺失，只如实说明未来provider缺payload，不靠旧SHA伪恢复，也不加成当前R418的新数学门。

原geometry目录、450 checkpoint、原factory和source_topic也保持到本次已接全部消费者结束。没有数据复制入Git、Release或新artifact。R426未冻接口未调用；R425 source已发布，但本编排未pin也未运行。

## 8. 单份必要reader

调用：

```text
python -u computations/root_20261115_current_C_ten450_postsolve_necessary.py \
  --directory <actual-postsolve-out> \
  --out <fresh-postsolve-necessary-summary.json>
```

先要求原procedure完成finally，校验冻结producer来源和当前run／source，再按记录PID/start-time及实际/proc核实际owner已静止。没有owner静止证据时不读可能仍写入的科学结果，不清理raw。

原 `result.json` 的科学值只做原键选择，不做科学统计或数值复算；缺键与原null分开。五阶段全部原行保留，未运行后缀不省。大数组／完整enclosure／pair frontier只保原identity和元数据条数，正文明确未逐值返回；不是压缩编码的数据运输。

必要范围包括原初场全十word／dyadic、原接受来源、五阶段所有原错误和资源状态、原root/RK/node计数、metric全部fullflags／$\eta$/counts/scope、reach的原$K/\tau$/diameter/coverage/pending必要范围。每阶段stderr最多一个8192B必要文本范围，完整文件SHA和未显示字节范围分开；stdout科学大表不返回。

只写一份ASCII必要JSON，硬上限90000B，不承诺未运行时已测得大小。若超过，单份小错误记录原拟输出bytes/SHA和complete=false，不分片／编码传输，不减科学范围，不假称root已经读大表。

唯一输出标签：

```text
BEGIN_CURRENT_C_TEN450_POSTSOLVE_NECESSARY
END_CURRENT_C_TEN450_POSTSOLVE_NECESSARY
```

`GITHUB_OUTPUT`：

- `postsolve_summary`；
- `postsolve_summary_bytes`；
- `postsolve_summary_sha256`；
- `postsolve_readback_complete`。

所有子CLI的 `GITHUB_OUTPUT` 从其环境中移除，避免把大临时科学正文误交给job output。子stdout/stderr原文件保留，由本必要reader按上述范围读出。

## 9. 未来workflow清理的精确改动责任

本次只交requestless源，未修改193 workflow或启动新run。将来接线必须同时做到：

1. 193全部原前置／原两阶段source／预算／FD/final gates原样保留。
2. 在原namespace删除之前，用实际运行中已经生成的路径／SHA形成postsolve输入。将完整参数置于显式recipe；不从未来结果猜$K/\tau$。
3. 原193必要reader仍独立执行，新增postsolve必要reader在其自身producer关闭以后执行。
4. 原清理条件新增合取：
   `old_readback_complete && postsolve_readback_complete && all_original_and_new_owned_processes_quiet`。
5. 任一必要reader超限／缺失／失败时，不主动删除该namespace；同时诚实说明Actions runner销毁后不保证raw可恢复。
6. 最终小report可以分别展示原BVP必要结论和本postsolve必要结论；必须保它们各自schema、bytes/SHA，不能合并后冒成一个旧输出。job output总量另按实际ASCII/UTF16责任接线，不搬大ledger。

新source和reader均从不调用unlink/rmtree、上传或Git mutation。它们给出可以清理的**新增必要读回条件**，不替代旧owner与旧readback责任。

## 10. 直接pins与原完整闭包的区别

新runner逐字核11个直接文件。除第1节旧launcher／driver和R400 checkpoint `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` 外：

| 原组件 | SHA256 |
| --- | --- |
| R409 Node | `5cc3134ed58aed45efea012219aa2e889624c47b41d5ee9f558da231806ab568` |
| R413 atlas | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| R409 shared | `6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3` |
| R418 metric | `28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590` |
| R422 reach | `3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834` |
| 原capacity loader | `07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395` |
| R416准确cut | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| R417真实帽／已修模块身份 | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |

这11件不是原整个运行闭包。真实193的98前置、69公开runtime／29native及78恢复源，连同各R409/R413/R416/R417/R418/R422递归源／proof依赖都仍由其原接口保留。未来独立request必须合并完整实际执行及实际被hash的源集合，不能仅据这11个直接pin宣布完整runtime已齐。

本次没有新的source-view替换或数学helper修改，完整差异就是两件新文件。旧193、R409、R413、R416、R417、R418、R422字节全不变。

## 11. 执行后的结论边界

完整有限450接受只属于原两阶段对象。R409明确场仍不证明原准确连续ODE轨道；R416新cut场的几何证书不能重新标回旧有限solver。R418／R422真结果只依其实际scope解释。

当前仍未执行R425 held／全像Hausdorff／含反射$\delta_E$、R426live-query、same-$g$网格／谱精化或新的准确ODE误差比较。清理后未来若要运行这些消费者，必须在新的真实两阶段重生同job插入，不可凭本摘要／SHA复原旧450或C source payload。以上是接口责任，不是额外数学通过门。
