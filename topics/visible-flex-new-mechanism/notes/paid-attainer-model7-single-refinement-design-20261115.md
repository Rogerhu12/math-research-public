# 已付四个全网见证下的同模型一次 primary 细化

日期：2026-11-15。状态：源码/数学设计；未执行新开发或科学。

拟 POLICY：same159-paid-attainer-single-primary-refinement-v1。

新文件仅为 scripts/frame_metric_paid_attainer_refinement.py 与 scripts/frame_metric_paid_attainer_refinement_development.py。transfer、恢复真实 objective/同中心模型、一次普通试验与原 SOC、audit/workflow/request 由 root 独占接线。全部旧源保持。

## 1. 已发生事实与精确的新问题

原 run43767357527/job132975354666/source6f886c385bdc12c8963d451369c9250fa19a45a0 的 m7 在同一真实最佳中心 $x$ 上已启动一次 inner LP（全局第10次），但因 pair allocation 的临时绝对 ceiling10，在生成下一轮 cut 前返回。该候选的 repaired affine 改善为负，未作普通几何评价。全局10/12并未耗尽，原 epigraph gap 为 $2.4768679406952238\times10^{-5}>10^{-9}$。

原中心为本次最终最佳点，$\eta=0.26623355613853394$，$B=0.00025$，bank438、pool4432/4525、版本1/2、legacy/covered0/0。guard 系数已提交为 coarse17.022353404161095、fine18.064283125328743。

本次只研究该未完成模型的一次新细化：**保原模型全部约束，在已付四个全网见证处加入至多四条新的合法范数支持行，然后只启动一次新 primary LP（全局 ordinal11），仍为原 SOC 留 ordinal12。** 不重跑第10次 LP，不重置 epoch，不启动第八个新外模型，不改变 score、guard、$g,b_0$、真实门和总预算。若无新支持行则零新 LP 停止。

## 2. 为什么不能声称恢复了原完整提案

冻结 solve_primary 的 report 只存标量、范数、残差和模型身份，159维 step 只返回给上层。memory inner 在共享 scoped ceiling 的检查处先 break，尚未调用 model.cuts 或 bank.remember。outer 收到 p=None 后直接 finish，记录 exact_binary64_independent_proposed_step 的语句在这条返回路径之后。

完整 oracle 的内存 cache 曾持有原 $p_*$，但 report 只保 direction SHA、四个 attainer 和标量；cache 中的159数组没有序列化。因此本次不重构未知 $p_*$，不宣称重复其所有 selected-separation 选择，不声称新支持行已对未知向量作完整 de/df replay。

保留的四个真实 observable 见证足以定义有效支持方向。这是从已付见证继续同一凸模型的有限算法，不是原内层任意中断点的通用 checkpoint 恢复器。

## 3. 原见证的定位与来源绑定

读取固定原 job 的 CURVATURE_GUARD_MODEL 第7项。其 linear_program.complete_original_grid_model.oracle.direction_events 中唯一 ordinal1、phase=primary-inner、status=complete 的非零方向 event，保存：

- direction SHA：4ece9d67a3f29d901c4e27d4880f8cc56283cbda474b8c76e65f003bfbe60634；
- center binding SHA：b1cdea784c2e85779174d7ab90532dc6677893b44ab84dadb208e2c7b8b0077d；
- 四个 attainer，顺序为 coarse+、coarse−、fine+、fine−；
- 每项的 original_row（grid/group/flat_row_id 及原网格坐标）、original_point_flat_index、radial_index、theta_index；
- 每项的 phi、base_e/base_f、de_step/df_step、affine_e/affine_f；
- maxima 和 grid_scans 的完整覆盖记录。

原 COMPLETE 的完整 oracle progress 第7项也有同一 event。两处同时存在时应核相等；不能把 observer 按深度省略的 metadata 当真实数组。已有 canonical JSON metadata（排序键、紧分隔、无LF）为：

| 子对象 | 字节 | SHA-256 |
|---|---:|---|
| attainers | 1744 | 5dc115ca8583b98b842050ee7227f6f46f9f9d4b85896d2513c850d443556bc7 |
| grid_scans | 629 | 346d255e3c0801e7e0917a573c362b9ca7b9ecedd77be8e8b9d84316a0475538 |
| maxima | 78 | 7ec739759014291aa5b404a6af8175176627039fb673e281149ab4043aa63de3 |

