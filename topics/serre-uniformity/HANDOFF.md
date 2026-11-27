# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：c64c683782af9d560c6f84f2d31edfbedd5786a5**（2026-11-28 03:36 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull 2026-11-27 01:48 Asia/Taipei；2026-11-28 03:27重试执行器仍报无可用环境，shell未启动。按根规则8连接器同步、读diff、expected_sha非force提交，拒绝立即同步重基重推至成功；环境恢复立即pull --rebase。下一次真实尝试不晚于2026-11-28 04:27。令牌只CLI。数学程序仅本公开仓库Actions；本地/V8仅metadata/文本，不作数学计算。[此前偏差纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-forced-Manin-and-Lame-boundaries.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：完整一般 p；原单位与实际 cochain

[R1003](results/R1003-global-scope-and-remaining-branches.md)保全部N_ns主范围；R317的整j/固定K/σ1/二三小域及小惯性C³均不可删。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)原good≥floor(p/16)+3、forced Ω(p/logp)，完整T链预算不改1/16。候选O(p^1.5logp)和有界惰性CM不推Q-CM，单cusp无Runge。

[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)已付同时非零/localization、导子和判别式，选素界仍不够小；[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)分母annihilator允许−1modp整支。几何Weil零不消HS混合项。

[原整K₂](notes/2026-11-27-original-cuspidal-K2-torsion-and-odd-Jacobian-obstruction.md)残余μp⊗J(K)[p]、全cusp Δ分裂及[整p Chen/Ohta](notes/2026-11-27-original-prime-p-Chen-isogeny-and-odd-torsion-reduction.md)均已付；Σ(p²)[p∞]=0不消非Shimura odd。R1131 forced r=p−1−2j及两Bernoulli门锁实际非分裂rank2/Fricke+，radical β_(4j+2)而非βr，规范K₂角色2j+2零。R1132低偶r两Bernoulli门迫full块w负、原正商该p块零，规范K₂角色2−r零；r2需p∤Bp−3，p7mod8指定低偶r无条件。只运输已证明的简单socle/整torsion，不代K₂/p。

[原整单位关系](notes/2026-11-28-original-integral-Manin-relations-and-cusp-constants.md)仅将原单位符号格中已有理为零的平凡角色关系整提升，保实cusps、e₀/平均/S-unit transfer及R1132前提；不除12p。

[R1133](results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)实际A+B=1的half范数恢复全部原Vχ，保leading。显式Heis和同Norm见证class4 p⁵塔首层(a,a,a,b)已付；cusp iff四moment全零，即赋值向量∈(σ−1)^4，Norm只控M0。§10 Fourier/λp相位严格交换同一Heis商；纤维积保两三阶及两极端四阶(p⁷)，混合四阶零。常Lie中心读K₂/p的ω²，非e₀整torsion。原见证/跨轨道Cor/算术与proper下降继续。

[原跨line弦单位](notes/2026-11-28-original-cross-line-chord-unit-equations.md)：i仅E[p]索引，(P,aP,iP)给严格U+V=1；一次bar范数及全部θ相位/leading付两槽uχFχ/m、vχFχ/m。uχ=2[g(a+1)−g(a−1)]，g=(t²−δ)^r−t^(2r)；每actualχ有2≤a≤m使uχunit，第二槽保ψ₂²、不除κ₂。不保证两χ共a或第二槽unit。泛配置双tame只作范围，不能传实际cup；global正在做真实跨line交叉和/Manin组合。

[原aux-c整Manin](notes/2026-11-28-original-auxiliary-c-torsion-Manin-correlation.md)：原K₃付整三项式；双κ同选奇c<p为unit、辅助域度p单位。§7第二K₃与O值1把完整Cor移回p点：𝒫=2c²{M_a,M_b}−2c⁴C_ab，C_ab=Σi<j(ai bj−bi aj){(xi−xj)/d0,hi/hj}。两次{-1,h}成对整消、C排序仅二扭。原权/配置cross仍须付，不能设C零或改c⁴−[c,c]；个别hc有Hodge权，augmentation才消权。

[R1136](results/R1136-original-forced-compact-Manin-sources.md)原forced双权逐det消边界，J双对偶/两负号及p+1 transfer准确落原正商；独立和为2(p−1)eθ读数，rank1来自Γ1p、diamond θ²含quadratic例外。物理σℓ修正给I_(2j+2k+2)，四阶指定非重复邻对不落低混合消块门。保全部cyclic-n correlation与未付operator/twist；同z bar-cross变{A,R}仍非零。

## O1：指定 U^m、原 Picard 两 jet 与真实三同源

[原Tate normal-FM](notes/2026-11-27-original-Tate-three-torsion-normal-FM-variation.md) §§1–16保原Miller/Verschiebung、kerV/−Q刚化、全自然基与P/N连接。6v dot t̂=ΦN_full f；全V₀低阶共轭已排，指定U^m未排。首normal×Picard一/四阶零而normal零阶unit。真实Prym族Y²=−(3x+ε)(x³+2v)给完整θ及rank2 Gauss，θ为终止ε₂F₁，cup1/(9v)；moving三挠不代fixed Picard，period仅<p安全、首共振p+1。

