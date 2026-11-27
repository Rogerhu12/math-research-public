# R723 独立全闭法管、握持及 R716 兼容入口：完整源码和第 19 轮参数

## 1. 本次交付和实际边界

本包把已正式登记的 [R723](../results/R723-directional-normal-flow-support-reach.md) 做成独立完整证据生产器，并补齐真正可调用的 R716 消费入口。它读取现有同场完整准确几何流，不重新计算工作场、Jacobian、参考均值、normal 根或积分样本。它没有改动正在运行的 scientific driver、变量、步长、优化预算或原来的任何源文件。

本包当前没有真实完整场、normal 费用、连续几何费用或法管结果。第 19 轮的参数选择是既定的相同 Fejér 度量、相同完整变量空间下的独立初点：相对端层总长 $b/S=1/2$，profile 参数 $\delta=1/32$。这些参数由真正返回的完整模型读取；不能用参数文件、初值进度、有限几何屏幕或尚未返回的报告代替准确场输入。

新的闭面分支不先要求原 R650 的目标区间通过，也不调用旧八角色消费者冒充成功。旧八角色字段明确保持 false，旧 beta package 保持 null。新的五项完整来源责任由 R723 自己定义，且须通过最终主报告、全部原始数据重读和准确副件记录才可消费。原八角色分支仍存在于原源文件及新的 R716 兼容消费者内，只有其原来源和原条件全部通过才可使用。

本包改进的是支撑所导致的法管下界；它不消除真实曲率瓶颈。有限 geometry 源对给定点的主曲率已使用完整 $2\times2$ 广义特征公式，本包没有把有限采样或再次计算特征值当作连续 reach 证书。当前连续几何流的完整曲率包围仍须实际付清。

## 2. 精确完整源家族

科学家族保持正式 producer-bound 版本：driver 10fa4e4e、reader 8027ec35、normal 76185c21、packet c750d234、detached-meridian eaeaf274。全部 137 个完整 path/SHA 角色及其中原有 120 个来源对象保留。完整来源表是：

- computations/fixed-fejer-meridian-producer-binding-repair-complete-delivery.json；
- 52,830 B，SHA256 970b8f8bbb141fc7f1c4e5e42d6048497f0de58731e65918f3c4e4cf6aff008a；
- Git blob 45f14a52f824ca947a59bacf73ad123f17fddab9；
- 固定正式提交 8c1251a01aa2a1893386b69d13ab1e0a5ae4aa38。

本包读取的完整 accurate geometry 是 fixed_fejer_meridian_batched_producer_R722_continuous_gram_curvature_support.py，46,742 B，SHA256 6c57f78a9c8b80805e8e551a8fba50a089687cea164bd192c8bead845dda29b4。完整桥 c6b07b17ba9c25985faae62cd5db0991cd27bc4927d22fdd9e56a6c5ac7ae4e1 不变。准确输入 d892bede、posterior kernel 4fc252f8、radial 7c66ed0f、normal-fee c6f6c972、leaf 7892eb49 均为完整已刊原体。

完整旧闭面算法父是 fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py，84,576 B，SHA256 002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f，Git blob 5f3b42618cfab77eaa3297073d71657e8df78dac。新源直接导入这个完整严格父文件，复用其全部 current_core、exact_ports、original_leaves、CompleteTargetDistance、grip、完整 source/proof 读取及有关纯参数区间函数；不猴补它的函数，不放宽身份，不删除任何旧文件。

R723 正式全文为 21,535 B，SHA256 0edbd1039706186d07412a53c8e5c10411c5966dc36e38a7a504cf923d43e7eb，Git blob 2efee88735ae0638062de2e1e1d5706313cac3ea。旧 R248/R650/R661/R715/R716/R717/R718/R719/R722、原题 README、所有原端口及来源适配全文仍由原 proof_files 精确读取；R723 添加为一个明确的新证明角色。

