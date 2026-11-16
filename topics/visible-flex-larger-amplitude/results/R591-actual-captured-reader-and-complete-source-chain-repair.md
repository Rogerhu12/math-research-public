# R591 — actual239 的真实 captured reader 绑定修复与 request247 完整来源接口

作者：OpenAI / ChatGPT geometry agent（AI）。日期：2026-11-16（UTC）。

**可信度：已证明（限本节明确的源码条件构造、原来源关系及预算/读回合同）；request247 尚未运行，不填入任何科学验收、场值、误差或资源收益。**

## 591.1 问题及本次结论

本结论接 [R571 的实际239终态](R571-actual239-source-reader-binding-stop-and-complete-metadata-boundary.md)。该次官方 run 43891863925、source e396395de8ed0c124cd481d85a32e795aa795812，在公开 entry 初始化期间返回了明确的 ValueError：Use the current composer and actual generated metadata readers。原 result 的 scientific_computation_started 为 false，尚未进入十一层来源生成，实际 job deadline 也尚未形成。该结论只说明此次已返回的来源断点；不把随后缺环境变量的衍生错误当作科学求解拒绝。

真实源码不一致在 R570 composer.compose：其四个 metadata 名称中的 TWO_PHASE_READER 仍为旧 bound230 reader，而同一 composer.form_current_inner 经完整 R544/R567/R570 来源关系已经把 current_BVP_readout 和 metadata_sources 绑定到实际 captured239 reader。四项集合的严格相等检查因此正确地拒绝了不一致的内部合同。

本次修复把该一个常量改为实际 R570 captured239 reader 的准确名称，保留四项严格集合相等、完整 bytes/SHA、同实际 computations、实际 current driver/launcher/schema 和全部原科学门。新 request247 是独立的来源/metadata 后继；不修改、重派发或冒用 actual239，不把旧 reader 放回合同，也不令旧名字指向新内容。

新包只新增两个公开 Python 来源、一个六 metadata view 的完整 literal plan、一个完整 outer request 和一个 workflow；六个 metadata 输出由真实 Actions 在同 computations 中创建。原239全部618个来源逐值保留；新增3个公开来源及6个生成 metadata 来源，形成310 public＋317 generated＝627。原 R570 的56个科学/诊断/来源输出全部保留原字节，不为本修复重新复制数学内核。

## 591.2 实际旧对象与新对象

旧 composer：

- root_20261116_request239_sampling_refinement_composition.py，76607 bytes，SHA256 ebd89315edd17a1e9da8b49c73ec770e108213ef4f4c58d59ddaf0da92224d41。
- 冻结239请求54783 bytes，SHA256 6eb0b2572b8ef204b80e1c5d6172e902c0b37254d305f641cb11bef4f818812f。
- 冻结239 workflow91712 bytes，SHA256 f49152d9f22af88a35be61056117e07de7cd2d0e54ac985599a42a900b3a8c4d。

旧常量指向 root_20261116_actual202_bound230_coast_base_zero_linear_gzip_two_phase_necessary_readout.py，31492 bytes，SHA256 fecdc98d02fb420fa3146c1af197304cab199d798a119a1b15bce37dbefbfbbc。

真实 current reader 是 root_20261116_actual202_captured239_coast_base_zero_linear_gzip_two_phase_necessary_readout.py，32662 bytes，SHA256 508885ca68dc0500a8bd5923b2cfb90746ebb118bc4fd25a83cb5160d153a7e9。它的实际 schema 仍是 R505-actual202-coast-base-zero-linear-ten-two-phase-necessary-readback-v1；R570 已显式改变来源及 capture 选择，并未改这个 schema。不能仅凭 schema 一样就把两文件混为同一来源。

该实际 reader 硬绑定 R570 first driver 的51960b10…和 launcher 的3d6e1224…，完整选择原 sampler、真实 design453/frozen450 两阶段与 same-call cubic 记录。R591 不改它的源码、选择范围、LIMIT、FD/final/quiet 条件或必要帧。本次只有其上层 metadata 名称与真实 current 描述统一。

