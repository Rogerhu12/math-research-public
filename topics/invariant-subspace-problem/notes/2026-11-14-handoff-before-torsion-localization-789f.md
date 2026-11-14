# 交接

## 当前接手、完成标准与同步

- **目标未完成：** 完整复可分无限维 Hilbert 普通 ISP；须证明每个有界算子有非零真闭不变子空间，或给完整反例。排除当前候选/完成有限模型均不等于完成。
- **负责人：** Astra-ISP-789f。根独占git、共享追踪与main推送；代理各写独占789f稿。
- **最近成功实际 pull 与已读规则提交：** `555d4e4fa27b7fa86e22f9b4ab9c7b821d92bb10`（2026-11-14 14:05:54 UTC，实际pull/rebase成功，两README差异为空）；旧库已读迁移授权 `5b8cbd10993f9e66c67e0d686c72aab113406c5b`；历次同步见 notes/2026-11-14-root-git-sync-checks-789f.json。
- **执行授权：** 每结论即推；非快进立即pull --rebase后再推，循环到成功，不force。至少每小时实际pull；逐次比对根/课题README，只读新差异并立即遵守。令牌仅CLI临时环境，不写文件/提交；只写本课题log，不写根README/LOG。
- **现行规则：** 已获迁移授权，只在公开Rogerhu12/math-research-public及本库Actions工作；不恢复旧代跑。规则12取消额外独立复核；规则13本库约4核/16GB、单job≤6h、账户并行≤20。
- **完整旧范围：** [本次压缩前H](notes/2026-11-14-handoff-before-full-four-site-phase-789f.md)、[此前完整open](notes/2026-11-14-open-before-kernel-standard-source-789f.md)及各自归档链保全部已付/失败/未付范围；未列不算关闭。

## 工作区与恢复

根管理检出为 `/workspace/scratch/789f3e887d7c/math-research-recovered`，旧 `math-research-public` 目录保代理稿。12:35断连后临时盘旧Git元数据/NF/GB/DAG确已丢失；未推Green结论已由API重建818e9d7b，Garayev原文审查已推4c071886。恢复后已新建同步检出，实际git工作正常。

新T96大基/NF/DAG从本库run43597823809的artifact14114364261下载至 `/tmp/isp-t96-recovery-789f`；其中 `isp-r150-native-nf` 含原model和三DAG，`isp-r150-reweighted-graph-work/t96`含完整新图。该artifact至2026-12-14；已完成的完整目标/原17式系数均另入仓库，不依赖到期artifact。原式临时输出在 `/tmp/isp-original17-t96-output-789f`，标准来源在 `/tmp/isp-kernel-standard-789f`。

## 原模型与仍未付的主要接口

H=L²(Z₂,Haar)，Af(y)=a_v₂(y)f(y−1)，a_j=exp[−(280/3)16^j+90·8^j−300·2^j+850/3]、零点权0。A非零非紧、单射稠密像、拟幂零，W*(A)=B(H)、A′无非零紧。N_j²=η_jN_(j+1)、N_j WOT→I/2而非SOT；闭A不变M均closure AM=M，普通循环性未知。

- 原Haar慢主理想与负边界T_N/T_Y分开；后者M=kerT含e0、N=closure BM，N=M仍开。R187/200付M∩RanB^r⊂N；R239付合法d≈log^(1/3)q、c>K*权核；无权完整λ²=〈G⁻¹r,r〉增长/Σ1/[ell(1+λ²)]发散未付。
- 原graph保M3初次/M2以后、同w/同未来/真负前缀/自然逆域及完整左右费。Keff≥e^(59d³/256)/(2^19d)已付；固定测试局部Gram、pure深jet、普通右费/跨birth仍缺。primitive MP不代graph Gram，固定birth不代移动birth，全H稠密不传未知限制。
- 正常湮灭者的一般有限原秩仍开；R276同尾正完成不付全链谱/正距，R289熵o(m)仍容R291尾rank指数。完整下一尾理想距离m_j上界/单位锚未付；R272单侧修复失自伴、R280因子排除不代普通子空间。
- R147/150其余mean秩/高ess、R176部分谱、R236慢核/原右源及R268–290全部未列范围仍保归档/open，均不视为关闭；R285形式反例非Boolean。

## 一、有限Boolean费用与原连续尾

真实统一目标为全部正权/出生/高度的加强相邻费用。R297已同κ归约到奇硬M=2r+1首边：A_U*L1L3⁻¹L1A_U≤κI，等价互易权桥B*L2²B≤κG1；所有实际源、完整逆和压缩次序保留。未投影自然提升在真五位发散，不能删投影。

