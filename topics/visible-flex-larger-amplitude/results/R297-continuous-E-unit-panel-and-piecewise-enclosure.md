# R297：原冻结连续模型 C 的单位面板六积分与完整分支包含

作者：AI（geometry）。日期：2026-11-15。分类：**变量代换、区间包含与误差判据已证明；新实现只完成源码检查，尚无 request136 实际数值结果。**

## 1. 实际132与诊断边界

request132 的 run 为 43702946191，源码提交为 185e4f3eb798fbca5fabab8ca928741cb4cd6446。原生产器 geometry_20261115_stored_continuous_E_cover.py 为66415 bytes，SHA-256：

9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed。

完整原事实见 [R293](R293-actual132-continuous-E-panel-budget-and-unpaid-whole-domain.md)。实际 integral_panels=200000、inverse_cover_nodes=0、rigorous_analytic_component_integrals=1103610；1378个原piece已完成，原piece1378（cell6、segment1）尚有闭面板未付，随后1379–1439的完整suffix未执行。首个未付闭区间为

$$
\left[\frac{126450279677349}{140737488355328},
      \frac{63225139838675}{70368744177664}\right],
\qquad \mathrm{depth}=47.
$$

自然外半径、有限头六积分和whole-domain查询都未形成；原结果诚实报告partial。保存的小摘要未包含每个accepted panel的analytic_fallback_reason、cap分支及恢复宽度，不能从它断言一个确定cap接口、$w_x=0$或参数不确定性就是唯一原因。

源码能直接确定两件事：

1. QueryCover尚未运行，所以value_width_bits=24的径向查询细分目标不是本次停滞触发条件。执行停在有限头六积分工作精度判据。
2. 原analytic_integrals将被积函数除以幅度$M$，在原面板$[a,b]$上仍传固定abs_tol=$\epsilon_A$；外层却要求恢复积分的全宽不超过$\epsilon_A(b-a)+\epsilon_R|I|_{\rm upper}$。内部绝对容差未按$M$和面板长度传递。它还要求整个实面板先确定唯一cap分支和$q=w_x$符号，才调用Acb。

这是可独立修正的实现限制，不是对132每个面板作出的唯一数值根因判定。本次不提高原200000面板、1800秒或任何模型精度预算。实际效果必须由136原结果回答。

## 2. 独立源与同一个数学对象

新入口：[geometry_20261115_stored_continuous_E_cover_v2.py](../computations/geometry_20261115_stored_continuous_E_cover_v2.py)，77697 bytes，SHA-256：

004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea。

原9aa0源不改。新源要求同目录保留原文件并核原SHA，绑定和结果分别记录新source_sha256与preserved_original_producer_source。新输出schema为R286-original-stored-convention-C-continuous-E-cover-v2，不冒原v1生产者。

目标仍为[R286](R286-original-stored-continuous-integral-and-metric-bridge.md)明确约定C下的同一连续对象族；MODEL_SCHEMA仍为R286-original-stored-continuous-model-convention-C-v1。没有另选连续模型，没有改变frozen binary参数的准确实数含义，没有把旧48步selector有限输出认证为这个连续模型的解。

中断前版本已实际完成纯AST/compile检查：68个原定义AST完全相同，包括全部Piece、ContinuousHead、Jet2、QueryCover方法，以及build_head、finite_join_conditions、parse_queries和原goal_met。六个原定义改动涉及生产者身份、积分策略、诊断或参数入口；新增四个helper。没有import生产器/flint或运行科学。随后本版仅删除新增helper中的点值q==0短路，原68定义未动；末一行文本修正尚未在本地重跑AST，由Actions原前置compile核最终完整源。

完整160×9顺序、原shallow $R_n,\alpha_n$、原cut/cuff/cap/flat/valley/正权重和覆写顺序、所有深层$n\ge160$准确原根族、原warp参数/曲率参数、全六primitive、finite/protected join、真实积分产生的自然$R_{\rm out}$、全闭query和未付suffix全部保留。

自然外端不能换成nominal binary cut，也不能按$E=1$向外平延拓。它与内cuff的区别见[R294](R294-nine450-exact-C2-seams-and-target-atlas.md)。本次没有实际接受field，没有新的nonlinear/RHS/J/ODE，不支付相对metric的$10^{-6}$门。

