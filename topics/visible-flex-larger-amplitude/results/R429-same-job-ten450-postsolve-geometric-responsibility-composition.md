# R429：同一真实 450 初场的完整几何责任组合与原临时现场接线

AI 辅助推导及源码记录；2026-11-15。本文证明一个带明确前提的组合命题，并给出不改变既有求解器的可执行编排。它不报告任何新的科学运行、不假定已经得到 accepted450，也不选择 $K$、$\tau$、$\eta$、帽数据或未来 run。

## 1. 要连接的三个不同对象

首先区分三个层次，避免由有限 BVP 接受跳到连续几何结论。

1. **原有限 native／full-DN 对象。** 原 193 入口先在七个 shape 坐标冻结、三个 active 坐标活动的 453 维问题上执行原全部门；随后在该真实末十词处重新形成零 active、零固定低阶目标行的完整 450 维问题，再付其本身的 RHS、当前 $H$、FD、338×112 响应和最终 audit。453 接受只给450种子。
2. **R409 的新明确场。** 对真正450 checkpoint保留的完整状态、两 mean、实际 geometry 和原 source，额外执行原全576段／全部真实子步的226态径向与物理读出。全节点数据随后按原 R409 程序生成共享背景和 Hermite／Fourier 明确场。这个场以实际有限数据为系数；它不因数据来自 accepted450 就变成已证准确连续 ODE 轨道。
3. **R416 的准确 cut 场及 R417 的完整帽。** 几何消费者在 R409 七元组上用同一准确十族 target 和原 C 根族构造独立 R416 cut patch，并接 R417 全部固定帽。R418 和 R422 评价的是这个有明确表达式的场族。它们不把旧 R409 renderer、旧有限求解器的接受或单纯 source SHA 重新标成当前几何接受。

记真正 checkpoint 的十个 binary64 词为 $p=(p_1,\ldots,p_{10})$，每个词按自己的准确 dyadic 值解释；记与之绑定的原 C 输入及允许根族为 $\mathcal C$。给定真实全节点系数 $\mathcal A$、原 cuff、声明的 cut 宽度 $W$、帽高度 $H$ 和完整 marker 列表 $\mathcal M$，写

$$
F_{\mathcal A,p,C,W,H,\mathcal M},\qquad
g_{p,C,\mathcal M},\qquad C\in\mathcal C .
$$

这里的记号只指上述冻结程序定义的对象，未引入新的连续重构、额外 root 选择、几何配准或参数调优。

## 2. 原450责任不能由“删三行”取代

原 driver 的成功分支实际上执行下列责任链：

- 原 design453 main 返回0且其原 `new_coupled_finite_acceptance` 为 true；
- writer 从该次实际 flow、boundary、separated、原 raw client 和完整五类结果形成453 checkpoint；
- `prepare_frozen` 读取该 checkpoint 的全十词，冻结在真实末状态上，调用 `fresh450_seed`。这里仅形成新初猜，完整新450 RHS和原preflight仍实际求值；
- 第二次 `run_phase` 执行原当前 $H$、原五cut比较、原FD和完整main；只在本次原接受后产生450 checkpoint；
- 两阶段 lease 均释放，唯一 raw owner 在 driver `finally` 中关闭；launcher 实际观察其进程组静止。

新编排只消费这个既有成功分支。它逐字绑定 launcher／driver 来源、当前run／science commit、原 adapter receipt、checkpoint receipt、两阶段十词及 `actual_dimension=450`、$k=K_0=0$ 等来源字段。它不再以更弱残差或新的 tolerance 判断 field 接受。

**命题 1。** 假设原193 source及其各原消费者按已声明合同正确执行，且这些字节／来源匹配成立。新编排把450输入交给R409时，该输入是本次真实独立450的输出，而不是453数组删行后的重标对象。

**证明。** 实际 checkpoint 只能从原第二次 `run_phase` 的原main成功分支产生；原 writer 同时绑定本次未注解 fullDN、当前FD、FD anchor、最终 native 和 physical cut audit。新编排要求两阶段真实返回，且目标 checkpoint 的原writer／driver、维数和零active状态吻合。最终对象的每个字段由本次原receipt追到对应临时文件，不能由调用者另给一个接受布尔量替换。因此结论是来源与控制流的组合，不是额外数值门。$\square$

