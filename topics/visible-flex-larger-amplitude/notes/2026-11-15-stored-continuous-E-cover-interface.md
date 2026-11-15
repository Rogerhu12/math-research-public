# 原冻结来源、约定 C 连续 E 的完整区间生产器

2026-11-15，geometry，GPT-6 Astra Pro，AI-assisted。

状态：独立源码与完整数学/接线接口；只进行源码阅读、AST和字节SHA检查，未导入或运行科学模块。没有实际 E 区间、未来 field、原 metric 阈值或运行结果。

本组件直接落实 [R286](../results/R286-original-stored-continuous-integral-and-metric-bridge.md) 的有限头六primitive和无限深尾解析包络。它不穷举原48层有限selector，不调用旧数值factory，不借R26任何数值证书。其目标是**明确声明约定 C 下、原准确深根允许族的连续模型**，不是对旧finite返回的重新命名。

## 1. 文件和身份

源码：

- computations/geometry_20261115_stored_continuous_E_cover.py
- 66,415 B
- SHA256：9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed

源码中的证明pin使用已经实际发布的R286文本：

- results/R286-original-stored-continuous-integral-and-metric-bridge.md
- 37,491 B
- SHA256：81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb
- 发布commit：90b232d861000cb1ce94a6d5420836c1d89f910a

R286草稿末EOF多空行的旧SHA不是运行pin；数学内容相同，入口只接受实际发布字节。

运行所需数值包为 python-flint==0.9.0。Python沿项目原3.12.14可用；无需Node、NumPy、BLAS、旧native worker或任何原非线性进程。原JS只读并核SHA，绝不导入。

入口 main 和 ContinuousHead 构造均要求：

- GITHUB_ACTIONS=true；
- GITHUB_REPOSITORY=Rogerhu12/math-research-public。

本地只可继续源码/AST工作，不执行该生产器或其数值类。

## 2. 为什么这不是另一个外部区间消费者

入口自己从原真实输入构造：

1. 原160行的浅层 R_n、alpha_n；
2. 原冻结的 d0/c0/rCuff/epsilonScale/global warp alpha；
3. 全部cap、valley、flat、最后cut-preserving覆盖及正warp权重；
4. 160×9个真实有限源段；
5. 每段同一实表达的全部六primitive；
6. 原根族的整个无限未warp深尾；
7. 真实自然外端 R_out；
8. 给定物理半径闭区间的完整可能逆像覆盖及 E 包围。

没有让外部文件提供一个未经证明的 E_lower/E_upper后只做格式检查。输入query只有域和实际来源身份；数值包围由本组件自身产生。

它也没有自动解决“课题的原g应采用哪一种实模型解释”。这一模型层责任在R286已明确分开。新输出始终写明约定 C，且原finite输出认证、a601同场阈值、actual accepted field等标志保持false。

## 3. 原输入及源文件布局

三个数据文件均必须给实际文件SHA，plain/gzip按magic读取，SHA绑定原压缩或原plain字节，另记录decoded bytes/SHA：

| CLI | 原内容 |
|---|---|
| --config / --config-sha256 | 原physical配置 |
| --ledger-ready / --ledger-ready-sha256 | 原160行浅校准和保存global alpha的ready |
| --stored-ready / --stored-ready-sha256 | 旧storedMetricAdapter的实际原参考 |
| --proof | 上述已发布R286原文 |
| --queries / --queries-sha256 | 可选的闭径向query计划 |
| --out | 新建、本请求自有临时目录 |

ready允许外层带ready键，符合原强冻结adapter的读取口径。使用rationalDeepModel字段是因为原强冻结source也从该历史对象提取**相同的原浅层存数**；本组件不使用它的 rational-deep 无限对象或旧数值包络。

实际交叉关系包括：

- 原source revision准确为869436630c99aa5a68afb55bd8877c826034d117；
- ledger start160、stored cellCount160、完整160行n=0..159；
- 原config、ledger physicalParameters与stored physicalParameters的全部原geometry键；
- 四个derived键rCuff、oldCut、epsilonScale、prefixRByCell逐原数相同；
- 原保存global warp alpha为同一个正binary64数；
- 原stored七分点fingerprint及字段列表和before/after身份；同时保存原ledger的独立headFingerprint，明确本生产器不重算任何旧数值指纹；
- 每行delta/R/c/lengthScale/alpha完整保留，当前实解释要求实际lengthScale为1；
- orientation+1、protectCell160、unrejoined、a=11/4、etaPower=3/2、deep R64，以及原protect/prefix范围。

