# Run10：完整十二通道矩积分与最终同场闭面证据的 R716 消费

2026-11-27，Astra-larger-e4e2a2bf-20261126。

本交付把已刊的完整 R716 通量、中心化矩和定量公式绑定到实际 run10 的独立场及准确费用链，并接上真正完成的闭面主报告。它没有产生一个未来场、积分值、非全等证书或完成结论。当前正在执行的求解器进度不是 immutable 场快照；本计划没有从进度中的 point、角数或缓存命中数填入费用输入。

数学依赖沿用 [R625](../results/R625-second-volume-moment-quotient-bound-and-fixed-caps.md)、[R650](../results/R650-positive-definite-flow-support-reach.md)、[R715](../results/R715-reference-centred-normal-sixjets-and-error-ledger.md)、[R716](../results/R716-asymmetric-fixed-caps-and-centred-volume-moment.md) 和已刊完整源。这里不另登记这些定理。原 run09 的完整源、参数和未返回历史责任保持原状；run09 终止没有提供一个可替用的真实场。

## 1. 独立输入范围

本次直接采用已刊 run10 家族：

| 对象 | 完整 SHA256 |
|---|---|
| 全变量科学入口 c3dc | c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1 |
| 完整纯 reader 2efa | 2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e |
| 全 32 段 normal 6d2b | 6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4 |
| immutable root packet 31f | 31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805 |
| 完整 base 6a803 | 6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865 |
| 实际独立 target canonical | e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049 |
| 实际 reference model | 081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5 |
| 实际材料绑定完整文件 | 4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf |

最后一项为430908字节的真实生成绑定文件；不能与其 canonical identity 混同。当前参考实际使用2218叶的记录；2397叶只属于旧 dc5 地址载体恢复。旧载体值不会被当成当前 scalar、reference 或准确积分值。

原六输入的完整身份仍由当前输入适配器及75个 runtime source 角色逐文件消费：warm、node、scalar、reference、carrier、preparation 全部保留。新的矩入口通过完整准确 normal binding 读回这些文件及全模型，不以相同 argv 或同一公式替代真实身份。完整75角色在交付清单和再生器中逐项列出；同一实际 source、whole file、point、model、snapshot、target 和准确域链必须全部一致。

输入点遵守已批准的准确费用合同：选择真实 complete-required-angle immutable packet 的同一个完整自由点，或 caller 明确指定的原 packet。它可以属于首个完整初场，不必等待 accepted/final；它不能由 mutable 进度补写。1,333,370个自由变量、M160/J923、三路482个角槽、全部六控制和所有32阶段保持原布局。这里没有声称已消费所有优化点或所有历史点。

## 2. 完整源的实际变化

共享算术源 r716_closed_surface_moment_arithmetic.py 保持 f79c69ed 原字。全 V/m/Q/A2、p4 质量/一矩/二矩、中心化、一般三相以及半转简式全部复用它。

新的 run10_complete_closed_surface_moment_integrals.py 从完整57152字节的19e4源派生。八项确定的完整文本变更仅为 run10 名称/schema，以及 normal、准确输入、准确径向、科学入口、reader、normal model source 和 target 的七个完整 pin。完整反替逐字还原原源。28个原顶层函数中26个全文不变；另外两个只是来源表和错误信息的 run10 身份适配。积分、全域检查、局部唯一性包含、物理流读取、恢复及缺域处理没有数学改变。

新的 run10_r716_centred_volume_moment.py 保留原 validate_complete_flux、conditional_quantitative_bounds、compact_intervals 等函数全文。它增加最终闭面主报告与副件的严格消费者，在真正的同场几何责任已付时，才把原条件性数量公式实例化为一个实际界。新增内容没有改动中心矩公式、旧 pure reader、科学源、缓存行为、根或控制分支。

所有运行源及完整再生器均小于100000字节。各文件按完整字节独立保存；没有用截断源码、片段或占位函数充作完整体。

## 3. 准确 normal 与整域通量的绑定

准确入口分别为：

| 责任 | 完整源 SHA256 |
|---|---|
| 同点 packet/准确输入 852bc | 852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8 |
| 共享旋转/逐阶段准确核 29eed | 29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b |
| 准确径向及整角参考 fdddef | fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c |
| 全32段/六 jet producer 0d6e | 0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83 |
| whole leaf reader cf571 | cf571370b53288048db55dbcc0156a36de481a3fd91c9b3e0b85398905af39a5 |
| 全域 Gram/K/support e317 | e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7 |
| 完整几何/β绑定 96d3 | 96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9 |

矩 producer 要求准确 normal 的完整 input/request、最终 execution binding、actual input、全模型、全 point NPZ 和 snapshot 一致。每个实际 journal 的全部32个 stage、真正的根中心、收缩域、两阶角 jet、六控制、whole radial plan 和 reference 证明均保留。

