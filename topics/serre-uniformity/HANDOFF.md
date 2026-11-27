# Serre 一致性交接

## 目标、认领、规则

绝对常数C使全部无CM E/Q在p>C时模p满射，或给p→∞完整反例族。**主目标OPEN，未达课题README完成标准；继续，不等阶段回复。**

会话 **Astra-serre-24b8836b-20261126**。已部分克隆并真实pull main，读根/课题README及H/open/log/notes；私库QUEUE认领已推233f74794091dd015c3868cb8f2b57c15fec2c63，私库规则36cf1ed2已读。不得重做登记结论/窗口。

**公开两README已读提交：6c5de852b9e6c6b974cffeca3edcc5791df3f781**（2026-11-28 04:41 Asia/Taipei；终端失效后连接器同步main，两README无差异；最近真实pull为01:48）。每次同步检查两README diff，至少每小时；变化只读差异即执行。

最近真实pull 2026-11-27 01:48 Asia/Taipei；04:21重试仍无可用执行环境，shell未启动。按根规则8连接器同步、读diff、expected_sha非force提交，拒绝立即同步重基重推至成功；环境恢复立即pull --rebase。下一次真实尝试不晚于2026-11-28 05:21。令牌只CLI。数学程序仅本公开仓库Actions；本地/V8仅metadata/文本，不作数学计算。[此前偏差纠正](notes/2026-11-26-execution-path-deviation-and-correction.md)。

root管main/H/open/index/log，子研究仅独立candidate；每条结论即推。H<10KB，open尽量<30KB，每MD<100KB，topic<200MB；不存可重算raw/artifact/Release，不写根LOG。[最新逐字前态](handoff-archive-2026-11-28-before-exact-Pade-top.md)沿链保完整旧公式、source/run/hash；[open](open.md)/[索引](results.md)为完整入口。旧“R1003 norm3准备中”未交，现R1003为范围纠错。

## O0：完整一般 p 与原算术 cochain

[R1003](results/R1003-global-scope-and-remaining-branches.md)保完整N_ns；R317的整j/固定K/σ1/二三小域和小惯性C³均未删。[R1128](results/R1128-all-prime-linear-good-cuspidal-rank.md)原good≥floor(p/16)+3、forced Ω(p/logp)；原候选O(p^1.5logp)，有界惰性CM不推Q-CM。[R1112](results/R1112-original-simultaneous-cuspidal-Frobenius-selection.md)已付同时非零与导子/判别式，选素界仍不够；[R1115](results/R1115-original-cuspidal-nonintegral-j-branches-and-denominator-Frobenius.md)仍容−1modp整支。一般p排点未成。

R1131的原forced高偶r，在B_(4j+2)/B_(p−1−4j)单位门内锁真实rank2非split/Fricke+，radical β_(4j+2)，奇K有理p∞及指定规范整K₂角色消零。R1132的低偶r两Bernoulli门迫full块w负，原正商该块零；r2须Bp−3单位，p7mod8指定r由二次类数无条件。整Chen/Ohta、全cusp平均与原rational-zero单位关系已成；这些结论均不代任意K₂/p杯积零。

[R1133](results/R1133-original-primitive-unit-equations-and-Heisenberg-source.md)原half范数、Heis/class4 p⁵塔与Fourier交换已成；cusp须四moments，Norm仅M0；p⁷纤维积只保两极端四阶。原aux-c/跨line全部cross及ψ₂²保于open/前态；常Lie中心ω²非e₀整torsion。四阶proper/arithmetic继续。

[R1136](results/R1136-original-forced-compact-Manin-sources.md)原两秩紧致源、J/transfer/θ² diamond、ordinary Hecke及rank1 exact p²/Fricke+ twist全成（保quadratic-St）；整away-p order、source unsmoothing不代全field关系。[R1138](results/R1138-original-integral-bare-cup-smoothing-comparison.md)原除子/augmentation付全部n>3的S_n=(4/m²)V_n{Fχ,Fψ}，V_n=n⁴−n^(a+2)T_n+n^(2a+1)，两cross完整。[R1139](results/R1139-original-compact-target-unsmoothing-and-bare-cup.md)明确F33低mixed门下付HS/base/Pic全部target公共核消去，原裸cup=指定Ψ(c)；值未零，四阶指定邻对在门外。