数值原JSON拒绝非有限词；包括由极大十进制指数溢出得到的非有限float。原数字比较按binary64词，包括可保存的负零。完整原文件SHA与实际字段均保留，不把“JSON相等”冒原字节相等。

### 源目录

--runtime-computations包含以下四个原小模块：

| 名称 | SHA256 |
|---|---|
| tail_frozen_geometry.mjs | db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3 |
| strong_frozen_calibration_factory.mjs | 77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247 |
| closure_bounded_point_cache.mjs | 35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043 |
| exact_20261114_closed_background.mjs | be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b |

--source-topic使用项目原restore78已经采用的原目录布局。其source-origin.json须给上述86943663 revision。scripts内：

| 名称 | SHA256 |
|---|---|
| closing_weighted_tail.mjs | 740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e |
| closing_recalibrated_tail.mjs | 4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6 |

repro/source-root/topics/large-amplitude-twist-flex/scripts内：

| 名称 | SHA256 |
|---|---|
| tailnext_balanced_tail.mjs | 928567418f411b70c4040be9ee08be2a78b65e147b8d0c5728f4cf6766a28888 |
| general_root_smooth_tail_cells.cjs | d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575 |
| f6tail_cusp_grid.mjs | b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f |

所有原件只读。没有调用原loader来重造校准、transfer、profile数值采样或非线性尾。

## 4. 声明 C、深根族和未付选择

模型schema为：

R286-original-stored-continuous-model-convention-C-v1

保留原R286的明确约定：

- 输入binary常数按准确dyadic使用；
- $\delta_n=d_0 2^{-n}$、$c_n=c_0 2^{-n/2}$、$\mu_n=\epsilon\delta_n^{11/4}$和raw半径由真实关系形成；
- 原表中的其它独立舍入派生词仍完整保存，但不同时当作互相矛盾的准确实关系；
- 浅层 R_n、alpha_n不重新校准；
- global lambda不重新选取；
- 自然R_out不移回名义cut；
- 无限深部仍是原准确ODE校准根在[1/2,2]中的允许选择，绝不是65/64替代。

本次CLI的 --deep-definition只接受original-exact-root-family。这有意表示**全允许根族**。源码没有假装实现了一个尚未运行的具体选根序列。

原根存在的量化前提由准确dyadic比较给出：d0>0、d0≤1/10、c0>0、c0≤1/16、n≥160、R64。R286已证明这些前提使每个原准确传递下左元两端异号，B<2^-63<33。若某输入不满足这组已证前提，源码不以unresolved==0假定根存在：完整无限深责任保持unpaid、不会给整个连续模型的完成声明。有限头已计算部分仍可以保全。

报告区分：

- original_exact_deep_root_existence_proved；
- original_exact_deep_root_choice_resolved，始终false；
- all_admissible_original_root_choices_uniformly_enclosed；
- deep_root_values_computed，始终0。

R286的固定有理中三分区交错选根规则仅作为**未选择的可用规则**引用。因为当前所有深界对每种允许根同时成立，生产本次有效包围不需要先执行该规则。以后若要比统一族界更窄而需要特定根，须完整实现并绑定该规则；不能将目前的false改标签。

## 5. 完整有限表达和真实导数

Piece按原n159→0、每n中j0→8排列。每段保完整raw log、valley项、cap四分支、flat赋值/过渡、随后cut-preserving两处覆盖和原weight。

Jet2的三个槽是真实函数对源x的值、一阶导数、二阶导数，不是factorial-scaled系数。乘积和exp均用完整链式法则；log只对固定正常数求值。S、S'、S''保原quintic表达；实panel中允许用已证明的S单调性和0≤S'≤15/8、|S''|≤15收紧区间，这不改变函数。

cap边界不靠采样分类。一个闭panel若跨多个可能分支，所有可能分支都在全panel求值并取包络。即使某个公式在panel的其它点并非实际分支，它仍覆盖该分支真正负责的子集。完全被flat覆盖的cap以及最末raw overwrite只按原代数作用域消去；没有提早返回漏掉最后两段覆盖。

