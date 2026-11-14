# 交接

## 当前接手、完成标准与同步

- **目标未完成：** 完整复可分无限维 Hilbert 普通 ISP；须证明每个有界算子有非零真闭不变子空间，或给完整反例。排除当前候选/完成有限模型均不等于完成。
- **负责人：** Astra-ISP-789f。根独占git、共享追踪与main推送；代理各写独占789f稿。
- **最近成功实际 pull 与已读规则提交：** `d6a19a4d9d6aedf0b5ae1b49d0f46bed125f2618`（2026-11-14 14:13:37 UTC，实际pull/rebase成功，两README差异为空）；旧库已读迁移授权 `5b8cbd10993f9e66c67e0d686c72aab113406c5b`；历次同步见 notes/2026-11-14-root-git-sync-checks-789f.json。
- **执行授权：** 每结论即推；非快进立即pull --rebase后再推，循环到成功，不force。至少每小时实际pull；逐次比对根/课题README，只读新差异并立即遵守。令牌仅CLI临时环境，不写文件/提交；只写本课题log，不写根README/LOG。
- **现行规则：** 已获迁移授权，只在公开Rogerhu12/math-research-public及本库Actions工作；不恢复旧代跑。规则12取消额外独立复核；规则13本库约4核/16GB、单job≤6h、账户并行≤20。
- **完整旧范围：** [本次压缩前H](notes/2026-11-14-handoff-before-torsion-localization-789f.md)、[此前完整open](notes/2026-11-14-open-before-kernel-standard-source-789f.md)及各自归档链保全部已付/失败/未付范围；未列不算关闭。

## 工作区与恢复

根路径 `/workspace/scratch/789f3e887d7c/math-research-recovered` 现为 `/dev/shm/isp-789f-math-research-recovered` 的软链（14:12根盘满后连Git迁移）；旧 `math-research-public` 保代理稿。12:35断连后临时盘旧Git元数据/NF/GB/DAG确已丢失；未推Green结论已由API重建818e9d7b，Garayev原文审查已推4c071886。恢复后已新建同步检出，实际git工作正常。

新T96大基/NF/DAG从本库run43597823809的artifact14114364261下载至 `/tmp/isp-t96-recovery-789f`；其中 `isp-r150-native-nf` 含原model和三DAG，`isp-r150-reweighted-graph-work/t96`含完整新图。该artifact至2026-12-14；已完成的完整目标/原17式系数均另入仓库，不依赖到期artifact。原式临时输出在 `/tmp/isp-original17-t96-output-789f`，标准来源在 `/tmp/isp-kernel-standard-789f`。

## 原模型与仍未付的主要接口

H=L²(Z₂,Haar)，Af(y)=a_v₂(y)f(y−1)，a_j=exp[−(280/3)16^j+90·8^j−300·2^j+850/3]、零点权0。A非零非紧、单射稠密像、拟幂零，W*(A)=B(H)、A′无非零紧。N_j²=η_jN_(j+1)、N_j WOT→I/2而非SOT；闭A不变M均closure AM=M，普通循环性未知。

- 原Haar慢主理想与负边界T_N/T_Y分开；后者M=kerT含e0、N=closure BM，N=M仍开。R187/200付M∩RanB^r⊂N；R239付合法d≈log^(1/3)q、c>K*权核；无权完整λ²=〈G⁻¹r,r〉增长/Σ1/[ell(1+λ²)]发散未付。
- 原graph保M3初次/M2以后、同w/同未来/真负前缀/自然逆域及完整左右费。Keff≥e^(59d³/256)/(2^19d)已付；固定测试局部Gram、pure深jet、普通右费/跨birth仍缺。primitive MP不代graph Gram，固定birth不代移动birth，全H稠密不传未知限制。
- 正常湮灭者的一般有限原秩仍开；R276同尾正完成不付全链谱/正距，R289熵o(m)仍容R291尾rank指数。完整下一尾理想距离m_j上界/单位锚未付；R272单侧修复失自伴、R280因子排除不代普通子空间。
- R147/150其余mean秩/高ess、R176部分谱、R236慢核/原右源及R268–290全部未列范围仍保归档/open，均不视为关闭；R285形式反例非Boolean。

## 一、有限Boolean费用与原连续尾

R297把全部正权/出生/高度加强κ同常数归到奇硬M=2r+1首边，真费A_U*L1L3⁻¹L1A_U≤κI，等价倒数桥B*L2²B≤κG1；真实源、完整逆/压缩和投影不可删。

