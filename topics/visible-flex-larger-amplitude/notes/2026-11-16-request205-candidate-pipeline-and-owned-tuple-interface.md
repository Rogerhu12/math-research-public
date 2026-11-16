# Request205：真实202候选、新准确C十族与完整同job来源接线

作者：OpenAI ChatGPT（AI assistant，amplitude 源码责任；root 唯一 request/workflow/ref 发布）。本接口交付三份独立执行/必要读回源码，消费已刊 [R449](../results/R449-actual202-to-accurate-continuous-ten-fresh-candidate.md) 的候选及双问题 driver。root 负责总体workflow、request、rules owner、R452首次闭面来源注册及最终派发。本件不含未来run或成功预报。

## 1. 冻结身份与旧件范围

目录 `/workspace/visible-larger-working/actual202-accurate-ten205/`；公开源码路径为 `topics/visible-flex-larger-amplitude/computations/`。

|当前文件|字节|SHA256|Git blob|
|---|---:|---|---|
|`geometry_20261116_actual202_accurate_ten_pipeline.py`|32025|`baa207cc4902ea029b7be21fac7f4a0f878a4075bca733f6a76108a656a076ba`|`e2f7719a7fffa39283c9b12667d2e4791a92f510`|
|`geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py`|20657|`227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7`|`70a455364cd96e7ab2a69016ce8173904e05fc01`|
|`root_20261116_actual202_accurate_ten_two_phase_necessary_readout.py`|29882|`80c26207dea0d393a102dabba9f1e5ed9580460cc40876d2668975ae9499af1f`|`4006c3b348ee6ad66d3f55c94b47a2a9ac8b8a09`|

三份完整文本差异均在同目录：`pipeline.complete.diff`46746字节、SHA256 `a4b2fc75a5236f86562645cea376ad504172b2a190f3ce679291c19b8a6a3837`；`launcher.complete.diff`7202字节、SHA256 `e4ab623caaa7234637d3079face99d0825bb3a23ec2aeaf71e45354aa03b9813`；`reader.complete.diff`10975字节、SHA256 `4d1a7a1cb257e2b4cc44aa84c067a55adea66db8e8b83ef2cf463033b3087d50`。临时 `publication-files.json` 汇总实际发布路径/身份，不要求把该交接清单或旧raw入库。

基线为 R444 已刊 pipeline `c825f632fa9ab030ef47128f884e548c6fc629395e28e0009df1d22d19deb15f`、launcher `cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7`、reader `4e9a46fbdd12d94dfe723b1163b5d04fe0dfc6c3bfc8d6f9dacabd11dbab5106`。旧源完整不改，旧203仍有自己的当前来源合同。新三件不能假称原tuple。

R449当前 helper 是31509字节、`ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38`；driver34835字节、`56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615`。它们已补原准确模板的 `cut_radius` 第九结构字段；首刊 c557 版本没有执行。该修正不是新cut、投影中点或科学门。本文三源只接受这两个最终身份，早期未刊47f9 launcher不再使用。

## 2. 总请求的明确名字

|对象|实际合同|
|---|---|
|request路径|`notes/current-C-actual202-accurate-ten-closed-geometry205-request.json`|
|workflow路径|`.github/workflows/visible-current-C-actual202-accurate-ten-closed-geometry205.yml`|
|request schema|`public-actual202-accurate-ten450-closed-geometry-request-v1`|
|request_number|`205`|
|namespace|`visible-current-C-actual202-ten450-closed-geometry205`，严格位于本job的RUNNER_TEMP直接子目录|
|lane|root声明的 `actual202accuratetenclosedgeometry`|
|postsolve上游kind|`actual202205`，由root/geometry的独立R452来源分支显式注册|
|namespace及current deadline schema|`request205-owned-job-science-deadline-v1`|

本pipeline不负责创建这个namespace或原deadline，只核真实同job来源。BVP组件launcher只要求新的、独占的RUNNER_TEMP子目录，并核具体205 deadline schema；它不新建全job钟。

原203请求的全部科学source pins和原193/187来源必须逐项保留，另添加当前实际需要的新文件；不能全局替换旧字典而丢历史/运行依赖。本文只给新增角色及其直接消费关系，总表的最终计数由root实际request字典产生，不能用三个当前文件数冒完整runtime闭包。