以源$x$为坐标，$q=w_x$，原真实速度仍为$D=b+c|q|$。Piece.expression保完整b_x、c_x，并直接用R286式：

$$
w_r=\frac qD,\qquad
w_{rr}=\frac{bq_x-qb_x-qc_x|q|}{D^3}.
$$

E、E_r、E_rr由同一个w求得。没有用旧point.drdx、独立renderer jets或差分来猜导数。正D下界来自正参数的凸组合，包含在闭panel包围中。

### 真实接缝范围

finite_join_conditions检查原flat过渡确有完整整数源段，且全部原raw端口、quintic、cap端值和unit weight端口的结构保留。

protected_join分别保存实际内端log slope的三槽差，并只在以下结构已付时宣布已证明：

- cap在保护端严格属于raw，或未启用cap；
- 没有覆盖保护端的整段flat赋值；
- 若恰为flat transition起点，原S/S'/S''均为0；
- 原chi/chi'为0且j0=1。

单凭finite fingerprint、schema或chi=0不会把保护端标成C²。未证的接缝不会被删除，也不会把它当作非线性求解失败；只是相应连续模型条件仍unpaid。

## 6. 六primitive的区间积分

每段完整保存

$$
(A,B,\sqrt E A,\sqrt E B,wA,wB).
$$

SixPrimitiveIntegrator对每个闭panel先产生真实六函数值域。完整range×准确长度已经是有效积分包围。若其工作宽度足够则直接保留。

否则，在整panel的cap分支和q符号已严格确定时，对六个分量分别调用严格Acb积分。只有正常有限返回、虚部包含0才使用；与已有range×length包围取交，保留两种方法共同允许的完整区间。

Acb callback使用analytic标志处理sqrt分支。不能仅由实轴正性推断某个复球上解析；无法返回有限球时退回原完整实区间和细分。绝对值未判定处不做解析符号替代。

所有中间区间始终包含真实量。达到工作最大深度但已有有限range时，可保存一个较宽的有效包围，并将work_width_goal_met记false；这不会制造数学失败或伪精度成功。

若资源耗尽、当前panel非有限且不能再细分，则记录当前完整pending stack，并记录其后所有未访问原piece的索引后缀。不能越过缺失部分继续构造一个虚假的外端。

同一真实起点累计所有积分形成R_out；原名义cut只作差值报告。whole_range给出的正径向增量可与六primitive组合区间相交，这是同一真实函数的两个包含界，而不是改写积分或原参数。

## 7. 整个无限深尾的解析包络

深原点为准确rc，有限头内端为R286的raw r_o(A_159)。深部n≥160全部包含，不作有限截断冒全域。

代码先用R286的$W_N,H_N,L_N,M_N$，$N=160$，给

$$
1\le E\le1+W_N^2.
$$

为了在输出中同时给整个深域的E_r/E_rr界，使用一个保守但完全显式的正级数上界。对$k\ge0$且$H_N\ge2\log2$，

$$
H_{N+k}\le(k+1)H_N,\quad
L_{N+k}\le(k+1)2^{3k/2}L_N,\quad
M_{N+k}\le(k+1)2^{3k}M_N.
$$

配合$W_{N+k}=W_N2^{-7k/4}$，R286每cell导数界被下列正级数总和逐项控制：

$$
\sum_{k\ge0}(k+1)q^k=\frac1{(1-q)^2},\qquad
\sum_{k\ge0}(k+1)^2q^k=\frac{1+q}{(1-q)^3}.
$$

$E_r$的一阶项用$q=1/4$；$E_{rr}$的$L^2$和$M$项用$q=2^{-1/2}$，其$L$项仍用$1/4$。用总和代替上确界只会变宽，覆盖每个无限深cell及cuff，不是只评估第160cell。

深域还记录六primitive的自然未warp扩展A=dr_o、B=0：径向宽度为真r_inner−rc，meridian积分在该宽度和sqrt(1+W_N²)倍宽度之间，height在0和W_N倍宽度之间。此项明确为解析unwarped延拓，未假装旧factory实际调用过无限多个积分。

深域根族界无法满足某个任意细的工作宽度时，保留其有效整体包围并标注root-family resolution limitation，不选择一个未计算的根，不改为65/64，也不假定缺失根已经存在。