本次输入消费在 runner 只读原已完成日志。原 log7918876B/SHA8ce149f015b3139625e9a3ee887b407977ca4c7ca94387379e98dc986fe730af；COMPLETE+LF1700302B/SHA6208d8519e766141b46a70a329fb9ae84b9ddbfb8617016b85304a50b9a26194。其140Python/146总绑定和已付开发按原回执核对，旧开发不执行。不得把这些可重算 payload 写入 Git/artifact/Release。

## 4. 支持行的数学正确性

原两个 regularized metric 分支为

$$
\phi_\sigma(e,f)=\frac{\sigma e+\sqrt{e^2+4f^2+\epsilon^2}}2,\qquad \sigma\in\{1,-1\}.
$$

对任何真实三向量 $n$ 满足 $\|n\|_2\le1$，Cauchy–Schwarz 给出全局下界

$$
\ell_{\sigma,n}(e,f)
=\frac{\sigma+n_1}{2}e+n_2 f+\frac{n_3\epsilon}{2}
\le\phi_\sigma(e,f).
$$

由原 attainer 的已付 $(E_*,F_*)$ 取 $n=(E_*,2F_*,\epsilon)/\|(E_*,2F_*,\epsilon)\|$。实现复用原 unit_ball_direction：浮点归一化后必要时向零移动，逐项用 binary64 有理数验证平方和不大于1。无须知道生成这对 observable 的159维向量，所得方向仍给所有 $(e,f)$ 的下界。内移使其可能不是精确接触切平面，应记录真实原点支持缺口，不伪称零。

在恢复的同中心原行上，

$$
e(p)=e_0+d_e p,\qquad f(p)=f_0+d_f p,
$$

故 $a=((\sigma+n_1)/2)d_e+n_2d_f$，$b=t-((\sigma+n_1)/2)e_0-n_2f_0-n_3\epsilon/2$。原 mapped LP 变量为 $z=p/\text{step_scale}$，附加

$$
(a\cdot\text{step_scale})z-\rho\le b.
$$

复用原 support_row 完整组装，不改原目标、norm penalty、耦合物理盒、hard rows 或曲率 guard RHS。该行是同一完整两网 affine epigraph 的有效松弛约束；浮点组装及最终残差仍受原数值门约束，不是区间证书。

可按原 $\phi(E_*,F_*)-t-\rho_{\rm old}>$ 原 gap tolerance 筛出原见证中的违反分支，并记录内移后支持值的缺口。即使原 JVP 与新逐行 J 的微小舍入差不能对未知 $p_*$ 重放，下界有效性仍不依赖该接触主张。代码不得把缺失 replay 写成通过。

## 5. 同模型恢复必须保留的数组与身份

root 构造真实 objective，不调用旧完整 epoch 的 run。current_model_binding 须由该 live objective 的真实pool版本和原 model_binding 生成；core 再核可读取的原数组/映射/最终签名，不能把旧报告直接复制冒作新 live binding。恢复：

1. 原159中心、完整163重构、同reference、$g,b_0$、source cfg、M/原width/subspace/coordinate/grid与永久anchor；
2. 原438有序 bank entries/context/hash；原pool整数ID/顺序与版本1/2；不能默认再initialize/min-row补池；
3. 原学习state、maximizing event indices、两coeff及m7冻结guard targets，不重新导入旧paid样本改变state；
4. 原 guarded primary 的 active values/J/groups/tolerances/state/step_scale、A/c/lower/upper、guarded targets/RHS和两个 observable factories 的最终 binding；
5. 原 initial memory cut round 的438行 A/b摘要、原行顺序和bank hash。

原 guard 报告已含 unchanged_array_sha256、before/guarded target/RHS hashes；原 model_binding 含 base/M/width/subspace/coordinate/active-row-mapping与最终含v/J的模型签名；原 complete model含selected observable及oracle binding。当前可比字段必须逐项核同，不能仅凭 source schema 一致就跳过。纯执行元数据差异若有必须明列，不以其为由豁免物理模型数组差异。

