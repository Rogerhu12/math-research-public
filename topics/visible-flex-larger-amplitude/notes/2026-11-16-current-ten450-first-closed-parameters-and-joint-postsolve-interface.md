# R437 首次闭构造参数与 joint postsolve 完整接口

作者：ChatGPT amplitude agent（AI）。日期：2026-11-16。

正文：[R437：首个真实闭构造的参数选择、材料定义冻结与同作业接线](../results/R437-first-current-closed-construction-and-material-definition-freeze.md)。本包是可直接接入未来公开 Actions 的独立源码和明确参数；没有创建 request、workflow、实际父场或 run，没有 dispatch。总体203请求/工作流由root另行绑定真实来源。

## 1. 发布件与实际角色

| 文件 | bytes | SHA256 |
|---|---:|---|
| `geometry_20261116_current_C_ten450_closed_parameter_policy.py` | 37392 | `d7d01460f5a22f4fa2ca75ad36475688d65a465ba488d9caff65cb5ef13fb871` |
| `geometry_20261116_current_C_ten450_parameter_block_postsolve.py` | 26427 | `0f03ad496c8df7f148cf1fe532785a9a90d4b1e4827115f639223762e03d743f` |
| `root_20261116_current_C_ten450_parameter_block_postsolve_necessary.py` | 10414 | `f6176dbad15934153cd69c0b5c98a943aa76e423e4ce5627714eb1480c9acf65` |
| `geometry_20261116_current_C_ten450_parameter_block_postsolve_held.py` | 5450 | `28b48f0cc5c281353db3812c4950e4f0b4516c2bae81342108658ae6f49b7ff4` |
| `current-ten450-first-closed-parameter-policy.json` | 2198 | `fe932b50f25bd8d77709be1efd26da8c24a7d87f9ad1423bd6a9ebc34c1d0a41` |
| `current-ten450-first-closed-work-choices.json` | 3356 | `8a03c854c93194f6bb3f2f75f06c20bf8397e5b85451ce6a1e7247f0a95c7d08` |
| `R437-first-current-closed-construction-and-material-definition-freeze.md` | 14508 | `11b99358b63eccb0bc96e4c159eff9f5b6fcc450d2ed7dd2ee3e36cc07308e46` |

四运行件均小于100KB。`parameter-policy` 是实际被 helper 校核的几何定义选择；`work-choices` 是总体入口复制到各实际runtime spec的明确资源/常数，不包含虚构路径、accepted checkpoint或未来SHA。完整diff及publication manifest是交付审读材料，不作为科学门，不需入Git。

源码实施的工作只发生在 `GITHUB_ACTIONS=true`、`GITHUB_REPOSITORY=Rogerhu12/math-research-public` 中。本地仅作源文字、JSON、字节/SHA与diff处理，未导入项目、未做AST、未编译、未运行科学或独立fixture。代码中的 `compile/exec` 是未来Actions加载冻结源码视图的实施，不是本地已经执行。

## 2. 明确的来源合同与 closure

### 2.1 三分支

`upstream_kind` 恰可选：

| 值 | 实际来源/截止钟 |
|---|---|
| `original193-frozen450` | 原193 driver11dd/launcher6ff，原 `request193-owned-job-science-deadline-v1` |
| `R431-refined450` | 已发表R431 launcher4375375b、R427 driver70a5709d，原193 origin及其同一截止钟 |
| `joint203-frozen450` | R444新5400 driver/cb057 launcher，`request203-owned-job-science-deadline-v1` |

joint203的完整角色：

- driver `geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py`，33857B / `5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592`；schema `current-C-continuous-ten-joint-live-full453-to-frozen450-physical-DN-v1`。
- launcher `geometry_20261116_continuous_ten_joint_full453_frozen450_launch.py`，19376B / `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7`；schema `current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1`。
- 原 two-phase 的 `adapter-status.json`、两phase字段、`actual_final_checkpoint/directory`、43f writer、lease与真实owner静止范围原样；新checkpoint必须记录真正5400 driver，不能改标签成11dd。

