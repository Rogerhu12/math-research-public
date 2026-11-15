# Request171：同一 Actions 原37八批后接真实38查询的完整接口

日期：2026-11-15。本文是独立源码和执行合同；尚未为171填写未来 run、末场、接受或数值结论。所有新科学只在公共 Actions 执行。原155和其37科学源码保持原字节。

## 1. 已付依据与这次唯一科学扩展

原 [R344](../results/R344-actual155-eight-complete37-pairs-and-unselected-left462.md) 完整读回 actual155 的八个原模型及八次真实新 warm FD。第6批最近拒绝 alpha=1/2、第7批最近拒绝 alpha=1，都是原37已选角网格全部有效、原 merit 条件满足，而唯一未选 LEFT-RMS462 的 beta 平方为负。两处原最低值分别为 -1.7827069382052452 和 -10.25057313338912。更远试步的其他失败不被删除；本次不据此再增其他查询。

因此新38只加入原 left RMS 规则在 interval462 的完整2048角查询。它需要新的实际 endpoint462 Jacobian/P 块和完整 B 支持，不能只改 query 标签。原37中21个 LEFT 与16个 MID全部保留。原实际155最后 warm/status 已按规则清理，字节 SHA 是历史身份，并不使那些原件重新可用。

本请求的第一阶段从仍可恢复的 actual98 原31 pair 开始，在当前 job 中重新执行**原37八批**；每批完整原模型、真实 nonlinear trials、原 warm 和新 FD 均真实产生。只有当前 job 确实完成八个 eligible 原37 pair，才把仍在临时目录中的最后两个原文件交给新38。此重新执行不预设会逐字复现 actual155 的候选、耗时、权重、接受 alpha 或输出 SHA。

37与38都有有限QP工作预算。新增约束不证明原 selected-query 曲率消失、QP最优、较大步长、收敛、native或完整BVP接受；没有把这些新主张写成门。

## 2. 实际数组支持及完整数学责任

| 项 | 原37 | 新38 |
|---|---|---|
| LEFT interval顺序 | 463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487 | 在原顺序最前加入462 |
| MID interval顺序 | 471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490 | 全部原样 |
| query数/原角行数 | 37 / 75776 | 38 / 77824 |
| unique capture cells | 24 | 25，新增462 |
| 实际query端点并集 | 463…491，共29 | 462…491，共30 |
| complete B local | 9805 | 10143 |
| zero layout | 空 | 空 |
| 原 C 支持 | nodes471…482及三个全局控制，4059 | 原样 |
| 全变量 | 236036 | 原样 |

LEFT fraction 保留字面 binary64 `0.17267316464601146`；MID fraction 保留 `.5`。不是用后者替代新 LEFT462。LEFT仍在原 CubicHermiteSpline 站读取原完整端点值/RHS；MID仍直接读取原 `state.middle[j]` 与 `problem.mid[j]`，并保其原 nodal RHS Jacobian/P 链与显式 scalar control jets。

新增 node462 属于原 C 支持之外。新 source 根据实际typed端点并集形成全 B local indices，核 declared layout 等于实际 block-column union。全 H、原 A/AT、所有 W/b/g/S、完整自由core109、全部原边界行及outside恢复照原；没有截去新列、把其方向固定为零或冒用旧 Bz。原 source 中以 parent 描述的 capture扩展元数据都由显式 `query_extension_reference` 限定为**原37源基线**；后续 own38 pair 保同38布局，由读回 `query_changes_since_this_model_input` 正确返回空列表。

相对原37的数学正文保持：原 LEFT 导数生成、原 MID 链式公式、full-coordinate matvec/rmatvec、局部scatter、complete QR/condensation、候选比较、R267 ordinary-float读出及原 nonlinear selector。原科学常量与阈值不变：

```text
--iterations 1
--damping 270
--lsmr-iterations 200
--projection-sweeps 200
--line-search-steps 17
--budget-seconds 1200
--angles 4096
--jac-workers 2
--condensed-budget-seconds 600
--condensed-trial-reserve-seconds 90
--condensed-recovery-reserve-seconds 30
--condensed-max-working 512
--condensed-dual-sweeps 200
--condensed-store-root
```

