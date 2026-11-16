# R504：重算同 C 的六个完整 metric/evidence 消费者

日期：2026-11-16。作者：ChatGPT（AI，geometry协作代理）。

本接口接R495真实已加载场与R500实际query API。完整条件见 [R504](../results/R504-recomputed-C-query-complete-metric-and-evidence-consumers.md)。没有新request/workflow、实际accepted父、数值结果或预算数值选择；217/R490仍未建立。

## 1. 正式文件和不重复的展开源码

本次正式运行源是三个小文件：

| 路径 | bytes | SHA-256 |
|---|---:|---|
| computations/geometry_20261116_same_C_recomputed_fixed_query_consumer.py | 7655 | 0cda42f08ae866c9c002fd396240399a9e2193378f44cd8939e26e7af45e6b4c |
| computations/root_20261116_same_C_recomputed_tail_metric_source_views.py | 9454 | 3c282629dbad2c9b77c8245f84a801570b143a8ebe4619a8c4033b3664cc6789 |
| computations/r504-same-C-recomputed-tail-metric-source-plan.json | 38102 | 34436dfc5a6317a79b4a3b86673112b26888baaf3ccc1e7c0376acf3c34e69c3 |

展开的六个程序仅按完整计划在实际Actions computations下生成。它们每件小于100000 B；不把原算法五万字无改动正文复制到Git。完整plan本身保存每条before/after/count和旧/新全文身份，是本次完整差异，不是哈希替代被修改片段。

generator沿原R495 metadata generator，只换明确新schema/frame/plan角色标签，以及七件helper的实际集合。原先“核全部选中输入和输出字节→再独占写新名→记录全部未确认角色”的控制流不变，不导入或编译生成程序。

## 2. 先后顺序与现有源范围

必须先有：

1. 原真实公开source闭包及所需既有动态views；
2. R495对应role的实际生成程序，完整SHA与下表一致；
3. 已刊R500源码、固定薄接口和下表七件helper；
4. 最后才由本generator形成R504新basename。

原R495 incrementalM与evidence的祖先含R464实际生成view，不能用不存在的路径先验SHA，也不能将R504输出冒原R464/R495身份。所选role未涉及的完整数学依赖仍由其真实科学入口按原contract恢复与绑定。

### 七件实际生成依赖

| 文件 | bytes | SHA-256 |
|---|---:|---|
| geometry_20261116_same_C_refined_metric_family_bridge.py | 12303 | 06656a5ed8bd020d7ab476ed9790f8fc9e4e75d3e7f61ef9c9cc1fb765ddfc74 |
| geometry_20261116_same_C_refined_leaf_target_and_cut.py | 35549 | a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7 |
| geometry_20261116_complete_coast_bernstein_enclosures.py | 18291 | 3730c62b5c1a40fb594c9a2d9ed95a523a9134f12eb0b8def59c764d79e3edae |
| geometry_20261116_same_C_refined_head_tail_queries.py | 29687 | 2ab6b97fc77c520ed8b888d31a766d9e4e744fb40dc8af46dfd4d287f015b580 |
| geometry_20261116_same_C_recomputed_fixed_query_consumer.py | 7655 | 0cda42f08ae866c9c002fd396240399a9e2193378f44cd8939e26e7af45e6b4c |
| geometry_20261115_current_C_ten_live_query_complete_metric.py | 55040 | 77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892 |
| geometry_20261115_same_job_C_live_query_provider.py | 31603 | 07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9 |

这些是generator对直接helper的文字绑定；R489原provider、f12f及其全部祖先、当前field/CP/material源也必须按R495/R500真实传递闭包存在。七件表不替代科学closure。

### 六个精确baseline

| role | R495实际basename | bytes / SHA-256 |
|---|---|---|
| fixed_original112 | geometry_20261116_refined_C_original112_fixed_metric.py | 52120 / c8729d2e07cb398c80c02d7aab6f5f7efb78d9607542fd17979720671552e110 |
| live_original112 | geometry_20261116_refined_C_original112_live_metric.py | 57022 / 927ed104fa2d94a45531d42f5b5ab1927760e1ea832c4a038980968083c3c8ed |
| live_resolution112 | geometry_20261116_refined_C_resolution112_live_metric.py | 57053 / 596bbacba0002351684960c21c0e2351e2c2e506482b9204cb9633fa29beaad1 |
| live_completeM | geometry_20261116_refined_C_complete_M_live_metric.py | 57000 / b434a1032466ed2c40fc34cda7c8144008a068f654a5136989b102980681118f |
| live_incrementalM | geometry_20261116_refined_C_incremental_M_live_metric.py | 57066 / 9933f4c76c33a8459ae3af11505682bcc0063a6ae2e6bd96b8296da6b0baf260 |
| evidence | geometry_20261116_refined_C_fixed_target_metric_evidence.py | 64481 / ec52160b75526cf645fbca71858169c35d249941757d5483440020ac3ba8278d |

