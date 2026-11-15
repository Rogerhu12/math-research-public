# Request193：连续十族真实453求解后，同参数完整冻结450的现场接口

作者：AI。日期：2026-11-15。本文是可执行源和来源合同；没有预填未来 run、科学读数或成功。实际结果编号保留 R408。此请求沿已发表 R400，把当前准确定义的连续十族接入两个实际完整问题。旧187、R400及任何原科学源不改；新入口由根唯一发布并由请求文件的 push 触发。

## 1. 本次明确要做的工作

起点是 actual180 已实际选择的准确九系数，加一个明确的正零 $\xi=0$。独立十族 factory 在本作业真实运行，消费本作业重新计算的原连续 C 及 cut 二阶读数。随后七个形状坐标冻结、原前三个坐标活动，实际解完整453维物理 DN 问题。只有原求解器真实接受、现场 R400 checkpoint 写完并绑定成功，才将该实际末十词全部冻结，建立另一个完整450维问题并真正求解。

450 保留全部338物理状态、112 core未知数及112右端条件。它的 $K=0,k=0$，左端338行；453 的 $K=3,k=3$，左端341行。450的新初猜可保留父453的前450行，但它必须重新评价全部450 RHS、原全域预检、当前 H、原 FD、原 nonlinear fullDN、完整338×112最终响应和新最终审计。删去父三行不产生450接受。

这不是旧字面 Gauss 十族的重标，也不是旧九族 factory/result 的改名。新准确十族、新有限 compiler 和实际 current-C native 保持各自身份。有限原求解器接受不证明准确连续目标的同场误差、全局 $C^2$ 接缝、闭合、嵌入、reach 或无限模 DN。

## 2. 唯一请求及九件发布清单

源码和请求均落在题目 computations；工作流落在仓库 .github/workflows；本文落在题目 notes。完整字节身份如下。

| 角色 | 文件 | bytes | SHA256 |
|---|---|---:|---|
| hooks | `geometry_20261115_continuous_ten_full453_frozen450_live_hooks.py` | 10762 | `bedb6ca2e926cb2dd689246bc3ca47f561c5a5055d2e8c24237daf98bda88812` |
| driver | `geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py` | 33794 | `11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8` |
| pipeline | `geometry_20261115_selected_coast_continuous_ten_pipeline.py` | 28580 | `be5b2bbf2b8f032c7e690753ce9df4ae737d2ecec37d8c3a1e1129a6a7dc42f3` |
| launcher | `geometry_20261115_continuous_ten_full453_frozen450_launch.py` | 19366 | `6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66` |
| owner | `geometry_20261115_continuous_ten_two_phase_owned_process.py` | 14019 | `138ea16a6a8d3ff1b39bbb934e2837810bff218a6aecba19ed08a46fb4af278c` |
| reader | `root_20261115_continuous_ten_two_phase_necessary_readout.py` | 25701 | `622f4f3c8255a4980e931457f912cca1ee00d25af965da18f39aecc6860c8d72` |
| request | `public-continuous-ten-current-C-full453-frozen450-request.json` | 79920 | `052c4fb1ad153e93578826d3e8270e8e2c3a06b486f62409def0386518184780` |
| workflow | `visible-larger-public-continuous-ten-full453-frozen450.yml` | 83716 | `e4bab919f784a3933e4ac76f2bd32d7c6cc148cf38f2fc663ff0886319c311c0` |

本文自身身份由同目录 publication-files.json 列出，避免自引用 hash。该清单和完整差异供源文本审阅，不是新增科学验收件，不要求提交其本地回执。所有新正式文件均小于100KB，没有把可重算数据编码或拆分入库。

请求 schema 为 `public-continuous-ten-current-C-full453-frozen450-request-v1`，request_number=193。工作流只监听这个新的请求路径：

`topics/visible-flex-larger-amplitude/computations/public-continuous-ten-current-C-full453-frozen450-request.json`。

独立临时 namespace 是 `visible-continuous-ten-current-C-full453-frozen450193`，不修改187的请求、工作流、目录或真实运行。触发前本合同不宣称已存在193 run。

## 3. 实际来源、准确点与十族