## 3. 保留的六个函数

在原piece坐标$x\in[0,1]$上，记

$$
w=e^{g(x)}>0,\qquad E=1+w^2,\qquad q=w_x,\qquad
r_x=\ell r_o/\sqrt{12}.
$$

$g$是原完整cap/flat/valley/cut覆写后的log-profile；$\ell$是同一原piece的实长度。$\chi,j_0,\omega$保持原protected/cut过渡、端口尺度和正权重。原六函数为

$$
A=r_xj_0(1-\chi)+\frac{\chi|q|}{K E^{3/2}},
\qquad B=\frac{\chi r_x\omega}{E},
$$

$$
(f_0,f_1,f_2,f_3,f_4,f_5)
=(A,B,\sqrt E A,\sqrt E B,wA,wB).
$$

新代码没有以未cap的profile替代真实profile，没有清零任何primitive，也没有只计算两个径向积分。六组件可分别求包围，但均是同一完整原函数定义的真实积分；独立区间损失相关性只会扩大包含范围。

## 4. 单位面板变换与原全宽目标

固定闭面板$[a,b]$，$\Delta=b-a>0$。由原Piece.range得到$f_k$在完整面板上的有效区间$F_k$。若$F_k=\{0\}$，积分准确为零；否则取

$$
M_k=\max\{|\inf F_k|,|\sup F_k|\}>0.
$$

这是包围端点产生的计算尺度，不是物理参数。定义

$$
J_k=\int_0^1\frac{f_k(a+\Delta t)}{M_k}\,dt.
$$

准确变量代换给出

$$
I_k=\int_a^b f_k(x)\,dx=\Delta M_kJ_k. \tag{1}
$$

回调和恢复乘法均用完整Arb/Acb包围，不取中点。本次dyadic面板端点在256-bit精度下可以准确表示；如果将来某些有理端点需包围，仍必须把该区间传播包含在回调及恢复中，不声称只有最终乘法的舍入。

原外层工作目标完全不变。对恢复积分区间$\mathcal I_k$检查

$$
\operatorname{wid}(\mathcal I_k)
\le
\epsilon_A\Delta+
\epsilon_R\max\{|\inf\mathcal I_k|,|\sup\mathcal I_k|\},
\quad
\epsilon_A=2^{-96},\quad\epsilon_R=2^{-80}. \tag{2}
$$

这里wid是整个上下端点之差，**不是Arb的radius**。

### 4.1 内部容差不等于误差证书

新Acb调用固定积分区间$[0,1]$，请求

$$
\mathrm{abs\_tol}=\frac{\epsilon_A}{2^gM_k},
\qquad
\mathrm{rel\_tol}=\frac{\epsilon_R}{2^g},
\qquad g=8. \tag{3}
$$

若规范化积分误差半径为$r_k$且$\Delta,M_k$准确固定，恢复半径为$\Delta M_kr_k$，恢复全宽为$2\Delta M_kr_k$。例如假设某个有效半径界满足

$$
r_k\le2^{-g}(\epsilon_A/M_k+\epsilon_R|J_k|),
$$

则准确恢复所产生的全宽至多

$$
2^{1-g}(\epsilon_A\Delta+\epsilon_R|I_k|).
$$

这只解释式(3)的单位与工作余量，**不证明实际Acb返回必满足该假设，也不证明$g=8$本身足够**。Acb内部目标会受子区间累加、舍入和输入区间传播影响；官方文档明确总误差可能超过所请求目标。因此代码只依据真正恢复后的有向上下界重新检验式(2)。如果恢复乘法存在区间/舍入误差，$\mathcal I_k$已经包括它。

相对项也不直接从Acb内部估计复制为最终误差；原goal_met由当前完整积分上下界重新形成。新参数analytic_guard_bits只是内部工作余量，不修改原目标或任何科学验收标准。

### 4.2 保守交集、逐组件回退、闭覆盖

原实区间同时给出$I_k\in\Delta F_k$。因此$\mathcal I_k\cap\Delta F_k$仍包含真实$I_k$。单个Acb组件没有有限实包围时，代码保留该组件的$\Delta F_k$，同时保留其他组件已经得到的有效包围；不丢弃任何primitive。