### 六个精确新输出

| role | 新basename | bytes | SHA-256 |
|---|---|---:|---|
| fixed_original112 | geometry_20261116_recomputed_C_original112_fixed_metric.py | 52454 | 09c1bc45da87a299985368a4f6f3193a2b1cd48cbd42f4605b33e99319512a9b |
| live_original112 | geometry_20261116_recomputed_C_original112_live_metric.py | 57288 | 7d47d97fcc1bdbedb5900c7b0eaf6f33713ad40713313173c8b96313d5beed10 |
| live_resolution112 | geometry_20261116_recomputed_C_resolution112_live_metric.py | 57315 | 0bea4d3d69de45ff319f9e8e7e672cd83aaa89e77836c81b9c97a36cf8be5c89 |
| live_completeM | geometry_20261116_recomputed_C_complete_M_live_metric.py | 57270 | f2fff4a5c72c61b147e007e301eef71d8c4c617355b75d12a5e705fc334e77fc |
| live_incrementalM | geometry_20261116_recomputed_C_incremental_M_live_metric.py | 57330 | f9645484c3809bf08759ede6c49781336288e9313553f03f00ff3f1884a57d2d |
| evidence | geometry_20261116_recomputed_C_fixed_target_metric_evidence.py | 65229 | 18a96d962da2fc3010e0b52144030a72e506bb6860fed7a953d94ac65b8e4a32 |

这些SHA来自对全部原文本逐literal count应用后的完整字节身份；没有执行生成的科学函数、AST或compile。实际Actions仍先核输入字节并再核真正写出的输出，不能以本地预览身份替代实际生成结果。

## 3. Generator的完整CLI与记录

~~~bash
python -u "$COMP/root_20261116_same_C_recomputed_tail_metric_source_views.py" \
  --computations "$COMP" \
  --plan "$COMP/r504-same-C-recomputed-tail-metric-source-plan.json" \
  --plan-sha256 "34436dfc5a6317a79b4a3b86673112b26888baaf3ccc1e7c0376acf3c34e69c3" \
  --roles fixed_original112 live_original112 live_resolution112 live_completeM live_incrementalM evidence \
  --out "$NS/r504-source-views"
~~~

这是来源操作示意，不预填某次科学参数。COMP必须是真实public computations，等于generator HERE；NS必须是caller实际RUNNER_TEMP namespace。out是新的独占元数据目录，不得包住COMP或覆盖旧目录。

--roles可显式选择上述集合的子集，不能重复role。所有被选目标必须尚不存在。generator先完整校验全部选中baseline、全部patch count和预期最终bytes/SHA，再逐个xb写入新文件；不会覆写原程序或把旧name当缓存。

结果位于out/result.json，schema为R504-same-C-recomputed-tail-metric-source-generation-v1；实际frame：

~~~text
BEGIN_R504_RECOMPUTED_C_TAIL_METRIC_SOURCE_VIEWS
END_R504_RECOMPUTED_C_TAIL_METRIC_SOURCE_VIEWS
~~~

必要字段包含actual_computations、requested/selected/unselected_roles、实际helper、全部baseline和output身份、current_view、unconfirmed_roles、completed与原error。失败后原新文件保留，不能据有一部分输出就说全role生成。该元数据仍执行单90000 B限制；超限70，不语义分包。

## 4. 六个实际科学schema与frame

