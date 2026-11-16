# 已付末模型四 attainer 的新支持与最后一个 LP 名额

日期：2026-11-16。状态：仅源码与纸面合同；没有执行开发、几何、J/JVP、LP 或科学。根统一发布和公开 Actions 调度。本稿不修改任何旧源，不重启已关闭 epoch，也不增加当前独立任务的资源上限。

## 1. 具体证据与本次唯一改动

原 direct-reference 独立任务 run43780594182 / job133016656592 / source a0d71ea94446f0fcf64d1f69e4dbadd5910204ba 已完成：

- 累计科学 257.595331213 s，58 个共享真实 value。
- 62 primary + 1 SOC = 63/64 个已启动 LP。
- 第28模型位于第27个接受点，$B=0.00025$；原两网各14门通过。
- 该模型只获一次 primary LP。HiGHS status0/success，松弛改善为正；完整 affine slack 的修复改善为负，gap约 $2.8959\times10^{-5}$ 大于原 $10^{-9}$ 容差。
- 原 solver 在达到 scoped ceiling 后先退出，未加入下一轮 separation cuts。MODEL28 的一个完整 oracle 方向仍保留四个实际 attainer。
- 原 MODEL28 没有物理 trial、没有 correction、没有可返回的正改善候选。剩余一个预留 SOC 名额没有一个实际 trial 可供修正。

本次唯一算法变更是**在上述已证明的特定末分支，允许用一个确有新增合法支持的 primary 消费原第64名额**。源63次调用、257.595331213秒与58value均继承；原累计1800s/64LP/160value/每LP10s不变。之后没有SOC额度，这是显式的机会损失，不再宣称新候选仍保留SOC补救。

不承诺这次新切面会产生改善。若没有不同的新支持，零新LP终止。若新候选无法经过原接受规则，保留原最后接受点；不得免费再解、加预算或递归另开模型。

## 2. 数学：无需未知旧步的合法支持

原两分支为
$$
\phi_\sigma(E,F)=\frac{\sigma E+\sqrt{E^2+4F^2+\epsilon^2}}2,
\qquad \sigma\in\{+1,-1\}.
$$

任一真实有理/二进制有理三元组 $n=(n_1,n_2,n_3)$ 满足 $\|n\|_2\le1$ 时，
$$
\ell_{\sigma,n}(E,F)
=\frac{\sigma+n_1}{2}E+n_2F+\frac{n_3\epsilon}{2}
\le\phi_\sigma(E,F)
$$
对所有 $E,F$ 成立。由已付 attainer 的 affine $E_*,F_*$ 选择方向，再采用冻结 unit_ball_direction 的逐分量朝零修正，并以精确 binary64 有理平方和核 $\|n\|_2^2\le1$。不把浮点归一化直接称严格单位法向。

恢复当前真实行 $e_0,f_0,de,df$ 与原变量缩放 $S$ 后，
$$
E=e_0+de\,S z,\qquad F=f_0+df\,S z.
$$
因此新增原单位 LP 行是
$$
\left(\frac{\sigma+n_1}{2}de+n_2df\right)S z-\rho
\le \eta_{\rm target}
-\left(\frac{\sigma+n_1}{2}e_0+n_2f_0+\frac{n_3\epsilon}{2}\right).
$$

代码直接复用原 support_row，原 $\eta_{\rm target},\epsilon,S$ 不变。该证明只需要法向合法，不需要恢复旧未知159步，也不声称向内舍入后的新支持仍在未知旧步处严格接触。

原 four attainers 只提供选法向的已付信息；当前模型所有512 bank行与4条原补充行完整保留。即使同一个 grid/branch/row 对应新法向，也追加为独立支持，不覆盖旧行。

## 3. 窄输入与严格同模型边界

根的 reader/transfer 只读原完成日志一次，核原source、run/job、原请求完整source闭包及记录指纹。原日志 SHA：

ee418c296ab6af5cac1066a19811cc0393c53f7b576244b151183e09f1fe62c9

MODEL28 JSON+LF SHA：

4177aefe47ee4675b4f4fc4ceadf3fcb300b0fe7c36450acef6aab5331cf78f1

COMPLETE JSON+LF SHA：

c9731defe5d0bc80b6f8aaad43e9a834a45e2a53618668c05ec8e06f93ce8c90

只在runner内使用原checkpoint：exact reference163、final159/163、4438/4533完整有序池/版本7/6、512 bank、4条原额外支持、35个学习events及既有commits/coefficients、当前controller。禁止用报告中简短pool计数猜恢复ID，也不重播事件去重建bank。