## 8. 闭径向query及逆像覆盖

可选query文件schema：

R286-original-stored-convention-C-closed-queries-v1

顶层必有config_sha256及非空queries。可以同时给calibration_ledger_sha256、stored_reference_sha256和original_profile_fingerprint，给出则必须与实际输入相符。所有query id唯一。

两种query：

- whole-natural-domain：准确符号域[原rc,真实R_out]；
- closed-rational-radius-interval：left/right为原finite JSON数或准确有理字符串，左右端点都闭，允许singleton。

若未给query文件，默认只请求整个自然域，不把名义cut当其右端。

对有理域，源码必须证明左端不低于原rc、右端不高于真实R_out包围的下端；若真实cut包含关系还未决，就保留whole-query unpaid。不能为了回答它而重选global alpha或移动cut。

每个完成source panel保存真实左/右半径区间和整panel E界。query只丢弃已严格证明径向像不相交的panel；所有可能相交者都保留，含共享端点。深尾是一个完整解析覆盖项。

需要细化时，对原参数panel二分，重新严格积分左半的全部六primitive得到真中间半径。两子段共享同一个中间半径包围，右端保父端点。每个子段重新包围实际表达；不是沿旧point.r作一个不明单调的binary搜索。

如果细化预算耗尽或子积分失败，父panel已知的完整有效包围仍在。代码保存父panel及所有pending siblings的完整区域和理由。于是可能出现：

- complete_closed_domain_bound=true；
- work_resolution_complete=false。

这是“覆盖完整但包围较宽”的正确状态。它与“源积分漏掉原片段，连外端尚未知”的不完整状态不同。未访问的后续query另保存完整query-plan后缀，不能假造其已经回答。

value-width-bits控制每个保留逆像片的E区间宽度，而非整个query上E的真实变化幅度；一个非恒定函数在大query上的最终包络本来可以很宽。

工作width目标只驱动计算精度；它不是原1e-6 metric门，也不是BVP、line search、reach或任何新增科学接受门。

## 9. CLI与预算

最小参数化入口如下。所有ACTUAL_SHA必须由真正输入原件填写，本文不预填未来field/run：

    python computations/geometry_20261115_stored_continuous_E_cover.py \
      --runtime-computations computations \
      --source-topic ORIGINAL_RESTORED_SOURCE_TOPIC \
      --config ACTUAL_CONFIG --config-sha256 ACTUAL_CONFIG_SHA \
      --ledger-ready ACTUAL_LEDGER --ledger-ready-sha256 ACTUAL_LEDGER_SHA \
      --stored-ready ACTUAL_STORED --stored-ready-sha256 ACTUAL_STORED_SHA \
      --proof results/R286-original-stored-continuous-integral-and-metric-bridge.md \
      --queries ACTUAL_QUERY_PLAN --queries-sha256 ACTUAL_QUERY_SHA \
      --out NEW_REQUEST_OWNED_DIRECTORY

query两个参数可以一起省略。默认工作参数：

| 参数 | 默认 |
|---|---:|
| precision-bits | 256 |
| integral-absolute-bits | 96 |
| integral-relative-bits | 80 |
| integral-evaluation-limit | 100000 |
| value-width-bits | 24 |
| max-depth | 48 |
| query-depth | 12 |
| max-panels | 200000 |
| max-query-nodes | 200000 |
| budget-seconds | 1800 |
| deep-definition | original-exact-root-family |

这些只是明确的区间工作参数及资源界，不包含当前场、不声称任何误差阈值已经满足。与原selector的48次循环无关：max-depth48是本组件可显式调整的实区间细分预算，**不是**重演或修改旧finite48算法。

当前生产器不包含工作流、网络读取或Git/Release写入；原输入与源码由后续公开Actions按真实来源恢复。没有因此调度一个尚未请求的科学运行。

## 10. 输出及完成语义

顶层result schema：

R286-original-stored-convention-C-continuous-E-cover-v1

正常元数据：

- input-binding.json：原实际文件/源/证明身份、完整冻结表、约定 C和工作参数；
- query-plan.json：每个准确原query及本次binding；
- query-results.json：每个已回答query的完整E包围/域责任/精度责任；
- result.json：总体范围、自然R_out、名义cut差、六primitive、深尾、接缝和所有状态。

