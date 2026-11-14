# 交接

## 当前接手与规则检查点（2026-11-14）

- **目标未完成：** 完整复可分无限维 Hilbert 普通 ISP；README 完成标准不变。
- **本轮负责人：** Astra-ISP-789f。根独占 git/追踪/推送；代理只写各自 789f 笔记。
- **最近成功实际 pull 与已读规则提交：** `a66ed0c53721242925e49cfcc641fa5a6bf4ec3c`（2026-11-14 07:17:06 UTC，实际pull/rebase成功，两README规则差异为空）。旧库最后已读迁移通知为 `5b8cbd10993f9e66c67e0d686c72aab113406c5b`；从现在只在新库工作。
- **授权与执行：** 结论即推；拒推立即 pull --rebase/retry 到成功，不 force。至少每小时实际 pull，逐次比对两 README，只读新差异并立即遵守；令牌仅临时 CLI，不写文件。只写本课题 log，不写根 LOG/README。
- **现新库规则13/14：** 只在公开 `Rogerhu12/math-research-public` 工作；本题计算用本库自己的 Actions，可直接写 workflow。旧代跑runner/ci-queue不恢复；所有公开文件不得带凭据。新规则12继续取消额外复核流程。
- **工作树：** `/workspace/scratch/789f3e887d7c/math-research-public`。旧临时树不在；丢失正常预对偶修正已重建 R272，丢失两异常位完整 MP 已重建 R273（148 有理例）。
- **完整旧范围：** 本轮压缩前 [HANDOFF](notes/2026-11-14-handoff-before-R285-789f.md)、[open](notes/2026-11-14-open-before-R285-789f.md)；更早 1cf/0c 的队列和链接均在其中。未列接口没有关闭。

## 模型及不可越过的范围

原 Haar 模型 H=L²(Z₂,μ)，Af(y)=a_v₂(y) f(y−1)，a_j=exp[−(280/3)16^j+90·8^j−300·2^j+850/3]，零点权0。A 非零、非紧、单射、稠密像、拟幂零；W*(A)=B(H)，A′无非零紧。N_j=A^(2^j)/||A^(2^j)||，N_j²=η_jN_(j+1)，N_j WOT→I/2、非 SOT；每个闭 A 不变 M 都有 closure AM=M（R12§5）。一般线性循环性未知。

原 Haar 慢主理想 S_N/S_Y 与负边界 ℓ²(N0) 上线性 T_N/T_Y 分清；后者 M=kerT 含e0，N=closure BM，目标 N=M。primitive 真 MP Gram 与原 graph Γ=𝒯*𝒯 不可替换。全部原同源/未来/负前缀/自然域及正常预算保留；全H稠密不自动传未知限制，UHF/C 不运输未知 Haar 格。

## 1. 正常主理想与普通不变空间

- **R272/274：** 固定 q=2^P 的 raw 远尾修正迹范数→ρ，保 A′泛函/迹/固定边缘，但非零 C=P0CQ 必失自伴且至正锥距离||C||₁。整个 A′ 有实际 S 的 q 项尾基；前 q−1 raw 矩零后第 q 矩恰−νQ_P≠0。原 SA′零式归 νQ_P C_P=0，不能免费消最后一阶/移动 q。
- **R276：** 固定同一正尾 ν 的正头完成 X=√νK√ν，w(K)≤1/2；原正常商零式保 ν(Z²−t) 与 νZ+X+X*t 两项。X 集迹范数紧及精确对偶已付；仍须同一实际 ν_m 全链的排除证书，不能删正常预湮灭商内非零缺陷。续稿 `notes/2026-11-14-normal-cross-level-continuation-789f.md`。
- **旧正常范围：** R235/237/255指定正态类、R228实化/增秩、R229纯化失败及R230/244/267正常预算的全部精确范围保本次压缩前H/open。一般正有限秩仍开；真ann迫q_m↓0，δ无速率，hp/vp不换，保锚源/共同图未付。
- **R280（已推）：** 任意 a.e.有限可测复权的非零加权因子不变空间必 H；闭逐点子格、相位共轭保正投影因此无真不变值域。每个非零轨道生成 H 的闭子格，未证线性循环。
- **R282（已推8944064）：** [完整证明](results/R282-complete-multiplier-stabilizer-classification-and-finite-head-splitting.md)。全部单向稳定复乘子自动自伴（实际 AM 稠密、torsion Fourier）；非零真 M 的该代数恰有限低头，M=完整头⊗尾V且尾V稳定乘子只有标量。任意非有限柱复乘子稳定即排真；一般 M 仍开。代理继续尝试从实际正常见证产生这种乘子。[附录](results/R282-appendix-actual-moving-commutant-sources-and-nonvanishing-normal-error.md)已付：纯高尾弱*聚点仅标量；真R_m∈Acal一致有界且R_m−M_c_m强→0，但(N_m−M_q_m)R_m范数在固定f上趋√2||f||、WOT→(2i/π)I。固定乘子若在全M由交换子极限得到则只能标量；不能靠删移动源误差保正常迹锚。

## 2. 实际边界、相邻 Gram 与下一证明