| role | source/result schema | compute中的必要frame |
|---|---|---|
| fixed_original112 | R504-same-C-recomputed-original112-fixed-query-complete-metric-v1 | BEGIN_R504_FIXED_ORIGINAL112_RECOMPUTED_C_METRIC / END_R504_FIXED_ORIGINAL112_RECOMPUTED_C_METRIC |
| live_original112 | R504-same-C-recomputed-original112-live-query-complete-metric-v1 | BEGIN_R504_LIVE_ORIGINAL112_RECOMPUTED_C_METRIC / END_R504_LIVE_ORIGINAL112_RECOMPUTED_C_METRIC |
| live_resolution112 | R504-same-C-recomputed-resolution112-live-query-complete-metric-v1 | BEGIN_R504_LIVE_RESOLUTION112_RECOMPUTED_C_METRIC / END_R504_LIVE_RESOLUTION112_RECOMPUTED_C_METRIC |
| live_completeM | R504-same-C-recomputed-complete-M-live-query-complete-metric-v1 | BEGIN_R504_LIVE_COMPLETEM_RECOMPUTED_C_METRIC / END_R504_LIVE_COMPLETEM_RECOMPUTED_C_METRIC |
| live_incrementalM | R504-same-C-recomputed-incremental-M-live-query-complete-metric-v1 | BEGIN_R504_LIVE_INCREMENTALM_RECOMPUTED_C_METRIC / END_R504_LIVE_INCREMENTALM_RECOMPUTED_C_METRIC |
| evidence | R504-same-accurate-closed-target-recomputed-C-metric-evidence-v1 | BEGIN_R504_RECOMPUTED_C_FIXED_TARGET_EVIDENCE / END_R504_RECOMPUTED_C_FIXED_TARGET_EVIDENCE |

前五个metric的必要schema是source schema加-necessary-summary。evidence的measure result就是其source schema；measure input加-measure-input-v1，series input加-compare-input-v1，series result加-actual-series-v1。这些均是新source的实际schema，不用旧R495标签冒新路径。

旧R495/R500源码保持原字节。新程序的__file__/source_sha取其实际新文件；generator/plan不能替它代填科学结果身份。

## 5. 固定metric：全部原CLI，无新的query参数

fixed_original112保原CLI完整列表：

- --computations；
- --directory、--result-sha256；
- --checkpoint-directory、--proof-directory；
- --cuff-atlas、--cuff-atlas-sha256；
- --continuous-e-result、--continuous-e-result-sha256；
- --refinement-directory、--refinement-result-sha256；
- --eta、--interval-bits、--sqrt-bits；
- --initial-angular-depth、--max-depth、--max-visited-cells；
- --budget-seconds、--out。

原parser允许的可选项保持原样；实际R495/R500绑定需要的真实CP/原C不能因parser可选就用缺失来源冒场。continuous-e-result仍指field定义绑定的**旧**实际C，refinement-directory指真实R489独立目录。

固定分支调用：

~~~python
TailQuery.bind_loaded_fixed_same_C_tail_queries(
    current_bundle,
    args=args,
    output=args.out,
    metric_started=started,
    budget_check=lambda: Bridge.check_local_budget(started, declared_budget_seconds))
~~~

该helper复用R500原完整绑定和FixedRefinedQueries，再调用同一SameCTailQueries.bounds闭覆盖算法。它不建LiveQueryTarget，不建query budget/journal，不执行新中点积分。没有新增11个c_query参数。

其binding在large-arrays/same-C-fixed-refined-tail-binding.json；原field/atlas/两帽、complete root plan、四Loewner、闭DFS、全部pending原样。初始cuts可因实际新query闭端点而改变，planned_roots按该次真cuts全重列；不能继承旧rank paid状态。

## 6. 四个live metric：沿原参数与原唯一oracle

四条live metric使用上一节原全部CLI，再保这11项原参数：

- --c-query-precision-bits；
- --c-query-integral-absolute-bits；
- --c-query-integral-relative-bits；
- --c-query-analytic-guard-bits；
- --c-query-integral-evaluation-limit；
- --c-query-value-width-bits；
- --c-query-integral-max-depth；
- --c-query-inverse-max-depth；
- --c-query-max-panels；
- --c-query-max-nodes；
- --c-query-budget-seconds。

没有新增参数、提高额度或重置钟。原R495根据实际R489 namespace deadline作clipped_total_allowance仍先真实执行。

原两行fixed_tail/Live构造被一处R500.bind_loaded_same_C_tail_queries替代；没有保留旧Live然后再建一个新的。R500本身会先完整绑定旧原ActualCompleteCTarget，并使用新R489 query/source建立一个原R426 oracle。

原所有inspector、四Loewner和闭DFS不改；未通过的真实radial cell仍按原条件调用refine，current query和完整source row/pending由原R426保。原coarse合法界继续可用。scope明确“当前query调用不重做全head”与“它的输入确是R489先前真实重算head”这两层。

