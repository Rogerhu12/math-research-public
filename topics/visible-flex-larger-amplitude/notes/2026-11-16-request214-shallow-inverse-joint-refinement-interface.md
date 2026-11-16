# request214：浅逆采样、完整450父与同 job mesh→M128续链接口

作者：ChatGPT geometry agent（AI）  
日期：2026-11-16  
状态：独立源码/请求/工作流封口；没有本次实际run或科学结果。条件结论见 [R482](../results/R482-shallow-inverse-and-same-job-incremental-refinement-composition.md)，未来实际结果预留R484。原209、212及其在跑入口不改。

## 1. 实际组合与边界

本次以原205的完整current-C、全根族、cut、真实far、actual202准确十族candidate、full453→冻结末十词→fresh450、原全部终门和首个闭面链为首级；只把原逆像工作深度24改成2，并用已刊R477的两reader完整保存原点/栈未付字段。随后在同job原临时件仍在时接原209的R456五因子细化，再接R464的完整M128旧112+新增模态union和新有限求解。

depth2**确实传播到三层采样**，因为原209 `solve_input` 两分支都继承首级 `native_sampling.parameters.sample_inverse_depth`。本次不是只改变首级的实验。32bit目标仍work-only；1M尝试上限、完整field计划、原候选并集、原误差与所有科学接受规则不改。

全部有限求解、当前H、完整J/FD/fullDN/final/audit重新执行。首级或下一父未真实接受，后继不能拿partial、历史状态或哈希补成父；几何/误差/display不通过也不成为额外BVP拒收门。没有在本次接口中给未来parent、p10、H、K/τ证书、metric误差或效果填值。

本次只新增四个标准库调用/metadata源。R456/R462/R463/R464/R459/R461数学源与原15源视图生成表逐字沿用，不复制未变核，不覆盖既有文件。

## 2. 完整基线与实际来源集合

原205请求 `current-C-actual202-accurate-ten-closed-geometry205-request.json` 是97406字节/SHA `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`；原205 workflow95760字节/`726d97e1aada5d34ddfa949753ce59c6909122d3de8c39bd5a2160fdb8712c36`。原209请求36220字节/`aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009`，workflow96476/`1c53b3c27ab531b99308150a7213e15d17717c57cff846b1dbffe0ffc9e5d65a`。原212请求9965/`8803750dbb21bcc24e0809e7bdc4389c567de9b8a10532d52b42b2f7a7ee30bf`，workflow99644/`d1022e74a6217d582f08692b2458bb4d20a3a5dec61ba4dc88907a27e13c3cc0`。

composer逐件核这六份完整字节，并检查原209的全部执行参数、数学role、原witness、实际family、proof和15view映射相等。旧source归属保留：

| 集合 | 实际件数 | 语义 |
|---|---:|---|
| 原205 | 154 | 全部原source pin保留 |
| 原209在205之外 | 91 | 包括旧metadata祖先，不重标成214 |
| 原209 published并集 | 245 | 逐成员保持原SHA |
| 本次新增composer+两R477reader | 3 | 首级派生合同154→157 |
| 本次新增owner+runner+reader | 3 | 加到外层原91件map，故该map94件 |
| 本次全部published并集 | 251 | 相对最初154净增97件 |
| 原R464实际生成views | 15 | 不预先下载，不覆盖旧名 |
| 本次运行闭包 | 266 | 251+15，无集合重叠 |

当前源/入口identity表见末节，完整集合逐键保存在小外层请求。`additional_source_count=97`是相对原154的全并集净增加；`additional_source_map_count=94`是外层map本身的长度。三件首级metadata已在157内层中，不能再重复计数。

来源继承只支付代码/输入绑定，不支付任何历史科学数值或未来接受。原212、209的run不作为本次parent，也不下载其巨raw。

## 3. 四新源与真实schema

| 职责 | 实际basename | schema |
|---|---|---|
| composition/初始化 | `root_20261116_request214_sampling_refinement_composition.py` | `request214-original205-and209-explicit-shallow-refinement-composition-v1` |
| 来源+拥有进程 | `geometry_20261116_request214_owned_roles.py` | `R482-request214-owned-nested-role-v1` |
| 完整续链 | `geometry_20261116_request214_joint_refinement.py` | `R482-actual205-contract-incremental-M-refinement-evidence-and-displays-v1` |
| 必要读取/清理 | `root_20261116_request214_refinement_necessary.py` | `R482-joint-refinement-one-necessary-readback-v1` |

