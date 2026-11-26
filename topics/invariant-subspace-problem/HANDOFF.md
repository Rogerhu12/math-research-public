# 交接

维护：`Astra-ISP-347c-20261126`（AI-assisted GPT-6 Astra Pro）；从已推送的 `Astra-ISP-b2a9acde-20261120` 接续，后者接续789f。

## 主目标、规则与执行

- **普通复可分无限维 Hilbert ISP 未完成。** 完成标准仍仅全体有界算子的存在定理或完整反例；子结果不作完成。
- **最近实际 pull / 已读规则提交：** `1be726e03e13f455d131458d45121a9dfbb9488d`（2026-11-26 05:24:55 UTC）。本次两README无新规则差异；已读根/课题README、H/open、结果索引及定点log/notes。每次pull及至少每小时比diff，记录SHA。
- 私库 `QUEUE.md` 已成功更新认领，提交 `e776df496eedfa449b0475cefe140fdae7023db4`；非快进已逐次pull --rebase后重推成功。研究在公开仓库，私库仅维护QUEUE；不force，令牌仅CLI环境。
- 本地部分克隆已恢复；`/tmp/isp-347c05929dd3/math-research-public`。workspace磁盘不足已换TMP，不影响研究。root独占git/H/open/results/log；子代理只写各自TMP草稿。每个完整结论单独推送，计算只留源码/参数/身份/SHA，无数组。
- 全部旧状态、来源和失败范围保[接手H快照](notes/2026-11-26-handoff-at-takeover-347c.md)及原归档链。MD<100KB、H<10KB、open尽量<30KB、topic<200MB；不写根LOG。
- 请求14现已确认run44738311930成功（2026-11-20 12:44:31–12:44:58 UTC，head71e86b47cb04a2fffe6ee39331f660feb954ae0d）；四标签的具体输出仍待回收并写正式证明。311型旧run44737710336中单标签成功不等于全workflow成功，原身份保留。不得重跑已闭计算。
- 当前并行：311及请求14秩一除子型完整证明；unit3+1真正一般图；R271真实源加权费用。父代理回收权11与文献状态，不把成功执行当成数学目标成立。

## R150：原Bell非零临界点与全部来源

- 原W31/W127、Γ120、权7–10及来源范围已登记，不重算。ΓE10=13697、δ14b²非成员、μ10核2171全Koszul；200/120核111/31，旧run43926933406身份已恢复。
- [权11–14严格上界](results/R150-appendix-original-koszul-two-cycles-and-weight-eleven-through-fourteen-rank-ceilings.md)36782/90012/203542/430212；qb³/b⁴/δb³新负门36783/90013/203543。四q联合门36786，未有完成的新大矩阵秩。
- **权11请求3已结束，待回收完整输出：** run44732018666/job136273939599于2026-11-20 16:03:56 UTC完成，workflow success；完整原200生成元/8037189项、150646行/37568源和四规范q·b³；固定40000行投影只给秩下界。native14400秒、job345分钟，每30分钟真实pull比规则。首两run的日志参数/FLINT指数类型问题均修复并保身份；新精确整数控制在父重建前核，旧权10矩阵不重算，数组只TMP。
- **全essT3≤3的原matched Bell已零。** W±上确有Cat3真临界点，不能把该层宣空；一般V非零Bell非零只能ess4/5/6。
- **[整个V0临界层的三个原Bell均零](results/R150-appendix-zero-third-cumulant-all-matched-bell-values-vanish-and-exact-index-three.md)：** 无Cat/H秩/ess/支撑限制，含y0。原highest解H(y)，完整17低梯度I0有(r·y)S_r²∈I0，乘Q_r得S_r³；run44732550495全792×3 QQ回乘0。平方非成员给每个原根准确指数3；不搬成全Jacobian同幂，degree9无需运行。另V0/ess4整层已空的更强几何结论保索引，不把ess5/6宣空。
- **外均值ess4主支：** Cat(y)=3、dimW4、y∉W，唯一原length5代数保同L,ν及全jets。全部rankH3、全部rankH4 proper局部单零（长度2–5）、孤立零点加unit单四jet/两个双点均已空。包括半权、零权、零配对、合流及∞，正式源与执行身份见索引和前H。
- **unit3+1孤立零点：** 全p0、半权、alpha0、q0及gamma0均闭，正式稿见索引；q0商代数源run44737710336全通过，1.484秒，旧超时身份保留。真正一般图p q alpha gamma均非零、b≠1/2；已从原方程付s≠x、p0、n0、m及T=2x²−b非零。继续低阶原迹相容与全部mean，不把剩余一般支判空。
- 孤立零点的unit2+1+1、unit1⁴，全部rankH5单位支，一般V≠0 inner mean和ess5/6仍开。inner不能从V自己低秩自动推y/H共同支撑，全部原低梯度仍保。
- **rankV1：** 自身五重均值极线整支已空，run44736004677固定160阶mod103=27与∞4阶77，特殊s全保。新Δ_s³(q_s/Δ_t)源run44737710336完整通过，QQ248→184、固定368阶mod1009=774、所有边界及四T3=0幸存族核全，待独立正式稿。Δ_s⁴Δ_t/Δ_s³Δ_t²的固定440/480阶已非零，但s=-1实度降到12/24，旧16/32断言失败；修真实度后重核完整边界。其他V1及高秩V仍开。
- **[旧纯三次判据已修](results/R150-appendix-polar-pure-cube-sign-correction-and-exact-resultant.md)：** 正确Q=B³−27A²D，root同一BigInt函数全10阶整数结式260758295153015625（mod103=56）；旧正文/Python源同步更正。无纯三次结论保持，旧正号/数值不再作证，其余闭几何不重跑。
- 原4212来源枚举/系数高度、全局Bell自然幂及完整算子桥仍开。图册须每图真实幂来源并N=1+Σ(Ni−1)粘合；几何覆盖、V0子层证书不代全局原来源/实际费用。