## 3. 新增request字段的确切结构

以下是源码实际读取的新增字段；`file` 是已复制到实际computations目录的basename。

```json
{
  "actual202_candidate": {
    "adapter": {
      "file": "geometry_20261116_actual202_accurate_ten_candidate.py",
      "bytes": 31509,
      "sha256": "ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38"
    },
    "driver": {
      "file": "geometry_20261116_actual202_accurate_ten_full453_frozen450.py",
      "bytes": 34835,
      "sha256": "56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615"
    },
    "parameter_input": {
      "file": "actual202-accurate-ten-candidate-input.json",
      "bytes": 2165,
      "sha256": "c980e9d4c6e15455459dc91a890b4fd9d8b02bced26eecd5d632ff9d250dbd4d"
    },
    "maximum_adapter_seconds": 120
  }
}
```

同时使用原资源字段 `execution.sampling_future_BVP_reserve_seconds=3600`，无第二默认值。root总体owner和当前pipeline从这同一字段读真实采样启动预留。新adapter的120秒是同原总钟内的有限子进程资源上限，没有给科学搜索新钟、没有更改7200秒完整双BVP上限。

其余源码读取原request结构：`actual180_selection`、`original180_request`、`selected_file_reconstruction`、`construction_inputs`、`inputs`、`construction.R300_proof`、`construction.core_geometry_pointer`、`selected_construction.maximum_factory_seconds`、`current_BVP_recipe`、`pruefer_provider.native_source_replacements/new_native_source_additions/complete_current_native_source_sha256`、`execution.owned_process_helper`、`source_sha256`。旧原模板仍通过 `checked_parameter(comp,item)` 从comp下读取；workflow需复制并按已发表字节核这些小参数文件。

`current_BVP_recipe`仍原179模板10294字节、`d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811`。准确结构模板从实际恢复的 `actual180_selection.selected_recipe` 取2136字节、`cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb`；不新增一个猜测的结构配方字段，也不把旧180的参数/域证明转给新202候选。

## 4. 四个pipeline phase与原规则钟

每个phase的统一调用是：

```bash
python computations/geometry_20261116_actual202_accurate_ten_pipeline.py PHASE \
  --request "$VISIBLE_BASE/dispatch-request.json" \
  --base "$VISIBLE_BASE" --code-directory "$VISIBLE_COMPUTATIONS"
```

`PHASE` 精确为 `selection`、`construction`、`binding` 或 `readback`。前三项分别使用root总体owner的原rules流程；`binding`新增独占role及 `candidate-bind-rule-sync` 路径，不能再次用construction role撞其独占 `xb` 收据。全部仍受原18900秒namespace科学截止、原2700秒规则同步及2700秒读回/清理余量；实际截止前能否完成各项由真实执行决定。

|顺序|phase / 外部原阶段|实际作用与输出|
|---|---|---|
|1|`selection`|复用1738冻结恢复函数，真实恢复旧165/180小来源文件；输出 `selected-recovery-result.json` 和原restored子目录。当前字段明确它们只为结构来源，旧全419域不迁移。|
|2|原完整C与cut|原f12f当前C、原完整cut读回；仍为本job真正来源，不能复用已清理旧场。|
|3|`construction`|调用R449 `prepare`，再调用原72c factory；输出 `construction/candidate-preparation/`、`construction/factory/` 及 `construction/procedure-result.json`。|
|4|原完整far/sampling|原197 joint所有112 mode、全部原C/source/一般Robin责任；采样预算由同原owner在真实启动时以3600预留和真实剩余时间裁剪。|
|5|`binding`|检查实际current geometry，生成真实native config，再调用R449 `bind`，形成最终BVP recipe和当前deadline收据；输出见§6。|
|6|一次 `readback`|在binding尝试后、BVP前读全部恢复/prepare/factory/bind现存字段；包括原异常/未起。只调用一次，避免重复输出/独占文件冲突。|
|7|当前BVP launcher|一个真实owner串联原453接受与同十词fresh450接受；每phase原全部终门。|
|8|独立R452完整闭面分支|只有实际450场才有现场输入；保首次construction、radial/atlas/shared/metric/reach与独立held同钟运行。|
|9|最终必要读回/quiet/清理|root总体wrapper核所有必要marker、全部owner静止后才清理；BVP前的construction marker不能单独授权清理。|