原37和新38各自的 FD入口都运行原完整 affine-tail response 的全部原方向、步长、Richardson及实现阈值。FD从该批真实新 warm 的实际 SHA 重算；这不调用当前H的非线性native，不获得新fullDN证书。

## 3. 真实父输入和两阶段来源

唯一初始科学父件来自：

- actual98 run `43677587785`，source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`；
- artifact `14147700690`，`visible-followup-condensedqp-43677587785-1`；
- 完整 ZIP 809042943 bytes，SHA256 `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`；
- 原 `warm-001.json.gz` 4927052 bytes，SHA256 `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`；
- 原 `driver-status.json` 3379453 bytes，SHA256 `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。

复用原 request155 helper 和512247运输：核官方metadata/source、完整ZIP size/SHA、安全central-directory路径，唯独提取以上两个原成员并核各自CRC、size/SHA。未提取成员不冒完整解压/CRC审计。然后删除临时ZIP。

四数学输入保持原155字节及历史恢复路径：

| 临时名 | SHA256 |
|---|---|
| accepted.json.gz | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared.json.gz | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail-anchor.json.gz | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail-config.json | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

由原冻结 `exact_20261114_public_resume.py` 恢复其所需原public source；工作流只 fetch 已指名历史 commit，不切换 scientific checkout。原155 `public-thirty-seven-model-recipe.json` 完整27755 bytes / `f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea` 在171中作为真正的第一阶段原子协议读取和核对。

第一阶段 `batch-000`…`batch-007`调用已冻结37 observer/producer/domain/FD。这四原源完全未修改，也没有调用旧155 batch worker的 `main`。新协调器复用其实际单批调用/原pair验证/移动/读回逻辑，以便在第八批后保留现场。

第二阶段 `batch-008`…`batch-015`调用四新38源。batch8实际开始前写入 `phase-handoff.json` 并完整输出：run/source、八个真实前缀pair已付、原carrier路径、原两文件bytes/SHA、原37 status schema、真实optimization/acceptance flags、最后37摘要身份和接收方38入口。`new38_model_not_yet_executed=true` 在这份交接收据中故意保留：它只是启动前原件绑定，后续实际模型/FD报告另付。

## 4. 新38 parent validator：动态SHA不等于伪造status

新 warm 的 `PARENT_SCHEMA` 是实际37 producer schema：

```text
exact-constraint-thirty-seven-query-condensed-complete-H-warm-v1
```

新自身 schema 为：

```text
exact-constraint-thirty-eight-query-condensed-complete-H-warm-v1
```

只允许上面真实37 pair 或之后真实own38 pair。两路径都用CLI的 `--expected-resume-sha`、`--expected-parent-status-sha` 核**当前原字节**，并保留原 `baseline.bind_parent` 的所有实际状态/来源核验：

1. 原prepared/accepted/tail-anchor/config四来源身份；
2. 原mesh、field representation、完整scalar profile责任、constant-state三控制；
3. 原warm与status的unaccepted语义、one-step optimization progress、latest_warm SHA；
4. status identity每字段与完整warm producer逐字段相同；
5. producer source名字集合与相应37或38全闭包相同，并逐文件SHA匹配。

旧validator内历史命名 `ACTUAL37_WARM_SHA`、`ACTUAL37_STATUS_SHA` 作为**此次完整37初父的明确运行时参数**由这两个真实CLI SHA赋值。它们不冒实际request37或deleted155原件。`main`保存/恢复所有这些全局、engine包装和argv，旧源字节不改。

原37 `SOURCE_NAMES/FROZEN` 被整体继承，额外把原37 warm/domain和新38 domain锁到其真实源码。FD和observer的入口pin已回填当前新warm SHA；不把旧producer套上新schema。

## 5. 实际pair生命周期及失败范围

每批按以下顺序执行：