它仍不证明该有限解等于准确无限维 DN 解；这个限制与 R400 一致。

## 3. 七元组、原 cuff 与同一帽的具体连接

R409 的原加载器实际返回

$$
(\text{paths},\text{plan},\text{assembly},\text{target},
  \text{saved},A,\text{bindings}),
$$

不能用旧675活动片对象或另一 background 冒充这个七元组。R413 从同一个真实 checkpoint 和原 C 绑定中取得原 cuff **word**；它不另选 cuff，也不把新的内平环半径改称原自然边界。

原 `R413.prepare` 先产生两件独立真实输出：

- `r409-original-cuff-plan.json`；
- `original-cuff-target-atlas.json`。

R409 shared prepare 消费第一件；后来的 R416/R417 消费第二件并调用原 `bind_loaded_shared_bundle`。因此实际可执行顺序应为：

$$
\text{真实450}
\longrightarrow
\begin{cases}
\text{R409全径向读出},\\
\text{R413原cuff计划／atlas}
\end{cases}
\longrightarrow
\text{R409共享场}.
$$

本次编排顺次执行两个独立前件以保持简单的所有权和预算；没有把“先运行哪一个”冒成数学依赖。

对每一帽侧 $\sigma\in\{+1,-1\}$，严格采用 R409／R417 的同一个图

$$
F_\sigma(x,y)=
\bigl(x,y,\sigma(H+b_\sigma(x,y))\bigr),\qquad
b_\sigma=\sum_{i\in\mathcal M_\sigma}
 A_i\left(1-\frac{|(x,y)-c_i|^2}{R_i^2}\right)_+^4 .
$$

相应定向法向可以写为

$$
n_\sigma=
\frac{(-b_{\sigma,x},-b_{\sigma,y},\sigma)}
{\sqrt{1+|\nabla b_\sigma|^2}}.
$$

所有重叠 marker 在求度量、曲率或法向球以前全部相加；负 $A_i$ 不删除。其拉回度量为

$$
I+\nabla b_\sigma\otimes\nabla b_\sigma,
$$

和 R413/R417 的帽 target 完全同一个表达式。R418 对完整帽的 metric=0 责任来自这个图恒等式及完整marker／side／cuff绑定；它不谎称已经扫过帽的所有 Cartesian 区间格。R422 则独立付其真正所需的完整帽 cover／六jet／曲率／法向／pair责任。

**命题 2。** 如果上述真实 plan、atlas、全十词和七元组绑定成立，则 R418 与 R422 所使用的帽、原 cuff、完整共享系数和准确 cut target 的语义定义一致；程序加载时不同的模块对象或 interval 工作精度不构成另一个数学 target。

**证明。** plan 的 checkpoint、cuff、$W$、$H$ 和完整marker字段由 R413 对实际七元组逐字段绑定。R416 从同一 target DAG、原 C 根族和同一 finite 系数定义准确 cut 部分；R417 依据实际 $A$ 所属已核模块进行绑定，不靠另一次同路径加载产生的不同 Python 类来改对象。改变工作精度只改变有向 enclosure 的形成精度，不允许修改上述参数、公式和来源。故是同一个绑定场族。这里不宣称不同消费者形成的 enclosure 文件或中间数组逐字相等。$\square$

## 4. metric 与 reach 是平行责任，不是彼此新增门

令 $M$ 为 R418 按其原完整闭域分割、原四个 Loewner 检验和全部 target 责任得到的数学结论。其通过时，对它所绑定的所有点、允许相位及同一 C 根族成员成立

$$
(1-\eta)g(v,v)
\leq \langle dF(v),dF(v)\rangle
\leq (1+\eta)g(v,v).
$$

这里 $\eta$ 必须是显式提出并真实传给原消费者的准确文本；新编排既不选择它，也不根据结果放大它。