源码直接核：

1. 原source MODEL28的 returned_candidate=false、gap_met=false、inexact=true、几何前拒绝原因、空trial/correction、原63调用/只一次scoped LP。
2. 原allocation 62已用、余2、grant1、ceiling63、结束余1、cfg未变；确无新 separation cut，初始支持516。
3. 恢复 complete 两factory binding、oracle center binding、原物理base/159 array、M、原physical widths、subspace、coordinate、active row mapping与pool版本。
4. 原primary全部 A,c,lower,upper,active_values,active_J,active_groups,active_tolerances,state,step_scale hash，以及已经guard过的真实 b,targets hash。
5. 原冻结 $\gamma$ / learning state / exact $B$ / guard scalar signature，不再commit一次空pending，更不在本模型内改target。
6. 原有序512 bank state和四supplemental normal记录；实际重建出来的原516支持 $A,b$ 必须匹配 paid m28 hash。
7. 两张原完整grid标签/整数ID/分支与attainer的base $e,f$ 对应；base比较只用原replay容差。旧方向/JVP不重新执行。

重要恢复边界：

- 不调用硬编码438输入的原 DirectReferenceGuardObjective constructor 让它重新迁移一次。根写中途checkpoint-aware构造，保持原历史“epoch初始438”definition与当前512状态分别准确。
- 仍用已付 direct-reference ordinary方法，继承正确field/gate/objective identity，不能再接回旧FiveHeight普通identity。
- 新释放规则放独立solver metadata，原field/complete数学binding不改；原正常allocation函数未修改，本次显式绕过的是它的“最后一个名额不授primary”分支。不得把新释放记作原规则本来允许。
- 必要当前两网cache/selectedJ和缺失bank行的重建都收费。没有从原日志复原未发布dense A/J。
- 重建后必须保同一runtime对象，把两网cache直接消费进selectedJ/factories/新LP/实际trial；不做一次昂贵审计后再另进程冷恢复。

## 4. 新模块接口与真实调用顺序

新文件：

- scripts/frame_metric_terminal_paid_slot.py
- scripts/frame_metric_terminal_paid_slot_development.py

旧源码全部保持。

### 4.1 资格与预备支持

validate_release(source_model, cfg, ledger) 只核特定已付末分支与真实63/62/1 ledger，返回明确一名额释放收据。它不调用LP、几何或J。

prepare_terminal_support_model(primary, complete, source_model, cfg, ledger, *, wall, progress)：

1. 验证以上同模型/原guard/原两factory身份；
2. 调用原 complete.initial_cuts() 一次，真实重建512+4并核原hash；
3. 在原selected observable内找四attainer的当前row；仅缺行时调用原 oracle.original_row 新求必要行J；
4. 用已付affine $E_*,F_*$ 形成合法normals，原base $e,f$ 严格对接；
5. 按当前浮点组装后的整行 $[A,b]$ hash 判重，保原516序列不动；
6. 只有真正增加至少一条不同支持时返回 TerminalPaidSupportModel。全部重复则返回None，明确0LP；原最后名额仍未用。

这一步不调用旧方向JVP、不恢复旧未知step、不调用旧LP63、不修改真实学习池，也不写bank来替换旧法向。

TerminalPaidSupportModel 继承原 SupplementalCompleteModel 的完整仿射函数、原cut和report方法，只把 initial_cuts() 改成返回上述已准备、只读的支持bundle。原数组组装不是区间证书，后续原单位残差与真实门仍不可省略。

根将新的wrapper显式安装到当前primary/模型报告列表对应位置，不通过monkeypatch改变冻结class。prepare与solve之间不修改cfg、pool、gamma、targets或模型。

### 4.2 唯一新LP

solve_terminal_last_slot(primary, wrapped, cfg, ledger, *, wall, remaining_seconds, progress) 调用冻结 solve_remembered_primary。它看到实际ledger63与原cfg上限64，故最多调用一次原solver。

- linear_program_invocation_count / primary_LP_invocation_count 仍由冻结solver在调用前增加。
- 原SOC计数1不变。总额最多64，不是把原63计入新的独立小budget。
- 原修复rho、完整仿射范数evaluation、原residual/box/improvement floor全部保留。
- 若remaining_seconds已不足、wall失败或准备阶段失败，可以0LP退出；实际费用/已启动数照实保留。
- solver异常如果已启动仍是第64次付费；异常前0启动则仍63。没有虚收费或清零。
- 调用后没有SOC可供修复。必须记录“新候选无SOC机会”，不能把不存在的SOC当作已拒绝/已通过。