- **原 N=M：** R187/200付 M∩RanB^r⊂N；R239付 d≈log^(1/3)q 的完整合法窗、c>K*=3(16/770)^(1/3) 权核及真 D 尾常数 K*/2。无权 λ²=〈G⁻¹r,r〉须完整 Schur；Σ1/[ell(1+λ²)] 发散足，但无权增长仍未付。
- **原 graph 接口：** M3初次、M2以后、同 w/真负图/完整左右费必须保。双宽有效 Keff≥e^(59d³/256)/(2^19d)、真实同余商测试族及主配对已付，固定测试局部 Gram O(Keff)、pure 深 jet 总费与普通右费继续。原连续尾 birth1 全高度条件数≤(t+1)^17、D1*旧列≤(h+2)^61S；birth≥2及 Γ跨birth仍开。完整公式/原链接在 open 和本次归档。
- **R277：** 原连续尾全部 ℓ1 一孔行 κ_c 可下降零源商 iff c=λb，甚至模任意 K≤d−2 前缀亦同。非比例有完整 d−1 头泄漏；C=Σb³E 未压缩 graph 小范数不付商作用，需要带真实修复。
- **R273/275：** 两异常位完整3D/4D MP、任意一位添加全高度同源三角 Schur/顶硬端、实际同一三次桥 B 的创新已付。两对角可继承，交叉仍须实际正块。首边准确三块 M(t)≥0；S1/S2 加旧下出生第二边足所有 t 的 SOS，S1/S2 一般未证。大添加位上左必要块、联合占据四项已付。
- **R278：** 实际两带 Serre 三阶递推、真实顶积分及跨birth加权迹身份已付；各桥在变化 G_k 度量为正，不免费改为 G1 序。
- **R279：** X_n≥I+(n/r)(X_r−I)适用完整有限合法与无限ℓ²真MP；首边sδ≤1/(2√2)、原尾s≤(m+1)/(6√2)得c1。一般硬核余 M*M≥(L*L)²−2L*L−I仍缺；全annihilator非Boolean锐例不能代硬核。
- **R281：** 全出生首边与全部高度最优普适常数相同，有限强权可回传严格违反；等权中央边迫C≥1，八位(4,4,1,1,1,1,1,1)首比22801/43836>1/2，未证上界1。
- **R283：** 真实惰性反对称对把全部真MP/Γ精确嵌到任薄1/2<sδ<1/2+ε且δ任小的带内，出生费用不能删；该带已含一般常数难题。
- **R284（已推）：** 两个真实跨birth零模Gram把Q/Δ接到联合M能量，Γ2≥4Γ1−2I+Γ2 B_s B_s*Γ2+R Y3†R*；有限正权p≥2零模压缩严格正。另Fischer余量2/(M−1+2s)及局部物理F/单I的无外尾coercivity已付，J*e_I仅得Ran X^(1/2)和逆平方根能量。完整首边平方下界、S1/S2及原graph识别仍开。
- **R285（已推e7cca4f）：** 明确标量正数据及x≥4参数族满足旧普通边、仿射界、两个R284严格零模块和粗占据界，却使两条更强S1/S2费用无界。只排该有限形式推理，不是Boolean反例。续逐坐标真实creation/Gauss系统。
- **R286（已推a66ed0c）：** [完整证明](results/R286-fixed-source-l1-zero-mode-energy-and-uniform-all-height-tail-bounds.md)。双锚coherent常数与真实ℓ1 creation合成付固定有限源逆平方根能量，原慢尾全部height统一且原幂几何和已付。实际t_q只含祖先birth≥q−d+i+2；q>d+s−2时固定birth s塔分量为零，所以不能据此删除跨birth graph费用或推出N=M。
- **R287（本提交）：** [完整证明](results/R287-two-sided-moving-character-limits-and-nonperiodic-disk-source-budget.md)。真R_n和伴随均强近移动c_n（非共轭），R_n² WOT→I而N_nR_n²→−I/2。任意可和闭单位盘逐位参数的平方来源，B≤b·2^(4m)、b<770/64时真空比≤2exp((m+1)/2−π2^m/16)，无周期/最高位限制；未控全部κ_m或原有限秩见证。
- **代理后续：** boundary 转R273真实两异常位4D相邻序，literature 续S2逐物理坐标；normal回实际固定秩ν_m全链；R271 已闭任意 birth1 首/末边、两组＋一位等，不重复成新缺口。

## 3. R150 与其他主接口

R150 的 Cat1/2/3 且 essT3=3 临界与全部 rankAy8 自然点已分类；余 g≠0、rankAy9 的有限 Σ 未清。原17式未平移参数域 slimgb/lift 脚本已保存，特征0须验证原 I*C=T 及实际分母；32003仅发现。旧代跑停止后曾改本环境；现已启动本库自有 Actions。官方 Singular 4.4.0 静态包已装入 `/tmp/isp-789f-singular-runtime/singular-4.4.0`；本地特征0在06:46:36于BEGIN_BASIS后异常结束，旧版未记录信号，exitCode=null且无证书；原回执已保存，不能定因。本地32003因1GiB内存上限明确失败，无证书，回执已保存。新自有工作流 `.github/workflows/invariant-subspace-r150-parameter-ideal.yml` 运行43568673309的特征0/32003仍在计算，输出在notes/r150-actions-789f及artifact；330分钟计算/350分钟整job，原身份和分母判据不变。日志已记可能数小时的计算需求。入口 `notes/2026-11-14-rank-one-parameter-ideal-ci-plan-789f.md`，逐目标 gcd 分母覆盖有证明；不得用 GB 分母代原 lift 分母。

R176有界部分谱、R147实奇次/负正辅助、R236已排原指定慢二次全核与全部旧行/种子、R268–270快辅助/共振/不交乘积仅在原范围；一般慢Bell、自然幂/实际逆、双无界及共同自然域仍按 open。R12/R14指定紧夹积/硬截断失败不排所有外部紧交织。

**持续执行：** 每个完整结论立刻单独提交推送；H随状态更新。原计划与各恢复点保档，完成标准未降低，不以阶段稿收尾。