- R298全独立五权整个K2≤743/782；R295出生1全部高度κ1024；R292/293分组/单异常范围仅按原量词。R300固定旧四权＋三弱位全14维极限≤743/782，充分小ε≤1525/1564；任意旧2s池三弱位的完整三族范数极限无常数放大，旧q3/h6与全Schur/交叉已付。均不把边界换成有限内部全权界。
- [有限a铅笔](notes/2026-11-14-finite-weak-bit-common-defect-pencil-and-coefficient-obstruction-789f-next.md)准确等价硬端界；实际四权排每个固定κ的P1逐系数正。[指定首Schur行](notes/2026-11-14-critical-even-pool-first-schur-sos-row-789f-next.md)给条件SOS，尚须相位与完整最高边缺陷两个预算。
- [真实共同谱](notes/2026-11-14-critical-even-pool-commuting-full-grams-and-phase-moments-789f-next.md)：完整F/Q交换，补集连接T自伴、T²=F⁻¹Q；真V的G/L/4G+R是同一压缩，Tv=σp⁻¹D²v。压缩后矩不交换，低birth nuisance不能删。
- [奇→偶完整相位极限](notes/2026-11-14-odd-to-even-weak-bit-phase-limit-and-universal-hard-transfer-789f-next.md)为diag(0,Q*G⁻¹Q+Z*L2⁻¹Z)。全部偶临界相位统一κ单独足以推出全部奇硬及加强高度同κ；无尺寸循环、未证反向等价，也未付任何一般相位常数。
- [任意四权完整相位](notes/2026-11-14-four-bit-all-weight-even-phase-bound-789f-next.md)已证整个三维V上H0*L⁻¹H0≤I，等权取等、最优1；原完整G逆/L顶逆及物理度量均保。整数D前两主子式和行列式两乘法锥共416/3094/3849/2465正系数，完整证书已存。未外推更大偶池。
- [完整低位相位预算](notes/2026-11-14-three-site-phase-sos-and-complete-five-site-boundary-789f.md)：任意旧3权的完整下块有正平方证0<K<1且普适常数1最优；旧5权(r,r⁻¹,1,1,1)的S3标准型等价真实3位、≤25/48，结合平凡型得整个4维K<3/4 I；固定r加充分小正弱位后整个9维相位≤7/8。未付一般权/有限内部或r统一阈值。
- [全次数Johnson分拆](notes/2026-11-14-all-degree-pair-splitting-johnson-identity-and-arithmetic-obstruction-789f-next.md)保原完整q_k/q_(k−1)及新层低阶投影，准确展开全算术缺陷；等权M24/s4给−49588但真实S1缺陷+136，只排出生一算术步骤直接延拓。所需算术λ随出生至少线性，不是最优S1下界。
- R297 Green–Ward保整个补空间逆与A−/J+源度量；真实非实极点排共同平方权平移的Stieltjes捷径，不反S1/Pick。R299逐位Pick/全primitive能量不免费插L1；R294共同Newton与R296全残差两带、负拟合二阶差保完整nuisance，混合预算未付。

## 二、R150原十七式与特征零提升

原11物理N＋6Γ的M5为6188×4367、泛秩4354。rankAy8与0/2/−6/∞已闭；余rankAy9有限Σ及char0实际来源/分母。其他mean秩/高ess/自然幂另开，详细因子/数量保压缩前H。

- 原3333常预基加2195余源的NF有1034分量；完整GB1021行/次数和716，挠维315/minpoly190。九目标最小h31度24，j4/10少(s−1)；char0候选h0=s³(s−2)F+²F−²E8。原线性逆最小Dlin46次不免费降到24，模31五新增因子不当复坏点；原∞模31阶≥24不外推char0。
- [T96完整图](results/R150-appendix-complete-t96-kernel-and-exact-nine-source-identities.md)run43597823809得1021输出/1174纯核，全RC=h31T，完整gzip已存；[原17证书](results/R150-appendix-nine-targets-full-original-seventeen-equation-certificate-mod31.md)全DAG/D-content及4367×147×9原系数核清，最高135次/完整3.166MB gzip已推4e6a1539。不重跑旧图/高次DAG。
- [标准来源](notes/2026-11-14-r150-kernel-standard-source-and-bounded-lift-789f.md)九目标最小cost=[85,85,85,84,85,85,85,85,85]，最高69次；B85为54596标准NF列＋原预基162778列，共217374个char0独立整数列，219032输出。完整canonical gzip已推81356e8a；此标准列族不是全部原列。
- [原首轮残差](notes/2026-11-14-r150-first-original-padic-residual-789f.md)6.28131秒，h0 mod31=25h31，原primitive模31全真，x0 cost85/最高74次；r1有1874424非零系数。完整整数式/x0/r1均保存。
- [完整像障碍](notes/2026-11-14-r150-first-residual-fixed-source-obstruction-789f.md)轻证书1.20032秒全9 NF(r1)非零，常数项数66/64/65/67/66/64/64/65/64；原m3m6m9分量为17/27/22/26/8/6/13/16/2。全G商＋余逐项核清；单位子式严格排h0各目标在固定标准列Q像，添同标准族任意更高次数仍无效。不能排非标准来源/kernel初值或完整char0理想。
- [B85全已选来源β](notes/2026-11-14-r150-budget85-full-source-bockstein-and-saturation-789f.md)：258288原列→219032输出，模31核40914/coker1658；完整kernel移位给全核，mod961可解iff[r1]∈imβ。β尚未计算，有限coker不自动替无限G商。24未知g作用覆盖任意多项式次数；660未选N行仍另开，最后须有理重构及原17精确身份。

## 原文接口与持续执行

[原文续查](notes/2026-11-14-current-isp-literature-refresh-789f-next.md)及Garayev实际可逆例的第二分支合格极限必零证明已推；Müller主条件不适配原A，Rosenblum仍需真实最终零矩。[balanced-walk接口](notes/2026-11-14-balanced-walk-two-layer-metric-mismatch-for-phase-789f-next.md)的中层多出非恒定外部权和，不能直接套跨层相位；旧快幂/Bishop/最小向量/预解范围见原档，不重复。

normal_annihilator继续char0固定预算提升；literature_audit专攻真实偶相位；boundary_core转原连续尾的完整分拆/Johnson harmonic预算，保高degree nuisance Schur。根维护证明、追踪、同步与逐结论推送。主ISP不以阶段稿收尾。

## 计算同步

- **最近 CI pull 与规则核对：** `9da7d829b4ed24357484ab5cadf038f2e553b4a3`（2026-11-14 13:10:38 UTC，实际 pull/rebase 成功，两 README 与任务源哈希一致）；R150 来源图运行 43597823809-1，真实结果见本次回执。