令 $R$ 为 R422 原完整 curvature、AA／CC／AC 全pair、全部空间／相位分割及原 $K,\tau$ 责任付清后的结论。按 R422 原证明，在其全部前提成立时得到对应准确场的 embedding／reach 结论；原 `README_reach_fraction_paid` 还分别保留全像直径 $D$ 的责任和原 $\tau\geq3D/100$ 条件，不把部分采样直径冒成全像 $D$。

**命题 3（同场组合）。** 在命题2的同一语义场族前提下，如果原 M 与原 R 都付清，它们可同时用于同一个 $F_{\mathcal A,p,C,W,H,\mathcal M}$，无需再引入一个数值通过门证明“两者属于同一个场”。反之，M 未解、资源停止或计算错误本身不使原 R 的输入对象失效。

**证明。** 两个消费者只共享已完成的原 shared field／atlas／checkpoint，分别执行各自原范围与预算。命题2已经给出对象相同；两类结论的合取因此只需各自原前提，不需把 M 的通过当成 R 可执行的前提。新编排也据此在 shared field 形成以后独立调用 reach，即使 metric 返回 unresolved、partial、error 或自己的stdout超限。除非 owner 尚未静止、显式总体资源已经耗尽或遭外部终止，不以 metric 结果阻止 reach。$\square$

这项逻辑不把未完成的 cell/pair 从责任中删掉。所有原未访suffix、当前frontier和失败仍在原临时结果中；必要摘要只选择其来源、计数与责任范围，不声称逐值返回完整大表。

## 5. 为什么要保留原 C 目录

R418 当前固定接口实际需要本次原 C 的四件真实输出：

- `result.json`；
- `input-binding.json`；
- `query-plan.json`；
- `query-results.json`。

它们必须是当前 checkpoint／geometry 已消费的实际对象，不是另一次相同公式计算所产生但未经绑定的新盒子。

R426 的后续同 C 按需 query 还需要同目录原 source 数据：

- `large-arrays/complete-source-radial-panels.jsonl`；
- `large-arrays/source-piece-index.json`。

当前编排不调用尚未接入的R426，不借其未来能力宣称 fixed-C 盒可以任意细化。它记录两件额外 source payload 是否实际仍存在并保持它们；如果缺失，就如实标记，不能拿旧SHA代替内容。额外两个payload是否存在不成为当前原R418固定接口的新科学门。

原193 driver自身不删除这些数据；它的 `finally` 只关闭真实owner并写原status。原workflow最终清理才删除整个本次namespace。因此未来接线须把postsolve放在这次最终清理以前，完整原C目录保留到所有已接入消费者及必要读回完成。无需复制旧大数据，也无需重新付一次C。

## 6. 全局钟与过程所有权的条件不等于数学通过

“原namespace截止时间”的来源须同时绑定原launcher的 `actual_job_deadline` receipt：当前读取文件的bytes／SHA逐字一致，再核schema、run、source和原recipe。仅同job、同recipe但重写start或预算的另一份文件不满足此前提。

声明的各阶段资源上限记为 $b_i>0$，原namespace绝对science截止时间为 $T$，原postsolve shutdown reserve 为 $q>0$。阶段开始时只可使用

$$
b_i^{\rm actual}=
\min\{b_i,T-t_{\rm start}-q\}.
$$

如果右侧非正，记录该阶段未启动；不能重新设一个完整 $b_i$ 钟来延长原请求。若有资源，原消费者收到实际 $b_i^{\rm actual}$；独立owner只向自己实际创建、PID和start-time均吻合的进程发送停止信号，完成wait/reap并记录是否静止。

这只是程序资源政策，不是操作系统精确到零延迟的实时保证；实际启动、停止、残余进程和耗时都必须由本次结果报告。进程不静止时，不读取可能仍在写入的科学结果，也不删除其现场。

资源不足、original CLI错误与数学 unresolved 三者保留不同字段。未获得完整输入时，下游未访后缀逐阶段保留。原BVP/native/scientific source不因这些过程状态而被赋予接受或拒绝。

## 7. 单份必要结论与正确清理

新reader只用标准库读取封闭后的原JSON／文件／过程元数据；不导入科学模块、重求最小值或重算曲率。

