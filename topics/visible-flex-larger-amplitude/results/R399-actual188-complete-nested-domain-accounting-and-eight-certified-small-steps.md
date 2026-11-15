# R399：实际188完整嵌套闭段责任已访问，较小八档全部查询严格过，原37步与FD另行通过

日期：2026-11-15。对象是已真实结束的 request188。本文只读取该次 Actions 原字段、源码退出语义和字节身份，没有本地重做区间、多项式、模型、RHS、Jacobian 或 FD。

## 399.1 已取得的结果与尚未取得的结果

**本次完成了全部 $37\times2048\times17$ 项准确 Hermite 查询路径闭段责任记账。** 直接区间计算与同路径包含继承分别记录；最后八档 $k=9,\ldots,16$、$\alpha_k=2^{-k}$，对全部37查询、每个2048角点均有严格域证明。较大九档仍有未决，因此全17档统一证书为 false，后置诊断按原程序返回3。没有预算截断、科学异常、严格域反证或未访问后缀。

此前原37模型真实 $\alpha=1/8$ 步已接受，新 warm 的完整边界 FD 已通过。后置诊断返回3不更改这两个原结果；较小八档的准确有限路径域证明也不产生新的原优化步、native 解、fullDN、连续角证书或整段 IEEE 执行误差证书。

这次支付的是 [R398同一路径嵌套闭段包含](R398-same-Hermite-path-nested-closed-domain-inheritance.md) 的一次完整有限范围应用，不回填 [实际175](R372-actual175-original37-accepted-FD-and-partial-closed-Hermite-domains.md) 当时未完成的事务。两次均从 actual98 独立形成自己的真实模型、方向和原调用记录，未借已清理现场。

## 399.2 真实运行、单摘要与读取口径