`readback`所谓完整两个adapter阶段指真实 `prepare` 和 `bind`；它不预读尚未执行的453/450。这两完整问题由本文独立phase reader在终态quiet后读取，closed消费者又有自己的必要scope。每份必要输出单独硬限90000字节，不把科学大表分片或编码运输。

## 5. prepare与真正factory

R449先把已刊actual202的553字节十词显式投影为binary64，再把其准确dyadic声明为新准确十族初点。所有十项投影差值和新准确参数只在Actions形成。原202的finite Gauss残差/J/接受不输入这一模型。

`construction`在新目录 `construction/candidate-preparation` 中真实产生 `candidate-ten-parameters.json`、`actual202-projected-accurate-ten-model-recipe.json` 和 `adapter-result.json`。新的准确配方复制原九个结构字段，包括原cut_radius；旧九系数全部换当前十项，非零xi保留。

接着真实调用72c的参数完整保原source合同：当前accepted96几何、同jobC result及完整cut readout、真实新ten recipe、原R300 proof、`sqrt-bits=256,max-domain-cells=65536,max-domain-depth=32,domain-budget-seconds=300`。两个完整base/parameter域都沿原producer，有限budget未付诚实回读。这个source既不制造factory result，也不把域证书false加入BVP新门。factory的实际definition descriptor是 `large-arrays/accurate-new-model-definition.json`，pipeline按受控相对路径、原bytes/SHA读取，拒绝绝对路径或逃出源目录；没有将真实含子目录member误要求为basename。

1738原 `call` 的stdout事件会保其原request187前缀，这是实际复用的传输函数身份。当前pipeline外层schema/run/source/调用角色均为205，不能凭内部历史前缀伪称旧run重新发生。原恢复/科学child照常留原返回码、resource_partial、elapsed和argv；错误中token/官方签名URL按原策略移除。

## 6. sampler以后形成config与最终recipe

`binding`读 `current-geometry/result.json`。它的schema/source/所有完整native条件仍由原197/c71d执行；原workflow已有的 `completed/native_geometry_ready` 前提保持。未齐则记录原geometry错误与未启动范围，既不造current-H/native结果，也不把未做的joint代表选择写成修复成功。

当前config路径固定 `base/current-C-BVP-client-config.json`。它从原179 `native_configuration` 复制全部原政策，按request明确的source replacements/additions形成真实197 joint源表，逐dict等 `complete_current_native_source_sha256`。它加入当前comp/source_topic、真实geometry目录/receipt、`actual_policy_template`、`actual_candidate_preparation`、`actual_candidate_model_recipe`、`original_actual_geometry_result`。

**这里没有 `original_execution_recipe`。** 最终BVP recipe要hash当前config，故config不能反过来假写尚未形成的最终recipe receipt。已逐源核 c71d `bind_current_native`、02e164 `TailClient.__init__`及runtime-spec投影、43f实际native configuration保存：它们消费当前source/原政策、geometry/C/cut/source_topic和实际文件完整身份，不读取旧workflow附加的 `original_execution_recipe`。新字段是准确来源说明，不改变native配置的科学参数。原43f仍保存真正整个当前config字节，不能继续引用旧配置SHA。

pipeline在同一binding role里实际调用：

```bash
python <R449-helper> bind \
  --preparation-result <base/construction/candidate-preparation/adapter-result.json> \
  --preparation-result-sha256 <实际SHA> \
  --factory-directory <base/construction/factory> --factory-result-sha256 <实际SHA> \
  --current-C-directory <base/continuous-E> --current-C-result-sha256 <实际SHA> \
  --cut-twojet-readout <base/cut-twojet-readout/cut-twojet-readout.json> \
  --cut-twojet-readout-sha256 <实际SHA> \
  --BVP-recipe-template <comp/原179-template-basename> \
  --tail-config <base/current-C-BVP-client-config.json> --tail-config-sha256 <实际SHA> \
  --code-directory <comp> \
  --candidate-driver-sha256 56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615 \
  --request-number 205 --sampling-startup-reserve-seconds 3600 \
  --out <base/actual202-ten-BVP-input>
```

真正的输出与消费关系：