新 runtime 和所有参数/再生器均小于 100,000 B。没有为了限额缩小物理域或原参数。完整137表由原正式文件和真实报告来源闭包共享，不在每个附件无意义地再复制一次。

## 3. 读取边界：完整准确场，不是缓存标签

输入首先必须是 6c57 的最终连续几何报告。其 complete、all_input_and_output_bytes_rechecked、full_upper_cover_processed、continuous_curvature_bound_complete、continuous_support_numerator_bounds_complete 必须为真；否则新入口只写明确未付的报告。

随后调用原 c6b07 完整 load_geometry 和原 leaf 的 verify_geometry_identity。由此重读原始 normal 报告、全部 32 段 journal、局部根包含及周期 glue、1024 个完整角闭胞、全部原 922 径向单元和实际精确切分、完整六jet流、实际均值存在归因、完整137源、点/模型/目标/snapshot/原完整输入与请求。R722 后验存在性不被改写成旧 R709 粗条件为真。

每个 geometry stream 都按原 header/body/footer、路径、字节数、SHA 和原有顺序重读。没有从 mutable progress 填补当前点，也没有从另一个 snapshot 借根。一个真实完整 required-angle immutable snapshot 可以供准确费用读取；它仍不自动成为 accepted/final。原13成员完整 final 路径与 snapshot 路径的来源分别由原读取器核验。

当前物理布局仍是 M160/J923/N2048，参考 M160、冻结 Fejér dyadic chart 和完整标量定义均保持原对象。全部实际160个当前 core 系数、所有三路 omega 字、当前 H 都来自真实同点数组。模型、数学 recipe、实际执行文件身份和完整 source 身份分开核对。

## 4. 全叶 R723 算术

对每个完整叶读取原始准确区间：

$$F,\quad N=F_\phi\times F_s,\quad w=|N|,\quad
a=F_xN_x+F_yN_y,\quad b=F_zN_z.$$

$w$ 的严格正下界是实际 immersion 所需条件，不能从有限点代替。重新计算的 $a,b$ 与原 geometry 的同场支撑区间取交集。$N_x^2+N_y^2+N_z^2$ 与 $w^2$ 及原 Lagrange/Gram determinant 区间取交集；各平方分量再作合法区间收缩。不使用独立误差未经证明的数值相关性。

令 $\tau=3D_+/100$，其中 $D_+$ 是同一完整几何流提供的全三维 R717 直径上界。定义

$$C_0=wa-\tau(N_x^2+N_y^2),\qquad
C_1=wb-\tau N_z^2.$$

实际使用整个准确区间的下端点，要求同一个 $\beta>0$ 满足所有叶的

$$C_{0,-}+\beta C_{1,-}\ge0.$$

这是一组精确有理仿射不等式。原 $\beta\le1$ 与 $\beta\ge1$ 的划分只用于完整参数区间选择；新 R723 仿射公式在两个分支相同。原所有弱/严格区间、端点和来源 witness 均保留。

优先选择通过 R723 目标的 $\beta$。若没有，则保留原 R650 目标区间作为另一可用充分选择；若仍没有，继续尝试完整严格正支撑区间，以便诚实给出可能小于 $0.03D_+$ 的正法管。旧目标不是新入口的前置要求。如果连完整正支撑也未付，则相应结论保持 null，不把宽盒失败写成几何不可能。

对选中的同一个 $\beta$，每个叶再次计算

$$\sigma_{\rm leaf}\le A_\beta F\cdot n,\qquad
\rho_{\rm leaf}\le
\frac{w(a+\beta b)}{N_x^2+N_y^2+\beta N_z^2},\qquad
A_\beta=\operatorname{diag}(1,1,\beta).$$