原187完整接线基线为 commit `6a272aae6a3a0ac864bb2c5769bcf78a6a2312c8`。原 driver 63965B/ff66783d6491d56fd3b5b64f7be00849f744f08441811bf764608ae79619e248；原 pipeline 41592B/1738fbb7fe1ca5211fb09442d14e740b2363c7d6c5d5daa14dd26c5f60a60d9b；原 launcher 19281B/847bd309b5fac867e8ab20adf4d307c199eece10eccdcdca431d419e9c9527f5；原 owner 14004B/ff9ef5d0a5512a1ce6d6bb78a087f6a2a97c6c23defddcba3c901eca747c6be8；原必要 reader 51108B/34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9。

actual180 的 run 为43753422569，source为636bbc30601cb577266219ed66bb2759d285badc，原 report job132932432397；必要 summary 64284B（不含末LF），SHA为503d2e7d86359c687842e5ce2d5161cac951c7a0b80c5d2b08f5bec3231dcafd。原选择 $\beta=1/16$ 的九系数，只作为本次明确起点：

$$
(0.3055213835477326,\ 0.21645013203050154,\ 0.021418782473590154,\
-0.06322334619266512,\ -0.01747451701873286,\ 0.05860072306016053,\
1.0751306255033548,\ 0.6886900390922872,\ 0.058658947547659664).
$$

代码以恢复的准确有理词与 binary64 逐词可表示性为准，上述十进制展示不替代原 binding。新顺序固定为
$$
(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3,\xi).
$$
前九项原 control_terms 是 support 0、1、2 上 power 0、1、2；第十项是 support1、power4。准确半径形状及其一、二阶导数都来自同一个半径多项式。支撑和自然总长不依这十个系数，不把原 s 与公共 u 混用。

本次 $\xi$ 冻结为正零，活动坐标仍严格只有 $p_1,p_2,p_3$，七个形状坐标索引为3…9。局部准确形状在 support1 的0、1/2、1处三jet全零，不足以断言完整第十响应列为零；实际积分、RK和其他内部采样可以看见内部形状。此请求既不活动第十列，也不增加非零列或秩通过条件。完整初猜网格和新 RHS 在 Actions 临时原件中保留身份。

独立十族三件不在本次改写：

| 源 | bytes | SHA256 |
|---|---:|---|
| geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py | 46691 | 72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682 |
| geometry_20261115_continuous_ten_fixed_power_scalar_numeric_v3.py | 24933 | 7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd |
| geometry_20261115_continuous_ten_fixed_power_augmented_v3.py | 6474 | a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f |

## 4. 真实恢复与准确定义的限制关系

pipeline 只复用冻结187的 actual180/165 官方日志恢复和已发表原165 DAG重建；不会重做已付418片/选定 coast 的域搜索。原165数据仅在 Actions 临时扫描；原参数、selected recipe/definition、原cut和输入字段按原SHA和来源重建，不据receipt猜正文。此部分采用同原恢复的认证和超时，不把 token 放入科学子进程或输出。

接着执行新的十族 factory.main，得到真实新 result.json、准确 definition 和实际 model recipe。原九 recipe 经显式零 $\xi$ 扩展，不伪造旧 factory schema。新构造 source 为72c4635e…；旧0d89370d九 factory只作为准确限制及数学源码基线保留。

限制比较保以下责任：

- 新旧同一准确 core几何、cut有理数、连续 C原root族语义、宽度和 $\kappa$ 等recipe。
- 准确 base DAG、pieces、supports、自然坐标与长度字段逐canonical比较。
- 前九准确有理值全部相同，第十准确为零；新增项真实 source/schema/control_terms和零jet声明明确。
- actual180 的准确全419片、全原root族初点域证据只传到这个同一准确初点。不同作业的外包盒、run、result SHA不是同一个证据文件，不能冒逐字相同；它们也不改变被绑定的准确语义函数。
- 原或新数值影子、活动参数改变后的域、任何旧J/FD/fullDN接受不从该传递自动取得。

factory仍付原两次区间域尝试（每次300秒、65536 cells、depth32、sqrt256bits），保其真实成功/未决/失败。当前域 flag不被新代码提升为第二个BVP接受门；依原流程保真实return code和存在的定义。若没有可绑定的实际definition或来源协议失败，下游缺输入而止，不称数学不存在。工作流各必要读回与后续原责任保留 always 分支。

## 5. 98、61、69、29、78是不同的来源集合

不能把原84前置表称为完整runtime闭包。精确区分如下：

