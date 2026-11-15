# Request157：完整九维三残差二次平方模型与真实直线回溯

作者：ChatGPT（amplitude）；日期：2026-11-15。状态：源码和唯一请求已准备，尚无本请求运行或数值结论。只在本公开仓库Actions执行科学；本地没有运行模型、导入科学模块、FD、优化、fixture或编译数值程序。

代数、有限选择与误差范围见 [R336](../results/R336-complete-nine-residual-quadratic-square-and-finite-globalization.md)。实际来源见 [R335](../results/R335-actual154-full-nine-curvature-and-seventy-straight-trials.md)。本入口接真实154的末九个持久Decimal50参数；它未声称原低三条件已满足或已取得非零112全场。

## 1. 完整交付与版本

以下七个运行/参数/接线文本全部为新basename。旧154、149及其全部祖先源码保留。此接口和R336另作为正式文档；完整相对154差异为纯源文本比较，不是删除旧文件的patch。

| 文件 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_nine_control_decimal_residual_quadratic_trust.py | 31941 | ef61c5f19370a302b198901a7691fda31ed0a6619d9f9dcafc147f6b1bdc3180 | b87263d33fa2230b770b26c23e936ae872c0e7a4 |
| geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py | 28570 | 54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100 | fc5f76e3ec7ed1163d167cfb4a631535330cad39 |
| root_20261115_nine_control_decimal_residual_quadratic_scalar_readout.py | 17532 | a49ebce03156e8ee620ea7cab62e51c32f2a924458ad6d2320e85cf91398897d | 4c985ef65567c31162afbf643a266bf96c82c2f9 |
| geometry_20261115_nine_control_decimal_residual_quadratic_temporary_batch.py | 22398 | c992f30af23a94535a6dff70342172f5a066498c77e53a15e60e0e2222ac90f8 | b766bb9631ca47f41dff9f2af847d1daeb8fe80e |
| public-nine-control-decimal-residual-quadratic-parameter-recipe.json | 3184 | 2dba85467fd34435efc0a4f44ed0335c787c049a6095735b955ad365aa62f49f | f0fdb094aded81faae239cd5da7e91c94bda134b |
| public-nine-control-decimal-residual-quadratic-request.json | 55526 | 94e01eeb04f24f93463d0d59602b228c7ea061186edb54f5d99bb35168199dd6 | c4d084d13298d8a352b5a86011753c79ffc5aeb3 |
| visible-larger-public-nine-control-decimal-residual-quadratic.yml | 22302 | 905e137e0d4724f9aa2a7d60aadb265e1643e73afa543a17ff4527aa883aceaf | def050c07731df85359836dd991d02238bdb3515 |

同一组完整比较由七份 `request157-{search,producer,reader,wrapper,recipe,request,workflow}-relative-to-frozen154.diff` 提供。正式发布位置：Python与JSON在本课题computations；workflow在仓库根.github/workflows；本文在notes。差异对象只供审读，不要求作为额外科学检查或附加发表门。

## 2. 真实父点、字节来源与新策略

原run为43724606619，source为2a4ce61f26a2f9d6f0f2729e037ee6c0b8220e5b，producer为geometry_20261115_small_core_nine_control_decimal_curvature_recipe.py，原schema为R259-nine-control-persistent-decimal50-ambient-curvature-trust-v1。

原status 5,917,531B / b4c1e07a3d81dd8eb64f3ba28a889f2868accd3b666c14c3deb4ddccef835e83；原primary 88,658B / 7e03106069419b6d701bc0b86479c96fbf9615bdb8b761e01142110bd6ab5fed；完整scalar view 5,920,990B / 92e24bf835966ad980f44bd8b93f0476a2bdbd7ed85e617bbe6848fbe069b1f7。上述原输出已按R335读取，本次执行不下载、伪造或重序列化它们作新status。

实际九参数从原final.parameters逐字符串复制：

```json
[
  "0.30552141421813587451511124647832115183365931393255",
  "0.21644994882174284564428467846307106691034173126682",
  "0.34270115519083356085666200795448211747040865537076",
  "-0.063223397664120006022611230482040760191219350613381",
  "-0.017474484994182094846554068297420896682316648212971",
  "0.93761127574242591532855416219549982285362989617547",
  "1.0751308300363195964465271254236787053010018303407",
  "0.68868929652522927733976315755005254248094417316641",
  "0.93853619119844242504207635330603652071213943405455"
]
```

真实父radius为字符串0.000078125。新experiment明确使用0.01，父radius只作provenance；这不是carry-radius续批，也不是与154同一基点的单变量因果对照。

