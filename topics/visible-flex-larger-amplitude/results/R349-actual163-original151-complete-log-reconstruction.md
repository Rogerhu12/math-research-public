# R349 实际163对151原日志的完整字节重建与准确目标读回补充

作者：ChatGPT /root/amplitude；日期：2026-11-15。本文补充 R341 的原件读取边界；它记录一次公开 Actions 元数据读回，不重新执行区间算术、原数值曲线、RHS、Jacobian 或科学求解。R341 的科学结论不因日志读回成功而改变。

## 349.1 本次新增的已付证据

实际163的 read151 job 成功下载原151 compute 日志一次，在临时目录逐条重建原输入、完整目标结果、全部节点/当前覆盖/未决队列/覆盖事务，并核对源定义的记录顺序、字节数、SHA256、父子替换和各数值分片的端点链。该 job 的470411项元数据检查全部匹配，未重新计算任何包围值。

本代理随后完整读取 read151 的新语义日志，重建并逐字核对全部五个语义组。原完整输入62020 B、原完整结果101961 B 和完整重建范围收据111286 B均已返回；不再仅凭原report的小摘要推测其中字段。另一方面，65535条原节点的区间值没有全部打印到新语义日志，本代理及root也没有逐值重读这些节点。原节点的完整字节和覆盖责任由公开163读取程序核验，不能改称独立重证了每个区间谓词。

新增证据确认原结论：151在有效公共坐标闭覆盖下用尽节点交易预算，仍有10468项未决；没有严格域反证，也没有完整目标误差证书。不能把新的 complete=true、元数据检查全匹配或 read151 的 success 解释成原目标成功。

## 349.2 两轮运行及来源身份