全族Dε^p=HεDε、DεΨε=HεU−βε；加律保−HM，dotR保全S_(p−3)/常数。Ψε(Q)=(εH−ε^p)/6，二阶公式已付。§16完整普通Picard连接为(D_R+h_Z)T̂[f]=T̂[(Ψε+H D_T)f]，实际M div=V*O−pO、Hc=−DlogM、c(FQ)=−ε/6；保moving-zero的HD_T与全部高极输出。p-curvature只核尺度。[R1137](results/R1137-original-Lame-conjugation-with-complete-boundaries.md)付D₀/Λ全部rank3端点、D⁴的δ⁴c_N及原U/B/C完整变换，指定φ满足2Λ³φ+3ΨΛ²φ+6Φ(V)φ+3δΨ=0。Λ非局部D，moving p极仍保；继续真正两jet消元。

§15固定E_P上Ξ=d(xR/r)+3v(R/r²)ωP、Υ=−3R²ωP读3e、−3K4；proper高极p次自由项按CM权排。两类在同一CM线，不能用全rank2完美性。完整Fermat矩给e=vΣr_iL_i、K4=Σr_ir_jL_(i+j+1)，前k矩unit、后k零；**两原和非同时零仍开**。

[原Prym三同源/trace](notes/2026-11-28-original-fixed-Prym-three-isogeny-and-trace.md)：τ(A,B)=(ζA,ζ²B)，φ=(q/ρ²,w/2)，φ*ωE=−3ρ⁻²ωP。A*=Tr(R/r²)/3、B*=TrR²/3准确读e/v、K4，顶项3ρ⁻²U^(m−1)、U^(p−1)。§6真实ψ=(2v/(ρ²x),−svr/x)给φ=[−s]ψ；A³=2(V−v),B³=2(V+v)，LA=LB=0且W=−2ρ²v，原trace已写成同一E的CM[-s] trace。§7原genus4二次源W²=x²+4r²的branch不被τ保持，不能提升；完整Norm=U³+125v²/4非平方，三条平移cover必须保留。

[原genus4全局Raynaud](notes/2026-11-28-original-genus-four-global-Raynaud-vanishing.md)：实际degree3商y³=(2/κ)(1−η⁶)，四基全Cartier-zero；μ6×μ3排第四基的三对。原ω↦h及absolute负号给e=3ρsδA，再消费e0 iffS0，得到e0 iff全局β恒零。Y非hyperelliptic，不反用单向引理，也不把四维isotropic当矛盾。

[原Lamé续稿](notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)的短旗标/Green/全Newton/纯极Φ及R1113完整Lamé谱已付；相邻单位、零谱投影、R1130相邻δ都不代指定两jet。R1126六CM十五配对保A/S/T，Pfaffian不含S；R1060非CMordinary不推S；旧至500000窗口不重扫。

[R1134](results/R1134-original-single-source-low-Euler-obstruction.md)四个原输入的十五列Euler小类全rank，真实run/hash已消费，勿重跑；有限结论不外推。

## O2：原 Gaussian good-mask 与共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md) p4k3且p|Bp−3时χ2 coarse一次斜率unit，只付跨盘。剩余p∤Bp−3；盘内还需原高度。[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)constant iff ord_bG_v≥s，degree=(s−ord)/2，非constant≥max{3,floor(p/96)+2}，不推独立/纤维唯一。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md) §§7–9保全gauge/低卷积/高尾，f_n=−Θ^nG_v/(n!(v)_n)及有限Möbius点对差，仅weight≤p−3。Θ^p在SS=δ²∂w，不横向微分单点对等式。原有限本征重建已把h≥1长尾消成L−2h单位逆，全部centered矩阵由原principal唯一重建；ξ标量化保全binomial及P=0，h0不外推。见[新原重建](notes/2026-11-28-original-Gaussian-finite-contiguity-and-spectral-reconstruction.md)；o2已付R² Newton商；R1135双低指标分支同一frame非对角pair至多一对，另支Δ_low/48仍待非零，保跨twist/P=0。R1135§§5–7的原norm2三乘积与安全残数准确消V₂：c₃=−40G_(p−3)+25H+8a³V₃/81−4a⁴V₄/243；V₃/V₄、Δ_low仍开。

## 已完成与永久边界

[R1125](results/R1125-original-full47-rational-point-classification.md)完整47Q恰八CM，所有高度/whole盘及独立审计均成。真实run/hash沿归档保留，不重跑47/41/旧窗口。

同h仍须本原/Legendre/fi gj两mask。R971 full-span、R1006全p稳定已否，特定A/E4/mark仍开。R948仅有限Abel零集，候选MW像可非零；原σ/cY、η_h、d/N、nonp/Poincaré/splitting不可删。R907原artifact真404，不据摘要重造；R1004导子下界不代高度上界。O3–6全部准确输入与旧断点见open及逐字归档。主标准不变，继续。