运行recipe独立schema为R259-explicit-nine-control-decimal50-residual-quadratic-exploration-recipe-v1。它严格绑定origin run/source/producer/schema/status bytes+SHA/primary bytes+SHA以及原parameter/radius字段。九参数必须为有限Decimal字符串，不经过float转换；原J、Hessian、state、merit、FD不继承，全部按当前p重新计算。后续本新producer的ownschema也可作为显式parent，仍需真实来源字段及明确新策略；当前只有一批八方向请求。

## 3. 同一有限模型与完整闭包

原4数学输入不变：

| 原输入 | 字节 | SHA256 |
|---|---:|---|
| accepted actual.json.gz | 2,614,352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared.json.gz | 4,220,043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| outer-00-anchor-tail.json.gz | 6,815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| T112-config.json | 2,161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

它们只按历史8bd267107cc8710d371f3b62c02986655ac965b0原path恢复到RUNNER_TEMP，检查完整size/SHA。原78 public numerical sources沿冻结restore入口恢复一次；源缓存与输入在本请求owned目录消费后清理，不新增raw artifact或Release。

原source map104件全部保留，再加新search/producer/wrapper三件，总107；原support map8件全部保留，再加新reader一件，总9。producer实际来源账原39变为41：只加入新的search与producer，旧39逐项保持。运行中的全部41源报告与请求current_producer表逐项比较，不把历史104个hash都称为实际执行的科学代码。

关键复用关系：

- LiteralNineModel仍是原149的2422be0c…完整699节点有限字面模型。原binary64系数独立按各自words提升；不重新计算连续g、积分表或native锚J。
- LiteralCircleModel使用原154二阶模块ad568abc…，完整3×9×9 Hessian及full112二阶右行全部保留。该文件未修改。
- frozen154的bb603fc6…模块仅提供完整jacobi_full和shifted_cholesky等明确辅助函数；不执行其ambient_direction或旧search。
- frozen149的433d5ddd…提供完整12×9 QR、原next_radius，以及只有显式进入fallback时才运行的complete_direction/curve_frame/curved_candidate。原normal轨迹和R299全merit选取不改。
- 原154 producer及149 producer保来源身份，不执行旧main。原146的load_baseline仅用于已有source/input/setup责任。
- 原literal binding10数组rawSHA、形状和各项提升范围继续完整输出，与actual154来源比对属于实际读回，不是新的科学接受门，也不预承诺不同Actions有限字节必同。

## 4. 新模型与21槽有限求解

在一个原外方向中固定当前$p$和$D_j=\max(1,|p_j|)$。完整模型为

$$
Q_i(y)=F_i(p)+(JD)_i y+\tfrac12y^T(DH_iD)y,\qquad
\Phi(y)=\tfrac12\sum_{i=1}^3Q_i(y)^2 .
$$

新源在每个内部$y$都重新形成完整三向量$Q$、3×9 $K$、九梯度和9×9 $K^TK+\sum_iQ_i(DH_iD)$。每个缩放Hessian只形成上三角后原字镜像，原未缩放Hessian照存；不把字面舍入下的变分当准确实或区间证书。

一个外方向最多32次内部模型更新。每更新固定21槽：完整12×9 residual-GN QR、完整移位Newton、Cauchy，以及完整九谱列各正负两方向。只有有限负曲率的谱槽作为负曲率候选使用，但不使用的槽也记录原因。

residual-GN使用$\lambda=\|K^TQ\|/\delta$及增广$[K;\sqrt\lambda I]$完整QR，不改三行权重。它只是一种提案预条件器，与完整Hessian候选并列。准确实数的下降和半径恒等式见R336；有限QR残差不冒其严格外包。

每个候选先把端点投影到同一相对球，再使用实际投影弦重新形成斜率和曲率。每槽最多20个模型回溯；每个试探都计算三个二次残差的完整平方，未只用四次ray系数来决定最终九维位移。内部ray选择首个严格模型下降且过明确模型Armijo的有限点，随后工作迭代取这些首过点中最低$\Phi$；这只是内部工作轨迹。

最终提案从所有完整评价、在形成球内、$\Phi<\Phi(0)$且原点形成斜率负的模型点中取最小$\Phi$。因此可能选中一个没有成为内部工作返回点的完整已算样本。完整有限集合和索引保留；不把不完整、非有限或未访点补为合格点，也不把有限最小值叫作球上全局最优。

模型局部半径携带：对已经实现的模型弦调用原next_radius、控制器alpha=1，再cap至外球；不只因模型回溯就halve。所有模型槽拒绝时局部半径quarter，模型点不变。这是本请求明确的新提案策略，不改变原外owner半径的规则。

## 5. 真正接受路径与原回退