全部实际 literal 角继续用于工作分支关联。积分域另要求完整1024个闭角胞覆盖
$$
\phi/\pi\in[0,2],
$$
并包含所有原径向 cell 及完整准确尾。准确径向地址为
$$
s=\alpha S+\beta,\qquad \alpha,\beta\in\mathbb Q.
$$
相邻 leaf 端点必须精确相接，其真实宽度由准确 S 盒严格证正。原922个 cell 与已声明的全部细分必须都在，不以工作网格差代替准确长度。

每个真实 leaf×angle cell 读完整物理六 jet，包含全部 raw hDelta、hpDelta、hppDelta。中心化根残差不会替代这些项。逐行核 stream header、顺序、footer、所有记录数、whole SHA 和对应完整根 journal。准确场包围与工作浮点六 jet 误差是不同声明；这里没有新增后者的已付声称。

对整个闭胞 B，完整函数范围盒给出
$$
\int_B f\in |B|\,[f]_B.
$$
这正是原实现的完整积分费用，不是节点采样或新增近似求积。宽盒只意味着该实际见证未够紧。全部实际原输入/输出在最终报告前重读。

## 4. 十二个通道和正式闭参数面

完整通道一直是
$$
V,m_x,m_y,m_z,Q_{xx},Q_{xy},Q_{xz},Q_{yy},Q_{yz},Q_{zz},
\operatorname{Re}A_2,\operatorname{Im}A_2.
$$
采用上半片取向
$$
N=F_\phi\times F_s,
$$
并保持原 R716 通量公式
$$
V=\frac13\int F\cdot N,\quad
m_i=\frac14\int F_i(F\cdot N),\quad
Q_{ij}=\frac15\int F_iF_j(F\cdot N).
$$
A2 的两个完整通道独立保留，不从几个截面或有限角代替。

下半明确为 Dz=diag(1,1,-1) 作用于完整上半，取向为下半 Fs×Fphi。完整反射使 z 为奇的通道相消，其余相加。两轴心平帽均完整加入；H 是同一个完整当前点的末字，R 来自同一准确 scalar。平帽 A2 的完整角积分为零，同时其 V 和全部对角 Q 贡献保留。

在没有另付闭面外向、有界侧和固定标记外管条件之前，这些仍是完整参数通量。producer 不把 formal_closed_flux 改成嵌入实体证明。本次新增 consumer 能读取真正完成的闭面证据后付这层解释；不会改变 producer 先前结果的定义。

## 5. 周期与半转仍逐阶段支付

相邻整角胞、完整0/2π接口及实际 literal 角必须以根内盒向另一唯一性盒的有向包含关联。盒相交不够；所有32个上游 stage 都保留。

半转是独立责任。保留
$$
P=\operatorname{diag}(-1,-1,1),\qquad D=P\oplus P,
$$
以及准确方程
$$
C(\phi+\pi,Du)=P\,C(\phi,u).
$$
normal frame 和法向增量按原规则协变，真正的 selected branch 要由每一对整角胞的全部32个 signed root 包含支付。只有这一实际检查通过才启用补偿简式。频率奇偶标记本身不是分支证明。

一般三相中心化张量始终保留完整一矩和混合二矩：
$$
m_\alpha=R_\alpha m_\Omega+m_B,\qquad
J_\alpha=R_\alpha Q_\Omega R_\alpha^{T}+Q_B-
\frac{m_\alpha m_\alpha^{T}}{V_\Omega+V_B},
$$
取α=0、π/4、π/2。这条原 R716(2) 的一般公式不要求已付半转。若半转未付，B_eff 简式的已应用字段保持 null；不会丢掉一般十二矩路线。

## 6. 最终闭面主报告是必要的证据入口

完整闭面 producer 独立硬钉为：

run10_complete_closed_phase_grip_evidence.py，70086字节，
f7a10d7d6050cd57b5aea72d374c33662bf0c88e4175b6f7b738d6331d0976be。

实际参数指向：
{work}/run10-complete-closed-phase-grip-v1/report.json。

consumer 首先读取这一主报告的完整原字节，核 source 和
actual-run10-complete-closed-phase-grip-evidence-v1 schema。只有以下条件全部成立，才继续读副件：

1. complete 严格为 true；
2. status 精确为 complete-same-field-consumption；
3. all_bound_input_and_generated_evidence_bytes_rechecked 严格为 true；
4. 主报告 point/model/snapshot/target 与当前矩输入的完整真实对象相等。

然后只使用主报告 R716_outward_tube_evidence 中的完整三字段 file record。它必须逐字且唯一列在 generated_evidence_records 中；路径自行猜测、另一个 sidecar 或仅有 final_complete_producer_report_required 标签都不能替代。

