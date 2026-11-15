# R293：actual132 连续 E 首次完整源执行、面板预算及尚未支付的整段查询

作者：ChatGPT /root（GPT-6 Astra Pro，AI-assisted）；2026-11-15。

**分类：公开 Actions 的实际有限执行、区间输出及原件身份事实。** 本次原连续生产器在 `482.79984332900005` 秒内访问完整原表达的先后分片，完成 `1378` 个原分片后用尽明确的 `200000` 积分面板预算。全部 `1440` 个分片未完成，唯一整自然闭域查询的 `E=null`、`domain_containment_proved=false`，自然外半径也为空。因此它没有形成可供同场 metric 使用的完整连续目标证书；Actions 的 success 只表示过程和诚实部分结果正常返回。

## 1. 来源、输入及实际合同

实际运行是 [43702946191](https://github.com/Rogerhu12/math-research-public/actions/runs/43702946191)，source `185e4f3eb798fbca5fabab8ca928741cb4cd6446`。compute `132777819446` 于 `10:12:30–10:21:02 UTC`，report `132779955239` 于 `10:21:04–10:21:07 UTC`，两者均 success。科学规则 runner 实际起止 `10:12:57–10:21:00 UTC`，science/wrapper 返回码均0，未发生规则变化、同步失败或科学 checkout 修改。

入口及完整数学合同见 [Request132](../notes/2026-11-15-request132-original-continuous-E-execution-interface.md)、[R286](R286-original-stored-continuous-integral-and-metric-bridge.md) 及[生产器接口](../notes/2026-11-15-stored-continuous-E-cover-interface.md)。实际源为 `geometry_20261115_stored_continuous_E_cover.py`，66415B / `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed`；request `1b3d3348217c011d419d2e70fa0decc77479ba8b1b3a41e0b4abdb58ad335a88`，query recipe `4fa2baa15518ee5045d4a21305ff3f727ef594f966e8a95f9bc6f89eaac3b979`。

原 T112 config、校准 ledger-ready 和 stored-ready 从公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 临时按完整字节恢复；三个输入的 SHA 分别为 `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`、`563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6`、`c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d`。原78源、8个当前 pin 和9个公式来源保持，未输入 accepted 场，未运行旧48层有限 selector、ODE 或 shooting J。

实际合同为 `original-exact-root-family`、256 bits、绝对积分96 bits、相对积分80 bits、单次 analytic evaluation limit100000、value width24 bits、max depth48、query depth12、200000 integral panels、200000 inverse query nodes、1800秒工作预算。每个原分片的六个共同 primitive 全部保留：`A,B,sqrtE_A,sqrtE_B,w_A,w_B`。深端覆盖原全体 `n>=160` 的准确根族，不选择特定根，也不改为旧有理深目标。

## 2. 已完成工作与具体停止位置

| 原读数 | 实际值 |
|---|---|
| 原 finite head cells / pieces | 160 / 1440 |
| complete original pieces | 1378 |
| integral panels | 200000 |
| rigorous analytic component integrals | 1103610 |
| inverse cover nodes | 0 |
| 原 elapsed seconds | 482.79984332900005 |
| producer error | null |
| numerical work resolution complete | false |
| full finite head complete | false |
| finite head all six primitives | null |
| deep plus head all six primitives | null |
| natural outer radius / minus nominal cut | null / null |

原进度按原 cell159向外排列；cell7完成时为1377片，原 elapsed `96.483798958` 秒。第一个明确未付记录在原 `cell=6, segment=1, source_piece=1378`，深度47，闭参数区间精确保存为

\[
\left[\frac{126450279677349}{140737488355328},
      \frac{63225139838675}{70368744177664}\right].
\]

原 reason 为 `Declared complete integral-panel resource budget reached`，`included_in_complete_primitive=false`。这不是1800秒到期、不是外部 Actions 超时，也不是程序 exception；记录不能证明这个原函数没有合法积分。单凭该记录同样不能断定已经到达最大深度，或把成本唯一归因于某个绝对值零点。需要从实际分裂和精度策略继续定位，不能拿未运行的原因替换原停止原因。

## 3. 全部未付责任的实际读回范围

临时 unpaid ledger 共33行：31条 `integral-panel`、1条 `unvisited-source-piece-suffix`、1条 `whole-query`。工作流读者先完整读取并核该 ledger 的9585B / `707506c69eeae5169a482179b8ebd7bdcc9eedd9971c027b617292b04f5d292c`，逐行解析全部33行，才产生计数及后缀。

保存的全部未访 source 后缀只有一条：`first_piece=1379, stop_piece=1440`，即原半开索引区间 `[1379,1440)`；完整原 piece index 仍定义所有1440片。部分执行的 piece1378由31条 panel 未付记录保留，不能只看后缀就把它冒已完成。没有被静默删除的查询后缀；唯一 query 已实际返回明确未解决对象。

本地可读原日志保留首个完整 panel 问题、全部 source/query 后缀、分类计数及整 ledger 身份；其余30个 panel 的逐区间 payload 只在 Actions 临时 ledger 中被完整读取，随后依第15条清理。本文不声称独立重新取回这些已删区间，不从SHA恢复它们，也不将 ledger 的临时完整消费说成当前仍有完整 raw 下载。

唯一原 query 的左右端均闭，范围是精确 dyadic `rCuff` 至真实积分定义的自然 `R_out`。原结果为：

- `complete_closed_domain_bound=false`、`domain_containment_proved=false`；
- `E=null`、`unresolved_whole_query=true`、`work_resolution_complete=false`；
- 原 reason 为 `The complete source or original-root existence premise is unpaid`。

该 reason 是源码合并条件的原文字；本次原准确深根存在性 flag 实际为 true，具体尚未支付的是完整 finite source。不能误写成本次已否定深根存在性。未得到全 primitive 累计原点和自然外半径，就没有启动有效的完整径向逆像覆盖；原 `inverse_cover_nodes=0` 与此范围一致。

## 4. 实际深端包围与结构标志的边界

原 `deep_cover` 保全所有原准确根选择及 cuff，采用 R286 的统一几何级数导数界，未数值求出任何深根。原显示值为：

| 原深端区间字段 | 原输出 display |
|---|---|
| E | `[1.000000000000000000000000000000000000000000000000000000000000000000000000000 +/- 4.75e-77]` |
| E_r | `[+/- 3.22e-84]` |
| E_rr | `[+/- 0.0446]` |
| radial right | `[0.04999999999999998889776975374843459576368331909179723053517628596091414439645 +/- 4.30e-78]` |

这些 display 不是另行十进制构造的证书；原输出同时保准确 dyadic 下上端，完整 producer result 的字节身份见下一节。上述是深端统一包围，不能外推至尚未付完的有限头或实际几何 cut。

原 `protected_join.proved=true`、`finite_joins.proved=true`，原 active flat transition segment为2；源明确没有以有限 schema/fingerprint 作为C²证明。它还记录 `declared_continuous_model_family_conditions_proved=true`、`original_exact_deep_root_existence_proved=true`、`all_admissible_original_root_choices_uniformly_enclosed=true`。本文报告这些实际字段及其 R286 结构依据，未从包含零的小区间单独推出恒等，也未把它们扩成整闭材料面的目标 atlas。

`original_exact_deep_root_choice_resolved=false`、`original_continuous_g_model_choice_automatically_discharged=false`、`original_finite_output_certified_as_continuous_solution=false`、`a601_same_field_binding_or_relative_metric_threshold_paid=false`。原模型C的额外选择、有限程序与连续实表达的身份、同场 atlas 和完整相对算子误差均仍需分别实际支付。内 cuff 的平极限不得被误用为自然外端可常值延拓；后一端的独立接合责任仍在。

## 5. 原日志及重建身份

| 原件或完整日志输出 | bytes | SHA-256 |
|---|---:|---|
| compute log | 94444 | `5614413426011d5881d98c73a3fee49f829b465d7fb8efe1f669c1bf93979636` |
| report log | 21959 | `f5f940be9c6965dc339ecbe9363ceb6a13365befd81cbc295f475283ef3ae470` |
| 工作流合并 scalar summary | 8716 | `7ccbcf3c36a9c4df65ba72f98c87ec620d8d64024b9c6a5dea58129d34946369` |
| 原 producer stdout summary（含其原结尾LF） | 6125 | `06c2079debdf51a60d8571961d15f279a2215bcd5961e72cf65f22fd1dcfc6a3` |
| 原 result.json | 5992 | `e18d07b684bc78c1ef9186d3e16cf7f2288e958a4298523223c70d4cc2ff53cb` |
| 原 query-results.json | 608 | `009f8e1146268fa7e5defc961c196960a3a959b93b24ff90a6ed33c563856e2e` |

root 核了 compute/report 两份8716B摘要完全相同且匹配原事件SHA，并从其完整 `source_result` 与 `query_results` 依原 canonical JSON 编码重建5992B与608B，均与原件字节身份一致；原6125B producer摘要也逐字核身份。这里只做原 JSON/字节工作，没有本地积分、范数、区间算术或科学模块导入。

原六 primitive panel ledger 为523030685B、100674行 / `45e66a78bfb18ba889002d215fcebaadebb0183059bc3fcfd80e5d8405873ffa`；原 radial panel ledger 为192279067B、100674行 / `b1e544da471eb923ea07f8e5500ec0c934a408fff6a08d921b8898ee587da634`。这些只是原生产器消费时的完整身份和范围，既未提交、上传，也未在本地重算；不能把100674个已记录叶当作1440个原片已经全付。临时输入、索引、ledger及输出均在完整读回之后清理。

## 6. 直接后继

此运行确定了应处理的真实瓶颈：六 primitive 的有限头面板策略在原cell6/segment1消耗完整面板预算。后继须保全部原表达、六 primitive、深根族、累计原点、自然外域和全部未访责任，先从已冻结源识别分裂成本与工作精度要求，再用明确独立源码/参数在本公开库Actions重做。不得把预算失败改成数学拒绝，或略过剩余原片直接构造全域E。

全部课题目标仍未完成；本结论之后立即继续该积分问题、非零完整112场和同场闭面/metric工作。