| 项目 | 原始身份 |
|---|---|
| 原科学run | [43724306509](https://github.com/Rogerhu12/math-research-public/actions/runs/43724306509) |
| 原科学source | `618a9369d2bd45210767e294726cec10be1cd2df` |
| 原compute / report | `132842781513` failure / `132859348081` success |
| 元数据run | [43732715988](https://github.com/Rogerhu12/math-research-public/actions/runs/43732715988) |
| 元数据source | `4e1decc718c712b2eaa26a7da598d89236a21ef0` |
| read151 / read157 / report | `132868511229` / `132868510914` / `132868952547`，三者success |
| 163读者 | `root_20261115_existing151_157_log_readback.py`，77301 B / `ecb77c7e4aae0b7888c58c753ca74d49f0528db3f743443582c3bc4503853250` |
| 163请求 | 17848 B / `4ae311d844e7f25adf6fe65e0d246ad26d2deb7e236dfe6a3599a7672c40ec63` |
| 163工作流 | 13974 B / `1413450a6c0c8263c276c863dbbb6a4da9e7b3f88b7486a48f8166e33bc49893` |

163先向官方 API 读取原run、compute、report的终态和source，核验实际原消费者及工作流的完整字节，没有导入它们。原消费者 `root_20261115_continuous_nine_target_enclosures.py` 为69431 B / `6dfb79be9b77e85ffff496e4349b9c6b01c1ab74f28d0a64bf76d4dc8cadb768`；原工作流50748 B / `3995b487f98f3c61cf28cc0418f666c9cb1ae6748156930718fb889f4ed5a9e9`。

实际下载的原compute日志为899965552 B / `4e907e5d935c91223accc038d5d8ea90f222cb5ee8ee34ef7310659aa6f1d1eb`。原report日志没有重复下载。运输层仅去除锚定的GitHub timestamp/BOM前缀，原JSON数字词和科学文本不重写；142915行中142905行具有时间前缀，429个异常运输前缀保留独立记录，归一化LF文本SHA为 `4892730789d70e8e3bf09eab315de303acbbd487b154b9ed42e17be4162a140d`。这是运输文字处理，不是科学数据归一化。

元数据job自身记录 elapsed=83.667338475秒，exit=0、exception=null。临时原日志已在身份记录后删除，owned_cleanup.completed=true，cleanup.exception=null；没有生成新的artifact、Release数据或Git原数据。

## 349.3 本代理实际读取的五个语义组

read151新日志完整原字节为378606 B / `1f18e51f699f08eaec9b3c70b83c4e4ca8a87dbf454fa82e235674d62a28c73d`。下表按 begin/part/end 协议连接已解码的ASCII字符串，保持原末尾LF；全部134项本地JSON/字节/顺序检查匹配，没有科学算术。

| 语义组 | B | SHA256 |
|---|---:|---|
| official-original-run-job-and-protocol-source-binding | 1619 | `7c28b19f0e2c54f1ffeae211d7f1eb55865e15528258144cc7a421541637f087` |
| 151-complete-input-and-rebuilt-definition-binding | 62020 | `6ed65011f5235f923123ccbcc529b8011bb0389aa3a6c155388ee7373d21c4cb` |
| 151-complete-target-result | 101961 | `95fa1e1104cf5dcfbf154bbba1b55e27bd1afb685dd82a51cec255d67ba08f94` |
| complete-original-reconstruction-scope-and-coverage | 111286 | `d19430df9abdbaf36f7fc31324274dd7ef203fdc02995c612f459d1cc8286ca0` |
| complete-semantic-output-index | 1562 | `4a6e9c841f89287729f19de14242d5aa9d8ac503bc5c9f700c5ba42b8b5a3642` |

163 report原日志221759 B / `74b105cb2f3a204906c8cf1a625c135d7e1ec1c361ea2f44a13dfa3726367e60`；其中151小索引44943 B / `02ba98937f39ab3b24eb875bda1114d4a8abe41724f9fea889190f4ce6b896b1`，也已完整读取。索引保原470411项检查的有序收据SHA `643b606e945b883b11f3908ef99572aeafbc60290d0e8e40023d5d6cf2728b04`。检查数只说明程序实际执行的元数据责任，不能代替区间运算正确性证明或独立科学复算。

上述大于100KB的语义组是既有Actions日志中的原材料，不作为新数据提交Git或Release。本文只保必要结论、来源及原输出身份。

## 349.4 完整原结果确认的停止原因与未付范围

原 `resource_stop_reason` 精确为 `maximum-evaluated-node-budget-before-two-child-transaction`。声明最大评价节点65536，实际已尝试并完整记录65535个节点；下一次原子替父事务需要两个子节点，不能只保存一个。原预算900秒，`elapsed_seconds_including_binding=127.38605653900004`；没有耗尽科学墙钟。

| 原字段 | 原值 |
|---|---:|
| initial_numeric_pieces | 419 |
| evaluated_node_attempts / completed_node_records | 65535 / 65535 |
| current cover leaves | 32977 |
| radius_proved | 32879 |
| speed_proved / domain_proved | 32780 / 32780 |
| relative_goal_met | 22514 |
| unresolved / queue / complete_pending_or_refuted_rows | 10468 / 10468 / 10468 |
| rigorously_refuted | 0 |
| complete_unvisited_coarse_count | 0 |
| completed_atomic_splits | 32558 |
| scientific_controlled_exit_code | 3 |

原 `phase=bounded-target-enclosure-finished`、`procedure_complete=true`，但 `comparison_work_goal_complete=false`。`full_public_u_closed_cover=true`；原完整准确九参数域、严格速度域、全域半径正性、有限全域目标相对界均false。原 `global_delta_upper=null`，`whole_prefix_relative_delta_below_one=false`；`at_least_one_accurate_domain_interval_rigorously_refuted=false`、`error=null`、`interrupted_transaction=null`。

原策略保全部419数值分片、最大深度32、grid_bits=320、原tree sqrt_bits=256和work goal `1/10000000`。准确目标没有被数值长度替换，所有可能准确分片及九控制仍保留，原数值局部变量没有裁切，两侧接缝均保留。以上是原结果明确的范围字段，不等于其未完成谓词已变真。

`actual_field_created`、`native_success`、`fullDN_success`、`same_field_metric_certificate_paid`、`true_IEEE_evaluator_error_bound_supplied` 及原whole-tail/caps/closed/strong-C2/reach/held责任均false。163没有重跑151或改变这些门。

## 349.5 原完整ledger确切覆盖

| 原ledger | B / 记录数 | SHA256 |
|---|---|---|
| evaluated_nodes | 526666191 / 65535 | `242f9dcf852bc76aca516a87e2d3e1702c79e407ac7ef56aea4c5aaed88d65da` |
| current_cover | 267198234 / 32977 | `61350c911aae16e5a17000ecc1d94f724d5bce10c11a1a0e95e49c4c8d07f247` |
| complete_frontier | 88905408 / 10468 | `a8a87f59c96e92106ca774cdf892b7e1743f089b9a8ba30e648402d3ad9cb9bd` |
| complete_cover_transactions | 18137631 / 65535 | `b1a68bc1390908d0e0cb57d7b950b3ab779322e0fa04998256d9d3a465aca27a` |
| original_query_plan | 52193 / 419片 | `d413d4f414199d842e6f7800fc0753f4edc1ad30e9a3e427cd62075c4faedcb4` |

原3038项grid外包记录为1533021 B / `12794fb7e461a421b20c29e1383f26c867242feecf2b2dc599872f71eb13c9fc`。163完整重建其字节并记身份，没有重复Q或区间算术。419片的完整字符串覆盖元数据为99029 B / `98c3846e81459c484afcc291e165908582ecb636677113d41a12fabe8642e4e9`。

重建收据明确 `all_node_enclosures_recomputed=false`、`exact_predicate_proofs_repeated=false`、`all_original_node_values_printed_to_new_log=false`、`root_has_independently_read_every_node_value=false`。因此不能仅由汇总SHA断言未决集中于某支撑、某条接缝或某个谓词，也不能捏造未打印的叶记录中d0/d1/a/as数值。若后续需要这些归因，应从原日志一次性选择真实记录或原分组，不重新制造原结果。

## 349.6 完整输入与两个全局原区间

原输入绑定含20件科学source身份、实际九个binary64词及其准确二进有理数、实际定义和全字段重建对照、准确连续E构造、config/core/recipe/cut/tail、三支撑与旧域证据。原定义377789 B / `9ac99b2722d7a6f4d02cd51420d6428c878a9712763bc679f07f6d2a8154d235`；原T112 config2161 B / `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。这些大输入没有由本次读者重跑；本文读的是151已记录的完整绑定。

原参考是字面词表达式的准确实数模型，明确不是原IEEE程序。三支撑的右端采用准确left+width；记录中同时保rounded_right词，但没有用它偷偷替换准确端点。第一支撑两者不同也保留。原 `current_C_tail_J_or_nonzero_field_not_supplied=true`，原数值float DAG/BVP没有在读者重执行。

为了下一次真正的包围算法设计，以下抄录原结果两个全局区间，整数和指数均来自原JSON，未转十进近似、未重新求界。

`accurate_total_length`：

- binary_exponent：`-320`；
- lower_integer：`5817495797978587951600625954867948311841826001286377790825445872266120557367955447600226036870001`；
- upper_integer：`5817495798060272125493160855109471965123506575147906484289958839671069018287975799464298896827070`。

原 `literal_total_length_exact="6132919223663265/2251799813685248"`。它仍是原数值参考长度，不能据名称替换准确长度。

`global_radial_relative_target_difference`：

- binary_exponent：`-320`；
- lower_integer：`-29991427844989880973945738594146434624155381050836170410860236025662184032800175485685`；
- upper_integer：`29991885433470724853527855143664892931431252586027647993413842198112339333113577211684`。

这个全局径向差已有原区间，完整目标仍受其它未决责任限制。不能以该单个区间代替 `global_delta_upper`，后者原值仍null。

## 349.7 对后继工作的约束

本补充付清了R341所缺的原完整结果、输入和全ledger字节覆盖读取。后继可以针对公共u、准确长度及支撑多项式的依赖膨胀提出独立收窄算法，但必须保原完整目标、九控制及未决责任；不能仅把节点上限增加解释成已付准确目标。现有记录也不支持从汇总计数推断唯一失败位置。

对157的另一路，163索引已成功，但本代理未能完整接收其新巨大语义日志；157初末FD、全部外模型和试探的独立原值读取交给明确的后续167，不借151读回成功冒该范围。本文没有混入157的新科学结论。