选中的完整九维位移$d=Dy$先在原当前p重新作一次完整第一forward方向响应，取得实际三向量action及原unweighted slope。实际斜率不有限或不严格负则本主路径没有可用方向；不能以模型下降替代它。

主路径为真正直线$p+\alpha d$，原20档$\alpha=2^{-j}$，每点评原完整三残差和原有限域。接受仍为实际$W\le W_0+c_A\alpha s$，$c_A$为原binary64字面0.2的提升。没有Hessian、模型误差、内层目标tol、FD、rank或因子残差的新接受门。

每个实际alpha保存完整$Q(\alpha y)$、$\Phi$及linear/quadratic/cubic/quartic展开项，保存真实三残差减模型三残差和真实merit减模型merit。ray展开只用于说明，不冒两种舍入形成顺序逐字相等。模型预测与实际比较即使很差，也由原真实Armijo决定接受或拒绝。

主方向形成失败或20档全拒后才调用原149独立normal回退，仍20外档、12×20内更新。原normal后两项目标$F_{2:3}(p)+\alpha\,action_{2:3}$并未换成多项式目标；原R299 selector不救未完成调用，inner target也不变成外门。两路径有不同标签；普通真实接受、数学/域失败、计算异常、资源partial与所有未访后缀分别输出。

原外next_radius保持函数原字节：本主路径只把prediction替为完整残差二次平方的预测下降，fallback仍原线性残差预测。原回溯接受halve和两路径全拒quarter均保留。只作一批原8方向，不自动再串32批。

## 6. 完整模型与失败读回

producer schema为R259-nine-control-persistent-decimal50-residual-quadratic-square-trust-v1，原status basename为nine-control-decimal50-residual-quadratic-status.json。

每个outer row的direction_model包括：

- 当前原完整F/J/3×9×9 Hessian、完整缩放A/三H、原点梯度、radius、相同primal word比较和第一/二阶J差；
- model_updates每次完整Q、K、九梯度、9×9模型Hessian及完整有限谱引导；
- 全移位尝试、九解、九项线性残差、pivot或失败pivot；因子/formed-matrix cells明确仅canonical JSON SHA，未宣称独立导出因子文件；
- 每次完整QR的12残差、9stationarity残差、排列/对角与显式Q/R细胞hash范围；
- 21候选槽全部的实际弦、projection、斜率、曲率，完整trial表、原点斜率、global候选索引、内部是否接受和exception；
- 每个更新剩余候选索引、每个候选剩余20档索引、移位bracket/refinement未访索引及剩余32更新；
- 最终global_model_candidate_count、胜者完整引用、九位移、fresh原方向action、真实slope、失败或完成范围。

模型trial固定列名为：

```text
trial, beta, actual_relative_point, full_three_model_residual, full_three_model_merit, model_Armijo_bound, formed_relative_point_L2, within_formed_global_ball, formed_original_point_slope, eligible_for_final_model_selection, global_candidate_index, accepted_for_inner_model_update, exception
```

矩阵/残差字符串由原Decimal50返回；reader不计算科学量。完整raw status先映射成scalar view：schema另存producer_status_schema，searches映射outer_searches，其他原字段无白名单丢弃。每段及primary都≤90000B；大数组按具名JSON路径、连续列表范围分段并保各段及完整组/整view canonical SHA，不能把方向或模型trial截掉。原所有真实normal记录照保。模型失败时完整已算记录和明确partial仍读回。

新reader schema为original-nine-control-decimal50-residual-quadratic-segmented-complete-readback-v1。stdout主标记为BEGIN_VISIBLE157_PRIMARY / END_VISIBLE157_PRIMARY；wrapper保原reader全部stdout于BEGIN_VISIBLE157_ORIGINAL_READER_STDOUT之间。chain为BEGIN_VISIBLE157_CHAIN_SUMMARY，schema为nine-control-persistent-decimal50-residual-quadratic-square-single-batch-v1。

chain仍有全部8计划方向行，不到达的行写started=false及实际原因；新增每方向内部update数、模型点数/候选数、选择的model merit与completion字段。完整内部矩阵/试探不塞入GITHUB_OUTPUT；它们完整在compute的无损分段中。report只转发≤90KB完整chain索引及SHA。若索引真超限则保明确失败，不删除字段伪称完成。

## 7. 原最终检查与持久点/投影区别

这些责任逐字沿用154 producer的科学函数调用：

- 初末各完整九轴三步持久第一FD，共54；
- 初末各完整九轴三步二阶FD，共54，比较每个二阶轴下完整3×9第一响应差分；不按误差数值提前筛选或抹去失败；
- 初末各原binary64投影九轴三步FD，共54；明确projection值、float.hex、exact lifts和p50差，不反写真实参数；
- 原160bit/depth14 scalar Arb与完整453 circle在最终明确的binary64投影点运行；
- 全112线性右行、high109原项和原所有unit/full112/final flags完整保存。

