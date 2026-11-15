# 由已观察曲率缺陷学习下一 primary 提案余量

日期：2026-11-15。状态：新算法设计；尚未执行新增人工检查或科学运行。仅消费已经完成的 run 43762868037 / job 132961344492 的真实输出及其冻结源码。作者：tail_cost。root 负责所有正式提交、workflow、request 和公开执行。

## 1. 问题与本次唯一变化

当前真实最优 checkpoint 来自 source 4f1365300b70831550d544df119d738b2531eff5：

- 两网最大 metric 为 0.2662701215525791；最大曲率为57.99998346840656。
- 完整有序 norm bank375条，原两池4432/4451，$B=0.00025$，legacy/covered streak均0。
- 本轮6个模型全部得到真实接受点，其中模型2、6的首个完整普通步在原曲率门失败，原 same-layout SOC 随后用很小修正支付曲率。
- 该轮新增 covered-soft 规则未产生额外增长。不能通过重复上一阶段等待它触发。

新方法只学习下一 primary 的曲率提案余量。保留原几何、$g,b_0$、permanent anchor、独立159/物理163映射、全部实际两网门及其容差、原 soft convex model、原行池学习、原 SOC RHS、ordinary/expanded/same-layout fallback、两 streak 和12 LP/40值/120秒active/每LP最多10秒预算。

策略名固定为：

**same159-observed-curvature-defect-primary-guard-v1**

新类 **CurvatureDefectGuardObjective**，阶段键 **curvature_defect_guard_stage**。

首版只覆盖两个桶 $(\mathrm{coarse},8)$ 与 $(\mathrm{fine},8)$。group8是已有原尺度PSD determinant行，不是直接主曲率数值；不能把其余量与曲率58的差直接混为同一单位。其他7/9/10曲率组仍使用原提案与实际门。

## 2. 已观察证据

冻结原函数 curvature_trial_diagnostics 在池学习前，读取同一实际候选的缓存。其预测明确是

$$
v_i(x)+J_i(x)(y-x),
$$

其中$x,y$是真实独立159状态，$J_i$与$v_i$来自同一已接受中心及同一原行序。不是用LP返回的名义$p$替代实际$y-x$，也不是用SOC在$y$处的校正预测。

本次已经付费的记录包括：

| 源模型/网格 | 原group8预测/实际或组内缺陷 | 记录值 |
|---|---|---:|
| m2 fine，实际最小行的预测 | 原单位 | 1.0000000068338184e−7 |
| 同行实际值 | 原单位 | −1.8153050309734704e−7 |
| 同行 actual−prediction | 原单位 | −2.815305037807289e−7 |
| m2 fine，整个已选group8最小缺陷 | 不必与实际最小行同一ID | −4.920795264595768e−7 |
| m6 fine，flat ID1091917的预测 | 原单位 | 9.999999968672221e−8 |
| 同行实际值 | 原单位 | −1.1536221166007416e−7 |
| 同行 actual−prediction | 原单位 | −2.1536221134679638e−7 |
| m6 fine，已选group8最小缺陷 | 不假定argmin与上一行相同 | −2.9204490656353777e−7 |
| m6 coarse，已选group8最小缺陷 | 原单位 | −2.339915512183932e−7 |

不能把 selected_predicted_minimum 与 selected_actual_minimum 相减后冒充同一行缺陷。学习使用原 minimum_actual_minus_prediction，即同一行差逐项计算后的最小值。原负数、临界行记录及整体门失败仍原样保存。

该输出支持“下一提案需要更可靠的曲率预测”这一新子问题，不证明本方法已经改善收敛，也不证明所学数值是后继中心的误差上界。

## 3. 有限学习状态与真实步范数

对一个合格历史样本$s$，令

$$
d_s=y_s-x_s,\qquad
z_s=D_{\rm phys}^{-1}M d_s,
$$

其中$M$为原159到163物理映射，$D_{\rm phys}$为原盒宽度。采用原subspace.step_norms的共同body尺度：

$$
b_s=\max\{\|z_s^{\rm body}\|_\infty,\,
8\|z_s^{\rm tail}\|_\infty,\,
\|z_s^{\rm height}\|_\infty/4\}.
$$

五个独立height坐标的范数不能代替最后一个真实九height物理块。必须从实际$y-x$构造，不能用model B或LP名义step代替$b_s$。model B另保留为来源信息。

对每个原网格$g$，从已选group8的真实差取

$$
\delta_{s,g}=\min_{i\in S_{s,g,8}}
 \{v_i(y_s)-v_i(x_s)-J_i(x_s)d_s\},
$$

并定义非负经验量