新R437明确使用这个tuple，不依赖请求号名称来猜provider。原R431代码仍只支持其已发表的原193 origin；尚未在本包扩成joint网格分支。R441的未来来源必须独立显式接入，不用`R431-refined450`冒它。

`bind_joint203` 从冻结R438的真实 `bind_original193` 完整正文创建函数视图，只换函数名和明确的来源环境：LAUNCH/DRIVER/PINS/UPSTREAM_SCHEMA/DRIVER_SCHEMA/DEADLINE_SCHEMA。全453/450接受、同十词、原FD/native/finalaudit、checkpoint/C/geometry/原clock和quiet检查原文保留。

### 2.2 原R438源与20个直接运行pins

导入的原完整runner为 `geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py`，66873B / `5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95`。原16项PINS逐值保留，包括原193与R431角色（它们也是可选分支），R409径向/shared、R413、R416/417、原R418、R426/provider、原R422、R435和capacity。

新直接PINS在这16项上加：上述R438 runner本身、本次policy helper、新joint launcher、新joint driver，共20项。这只是该runner的直接校核集合，不冒称它是所有递归科学模块或总体203的完整closure。

policy helper另直接校核7个冻结解释源：Shared6a5f、Checkpoint43f、Cut28417、Atlas02bb、Caps0ff1、Saved1c7a、Active675。后两项确保完整core/准确材料定义的来源明确。各模块原有完整递归闭包继续由真正源加载器与总请求保留；新helper不删除这些校核。

新reader加载原R438 reader26912B/`57413c73db29cb9f65451f631771c07c642edf162dfbe6cdbaa292b5fb451fe5`。新held加载原R438 held44769B/`119ec38cc9351a2d040ce8c7101b933e1e572d19deabb7baf62c4c1cec62eada`，将producer registry精确限制为本次新R437runner，并将必要quiet/readback指向本次新reader；原R425科学源仍53711B/`c87b3a9b9d17f74d8c4f4066f65318e50fed5a56143f620628049a86dcf77ef2`。

因此总请求须同时提供三件原R438文本、四件本包运行文本、两小参数文件、新joint完整R444依赖以及原消费者闭包；不能只复制这四小源而遗漏被真实import/校核的旧源。原16pins不是“旧source不执行”，其中R438五科学角色仍真正运行；旧193/R431只在各自选定分支解释来源。

## 3. 总体作业怎样构造真实runtime spec

新runner schema为 `R437-current-ten450-first-or-frozen-construction-block-postsolve-v1`；输入schema是该词加 `-input-v1`。CLI：

```sh
python -u computations/geometry_20261116_current_C_ten450_parameter_block_postsolve.py \
  --input ACTUAL_POSTSOLVE_INPUT_JSON --input-sha256 ACTUAL_INPUT_SHA256
```

实际JSON必须由本job在真实上游产物存在后构造。下面列字段是接线模板，不是已经存在的路径/成功实例：

| 字段 | 必须填入的实际内容 |
|---|---|
| `schema` | 上述新输入schema |
| `upstream_kind` | 例如首次joint203时精确为`joint203-frozen450` |
| `namespace` | 原job建立的唯一RUNNER_TEMP自有目录 |
| `upstream_launch_directory` | 真正新joint两阶段launcher输出目录，不是旧run摘要 |
| `upstream_result_sha256` | 实际`result.json`SHA；原body允许此明确绑定 |
| `job_deadline`, `job_deadline_sha256` | 原launcher真实消费的deadline文件及SHA，且bytes/SHA与其`actual_job_deadline`一致 |
| `geometry_directory` | 同job完整新provider原native geometry目录 |
| `continuous_e_directory`, `continuous_e_result_sha256` | 同job真实C目录及resultSHA |
| `computations`, `proof_directory`, `source_topic` | 实际固定checkout/source路径 |
| `out` | namespace内新的 sibling 后处理目录，不覆盖上游 |
| `construction_policy` | `{"file":实际复制的小policy文件,"sha256":真实policySHA}` |
| `construction_mode` | 首次`initial-construction`；已有A/B的明确后继才`reuse-construction` |
| `resources` | work-choices中的原五stage caps、两参数caps、heap/free/shutdown |
| `metric`, `c_queries`, `reach`, `witness_resolution` | 小work-choices对应完整对象原样 |