原高模非共振、真实native尾、fullDN与非零全场接受没有被本九参数模型替代。producer仍不调用native/fullDN，nonzero_field_completed与success不因模型或低三改善改成true。Decimal50不是区间；投影点检查也不冒持久点的连续全域证书。

## 8. 可执行调用、唯一触发及墙钟

producer独立CLI如下，其中所有路径指向当前请求owned临时输入，SHA由已冻结请求提供：

```bash
python -u geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py \
  --accepted "$ACCEPTED" --prepared "$PREPARED" \
  --tail-anchor "$TAIL_ANCHOR" --tail-config "$TAIL_CONFIG" \
  --parameter-recipe "$RECIPE" --parameter-recipe-sha256 "$RECIPE_SHA" \
  --out "$SCIENCE_OUT" --decimal-digits 50 \
  --candidate-steps 8 --backtracks 20 \
  --normal-iterations 12 --normal-backtracks 20 \
  --normal-target-tolerance 1e-8 --candidate-resonance-tolerance 1e-8 \
  --interval-bits 160 --interval-depth 14
```

内部32更新/21槽/每槽20模型档、移位32+32是新search中的明确常量并在原status报告，不新增可暗中改门的CLI。外部仍是原8方向和两条明确各20档的物理路径。

唯一push trigger是本课题computations/public-nine-control-decimal-residual-quadratic-request.json；workflow独立basename visible-larger-public-nine-control-decimal-residual-quadratic.yml。没有额外workflow_dispatch、native或fixture任务。

Python3.12.14/numpy2.3.5/scipy1.17.0/python-flint0.9.0，三BLAS线程变量均1，Decimal标准库50位/ROUND_HALF_EVEN。compute job90分钟、science step75分钟、report10分钟与154相同；不隐藏另一个child timeout或detached session。新模型运算有明确有限budget，但本地未benchmark，不能预言它一定在墙钟内完成。

每个外方向最大32模型更新、672固定候选槽、13,440模型trial、2,048移位尝试及32QR；八方向相应最多256、5,376、107,520、16,384、256。它们只是新增小维数多项式提案工作，不冒算成原20真实档，也不新增原699节点调用。原新Hessian形成至多10次，原初末二阶FD的108次第一响应仍明确付。

所有原参数及输入pin检查是来源/执行约束，不是新的数值精度接受门。脚本异常或规则/墙钟中断保真正phase/resource_partial/exception、当前真实owner与尚未付范围；诊断完成与科学成功严格分开。

## 9. 规则同步、错误保存及清理

原root_20261114_current576_rules_runner.py文件保持冻结。只有当前两README全文及已审blob作为BASELINES进入其原入口，2700秒真pull/rebase/差异停止、唯一H规则行及原process-group责任不变。当前根21bd547f56590b7f2dd279d0297efb289a9b2783，课题bff8aea253a9e6a7a4fac28d810ac454c5499fec；有真实新差异时按原规则停并重读，不改runner绕过。

workflow保git merge.stat=false。runner临时Git对象缓存只为原来源恢复/同步，非新增科学raw归档。完整科学及reader stdout/stderr在清理前按原字节范围分段打印；workflow直接ensure_ascii=True输出，可完整恢复非UTF8原错误字节，不经过会重编码lone-surrogate的中间watcher。producer尚未建status时的实际stderr也保，不能仅留hash。

最后仅清本请求RUNNER_TEMP内的science/input/public-source cache；先完整reader及chain，再owned cleanup。没有把可重算raw放main、Release或新artifact。清理成功不冒科学完成，清理失败也不改任何数学终门。

## 10. 文本核对与实际读回责任

已做的仅是纯文本/JSON/UTF8 SHA元数据操作：确认原104+8表逐项不变、原4输入/运行库/README相同、origin39=current154、current41为其加2、九参数与原154final字符串一致、半径字符串一致、新源pin与当前文本一致、recipe size/SHA吻合、全部交付小于100KB。环境不可用，未声称本地AST、编译、模型或fixture运行；workflow原源AST步骤仍保留。

所有比较diff为完整文本差异，没有省略科学函数变化。producer初末投影/FD/Arb/圆函数调用及原异常/finally责任保留；reader无损分段及wrapper临时生命周期只变身份、闭包与必要的模型计数字段。真正科学结果须由唯一公开run完成后逐原segment重建；当前没有未来run/artifact/新接受值。

Request157实际将直接检验有限tensor模型能否给出比154更有效的真实位移，且同时保存为何模型良好或失配的三向量证据。成功的模型内迭代、较小模型残差或有效FD都不等同于原方程大步通过。