| 集合 | 本次作用 |
|---|---|
| 原187的84命名前置pins | 全部原字节保留；作为完整旧接线基线。 |
| 原187实际导出的61 entries | 原driver的55直接 PINS，加实际core.FROZEN_SOURCES/family.SOURCE_PINS的并集及原driver自身。 |
| 新driver实际导出的69 entries | 在该61责任上加入本次hook/driver、R400 profile/checkpoint、连续十3件与实际物理依赖；writer记录其真实并集。 |
| 当前native29 | 保187实际positive-endpoint/完整112far及原所有worker配置，不减源，不换旧graph。 |
| 本次前置98命名pins | 原84 + 六新运行/读回源 + 五已发表连续十/R400源 + 三个原来已被实际源码引用但未进84表的旧源。 |
| 原恢复78源 | 原历史manifest恢复集合，与上述集合有交叠但有独立路径/作用，仍沿原公开恢复机制。 |

三个追加旧源不是新数学：

1. normal_terminal_projector d6c6f1308f678cae77750b33977d41f2bdb8d355f345d43bcb3f68b1e9e7d47d 与 normal_bvp_continue 3baf49eea03a12baa3da452a53e57bfe6b25e1e77f6ceb8da066a2e7d63c1ce8，原core.FROZEN_SOURCES已经读取/hash绑定；本次把它们明确写进派发表。
2. r225_free_core_bvp 23914B/a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08，由R400 CurrentTenProfile.SOURCE_PINS实际绑定；物理数值源不变。

Actions用纯AST字面量解析这些PINS并校全文件SHA，不import科学模块来核source集合；之后真实科学入口自行核原来源。69也不被宣称穷尽所有Python传递import。请求中保完整原84值，并记录补充3项的来源理由。

R400 profile 为30299B/3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6，checkpoint为36989B/43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae。其证明和四源已发表于d7621c59f8ab870f7852fa49b6f8328593915ba2；本次只消费profile/checkpoint，不执行SavedPrefix、metric或径向消费者。

## 6. 初猜、完整453及五个cut量

原accepted96文件仍作为真实core几何、原目标和构造metadata来源；699×453完整原初猜也是显式种子。恢复原历史文件，不将未收敛field或旧native锚冒成当前接受。新flow在公共u重新对应新自然长，对全部物理338/core112行保原seed，三活动行替换成明确起点，并重新形成全部453 RHS。原node/mid及两单元内RMS采样域预检照付；新增节点仍受原max_nodes1200。

低三目标为显式 $\lambda=0.001$ 乘原accepted96的三core系数，不以低三诊断先达阈值为新增开跑门。高109 core未知和全部112边界行没有被删掉。

profile自身有限编译的 E、Ep 和据此计算的 backgroundSlope/Second保其原形成路径。真实native当前H返回以后才比较 radius、E、Ep、backgroundSlope、backgroundSecond，原isclose阈值仍 rtol $2\times10^{-11}$、atol $2\times10^{-13}$。新native值不会覆盖profile目标的这些量；这项有限比较也不成为准确实接缝证明。

PhaseLease把原core.close限制为本阶段租约结束。driver才拥有真正raw client；首次当前H前立即将引用写入finally责任，故第一调用/FD异常也进入原owner关闭。第二阶段复用同一个worker的真实warm状态，但新H仍调用原solve，不从父响应缓存产生接受。

## 7. 完整原求解器和现场 checkpoint

hooks只替换原main实际构造入口、标量spec、独立边界/flow和lease，不改原 complete-band、Newton/QR、RMS、BC、线搜或最终审计正文。原完整main确实创建本次CurrentTenProfile的flow/boundary/SeparatedBoundary，hooks保存它们的实际对象。

原接受JSON的source、schema、profile、metric字段保持原core写出的字面值；新的producer责任放到独立R400 manifest，不覆写原fullDN后再假称原件。R400 writer只有在原main已实际接受后，才从当前现场对象捕获：

- 原actual.json.gz、FD anchor与完整response-check、最终实际native fullJ/audit。
- 当前flow维数、真实K/k、338物理/112core、实际十个binary64词及其准确dyadic值。
- 该现场原raw owner/config/geometry/source、完整577×224 native状态和338×112响应的原身份。
- 当前H由原trace重新形成的比较、原physical cut audit、完整mesh/state/RHS/profile责任。
- 父checkpoint仅来源和初猜，不继承当前接受。