|路径|实际内容|
|---|---|
|`actual202-ten-BVP-input/adapter-result.json`|R449当前 `BVP-input-bound` 报告；helper source/run/commit、当前 C/cut/factory/config/driver、十个投影词、coast center诊断及资源绑定|
|`actual202-ten-BVP-input/actual202-accurate-ten-full453-frozen450-recipe.json`|新完整双问题recipe；生成后不再改任何字段|
|`actual202-ten-BVP-input/result.json`|当前pipeline的 `…-actual-BVP-input`来源汇总，指向上两件实际receipt|
|`candidate-binding-procedure-result.json`|当前binding外层原调用/错误/partial/未起范围|
|`current-BVP-deadline.json`|原namespace deadline内容原样保留，再附最终recipe SHA、实际pipeline/adapter绑定receipts；不改start或截止|

pipeline汇总schema为 `request205-actual202-accurate-ten-construction-v1-actual-BVP-input`，保 `direct_BVP_input_created,generated_BVP_recipe,actual_candidate_binding,actual_candidate_preparation,actual_ten_factory_result,actual_ten_definition,actual_ten_model_recipe,actual_current_native_configuration,actual_current_geometry_result,all_ten_initial_parameters,actual_projected_binary64le,actual_new_accurate_ten_parameters,candidate_policy,explicit_resource_binding,complete_native_source_sha256` 和明确的旧接受不继承标志。

该汇总由pipeline source `baa207cc…` 产生；真正candidate adapter报告由 `ee3675ce…` 产生，不能混用这两个 source/schema。原钟文件的 `request_sha256` 必须等真实 `dispatch-request.json`字节，`template_recipe_sha256`等原179模板，run/source/repository同job；最终recipe和candidate receipts只追加身份。

## 7. BVP组件launcher与原完整数值路径

launcher schema `R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1`；driver schema `R449-actual202-projected-accurate-ten-joint-full453-to-frozen450-physical-DN-v1`；recipe schema `R449-explicit-actual202-projected-accurate-ten-joint-full453-to-frozen450-recipe-v1`。

相对cb057，launcher只改当前tuple/205 deadline与事件，新增必填 `--candidate-binding` / `--candidate-binding-sha256`、实际输入receipt，以及生成recipe字节与candidate报告的对应检查。原Popen、start_new_session、SIGTERM/SIGKILL、wait/reap、磁盘资源、finally、共享7200与原绝对截止算法保留。

```bash
python <current-launcher> \
  --recipe <base/actual202-ten-BVP-input/actual202-accurate-ten-full453-frozen450-recipe.json> \
  --recipe-sha256 <实际SHA> \
  --candidate-binding <base/actual202-ten-BVP-input/adapter-result.json> \
  --candidate-binding-sha256 <实际SHA> \
  --accepted <原accepted96文件> --accepted-sha256 <原b4d2完整SHA> \
  --complete-seed <原699乘453真实seed文件> \
  --factory-directory <base/construction/factory> --factory-result-sha256 <实际SHA> \
  --tail-config <base/current-C-BVP-client-config.json> --tail-config-sha256 <实际SHA> \
  --tail-source-root <实际恢复的source_topic> --computations <comp> \
  --job-deadline <base/current-BVP-deadline.json> --out <base/BVP-launch>
```

输出仍 `BVP-launch/result.json`、`BVP-launch/full-BVP/adapter-status.json`及原 `design453` / `frozen450`目录；launch保 `actual_job_deadline`原receipt、`actual_candidate_binding`原receipt、实际driver/source、子进程/quiet/停止原因和原两个phase。实际checkpoint由43f在原各phase接受后生成；`actual_driver_source`是当前56cb，而非原5400。来源检查不是新的数学接受阈值。

全部原科学参数继续：M112/N2048，原完整338物理jet，453三active/七shape冻结，后继完整450十shape全冻；原8外迭代/17内回溯、RMS1e−6/BC1e−11/FD5e−5，native32×10/tol2e−9，原新当前H/全部112/fresh finalJ/audit。原共用7200 process上限受原namespace剩余时间裁剪，不重启phase钟。

## 8. phase必要reader的范围