独立外层schema为 `public-actual202-shallow-inverse-incremental-M-joint-refinement-and-displays-request-v1`，`request_number=214`。其实际workflow是 `.github/workflows/visible-current-C-actual202-shallow-inverse-incremental-M-refinement214.yml`。

原组件仍要求的内层schema为 `public-actual202-accurate-ten450-closed-geometry-request-v1`、`request_number=205`。这只保API，不等于原205完整字节没改。内层实际文件 `request214-derived205-dispatch.json` 与随后完全相同的 `dispatch-request.json` 有新的现场SHA；`explicit214_composition`和独立receipt明确实际214/current run/source。任何验证实际dispatch的分支均读这个现场身份，原06ae仅作为被核对的原基线。

首BVP实际reader为已刊R477：

- `root_20261116_current_C_sampling_scope_necessary_readout.py`，55606/`47d7ec771331f417dffb783a79e02d1ae9720e9ad0a699a72c37cf3031718cb2`。
- `root_20261116_actual202_sampling_scope_two_phase_necessary_readout.py`，30114/`6e40dc6365246113d8abc07110582a030b4930195070a71ba08e9872a11bb1e7`。

外reader真实schema `actual202-complete-sampling-scope-ten-two-phase-necessary-readback-v1`；frame `BEGIN_ACTUAL202_COMPLETE_SAMPLING_SCOPE_TEN_TWO_PHASE_NECESSARY`/对应END。它实际加载新BASE，旧80c2与19878只保祖先身份，不能只改receipt标签却调用旧选择器。工作流后检和最终清理也使用这个新schema。

## 4. composition白名单与唯一namespace初始化

所有源位于当前checkout `topics/visible-flex-larger-amplitude/computations`；composer要求其 `HERE` 就是该真实目录。原source视图也在此产生，新名字必须原先不存在。

原namespace保持 `$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205`。一次 `initialize` 先建立新目录，完成明确派生与receipt，再复制原14815字节/f779c6a2 owner、核原d926cecf BVP模板，并在原创建位置写唯一startup deadline。这里只把原YAML的标准库初始化搬入可绑定源，不增第二时钟，不改owner算法。

派生仅允许：depth24→2、三metadata pins/sourcecount、当前reader四identity字段、workflow路径、`explicit214_composition`。将这些字段恢复后必须与原205 JSON完整相等。原209的所有科学work/role表也直接与已刊原件相等。此为原来源合同的实际绑定，不是新数值测试或独立科学接受门。

后继既可从checkout请求进入，也可从唯一 `$BASE/refinement214-request.json` 副本进入。composer明确只认这两个实际路径，并要求副本全文与checkout相同；receipt中的outer file始终标明checkout相对路径。没有开放任意同schema路径。

metadata生成后，原workflow预检把准确派生字节写成 `dispatch-request.json`。实际deadline的 `request_sha256`是派生SHA，原06ae只在composition来源中出现。已有startup timestamp、后续BVP actual_job_deadline及原recipe关系保持，原后继继续从真实BVP返回的deadline receipt读取，不能拿另一个尚未生成文件补钟。

## 5. 完整CLI与真实调用顺序

以下命令仅在原公开Actions环境执行。`COMP`是当前真实computations，`BASE`是上述唯一namespace，`OUTER`是checkout中的214请求；`OUTER_SHA`见末表。源内同时核 `GITHUB_ACTIONS`、repository、run/source和实际路径。

### 5.1 唯一初始化

```bash
python3 "$COMP/root_20261116_request214_sampling_refinement_composition.py" initialize \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
```

它写 `request214-derived205-dispatch.json`、`request214-composition.json`、`request205_owned_process.py`和`job-science-deadline.json`，并向 `GITHUB_ENV` 写真实 `VISIBLE_BASE/VISIBLE_COMPUTATIONS`。目录已存在则不覆写。没有从旧job续时间或续raw。

`verify`接相同四个选项，只重核原件和实际派生；在首级dispatch尚未写出时允许只核derived文件。`prepare`保留为一次独立metadata写入API，不是本workflow的第二次初始化；它不创建科学钟且不能覆盖实际receipt。

