# 已付 MaxTime 方向实际验收：首次入口审源

日期：2026-11-16。本稿记录首次执行前的完整源码审阅与冻结合同，不声称新验收已经运行。

## 1. 新问题与唯一原来源

[已发表实际记录](finite-cone-first-actual-and-backend-time-limit-20261116.md)中，run 43792959676 / job 133055320913 / source c0e7336c28b8d1b1f83306e3a0781069f57c0f48 的 m27、锥调用31，以 MaxTime 返回一个有限原161向量；原返回过滤前已保存其中真正的 p159。该调用没有产生模型合格候选，没有修复，也没有实际试点。rho/norm 附属量没有保存。

本入口严格采用[已发表设计](paid-MaxTime-vector-actual-only-validation-design-20261116.md)：从原 accepted52 出发，仅用那个未试的 p159 作独立实际验收。原 MaxTime、缺失附属量和原仿射资格都不改写。不重新运行锥31，不使用剩余锥32，不生成另一个方向。

原 p159 数组 SHA 为 17605ea24e9cefa4a73410913b3287c7b0f4b5303550a38f2da0f99850a0c644；原 accepted52 的 physical SHA 为 0c03e09059cac846ec5ab6a246236c52b42d28394930aa35759953ea2ce1fc21。这些是原记录身份，没有把重构后的相近向量代替原返回向量。

## 2. 冻结入口与源闭包

| 文件 | UTF-8 字节 | SHA256 |
|---|---:|---|
| scripts/frame_metric_paid_cone_vector.py | 25807 | b8e772367d718073421a5885dbb8c97cc3725bd4a83271c8498ab35d286f4593 |
| scripts/frame_metric_paid_cone_vector_development.py | 10220 | bdb30f32999ec493a0ffa97e7aedfbb2362a4a0f359f3d78638bcbebd7028e4d |
| scripts/frame_metric_paid_cone_vector_audit.py | 41377 | 2207f9c64648551fa89a5fc5c59ea9c9974b5c216476b659478f5643ffdccba1 |
| .github/workflows/visible-paid-cone-vector.yml | 4550 | f03a31a3ae4901d333cd19a87eab920e4896fdd5c231dc5cc3a9104c80fd233b |
| computations/request-paid-cone-vector.json | 39813 | 2a75f7668fba356feb300fe618a08adabe9973f36e90504f56208211eb3cf69e |

除 workflow 外，路径均相对本课题目录。root 阅读完整 core、development、最终 audit、workflow 及 request 参数/来源，并逐字段比较源闭包。

最终 request 恰绑定 182 项：原175项逐项不变，加三个新 Python、新 workflow、冻结的旧 request 文件、已发表实际 note 和已发表设计；合计167 Python、11 workflow、3份人读 Markdown、1个旧 request JSON。原98个输入参数逐项相同。root 对七个新增绑定逐件核字节/SHA；均与最终 request 一致。旧完整 source closure 在新实际入口中仍逐文件核当前字节。

审阅期间 audit 仅增加两条原来源断言：原 finite_original161_vector 确为真，且 step 来源确为“this new cone solver vector before any return filter”。其它 core、六检查和 workflow 保持冻结。未在本地运行新检查或研究程序。

## 3. 原输入与真实末态恢复

入口只读取一次最新原 7416045 字节 job log，并核原 run/job/source/status、raw log、REQUEST、DEVELOPMENT、PRIOR_WORK_REUSED、m26、m27 和 COMPLETE 各原字节/SHA。更早日志不重新下载；原24输入按原参数一次读取，准备成本计入本次延续钟。

恢复采用最终 COMPLETE 的两个真实科学钟：
657.9451113929999 秒（新锥任务）及 1014.074931654 秒（原累计）。
不能使用较早 checkpoint 中尚未计完末过程的钟。

m26 必须实际拥有 accepted52 的同 physical SHA、完整159/163值和两网14门收据；m27 必须就在这个 accepted52 上线性化、trials/corrections 均空、唯一调用序数31且 MaxTime。缺少任一原记录即停止，没有重求或补造来源。

初始点两网值直接使用 m26 已付且身份相同的原收据，新增初始几何调用为零。最终若仍选52，继续用这些收据；若接受53，最终门只消费新试点自己的两网原收据，独立末验几何调用同样为零。两者明确标出收据拥有者，不把旧值当新计算。

保持原 g、b0、159→163 精确坐标、参数、普通场、原网格与全部门。池从4448/4543、版本13/12恢复；bank512条/8个独立支持、学习62 events/61 commits/pending0、原γ、B=.00025、双streak0/0保持真实末态。