[R1140](results/R1140-original-low-weight-Manin-source-reduction.md)原j1,k2：C¹=0、C²=(16δ²/21)C_Eis，实际Merel/det/apolar给λℓ=ℓ⁻²+ℓ³。无门已有β=β_E+β₈，v_n=n⁻¹¹(n⁵−1)(n¹⁰−1)，β_E=S_n/v_n，V_nβ₈0；B16/B_(p−15)单位才删β₈。§§10–12真实degree-p norm不反除p，trace-fixed付24常数，一次Galois/Cartan权u⁴v⁸，fixed-Weil n⁻⁴与两cross准确给β_E=16δ² V_n₀𝒯{W*G₄,G₈}/(21m²v₀)。§13已付该bare trace在原X_K的全部cusp tame，F33内cup=(4δ²/21)𝒯{W*G₄,G₈}，可去V投影；门外仍保compact I8差。实际标量不造F0。

[R1141](results/R1141-original-arithmetic-endpoint-and-circular-unit-cup.md)在p∤B_(p−5)时，原arith-compact θ=ω⁻⁶的整个I3像=span{Fχ1,βχ2}（允许零）。全S={p}延拓/Hecke闭包、BrS0、完整Pic商、DVR与MW可除项的真实socle提升均成；Q下降ω5→V→ω10，B10单位删商H¹。再B16/B_(p−15)门得∃c原cup{F1,F2/ε2^c}=0于fieldK₂/p；c未定，proper Pic H²障碍仍保。root继续该Pic结构，global继续实际p-isogeny常数/cochains。

## O1：原 U^m 的两 jet 与精确 Padé

[R1137](results/R1137-original-Lame-conjugation-with-complete-boundaries.md)原D₀/Λ rank3边界、U/B/C完整共轭及指定2Λ³φ+3ΨΛ²φ+6Φ(V)φ+3δΨ=0已成；Λ非局部D、moving p极不可删。§2整差商/相对Cartier/碰撞值χ(−Q)=−d0/v给实际Padé：
N=(p−5)/6，Q=H(−v²x)、P=−J(−v²x)/a0，
QF−P的contact恰2N+1且首余项unit，F=₂F₁(1/3,1/2;4/3)=√(1−x)G_N。
原e/K4双零 iff Q0=Q1=0，P亦含x²；约后deg≤N−2/contact2N−1。§2.5新付P_N=−2(v²)^(2N+1)(2/3)_N/(7/6)_N unit，degP=N；不单独排二次缺陷。o1继续原相邻Hankel/Pearson/旁列。

原Tate normal-FM的普通连接保HD_T及全部高极；固定Prym三同源φ=[−s]ψ、完整trace与Fermat矩已成，Ξ/Υ同一CM线，不能由完美性推e/K4非同时零。genus4 Y非hyperelliptic且e0 iff全βY0，单向引理不反用。R1113完整谱、R1130相邻δ、R1126六CM配对、R1060非CM ordinary及所有旧窗口只消费；R1134四输入十五Euler列fullrank及run/hash已成，不重跑。上述准确公式/links见open和前态。

## O2：原 Gaussian 全 good-mask 与共同纤维

[R1127](results/R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md) p4k3且p|Bp−3时χ2 coarse一次unit只付跨盘，盘内仍须原高度；剩余p∤Bp−3。[R1129](results/R1129-linear-many-nonconstant-original-Gaussian-profiles.md)线性多个非constant不代独立/注入。

[R1116](results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)与[原有限重建](notes/2026-11-28-original-Gaussian-finite-contiguity-and-spectral-reconstruction.md)保全gauge/常数/高尾/实际mask，付h≥1的L−2h逆、R² Newton商与完整principal；h0不外推，Θ^p在SS非零。

[R1135](results/R1135-original-Gaussian-low-row-fiber-constraint.md)双低good分支至多一个非对角unordered pair；另一支Δ_low/48尚待unit。norm2准确消V₂后保V₃/V₄；另两二同源只给原偶band对角运输，旁unit在CM gauge抵消。§10两实际下降线已真运输：α^p=iα、t*′=it*、z′=−z；δ′=ηδ；Kronecker γ′=ηγ、N_R′=η⁻¹N_R，Weil γ_W/bχ保持。完整核与i0给Π′(z′)=Π(−z′)，同component两线统一z∈Fp；保S0/P0，不合并其他components。o2继续全部good余对或Δ。

## 已成、禁止重做与其它入口

[R1125](results/R1125-original-full47-rational-point-classification.md)原完整47Q恰八CM，全部4513 whole盘/高度/全维来源和后到q²审计已成，不重跑47/41/旧端值窗口；run/hash沿原文/归档。

同h仍须本原/Legendre/fi gj实际mask。R971 full-span、R1006全p稳定已否，特定A/E4/mark未否；R948仅有限Abel零集，MW像可非零；原σ/cY、η_h、d/N、nonp/Poincaré/splitting不能删。R907原artifact真404，不据摘要重造；R1004导子下界不代高度上界。O3–6完整断点见open/归档。主标准未变，继续。