### 5.2 原首级预检后生成全部15views

```bash
python -u "$COMP/geometry_20261116_request214_owned_roles.py" prepare \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
```

此步先绑定完整251已发表源，再真实调用原68ae7071 generator，在实际 `COMP` 创建15个新basename。只有全部文件已经存在且其完整bytes/SHA与冻结映射相同后，才绑定新view/新role。原Actions语法预检在此真实文件存在之后执行；作者没有在本地执行它。准备结果在 `source-preparation214/result.json`，生成器原receipt路径由原 `source_view_generation.receipt_directory`保留，不能猜写另一个目录。

### 5.3 同job真实科学续链

```bash
python -u "$COMP/geometry_20261116_request214_joint_refinement.py" rules \
  --request "$BASE/refinement214-request.json" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --proof-directory "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/results"
```

工作流外层仍使用原剩余science秒数的TERM/KILL timeout。`rules`调用原3b8b6dd5 live-rules runner；由它真实创建exclusive session，再进入内部 `run`。不能从普通共享PGID绕过此入口伪造owner。`witness --input --input-sha256 --computations`仅由该runner为当前真实field生成原四个witness，使用实际cut/atlas源，没有从旧pieceindex或旧数值点接用。

源内实际阶段名单保持：`level0_measure/display`；`level1_solve/geometry/witness/held/measure/display`；`level2_solve/geometry/witness/held/measure/display`；`compare`。每个实际文件、退出、拥有进程、未启动原因、未返scope及原资源裁剪保存到 `refinement214/result.json`，不由job标签补全。

### 5.4 composition及完整精化必要读回

```bash
python -u "$COMP/root_20261116_request214_sampling_refinement_composition.py" readback \
  --request "$OUTER" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
python -u "$COMP/root_20261116_request214_refinement_necessary.py" readback \
  --request "$BASE/refinement214-request.json" --request-sha256 "$OUTER_SHA" \
  --base "$BASE" --computations "$COMP"
```

两者都是always路径，前者外层timeout以原timestamp+21600剩余裁剪；后者的实际metadata子进程共享原读回截止时间。composition失败不会阻止后者尝试读取其余实际范围，但其缺失会使本次完整读回为false并阻止清理。

`component --role --directory --out`是内部metadata子调用，另需相同request、SHA、base、computations；它只使用冻结原reader/held的实际builder，不起第二个科学求解。`cleanup`用同样request、SHA、base、computations，仅在末节全部条件通过后删临时base。

## 6. 三层精化和原完整门

首级全C仍f12f完整1440片、六primitive、原cut-point及whole-natural query、真正full112深端/far和原全物理field计划。candidate用原actual202 R449准确词/原source绑定；原finite构造、连续族、native数值代表及准确C根族的区别原样保留。

首个实际56cb driver/227e launcher返回accepted450后，R456接其真实CP。level1所有五因子均2：径向mesh、field/native角、native steps、material角、physical角；`max_nodes=2400`是资源容量，不能删原parent节点/literal knots或宣称一定够。原Hermite插值仅初猜，fresh450/H/338×112J/FD/fullDN/final/audit都重新付。

level2接真实level1接受父，M128、其余四因子均1。实际新分辨率从新父继承，不把steps回填成首级12。原112 complete far族、完整候选/误差及实际μ字按R462复用；新全M深界仍重付，新增16频率真正传播，Q/Pi槽放置按新M，全部新native/J/完整M有限方程与末门重新执行。R464 sample/configure两调用和真实新config来源不改；sampler full未付返回分支保持原件。

每层成功后都重新做radial/cuff/shared、live C查询metric、完整块reach及held；同一旧几何结果不作新几何成功。首A/B、完整W/H/marker与材料定义用于原共同目标绑定。缺B只使共同材料measurement角色未付，不阻其不需要B的solver或原physical-angle显示。

三级measurement与compare都调用同一新R464 evidence view，family依次 `original112/resolution112/incrementalM`；三级display都调用同一R464 display view，family依次 `current112/resolution112/incrementalM`。不混旧R459结果schema；level2 held只认新R464 post tuple及其实际必要frame，不能用旧R451包装替代。