## 4. 唯一方向、原实际门及失败边界

比例严格依次为 1、1/2、1/4、1/8、1/16、1/32。每次使用原 subspace.apply 的浮点次序；完整候选 exact159、physical163、实际位移159、原物理步长范数都在进入实际门或求值前记录。没有将数值舍入后的实际位移误当精确 alpha*p。

原精确163盒及支持不变量先保留。原粗网普通场求值后，只要实际 regularity 条件允许，按原逻辑求完整细网，即使其他粗门失败；原14门、旧metric条件及两网真实eta全部保留。

接受要求两网真实 admissible、严格eta下降，下降至少原 1e-7；只有两网同时达到原新目标时，才用已存在的目标例外允许更小的严格下降。相等不接受。新入口至多增加一个 accepted53；这种接受只表示实际原两网验收通过，没有追授原 MaxTime 的仿射或 cone 资格。

两池采用一个明确策略：调用原 value-only expand_pool / learn_fine_violations，只消费当前拥有的普通值缓存。不接受的试点若发现新行或池容量阻碍，就结束沿这一个固定方向的二分，不再用未重建模型的方向越过新约束。

不调用 J、JVP、模型装配、LP、SOC 或锥求解器。没有预测质量、曲率误差训练、covered-growth、norm-bank replay 或虚构模型附属值；bank/学习/双streak是被动继承，接受53也不冒称旧模型在53有效。

## 5. 费用连续与异常捕获

新实际值最多12次。原锥任务96次/1200秒、原累计160次/1800秒都保留，入口使用它们的交集及额外12次限制。从源54次新锥值、116次累计值继续；原31次锥和已关闭64次HiGHS不变。

continuation clock 在新原日志及24输入读取**之前**开始。全部输入准备、实际失败调用和真实超时均继续计入，不在进入几何时重置钟，也不截去一次调用造成的实际超额。

root 对父类 fine_decision 的收费边界作窄核：fine_evaluations 在 problem.geometry 前递增，finally 记录持续时间，因此新 wrapper 不再重复收费。coarse 的父类存在返回后记次边界；新 wrapper 利用真实 geometry_calls_started 对异常进行恰好一次补记，并保失败收据。没有把 fine 失败删出账本或给该方向额外预算。

异常时保已开始的 trial、求值前完整候选、最后已接受点、真实计数和时间。source读取、构造或报告阶段失败也写出实际已付状态。新 future checkpoint 明确其 value-only 身份，保原求解器捕获来源，不能继承“本入口捕获新求解器向量”等不实标签。

## 6. 仅六项新接口检查

首次 Actions 执行恰两组各三项：

1. 保存向量与延续钟：159数组/指纹恢复；长度或指纹错误在新实际值前拒绝；两个原钟继续且超额不截去。
2. 实际验收与失败记录：两网严格下降、原目标例外与接受53；失败试点发现新行即停止该方向；已收费细值异常时完整159/163候选仍在。

这些使用声明的数组假对象，没有真实几何、J/JVP、求解器或 tiny solver。原锥12项、末槽11项、几何9项检查仅消费原已付收据，全部不重执行。六项新检查不是旧几何测试的重包装。

## 7. 实际拉取与输出合同

workflow 在任何新开发/科学执行之前，通过原 read_original_actions_log.py 做真实公开和私有 partial-clone/pull，输出每次根/题 README diff 与提交号，并验证私有 QUEUE 的本会话进行中。若 README 不匹配则立即停止新计算，root 只读变化并执行新规矩。随后恢复本次冻结 source commit，核全部绑定。

workflow 使用原固定 Python 3.12.14、numpy2.3.5、scipy1.17.0、clarabel0.11.1；安装依赖不表示调用求解器。PAT 不写源码、文件、request 或 API；私有读规则用已有 runner secret，之后删除该环境值。

本入口只写 runner 临时报告并以 PAID_CONE_VECTOR_* 原 stdout 输出。原完整日志、物理数组、checkpoint 和新报告 payload 不入 Git、artifact、Release 或缓存。20分钟 job 上限只是平台保护，不替换原1200/1800科学钟。

源码与本审源结论完成后连同唯一 request 发布。实际结果必须随后从原 Actions 输出读取并单独记账；无论接受、拒绝、发现新行或预算停止，都不推断驻点、不可行或不存在其它方向。主课题全几何完成门保持未付。