| 项目 | 原身份 |
|---|---|
| run | [43761083360](https://github.com/Rogerhu12/math-research-public/actions/runs/43761083360) |
| 固定源码提交 | 068805ae3009884cbbcd200ba4c9f9be474f5bd7 |
| 唯一 job | 132955840323，original37-and-nested-query-domain |
| job 终态 | failure；科学 step7 返回3，必要读回 step8 success，清理 step9 success |
| request | public-thirty-seven-R398-nested-query-domain-request.json |
| request SHA256 | 658621725d67ad7642bb8e2f43224e9b38914b2826d7a173ae959e1e8e3f7641 |
| necessary summary，含文件末 LF | 76,295 B / 073725145d09166501722618aa356a126c0e6413cae1890f5e41a5c4ca978810 |
| 同一 JSON 帧正文，不含分隔 LF | 76,294 B / dfb079de54cc683cea59653e4f7ed9c57407eb18e2bb2a8c51e7cfe350a05a9f |

唯一取回的是这个已结束 job 的 GitHub connector 解码日志。工具返回字符串重新按 UTF-8 编码为127,899 B，SHA256 f51b96200f17ed75d9c150a0ee4cd9c0d24aae48d666aea67ba14bdb85f89e49；这是**工具解码字符串的 UTF-8 身份**，不冒 GitHub HTTP 原响应字节身份。原字符串保留，解析视图仅逐物理行去一个行首 BOM，再去锚定时间戳；未对任意正文作 BOM/空白归一化。

唯一实际非 ANSI 帧是 BEGIN_REQUEST188_NECESSARY_SCALAR_SUMMARY 到相应 END。正文加回一个 LF 后，bytes/SHA与原 request188_necessary_scalar_summary_identity 的 receipt 精确相同。readback_complete、summary_complete、transport_complete 均 true。本文读了完整必要摘要，未把7 MB原 result 或数 GB区间账本重新下载到本地，也未把大表语义拆包。

## 399.3 来源、真实调用与原预算

原父仍是 actual98：

- artifact run43677587785 / id14147700690，原完整 ZIP 声明809,042,943 B / 9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a。
- 父 warm：4,927,052 B / b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67。
- 父 status：3,379,453 B / b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。
- 原 recipe：f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea。没有把它改成已清理的155、171或175末点。

Actions source-binding 步完成105源与3参数件逐字身份核及语法解析；日志明确90个原 recipe 源、原 batch worker、158/166/170/175来源及2个独立188源的分工。本文不把日志中的已执行核查冒成本地重新读取全部105件。

| 核心源 | bytes / SHA256 |
|---|---|
| exact_20261115_R398_thirty_seven_nested_query_domain.py | 46,107 / 51d12ef4f224f2b579bd4afbda0f9fd568b2c6eea61e13eec4a1bcbd89422365 |
| geometry_20261115_R398_thirty_seven_nested_query_same_job.py | 实际 source SHA e1f80243405667ba037d826e86004ae8a0fc61747a2b634cd8da0c10fe5a4627 |
| 不变 capture | 0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90 |
| 原170端点核 | 84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a |
| 私有生成端点模块 | 75,536 / a2d2d09b521996f2201b5634aabe5ddc61218b24b7f3ee96e6501a00af12d1bc |
| R398已发表证明 | 11,337 / be828511c22ec7fe6c0e9dcefa1637b2b2587d5e634407d8e25ddb9e7ca82ba7 |

原170数值函数保持，采用正式正 sin 版本，未使用负 sin 审稿。原175 consumer/runtime只保来源而未执行。完整端点变量仍29份，不能把同节点但不同实际 A/J/P/cache words 合并。

本次 capture 实际记录12次 evaluate、1个域对象、1个最终方向、185次 angular return；observation_complete=true、errors空，原runtime aliases已恢复。185是此次实际调用数，不能以37查询或29端点数推成固定调用数。

原模型预算：1次模型、17档回溯、damping270、200 LSMR/投影/dual sweeps、600 s凝聚、90 s试步预留、30 s恢复预留、原模型1200 s、4096全角与2 Jacobian workers。后置诊断5400 s；全链10800 s包含恢复、模型、完整J/QR、FD与诊断；读回清理预留300 s。320-bit向外整数格、384-bit Arb三角函数保持。均是资源上界，不是新增原接受条件。

## 399.4 原模型四个真实试步与新 warm FD

原模型完整返回0，用时718.81264604 s。固定权 merit原值43.363003729098274，原实际斜率 −0.21838603098375256。实际只访问档0–3，档4–16未作原非线性试步；后置准确域诊断不把它们补成原试步。

| 原档 | $\alpha$ | 原结果与必要地址 |
|---|---:|---|
| 0 | 1 | 拒绝。原 midpoint487，angle992，$\beta^2=-0.07787348001852168$，原 RHS 非有限；RMS阶段未到。 |
| 1 | 1/2 | 拒绝。midpoint471，angle959，$\beta^2=-0.042792191869085006$；RMS阶段未到。 |
| 2 | 1/4 | 拒绝。midpoint471，angle44，$\beta^2=-0.19167001275188889$。本次最近拒绝的选中查询还包括 LEFT-RMS464，angle54，$\beta^2=-0.2683086899521916$。 |
| 3 | 1/8 | 接受。实际 merit43.33605694766103，原下降0.02694678143724616，预测下降0.026877973010679432，原比值1.0025600303467597。 |

四档原 selected linear reserve 都无负行；最近拒绝档的线性 $\beta^2$ 最小值0.0007427224110553854，reserve最小值0.0003183097338947949。线性选中行通过不能替代原非线性域；本次最近拒绝确有已选 LEFT464/MID471，不能说全因未选查询。

接受档全699节点、698中点以及两侧RMS原检查实际完成。RMS fractions为0.17267316464601146和0.8273268353539885，各698点，失败数均0。完整边界最大残差6.857449986338445e−9；原物理 collocation 最大值0.007107481419522546，位于 interval461、原 residual row155819。原4096角 $\rho$ guard valid，最小值0.16604058243274977。它们是原报告，不是本文重新评价。

| 新 pair 对象 | bytes / SHA256 |
|---|---|
| model-000.json | 814,495 / 451e130b42416512e159045ea994812410f1815d1975df5d69f7559b6c417148 |
| driver-status.json | 3,647,546 / 88885f6c3b6fe87598664d4e67c7de9caf2b6b1319f74bbfbf9146cda43cfb2a |
| warm-001.json.gz | 4,943,006 / c5614a9d1bf612523fbd7e2d98ed8c93fa31dade1d043873a9c5578985539691 |
| response-check.json | 2,839,007 / a54bb94090687fd4388ba944b0f4b55e50c123cde8d609504e0e231878acdec6 |

FD子程序实际返回0、用时19.10002697699997 s。二阶最大相对方向误差0.00000988344249574147，四阶/最大误差8.81884772255149e−10，阈值0.00005；direct/separated两组二阶收缩均true，offblock最大值0，implementation_check_passed=true。没有以父FD标签替换新FD，currentH不等于旧affine anchor，ready linear graph未用作此次非线性DN。

原 status 的 accepted_warm_steps=1、optimization_progress=true，但 success=false、new_coupled_finite_acceptance=false；native_at_current_height_solved=false，完整fullDN与闭曲面未付。QP大表只保身份，本文不据紧凑schema声称QP最优。

## 399.5 全部17档的准确闭段结果

对每个固定查询 $q$、原2048离散角 $n$，声明同一个准确有限 Hermite 路径，考察 $[0,2^{-k}]$。全部453分量（338物理、115常量RHS行，含两均值）、准确端点形成项、真实 A-chunk literal $b+C p$、全15个 degree≤14系数均保。端点二阶包围用 [R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md)；可变余项不被当作固定系数多项式求导。

方法有两类：

1. direct：该闭段全部系数实际作原向外 Bernstein/Horner 判定。
2. inherited：同一query、angle、准确路径已有较大闭段的直接严格证明，且子档自己的完整gap依赖已付，因集合包含证明较小闭段。没有重新计算子档系数包围，也不要求独立余项盒彼此嵌套。

全部629个 query×step 完整453 gap已完成且可用；29个端点、全部JP变体及原点态transfer的pending范围均空。75,776个query-angle事务全部提交；末事务query36/angle2047、next_trial_index17、whole_angle_record_committed=true。结束时commit inactive，deferred signals空。

下表是原query_index的未决集合 $U$：表示该查询尚未全2048角证完。没有严格反证或未访，故表外查询都已全角严格证完。

| $k$ | $\alpha_k$ | 原未决查询 $U$ |
|---:|---:|---|
| 0 | 1 | 0–36 |
| 1 | 1/2 | 0–36 |
| 2 | 1/4 | 0–34 |
| 3 | 1/8 | 1–17；19；21–34 |
| 4 | 1/16 | 2–16；23–29；31–34 |
| 5 | 1/32 | 7–9；12–16；23；27–29；31；33 |
| 6 | 1/64 | 8–9；14；16；23；27–28；31；33 |
| 7 | 1/128 | 14；16；27–28 |
| 8 | 1/256 | 14；16 |
| 9 | 1/512 | 空 |
| 10 | 1/1024 | 空 |
| 11 | 1/2048 | 空 |
| 12 | 1/4096 | 空 |
| 13 | 1/8192 | 空 |
| 14 | 1/16384 | 空 |
| 15 | 1/32768 | 空 |
| 16 | 1/65536 | 空 |

末两项query14、16是 LEFT-RMS480、LEFT-RMS482。在k8原各有2046角已证、2角未决；k9各余下2角直接证明，其余2046角继承；k10–16全部继承。必要摘要没有返回这4个原角的具体区间见证，本文不编造地址、上下界或主因。

固定37查询完整映射：

- query0–20：LEFT-RMS intervals [463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487]。
- query21–36：MID intervals [471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490]。

| 原全局字段 | 原值 |
|---|---:|
| query-angle rows committed | 75,776 |
| query-angle-step responsibilities | 1,288,192 |
| direct evaluations | 168,176 |
| direct strict proofs | 75,776 |
| inclusion inheritances | 1,120,016 |
| inherited strict proofs | 1,120,016 |
| 全部 strict proofs | 1,195,792 |
| unresolved | 92,400 |
| rigorously refuted | 0 |

每个query-angle首个直接严格父段的档位直方图，按k0–16原顺序为：

[31010,15064,15882,10982,1856,766,160,40,12,4,0,0,0,0,0,0,0]。

这些是已存整数计数，不是本文据多项式重新计算。每个query-angle最终都有一个直接严格父段，最迟k9；不证明它是最大可行段，也不把较大段未决改成失败。

## 399.6 返回3的准确原因

原记录同时有 scientific_completed=true、all_requested_query_angle_step_responsibilities_accounted_for=true、committed_method_counts_consistent=true，但 complete_accurate_query_domain_on_all_closed_steps=false。all_requested_direct_step_range_evaluations_performed=false来自1,120,016项合法继承，不是漏访。any_accurate_query_angle_rigorously_refuted=false、resource_partial=false、scientific_exception=null。

源码返回语义是：全17档全部查询全角严格过则0，否则3；“全部责任访问完”不自动返回0。92,400未决是已完成判定但包围尚不能给严格结论，和未访问不同。

后置科学elapsed3900.1662292699993 s，进程elapsed3900.4775305109997 s，低于5400 s上限；全链elapsed4819.388457674 s，低于10800 s。无外部deadline触发、signal列表空。原规则runner从20:59:40到22:19:59，2轮同步，README_change=null、science_terminated_for_actual_rule_change=false、science/wrapper均3。不能记成规则终止、数值异常或资源截断。

实际α1/8的原float点通过，与对应准确闭段未决不矛盾：前者检查实际试点，后者包围零到该步的准确有限路径；原IEEE执行与准确有限表达式也仍分开。

## 399.7 内部结果身份与实际清理

| Actions临时对象 | 原bytes / SHA256 |
|---|---|
| pipeline.json | 12,237 / d2e47e3ecd74a4a6f64e24451e6f22596e1baf5440371f64f4bd2e4eee60ba73 |
| original-pair-summary.json | 442,654 / 3c472a4a4ae87f5f90c0a350d6225f11c5530c6c025c03cbb4726a10e7479575 |
| 完整 diagnostic result.json | 7,037,942 / e5f913820d6af03f2f8252cedad5fafd51155cfc45e032e7455b092a37016df5 |
| capture.json | 767,326 / ae3c5647374e7ede1a2ddac929195096dea9010280a5423e33431488c4ead8a4 |
| complete-input-binding.json.gz | 194,972 / 9a7f3ed8172efa73f861cd4cf2e99cef44979b46e2a9d49739703ecd976c8ccf |

input-binding原未压缩身份1,311,891 B / 4eb807fd4152bd9fbebdd47d7d352f530c68da07b0e22084e3d046dd940207d7。它们是原摘要中的receipt；未下载这些大对象，不冒逐行科学复核。

全部临时ledger未压缩总量原值4,467,913,088 B，低于8 GiB上限。原计数：29完整端点向量记录；各29端点2048 angle-jet记录；all17 closed endpoint账本59,392记录；完整453 gap账本629记录；query families账本666记录；完整17档query-angle账本75,776记录。最后账本原压缩483,877,364 B / 7cfc453948f32257ac8b2819165ced20d2ccf1666b3b985fd264ae65a2f086f3，未压缩3,227,485,626 B / c33448969e620b51ea769c7233e8654b149131a4bc6c34a266dc9417840c7a78。只保生成脚本、参数、run、身份和必要结论，不将可重算大表换编码保存。

日志明确先输出完整单摘要并写complete marker，随后依次实际发生 request188_owned_cleanup_begin（marker present=true）、request188_owned_cleanup_complete（removed_directory=visible-R398-188）、request188_rule_mirror_removed；官方cleanup step success。大对象、末warm和规则镜像这次实际已清理，不能以后仅凭SHA冒续接现场。复现须在新的公开Actions从真实actual98恢复并按原配方重做；无raw artifact、Release或Git数据上传。

## 399.8 可以用于下一步的范围

本次严格覆盖较小八档同一准确有限路径的全部声明离散角责任，并在实际预算内完成全部记账。它不修改优化器已完成的α1/8接受，也不成为新的求解门。

未付仍包括较大九档完整严格结论、整段原IEEE误差、连续角/站位、全699节点/698中点/RMS的连续证书、当前H真正native、fullDN、最终338响应及独立物理审计、同一完整场满足用户最终几何目标。没有QP最优、无解、浮点底线或Hermite误差唯一主因结论。完整场主线可继续，不为搬取本次大ledger另设前门。

复现入口是固定提交的request188与同名workflow：actual98真实来源、105源/3参数、1次原37模型与新warm FD，随后5400 s后置R398诊断；必要单摘要上限90,000 B，完整原对象只在同job清理前处理。每个新run有自己的模型、方向、计数和字节身份，不借本次完成标签。
