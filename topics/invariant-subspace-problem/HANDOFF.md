# 交接

## 当前接手与规则检查点（2026-11-14）

- **目标未完成：** 完整复可分无限维 Hilbert 普通 ISP；README 完成标准不变。
- **本轮负责人：** Astra-ISP-789f。根独占 git/追踪/推送；代理只写各自 789f 笔记。
- **最近成功实际 pull 与已读规则提交：** `91bb1fbf6010adea6b75c4dc5f86a7625e5ca382`（2026-11-14 12:30:15 UTC，实际pull/rebase成功，两README规则差异为空）。旧库最后已读迁移通知为 `5b8cbd10993f9e66c67e0d686c72aab113406c5b`；从现在只在新库工作。
- **授权与执行：** 结论即推；拒推立即 pull --rebase/retry 到成功，不 force。至少每小时实际 pull，逐次比对两 README，只读新差异并立即遵守；令牌仅临时 CLI，不写文件。只写本课题 log，不写根 LOG/README。
- **现新库规则13/14：** 只在公开 `Rogerhu12/math-research-public` 工作；本题计算用本库自己的 Actions，可直接写 workflow。旧代跑runner/ci-queue不恢复；所有公开文件不得带凭据。新规则12继续取消额外复核流程。`0c17ddf2`新增表列课题/规矩1、13扩范围，`ee26c0a6`仅改另题标题，均已读，ISP标准不变。
- **工作树：** `/workspace/scratch/789f3e887d7c/math-research-public`；旧R272/273已重建推送。历史只读副本移至`/tmp/isp-789f-old-math-research`以释放共享磁盘，全部保留；公开库Git元数据因共享盘满移至`/dev/shm/isp-789f-math-research-public-git`，原`.git`指针可正常工作。
- **完整旧范围：** [此前H](notes/2026-11-14-handoff-before-general-three-weak-789f.md)与[open归档](notes/2026-11-14-open-before-general-three-weak-789f.md)保完整范围；未列接口不算关闭。

## 模型、主缺口与所有旧范围

原H=L²(Z₂,Haar)，Af(y)=a_v₂(y)f(y−1)，a_j=exp[−(280/3)16^j+90·8^j−300·2^j+850/3]，零点权0。A非零/非紧/单射/稠密/拟幂零；W*(A)=B(H)，A′无非零紧。N_j²=η_jN_(j+1)、N_j WOT→I/2非SOT；每个闭A不变M均closure AM=M（R12§5），普通线性循环性仍未知。

Haar慢主理想与负边界ℓ²上T_N/T_Y分清；后者M=kerT含e0，N=closure BM，目标N=M。primitive MP Gram不替原graph Γ=𝒯*𝒯；同未来/同源/负前缀/自然域/正常预算不删，全H稠密或UHF模型不运输未知Haar限制。

- 原N=M：R187/200付M∩RanB^r⊂N；R239付d≈log^(1/3)q合法窗和c>K*=3(16/770)^(1/3)权核。无权λ²=〈G⁻¹r,r〉须完整Schur；Σ1/[ell(1+λ²)]发散足，增长未付。
- 原graph仍须M3初次/M2以后、同w、真负图及完整左右费。Keff≥e^(59d³/256)/(2^19d)已付；固定测试局部Gram O(Keff)、pure深jet、ordinary右费、跨birth合并缺。R294 birth1尾多项式预算不支付这些缺口。
- 正常路线：R272/274 raw修复失自伴，R276同尾正完成不付全链谱/正距；一般正有限秩、同ρ/hp/vp/原右源/单位费仍开。R280排可测加权因子/闭子格，R282稳定代数恰有限低头，移动源正常误差不消失。
- R291头矩独立给op-Schmidt≥2^M/尾rank≥ceil2^(M/2)，仍容有限原秩尾熵o(m)。正谱压缩付ε_(j+1)≥[128(1+m_j)]⁻²、liminf m_j√ε_(j+1)≥1/16；完整下一尾理想距离m_j上界/单位锚仍缺。
- R147/150其他mean秩与高ess、R176部分谱、R236原慢核/种子、R268–290全部旧范围及原紧方法边界，均保此前H/open和索引。未列仍开；R285非Boolean，R286固定出生不付移动出生。

## 1. 当前硬端证明线

M=2r+1，U=K_r、V=K_(r−1)、G1上第一Gram、Lj下MP Gram、B三次桥、A=Σbi⁻¹Ei。R297同κ归约保完整跨出生/a⁻¹抵消：全部正权/出生/高度加强κ⇔奇数硬端首边同κ。真实目标
A_U*L1L3⁻¹L1A_U≤κI，且Δ*G1=−L1A_U；倒数桥为B*L2²B≤κG1。两个自然未投影提升真五位发散，不能删原投影或压缩逆。