新的四项 ADDITIONAL 为：

| 成员 | 实际用途 |
| --- | --- |
| root_20261116_request247_sampling_refinement_composition.py | 本次公开 composer 自身 |
| root_20261116_current_C_gzip_sampling_scope_necessary_readout.py | 已发表完整 gzip/采样必要范围 |
| root_20261116_actual202_captured239_coast_base_zero_linear_gzip_two_phase_necessary_readout.py | 原 R570 实际两阶段/capture reader |
| root_20261116_coast_base_zero_linear_gzip_rule_resource_readback.py | 原真实规则/资源必要选择 |

集合恰有四项，没有放宽成子集检查，也没有无来源的别名兜底。尚未生成的 captured239 文件，在初始化时只是与完整来源计划逐字段一致的 deferred descriptor；declared_source_identity 不把声明冒充实际文件回执。之后仍须真实执行全部来源生成和源字节绑定，才进入原科学程序。

## 591.3 完整来源集合与生成次序

设 P239 和 G239 是冻结239的 public 与 generated 来源集合。本次两个公开 Python basename 和一个 plan basename 都是新名字，六个 metadata 输出也都与原311个生成名字不同。新集合为：

$$
P_{247}=P_{239}\cup\{\text{composer247, entry247, plan591}\},
\qquad
G_{247}=G_{239}\cup\{\text{六个metadata247输出}\}.
$$

因此来源数量为307＋3＝310、311＋6＝317、总计627。这里是显式来源表的集合关系，不是“所有可能 Python import 已自动证明”的泛化声明。原 runtime/source-map 检查仍在真实 Actions 对每项执行。

十二层的顺序和基数如下。前十一层整个描述、原输出与身份保持；新层只有六个 metadata 输出。

| 索引 | 原职责 | 输出数 |
| --- | --- | ---: |
| 0 | R464 完整 incremental-M 来源视图 | 15 |
| 1 | R483 coast Bernstein 来源视图 | 5 |
| 2 | R487 原三层 coast/union 来源 | 13 |
| 3 | R496 当前 zero-linear 来源 | 49 |
| 4 | 完整 gzip writer/decoder 来源 | 51 |
| 5 | 原 R503 coast-base 来源、222 source-only 分类修复 | 46 |
| 6 | R559 原 historical217 八项＋R544 四十九项 | 57 |
| 7 | 原230六 metadata 来源 | 6 |
| 8 | 原235六 metadata 来源 | 6 |
| 9 | 原 R567 prefix tube 与 metadata 来源 | 7 |
| 10 | 原 R570 same-call cubic 完整来源 | 56 |
| 11 | 本 R591 六 metadata 来源 | 6 |

新 plan 使用已发表的原 R496 ordinary literal generator：root_20261116_current_C_zero_linear_source_views.py，11895 bytes，SHA256 4d4c507edd571b67655fd2e66fb4bcfa173b1239928443831a81a925c4869ec4。plan 的物理 schema 保持 R496-current-C-zero-linear-three-level-source-view-plan-v1，独立 logical_schema 为 R591-actual-captured-reader-and-metadata-source-plan-v1。

plan 中有20个具名 literal before/after、37次带准确 occurrence count 的应用，六项 baseline/output 各自含完整 bytes/SHA。它只把实际239 metadata 新命名为247、显式级联 composer/owner 的真实身份、登记十二层及317个输出；不重写 R570 科学文件。required_public_sources 仅列两个新 Python 来源；JSON plan 本身仍在完整 public/source-plan 绑定中，不再误塞进只收.py/.mjs的 source-only 清单。

六个新输出如下；完整 baseline 和全部 literal 操作就在计划内，不能用本表替代生成计划。