1. 当前pair的原文件路径/SHA传给原model CLI；
2. 原model确实产生one-step progress warm后，照原验证完整warm/status；
3. 在该**新warm**上实际运行原FD，并核原implementation flag、当前prepared SHA和fresh FD字段；
4. 输出完整本批摘要与全部原trial JSON字段；若超过90000 bytes，使用既有完整member语义流；
5. 完整读回返回后才以 `os.replace` 移动两个原文件到 `parent-after-NNN`，再次核移动前后原bytes/size/SHA一致；
6. 清本批大数组及已消费旧pair，保当前真实pair供下一批。

`validate_completed_pair`、`pair_identity`、`move_pair`、`model_command`、`field_identity`、`compare_reference` 的完整函数正文与原155逐字一致。新控制流只选择37/38阶段、输出目录、预算和交接元数据，不另定义数值接受准则。

任何前缀原model/FD未提供eligible successor，38阶段均未开始；它不被宣称无解。新38原拒绝照原记录，编排不自动补query或改lambda。pair/来源/I/O异常也不被记成数学拒绝或native失败。

异常发生在print/move之间时，可能一份status已移到carrier而另份尚在batch。新helper的always只读路径同时遍历：

- 每个 `batch-NNN/thirty-seven-condensed-warm/`；
- 每个 `batch-NNN/thirty-eight-condensed-warm/`；
- 每批 `physical-response/response-check.json`及全部原child `.log`；
- 所有实际 `parent-after-NNN/driver-status.json`原iterations/trials；
- 若存在的 `phase-handoff.json`、`chain-progress.json`。

它不从缺文件/返回码猜原门通过。JSON选择器失败时，完整原文件字节走既有12000-byte、surrogateescape、ASCII JSON双层编码；每事件界保持88000 bytes。复用的协议事件名中 `request155_*` 明确是已发表的传输协议版本，真实171阶段身份在label、完整对象和源表中，不冒155数值。

新helper薄适配只导入并核原f5d598纯字节/JSON helper；没有数值模块导入。38的 `summarize`保原trial字段，仅切换真实38 entry key、实际增LEFT462和相关元数据。37摘要由未改的原helper直接读取。

## 6. 全部实际trial与未访范围

每个真实原model仍最多17档，实际 visited trial全部完整输出，包括原selected-angle、domain、RMS、merit、linear reserve和拒绝原因。未访问alpha不能从后置summary补成成功或失败。原standalone model与status内科学字段比较只读原值，不是新增接受门。

协调器记录global batch_index与phase_batch_index，保每批原输入pair、原输出pair、真实model/FD退出码、原alpha、原fixed-weight merit前后及整份摘要SHA。不同批权重/模型重建，不跨批相减加成单一模型下降量。所有含科学数组的大原始文件只在Actions临时现场，摘要不根据hash反造数组。

链末输出明确completed prefix/extension count、最后实际完成pair、每个未访问后缀的global/phase index、原stop、全部gate false范围和real handoff。它不是新的可恢复raw checkpoint。

## 7. 资源范围与未执行语义

本次明确请求最多8原37批及8新38批。**300分钟链资源时钟从入口开始、在恢复实际98和source之前计时**。每个新原子pair开始前，需剩余至少1500秒；这是资源启动条件，不是科学门或单次FD耗时定理。剩余不足就原样记录 `explicit_between_pairs_resource_budget`、未启动后缀和exit3。

开始后的model仍收到原1200/600/90/30预算及全部原迭代数，FD协议原样；编排不为凑16批而缩短任何原子预算。一个内部科学调用可超过其检查点间时间，故不能把1500秒声明为原pair的已证硬上界。外部science step为320分钟，job为350分钟，另有10分钟always读回及setup/cleanup余量；最坏外部超时或规则停止可截断当前原子，报告真实partial，不反推任何未返回科学结果。

当全部规定pair完成，过程可以exit0，而 `success=false`、`new_coupled_finite_acceptance=false`、native/fullDN未调用保持。它仅完成所声明的优化实验。

最终完整链对象先通过有界语义流输出，再删除正常退出owned namespace。若发生异常，namespace保留供always readback。工作流末清理只有 `steps.surviving_readback.outcome == success` 才删除；否则输出未读目录/原因并保留至runner自身销毁。没有raw artifact、Release或Git数据上传。

## 8. Source closure、规则同步和实际命令