$$
a_{s,g}=\frac{\max(0,-\delta_{s,g})}{b_s^2}.
$$

学习状态只有两个系数及其达到最大值的来源：

$$
\gamma_g=\max_{s\ {\rm 已提交}}a_{s,g}.
$$

不引入额外安全放大倍数或新调参。非负部分是策略的明确定义，不覆盖或裁剪原负缺陷记录。原正缺陷不将已有$\gamma_g$减小。

要求$b_s$有限且严格正，系数计算有限，原网格/坐标/物理映射/宽度、固定曲率尺度和source cfg身份相符。零或非有限步不更新该样本并记录原因；结构错误、错source/错网格/错原状态不得静默当成有效样本。缺少fine实际值时，只能记录已有coarse样本，不能补零fine数据。

两个桶的最大值是经验记忆，并非行级或全域上界。原选中集合发生变化时，历史单位与网格仍准确，但其在新中心/新行上的泛化仍是新提案假设。不会把这些历史scalar冒充新中心的旧Jacobian行。

## 4. 下一 primary 的准确RHS

先调用原 selected_model/build_primary 得到完整原mapped LP。记其原group8提案target为$t_i^{\rm old}$，原固定floor为

$$
f_{\rm curv}=10^{-7}.
$$

本模型冻结$\gamma$，在原半径$B>0$处仅对当前已选、真正属于原variable domain的group8行设置

$$
t_i^{\rm guard}
 =\max\{t_i^{\rm old},\,f_{\rm curv}+\gamma_g B^2\}.
$$

其他行保持逐项相同。原hard行约束为

$$
-J_i\,\mathrm{step\_scale}\,z
 \le v_i(x)-t_i,
$$

所以只将这些行的$b_i$改为$v_i(x)-t_i^{\rm guard}$，同时准确更新primary.targets。

以下全部保持：

- 原完整$A$、$c$、上下界、159到163物理map、coupled原盒/信赖域/physical norm行。
- 原active values/J/groups/tolerances和两网原整数ID顺序。
- 原soft scalar行与complete affine-e/f convex norm cuts、rho上修与最终原单位残余检查。
- 原7/9/10及strip组等其他提案targets。
- 原固定外域、zero-J行分类及保留规则。

不删zero-J行。如果更高target使此LP不可行，必须如实使用原solver失败、计费与缩径；不钳制target到当前base，不免费重求未加guard的模型，不把guard“成功”写成实际门通过。

当$\gamma_g=0$时该网格所有提案数值必须与旧模型逐位相同。$B$减半时经验新增floor部分减为四分之一；原target的max仍按原公式保留。没有修改source cfg里的固定floor，更没有将实际curvature门的容差放宽。

### 4.1 为什么采用平方尺度，以及它不证明什么

如果同一行函数在连接$x$与$y$的邻域为$C^2$，Taylor余项有

$$
v_i(x+d)-v_i(x)-J_i(x)d
 =\int_0^1(1-t)\,d^\mathsf T
   D^2v_i(x+td)d\,dt.
$$

这解释二次尺度的来源。有限样本并不提供整个邻域Hessian上界；端点regularity检查本身也不授连接线段的全程regularity。因此$\gamma_gB^2$只用于提案，不能宣称连续误差证书、后继网格全覆盖或实际严格可行。原真实两网验收仍拥有最终决定权。

## 5. 同一模型冻结、下一模型提交

只有首个完整普通trial允许产生新样本：

- kind为原 primary-metric-short-step；
- alpha_exact严格为1；
- 同一原accepted center和当前primary的两次factory最终签名；
- 使用池学习前的原完整selected-row诊断；
- 不是SOC、parabolic backtrack、expanded rebound或其$y$处校正诊断。

新样本先进入pending记录，不能在该模型的inner LP、后续backtrack、SOC或incumbent校验中改变当前$\gamma$、targets或$b$。这样同一模型的原repaired-incumbent论证与cut residual合同不变。

只在下一普通primary建立前提交pending；若本轮退出则在最终checkpoint记录中提交已完成、来源明确的pending，但不追改任何已求LP。新模型记录使用的learning-state SHA，源模型记录样本何时提交及哪个后继模型首次消费。

异常/early return保留已启动LP和值费用和最后真实接受点。不存在“样本没提交所以当作未观测”的费用擦除。

## 6. 原SOC、complete model与签名边界

### 6.1 原SOC RHS确实不读新target

冻结 build_correction 读取primary.active_values/active_J/groups、真实$y$行、原scalar predicted gain和cfg原floor，自己形成

$$
t_i^{\rm SOC}
 =\max\{\tfrac14\max(v_i(x),0),\,f_{\rm curv}\}
$$