首次输入不能有`construction`、`first_construction_freeze`或`first_material_transport`；尤其不允许用一个假H让旧验证先通过。reuse输入则必须额外提供真实A、B各自的`{file,sha256}`。R431分支还需其原`origin_launch_directory`；该来源合同沿原源。

总入口可在上游失败时仍调用新runner，让其返回原未启动后缀；也可显式记录全部后继未启动。不得把失败输入补成accepted450。helper绝不触发新的BVP或修改原stem。

## 4. 径向CLI完全不需要未知H

原R438 `run` 的径向body逐字保留。它在真实binding后写`radial-input.json`，字段恰为：

```text
schema = current-C-ten450-complete-radial-Cartesian-readout-v1-input-v1
computations, source_topic
checkpoint_directory, checkpoint_sha256
geometry_directory
out, budget_seconds, free_bytes_reserve
```

实际command为：

```sh
node --max-old-space-size=ACTUAL_HEAP_MIB \
  --import computations/exact_20261114_tail_capacity_loader.mjs \
  computations/geometry_20261115_current_C_ten450_radial_readout.mjs \
  ACTUAL_RADIAL_INPUT_JSON
```

没有H、W、markers参数。只有原radial实际完整返回，R437的`invoke`才执行`construction_parameters`；随后原`run`正文才从新形成的`self.spec["construction"]`写原cuff construction。没有在真实共享输入之前假造新schema/accepted字段。

## 5. 参数helper的三操作与真实产物

helper schema `R437-current-ten450-explicit-closed-parameter-policy-v1`，输入schema加`-input-v1`，policy schema加`-recipe-v1`。统一CLI：

```sh
python -u computations/geometry_20261116_current_C_ten450_closed_parameter_policy.py \
  --input ACTUAL_PARAMETER_INPUT_JSON --input-sha256 ACTUAL_INPUT_SHA256
```

所有操作公共输入：`operation,namespace,computations,origin_launch_directory,origin_result_sha256,job_deadline,job_deadline_sha256,checkpoint_directory,checkpoint_sha256,policy,policy_sha256,resources,out`。resources恰提供`budget_seconds/free_bytes_reserve`。新runner真实生成这些JSON与身份，调用者不用预编将来的值。

### 5.1 initial-construction

额外输入`radial_directory/radial_result_sha256`。完整读原radial与cp后按R437正文形成H/W/markers。产物：

- `first-construction-freeze.json`：记录A，schema为helper schema加`-first-construction-freeze-v1`；包含完整core定义、实际构造词及H形成数据。
- `r413-construction.json`：原R413真实construction schema，绑定本次checkpoint SHA和原cuff。
- `result.json`及`necessary-summary.json`：实际参数操作范围、身份、失败/未访。

H_*是当前末mean、当前FFT DC、当前RK background差的有限准确组合，最终只做一次RN64。它是明确新experiment datum，不是某原连续primitive的证书。W=.01、k=1/160是已有构造的自由选择，仍须原域/全几何实付。

### 5.2 reuse-construction

额外输入A、B各自真实文件与SHA。真正读首core/Phi/transport，逐词复用W/H/all markers。`first_and_current_core_words_equal`只诊断，不阻当前solver或几何consumer。输出新的、绑定当前cp的`r413-construction.json`，而非改写原A。

当前代码仍让R409使用当前core。`material_pullback_or_conjugacy_executed=false`与`actual_common_material_pullback_still_unpaid=true`明确记录。这里没有按新解重选H，也没有把首core强塞当前BVP；同一闭g的下一步由R443/R441/R442的真正运输责任承担。