新recipe保存原155的90个recipe源身份，再显式保旧155 worker原SHA作为算法/来源基线（不执行）；新增四38科学源和一个thin helper，共96个recipe source pin。独立171 worker由request再锁1个，共**97**。原 `source-dependencies.json` 参数manifest唯一一份、SHA `7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941` 完全保留。

每个原source/parameter实际字节在Actions开始逐SHA核；所有Python源由原AST步骤解析。父37 recipe的全部90source和参数需为新recipe逐项子集；工作流另核原155 worker身份。没有删改先前pin、套用旧“85个源”标签或把新增producer闭包当原父闭包。

新trigger：

```text
topics/visible-flex-larger-amplitude/computations/public-thirty-eight-same-job-batch-request.json
```

新独立concurrency：`visible-larger-thirty-eight-same-job-batches`，`cancel-in-progress:false`。原38科学运行命令由协调器传完整实际父参数生成；job主入口是：

```text
python -u geometry_20261115_thirty_eight_same_job_batches.py \
  --repo-root "$GITHUB_WORKSPACE" \
  --request "$VISIBLE_COMPUTATIONS/public-thirty-eight-same-job-batch-request.json"
```

外包未改的3b8 rules runner，当前明确已读root `21bd547f56590b7f2dd279d0297efb289a9b2783`、topic `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。startup和每2700秒原真实pull/rebase/diff/stop保持，fixed scientific checkout不切main。`git config --global merge.stat false`沿既有运行器要求，防已删历史raw的diffstat，未绕过实际规则比较。token只在transport/规则进程env，传科学子进程前删 `GITHUB_TOKEN/GH_TOKEN/MR_TOKEN`。

## 9. 最终文件与完整原基线

除workflow在 `.github/workflows/` 外，新源与两JSON在本课题 `computations/`。全部对象是小UTF8源码/参数，不含raw科学数据。正式基线是原155发布commit `0aa9dca2d8029721cd1e820948699206a7da4388`；四数学source各对应同suffix的 `geometry_20261115_thirty_seven_query_*.py`，newhelper对应原 `root_20261115_thirty_seven_temporary_readout.py`，newworker对应原 `geometry_20261115_thirty_seven_temporary_batches.py`，workflow对应原 `visible-larger-public-thirty-seven-batches.yml`。新recipe和request显式是新的完整协议。

| 路径 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| `topics/visible-flex-larger-amplitude/computations/geometry_20261115_thirty_eight_query_domain_operator.py` | 35653 | `f1684f4b23d1b50d97779ae79bb90554307a524c0a8932de6af824ca1fa98e17` | `a26f5462fa97bae4b22bc019c9a066ed6c4fda09` |
| `topics/visible-flex-larger-amplitude/computations/geometry_20261115_thirty_eight_query_condensed_warm.py` | 49683 | `4e93c558c09fcf9e86525834fc09fe206cd36e2df88af4b968f64ae6aaeccc50` | `f5710b23fdb2b5aedab87f07feb9fd45e474d70d` |
| `topics/visible-flex-larger-amplitude/computations/geometry_20261115_thirty_eight_query_condensed_response.py` | 2625 | `ccc2c242b3806cdea83e05ce9b756a01dc6cf875e12bd2f45e8f2fe7994906ad` | `3f65e28f088c5cc9aa60eaf55ef60b48ae8b3d41` |
| `topics/visible-flex-larger-amplitude/computations/geometry_20261115_thirty_eight_query_collocation_observer_warm.py` | 16736 | `96ed2b5d5b98c4d9b18afcd0616046c02874c6d6b569dbc0cd34d2e8918bf920` | `d96236cb600294b8002c76cc9864c42573090aa8` |
| `topics/visible-flex-larger-amplitude/computations/root_20261115_thirty_eight_temporary_readout.py` | 15387 | `32c2bca1cb068143dd01d99ef0eced97550fd24331a49684b66c7dad2743b80d` | `a4ccbf181f2b3f9bba101bbc1ea36f5917135aeb` |
| `topics/visible-flex-larger-amplitude/computations/geometry_20261115_thirty_eight_same_job_batches.py` | 34840 | `2564be712a79aae29b5c2ce99518a8508e10f581e8a204a2162aec7b20859866` | `f73a3a84a29621df8623b72a5fc57cc3a4965785` |
| `topics/visible-flex-larger-amplitude/computations/public-thirty-eight-same-job-recipe.json` | 24111 | `947ace5169e6d3037ba61c561ed92a4be554f3e37b133966dd897c321e3fc890` | `c5bee9685b8b1c8abd975a03d35a3c9f2dcf38a3` |
| `topics/visible-flex-larger-amplitude/computations/public-thirty-eight-same-job-batch-request.json` | 6853 | `06d3b8c9f207ebcc9ee58cce3e78f59d48b689a193822569bf8e697034d8b748` | `954ee25403452d17aec418084327b996bfa9c299` |
| `.github/workflows/visible-larger-public-thirty-eight-same-job-batches.yml` | 10684 | `2895b50da5c2d00a0d003679f21ae0154cdafdba9b01db6b4f847d70b1408636` | `bb0dfd6d8e9ad8c35722e96fc54e21c2c1c818ef` |

这些SHA不含未来171输出身份，实际执行时由各原件形成runtime receipt。

## 10. 完整差异与本地执行范围

以下七份完整diff供源码阅读，可由上述原、新source重新得到；不要求发布可重算静态回执。数学新支持、动态父绑定及两个阶段控制流在这些diff中全部显式出现。

| 对应新文件 | diff bytes | diff SHA256 | 临时diff blob |
|---|---:|---|---|
| `geometry_20261115_thirty_eight_query_domain_operator.py` | 13280 | `95180378b75b8ca0429b88684ca66f190d8de2f2c44dd8a151afe1ec9b620f7c` | `a80c8c87046f6e059918c58ccf09ef0ad50636d1` |
| `geometry_20261115_thirty_eight_query_condensed_warm.py` | 20860 | `975362fd17d8cc28e6430c3d2b50a1413edd71df8df30f95ef45d615c205f7bd` | `2a4fb86146b44961a4c165c1de8d0af251fa01c4` |
| `geometry_20261115_thirty_eight_query_condensed_response.py` | 1393 | `cf5f308060f5c6ee0e9f3d0a534045ef554c0c2b31edfa04cfb9212403936a43` | `f5b50ec61dea286d3d10b603e08f5a3318e7dc78` |
| `geometry_20261115_thirty_eight_query_collocation_observer_warm.py` | 1991 | `7d8deb3257f802c5a39265cf170002ab575d175c0b9928b74f0701ca6a23859b` | `316c31324f819c57344b236238e10d38110a33ee` |
| `root_20261115_thirty_eight_temporary_readout.py` | 35340 | `af75aaa0292cc906fd8c009cb2d2b13949fc182a14efeda33483f911cecaaf43` | `740ce4b28da45222c89e3a06771db44c99f625d2` |
| `geometry_20261115_thirty_eight_same_job_batches.py` | 32040 | `d04a7d321548e71b2f739cedb3c3275e33998067acc988a4380fdb355cf8a1ac` | `e4f40c6ac1e968e67812a081f1bbfcc8fceb713e` |
| `visible-larger-public-thirty-eight-same-job-batches.yml` | 12291 | `b91216ca28306d0306cfa3af535c3a1da27f926c4d95dd10d724b84663663e0a` | `dbd93428d5fc9fbde4beecc2e78fb118ba98ca5d` |

纯文本已核：新typed列表22+16；unique cells25/endpoint30；ZERO_LAYOUT_NODES为空；新warm/FD/observer依赖pin一致；原模型/evidence、pair validator、model command和move等指名完整函数正文逐字保留；全部原91source身份没有删改。此处整数集合检查是源码布局元数据，不是数学模型运行。

当前终端仍报告 `No usable execution environment`。没有声称本地AST、bash-n、fixture、导入或科学执行已过。工作流保原真实AST/source解析步骤；该步骤正常后直接进入原科学，不另设证明、审查或合成数值试验前门。

171之外，R354/170有限参考和Hermite误差诊断独立推进，不加入此次原model/FD接受条件。145方向/真实映射缺口由独立后继处理，也不改变本请求。