| role | actual basename | bytes | SHA256 |
| --- | --- | ---: | --- |
| meta_owner | geometry_20261116_request247_owned_roles.py | 25736 | 135dd5bb30081c2b2067086093c6cb37ea332f02567e502a0b0baede23d869f8 |
| meta_runner | geometry_20261116_request247_joint_refinement.py | 48824 | 702bc37f82e1fab4cbc5b81693ba9e903b5e458b98351cb047c16ff85229be6b |
| meta_reader | root_20261116_request247_refinement_necessary.py | 44584 | 3535c678c017bd5c44dda8e5333deb4814e1b8d53d53bca16f507fa9fe57531e |
| meta_same_composer | root_20261116_request247_same_C_composition.py | 33381 | 67d50c732ef1c4ccbf35e2eb489944d2daa0783b906dfc1e3c5c4b90b4f84047 |
| meta_same_runner | geometry_20261116_request247_same_C_refinement.py | 45658 | e0d791a5c2938af7d0fb2a76dcc743f0f6812fc860dc41aa268f41e459f43388 |
| meta_same_reader | root_20261116_request247_same_C_necessary.py | 35746 | 549e1791274e97a17e1154419ffeff46c552ccdb729294eb071a2c67a6ab8132 |

旧 six metadata 仍先真实生成并保留，随后六个新名独占创建；不会覆盖旧文件，也不在旧 module 全局猴补后仍称旧来源。新 owner 真实加载新 composer；新 joint runner/reader 真实硬绑定新 owner。same-C composer/runner/reader 通过当前 outer 的真实 descriptor 绑定同一条新来源。

## 591.4 条件命题及证明

**命题591-A（原科学输入的来源保持）。** 假设本次 checkout 含全部冻结来源的原字节，公开 entry 和所有原来源步骤在既有资源合同内正常返回，且实际 source/result 身份检查全部成立，则本次 formed inner 中原科学对象、各原阈值和工作预算等于冻结239所选的同一来源对象；由该对象进入的全部 R570 科学/诊断输出字节保持不变。新 metadata 外层不生成或预填 accepted parent、native 数组、C 叶值、quintic/cubic 系数或 metric 误差。

证明如下。entry.contract 首先绑定完整冻结239请求及 workflow，检查 same_C_work、scientific_scope 和原 retention 的各具名成员完整相等。execution 只允许 metadata_working_view 的来源说明变化；数值预算对象恢复后逐值等于原239。原222的修复仍从完整冻结220原文和已发表 literal patch 真正形成，先核其完整 derived220 身份，且原 roles/native_registration/execution/refinement_work 关系保留。

form_current_inner 读取完整 core/metadata/tube/cubic/repair 五个当前计划，按每个 baseline 完整身份递推。旧 R570 科学 descriptor 在 repair plan 中没有后继，所以逐值保持；只有六个 metadata descriptor 和相应 metadata schema 转入新输出。所有旧 public 项按原 SHA 加回，任何同名不同 SHA 都仍拒绝。最后将允许改变的来源/metadata 成员恢复为祖先对象，要求其余对象完整相等；execution 与 refinement_work 另外仍检查原样相等。

current_dispatch 的数学输入仍取完整原205子合同，通过原 R503/浅逆/全场/完整native来源的既有明示分支形成；本次没更改该函数的数学及数值选择正文。其白名单之外的所有原205成员仍完整相等；scientific_parameters、inputs、construction_inputs、construction、selected_construction、actual180_selection、query_recipe、finite_head、deep_far 均保原对象。已发表的 sample_inverse_depth=2 继续真实传播，除此之外 native_sampling.parameters 等于原205对象。来源映射和工作时钟没有被当成科学数值。证毕。

**命题591-B（具体集合断口关闭）。** 在同样前提下，新 composer.compose 的声明四键集合与其 ADDITIONAL 相同；actual239 那一个确定的旧名称差异不再存在。

证明：真实 R570 重绑定的 first_reader 已是 captured239 的32662/508885…对象，本计划不修改该对象。新元数据四键只把公开 composer 自身换成新247名字，其余分别是原 BASE_READER、这个 captured239 reader 和原 RULE_READER。新常量恰为 captured239 完整 basename；集合四项没有重复。strict equality、file键等于basename、来源表完整 SHA 和后续实际 materialization 检查均原样保留。因而由已知两个不同 reader 名称造成的原不等式被消除。该命题不保证此后所有其他工程检查、资源、采样或科学条件都通过。证毕。

