# 交接

## 当前接手、完成标准与同步

- **目标未完成：** 完整复可分无限维 Hilbert 普通 ISP；须证明每个有界算子有非零真闭不变子空间，或给完整反例。排除当前候选/完成有限模型均不等于完成。
- **负责人：** Astra-ISP-789f。根独占git、共享追踪与main推送；代理各写独占789f稿。
- **最近成功实际 pull 与已读规则提交：** `3cc607c7bee7661d194af5ec9ef047b86976d875`（2026-11-14 13:47:46 UTC，实际pull/rebase成功，两README差异为空）；旧库已读迁移授权 `5b8cbd10993f9e66c67e0d686c72aab113406c5b`；历次同步见 notes/2026-11-14-root-git-sync-checks-789f.json。
- **执行授权：** 每结论即推；非快进立即pull --rebase后再推，循环到成功，不force。至少每小时实际pull；逐次比对根/课题README，只读新差异并立即遵守。令牌仅CLI临时环境，不写文件/提交；只写本课题log，不写根README/LOG。
- **现行规则：** 已获迁移授权，只在公开Rogerhu12/math-research-public及本库Actions工作；不恢复旧代跑。规则12取消额外独立复核；规则13本库约4核/16GB、单job≤6h、账户并行≤20。
- **完整旧范围：** [本次压缩前H](notes/2026-11-14-handoff-before-standard-lift-and-phase-budget-789f.md)、[此前完整open](notes/2026-11-14-open-before-kernel-standard-source-789f.md)及各自归档链保全部已付/失败/未付范围；未列不算关闭。

## 工作区与恢复

根管理检出为 `/workspace/scratch/789f3e887d7c/math-research-recovered`，旧 `math-research-public` 目录保代理稿。12:35断连后临时盘旧Git元数据/NF/GB/DAG确已丢失；未推Green结论已由API重建818e9d7b，Garayev原文审查已推4c071886。恢复后已新建同步检出，实际git工作正常。

新T96大基/NF/DAG从本库run43597823809的artifact14114364261下载至 `/tmp/isp-t96-recovery-789f`；其中 `isp-r150-native-nf` 含原model和三DAG，`isp-r150-reweighted-graph-work/t96`含完整新图。该artifact至2026-12-14；已完成的完整目标/原17式系数均另入仓库，不依赖到期artifact。原式临时输出在 `/tmp/isp-original17-t96-output-789f`，标准来源在 `/tmp/isp-kernel-standard-789f`。

## 原模型与仍未付的主要接口

H=L²(Z₂,Haar)，Af(y)=a_v₂(y)f(y−1)，a_j=exp[−(280/3)16^j+90·8^j−300·2^j+850/3]，零点权0。A非零、非紧、单射、稠密像、拟幂零，W*(A)=B(H)，A′无非零紧。归一dyadic幂N_j²=η_jN_(j+1)，N_j WOT→I/2而非SOT；每个闭A不变M均closure AM=M（R12§5）。普通线性循环性未知。

- 原Haar慢主理想与负边界T_N/T_Y分开：后者M=kerT含e0、N=closure BM，N=M仍开。R187/200付M∩RanB^r⊂N；R239付d≈log^(1/3)q合法窗、c>K*=3(16/770)^(1/3)权核。无权λ²=〈G⁻¹r,r〉完整Schur及Σ1/[ell(1+λ²)]发散所需增长未付。
- 原graph要M3初次/M2以后、同w、同未来、真负前缀、自然逆域及完整左右费。Keff≥e^(59d³/256)/(2^19d)已付；固定测试局部Gram O(Keff)、pure深jet、ordinary右费与跨birth合并仍缺。primitive MP Gram不能替原graph Gram；固定birth不代移动birth，全H稠密不传未知限制。
- 一般正有限秩正常湮灭者仍开。R272单侧修复失自伴；R276同尾正完成不付全链谱/正距；R280可测因子/子格排除不代普通子空间。R289有限原秩尾熵o(m)仍容R291尾rank指数；完整下一尾理想距离m_j上界/单位锚缺，旧准确预算见归档。
- R147/150其余mean秩/高ess、R176部分谱、R236慢核/种子和原右源、R268–290全部旧范围仍开；原紧方法与特定弱极限失败不外推所有方法。R285非Boolean，R286固定出生不付移动出生。

## 一、有限Boolean费用与原连续尾

真实统一目标为全部正权/出生/高度的加强相邻费用。R297已同κ归约到奇硬M=2r+1首边：A_U*L1L3⁻¹L1A_U≤κI，等价互易权桥B*L2²B≤κG1；所有实际源、完整逆和压缩次序保留。未投影自然提升在真五位发散，不能删投影。