### 5.3 held-witnesses与材料记录B

原shared_field成功后立即调用，额外真实输入：`shared_directory/shared_result_sha256/cuff_atlas/cuff_atlas_sha256/proof_directory/witness_resolution/construction_mode`，以及实际A、reuse时实际B。

它先加载同一R416准确场/原七元组，并附原R413 atlas；随后保存`first-material-transport.json`（首次）或`current-material-transport.json`（reuse）。完整实际registration/normalization只在本job临时记录，不转成新科学门。必要report只保其receipt/定义身份和明确scope。

再在真实piece表解析唯一prefix左端0和四q词，产`r425-witness-plan.json`。source只确定真实地址，不执行四点场包围或距离。若此动作异常，record/error保留，原metric/reach继续；held自身后来根据真正已有依赖决定可否启动。

实际源加载R416可能会形成其原准确cut包围；本接口的“只确定地址”不表示整个loader零科学工作。所有该工作仍在Actions，沿原解释/原前提，不新增阈值。

## 6. 显式参数及资源选择

小work-choices已经逐项列原consumer全部CLI键，调用者应复制对象，不删字段或自行补默认值：

| 范围 | 本次明确选择 |
|---|---|
| 原总钟 | 沿原deadline18900science+2700readback，不重启 |
| 五stage局部cap（秒） | radial1800；atlas120；shared600；metric1800；reach1800 |
| 两参数局部cap（秒） | construction120；witness/material120 |
| 独立held cap（秒） | 1800 |
| owned shutdown/free/Node heap | 30秒；2147483648B；12288MiB |
| metric | eta=`1/1000000`，interval256，sqrt128，angular depth2，maxdepth20，100000cells |
| R426按需C | precision256；absolute/relative128；guard8；eval200000；width80；depth40/40；panels100000；nodes200000；累计active900秒 |
| reach常数 | K=`1250/149`；tau=`1183/10000` |
| reach原12＋新3工作键 | active2；curvature/pairdepth20；interval256/sqrt128；cells200000；pairnodes1000000；pairs1000000；cache4096；constantlevels8；blocknodes1000000；unioncells4096；blockcache4096 |
| held全部8键 | active2；positiondepth20；radiusgoal=`1/1000000`；interval256/sqrt128；positioncells200000；prefixpoints4096；tailwitnesses4096 |

这些是有限资源/实验策略，不能声称原剩余时间足够、原未标记reach已有、tau/D或delta_E比例已付。每个stage cap继续被原绝对remaining clock裁剪；到时保真正pending/未访。R426仅在原metric cell尚未证时按实际同C query精化，完整粗界不因精化资源未达而被抹掉。

这个work-choices没有额外scientific gate。它也没有宣称要缩减原全部根pair空间；max_nodes只是原有限运行上限，R435原完整AA/CC/AC责任及未访块仍完整列出。

## 7. 独立held与必要reader

新的held source schema：`R437-current-ten450-parameter-block-same-job-held-after-shared-v1`。输入schema加`-input-v1`。原held命令与全部8个科学/work键保：

```sh
python -u computations/geometry_20261116_current_C_ten450_parameter_block_postsolve_held.py run \
  --input ACTUAL_HELD_INPUT_JSON --input-sha256 ACTUAL_HELD_INPUT_SHA256
python -u computations/geometry_20261116_current_C_ten450_parameter_block_postsolve_held.py readback \
  --directory ACTUAL_HELD_OUT --computations ACTUAL_COMPUTATIONS --out ACTUAL_HELD_NECESSARY_JSON
```

held input只有原R438十项：schema、postsolve_directory、postsolve_procedure_sha256、postsolve_input、postsolve_input_sha256、witness_plan、witness_plan_sha256、held、resources、out。以上以原`set(spec)`字面为准，不增加source伪门。新registry只接受本次新R437runner准确源/两schema，Read绑定新reader以同时核原五stage和两参数组静止。