**命题591-C（资源与未付范围不升格）。** 元数据初始化、生成或读回失败不能被此修复变成科学成功、quiet 证据或清理授权。

证明：entry 在复制前只建立一次 namespace 起点。实际 deadline 来自该起点及原18900/2700，未完成初始化时仍允许 immutable source scope 的独立 necessary；其标记不声明 process quiet。generation readback 独立记录十二层实际返回、当前索引、完整声明地址及失败/未访。超限仍70、不写完成marker。cleanup 先要求源生成必要标记及原body身份，再交真实 same-C composition/necessary/quiet 和原 refinement reader，后者保全部原所有权观察与清理条件。各层不能以路径存在、SHA、step成功或不可读文件代替值和完成范围。证毕。

本次增加来源准备工作，因此不同实际运行可有不同剩余时间和资源停点；“数学来源及参数保持”不等于承诺两次浮点轨迹、实际工作量或完成状态相同。

## 591.5 保留的科学范围及明确未付

以下来源仍由原完整链实际执行，R591 未改变其算术、门或预算：

1. 同一准确 C/root 语义的原完整1440 head、六primitive、cut和全部112 far/单位行族；浅逆depth2为原work分配，32bit仍work-only，完整逆像、所有候选、完整原节点计划和异常未访不能省。
2. 原 R503 显式 coast-base 初猜与原453完整求解；只有真实接受后才固定实际末十词并重新支付完整450。full current H、338×112 J、原FD、fullDN、final/audit都仍真实执行，不删453三行充450。
3. 真450 parent 后的 R456 同far五factor refinement，以及 R462/R463/R464 真新增模态 union、全新M deep/grid/native/J/BVP与末门。旧112 Q/Pi 的来源、原μ词、Pi新列偏移和全部family误差仍按原已付合同。
4. 当前真实 radial、R413原cuff、准确cut patch、两帽、完整四Loewner/闭DFS、block reach、held/含反射完整像、三层真实误差测量/比较和临时显示。metric/reach通过不成为相互或后继额外门。
5. R489/R492/R500/R504/R544/R567/R570 实际 same-C 两slot，保同一个真实 field/CP/definition/十词和材料来源的范围，真实重算 C head及query；原 coarse enclosure 后备与全root/domain责任不丢。
6. R570三实际 driver 的同次 sol.sol.c 捕获；原九个完整member、phase状态、全部地址/错误、准确 Q−C* 与真实 Q−C_lit 区别、rho_lower完整归一化及原全prefix退休/未访责任。capture/diagnostic unpaid不成为BVP或metric拒绝门。

原 R575 连续Fourier尾项/alias库并未因本修复而自动调用；其实际后继仍由单独 R576/241 处理。R591 也不声称有已接受450、完整闭面metric/reach/held、测得误差下降、机器精度平台或原solver容差到全域metric floor。原同C输入宽度/全tube正域/FFT表与RHS形成误差等未付边界继续以真实结果为准。

## 591.6 原钟、路径及输入输出合同

唯一 base 保持：

    $RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205

这里205是既有运行namespace的合同名，不是复用actual205的文件、时间或结果。新临时工作视图：

    $RUNNER_TEMP/request247-runtime-metadata-workspace

公开entry从真实原checkout读取来源，namespace-created timestamp先于复制、literal formation及源准备。原checkout/source/ref/index不改；工作视图的.git只引用原真实对象库。环境脚本为：

    $RUNNER_TEMP/request247-runtime-env.sh

它声明 REQUEST247_PRIMARY_WORKSPACE、REQUEST247_RUNTIME_WORKSPACE、GITHUB_WORKSPACE、VISIBLE_BASE、VISIBLE_COMPUTATIONS、REQUEST247_CURRENT_INNER_SHA256 等实际值，并进入真实工作视图。每个实际run块仍显式source该脚本。COMP为视图/topics/visible-flex-larger-amplitude/computations；其模块HERE必须等于这个真实目录。SOURCE_TOPIC保原已恢复、位于base内的实际原source树；proof-directory是工作视图中的results。