每个子面板区间都包含其真实积分，区间和便包含完整面板积分。相邻闭端点重合是零测度，不产生遗漏或重复的正测度贡献。原二分/max_depth/资源栈保持：达到最大深度的有限粗界可以保留为合法包围，work_width_goal_met必须false；若资源中断，完整pending stack、未访问source/query后缀继续保存，不制造完整外半径。

式(2)逐面板逐组件检查，不是一个未经证明的全模型$10^{-6}$承诺。六个函数非负，但本实现没有借非负性跳过任何组件或条件。

## 5. 全分支Acb回调

### 5.1 原全面板唯一分支与符号已证

若原analytic_kind确认整个实面板上唯一cap分支及$q$符号，直接复用原Piece.expression，只改输入变量和请求容差。一个在被积实面板上等于真实函数的解析延拓足够用于椭圆误差界；不要求该延拓在面板外的实轴上仍等于全局分段定义。开方仍传递analytic标志。

### 5.2 cap分支已证、$q$符号未证

$B,\sqrt E B,wB$不含$|q|$，不应被不相关的$q$符号判定阻塞。其余三组件使用q.real_abs(analytic=analytic)，即实变量绝对值的分段复解析延拓，**不用复模长abs(q)**。

analytic=True且球跨非解析部位时，返回非有限值，解析Gauss规则不能使用该椭圆。analytic=False时，回调必须包含完整闭实面板及零点。某个退化输入球上点值$q=0$不证明局部恒零，新分支回调因此始终调用real_abs(analytic=analytic)。只有原analytic_kind已在整个正宽实面板证明符号为0时，才沿用原全面板恒零的解析延拓；不能由一个点值绕过非解析检查。

### 5.3 cap分支也未证

令$z=\log w_{\rm raw}-\log w_{\rm cap}$，$L>0$为原capTransition。保持raw、transition-low、transition-high、cap四段及所有flat/cut后覆写。通过Acb球上$\Re z$的区间保留所有可能原分支。

- analytic=True且可能分支不唯一时，返回非有限球；有限hull不能假充解析性。
- analytic=False时，逐可能分支评价并取完整复区间hull，包含每个真实实点的分支与全部边界。
- 原full-flat覆写和最终cut-preserving raw覆写照原顺序使用；不是新增数学shortcut。

唯一分支内的多项式、指数、原常数和按analytic检查的开方构成正确解析延拓。多分支面板由Acb在内部适应细分，并在跨界小片保留直接区间积分；任何窄cap/cusp strip均未删除，也不要求数值恰好命中零根。

### 5.4 包含定理

固定约定C中任一允许的实际参数/根选择。所有参数区间包含其真实常数。analytic=False的候选集合覆盖该真实函数的全部可能分支，各候选表达式的区间包含对应真实值，所以hull仍包含真实函数。analytic=True只在经过确认的解析延拓上返回有限包围；不能确认时拒绝解析调用。正确的Acb积分包含、式(1)恢复、与实区间交集以及闭子面板区间相加依次保持包含。

因此，若完整原source和查询完成，新结果包围的是**同一R286连续模型族**的六积分和$E$，不是另一目标度量。结论不保证有限工作预算一定完成，也不保证固定精度的参数包围能靠空间二分无限缩窄；这些情况按粗合法界/工作精度未付或resource-partial明确报告。

## 6. 官方primary接口与可核范围

仅阅读官方文档，没有本地import/运行flint：

- python-flint 0.9.0，acb.integral与analytic回调：<https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral>
- 同版acb.real_abs：<https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.real_abs>
- 同版acb.sqrt与acb.union：<https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.sqrt>
- FLINT acb_calc_integrate的有效包含、内部目标/累计误差与资源截停：<https://flintlib.org/doc/acb_calc/integrate.html>
- Fredrik Johansson, Numerical integration in arbitrary-precision ball arithmetic, 2018, arXiv:1802.07942：<https://arxiv.org/abs/1802.07942>。

文档对内部error的说明不替代式(2)。本次实际Python接口仍锁python-flint==0.9.0。任何科学数值都只在Rogerhu12/math-research-public的Actions执行。

## 7. CLI与输出身份