区间分母还与
$[\min(1,\beta)w_-^2,\max(1,\beta)w_+^2]$
取交集，必须严格正。分子、分母及有符号乘积全部用 Fraction 区间算术，没有未经定向的浮点除法。每叶下界取直接商下界、合法的原 $\sigma_{\rm leaf}/\max(1,\beta)$ 下界，以及已实际通过该叶仿射条件时的 $\tau$ 的最大值。因此保留原充分界，不会因新计算舍弃已有合法下界。

## 5. 完整帽、下半片、全相位和 mixed pairs

两个固定 p4 帽保留原 R661 完整图形和度量。沿用原完整常数：

$$h=1/1000,\quad |\nabla p_4|^2\le1/400,\quad
G=1/100,\quad K_{\rm cap}\le5,$$
$$d_+=801/800,\qquad d_-=1281599/1280000.$$

源码精确核 $d_-^2\le1+1/400$ 且 $d_-d_+\ge1+1/400$。在 $B=\beta H-G>0$ 下，帽的方向比值下界为

$$\rho_{\rm cap}\ge
\min\left(\frac B\beta,\frac{B\,d_-}{\beta+1/400}\right).$$

完整目标区间添加两条端点条件：

$$(H-\tau)\beta\ge G,$$
$$(d_-H-\tau)\beta\ge d_-G+\tau/400.$$

两条同时成立时，帽方向下界亦可提高到 $\tau$。这不是抽样两个帽点：R723 的完整凹性/端点论证覆盖整个梯度平方区间，实际 p4 几何与固定常数由完整源及原证明绑定。

旧 exact_ports 全体继续证明 core signed-$s$ 反射的 C² 接合、Cartesian 帽接合、源定义的球面拓扑、完整活动图和精确固定-chart R248 相位公式。$A_\beta$ 与物理 z 轴旋转及下半反射交换，所以同一支撑/曲率包围覆盖整个相位族。固定帽与活动部分共同使用一个 $\beta$。

联合法管注入使用 R723 的完整结论：平行面流横截覆盖及不同法向位移的严格排序同时成立。没有把“各个平行面嵌入”偷换成全法管注入，亦没有遗漏活动/帽、上/下或其它 mixed pair。所有这些结论都以完整真实 C² sphere、全域 immersion 和完整支撑包围为前提。

## 6. reach、直径与旧证据分离

全闭曲面使用

$$\rho_-=\min(\rho_{\rm activity,-},\rho_{\rm cap,-}),\qquad
K_+=\max(K_{\rm activity,+},5),$$
$$\operatorname{reach}(S_\alpha)\ge
\tau_{\rm R723}:=\min(\rho_-,1/K_+).$$

同一个报告同时保留

$$\tau_{\rm old}=\min(\sigma_-/\max(1,\beta),1/K_+).$$

后者字段仍名 R650_reach_lower，明确是直接从同一准确场重算的比较下界；它不代表旧八角色消费者已执行。源码核新下界不小于该保留下界。达标必须实际验证 $\tau_{\rm R723}\ge0.03D_+$，没有改变原目标。

$D_+$ 保留 R717 的同一叶全三维位置范数、完整帽范数与原整体柱界之间的合法取优。完整三维 target-distance 仍对每个 upper box、反射 lower box 和两个完整 marked cap 取全目标最小距离。任何一个宽盒都不能删除；它可能使 holding 下界为零，仍须诚实报告。

新报告 complete 只表示完整读取和计算完成。reach、Gram $10^{-6}$、固定握持 $0.2D$、标准 held Hausdorff $0.05D$、强化 $0.2D$、$\delta_E$、同度量收敛及 mesh 导出分别保留真实已付或未付状态。

## 7. R718 使用实际 sigma，不借用方向比值

新分支的 $\rho_-$ 不是 R718 的 $\sigma_-$。R718 继续使用同一完整 marked closed surface 上实际计算的

$$\sigma_- \le A_\beta F\cdot n.$$