- [R298全独立五权](results/R298-five-independent-positive-weights-birth-two-hard-top-strengthened-s1.md)整个K2费≤743/782，缺陷≥39/782；79完整对称整数轨道，保真实负项。原birth1全height已由R295付统一κ1024；R292/293分组/单异常范围保此前H，不外推一般权。
- [R300七位三弱位](results/R300-seven-site-hard-top-strict-boundary-region-with-three-simultaneous-weak-sites.md)：任意固定旧4正权/弱3内部权，全14维极限≤743/782；充分小ε时全源≤1525/1564<1，阈值不宣称全权一致。
- [R300任意临界池三弱位](results/R300-appendix-arbitrary-critical-pool-three-weak-site-recursion.md)：旧2s位加3弱位，完整上源(U⊗K1w)⊕(V⊗W2)⊕(W⊗W3)，倒数低源X=kerA⁴|O_s、Y=kerA²|O_(s−1)。真正范数极限是diag(I_U⊗Kweak,K_old,s−1⊗Rw*Rw,K_old,s−2)，无常数放大。q=3旧h6项、整个cokernel Schur和所有交叉已付；非严格极限不代有限ε同界。
- 同稿给真实联合列M_t=J2 C2G1−J3 L3⁻¹δ*G1，M_t*M_t=旧首加强费，且M_tf=P_kerd⁴[(d*)²F_t⁻¹f/2+(d*)³F_(t−1)⁻¹dF_t⁻¹f/6]。加权不交容斥与Aq_j=−j(j+1)q_(j+1)付共同抵消。[有限a完整铅笔](notes/2026-11-14-finite-weak-bit-common-defect-pencil-and-coefficient-obstruction-789f-next.md)现给全硬费≤κ当且仅当Pκ(t)=P0+tP1+t²diag(0,L,0)正，保两个源度量。P0恰旧首加强缺陷；实际旧四权(r,r⁻¹,1,1)使P1正所需κ≳r²/4，任何固定κ的逐系数法均失败。继续联合半线平方，负系数不是完整硬费反例。
- [R297 Green–Ward](results/R297-appendix-physical-green-ward-cancellation-and-full-complement-schur.md)：真顶输入T:V_a→U、TT*=硬费，T=(4PHR*−G1PKR*)/6。固定无权源配对Tform=−εp J_q*Cinv_11/3，Cinv为整个补空间逆，上下源度量A−/J+均保；统一正预算仍开。
- R299逐位内函数给同物理Pick Gram/全birth能量，真三阶dual塔非实根排标量Newton捷径；不免费插L1。R296完整低阶回归、共同Z/两带/负拟合二阶差及出生二ridge已付，混合二阶预算仍开。原graph未由这些有限模型关闭。

## 2. R150 原参数模与准确检查点

原17式=11物理极化N+6Γ；原M5为6188×4367、函数域秩4354。全部rankAy8与0/2/−6/∞已闭，余g≠0/rankAy9有限Σ、char0 IC=T及实际分母；其他mean秩、高ess与全局自然幂/实际逆另开。

- [全NF](results/R150-appendix-native-layered-normal-forms-for-all-original-parameter-sources.md)54.8127秒/512MiB完成2195来源/9目标、1034分量/最高45次；全原来源DAG保留。[完整GB](results/R150-appendix-complete-native-polynomial-basis-and-finite-torsion-space.md)184.148秒给1021基、最高8次、总716；全部torsion NF≤7，状态维820。
- [全挠空间](results/R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)2.084秒得观测秩505、W维315、CW=0/AW=WJ和九目标坐标；压缩状态/来源在notes。charpoly315/minpoly190，另五个不可约因子共60次支撑且各平方；只是模31，E8与旧点碰撞，不是复参数异常点。
- [九目标](results/R150-appendix-nine-original-targets-exact-mod31-annihilator-degree24.md)共同最小Ann h31=s³(s−2)²(s−1)P+²P−²E6度24；j4/10少(s−1)度23。额外五因子与s+6均不进入任何目标。候选h0=s³(s−2)F+²F−²E8仅待char0证明。
- [完整基系数](results/R150-appendix-explicit-degree49-target-basis-coefficients-and-source-replay-bound.md)已核全部1034分量GQ=h31T，Q最高49次/342321非零系数，压缩完整保存。原源无相消上界26265不是实际次数；[实际反向前缀](notes/2026-11-14-r150-actual-reverse-prefix-checkpoint-789f.md)已完成976/2195来源、实际来源次数1018/中间2862，52.055秒保存checkpoint，未全展开，停止续跑该配置，转低次数直接lift。
- [移位来源图](notes/2026-11-14-r150-shifted-graph-low-degree-lift-789f.md)给2195原图列的六组移位弱Popov与严格低次数条件：若全量1021输出主元/1174真零关系成立，则九目标原源系数≤114−δ、主体≤69，接常预基≤104。唯一50.386秒前缀672列、81来源主元全输出零；尚未全量，拟发本库一次1800秒/4GiB原生任务。
- [特征零线性块](results/R150-appendix-exact-characteristic-zero-linear-divisor-and-minimal-inverse.md)精确Dlin=s⁸(s−2)²(s+6)²F+³F−³E8²度46；单位双核补给全部9阶gcd及横向逆最小分母，h0是其真因子。非线性项/Γ不可删，不能由一次线性逆免费得到24次预算。
- [∞一阶图](results/R150-appendix-original-infinity-jet-and-mod31-determinantal-thickness.md)保原全部6188来源，常数秩4340/连接秩4，模31∞除子阶≥24、齐次总度≥339。不给char0厚度或未算高阶上界；原74次条件准则在31不触发。整个除子与目标Ann分开。
- **运行与恢复：** CI43588728414于11:41:15 exit124，实到BEGIN_BASIS；输出在notes/r150-module-actions-789f/43588728414-1/char31，当前无远端长任务。原生完整结果另付，不重跑旧std。大NF/GB/DAG在/tmp/r150-native-nf-all-789f、/tmp/r150-native-gb-full-789f；全状态及Q有仓库压缩副本。反向前缀在/tmp/r150-reverse-actual-prefix-789f。

## 持续执行

boundary_core继续有限a共同缺陷；normal_annihilator转有次数约束的原来源/char0提升；literature_audit继续实际正Schur预算与定向原文核对。根独占追踪/git，结论逐条立即推。所有旧接口、失败范围与完整链接按前H/open保存，普通ISP完成标准不变，不以阶段稿收尾。