- R298全独立五权整个K2≤743/782；R295出生1全部高度κ1024；R292/293分组/单异常范围仅按原量词。R300固定旧四权＋三弱位全14维极限≤743/782，充分小ε≤1525/1564；任意旧2s池三弱位的完整三族范数极限无常数放大，旧q3/h6与全Schur/交叉已付。均不把边界换成有限内部全权界。
- [有限a铅笔](notes/2026-11-14-finite-weak-bit-common-defect-pencil-and-coefficient-obstruction-789f-next.md)准确等价硬端界；实际四权排每个固定κ的P1逐系数正。[指定首Schur行](notes/2026-11-14-critical-even-pool-first-schur-sos-row-789f-next.md)给条件SOS，尚须相位与完整最高边缺陷两个预算。
- [真实共同谱](notes/2026-11-14-critical-even-pool-commuting-full-grams-and-phase-moments-789f-next.md)：完整F/Q交换，补集连接T自伴、T²=F⁻¹Q；真V的G/L/4G+R是同一压缩，Tv=σp⁻¹D²v。压缩后矩不交换，低birth nuisance不能删。
- [奇→偶完整相位极限](notes/2026-11-14-odd-to-even-weak-bit-phase-limit-and-universal-hard-transfer-789f-next.md)为diag(0,Q*G⁻¹Q+Z*L2⁻¹Z)。全部偶临界相位统一κ单独足以推出全部奇硬及加强高度同κ；无尺寸循环、未证反向等价，也未付任何一般相位常数。
- [固定S3相位预算](notes/2026-11-14-odd-five-bit-s3-phase-trace-budget-789f.md)：旧(r,r⁻¹,1,1,1)完整二维不变源由正系数迹证K<3/4 I；固定r加充分小正弱位后完整三维S3相位≤7/8。未覆盖其它S3型或一般权，弱位阈值不宣称r统一。
- [全次数Johnson分拆](notes/2026-11-14-all-degree-pair-splitting-johnson-identity-and-arithmetic-obstruction-789f-next.md)保原完整q_k/q_(k−1)及新层低阶投影，准确展开全算术缺陷；等权M24/s4给−49588但真实S1缺陷+136，只排出生一算术步骤直接延拓。所需算术λ随出生至少线性，不是最优S1下界。
- R297 Green–Ward保整个补空间逆与A−/J+源度量；真实非实极点排共同平方权平移的Stieltjes捷径，不反S1/Pick。R299逐位Pick/全primitive能量不免费插L1；R294共同Newton与R296全残差两带、负拟合二阶差保完整nuisance，混合预算未付。

## 二、R150原十七式与特征零提升

原17式=11物理极化N＋6Γ，M5为6188×4367、泛秩4354。rankAy8与0/2/−6/∞已闭；余g≠0/rankAy9有限Σ、char0目标来源/实际分母。其余mean秩/高ess/全局自然幂仍另开。

- 原3333常单位预基加2195真实来源，NF有1034分量；完整GB1021行、次数和716。全挠空间维315，charpoly315/minpoly190；五个新增模31因子不当复异常点。原∞一阶图模31除子阶≥24，不推char0厚度；旧74次条件在31不触发。
- 九目标共同最小h31=s³(s−2)²(s−1)P+²P−²E6度24，j4/10自身少(s−1)；额外五因子与s+6不进入目标。char0候选h0=s³(s−2)F+²F−²E8仍待来源证明。线性逆最小Dlin=s⁸(s−2)²(s+6)²F+³F−³E8²度46，不能删非线性/Γ免费降到24次。
- [T96完整图与九目标](results/R150-appendix-complete-t96-kernel-and-exact-nine-source-identities.md)：run43597823809一次T96 18.705秒得1021输出/1174纯核、次数和716；九目标4.84342秒全RC=h31T，来源最高130，完整gzip已存。T64原202个非零来源输出已准确处理；不重跑旧std或高次反向DAG。
- [原17式完整模31证书](results/R150-appendix-nine-targets-full-original-seventeen-equation-certificate-mod31.md)已18.119秒完成全部原DAG/D-content恢复及4367×147×9系数核验，最高135次、5435非零原行/4452535非零系数；完整3.166MB gzip已推4e6a1539。
- [kernel标准源与B85](notes/2026-11-14-r150-kernel-standard-source-and-bounded-lift-789f.md)已6.51095秒实得最高69次，九目标最小cost=[85,85,85,84,85,85,85,85,85]，完整gzip已推81356e8a。B85余源标准54596列，加原预基为217374个char0独立原整数列/219032输出；补偿层界75/65/55/45。该最小性不免费扩到所有6188行。
- [首轮原整数残差](notes/2026-11-14-r150-first-original-padic-residual-789f.md)已6.28131秒完成，原primitive17式模31全真，x0 cost85/最高74次；mod961卷积给r1的1874424个非零系数，完整初始源/残差/整数式gzip已保存。正在求同固定列correction，未有mod961身份。单位大子式保证Q31解若存在必整；失败只排固定列，有限成功位数不代char0，最终须有理重构及原17精确身份。

## 原文接口与持续执行

[原文续查](notes/2026-11-14-current-isp-literature-refresh-789f-next.md)及Garayev实际可逆例的第二分支合格极限必零证明已推；Müller主条件不适配原A，Rosenblum仍需真实最终零矩。旧快幂/Bishop/最小向量/预解路线的准确适用范围见原档，不因新搜索重复已排结论。

normal_annihilator继续char0固定预算提升；literature_audit专攻真实偶相位；boundary_core转原连续尾的完整分拆/Johnson harmonic预算，保高degree nuisance Schur。根维护证明、追踪、同步与逐结论推送。主ISP不以阶段稿收尾。

## 计算同步

- **最近 CI pull 与规则核对：** `9da7d829b4ed24357484ab5cadf038f2e553b4a3`（2026-11-14 13:10:38 UTC，实际 pull/rebase 成功，两 README 与任务源哈希一致）；R150 来源图运行 43597823809-1，真实结果见本次回执。