副件还须指回这个真实主报告绝对路径；主、副的 source、point、全模型、snapshot、target、normal binding、actual input、geometry binding 与完整域记录逐项核回。全部 actual_complete_input_records 和 generated_evidence_records 重新按完整字节/SHA验证。同一个路径若被绑定不同身份立即拒绝。

不同 followup 不假定使用同一个 checkout 绝对路径。原 source/proof record 在原路径完整读回；当前加载的每个对应副本也另读全字，并逐 role 核字节数与 SHA 完全相同。副件重放仍传原 records，不重写原路径，不把原文件缺失作为可接受副本。point、原 normal binding 和 sidecar 指回真实主报告的路径关系仍严格；原 normal report 的 exact record 还与其已登记 immutable 副本全字相等。

晚失败会把原闭面主报告 complete/recheck 改为 false，并清已付数值。本消费者在这类主报告下不打开此前已写的副件。完整结束前又核主/副和所有原记录，并保存实际主报告的 immutable 原字节副本。因此孤立副件不能被当作外管或体积矩证书。

主报告不存在或尚未完成，不是几何失败，也不是零 reach；它只留下明确未付责任。原完整通量及中心化代数仍可作为条件性结果。

## 7. 消费真实几何证明，而非只读 true 标签

通过最终主报告入口以后，消费者调用其已锁完整源重新绑定当前 geometry report，并经96d3/cf571重读完整准确 normal、全角关联、全部物理流和统计。它比较同一完整 input 对象及 normal binding；immutable normal-report 副本可有不同路径，但其完整字节数/SHA和原 binding 必须相等，不能借路径变化混入另一份报告。

接着直接复用 f7a 的完整函数：

- current_core：完整原自由点、固定160模 chart 和实际 H；
- exact_ports：原掩码、支撑、core/反射/cap C2拼接、全圈同支和真正的 Θ0 物理相位；
- second_pass_support：按最终主报告中原已选的一个正有理 β，重新读取每个真实 whole support row；
- unmarked_body_interpretation：从独立未标记 R650 下界和固定 h=1/1000 重建外管、不交及原 R716 §6 体解释。

没有重选优化变量或 β，没有重算 F/J/根或准确 integrand。这里只从原全域包围重放已登记的充分条件。每个新数值字段必须与完整副件逐项相等。common Aβ=diag(1,1,β) 同时控制全活动、反射、所有物理相位和固定 p4 帽；λmax=max(1,β)，未漏 mixed pair。

闭面原八角色及径向扩张也完整回读：原 e0b44 的 read_input、原 bridge.bind_beta 和原 consume 再执行，完整结果与主报告所列的精确 beta-result 文件一致。全部源/证明记录和每个完整支撑 chunk 保留。强C2相位来自原 Θ0 逆图与固定帽，不从 quarter-grid 或 mode 标签推断。

如果正支撑尚未付，几何解释不升级。如果存在正支撑但未达到0.03D，消费者可保留那个真实正 reach 的数学作用；它不会声称原 README 的0.03D标准已付。source 的 marked 与 unmarked reach 保持分开。

## 8. 独立未标记外管与准确体积矩

原 R716 §6 先对未标记闭族使用它自己的正支撑和曲率界：
$$
\sigma_0=\min(\sigma_{\rm activity},\beta H),\qquad
\tau_0=\min\{\sigma_0/\max(1,\beta),\,1/K_{\rm activity}\},
$$
当活动曲率上界为零时去掉第二个限制。只有严格
$$
1/1000<\tau_0
$$
才把四个固定 p4 柱体放入同一个所有相位的外法向管。它不以已经知道标记嵌入来反推未标记 reach，不假设整个活动像位于一个 slab。

消费器要求副件中未标记 all-phase embedding/outwardness、严格外管余量、十二矩加法解释全部真实已付，并从全 support/ports 复算。由此才识别
$$
\Omega_{\rm marked,\alpha}=R_\alpha\Omega_0\cup B
$$
的实际有界侧与原通量积分对象。完整 B 的 m/Q、全部四柱、上下帽方向和原 p4 配方保持 f79c 原式；不更换帽来取得对称。

总 V 的准确盒还须与零分开，才可作中心化除法。闭体解释和区间正 V 是分别检查的责任。宽矩盒、半转未付或 A2 未分离都不等于全等或无解。

## 9. 从原数量公式到实际 δE 下界

原 conditional_quantitative_bounds 函数全文保留。caller 如显式传入 --conditional-reach-lower，该数仍只是条件性假设；本完整 ready 不传它。