完整CLI：

    python geometry_20261115_stored_continuous_E_cover_v2.py
      --config ORIGINAL_CONFIG --config-sha256 ACTUAL_CONFIG_SHA
      --ledger-ready ORIGINAL_LEDGER --ledger-ready-sha256 ACTUAL_LEDGER_SHA
      --stored-ready ORIGINAL_STORED --stored-ready-sha256 ACTUAL_STORED_SHA
      --runtime-computations CHECKOUT_COMPUTATIONS
      --source-topic RESTORED_ORIGINAL_SOURCE_TOPIC
      --proof R286_ORIGINAL_PROOF
      --queries ORIGINAL_QUERY --queries-sha256 ACTUAL_QUERY_SHA
      --deep-definition original-exact-root-family
      --precision-bits 256
      --integral-absolute-bits 96 --integral-relative-bits 80
      --analytic-guard-bits 8 --integral-evaluation-limit 100000
      --value-width-bits 24 --max-depth 48 --query-depth 12
      --max-panels 200000 --max-query-nodes 200000
      --budget-seconds 1800 --out NEW_REQUEST_OWNED_DIRECTORY

结果路径仍为result.json、input-binding.json、query-plan.json、query-results.json及原四个complete journal。源和查询结果schema前缀改cover-v2；外部query输入schema仍为原R286-original-stored-convention-C-closed-queries-v1。

| 新字段 | 准确含义 |
|---|---|
| preserved_original_producer_source | 9aa0原文件的实际name/bytes/SHA |
| integral_strategy | 单位面板规范化和完整piecewise回调身份 |
| original_six_full_width_goal_unchanged | 原goal_met没有改变 |
| original_real_profile_and_model_C_unchanged | 本次不改变模型定义 |
| integration_diagnostics.counts | 实际分支/组件调用、回退、恢复目标和粗界计数 |
| integration_diagnostics.last_attempted_panel | 实际最后面板及六项完整宽度、目标、请求容差 |
| guard_bits_alone_are_not_an_error_certificate | 内部guard不能证明完成 |

最后attempted panel可能与unpaid ledger中第一个pending panel不同，不能混称。legacy_gate_bypassed_for_cap或derivative_sign仅表示当前区间分类，不能报告为已确定的物理根因。最后面板只是诊断；全未访问范围依旧在完整原ledger，不以一个样本替代。

numerical_work_resolution_complete、full_finite_head_complete及continuous_convention_C_query_enclosures_complete三种责任分开。有限粗界可真实完成包含而未达工作宽度；内部tol达到也不替代恢复检查。全source未完成时不填自然$R_{\rm out}$或whole-domain $E$。

只认原9aa0/v1的下游metric绑定器不会因同模型schema自动接受v2。未来若消费真实v2结果，须明确增加该新生产者及完整输出身份；不覆写旧source、不修改原metric门。当前没有实际场/新query结果，不预填任何接受值。

## 8. Request136直接执行与保留策略

复用原132三件配置/ready、R286、九个原公式source和同一份whole-natural-domain query。历史输入从8bd267107cc8710d371f3b62c02986655ac965b0恢复；原public78源码照旧恢复一次。无需取132巨ledger或增加fixture。

新请求保原8个入口/运行依赖，再加本v2，共9项pin。唯一shared触发仍为computations/public-original-stored-continuous-E-request.json，workflow仍为.github/workflows/visible-larger-public-stored-continuous-E.yml。owned临时命名空间改136。原预算保持science45分钟/job65分钟、内部1800秒。真实rules-sync parent保原pull/rebase/README变化处理，科学child移除GitHub token。

raw配置、六积分/径向/query/未付journal均只保于request-owned临时目录；原scalar读回后always清理。没有artifact/Release/Git raw上传。stdout保完整小结果及SHA、实际未付分类/第一问题/所有未访问suffix和规则同步原结果。metadata超限及执行异常诚实失败，不截删科学事实。

初稿在环境中断前已完成AST/compile与68个原定义对照，随后按公开9aa0+四组已付patch恢复原668fb695身份，再作本文件明确的一行q==0修正，形成上列新身份。136接线文本的语法检查如果未在本地实际执行，另在交付记录明确；不得冒已运行。没有本地积分、根、区间求值或未来run/成功值。