必要结论保留：

- 真实upstream两阶段来源、原接受状态、全十词、checkpoint／geometry／C身份；
- 五个阶段全部启动／停止／未访行、真实资源和错误；
- 原径向节点／root／RK实际计数、shared场形成标志；
- 原metric各全域flags、原 $\eta$、计数、scope及真实pending的必要范围；
- 原reach全闭域／pair flags、原 $K,\tau$、计数、原直径／reach条件、未付责任；
- 全部原结果和大ledger的字节身份；大frontier只身份／条数并明确没有逐值传回；
- 每阶段stderr最多一个明确原字节范围的必要文本片段；全文件SHA另保。非UTF8显示替换和未显示范围均明确，不用编码拼装运输原数据。

输出只有一份不超过90000B的JSON。超过上限时，只返回诚实的小错误身份，不分片、压缩编码或删字段假称完整，也不授权清理。

若 reader完成且观察所有实际owner静止，它只支付**新增postsolve必要读回条件**。原193自己的必要读回条件仍要分别支付。最终workflow必须把两者与原owner静止条件合取以后才能清理整个namespace。新两个源本身从不删除、上传或保存可重算raw。

## 8. 原transport错误不能改造成新数学门

R413原CLI存在一个明确分支：真实 `completed=true`、计划／atlas／result均已写出，但独立stdout摘要太大，返回70。同job下一消费者直接消费已核的原文件，不依赖该stdout正文。

新编排只对这个**已由冻结R413控制流证明的特定分支**，允许完整计划继续被原R409消费，同时保留70和summary-overflow状态；它不把任意非零退出解释为成功。其余producer仍需真实原完成结果、静止和原依赖。原metric自己的stdout超限也不阻独立reach；最终单份必要读回仍需如实说明实际scope。

这既不放宽原科学判定，也避免把一个不改变原对象的运输失败附加为科学接受门。

## 9. 仍然未付及实际参数缺口

当前两源码只给完整可执行接口，没有请求号、未来run或预填参数。真正运行仍需明确给出：

- 本次原450 checkpoint能够产生的上游输入和同job路径；
- $W,H$ 及完整marker列表；原cuff由R413真实取得；
- 准确文本 $\eta,K,\tau$；
- metric／reach的显式覆盖深度、节点上限、工作精度；
- 五阶段资源预算、储存reserve与原namespace的真实剩余时间。

没有选这些值，不等于需要用户额外审批；只是不能把尚未指定的实验参数伪装成已有事实。

R425 held-set、全像Hausdorff保持、含反射Euclidean非同余／$\delta_E$仍未接入；R426按需C精化仍未接入；same-$g$网格／谱精化和原准确轨道误差仍各按其原责任。即使本次未来metric与reach均通过，也不由这个编排直接宣布课题完成。

## 10. 源与既有结论

新增两件源码：

- `geometry_20261115_current_C_ten450_postsolve_geometry.py`：独立过程编排；只调用冻结原CLI，不定义新的科学公式。
- `root_20261115_current_C_ten450_postsolve_necessary.py`：单份必要元数据；不执行科学、不清理raw。

来源及理论责任分别见：

- [R400](R400-current-continuous-ten-frozen450-and-complete-prefix-metric-binding.md)：真实profile／checkpoint及完整450责任；
- [R409](R409-current-continuous-ten450-full-radial-shared-background-and-seam-construction.md)：全径向共享场；
- [R413](R413-original-C-cuff-word-and-fixed-cap-target-atlas-binding.md)：原cuff和帽target atlas；
- [R416](R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md)：准确cut场；
- [R417](R417-current-ten450-fixed-cap-six-jets-curvature-and-normal-balls.md)：完整帽六jet／曲率／法向；
- [R418](R418-current-C-complete-closed-relative-metric-source-interface.md)：同一准确全场相对metric；
- [R422](R422-current-C-closed-pair-universe-and-reach-binding.md)：完整AA／CC／AC和reach。

这些是条件定理及源接口的组合。本文没有执行任何实际区间、全域metric、reach、held或后继BVP科学计算。