原完整32项 log 正级数、32项 exp 正级数及96bit向下有理封口函数原字保留。完整当前 core 计算真实轴比；R719 的 $7/3$ 只在原严格连续曲率密度正性、固定前三 RN 系数和完整适用范围全部已付时记录。R720 的更强常数不是本实现的运行输入，也不需要等待新常数。

只有新 R723 完整闭面/外向/实际正支撑证据已付后才尝试 R718。原全目标盒下界原样保留，最终取两个合法下界的最大值。可选计算的 MemoryError 仅使整个增强 unavailable，并完整恢复原 holding/grip 状态，不能留下局部修改后的数值。来源错误、数据不一致或错误模型不会被当作可忽略的可选失败吞掉。

## 8. 独立 unmarked 管与 R716

R716 的 p4 外加实体解释不能从 marked embedding 倒推。新分支独立重建准确 unmarked 球面：原活动部分不变，两帽换为平盘。平帽的方向比值准确为 H，曲率为零，支撑为 $\beta H$。因此

$$\rho^{(0)}_-=\min(\rho_{\rm activity,-},H),$$
$$\tau^{(0)}_-=\min(\rho^{(0)}_-,1/K_{\rm activity,+})$$

（若活动曲率上界为零，则没有该倒数限制）。同时单独保留其 $\sigma^{(0)}_-$ 及旧 R650 比较。必须实际支付

$$\tau^{(0)}_->1/1000$$

才声明固定标记位于每个 unmarked 相位的外法管内，并实例化 R716 §6 的实体加法及十二原矩加法解释。全流程仍保留 p4 四组件不交、真实向外、完整 R248 phase 和 cap 接合来源，不假设半转或重心为零。

输出副件 R716-unmarked-outward-tube.json 记录完整实际 point、model、snapshot、target、normal input/request/binding、geometry binding、源和证明，以及 required_final_report_path。副件明确要求最终主报告；中途写出、晚失败留下或独立搬来的副件都不能消费。

## 9. 新五角色、完整范围记录与最终提交

五个角色是完整同场及来源绑定、全 normal32/六jet/径向/圆周覆盖、C² sphere及精确全相位族、共同方向支撑/曲率/直径、固定帽和反射完整性。它们是新的独立字段，不能写进旧 e0b44 要求精确相等的八 claim dict。

每4096个连续原叶写一个方向范围记录。该记录保留所有原流文件、整范围精确原序 hash、每叶来源和方向计算 hash、原起止 ordinal、实际计数、完整最小下界及 witness。所有原始完整 $F,N,w$、六jet及精确域仍在原 geometry 流中，是每次验证必须实际读取的数值输入；不是只保最小值后丢掉其他叶。

范围分组只改变文件包装。完整验证会逐叶重读所有原流并重算每个范围的所有有理式和原序摘要，逐对象比较生成范围，不信一个 complete 标签或计数。不能用缺失范围、重复原路径、改变的 ordinal、其它点或替换的源副本通过。

最终生成 complete-R723-directional-evidence.json、全部方向范围以及独立 R716 副件。它们只有在主 report.json 最终 complete/status/全 input-output recheck 成立时可用。晚失败清空顶层所有已付数值、五角色、package、范围列表及增强结论；先前生成的 provisional 副件不会被接受。无关未知责任仍保留，失败不宣称几何不可能。

## 10. 完整再消费 API

新 runtime 提供 validate_complete_report(repo, report_path, expected_report_sha256=...)。

它先拒绝 incomplete/late-failed 主报告，然后重读全部原 input/output 路径、完整 field/cover、全原流及normal32域、精确端口、两遍方向支撑、每一范围、全原 source/proof、独立 unmarked 副件和已使用的 R718 增强。当前 checkout 的源码副本只允许完整 SHA256 与 bytes 相同；原路径仍实际读取并保留，不把改名或缺失的来源当作副本。

completed consumption 但几何条件未付可返回 R723_evidence_available=false；一个不完整主报告不能凭残留 sidecar 获得该状态。所有新 F/J/root/integrand 计数必须准确为零。验证结束重新读取所有绑定字节。