不可混淆以下四份对象：

| 对象 | 路径/身份责任 |
| --- | --- |
| 原冻结220 request | 原checkout中99218/f6ca6387…，源祖先只读 |
| 原222 repaired220 | 按冻结原文literal形成，99330/2d1c3a7d… |
| 本次实际 inner247 | 工作视图中的原220固定路径；schema/number为247；完整bytes/SHA只能由本次formation实际取得 |
| 本次 derived205 dispatch | base/request220-derived205-dispatch.json；原205 runtime schema/索引保留，source map等明确派生，deadline.request_sha256绑定这份真实全文 |

实际inner另原字复制到base/refinement220-request.json，所有原后继以同一实际SHA使用它。原220文件名和205 runtime schema是被保留的接口路径，不能用于混淆本次run/source。新outer是独立247 request，必须使用下节公布的完整SHA。

科学仍原18900秒，读回2700秒，合21600秒且job360分钟；原BVP maximum7200、既有sampling/linear相位预算和未来reserve、free门以及各几何cap都保持冻结子合同的实际值。32GiB startup门不下降，完整gzip从首行写入并由原stored/decoded消费者读取。source-generation多一层不重开任何钟，也不保证剩余预算够。

same-C仍每个真实head总1800＝1650 head＋120 cut必要＋30 child shutdown；metric240、measurement300、comparison120，以及terminal measurement/close reserve900。所有cap裁实际同一个全局deadline；display仍保原末900，measurement/compare只用其原终测规则。原TERM→KILL、PID/start-time/session核定、OwnedTree/child.wait和quiet观察正文保持。

## 591.7 公开及生成CLI

所有命令仅由本次公开Actions执行。下列是实际调用合同，不是本地执行指示；完整参数值和shell guard都保存在当前workflow全文。

先在原checkout执行新entry：

~~~bash
python3 "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/root_20261116_request247_actual_source_entry.py" initialize \
  --request "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/current-C-captured-reader-refinement247-request.json" \
  --request-sha256 42547b2d206c9a783dad9f10724770523edcd92e935ffda2869b02536cc12f04 \
  --base "$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205" \
  --computations "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations"
~~~

随后每个run块source实际env，使用同一个base/COMP。两个request参数组必须区分：

- **outer参数组**：新current-C-captured-reader-refinement247-request.json及42547b2d…，用于新entry、same-C composer/runner/reader。
- **inner参数组**：工作视图原220固定路径或base/refinement220-request.json，SHA取REQUEST247_CURRENT_INNER_SHA256，用于公开sampling/refinement composer、owner、joint runner/reader。不得把outerSHA传给inner caller，也不得填旧f6ca或2d1c。

所有常规metadata CLI还要求 --base 和 --computations；实际commands如下。

| source | command/附加参数 | request种类 |
| --- | --- | --- |
| public entry | initialize；readback；cleanup | outer |
| public entry | guard-cleanup，--new-composition-outcome、--new-readback-outcome，完整“-- cleanup …”后缀 | outer |
| public sampling/refinement composer | materialize、generation-readback、prepare、verify、readback | inner |
| generated owner | prepare | inner |
| generated joint runner | rules；原rules内部run；--source-topic、--proof-directory | inner |
| generated joint runner | witness；--input、--input-sha256、--computations，原现场生成输入 | 原显式input |
| generated joint reader | readback；component带--role/--directory/--out；cleanup | inner |
| generated same-C composer | bind、preflight、prepare、readback；cleanup带两个outcome及原后缀 | outer |
| generated same-C runner | rules；原rules内部run；--phase first或successors，--source-topic、--proof-directory | outer |
| generated same-C reader | 无position command；--prepare-outcome、--first-outcome、--successors-outcome | outer |

public composer仍保initialize API，然而本工作流只由公开entry创建namespace；不再独立调用composer.initialize重开钟。materialize顺序创建十二层。same-C bind/preflight再使用完整冻结222 PYPINS，经原四项精确metadata替换，核真正247当前workflow，而不是旧220。该原PYPINS的科学断言保持，包括本次仍为原单worker采样schema；本修复不接R556两worker，不触及234特有schema断口。

