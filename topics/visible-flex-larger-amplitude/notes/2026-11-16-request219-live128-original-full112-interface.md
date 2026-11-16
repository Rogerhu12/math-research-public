# Request219：actual63 原全112前缀、逐 H live128 与原 FD/fullDN 接口

> **2026-11-16 后续勘误与实际运行：** [R502](../results/R502-actual219-input-pin-failure-and-unstarted-live128-scope.md)记录 actual219 在准备阶段失败、科学与19200秒钟未启动。本页原 ledger-ready 表曾漏一个 `e`；该表现已改为原204/208合同的正确64字符 SHA（`edae34`），actual219 实际请求仍是当时错误的63字符声明。原21110B / bc484aa47e7f0ec15902ec78bacaf5a7509b331070f8e86c6046e9eeaac181e7版完整保在[f0c78734历史](https://github.com/Rogerhu12/math-research-public/blob/f0c787340f29734e17c9428ba7588e2a58ae665e/topics/visible-flex-larger-amplitude/notes/2026-11-16-request219-live128-original-full112-interface.md)。除这处表项与本说明，以下正文保留发表时叙述；实际执行范围以R502为准，原219请求/workflow/程序未修改。

作者：ChatGPT / exact_refinement（AI 辅助研究）  
日期：2026-11-16

**状态：完整可执行源与参数已准备；未执行 request219。** 条件实现结论为 [R501](../results/R501-live128-original-full112-same-call-executable-composition.md)，实际结论预留 R502。根发布后使用本仓库官方 `workflow_dispatch`，再核真实head/run；本接口没有预填run id，也没有修改Git ref。

## 1. 选择的原父与合同

本次选择原7ba实际设计的 actual63 完整前缀路线。保留原350分钟job、320分钟science、原有限profile、所有112偶频、全453前缀状态、三scalar controls及完整fullDN门。原7ba模板没有产生本条可继承的成功live父；不是从连续C的205/216改标签。

真实初始对象分开：

- accepted96仅是原profile/core的历史构造来源；
- actual63的全112、全453坐标 warm/status 是**当前未接受前缀初猜**；
- actual91 failed73 全577×224状态是**尾部初猜**；
- 每个真实H的128结果、stage/J与audit必须本job重新形成；
- 旧native61完成response不作为输入；不导入旧非零cache、旧W、旧J或旧域接受。

原78个public numerical source由未改113997恢复。新client实际需要 `topic/repro/source-root`；219明确传此目录，而不是把恢复函数返回的topic本身冒成source_root。原 `source_root.parent.parent==topic` 检查保持。

## 2. 公开执行件及精确字节

所有16运行源均小于100KB，合计376388B；数学C++展开、source diff与交接manifest不是额外Git发表件。334项完整pin位于request的 `source_sha256`，包括原组件、原full112消费者与actual63完整producer/import祖先。历史pin不表示该历史实验入口被执行。

| # | 文件 | bytes | SHA-256 | 实际作用 |
|---:|---|---:|---|---|
| 1 | [exact_20261116_binary128_live_response_projection.py](../computations/exact_20261116_binary128_live_response_projection.py) | 19902 | b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e | 准确 binary128 word/hex → binary64，一次 RN-even |
| 2 | [geometry_20261116_native128_live_scalar_source.py](../computations/geometry_20261116_native128_live_scalar_source.py) | 15897 | 06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b | 委托原 qualified C++，增加13/9 raw scalar出口 |
| 3 | [geometry_20261116_live128_actual91_seed.py](../computations/geometry_20261116_live128_actual91_seed.py) | 9131 | 219f5f8b26af05c17e596a1534e1fe5390c72ecb895de3b5606505525b8e429a | 全 actual91 failed73 artifact绑定，仅初猜 |
| 4 | [geometry_20261116_live128_final_components.py](../computations/geometry_20261116_live128_final_components.py) | 32027 | 2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866 | 同call四组件launcher独立来源view |
| 5 | [geometry_20261116_live128_response_assembly.py](../computations/geometry_20261116_live128_response_assembly.py) | 28584 | 08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb | 完整组件与投影 → 原 normal response |
| 6 | [geometry_20261116_live128_same_call_owner.py](../computations/geometry_20261116_live128_same_call_owner.py) | 18850 | 5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5 | 原持久128 owner工程view、same-call/deadline |
| 7 | [exact_20261116_live128_current576_system.py](../computations/exact_20261116_live128_current576_system.py) | 28975 | e37b13457b9dd9cbd0e918a2bf98988b5027b49fad5c54ffd824016dd2efa7c2 | 当前完整withJ十数组与R273来源绑定 |
| 8 | [exact_20261116_live128_current576_chain_qr.py](../computations/exact_20261116_live128_current576_chain_qr.py) | 21830 | faac8b013b9151ba92760962d4303c847301a9057834e7230ab37ea6d0c04b49 | 原完整R273 chain QR数学体 |
| 9 | [geometry_20261116_live128_current_call.mjs](../computations/geometry_20261116_live128_current_call.mjs) | 34356 | c20af799243d35a045c9c5be7900fbd19bb8b391acb9efb26fe9c5265566cd21 | 每次真实H捕获、literal/physical packet及同步call |
| 10 | [geometry_20261116_live128_call_pipeline.py](../computations/geometry_20261116_live128_call_pipeline.py) | 19240 | 137cc95996dca1d876640fb81e4fd3290d41e32e9b23027cb29d103b5cb0eda8 | clock/factor/solve-response三真实phase |
| 11 | [geometry_20261116_live128_worker.mjs](../computations/geometry_20261116_live128_worker.mjs) | 8167 | 8cc51b3e1a1c232c8b5769ef1cfc39261deb7aba84d0b8365b62cbf88c270b72 | 原36cf协议view、原warm与verbatim响应 |
| 12 | [geometry_20261116_live128_owned_process.py](../computations/geometry_20261116_live128_owned_process.py) | 9068 | 1516306f3ead5a5e8b54f389da172ef9544298b13ccf659c390cb874d26ed6a7 | pid/start-time/session/group及真实quiet |
| 13 | [geometry_20261116_live128_tail_client.py](../computations/geometry_20261116_live128_tail_client.py) | 30316 | 9f32e5ddd376016e51f678d9f0328727e63d8aacb5c4583046dc705949cc1894 | 原1cdf solve正文、newlive构造/close |
| 14 | [geometry_20261116_live128_original_full_dn.py](../computations/geometry_20261116_live128_original_full_dn.py) | 35318 | 63bbbefcfda8ae5761be314da743afc5291ad1a83749cf6d554003d429f5508e | 原7ba actual63→FD→fullDN数学体 |
| 15 | [geometry_20261116_live128_original_fullDN_owned_run.py](../computations/geometry_20261116_live128_original_fullDN_owned_run.py) | 29477 | 64126513260ad2790b9a5561a6536f43a1eadfde3313b0f20e19236bcb8c13a7 | 恢复原输入、一个19200钟、原rules与owned生命周期 |
| 16 | [root_20261116_live128_original_fullDN_necessary.py](../computations/root_20261116_live128_original_fullDN_necessary.py) | 35250 | a585f94bede489a1849e4776cac6909c6d0aad248102a1ac1fcccd8e56563888 | 单90KB必要返回、完整错误/未付范围 |

入口：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| [public-live128-original-full112-FD-fullDN-request.json](../computations/public-live128-original-full112-FD-fullDN-request.json) | 52615 | 1c9400110f65f5930f833142a85a48ce389df7f652c385fd2435676c369b251b |
| [.github/workflows/visible-larger-public-live128-original-fullDN.yml](../../../.github/workflows/visible-larger-public-live128-original-fullDN.yml) | 13262 | a32461ef6a9da97213391eebfa63ae1250573c5ee2909471b5281506ade133e5 |

相对原7ba模板的变化均是本条明确的真实来源、live响应、预算共享、生命周期和必要读回。原fullDN的profile/physical boundary/FD/full_argv数学体保留。没有把原context的source字符串改成旧源SHA后仍执行新函数。

## 3. 原始输入与恢复

六份输入仅在Actions通过固定历史commit/path/blob恢复。历史commit固定为 `8bd267107cc8710d371f3b62c02986655ac965b0`。完整path和Git blob在request逐项给出；下面只列必要角色和原内容身份。

| 角色 | 实际字节 | SHA-256 |
|---|---:|---|
| 原accepted96 gzip | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| actual63 warm-001 gzip | 4799943 | 6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a |
| actual63 status gzip | 231286 | 6443fce5e818ff20fd36075f6038ee60630d0b77e8ed2304d41e4d072ea6a005 |
| 上行解压后的原status | 1810333 | 8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46 |
| T112 config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| frozen ledger ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| frozen stored ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

actual63 run43646179305，原source `db6d728f30ee2d0c9ea62c96c622d8d85d2354b2`。status只解压，不重序列化后冒原SHA。原warm中的 `/complete_scalar_profile/complete_original_port` 全对象写入一个**新**临时port transport，记录其新的真实身份；不伪称这就是某个旧port文件的字节。

actual91原完整artifact：run43672150224，artifact14145200674，名称 `visible-mainline-modelresponse-43672150224-1`，source `b78f0dd1471a118d2ed21467602509d188c2ab67`，10267458B，SHA `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。未改98e transport继续验证完整ZIP及各成员。新seed仅从其真实原数组取初猜，不运行旧一word proposal，不把failed73改为converged。

原两个ready分别通过 `VISIBLE_FLEX_FROZEN_LEDGER_READY` 与 `VISIBLE_FLEX_FROZEN_STORED_READY` 传给原geometry。令牌仅在Actions环境；无用户PAT、token文件或日志。

## 4. 实际阶段与同call对象

顶层schema为 `public-live128-original-full112-FD-fullDN-request-v1`，request_number219。namespace唯一为 `$RUNNER_TEMP/visible-live128-original-fullDN219`。

### 4.1 准备与原规则

`owned_run.py prepare` 实际绑定334source、当前双README、六历史原件、actual63producer ledger、原78source与actual91 seed。只在返回后标preparation.complete，不由“目录存在”补成功。

`owned_run.py run` 创建一次19200秒deadline，随后启动独立rules session。其 `rules` 子模式导入原3b8，不改该源：先从实际checkout核当前root21bd/topicbff8，显式替换它的旧内嵌6183 baseline为已读当前文本并写 `rules-baseline-update.json`。原pull/rebase、2700秒同步、README变化终止、push竞争处理和H规则记录全部保留。

### 4.2 原前缀与client

science session先记录实际pid/start-time/pgid/sid，再exec新7ba view。原accepted/profile/warm/status完整检查及所有453坐标仍由原数学入口执行。它形成真实current H，构造一个新live client，不先导入completed61。

client的record prefix仍是 `science/full-dn/true-tail`。实际Node session和call目录位于 `science/full-dn/true-tail_live128/`。ready明确新worker/source、binary128 live组件和RN64投影算术身份。ready.linearD仍是原名义零/线性资料，不能替代真实新H/J。

### 4.3 每个未缓存实际H

调用顺序为：

1. 原warm/amplitude/tangent策略选择完整初猜；
2. 原complete withJ实际评价，完整十数组和current-H identity；
3. 新system/QR来源view调用原R273全行数学体；
4. 原61e literal packet与824 physical packet；
5. 原持久128 owner32×10及独立fresh replay；
6. 同actual128 final state的stage、boundary、mixed endpoint；audit按请求；
7. 全数组/word一次准确RN64投影；
8. 原normal response通过Node stdout原文发出，再写真实 `protocol-written.json`。

存在call-result不等于协议已flush。必要reader以 `protocol-written.json` 区分真实写出；不会仅从assembler成功或预期call序号补普通响应。

### 4.4 原FD与fullDN

首次current-H/J正常返回后，实际执行两组10方向原FD。这里差分的是固定真实response形成的仿射boundary实现；不宣称对非线性DN再次做了native差分。

fullDN原 `load_client` 接点返回同一个Pythonclient，其原H缓存仅在原条件下复用，不制造新call。fullDN的每轮新H仍调用同Node真实完整链。最后audit请求不能借前面非audit返回补齐。

## 5. 精确维数和返回内容

每call存储577×224 shooting状态；局部 RK 积分/变分是226状态，保两mean。stage完整576×224方向；boundary完整112 RHS；endpoint保存338 jets及请求的338×112混合J。状态表、局部状态和stage方向三种维数分别记录。

338jets顺序固定：height112、meanHeight1、slope112、meanSlope1、second112。物理scalar13项与audit9项的slot顺序由新qualifier原raw输出记录。residual和meanHeightToCut由原%Qa准确dyadic文本投影。所有原必须finite的字段继续finite；非finite不钳制，带实际位置返回失败。

原混合J含其既有有限差分/变分责任；没有将其包装成全338解析或整个IEEE程序的准确导数。若原stage为recorded-factor名义切向，其解释仍按原组件，未更换成理想Gram逆。

noJ接口也是真当前H。此实现可能为物理readout形成完整stage和endpoint J，summary明确“formed”与“returned by request”两字段；不宣称noJ成本已经降低。

可选tangent predictor只用本次实际已投影stage maps，原checkpoint是明确的RN64 state；跨H只作初猜。保留原完整prediction回退，没有额外对拍接受门。

## 6. 数学门与参数

原prefix/fullDN参数：

| 参数 | 值/范围 |
|---|---|
| field/tail M；spacing | 112；2 |
| 原角quadrature与warm N | 2048 |
| material / physical test angles | 4096 / 4096 |
| 原node heap | 6144MiB |
| jac_workers | 2 |
| fullDN max_nodes | 1200 |
| outer_iterations | 8 |
| extension_step / taper_fraction | 0.005 / 0.4 |
| R273 eta / exact_workers / factor bytes cap | 字符串"1" / 2 / 2147483648 |
| 原owner | 32方向 × 10trial，tol2e−9 |
| affine FD | 2×10方向；3层；2 Richardson；5e−5及原收缩 |
| prefix inner Newton | 原17trial |
| 原RMS / boundary门 | 1e−6 / 1e−11 |
| 原最终native与物理audit | 真正fresh执行，全原责任 |

初始current H由实际whole field计算，不是额外控制配方。原affine boundary、constant-core/parameter漂移、physical RMS、原域、二阶mean接缝和final cut audit都保留。最终finite-fullDN接受也不等于闭面目标完成。

## 7. 总资源与阶段裁切

选择原7ba的350分钟job、320分钟science。source/input恢复在科学钟开始前；一次19200秒科学钟开始在原rules初次同步及第一次native factory之前。所有未来H共用它。

| 资源 | 声明 |
|---|---:|
| 全科学绝对钟 | 19200秒一次 |
| 最后关闭/读回reserve | 120秒 |
| R273 factor process上限 | 19200秒，按剩余裁切 |
| owner / fresh replay | 6000 / 1200秒 |
| stage / boundary / endpoint / audit science cap | 8000 / 600 / 600 / 1800秒 |
| component threads | 4 |
| 初始临时可用空间计划 | 64GiB |
| 运行中free空间停止值 | 2GiB |
| 原outer最多未缓存协议调用 | 1+2×8+1=18 |

组件仍保原binding/compile/readback等开销和audit预留，实际allocations写原receipt。上述是上限，**不是每call拥有新19200秒**，也不是阶段可同时各用其上限。资源不足时保存真正pending/error；不改变数值接受阈值，不保证第一call或18call必能完成。

workflow沿原方式仅在必要时删除三个未使用runner SDK目录来满足声明空间，不删除科学数据。64GiB计划不等于已经证明全可能call峰值一定可装入；实际空间持续监视，达到原声明停止值则资源partial。

## 8. 进程、读取与清理

三个真实所有权层：

- outer启动的rules独立session；
- 原3b8启动、由science模式在exec前注册的science session；
- 新client启动且在ready前注册的Node独立session，其同步组件继承该组。

每层记录pid/pgid/sid/start ticks/uid/namespace/run。外层deadline或信号不会假定杀父进程就杀掉Node。quiet按已确认身份停止group，再观察namespace内进程；未知或不可读写者不被略过。zombie可明确记为不再执行写入，不与活进程混计。

必要reader先调用实际quiet，未证静止时不打开科学结果树，更不删除。其输出单独放 `$RUNNER_TEMP/visible-live128-original-fullDN219-necessary.json`。cleanup再核same request/run/source与完整必要标志，重新quiet，最后才删唯一namespace。必要scope完整记录了失败也允许cleanup；科学成功不是删除的额外条件。

prepare未返回、readback异常、字节超限或quiet未证，都只输出真实失败并 `removed=false`。不构造虚假的完整source receipt。实际清理结局待R502逐日志报告。

## 9. 唯一必要摘要

frame：

`BEGIN_REQUEST219_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY`  
`END_REQUEST219_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY`

schema：`R501-live128-original-full112-necessary-v1`。

compute与report使用同一原ASCII JSON（包含一个末LF）和同一bytes/SHA；report不重新序列化。joboutputs只传这份已受90000B上限约束的必要对象。原大state/J/factor/完整field只在同job临时科学消费，不上传artifact，不回Git。

摘要保：

- 完整实际call编号、请求flags/H身份、当前phase、protocol写出或未返；
- owner所有实际返回initial/trial/iteration/final必要标量、真实错误地址和未访后缀；
- stage完整范围与未完成RK/方向地址、boundary112、endpoint338×112、audit实际schedule完成/未付；
- scalar word和hex投影的实际来源，两个mean，原component总对象身份；
- 两FD组所有20方向的3层/2Richardson/2contraction及原判定；
- fullDN原outer history、所有原Newton observer返回的残差评价/失败地址、最后checkpoint身份、RMS preflight原返回范围、final原标量与两mean接缝；
- 全部非空真实stderr文字（surrogateescape→ASCII JSON逐字节保留）、原文件身份、实际rules/deadline/quiet/error与cleanup边界。

原Newton observer没有alpha/接受boolean，摘要不从checkpoint反推。原RMS writer只导出每fraction前24个invalid points时，必要view明确此原限制，不能说其他点地址已经读取。

相邻stage只有在必要字段严格相同且实际地址连续时共用一个透明半开范围；这不是编码或搬运完整科学树。所有实际原trial不因此去掉。

若完整必要对象超过90000B，只在临时目录保存原对象并返回其真实bytes/SHA、transport70和未返回范围；不得拆包、上调上限或截断后标complete。异常正文较大同样适用。初次尚无数值执行，本文不保证摘要实际必小于90KB。

## 10. 调用命令

仅在公开Actions job且实际request bytes已经绑定时调用：

~~~bash
python -u "$COMP/geometry_20261116_live128_original_fullDN_owned_run.py" prepare \
  --request "$COMP/public-live128-original-full112-FD-fullDN-request.json" \
  --request-sha256 1c9400110f65f5930f833142a85a48ce389df7f652c385fd2435676c369b251b \
  --namespace "$RUNNER_TEMP/visible-live128-original-fullDN219"

python -u "$COMP/geometry_20261116_live128_original_fullDN_owned_run.py" run \
  --request "$COMP/public-live128-original-full112-FD-fullDN-request.json" \
  --request-sha256 1c9400110f65f5930f833142a85a48ce389df7f652c385fd2435676c369b251b \
  --namespace "$RUNNER_TEMP/visible-live128-original-fullDN219"
~~~

readback与conditional cleanup由workflow的always步骤实际调用。source准备与正常Python/Node语法检查在Actions执行；无本地科学/import/AST/compile/独立fixture。C++数学组件只在真实需要的科学phase编译，费用计入同一science clock。

## 11. 相对旧实现的准确边界

- 原69c/204固定actual91 H和call1探针不被重标；新call模块真正接当前H。
- 原correction hook返回方向的接点不能独自提供live128 response；新pipeline另完成owner与组件。
- 原378 worker对solve返回的64位首阶覆盖不用于此入口；原36cf协议warm选择与新完整response明确组合。
- 原1cdf solve、原7ba FD/fullDN数学功能与原c6a fullDN主门保留。
- 原5e68限定工具保留；新physical scalar view写出额外原word，原数学公式不复制或替换。
- component summary传输70与实际科学complete分开；缺数据时不以expected shape补齐。
- 原3b8的旧内嵌root6183基线须显式更新至已读21bd；新receipt列旧/新实际身份，规则算法不改。
- 原source恢复返回topic，真正client参数必须是topic/repro/source-root；这一真实path接点已修。
- source闭包包含actual63 producer递归SOURCE_NAMES和原delayed lifted_modes_response c216；没有把几个直接import的pin误称全部transitive closure。
- 原科学stdout保本job临时；原所有error stderr与必要记录受单90KB真实上限，不能以绿色report代替科学结论。

## 12. 发表与下一次实际结果

主控唯一Git发布，不写ref/branch的detached blob仅供完整小源码交接。16运行源、request、workflow和本条两文稿为发表件；展开C++、临时数学数组、diff、交接manifest不入topic树。topic实际新增约0.47MB；最终以主控入库tree metadata为准。

新workflow同时有push-path与workflow_dispatch。因为主控恢复publication的GITHUB_TOKEN push不会自动产生普通push后继，正式发表后使用官方dispatch，核真实source/head/job；只有那时填写实际219身份。没有把当前已准备的源称作已运行。

R502需分列：真正进入的H与owner、全224/226/112/338实际完成范围、normal response、原FD、fullDN与fresh audit、资源或工程错误、单必要传输和实际清理。任一未开始阶段保持未付，不从334pins、组件SHA、返回码或job颜色补数学结论。

[已刊R493条件基础](../results/R493-current-H-live128-response-projection-and-original-fullDN-interface.md)；[R491原门责任](../results/R491-original-native-fullDN-gates-and-complete128-response-consumption.md)；[R501条件实现](../results/R501-live128-original-full112-same-call-executable-composition.md)。