若原求解器接受后writer/capture失败，原main接受和checkpoint失败分别如实保存，session success不得因原mainflag被推成整个两阶段完成。旧core JSON的fixed_modes=3元数据不被默改；manifest另列实际K=0/k=0及该旧metadata不是当前K的声明。450接受必须从它自己的真实原main取得，不能靠metadata标签。

成功checkpoint的关键schema为
`R400-current-continuous-ten-complete-physical-DN-checkpoint-v1`；
193主status schema为
`current-C-continuous-ten-live-full453-to-frozen450-physical-DN-v1`。
阶段prepared/row.started表示原完整预检已返回，不表示此之前完全没有source setup、profile构造或RHS尝试。异常scope不得据false started虚称“零科学”。

## 8. 两阶段实际衔接

第一阶段成功checkpoint写回以后，代码从manifest的十个float64小端词构造固定点，调用R400 freeze_at_current_state，保持实际旧主flow对应的点/批两条有限路径。全冻结view不复用未接受参数。fresh450_seed只提供种子，并按新450flow重算所有RHS。

新450的target为空，core112仍全部自由；左338/right112全部原完整行。其affine tail新建，原preflight和当前H重新求，FD及最终native审计都重新付。父453当前响应/affine不被直接用作450锚。

主driver记录两条预先声明的phase状态；没有开启的后缀保留。以下结果分开：

- 453原接受未付：450未启动。
- 453原接受成立但checkpoint/冻结/450准备失败：记录已付453范围与真实异常，450不冒接受。
- 450已启动但FD/native/线搜/预算/审计失败：记录其真实已做/未付，父453不代它通过。
- 两个真实问题及各自checkpoint均完成：有限两阶段 success可成立；所有闭几何、准确同场误差及后续径向责任仍未付。

## 9. 原预算、运行依赖和完整进程责任

不增加任何科学阈值。配置保原Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0，Node24.22.1/heap6144MiB，BLAS单线程、jac_workers2。原native32次×10档、eta1、sensitivity_eta0、tolerance $2\times10^{-9}$，原QR子进程1800秒不变。每一fullDN问题仍原8outer/17档、RMS $10^{-6}$、BC $10^{-11}$、FD $5\times10^{-5}$、max_nodes1200、material/physical angles4096。

两个问题共享一次7200秒BVP进程预算；第二阶段不重置它，也不重开worker。元数据36是原协议进入次数上界说明，不作为新的调用次数停止门。单次native容量不是整两阶段总容量保证。

前置资源仍沿187：C3600秒/step75分钟；恢复step25分钟，原180report transport180秒、原165parent660秒、重建parent330秒；factory900秒/step20分钟；完整far step5分钟；原sampler linear14400/point1800秒与step285分钟。真实startup按原namespace剩余时间和保留BVP7200秒共同clip原采样两预算，原argv/有效argv均保存；binding/setup不冒计入sampler内部phaseclock。

namespace18900秒、读回保留2700秒、job360分钟；原BVP step135分钟实际仍受剩余namespace与7200共同限制。18900是原启动资源计划，不声称已有对所有前置阶段统一绝对kill。至少34GiB起始空间、运行2GiB reserve不变，超时/空间/外部signal是resource partial，与数学拒绝分开。

owner保原pid/start_ticks/pgid/sid身份、隔离science组、信号转发、wait/reap和静止观察。原rules_runner SHA3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde及2700秒真实pull/rebase机制不改；只注入已实际读过的README baselines。git merge.stat=false避免无关大blob diffstat；不改数学源。

## 10. 单份必要读回与清理

新的metadata reader以冻结187 reader为原文解析工具，不import科学模块，也不重新算科学maxima、矩阵、域或解。每份语义summary仍为单份ASCII JSON、含LF、≤90000B；没有把大科学树编码/切段传输。

193 BVP necessary返回：

- 本作业launcher真实启动/退出/资源/静止记录，两阶段全部状态及异常/未访后缀。
- 实际sampler各已存在mode/未付范围及原错误；成功112far完整区间表只整体identity，Actions内仍读取原件。
- 每阶段原FD全部已存在方向、三误差层、两个Richardson层、两个收缩比和原flags；表只合并列名，另保原key-set以区别absent与null，不删失败。
- 每阶段原fullDN必要状态、原终审计与cut量；checkpoint成员按原SHA全核。成功场大数组只身份，不经工具传输。
- 同一个实际native目录只读一次。全部原trace/trial/linear-child原记录在Actions内parse；每个call的最后实际iteration trial标量全部返回，较早native trial及成功factor大表只identity。
- 全部失败/未完成linear-child与首末实际child保必要字段，成功每RHS大maxima表只identity；不声称root逐值读过这些未输出的大表。
- 所有实际owned file总字节scope、原日志错误索引、读错及省略索引identity。原目录缺失按未开始/失败说明，不以空目录冒完整科学。