owner.prepare原样做完整来源和原Actions语法处理；两项历史syntax-only exclusions仍来自原合同，不能因此跳过任何实际当前source或数学条件。新56科学源不在生成前伪称文件存在，真实生成后才进入角色加载和源恢复。

科学顺序仍是原全C/head/cut/far/sampling、实际初点绑定、真正453→450、首次完整闭面；随后same-C first slot、原真实mesh→incremental-M与完整几何/evidence/display、same-C successors与比较。slot可以保partial，不能用metadata结果补造任何前置场。各个同场same-C八角色的实际来源创建receipt仍是原R570 materialization；六metadata247的receipt仅证明metadata来源，不能代替科学源创建或科学完成。

## 591.8 必要scope、帧和实际markers

原所有必要选择、失败记录、原partial与未访地址继续保留；没有为加一层来源删除字段。无必要正文时，保实际原件identity和真实未返范围，不能凭SHA重建值，也不能将0/null/缺失互换。

新metadata帧如下；BEGIN_与END_分别包住表中stem。原科学caller自己的帧/schema保持旧真实值，包括captured239 reader的R505 schema和same-C cubic evidence的REQUEST239_SAME_CALL_CUBIC_COMPLETE_METRIC_EVIDENCE。

| scope | frame stem | 实际必要/marker路径 |
| --- | --- | --- |
| entry原始完整metadata | REQUEST247_ACTUAL_SOURCE_BINDING_NECESSARY | request247-source-binding-readback/summary.json；request247-source-binding-readback-complete.json |
| 十二层generation | REQUEST247_COMPLETE_SOURCE_GENERATION_NECESSARY | source-generation247-readback/summary.json；同目录readback-complete.json |
| 完整来源composition | REQUEST247_SOURCE_COMPOSITION_NECESSARY | request247-composition-necessary-summary.json；原request220-composition-readback-complete.json |
| 原三层refinement | REQUEST247_REFINEMENT_NECESSARY | 原refinement220-readback完整scope及当前schema |
| same-C来源注册 | REQUEST247_SAME_C_SOURCE_COMPOSITION_NECESSARY | same-C247-composition-readback/summary.json及其marker |
| same-C两slot/evidence | REQUEST247_SAME_C_COMPLETE_NECESSARY | same-C247-readback/summary.json及其marker |

entry marker schema为request247-current-C-source-binding-entry-v1-readback-complete-v1；generation marker为request247-current-C-actual-source-composition-v1-generation-readback-complete-v1；composition marker为request247-current-C-actual-source-composition-v1-readback-complete；same-C necessary marker为request247-complete-same-C-consumer-readback-marker-v1。所有marker仍绑定实际repository/run/source/必要body身份，不预填未来ID。

source-generation读回逐层保generator、plan、实际返回、完整source_rows、current generation、未访问后缀及全部原stderr/error。其已声明的重复来源provenance字段仍按原具名选取保存原件identity；不声称全original JSON每字均回传。entry scope返回其完整原result metadata和真实namespace-start；仅immutable scope完整不等于过程quiet或科学完成。

每个既有语义body仍单90000bytes。source composition保持原具名关系且只在严格更小时使用；source generation/科学necessary仍按实际body大小返回。大于90000仍exit70、保完整临时原件、不给成功必要marker；不分片、不通用编码、不把旧overflow descriptor冒fullscope。本次新增来源会增加部分metadata体积，**没有证明所有实际结果必定能装入90KB**。任何工程失败/体积超限仍按实际明确未返，不用空值代替。

report保原五份primary正文、原generation/refinement必要transport合同；新same-C几何/measurement/compare正文仍在compute独立frame，report仅转其identity/outcomes。原capture raw临时保在实际BVP phase；同slot原cell ledger也只临时保。可再生raw、necessary输出和大日志不入Git或detached blob。

## 591.9 成功、失败和清理路径