## 7. 全部原资源计划

| 项目 | 原显式计划 |
|---|---|
| job / 原namespace | 360分钟 / science18900秒+readback2700秒 |
| 首级C / far-sampling | 原C3600；linear14400、sampling1800 |
| 首级预留 / BVP最大 | 未来BVP reserve3600；实际BVP cap7200且服从剩余 |
| level1 | sample900，refinement7200 |
| level2 | 全M deep300，sample12000，refinement7200 |
| 各场几何 | radial600、cuff120、shared300、metric600、reach600 |
| 各场其他 | witness120、held300、measure300、display120；compare120 |
| 末端与停止 | terminal measurement reserve900；child shutdown30；启动8GiB、运行free2GiB |
| measurement | 256bit、sqrt128、起始角深2、maxdepth20、100000 cells、逆映射80、phase cells100000 |
| measurement标量 | width goal `1/100000000`；原reference eta `1/1000000`，均不是本次新增接受阈值 |

上限全部按真正原剩余时间clip，并不意味着和小于18900或所有阶段均会执行。display调用仍保末900，measurement与compare才能使用终测余额。原prior阶段binding/setup计时边界、原namespace计划非统一绝对杀钟、各step/job硬限区别照旧，不能扩大宣称。

native采样的原参数除深度外完整保留：precision256、maxpanels25M、linear maxdepth32、norm1/4、defectbits12、Taylor24、cache65536、free2GiB、valuebits32、1M attempts、初始steps12、representative maxprecision4096。它们是原执行参数，不是已完成计数。

## 8. 固定g误差、全t及显示的准确范围

原R459的真实广义谱误差上下界用于三级比较。严格上界下降只能证明上包围改善；若新上界小于旧下界才足以证明真实sup严格下降；重叠记录未分辨并继续原预算内调用，不加拒收门。原solver/RMS/native的容差不被改名成relative-metric floor。

全t metric上界依赖原准确相位共轭、全角覆盖、两帽固定和同目标拉回的完整条件；有限t点不是替代。实际time-subdivisions依次4、8、16，原四common witnesses在prefix公共u=1/2、q=0/1/4、上下两侧，全部来源留原evidence。

显示每层仍physical-angle-image，t集合分别 `{0,1/2,1}`、五个quarter点、九个eighth点；grid为prefix8、tail8、cap4、angle32。每个owned显示文件严格小于5000000字节，由实际producer核；完整vertex/radius/file只同job临时，必要读回保每frame状态、完整file身份、误差极值与当前未付。这里没有承诺全部显示可完成或任何文件已存在。

README要求的真实加密误差下降至机器精度或原solver容差仍是实际证据责任。有限两后继、同一eta多次pass、一次误差比较或几张display都不自动满足它，也不新增“无限精化”或跨级全C²收敛前门。

## 9. 必要scope与不完整返回

原C、cut两jet、deepfar、construction、BVP、closed、rules七项全部照旧。首BVP实际R477多保八项原点/栈字段，不限缩为count/hash；R456与R462的完整未付行按原reader正文保持。不存在的原键不补为零、empty或成功。

精化scope读取全部实际阶段、每个solver原接受/未付、原全几何结果的必要责任、measurement bounds/compare、每一显示frame/error/maxima、全部原异常与未访。完整成功大数组、巨大ledger只记录原身份和明确范围；不是在聊天中逐值复核这些raw。

composition frame为 `BEGIN_REQUEST214_SOURCE_COMPOSITION_NECESSARY`/对应END。它是独立小来源对象，不是将大科学结果切片传输。精化frame为 `BEGIN_REQUEST214_REFINEMENT_NECESSARY`/对应END，schema在§3。完整composition在compute一次输出；精化summary只引用其完整identity/marker及派生来源，report不多传一个全体。

每个原必要90000字节限制保持；完整失败/未访极端多时仍可诚实70，不承诺一定装下。overflow或必要scope未返不写complete marker，不先删未读raw。原first closed的三份完整必要体仍留compute，report只传其identity/outcomes；原五primary加精化单体沿原report，不增加全部几何raw副本。

实际exit/科学/读回/静止分责：数学或资源partial如果其全部必要scope完整返回且quiet，可以沿原合同完成读回与清理；transport partial、未知owner、未回传原错误或缺marker则不主动清理。job红/绿本身不决定方程、metric、reach或held是否成功。