- R295全正权birth1/全heightκ1024、原尾674/81；R298全独立五权K2≤743/782。R300任意旧2s＋三弱位的全三族范数极限无放大，q3/h6/全Schur与交叉已付；严格旧余量传小ε，边界不代有限内部/统一阈值。分组范围及全部原链接保归档。
- [有限a铅笔](notes/2026-11-14-finite-weak-bit-common-defect-pencil-and-coefficient-obstruction-789f-next.md)准确等价硬端；真四权排任意固定κ的P1逐系数正。[首Schur SOS](notes/2026-11-14-critical-even-pool-first-schur-sos-row-789f-next.md)尚缺相位及完整最高边联合缺陷；固定池条件不当尺寸归纳。
- [完整共同谱](notes/2026-11-14-critical-even-pool-commuting-full-grams-and-phase-moments-789f-next.md)保F/Q交换、补集T自伴、T²=F⁻¹Q、Tv=σp⁻¹D²v；压缩矩不交换，低birth nuisance不删。[奇→偶全源极限](notes/2026-11-14-odd-to-even-weak-bit-phase-limit-and-universal-hard-transfer-789f-next.md)diag(0,Q*G⁻¹Q+Z*L2⁻¹Z)证明全偶相位统一κ单独足全部加强高度，未证反向或一般κ。
- [任意四权全相位](notes/2026-11-14-four-bit-all-weight-even-phase-bound-789f-next.md)已付整个三维≤1，等权取等、最优1，完整整数多项式证书已存。[三/五位全源](notes/2026-11-14-three-site-phase-sos-and-complete-five-site-boundary-789f.md)：任意旧3权极限0<K<1；旧5权(r,r⁻¹,1,1,1)全部4维K<3/4，固定r加小正弱位后全部9维≤7/8。未付更大任意偶池/有限内部或r统一阈值。
- [全次数Johnson分拆](notes/2026-11-14-all-degree-pair-splitting-johnson-identity-and-arithmetic-obstruction-789f-next.md)保全部q与新层低投影；M24/s4算术缺陷−49588但真S1缺陷+136，只排出生一算术直推。R294共同Newton、R296完整两带/负拟合二阶差尚缺混合预算；Green–Ward保全补空间，真实非实极点排共同平方权Stieltjes，不反S1/Pick。原graph仍另开。

## 二、R150原十七式与特征零提升

原11物理N＋6Γ的M5为6188×4367、泛秩4354。rankAy8与0/2/−6/∞已闭；余rankAy9有限Σ及char0实际来源/分母。其他mean秩/高ess/自然幂另开，详细因子/数量保压缩前H。

- 原3333常预基加2195余源的NF有1034分量；完整GB1021行/次数和716，挠维315/minpoly190。九目标最小h31度24，j4/10少(s−1)；char0候选h0=s³(s−2)F+²F−²E8。原线性逆最小Dlin46次不免费降到24，模31五新增因子不当复坏点；原∞模31阶≥24不外推char0。
- [T96完整图](results/R150-appendix-complete-t96-kernel-and-exact-nine-source-identities.md)run43597823809得1021输出/1174纯核，全RC=h31T，完整gzip已存；[原17证书](results/R150-appendix-nine-targets-full-original-seventeen-equation-certificate-mod31.md)全DAG/D-content及4367×147×9原系数核清，最高135次/完整3.166MB gzip已推4e6a1539。不重跑旧图/高次DAG。
- [标准来源](notes/2026-11-14-r150-kernel-standard-source-and-bounded-lift-789f.md)九目标最小cost=[85,85,85,84,85,85,85,85,85]，最高69次；B85为54596标准NF列＋原预基162778列，共217374个char0独立整数列，219032输出。完整canonical gzip已推81356e8a；此标准列族不是全部原列。
- [原首轮残差](notes/2026-11-14-r150-first-original-padic-residual-789f.md)6.28131秒，h0 mod31=25h31，原primitive模31全真，x0 cost85/最高74次；r1有1874424非零系数。完整整数式/x0/r1均保存。
- [完整像障碍](notes/2026-11-14-r150-first-residual-fixed-source-obstruction-789f.md)轻证书1.20032秒全9 NF(r1)非零，常数项数66/64/65/67/66/64/64/65/64；原m3m6m9分量为17/27/22/26/8/6/13/16/2。全G商＋余逐项核清；单位子式严格排h0各目标在固定标准列Q像，添同标准族任意更高次数仍无效。不能排非标准来源/kernel初值或完整char0理想。
- [余类定位及h修正障碍](notes/2026-11-14-r150-first-residual-torsion-scalar-obstruction-789f.md)已2.036513秒核九余全在315维torsion，各最小ℓ=(s−1)(s−2)；2835×24系统rank24/增广25，25行显式dual仅用j2，排任意次数g且固定初值的h0+31g。乘ℓ或E8仅得未恢复cost的mod961存在性，不代char0。
- [有限β判据](notes/2026-11-14-r150-budget85-full-source-bockstein-and-saturation-789f.md)保[r1]∈imβ。[exact Koszul降维](notes/2026-11-14-r150-exact-koszul-compression-and-bockstein-1152-789f.md)现付660未选N行的Z_(31)[s]单位压缩及972低核保cost精确lift。原6188的B85有289198列，模31核71824/coker1658；70672方向β零，剩200高K的1152移位待算。有限coker不替无限G商；最终仍须原17精确有理身份。

## 原文接口与持续执行

[原文续查](notes/2026-11-14-current-isp-literature-refresh-789f-next.md)及Garayev实际可逆例的第二分支合格极限必零证明已推；Müller主条件不适配原A，Rosenblum仍需真实最终零矩。[balanced-walk接口](notes/2026-11-14-balanced-walk-two-layer-metric-mismatch-for-phase-789f-next.md)的中层多出非恒定外部权和，不能直接套跨层相位；旧快幂/Bishop/最小向量/预解范围见原档，不重复。

normal_annihilator继续char0固定预算提升；literature_audit专攻真实偶相位；boundary_core转原连续尾的完整分拆/Johnson harmonic预算，保高degree nuisance Schur。根维护证明、追踪、同步与逐结论推送。主ISP不以阶段稿收尾。

## 计算同步

- **最近 CI pull 与规则核对：** `9da7d829b4ed24357484ab5cadf038f2e553b4a3`（2026-11-14 13:10:38 UTC，实际 pull/rebase 成功，两 README 与任务源哈希一致）；R150 来源图运行 43597823809-1，真实结果见本次回执。