正常初始化完整返回时，entry的actual_derived_request、actual_derived205、actual_composition、actual_job_deadline及env script都是本次实际文件回执。随后有真实materialization/owner prepare、原完整科学/读回才各自支付对应责任。

若初始化尚未形成env，generation-readback的workflow分支明确报告actual_source_entry_did_not_form_runtime_environment；新entry.readback仍可读取同job原result及namespace-start，必要范围只限该metadata。它不把未生成的科学源或未访问的scientific stage填成失败数值，也不会制造jobdeadline。后续原always步骤在缺路径时保持真实失败/未起，不能以这些step标签作科学结论。

guard-cleanup先验证本次generation marker及完整必要summary identity、实际inner请求身份，然后才转交实际generated same-C composer。后者保新composition/necessary/quiet和原phase owner的全部责任，再转公开entry.cleanup；entry核自己的scope marker、真正completed preparation及derived205/inner文件，最后exec真实当前refinement reader.cleanup。原205原所有role/outcome/quiet及全部必要条件不减。

失败源生成、必要body超限、缺失marker、未知process范围均不授权删除。metadata scope完整既不表示所有源创建成功，也不表示原BVP/closed scope通过。cleanup step的退出状态不代替实际removed事件；只有终态实际事件才可说明raw是否删除。至此之前raw保留在同job，Runner自然销毁与主动已核删除分开记录。

## 591.10 运行文件身份及交付

下表列本次五个完整运行/入口文本。六metadata展开只在Actions由plan创建，未将展开副本重复存入Git；完整plan含其全部来源及修改。

| role | basename | bytes | SHA256 |
| --- | --- | ---: | --- |
| composer | root_20261116_request247_sampling_refinement_composition.py | 77251 | d7520c1897ee3bbc53d60fdd9f2a6ebd21d24f13e46b8712acbe99d0a79446c2 |
| entry | root_20261116_request247_actual_source_entry.py | 38200 | 156d6738ae064af53e66420ecc5f59d291b2c2f1878ec1dbe6134483c00e6847 |
| plan | r591-actual-captured-reader-metadata-source-plan.json | 11508 | f48be38bc84853fb3fb411bf39e52c56349239244ad3dcd89c94aab9c386090d |
| request | current-C-captured-reader-refinement247-request.json | 59436 | 42547b2d206c9a783dad9f10724770523edcd92e935ffda2869b02536cc12f04 |
| workflow | visible-current-C-captured-reader-refinement247.yml | 92020 | 11bf60e5d66a13c96c9e1914d331031cde78f116203c0138a500e8092059205b |

workflow完整92020 bytes，小于原100000单文件界；没有为此删科学步骤或改变clock。它保原workflow_dispatch实际入口；未来只由根端按完整发表tuple单次dispatch，实际run/head/jobs另由官方回执绑定。此文没有request247实际run或source_head值。实际结论号R592只预留，不在本证明中提前填验收。

本次作者完成的是原全文来源、literal替换、字节hash、请求JSON及调用/清理控制流的文本构造；未执行项目科学源码、import/AST/compile、数值短跑或fixture。原Actions中的源准备和语法步骤仍在实际workflow按原范围执行，不新增独立检查作为派发或科学接受前门。

## 591.11 来源和后继责任

直接源码依据为 [R570完整来源结论](R570-actual-same-call-cubic-current-field-and-complete-source-chain.md)、[R570完整接口](../notes/2026-11-16-request239-same-call-cubic-complete-chain-interface.md)、冻结239request/workflow及本次新完整literal plan。实际失败范围只引用R571的唯一终态必要返回，不重复取旧日志、不使用其raw为新输入。

原R569准确rho修订、R553全coefficient tube及R521条件常数、原R504/R489完整same-C源责任保持；R575的完整Fourier投影缺陷尚需实际caller单独支付。一个reader集合绑定修复不能证明该数学或数值责任完成。当前可行动的下一步是通过这个独立完整入口重新形成同job真实父与全域consumer结果；若预算/原门/来源/必要transport仍停，则以实际返回范围继续原问题，不把本源构造当完成证明。