三个依赖仍仅radial、atlas、shared；metric/reach的negative、partial或error不是held前门。只有实际witness文件在正确同场中存在才能给其原CLI。不存在时总体入口如实记未启动，而不造点坐标。

新postsolve必要reader schema `R437-current-ten450-parameter-block-postsolve-one-necessary-conclusion-v1`，原CLI保持：

```sh
python -u computations/root_20261116_current_C_ten450_parameter_block_postsolve_necessary.py \
  --directory ACTUAL_POSTSOLVE_OUT --out ACTUAL_POSTSOLVE_NECESSARY_JSON
```

帧是 `BEGIN_R437_PARAMETER_BLOCK_POSTSOLVE_NECESSARY` / `END_R437_PARAMETER_BLOCK_POSTSOLVE_NECESSARY`；helper帧 `BEGIN_R437_CLOSED_PARAMETER_NECESSARY`；held帧 `BEGIN_R437_CURRENT_TEN_PARAMETER_BLOCK_HELD_NECESSARY`，各有对应END。

原reader返回文件/结构身份、五阶段必要原字段、全部真实未访/错误，附完整实际W/H/markers、两参数动作和四witness，材料大正文只receipt。各单份硬90000B；超限70/必要读回未完成，不拆分、编码或用仅SHA冒读完。第一次实际执行前不保证摘要一定有余量。

原R438选择的异常/日志是既定必要范围，未被扩大成完整原始stderr的保证；新helper error含其实际traceback，仍受整体硬限。若owner在status前中断，原生命周期/文件缺失/未访责任保持，不能把空字段变成成功。

## 8. first A/B、原C与完整raw生命周期

总job不得在原193/新joint两阶段结束就立刻清其raw。要保：

1. 实际accepted450 checkpoint全部原payload和同jobgeometry；
2. 原C `result.json/input-binding.json/query-plan.json/query-results.json`，`large-arrays/complete-source-radial-panels.jsonl`、`large-arrays/source-piece-index.json`直到metric/provider结束；
3. 本次radial、shared七元组、atlas、全部新结果与first A/B直到声明的后继mesh/几何/held完成；
4. 每个必要reader真正完成，且原BVP、postsolve、两参数动作、held与任何mesh属主均已静止。

R437四源本身不删除。总体203 workflow把上述条件加到原自有namespace清理，不增科学通过门。某consumer必要摘要超限时不能主动清掉其同job现场；runner最终销毁仍必须诚实说明不能再从旧SHA恢复。

first A/B是实际定义/来源，不是把整个raw/证书迁入Git的许可证；大场仍不保存。将来独立run要重生真原输入和首次构造，不能凭本次必要摘要重贴旧accepted状态。若未来需要跨run固定同一个材料图，必须明确携带可审查的实际定义与真实重生合同；本次只支持同job A/B。

## 9. 文字差异与尚未运行范围

每个新source有完整文件diff。另有三份最小body差异：

- `R437-validate-view-complete.diff`：原construction对象改真实policy/mode/A/B/两caps字段；其余原五stage/metric/query/reach验证保。
- `R437-joint-origin-body-complete.diff`：只函数名；新来源环境逐项在`R437-explicit-source-view-environments.json`。
- `R437-parameter-owned-invoke-complete.diff`：只row集合、两个cap索引、方法名及四个skip地址；原stop/wait/absolute-clock正文保。

reader与held完整replacement表直接在新source中，所有旧fragment均要求恰出现一次；这是固定来源实现约束，不是独立科学fixture。它们在实际Actions加载并记录view bytes/SHA，未宣称与旧schema输出逐字相同。

本次未支付：真正453/450接受、实际H/marker/core/registration、完整R409重放、准确新闭场/全t metric/reach/held/反射、README比例、当前几何误差/连续ODE同一性、共同材料拉回和同一g的全部精化。每项以后只从真实返回记账，不能以源齐或proof已刊预填通过。