原438 memory行一次重建后冻结。新见证行附加到其后，按实际 A/b指纹去重。即使新 normal 与原 bank 某同row的normal不同，**本次LP仍保留旧438行**；后继bank选择规则不能在当前模型删掉旧约束。本薄 core 仅把新支持附在本次LP，不调用 bank.remember 替换原438 entries；新增方向作为本次支持记录保留，是否用于后继 memory 属显式的新输入选择，不默改当前bank。

见证点 e0/f0 与原base_e/base_f按冻结 replay 容差核同；row ID/分支/原网格坐标与point index必须严格一致。若需要补该原点de/df，只作必要的原 selected-row J，实际计费。旧方向的整网JVP不重复。

## 6. 一次新 LP 的 ledger 与返回语义

core 接受现成同模型 primary/model/cfg，以及已经继承原计数的 ledger。入口要求原 total=10、primary=10、SOC=0，共享limit12；原m7已付inner1、gap未合、gain不改善且没有任何trial。新调用在真正solver启动前计 total11/primary11，异常也算已启动。每模型至此累计inner2，不超过原3；core不含第三次求解循环。

新LP时间限制不超过原单LP10秒与实际剩余active时间。必要恢复、选行J、cut组装、新候选JVP/普通值/SOC均记录真实费用；不得以“只读恢复”隐去实际几何或导数调用。原共享clock/值额度的已消耗部分随恢复继承，独立末验仍另列。若耗尽，不调用solver。

新LP复用 frozen_solve_primary；候选复用原 _candidate，在完整两网 affine 模型上重新评价 rho、向上修复auxiliary，并核新旧全部约束与bounds。旧未返回候选只保其已报告 scalar objective/gain作来源及严格better比较，不伪造step或再评价它。若新候选未优于原nonreturnable incumbent，或者没有原floor之上的repaired改善，返回无提案。若有改善，则沿原合同允许返回已标记的 inexact cut候选；不额外强加gap必须合，也不把未合写成已合。

只有新的真实159方向可进入普通trial与原SOC。旧group8guard只用于普通primary；原same-layout/expanded SOC的RHS、retention、actual-total-step诊断、learning/hold/fallback保持，最多占唯一余下ordinal12。不再次开新primary、重做旧第10LP或因失败无guard免费重解。

## 7. 报告不能混淆的三层

报告分列：

- 原付事实：m7原LP ordinal10、旧cut lower bound/affine gap、来源direction SHA与四observable见证；未知159 step明确缺失。
- 本次恢复/支持：具体身份核对、原438行hash、每新normal的exact-unit-ball检验、原见证分离/内移缺口、新行去重及真实J/组装费用。
- 新执行：唯一新primary是否启动（ordinal11）、原solver状态/repair/gap/actual gain、是否实际trial、是否进入原SOC ordinal12、真实所有门、末best与余预算。

没有新行时报告no-new-paid-witness-support/0LP；绑定或预算失败保原best并报告具体位置。新LP失败/新candidate无改善仍不能冒作完整凸模型或真实问题驻点。

## 8. 最小源码接口与新开发范围

core 拟导出：

- build_paid_attainer_supports(primary, model, cfg, *, source_model, source_event, current_model_binding, progress, wall)；
- solve_one_paid_attainer_refinement(primary, model, cfg, ledger, *, source_model, source_event, current_model_binding, progress, wall, remaining_seconds, solve_one=None)。

production的solver固定为冻结函数；solve_one只在有明确人工array flag的新增fixture内开放。core不fetch、不dispatch、不改ref，也不在import时运行开发或科学。

新增开发只覆盖新接口：四见证/源binding及缺step范围；新support的附加/去重且原438类行不被替换；无新行0LP及唯一新LP先记账/异常不漏账；原rho修复与nonreturnable旧incumbent比较。可使用最小人工array和stubsolver，不能调用旧18/20/19/26/cache开发，也不重测旧全几何/求解器套件。冻结为四组各4项、共16项；所有检查尚未执行，不预称通过。

所有新开发和实际首次执行仍由root在公共Actions完成。本设计没有预期收益或成功承诺；它只支付了一个数据充分、约束有效、额定成本有限的真正新问题。