## 7. evidence仍是真live，不是固定表替代

evidence保原三个子命令：

~~~text
measure --input <actual input> --input-sha256 <actual SHA>
compare --input <actual series input> --input-sha256 <actual SHA>
readback --directory <actual output> --result-sha256 <actual SHA> --out <fresh readback>
~~~

它保原field.family的original112/resolution112/completeM/incrementalM四项，以及各原真实metric loader来源。**FAMILIES表用于加载原准确场/数学模块，不改成新outer view的name来冒类owner。** 场真正加载后仍由R495桥构成独立求值视图，然后才接R500。

输入 field 保原 8 键：

~~~text
family
directory
result_sha256
checkpoint_directory
cuff_atlas
continuous_e_result
refinement_directory
refinement_result_sha256
~~~


work、c_queries、time_grid、first_material_transport/first_plan/first_assembly、job_deadline均原合同。特别c_queries仍全部11键；time_grid仍真实正整subdivisions和每个共同坐标/side witness，不预填时间或误差。

evidence原先已经有LiveQueryTarget和refine（含真实t witness的径向query）。本次真实替换为R500，同一原live_started和原Budget.remaining配对；原Budget.check、global绝对deadline及磁盘reserve仍作用。没有把它降为fixed，没有另加一份active query预算。

原relative norm、真实lower witness、完整upper/祖先fallback、全域coverage、全t同余及真实t-grid访问都不改。原FD/final/solver容差只作为真实来源证据，不凭其数值冒metric floor。

## 8. 必要readback新增范围

前五个metric仍通过same_actual_C_target保新tail.necessary，包含旧/新四件、全部query状态/错误/未访和实际live当前地址，末summary键已有此完整对象。

evidence新增same_semantic_tail_queries到result及necessary。这个对象的完整scope随各实际measurement输出；原所有规范化metric量、coverage、actual_time_grid、末tolerance证据保留。

series compare不重复每level的大tail对象。每level保存same_semantic_tail_queries_reference：

- actual_measurement_result：这份完整实际result的身份；
- object_present：原对象是否真实存在；
- complete_object_identity：对应完整必要对象canonical bytes/SHA；
- full_query_scope_in_that_measurement_necessary_not_repeated_here=true。

这只减少重复输出。若某次measurement必要未返回、超过90KB或不完整，series不因有SHA就把它补成已读。各measurement的完整错误和query/frontier仍原必要责任。所有raw仍在同job临时目录，未删未上传。

原R495 Bridge.compact中的tail未切换flag原样保留，新增refined_semantic_C_evaluation_scope明确那是前一leaf-only层回执。当前全部tail事实以新的same_actual_C_target或same_semantic_tail_queries为准，不改旧回执后假称它就是原source输出。

原90000 B/70限制不改。任意多错误未决仍可能超限；没有“保证必装入”或raw分包协议。

## 9. 同g和材料签名

R500对外expected_binding等仍指旧准确field的原绑定；新query的工作参数/result/source另列。evidence的fixed_closed_target_signature因此继续绑定同一个准确g与first material/全construction/十词/cuff/t范围，不被新C求值工作的字节变化污染。

原材料六jet查询仍绑定原合法current视图，R495保证其准确函数同新求值视图相同，可能保更宽盒。R504不自动宣称全部材料逆/六jet误差均已收紧；实际径向E目标查询才是本次新来源范围。

同一完整C/root族保留；没有选择numeric midpoint、没有把tail target改成1+Bprime²、没有把旧accepted450重标为新父。新盒有效不等于实际严格变窄，更不等于全域误差下降或任务完成。

## 10. 来源生成之外还须真实完成的调用

本次已支付六个可执行outer程序的实际调用/新schema/必要选取。未来owned入口仍须：

1. 同job保真实accepted场和原完整C/geometry；
2. 真运行R489并保全部新source/query raw及原deadline；
3. 按实际来源先生成所需R495，再生成R504；
4. 核实际生成输出后调用相应新name；
5. 原必要/quiet/cleanup全部真实完成后才处理临时payload。

没有新workflow、总request、solver参数、eta/K/tau/W/H、实际父或科学结果预填。旧当前请求均不改。R489仍explicit actual202205来源；其它改过tuple的后继须独立登记，不能当作自动兼容。

scope/phase/status都按真实返回记录；量纲、准确g、全t和原native/FD/fullDN/final门不减。没有新增fixture、独立审计或短跑前门。