（只在原对应曲率组）。它不读取primary.targets。

故新ordinary wrapper可以修改primary提案$b$/targets，同时原same-layout SOC仍使用原真实$y$、原base/J及原RHS。Expanded-pool重建必须继续调用未加guard的原selected_model，仅用其构造原SOC上下文；不能把ordinary学习wrapper递归套给rebound。

Actual total-step质量仍由同$x$ complete model对真实$z-x$计算。原scalar SOC保留预算与complete ratio分开记录；guard不产生新的可替代ratio。

### 6.2 两次factory最终绑定

先构造旧scalar primary，加入本次guard，再调用原selected-affine及complete-affine两次factory。它们会更新primary最终签名。ordinary context、SOC_hold_model_binding以及新样本只允许在两次更新之后绑定。

Guard记录至少含：

- 原未加guard scalar signature；
- 本模型冻结learning-state及两个$\gamma$的精确binary64身份；
- model B、实际目标向量与$b$的hash；
- 改动原ID列表/数量、最大增量及保持不变数组hash；
- 加guard后的scalar signature与两factory最终signature。

旧键名radius_independent_model_sha256仍由冻结调用链读取，但本次新增target依赖$B^2$。必须明确记录该guarded signature是**含B的完整模型身份**；不能据旧键名授原radius_mapped_witness的半径无关证明。新wrapper将B与targets纳入签名，不允许跨B误认同一模型。原实际controller不调用该witness，仍按原真实门更新。

Norm bank的context只依原coordinate/reference/factorization/grid/epsilon；source cfg与这些对象均不改变。新primary签名不豁免375-entry原bank完整hash核验，也不允许reanchor。

## 7. 当前checkpoint与两个已付训练样本

唯一新继续点为本轮真实future checkpoint；仍消费24份原完成输入作为其必要依赖，不将它们重跑成新科学：

- bank375及原有序context/hash；
- coarse4432/fine4451完整原池、版本和顺序；
- $B=.00025$，legacy/covered均0；
- 原reference163、独立159/物理163和source cfg完全恢复。

初始训练样本只来自source模型2、6各自trial0。$x$取stage.accepted_iterates中对应linearized_at_accepted_index，$y$取trial的原exact159记录。使用已付日志的group8完整诊断，不恢复原J，不重算原geometry，不重解旧primary或旧SOC。

固定构造参数：

- initial_bank_context、initial_bank_entries；
- expected_initial_bank_state_sha256、expected_initial_bank_entries=375；
- curvature_defect_guard_policy=POLICY；
- initial_curvature_defect_samples；
- initial_direction_records为空。

每个sample采用以下小结构；不携带完整旧LP payload：

    {
      "schema": POLICY + "-paid-first-primary-sample",
      "source": {
        "run_id": "...", "job_id": "...", "source_sha": "...",
        "log_sha256": "...", "complete_record_sha256": "..."
      },
      "source_model": {
        "number": 2 or 6, "trust_before_model": ...,
        "linearized_at_accepted_index": ...,
        "linearized_at_physical_sha256": "...",
        "SOC_hold_model_binding": { ... original ... }
      },
      "source_trial": {
        "kind": "...", "alpha_exact": "1",
        "physical_state_sha256": "...",
        "exact_binary64_independent_coordinates": [ ... ],
        "curvature_nonlinear_defect_diagnostic": { ... original ... }
      },
      "source_base_point": {
        "accepted_index": ...,
        "physical_state_sha256": "...",
        "exact_binary64_independent_coordinates": [ ... ]
      },
      "source_final_factory_context": { ... original ordinary_covered_context ... }
    }

旧SOC_hold_model_binding与旧ordinary_covered_context.final_model_binding必须原样相等。历史原signature保留为来源，不能强行要求它等于本次新增policy metadata下的新signature。map/width/subspace/coordinate/source cfg及网格等不变定义仍与当前实现逐项核同；历史原行mapping与versions则必须在该样本的旧SOC binding和旧ordinary context之间准确一致。旧池/旧selected行序不要求等于本轮已初始化的新池/新行序，不能误拒合法的fine新增池，也不能把旧行观测冒充新中心的行级误差界。不能借“新schema”跳过这些来源核验。

新core可用原$M$/width对已存exact$x,y$计算$b_s$；这是新输入映射，非旧科学恢复。它不能凭当前状态或LP名义step猜旧$x,y$。

## 8. 最小新增代码与责任

所有旧135份Python源码冻结不改。新增独立5文件：