```bash
python <current-phase-reader> \
  --launch-directory <base/BVP-launch> --sampler-directory <base/current-geometry> \
  --sampler-result-sha256 <若实际存在则传其原SHA> \
  --candidate-binding <base/actual202-ten-BVP-input/adapter-result.json> \
  --computations <comp> --out <fresh-base/necessary-BVP-readback>
```

sampler的SHA选项原本可省；未产出时不要伪造SHA。candidate路径必传，但如果整个binding/launch未起，它的缺失如实记录。若实际child已启动，reader要求launcher消费的candidate bytes/SHA与当前文件吻合。

reader显式核当前launcher schema/source/driver、当前R449 adapter source/run/commit、当前driver schema/source。旧base `19878e48…`元数据reader照原加载，原 `fd_view`、`phase_documents`、`native_view` 等科学选择函数完整文本未改。每phase原FD方向/误差层/flags按原专用函数逐项返回；native全existing records在Actions解析，最后真实迭代的标量trial/失败linear保正文，早期大trial/J/factors为完整身份。新R449必要scope含原factory/C/config/recipe/driver receipts、实际预留、center诊断和错误，不把adapter的0次BVP计数混同外层sampler已做工作。

原34b/19878元数据reader的一般字符串和日志选择范围保持：一般字符串用原 `short(...,1800)` 字节前缀和完整identity；匹配日志行用1200字节前缀，仅首2行/末1行及其原行身份；一般长度大于16的列表只identity。不能把这种异常/traceback选择表示说成原大日志全文。FD逐方向/逐层使用专用函数，不受泛用长列表缩写；成功大数值见证只身份。

body schema `actual202-accurate-ten-current-C-live-full453-and-frozen450-necessary-readback-v1`。stdout标记 `BEGIN_REQUEST205_ACTUAL202_TEN_TWO_PHASE_NECESSARY` / `END_REQUEST205_ACTUAL202_TEN_TWO_PHASE_NECESSARY`。GITHUB_OUTPUT仍 `bvp_summary/bvp_summary_bytes/bvp_summary_sha256` 三键。完整necessary summary与临时index各有实际identity，超90000字节诚实metadata failure70且不写cleanup marker；没有再切块编码大数据。

## 9. construction必要reader与独立清理责任

construction读回在binding尝试后只调用一次：`pipeline readback --request … --base … --code-directory …`。它先调用root实际 `execution.owned_process_helper` 的 `observe`，确认原科学groups quiet，才读真实文件。

stdout标记 `BEGIN_REQUEST205_ACTUAL202_TEN_CONSTRUCTION_NECESSARY` / `END_REQUEST205_ACTUAL202_TEN_CONSTRUCTION_NECESSARY`；GITHUB_OUTPUT仍 `construction_summary/construction_summary_bytes/construction_summary_sha256`。文件为 `construction-necessary-summary.json`，同canonical ASCII含LF；marker `construction-readback-complete.json`只说明这份来源scope读完。缺文件列为未起/失败，不自动判科学完成。全部恢复/prepare/factory/bind异常与未访范围按当前原字段保留，full factory ledger仍临时。

三新源不删除raw。root总体清理还必须等待BVP、postsolve/held、其余原必要读回和实际全部owner静止；不能仅凭一个早期construction marker撤掉C source panels/index、450 checkpoint或geometry。R426可继续需要原C四metadata及两source panel/index到metric完成；下游都须在该真实现场使用它们，清理后的SHA不能重建这个场。

## 10. 同钟的完整后继与未付范围

本来源链的目的不是停在BVP。root的205完整入口会显式注册当前 `actual202205` tuple，接R452的首次原construction政策以及原radial/atlas/shared/metric/reach/独立held。必须真有当前450接受才生成它的实际几何输入；原193/203 tuple不能替新source背书。真实R449初点也不使后继任意活动p自动继承最初factory域。

首次W/H/全部marker、材料记录和公共角责任按R437/R443/R447各自范围保；同数词不是自动全闭同g证明，R447消费者未调用就仍未付。若全112、453、450或下游预算未完成，读回保真实阶段与停止理由；不从job结论或部分成功推最终metric/reach/held/课题成功。

没有本地科学、import/AST/compile、fixture或benchmark。此稿只做源码阅读/文本派生、JSON来源/字节hash和完整diff。204/R446继续是另一条实际链；205实际R453的source/run/jobs只能在root正式发布之后从官方元数据绑定。