## R271：同w的实际完整源费用

M=kerT、N=closure BM；N=M未证。始终保same-w/u、全部partial、真intersection旗、MP自然域、负前缀/未来/carry与真帽外投影。旧τ14/Bessel、PV−PK能量、一次MP与各低旗预算只保原范围；核外第二逆/任意kernel-input未付。

- [纯远孔完整Galerkin/MP](results/R271-appendix-dual-tower-kernel-only-error-pure-far-height-representatives-and-joint-reciprocal-budget.md)及[分离高度门](results/R271-appendix-separated-height-bands-exact-full-head-bessel-and-d-sized-prefix-budget.md)：m∈4ℕ≥20、d=2^m、R=d、Q=4d，允许上半高度带的全β行Bessel1；非零同w锚必要Σκ⁻²有限。增长R/Q必须重新核原母窗，不能移用旧帽。
- 原forcing准确是最低整数坐标f1=e1⊗Ω，Ce1=e0、Ce0=0；实际C²f1=0。它不同于任意物理一孔列，后者不能套该低真旗前提。
- N/Y、偶R/奇r全MP至多最高t⁻¹，新增秩全一阶；偶r可t⁻²。旧/参考头相似e221a/e441a给883a费，原−logt主阶1400a。实际源若≤Lt²、logL=o(a)才有517a余量，这个全源条件未证。
- [精确源极点](results/R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md)：K=kerX0、E1=P_cokerX0 X1|K、F0=kerE1，E1*q₋₁=P_K(f−H0a0)。有界恰退化全K-Galerkin解属F0；O(t)还须ξ0=0且P_Kξ1=0。固定E不代移动谱投影。
- **[任意奇高度全Hankel合同/高孔费](results/R271-appendix-general-odd-height-hankel-congruence-and-complete-high-hole-cost.md)：** m≥5、偶R≥d、任意奇r，全部长短坏链和旧真A幂旗保留；A0=min(max(0,(R−n−r+3)/2),m+(R−d+r+1)/2)。全q₋₁≤C_mr4^Ry^(2(d+r−3))s^(2A0−m−R−r+1)γ^(A0−1)Zγ；C_mr全阶乘/exp(12r²/n)明确、原s*=e⁻¹⁰⁷⁰缩放有效。非正交还原只付一次κ；实际γ<1/16加权Zγ仍开。
- **[全区间正则界](results/R271-appendix-complete-highest-carry-linear-graphs-and-full-interval-regular-cost.md)：** 真核/余核是固定自由块⊥底坐标I的线性图，Π′、Q′≤2L；全0<t≤1有q−t⁻¹q₋₁的明确K0、h、h1、L费用。有效半径已付，粗费用仍大，需实际源/导数或孔相关乘积。
- **最高单位不变、辅助分级及S一致真旗费已证，见索引两完整稿。** U(A)不改原完整F0；规范方向真极限以cyclic维数补齐。保原Gram的K_D有S/R无关正谱界及辅助带宽n−1，Chebyshev源尾合法但粗条件数只允γ近1；四头相关式阻止免费删混级费。原最低列完整Schur另给ξ0≤1600Kflag³，对0<S≤1成立，Kflag=e221a4^Ry2d[(90m6)^(2d(d+1))+27(n+2)³2^n]。这是无权64^R费；真正加权Zγ继续，不能替换Galerkin压缩逆。
- 小头m2/R2 κ²<e⁻²⁰⁰⁰、m3/R0/r3 κ²>e³⁸⁰⁰⁰且极点非零，均非旧联合窗；不能逐级外推。原m3高孔/一般r3已闭范围保前H和索引，不重算。
- 全部返回接口继续：旧carry真实源、完整负部合并与同w倒数和、核外第二逆/第三旗、帽逆伴随后误差。固定公共多项式塔的指数障碍只排原家族，不排实际源专属lift；不能以小残量、另一个核或任意有限层替换原项。

## 原Deddens与变化来源

- 全D_A/shift/core/copy/负幂/平均的已证范围见索引及前H。D_A localizing但范数不闭，统一c族非localizing，范数闭包无非零compact；勿重复套缺假设判据。
- 任意D_A同最优c可由有限头下三角SOT逼近；固定c球的有限输入像弱紧=有限头像norm闭包，有限插值费若有限可达。任意目标有限费仍未证。
- 全交换子单位球是原多项式单位球SOT闭包；特选同头C/ΠC同趋X、op差零且最优c1。一般Π在统一c球仍不强连续：B_m op→0,c≤2而ΠB_m→−I/4，不能自动平均任意D逼近。
- 负幂域与c等距共轭保留，真实u_n=Φ⁻ⁿ(R_n)u_(n−1)。硬/软copy五次费用障碍只排原家族。当前变化来源凸最优费、未知不变M被D核心保持、∩A^kM稠密的增长预算均仍开。