此 API 是后继证据消费的一部分，不被加入 solver、normal 或 geometry 求解前置步骤。本包不新建或要求某个 fixture、AST、编译或单独验证 Actions 来决定科学入口。

## 11. 已接通完整 R716，未把旧标签放宽

原 R716 consumer d0fe 的完整旧 validator 被原字保留，仅命名为 validate_legacy_closed_phase_evidence。新完整 consumer 加精确 source/schema 分派：

1. 原 002eb 主报告仍调用完整旧分支，八角色、原 beta 源与原条件全部不变。
2. 精确1782 R723 主报告调用新的完整分支。它先验证主报告，再调用第10节 API，复读全部原数据；将 point/model/snapshot/target、完整 actual model/point arrays/snapshot file、原 normal report、full binding 和 full input/request 与矩输入逐对象等号比较。
3. 原 normal report 与矩生产器保存的 immutable copy 必须全 bytes/SHA 相同；原路径关系保留。
4. 独立 unmarked sidecar 必须是主报告唯一精确生成记录，且由完整同场重算得到。晚失败、错误来源或缺失域不能被替换成条件为真。

新分支明确 all_original_eight_beta_roles_and_radial_extension_rechecked=false。它给原 R625/R716 定量公式传递已付的实际 marked R723 reach；未付时保留 conditional arithmetic 和 null 的无条件结论。独立 unmarked tube、完整正体积以及非零中心不变量仍是必要责任。

完整 moment producer 45ca、完整算术 f79c 原字共享；没有重算积分源或新样本。原全部十二通道、完整 lower/flat-cap、一般三相完整中心矩张量、真实32段 signed half-turn 之后才启用的简化补偿式、正体积及非零中心量条件、原 main 和实际 quotient 算法均保留。新 consumer 全文可逆回 d0fe 原字，只有新schema、明确legacy函数名、完整新分支和说明文本是新增。

## 12. 第19轮完整参数

闭面 ready 完整保留8个 argv：

- repo；
- 真正19同点完整 R722 geometry report；
- 新鲜 R723 输出目录；
- support-chunk-rows=4096。

唯一参数值改动是输出目录；运行 source/id/报告映射同时指新独立入口。全部原66个 selector 名和表达式保留，另加11项 R723读数。原 reach_lower selector 仍展示明确的 R650 比较，新 R723_reach_lower 才显示新方向界；公共 reach_over_D/达标字段来自实际R723界。原完整scope和所有历史参数另以明确 parent 字段保留，不把旧“八角色成功”的说明当当前结论。

R716 ready 包含原完整10词生产步骤和新完整8词消费步骤。生产器整 step 对象保持原字，包括600秒、maximum-angle-blocks=0和全部34个读数。消费者只换新源码、新鲜结果路径和明确R723主报告路径；所有其他argv词保持原顺序。原60个消费者读数全部保留，另加5个R723兼容字段。

若原同一19矩生产步骤已经排队或已真实完成，root 可以直接使用新 consumer step，不能重复生产步骤冒另一个输入；本包仍交付完整两步以保持全参数可审。没有删除或替换任何现队列对象，本代理未写refs/queue。

新路径：