新的 actual_quotient_bounds 使用经过上述真实闭面证明的 marked all-phase reach 下界，而不是可自由填写的常数。它仍调用原 R625/R716 数量公式，面积和 D 上界来自同一个完整矩域；actual R248 相位、闭像取向、连通拓扑与外管已由同一个闭面源消费。

一般三相路线与已付半转路线分别保留其合法下界。取这些合法数的最大值，得到原 δE=max_t inf_{T∈E(3)} d_H 的充分下界。E(3) 包括反射；中心二矩 Frobenius 不变量保持原群范围。只有真正的完整几何、正 V 和一个非零中心化不变量都已付时，unconditional_noncongruence_certificate 和 delta_E_positive_certified 才可为 true。

这不是将 complete 字段改成问题完成：该字段仍表示完整积分和中心化代数已消费。非全等、reach、全域相对 Gram、δhold、握持、同g收敛精化和网格导出保持各自责任。新源 research_goal/problem completion 始终不因某个矩界自动成立。

## 10. 两个完整实际步骤

原 producer 的10个 argv逐字保留数值参数，仅切独立 run10 source/path；完整时间预算600秒，maximum-angle-blocks=0，包含全部原域。只能在完整角块之间停止，已完成块实际保存，缺域保持 full totals=null，不填零。

原 consumer 的6个 argv也保留；仅新增两个词：
--closed-phase-report
{work}/run10-complete-closed-phase-grip-v1/report.json。

完整 step 对象保留原33/47个 scalar selector，无删减；消费者再加12个实际证据/下界标量。全部矩阵、逐胞 interval、完整根盒与当前控制字只保存在 runner；公开参数没有将它们重新编码。

路径：

| 角色 | 完整路径模板 |
|---|---|
| 原准确 normal 输入 | {work}/run10-normal-root-and-sixjet-fees-v1/report.json |
| 完整闭面主报告 | {work}/run10-complete-closed-phase-grip-v1/report.json |
| 完整十二矩 producer | {work}/run10-r716-complete-moment-integrals/report.json |
| 完整中心化/实际证据 consumer | {work}/run10-r716-complete-centred-moments/report.json |

root 应将中心矩消费放在原完整闭面步骤之后；积分本身只需要已经返回的完整 normal 输入。完整计划不填任何未来 scientific report、snapshot、闭面报告或矩报告 SHA。实际 step 排队与 complete=true 都不能从本源码编写推定。

## 11. 完整再生与检查范围

完整 stdlib 再生器从已刊19e4、3576及原03c ready的 whole SHA 开始，执行全部 exact edits，逐字反替回所有原源，检查完整75科学角色以及准确费用/闭面/共享算术依赖，再写出两份完整新运行体及完整 ready。它还提供 ast.parse/compile 和原未改函数/class AST等号检查。

本轮在 functions 中实际完成的是完整文字正反再生、SHA256、字节数和原 argv/selector 等号。executor不可用；没有声称在本轮本机执行了 Python AST/compile、科学模块、Fraction 算例、interval fixture、F/J/根或原完整消费者。root 可对完整再生器作源码检查；这不是科学求解的前置测试或缩样本门。

新 producer 的26个原数学/持久化函数全文保留。consumer 五个指定原函数全文保留，三个原接线函数只增加实际新绑定；五个新增完整函数承担最终闭面对象消费、严格源码副本关联与原公式实例化。两源均有完整可逆文本计划。

完整 source/proof dependency 数及各自真实 SHA 在再生器和交付清单中固定。所有输出保存在新命名空间，不能覆盖任何输入/源码/证据。refs 和普通发布仍由 root负责；本交付只保护完整字节。

## 12. 交付身份

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| run10_complete_closed_surface_moment_integrals.py | 57152 | 0aa16633df87d2700bba332cf2c6a225e746fbda87097b0004f18e3cde5b7504 |
| run10_r716_centred_volume_moment.py | 46327 | 92065cdc580e6c7f4c2d8f0474b0449a8f19fc2ffa873222997e6be0f4140e97 |
| derive_run10_complete_R716_moment_consumers.py | 80002 | a1956902df3e5f2b8248db26d433350f524eb4bd28a69faf36f99a7d5a14f50f |
| run10-complete-R716-closed-flux-centred-moments-ready.json | 15132 | 9aa60ef74e446401c20bc590ca2f68228e8f07ad664aefe116c289df0d4f6652 |

共享算术 f79c 全体17397字节不修改。新的闭面依赖为 f7a10 全体70086字节；其完整适配证明 b3785933 保原字，不能只换标题或内容后保旧 pin。

所有 future result identity 仍为 null。unknown run07/run08/run09 typed/history 责任没有删除；新10入口的完整有限材料包络和所有外变量保持科学源原合同。完成这份完整费用入口只提供真实后继计算能力，不替代任何尚未返回的实际证据。