单份上限若实际超出，输出诚实over-budget小失败，exit70，complete=false，不写成功cleanup marker；不抬90K、不伪complete、不改科学acceptance。容量是实际结果属性，本源未以本地科学或假fixture预测保证其一定足够。

各不同语义原C、cut、far、construction、BVP必要摘要沿原report job接口分开保存；这不是为重建一棵大数据树拆包。R400完整成功成员留在本次临时目录直到全部必要读回完成。

读回成功不代表科学成功。只有原所有必要readback结果和marker按SHA/当前run/source一致、owner静止且原cleanup合同满足，才删本请求可重生目录。科学失败但必要记录完整可以依原合同清；必要读回失败/超限主动skip，静止原件只随runner生命周期消失。活跃process、未静止partial、别的请求目录不删。

## 11. R409、SavedPrefix与未来同场消费者尚未执行

本次没有调用R409 radial replay/shared-field，没有调用R400 SavedPrefix/prefix metric，也没有新增几何plan/assembly/B/closed-surface结果。将来需要的输入合同是实际450 checkpoint目录及SHA、同job native geometry、实际worker/source配置、computations和source-topic。这个现场输入槽本身不是已经执行的几何。

本次450 raw仍在原必要读回成功和owner静止后按规则清理。未来不能凭193摘要、SHA或接受flag复原被清理的450场。若要接R409，必须在新的真实453→450重生作业内，在真实450接受后且清理前显式接入；或者本次后续经独立已声明协议保留真实现场，但当前请求没有这样的改变。R409计划参数未在此预选，不能由本接口预付未来plan。

特别是父点准确域传递、有限current-C代表、fullDN数值接受及完整连续metric/tail/几何证明是分开的责任。新pipeline不会把actual180准确全域证明扩大为活动p改变以后全部参数或新field通过。

## 12. 可执行入口和完整差异

工作流完整调用关系为：

1. 创建独立namespace、复核98源码与原输入、恢复78source/原历史seed；保持原真实规则同步。
2. 完成原连续C、原cut twojet及actual180/165必要恢复。
3. 新pipeline construction真实调用十factory，生成当前十recipe、definition、input binding及该实际recipe SHA绑定的deadline。
4. 原同C全部112 far和positive-endpoint sampler真实运行。
5. 新launcher启动本driver一次；driver顺序进行真实453和450，保存两个现场checkpoint/全部原输出；finally关闭唯一rawowner。
6. 原owned-process静止后新reader输出单份必要scope；原其他必要读回照付，最后条件cleanup。

driver CLI沿原accepted/complete-seed/factory/tail-config/source-root/out/work及各真实SHA输入；generated recipe在
`continuous-ten-BVP-input/current-selected-ten-full453-frozen450-recipe.json`。
launcher只接受本作业真实该recipe/namespace/deadline，不把旧179资源模板当实际新参数对象。request中的 scientific_entry 仍指前置原连续C入口，current_BVP才是本次完整两阶段入口。

交付差异包括新driver、pipeline、launcher、owner、reader、request、workflow相对冻结187各全文diff；hooks另提供来自原original_full_solve的完整源级差异和自身全文。它们在独立工作目录可逐字重建，不依赖隐去的局部patch。现阶段只做文本/JSON/字节来源操作；没有本地科学、import、编译、AST或测试，也不据源码检查宣称实际已跑。原Actions自己的AST/bash等前置原样执行，不新增fixture、数值验收或root复核门。

## 13. 既有论据

- [R400：连续十参数与冻结450、完整同场度量绑定](../results/R400-current-continuous-ten-frozen450-and-complete-prefix-metric-binding.md)。
- [连续十族源码设计](2026-11-15-continuous-C-fixed-power-ten-source-design.md)：准确profile、s/u和新增shape责任。
- [R380：原连续C正端点Prüfer与Robin责任](../results/R380-continuous-C-Pruefer-angle-lifts-and-oriented-Robin-enclosures.md)。
- 请求中保R300/R323/R357原证明、实际180和原187输入源身份；不以本文替代任何实际结果。