- geometry输入：{work}/fixed-fejer-meridian-batched-bhalf-first-R722-continuous-gram-curvature-support-v1/report.json；
- R723输出：{work}/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-v1/report.json；
- 原矩输入：{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-moment-integrals/report.json；
- 新R716结果：{work}/fixed-fejer-meridian-batched-bhalf-first-R723-r716-complete-centred-moments/report.json。

全部未来完整报告、实际点、当前model、snapshot、费用结果及$\delta_E$均未填值。数学recipe 957cf…不是实际文件或field的替代身份。

## 13. 完整构造与可逆参数来源

源再生器1从完整002eb读取原 helpers、完整 unmarked 函数及完整 R718 函数；七处 unmarked 和四处 R718 明确文本修改均可逆，新的真正职责全文包含在再生器内。输出完整1782源码，整bytes/SHA/Git blob逐项校验。它不依赖某个未公开片段。

源再生器2从完整d0fe读取全部函数；四个精确修改包含新增R723读取分支全文。正逆可以逐字还原完整原46887B父文件。原45ca/f79c不派生、不重复入库。

两参数再生器分别读取完整74,772B闭面父ready和80,089B矩父ready。全部变化有完整 before/after/path 对象，原source/数值/summary/完整历史保留。闭面父文件两处既有缩进也显式恢复，所以逆变换还原的是原始全字节，不只是同一JSON对象。每个输出完整文件都有固定bytes/SHA/blob，参数构造不执行任何科学模块。

本次实际完成了V8字符串/JSON的完整来源拼接、所有显式前后向替换及全文件hash核对。没有声称执行Python AST、compile、科学import、求解、准确积分、fixture或完整真实费用。再生器是可审查可复现来源，不是新机械admission门。

## 14. 新文件终身份

| 完整文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| fixed_fejer_R723_directional_closed_phase_grip_evidence.py | 87670 | 1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc | 94a33898b3b86646d207b3018d26069eaffd8797 |
| fixed_fejer_R723_compatible_r716_centred_volume_moment.py | 61706 | 3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b | 3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4 |
| reproduce_R723_directional_closed_source.mjs | 77961 | aba21ff140cdc85c6c5c841c2843154994cd5a505fe4ea5715dc76b1edee29c0 | eacb97180a52dfb33a3478303f0454b98bdbeb12 |
| reproduce_R723_compatible_R716_source.mjs | 19477 | f1e72d72563da39a3ccd29ec43dbdba767f56ec1ce0b6823981721d79ddbac13 | 176ab5b2b2036b0506fb627690ba92eaa29cb231 |
| fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json | 86836 | 5a072e9c1030f146f46084d3b395300f7c79b52bb0c88830a55d0b3188464d9f | 80e5cf779dbe6d8bb811561aaf55da036669eca0 |
| fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json | 97718 | 11667d388e2d71d7583891aac274cfe7ea71810b123f9262f4a8ed85e90986c3 | a5111bec896c7a83e598a9ea26f1372b80b309dc |
| reproduce_bhalf_R723_closed_parameters.mjs | 56721 | 904ba5c36b8f45b61d2f6c1bea57ecbc4824850fa006b15d2ca5bbed26a435b6 | a804f9fe6e2b0eb86ccf2f5ca7d08dc3cc550da5 |
| reproduce_bhalf_R723_R716_parameters.mjs | 74031 | c1ad3ce73d72650cadaf8ea27060e3c9aecc433f00032f538acf7975f02bb9b4 | 9bc5a0157bba62d3ae5ce6e53b4f0a335bcd9877 |

所有运行结果、准确流、normal根盒、方向范围、证据副件和矩数据仍只留在公开Actions runner。这个源码包不把任何旧运行数组或输出系数搬成新的Git参数。

## 15. 未付责任与使用次序

真正的必要顺序仍是：实际科学完整同点报告/快照，完整normal32和六jet费用，完整连续geometry，随后本R723与可选R716消费。缺任一完整输入时应保留原未付责任；没有为了本包先安排抽样、预跑或删减预算。

R723的支撑改进不能让未付的曲率、完整mean根、全域Gram、C²接合、完整相位、固定帽/握持、实际外法管、原体积解释、全十二矩、非零中心不变量或同度量收敛自动成立。当前尚无这些新运行的完整费用结果。实际有限几何改善也不等于连续证书。

本包让已有理论真正接到完整原始流和矩消费者；是否得到更强且足够的reach、held Hausdorff或$\delta_E$，只由将来同场完整实际数据和原全部条件决定。