临时large-arrays内：

- source-piece-index.json：完整1440源段索引；
- six-primitive-panels.jsonl：每个完整panel的六积分/六值域/方法/边界；
- complete-source-radial-panels.jsonl：有限头已付径向片；
- query-closed-inverse-cover.jsonl：所有已付或保守继承的闭逆像片；
- unpaid-complete-scope.jsonl：所有未付source panel、完整suffix、query或精度范围。

每个最终ledger/文件都记录实际bytes/SHA；写完fsync。浮点display仅供阅读，严格区间端点为整数mantissa和binary exponent。

核心状态必须按各自意义读取：

| 字段 | 含义 |
|---|---|
| full_finite_head_complete | 原1440段六primitive均有完整包围 |
| natural_outer_radius | 仅在完整头形成后给；不由名义cut代入 |
| original_exact_deep_root_existence_proved | R286根存在前提已在本输入满足 |
| original_exact_deep_root_choice_resolved | false，本次只给统一根族界 |
| protected_join / finite_joins | 原实际结构的连续拼接责任 |
| all_requested_closed_query_bounds_complete | 每个请求整个闭域都有有效包围 |
| continuous_convention_C_query_enclosures_complete | 上述完整包围且本输入连续模型条件已付 |
| numerical_work_resolution_complete | 工作精度另行完成；不是科学验收 |
| resource_or_unpaid_scope_rows | 保存未付范围，不以计数0代替根存在证明 |

始终false的责任包括：

- original_finite_output_certified_as_continuous_solution；
- original_continuous_g_model_choice_automatically_discharged；
- a601_same_field_binding_or_relative_metric_threshold_paid；
- actual_accepted_field_created；
- nonlinear_tail_or_ODE_or_shooting_J_run。

值域可能完整但宽；也可能预算只支付部分有限头。两者都不能被下游概括为“原metric已过”。

正常完成或诚实partial均可exit 0，必须读取上述原状态。运行内部捕获的异常exit 2；输入或I/O未能形成最终报告时明确非零退出；compact primary超90000 B时exit 70。成功进程退出不等于连续责任、精度或原metric已通过。

## 11. a601的实际接入边界

a601现有TAIL_SCHEMA是same-original-stored-tail-closed-E-envelope-premises-v1，TAIL_DEFINITION仍写原stored g_A。该旧消费者没有自动采用新的模型约定 C。**本组件不输出一个冒用该旧schema的文件。**

后续真正同场使用时应：

1. 明确目标采用约定 C，以及根族统一结论如何涵盖已选原深背景；
2. 以真正完整field binding生成该场所需的闭径向query计划；
3. 对自然R_out与原field径向域给实际身份/差项，不把二者硬等；
4. 使用本组件已证闭包围；
5. 在独立薄适配中明确新target/model/proof/source身份，再沿原R251全2×2相对算子和真实材料角pullback比较。

完整F仍是原有限表达，mean、SE2、cut、shared-B、两帽及phi→theta混合项均不由该E生产器改写。保护/外接缝未付时不能从schema消去责任。无实际接受场时不应填写上述field、threshold、tau或任何成功数值。

这不是新增审批门，而是防止把新的连续模型数据错接成已证明的旧finite对象。连续E的数值生产本身已落实在本源，剩余的是实际模型/同场身份和真正执行结果。

## 12. Rule15与本次检查范围

原derived raw均为本次out目录内可重算临时数据。未来公开Actions只保源/参数/实际run和输出SHA，stdout打印独立compact primary：

BEGIN_R286_CONTINUOUS_ORIGINAL_E_SUMMARY
END_R286_CONTINUOUS_ORIGINAL_E_SUMMARY

其内容包括各完整文件实际SHA、范围和状态。单primary若意外大于90000 B，源码保临时完整result并输出明确metadata-over-budget事件、返回70；不截掉query或声称其已公开。后续workflow应在真实读回后always清理本请求自有原raw，不上传或写入Git/Release。

本次只完成源码和接口。AST解析通过；数值模块仅在Actions guard之后由initialise_math导入；未执行该函数、任何Arb/Acb操作、校准、RHS、ODE、积分、selector、J、数据fixture或未来field计算。无Git mutation、无下载、无dispatch。