1. frame_metric_curvature_defect_guard.py：两桶状态、已付sample解码与绑定、pending/commit、guarded primary wrapper、375-entry直接constructor、snapshot和观察账。
2. frame_metric_curvature_defect_guard_recovery.py：显式复用原outer控制链；只接ordinary wrapper、first-trial观察、下一模型/末点提交及新报告。原solver/SOC/learning/controllers仍import调用。
3. frame_metric_curvature_defect_guard_development.py：仅新增接口人工。
4. frame_metric_curvature_defect_guard_transfer.py：root负责唯一原log读取、原checkpoint和两sample恢复、paid source闭包核。
5. frame_metric_curvature_defect_guard_audit.py：root负责四类新入口/实际audit/输出及request/workflow。

Recovery保持原参数名与返回结构，增加独立metadata。生产恢复链不得monkeypatch冻结模块或覆盖旧tag冒旧source。新增构造人工可在局部context-manager内临时替换基础依赖以隔离新入口，退出即恢复且明确标记人工；这不修改任何冻结源码，也不进入实际恢复链。没有新增primary/SOC solve入口，也不改变共享ledger ceiling的try/finally恢复。

## 9. 仅覆盖新逻辑的开发范围

按四组组织，最终项数在源码冻结时列明，不预报通过：

1. **新RHS与身份**：原ArrayLP上仅两个网格group8所需targets/$b$变化；其他数组与原row order不变；零系数完全无数值变化；B平方缩放与最终signature有据。
2. **真实步与延迟学习**：actual$y-x$与名义$p$不同的人工例；桶取逐行差的最小值而非两个min之差；零/非有限norm不更新；pending在当前模型冻结，下一模型才见新系数。
3. **原SOC/失败范围**：同一个人工raw primary经guard前后，冻结build_correction仍给同一原SOC RHS；保zero-J不删，guard可使原LP域不可行；新wrapper没有免费unguarded重求或额外solver调用。
4. **375入口和报告**：准确ordered375 checkpoint通过新constructor而不调用旧hardcoded59入口；历史双binding、source cfg与context不匹配拒绝；direct checkpoint与两个paid sample只做新映射，不事件重放。

可调用旧人工数组构造器作为新fixture数据，不能再次调用任何旧developer_check。不运行旧20/19/26/cache组；它们只消费已付receipt与冻结源。新人工不求科学LP、不调用真实geometry/JVP或优化器。

## 10. 成本、失败与首实际读取清单

新增成本只有原数组上的hash、$M d$/范数、有限scalar学习、targets/$b$更新与记录，全部计入原时钟。没有新科学J/JVP、原全值或LP调用；复制/哈希数组并非零成本，应实记bookkeeping耗时。

每个primary需输出：

- 当前两桶系数与来源、冻结state SHA、被guard的原ID数和目标增量；
- 原floor、原targets与guarded targets的身份；原不变数组核对；
- 所有实际started LP、gap/repaired/incumbent、预算和失败路径；
- first ordinary真实$x,y,d$身份、原负缺陷、$b_s$及pending/commit；
- 原实际gate/learning/SOC/hold/covered-growth事件与全费用；
- 加guard后是否仍需SOC，若无需也只记观察，不能单次归因成普遍改进；
- 末点真实eta、kappa、完整bank/pool/controller/learning checkpoint。

若guard导致可行提案减少、LP失败或仅耗尽原预算，应如实记录。不能为等成功增加LP、active时间、value预算，不能改变曲率58/metric门，也不能用“经验保护”替代实际验收。

## 11. 静态核对来源

数学/API核对只读以下冻结源码在source 4f1365300b70831550d544df119d738b2531eff5的原文本：

- frame_metric_entry_tail_height159.py：selected_model将同一两网base/J/groups/tolerances交原build_primary。
- frame_entry_tail_height_blocks.py：原target/RHS，实际共同physical body范数，build_correction独立重建原SOC target。
- frame_metric_spectral_soc_scaling.py：curvature_trial_diagnostics使用actual state−reference_state，先缓存/同ID核对再分组，记录原负缺陷。
- frame_metric_spectral_curvature_reserve.py：原group7..10的单位、floor与“提案不是实际误差界”的既有范围。
- frame_metric_affine_spectral_model.py与frame_complete_affine_metric_oracle.py：两factory签名、repaired-rho与完整soft模型；新hard RHS仍受原最终残余检查。
- frame_metric_norm_direction_memory.py对应的已付norm-bank实现：context独立于新policy注释；旧numeric cut不能跨中心复用。
- frame_metric_covered_soft_growth.py及_recovery.py：当前真实375来源的原运行链、同模型context和所有fallback。

本设计没有执行符号程序、求积、开发检查或科学运行。它是由已观察原单位缺陷驱动的独立新proposal算法；其实际效用必须由随后唯一公开新运行判断。