新wrapper仅在新候选已经被原 evaluated(step) 实际评价时复制其exact binary64 step到报告，零额外evaluation/JVP。该记录只属于新第64次候选；旧63的未知step仍未知。它用于避免下一次再丢失已经得到的新向量，不是保存任何跨run数组cache。

## 5. 实际trial、失败与末点合同

若原solver返回None或未满足原正改善floor，零物理trial，保留原best。阶段报告应保原gap/inexact/solver status与本次新支持数，不宣驻点。

如果返回候选，根的显式recovery复用原ordinary candidate/actual-d/精确盒/两网14门/严格metric下降/实际pool学习/ordinary fallback。两网首全步或原合法backtracking所需value照实收费。唯一被本次明示改变的是没有可用SOC名额，不能伪装执行了其分支。

- 不降低curvature/metric容差，不放宽guard RHS、radius cap、physical width或auxiliary。
- 实际学习facts保留；新full primary的真实defect可以按旧规则记录，但不能回头改变当前冻结$\gamma$。
- 一次新LP后不再构建另一primary模型，源总LP最多64。没有新候选时也不能借unused mark另重试。
- 若best不变，引用源独立/接受时完整两网门且注明复用。若newbest改变，使用新接受trial原14flags/physicalSHA；不拿compact eta对照替代完整门。
- 完整未来checkpoint保存新的best、全部池、bank、learning/两streak、当前累计clock/values/LP，以及此次新四normals的独立来源记录。它们不偷偷插入“latest normal per row”而覆盖原512。
- 新实际向量、原数组及source日志只留runner/原log；发布源、参数、指纹、人类结果。

## 6. 资源与已付工作的准确继承

科学单钟仍从原新任务起点累计：

- 起始科学已付 **257.595331213 s**；
- 起始真实values **58**；
- 起始LP **63**（primary62，SOC1）；
- 全部上限仍 **1800 / 160 / 64 / 每LP10**。
- 冷ordinary、source读取/必要24输入恢复、当前J/支持重建、原新candidate评价及两网trial均进剩余同钟。当前进程import/dev成本另列且process总计一并给出。
- 之前关闭m7 epoch的241.314203844 active等祖先账仍保留，不能拿它给此任务再充/再清零。
- 本任务前两次入口失败已经含在257.595中，不能再加一次28.690或只继承最后成功增量。

若恢复本身预算已尽，零新LP退出而保真实费用。一次冷调用是非抢占的，返回后可能超过time limit；必须如实报告，不把超时调用藏到initialization。

旧3组9个direct-reference开发check只消费原已认证收据。没有旧科学/旧developer/旧primary/JVP replay。新11个纯接口fixture的首次执行与科学分别记成本。

## 7. 最小新开发：3组11个case

新 developer_check() 返回 all_passed、groups、executed_check_count、源hash及execution。三组case数 **4 / 3 / 4**。

| 组 | cases | 只覆盖的新边界 |
|---|---:|---|
| terminal_release_eligibility | 4 | 特定末分支可释放；原有物理trial拒绝；gap已完成拒绝；第64已花拒绝 |
| support_bundle_nonreplacement | 3 | 保原重复行/序列并只追加不同新行；全重复0新调用；非有限新支持拒绝 |
| single_slot_ledger_and_failure | 4 | 一次63→64且SOC余0；二次调用拒绝；调用后异常保64收费；调用前异常不虚收费 |

最多3次新的stub callback，**realLP / ordinary geometry / directionalJVP / oldsuite / optimizer均0**。这些不调用旧9组，也不测试已经付过的geometry/rank或旧solver算法。首执行只在公开Actions，当前没有任何passed声明。

开发源码与production保持分开。若新fixture失败，仅修实际未完成路径，已通过组按其真实收据复用，不机械重跑。

## 8. 发布及下一科学问题的边界

根负责恢复constructor/transfer/显式recovery/audit、完整source manifest、公开workflow/request与唯一运行；此两小源只解决新支持与最后名额释放。任何hook都不得改变旧evaluation数学identity或删除freeze check。

此改动检验的是“已付全网方向信息能否用剩余一个真实名额形成可接受新候选”。若不能，它仍留下完整新候选与完整affine gap/attainers供下一不同机制，例如完整norm-cone或更有效的多法向支持维护。无论结果怎样，都不能原样再加64次、重跑旧63次，或把当前allocation造成的inexact停止宣为数学驻点。