## 10. marker与唯一末端清理

清理读取实际九个step outcome：`C_READBACK_OUTCOME`、`CUT_READBACK_OUTCOME`、`CONSTRUCTION_READBACK_OUTCOME`、`FAR_READBACK_OUTCOME`、`BVP_READBACK_OUTCOME`、`RULES_READBACK_OUTCOME`、`CLOSED_READBACK_OUTCOME`、`REFINEMENT_READBACK_OUTCOME`、`COMPOSITION_READBACK_OUTCOME`，均须success。

然后逐原件核：BVP新schema完整scope与summary bytes/SHA；rules complete+quiet；closed205同run/source marker与summary；construction marker与summary；composition当前外层、实际deriveddispatch和完整receipt；新214精化marker/summary/source；原f779 owner.observe；actual BVP-owned group；全部新214 run/role/readback拥有进程与未知namespace范围。现有七scope条件一项不删。

新增composition marker：`request214-composition-readback-complete.json`，schema `request214-original205-and209-explicit-shallow-refinement-composition-v1-readback-complete`，字段repository/run_id/source_commit/complete/necessary_summary/derived_dispatch/outer_request。

新增精化marker：`refinement214-readback-complete.json`，schema `request214-refinement-necessary-readback-complete-v1`，真实source、同run/source、complete/quiescent、necessary_summary、actual_refinement_result。缺失不推填。只在全部条件后删 `BASE`；没有上传raw/artifact、提交临时数组或从另job搬运完整field。

## 11. 工作流、边界与发表清单

本次workflow使用独立path触发/并发组，文件97252字节，低于100000。原YAML namespace初始化移入真实bound composer，原首级科学块保留，15源生成顺序保持；其差异文件完整包含上述移动、派生depth2、实际reader/schema和新调用来源。不是为了缩文件删掉原数学流程。

运行所需新发表物只有四Python源、小outer request、workflow，以及R482/本接口。已刊R477两个源只作为输入引用，不重复发布；其余无改动依赖不复制。`publication-files.json`、六完整diff、作者标准库文本builder和临时metadata计数回执仅供交接，不进Git作为额外归档/审计前门。

未做本地source import、AST、compile、fixture或科学运行。Actions中原实际语法/来源预检仍留原位置；这不构成作者会话里已经执行通过的声明。本条也没有代替root的唯一Git/push角色或宣布当前212/209的终态。

## 12. 最终完整字节身份

| 文件 | bytes | SHA256 |
|---|---:|---|
| `root_20261116_request214_sampling_refinement_composition.py` | 25592 | `7ca365978dfa491c64dd94554b0e7470d2785e1d99fa249d847f2e76bf4c8949` |
| `geometry_20261116_request214_owned_roles.py` | 25558 | `5b9e90394a363b1a93e07a167676be8b764a049e08a07057f9f877bd9dd3ebb7` |
| `geometry_20261116_request214_joint_refinement.py` | 48849 | `39f1d36cf2f50fad633963130530ff430d5324e578ee068df52db0b9ed09313c` |
| `root_20261116_request214_refinement_necessary.py` | 42106 | `b4106f39d1ecd0fa74f1412afb5b25d34e80892c406e50ccdb71c1bbcb424eff` |
| `current-C-actual202-shallow-inverse-incremental-M-refinement214-request.json` | 42062 | `c81530feca5c61e9a901937abf2e5c2704562f6eeaff0cbb70b817ec48519fe1` |
| `visible-current-C-actual202-shallow-inverse-incremental-M-refinement214.yml` | 97252 | `9ce8515103cae3388330bcabad08164a52a7d22d5e34ead248db5f26bba8565e` |
| `R482-shallow-inverse-and-same-job-incremental-refinement-composition.md` | 16368 | `6ad857f474e95149a6051c91ce941b5eb1fc11d49dfbd97ad132f64791ece8b9` |

四新运行源均各有完整baseline unified diff；小请求及工作流各有相对已刊209完整diff。本接口自身identity由交接manifest列出，避免自包含hash。实际recipe、派生dispatch和未来结果的SHA只能由本次真实Actions产生，不在此表预填。

